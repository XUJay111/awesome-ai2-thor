import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse
from urllib.error import HTTPError
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import verify_arxiv_titles as verifier
from scan_arxiv import QueryError


def feed(titles):
    entries = ''.join(f'<entry><id>https://arxiv.org/abs/{identifier}v2</id>'
                      f'<title>{escape(title)}</title></entry>' for identifier, title in titles.items())
    return f'<feed xmlns="http://www.w3.org/2005/Atom">{entries}</feed>'.encode()


class VerifyTitleTests(unittest.TestCase):
    def test_catalog_keeps_all_entry_titles_but_deduplicates_ids_and_versions(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'data.yml'
            path.write_text('''entries:
- title: A title
  links:
    paper: https://arxiv.org/pdf/2610.12345v3.pdf
    arxiv: https://arxiv.org/abs/2610.12345
- title: Another entry for the same paper
  links:
    paper: https://arxiv.org/html/2610.12345v1
- title: Legacy paper
  links:
    paper: https://arxiv.org/abs/cs/0601001v2
''')
            self.assertEqual(verifier.catalog_titles(path), {
                '2610.12345': ['A title', 'Another entry for the same paper'],
                'cs/0601001': ['Legacy paper']})

    def test_batches_of_fifty_use_id_list_and_share_three_second_limiter(self):
        catalog = {f'2610.{n:05d}': [f'Paper {n}'] for n in range(101)}
        clock = [0.0]
        calls = []
        def open_request(request, **kwargs):
            params = parse_qs(urlparse(request.full_url).query)
            calls.append((clock[0], params))
            return io.BytesIO(feed({identifier: catalog[identifier][0]
                                    for identifier in params['id_list'][0].split(',')}))
        with patch('scan_arxiv.urlopen', side_effect=open_request), \
             patch('scan_arxiv.time.monotonic', side_effect=lambda: clock[0]), \
             patch('scan_arxiv.time.sleep', side_effect=lambda seconds: clock.__setitem__(0, clock[0] + seconds)):
            report = verifier.verify(verifier.ArxivClient(), catalog)
        self.assertEqual([len(p['id_list'][0].split(',')) for _, p in calls], [50, 50, 1])
        self.assertTrue(all(p['max_results'] == ['50'] and 'search_query' not in p for _, p in calls))
        self.assertTrue(all(b[0] - a[0] >= 3 for a, b in zip(calls, calls[1:])))
        self.assertEqual(report, {'ids': 101, 'checked': 101, 'whitelisted': 0, 'mismatches': [], 'failures': {}})

    def test_fuzzy_normalization_and_strict_threshold(self):
        self.assertEqual(verifier.title_similarity('AI2–THOR:  A MODEL!', 'ai2 thor a model'), 1)
        # Three out of five characters match: exactly 0.6 must not be flagged.
        catalog = {'2610.00001': ['abcde'], '2610.00002': ['abcde']}
        with patch.object(verifier.ArxivClient, 'fetch', return_value=feed({
                '2610.00001': 'abcxy', '2610.00002': 'abxyz'})):
            report = verifier.verify(verifier.ArxivClient(), catalog)
        self.assertEqual([m['arxiv_id'] for m in report['mismatches']], ['2610.00002'])
        self.assertAlmostEqual(report['mismatches'][0]['similarity'], 0.4)

    def test_only_named_method_and_environment_entries_are_whitelisted(self):
        names = ['HLSM', 'HLSM: Hierarchical Language-conditioned Spatial Model',
                 'MAP-THOR', 'infinity-THOR', 'HLSM-like method']
        catalog = {f'2610.{n:05d}': [name] for n, name in enumerate(names)}
        with patch.object(verifier.ArxivClient, 'fetch', return_value=feed({k: 'Unrelated title' for k in catalog})):
            report = verifier.verify(verifier.ArxivClient(), catalog)
        self.assertEqual(report['whitelisted'], 4)
        self.assertEqual(report['checked'], 1)
        self.assertEqual(report['mismatches'][0]['catalog_title'], 'HLSM-like method')

    def test_missing_metadata_and_api_errors_cannot_pass_silently(self):
        client = verifier.ArxivClient()
        for response in [b'invalid XML', feed({'error': 'API error'}), feed({}), feed({'2610.00001': ''})]:
            with self.subTest(response=response), patch.object(client, 'fetch', return_value=response):
                report = verifier.verify(client, {'2610.00001': ['A title']})
            self.assertIn('2610.00001', report['failures'])
        with patch.object(client, 'fetch', side_effect=QueryError('HTTP 429 after 3 retries')):
            report = verifier.verify(client, {'2610.00001': ['A title']})
        self.assertEqual(report['failures'], {'2610.00001': 'HTTP 429 after 3 retries'})

    def run_cli(self, path, args):
        with patch.object(sys, 'argv', ['verify_arxiv_titles.py', '--data', str(path), *args]), \
             patch.dict(verifier.os.environ, {'GH_TOKEN': 'test-token'}, clear=True), \
             patch('sys.stdout', new=io.StringIO()), patch('sys.stderr', new=io.StringIO()):
            return verifier.main()

    def test_cli_publishes_only_mismatches_and_never_edits_catalog(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'data.yml'
            path.write_text('entries:\n- title: A title\n  links:\n    paper: https://arxiv.org/abs/2610.00001\n')
            before = path.read_bytes()
            with patch.object(verifier.ArxivClient, 'fetch', return_value=feed({'2610.00001': 'Unrelated paper'})), \
                 patch.object(verifier.GitHub, 'create_issue', return_value={'html_url': 'https://github.com/test/repo/issues/1'}) as create:
                self.assertEqual(self.run_cli(path, []), 1)
                create.assert_not_called()
                self.assertEqual(self.run_cli(path, ['--create-issue', '--repository', 'test/repo']), 1)
                self.assertEqual(create.call_args.kwargs['label'], 'arxiv-title-audit')
                self.assertIn('Unrelated paper', create.call_args.args[1])
            with patch.object(verifier.ArxivClient, 'fetch', return_value=feed({'2610.00001': 'A title'})), \
                 patch.object(verifier.GitHub, 'create_issue') as create:
                self.assertEqual(self.run_cli(path, ['--create-issue', '--repository', 'test/repo']), 0)
                create.assert_not_called()
            with patch.object(verifier.ArxivClient, 'fetch', side_effect=QueryError('network unavailable')):
                self.assertEqual(self.run_cli(path, []), 2)
            self.assertEqual(path.read_bytes(), before)

    def test_audit_issue_gets_its_own_label(self):
        github = verifier.GitHub('test/repo', 'test-token')
        missing = HTTPError('https://api.github.com', 404, 'missing label', {}, None)
        with patch.object(github, 'request', side_effect=[missing, {}, {'html_url': 'issue'}]) as request:
            github.create_issue('Audit', 'Body', label='arxiv-title-audit', description='Review titles')
        self.assertEqual(request.call_args_list[0].args[0], '/labels/arxiv-title-audit')
        self.assertEqual(request.call_args_list[1].args[1]['name'], 'arxiv-title-audit')
        self.assertEqual(request.call_args_list[2].args[1]['labels'], ['arxiv-title-audit'])

    def test_report_escapes_untrusted_title_markup(self):
        report = {'ids': 1, 'checked': 1, 'whitelisted': 0, 'failures': {}, 'mismatches': [{
            'arxiv_id': '2610.00001', 'catalog_title': 'Title](https://evil.example)\n- [ ] injected',
            'arxiv_title': '<details>Fake</details>', 'similarity': 0.1}]}
        body = verifier.issue_body(report)
        self.assertNotIn('<details>', body)
        self.assertNotIn('\n- [ ]', body)


if __name__ == '__main__':
    unittest.main()
