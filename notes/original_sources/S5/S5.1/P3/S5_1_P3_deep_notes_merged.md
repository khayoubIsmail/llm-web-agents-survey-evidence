# S5.1 P3 — Deep Notes, Venue/Status Verification, and Section Synthesis

**Section:** S5.1 — Benchmarks and Evaluation for LLM-Based Agents / Web Agents  
**Priority:** P3 supporting literature  
**Purpose:** These papers are not necessarily core web-agent benchmarks, but they strengthen the evaluation chapter by showing how the broader agent-evaluation field measures multi-agent reasoning, repository-level execution, multimodal planning, data-analysis execution, agent-as-judge evaluation, and GUI/task-completion judging.

---

## 0. Executive Summary

This S5.1 P3 batch contains **6 papers**:

| # | Paper | Main evaluation angle | Venue / status | Use strength |
|---|---|---|---|---|
| 1 | MAgIC | Multi-agent cognition, collaboration, rationality | **EMNLP 2024 main conference** | Safe supporting citation |
| 2 | ML-Bench | Repository-level ML/code-agent execution | **ICLR 2025 AgenticAI Workshop Oral**; not main ICLR | Use as workshop benchmark |
| 3 | EgoPlan-Bench | Multimodal egocentric planning | **International Journal of Computer Vision, 2026**; originally arXiv 2023/2024 | Safe supporting citation |
| 4 | InfiAgent-DABench | Data-analysis agent benchmark | **ICML 2024** | Safe supporting citation |
| 5 | Auto-Eval Judge | General modular agent-as-judge framework | **arXiv 2025 preprint** | Use cautiously |
| 6 | Computer-Use Agents as Judges for Generative UI | CUA-as-judge for agent-native GUI design | **arXiv 2025; ICLR 2026 withdrawn submission** | Use only as grey/preprint evidence |

**Main S5.1 synthesis:** These papers show that agent evaluation is moving from static answer accuracy toward **interactive, process-aware, environment-grounded, and judge-assisted evaluation**. For your survey, they support the claim that web-agent benchmarks should evaluate not only final task success, but also intermediate trajectory quality, tool/environment interaction, recoverability from errors, cost, execution traces, and task-verification mechanisms. However, most of these benchmarks are still **not extraction-specific**: they evaluate reasoning, planning, code execution, data analysis, or GUI navigation, but they do not jointly evaluate schema-guided web data extraction, provenance, pagination completeness, source grounding, and field-level correctness.

---

## 1. Venue / Status Verification Table

| Paper | Uploaded version status | Verified final / current status | Citation caution |
|---|---|---|---|
| MAgIC | arXiv v3, 2024 | EMNLP 2024 main proceedings, ACL Anthology ID 2024.emnlp-main.416, DOI 10.18653/v1/2024.emnlp-main.416 | Strong citation. Use final EMNLP version. |
| ML-Bench | arXiv v5, 2024; uploaded PDF says “Preprint. Under review.” | OpenReview shows ICLR 2025 Workshop AgenticAI **Oral**. A separate ICLR 2025 main-conference thread exists as submitted, not final accepted main conference. | Cite as ICLR 2025 AgenticAI Workshop Oral or arXiv/workshop, not main ICLR. |
| EgoPlan-Bench | arXiv v3, 2024; uploaded PDF says “Preprint. Under review.” | International Journal of Computer Vision, open-access Original Paper, article 118, published 12 Feb 2026, DOI 10.1007/s11263-025-02676-0 | Strong citation. Use IJCV version when possible. |
| InfiAgent-DABench | arXiv v3, 2024; uploaded PDF uses early counts: 257 questions / 52 CSV files | ICML 2024, PMLR volume 235, pages 19544–19572. Final version uses larger DAEval counts: 603 questions / 124 CSV files. | Strong citation. Use final ICML counts, not older arXiv counts, in final survey. |
| Auto-Eval Judge | arXiv 2025 | No peer-reviewed venue found; Microsoft/UMass-related arXiv preprint | Cite cautiously as preprint/technical framework. |
| Computer-Use Agents as Judges for Generative UI | arXiv 2025 | OpenReview shows ICLR 2026 **Withdrawn Submission**; arXiv/project page still available | Use only as grey/preprint evidence; do not present as accepted. |

---

# 2. Paper Notes

---

# 2.1 MAgIC: Investigation of Large Language Model Powered Multi-Agent in Cognition, Adaptability, Rationality and Collaboration

## Venue / Status

- **Final venue:** EMNLP 2024 main conference.
- **Status:** Peer-reviewed conference paper.
- **Uploaded version:** arXiv v3, 27 Nov 2024.
- **Venue caution:** Use the final ACL Anthology / EMNLP citation, not only the arXiv version.

## Core idea

MAgIC proposes a competition-based benchmark for evaluating LLMs as agents in multi-agent settings. Instead of testing isolated reasoning or single-agent tool use, it evaluates whether models can reason about other agents, adapt under uncertainty, cooperate, coordinate, deceive, and act rationally in interactive environments.

