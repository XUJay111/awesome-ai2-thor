#!/usr/bin/env python3
"""Audit catalog titles against arXiv metadata; optionally open a review Issue."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from difflib import SequenceMatcher
import json
import os
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import urlencode
import xml.etree.ElementTree as ET

import yaml

from scan_arxiv import ArxivClient, GitHub, NS, QueryError, markdown_text, normalized

ROOT = Path(__file__).resolve().parents[1]
BATCH_SIZE = 50
THRESHOLD = 0.6
# These entries name methods/environments rather than the linked paper's title.
TITLE_WHITELIST = frozenset({'hlsm', 'map-thor', 'infinity-thor'})
ID_RE = re.compile(
    r'arxiv\.org/(?:abs|pdf|html)/((?:\d{4}\.\d{4,5}|[a-z][a-z.-]+/\d{7}))(?:v\d+)?', re.I)


def normalize_title(title: str) -> str:
    title = unicodedata.normalize('NFKC', title).casefold()
    return ' '.join(re.sub(r'[\W_]+', ' ', title).split())


def title_similarity(expected: str, actual: str) -> float:
    return SequenceMatcher(None, normalize_title(expected), normalize_title(actual), autojunk=False).ratio()


def whitelisted(title: str) -> bool:
    # Also recognize the catalog's expanded "HLSM: ..." method entry.
    return title.split(':', 1)[0].strip().casefold() in TITLE_WHITELIST


def catalog_titles(path: Path) -> dict[str, list[str]]:
    data = yaml.safe_load(path.read_text(encoding='utf-8'))
    titles: dict[str, list[str]] = {}
    for entry in data['entries']:
        ids = {identifier for url in entry.get('links', {}).values()
               for identifier in ID_RE.findall(str(url))}
        for identifier in sorted(ids):
            titles.setdefault(identifier, []).append(entry['title'])
    return titles


def fetch_titles(client: ArxivClient, identifiers: list[str]) -> dict[str, str]:
    params = urlencode({'id_list': ','.join(identifiers), 'max_results': BATCH_SIZE})
    try:
        feed = ET.fromstring(client.fetch('https://export.arxiv.org/api/query?' + params))
    except ET.ParseError as exc:
        raise QueryError('Invalid Atom response') from exc
    titles = {}
    for entry in feed.findall('a:entry', NS):
        ids = ID_RE.findall(entry.findtext('a:id', '', NS))
        if len(ids) != 1 or ids[0] not in identifiers:
            raise QueryError('arXiv returned an unexpected or API error entry')
        title = normalized(entry.findtext('a:title', '', NS))
        if title:
            titles[ids[0]] = title
    return titles


def verify(client: ArxivClient, catalog: dict[str, list[str]]) -> dict:
    report = {'ids': len(catalog), 'checked': 0, 'whitelisted': 0,
              'mismatches': [], 'failures': {}}
    identifiers = sorted(catalog)
    for start in range(0, len(identifiers), BATCH_SIZE):
        batch = identifiers[start:start + BATCH_SIZE]
        try:
            actual = fetch_titles(client, batch)
        except QueryError as exc:
            report['failures'].update({identifier: str(exc) for identifier in batch})
            continue
        for identifier in batch:
            if identifier not in actual:
                report['failures'][identifier] = 'No title returned by arXiv'
                continue
            for expected in catalog[identifier]:
                if whitelisted(expected):
                    report['whitelisted'] += 1
                    continue
                report['checked'] += 1
                score = title_similarity(expected, actual[identifier])
                if score < THRESHOLD:
                    report['mismatches'].append({'arxiv_id': identifier, 'catalog_title': expected,
                                                 'arxiv_title': actual[identifier], 'similarity': score})
    return report


def issue_body(report: dict) -> str:
    lines = [f"Checked {report['checked']} catalog titles against {report['ids']} arXiv IDs; "
             f"{report['whitelisted']} method/environment titles whitelisted.",
             f'Title similarity below {THRESHOLD} needs human review. No catalog entries were changed.', '']
    for mismatch in report['mismatches']:
        lines += [f"- **{markdown_text(mismatch['catalog_title'])}** · "
                  f"[arXiv:{mismatch['arxiv_id']}](https://arxiv.org/abs/{mismatch['arxiv_id']}) · "
                  f"similarity {mismatch['similarity']:.3f}",
                  f"  - arXiv title: {markdown_text(mismatch['arxiv_title'])}", '']
    if report['failures']:
        lines += ['### IDs that could not be verified', '']
        lines += [f'- {identifier}: {markdown_text(reason)}' for identifier, reason in report['failures'].items()]
        lines.append('')
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=ROOT / 'data.yml')
    parser.add_argument('--output', type=Path, help='Optional JSON audit report')
    parser.add_argument('--repository', default=os.getenv('GITHUB_REPOSITORY'))
    parser.add_argument('--create-issue', action='store_true')
    args = parser.parse_args()
    token = os.getenv('GH_TOKEN') or os.getenv('GITHUB_TOKEN')
    if args.create_issue and not (args.repository and token):
        parser.error('--create-issue requires a repository and GH_TOKEN or GITHUB_TOKEN')
    report = verify(ArxivClient(), catalog_titles(args.data))
    body = issue_body(report)
    print(body)
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    if os.getenv('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as summary:
            summary.write(body)
    if args.create_issue and report['mismatches']:
        as_of = datetime.now(timezone.utc).date()
        issue = GitHub(args.repository, token).create_issue(
            f"arXiv title audit {as_of}: {len(report['mismatches'])} mismatches", body,
            label='arxiv-title-audit', description='Catalog titles that differ from arXiv metadata')
        print('Created ' + issue['html_url'])
    if report['failures']:
        print('Some IDs could not be verified; see the report above.', file=sys.stderr)
        return 2
    return 1 if report['mismatches'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
