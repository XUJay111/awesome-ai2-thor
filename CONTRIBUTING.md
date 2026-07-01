# Contributing

This repository is a curated AI2-THOR-family research index, not a general embodied AI awesome list. Contributions should make the AI2-THOR connection easy to verify.

## Scope

Directly in scope:

- Work that uses, extends, evaluates, wraps, visualizes, or generates data for AI2-THOR, iTHOR, RoboTHOR, ProcTHOR, ManipulaTHOR, ArchitecTHOR, ALFRED, TEACh, or EmbodiedBench.
- Official ecosystem platforms, benchmarks, datasets, tools, and challenge infrastructure.
- Community tools and tutorials when they directly support AI2-THOR-family workflows.

Use caution for ALFRED-derived, EmbodiedBench-derived, Habitat-mixed, or other simulator-mixed work. The entry summary must explain the AI2-THOR-family connection.

Out of scope:

- Generic embodied AI papers without a verifiable AI2-THOR-family connection.
- Pure real-world robot systems with no AI2-THOR-family simulator, dataset, or benchmark usage.
- Pure VLM/LLM agent papers unless their evaluation or released code uses an AI2-THOR-family task.

## Acceptance Criteria

- Use primary sources where available: paper, proceedings page, official project page, or official repository.
- Every academic entry must include a `Links:` line with at least one primary source.
- Blog posts and tutorials belong only in `Tutorials and Notes`.
- Secondary Chinese blogs may remain as learning resources, but academic entries should cite papers, project pages, or official code first.
- Do not guess venue/status. Use `arXiv` or `needs-verification` when uncertain.

## Entry Format

README entries are generated from `data.yml` and follow this format:

```markdown
### Title

`year` `venue/status` `topic` `ecosystem`

Links: [Paper](paper-url) · [Project](project-url) · [Code](repo-url)

One concise paragraph explaining how the work uses, extends, benchmarks, or supports AI2-THOR-family systems.
```

Rules:

- Keep the summary to one concise paragraph, usually 1-3 sentences.
- Keep the tag order as `year`, `venue/status`, `task/domain`, `AI2-THOR connection` where possible.
- Put venue/status in tags, not buried in the summary paragraph.
- Prefer `Paper`, `Project`, and `Code` labels for primary links.
- Keep `tags` non-empty, even for tutorials and notes.
- Include `year` and `venue` fields for every entry. Use `null` only when the value is genuinely unknown or not applicable.

## Generated README Portal

`README.md` is generated from `data.yml`; do not hand-edit portal sections in the README. The generator builds:

- `At a Glance`: active entries, total tracked entries, papers, code repositories, recent entries, and ecosystem coverage.
- `Research Map`: major directions linked to the relevant README sections.
- `Curated Routes`: fixed learning paths for new users, ObjectNav/RoboTHOR, ALFRED/TEACh, ProcTHOR, and LLM/VLM agents.
- `Recent Frontier`: the newest active 2025-2026 entries.
- The full category index and entry list.

After any data or generator change, run both validation and README generation and confirm a second generator run is stable.

## Status Labels

- `verified-paper`: Paper link and AI2-THOR-family connection have been checked.
- `verified-project`: Project or code link has been checked, but no corresponding paper is confirmed.
- `tutorial`: Tutorial, blog post, course note, or walkthrough.
- `needs-verification`: Candidate entry that needs source cleanup before it enters the README main list.
- `out-of-scope`: Checked item that should not be added, to avoid repeated discussion.

## Category Guide

- `Platforms and Environment Generation`: Core simulators, generated environments, and ecosystem extensions.
- `Benchmarks and Evaluation`: Benchmarks, challenges, evaluation interfaces, and benchmark variants.
- `Instruction Following and Household Tasks`: ALFRED, TEACh, and language-grounded household task methods.
- `Navigation`: ObjectNav, semantic navigation, and navigation-analysis work.
- `Planning, Memory, and Multi-Agent Systems`: Planning, memory, dialogue, assistance, and multi-agent systems.
- `RL-Trained VLM Agents`: VLM-agent training work using AI2-THOR-family evaluation.
- `Perception, Physics, and Scene Graphs`: Perception, physical reasoning, scene graphs, and object interaction.
- `Datasets and Assets`: Datasets, imported assets, and derived benchmark resources.
- `Tools and Environments`: Wrappers, infrastructure, visualization, and community environments.
- `Tutorials and Notes`: Secondary/community learning resources.

## Verification Checklist

- [ ] The entry has a clear AI2-THOR-family connection.
- [ ] I used primary links where available.
- [ ] I added or updated `last_verified`.
- [ ] I placed the entry in the correct category.
- [ ] I ran `python scripts/validate_data.py`.
- [ ] I regenerated README if data changed.

## How to Add an Entry

1. Edit `data.yml`.
2. Use `last_verified` in `YYYY-MM-DD` format.
3. Run `python scripts/validate_data.py`.
4. Run `python scripts/generate_readme.py`.
5. Check `git diff` and confirm README changes are generated from data.

## Review Policy

- Keep a pull request focused on one topic or a small related group of entries.
- Entries without an AI2-THOR-family connection explanation are not accepted.
- Broken-link fixes take priority over new entries.
- If venue/status is uncertain, use `arXiv` or `needs-verification`; do not infer acceptance.
- Prefer primary paper, proceedings, project, dataset, or official repository links over secondary blogs and broad paper lists.

## Maintenance Notes

- `data.yml` is the source of truth.
- `README.md` is generated and should stay stable after repeated generator runs.
- `archive/data.md` is retained as historical draft data only.
- Link-check allowlists should include comments explaining unstable or rate-limited sites.
- Keep the generated README at or above 300 active entries. Active entries are `verified-paper`, `verified-project`, and `tutorial`; `needs-verification` and `out-of-scope` entries do not count.
- Preserve a candidate pool for uncertain or tangential items by using `needs-verification`. Candidate summaries must state exactly what needs to be verified before promotion.
- Do not promote a candidate just to maintain the count. Add verified primary-source entries first, then rerun validation to confirm the active count.
