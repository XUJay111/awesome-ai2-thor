#!/usr/bin/env python3
"""Generate README.md from data.yml."""

from __future__ import annotations

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data.yml"
README_PATH = ROOT / "README.md"

LAST_VERIFIED = "2026-06"

CATEGORY_NOTES = {
    "Platforms and Environment Generation": "Core simulators, generated environments, and official ecosystem extensions.",
    "Benchmarks and Evaluation": "Benchmarks, challenges, and evaluation interfaces with a concrete AI2-THOR-family connection.",
    "Instruction Following and Household Tasks": "Instruction-following, household-task, and language-grounded execution methods using ALFRED, TEACh, or AI2-THOR-style tasks.",
    "Navigation": "ObjectNav, semantic navigation, and navigation-analysis work evaluated in AI2-THOR-family environments.",
    "Planning, Memory, and Multi-Agent Systems": "Planning, memory, dialogue, assistance, and multi-agent systems grounded in AI2-THOR-derived tasks.",
    "RL-Trained VLM Agents": "VLM-agent training and reinforcement-learning work whose evaluation includes AI2-THOR-family benchmarks.",
    "Perception, Physics, and Scene Graphs": "Perception, physical reasoning, and scene-graph work relevant to AI2-THOR-style embodied interaction.",
    "Datasets and Assets": "Datasets, assets, and derived benchmark resources for AI2-THOR-family workflows.",
    "Tools and Environments": "Wrappers, infrastructure, visualization tools, and community environments for AI2-THOR-family research.",
    "Tutorials and Notes": "Secondary and community learning resources. Prefer primary paper, project, or code links for academic entries.",
}

LINK_ORDER = [
    "paper",
    "project",
    "code",
    "dataset",
    "challenge",
    "workshop",
    "acl_anthology",
    "arxiv",
    "tutorial",
    "note",
    "official_code",
    "dataset_tools",
    "sgclip_code",
]

LINK_LABELS = {
    "paper": "Paper",
    "project": "Project",
    "code": "Code",
    "dataset": "Dataset",
    "challenge": "Challenge",
    "workshop": "Workshop",
    "acl_anthology": "ACL Anthology",
    "arxiv": "arXiv",
    "tutorial": "Tutorial",
    "note": "Note",
    "official_code": "Official code",
    "dataset_tools": "Dataset tools",
    "sgclip_code": "SGCLIP Code",
}


def slugify(heading: str) -> str:
    slug = heading.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug.strip())
    return slug


def load_data() -> dict:
    with DATA_PATH.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise SystemExit("data.yml must contain a mapping with an entries list")
    return data


def render_links(links: dict) -> str:
    parts: list[str] = []
    seen = set()
    for key in LINK_ORDER:
        value = links.get(key)
        if value:
            parts.append(f"[{LINK_LABELS[key]}]({value})")
            seen.add(key)
    for key, value in links.items():
        if key not in seen and value:
            label = key.replace("_", " ").title()
            parts.append(f"[{label}]({value})")
    return " · ".join(parts)


def render_entry(entry: dict) -> list[str]:
    tags = entry.get("tags") or []
    lines = [
        f"### {entry['title']}",
        "",
    ]
    if tags:
        lines.extend([" ".join(f"`{tag}`" for tag in tags), ""])
    lines.extend(
        [
            f"Links: {render_links(entry['links'])}",
            "",
            entry["summary"].strip(),
            "",
        ]
    )
    return lines


def render_readme(data: dict) -> str:
    entries = [
        entry
        for entry in data["entries"]
        if entry.get("status") not in {"needs-verification", "out-of-scope"}
    ]
    categories = list(dict.fromkeys(entry["category"] for entry in entries))

    lines = [
        "# Awesome AI2-THOR",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)",
        "[![Link Check](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/link-check.yml/badge.svg)](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/link-check.yml)",
        "[![Data Validation](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/validate-data.yml/badge.svg)](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/validate-data.yml)",
        "",
        f"Maintained as a curated research index. Last verified: {data.get('last_verified', LAST_VERIFIED)}.",
        "",
        "A curated map of papers, benchmarks, datasets, environments, and tools built on top of [AI2-THOR](https://ai2thor.allenai.org/) and its ecosystem, including iTHOR, RoboTHOR, ProcTHOR, ManipulaTHOR, ArchitecTHOR, ALFRED, TEACh, and EmbodiedBench.",
        "",
        "This is an AI2-THOR-family index, not a general embodied AI awesome list. Each entry should make its AI2-THOR-family connection clear through primary paper, project, or code links whenever possible.",
        "",
        "## Contents",
        "",
    ]

    lines.extend(f"- [{category}](#{slugify(category)})" for category in categories)
    lines.append("")

    for category in categories:
        lines.extend([f"## {category}", ""])
        note = CATEGORY_NOTES.get(category)
        if note:
            lines.extend([f"*{note}*", ""])
        for entry in entries:
            if entry["category"] == category:
                lines.extend(render_entry(entry))

    lines.extend(
        [
            "## Contributing",
            "",
            "Edit `data.yml` first, then regenerate this README:",
            "",
            "```bash",
            "python scripts/validate_data.py",
            "python scripts/generate_readme.py",
            "```",
            "",
            "Entry format:",
            "",
            "```markdown",
            "### Title",
            "",
            "`year` `venue/status` `topic` `ecosystem`",
            "",
            "Links: [Paper](paper-url) · [Project](project-url) · [Code](repo-url)",
            "",
            "One concise paragraph explaining how the work uses, extends, benchmarks, or supports AI2-THOR-family systems.",
            "```",
            "",
            "See [CONTRIBUTING.md](CONTRIBUTING.md) for scope, verification rules, status labels, and review policy.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    data = load_data()
    README_PATH.write_text(render_readme(data), encoding="utf-8")


if __name__ == "__main__":
    main()
