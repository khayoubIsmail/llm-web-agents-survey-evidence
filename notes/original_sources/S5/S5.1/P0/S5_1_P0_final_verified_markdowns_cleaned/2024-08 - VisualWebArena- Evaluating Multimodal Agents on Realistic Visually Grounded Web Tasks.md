# Paper 303 — VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks

## Metadata

- **Title:** VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks
- **Authors:** Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Russ Salakhutdinov, Daniel Fried
- **Year:** 2024
- **Venue:** Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL 2024), Long Papers, pp. 881-905
- **DOI:** 10.18653/v1/2024.acl-long.50
- **arXiv ID:** arXiv:2401.13649
- **Final publication status:** Final venue verified online: ACL 2024 Long Papers.
- **Verification source:** ACL Anthology: https://aclanthology.org/2024.acl-long.50/
- **Thesis section:** S5.1 — Benchmarks and Evaluation
- **Cross-links:** S4 multimodal web agents; S5.2 visual grounding; S5.3 multimodal planning; S5.5 visual failure modes; S7 visual verification; S8 multimodal deployment
- **Category:** MULTIMODAL WEB AGENT BENCHMARK / VISUAL GROUNDING / WEB ARENA EXTENSION
- **Paper type:** Benchmark environment + multimodal evaluation
- **Priority:** P0
- **BibTeX key:** koh2024visualwebarena

## Citation note

Preferred final citation for VisualWebArena.


---

## Simple understanding

VisualWebArena extends WebArena to evaluate multimodal web agents on visually grounded tasks.

WebArena mainly evaluates text/accessibility-tree agents. VisualWebArena argues that this misses an important part of real web use: many tasks require visual understanding.

Examples include:

```text
buy the green polo shirt
find the latest image post containing animals
create a listing for the object shown in an input image
select the cheapest red car in a price range
```

VisualWebArena contains:

```text
910 visually grounded tasks
3 environments: Classifieds, Shopping, Reddit
self-hosted reproducible websites
visual reward functions
input images in 25.2% of tasks
Set-of-Marks style screenshots
```

For my thesis, VisualWebArena is central because generalized web automation and data extraction cannot rely only on text or DOM. Agents must connect screenshots, image content, layout, and DOM/action targets.

---

## Notes

- **Core idea:**
  Introduce a realistic benchmark for multimodal web agents on visually grounded web tasks, extending WebArena with visual reasoning and visual evaluation.

- **Key finding:**
  VLM agents outperform text-only agents, but the best GPT-4V + Set-of-Marks agent still reaches only about 16.4% success, far below human performance of 88.7%.

- **Limitation:**
  VisualWebArena improves multimodal evaluation but still uses self-hosted environments, not the fully live open web.

- **Additional limitation:**
  Some visual reward functions depend on external VLM/LLM evaluators, which introduces evaluator-model dependence.

- **Additional limitation:**
  The benchmark tests visual grounding, but not all real deployment issues such as login, privacy, CAPTCHAs, irreversible actions, and changing websites.

- **Additional limitation:**
  Even strong multimodal models struggle with fine-grained visual reasoning, OCR, exhaustive search, and long-horizon task completion.

- **Connects to:**
  WebArena, SeeAct, WebVoyager, multimodal grounding, Set-of-Marks prompting, visual data extraction, and UI perception.

- **Use in thesis:**
  Use as the main S5.1 P0 benchmark for evaluating multimodal web agents and visual grounding.

---

## Thesis-ready paragraph

VisualWebArena extends WebArena by introducing visually grounded web tasks that require agents to process screenshots, images, webpage structure, and natural-language goals together. The benchmark contains 910 tasks across Classifieds, Shopping, and Reddit environments, with all tasks requiring visual understanding and 25.2% involving input images. It also proposes Set-of-Marks-style annotated screenshots that label interactable elements with bounding boxes and IDs, making visual observations more actionable for VLM agents. For this thesis, VisualWebArena is a key S5.1 benchmark because generalized web automation and data extraction often require visual information that is absent from text or DOM representations. Its results show that multimodality helps, but current VLM agents remain far from human performance, exposing the gap between visual perception and reliable web action grounding.

---

## Why this paper matters for my thesis

This paper matters because many web tasks are not purely textual.

A DOM or accessibility tree may not tell the agent:

```text
which product is red
which post image contains animals
which car in the picture matches the user request
which object from an input image should be listed
```

VisualWebArena therefore makes the evaluation more realistic for modern interfaces.

For the thesis, it supports the claim:

```text
generalized web automation requires multimodal grounding, not only HTML parsing
```


---

## Important concepts to remember

### 1. Visually grounded task

