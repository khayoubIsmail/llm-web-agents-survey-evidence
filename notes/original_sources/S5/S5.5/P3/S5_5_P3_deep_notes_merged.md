# S5.5 P3 Deep Notes — Generalization, Failure Modes, and Failure Verification in LLM Agents

**Section:** S5.5 — Generalization / Failure Modes / Reliability Gaps  
**Priority:** P3 supporting papers  
**Batch size:** 4 papers  
**Purpose:** Build a deep archive of supporting evidence for the thesis/survey argument that LLM-based agents remain fragile under dynamic rules, long-horizon interaction, hidden state changes, multi-agent dependencies, and silent trajectory-level failures.

---

## 0. Executive Synthesis

The S5.5 P3 papers are highly relevant even if not all should be cited heavily in the final survey. Together, they strengthen the claim that current LLM agents fail not only because of low-level perception or weak planning, but because they lack robust **generalization under changing rules**, **epistemic agency**, **interpretable failure localization**, and **trajectory-level anomaly detection**.

The four papers cover complementary failure dimensions:

| Failure dimension | Main supporting paper | Why it matters for your review |
|---|---|---|
| Rule manipulation and compositional generalization | Baba Is AI | Shows that multimodal LLMs fail when the environment requires changing and composing rules, not merely following static instructions. |
| Epistemic agency and meta-reflection | Reflection-Bench | Formalizes agent reliability as cognitive capacities: prediction, decision-making, perception, memory, counterfactual thinking, belief updating, and meta-reflection. |
| Interpretable agent failure verification | VeriLA | Provides a human-centered framework for detecting which sub-agent failed and why, using criteria, uncertainty, and plan structure. |
| Silent multi-agent trajectory failures | Detecting Silent Failures in Multi-Agentic AI Trajectories | Introduces drift, cycles, missing details, tool failures, and context-propagation failures as detectable anomalies in agent traces. |

**Core conclusion for S5.5:**

> Current LLM-based agents should not be evaluated only by final task success. Their failures often arise from hidden weaknesses in rule grounding, belief updating, reflection, context propagation, and multi-step trajectory control. Therefore, future web-agent evaluation must include failure localization, trace-level anomaly detection, uncertainty-aware verification, and stress tests for compositional generalization.

---

## 1. Venue / Status Verification Summary

| Paper | Year | Venue / Status | Citation strength | Recommended use |
|---|---:|---|---|---|
| Baba Is AI: Break the Rules to Beat the Benchmark | 2024 / arXiv v2 2025 | ICML 2024, PMLR 235 according to the uploaded PDF; arXiv version also available | Strong if citing ICML/PMLR version | Use as evidence for rule-based compositional generalization failure. |
| Reflection-Bench: Evaluating Epistemic Agency in Large Language Models | 2025 | ICML 2025, PMLR 267 | Strong | Use as a central supporting reference for epistemic-agency failure modes. |
| VeriLA: A Human-Centered Evaluation Framework for Interpretable Verification of LLM Agent Failures | 2025 | arXiv 2025; listed by Megagon and author page as accepted/presented at HEAL@CHI 2025 workshop | Moderate | Use as workshop / human-centered evaluation evidence, not as a main benchmark pillar. |
| Detecting Silent Failures in Multi-Agentic AI Trajectories | 2025 | arXiv 2025 / CoRR; no confirmed peer-reviewed venue found | Cautious | Use as recent preprint evidence for trace-level silent-failure detection. |

**Citation caution:** Reflection-Bench and Baba Is AI are safest as peer-reviewed references. VeriLA is useful but should be labelled as workshop/position-style or preprint/workshop evidence. Detecting Silent Failures should be cited cautiously as a recent arXiv preprint.

---

## 2. Section-Level Critique for S5.5

### 2.1 What these P3 papers add

These papers help S5.5 move beyond a generic statement like “agents fail to generalize.” They let you build a sharper taxonomy of failure modes:

1. **Environmental rule failure:** agents misunderstand which rules are active, whether rules can be modified, and how rule changes affect the world.
2. **Compositional generalization failure:** agents learn individual patterns but fail to combine them into new action sequences.
3. **Epistemic failure:** agents do not reliably predict, update beliefs, remember feedback, or reflect on their own cognitive process.
4. **Verification failure:** systems often lack an interpretable mechanism to identify which component caused the error.
5. **Silent trajectory failure:** the final output may look valid while the internal path has drifted, looped, omitted details, or propagated wrong context.

### 2.2 How this connects to LLM-based web automation and extraction

