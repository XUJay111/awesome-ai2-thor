#!/usr/bin/env python3
"""Generate outlined Archivo floor plans, a timeline, and a local web font."""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import date
from functools import lru_cache
from html import escape
from fontTools import subset
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from catalog import ROOT, ROOMS, ROOM_BY_KEY, floorplan_layout, load_data, native_entries, papers_through, room_counts, today

ASSETS = ROOT / 'assets'
FONT = ASSETS / 'fonts' / 'Archivo.ttf'
LABELS = {
    'platforms': ['Platforms &', 'environment generation'],
    'benchmarks': ['Benchmarks &', 'evaluation'],
    'instructions': ['Instruction following', '& household tasks'],
    'navigation': ['Navigation'],
    'planning': ['Planning, memory', '& multi-agent systems'],
    'rl-agents': ['RL-trained', 'VLM agents'],
    'perception': ['Perception, physics', '& scene graphs'],
    'datasets': ['Datasets &', 'assets'],
    'tools': ['Tools &', 'environments'],
    'tutorials': ['Tutorials &', 'notes'],
}

@lru_cache(maxsize=3)
def archivo(width: int = 75, weight: int = 600) -> TTFont:
    return instantiateVariableFont(TTFont(FONT, recalcTimestamp=False), {'wdth': width, 'wght': weight}, inplace=True)

def text_width(text: str, size: float, width: int = 75, weight: int = 600) -> float:
    font = archivo(width, weight)
    cmap = font.getBestCmap()
    return sum(font['hmtx'][cmap.get(ord(c), '.notdef')][0] for c in text) * size / font['head'].unitsPerEm

def _units(value: float) -> str:
    # Glyphs are drawn in font units (1000/em) and scaled down; whole units are
    # far below one rendered pixel and cut the outlined SVGs to a fraction.
    return str(round(value))

@lru_cache(maxsize=4096)
def _glyph_path(width: int, weight: int, glyph: str) -> str:
    font = archivo(width, weight)
    pen = SVGPathPen(font.getGlyphSet(), ntos=_units)
    font.getGlyphSet()[glyph].draw(pen)
    return pen.getCommands()

_USED: dict[str, str] = {}

def glyph_defs() -> str:
    """Emit each outlined glyph once; text runs reference it with <use>."""
    body = ''.join(f'<path id="{gid}" d="{d}"/>' for gid, d in sorted(_USED.items()))
    _USED.clear()
    return f'<defs>{body}</defs>'

def outlined(text: str, x: float, y: float, size: float, color: str, width: int = 75, weight: int = 600, opacity: float = 1) -> str:
    font = archivo(width, weight)
    cmap = font.getBestCmap()
    scale, offset, uses = size / font['head'].unitsPerEm, 0, []
    for char in text:
        glyph = cmap.get(ord(char), '.notdef')
        commands = _glyph_path(width, weight, glyph)
        if commands:
            gid = f'a{width}-{weight}-{glyph}'.replace('.', '_')
            _USED[gid] = commands
            uses.append(f'<use href="#{gid}" transform="translate({x + offset * scale:.2f} {y:.2f}) scale({scale:.5f} {-scale:.5f})"/>')
        offset += font['hmtx'][glyph][0]
    return f'<g fill="{color}" opacity="{opacity}" aria-label="{escape(text, quote=True)}">' + ''.join(uses) + '</g>'

def darken(color: str) -> str:
    return '#' + ''.join(f'{round(int(color[i:i+2], 16) * .45):02X}' for i in (1, 3, 5))

PALETTE = {
    False: {'paper': '#F6F7F5', 'ink': '#1F2A30', 'accent': '#2D5BE3'},
    True: {'paper': '#172025', 'ink': '#E6E9E7', 'accent': '#7A9BFF'},
}

def window(x: float, y: float, length: float, horizontal: bool, paper: str, ink: str) -> str:
    """Architectural window: the 6px exterior wall opens into two thin panes."""
    if horizontal:
        return (f'<rect x="{x:.1f}" y="{y - 4:.1f}" width="{length:.1f}" height="8" fill="{paper}"/>'
                f'<path d="M{x:.1f} {y - 3:.1f}h{length:.1f}M{x:.1f} {y + 3:.1f}h{length:.1f}M{x:.1f} {y:.1f}h{length:.1f}" stroke="{ink}" stroke-width="1" fill="none"/>'
                f'<path d="M{x:.1f} {y - 4:.1f}v8M{x + length:.1f} {y - 4:.1f}v8" stroke="{ink}" stroke-width="2"/>')
    return (f'<rect x="{x - 4:.1f}" y="{y:.1f}" width="8" height="{length:.1f}" fill="{paper}"/>'
            f'<path d="M{x - 3:.1f} {y:.1f}v{length:.1f}M{x + 3:.1f} {y:.1f}v{length:.1f}M{x:.1f} {y:.1f}v{length:.1f}" stroke="{ink}" stroke-width="1" fill="none"/>'
            f'<path d="M{x - 4:.1f} {y:.1f}h8M{x - 4:.1f} {y + length:.1f}h8" stroke="{ink}" stroke-width="2"/>')

