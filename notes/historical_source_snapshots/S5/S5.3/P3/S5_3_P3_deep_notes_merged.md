# S5.3 P3 — Deep Paper Notes and Venue/Status Verification

**Section:** S5.3 — Planning and Reasoning for Web Agents  
**Priority level:** P3 — supporting but useful  
**Batch size:** 1 paper  
**Purpose of this file:** preserve deep notes for later selection when writing the thesis literature chapter and the cleaned ACM Computing Surveys-style survey.

---

## 0. Section-level summary

This S5.3 P3 batch contains one highly relevant planning/world-modeling paper:

1. **Can Language Models Serve as Text-Based World Simulators?** — Wang et al., ACL 2024 Short Papers.

Although this paper is not specifically about web agents, it is very useful for **S5.3 Planning and Reasoning** because it directly tests a central assumption behind many agentic planning methods: whether an LLM can internally simulate environment state transitions reliably enough to support planning. The answer is mostly negative: even GPT-4 struggles with non-trivial state transitions, especially environment-driven dynamics and transitions requiring arithmetic, commonsense, or scientific reasoning.

**How it supports your thesis:** generalized web automation and web data extraction require agents to predict the consequences of actions such as clicking filters, submitting forms, changing sort orders, opening menus, navigating pagination, and waiting for dynamic page updates. This paper gives evidence that LLMs should not be treated as reliable implicit world simulators. For web agents, this supports the need for explicit observation feedback, grounded state tracking, verifiable action effects, and benchmark protocols that measure state-transition errors rather than only final task success.

---

## 1. Venue/status verification table

| Paper | Year | Final venue/status | Peer-reviewed? | Citation strength | Notes |
|---|---:|---|---|---|---|
| Can Language Models Serve as Text-Based World Simulators? | 2024 | ACL 2024, Volume 2: Short Papers, pages 1–17 | Yes | Strong supporting citation | Cite ACL version, not only arXiv. The uploaded PDF is the arXiv version, but the final official version appears in ACL Anthology as `2024.acl-short.1`, DOI `10.18653/v1/2024.acl-short.1`. |

---

# 2. Paper note

## Can Language Models Serve as Text-Based World Simulators?

**Authors:** Ruoyao Wang, Graham Todd, Ziang Xiao, Xingdi Yuan, Marc-Alexandre Côté, Peter Clark, Peter Jansen  
**Year:** 2024  
**Final venue:** ACL 2024, Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics, Volume 2: Short Papers  
**Pages:** 1–17  
**DOI:** 10.18653/v1/2024.acl-short.1  
**ACL Anthology ID:** 2024.acl-short.1  
**Uploaded version:** arXiv:2406.06485v1, 10 June 2024  
**Citation key suggestion:** `wang2024textworldsimulators` or official ACL key `wang-etal-2024-language`

### Venue / status

- **Status:** Peer-reviewed ACL 2024 short paper.
- **Use in review:** Safe to cite as a strong supporting reference.
- **Citation caution:** Use the ACL Anthology version in the final bibliography. The arXiv PDF is acceptable for reading, but the final citation should be the ACL 2024 short-paper version.

### Paper type

- Benchmark paper.
- Evaluation paper.
- Planning/world-modeling analysis.
- LLM-as-simulator critique.

### Primary thesis section

- **Main section:** S5.3 — Planning and Reasoning for Web Agents.
- **Secondary sections:**
  - S5.1 — Benchmarks and Evaluation.
  - S5.5 — Failure Modes and Generalization.
  - S8 — Open Challenges.

---

## Core idea

The paper asks whether language models can directly serve as **text-based world simulators**: given a current state, an action, and game rules, can the model predict the next state, reward, and completion status accurately enough to replace manually coded simulation environments?

The authors answer this by constructing **BYTESIZED32-State-Prediction**, a dataset of state transitions from text-game environments, and evaluating GPT-4 and GPT-3.5 on single-step transition prediction.