For generalized web automation and web data extraction, these failures are critical:

- Websites are **dynamic rule environments**: workflows, forms, login states, filters, permissions, pagination, and session rules change across pages.
- Web extraction often requires **compositional generalization**: combining navigation, filtering, scrolling, schema grounding, entity disambiguation, and extraction into one robust workflow.
- Data extraction agents need **epistemic agency**: they must know when the page state changed, when evidence is missing, when extracted content is uncertain, and when to verify against source evidence.
- Multi-agent extraction pipelines need **failure attribution**: if extraction is wrong, the system must know whether the failure came from perception, planning, tool use, schema mapping, context propagation, or final synthesis.
- Silent failures are especially dangerous in extraction: an agent can return plausible structured JSON while missing fields, using stale page state, hallucinating values, or losing provenance.

### 2.3 Recommended S5.5 subsection structure

```text
S5.5 Generalization and Failure Modes
  S5.5.1 Failure under distractors, changing rules, and compositional environments
  S5.5.2 Epistemic agency: prediction, memory, belief updating, and meta-reflection
  S5.5.3 Error propagation and failure localization in multi-agent systems
  S5.5.4 Silent failures in agent trajectories
  S5.5.5 Implications for generalized web automation and data extraction
```

---

# 3. Deep Paper Notes

---

# 3.1 Baba Is AI: Break the Rules to Beat the Benchmark

## Venue / Status

- **Title:** Baba Is AI: Break the Rules to Beat the Benchmark
- **Authors:** Nathan Cloos, Meagan Jens, Michelangelo Naim, Yen-Ling Kuo, Ignacio Cases, Andrei Barbu, Christopher J. Cueva
- **Year:** 2024; arXiv v2 updated 2025
- **Venue/status:** ICML 2024 / PMLR 235 according to uploaded PDF; arXiv version also available.
- **Status label:** Peer-reviewed conference paper + arXiv version.
- **Citation caution:** Prefer the ICML/PMLR version. The arXiv page should be used only as access link unless the final BibTeX confirms PMLR metadata.

## Core idea

The paper introduces **Baba Is AI**, a benchmark based on the puzzle game *Baba Is You*. The key idea is to test whether multimodal LLM agents can solve environments where rules are not fixed background constraints but manipulable objects. The agent must understand objects, textual rule blocks, active/inactive rules, and how rearranging rule blocks changes what is possible in the environment.

Unlike many planning benchmarks where the rules of the environment are static, Baba Is AI asks agents to reason about environments in which success may require **making rules**, **breaking rules**, and composing these operations with navigation.

## Problem addressed

Many LLM-agent benchmarks test whether a model can follow instructions, select tools, or plan in a fixed task environment. This paper targets a deeper failure mode: can an agent generalize when the structure of the environment itself can be modified?

This is important because real agentic systems often operate in environments whose rules are implicit, stateful, and modifiable. In web automation, for example, clicking a filter, changing a form value, accepting a cookie banner, or logging in can change available actions and page semantics.

## Method / approach

The benchmark is a simplified gridworld version of *Baba Is You*. Objects such as baba, wall, key, door, and ball coexist with rule blocks such as `is`, `win`, `you`, and `stop`. A rule becomes active when blocks form a horizontal pattern such as:

```text
object is property
```

The model receives visual input of the gridworld and must generate a high-level plan using primitives such as:

```text
goto[object]
make[object is property]
break[object is property]
```

The benchmark tests several conditions:

- no distractor
- object distractor
- rule distractor
- object + rule distractor
- win-rule distractor
- two-room environments with additional wall/rule distractors
- compositional rule manipulation requiring combinations such as `break + make + goto`

The evaluated models include GPT-4o, Gemini-1.5-Pro, and Gemini-1.5-Flash.

## Key findings

The results show that models can succeed in simpler settings but degrade under distractors and fail strongly when they must compose rule manipulations.

Important observed failure patterns:

1. **Distractor sensitivity:** models are confused by irrelevant objects or irrelevant active rules.
2. **Poor rule grounding:** models sometimes attend to rules that do not actually apply to existing objects.
3. **Compositional weakness:** models fail when combining previously seen strategies into a new rule-manipulation plan.
4. **Path-planning errors:** models hallucinate blocked paths or misunderstand object positions.
5. **Grounding mistakes:** models refer to objects that are not present in the environment.

## Why this matters for S5.5

This paper is useful because it gives a concrete, visual, agentic demonstration of **generalization failure under changing rules**. For S5.5, it supports the claim that LLM agents cannot be assumed to generalize simply because they succeed in static or template-like environments.

