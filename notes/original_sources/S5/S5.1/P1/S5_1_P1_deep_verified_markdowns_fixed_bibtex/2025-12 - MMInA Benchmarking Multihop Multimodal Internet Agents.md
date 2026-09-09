# Paper 365 — MMInA: Benchmarking Multihop Multimodal Internet Agents

## Metadata

- **Title:** MMInA: Benchmarking Multihop Multimodal Internet Agents
- **Authors:** Ziniu Zhang, Shulin Tian, Liangyu Chen, Ziwei Liu
- **Year:** 2025
- **Venue/status:** Findings of ACL 2025
- **DOI:** 10.18653/v1/2025.findings-acl.703
- **arXiv ID:** arXiv:2404.09992
- **Final publication status:** Final venue verified online: Findings of ACL 2025.
- **Verification source:** https://aclanthology.org/2025.findings-acl.703.pdf ; https://arxiv.org/abs/2404.09992
- **Thesis section:** S5.1 — Web Agent Benchmarks and Evaluation
- **Benchmark type:** Multihop multimodal internet-agent benchmark
- **Priority:** P1
- **BibTeX key:** mmina2025

---

## Simple understanding

This paper contributes to **S5.1 — Benchmarks and Evaluation** by addressing the question:

```text
How should we evaluate web/GUI/browser agents beyond simple static accuracy?
```

Its main focus is:

```text
Multihop multimodal internet-agent benchmark
```

Scale / setting:

```text
1,050 human-written tasks across domains such as shopping and travel.
```

In simple terms, this paper matters because it adds a new evaluation angle that is not fully captured by the S5.1 P0 benchmarks. The P0 papers already cover offline real-web action prediction, executable self-hosted environments, visual grounding, and multi-turn dialogue. This P1 paper extends that landscape by making one specific benchmark pressure more visible: realism, difficulty, domain specialization, human preference, safety, long-horizon navigation, temporal robustness, or scalable benchmark generation.

---

## Notes

- **Core idea:**  
  Evaluate agents on compositional tasks requiring multimodal information extraction across multiple websites.

- **Key finding:**  
  Agents often fail on early hops; memory augmentation improves single-hop and multihop browsing.

- **Main limitation connected to thesis:**  
  Focuses on multi-hop information tasks rather than state-changing workflows or structured extraction schemas.

- **Use in thesis:**  
  Use to discuss multihop web information extraction and multimodal cross-site reasoning.

- **Connects to:**  
  S5.2 multimodal perception and grounding

- **BibTeX key:**  
  `mmina2025`

---

## Thesis-ready paragraph

MMInA: Benchmarking Multihop Multimodal Internet Agents extends the benchmark landscape for LLM-based web agents by focusing on **multihop multimodal internet-agent benchmark**. Its central contribution is that it evaluates agent behavior under conditions that are underrepresented in the core S5.1 P0 benchmarks. Specifically, it introduces or analyzes the setting: **1,050 human-written tasks across domains such as shopping and travel.**. This matters for the thesis because generalized web automation and structured data extraction cannot be evaluated only by a single success score or by a single environment type. A robust web agent must generalize across websites, handle dynamic or multimodal content, maintain long-horizon context, avoid unsafe actions, and produce verifiable outputs. The paper's main finding is that **Agents often fail on early hops; memory augmentation improves single-hop and multihop browsing.**. However, its limitation is equally important: **Focuses on multi-hop information tasks rather than state-changing workflows or structured extraction schemas.**. Therefore, the paper should be used as a P1 support reference that sharpens the S5.1 benchmark taxonomy and motivates later technical sections on grounding, planning, training, failure modes, safety, and deployment.

---

## Why this paper matters for my thesis

This paper is relevant because your thesis is not only asking:

```text
Can an agent complete a web task?
```

It is asking a stronger question:

```text
Can an LLM-based agent operate reliably across diverse, dynamic, realistic websites
and extract or deliver verifiable structured information?
```

This benchmark contributes one important evaluation pressure:

```text
Multihop multimodal internet-agent benchmark
```

For generalized web automation, this matters because benchmark design determines which failures become visible. A benchmark that only checks final answer accuracy may hide trajectory errors. A benchmark that only uses static pages may hide live-web brittleness. A benchmark that only tests text may hide visual grounding failures. A benchmark that ignores safety may overestimate deployment readiness.

This paper therefore helps build a richer evaluation map for S5.1.

---

## Important concepts to remember

### 1. Evaluation setting

The benchmark/evaluation setting is:

```text
Multihop multimodal internet-agent benchmark
```