## Key contribution

The paper contributes a multi-agent evaluation framework built around **five scenarios**:

1. Chameleon
2. Undercover
3. Cost Sharing
4. Multi-turn Prisoner’s Dilemma
5. Public Good

It defines **seven quantitative capability metrics**:

1. Judgment
2. Reasoning
3. Deception
4. Self-awareness
5. Cooperation
6. Coordination
7. Rationality

This is important because many agent benchmarks reduce performance to a single success rate. MAgIC instead decomposes agent ability into interpretable dimensions.

## Method / approach

The benchmark places challenger LLMs against fixed defender agents in competitive and collaborative game settings. The paper evaluates models by role-specific win rates and intermediate behavioral metrics. It also proposes a **PGM-aware agent**, where Probabilistic Graphical Models structure an agent’s reasoning about other agents’ beliefs, roles, and strategies.

The key methodological idea is that multi-agent success depends on reasoning over partial information and recursively modeling what other agents believe. The PGM layer formalizes this with multi-perspective variables such as an agent’s interpretation of the global state from different players’ viewpoints.

## Evaluation details

- Evaluates multiple LLMs, including GPT variants, Claude, PaLM, Cohere, and Llama-2-70B.
- Uses radar charts to visualize the seven ability dimensions.
- Reports that stronger models substantially outperform weaker models across the multi-agent ability area.
- The uploaded PDF states that GPT-o1 is the strongest and Llama-2-70B the weakest, with more than a threefold capability gap.
- The PGM enhancement improves measured abilities by about **37% on average**.

## Key findings

1. LLM agents differ significantly across social and strategic dimensions.
2. Good final win rate correlates with stronger area under the seven-dimensional ability profile.
3. PGM-aware reasoning improves several abilities, especially judgment, coordination, and rationality.
4. Multi-agent interaction exposes limitations not visible in single-agent benchmarks.

## Limitations

- The benchmark is based on artificial game environments, not real-world web tasks.
- The metrics are useful but scenario-dependent; deception and rationality in games do not directly map to benign web automation.
- It evaluates social/multi-agent cognition, not web navigation, web grounding, or data extraction.
- The PGM enhancement is more of a reasoning scaffold than a general evaluation method.

## Relevance to your thesis / survey

MAgIC is useful in S5.1 as evidence that agent evaluation is becoming **multi-dimensional**. It supports the argument that a single task success rate is insufficient for evaluating complex agents. For web data extraction agents, the analogous dimensions would be navigation success, field correctness, provenance accuracy, schema adherence, robustness, cost, and safety.

It is not directly about web automation or extraction, but it strengthens the methodological foundation for decomposed evaluation.

## How to use it in S5.1

Use MAgIC in the subsection on **general agent evaluation beyond final accuracy**. It can support a paragraph explaining that agent benchmarks increasingly decompose performance into capability dimensions rather than treating agents as black-box answer generators.

## Connects to

- **S3:** Agent architectures and multi-agent systems
- **S5.1:** Benchmark design and agent evaluation metrics
- **S5.3:** Reasoning, planning, and strategic decision-making
- **S8:** Need for richer evaluation frameworks

## Sentence to add later

> Beyond web-specific environments, MAgIC illustrates a broader trend in agent benchmarking: evaluating agents through decomposed behavioral dimensions such as judgment, reasoning, cooperation, coordination, and rationality, rather than relying only on aggregate success rates.

## Citation caution

Safe to cite strongly as **EMNLP 2024**. Use it as supporting evidence for multi-dimensional agent evaluation, not as evidence for web-agent extraction performance.

---

# 2.2 ML-Bench: Evaluating Large Language Models and Agents for Machine Learning Tasks on Repository-Level Code

## Venue / Status

- **Current verified status:** ICLR 2025 Workshop on Agentic AI, Oral.
- **Uploaded version:** arXiv v5, 21 Aug 2024; marked “Preprint. Under review.”
- **Venue caution:** Do not cite as accepted ICLR main conference. Cite as **ICLR 2025 AgenticAI Workshop Oral** or arXiv/workshop paper.

## Core idea

ML-Bench evaluates whether LLMs and agents can understand and use real machine-learning repositories at repository scale. It moves beyond function-level code benchmarks by requiring models to interpret README files, cross-file dependencies, command-line arguments, package environments, and executable workflows.

## Key contribution

The benchmark provides **9,641 examples across 18 GitHub repositories** and two evaluation settings:

1. **ML-LLM-Bench:** tests LLMs’ ability to generate bash/Python code in a preconfigured environment.
2. **ML-Agent-Bench:** tests autonomous agents end-to-end in a Linux sandbox, including repository exploration, dependency setup, data preparation, command execution, and final task completion.

This distinction is important because static code generation and interactive code-agent execution are different capabilities.

## Method / approach

The benchmark is constructed from real ML repositories. Annotators mine tasks from README files and repository documentation, extract parameters, generate diverse instructions, produce reference code, and verify executability. In the agent setting, agents operate inside a sandbox and iteratively execute commands, inspect errors, and revise their approach.