def floorplan_svg(entries: list[dict], dark: bool = False, through: str = '') -> str:
    counts, layout = room_counts(entries), floorplan_layout(room_counts(entries))
    paper, ink = PALETTE[dark]['paper'], PALETTE[dark]['ink']
    body = []
    hall_y = None
    for category, key, label, _, room_name, fill, *_ in ROOMS:
        x, y, width, height = layout[key]
        top_wing = y == 24
        if top_wing:
            hall_y = y + height
        color = darken(fill) if dark else fill
        body.append(f'<g id="room-{key}"><title>{escape(label)}: {counts[category]} entries ({room_name})</title>')
        body.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{width:.2f}" height="{height:.2f}" fill="{color}" stroke="{ink}" stroke-width="3"/>')
        font_size = 22 if height > 140 else 17
        font_size = min(font_size, *(max(11, (width - 32) / text_width(line, 1)) for line in LABELS[key]))
        for i, line in enumerate(LABELS[key]):
            body.append(outlined(line, x + 16, y + 16 + font_size + i * (font_size + 4), font_size, ink))
        count, count_size = str(counts[category]), (38 if height > 140 else 26)
        body.append(outlined(count, x + 16, y + height - 16, count_size, ink))
        # The room's household name sits on the count baseline, like a plan tag.
        tag_size = 14 if top_wing else 12
        tag_w = text_width(room_name, tag_size, 100, 400)
        if 16 + text_width(count, count_size, 75, 600) + 12 + tag_w + 16 <= width:
            body.append(outlined(room_name, x + width - 16 - tag_w, y + height - 16, tag_size, ink, width=100, weight=400, opacity=.62))
        door_x, door_y = x + width - 42, y + height if top_wing else y
        # Doors swing into the shared hall, keeping labels unobstructed.
        inward = 1 if top_wing else -1
        body.extend([
            f'<path d="M{door_x:.2f} {door_y:.2f}h22" stroke="{paper}" stroke-width="5"/>',
            f'<path d="M{door_x:.2f} {door_y:.2f}v{inward * 22}" stroke="{ink}" stroke-width="1.5" fill="none"/>',
            f'<path d="M{door_x + 22:.2f} {door_y:.2f}A22 22 0 0 {0 if inward == -1 else 1} {door_x:.2f} {door_y + inward * 22:.2f}" stroke="{ink}" stroke-width="1" fill="none"/>',
            '</g>',
        ])
    body.append(f'<path d="M24 24H1176V352H24Z" fill="none" stroke="{ink}" stroke-width="6"/>')
    # One window per exterior room face; widths follow the room, capped so walls still read.
    for category, key, *_ in ROOMS:
        x, y, width, height = layout[key]
        length = min(110, width * .34)
        body.append(window(x + (width - length) / 2, 24 if y == 24 else 352, length, True, paper, ink))
    nav, rl = layout['navigation'], layout['rl-agents']
    body.append(window(24, nav[1] + nav[3] * .3, nav[3] * .4, False, paper, ink))
    body.append(window(1176, rl[1] + rl[3] * .3, rl[3] * .4, False, paper, ink))
    if hall_y is not None:
        body.append(outlined('Hallway', 40, hall_y + 16.5, 11, ink, width=100, weight=400, opacity=.55))
    body.append(outlined('Each room is a section. Numbers are entries.', 24, 392, 14, ink, width=100, weight=400, opacity=.6))
    # Title block, as on an architectural sheet.
    cells = ['Awesome AI2-THOR', f'{len(entries)} entries', f'Papers through {through}' if through else '10 rooms']
    sizes = [(14, 100, 600), (14, 100, 400), (14, 100, 400)]
    widths = [text_width(t, s, w, g) + 28 for t, (s, w, g) in zip(cells, sizes)]
    bx = 1176 - sum(widths)
    body.append(f'<rect x="{bx:.1f}" y="368" width="{sum(widths):.1f}" height="36" fill="none" stroke="{ink}" stroke-width="1.5"/>')
    cx = bx
    for i, (text, (s, w, g)) in enumerate(zip(cells, sizes)):
        if i:
            body.append(f'<path d="M{cx:.1f} 368v36" stroke="{ink}" stroke-width="1"/>')
        body.append(outlined(text, cx + 14, 391, s, ink, width=w, weight=g, opacity=1 if i == 0 else .75))
        cx += widths[i]
    head = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="420" viewBox="0 0 1200 420" role="img" aria-labelledby="title desc">',
        '<title id="title">A floor plan of the AI2-THOR research catalog</title>',
        '<desc id="desc">Each room is a section. Areas and counts exclude text-only ALFWorld papers.</desc>',
        glyph_defs(),
        f'<rect width="1200" height="420" fill="{paper}"/>',
    ]
    return '\n'.join(head + body + ['</svg>', ''])

