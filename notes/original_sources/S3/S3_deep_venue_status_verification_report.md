# S3 Venue / Journal Status Deep Verification

## Scope

Section S3 papers checked:

```text
P0 = 3 papers
P1 = 6 papers
Total = 9 papers
```

Checked papers:

```text
1. ReAct
2. Reflexion
3. Toolformer
4. MRKL Systems
5. Tree of Thoughts
6. Cognitive Architectures for Language Agents / CoALA
7. The Rise and Potential of Large Language Model Based Agents: A Survey
8. Language Agent Tree Search / LATS
9. A Survey on Large Language Model based Autonomous Agents
```

---

## Final status table

| # | Priority | Paper | Status in current note | Deep-verified final status | Decision |
|---:|---|---|---|---|---|
| 1 | P0 | ReAct: Synergizing Reasoning and Acting in Language Models | ICLR 2023 | ICLR 2023, notable top 5% | Good |
| 2 | P0 | Reflexion: Language Agents with Verbal Reinforcement Learning | NeurIPS 2023 | NeurIPS 2023 | Good |
| 3 | P0 | Toolformer: Language Models Can Teach Themselves to Use Tools | NeurIPS 2023 | NeurIPS 2023 | Good |
| 4 | P1 | MRKL Systems | arXiv / AI21 technical report | arXiv preprint / AI21 Labs technical report, 2022 | Good; no final peer-reviewed venue found |
| 5 | P1 | Tree of Thoughts | NeurIPS 2023 / arXiv preprint | NeurIPS 2023 | Fix BibTeX to conference paper |
| 6 | P1 | Cognitive Architectures for Language Agents | TMLR 02/2024 | Transactions on Machine Learning Research, 02/2024 | Good |
| 7 | P1 | The Rise and Potential of Large Language Model Based Agents: A Survey | arXiv survey | Science China Information Sciences, 68, 121101, 2025 | Update venue/status |
| 8 | P1 | Language Agent Tree Search | ICML 2024 / PMLR 235 | ICML 2024, PMLR 235, pp. 62138–62160 | Good |
| 9 | P1 | A Survey on Large Language Model based Autonomous Agents | Frontiers of Computer Science, 2025 | Frontiers of Computer Science, 18, 186345, 2024 | Fix year/status |

---

## Required corrections

## 1. Tree of Thoughts

Current note says venue is NeurIPS 2023, but the BibTeX is still arXiv-style.

Use conference-style BibTeX:

```bibtex
@inproceedings{yao2023tree,
  title     = {Tree of Thoughts: Deliberate Problem Solving with Large Language Models},
  author    = {Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Thomas L. and Cao, Yuan and Narasimhan, Karthik},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {36},
  year      = {2023},
  eprint    = {2305.10601},
  archivePrefix = {arXiv},
  url       = {https://papers.nips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html}
}
```

## 2. The Rise and Potential of Large Language Model Based Agents: A Survey

Current note says arXiv survey only.

Correct final status:

```text
Science China Information Sciences
Volume 68
Article number 121101
Year 2025
DOI: 10.1007/s11432-024-4222-0
```

Recommended BibTeX:

```bibtex
@article{xi2025rise,
  title   = {The Rise and Potential of Large Language Model Based Agents: A Survey},
  author  = {Xi, Zhiheng and Chen, Wenxiang and Guo, Xin and He, Wei and Ding, Yiwen and Hong, Boyang and Zhang, Ming and Wang, Junzhe and Jin, Senjie and Zhou, Enyu and Zheng, Rui and Fan, Xiaoran and Wang, Xiao and Xiong, Limao and Zhou, Yuhao and Wang, Weiran and Jiang, Changhao and Zou, Yicheng and Liu, Xiangyang and Yin, Zhangyue and Dou, Shihan and Weng, Rongxiang and Cheng, Wensen and Zhang, Qi and Qin, Wenjuan and Zheng, Yongyan and Qiu, Xipeng and Huang, Xuanjing and Gui, Tao},
  journal = {Science China Information Sciences},
  volume  = {68},
  pages   = {121101},
  year    = {2025},
  doi     = {10.1007/s11432-024-4222-0}
}
```

