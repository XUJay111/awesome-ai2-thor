"""Architectural drawing of the catalog: floors, furniture, walls, doors, windows.

Everything here is text-free so the same drawing serves the README banner
(where labels are outlined glyphs) and the website (where labels are real,
focusable HTML buttons laid over the plan).
"""
from __future__ import annotations

from catalog import BOTTOM_WING, PLAN_BOX, ROOMS, TOP_WING, floorplan_layout, hallway

EXTERIOR = 10.0   # exterior wall thickness
INTERIOR = 5.0    # interior wall thickness
PAD = 16.0        # label inset from the inner wall face

THEMES = {
    False: {'paper': '#F6F7F5', 'ink': '#1F2A30', 'furniture': '#FCFCFA', 'line': 'rgba(31,42,48,.55)', 'texture': 'rgba(31,42,48,.07)'},
    True: {'paper': '#172025', 'ink': '#E6E9E7', 'furniture': '#2A363C', 'line': 'rgba(230,233,231,.5)', 'texture': 'rgba(230,233,231,.07)'},
}
# Floors: boards in living spaces, tile in wet rooms, plain concrete elsewhere.
TEXTURE = {
    'navigation': 'boards', 'planning': 'boards', 'benchmarks': 'boards', 'rl-agents': 'boards',
    'instructions': 'tile', 'perception': 'tile', 'platforms': 'tile',
}


def darken(color: str, factor: float = .45) -> str:
    return '#' + ''.join(f'{round(int(color[i:i+2], 16) * factor):02X}' for i in (1, 3, 5))


def fill_for(key: str, dark: bool) -> str:
    color = next(r[5] for r in ROOMS if r[1] == key)
    return darken(color) if dark else color


def defs(dark: bool, prefix: str = 'fp') -> str:
    t = THEMES[dark]
    return (
        f'<pattern id="{prefix}-boards" width="96" height="22" patternUnits="userSpaceOnUse">'
        f'<path d="M0 11H96M0 22H96M30 0V11M78 11V22" stroke="{t["texture"]}" stroke-width="1" fill="none"/></pattern>'
        f'<pattern id="{prefix}-tile" width="18" height="18" patternUnits="userSpaceOnUse">'
        f'<path d="M18 0V18H0" stroke="{t["texture"]}" stroke-width="1" fill="none"/></pattern>'
    )


# ---------------------------------------------------------------- furniture
# Each piece is drawn in its own design space (w x h) and scaled into a box.

def _r(x, y, w, h, rx=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>'


def _c(cx, cy, r):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}"/>'


