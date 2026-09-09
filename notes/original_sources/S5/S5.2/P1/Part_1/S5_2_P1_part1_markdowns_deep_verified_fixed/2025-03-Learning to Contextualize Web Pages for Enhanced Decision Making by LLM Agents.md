# Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents

## Metadata

- **Short name:** LCoW
- **Authors:** Dongjun Lee, Juyong Lee, Kyuyoung Kim, Jihoon Tack, Jinwoo Shin, Yee Whye Teh, Kimin Lee
- **Year:** 2025
- **Venue/status:** ICLR 2025
- **DOI:** Not found
- **arXiv ID:** arXiv:2503.10689
- **Venue/status source:** ICLR 2025 / OpenReview / arXiv
- **S5.2 cluster:** Web-page contextualization / observation simplification
- **Priority:** P1
- **BibTeX key:** `lcow2025`

---

## Simple understanding

This paper belongs to **S5.2: Perception, Grounding, and Web-State Representation**.

The main idea is:

```text
Decouples web-page understanding from decision-making by training a contextualization module that rewrites complex raw observations into focused, comprehensible observations for LLM agents.
```

For the thesis, the important point is that this paper helps explain how web/GUI agents represent the current interface before making a decision. It is not only about planning. It is about how the agent sees the page, selects useful information, grounds actions, and keeps the observation manageable.

---

## Four-note template

- **Core idea:**  
  Decouples web-page understanding from decision-making by training a contextualization module that rewrites complex raw observations into focused, comprehensible observations for LLM agents.

- **Key finding:**  
  LCoW improves success rates for closed-source and open-source agents on WorkArena and achieves strong WebShop performance.

- **Limitation connected to thesis:**  
  It improves decision context but still depends on the quality of the contextualizer and underlying raw observation; for the thesis, it helps observation reduction but does not solve source-grounded extraction verification.

- **Connects to:**  
  LineRetriever, WebAgent HTML summarization, S5.2 observation representation, S6 extraction.

- **Use in thesis:**  
  Use as the main P1 paper for contextualizing raw HTML/accessibility-tree observations.

---

## Detailed notes

- Transforms raw, long web observations into focused observations with explanations.
- Trains the contextualizer using rewards based on whether action models predict correct actions.
- Shows raw observation complexity can be a larger bottleneck than reasoning ability.
- Very relevant to cost-efficient web automation and data extraction.

---

## Thesis relevance

This paper supports the S5.2 claim that web agents require a reliable interface representation before they can act. For generalized web automation and data extraction, this matters because an agent must identify the right elements, ignore irrelevant page noise, preserve source evidence, and avoid grounding mistakes that cascade through a workflow.

The direct thesis connection is:

```text
better page representation / grounding
→ better action selection
→ more reliable web automation
→ more trustworthy data extraction
```

---

## Limitation as thesis gap

The remaining gap is not simply model accuracy. The thesis-relevant gap is that current systems still do not jointly solve:

```text
robust page perception
+ reliable element grounding
+ long-context observation reduction
+ live-web changes
+ structured extraction correctness
+ source-grounded verification
+ cost efficiency
```

So this paper should be used as part of the S5.2 technical decomposition, not as a final solution.

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.1** | Benchmark/evaluation context for web and GUI agents |
| **S5.2** | Main relevance: perception, representation, grounding, context selection |
| **S5.3** | Better observations improve planning and next-action decisions |
| **S5.5** | Grounding, parsing, and context errors become failure modes |
| **S6** | Web data extraction needs grounded fields, tables, values, and evidence |
| **S8** | Cost, latency, live-web robustness, and deployment constraints |

---

## Thesis-ready paragraph

LCoW contributes to the S5.2 discussion by showing that web/GUI-agent reliability depends on how the interface is represented and grounded before action execution. Decouples web-page understanding from decision-making by training a contextualization module that rewrites complex raw observations into focused, comprehensible observations for LLM agents. The main lesson for the thesis is that perception and grounding are not auxiliary modules; they directly determine whether an LLM-based agent can select the correct element, preserve the relevant page state, and execute a valid action. However, It improves decision context but still depends on the quality of the contextualizer and underlying raw observation; for the thesis, it helps observation reduction but does not solve source-grounded extraction verification. This makes the paper useful for motivating the thesis gap around generalized, robust, and verifiable web automation and data extraction.

---

## One-sentence summary

LCoW shows that **Decouples web-page understanding from decision-making by training a contextualization module that rewrites complex raw observations into focused, comprehensible observations for LLM agents**, but the thesis still needs robust grounding and extraction-oriented verification.

---

## BibTeX

```bibtex
@inproceedings{lcow2025,
  title     = {Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents},
  author    = {Dongjun Lee, Juyong Lee, Kyuyoung Kim, Jihoon Tack, Jinwoo Shin, Yee Whye Teh, Kimin Lee},
  booktitle = {International Conference on Learning Representations},
  year      = {2025},
  url       = {https://openreview.net/forum?id=3Gzz7ZQLiz},
  eprint    = {2503.10689},
  archivePrefix = {arXiv}
}
```

---

## Source links

- https://openreview.net/forum?id=3Gzz7ZQLiz
- https://arxiv.org/abs/2503.10689