The strongest contribution for your survey is not the benchmark itself, but the type of failure it reveals:

> LLM agents often learn surface-level patterns and fail when success requires restructuring the environment’s rules.

## Relevance to web automation and extraction

Baba Is AI is not a web benchmark, but the failure mode transfers strongly to web agents. A web page is a dynamic rule system:

- clicking one element changes available controls;
- forms encode hidden validation rules;
- pagination changes the visible dataset;
- filters change the extraction target;
- login/session state changes access;
- UI components can become enabled/disabled;
- JavaScript state can change without visible URL changes.

An extraction agent must not only “see” a page; it must understand the current state and how actions transform that state. Baba Is AI provides evidence that multimodal LLMs can fail when rule manipulation and compositional state transitions are required.

## Limitation

The benchmark is a simplified game environment, not a realistic browser or web automation environment. Its rule system is explicit and symbolic, whereas web rules are often implicit, distributed across DOM state, JavaScript behavior, network requests, and user permissions. Therefore, the paper should be used as **evidence for the type of generalization failure**, not as direct evidence that web agents fail in the same quantitative way.

## How to use it in the literature review

Use it in S5.5.1 as a supporting example after discussing broader web-agent generalization gaps:

> Benchmarks such as Baba Is AI show that even strong multimodal models can fail when generalization requires manipulating and composing environmental rules, suggesting that web agents must be evaluated under dynamic state changes rather than only static navigation tasks.

## Connects to

| Connects to | Reason |
|---|---|
| S5.2 Web perception and representation | Visual grounding and object/rule recognition are prerequisites. |
| S5.3 Planning and reasoning | Rule manipulation requires multi-step planning under changing state. |
| S5.5 Generalization and failure modes | Main use: compositional generalization failure. |
| S7 Security and robustness | Rule confusion can be exploited by adversarial UI or prompt injection. |
| S8 Open challenges | Need dynamic, stateful, compositional evaluation. |

## Sentence to add later

> Baba Is AI further illustrates that agent generalization remains brittle when success requires manipulating and composing environmental rules, a failure mode that directly parallels dynamic web interfaces where actions alter page state, available controls, and extraction conditions.

## Citation caution

Use as peer-reviewed evidence if citing the ICML/PMLR version. If your bibliography only has the arXiv metadata, annotate carefully and later replace with final PMLR BibTeX.

---

# 3.2 Reflection-Bench: Evaluating Epistemic Agency in Large Language Models

## Venue / Status

- **Title:** Reflection-Bench: Evaluating Epistemic Agency in Large Language Models
- **Authors:** Lingyu Li, Yixu Wang, Haiquan Zhao, Shuqi Kong, Yan Teng, Chunbo Li, Yingchun Wang
- **Year:** 2025
- **Venue/status:** ICML 2025, Proceedings of Machine Learning Research, Volume 267, pages 36236–36264.
- **Status label:** Peer-reviewed conference paper.
- **Citation caution:** Safe to cite strongly. Use the PMLR version.

## Core idea

Reflection-Bench evaluates whether LLMs possess **epistemic agency**, defined as the ability to construct, adapt, and monitor beliefs about dynamic environments. Instead of treating agent failure only as failed task completion, the paper decomposes agency into cognitive functions needed for reliable interaction.

The benchmark uses cognitive-psychology-inspired tasks to test seven dimensions:

1. prediction
2. decision-making
3. perception
4. memory
5. counterfactual thinking
6. belief updating
7. meta-reflection

## Problem addressed

Most LLM-agent benchmarks evaluate external performance: whether the agent completes a task. Reflection-Bench targets a deeper question: whether the base model has the internal cognitive capacities required to serve as a reliable agent core.

This is important because web agents depend on more than language generation. They must predict page transitions, update beliefs after actions, remember previous states, reason counterfactually after errors, and reflect on whether the current strategy is working.

## Method / approach

Reflection-Bench adapts seven cognitive-psychology paradigms:

| Dimension | Task used | What it tests |
|---|---|---|
| Prediction | Weather Prediction Task | Learning transition probabilities from feedback. |
| Decision-making | Wisconsin Card Sorting Test | Inferring and adapting to changing latent rules. |
| Perception | Oddball paradigm | Detecting contextual anomalies. |
| Memory | N-back | Maintaining and comparing information across steps. |
| Counterfactual thinking | Double-choice Iowa Gambling Task | Revising decisions after feedback. |
| Belief updating | Probabilistic Reversal Learning Task | Updating beliefs when reward probabilities reverse. |
| Meta-reflection | Meta-bandit task | Identifying higher-order patterns across changes. |

