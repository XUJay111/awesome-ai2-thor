"""Behavioral checks for curation boundaries, generated coverage, and anchors."""
from copy import deepcopy
from datetime import date
import json
from pathlib import Path
import re
import sys
import unittest
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from catalog import (
    ROOT, ROOMS, active_entries, entry_anchor, floorplan_layout,
    is_new, load_data, native_entries, room_counts, today,
)
from generate_readme import render_readme
from validate_data import validate_curation, validate_entry
from generate_assets import darken


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_data()
        cls.native = native_entries(cls.data)
        cls.active = active_entries(cls.data)

    def test_new_window_includes_boundaries_but_not_future_dates(self):
        as_of = date(2026, 10, 28)
        for added, expected in [("2026-10-28", True), ("2026-09-28", True), ("2026-09-27", False), ("2026-10-29", False)]:
            with self.subTest(added=added):
                self.assertEqual(is_new({"added": added}, as_of), expected)

    def test_scope_isolation_and_date_not_publication_year_drive_new(self):
        data = deepcopy(self.data)
        native = next(e for e in data["entries"] if e["scope"] == "thor-native")
        adjacent = next(e for e in data["entries"] if e["scope"] == "alfworld-adjacent")
        native["added"] = adjacent["added"] = "2026-10-28"
        for zh in (False, True):
            content = render_readme(data, zh, date(2026, 10, 28))
            recent = content.split("## 最近新增" if zh else "## What's new", 1)[1].split("## ", 1)[0]
            self.assertIn(native["title"], recent)
            self.assertNotIn(adjacent["title"], recent)
        counts = room_counts(active_entries(data))
        adjacent["scope"] = "thor-native"
        self.assertEqual(sum(room_counts(active_entries(data)).values()), sum(counts.values()) + 1)

    def test_all_active_entries_have_one_stable_anchor_in_each_readme(self):
        for zh in (False, True):
            content = render_readme(self.data, zh, today())
            anchors = re.findall(r'<a id="([^"]+)"', content)
            headings = re.findall(r"^#### (.+)$", content, re.M)
            from catalog import slugify
            anchors += [slugify(title) for title in headings]
            self.assertEqual(len(anchors), len(set(anchors)))
            for entry in self.active:
                self.assertIn(entry_anchor(entry), anchors, entry["title"])
            for target in re.findall(r"\]\(#([^\)]+)\)", content):
                self.assertIn(target, anchors + [slugify(r[0]) for r in ROOMS])
            self.assertLess(len(content.splitlines()), 900)

    def test_invalid_prose_and_adjacent_must_reads_are_rejected(self):
        original = self.native[0]
        for key, value in [("short", "word " * 16), ("highlight", "word " * 31), ("short", "This work uses a simulator"), ("added", "2026-02-30"), ("must_read", "true")]:
            entry = deepcopy(original)
            entry[key] = value
            self.assertTrue(validate_entry(0, entry, None), key)
        entry = deepcopy(original)
        entry.update(scope="alfworld-adjacent", env=["ALFWorld"], section="planning", category=ROOMS[4][0])
        self.assertTrue(any("must_read" in error for error in validate_entry(0, entry, None)))

    def test_editorial_rule_does_not_change_official_paper_titles(self):
        entry = deepcopy(self.native[0])
        entry["title"] = "A Comprehensive Study of Novel Object Navigation"
        self.assertFalse(validate_entry(0, entry, None))
        entry["highlight"] = "A comprehensive and novel approach."
        self.assertTrue(validate_entry(0, entry, None))

    def test_each_room_has_two_to_four_native_must_reads(self):
        self.assertFalse(validate_curation(self.active))
        changed = deepcopy(self.active)
        for entry in changed:
            if entry["category"] == ROOMS[0][0]:
                entry["must_read"] = False
        self.assertTrue(validate_curation(changed))

    def test_dynamic_floorplan_counts_and_largest_room(self):
        counts = room_counts(self.native)
        layout = floorplan_layout(counts)
        areas = {key: value[2] * value[3] for key, value in layout.items()}
        self.assertEqual(max(areas, key=areas.get), "navigation")
        changed = counts.copy()
        changed[ROOMS[0][0]] += 10
        self.assertNotEqual(floorplan_layout(changed), layout)
        self.assertEqual(set(layout), {room[1] for room in ROOMS})

    def test_outlined_assets_have_no_font_or_remote_dependency(self):
        ns = {"svg": "http://www.w3.org/2000/svg"}
        for name in ("floorplan-light.svg", "floorplan-dark.svg", "timeline-light.svg", "timeline-dark.svg", *(f"rooms/{room[1]}.svg" for room in ROOMS)):
            svg = ET.parse(ROOT / "assets" / name)
            self.assertFalse(svg.findall(".//svg:text", ns))
            self.assertFalse(svg.findall(".//svg:image", ns))
            self.assertTrue(svg.findall(".//svg:path", ns) or svg.findall(".//svg:rect", ns))
        for theme in ("light", "dark"):
            text = (ROOT / f"assets/floorplan-{theme}.svg").read_text()
            self.assertEqual(text.count('id="room-'), 10)
            for category, key, *_ in ROOMS:
                self.assertIn(f'{room_counts(self.native)[category]} entries', text)

    def test_generated_site_payload_preserves_resources(self):
        html = (ROOT / "docs/index.html").read_text()
        payload = re.search(r'<script type="application/json" id="catalog-data">(.+?)</script>', html, re.S)
        entries = json.loads(payload[1])
        self.assertEqual({e["anchor"] for e in entries}, {entry_anchor(e) for e in self.active})
        self.assertEqual(sum(e["scope"] == "thor-native" for e in entries), len(self.native))
        self.assertEqual(len(re.findall(r'<button[^>]+data-room="', html)), 10)
        self.assertIn("prefers-reduced-motion", html)
        self.assertIn("prefers-color-scheme:dark", html)
        self.assertNotIn("__DATA__", html)

    def test_room_and_interface_text_meet_aa_contrast(self):
        def luminance(hex_color):
            rgb = [int(hex_color[i:i+2], 16) / 255 for i in (1, 3, 5)]
            linear = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in rgb]
            return sum(v * w for v, w in zip(linear, (.2126, .7152, .0722)))
        def contrast(a, b):
            low, high = sorted((luminance(a), luminance(b)))
            return (high + .05) / (low + .05)
        for room in ROOMS:
            self.assertGreaterEqual(contrast("#1F2A30", room[5]), 4.5)
            self.assertGreaterEqual(contrast("#E6E9E7", darken(room[5])), 4.5)
        for text, background in [("#536068", "#F6F7F5"), ("#2D5BE3", "#F6F7F5"), ("#B0BBBF", "#172025"), ("#7A9BFF", "#172025")]:
            self.assertGreaterEqual(contrast(text, background), 4.5)


if __name__ == "__main__":
    unittest.main()
