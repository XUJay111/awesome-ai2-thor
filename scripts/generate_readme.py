#!/usr/bin/env python3
"""Generate both READMEs, outlined assets, and GitHub Pages from data.yml."""
from __future__ import annotations
import argparse
from datetime import date
from html import escape
import re
from urllib.parse import quote, urlparse
from catalog import (
    REPO, ROOT, ROOMS, ROOM_BY_KEY, SHORT_LABELS, SITE_URL, active_entries,
    arxiv_id, display_venue, ecosystem_counts, entry_anchor, is_new, load_data,
    native_entries, papers_through, recent_first, room_counts, slugify,
    sort_entries, today,
)
from generate_assets import generate_assets

NEW = '![NEW](https://img.shields.io/badge/new-2D5BE3?style=flat-square)'
ROUTES = [
    ('New to AI2-THOR', '初识 AI2-THOR', [('AI2-THOR:', 'AI2-THOR paper', 'AI2-THOR 论文', 'what the simulator is', '了解模拟器'), ('AI2-THOR Documentation', 'Official docs', '官方文档', 'run your first scene', '运行首个场景'), ('EmbodiedBench:', 'EmbodiedBench', 'EmbodiedBench', 'how visual agents are evaluated', '了解视觉智能体评测')]),
    ('ObjectNav and RoboTHOR', '目标导航与 RoboTHOR', [('RoboTHOR:', 'RoboTHOR paper', 'RoboTHOR 论文', 'understand simulation-to-real evaluation', '了解仿真到真实评测'), ('AllenAct ObjectNav Tutorial', 'ObjectNav tutorial', '目标导航教程', 'train a baseline', '训练基线'), ('Simple but Effective:', 'CLIP for embodied AI', 'CLIP 与具身智能', 'compare visual representations', '比较视觉表征')]),
    ('ALFRED and TEACh', 'ALFRED 与 TEACh', [('ALFRED:', 'ALFRED paper', 'ALFRED 论文', 'ground instructions in actions', '将指令落地为动作'), ('TEACh:', 'TEACh paper', 'TEACh 论文', 'add dialogue to household tasks', '为家务任务加入对话'), ('ALFRED Documentation', 'ALFRED resources', 'ALFRED 资源', 'check the evaluation protocol', '查看评测协议')]),
    ('ProcTHOR and scene generation', 'ProcTHOR 与场景生成', [('ProcTHOR:', 'ProcTHOR paper', 'ProcTHOR 论文', 'generate interactive houses', '生成可交互房屋'), ('ProcTHOR-10K Repository', 'ProcTHOR-10K repository', 'ProcTHOR-10K 仓库', 'load the house corpus', '加载房屋语料'), ('Holodeck:', 'Holodeck paper', 'Holodeck 论文', 'generate scenes from language', '从语言生成场景')]),
    ('LLM/VLM embodied agents', 'LLM/VLM 具身智能体', [('LoTa-Bench:', 'LoTa-Bench', 'LoTa-Bench', 'compare language planners', '比较语言规划器'), ('Embodied Agent Interface:', 'Embodied Agent Interface', 'Embodied Agent Interface', 'inspect decision stages', '检查决策阶段'), ('Embodied-Reasoner', 'Embodied-Reasoner', 'Embodied-Reasoner', 'connect reasoning to interaction', '连接推理与交互')]),
]

def find_entry(entries: list[dict], prefix: str) -> dict:
    return next(e for e in entries if e['title'].startswith(prefix))

def entry_link(entry: dict, label: str | None = None) -> str:
    return f'[{label or entry["title"]}](#{entry_anchor(entry)})'

def shield(label: str, message: str, color: str) -> str:
    def encode(value: str) -> str:
        return quote(value.replace('-', '--').replace('_', '__'), safe='')
    return f'https://img.shields.io/badge/{encode(label)}-{encode(message)}-{color}?style=flat-square'

def render_links(links: dict) -> str:
    rendered = []
    for kind, url in links.items():
        arxiv = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', url)
        if arxiv:
            label, image = 'arXiv', shield('arXiv', arxiv[1], 'B31B1B')
        elif kind in {'paper', 'acl_anthology'}:
            label, image = 'Paper', shield('paper', 'read', 'B31B1B')
        elif kind in {'code', 'official_code', 'sgclip_code'}:
            parsed, label = urlparse(url), 'Code'
            path = parsed.path.strip('/').split('/')
            image = f'https://img.shields.io/github/stars/{"/".join(path[:2])}?style=flat-square&label=code&color=1F2A30' if parsed.netloc == 'github.com' and len(path) >= 2 else shield('code', 'view', '1F2A30')
        elif kind in {'dataset', 'dataset_tools'}:
            label, image = 'Dataset', shield('data', 'download', '5E8C61')
        elif kind in {'tutorial', 'note'}:
            label, image = 'Tutorial', shield('tutorial', 'read', '7A7A72')
        else:
            label, image = 'Project', shield('project', 'page', '2D5BE3')
        rendered.append(f'[![{label}]({image})]({url})')
    return ' '.join(rendered)

