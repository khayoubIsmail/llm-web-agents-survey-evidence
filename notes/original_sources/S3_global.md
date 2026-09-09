# S3 - LLM Agent Architectures

Generated on: 2026-05-07 23:40

---

## P0 (3 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\P0\2022-10 - ReAct- Synergizing Reasoning and Acting in Language Models -- v1.md

# Paper 17 — ReAct: Synergizing Reasoning and Acting in Language Models

## Metadata

- **Title:** ReAct: Synergizing Reasoning and Acting in Language Models
- **Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- **Year:** 2023
- **First arXiv version:** 2022
- **Venue:** International Conference on Learning Representations (ICLR 2023)
- **DOI:** 10.48550/arXiv.2210.03629
- **arXiv ID:** arXiv:2210.03629
- **Thesis section:** S3 — LLM Agent Architectures
- **Cross-links:** S5.3 — Planning and Decision-Making; S5.5 — Failure Modes; S6 — Web Information Extraction; S8 — Deployment Realities
- **Category:** AGENT / REASONING-ACTING / TOOL-USE
- **Paper type:** Method / prompt-based agent architecture
- **Priority:** P0
- **BibTeX key:** yao2023react

---

## Simple understanding

This paper introduces **ReAct**, one of the most important early LLM-agent architectures.

Before ReAct, reasoning and acting were often studied separately. Chain-of-thought prompting made LLMs reason step by step, but the reasoning stayed inside the model and was not grounded in external observations. Other systems generated actions, but often without explicit reasoning traces.

ReAct combines both. The model alternates between:

```text
Thought → Action → Observation → Thought → Action → Observation
```

This allows the model to reason about what to do, take an action, observe the environment, then update its next reasoning step based on the observation.

For the thesis, ReAct is a cornerstone paper because it directly introduces the agent loop that later web agents use: reasoning plus action plus feedback from the environment.

---

## Notes

- **Core idea:**
  Introduces a prompting paradigm where LLMs interleave verbal reasoning traces with task-specific actions, allowing reasoning to guide actions and observations to update reasoning.

- **Key finding:**
  ReAct improves performance and interpretability across question answering, fact verification, ALFWorld, and WebShop. On ALFWorld and WebShop, it outperforms action-only and prior imitation/RL baselines with only one or a few in-context examples.

- **Limitation:**
- ReAct depends heavily on prompt examples and in-context learning. For web agents, this matters because complex websites and workflows may require many demonstrations, which can exceed the context window and reduce generalization.
- ReAct can still enter loops, repeat actions, or generate incorrect reasoning. For web agents, this matters because repeated wrong clicks, stale observations, or cyclic plans can cause task failure in long-horizon browser automation.
- ReAct uses simplified textual action spaces in its main benchmarks. For web agents, this matters because real websites include visual layout, hidden states, dynamic JavaScript behavior, authentication, pop-ups, and precise UI grounding problems.
- ReAct improves interpretability but does not guarantee factuality or correctness. For web agents, a readable reasoning trace can still justify an incorrect extraction or wrong UI action.
- ReAct does not provide persistent memory across tasks. For web agents, this matters because repeated or long-running automation benefits from remembering previous failures, website structure, and user preferences.

- **Connects to:**
  ReAct is the main bridge from S2 reasoning methods to S3 agent architectures. It connects CoT reasoning to action execution and environment feedback, and it directly feeds S5.3 planning and S5.5 failure-mode analysis.

- **Use in thesis:**
  Use as the first S3 cornerstone paper to define the basic LLM-agent loop: reasoning, acting, observation, and update. It is also directly relevant to web automation because it evaluates on WebShop, a web interaction benchmark.

- **BibTeX key:**
  yao2023react

---

## Thesis-ready paragraph

Yao et al. proposed ReAct, a prompting framework that interleaves reasoning traces and environment actions in large language models. Unlike chain-of-thought prompting, which produces static reasoning before an answer, ReAct places reasoning inside an interactive loop: the model reasons about the current state, takes an action, receives an observation, and updates its next reasoning step accordingly. This is a foundational architecture for LLM-based agents because it connects language reasoning to external environments. In web automation, the ReAct pattern maps naturally to browser use: an agent observes a page, reasons about the next step, clicks or types, observes the result, and continues. However, ReAct remains limited by prompt dependence, simplified action spaces, lack of persistent memory, and vulnerability to loops or hallucinated reasoning. These limitations motivate later work on reflection, memory, tool use, robust planning, grounding, and web-specific evaluation.

---

## Why this paper matters for my thesis

This paper matters because S3 is no longer only about what LLMs can understand or reason about. S3 is about how LLMs become **agents**.

For my thesis, the key question is:

```text
How can an LLM be organized into a system that observes, reasons, acts, receives feedback, and improves?
```

This paper contributes one core component of that answer. It helps move the literature review from:

```text
LLM as text generator
```

to:

```text
LLM as agent controller
```

For generalized web automation and data extraction, this is essential because the system must not only generate answers. It must interact with websites, call tools, handle observations, recover from failures, and verify extracted data.

---

## Important concepts to remember

- Reasoning trace: a natural-language thought used to plan, track progress, or recover from errors.
- Action: a command issued to an external environment or tool.
- Observation: feedback returned by the environment after an action.
- Reason-to-act: reasoning helps select the next action.
- Act-to-reason: actions retrieve new evidence that improves future reasoning.
- Agent loop: repeated Thought → Action → Observation cycles.

---

## Key evidence from the paper

- Figure 1 compares Standard, CoT, Act-only, and ReAct, showing how ReAct combines reasoning and action in HotpotQA and ALFWorld.
- On HotpotQA and FEVER, ReAct reduces hallucination compared with pure CoT by using external Wikipedia observations.
- On ALFWorld, the best ReAct trial reaches 71% success, outperforming Act-only and BUTLER baselines.
- On WebShop, ReAct reaches 40.0% success versus 30.1% for Act-only and around 29% for IL/RL baselines.
- Figure 4 shows that human editing of ReAct thoughts can correct future behavior, supporting interpretability and controllability.

---

## Connection to later sections

- **S5.3 Planning:** ReAct introduces action-conditioned planning and dynamic plan updates.
- **S5.5 Failure Modes:** loops, hallucinated thoughts, retrieval errors, and poor recovery.
- **S6 Extraction:** ReAct-style search/lookup/finish loops apply to evidence-gathering and extraction.
- **S8 Deployment:** prompt length, cost, tool reliability, and human-in-the-loop correction.

---

## Limitation connected to thesis

The most important thesis-relevant limitation is:

```text
This paper improves one part of agent behavior, but it does not fully solve generalized web automation.
```

A complete web agent still needs:

```text
instruction understanding
→ page observation
→ DOM or visual grounding
→ planning
→ action/tool execution
→ feedback interpretation
→ memory
→ error recovery
→ structured extraction
→ verification
→ safety control
```

Therefore, use this paper as a foundation for S3 agent architectures, then later connect its limitations to S5.2, S5.3, S5.5, S6, S7, and S8.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Very high. Read fully. Focus on Figure 1, Section 2, HotpotQA/FEVER results, ALFWorld/WebShop results, Figure 4, and limitations.
- **Main use:** Core S3 architecture paper
- **Read after:** S2 foundations
- **Use while writing:** S3 narrative and cross-linked sections on planning, tools, memory, failure modes, and deployment

---

## One-sentence summary

Introduces a prompting paradigm where LLMs interleave verbal reasoning traces with task-specific actions, allowing reasoning to guide actions and observations to update reasoning. Its main thesis relevance is that it moves LLMs from passive reasoning toward agentic systems, but still requires stronger grounding, verification, safety, and deployment mechanisms for generalized web automation.

---

## BibTeX