The evaluation uses:

- **Pass@K** for LLM code-generation tasks.
- **Success Rate** for end-to-end agent execution.
- Error categories such as hallucination, missing information, knowledge manipulation, syntax errors, and operational errors.

## Evaluation details

The uploaded paper reports:

- GPT-4o is the only tested LLM to exceed 50% Pass@5 in the ML-LLM-Bench setting.
- Human annotators reach 86.76% on the same subset, showing large remaining gaps.
- In ML-Agent-Bench, OpenDevin with GPT-4o reaches **76.47% success rate** on the evaluated subset.
- Agent framework choice matters: with the same underlying model, different frameworks obtain very different success rates.

## Key findings

1. Repository-level automation requires more than code generation; it requires long-context repository understanding and environment interaction.
2. Bash/script generation is harder than Python snippet generation.
3. Retrieval that is not task-specific can harm performance.
4. Interactive feedback improves execution but does not eliminate hallucination or environment setup errors.
5. Agent framework design materially affects task success.

## Limitations

- Domain is machine-learning repositories, not web environments.
- Evaluation focuses on executable repository tasks, not web navigation or extraction.
- Some tasks are README-derived, which may bias toward documented repository functionality.
- The strongest results depend on GPT-4o and specific agent frameworks.
- Workshop status means the citation is useful but less strong than a main conference/journal benchmark.

## Relevance to your thesis / survey

ML-Bench is highly relevant as a **methodological analog** for evaluating agents in complex software environments. It supports your argument that realistic agent evaluation must include:

- environment setup,
- interaction traces,
- error recovery,
- tool execution,
- artifact verification,
- and end-to-end task success.

For generalized web data extraction, the equivalent would be: browser setup, navigation, page-state inspection, extraction code/tool use, pagination, schema validation, provenance verification, and cost-aware completion.

## How to use it in S5.1

Use ML-Bench as evidence that agent benchmarks are evolving from static prompt-answer evaluation to **sandboxed, end-to-end execution evaluation**. It can support a paragraph contrasting code-agent benchmarks with web-agent benchmarks.

## Connects to

- **S3:** Tool-using and code-executing agents
- **S5.1:** End-to-end agent benchmarks
- **S5.3:** Planning and self-debugging
- **S5.6 / deployment:** Environment setup and operational constraints
- **S6:** Extraction pipelines that may require code/tool execution

## Sentence to add later

> ML-Bench shows that realistic agent evaluation must account for repository-scale context, environment setup, iterative execution, and error recovery, suggesting that web-agent benchmarks should similarly move beyond final answers toward end-to-end environment-grounded task completion.

## Citation caution

Use as **ICLR 2025 AgenticAI Workshop Oral** or arXiv/workshop benchmark. Do not call it a main-conference ICLR paper.

---

# 2.3 EgoPlan-Bench: Benchmarking Multimodal Large Language Models for Human-Level Planning

## Venue / Status

- **Final/current status:** International Journal of Computer Vision, 2026, open-access original paper.
- **Original uploaded version:** arXiv v3, 11 Jun 2024, marked “Preprint. Under review.”
- **Venue caution:** Use the final IJCV journal version when citing in the final survey.

## Core idea

EgoPlan-Bench evaluates whether multimodal LLMs can perform human-level planning from egocentric visual observations. The benchmark asks a model to infer the next appropriate action given a task goal, task progress video, and current observation.

This is different from ordinary video QA: the goal is not only to understand what happened, but to decide what action should come next.

## Key contribution

The benchmark introduces a planning-oriented evaluation setting using first-person video data. It contains human-verified multiple-choice questions derived from egocentric video sources such as Epic-Kitchens and Ego4D.

The uploaded version reports:

- **4,939 multiple-choice questions**
- **3,269 task goals**
- **3,185 action plans**
- **234 verbs**
- **558 objects**
- **419 scenes**

It also introduces **EgoPlan-IT**, an instruction-tuning dataset designed to improve planning ability.

## Method / approach

EgoPlan-Bench constructs task goals by hierarchical goal extraction from dense video narrations. It then creates multiple-choice planning questions where the model must select the next action. Candidate negative answers are chosen from actions under the same task goal, making all options semantically plausible unless the model uses visual state and progress information.

The construction pipeline includes:

1. Egocentric video source selection.
2. Hierarchical task-goal extraction using GPT-4.
3. Task filtering by action length.
4. QA generation.
5. Visual input alignment.
6. Negative-choice selection.
7. Human verification.

## Evaluation details

The uploaded paper evaluates 28 MLLMs, including GPT-4V, Gemini-Pro-Vision, SEED-X, XComposer, Video-LLaMA, LLaVA variants, Qwen-VL-Chat, and others.

A key result is that most models perform only slightly above random guessing. The uploaded version reports:

- GPT-4V: **37.98% accuracy**
- XComposer: **37.17% accuracy**
- SEED-X: **31.07% accuracy**
- Gemini-Pro-Vision: **30.46% accuracy**

The paper identifies three failure sources:

1. Insufficient integration of visual modality.
2. Missing key state changes in task progress.
3. Inadequate use of world knowledge.

## Key findings

1. Current MLLMs are weak at goal-conditioned action planning under egocentric observation.
2. Visual state tracking is a bottleneck for planning.
3. Long-horizon task progress makes planning harder.
4. Semantic similarity between goal and answer can mislead models if visual evidence is ignored.
5. Instruction tuning on EgoPlan-IT improves planning performance.

## Limitations

- Multiple-choice evaluation simplifies open-ended planning.
- It evaluates egocentric embodied planning, not web-agent planning.
- The visual domain is physical-world egocentric video, not screenshots/DOM/browser states.
- The benchmark does not evaluate extraction, provenance, or schema adherence.

## Relevance to your thesis / survey

EgoPlan-Bench is relevant because web agents also need **state-aware sequential planning**. For web extraction, an agent must know what has already been done: filters applied, pages visited, records extracted, popups closed, sorting changed, pagination state, and whether extraction is complete.

The paper supports your claim that current multimodal agents struggle when task progress, visual state, and goal-conditioned next actions must be integrated.

## How to use it in S5.1

Use EgoPlan-Bench in a paragraph on **planning benchmarks beyond web browsing**. It can support the idea that web-agent evaluation should include state-tracking and next-action correctness, not only final task completion.

## Connects to

- **S5.1:** Planning-oriented benchmarks
- **S5.2:** Multimodal perception and visual state tracking
- **S5.3:** Long-horizon planning
- **S5.5:** Failure modes: state-change blindness
- **S6:** Extraction completeness and pagination progress

## Sentence to add later

> EgoPlan-Bench demonstrates that even strong multimodal models struggle with goal-conditioned next-action prediction when they must integrate task progress, current visual state, and world knowledge, a challenge that directly parallels state-aware planning in web automation.

## Citation caution

Safe to cite strongly using the **IJCV 2026** version. If using numbers from the uploaded arXiv version, verify whether the final IJCV article changed any dataset statistics.

---

# 2.4 InfiAgent-DABench: Evaluating Agents on Data Analysis Tasks

## Venue / Status

- **Final venue:** ICML 2024.
- **Publication:** PMLR volume 235, pages 19544–19572.
- **Uploaded version:** arXiv v3, 11 Mar 2024.
- **Important version caution:** The uploaded PDF reports early validation statistics such as 257 questions and 52 CSV files. The final ICML/OpenReview/PMLR version reports a larger benchmark: 603 questions derived from 124 CSV files. Use the final ICML numbers in the final survey.

## Core idea

InfiAgent-DABench evaluates LLM-based agents on end-to-end data analysis tasks. The agent must reason over a CSV file, generate code, execute it in a Python sandbox, interpret the result, and produce a structured final answer.

The benchmark addresses a key problem: many data-analysis questions are open-ended and difficult to evaluate automatically. The authors solve this by converting questions into closed-form formats using a format-prompting technique.

## Key contribution

The paper contributes:

1. **DAEval**, a benchmark dataset for data-analysis questions over CSV files.
2. An agent framework for evaluating LLMs as data-analysis agents.
3. A closed-form answer format using special markers such as `@answer_name[value]`.
4. **DAInstruct**, an instruction-tuning dataset for data-analysis agents.
5. **DAAgent**, a specialized model/agent trained for data analysis.

## Method / approach

The benchmark construction pipeline includes:

1. Collection of real-world CSV files.
2. Generation of column descriptions and data summaries.
3. Identification of data-analysis concepts through expert interviews.
4. GPT-4 generation of open-ended questions.
5. Conversion to closed-form constraints and answer formats.
6. Label generation with OpenAI Advanced Data Analysis.
7. Human expert assessment and filtering.

The evaluation pipeline uses a ReAct-style agent that writes and executes Python code in a sandbox. A reformatting step converts model responses into the required answer format before regex/exact matching against labels.

## Evaluation details

The uploaded paper reports benchmarking of **34 LLMs** across proprietary models, open-source general LLMs, code LLMs, and agent frameworks.

Important findings from the uploaded version:

- GPT-4 achieves **78.99% accuracy** on DAEval validation.
- Qwen-72B-Chat reaches **59.92%**, close to GPT-3.5.
- DAAgent-34B reaches **64.59%**, exceeding GPT-3.5 by about **3.89%**.
- Agent frameworks such as AutoGen, XAgent, and Qwen-Agent are included.

## Key findings

1. Data-analysis tasks remain challenging even for strong LLMs.
2. Open-source models lag behind GPT-4 but are rapidly improving.
3. Instruction-tuned data-analysis agents can outperform generic models of similar size.
4. Closed-form format prompting enables scalable automatic evaluation of otherwise open-ended data-analysis questions.
5. Execution-grounded evaluation is more informative than static answer evaluation.

