#!/usr/bin/env python3
"""Generate README.md from data.yml."""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import yaml

from link_schema import LINK_LABELS, LINK_ORDER, RESOURCE_TYPES


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

ECOSYSTEM_PATTERNS = {
    "AI2-THOR / iTHOR": ["ai2-thor", "ithor"],
    "RoboTHOR": ["robothor"],
    "ProcTHOR": ["procthor"],
    "ManipulaTHOR": ["manipulathor"],
    "ArchitecTHOR": ["architecthor"],
    "ALFRED": ["alfred"],
    "TEACh": ["teach"],
    "EmbodiedBench": ["embodiedbench", "eb-alfred", "eb-navigation", "eb-manipulation"],
    "MAP-THOR / MAT-THOR": ["map-thor", "mat-thor", "mat2-thor"],
    "Other THOR variants": ["dualthor", "infinity-thor"],
}

TASK_PATTERNS = {
    "Instruction following": ["instruction", "alfred", "household task"],
    "Navigation / ObjectNav": ["navigation", "objectnav", "object-goal"],
    "Planning and memory": ["planning", "planner", "memory", "replanning"],
    "Multi-agent collaboration": ["multi-agent", "multi agent", "collaborative", "collaboration"],
    "Manipulation": ["manipulation", "mobile manipulation", "arm"],
    "Rearrangement / tidying": ["rearrangement", "tidying", "tidy"],
    "Dialogue and assistance": ["dialogue", "chat", "assistive", "assistance"],
    "Safety and physical reasoning": ["safety", "hazard", "physics", "physical"],
    "Scene generation and assets": ["generation", "procedural", "asset", "objaverse"],
}


RESEARCH_MAP = [
    (
        "Simulators and generated worlds",
        "AI2-THOR, RoboTHOR, ProcTHOR, ManipulaTHOR, ArchitecTHOR, and generated-scene extensions.",
        ["Platforms and Environment Generation", "Datasets and Assets"],
    ),
    (
        "Benchmarks and safety",
        "Shared tasks, challenge infrastructure, robustness checks, and safety-oriented evaluations.",
        ["Benchmarks and Evaluation"],
    ),
    (
        "ObjectNav and RoboTHOR",
        "Object-goal navigation, zero-shot navigation, semantic maps, and sim-to-real navigation analysis.",
        ["Navigation", "Tools and Environments"],
    ),
    (
        "ALFRED and TEACh",
        "Instruction following, dialogue-grounded household tasks, and long-horizon execution.",
        ["Instruction Following and Household Tasks", "Benchmarks and Evaluation"],
    ),
    (
        "LLM/VLM embodied agents",
        "Foundation-model agents, RL-trained VLM agents, prompting, reasoning, and closed-loop evaluation.",
        ["RL-Trained VLM Agents", "Planning, Memory, and Multi-Agent Systems"],
    ),
    (
        "Planning, memory, and collaboration",
        "Search, replanning, memory systems, multi-agent coordination, and human-agent assistance.",
        ["Planning, Memory, and Multi-Agent Systems"],
    ),
    (
        "Perception and physical reasoning",
        "Scene graphs, affordances, spatial understanding, physics, reconstruction, and interaction perception.",
        ["Perception, Physics, and Scene Graphs"],
    ),
    (
        "Tools and reproducibility",
        "Simulator wrappers, training code, evaluation harnesses, documentation, and community utilities.",
        ["Tools and Environments", "Tutorials and Notes"],
    ),
]

