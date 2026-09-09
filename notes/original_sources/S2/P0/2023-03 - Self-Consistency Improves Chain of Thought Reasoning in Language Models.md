# Paper 4 — Self-Consistency Improves Chain of Thought Reasoning in Language Models

## Metadata

- **Title:** Self-Consistency Improves Chain of Thought Reasoning in Language Models
- **Authors:** Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou
- **Year:** 2023
- **First arXiv version:** 2022
- **Venue:** International Conference on Learning Representations (ICLR 2023)
- **Publication type:** Conference paper / ICLR poster
- **DOI:** 10.48550/arXiv.2203.11171
- **arXiv ID:** arXiv:2203.11171
- **OpenReview ID:** 1PL1NIMMrw
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Cross-links:** S5.3 — Planning and Decision-Making; S5.5 — Limitations and Failure Modes
- **Category:** FND / REASONING
- **Paper type:** Method / decoding strategy
- **Priority:** P0
- **BibTeX key:** wang2023selfconsistency

---

## Simple understanding

This paper improves **chain-of-thought prompting**.

Chain-of-thought prompting asks a language model to solve a problem step by step. However, the usual method uses **greedy decoding**, meaning the model produces only one reasoning path. If that path is wrong, the final answer is usually wrong.

The paper proposes **self-consistency**: instead of generating only one reasoning path, the model samples many different reasoning paths, extracts the final answer from each path, and chooses the answer that appears most often.

The intuition is simple: for complex reasoning tasks, there may be many different valid ways to reach the same correct answer. If several reasoning paths independently lead to the same answer, that answer is more likely to be correct.

For my thesis, this paper matters because web agents also need reasoning and decision-making. A web agent may need to choose between several possible actions, plans, or extraction strategies. Self-consistency shows that sampling multiple reasoning paths can improve reliability, but it also reveals an important limitation: reasoning agreement alone does not guarantee grounded correctness in interactive web environments.

---

## Notes

- **Core idea:**
  Introduces self-consistency, a decoding strategy that improves chain-of-thought prompting by sampling multiple reasoning paths and selecting the most frequent final answer.

- **Key finding:**
  Self-consistency significantly improves reasoning accuracy across arithmetic and commonsense reasoning benchmarks. The paper reports large gains such as GSM8K (+17.9%), SVAMP (+11.0%), AQuA (+12.2%), StrategyQA (+6.4%), and ARC-Challenge (+3.9%).

- **Limitation:**
  Self-consistency increases inference cost because it requires multiple sampled reasoning paths instead of one model call.
  For web agents, this matters directly because browser automation is already expensive: each reasoning step may require page observation, DOM parsing, screenshot processing, tool calls, and sometimes real browser actions.
  Using many reasoning samples at every step can make web agents slow, costly, and impractical for long-horizon tasks. This motivates later work on efficient planning, confidence estimation, early stopping, verifier-guided reasoning, and selective use of multi-path reasoning in S5.3 and S5.5.

- **Additional limitation:**
  Self-consistency works best when there is a fixed final answer that can be aggregated by majority vote.
  For web agents, many decisions are not simple fixed-answer problems. The agent may need to choose an action sequence, interact with dynamic pages, or extract structured data where multiple outputs can be partially correct.
  This motivates the need for environment feedback, execution-based verification, and task-specific success criteria rather than only answer voting.

- **Additional limitation:**
  The method can still produce incorrect or nonsensical reasoning paths.
  For web agents, this matters because a consistent answer may still be grounded in a false page interpretation, wrong DOM element, stale observation, or hallucinated state.
  This motivates grounding mechanisms, tool-based verification, and observation-action feedback loops.

- **Connects to:**
  Chain-of-thought prompting, prompt-based reasoning, multi-path reasoning, uncertainty estimation, and later agent planning methods.
  It connects strongly to S5.3 because it improves reasoning reliability, and to S5.5 because it highlights cost, calibration, and grounding limitations.

- **Use in thesis:**
  Use this paper to explain that reasoning quality in LLMs can be improved not only by model scale or fine-tuning, but also by inference-time strategies.
  For web agents, self-consistency can be presented as an early method for improving decision reliability through multiple candidate reasoning paths.
  However, it should also be used to motivate why web agents need more than text-only reasoning: they require grounded verification through browser state, DOM evidence, and action feedback.

- **BibTeX key:**
  wang2023selfconsistency

---

## Thesis-ready paragraph

Wang et al. proposed self-consistency, an inference-time decoding strategy that improves chain-of-thought reasoning by sampling multiple reasoning paths and selecting the most frequent final answer. Rather than relying on a single greedy reasoning trace, self-consistency treats reasoning paths as latent alternatives and marginalizes over them through answer aggregation. This substantially improves performance on arithmetic and commonsense reasoning benchmarks, showing that large language models benefit from diverse intermediate reasoning. For LLM-based web agents, the paper is important because it introduces a simple mechanism for improving reasoning robustness without additional training. However, the method is not a complete solution for web automation: it increases inference cost, assumes answer aggregation is possible, and does not guarantee that the reasoning is grounded in the actual web environment. These limitations motivate later agentic methods that combine reasoning with browser observation, tool execution, verification, and feedback-driven planning.

---

## Why this paper matters for my thesis

This paper matters because web agents need reliable reasoning.

A web agent often has to reason about questions such as:

```text
Which button should I click next?
Which search result is relevant?
Which field corresponds to the requested information?
Should I scroll, search, go back, or submit?
Is the extracted value reliable?
Did the previous action succeed?
```

