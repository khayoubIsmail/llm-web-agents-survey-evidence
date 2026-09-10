# OS-ATLAS: A Foundation Action Model for Generalist GUI Agents

## Metadata

- **Short name:** OS-Atlas
- **Authors:** Zhiyong Wu, Zhenyu Wu, Fangzhi Xu, Yian Wang, Qiushi Sun, Chengyou Jia, Kanzhi Cheng, Zichen Ding, Liheng Chen, Paul Pu Liang, Yu Qiao
- **Year:** 2025
- **Venue/status:** ICLR 2025 Spotlight
- **DOI:** Not found
- **arXiv ID:** arXiv:2410.23218
- **Venue/status source:** ICLR 2025 / OpenReview
- **S5.2 cluster:** Foundation action model for GUI agents
- **Priority:** P1
- **BibTeX key:** `osatlas2025`

---

## Simple understanding

This paper belongs to **S5.2: Perception, Grounding, and Web-State Representation**.

The main idea is:

```text
Builds a generalist GUI action model using a large cross-platform GUI grounding corpus and unified action modeling across web, desktop, and mobile.
```

For the thesis, the important point is that this paper helps explain how web/GUI agents represent the current interface before making a decision. It is not only about planning. It is about how the agent sees the page, selects useful information, grounds actions, and keeps the observation manageable.

---

## Four-note template

- **Core idea:**  
  Builds a generalist GUI action model using a large cross-platform GUI grounding corpus and unified action modeling across web, desktop, and mobile.

- **Key finding:**  
  OS-Atlas improves OOD GUI grounding and agentic tasks over previous open-source models, showing that scale and cross-platform grounding data matter.

- **Limitation connected to thesis:**  
  Large-scale data and training are required, and generalized action prediction still does not guarantee task-level safety or extraction verification; for the thesis, it is strong grounding infrastructure but not a web-extraction solution by itself.

- **Connects to:**  
  SeeClick, UGround, UI-TARS, ShowUI, Magma.

- **Use in thesis:**  
  Use to discuss scaling laws/data infrastructure for generalist GUI grounding.

---

## Detailed notes

- Releases a synthesis toolkit for GUI grounding data across Windows, Linux, macOS, Android, and the web.
- Curates over 13M GUI elements from more than 2.3M screenshots.
- Works in grounding mode, action mode, and agent mode.
- Addresses action naming conflicts across platforms.

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

OS-Atlas contributes to the S5.2 discussion by showing that web/GUI-agent reliability depends on how the interface is represented and grounded before action execution. Builds a generalist GUI action model using a large cross-platform GUI grounding corpus and unified action modeling across web, desktop, and mobile. The main lesson for the thesis is that perception and grounding are not auxiliary modules; they directly determine whether an LLM-based agent can select the correct element, preserve the relevant page state, and execute a valid action. However, Large-scale data and training are required, and generalized action prediction still does not guarantee task-level safety or extraction verification; for the thesis, it is strong grounding infrastructure but not a web-extraction solution by itself. This makes the paper useful for motivating the thesis gap around generalized, robust, and verifiable web automation and data extraction.

---

## One-sentence summary

OS-Atlas shows that **Builds a generalist GUI action model using a large cross-platform GUI grounding corpus and unified action modeling across web, desktop, and mobile**, but the thesis still needs robust grounding and extraction-oriented verification.

---

## BibTeX

```bibtex
@inproceedings{osatlas2025,
  title     = {OS-ATLAS: A Foundation Action Model for Generalist GUI Agents},
  author    = {Zhiyong Wu, Zhenyu Wu, Fangzhi Xu, Yian Wang, Qiushi Sun, Chengyou Jia, Kanzhi Cheng, Zichen Ding, Liheng Chen, Paul Pu Liang, Yu Qiao},
  booktitle = {International Conference on Learning Representations},
  year      = {2025},
  url       = {https://openreview.net/forum?id=n9PDaFNi8t},
  eprint    = {2410.23218},
  archivePrefix = {arXiv}
}
```

---

## Source links

- https://openreview.net/forum?id=n9PDaFNi8t
- https://arxiv.org/abs/2410.23218