The benchmark evaluates 16 LLMs under multiple prompting strategies, including direct generation, free output, and zero-shot Chain-of-Thought.

## Key findings

Reflection-Bench finds that current LLMs show early signs of epistemic agency but remain limited, especially in prediction, decision-making, and meta-reflection.

Important findings:

1. **Three-tier performance hierarchy:** top models perform better but still fail in important cognitive dimensions.
2. **Meta-reflection is especially weak:** no model reliably recognizes even simple reversal patterns in the meta-bandit task.
3. **Local adaptation dominates:** models often rely on short-sighted strategies such as win-stay-lose-switch rather than learning global structure.
4. **Prompting effects are task-dependent:** CoT helps some tasks but can harm others, implying that fixed prompting strategies are insufficient.
5. **Parameterized design reduces contamination risk:** the benchmark can vary parameters to avoid memorization.

## Why this matters for S5.5

This paper gives S5.5 a strong conceptual foundation. Instead of merely listing failure cases, you can frame failure modes as weaknesses in epistemic agency.

This is especially useful for an ACM Computing Surveys-style paper because it offers a higher-level taxonomy:

- perception failure
- memory failure
- prediction failure
- decision failure
- belief-update failure
- counterfactual failure
- meta-reflection failure

This makes your review more intellectually structured than a simple benchmark inventory.

## Relevance to web automation and extraction

Web extraction agents need epistemic agency at every stage:

- **Prediction:** What will happen if I click this button, submit this form, or scroll?
- **Decision-making:** Which action is best under the current page state?
- **Perception:** Did the page change? Did new content load? Is this an error page?
- **Memory:** What filters have been applied? Which records were already extracted?
- **Counterfactual thinking:** If extraction failed, which prior action caused the failure?
- **Belief updating:** Does the agent update its understanding when the page behaves differently than expected?
- **Meta-reflection:** Does the agent recognize repeated failure patterns and revise its strategy?

For generalized schema-guided web extraction, these abilities are central because the agent must operate across heterogeneous sites where layouts, interaction rules, and data schemas vary.

## Limitation

Reflection-Bench evaluates base-model-level cognitive abilities through controlled psychological tasks. It does not directly evaluate full browser agents, tool-integrated systems, DOM perception, or web extraction pipelines. Therefore, it should be used as a conceptual and diagnostic framework, not as direct web-agent performance evidence.

## How to use it in the literature review

Use it in S5.5.2 to define epistemic agency as a deeper reliability requirement:

> Reflection-Bench reframes agent reliability as epistemic agency, decomposing robust interaction into prediction, decision-making, perception, memory, counterfactual reasoning, belief updating, and meta-reflection.

Then connect it to web agents:

> These dimensions map naturally to web automation, where agents must predict page-state transitions, perceive dynamic UI changes, update beliefs after failed actions, and reflect on repeated extraction errors.

## Connects to

| Connects to | Reason |
|---|---|
| S3 Agent architectures | Epistemic agency can be supported by memory, reflection, and planning modules. |
| S5.3 Planning and reasoning | Prediction and decision-making are planning prerequisites. |
| S5.5 Generalization/failure modes | Main use: cognitive taxonomy of failure. |
| S6 Web data extraction | Extraction needs belief updating and source verification. |
| S8 Open challenges | Need benchmarks that test epistemic agency in realistic web environments. |

## Sentence to add later

> Reflection-Bench suggests that robust web agents require epistemic agency: the ability to predict state transitions, update beliefs from feedback, remember prior interactions, reason counterfactually about failures, and meta-reflect on repeated errors.

## Citation caution

Safe to cite strongly as an ICML 2025 / PMLR paper. It should not replace web-agent benchmarks, but it can provide a strong theoretical lens for the failure-mode subsection.

---

# 3.3 VeriLA: A Human-Centered Evaluation Framework for Interpretable Verification of LLM Agent Failures

## Venue / Status

- **Title:** VeriLA: A Human-Centered Evaluation Framework for Interpretable Verification of LLM Agent Failures
- **Authors:** Yoo Yeon Sung, Hannah Kim, Dan Zhang
- **Year:** 2025
- **Venue/status:** arXiv 2025; listed by Megagon Labs and author page as accepted/presented at HEAL@CHI 2025 workshop.
- **Status label:** Workshop / arXiv preprint.
- **Citation caution:** Useful for supporting discussion on human-centered failure verification, but do not treat it as a major peer-reviewed benchmark unless you cite the workshop status explicitly.

