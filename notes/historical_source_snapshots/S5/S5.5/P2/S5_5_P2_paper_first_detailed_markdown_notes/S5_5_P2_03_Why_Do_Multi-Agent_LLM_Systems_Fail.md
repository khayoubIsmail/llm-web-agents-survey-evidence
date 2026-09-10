# S5.5 P2 Paper 03 — Why Do Multi-Agent LLM Systems Fail?

## Metadata

- **Title:** Why Do Multi-Agent LLM Systems Fail?
- **Year:** 2025
- **Verified venue/status:** NeurIPS 2025 Datasets and Benchmarks Track Spotlight
- **Peer-reviewed status:** Yes
- **Thesis section:** S5.5 — Failure Modes, Robustness, Debugging, Reliability, and Safety of LLM-based Agents
- **Main category:** multi-agent system failure taxonomy
- **S5.5 role:** failure taxonomy and diagnosis
- **Priority:** P2
- **Recommended citation strength:** Strong citation
- **Recommended reading depth:** Medium to high
- **BibTeX key:** `whydomultisystems2025`

---

## Simple understanding

This paper asks why multi-agent LLM systems fail. It introduces MAST, a failure taxonomy, and MAST-Data, a dataset of more than 1,600 annotated multi-agent traces across seven MAS frameworks.

In simple terms:

```text
Problem → LLM-based agents fail in interactive environments in ways that are not captured by simple final-answer accuracy.
Paper → This work studies, categorizes, evaluates, detects, or mitigates such failures.
Goal → Make agent behavior more reliable, diagnosable, safe, and robust.
```

For S5.5, the first task is to understand **what type of failure the paper studies**.  
Only after that should it be linked to P2 priority and to your thesis.

---

## Core idea

Empirically derive and annotate multi-agent system failure modes across system design, inter-agent misalignment, and task verification.

This paper mainly contributes to:

```text
multi-agent system failure taxonomy
```

In the broader agent-reliability pipeline, it fits here:

```text
agent trajectory
→ failure observation
→ failure classification / evaluator / judge / debugger
→ diagnosis of root cause or risk
→ mitigation, refinement, or safer deployment
```

---

## Key finding / main claim

MAS failures often come from system design and coordination problems, not only weak base models. The paper identifies 14 failure modes across 3 main categories.

For S5.5, the important question is:

```text
What does this paper reveal about why agents fail, and how can that failure be detected or reduced?
```

Typical S5.5 failure/reliability dimensions include:

- incorrect trajectory evaluation,
- missing reflection or recovery,
- hallucinated GUI localization,
- OOD/capability-boundary errors,
- navigation errors,
- tool-use and verification errors,
- agent-environment mismatch,
- multi-agent coordination failures,
- blind goal pursuit,
- weak environment understanding,
- and visual/interface bias.

---

## Key evidence to extract from the paper

When reading this paper, extract these evidence points:

- **NeurIPS 2025 Datasets and Benchmarks Track Spotlight status.**
- **MAST taxonomy with 14 failure modes.**
- **MAST-Data: 1,642 annotated traces.**
- **Human inter-annotator agreement and LLM-as-judge agreement.**

Also extract, if available:

- number of tasks/traces/benchmarks,
- failure taxonomy categories,
- judge or evaluator agreement,
- benchmark environment,
- failure rates,
- mitigation effect,
- ablation results,
- and authors' stated limitations.

---

## Limitations

- **Limitation 1:** Focused on multi-agent systems, not only web agents.
- **Limitation 2:** LLM-as-judge annotation still needs calibration and human validation.
- **Limitation 3:** Failure categories may not cover every future MAS architecture.

General thesis-level limitation:

```text
Failure analysis is necessary but not sufficient.
A taxonomy or benchmark identifies the problem, but reliable deployment also needs mitigation, verification, monitoring, and safety constraints.
```

Therefore, this paper should normally be used as **P2 support** unless it becomes central to the S5.5 subsection.

---

## Venue/status caution

Use as a stronger source. Verified status: **NeurIPS 2025 Datasets and Benchmarks Track Spotlight**.

For final thesis writing:

```text
confirmed peer-reviewed venue → stronger citation
workshop paper → useful design/qualitative support
arXiv / preprint / submission → recent trend, cite cautiously
withdrawn submission → cite only as arXiv/preprint
```

---

## Relation to S5.5

This paper belongs in **S5.5** because S5.5 focuses on agent failure modes, reliability, debugging, and safety.

Its role is:

```text
Why Do Multi-Agent LLM Systems Fail?
→ failure taxonomy and diagnosis
→ P2 support for failure/reliability discussion
```

Use the paper after explaining the failure problem first.  
Do not introduce it only as “P2”; introduce the failure mechanism or diagnostic gap.

---

## Relation to the thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because generalized web automation requires agents that do not only act, but also:

```text
detect when they are failing
avoid unsafe or impossible actions
understand environment state
recover from wrong decisions
evaluate whether the task is actually complete
distinguish navigation failure from extraction/tool failure
handle UI and visual bias
```

The paper supports that pipeline by improving:

```text
failure taxonomy and diagnosis
```

---

## How to use this paper in the literature review

Recommended use:

- Use it as **P2 support** in S5.5.
- Extract one precise failure category or diagnostic contribution.
- Extract one quantitative result or qualitative insight.
- Extract one limitation.
- Compare it with other S5.5 failure-analysis papers.
- If it is a preprint/workshop, phrase claims cautiously.

Suggested thesis sentence:

> Why Do Multi-Agent LLM Systems Fail? contributes to S5.5 by addressing **multi-agent system failure taxonomy**, showing that LLM-based agents require explicit failure diagnosis, reliability evaluation, and safety-aware mechanisms beyond task success metrics.

---

## Comparison with nearby S5.5 papers

Compare this paper with:

```text
Autonomous Evaluation and Refinement of Digital Agents
MAST / Why Do Multi-Agent LLM Systems Fail?
Aegis
AgentDebug
GEM OOD Detection
Logit Sharpness / GUI localization bias
BLIND-ACT / Blind Goal-Directedness
Task2Quiz
VAF visual-attribute evaluation
The Amazing Agent Race
```

The comparison question is:

```text
Does this paper study failures in evaluation, perception, planning, environment understanding, safety, navigation, debugging, or multi-agent coordination?
```

---

## Reading decision

- **Keep in S5.5 P2:** Yes
- **Read fully?** Yes, if it becomes part of the S5.5 backbone.
- **Depth needed:** Medium to high
- **Main use:** Support discussion of multi-agent system failure taxonomy
- **Most important parts to read:**
  - Abstract and introduction
  - Failure taxonomy or benchmark design
  - Evaluation setup
  - Main results table
  - Failure examples/case studies
  - Mitigation or debugging method
  - Limitations/discussion

---

## One-sentence summary

Why Do Multi-Agent LLM Systems Fail? is a P2 source for S5.5 because it helps explain **multi-agent system failure taxonomy**, but it should be cited according to its verified venue/status and used mainly to enrich the failure/reliability/safety discussion.

---

## BibTeX placeholder

```bibtex
@misc{whydomultisystems2025,
  title = {Why Do Multi-Agent LLM Systems Fail?},
  year = {2025},
  note = {NeurIPS 2025 Datasets and Benchmarks Track Spotlight. Verify final bibliographic metadata before thesis submission.}
}
```
