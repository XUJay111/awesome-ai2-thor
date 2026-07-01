"""Shared link metadata for validation and README generation."""

from __future__ import annotations


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

PRIMARY_LINKS = set(LINK_ORDER)
DUPLICATE_CHECK_LINKS = {"paper", "arxiv", "acl_anthology"}

RESOURCE_TYPES = {
    "papers": ["paper", "arxiv", "acl_anthology"],
    "project pages": ["project"],
    "code repositories": ["code", "official_code", "sgclip_code"],
    "datasets": ["dataset", "dataset_tools"],
    "challenges/workshops": ["challenge", "workshop"],
    "tutorials/notes": ["tutorial", "note"],
}