## Core idea

VeriLA proposes a human-centered framework for verifying failures in compound LLM-agent systems. It focuses on making agent failures interpretable and reducing manual inspection cost by evaluating each agent’s execution output against human-defined criteria, uncertainty features, and dependency structure in the plan.

The central idea is that failures in multi-agent systems should be localized at the sub-agent level, not only judged by final-answer correctness.

## Problem addressed

Compound AI systems decompose tasks into subtasks assigned to specialized agents. If one agent fails, the error can propagate downstream and compromise the final output. However, manual debugging is difficult because:

- intermediate reasoning is opaque;
- agent outputs may not align with human expectations;
- dependencies between agents make root-cause analysis hard;
- checking every intermediate output is costly;
- final failure may not reveal which agent caused the issue.

## Method / approach

VeriLA has three main stages:

1. **Planning:** A planning agent decomposes a task into subtasks using a human-designed agent registry and generates a DAG-style plan.
2. **Agent execution:** Specialized LLM agents execute each subtask.
3. **Execution verification:** Agent-specific verifiers evaluate each output using features from human-defined criteria, uncertainty estimates, and plan-structure information.

The framework uses:

- human-designed agent registry;
- human-defined agent criteria;
- external LLM judge scores;
- verbalized confidence;
- logit-based confidence;
- self-consistency features;
- subtask type;
- plan graph features such as dependency structure;
- aggregation metrics to estimate overall task failure.

The case study focuses on mathematical reasoning tasks from GSM8K and BIG-Bench Hard subsets.

## Key findings

The case study suggests that VeriLA can detect agent execution failures with strong accuracy across several math reasoning datasets. The paper reports that criteria-based features are especially important, showing that human-defined evaluation criteria contribute substantially to verifier performance.

Important insights:

1. **Agent-level verification is useful:** evaluating subtasks helps identify where failure occurs.
2. **Human-defined criteria matter:** task-specific criteria align verification with human expectations.
3. **Uncertainty features are informative but not sufficient alone.**
4. **Plan structure matters:** dependencies help explain how failures propagate.
5. **Aggregation metrics help prioritize likely failing tasks.**

## Why this matters for S5.5

VeriLA supports the argument that agent evaluation should be **interpretable and localized**. For S5.5, it provides a framework for discussing failure not only as a model-level phenomenon but as a system-level phenomenon involving planning, execution, dependencies, and human-aligned validation.

This is useful because web extraction agents may use multiple components:

- browser controller;
- DOM parser;
- visual perception module;
- planner;
- schema mapper;
- extraction verifier;
- provenance checker;
- final JSON generator.

If the final output is wrong, the system needs to know which component failed.

## Relevance to web automation and extraction

For generalized web data extraction, a VeriLA-like framework could verify subtasks such as:

| Web extraction subtask | Possible verifier criteria |
|---|---|
| Locate target records | Correct page area, complete list, no irrelevant region. |
| Click/filter/search | Correct control, correct query, expected state change. |
| Extract fields | Completeness, schema alignment, value correctness. |
| Map fields to schema | Correct entity-field pairing, no hallucinated attributes. |
| Preserve provenance | Each extracted value linked to source evidence. |
| Final structured output | Valid JSON, no missing required fields, no unsupported values. |

This paper can help you argue that web-agent evaluation should include **subtask-level verifiers**, not only end-to-end exact match.

## Limitation

VeriLA is evaluated on structured mathematical reasoning tasks, not browser automation or web data extraction. The approach depends on predefined agent registries and human-designed criteria, which may be harder to scale to open-world web tasks. It also relies partly on LLM-based evaluation, which can inherit judge bias and calibration problems.

## How to use it in the literature review

Use it in S5.5.3 as evidence for interpretable failure localization:

> VeriLA demonstrates that compound LLM-agent failures can be analyzed by verifying individual agent outputs against human-defined criteria, uncertainty signals, and plan-structure features.

Then connect to web extraction:

> This perspective is particularly relevant to web extraction, where wrong outputs may originate from perception, navigation, schema mapping, context propagation, or final formatting rather than from a single model error.

## Connects to

| Connects to | Reason |
|---|---|
| S3 Multi-agent architectures | VeriLA targets compound systems with planning and specialized agents. |
| S5.1 Evaluation | Adds human-centered verification beyond final accuracy. |
| S5.5 Failure modes | Main use: interpretable failure verification. |
| S6 Web data extraction | Helps design field-level and provenance-level verification. |
| S7 Robustness | Failure localization supports safer and more auditable systems. |

## Sentence to add later