## Limitations

- The benchmark relies partly on GPT-4 and OpenAI ADA for dataset construction and labeling.
- Closed-form conversion improves automatic evaluation but may simplify genuine exploratory data analysis.
- It focuses on CSV/data-analysis tasks, not web navigation or web extraction.
- Some tasks are code-heavy, favoring code-writing agents.
- The uploaded version has older dataset statistics; final ICML numbers should be used.

## Relevance to your thesis / survey

This paper is very useful for your S5.1 evaluation discussion because generalized web data extraction also needs structured output evaluation. InfiAgent-DABench shows how open-ended tasks can be converted into machine-checkable outputs through constraints and closed-form answer formats.

For your thesis, this supports the need for:

- field-level evaluation,
- schema-constrained outputs,
- automatic parsing and matching,
- executable validation,
- and environment-grounded intermediate traces.

## How to use it in S5.1

Use InfiAgent-DABench as a strong example of **execution-based, structured-output agent evaluation**. It is especially useful when arguing that web extraction benchmarks should not only judge free-form answers, but should require schema-valid outputs that can be automatically checked.

## Connects to

- **S5.1:** Benchmarking and automatic evaluation
- **S5.4:** Training data and instruction tuning for agents
- **S6:** Structured data extraction and schema-constrained outputs
- **S8:** Need for extraction-specific evaluation metrics

## Sentence to add later

> InfiAgent-DABench demonstrates how open-ended data-analysis tasks can be transformed into structured, automatically checkable outputs, offering a useful methodological parallel for evaluating schema-guided web extraction agents.

## Citation caution

Safe to cite strongly as **ICML 2024**, but use the final ICML benchmark statistics rather than the older uploaded arXiv statistics.

---

# 2.5 Auto-Eval Judge: Towards a General Agentic Framework for Task Completion Evaluation

## Venue / Status

- **Current status:** arXiv 2025 preprint.
- **No peer-reviewed venue found during verification.**
- **Citation caution:** Use as a recent preprint / technical framework, not as established peer-reviewed evidence.

## Core idea

Auto-Eval Judge proposes a general-purpose modular framework for evaluating agent task completion. It argues that LLM-as-a-Judge methods often evaluate only final outputs, while agentic tasks require judging intermediate reasoning and execution traces.

The framework introduces two roles:

- **Actor:** the agent performing the task.
- **Judge:** the agent evaluating the Actor’s task completion.

## Key contribution

The main contribution is a modular **Agent-as-a-Judge** framework that decomposes task-completion evaluation into submodules:

1. **Criteria Generator:** generates binary checklist questions from the task.
2. **Artifact Content Parser:** indexes and retrieves relevant evidence from actor logs.
3. **Criteria Check Composer:** verifies each criterion using retrieved evidence and tools.
4. **Verdict Generator:** aggregates checklist results into a final yes/no task-completion verdict.

This is important because it shifts evaluation from final-output grading to process-aware verification.

## Method / approach

The framework follows a human-like evaluation process:

1. Decompose the task into explicit requirements.
2. Retrieve evidence from the actor’s logs and artifacts.
3. Verify each requirement using logical, factual, or coding checks.
4. Aggregate evidence into a final verdict.

The system uses chunking, summarization, retrieval, cross-encoders, LLM reasoning, and optionally external tools through an agentic pipeline.

## Evaluation details

The paper evaluates a Magentic-One Actor Agent on two datasets:

1. **GAIA**
2. **BigCodeBench**

Reported results from the uploaded PDF:

- On GAIA, the Judge improves alignment accuracy over GPT-4o LLM-as-a-Judge by **4.76%**.
- On BigCodeBench, it improves alignment accuracy by **10.52%**.
- The framework improves precision substantially on BigCodeBench but still has issues with recall and task-specific verification.

## Key findings

1. Process-aware judging can align better with human evaluation than final-output-only LLM judging.
2. Automatically generated checklists help make task completion explicit.
3. Evidence retrieval from logs is important but fragile.
4. A judge may need to actively solve or independently verify tasks, rather than simply trust actor logs.

## Limitations

The paper itself notes several limitations:

- It currently focuses on text-based tasks.
- It does not handle multimodal tasks or rich file attachments well.
- The Artifact Content Parser processes only a single log file.
- It may incorrectly treat planned actions as completed actions.
- Some role-playing tasks confuse checklist generation.
- Evaluation samples are relatively small.

Additional critique for your survey:

- It is a preprint, so claims need caution.
- It evaluates judging quality, not agent task performance directly.
- It does not target web navigation, web extraction, or browser-state verification.

## Relevance to your thesis / survey

Auto-Eval Judge is highly relevant to S5.1 because generalized web extraction agents need evaluation beyond final answers. For example, if an agent returns extracted records, the benchmark should verify:

- whether the agent visited the required pages,
- whether it applied the correct filters,
- whether extracted values match source evidence,
- whether pagination was exhausted,
- whether provenance links point to correct DOM/screenshot locations,
- and whether the final schema is valid.