def render_routes(entries: list[dict], zh: bool) -> list[str]:
    lines = ['## 开始阅读' if zh else '## Start here', '']
    for i, (name, name_zh, steps) in enumerate(ROUTES):
        if i == 3:
            lines += ['<details>', '<summary>另两条阅读路线</summary>' if zh else '<summary>Two more reading routes</summary>', '']
        lines += [f'**{name_zh if zh else name}**', '']
        for number, (prefix, label, label_zh, note, note_zh) in enumerate(steps, 1):
            lines.append(f'{number}. {entry_link(find_entry(entries, prefix), label_zh if zh else label)} — {note_zh if zh else note}')
        lines.append('')
    return lines + ['</details>', '']

def render_family(entries: list[dict], zh: bool) -> list[str]:
    lines = ['## THOR 家族' if zh else '## The THOR family', '', '```mermaid', 'flowchart LR',
        '  A["AI2-THOR 2017"] --> B["iTHOR"]',
        '  A --> C["RoboTHOR 2020"]', '  A --> D["ManipulaTHOR 2021"]',
        '  A --> E["ProcTHOR 2022"]', '  A --> F["ArchitecTHOR"]',
        '  E --> G["Holodeck 2024"]', '  E --> H["SPOC 2024"]',
        '  A --> I["ALFRED 2020"]', '  A --> J["TEACh 2022"]',
        '  I --> K["ALFWorld 2021"]', '  A --> L["EmbodiedBench 2025"]',
        f'  classDef platform fill:{ROOM_BY_KEY["platforms"][5]},color:#1F2A30,stroke:#1F2A30',
        f'  classDef navigation fill:{ROOM_BY_KEY["navigation"][5]},color:#1F2A30,stroke:#1F2A30',
        f'  classDef household fill:{ROOM_BY_KEY["instructions"][5]},color:#1F2A30,stroke:#1F2A30',
        f'  classDef evaluation fill:{ROOM_BY_KEY["benchmarks"][5]},color:#1F2A30,stroke:#1F2A30',
        '  class A,B,D,E,F,G platform', '  class C,H navigation',
        '  class I,J,K household', '  class L evaluation', '```', '']
    refs = [('AI2-THOR:', 'AI2-THOR / iTHOR'), ('RoboTHOR:', 'RoboTHOR'), ('ManipulaTHOR:', 'ManipulaTHOR'), ('ProcTHOR:', 'ProcTHOR'), ('Selective Visual Representations', 'ArchitecTHOR evaluation'), ('Holodeck:', 'Holodeck'), ('SPOC:', 'SPOC'), ('ALFRED:', 'ALFRED'), ('TEACh:', 'TEACh'), ('ALFWorld:', 'ALFWorld'), ('EmbodiedBench:', 'EmbodiedBench')]
    lines += [' / '.join(entry_link(find_entry(entries, prefix), label) for prefix, label in refs), '']
    return lines + ['连接线表示模拟器扩展或任务谱系，不表示模型继承。' if zh else 'Edges show simulator extensions or task lineage, rather than model inheritance.', '']

def render_table(entries: list[dict], zh: bool, as_of: date) -> list[str]:
    lines = ['| 年份 | 论文或资源 | 环境 | 链接 |' if zh else '| Year | Paper / resource | Env | Links |', '| :--: | --- | :--: | --- |']
    for entry in sort_entries(entries):
        title = escape(entry['title']).replace('|', '&#124;')
        short = escape(entry['short_zh' if zh else 'short']).replace('|', '&#124;')
        mark = f' {NEW}' if entry['scope'] == 'thor-native' and is_new(entry, as_of) else ''
        env = '<br>'.join(entry['env'])
        lines.append(f'| {entry["year"] or "—"} | <a id="{entry_anchor(entry)}"></a>**{title}**{mark}<br><sub>{short}</sub> | {env} | {render_links(entry["links"])} |')
    return lines + ['']

def render_must_read(entry: dict, zh: bool, as_of: date) -> list[str]:
    # Keep NEW off the heading so its generated anchor never changes over time.
    mark = f' {NEW}' if is_new(entry, as_of) else ''
    meta = ' '.join(part for part in [display_venue(entry), entry['year'] or ''] if part)
    meta = ' · '.join(part for part in [meta, ' / '.join(entry['env'])] if part)
    return [f'#### {entry["title"]}', '', meta, '', render_links(entry['links']) + mark, '', entry['highlight_zh' if zh else 'highlight'], '']

