# S2 - Foundations of LLMs for Agentic Tasks

Generated on: 2026-05-07 23:40

---

## P0 (6 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P0\2017-06 - Attention Is All You Need.md

# Paper 1 — Attention Is All You Need

## Metadata

- **Title:** Attention Is All You Need
- **Authors:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin
- **Year:** 2017
- **Venue:** Advances in Neural Information Processing Systems 30 (NIPS 2017)
- **DOI:** 10.48550/arXiv.1706.03762
- **arXiv ID:** arXiv:1706.03762
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Category:** FND
- **Paper type:** Method
- **Priority:** P0
- **BibTeX key:** vaswani2017attention

---

## Simple understanding

This paper introduced the **Transformer**, the architecture that later became the foundation of modern large language models.

Before the Transformer, most sequence models used **RNNs**, **LSTMs**, or **CNNs**. These models processed sequences in a more sequential way, which made training slower and made long-range dependencies harder to learn.

The Transformer replaces recurrence and convolution with **self-attention**. This means each token can directly attend to other tokens in the sequence. This made training more parallelizable, more scalable, and more effective for sequence modeling tasks such as machine translation.

For my thesis, this paper is not directly about web agents, web automation, or data extraction. It is important because it provides the architectural foundation that later enabled GPT, BERT, T5, multimodal LLMs, and LLM-based agents.

---

## Notes

- **Core idea:**
  Introduces the Transformer, a sequence-to-sequence architecture based entirely on self-attention, without recurrent or convolutional layers.

- **Key finding:**
  Self-attention allows better parallelization, shorter dependency paths between tokens, and strong translation performance. The Transformer achieved state-of-the-art results on WMT 2014 English-German and English-French translation tasks.

- **Limitation:**
  Self-attention has quadratic complexity with sequence length, making very long inputs expensive.
  For web agents, this matters directly because HTML pages, DOM trees, screenshots converted to text, and action histories can exceed the context budget.
  This limitation motivates later work on web representation, DOM pruning, context compression, and long-horizon memory in S5.2 and S5.3.

- **Connects to:**
  S2 foundations of LLMs. It is the architectural starting point for GPT, BERT, T5, multimodal LLMs, and later LLM-based agents.

- **Use in thesis:**
  Use as the first foundation paper to explain why modern LLMs became possible.
  Connect it to web agents by saying that Transformer-based LLMs provide the language understanding, reasoning, and representation capacity later used for web navigation, DOM understanding, action planning, and information extraction.

- **BibTeX key:**
  vaswani2017attention

---

## Thesis-ready paragraph

The Transformer architecture introduced by Vaswani et al. replaced recurrent sequence processing with self-attention, enabling efficient parallel training and direct modeling of long-range token dependencies. This architectural shift is foundational for modern LLMs, which later became the reasoning and decision-making core of LLM-based agents. For web automation, the Transformer is important because web agents must process instructions, HTML/DOM structures, observations, and action histories as sequences. However, the quadratic cost of self-attention also foreshadows a major limitation for web agents: handling long, noisy, and dynamic web contexts.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Medium
- **Main use:** Background foundation
- **Most important parts:** Transformer architecture, self-attention, multi-head attention, positional encoding, motivation for parallelization, limitations for long sequences

---

## BibTeX

```bibtex
@inproceedings{vaswani2017attention,
  title     = {Attention Is All You Need},
  author    = {Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N. and Kaiser, {\L}ukasz and Polosukhin, Illia},
  booktitle = {Advances in Neural Information Processing Systems 30},
  year      = {2017},
  doi       = {10.48550/arXiv.1706.03762},
  eprint    = {1706.03762},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL}
}

---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P0\2018-10 - BERT- Pre-training of Deep Bidirectional Transformers for Language Understanding.md

# Paper 2 — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

## Metadata

- **Title:** BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
- **Authors:** Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova
- **Year:** 2019
- **First arXiv version:** 2018
- **Venue:** Proceedings of NAACL-HLT 2019, Volume 1: Long and Short Papers
- **Pages:** 4171–4186
- **DOI:** 10.18653/v1/N19-1423
- **arXiv ID:** arXiv:1810.04805
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Category:** FND
- **Paper type:** Method
- **Priority:** P0
- **BibTeX key:** devlin2019bert

---

## Simple understanding

This paper introduced **BERT**, one of the most influential Transformer-based language models before the LLM era.

BERT stands for **Bidirectional Encoder Representations from Transformers**. Its main idea is to pre-train a Transformer encoder so that it understands language using both the left and right context of each word.

Before BERT, models such as GPT used left-to-right language modeling. That means each token could only attend to previous tokens. BERT changed this by using **masked language modeling**, where some words are hidden and the model learns to predict them from both directions.

BERT showed that a single pre-trained model can be fine-tuned with only a small output layer for many NLP tasks, such as classification, natural language inference, named entity recognition, and question answering.

For my thesis, BERT is important as a foundation paper. It is not directly about web agents, but it explains how Transformer-based models became strong language understanding systems. This matters because web agents need to understand user instructions, web page text, form labels, buttons, DOM content, and task context.

---

## Notes

- **Core idea:**
  Introduces BERT, a deeply bidirectional Transformer encoder pre-trained on large unlabeled text using masked language modeling and next sentence prediction.

- **Key finding:**
  Bidirectional pre-training significantly improves language understanding. BERT achieved state-of-the-art results on eleven NLP tasks, including GLUE, MultiNLI, SQuAD, and named entity recognition.

- **Limitation:**
  BERT is mainly an encoder-only language understanding model, not an action-generating or interactive agent model.
  For web agents, this matters because understanding web content is only one part of the problem; an agent must also plan, act, observe feedback, recover from failures, and operate across dynamic websites.
  This limitation motivates the later shift from static language understanding models in S2 to agent architectures in S3 and web-agent systems in S4/S5.

- **Connects to:**
  S2 foundations of LLMs. BERT shows how Transformer pre-training can produce reusable language representations for many downstream tasks.
  It connects to later web representation work because DOM text, labels, page content, and user instructions all require contextual language understanding.

- **Use in thesis:**
  Use BERT as a foundation paper to explain the transition from Transformer architecture to pre-trained language models.
  In the thesis narrative, BERT helps show that general-purpose pre-training made it possible to reuse one model across many tasks.
  This idea later supports LLM-based agents, where a pre-trained model is adapted to web navigation, instruction following, and information extraction.

- **BibTeX key:**
  devlin2019bert

---

## Thesis-ready paragraph

BERT extended the Transformer architecture into a general-purpose language understanding model through deep bidirectional pre-training. By using masked language modeling, Devlin et al. enabled the model to condition on both left and right context, producing contextual representations that could be fine-tuned for a wide range of NLP tasks with minimal task-specific architecture. For LLM-based web agents, BERT is important as an early demonstration that pre-trained Transformer models can generalize across language understanding tasks. However, BERT remains a passive understanding model: it does not plan, act, interact with environments, or recover from execution failures. This limitation marks an important boundary between foundation language models and the later agentic systems required for generalized web automation and data extraction.

---

## Why this paper matters for my thesis

BERT matters because web agents need strong language understanding before they can act.

A web agent must understand:

- user instructions,
- web page text,
- form labels,
- buttons and menus,
- search results,
- extracted information,
- task constraints,
- and previous interaction history.

BERT is not a web-agent paper, but it is part of the foundation that made later LLM-based agents possible.

The thesis connection is:

```text
Transformer architecture → pre-trained language models → instruction-following LLMs → LLM-based agents → web agents
```

BERT belongs to the second step of this chain.

---

## Important concepts to remember

### 1. Bidirectional Transformer encoder

BERT uses a Transformer encoder that reads the whole input sequence at once. This allows each token to use both previous and following context.

This is useful for language understanding tasks, especially when the meaning of a word depends on its surrounding text.

### 2. Masked Language Modeling

BERT randomly masks some tokens and trains the model to predict them.

Example:

```text
Input:  The user clicked the [MASK] button.
Target: submit
```

The model must use both left and right context to predict the missing word.

### 3. Next Sentence Prediction

BERT also learns whether two text segments follow each other.

This was designed to help tasks involving sentence-pair understanding, such as question answering and natural language inference.

### 4. Fine-tuning

After pre-training, BERT can be adapted to a specific task by adding a small output layer.

This was important because it showed that one pre-trained model could be reused across many tasks.

---

## Connection to later sections

- **S2 — Foundations:**
  BERT is a core foundation paper for pre-trained Transformer models.

- **S3 — Agent architectures:**
  BERT itself is not an agent, but later agents inherit the idea of using pre-trained models as reusable reasoning or understanding modules.

- **S5.2 — Web perception and representation:**
  BERT connects indirectly to models that represent HTML, DOM text, and web page content, such as MarkupLM and HTML-aware models.

- **S6 — Web information extraction:**
  BERT supports the broader idea that pre-trained language models can be fine-tuned for extraction tasks such as NER, QA, and field-level information extraction.

---

## Limitation connected to thesis

BERT improves language understanding, but it does not solve interaction.

For my thesis, this is important because web automation is not only a language understanding problem. A web agent must:

- understand the page,
- decide what to do,
- click or type,
- observe the result,
- update its plan,
- handle errors,
- and extract structured data.

BERT addresses mostly the first part: understanding. It does not address action, planning, memory, dynamic web environments, or generalization across unseen websites.

So BERT motivates the need for later agentic models.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Medium
- **Main use:** Background foundation
- **Most important parts:**
  - Abstract
  - Introduction
  - BERT architecture
  - Masked Language Modeling
  - Next Sentence Prediction
  - Fine-tuning procedure
  - Results on GLUE and SQuAD
  - Ablation studies

---

## One-sentence summary

BERT showed that deeply bidirectional Transformer pre-training can create reusable language understanding models, but it remains a passive understanding model rather than an interactive agent.

---

## BibTeX

```bibtex
@inproceedings{devlin2019bert,
  title     = {BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding},
  author    = {Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina},
  booktitle = {Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1},
  pages     = {4171--4186},
  year      = {2019},
  publisher = {Association for Computational Linguistics},
  doi       = {10.18653/v1/N19-1423},
  eprint    = {1810.04805},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL}
}
```


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P0\2020-07 - Language Models are Few-Shot Learners.md

# Paper 3 — Language Models are Few-Shot Learners

## Metadata

- **Title:** Language Models are Few-Shot Learners
- **Authors:** Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei
- **Year:** 2020
- **Venue:** Advances in Neural Information Processing Systems 33 (NeurIPS 2020)
- **DOI:** 10.48550/arXiv.2005.14165
- **Proceedings DOI record:** 10.5555/3495724.3495883
- **arXiv ID:** arXiv:2005.14165
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Category:** FND
- **Paper type:** Method / system-scale empirical study
- **Priority:** P0
- **BibTeX key:** brown2020language

---

## Simple understanding

This paper introduced **GPT-3**, a very large autoregressive language model with **175 billion parameters**.

The main idea is that when language models become very large, they can perform many tasks from only:

- a natural language instruction,
- one example,
- or a few examples in the prompt.

This is called **in-context learning**.

Unlike BERT, which usually needs fine-tuning for each task, GPT-3 performs tasks without changing its weights. The task is specified directly inside the input prompt.

For my thesis, this paper is very important because it marks the transition from **pre-trained language models as static NLP models** to **language models as general-purpose task performers**. This is a key step toward LLM-based agents, because agents rely heavily on instruction following, prompt-based adaptation, and task execution without retraining.

---

## Notes

- **Core idea:**
  Scaling autoregressive Transformer language models enables strong zero-shot, one-shot, and few-shot task performance through in-context learning, without task-specific fine-tuning.

- **Key finding:**
  GPT-3 shows that very large language models can perform many NLP tasks by conditioning on natural language prompts and examples. Performance improves with model scale, and few-shot prompting becomes increasingly effective in larger models.

- **Limitation:**
  GPT-3 is still a text prediction model, not a grounded interactive agent.
  For web agents, this matters directly because generalized web automation requires more than generating text: the system must observe web states, select actions, interact with dynamic interfaces, verify outcomes, recover from errors, and extract structured data.
  This limitation motivates the later shift from prompt-based task completion in S2 to agent architectures in S3 and web-interaction systems in S4/S5.

- **Connects to:**
  S2 foundations of LLMs for agentic tasks.
  It connects directly to instruction following, in-context learning, prompt-based task specification, and the later use of LLMs as decision-making cores in web agents.

- **Use in thesis:**
  Use this paper to explain why LLMs became useful beyond classical NLP tasks.
  It supports the thesis narrative that large language models can act as general-purpose task engines, but also shows why agents need additional components such as tools, memory, planning, environment feedback, grounding, and execution control.

- **BibTeX key:**
  brown2020language

---

## Thesis-ready paragraph

Brown et al. introduced GPT-3, a 175-billion-parameter autoregressive language model, and showed that scaling language models substantially improves zero-shot, one-shot, and few-shot performance. The key contribution of this work is the demonstration of in-context learning: tasks can be specified through natural language instructions and examples in the prompt, without gradient-based fine-tuning. For LLM-based web agents, this paper is foundational because it shows that large language models can serve as flexible task-conditioned reasoning engines. However, GPT-3 remains a passive text prediction system. It does not directly interact with web environments, observe state transitions, execute actions, or recover from failures. This limitation motivates the development of agentic architectures that wrap LLMs with planning, tool use, memory, grounding, and feedback mechanisms for generalized web automation and data extraction.

---

## Why this paper matters for my thesis

This paper matters because it introduces the practical idea that a language model can perform a new task from a prompt.

For web automation, this is crucial.

A web agent often receives instructions such as:

```text
Find the price of this product.
Fill this form.
Extract all company names from this page.
Compare these search results.
Book an appointment.
```

GPT-3 shows that a model can interpret such instructions without being fine-tuned for each individual task.

But web automation requires more than instruction understanding. The model must also:

- inspect the current web page,
- choose the next action,
- click, type, scroll, or search,
- observe what changed,
- revise the plan,
- handle unexpected pages,
- and extract structured information.

So GPT-3 provides the **language intelligence**, but not the full **agent loop**.

---

## Important concepts to remember

### 1. In-context learning

In-context learning means the model learns the task from the prompt at inference time.

Example:

```text
Translate English to French:

