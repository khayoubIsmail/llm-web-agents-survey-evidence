# Paper 6 — Emergent Abilities of Large Language Models

## Metadata

- **Title:** Emergent Abilities of Large Language Models
- **Authors:** Jason Wei et al.
- **Year:** 2022
- **Venue / status:** Transactions on Machine Learning Research
- **Publication type:** Peer-reviewed journal-style paper
- **arXiv ID:** arXiv:2206.07682
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Cross-links:** S3 — LLM Agent Architectures; S5.3 — Planning and Decision-Making
- **Category:** FND / EMERGENCE / SCALE
- **Paper type:** Conceptual / survey-style analysis
- **Priority:** P2
- **BibTeX key:** wei2022emergent

## Simple understanding

This paper discusses **emergent abilities** in large language models: abilities that are absent in smaller models but appear in larger models.

The paper argues that some capabilities cannot be predicted simply by extrapolating from small models. Examples include few-shot prompting, chain-of-thought reasoning, and other task behaviors.

For the thesis, this paper helps explain why LLM-based agents became possible only after models reached sufficient scale.

## Notes

- **Core idea:**  
  Some LLM capabilities appear only after a scale threshold.

- **Key contribution:**  
  Defines emergent abilities and surveys examples from prior work.

- **Key finding:**  
  Certain tasks show near-random performance at small scale and much better performance at larger scale.

- **Thesis limitation:**  
  Emergence is descriptive, not a complete explanation. It does not explain how to build reliable agents or guarantee robust behavior.

- **Connection to agents:**  
  Agentic abilities such as instruction following, reasoning, tool use, and planning are often associated with model scale and emergent behavior.

- **Use in thesis:**  
  Use it to explain why scaling transformed LLMs from text generators into models usable as reasoning cores for agents.

## Thesis-ready paragraph

Wei et al. introduced the notion of emergent abilities in large language models, describing capabilities that are not present in smaller models but appear once models reach sufficient scale. This concept is important for LLM-based agents because many agent-relevant behaviors, such as few-shot adaptation, reasoning, and instruction following, became practically useful only in large-scale models. However, emergence does not guarantee reliability: an ability may appear on benchmarks while remaining brittle in interactive web environments that require grounding, action execution, and verification.

## Why this paper matters for my thesis

This paper matters because it gives a vocabulary for discussing why LLM-based agents became possible after scaling. It supports the argument that agentic systems depend on capabilities that were not obvious in smaller language models.

## Reading decision

- **Read fully?** No
- **Depth needed:** Medium
- **Main use:** Emergence and scale discussion
- **Most important parts:** Abstract, definition of emergence, few-shot prompted tasks, augmented prompting

## One-sentence summary

Emergent Abilities explains how scale can produce new LLM capabilities, but it does not solve reliability or grounded agency.

---
