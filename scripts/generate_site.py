#!/usr/bin/env python3
"""Build a single, portable HTML catalog for GitHub Pages."""
from __future__ import annotations
import base64
from datetime import date
from html import escape
import json
from catalog import ROOT, ROOMS, SHORT_LABELS, active_entries, arxiv_id, display_venue, entry_anchor, is_new, papers_through, room_counts
from generate_assets import darken

def web_layout(counts: dict) -> dict:
    result = {}
    wings = [(['navigation', 'benchmarks', 'platforms', 'tutorials'], 3), (['instructions', 'planning', 'rl-agents', 'perception', 'tools', 'datasets'], 315)]
    for keys, x in wings:
        weights = {key: counts[next(r[0] for r in ROOMS if r[1] == key)] for key in keys}
        available = 414 - 8 * (len(keys) - 1)
        minimum = 49
        remaining = available - minimum * len(keys)
        y = 3
        for key in keys:
            height = minimum + remaining * weights[key] / sum(weights.values())
            result[key] = (x, y, 282, height)
            y += height + 8
    return result

def generate_site(data: dict, as_of: date) -> None:
    entries = active_entries(data)
    counts = room_counts(entries)
    layout = web_layout(counts)
    labels = {'platforms':'Platforms', 'benchmarks':'Benchmarks', 'instructions':'Instructions', 'navigation':'Navigation', 'planning':'Planning', 'rl-agents':'RL agents', 'perception':'Perception', 'datasets':'Datasets', 'tools':'Tools', 'tutorials':'Tutorials'}
    buttons, walls = [], []
    for i, (category, key, label, zh, room, color, note, note_zh) in enumerate(ROOMS):
        x, y, w, h = layout[key]
        style = f'--x:{x/6:.4f}%;--y:{y/4.2:.4f}%;--w:{w/6:.4f}%;--h:{h/4.2:.4f}%;--mobile-x:{i%5*20}%;--mobile-y:{int(i/5)*54}%;--fill:{color};--fill-dark:{darken(color)}'
        compact = ' compact' if h < 85 else ''
        buttons.append(f'<button type="button" class="room{compact}" data-room="{key}" style="{style}" aria-pressed="false" aria-label="{escape(label)}: {counts[category]} entries"><span class="room-label">{labels[key]}</span><span class="room-count">{counts[category]}</span><span class="room-name">{room}</span></button>')
        # A small door break on the corridor side turns the diagram into a plan.
        edge = x+w if x == 3 else x
        door = y+h-23
        path = f'M{edge} {door}V{y}H{x if x==3 else x+w}V{y+h}H{edge}V{door+16}'
        arc = f'M{edge} {door}h{-16 if x==3 else 16}M{edge} {door+16}A16 16 0 0 {0 if x==3 else 1} {edge+(-16 if x==3 else 16)} {door}'
        walls.append(f'<path class="wall" style="--delay:{i*22}ms" d="{path}"/><path class="door" d="{arc}"/>')
    payload = []
    for entry in entries:
        payload.append({k:entry[k] for k in ['title','year','venue','section','env','must_read','scope','short','highlight','added','links']})
        payload[-1]['anchor'] = entry_anchor(entry)
        venue = display_venue(entry)
        # 'arXiv' as a venue only repeats the arXiv link beside it.
        payload[-1]['venue'] = '' if venue.lower() == 'arxiv' and any('arxiv.org' in str(u) for u in entry['links'].values()) else venue
        payload[-1]['order'] = arxiv_id(entry)[0] * 100000 + arxiv_id(entry)[1]
        payload[-1]['new'] = entry['scope'] == 'thor-native' and is_new(entry, as_of)
    rooms = [{'key':r[1],'label':r[2],'short':SHORT_LABELS[r[1]][0],'color':r[5],'note':r[6]} for r in ROOMS]
    template = (ROOT/'scripts/templates/index.html').read_text(encoding='utf-8')
    replacements = {
        '__FONT__':base64.b64encode((ROOT/'assets/fonts/Archivo.woff2').read_bytes()).decode(),
        '__ROOM_BUTTONS__':'\n'.join(buttons), '__WALLS__':'\n'.join(walls),
        '__DATA__':json.dumps(payload,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c'),
        '__ROOMS__':json.dumps(rooms,ensure_ascii=False,separators=(',',':')),
        '__UPDATED__':papers_through(entries) or data['updated'], '__NATIVE_COUNT__':str(sum(counts.values())),
    }
    for key,value in replacements.items(): template=template.replace(key,value)
    docs=ROOT/'docs'
    docs.mkdir(exist_ok=True)
    (docs/'index.html').write_text(template,encoding='utf-8')
    (docs/'.nojekyll').write_text('',encoding='utf-8')
