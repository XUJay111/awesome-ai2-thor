import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import scan_arxiv as scanner
from datetime import date


def feed(identifier='2610.12345', summary='We evaluate in ProcTHOR houses.', total=1):
    entry = f'''<entry><id>https://arxiv.org/abs/{identifier}v2</id>
    <title>A real candidate</title><published>2026-10-25T00:00:00Z</published>
    <summary>{summary}</summary></entry>''' if identifier else ''
    return f'''<feed xmlns="http://www.w3.org/2005/Atom"
    xmlns:o="http://a9.com/-/spec/opensearch/1.1/">
    <o:totalResults>{total}</o:totalResults>{entry}</feed>'''.encode()


class ScanTests(unittest.TestCase):
    since = date(2026, 10, 14)
    until = date(2026, 10, 28)

    def test_abstract_queries_paginate_and_preserve_evidence(self):
        urls = []
        def fetch(url):
            urls.append(url)
            return feed('2610.12345' if len(urls) == 1 else '2610.12346', total=2)
        client = scanner.ArxivClient()
        with patch.object(client, 'fetch', side_effect=fetch):
            papers = list(client.papers('ProcTHOR', self.since, self.until))
        self.assertEqual([p.arxiv_id for p in papers], ['2610.12345', '2610.12346'])
        self.assertEqual(papers[0].evidence, 'We evaluate in ProcTHOR houses.')
        self.assertEqual(parse_qs(urlparse(urls[1]).query)['start'], ['1'])
        self.assertIn('abs:"ProcTHOR"', parse_qs(urlparse(urls[0]).query)['search_query'][0])
        self.assertNotIn('all:', urls[0])

    def test_date_filter_uses_submission_not_update_date(self):
        client = scanner.ArxivClient()
        old = feed().replace(b'2026-10-25', b'2026-09-25')
        with patch.object(client, 'fetch', return_value=old):
            self.assertEqual(list(client.papers('ProcTHOR', self.since, self.until)), [])

    def test_compound_queries_and_alfworld_group(self):
        self.assertNotIn('ALFRED AND embodied', scanner.matches('ALFRED is a person.'))
        self.assertIn('ALFRED AND embodied', scanner.matches('An embodied agent uses ALFRED.'))
        self.assertNotIn('iTHOR', scanner.matches('We use miniTHOR.'))
        only = scanner.Paper('2610.12345', 'Text tasks', '2026-10-25', '', ['ALFWorld'], 'Evaluate on ALFWorld.')
        both = scanner.Paper('2610.12346', 'Visual tasks', '2026-10-25', '', ['ProcTHOR', 'ALFWorld'], 'Evaluate on ProcTHOR and ALFWorld.')
        body = scanner.issue_body([only, both], {}, self.since, self.until)
        self.assertLess(body.index('Visual tasks'), body.index('### ALFWorld only'))
        self.assertGreater(body.index('Text tasks'), body.index('### ALFWorld only'))

    def test_dedup_catalog_versions_and_closed_issue_pagination(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'data.yml'
            path.write_text('entries:\n- links:\n    paper: https://arxiv.org/pdf/2610.12345v3.pdf\n')
            self.assertEqual(scanner.catalog_ids(path), {'2610.12345'})
        github = scanner.GitHub('test/repo', 'test-token')
        page = [{'body': 'https://arxiv.org/abs/2610.12346v1', 'state': 'closed'}] * 100
        with patch.object(github, 'request', side_effect=[page, [{'body': None}]]) as request:
            known = github.previous_ids()
        self.assertEqual(known, {'2610.12346'})
        self.assertIn('state=all', request.call_args_list[0].args[0])
        self.assertIn('page=2', request.call_args_list[1].args[0])

    def test_second_scan_skips_papers_already_posted(self):
        client = scanner.ArxivClient()
        with patch.object(client, 'fetch', return_value=feed()):
            first, errors = scanner.scan(client, ['ProcTHOR'], self.since, self.until, set())
            prior = scanner.arxiv_ids(scanner.issue_body(first, errors, self.since, self.until))
            second, errors = scanner.scan(client, ['ProcTHOR'], self.since, self.until, prior)
        self.assertEqual(len(first), 1)
        self.assertEqual(second, [])
        self.assertEqual(errors, {})

    def test_rate_limit_applies_to_successive_requests_and_all_retries(self):
        clock = [0.0]
        calls = []
        def sleep(seconds):
            clock[0] += seconds
        def open_request(*args, **kwargs):
            calls.append(clock[0])
            if len(calls) < 4:
                raise HTTPError('https://export.arxiv.org', 429, 'rate limited', {'Retry-After': '5'}, None)
            return io.BytesIO(b'feed')
        client = scanner.ArxivClient()
        with patch.object(scanner.time, 'monotonic', side_effect=lambda: clock[0]), \
             patch.object(scanner.time, 'sleep', side_effect=sleep), \
             patch.object(scanner, 'urlopen', side_effect=open_request):
            self.assertEqual(client.fetch('https://export.arxiv.org/api/query'), b'feed')
            client.fetch('https://export.arxiv.org/api/query')
        self.assertEqual(len(calls), 5)
        self.assertTrue(all(b - a >= 3 for a, b in zip(calls, calls[1:])))
        self.assertGreaterEqual(calls[1] - calls[0], 5)

    def test_failed_query_is_reported_after_exactly_three_retries(self):
        client = scanner.ArxivClient()
        error = HTTPError('https://export.arxiv.org', 429, 'rate limited', {}, None)
        with patch.object(scanner, 'urlopen', side_effect=error) as request, \
             patch.object(scanner.time, 'sleep'):
            papers, errors = scanner.scan(client, ['ProcTHOR'], self.since, self.until, set())
        self.assertEqual(request.call_count, 4)
        self.assertEqual(papers, [])
        self.assertEqual(errors, {'ProcTHOR': 'HTTP 429 after 3 retries'})
        self.assertIn('### Queries that did not finish', scanner.issue_body(papers, errors, self.since, self.until))

    def test_empty_scan_creates_no_issue_and_leaves_catalog_untouched(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'data.yml'
            path.write_text('entries: []\n')
            before = path.read_bytes()
            with patch.object(sys, 'argv', ['scan_arxiv.py', '--data', str(path), '--create-issue', '--repository', 'test/repo']), \
                 patch.dict(scanner.os.environ, {'GH_TOKEN': 'test-token'}), \
                 patch.object(scanner.GitHub, 'previous_ids', return_value=set()), \
                 patch.object(scanner.GitHub, 'create_issue') as create, \
                 patch.object(scanner, 'scan', return_value=([], {})), \
                 patch('sys.stdout', new=io.StringIO()):
                self.assertEqual(scanner.main(), 0)
            create.assert_not_called()
            self.assertEqual(path.read_bytes(), before)

    def test_metadata_cannot_inject_checkboxes_or_links(self):
        paper = scanner.Paper('2610.12345', 'Title](https://evil.example)\n- [ ] injected', '2026-10-25', '', ['ProcTHOR'], '<script>x</script>\n### Heading')
        body = scanner.issue_body([paper], {}, self.since, self.until)
        self.assertEqual(body.count('\n- [ ]'), 1)
        self.assertNotIn('<script>', body)
        self.assertNotIn('\n### Heading', body)


if __name__ == '__main__':
    unittest.main()