def room_icon(key: str) -> str:
    return f'<img src="assets/rooms/{key}.svg" width="88" height="28" alt="" align="absmiddle">'

def render_recent(native: list[dict], zh: bool, as_of: date) -> list[str]:
    lines = ['## 最近新增' if zh else "## What's new", '']
    recent = recent_first([e for e in native if is_new(e, as_of)])
    if not recent:
        latest = recent_first(native)[:5]
        lines += [f'最近 30 天暂无新增。最近一批收录于 {latest[0]["added"]}：' if zh else f'Nothing added in the last 30 days. The latest batch arrived on {latest[0]["added"]}:', '']
        return lines + [f'- {entry_link(e)}' for e in latest] + ['']
    months = sorted({f'20{arxiv_id(e)[0] // 100:02d}-{arxiv_id(e)[0] % 100:02d}' for e in recent if arxiv_id(e)[0]})
    span = f'{months[0]} to {months[-1]}' if len(months) > 1 else (months[0] if months else '')
    lines += [f'{recent[0]["added"]} 新增 {len(recent)} 条' + (f'，覆盖 {span} 的 arXiv 论文。' if span else '。') if zh else f'{len(recent)} entries added on {recent[0]["added"]}' + (f', covering arXiv papers from {span}.' if span else '.'), '']
    header = ['| 论文 | 房间 | 环境 | 链接 |' if zh else '| Paper | Room | Env | Links |', '| --- | :--: | :--: | --- |']
    def row(e: dict) -> str:
        room = SHORT_LABELS[e['section']][1 if zh else 0]
        title = escape(e['title']).replace('|', '&#124;')
        short = escape(e['short_zh' if zh else 'short']).replace('|', '&#124;')
        return f'| [**{title}**](#{entry_anchor(e)})<br><sub>{short}</sub> | {room} | {"<br>".join(e["env"])} | {render_links(e["links"])} |'
    lines += header + [row(e) for e in recent[:6]] + ['']
    if len(recent) > 6:
        lines += ['<details>', f'<summary>其余 {len(recent) - 6} 条新增</summary>' if zh else f'<summary>{len(recent) - 6} more additions</summary>', '']
        lines += header + [row(e) for e in recent[6:]] + ['', '</details>', '']
    return lines

