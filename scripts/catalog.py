"""Shared catalog rules, room colors, and stable anchors for every generated view."""

from __future__ import annotations

import re
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

ROOT = Path(__file__).resolve().parents[1]
REPO = "XUJay111/awesome-ai2-thor"
SITE_URL = "https://xujay111.github.io/awesome-ai2-thor/"
ACTIVE_STATUSES = {"verified-paper", "verified-project", "tutorial"}
FORBIDDEN_PHRASES = (
    "it is included as", "is included from the primary arxiv record",
    "explicitly connects", "explicitly names", "reports experiments connected to",
    "evaluates agent methods on alfworld, the text-game", "this work uses",
    "important", "novel", "comprehensive", "state-of-the-art",
)

# The category names stay stable for existing contributors and incoming links.
# (category, URL key, label, Chinese label, room name, fill, description, Chinese description)
ROOMS = [
    ("Platforms and Environment Generation", "platforms", "Platforms and environment generation", "平台与环境生成", "Foyer", "#E4E3DD", "Simulators and generated worlds.", "模拟器与场景生成。"),
    ("Benchmarks and Evaluation", "benchmarks", "Benchmarks and evaluation", "基准与评测", "Study", "#DDBFC2", "Shared tasks, safety, and evaluation protocols.", "任务、安全与评测协议。"),
    ("Instruction Following and Household Tasks", "instructions", "Instruction following and household tasks", "指令跟随与家务任务", "Kitchen", "#B7CBB0", "ALFRED, TEACh, and language-grounded execution.", "ALFRED、TEACh 与语言驱动的执行。"),
    ("Navigation", "navigation", "Navigation", "导航", "Living room", "#DCCFB8", "ObjectNav, exploration, and sim-to-real transfer.", "目标导航、探索与仿真迁移。"),
    ("Planning, Memory, and Multi-Agent Systems", "planning", "Planning, memory, and multi-agent systems", "规划、记忆与多智能体", "Dining", "#CABEAA", "Replanning, spatial memory, and collaboration.", "重规划、空间记忆与协作。"),
    ("RL-Trained VLM Agents", "rl-agents", "RL-trained VLM agents", "强化学习训练的 VLM 智能体", "Bedroom", "#C5C8E0", "Policy training and embodied reasoning.", "策略训练与具身推理。"),
    ("Perception, Physics, and Scene Graphs", "perception", "Perception, physics, and scene graphs", "感知、物理与场景图", "Bathroom", "#A8D1D3", "Objects, affordances, and physical reasoning.", "物体、可供性与物理推理。"),
    ("Datasets and Assets", "datasets", "Datasets and assets", "数据集与资产", "Storage", "#E4E3DD", "Scene corpora, object assets, and task data.", "场景、物体资产与任务数据。"),
    ("Tools and Environments", "tools", "Tools and environments", "工具与环境", "Garage", "#D2D1CB", "Training frameworks, wrappers, and utilities.", "训练框架、封装与实用工具。"),
    ("Tutorials and Notes", "tutorials", "Tutorials and notes", "教程与笔记", "Closet", "#E4E3DD", "Installation, first scenes, and reproducible baselines.", "安装、首个场景与可复现基线。"),
]
ROOM_BY_CATEGORY = {room[0]: room for room in ROOMS}
ROOM_BY_KEY = {room[1]: room for room in ROOMS}
SHORT_LABELS = {
    'platforms': ('Platforms', '平台'), 'benchmarks': ('Benchmarks', '基准'),
    'instructions': ('Instructions', '指令'), 'navigation': ('Navigation', '导航'),
    'planning': ('Planning', '规划'), 'rl-agents': ('RL agents', '强化学习'),
    'perception': ('Perception', '感知'), 'datasets': ('Datasets', '数据'),
    'tools': ('Tools', '工具'), 'tutorials': ('Tutorials', '教程'),
}


def load_data(path: Path | None = None) -> dict:
    return yaml.safe_load((path or ROOT / "data.yml").read_text(encoding="utf-8"))