A web task where success depends on visual information such as images, colors, layout, or visual object identity.

### 2. Set-of-Marks prompting

Annotating interactable elements on a screenshot with bounding boxes and IDs so the model can reference them.

### 3. Visual reward functions

Evaluation functions such as VQA-based checks or image similarity checks.

### 4. Multimodal agent

An agent that uses text, screenshots, image inputs, and/or structured page representations.

### 5. Accessibility tree + captions

A hybrid representation where image captions are added to the accessibility tree.

### 6. SoM representation

Screenshot plus marked elements and textual labels for direct visual grounding.

### 7. Execution-based evaluation

Checking whether the final state satisfies the task goal.

---

## Key evidence from the paper

### Benchmark scale

VisualWebArena introduces 910 visually grounded tasks across three self-hosted environments.

### Visual input

25.2% of tasks include input images requiring interleaved image-text understanding.

### Environment design

Classifieds is newly introduced; Shopping and Reddit are inherited from WebArena.

### Human-agent gap

Human performance is 88.7%, while the best VLM agent reaches about 16.4%.

### Text-only limitation

The best text-only GPT-4 agent reaches about 7.25%; adding captions improves performance; multimodal agents improve further.

### SoM result

Set-of-Marks improves GPT-4V performance over screenshot + accessibility tree, showing that action-space marking improves navigability.

---

## Connection to earlier and later papers

### Connection to WebArena

VisualWebArena builds directly on WebArena but changes the task distribution toward visual grounding.

```text
WebArena = realistic functional web tasks
VisualWebArena = realistic functional web tasks + visual grounding
```

### Connection to SeeAct and WebVoyager

SeeAct and WebVoyager show multimodal agents can reason over webpages, but grounding remains difficult.

VisualWebArena gives a benchmark to measure that difficulty.

### Connection to S5.2

The paper directly motivates S5.2 because it compares accessibility trees, screenshots, image captions, and Set-of-Marks observations.

### Connection to S6

For web data extraction, visual grounding is necessary when information appears in images, product photos, screenshots, or layout-dependent regions.

---

## Connection to later thesis sections

- **S5.1 — Benchmarks and Evaluation:**
  Core multimodal web-agent benchmark.
- **S5.2 — Perception and Grounding:**
  Screenshots, accessibility trees, image captions, Set-of-Marks.
- **S5.3 — Planning:**
  Long-horizon visually grounded web tasks.
- **S5.5 — Failure Modes:**
  Visual misunderstanding, OCR errors, poor exhaustive search, and grounding failure.
- **S6 — Data Extraction:**
  Visual information extraction from webpages.
- **S7 — Verification:**
  VLM/LLM-based evaluators and visual correctness checks.
- **S8 — Deployment:**
  Need for multimodal agents in real user interfaces.

---

## Limitation connected to thesis

VisualWebArena is crucial but does not fully solve generalized multimodal web automation.

It improves:

```text
visual grounding evaluation + multimodal benchmark tasks + execution-based visual rewards
```

but it does not fully solve:

- live open-web generalization,
- evaluator reliability for VQA/fuzzy visual tasks,
- safe deployment,
- cost-efficient screenshot processing,
- robust OCR and fine-grained visual grounding,
- or structured extraction verification.

For the thesis, VisualWebArena strengthens the S4 central gap: no system yet combines reliable DOM grounding, visual grounding, live-web generalization, safe deployment, structured extraction, and cost efficiency.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Very high
- **Main use:** S5.1 P0 benchmark/evaluation cornerstone paper
- **Most important parts:**
  - Abstract
  - Figure 1 benchmark examples
  - Observation/action space
  - Evaluation functions
  - Task creation
  - Table 3 main results
  - Set-of-Marks analysis
  - Human performance
  - Failure analysis

---

## One-sentence summary

VisualWebArena shows that multimodal web-agent evaluation is necessary, but current VLM agents remain far below human performance on visually grounded web tasks.

---

## BibTeX

```bibtex
@inproceedings{koh2024visualwebarena,
  title     = {VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks},
  author    = {Koh, Jing Yu and Lo, Robert and Jang, Lawrence and Duvvur, Vikram and Lim, Ming and Huang, Po-Yu and Neubig, Graham and Zhou, Shuyan and Salakhutdinov, Russ and Fried, Daniel},
  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages     = {881--905},
  year      = {2024},
  publisher = {Association for Computational Linguistics},
  doi       = {10.18653/v1/2024.acl-long.50},
  url       = {https://aclanthology.org/2024.acl-long.50/}
}
```

---

## Source links

- https://aclanthology.org/2024.acl-long.50/
- https://arxiv.org/abs/2401.13649
- https://jykoh.com/vwa
