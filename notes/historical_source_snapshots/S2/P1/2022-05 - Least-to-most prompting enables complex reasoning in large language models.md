# Paper 11 — Least-to-Most Prompting Enables Complex Reasoning in Large Language Models

## Metadata

- **Title:** Least-to-Most Prompting Enables Complex Reasoning in Large Language Models
- **Authors:** Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Claire Cui, Olivier Bousquet, Quoc Le, Ed Chi
- **Year:** 2023
- **Venue:** International Conference on Learning Representations (ICLR 2023)
- **DOI:** 10.48550/arXiv.2205.10625
- **arXiv ID:** arXiv:2205.10625
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Cross-links:** S5.3 — Planning and Decision-Making; S5.5 — Failure Modes
- **Category:** FND / DECOMPOSITION / REASONING
- **Paper type:** Method / prompting strategy
- **Priority:** P1
- **BibTeX key:** zhou2023least

---

## Simple understanding

This paper improves over basic chain-of-thought by explicitly decomposing complex problems into simpler subproblems and solving them in order. The method has two stages: first ask the model to decompose the problem, then ask it to solve each subproblem sequentially using previous answers.

For the thesis, this is highly relevant because web automation is naturally decompositional. A web task usually requires a sequence of subgoals and browser actions, not one answer.

---

## Notes

- **Core idea:**
  Introduces least-to-most prompting, a decomposition-based prompting strategy that breaks a complex task into simpler subproblems and solves them sequentially.

- **Key finding:**
  Least-to-most prompting improves easy-to-hard generalization, especially on compositional and symbolic reasoning tasks such as SCAN, where it strongly outperforms standard chain-of-thought.

- **Limitation:**
- Least-to-most depends on the quality of the decomposition. For web agents, this matters because a wrong decomposition can cause the agent to follow the wrong workflow, skip required steps, or interact with the wrong page elements.
- The method solves textual subproblems, not grounded browser states. For web agents, each subproblem must be mapped to a concrete action such as click, type, search, or extract.
- Sequential decomposition can accumulate errors. For web agents, one wrong substep may propagate through the action history and cause long-horizon failure, motivating feedback, reflection, and recovery mechanisms.

- **Connects to:**
  Connects CoT to planning and hierarchical decomposition. It is directly relevant to web-agent planning and task decomposition.

- **Use in thesis:**
  Use in S2 as a reasoning foundation and in S5.3 as a precursor to agent planning methods that decompose web tasks into subgoals.

- **BibTeX key:**
  zhou2023least

---

## Thesis-ready paragraph

Zhou et al. proposed least-to-most prompting, a strategy that decomposes a complex problem into simpler subproblems and solves them sequentially. Compared with ordinary chain-of-thought prompting, least-to-most explicitly structures reasoning as progressive subproblem solving and improves easy-to-hard generalization. This is highly relevant to web agents because generalized web automation requires decomposing user goals into ordered subgoals and browser actions. However, the method remains a text-only reasoning strategy: it does not ground subproblems in actual DOM elements, browser state, or execution feedback. Its thesis-relevant limitation is that decomposition alone is insufficient unless each subproblem is connected to grounded actions and verified outcomes.

---

## Why this paper matters for my thesis

This paper matters because it adds one important capability to the foundation of LLM-based agents.

For my thesis, the important question is not only:

```text
What can the model do?
```

but also:

```text
What is still missing for generalized web automation and data extraction?
```

This paper supports the S2 narrative because it helps explain how LLMs became useful as the cognitive core of agents. At the same time, its limitations show why a pure language model or prompting method is not enough. A web agent must connect language understanding and reasoning to browser perception, grounded actions, feedback, memory, safety, and verification.

---

## Important concepts to remember

- Decomposition stage: generate subproblems from the original problem.
- Subproblem solving stage: solve each subproblem in sequence.
- Easy-to-hard generalization: solve harder test problems than demonstrations.
- Hierarchical reasoning: a precursor to hierarchical planning in agents.

---

## Connection to Section S2 narrative

This paper fits into S2 as part of the transition from general language modeling to agent-relevant capabilities.

The broad S2 arc is:

```text
Transformer architecture
→ pretraining
→ transfer learning
→ in-context learning
→ instruction following
→ reasoning
→ retrieval / grounding
→ multimodal and long-context models
```

This paper contributes to one part of that arc and helps prepare the transition toward S3 and S5, where LLMs are embedded inside agent architectures for planning, tool use, memory, browser control, and web-specific grounding.

---

## Limitation connected to thesis

The most important thesis-relevant limitation is:

```text
This work improves an LLM capability, but it does not by itself create a reliable grounded web agent.
```

For generalized web automation and data extraction, the system must still solve:

```text
instruction understanding
→ web/page observation
→ DOM or visual grounding
→ reasoning and planning
→ action execution
→ feedback interpretation
→ error recovery
→ structured extraction
→ verification
```

Therefore, this paper should be used as a foundation, not as a complete web-agent solution.

---

## Reading decision

- **Read fully?** Yes, as a P1 paper
- **Depth needed:** High. Focus on Figure 1, method section, SCAN results, error analysis, and comparison with CoT.
- **Main use:** Strengthen S2 foundation and support later S3/S5/S6/S7 links
- **Read after:** S2 P0 papers
- **Use while writing:** S2 foundation narrative and relevant cross-linked sections

---

## One-sentence summary

Introduces least-to-most prompting, a decomposition-based prompting strategy that breaks a complex task into simpler subproblems and solves them sequentially. Its main thesis relevance is that it strengthens the LLM foundation, but still requires agent-level grounding, interaction, and verification for web automation.

---

## BibTeX

```bibtex
@inproceedings{zhou2023least,
  title     = {Least-to-Most Prompting Enables Complex Reasoning in Large Language Models},
  author    = {Zhou, Denny and Scharli, Nathanael and Hou, Le and Wei, Jason and Scales, Nathan and Wang, Xuezhi and Schuurmans, Dale and Cui, Claire and Bousquet, Olivier and Le, Quoc and Chi, Ed},
  booktitle = {International Conference on Learning Representations},
  year      = {2023},
  eprint    = {2205.10625},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  doi       = {10.48550/arXiv.2205.10625}
}
```

---

## Source links

- https://arxiv.org/abs/2205.10625
- https://openreview.net/forum?id=WZH7099tgfM