cat → chat
dog → chien
house →
```

The model infers the pattern and completes the task.

This is important for web agents because many web tasks are specified through natural language instructions and examples rather than supervised datasets.

### 2. Zero-shot, one-shot, and few-shot prompting

- **Zero-shot:** only task instruction is given.
- **One-shot:** one example is given.
- **Few-shot:** several examples are given.

GPT-3 showed that larger models benefit more from examples in the prompt.

### 3. Scaling

The paper shows that increasing model size improves performance across many tasks.

This supports the later idea that LLMs can become general-purpose reasoning and task-execution components.

### 4. No fine-tuning

GPT-3 performs many tasks without updating model weights.

This matters for generalized web automation because it is unrealistic to fine-tune a new model for every website, interface, or extraction task.

### 5. Data contamination and web-scale training

The paper discusses benchmark contamination because GPT-3 is trained on large web corpora.

This connects to my thesis because web agents and web data extraction systems also operate over noisy, duplicated, dynamic, and potentially contaminated web data.

---

## Connection to later sections

- **S2 — Foundations:**
  GPT-3 is a core foundation paper for large-scale language models and in-context learning.

- **S3 — LLM Agent Architectures:**
  Later agents use LLMs as central reasoning modules. GPT-3 explains why prompting can be used as a task interface.

- **S4 — Evolution of Web Agent Systems:**
  WebGPT and later browser agents build on the idea that LLMs can follow instructions and answer questions using text interaction.

- **S5.3 — Planning and Decision-Making:**
  GPT-3 has limited reasoning and planning ability. Later work tries to improve this with ReAct, Tree-of-Thoughts, Reflexion, and explicit planning.

- **S5.5 — Limitations and Failure Modes:**
  GPT-3’s limitations in reasoning, coherence, grounding, and robustness foreshadow many web-agent failure modes.

- **S6 — Web Information Extraction:**
  Few-shot prompting becomes important for extraction tasks where only a few examples of desired output format are available.

---

## Limitation connected to thesis

GPT-3 is flexible, but it is not an autonomous agent.

For my thesis, this matters because generalized web automation and data extraction require an agent to close the loop between:

```text
instruction → observation → reasoning → action → feedback → correction → extraction
```

GPT-3 mainly supports:

```text
instruction → text completion
```

Therefore, the limitation is not only that GPT-3 sometimes fails on benchmarks. The deeper thesis-relevant limitation is that prompt-based language modeling alone does not provide reliable grounded action, state tracking, long-horizon planning, or structured interaction with web environments.

This motivates the need for agent frameworks, tool use, browser interaction, memory, planning, and evaluation benchmarks.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Medium-high
- **Main use:** Foundation for in-context learning and LLM-based task generalization
- **Most important parts:**
  - Abstract
  - Introduction
  - In-context learning definition
  - Zero-shot / one-shot / few-shot setup
  - Model scale and training data
  - Results summary
  - Limitations
  - Broader impacts
  - Data contamination discussion

---

## One-sentence summary

GPT-3 showed that very large language models can perform many tasks from prompts and examples without fine-tuning, but it remains a passive text model rather than a grounded interactive web agent.

---

## BibTeX

```bibtex
@inproceedings{brown2020language,
  title     = {Language Models are Few-Shot Learners},
  author    = {Brown, Tom B. and Mann, Benjamin and Ryder, Nick and Subbiah, Melanie and Kaplan, Jared and Dhariwal, Prafulla and Neelakantan, Arvind and Shyam, Pranav and Sastry, Girish and Askell, Amanda and Agarwal, Sandhini and Herbert-Voss, Ariel and Krueger, Gretchen and Henighan, Tom and Child, Rewon and Ramesh, Aditya and Ziegler, Daniel M. and Wu, Jeffrey and Winter, Clemens and Hesse, Christopher and Chen, Mark and Sigler, Eric and Litwin, Mateusz and Gray, Scott and Chess, Benjamin and Clark, Jack and Berner, Christopher and McCandlish, Sam and Radford, Alec and Sutskever, Ilya and Amodei, Dario},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {33},
  pages     = {1877--1901},
  year      = {2020},
  publisher = {Curran Associates, Inc.},
  eprint    = {2005.14165},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  doi       = {10.48550/arXiv.2005.14165}
}
```


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P0\2022-03 - Training language models to follow instructions with human feedback.md

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


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P0\2023-01 - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.md

# Paper 6 — Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

## Metadata

- **Title:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- **Authors:** Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, Denny Zhou
- **Year:** 2022
- **Latest arXiv version:** 2023
- **Venue:** Advances in Neural Information Processing Systems 35 (NeurIPS 2022)
- **DOI:** 10.48550/arXiv.2201.11903
- **arXiv ID:** arXiv:2201.11903
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Cross-links:** S3 — LLM Agent Architectures; S5.3 — Planning and Decision-Making; S5.5 — Limitations and Failure Modes
- **Category:** FND / REASONING / PROMPTING
- **Paper type:** Method / prompting strategy / empirical evaluation
- **Priority:** P0
- **BibTeX key:** wei2022chain

---

## Simple understanding

This paper introduced **chain-of-thought prompting** as a simple way to improve reasoning in large language models.

The idea is simple: instead of asking the model to directly produce the final answer, the prompt gives examples where the answer includes **intermediate reasoning steps** before the final answer.

Standard prompting:

```text
Question → Final answer
```

Chain-of-thought prompting:

```text
Question → Step-by-step reasoning → Final answer
```

The paper shows that this helps large language models solve tasks requiring arithmetic reasoning, commonsense reasoning, symbolic reasoning, and simple planning-like reasoning.

For my thesis, this paper matters because web agents also need multi-step reasoning. A web agent must often decompose a user instruction into smaller steps, reason about the current page, decide the next action, and revise the plan after feedback. Chain-of-thought prompting is one of the first major methods showing that LLM reasoning can be elicited through prompting without fine-tuning.

---

## Notes

- **Core idea:**
  Chain-of-thought prompting improves reasoning by giving the model few-shot examples that include intermediate natural-language reasoning steps before the final answer.

- **Key finding:**
  Chain-of-thought prompting significantly improves performance on arithmetic, commonsense, and symbolic reasoning tasks, especially for very large models. The paper reports that PaLM 540B with chain-of-thought prompting achieves state-of-the-art performance on GSM8K compared with standard prompting and previous methods.

- **Limitation:**
  Chain-of-thought prompting is an emergent ability mainly observed in very large models; smaller models often produce fluent but illogical reasoning.
  For web agents, this matters directly because deploying large LLMs for browser automation can be expensive, slow, and difficult to scale. Web agents often need repeated reasoning at every step, so relying on very large models for every action increases cost and latency.
  This motivates later work on efficient agent planning, smaller specialized agents, tool-assisted reasoning, and selective reasoning in S5.3 and S8.

- **Additional limitation:**
  The generated reasoning path is not guaranteed to be correct or faithful to the model’s actual decision process.
  For web agents, this matters because a plausible explanation can still lead to a wrong click, incorrect field selection, false extraction, or hallucinated web state.
  This motivates later work on grounding, verification, observation-action feedback, and execution-based evaluation in S5.2, S5.3, and S5.5.

- **Additional limitation:**
  Chain-of-thought works best for tasks with clear intermediate reasoning and final answers.
  For web agents, many tasks are open-ended, dynamic, and interactive: the correct next action depends on page state, hidden UI changes, website-specific constraints, and previous actions.
  This motivates agent architectures that combine reasoning with browser state, memory, planning, and environment feedback.

- **Additional limitation:**
  Chain-of-thought prompting can be sensitive to exemplars, prompt format, and task type.
  For web agents, this matters because generalized web automation cannot rely on hand-crafted prompts for every website or task.
  This motivates automatic prompt construction, reusable agent policies, learned planning strategies, and robust evaluation across many websites.

- **Connects to:**
  S2 because it is a foundational LLM reasoning method.
  S3 because later LLM agents use reasoning traces as part of their agent loop.
  S5.3 because it directly supports planning, decomposition, and multi-step decision-making.
  S5.5 because it exposes reasoning failures, hallucinated rationales, and scaling limitations.

- **Use in thesis:**
  Use this paper to explain how LLMs moved from simple prompt completion toward explicit step-by-step reasoning.
  It supports the argument that reasoning can be elicited from LLMs through prompting, but also shows why reasoning alone is insufficient for robust web automation unless combined with grounding, feedback, verification, and action execution.

- **BibTeX key:**
  wei2022chain

---

## Thesis-ready paragraph

Wei et al. introduced chain-of-thought prompting, a prompting strategy that elicits intermediate reasoning steps from large language models before producing a final answer. By providing few-shot examples containing reasoning traces, the method enables sufficiently large models to decompose complex tasks into intermediate steps and substantially improves performance on arithmetic, commonsense, and symbolic reasoning benchmarks. For LLM-based web agents, this paper is foundational because web automation requires decomposition of user goals into ordered actions, interpretation of intermediate observations, and multi-step decision-making. However, chain-of-thought prompting alone is not sufficient for web agency. It does not guarantee faithful or correct reasoning, works mainly at large model scale, and does not ground the reasoning in a live browser environment. These limitations motivate later agent architectures that combine reasoning traces with action execution, environment feedback, tool use, memory, and verification.

---

## Why this paper matters for my thesis

This paper matters because a web agent needs to reason before acting.

A web automation task is rarely a single-step problem. For example:

```text
Find the cheapest product from this page.
```

The agent may need to reason:

```text
1. Identify product cards.
2. Extract prices.
3. Compare prices.
4. Check availability.
5. Return the cheapest valid product.
```

Another example:

```text
Fill the registration form.
```

The agent may need to reason:

```text
1. Locate the name field.
2. Locate the email field.
3. Detect required fields.
4. Avoid submitting incomplete information.
5. Verify that submission succeeded.
```

Chain-of-thought prompting shows that LLMs can produce this kind of step-by-step decomposition.

But the paper only studies reasoning in text-based benchmarks. It does not solve:

- browser interaction,
- DOM grounding,
- UI element selection,
- action execution,
- dynamic page updates,
- long-horizon memory,
- or verification of final results.

So the thesis connection is:

```text
Chain-of-thought prompting → step-by-step reasoning → agent planning → web-agent decision-making
```

---

## Important concepts to remember

### 1. Chain of thought

A chain of thought is a sequence of intermediate reasoning steps leading to a final answer.

Example:

```text
Question: Roger has 5 tennis balls. He buys 2 cans. Each can has 3 balls. How many balls?
Reasoning: He starts with 5. Two cans contain 2 × 3 = 6. Total is 5 + 6 = 11.
Answer: 11.
```

### 2. Standard prompting vs chain-of-thought prompting

Standard prompting gives examples like:

```text
Q: ...
A: The answer is 11.
```

Chain-of-thought prompting gives examples like:

```text
Q: ...
A: Step 1... Step 2... Therefore, the answer is 11.
```

The difference is that chain-of-thought exposes the intermediate reasoning pattern.

### 3. Emergent reasoning ability

The paper argues that chain-of-thought prompting works mainly in sufficiently large models.

Small models often generate reasoning text, but the reasoning may be illogical or incorrect.

This is important for the thesis because web-agent reasoning quality depends strongly on the underlying model capability.

### 4. Reasoning as decomposition

The method helps models decompose complex problems into smaller steps.

This is directly relevant to web agents because web tasks are naturally decompositional:

```text
goal → subgoals → actions → observations → corrections
```

### 5. Prompting without fine-tuning

The paper does not fine-tune models. It only changes the prompt.

This is important because it shows that reasoning behavior can be elicited from off-the-shelf LLMs.

For web agents, this explains why many early agents relied on prompt engineering rather than specialized training.

---

## Key evidence from the paper

### Figure 1 — CoT vs standard prompting

Figure 1 shows the main difference between standard prompting and chain-of-thought prompting.

Standard prompting gives only the final answer. Chain-of-thought prompting gives intermediate reasoning steps before the final answer.

This figure is the core conceptual contribution of the paper.

### Figure 2 — GSM8K improvement

Figure 2 shows that PaLM 540B with chain-of-thought prompting strongly improves on GSM8K math word problems compared with standard prompting.

This supports the claim that step-by-step reasoning can unlock abilities not visible under normal prompting.

### Figure 4 — Reasoning emerges with scale

Figure 4 shows that chain-of-thought prompting becomes much more effective as model size increases.

This is important because the paper does not claim that any model can reason well with CoT. The effect depends strongly on model scale.

### Figure 5 — Ablation study

Figure 5 compares chain-of-thought prompting with alternatives such as equation-only prompting and reasoning-after-answer prompting.

The result suggests that the benefit does not come only from producing more tokens or writing equations. The natural-language intermediate reasoning steps matter.

### Figure 7 — Commonsense reasoning

Figure 7 shows that chain-of-thought also improves commonsense reasoning tasks, not only arithmetic.

This matters for web agents because web automation often requires commonsense interpretation of page content, labels, and user goals.

### Figure 8 — Symbolic reasoning and length generalization

Figure 8 shows that chain-of-thought helps with symbolic tasks such as letter concatenation and coin-flip state tracking, including longer out-of-domain sequences.

This connects to web agents because action histories and web workflows also require state tracking over multiple steps.

---

## Connection to earlier and later papers

### Connection to GPT-3

GPT-3 showed that LLMs can perform tasks from prompts and examples.

Chain-of-thought extends this idea by showing that examples can include reasoning steps, not only final outputs.

```text
GPT-3: few-shot task learning
CoT: few-shot reasoning pattern learning
```

### Connection to InstructGPT

InstructGPT makes models better at following user instructions.

Chain-of-thought makes models better at reasoning through tasks.

For agents, both are needed:

```text
Instruction following + step-by-step reasoning = foundation for agent behavior
```

### Connection to Self-Consistency

Self-consistency improves chain-of-thought by sampling multiple reasoning paths and selecting the most frequent answer.

So the progression is:

```text
CoT: one reasoning path
Self-consistency: many reasoning paths + answer aggregation
```

### Connection to ReAct

ReAct later combines reasoning traces with actions.

This is very important for the thesis:

```text
CoT: Reason → Answer
ReAct: Reason → Action → Observation → Reason → Action
```

ReAct can be seen as a more agentic extension of chain-of-thought.

---

## Connection to later thesis sections

- **S2 — Foundations:**
  Chain-of-thought is a core foundation paper for reasoning in LLMs.

- **S3 — LLM Agent Architectures:**
  Later agents use reasoning traces as part of their internal decision loop.

- **S5.3 — Planning and Decision-Making:**
  CoT directly supports task decomposition and multi-step reasoning.

- **S5.5 — Limitations and Failure Modes:**
  The paper exposes reasoning hallucinations, unfaithful explanations, scale dependence, and prompt sensitivity.

- **S6 — Web Information Extraction:**
  CoT can help extraction when the model must reason about which fields, entities, or tables are relevant.

- **S8 — Deployment Realities:**
  CoT increases token usage and cost, which matters for real web-agent deployment.

---

## Limitation connected to thesis

Chain-of-thought improves reasoning, but it does not solve grounded web automation.

For my thesis, this matters because generalized web automation requires the full loop:

```text
instruction → observation → reasoning → action → feedback → correction → extraction
```

Chain-of-thought mainly improves:

```text
reasoning → answer
```

It does not directly solve:

- observing the web page,
- grounding reasoning in DOM elements,
- selecting safe and correct actions,
- interacting with dynamic websites,
- verifying that actions succeeded,
- recovering from browser failures,
- or validating extracted data.

Therefore, CoT is a foundational reasoning technique, but not a complete agent architecture.

The paper motivates later work on ReAct, Reflexion, Tree-of-Thoughts, planning-based agents, browser agents, and web-agent evaluation benchmarks.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High
- **Main use:** Foundation for LLM reasoning and later agent planning
- **Most important parts:**
  - Abstract
  - Figure 1
  - Introduction
  - Section 2: Chain-of-Thought Prompting
  - Section 3.2: Arithmetic reasoning results
  - Figure 4
  - Figure 5
  - Section 4: Commonsense reasoning
  - Section 5: Symbolic reasoning
  - Section 6: Discussion and limitations
  - Appendix A.1 and A.2 for scale and prompt robustness
  - Appendix D for error analysis

---

## One-sentence summary

Chain-of-thought prompting shows that large language models can solve harder reasoning tasks when prompted to generate intermediate reasoning steps, but for web agents this reasoning must be grounded in browser observations, actions, feedback, and verification.

---

## BibTeX

```bibtex
@inproceedings{wei2022chain,
  title     = {Chain-of-Thought Prompting Elicits Reasoning in Large Language Models},
  author    = {Wei, Jason and Wang, Xuezhi and Schuurmans, Dale and Bosma, Maarten and Ichter, Brian and Xia, Fei and Chi, Ed H. and Le, Quoc V. and Zhou, Denny},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {35},
  year      = {2022},
  eprint    = {2201.11903},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  doi       = {10.48550/arXiv.2201.11903}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2201.11903
- NeurIPS proceedings: https://proceedings.neurips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P0\2023-03 - Self-Consistency Improves Chain of Thought Reasoning in Language Models.md

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


---

## P1 (10 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P1\2018-06 - Improving Language Understanding by Generative Pre-Training.md

# Paper 7 — Improving Language Understanding by Generative Pre-Training

## Metadata

- **Title:** Improving Language Understanding by Generative Pre-Training
- **Authors:** Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever
- **Year:** 2018
- **Venue:** OpenAI technical report / preprint
- **DOI:** Not listed / no official DOI found in the uploaded paper
- **arXiv ID:** Not listed / no arXiv ID in the uploaded paper
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Cross-links:** S3 — LLM Agent Architectures; S6 — Web Information Extraction
- **Category:** FND / PRETRAINING / TRANSFER
- **Paper type:** Method / pretraining + fine-tuning framework
- **Priority:** P1
- **BibTeX key:** radford2018improving

---

## Simple understanding

This paper is the original GPT-style generative pre-training paper. It shows that a Transformer decoder can first be trained with a language-modeling objective on large unlabeled text, then fine-tuned for many downstream language understanding tasks with minimal architectural changes.

The important shift is that language modeling becomes a general pretraining method. Instead of building a different architecture for every NLP task, the same pretrained Transformer can be adapted to classification, entailment, similarity, and question answering by converting structured inputs into token sequences.

For the thesis, this paper is important because it begins the GPT line: a general-purpose generative language model can learn reusable representations from raw web-scale text. This is one foundation for later instruction-following LLMs and agents.

---

## Notes

- **Core idea:**
  Introduces generative pre-training with a Transformer decoder followed by supervised fine-tuning, showing that a mostly task-agnostic model can transfer to many language understanding tasks.

- **Key finding:**
  The model improves the state of the art on 9 of 12 evaluated NLU tasks, including commonsense reasoning, question answering, textual entailment, and GLUE-style evaluation.

- **Limitation:**
- The model still depends on supervised fine-tuning for each downstream task. For web agents, this matters because generalized web automation cannot assume a labeled dataset or a fine-tuned checkpoint for every website, interface, workflow, or extraction schema. This motivates GPT-3-style in-context learning, instruction tuning, and agent methods that adapt at inference time.
- The paper focuses on static language understanding tasks, not interaction. For web agents, this matters because understanding a text input is only one part of the loop; agents must observe web state, choose actions, execute them, and recover from failures.
- The model processes text sequences but has no explicit grounding in DOM structure, visual layout, browser state, or external tools. This motivates later web-specific representation and grounding work in S5.2.

- **Connects to:**
  Connects BERT/GPT-era pretraining to later general-purpose LLM agents. It is a bridge between the Transformer architecture and the GPT-3/InstructGPT line used as agent backbones.

- **Use in thesis:**
  Use as historical foundation for the GPT paradigm: unsupervised generative pretraining creates reusable capabilities, but fine-tuning-only transfer is not enough for generalized web automation.

- **BibTeX key:**
  radford2018improving

---

## Thesis-ready paragraph

Radford et al. introduced a two-stage transfer-learning framework in which a Transformer decoder is first pretrained with a generative language modeling objective on unlabeled text and then fine-tuned for diverse supervised NLP tasks. This work is important for LLM-based agents because it established the GPT-style paradigm: a single generative model can acquire reusable linguistic knowledge from large-scale text and transfer it across tasks. However, the framework still relies on task-specific fine-tuning and static benchmark inputs. For generalized web automation and data extraction, this is insufficient because agents must adapt to unseen websites, interact with dynamic interfaces, and ground decisions in live browser states. The paper therefore provides an important foundation, while also motivating the later move toward in-context learning, instruction following, and agentic interaction.

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

- Generative pre-training: train a decoder language model on unlabeled text before task adaptation.
- Task-aware input transformations: convert structured inputs such as sentence pairs into linear token sequences.
- Minimal architectural change: reuse the same model across tasks with small task-specific output heads.
- Early GPT lineage: this paper is the direct predecessor of GPT-2, GPT-3, and instruction-following GPT models.

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
- **Depth needed:** Medium. Focus on abstract, introduction, framework, task-specific input transformations, results, and conclusion.
- **Main use:** Strengthen S2 foundation and support later S3/S5/S6/S7 links
- **Read after:** S2 P0 papers
- **Use while writing:** S2 foundation narrative and relevant cross-linked sections

---

## One-sentence summary

Introduces generative pre-training with a Transformer decoder followed by supervised fine-tuning, showing that a mostly task-agnostic model can transfer to many language understanding tasks. Its main thesis relevance is that it strengthens the LLM foundation, but still requires agent-level grounding, interaction, and verification for web automation.

---

## BibTeX

```bibtex
@article{radford2018improving,
  title  = {Improving Language Understanding by Generative Pre-Training},
  author = {Radford, Alec and Narasimhan, Karthik and Salimans, Tim and Sutskever, Ilya},
  year   = {2018},
  note   = {OpenAI technical report}
}
```

---

## Source links

- https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P1\2020-05 - Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.md

# Paper 8 — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## Metadata

- **Title:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
- **Authors:** Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela
- **Year:** 2020
- **Venue:** Advances in Neural Information Processing Systems 33 (NeurIPS 2020)
- **DOI:** 10.48550/arXiv.2005.11401
- **arXiv ID:** arXiv:2005.11401
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Cross-links:** S6 — LLM-Based Web Information Extraction; S7 — Trustworthiness; S8 — Deployment
- **Category:** FND / RAG / KNOWLEDGE
- **Paper type:** Method / retrieval-augmented generation
- **Priority:** P1
- **BibTeX key:** lewis2020retrieval

---

## Simple understanding

This paper introduced RAG, a framework that combines a pretrained generator with an external retriever. The model does not rely only on knowledge stored in its parameters. It retrieves relevant passages from a non-parametric memory, such as Wikipedia, and conditions generation on those passages.

For the thesis, this is important because web agents often need fresh, external, and verifiable information. A pure LLM may hallucinate or use outdated knowledge, while a retrieval-augmented system can consult documents, pages, search results, or databases. RAG is therefore a foundation for grounded question answering, web information extraction, and agent verification.

---

## Notes

- **Core idea:**
  Combines parametric memory in a seq2seq model with non-parametric memory from dense retrieval, enabling generation conditioned on retrieved evidence.

- **Key finding:**
  RAG improves open-domain QA and knowledge-intensive generation, setting strong results on several QA tasks and producing more specific, diverse, and factual outputs than a parametric-only seq2seq baseline.

- **Limitation:**
- RAG depends on retrieval quality. For web agents, this matters because if the retriever selects irrelevant, stale, duplicated, or noisy web content, the agent may reason from wrong evidence and extract incorrect data. This motivates retrieval evaluation, source ranking, and evidence verification in S6/S7.
- RAG retrieves static passages rather than interacting with dynamic web pages. For web agents, this matters because automation often requires clicking, scrolling, submitting forms, and observing page changes, not only retrieving documents.
- RAG provides provenance for generated answers, but provenance alone does not guarantee correct action. For web agents, retrieved evidence must be connected to DOM elements, UI actions, and final extraction verification.

- **Connects to:**
  Connects foundation LLMs to retrieval, grounding, provenance, and factuality. It is essential for web extraction and agent systems that need external evidence.

- **Use in thesis:**
  Use as the core foundation for retrieval-augmented web agents and extraction systems. It supports the argument that agents need external memory and verifiable evidence, not only parametric knowledge.

- **BibTeX key:**
  lewis2020retrieval

---

## Thesis-ready paragraph

Lewis et al. introduced retrieval-augmented generation, a framework that combines a pretrained parametric generator with a non-parametric memory accessed through dense retrieval. Instead of relying only on knowledge stored in model parameters, RAG retrieves relevant passages and conditions generation on them. This is foundational for LLM-based web agents because generalized web automation and data extraction often require current, source-grounded, and verifiable information. However, RAG alone does not solve interactive web automation: retrieval quality can fail, retrieved passages may be noisy or stale, and the model does not execute browser actions or verify outcomes through the environment. Thus, RAG provides an important grounding mechanism but must be integrated with agent loops, DOM grounding, action execution, and evidence-based verification.

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

- Parametric memory: knowledge stored in model weights.
- Non-parametric memory: external corpus/index that can be retrieved and updated.
- RAG-Sequence: conditions the whole generated sequence on retrieved passages.
- RAG-Token: can condition different generated tokens on different retrieved passages.
- Provenance: retrieved documents can be inspected as evidence for outputs.

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
- **Depth needed:** High. Focus on abstract, Figure 1, Sections 1–2, results on QA/generation, and discussion of provenance/updating knowledge.
- **Main use:** Strengthen S2 foundation and support later S3/S5/S6/S7 links
- **Read after:** S2 P0 papers
- **Use while writing:** S2 foundation narrative and relevant cross-linked sections

---

## One-sentence summary

Combines parametric memory in a seq2seq model with non-parametric memory from dense retrieval, enabling generation conditioned on retrieved evidence. Its main thesis relevance is that it strengthens the LLM foundation, but still requires agent-level grounding, interaction, and verification for web automation.

---

## BibTeX

```bibtex
@inproceedings{lewis2020retrieval,
  title     = {Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks},
  author    = {Lewis, Patrick and Perez, Ethan and Piktus, Aleksandra and Petroni, Fabio and Karpukhin, Vladimir and Goyal, Naman and Kuttler, Heinrich and Lewis, Mike and Yih, Wen-tau and Rocktaschel, Tim and Riedel, Sebastian and Kiela, Douwe},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {33},
  year      = {2020},
  eprint    = {2005.11401},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  doi       = {10.48550/arXiv.2005.11401}
}
```

---

## Source links

- https://arxiv.org/abs/2005.11401
- https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P1\2022-02 - Finetuned Language Models Are Zero-Shot Learners.md

# Paper 9 — Finetuned Language Models Are Zero-Shot Learners

## Metadata

- **Title:** Finetuned Language Models Are Zero-Shot Learners
- **Authors:** Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai, Quoc V. Le
- **Year:** 2022
- **Venue:** International Conference on Learning Representations (ICLR 2022)
- **DOI:** 10.48550/arXiv.2109.01652
- **arXiv ID:** arXiv:2109.01652
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Cross-links:** S3 — LLM Agent Architectures; S5.3 — Planning; S8 — Deployment
- **Category:** FND / INSTRUCTION-TUNING / ZERO-SHOT
- **Paper type:** Method / instruction tuning
- **Priority:** P1
- **BibTeX key:** wei2022finetuned

---

## Simple understanding

This paper introduced FLAN, an instruction-tuned language model. The main idea is to fine-tune a pretrained LM on many datasets reformulated as natural-language instructions, so that the model learns how to respond to instructions even for unseen tasks.

For the thesis, this paper is important because web agents are instruction-driven systems. A user tells the agent what to do, and the model must map that instruction to useful behavior. FLAN shows that training on many instruction-formatted tasks improves zero-shot generalization.

---

## Notes

- **Core idea:**
  Introduces instruction tuning: fine-tuning a large language model on many tasks phrased as natural-language instructions to improve zero-shot performance on unseen task types.

- **Key finding:**
  FLAN improves zero-shot performance over the base model and outperforms zero-shot GPT-3 on many evaluated datasets; ablations show that number of tasks, model scale, and natural-language instructions are key factors.

- **Limitation:**
- FLAN improves instruction following for NLP tasks but does not perform grounded environment interaction. For web agents, this matters because an agent must convert instructions into browser actions and verify outcomes, not just produce text.
- The instruction-tuning mixture is built from predefined NLP datasets. For web agents, this matters because real websites contain long, noisy, dynamic, multimodal, and task-specific contexts not represented by traditional NLP benchmarks.
- Instruction tuning depends on task coverage. For web agents, unseen websites and workflows may require behaviors not covered during instruction tuning, motivating agent-level generalization and online feedback.

- **Connects to:**
  Connects GPT-3 few-shot learning to InstructGPT/RLHF and later instruction-following agents. It shows that models can learn a general instruction interface.

- **Use in thesis:**
  Use to explain why instruction following became a core prerequisite for LLM agents and why web agents can be controlled through natural language.

- **BibTeX key:**
  wei2022finetuned

---

## Thesis-ready paragraph

Wei et al. proposed instruction tuning, a simple but influential method for improving zero-shot generalization by fine-tuning a pretrained language model on many tasks expressed through natural-language instructions. The resulting FLAN model demonstrates that exposure to diverse instruction-formatted tasks improves performance on unseen task types. For LLM-based web agents, this is foundational because user goals in web automation are naturally expressed as instructions. However, FLAN remains a language-task model rather than an interactive agent: it does not observe web pages, select DOM-grounded actions, handle dynamic browser feedback, or verify extracted information. Therefore, instruction tuning provides the instruction-following substrate for agents, but must be combined with planning, tools, memory, and environment grounding.

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

- Instruction tuning: supervised fine-tuning on task instructions and outputs.
- Task clusters: evaluation holds out entire task types to test unseen-task generalization.
- Natural-language templates: datasets are reformatted as instructions.
- Zero-shot generalization: the model responds to new tasks without examples at inference time.

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
- **Depth needed:** High. Focus on Figure 1, Figure 2, task mixture, evaluation splits, results, and ablations.
- **Main use:** Strengthen S2 foundation and support later S3/S5/S6/S7 links
- **Read after:** S2 P0 papers
- **Use while writing:** S2 foundation narrative and relevant cross-linked sections

---

## One-sentence summary

Introduces instruction tuning: fine-tuning a large language model on many tasks phrased as natural-language instructions to improve zero-shot performance on unseen task types. Its main thesis relevance is that it strengthens the LLM foundation, but still requires agent-level grounding, interaction, and verification for web automation.

---

## BibTeX

```bibtex
@inproceedings{wei2022finetuned,
  title     = {Finetuned Language Models Are Zero-Shot Learners},
  author    = {Wei, Jason and Bosma, Maarten and Zhao, Vincent Y. and Guu, Kelvin and Yu, Adams Wei and Lester, Brian and Du, Nan and Dai, Andrew M. and Le, Quoc V.},
  booktitle = {International Conference on Learning Representations},
  year      = {2022},
  eprint    = {2109.01652},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  doi       = {10.48550/arXiv.2109.01652}
}
```

---

## Source links

- https://arxiv.org/abs/2109.01652
- https://openreview.net/forum?id=gEZrGCozdqR


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P1\2022-04-Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback.md

# Paper 12 — Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback

## Metadata

- **Title:** Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback
- **Authors:** Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, Nicholas Joseph, Saurav Kadavath, Jackson Kernion, Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac Hatfield-Dodds, Danny Hernandez, Tristan Hume, Scott Johnston, Shauna Kravec, Liane Lovitt, Neel Nanda, Catherine Olsson, Dario Amodei, Tom Brown, Jack Clark, Sam McCandlish, Chris Olah, Ben Mann, Jared Kaplan
- **Year:** 2022
- **Venue:** arXiv preprint / Anthropic technical report
- **DOI:** 10.48550/arXiv.2204.05862
- **arXiv ID:** arXiv:2204.05862
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Cross-links:** S7 — Security, Robustness, and Trustworthiness; S8 — Deployment
- **Category:** FND / RLHF / ALIGNMENT
- **Paper type:** Method / alignment training / empirical study
- **Priority:** P1
- **BibTeX key:** bai2022training

---

## Simple understanding

This paper applies RLHF to train language models to behave as helpful and harmless assistants. It separates helpfulness data from harmlessness/red-teaming data, trains preference models, and then trains policies with reinforcement learning.

For the thesis, this is important because web agents are not only answer generators. They may take actions on behalf of users. Therefore helpfulness, harmlessness, refusal, over-compliance, safety, and human oversight become central requirements.

---

## Notes

- **Core idea:**
  Uses preference modeling and RLHF to train assistants that balance helpfulness and harmlessness, including red-team data and iterated online feedback.

- **Key finding:**
  RLHF improves human preference scores and can improve or preserve many NLP capabilities for larger models; the paper also identifies tension between helpfulness and harmlessness.

- **Limitation:**
- Human preference data reflects the preferences and instructions of particular annotators. For web agents, this matters because automation may affect diverse users, websites, and third parties with different privacy, risk, and safety expectations.
- Helpfulness and harmlessness can conflict. For web agents, this matters because an agent may be asked to perform risky automation, bypass restrictions, scrape sensitive data, or submit information; being helpful must be constrained by safety.
- RLHF optimizes conversational behavior, not necessarily grounded task success. For web agents, a response may look helpful while the underlying browser action is wrong, unsafe, or unverifiable.

- **Connects to:**
  Connects InstructGPT-style RLHF to assistant safety, red teaming, harmlessness, and deployment. Essential for S7.

- **Use in thesis:**
  Use to argue that web agents need alignment and safety mechanisms, not only reasoning and planning. It helps frame risks of autonomous web action.

- **BibTeX key:**
  bai2022training

---

## Thesis-ready paragraph

Bai et al. extended RLHF to train assistants that are both helpful and harmless, using separate preference datasets for helpfulness and red-team harmlessness. The paper is important for LLM-based agents because it treats alignment as an operational requirement rather than a secondary property. In web automation, this becomes even more critical: agents may click, submit, retrieve, scrape, or expose information. However, conversational RLHF does not guarantee safe grounded action. The thesis-relevant limitation is that models optimized for preferred text responses may still fail when their outputs are converted into browser actions. Therefore, web agents require safety policies, action constraints, verification, and human oversight in addition to RLHF-trained helpfulness.

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

- Preference model: model trained to predict which response humans prefer.
- Helpfulness vs harmlessness: objectives can conflict.
- Red teaming: adversarial prompting to expose harmful behavior.
- Online RLHF: iteratively update models using fresh feedback.
- Alignment tax/bonus: alignment can harm or improve benchmark performance depending on scale and setup.

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
- **Depth needed:** Medium-high. Focus on Figures 1–3, data collection, helpful vs harmless tension, RLHF robustness, limitations, and broader impacts.
- **Main use:** Strengthen S2 foundation and support later S3/S5/S6/S7 links
- **Read after:** S2 P0 papers
- **Use while writing:** S2 foundation narrative and relevant cross-linked sections

---

## One-sentence summary

Uses preference modeling and RLHF to train assistants that balance helpfulness and harmlessness, including red-team data and iterated online feedback. Its main thesis relevance is that it strengthens the LLM foundation, but still requires agent-level grounding, interaction, and verification for web automation.

---

## BibTeX

```bibtex
@article{bai2022training,
  title   = {Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback},
  author  = {Bai, Yuntao and Jones, Andy and Ndousse, Kamal and Askell, Amanda and Chen, Anna and DasSarma, Nova and Drain, Dawn and Fort, Stanislav and Ganguli, Deep and Henighan, Tom and Joseph, Nicholas and Kadavath, Saurav and Kernion, Jackson and Conerly, Tom and El-Showk, Sheer and Elhage, Nelson and Hatfield-Dodds, Zac and Hernandez, Danny and Hume, Tristan and Johnston, Scott and Kravec, Shauna and Lovitt, Liane and Nanda, Neel and Olsson, Catherine and Amodei, Dario and Brown, Tom and Clark, Jack and McCandlish, Sam and Olah, Chris and Mann, Ben and Kaplan, Jared},
  journal = {arXiv preprint arXiv:2204.05862},
  year    = {2022},
  doi     = {10.48550/arXiv.2204.05862}
}
```

---

## Source links

- https://arxiv.org/abs/2204.05862
- https://github.com/anthropics/hh-rlhf


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P1\2022-05 - Least-to-most prompting enables complex reasoning in large language models.md

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


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P1\2022-05-Large Language Models are Zero-Shot Reasoners.md

# Paper 10 — Large Language Models are Zero-Shot Reasoners

## Metadata

- **Title:** Large Language Models are Zero-Shot Reasoners
- **Authors:** Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, Yusuke Iwasawa
- **Year:** 2022
- **Venue:** Advances in Neural Information Processing Systems 35 (NeurIPS 2022)
- **DOI:** 10.48550/arXiv.2205.11916
- **arXiv ID:** arXiv:2205.11916
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Cross-links:** S5.3 — Planning and Decision-Making; S5.5 — Failure Modes
- **Category:** FND / REASONING / PROMPTING
- **Paper type:** Method / zero-shot prompting
- **Priority:** P1
- **BibTeX key:** kojima2022large

---

## Simple understanding

This paper shows that LLMs can perform step-by-step reasoning without few-shot demonstrations. Instead of giving worked examples, the prompt simply adds a trigger such as “Let’s think step by step.”

This is called Zero-shot-CoT. It is important because it reduces the need for handcrafted examples. For web agents, this means the model can sometimes reason about a new task directly from an instruction, which is useful when no task-specific demonstrations exist.

---

## Notes

- **Core idea:**
  Introduces Zero-shot-CoT, a task-agnostic prompt that elicits reasoning by adding a simple reasoning trigger such as “Let’s think step by step.”

- **Key finding:**
  Zero-shot-CoT substantially improves zero-shot performance on arithmetic, symbolic, commonsense, and logical reasoning tasks compared with standard zero-shot prompting.

- **Limitation:**
- Zero-shot-CoT still relies on prompt phrasing and does not guarantee correct reasoning. For web agents, this matters because a simple reasoning trigger may produce confident but wrong plans, wrong element choices, or hallucinated page states.
- The method produces reasoning text but does not interact with an environment. For web agents, this matters because browser automation requires action execution and feedback, not only a textual answer.
- The method uses a two-stage process for reasoning extraction and answer extraction. For web agents, repeated two-stage prompting at every browser step can increase latency and cost.

- **Connects to:**
  Extends Chain-of-Thought by removing the need for few-shot reasoning examples. It connects to agent planning because agents often need to reason in new situations without examples.

- **Use in thesis:**
  Use as a foundation for prompt-based reasoning in agents, especially when task-specific web demonstrations are unavailable.

- **BibTeX key:**
  kojima2022large

---

## Thesis-ready paragraph

Kojima et al. showed that large language models can act as zero-shot reasoners when prompted with a simple trigger such as “Let’s think step by step.” Unlike few-shot chain-of-thought prompting, Zero-shot-CoT does not require manually crafted reasoning examples for each task. This is important for generalized web automation because web agents often face novel websites and tasks where demonstrations are unavailable. However, the method remains a text-only reasoning strategy. It does not guarantee faithful reasoning, does not ground decisions in a browser environment, and does not verify that actions succeed. Thus, Zero-shot-CoT supports flexible reasoning but must be combined with observation, action, feedback, and verification mechanisms for robust web agents.

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

- Zero-shot-CoT: elicit reasoning without demonstrations.
- Reasoning trigger: short phrase that changes model behavior.
- Two-stage prompting: first generate reasoning, then extract final answer.
- Task-agnostic prompting: the same trigger works across multiple reasoning benchmarks.

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
- **Depth needed:** Medium-high. Focus on Figure 1, Figure 2, method, benchmark comparison, and limitations.
- **Main use:** Strengthen S2 foundation and support later S3/S5/S6/S7 links
- **Read after:** S2 P0 papers
- **Use while writing:** S2 foundation narrative and relevant cross-linked sections

---

## One-sentence summary

Introduces Zero-shot-CoT, a task-agnostic prompt that elicits reasoning by adding a simple reasoning trigger such as “Let’s think step by step.” Its main thesis relevance is that it strengthens the LLM foundation, but still requires agent-level grounding, interaction, and verification for web automation.

---

## BibTeX

```bibtex
@inproceedings{kojima2022large,
  title     = {Large Language Models are Zero-Shot Reasoners},
  author    = {Kojima, Takeshi and Gu, Shixiang Shane and Reid, Machel and Matsuo, Yutaka and Iwasawa, Yusuke},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {35},
  year      = {2022},
  eprint    = {2205.11916},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  doi       = {10.48550/arXiv.2205.11916}
}
```

---

## Source links

- https://arxiv.org/abs/2205.11916
- https://proceedings.neurips.cc/paper/2022/hash/8bb0d291acd4acf06ef112099c16f326-Abstract-Conference.html


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P1\2023-04-Visual Instruction Tuning.md

# Paper 14 — Visual Instruction Tuning

## Metadata

- **Title:** Visual Instruction Tuning
- **Authors:** Haotian Liu, Chunyuan Li, Qingyang Wu, Yong Jae Lee
- **Year:** 2023
- **Venue:** Advances in Neural Information Processing Systems 36 (NeurIPS 2023)
- **DOI:** 10.48550/arXiv.2304.08485
- **arXiv ID:** arXiv:2304.08485
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Cross-links:** S5.2 — Perception, Grounding, and Interface Representation; S5.3 — Planning
- **Category:** FND / MULTIMODAL / INSTRUCTION-TUNING
- **Paper type:** Method / multimodal instruction tuning
- **Priority:** P1
- **BibTeX key:** liu2023visual

---

## Simple understanding

This paper introduced LLaVA, a large language-and-vision assistant built by connecting a CLIP vision encoder to a language model and instruction-tuning it on generated multimodal instruction-following data.

For the thesis, this is important because web agents increasingly use screenshots, visual layout, icons, buttons, tables, and charts—not only HTML text. Visual instruction tuning is a foundation for agents that can understand web pages visually.

---

## Notes

- **Core idea:**
  Extends instruction tuning to the multimodal setting by generating image-language instruction data and training LLaVA as a visual-language assistant.

- **Key finding:**
  LLaVA shows strong multimodal chat behavior, reaches 85.1% relative score compared with GPT-4 on a synthetic multimodal instruction-following benchmark, and improves ScienceQA when combined with GPT-4.

- **Limitation:**
- LLaVA relies on generated instruction data from language-only GPT-4 based on captions and boxes rather than direct GPT-4 visual perception. For web agents, this matters because generated supervision may miss subtle UI details, layout relations, hidden states, and interactive affordances.
- The model understands images but does not execute actions in a browser. For web agents, visual understanding must be connected to action selection, coordinates, DOM elements, and feedback.
- The simple visual-language projection may be insufficient for precise UI grounding. For web agents, small differences between buttons, forms, icons, or table cells can determine task success.

- **Connects to:**
  Connects instruction tuning to multimodal web perception. It is important for S5.2 because modern web agents often rely on screenshots and visual grounding.

- **Use in thesis:**
  Use to motivate multimodal web agents that combine language instructions with visual page understanding.

- **BibTeX key:**
  liu2023visual

---

## Thesis-ready paragraph

Liu et al. introduced visual instruction tuning through LLaVA, an end-to-end multimodal assistant that connects a CLIP vision encoder with an instruction-following language model. The paper extends the instruction-tuning paradigm from text-only tasks to image-language interaction by generating multimodal instruction-following data with GPT-4. For web agents, this is foundational because many web interfaces require visual interpretation of layout, icons, buttons, charts, and screenshots. However, LLaVA does not itself solve web automation: it does not execute browser actions, ground responses to DOM nodes, or verify task completion through environment feedback. Thus, visual instruction tuning provides an important perception layer for web agents, but it must be integrated with planning and control mechanisms.

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

- Visual instruction tuning: instruction-following training for image-language models.
- LLaVA: Large Language and Vision Assistant.
- CLIP vision encoder + LLM: architecture for multimodal understanding.
- Generated multimodal data: GPT-4-generated questions, descriptions, and reasoning based on image metadata.

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
- **Depth needed:** High for S5.2. Focus on abstract, data generation, Figure 1 architecture, training setup, evaluation, and limitations.
- **Main use:** Strengthen S2 foundation and support later S3/S5/S6/S7 links
- **Read after:** S2 P0 papers
- **Use while writing:** S2 foundation narrative and relevant cross-linked sections

---

## One-sentence summary

Extends instruction tuning to the multimodal setting by generating image-language instruction data and training LLaVA as a visual-language assistant. Its main thesis relevance is that it strengthens the LLM foundation, but still requires agent-level grounding, interaction, and verification for web automation.

---

## BibTeX

```bibtex
@inproceedings{liu2023visual,
  title     = {Visual Instruction Tuning},
  author    = {Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {36},
  year      = {2023},
  eprint    = {2304.08485},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV},
  doi       = {10.48550/arXiv.2304.08485}
}
```

---

## Source links

- https://arxiv.org/abs/2304.08485
- https://papers.nips.cc/paper_files/paper/2023/hash/6dcf277ea32ce3288914faf369fe6de0-Abstract-Conference.html


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P1\2023-09 - Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer.md

# Paper 13 — Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer

## Metadata

- **Title:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer
- **Authors:** Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu
- **Year:** 2020
- **Venue:** Journal of Machine Learning Research, 21(140):1–67
- **DOI:** 10.48550/arXiv.1910.10683
- **arXiv ID:** arXiv:1910.10683
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Cross-links:** S6 — Web Information Extraction; S8 — Deployment
- **Category:** FND / TRANSFER / TEXT-TO-TEXT
- **Paper type:** Empirical study / unified framework
- **Priority:** P1
- **BibTeX key:** raffel2020exploring

---

## Simple understanding

This paper introduced T5, the Text-to-Text Transfer Transformer. The main idea is to convert every NLP task into the same format: text input to text output. Classification, translation, summarization, and question answering are all treated as generation tasks.

For the thesis, T5 matters because web agents also benefit from unifying tasks as text-to-text or instruction-to-output problems. Extraction, summarization, QA, and form understanding can all be represented through textual instructions and structured textual outputs.

---

## Notes

- **Core idea:**
  Introduces a unified text-to-text framework and systematically studies transfer learning choices such as objectives, architectures, datasets, scale, and multitask learning.

- **Key finding:**
  T5 plus the cleaned C4 web corpus and scaled training achieves strong or state-of-the-art results across many NLP tasks, while showing the value of a unified text-to-text formulation.

- **Limitation:**
- T5 unifies text tasks but does not model action or environment feedback. For web agents, this matters because browser automation requires observing, acting, and verifying, not only mapping text input to text output.
- The C4 corpus is cleaned web text, not live web interaction data. For web agents, this matters because real websites contain scripts, layout, DOM structure, dynamic content, and interactive affordances removed or abstracted away in text corpora.
- The text-to-text interface can hide task structure. For web agents, this matters because DOM hierarchy, visual layout, and UI affordances may be lost if everything is flattened into plain text.

- **Connects to:**
  Connects transfer learning, web-scale data, and unified task formatting. It supports S6 extraction tasks and later instruction-output agent interfaces.

- **Use in thesis:**
  Use to explain why many LLM tasks, including extraction and QA, can be represented as text-to-text problems, while also showing why web agents need additional grounding beyond text.

- **BibTeX key:**
  raffel2020exploring

---

## Thesis-ready paragraph

Raffel et al. introduced T5, a unified text-to-text framework that reformulates diverse NLP tasks as conditional text generation. This work is foundational because it simplifies transfer learning: the same model, objective, and decoding procedure can handle classification, summarization, translation, and question answering. For LLM-based web automation and data extraction, this supports the idea that many web tasks can be expressed as instruction-to-output transformations, including extracting fields, answering questions over pages, and summarizing content. However, the text-to-text abstraction does not capture interactive browser state, DOM structure, or action execution. Therefore, T5 provides a powerful task formulation but not a complete model of web agency.

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

- Text-to-text framework: every task uses text input and text output.
- C4: Colossal Clean Crawled Corpus, a cleaned Common Crawl dataset.
- Transfer learning survey: systematic comparison of objectives, datasets, scale, and architectures.
- Encoder-decoder Transformer: useful for conditional generation tasks.

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
- **Depth needed:** Medium. Focus on abstract, Figure 1, C4 dataset, text-to-text setup, transfer experiments, and conclusion.
- **Main use:** Strengthen S2 foundation and support later S3/S5/S6/S7 links
- **Read after:** S2 P0 papers
- **Use while writing:** S2 foundation narrative and relevant cross-linked sections

---

## One-sentence summary

Introduces a unified text-to-text framework and systematically studies transfer learning choices such as objectives, architectures, datasets, scale, and multitask learning. Its main thesis relevance is that it strengthens the LLM foundation, but still requires agent-level grounding, interaction, and verification for web automation.

---

## BibTeX

```bibtex
@article{raffel2020exploring,
  title   = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
  author  = {Raffel, Colin and Shazeer, Noam and Roberts, Adam and Lee, Katherine and Narang, Sharan and Matena, Michael and Zhou, Yanqi and Li, Wei and Liu, Peter J.},
  journal = {Journal of Machine Learning Research},
  volume  = {21},
  number  = {140},
  pages   = {1--67},
  year    = {2020},
  eprint  = {1910.10683},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  doi     = {10.48550/arXiv.1910.10683}
}
```

---

## Source links

- https://jmlr.org/papers/v21/20-074.html
- https://arxiv.org/abs/1910.10683


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P1\2024-03 - GPT-4 Technical Report.md

# Paper 15 — GPT-4 Technical Report

## Metadata

- **Title:** GPT-4 Technical Report
- **Authors:** OpenAI
- **Year:** 2023 / latest arXiv version 2024
- **Venue:** arXiv technical report
- **DOI:** 10.48550/arXiv.2303.08774
- **arXiv ID:** arXiv:2303.08774
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Cross-links:** S5.2 — Multimodal Perception; S5.5 — Failure Modes; S7 — Safety
- **Category:** FND / MULTIMODAL / FRONTIER-LLM
- **Paper type:** Technical report / model evaluation / system card
- **Priority:** P1
- **BibTeX key:** openai2023gpt4

---

## Simple understanding

This report presents GPT-4 as a large-scale multimodal model that accepts image and text inputs and produces text outputs. It shows strong performance on many professional, academic, NLP, coding, and reasoning benchmarks.

For the thesis, GPT-4 matters because many modern web agents use frontier multimodal LLMs as their reasoning core. GPT-4 represents the transition from text-only LLMs to models that can understand screenshots and complex multimodal inputs.

---

## Notes

- **Core idea:**
  Reports GPT-4’s capabilities, predictable scaling, multimodal input handling, benchmark performance, limitations, and safety considerations.

- **Key finding:**
  GPT-4 achieves strong benchmark and exam performance, including high scores on academic/professional exams, improved instruction following, and multimodal input capabilities.

- **Limitation:**
- GPT-4 can hallucinate and is not fully reliable. For web agents, this matters because hallucinated page states, false assumptions, or fabricated extracted values can lead to wrong automation outcomes.
- The report notes limited context and no learning from experience. For web agents, this matters because long workflows require persistent memory, state tracking, and adaptation across repeated interactions.
- The model accepts images and text but does not by itself provide a full browser-control loop. For web agents, multimodal understanding must be connected to actions, DOM/coordinate grounding, tool execution, and verification.

- **Connects to:**
  Connects foundation LLMs to frontier multimodal agents, safety, benchmark evaluation, and screenshot-based web interaction.

- **Use in thesis:**
  Use to establish the capability level of frontier LLMs and the continuing limitations that motivate explicit agent architectures and safety mechanisms.

- **BibTeX key:**
  openai2023gpt4

---

## Thesis-ready paragraph

The GPT-4 Technical Report presents GPT-4 as a large-scale multimodal Transformer-based model capable of processing image and text inputs and generating text outputs. Its strong performance on academic, professional, coding, and NLP benchmarks demonstrates the emergence of frontier models as general-purpose reasoning engines. For LLM-based web agents, GPT-4 is important because multimodal understanding enables agents to reason over screenshots, documents, diagrams, and interface states. However, the report also emphasizes limitations such as hallucination, limited context, and lack of learning from experience. These limitations are directly relevant to web automation: a powerful model can still misread a page, select an incorrect action, or produce unverified outputs. Therefore, GPT-4 supports the feasibility of LLM-based agents while motivating grounded action loops, tool use, verification, and safety constraints.

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

- Frontier multimodal LLM: image+text input with text output.
- Predictable scaling: use small-run scaling laws to estimate larger model performance.
- Post-training alignment: improves factuality and adherence to desired behavior.
- System card: analyzes risks including bias, disinformation, cybersecurity, privacy, and over-reliance.

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
- **Depth needed:** Medium-high. Focus on abstract, limitations, predictable scaling, capabilities, visual inputs, and system card risks.
- **Main use:** Strengthen S2 foundation and support later S3/S5/S6/S7 links
- **Read after:** S2 P0 papers
- **Use while writing:** S2 foundation narrative and relevant cross-linked sections

---

## One-sentence summary

Reports GPT-4’s capabilities, predictable scaling, multimodal input handling, benchmark performance, limitations, and safety considerations. Its main thesis relevance is that it strengthens the LLM foundation, but still requires agent-level grounding, interaction, and verification for web automation.

---

## BibTeX

```bibtex
@article{openai2023gpt4,
  title   = {GPT-4 Technical Report},
  author  = {{OpenAI}},
  journal = {arXiv preprint arXiv:2303.08774},
  year    = {2023},
  doi     = {10.48550/arXiv.2303.08774}
}
```

---

## Source links

- https://arxiv.org/abs/2303.08774


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\P1\2024-05 - Gemini 1.5- Unlocking multimodal understanding across millions of tokens of context.md

# Paper 16 — Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context

## Metadata

- **Title:** Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context
- **Authors:** Gemini Team, Google
- **Year:** 2024
- **Venue:** arXiv technical report / Google report
- **DOI:** 10.48550/arXiv.2403.05530
- **arXiv ID:** arXiv:2403.05530
- **Thesis section:** S2 — Foundations of LLMs for Agentic Tasks
- **Cross-links:** S5.2 — Web Representation; S5.3 — Long-Horizon Planning; S8 — Deployment
- **Category:** FND / LONG-CONTEXT / MULTIMODAL
- **Paper type:** Technical report / model evaluation
- **Priority:** P1
- **BibTeX key:** geminiteam2024gemini15

---

## Simple understanding

This report introduces Gemini 1.5 Pro and Gemini 1.5 Flash, emphasizing extremely long multimodal context windows. The models can process millions of tokens across text, code, audio, and video, with strong recall on long-context tasks.

For the thesis, this is very important because web agents often suffer from context limits: long HTML, DOM trees, multiple pages, search histories, action traces, screenshots, and documents. Long-context models reduce this bottleneck, but do not remove the need for grounding and action verification.

---

## Notes

- **Core idea:**
  Introduces Gemini 1.5 models with multimodal long-context understanding across millions of tokens, including text, code, video, and audio.

- **Key finding:**
  Gemini 1.5 achieves near-perfect recall on long-context retrieval tasks across modalities and shows strong long-document, long-video, and long-audio understanding while maintaining strong core capabilities.

- **Limitation:**
- Long context improves recall but does not guarantee correct reasoning or action selection. For web agents, this matters because simply placing a full DOM or history in context does not ensure the model chooses the right next browser action.
- Million-token context can be expensive and slow. For web agents, this matters because real-time automation needs efficient observation, pruning, memory, and selective attention rather than always processing everything.
- The report focuses on model capability, not complete autonomous web execution. For web agents, long-context understanding must be integrated with browser tools, state tracking, action feedback, and safety constraints.

- **Connects to:**
  Connects directly to long-context bottlenecks in web agents: DOM size, action history, multiple documents, screenshots, video/audio, and memory.

- **Use in thesis:**
  Use to discuss how long-context frontier models change the design space of web agents, while still requiring structured grounding and control.

- **BibTeX key:**
  geminiteam2024gemini15

---

## Thesis-ready paragraph

The Gemini 1.5 report presents a major advance in multimodal long-context modeling, with models capable of processing millions of tokens across text, code, audio, and video. For LLM-based web automation, this directly addresses one of the main limitations of earlier Transformer-based agents: web pages, DOM trees, multi-page workflows, and action histories can exceed ordinary context windows. Long-context models make it more feasible to provide complete page and task histories to an agent. However, long context alone does not solve web agency. The model must still identify relevant information, ground decisions in the interface, select safe actions, execute them, and verify outcomes. Therefore, Gemini 1.5 is important for reducing context bottlenecks, but it does not replace the need for web-specific perception, planning, memory, and feedback mechanisms.

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

- Million-token context: ability to process very long inputs.
- Multimodal long context: text, code, image/video, and audio in one context.
- Needle-in-a-haystack recall: tests retrieval of specific information hidden in long input.
- Long-context web relevance: full DOMs, long histories, documents, screenshots, and multi-page workflows.

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
- **Depth needed:** High for long-context thesis gaps. Focus on introduction, Figures 1–7, long-context evaluation, model architecture, and deployment/latency discussion.
- **Main use:** Strengthen S2 foundation and support later S3/S5/S6/S7 links
- **Read after:** S2 P0 papers
- **Use while writing:** S2 foundation narrative and relevant cross-linked sections

---

## One-sentence summary

Introduces Gemini 1.5 models with multimodal long-context understanding across millions of tokens, including text, code, video, and audio. Its main thesis relevance is that it strengthens the LLM foundation, but still requires agent-level grounding, interaction, and verification for web automation.

---

## BibTeX

```bibtex
@article{geminiteam2024gemini15,
  title   = {Gemini 1.5: Unlocking Multimodal Understanding across Millions of Tokens of Context},
  author  = {{Gemini Team}},
  journal = {arXiv preprint arXiv:2403.05530},
  year    = {2024},
  doi     = {10.48550/arXiv.2403.05530}
}
```

---

## Source links

- https://arxiv.org/abs/2403.05530


---

## Synthesis / Writing Notes (3 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\Writing\S2_mini_synthesis_from_P0.md

# S2 Mini-Synthesis — Foundations of LLMs for Agentic Tasks

## 1. Narrative

Section S2 establishes the foundation of modern LLM-based agents. The progression begins with the Transformer architecture, which replaced recurrent sequence processing with self-attention and enabled scalable language modeling. This architectural shift made it possible to train models that can process instructions, documents, web pages, and interaction histories as token sequences.

BERT then showed that Transformer-based pretraining could produce reusable language representations for many downstream understanding tasks. Although BERT is not an agent model, it demonstrated that pre-trained language models can capture contextual meaning and transfer to tasks such as question answering, classification, and information extraction. This is important for web agents because they must understand user instructions, page text, labels, buttons, forms, and extracted information.

GPT-3 marked a major transition from task-specific fine-tuning to in-context learning. Instead of training a separate model for every task, GPT-3 showed that large language models can perform many tasks from natural-language prompts and a few examples. This is a key foundation for generalized web automation, where the agent must adapt to new websites, new instructions, and new extraction formats without retraining.

InstructGPT advanced this foundation by aligning language models with user intent through human feedback. It showed that scale alone is not enough: models must also be trained to follow instructions, respect constraints, reduce hallucinations, and produce helpful outputs. For web agents, instruction following is essential because the agent must interpret user goals and act according to explicit and implicit constraints.

Chain-of-thought prompting then showed that large language models can be prompted to generate intermediate reasoning steps before producing an answer. This is important for agentic tasks because web automation often requires decomposition: the agent must break a goal into subgoals, reason about the current page, choose the next action, and revise its plan after feedback.

Self-consistency improved chain-of-thought reasoning by sampling multiple reasoning paths and selecting the most consistent final answer. This introduced an important inference-time reliability technique: instead of trusting one reasoning trace, the system can compare several candidate reasoning paths. For web agents, this idea is useful for action selection, extraction verification, and uncertainty reduction, although it increases cost and still requires grounding in the web environment.

Overall, the six P0 papers in S2 show the progression from language model architecture to agent-relevant capabilities:

```text
Transformer → BERT → GPT-3 → InstructGPT → Chain-of-Thought → Self-Consistency
```

This can be understood as:

```text
architecture → pretraining → in-context learning → instruction following → reasoning → reasoning reliability
```

Together, these works explain why modern LLMs became suitable as the reasoning and decision-making core of web agents.

---

## 2. Main conceptual contribution of S2

The central idea of S2 is that LLM-based agents did not appear suddenly. They emerged from several technical developments:

1. **Scalable sequence modeling**
   - The Transformer made it possible to train large models efficiently using self-attention.

2. **Reusable language understanding**
   - BERT showed that pre-trained Transformer models can be adapted to many language understanding tasks.

3. **Task generalization through prompting**
   - GPT-3 showed that large models can perform new tasks from prompts and examples without task-specific fine-tuning.

4. **Instruction alignment**
   - InstructGPT showed that models can be made more useful and controllable by training them with human feedback.

5. **Explicit reasoning**
   - Chain-of-thought prompting showed that LLMs can solve harder tasks by generating intermediate reasoning steps.

6. **Reasoning robustness**
   - Self-consistency showed that multiple reasoning paths can improve answer reliability.

These capabilities are foundational for LLM-based agents because an agent needs to understand instructions, reason over observations, choose actions, adapt to new situations, and produce useful outputs.

---

## 3. Gap

The main gap after S2 is that these models are still mostly **language models**, not complete agents.

They can:

```text
understand language
follow instructions
reason step by step
generate answers
adapt from prompts
```

But they do not fully solve:

```text
grounded perception
browser interaction
DOM understanding
long-horizon planning
action execution
state tracking
error recovery
verification
safe autonomous operation
structured web data extraction
```

This is the key gap for the thesis.

The foundational LLM papers provide the cognitive core of web agents, but they do not provide the full agent loop. A web agent must connect language reasoning to real web environments. It must observe pages, select actions, execute them, interpret feedback, recover from errors, and verify outputs.

So the gap is:

```text
LLMs are strong at language reasoning, but weak as grounded, reliable, interactive web agents.
```

---

## 4. Thesis connection

This section supports the thesis by showing why LLMs are useful for generalized web automation and data extraction, but also why LLMs alone are insufficient.

For the thesis topic, “LLM-based agents for generalized web automation and data extraction,” S2 provides the foundation for three claims:

### Claim 1 — LLMs provide the reasoning core

Transformer-based LLMs can process natural language instructions, web page text, HTML content, and interaction histories. GPT-3, InstructGPT, and chain-of-thought prompting show that LLMs can generalize across tasks, follow instructions, and reason through multi-step problems.

### Claim 2 — Web automation requires more than language modeling

The limitations of these papers show that language modeling alone does not solve grounded interaction. A web agent must operate in a dynamic environment, where correctness depends not only on text generation but also on successful actions, valid observations, and verified outputs.

### Claim 3 — Later web-agent work builds directly on these foundations

The agent literature in later sections extends these foundations by adding:

```text
reasoning + action
planning + memory
tools + browser control
DOM/screenshot grounding
feedback loops
reflection and correction
evaluation benchmarks
safety and trust mechanisms
```

Therefore, S2 should be written as the bridge between general LLMs and web agents.

---

## 5. Thesis-ready synthesis paragraph

The development of LLM-based agents builds on a sequence of foundational advances in language modeling. The Transformer architecture introduced scalable self-attention, enabling efficient training of large sequence models. BERT demonstrated that Transformer pretraining can produce reusable contextual representations for language understanding, while GPT-3 showed that sufficiently large language models can generalize to new tasks through prompting and in-context learning. InstructGPT then shifted the focus from raw language modeling ability to instruction following and alignment with user intent through human feedback. Chain-of-thought prompting further showed that large language models can perform multi-step reasoning when prompted to generate intermediate reasoning steps, and self-consistency improved this reasoning by aggregating multiple reasoning paths. Together, these works provide the cognitive foundation for LLM-based agents: language understanding, task generalization, instruction following, reasoning, and inference-time reliability. However, they also reveal a central limitation for generalized web automation and data extraction: LLMs alone do not provide grounded perception, browser interaction, action execution, feedback interpretation, or reliable verification. This motivates the transition from foundation LLMs to agent architectures that combine language models with tools, memory, planning, environment feedback, and web-specific grounding mechanisms.

---

## 6. Limitations connected to the thesis

The P0 papers in S2 reveal several thesis-relevant limitations:

- **Transformer limitation:**
  Self-attention is expensive for long sequences.
  For web agents, this matters because DOM trees, HTML pages, screenshots converted to text, and action histories can exceed the context budget.
  This motivates DOM pruning, context compression, memory, and efficient representation methods.

- **BERT limitation:**
  BERT is a passive understanding model, not an action-generating agent.
  For web agents, this matters because understanding page content is only one part of automation; agents must also plan, act, observe feedback, and recover from errors.

- **GPT-3 limitation:**
  GPT-3 performs prompt-based task completion but is not grounded in an environment.
  For web agents, this matters because web automation requires interaction with live pages, not only text completion.

- **InstructGPT limitation:**
  Instruction following improves helpfulness but does not guarantee safe or correct autonomous action.
  For web agents, this matters because unsafe compliance, hallucination, or false assumptions can produce wrong clicks, wrong submissions, privacy risks, or incorrect extracted data.

- **Chain-of-thought limitation:**
  Reasoning traces can be plausible but incorrect or unfaithful.
  For web agents, this matters because a plausible reasoning trace can still select the wrong DOM element or hallucinate page state.

- **Self-consistency limitation:**
  Multiple reasoning paths improve reliability but increase inference cost and do not guarantee grounding.
  For web agents, this matters because repeated reasoning across many browser steps can become slow and expensive, and majority agreement can still be wrong if all paths rely on the same false observation.

---

## 7. Final S2 mini-synthesis

S2 shows that LLM-based agents are built on six core foundations: scalable Transformer architectures, pre-trained language understanding, in-context learning, instruction alignment, chain-of-thought reasoning, and self-consistent reasoning. These foundations explain why LLMs can serve as the central reasoning module of web agents. However, they also show the boundary of pure language modeling. The models can understand, reason, and generate, but they do not by themselves perceive web interfaces, execute browser actions, verify outcomes, or recover from interaction failures. Therefore, the next step in the literature review is to move from LLM foundations to agent architectures, where LLMs are embedded in systems with planning, tools, memory, feedback, and environment grounding.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\Writing\S2_refined_synthesis_after_P1.md

# S2 Refined Synthesis — Foundations of LLMs for Agentic Tasks  
## Updated after P0 + first 10 P1 papers

## 1. What changed after adding the P1 papers

The P0 synthesis already established the core progression:

```text
Transformer → BERT → GPT-3 → InstructGPT → Chain-of-Thought → Self-Consistency
```

After reading the first 10 P1 papers, S2 becomes richer and more complete. The refined progression is now:

```text
Transformer
→ GPT-style generative pretraining / BERT / T5
→ GPT-3 in-context learning
→ FLAN + InstructGPT + Helpful/Harmless RLHF
→ Chain-of-Thought + Zero-shot-CoT + Self-Consistency + Least-to-Most
→ RAG
→ LLaVA / GPT-4 / Gemini 1.5
```

This can be summarized conceptually as:

```text
architecture
→ pretraining and transfer
→ task generalization
→ instruction following and alignment
→ reasoning and decomposition
→ retrieval and external memory
→ multimodal and long-context foundation models
```

The P1 papers do not replace the P0 narrative. They refine it by showing that LLM-based agents require more than one foundation. They require language understanding, prompting, instruction following, reasoning, retrieval, multimodal perception, long-context processing, and alignment.

---

## 2. Refined narrative

Section S2 explains how modern LLM-based agents became possible. The foundation begins with the Transformer, which introduced scalable self-attention and enabled efficient training of large sequence models. This architecture made it possible to process instructions, documents, HTML, DOM text, action histories, and other web-related inputs as token sequences.

The next step was transfer learning through large-scale pretraining. GPT-style generative pretraining showed that a Transformer decoder trained on unlabeled text could transfer to many language understanding tasks through fine-tuning. BERT showed that bidirectional Transformer pretraining could produce strong contextual representations for language understanding. T5 then unified many NLP tasks under a text-to-text framework, showing that classification, translation, summarization, question answering, and other tasks can be represented as conditional text generation. Together, these works established that one pretrained model can serve as a reusable foundation across many tasks.

GPT-3 then shifted the field from task-specific fine-tuning toward in-context learning. Instead of training a separate model for every task, GPT-3 showed that large language models can perform new tasks from prompts and examples. This is essential for generalized web automation because a web agent cannot be fine-tuned for every website, form, workflow, or extraction schema.

Instruction following became the next major step. FLAN showed that instruction tuning on many tasks expressed in natural language improves zero-shot generalization to unseen task types. InstructGPT and the Helpful/Harmless RLHF work showed that large models must also be aligned with user intent and safety preferences. For web agents, this is critical because user goals are expressed as instructions, but agent behavior must also respect constraints, avoid unsafe actions, and handle harmful or ambiguous requests.

Reasoning methods then made LLMs more agent-relevant. Chain-of-thought prompting showed that large models can solve harder tasks by generating intermediate reasoning steps. Zero-shot-CoT showed that even a simple prompt such as “Let’s think step by step” can elicit reasoning without few-shot examples. Self-consistency improved reasoning reliability by sampling multiple reasoning paths and selecting the most consistent answer. Least-to-most prompting added explicit decomposition: complex tasks can be broken into simpler subproblems and solved sequentially. This is directly relevant to web agents because web automation tasks naturally require decomposition into subgoals and actions.

RAG added another essential foundation: external memory and retrieval. Pure LLMs rely on parametric knowledge stored in model weights, which can be outdated, incomplete, or hallucinated. Retrieval-augmented generation combines a generator with an external retriever, allowing outputs to be grounded in retrieved evidence. For web data extraction and web automation, this is important because agents often need current, source-grounded, and verifiable information from pages, documents, search results, or databases.

Finally, multimodal and long-context models expanded what LLMs can perceive and process. LLaVA introduced visual instruction tuning, showing how instruction-following can be extended to image-language models. GPT-4 demonstrated strong frontier multimodal capabilities and professional-level benchmark performance, while still showing limitations such as hallucination and lack of learning from experience. Gemini 1.5 pushed the long-context frontier, showing that models can process millions of tokens across text, code, audio, and video. This is important for web agents because real web tasks often involve screenshots, long pages, large DOM trees, multiple documents, action histories, and multimodal content.

Therefore, S2 should not be written only as a history of LLMs. It should be written as the construction of the agentic capability stack.

---

## 3. Refined capability stack for LLM-based web agents

The papers in S2 provide the following capabilities:

| Capability | Main papers | Why it matters for web agents |
|---|---|---|
| Scalable sequence modeling | Transformer | Enables LLMs to process instructions, pages, and histories as sequences |
| Pretraining and transfer | GPT-1, BERT, T5 | Enables reusable language representations and task adaptation |
| In-context learning | GPT-3 | Enables adaptation to new web tasks without fine-tuning |
| Instruction following | FLAN, InstructGPT | Enables natural-language control of agents |
| Alignment and safety | InstructGPT, Helpful/Harmless RLHF | Helps constrain agent behavior and reduce harmful compliance |
| Step-by-step reasoning | Chain-of-Thought, Zero-shot-CoT | Supports task decomposition and intermediate reasoning |
| Reasoning robustness | Self-Consistency | Reduces reliance on one reasoning path |
| Hierarchical decomposition | Least-to-Most | Supports subgoal-based web task planning |
| Retrieval and external memory | RAG | Grounds answers in external evidence and supports factuality |
| Multimodal perception | LLaVA, GPT-4 | Enables screenshot, visual layout, and document understanding |
| Long-context processing | Gemini 1.5 | Helps with long DOMs, long documents, action histories, and multi-page tasks |

---

## 4. Refined gap

After P0 papers, the main gap was:

```text
LLMs are strong at language reasoning, but weak as grounded, reliable, interactive web agents.
```

After adding the P1 papers, this gap becomes more precise:

```text
Modern LLMs provide many agent-relevant capabilities, but these capabilities remain fragmented and insufficient for reliable generalized web automation unless they are integrated into a grounded agent loop.
```

The P1 papers show that LLMs can now:

```text
transfer across tasks
follow instructions
reason step by step
decompose problems
retrieve external evidence
process images and text
handle long contexts
align better with user preferences
```

But they still do not fully solve:

```text
DOM-grounded perception
reliable UI element selection
browser action execution
state tracking across pages
long-horizon planning under uncertainty
error recovery after failed actions
verification of extracted data
safe autonomous operation
deployment cost and latency
robustness across unseen websites
```

So the refined gap is not simply “LLMs cannot act.”  
The refined gap is:

```text
LLMs provide the cognitive components of agency, but generalized web automation requires system-level integration of perception, planning, action, memory, retrieval, safety, and verification.
```

---

## 5. Refined thesis connection

For the thesis topic, “LLM-based agents for generalized web automation and data extraction,” S2 supports four major claims.

### Claim 1 — LLMs provide the cognitive core of agents

Transformer-based LLMs provide the language understanding and reasoning foundation for web agents. GPT-style pretraining, BERT, T5, GPT-3, FLAN, and InstructGPT show that LLMs can understand language, adapt to tasks, follow instructions, and produce useful outputs.

### Claim 2 — Agentic behavior requires reasoning and decomposition

Chain-of-thought, Zero-shot-CoT, Self-Consistency, and Least-to-Most prompting show that LLMs can perform multi-step reasoning and problem decomposition. These capabilities are necessary for web automation because a user goal must be transformed into subgoals, actions, observations, and corrections.

### Claim 3 — Web agents need grounding beyond parametric knowledge

RAG shows that LLMs need external knowledge sources to improve factuality, updateability, and provenance. LLaVA, GPT-4, and Gemini 1.5 show that agents increasingly need multimodal perception and long-context processing. This is important because web environments contain text, visual layout, DOM structures, screenshots, documents, tables, and long interaction histories.

### Claim 4 — LLM capabilities alone are not enough

Even with instruction following, reasoning, retrieval, multimodality, and long context, LLMs do not automatically become reliable web agents. They must be embedded in architectures that include tools, browser control, memory, grounding, safety constraints, feedback loops, and evaluation mechanisms.

---

## 6. Refined thesis-ready synthesis paragraph

The foundations of LLM-based agents emerge from a sequence of advances in language modeling, transfer learning, prompting, alignment, retrieval, multimodality, and long-context modeling. The Transformer introduced scalable self-attention, enabling large models to process sequences efficiently. GPT-style generative pretraining, BERT, and T5 then demonstrated that pretrained Transformer models can transfer across a wide range of language understanding and generation tasks, with T5 further unifying NLP tasks under a text-to-text formulation. GPT-3 shifted this paradigm toward in-context learning, showing that sufficiently large models can adapt to new tasks from prompts and examples without task-specific fine-tuning. FLAN, InstructGPT, and helpful/harmless RLHF further transformed LLMs into instruction-following and preference-aligned systems, making them more suitable as user-facing assistants. Reasoning-oriented methods such as chain-of-thought prompting, Zero-shot-CoT, self-consistency, and least-to-most prompting showed that LLMs can perform step-by-step reasoning, sample multiple reasoning paths, and decompose complex problems into subproblems. Retrieval-augmented generation added external memory and provenance, while LLaVA, GPT-4, and Gemini 1.5 extended the foundation toward multimodal perception and long-context understanding. Together, these works explain why LLMs can serve as the cognitive core of web agents. However, they also reveal the central limitation motivating this thesis: LLMs alone do not provide grounded browser perception, reliable action execution, state tracking, error recovery, safety control, or verification of extracted data. Generalized web automation therefore requires agent architectures that integrate LLM reasoning with tools, memory, retrieval, DOM and visual grounding, feedback loops, and robust evaluation.

---

## 7. Refined limitations connected to the thesis

### 7.1 Pretraining and transfer limitation

GPT-1, BERT, and T5 show that pretrained models can transfer across NLP tasks, but they mostly operate on static textual inputs.

For web agents, this matters because web automation is not only an NLP task. A web agent must interact with dynamic pages, execute actions, observe results, and update its state. This motivates the move from static transfer learning to interactive agent architectures.

### 7.2 In-context learning limitation

GPT-3 shows that models can adapt to tasks through prompts, but prompt-based task completion is still not grounded interaction.

For web agents, this matters because a prompt can specify a task, but the model still needs browser access, DOM grounding, memory, and feedback to complete the task reliably.

### 7.3 Instruction-following limitation

FLAN, InstructGPT, and RLHF models improve instruction following, but instruction following alone does not guarantee correct autonomous action.

For web agents, this matters because a model can appear helpful while still choosing the wrong button, submitting wrong data, leaking sensitive information, or hallucinating an extracted value.

### 7.4 Reasoning limitation

Chain-of-thought, Zero-shot-CoT, Self-Consistency, and Least-to-Most improve reasoning, but reasoning traces are not guaranteed to be faithful or grounded.

For web agents, this matters because plausible reasoning can still be based on a wrong page interpretation, a stale observation, or a nonexistent DOM element.

### 7.5 Retrieval limitation

RAG grounds generation in retrieved evidence, but it depends on retrieval quality and does not perform browser actions.

For web agents, this matters because retrieved documents may be irrelevant, stale, duplicated, or incomplete. The agent still needs to verify evidence against the live page and connect evidence to actions or extracted fields.

### 7.6 Multimodal limitation

LLaVA and GPT-4 show that models can reason over images and text, but visual understanding is not the same as UI grounding.

For web agents, this matters because a screenshot-level understanding must be connected to precise elements, coordinates, DOM nodes, forms, and interaction affordances.

### 7.7 Long-context limitation

Gemini 1.5 shows that long-context models can process millions of tokens, but more context does not automatically mean better agency.

For web agents, this matters because full DOMs, action histories, and documents may fit in context, but the model still needs relevance selection, planning, action control, and verification. Long context also introduces cost and latency issues.

### 7.8 Alignment and safety limitation

Helpful/harmless RLHF improves assistant behavior, but it does not guarantee safe autonomous web execution.

For web agents, this matters because agents can take actions that affect users, websites, accounts, or third parties. Safety requires action constraints, permission boundaries, risk detection, and human oversight.

---

## 8. Refined transition to S3

S2 ends by showing that modern LLMs provide the building blocks of agency:

```text
understanding
instruction following
reasoning
decomposition
retrieval
multimodal perception
long-context processing
alignment
```

But these are still building blocks, not a complete agent.

Therefore, S3 should begin with the question:

```text
How are these LLM capabilities organized into agent architectures?
```

S3 should then explain how later systems wrap LLMs with:

```text
planning
memory
tools
reflection
action execution
environment feedback
multi-agent coordination
evaluation loops
```

This transition is important because it moves the literature review from:

```text
LLMs as models
```

to:

```text
LLMs as components inside agents
```

---

## 9. Final refined S2 synthesis

S2 demonstrates that LLM-based agents are built on a layered foundation. The Transformer made scalable sequence modeling possible. GPT-style pretraining, BERT, and T5 established transfer learning and reusable language representations. GPT-3 introduced in-context task generalization. FLAN, InstructGPT, and helpful/harmless RLHF improved instruction following and alignment. Chain-of-thought, Zero-shot-CoT, Self-Consistency, and Least-to-Most prompting strengthened reasoning, reliability, and decomposition. RAG introduced retrieval and external memory. LLaVA, GPT-4, and Gemini 1.5 extended the foundation toward multimodal and long-context understanding.

These advances explain why LLMs are suitable as the cognitive core of web agents. They can understand instructions, reason over observations, retrieve information, process long contexts, and interpret multimodal inputs. However, S2 also shows that LLMs alone are not sufficient for generalized web automation and data extraction. They do not inherently provide grounded perception, browser action execution, reliable state tracking, error recovery, safety control, or verification. The next stage of the literature review must therefore examine agent architectures that integrate LLMs with tools, memory, planning, environment feedback, DOM and visual grounding, and robust evaluation.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\Writing\S2_refined_synthesis_after_P1_with_cross_links.md

# S2 Refined Synthesis — Foundations of LLMs for Agentic Tasks  
## Updated after P0 + first 10 P1 papers

## 1. What changed after adding the P1 papers

The P0 synthesis already established the core progression:

```text
Transformer → BERT → GPT-3 → InstructGPT → Chain-of-Thought → Self-Consistency
```

After reading the first 10 P1 papers, S2 becomes richer and more complete. The refined progression is now:

```text
Transformer
→ GPT-style generative pretraining / BERT / T5
→ GPT-3 in-context learning
→ FLAN + InstructGPT + Helpful/Harmless RLHF
→ Chain-of-Thought + Zero-shot-CoT + Self-Consistency + Least-to-Most
→ RAG
→ LLaVA / GPT-4 / Gemini 1.5
```

This can be summarized conceptually as:

```text
architecture
→ pretraining and transfer
→ task generalization
→ instruction following and alignment
→ reasoning and decomposition
→ retrieval and external memory
→ multimodal and long-context foundation models
```

The P1 papers do not replace the P0 narrative. They refine it by showing that LLM-based agents require more than one foundation. They require language understanding, prompting, instruction following, reasoning, retrieval, multimodal perception, long-context processing, and alignment.

---

## 2. Refined narrative

Section S2 explains how modern LLM-based agents became possible. The foundation begins with the Transformer, which introduced scalable self-attention and enabled efficient training of large sequence models. This architecture made it possible to process instructions, documents, HTML, DOM text, action histories, and other web-related inputs as token sequences.

The next step was transfer learning through large-scale pretraining. GPT-style generative pretraining showed that a Transformer decoder trained on unlabeled text could transfer to many language understanding tasks through fine-tuning. BERT showed that bidirectional Transformer pretraining could produce strong contextual representations for language understanding. T5 then unified many NLP tasks under a text-to-text framework, showing that classification, translation, summarization, question answering, and other tasks can be represented as conditional text generation. Together, these works established that one pretrained model can serve as a reusable foundation across many tasks.

GPT-3 then shifted the field from task-specific fine-tuning toward in-context learning. Instead of training a separate model for every task, GPT-3 showed that large language models can perform new tasks from prompts and examples. This is essential for generalized web automation because a web agent cannot be fine-tuned for every website, form, workflow, or extraction schema.

Instruction following became the next major step. FLAN showed that instruction tuning on many tasks expressed in natural language improves zero-shot generalization to unseen task types. InstructGPT and the Helpful/Harmless RLHF work showed that large models must also be aligned with user intent and safety preferences. For web agents, this is critical because user goals are expressed as instructions, but agent behavior must also respect constraints, avoid unsafe actions, and handle harmful or ambiguous requests.

Reasoning methods then made LLMs more agent-relevant. Chain-of-thought prompting showed that large models can solve harder tasks by generating intermediate reasoning steps. Zero-shot-CoT showed that even a simple prompt such as “Let’s think step by step” can elicit reasoning without few-shot examples. Self-consistency improved reasoning reliability by sampling multiple reasoning paths and selecting the most consistent answer. Least-to-most prompting added explicit decomposition: complex tasks can be broken into simpler subproblems and solved sequentially. This is directly relevant to web agents because web automation tasks naturally require decomposition into subgoals and actions.

RAG added another essential foundation: external memory and retrieval. Pure LLMs rely on parametric knowledge stored in model weights, which can be outdated, incomplete, or hallucinated. Retrieval-augmented generation combines a generator with an external retriever, allowing outputs to be grounded in retrieved evidence. For web data extraction and web automation, this is important because agents often need current, source-grounded, and verifiable information from pages, documents, search results, or databases.

Finally, multimodal and long-context models expanded what LLMs can perceive and process. LLaVA introduced visual instruction tuning, showing how instruction-following can be extended to image-language models. GPT-4 demonstrated strong frontier multimodal capabilities and professional-level benchmark performance, while still showing limitations such as hallucination and lack of learning from experience. Gemini 1.5 pushed the long-context frontier, showing that models can process millions of tokens across text, code, audio, and video. This is important for web agents because real web tasks often involve screenshots, long pages, large DOM trees, multiple documents, action histories, and multimodal content.

Therefore, S2 should not be written only as a history of LLMs. It should be written as the construction of the agentic capability stack.

---

## 3. Refined capability stack for LLM-based web agents

The papers in S2 provide the following capabilities:

| Capability | Main papers | Why it matters for web agents |
|---|---|---|
| Scalable sequence modeling | Transformer | Enables LLMs to process instructions, pages, and histories as sequences |
| Pretraining and transfer | GPT-1, BERT, T5 | Enables reusable language representations and task adaptation |
| In-context learning | GPT-3 | Enables adaptation to new web tasks without fine-tuning |
| Instruction following | FLAN, InstructGPT | Enables natural-language control of agents |
| Alignment and safety | InstructGPT, Helpful/Harmless RLHF | Helps constrain agent behavior and reduce harmful compliance |
| Step-by-step reasoning | Chain-of-Thought, Zero-shot-CoT | Supports task decomposition and intermediate reasoning |
| Reasoning robustness | Self-Consistency | Reduces reliance on one reasoning path |
| Hierarchical decomposition | Least-to-Most | Supports subgoal-based web task planning |
| Retrieval and external memory | RAG | Grounds answers in external evidence and supports factuality |
| Multimodal perception | LLaVA, GPT-4 | Enables screenshot, visual layout, and document understanding |
| Long-context processing | Gemini 1.5 | Helps with long DOMs, long documents, action histories, and multi-page tasks |

---

## 4. Refined gap

After P0 papers, the main gap was:

```text
LLMs are strong at language reasoning, but weak as grounded, reliable, interactive web agents.
```

After adding the P1 papers, this gap becomes more precise:

```text
Modern LLMs provide many agent-relevant capabilities, but these capabilities remain fragmented and insufficient for reliable generalized web automation unless they are integrated into a grounded agent loop.
```

The P1 papers show that LLMs can now:

```text
transfer across tasks
follow instructions
reason step by step
decompose problems
retrieve external evidence
process images and text
handle long contexts
align better with user preferences
```

But they still do not fully solve:

```text
DOM-grounded perception
reliable UI element selection
browser action execution
state tracking across pages
long-horizon planning under uncertainty
error recovery after failed actions
verification of extracted data
safe autonomous operation
deployment cost and latency
robustness across unseen websites
```

So the refined gap is not simply “LLMs cannot act.”  
The refined gap is:

```text
LLMs provide the cognitive components of agency, but generalized web automation requires system-level integration of perception, planning, action, memory, retrieval, safety, and verification.
```

---

## 5. Refined thesis connection

For the thesis topic, “LLM-based agents for generalized web automation and data extraction,” S2 supports four major claims.

### Claim 1 — LLMs provide the cognitive core of agents

Transformer-based LLMs provide the language understanding and reasoning foundation for web agents. GPT-style pretraining, BERT, T5, GPT-3, FLAN, and InstructGPT show that LLMs can understand language, adapt to tasks, follow instructions, and produce useful outputs.

### Claim 2 — Agentic behavior requires reasoning and decomposition

Chain-of-thought, Zero-shot-CoT, Self-Consistency, and Least-to-Most prompting show that LLMs can perform multi-step reasoning and problem decomposition. These capabilities are necessary for web automation because a user goal must be transformed into subgoals, actions, observations, and corrections.

### Claim 3 — Web agents need grounding beyond parametric knowledge

RAG shows that LLMs need external knowledge sources to improve factuality, updateability, and provenance. LLaVA, GPT-4, and Gemini 1.5 show that agents increasingly need multimodal perception and long-context processing. This is important because web environments contain text, visual layout, DOM structures, screenshots, documents, tables, and long interaction histories.

### Claim 4 — LLM capabilities alone are not enough

Even with instruction following, reasoning, retrieval, multimodality, and long context, LLMs do not automatically become reliable web agents. They must be embedded in architectures that include tools, browser control, memory, grounding, safety constraints, feedback loops, and evaluation mechanisms.

---

## 6. Refined thesis-ready synthesis paragraph

The foundations of LLM-based agents emerge from a sequence of advances in language modeling, transfer learning, prompting, alignment, retrieval, multimodality, and long-context modeling. The Transformer introduced scalable self-attention, enabling large models to process sequences efficiently. GPT-style generative pretraining, BERT, and T5 then demonstrated that pretrained Transformer models can transfer across a wide range of language understanding and generation tasks, with T5 further unifying NLP tasks under a text-to-text formulation. GPT-3 shifted this paradigm toward in-context learning, showing that sufficiently large models can adapt to new tasks from prompts and examples without task-specific fine-tuning. FLAN, InstructGPT, and helpful/harmless RLHF further transformed LLMs into instruction-following and preference-aligned systems, making them more suitable as user-facing assistants. Reasoning-oriented methods such as chain-of-thought prompting, Zero-shot-CoT, self-consistency, and least-to-most prompting showed that LLMs can perform step-by-step reasoning, sample multiple reasoning paths, and decompose complex problems into subproblems. Retrieval-augmented generation added external memory and provenance, while LLaVA, GPT-4, and Gemini 1.5 extended the foundation toward multimodal perception and long-context understanding. Together, these works explain why LLMs can serve as the cognitive core of web agents. However, they also reveal the central limitation motivating this thesis: LLMs alone do not provide grounded browser perception, reliable action execution, state tracking, error recovery, safety control, or verification of extracted data. Generalized web automation therefore requires agent architectures that integrate LLM reasoning with tools, memory, retrieval, DOM and visual grounding, feedback loops, and robust evaluation.

---

## 7. Refined limitations connected to the thesis

### 7.1 Pretraining and transfer limitation

GPT-1, BERT, and T5 show that pretrained models can transfer across NLP tasks, but they mostly operate on static textual inputs.

For web agents, this matters because web automation is not only an NLP task. A web agent must interact with dynamic pages, execute actions, observe results, and update its state. This motivates the move from static transfer learning to interactive agent architectures.

### 7.2 In-context learning limitation

GPT-3 shows that models can adapt to tasks through prompts, but prompt-based task completion is still not grounded interaction.

For web agents, this matters because a prompt can specify a task, but the model still needs browser access, DOM grounding, memory, and feedback to complete the task reliably.

### 7.3 Instruction-following limitation

FLAN, InstructGPT, and RLHF models improve instruction following, but instruction following alone does not guarantee correct autonomous action.

For web agents, this matters because a model can appear helpful while still choosing the wrong button, submitting wrong data, leaking sensitive information, or hallucinating an extracted value.

### 7.4 Reasoning limitation

Chain-of-thought, Zero-shot-CoT, Self-Consistency, and Least-to-Most improve reasoning, but reasoning traces are not guaranteed to be faithful or grounded.

For web agents, this matters because plausible reasoning can still be based on a wrong page interpretation, a stale observation, or a nonexistent DOM element.

### 7.5 Retrieval limitation

RAG grounds generation in retrieved evidence, but it depends on retrieval quality and does not perform browser actions.

For web agents, this matters because retrieved documents may be irrelevant, stale, duplicated, or incomplete. The agent still needs to verify evidence against the live page and connect evidence to actions or extracted fields.

### 7.6 Multimodal limitation

LLaVA and GPT-4 show that models can reason over images and text, but visual understanding is not the same as UI grounding.

For web agents, this matters because a screenshot-level understanding must be connected to precise elements, coordinates, DOM nodes, forms, and interaction affordances.

### 7.7 Long-context limitation

Gemini 1.5 shows that long-context models can process millions of tokens, but more context does not automatically mean better agency.

For web agents, this matters because full DOMs, action histories, and documents may fit in context, but the model still needs relevance selection, planning, action control, and verification. Long context also introduces cost and latency issues.

### 7.8 Alignment and safety limitation

Helpful/harmless RLHF improves assistant behavior, but it does not guarantee safe autonomous web execution.

For web agents, this matters because agents can take actions that affect users, websites, accounts, or third parties. Safety requires action constraints, permission boundaries, risk detection, and human oversight.

---

## 8. Refined transition to S3

S2 ends by showing that modern LLMs provide the building blocks of agency:

```text
understanding
instruction following
reasoning
decomposition
retrieval
multimodal perception
long-context processing
alignment
```

But these are still building blocks, not a complete agent.

Therefore, S3 should begin with the question:

```text
How are these LLM capabilities organized into agent architectures?
```

S3 should then explain how later systems wrap LLMs with:

```text
planning
memory
tools
reflection
action execution
environment feedback
multi-agent coordination
evaluation loops
```

This transition is important because it moves the literature review from:

```text
LLMs as models
```

to:

```text
LLMs as components inside agents
```

---

## 9. Final refined S2 synthesis

S2 demonstrates that LLM-based agents are built on a layered foundation. The Transformer made scalable sequence modeling possible. GPT-style pretraining, BERT, and T5 established transfer learning and reusable language representations. GPT-3 introduced in-context task generalization. FLAN, InstructGPT, and helpful/harmless RLHF improved instruction following and alignment. Chain-of-thought, Zero-shot-CoT, Self-Consistency, and Least-to-Most prompting strengthened reasoning, reliability, and decomposition. RAG introduced retrieval and external memory. LLaVA, GPT-4, and Gemini 1.5 extended the foundation toward multimodal and long-context understanding.

These advances explain why LLMs are suitable as the cognitive core of web agents. They can understand instructions, reason over observations, retrieve information, process long contexts, and interpret multimodal inputs. However, S2 also shows that LLMs alone are not sufficient for generalized web automation and data extraction. They do not inherently provide grounded perception, browser action execution, reliable state tracking, error recovery, safety control, or verification. The next stage of the literature review must therefore examine agent architectures that integrate LLMs with tools, memory, planning, environment feedback, DOM and visual grounding, and robust evaluation.

---

## Cross-links to later sections

| Paper | Feeds |
|-------|-------|
| RAG | S6 (extraction), S7 (verification) |
| LLaVA, GPT-4 | S5.2 (multimodal grounding) |
| Gemini 1.5 | S5.2 (long DOM), S5.3 (long-horizon) |
| Least-to-most | S5.3 (task decomposition) |
| Bai et al. RLHF | S7 (safety, alignment) |
| Zero-shot-CoT | S5.3 (planning without demos) |


---

## Synthesis / Writing Notes (3 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\writing\S2_mini_synthesis_from_P0.md

# S2 Mini-Synthesis — Foundations of LLMs for Agentic Tasks

## 1. Narrative

Section S2 establishes the foundation of modern LLM-based agents. The progression begins with the Transformer architecture, which replaced recurrent sequence processing with self-attention and enabled scalable language modeling. This architectural shift made it possible to train models that can process instructions, documents, web pages, and interaction histories as token sequences.

BERT then showed that Transformer-based pretraining could produce reusable language representations for many downstream understanding tasks. Although BERT is not an agent model, it demonstrated that pre-trained language models can capture contextual meaning and transfer to tasks such as question answering, classification, and information extraction. This is important for web agents because they must understand user instructions, page text, labels, buttons, forms, and extracted information.

GPT-3 marked a major transition from task-specific fine-tuning to in-context learning. Instead of training a separate model for every task, GPT-3 showed that large language models can perform many tasks from natural-language prompts and a few examples. This is a key foundation for generalized web automation, where the agent must adapt to new websites, new instructions, and new extraction formats without retraining.

InstructGPT advanced this foundation by aligning language models with user intent through human feedback. It showed that scale alone is not enough: models must also be trained to follow instructions, respect constraints, reduce hallucinations, and produce helpful outputs. For web agents, instruction following is essential because the agent must interpret user goals and act according to explicit and implicit constraints.

Chain-of-thought prompting then showed that large language models can be prompted to generate intermediate reasoning steps before producing an answer. This is important for agentic tasks because web automation often requires decomposition: the agent must break a goal into subgoals, reason about the current page, choose the next action, and revise its plan after feedback.

Self-consistency improved chain-of-thought reasoning by sampling multiple reasoning paths and selecting the most consistent final answer. This introduced an important inference-time reliability technique: instead of trusting one reasoning trace, the system can compare several candidate reasoning paths. For web agents, this idea is useful for action selection, extraction verification, and uncertainty reduction, although it increases cost and still requires grounding in the web environment.

Overall, the six P0 papers in S2 show the progression from language model architecture to agent-relevant capabilities:

```text
Transformer → BERT → GPT-3 → InstructGPT → Chain-of-Thought → Self-Consistency
```

This can be understood as:

```text
architecture → pretraining → in-context learning → instruction following → reasoning → reasoning reliability
```

Together, these works explain why modern LLMs became suitable as the reasoning and decision-making core of web agents.

---

## 2. Main conceptual contribution of S2

The central idea of S2 is that LLM-based agents did not appear suddenly. They emerged from several technical developments:

1. **Scalable sequence modeling**
   - The Transformer made it possible to train large models efficiently using self-attention.

2. **Reusable language understanding**
   - BERT showed that pre-trained Transformer models can be adapted to many language understanding tasks.

3. **Task generalization through prompting**
   - GPT-3 showed that large models can perform new tasks from prompts and examples without task-specific fine-tuning.

4. **Instruction alignment**
   - InstructGPT showed that models can be made more useful and controllable by training them with human feedback.

5. **Explicit reasoning**
   - Chain-of-thought prompting showed that LLMs can solve harder tasks by generating intermediate reasoning steps.

6. **Reasoning robustness**
   - Self-consistency showed that multiple reasoning paths can improve answer reliability.

These capabilities are foundational for LLM-based agents because an agent needs to understand instructions, reason over observations, choose actions, adapt to new situations, and produce useful outputs.

---

## 3. Gap

The main gap after S2 is that these models are still mostly **language models**, not complete agents.

They can:

```text
understand language
follow instructions
reason step by step
generate answers
adapt from prompts
```

But they do not fully solve:

```text
grounded perception
browser interaction
DOM understanding
long-horizon planning
action execution
state tracking
error recovery
verification
safe autonomous operation
structured web data extraction
```

This is the key gap for the thesis.

The foundational LLM papers provide the cognitive core of web agents, but they do not provide the full agent loop. A web agent must connect language reasoning to real web environments. It must observe pages, select actions, execute them, interpret feedback, recover from errors, and verify outputs.

So the gap is:

```text
LLMs are strong at language reasoning, but weak as grounded, reliable, interactive web agents.
```

---

## 4. Thesis connection

This section supports the thesis by showing why LLMs are useful for generalized web automation and data extraction, but also why LLMs alone are insufficient.

For the thesis topic, “LLM-based agents for generalized web automation and data extraction,” S2 provides the foundation for three claims:

### Claim 1 — LLMs provide the reasoning core

Transformer-based LLMs can process natural language instructions, web page text, HTML content, and interaction histories. GPT-3, InstructGPT, and chain-of-thought prompting show that LLMs can generalize across tasks, follow instructions, and reason through multi-step problems.

### Claim 2 — Web automation requires more than language modeling

The limitations of these papers show that language modeling alone does not solve grounded interaction. A web agent must operate in a dynamic environment, where correctness depends not only on text generation but also on successful actions, valid observations, and verified outputs.

### Claim 3 — Later web-agent work builds directly on these foundations

The agent literature in later sections extends these foundations by adding:

```text
reasoning + action
planning + memory
tools + browser control
DOM/screenshot grounding
feedback loops
reflection and correction
evaluation benchmarks
safety and trust mechanisms
```

Therefore, S2 should be written as the bridge between general LLMs and web agents.

---

## 5. Thesis-ready synthesis paragraph

The development of LLM-based agents builds on a sequence of foundational advances in language modeling. The Transformer architecture introduced scalable self-attention, enabling efficient training of large sequence models. BERT demonstrated that Transformer pretraining can produce reusable contextual representations for language understanding, while GPT-3 showed that sufficiently large language models can generalize to new tasks through prompting and in-context learning. InstructGPT then shifted the focus from raw language modeling ability to instruction following and alignment with user intent through human feedback. Chain-of-thought prompting further showed that large language models can perform multi-step reasoning when prompted to generate intermediate reasoning steps, and self-consistency improved this reasoning by aggregating multiple reasoning paths. Together, these works provide the cognitive foundation for LLM-based agents: language understanding, task generalization, instruction following, reasoning, and inference-time reliability. However, they also reveal a central limitation for generalized web automation and data extraction: LLMs alone do not provide grounded perception, browser interaction, action execution, feedback interpretation, or reliable verification. This motivates the transition from foundation LLMs to agent architectures that combine language models with tools, memory, planning, environment feedback, and web-specific grounding mechanisms.

---

## 6. Limitations connected to the thesis

The P0 papers in S2 reveal several thesis-relevant limitations:

- **Transformer limitation:**
  Self-attention is expensive for long sequences.
  For web agents, this matters because DOM trees, HTML pages, screenshots converted to text, and action histories can exceed the context budget.
  This motivates DOM pruning, context compression, memory, and efficient representation methods.

- **BERT limitation:**
  BERT is a passive understanding model, not an action-generating agent.
  For web agents, this matters because understanding page content is only one part of automation; agents must also plan, act, observe feedback, and recover from errors.

- **GPT-3 limitation:**
  GPT-3 performs prompt-based task completion but is not grounded in an environment.
  For web agents, this matters because web automation requires interaction with live pages, not only text completion.

- **InstructGPT limitation:**
  Instruction following improves helpfulness but does not guarantee safe or correct autonomous action.
  For web agents, this matters because unsafe compliance, hallucination, or false assumptions can produce wrong clicks, wrong submissions, privacy risks, or incorrect extracted data.

- **Chain-of-thought limitation:**
  Reasoning traces can be plausible but incorrect or unfaithful.
  For web agents, this matters because a plausible reasoning trace can still select the wrong DOM element or hallucinate page state.

- **Self-consistency limitation:**
  Multiple reasoning paths improve reliability but increase inference cost and do not guarantee grounding.
  For web agents, this matters because repeated reasoning across many browser steps can become slow and expensive, and majority agreement can still be wrong if all paths rely on the same false observation.

---

## 7. Final S2 mini-synthesis

S2 shows that LLM-based agents are built on six core foundations: scalable Transformer architectures, pre-trained language understanding, in-context learning, instruction alignment, chain-of-thought reasoning, and self-consistent reasoning. These foundations explain why LLMs can serve as the central reasoning module of web agents. However, they also show the boundary of pure language modeling. The models can understand, reason, and generate, but they do not by themselves perceive web interfaces, execute browser actions, verify outcomes, or recover from interaction failures. Therefore, the next step in the literature review is to move from LLM foundations to agent architectures, where LLMs are embedded in systems with planning, tools, memory, feedback, and environment grounding.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\writing\S2_refined_synthesis_after_P1.md

# S2 Refined Synthesis — Foundations of LLMs for Agentic Tasks  
## Updated after P0 + first 10 P1 papers

## 1. What changed after adding the P1 papers

The P0 synthesis already established the core progression:

```text
Transformer → BERT → GPT-3 → InstructGPT → Chain-of-Thought → Self-Consistency
```

After reading the first 10 P1 papers, S2 becomes richer and more complete. The refined progression is now:

```text
Transformer
→ GPT-style generative pretraining / BERT / T5
→ GPT-3 in-context learning
→ FLAN + InstructGPT + Helpful/Harmless RLHF
→ Chain-of-Thought + Zero-shot-CoT + Self-Consistency + Least-to-Most
→ RAG
→ LLaVA / GPT-4 / Gemini 1.5
```

This can be summarized conceptually as:

```text
architecture
→ pretraining and transfer
→ task generalization
→ instruction following and alignment
→ reasoning and decomposition
→ retrieval and external memory
→ multimodal and long-context foundation models
```

The P1 papers do not replace the P0 narrative. They refine it by showing that LLM-based agents require more than one foundation. They require language understanding, prompting, instruction following, reasoning, retrieval, multimodal perception, long-context processing, and alignment.

---

## 2. Refined narrative

Section S2 explains how modern LLM-based agents became possible. The foundation begins with the Transformer, which introduced scalable self-attention and enabled efficient training of large sequence models. This architecture made it possible to process instructions, documents, HTML, DOM text, action histories, and other web-related inputs as token sequences.

The next step was transfer learning through large-scale pretraining. GPT-style generative pretraining showed that a Transformer decoder trained on unlabeled text could transfer to many language understanding tasks through fine-tuning. BERT showed that bidirectional Transformer pretraining could produce strong contextual representations for language understanding. T5 then unified many NLP tasks under a text-to-text framework, showing that classification, translation, summarization, question answering, and other tasks can be represented as conditional text generation. Together, these works established that one pretrained model can serve as a reusable foundation across many tasks.

GPT-3 then shifted the field from task-specific fine-tuning toward in-context learning. Instead of training a separate model for every task, GPT-3 showed that large language models can perform new tasks from prompts and examples. This is essential for generalized web automation because a web agent cannot be fine-tuned for every website, form, workflow, or extraction schema.

Instruction following became the next major step. FLAN showed that instruction tuning on many tasks expressed in natural language improves zero-shot generalization to unseen task types. InstructGPT and the Helpful/Harmless RLHF work showed that large models must also be aligned with user intent and safety preferences. For web agents, this is critical because user goals are expressed as instructions, but agent behavior must also respect constraints, avoid unsafe actions, and handle harmful or ambiguous requests.

Reasoning methods then made LLMs more agent-relevant. Chain-of-thought prompting showed that large models can solve harder tasks by generating intermediate reasoning steps. Zero-shot-CoT showed that even a simple prompt such as “Let’s think step by step” can elicit reasoning without few-shot examples. Self-consistency improved reasoning reliability by sampling multiple reasoning paths and selecting the most consistent answer. Least-to-most prompting added explicit decomposition: complex tasks can be broken into simpler subproblems and solved sequentially. This is directly relevant to web agents because web automation tasks naturally require decomposition into subgoals and actions.

RAG added another essential foundation: external memory and retrieval. Pure LLMs rely on parametric knowledge stored in model weights, which can be outdated, incomplete, or hallucinated. Retrieval-augmented generation combines a generator with an external retriever, allowing outputs to be grounded in retrieved evidence. For web data extraction and web automation, this is important because agents often need current, source-grounded, and verifiable information from pages, documents, search results, or databases.

Finally, multimodal and long-context models expanded what LLMs can perceive and process. LLaVA introduced visual instruction tuning, showing how instruction-following can be extended to image-language models. GPT-4 demonstrated strong frontier multimodal capabilities and professional-level benchmark performance, while still showing limitations such as hallucination and lack of learning from experience. Gemini 1.5 pushed the long-context frontier, showing that models can process millions of tokens across text, code, audio, and video. This is important for web agents because real web tasks often involve screenshots, long pages, large DOM trees, multiple documents, action histories, and multimodal content.

Therefore, S2 should not be written only as a history of LLMs. It should be written as the construction of the agentic capability stack.

---

## 3. Refined capability stack for LLM-based web agents

The papers in S2 provide the following capabilities:

| Capability | Main papers | Why it matters for web agents |
|---|---|---|
| Scalable sequence modeling | Transformer | Enables LLMs to process instructions, pages, and histories as sequences |
| Pretraining and transfer | GPT-1, BERT, T5 | Enables reusable language representations and task adaptation |
| In-context learning | GPT-3 | Enables adaptation to new web tasks without fine-tuning |
| Instruction following | FLAN, InstructGPT | Enables natural-language control of agents |
| Alignment and safety | InstructGPT, Helpful/Harmless RLHF | Helps constrain agent behavior and reduce harmful compliance |
| Step-by-step reasoning | Chain-of-Thought, Zero-shot-CoT | Supports task decomposition and intermediate reasoning |
| Reasoning robustness | Self-Consistency | Reduces reliance on one reasoning path |
| Hierarchical decomposition | Least-to-Most | Supports subgoal-based web task planning |
| Retrieval and external memory | RAG | Grounds answers in external evidence and supports factuality |
| Multimodal perception | LLaVA, GPT-4 | Enables screenshot, visual layout, and document understanding |
| Long-context processing | Gemini 1.5 | Helps with long DOMs, long documents, action histories, and multi-page tasks |

---

## 4. Refined gap

After P0 papers, the main gap was:

```text
LLMs are strong at language reasoning, but weak as grounded, reliable, interactive web agents.
```

After adding the P1 papers, this gap becomes more precise:

```text
Modern LLMs provide many agent-relevant capabilities, but these capabilities remain fragmented and insufficient for reliable generalized web automation unless they are integrated into a grounded agent loop.
```

The P1 papers show that LLMs can now:

```text
transfer across tasks
follow instructions
reason step by step
decompose problems
retrieve external evidence
process images and text
handle long contexts
align better with user preferences
```

But they still do not fully solve:

```text
DOM-grounded perception
reliable UI element selection
browser action execution
state tracking across pages
long-horizon planning under uncertainty
error recovery after failed actions
verification of extracted data
safe autonomous operation
deployment cost and latency
robustness across unseen websites
```

So the refined gap is not simply “LLMs cannot act.”  
The refined gap is:

```text
LLMs provide the cognitive components of agency, but generalized web automation requires system-level integration of perception, planning, action, memory, retrieval, safety, and verification.
```

---

## 5. Refined thesis connection

For the thesis topic, “LLM-based agents for generalized web automation and data extraction,” S2 supports four major claims.

### Claim 1 — LLMs provide the cognitive core of agents

Transformer-based LLMs provide the language understanding and reasoning foundation for web agents. GPT-style pretraining, BERT, T5, GPT-3, FLAN, and InstructGPT show that LLMs can understand language, adapt to tasks, follow instructions, and produce useful outputs.

### Claim 2 — Agentic behavior requires reasoning and decomposition

Chain-of-thought, Zero-shot-CoT, Self-Consistency, and Least-to-Most prompting show that LLMs can perform multi-step reasoning and problem decomposition. These capabilities are necessary for web automation because a user goal must be transformed into subgoals, actions, observations, and corrections.

### Claim 3 — Web agents need grounding beyond parametric knowledge

RAG shows that LLMs need external knowledge sources to improve factuality, updateability, and provenance. LLaVA, GPT-4, and Gemini 1.5 show that agents increasingly need multimodal perception and long-context processing. This is important because web environments contain text, visual layout, DOM structures, screenshots, documents, tables, and long interaction histories.

### Claim 4 — LLM capabilities alone are not enough

Even with instruction following, reasoning, retrieval, multimodality, and long context, LLMs do not automatically become reliable web agents. They must be embedded in architectures that include tools, browser control, memory, grounding, safety constraints, feedback loops, and evaluation mechanisms.

---

## 6. Refined thesis-ready synthesis paragraph

The foundations of LLM-based agents emerge from a sequence of advances in language modeling, transfer learning, prompting, alignment, retrieval, multimodality, and long-context modeling. The Transformer introduced scalable self-attention, enabling large models to process sequences efficiently. GPT-style generative pretraining, BERT, and T5 then demonstrated that pretrained Transformer models can transfer across a wide range of language understanding and generation tasks, with T5 further unifying NLP tasks under a text-to-text formulation. GPT-3 shifted this paradigm toward in-context learning, showing that sufficiently large models can adapt to new tasks from prompts and examples without task-specific fine-tuning. FLAN, InstructGPT, and helpful/harmless RLHF further transformed LLMs into instruction-following and preference-aligned systems, making them more suitable as user-facing assistants. Reasoning-oriented methods such as chain-of-thought prompting, Zero-shot-CoT, self-consistency, and least-to-most prompting showed that LLMs can perform step-by-step reasoning, sample multiple reasoning paths, and decompose complex problems into subproblems. Retrieval-augmented generation added external memory and provenance, while LLaVA, GPT-4, and Gemini 1.5 extended the foundation toward multimodal perception and long-context understanding. Together, these works explain why LLMs can serve as the cognitive core of web agents. However, they also reveal the central limitation motivating this thesis: LLMs alone do not provide grounded browser perception, reliable action execution, state tracking, error recovery, safety control, or verification of extracted data. Generalized web automation therefore requires agent architectures that integrate LLM reasoning with tools, memory, retrieval, DOM and visual grounding, feedback loops, and robust evaluation.

---

## 7. Refined limitations connected to the thesis

### 7.1 Pretraining and transfer limitation

GPT-1, BERT, and T5 show that pretrained models can transfer across NLP tasks, but they mostly operate on static textual inputs.

For web agents, this matters because web automation is not only an NLP task. A web agent must interact with dynamic pages, execute actions, observe results, and update its state. This motivates the move from static transfer learning to interactive agent architectures.

### 7.2 In-context learning limitation

GPT-3 shows that models can adapt to tasks through prompts, but prompt-based task completion is still not grounded interaction.

For web agents, this matters because a prompt can specify a task, but the model still needs browser access, DOM grounding, memory, and feedback to complete the task reliably.

### 7.3 Instruction-following limitation

FLAN, InstructGPT, and RLHF models improve instruction following, but instruction following alone does not guarantee correct autonomous action.

For web agents, this matters because a model can appear helpful while still choosing the wrong button, submitting wrong data, leaking sensitive information, or hallucinating an extracted value.

### 7.4 Reasoning limitation

Chain-of-thought, Zero-shot-CoT, Self-Consistency, and Least-to-Most improve reasoning, but reasoning traces are not guaranteed to be faithful or grounded.

For web agents, this matters because plausible reasoning can still be based on a wrong page interpretation, a stale observation, or a nonexistent DOM element.

### 7.5 Retrieval limitation

RAG grounds generation in retrieved evidence, but it depends on retrieval quality and does not perform browser actions.

For web agents, this matters because retrieved documents may be irrelevant, stale, duplicated, or incomplete. The agent still needs to verify evidence against the live page and connect evidence to actions or extracted fields.

### 7.6 Multimodal limitation

LLaVA and GPT-4 show that models can reason over images and text, but visual understanding is not the same as UI grounding.

For web agents, this matters because a screenshot-level understanding must be connected to precise elements, coordinates, DOM nodes, forms, and interaction affordances.

### 7.7 Long-context limitation

Gemini 1.5 shows that long-context models can process millions of tokens, but more context does not automatically mean better agency.

For web agents, this matters because full DOMs, action histories, and documents may fit in context, but the model still needs relevance selection, planning, action control, and verification. Long context also introduces cost and latency issues.

### 7.8 Alignment and safety limitation

Helpful/harmless RLHF improves assistant behavior, but it does not guarantee safe autonomous web execution.

For web agents, this matters because agents can take actions that affect users, websites, accounts, or third parties. Safety requires action constraints, permission boundaries, risk detection, and human oversight.

---

## 8. Refined transition to S3

S2 ends by showing that modern LLMs provide the building blocks of agency:

```text
understanding
instruction following
reasoning
decomposition
retrieval
multimodal perception
long-context processing
alignment
```

But these are still building blocks, not a complete agent.

Therefore, S3 should begin with the question:

```text
How are these LLM capabilities organized into agent architectures?
```

S3 should then explain how later systems wrap LLMs with:

```text
planning
memory
tools
reflection
action execution
environment feedback
multi-agent coordination
evaluation loops
```

This transition is important because it moves the literature review from:

```text
LLMs as models
```

to:

```text
LLMs as components inside agents
```

---

## 9. Final refined S2 synthesis

S2 demonstrates that LLM-based agents are built on a layered foundation. The Transformer made scalable sequence modeling possible. GPT-style pretraining, BERT, and T5 established transfer learning and reusable language representations. GPT-3 introduced in-context task generalization. FLAN, InstructGPT, and helpful/harmless RLHF improved instruction following and alignment. Chain-of-thought, Zero-shot-CoT, Self-Consistency, and Least-to-Most prompting strengthened reasoning, reliability, and decomposition. RAG introduced retrieval and external memory. LLaVA, GPT-4, and Gemini 1.5 extended the foundation toward multimodal and long-context understanding.

These advances explain why LLMs are suitable as the cognitive core of web agents. They can understand instructions, reason over observations, retrieve information, process long contexts, and interpret multimodal inputs. However, S2 also shows that LLMs alone are not sufficient for generalized web automation and data extraction. They do not inherently provide grounded perception, browser action execution, reliable state tracking, error recovery, safety control, or verification. The next stage of the literature review must therefore examine agent architectures that integrate LLMs with tools, memory, planning, environment feedback, DOM and visual grounding, and robust evaluation.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S2\writing\S2_refined_synthesis_after_P1_with_cross_links.md

# S2 Refined Synthesis — Foundations of LLMs for Agentic Tasks  
## Updated after P0 + first 10 P1 papers

## 1. What changed after adding the P1 papers

The P0 synthesis already established the core progression:

```text
Transformer → BERT → GPT-3 → InstructGPT → Chain-of-Thought → Self-Consistency
```

After reading the first 10 P1 papers, S2 becomes richer and more complete. The refined progression is now:

```text
Transformer
→ GPT-style generative pretraining / BERT / T5
→ GPT-3 in-context learning
→ FLAN + InstructGPT + Helpful/Harmless RLHF
→ Chain-of-Thought + Zero-shot-CoT + Self-Consistency + Least-to-Most
→ RAG
→ LLaVA / GPT-4 / Gemini 1.5
```

This can be summarized conceptually as:

```text
architecture
→ pretraining and transfer
→ task generalization
→ instruction following and alignment
→ reasoning and decomposition
→ retrieval and external memory
→ multimodal and long-context foundation models
```

The P1 papers do not replace the P0 narrative. They refine it by showing that LLM-based agents require more than one foundation. They require language understanding, prompting, instruction following, reasoning, retrieval, multimodal perception, long-context processing, and alignment.

---

## 2. Refined narrative

Section S2 explains how modern LLM-based agents became possible. The foundation begins with the Transformer, which introduced scalable self-attention and enabled efficient training of large sequence models. This architecture made it possible to process instructions, documents, HTML, DOM text, action histories, and other web-related inputs as token sequences.

The next step was transfer learning through large-scale pretraining. GPT-style generative pretraining showed that a Transformer decoder trained on unlabeled text could transfer to many language understanding tasks through fine-tuning. BERT showed that bidirectional Transformer pretraining could produce strong contextual representations for language understanding. T5 then unified many NLP tasks under a text-to-text framework, showing that classification, translation, summarization, question answering, and other tasks can be represented as conditional text generation. Together, these works established that one pretrained model can serve as a reusable foundation across many tasks.

GPT-3 then shifted the field from task-specific fine-tuning toward in-context learning. Instead of training a separate model for every task, GPT-3 showed that large language models can perform new tasks from prompts and examples. This is essential for generalized web automation because a web agent cannot be fine-tuned for every website, form, workflow, or extraction schema.

Instruction following became the next major step. FLAN showed that instruction tuning on many tasks expressed in natural language improves zero-shot generalization to unseen task types. InstructGPT and the Helpful/Harmless RLHF work showed that large models must also be aligned with user intent and safety preferences. For web agents, this is critical because user goals are expressed as instructions, but agent behavior must also respect constraints, avoid unsafe actions, and handle harmful or ambiguous requests.

Reasoning methods then made LLMs more agent-relevant. Chain-of-thought prompting showed that large models can solve harder tasks by generating intermediate reasoning steps. Zero-shot-CoT showed that even a simple prompt such as “Let’s think step by step” can elicit reasoning without few-shot examples. Self-consistency improved reasoning reliability by sampling multiple reasoning paths and selecting the most consistent answer. Least-to-most prompting added explicit decomposition: complex tasks can be broken into simpler subproblems and solved sequentially. This is directly relevant to web agents because web automation tasks naturally require decomposition into subgoals and actions.

RAG added another essential foundation: external memory and retrieval. Pure LLMs rely on parametric knowledge stored in model weights, which can be outdated, incomplete, or hallucinated. Retrieval-augmented generation combines a generator with an external retriever, allowing outputs to be grounded in retrieved evidence. For web data extraction and web automation, this is important because agents often need current, source-grounded, and verifiable information from pages, documents, search results, or databases.

Finally, multimodal and long-context models expanded what LLMs can perceive and process. LLaVA introduced visual instruction tuning, showing how instruction-following can be extended to image-language models. GPT-4 demonstrated strong frontier multimodal capabilities and professional-level benchmark performance, while still showing limitations such as hallucination and lack of learning from experience. Gemini 1.5 pushed the long-context frontier, showing that models can process millions of tokens across text, code, audio, and video. This is important for web agents because real web tasks often involve screenshots, long pages, large DOM trees, multiple documents, action histories, and multimodal content.

Therefore, S2 should not be written only as a history of LLMs. It should be written as the construction of the agentic capability stack.

---

## 3. Refined capability stack for LLM-based web agents

The papers in S2 provide the following capabilities:

| Capability | Main papers | Why it matters for web agents |
|---|---|---|
| Scalable sequence modeling | Transformer | Enables LLMs to process instructions, pages, and histories as sequences |
| Pretraining and transfer | GPT-1, BERT, T5 | Enables reusable language representations and task adaptation |
| In-context learning | GPT-3 | Enables adaptation to new web tasks without fine-tuning |
| Instruction following | FLAN, InstructGPT | Enables natural-language control of agents |
| Alignment and safety | InstructGPT, Helpful/Harmless RLHF | Helps constrain agent behavior and reduce harmful compliance |
| Step-by-step reasoning | Chain-of-Thought, Zero-shot-CoT | Supports task decomposition and intermediate reasoning |
| Reasoning robustness | Self-Consistency | Reduces reliance on one reasoning path |
| Hierarchical decomposition | Least-to-Most | Supports subgoal-based web task planning |
| Retrieval and external memory | RAG | Grounds answers in external evidence and supports factuality |
| Multimodal perception | LLaVA, GPT-4 | Enables screenshot, visual layout, and document understanding |
| Long-context processing | Gemini 1.5 | Helps with long DOMs, long documents, action histories, and multi-page tasks |

---

## 4. Refined gap

After P0 papers, the main gap was:

```text
LLMs are strong at language reasoning, but weak as grounded, reliable, interactive web agents.
```

After adding the P1 papers, this gap becomes more precise:

```text
Modern LLMs provide many agent-relevant capabilities, but these capabilities remain fragmented and insufficient for reliable generalized web automation unless they are integrated into a grounded agent loop.
```

The P1 papers show that LLMs can now:

```text
transfer across tasks
follow instructions
reason step by step
decompose problems
retrieve external evidence
process images and text
handle long contexts
align better with user preferences
```

But they still do not fully solve:

```text
DOM-grounded perception
reliable UI element selection
browser action execution
state tracking across pages
long-horizon planning under uncertainty
error recovery after failed actions
verification of extracted data
safe autonomous operation
deployment cost and latency
robustness across unseen websites
```

So the refined gap is not simply “LLMs cannot act.”  
The refined gap is:

```text
LLMs provide the cognitive components of agency, but generalized web automation requires system-level integration of perception, planning, action, memory, retrieval, safety, and verification.
```

---

## 5. Refined thesis connection

For the thesis topic, “LLM-based agents for generalized web automation and data extraction,” S2 supports four major claims.

### Claim 1 — LLMs provide the cognitive core of agents

Transformer-based LLMs provide the language understanding and reasoning foundation for web agents. GPT-style pretraining, BERT, T5, GPT-3, FLAN, and InstructGPT show that LLMs can understand language, adapt to tasks, follow instructions, and produce useful outputs.

### Claim 2 — Agentic behavior requires reasoning and decomposition

Chain-of-thought, Zero-shot-CoT, Self-Consistency, and Least-to-Most prompting show that LLMs can perform multi-step reasoning and problem decomposition. These capabilities are necessary for web automation because a user goal must be transformed into subgoals, actions, observations, and corrections.

### Claim 3 — Web agents need grounding beyond parametric knowledge

RAG shows that LLMs need external knowledge sources to improve factuality, updateability, and provenance. LLaVA, GPT-4, and Gemini 1.5 show that agents increasingly need multimodal perception and long-context processing. This is important because web environments contain text, visual layout, DOM structures, screenshots, documents, tables, and long interaction histories.

### Claim 4 — LLM capabilities alone are not enough

Even with instruction following, reasoning, retrieval, multimodality, and long context, LLMs do not automatically become reliable web agents. They must be embedded in architectures that include tools, browser control, memory, grounding, safety constraints, feedback loops, and evaluation mechanisms.

---

## 6. Refined thesis-ready synthesis paragraph

The foundations of LLM-based agents emerge from a sequence of advances in language modeling, transfer learning, prompting, alignment, retrieval, multimodality, and long-context modeling. The Transformer introduced scalable self-attention, enabling large models to process sequences efficiently. GPT-style generative pretraining, BERT, and T5 then demonstrated that pretrained Transformer models can transfer across a wide range of language understanding and generation tasks, with T5 further unifying NLP tasks under a text-to-text formulation. GPT-3 shifted this paradigm toward in-context learning, showing that sufficiently large models can adapt to new tasks from prompts and examples without task-specific fine-tuning. FLAN, InstructGPT, and helpful/harmless RLHF further transformed LLMs into instruction-following and preference-aligned systems, making them more suitable as user-facing assistants. Reasoning-oriented methods such as chain-of-thought prompting, Zero-shot-CoT, self-consistency, and least-to-most prompting showed that LLMs can perform step-by-step reasoning, sample multiple reasoning paths, and decompose complex problems into subproblems. Retrieval-augmented generation added external memory and provenance, while LLaVA, GPT-4, and Gemini 1.5 extended the foundation toward multimodal perception and long-context understanding. Together, these works explain why LLMs can serve as the cognitive core of web agents. However, they also reveal the central limitation motivating this thesis: LLMs alone do not provide grounded browser perception, reliable action execution, state tracking, error recovery, safety control, or verification of extracted data. Generalized web automation therefore requires agent architectures that integrate LLM reasoning with tools, memory, retrieval, DOM and visual grounding, feedback loops, and robust evaluation.

---

## 7. Refined limitations connected to the thesis

### 7.1 Pretraining and transfer limitation

GPT-1, BERT, and T5 show that pretrained models can transfer across NLP tasks, but they mostly operate on static textual inputs.

For web agents, this matters because web automation is not only an NLP task. A web agent must interact with dynamic pages, execute actions, observe results, and update its state. This motivates the move from static transfer learning to interactive agent architectures.

### 7.2 In-context learning limitation

GPT-3 shows that models can adapt to tasks through prompts, but prompt-based task completion is still not grounded interaction.

For web agents, this matters because a prompt can specify a task, but the model still needs browser access, DOM grounding, memory, and feedback to complete the task reliably.

### 7.3 Instruction-following limitation

FLAN, InstructGPT, and RLHF models improve instruction following, but instruction following alone does not guarantee correct autonomous action.

For web agents, this matters because a model can appear helpful while still choosing the wrong button, submitting wrong data, leaking sensitive information, or hallucinating an extracted value.

### 7.4 Reasoning limitation

Chain-of-thought, Zero-shot-CoT, Self-Consistency, and Least-to-Most improve reasoning, but reasoning traces are not guaranteed to be faithful or grounded.

For web agents, this matters because plausible reasoning can still be based on a wrong page interpretation, a stale observation, or a nonexistent DOM element.

### 7.5 Retrieval limitation

RAG grounds generation in retrieved evidence, but it depends on retrieval quality and does not perform browser actions.

For web agents, this matters because retrieved documents may be irrelevant, stale, duplicated, or incomplete. The agent still needs to verify evidence against the live page and connect evidence to actions or extracted fields.

### 7.6 Multimodal limitation

LLaVA and GPT-4 show that models can reason over images and text, but visual understanding is not the same as UI grounding.

For web agents, this matters because a screenshot-level understanding must be connected to precise elements, coordinates, DOM nodes, forms, and interaction affordances.

### 7.7 Long-context limitation

Gemini 1.5 shows that long-context models can process millions of tokens, but more context does not automatically mean better agency.

For web agents, this matters because full DOMs, action histories, and documents may fit in context, but the model still needs relevance selection, planning, action control, and verification. Long context also introduces cost and latency issues.

### 7.8 Alignment and safety limitation

Helpful/harmless RLHF improves assistant behavior, but it does not guarantee safe autonomous web execution.

For web agents, this matters because agents can take actions that affect users, websites, accounts, or third parties. Safety requires action constraints, permission boundaries, risk detection, and human oversight.

---

## 8. Refined transition to S3

S2 ends by showing that modern LLMs provide the building blocks of agency:

```text
understanding
instruction following
reasoning
decomposition
retrieval
multimodal perception
long-context processing
alignment
```

But these are still building blocks, not a complete agent.

Therefore, S3 should begin with the question:

```text
How are these LLM capabilities organized into agent architectures?
```

S3 should then explain how later systems wrap LLMs with:

```text
planning
memory
tools
reflection
action execution
environment feedback
multi-agent coordination
evaluation loops
```

This transition is important because it moves the literature review from:

```text
LLMs as models
```

to:

```text
LLMs as components inside agents
```

---

## 9. Final refined S2 synthesis

S2 demonstrates that LLM-based agents are built on a layered foundation. The Transformer made scalable sequence modeling possible. GPT-style pretraining, BERT, and T5 established transfer learning and reusable language representations. GPT-3 introduced in-context task generalization. FLAN, InstructGPT, and helpful/harmless RLHF improved instruction following and alignment. Chain-of-thought, Zero-shot-CoT, Self-Consistency, and Least-to-Most prompting strengthened reasoning, reliability, and decomposition. RAG introduced retrieval and external memory. LLaVA, GPT-4, and Gemini 1.5 extended the foundation toward multimodal and long-context understanding.

These advances explain why LLMs are suitable as the cognitive core of web agents. They can understand instructions, reason over observations, retrieve information, process long contexts, and interpret multimodal inputs. However, S2 also shows that LLMs alone are not sufficient for generalized web automation and data extraction. They do not inherently provide grounded perception, browser action execution, reliable state tracking, error recovery, safety control, or verification. The next stage of the literature review must therefore examine agent architectures that integrate LLMs with tools, memory, planning, environment feedback, DOM and visual grounding, and robust evaluation.

---

## Cross-links to later sections

| Paper | Feeds |
|-------|-------|
| RAG | S6 (extraction), S7 (verification) |
| LLaVA, GPT-4 | S5.2 (multimodal grounding) |
| Gemini 1.5 | S5.2 (long DOM), S5.3 (long-horizon) |
| Least-to-most | S5.3 (task decomposition) |
| Bai et al. RLHF | S7 (safety, alignment) |
| Zero-shot-CoT | S5.3 (planning without demos) |


---


Total files merged: 22