FURNITURE = {
    # living room: sofa facing a coffee table on a rug, armchair, plant
    'navigation': (130, 100, 'bottom-right', lambda: ''.join([
        '<rect x="8" y="14" width="104" height="64" rx="2" fill="none" stroke-dasharray="3 3"/>',
        _r(14, 74, 92, 22, 5), '<path d="M22 74V88H98V74" fill="none"/>',
        _r(40, 38, 40, 18, 2),
        _r(48, 2, 24, 20, 5), '<path d="M51 2V8H69V2" fill="none"/>',
        _c(120, 90, 8), _c(120, 90, 4),
    ])),
    # dining: table with six chairs
    'planning': (120, 80, 'center-right', lambda: ''.join([
        *[_r(x, 6, 14, 10, 2) for x in (30, 53, 76)],
        *[_r(x, 64, 14, 10, 2) for x in (30, 53, 76)],
        _r(10, 33, 10, 14, 2), _r(100, 33, 10, 14, 2),
        _r(22, 18, 76, 44, 4),
    ])),
    # kitchen: L-shaped counter with sink and hob, island with stools
    'instructions': (120, 96, 'top-right', lambda: ''.join([
        '<path d="M0 0H120V96H100V20H0Z"/>',
        _r(26, 4, 28, 12, 3), _c(40, 10, 1.6),
        *[_c(cx, cy, 3.6) for cx in (106, 115) for cy in (38, 50)],
        _r(28, 44, 48, 24, 2),
        *[_c(cx, 80, 4.5) for cx in (38, 52, 66)],
    ])),
    # study: desk with monitor and chair, bookshelf on the side wall
    'benchmarks': (112, 92, 'top-right', lambda: ''.join([
        _r(14, 0, 70, 22), _r(36, 5, 26, 4, 1),
        _c(49, 36, 9), '<path d="M40 44Q49 50 58 44" fill="none"/>',
        _r(96, 0, 16, 84), '<path d="M96 14H112M96 28H112M96 42H112M96 56H112M96 70H112" fill="none"/>',
    ])),
    # bedroom: bed with pillows and a nightstand
    'rl-agents': (110, 70, 'bottom-right', lambda: ''.join([
        _r(20, 6, 82, 58, 3), _r(100, 6, 10, 58, 2),
        _r(84, 12, 14, 19, 3), _r(84, 39, 14, 19, 3),
        '<path d="M58 6V64" fill="none"/>',
    ])),
    # bathroom: tub, toilet, basin
    'perception': (118, 70, 'bottom-right', lambda: ''.join([
        _r(78, 6, 40, 64, 10), _r(84, 12, 28, 52, 8),
        _r(46, 60, 20, 10, 2), '<ellipse cx="56" cy="48" rx="8" ry="11"/>',
        _r(4, 50, 30, 20, 3), '<ellipse cx="19" cy="60" rx="9" ry="6"/>',
    ])),
    # garage: car from above and a workbench
    'tools': (124, 72, 'bottom-right', lambda: ''.join([
        _r(26, 4, 96, 48, 14), _r(78, 10, 16, 36, 4), _r(36, 12, 10, 32, 3),
        '<path d="M60 4V10M60 46V52" fill="none"/>',
        _r(0, 58, 60, 14), '<path d="M10 58V72M24 58V72M38 58V72" fill="none"/>',
    ])),
    # storage: shelving units and boxes
    'datasets': (96, 64, 'bottom-right', lambda: ''.join([
        *[_r(x, 46, 28, 18) for x in (0, 34, 68)],
        '<path d="M0 55H96M14 46V64M48 46V64M82 46V64" fill="none"/>',
        _r(40, 10, 20, 20, 1), _r(64, 16, 16, 16, 1), '<path d="M40 20H60M64 24H80" fill="none"/>',
    ])),
    # closet: hanging rail with hangers
    'tutorials': (60, 40, 'bottom-right', lambda: ''.join([
        _r(0, 30, 60, 10),
        '<path d="M4 26H56" fill="none"/>',
        *[f'<path d="M{x} 26V18" fill="none"/>' for x in (12, 22, 32, 42, 52)],
    ])),
}


def furniture(key: str, box: tuple[float, float, float, float], dark: bool, flip_y: bool = False) -> str:
    """Scale a room's furniture into the free part of the room; skip if it would be cramped."""
    if key not in FURNITURE:
        return ''
    w0, h0, anchor, draw = FURNITURE[key]
    bx, by, bw, bh = box
    s = min(bw / w0, bh / h0, 1.5)
    if s < .62:
        return ''
    w, h = w0 * s, h0 * s
    x = bx + bw - w
    if anchor == 'top-right':
        y = by
    elif anchor == 'bottom-right':
        y = by + bh - h
    else:
        y = by + (bh - h) / 2
    t = THEMES[dark]
    transform = f'translate({x:.1f} {y:.1f}) scale({s:.3f})'
    if flip_y:  # mirror wall-hugging pieces for rooms whose exterior wall is at the bottom
        transform = f'translate({x:.1f} {y + h:.1f}) scale({s:.3f} {-s:.3f})'
    return (f'<g class="furniture" data-for="{key}" transform="{transform}" fill="{t["furniture"]}" stroke="{t["line"]}" '
            f'stroke-width="{1.15 / s:.2f}" stroke-linejoin="round">{draw()}</g>')


# ---------------------------------------------------------------- plan

def label_room(key: str, top_wing: bool) -> float:
    """Approximate width reserved for the label stack; furniture starts to its right."""
    from catalog import SHORT_LABELS
    return len(SHORT_LABELS[key][0]) * (11.5 if top_wing else 8.8) + 18


