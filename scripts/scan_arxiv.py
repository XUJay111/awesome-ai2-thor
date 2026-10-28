#!/usr/bin/env python3
"""Find arXiv candidates; publishing an Issue is opt-in and never edits data.yml."""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from datetime import date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
import html
import json
import os
from pathlib import Path
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

import yaml

ROOT = Path(__file__).resolve().parents[1]
QUERIES = {
    '"AI2-THOR"': ('AI2-THOR',),
    'iTHOR': ('iTHOR',),
    'RoboTHOR': ('RoboTHOR',),
    'ProcTHOR': ('ProcTHOR',),
    'ManipulaTHOR': ('ManipulaTHOR',),
    'ArchitecTHOR': ('ArchitecTHOR',),
    'ALFRED AND embodied': ('ALFRED', 'embodied'),
    '"EB-ALFRED"': ('EB-ALFRED',),
    'EmbodiedBench': ('EmbodiedBench',),
    'TEACh AND embodied': ('TEACh', 'embodied'),
    'Holodeck AND embodied': ('Holodeck', 'embodied'),
    'Objaverse AND THOR': ('Objaverse', 'THOR'),
    'SPOC AND robot': ('SPOC', 'robot'),
    'CHORES AND robot': ('CHORES', 'robot'),
    'ALFWorld': ('ALFWorld',),
}
NS = {'a': 'http://www.w3.org/2005/Atom',
      'o': 'http://a9.com/-/spec/opensearch/1.1/'}
ID_RE = re.compile(r'(?:arxiv\.org/(?:abs|pdf|html)/|arXiv:\s*)(\d{4}\.\d{4,5})(?:v\d+)?', re.I)
USER_AGENT = 'awesome-ai2-thor arXiv scanner (https://github.com/XUJay111/awesome-ai2-thor)'


def arxiv_ids(text: str) -> set[str]:
    return set(ID_RE.findall(text))


def catalog_ids(path: Path) -> set[str]:
    data = yaml.safe_load(path.read_text(encoding='utf-8'))
    return {identifier for e in data['entries'] for url in e.get('links', {}).values()
            for identifier in arxiv_ids(str(url))}


def normalized(text: str) -> str:
    return ' '.join(text.split())


def has_term(text: str, term: str) -> bool:
    pattern = re.escape(term).replace(r'\-', r'[-\u2010-\u2015]')
    return bool(re.search(r'(?<!\w)' + pattern + r'(?!\w)', text, re.I))


def matches(summary: str) -> list[str]:
    return [label for label, terms in QUERIES.items()
            if all(has_term(summary, term) for term in terms)]


def evidence_sentence(summary: str, labels: list[str]) -> str:
    sentences = re.split(r'(?<=[.!?])\s+', normalized(summary))
    terms = [QUERIES[label][0] for label in labels]
    return next((s for s in sentences if any(has_term(s, term) for term in terms)), '')


@dataclass
class Paper:
    arxiv_id: str
    title: str
    submitted: str
    summary: str
    matched: list[str]
    evidence: str

    @property
    def alfworld_only(self) -> bool:
        return self.matched == ['ALFWorld']


class QueryError(RuntimeError):
    pass


class ArxivClient:
    """One client serializes pages and retries, with >=3 seconds between calls."""
    def __init__(self):
        self.last_request: float | None = None

    def fetch(self, url: str) -> bytes:
        delay = 0.0
        for attempt in range(4):  # Initial request plus three retries.
            if self.last_request is not None:
                delay = max(delay, 3 - (time.monotonic() - self.last_request))
            if delay > 0:
                time.sleep(delay)
            self.last_request = time.monotonic()
            try:
                with urlopen(Request(url, headers={'User-Agent': USER_AGENT}), timeout=60) as response:
                    return response.read()
            except HTTPError as exc:
                if exc.code != 429 and not 500 <= exc.code < 600:
                    raise QueryError(f'HTTP {exc.code}') from exc
                if attempt == 3:
                    raise QueryError(f'HTTP {exc.code} after 3 retries') from exc
                delay = 3 * 2 ** attempt
                retry_after = exc.headers.get('Retry-After')
                if retry_after:
                    try:
                        delay = max(delay, float(retry_after))
                    except ValueError:
                        try:
                            delay = max(delay, (parsedate_to_datetime(retry_after) - datetime.now(timezone.utc)).total_seconds())
                        except (TypeError, ValueError):
                            pass
            except (URLError, TimeoutError, OSError) as exc:
                if attempt == 3:
                    raise QueryError(f'{type(exc).__name__} after 3 retries') from exc
                delay = 3 * 2 ** attempt
        raise AssertionError('unreachable')

    def papers(self, label: str, since: date, until: date):
        abstract_query = ' AND '.join(f'abs:"{term}"' for term in QUERIES[label])
        query = f'({abstract_query}) AND submittedDate:[{since:%Y%m%d}0000 TO {until:%Y%m%d}2359]'
        start = 0
        while True:
            params = urlencode({'search_query': query, 'start': start, 'max_results': 100,
                                'sortBy': 'submittedDate', 'sortOrder': 'descending'})
            try:
                feed = ET.fromstring(self.fetch('https://export.arxiv.org/api/query?' + params))
            except ET.ParseError as exc:
                raise QueryError('Invalid Atom response') from exc
            entries = feed.findall('a:entry', NS)
            total = int(feed.findtext('o:totalResults', str(len(entries)), NS))
            for entry in entries:
                ids = arxiv_ids(entry.findtext('a:id', '', NS))
                if not ids:
                    raise QueryError('arXiv returned an API error entry')
                submitted = entry.findtext('a:published', '', NS)[:10]
                if not submitted:
                    raise QueryError('arXiv entry has no submission date')
                if not since.isoformat() <= submitted <= until.isoformat():
                    continue
                summary = normalized(entry.findtext('a:summary', '', NS))
                labels = matches(summary)
                evidence = evidence_sentence(summary, labels)
                if labels and evidence:
                    yield Paper(next(iter(ids)), normalized(entry.findtext('a:title', '', NS)),
                                submitted, summary, labels, evidence)
            start += len(entries)
            if start >= total:
                break
            if not entries:
                raise QueryError('Incomplete arXiv pagination')