Auto-Eval Judge supports your idea that evaluation should inspect intermediate traces and artifacts.

## How to use it in S5.1

Use it in a subsection on **agent-as-judge and process-level evaluation**. It is useful for explaining why final-output-only evaluation is insufficient for autonomous agents.

## Connects to

- **S5.1:** Agent evaluation methodology
- **S5.5:** Failure analysis and process-level debugging
- **S6:** Verification of extracted artifacts
- **S7:** Trustworthy evaluation and auditability
- **S8:** Open challenge: source-grounded verification

## Sentence to add later

> Recent agent-as-judge frameworks such as Auto-Eval Judge highlight the need to evaluate intermediate reasoning traces and execution artifacts, suggesting that future web-extraction benchmarks should verify not only final outputs but also the process by which records and provenance are obtained.

## Citation caution

Use cautiously as **arXiv 2025 preprint**. Good for current trend and framework inspiration, but not as definitive evidence.

---

# 2.6 Computer-Use Agents as Judges for Generative User Interface

## Venue / Status

- **Current status:** arXiv 2025 preprint.
- **OpenReview status:** ICLR 2026 Conference **Withdrawn Submission**.
- **Citation caution:** Do not cite as accepted ICLR. Use only as preprint / grey literature unless a later peer-reviewed version appears.

## Core idea

This paper asks whether Computer-Use Agents (CUAs) can act as judges to help code-generation models redesign GUIs. Instead of adapting agents to fixed human-designed interfaces, it explores adapting the interface itself to improve agent success.

The paper proposes a **Coder–CUA collaboration framework**:

- The **Coder** designs and revises GUIs.
- The **CUA** acts as a judge by navigating tasks and providing feedback.

## Key contribution

The paper introduces:

1. **AUI-Gym**, a benchmark for automatic GUI development.
2. **52 applications** across six domains.
3. **1,560 tasks** generated with GPT-5 and human-filtered.
4. Per-task rule-based verifiers.
5. A **Coder–CUA collaboration framework**.
6. A **CUA Dashboard** that compresses multi-step navigation histories into a single visual summary.

## Method / approach

The benchmark treats UI design as an environment-optimization problem. Given a user query requesting a single-page app, the Coder generates an HTML application. The Verifier determines whether tasks are solvable in the generated UI, and the CUA executes solvable tasks through clicks, typing, scrolling, and other actions.

Two main metrics are used:

1. **Function Completeness (FC):** whether the generated UI supports the task at all.
2. **CUA Success Rate (SR):** whether the CUA can successfully complete the task.

The framework uses two feedback signals:

- **Task Solvability Feedback:** missing features or unsupported tasks.
- **CUA Navigation Feedback:** execution trajectories and failure points.

The CUA Dashboard summarizes task outcomes, actions, intermediate states, and failure locations in one visual artifact, reportedly reducing visual redundancy by **76.2%** on average.

## Evaluation details

The uploaded PDF evaluates coders such as GPT-5, GPT-4o, and Qwen3-Coder-30B, with CUAs such as UI-TARS-1.5-7B and Operator.

Important reported findings:

- Initial UIs may appear visually acceptable but fail functional tasks.
- Task solvability feedback improves function completeness.
- CUA navigation feedback exposes interaction bottlenecks.
- Agent-oriented redesigns often simplify layouts, improve contrast, and remove unnecessary styling.
- Integrated feedback improves overall usability for agents.

## Key findings

1. Agent-native UI design is different from human-centered UI design.
2. CUA navigation success can be used as an evaluation signal for generated interfaces.
3. Task solvability and navigation success measure different things: a task may be supported but still difficult for an agent to execute.
4. Visual trajectory compression can make agent feedback more usable for iterative redesign.

## Limitations

- The paper is a withdrawn ICLR 2026 submission, so it must be treated cautiously.
- The benchmark uses generated web apps rather than real-world websites.
- GPT-5 usage makes the setup difficult to reproduce independently if model access changes.
- The task/verifier generation pipeline depends heavily on LLM-generated tests.
- It optimizes UIs for agents, which may conflict with human usability or accessibility.
- It does not evaluate web extraction, provenance, schema adherence, or information completeness.

## Relevance to your thesis / survey

This paper is relevant because it introduces the idea that GUIs can be evaluated from an agent perspective. For web automation and extraction, this is important: many websites are designed for humans, not agents. Agent failures often arise from hidden states, ambiguous controls, dynamic components, popups, animations, or visually complex layouts.

However, for your final survey, it should be used only as a P3/grey literature example because of its withdrawn status.

## How to use it in S5.1

Use it briefly in a paragraph on **agent-as-judge and GUI-specific evaluation**, with explicit caution that it is preprint/withdrawn. It can support the concept of CUA success rate and task solvability as separate evaluation dimensions.

## Connects to

- **S5.1:** GUI/task-completion evaluation
- **S5.2:** UI perception and visual grounding
- **S5.5:** Navigation failure diagnosis
- **S7:** Trust, verification, and auditability
- **S8:** Agent-native web environments and evaluation