CURATED_ROUTES = [
    (
        "New to AI2-THOR",
        "Start with the simulator, official docs, and a benchmark overview before diving into task-specific papers.",
        ["AI2-THOR: An Interactive 3D Environment for Visual AI", "AI2-THOR Documentation", "EmbodiedBench: Comprehensive Benchmarking MLLMs for Vision-Driven Embodied Agents"],
    ),
    (
        "ObjectNav and RoboTHOR",
        "Follow the path from sim-to-real navigation to ObjectNav evaluation and modern zero-shot navigation methods.",
        ["RoboTHOR: An Open Simulation-to-Real Embodied AI Platform", "AllenAct ObjectNav Tutorial", "Simple but Effective: CLIP Embeddings for Embodied AI"],
    ),
    (
        "ALFRED / TEACh instruction following",
        "Use the benchmark papers and official resources to understand household task execution and dialogue-grounded agents.",
        ["ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks", "TEACh: Task-driven Embodied Agents that Chat", "ALFRED Documentation and Leaderboards"],
    ),
    (
        "ProcTHOR and scene generation",
        "Track procedural scale, generated assets, and language-guided environment creation.",
        ["ProcTHOR: Large-Scale Embodied AI Using Procedural Generation", "ProcTHOR-10K Repository", "Holodeck: Language Guided Generation of 3D Embodied AI Environments"],
    ),
    (
        "LLM/VLM embodied agents",
        "Compare planner benchmarks, foundation-model agents, memory, and RL-based embodied reasoning.",
        ["LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents", "Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making", "Embodied-Reasoner"],
    ),
]


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


def entry_search_text(entry: dict) -> str:
    fields = [
        entry.get("title", ""),
        entry.get("category", ""),
        entry.get("ai2thor_connection", ""),
        entry.get("summary", ""),
        " ".join(entry.get("tags") or []),
    ]
    return " ".join(fields).lower()


def count_patterns(entries: list[dict], patterns: dict[str, list[str]]) -> Counter:
    counts: Counter = Counter()
    for entry in entries:
        text = entry_search_text(entry)
        for label, terms in patterns.items():
            if any(term in text for term in terms):
                counts[label] += 1
    return counts


def render_count_list(counts: Counter, order: list[str] | None = None) -> str:
    labels = order or [label for label, _ in counts.most_common()]
    return ", ".join(f"{label} ({counts[label]})" for label in labels if counts.get(label))


def make_entry_anchor(entry: dict) -> str:
    return slugify(entry["title"])


def entry_link(entry: dict) -> str:
    return f"[{entry['title']}](#{make_entry_anchor(entry)})"


def entry_recency_key(entry: dict) -> tuple[str, str]:
    links = entry.get("links") or {}
    link_text = " ".join(str(value) for value in links.values())
    arxiv_match = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4})\.(\d{4,5})(?:v\d+)?", link_text)
    if arxiv_match:
        return (arxiv_match.group(1), arxiv_match.group(2))
    year = str(entry.get("year") or "")
    return (year if year.isdigit() else "0000", entry["title"].lower())


def render_at_a_glance(entries: list[dict], total_entries: int) -> list[str]:
    paper_count = sum(
        1
        for entry in entries
        if any(key in (entry.get("links") or {}) for key in RESOURCE_TYPES["papers"])
    )
    code_count = sum(
        1
        for entry in entries
        if any(key in (entry.get("links") or {}) for key in RESOURCE_TYPES["code repositories"])
    )
    recent_count = sum(
        1
        for entry in entries
        if str(entry.get("year") or "").isdigit() and int(entry["year"]) >= 2024
    )
    ecosystem_count = len(count_patterns(entries, ECOSYSTEM_PATTERNS))

    return [
        "## At a Glance",
        "",
        "| Metric | Count |",
        "| --- | ---: |",
        f"| Active README entries | {len(entries)} |",
        f"| Total tracked entries | {total_entries} |",
        f"| Paper entries | {paper_count} |",
        f"| Entries with code repositories | {code_count} |",
        f"| 2024-2026 entries | {recent_count} |",
        f"| AI2-THOR-family ecosystems represented | {ecosystem_count} |",
        "",
    ]


def render_research_map() -> list[str]:
    lines = [
        "## Research Map",
        "",
        "| Direction | Use This For | Sections |",
        "| --- | --- | --- |",
    ]
    for direction, description, sections in RESEARCH_MAP:
        section_links = ", ".join(f"[{section}](#{slugify(section)})" for section in sections)
        lines.append(f"| {direction} | {description} | {section_links} |")
    lines.append("")
    return lines