class GitHub:
    def __init__(self, repository: str, token: str):
        if not re.fullmatch(r'[\w.-]+/[\w.-]+', repository):
            raise ValueError('Expected owner/repository')
        self.base = f'https://api.github.com/repos/{repository}'
        self.token = token

    def request(self, path: str, payload=None):
        request = Request(self.base + path,
                          data=json.dumps(payload).encode() if payload is not None else None,
                          headers={'Authorization': f'Bearer {self.token}',
                                   'Accept': 'application/vnd.github+json',
                                   'Content-Type': 'application/json',
                                   'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': USER_AGENT})
        with urlopen(request, timeout=60) as response:
            return json.load(response)

    def previous_ids(self) -> set[str]:
        known = set()
        page = 1
        while True:
            issues = self.request(f'/issues?labels=arxiv-scan&state=all&per_page=100&page={page}')
            for issue in issues:
                if 'pull_request' not in issue:
                    known.update(arxiv_ids(issue.get('body') or ''))
            if len(issues) < 100:
                return known
            page += 1

    def create_issue(self, title: str, body: str):
        try:
            self.request('/labels/' + quote('arxiv-scan', safe=''))
        except HTTPError as exc:
            if exc.code != 404:
                raise
            self.request('/labels', {'name': 'arxiv-scan', 'color': '2D5BE3',
                                     'description': 'arXiv candidates awaiting human review'})
        return self.request('/issues', {'title': title, 'body': body, 'labels': ['arxiv-scan']})


def markdown_text(text: str) -> str:
    return re.sub(r'([\\`*_[\]])', r'\\\1', html.escape(normalized(text), quote=False))


def issue_body(papers: list[Paper], failures: dict[str, str], since: date, until: date) -> str:
    lines = [f'Candidates submitted {since} to {until} that mention an AI2-THOR-family environment.',
             'Tick the ones to add, then ask for them to be entered in data.yml.', '']
    for adjacent, heading in [(False, 'Simulator family'), (True, 'ALFWorld only (text environment)')]:
        group = [p for p in papers if p.alfworld_only == adjacent]
        if not group:
            continue
        lines += [f'### {heading}', '']
        for paper in group:
            labels = ', '.join(paper.matched)
            lines += [f'- [ ] **[{markdown_text(paper.title)}](https://arxiv.org/abs/{paper.arxiv_id})** · {paper.submitted} · matched: {markdown_text(labels)}',
                      f'  > "{markdown_text(paper.evidence)}"', '']
    if failures:
        lines += ['### Queries that did not finish', '']
        lines += [f'- {markdown_text(label)} ({markdown_text(reason)})' for label, reason in failures.items()]
        lines.append('')
    return '\n'.join(lines)


def scan(client: ArxivClient, labels: list[str], since: date, until: date, known: set[str]):
    candidates = {}
    failures = {}
    for label in labels:
        try:
            for paper in client.papers(label, since, until):
                if paper.arxiv_id not in known:
                    candidates[paper.arxiv_id] = paper
        except QueryError as exc:
            failures[label] = str(exc)
    return sorted(candidates.values(), key=lambda p: (p.submitted, p.arxiv_id), reverse=True), failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--as-of', type=date.fromisoformat, default=datetime.now(timezone.utc).date())
    parser.add_argument('--since', type=date.fromisoformat)
    parser.add_argument('--query', choices=list(QUERIES), action='append')
    parser.add_argument('--data', type=Path, default=ROOT / 'data.yml')
    parser.add_argument('--output', type=Path, help='Optional JSON research report')
    parser.add_argument('--repository', default=os.getenv('GITHUB_REPOSITORY'))
    parser.add_argument('--create-issue', action='store_true')
    args = parser.parse_args()
    since = args.since or args.as_of - timedelta(days=14)
    if since > args.as_of:
        parser.error('--since must be on or before --as-of')
    token = os.getenv('GH_TOKEN') or os.getenv('GITHUB_TOKEN')
    if args.create_issue and not (args.repository and token):
        parser.error('--create-issue requires a repository and GH_TOKEN or GITHUB_TOKEN')
    github = GitHub(args.repository, token) if args.repository and token else None
    known = catalog_ids(args.data)
    if github:
        known.update(github.previous_ids())  # Abort on failed deduplication; never post duplicates.
    papers, failures = scan(ArxivClient(), args.query or list(QUERIES), since, args.as_of, known)
    body = issue_body(papers, failures, since, args.as_of)
    print(body if papers or failures else 'No new candidates; no Issue created.')
    if args.output:
        args.output.write_text(json.dumps({'since': str(since), 'until': str(args.as_of),
                                          'candidates': [asdict(p) for p in papers],
                                          'failures': failures}, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    if args.create_issue and papers:
        issue = github.create_issue(f'arXiv scan {args.as_of}: {len(papers)} candidates', body)
        print('Created ' + issue['html_url'])
    if os.getenv('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as summary:
            summary.write(body if papers or failures else 'No new candidates; no Issue created.\n')
    if failures:
        print(f'{len(failures)} queries did not finish; see the report above.', file=sys.stderr)
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