## Sentence to add later

> Recent CUA-as-judge work further separates interface task solvability from navigation success, suggesting that web-agent benchmarks should distinguish whether a task is objectively supported by the environment from whether an agent can reliably execute it.

## Citation caution

Use only as **arXiv / withdrawn ICLR 2026 submission**. Do not present it as accepted or peer-reviewed.

---

# 3. Section-Level Synthesis for S5.1

## 3.1 What this P3 batch adds to S5.1

This batch expands S5.1 beyond standard web-agent benchmarks by showing that the broader agent-evaluation field is converging around six principles:

1. **Multi-dimensional evaluation**  
   MAgIC shows that agent capability can be decomposed into interpretable behavioral dimensions rather than a single success rate.

2. **Execution-grounded evaluation**  
   ML-Bench and InfiAgent-DABench evaluate agents inside sandboxes or execution environments, making performance depend on tool use, code execution, error recovery, and artifact correctness.

3. **State-aware planning evaluation**  
   EgoPlan-Bench shows that models fail when they must integrate goals, current observations, task progress, and world knowledge.

4. **Structured-output evaluation**  
   InfiAgent-DABench demonstrates closed-form answer formats and automatic matching, which is directly relevant to schema-guided extraction evaluation.

5. **Process-level / agent-as-judge evaluation**  
   Auto-Eval Judge argues that final outputs alone are insufficient; intermediate logs and artifacts should be evaluated.

6. **GUI/task-solvability separation**  
   CUA-as-Judge separates whether a UI supports a task from whether a CUA can execute it, which maps well to the distinction between website affordance and agent capability.

## 3.2 How these papers support your central thesis gap

Your survey’s central gap is:

> Current web-agent benchmarks do not fully evaluate generalized, schema-guided, source-verifiable web data extraction across arbitrary websites.

This P3 batch supports that claim indirectly:

- MAgIC shows that agents require decomposed behavioral evaluation.
- ML-Bench shows that complex environments require end-to-end sandboxed evaluation.
- EgoPlan-Bench shows that task progress and visual state tracking remain difficult.
- InfiAgent-DABench shows that structured outputs can make open-ended tasks automatically evaluable.
- Auto-Eval Judge shows the need to inspect process traces and artifacts.
- CUA-as-Judge shows that environment support and agent navigation success must be separated.

Together, they strengthen your argument that web-agent evaluation should include:

- final task success,
- process correctness,
- state tracking,
- environment interaction,
- structured output validity,
- provenance verification,
- and failure diagnosis.

## 3.3 What this batch does NOT solve

None of these papers fully evaluates generalized web extraction.

Missing dimensions remain:

| Missing dimension | Why still missing |
|---|---|
| Field-level extraction F1 | These benchmarks do not evaluate extracted records/fields from arbitrary websites. |
| Schema adherence | Only InfiAgent-DABench gives structured outputs, but not web schemas. |
| Provenance accuracy | None verifies every extracted value against DOM/screenshot evidence. |
| Pagination completeness | None evaluates whether all records across pages were extracted. |
| Cross-site generalization | ML-Bench has repo variation; not website/schema variation. |
| Live web volatility | These benchmarks are mostly static or controlled. |
| Extraction safety | None focuses on prompt injection or malicious content inside extracted fields. |
| Cost per correct extracted row | None reports extraction-specific economic efficiency. |

## 3.4 Suggested paragraph for S5.1

> Broader agent-evaluation benchmarks reinforce the need to move beyond final-answer accuracy. MAgIC decomposes multi-agent performance into behavioral dimensions such as judgment, reasoning, cooperation, coordination, and rationality; ML-Bench and InfiAgent-DABench evaluate agents in execution environments where success depends on code generation, tool use, and iterative error recovery; EgoPlan-Bench highlights the difficulty of state-aware planning from multimodal observations; and recent agent-as-judge frameworks evaluate intermediate traces and artifacts rather than only final outputs. However, these benchmarks remain adjacent rather than sufficient for generalized web data extraction: they do not jointly measure schema adherence, field-level correctness, provenance accuracy, pagination completeness, source-grounded verification, and cost per correct extracted record.

---

# 4. Tools, Frameworks, and Evaluation Ecosystem Examples from This Batch

| Category | Examples from papers | How to use in your review |
|---|---|---|
| Multi-agent evaluation | MAgIC, PGM-aware agents | Use as examples of decomposed behavioral metrics. |
| Repository/code-agent evaluation | ML-Bench, ML-Agent-Bench, ML-LLM-Bench | Use as examples of sandboxed, end-to-end execution benchmarks. |
| Agent frameworks | OpenDevin, SWE-Agent, AutoGen, Aider | Mention as evaluation targets / frameworks in software-agent benchmarks. |
| Data-analysis agents | InfiAgent, DAAgent, Qwen-Agent, XAgent, OpenAI ADA, TaskWeaver, Open Interpreter | Use as examples of execution-grounded data-analysis agents. |
| Multimodal planning | EgoPlan-Bench, EgoPlan-IT | Use as examples of state-aware planning evaluation. |
| Agent-as-judge | Auto-Eval Judge, Magentic-One Actor/Judge setup | Use in process-level evaluation discussion. |
| GUI/CUA evaluation | AUI-Gym, CUA Dashboard, UI-TARS, Operator | Use cautiously as grey literature for GUI task-solvability and CUA success rate. |
| Automatic verification | Closed-form labels, regex matching, task-specific rule checkers, checklist criteria | Use to motivate automated verification for web extraction outputs. |