> Human-centered verification frameworks such as VeriLA show that agent failures can be localized by combining human-defined criteria, uncertainty estimates, and plan-structure features, a direction that is especially important for web extraction pipelines where errors propagate across perception, navigation, and schema-mapping stages.

## Citation caution

Cite as HEAL@CHI 2025 workshop / arXiv preprint. Use cautiously and mainly as a recent framework example.

---

# 3.4 Detecting Silent Failures in Multi-Agentic AI Trajectories

## Venue / Status

- **Title:** Detecting Silent Failures in Multi-Agentic AI Trajectories
- **Authors:** Divya Pathak, Harshit Kumar, Anuska Roy, Felix George, Mudit Verma, Pratibha Moogi
- **Year:** 2025
- **Venue/status:** arXiv 2025 / CoRR; no confirmed peer-reviewed venue found.
- **Status label:** arXiv preprint.
- **Citation caution:** Very relevant to S5.5, but cite cautiously as recent preprint evidence.

## Core idea

The paper introduces the problem of detecting **silent failures** in multi-agent AI trajectories. Silent failures are failures that do not produce explicit errors but still indicate that the system deviated from intended behavior.

The paper focuses on anomaly detection over agent traces, using features extracted from execution trajectories.

## Problem addressed

Multi-agent LLM systems are non-deterministic. The same input can produce different trajectories depending on:

- model variation;
- system prompt quality;
- stochastic reasoning;
- tool invocation choices;
- user prompt variation;
- agent orchestration behavior.

Because of this, failures may not appear as obvious exceptions. Instead, agents may drift, loop, omit requested information, or propagate wrong context while still returning a plausible final response.

## Failure types defined

The paper identifies several silent failure categories:

| Failure type | Meaning |
|---|---|
| Drift | The agent diverges from intended path and selects irrelevant tools or agents. |
| Cycles | The agent repeatedly invokes itself, another agent, or a tool in redundant loops. |
| Missing details | Final output omits crucial requested information. |
| Tool failures | External tools fail silently, return unexpected results, or hit limits. |
| Context propagation failures | Incorrect or incomplete context is passed to dependent agents/tools. |

These categories are directly relevant to web automation and extraction.

## Method / approach

The paper presents a dataset curation pipeline for anomaly detection in agentic trajectories:

1. Collect agentic traces using OpenTelemetry-style distributed tracing.
2. Vary input queries, system prompts, and LLM models to capture non-determinism.
3. Extract features from traces.
4. Label trajectories as normal or anomalous.
5. Benchmark supervised, semi-supervised, and unsupervised anomaly detection models.

Feature categories include:

- token features;
- latency features;
- path features;
- prompt/context features;
- model features.

The paper constructs two datasets:

- Stock Market Analysis Assistant: 4,275 traces.
- Research and Writing Assistant: 894 traces.

It evaluates methods such as XGBoost, Random Forest, Logistic Regression, SVM, Naive Bayes, SVDD, Isolation Forest, and K-Means.

## Key findings

The paper reports strong results for supervised and semi-supervised methods:

- XGBoost achieves high accuracy, up to about 98% on the stock-market dataset.
- SVDD performs competitively in the semi-supervised setting, up to about 96% accuracy.
- Path-level features such as tool count, total steps, unique steps, and agent count are highly important.
- Subtle drift remains difficult to detect because such failures can resemble normal trajectories.

## Why this matters for S5.5

This paper is very relevant because it shifts failure analysis from final output to **trajectory analysis**. For web agents, this is essential. A final answer can look correct while the trajectory contains hidden errors, such as:

- clicked wrong element but recovered accidentally;
- skipped pagination;
- extracted from stale page state;
- called irrelevant tools;
- entered a loop;
- missed a required field;
- passed wrong context from navigation module to extraction module;
- returned valid JSON with unsupported values.

This supports your survey argument that generalized web extraction needs observability and trace-level evaluation.

## Relevance to web automation and extraction

In web automation, silent failures are common:

| Web-agent silent failure | Example |
|---|---|
| Drift | Agent navigates to product reviews instead of product specifications. |
| Cycle | Agent repeatedly scrolls or reopens the same filter panel. |
| Missing details | Extracts product name and price but omits availability or seller. |
| Tool failure | Browser action returns no error but click did not trigger expected state change. |
| Context propagation failure | Schema mapper receives stale DOM content from the previous page. |

For web data extraction, this is especially important because users often care about structured outputs, not the path. Without trace-level detection, a system may silently return incomplete or unverifiable data.

## Limitation