def room_icon_svg(entries: list[dict], key: str) -> str:
    """A thumbnail of the plan with one room filled: 'you are here' for each section."""
    layout = floorplan_layout(room_counts(entries))
    sx, sy = 84 / 1152, 24 / 328
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="88" height="28" viewBox="0 0 88 28" aria-hidden="true">']
    for _, k, *_rest in ROOMS:
        x, y, w, h = layout[k]
        fill = ROOM_BY_KEY[k][5] if k == key else 'none'
        rx, ry = 2 + (x - 24) * sx, 2 + (y - 24) * sy
        parts.append(f'<rect x="{rx + .5:.1f}" y="{ry + .5:.1f}" width="{max(w * sx - 1, 1):.1f}" height="{max(h * sy - 1, 1):.1f}" fill="{fill}" stroke="#8A949A" stroke-width="1"/>')
    return '\n'.join(parts + ['</svg>', ''])

def timeline_svg(entries: list[dict], as_of: date, dark: bool = False) -> str:
    counts = Counter(int(e['year']) for e in entries if e['year'])
    years = list(range(min(counts, default=as_of.year), max(max(counts, default=as_of.year), as_of.year) + 1))
    paper, ink, accent = PALETTE[dark]['paper'], PALETTE[dark]['ink'], PALETTE[dark]['accent']
    body = []
    step, max_count = 1152 / len(years), max(counts.values(), default=1)
    for i, year in enumerate(years):
        x, height = 24 + i * step, counts[year] / max_count * 140
        color = accent if year == as_of.year else ink
        body.append(f'<rect x="{x + 12:.2f}" y="{182 - height:.2f}" width="{step - 24:.2f}" height="{height:.2f}" fill="{color}"/>')
        body.append(outlined(str(counts[year]), x + 12, 172 - height, 16, ink, width=100, weight=400))
        body.append(outlined(str(year), x + 12, 212, 16, ink, width=100, weight=400, opacity=.7))
    head = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="240" viewBox="0 0 1200 240" role="img" aria-labelledby="title desc">',
        '<title id="title">Entries by publication year</title>',
        '<desc id="desc">' + escape(', '.join(f'{year}: {counts[year]}' for year in years)) + '</desc>',
        glyph_defs(),
        f'<rect width="1200" height="240" fill="{paper}"/>',
    ]
    return '\n'.join(head + body + ['</svg>', ''])

def generate_assets(data: dict, as_of: date) -> None:
    ASSETS.mkdir(exist_ok=True)
    entries = native_entries(data)
    through = papers_through(entries)
    for dark in (False, True):
        suffix = 'dark' if dark else 'light'
        (ASSETS / f'floorplan-{suffix}.svg').write_text(floorplan_svg(entries, dark, through), encoding='utf-8')
        (ASSETS / f'timeline-{suffix}.svg').write_text(timeline_svg(entries, as_of, dark), encoding='utf-8')
    (ASSETS / 'rooms').mkdir(exist_ok=True)
    for _, key, *_ in ROOMS:
        (ASSETS / 'rooms' / f'{key}.svg').write_text(room_icon_svg(entries, key), encoding='utf-8')
    font = TTFont(FONT, recalcTimestamp=False)
    options = subset.Options()
    options.recalc_timestamp = False
    subsetter = subset.Subsetter(options=options)
    subsetter.populate(unicodes=list(range(32, 127)) + [0x2013, 0x2014, 0x2019, 0x201C, 0x201D, 0x00B7])
    subsetter.subset(font)
    font.flavor = 'woff2'
    font.save(ASSETS / 'fonts' / 'Archivo.woff2')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--as-of', type=date.fromisoformat, default=today())
    generate_assets(load_data(), parser.parse_args().as_of)
