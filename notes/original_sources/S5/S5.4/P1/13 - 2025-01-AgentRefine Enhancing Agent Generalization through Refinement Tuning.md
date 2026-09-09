# AgentRefine: Enhancing Agent Generalization through Refinement Tuning

## Metadata

- **Short name:** AgentRefine
- **Authors:** Dayuan Fu, Keqing He, Yejie Wang, Wentao Hong, Zhuoma Gongque, Weihao Zeng, Wei Wang, Jingang Wang, Xunliang Cai, Weiran Xu
- **Year used for thesis:** 2025
- **Venue/status:** ICLR 2025 conference paper
- **DOI:** Not found
- **arXiv ID:** arXiv:2501.01702
- **Venue/status source:** online re-check + uploaded PDF metadata
- **S5.4 cluster:** refinement tuning / error correction
- **Priority:** P1
- **BibTeX key:** `fu2025agentrefine`

---

## Simple understanding

This paper belongs to **S5.4 — Training Strategies and Generalization**.

The central idea is:

```text
Trains agents on trajectories where a strong LLM refines erroneous actions using environment feedback, so the model learns to correct mistakes instead of memorizing state-action pairs.
```

For your thesis, this paper helps explain how web agents become better through training, adaptation, synthetic supervision, reward modeling, memory, distillation, environment synthesis, or reinforcement learning.

---

## Four-note template

- **Core idea:**  
  Trains agents on trajectories where a strong LLM refines erroneous actions using environment feedback, so the model learns to correct mistakes instead of memorizing state-action pairs.

- **Key finding:**  
  Refinement tuning improves generalization and robustness across diverse agent tasks.

- **Limitation connected to thesis:**  
  Refinement labels still depend on strong teacher quality and may not provide verifiable extraction correctness.

- **Connects to:**  
  Reflexion, WebCoT, S5.5 recovery, S5.4 training.

- **Use in thesis:**  
  Use for training agents to recover from mistakes.

---

## Detailed notes

### 1. Training signal

The paper contributes one of the following S5.4 training signals:

```text
refinement tuning / error correction
```

This matters because web agents cannot rely only on prompt engineering. They need supervision from demonstrations, trajectories, reward models, environment interaction, synthetic tasks, or self-improvement loops.

### 2. What is being learned?

The agent is learning some combination of:

```text
web navigation policy
element grounding
action formatting
planning routines
recovery behavior
memory use
reward-guided behavior
environment-specific procedural knowledge
```

The exact emphasis for this paper is:

```text
Trains agents on trajectories where a strong LLM refines erroneous actions using environment feedback, so the model learns to correct mistakes instead of memorizing state-action pairs.
```

### 3. Why it improves generalization

The paper’s generalization mechanism is:

```text
Refinement tuning improves generalization and robustness across diverse agent tasks.
```

This is important for your thesis because generalized web automation must work across unseen pages, changing DOM structures, different visual layouts, and new workflows.

### 4. Why it is not enough for your thesis

The paper still leaves a thesis-specific gap:

```text
Refinement labels still depend on strong teacher quality and may not provide verifiable extraction correctness.
```

For **LLM-based agents for generalized web automation and data extraction**, the missing piece is usually not only task success. The agent must also produce correct, structured, verifiable outputs.

---

## Thesis relevance

This paper supports the argument that web-agent training is moving from isolated prompting toward data- and feedback-driven improvement.

The important S5.4 claim is:

```text
web agents need training signals aligned with long-horizon interaction,
not only language modeling or static instruction following.
```

For data extraction, this becomes:

```text
navigation training
+ grounding training
+ extraction schema training
+ source-evidence verification
+ safety-aware rewards
```

Most S5.4 papers improve the first two or three components, but they rarely optimize the full extraction pipeline.

---

## Limitation as thesis gap

Use this paper to motivate the following gap:

```text
Current web-agent training improves task completion,
but it usually does not jointly optimize:
- structured extraction correctness
- field-level schema adherence
- source provenance
- evidence preservation
- safe irreversible actions
- cross-site generalization
- reproducible and affordable deployment
```

So this paper is useful, but it should not be presented as a complete solution for your thesis.

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | Training depends on webpage representation, screenshots, DOM/AxTree, grounding, and context |
| **S5.3** | Training improves planning, decomposition, rollback, and long-horizon behavior |
| **S5.5** | Training changes failure modes: loops, wrong page, failure to recover, hallucinated tasks, noisy trajectories |
| **S6** | Extraction needs training data and rewards for schema, evidence, and field correctness |
| **S8** | Deployment depends on cost, reproducibility, safety, open data/models, and environment realism |

---

## Thesis-ready paragraph

AgentRefine contributes to S5.4 by showing that web-agent behavior can be improved through a specific training or adaptation mechanism: Trains agents on trajectories where a strong LLM refines erroneous actions using environment feedback, so the model learns to correct mistakes instead of memorizing state-action pairs. The main result is that Refinement tuning improves generalization and robustness across diverse agent tasks. For the thesis, this paper is important because it moves web agents beyond prompt-only behavior and toward learned, reusable, or self-improving interaction skills. However, Refinement labels still depend on strong teacher quality and may not provide verifiable extraction correctness. Therefore, it should be used as evidence for progress in web-agent training while preserving the thesis gap around generalized, source-verifiable web data extraction.

---

## One-sentence summary

AgentRefine shows that **Trains agents on trajectories where a strong LLM refines erroneous actions using environment feedback, so the model learns to correct mistakes instead of memorizing state-action pairs**, but generalized web data extraction still needs schema-aware, source-verifiable, and safety-aware training objectives.

---

## BibTeX

```bibtex
@inproceedings{fu2025agentrefine,
  title     = {AgentRefine: Enhancing Agent Generalization through Refinement Tuning},
  author    = {Dayuan Fu, Keqing He, Yejie Wang, Wentao Hong, Zhuoma Gongque, Weihao Zeng, Wei Wang, Jingang Wang, Xunliang Cai, Weiran Xu},
  booktitle = {ICLR 2025},
  year      = {2025},
  url       = {https://openreview.net/forum?id=FDimWzmcWn},
  eprint    = {2501.01702},
  archivePrefix = {arXiv}
}
```

---

## Source links

- https://openreview.net/forum?id=FDimWzmcWn
- https://arxiv.org/abs/2501.01702