Suggested BibTeX key change:

```text
xi2023rise → xi2025rise
```

You can keep `xi2023rise` if you want stability across your notes, but the final bibliography should show year 2025.

## 3. A Survey on Large Language Model based Autonomous Agents

Current note says:

```text
Year used for thesis: 2025
Venue: Frontiers of Computer Science, 2025
```

Correct final status:

```text
Frontiers of Computer Science
Volume 18
Article number 186345
Year 2024
DOI: 10.1007/s11704-024-40231-1
Published: 22 March 2024
Version of record: 22 March 2024
```

Recommended BibTeX:

```bibtex
@article{wang2024survey,
  title   = {A Survey on Large Language Model based Autonomous Agents},
  author  = {Wang, Lei and Ma, Chen and Feng, Xueyang and Zhang, Zeyu and Yang, Hao and Zhang, Jingsen and Chen, Zhiyuan and Tang, Jiakai and Chen, Xu and Lin, Yankai and Zhao, Wayne Xin and Wei, Zhewei and Wen, Jirong},
  journal = {Frontiers of Computer Science},
  volume  = {18},
  pages   = {186345},
  year    = {2024},
  doi     = {10.1007/s11704-024-40231-1}
}
```

Suggested BibTeX key change:

```text
wang2025survey → wang2024survey
```

## 4. MRKL Systems

Keep as:

```text
arXiv preprint / AI21 Labs technical report, 2022
```

No final peer-reviewed conference or journal venue was found in this check.

## 5. CoALA

Current note is correct:

```text
Transactions on Machine Learning Research, 02/2024
```

Recommended BibTeX can stay:

```bibtex
@article{sumers2024cognitive,
  title   = {Cognitive Architectures for Language Agents},
  author  = {Sumers, Theodore R. and Yao, Shunyu and Narasimhan, Karthik and Griffiths, Thomas L.},
  journal = {Transactions on Machine Learning Research},
  year    = {2024},
  eprint  = {2309.02427},
  archivePrefix = {arXiv},
  url     = {https://openreview.net/forum?id=1i6ZCvflQJ}
}
```

## 6. LATS

Current note is correct, but add pages:

```text
Proceedings of the 41st International Conference on Machine Learning
PMLR 235
Pages 62138–62160
Year 2024
```

Recommended BibTeX:

```bibtex
@inproceedings{zhou2024language,
  title     = {Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models},
  author    = {Zhou, Andy and Yan, Kai and Shlapentokh-Rothman, Michal and Wang, Haohan and Wang, Yu-Xiong},
  booktitle = {Proceedings of the 41st International Conference on Machine Learning},
  series    = {Proceedings of Machine Learning Research},
  volume    = {235},
  pages     = {62138--62160},
  year      = {2024},
  publisher = {PMLR},
  url       = {https://proceedings.mlr.press/v235/zhou24r.html}
}
```

---

## Final verdict

```text
S3 is mostly correct.
No paper needs to be removed.
No duplicate found.
Two major venue/status updates are needed:
  1. Xi et al. survey is now Science China Information Sciences 2025.
  2. Wang et al. survey is Frontiers of Computer Science 2024, not 2025.
One BibTeX correction is needed:
  Tree of Thoughts should be @inproceedings for NeurIPS 2023, not only arXiv.
```

## Final corrected S3 status list

```text
P0:
- ReAct → ICLR 2023
- Reflexion → NeurIPS 2023
- Toolformer → NeurIPS 2023

P1:
- MRKL Systems → arXiv / AI21 technical report, 2022
- Tree of Thoughts → NeurIPS 2023
- CoALA → TMLR 2024
- The Rise and Potential of LLM-Based Agents → Science China Information Sciences 2025
- LATS → ICML 2024 / PMLR 235
- A Survey on LLM-Based Autonomous Agents → Frontiers of Computer Science 2024
```
