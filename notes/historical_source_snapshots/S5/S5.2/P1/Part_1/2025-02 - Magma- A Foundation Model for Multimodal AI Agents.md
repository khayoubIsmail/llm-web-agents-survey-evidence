# Magma: A Foundation Model for Multimodal AI Agents

## Metadata

- **Short name:** Magma
- **Authors:** Jianwei Yang, Reuben Tan, Qianhui Wu, Ruijie Zheng, Baolin Peng, Yongyuan Liang, Yu Gu, Mu Cai, Seonghyeon Ye, Joel Jang, Yuquan Deng, Lars Liden, Jianfeng Gao
- **Year:** 2025
- **Venue/status:** CVPR 2025
- **DOI:** Not found
- **arXiv ID:** arXiv:2502.13130
- **Venue/status source:** CVF Open Access
- **S5.2 cluster:** Multimodal foundation model for agentic action
- **Priority:** P1
- **BibTeX key:** `magma2025`

---

## Simple understanding

This paper belongs to **S5.2: Perception, Grounding, and Web-State Representation**.

The main idea is:

```text
Extends VLMs into multimodal agents by training on heterogeneous vision, video, UI, and robotics data using Set-of-Mark and Trace-of-Mark signals.
```

For the thesis, the important point is that this paper helps explain how web/GUI agents represent the current interface before making a decision. It is not only about planning. It is about how the agent sees the page, selects useful information, grounds actions, and keeps the observation manageable.

---

## Four-note template

- **Core idea:**  
  Extends VLMs into multimodal agents by training on heterogeneous vision, video, UI, and robotics data using Set-of-Mark and Trace-of-Mark signals.

- **Key finding:**  
  Magma shows that SoM and ToM can bridge verbal understanding and spatial-temporal action planning across digital and physical environments.

- **Limitation connected to thesis:**  
  Very broad agentic scope may dilute web-specific extraction analysis; for the thesis, use it as a general foundation-model trend, not the main web-grounding evidence.

- **Connects to:**  
  SoM, UI-TARS, ShowUI, robotics VLA, S5.4 training.

- **Use in thesis:**  
  Use to discuss the broader convergence of web/GUI agents with multimodal action foundation models.

---

## Detailed notes

- Uses SoM for actionable objects in images and ToM for movements in videos.
- Targets UI navigation, visual-language understanding, and robotic manipulation.
- Important because it treats action grounding and planning as pretraining objectives.
- Shows web/GUI automation is part of a wider multimodal agent modeling trend.

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

Magma contributes to the S5.2 discussion by showing that web/GUI-agent reliability depends on how the interface is represented and grounded before action execution. Extends VLMs into multimodal agents by training on heterogeneous vision, video, UI, and robotics data using Set-of-Mark and Trace-of-Mark signals. The main lesson for the thesis is that perception and grounding are not auxiliary modules; they directly determine whether an LLM-based agent can select the correct element, preserve the relevant page state, and execute a valid action. However, Very broad agentic scope may dilute web-specific extraction analysis; for the thesis, use it as a general foundation-model trend, not the main web-grounding evidence. This makes the paper useful for motivating the thesis gap around generalized, robust, and verifiable web automation and data extraction.

---

## One-sentence summary

Magma shows that **Extends VLMs into multimodal agents by training on heterogeneous vision, video, UI, and robotics data using Set-of-Mark and Trace-of-Mark signals**, but the thesis still needs robust grounding and extraction-oriented verification.

---

## BibTeX

```bibtex
@inproceedings{magma2025,
  title     = {Magma: A Foundation Model for Multimodal AI Agents},
  author    = {Jianwei Yang, Reuben Tan, Qianhui Wu, Ruijie Zheng, Baolin Peng, Yongyuan Liang, Yu Gu, Mu Cai, Seonghyeon Ye, Joel Jang, Yuquan Deng, Lars Liden, Jianfeng Gao},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year      = {2025},
  url       = {https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Magma_A_Foundation_Model_for_Multimodal_AI_Agents_CVPR_2025_paper.html},
  eprint    = {2502.13130},
  archivePrefix = {arXiv}
}
```

---

## Source links

- https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Magma_A_Foundation_Model_for_Multimodal_AI_Agents_CVPR_2025_paper.html
- https://arxiv.org/abs/2502.13130