The central result is important for agent planning: LLMs are not yet reliable enough to act as standalone world models. They can often handle simple action-driven updates but fail much more often on environment-driven dynamics and non-trivial state changes.

---

## Problem addressed

Many planning methods assume some form of world model. In classical planning, the transition model is explicit. In LLM-based planning, however, the model is often asked to implicitly reason about action effects using prior knowledge and in-context rules.

The paper challenges this assumption. It asks whether an LLM can accurately simulate:

1. **Action-driven transitions** — direct effects of an action, such as opening a box or turning on a sink.
2. **Environment-driven transitions** — effects caused by latent environment dynamics, such as water filling a cup after the sink is turned on.
3. **Game progress** — reward, termination, and success/failure status.
4. **Full world-state evolution** — the combined transition after both action and environment dynamics.

For web agents, this maps directly to whether an LLM can infer what happens after clicking, filtering, typing, submitting, scrolling, opening a modal, waiting for asynchronous updates, or changing page state.

---

## Method / approach

The authors formulate text environments as goal-conditioned partially observable Markov decision processes and define an **LLM-as-a-Simulator (LLM-Sim)** task.

The simulator receives:

- natural-language context and rules,
- current state represented as JSON,
- current action,
- sometimes examples of transitions.

It must output:

- next world state,
- reward,
- game-over flag,
- game-won flag.

The paper decomposes simulation into three functions:

| Component | Meaning | Why it matters |
|---|---|---|
| `Fact` | Action-driven transition simulator | Tests whether the model understands direct action effects. |
| `Fenv` | Environment-driven transition simulator | Tests latent dynamics independent of the immediate action. |
| `FR` | Game progress simulator | Tests whether the model understands score, completion, and success conditions. |
| `F` | Full transition simulator | Tests complete next-state prediction. |

The paper evaluates two output modes:

1. **Full-state prediction** — output the complete next JSON state.
2. **State-difference prediction** — output only modified/removed state components.

The state-difference setup is especially relevant for web agents, because many web-state updates are sparse: most DOM/page elements remain unchanged after an action, while only some components change.

---

## Dataset / benchmark

The authors introduce **BYTESIZED32-State-Prediction (BYTESIZED32-SP)**.

Key dataset properties:

- Derived from the BYTESIZED32 corpus.
- Contains **76,369 state transitions**.
- Covers **31 text games**.
- States are represented as structured JSON objects.
- Each transition includes current state, action, intermediate action-driven state, next state, reward, and completion status.
- Context includes action rules, object rules, scoring rules, and example transitions.

This makes the benchmark useful because it isolates state-transition prediction, instead of only measuring final task success.

---

## Experimental setup

The paper evaluates GPT-4 and GPT-3.5 in in-context learning settings.

Important conditions:

| Condition | Description |
|---|---|
| Human-written rules | Rules written by expert annotators. |
| LLM-generated rules | Rules generated from code by GPT-4 and manually checked. |
| No rules | Model predicts using only prior knowledge and examples. |
| Static transitions | No non-trivial world-state change. |
| Dynamic transitions | World state changes non-trivially. |
| Full output | Full next state. |
| Diff output | Only state differences. |

The design is careful because it separates easy cases from hard cases. Static states are much easier than dynamic ones, and direct action effects are easier than environment dynamics.

---

## Key findings

### 1. LLMs are unreliable world simulators

Even GPT-4 does not reach reliable accuracy on dynamic state transitions. The paper reports that across settings, accuracy does not exceed **59.9%** for transitions involving non-trivial state changes.

**Interpretation for your review:** planning methods that rely only on LLM-internal simulation are fragile. Web agents should use external observations and environment feedback rather than assuming that the LLM correctly predicts page-state evolution.

### 2. Action-driven transitions are easier than environment-driven transitions