---

# 5. Recommended Inclusion Decision

| Paper | Include in final survey? | Recommended role |
|---|---|---|
| MAgIC | Yes, briefly | Support broader trend toward decomposed agent metrics. |
| ML-Bench | Yes, briefly | Support end-to-end execution and sandbox evaluation. |
| EgoPlan-Bench | Yes | Support planning/state-tracking limitations in multimodal agents. |
| InfiAgent-DABench | Yes | Strong methodological support for structured/closed-form agent evaluation. |
| Auto-Eval Judge | Maybe | Use only if discussing agent-as-judge/process evaluation. Mark as preprint. |
| CUA as Judges for Generative UI | Maybe / footnote | Use only as recent grey literature; mention withdrawn status internally, avoid relying on it heavily. |

## Strongest papers for final S5.1

1. **InfiAgent-DABench** — because it directly connects to structured, automatically checkable task outputs.
2. **ML-Bench** — because it emphasizes end-to-end interactive execution.
3. **EgoPlan-Bench** — because it supports state-aware multimodal planning limitations.
4. **MAgIC** — good for multi-dimensional agent evaluation.

## Papers to use cautiously

1. **Auto-Eval Judge** — useful but preprint.
2. **Computer-Use Agents as Judges for Generative UI** — interesting but withdrawn from ICLR 2026; use only as grey literature if needed.

---

# 6. Ready-to-Add Sentences by Theme

## Theme: Final success is not enough

> Recent agent benchmarks increasingly move beyond aggregate success rates: MAgIC decomposes multi-agent behavior into judgment, reasoning, cooperation, coordination, and rationality, while process-oriented judge frameworks inspect intermediate logs and artifacts rather than only final outputs.

## Theme: Execution-grounded evaluation

> ML-Bench and InfiAgent-DABench show that realistic agent evaluation often requires sandboxed interaction, code execution, environment feedback, and artifact verification, rather than static prompt-response scoring.

## Theme: Structured output evaluation

> InfiAgent-DABench is particularly relevant for extraction-oriented evaluation because it converts open-ended data-analysis tasks into structured, machine-checkable answer formats, suggesting a similar path for schema-guided web extraction benchmarks.

## Theme: State-aware planning

> EgoPlan-Bench demonstrates that models still struggle to integrate task goals, task progress, current observations, and world knowledge, a capability that is also essential for robust multi-step web automation.

## Theme: Agent-as-judge

> Agent-as-judge frameworks suggest that future web-agent benchmarks should verify the process by which an answer is produced, including page visits, actions, intermediate observations, and final artifacts.

## Theme: GUI task solvability

> CUA-as-judge work separates task solvability from navigation success, a distinction that can help web-agent benchmarks identify whether failures arise from missing website affordances, poor perception, or weak planning.

---

# 7. Direct Integration into Your Survey Argument

For S5.1, this batch should not dominate the subsection. Use it as **supporting context** after discussing core web-agent benchmarks such as WebArena, Mind2Web, VisualWebArena, BrowserGym, WorkArena, WebVoyager, and extraction-specific benchmarks.

Recommended placement:

1. First discuss core web-agent benchmarks.
2. Then discuss extraction-specific benchmark gaps.
3. Then add a paragraph: “Adjacent agent-evaluation benchmarks reinforce this limitation...”
4. Cite MAgIC, ML-Bench, EgoPlan-Bench, InfiAgent-DABench, and optionally Auto-Eval Judge.
5. Conclude that no current benchmark jointly measures generalized web extraction.

## Suggested final transition sentence

> These adjacent benchmarks provide useful design patterns—decomposed metrics, sandboxed execution, structured outputs, and process-aware judging—but they also make the missing benchmark for generalized web data extraction more visible: no existing evaluation combines live web interaction, schema-guided extraction, source-level provenance, pagination completeness, robustness, and cost-aware success.

---

# 8. Final Notes for Later Filtering

Keep these P3 papers in your research archive. In the final ACM Computing Surveys version, do not over-cite all of them in the main text. Use only the strongest 3–4 depending on space:

- **Include:** InfiAgent-DABench, ML-Bench, EgoPlan-Bench.
- **Briefly include:** MAgIC.
- **Optional / footnote:** Auto-Eval Judge.
- **Very cautious / grey literature:** CUA-as-Judge because of withdrawn OpenReview status.