The paper is a recent arXiv preprint and the datasets are from two specific multi-agent applications, not browser agents. The anomaly labels depend on expected trajectories, which may be hard to define in open-ended web environments where multiple valid paths exist. The detection models rely on engineered features; more semantic or causal failure detection may be needed for robust web-agent evaluation.

## How to use it in the literature review

Use it in S5.5.4 as evidence for trace-level failure detection:

> Recent work on silent failures frames multi-agent reliability as an anomaly-detection problem over agent trajectories, identifying drift, cycles, missing details, tool failures, and context-propagation failures as failure modes that may not be visible from final outputs alone.

Then connect to your thesis:

> For generalized web extraction, this suggests that evaluation should log and verify not only extracted values, but also the navigation and interaction trajectory that produced them.

## Connects to

| Connects to | Reason |
|---|---|
| S5.1 Evaluation | Adds trajectory-level evaluation beyond final metrics. |
| S5.5 Failure modes | Main use: silent failures and anomaly detection. |
| S6 Web data extraction | Missing details and stale context are extraction-critical. |
| S7 Security and robustness | Trace anomaly detection can detect malicious or unsafe deviations. |
| S8 Open challenges | Need observability and failure-detection benchmarks for web agents. |

## Sentence to add later

> Silent-failure studies show that multi-agent systems can drift, loop, omit requested details, or propagate stale context without producing explicit errors, implying that web extraction benchmarks should evaluate interaction traces and provenance rather than final structured outputs alone.

## Citation caution

Use as a recent preprint. Good for open-challenges and future-work discussion, but do not make it a central peer-reviewed benchmark reference until venue status is confirmed.

---

# 4. Integrated Failure-Mode Taxonomy for S5.5

This batch supports the following taxonomy for your S5.5 section:

| Failure class | Definition | Evidence from P3 papers | Web extraction implication |
|---|---|---|---|
| Rule-state failure | Agent misinterprets active/inactive rules or state-changing actions. | Baba Is AI | Browser state, filters, forms, sessions, modals. |
| Distractor failure | Agent attends to irrelevant objects/rules/context. | Baba Is AI | Ads, sidebars, duplicated DOM nodes, hidden elements. |
| Compositional generalization failure | Agent fails to combine known primitives in new situations. | Baba Is AI | Novel site workflows requiring unseen action combinations. |
| Prediction failure | Agent fails to anticipate environmental transitions. | Reflection-Bench | Wrong expectation after click, scroll, submit, filter. |
| Memory failure | Agent fails to retain previous interaction state. | Reflection-Bench | Lost pagination state, repeated extraction, missed records. |
| Belief-updating failure | Agent fails to revise assumptions after feedback. | Reflection-Bench | Continues wrong strategy after page behavior changes. |
| Meta-reflection failure | Agent cannot detect repeated failure patterns. | Reflection-Bench | Repeats failed navigation/extraction strategy. |
| Execution-localization failure | System cannot identify which sub-agent failed. | VeriLA | Hard to debug perception vs planning vs extraction errors. |
| Error-propagation failure | One bad subtask contaminates downstream outputs. | VeriLA | Wrong DOM region leads to wrong schema mapping and final JSON. |
| Silent trajectory failure | Agent trajectory deviates without explicit error. | Detecting Silent Failures | Plausible output but incomplete, stale, or unverifiable extraction. |

---

# 5. Ready-to-Add Paragraph for S5.5

Current LLM agents remain brittle under dynamic and compositional conditions. Baba Is AI shows that even strong multimodal models can fail when success requires manipulating and composing environmental rules rather than merely following static instructions. Reflection-Bench extends this critique by framing agent reliability as epistemic agency, decomposing robust interaction into prediction, decision-making, perception, memory, counterfactual reasoning, belief updating, and meta-reflection. From a systems perspective, VeriLA and recent work on silent failures show that multi-agent failures often require interpretable verification and trace-level anomaly detection, because errors may propagate across subtasks or remain hidden in apparently valid outputs. For generalized web automation and data extraction, these findings imply that evaluation should move beyond final task success toward state-aware, provenance-aware, and trajectory-aware failure analysis.

---

# 6. Tools and Framework Examples for S5.5

These tools/frameworks are useful to mention in the failure-mode and observability discussion. They should not be treated as peer-reviewed evidence unless accompanied by papers or documentation.