def today() -> date:
    return datetime.now(ZoneInfo("Asia/Shanghai")).date()


def active_entries(data: dict) -> list[dict]:
    return [e for e in data["entries"] if e.get("status") in ACTIVE_STATUSES]


def native_entries(data: dict) -> list[dict]:
    return [e for e in active_entries(data) if e["scope"] == "thor-native"]


def slugify(text: str) -> str:
    # Match the existing GitHub heading anchors, including repeated hyphens.
    return re.sub(r"\s+", "-", re.sub(r"[^\w\s-]", "", text.lower()).strip())


def entry_anchor(entry: dict) -> str:
    return slugify(entry["title"])


def is_new(entry: dict, as_of: date) -> bool:
    return 0 <= (as_of - date.fromisoformat(entry["added"])).days <= 30


def sort_entries(entries: list[dict]) -> list[dict]:
    # Newest year first; inside a year the newest arXiv record leads, so the
    # "Latest entries" tables really show the latest work.
    return sorted(entries, key=lambda e: (-int(e["year"] or 0), tuple(-n for n in arxiv_id(e)), e["title"].casefold()))


ARXIV_ID = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4})\.(\d{4,5})")


def arxiv_id(entry: dict) -> tuple[int, int]:
    """(yymm, number) of the entry's arXiv record, or (0, 0) when it has none."""
    for url in entry["links"].values():
        match = ARXIV_ID.search(str(url))
        if match:
            return int(match[1]), int(match[2])
    return 0, 0


def papers_through(entries: list[dict]) -> str:
    """Latest arXiv month covered by the catalog, e.g. '2026-10'."""
    yymm = max((arxiv_id(e)[0] for e in entries), default=0)
    return f"20{yymm // 100:02d}-{yymm % 100:02d}" if yymm else ""


def recent_first(entries: list[dict]) -> list[dict]:
    """Newest additions first; within one batch, newest arXiv record first."""
    return sorted(entries, key=lambda e: (e["added"], arxiv_id(e), e["title"]), reverse=True)


REAL_VENUE_EXCLUDE = {"platform", "official docs", "documentation", "code", "dataset", "challenge", "framework"}


def display_venue(entry: dict) -> str:
    venue = (entry.get("venue") or "").strip()
    return "" if venue.lower() in REAL_VENUE_EXCLUDE else venue


def room_counts(entries: list[dict]) -> Counter:
    return Counter(e["category"] for e in entries if e["scope"] == "thor-native")


def ecosystem_counts(entries: list[dict]) -> Counter:
    return Counter(env for e in entries for env in e["env"])


def banned_phrases(text: str) -> list[str]:
    return [phrase for phrase in FORBIDDEN_PHRASES if re.search(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", text, re.I)]


def floorplan_layout(counts: Counter) -> dict[str, tuple[float, float, float, float]]:
    """Two wings around a corridor, with area driven by native entry counts.

    A small minimum width keeps labels legible in the storage rooms. The larger
    rooms remain proportional; no adjacent-only entries affect these dimensions.
    """
    top = ["navigation", "instructions", "planning", "rl-agents"]
    bottom = ["platforms", "benchmarks", "perception", "tools", "datasets", "tutorials"]
    weights = {r[1]: max(counts[r[0]], 1) for r in ROOMS}
    upper_fraction = sum(weights[k] for k in top) / sum(weights.values())
    upper_h = max(165, min(212, 304 * upper_fraction))
    result = {}
    for keys, y, height in [(top, 24, upper_h), (bottom, 24 + upper_h + 24, 304 - upper_h)]:
        available = 1152 - 8 * (len(keys) - 1)
        minimum = 92 if keys == bottom else 130
        spare = available - len(keys) * minimum
        x = 24.0
        for key in keys:
            width = minimum + spare * weights[key] / sum(weights[k] for k in keys)
            result[key] = (x, y, width, height)
            x += width + 8
    return result