GPT-4 handles direct action effects better than latent environment dynamics. For example, predicting that an object has been opened is easier than predicting secondary effects that happen after time or environmental rules are applied.

**Web-agent implication:** clicking a button may be easier to reason about than predicting asynchronous updates, hidden state changes, pagination effects, or dynamic JavaScript behavior.

### 3. Static transitions are easier than dynamic transitions

The model often performs better when the correct next state is unchanged. This matters because high aggregate accuracy may hide weakness on the actually important cases where actions change the environment.

**Web-agent implication:** a benchmark should distinguish no-op actions from state-changing actions. Otherwise, an agent may appear competent because many actions do not change visible state.

### 4. Rules help, but do not solve the problem

Providing action/object/scoring rules improves performance, and GPT-4-generated rules can be approximately comparable to human-written rules in some conditions. However, rules do not make the LLM a fully reliable simulator.

**Web-agent implication:** even if an agent receives descriptions of website affordances or API/documentation rules, it still needs execution-grounded verification.

### 5. Arithmetic, commonsense, and scientific dynamics are major failure points

The authors find errors concentrated in properties requiring arithmetic, commonsense inference, or scientific knowledge. The model is better with simple Boolean properties than complex numerical or causal dynamics.

**Web-agent implication:** web automation tasks involving counters, prices, quantities, filters, date ranges, pagination totals, or table transformations may be vulnerable to planning errors unless the agent verifies state changes explicitly.

---

## Important figures/tables to remember

### Figure 1 — LLM as full-state vs state-difference simulator

The figure shows how the model receives state, action, rules, and examples, then predicts either a full next state or only the state difference. It is useful as a conceptual illustration for your S5.3 discussion of **state-transition prediction**.

### Table 1 — BYTESIZED32-SP corpus statistics

Useful numbers:

- 31 games.
- 76,369 transitions.
- Average 2,463.5 states per game.
- Average 7.4 action verbs per game.
- Average 10.4 object instances per state.

### Table 2 — GPT-4 transition prediction accuracy

This is the most important empirical table. It shows that GPT-4 performs much better on action-driven transitions than environment-driven transitions, and much better on static than dynamic transitions.

### Table 3 — Game progress prediction

GPT-4 predicts game progress much better when rules are provided, reaching 92.1% with LLM-generated rules, compared with 61.5% without rules.

### Figure 2 — Error breakdown by property type

This is useful for failure-mode discussion. It shows that errors concentrate around properties requiring non-trivial state updates, including arithmetic-like and environment-dynamic variables.

---

## Limitations

1. **Text-game domain only.** The benchmark focuses on text-based games, not web pages, graphical interfaces, or browser environments.
2. **Single-step prediction.** The evaluation isolates one-step transitions. Real agents perform long multi-step trajectories where errors compound.
3. **Limited model coverage.** The main analysis centers on GPT-4 and GPT-3.5, not a large contemporary model suite.
4. **Structured JSON state.** The task assumes access to a structured state representation. Real web agents often see partial DOM, screenshots, accessibility trees, or noisy OCR rather than gold JSON state.
5. **Simplified environment class.** Text games are controlled environments; modern web pages include JavaScript, dynamic rendering, asynchronous network calls, ads, modals, cookie banners, authentication flows, and anti-bot behavior.

---

## Critique

This paper is highly valuable because it measures a specific agentic capability that is often assumed but rarely isolated: **transition-level world modeling**. Its strongest contribution is not just the dataset, but the decomposition between action-driven and environment-driven transitions.

For your literature review, the paper should not be presented as a web-agent benchmark. It should be presented as **planning evidence**: it empirically shows that LLMs cannot be trusted as implicit simulators of state change.

The main weakness for your thesis is domain distance. Text games are not websites. However, the abstraction is close enough to support your argument: web agents also operate in stateful environments where actions change hidden and visible state. The paper therefore supports a general claim about planning fragility, but not a direct claim about browser automation performance.

---