| Category | Examples | How to connect to S5.5 |
|---|---|---|
| Browser automation tracing | Playwright tracing, Selenium logs, Chrome DevTools Protocol | Capture page actions, screenshots, network events, console errors. |
| Agent observability | OpenTelemetry, AgentOps, LangSmith, Arize Phoenix | Monitor trajectories, tool calls, latency, token usage, and failure signals. |
| Agent frameworks | LangChain, AutoGen, CrewAI, OpenAI Agents SDK | Multi-agent workflows where error propagation and silent failures occur. |
| Evaluation harnesses | BrowserGym, WebArena, VisualWebArena, OSWorld | Can be extended with failure-mode annotations and trajectory diagnostics. |
| Verification tools | LLM-as-judge, task-specific verifiers, schema validators, JSON validators | Useful for subtask-level and field-level verification. |
| Web extraction validators | schema validation, provenance checking, DOM-to-value alignment | Critical for detecting hallucinated or unsupported extracted fields. |
| Anomaly detection infrastructure | XGBoost, Random Forest, SVDD, Isolation Forest, K-Means, SHAP | Can model normal vs anomalous agent traces. |

---

# 7. Recommendations: What to Include Later

## Strongly include

1. **Reflection-Bench**  
   Use it for a strong conceptual framing of epistemic agency and cognitive failure dimensions.

2. **Baba Is AI**  
   Use it as concrete evidence that current multimodal LLMs fail in rule-manipulation and compositional environments.

## Include briefly / supporting

3. **VeriLA**  
   Use as a recent human-centered verification framework for localized agent-failure analysis.

4. **Detecting Silent Failures in Multi-Agentic AI Trajectories**  
   Use as recent evidence for silent failure and trajectory-level anomaly detection, but cite cautiously as arXiv-only.

## Do not overuse

Do not make S5.5 dominated by non-web benchmarks. Use these P3 papers to strengthen the conceptual failure taxonomy, then connect back quickly to web agents and extraction.

---

# 8. Final S5.5 Thesis Contribution Link

These P3 papers help justify the need for your thesis direction:

> Generalized web data extraction cannot rely only on stronger LLMs or larger benchmarks. It requires agents that can perceive dynamic page state, compose actions under changing rules, update beliefs after failures, verify intermediate outputs, preserve provenance, and detect silent trajectory anomalies.

This is directly aligned with your thesis gap:

> Existing web-agent benchmarks measure task completion, but generalized web extraction requires state-aware, schema-aware, provenance-aware, and failure-aware agent evaluation.

---

# 9. Short Bibliographic Notes

## Baba Is AI
Prefer final ICML/PMLR citation if available in your BibTeX manager:

```bibtex
@inproceedings{cloos2024baba,
  title={Baba Is AI: Break the Rules to Beat the Benchmark},
  author={Cloos, Nathan and Jens, Meagan and Naim, Michelangelo and Kuo, Yen-Ling and Cases, Ignacio and Barbu, Andrei and Cueva, Christopher J.},
  booktitle={Proceedings of the 41st International Conference on Machine Learning},
  series={Proceedings of Machine Learning Research},
  volume={235},
  year={2024}
}
```

## Reflection-Bench
Use PMLR citation:

```bibtex
@InProceedings{pmlr-v267-li25cu,
  title={Reflection-Bench: Evaluating Epistemic Agency in Large Language Models},
  author={Li, Lingyu and Wang, Yixu and Zhao, Haiquan and Kong, Shuqi and Teng, Yan and Li, Chunbo and Wang, Yingchun},
  booktitle={Proceedings of the 42nd International Conference on Machine Learning},
  pages={36236--36264},
  year={2025},
  volume={267},
  series={Proceedings of Machine Learning Research},
  publisher={PMLR}
}
```

## VeriLA
Use cautious workshop/arXiv form:

```bibtex
@misc{sung2025verila,
  title={VeriLA: A Human-Centered Evaluation Framework for Interpretable Verification of LLM Agent Failures},
  author={Sung, Yoo Yeon and Kim, Hannah and Zhang, Dan},
  year={2025},
  eprint={2503.12651},
  archivePrefix={arXiv},
  primaryClass={cs.AI},
  note={HEAL@CHI 2025 workshop / arXiv preprint}
}
```

## Detecting Silent Failures
Use cautious arXiv form:

```bibtex
@misc{pathak2025silentfailures,
  title={Detecting Silent Failures in Multi-Agentic AI Trajectories},
  author={Pathak, Divya and Kumar, Harshit and Roy, Anuska and George, Felix and Verma, Mudit and Moogi, Pratibha},
  year={2025},
  eprint={2511.04032},
  archivePrefix={arXiv},
  primaryClass={cs.AI},
  note={arXiv preprint}
}
```
