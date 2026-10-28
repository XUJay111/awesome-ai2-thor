# Contributing

This is an index of AI2-THOR-family research and tools. Keep the connection to the simulator, task, or dataset clear and cite primary sources.

## Scope and evidence

- Include work using or extending AI2-THOR, iTHOR, RoboTHOR, ProcTHOR, ManipulaTHOR, ArchitecTHOR, ALFRED, TEACh, or EmbodiedBench.
- Use paper, proceedings, official project, code, or dataset links. Check mixed-simulator work carefully.
- Keep original paper titles and venue names. Do not infer acceptance or invent experimental results.
- Put uncertain resources in `needs-verification`; state exactly what to verify in the summary.
- Mark papers evaluated only in the ALFWorld text environment as `scope: alfworld-adjacent`. They belong in Planning, have `env: [ALFWorld]`, and cannot be must-reads. The original ALFWorld text-to-visual bridge remains in the simulator-family index.
- Tutorials belong in `Tutorials and Notes` with `status: tutorial`.

## Source of truth

Edit `data.yml` and the generators. Both READMEs, all three SVGs, the web font, and `docs/index.html` are generated outputs. Never hand-edit them. Website source lives in `scripts/templates/index.html`; shared room metadata and colors live in `scripts/catalog.py`.

The site is a single HTML file with embedded data and a locally bundled Archivo font. It has no framework, external scripts, or runtime package dependencies. Its font is distributed under the [SIL Open Font License](assets/fonts/OFL.txt).

## Entry fields

```yaml
- title: "ProcTHOR: Large-Scale Embodied AI Using Procedural Generation"
  year: '2022'
  venue: NeurIPS
  status: verified-paper
  category: Platforms and Environment Generation
  section: platforms
  env: [ProcTHOR]
  tags: ['2022', NeurIPS, procedural generation]
  scope: thor-native
  must_read: true
  highlight: "Generates interactive ProcTHOR houses procedurally, making scene diversity a scalable training resource for navigation."
  short: "Procedurally generated interactive houses"
  highlight_zh: "程序化生成可交互的 ProcTHOR 房屋，为导航训练提供可扩展的场景多样性。"
  short_zh: "程序化生成的可交互房屋"
  summary: "Generates interactive ProcTHOR houses for navigation and household interaction."
  ai2thor_connection: ProcTHOR
  links:
    paper: https://arxiv.org/abs/2206.06994
    code: https://github.com/allenai/procthor
  added: '2026-06-22'
  last_verified: '2026-06-23'
```

- `highlight`: at most 30 English words; explain the contribution, environment, and use. Must-reads display this copy.
- `short`: at most 15 English words; state a concrete contribution. Tables and search results display this copy.
- Add matching Chinese copy in `highlight_zh` and `short_zh`; retain English resource titles.
- Each section has 2–4 native must-reads, selected for their role as an entry point or reusable reference.
- `section` must match `category`; the ten keys and room colors are defined in `scripts/catalog.py`.
- `added` is the actual catalog inclusion date. Existing dates were recovered from the first committed occurrence of each title in Git history. Rewriting copy does not reset this date.
- `last_verified` records source verification, separately from the top-level `updated` presentation date. Do not advance verification dates without checking sources.
- NEW marks use a rolling, inclusive 0–30 day window in Asia/Shanghai. Future dates are rejected. Only native work can appear in What's new.
- Active statuses are `verified-paper`, `verified-project`, and `tutorial`; candidates and `out-of-scope` records stay outside published views.

The prose validator rejects formulaic inclusion statements and promotional wording. These checks apply to summaries and editorial highlights; official academic titles, venue metadata, and their stable anchors remain verbatim.

## Generate and check

Use Python 3.11 or later:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
make generate
make check
```

`make generate` updates both languages, both floor plans, the publication-year chart, the web font, and the site. `make check` validates curation, runs Python regression checks, regenerates all outputs, and fails if any were stale. A passing second run confirms byte-for-byte stability.

For reproducible date-sensitive checks:

```bash
python scripts/generate_readme.py --as-of 2026-10-28
```

For JavaScript behavior and Mermaid syntax checks, install development dependencies with Node.js 20.19 or later:

```bash
npm ci
npm test
```

These checks exercise filtering, search, shared URLs, scope isolation, focusable controls, and Mermaid parsing in a DOM test environment. They do not replace visual browser checks.

## Preview and publish

```bash
make preview
```

Open `http://127.0.0.1:8000`. Check desktop and narrow layouts, system dark mode, reduced motion, and keyboard focus. Search, room, environment, and year filters are encoded in the URL; the optional text-only filter uses `text=1`.

The Pages workflow uploads only `docs/`. After merging, choose **GitHub Actions** in the repository's **Settings / Pages / Build and deployment / Source**. The workflow runs on pushes to `main`, manual dispatch, and a daily schedule; it rebuilds the site so NEW labels expire. It does not commit scheduled changes back into the source branch. README badges update when the generator is next run and committed.

Preview the README on GitHub to verify the hosted Mermaid renderer. Generated SVG text is outlined, so images do not depend on GitHub loading fonts. GitHub handles Markdown table scrolling on narrow screens.

## Review policy

Keep changes focused and fix broken links before adding resources. Preserve all original primary URLs when changing presentation. Maintain at least 300 active resources across the native index and the explicitly labeled text-only appendix; never promote a candidate to meet a count. Room counts, navigation filters, and the timeline include native resources only. `archive/data.md` is historical reference data.
