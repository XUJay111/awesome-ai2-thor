#!/usr/bin/env python3
"""Build a single, portable HTML catalog for GitHub Pages."""
from __future__ import annotations
import base64
from datetime import date
from html import escape
import json
from catalog import (
    BOTTOM_WING, PLAN_BOX, ROOT, ROOMS, SHORT_LABELS, TOP_WING, active_entries, arxiv_id,
    display_venue, entry_anchor, floorplan_layout, is_new, papers_through, room_counts,
)
import floorplan as fp

# The website frame crops the banner to the house plus the front step.
VIEW = (12.0, 12.0, 1176.0, 372.0)  # x, y, width, height in plan units


def pct(value: float, origin: float, size: float) -> str:
    return f'{(value - origin) / size * 100:.3f}%'


def room_buttons(entries: list[dict]) -> str:
    counts = room_counts(entries)
    layout = floorplan_layout(counts)
    vx, vy, vw, vh = VIEW
    out = []
    for category, key, label, _, room_name, color, *_ in ROOMS:
        x, y, w, h = layout[key]
        wing = 'top' if key in TOP_WING else 'bottom'
        size = 'narrow' if w < 200 else 'wide'
        style = (f'--x:{pct(x, vx, vw)};--y:{pct(y, vy, vh)};--w:{w / vw * 100:.3f}%;--h:{h / vh * 100:.3f}%;'
                 f'--fill:{color};--fill-dark:{fp.darken(color)}')
        out.append(
            f'<button type="button" class="room {wing} {size}" data-room="{key}" style="{style}" aria-pressed="false" '
            f'aria-label="{escape(label)}, {counts[category]} entries">'
            f'<span class="room-head"><span class="room-label">{SHORT_LABELS[key][0]}</span>'
            f'<span class="room-name">{room_name}</span></span>'
            f'<span class="room-count">{counts[category]}</span></button>')
    return '\n'.join(out)


def plan_svgs(entries: list[dict]) -> str:
    vx, vy, vw, vh = VIEW
    svgs = []
    for dark in (False, True):
        theme = 'dark' if dark else 'light'
        svgs.append(f'<svg class="plan-art theme-{theme}" viewBox="{vx} {vy} {vw} {vh}" aria-hidden="true" focusable="false">'
                    f'{fp.plan(entries, dark, prefix="w" + theme[0])}</svg>')
    return '\n'.join(svgs)


def start_tag(entries: list[dict]) -> str:
    vx, vy, vw, vh = VIEW
    cx, cy = fp.entrance_point(entries)
    return (f'<a class="start-tag" href="#start" style="left:{pct(cx, vx, vw)};top:{pct(cy, vy, vh)}">'
            f'<svg viewBox="0 0 10 12" aria-hidden="true"><path d="M5 11V2M1 6l4-4 4 4"/></svg>Start here</a>')


def routes(entries: list[dict]) -> list[dict]:
    from generate_readme import ROUTES, find_entry
    out = []
    for name, _, steps in ROUTES:
        out.append({'name': name, 'steps': [
            {'label': label, 'note': note, 'anchor': entry_anchor(find_entry(entries, prefix))}
            for prefix, label, _, note, _ in steps]})
    return out


def generate_site(data: dict, as_of: date) -> None:
    entries = active_entries(data)
    counts = room_counts(entries)
    native = [e for e in entries if e['scope'] == 'thor-native']
    payload = []
    for entry in entries:
        item = {k: entry[k] for k in ['title', 'year', 'section', 'env', 'must_read', 'scope', 'short', 'highlight', 'added', 'links']}
        venue = display_venue(entry)
        # 'arXiv' as a venue only repeats the arXiv link beside it.
        item['venue'] = '' if venue.lower() == 'arxiv' and any('arxiv.org' in str(u) for u in entry['links'].values()) else venue
        item['anchor'] = entry_anchor(entry)
        item['order'] = arxiv_id(entry)[0] * 100000 + arxiv_id(entry)[1]
        item['new'] = entry['scope'] == 'thor-native' and is_new(entry, as_of)
        payload.append(item)
    rooms = [{'key': r[1], 'label': r[2], 'short': SHORT_LABELS[r[1]][0], 'room': r[4], 'color': r[5],
              'dark': fp.darken(r[5]), 'note': r[6]} for r in ROOMS]
    template = (ROOT / 'scripts/templates/index.html').read_text(encoding='utf-8')
    replacements = {
        '__FONT__': base64.b64encode((ROOT / 'assets/fonts/Archivo.woff2').read_bytes()).decode(),
        '__PLAN_SVGS__': plan_svgs(native),
        '__ROOM_BUTTONS__': room_buttons(native),
        '__START_TAG__': start_tag(native),
        '__DATA__': json.dumps(payload, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c'),
        '__ROOMS__': json.dumps(rooms, ensure_ascii=False, separators=(',', ':')),
        '__ROUTES__': json.dumps(routes(entries), ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c'),
        '__UPDATED__': papers_through(entries) or data['updated'],
        '__NATIVE_COUNT__': str(sum(counts.values())),
    }
    for key, value in replacements.items():
        template = template.replace(key, value)
    docs = ROOT / 'docs'
    docs.mkdir(exist_ok=True)
    (docs / 'index.html').write_text(template, encoding='utf-8')
    (docs / '.nojekyll').write_text('', encoding='utf-8')