```bibtex
@inproceedings{yao2023react,
  title     = {ReAct: Synergizing Reasoning and Acting in Language Models},
  author    = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  booktitle = {International Conference on Learning Representations},
  year      = {2023},
  eprint    = {2210.03629},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  doi       = {10.48550/arXiv.2210.03629}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2210.03629
- ICLR / project material: https://react-lm.github.io


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\P0\2023-03 - Reflexion- Language Agents with Verbal Reinforcement Learning -- v1.md

# Paper 18 — Reflexion: Language Agents with Verbal Reinforcement Learning

## Metadata

- **Title:** Reflexion: Language Agents with Verbal Reinforcement Learning
- **Authors:** Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
- **Year:** 2023
- **First arXiv version:** 2023
- **Venue:** Advances in Neural Information Processing Systems 36 (NeurIPS 2023)
- **DOI:** 10.48550/arXiv.2303.11366
- **arXiv ID:** arXiv:2303.11366
- **Thesis section:** S3 — LLM Agent Architectures
- **Cross-links:** S5.3 — Planning and Decision-Making; S5.5 — Failure Modes; S7 — Safety and Trustworthiness; S8 — Deployment Realities
- **Category:** AGENT / REFLECTION / MEMORY / VERBAL-RL
- **Paper type:** Method / agent memory and self-reflection framework
- **Priority:** P0
- **BibTeX key:** shinn2023reflexion

---

## Simple understanding

This paper introduces **Reflexion**, an agent framework that allows LLM agents to learn from failure without changing model weights.

The key idea is simple: after a failed attempt, the agent writes a natural-language reflection about what went wrong and stores it in memory. On the next trial, the agent uses this reflection to make a better plan.

So Reflexion changes the agent through **language memory**, not fine-tuning.

For the thesis, this paper is crucial because web agents often fail because of loops, wrong searches, bad UI decisions, or incomplete plans. Reflexion provides a mechanism for error recovery and learning from previous attempts, which is central for robust generalized web automation.

---

## Notes

- **Core idea:**
  Introduces verbal reinforcement learning: agents improve across trials by reflecting in natural language, storing reflections in episodic memory, and using that memory to guide later decisions.

- **Key finding:**
  Reflexion improves agent performance across decision-making and knowledge-intensive tasks. The uploaded v1 reports strong gains on ALFWorld and HotPotQA; the later NeurIPS version also extends the framework to coding and reasoning tasks.

- **Limitation:**
- Reflexion depends on failure detection or reward signals. For web agents, this matters because many web tasks do not provide clear success/failure feedback; an agent may submit a form or extract data without knowing whether the result is correct.
- Reflections can be wrong or unhelpful. For web agents, this matters because an incorrect reflection can bias future actions, repeat a bad strategy, or create false confidence about a website structure.
- Reflexion improves over repeated trials, but some web tasks are one-shot or risky. For web agents, retrying may be impossible if actions involve purchases, submissions, account changes, or irreversible operations.
- Memory is limited and can become noisy. For web agents, long workflows across many pages require memory management, relevance filtering, and forgetting mechanisms.
- The uploaded early version reports limited improvement on WebShop. For web agents, this matters because performance may depend more on search/tool quality and environment constraints than on reflection alone.

- **Connects to:**
  Reflexion extends ReAct by adding memory and self-improvement across trials. It connects directly to planning, error recovery, long-horizon task execution, and failure-mode mitigation.

- **Use in thesis:**
  Use as the key S3 paper for reflection and dynamic memory. It motivates why web agents need feedback loops and self-correction, not only reasoning-action loops.

- **BibTeX key:**
  shinn2023reflexion

---

## Thesis-ready paragraph

Shinn et al. introduced Reflexion, a framework that reinforces language agents through verbal feedback rather than model weight updates. After a failed attempt, the agent generates a reflection describing its mistake, stores that reflection in memory, and uses it to guide future trials. This is important for LLM-based web agents because browser automation involves long-horizon interaction where failures are common: agents may loop, choose the wrong element, search poorly, or misunderstand page state. Reflexion provides a lightweight mechanism for learning from such failures without fine-tuning. However, its effectiveness depends on reliable failure detection, useful reflection quality, and the possibility of retrying tasks. In real web automation, retries may be costly or unsafe, and success signals may be ambiguous. Therefore, Reflexion is a foundation for self-correcting agents, but it must be integrated with verification, risk control, memory management, and human oversight for robust deployment.

---

## Why this paper matters for my thesis

This paper matters because S3 is no longer only about what LLMs can understand or reason about. S3 is about how LLMs become **agents**.

For my thesis, the key question is:

```text
How can an LLM be organized into a system that observes, reasons, acts, receives feedback, and improves?
```

This paper contributes one core component of that answer. It helps move the literature review from:

```text
LLM as text generator
```

to:

```text
LLM as agent controller
```

For generalized web automation and data extraction, this is essential because the system must not only generate answers. It must interact with websites, call tools, handle observations, recover from failures, and verify extracted data.

---

## Important concepts to remember

- Verbal reinforcement learning: improvement through language feedback instead of weight updates.
- Episodic memory: stored reflections from previous failed trials.
- Self-reflection: natural-language analysis of what went wrong and how to change the next attempt.
- Binary reward/success signal: a simplified indicator used to decide whether reflection is needed.
- Trial-based learning: the agent improves across repeated attempts.

---

## Key evidence from the paper

- Figure 1 presents Reflexion as an add-on to decision-making agents, especially ReAct-style agents.
- In the uploaded v1, the Reflexion agent solves 97% of ALFWorld tasks in 12 trials, compared with a weaker base ReAct trajectory.
- In HotPotQA, the uploaded v1 shows Reflexion improving over repeated trials while the non-reflective baseline stagnates.
- Figure 4 shows a failed ALFWorld trajectory corrected through reflection and a better second trial.
- Figure 6 shows limited improvement on WebShop, highlighting that reflection alone may not overcome poor search/tool quality.

---

## Connection to later sections

- **S5.3 Planning:** reflection supports plan repair and retry strategies.
- **S5.5 Failure Modes:** targets loops, hallucination, inefficient planning, and repeated failure.
- **S7 Safety:** reflection must be constrained because unsafe actions cannot always be retried.
- **S8 Deployment:** memory quality, cost of retries, success detection, and operational risk.

---

## Limitation connected to thesis

The most important thesis-relevant limitation is:

```text
This paper improves one part of agent behavior, but it does not fully solve generalized web automation.
```

A complete web agent still needs:

```text
instruction understanding
→ page observation
→ DOM or visual grounding
→ planning
→ action/tool execution
→ feedback interpretation
→ memory
→ error recovery
→ structured extraction
→ verification
→ safety control
```

Therefore, use this paper as a foundation for S3 agent architectures, then later connect its limitations to S5.2, S5.3, S5.5, S6, S7, and S8.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Very high. Read fully. Focus on architecture, memory/reflection loop, heuristics, ALFWorld, HotPotQA, WebShop limitation, and discussion.
- **Main use:** Core S3 architecture paper
- **Read after:** S2 foundations
- **Use while writing:** S3 narrative and cross-linked sections on planning, tools, memory, failure modes, and deployment

---

## One-sentence summary

Introduces verbal reinforcement learning: agents improve across trials by reflecting in natural language, storing reflections in episodic memory, and using that memory to guide later decisions. Its main thesis relevance is that it moves LLMs from passive reasoning toward agentic systems, but still requires stronger grounding, verification, safety, and deployment mechanisms for generalized web automation.

---

## BibTeX

```bibtex
@inproceedings{shinn2023reflexion,
  title     = {Reflexion: Language Agents with Verbal Reinforcement Learning},
  author    = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {36},
  year      = {2023},
  eprint    = {2303.11366},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  doi       = {10.48550/arXiv.2303.11366}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2303.11366
- OpenReview: https://openreview.net/forum?id=vAElhFcKW6
- Code: https://github.com/noahshinn/reflexion


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\P0\2024-02 - Toolformer- Language Models Can Teach Themselves to Use Tools.md

# Paper 19 — Toolformer: Language Models Can Teach Themselves to Use Tools

## Metadata

- **Title:** Toolformer: Language Models Can Teach Themselves to Use Tools
- **Authors:** Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom
- **Year:** 2023
- **First arXiv version:** 2023
- **Venue:** Advances in Neural Information Processing Systems 36 (NeurIPS 2023)
- **DOI:** 10.48550/arXiv.2302.04761
- **arXiv ID:** arXiv:2302.04761
- **Thesis section:** S3 — LLM Agent Architectures
- **Cross-links:** S5.3 — Planning and Decision-Making; S6 — Web Information Extraction; S7 — Verification; S8 — Deployment Realities
- **Category:** AGENT / TOOL-USE / SELF-SUPERVISION
- **Paper type:** Method / self-supervised tool-use training
- **Priority:** P0
- **BibTeX key:** schick2023toolformer

---

## Simple understanding

This paper introduces **Toolformer**, a language model that learns to use external tools through APIs.

The model learns when to call a tool, which tool to call, what arguments to pass, and how to use the returned result. Importantly, this is done mostly through self-supervision: a model proposes API calls inside text, executes the calls, keeps only the calls that reduce future-token prediction loss, and then fine-tunes on the filtered examples.

For the thesis, Toolformer is important because web agents require tools: search engines, browsers, calculators, databases, APIs, extractors, and validators. Toolformer is a foundation for tool-using LLM agents.

---

## Notes

- **Core idea:**
  Introduces a self-supervised method for teaching language models to use external tools via API calls, deciding when and how to call tools during generation.

- **Key finding:**
  Toolformer improves zero-shot performance on tasks requiring factual lookup, arithmetic, temporal reasoning, translation, and QA, often outperforming much larger models on tool-relevant tasks while preserving language modeling ability.

- **Limitation:**
- Toolformer cannot chain tools in its original form. For web agents, this matters because real web automation often requires multi-tool workflows such as search → browse → extract → validate → store.
- Toolformer does not use tools interactively. For web agents, this matters because browser automation requires iterative query reformulation, page navigation, scrolling, clicking, and handling returned errors.
- The method is sensitive to wording and tool-call decisions. For web agents, this matters because user instructions and web contexts vary widely, and brittle tool invocation can cause missing evidence or wrong actions.
- Toolformer does not account for tool cost when deciding whether to call APIs. For web agents, this matters because web automation can involve expensive browser sessions, paid APIs, latency, rate limits, and operational constraints.
- Toolformer uses text-only API calls, not grounded UI actions. For web agents, this matters because clicking a button or selecting a form field requires DOM or visual grounding, not only API syntax.

- **Connects to:**
  Toolformer connects LLMs to external tools and APIs. It is a foundation for agent architectures that call search, calculators, browsers, databases, and extraction tools.

- **Use in thesis:**
  Use as the key S3 paper for tool-use learning. It supports the thesis claim that LLM agents need external tools to overcome hallucination, outdated knowledge, weak arithmetic, and limited internal capability.

- **BibTeX key:**
  schick2023toolformer

---

## Thesis-ready paragraph

Schick et al. introduced Toolformer, a self-supervised framework that teaches language models to use external APIs during generation. The model samples possible tool calls, executes them, filters calls that improve future-token prediction, and fine-tunes on the resulting tool-augmented corpus. This paper is foundational for LLM-based agents because it shows that tool use can be learned rather than manually scripted for each task. For web automation and data extraction, tool use is essential: agents may need search engines, browsers, calculators, databases, APIs, extractors, and validators. However, Toolformer does not provide a complete web-agent architecture. It cannot chain tools in its original formulation, does not interactively browse or reformulate tool calls, ignores tool cost, and does not ground actions in web interfaces. Thus, Toolformer provides a foundation for tool-using agents, but web automation requires multi-step orchestration, environment feedback, grounding, and verification.

---

## Why this paper matters for my thesis

This paper matters because S3 is no longer only about what LLMs can understand or reason about. S3 is about how LLMs become **agents**.

For my thesis, the key question is:

```text
How can an LLM be organized into a system that observes, reasons, acts, receives feedback, and improves?
```

This paper contributes one core component of that answer. It helps move the literature review from:

```text
LLM as text generator
```

to:

```text
LLM as agent controller
```

For generalized web automation and data extraction, this is essential because the system must not only generate answers. It must interact with websites, call tools, handle observations, recover from failures, and verify extracted data.

---

## Important concepts to remember

- API call: a structured tool invocation inserted into the generated text.
- Self-supervised tool-use data: the model proposes calls and keeps only calls that help prediction.
- Loss-based filtering: retain API calls only when the tool result reduces future-token loss.
- Tool set: QA system, Wikipedia search, calculator, calendar, and machine translation.
- Tool-use emergence: larger models become better at deciding when tools help.

---

## Key evidence from the paper

- Figure 1 shows Toolformer autonomously using QA, calculator, translation, and Wikipedia search tools.
- Figure 2 shows the pipeline: sample API calls, execute calls, filter useful calls, and fine-tune on tool-augmented data.
- Table 3 shows strong gains on factual and math benchmarks, especially when calculator or QA tools are useful.
- Table 4 shows gains on QA and temporal datasets, though some tool limitations remain.
- Section 6 explicitly notes limitations: no chained tool use, no interactive tool use, wording sensitivity, sample inefficiency, and no tool-cost awareness.

---

## Connection to later sections

- **S5.3 Planning:** tool calls must be planned, sequenced, and sometimes chained.
- **S6 Extraction:** APIs and search tools support evidence retrieval and structured extraction.
- **S7 Verification:** tools can validate facts, calculations, and outputs.
- **S8 Deployment:** API cost, latency, tool errors, and rate limits affect real systems.

---

## Limitation connected to thesis

The most important thesis-relevant limitation is:

```text
This paper improves one part of agent behavior, but it does not fully solve generalized web automation.
```

A complete web agent still needs:

```text
instruction understanding
→ page observation
→ DOM or visual grounding
→ planning
→ action/tool execution
→ feedback interpretation
→ memory
→ error recovery
→ structured extraction
→ verification
→ safety control
```

Therefore, use this paper as a foundation for S3 agent architectures, then later connect its limitations to S5.2, S5.3, S5.5, S6, S7, and S8.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Very high. Read fully. Focus on Figures 1–2, Section 2 method, tools, Tables 3–5, scaling, and limitations.
- **Main use:** Core S3 architecture paper
- **Read after:** S2 foundations
- **Use while writing:** S3 narrative and cross-linked sections on planning, tools, memory, failure modes, and deployment

---

## One-sentence summary

Introduces a self-supervised method for teaching language models to use external tools via API calls, deciding when and how to call tools during generation. Its main thesis relevance is that it moves LLMs from passive reasoning toward agentic systems, but still requires stronger grounding, verification, safety, and deployment mechanisms for generalized web automation.

---

## BibTeX

```bibtex
@inproceedings{schick2023toolformer,
  title     = {Toolformer: Language Models Can Teach Themselves to Use Tools},
  author    = {Schick, Timo and Dwivedi-Yu, Jane and Dessi, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {36},
  year      = {2023},
  eprint    = {2302.04761},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  doi       = {10.48550/arXiv.2302.04761}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2302.04761
- OpenReview: https://openreview.net/forum?id=Yacmpz84TH
- Meta AI publication page: https://ai.meta.com/research/publications/toolformer-language-models-can-teach-themselves-to-use-tools/


---

## P1 (6 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\P1\2022-05-MRKL Systems A modular neuro-symbolic architecture that combines large language models external knowledge sources and discrete reasoning.md

# Paper 71 — MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning

## Metadata

- **Title:** MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning
- **Authors:** Ehud Karpas, Omri Abend, Yonatan Belinkov, Barak Lenz, Opher Lieber, Nir Ratner, Yoav Shoham, Hofit Bata, Yoav Levine, Kevin Leyton-Brown, Dor Muhlgay, Noam Rozen, Erez Schwartz, Gal Shachaf, Shai Shalev-Shwartz, Amnon Shashua, Moshe Tenenholtz
- **Year:** 2022
- **Date:** May 3, 2022
- **Venue:** arXiv preprint / AI21 Labs technical report
- **DOI:** 10.48550/arXiv.2205.00445
- **arXiv ID:** arXiv:2205.00445
- **Thesis section:** S3 — LLM Agent Architectures
- **Cross-links:** S5.3 — Planning and Decision-Making; S5.4 — Training Strategies and Generalization; S6 — Web Information Extraction; S7 — Verification and Trustworthiness; S8 — Deployment Realities
- **Category:** AGT / TOOL-USE / NEURO-SYMBOLIC
- **Paper type:** Method / architecture / system design
- **Priority:** P1
- **BibTeX key:** karpas2022mrkl

---

## Simple understanding

This paper introduces **MRKL systems**, pronounced “miracle”: **Modular Reasoning, Knowledge and Language** systems.

The main idea is that a large language model should not do everything alone. LLMs are strong at language understanding and generation, but they are weak in several important cases:

- they do not know current information,
- they cannot access proprietary/private databases,
- they make mistakes in exact reasoning and arithmetic,
- they can hallucinate,
- and fine-tuning one huge model for every capability creates “model explosion.”

MRKL proposes a **systems architecture** where a central language model is combined with multiple external expert modules. These modules can be neural models, symbolic tools, calculators, databases, APIs, search engines, or other discrete reasoning systems.

The MRKL system uses a **router** to decide which expert module should handle the input. If no expert is appropriate, the system can fall back to the general-purpose LLM.

For my thesis, MRKL is important because web agents are also modular systems. A robust web automation agent cannot rely only on the LLM. It needs browsers, search tools, APIs, DOM parsers, extractors, validators, storage systems, and safety filters.

---

## Notes

- **Core idea:**
  Proposes a modular neuro-symbolic architecture that combines large language models with external expert modules for knowledge access and discrete reasoning.

- **Key finding:**
  The paper argues that modular expert routing can overcome major LLM limitations: stale knowledge, lack of proprietary data access, weak exact reasoning, model explosion, and poor interpretability. Its Jurassic-X implementation shows how an LLM-based system can delegate arithmetic to a symbolic calculator after extracting the correct arguments from natural language.

- **Limitation:**
  MRKL depends heavily on the quality of the router.
  For web agents, this matters directly because an agent must decide whether to use the browser, a search engine, a database, an extractor, a calculator, a validator, or the base LLM. A wrong routing decision can produce incorrect actions, miss evidence, or hallucinate results.

- **Additional limitation:**
  MRKL solves modular delegation but does not fully specify long-horizon planning.
  For web agents, this matters because many tasks require sequences of modules: search → browse → inspect DOM → extract → verify → store. A router alone is not enough; the agent needs planning and orchestration over time.

- **Additional limitation:**
  MRKL focuses on text-to-module routing and symbolic argument extraction.
  For web agents, this matters because real browser automation also requires visual/DOM grounding, UI state tracking, scrolling, clicking, form filling, and handling JavaScript-driven page changes.

- **Additional limitation:**
  Adding modules increases system complexity.
  For web agents, this matters because every added expert introduces possible failures: API downtime, bad schemas, latency, cost, authentication problems, and incompatible outputs. This motivates S8 deployment analysis.

- **Additional limitation:**
  Expert modules need reliable interfaces.
  For web agents, this matters because extraction tools, browser tools, and validation tools must expose stable, interpretable outputs that the agent can use safely.

- **Connects to:**
  Toolformer, HuggingGPT, ReAct, LATS, RAG, tool-augmented agents, neuro-symbolic systems, and production-grade web automation systems.

- **Use in thesis:**
  Use MRKL as an early architecture paper showing that LLM-based agents should be modular systems rather than monolithic models. It is especially useful for arguing that web agents require external tools and expert modules for dynamic information, exact reasoning, private databases, and verification.

- **BibTeX key:**
  karpas2022mrkl

---

## Thesis-ready paragraph

Karpas et al. proposed MRKL systems, a modular neuro-symbolic architecture that combines large language models with external knowledge sources and discrete reasoning modules. Rather than treating the LLM as a monolithic solution, MRKL introduces an extendable set of expert modules and a router that directs inputs to the most appropriate module. This architecture is important for LLM-based web automation because web agents require capabilities that pure LLMs do not reliably provide: access to current information, interaction with private databases, exact calculation, symbolic reasoning, and interpretable verification. However, MRKL does not by itself solve the full web-agent problem. Generalized web automation requires long-horizon planning, DOM and visual grounding, interactive browser control, failure recovery, and safe orchestration of multiple tools over time. MRKL therefore provides an important modular foundation for agent architectures, while motivating later work on planning, tool chaining, environment feedback, and deployment-aware agent design.

---

## Why this paper matters for my thesis

This paper matters because generalized web automation is naturally modular.

A web agent may need to use:

```text
LLM reasoning
+ browser automation
+ search engine
+ database/API access
+ DOM parser
+ screenshot analysis
+ extraction model
+ calculator
+ verifier
+ memory system
+ safety policy
```

MRKL gives the architectural idea behind this:

```text
user input → router → expert module(s) → output
```

For a web automation thesis, the important insight is:

```text
A web agent should not ask the LLM to do everything internally.
```

Instead, the LLM should coordinate or cooperate with external systems.

Example:

```text
Task: Extract current product prices from a website.

Bad monolithic approach:
LLM guesses prices from text or memory.

MRKL-style approach:
Browser module opens site.
DOM parser extracts product cards.
Currency module normalizes prices.
Verifier checks extracted values.
LLM summarizes final structured output.
```

So MRKL supports the design principle that LLM agents need **modular tool composition**.

---

## Important concepts to remember

### 1. MRKL

MRKL means:

```text
Modular Reasoning, Knowledge and Language
```

The idea is to combine:

```text
LLM language ability
+ external knowledge sources
+ symbolic/discrete reasoning modules
```

### 2. Experts

Experts are modules specialized for particular tasks.

Examples:

```text
calculator
calendar
database
currency converter
weather API
search engine
domain-specific model
proprietary knowledge base
```

For web agents, experts may include:

```text
browser controller
HTML/DOM parser
vision model
table extractor
RAG retriever
data validator
anti-duplication module
schema matcher
```

### 3. Router

The router decides which expert should handle the input.

In a web agent, routing is similar to deciding:

```text
Should I reason?
Should I search?
Should I click?
Should I use the DOM?
Should I call an API?
Should I verify?
Should I ask the user?
```

### 4. Safe fallback

If no expert matches the input, the system can fall back to the general-purpose LLM.

This is useful because it preserves generality while still using specialized tools when appropriate.

### 5. Robust extensibility

New modules can be added independently.

For web agents, this is important because new websites, extraction tasks, and deployment contexts may require new tools.

### 6. Interpretability

When a module is called, it can provide a rationale or trace.

Example:

```text
The answer is 2 because the calculator returned 2.
```

For web agents, this matters because extraction and action decisions should be traceable to evidence.

### 7. Neuro-symbolic architecture

MRKL is neuro-symbolic because it combines:

```text
neural models → language understanding, routing, extraction of arguments
symbolic modules → exact computation, database access, APIs, rules
```

This hybrid idea is central for reliable web automation.

---

## Key evidence from the paper

### Figure on page 3 — MRKL high-level design

The figure shows the main architecture:

```text
Input text
→ Language Model J-1
→ Input Adapter
→ Expert modules
→ Language Model J-1
→ Output text
```

The modules include examples such as weather API, currency, calendar, database, calculator, and additional experts.

This figure is important because it visually shows the shift from a single LLM to a modular system.

### Section 1 — LLM limitations

The paper lists several limitations of standalone LLMs:

- lack of current information,
- lack of proprietary information,
- weak discrete reasoning,
- and model explosion from task-specific fine-tuning.

These limitations map directly to web agents because web automation depends on dynamic, private, structured, and task-specific information.

### Section 1 — Benefits of MRKL

The paper lists several benefits:

```text
safe fallback
robust extensibility
interpretability
up-to-date information
proprietary knowledge
compositionality
```

These are all thesis-relevant for web agents.

### Section 3 — Calculator test case

The calculator experiment illustrates the neuro-symbolic divide.

The LLM should not perform arithmetic internally. Instead, it should extract the correct operands and operation, then pass them to a symbolic calculator.

For web agents, this same idea applies to extraction and verification:

```text
LLM identifies task meaning.
Specialized tool performs reliable operation.
LLM integrates the result.
```

### Discussion

The discussion frames MRKL as a way to retain the flexibility of LLMs while avoiding their limitations through external modules.

---

## Connection to earlier and later papers

### Connection to GPT-3

GPT-3 shows that LLMs can perform many tasks from prompts.

MRKL says this is not enough:

```text
GPT-3 = general language/task ability
MRKL = general language ability + specialized modules
```

### Connection to Toolformer

Toolformer later learns when and how to call tools through self-supervision.

MRKL gives the earlier system-level architecture:

```text
MRKL: modular expert system with router
Toolformer: LM learns tool calls in generated text
```

### Connection to ReAct

ReAct interleaves reasoning and action.

MRKL provides a tool architecture that ReAct-style agents can act through:

```text
ReAct decides next action.
MRKL-style modules execute specialized capabilities.
```

### Connection to LATS

LATS uses search over reasoning and acting trajectories.

MRKL complements this by providing the modular experts that a planner could choose among.

### Connection to RAG

RAG retrieves external knowledge.

MRKL generalizes this idea: retrieval is one expert among many possible experts.

```text
RAG = retrieval expert
MRKL = retrieval + calculator + database + calendar + more
```

---

## Connection to later thesis sections

- **S3 — LLM Agent Architectures:**
  MRKL is a key architecture for modular, tool-augmented agents.

- **S5.3 — Planning and Decision-Making:**
  The router is an early form of module/action selection. Later planners must sequence multiple tools.

- **S5.4 — Training Strategies and Generalization:**
  MRKL avoids full retraining by adding modules and retraining only lightweight components such as routers.

- **S6 — Web Information Extraction:**
  External modules can include extractors, databases, APIs, schema matchers, and validators.

- **S7 — Security, Robustness, and Trustworthiness:**
  Modular expert calls improve traceability and verification, but also introduce security risks around tool access.

- **S8 — Deployment Realities:**
  MRKL raises real engineering issues: module interfaces, routing reliability, latency, cost, monitoring, and maintenance.

---

## Limitation connected to thesis

MRKL introduces modularity, but it does not solve grounded web interaction.

For generalized web automation, the system must perform:

```text
instruction understanding
→ page observation
→ routing/tool selection
→ DOM or visual grounding
→ action execution
→ feedback interpretation
→ tool chaining
→ extraction
→ verification
→ safe output
```

MRKL mainly addresses:

```text
routing/tool selection
+ external knowledge/reasoning access
```

It does not directly solve:

- clicking UI elements,
- navigating pages,
- grounding actions in DOM nodes,
- managing browser state,
- handling dynamic page changes,
- deciding long-horizon workflows,
- or verifying that a web action succeeded.

Therefore, MRKL should be used in the thesis as a **modular architecture foundation**, not as a complete web-agent solution.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High
- **Main use:** Foundation for modular neuro-symbolic agents and tool orchestration
- **Most important parts:**
  - Abstract
  - Section 1: LLM limitations
  - MRKL architecture figure
  - Benefits of MRKL systems
  - Section 3: calculator test case
  - Discussion
  - Appendix comparison of few-shot vs prompt tuning for arithmetic extraction

---

## One-sentence summary

MRKL systems argue that LLMs should be embedded in modular neuro-symbolic architectures with expert tools and routers, but for web automation this modularity must still be combined with browser grounding, planning, feedback, and verification.

---

## BibTeX

```bibtex
@article{karpas2022mrkl,
  title   = {MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning},
  author  = {Karpas, Ehud and Abend, Omri and Belinkov, Yonatan and Lenz, Barak and Lieber, Opher and Ratner, Nir and Shoham, Yoav and Bata, Hofit and Levine, Yoav and Leyton-Brown, Kevin and Muhlgay, Dor and Rozen, Noam and Schwartz, Erez and Shachaf, Gal and Shalev-Shwartz, Shai and Shashua, Amnon and Tenenholtz, Moshe},
  journal = {arXiv preprint arXiv:2205.00445},
  year    = {2022},
  doi     = {10.48550/arXiv.2205.00445}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2205.00445


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\P1\2023-05 - Tree of Thoughts- Deliberate Problem Solving with Large Language Models -- v1.md

# Paper 75 — Tree of Thoughts: Deliberate Problem Solving with Large Language Models

## Metadata

- **Title:** Tree of Thoughts: Deliberate Problem Solving with Large Language Models
- **Authors:** Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan
- **Year:** 2023
- **First arXiv version:** 2023
- **Venue:** NeurIPS 2023 / arXiv preprint
- **DOI:** 10.48550/arXiv.2305.10601
- **arXiv ID:** arXiv:2305.10601
- **Thesis section:** S3 — LLM Agent Architectures
- **Cross-links:** S5.3 — Planning and Decision-Making; S5.5 — Failure Modes; S8 — Deployment Realities
- **Category:** REA / PLANNING / SEARCH
- **Paper type:** Method / inference-time planning framework
- **Priority:** P1
- **BibTeX key:** yao2023tree

---

## Simple understanding

This paper introduces **Tree of Thoughts (ToT)**.

Chain-of-thought prompting makes a model produce one sequence of reasoning steps. Self-consistency samples several full reasoning chains and chooses the most common answer. Tree of Thoughts goes further: it treats reasoning as a **search problem**.

Instead of committing to one reasoning path, the model explores multiple possible intermediate “thoughts.” Each thought is a meaningful chunk of reasoning. The model can generate possible thoughts, evaluate them, keep the most promising ones, and backtrack when a path is bad.

The key idea is:

```text
Reasoning is not only a chain.
Reasoning can be a tree.
```

For my thesis, ToT matters because web automation also requires planning and search. A web agent should not always follow the first action sequence it generates. It may need to explore alternatives, compare candidate plans, backtrack, and choose the most promising path.

---

## Notes

- **Core idea:**
  Generalizes chain-of-thought into a tree-search framework where LLMs generate, evaluate, and search over multiple intermediate “thoughts” before selecting a final solution.

- **Key finding:**
  ToT substantially improves performance on tasks requiring planning or search. On Game of 24, GPT-4 with chain-of-thought solves only 4% of tasks, while ToT reaches 74% success. ToT also improves Creative Writing and Mini Crosswords.

- **Limitation:**
  ToT is computationally expensive because it requires generating and evaluating many thoughts.
  For web agents, this matters directly because each candidate plan or action may require browser observations, screenshots, DOM parsing, or tool calls. Exhaustive search over web actions can quickly become too slow or costly.

- **Additional limitation:**
  ToT assumes the model can evaluate thoughts reliably.
  For web agents, this matters because an LLM may incorrectly judge a plan as promising even if it refers to a nonexistent button, wrong DOM element, or stale page state.

- **Additional limitation:**
  ToT was evaluated mainly on controlled reasoning/search tasks, not full dynamic web environments.
  For web agents, this matters because real websites are interactive, partially observable, visually complex, and sometimes irreversible.

- **Additional limitation:**
  ToT does not inherently use external environment feedback.
  For web agents, this matters because planning should be grounded in actual browser observations, not only internal model estimates.

- **Additional limitation:**
  Backtracking is easy in text reasoning but harder in real web actions.
  For web agents, this matters because some actions cannot be undone safely, such as submitting a form, deleting data, sending a message, or confirming a purchase.

- **Connects to:**
  Chain-of-thought, self-consistency, Least-to-Most prompting, ReAct, LATS, RAP, MCTS-style planning, search-based agents, and long-horizon web planning.

- **Use in thesis:**
  Use ToT as a key planning paper showing that agent reasoning can be treated as structured search rather than a single greedy trajectory. It supports S5.3 strongly, but should be contrasted with web agents that need environment feedback and safe action execution.

- **BibTeX key:**
  yao2023tree

---

## Thesis-ready paragraph

Yao et al. introduced Tree of Thoughts, an inference-time planning framework that generalizes chain-of-thought prompting into a search over intermediate reasoning states. Instead of generating one reasoning chain, ToT represents problem solving as a tree where each node is a partial solution and each edge is a possible thought continuation. The language model generates candidate thoughts, evaluates their promise, and uses search algorithms such as breadth-first or depth-first search to explore, prune, and backtrack. This is important for LLM-based web agents because web automation often requires planning under uncertainty: the agent must consider alternative actions, evaluate partial progress, and revise decisions when a path fails. However, ToT remains primarily a text-based reasoning framework. It is expensive, depends on LLM self-evaluation, and does not inherently ground decisions in live browser observations or irreversible web actions. Therefore, ToT provides a planning foundation that later web agents must extend with environment feedback, action constraints, DOM/visual grounding, and verification.

---

## Why this paper matters for my thesis

This paper matters because web automation is not a simple one-chain reasoning problem.

A web agent may need to choose between several possible next actions:

```text
click search result 1
click search result 2
scroll down
open filter menu
use site search
go back
extract current table
```

A simple ReAct-style agent often follows one path. If that path is wrong, the whole task can fail.

ToT suggests a better strategy:

```text
generate candidate plans
evaluate candidate states
keep promising paths
discard bad paths
backtrack when needed
```

For web data extraction, this can help when:

```text
there are multiple possible pages,
several extraction strategies,
ambiguous labels,
missing fields,
or uncertain action sequences.
```

However, ToT alone is not enough because web actions are not just text thoughts. They affect a real environment. A web agent must know which actions are reversible, safe, and grounded in the current page.

---

## Important concepts to remember

### 1. Thought

A “thought” is a coherent unit of intermediate reasoning.

It can be:

```text
a line of arithmetic,
a short plan,
a candidate word,
a subgoal,
or a partial solution.
```

For web agents, a thought could be:

```text
Search within the page first.
Open the product details page.
Use the table header to identify the price column.
Verify that the extracted value is not an advertisement.
```

### 2. Thought decomposition

The problem must be broken into useful thought steps.

The paper emphasizes that a thought should be:

```text
small enough to generate diverse alternatives
large enough to evaluate meaningfully
```

For web agents, this maps to choosing the right level of planning:

```text
too small: one token or one pixel
too large: complete full workflow without feedback
good level: one action/subgoal at a time
```

### 3. Thought generation

The model generates candidate thoughts from the current state.

Two strategies:

```text
sample thoughts independently
or propose multiple candidates sequentially
```

### 4. Thought evaluation

The model evaluates whether a thought/state is promising.

This can be:

```text
value scoring
voting
classification such as sure / likely / impossible
```

For web agents, this is similar to evaluating whether a candidate action is likely to progress toward task completion.

### 5. Search algorithm

ToT can use:

```text
breadth-first search
depth-first search
backtracking
pruning
```

For web agents, this connects to long-horizon planning and action search.

### 6. Lookahead and backtracking

ToT enables the model to look ahead and backtrack, which standard CoT does not.

For web agents, this is important but risky because not all browser actions are reversible.

---

## Key evidence from the paper

### Figure 1 — From IO/CoT/CoT-SC to ToT

Figure 1 compares four approaches:

```text
Input-output prompting
Chain-of-thought
Self-consistency with CoT
Tree of Thoughts
```

The figure shows that ToT explicitly explores multiple intermediate thoughts rather than sampling only one chain or voting only at the final answer.

### Section 3 — ToT framework

Section 3 formalizes ToT through four design questions:

```text
1. How to decompose thoughts?
2. How to generate thoughts?
3. How to evaluate states?
4. What search algorithm to use?
```

These four questions are directly useful for designing web-agent planners.

### Table 1 — Task overview

Table 1 shows that different tasks require different thought units:

```text
Game of 24 → intermediate equations
Creative Writing → writing plans
Crosswords → candidate words
```

For web agents, this implies that thought/action decomposition must be task-specific.

### Game of 24 result

The paper reports:

```text
GPT-4 + CoT: 4% success
ToT: 74% success
```

This is the strongest headline result.

### Creative Writing result

ToT improves coherence by generating multiple plans and voting for the best plan before writing.

This supports the idea that planning before generation improves quality.

### Mini Crosswords result

ToT improves letter, word, and game success over IO and CoT, showing usefulness in a harder search task.

### Ablations

The paper shows that pruning and backtracking matter. Removing them reduces performance, supporting the claim that search structure is important.

---

## Connection to earlier and later papers

### Connection to Chain-of-Thought

CoT generates one reasoning path.

```text
CoT:
input → thought 1 → thought 2 → answer
```

ToT generalizes this:

```text
ToT:
input → multiple candidate thoughts → evaluate → search → answer
```

### Connection to Self-Consistency

Self-consistency samples many complete chains and votes at the end.

ToT samples and evaluates at intermediate steps.

```text
Self-consistency = final-answer aggregation
ToT = intermediate-state search
```

### Connection to Least-to-Most

Least-to-most decomposes a task into subproblems.

ToT adds search among possible decompositions or partial solutions.

### Connection to ReAct

ReAct adds environment actions and observations.

ToT adds search and backtracking.

For web agents, the future direction is combining both:

```text
ReAct = act and observe
ToT = search over thoughts
LATS = search over reasoning + acting + feedback
```

### Connection to LATS

LATS can be seen as a web/agent-oriented extension of ToT:

```text
ToT: search over thoughts
LATS: search over reasoning-action trajectories with environment feedback
```

---

## Connection to later thesis sections

- **S3 — LLM Agent Architectures:**
  ToT is an agent-relevant planning architecture, even if it is not a full interactive web agent.

- **S5.3 — Planning and Decision-Making:**
  ToT is one of the most important foundations for tree-based planning and deliberate search.

- **S5.5 — Limitations and Failure Modes:**
  ToT highlights cost, bad self-evaluation, search explosion, and wrong pruning.

- **S8 — Deployment Realities:**
  ToT has high inference cost and token usage, which matters for deployed web agents.

---

## Limitation connected to thesis

Tree of Thoughts improves deliberate reasoning, but it does not solve grounded web planning.

For my thesis, the full web-agent loop is:

```text
instruction → observation → planning/search → grounded action → feedback → correction → extraction → verification
```

ToT mainly improves:

```text
planning/search over thoughts
```

It does not directly solve:

- DOM grounding,
- visual UI grounding,
- action execution,
- irreversible web actions,
- dynamic page state,
- success verification,
- browser tool latency,
- or safety constraints.

Therefore, ToT should be used as a planning foundation, but web automation requires extensions that combine tree search with environment feedback, tool execution, and safe control.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High
- **Main use:** Foundation for deliberate planning and search
- **Most important parts:**
  - Abstract
  - Figure 1
  - Section 3: Tree of Thoughts framework
  - Thought decomposition/generation/evaluation
  - Algorithms 1 and 2
  - Table 1
  - Game of 24 results
  - Creative Writing results
  - Mini Crosswords results
  - Ablations and limitations

---

## One-sentence summary

Tree of Thoughts turns LLM reasoning from a single chain into a searchable tree of intermediate thoughts, which is useful for planning but must be grounded in browser observations and safe actions before it can support reliable web automation.

---

## BibTeX

```bibtex
@article{yao2023tree,
  title   = {Tree of Thoughts: Deliberate Problem Solving with Large Language Models},
  author  = {Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Thomas L. and Cao, Yuan and Narasimhan, Karthik},
  journal = {arXiv preprint arXiv:2305.10601},
  year    = {2023},
  doi     = {10.48550/arXiv.2305.10601}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2305.10601
- Code: https://github.com/ysymyth/tree-of-thought-llm


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\P1\2023-09-Cognitive Architectures for Language Agents.md

# Paper 72 — Cognitive Architectures for Language Agents

## Metadata

- **Title:** Cognitive Architectures for Language Agents
- **Authors:** Theodore R. Sumers, Shunyu Yao, Karthik Narasimhan, Thomas L. Griffiths
- **Year:** 2024
- **First arXiv version:** 2023
- **Venue:** Transactions on Machine Learning Research (TMLR), 02/2024
- **OpenReview ID:** 1i6ZCvflQJ
- **DOI:** Not listed in the uploaded paper / no DOI found in the paper
- **arXiv ID:** arXiv:2309.02427
- **Thesis section:** S3 — LLM Agent Architectures
- **Cross-links:** S5.2 — Grounding and Interface Representation; S5.3 — Planning and Decision-Making; S5.4 — Training and Learning; S5.5 — Failure Modes; S8 — Deployment
- **Category:** AGT / COGNITIVE ARCHITECTURE / SURVEY
- **Paper type:** Conceptual framework / survey / architecture
- **Priority:** P1
- **BibTeX key:** sumers2024cognitive

---

## Simple understanding

This paper introduces **CoALA**: **Cognitive Architectures for Language Agents**.

The paper is not mainly a new benchmark or a new agent system. It is a conceptual framework for organizing language agents.

The authors argue that recent LLM agents are becoming more complex, but the field lacks common vocabulary and design principles. Different papers use words such as “tool use,” “actions,” “memory,” “grounding,” “reasoning,” and “planning” in inconsistent ways.

CoALA solves this by borrowing ideas from cognitive science and symbolic AI. It defines a language agent in terms of:

```text
memory
action space
decision-making procedure
```

It divides actions into:

```text
internal actions: reasoning, retrieval, learning
external actions: grounding actions in the world
```

For my thesis, CoALA is very important because it gives a clean conceptual structure for discussing web agents. A web agent is not just an LLM with a browser. It is a cognitive architecture with memory, internal reasoning, external actions, perception, grounding, and decision cycles.

---

## Notes

- **Core idea:**
  Proposes CoALA, a conceptual framework that organizes language agents around modular memories, structured action spaces, and repeated decision-making cycles.

- **Key finding:**
  CoALA shows that many recent LLM agents can be described using a small set of architectural concepts: working memory, long-term memory, internal actions, external actions, grounding, retrieval, reasoning, learning, planning, and execution.

- **Limitation:**
  CoALA is a conceptual framework rather than an implemented web-agent system.
  For web agents, this matters because it helps organize the literature, but it does not by itself solve DOM grounding, UI control, verification, or deployment reliability.

- **Additional limitation:**
  CoALA is broad and abstract.
  For web agents, this matters because the thesis must instantiate the framework into web-specific components such as browser observations, DOM memory, screenshot grounding, click/type actions, extraction schemas, and verification rules.

- **Additional limitation:**
  CoALA emphasizes architecture but not benchmark-level performance.
  For web agents, this matters because a clear architecture must still be evaluated on realistic websites, dynamic pages, long-horizon workflows, and extraction tasks.

- **Additional limitation:**
  CoALA’s memory/action categories do not automatically solve memory selection.
  For web agents, this matters because long web histories, repeated observations, and noisy pages require relevance filtering, summarization, and evidence tracking.

- **Additional limitation:**
  CoALA does not fully specify safety constraints for external actions.
  For web agents, this matters because actions such as submitting forms, logging in, sending messages, and making purchases require permission and risk controls.

- **Connects to:**
  ReAct, Reflexion, Toolformer, MRKL, Generative Agents, Voyager, WebGPT, web navigation systems, memory-augmented agents, and modular agent frameworks.

- **Use in thesis:**
  Use CoALA as the organizing conceptual framework for S3. It can help define what an LLM-based web agent is: an LLM embedded in a cognitive architecture with memory, internal actions, external actions, grounding, retrieval, learning, and decision-making.

- **BibTeX key:**
  sumers2024cognitive

---

## Thesis-ready paragraph

Sumers et al. proposed Cognitive Architectures for Language Agents (CoALA), a conceptual framework that organizes LLM-based agents using ideas from cognitive science and symbolic AI. CoALA represents language agents as systems with memory components, structured action spaces, and repeated decision-making procedures. It distinguishes between internal actions, such as reasoning, retrieval, and learning over memory, and external actions, such as interacting with environments through grounding. This framework is highly relevant for web automation because a web agent must maintain working memory, retrieve prior information, reason over page state, execute browser actions, and update its internal state after observations. However, CoALA remains a general conceptual framework rather than a complete web-agent implementation. Its thesis-relevant value is that it provides a vocabulary and architecture for organizing later work, while leaving web-specific problems—DOM grounding, visual interface representation, action safety, verification, and deployment constraints—to be solved by specialized systems.

---

## Why this paper matters for my thesis

This paper matters because it gives me a vocabulary for describing LLM agents clearly.

Without a framework, many papers look different:

```text
ReAct talks about thoughts/actions/observations.
Reflexion talks about memory/reflection.
Toolformer talks about tool calls.
MRKL talks about routers and experts.
WebGPT talks about browsing.
Voyager talks about skill memory.
```

CoALA helps unify them.

For web agents, I can describe the system as:

```text
Working memory:
current page, current task, recent actions, extracted fields

Long-term memory:
past websites, prior failures, reusable workflows, user preferences

Internal actions:
reason, retrieve memory, reflect, update plan

External actions:
click, type, scroll, search, call API, extract table

Decision-making:
propose actions → evaluate actions → select action → execute → observe
```

This is extremely useful for writing the S3 section and connecting it to S5.

---

## Important concepts to remember

### 1. Cognitive architecture

A cognitive architecture is a structured model of how an intelligent system stores information, selects actions, learns, and interacts with its environment.

For web agents, this means the architecture should specify:

```text
what the agent remembers,
what actions it can take,
how it chooses actions,
how it learns from outcomes,
and how it grounds actions in the web environment.
```

### 2. CoALA

CoALA means:

```text
Cognitive Architectures for Language Agents
```

It is a framework for describing and designing LLM-based agents.

### 3. Memory

CoALA distinguishes:

```text
working memory
long-term memory
```

Long-term memory can include:

```text
episodic memory
semantic memory
procedural memory
```

For web agents:

```text
episodic memory = past action trajectories
semantic memory = facts about websites/tasks
procedural memory = reusable workflows or skills
```

### 4. Action space

CoALA divides actions into:

```text
internal actions
external actions
```

Internal actions modify the agent’s internal state.

External actions interact with the world.

### 5. Internal actions

Internal actions include:

```text
reasoning
retrieval
learning
```

For a web agent:

```text
reasoning = decide next step
retrieval = recall previous page/task info
learning = store a new workflow or failure lesson
```

### 6. External actions

External actions are grounded interactions with the environment.

For web agents:

```text
click
type
scroll
submit
open URL
download file
call browser tool
extract DOM
```

### 7. Decision cycle

CoALA describes the agent as running repeated decision cycles:

```text
observe
retrieve/reason
propose action
evaluate action
select action
execute action
observe again
```

This is directly aligned with web automation.

---

## Key evidence from the paper

### Figure 1 — NLP model vs language agent vs cognitive language agent

Figure 1 distinguishes:

```text
A. LLM as text input-output model
B. Language agent in environment feedback loop
C. Cognitive language agent with memory, retrieval, learning, reasoning, actions
```

This figure is useful for the thesis because it visually explains the move from S2 to S3.

### Figure 4 — CoALA framework

Figure 4 presents the full CoALA architecture:

```text
decision procedure
working memory
procedural memory
semantic memory
episodic memory
retrieval
learning
reasoning
grounding
external environment
```

This is one of the most important figures for S3.

### Figure 5 — Action space

Figure 5 divides agent actions into:

```text
internal actions: reasoning, retrieval, learning
external actions: grounding
```

This distinction is useful for web agents because browser actions are external while reasoning and memory operations are internal.

### Section 4 — CoALA framework

Section 4 is the core section. It defines memory, action, and decision-making as the main architectural dimensions.

### Section 6 — Actionable insights

Section 6 argues that language agents should be modular, with reusable abstractions such as Memory, Action, and Agent classes.

This is very relevant for deployment and software engineering of web agents.

---

## Connection to earlier and later papers

### Connection to ReAct

ReAct is one example inside CoALA:

```text
working memory: current observation and reasoning trace
external action: environment action
decision cycle: thought → action → observation
```

### Connection to Reflexion

Reflexion fits CoALA as:

```text
episodic memory
learning action
reflection over failed trajectories
```

### Connection to Toolformer

Toolformer fits CoALA as tool/external action selection, but with tool calls embedded in language generation.

### Connection to MRKL

MRKL fits CoALA as a modular action/expert architecture with routing.

### Connection to LATS

LATS adds explicit planning/search to CoALA’s decision procedure.

### Connection to web agents

Web agents instantiate CoALA with:

```text
external environment = browser/web
external actions = click/type/scroll/search/extract
working memory = page state and task state
long-term memory = prior web knowledge and trajectories
grounding = DOM nodes, screenshots, coordinates
```

---

## Connection to later thesis sections

- **S3 — LLM Agent Architectures:**
  CoALA provides the conceptual vocabulary for the whole section.

- **S5.2 — Perception, Grounding, and Interface Representation:**
  CoALA’s grounding action concept maps directly to DOM and visual grounding.

- **S5.3 — Planning and Decision-Making:**
  CoALA’s decision procedure organizes planning, proposal, evaluation, selection, and execution.

- **S5.4 — Training Strategies and Generalization:**
  CoALA’s learning actions connect to procedural, semantic, and episodic memory updates.

- **S5.5 — Failure Modes:**
  The framework helps localize failure: memory failure, retrieval failure, reasoning failure, grounding failure, or decision failure.

- **S8 — Deployment Realities:**
  CoALA’s modular design supports reusable engineering abstractions for real agents.

---

## Limitation connected to thesis

CoALA provides the architecture language, but not the web-agent solution.

For my thesis, the full web-agent problem is:

```text
instruction → perception → working memory → reasoning/retrieval → planning → grounded browser action → observation → learning/reflection → extraction → verification
```

CoALA helps describe this loop, but it does not implement:

- DOM parsing,
- screenshot interpretation,
- web benchmarks,
- browser action execution,
- extraction validation,
- safe submission policies,
- anti-loop mechanisms,
- cost control,
- or robust deployment.

Therefore, CoALA should be used as the **conceptual backbone** of S3, while web-specific papers in S4/S5 provide concrete implementations and evaluations.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High
- **Main use:** Organizing framework for agent architecture
- **Most important parts:**
  - Abstract
  - Figure 1
  - Section 3.3
  - Section 4: CoALA framework
  - Figure 4
  - Figure 5
  - Section 4.1 memory
  - Section 4.2–4.6 actions and decision-making
  - Section 5 case studies
  - Section 6 actionable insights

---

## One-sentence summary

CoALA gives a cognitive-architecture framework for LLM agents based on memory, internal/external actions, and decision cycles, making it a strong conceptual backbone for web-agent architecture but not a full solution to web grounding and verification.

---

## BibTeX

```bibtex
@article{sumers2024cognitive,
  title   = {Cognitive Architectures for Language Agents},
  author  = {Sumers, Theodore R. and Yao, Shunyu and Narasimhan, Karthik and Griffiths, Thomas L.},
  journal = {Transactions on Machine Learning Research},
  year    = {2024},
  eprint  = {2309.02427},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  url     = {https://openreview.net/forum?id=1i6ZCvflQJ}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2309.02427
- OpenReview: https://openreview.net/forum?id=1i6ZCvflQJ


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\P1\2023-09-The Rise and Potential of Large Language Model Based Agents A Survey.md

# Paper 74 — The Rise and Potential of Large Language Model Based Agents: A Survey

## Metadata

- **Title:** The Rise and Potential of Large Language Model Based Agents: A Survey
- **Authors:** Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang, Junzhe Wang, Senjie Jin, Enyu Zhou, Rui Zheng, Xiaoran Fan, Xiao Wang, Limao Xiong, Yuhao Zhou, Weiran Wang, Changhao Jiang, Yicheng Zou, Xiangyang Liu, Zhangyue Yin, Shihan Dou, Rongxiang Weng, Wensen Cheng, Qi Zhang, Wenjuan Qin, Yongyan Zheng, Xipeng Qiu, Xuanjing Huang, Tao Gui
- **Year:** 2023
- **Latest arXiv version in uploaded PDF:** 2023
- **Venue:** arXiv survey / Fudan NLP Group
- **DOI:** 10.48550/arXiv.2309.07864
- **arXiv ID:** arXiv:2309.07864
- **Thesis section:** S3 — LLM Agent Architectures
- **Cross-links:** S5.1 — Evaluation; S5.2 — Perception; S5.3 — Planning; S5.4 — Memory/Generalization; S5.5 — Failure Modes; S7 — Risks; S8 — Open Challenges
- **Category:** SUR / AGENT SURVEY / TAXONOMY
- **Paper type:** Survey / taxonomy / conceptual framework
- **Priority:** P1
- **BibTeX key:** xi2023rise

---

## Simple understanding

This paper is a broad survey of **LLM-based agents**.

It starts from the general concept of agents, then explains why LLMs are suitable as the “brain” of agents. It proposes a general framework with three main parts:

```text
brain → perception → action
```

The **brain** includes natural language interaction, knowledge, memory, reasoning, planning, transferability, and generalization.

The **perception** module expands the input space beyond text, including visual, auditory, and other modalities.

The **action** module expands the output space beyond text, including tool use and embodied action.

For my thesis, this paper is important because it provides a broad taxonomy for LLM agents and helps position web agents as one application area inside the larger agent literature.

---

## Notes

- **Core idea:**
  Surveys LLM-based agents and proposes a general conceptual framework composed of brain, perception, and action modules.

- **Key finding:**
  The survey argues that LLMs are suitable foundations for agents because they provide natural language interaction, knowledge, memory, reasoning, planning, transferability, generalization, and social ability. It organizes agent applications into single-agent systems, multi-agent systems, human-agent cooperation, and agent societies.

- **Limitation:**
  The survey is broad rather than web-specific.
  For web agents, this matters because it provides useful general categories but does not deeply analyze DOM grounding, browser automation, web extraction benchmarks, anti-bot constraints, or deployment issues specific to the web.

- **Additional limitation:**
  The brain-perception-action framework is high-level.
  For web agents, this matters because each component must be concretized into technical mechanisms: DOM parsing, screenshot encoding, click actions, form filling, extraction schemas, memory retrieval, and validation.

- **Additional limitation:**
  The survey covers many applications, including agent societies, which are not central to my thesis.
  For web automation, the useful parts are mainly construction, perception/action expansion, reasoning/planning, evaluation, and risks.

- **Additional limitation:**
  The survey identifies security and trustworthiness risks but does not provide concrete mitigation mechanisms for browser agents.
  For web agents, this matters because autonomous web actions can cause privacy leaks, harmful scraping, wrong submissions, or unauthorized operations.

- **Additional limitation:**
  The survey emphasizes potential and breadth.
  For web agents, this matters because my thesis should also emphasize practical bottlenecks: robustness, verification, long-horizon reliability, grounding, latency, and cost.

- **Connects to:**
  CoALA, autonomous agent surveys, ReAct, Reflexion, Toolformer, MRKL, web agents, multi-agent systems, human-agent collaboration, and agent safety literature.

- **Use in thesis:**
  Use this survey as a high-level taxonomy of LLM-based agents. It is useful for defining the components of an LLM agent and for positioning web automation within the broader agent landscape.

- **BibTeX key:**
  xi2023rise

---

## Thesis-ready paragraph

Xi et al. provide a comprehensive survey of large language model based agents, framing them as systems composed of a brain, perception module, and action module. In this framework, the LLM-based brain supports natural language interaction, knowledge use, memory, reasoning, planning, transferability, and generalization; perception expands the agent’s input space beyond text; and action expands the output space through tools and embodied behavior. This taxonomy is useful for situating web agents within the broader LLM-agent literature: a web agent must perceive web environments, reason and plan through an LLM-centered brain, and act through browser operations or tools. However, the survey is broad and not web-specific. It does not deeply address the technical problems that dominate generalized web automation and data extraction, such as DOM grounding, visual UI representation, structured extraction, action verification, anti-loop mechanisms, privacy constraints, and deployment cost. Therefore, the survey provides a high-level conceptual map, while later web-specific sections must analyze concrete architectures, benchmarks, and failure modes.

---

## Why this paper matters for my thesis

This paper matters because it helps define what an LLM-based agent is.

The survey says an agent can be understood through:

```text
brain
perception
action
```

For my thesis, this maps naturally to web automation:

```text
Brain:
LLM reasoning, planning, memory, task understanding

Perception:
HTML, DOM, screenshots, page text, browser state, documents

Action:
click, type, scroll, search, call APIs, extract data, submit forms
```

This gives a clean way to introduce web agents later.

The paper also helps distinguish a web agent from a chatbot:

```text
chatbot = mostly text input → text output
web agent = environment perception → decision-making → external action → feedback
```

---

## Important concepts to remember

### 1. Agent

The paper follows the AI view of an agent as an entity that:

```text
perceives its environment
makes decisions
takes actions
```

For web automation:

```text
environment = website/browser
perception = DOM/screenshot/page text
decision = choose action or extraction step
action = browser/tool operation
```

### 2. Brain

The brain is the controller of the agent.

It includes:

```text
natural language interaction
knowledge
memory
reasoning
planning
transferability
generalization
```

For web agents, this corresponds to the LLM-centered decision module.

### 3. Perception

Perception expands the agent’s input space.

The survey discusses:

```text
textual input
visual input
auditory input
other input
```

For web agents, the most important are:

```text
textual input: HTML, page text, DOM labels
visual input: screenshots, layout, icons, tables
```

### 4. Action

Action expands what the agent can do.

The survey discusses:

```text
textual output
tool use
embodied action
```

For web agents:

```text
tool use = search, browser, APIs
embodied action = clicking/typing/scrolling in the browser
```

### 5. Agent society

The paper also discusses multi-agent systems and agent societies.

For my thesis, this is background only unless I discuss multi-agent web automation.

### 6. Human-agent cooperation

The survey discusses instructor-executor and equal partnership paradigms.

For web agents, this matters when the system asks for clarification, permission, or human approval before risky actions.

---

## Key evidence from the paper

### Figure 1 — Envisioned agent society

Figure 1 shows agents acting in a simulated society with cooperation, tool use, planning, and human participation.

For the thesis, this is less central than web automation, but it helps illustrate the broad agent vision.

### Figure 2 — General framework of LLM-based agent

Figure 2 is the most important figure for my thesis.

It shows:

```text
environment → perception → brain → action → environment
```

The brain includes:

```text
memory
knowledge
decision making
planning/reasoning
```

The action module includes:

```text
text
tools
embodiment
```

This is directly useful for defining the basic structure of web agents.

### Figure 3 — Typology of the brain module

Figure 3 categorizes the brain module into:

```text
natural language interaction
knowledge
memory
reasoning and planning
transferability and generalization
```

This helps organize S3 and S5.

### Section 3 — Construction of LLM-based agents

Section 3 is the most relevant part for S3 because it explains how LLM agents are constructed.

### Section 6 — Discussion

Section 6 is useful for thesis gaps because it discusses evaluation, security, trustworthiness, scaling, and open problems.

---

## Connection to earlier and later papers

### Connection to S2 foundations

S2 explains the abilities of LLMs:

```text
language understanding
instruction following
reasoning
alignment
long-context
multimodality
```

This survey explains how those abilities are placed into an agent framework.

### Connection to ReAct

ReAct is an example of the action/feedback loop inside the action and brain modules.

### Connection to Reflexion

Reflexion is part of memory and planning/reflection.

### Connection to Toolformer and MRKL

Toolformer and MRKL are examples of tool-using action modules.

### Connection to CoALA

CoALA gives a more precise cognitive architecture vocabulary.

This survey gives a broader taxonomy:

```text
Xi et al. = broad agent landscape
CoALA = detailed cognitive architecture framework
```

### Connection to web agents

The survey positions web agents as a type of LLM-based agent with:

```text
digital environment
text/visual perception
tool/browser actions
planning and memory
```

---

## Connection to later thesis sections

- **S3 — LLM Agent Architectures:**
  Use this survey to introduce broad LLM-agent construction.

- **S5.1 — Web Agent Benchmarks and Evaluation:**
  The survey discusses agent evaluation dimensions such as utility, sociability, values, and continual evolution.

- **S5.2 — Perception, Grounding, and Interface Representation:**
  Its perception module supports the discussion of textual, visual, and multimodal inputs.

- **S5.3 — Planning and Decision-Making:**
  The brain module includes reasoning and planning.

- **S5.4 — Training Strategies and Generalization:**
  The brain module includes memory, transferability, generalization, and continual learning.

- **S5.5 — Limitations and Failure Modes:**
  Broad agent risks and failures feed into failure taxonomy.

- **S7 — Security, Robustness, and Trustworthiness:**
  The survey discusses adversarial robustness, trustworthiness, and risks.

- **S8 — Open Challenges and Deployment Realities:**
  The survey’s open problems help frame deployment challenges.

---

## Limitation connected to thesis

This survey gives a broad map, but it does not solve the specific technical problems of generalized web automation.

For my thesis, a web agent requires:

```text
browser environment perception
DOM and visual grounding
action execution
state tracking
task planning
structured extraction
verification
privacy/safety control
deployment reliability
```

The survey mainly gives:

```text
general agent taxonomy
high-level construction framework
broad application categories
open problems
```

Therefore, it should be used to position the thesis, not as direct evidence that web automation is solved.

---

## Reading decision

- **Read fully?** No, selective deep reading
- **Depth needed:** Medium-high
- **Main use:** Broad taxonomy and positioning
- **Most important parts:**
  - Abstract
  - Introduction
  - Figure 2
  - Figure 3
  - Section 3: construction of LLM-based agents
  - Section 3.1: brain
  - Section 3.2: perception
  - Section 3.3: action
  - Section 6.2: evaluation
  - Section 6.3: security/trustworthiness
  - Section 6.5: open problems

---

## One-sentence summary

This survey organizes LLM-based agents around brain, perception, and action modules, providing a broad taxonomy that helps position web agents, but it remains too general to address web-specific grounding, extraction, verification, and deployment challenges.

---

## BibTeX

```bibtex
@article{xi2023rise,
  title   = {The Rise and Potential of Large Language Model Based Agents: A Survey},
  author  = {Xi, Zhiheng and Chen, Wenxiang and Guo, Xin and He, Wei and Ding, Yiwen and Hong, Boyang and Zhang, Ming and Wang, Junzhe and Jin, Senjie and Zhou, Enyu and Zheng, Rui and Fan, Xiaoran and Wang, Xiao and Xiong, Limao and Zhou, Yuhao and Wang, Weiran and Jiang, Changhao and Zou, Yicheng and Liu, Xiangyang and Yin, Zhangyue and Dou, Shihan and Weng, Rongxiang and Cheng, Wensen and Zhang, Qi and Qin, Wenjuan and Zheng, Yongyan and Qiu, Xipeng and Huang, Xuanjing and Gui, Tao},
  journal = {arXiv preprint arXiv:2309.07864},
  year    = {2023},
  doi     = {10.48550/arXiv.2309.07864}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2309.07864
- Repository: https://github.com/WooooDyy/LLM-Agent-Paper-List


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\P1\2023-10-Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models.md

# Paper 73 — Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models

## Metadata

- **Title:** Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models
- **Authors:** Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang
- **Year:** 2024
- **First arXiv version:** 2023
- **Venue:** Proceedings of the 41st International Conference on Machine Learning (ICML 2024), PMLR 235
- **DOI:** 10.48550/arXiv.2310.04406
- **arXiv ID:** arXiv:2310.04406
- **Thesis section:** S3 — LLM Agent Architectures
- **Cross-links:** S5.3 — Planning and Decision-Making; S5.4 — Training/Gradient-free Improvement; S5.5 — Failure Modes; S8 — Deployment Realities
- **Category:** REA / PLANNING / SEARCH / AGENT
- **Paper type:** Method / search-based agent framework
- **Priority:** P1
- **BibTeX key:** zhou2024language

---

## Simple understanding

This paper introduces **Language Agent Tree Search (LATS)**.

LATS combines several ideas:

```text
ReAct → reasoning + acting
Tree of Thoughts → search over multiple paths
Reflexion → self-reflection from failed attempts
MCTS → principled tree search
environment feedback → observations after actions
```

The main idea is that an LLM agent should not greedily follow one trajectory. It should search over possible reasoning-action trajectories, evaluate them, use environment feedback, and backpropagate useful values through the search tree.

LATS uses **Monte Carlo Tree Search (MCTS)** to plan over language-agent trajectories.

For my thesis, LATS is extremely relevant because it directly targets the weakness of simple ReAct-style agents: they act reflexively and do not plan ahead enough. Web automation often requires planning under uncertainty, evaluating alternatives, and learning from feedback.

---

## Notes

- **Core idea:**
  Proposes LATS, a Monte Carlo Tree Search framework that unifies reasoning, acting, planning, self-reflection, and external feedback for language agents.

- **Key finding:**
  LATS improves performance across programming, interactive QA, web navigation, and math. The paper reports 92.7% pass@1 on HumanEval with GPT-4, and an average score of 75.9 on WebShop with GPT-3.5. It also improves over ReAct on HotPotQA and WebShop.

- **Limitation:**
  LATS has higher computational cost than simpler methods such as ReAct or Reflexion.
  For web agents, this matters directly because each tree expansion may require extra LLM calls, browser actions, page observations, tool calls, and evaluation prompts, increasing latency and cost.

- **Additional limitation:**
  LATS assumes the ability to revert to earlier states.
  For web agents, this matters because not all web actions are reversible. Submitting a form, sending a message, deleting data, placing an order, or changing account settings may be unsafe to explore through trial and error.

- **Additional limitation:**
  LATS depends on environment feedback and value estimation.
  For web agents, this matters because many websites do not provide clean rewards or clear success signals. The agent may need a separate verifier to determine whether an action or extraction was correct.

- **Additional limitation:**
  LATS still operates in constrained benchmark environments.
  For web agents, this matters because real websites include authentication, CAPTCHAs, dynamic JavaScript, ambiguous UI states, advertisements, anti-bot systems, and layout changes.

- **Additional limitation:**
  LATS can reduce but not eliminate planning errors.
  For web agents, this matters because search over bad candidate actions can still fail if the observation is wrong, the DOM grounding is weak, or the value function misjudges progress.

- **Connects to:**
  ReAct, Reflexion, Tree of Thoughts, RAP, MCTS, WebShop, HotPotQA, HumanEval, web navigation, and planning-based agents.

- **Use in thesis:**
  Use LATS as the strongest S3 P1 bridge between general LLM-agent architectures and web-agent planning. It directly unifies reasoning, acting, and planning, and it includes a web navigation evaluation on WebShop.

- **BibTeX key:**
  zhou2024language

---

## Thesis-ready paragraph

Zhou et al. introduced Language Agent Tree Search (LATS), a framework that unifies reasoning, acting, and planning in language-model agents through Monte Carlo Tree Search. LATS expands ReAct-style agents from a single trajectory into a search tree of possible reasoning-action paths. At each step, the agent samples candidate actions, obtains environment feedback, evaluates states with an LLM-based value function and self-consistency signal, simulates trajectories, backpropagates values, and generates self-reflections after failed attempts. This is highly relevant to LLM-based web automation because web tasks require more than reactive action selection: agents must compare alternatives, plan ahead, adapt to observations, and recover from failure. LATS demonstrates strong results on programming, QA, math, and WebShop web navigation, showing the value of combining search with external feedback. However, its higher computational cost and assumption of reversible states limit direct deployment on real websites, where actions may be irreversible or risky. Therefore, LATS provides a powerful planning architecture for web agents, but it must be combined with safety constraints, action verification, cost control, and web-specific grounding mechanisms.

---

## Why this paper matters for my thesis

This paper matters because it directly addresses a central problem in web automation:

```text
A web agent should not blindly follow the first plan it generates.
```

A ReAct agent may do:

```text
observe → think → act → observe → think → act
```

But LATS does:

```text
observe
→ sample multiple possible actions
→ evaluate them
→ simulate trajectories
→ use feedback
→ backpropagate values
→ reflect on failures
→ choose stronger trajectory
```

For web automation, this is important because a task may have many possible paths:

```text
use site search
use filters
open search result
scroll to table
switch tabs
try another page
extract from DOM
extract from screenshot
verify with external source
```

LATS gives a method for comparing those paths instead of committing too early.

However, real websites are not fully reversible. Therefore, LATS is most useful when combined with:

```text
safe sandboxing
read-only exploration
human approval for risky actions
dry-run planning
action risk classification
state snapshots
verification tools
```

---

## Important concepts to remember

### 1. LATS

LATS means:

```text
Language Agent Tree Search
```

It is an LLM-agent framework that combines:

```text
reasoning
acting
planning
self-reflection
external feedback
memory/search tree
```

### 2. Monte Carlo Tree Search

MCTS is a search algorithm that balances:

```text
exploration: try uncertain actions
exploitation: continue promising paths
```

LATS adapts MCTS to language-agent trajectories.

### 3. Search tree

Each node represents a partial trajectory:

```text
original input
+ previous actions
+ previous observations
```

For web agents, a node can represent:

```text
task + browser state + action history + observations
```

### 4. Expansion

The agent samples multiple candidate actions from the LLM.

For web agents, candidate actions may be:

```text
click a button
type into a field
scroll
open a link
search
extract a table
```

### 5. Evaluation

LATS assigns values to nodes using:

```text
LM score
+ self-consistency score
```

The score guides the search.

### 6. Simulation

The agent continues from a node until a terminal state or budget limit.

For web agents, this is like trying a candidate workflow.

### 7. Backpropagation

The outcome of a trajectory updates values of previous nodes.

This helps the agent learn which earlier choices were promising.

### 8. Reflection

If a trajectory fails, the agent generates a reflection and uses it in future search.

This connects LATS to Reflexion.

---

## Key evidence from the paper

### Figure 1 — LATS overview

Figure 1 shows LATS as a unified framework using external environment feedback and an MCTS-based search algorithm.

This figure is important because it visually shows the combination of reasoning, acting, and planning.

### Table 1 — Comparison with related methods

Table 1 compares:

```text
CoT
ReAct
ToT
RAP
Self-Refine
Beam Search
Reflexion
LATS
```

LATS is marked as combining:

```text
reasoning
acting
planning
self-reflection
external memory
```

This table is very useful for the thesis because it positions LATS as a synthesis of previous methods.

### Section 4 — LATS method

Section 4 explains the operations:

```text
selection
expansion
evaluation
simulation
backpropagation
reflection
```

These operations can map directly to web-agent planning.

### WebShop result

The paper reports that LATS raises the average WebShop score by 22.1 with GPT-3.5 and achieves an average score of 75.9.

This is highly relevant because WebShop is a web navigation benchmark.

### HumanEval result

The paper reports 92.7% pass@1 on HumanEval with GPT-4.

This shows that the search framework is not only useful for web navigation but also for coding.

### Limitations section

The paper explicitly notes two major limitations:

```text
higher computational cost
assumption that states can be reverted
```

Both are directly relevant to real web automation.

---

## Connection to earlier and later papers

### Connection to ReAct

ReAct follows one reasoning-action trajectory.

LATS searches over multiple trajectories.

```text
ReAct = one path
LATS = tree of possible ReAct paths
```

### Connection to Tree of Thoughts

ToT searches over thoughts.

LATS searches over reasoning-action-observation trajectories.

```text
ToT = tree of thoughts
LATS = tree of language-agent actions with feedback
```

### Connection to Reflexion

Reflexion uses self-reflection after failure.

LATS integrates reflection into search.

```text
Reflexion = improve next trial
LATS = use reflection during tree search
```

### Connection to MRKL and Toolformer

MRKL and Toolformer provide tool-use mechanisms.

LATS can plan over tool calls and action choices.

### Connection to web agents

LATS is directly relevant to web agents because it evaluates on WebShop and treats web navigation as a decision-making problem.

---

## Connection to later thesis sections

- **S3 — LLM Agent Architectures:**
  LATS is a key architecture that integrates reasoning, acting, planning, reflection, and feedback.

- **S5.3 — Planning and Decision-Making:**
  LATS is one of the most important planning papers for language agents.

- **S5.4 — Training Strategies and Generalization:**
  LATS is gradient-free; it improves behavior through search and feedback rather than fine-tuning.

- **S5.5 — Failure Modes:**
  It addresses some ReAct failure modes but introduces cost, reversibility, and value-estimation issues.

- **S8 — Deployment Realities:**
  LATS has direct deployment implications: computation, latency, browser action cost, and irreversible actions.

---

## Limitation connected to thesis

LATS improves planning, but it is not directly deployment-ready for unrestricted web automation.

For my thesis, generalized web automation requires:

```text
safe observation
grounded action generation
planning/search
execution
feedback
verification
risk control
cost control
human oversight when needed
```

LATS mainly improves:

```text
planning/search over reasoning-action trajectories
```

It does not fully solve:

- precise DOM grounding,
- screenshot-to-action mapping,
- irreversible actions,
- ambiguous success signals,
- anti-bot barriers,
- long-running browser costs,
- user privacy,
- or production monitoring.

Therefore, LATS should be used as a major planning foundation, but real web agents need safety-aware and deployment-aware adaptations.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Very high
- **Main use:** Planning architecture for agents and web navigation
- **Most important parts:**
  - Abstract
  - Figure 1
  - Table 1
  - Section 3: preliminaries
  - Section 4: LATS method
  - Figure 2: six operations
  - WebShop experiments
  - HotPotQA experiments
  - HumanEval experiments
  - Ablation studies
  - Limitations

---

## One-sentence summary

LATS turns language agents into search-based planners by combining ReAct-style acting, Tree-of-Thought-style search, Reflexion-style feedback, and MCTS, but real web automation still requires safety, grounding, verification, and cost control.

---

## BibTeX

```bibtex
@inproceedings{zhou2024language,
  title     = {Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models},
  author    = {Zhou, Andy and Yan, Kai and Shlapentokh-Rothman, Michal and Wang, Haohan and Wang, Yu-Xiong},
  booktitle = {Proceedings of the 41st International Conference on Machine Learning},
  series    = {Proceedings of Machine Learning Research},
  volume    = {235},
  year      = {2024},
  eprint    = {2310.04406},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  doi       = {10.48550/arXiv.2310.04406}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2310.04406
- Code: https://github.com/lapisrocks/LanguageAgentTreeSearch


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\P1\2025-03 - A Survey on Large Language Model based Autonomous Agents.md

# Paper 76 — A Survey on Large Language Model based Autonomous Agents

## Metadata

- **Title:** A Survey on Large Language Model based Autonomous Agents
- **Authors:** Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhi-Yuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, Ji-Rong Wen
- **Year:** 2025
- **First arXiv version:** 2023
- **Latest arXiv version in uploaded PDF:** 2025
- **Venue:** Frontiers of Computer Science, 2025
- **DOI:** 10.1007/s11704-024-40231-1
- **arXiv ID:** arXiv:2308.11432
- **Thesis section:** S3 — LLM Agent Architectures
- **Cross-links:** S5.1 — Evaluation; S5.3 — Planning; S5.4 — Memory/Training/Capability Acquisition; S5.5 — Failure Modes; S7 — Safety; S8 — Deployment
- **Category:** SUR / AUTONOMOUS AGENTS / TAXONOMY
- **Paper type:** Survey / review / taxonomy
- **Priority:** P1
- **BibTeX key:** wang2025survey

---

## Simple understanding

This paper is a survey of **LLM-based autonomous agents**.

It organizes the field around three big topics:

```text
construction
application
evaluation
```

For construction, it proposes a unified framework with four major modules:

```text
profile
memory
planning
action
```

This is slightly different from the Xi et al. survey, which used:

```text
brain
perception
action
```

This survey focuses more directly on autonomous agent architecture design and capability acquisition.

For my thesis, this paper is important because it gives a clear taxonomy of agent modules:

```text
profile → who the agent is
memory → what the agent remembers
planning → how the agent decides future steps
action → how the agent affects the environment
```

This maps well to web agents, where the agent needs roles, memory, planning, and browser/tool actions.

---

## Notes

- **Core idea:**
  Provides a systematic survey of LLM-based autonomous agents, organized around construction, applications, and evaluation, with a unified architecture framework including profile, memory, planning, and action modules.

- **Key finding:**
  The paper argues that LLM-based agents differ from traditional agents because they use LLMs as central controllers with broad world knowledge, natural language interfaces, memory, planning, and tool/action capabilities. It categorizes agent construction methods and evaluation strategies.

- **Limitation:**
  The survey is broad and covers many types of autonomous agents, not only web agents.
  For web automation, this matters because the general framework must be translated into web-specific design choices: browser profile, web memory, DOM/action planning, extraction tools, and verification.

- **Additional limitation:**
  Survey taxonomies can become quickly outdated.
  For web agents, this matters because web-agent research evolves rapidly, with new benchmarks, multimodal models, and tool-use frameworks appearing frequently.

- **Additional limitation:**
  The framework describes modules but does not prescribe exact implementation.
  For web agents, this matters because memory, planning, and action modules require concrete methods for DOM grounding, state tracking, tool calls, and safe browser execution.

- **Additional limitation:**
  Evaluation remains difficult.
  For web agents, this matters because task success, extraction correctness, safety, robustness, and user trust are hard to measure with one metric.

- **Additional limitation:**
  The survey discusses applications broadly.
  For my thesis, only parts related to architecture, memory, planning, action, evaluation, and challenges should be deeply used.

- **Connects to:**
  CoALA, Xi et al. survey, ReAct, Reflexion, Toolformer, ToT, LATS, Voyager, Generative Agents, WebGPT, Mind2Web, WebShop, and agent evaluation literature.

- **Use in thesis:**
  Use this paper as a modern survey reference for autonomous LLM-agent construction. It is useful for defining agent modules, memory/planning/action taxonomies, and evaluation challenges.

- **BibTeX key:**
  wang2025survey

---

## Thesis-ready paragraph

Wang et al. provide a comprehensive survey of LLM-based autonomous agents, organizing the literature around agent construction, applications, and evaluation. For construction, the paper proposes a unified framework consisting of profile, memory, planning, and action modules. This taxonomy is useful for web automation because a web agent must operate with a task or role profile, maintain short-term and long-term memory over web interactions, plan multi-step workflows, and translate decisions into browser or tool actions. The survey also highlights capability acquisition and evaluation as central problems for autonomous agents. However, because the paper is broad, it does not deeply solve web-specific challenges such as DOM grounding, visual UI understanding, structured extraction, safe execution, or verification. Therefore, it should be used as an architectural and evaluative map for S3, while later sections should focus on web-specific benchmarks, grounding methods, training strategies, and failure modes.

---

## Why this paper matters for my thesis

This paper matters because it gives a practical modular framework:

```text
Profile
Memory
Planning
Action
```

For my thesis, this maps to:

```text
Profile:
task role, domain role, extraction role, user constraints

Memory:
current page history, previous actions, extracted fields, prior failures

Planning:
subgoal decomposition, action sequence, retry strategy

Action:
click, type, scroll, search, extract, validate, store
```

This is very useful for S3 because it helps explain what an autonomous LLM agent contains.

It also helps later sections:

```text
memory → S5.4
planning → S5.3
action → S5.2/S5.3
evaluation → S5.1
challenges → S5.5/S7/S8
```

---

## Important concepts to remember

### 1. Autonomous agent

The paper uses the idea that an autonomous agent is situated in an environment, senses it, acts on it, and pursues goals over time.

For web agents:

```text
environment = browser/web
sensing = page/DOM/screenshot observation
acting = browser/tool operations
goal = user task or extraction objective
```

### 2. Construction

Construction asks:

```text
How should the agent architecture be designed?
How can the agent acquire the capabilities needed for tasks?
```

This is central for S3.

### 3. Profile module

The profile module defines the agent’s role or identity.

For web automation:

```text
“You are a web extraction agent.”
“You are a browser automation assistant.”
“You must prioritize safe read-only actions.”
```

This affects memory, planning, and action.

### 4. Memory module

The memory module stores and retrieves information.

The survey distinguishes memory by:

```text
structure
format
operation
```

For web agents, memory can store:

```text
visited pages
action history
extracted values
failed selectors
successful workflows
user preferences
```

### 5. Planning module

The planning module decomposes tasks and decides future actions.

The survey distinguishes:

```text
planning without feedback
planning with feedback
single-path reasoning
multi-path reasoning
external planners
```

For web agents, planning is central because tasks are long-horizon and interactive.

### 6. Action module

The action module translates plans into outputs.

For web agents:

```text
task completion
communication
exploration
tool use
database access
environment actions
```

### 7. Evaluation

The survey emphasizes that evaluating autonomous agents is difficult and requires subjective/objective strategies.

For web agents, evaluation must include:

```text
task success
step success
extraction accuracy
robustness
safety
cost
latency
generalization
```

---

## Key evidence from the paper

### Figure 1 — Growth trend of LLM-based autonomous agents

Figure 1 shows rapid growth in LLM-agent papers from 2021 to 2023, with categories such as:

```text
tool agent
simulation agent
general agent
embodied agent
game agent
web agent
assistant agent
```

This figure is useful for thesis motivation because it shows the rapid expansion of the field.

### Figure 2 — Unified framework

Figure 2 is the most important figure for S3.

It organizes agent architecture into:

```text
profile
memory
planning
action
```

Each module has subcomponents.

### Section 2.1 — Agent architecture design

This section details the unified framework and is the most relevant part for S3.

### Section 2.1.2 — Memory module

The memory section is useful for S5.4 because it discusses memory structures, formats, and operations.

### Section 2.1.3 — Planning module

The planning section is useful for S5.3 because it compares single-path and multi-path reasoning, feedback-based planning, and external planners.

### Figure 3 — Single-path vs multi-path reasoning

Figure 3 compares strategies such as:

```text
CoT / Zero-shot-CoT
CoT-SC
ToT / RAP
```

This is directly useful for planning discussion.

### Evaluation section

The evaluation discussion is useful for S5.1 because it shows that agent evaluation is broader than simple benchmark accuracy.

---

## Connection to earlier and later papers

### Connection to Xi et al. survey

Xi et al. survey gives:

```text
brain / perception / action
```

Wang et al. survey gives:

```text
profile / memory / planning / action
```

Together, they provide complementary taxonomies.

### Connection to CoALA

CoALA provides a theoretical architecture grounded in cognitive science.

Wang et al. provides a broader empirical taxonomy of autonomous agent modules.

### Connection to ReAct

ReAct is a planning/action method under this taxonomy.

### Connection to Reflexion

Reflexion is memory reflection and feedback-based improvement.

### Connection to Toolformer and MRKL

Toolformer and MRKL belong to action/tool-use architecture.

### Connection to ToT and LATS

ToT and LATS belong to multi-path planning and search.

---

## Connection to later thesis sections

- **S3 — LLM Agent Architectures:**
  Use it as a modern comprehensive survey of autonomous agent construction.

- **S5.1 — Web Agent Benchmarks and Evaluation:**
  Its evaluation discussion helps frame metrics and strategies.

- **S5.3 — Planning and Decision-Making:**
  Its planning module directly supports this section.

- **S5.4 — Training Strategies and Generalization:**
  Memory, capability acquisition, and feedback mechanisms feed this section.

- **S5.5 — Limitations and Failure Modes:**
  Challenges and future directions support the failure/gap discussion.

- **S7 — Security, Robustness, and Trustworthiness:**
  Risks and safety concerns feed into this section.

- **S8 — Deployment Realities:**
  The survey’s discussion of applications and challenges supports deployment framing.

---

## Limitation connected to thesis

This survey is useful for architecture and taxonomy, but it does not directly solve web automation.

For generalized web automation, I still need to address:

```text
DOM grounding
visual grounding
browser control
web-specific memory
site generalization
anti-loop mechanisms
extraction verification
privacy and safe action boundaries
real-time cost and latency
```

The survey mainly gives:

```text
agent construction categories
memory/planning/action taxonomy
applications
evaluation strategies
challenges
```

Therefore, it should be used as a high-level S3 reference and as a bridge to S5, but not as the final evidence for web-agent performance.

---

## Reading decision

- **Read fully?** No, selective deep reading
- **Depth needed:** Medium-high
- **Main use:** Taxonomy of autonomous agent architecture and evaluation
- **Most important parts:**
  - Abstract
  - Figure 1
  - Section 2: construction
  - Figure 2
  - Memory module
  - Planning module
  - Figure 3
  - Action module
  - Evaluation strategies
  - Challenges and future directions

---

## One-sentence summary

This survey organizes LLM-based autonomous agents around profile, memory, planning, and action modules, providing a useful taxonomy for web-agent architecture while leaving web-specific grounding, extraction, verification, and deployment problems unresolved.

---

## BibTeX

```bibtex
@article{wang2025survey,
  title   = {A Survey on Large Language Model based Autonomous Agents},
  author  = {Wang, Lei and Ma, Chen and Feng, Xueyang and Zhang, Zeyu and Yang, Hao and Zhang, Jingsen and Chen, Zhi-Yuan and Tang, Jiakai and Chen, Xu and Lin, Yankai and Zhao, Wayne Xin and Wei, Zhewei and Wen, Ji-Rong},
  journal = {Frontiers of Computer Science},
  year    = {2025},
  doi     = {10.1007/s11704-024-40231-1},
  eprint  = {2308.11432},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2308.11432
- DOI: https://doi.org/10.1007/s11704-024-40231-1


---

## Synthesis / Writing Notes (3 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\Writing\S3_mini_synthesis_from_P0.md

# S3 Mini-Synthesis — LLM Agent Architectures  
## Based on S3 P0 papers: ReAct, Reflexion, Toolformer

## 1. Narrative

Section S3 marks the transition from **LLMs as language models** to **LLMs as agent controllers**.

In S2, the literature showed that LLMs can understand language, follow instructions, reason step by step, use in-context examples, and improve reasoning reliability. However, these capabilities are still mostly internal to the model. S3 begins where S2 stops: it asks how these LLM capabilities can be organized into systems that **act**, **observe**, **use tools**, **remember**, and **recover from failure**.

The three P0 papers in S3 define three core architectural directions:

```text
ReAct → reasoning + acting loop
Reflexion → memory + self-reflection loop
Toolformer → learned tool-use loop
```

Together, they form the basic architecture of modern LLM agents:

```text
Reason → Act → Observe → Reflect → Use tools → Update behavior
```

---

## 2. Paper-level synthesis

### 2.1 ReAct — Reasoning and acting

ReAct introduces the central LLM-agent loop:

```text
Thought → Action → Observation → Thought → Action → Observation
```

This is a major shift from chain-of-thought prompting. In chain-of-thought, the model reasons internally and then gives an answer. In ReAct, the model reasons, acts in an environment, receives observations, and updates its reasoning based on feedback.

For web agents, this is foundational. Web automation naturally follows the ReAct pattern:

```text
observe page → reason about next step → click/type/search → observe result → continue
```

ReAct shows that reasoning and acting are stronger together than either alone. Reasoning helps the agent plan, track progress, and recover from exceptions. Acting gives the agent external evidence that reduces hallucination and grounds reasoning in observations.

However, ReAct still depends heavily on prompts, simplified action spaces, and short trajectories. It can loop, hallucinate thoughts, repeat wrong actions, and fail on complex long-horizon workflows. For web agents, this matters because real websites are dynamic, noisy, multimodal, and often require precise DOM or visual grounding.

---

### 2.2 Reflexion — Memory and self-reflection

Reflexion extends ReAct by adding **memory** and **self-reflection**.

Instead of changing model weights, the agent learns from failure through natural-language reflection. After a failed attempt, the agent writes a reflection explaining what went wrong and stores it in memory. On the next trial, the agent uses this memory to improve its plan.

The basic Reflexion loop is:

```text
Attempt task → fail → reflect → store memory → retry with reflection
```

For web agents, Reflexion is important because failure is common in web automation. Agents may click the wrong element, choose a bad search query, misunderstand a form, loop between pages, or fail to verify an extracted value. Reflexion provides a lightweight mechanism for self-correction without fine-tuning.

However, Reflexion depends on reliable failure detection. Many web tasks do not provide a clear success/failure signal. A form may submit successfully but contain wrong information. An extracted value may look correct but be stale. A purchase or account action may be irreversible. For web agents, this means reflection must be combined with verification, risk detection, safe retry policies, and human oversight.

---

### 2.3 Toolformer — Tool use

Toolformer adds another essential architectural component: **external tool use**.

The paper shows that a language model can learn when to call tools, which tool to call, what arguments to pass, and how to use the result. It does this through self-supervised data generation: the model proposes API calls, executes them, keeps useful calls that reduce prediction loss, and fine-tunes on the resulting tool-augmented data.

For web agents, Toolformer matters because web automation requires tools. A practical web agent may need:

```text
browser tools
search engines
calculators
databases
retrievers
extractors
validators
APIs
file systems
code execution
```

Toolformer shows that tool use can be learned, not only manually scripted.

However, Toolformer does not solve full agentic tool orchestration. It cannot originally chain tools, browse interactively, reformulate failed searches, reason about tool cost, or ground tool calls in UI actions. For web agents, this matters because real workflows often require multi-step tool chains:

```text
search → open page → inspect DOM → extract data → validate → store result
```

Thus, Toolformer is foundational for tool-using agents, but generalized web automation needs planning, feedback, grounding, and verification around tool use.

---

## 3. Main conceptual contribution of S3

The main contribution of S3 is that **agency is a system property**, not a property of the language model alone.

The three P0 papers show that an LLM becomes an agent when it is embedded inside a loop with additional components:

| Agent component | Main paper | Role |
|---|---|---|
| Reasoning-action loop | ReAct | Connects thoughts, actions, and observations |
| Reflection and memory | Reflexion | Enables learning from failure across trials |
| Tool use | Toolformer | Enables external computation, retrieval, and API access |

Together, these papers define the first layer of LLM-agent architecture:

```text
LLM + reasoning traces + actions + observations + tools + memory
```

This is the foundation for later web agents.

---

## 4. S3 narrative arc

The S3 narrative can be written as a progression:

```text
Step 1 — ReAct:
LLMs can reason and act in an interleaved loop.

Step 2 — Reflexion:
LLM agents can use verbal memory to learn from failed attempts.

Step 3 — Toolformer:
LLMs can learn to call external tools to overcome internal limitations.
```

This gives the section a clear structure:

```text
Reasoning + Acting
→ Reflection + Memory
→ Tool Use
```

Or more generally:

```text
interactive agency
→ self-correction
→ external capability extension
```

This progression prepares the transition from general agent architectures to web-specific agents in later sections.

---

## 5. Refined gap after S3 P0

After S2, the gap was:

```text
LLMs are strong at language reasoning, but weak as grounded, reliable, interactive web agents.
```

After S3 P0, the gap becomes more precise:

```text
Early LLM-agent architectures introduce reasoning-action loops, memory, reflection, and tool use, but they still do not fully solve grounded, reliable, safe, and scalable web automation.
```

These papers show that LLM agents can:

```text
reason before acting
act in environments
observe feedback
call tools
learn from failed trials
store verbal memories
reduce some hallucinations
improve interpretability
```

But they do not fully solve:

```text
precise DOM grounding
visual UI grounding
dynamic website interaction
long-horizon web workflows
tool-chain orchestration
robust success verification
safe irreversible actions
memory reliability
cost and latency
generalization across unseen websites
```

So the refined S3 gap is:

```text
LLM-agent architectures provide the control loop, but generalized web automation requires grounding, verification, robust planning, safety constraints, and deployment-aware orchestration.
```

---

## 6. Thesis connection

For the thesis topic, **“LLM-based agents for generalized web automation and data extraction,”** S3 supports four major claims.

### Claim 1 — Web agents need an interactive control loop

ReAct shows that LLMs must not only reason internally. They must connect reasoning to actions and observations. This is the basic structure of web automation:

```text
observe → reason → act → observe again
```

### Claim 2 — Web agents need memory and recovery

Reflexion shows that agents can improve through verbal memory and self-reflection. This is important because web agents fail often and need mechanisms to recover from wrong clicks, bad searches, incomplete extraction, and long-horizon planning errors.

### Claim 3 — Web agents need external tools

Toolformer shows that LLMs can learn to use tools through API calls. This is essential because web agents need browsers, search, calculators, retrievers, validators, databases, and other external tools.

### Claim 4 — Architecture is not enough without grounding and verification

The S3 papers introduce agent loops, but they do not fully solve grounding and verification. For web automation, the agent must connect high-level reasoning to exact web elements, tool results, extracted values, and success criteria.

---

## 7. Thesis-ready synthesis paragraph

LLM agent architectures extend foundation language models by embedding them in interactive control loops. ReAct introduces the central reasoning-action-observation pattern, allowing an LLM to reason about the current state, execute an action, receive environmental feedback, and update its next decision. This moves LLMs beyond static chain-of-thought reasoning toward interactive task solving. Reflexion adds a self-improvement mechanism by storing natural-language reflections after failed trials and using them as memory for future attempts, enabling agents to recover from repeated mistakes without updating model weights. Toolformer adds external tool use by training language models to decide when and how to call APIs, allowing them to overcome limitations in arithmetic, factual lookup, temporal awareness, and translation. Together, these works establish the core architectural components of LLM-based agents: reasoning, action, observation, memory, reflection, and tool use. For generalized web automation and data extraction, these components are necessary but insufficient. Real web agents must also solve precise DOM and visual grounding, dynamic browser interaction, long-horizon state tracking, safe action execution, robust verification of extracted data, and deployment constraints such as cost, latency, and tool reliability. Thus, S3 provides the agentic control foundation that later web-specific systems extend with grounding, planning, evaluation, and safety mechanisms.

---

## 8. Limitations connected to the thesis

### 8.1 ReAct limitation — prompt-based control is fragile

ReAct relies on few-shot prompting and hand-written trajectories.

For web agents, this matters because generalized web automation cannot depend on manually crafted examples for every website, workflow, or task type. Real websites vary in layout, terminology, action space, and interaction rules. This motivates later work on more robust planning, training, memory, and web-specific benchmarks.

### 8.2 ReAct limitation — loops and hallucinated actions

ReAct can repeat actions, enter loops, or produce hallucinated reasoning.

For web agents, this matters because a loop can repeatedly click the wrong element, resubmit a form, or waste browser/tool calls. Hallucinated reasoning can cause the agent to believe it saw a button, field, or value that does not exist. This motivates failure detection, reflection, verification, and safe execution constraints.

### 8.3 Reflexion limitation — success signals are hard

Reflexion depends on detecting failure and using reward or success signals.

For web agents, this matters because many web tasks have ambiguous success criteria. A page may not show a clear success message, extracted data may be partially correct, and some actions cannot be safely retried. This motivates explicit success detectors, validators, human approval, and confidence estimation.

### 8.4 Reflexion limitation — reflection can be wrong

Reflections are natural-language outputs and can themselves be inaccurate.

For web agents, this matters because a wrong reflection can make the next attempt worse. For example, the agent may incorrectly conclude that a website has a certain structure or that a value was extracted from the right field. This motivates memory validation and evidence-grounded reflection.

### 8.5 Toolformer limitation — no chained interactive tool use

Toolformer does not originally support chained tool use or interactive browsing.

For web agents, this matters because web automation normally requires tool chains:

```text
search → browse → inspect → extract → validate → store
```

This motivates later agent architectures that plan and orchestrate multiple tools over several steps.

### 8.6 Toolformer limitation — tool cost is ignored

Toolformer does not account for API cost, latency, or reliability when deciding whether to use a tool.

For web agents, this matters because browser automation may involve expensive API calls, slow page loading, rate limits, CAPTCHA, proxy costs, and tool failures. This motivates deployment-aware agent design.

---

## 9. Cross-links to later sections

| Paper | Feeds |
|---|---|
| ReAct | S5.3 planning, S5.5 failure modes, S6 search/extraction, S8 deployment |
| Reflexion | S5.3 recovery planning, S5.5 loops/failures, S7 safety, S8 retry cost |
| Toolformer | S5.3 tool planning, S6 extraction tools, S7 verification, S8 tool cost/latency |

---

## 10. Transition to S4 and S5

S3 shows how LLMs become agents in general:

```text
reasoning + acting + observation + memory + tools
```

The next question is:

```text
How are these general agent architectures adapted to the web?
```

This transition leads naturally to:

- **S4 — Evolution of Web Agent Systems**
  - How LLM agents moved into browser and web environments.

- **S5.1 — Web Agent Benchmarks and Evaluation**
  - How web-agent success is measured.

- **S5.2 — Perception, Grounding, and Interface Representation**
  - How agents represent DOM, screenshots, UI elements, and web state.

- **S5.3 — Planning and Decision-Making**
  - How agents plan long-horizon web actions.

- **S5.5 — Limitations and Failure Modes**
  - How agents fail through loops, hallucinations, grounding errors, and unsafe actions.

---

## 11. Final S3 mini-synthesis

S3 establishes the architectural foundation of LLM-based agents. ReAct shows that LLMs can interleave reasoning and acting, forming the basic observation-action loop required for interactive task solving. Reflexion adds verbal memory and self-reflection, allowing agents to learn from failed attempts without fine-tuning. Toolformer adds tool use, showing that language models can learn to call APIs to overcome limitations in factuality, arithmetic, temporal awareness, and external knowledge access. Together, these papers define the core components of LLM-agent architecture: reasoning, action, observation, tool use, memory, and reflection.

For generalized web automation and data extraction, these components are essential. A web agent must reason about user goals, act on web pages, observe changes, use tools, remember previous steps, recover from failures, and verify outputs. However, S3 also shows that early LLM-agent architectures remain incomplete for real web environments. They do not fully solve DOM grounding, visual grounding, dynamic interaction, long-horizon reliability, safe action execution, or deployment constraints. Therefore, the literature must next examine how these general agent patterns are adapted, evaluated, and extended in web-specific systems.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\Writing\S3_mini_synthesis_from_P0_updated_cross_links.md

# S3 Mini-Synthesis — LLM Agent Architectures  
## Based on S3 P0 papers: ReAct, Reflexion, Toolformer

## 1. Narrative

Section S3 marks the transition from **LLMs as language models** to **LLMs as agent controllers**.

In S2, the literature showed that LLMs can understand language, follow instructions, reason step by step, use in-context examples, and improve reasoning reliability. However, these capabilities are still mostly internal to the model. S3 begins where S2 stops: it asks how these LLM capabilities can be organized into systems that **act**, **observe**, **use tools**, **remember**, and **recover from failure**.

The three P0 papers in S3 define three core architectural directions:

```text
ReAct → reasoning + acting loop
Reflexion → memory + self-reflection loop
Toolformer → learned tool-use loop
```

Together, they form the basic architecture of modern LLM agents:

```text
Reason → Act → Observe → Reflect → Use tools → Update behavior
```

---

## 2. Paper-level synthesis

### 2.1 ReAct — Reasoning and acting

ReAct introduces the central LLM-agent loop:

```text
Thought → Action → Observation → Thought → Action → Observation
```

This is a major shift from chain-of-thought prompting. In chain-of-thought, the model reasons internally and then gives an answer. In ReAct, the model reasons, acts in an environment, receives observations, and updates its reasoning based on feedback.

For web agents, this is foundational. Web automation naturally follows the ReAct pattern:

```text
observe page → reason about next step → click/type/search → observe result → continue
```

ReAct shows that reasoning and acting are stronger together than either alone. Reasoning helps the agent plan, track progress, and recover from exceptions. Acting gives the agent external evidence that reduces hallucination and grounds reasoning in observations.

However, ReAct still depends heavily on prompts, simplified action spaces, and short trajectories. It can loop, hallucinate thoughts, repeat wrong actions, and fail on complex long-horizon workflows. For web agents, this matters because real websites are dynamic, noisy, multimodal, and often require precise DOM or visual grounding.

---

### 2.2 Reflexion — Memory and self-reflection

Reflexion extends ReAct by adding **memory** and **self-reflection**.

Instead of changing model weights, the agent learns from failure through natural-language reflection. After a failed attempt, the agent writes a reflection explaining what went wrong and stores it in memory. On the next trial, the agent uses this memory to improve its plan.

The basic Reflexion loop is:

```text
Attempt task → fail → reflect → store memory → retry with reflection
```

For web agents, Reflexion is important because failure is common in web automation. Agents may click the wrong element, choose a bad search query, misunderstand a form, loop between pages, or fail to verify an extracted value. Reflexion provides a lightweight mechanism for self-correction without fine-tuning.

However, Reflexion depends on reliable failure detection. Many web tasks do not provide a clear success/failure signal. A form may submit successfully but contain wrong information. An extracted value may look correct but be stale. A purchase or account action may be irreversible. For web agents, this means reflection must be combined with verification, risk detection, safe retry policies, and human oversight.

---

### 2.3 Toolformer — Tool use

Toolformer adds another essential architectural component: **external tool use**.

The paper shows that a language model can learn when to call tools, which tool to call, what arguments to pass, and how to use the result. It does this through self-supervised data generation: the model proposes API calls, executes them, keeps useful calls that reduce prediction loss, and fine-tunes on the resulting tool-augmented data.

For web agents, Toolformer matters because web automation requires tools. A practical web agent may need:

```text
browser tools
search engines
calculators
databases
retrievers
extractors
validators
APIs
file systems
code execution
```

Toolformer shows that tool use can be learned, not only manually scripted.

However, Toolformer does not solve full agentic tool orchestration. It cannot originally chain tools, browse interactively, reformulate failed searches, reason about tool cost, or ground tool calls in UI actions. For web agents, this matters because real workflows often require multi-step tool chains:

```text
search → open page → inspect DOM → extract data → validate → store result
```

Thus, Toolformer is foundational for tool-using agents, but generalized web automation needs planning, feedback, grounding, and verification around tool use.

---

## 3. Main conceptual contribution of S3

The main contribution of S3 is that **agency is a system property**, not a property of the language model alone.

The three P0 papers show that an LLM becomes an agent when it is embedded inside a loop with additional components:

| Agent component | Main paper | Role |
|---|---|---|
| Reasoning-action loop | ReAct | Connects thoughts, actions, and observations |
| Reflection and memory | Reflexion | Enables learning from failure across trials |
| Tool use | Toolformer | Enables external computation, retrieval, and API access |

Together, these papers define the first layer of LLM-agent architecture:

```text
LLM + reasoning traces + actions + observations + tools + memory
```

This is the foundation for later web agents.

---

## 4. S3 narrative arc

The S3 narrative can be written as a progression:

```text
Step 1 — ReAct:
LLMs can reason and act in an interleaved loop.

Step 2 — Reflexion:
LLM agents can use verbal memory to learn from failed attempts.

Step 3 — Toolformer:
LLMs can learn to call external tools to overcome internal limitations.
```

This gives the section a clear structure:

```text
Reasoning + Acting
→ Reflection + Memory
→ Tool Use
```

Or more generally:

```text
interactive agency
→ self-correction
→ external capability extension
```

This progression prepares the transition from general agent architectures to web-specific agents in later sections.

---

## 5. Refined gap after S3 P0

After S2, the gap was:

```text
LLMs are strong at language reasoning, but weak as grounded, reliable, interactive web agents.
```

After S3 P0, the gap becomes more precise:

```text
Early LLM-agent architectures introduce reasoning-action loops, memory, reflection, and tool use, but they still do not fully solve grounded, reliable, safe, and scalable web automation.
```

These papers show that LLM agents can:

```text
reason before acting
act in environments
observe feedback
call tools
learn from failed trials
store verbal memories
reduce some hallucinations
improve interpretability
```

But they do not fully solve:

```text
precise DOM grounding
visual UI grounding
dynamic website interaction
long-horizon web workflows
tool-chain orchestration
robust success verification
safe irreversible actions
memory reliability
cost and latency
generalization across unseen websites
```

So the refined S3 gap is:

```text
LLM-agent architectures provide the control loop, but generalized web automation requires grounding, verification, robust planning, safety constraints, and deployment-aware orchestration.
```

---

## 6. Thesis connection

For the thesis topic, **“LLM-based agents for generalized web automation and data extraction,”** S3 supports four major claims.

### Claim 1 — Web agents need an interactive control loop

ReAct shows that LLMs must not only reason internally. They must connect reasoning to actions and observations. This is the basic structure of web automation:

```text
observe → reason → act → observe again
```

### Claim 2 — Web agents need memory and recovery

Reflexion shows that agents can improve through verbal memory and self-reflection. This is important because web agents fail often and need mechanisms to recover from wrong clicks, bad searches, incomplete extraction, and long-horizon planning errors.

### Claim 3 — Web agents need external tools

Toolformer shows that LLMs can learn to use tools through API calls. This is essential because web agents need browsers, search, calculators, retrievers, validators, databases, and other external tools.

### Claim 4 — Architecture is not enough without grounding and verification

The S3 papers introduce agent loops, but they do not fully solve grounding and verification. For web automation, the agent must connect high-level reasoning to exact web elements, tool results, extracted values, and success criteria.

---

## 7. Thesis-ready synthesis paragraph

LLM agent architectures extend foundation language models by embedding them in interactive control loops. ReAct introduces the central reasoning-action-observation pattern, allowing an LLM to reason about the current state, execute an action, receive environmental feedback, and update its next decision. This moves LLMs beyond static chain-of-thought reasoning toward interactive task solving. Reflexion adds a self-improvement mechanism by storing natural-language reflections after failed trials and using them as memory for future attempts, enabling agents to recover from repeated mistakes without updating model weights. Toolformer adds external tool use by training language models to decide when and how to call APIs, allowing them to overcome limitations in arithmetic, factual lookup, temporal awareness, and translation. Together, these works establish the core architectural components of LLM-based agents: reasoning, action, observation, memory, reflection, and tool use. For generalized web automation and data extraction, these components are necessary but insufficient. Real web agents must also solve precise DOM and visual grounding, dynamic browser interaction, long-horizon state tracking, safe action execution, robust verification of extracted data, and deployment constraints such as cost, latency, and tool reliability. Thus, S3 provides the agentic control foundation that later web-specific systems extend with grounding, planning, evaluation, and safety mechanisms.

---

## 8. Limitations connected to the thesis

### 8.1 ReAct limitation — prompt-based control is fragile

ReAct relies on few-shot prompting and hand-written trajectories.

For web agents, this matters because generalized web automation cannot depend on manually crafted examples for every website, workflow, or task type. Real websites vary in layout, terminology, action space, and interaction rules. This motivates later work on more robust planning, training, memory, and web-specific benchmarks.

### 8.2 ReAct limitation — loops and hallucinated actions

ReAct can repeat actions, enter loops, or produce hallucinated reasoning.

For web agents, this matters because a loop can repeatedly click the wrong element, resubmit a form, or waste browser/tool calls. Hallucinated reasoning can cause the agent to believe it saw a button, field, or value that does not exist. This motivates failure detection, reflection, verification, and safe execution constraints.

### 8.3 Reflexion limitation — success signals are hard

Reflexion depends on detecting failure and using reward or success signals.

For web agents, this matters because many web tasks have ambiguous success criteria. A page may not show a clear success message, extracted data may be partially correct, and some actions cannot be safely retried. This motivates explicit success detectors, validators, human approval, and confidence estimation.

### 8.4 Reflexion limitation — reflection can be wrong

Reflections are natural-language outputs and can themselves be inaccurate.

For web agents, this matters because a wrong reflection can make the next attempt worse. For example, the agent may incorrectly conclude that a website has a certain structure or that a value was extracted from the right field. This motivates memory validation and evidence-grounded reflection.

### 8.5 Toolformer limitation — no chained interactive tool use

Toolformer does not originally support chained tool use or interactive browsing.

For web agents, this matters because web automation normally requires tool chains:

```text
search → browse → inspect → extract → validate → store
```

This motivates later agent architectures that plan and orchestrate multiple tools over several steps.

### 8.6 Toolformer limitation — tool cost is ignored

Toolformer does not account for API cost, latency, or reliability when deciding whether to use a tool.

For web agents, this matters because browser automation may involve expensive API calls, slow page loading, rate limits, CAPTCHA, proxy costs, and tool failures. This motivates deployment-aware agent design.

---

## 9. Cross-links to later sections

| Paper | Feeds |
|---|---|
| ReAct | S5.3 planning, S5.5 failure modes, S6 search/extraction, S8 deployment |
| Reflexion | S5.3 recovery planning, S5.4 training/verbal RL, S5.5 loops/failures, S7 safety, S8 retry cost |
| Toolformer | S5.3 tool planning, S6 extraction tools, S7 verification, S8 tool cost/latency |

---


### Additional S5.4 link — Reflexion as verbal RL

Reflexion also feeds **S5.4 — Training Strategies and Generalization** because it shows that agent behavior can be improved through **language feedback and episodic memory** rather than gradient-based reinforcement learning or model fine-tuning. This makes Reflexion an important precursor to later human-in-the-loop and feedback-driven training approaches for agents.

---

## 10. Transition to S4 and S5

S3 shows how LLMs become agents in general:

```text
reasoning + acting + observation + memory + tools
```

The next question is:

```text
How are these general agent architectures adapted to the web?
```

This transition leads naturally to:

- **S4 — Evolution of Web Agent Systems**
  - How LLM agents moved into browser and web environments.

- **S5.1 — Web Agent Benchmarks and Evaluation**
  - How web-agent success is measured.

- **S5.2 — Perception, Grounding, and Interface Representation**
  - How agents represent DOM, screenshots, UI elements, and web state.

- **S5.3 — Planning and Decision-Making**
  - How agents plan long-horizon web actions.

- **S5.5 — Limitations and Failure Modes**
  - How agents fail through loops, hallucinations, grounding errors, and unsafe actions.

---

## 11. Final S3 mini-synthesis

S3 establishes the architectural foundation of LLM-based agents. ReAct shows that LLMs can interleave reasoning and acting, forming the basic observation-action loop required for interactive task solving. Reflexion adds verbal memory and self-reflection, allowing agents to learn from failed attempts without fine-tuning. Toolformer adds tool use, showing that language models can learn to call APIs to overcome limitations in factuality, arithmetic, temporal awareness, and external knowledge access. Together, these papers define the core components of LLM-agent architecture: reasoning, action, observation, tool use, memory, and reflection.

For generalized web automation and data extraction, these components are essential. A web agent must reason about user goals, act on web pages, observe changes, use tools, remember previous steps, recover from failures, and verify outputs. However, S3 also shows that early LLM-agent architectures remain incomplete for real web environments. They do not fully solve DOM grounding, visual grounding, dynamic interaction, long-horizon reliability, safe action execution, or deployment constraints. Therefore, the literature must next examine how these general agent patterns are adapted, evaluated, and extended in web-specific systems.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\Writing\S3_refined_synthesis_after_P1.md

# S3 Refined Synthesis — LLM Agent Architectures  
## Updated after P0 + P1 papers

## 1. What changed after adding the P1 papers

The S3 P0 synthesis established the basic architecture of early LLM agents:

```text
ReAct → Reflexion → Toolformer
```

This gave the first agentic progression:

```text
reasoning + acting
→ reflection + memory
→ tool use
```

After adding the S3 P1 papers, the section becomes broader and more complete. The refined S3 narrative is now:

```text
MRKL
→ ReAct
→ Reflexion
→ Toolformer
→ Tree of Thoughts
→ LATS
→ CoALA
→ Agent surveys
```

Conceptually, this means:

```text
modular tool architecture
→ reasoning-action loop
→ memory and self-correction
→ learned tool use
→ deliberate planning/search
→ unified reasoning-acting-planning
→ cognitive architecture framework
→ broad agent taxonomy
```

The P1 papers do not replace the P0 synthesis. They refine it by showing that LLM-agent architecture is not only about a simple action loop. It includes modularity, tool routing, memory, reflection, planning, search, cognitive architecture, evaluation, and taxonomy.

---

## 2. Refined narrative

Section S3 explains how LLMs are transformed from language models into agent architectures.

In S2, LLMs were shown to provide core capabilities: instruction following, in-context learning, reasoning, decomposition, alignment, retrieval, multimodality, and long-context processing. However, those capabilities mostly remain inside the model. S3 explains how these capabilities are organized into systems that can act, observe, use tools, remember, plan, and improve.

The earliest architectural direction is modularity. MRKL systems argue that LLMs should not be treated as monolithic systems. Instead, they should be embedded in modular neuro-symbolic architectures, where a router selects among expert modules such as calculators, databases, APIs, search tools, and other specialized systems. This is important for web agents because generalized web automation requires interaction with browsers, DOM parsers, extraction tools, validators, databases, and external APIs.

ReAct then introduces the core reasoning-action-observation loop. Instead of producing only a final answer or a static chain of thought, the model alternates between reasoning, acting, and observing. This is the first major step toward interactive LLM agents. For web automation, ReAct maps naturally to browser interaction: observe the page, reason about the next step, click or type, observe the result, and continue.

Reflexion extends this loop by adding self-reflection and memory. After a failed attempt, the agent writes a natural-language reflection and stores it for later trials. This shows that agent behavior can be improved through verbal feedback and episodic memory, without updating model weights. For web agents, this is important because failures are common: wrong clicks, loops, bad search queries, incorrect extractions, and incomplete workflows require recovery mechanisms.

Toolformer strengthens the tool-use dimension. It shows that language models can learn when and how to call external tools through self-supervised data generation. This is important because web agents need external tools to overcome LLM limitations: search, browsing, calculation, data extraction, validation, and API access. However, Toolformer alone does not provide long-horizon tool orchestration or grounded browser control.

Tree of Thoughts adds deliberate planning and search. It generalizes chain-of-thought into a tree of intermediate reasoning states, allowing the model to generate, evaluate, prune, and backtrack among candidate thoughts. This is relevant for web automation because a web agent should not always follow the first action sequence it generates. It may need to compare alternative plans and backtrack when a path is unpromising.

LATS then unifies several previous directions. It combines ReAct-style reasoning and acting, Tree-of-Thought-style search, Reflexion-style feedback, and Monte Carlo Tree Search. LATS is especially important because it directly combines reasoning, acting, planning, self-reflection, and external environment feedback. It therefore provides one of the strongest bridges from general agent architecture to web-agent planning.

CoALA provides the conceptual architecture for organizing all these components. It frames language agents through memory, action spaces, and decision-making procedures. It distinguishes internal actions such as reasoning, retrieval, and learning from external actions such as grounding in an environment. For web agents, this is very useful because it provides the vocabulary needed to describe DOM grounding, browser actions, memory retrieval, planning, and feedback.

The two broad agent surveys then position these papers within the larger agent landscape. Xi et al. organize LLM agents around brain, perception, and action. Wang et al. organize autonomous agents around profile, memory, planning, and action. Together, these surveys show that LLM-based agents are not isolated methods, but a rapidly growing research field with shared architectural modules, application areas, evaluation challenges, and risks.

---

## 3. Refined S3 architecture stack

The S3 papers provide the following architectural components:

| Component | Main papers | Role in LLM agents | Relevance for web automation |
|---|---|---|---|
| Modular expert architecture | MRKL | Routes tasks to specialized modules | Browser, APIs, validators, extractors, databases |
| Reasoning-action loop | ReAct | Interleaves thought, action, observation | Core browser automation loop |
| Self-reflection | Reflexion | Learns from failed attempts using language memory | Recovery from loops, wrong clicks, failed extraction |
| Tool use | Toolformer, MRKL | Connects LLMs to external tools/APIs | Search, browser tools, calculators, extraction APIs |
| Deliberate search | Tree of Thoughts | Explores multiple reasoning paths | Alternative plans and candidate workflows |
| Search-based agent planning | LATS | Combines reasoning, acting, planning, feedback | Long-horizon web navigation and WebShop-style tasks |
| Cognitive architecture | CoALA | Organizes memory, actions, decisions | Framework for web-agent architecture |
| General agent taxonomy | Xi et al., Wang et al. | Maps the field and components | Positions web agents in broader agent literature |

---

## 4. Refined conceptual contribution of S3

The central contribution of S3 is that **LLM agency is architectural**.

A model becomes an agent not simply because it is large or instruction-following, but because it is embedded in a system with:

```text
memory
tools
actions
observations
planning
reflection
retrieval
external grounding
decision cycles
```

The S3 papers show the transition from:

```text
LLM as text generator
```

to:

```text
LLM as controller inside an agent architecture
```

This is the essential bridge between foundation LLMs and web agents.

---

## 5. Refined gap after S3 P1

After S3 P0, the gap was:

```text
Early LLM-agent architectures introduce reasoning-action loops, memory, reflection, and tool use, but they still do not fully solve grounded, reliable, safe, and scalable web automation.
```

After adding S3 P1 papers, the gap becomes more precise:

```text
LLM-agent architectures now include modular tools, reasoning-action loops, reflection, memory, search-based planning, and cognitive frameworks, but generalized web automation still requires web-specific grounding, verification, safety, and deployment-aware orchestration.
```

The refined gap is not that agents lack architecture. The refined gap is that general agent architectures still need to be adapted to the web.

They can now support:

```text
reasoning before acting
tool/module selection
reflection after failure
multi-path planning
search over trajectories
memory and retrieval
conceptual architecture
agent taxonomy
```

But they still do not fully solve:

```text
DOM-grounded perception
screenshot-to-action grounding
precise UI element selection
dynamic JavaScript interaction
long-horizon browser workflows
irreversible web actions
robust extraction verification
safe tool orchestration
cost and latency control
generalization across unseen websites
privacy and permission boundaries
```

Therefore, the refined S3 gap is:

```text
General LLM-agent architectures provide the control logic of agency, but web automation requires grounding that control logic in real browser environments with reliable perception, action, verification, and safety.
```

---

## 6. Refined thesis connection

For the thesis topic, **“LLM-based agents for generalized web automation and data extraction,”** S3 supports five major claims.

### Claim 1 — Web agents require modular architecture

MRKL and Toolformer show that LLM agents need external modules and tools. This supports the thesis claim that web automation cannot rely on a single LLM. A robust web agent needs a modular architecture with browser tools, search, DOM parsers, extraction modules, validators, APIs, and memory systems.

### Claim 2 — Web agents require a reasoning-action-observation loop

ReAct shows that agents must connect reasoning to actions and observations. This is the core loop of web automation:

```text
observe page → reason → act → observe result
```

Without this loop, the model remains a text generator rather than an interactive web agent.

### Claim 3 — Web agents require memory and self-correction

Reflexion shows that agents can improve through verbal feedback and episodic memory. For web automation, this matters because agents must recover from errors, loops, incomplete extraction, failed navigation, and wrong assumptions about page structure.

### Claim 4 — Web agents require planning and search

Tree of Thoughts and LATS show that difficult tasks require deliberate planning, alternative trajectory exploration, and backtracking. Web tasks are often long-horizon and uncertain, so the agent must compare candidate actions, evaluate partial progress, and revise plans.

### Claim 5 — Web agents require a cognitive/system framework

CoALA and the surveys show that LLM agents should be understood as systems with memory, perception, action, planning, and evaluation. This supports the thesis structure: later sections can analyze web agents by decomposing them into perception/grounding, planning, training, failure modes, extraction, safety, and deployment.

---

## 7. Refined thesis-ready synthesis paragraph

LLM agent architectures extend foundation language models by embedding them in modular, interactive, and memory-aware systems. MRKL systems introduced the idea that LLMs should be combined with external expert modules, enabling access to current knowledge, proprietary data, exact reasoning, and symbolic tools. ReAct then established the core reasoning-action-observation loop, allowing LLMs to reason about a state, execute an action, receive feedback, and update their next decision. Reflexion extended this loop with verbal self-reflection and episodic memory, showing that agents can improve across attempts without gradient updates. Toolformer further advanced tool use by teaching language models to call external APIs through self-supervised data generation. Tree of Thoughts introduced deliberate search over intermediate reasoning states, while LATS unified reasoning, acting, planning, reflection, and external feedback through language-agent tree search. CoALA and recent surveys then provided broader frameworks for understanding agents as systems with memory, internal and external actions, decision procedures, perception, planning, and evaluation. Together, these works define the architectural foundation of LLM-based agents. For generalized web automation and data extraction, they provide the necessary control components: modularity, tool use, reasoning, action, observation, memory, reflection, and planning. However, they remain insufficient without web-specific grounding, reliable browser action execution, DOM and visual perception, state tracking, extraction verification, safety constraints, and deployment-aware orchestration. This motivates the transition from general LLM-agent architectures to web-specific agent systems and benchmarks.

---

## 8. Refined limitations connected to the thesis

### 8.1 Modularity limitation

MRKL and Toolformer show that external tools are necessary, but tool use is not automatically reliable.

For web agents, this matters because tools must be selected, sequenced, monitored, and verified. Browser automation requires more than a single tool call; it often requires multi-step orchestration across search, navigation, extraction, validation, and storage.

### 8.2 Routing limitation

MRKL relies on a router to select the correct expert module.

For web agents, this matters because wrong routing can send a task to the wrong tool. For example, the agent may use the LLM when it should query the DOM, or scrape text when it should verify with a source.

### 8.3 ReAct limitation

ReAct introduces the action loop, but it often follows one trajectory and can loop or hallucinate.

For web agents, this matters because a wrong trajectory can repeatedly click the wrong element, miss a field, hallucinate page content, or fail silently. This motivates reflection, search, and verification.

### 8.4 Reflexion limitation

Reflexion improves behavior through verbal memory, but it depends on clear failure signals.

For web agents, this matters because many web tasks do not provide explicit success or failure. An extraction can look correct but be wrong. A form can submit with hidden errors. A task can partially succeed. This motivates explicit validators and success detectors.

### 8.5 Toolformer limitation

Toolformer learns tool use, but it does not originally support chained interactive tool use.

For web agents, this matters because web automation requires iterative tool use over time, including search, browsing, inspection, extraction, verification, and storage.

### 8.6 Tree-of-Thoughts limitation

Tree of Thoughts improves planning through search, but it is mainly text-based and can be expensive.

For web agents, this matters because each branch may require browser actions, screenshots, DOM parsing, or tool calls. Search must therefore be selective and cost-aware.

### 8.7 LATS limitation

LATS unifies reasoning, acting, planning, and feedback, but assumes reversibility and increases computation.

For web agents, this matters because many actions are not safely reversible: submitting forms, sending messages, deleting items, or making purchases. LATS-style planning must be adapted with safe exploration policies.

### 8.8 CoALA limitation

CoALA gives a conceptual architecture, but not a concrete web-agent implementation.

For web agents, this matters because the framework must be instantiated with web-specific components: DOM state, browser actions, visual grounding, extraction schemas, validators, and safety policies.

### 8.9 Survey limitation

The surveys provide broad taxonomies, but not detailed solutions for web automation.

For the thesis, they are useful for positioning and structure, but web-specific sections must supply the concrete evidence, benchmarks, systems, and failure analysis.

---

## 9. Updated cross-links to later sections

| Paper | Feeds |
|---|---|
| MRKL | S5.3 tool planning, S5.4 modular generalization, S6 extraction modules, S7 verification, S8 deployment |
| ReAct | S5.3 planning, S5.5 loops/failure modes, S6 search/extraction, S8 deployment |
| Reflexion | S5.3 recovery planning, S5.4 verbal RL/training, S5.5 failures, S7 safety, S8 retry cost |
| Toolformer | S5.3 tool planning, S6 extraction tools, S7 verification, S8 tool cost/latency |
| Tree of Thoughts | S5.3 deliberate planning/search, S5.5 search failure, S8 inference cost |
| LATS | S5.3 search-based web planning, S5.4 gradient-free improvement, S5.5 reversibility/cost failures, S8 deployment |
| CoALA | S5.2 grounding, S5.3 decision cycles, S5.4 memory/learning, S5.5 failure localization, S8 architecture |
| Xi et al. survey | S5.1 evaluation, S5.2 perception/action, S5.3 planning, S7 risks |
| Wang et al. survey | S5.1 evaluation, S5.3 planning, S5.4 memory/capability acquisition, S8 challenges |

---

## 10. Transition to S4 and S5

S3 establishes the general architecture of LLM agents:

```text
LLM + memory + tools + actions + observations + planning + reflection
```

The next question is:

```text
How are these general agent architectures adapted to web environments?
```

This transition leads to web-specific issues:

```text
How does the agent perceive a web page?
How does it represent DOM, HTML, screenshots, forms, and tables?
How does it choose safe browser actions?
How does it plan across multiple pages?
How does it know whether extraction is correct?
How does it avoid loops and hallucinated page states?
How does it operate under cost, latency, and privacy constraints?
```

Therefore, after S3, the literature review should move toward:

- **S4 — Evolution of Web Agent Systems**
  - How general LLM-agent patterns became browser/web agents.

- **S5.1 — Benchmarks and Evaluation**
  - How web-agent success is measured.

- **S5.2 — Perception, Grounding, and Interface Representation**
  - How agents represent web pages, DOMs, screenshots, and UI elements.

- **S5.3 — Planning and Decision-Making**
  - How agents plan and execute long-horizon web tasks.

- **S5.4 — Training Strategies and Generalization**
  - How agents learn from demonstrations, feedback, trajectories, memory, or synthetic data.

- **S5.5 — Failure Modes**
  - How agents fail through loops, hallucinations, grounding errors, unsafe actions, and tool failures.

---

## 11. Final refined S3 synthesis

S3 shows that LLM-based agents emerge when foundation models are embedded inside modular, interactive control architectures. MRKL introduces modular expert routing, showing that LLMs should be combined with external tools and symbolic systems. ReAct establishes the reasoning-action-observation loop that makes LLMs interactive. Reflexion adds verbal memory and self-correction, enabling agents to improve from failed attempts without gradient updates. Toolformer shows that language models can learn to use external tools. Tree of Thoughts introduces deliberate search over reasoning states, while LATS unifies reasoning, acting, planning, feedback, and reflection through language-agent tree search. CoALA and recent surveys provide the broader conceptual and taxonomic frameworks needed to organize these components.

Together, these papers define the architectural foundations required for web agents: modularity, tool use, reasoning, action, observation, memory, reflection, planning, and search. However, they also show that general LLM-agent architectures are not sufficient for generalized web automation and data extraction. The remaining challenge is to ground these architectures in real web environments, where agents must perceive DOM and visual interfaces, execute browser actions safely, track state across long workflows, verify extracted data, recover from failures, and operate under deployment constraints. This refined S3 synthesis therefore motivates the next stage of the literature review: web-specific agent systems, benchmarks, grounding methods, planning techniques, training strategies, and failure analysis.


---

## Synthesis / Writing Notes (3 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\writing\S3_mini_synthesis_from_P0.md

# S3 Mini-Synthesis — LLM Agent Architectures  
## Based on S3 P0 papers: ReAct, Reflexion, Toolformer

## 1. Narrative

Section S3 marks the transition from **LLMs as language models** to **LLMs as agent controllers**.

In S2, the literature showed that LLMs can understand language, follow instructions, reason step by step, use in-context examples, and improve reasoning reliability. However, these capabilities are still mostly internal to the model. S3 begins where S2 stops: it asks how these LLM capabilities can be organized into systems that **act**, **observe**, **use tools**, **remember**, and **recover from failure**.

The three P0 papers in S3 define three core architectural directions:

```text
ReAct → reasoning + acting loop
Reflexion → memory + self-reflection loop
Toolformer → learned tool-use loop
```

Together, they form the basic architecture of modern LLM agents:

```text
Reason → Act → Observe → Reflect → Use tools → Update behavior
```

---

## 2. Paper-level synthesis

### 2.1 ReAct — Reasoning and acting

ReAct introduces the central LLM-agent loop:

```text
Thought → Action → Observation → Thought → Action → Observation
```

This is a major shift from chain-of-thought prompting. In chain-of-thought, the model reasons internally and then gives an answer. In ReAct, the model reasons, acts in an environment, receives observations, and updates its reasoning based on feedback.

For web agents, this is foundational. Web automation naturally follows the ReAct pattern:

```text
observe page → reason about next step → click/type/search → observe result → continue
```

ReAct shows that reasoning and acting are stronger together than either alone. Reasoning helps the agent plan, track progress, and recover from exceptions. Acting gives the agent external evidence that reduces hallucination and grounds reasoning in observations.

However, ReAct still depends heavily on prompts, simplified action spaces, and short trajectories. It can loop, hallucinate thoughts, repeat wrong actions, and fail on complex long-horizon workflows. For web agents, this matters because real websites are dynamic, noisy, multimodal, and often require precise DOM or visual grounding.

---

### 2.2 Reflexion — Memory and self-reflection

Reflexion extends ReAct by adding **memory** and **self-reflection**.

Instead of changing model weights, the agent learns from failure through natural-language reflection. After a failed attempt, the agent writes a reflection explaining what went wrong and stores it in memory. On the next trial, the agent uses this memory to improve its plan.

The basic Reflexion loop is:

```text
Attempt task → fail → reflect → store memory → retry with reflection
```

For web agents, Reflexion is important because failure is common in web automation. Agents may click the wrong element, choose a bad search query, misunderstand a form, loop between pages, or fail to verify an extracted value. Reflexion provides a lightweight mechanism for self-correction without fine-tuning.

However, Reflexion depends on reliable failure detection. Many web tasks do not provide a clear success/failure signal. A form may submit successfully but contain wrong information. An extracted value may look correct but be stale. A purchase or account action may be irreversible. For web agents, this means reflection must be combined with verification, risk detection, safe retry policies, and human oversight.

---

### 2.3 Toolformer — Tool use

Toolformer adds another essential architectural component: **external tool use**.

The paper shows that a language model can learn when to call tools, which tool to call, what arguments to pass, and how to use the result. It does this through self-supervised data generation: the model proposes API calls, executes them, keeps useful calls that reduce prediction loss, and fine-tunes on the resulting tool-augmented data.

For web agents, Toolformer matters because web automation requires tools. A practical web agent may need:

```text
browser tools
search engines
calculators
databases
retrievers
extractors
validators
APIs
file systems
code execution
```

Toolformer shows that tool use can be learned, not only manually scripted.

However, Toolformer does not solve full agentic tool orchestration. It cannot originally chain tools, browse interactively, reformulate failed searches, reason about tool cost, or ground tool calls in UI actions. For web agents, this matters because real workflows often require multi-step tool chains:

```text
search → open page → inspect DOM → extract data → validate → store result
```

Thus, Toolformer is foundational for tool-using agents, but generalized web automation needs planning, feedback, grounding, and verification around tool use.

---

## 3. Main conceptual contribution of S3

The main contribution of S3 is that **agency is a system property**, not a property of the language model alone.

The three P0 papers show that an LLM becomes an agent when it is embedded inside a loop with additional components:

| Agent component | Main paper | Role |
|---|---|---|
| Reasoning-action loop | ReAct | Connects thoughts, actions, and observations |
| Reflection and memory | Reflexion | Enables learning from failure across trials |
| Tool use | Toolformer | Enables external computation, retrieval, and API access |

Together, these papers define the first layer of LLM-agent architecture:

```text
LLM + reasoning traces + actions + observations + tools + memory
```

This is the foundation for later web agents.

---

## 4. S3 narrative arc

The S3 narrative can be written as a progression:

```text
Step 1 — ReAct:
LLMs can reason and act in an interleaved loop.

Step 2 — Reflexion:
LLM agents can use verbal memory to learn from failed attempts.

Step 3 — Toolformer:
LLMs can learn to call external tools to overcome internal limitations.
```

This gives the section a clear structure:

```text
Reasoning + Acting
→ Reflection + Memory
→ Tool Use
```

Or more generally:

```text
interactive agency
→ self-correction
→ external capability extension
```

This progression prepares the transition from general agent architectures to web-specific agents in later sections.

---

## 5. Refined gap after S3 P0

After S2, the gap was:

```text
LLMs are strong at language reasoning, but weak as grounded, reliable, interactive web agents.
```

After S3 P0, the gap becomes more precise:

```text
Early LLM-agent architectures introduce reasoning-action loops, memory, reflection, and tool use, but they still do not fully solve grounded, reliable, safe, and scalable web automation.
```

These papers show that LLM agents can:

```text
reason before acting
act in environments
observe feedback
call tools
learn from failed trials
store verbal memories
reduce some hallucinations
improve interpretability
```

But they do not fully solve:

```text
precise DOM grounding
visual UI grounding
dynamic website interaction
long-horizon web workflows
tool-chain orchestration
robust success verification
safe irreversible actions
memory reliability
cost and latency
generalization across unseen websites
```

So the refined S3 gap is:

```text
LLM-agent architectures provide the control loop, but generalized web automation requires grounding, verification, robust planning, safety constraints, and deployment-aware orchestration.
```

---

## 6. Thesis connection

For the thesis topic, **“LLM-based agents for generalized web automation and data extraction,”** S3 supports four major claims.

### Claim 1 — Web agents need an interactive control loop

ReAct shows that LLMs must not only reason internally. They must connect reasoning to actions and observations. This is the basic structure of web automation:

```text
observe → reason → act → observe again
```

### Claim 2 — Web agents need memory and recovery

Reflexion shows that agents can improve through verbal memory and self-reflection. This is important because web agents fail often and need mechanisms to recover from wrong clicks, bad searches, incomplete extraction, and long-horizon planning errors.

### Claim 3 — Web agents need external tools

Toolformer shows that LLMs can learn to use tools through API calls. This is essential because web agents need browsers, search, calculators, retrievers, validators, databases, and other external tools.

### Claim 4 — Architecture is not enough without grounding and verification

The S3 papers introduce agent loops, but they do not fully solve grounding and verification. For web automation, the agent must connect high-level reasoning to exact web elements, tool results, extracted values, and success criteria.

---

## 7. Thesis-ready synthesis paragraph

LLM agent architectures extend foundation language models by embedding them in interactive control loops. ReAct introduces the central reasoning-action-observation pattern, allowing an LLM to reason about the current state, execute an action, receive environmental feedback, and update its next decision. This moves LLMs beyond static chain-of-thought reasoning toward interactive task solving. Reflexion adds a self-improvement mechanism by storing natural-language reflections after failed trials and using them as memory for future attempts, enabling agents to recover from repeated mistakes without updating model weights. Toolformer adds external tool use by training language models to decide when and how to call APIs, allowing them to overcome limitations in arithmetic, factual lookup, temporal awareness, and translation. Together, these works establish the core architectural components of LLM-based agents: reasoning, action, observation, memory, reflection, and tool use. For generalized web automation and data extraction, these components are necessary but insufficient. Real web agents must also solve precise DOM and visual grounding, dynamic browser interaction, long-horizon state tracking, safe action execution, robust verification of extracted data, and deployment constraints such as cost, latency, and tool reliability. Thus, S3 provides the agentic control foundation that later web-specific systems extend with grounding, planning, evaluation, and safety mechanisms.

---

## 8. Limitations connected to the thesis

### 8.1 ReAct limitation — prompt-based control is fragile

ReAct relies on few-shot prompting and hand-written trajectories.

For web agents, this matters because generalized web automation cannot depend on manually crafted examples for every website, workflow, or task type. Real websites vary in layout, terminology, action space, and interaction rules. This motivates later work on more robust planning, training, memory, and web-specific benchmarks.

### 8.2 ReAct limitation — loops and hallucinated actions

ReAct can repeat actions, enter loops, or produce hallucinated reasoning.

For web agents, this matters because a loop can repeatedly click the wrong element, resubmit a form, or waste browser/tool calls. Hallucinated reasoning can cause the agent to believe it saw a button, field, or value that does not exist. This motivates failure detection, reflection, verification, and safe execution constraints.

### 8.3 Reflexion limitation — success signals are hard

Reflexion depends on detecting failure and using reward or success signals.

For web agents, this matters because many web tasks have ambiguous success criteria. A page may not show a clear success message, extracted data may be partially correct, and some actions cannot be safely retried. This motivates explicit success detectors, validators, human approval, and confidence estimation.

### 8.4 Reflexion limitation — reflection can be wrong

Reflections are natural-language outputs and can themselves be inaccurate.

For web agents, this matters because a wrong reflection can make the next attempt worse. For example, the agent may incorrectly conclude that a website has a certain structure or that a value was extracted from the right field. This motivates memory validation and evidence-grounded reflection.

### 8.5 Toolformer limitation — no chained interactive tool use

Toolformer does not originally support chained tool use or interactive browsing.

For web agents, this matters because web automation normally requires tool chains:

```text
search → browse → inspect → extract → validate → store
```

This motivates later agent architectures that plan and orchestrate multiple tools over several steps.

### 8.6 Toolformer limitation — tool cost is ignored

Toolformer does not account for API cost, latency, or reliability when deciding whether to use a tool.

For web agents, this matters because browser automation may involve expensive API calls, slow page loading, rate limits, CAPTCHA, proxy costs, and tool failures. This motivates deployment-aware agent design.

---

## 9. Cross-links to later sections

| Paper | Feeds |
|---|---|
| ReAct | S5.3 planning, S5.5 failure modes, S6 search/extraction, S8 deployment |
| Reflexion | S5.3 recovery planning, S5.5 loops/failures, S7 safety, S8 retry cost |
| Toolformer | S5.3 tool planning, S6 extraction tools, S7 verification, S8 tool cost/latency |

---

## 10. Transition to S4 and S5

S3 shows how LLMs become agents in general:

```text
reasoning + acting + observation + memory + tools
```

The next question is:

```text
How are these general agent architectures adapted to the web?
```

This transition leads naturally to:

- **S4 — Evolution of Web Agent Systems**
  - How LLM agents moved into browser and web environments.

- **S5.1 — Web Agent Benchmarks and Evaluation**
  - How web-agent success is measured.

- **S5.2 — Perception, Grounding, and Interface Representation**
  - How agents represent DOM, screenshots, UI elements, and web state.

- **S5.3 — Planning and Decision-Making**
  - How agents plan long-horizon web actions.

- **S5.5 — Limitations and Failure Modes**
  - How agents fail through loops, hallucinations, grounding errors, and unsafe actions.

---

## 11. Final S3 mini-synthesis

S3 establishes the architectural foundation of LLM-based agents. ReAct shows that LLMs can interleave reasoning and acting, forming the basic observation-action loop required for interactive task solving. Reflexion adds verbal memory and self-reflection, allowing agents to learn from failed attempts without fine-tuning. Toolformer adds tool use, showing that language models can learn to call APIs to overcome limitations in factuality, arithmetic, temporal awareness, and external knowledge access. Together, these papers define the core components of LLM-agent architecture: reasoning, action, observation, tool use, memory, and reflection.

For generalized web automation and data extraction, these components are essential. A web agent must reason about user goals, act on web pages, observe changes, use tools, remember previous steps, recover from failures, and verify outputs. However, S3 also shows that early LLM-agent architectures remain incomplete for real web environments. They do not fully solve DOM grounding, visual grounding, dynamic interaction, long-horizon reliability, safe action execution, or deployment constraints. Therefore, the literature must next examine how these general agent patterns are adapted, evaluated, and extended in web-specific systems.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\writing\S3_mini_synthesis_from_P0_updated_cross_links.md

# S3 Mini-Synthesis — LLM Agent Architectures  
## Based on S3 P0 papers: ReAct, Reflexion, Toolformer

## 1. Narrative

Section S3 marks the transition from **LLMs as language models** to **LLMs as agent controllers**.

In S2, the literature showed that LLMs can understand language, follow instructions, reason step by step, use in-context examples, and improve reasoning reliability. However, these capabilities are still mostly internal to the model. S3 begins where S2 stops: it asks how these LLM capabilities can be organized into systems that **act**, **observe**, **use tools**, **remember**, and **recover from failure**.

The three P0 papers in S3 define three core architectural directions:

```text
ReAct → reasoning + acting loop
Reflexion → memory + self-reflection loop
Toolformer → learned tool-use loop
```

Together, they form the basic architecture of modern LLM agents:

```text
Reason → Act → Observe → Reflect → Use tools → Update behavior
```

---

## 2. Paper-level synthesis

### 2.1 ReAct — Reasoning and acting

ReAct introduces the central LLM-agent loop:

```text
Thought → Action → Observation → Thought → Action → Observation
```

This is a major shift from chain-of-thought prompting. In chain-of-thought, the model reasons internally and then gives an answer. In ReAct, the model reasons, acts in an environment, receives observations, and updates its reasoning based on feedback.

For web agents, this is foundational. Web automation naturally follows the ReAct pattern:

```text
observe page → reason about next step → click/type/search → observe result → continue
```

ReAct shows that reasoning and acting are stronger together than either alone. Reasoning helps the agent plan, track progress, and recover from exceptions. Acting gives the agent external evidence that reduces hallucination and grounds reasoning in observations.

However, ReAct still depends heavily on prompts, simplified action spaces, and short trajectories. It can loop, hallucinate thoughts, repeat wrong actions, and fail on complex long-horizon workflows. For web agents, this matters because real websites are dynamic, noisy, multimodal, and often require precise DOM or visual grounding.

---

### 2.2 Reflexion — Memory and self-reflection

Reflexion extends ReAct by adding **memory** and **self-reflection**.

Instead of changing model weights, the agent learns from failure through natural-language reflection. After a failed attempt, the agent writes a reflection explaining what went wrong and stores it in memory. On the next trial, the agent uses this memory to improve its plan.

The basic Reflexion loop is:

```text
Attempt task → fail → reflect → store memory → retry with reflection
```

For web agents, Reflexion is important because failure is common in web automation. Agents may click the wrong element, choose a bad search query, misunderstand a form, loop between pages, or fail to verify an extracted value. Reflexion provides a lightweight mechanism for self-correction without fine-tuning.

However, Reflexion depends on reliable failure detection. Many web tasks do not provide a clear success/failure signal. A form may submit successfully but contain wrong information. An extracted value may look correct but be stale. A purchase or account action may be irreversible. For web agents, this means reflection must be combined with verification, risk detection, safe retry policies, and human oversight.

---

### 2.3 Toolformer — Tool use

Toolformer adds another essential architectural component: **external tool use**.

The paper shows that a language model can learn when to call tools, which tool to call, what arguments to pass, and how to use the result. It does this through self-supervised data generation: the model proposes API calls, executes them, keeps useful calls that reduce prediction loss, and fine-tunes on the resulting tool-augmented data.

For web agents, Toolformer matters because web automation requires tools. A practical web agent may need:

```text
browser tools
search engines
calculators
databases
retrievers
extractors
validators
APIs
file systems
code execution
```

Toolformer shows that tool use can be learned, not only manually scripted.

However, Toolformer does not solve full agentic tool orchestration. It cannot originally chain tools, browse interactively, reformulate failed searches, reason about tool cost, or ground tool calls in UI actions. For web agents, this matters because real workflows often require multi-step tool chains:

```text
search → open page → inspect DOM → extract data → validate → store result
```

Thus, Toolformer is foundational for tool-using agents, but generalized web automation needs planning, feedback, grounding, and verification around tool use.

---

## 3. Main conceptual contribution of S3

The main contribution of S3 is that **agency is a system property**, not a property of the language model alone.

The three P0 papers show that an LLM becomes an agent when it is embedded inside a loop with additional components:

| Agent component | Main paper | Role |
|---|---|---|
| Reasoning-action loop | ReAct | Connects thoughts, actions, and observations |
| Reflection and memory | Reflexion | Enables learning from failure across trials |
| Tool use | Toolformer | Enables external computation, retrieval, and API access |

Together, these papers define the first layer of LLM-agent architecture:

```text
LLM + reasoning traces + actions + observations + tools + memory
```

This is the foundation for later web agents.

---

## 4. S3 narrative arc

The S3 narrative can be written as a progression:

```text
Step 1 — ReAct:
LLMs can reason and act in an interleaved loop.

Step 2 — Reflexion:
LLM agents can use verbal memory to learn from failed attempts.

Step 3 — Toolformer:
LLMs can learn to call external tools to overcome internal limitations.
```

This gives the section a clear structure:

```text
Reasoning + Acting
→ Reflection + Memory
→ Tool Use
```

Or more generally:

```text
interactive agency
→ self-correction
→ external capability extension
```

This progression prepares the transition from general agent architectures to web-specific agents in later sections.

---

## 5. Refined gap after S3 P0

After S2, the gap was:

```text
LLMs are strong at language reasoning, but weak as grounded, reliable, interactive web agents.
```

After S3 P0, the gap becomes more precise:

```text
Early LLM-agent architectures introduce reasoning-action loops, memory, reflection, and tool use, but they still do not fully solve grounded, reliable, safe, and scalable web automation.
```

These papers show that LLM agents can:

```text
reason before acting
act in environments
observe feedback
call tools
learn from failed trials
store verbal memories
reduce some hallucinations
improve interpretability
```

But they do not fully solve:

```text
precise DOM grounding
visual UI grounding
dynamic website interaction
long-horizon web workflows
tool-chain orchestration
robust success verification
safe irreversible actions
memory reliability
cost and latency
generalization across unseen websites
```

So the refined S3 gap is:

```text
LLM-agent architectures provide the control loop, but generalized web automation requires grounding, verification, robust planning, safety constraints, and deployment-aware orchestration.
```

---

## 6. Thesis connection

For the thesis topic, **“LLM-based agents for generalized web automation and data extraction,”** S3 supports four major claims.

### Claim 1 — Web agents need an interactive control loop

ReAct shows that LLMs must not only reason internally. They must connect reasoning to actions and observations. This is the basic structure of web automation:

```text
observe → reason → act → observe again
```

### Claim 2 — Web agents need memory and recovery

Reflexion shows that agents can improve through verbal memory and self-reflection. This is important because web agents fail often and need mechanisms to recover from wrong clicks, bad searches, incomplete extraction, and long-horizon planning errors.

### Claim 3 — Web agents need external tools

Toolformer shows that LLMs can learn to use tools through API calls. This is essential because web agents need browsers, search, calculators, retrievers, validators, databases, and other external tools.

### Claim 4 — Architecture is not enough without grounding and verification

The S3 papers introduce agent loops, but they do not fully solve grounding and verification. For web automation, the agent must connect high-level reasoning to exact web elements, tool results, extracted values, and success criteria.

---

## 7. Thesis-ready synthesis paragraph

LLM agent architectures extend foundation language models by embedding them in interactive control loops. ReAct introduces the central reasoning-action-observation pattern, allowing an LLM to reason about the current state, execute an action, receive environmental feedback, and update its next decision. This moves LLMs beyond static chain-of-thought reasoning toward interactive task solving. Reflexion adds a self-improvement mechanism by storing natural-language reflections after failed trials and using them as memory for future attempts, enabling agents to recover from repeated mistakes without updating model weights. Toolformer adds external tool use by training language models to decide when and how to call APIs, allowing them to overcome limitations in arithmetic, factual lookup, temporal awareness, and translation. Together, these works establish the core architectural components of LLM-based agents: reasoning, action, observation, memory, reflection, and tool use. For generalized web automation and data extraction, these components are necessary but insufficient. Real web agents must also solve precise DOM and visual grounding, dynamic browser interaction, long-horizon state tracking, safe action execution, robust verification of extracted data, and deployment constraints such as cost, latency, and tool reliability. Thus, S3 provides the agentic control foundation that later web-specific systems extend with grounding, planning, evaluation, and safety mechanisms.

---

## 8. Limitations connected to the thesis

### 8.1 ReAct limitation — prompt-based control is fragile

ReAct relies on few-shot prompting and hand-written trajectories.

For web agents, this matters because generalized web automation cannot depend on manually crafted examples for every website, workflow, or task type. Real websites vary in layout, terminology, action space, and interaction rules. This motivates later work on more robust planning, training, memory, and web-specific benchmarks.

### 8.2 ReAct limitation — loops and hallucinated actions

ReAct can repeat actions, enter loops, or produce hallucinated reasoning.

For web agents, this matters because a loop can repeatedly click the wrong element, resubmit a form, or waste browser/tool calls. Hallucinated reasoning can cause the agent to believe it saw a button, field, or value that does not exist. This motivates failure detection, reflection, verification, and safe execution constraints.

### 8.3 Reflexion limitation — success signals are hard

Reflexion depends on detecting failure and using reward or success signals.

For web agents, this matters because many web tasks have ambiguous success criteria. A page may not show a clear success message, extracted data may be partially correct, and some actions cannot be safely retried. This motivates explicit success detectors, validators, human approval, and confidence estimation.

### 8.4 Reflexion limitation — reflection can be wrong

Reflections are natural-language outputs and can themselves be inaccurate.

For web agents, this matters because a wrong reflection can make the next attempt worse. For example, the agent may incorrectly conclude that a website has a certain structure or that a value was extracted from the right field. This motivates memory validation and evidence-grounded reflection.

### 8.5 Toolformer limitation — no chained interactive tool use

Toolformer does not originally support chained tool use or interactive browsing.

For web agents, this matters because web automation normally requires tool chains:

```text
search → browse → inspect → extract → validate → store
```

This motivates later agent architectures that plan and orchestrate multiple tools over several steps.

### 8.6 Toolformer limitation — tool cost is ignored

Toolformer does not account for API cost, latency, or reliability when deciding whether to use a tool.

For web agents, this matters because browser automation may involve expensive API calls, slow page loading, rate limits, CAPTCHA, proxy costs, and tool failures. This motivates deployment-aware agent design.

---

## 9. Cross-links to later sections

| Paper | Feeds |
|---|---|
| ReAct | S5.3 planning, S5.5 failure modes, S6 search/extraction, S8 deployment |
| Reflexion | S5.3 recovery planning, S5.4 training/verbal RL, S5.5 loops/failures, S7 safety, S8 retry cost |
| Toolformer | S5.3 tool planning, S6 extraction tools, S7 verification, S8 tool cost/latency |

---


### Additional S5.4 link — Reflexion as verbal RL

Reflexion also feeds **S5.4 — Training Strategies and Generalization** because it shows that agent behavior can be improved through **language feedback and episodic memory** rather than gradient-based reinforcement learning or model fine-tuning. This makes Reflexion an important precursor to later human-in-the-loop and feedback-driven training approaches for agents.

---

## 10. Transition to S4 and S5

S3 shows how LLMs become agents in general:

```text
reasoning + acting + observation + memory + tools
```

The next question is:

```text
How are these general agent architectures adapted to the web?
```

This transition leads naturally to:

- **S4 — Evolution of Web Agent Systems**
  - How LLM agents moved into browser and web environments.

- **S5.1 — Web Agent Benchmarks and Evaluation**
  - How web-agent success is measured.

- **S5.2 — Perception, Grounding, and Interface Representation**
  - How agents represent DOM, screenshots, UI elements, and web state.

- **S5.3 — Planning and Decision-Making**
  - How agents plan long-horizon web actions.

- **S5.5 — Limitations and Failure Modes**
  - How agents fail through loops, hallucinations, grounding errors, and unsafe actions.

---

## 11. Final S3 mini-synthesis

S3 establishes the architectural foundation of LLM-based agents. ReAct shows that LLMs can interleave reasoning and acting, forming the basic observation-action loop required for interactive task solving. Reflexion adds verbal memory and self-reflection, allowing agents to learn from failed attempts without fine-tuning. Toolformer adds tool use, showing that language models can learn to call APIs to overcome limitations in factuality, arithmetic, temporal awareness, and external knowledge access. Together, these papers define the core components of LLM-agent architecture: reasoning, action, observation, tool use, memory, and reflection.

For generalized web automation and data extraction, these components are essential. A web agent must reason about user goals, act on web pages, observe changes, use tools, remember previous steps, recover from failures, and verify outputs. However, S3 also shows that early LLM-agent architectures remain incomplete for real web environments. They do not fully solve DOM grounding, visual grounding, dynamic interaction, long-horizon reliability, safe action execution, or deployment constraints. Therefore, the literature must next examine how these general agent patterns are adapted, evaluated, and extended in web-specific systems.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S3\writing\S3_refined_synthesis_after_P1.md

# S3 Refined Synthesis — LLM Agent Architectures  
## Updated after P0 + P1 papers

## 1. What changed after adding the P1 papers

The S3 P0 synthesis established the basic architecture of early LLM agents:

```text
ReAct → Reflexion → Toolformer
```

This gave the first agentic progression:

```text
reasoning + acting
→ reflection + memory
→ tool use
```

After adding the S3 P1 papers, the section becomes broader and more complete. The refined S3 narrative is now:

```text
MRKL
→ ReAct
→ Reflexion
→ Toolformer
→ Tree of Thoughts
→ LATS
→ CoALA
→ Agent surveys
```

Conceptually, this means:

```text
modular tool architecture
→ reasoning-action loop
→ memory and self-correction
→ learned tool use
→ deliberate planning/search
→ unified reasoning-acting-planning
→ cognitive architecture framework
→ broad agent taxonomy
```

The P1 papers do not replace the P0 synthesis. They refine it by showing that LLM-agent architecture is not only about a simple action loop. It includes modularity, tool routing, memory, reflection, planning, search, cognitive architecture, evaluation, and taxonomy.

---

## 2. Refined narrative

Section S3 explains how LLMs are transformed from language models into agent architectures.

In S2, LLMs were shown to provide core capabilities: instruction following, in-context learning, reasoning, decomposition, alignment, retrieval, multimodality, and long-context processing. However, those capabilities mostly remain inside the model. S3 explains how these capabilities are organized into systems that can act, observe, use tools, remember, plan, and improve.

The earliest architectural direction is modularity. MRKL systems argue that LLMs should not be treated as monolithic systems. Instead, they should be embedded in modular neuro-symbolic architectures, where a router selects among expert modules such as calculators, databases, APIs, search tools, and other specialized systems. This is important for web agents because generalized web automation requires interaction with browsers, DOM parsers, extraction tools, validators, databases, and external APIs.

ReAct then introduces the core reasoning-action-observation loop. Instead of producing only a final answer or a static chain of thought, the model alternates between reasoning, acting, and observing. This is the first major step toward interactive LLM agents. For web automation, ReAct maps naturally to browser interaction: observe the page, reason about the next step, click or type, observe the result, and continue.

Reflexion extends this loop by adding self-reflection and memory. After a failed attempt, the agent writes a natural-language reflection and stores it for later trials. This shows that agent behavior can be improved through verbal feedback and episodic memory, without updating model weights. For web agents, this is important because failures are common: wrong clicks, loops, bad search queries, incorrect extractions, and incomplete workflows require recovery mechanisms.

Toolformer strengthens the tool-use dimension. It shows that language models can learn when and how to call external tools through self-supervised data generation. This is important because web agents need external tools to overcome LLM limitations: search, browsing, calculation, data extraction, validation, and API access. However, Toolformer alone does not provide long-horizon tool orchestration or grounded browser control.

Tree of Thoughts adds deliberate planning and search. It generalizes chain-of-thought into a tree of intermediate reasoning states, allowing the model to generate, evaluate, prune, and backtrack among candidate thoughts. This is relevant for web automation because a web agent should not always follow the first action sequence it generates. It may need to compare alternative plans and backtrack when a path is unpromising.

LATS then unifies several previous directions. It combines ReAct-style reasoning and acting, Tree-of-Thought-style search, Reflexion-style feedback, and Monte Carlo Tree Search. LATS is especially important because it directly combines reasoning, acting, planning, self-reflection, and external environment feedback. It therefore provides one of the strongest bridges from general agent architecture to web-agent planning.

CoALA provides the conceptual architecture for organizing all these components. It frames language agents through memory, action spaces, and decision-making procedures. It distinguishes internal actions such as reasoning, retrieval, and learning from external actions such as grounding in an environment. For web agents, this is very useful because it provides the vocabulary needed to describe DOM grounding, browser actions, memory retrieval, planning, and feedback.

The two broad agent surveys then position these papers within the larger agent landscape. Xi et al. organize LLM agents around brain, perception, and action. Wang et al. organize autonomous agents around profile, memory, planning, and action. Together, these surveys show that LLM-based agents are not isolated methods, but a rapidly growing research field with shared architectural modules, application areas, evaluation challenges, and risks.

---

## 3. Refined S3 architecture stack

The S3 papers provide the following architectural components:

| Component | Main papers | Role in LLM agents | Relevance for web automation |
|---|---|---|---|
| Modular expert architecture | MRKL | Routes tasks to specialized modules | Browser, APIs, validators, extractors, databases |
| Reasoning-action loop | ReAct | Interleaves thought, action, observation | Core browser automation loop |
| Self-reflection | Reflexion | Learns from failed attempts using language memory | Recovery from loops, wrong clicks, failed extraction |
| Tool use | Toolformer, MRKL | Connects LLMs to external tools/APIs | Search, browser tools, calculators, extraction APIs |
| Deliberate search | Tree of Thoughts | Explores multiple reasoning paths | Alternative plans and candidate workflows |
| Search-based agent planning | LATS | Combines reasoning, acting, planning, feedback | Long-horizon web navigation and WebShop-style tasks |
| Cognitive architecture | CoALA | Organizes memory, actions, decisions | Framework for web-agent architecture |
| General agent taxonomy | Xi et al., Wang et al. | Maps the field and components | Positions web agents in broader agent literature |

---

## 4. Refined conceptual contribution of S3

The central contribution of S3 is that **LLM agency is architectural**.

A model becomes an agent not simply because it is large or instruction-following, but because it is embedded in a system with:

```text
memory
tools
actions
observations
planning
reflection
retrieval
external grounding
decision cycles
```

The S3 papers show the transition from:

```text
LLM as text generator
```

to:

```text
LLM as controller inside an agent architecture
```

This is the essential bridge between foundation LLMs and web agents.

---

## 5. Refined gap after S3 P1

After S3 P0, the gap was:

```text
Early LLM-agent architectures introduce reasoning-action loops, memory, reflection, and tool use, but they still do not fully solve grounded, reliable, safe, and scalable web automation.
```

After adding S3 P1 papers, the gap becomes more precise:

```text
LLM-agent architectures now include modular tools, reasoning-action loops, reflection, memory, search-based planning, and cognitive frameworks, but generalized web automation still requires web-specific grounding, verification, safety, and deployment-aware orchestration.
```

The refined gap is not that agents lack architecture. The refined gap is that general agent architectures still need to be adapted to the web.

They can now support:

```text
reasoning before acting
tool/module selection
reflection after failure
multi-path planning
search over trajectories
memory and retrieval
conceptual architecture
agent taxonomy
```

But they still do not fully solve:

```text
DOM-grounded perception
screenshot-to-action grounding
precise UI element selection
dynamic JavaScript interaction
long-horizon browser workflows
irreversible web actions
robust extraction verification
safe tool orchestration
cost and latency control
generalization across unseen websites
privacy and permission boundaries
```

Therefore, the refined S3 gap is:

```text
General LLM-agent architectures provide the control logic of agency, but web automation requires grounding that control logic in real browser environments with reliable perception, action, verification, and safety.
```

---

## 6. Refined thesis connection

For the thesis topic, **“LLM-based agents for generalized web automation and data extraction,”** S3 supports five major claims.

### Claim 1 — Web agents require modular architecture

MRKL and Toolformer show that LLM agents need external modules and tools. This supports the thesis claim that web automation cannot rely on a single LLM. A robust web agent needs a modular architecture with browser tools, search, DOM parsers, extraction modules, validators, APIs, and memory systems.

### Claim 2 — Web agents require a reasoning-action-observation loop

ReAct shows that agents must connect reasoning to actions and observations. This is the core loop of web automation:

```text
observe page → reason → act → observe result
```

Without this loop, the model remains a text generator rather than an interactive web agent.

### Claim 3 — Web agents require memory and self-correction

Reflexion shows that agents can improve through verbal feedback and episodic memory. For web automation, this matters because agents must recover from errors, loops, incomplete extraction, failed navigation, and wrong assumptions about page structure.

### Claim 4 — Web agents require planning and search

Tree of Thoughts and LATS show that difficult tasks require deliberate planning, alternative trajectory exploration, and backtracking. Web tasks are often long-horizon and uncertain, so the agent must compare candidate actions, evaluate partial progress, and revise plans.

### Claim 5 — Web agents require a cognitive/system framework

CoALA and the surveys show that LLM agents should be understood as systems with memory, perception, action, planning, and evaluation. This supports the thesis structure: later sections can analyze web agents by decomposing them into perception/grounding, planning, training, failure modes, extraction, safety, and deployment.

---

## 7. Refined thesis-ready synthesis paragraph

LLM agent architectures extend foundation language models by embedding them in modular, interactive, and memory-aware systems. MRKL systems introduced the idea that LLMs should be combined with external expert modules, enabling access to current knowledge, proprietary data, exact reasoning, and symbolic tools. ReAct then established the core reasoning-action-observation loop, allowing LLMs to reason about a state, execute an action, receive feedback, and update their next decision. Reflexion extended this loop with verbal self-reflection and episodic memory, showing that agents can improve across attempts without gradient updates. Toolformer further advanced tool use by teaching language models to call external APIs through self-supervised data generation. Tree of Thoughts introduced deliberate search over intermediate reasoning states, while LATS unified reasoning, acting, planning, reflection, and external feedback through language-agent tree search. CoALA and recent surveys then provided broader frameworks for understanding agents as systems with memory, internal and external actions, decision procedures, perception, planning, and evaluation. Together, these works define the architectural foundation of LLM-based agents. For generalized web automation and data extraction, they provide the necessary control components: modularity, tool use, reasoning, action, observation, memory, reflection, and planning. However, they remain insufficient without web-specific grounding, reliable browser action execution, DOM and visual perception, state tracking, extraction verification, safety constraints, and deployment-aware orchestration. This motivates the transition from general LLM-agent architectures to web-specific agent systems and benchmarks.

---

## 8. Refined limitations connected to the thesis

### 8.1 Modularity limitation

MRKL and Toolformer show that external tools are necessary, but tool use is not automatically reliable.

For web agents, this matters because tools must be selected, sequenced, monitored, and verified. Browser automation requires more than a single tool call; it often requires multi-step orchestration across search, navigation, extraction, validation, and storage.

### 8.2 Routing limitation

MRKL relies on a router to select the correct expert module.

For web agents, this matters because wrong routing can send a task to the wrong tool. For example, the agent may use the LLM when it should query the DOM, or scrape text when it should verify with a source.

### 8.3 ReAct limitation

ReAct introduces the action loop, but it often follows one trajectory and can loop or hallucinate.

For web agents, this matters because a wrong trajectory can repeatedly click the wrong element, miss a field, hallucinate page content, or fail silently. This motivates reflection, search, and verification.

### 8.4 Reflexion limitation

Reflexion improves behavior through verbal memory, but it depends on clear failure signals.

For web agents, this matters because many web tasks do not provide explicit success or failure. An extraction can look correct but be wrong. A form can submit with hidden errors. A task can partially succeed. This motivates explicit validators and success detectors.

### 8.5 Toolformer limitation

Toolformer learns tool use, but it does not originally support chained interactive tool use.

For web agents, this matters because web automation requires iterative tool use over time, including search, browsing, inspection, extraction, verification, and storage.

### 8.6 Tree-of-Thoughts limitation

Tree of Thoughts improves planning through search, but it is mainly text-based and can be expensive.

For web agents, this matters because each branch may require browser actions, screenshots, DOM parsing, or tool calls. Search must therefore be selective and cost-aware.

### 8.7 LATS limitation

LATS unifies reasoning, acting, planning, and feedback, but assumes reversibility and increases computation.

For web agents, this matters because many actions are not safely reversible: submitting forms, sending messages, deleting items, or making purchases. LATS-style planning must be adapted with safe exploration policies.

### 8.8 CoALA limitation

CoALA gives a conceptual architecture, but not a concrete web-agent implementation.

For web agents, this matters because the framework must be instantiated with web-specific components: DOM state, browser actions, visual grounding, extraction schemas, validators, and safety policies.

### 8.9 Survey limitation

The surveys provide broad taxonomies, but not detailed solutions for web automation.

For the thesis, they are useful for positioning and structure, but web-specific sections must supply the concrete evidence, benchmarks, systems, and failure analysis.

---

## 9. Updated cross-links to later sections

| Paper | Feeds |
|---|---|
| MRKL | S5.3 tool planning, S5.4 modular generalization, S6 extraction modules, S7 verification, S8 deployment |
| ReAct | S5.3 planning, S5.5 loops/failure modes, S6 search/extraction, S8 deployment |
| Reflexion | S5.3 recovery planning, S5.4 verbal RL/training, S5.5 failures, S7 safety, S8 retry cost |
| Toolformer | S5.3 tool planning, S6 extraction tools, S7 verification, S8 tool cost/latency |
| Tree of Thoughts | S5.3 deliberate planning/search, S5.5 search failure, S8 inference cost |
| LATS | S5.3 search-based web planning, S5.4 gradient-free improvement, S5.5 reversibility/cost failures, S8 deployment |
| CoALA | S5.2 grounding, S5.3 decision cycles, S5.4 memory/learning, S5.5 failure localization, S8 architecture |
| Xi et al. survey | S5.1 evaluation, S5.2 perception/action, S5.3 planning, S7 risks |
| Wang et al. survey | S5.1 evaluation, S5.3 planning, S5.4 memory/capability acquisition, S8 challenges |

---

## 10. Transition to S4 and S5

S3 establishes the general architecture of LLM agents:

```text
LLM + memory + tools + actions + observations + planning + reflection
```

The next question is:

```text
How are these general agent architectures adapted to web environments?
```

This transition leads to web-specific issues:

```text
How does the agent perceive a web page?
How does it represent DOM, HTML, screenshots, forms, and tables?
How does it choose safe browser actions?
How does it plan across multiple pages?
How does it know whether extraction is correct?
How does it avoid loops and hallucinated page states?
How does it operate under cost, latency, and privacy constraints?
```

Therefore, after S3, the literature review should move toward:

- **S4 — Evolution of Web Agent Systems**
  - How general LLM-agent patterns became browser/web agents.

- **S5.1 — Benchmarks and Evaluation**
  - How web-agent success is measured.

- **S5.2 — Perception, Grounding, and Interface Representation**
  - How agents represent web pages, DOMs, screenshots, and UI elements.

- **S5.3 — Planning and Decision-Making**
  - How agents plan and execute long-horizon web tasks.

- **S5.4 — Training Strategies and Generalization**
  - How agents learn from demonstrations, feedback, trajectories, memory, or synthetic data.

- **S5.5 — Failure Modes**
  - How agents fail through loops, hallucinations, grounding errors, unsafe actions, and tool failures.

---

## 11. Final refined S3 synthesis

S3 shows that LLM-based agents emerge when foundation models are embedded inside modular, interactive control architectures. MRKL introduces modular expert routing, showing that LLMs should be combined with external tools and symbolic systems. ReAct establishes the reasoning-action-observation loop that makes LLMs interactive. Reflexion adds verbal memory and self-correction, enabling agents to improve from failed attempts without gradient updates. Toolformer shows that language models can learn to use external tools. Tree of Thoughts introduces deliberate search over reasoning states, while LATS unifies reasoning, acting, planning, feedback, and reflection through language-agent tree search. CoALA and recent surveys provide the broader conceptual and taxonomic frameworks needed to organize these components.

Together, these papers define the architectural foundations required for web agents: modularity, tool use, reasoning, action, observation, memory, reflection, planning, and search. However, they also show that general LLM-agent architectures are not sufficient for generalized web automation and data extraction. The remaining challenge is to ground these architectures in real web environments, where agents must perceive DOM and visual interfaces, execute browser actions safely, track state across long workflows, verify extracted data, recover from failures, and operate under deployment constraints. This refined S3 synthesis therefore motivates the next stage of the literature review: web-specific agent systems, benchmarks, grounding methods, planning techniques, training strategies, and failure analysis.


---


Total files merged: 15
