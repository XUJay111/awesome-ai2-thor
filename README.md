# Awesome AI2-THOR

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)
[![Markdown](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/markdown.yml/badge.svg)](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/markdown.yml)
[![Link Check](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/link-check.yml/badge.svg)](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/link-check.yml)
[![Data Validation](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/validate-data.yml/badge.svg)](https://github.com/XUJay111/awesome-ai2-thor/actions/workflows/validate-data.yml)

Maintained as a curated research index. Last verified: 2026-06.

A curated map of papers, benchmarks, datasets, environments, and tools built on top of [AI2-THOR](https://ai2thor.allenai.org/) and its ecosystem, including iTHOR, RoboTHOR, ProcTHOR, ManipulaTHOR, ArchitecTHOR, ALFRED, TEACh, and EmbodiedBench.

This is an AI2-THOR-family index, not a general embodied AI awesome list. Each entry should make its AI2-THOR-family connection clear through primary paper, project, or code links whenever possible.

## At a Glance

| Metric | Count |
| --- | ---: |
| Active README entries | 306 |
| Total tracked entries | 319 |
| Paper entries | 261 |
| Entries with code repositories | 110 |
| 2024-2026 entries | 151 |
| AI2-THOR-family ecosystems represented | 10 |

## Research Map

| Direction | Use This For | Sections |
| --- | --- | --- |
| Simulators and generated worlds | AI2-THOR, RoboTHOR, ProcTHOR, ManipulaTHOR, ArchitecTHOR, and generated-scene extensions. | [Platforms and Environment Generation](#platforms-and-environment-generation), [Datasets and Assets](#datasets-and-assets) |
| Benchmarks and safety | Shared tasks, challenge infrastructure, robustness checks, and safety-oriented evaluations. | [Benchmarks and Evaluation](#benchmarks-and-evaluation) |
| ObjectNav and RoboTHOR | Object-goal navigation, zero-shot navigation, semantic maps, and sim-to-real navigation analysis. | [Navigation](#navigation), [Tools and Environments](#tools-and-environments) |
| ALFRED and TEACh | Instruction following, dialogue-grounded household tasks, and long-horizon execution. | [Instruction Following and Household Tasks](#instruction-following-and-household-tasks), [Benchmarks and Evaluation](#benchmarks-and-evaluation) |
| LLM/VLM embodied agents | Foundation-model agents, RL-trained VLM agents, prompting, reasoning, and closed-loop evaluation. | [RL-Trained VLM Agents](#rl-trained-vlm-agents), [Planning, Memory, and Multi-Agent Systems](#planning-memory-and-multi-agent-systems) |
| Planning, memory, and collaboration | Search, replanning, memory systems, multi-agent coordination, and human-agent assistance. | [Planning, Memory, and Multi-Agent Systems](#planning-memory-and-multi-agent-systems) |
| Perception and physical reasoning | Scene graphs, affordances, spatial understanding, physics, reconstruction, and interaction perception. | [Perception, Physics, and Scene Graphs](#perception-physics-and-scene-graphs) |
| Tools and reproducibility | Simulator wrappers, training code, evaluation harnesses, documentation, and community utilities. | [Tools and Environments](#tools-and-environments), [Tutorials and Notes](#tutorials-and-notes) |

## Curated Routes

### New to AI2-THOR

Start with the simulator, official docs, and a benchmark overview before diving into task-specific papers.

[AI2-THOR: An Interactive 3D Environment for Visual AI](#ai2-thor-an-interactive-3d-environment-for-visual-ai) -> [AI2-THOR Documentation](#ai2-thor-documentation) -> [EmbodiedBench: Comprehensive Benchmarking MLLMs for Vision-Driven Embodied Agents](#embodiedbench-comprehensive-benchmarking-mllms-for-vision-driven-embodied-agents)

### ObjectNav and RoboTHOR

Follow the path from sim-to-real navigation to ObjectNav evaluation and modern zero-shot navigation methods.

[RoboTHOR: An Open Simulation-to-Real Embodied AI Platform](#robothor-an-open-simulation-to-real-embodied-ai-platform) -> [AllenAct ObjectNav Tutorial](#allenact-objectnav-tutorial) -> [Simple but Effective: CLIP Embeddings for Embodied AI](#simple-but-effective-clip-embeddings-for-embodied-ai)

### ALFRED / TEACh instruction following

Use the benchmark papers and official resources to understand household task execution and dialogue-grounded agents.

[ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks](#alfred-a-benchmark-for-interpreting-grounded-instructions-for-everyday-tasks) -> [TEACh: Task-driven Embodied Agents that Chat](#teach-task-driven-embodied-agents-that-chat) -> [ALFRED Documentation and Leaderboards](#alfred-documentation-and-leaderboards)

### ProcTHOR and scene generation

Track procedural scale, generated assets, and language-guided environment creation.

[ProcTHOR: Large-Scale Embodied AI Using Procedural Generation](#procthor-large-scale-embodied-ai-using-procedural-generation) -> [ProcTHOR-10K Repository](#procthor-10k-repository) -> [Holodeck: Language Guided Generation of 3D Embodied AI Environments](#holodeck-language-guided-generation-of-3d-embodied-ai-environments)

### LLM/VLM embodied agents

Compare planner benchmarks, foundation-model agents, memory, and RL-based embodied reasoning.

[LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents](#lota-bench-benchmarking-language-oriented-task-planners-for-embodied-agents) -> [Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making](#embodied-agent-interface-benchmarking-llms-for-embodied-decision-making) -> [Embodied-Reasoner](#embodied-reasoner)

## Recent Frontier

- 2026: [TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning](#triage-role-typed-credit-assignment-for-agentic-reinforcement-learning)
- 2026: [Self-Evolving World Models for LLM Agent Planning](#self-evolving-world-models-for-llm-agent-planning)
- 2026: [DuoMem: Towards Capable On-Device Memory Agents via Dual-Space Distillation](#duomem-towards-capable-on-device-memory-agents-via-dual-space-distillation)
- 2026: [UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation](#ucob-learning-to-utilize-and-evolve-agentic-skills-via-credit-aware-on-policy-bidirectional-self-distillation)
- 2026: [Selective Memory Retention for Long-Horizon LLM Agents](#selective-memory-retention-for-long-horizon-llm-agents)
- 2026: [ATOD: Annealed Turn-aware On-policy Distillation for Multi-turn Autonomous Agents](#atod-annealed-turn-aware-on-policy-distillation-for-multi-turn-autonomous-agents)
- 2026: [OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning](#opid-on-policy-skill-distillation-for-agentic-reinforcement-learning)
- 2026: [SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills](#skill-disco-distilling-and-compiling-agent-traces-into-reusable-procedural-skills)
- 2026: [Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents](#semantic-consistency-policy-optimization-for-reinforcement-learning-of-llm-agents)
- 2026: [BiPACE: Bisimulation-Guided Policy Optimization with Action Counterfactual Estimation for LLM Agents](#bipace-bisimulation-guided-policy-optimization-with-action-counterfactual-estimation-for-llm-agents)
- 2026: [SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation](#sage-nav-leveraging-llm-planning-and-alignment-fusion-for-hierarchical-scene-graph-guided-navigation)
- 2026: [The Interplay of Harness Design and Post-Training in LLM Agents](#the-interplay-of-harness-design-and-post-training-in-llm-agents)

## Project Index

- Coverage: 306 active entries across 10 sections (319 total tracked entries).
- Status mix: verified-paper (261), verified-project (40), tutorial (5).
- Timeline: 2017 (4), 2018 (4), 2019 (8), 2020 (11), 2021 (24), 2022 (29), 2023 (41), 2024 (54), 2025 (41), 2026 (56), unknown (34).
- Ecosystems: AI2-THOR / iTHOR (257), RoboTHOR (34), ProcTHOR (27), ManipulaTHOR (3), ArchitecTHOR (1), ALFRED (78), TEACh (13), EmbodiedBench (15), MAP-THOR / MAT-THOR (3), Other THOR variants (2).
- Task themes: Instruction following (112), Navigation / ObjectNav (120), Planning and memory (136), Multi-agent collaboration (62), Manipulation (16), Rearrangement / tidying (8), Dialogue and assistance (16), Safety and physical reasoning (43), Scene generation and assets (35).
- Resources: papers (261), project pages (44), code repositories (110), datasets (6), challenges/workshops (2), tutorials/notes (5).

Section counts:

- [Platforms and Environment Generation](#platforms-and-environment-generation): 12
- [Benchmarks and Evaluation](#benchmarks-and-evaluation): 28
- [Instruction Following and Household Tasks](#instruction-following-and-household-tasks): 54
- [Navigation](#navigation): 80
- [Planning, Memory, and Multi-Agent Systems](#planning-memory-and-multi-agent-systems): 53
- [RL-Trained VLM Agents](#rl-trained-vlm-agents): 17
- [Perception, Physics, and Scene Graphs](#perception-physics-and-scene-graphs): 23
- [Datasets and Assets](#datasets-and-assets): 10
- [Tools and Environments](#tools-and-environments): 24
- [Tutorials and Notes](#tutorials-and-notes): 5

## Contents

- [Platforms and Environment Generation](#platforms-and-environment-generation)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [Instruction Following and Household Tasks](#instruction-following-and-household-tasks)
- [Navigation](#navigation)
- [Planning, Memory, and Multi-Agent Systems](#planning-memory-and-multi-agent-systems)
- [RL-Trained VLM Agents](#rl-trained-vlm-agents)
- [Perception, Physics, and Scene Graphs](#perception-physics-and-scene-graphs)
- [Datasets and Assets](#datasets-and-assets)
- [Tools and Environments](#tools-and-environments)
- [Tutorials and Notes](#tutorials-and-notes)

## Platforms and Environment Generation

*Core simulators, generated environments, and official ecosystem extensions.*

### AI2-THOR: An Interactive 3D Environment for Visual AI

`2017` `platform` `interactive simulation`

Links: [Paper](https://arxiv.org/abs/1712.05474) · [Project](https://ai2thor.allenai.org/) · [Code](https://github.com/allenai/ai2thor)

AI2-THOR is the base interactive simulator for household embodied AI. It provides visually rich indoor scenes, navigation, physics-enabled object interaction, metadata, and a Python controller API, making it the foundation for many later navigation, manipulation, rearrangement, and instruction-following benchmarks.

### RoboTHOR: An Open Simulation-to-Real Embodied AI Platform

`2020` `CVPR` `sim-to-real` `navigation`

Links: [Paper](https://arxiv.org/abs/2004.06799) · [Project](https://ai2thor.allenai.org/robothor/) · [Code](https://github.com/allenai/ai2thor)

RoboTHOR extends AI2-THOR with paired simulated and real physical spaces, allowing researchers to quantify the transfer gap between simulation-trained navigation agents and real-world robot deployment. It helped turn sim-to-real generalization from an informal concern into a benchmarked research problem.

### ManipulaTHOR: A Framework for Visual Object Manipulation

`2021` `CVPR` `manipulation` `mobile arm`

Links: [Paper](https://arxiv.org/abs/2104.11213) · [Project](https://ai2thor.allenai.org/manipulathor/) · [Code](https://github.com/allenai/manipulathor)

ManipulaTHOR expands AI2-THOR from navigation-only agents to mobile manipulation. It introduces arm-based interaction tasks such as ArmPointNav, where agents must reason about visual observations, navigation, occlusion, obstacle avoidance, and object manipulation in one closed-loop setting.

### Visual Room Rearrangement

`2021` `CVPR` `rearrangement` `benchmark`

Links: [Paper](https://arxiv.org/abs/2103.16544) · [Project](https://ai2thor.allenai.org/rearrangement/) · [Code](https://github.com/allenai/ai2thor-rearrangement)

Visual Room Rearrangement asks agents to observe a reference room state and then restore displaced objects and object states. The task moves beyond finding a target object: agents must remember, compare, navigate, interact, and repair a scene over a long sequence of actions.

### ProcTHOR: Large-Scale Embodied AI Using Procedural Generation

`2022` `NeurIPS` `procedural generation` `scaling`

Links: [Paper](https://arxiv.org/abs/2206.06994) · [Project](https://procthor.allenai.org/) · [Code](https://github.com/allenai/procthor)

ProcTHOR brings large-scale procedural generation into the AI2-THOR ecosystem. It generates diverse, semantically plausible, interactive household environments and shows that environment scale and diversity can substantially improve generalization across navigation, rearrangement, and manipulation tasks.

### Phone2Proc: Bringing Robust Robots Into Our Chaotic World

`2022` `arXiv` `sim-to-real` `conditional generation`

Links: [Paper](https://arxiv.org/abs/2212.04819) · [Project](https://allenai.org/project/phone2proc) · [Code](https://github.com/allenai/phone2proc)

Phone2Proc conditions procedural scene generation on a quick phone scan of a target real-world environment. The generated training scenes preserve large-scale layout while randomizing clutter, materials, lighting, and object placement, improving sim-to-real robustness for ObjectNav.

### Holodeck: Language Guided Generation of 3D Embodied AI Environments

`2024` `CVPR` `language-guided generation` `Objaverse`

Links: [Paper](https://arxiv.org/abs/2312.09067) · [Project](https://yueyang1996.github.io/holodeck/) · [Code](https://github.com/allenai/Holodeck)

Holodeck uses language prompts, LLM-based scene planning, Objaverse assets, and AI2-THOR-compatible interaction to generate embodied AI environments. It targets open-ended scene types and semantic layouts that are difficult to cover with hand-authored procedural rules alone.

### SPOC: Imitating Shortest Paths in Simulation Enables Effective Navigation and Manipulation in the Real World

`2024` `CVPR` `ProcTHOR` `sim-to-real`

Links: [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Ehsani_SPOC_Imitating_Shortest_Paths_in_Simulation_Enables_Effective_Navigation_and_CVPR_2024_paper.html) · [Project](https://spoc-robot.github.io/) · [Code](https://github.com/allenai/spoc-robot-training)

SPOC uses AI2-THOR and ProcTHOR to generate large-scale shortest-path demonstrations for navigation and manipulation, then transfers the resulting policies to real robots. It is an important sim-to-real example of scaling training data through the AI2-THOR ecosystem.

### Beyond Needle(s) in the Embodied Haystack

`2025` `arXiv` `long-horizon` `benchmark generation`

Links: [Paper](https://arxiv.org/abs/2505.16928)

This work introduces infinity-THOR, a long-horizon embodied task framework for extreme-context reasoning. It generates scalable trajectories and a Needle(s) in the Embodied Haystack task where agents must reason over long action-observation histories.

### DualTHOR

`2025` `environment` `dual-arm humanoid` `AI2-THOR`

Links: [Code](https://github.com/ds199895/DualTHOR) · [arXiv](https://arxiv.org/abs/2506.16012)

DualTHOR is a lightweight dual-arm humanoid simulation environment built on AI2-THOR. Its repository adds dual-arm task setup, parallel arm execution, task replay, contingency modeling, inverse-kinematics-based actions, and more detailed object state transitions; the linked arXiv record is currently withdrawn, so this entry is tracked as a verified project.

### Enhancing Multi-Agent Systems via Reinforcement Learning with LLM-based Planner and Graph-based Policy

`2025` `arXiv` `planning` `multi-agent`

Links: [arXiv](https://arxiv.org/abs/2503.10049)

This work uses AI2-THOR for embodied safety evaluation and planning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### SPREAD: Spatial-Physical REasoning via geometry Aware Diffusion

`2026` `arXiv` `ProcTHOR`

Links: [arXiv](https://arxiv.org/abs/2603.27573)

This work uses ProcTHOR for scene generation and environment design. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

## Benchmarks and Evaluation

*Benchmarks, challenges, and evaluation interfaces with a concrete AI2-THOR-family connection.*

### IQA: Visual Question Answering in Interactive Environments

`2018` `CVPR` `interactive QA` `AI2-THOR`

Links: [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Gordon_IQA_Visual_Question_CVPR_2018_paper.html) · [Project](https://prior.allenai.org/projects/iqa) · [Code](https://github.com/danielgordon10/thor-iqa-cvpr-2018)

IQA asks agents to answer questions that require active navigation and object interaction, such as checking inside containers. Built on AI2-THOR, it was one of the early benchmarks to move visual question answering from static images into embodied, interactive environments.

### Two Body Problem: Collaborative Visual Task Completion

`2019` `CVPR` `multi-agent` `AI2-THOR`

Links: [Paper](https://openaccess.thecvf.com/content_CVPR_2019/html/Jain_Two_Body_Problem_Collaborative_Visual_Task_Completion_CVPR_2019_paper.html)

Two Body Problem extends AI2-THOR to collaborative visual task completion with multiple agents that communicate and act in the same environment. It is an early example of multi-agent embodied interaction inside the AI2-THOR simulator.

### ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks

`2020` `CVPR` `instruction following` `household tasks`

Links: [Paper](https://arxiv.org/abs/1912.01734) · [Project](https://askforalfred.com/) · [Code](https://github.com/askforalfred/alfred)

ALFRED pairs natural-language household instructions with expert demonstrations in AI2-THOR. It is one of the central benchmarks for embodied instruction following because it combines language grounding, egocentric vision, navigation, object interaction, and irreversible state changes.

### ALFWorld: Aligning Text and Embodied Environments for Interactive Learning

`2021` `ICLR` `text-to-embodied transfer` `ALFRED`

Links: [Paper](https://arxiv.org/abs/2010.03768) · [Project](https://alfworld.github.io/) · [Code](https://github.com/alfworld/alfworld)

ALFWorld aligns TextWorld-style abstract household tasks with concrete ALFRED execution in AI2-THOR. It lets agents learn language and planning policies in a lightweight text environment, then transfer those policies to visually grounded embodied execution.

### TEACh: Task-driven Embodied Agents that Chat

`2022` `AAAI` `dialogue` `task execution`

Links: [Paper](https://arxiv.org/abs/2110.00534) · [Code](https://github.com/alexa/teach)

TEACh extends AI2-THOR household tasks with human-human dialogue between a Commander and a Follower. It evaluates whether embodied agents can use conversation to understand ambiguous goals, recover missing information, and execute long-horizon household tasks.

### DialFRED: Dialogue-Enabled Agents for Embodied Instruction Following

`2022` `IEEE RA-L` `dialogue` `ALFRED`

Links: [Paper](https://arxiv.org/abs/2202.13330) · [Code](https://github.com/xfgao/DialFRED) · [Challenge](https://eval.ai/web/challenges/challenge-page/1859/overview)

DialFRED augments ALFRED with agent-initiated clarification questions and human answers. It is useful for studying when an embodied agent should ask for missing information instead of blindly executing an underspecified instruction.

### Dialog Acts for Task-Driven Embodied Agents

`2022` `SIGDIAL` `dialogue annotation` `TEACh`

Links: [Paper](https://arxiv.org/abs/2209.12953) · [Code](https://github.com/alexa/teach)

This work annotates TEACh dialogues with dialog acts and studies how those labels help embodied task execution. It adds a pragmatic dialogue layer to AI2-THOR household tasks, making it easier to analyze instructions, questions, confirmations, corrections, and action-relevant utterances.

### ACT-Thor: A Controlled Benchmark for Embodied Action Understanding in Simulated Environments

`2022` `COLING` `action understanding` `AI2-THOR`

Links: [Paper](https://aclanthology.org/2022.coling-1.495/) · [Code](https://github.com/hannamw/ACT-Thor) · [Dataset](https://huggingface.co/datasets/mwhanna/ACT-Thor)

ACT-Thor uses AI2-THOR to create controlled before-action and after-action visual reasoning examples for grounded verb and action-effect understanding. It evaluates whether models can infer how embodied actions transform objects and scenes, rather than only recognizing static visual categories.

### Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making

`2024` `NeurIPS Datasets and Benchmarks` `LLM evaluation`

Links: [Paper](https://openreview.net/forum?id=iSwK1YqO7v) · [Project](https://embodied-agent-interface.github.io/)

Embodied Agent Interface defines a common interface for evaluating LLMs as embodied decision modules. Instead of reporting only final task success, it decomposes embodied decision making into interpretable stages such as goal interpretation, subgoal decomposition, action generation, and state transition modeling.

### LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents

`2024` `ICLR` `LLM planning` `ALFRED`

Links: [Paper](https://openreview.net/forum?id=ADSxCpCu9s) · [Project](https://choi-jaewoo.github.io/LoTa-Bench/) · [Code](https://github.com/lbaa2022/LLMTaskPlanning) · [arXiv](https://arxiv.org/abs/2402.08178)

LoTa-Bench evaluates language-oriented task planners in two embodied setups, including ALFRED with the AI2-THOR simulator. It provides an automated benchmark for comparing LLM-based planners, prompt strategies, replanning, and fine-tuning in household task execution.

### EmbodiedBench: Comprehensive Benchmarking MLLMs for Vision-Driven Embodied Agents

`2025` `ICML` `MLLM agents` `benchmark`

Links: [Paper](https://openreview.net/forum?id=DgGF2LEBPS) · [Project](https://embodiedbench.github.io/) · [Code](https://github.com/EmbodiedBench/EmbodiedBench)

EmbodiedBench evaluates multimodal large language models as closed-loop embodied agents across EB-ALFRED, EB-Habitat, EB-Navigation, and EB-Manipulation. The benchmark makes the gap between high-level semantic planning and low-level visual/action grounding explicit.

### 2023 AI2-THOR Rearrangement Challenge

`2023` `challenge` `rearrangement`

Links: [Project](https://ai2thor.allenai.org/rearrangement/) · [Code](https://github.com/allenai/ai2thor-rearrangement)

The AI2-THOR Rearrangement Challenge provides datasets, task samplers, evaluation metrics, and baselines for restoring object configurations. It is the practical challenge infrastructure around the Visual Room Rearrangement task.

### SafetyALFRED: Evaluating Safety-Conscious Planning of Multimodal Large Language Models

`2026` `ACL Findings` `safety` `ALFRED`

Links: [Paper](https://arxiv.org/abs/2604.19638) · [Code](https://github.com/sled-group/SafetyALFRED)

SafetyALFRED builds on ALFRED with kitchen hazards and safety-conscious planning tasks. It evaluates whether MLLM agents can move beyond recognizing hazards in QA form and actively plan corrective embodied actions in an interactive household setting.

### SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents

`2024` `arXiv` `safety` `AI2-THOR`

Links: [Paper](https://arxiv.org/abs/2412.13178) · [Project](https://safeagentbench.github.io/) · [Code](https://github.com/shengyin1224/SafeAgentBench) · [Dataset](https://huggingface.co/datasets/safeagentbench/SafeAgentBench)

SafeAgentBench introduces safety-aware task-planning evaluation for embodied LLM agents with hazardous and safe household tasks. Its SafeAgentEnv is based on AI2-THOR and adds high-level actions, multi-agent execution, and both execution-based and semantic evaluation for physical-risk scenarios.

### AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions

`2026` `CVPR` `safety` `SAFE-THOR`

Links: [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Ying_AGENTSAFE_Benchmarking_the_Safety_of_Embodied_Agents_on_Hazardous_Instructions_CVPR_2026_paper.pdf) · [arXiv](https://arxiv.org/abs/2506.14697)

AGENTSAFE evaluates embodied VLM agents under hazardous instructions with SAFE-THOR, a sandbox built on AI2-THOR. It combines adversarial scenarios, risk-aware instruction variants, and fine-grained diagnosis across perception, planning, and execution safety.

### AsgardBench

`2026` `arXiv` `visually grounded planning` `AI2-THOR`

Links: [Paper](https://arxiv.org/abs/2603.15888) · [Project](https://www.microsoft.com/en-us/research/blog/asgardbench-a-benchmark-for-visually-grounded-interactive-planning/) · [Code](https://github.com/microsoft/AsgardBench)

AsgardBench evaluates whether multimodal agents can adapt high-level household action plans from egocentric visual observations and minimal success/failure feedback. It is built on AI2-THOR scenes and isolates visually grounded interactive planning from navigation and low-level control noise.

### Where to Look: Can Foundation Models Reach a Target Viewpoint Through Active Exploration?

`2026` `arXiv` `active perception` `TVRBench`

Links: [Paper](https://arxiv.org/abs/2606.01247) · [Code](https://github.com/aim-uofa/TVRBench)

This work introduces Target Viewpoint Reproduction and TVRBench, a closed-loop active perception benchmark where agents move until their observation matches a target image. TVRBench uses AI2-THOR for single-room scenes and ProcTHOR-10K for multi-room scenes, exposing spatial memory and perception-to-action bottlenecks in foundation models.

### Embodied Web Agents

`2025` `NeurIPS Datasets and Benchmarks` `web agents` `AI2-THOR`

Links: [Paper](https://arxiv.org/abs/2506.15677) · [Project](https://embodied-web-agent.github.io/)

Embodied Web Agents studies agents that coordinate physical embodied interaction with web-scale information access. Its task environments include AI2-THOR indoor scenes for embodied cooking and navigation-style tasks, coupled with web interfaces for cross-domain reasoning.

### CL-ALFRED: Online Continual Learning for Interactive Instruction Following Agents

`2024` `ICLR` `continual learning` `ALFRED`

Links: [Paper](https://openreview.net/forum?id=7M0EzjugaN) · [Project](https://bhkim94.github.io/projects/CL-ALFRED/) · [Code](https://github.com/snumprlab/cl-alfred)

CL-ALFRED turns ALFRED into a continual-learning benchmark with behavior-incremental and environment-incremental streams. It measures whether embodied instruction-following agents can adapt to new tasks and scenes without catastrophically forgetting prior household skills.

### ReALFRED: An Embodied Instruction Following Benchmark in Photo-Realistic Environments

`2024` `ECCV` `ALFRED-derived` `photo-realistic benchmark`

Links: [Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1610_ECCV_2024_paper.php) · [Project](https://twoongg.github.io/projects/realfred/) · [Code](https://github.com/snumprlab/realfred)

ReALFRED extends ALFRED-style instruction following to photo-realistic scanned multi-room environments. It is included as direct ALFRED lineage, but it should be read as ALFRED-derived rather than a native AI2-THOR benchmark.

### Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems

`2026` `arXiv` `safety` `benchmark`

Links: [arXiv](https://arxiv.org/abs/2604.05427)

This work evaluates in AI2-THOR for embodied safety evaluation and planning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Detecting Non-Optimal Decisions of Embodied Agents via Diversity-Guided Metamorphic Testing

`2025` `arXiv` `planning` `benchmark`

Links: [arXiv](https://arxiv.org/abs/2512.20083)

This work evaluates in AI2-THOR for embodied task planning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### SENTINEL: A Multi-Level Formal Framework for Safety Evaluation of Foundation Model-based Embodied Agents

`2025` `arXiv` `planning` `safety`

Links: [arXiv](https://arxiv.org/abs/2510.12985)

This work evaluates in AI2-THOR for embodied safety evaluation and planning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Do LLMs Build World Models From Text? A Multilingual Diagnostic of Spatial Reasoning

`2026` `arXiv` `memory` `benchmark`

Links: [arXiv](https://arxiv.org/abs/2605.28277)

This work evaluates in ProcTHOR for embodied memory and spatial reasoning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### CoWs on Pasture: Baselines and Benchmarks for Language-Driven Zero-Shot Object Navigation

`2022` `arXiv` `ObjectNav` `navigation`

Links: [Code](https://github.com/real-stanford/cow) · [arXiv](https://arxiv.org/abs/2203.10421)

This work evaluates in RoboTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### GroundControl: Anticipating Navigation Failures in Vision-Language Agents via Trajectory-Consistent Uncertainty Estimates

`2026` `arXiv` `navigation` `safety`

Links: [arXiv](https://arxiv.org/abs/2606.20479)

This work evaluates in EmbodiedBench / EB-Navigation for embodied safety evaluation and planning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### MAEA: Multimodal Attribution for Embodied AI

`2023` `arXiv` `safety` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2307.13850)

MAEA: Multimodal Attribution for Embodied AI uses ALFRED as an embodied household-task benchmark for safety. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

### Robustness Testing of Multi-Modal Models in Varied Home Environments for Assistive Robots

`2024` `arXiv` `safety` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2406.12443)

Robustness Testing of Multi-Modal Models in Varied Home Environments for Assistive Robots reports experiments connected to AI2-THOR for safety. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

## Instruction Following and Household Tasks

*Instruction-following, household-task, and language-grounded execution methods using ALFRED, TEACh, or AI2-THOR-style tasks.*

### Are We There Yet? Learning to Localize in Embodied Instruction Following

`2021` `AAAI HAI` `ALFRED` `localization`

Links: [Paper](https://arxiv.org/abs/2101.03431)

This work focuses on localization and navigation subgoals in ALFRED. It augments the agent's field of view with multiple viewing angles, predicts relative spatial relations to target locations, and improves object grounding with pretrained detection.

### MOCA: Factorizing Perception and Policy for Interactive Instruction Following

`2021` `ICCV` `ALFRED` `object-centric policy`

Links: [Paper](https://arxiv.org/abs/2012.03208) · [Code](https://github.com/gistvision/moca)

MOCA factorizes ALFRED agents into interactive perception and action-policy streams. Its object-centric perception, language-conditioned grounding, and obstruction handling made it an important early modular baseline for interactive instruction following.

### Episodic Transformer for Vision-and-Language Navigation

`2021` `ICCV` `ALFRED` `episode memory`

Links: [Paper](https://arxiv.org/abs/2105.06453) · [Project](https://sites.google.com/view/episodictransformer) · [Code](https://github.com/alexpashevich/E.T.)

Episodic Transformer models full ALFRED episodes with a multimodal transformer over language, visual observations, and actions. It showed the value of long episode history and synthetic-instruction pretraining for compositional household tasks.

### Look Wide and Interpret Twice

`2021` `IJCAI` `ALFRED` `visual grounding`

Links: [Paper](https://arxiv.org/abs/2106.00596) · [Code](https://github.com/quangvnai/lwit-alfred)

Look Wide and Interpret Twice improves ALFRED instruction following with two-stage instruction interpretation and wider visual context. It first predicts tentative action/object structure from language, then refines decisions with panoramic and object-centric visual evidence.

### HiTUT: Hierarchical Task Learning from Language Instructions with Unified Transformers and Self-Monitoring

`2021` `Findings of ACL` `ALFRED` `hierarchical planning`

Links: [Paper](https://aclanthology.org/2021.findings-acl.368/) · [Code](https://github.com/594zyc/HiTUT)

HiTUT decomposes ALFRED into subgoal planning, navigation, and object manipulation while using unified transformer modules across the hierarchy. Its self-monitoring and task-structure modeling make failures easier to diagnose than in purely flat sequence policies.

### Embodied BERT: A Transformer Model for Embodied, Language-guided Visual Task Completion

`2021` `EMNLP NILLI` `ALFRED` `multimodal transformer`

Links: [Paper](https://arxiv.org/abs/2108.04927)

Embodied BERT applies transformer modeling to long-horizon ALFRED histories with language, panoramic object detections, and action context. It helped connect object-centric navigation targets with language-guided visual task completion.

### HLSM: Hierarchical Language-conditioned Spatial Model for Embodied Instruction Following

`2021` `CoRL` `ALFRED` `semantic maps`

Links: [Paper](https://arxiv.org/abs/2107.05612) · [Project](https://hlsm-alfred.github.io/) · [Code](https://github.com/valtsblukis/hlsm)

HLSM represents ALFRED tasks through persistent semantic spatial maps and hierarchical control. It helped establish the importance of explicit spatial memory for long-horizon instruction following, rather than relying only on recurrent hidden states or end-to-end sequence policies.

### Agent with the Big Picture

`2021` `CVPR Embodied AI Workshop` `ALFRED` `wide-view observation`

Links: [Code](https://github.com/snumprlab/abp) · [Dataset](https://huggingface.co/datasets/byeonghwikim/abp_dataset) · [Workshop](https://askforalfred.com/EAI21/)

Agent with the Big Picture augments ALFRED agents with additional observations from navigable directions, giving the policy a wider spatial context than a single egocentric frame. It is useful as a compact example of improving ALFRED execution through better observation design.

### FILM: Following Instructions in Language with Modular Methods

`2022` `ICLR` `ALFRED` `modular agent`

Links: [Paper](https://arxiv.org/abs/2110.07342) · [Code](https://github.com/soyeonm/FILM)

FILM decomposes instruction following into language parsing, semantic map construction, semantic search, and execution. Its strong ALFRED performance with less training data showed that explicit maps and modular priors can be highly competitive with end-to-end imitation learning.

### Embodied Concept Learner: Self-supervised Learning of Concepts and Mapping for Instruction Following

`2023` `CoRL` `ALFRED` `self-supervised concepts`

Links: [Paper](https://proceedings.mlr.press/v205/ding23b.html) · [Project](https://dingmyu.github.io/ecl/)

Embodied Concept Learner learns semantic and geometric concepts from embodied interaction before applying them to ALFRED instruction following. It targets the perception and mapping bottleneck in long-horizon household tasks, especially when supervised labels are limited.

### DANLI: Deliberative Agent for Following Natural Language Instructions

`2022` `EMNLP` `TEACh` `neuro-symbolic planning`

Links: [Paper](https://arxiv.org/abs/2210.12485) · [Code](https://github.com/sled-group/DANLI) · [ACL Anthology](https://aclanthology.org/2022.emnlp-main.83/)

DANLI introduces a deliberative neuro-symbolic agent for following natural-language instructions. It maintains task progress and symbolic state to reason about preconditions and subgoals, reducing purely reactive behavior in long-horizon household tasks.

### VLM-Act: A Benchmark for Vision-Language-Action Models

`2024` `ICLR Workshop` `VLA benchmark` `ALFRED`

Links: [Paper](https://arxiv.org/abs/2404.08700) · [Code](https://github.com/OSU-NLP-Group/VLM-Act)

VLM-Act evaluates vision-language-action models on action prediction and long-horizon embodied task execution. It includes ALFRED as one of its central benchmarks, using AI2-THOR-style household instruction following to test whether VLM representations transfer into executable actions.

### LACMA: Language-Aligning Contrastive Learning with Meta-Actions

`2023` `EMNLP` `ALFRED` `contrastive learning`

Links: [Paper](https://arxiv.org/abs/2310.12344) · [Code](https://github.com/joeyy5588/LACMA) · [ACL Anthology](https://aclanthology.org/2023.emnlp-main.77/)

LACMA improves ALFRED generalization by explicitly aligning language instructions with agent hidden states and introducing meta-actions as an intermediate semantic layer. The work targets the gap between natural language goals and low-level action sequences.

### SPRINT: Scalable Policy Pre-Training via Language Instruction Relabeling

`2024` `ICRA` `ALFRED` `policy pretraining`

Links: [Paper](https://arxiv.org/abs/2306.11886) · [Project](https://clvrai.github.io/sprint/) · [Code](https://github.com/clvrai/sprint)

SPRINT relabels and chains ALFRED trajectories to pretrain reusable household skills at scale. Its ALFRED-RL setup connects offline instruction relabeling with downstream long-horizon execution in the ALFRED simulator.

### LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models

`2023` `ICCV` `LLM planning`

Links: [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Song_LLM-Planner_Few-Shot_Grounded_Planning_for_Embodied_Agents_with_Large_Language_Models_ICCV_2023_paper.html) · [Project](https://dki-lab.github.io/LLM-Planner/) · [Code](https://github.com/OSU-NLP-Group/LLM-Planner)

LLM-Planner uses few-shot prompting to turn large language models into grounded high-level planners for embodied agents. It provides prompt-generation and end-to-end examples that connect language model plans to executable embodied task steps.

### Wonderful Team: Zero-Shot Physical Task Planning with Visual LLMs

`2024` `arXiv` `zero-shot planning` `AI2-THOR`

Links: [Paper](https://arxiv.org/abs/2407.19094) · [Code](https://github.com/jeongeun980906/Wonderful-Team)

Wonderful Team studies zero-shot physical task planning with visual LLMs, using AI2-THOR to evaluate whether agents can infer object states and feasible household action sequences from visual observations. It is useful for comparing direct multimodal planning against more modular embodied pipelines.

### Cook2LTL: Translating Cooking Recipes to LTL Formulae using Large Language Models

`2024` `ICRA` `formal methods` `cooking tasks`

Links: [Paper](https://arxiv.org/abs/2310.00163) · [Project](https://prg.cs.umd.edu/cook2ltl) · [Code](https://github.com/angmavrogiannis/Cook2LTL)

Cook2LTL translates natural-language cooking recipes into linear temporal logic specifications and executes them in AI2-THOR. It connects LLM semantic parsing with formal task specifications, making recipe instructions more precise and verifiable.

### DISCO: Embodied Navigation and Interaction via Differentiable Scene Semantics and Dual-level Control

`2024` `ECCV` `ALFRED` `navigation and interaction`

Links: [Paper](https://arxiv.org/abs/2407.14758) · [Code](https://github.com/AllenXuuu/DISCO)

DISCO combines differentiable scene semantics with dual-level coarse-to-fine control for ALFRED. It uses structured scene representations for navigation while keeping local interaction policies focused, showing that carefully engineered modular control remains a strong baseline.

### ThinkBot: Embodied Instruction Following with Thought Chain Reasoning

`2025` `ICLR` `ALFRED` `reasoning`

Links: [Paper](https://openreview.net/forum?id=tFDTHA3odg) · [Project](https://guanxinglu.github.io/thinkbot/) · [arXiv](https://arxiv.org/abs/2312.07062)

ThinkBot uses LLM-based thought-chain reasoning to fill in implicit intermediate subgoals that human instructions often omit. It pairs this instruction completion with object localization so that recovered subgoals can be grounded in partially observed environments.

### Dual Preference Optimization for Embodied Multimodal Agent

`2025` `arXiv` `preference optimization` `ALFRED`

Links: [Paper](https://arxiv.org/abs/2502.02024) · [Code](https://github.com/7pinkdylan/DeMo)

This work applies dual preference optimization to embodied multimodal agents, combining action-level and trajectory-level preferences for instruction following. Its evaluation includes ALFRED, making it relevant to preference-aligned policies for AI2-THOR household task execution.

### Hindsight Planner: A Closed-Loop Few-Shot Planner for Embodied Instruction Following

`2024` `arXiv` `ALFRED` `few-shot planning`

Links: [Paper](https://arxiv.org/abs/2412.19562)

Hindsight Planner frames ALFRED instruction following as closed-loop few-shot planning under partial observability. It combines adaptation, actor-critic style feedback, and hindsight relabeling so the planner can recover from suboptimal intermediate actions.

### RePlan-Bot: Multi-Level Replanning for Embodied Instruction Following

`2026` `arXiv` `ALFRED` `replanning`

Links: [Paper](https://arxiv.org/abs/2605.25851)

RePlan-Bot performs continuous multi-level replanning for ALFRED-style embodied instruction following. It combines an LLM-based high-level auditor, commonsense-guided object search, instance-map localization, and a lightweight low-level corrector to reduce long-horizon failures and risky irreversible actions.

### Recurrent Reasoning with Vision-Language Models for Estimating Long-Horizon Embodied Task Progress

`2026` `CVPR` `ALFRED-RL` `progress estimation`

Links: [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Recurrent_Reasoning_with_Vision-Language_Models_for_Estimating_Long-Horizon_Embodied_Task_CVPR_2026_paper.html)

This work uses recurrent VLM reasoning to estimate task progress for long-horizon embodied instruction following. Its ALFRED-RL experiments use AI2-THOR-based execution to turn progress estimates into denser reward signals for policy improvement.

### RoboAgent: Chaining Basic Capabilities for Embodied Task Planning

`2026` `CVPR` `ALFRED` `capability chaining`

Links: [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_RoboAgent_Chaining_Basic_Capabilities_for_Embodied_Task_Planning_CVPR_2026_paper.html)

RoboAgent trains embodied task planning by chaining basic capabilities into longer household procedures. It is relevant here because it trains and evaluates on ALFRED and EB-ALFRED-style AI2-THOR-derived tasks.

### ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures

`2026` `arXiv` `planning` `benchmark`

Links: [arXiv](https://arxiv.org/abs/2604.21232)

This work evaluates in AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### SVLL: Staged Vision-Language Learning for Physically Grounded Embodied Task Planning

`2026` `arXiv` `planning` `benchmark`

Links: [arXiv](https://arxiv.org/abs/2603.11563)

This work evaluates in AI2-THOR for embodied task planning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Towards Zero-Knowledge Task Planning via a Language-based Approach

`2026` `arXiv` `planning` `LLM`

Links: [arXiv](https://arxiv.org/abs/2601.03398)

This work uses AI2-THOR for embodied task planning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### MADRA: Multi-Agent Debate for Risk-Aware Embodied Planning

`2025` `arXiv` `planning` `memory`

Links: [arXiv](https://arxiv.org/abs/2511.21460)

This work evaluates in AI2-THOR for embodied task planning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Graphormer-Guided Task Planning: Beyond Static Rules with LLM Safety Perception

`2025` `arXiv` `planning` `safety`

Links: [arXiv](https://arxiv.org/abs/2503.06866)

This work evaluates in AI2-THOR for embodied task planning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Planning with affordances: Integrating learned affordance models and symbolic planning

`2025` `arXiv` `planning` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2502.02768)

This work uses AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner

`2024` `arXiv` `planning` `multi-agent`

Links: [Code](https://github.com/tasl-lab/LaMMA-P) · [arXiv](https://arxiv.org/abs/2409.20560)

This work evaluates in AI2-THOR for embodied task planning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Implicit and Explicit Commonsense for Multi-sentence Video Captioning

`2023` `arXiv` `ALFRED` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2303.07545)

This work uses AI2-THOR / ALFRED for embodied instruction following. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Multi-Robot Learning-Informed Task Planning Under Uncertainty

`2026` `arXiv` `planning` `ProcTHOR`

Links: [arXiv](https://arxiv.org/abs/2603.20544)

This work uses ProcTHOR for embodied task planning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Heterogeneous Embodied Multi-Agent Collaboration

`2023` `arXiv` `planning` `multi-agent`

Links: [arXiv](https://arxiv.org/abs/2307.13957)

This work evaluates in ProcTHOR for embodied task planning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Enabling Extensible Embodied Capabilities with Tools

`2026` `arXiv` `navigation` `planning`

Links: [arXiv](https://arxiv.org/abs/2605.26637)

This work evaluates in EmbodiedBench / ALFRED / EB-ALFRED / EB-Navigation for embodied instruction following. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving Embodied Agents

`2026` `arXiv` `benchmark` `VLM`

Links: [arXiv](https://arxiv.org/abs/2603.24018)

This work evaluates in EmbodiedBench / ALFRED / EB-ALFRED for embodied instruction following. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### BrainMem: Brain-Inspired Evolving Memory for Embodied Agent Task Planning

`2026` `arXiv` `navigation` `planning`

Links: [arXiv](https://arxiv.org/abs/2604.16331)

This work evaluates in EmbodiedBench / ALFRED / EB-ALFRED / EB-Navigation for embodied instruction following. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Aligning Agentic World Models via Knowledgeable Experience Learning

`2026` `arXiv` `memory` `LLM`

Links: [arXiv](https://arxiv.org/abs/2601.13247)

This work evaluates in EmbodiedBench / ALFRED / EB-ALFRED for embodied instruction following. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### World-aware Planning Narratives Enhance Large Vision-Language Model Planner

`2025` `arXiv` `planning` `benchmark`

Links: [arXiv](https://arxiv.org/abs/2506.21230)

This work evaluates in EmbodiedBench / ALFRED / EB-ALFRED for embodied instruction following. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### On-Device Robotic Planning: Eliminating Inference Redundancy for Efficient Decision-Making

`2026` `arXiv` `ALFRED` `efficient planning`

Links: [arXiv](https://arxiv.org/abs/2605.31460)

This work studies efficient robotic decision-making on ALFRED, focusing on reducing redundant reasoning calls while preserving embodied planning performance. It is relevant to AI2-THOR-family instruction-following systems because ALFRED is built on AI2-THOR household tasks.

### Environmental Understanding Vision-Language Model for Embodied Agent

`2026` `arXiv` `VLM` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2604.19839)

This work targets environmental understanding for vision-language embodied agents and evaluates in ALFRED-style instruction-following settings. It is included because the benchmark connection grounds the method in the AI2-THOR-family ecosystem.

### GaLa: Hypergraph-Guided Visual Language Models for Procedural Planning

`2026` `arXiv` `procedural planning` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2604.17241)

GaLa uses hypergraph-guided visual-language reasoning for procedural planning in embodied tasks. Its ALFRED evaluation makes it relevant to AI2-THOR-family instruction following and household task execution.

### Egocentric Planning for Scalable Embodied Task Achievement

`2023` `arXiv` `planning` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2306.01295)

Egocentric Planning for Scalable Embodied Task Achievement uses ALFRED as an embodied household-task benchmark for planning. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

### Embodied Concept Learner: Self-supervised Learning of Concepts and Mapping through Instruction Following

`2023` `arXiv` `planning` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2304.03767)

Embodied Concept Learner: Self-supervised Learning of Concepts and Mapping through Instruction Following uses ALFRED as an embodied household-task benchmark for planning. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

### Multimodal Contextualized Plan Prediction for Embodied Task Completion

`2023` `arXiv` `planning` `TEACh`

Links: [arXiv](https://arxiv.org/abs/2305.06485)

Multimodal Contextualized Plan Prediction for Embodied Task Completion studies planning in TEACh-style embodied task completion. TEACh extends AI2-THOR household tasks with situated dialogue, making the work relevant to conversational instruction-following agents.

### Multimodal Speech Recognition for Language-Guided Embodied Agents

`2023` `arXiv` `planning` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2302.14030)

Multimodal Speech Recognition for Language-Guided Embodied Agents uses ALFRED as an embodied household-task benchmark for planning. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

### Embodied CoT Distillation From LLM To Off-the-shelf Agents

`2024` `arXiv` `planning` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2412.11499)

Embodied CoT Distillation From LLM To Off-the-shelf Agents uses ALFRED as an embodied household-task benchmark for planning. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

### Multi-Agent Planning Using Visual Language Models

`2024` `arXiv` `planning` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2408.05478)

Multi-Agent Planning Using Visual Language Models uses ALFRED as an embodied household-task benchmark for planning. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

### Simulating User Agents for Embodied Conversational-AI

`2024` `arXiv` `planning` `TEACh`

Links: [arXiv](https://arxiv.org/abs/2410.23535)

Simulating User Agents for Embodied Conversational-AI studies planning in TEACh-style embodied task completion. TEACh extends AI2-THOR household tasks with situated dialogue, making the work relevant to conversational instruction-following agents.

### VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought

`2024` `arXiv` `memory` `TEACh`

Links: [arXiv](https://arxiv.org/abs/2406.14596)

VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought studies memory in TEACh-style embodied task completion. TEACh extends AI2-THOR household tasks with situated dialogue, making the work relevant to conversational instruction-following agents.

### Exploratory Retrieval-Augmented Planning For Continual Embodied Instruction Following

`2025` `arXiv` `memory` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2509.08222)

Exploratory Retrieval-Augmented Planning For Continual Embodied Instruction Following uses ALFRED as an embodied household-task benchmark for memory. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

### LLaPa: A Vision-Language Model Framework for Counterfactual-Aware Procedural Planning

`2025` `arXiv` `memory` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2507.08496)

LLaPa: A Vision-Language Model Framework for Counterfactual-Aware Procedural Planning uses ALFRED as an embodied household-task benchmark for memory. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

### ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning

`2025` `arXiv` `memory` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2511.02424)

ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning uses ALFRED as an embodied household-task benchmark for memory. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

### Machine Intelligence that Understands Visual and Linguistic Information and Interacts with Humans and Environments

`2026` `arXiv` `interaction` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2605.24020)

Machine Intelligence that Understands Visual and Linguistic Information and Interacts with Humans and Environments uses ALFRED as an embodied household-task benchmark for interaction. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

## Navigation

*ObjectNav, semantic navigation, and navigation-analysis work evaluated in AI2-THOR-family environments.*

### Target-driven Visual Navigation in Indoor Scenes using Deep Reinforcement Learning

`2017` `ICRA` `AI2-THOR` `deep RL`

Links: [Paper](https://arxiv.org/abs/1609.05143) · [Project](https://prior.allenai.org/projects/target-driven-visual-navigation) · [Code](https://github.com/caomw/icra2017-visual-navigation-1)

This early target-conditioned navigation work trains agents to reach visual goals from egocentric observations using deep reinforcement learning. It helped establish AI2-THOR as a practical environment for studying embodied visual navigation under realistic indoor variation.

### Visual Semantic Navigation using Scene Priors

`2018` `arXiv` `AI2-THOR` `semantic priors`

Links: [Paper](https://arxiv.org/abs/1810.06543)

Visual Semantic Navigation uses graph-based semantic priors to guide object-goal search in unseen indoor scenes. The core idea is that object co-occurrence and spatial context can help an agent search more intelligently than random exploration or purely reactive policies.

### Search for or Navigate to? Dual Adaptive Thinking for Object Navigation

`2023` `ICCV` `AI2-THOR` `RoboTHOR`

Links: [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Dang_Search_for_or_Navigate_to_Dual_Adaptive_Thinking_for_Object_ICCV_2023_paper.html)

Dual Adaptive Thinking separates object navigation into searching and goal-reaching modes, switching behavior based on whether a target has been discovered. It reports experiments on both AI2-THOR and RoboTHOR, making it a direct bridge between iTHOR-style ObjectNav and sim-to-real navigation.

### SAVN: Self-Adaptive Visual Navigation Using Meta-Learning

`2019` `CVPR Oral` `AI2-THOR` `meta-learning`

Links: [Paper](https://arxiv.org/abs/1812.00971) · [Code](https://github.com/allenai/savn)

SAVN trains navigation agents that can adapt during test-time exploration using a self-supervised interaction loss. It is an important AI2-THOR navigation baseline because it studies online adaptation rather than assuming that a fixed policy will generalize to every new scene.

### Unsupervised Reinforcement Learning of Transferable Meta-Skills for Embodied Navigation

`2019` `arXiv` `AI2-THOR` `meta-skills`

Links: [Paper](https://arxiv.org/abs/1911.07450)

This work learns transferable navigation meta-skills from unannotated AI2-THOR environments before adapting them to object-goal navigation. It is useful for the low-resource setting where only a small number of scenes have target-object reward annotations.

### Learning Object Relation Graph and Tentative Policy for Visual Navigation

`2020` `arXiv` `AI2-THOR` `object relation graph`

Links: [Paper](https://arxiv.org/abs/2007.11018) · [Code](https://github.com/xiaobaishu0097/ECCV-VN)

This method combines object relation graphs, trial-driven imitation learning, and a memory-augmented tentative policy network for target-driven visual navigation. It uses AI2-THOR to evaluate whether object co-occurrence and spatial correlations help agents escape loops and navigate more efficiently.

### Pushing it out of the Way: Interactive Visual Navigation

`2021` `arXiv` `AI2-THOR` `interactive navigation`

Links: [Paper](https://arxiv.org/abs/2104.14040)

Interactive Visual Navigation studies cases where moving through the world is not enough: agents may need to push obstacles away or move objects to target locations. The Neural Interaction Engine predicts action effects in AI2-THOR so planning can account for physical scene changes.

### Communicative Learning with Natural Gestures for Embodied Navigation Agents with Human-in-the-Scene

`2021` `arXiv` `Ges-THOR` `gesture-guided navigation`

Links: [Paper](https://arxiv.org/abs/2108.02846)

This work introduces Ges-THOR, a VR-based extension of AI2-THOR where a human in the scene guides an embodied navigation agent using natural gestures. It broadens the AI2-THOR navigation setting from language-only instructions to multimodal human communication.

### What Do Navigation Agents Learn About Their Environment?

`2022` `CVPR` `analysis` `navigation`

Links: [Paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Dwivedi_What_Do_Navigation_Agents_Learn_About_Their_Environment_CVPR_2022_paper.pdf)

This paper analyzes what information navigation agents encode about their environments, including object locations, layouts, traversability, and spatial structure. It is useful for understanding whether high task success reflects real environment understanding or exploitation of dataset shortcuts.

### Object Memory Transformer for Object Goal Navigation

`2022` `arXiv` `AI2-THOR` `object memory`

Links: [Paper](https://arxiv.org/abs/2203.14708)

Object Memory Transformer stores long-term object-scene observations and attends over them during object-goal navigation. Its AI2-THOR experiments emphasize that remembering previously observed object semantics can improve navigation efficiency in unknown environments.

### Selective Visual Representations Improve Convergence and Generalization for Embodied AI

`2023` `arXiv` `representation learning` `ProcTHOR`

Links: [Paper](https://arxiv.org/abs/2311.04193) · [Project](https://embodied-codebook.github.io/) · [Code](https://github.com/allenai/procthor-rl)

This work learns task-conditioned filters over general visual representations, reducing irrelevant visual noise for embodied policies. It evaluates across ProcTHOR, ArchitecTHOR, RoboTHOR, iTHOR, and ManipulaTHOR, showing that selective representation bottlenecks can improve convergence and generalization.

### PoliFormer: Scaling On-Policy RL with Transformers Results in Masterful Navigators

`2024` `arXiv` `ProcTHOR` `ObjectNav`

Links: [Paper](https://arxiv.org/abs/2406.20083) · [Project](https://poliformer.allen.ai/) · [Code](https://github.com/allenai/PoliFormer)

PoliFormer scales on-policy reinforcement learning with transformer policies for ObjectNav. It uses large ProcTHOR training corpora and studies how model scale, environment scale, and embodiment choices affect navigation performance.

### CogDDN: A Cognitive Demand-Driven Navigation with Decision Optimization and Dual-Process Thinking

`2025` `ACM MM` `ProcTHOR` `demand-driven navigation`

Links: [Paper](https://arxiv.org/abs/2507.11334) · [Project](https://yuehaohuang.github.io/CogDDN/)

CogDDN frames navigation around implicit human demands rather than fixed object categories. It combines object detection, semantic demand matching, heuristic decision making, analytic reflection, and a knowledge base to navigate ProcTHOR scenes from egocentric visual input.

### From Reactive to Map-Based AI: Tuned Local LLMs for Semantic Zone Inference in Object-Goal Navigation

`2026` `arXiv` `AI2-THOR` `semantic mapping`

Links: [Paper](https://arxiv.org/abs/2603.08086)

This work studies ObjectNav with local LLMs and topological-grid memory for semantic zone inference. It belongs in the AI2-THOR navigation line because evaluation is performed directly in AI2-THOR ObjectNav environments.

### Visual Reaction: Learning to Play Catch with Your Drone

`2025` `ICRA` `drone navigation` `AI2-THOR`

Links: [Paper](https://arxiv.org/abs/2403.11705) · [Project](https://visualreaction.github.io/) · [Code](https://github.com/RuohanGao/visualreaction)

Visual Reaction uses AI2-THOR-style indoor scenes to train and evaluate reactive aerial navigation for a drone catching task. It broadens the navigation coverage beyond ground robots and ObjectNav toward fast visual control and dynamic target interception.

### AION: Aerial Indoor Object-Goal Navigation Using Dual-Policy Reinforcement Learning

`2026` `IROS` `AI2-THOR` `aerial ObjectNav`

Links: [Paper](https://arxiv.org/abs/2601.15614) · [Code](https://github.com/Zichen-Yan/AION)

AION studies vision-based aerial ObjectNav with a dual-policy reinforcement-learning framework that separates exploration from goal reaching. It evaluates the method on AI2-THOR ObjectNav and also tests real-time drone execution in IsaacSim.

### Collision-Aware Object-Goal Visual Navigation via Two-Stage Deep Reinforcement Learning

`2025` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2502.13498)

This work evaluates in AI2-THOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### The One RING: a Robotic Indoor Navigation Generalist

`2024` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2412.14401)

This work evaluates in AI2-THOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Efficient Strategy Learning by Decoupling Searching and Pathfinding for Object Navigation

`2024` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2406.14103)

This work evaluates in AI2-THOR / RoboTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### TDANet: Target-Directed Attention Network For Object-Goal Visual Navigation With Zero-Shot Ability

`2024` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2404.08353)

This work evaluates in AI2-THOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Advancing Object Goal Navigation Through LLM-enhanced Object Affinities Transfer

`2024` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2403.09971)

This work evaluates in AI2-THOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Aligning Knowledge Graph with Visual Perception for Object-goal Navigation

`2024` `arXiv` `ObjectNav` `navigation`

Links: [Code](https://github.com/nuoxu/AKGVP) · [arXiv](https://arxiv.org/abs/2402.18892)

This work evaluates in AI2-THOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Building Category Graphs Representation with Spatial and Temporal Attention for Visual Navigation

`2023` `arXiv` `navigation` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2312.03327)

This work evaluates in AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Zero-Shot Object Goal Visual Navigation With Class-Independent Relationship Network

`2023` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2310.09883)

This work evaluates in AI2-THOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Implicit Obstacle Map-driven Indoor Navigation Model for Robust Obstacle Avoidance

`2023` `arXiv` `navigation` `memory`

Links: [arXiv](https://arxiv.org/abs/2308.12845)

This work evaluates in AI2-THOR / RoboTHOR for embodied memory and spatial reasoning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Moving Forward by Moving Backward: Embedding Action Impact over Action Semantics

`2023` `arXiv` `navigation` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2304.12289)

This work uses AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Zero-Shot Object Searching Using Large-scale Object Relationship Prior

`2023` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2303.06228)

This work uses AI2-THOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Multiple Thinking Achieving Meta-Ability Decoupling for Object Navigation

`2023` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2302.01520)

This work evaluates in AI2-THOR / RoboTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Generalized Object Search

`2023` `arXiv` `planning` `benchmark`

Links: [arXiv](https://arxiv.org/abs/2301.10121)

This work evaluates in AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Role of reward shaping in object-goal navigation

`2022` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2207.08021)

This work uses AI2-THOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Zero-shot object goal visual navigation

`2022` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2206.07423)

This work evaluates in AI2-THOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Unbiased Directed Object Attention Graph for Object Navigation

`2022` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2204.04421)

This work uses AI2-THOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Agent-Centric Relation Graph for Object Visual Navigation

`2021` `arXiv` `navigation` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2111.14422)

This work uses AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Towards Optimal Correlational Object Search

`2021` `arXiv` `planning` `benchmark`

Links: [arXiv](https://arxiv.org/abs/2110.09991)

This work evaluates in AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Hierarchical Object-to-Zone Graph for Object Navigation

`2021` `arXiv` `ObjectNav` `navigation`

Links: [Code](https://github.com/sx-zhang/HOZ) · [arXiv](https://arxiv.org/abs/2109.02066)

This work evaluates in AI2-THOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### VTNet: Visual Transformer Network for Object Goal Navigation

`2021` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2105.09447)

This work uses AI2-THOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Dynamic Value Estimation for Single-Task Multi-Scene Reinforcement Learning

`2020` `arXiv` `navigation` `RL`

Links: [arXiv](https://arxiv.org/abs/2005.12254)

This work evaluates in AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Improving Target-driven Visual Navigation with Attention on 3D Spatial Relationships

`2020` `arXiv` `navigation` `RL`

Links: [arXiv](https://arxiv.org/abs/2005.02153)

This work uses AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Reinforcement Learning-based Visual Navigation with Information-Theoretic Regularization

`2019` `arXiv` `navigation` `benchmark`

Links: [arXiv](https://arxiv.org/abs/1912.04078)

This work evaluates in AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Vision-based Navigation Using Deep Reinforcement Learning

`2019` `arXiv` `navigation` `segmentation`

Links: [arXiv](https://arxiv.org/abs/1908.03627)

This work evaluates in AI2-THOR for embodied perception. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Active Object Perceiver: Recognition-guided Policy Learning for Object Searching on Mobile Robots

`2018` `arXiv` `navigation` `RL`

Links: [arXiv](https://arxiv.org/abs/1807.11174)

This work uses AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation

`2026` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2606.25497)

This work evaluates in RoboTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Effective Task Planning with Missing Objects using Learning-Informed Object Search

`2026` `arXiv` `planning` `ProcTHOR`

Links: [arXiv](https://arxiv.org/abs/2602.11468)

This work uses ProcTHOR for embodied task planning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### VISTAv2: World Imagination for Indoor Vision-and-Language Navigation

`2025` `arXiv` `navigation` `planning`

Links: [arXiv](https://arxiv.org/abs/2512.00041)

This work uses RoboTHOR for vision-and-language navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### STRIVE: Structured Representation Integrating VLM Reasoning for Efficient Object Navigation

`2025` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2505.06729)

This work evaluates in RoboTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### VISTA: Generative Visual Imagination for Vision-and-Language Navigation

`2025` `arXiv` `navigation` `benchmark`

Links: [arXiv](https://arxiv.org/abs/2505.07868)

This work evaluates in RoboTHOR for vision-and-language navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### CogNav: Cognitive Process Modeling for Object Goal Navigation with LLMs

`2024` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2412.10439)

This work evaluates in RoboTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Exploring the Reliability of Foundation Model-Based Frontier Selection in Zero-Shot Object Goal Navigation

`2024` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2410.21037)

This work uses RoboTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Zero-shot Object Navigation with Vision-Language Models Reasoning

`2024` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2410.18570)

This work evaluates in RoboTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### SG-Nav: Online 3D Scene Graph Prompting for LLM-based Zero-shot Object Navigation

`2024` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2410.08189)

This work evaluates in RoboTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Leveraging Unknown Objects to Construct Labeled-Unlabeled Meta-Relationships for Zero-Shot Object Navigation

`2024` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2405.15222)

This work evaluates in RoboTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Promptable Behaviors: Personalizing Multi-Objective Rewards from Human Preferences

`2023` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2312.09337)

This work uses RoboTHOR / ProcTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Find What You Want: Learning Demand-conditioned Object Attribute Space for Demand-driven Navigation

`2023` `arXiv` `ObjectNav` `navigation`

Links: [Code](https://github.com/whcpumpkin/Demand-driven-navigation) · [arXiv](https://arxiv.org/abs/2309.08138)

This work uses ProcTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### SayNav: Grounding Large Language Models for Dynamic Planning to Navigation in New Environments

`2023` `arXiv` `ObjectNav` `navigation`

Links: [Code](https://github.com/arajv/SayNav) · [arXiv](https://arxiv.org/abs/2309.04077)

This work evaluates in ProcTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### When Learning Is Out of Reach, Reset: Generalization in Autonomous Visuomotor Reinforcement Learning

`2023` `arXiv` `ObjectNav` `benchmark`

Links: [Code](https://github.com/zcczhang/rmrl) · [arXiv](https://arxiv.org/abs/2303.17600)

This work evaluates in RoboTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Can an Embodied Agent Find Your "Cat-shaped Mug"? LLM-Guided Exploration for Zero-Shot Object Navigation

`2023` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2303.03480)

This work evaluates in RoboTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### ESC: Exploration with Soft Commonsense Constraints for Zero-shot Object Navigation

`2023` `arXiv` `ObjectNav` `navigation`

Links: [arXiv](https://arxiv.org/abs/2301.13166)

This work evaluates in RoboTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Simple but Effective: CLIP Embeddings for Embodied AI

`2021` `arXiv` `ObjectNav` `navigation`

Links: [Code](https://github.com/allenai/embodied-clip) · [arXiv](https://arxiv.org/abs/2111.09888)

This work evaluates in iTHOR / RoboTHOR for object-goal navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents

`2026` `arXiv` `benchmarks`

Links: [arXiv](https://arxiv.org/abs/2605.10332)

This work evaluates in EmbodiedBench for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### SeeNav-Agent: Enhancing Vision-Language Navigation with Visual Prompt and Step-Level Policy Optimization

`2025` `arXiv` `navigation` `planning`

Links: [arXiv](https://arxiv.org/abs/2512.02631)

This work evaluates in EmbodiedBench for vision-and-language navigation. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### LGX: Language-Guided Exploration

`2023` `zero-shot ObjectNav` `RoboTHOR`

Links: [Code](https://github.com/vdorbala/LGX)

LGX is code for language-guided exploration in zero-shot object navigation. It complements the L-ZSON and RoboTHOR navigation entries with a concrete implementation.

### RDMAE-Nav

`navigation` `robustness` `RoboTHOR`

Links: [Code](https://github.com/danelpeng/RDMAE_Nav)

RDMAE-Nav is a robust embodied-navigation project focused on visual corruptions and robustness. It is included as a RoboTHOR-related implementation resource for robust navigation research.

### STRIVE project page

`2025` `VLM` `ObjectNav`

Links: [Code](https://github.com/igzat1no/STRIVE)

STRIVE provides project resources for Structured Representation Integrating VLM Reasoning for Efficient Object Navigation. It complements the arXiv entry with implementation or project-page materials.

### NOLO: Navigate Only Look Once

`2025` `IROS` `ObjectNav`

Links: [Code](https://github.com/zhoubohan0/NOLO)

NOLO is the official implementation of Navigate Only Look Once, an object-navigation project. It is relevant as a recent embodied-navigation resource connected to RoboTHOR-style evaluation.

### VUSFA:Variational Universal Successor Features Approximator to Improve Transfer DRL for Target Driven Visual Navigation

`2019` `arXiv` `navigation` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/1908.06376)

VUSFA:Variational Universal Successor Features Approximator to Improve Transfer DRL for Target Driven Visual Navigation reports experiments connected to AI2-THOR for navigation. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Optimistic Agent: Accurate Graph-Based Value Estimation for More Successful Visual Navigation

`2020` `arXiv` `navigation` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2004.03222)

Optimistic Agent: Accurate Graph-Based Value Estimation for More Successful Visual Navigation reports experiments connected to AI2-THOR for navigation. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Learning Embeddings that Capture Spatial Semantics for Indoor Navigation

`2021` `arXiv` `navigation` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2108.00159)

Learning Embeddings that Capture Spatial Semantics for Indoor Navigation reports experiments connected to AI2-THOR for navigation. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Learning for Visual Navigation by Imagining the Success

`2021` `arXiv` `navigation` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2103.00446)

Learning for Visual Navigation by Imagining the Success reports experiments connected to AI2-THOR for navigation. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Learning to Act with Affordance-Aware Multimodal Neural SLAM

`2022` `arXiv` `navigation` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2201.09862)

Learning to Act with Affordance-Aware Multimodal Neural SLAM uses ALFRED as an embodied household-task benchmark for navigation. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

### LEBP -- Language Expectation & Binding Policy: A Two-Stream Framework for Embodied Vision-and-Language Interaction Task Learning Agents

`2022` `arXiv` `navigation` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2203.04637)

LEBP -- Language Expectation & Binding Policy: A Two-Stream Framework for Embodied Vision-and-Language Interaction Task Learning Agents uses ALFRED as an embodied household-task benchmark for navigation. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

### On the Limits of Evaluating Embodied Agent Model Generalization Using Validation Sets

`2022` `arXiv` `navigation` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2205.09249)

On the Limits of Evaluating Embodied Agent Model Generalization Using Validation Sets uses ALFRED as an embodied household-task benchmark for navigation. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

### CARTIER: Cartographic lAnguage Reasoning Targeted at Instruction Execution for Robots

`2023` `arXiv` `navigation` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2307.11865)

CARTIER: Cartographic lAnguage Reasoning Targeted at Instruction Execution for Robots reports experiments connected to AI2-THOR for navigation. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### ELBA: Learning by Asking for Embodied Visual Navigation and Task Completion

`2023` `arXiv` `navigation` `TEACh`

Links: [arXiv](https://arxiv.org/abs/2302.04865)

ELBA: Learning by Asking for Embodied Visual Navigation and Task Completion studies navigation in TEACh-style embodied task completion. TEACh extends AI2-THOR household tasks with situated dialogue, making the work relevant to conversational instruction-following agents.

### Privacy Risks in Reinforcement Learning for Household Robots

`2023` `arXiv` `navigation` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2306.09273)

Privacy Risks in Reinforcement Learning for Household Robots reports experiments connected to AI2-THOR for navigation. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### RoboGPT: an intelligent agent of making embodied long-term decisions for daily instruction tasks

`2023` `arXiv` `navigation` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2311.15649)

RoboGPT: an intelligent agent of making embodied long-term decisions for daily instruction tasks uses ALFRED as an embodied household-task benchmark for navigation. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

### Commonsense Scene Graph-based Target Localization for Object Search

`2024` `arXiv` `navigation` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2404.00343)

Commonsense Scene Graph-based Target Localization for Object Search reports experiments connected to AI2-THOR for navigation. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Efficient Policy Adaptation with Contrastive Prompt Ensemble for Embodied Agents

`2024` `arXiv` `navigation` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2412.11484)

Efficient Policy Adaptation with Contrastive Prompt Ensemble for Embodied Agents reports experiments connected to AI2-THOR for navigation. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Grounding Video Models to Actions through Goal Conditioned Exploration

`2024` `arXiv` `navigation` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2411.07223)

Grounding Video Models to Actions through Goal Conditioned Exploration reports experiments connected to AI2-THOR for navigation. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Plan Verification for LLM-Based Embodied Task Completion Agents

`2025` `arXiv` `navigation` `TEACh`

Links: [arXiv](https://arxiv.org/abs/2509.02761)

Plan Verification for LLM-Based Embodied Task Completion Agents studies navigation in TEACh-style embodied task completion. TEACh extends AI2-THOR household tasks with situated dialogue, making the work relevant to conversational instruction-following agents.

### TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning

`2026` `arXiv` `navigation` `ALFWorld`

Links: [arXiv](https://arxiv.org/abs/2606.32017)

TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning evaluates agent methods on ALFWorld, the text-game environment aligned with ALFRED and THOR household tasks. It is included as an ALFRED-derived planning and evaluation entry rather than as direct AI2-THOR simulator execution.

## Planning, Memory, and Multi-Agent Systems

*Planning, memory, dialogue, assistance, and multi-agent systems grounded in AI2-THOR-derived tasks.*

### Visual Semantic Planning using Deep Successor Representations

`2017` `ICCV` `THOR` `visual semantic planning`

Links: [Paper](https://arxiv.org/abs/1705.08080) · [Project](https://prior.allenai.org/projects/visual-semantic-planning)

Visual Semantic Planning learns to predict action sequences that change object states in THOR. It is an early precursor to household interaction benchmarks because it goes beyond navigation into planning around object affordances and state-changing actions.

### PIGLeT: Language Grounding Through Neuro-Symbolic Interaction in a 3D World

`2021` `ACL` `language grounding` `AI2-THOR`

Links: [Paper](https://arxiv.org/abs/2106.00188) · [Project](https://piglet.cs.umass.edu/) · [Code](https://github.com/rowanz/piglet)

PIGLeT learns grounded language and action consequences by interacting with objects in AI2-THOR. It combines symbolic object-state reasoning with neural language models, making it an early bridge between embodied interaction and language-grounded commonsense prediction.

### MaSS: A Simple Approach for Visual Rearrangement

`2023` `ICLR` `rearrangement` `semantic mapping`

Links: [Paper](https://arxiv.org/abs/2206.13396) · [Code](https://github.com/brandontrabucco/mass)

MaSS tackles the AI2-THOR Rearrangement Challenge with a simple modular pipeline based on semantic segmentation, voxel mapping, and semantic search. It is a strong example of how explicit spatial structure can compete in long-horizon rearrangement without relying on opaque end-to-end policies.

### TIDEE: Tidying Up Novel Rooms using Visuo-Semantic Commonsense Priors

`2022` `ECCV` `tidying` `rearrangement`

Links: [Paper](https://arxiv.org/abs/2207.10761) · [Project](https://tidee-agent.github.io/) · [Code](https://github.com/Gabesarch/TIDEE)

TIDEE studies open-ended room tidying in AI2-THOR. Instead of copying a reference goal state, it uses visuo-semantic commonsense priors, graph memory, and visual search to identify out-of-place objects and move them to plausible receptacles or surfaces.

### Towards Disturbance-Free Visual Mobile Manipulation

`2022` `ICRA` `ManipulaTHOR` `mobile manipulation`

Links: [Paper](https://arxiv.org/abs/2112.12612)

This work studies mobile manipulation policies that complete ManipulaTHOR tasks while avoiding unnecessary collisions and environmental disturbance. It adds a safety and physical-side-effect lens to ArmPointNav-style visual mobile manipulation.

### JARVIS: A Neuro-Symbolic Commonsense Reasoning Framework for Conversational Embodied Agents

`2022` `arXiv` `TEACh` `neuro-symbolic planning`

Links: [Paper](https://arxiv.org/abs/2208.13266)

JARVIS combines language understanding, semantic mapping, commonsense reasoning, and symbolic action generation for TEACh-style conversational embodied tasks. It focuses on using structured reasoning to bridge dialogue intent and executable household actions.

### HELPER: Open-Ended Instructable Embodied Agents with Memory-Augmented Large Language Models

`2023` `Findings of EMNLP` `TEACh` `memory-augmented LLM`

Links: [Paper](https://arxiv.org/abs/2310.15127) · [Project](https://helper-agent-llm.github.io/) · [Code](https://github.com/Gabesarch/HELPER)

HELPER uses retrieval-augmented memory over language-program pairs to personalize embodied task execution from open-ended human dialogue. It targets TEACh execution and shows how deployment-time memories can adapt an LLM planner to user-specific routines.

### Prompter: Utilizing LLM Prompting for Data-Efficient Embodied Instruction Following

`2022` `arXiv` `ALFRED` `LLM planning`

Links: [Paper](https://arxiv.org/abs/2211.03267)

Prompter uses large-language-model prompting to inject object-landmark relationships and task constraints into ALFRED agents. It is representative of early attempts to use LLM world knowledge for data-efficient embodied instruction following before full VLM-agent pipelines became common.

### DialMAT: Dialogue-Enabled Transformer with Moment-Based Adversarial Training

`2023` `CVPR Embodied AI Workshop` `DialFRED` `dialogue`

Links: [Paper](https://arxiv.org/abs/2311.06855)

DialMAT trains a dialogue-enabled transformer for DialFRED using moment-based adversarial training. It is a direct DialFRED follow-up and is useful for tracking methods that turn clarification dialogue into better ALFRED-derived task execution.

### CAPEAM: Context-Aware Planning and Environment-Aware Memory

`2023` `arXiv` `ALFRED` `memory` `planning`

Links: [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Kim_Context-Aware_Planning_and_Environment-Aware_Memory_for_Instruction_Following_Embodied_Agents_ICCV_2023_paper.html) · [Project](https://bhkim94.github.io/projects/CAPEAM/) · [Code](https://github.com/snumprlab/capeam)

CAPEAM improves ALFRED execution by tracking action consequences, object states, and environment changes across time. Its context-aware planning and memory design target common long-horizon failures such as stale assumptions after object interaction.

### Socratic Planner: Inquiry-Based Zero-Shot Planning for Embodied Instruction Following

`2024` `arXiv` `ALFRED` `zero-shot planning`

Links: [Paper](https://arxiv.org/abs/2404.15190)

Socratic Planner decomposes embodied instructions through self-questioning and uses visual feedback to revise plans during execution. It fits the ALFRED line of work that explores LLM planning without heavy benchmark-specific policy training.

### Smart Help: Strategic Opponent Modeling for Proactive and Adaptive Robot Assistance in Households

`2024` `arXiv` `assistance` `multi-agent`

Links: [Paper](https://arxiv.org/abs/2404.09001)

Smart Help defines an assistive-agent challenge in AI2-THOR where a robot must proactively adapt to humans with different abilities and dynamic goals. It emphasizes modeling the other agent's capability and intent rather than executing a fixed helper policy.

### LLaMAR: Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments

`2024` `NeurIPS` `multi-agent` `MAP-THOR`

Links: [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/7d6e85e88495104442af94c98e899659-Abstract-Conference.html) · [Project](https://nsidn98.github.io/LLaMAR/) · [Code](https://github.com/nsidn98/LLaMAR)

LLaMAR uses a plan-act-correct-verify loop for language-model-based multi-agent planning under partial observability. It introduces MAP-THOR, an AI2-THOR-based multi-agent household test suite for long-horizon collaborative planning.

### KARMA: Augmenting Embodied AI Agents with Long-and-short Term Memory Systems

`2024` `arXiv` `memory` `scene graphs`

Links: [Paper](https://arxiv.org/abs/2409.14908) · [Code](https://github.com/WZX0Swarm0Robotics/KARMA)

KARMA adds long-term and short-term memory modules to embodied agents. Long-term memory stores 3D scene-graph experience, while short-term memory tracks recent object state and position changes, helping LLM-based planners avoid repeated mistakes in household tasks.

### HELPER-X: A Unified Instructable Embodied Agent

`2024` `arXiv` `memory-augmented LLM` `multi-domain`

Links: [Paper](https://arxiv.org/abs/2404.19065) · [Project](https://helper-agent-llm.github.io/)

HELPER-X extends memory-augmented LLM planning across ALFRED, TEACh, DialFRED, and room reorganization tasks. It focuses on broad instructability through retrieved examples and shared memory, without requiring heavy in-domain training for every benchmark.

### Scene Graph-Guided Proactive Replanning for Failure-Resilient Embodied Agent

`2025` `arXiv` `replanning` `scene graphs`

Links: [Paper](https://arxiv.org/abs/2508.11286)

This method compares current scene graphs against reference graphs from successful demonstrations and triggers replanning before execution failures occur. It targets common household-task failures such as stale assumptions about object state or spatial relations.

### AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition

`2026` `arXiv` `ALFRED` `RoboTHOR`

Links: [Paper](https://arxiv.org/abs/2606.14674) · [Project](https://agentspec-embodied.github.io/)

AgentSpec studies how reasoning, memory, reflection, and learning modules compose inside embodied agent scaffolds. It is in scope because its controlled evaluations instantiate agents in both ALFRED and RoboTHOR.

### Emergence: Overcoming Privileged Information Bias in Asymmetric Embodied Agents via Active Querying

`2025` `arXiv` `multi-agent` `active querying`

Links: [Paper](https://arxiv.org/abs/2512.15776)

Emergence introduces an asymmetric assistive reasoning setup in AI2-THOR where a knowledgeable leader must guide a sensor-limited follower. It studies privileged-information bias and compares push-style instruction with pull-style active querying for collaborative embodied tasks.

### Scale-Plan: Scalable Language-Enabled Task Planning for Heterogeneous Multi-Robot Teams

`2026` `arXiv` `multi-robot planning` `MAT2-THOR`

Links: [Paper](https://arxiv.org/abs/2603.08814)

Scale-Plan uses LLM-guided graph search to filter task-relevant actions and objects before multi-robot planning. It introduces MAT2-THOR, a cleaned AI2-THOR-based benchmark for evaluating heterogeneous multi-robot planning systems.

### Flexible Agent Alignment with Goal Inference from Open-Ended Dialog

`2025` `arXiv` `LLM` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2508.15119)

This work uses AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Embodied Referring Expression for Manipulation Question Answering in Interactive Environment

`2022` `arXiv` `benchmark` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2210.02709)

This work evaluates in AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### eMEM: A Hybrid Spatio-Temporal Memory System For Embodied Agents

`2026` `arXiv` `memory` `benchmark`

Links: [arXiv](https://arxiv.org/abs/2606.03374)

This work evaluates in ProcTHOR for embodied memory and spatial reasoning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### StateLinFormer: Stateful Training Enhancing Long-term Memory in Navigation

`2026` `arXiv` `navigation` `memory`

Links: [arXiv](https://arxiv.org/abs/2603.23571)

This work uses ProcTHOR for embodied memory and spatial reasoning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### ESCAPE: Episodic Spatial Memory and Adaptive Execution Policy for Long-Horizon Mobile Manipulation

`2026` `arXiv` `memory` `mobile manipulation`

Links: [arXiv](https://arxiv.org/abs/2604.13633)

ESCAPE studies episodic spatial memory and adaptive execution for long-horizon mobile manipulation. It is included because the work reports ALFRED-family embodied task evaluation, connecting it to AI2-THOR household workflows.

### KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning

`2026` `arXiv` `memory` `planning`

Links: [arXiv](https://arxiv.org/abs/2602.23592)

KEEP proposes KV-cache-centric memory management for long-horizon embodied planning. It is relevant here because the evaluation includes ALFRED-style embodied planning, tying the method to AI2-THOR-family tasks.

### Cordial Sync

`2024` `multi-agent` `AI2-THOR` `code`

Links: [Code](https://github.com/allenai/cordial-sync)

cordial-sync is AllenAI code for reproducing A Cordial Sync, a multi-agent embodied task project. It belongs in the AI2-THOR ecosystem because the repository supports experiments on multi-agent embodied tasks.

### Ask4Help

`help-seeking` `navigation` `RoboTHOR`

Links: [Code](https://github.com/allenai/ask4help)

Ask4Help releases code for studying when embodied navigation agents should ask for help. It is part of the RoboTHOR research ecosystem around navigation, uncertainty, and assistance.

### OGAMUS: Online Grounding of Action Models in Unknown Situations

`planning` `grounding` `AI2-THOR`

Links: [Code](https://github.com/LamannaLeonardo/OGAMUS)

OGAMUS provides code for online grounding of action models in unknown situations. It is relevant as a planning and grounding project that appears in AI2-THOR-family embodied-agent search results.

### TaPA

`2023` `LLM` `task planning`

Links: [Code](https://github.com/Gary3410/TaPA)

TaPA is code for Embodied Task Planning with Large Language Models. The repository is relevant to AI2-THOR-family planning workflows because it targets embodied task planning and appears in AI2-THOR search results with released code.

### SMART-LLM

`2023` `LLM` `multi-agent`

Links: [Code](https://github.com/SMARTlab-Purdue/SMART-LLM)

SMART-LLM is a codebase for Smart Multi-Agent Robot Task Planning using Large Language Models. It is useful for readers tracking LLM-based planning systems that overlap with AI2-THOR-style household task environments.

### Embodied-Reasoner

`2024` `reasoning` `interactive tasks`

Links: [Code](https://github.com/zwq2018/embodied_reasoner)

Embodied-Reasoner releases code for synergizing visual search, reasoning, and action in embodied interactive tasks. It is included as a project resource for AI2-THOR-family embodied reasoning workflows.

### Automata-Guided Hierarchical Reinforcement Learning for Skill Composition

`2017` `arXiv` `planning` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/1711.00129)

Automata-Guided Hierarchical Reinforcement Learning for Skill Composition reports experiments connected to AI2-THOR for planning. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### RoboCSE: Robot Common Sense Embedding

`2019` `arXiv` `memory` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/1903.00412)

RoboCSE: Robot Common Sense Embedding reports experiments connected to AI2-THOR for memory. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Reinforcement Learning for Sparse-Reward Object-Interaction Tasks in a First-person Simulated 3D Environment

`2020` `arXiv` `interaction` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2010.15195)

Reinforcement Learning for Sparse-Reward Object-Interaction Tasks in a First-person Simulated 3D Environment reports experiments connected to AI2-THOR for interaction. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Shaping embodied agent behavior with activity-context priors from egocentric video

`2021` `arXiv` `planning` `iTHOR`

Links: [arXiv](https://arxiv.org/abs/2110.07692)

Shaping embodied agent behavior with activity-context priors from egocentric video reports experiments connected to iTHOR for planning. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### DoRO: Disambiguation of referred object for embodied agents

`2022` `arXiv` `embodied agents` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2207.14205)

DoRO: Disambiguation of referred object for embodied agents reports experiments connected to AI2-THOR for embodied agents. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Matching options to tasks using Option-Indexed Hierarchical Reinforcement Learning

`2022` `arXiv` `memory` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2206.05750)

Matching options to tasks using Option-Indexed Hierarchical Reinforcement Learning reports experiments connected to AI2-THOR for memory. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### SGL: Symbolic Goal Learning in a Hybrid, Modular Framework for Human Instruction Following

`2022` `arXiv` `planning` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2202.12912)

SGL: Symbolic Goal Learning in a Hybrid, Modular Framework for Human Instruction Following reports experiments connected to AI2-THOR for planning. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### EmbodiedRAG: Dynamic 3D Scene Graph Retrieval for Efficient and Scalable Robot Task Planning

`2024` `arXiv` `memory` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2410.23968)

EmbodiedRAG: Dynamic 3D Scene Graph Retrieval for Efficient and Scalable Robot Task Planning reports experiments connected to AI2-THOR for memory. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Goal Inference from Open-Ended Dialog

`2024` `arXiv` `interaction` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2410.13957)

Goal Inference from Open-Ended Dialog reports experiments connected to AI2-THOR for interaction. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Recover: A Neuro-Symbolic Framework for Failure Detection and Recovery

`2024` `arXiv` `planning` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2404.00756)

Recover: A Neuro-Symbolic Framework for Failure Detection and Recovery reports experiments connected to AI2-THOR for planning. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### VideoAgent: Self-Improving Video Generation

`2024` `arXiv` `planning` `iTHOR`

Links: [arXiv](https://arxiv.org/abs/2410.10076)

VideoAgent: Self-Improving Video Generation reports experiments connected to iTHOR for planning. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Spatial Policy: Guiding Visuomotor Robotic Manipulation with Spatial-Aware Modeling and Reasoning

`2025` `arXiv` `planning` `iTHOR`

Links: [arXiv](https://arxiv.org/abs/2508.15874)

Spatial Policy: Guiding Visuomotor Robotic Manipulation with Spatial-Aware Modeling and Reasoning reports experiments connected to iTHOR for planning. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### ATOD: Annealed Turn-aware On-policy Distillation for Multi-turn Autonomous Agents

`2026` `arXiv` `rl` `ALFWorld`

Links: [arXiv](https://arxiv.org/abs/2606.27814)

ATOD: Annealed Turn-aware On-policy Distillation for Multi-turn Autonomous Agents evaluates agent methods on ALFWorld, the text-game environment aligned with ALFRED and THOR household tasks. It is included as an ALFRED-derived planning and evaluation entry rather than as direct AI2-THOR simulator execution.

### BiPACE: Bisimulation-Guided Policy Optimization with Action Counterfactual Estimation for LLM Agents

`2026` `arXiv` `planning` `ALFWorld`

Links: [arXiv](https://arxiv.org/abs/2606.25556)

BiPACE: Bisimulation-Guided Policy Optimization with Action Counterfactual Estimation for LLM Agents evaluates agent methods on ALFWorld, the text-game environment aligned with ALFRED and THOR household tasks. It is included as an ALFRED-derived planning and evaluation entry rather than as direct AI2-THOR simulator execution.

### DuoMem: Towards Capable On-Device Memory Agents via Dual-Space Distillation

`2026` `arXiv` `memory` `ALFWorld`

Links: [arXiv](https://arxiv.org/abs/2606.29961)

DuoMem: Towards Capable On-Device Memory Agents via Dual-Space Distillation evaluates agent methods on ALFWorld, the text-game environment aligned with ALFRED and THOR household tasks. It is included as an ALFRED-derived planning and evaluation entry rather than as direct AI2-THOR simulator execution.

### Group-Graph Policy Optimization for Long-Horizon Agentic Reinforcement Learning

`2026` `arXiv` `planning` `ALFWorld`

Links: [arXiv](https://arxiv.org/abs/2606.22995)

Group-Graph Policy Optimization for Long-Horizon Agentic Reinforcement Learning evaluates agent methods on ALFWorld, the text-game environment aligned with ALFRED and THOR household tasks. It is included as an ALFRED-derived planning and evaluation entry rather than as direct AI2-THOR simulator execution.

### OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning

`2026` `arXiv` `memory` `ALFWorld`

Links: [arXiv](https://arxiv.org/abs/2606.26790)

OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning evaluates agent methods on ALFWorld, the text-game environment aligned with ALFRED and THOR household tasks. It is included as an ALFRED-derived planning and evaluation entry rather than as direct AI2-THOR simulator execution.

### Selective Memory Retention for Long-Horizon LLM Agents

`2026` `arXiv` `memory` `ALFWorld`

Links: [arXiv](https://arxiv.org/abs/2606.29178)

Selective Memory Retention for Long-Horizon LLM Agents evaluates agent methods on ALFWorld, the text-game environment aligned with ALFRED and THOR household tasks. It is included as an ALFRED-derived planning and evaluation entry rather than as direct AI2-THOR simulator execution.

### Self-Evolving World Models for LLM Agent Planning

`2026` `arXiv` `memory` `ALFWorld`

Links: [arXiv](https://arxiv.org/abs/2606.30639)

Self-Evolving World Models for LLM Agent Planning evaluates agent methods on ALFWorld, the text-game environment aligned with ALFRED and THOR household tasks. It is included as an ALFRED-derived planning and evaluation entry rather than as direct AI2-THOR simulator execution.

### SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills

`2026` `arXiv` `planning` `ALFWorld`

Links: [arXiv](https://arxiv.org/abs/2606.26669)

SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills evaluates agent methods on ALFWorld, the text-game environment aligned with ALFRED and THOR household tasks. It is included as an ALFRED-derived planning and evaluation entry rather than as direct AI2-THOR simulator execution.

### The Interplay of Harness Design and Post-Training in LLM Agents

`2026` `arXiv` `planning` `ALFWorld`

Links: [arXiv](https://arxiv.org/abs/2606.25447)

The Interplay of Harness Design and Post-Training in LLM Agents evaluates agent methods on ALFWorld, the text-game environment aligned with ALFRED and THOR household tasks. It is included as an ALFRED-derived planning and evaluation entry rather than as direct AI2-THOR simulator execution.

### UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation

`2026` `arXiv` `memory` `ALFWorld`

Links: [arXiv](https://arxiv.org/abs/2606.29502)

UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation evaluates agent methods on ALFWorld, the text-game environment aligned with ALFRED and THOR household tasks. It is included as an ALFRED-derived planning and evaluation entry rather than as direct AI2-THOR simulator execution.

## RL-Trained VLM Agents

*VLM-agent training and reinforcement-learning work whose evaluation includes AI2-THOR-family benchmarks.*

### ERA: Transforming VLMs into Embodied Agents via Embodied Prior Learning and Online Reinforcement Learning

`2025` `arXiv` `online RL` `EmbodiedBench`

Links: [Paper](https://arxiv.org/abs/2510.12693) · [Code](https://github.com/Embodied-Reasoning-Agent/Embodied-Reasoning-Agent)

ERA turns smaller VLMs into embodied agents through embodied prior learning followed by online reinforcement learning. Its self-summarization, dense reward shaping, and turn-level policy optimization directly target long-horizon sparse-reward failures in EB-ALFRED and EB-Manipulation.

### Reinforced Reasoning for Embodied Planning

`2025` `arXiv` `GRPO` `embodied planning`

Links: [Paper](https://arxiv.org/abs/2505.22050)

This work brings R1-style reinforcement fine-tuning into embodied planning. It first distills structured decision-making data, then applies GRPO-style optimization with rule-based rewards for multi-step action quality, highlighting the value of SFT-to-RL pipelines for embodied agents.

### RoboGPT-R1: Enhancing Robot Task Planning with Reinforcement Learning

`2026` `AAMAS` `RL` `EmbodiedBench`

Links: [Paper](https://arxiv.org/abs/2510.14828)

RoboGPT-R1 uses expert-sequence SFT followed by reinforcement learning to improve robot task planning with Qwen2.5-VL-3B. Its reported gains on EmbodiedBench-style evaluation make it a useful comparison point for GRPO/RL-based embodied VLM training.

### ESearch-R1: Learning Cost-Aware MLLM Agents for Interactive Embodied Search via Reinforcement Learning

`2025` `arXiv` `AI2-THOR` `cost-aware GRPO`

Links: [Paper](https://arxiv.org/abs/2512.18571)

ESearch-R1 trains agents to balance asking questions, retrieving memory, and physically navigating in AI2-THOR. Its cost-aware GRPO objective rewards trajectories that solve ambiguous search tasks while reducing expensive exploration and human-attention costs.

### Think Twice, Act Once: Verifier-Guided Action Selection for Embodied Agents

`2026` `CVPR (Findings)` `ALFRED` `verifier`

Links: [Paper](https://arxiv.org/abs/2605.12620)

VegAS samples an ensemble of candidate actions at test time and uses a generative verifier, trained on synthesized failure cases, to select the most reliable one. It is in scope because its embodied evaluation spans ALFRED (AI2-THOR) alongside Habitat, reporting sizable gains on long-horizon tasks.

### RenderMem: Rendering as Spatial Memory Retrieval

`2026` `arXiv` `memory` `VLM`

Links: [arXiv](https://arxiv.org/abs/2603.14669)

This work uses AI2-THOR for embodied memory and spatial reasoning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Toward Agentic AI: Task-Oriented Communication for Hierarchical Planning of Long-Horizon Tasks

`2026` `arXiv` `planning` `benchmark`

Links: [arXiv](https://arxiv.org/abs/2601.13685)

This work evaluates in AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### SplatR : Experience Goal Visual Rearrangement with 3D Gaussian Splatting and Dense Feature Matching

`2024` `arXiv` `memory` `rearrangement`

Links: [arXiv](https://arxiv.org/abs/2411.14322)

This work evaluates in AI2-THOR for visual rearrangement. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### SELU: Self-Learning Embodied MLLMs in Unknown Environments

`2024` `arXiv` `VLM` `LLM`

Links: [arXiv](https://arxiv.org/abs/2410.03303)

This work uses AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Automating Transfer of Robot Task Plans using Functorial Data Migrations

`2024` `arXiv` `planning` `benchmark`

Links: [arXiv](https://arxiv.org/abs/2406.15961)

This work evaluates in AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### ASC me to Do Anything: Multi-task Training for Embodied AI

`2022` `arXiv` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2202.06987)

This work evaluates in AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### GridToPix: Training Embodied Agents with Minimal Supervision

`2021` `arXiv` `navigation` `RL`

Links: [arXiv](https://arxiv.org/abs/2105.00931)

This work evaluates in AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Neural Task Graphs: Generalizing to Unseen Tasks from a Single Video Demonstration

`2018` `arXiv` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/1807.03480)

This work uses AI2-THOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### MemCompiler: Compile, Don't Inject -- State-Conditioned Memory for Embodied Agents

`2026` `arXiv` `memory`

Links: [arXiv](https://arxiv.org/abs/2605.07594)

This work evaluates in EmbodiedBench for embodied memory and spatial reasoning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents

`2026` `arXiv` `memory` `benchmark`

Links: [arXiv](https://arxiv.org/abs/2601.20831)

This work evaluates in EmbodiedBench for embodied memory and spatial reasoning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Interactive Environmental Learning in Physical Embodied Systems

`2025` `arXiv` `planning` `memory`

Links: [arXiv](https://arxiv.org/abs/2508.01415)

This work evaluates in EmbodiedBench for embodied memory and spatial reasoning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### When Should a Robot Think? Resource-Aware Reasoning via Reinforcement Learning for Embodied Robotic Decision-Making

`2026` `arXiv` `RL` `reasoning`

Links: [arXiv](https://arxiv.org/abs/2603.16673)

This work studies when an embodied agent should invoke expensive reasoning during robotic decision-making. Its ALFRED evaluation makes it relevant to AI2-THOR-family planning agents with resource-aware reasoning policies.

## Perception, Physics, and Scene Graphs

*Perception, physical reasoning, and scene-graph work relevant to AI2-THOR-style embodied interaction.*

### Learning About Objects by Learning to Interact with Them

`2020` `NeurIPS` `AI2-THOR` `self-supervised interaction`

Links: [Paper](https://proceedings.neurips.cc/paper/2020/hash/291597a100aadd814d197af4f4bab3a7-Abstract.html) · [Code](https://github.com/allenai/learning_from_interaction)

This work learns object extent and physical properties through unsupervised interaction in AI2-THOR. It broadens the ecosystem beyond navigation and instruction following by showing how embodied agents can acquire object knowledge through active manipulation.

### ActioNet: A Multimodal Dataset for Human Activities Using AI2-THOR

`2023` `ICIP` `activity recognition` `AI2-THOR`

Links: [Paper](https://ieeexplore.ieee.org/document/10222876) · [Code](https://github.com/Alee08/ActioNet) · [arXiv](https://arxiv.org/abs/2306.04692)

ActioNet uses AI2-THOR to generate multimodal egocentric observations for human activity recognition, including RGB, depth, segmentation, and metadata-style signals. It is useful for perception-focused work that needs controlled household activities rather than only navigation or task-success labels.

### Integrating Vision Foundation Models with Reinforcement Learning for Enhanced Object Interaction

`2025` `RCVE` `AI2-THOR` `SAM/YOLO/PPO`

Links: [Paper](https://arxiv.org/abs/2508.05838)

This paper integrates vision foundation models such as SAM and YOLOv5 with PPO agents in AI2-THOR kitchen environments. It studies how stronger object detection and segmentation can improve navigation and interaction success for embodied agents.

### PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding

`2025` `ICLR` `physics` `VLM evaluation`

Links: [Paper](https://arxiv.org/abs/2501.16411) · [Project](https://physbench.github.io/)

PhysBench evaluates VLM physical-world understanding across object properties, relations, scenes, and dynamics. It is relevant to AI2-THOR-style embodied agents because physical commonsense errors often become interaction, manipulation, and planning failures.

### ESCA: Contextualizing Embodied Agents via Scene-Graph Generation

`2025` `NeurIPS` `scene graphs` `perception`

Links: [Paper](https://arxiv.org/abs/2510.15963) · [Code](https://github.com/video-fm/ESCA) · [SGCLIP Code](https://github.com/video-fm/LASER)

ESCA uses spatial-temporal scene graphs as a perception layer for embodied agents. It argues that many embodied failures are perception failures, and that grounding agents in structured object-relation graphs can reduce hallucination, missed objects, and incorrect context assumptions.

### FunFact: Building Probabilistic Functional 3D Scene Graphs via Factor-Graph Reasoning

`2026` `arXiv` `scene graph` `benchmark`

Links: [arXiv](https://arxiv.org/abs/2604.03696)

This work evaluates in AI2-THOR for scene-graph and spatial reasoning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### See, Symbolize, Act: Grounding VLMs with Spatial Representations for Better Gameplay

`2026` `arXiv` `VLM` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2603.11601)

This work uses AI2-THOR for embodied perception. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### GRIP: A Unified Framework for Grid-Based Relay and Co-Occurrence-Aware Planning in Dynamic Environments

`2025` `arXiv` `navigation` `planning`

Links: [arXiv](https://arxiv.org/abs/2510.10865)

This work evaluates in AI2-THOR / RoboTHOR for embodied memory and spatial reasoning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### A Unified Framework for Real-Time Failure Handling in Robotics Using Vision-Language Models, Reactive Planner and Behavior Trees

`2025` `arXiv` `planning` `scene graph`

Links: [arXiv](https://arxiv.org/abs/2503.15202)

This work evaluates in AI2-THOR for scene-graph and spatial reasoning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Discovering Object Attributes by Prompting Large Language Models with Perception-Action APIs

`2024` `arXiv` `VLM` `LLM`

Links: [arXiv](https://arxiv.org/abs/2409.15505)

This work uses AI2-THOR for embodied perception. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### SegmATRon: Embodied Adaptive Semantic Segmentation for Indoor Environment

`2023` `arXiv` `segmentation` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2310.12031)

This work uses AI2-THOR for embodied perception. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Learning Concept-Based Causal Transition and Symbolic Reasoning for Visual Planning

`2023` `arXiv` `planning` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2310.03325)

This work uses AI2-THOR for embodied task planning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### CoReLIN: Constraint-based Reasoning for Zero-shot Lifelong Interactive Navigation

`2026` `arXiv` `navigation` `planning`

Links: [arXiv](https://arxiv.org/abs/2602.20055)

This work uses ProcTHOR for scene-graph and spatial reasoning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Investigating Domain Gaps for Indoor 3D Object Detection

`2025` `arXiv` `benchmark` `ProcTHOR`

Links: [arXiv](https://arxiv.org/abs/2508.17439)

This work evaluates in ProcTHOR for AI2-THOR-family embodied-agent workflows. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### Leveraging Semantics for Incremental Learning in Multi-Relational Embeddings

`2019` `arXiv` `perception` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/1905.12181)

Leveraging Semantics for Incremental Learning in Multi-Relational Embeddings reports experiments connected to AI2-THOR for perception. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Learning Affordance Landscapes for Interaction Exploration in 3D Environments

`2020` `arXiv` `perception` `iTHOR`

Links: [arXiv](https://arxiv.org/abs/2008.09241)

Learning Affordance Landscapes for Interaction Exploration in 3D Environments reports experiments connected to iTHOR for perception. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Towards Embodied Scene Description

`2020` `arXiv` `perception` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2004.14638)

Towards Embodied Scene Description reports experiments connected to AI2-THOR for perception. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### IFR-Explore: Learning Inter-object Functional Relationships in 3D Indoor Scenes

`2021` `arXiv` `perception` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2112.05298)

IFR-Explore: Learning Inter-object Functional Relationships in 3D Indoor Scenes reports experiments connected to AI2-THOR for perception. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Moment-based Adversarial Training for Embodied Language Comprehension

`2022` `arXiv` `perception` `ALFRED`

Links: [arXiv](https://arxiv.org/abs/2204.00889)

Moment-based Adversarial Training for Embodied Language Comprehension uses ALFRED as an embodied household-task benchmark for perception. Because ALFRED tasks are grounded in AI2-THOR scenes and interactions, the paper is relevant to instruction-following research in the AI2-THOR ecosystem.

### Behind the Veil: Enhanced Indoor 3D Scene Reconstruction with Occluded Surfaces Completion

`2024` `arXiv` `perception` `iTHOR`

Links: [arXiv](https://arxiv.org/abs/2404.03070)

Behind the Veil: Enhanced Indoor 3D Scene Reconstruction with Occluded Surfaces Completion reports experiments connected to iTHOR for perception. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### ODIN: A Single Model for 2D and 3D Segmentation

`2024` `arXiv` `perception` `TEACh`

Links: [arXiv](https://arxiv.org/abs/2401.02416)

ODIN: A Single Model for 2D and 3D Segmentation studies perception in TEACh-style embodied task completion. TEACh extends AI2-THOR household tasks with situated dialogue, making the work relevant to conversational instruction-following agents.

### Segment Any Object Model (SAOM): Real-to-Simulation Fine-Tuning Strategy for Multi-Class Multi-Instance Segmentation

`2024` `arXiv` `perception` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2403.10780)

Segment Any Object Model (SAOM): Real-to-Simulation Fine-Tuning Strategy for Multi-Class Multi-Instance Segmentation reports experiments connected to AI2-THOR for perception. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents

`2026` `arXiv` `perception` `ALFWorld`

Links: [arXiv](https://arxiv.org/abs/2606.25852)

Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents evaluates agent methods on ALFWorld, the text-game environment aligned with ALFRED and THOR household tasks. It is included as an ALFRED-derived planning and evaluation entry rather than as direct AI2-THOR simulator execution.

## Datasets and Assets

*Datasets, assets, and derived benchmark resources for AI2-THOR-family workflows.*

### Objaverse-THOR / Objathor

`dataset` `assets` `Objaverse` `ProcTHOR`

Links: [Code](https://github.com/allenai/objathor) · [Dataset tools](https://github.com/allenai/objathor/tree/main/objathor/dataset)

Objathor provides tools and dataset utilities for importing, annotating, and preparing Objaverse-style 3D assets for AI2-THOR and ProcTHOR workflows. It supports the asset side of large-scale environment generation.

### Semantic2Thor Dataset

`dataset` `semantics` `affordances`

Links: [Code](https://github.com/maxzuo/semantic-ai2thor-dataset)

Semantic2Thor augments AI2-THOR pickupable objects with semantic embeddings, WordNet/ConceptNet links, Walmart category information, and affordance vectors. It is useful for object commonsense, semantic grounding, and affordance-aware planning.

### MAP-THOR

`benchmark` `multi-agent` `planning`

Links: [Paper](https://arxiv.org/abs/2407.10031) · [Code](https://github.com/nsidn98/LLaMAR)

MAP-THOR is the multi-agent household planning test suite introduced with LLaMAR. It extends the AI2-THOR task setting toward partial observability, multi-agent coordination, information asymmetry, and long-horizon household collaboration.

### ProcTHOR-10K

`dataset` `ProcTHOR` `scenes`

Links: [Code](https://github.com/allenai/procthor) · [Dataset](https://huggingface.co/datasets/allenai/procthor-10k)

ProcTHOR-10K is an official release of procedurally generated interactive household scenes for ProcTHOR. It is useful as a compact, citable scene corpus for navigation, rearrangement, active perception, and embodied-agent evaluation.

### AI2-THOR ObjectNav Evaluation Datasets

`dataset` `ObjectNav` `evaluation`

Links: [Code](https://github.com/allenai/robothor-challenge) · [Dataset](https://ai2thor.allenai.org/robothor/objectnav-dataset/)

The official ObjectNav evaluation datasets support RoboTHOR and AI2-THOR-family ObjectNav challenge workflows. They provide the task instances and split definitions needed to compare navigation agents under standard evaluation conditions.

### MM-Conv: A Multi-modal Conversational Dataset for Virtual Humans

`2024` `arXiv` `scene graph` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2410.00253)

This work uses AI2-THOR for scene-graph and spatial reasoning. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### DStruct2Design: Data and Benchmarks for Data Structure Driven Generative Floor Plan Design

`2024` `arXiv` `benchmark` `LLM`

Links: [arXiv](https://arxiv.org/abs/2407.15723)

This work evaluates in ProcTHOR for scene generation and environment design. It is included as a primary arXiv entry because the abstract explicitly connects the method, benchmark, or dataset to the AI2-THOR-family ecosystem.

### ProcTHOR-10K Repository

`ProcTHOR` `dataset` `houses`

Links: [Code](https://github.com/allenai/procthor-10k)

The ProcTHOR-10K repository provides dataset files and tooling for the generated house corpus. It complements the Hugging Face dataset entry with a GitHub resource for ProcTHOR scene data.

### Habitat Synthetic Scenes Dataset (HSSD-200): An Analysis of 3D Scene Scale and Realism Tradeoffs for ObjectGoal Navigation

`2023` `arXiv` `navigation` `ProcTHOR`

Links: [arXiv](https://arxiv.org/abs/2306.11290)

Habitat Synthetic Scenes Dataset (HSSD-200): An Analysis of 3D Scene Scale and Realism Tradeoffs for ObjectGoal Navigation reports experiments connected to ProcTHOR for navigation. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

### Video2Layout: Recall and Reconstruct Metric-Grounded Cognitive Map for Spatial Reasoning

`2025` `arXiv` `perception` `AI2-THOR`

Links: [arXiv](https://arxiv.org/abs/2511.16160)

Video2Layout: Recall and Reconstruct Metric-Grounded Cognitive Map for Spatial Reasoning reports experiments connected to AI2-THOR for perception. It is included from the primary arXiv record because the abstract explicitly names the AI2-THOR-family simulator, benchmark, or derived environment.

## Tools and Environments

*Wrappers, infrastructure, visualization tools, and community environments for AI2-THOR-family research.*

### AllenAct

`2020` `framework` `embodied AI training`

Links: [Paper](https://arxiv.org/abs/2008.12760) · [Project](https://allenact.org/) · [Code](https://github.com/allenai/allenact)

AllenAct is a modular embodied-AI training framework from AI2. It includes abstractions and baselines for AI2-THOR-family tasks, making it useful infrastructure for reproducible navigation, manipulation, and instruction-following experiments.

### RoboTHOR ObjectNav Challenge

`challenge` `RoboTHOR` `ObjectNav`

Links: [Code](https://github.com/allenai/robothor-challenge)

The RoboTHOR ObjectNav Challenge repository provides official datasets, baselines, metrics, challenge scripts, and submission tooling for navigation in RoboTHOR. It is the practical infrastructure companion to the RoboTHOR sim-to-real benchmark.

### AI2-THOR Docker

`tool` `infrastructure` `rendering`

Links: [Code](https://github.com/allenai/ai2thor-docker)

AI2-THOR Docker packages the simulator rendering stack for reproducible headless or GPU-backed execution. It is useful when running AI2-THOR experiments on servers, clusters, or containerized training pipelines.

### ProcTHOR RL

`tool` `ProcTHOR` `ObjectNav training`

Links: [Code](https://github.com/allenai/procthor-rl)

ProcTHOR RL contains training and evaluation scripts for ObjectNav agents in ProcTHOR. It is useful both as official infrastructure for ProcTHOR experiments and as a concrete reference for large-scale AI2-THOR-family reinforcement learning.

### AI2-THOR Examples

`examples` `documentation` `controller API`

Links: [Project](https://ai2thor.allenai.org/examples/) · [Code](https://github.com/allenai/ai2thor)

The official AI2-THOR examples page gives runnable snippets for controller setup, navigation, object metadata, image observations, and interaction actions. It is one of the best practical entry points for new users learning the simulator API.

### AI2-THOR Publications Index

`bibliography` `official index` `publications`

Links: [Project](https://ai2thor.allenai.org/publications/)

The official AI2-THOR publications page tracks papers across the simulator ecosystem. It is a useful companion resource for this curated list because it helps verify whether a candidate work has an explicit AI2-THOR-family connection.

### AI2-THOR Colab

`tool` `Colab` `runtime helper`

Links: [Code](https://github.com/allenai/ai2thor-colab)

AI2-THOR Colab provides helper utilities for running AI2-THOR in Google Colab, including display and X-server setup. It is useful for lightweight demos, tutorials, and quick experiments without a full local Unity setup.

### ai2thor-web

`tool` `web control` `data collection`

Links: [Code](https://github.com/zkytony/ai2thor-web)

ai2thor-web provides a browser-based interface for remotely controlling AI2-THOR and collecting user-study data. It is useful when experiments require humans to interact with simulator scenes through a web UI.

### RL-THOR

`tool` `Gymnasium-style wrapper` `RL`

Links: [Code](https://github.com/Kajiih/rl_thor)

RL-THOR is a lightweight reinforcement-learning wrapper around AI2-THOR with customizable tasks and a Gym-like API. It is another practical option for building small AI2-THOR RL experiments without adopting a larger framework.

### Indoor Scene Generation for EAI / Luminous-for-ALFRED

`tool` `scene generation` `ALFRED`

Links: [Code](https://github.com/amazon-science/indoor-scene-generation-eai)

This Amazon Science project provides indoor scene generation and ALFRED task/trajectory generation tooling. It is useful for expanding ALFRED-style household task data and studying how generated scenes affect embodied instruction following.

### TEACh TATC

`tool` `TEACh` `two-agent challenge`

Links: [Code](https://github.com/GLAMOR-USC/teach_tatc)

TEACh TATC adapts TEACh into a two-agent task-completion setting with Commander/Follower collaboration. It is useful for experiments that separate instruction generation, communication, and embodied execution within the TEACh lineage.

### ALFRED-RL

`tool` `ALFRED` `RL environment`

Links: [Code](https://github.com/clvrai/sprint)

ALFRED-RL is the reinforcement-learning environment and training stack released inside SPRINT. It connects ALFRED task execution with online/offline RL workflows and is used by later ALFRED policy-training work.

### ProcTHOR-Nav-Vis

`tool` `visualization` `ProcTHOR`

Links: [Code](https://github.com/khm159/ProcthorNavVis)

ProcTHOR-Nav-Vis is a visualization and demo-video generation toolkit for ProcTHOR environments. It supports interactive coordinate/action annotation and scripted replay from multiple camera perspectives.

### thor2blender

`tool` `Blender` `scene export`

Links: [Code](https://github.com/Tomoya-Matsubara/thor2blender)

thor2blender helps move AI2-THOR scene information into Blender workflows. It is useful for rendering, visualization, dataset generation, and multi-view synthetic data pipelines outside the default AI2-THOR renderer.

### ai2thor-gym

`tool` `Gymnasium wrapper` `RL`

Links: [Code](https://github.com/m-barker/ai2thor-gym)

ai2thor-gym wraps AI2-THOR with a Gymnasium-style interface. The included egg-cooking example demonstrates task progress rewards over object search, interaction, and cooking actions in a kitchen scene.

### cups-rl

`tool` `RL` `transfer learning`

Links: [Code](https://github.com/TheMTank/cups-rl)

cups-rl contains reinforcement-learning experiments for domain and task transfer in AI2-THOR household tasks. It focuses on learning transferable object interaction behavior, such as picking up cups under varying conditions.

### ai2thor-task-planner

`tool` `PDDL` `planning`

Links: [Code](https://github.com/xHugo21/ai2thor-task-planner)

ai2thor-task-planner executes tasks in iTHOR using automated planning and neural perception components. It can generate PDDL problems from simulator metadata or perception, produce plans, and translate them back into executable simulator actions.

### Embodied Reasoning Agent

`codebase` `ERA` `online RL`

Links: [Code](https://github.com/Embodied-Reasoning-Agent/Embodied-Reasoning-Agent)

This is the released codebase for ERA, including embodied prior learning and online reinforcement learning components for VLM-based embodied agents.

### thortils

`tool` `AI2-THOR` `utilities`

Links: [Code](https://github.com/zkytony/thortils)

thortils provides utility functions for working with AI2-THOR, aiming to make common simulator operations reusable across projects. It is a practical support library for AI2-THOR experimentation and scripting.

### AI2Thor Keyboard Player

`tool` `AI2-THOR` `data collection`

Links: [Code](https://github.com/ByZ0e/AI2Thor_keyboard_player)

AI2Thor Keyboard Player is a keyboard-based interaction and data-collection tool for AI2-THOR. It can help users manually inspect scenes, collect demonstrations, or debug simulator actions.

### AI2 ObjectNav Evaluation

`ObjectNav` `evaluation` `RoboTHOR`

Links: [Code](https://github.com/allenai/object-nav-eval)

object-nav-eval provides evaluation tasks for ObjectNav models in the AllenAI embodied-AI ecosystem. It is useful infrastructure for benchmarking AI2-THOR-family navigation agents.

### RobustNav

`navigation` `corruptions` `RoboTHOR`

Links: [Code](https://github.com/allenai/robustnav)

RobustNav evaluates pretrained navigation agents under visual corruptions and distribution shifts. It is relevant to AI2-THOR-family navigation because it builds on RoboTHOR-style embodied evaluation.

### ADVISOR

`AllenAI` `training` `RoboTHOR`

Links: [Code](https://github.com/allenai/advisor)

ADVISOR is an AllenAI embodied-agent training codebase associated with AI2-THOR-family navigation research. It is useful for readers looking for training infrastructure beyond the core simulator.

### PRIOR Data Package

`AllenAI` `dataset distribution` `ProcTHOR`

Links: [Code](https://github.com/allenai/prior)

PRIOR is AllenAI infrastructure for seamless data distribution in AI workflows. It is useful around AI2-THOR-family datasets such as ProcTHOR resources and embodied-agent assets.

## Tutorials and Notes

*Secondary and community learning resources. Prefer primary paper, project, or code links for academic entries.*

### CSDN AI2-THOR tutorial

`tutorial` `community note` `AI2-THOR`

Links: [Tutorial](https://blog.csdn.net/u010705932/article/details/104472316)

A community tutorial for getting familiar with AI2-THOR usage. Keep this as a learning resource rather than a paper citation.

### AI2-THOR Documentation

`official docs` `API` `getting started`

Links: [Code](https://github.com/allenai/ai2thor) · [Tutorial](https://ai2thor.allenai.org/ithor/documentation/)

The official AI2-THOR documentation covers installation, controller usage, actions, event metadata, scenes, and object interaction APIs. It is the most reliable starting point for reproducing papers or building new simulator experiments.

### AllenAct ObjectNav Tutorial

`tutorial` `AllenAct` `ObjectNav`

Links: [Code](https://github.com/allenai/allenact) · [Tutorial](https://allenact.org/tutorials/robothor-tutorial/)

This AllenAct tutorial walks through RoboTHOR ObjectNav training and evaluation with the AllenAct framework. It is useful for readers who want to move from the curated paper list to a concrete reproducible navigation baseline.

### ALFRED Documentation and Leaderboards

`ALFRED` `documentation` `leaderboard`

Links: [Code](https://github.com/askforalfred/alfred) · [Tutorial](https://askforalfred.com/)

The official ALFRED site links the benchmark paper, dataset, leaderboard, challenge information, and implementation resources. It is a practical reference for understanding the AI2-THOR-based instruction-following benchmark and its evaluation protocol.

### Cook2LTL CSDN note

`tutorial` `community note` `Cook2LTL`

Links: [Note](https://blog.csdn.net/muyulingfengye/article/details/144618712) · [Official code](https://github.com/angmavrogiannis/Cook2LTL)

A secondary Chinese note about Cook2LTL. Prefer citing the official paper and repository in academic or project documentation.

## Contributing

Edit `data.yml` first, then regenerate this README:

```bash
python scripts/validate_data.py
python scripts/generate_readme.py
```

Entry format:

```markdown
### Title

`year` `venue/status` `topic` `ecosystem`

Links: [Paper](paper-url) · [Project](project-url) · [Code](repo-url)

One concise paragraph explaining how the work uses, extends, benchmarks, or supports AI2-THOR-family systems.
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for scope, verification rules, status labels, and review policy.