def door_positions(layout: dict) -> dict[str, tuple[float, float, bool]]:
    """(x, width, top_wing) of each room's hallway door, avoiding clashes across the hall."""
    doors = {}
    for key in TOP_WING:
        x, y, w, h = layout[key]
        doors[key] = (x + w - 52, 32.0, True)
    for key in BOTTOM_WING:
        x, y, w, h = layout[key]
        width = 28.0
        left = x + 20
        right = x + w - 20 - width
        clash = lambda d: any(abs(d - tx) < 40 for tx, _, top in doors.values() if top)
        doors[key] = (left if not clash(left) else right, width, False)
    return doors


def plan(entries: list[dict], dark: bool, *, prefix: str = 'fp', furniture_on: bool = True, entrance_label: bool = False) -> str:
    """Return SVG elements (no <svg> wrapper) for the whole house in the 1200 x 372 frame."""
    from catalog import room_counts
    t = THEMES[dark]
    layout = floorplan_layout(room_counts(entries))
    hx, hy, hw, hh = hallway(layout)
    x0, y0, x1, y1 = PLAN_BOX
    parts = [f'<defs>{defs(dark, prefix)}</defs>']
    # floors
    parts.append(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" fill="{t["paper"]}"/>')
    for _, key, *_ in ROOMS:
        x, y, w, h = layout[key]
        parts.append(f'<rect class="floor" data-floor="{key}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill_for(key, dark)}"/>')
        if key in TEXTURE:
            parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="url(#{prefix}-{TEXTURE[key]})" pointer-events="none"/>')
    # hallway runner
    parts.append(f'<rect x="{hx + 60:.1f}" y="{hy + 9:.1f}" width="{hw - 120:.1f}" height="{hh - 18:.1f}" rx="2" fill="none" stroke="{t["texture"]}" stroke-width="1.5"/>')
    # furniture
    if furniture_on:
        for key in TOP_WING + BOTTOM_WING:
            x, y, w, h = layout[key]
            top = key in TOP_WING
            reserve = label_room(key, top)
            inner = INTERIOR / 2
            box = (x + max(w * .42, reserve + PAD), y + (EXTERIOR / 2 + 6 if top else inner + 10),
                   w - max(w * .42, reserve + PAD) - (EXTERIOR / 2 + 6 if key in ('benchmarks', 'tutorials') else inner + 8),
                   h - (EXTERIOR / 2 + 6 if top else inner + 10) - (inner + 10 if top else EXTERIOR / 2 + 6))
            if key in ('datasets', 'tutorials'):
                # Small rooms: tuck furniture into the corner beside the count, under the label.
                box = (x + 78, y + 54, w - 78 - (EXTERIOR / 2 + 8 if key == 'tutorials' else inner + 8), h - 54 - (EXTERIOR / 2 + 6))
            parts.append(furniture(key, box, dark))
    # walls: interior partitions, hallway walls, exterior shell
    wall = []
    for wing in (TOP_WING, BOTTOM_WING):
        for key in wing[1:]:
            x, y, w, h = layout[key]
            wall.append(f'<rect x="{x - INTERIOR / 2:.1f}" y="{y:.1f}" width="{INTERIOR}" height="{h:.1f}"/>')
    for yy in (hy, hy + hh):
        wall.append(f'<rect x="{x0:.1f}" y="{yy - INTERIOR / 2:.1f}" width="{x1 - x0:.1f}" height="{INTERIOR}"/>')
    parts.append(f'<g fill="{t["ink"]}">{"".join(wall)}</g>')
    parts.append(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" fill="none" stroke="{t["ink"]}" stroke-width="{EXTERIOR}"/>')
    # doors into the hallway: an opening, the leaf, and its swing
    for key, (dx, dw, top) in door_positions(layout).items():
        x, y, w, h = layout[key]
        wy = y + h if top else y
        sign = 1 if top else -1
        parts.append(f'<rect x="{dx:.1f}" y="{wy - INTERIOR / 2 - .5:.1f}" width="{dw}" height="{INTERIOR + 1}" fill="{t["paper"]}"/>')
        parts.append(f'<path d="M{dx:.1f} {wy:.1f}v{sign * dw:.1f}" stroke="{t["ink"]}" stroke-width="1.6" fill="none"/>')
        parts.append(f'<path d="M{dx:.1f} {wy + sign * dw:.1f}A{dw} {dw} 0 0 {0 if top else 1} {dx + dw:.1f} {wy:.1f}" class="swing" stroke="{t["line"]}" stroke-width="1" fill="none"/>')
    # windows in the exterior shell
    def window(x, y, length, horizontal):
        e = EXTERIOR / 2
        if horizontal:
            return (f'<rect x="{x:.1f}" y="{y - e:.1f}" width="{length:.1f}" height="{EXTERIOR}" fill="{t["paper"]}"/>'
                    f'<path d="M{x:.1f} {y - e + .5:.1f}h{length:.1f}M{x:.1f} {y + e - .5:.1f}h{length:.1f}M{x:.1f} {y:.1f}h{length:.1f}" stroke="{t["ink"]}" stroke-width="1" fill="none"/>'
                    f'<path d="M{x:.1f} {y - e:.1f}v{EXTERIOR}M{x + length:.1f} {y - e:.1f}v{EXTERIOR}" stroke="{t["ink"]}" stroke-width="2"/>')
        return (f'<rect x="{x - e:.1f}" y="{y:.1f}" width="{EXTERIOR}" height="{length:.1f}" fill="{t["paper"]}"/>'
                f'<path d="M{x - e + .5:.1f} {y:.1f}v{length:.1f}M{x + e - .5:.1f} {y:.1f}v{length:.1f}M{x:.1f} {y:.1f}v{length:.1f}" stroke="{t["ink"]}" stroke-width="1" fill="none"/>'
                f'<path d="M{x - e:.1f} {y:.1f}h{EXTERIOR}M{x - e:.1f} {y + length:.1f}h{EXTERIOR}" stroke="{t["ink"]}" stroke-width="2"/>')
    for key in TOP_WING:
        x, y, w, h = layout[key]
        length = min(120, w * .36)
        parts.append(window(x + (w - length) / 2, y0, length, True))
    for key in BOTTOM_WING:
        if key in ('platforms', 'tutorials'):
            continue
        x, y, w, h = layout[key]
        length = min(96, w * .34)
        parts.append(window(x + (w - length) / 2, y1, length, True))
    nav, study = layout['navigation'], layout['benchmarks']
    parts.append(window(x0, nav[1] + nav[3] * .32, nav[3] * .36, False))
    parts.append(window(x1, study[1] + study[3] * .32, study[3] * .36, False))
    # front door: through the foyer's exterior wall, swinging in
    fx, fy, fw, fh = layout['platforms']
    door_w = 34.0
    dx = fx + fw - door_w - 22
    parts.append(f'<rect x="{dx:.1f}" y="{y1 - EXTERIOR / 2 - .5:.1f}" width="{door_w}" height="{EXTERIOR + 1}" fill="{fill_for("platforms", dark)}"/>')
    parts.append(f'<path d="M{dx + door_w:.1f} {y1:.1f}v{-door_w}" stroke="{t["ink"]}" stroke-width="1.6" fill="none"/>')
    parts.append(f'<path d="M{dx + door_w:.1f} {y1 - door_w:.1f}A{door_w} {door_w} 0 0 0 {dx:.1f} {y1:.1f}" class="swing" stroke="{t["line"]}" stroke-width="1" fill="none"/>')
    parts.append(f'<path d="M{dx + 4:.1f} {y1 + 9:.1f}h{door_w - 8}" stroke="{t["ink"]}" stroke-width="1.5"/>')  # threshold step
    return '\n'.join(p for p in parts if p)


def entrance_point(entries: list[dict]) -> tuple[float, float]:
    """Center of the front door's outside step, for the 'Start here' tag."""
    from catalog import room_counts
    fx, fy, fw, fh = floorplan_layout(room_counts(entries))['platforms']
    return fx + fw - 34 / 2 - 22, PLAN_BOX[3] + 9