A single reasoning path can be wrong. Self-consistency shows that asking the model to produce multiple reasoning paths and choosing the most consistent answer can improve reliability.

However, web automation is not only a reasoning benchmark. It is an interactive process. The agent must act in a changing environment.

So the thesis connection is:

```text
Chain-of-thought reasoning → self-consistency → more reliable reasoning → but still not grounded web agency
```

Self-consistency is useful, but it needs to be combined with:

- web page observation,
- DOM or screenshot grounding,
- action execution,
- feedback from the browser,
- memory of previous steps,
- and verification of final extracted data.

---

## Important concepts to remember

### 1. Chain-of-thought prompting

Chain-of-thought prompting asks the model to generate intermediate reasoning steps before giving the final answer.

Example:

```text
Question: Janet has 16 eggs. She eats 3 and uses 4 for muffins. She sells the rest for $2 each. How much does she make?

Reasoning:
16 - 3 - 4 = 9 eggs left.
9 × 2 = 18.
Answer: $18
```

### 2. Greedy decoding problem

Standard chain-of-thought often uses greedy decoding.

That means the model gives only one reasoning path.

If the model makes a mistake early, the final answer may be wrong.

### 3. Self-consistency

Self-consistency samples many reasoning paths.

Example:

```text
Path 1 → answer 18
Path 2 → answer 26
Path 3 → answer 18
Path 4 → answer 14
Path 5 → answer 18
```

The final answer is **18**, because it is the most frequent.

### 4. Majority vote over answers

The method does not choose the reasoning path with the highest probability.

Instead, it chooses the answer with the strongest agreement across multiple reasoning paths.

### 5. Reasoning diversity

The key idea is that correct answers are more likely to be reached by multiple different reasoning paths.

This makes diversity useful, not harmful.

---

## Key evidence from the paper

### Figure 1 — Method overview

Figure 1 shows the complete self-consistency pipeline:

```text
CoT prompt → sample diverse reasoning paths → aggregate final answers → choose most consistent answer
```

The example shows that greedy decoding gives the wrong answer, while multiple sampled reasoning paths recover the correct answer by majority agreement.

### Table 2 — Arithmetic reasoning results

The paper reports strong gains on arithmetic reasoning tasks.

Important examples:

- GSM8K: +17.9%
- SVAMP: +11.0%
- AQuA: +12.2%
- MultiArith: strong improvement across models

This matters because arithmetic reasoning is a common proxy for multi-step reasoning.

### Table 3 — Commonsense and symbolic reasoning results

Self-consistency also improves commonsense reasoning and symbolic reasoning.

Important examples:

- StrategyQA: +6.4%
- ARC-Challenge: +3.9%
- Coinflip and letter concatenation also improve with sufficient model scale.

### Figure 2 — More sampled paths improve accuracy

The paper shows that increasing the number of sampled reasoning paths usually improves performance.

This supports the idea that reasoning diversity is useful.

### Table 5 — Helps when chain-of-thought hurts

The paper also shows that chain-of-thought can sometimes hurt performance, but self-consistency can recover and improve performance.

This is important for my thesis because web agents may sometimes generate misleading rationales. More reasoning is not always better unless it is checked or aggregated.

---

## Connection to later sections

- **S2 — Foundations:**
  Self-consistency is a core inference-time reasoning method for LLMs.

- **S5.3 — Planning and Decision-Making:**
  It connects to multi-path reasoning, candidate action selection, planning robustness, and uncertainty estimation.

- **S5.5 — Limitations and Failure Modes:**
  It highlights major issues: cost, unreliable rationales, ungrounded reasoning, and overconfidence.

- **S6 — Web Information Extraction:**
  It can support extraction tasks where multiple candidate outputs are generated and the most consistent structured answer is selected.

- **S8 — Deployment Realities:**
  Its computational cost is important when deploying web agents in real browser environments.

---

## Limitation connected to thesis

Self-consistency improves reasoning, but it does not solve grounded web interaction.

For my thesis, this matters because web automation requires an agent to close the loop between:

```text
instruction → observation → reasoning → action → feedback → correction → extraction
```

Self-consistency mainly improves this part:

```text
reasoning → answer selection
```

It does not directly solve:

- choosing reliable browser actions,
- verifying that a click succeeded,
- grounding reasoning in DOM elements,
- handling dynamic page changes,
- managing long action histories,
- deciding when to stop,
- or validating extracted data against the live page.

Therefore, self-consistency is important as a reasoning reliability technique, but not sufficient as a complete agent architecture.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Medium
- **Main use:** Foundation for reasoning reliability and inference-time planning
- **Most important parts:**
  - Abstract
  - Introduction
  - Figure 1
  - Section 2: Self-consistency over diverse reasoning paths
  - Table 2 and Table 3
  - Section 3.3: when chain-of-thought hurts
  - Section 3.4: comparison with beam search and sample-and-rank
  - Section 3.5: robustness and uncertainty
  - Conclusion and limitations

---

## One-sentence summary

Self-consistency improves chain-of-thought reasoning by sampling multiple reasoning paths and choosing the most consistent final answer, but for web agents it must be combined with grounding, verification, and feedback from the browser environment.

---

## BibTeX

```bibtex
@inproceedings{wang2023selfconsistency,
  title     = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
  author    = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed H. and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
  booktitle = {International Conference on Learning Representations},
  year      = {2023},
  eprint    = {2203.11171},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  doi       = {10.48550/arXiv.2203.11171},
  url       = {https://openreview.net/forum?id=1PL1NIMMrw}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2203.11171
- OpenReview: https://openreview.net/forum?id=1PL1NIMMrw
