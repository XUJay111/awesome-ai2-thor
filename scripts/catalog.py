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
    ("Platforms and Environment Generation", "platforms", "Platforms and environment generation", "平台与环境生成", "Foyer", "#E8E4DA", "Simulators and generated worlds.", "模拟器与场景生成。"),
    ("Benchmarks and Evaluation", "benchmarks", "Benchmarks and evaluation", "基准与评测", "Study", "#EBD3D5", "Shared tasks, safety, and evaluation protocols.", "任务、安全与评测协议。"),
    ("Instruction Following and Household Tasks", "instructions", "Instruction following and household tasks", "指令跟随与家务任务", "Kitchen", "#D3E0CC", "ALFRED, TEACh, and language-grounded execution.", "ALFRED、TEACh 与语言驱动的执行。"),
    ("Navigation", "navigation", "Navigation", "导航", "Living room", "#EADCC3", "ObjectNav, exploration, and sim-to-real transfer.", "目标导航、探索与仿真迁移。"),
    ("Planning, Memory, and Multi-Agent Systems", "planning", "Planning, memory, and multi-agent systems", "规划、记忆与多智能体", "Dining", "#F1D9C8", "Replanning, spatial memory, and collaboration.", "重规划、空间记忆与协作。"),
    ("RL-Trained VLM Agents", "rl-agents", "RL-trained VLM agents", "强化学习训练的 VLM 智能体", "Bedroom", "#D8D9EE", "Policy training and embodied reasoning.", "策略训练与具身推理。"),
    ("Perception, Physics, and Scene Graphs", "perception", "Perception, physics, and scene graphs", "感知、物理与场景图", "Bathroom", "#C9E2E2", "Objects, affordances, and physical reasoning.", "物体、可供性与物理推理。"),
    ("Datasets and Assets", "datasets", "Datasets and assets", "数据集与资产", "Storage", "#E4E1D6", "Scene corpora, object assets, and task data.", "场景、物体资产与任务数据。"),
    ("Tools and Environments", "tools", "Tools and environments", "工具与环境", "Garage", "#DCDBD5", "Training frameworks, wrappers, and utilities.", "训练框架、封装与实用工具。"),
    ("Tutorials and Notes", "tutorials", "Tutorials and notes", "教程与笔记", "Closet", "#ECE5D8", "Installation, first scenes, and reproducible baselines.", "安装、首个场景与可复现基线。"),
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


PLAN_BOX = (24.0, 24.0, 1176.0, 344.0)  # exterior wall centerlines
HALL_HEIGHT = 34.0
TOP_WING = ["navigation", "planning", "instructions", "benchmarks"]
BOTTOM_WING = ["platforms", "perception", "rl-agents", "tools", "datasets", "tutorials"]


def floorplan_layout(counts: Counter) -> dict[str, tuple[float, float, float, float]]:
    """Rooms on two wings of a hallway, sharing walls like a real plan.

    Rectangles are wall-centerline cells. Areas follow entry counts on a
    compressed scale (count ** 0.85) so the closet stays usable while the
    living room still reads as the largest space.
    """
    x0, y0, x1, y1 = PLAN_BOX
    weights = {r[1]: max(counts[r[0]], 1) ** 0.85 for r in ROOMS}
    top_w = sum(weights[k] for k in TOP_WING)
    rooms_h = (y1 - y0) - HALL_HEIGHT
    upper_h = max(150.0, min(168.0, rooms_h * top_w / sum(weights.values())))
    result = {}
    for keys, y, height, minimum in [
        (TOP_WING, y0, upper_h, 150.0),
        (BOTTOM_WING, y0 + upper_h + HALL_HEIGHT, rooms_h - upper_h, 104.0),
    ]:
        spare = (x1 - x0) - minimum * len(keys)
        total = sum(weights[k] for k in keys)
        x = x0
        for key in keys:
            width = minimum + spare * weights[key] / total
            result[key] = (x, y, width, height)
            x += width
    return result


def hallway(layout: dict) -> tuple[float, float, float, float]:
    """The hallway cell between the two wings of a layout."""
    x0, _, x1, _ = PLAN_BOX
    top = layout[TOP_WING[0]]
    return x0, top[1] + top[3], x1 - x0, HALL_HEIGHT
