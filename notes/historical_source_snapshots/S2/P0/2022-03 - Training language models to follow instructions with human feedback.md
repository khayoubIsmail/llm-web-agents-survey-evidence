# Paper 5 — Training Language Models to Follow Instructions with Human Feedback

## Metadata

- **Title:** Training Language Models to Follow Instructions with Human Feedback
- **Authors:** Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe
- **Year:** 2022
- **Venue:** Advances in Neural Information Processing Systems 35 (NeurIPS 2022), Main Conference Track
- **DOI:** 10.48550/arXiv.2203.02155
- **arXiv ID:** arXiv:2203.02155
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Cross-links:** S3 — LLM Agent Architectures; S5.5 — Limitations and Failure Modes; S7 — Security, Robustness, and Trustworthiness
- **Category:** FND / ALIGNMENT / INSTRUCTION-FOLLOWING
- **Paper type:** Method / system training / empirical evaluation
- **Priority:** P0
- **BibTeX key:** ouyang2022training

---

## Simple understanding

This paper introduced **InstructGPT**, a version of GPT-3 fine-tuned to follow user instructions using **human feedback**.

The main problem is that scaling language models does not automatically make them better at following what users want. A large model can still ignore instructions, hallucinate, produce toxic content, or give unhelpful answers.

The paper proposes a training pipeline based on **reinforcement learning from human feedback (RLHF)**:

```text
1. Human demonstrations → supervised fine-tuning
2. Human rankings of model outputs → reward model
3. Reward model → PPO fine-tuning
```

The result is a model that is more aligned with user intent. The authors show that a **1.3B InstructGPT model** can be preferred over the original **175B GPT-3** despite being much smaller.

For my thesis, this paper is foundational because LLM-based agents depend heavily on instruction following. A web agent must understand what the user wants, follow constraints, avoid unsafe behavior, and produce useful outputs. InstructGPT is a major step from general language modeling toward instruction-following systems that can later be used as the core of agents.

---

## Notes

- **Core idea:**
  Fine-tune GPT-3 with human demonstrations and human preference rankings so that the model follows user instructions more helpfully, truthfully, and safely.

- **Key finding:**
  InstructGPT models are preferred over GPT-3 in human evaluations. The paper reports that outputs from a 1.3B InstructGPT model are preferred to outputs from a 175B GPT-3 model, despite having over 100x fewer parameters.

- **Limitation:**
  InstructGPT improves instruction following, but it is still not an autonomous agent.
  For web agents, this matters because following a natural-language instruction is only the first step. A web agent must also observe web states, choose actions, interact with interfaces, handle failures, update plans, and verify extracted data.
  This limitation motivates the move from instruction-following LLMs in S2 to agent architectures in S3 and browser-based web agents in S4/S5.

- **Additional limitation:**
  The model is aligned to the preferences of a specific group of labelers and researchers, not to all users or all affected communities.
  For web agents, this matters because generalized web automation may be deployed across cultures, languages, websites, and user groups with different expectations of helpfulness, risk, privacy, and acceptable behavior.
  This motivates S7 discussions on trustworthiness, human oversight, safety policies, and context-sensitive alignment.

- **Additional limitation:**
  InstructGPT can still make simple mistakes, hallucinate, over-hedge, fail on false premises, and follow harmful instructions.
  For web agents, this matters directly because hallucinated page states, false assumptions, or unsafe compliance can lead to incorrect clicks, wrong submissions, privacy leakage, or harmful automation.
  This motivates verification, grounding, refusal behavior, browser-state feedback, and safety constraints in later web-agent systems.

- **Additional limitation:**
  RLHF can cause performance regressions on some public NLP benchmarks, described as an alignment tax.
  For web agents, this matters because improving helpfulness or safety may trade off with task success, factuality, speed, or robustness.
  This motivates careful evaluation of both agent capability and agent safety, rather than optimizing only user preference or task-completion rate.

- **Connects to:**
  S2 foundations of LLMs for agentic tasks because it turns GPT-3-like models into instruction-following systems.
  It connects to S3 because later agents use instruction-tuned LLMs as their central reasoning and decision-making component.
  It connects to S7 because it introduces alignment, human feedback, safety, truthfulness, and harmlessness as core concerns.