## Relevance to your thesis

Your thesis focuses on **LLM-based agents for generalized web automation and data extraction**. This paper is relevant because generalized web extraction requires more than selecting actions. The agent must understand whether each action produced the intended state change.

Examples:

- Did clicking “next page” actually move to the next page?
- Did a filter apply correctly?
- Did a dropdown selection change the results table?
- Did the website silently reject a form input?
- Did a modal block interaction?
- Did the page update asynchronously after a delay?
- Did the extraction schema remain valid after navigation?

The paper supports the argument that LLMs should not rely only on internal world simulation. Instead, robust web agents need:

1. explicit state observation,
2. action-effect verification,
3. state-difference tracking,
4. recovery after failed transitions,
5. grounding in DOM/screenshot/accessibility evidence,
6. benchmark metrics for transition correctness.

---

## How to use it in S5.3

Use this paper in the subsection on **planning, world models, and action-effect prediction**.

Suggested placement:

```text
S5.3 Planning and Reasoning for Web Agents
  - ReAct-style reactive planning
  - Tree/search-based planning
  - LLMs as implicit world models
  - Limits of LLM-based state-transition simulation
  - Need for grounded feedback loops in web agents
```

This paper should appear after discussing planning methods such as ReAct, RAP, LLM+P, and WorldCoder, because it provides a counterpoint: even when LLMs are used as world models, their transition predictions remain unreliable.

---

## Ready-to-add sentence

> Wang et al. show that even GPT-4 remains an unreliable text-based world simulator, with major weaknesses on dynamic and environment-driven state transitions; this suggests that web agents should not rely on LLM-internal action-effect prediction alone, but should instead combine planning with explicit observation feedback, state-difference tracking, and grounded verification.

---

## Ready-to-add paragraph for S5.3

> A complementary line of work evaluates whether LLMs can act as implicit world models for planning. Wang et al. introduce BYTESIZED32-State-Prediction, a benchmark that asks language models to predict state transitions in text-game environments from structured JSON states, action rules, and task context. Their results show that even GPT-4 is unreliable on non-trivial dynamic transitions, especially environment-driven changes that are not the direct result of the immediate action. For web agents, this is an important caution: browser automation similarly requires predicting and verifying state changes caused by clicks, form submissions, filters, pagination, and asynchronous page updates. Therefore, robust web-agent planning should not rely only on LLM-internal simulation, but should incorporate external observation, explicit state tracking, and transition-level verification.

---

## Connects to

| Target section | Connection |
|---|---|
| S3 — LLM Agent Architectures | Supports discussion of memory/planning loops and the limits of model-internal reasoning. |
| S5.1 — Benchmarks and Evaluation | Shows why transition-level metrics are needed, not only final success rate. |
| S5.3 — Planning and Reasoning | Directly relevant to world modeling, planning, action-effect prediction, and environment simulation. |
| S5.5 — Generalization and Failure Modes | Supports failure modes around incorrect state prediction and compounding planning errors. |
| S6 — Web Data Extraction | Supports need to verify extraction actions such as filtering, pagination, and table expansion. |
| S8 — Open Challenges | Supports future work on state-aware, verifiable, grounded web agents. |

---

## Tools/frameworks/examples to mention with this paper

| Tool / benchmark / framework | Category | How it connects |
|---|---|---|
| BYTESIZED32-State-Prediction | Benchmark | Main dataset introduced by the paper for testing text-game state-transition simulation. |
| BYTESIZED32 | Text-game/world-model corpus | Source corpus from which the benchmark is derived. |
| TextWorld | Text-based environment | Earlier environment family for embodied language agents and interactive fiction. |
| ScienceWorld | Text-based science environment | Related environment where agents interact with scientific commonsense tasks. |
| ALFWorld | Text + embodied environment | Related benchmark linking text-based planning with embodied action. |
| RAP / Reasoning via Planning | Planning method | Example of LLM planning with an internal/world-model-like component. |
| LLM+P | Neuro-symbolic planning | Example of using formal planners to compensate for weak LLM planning. |
| WorldCoder | Model-based LLM agent | Related direction where agents build world models through code and interaction. |
| JSON state-difference tracking | Evaluation design pattern | Useful idea for web agents: compare pre/post action state differences rather than only final answer. |