This tells us what kind of agent capability the paper mainly stresses.

### 2. Scale and environment

The scale/environment is:

```text
1,050 human-written tasks across domains such as shopping and travel.
```

This matters because benchmark scale affects both generalization claims and evaluation cost.

### 3. Measurement philosophy

This paper should be read as part of the broader S5.1 shift:

```text
static accuracy
→ action/trajectory evaluation
→ functional task success
→ multimodal and live-web evaluation
→ safety / reliability / cost / robustness evaluation
```

### 4. Thesis-relevant failure

The key limitation is:

```text
Focuses on multi-hop information tasks rather than state-changing workflows or structured extraction schemas.
```

This limitation should be connected directly to your thesis gap rather than left as a generic paper weakness.

---

## Key evidence from the paper / online verification

### Publication status

Venue/status was re-checked online:

```text
Final venue verified online: Findings of ACL 2025.
```

Verification source:

```text
https://aclanthology.org/2025.findings-acl.703.pdf ; https://arxiv.org/abs/2404.09992
```

### Contribution evidence

The paper's contribution can be summarized as:

```text
Evaluate agents on compositional tasks requiring multimodal information extraction across multiple websites.
```

### Result evidence

The paper's headline finding is:

```text
Agents often fail on early hops; memory augmentation improves single-hop and multihop browsing.
```

---

## Connection to earlier and later papers

### Connection to S5.1 P0 papers

This P1 paper complements the S5.1 P0 benchmarks:

```text
Mind2Web        → offline real-web action prediction
WebArena        → executable self-hosted task completion
VisualWebArena  → visually grounded multimodal evaluation
WebLINX         → multi-turn conversational web navigation
```

Its specific contribution is:

```text
Multihop multimodal internet-agent benchmark
```

### Connection to later thesis sections

- **S5.2 — Perception and grounding:**  
  Relevant when the benchmark stresses screenshots, DOM, HTML, accessibility trees, multimodal cues, or UI changes.

- **S5.3 — Planning and decision-making:**  
  Relevant when tasks are long-horizon, multi-step, multi-site, or require hidden-context investigation.

- **S5.4 — Training and generalization:**  
  Relevant when the benchmark exposes transfer failure, OOD splits, temporal drift, or trajectory-data limitations.

- **S5.5 — Failure modes:**  
  Relevant because benchmark design reveals different failures: grounding failure, hallucinated evidence, poor stopping, repetitive actions, weak memory, or unsafe action selection.

- **S7/S8 — Safety and deployment:**  
  Relevant when evaluation includes live-web risks, safety policies, privacy, cost, latency, or reproducibility.

---

## Limitation connected to thesis

The key thesis limitation is:

```text
Focuses on multi-hop information tasks rather than state-changing workflows or structured extraction schemas.
```

This means the paper should not be used as proof that generalized web automation is solved. Instead, use it to show that the field is progressively expanding benchmark coverage while still leaving the central thesis gap open:

```text
No benchmark fully combines:
large-scale real-web diversity
+ live interaction
+ multimodal grounding
+ structured extraction correctness
+ safety constraints
+ reproducibility
+ cost/latency measurement
+ robust cross-site generalization
```

---

## Reading decision

- **Read fully?** Yes, but depth depends on thesis subsection.
- **Depth needed:** Medium-high for S5.1; high if the benchmark directly supports your evaluation taxonomy.
- **Main use:** Benchmark/evaluation support paper.
- **Most important parts:**
  - Abstract and introduction
  - Benchmark construction
  - Evaluation protocol and metrics
  - Main results
  - Human/agent gap or model comparison
  - Failure analysis
  - Limitations and reproducibility notes

---

## One-sentence summary

MMInA: Benchmarking Multihop Multimodal Internet Agents is a P1 benchmark/evaluation paper that contributes **multihop multimodal internet-agent benchmark** and shows that agents often fail on early hops; memory augmentation improves single-hop and multihop browsing.

---

## BibTeX

```bibtex
@inproceedings{mmina2025,
  title = {MMInA: Benchmarking Multihop Multimodal Internet Agents},
  author = {Ziniu Zhang, Shulin Tian, Liangyu Chen, Ziwei Liu},
  year = {2025},
  booktitle = {Findings of ACL 2025},
  doi = {10.18653/v1/2025.findings-acl.703},
  eprint = {2404.09992},
  archivePrefix = {arXiv},
  url = {https://aclanthology.org/2025.findings-acl.703.pdf}
}
```

---

## Source links

- https://aclanthology.org/2025.findings-acl.703.pdf
- https://arxiv.org/abs/2404.09992