- **Use in thesis:**
  Use this paper to explain the transition from prompt-based large language models to instruction-following models.
  It is a key bridge between GPT-3 and practical LLM agents.
  For the thesis, it supports the claim that web agents require not only scale and in-context learning, but also instruction alignment, preference learning, safety constraints, and human-centered evaluation.

- **BibTeX key:**
  ouyang2022training

---

## Thesis-ready paragraph

Ouyang et al. introduced InstructGPT, a family of GPT-3 models fine-tuned using human feedback to better follow user instructions. Their RLHF pipeline combines supervised fine-tuning on human demonstrations, reward modeling from human preference rankings, and policy optimization with PPO. This work is foundational for LLM-based agents because it shifts large language models from generic next-token predictors toward systems optimized to satisfy user intent. For web automation, instruction following is a necessary prerequisite: an agent must interpret user goals, respect constraints, produce useful outputs, and avoid harmful behavior. However, InstructGPT is still not an autonomous web agent. It does not itself provide browser interaction, environment grounding, long-horizon planning, execution feedback, or robust verification. This limitation marks the boundary between aligned instruction-following models and the later agentic systems required for generalized web automation and data extraction.

---

## Why this paper matters for my thesis

This paper matters because web agents start from user instructions.

Examples of user instructions in web automation:

```text
Find the cheapest flight from Marrakech to Paris.
Extract all product prices from this website.
Fill this application form using my information.
Compare the top five search results.
Download the invoice from my account.
```

A general language model may understand the words but still fail to follow the real user intent.

InstructGPT shows that human feedback can make models better at:

- following explicit instructions,
- satisfying constraints,
- producing more helpful answers,
- reducing hallucinations,
- reducing toxic outputs in some settings,
- and aligning outputs with user preferences.

But this paper does not solve the full web-agent problem.

The thesis connection is:

```text
GPT-3 → InstructGPT → instruction-following LLMs → LLM-based agents → web agents
```

InstructGPT gives the agent a better instruction-following brain, but not the full agent loop.

---

## Important concepts to remember

### 1. Misalignment of language modeling objective

The paper argues that next-token prediction is not the same as following user intent.

A model trained to predict internet text may produce fluent text, but not necessarily helpful, truthful, or safe answers.

For web agents, this is important because the objective should not be only:

```text
generate plausible text
```

It should be closer to:

```text
complete the user's web task correctly, safely, and verifiably
```

### 2. RLHF

RLHF means **reinforcement learning from human feedback**.

The model is not only trained on correct answers. It is trained using human preferences about which output is better.

This is important for tasks where there is no single exact answer, such as writing, summarization, instruction following, and many agent behaviors.

### 3. Three-step training pipeline

The paper uses three main steps:

```text
Step 1: Supervised fine-tuning
Humans write ideal answers to prompts.

Step 2: Reward model training
Humans rank model outputs.

Step 3: PPO fine-tuning
The model is optimized to produce outputs that receive high reward from the reward model.
```

This pipeline became one of the most influential recipes for modern instruction-following LLMs.

### 4. Helpful, honest, harmless

The paper frames alignment around three criteria:

- **Helpful:** follow the user’s intention and help solve the task.
- **Honest / truthful:** avoid fabricating information or misleading users.
- **Harmless:** avoid harmful, biased, toxic, or unsafe outputs.

For web agents, these criteria become even more important because the system can take actions, not only generate text.

### 5. Alignment tax

The paper observes that RLHF can reduce performance on some public NLP benchmarks.

This is called an **alignment tax**.

For my thesis, this concept matters because web-agent design may also involve trade-offs:

```text
task success vs safety
speed vs verification
autonomy vs human control
helpfulness vs refusal
exploration vs risk
```

---

## Key evidence from the paper

### Figure 1 — InstructGPT beats GPT-3 in human preference

Figure 1 shows that InstructGPT models trained with PPO and pretraining mix outperform GPT-3 baselines in human evaluations.

The important result is that a much smaller InstructGPT model can be preferred over a much larger GPT-3 model.

This supports the idea that **alignment and instruction tuning can matter more than scale alone**.

