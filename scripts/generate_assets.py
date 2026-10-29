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
from catalog import (BOTTOM_WING, PLAN_BOX, ROOT, ROOMS, ROOM_BY_KEY, SHORT_LABELS, TOP_WING, floorplan_layout,
                     hallway, load_data, native_entries, papers_through, room_counts, today)
import floorplan as fp

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

@lru_cache(maxsize=8)
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

darken = fp.darken

PALETTE = {
    False: {'paper': '#F6F7F5', 'ink': '#1F2A30', 'accent': '#2D5BE3'},
    True: {'paper': '#172025', 'ink': '#E6E9E7', 'accent': '#7A9BFF'},
}

def room_labels(entries: list[dict], dark: bool) -> list[str]:
    """Outlined section name, household room name, and count for every room."""
    counts, layout = room_counts(entries), floorplan_layout(room_counts(entries))
    ink = PALETTE[dark]['ink']
    out = []
    for category, key, label, _, room_name, *_ in ROOMS:
        x, y, w, h = layout[key]
        top = key in TOP_WING
        inner_top = (fp.EXTERIOR if top else fp.INTERIOR) / 2 + fp.PAD
        inner_bottom = (fp.INTERIOR if top else fp.EXTERIOR) / 2 + fp.PAD
        left = x + (fp.EXTERIOR if x == PLAN_BOX[0] else fp.INTERIOR) / 2 + fp.PAD - 2
        name = SHORT_LABELS[key][0]
        size, tag, num = (22, 13, 40) if top else (17, 11.5, 28)
        size = min(size, (w - 2 * fp.PAD) / max(text_width(name, 1), 1))
        out.append(f'<g id="room-{key}"><title>{escape(label)}: {counts[category]} entries ({room_name})</title>')
        out.append(outlined(name, left, y + inner_top + size * .78, size, ink))
        out.append(outlined(room_name, left, y + inner_top + size * .78 + tag + 6, tag, ink, width=100, weight=400, opacity=.58))
        out.append(outlined(str(counts[category]), left, y + h - inner_bottom, num, ink, width=75, weight=500))
        out.append('</g>')
    return out


def start_tag(entries: list[dict], dark: bool) -> list[str]:
    ink = PALETTE[dark]['ink']
    cx, cy = fp.entrance_point(entries)
    text = 'Start here'
    w = text_width(text, 12, 100, 500)
    return [f'<path d="M{cx:.1f} {cy + 4:.1f}v10M{cx - 4:.1f} {cy + 8:.1f}l4 -4l4 4" stroke="{ink}" stroke-width="1.2" fill="none" opacity=".7"/>',
            outlined(text, cx - w / 2, cy + 28, 12, ink, width=100, weight=500, opacity=.7)]


def title_block(entries: list[dict], dark: bool, through: str, right: float = 1176, top: float = 370) -> list[str]:
    ink = PALETTE[dark]['ink']
    cells = ['Awesome AI2-THOR', f'{len(entries)} entries', f'Papers through {through}' if through else '10 rooms']
    sizes = [(13, 100, 600), (13, 100, 400), (13, 100, 400)]
    widths = [text_width(t, s, w, g) + 26 for t, (s, w, g) in zip(cells, sizes)]
    bx = right - sum(widths)
    out = [f'<rect x="{bx:.1f}" y="{top}" width="{sum(widths):.1f}" height="32" fill="none" stroke="{ink}" stroke-width="1.2"/>']
    cx = bx
    for i, (text, (s, w, g)) in enumerate(zip(cells, sizes)):
        if i:
            out.append(f'<path d="M{cx:.1f} {top}v32" stroke="{ink}" stroke-width="1"/>')
        out.append(outlined(text, cx + 13, top + 21, s, ink, width=w, weight=g, opacity=1 if i == 0 else .72))
        cx += widths[i]
    return out


def floorplan_svg(entries: list[dict], dark: bool = False, through: str = '') -> str:
    paper = PALETTE[dark]['paper']
    body = [fp.plan(entries, dark, prefix='b')] + room_labels(entries, dark) + start_tag(entries, dark) + title_block(entries, dark, through)
    head = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="420" viewBox="0 0 1200 420" role="img" aria-labelledby="title desc">',
        '<title id="title">A floor plan of the AI2-THOR research catalog</title>',
        '<desc id="desc">Each room is a research direction; larger rooms hold more papers. Counts exclude text-only ALFWorld papers.</desc>',
        glyph_defs(),
        f'<rect width="1200" height="420" fill="{paper}"/>',
    ]
    return '\n'.join(head + body + ['</svg>', ''])


def social_preview_svg(entries: list[dict], through: str = '') -> str:
    """1280 x 640 card for link previews: the plan is the picture, the name is the caption."""
    paper, ink = PALETTE[False]['paper'], PALETTE[False]['ink']
    title, sub = 'Awesome AI2-THOR', 'Papers, benchmarks, and tools for the AI2-THOR family'
    facts = f'{len(entries)} entries' + (f'  /  papers through {through}' if through else '')
    body = [
        outlined(title, 64, 126, 72, ink, width=100, weight=700),
        outlined(sub, 66, 174, 26, ink, width=100, weight=400, opacity=.72),
        outlined(facts, 1216 - text_width(facts, 20, 100, 400), 126, 20, ink, width=100, weight=400, opacity=.62),
        '<g transform="translate(40 226)">', fp.plan(entries, False, prefix='s'), *room_labels(entries, False), '</g>',
    ]
    head = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="640" viewBox="0 0 1280 640" role="img" aria-label="Awesome AI2-THOR: a floor plan of the research catalog">',
        glyph_defs(),
        f'<rect width="1280" height="640" fill="{paper}"/>',
    ]
    return '\n'.join(head + body + ['</svg>', ''])


def room_icon_svg(entries: list[dict], key: str) -> str:
    """A thumbnail of the plan with one room filled: 'you are here' for each section."""
    layout = floorplan_layout(room_counts(entries))
    x0, y0, x1, y1 = PLAN_BOX
    sx, sy = 84 / (x1 - x0), 24 / (y1 - y0)
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="88" height="28" viewBox="0 0 88 28" aria-hidden="true">']
    x, y, w, h = layout[key]
    parts.append(f'<rect x="{2 + (x - x0) * sx:.1f}" y="{2 + (y - y0) * sy:.1f}" width="{w * sx:.1f}" height="{h * sy:.1f}" fill="{fp.darken(ROOM_BY_KEY[key][5], .82)}"/>')
    lines = []
    for wing in (TOP_WING, BOTTOM_WING):
        for k in wing[1:]:
            rx, ry, rw, rh = layout[k]
            lines.append(f'M{2 + (rx - x0) * sx:.1f} {2 + (ry - y0) * sy:.1f}v{rh * sy:.1f}')
    hx, hy, hw, hh = hallway(layout)
    lines.append(f'M2 {2 + (hy - y0) * sy:.1f}h84M2 {2 + (hy + hh - y0) * sy:.1f}h84')
    parts.append(f'<path d="{"".join(lines)}" stroke="#8A949A" stroke-width="1" fill="none"/>')
    parts.append('<rect x="2" y="2" width="84" height="24" fill="none" stroke="#8A949A" stroke-width="1.6"/>')
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
    (ASSETS / 'social-preview.svg').write_text(social_preview_svg(entries, through), encoding='utf-8')
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
