# Awesome AI2-THOR

[![AI2-THOR](https://img.shields.io/badge/AI2--THOR-ecosystem-blue)](https://ai2thor.allenai.org/)
[![Papers](https://img.shields.io/badge/papers-curated-success)](#contents)
[![Contributions](https://img.shields.io/badge/contributions-welcome-informational)](CONTRIBUTING.md)

A curated map of papers, benchmarks, datasets, environments, and tools built on top of [AI2-THOR](https://ai2thor.allenai.org/) and its ecosystem, including iTHOR, RoboTHOR, ProcTHOR, ManipulaTHOR, ArchitecTHOR, ALFRED, TEACh, and EmbodiedBench.

The list focuses on work with a clear AI2-THOR-family connection. Each entry includes primary paper/project links and open-source repositories when they are available.

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

Links: [Paper](https://arxiv.org/abs/2212.04819) · [Project](https://allenai.org/project/phone2proc)

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

## Benchmarks and Evaluation

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

Links: [Paper](https://arxiv.org/abs/2202.13330) · [Challenge](https://eval.ai/web/challenges/challenge-page/1859/overview) · [Code](https://github.com/xfgao/DialFRED)

DialFRED augments ALFRED with agent-initiated clarification questions and human answers. It is useful for studying when an embodied agent should ask for missing information instead of blindly executing an underspecified instruction.

### Dialog Acts for Task-Driven Embodied Agents

`2022` `SIGDIAL` `dialogue annotation` `TEACh`

Links: [Paper](https://arxiv.org/abs/2209.12953) · [Code](https://github.com/alexa/teach)

This work annotates TEACh dialogues with dialog acts and studies how those labels help embodied task execution. It adds a pragmatic dialogue layer to AI2-THOR household tasks, making it easier to analyze instructions, questions, confirmations, corrections, and action-relevant utterances.

### Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making

`2024` `NeurIPS Datasets and Benchmarks` `LLM evaluation`

Links: [Paper](https://openreview.net/forum?id=iSwK1YqO7v) · [Project](https://embodied-agent-interface.github.io/)

Embodied Agent Interface defines a common interface for evaluating LLMs as embodied decision modules. Instead of reporting only final task success, it decomposes embodied decision making into interpretable stages such as goal interpretation, subgoal decomposition, action generation, and state transition modeling.

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

### CL-ALFRED: Online Continual Learning for Interactive Instruction Following Agents

`2024` `ICLR` `continual learning` `ALFRED`

Links: [Paper](https://openreview.net/forum?id=7M0EzjugaN) · [Project](https://bhkim94.github.io/projects/CL-ALFRED/) · [Code](https://github.com/snumprlab/cl-alfred)

CL-ALFRED turns ALFRED into a continual-learning benchmark with behavior-incremental and environment-incremental streams. It measures whether embodied instruction-following agents can adapt to new tasks and scenes without catastrophically forgetting prior household skills.

### ReALFRED: An Embodied Instruction Following Benchmark in Photo-Realistic Environments

`2024` `ECCV` `ALFRED-derived` `photo-realistic benchmark`

Links: [Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1610_ECCV_2024_paper.php) · [Project](https://twoongg.github.io/projects/realfred/) · [Code](https://github.com/snumprlab/realfred)

ReALFRED extends ALFRED-style instruction following to photo-realistic scanned multi-room environments. It is included as direct ALFRED lineage, but it should be read as ALFRED-derived rather than a native AI2-THOR benchmark.

## Instruction Following and Household Tasks

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

Links: [Workshop](https://askforalfred.com/EAI21/) · [Code](https://github.com/snumprlab/abp) · [Dataset](https://huggingface.co/datasets/byeonghwikim/abp_dataset)

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

Links: [Paper](https://arxiv.org/abs/2210.12485) · [ACL Anthology](https://aclanthology.org/2022.emnlp-main.83/) · [Code](https://github.com/sled-group/DANLI)

DANLI introduces a deliberative neuro-symbolic agent for following natural-language instructions. It maintains task progress and symbolic state to reason about preconditions and subgoals, reducing purely reactive behavior in long-horizon household tasks.

### LACMA: Language-Aligning Contrastive Learning with Meta-Actions

`2023` `EMNLP` `ALFRED` `contrastive learning`

Links: [Paper](https://arxiv.org/abs/2310.12344) · [ACL Anthology](https://aclanthology.org/2023.emnlp-main.77/) · [Code](https://github.com/joeyy5588/LACMA)

LACMA improves ALFRED generalization by explicitly aligning language instructions with agent hidden states and introducing meta-actions as an intermediate semantic layer. The work targets the gap between natural language goals and low-level action sequences.

### SPRINT: Scalable Policy Pre-Training via Language Instruction Relabeling

`2024` `ICRA` `ALFRED` `policy pretraining`

Links: [Paper](https://arxiv.org/abs/2306.11886) · [Project](https://clvrai.github.io/sprint/) · [Code](https://github.com/clvrai/sprint)

SPRINT relabels and chains ALFRED trajectories to pretrain reusable household skills at scale. Its ALFRED-RL setup connects offline instruction relabeling with downstream long-horizon execution in the ALFRED simulator.

### LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models

`2023` `ICCV` `LLM planning`

Links: [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Song_LLM-Planner_Few-Shot_Grounded_Planning_for_Embodied_Agents_with_Large_Language_Models_ICCV_2023_paper.html) · [Project](https://dki-lab.github.io/LLM-Planner/) · [Code](https://github.com/OSU-NLP-Group/LLM-Planner)

LLM-Planner uses few-shot prompting to turn large language models into grounded high-level planners for embodied agents. It provides prompt-generation and end-to-end examples that connect language model plans to executable embodied task steps.

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

## Navigation

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

## Planning, Memory, and Multi-Agent Systems

### Visual Semantic Planning using Deep Successor Representations

`2017` `ICCV` `THOR` `visual semantic planning`

Links: [Paper](https://arxiv.org/abs/1705.08080) · [Project](https://prior.allenai.org/projects/visual-semantic-planning)

Visual Semantic Planning learns to predict action sequences that change object states in THOR. It is an early precursor to household interaction benchmarks because it goes beyond navigation into planning around object affordances and state-changing actions.

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

## RL-Trained VLM Agents

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

### Verifier-Guided Action Selection for Embodied Agents

`2026` `arXiv` `EB-ALFRED` `verifier`

Links: [Paper](https://arxiv.org/abs/2605.12620)

Verifier-Guided Action Selection uses a verifier to score and choose actions for embodied agents. It is included because its evaluation uses EmbodiedBench's EB-ALFRED implementation, which is derived from ALFRED and AI2-THOR.

## Perception, Physics, and Scene Graphs

### Learning About Objects by Learning to Interact with Them

`2020` `NeurIPS` `AI2-THOR` `self-supervised interaction`

Links: [Paper](https://proceedings.neurips.cc/paper/2020/hash/291597a100aadd814d197af4f4bab3a7-Abstract.html) · [Code](https://github.com/allenai/learning_from_interaction)

This work learns object extent and physical properties through unsupervised interaction in AI2-THOR. It broadens the ecosystem beyond navigation and instruction following by showing how embodied agents can acquire object knowledge through active manipulation.

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

## Datasets and Assets

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

### infinity-THOR

`benchmark` `long-context` `long-horizon`

Links: [Paper](https://arxiv.org/abs/2505.16928)

infinity-THOR is the long-horizon task generation framework introduced in Beyond Needle(s) in the Embodied Haystack. It is designed for testing long-context embodied reasoning over extended trajectories and multi-step QA-style tasks.

## Tools and Environments

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

Links: [Code](https://github.com/Embodied-Reasoning-Agent/Embodied-Reasoning-Agent) · [Paper](https://arxiv.org/abs/2510.12693)

This is the released codebase for ERA, including embodied prior learning and online reinforcement learning components for VLM-based embodied agents.

### DualTHOR

`environment` `dual-arm humanoid` `interaction`

Links: [Code](https://github.com/ds199895/DualTHOR)

DualTHOR extends AI2-THOR into a dual-arm humanoid environment with richer action execution, contingency modeling, task replay, inverse-kinematics-based motion, and more detailed object state transitions. It is especially relevant for studying bimanual planning and failure recovery.

## Tutorials and Notes

### CSDN AI2-THOR tutorial

Links: [Tutorial](https://blog.csdn.net/u010705932/article/details/104472316)

A community tutorial for getting familiar with AI2-THOR usage. Keep this as a learning resource rather than a paper citation.

### Cook2LTL CSDN note

Links: [Note](https://blog.csdn.net/muyulingfengye/article/details/144618712) · [Official code](https://github.com/angmavrogiannis/Cook2LTL)

A secondary Chinese note about Cook2LTL. Prefer citing the official paper and repository in academic or project documentation.

## Contributing

Use primary sources where possible and keep each entry compact:

```markdown
### Paper or Project Title

`year` `venue/status` `topic`

Links: [Paper](paper-url) · [Project](project-url) · [Code](repo-url)

One concise paragraph explaining how the work uses or extends AI2-THOR.
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for verification rules and suggested categories.