def render_readme(data: dict, zh: bool, as_of: date) -> str:
    all_active, native = active_entries(data), native_entries(data)
    adjacent = [e for e in all_active if e['scope'] == 'alfworld-adjacent']
    counts = room_counts(native)
    top_badges = [
        f'[![Awesome]({shield("awesome", "AI2-THOR", "1F2A30")})](https://awesome.re)',
        f'![Entries]({shield("entries", str(len(native)), "1F2A30")})',
        f'![Papers through]({shield("papers through", papers_through(native) or data["updated"], "1F2A30")})',
        f'[![Stars](https://img.shields.io/github/stars/{REPO}?style=flat-square&color=1F2A30)](https://github.com/{REPO})',
        f'[![Link check](https://img.shields.io/github/actions/workflow/status/{REPO}/link-check.yml?branch=main&style=flat-square&label=link%20check&color=1F2A30)](https://github.com/{REPO}/actions/workflows/link-check.yml)',
    ]
    lines = ['<!-- Generated from data.yml. Run python scripts/generate_readme.py. -->', '<picture>', '  <source media="(prefers-color-scheme: dark)" srcset="assets/floorplan-dark.svg">', '  <img src="assets/floorplan-light.svg" alt="Floor plan of the list: each room is a section, sized by number of entries" width="1200">', '</picture>', '', '# Awesome AI2-THOR', '', 'AI2-THOR 及其家族的论文、基准与工具地图。' if zh else 'A map of papers, benchmarks, and tools built on AI2-THOR and its family.', '', ' '.join(top_badges), '', f'[网站]({SITE_URL}) / [English](README.md) / [参与贡献](CONTRIBUTING.md)' if zh else f'[Website]({SITE_URL}) / [中文](README.zh-CN.md) / [Contribute](CONTRIBUTING.md)', '']
    lines += render_routes(all_active, zh) + render_family(all_active, zh)
    lines += render_recent(native, zh, as_of)
    lines += ['## 目录' if zh else '## Contents', '']
    for category, _, label, label_zh, _, _, note, note_zh in ROOMS:
        lines.append(f'- [{label_zh if zh else label}](#{slugify(category)}) <sub>{counts[category]}</sub> — {note_zh if zh else note}')
    lines += ['', f'{len(native)} 条模拟器家族资源；另附 {len(adjacent)} 条 ALFWorld 文本环境工作。' if zh else f'{len(native)} simulator-family resources; {len(adjacent)} text-only ALFWorld papers appear in a separate appendix.', '']
    for category, key, label, label_zh, _, _, note, note_zh in ROOMS:
        # Explicit anchors keep Contents links stable even with the icon in the heading.
        lines += [f'<a id="{slugify(category)}"></a>', '']
        lines += [f'## {room_icon(key)} {label_zh if zh else label}', '', f'{note_zh if zh else note} {counts[category]} 条。' if zh else f'{note} {counts[category]} entries.', '']
        entries = [e for e in native if e['category'] == category]
        for entry in entries:
            if entry['must_read']: lines += render_must_read(entry, zh, as_of)
        remaining = sort_entries([e for e in entries if not e['must_read']])
        if len(entries) > 15:
            lines += ['**最新条目**' if zh else '**Latest entries**', '']
            lines += render_table(remaining[:5], zh, as_of)
            lines += ['<details>', f'<summary>全部 {len(entries)} 条（另 {len(remaining[5:])} 条）</summary>' if zh else f'<summary>All {len(entries)} entries ({len(remaining[5:])} more below)</summary>', '']
            lines += render_table(remaining[5:], zh, as_of) + ['</details>', '']
        elif remaining:
            lines += render_table(remaining, zh, as_of)
        if key == 'planning' and adjacent:
            lines += ['<details>', f'<summary>ALFWorld 相关工作（纯文本，{len(adjacent)} 条）</summary>' if zh else f'<summary>ALFWorld-adjacent work (text-only, {len(adjacent)})</summary>', '', '这些论文使用 ALFWorld 文本任务，不据此认定其运行了 THOR 视觉模拟器；不计入房间条目数。' if zh else 'These papers use ALFWorld text tasks; this does not establish execution in the THOR visual simulator. They are excluded from room counts.', '']
            lines += render_table(adjacent, zh, as_of) + ['</details>', '']
    envs = ecosystem_counts(native)
    lines += ['## 数据一览' if zh else '## By the numbers', '', '<picture>', '  <source media="(prefers-color-scheme: dark)" srcset="assets/timeline-dark.svg">', f'  <img src="assets/timeline-light.svg" alt="{"按发表年份统计的资源" if zh else "Entries by publication year"}" width="1200">', '</picture>', '', ' / '.join(f'{env} {count}' for env, count in envs.most_common()), '', f'共跟踪 {len(data["entries"])} 条：{len(native)} 条模拟器家族资源，{len(adjacent)} 条文本环境工作，{len(data["entries"])-len(all_active)} 条待核实。' if zh else f'{len(data["entries"])} tracked records: {len(native)} simulator-family resources, {len(adjacent)} text-only papers, and {len(data["entries"])-len(all_active)} candidates awaiting verification.', '', '年份未知的资源不计入柱状图；生态标签可重叠。展示更新日期与论文核验日期分别记录。' if zh else 'Undated resources are omitted from the chart; ecosystem labels can overlap. Presentation updates and source verification dates are tracked separately.', '', '## 参与贡献' if zh else '## Contributing', '', '先编辑 `data.yml`，再校验并重新生成全部产物：' if zh else 'Edit `data.yml`, then validate and regenerate every view:', '', '```bash', 'python -m pip install -r requirements.txt', 'make check', '```', '', '[贡献指南](CONTRIBUTING.md)' if zh else '[Contribution guide](CONTRIBUTING.md)', '', '## Star history', '', f'[![Star history](https://api.star-history.com/svg?repos={REPO}&type=Date)](https://star-history.com/#{REPO}&Date)', '', '## 许可' if zh else '## License', '', '[CC0-1.0](LICENSE). Archivo: [SIL Open Font License](assets/fonts/OFL.txt).', '']
    return '\n'.join(lines)

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--as-of', type=date.fromisoformat, default=today(), help='Reference date for NEW badges; defaults to today in Asia/Shanghai.')
    args = parser.parse_args()
    data = load_data()
    generate_assets(data, args.as_of)
    for zh, filename in [(False, 'README.md'), (True, 'README.zh-CN.md')]:
        (ROOT / filename).write_text(render_readme(data, zh, args.as_of), encoding='utf-8')
    from generate_site import generate_site
    generate_site(data, args.as_of)
    print('Generated both READMEs, floor plans, timeline, web font, and docs/index.html.')

if __name__ == '__main__':
    main()