### Figure 2 — The RLHF pipeline

Figure 2 illustrates the three-step method:

```text
SFT → reward model → PPO
```

This figure is the most important methodological figure in the paper.

### Figure 4 — Better instruction following and fewer hallucinations

Figure 4 shows that PPO models:

- attempt the correct instruction more often,
- follow explicit constraints more often,
- are more appropriate for customer assistant use,
- and hallucinate less on closed-domain tasks.

For web agents, this is important because hallucination and instruction failure can directly break automation tasks.

### Figure 8 — Generalization beyond training distribution

The paper shows qualitative examples where InstructGPT follows instructions in French and answers code questions.

This matters because web agents need to generalize to diverse tasks, domains, and sometimes languages.

### Figure 9 — Remaining simple mistakes

Figure 9 shows that InstructGPT still fails on false premises and can over-hedge.

This is important for the thesis because web agents must detect invalid assumptions and avoid acting on false premises.

---

## Connection to later sections

- **S2 — Foundations:**
  This is a core foundation paper for instruction-following LLMs and RLHF.

- **S3 — LLM Agent Architectures:**
  Most later agents rely on instruction-tuned models as their reasoning core.

- **S4 — Evolution of Web Agent Systems:**
  WebGPT and browser-based agents build on instruction-following and human feedback.

- **S5.3 — Planning and Decision-Making:**
  Instruction-following is required before the model can plan actions based on user goals.

- **S5.5 — Limitations and Failure Modes:**
  The paper identifies hallucination, false-premise failure, harmful compliance, and alignment tax.

- **S7 — Security, Robustness, and Trustworthiness:**
  The paper is directly relevant to safety, human preferences, toxicity, bias, refusal behavior, and deployment risk.

- **S8 — Open Challenges and Deployment Realities:**
  RLHF improves user-facing behavior but introduces questions about cost, alignment targets, evaluation, and trade-offs.

---

## Limitation connected to thesis

InstructGPT improves alignment, but it does not solve grounded autonomous task execution.

For my thesis, this matters because generalized web automation and data extraction require the agent to do more than answer instructions.

A full web agent must perform:

```text
instruction understanding
→ page observation
→ state representation
→ reasoning and planning
→ action execution
→ feedback interpretation
→ error recovery
→ data extraction
→ verification
```

InstructGPT mainly improves:

```text
instruction understanding
→ response generation
```

Therefore, its limitation is not simply that it still makes mistakes. The thesis-relevant limitation is that instruction following alone is insufficient for robust web automation. The model must be embedded inside an agent architecture with tools, browser control, memory, grounding, safety constraints, and execution-based evaluation.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High
- **Main use:** Foundation for instruction-following LLMs, RLHF, and alignment
- **Most important parts:**
  - Abstract
  - Introduction
  - Figure 1
  - Figure 2
  - Section 3.1: high-level methodology
  - Section 3.2: dataset
  - Section 3.5: models
  - Section 3.6: evaluation
  - Section 4.1: results on API distribution
  - Section 4.3: qualitative results
  - Section 5.2: who are we aligning to?
  - Section 5.3: limitations
  - Section 5.4: open questions

---

## One-sentence summary

InstructGPT showed that fine-tuning language models with human feedback makes them much better at following user intent, but instruction alignment alone is not enough for grounded, reliable, and safe web-agent execution.

---

## BibTeX

```bibtex
@inproceedings{ouyang2022training,
  title     = {Training Language Models to Follow Instructions with Human Feedback},
  author    = {Ouyang, Long and Wu, Jeff and Jiang, Xu and Almeida, Diogo and Wainwright, Carroll L. and Mishkin, Pamela and Zhang, Chong and Agarwal, Sandhini and Slama, Katarina and Ray, Alex and Schulman, John and Hilton, Jacob and Kelton, Fraser and Miller, Luke and Simens, Maddie and Askell, Amanda and Welinder, Peter and Christiano, Paul and Leike, Jan and Lowe, Ryan},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {35},
  year      = {2022},
  eprint    = {2203.02155},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  doi       = {10.48550/arXiv.2203.02155}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2203.02155
- NeurIPS proceedings: https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html
