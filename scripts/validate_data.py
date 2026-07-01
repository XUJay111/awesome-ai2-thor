#!/usr/bin/env python3
"""Validate data.yml for the Awesome AI2-THOR index."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

import yaml

from link_schema import DUPLICATE_CHECK_LINKS, PRIMARY_LINKS


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data.yml"

VALID_STATUS = {
    "verified-paper",
    "verified-project",
    "tutorial",
    "needs-verification",
    "out-of-scope",
}

VALID_CATEGORIES = {
    "Platforms and Environment Generation",
    "Benchmarks and Evaluation",
    "Instruction Following and Household Tasks",
    "Navigation",
    "Planning, Memory, and Multi-Agent Systems",
    "RL-Trained VLM Agents",
    "Perception, Physics, and Scene Graphs",
    "Datasets and Assets",
    "Tools and Environments",
    "Tutorials and Notes",
}

REQUIRED_FIELDS = {
    "title",
    "year",
    "status",
    "venue",
    "category",
    "tags",
    "links",
    "ai2thor_connection",
    "summary",
    "last_verified",
}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MONTH_RE = re.compile(r"^\d{4}-\d{2}$")
YEAR_RE = re.compile(r"^\d{4}$")
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?")


def active_entry(entry: dict) -> bool:
    return entry.get("status") not in {"needs-verification", "out-of-scope"}


def load_data() -> dict:
    try:
        with DATA_PATH.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except FileNotFoundError:
        raise SystemExit("data.yml not found")
    if not isinstance(data, dict) or not isinstance(data.get("entries"), list):
        raise SystemExit("data.yml must contain an entries list")
    return data


def is_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def minimum_last_verified(data: dict) -> str | None:
    value = data.get("last_verified")
    if isinstance(value, str):
        if DATE_RE.match(value):
            return value
        if MONTH_RE.match(value):
            return f"{value}-01"
    return None


def normalized_arxiv_id(url: str) -> str | None:
    match = ARXIV_RE.search(url)
    if match:
        return match.group(1)
    return None


def validate_entry(index: int, entry: dict, minimum_verified: str | None) -> list[str]:
    label = entry.get("title", f"entry #{index + 1}")
    errors: list[str] = []

    missing = REQUIRED_FIELDS - set(entry)
    if missing:
        errors.append(f"{label}: missing fields: {', '.join(sorted(missing))}")

    title = entry.get("title")
    if not isinstance(title, str) or not title.strip():
        errors.append(f"{label}: title must be non-empty")

    year = entry.get("year")
    if year is not None and (not isinstance(year, int) and not (isinstance(year, str) and YEAR_RE.match(year))):
        errors.append(f"{label}: year must be a four-digit year or null")

    status = entry.get("status")
    if status not in VALID_STATUS:
        errors.append(f"{label}: invalid status {status!r}")

    category = entry.get("category")
    if category not in VALID_CATEGORIES:
        errors.append(f"{label}: invalid category {category!r}")

    venue = entry.get("venue")
    if venue is not None and (not isinstance(venue, str) or not venue.strip()):
        errors.append(f"{label}: venue must be a non-empty string or null")

    tags = entry.get("tags")
    if (
        not isinstance(tags, list)
        or not tags
        or not all(isinstance(tag, str) and tag.strip() for tag in tags)
    ):
        errors.append(f"{label}: tags must be a non-empty list of strings")

    links = entry.get("links")
    if not isinstance(links, dict) or not links:
        errors.append(f"{label}: links must be a non-empty mapping")
    else:
        for key, value in links.items():
            if not isinstance(key, str) or not isinstance(value, str) or not value.strip():
                errors.append(f"{label}: link keys and values must be non-empty strings")
            elif not is_url(value):
                errors.append(f"{label}: link {key!r} is not an http(s) URL: {value}")
        if not PRIMARY_LINKS.intersection(links):
            errors.append(f"{label}: must include at least one primary link")

    connection = entry.get("ai2thor_connection")
    if not isinstance(connection, str) or not connection.strip():
        errors.append(f"{label}: ai2thor_connection must be non-empty")

    summary = entry.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        errors.append(f"{label}: summary must be non-empty")
    elif "\n" in summary.strip():
        errors.append(f"{label}: summary must be one paragraph")
    elif status == "needs-verification":
        summary_lower = summary.lower()
        if "verify" not in summary_lower:
            errors.append(f"{label}: needs-verification summary must state what to verify")
        if len(summary.split()) < 8:
            errors.append(f"{label}: needs-verification summary must explain the verification gap")

    last_verified = entry.get("last_verified")
    if not isinstance(last_verified, str) or not DATE_RE.match(last_verified):
        errors.append(f"{label}: last_verified must use YYYY-MM-DD")
    elif active_entry(entry) and minimum_verified and last_verified < minimum_verified:
        errors.append(
            f"{label}: last_verified {last_verified} is older than top-level last_verified {minimum_verified}"
        )

    if category == "Tutorials and Notes" and status != "tutorial":
        errors.append(f"{label}: Tutorials and Notes entries must use tutorial status")
    if status == "tutorial" and category != "Tutorials and Notes":
        errors.append(f"{label}: tutorial status is only allowed in Tutorials and Notes")

    return errors


def validate_duplicates(entries: list[dict]) -> list[str]:
    errors: list[str] = []
    titles = Counter(entry.get("title") for entry in entries)
    for title, count in titles.items():
        if title and count > 1:
            errors.append(f"duplicate title: {title}")

    primary_urls: list[str] = []
    arxiv_ids: list[str] = []
    for entry in entries:
        if not active_entry(entry):
            continue
        links = entry.get("links") or {}
        for key in DUPLICATE_CHECK_LINKS:
            if key in links:
                primary_urls.append(links[key])
                arxiv_id = normalized_arxiv_id(links[key])
                if arxiv_id:
                    arxiv_ids.append(arxiv_id)
    url_counts = Counter(primary_urls)
    for url, count in url_counts.items():
        if count > 1:
            errors.append(f"duplicate primary link: {url}")
    arxiv_counts = Counter(arxiv_ids)
    for arxiv_id, count in arxiv_counts.items():
        if count > 1:
            errors.append(f"duplicate arXiv id: {arxiv_id}")
    return errors


def main() -> int:
    data = load_data()
    entries = data["entries"]
    minimum_verified = minimum_last_verified(data)
    errors: list[str] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"entry #{index + 1}: must be a mapping")
            continue
        errors.extend(validate_entry(index, entry, minimum_verified))
    errors.extend(validate_duplicates(entries))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    active_entries = [
        entry
        for entry in entries
        if isinstance(entry, dict) and active_entry(entry)
    ]
    print(f"Validated {len(entries)} total entries ({len(active_entries)} active).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