def render_curated_routes(entries: list[dict]) -> list[str]:
    by_title = {entry["title"]: entry for entry in entries}
    lines = ["## Curated Routes", ""]
    for route, description, titles in CURATED_ROUTES:
        route_entries = [by_title[title] for title in titles if title in by_title]
        if not route_entries:
            continue
        links = " -> ".join(entry_link(entry) for entry in route_entries)
        lines.extend([f"### {route}", "", description, "", links, ""])
    return lines


def render_recent_frontier(entries: list[dict]) -> list[str]:
    recent_entries = sorted(
        [
            entry
            for entry in entries
            if str(entry.get("year") or "") in {"2025", "2026"}
        ],
        key=entry_recency_key,
        reverse=True,
    )[:12]
    if not recent_entries:
        return []
    lines = ["## Recent Frontier", ""]
    lines.extend(
        f"- {entry.get('year')}: {entry_link(entry)}"
        for entry in recent_entries
    )
    lines.append("")
    return lines


def render_project_index(entries: list[dict], total_entries: int, categories: list[str]) -> list[str]:
    category_counts = Counter(entry["category"] for entry in entries)
    status_counts = Counter(entry["status"] for entry in entries)
    year_counts = Counter(str(entry.get("year") or "unknown") for entry in entries)
    ecosystem_counts = count_patterns(entries, ECOSYSTEM_PATTERNS)
    task_counts = count_patterns(entries, TASK_PATTERNS)
    resource_counts = Counter()
    for entry in entries:
        links = entry.get("links") or {}
        for label, keys in RESOURCE_TYPES.items():
            if any(key in links for key in keys):
                resource_counts[label] += 1

    known_years = sorted(year for year in year_counts if year.isdigit())
    unknown_years = year_counts.get("unknown", 0)
    year_text = ", ".join(f"{year} ({year_counts[year]})" for year in known_years)
    if unknown_years:
        year_text = f"{year_text}, unknown ({unknown_years})" if year_text else f"unknown ({unknown_years})"

    lines = [
        "## Project Index",
        "",
        f"- Coverage: {len(entries)} active entries across {len(categories)} sections ({total_entries} total tracked entries).",
        f"- Status mix: {render_count_list(status_counts)}.",
        f"- Timeline: {year_text}.",
        f"- Ecosystems: {render_count_list(ecosystem_counts, list(ECOSYSTEM_PATTERNS))}.",
        f"- Task themes: {render_count_list(task_counts, list(TASK_PATTERNS))}.",
        f"- Resources: {render_count_list(resource_counts, list(RESOURCE_TYPES))}.",
        "",
        "Section counts:",
        "",
    ]
    lines.extend(
        f"- [{category}](#{slugify(category)}): {category_counts[category]}"
        for category in categories
    )
    lines.append("")
    return lines


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
        "[![Markdown](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/markdown.yml/badge.svg)](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/markdown.yml)",
        "[![Link Check](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/link-check.yml/badge.svg)](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/link-check.yml)",
        "[![Data Validation](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/validate-data.yml/badge.svg)](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/validate-data.yml)",
        "",
        f"Maintained as a curated research index. Last verified: {data.get('last_verified', LAST_VERIFIED)}.",
        "",
        "A curated map of papers, benchmarks, datasets, environments, and tools built on top of [AI2-THOR](https://ai2thor.allenai.org/) and its ecosystem, including iTHOR, RoboTHOR, ProcTHOR, ManipulaTHOR, ArchitecTHOR, ALFRED, TEACh, and EmbodiedBench.",
        "",
        "This is an AI2-THOR-family index, not a general embodied AI awesome list. Each entry should make its AI2-THOR-family connection clear through primary paper, project, or code links whenever possible.",
        "",
    ]

    lines.extend(render_at_a_glance(entries, len(data["entries"])))
    lines.extend(render_research_map())
    lines.extend(render_curated_routes(entries))
    lines.extend(render_recent_frontier(entries))
    lines.extend(render_project_index(entries, len(data["entries"]), categories))
    lines.extend(["## Contents", ""])
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