---

## Recommendation for final thesis/survey

**Include, but briefly.**

This is a strong P3 paper for S5.3. It should not receive as much space as core web-agent papers, but it is worth citing because it gives empirical evidence for a key planning limitation.

Recommended usage level:

- **Thesis chapter:** 1 paragraph + possibly one sentence in the open-gap synthesis.
- **ACM survey:** 2–4 sentences in a subsection about planning/world models.
- **Short conference paper:** only cite if the paper focuses on evaluation gaps or planning reliability.

---

## Citation caution

Use the official ACL version:

```bibtex
@inproceedings{wang-etal-2024-language,
  title = {Can Language Models Serve as Text-Based World Simulators?},
  author = {Wang, Ruoyao and Todd, Graham and Xiao, Ziang and Yuan, Xingdi and C{\^o}t{\'e}, Marc-Alexandre and Clark, Peter and Jansen, Peter},
  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
  month = aug,
  year = {2024},
  address = {Bangkok, Thailand},
  publisher = {Association for Computational Linguistics},
  pages = {1--17},
  doi = {10.18653/v1/2024.acl-short.1},
  url = {https://aclanthology.org/2024.acl-short.1/}
}
```

---

# 3. S5.3 synthesis from this P3 batch

This P3 batch adds one important conceptual point to S5.3:

> LLM planning should not be treated as reliable world simulation.

Many web-agent systems use prompting, chain-of-thought, ReAct-style loops, or search-based planning, but the ability to plan depends on predicting what actions will do. Wang et al. show that LLMs struggle to predict even structured text-game state transitions under controlled conditions. Therefore, web-agent planning should be evaluated not only by final task success but also by whether the agent correctly tracks intermediate state changes.

For generalized web extraction, this is especially important because extraction workflows are stateful:

1. The agent may need to apply filters before extraction.
2. It may need to paginate through result pages.
3. It may need to open detail pages and return safely.
4. It may need to detect whether a click changed content or failed silently.
5. It may need to distinguish visible state from hidden page/application state.
6. It may need to recover when the expected state transition does not occur.

Thus, this paper supports a strong claim in your review:

> The planning bottleneck for web agents is not only choosing the next action; it is verifying whether the selected action changed the web environment in the intended way.

---

# 4. Possible subsection text for S5.3

## LLMs as implicit world models

A key assumption behind agentic planning is that the agent can anticipate how the environment will change after an action. However, recent evidence suggests that LLMs remain unreliable as implicit world simulators. Wang et al. evaluate GPT-4 and GPT-3.5 on BYTESIZED32-State-Prediction, a benchmark of structured text-game state transitions. Their results show that models handle direct action effects better than environment-driven dynamics and remain weak on non-trivial dynamic state changes. This finding is directly relevant to web agents: browser actions often trigger hidden or delayed page-state updates, such as asynchronous loading, filtering, modal changes, pagination, and form validation. As a result, robust web-agent planning should be designed around observation feedback and transition verification rather than relying purely on internal LLM prediction.

---

# 5. Final inclusion decision

| Decision | Reason |
|---|---|
| Include in thesis literature chapter | Yes — useful as supporting evidence for planning/world-modeling limits. |
| Include in ACM survey | Yes, but briefly — use in planning limitations or evaluation gaps. |
| Include in 6–8 page conference paper | Only if the paper discusses planning reliability or benchmark gaps. |
| Cite as core web-agent benchmark | No — it is not a web benchmark. |
| Cite as planning/world-model evidence | Yes — this is the correct use. |

