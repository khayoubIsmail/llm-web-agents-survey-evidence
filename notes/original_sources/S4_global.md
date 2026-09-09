# S4 - Evolution of Web Agent Systems

Generated on: 2026-05-07 23:40

---

## P0 (5 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P0\2017 - World of Bits- An Open-Domain Platform for Web-Based Agents.md

# Paper 280 — World of Bits: An Open-Domain Platform for Web-Based Agents

## Metadata

- **Title:** World of Bits: An Open-Domain Platform for Web-Based Agents
- **Authors:** Tianlin (Tim) Shi, Andrej Karpathy, Linxi (Jim) Fan, Jonathan Hernandez, Percy Liang
- **Year:** 2017
- **Venue:** Proceedings of the 34th International Conference on Machine Learning (ICML 2017), PMLR 70
- **Pages:** 3135–3144
- **DOI:** No standard DOI listed by PMLR / ACM proceedings record: 10.5555/3305890.3306005
- **arXiv ID:** Not listed in the paper
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 — Benchmarks and Evaluation; S5.2 — Perception and Grounding; S5.3 — Planning and Decision-Making; S5.4 — Training Strategies; S5.5 — Failure Modes; S8 — Deployment Realities
- **Category:** WEB-F / BENCHMARK / RL-BASED WEB AGENTS
- **Paper type:** Benchmark / platform / early web-agent environment
- **Priority:** P0
- **BibTeX key:** shi2017world

---

## Simple understanding

This paper introduces **World of Bits (WoB)**, one of the earliest open-domain platforms for training agents to interact with web interfaces.

The central idea is simple:

```text
web page = environment
agent observation = screen pixels + DOM + reward
agent action = keyboard and mouse commands
```

Unlike classical NLP tasks, WoB treats the web as an **interactive environment**. The agent does not only read text; it must click, type, drag, scroll, and complete tasks on webpages.

The paper introduces three related task collections:

```text
MiniWoB → synthetic controlled web tasks
FormWoB → cached real flight-booking websites
QAWoB → crowdsourced question-answering tasks on real websites
```

For my thesis, this paper is foundational because it frames the web as a benchmark environment for agents before the LLM era. It shows why web automation is difficult: the agent must connect natural language instructions, visual perception, DOM structure, low-level actions, sparse rewards, and long-horizon interaction.

---

## Notes

- **Core idea:**
  Introduces a web-based RL platform where agents complete tasks on websites using low-level keyboard and mouse actions while observing pixels, DOM elements, and rewards.

- **Key finding:**
  Agents trained with behavioral cloning and reinforcement learning can solve some simple web tasks, but performance remains low on complex tasks. On MiniWoB, SL+RL reaches 34.8 human-normalized success rate overall, but only 4.3 on compound tasks and 7.8 on mouse+keyboard tasks.

- **Limitation:**
  WoB uses low-level mouse and keyboard actions.
  For web agents, this matters because low-level control makes exploration difficult and increases trajectory length. Modern LLM web agents often use higher-level actions such as `click(element)`, `type(text)`, or `select(option)` to reduce search space.

- **Additional limitation:**
  RL struggles with sparse rewards and long-horizon web tasks.
  For my thesis, this directly motivates LLM-based agents: instead of learning from random exploration, modern agents can use language understanding, planning, demonstrations, and reasoning.

- **Additional limitation:**
  FormWoB uses cached HTTP traffic to make live sites reproducible.
  For web agents, this matters because reproducibility conflicts with realism: cached sites are stable but not fully live; live sites are realistic but unstable.

- **Additional limitation:**
  MiniWoB is controlled and useful but simplified.
  For generalized web automation, this means MiniWoB cannot represent all real-world issues: authentication, pop-ups, ads, dynamic JavaScript, anti-bot defenses, full-page layout, and visual complexity.

- **Additional limitation:**
  QAWoB is scalable but reward design remains difficult.
  For web extraction, this matters because defining correct success criteria for open-ended web tasks is still one of the major evaluation challenges.

- **Connects to:**
  WebShop, MiniWoB++, DOM-Q-NET, RL-based web agents, Mind2Web, WebArena, BrowserGym, and modern browser-agent benchmarks.

- **Use in thesis:**
  Use WoB to introduce the pre-LLM web-agent era and explain why the web became an attractive but difficult environment for agent research. It is the historical foundation for S4.

- **BibTeX key:**
  shi2017world

---

## Thesis-ready paragraph

Shi et al. introduced World of Bits, an open-domain platform for training agents to perform tasks on the web through low-level keyboard and mouse actions. The platform represents webpages through rendered pixels and DOM information, allowing agents to interact with real browser interfaces rather than simplified symbolic environments. World of Bits is important because it reframed the web as an interactive benchmark for agents, combining natural language instructions, visual perception, DOM grounding, and action execution. However, the paper also exposed the difficulty of web automation before the LLM era: behavioral cloning and reinforcement learning achieved only limited success, especially on tasks requiring keyboard input, compound actions, or long-horizon interaction. For LLM-based web automation, WoB provides the historical starting point: it shows that the web is a rich environment for agents, but that low-level RL alone is insufficient for robust generalization.

---

## Why this paper matters for my thesis

This paper matters because it is the first major step in treating the web as an agent environment.

For my thesis, the important shift is:

```text
classical web automation = scripts and wrappers
World of Bits = learning agents that interact with web interfaces
```

WoB shows that web automation requires multiple skills:

```text
understand instruction
perceive page
locate element
choose action
execute click/type/scroll
observe change
complete task
```

This is exactly the foundation of generalized web automation.

However, WoB also shows why early web agents were limited:

```text
low-level actions are hard
RL exploration is inefficient
rewards are sparse
websites change
tasks require long horizons
DOM + pixels must be grounded
```

This motivates the shift toward LLM-based web agents, where language models provide instruction understanding, reasoning, planning, and reusable knowledge.

---

## Important concepts to remember

### 1. Web as an environment

The paper treats a website as an environment similar to a game or robot world.

The agent observes:

```text
screen pixels
DOM elements
reward
```

and acts through:

```text
keyboard events
mouse events
```

### 2. DOM grounding

Each DOM element is associated with a bounding box.

This is important because it connects:

```text
HTML structure ↔ visual screen location ↔ mouse action
```

This is still central in modern web agents.

### 3. MiniWoB

MiniWoB is a set of 100 small synthetic web tasks.

Examples include:

```text
click button
choose dropdown
enter text
use date picker
drag slider
search/reply/compound tasks
```

MiniWoB is controlled, reproducible, and useful for RL experiments.

### 4. FormWoB

FormWoB converts real flight-booking websites into reproducible tasks by caching HTTP traffic.

This introduces an important tension:

```text
live web realism vs reproducible offline evaluation
```

### 5. QAWoB

QAWoB crowdsources web tasks as question answering.

A worker writes a query, performs the task on a real website, and marks the DOM answer element.

This is an early attempt to scale web-task collection.

### 6. Behavioral cloning + reinforcement learning

The paper trains agents using:

```text
human demonstrations → supervised learning
then
policy gradient RL → improve reward
```

This prefigures later imitation-learning and RLHF-based web agents.

---

## Key evidence from the paper

### Figure 1 — WoB observation/action interface

Figure 1 shows that agents perceive:

```text
screen pixels
DOM with coordinates
reward
```

and output:

```text
keyboard commands
mouse commands
```

This figure is important because it defines the basic web-agent perception-action interface.

### Figure 2 — Open-domain web task examples

Figure 2 shows diverse tasks such as booking flights, finding restaurants, calculating payments, checking product prices, and finding recipes.

This supports the thesis claim that the web is a broad, open-domain environment.

### Figure 3 — MiniWoB tasks

Figure 3 shows examples ranging from simple buttons to more complex web interactions.

This helps explain the controlled benchmark side of WoB.

### Table 1 — MiniWoB results

The paper reports:

```text
Random: 20.8
SL: 24.8
SL+RL: 34.8
Mouse+Keyboard: 7.8
Compound: 4.3
```

This is strong evidence that early RL agents struggle with complex web tasks.

### FormWoB

FormWoB uses cached real flight websites and shows the difficulty of working with dynamic web interfaces while maintaining reproducibility.

### QAWoB

QAWoB contains hundreds of query templates and thousands of queries, showing the potential of crowdsourcing web tasks at scale.

---

## Connection to earlier and later papers

### Connection to classical automation

Classical automation scripts assume known page structure.

WoB asks whether agents can learn to operate web interfaces more generally.

### Connection to WebShop

WebShop inherits the idea of the web as an interactive environment but simplifies the action space to search and choose actions.

```text
WoB = low-level keyboard/mouse
WebShop = higher-level semantic web actions
```

### Connection to WebGPT

WebGPT shifts from RL agents controlling UI to GPT-3 using a text-based browser for information seeking and cited answers.

### Connection to SeeAct and WebVoyager

SeeAct and WebVoyager return to browser interaction, but with multimodal LLMs instead of CNN/RL models.

### Connection to S5

WoB feeds several later problems:

```text
S5.1 evaluation and benchmark design
S5.2 DOM/pixel grounding
S5.3 long-horizon planning
S5.4 imitation + RL training
S5.5 failure modes
S8 reproducibility vs realism
```

---

## Connection to later thesis sections

- **S5.1 — Benchmarks and Evaluation:**
  WoB is one of the earliest benchmark platforms for web agents.

- **S5.2 — Perception and Grounding:**
  It introduces combined pixel and DOM observations with bounding boxes.

- **S5.3 — Planning and Decision-Making:**
  Compound MiniWoB tasks expose long-horizon planning difficulty.

- **S5.4 — Training Strategies:**
  It uses demonstrations, behavioral cloning, and reinforcement learning.

- **S5.5 — Failure Modes:**
  Poor performance on keyboard and compound tasks highlights exploration and grounding failures.

- **S8 — Deployment Realities:**
  It introduces the realism/reproducibility trade-off through cached websites.

---

## Limitation connected to thesis

World of Bits makes the web an agent environment, but it does not solve generalized web automation.

For my thesis, the full web-agent loop is:

```text
instruction → perception → grounding → planning → action → feedback → recovery → extraction → verification
```

WoB mainly provides:

```text
environment + observation/action interface + early training baselines
```

It does not provide:

- robust natural-language reasoning,
- LLM-based planning,
- semantic tool use,
- reliable DOM abstraction,
- multimodal web understanding,
- extraction verification,
- or safe deployment on live websites.

Therefore, WoB should be used as the historical foundation for S4: it shows the problem clearly before modern LLMs became available.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High
- **Main use:** Historical foundation for web-agent environments
- **Most important parts:**
  - Abstract
  - Introduction
  - Figure 1
  - Figure 2
  - Section 2.1: Web as an Environment
  - MiniWoB / FormWoB / QAWoB construction
  - Table 1
  - Discussion of low performance on compound tasks
  - Reproducibility/caching method

---

## One-sentence summary

World of Bits introduced the web as an open-domain interactive environment for agents, but its low-level RL approach struggled with long-horizon and compound web tasks, motivating later LLM-based web agents.

---

## BibTeX

```bibtex
@inproceedings{shi2017world,
  title     = {World of Bits: An Open-Domain Platform for Web-Based Agents},
  author    = {Shi, Tianlin and Karpathy, Andrej and Fan, Linxi and Hernandez, Jonathan and Liang, Percy},
  booktitle = {Proceedings of the 34th International Conference on Machine Learning},
  series    = {Proceedings of Machine Learning Research},
  volume    = {70},
  pages     = {3135--3144},
  year      = {2017},
  publisher = {PMLR},
  url       = {https://proceedings.mlr.press/v70/shi17a.html}
}
```

---

## Source links

- PMLR: https://proceedings.mlr.press/v70/shi17a.html
- PDF: https://proceedings.mlr.press/v70/shi17a/shi17a.pdf


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P0\2022-06 - WebGPT- Browser-Assisted Question-Answering with Human Feedback.md

# Paper 281 — WebGPT: Browser-Assisted Question-Answering with Human Feedback

## Metadata

- **Title:** WebGPT: Browser-assisted question-answering with human feedback
- **Authors:** Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, Xu Jiang, Karl Cobbe, Tyna Eloundou, Gretchen Krueger, Kevin Button, Matthew Knight, Benjamin Chess, John Schulman
- **Year:** 2022
- **First arXiv version:** 2021
- **Venue:** arXiv preprint / OpenAI technical report
- **DOI:** 10.48550/arXiv.2112.09332
- **arXiv ID:** arXiv:2112.09332
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 — Evaluation; S5.3 — Planning and Browsing; S5.4 — Human Feedback / Training; S6 — Web Information Extraction and QA; S7 — Verification and Trustworthiness; S8 — Deployment and Safety
- **Category:** WEB-F / LLM-WEB / BROWSING / HUMAN FEEDBACK
- **Paper type:** System / browser-assisted QA / human-feedback training
- **Priority:** P0
- **BibTeX key:** nakano2022webgpt

---

## Simple understanding

This paper introduces **WebGPT**, an early LLM-based web-browsing system.

WebGPT fine-tunes GPT-3 to answer long-form questions by using a **text-based browser**. The model can:

```text
search the web
click links
find text in a page
scroll
quote evidence
go back
finish browsing
write an answer with references
```

The system is trained with:

```text
human demonstrations → behavior cloning
human comparisons → reward model
reward model → RL or rejection sampling
```

The key idea is not only that the model uses the web, but that it must collect **references** while browsing. These references help humans judge whether the final answer is supported by evidence.

For my thesis, WebGPT is a turning point. It shifts web-agent research from pre-LLM RL systems to LLM agents that use browsing as an external information source and learn from human feedback.

---

## Notes

- **Core idea:**
  Fine-tunes GPT-3 to use a text-based browsing environment for long-form question answering, with cited references collected during browsing and human feedback used to optimize answer quality.

- **Key finding:**
  The best WebGPT model, a 175B best-of-64 model trained with behavior cloning and rejection sampling against a reward model, is preferred 56% of the time over human demonstrators and 69% of the time over highest-voted Reddit ELI5 answers. It also improves truthfulness over GPT-3 on TruthfulQA.

- **Limitation:**
  WebGPT is a text-based browser agent, not a full web automation agent.
  For web agents, this matters because it can search, click links, scroll, and quote, but it cannot interact with forms, buttons, dynamic interfaces, calendars, checkboxes, menus, or visual layouts in a general way.

- **Additional limitation:**
  WebGPT focuses on long-form QA, not generalized task execution.
  For my thesis, this matters because generalized web automation includes data extraction, form filling, comparison shopping, booking, account navigation, and multi-step workflows, not only answer synthesis.

- **Additional limitation:**
  References improve evaluation but can be cherry-picked.
  For web extraction and verification, this matters because cited evidence does not guarantee a fair or complete assessment of the source.

- **Additional limitation:**
  WebGPT can appear authoritative because of citations.
  For web agents, this matters because users may overtrust outputs even when the model makes subtle synthesis errors or uses unreliable sources.

- **Additional limitation:**
  Live web access introduces safety risks.
  For web agents, this matters because more capable systems could take actions that affect real websites, users, or third parties.

- **Connects to:**
  RAG, WebShop, ReAct, WebVoyager, browser agents, retrieval-based QA, citation-based verification, RLHF, and human feedback for agents.

- **Use in thesis:**
  Use WebGPT as the turning point from static LLMs to LLMs that browse and use web evidence. It is especially important for S4, S6, and S7.

- **BibTeX key:**
  nakano2022webgpt

---

## Thesis-ready paragraph

Nakano et al. introduced WebGPT, a browser-assisted question-answering system that fine-tunes GPT-3 to search and navigate a text-based web-browsing environment. The model learns to issue browser commands, collect textual references, and compose long-form answers supported by cited evidence. WebGPT is important for the evolution of web agents because it demonstrates that language models can be trained to use the web as an external information source, combining retrieval, navigation, synthesis, and human-feedback optimization. Its best model outperforms human demonstrators on ELI5 preference judgments and improves truthfulness over GPT-3 on TruthfulQA. However, WebGPT remains limited to text-based browsing and long-form QA. It does not solve full browser automation, visual grounding, form interaction, DOM-level action execution, structured extraction, or safe autonomous operation. For this thesis, WebGPT marks the shift from web environments as RL benchmarks to LLM-based browsing agents grounded in references and human feedback.

---

## Why this paper matters for my thesis

This paper matters because it is one of the first major examples of an LLM acting through a browser-like environment.

Before WebGPT:

```text
LLMs mostly answered from internal knowledge.
RL web agents interacted with pages but had weak language reasoning.
```

WebGPT combines both:

```text
LLM reasoning + web browsing + human feedback + references
```

For generalized web automation and data extraction, this matters because an agent should not only answer from memory. It should:

```text
search the web
inspect sources
collect evidence
cite references
synthesize answers
allow verification
```

However, WebGPT is still narrow:

```text
task = answer long-form questions
interface = text browser
actions = search/click/scroll/quote
output = answer with references
```

A generalized web agent must also:

```text
fill forms
click visual elements
use dynamic websites
extract structured fields
verify values
handle authentication and state
avoid unsafe actions
```

So WebGPT is a major transition paper, but not the final web-agent architecture.

---

## Important concepts to remember

### 1. Text-based browser

WebGPT converts browsing into a text command environment.

Actions include:

```text
Search <query>
Click link
Find in page
Quote text
Scroll
Back
End
```

This makes browsing easier for a language model because the action space is textual.

### 2. References

The model must quote text from pages while browsing.

These quotes become evidence for the final answer.

For thesis work, this is important because references support:

```text
traceability
verification
human evaluation
reduced hallucination
```

### 3. Behavior cloning

Humans demonstrate how to browse and answer questions.

The model is fine-tuned to imitate these demonstrations.

### 4. Reward modeling

Humans compare pairs of answers.

A reward model learns which answer is preferred.

### 5. Rejection sampling

The model generates multiple answers and selects the one with the highest reward-model score.

This is an inference-time optimization method.

### 6. Truthfulness

WebGPT improves truthfulness because it is incentivized to use reliable sources, but it can still quote unreliable sources and produce false answers.

### 7. Safety of live web access

The paper explicitly discusses risks of giving models access to the web.

This is highly relevant for web agents that can perform actions, not only retrieve information.

---

## Key evidence from the paper

### Figure 1 — Text-based web-browsing environment

Figure 1 shows the human interface and the textual observation given to the model.

This is important because it defines WebGPT’s browser abstraction.

### Table 1 — Browser commands

The command table shows the model’s action space:

```text
Search
Click
Find
Quote
Scroll
Top
Back
End
```

This is an early LLM-compatible browser action space.

### ELI5 results

The best 175B best-of-64 model is preferred:

```text
56% over human demonstrators
69% over highest-voted Reddit answers
```

This supports the claim that LLM + browsing + human feedback can outperform simple imitation.

### TruthfulQA results

WebGPT improves truthfulness compared with GPT-3, showing that browsing and references can reduce some falsehoods.

### Section 6.4 — References for factual evaluation

The paper explains why references help human evaluation:

```text
more accurate feedback
less noisy feedback
transparency
```

### Section 6.5 — Risks of live web access

The paper notes that live web access can introduce risks if models can affect the external world.

This is directly relevant for safe web automation.

---

## Connection to earlier and later papers

### Connection to RAG

RAG retrieves documents and conditions generation on them.

WebGPT turns retrieval into an interactive browsing process:

```text
RAG = retrieve passages
WebGPT = search, click, quote, then answer
```

### Connection to ReAct

WebGPT predates ReAct but uses an action-observation loop.

ReAct generalizes this pattern:

```text
reason → action → observation
```

### Connection to WebShop

WebShop moves from text-based QA browsing to grounded interactive e-commerce tasks with automatic rewards.

### Connection to SeeAct and WebVoyager

SeeAct and WebVoyager extend browser agents to multimodal live web interaction.

### Connection to S6

WebGPT is strongly relevant to web information extraction and source-grounded QA.

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  Human preference, reward models, factuality, and cited references.

- **S5.3 — Planning:**
  Browsing requires search, click, scroll, quote, and stopping decisions.

- **S5.4 — Training:**
  Demonstrations, reward modeling, RL, and rejection sampling.

- **S6 — Web Information Extraction:**
  WebGPT is a source-grounded web QA and evidence-gathering system.

- **S7 — Verification and Trustworthiness:**
  References help but do not fully solve cherry-picking, bias, or hallucination.

- **S8 — Deployment:**
  Live web access introduces safety and overreliance concerns.

---

## Limitation connected to thesis

WebGPT is an LLM browser agent, but it is not a generalized web automation agent.

For my thesis, generalized web automation requires:

```text
instruction → page perception → action planning → grounded UI action → feedback → extraction → verification
```

WebGPT mainly solves:

```text
question → web search/navigation → evidence quotes → answer synthesis
```

It does not solve:

- DOM-level action grounding,
- visual layout understanding,
- form filling,
- dynamic website workflows,
- structured extraction,
- multi-page state tracking beyond text summaries,
- or safe execution of real-world actions.

Therefore, WebGPT should be used as the **LLM-browsing turning point** in S4, especially for web QA and evidence-grounded generation.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Very high
- **Main use:** Turning point from LLMs to browser-assisted agents
- **Most important parts:**
  - Abstract
  - Figure 1
  - Table 1
  - Section 2: environment design
  - Section 3: demonstrations/comparisons/training
  - Section 4: ELI5 and TruthfulQA evaluation
  - Section 5: RL vs rejection sampling
  - Section 6.4: references for factual evaluation
  - Section 6.5: risks of live web access

---

## One-sentence summary

WebGPT fine-tunes GPT-3 to browse the web and answer questions with cited references using human feedback, marking a key transition toward LLM-based web agents but remaining limited to text-based QA rather than general web automation.

---

## BibTeX

```bibtex
@article{nakano2022webgpt,
  title   = {WebGPT: Browser-assisted question-answering with human feedback},
  author  = {Nakano, Reiichiro and Hilton, Jacob and Balaji, Suchir and Wu, Jeff and Ouyang, Long and Kim, Christina and Hesse, Christopher and Jain, Shantanu and Kosaraju, Vineet and Saunders, William and Jiang, Xu and Cobbe, Karl and Eloundou, Tyna and Krueger, Gretchen and Button, Kevin and Knight, Matthew and Chess, Benjamin and Schulman, John},
  journal = {arXiv preprint arXiv:2112.09332},
  year    = {2022},
  doi     = {10.48550/arXiv.2112.09332}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2112.09332
- PDF: https://cdn.openai.com/WebGPT.pdf


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P0\2022-07 - WebShop- Towards Scalable Real-World Web Interaction with Grounded Language Agents -- v1.md

# Paper 282 — WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents

## Metadata

- **Title:** WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents
- **Authors:** Shunyu Yao, Howard Chen, John Yang, Karthik Narasimhan
- **Year:** 2022
- **Venue:** Advances in Neural Information Processing Systems 35 (NeurIPS 2022)
- **Proceedings DOI:** 10.52202/068431-1508
- **arXiv DOI:** 10.48550/arXiv.2207.01206
- **arXiv ID:** arXiv:2207.01206
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 — Benchmarks and Evaluation; S5.2 — Perception and Interface Representation; S5.3 — Planning and Strategic Exploration; S5.4 — Imitation/RL Training; S5.5 — Failure Modes; S8 — Deployment and Sim-to-Real
- **Category:** WEB-F / BENCHMARK / GROUNDED LANGUAGE AGENTS
- **Paper type:** Benchmark / simulated web environment / agent evaluation
- **Priority:** P0
- **BibTeX key:** yao2022webshop

---

## Simple understanding

This paper introduces **WebShop**, a simulated e-commerce website benchmark for grounded language agents.

The task is:

```text
given a natural-language shopping instruction
→ search for products
→ inspect search results
→ open item pages
→ read descriptions/details
→ choose options
→ click Buy
→ receive reward
```

WebShop contains:

```text
1.18 million real-world products
12,087 crowdsourced instructions
over 1,600 human demonstrations
automatic reward
HTML mode + simple text mode
```

Compared with World of Bits, WebShop uses a more semantic action space:

```text
search[query]
choose[button/product/option]
```

instead of raw mouse and keyboard actions.

For my thesis, WebShop is crucial because it gives a scalable benchmark for **web interaction with language grounding**. It connects web automation, product search, instruction following, exploration, and data extraction.

---

## Notes

- **Core idea:**
  Introduces a scalable e-commerce web environment where agents follow natural-language product instructions, navigate pages, choose options, and purchase matching items with automatically computed rewards.

- **Key finding:**
  The best model reaches around 29% task success, outperforming rule heuristics at 9.6%, but remains far below human expert performance at 59%. The paper also shows non-trivial sim-to-real transfer to Amazon.

- **Limitation:**
  WebShop is simulated, not a fully live web environment.
  For web agents, this matters because real websites contain changing layouts, ads, pop-ups, authentication, CAPTCHAs, tracking, dynamic JavaScript, and unpredictable failures.

- **Additional limitation:**
  WebShop is e-commerce-specific.
  For generalized web automation, this matters because many web tasks involve forms, maps, news, travel, education, documents, dashboards, and extraction workflows beyond shopping.

- **Additional limitation:**
  The action space is simplified.
  For web agents, `search` and `choose` actions are useful abstractions, but they hide lower-level UI complexities such as scrolling regions, modals, hidden elements, coordinate grounding, and form validation.

- **Additional limitation:**
  Automatic reward is useful but imperfect.
  For web extraction, this matters because reward functions based on attributes, options, price, and product type may not capture all semantic correctness.

- **Additional limitation:**
  Agents struggle with query reformulation, option selection, exploration, and memory.
  These are directly thesis-relevant because web data extraction also requires robust search, comparison, backtracking, and remembering visited pages.

- **Connects to:**
  World of Bits, ReAct, WebGPT, LATS, WebArena, online shopping agents, grounding benchmarks, and web-agent evaluation.

- **Use in thesis:**
  Use WebShop as the main S4 benchmark paper that bridges pre-LLM web environments and modern grounded language agents. It is also useful for showing the gap between agent performance and human web behavior.

- **BibTeX key:**
  yao2022webshop

---

## Thesis-ready paragraph

Yao et al. introduced WebShop, a scalable simulated e-commerce environment for evaluating grounded language agents on realistic web interaction tasks. Unlike earlier low-level web benchmarks, WebShop uses real product data, crowdsourced natural-language instructions, and a semantic action space consisting of search and choice actions. The agent must formulate search queries, navigate result pages, inspect products, select options, and purchase an item matching the user’s requirements. This benchmark is important for LLM-based web automation because it combines language grounding, sequential decision-making, exploration, and automatic reward computation. However, WebShop also reveals the difficulty of web interaction: the best model substantially outperforms rule-based baselines but remains far below expert human success. The paper therefore demonstrates both the promise of scalable web-agent benchmarks and the remaining need for stronger language understanding, memory, exploration, planning, and sim-to-real robustness.

---

## Why this paper matters for my thesis

This paper matters because it provides a concrete benchmark for web automation as language-guided decision-making.

A WebShop agent must solve problems similar to real web automation:

```text
understand instruction
generate search query
read noisy product text
compare products
select options
navigate pages
backtrack
decide when to buy
```

These skills are closely related to web data extraction:

```text
find relevant page
extract fields
compare candidates
verify constraints
return structured output
```

WebShop also shows an important shift:

```text
World of Bits: low-level UI control
WebShop: semantic web interaction with realistic text
```

This makes it more relevant to LLM-based agents.

However, WebShop is still not fully general because it is a simulated shopping site with controlled actions and rewards.

---

## Important concepts to remember

### 1. Grounded language agent

A grounded language agent must connect language instructions to actions in an environment.

In WebShop:

```text
instruction = user product requirement
grounding = product attributes, options, prices, page text
action = search or choose
reward = product matches instruction
```

### 2. WebShop environment

The environment includes four page types:

```text
search page
results page
item page
item-detail page
```

The agent moves between them using semantic actions.

### 3. Action space

WebShop uses high-level actions:

```text
search[query]
choose[product title]
choose[option]
choose[description/overview]
choose[previous]
choose[buy]
```

This makes the task more tractable than raw mouse/keyboard control.

### 4. Automatic reward

Reward is computed using:

```text
product type
attributes
options
price
```

This avoids constant human feedback and supports scalable RL evaluation.

### 5. Query reformulation

The paper shows that directly searching the whole instruction is often not enough.

Agents must learn to generate better search queries.

### 6. Strategic exploration

Agents must explore multiple products and sometimes backtrack.

Humans do this better than models.

### 7. Sim-to-real transfer

Agents trained on WebShop can transfer non-trivially to Amazon with minor code changes.

This is important for deployment relevance.

---

## Key evidence from the paper

### Figure 1 — WebShop environment

Figure 1 shows the full shopping trajectory:

```text
search → results → item → item-detail → option selection → buy
```

This is one of the clearest examples of a language-grounded web task.

### Dataset scale

WebShop contains:

```text
1.18M products
12,087 instructions
1,600+ human demonstrations
```

This supports scalability.

### Results

The best agent achieves:

```text
Task success: about 29%
Rule baseline: 9.6%
Human expert: 59%
```

This shows both progress and a large remaining gap.

### Ablations

The paper shows the importance of language pretraining and search generation.

Removing pretrained choice models or search-generation models reduces performance.

### Human vs agent analysis

Humans explore more items, use more searches, and remember previous products better.

This motivates memory and planning research.

### Sim-to-real transfer

The model transfers to Amazon with similar performance trends, suggesting that simulated benchmarks can help train practical agents.

---

## Connection to earlier and later papers

### Connection to World of Bits

WebShop builds on the web-as-environment idea but uses higher-level semantic actions.

```text
WoB = raw UI control
WebShop = semantic search/choose actions
```

### Connection to WebGPT

WebGPT uses browsing for question answering.

WebShop uses browsing-like interaction for e-commerce task completion.

### Connection to ReAct

ReAct later uses WebShop as an environment where reasoning-action loops can improve decisions.

### Connection to SeeAct and WebVoyager

SeeAct and WebVoyager move from simulated/e-commerce environments to broader live-web multimodal agents.

### Connection to S5

WebShop feeds benchmark design, planning, memory, exploration, training, and sim-to-real deployment.

---

## Connection to later thesis sections

- **S5.1 — Benchmarks and Evaluation:**
  WebShop is a major interactive web-agent benchmark.

- **S5.2 — Interface Representation:**
  It provides HTML mode and simple mode, showing the trade-off between realism and agent-readable state.

- **S5.3 — Planning and Exploration:**
  Query reformulation, product comparison, and backtracking are key planning challenges.

- **S5.4 — Training:**
  The paper uses imitation learning and reinforcement learning.

- **S5.5 — Failure Modes:**
  Agents fail through weak option matching, poor search, shallow exploration, and lack of memory.

- **S8 — Deployment:**
  Sim-to-real transfer to Amazon connects benchmark research to real-world web automation.

---

## Limitation connected to thesis

WebShop is a strong benchmark, but it does not fully solve generalized web automation.

For my thesis, generalized web automation requires:

```text
multi-domain tasks
live website interaction
DOM and visual grounding
safe browser actions
structured data extraction
verification
robust recovery
privacy and deployment constraints
```

WebShop mainly addresses:

```text
e-commerce search and purchase simulation
language grounding
automatic reward
semantic action selection
```

It does not fully cover:

- arbitrary websites,
- real-time dynamic interfaces,
- authentication,
- visual grounding,
- extraction-specific tasks,
- irreversible action safety,
- or cross-domain workflows.

Therefore, WebShop should be used as a cornerstone benchmark showing scalable grounded web interaction, but not as a complete representation of generalized web automation.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Very high
- **Main use:** Core benchmark for grounded web interaction
- **Most important parts:**
  - Abstract
  - Figure 1
  - Task formulation
  - Environment implementation
  - Reward definition
  - Research challenges
  - Model architecture
  - Results and ablations
  - Human vs agent analysis
  - Sim-to-real transfer
  - Limitations and societal impact

---

## One-sentence summary

WebShop provides a scalable e-commerce benchmark for grounded language agents, showing that semantic web interaction is possible but still far below human performance due to search, option selection, exploration, and memory limitations.

---

## BibTeX

```bibtex
@inproceedings{yao2022webshop,
  title     = {WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents},
  author    = {Yao, Shunyu and Chen, Howard and Yang, John and Narasimhan, Karthik},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {35},
  year      = {2022},
  doi       = {10.52202/068431-1508},
  eprint    = {2207.01206},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2207.01206
- NeurIPS: https://proceedings.neurips.cc/paper_files/paper/2022/hash/82ad13ec01f9fe44c01cb91814fd7b8c-Abstract-Conference.html
- Project: https://webshop-pnlp.github.io


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P0\2024-03 - SeeAct- GPT-4V__ision__ is a Generalist Web Agent if Grounded.md

# Paper 284 — GPT-4V(ision) is a Generalist Web Agent, if Grounded

## Metadata

- **Title:** GPT-4V(ision) is a Generalist Web Agent, if Grounded
- **System name:** SeeAct
- **Authors:** Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su
- **Year:** 2024
- **Venue:** International Conference on Machine Learning (ICML 2024)
- **DOI:** 10.48550/arXiv.2401.01614
- **arXiv ID:** arXiv:2401.01614
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 — Offline vs Online Evaluation; S5.2 — Visual/HTML Grounding; S5.3 — Web Planning; S5.5 — Failure Modes; S7 — Safety; S8 — Deployment Realities
- **Category:** WEB-F / MULTIMODAL WEB AGENT / GROUNDING
- **Paper type:** System / evaluation / grounding study
- **Priority:** P0
- **BibTeX key:** zheng2024gpt4v

---

## Simple understanding

This paper introduces **SeeAct**, a generalist web agent based on GPT-4V.

The central message is in the title:

```text
GPT-4V can be a generalist web agent if grounding is solved.
```

The paper separates web-agent ability into two parts:

```text
1. Action generation:
   deciding what should be done next in natural language

2. Action grounding:
   converting that plan into an executable browser action
   by selecting the correct HTML element, operation, and value
```

The paper finds that GPT-4V is strong at understanding rendered webpages and generating reasonable action descriptions. However, the hard part is grounding those descriptions into precise UI elements.

For my thesis, SeeAct is extremely important because it identifies **grounding** as a major bottleneck for multimodal web agents.

---

## Notes

- **Core idea:**
  Proposes SeeAct, a GPT-4V-based web agent that uses visual webpage understanding for action generation and studies methods for grounding textual action descriptions into executable browser actions.

- **Key finding:**
  With oracle grounding, GPT-4V can complete 51.1% of live web tasks, far outperforming GPT-4 and FLAN-T5 baselines. However, automatic grounding remains far below oracle grounding, showing that element grounding is the main bottleneck.

- **Limitation:**
  Grounding remains the major unsolved problem.
  For web agents, this matters directly because a correct high-level plan is useless if the agent clicks the wrong element, types into the wrong field, or selects the wrong dropdown.

- **Additional limitation:**
  Set-of-mark/image annotation is not sufficient for complex webpages.
  For S5.2, this matters because web screenshots contain many dense elements and rich spatial relations; object-centric visual grounding methods do not transfer cleanly.

- **Additional limitation:**
  SeeAct uses a two-stage action-generation/action-grounding pipeline.
  For deployment, this matters because each stage can fail independently, and errors cascade across long tasks.

- **Additional limitation:**
  Offline evaluation underestimates or misrepresents true performance.
  For web agents, this matters because one task may have multiple valid action paths, but offline datasets usually contain only one reference trajectory.

- **Additional limitation:**
  The paper uses human monitoring for online evaluation to avoid harmful actions.
  For generalized deployment, this matters because web agents can affect real-world states, accounts, transactions, forms, and user data.

- **Connects to:**
  Mind2Web, WebVoyager, WebArena, GPT-4V, LLaVA, CogAgent, visual grounding, DOM grounding, Set-of-Mark prompting, and multimodal web agents.

- **Use in thesis:**
  Use SeeAct as the key S4 paper showing that multimodal LLMs have strong web-agent potential, but grounding is the central barrier.

- **BibTeX key:**
  zheng2024gpt4v

---

## Thesis-ready paragraph

Zheng et al. introduced SeeAct, a GPT-4V-based generalist web agent that investigates whether large multimodal models can act on arbitrary websites. The paper decomposes web-agent behavior into action generation, where the model describes the next step in natural language, and action grounding, where that description is converted into an executable browser action by selecting the correct webpage element and operation. The results show that GPT-4V has strong potential as a web agent when oracle grounding is available: it reaches 51.1% task success in online evaluation. However, automatic grounding methods remain substantially below oracle grounding, revealing that precise element grounding is the main bottleneck. For this thesis, SeeAct is central because it identifies the gap between multimodal understanding and reliable browser control. Generalized web automation requires not only strong visual reasoning, but also robust HTML/visual grounding, online evaluation, safety monitoring, and error recovery.

---

## Why this paper matters for my thesis

This paper matters because it explains a key problem in modern web agents:

```text
The model may know what to do,
but still fail to do it on the actual page.
```

Example:

```text
Plan:
Click the “Find Your Truck” button.

Grounding problem:
Which exact HTML element is that?
Which operation should be used?
Is the element visible?
Is there another similar button?
Should the action be CLICK, TYPE, or SELECT?
```

This is directly connected to generalized web automation.

The thesis needs this distinction:

```text
reasoning/planning ≠ grounding/execution
```

An LMM can generate a good plan, but web automation succeeds only if the plan is grounded into:

```text
correct DOM element
correct visual location
correct operation
correct input value
safe execution
```

SeeAct is therefore a key bridge from S4 to S5.2.

---

## Important concepts to remember

### 1. Generalist web agent

A generalist web agent should follow natural-language instructions on arbitrary websites.

It must generalize across:

```text
tasks
websites
domains
layouts
interaction patterns
```

### 2. Action generation

Action generation means producing the intended next action in natural language.

Example:

```text
Click the button labeled “Find Your Truck.”
```

### 3. Action grounding

Action grounding means converting the textual action into an executable browser event:

```text
element = specific HTML node
operation = CLICK / TYPE / SELECT
value = input text if needed
```

### 4. Element grounding

Element grounding is the hardest part of action grounding.

The agent must identify the exact target element among many possible elements.

### 5. Grounding strategies

The paper studies:

```text
element attributes
textual choices
image annotation
oracle grounding
```

### 6. Oracle grounding

Oracle grounding uses human annotation to identify the intended action.

It estimates the upper bound of GPT-4V’s action-generation ability.

### 7. Online vs offline evaluation

Offline evaluation checks against cached reference trajectories.

Online evaluation tests the agent on live websites.

The paper shows that online evaluation may be more realistic because multiple valid plans can solve the same task.

---

## Key evidence from the paper

### Figure 1 — SeeAct overview

Figure 1 shows GPT-4V generating a textual action description and then grounding it into an HTML element and operation.

This figure is central for explaining the generation-grounding divide.

### Figure 2 — Element grounding methods

Figure 2 compares:

```text
element attributes
textual choices
image annotation
```

This is directly useful for S5.2.

### Table 2 — Offline evaluation

GPT-4V with oracle grounding achieves much higher step success than other models, especially cross-website and cross-domain.

This shows GPT-4V’s generalist potential.

### Table 3 — Grounding comparison

Step success rates show a large gap between automatic grounding and oracle grounding:

```text
SEEACTChoice: around 32–42%
SEEACTOracle: around 62–65%
```

This proves that grounding is the bottleneck.

### Table 4 — Online task success

Online success rates:

```text
FLAN-T5-XL: 8.9%
GPT-4: 13.3%
SEEACTChoice: 37.8%
SEEACTOracle: 51.1%
```

This demonstrates the strong potential of GPT-4V if grounding improves.

### Error analysis

The paper shows that image annotation can cause hallucinated bounding boxes or label confusion.

This is important because visual prompting alone is not enough for web grounding.

### Impact statement

The paper warns about privacy, sensitive operations, financial transactions, application forms, and harmful actions.

This is important for S7/S8.

---

## Connection to earlier and later papers

### Connection to WebGPT

WebGPT uses text browsing.

SeeAct uses rendered screenshots and GPT-4V.

```text
WebGPT = text browser
SeeAct = multimodal visual web agent
```

### Connection to WebShop

WebShop studies grounded e-commerce interaction in simulation.

SeeAct studies generalist web action on real/cached websites with multimodal models.

### Connection to WebVoyager

SeeAct identifies grounding as the bottleneck.

WebVoyager proposes an end-to-end screenshot + element-labeling live-web agent.

### Connection to Mind2Web

SeeAct evaluates on Mind2Web and Multimodal-Mind2Web.

### Connection to S5.2

SeeAct is one of the most important grounding papers for web agents.

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  SeeAct compares offline and online evaluation.

- **S5.2 — Perception and Grounding:**
  This is the strongest cross-link: the paper’s main claim is that grounding is the bottleneck.

- **S5.3 — Planning:**
  GPT-4V shows planning ability, speculative reasoning, and error correction awareness.

- **S5.5 — Failure Modes:**
  Grounding errors, label hallucination, and cascading failures are central.

- **S7 — Safety:**
  Live-web actions require human monitoring and risk control.

- **S8 — Deployment:**
  Generalist web agents must handle live websites and avoid harmful actions.

---

## Limitation connected to thesis

SeeAct shows strong multimodal planning, but not solved generalized automation.

For my thesis, the full problem is:

```text
instruction → multimodal observation → plan → grounded element selection → browser action → feedback → verification → safe completion
```

SeeAct mainly studies:

```text
action generation
+ action grounding
```

It does not fully solve:

- long-horizon planning,
- robust memory,
- structured data extraction,
- cost-aware browsing,
- authentication,
- CAPTCHA,
- irreversible action safety,
- or fully reliable automatic grounding.

Therefore, SeeAct should be used as the key S4 paper showing that web-agent success depends on grounding, not only LMM capability.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Very high
- **Main use:** Core multimodal web-agent grounding paper
- **Most important parts:**
  - Abstract
  - Figure 1
  - Section 2.1 formulation
  - Section 2.2 action generation
  - Section 2.3 action grounding
  - Figure 2
  - Table 2
  - Table 3
  - Table 4
  - Online evaluation
  - Error analysis
  - Impact statement

---

## One-sentence summary

SeeAct shows that GPT-4V has strong potential as a generalist web agent, but the major bottleneck is grounding natural-language action plans into precise executable browser actions.

---

## BibTeX

```bibtex
@inproceedings{zheng2024gpt4v,
  title     = {GPT-4V(ision) is a Generalist Web Agent, if Grounded},
  author    = {Zheng, Boyuan and Gou, Boyu and Kil, Jihyung and Sun, Huan and Su, Yu},
  booktitle = {International Conference on Machine Learning},
  year      = {2024},
  eprint    = {2401.01614},
  archivePrefix = {arXiv},
  primaryClass = {cs.IR},
  doi       = {10.48550/arXiv.2401.01614},
  url       = {https://github.com/OSU-NLP-Group/SeeAct}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2401.01614
- Project: https://osu-nlp-group.github.io/SeeAct/
- GitHub: https://github.com/OSU-NLP-Group/SeeAct


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P0\2024-06 - - WebVoyager- Building an End-to-End Web Agent with.md

# Paper 283 — WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models

## Metadata

- **Title:** WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models
- **Authors:** Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, Yong Dai, Hongming Zhang, Zhenzhong Lan, Dong Yu
- **Year:** 2024
- **Venue:** Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL 2024), Long Papers
- **Pages:** 6864–6890
- **DOI:** 10.18653/v1/2024.acl-long.371
- **arXiv DOI:** 10.48550/arXiv.2401.13919
- **arXiv ID:** arXiv:2401.13919
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 — Online Evaluation; S5.2 — Multimodal Web Perception; S5.3 — End-to-End Planning; S5.5 — Failure Modes; S7 — Safety and Evaluation Trust; S8 — Deployment Realities
- **Category:** WEB-F / MULTIMODAL WEB AGENT / LIVE WEB
- **Paper type:** System / benchmark / online end-to-end web agent
- **Priority:** P0
- **BibTeX key:** he2024webvoyager

---

## Simple understanding

This paper introduces **WebVoyager**, an end-to-end multimodal web agent that operates on real websites.

The main idea is:

```text
user task
→ screenshot + interactive element text
→ LMM reasoning
→ action
→ browser execution
→ new screenshot
→ repeat until answer
```

WebVoyager uses screenshots as the main observation because webpages are designed visually for humans. It also overlays numerical labels on interactive elements, so the model can refer to clickable or typable targets.

The paper introduces:

```text
a live-web agent
a benchmark of 643 tasks across 15 websites
an automatic evaluator using GPT-4V
human validation of evaluator agreement
```

For my thesis, WebVoyager is crucial because it represents the modern multimodal web-agent paradigm: an LMM observes real websites, reasons step by step, executes browser actions, and returns final answers.

---

## Notes

- **Core idea:**
  Builds an end-to-end multimodal web agent that uses screenshots plus interactive element text to complete user instructions on live real-world websites.

- **Key finding:**
  WebVoyager achieves 59.1% task success on its benchmark, outperforming GPT-4 All Tools at 30.8% and a text-only WebVoyager baseline at 40.1%. Its GPT-4V-based automatic evaluation reaches 85.3% agreement with human judgment.

- **Limitation:**
  WebVoyager still depends on element labeling and visual grounding quality.
  For web agents, this matters because wrong labels, dense interfaces, small text, or visually ambiguous elements can lead to wrong actions.

- **Additional limitation:**
  WebVoyager uses a maximum step budget and can get stuck.
  For generalized web automation, this matters because long-horizon tasks may require more than fixed-step interaction and better recovery from navigation loops.

- **Additional limitation:**
  The benchmark avoids login and CAPTCHA tasks.
  For deployment, this matters because many practical web automation tasks require accounts, authentication, permissions, and anti-bot constraints.

- **Additional limitation:**
  Automatic evaluation with GPT-4V is promising but not perfect.
  For web agents, this matters because evaluator bias, trajectory ambiguity, and open-ended answers can affect reported success.

- **Additional limitation:**
  Text-heavy websites remain difficult.
  For web extraction, this matters because many information-heavy pages require reliable text extraction from HTML, not only screenshot-based reasoning.

- **Connects to:**
  SeeAct, WebGPT, WebShop, ReAct, Set-of-Mark prompting, WebArena, VisualWebArena, BrowserGym, multimodal web agents, and online evaluation.

- **Use in thesis:**
  Use WebVoyager as the key S4 modern live-web system showing end-to-end multimodal web automation on real websites.

- **BibTeX key:**
  he2024webvoyager

---

## Thesis-ready paragraph

He et al. introduced WebVoyager, an end-to-end multimodal web agent that completes user instructions by interacting directly with real-world websites. Unlike earlier text-only or simulated web agents, WebVoyager uses rendered screenshots as a primary observation channel and augments them with labeled interactive elements and textual metadata. At each step, the agent reasons over the current observation, generates an action such as clicking, typing, scrolling, waiting, going back, or answering, and executes it in a live browser. The paper also introduces a benchmark of 643 tasks across 15 popular websites and an automatic trajectory-evaluation protocol using GPT-4V, validated against human judgments. WebVoyager is important for this thesis because it demonstrates a modern multimodal paradigm for web automation: LMMs can operate directly on live web interfaces. However, its failures show that generalized web automation still requires stronger visual grounding, loop avoidance, text extraction, robust planning, authentication handling, and reliable evaluation.

---

## Why this paper matters for my thesis

This paper matters because it shows the shift from controlled/simulated web environments to real online websites.

The S4 progression becomes:

```text
World of Bits → web as environment
WebGPT → LLM with text browser
WebShop → scalable simulated e-commerce interaction
SeeAct → GPT-4V potential if grounded
WebVoyager → end-to-end LMM web agent on live websites
```

For my thesis, WebVoyager is important because it operationalizes many components of a generalized web agent:

```text
screenshots
interactive element labels
text metadata
ReAct-style thought/action loop
browser execution
online task success
automatic evaluation
```

It is closer to real web automation than WebGPT or WebShop.

However, it still shows major open problems:

```text
navigation stuck
visual grounding errors
hallucination
prompt misalignment
dense text handling
long trajectories
safety for real websites
```

These gaps can feed directly into S5.2, S5.3, S5.5, and S8.

---

## Important concepts to remember

### 1. End-to-end web agent

WebVoyager performs the full loop:

```text
observe → think → act → observe → answer
```

without intermediate human intervention.

### 2. Screenshot-first observation

The agent uses webpage screenshots as the main input.

This follows the idea that websites are designed visually for humans.

### 3. Interactive element labels

WebVoyager overlays numerical labels on interactive elements.

The model can then choose actions like:

```text
Click [10]
Type [17]: query text
Scroll
Back
Answer
```

### 4. Auxiliary text

The agent also receives element type and text content.

This helps when screenshots alone are insufficient.

### 5. ReAct-style prompting

The model generates a thought before the action.

This connects S3 agent architecture to S4 web agents.

### 6. Online evaluation

WebVoyager evaluates agents on live websites, not only cached pages or offline trajectories.

### 7. GPT-4V evaluator

The paper uses GPT-4V to evaluate full trajectories and final answers, achieving high agreement with human judgments.

### 8. Failure categories

The paper identifies major failure reasons:

```text
navigation stuck
visual grounding issue
hallucination
prompt misalignment
```

These are useful for S5.5.

---

## Key evidence from the paper

### Figure 1 — WebVoyager workflow

Figure 1 shows the overall loop:

```text
user query → observation → thought → action → browser → answer
```

This is directly aligned with the thesis architecture.

### Figure 2 — Marked screenshots

Figure 2 shows how interactive elements are labeled on screenshots.

This is important for S5.2 grounding.

### Benchmark scale

The paper creates:

```text
643 tasks
15 websites
GAIA web tasks
SeeAct online tasks
```

This supports broader evaluation than a single website or domain.

### Main results

WebVoyager achieves:

```text
59.1% success overall
GPT-4 All Tools: 30.8%
Text-only baseline: 40.1%
```

This shows the value of multimodal web interaction.

### Evaluator result

GPT-4V automatic evaluation achieves:

```text
85.3% agreement with human judgment
κ = 0.70
```

This is important for scalable evaluation.

### Error analysis

Major failure categories include:

```text
Navigation Stuck: 44.4%
Visual Grounding Issue: 24.8%
Hallucination: 21.8%
Prompt Misalignment: 9.0%
```

This is directly useful for S5.5.

---

## Connection to earlier and later papers

### Connection to WebGPT

WebGPT uses a text browser for QA.

WebVoyager uses screenshots and live browser interaction for broader web tasks.

```text
WebGPT = text browsing + references
WebVoyager = multimodal live browsing + end-to-end task completion
```

### Connection to WebShop

WebShop is simulated and e-commerce-specific.

WebVoyager works on 15 real websites.

### Connection to SeeAct

SeeAct focuses on whether GPT-4V can be a generalist web agent if grounding is solved.

WebVoyager builds a practical end-to-end multimodal agent with marked screenshots.

### Connection to ReAct

WebVoyager uses the ReAct-style thought-action loop in a real browser environment.

### Connection to S5

WebVoyager contributes to:

```text
S5.1 online evaluation
S5.2 visual grounding
S5.3 planning
S5.5 failure modes
S8 deployment
```

---

## Connection to later thesis sections

- **S5.1 — Benchmarks and Evaluation:**
  WebVoyager introduces an online benchmark and GPT-4V-based evaluation.

- **S5.2 — Perception and Grounding:**
  It uses screenshots, element labels, and auxiliary element text.

- **S5.3 — Planning and Decision-Making:**
  The agent performs step-by-step online navigation.

- **S5.5 — Failure Modes:**
  The paper provides a clear failure taxonomy.

- **S7 — Trustworthiness:**
  Automatic evaluation and live-web safety require careful validation.

- **S8 — Deployment:**
  It surfaces practical issues: CAPTCHAs, login omission, popups, dynamic pages, and cost.

---

## Limitation connected to thesis

WebVoyager is close to generalized web automation, but it is not complete.

For my thesis, the remaining challenges are:

```text
robust visual grounding
long-horizon recovery
safe login/account interaction
CAPTCHA and website policy constraints
structured extraction verification
dense text handling
state memory beyond clipped context
privacy and irreversible action safety
```

WebVoyager mainly demonstrates:

```text
multimodal live-web task completion
```

but does not fully solve:

- secure actions,
- task-specific verification,
- robust extraction,
- multi-session memory,
- error recovery after wrong actions,
- or deployment at scale.

Therefore, WebVoyager should be used as a major modern S4 system and a bridge into S5’s technical challenges.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Very high
- **Main use:** Modern end-to-end live multimodal web-agent system
- **Most important parts:**
  - Abstract
  - Figure 1
  - Figure 2
  - Interaction formulation
  - Observation/action space
  - Benchmark construction
  - Evaluation protocol
  - Main results
  - GPT-4V evaluator agreement
  - Error analysis
  - Discussion and limitations

---

## One-sentence summary

WebVoyager demonstrates that large multimodal models can complete many live-web tasks end-to-end using screenshots and labeled elements, but failures in grounding, navigation, hallucination, and prompt alignment remain central barriers to reliable generalized web automation.

---

## BibTeX

```bibtex
@inproceedings{he2024webvoyager,
  title     = {WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models},
  author    = {He, Hongliang and Yao, Wenlin and Ma, Kaixin and Yu, Wenhao and Dai, Yong and Zhang, Hongming and Lan, Zhenzhong and Yu, Dong},
  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages     = {6864--6890},
  year      = {2024},
  publisher = {Association for Computational Linguistics},
  doi       = {10.18653/v1/2024.acl-long.371},
  url       = {https://aclanthology.org/2024.acl-long.371/}
}
```

---

## Source links

- ACL Anthology: https://aclanthology.org/2024.acl-long.371/
- arXiv: https://arxiv.org/abs/2401.13919
- GitHub: https://github.com/MinorJerry/WebVoyager


---

## P1 (33 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2018-02 - Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration.md

# Paper 285 — Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration

## Metadata

- **Title:** Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration
- **Authors:** Evan Zheran Liu, Kelvin Guu, Panupong Pasupat, Tianlin Shi, Percy Liang
- **Year:** 2018
- **Venue:** International Conference on Learning Representations (ICLR 2018), conference paper
- **DOI:** 10.48550/arXiv.1802.08802
- **arXiv ID:** arXiv:1802.08802
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 benchmarks; S5.2 interface representation; S5.3 exploration/planning; S5.4 demonstrations/RL; S5.5 sparse-reward failure modes
- **Category:** WEB-RL / WORKFLOW-GUIDED EXPLORATION / MINIWOB
- **Paper type:** Method / RL training strategy for web interfaces
- **Priority:** P1
- **BibTeX key:** liu2018reinforcement
- **Final publication status:** Final venue verified: ICLR 2018 conference paper.
- **Verification source:** https://openreview.net/forum?id=ryTp3f-0-

---

## Simple understanding

This paper is a pre-LLM web-agent paper that tries to solve a key problem in browser automation: **sparse reward exploration**.

In many web tasks, the agent only receives reward after completing the whole task. For example, if the goal is to fill a form and submit it, the agent may need many correct clicks and typed values before seeing any success signal. Random exploration is therefore very inefficient.

The paper proposes **Workflow-Guided Exploration (WGE)**. Instead of directly cloning expert demonstrations, the method extracts abstract workflows from demonstrations. A workflow is a high-level action pattern such as:

```text
click textbox → type value → click submit
```

The RL agent then explores within this workflow structure. This reduces the search space while still allowing the agent to discover successful concrete actions.

For my thesis, the paper matters because it shows an early solution to the same problem that later LLM web agents face: how to avoid blind exploration in a huge web-action space. Later systems use language plans, ReAct traces, memory, and tool abstractions for similar reasons.

---

## Notes

- **Core idea:**
  Use expert demonstrations to infer abstract workflows that constrain reinforcement-learning exploration on web interfaces.

- **Key finding:**
  Workflow-guided exploration improves sample efficiency over behavioral cloning and achieves strong results on MiniWoB-style web tasks using only a small number of demonstrations per task.

- **Limitation:**
  The method still requires expert demonstrations. For generalized web automation, this matters because demonstrations cannot realistically be collected for every website, workflow, and extraction schema.

- **Additional limitation:**
  The workflows are derived from previous trajectories, so they may not generalize to unseen layouts or new task structures. For web agents, this motivates LLM-based reasoning and planning rather than relying only on fixed workflow templates.

- **Additional limitation:**
  The approach remains RL-based and has limited natural-language reasoning. For the thesis, this explains why pre-LLM web agents struggled with open-ended user instructions.

- **Additional limitation:**
  Grounding remains difficult: the agent still has to map abstract steps to concrete elements, clicks, and typed values.

- **Connects to:**
  World of Bits, DOM-Q-NET, MiniWoB, imitation learning, RL for web interfaces, AutoWebGLM, and training-based web agents.

- **Use in thesis:**
  Use this paper to show that demonstration-guided exploration was an important pre-LLM strategy for web automation, and that sparse reward remains a core challenge.

---

## Thesis-ready paragraph

Liu et al. proposed Workflow-Guided Exploration, a reinforcement-learning method for web-interface agents that uses expert demonstrations to constrain exploration without forcing exact imitation. From each demonstration, the method induces abstract workflows that define plausible classes of actions, then trains an agent to explore within this reduced action space. This is important for the evolution of web agents because it shows that web automation is difficult not only because of perception, but also because of sparse rewards and large action spaces. For LLM-based web automation, WGE is an early precursor to later planning and demonstration-based approaches: it uses human demonstrations to guide search, while later LLM agents use language reasoning, trajectories, and memory to guide action selection. However, WGE remains limited by demonstration dependence, low-level action grounding, and weak generalization to arbitrary real websites.

---

## Why this paper matters for my thesis

This paper matters because web automation often fails when the agent explores blindly.

A website may require:

```text
click the correct field
type the correct value
select the correct option
click submit
wait for response
verify success
```

If the reward appears only after the final step, random RL rarely succeeds. WGE shows that demonstrations can provide structure:

```text
demonstration → abstract workflow → guided exploration → successful trajectories
```

For the thesis, this is useful because modern LLM web agents still need guidance. The guidance may come from prompts, demonstrations, memories, self-reflections, learned policies, or tools, but the underlying reason is the same: web action spaces are too large for unguided exploration.

---

## Important concepts to remember

### 1. Workflow

An abstract pattern of action types derived from demonstrations.

### 2. Workflow lattice

A compact representation of possible workflows consistent with a demonstration.

### 3. Workflow-guided exploration

RL exploration constrained to actions allowed by an inferred workflow.

### 4. Behavioral cloning

Supervised imitation of human demonstrations.

### 5. Sparse reward

A reward signal that appears only after the whole task succeeds.

### 6. MiniWoB

A benchmark suite of small web tasks introduced in the World of Bits ecosystem.

---

## Key evidence from the paper

### WGE pipeline

The paper presents a pipeline where demonstrations generate workflow lattices, RL explores within them, successful trajectories are stored, and a policy is trained from successful episodes.

### Sample efficiency

The paper emphasizes that WGE improves sample efficiency compared with standard behavioral cloning and unguided RL.

### MiniWoB results

The method is evaluated on web-interface tasks from the MiniWoB setting, connecting directly to the early web-agent benchmark line.

### Thesis-relevant result

The key evidence is not only the numerical improvement, but the diagnosis: web tasks need structured exploration because sparse rewards and low-level actions are hard.

---

## Connection to earlier and later papers

### Connection to World of Bits

World of Bits introduces the web as an environment for agents.

WGE improves the training strategy inside this kind of environment by using demonstrations to guide exploration.

```text
World of Bits = environment
WGE = better exploration method for that environment
```

### Connection to DOM-Q-NET

DOM-Q-NET focuses on DOM representation.

WGE focuses on exploration.

Together, they show two pre-LLM needs:

```text
represent the page well
explore the action space efficiently
```

### Connection to LLM web agents

LLM agents later reduce exploration difficulty through:

```text
language reasoning
task decomposition
tool calls
memory
self-reflection
structured prompts
```

WGE is an early non-LLM version of that idea.

---

## Connection to later thesis sections

- **S5.1 — Benchmarks and Evaluation:**
  MiniWoB and early task success metrics.
- **S5.3 — Planning and Decision-Making:**
  Workflow constraints as an early planning/exploration mechanism.
- **S5.4 — Training Strategies:**
  Demonstrations, behavioral cloning, and reinforcement learning.
- **S5.5 — Failure Modes:**
  Sparse reward, overfitting to demonstrations, and exploration failure.

---

## Limitation connected to thesis

Workflow-Guided Exploration improves RL training, but it does not solve generalized web automation.

For my thesis, the full web-agent loop is:

```text
instruction → page observation → grounding → planning → action → feedback → recovery → extraction → verification
```

WGE mainly improves:

```text
demonstration → workflow → exploration
```

It does not fully solve:

- natural-language instruction understanding,
- generalization to unseen sites,
- robust DOM/visual grounding,
- dynamic website behavior,
- structured data extraction,
- or safe autonomous execution.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Introduction
  - Workflow definition
  - Workflow-guided exploration algorithm
  - MiniWoB experiments
  - Comparison with behavioral cloning
  - Limitations

---

## One-sentence summary

Workflow-Guided Exploration shows that demonstrations can guide sparse-reward web RL, but generalized web automation still needs language reasoning, robust grounding, and cross-site generalization.

---

## BibTeX

```bibtex
@inproceedings{liu2018reinforcement,
  title     = {Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration},
  author    = {Liu, Evan Zheran and Guu, Kelvin and Pasupat, Panupong and Shi, Tianlin and Liang, Percy},
  booktitle = {International Conference on Learning Representations},
  year      = {2018},
  eprint    = {1802.08802},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  doi       = {10.48550/arXiv.1802.08802},
  url       = {https://openreview.net/forum?id=ryTp3f-0-}
}
```

---

## Source links

- https://arxiv.org/abs/1802.08802


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2019-02 - DOM-Q-NET- Grounded RL on Structured Language.md

# Paper 286 — DOM-Q-NET: Grounded RL on Structured Language

## Metadata

- **Title:** DOM-Q-NET: Grounded RL on Structured Language
- **Authors:** Sheng Jia, Jamie Kiros, Jimmy Ba
- **Year:** 2019
- **Venue:** International Conference on Learning Representations (ICLR 2019), conference paper
- **DOI:** 10.48550/arXiv.1902.07257
- **arXiv ID:** arXiv:1902.07257
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 MiniWoB evaluation; S5.2 DOM representation; S5.4 RL/multitask learning; S5.5 large variable action-space failure
- **Category:** WEB-RL / DOM REPRESENTATION / GRAPH NEURAL NETWORK
- **Paper type:** Method / RL architecture
- **Priority:** P1
- **BibTeX key:** jia2019domqnet
- **Final publication status:** Final venue verified: ICLR 2019 conference paper.
- **Verification source:** https://openreview.net/forum?id=HJgd1nAqFX

---

## Simple understanding

This paper introduces **DOM-Q-NET**, a reinforcement-learning architecture for web navigation.

The central idea is that a webpage should not be represented only as pixels or flat text. A webpage has structure: the HTML document is a **DOM tree**. Buttons, inputs, labels, tables, links, and containers are arranged in a hierarchy.

DOM-Q-NET uses a graph neural network to represent this DOM structure. It then learns Q-values for different types of actions, such as clicking and typing.

For my thesis, the paper matters because DOM representation is still one of the central problems in LLM web agents. Even modern agents must decide which DOM element corresponds to a user instruction or visual target.

---

## Notes

- **Core idea:**
  Represent the webpage as a DOM graph and use graph neural networks with factorized Q-functions to learn grounded web actions.

- **Key finding:**
  DOM-Q-NET performs competitively on MiniWoB tasks without expert demonstrations and improves sample efficiency in multi-task training.

- **Limitation:**
  The evaluation is mainly on MiniWoB-like tasks, which are much simpler than live websites.

- **Additional limitation:**
  The model lacks LLM-style natural-language reasoning and cannot flexibly interpret complex user instructions.

- **Additional limitation:**
  DOM structure helps but does not solve visual layout grounding; many real websites require both DOM and screenshot understanding.

- **Additional limitation:**
  The action space remains restricted compared with arbitrary browser operations.

- **Connects to:**
  World of Bits, WGE, HTML-T5, WebAgent, AutoWebGLM, Mind2Web, and modern DOM-aware LLM agents.

- **Use in thesis:**
  Use as a key pre-LLM DOM grounding paper showing why structured page representation is essential.

---

## Thesis-ready paragraph

Jia et al. introduced DOM-Q-NET, a reinforcement-learning architecture for web navigation that explicitly represents webpages through their DOM structure. By using graph neural networks over DOM nodes and factorizing Q-functions over action categories, DOM-Q-NET addresses the variable and structured action space of web interfaces. This paper is important for the evolution of web agents because it establishes the DOM as a central representation for grounding actions. Although the method predates LLM agents and is evaluated on simplified MiniWoB tasks, the problem it addresses remains fundamental: a web agent must map instructions and decisions to concrete webpage elements. Its limitations motivate later HTML-aware, multimodal, and LLM-based web agents that combine structural DOM representations with language reasoning and visual grounding.

---

## Why this paper matters for my thesis

This paper matters because a web agent needs to know **where to act**.

A webpage is not a simple text document. It contains:

```text
buttons
forms
links
tables
dropdowns
hidden elements
nested containers
labels
attributes
```

The DOM gives the agent structure.

For example, if the instruction is:

```text
Click the search button.
```

the agent must identify the right DOM node among many possible clickable elements.

DOM-Q-NET is an early attempt to solve this with deep RL and graph neural networks. Modern LLM agents often use different models, but they still face the same grounding problem.

---

## Important concepts to remember

### 1. DOM tree

The browser's structured representation of the HTML document.

### 2. Grounded RL

RL where actions correspond to actual interface elements.

### 3. Graph neural network

A neural network that propagates information across linked DOM nodes.

### 4. Factorized Q-function

A Q-value design split across action categories.

### 5. Variable action space

The set of possible actions changes depending on the webpage state.

### 6. Multi-task training

Training across several web tasks to improve generalization.

---

## Key evidence from the paper

### Motivation

The paper highlights that web navigation has large discrete action spaces and a changing number of valid actions.

### DOM representation

The model uses DOM graph structure instead of treating the page only as pixels.

### MiniWoB evaluation

It evaluates on MiniWoB tasks, linking it to the World of Bits benchmark line.

### Sample efficiency

The paper reports improved sample efficiency in multi-task settings.

---

## Connection to earlier and later papers

### Connection to World of Bits

World of Bits introduced pixel + DOM observations.

DOM-Q-NET makes DOM structure the central modeling object.

### Connection to WebAgent and AutoWebGLM

WebAgent and AutoWebGLM later continue the DOM/HTML representation line, but with LLMs and HTML simplification.

```text
DOM-Q-NET: DOM graph + RL
WebAgent: long HTML + HTML-T5 + program synthesis
AutoWebGLM: simplified HTML + trained LLM policy
```

### Connection to SeeAct and WebVoyager

SeeAct and WebVoyager show that DOM alone is not enough. Visual screenshots and element labels are also important.

---

## Connection to later thesis sections

- **S5.2 — Perception and Grounding:**
  DOM representation and element selection.
- **S5.4 — Training Strategies:**
  RL and multi-task learning on web tasks.
- **S5.5 — Failure Modes:**
  Large variable action spaces and incorrect element grounding.
- **S8 — Deployment:**
  Gap between simplified DOM benchmarks and live websites.

---

## Limitation connected to thesis

DOM-Q-NET improves structured web representation, but it does not solve generalized web automation.

It mainly improves:

```text
webpage representation → DOM-based action selection
```

It does not solve:

- complex natural-language instructions,
- live dynamic websites,
- visual layout understanding,
- long-horizon planning,
- structured extraction verification,
- or safe web action execution.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Medium-high
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Problem formulation
  - DOM graph representation
  - Action factorization
  - MiniWoB experiments
  - Multi-task results
  - Limitations

---

## One-sentence summary

DOM-Q-NET shows that DOM structure is a useful inductive bias for web agents, but RL on simplified DOM tasks is not sufficient for generalized web automation.

---

## BibTeX

```bibtex
@inproceedings{jia2019domqnet,
  title     = {DOM-Q-NET: Grounded RL on Structured Language},
  author    = {Jia, Sheng and Kiros, Jamie and Ba, Jimmy},
  booktitle = {International Conference on Learning Representations},
  year      = {2019},
  eprint    = {1902.07257},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  doi       = {10.48550/arXiv.1902.07257},
  url       = {https://openreview.net/forum?id=HJgd1nAqFX}
}
```

---

## Source links

- https://arxiv.org/abs/1902.07257


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2023-07 - A Real-World WebAgent with Planning Long Context Understanding and Program Synthesis.md

# Paper 287 — A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis

## Metadata

- **Title:** A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis
- **Authors:** Izzeddin Gur, Hiroki Furuta, Austin Huang, Mustafa Safdari, Yutaka Matsuo, Douglas Eck, Aleksandra Faust
- **Year:** 2024
- **Venue:** International Conference on Learning Representations (ICLR 2024), conference paper
- **DOI:** 10.48550/arXiv.2307.12856
- **arXiv ID:** arXiv:2307.12856
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.2 long HTML/interface representation; S5.3 planning; S5.4 self-experience training; S6 extraction/program synthesis; S8 real-web deployment
- **Category:** WEB-LLM / REAL-WORLD WEB AGENT / HTML-T5 / PROGRAM SYNTHESIS
- **Paper type:** System / modular LLM web agent
- **Priority:** P1
- **BibTeX key:** gur2024realworld
- **Final publication status:** Final venue verified: ICLR 2024 conference paper.
- **Verification source:** https://openreview.net/forum?id=9JQtrumvg8

---

## Simple understanding

This paper introduces **WebAgent**, a real-world LLM-based web automation system.

The key problem is that real websites are much harder than simulated environments. Real pages have:

```text
long messy HTML
dynamic content
irrelevant boilerplate
no fixed action space
many clickable elements
task-specific structure
```

The paper proposes a modular solution:

```text
user instruction
→ planning into sub-instructions
→ long HTML summarization
→ task-relevant snippets
→ Python program synthesis
→ browser action
```

The system uses **HTML-T5** for HTML understanding and summarization, and a language model for generating executable Python programs.

For my thesis, this paper matters because it directly targets real-world web automation and shows why long-context HTML understanding and programmatic actions are important.

---

## Notes

- **Core idea:**
  Build a real-world web agent by combining planning, long HTML summarization, and program synthesis.

- **Key finding:**
  The paper reports improved real-world web success and strong results on MiniWoB++ and Mind2Web-style tasks, showing that HTML-specialized models help web automation.

- **Limitation:**
  The system depends on specialized components such as HTML-T5 and program synthesis, increasing engineering complexity.

- **Additional limitation:**
  HTML summarization may remove task-relevant elements. For extraction, this can cause missing fields or wrong outputs.

- **Additional limitation:**
  Generated Python actions are powerful but risky. For deployment, program synthesis must be sandboxed and verified.

- **Additional limitation:**
  The approach emphasizes HTML more than visual layout, but many modern webpages require screenshot-level reasoning.

- **Connects to:**
  DOM-Q-NET, WebGPT, WebShop, Mind2Web, AutoWebGLM, WebVoyager, and program-synthesis web automation.

- **Use in thesis:**
  Use as a major real-world web-agent paper showing that real web automation requires long HTML handling, planning, and executable action generation.

---

## Thesis-ready paragraph

Gur et al. introduced WebAgent, a modular LLM-based system for real-world web automation that combines planning, long-context HTML understanding, and program synthesis. The system decomposes natural-language instructions into sub-instructions, summarizes long HTML pages into task-relevant snippets using HTML-T5, and generates executable Python programs to interact with websites. This work is important because it directly addresses the limitations of simulated web benchmarks: real websites have open-ended action spaces, long noisy HTML, and no predefined set of clickable actions. For generalized web automation and data extraction, WebAgent shows that LLM agents need specialized web representations and executable action mechanisms. However, it also reveals major open issues: summarization can omit relevant information, generated code must be constrained, and real websites remain dynamic and difficult to evaluate robustly.

---

## Why this paper matters for my thesis

This paper matters because it moves from simplified benchmarks to real websites.

A real webpage may have:

```text
50,000+ HTML tokens
ads
menus
hidden elements
scripts
forms
irrelevant sections
duplicated labels
```

A model cannot simply read everything naively.

WebAgent proposes:

```text
plan the task
compress the page
focus on relevant snippets
generate code to act
```

For data extraction, this is especially relevant because extraction requires selecting the right parts of the HTML and producing structured output.

---

## Important concepts to remember

### 1. HTML-T5

A model specialized for understanding and processing long HTML.

### 2. Long HTML summarization

Compressing page HTML into task-relevant snippets.

### 3. Program synthesis

Generating executable Python code to interact with a website.

### 4. Sub-instruction planning

Breaking a user instruction into smaller actionable steps.

### 5. Self-experience supervision

Using generated agent experience to improve web-model behavior.

### 6. Open-ended action space

Real websites do not provide a fixed set of actions.

---

## Key evidence from the paper

### Real vs simulated web

The paper contrasts real websites with simplified simulators, highlighting long HTML and open-ended actions.

### Architecture

The system combines HTML-T5 planning/summarization and program synthesis.

### HTML length

The paper emphasizes that real webpages have much longer HTML than benchmark simulators.

### Reported gains

The paper reports strong improvements in real-world web settings and HTML-based benchmarks.

---

## Connection to earlier and later papers

### Connection to DOM-Q-NET

DOM-Q-NET uses DOM graph structure.

WebAgent extends the representation problem to real long HTML.

```text
DOM-Q-NET = structured DOM for RL
WebAgent = long HTML understanding for LLM agents
```

### Connection to AutoWebGLM

Both systems simplify or transform HTML for web agents.

WebAgent uses HTML-T5 and program synthesis.

AutoWebGLM uses simplified HTML and trained web-navigation policies.

### Connection to WebVoyager

WebAgent is more HTML/program-oriented.

WebVoyager is more screenshot/multimodal-oriented.

Both address real websites.

---

## Connection to later thesis sections

- **S5.2 — Perception and Grounding:**
  Long HTML summarization and task-relevant snippet selection.
- **S5.3 — Planning:**
  Sub-instruction planning and action decomposition.
- **S5.4 — Training:**
  HTML-T5 specialization and self-experience supervision.
- **S6 — Extraction:**
  Programmatic extraction and structured web operations.
- **S8 — Deployment:**
  Risks of generated code and real-web variability.

---

## Limitation connected to thesis

WebAgent improves real-world web automation, but it is not a complete solution.

It mainly improves:

```text
planning + HTML compression + programmatic action
```

It does not fully solve:

- screenshot/visual grounding,
- safe execution of generated programs,
- dynamic website change,
- robust verification of extracted data,
- user privacy,
- or generalization to all websites.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Very high
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Figures comparing simulated and real websites
  - HTML-T5 method
  - Planning module
  - HTML summarization
  - Program synthesis
  - Real-world evaluation
  - Limitations

---

## One-sentence summary

WebAgent shows that real-world web automation requires planning, long HTML understanding, and program synthesis, but generated actions and compressed observations still need grounding, safety, and verification.

---

## BibTeX

```bibtex
@inproceedings{gur2024realworld,
  title     = {A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis},
  author    = {Gur, Izzeddin and Furuta, Hiroki and Huang, Austin and Safdari, Mustafa and Matsuo, Yutaka and Eck, Douglas and Faust, Aleksandra},
  booktitle = {International Conference on Learning Representations},
  year      = {2024},
  eprint    = {2307.12856},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  doi       = {10.48550/arXiv.2307.12856},
  url       = {https://openreview.net/forum?id=9JQtrumvg8}
}
```

---

## Source links

- https://arxiv.org/abs/2307.12856


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2024-05 - Large Language Model Powered Agents in the Web.md

# Paper 288 — Large Language Model Powered Agents in the Web

## Metadata

- **Title:** Large Language Model Powered Agents in the Web
- **Authors:** Yang Deng, An Zhang, Yankai Lin, Xu Chen, Ji-Rong Wen, Tat-Seng Chua
- **Year:** 2024
- **Venue:** Companion Proceedings of the ACM Web Conference 2024 (WWW 2024 Companion), tutorial paper, pp. 1242–1245
- **DOI:** 10.1145/3589335.3641240
- **arXiv ID:** Not listed
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S3 agent architecture; S4 web-agent scope; S5.3 planning; S6 web mining/recommender/conversational systems; S8 applications
- **Category:** TUTORIAL / WEB APPLICATIONS / LLM AGENTS
- **Paper type:** Tutorial paper / overview
- **Priority:** P1
- **BibTeX key:** deng2024llmpoweredweb
- **Final publication status:** Final venue verified: WWW 2024 Companion tutorial paper.
- **Verification source:** https://doi.org/10.1145/3589335.3641240

---

## Simple understanding

This paper is a **WWW 2024 tutorial paper** about LLM-powered agents in the web.

It is not a new system paper or benchmark. Its value is positioning: it explains that LLM-powered agents are becoming relevant across web applications, including:

```text
web mining
social networks
recommender systems
conversational systems
web automation
```

The paper describes LLM-agent architecture using modules such as:

```text
profile
memory
planning
action
```

For my thesis, this paper is useful as context. It helps position generalized web automation inside the broader WWW research community.

---

## Notes

- **Core idea:**
  Present a tutorial overview of LLM-powered agents in web applications and their architecture.

- **Key finding:**
  The tutorial argues that LLM agents can enhance web applications through memory, planning, reasoning, and autonomous action.

- **Limitation:**
  It is a tutorial/overview, not a new empirical system paper.

- **Additional limitation:**
  It is broad across web applications and does not deeply analyze DOM grounding, browser control, or extraction verification.

- **Additional limitation:**
  Use it for positioning, not for detailed performance claims.

- **Connects to:**
  LLM agents, recommender systems, web mining, social networks, conversational systems, and web automation.

- **Use in thesis:**
  Use briefly to show that LLM agents are recognized as an important topic in the Web/WWW research community.

---

## Thesis-ready paragraph

Deng et al. present a WWW 2024 tutorial on large-language-model-powered agents in the web. The paper positions LLM agents as a broad paradigm for enhancing web applications through profiling, memory, planning, and action. It discusses applications beyond browser control, including web mining, social networks, recommender systems, and conversational systems. For this thesis, the paper is useful as contextual support because it shows that LLM-based agents are becoming important across the web research ecosystem. However, because it is a short tutorial paper rather than a full system or benchmark, it should not be used as primary evidence for technical claims about web automation performance, grounding, or extraction.

---

## Why this paper matters for my thesis

This paper matters mainly for positioning.

Your thesis is about:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper helps show that the broader web community is also moving toward:

```text
LLM agents + web applications
```

It is useful in the introduction or S4 framing, but it should not replace primary papers such as WebGPT, WebShop, SeeAct, WebVoyager, WebAgent, or AutoWebGLM.

---

## Important concepts to remember

### 1. Profile

The role, identity, or goal description of an agent.

### 2. Memory

Information stored from previous interactions or user history.

### 3. Planning

The process of decomposing a goal into steps.

### 4. Action

The operations the agent performs in a web environment or web application.

### 5. Web applications

Broader web settings beyond browser navigation, including recommendation and social platforms.

---

## Key evidence from the paper

### Tutorial scope

The paper positions LLM agents across web mining, social networks, recommender systems, and conversational systems.

### Architecture overview

It uses common agent modules such as profiling, memory, planning, and action.

### WWW relevance

Its publication as a WWW companion/tutorial paper supports the relevance of LLM agents to web research.

---

## Connection to earlier and later papers

### Connection to agent surveys

This tutorial overlaps with broad agent surveys but is focused on the web research community.

### Connection to S4

It can be used to introduce why LLM agents matter beyond narrow browser tasks.

### Connection to S6

It connects web automation with web mining, recommendation, and conversational systems.

---

## Connection to later thesis sections

- **S3 — Agent Architectures:**
  Profile-memory-planning-action framing.
- **S4 — Web Agent Evolution:**
  Contextual positioning within web research.
- **S6 — Web Information Access:**
  Connections to web mining and recommendation.
- **S8 — Deployment:**
  Practical web applications and product-facing agents.

---

## Limitation connected to thesis

This paper does not solve any technical web-agent challenge.

For the thesis, use it as background only. It does not provide:

- a benchmark,
- a new system,
- detailed web grounding analysis,
- extraction evaluation,
- or deployment results.

---

## Reading decision

- **Read fully?** No, selective reading is enough
- **Depth needed:** Selective
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Tutorial outline
  - Agent architecture overview
  - Application areas

---

## One-sentence summary

This tutorial positions LLM-powered agents as a broad web-application paradigm, but it is contextual rather than a core technical web-automation paper.

---

## BibTeX

```bibtex
@inproceedings{deng2024llmpoweredweb,
  title     = {Large Language Model Powered Agents in the Web},
  author    = {Deng, Yang and Zhang, An and Lin, Yankai and Chen, Xu and Wen, Ji-Rong and Chua, Tat-Seng},
  booktitle = {Companion Proceedings of the ACM Web Conference 2024},
  pages     = {1242--1245},
  year      = {2024},
  publisher = {Association for Computing Machinery},
  doi       = {10.1145/3589335.3641240},
  url       = {https://doi.org/10.1145/3589335.3641240}
}
```

---

## Source links

- https://doi.org/10.1145/3589335.3641240


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2024-10 - Agent S- An Open Agentic Framework that Uses Computers Like a Human.md

# Paper 290 — Agent S: An Open Agentic Framework that Uses Computers Like a Human

## Metadata

- **Title:** Agent S: An Open Agentic Framework that Uses Computers Like a Human
- **Authors:** Saaket Agashe, Jiuzhou Han, Shuyu Gan, Jiachen Yang, Ang Li, Xin Eric Wang
- **Year:** 2024
- **Venue:** International Conference on Learning Representations (ICLR 2025), poster
- **DOI:** 10.48550/arXiv.2410.08164
- **arXiv ID:** arXiv:2410.08164
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.2 GUI grounding; S5.3 hierarchical planning; S5.4 memory/experience; S5.5 GUI failures; S8 cross-platform computer use
- **Category:** GUI AGENT / COMPUTER-USE / HIERARCHICAL PLANNING
- **Paper type:** System / open agentic framework
- **Priority:** P1
- **BibTeX key:** agashe2024agents
- **Final publication status:** Final venue verified: ICLR 2025 Poster.
- **Verification source:** https://openreview.net/forum?id=lIVRgt4nLv

---

## Simple understanding

Agent S is a general **computer-use GUI agent**, not only a web agent.

It targets tasks across desktop environments and applications. The system is built around three major needs:

```text
domain-specific knowledge
long-horizon hierarchical planning
dynamic interface handling
```

Agent S uses:

```text
online web search
narrative memory
episodic memory
hierarchical planning
Agent-Computer Interface
```

For my thesis, Agent S is useful because generalized web automation is part of a larger movement: LLM agents that use computers and graphical interfaces like humans. Web agents share many of the same challenges: perception, grounding, memory, action execution, and safety.

---

## Notes

- **Core idea:**
  Build an open GUI-agent framework with experience-augmented hierarchical planning, external knowledge retrieval, narrative/episodic memory, and an Agent-Computer Interface.

- **Key finding:**
  Agent S improves performance on OSWorld and WindowsAgentArena relative to baseline GUI agents, showing the value of hierarchical planning and experience.

- **Limitation:**
  It remains far below human performance on realistic computer-use tasks.

- **Additional limitation:**
  It is a general GUI/computer agent, not a web-extraction-specific system.

- **Additional limitation:**
  Memory can be stale, wrong, or irrelevant if not verified.

- **Additional limitation:**
  External web search can introduce noisy or unreliable information.

- **Connects to:**
  WebVoyager, SeeAct, AutoGLM, CoALA, Reflexion, OSWorld, WindowsAgentArena, and broader computer-use agents.

- **Use in thesis:**
  Use to show that web automation belongs to the broader GUI-agent/computer-use paradigm.

---

## Thesis-ready paragraph

Agashe et al. introduced Agent S, an open agentic framework designed to use computers through graphical user interfaces. The system combines online knowledge retrieval, narrative memory, episodic memory, hierarchical planning, and a language-centric Agent-Computer Interface. Although Agent S is broader than web automation, it is relevant to this thesis because web agents face similar challenges: they must use domain knowledge, plan over long horizons, interact with dynamic interfaces, and remember previous experiences. Agent S demonstrates that hierarchical planning and memory improve GUI-agent performance, but its remaining gap to human performance shows that reliable computer-use automation remains difficult. For web automation, the paper is most useful as a bridge from browser agents to general GUI agents.

---

## Why this paper matters for my thesis

This paper matters because web automation is increasingly part of **computer-use automation**.

A real assistant may need to:

```text
open browser
use web app
download file
open spreadsheet
copy extracted data
send email
```

This crosses the boundary between web and desktop GUI tasks.

Agent S helps your thesis connect web agents to the broader GUI-agent literature, especially for:

```text
memory
hierarchical planning
interface action abstraction
experience reuse
```


---

## Important concepts to remember

### 1. Agent-Computer Interface

A structured interface that defines how the agent can interact with the computer.

### 2. Hierarchical planning

Breaking a complex task into subtasks and low-level actions.

### 3. Narrative memory

High-level summaries of prior experiences.

### 4. Episodic memory

Detailed memories of specific previous task trajectories.

### 5. Online knowledge retrieval

Using web search to gather task-specific instructions or domain knowledge.

### 6. OSWorld

A benchmark for realistic operating-system tasks.

---

## Key evidence from the paper

### Architecture

The paper presents an architecture combining online search, narrative memory, episodic memory, hierarchical planning, and ACI.

### Motivation

It identifies domain knowledge, long-horizon planning, and dynamic non-uniform interfaces as central challenges.

### Benchmark results

Agent S improves performance on OSWorld and WindowsAgentArena, showing benefit from experience-augmented planning.

### Thesis evidence

The key lesson is that realistic GUI automation requires both memory and planning, not only a vision-language model.

---

## Connection to earlier and later papers

### Connection to Reflexion

Agent S uses experience and memory, similar in spirit to Reflexion, but in broader GUI environments.

### Connection to WebVoyager

WebVoyager is browser-specific.

Agent S is broader computer-use.

### Connection to AutoGLM

Both Agent S and AutoGLM represent the trend toward general GUI foundation agents.

---

## Connection to later thesis sections

- **S5.2 — Grounding:**
  GUI perception and action targeting.
- **S5.3 — Planning:**
  Hierarchical task decomposition.
- **S5.4 — Training/Memory:**
  Experience and memory reuse.
- **S5.5 — Failure Modes:**
  Dynamic interface failures and wrong action execution.
- **S8 — Deployment:**
  Cross-platform computer-use automation.

---

## Limitation connected to thesis

Agent S improves GUI automation, but it does not directly solve web data extraction.

It mainly contributes:

```text
hierarchical planning + memory + computer-use interface
```

It does not fully solve:

- DOM-specific grounding,
- web extraction verification,
- website-specific constraints,
- browser security,
- or precise data extraction workflows.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Medium-high
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Architecture figure
  - Agent-Computer Interface
  - Narrative memory
  - Episodic memory
  - Hierarchical planning
  - OSWorld results
  - Failure analysis

---

## One-sentence summary

Agent S shows that GUI agents benefit from hierarchical planning and experience memory, but realistic computer-use automation remains far from solved.

---

## BibTeX

```bibtex
@inproceedings{agashe2025agents,
  title     = {Agent S: An Open Agentic Framework that Uses Computers Like a Human},
  author    = {Agashe, Saaket and Han, Jiuzhou and Gan, Shuyu and Yang, Jiachen and Li, Ang and Wang, Xin Eric},
  booktitle = {International Conference on Learning Representations},
  year      = {2025},
  eprint    = {2410.08164},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  doi       = {10.48550/arXiv.2410.08164},
  url       = {https://openreview.net/forum?id=lIVRgt4nLv}
}
```

---

## Source links

- https://arxiv.org/abs/2410.08164
- https://github.com/simular-ai/Agent-S


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2024-10 - AutoGLM Autonomous Foundation Agents for GUIs.md

# Paper 291 — AutoGLM: Autonomous Foundation Agents for GUIs

## Metadata

- **Title:** AutoGLM: Autonomous Foundation Agents for GUIs
- **Authors:** Xiao Liu, Bo Qin, Dongzhu Liang, Guang Dong, Hanyu Lai, Hanchen Zhang, and others
- **Year:** 2024
- **Venue:** arXiv preprint
- **DOI:** 10.48550/arXiv.2411.00820
- **arXiv ID:** arXiv:2411.00820
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.2 intermediate interfaces/grounding; S5.3 planning; S5.4 online curriculum RL; S5.5 error recovery; S8 deployable GUI agents
- **Category:** GUI AGENT / FOUNDATION AGENT / WEB + ANDROID
- **Paper type:** System / foundation GUI agent
- **Priority:** P1
- **BibTeX key:** liu2024autoglm
- **Final publication status:** Final status checked: arXiv preprint; no final peer-reviewed conference/journal venue found.
- **Verification source:** https://arxiv.org/abs/2411.00820

---

## Simple understanding

AutoGLM presents autonomous foundation agents for graphical user interfaces, especially web and Android environments.

The key idea is to separate:

```text
planning behavior → flexible reasoning and recovery
grounding behavior → accurate mapping to UI elements
```

AutoGLM uses an **intermediate interface** so the planner does not directly operate on raw pixels or raw UI complexity. It also uses **progressive self-evolving online curriculum reinforcement learning** to improve behavior.

For my thesis, AutoGLM matters because web agents also need this separation. A web agent may understand what to do, but it still needs a reliable way to ground that plan into the correct UI element and action.

---

## Notes

- **Core idea:**
  Build GUI foundation agents using an intermediate interface that separates planning from grounding, trained with progressive self-evolving online curriculum RL.

- **Key finding:**
  The paper reports strong results on WebArena-like, OpenTable, AndroidLab, and common Chinese app tasks, suggesting progress toward deployable GUI agents.

- **Limitation:**
  High scores may depend on selected domains and task distributions; arbitrary web generalization remains difficult.

- **Additional limitation:**
  Intermediate interfaces require engineering and may not transfer perfectly across platforms.

- **Additional limitation:**
  Online RL requires safe environments and reliable rewards; real websites may contain irreversible actions.

- **Additional limitation:**
  Planning-grounding separation helps but does not eliminate grounding errors.

- **Connects to:**
  AutoWebGLM, SeeAct, WebVoyager, Agent S, GUI-agent surveys, and deployable browser/mobile agents.

- **Use in thesis:**
  Use as a modern GUI-agent paper showing the importance of planning-grounding separation and online training.

---

## Thesis-ready paragraph

AutoGLM introduces autonomous foundation agents for graphical user interfaces, focusing on web and mobile environments. The system emphasizes two design principles: an intermediate interface is needed to separate flexible planning from precise grounding, and self-evolving online curriculum reinforcement learning can improve agents through interaction. This is highly relevant to LLM-based web automation because a web agent must both reason about user goals and accurately ground actions in UI elements. AutoGLM’s results on web and Android tasks suggest progress toward deployable GUI agents, but its limitations remain central to this thesis: cross-site generalization, safety during online learning, reward reliability, and privacy-sensitive deployment.

---

## Why this paper matters for my thesis

This paper matters because it makes a key design principle explicit:

```text
planning ≠ grounding
```

A model may plan:

```text
Open the booking page and choose a date.
```

But grounding requires:

```text
which button?
which date cell?
which input field?
which operation?
```

AutoGLM argues that these should be separated through an intermediate interface and trained appropriately.

This directly supports S5.2 and S5.3.

---

## Important concepts to remember

### 1. Foundation agent

A general agent system designed to operate across GUI environments.

### 2. Intermediate interface

An abstraction layer between raw GUI and agent action planning.

### 3. Planning behavior

The agent’s reasoning over goals, subtasks, and recovery.

### 4. Grounding behavior

The mapping from planned actions to specific UI elements and operations.

### 5. Self-evolving online curriculum RL

Progressive interaction-based training from easier to harder tasks.

---

## Key evidence from the paper

### Design insight

The abstract emphasizes intermediate interface design and self-evolving curriculum RL.

### Web and mobile evaluation

The paper evaluates on web/browser and Android tasks.

### Reported performance

The paper reports strong benchmark results on WebArena-like, OpenTable, and Android tasks.

### Deployment relevance

Figures and examples show GUI foundation agents in practical app/browser settings.

---

## Connection to earlier and later papers

### Connection to SeeAct

SeeAct identifies grounding as the bottleneck.

AutoGLM proposes an intermediate-interface approach to improve planning-grounding separation.

### Connection to AutoWebGLM

AutoWebGLM is web-navigation-specific.

AutoGLM generalizes toward GUI foundation agents across web and mobile.

### Connection to Agent S

Both focus on broader computer/GUI use beyond only web browsing.

---

## Connection to later thesis sections

- **S5.2 — Perception/Grounding:**
  Intermediate interfaces and element grounding.
- **S5.3 — Planning:**
  Separation of planning behavior from execution.
- **S5.4 — Training:**
  Online curriculum RL and self-evolution.
- **S5.5 — Failure Modes:**
  Grounding errors and recovery.
- **S8 — Deployment:**
  Browser/mobile deployment, privacy, and permissions.

---

## Limitation connected to thesis

AutoGLM advances GUI foundation agents, but it does not fully solve generalized web automation.

It mainly improves:

```text
planning-grounding separation + online GUI training
```

It does not fully solve:

- reliable open-web generalization,
- extraction verification,
- website policy constraints,
- privacy-sensitive workflows,
- or long-term tool/interface maintenance.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Intermediate interface design
  - Planning vs grounding
  - Curriculum RL
  - Web/browser results
  - Android results
  - Limitations

---

## One-sentence summary

AutoGLM frames GUI automation as a foundation-agent problem where planning and grounding must be separated and improved through online curriculum learning.

---

## BibTeX

```bibtex
@article{liu2024autoglm,
  title   = {AutoGLM: Autonomous Foundation Agents for GUIs},
  author  = {Liu, Xiao and Qin, Bo and Liang, Dongzhu and Dong, Guang and Lai, Hanyu and Zhang, Hanchen and Zhao, Hanlin and Iong, Iat Long and Sun, Jiadai and Wang, Jiaqi and others},
  journal = {arXiv preprint arXiv:2411.00820},
  year    = {2024},
  doi     = {10.48550/arXiv.2411.00820}
}
```

---

## Source links

- https://arxiv.org/abs/2411.00820
- https://xiao9905.github.io/AutoGLM


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2024-10 - AutoWebGLM- Bootstrap and Reinforce A Large Language Model-based Web Navigating Agent.md

# Paper 289 — AutoWebGLM: Bootstrap and Reinforce A Large Language Model-based Web Navigating Agent

## Metadata

- **Title:** AutoWebGLM: Bootstrap and Reinforce A Large Language Model-based Web Navigating Agent
- **Authors:** Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, Jie Tang
- **Year:** 2024
- **Venue:** arXiv preprint / extended earlier version; superseded for citation by the KDD 2024 version
- **DOI:** 10.48550/arXiv.2404.03648
- **arXiv ID:** arXiv:2404.03648
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 AutoWebBench; S5.2 HTML simplification; S5.3 task decomposition; S5.4 curriculum/RL/RFT; S5.5 loops and self-checking failures; S8 browser extension/deployment
- **Category:** WEB-LLM / TRAINED WEB NAVIGATION AGENT / AUTOWEBGLM
- **Paper type:** System / training framework / benchmark
- **Priority:** P1
- **BibTeX key:** lai2024autowebglmbootstrap
- **Final publication status:** Final status verified: arXiv preprint/extended version; use the KDD 2024 paper as the final conference citation.
- **Verification source:** https://arxiv.org/abs/2404.03648


## Citation note

This is the extended arXiv/preprint version. For final thesis citation, prefer the KDD 2024 version: **AutoWebGLM: A Large Language Model-based Web Navigating Agent**.

---

## Simple understanding

This is the earlier/extended AutoWebGLM paper.

AutoWebGLM is a trained web-navigation agent based on **ChatGLM3-6B**. It is important because it moves away from only prompting large proprietary models and instead trains a smaller open model for browser navigation.

The paper argues that real web navigation is hard because:

```text
webpages are long and noisy
there is no unified action space
high-quality trajectories are scarce
agents get stuck in loops
self-checking is weak
```

AutoWebGLM addresses this with:

```text
HTML simplification
human-AI browsing trajectories
curriculum learning
reinforcement learning
rejection sampling finetuning
AutoWebBench
```

For my thesis, this paper is important because it shows how web agents can be specialized through data and training, not only prompt engineering.

---

## Notes

- **Core idea:**
  Train a ChatGLM3-6B-based web-navigation agent using simplified HTML observations, human-AI trajectories, curriculum learning, reinforcement learning, and rejection sampling finetuning.

- **Key finding:**
  AutoWebGLM is reported to perform competitively across web-navigation benchmarks and can outperform prompted GPT-4 in several settings while remaining smaller and deployable.

- **Limitation:**
  HTML simplification can remove information needed for precise extraction or grounding.

- **Additional limitation:**
  Training quality depends on trajectory quality; hybrid human-AI data can include bias or model errors.

- **Additional limitation:**
  RL and rejection sampling require reliable reward or evaluation signals, which are hard for open-ended web tasks.

- **Additional limitation:**
  The system is mainly a web-navigation agent, not a complete extraction/verifier system.

- **Connects to:**
  WebAgent, WebVoyager, Mind2Web, WebArena, MiniWoB++, AutoWebBench, and trained open web agents.

- **Use in thesis:**
  Use as a key S4 paper for trained web navigation and as support for S5.4 training strategies.

---

## Thesis-ready paragraph

AutoWebGLM presents a trained LLM-based web-navigation agent built on ChatGLM3-6B. The system combines HTML simplification, a browser automation framework, hybrid human-AI trajectory collection, curriculum learning, reinforcement learning, and rejection sampling finetuning. This paper is important for the evolution of web agents because it shows that smaller open models can be specialized for web navigation through task-specific data and training. For generalized web automation, AutoWebGLM addresses several practical problems: long noisy HTML, scarce demonstrations, open-domain action decisions, and loop correction. However, it also reveals remaining limitations: simplified HTML may omit relevant details, reward signals are difficult to define, and web navigation is not identical to robust structured data extraction.

---

## Why this paper matters for my thesis

This paper matters because it shows a practical path toward deployable open web agents.

A prompt-only agent may rely on:

```text
large proprietary model + prompt + browser tool
```

AutoWebGLM instead uses:

```text
smaller model + web-specific observation design + trajectories + training
```

For a PhD thesis, this is important because generalized web automation may require specialized models and datasets, not only prompting GPT-4-like systems.

---

## Important concepts to remember

### 1. HTML simplification

Reducing webpage HTML to a shorter representation for the model.

### 2. Curriculum learning

Training from simple operations to longer browsing traces.

### 3. Reinforcement learning

Optimizing behavior through reward signals.

### 4. Rejection sampling finetuning

Generating multiple outputs and fine-tuning on selected high-quality trajectories.

### 5. AutoWebBench

A bilingual benchmark for real-world browsing tasks.

### 6. Self-checking

The model’s ability to detect whether it is progressing or stuck.

---

## Key evidence from the paper

### Architecture

The paper presents a system with simplified HTML, automated browsing, OCR, curriculum learning, RL, and RFT.

### Trajectory data

It reports a browsing-operation dataset collected through human-AI collaboration.

### Benchmarking

It evaluates across several web-agent benchmarks and compares with stronger prompted models.

### Deployment

The system is associated with practical browser-agent deployment, making it relevant to S8.

---

## Connection to earlier and later papers

### Connection to WebAgent

Both WebAgent and AutoWebGLM target real web automation through HTML-aware methods.

WebAgent emphasizes program synthesis.

AutoWebGLM emphasizes trained web-navigation policies.

### Connection to WebVoyager

WebVoyager uses multimodal screenshots and labeled elements.

AutoWebGLM uses simplified HTML and trained browser operations.

### Connection to S5.4

AutoWebGLM is one of the strongest examples of web-agent training:

```text
trajectory data → curriculum → RL → RFT
```

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  AutoWebBench and multi-benchmark comparison.
- **S5.2 — Perception/Grounding:**
  HTML simplification and observation formatting.
- **S5.3 — Planning:**
  Task decomposition and browser navigation decisions.
- **S5.4 — Training:**
  Curriculum learning, RL, and rejection sampling finetuning.
- **S5.5 — Failure Modes:**
  Loops, bad self-checking, and wrong action inference.
- **S8 — Deployment:**
  Browser extension and real-world usability.

---

## Limitation connected to thesis

AutoWebGLM improves trained web navigation, but it does not fully solve generalized web automation and data extraction.

It mainly improves:

```text
web navigation policy + HTML simplification + training
```

It does not fully solve:

- arbitrary website generalization,
- robust extraction verification,
- multimodal visual grounding,
- privacy and permission boundaries,
- irreversible action safety,
- or long-term website maintenance.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Motivation/challenges
  - HTML simplification
  - Data collection
  - Curriculum learning
  - RL/RFT
  - AutoWebBench
  - Results
  - Failure analysis

---

## One-sentence summary

AutoWebGLM shows that smaller trained LLMs can become strong web-navigation agents through HTML simplification, trajectory data, curriculum learning, RL, and RFT.

---

## BibTeX

```bibtex
@article{lai2024autowebglmbootstrap,
  title   = {AutoWebGLM: Bootstrap And Reinforce A Large Language Model-based Web Navigating Agent},
  author  = {Lai, Hanyu and Liu, Xiao and Iong, Iat Long and Yao, Shuntian and Chen, Yuxuan and Shen, Pengbo and Yu, Hao and Zhang, Hanchen and Zhang, Xiaohan and Dong, Yuxiao and Tang, Jie},
  journal = {arXiv preprint arXiv:2404.03648},
  year    = {2024},
  doi     = {10.48550/arXiv.2404.03648},
  note    = {Extended earlier version; final conference version published at KDD 2024}
}
```

---

## Source links

- https://arxiv.org/abs/2404.03648
- https://github.com/THUDM/AutoWebGLM


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2024-11 - Large Language Model-Brained GUI Agents- A Survey - preprint version.md

# Paper 292 — Large Language Model-Brained GUI Agents: A Survey

## Metadata

- **Title:** Large Language Model-Brained GUI Agents: A Survey
- **Authors:** Chaoyun Zhang, Shilin He, Jiaxu Qian, Bowen Li, Liqun Li, Si Qin, Yu Kang, Minghua Ma, Guyue Liu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
- **Year:** 2024 / later 2025
- **Venue:** arXiv preprint; superseded by the peer-reviewed TMLR 2025 version
- **DOI:** 10.48550/arXiv.2411.18279
- **arXiv ID:** arXiv:2411.18279
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 evaluation; S5.2 GUI grounding; S5.3 planning/actions; S5.4 data/models; S5.5 challenges; S8 roadmap
- **Category:** SURVEY / LLM-BRAINED GUI AGENTS
- **Paper type:** Survey / taxonomy
- **Priority:** P1
- **BibTeX key:** zhang2024llmbrainedpreprint
- **Final publication status:** Final status checked: preprint version; prefer the TMLR 2025 version for final thesis citation.
- **Verification source:** https://arxiv.org/abs/2411.18279


## Citation note

This is the preprint version. For final thesis citation, prefer the peer-reviewed **TMLR 2025** version.

---

## Simple understanding

This is the preprint version of a broad survey on **LLM-brained GUI agents**.

It is useful because web agents are a subset of GUI agents. A GUI agent can control:

```text
web browsers
mobile apps
desktop applications
cross-platform software
```

The survey covers:

```text
background
frameworks
data
models
evaluation
applications
limitations
future roadmap
```

For the thesis, use this as a taxonomy source, but prefer the later TMLR version for final citation.

---

## Notes

- **Core idea:**
  Survey LLM-brained GUI agents across history, core components, frameworks, data, models, evaluation, applications, and challenges.

- **Key finding:**
  The survey argues that LLM-powered GUI agents shift automation from brittle scripts toward flexible natural-language-driven interaction.

- **Limitation:**
  It is a survey, not a new empirical system.

- **Additional limitation:**
  It is broad across web, mobile, and desktop, so web-specific claims should be supported by primary web-agent papers.

- **Additional limitation:**
  Use the later TMLR version when possible for final thesis citation.

- **Connects to:**
  Web agents, GUI automation, mobile agents, desktop agents, large action models, data collection, and evaluation benchmarks.

- **Use in thesis:**
  Use for broad GUI-agent framing and taxonomy.

---

## Thesis-ready paragraph

Zhang et al. survey LLM-brained GUI agents, defining them as agents that use LLMs or multimodal LLMs as cognitive engines for understanding GUI states, planning actions, and executing operations. The survey is relevant to this thesis because web agents are one important subcategory of GUI agents. Its discussion of operating environments, perception, planning, action execution, data, models, evaluation, and challenges helps position generalized web automation within a broader GUI-agent ecosystem. However, as a survey, it should be used mainly for taxonomy and roadmap; detailed empirical claims should rely on primary system papers such as WebVoyager, SeeAct, AutoWebGLM, and WebAgent.

---

## Why this paper matters for my thesis

This paper matters because it helps explain that web automation is part of a larger trend:

```text
chatbots → agents → GUI agents → computer-use agents
```

A web agent is not isolated. It shares problems with mobile and desktop agents:

```text
screen perception
element grounding
action generation
memory
planning
evaluation
privacy
latency
safety
```

The survey is useful for structure, not for detailed performance evidence.

---

## Important concepts to remember

### 1. LLM-brained GUI agent

A GUI agent using an LLM/MLLM as the cognitive engine.

### 2. Large Action Model

A model specialized for generating GUI actions.

### 3. Operating environment

The platform controlled by the agent: web, mobile, desktop, or cross-platform.

### 4. State perception

How the agent observes GUI state through screenshots, DOM, accessibility trees, OCR, or metadata.

### 5. Action execution

How the agent converts decisions into clicks, typing, API calls, or system operations.

### 6. Roadmap

Open problems such as privacy, latency, safety, ethics, and scalability.

---

## Key evidence from the paper

### Survey structure

The paper organizes the field into foundations, frameworks, data, models, evaluation, applications, and challenges.

### Figure 1

Shows an agent acting across applications such as browser, Word, PowerPoint, Teams, and other software.

### Motivation

The introduction contrasts brittle script-based automation with adaptive LLM-powered GUI agents.

### Limitations

The survey highlights privacy, latency, safety, human-agent interaction, customization, ethics, and scalability.

---

## Connection to earlier and later papers

### Connection to S4

This survey supports the broader framing that web agents are part of GUI-agent evolution.

### Connection to Agent S and AutoGLM

Agent S and AutoGLM are examples of the GUI-agent direction described by the survey.

### Connection to S5

The survey’s components map naturally to S5 technical sections.

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  Benchmarks and metrics.
- **S5.2 — Grounding:**
  GUI state perception and element localization.
- **S5.3 — Planning:**
  Action inference and task decomposition.
- **S5.4 — Training:**
  Data and large action models.
- **S5.5/S8 — Challenges:**
  Privacy, latency, safety, and scalability.

---

## Limitation connected to thesis

This survey does not directly solve web automation.

Use it to frame:

```text
web agents ⊂ GUI agents
```

but use primary web-agent papers for:

- benchmark results,
- architecture details,
- grounding mechanisms,
- extraction performance,
- and deployment claims.

---

## Reading decision

- **Read fully?** No, selective reading is enough
- **Depth needed:** Selective
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Definitions
  - Framework taxonomy
  - Data and models
  - Evaluation
  - Limitations and roadmap

---

## One-sentence summary

This survey maps the GUI-agent field and helps position web automation inside broader LLM-powered GUI automation.

---

## BibTeX

```bibtex
@article{zhang2024llmbrainedpreprint,
  title   = {Large Language Model-Brained GUI Agents: A Survey},
  author  = {Zhang, Chaoyun and He, Shilin and Qian, Jiaxu and Li, Bowen and Li, Liqun and Qin, Si and Kang, Yu and Ma, Minghua and Liu, Guyue and Lin, Qingwei and Rajmohan, Saravan and Zhang, Dongmei and Zhang, Qi},
  journal = {arXiv preprint arXiv:2411.18279},
  year    = {2024},
  doi     = {10.48550/arXiv.2411.18279},
  note    = {Preprint version; peer-reviewed version accepted in TMLR 2025}
}
```

---

## Source links

- https://arxiv.org/abs/2411.18279
- https://github.com/vyokky/LLM-Brained-GUI-Agents-Survey


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2024-12 - AutoWebGLM A Large Language Model-based Web Navigating Agent.md

# Paper 293 — AutoWebGLM: A Large Language Model-based Web Navigating Agent

## Metadata

- **Title:** AutoWebGLM: A Large Language Model-based Web Navigating Agent
- **Authors:** Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, Jie Tang
- **Year:** 2024
- **Venue:** Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 2024), pp. 5295–5306
- **DOI:** 10.1145/3637528.3671620
- **arXiv ID:** arXiv:2404.03648
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 AutoWebBench; S5.2 HTML simplification; S5.3 web navigation; S5.4 curriculum/RL/RFT; S5.5 loops/self-checking; S8 deployment
- **Category:** WEB-LLM / AUTOWEBGLM / TRAINED WEB NAVIGATION
- **Paper type:** System / conference paper
- **Priority:** P1
- **BibTeX key:** lai2024autowebglm
- **Final publication status:** Final venue verified: KDD 2024 conference paper.
- **Verification source:** https://doi.org/10.1145/3637528.3671620

---

## Simple understanding

This is the **KDD 2024 version** of AutoWebGLM. For final thesis citation, this version should be preferred over the earlier preprint note.

AutoWebGLM is an LLM-based web-navigation agent built on ChatGLM3-6B. It aims to build an open, deployable web agent rather than relying only on proprietary frontier models.

The system uses:

```text
simplified HTML observations
a browsing operation dataset
curriculum learning
reinforcement learning
rejection sampling finetuning
AutoWebBench
browser-extension-style deployment
```

For the thesis, this is a strong S4 P1 paper because it connects web-agent systems with training, benchmarking, and real-world deployment.

---

## Notes

- **Core idea:**
  Present an open ChatGLM3-6B-based web-navigation agent trained with simplified HTML, browsing traces, curriculum learning, RL, and rejection sampling finetuning.

- **Key finding:**
  The paper reports that AutoWebGLM performs competitively with or better than advanced prompted LLM agents across web-navigation benchmarks.

- **Limitation:**
  It is primarily a navigation agent, not a complete generalized web data extraction system.

- **Additional limitation:**
  HTML simplification helps context length but may remove information needed for exact extraction.

- **Additional limitation:**
  Reward signals and self-checking remain difficult in open-ended web tasks.

- **Additional limitation:**
  Deployment through browser tooling raises privacy, permissions, and safety concerns.

- **Connects to:**
  AutoWebGLM preprint, WebAgent, WebVoyager, Mind2Web, WebArena, MiniWoB++, and AutoWebBench.

- **Use in thesis:**
  Use this as the main AutoWebGLM citation and as a major example of trained open web-navigation agents.

---

## Thesis-ready paragraph

Lai et al. present AutoWebGLM, an LLM-based web navigating agent built on ChatGLM3-6B and trained for browser interaction. The system uses simplified HTML representations, a browsing operation dataset, curriculum learning, reinforcement learning, and rejection sampling finetuning to improve webpage understanding, task decomposition, and action execution. AutoWebGLM is important because it demonstrates that smaller open models can be specialized for web navigation rather than relying entirely on prompted proprietary LLMs. It also introduces AutoWebBench, a bilingual benchmark for realistic web tasks. For generalized web automation and data extraction, AutoWebGLM is a significant step toward deployable web agents, but it remains limited by observation simplification, reward design, self-checking reliability, and the need for robust verification of extracted information.

---

## Why this paper matters for my thesis

This paper matters because it gives a more deployable direction than prompt-only agents.

The key thesis point is:

```text
Prompting is not enough for robust web automation.
```

AutoWebGLM shows a training pipeline:

```text
web traces → curriculum → RL → rejection sampling finetuning → better web agent
```

This is important for S5.4.

It also shows the importance of observation design:

```text
raw HTML too long → simplified HTML → model-readable state
```

This is important for S5.2.

---

## Important concepts to remember

### 1. Simplified HTML

A compressed and cleaned HTML representation for the LLM.

### 2. Browsing operation dataset

A dataset of web-action traces used for training.

### 3. Curriculum learning

Training from simpler browsing operations to longer tasks.

### 4. Reinforcement learning

Optimization from task success signals.

### 5. Rejection sampling finetuning

Selecting higher-quality generated actions/trajectories for fine-tuning.

### 6. AutoWebBench

A bilingual benchmark for real-world web navigation.

---

## Key evidence from the paper

### KDD publication

This version is the conference paper and should be preferred for final citation.

### System components

The paper describes webpage simplification, operation data, curriculum learning, RL, and RFT.

### Benchmark comparison

The paper compares against prompted LLM agents and reports competitive performance.

### Deployment relevance

The system is designed as a practical web-navigation agent, making it relevant for S8.

---

## Connection to earlier and later papers

### Connection to the earlier AutoWebGLM note

The preprint/earlier version gives more context, but the KDD version is the stronger citation.

### Connection to WebAgent

Both use HTML-oriented representations, but WebAgent emphasizes program synthesis while AutoWebGLM emphasizes training a web-navigation model.

### Connection to WebVoyager

WebVoyager is multimodal/live-web.

AutoWebGLM is trained HTML/navigation-oriented.

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  AutoWebBench and benchmark design.
- **S5.2 — Perception/Grounding:**
  HTML simplification and webpage representation.
- **S5.3 — Planning:**
  Navigation and task decomposition.
- **S5.4 — Training:**
  Curriculum learning, RL, and RFT.
- **S5.5 — Failure Modes:**
  Looping and self-checking failures.
- **S8 — Deployment:**
  Browser extension and practical web-agent use.

---

## Limitation connected to thesis

AutoWebGLM is a strong web-navigation agent but not a full solution.

It improves:

```text
trained browsing policy + simplified HTML + benchmarked navigation
```

but still needs:

- robust extraction verification,
- multimodal grounding for visual tasks,
- privacy-aware deployment,
- safe irreversible-action handling,
- and maintenance across changing websites.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Very high
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Model/system overview
  - Simplified HTML
  - Browsing operation dataset
  - Curriculum learning
  - RL/RFT
  - AutoWebBench
  - Results
  - Limitations

---

## One-sentence summary

AutoWebGLM shows that trained open LLMs can become competitive web-navigation agents through simplified HTML, curated traces, curriculum learning, RL, and RFT.

---

## BibTeX

```bibtex
@inproceedings{lai2024autowebglm,
  title     = {AutoWebGLM: A Large Language Model-based Web Navigating Agent},
  author    = {Lai, Hanyu and Liu, Xiao and Iong, Iat Long and Yao, Shuntian and Chen, Yuxuan and Shen, Pengbo and Yu, Hao and Zhang, Hanchen and Zhang, Xiaohan and Dong, Yuxiao and Tang, Jie},
  booktitle = {Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  pages     = {5295--5306},
  year      = {2024},
  publisher = {Association for Computing Machinery},
  doi       = {10.1145/3637528.3671620},
  eprint    = {2404.03648},
  archivePrefix = {arXiv},
  url       = {https://doi.org/10.1145/3637528.3671620}
}
```

---

## Source links

- https://doi.org/10.1145/3637528.3671620
- https://arxiv.org/abs/2404.03648
- https://github.com/THUDM/AutoWebGLM


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2025-02 - GUI Agents with Foundation Models- A Comprehensive Survey.md

# Paper 294 — GUI Agents with Foundation Models: A Comprehensive Survey

## Metadata

- **Title:** GUI Agents with Foundation Models: A Comprehensive Survey
- **Authors:** Shuai Wang, Weiwen Liu, Jingxuan Chen, Yuqi Zhou, Weinan Gan, Xingshan Zeng, Yuhan Che, Shuai Yu, Xinlong Hao, Kun Shao, Bin Wang, Chuhan Wu, Yasheng Wang, Ruiming Tang, Jianye Hao
- **Year:** 2025
- **Venue:** arXiv preprint
- **DOI:** 10.48550/arXiv.2411.04890
- **arXiv ID:** arXiv:2411.04890
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 benchmarks; S5.2 GUI data/perception; S5.3 frameworks; S5.4 training/data; S8 applications
- **Category:** SURVEY / GUI AGENTS / FOUNDATION MODELS
- **Paper type:** Survey
- **Priority:** P1
- **BibTeX key:** wang2025guiagentsfoundationmodels
- **Final publication status:** Final status checked: arXiv preprint; no final peer-reviewed conference/journal venue found.
- **Verification source:** https://arxiv.org/abs/2411.04890

---

## Simple understanding

This is a compact survey of GUI agents with foundation models.

It organizes recent work around:

```text
data resources
frameworks
applications
```

For the thesis, it is useful because it places web agents inside the broader GUI-agent ecosystem. It shows the field’s movement from rule-based and RL automation toward multimodal foundation-model agents.

Use it as a survey reference, not as primary evidence for a specific web-agent result.

---

## Notes

- **Core idea:**
  Survey foundation-model-based GUI agents, focusing on datasets/resources, frameworks, and applications.

- **Key finding:**
  The survey argues that foundation models enable a shift from rule-based/RL GUI automation to multimodal, instruction-following GUI agents.

- **Limitation:**
  It is broad and relatively compact, so it cannot deeply analyze each web-agent system.

- **Additional limitation:**
  It covers mobile, web, and desktop agents; the thesis should use web-specific papers for detailed claims.

- **Connects to:**
  GUI datasets, benchmarks, mobile agents, web agents, desktop agents, and commercial GUI assistants.

- **Use in thesis:**
  Use for high-level GUI-agent context and for identifying resources/benchmark categories.

---

## Thesis-ready paragraph

Wang et al. survey GUI agents with foundation models and organize the field around data resources, frameworks, and applications. This survey is useful for a thesis on web automation because web agents are a major subset of GUI agents and share many technical problems with mobile and desktop agents, including perception, grounding, action generation, and evaluation. The paper highlights the broader shift from rule-based or reinforcement-learning GUI automation toward multimodal, instruction-following foundation-model agents. However, because it is a broad survey, it should be used mainly for taxonomy and context, while technical claims about web-agent performance should be supported by primary papers such as SeeAct, WebVoyager, WebAgent, and AutoWebGLM.

---

## Why this paper matters for my thesis

This paper matters because it helps place web automation in a bigger ecosystem.

The field is not only:

```text
browser agents
```

but also:

```text
mobile agents
desktop agents
cross-platform agents
commercial GUI assistants
```

This is useful for your thesis because many technical problems overlap:

```text
screen understanding
element grounding
trajectory data
action generation
evaluation
safety
```


---

## Important concepts to remember

### 1. Data resources

Screenshots, instructions, trajectories, UI metadata, and action labels.

### 2. Frameworks

The agent pipelines used to perceive, decide, act, and receive feedback.

### 3. Applications

Web, mobile, desktop, and commercial GUI automation.

### 4. Foundation models

Large language and multimodal models used as the agent core.

### 5. Success rate

A common but incomplete metric for GUI-agent evaluation.

---

## Key evidence from the paper

### Growth trend

The survey summarizes rapid growth in GUI agents using foundation models.

### Framework overview

It organizes work into data resources, frameworks, and applications.

### Historical shift

It contrasts traditional automation approaches with foundation-model-based GUI agents.

---

## Connection to earlier and later papers

### Connection to S4

This survey supports the claim that web agents are part of the broader GUI-agent wave.

### Connection to S5

Its datasets/frameworks/applications structure maps to evaluation, perception, training, and deployment sections.

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  Datasets, environments, and metrics.
- **S5.2 — Perception:**
  Screenshots and UI information.
- **S5.4 — Training:**
  Trajectory data and model training.
- **S8 — Deployment:**
  Applications and commercial GUI agents.

---

## Limitation connected to thesis

This survey is useful but not enough for detailed thesis claims.

It does not provide:

- a new web-agent method,
- a new benchmark,
- specific extraction evaluation,
- or a deep grounding analysis.

Use it as context.

---

## Reading decision

- **Read fully?** No, selective reading is enough
- **Depth needed:** Selective
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Data resources
  - Frameworks
  - Applications
  - Open challenges

---

## One-sentence summary

This survey gives a compact overview of foundation-model GUI agents and helps place web agents inside the broader GUI-agent ecosystem.

---

## BibTeX

```bibtex
@article{wang2025guiagentsfoundationmodels,
  title   = {GUI Agents with Foundation Models: A Comprehensive Survey},
  author  = {Wang, Shuai and Liu, Weiwen and Chen, Jingxuan and Zhou, Yuqi and Gan, Weinan and Zeng, Xingshan and Che, Yuhan and Yu, Shuai and Hao, Xinlong and Shao, Kun and Wang, Bin and Wu, Chuhan and Wang, Yasheng and Tang, Ruiming and Hao, Jianye},
  journal = {arXiv preprint arXiv:2411.04890},
  year    = {2025},
  doi     = {10.48550/arXiv.2411.04890}
}
```

---

## Source links

- https://arxiv.org/abs/2411.04890


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2025-06 - A Survey on (M)LLM-Based GUI Agents.md

# Paper 295 — A Survey on (M)LLM-Based GUI Agents

## Metadata

- **Title:** A Survey on (M)LLM-Based GUI Agents
- **Authors:** Fei Tang, Haolei Xu, Hang Zhang, Siqi Chen, Xingyu Wu, Yongliang Shen, Wenqi Zhang, Guiyang Hou, Zeqi Tan, Yuchen Yan, Kaitao Song, Jian Shao, Weiming Lu, Jun Xiao, Yueting Zhuang
- **Year:** 2025
- **Venue:** arXiv preprint
- **DOI:** 10.48550/arXiv.2504.13865
- **arXiv ID:** arXiv:2504.13865
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 evaluation; S5.2 perception; S5.3 planning; S5.4 exploration/knowledge; S5.5 safety/errors; S8 future directions
- **Category:** SURVEY / MLLM GUI AGENTS / FOUR-COMPONENT TAXONOMY
- **Paper type:** Survey / taxonomy
- **Priority:** P1
- **BibTeX key:** tang2025survey
- **Final publication status:** Final status checked: arXiv preprint; no final peer-reviewed conference/journal venue found.
- **Verification source:** https://arxiv.org/abs/2504.13865

---

## Simple understanding

This survey is useful because it organizes modern GUI agents around four components:

```text
perception
exploration
planning
interaction
```

This is very relevant to web agents.

A web agent must:

```text
perceive the page
explore or retrieve needed knowledge
plan task steps
interact with the browser safely
```

For the thesis, this paper is most useful as a taxonomy bridge from S4 systems to S5 technical dimensions.

---

## Notes

- **Core idea:**
  Survey (M)LLM-based GUI agents using four core components: perception, exploration, planning, and interaction.

- **Key finding:**
  The survey identifies key challenges including element localization, knowledge retrieval, long-horizon planning, and safety-aware execution.

- **Limitation:**
  It is a broad GUI-agent survey, not a primary web-agent system.

- **Additional limitation:**
  It does not provide new benchmark results.

- **Additional limitation:**
  Use primary papers for specific claims about SeeAct, WebVoyager, AutoGLM, or WebAgent.

- **Connects to:**
  SeeAct, WebVoyager, AutoGLM, Agent S, GUI grounding, exploration, planning, and interaction safety.

- **Use in thesis:**
  Use as a strong S5 taxonomy source.

---

## Thesis-ready paragraph

Tang et al. survey (M)LLM-based GUI agents and organize the field around four core components: perception, exploration, planning, and interaction. This taxonomy is especially useful for LLM-based web automation because it maps directly onto the web-agent pipeline: perceiving DOM or screenshots, retrieving relevant knowledge, planning multi-step actions, and executing interactions safely. The survey identifies central challenges such as element localization, knowledge retrieval, long-horizon planning, and safety-aware execution. For this thesis, the paper is valuable as a conceptual bridge from S4’s system evolution to S5’s technical decomposition, while specific empirical claims should still be grounded in primary benchmark and system papers.

---

## Why this paper matters for my thesis

This paper matters because it gives a clean structure for S5.

The thesis can use the four components like this:

```text
Perception → S5.2
Exploration → S5.3/S5.4
Planning → S5.3
Interaction → S5.2/S5.5/S7
```

It helps convert the chronological S4 story into a technical S5 analysis.

---

## Important concepts to remember

### 1. Perception

Understanding GUI state through screenshots, DOM/XML, OCR, or multimodal models.

### 2. Exploration

Gathering knowledge from history, environment interaction, or external sources.

### 3. Planning

Decomposing tasks and deciding action sequences.

### 4. Interaction

Executing operations safely and effectively in the GUI environment.

### 5. Element localization

Finding the exact target element for clicking, typing, or selecting.

### 6. Safety-aware execution

Avoiding risky, harmful, or irreversible actions.

---

## Key evidence from the paper

### Four-component taxonomy

The abstract and structure identify perception, exploration, planning, and interaction as fundamental components.

### Challenge list

The survey highlights accurate element localization, knowledge retrieval, long-horizon planning, and safety-aware execution.

### Pipeline view

The paper frames GUI agents as an information-processing pipeline from observation to action.

---

## Connection to earlier and later papers

### Connection to SeeAct

SeeAct’s grounding bottleneck falls under perception and interaction.

### Connection to WebVoyager

WebVoyager combines perception, planning, and interaction in live websites.

### Connection to AutoGLM

AutoGLM’s planning-grounding separation maps to planning and interaction.

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  Benchmarks and static/dynamic evaluation.
- **S5.2 — Perception:**
  Interface representation and element grounding.
- **S5.3 — Planning:**
  Long-horizon planning and verification.
- **S5.4 — Training:**
  Exploration and knowledge acquisition.
- **S5.5/S7 — Failures/Safety:**
  Safety-aware execution and error modes.

---

## Limitation connected to thesis

This survey gives structure, not solution.

It helps organize:

```text
perception → exploration → planning → interaction
```

but it does not itself solve:

- web-specific DOM grounding,
- extraction verification,
- live-site safety,
- or benchmark reliability.

---

## Reading decision

- **Read fully?** No, selective reading is enough
- **Depth needed:** Selective-high
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Architecture overview
  - Perception section
  - Exploration section
  - Planning section
  - Interaction section
  - Challenges

---

## One-sentence summary

This survey gives a useful four-part taxonomy—perception, exploration, planning, interaction—for organizing modern web/GUI agent capabilities.

---

## BibTeX

```bibtex
@article{tang2025survey,
  title   = {A Survey on (M)LLM-Based GUI Agents},
  author  = {Tang, Fei and Xu, Haolei and Zhang, Hang and Chen, Siqi and Wu, Xingyu and Shen, Yongliang and Zhang, Wenqi and Hou, Guiyang and Tan, Zeqi and Yan, Yuchen and Song, Kaitao and Shao, Jian and Lu, Weiming and Xiao, Jun and Zhuang, Yueting},
  journal = {arXiv preprint arXiv:2504.13865},
  year    = {2025},
  doi     = {10.48550/arXiv.2504.13865}
}
```

---

## Source links

- https://arxiv.org/abs/2504.13865
- https://github.com/zju-real/Awesome-GUI-Agents


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2025-06 - Large Language Model-Brained GUI Agents- A Survey.md

# Paper 296 — Large Language Model-Brained GUI Agents: A Survey

## Metadata

- **Title:** Large Language Model-Brained GUI Agents: A Survey
- **Authors:** Chaoyun Zhang, Shilin He, Jiaxu Qian, Bowen Li, Liqun Li, Si Qin, Yu Kang, Minghua Ma, Guyue Liu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
- **Year:** 2025
- **Venue:** Transactions on Machine Learning Research (TMLR), 2025
- **DOI:** Not listed
- **arXiv ID:** arXiv:2411.18279
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 evaluation; S5.2 grounding; S5.3 planning/actions; S5.4 data/models/LAMs; S5.5 challenges; S8 deployment roadmap
- **Category:** SURVEY / LLM-POWERED GUI AGENTS / TMLR
- **Paper type:** Peer-reviewed survey
- **Priority:** P1
- **BibTeX key:** zhang2025llmbrained
- **Final publication status:** Final venue verified: TMLR 2025.
- **Verification source:** https://openreview.net/forum?id=xChvYjvXTp

---

## Simple understanding

This is the later peer-reviewed **TMLR version** of the LLM-brained GUI agents survey.

For the final thesis, this version should be preferred over the earlier preprint version.

The survey covers:

```text
foundations
frameworks
data
models
evaluation
applications
limitations
future roadmap
```

For the thesis, this is one of the best broad survey references for connecting web agents to GUI agents.

---

## Notes

- **Core idea:**
  Provide a comprehensive peer-reviewed survey of LLM-powered GUI agents across foundations, frameworks, data, models, evaluation, applications, and challenges.

- **Key finding:**
  The survey argues that LLM-powered GUI agents enable flexible natural-language-driven automation across web, mobile, desktop, and cross-platform environments.

- **Limitation:**
  It is broad across GUI platforms, so web-specific claims need primary web-agent sources.

- **Additional limitation:**
  It does not present new empirical system results.

- **Additional limitation:**
  The field evolves quickly, so very recent agents may be absent.

- **Connects to:**
  Web agents, mobile agents, desktop agents, cross-platform agents, large action models, GUI benchmarks, and deployment challenges.

- **Use in thesis:**
  Use as the preferred broad survey citation for LLM-powered GUI agents.

---

## Thesis-ready paragraph

Zhang et al. provide a comprehensive TMLR survey of LLM-powered GUI agents, defining them as agents that operate within GUI environments using LLMs as cognitive engines to generate, plan, and execute actions flexibly. The survey is valuable for this thesis because web agents are a subcategory of GUI agents and share key challenges with mobile and desktop agents: state perception, grounding, planning, action execution, safety, privacy, latency, and cross-platform generalization. The survey should be used to support the broader framing of web automation, while primary web-agent papers such as WebGPT, WebShop, WebAgent, SeeAct, WebVoyager, and AutoWebGLM provide concrete system evidence.

---

## Why this paper matters for my thesis

This paper matters because it is the best survey-level source for the broader GUI-agent field.

It helps your thesis say:

```text
web agents are not isolated;
they are part of LLM-powered GUI agents.
```

It also helps organize:

```text
data
models
evaluation
applications
limitations
```

For final writing, cite this TMLR version instead of the preprint version.

---

## Important concepts to remember

### 1. LLM-powered GUI agent

An agent using an LLM/MLLM to perceive, plan, and act in GUI environments.

### 2. Frameworks

Agent architectures for web, mobile, desktop, and cross-platform control.

### 3. Large Action Model

A model adapted or trained for GUI action generation.

### 4. Evaluation

Benchmarks, metrics, and task success protocols for GUI agents.

### 5. Roadmap

Open problems: privacy, latency, safety, human-agent interaction, customization, ethics, scalability.

---

## Key evidence from the paper

### Survey scope

The survey covers frameworks, data, models, evaluation, applications, limitations, and future roadmap.

### GUI breadth

It includes web, mobile, computer/desktop, and cross-platform GUI agents.

### Roadmap

It identifies privacy, latency, safety, and scalability as important remaining challenges.

### Peer-reviewed status

The TMLR version is preferable for final academic citation.

---

## Connection to earlier and later papers

### Connection to preprint version

This is the preferred final version of the earlier survey.

### Connection to GUI-agent systems

Agent S and AutoGLM can be positioned using this survey.

### Connection to web agents

Web agents are one platform category inside the broader GUI-agent landscape.

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  GUI benchmarks and metrics.
- **S5.2 — Perception/Grounding:**
  Environment state perception and grounding.
- **S5.3 — Planning:**
  Action inference and task decomposition.
- **S5.4 — Training:**
  Data collection and large action models.
- **S5.5/S8 — Challenges:**
  Privacy, latency, safety, reliability, and scalability.

---

## Limitation connected to thesis

This survey is not a web automation solution.

Use it to support:

```text
broad GUI-agent framing
```

but rely on web-agent papers for:

- DOM/HTML specifics,
- live-web evaluations,
- extraction tasks,
- and grounding results.

---

## Reading decision

- **Read fully?** No, selective reading is enough
- **Depth needed:** Selective-high
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Definitions
  - Frameworks
  - Data
  - Models
  - Evaluation
  - Applications
  - Challenges and roadmap

---

## One-sentence summary

This TMLR survey is the preferred broad reference for LLM-powered GUI agents and their architecture, data, models, evaluation, and challenges.

---

## BibTeX

```bibtex
@article{zhang2025llmbrained,
  title   = {Large Language Model-Brained GUI Agents: A Survey},
  author  = {Zhang, Chaoyun and He, Shilin and Qian, Jiaxu and Li, Bowen and Li, Liqun and Qin, Si and Kang, Yu and Ma, Minghua and Liu, Guyue and Lin, Qingwei and Rajmohan, Saravan and Zhang, Dongmei and Zhang, Qi},
  journal = {Transactions on Machine Learning Research},
  year    = {2025},
  eprint  = {2411.18279},
  archivePrefix = {arXiv},
  url     = {https://openreview.net/forum?id=xChvYjvXTp}
}
```

---

## Source links

- https://openreview.net/forum?id=xChvYjvXTp
- https://arxiv.org/abs/2411.18279
- https://github.com/vyokky/LLM-Brained-GUI-Agents-Survey


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2025-07 - GUI Agents- A Survey.md

# Paper 297 — GUI Agents: A Survey

## Metadata

- **Title:** GUI Agents: A Survey
- **Authors:** Dang Nguyen, Jian Chen, Yu Wang, Gang Wu, Namyong Park, Zhengmian Hu, Hanjia Lyu, Junda Wu, Ryan Aponte, Yu Xia, Xintong Li, Jing Shi, Hongjie Chen, Viet Dac Lai, Zhouhang Xie, Sungchul Kim, Ruiyi Zhang, Tong Yu, Mehrab Tanjim, Nesreen K. Ahmed, Puneet Mathur, Seunghyun Yoon, Lina Yao, Jihyung Kil, Branislav Kveton, Thien Huu Nguyen, Trung Bui, Tianyi Zhou, Ryan A. Rossi, Franck Dernoncourt
- **Year:** 2025
- **Venue:** Findings of the Association for Computational Linguistics: ACL 2025, pp. 22522–22538
- **DOI:** 10.18653/v1/2025.findings-acl.1158
- **arXiv ID:** arXiv:2412.13501
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 benchmarks; S5.2 perception; S5.3 reasoning/planning; S5.4 training; S5.5 open problems
- **Category:** SURVEY / GUI AGENTS / ACL FINDINGS
- **Paper type:** Survey
- **Priority:** P1
- **BibTeX key:** nguyen2025guiagents
- **Final publication status:** Final venue verified: Findings of ACL 2025.
- **Verification source:** https://aclanthology.org/2025.findings-acl.1158/

---

## Simple understanding

This survey defines **GUI agents** and formalizes GUI tasks.

The definition is useful:

```text
A GUI agent is an autonomous agent that interacts with digital platforms through graphical user interfaces by observing visual elements and acting through clicking, typing, tapping, or similar operations.
```

The paper also formulates GUI-agent tasks as sequential decision problems, often as a **POMDP**.

For the thesis, this is useful because web agents are a special case of GUI agents operating in browser environments.

---

## Notes

- **Core idea:**
  Survey GUI agents powered by foundation models and organize their benchmarks, architectures, training methods, and open challenges.

- **Key finding:**
  The survey emphasizes unique GUI-agent challenges: dynamic layouts, diverse graphical designs, grounding issues, and fine-grained recognition of small scattered elements.

- **Limitation:**
  It covers GUI agents broadly, not only web agents.

- **Additional limitation:**
  It is a survey, not a new system paper.

- **Additional limitation:**
  Use primary benchmark papers for detailed empirical claims.

- **Connects to:**
  GUI-agent definitions, POMDP formulation, datasets vs environments, open-world vs closed-world benchmarks, and capability taxonomies.

- **Use in thesis:**
  Use for formal definitions and benchmark/evaluation framing.

---

## Thesis-ready paragraph

Nguyen et al. survey GUI agents and provide a useful formal definition: a GUI agent autonomously interacts with digital platforms through graphical interfaces by observing visual elements and acting through operations such as clicking, typing, and tapping. The paper also frames GUI-agent tasks as sequential decision problems, often modeled as partially observable Markov decision processes. For this thesis, this formalization is valuable because web agents are a specific type of GUI agent operating in browser environments. The survey’s organization around benchmarks, architectures, training methods, and open problems helps situate web automation within the broader GUI-agent field, while primary web-agent papers remain necessary for detailed claims about DOM, HTML, and live-web behavior.

---

## Why this paper matters for my thesis

This paper matters because it gives formal language for the thesis.

You can define web agents as:

```text
GUI agents whose environment is the web/browser.
```

Then the web-agent problem becomes:

```text
partially observable state
sequential actions
changing environment
history-dependent policy
```

This supports the academic framing of web automation as a sequential decision-making problem.

---

## Important concepts to remember

### 1. GUI agent

An autonomous agent that interacts with digital systems through graphical user interfaces.

### 2. POMDP

A partially observable Markov decision process used to formalize GUI-agent tasks.

### 3. Dataset vs environment

A static collection of examples versus an interactive dynamic system.

### 4. Open-world benchmark

A benchmark where needed information can exist outside the benchmark.

### 5. Closed-world benchmark

A benchmark where all needed information is contained inside the benchmark.

### 6. Perception, reasoning, planning, acting

A capability view of GUI-agent systems.

---

## Key evidence from the paper

### Definition

Section 2 defines GUI agents and formalizes GUI-agent tasks.

### POMDP formulation

The paper models GUI tasks as sequential interaction under partial observability.

### Benchmark taxonomy

The survey distinguishes datasets from environments and open-world from closed-world benchmarks.

### Challenges

The introduction highlights dynamic layouts, diverse graphical designs, and grounding issues.

---

## Connection to earlier and later papers

### Connection to web agents

Web agents are GUI agents specialized to web browser environments.

### Connection to S5.1

The dataset/environment distinction is important for web-agent evaluation.

### Connection to S5.2

The grounding challenge directly relates to DOM/screenshot element selection.

---

## Connection to later thesis sections

- **S5.1 — Benchmarks:**
  Dataset vs environment, open-world vs closed-world.
- **S5.2 — Perception:**
  GUI perception and grounding.
- **S5.3 — Planning:**
  Sequential decision-making formulation.
- **S5.4 — Training:**
  Training methods for GUI agents.
- **S5.5 — Failure Modes:**
  Open challenges and failure sources.

---

## Limitation connected to thesis

This survey helps formalize the problem but does not solve web automation.

Use it for definitions and evaluation categories, not for detailed system claims.

---

## Reading decision

- **Read fully?** No, selective reading is enough
- **Depth needed:** Selective
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Definition of GUI agent
  - POMDP formulation
  - Benchmarks section
  - Architecture section
  - Training section
  - Open problems

---

## One-sentence summary

This survey provides a clean formal definition and decision-process framing for GUI agents, useful for positioning web agents in S4/S5.

---

## BibTeX

```bibtex
@inproceedings{nguyen2025guiagents,
  title     = {GUI Agents: A Survey},
  author    = {Nguyen, Dang and Chen, Jian and Wang, Yu and Wu, Gang and Park, Namyong and Hu, Zhengmian and Lyu, Hanjia and Wu, Junda and Aponte, Ryan and Xia, Yu and Li, Xintong and Shi, Jing and Chen, Hongjie and Lai, Viet Dac and Xie, Zhouhang and Kim, Sungchul and Zhang, Ruiyi and Yu, Tong and Tanjim, Mehrab and Ahmed, Nesreen K. and Mathur, Puneet and Yoon, Seunghyun and Yao, Lina and Kil, Jihyung and Kveton, Branislav and Nguyen, Thien Huu and Bui, Trung and Zhou, Tianyi and Rossi, Ryan A. and Dernoncourt, Franck},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
  pages     = {22522--22538},
  year      = {2025},
  publisher = {Association for Computational Linguistics},
  doi       = {10.18653/v1/2025.findings-acl.1158},
  url       = {https://aclanthology.org/2025.findings-acl.1158/}
}
```

---

## Source links

- Not provided in uploaded text


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2025-08 - A Survey of WebAgents- Towards Next-Generation AI Agents for Web Automation with Large Foundation Models.md

# Paper 298 — A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models

## Metadata

- **Title:** A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models
- **Authors:** Liangbo Ning, Ziran Liang, Zhuohang Jiang, Haohao Qu, Yujuan Ding, Wenqi Fan, Xiao-yong Wei, Shanru Lin, Hui Liu, Philip S. Yu, Qing Li
- **Year:** 2025
- **Venue:** Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining, KDD 2025 Tutorial & Survey Track, pp. 6140–6150
- **DOI:** 10.1145/3711896.3736555
- **arXiv ID:** arXiv:2503.23350
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 evaluation; S5.2 perception; S5.3 planning/reasoning/execution; S5.4 training/data; S7 trustworthiness; S8 future directions
- **Category:** SURVEY / WEBAGENTS / LFM-BASED WEB AUTOMATION
- **Paper type:** WebAgents survey
- **Priority:** P1
- **BibTeX key:** ning2025surveywebagents
- **Final publication status:** Final venue verified: KDD 2025 Tutorial & Survey Track conference paper; arXiv is the long version.
- **Verification source:** https://doi.org/10.1145/3711896.3736555

---

## Simple understanding

This is the most directly relevant survey for your thesis because it focuses specifically on **WebAgents**.

It reviews web agents from three major perspectives:

```text
architecture
training
trustworthiness
```

It also breaks the web-agent pipeline into:

```text
perception
planning & reasoning
execution
```

For the thesis, this paper is very useful as a roadmap for S4, S5, S7, and S8.

---

## Notes

- **Core idea:**
  Survey large-foundation-model-based WebAgents for web automation, focusing on architectures, training, and trustworthiness.

- **Key finding:**
  The survey frames WebAgents as agents that perceive web environments, reason over action sequences, and execute interactions to complete user instructions.

- **Limitation:**
  It is a survey, so primary papers are still needed for exact system performance.

- **Additional limitation:**
  The field changes quickly, so later systems may not be covered.

- **Additional limitation:**
  It may include broad web applications beyond the exact focus of generalized web automation and data extraction.

- **Connects to:**
  Perception, planning/reasoning, execution, training, data, safety, robustness, privacy, and generalizability.

- **Use in thesis:**
  Use as a key web-specific survey reference and roadmap.

---

## Thesis-ready paragraph

Ning et al. provide a focused survey of WebAgents, defined as large-foundation-model-empowered agents that complete web tasks by perceiving web environments, reasoning over action sequences, and executing interactions. The survey organizes the literature around architectures, training, and trustworthiness, making it highly relevant to a thesis on LLM-based agents for generalized web automation and data extraction. Its architecture breakdown—perception, planning and reasoning, and execution—maps directly onto the technical challenges identified in S4. Its training and trustworthiness sections also support later discussions of data, fine-tuning, post-training, safety, robustness, privacy, and generalization. As a survey, it should guide structure and coverage, while primary papers should support detailed empirical claims.

---

## Why this paper matters for my thesis

This paper matters because it is directly about your thesis domain.

It gives the clean web-agent pipeline:

```text
perception → planning/reasoning → execution
```

And it gives the broader study dimensions:

```text
architecture
training
trustworthiness
```

This can help structure your thesis chapters or subsections.

---

## Important concepts to remember

### 1. WebAgent

An AI agent that automates web tasks according to user instructions.

### 2. Perception

Observing website state using screenshots, HTML, DOM, and previous actions.

### 3. Planning and reasoning

Generating action sequences to complete tasks.

### 4. Execution

Interacting with the website through browser actions or tools.

### 5. Training

Prompting, pretraining, fine-tuning, post-training, and data construction.

### 6. Trustworthiness

Safety, robustness, privacy, and generalizability.

---

## Key evidence from the paper

### Figure 1

Illustrates WebAgents perceiving, reasoning, and executing web tasks.

### Architecture section

Reviews perception, planning/reasoning, and execution.

### Training section

Covers data and training strategies for WebAgents.

### Trustworthiness section

Covers safety, robustness, privacy, and generalizability.

---

## Connection to earlier and later papers

### Connection to S4

This survey summarizes the web-agent evolution that S4 traces historically.

### Connection to S5

Its perception/planning/execution structure maps directly onto S5 technical sections.

### Connection to S7

Its trustworthiness section supports safety, privacy, robustness, and generalization discussion.

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  Benchmarks and metrics.
- **S5.2 — Perception:**
  HTML, DOM, screenshots, and observation design.
- **S5.3 — Planning/Reasoning/Execution:**
  Action sequence generation and web interaction.
- **S5.4 — Training:**
  Data, prompting, fine-tuning, post-training.
- **S7 — Trustworthiness:**
  Safety, robustness, privacy, generalizability.
- **S8 — Future directions:**
  Deployment and open challenges.

---

## Limitation connected to thesis

This survey is a roadmap, not a primary system.

Use it to organize the field, but support detailed claims with:

```text
World of Bits
WebGPT
WebShop
WebAgent
SeeAct
WebVoyager
AutoWebGLM
WALT
```


---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High but selective
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Introduction
  - Architecture section
  - Training section
  - Trustworthiness section
  - Future directions

---

## One-sentence summary

This WebAgents survey is a key structure paper for the thesis because it directly organizes web automation agents around architecture, training, and trustworthiness.

---

## BibTeX

```bibtex
@inproceedings{ning2025surveywebagents,
  title     = {A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models},
  author    = {Ning, Liangbo and Liang, Ziran and Jiang, Zhuohang and Qu, Haohao and Ding, Yujuan and Fan, Wenqi and Wei, Xiao-yong and Lin, Shanru and Liu, Hui and Yu, Philip S. and Li, Qing},
  booktitle = {Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  pages     = {6140--6150},
  year      = {2025},
  publisher = {Association for Computing Machinery},
  doi       = {10.1145/3711896.3736555},
  eprint    = {2503.23350},
  archivePrefix = {arXiv},
  url       = {https://doi.org/10.1145/3711896.3736555}
}
```

---

## Source links

- https://arxiv.org/abs/2503.23350


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\2025-09 - WALT- Web Agents that Learn Tools.md

# Paper 299 — WALT: Web Agents that Learn Tools

## Metadata

- **Title:** WALT: Web Agents that Learn Tools
- **Authors:** Viraj Prabhu, Yutong Dai, Matthew Fernandez, Jing Gu, Krithika Ramakrishnan, Yanqi Luo, Silvio Savarese, Caiming Xiong, Junnan Li, Zeyuan Chen, Ran Xu
- **Year:** 2025
- **Venue:** International Conference on Learning Representations (ICLR 2026), Poster
- **DOI:** 10.48550/arXiv.2510.01524
- **arXiv ID:** arXiv:2510.01524
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.2 site-function abstraction; S5.3 tool-based planning; S5.4 tool learning; S5.5 brittle UI-action failures; S6 extraction/tools; S8 efficient deployment
- **Category:** WEB AGENT / TOOL LEARNING / ACTION ABSTRACTION
- **Paper type:** Method / tool-learning web agent
- **Priority:** P1
- **BibTeX key:** prabhu2025walt
- **Final publication status:** Final venue verified: ICLR 2026 Poster.
- **Verification source:** https://openreview.net/forum?id=cgIDqcJcoI

---

## Simple understanding

WALT is a forward-looking web-agent paper that shifts from step-by-step UI actions to **learned website tools**.

Most web agents operate like this:

```text
click → type → click → scroll → click → inspect → click
```

WALT argues that humans often think at a higher level:

```text
search(query)
filter(criteria)
sort(order)
create(listing)
edit(item)
delete(item)
comment(text)
upvote(item)
```

The system reverse-engineers website-provided functionality into reusable invocable tools. These tools expose robust functions already built into websites.

For my thesis, WALT matters because it suggests a next-generation direction for web automation: agents should not always reason over primitive clicks; they should discover and call higher-level website tools when possible.

---

## Notes

- **Core idea:**
  Reverse-engineer website functionality into reusable invocable tools, reducing brittle step-by-step UI reasoning.

- **Key finding:**
  WALT reports state-of-the-art success on WebArena and VisualWebArena, with fewer steps and less LLM-dependent reasoning.

- **Limitation:**
  Tool discovery must be performed per website and may require expensive upfront exploration.

- **Additional limitation:**
  Learned tools can break when websites change.

- **Additional limitation:**
  Reverse-engineering URL parameters or hidden functionality may raise security, privacy, or terms-of-service concerns.

- **Additional limitation:**
  Tool abstraction helps repeated functions but may not help rare one-off interactions.

- **Connects to:**
  Toolformer, MRKL, WebArena, VisualWebArena, skill discovery, API-using agents, and deployment efficiency.

- **Use in thesis:**
  Use as a forward-looking paper showing the transition from primitive UI actions to site-level tool abstraction.

---

## Thesis-ready paragraph

Prabhu et al. introduce WALT, a framework for web agents that learn reusable tools by reverse-engineering website-provided functionality. Instead of executing long fragile sequences of primitive UI actions, WALT exposes high-level operations such as search, filter, sort, create, edit, delete, comment, or upvote as callable tools with validated schemas. This is highly relevant to generalized web automation because it shifts the burden from step-by-step UI interaction toward robust, reusable site-level abstractions. WALT’s results on WebArena and VisualWebArena suggest that tool-based abstraction can improve success and efficiency. However, the approach also introduces new challenges: tools must be discovered, validated, maintained, and used safely as websites change. For this thesis, WALT provides an important future direction: combining LLM planning with learned website-specific tools for more reliable automation.

---

## Why this paper matters for my thesis

This paper matters because it addresses one of the biggest practical problems in web automation:

```text
primitive UI trajectories are brittle
```

A small website change can break:

```text
click element 4 → type → click element 9
```

But a high-level tool can be more stable:

```text
search(query="blue kayak", category="Boats", sort_by="price")
```

For data extraction, this is important because many websites already provide useful functions:

```text
search
filter
sort
export
download
next page
open details
```

A future web agent should discover and use these functions instead of always clicking manually.

---

## Important concepts to remember

### 1. Website-provided functionality

Built-in operations such as search, filter, sort, post, edit, delete, comment, or vote.

### 2. Tool discovery

Identifying reusable site functions and exposing them as callable tools.

### 3. Demonstrate-generate-validate loop

Explore functionality, generate tools, then test and validate them.

### 4. URL-parameter promotion

Replacing UI sequences with robust URL/API-like parameterized operations when possible.

### 5. Tool-based abstraction

Replacing many primitive UI steps with one high-level operation.

### 6. Agentic fallback

Using limited agentic steps when deterministic tool execution is insufficient.

---

## Key evidence from the paper

### Figure 1

Contrasts fragile primitive UI action sequences with one high-level tool call.

### Tool coverage

The paper describes tools for discovery, communication, and content management.

### Reported results

The paper reports strong results on WebArena and VisualWebArena.

### Efficiency

It reports fewer steps on average and improved success through discovered tools, multimodal DOM parsing, and external verification.

---

## Connection to earlier and later papers

### Connection to Toolformer

Toolformer teaches models to use tools.

WALT discovers website-specific tools for web automation.

```text
Toolformer = language model learns API calls
WALT = web agent learns site tools
```

### Connection to MRKL

MRKL argues for modular expert systems.

WALT creates website-specific modules/tools.

### Connection to WebAgent and AutoWebGLM

WebAgent/AutoWebGLM operate through programmatic actions or trained policies.

WALT abstracts common website functionality into reusable tools.

---

## Connection to later thesis sections

- **S5.2 — Representation:**
  Website-function abstraction and action representation.
- **S5.3 — Planning:**
  Planning over tools instead of primitive UI actions.
- **S5.4 — Training/Learning:**
  Tool discovery and validation.
- **S5.5 — Failure Modes:**
  Brittle UI trajectories and maintenance failure.
- **S6 — Extraction:**
  Website tools for search, filtering, sorting, and data access.
- **S8 — Deployment:**
  Tool maintenance, monitoring, efficiency, and safety.

---

## Limitation connected to thesis

WALT is promising but introduces a new maintenance problem.

It improves:

```text
primitive UI actions → reusable site tools
```

but it still needs:

- safe tool discovery,
- validation,
- monitoring after website changes,
- permission and privacy controls,
- fallback actions,
- and extraction verification.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Figure 1
  - Tool discovery method
  - Demonstrate-generate-validate loop
  - WebArena results
  - VisualWebArena results
  - Ablations
  - Limitations

---

## One-sentence summary

WALT reframes web automation from brittle UI-step reasoning to reusable website-tool invocation, but tool discovery and maintenance become new deployment challenges.

---

## BibTeX

```bibtex
@inproceedings{prabhu2026walt,
  title     = {WALT: Web Agents that Learn Tools},
  author    = {Prabhu, Viraj and Dai, Yutong and Fernandez, Matthew and Gu, Jing and Ramakrishnan, Krithika and Luo, Yanqi and Savarese, Silvio and Xiong, Caiming and Li, Junnan and Chen, Zeyuan and Xu, Ran},
  booktitle = {International Conference on Learning Representations},
  year      = {2026},
  eprint    = {2510.01524},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  doi       = {10.48550/arXiv.2510.01524},
  url       = {https://openreview.net/forum?id=cgIDqcJcoI},
  note      = {ICLR 2026 Poster}
}
```

---

## Source links

- https://arxiv.org/abs/2510.01524


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_final_verified_reading_index.md

# S4 P1 Final Verified Markdown Notes — Reading Index

This folder contains the final S4 P1 markdown notes with venue/status metadata re-checked online one by one.

## Final venue/status table

| Paper | Final venue/status | Prefer for final thesis citation? |
|---|---|---|
| Workflow-Guided Exploration | ICLR 2018 conference paper | Yes |
| DOM-Q-NET | ICLR 2019 conference paper | Yes |
| WebAgent | ICLR 2024 conference paper | Yes |
| Large Language Model Powered Agents in the Web | WWW 2024 Companion tutorial paper | Context only |
| AutoWebGLM Bootstrap and Reinforce | arXiv extended/preprint version | No — prefer KDD 2024 version |
| Agent S | ICLR 2025 Poster | Yes |
| AutoGLM | arXiv preprint | Use as preprint unless a later venue appears |
| LLM-Brained GUI Agents survey preprint | arXiv preprint | No — prefer TMLR 2025 version |
| AutoWebGLM | KDD 2024 conference paper | Yes |
| GUI Agents with Foundation Models | arXiv preprint | Use as preprint |
| A Survey on (M)LLM-Based GUI Agents | arXiv preprint | Use as preprint |
| LLM-Brained GUI Agents survey | TMLR 2025 | Yes |
| GUI Agents: A Survey | Findings of ACL 2025 | Yes |
| A Survey of WebAgents | KDD 2025 Tutorial & Survey Track | Yes |
| WALT | ICLR 2026 Poster | Yes |

## Suggested reading order

```text
Pre-LLM/RL web agents:
285 WGE → 286 DOM-Q-NET

Real-world LLM web agents:
287 WebAgent → 293 AutoWebGLM KDD → 289 AutoWebGLM preprint only as extra detail

Broader GUI/computer-use agents:
290 Agent S → 291 AutoGLM

Survey/context papers:
288 WWW tutorial → 296 TMLR GUI survey → 297 ACL GUI survey → 298 KDD WebAgents survey
Optional/secondary: 292 preprint survey, 294 GUI foundation survey, 295 (M)LLM GUI survey

Forward-looking tool abstraction:
299 WALT
```

## Files

- `2018-02 - Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration.md`
- `2019-02 - DOM-Q-NET- Grounded RL on Structured Language.md`
- `2023-07 - A Real-World WebAgent with Planning Long Context Understanding and Program Synthesis.md`
- `2024-05 - Large Language Model Powered Agents in the Web.md`
- `2024-10 - AutoWebGLM- Bootstrap and Reinforce A Large Language Model-based Web Navigating Agent.md`
- `2024-10 - Agent S- An Open Agentic Framework that Uses Computers Like a Human.md`
- `2024-10 - AutoGLM Autonomous Foundation Agents for GUIs.md`
- `2024-11 - Large Language Model-Brained GUI Agents- A Survey - preprint version.md`
- `2024-12 - AutoWebGLM A Large Language Model-based Web Navigating Agent.md`
- `2025-02 - GUI Agents with Foundation Models- A Comprehensive Survey.md`
- `2025-06 - A Survey on (M)LLM-Based GUI Agents.md`
- `2025-06 - Large Language Model-Brained GUI Agents- A Survey.md`
- `2025-07 - GUI Agents- A Survey.md`
- `2025-08 - A Survey of WebAgents- Towards Next-Generation AI Agents for Web Automation with Large Foundation Models.md`
- `2025-09 - WALT- Web Agents that Learn Tools.md`

---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2018-02 - Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration.md

# Paper 285 — Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration

## Metadata

- **Title:** Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration
- **Authors:** Evan Zheran Liu, Kelvin Guu, Panupong Pasupat, Tianlin Shi, Percy Liang
- **Year:** 2018
- **Venue:** International Conference on Learning Representations (ICLR 2018)
- **DOI:** 10.48550/arXiv.1802.08802
- **arXiv ID:** arXiv:1802.08802
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 benchmarks; S5.2 interface representation; S5.3 exploration/planning; S5.4 demonstrations/RL; S5.5 sparse-reward failure modes
- **Category:** WEB-RL / WORKFLOW-GUIDED EXPLORATION / MINIWOB
- **Paper type:** Method / RL training strategy for web interfaces
- **Priority:** P1
- **BibTeX key:** liu2018reinforcement

---

## Simple understanding

This paper is a pre-LLM web-agent paper that tries to solve a key problem in browser automation: **sparse reward exploration**.

In many web tasks, the agent only receives reward after completing the whole task. For example, if the goal is to fill a form and submit it, the agent may need many correct clicks and typed values before seeing any success signal. Random exploration is therefore very inefficient.

The paper proposes **Workflow-Guided Exploration (WGE)**. Instead of directly cloning expert demonstrations, the method extracts abstract workflows from demonstrations. A workflow is a high-level action pattern such as:

```text
click textbox → type value → click submit
```

The RL agent then explores within this workflow structure. This reduces the search space while still allowing the agent to discover successful concrete actions.

For my thesis, the paper matters because it shows an early solution to the same problem that later LLM web agents face: how to avoid blind exploration in a huge web-action space. Later systems use language plans, ReAct traces, memory, and tool abstractions for similar reasons.

---

## Notes

- **Core idea:**
  Use expert demonstrations to infer abstract workflows that constrain reinforcement-learning exploration on web interfaces.

- **Key finding:**
  Workflow-guided exploration improves sample efficiency over behavioral cloning and achieves strong results on MiniWoB-style web tasks using only a small number of demonstrations per task.

- **Limitation:**
  The method still requires expert demonstrations. For generalized web automation, this matters because demonstrations cannot realistically be collected for every website, workflow, and extraction schema.

- **Additional limitation:**
  The workflows are derived from previous trajectories, so they may not generalize to unseen layouts or new task structures. For web agents, this motivates LLM-based reasoning and planning rather than relying only on fixed workflow templates.

- **Additional limitation:**
  The approach remains RL-based and has limited natural-language reasoning. For the thesis, this explains why pre-LLM web agents struggled with open-ended user instructions.

- **Additional limitation:**
  Grounding remains difficult: the agent still has to map abstract steps to concrete elements, clicks, and typed values.

- **Connects to:**
  World of Bits, DOM-Q-NET, MiniWoB, imitation learning, RL for web interfaces, AutoWebGLM, and training-based web agents.

- **Use in thesis:**
  Use this paper to show that demonstration-guided exploration was an important pre-LLM strategy for web automation, and that sparse reward remains a core challenge.

---

## Thesis-ready paragraph

Liu et al. proposed Workflow-Guided Exploration, a reinforcement-learning method for web-interface agents that uses expert demonstrations to constrain exploration without forcing exact imitation. From each demonstration, the method induces abstract workflows that define plausible classes of actions, then trains an agent to explore within this reduced action space. This is important for the evolution of web agents because it shows that web automation is difficult not only because of perception, but also because of sparse rewards and large action spaces. For LLM-based web automation, WGE is an early precursor to later planning and demonstration-based approaches: it uses human demonstrations to guide search, while later LLM agents use language reasoning, trajectories, and memory to guide action selection. However, WGE remains limited by demonstration dependence, low-level action grounding, and weak generalization to arbitrary real websites.

---

## Why this paper matters for my thesis

This paper matters because web automation often fails when the agent explores blindly.

A website may require:

```text
click the correct field
type the correct value
select the correct option
click submit
wait for response
verify success
```

If the reward appears only after the final step, random RL rarely succeeds. WGE shows that demonstrations can provide structure:

```text
demonstration → abstract workflow → guided exploration → successful trajectories
```

For the thesis, this is useful because modern LLM web agents still need guidance. The guidance may come from prompts, demonstrations, memories, self-reflections, learned policies, or tools, but the underlying reason is the same: web action spaces are too large for unguided exploration.

---

## Important concepts to remember

### 1. Workflow

An abstract pattern of action types derived from demonstrations.

### 2. Workflow lattice

A compact representation of possible workflows consistent with a demonstration.

### 3. Workflow-guided exploration

RL exploration constrained to actions allowed by an inferred workflow.

### 4. Behavioral cloning

Supervised imitation of human demonstrations.

### 5. Sparse reward

A reward signal that appears only after the whole task succeeds.

### 6. MiniWoB

A benchmark suite of small web tasks introduced in the World of Bits ecosystem.

---

## Key evidence from the paper

### WGE pipeline

The paper presents a pipeline where demonstrations generate workflow lattices, RL explores within them, successful trajectories are stored, and a policy is trained from successful episodes.

### Sample efficiency

The paper emphasizes that WGE improves sample efficiency compared with standard behavioral cloning and unguided RL.

### MiniWoB results

The method is evaluated on web-interface tasks from the MiniWoB setting, connecting directly to the early web-agent benchmark line.

### Thesis-relevant result

The key evidence is not only the numerical improvement, but the diagnosis: web tasks need structured exploration because sparse rewards and low-level actions are hard.

---

## Connection to earlier and later papers

### Connection to World of Bits

World of Bits introduces the web as an environment for agents.

WGE improves the training strategy inside this kind of environment by using demonstrations to guide exploration.

```text
World of Bits = environment
WGE = better exploration method for that environment
```

### Connection to DOM-Q-NET

DOM-Q-NET focuses on DOM representation.

WGE focuses on exploration.

Together, they show two pre-LLM needs:

```text
represent the page well
explore the action space efficiently
```

### Connection to LLM web agents

LLM agents later reduce exploration difficulty through:

```text
language reasoning
task decomposition
tool calls
memory
self-reflection
structured prompts
```

WGE is an early non-LLM version of that idea.

---

## Connection to later thesis sections

- **S5.1 — Benchmarks and Evaluation:**
  MiniWoB and early task success metrics.
- **S5.3 — Planning and Decision-Making:**
  Workflow constraints as an early planning/exploration mechanism.
- **S5.4 — Training Strategies:**
  Demonstrations, behavioral cloning, and reinforcement learning.
- **S5.5 — Failure Modes:**
  Sparse reward, overfitting to demonstrations, and exploration failure.

---

## Limitation connected to thesis

Workflow-Guided Exploration improves RL training, but it does not solve generalized web automation.

For my thesis, the full web-agent loop is:

```text
instruction → page observation → grounding → planning → action → feedback → recovery → extraction → verification
```

WGE mainly improves:

```text
demonstration → workflow → exploration
```

It does not fully solve:

- natural-language instruction understanding,
- generalization to unseen sites,
- robust DOM/visual grounding,
- dynamic website behavior,
- structured data extraction,
- or safe autonomous execution.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Introduction
  - Workflow definition
  - Workflow-guided exploration algorithm
  - MiniWoB experiments
  - Comparison with behavioral cloning
  - Limitations

---

## One-sentence summary

Workflow-Guided Exploration shows that demonstrations can guide sparse-reward web RL, but generalized web automation still needs language reasoning, robust grounding, and cross-site generalization.

---

## BibTeX

```bibtex
@inproceedings{liu2018reinforcement,
  title     = {Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration},
  author    = {Liu, Evan Zheran and Guu, Kelvin and Pasupat, Panupong and Shi, Tianlin and Liang, Percy},
  booktitle = {International Conference on Learning Representations},
  year      = {2018},
  eprint    = {1802.08802},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  doi       = {10.48550/arXiv.1802.08802}
}
```

---

## Source links

- https://arxiv.org/abs/1802.08802


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2019-02 - DOM-Q-NET- Grounded RL on Structured Language.md

# Paper 286 — DOM-Q-NET: Grounded RL on Structured Language

## Metadata

- **Title:** DOM-Q-NET: Grounded RL on Structured Language
- **Authors:** Sheng Jia, Jamie Kiros, Jimmy Ba
- **Year:** 2019
- **Venue:** International Conference on Learning Representations (ICLR 2019)
- **DOI:** 10.48550/arXiv.1902.07257
- **arXiv ID:** arXiv:1902.07257
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 MiniWoB evaluation; S5.2 DOM representation; S5.4 RL/multitask learning; S5.5 large variable action-space failure
- **Category:** WEB-RL / DOM REPRESENTATION / GRAPH NEURAL NETWORK
- **Paper type:** Method / RL architecture
- **Priority:** P1
- **BibTeX key:** jia2019domqnet

---

## Simple understanding

This paper introduces **DOM-Q-NET**, a reinforcement-learning architecture for web navigation.

The central idea is that a webpage should not be represented only as pixels or flat text. A webpage has structure: the HTML document is a **DOM tree**. Buttons, inputs, labels, tables, links, and containers are arranged in a hierarchy.

DOM-Q-NET uses a graph neural network to represent this DOM structure. It then learns Q-values for different types of actions, such as clicking and typing.

For my thesis, the paper matters because DOM representation is still one of the central problems in LLM web agents. Even modern agents must decide which DOM element corresponds to a user instruction or visual target.

---

## Notes

- **Core idea:**
  Represent the webpage as a DOM graph and use graph neural networks with factorized Q-functions to learn grounded web actions.

- **Key finding:**
  DOM-Q-NET performs competitively on MiniWoB tasks without expert demonstrations and improves sample efficiency in multi-task training.

- **Limitation:**
  The evaluation is mainly on MiniWoB-like tasks, which are much simpler than live websites.

- **Additional limitation:**
  The model lacks LLM-style natural-language reasoning and cannot flexibly interpret complex user instructions.

- **Additional limitation:**
  DOM structure helps but does not solve visual layout grounding; many real websites require both DOM and screenshot understanding.

- **Additional limitation:**
  The action space remains restricted compared with arbitrary browser operations.

- **Connects to:**
  World of Bits, WGE, HTML-T5, WebAgent, AutoWebGLM, Mind2Web, and modern DOM-aware LLM agents.

- **Use in thesis:**
  Use as a key pre-LLM DOM grounding paper showing why structured page representation is essential.

---

## Thesis-ready paragraph

Jia et al. introduced DOM-Q-NET, a reinforcement-learning architecture for web navigation that explicitly represents webpages through their DOM structure. By using graph neural networks over DOM nodes and factorizing Q-functions over action categories, DOM-Q-NET addresses the variable and structured action space of web interfaces. This paper is important for the evolution of web agents because it establishes the DOM as a central representation for grounding actions. Although the method predates LLM agents and is evaluated on simplified MiniWoB tasks, the problem it addresses remains fundamental: a web agent must map instructions and decisions to concrete webpage elements. Its limitations motivate later HTML-aware, multimodal, and LLM-based web agents that combine structural DOM representations with language reasoning and visual grounding.

---

## Why this paper matters for my thesis

This paper matters because a web agent needs to know **where to act**.

A webpage is not a simple text document. It contains:

```text
buttons
forms
links
tables
dropdowns
hidden elements
nested containers
labels
attributes
```

The DOM gives the agent structure.

For example, if the instruction is:

```text
Click the search button.
```

the agent must identify the right DOM node among many possible clickable elements.

DOM-Q-NET is an early attempt to solve this with deep RL and graph neural networks. Modern LLM agents often use different models, but they still face the same grounding problem.

---

## Important concepts to remember

### 1. DOM tree

The browser's structured representation of the HTML document.

### 2. Grounded RL

RL where actions correspond to actual interface elements.

### 3. Graph neural network

A neural network that propagates information across linked DOM nodes.

### 4. Factorized Q-function

A Q-value design split across action categories.

### 5. Variable action space

The set of possible actions changes depending on the webpage state.

### 6. Multi-task training

Training across several web tasks to improve generalization.

---

## Key evidence from the paper

### Motivation

The paper highlights that web navigation has large discrete action spaces and a changing number of valid actions.

### DOM representation

The model uses DOM graph structure instead of treating the page only as pixels.

### MiniWoB evaluation

It evaluates on MiniWoB tasks, linking it to the World of Bits benchmark line.

### Sample efficiency

The paper reports improved sample efficiency in multi-task settings.

---

## Connection to earlier and later papers

### Connection to World of Bits

World of Bits introduced pixel + DOM observations.

DOM-Q-NET makes DOM structure the central modeling object.

### Connection to WebAgent and AutoWebGLM

WebAgent and AutoWebGLM later continue the DOM/HTML representation line, but with LLMs and HTML simplification.

```text
DOM-Q-NET: DOM graph + RL
WebAgent: long HTML + HTML-T5 + program synthesis
AutoWebGLM: simplified HTML + trained LLM policy
```

### Connection to SeeAct and WebVoyager

SeeAct and WebVoyager show that DOM alone is not enough. Visual screenshots and element labels are also important.

---

## Connection to later thesis sections

- **S5.2 — Perception and Grounding:**
  DOM representation and element selection.
- **S5.4 — Training Strategies:**
  RL and multi-task learning on web tasks.
- **S5.5 — Failure Modes:**
  Large variable action spaces and incorrect element grounding.
- **S8 — Deployment:**
  Gap between simplified DOM benchmarks and live websites.

---

## Limitation connected to thesis

DOM-Q-NET improves structured web representation, but it does not solve generalized web automation.

It mainly improves:

```text
webpage representation → DOM-based action selection
```

It does not solve:

- complex natural-language instructions,
- live dynamic websites,
- visual layout understanding,
- long-horizon planning,
- structured extraction verification,
- or safe web action execution.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Medium-high
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Problem formulation
  - DOM graph representation
  - Action factorization
  - MiniWoB experiments
  - Multi-task results
  - Limitations

---

## One-sentence summary

DOM-Q-NET shows that DOM structure is a useful inductive bias for web agents, but RL on simplified DOM tasks is not sufficient for generalized web automation.

---

## BibTeX

```bibtex
@inproceedings{jia2019domqnet,
  title     = {DOM-Q-NET: Grounded RL on Structured Language},
  author    = {Jia, Sheng and Kiros, Jamie and Ba, Jimmy},
  booktitle = {International Conference on Learning Representations},
  year      = {2019},
  eprint    = {1902.07257},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  doi       = {10.48550/arXiv.1902.07257}
}
```

---

## Source links

- https://arxiv.org/abs/1902.07257


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2023-07 - A Real-World WebAgent with Planning Long Context Understanding and Program Synthesis.md

# Paper 287 — A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis

## Metadata

- **Title:** A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis
- **Authors:** Izzeddin Gur, Hiroki Furuta, Austin Huang, Mustafa Safdari, Yutaka Matsuo, Douglas Eck, Aleksandra Faust
- **Year:** 2024
- **Venue:** International Conference on Learning Representations (ICLR 2024)
- **DOI:** 10.48550/arXiv.2307.12856
- **arXiv ID:** arXiv:2307.12856
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.2 long HTML/interface representation; S5.3 planning; S5.4 self-experience training; S6 extraction/program synthesis; S8 real-web deployment
- **Category:** WEB-LLM / REAL-WORLD WEB AGENT / HTML-T5 / PROGRAM SYNTHESIS
- **Paper type:** System / modular LLM web agent
- **Priority:** P1
- **BibTeX key:** gur2024realworld

---

## Simple understanding

This paper introduces **WebAgent**, a real-world LLM-based web automation system.

The key problem is that real websites are much harder than simulated environments. Real pages have:

```text
long messy HTML
dynamic content
irrelevant boilerplate
no fixed action space
many clickable elements
task-specific structure
```

The paper proposes a modular solution:

```text
user instruction
→ planning into sub-instructions
→ long HTML summarization
→ task-relevant snippets
→ Python program synthesis
→ browser action
```

The system uses **HTML-T5** for HTML understanding and summarization, and a language model for generating executable Python programs.

For my thesis, this paper matters because it directly targets real-world web automation and shows why long-context HTML understanding and programmatic actions are important.

---

## Notes

- **Core idea:**
  Build a real-world web agent by combining planning, long HTML summarization, and program synthesis.

- **Key finding:**
  The paper reports improved real-world web success and strong results on MiniWoB++ and Mind2Web-style tasks, showing that HTML-specialized models help web automation.

- **Limitation:**
  The system depends on specialized components such as HTML-T5 and program synthesis, increasing engineering complexity.

- **Additional limitation:**
  HTML summarization may remove task-relevant elements. For extraction, this can cause missing fields or wrong outputs.

- **Additional limitation:**
  Generated Python actions are powerful but risky. For deployment, program synthesis must be sandboxed and verified.

- **Additional limitation:**
  The approach emphasizes HTML more than visual layout, but many modern webpages require screenshot-level reasoning.

- **Connects to:**
  DOM-Q-NET, WebGPT, WebShop, Mind2Web, AutoWebGLM, WebVoyager, and program-synthesis web automation.

- **Use in thesis:**
  Use as a major real-world web-agent paper showing that real web automation requires long HTML handling, planning, and executable action generation.

---

## Thesis-ready paragraph

Gur et al. introduced WebAgent, a modular LLM-based system for real-world web automation that combines planning, long-context HTML understanding, and program synthesis. The system decomposes natural-language instructions into sub-instructions, summarizes long HTML pages into task-relevant snippets using HTML-T5, and generates executable Python programs to interact with websites. This work is important because it directly addresses the limitations of simulated web benchmarks: real websites have open-ended action spaces, long noisy HTML, and no predefined set of clickable actions. For generalized web automation and data extraction, WebAgent shows that LLM agents need specialized web representations and executable action mechanisms. However, it also reveals major open issues: summarization can omit relevant information, generated code must be constrained, and real websites remain dynamic and difficult to evaluate robustly.

---

## Why this paper matters for my thesis

This paper matters because it moves from simplified benchmarks to real websites.

A real webpage may have:

```text
50,000+ HTML tokens
ads
menus
hidden elements
scripts
forms
irrelevant sections
duplicated labels
```

A model cannot simply read everything naively.

WebAgent proposes:

```text
plan the task
compress the page
focus on relevant snippets
generate code to act
```

For data extraction, this is especially relevant because extraction requires selecting the right parts of the HTML and producing structured output.

---

## Important concepts to remember

### 1. HTML-T5

A model specialized for understanding and processing long HTML.

### 2. Long HTML summarization

Compressing page HTML into task-relevant snippets.

### 3. Program synthesis

Generating executable Python code to interact with a website.

### 4. Sub-instruction planning

Breaking a user instruction into smaller actionable steps.

### 5. Self-experience supervision

Using generated agent experience to improve web-model behavior.

### 6. Open-ended action space

Real websites do not provide a fixed set of actions.

---

## Key evidence from the paper

### Real vs simulated web

The paper contrasts real websites with simplified simulators, highlighting long HTML and open-ended actions.

### Architecture

The system combines HTML-T5 planning/summarization and program synthesis.

### HTML length

The paper emphasizes that real webpages have much longer HTML than benchmark simulators.

### Reported gains

The paper reports strong improvements in real-world web settings and HTML-based benchmarks.

---

## Connection to earlier and later papers

### Connection to DOM-Q-NET

DOM-Q-NET uses DOM graph structure.

WebAgent extends the representation problem to real long HTML.

```text
DOM-Q-NET = structured DOM for RL
WebAgent = long HTML understanding for LLM agents
```

### Connection to AutoWebGLM

Both systems simplify or transform HTML for web agents.

WebAgent uses HTML-T5 and program synthesis.

AutoWebGLM uses simplified HTML and trained web-navigation policies.

### Connection to WebVoyager

WebAgent is more HTML/program-oriented.

WebVoyager is more screenshot/multimodal-oriented.

Both address real websites.

---

## Connection to later thesis sections

- **S5.2 — Perception and Grounding:**
  Long HTML summarization and task-relevant snippet selection.
- **S5.3 — Planning:**
  Sub-instruction planning and action decomposition.
- **S5.4 — Training:**
  HTML-T5 specialization and self-experience supervision.
- **S6 — Extraction:**
  Programmatic extraction and structured web operations.
- **S8 — Deployment:**
  Risks of generated code and real-web variability.

---

## Limitation connected to thesis

WebAgent improves real-world web automation, but it is not a complete solution.

It mainly improves:

```text
planning + HTML compression + programmatic action
```

It does not fully solve:

- screenshot/visual grounding,
- safe execution of generated programs,
- dynamic website change,
- robust verification of extracted data,
- user privacy,
- or generalization to all websites.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Very high
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Figures comparing simulated and real websites
  - HTML-T5 method
  - Planning module
  - HTML summarization
  - Program synthesis
  - Real-world evaluation
  - Limitations

---

## One-sentence summary

WebAgent shows that real-world web automation requires planning, long HTML understanding, and program synthesis, but generated actions and compressed observations still need grounding, safety, and verification.

---

## BibTeX

```bibtex
@inproceedings{gur2024realworld,
  title     = {A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis},
  author    = {Gur, Izzeddin and Furuta, Hiroki and Huang, Austin and Safdari, Mustafa and Matsuo, Yutaka and Eck, Douglas and Faust, Aleksandra},
  booktitle = {International Conference on Learning Representations},
  year      = {2024},
  eprint    = {2307.12856},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  doi       = {10.48550/arXiv.2307.12856}
}
```

---

## Source links

- https://arxiv.org/abs/2307.12856


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2024-05 - Large Language Model Powered Agents in the Web.md

# Paper 288 — Large Language Model Powered Agents in the Web

## Metadata

- **Title:** Large Language Model Powered Agents in the Web
- **Authors:** Yang Deng, An Zhang, Yankai Lin, Xu Chen, Ji-Rong Wen, Tat-Seng Chua
- **Year:** 2024
- **Venue:** Companion Proceedings of the ACM Web Conference 2024
- **DOI:** 10.1145/3589335.3641240
- **arXiv ID:** Not listed
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S3 agent architecture; S4 web-agent scope; S5.3 planning; S6 web mining/recommender/conversational systems; S8 applications
- **Category:** TUTORIAL / WEB APPLICATIONS / LLM AGENTS
- **Paper type:** Tutorial paper / overview
- **Priority:** P1
- **BibTeX key:** deng2024llmpoweredweb

---

## Simple understanding

This paper is a **WWW 2024 tutorial paper** about LLM-powered agents in the web.

It is not a new system paper or benchmark. Its value is positioning: it explains that LLM-powered agents are becoming relevant across web applications, including:

```text
web mining
social networks
recommender systems
conversational systems
web automation
```

The paper describes LLM-agent architecture using modules such as:

```text
profile
memory
planning
action
```

For my thesis, this paper is useful as context. It helps position generalized web automation inside the broader WWW research community.

---

## Notes

- **Core idea:**
  Present a tutorial overview of LLM-powered agents in web applications and their architecture.

- **Key finding:**
  The tutorial argues that LLM agents can enhance web applications through memory, planning, reasoning, and autonomous action.

- **Limitation:**
  It is a tutorial/overview, not a new empirical system paper.

- **Additional limitation:**
  It is broad across web applications and does not deeply analyze DOM grounding, browser control, or extraction verification.

- **Additional limitation:**
  Use it for positioning, not for detailed performance claims.

- **Connects to:**
  LLM agents, recommender systems, web mining, social networks, conversational systems, and web automation.

- **Use in thesis:**
  Use briefly to show that LLM agents are recognized as an important topic in the Web/WWW research community.

---

## Thesis-ready paragraph

Deng et al. present a WWW 2024 tutorial on large-language-model-powered agents in the web. The paper positions LLM agents as a broad paradigm for enhancing web applications through profiling, memory, planning, and action. It discusses applications beyond browser control, including web mining, social networks, recommender systems, and conversational systems. For this thesis, the paper is useful as contextual support because it shows that LLM-based agents are becoming important across the web research ecosystem. However, because it is a short tutorial paper rather than a full system or benchmark, it should not be used as primary evidence for technical claims about web automation performance, grounding, or extraction.

---

## Why this paper matters for my thesis

This paper matters mainly for positioning.

Your thesis is about:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper helps show that the broader web community is also moving toward:

```text
LLM agents + web applications
```

It is useful in the introduction or S4 framing, but it should not replace primary papers such as WebGPT, WebShop, SeeAct, WebVoyager, WebAgent, or AutoWebGLM.

---

## Important concepts to remember

### 1. Profile

The role, identity, or goal description of an agent.

### 2. Memory

Information stored from previous interactions or user history.

### 3. Planning

The process of decomposing a goal into steps.

### 4. Action

The operations the agent performs in a web environment or web application.

### 5. Web applications

Broader web settings beyond browser navigation, including recommendation and social platforms.

---

## Key evidence from the paper

### Tutorial scope

The paper positions LLM agents across web mining, social networks, recommender systems, and conversational systems.

### Architecture overview

It uses common agent modules such as profiling, memory, planning, and action.

### WWW relevance

Its publication as a WWW companion/tutorial paper supports the relevance of LLM agents to web research.

---

## Connection to earlier and later papers

### Connection to agent surveys

This tutorial overlaps with broad agent surveys but is focused on the web research community.

### Connection to S4

It can be used to introduce why LLM agents matter beyond narrow browser tasks.

### Connection to S6

It connects web automation with web mining, recommendation, and conversational systems.

---

## Connection to later thesis sections

- **S3 — Agent Architectures:**
  Profile-memory-planning-action framing.
- **S4 — Web Agent Evolution:**
  Contextual positioning within web research.
- **S6 — Web Information Access:**
  Connections to web mining and recommendation.
- **S8 — Deployment:**
  Practical web applications and product-facing agents.

---

## Limitation connected to thesis

This paper does not solve any technical web-agent challenge.

For the thesis, use it as background only. It does not provide:

- a benchmark,
- a new system,
- detailed web grounding analysis,
- extraction evaluation,
- or deployment results.

---

## Reading decision

- **Read fully?** No, selective reading is enough
- **Depth needed:** Selective
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Tutorial outline
  - Agent architecture overview
  - Application areas

---

## One-sentence summary

This tutorial positions LLM-powered agents as a broad web-application paradigm, but it is contextual rather than a core technical web-automation paper.

---

## BibTeX

```bibtex
@inproceedings{deng2024llmpoweredweb,
  title     = {Large Language Model Powered Agents in the Web},
  author    = {Deng, Yang and Zhang, An and Lin, Yankai and Chen, Xu and Wen, Ji-Rong and Chua, Tat-Seng},
  booktitle = {Companion Proceedings of the ACM Web Conference 2024},
  pages     = {1242--1243},
  year      = {2024},
  publisher = {ACM},
  doi       = {10.1145/3589335.3641240}
}
```

---

## Source links

- https://doi.org/10.1145/3589335.3641240


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2024-10 - Agent S- An Open Agentic Framework that Uses Computers Like a Human.md

# Paper 290 — Agent S: An Open Agentic Framework that Uses Computers Like a Human

## Metadata

- **Title:** Agent S: An Open Agentic Framework that Uses Computers Like a Human
- **Authors:** Saaket Agashe, Jiuzhou Han, Shuyu Gan, Jiachen Yang, Ang Li, Xin Eric Wang
- **Year:** 2024
- **Venue:** arXiv preprint
- **DOI:** 10.48550/arXiv.2410.08164
- **arXiv ID:** arXiv:2410.08164
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.2 GUI grounding; S5.3 hierarchical planning; S5.4 memory/experience; S5.5 GUI failures; S8 cross-platform computer use
- **Category:** GUI AGENT / COMPUTER-USE / HIERARCHICAL PLANNING
- **Paper type:** System / open agentic framework
- **Priority:** P1
- **BibTeX key:** agashe2024agents

---

## Simple understanding

Agent S is a general **computer-use GUI agent**, not only a web agent.

It targets tasks across desktop environments and applications. The system is built around three major needs:

```text
domain-specific knowledge
long-horizon hierarchical planning
dynamic interface handling
```

Agent S uses:

```text
online web search
narrative memory
episodic memory
hierarchical planning
Agent-Computer Interface
```

For my thesis, Agent S is useful because generalized web automation is part of a larger movement: LLM agents that use computers and graphical interfaces like humans. Web agents share many of the same challenges: perception, grounding, memory, action execution, and safety.

---

## Notes

- **Core idea:**
  Build an open GUI-agent framework with experience-augmented hierarchical planning, external knowledge retrieval, narrative/episodic memory, and an Agent-Computer Interface.

- **Key finding:**
  Agent S improves performance on OSWorld and WindowsAgentArena relative to baseline GUI agents, showing the value of hierarchical planning and experience.

- **Limitation:**
  It remains far below human performance on realistic computer-use tasks.

- **Additional limitation:**
  It is a general GUI/computer agent, not a web-extraction-specific system.

- **Additional limitation:**
  Memory can be stale, wrong, or irrelevant if not verified.

- **Additional limitation:**
  External web search can introduce noisy or unreliable information.

- **Connects to:**
  WebVoyager, SeeAct, AutoGLM, CoALA, Reflexion, OSWorld, WindowsAgentArena, and broader computer-use agents.

- **Use in thesis:**
  Use to show that web automation belongs to the broader GUI-agent/computer-use paradigm.

---

## Thesis-ready paragraph

Agashe et al. introduced Agent S, an open agentic framework designed to use computers through graphical user interfaces. The system combines online knowledge retrieval, narrative memory, episodic memory, hierarchical planning, and a language-centric Agent-Computer Interface. Although Agent S is broader than web automation, it is relevant to this thesis because web agents face similar challenges: they must use domain knowledge, plan over long horizons, interact with dynamic interfaces, and remember previous experiences. Agent S demonstrates that hierarchical planning and memory improve GUI-agent performance, but its remaining gap to human performance shows that reliable computer-use automation remains difficult. For web automation, the paper is most useful as a bridge from browser agents to general GUI agents.

---

## Why this paper matters for my thesis

This paper matters because web automation is increasingly part of **computer-use automation**.

A real assistant may need to:

```text
open browser
use web app
download file
open spreadsheet
copy extracted data
send email
```

This crosses the boundary between web and desktop GUI tasks.

Agent S helps your thesis connect web agents to the broader GUI-agent literature, especially for:

```text
memory
hierarchical planning
interface action abstraction
experience reuse
```


---

## Important concepts to remember

### 1. Agent-Computer Interface

A structured interface that defines how the agent can interact with the computer.

### 2. Hierarchical planning

Breaking a complex task into subtasks and low-level actions.

### 3. Narrative memory

High-level summaries of prior experiences.

### 4. Episodic memory

Detailed memories of specific previous task trajectories.

### 5. Online knowledge retrieval

Using web search to gather task-specific instructions or domain knowledge.

### 6. OSWorld

A benchmark for realistic operating-system tasks.

---

## Key evidence from the paper

### Architecture

The paper presents an architecture combining online search, narrative memory, episodic memory, hierarchical planning, and ACI.

### Motivation

It identifies domain knowledge, long-horizon planning, and dynamic non-uniform interfaces as central challenges.

### Benchmark results

Agent S improves performance on OSWorld and WindowsAgentArena, showing benefit from experience-augmented planning.

### Thesis evidence

The key lesson is that realistic GUI automation requires both memory and planning, not only a vision-language model.

---

## Connection to earlier and later papers

### Connection to Reflexion

Agent S uses experience and memory, similar in spirit to Reflexion, but in broader GUI environments.

### Connection to WebVoyager

WebVoyager is browser-specific.

Agent S is broader computer-use.

### Connection to AutoGLM

Both Agent S and AutoGLM represent the trend toward general GUI foundation agents.

---

## Connection to later thesis sections

- **S5.2 — Grounding:**
  GUI perception and action targeting.
- **S5.3 — Planning:**
  Hierarchical task decomposition.
- **S5.4 — Training/Memory:**
  Experience and memory reuse.
- **S5.5 — Failure Modes:**
  Dynamic interface failures and wrong action execution.
- **S8 — Deployment:**
  Cross-platform computer-use automation.

---

## Limitation connected to thesis

Agent S improves GUI automation, but it does not directly solve web data extraction.

It mainly contributes:

```text
hierarchical planning + memory + computer-use interface
```

It does not fully solve:

- DOM-specific grounding,
- web extraction verification,
- website-specific constraints,
- browser security,
- or precise data extraction workflows.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Medium-high
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Architecture figure
  - Agent-Computer Interface
  - Narrative memory
  - Episodic memory
  - Hierarchical planning
  - OSWorld results
  - Failure analysis

---

## One-sentence summary

Agent S shows that GUI agents benefit from hierarchical planning and experience memory, but realistic computer-use automation remains far from solved.

---

## BibTeX

```bibtex
@article{agashe2024agents,
  title   = {Agent S: An Open Agentic Framework that Uses Computers Like a Human},
  author  = {Agashe, Saaket and Han, Jiuzhou and Gan, Shuyu and Yang, Jiachen and Li, Ang and Wang, Xin Eric},
  journal = {arXiv preprint arXiv:2410.08164},
  year    = {2024},
  doi     = {10.48550/arXiv.2410.08164}
}
```

---

## Source links

- https://arxiv.org/abs/2410.08164
- https://github.com/simular-ai/Agent-S


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2024-10 - AutoGLM Autonomous Foundation Agents for GUIs.md

# Paper 291 — AutoGLM: Autonomous Foundation Agents for GUIs

## Metadata

- **Title:** AutoGLM: Autonomous Foundation Agents for GUIs
- **Authors:** Xiao Liu, Bo Qin, Dongzhu Liang, Guang Dong, Hanyu Lai, Hanchen Zhang, and others
- **Year:** 2024
- **Venue:** arXiv preprint
- **DOI:** 10.48550/arXiv.2411.00820
- **arXiv ID:** arXiv:2411.00820
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.2 intermediate interfaces/grounding; S5.3 planning; S5.4 online curriculum RL; S5.5 error recovery; S8 deployable GUI agents
- **Category:** GUI AGENT / FOUNDATION AGENT / WEB + ANDROID
- **Paper type:** System / foundation GUI agent
- **Priority:** P1
- **BibTeX key:** liu2024autoglm

---

## Simple understanding

AutoGLM presents autonomous foundation agents for graphical user interfaces, especially web and Android environments.

The key idea is to separate:

```text
planning behavior → flexible reasoning and recovery
grounding behavior → accurate mapping to UI elements
```

AutoGLM uses an **intermediate interface** so the planner does not directly operate on raw pixels or raw UI complexity. It also uses **progressive self-evolving online curriculum reinforcement learning** to improve behavior.

For my thesis, AutoGLM matters because web agents also need this separation. A web agent may understand what to do, but it still needs a reliable way to ground that plan into the correct UI element and action.

---

## Notes

- **Core idea:**
  Build GUI foundation agents using an intermediate interface that separates planning from grounding, trained with progressive self-evolving online curriculum RL.

- **Key finding:**
  The paper reports strong results on WebArena-like, OpenTable, AndroidLab, and common Chinese app tasks, suggesting progress toward deployable GUI agents.

- **Limitation:**
  High scores may depend on selected domains and task distributions; arbitrary web generalization remains difficult.

- **Additional limitation:**
  Intermediate interfaces require engineering and may not transfer perfectly across platforms.

- **Additional limitation:**
  Online RL requires safe environments and reliable rewards; real websites may contain irreversible actions.

- **Additional limitation:**
  Planning-grounding separation helps but does not eliminate grounding errors.

- **Connects to:**
  AutoWebGLM, SeeAct, WebVoyager, Agent S, GUI-agent surveys, and deployable browser/mobile agents.

- **Use in thesis:**
  Use as a modern GUI-agent paper showing the importance of planning-grounding separation and online training.

---

## Thesis-ready paragraph

AutoGLM introduces autonomous foundation agents for graphical user interfaces, focusing on web and mobile environments. The system emphasizes two design principles: an intermediate interface is needed to separate flexible planning from precise grounding, and self-evolving online curriculum reinforcement learning can improve agents through interaction. This is highly relevant to LLM-based web automation because a web agent must both reason about user goals and accurately ground actions in UI elements. AutoGLM’s results on web and Android tasks suggest progress toward deployable GUI agents, but its limitations remain central to this thesis: cross-site generalization, safety during online learning, reward reliability, and privacy-sensitive deployment.

---

## Why this paper matters for my thesis

This paper matters because it makes a key design principle explicit:

```text
planning ≠ grounding
```

A model may plan:

```text
Open the booking page and choose a date.
```

But grounding requires:

```text
which button?
which date cell?
which input field?
which operation?
```

AutoGLM argues that these should be separated through an intermediate interface and trained appropriately.

This directly supports S5.2 and S5.3.

---

## Important concepts to remember

### 1. Foundation agent

A general agent system designed to operate across GUI environments.

### 2. Intermediate interface

An abstraction layer between raw GUI and agent action planning.

### 3. Planning behavior

The agent’s reasoning over goals, subtasks, and recovery.

### 4. Grounding behavior

The mapping from planned actions to specific UI elements and operations.

### 5. Self-evolving online curriculum RL

Progressive interaction-based training from easier to harder tasks.

---

## Key evidence from the paper

### Design insight

The abstract emphasizes intermediate interface design and self-evolving curriculum RL.

### Web and mobile evaluation

The paper evaluates on web/browser and Android tasks.

### Reported performance

The paper reports strong benchmark results on WebArena-like, OpenTable, and Android tasks.

### Deployment relevance

Figures and examples show GUI foundation agents in practical app/browser settings.

---

## Connection to earlier and later papers

### Connection to SeeAct

SeeAct identifies grounding as the bottleneck.

AutoGLM proposes an intermediate-interface approach to improve planning-grounding separation.

### Connection to AutoWebGLM

AutoWebGLM is web-navigation-specific.

AutoGLM generalizes toward GUI foundation agents across web and mobile.

### Connection to Agent S

Both focus on broader computer/GUI use beyond only web browsing.

---

## Connection to later thesis sections

- **S5.2 — Perception/Grounding:**
  Intermediate interfaces and element grounding.
- **S5.3 — Planning:**
  Separation of planning behavior from execution.
- **S5.4 — Training:**
  Online curriculum RL and self-evolution.
- **S5.5 — Failure Modes:**
  Grounding errors and recovery.
- **S8 — Deployment:**
  Browser/mobile deployment, privacy, and permissions.

---

## Limitation connected to thesis

AutoGLM advances GUI foundation agents, but it does not fully solve generalized web automation.

It mainly improves:

```text
planning-grounding separation + online GUI training
```

It does not fully solve:

- reliable open-web generalization,
- extraction verification,
- website policy constraints,
- privacy-sensitive workflows,
- or long-term tool/interface maintenance.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Intermediate interface design
  - Planning vs grounding
  - Curriculum RL
  - Web/browser results
  - Android results
  - Limitations

---

## One-sentence summary

AutoGLM frames GUI automation as a foundation-agent problem where planning and grounding must be separated and improved through online curriculum learning.

---

## BibTeX

```bibtex
@article{liu2024autoglm,
  title   = {AutoGLM: Autonomous Foundation Agents for GUIs},
  author  = {Liu, Xiao and Qin, Bo and Liang, Dongzhu and Dong, Guang and Lai, Hanyu and Zhang, Hanchen and others},
  journal = {arXiv preprint arXiv:2411.00820},
  year    = {2024},
  doi     = {10.48550/arXiv.2411.00820}
}
```

---

## Source links

- https://arxiv.org/abs/2411.00820
- https://xiao9905.github.io/AutoGLM


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2024-10 - AutoWebGLM- Bootstrap and Reinforce A Large Language Model-based Web Navigating Agent.md

# Paper 289 — AutoWebGLM: Bootstrap and Reinforce A Large Language Model-based Web Navigating Agent

## Metadata

- **Title:** AutoWebGLM: Bootstrap and Reinforce A Large Language Model-based Web Navigating Agent
- **Authors:** Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, Jie Tang
- **Year:** 2024
- **Venue:** arXiv preprint / extended earlier version
- **DOI:** 10.48550/arXiv.2404.03648
- **arXiv ID:** arXiv:2404.03648
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 AutoWebBench; S5.2 HTML simplification; S5.3 task decomposition; S5.4 curriculum/RL/RFT; S5.5 loops and self-checking failures; S8 browser extension/deployment
- **Category:** WEB-LLM / TRAINED WEB NAVIGATION AGENT / AUTOWEBGLM
- **Paper type:** System / training framework / benchmark
- **Priority:** P1
- **BibTeX key:** lai2024autowebglmbootstrap

---

## Simple understanding

This is the earlier/extended AutoWebGLM paper.

AutoWebGLM is a trained web-navigation agent based on **ChatGLM3-6B**. It is important because it moves away from only prompting large proprietary models and instead trains a smaller open model for browser navigation.

The paper argues that real web navigation is hard because:

```text
webpages are long and noisy
there is no unified action space
high-quality trajectories are scarce
agents get stuck in loops
self-checking is weak
```

AutoWebGLM addresses this with:

```text
HTML simplification
human-AI browsing trajectories
curriculum learning
reinforcement learning
rejection sampling finetuning
AutoWebBench
```

For my thesis, this paper is important because it shows how web agents can be specialized through data and training, not only prompt engineering.

---

## Notes

- **Core idea:**
  Train a ChatGLM3-6B-based web-navigation agent using simplified HTML observations, human-AI trajectories, curriculum learning, reinforcement learning, and rejection sampling finetuning.

- **Key finding:**
  AutoWebGLM is reported to perform competitively across web-navigation benchmarks and can outperform prompted GPT-4 in several settings while remaining smaller and deployable.

- **Limitation:**
  HTML simplification can remove information needed for precise extraction or grounding.

- **Additional limitation:**
  Training quality depends on trajectory quality; hybrid human-AI data can include bias or model errors.

- **Additional limitation:**
  RL and rejection sampling require reliable reward or evaluation signals, which are hard for open-ended web tasks.

- **Additional limitation:**
  The system is mainly a web-navigation agent, not a complete extraction/verifier system.

- **Connects to:**
  WebAgent, WebVoyager, Mind2Web, WebArena, MiniWoB++, AutoWebBench, and trained open web agents.

- **Use in thesis:**
  Use as a key S4 paper for trained web navigation and as support for S5.4 training strategies.

---

## Thesis-ready paragraph

AutoWebGLM presents a trained LLM-based web-navigation agent built on ChatGLM3-6B. The system combines HTML simplification, a browser automation framework, hybrid human-AI trajectory collection, curriculum learning, reinforcement learning, and rejection sampling finetuning. This paper is important for the evolution of web agents because it shows that smaller open models can be specialized for web navigation through task-specific data and training. For generalized web automation, AutoWebGLM addresses several practical problems: long noisy HTML, scarce demonstrations, open-domain action decisions, and loop correction. However, it also reveals remaining limitations: simplified HTML may omit relevant details, reward signals are difficult to define, and web navigation is not identical to robust structured data extraction.

---

## Why this paper matters for my thesis

This paper matters because it shows a practical path toward deployable open web agents.

A prompt-only agent may rely on:

```text
large proprietary model + prompt + browser tool
```

AutoWebGLM instead uses:

```text
smaller model + web-specific observation design + trajectories + training
```

For a PhD thesis, this is important because generalized web automation may require specialized models and datasets, not only prompting GPT-4-like systems.

---

## Important concepts to remember

### 1. HTML simplification

Reducing webpage HTML to a shorter representation for the model.

### 2. Curriculum learning

Training from simple operations to longer browsing traces.

### 3. Reinforcement learning

Optimizing behavior through reward signals.

### 4. Rejection sampling finetuning

Generating multiple outputs and fine-tuning on selected high-quality trajectories.

### 5. AutoWebBench

A bilingual benchmark for real-world browsing tasks.

### 6. Self-checking

The model’s ability to detect whether it is progressing or stuck.

---

## Key evidence from the paper

### Architecture

The paper presents a system with simplified HTML, automated browsing, OCR, curriculum learning, RL, and RFT.

### Trajectory data

It reports a browsing-operation dataset collected through human-AI collaboration.

### Benchmarking

It evaluates across several web-agent benchmarks and compares with stronger prompted models.

### Deployment

The system is associated with practical browser-agent deployment, making it relevant to S8.

---

## Connection to earlier and later papers

### Connection to WebAgent

Both WebAgent and AutoWebGLM target real web automation through HTML-aware methods.

WebAgent emphasizes program synthesis.

AutoWebGLM emphasizes trained web-navigation policies.

### Connection to WebVoyager

WebVoyager uses multimodal screenshots and labeled elements.

AutoWebGLM uses simplified HTML and trained browser operations.

### Connection to S5.4

AutoWebGLM is one of the strongest examples of web-agent training:

```text
trajectory data → curriculum → RL → RFT
```

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  AutoWebBench and multi-benchmark comparison.
- **S5.2 — Perception/Grounding:**
  HTML simplification and observation formatting.
- **S5.3 — Planning:**
  Task decomposition and browser navigation decisions.
- **S5.4 — Training:**
  Curriculum learning, RL, and rejection sampling finetuning.
- **S5.5 — Failure Modes:**
  Loops, bad self-checking, and wrong action inference.
- **S8 — Deployment:**
  Browser extension and real-world usability.

---

## Limitation connected to thesis

AutoWebGLM improves trained web navigation, but it does not fully solve generalized web automation and data extraction.

It mainly improves:

```text
web navigation policy + HTML simplification + training
```

It does not fully solve:

- arbitrary website generalization,
- robust extraction verification,
- multimodal visual grounding,
- privacy and permission boundaries,
- irreversible action safety,
- or long-term website maintenance.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Motivation/challenges
  - HTML simplification
  - Data collection
  - Curriculum learning
  - RL/RFT
  - AutoWebBench
  - Results
  - Failure analysis

---

## One-sentence summary

AutoWebGLM shows that smaller trained LLMs can become strong web-navigation agents through HTML simplification, trajectory data, curriculum learning, RL, and RFT.

---

## BibTeX

```bibtex
@article{lai2024autowebglmbootstrap,
  title   = {AutoWebGLM: Bootstrap and Reinforce A Large Language Model-based Web Navigating Agent},
  author  = {Lai, Hanyu and Liu, Xiao and Iong, Iat Long and Yao, Shuntian and Chen, Yuxuan and Shen, Pengbo and Yu, Hao and Zhang, Hanchen and Zhang, Xiaohan and Dong, Yuxiao and Tang, Jie},
  journal = {arXiv preprint arXiv:2404.03648},
  year    = {2024},
  doi     = {10.48550/arXiv.2404.03648}
}
```

---

## Source links

- https://arxiv.org/abs/2404.03648
- https://github.com/THUDM/AutoWebGLM


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2024-11 - Large Language Model-Brained GUI Agents- A Survey - preprint version.md

# Paper 292 — Large Language Model-Brained GUI Agents: A Survey

## Metadata

- **Title:** Large Language Model-Brained GUI Agents: A Survey
- **Authors:** Chaoyun Zhang, Shilin He, Jiaxu Qian, Bowen Li, Liqun Li, Si Qin, Yu Kang, Minghua Ma, Guyue Liu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
- **Year:** 2024 / later 2025
- **Venue:** arXiv preprint; later Transactions on Machine Learning Research
- **DOI:** Not listed
- **arXiv ID:** arXiv:2411.18279
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 evaluation; S5.2 GUI grounding; S5.3 planning/actions; S5.4 data/models; S5.5 challenges; S8 roadmap
- **Category:** SURVEY / LLM-BRAINED GUI AGENTS
- **Paper type:** Survey / taxonomy
- **Priority:** P1
- **BibTeX key:** zhang2024llmbrainedpreprint

---

## Simple understanding

This is the preprint version of a broad survey on **LLM-brained GUI agents**.

It is useful because web agents are a subset of GUI agents. A GUI agent can control:

```text
web browsers
mobile apps
desktop applications
cross-platform software
```

The survey covers:

```text
background
frameworks
data
models
evaluation
applications
limitations
future roadmap
```

For the thesis, use this as a taxonomy source, but prefer the later TMLR version for final citation.

---

## Notes

- **Core idea:**
  Survey LLM-brained GUI agents across history, core components, frameworks, data, models, evaluation, applications, and challenges.

- **Key finding:**
  The survey argues that LLM-powered GUI agents shift automation from brittle scripts toward flexible natural-language-driven interaction.

- **Limitation:**
  It is a survey, not a new empirical system.

- **Additional limitation:**
  It is broad across web, mobile, and desktop, so web-specific claims should be supported by primary web-agent papers.

- **Additional limitation:**
  Use the later TMLR version when possible for final thesis citation.

- **Connects to:**
  Web agents, GUI automation, mobile agents, desktop agents, large action models, data collection, and evaluation benchmarks.

- **Use in thesis:**
  Use for broad GUI-agent framing and taxonomy.

---

## Thesis-ready paragraph

Zhang et al. survey LLM-brained GUI agents, defining them as agents that use LLMs or multimodal LLMs as cognitive engines for understanding GUI states, planning actions, and executing operations. The survey is relevant to this thesis because web agents are one important subcategory of GUI agents. Its discussion of operating environments, perception, planning, action execution, data, models, evaluation, and challenges helps position generalized web automation within a broader GUI-agent ecosystem. However, as a survey, it should be used mainly for taxonomy and roadmap; detailed empirical claims should rely on primary system papers such as WebVoyager, SeeAct, AutoWebGLM, and WebAgent.

---

## Why this paper matters for my thesis

This paper matters because it helps explain that web automation is part of a larger trend:

```text
chatbots → agents → GUI agents → computer-use agents
```

A web agent is not isolated. It shares problems with mobile and desktop agents:

```text
screen perception
element grounding
action generation
memory
planning
evaluation
privacy
latency
safety
```

The survey is useful for structure, not for detailed performance evidence.

---

## Important concepts to remember

### 1. LLM-brained GUI agent

A GUI agent using an LLM/MLLM as the cognitive engine.

### 2. Large Action Model

A model specialized for generating GUI actions.

### 3. Operating environment

The platform controlled by the agent: web, mobile, desktop, or cross-platform.

### 4. State perception

How the agent observes GUI state through screenshots, DOM, accessibility trees, OCR, or metadata.

### 5. Action execution

How the agent converts decisions into clicks, typing, API calls, or system operations.

### 6. Roadmap

Open problems such as privacy, latency, safety, ethics, and scalability.

---

## Key evidence from the paper

### Survey structure

The paper organizes the field into foundations, frameworks, data, models, evaluation, applications, and challenges.

### Figure 1

Shows an agent acting across applications such as browser, Word, PowerPoint, Teams, and other software.

### Motivation

The introduction contrasts brittle script-based automation with adaptive LLM-powered GUI agents.

### Limitations

The survey highlights privacy, latency, safety, human-agent interaction, customization, ethics, and scalability.

---

## Connection to earlier and later papers

### Connection to S4

This survey supports the broader framing that web agents are part of GUI-agent evolution.

### Connection to Agent S and AutoGLM

Agent S and AutoGLM are examples of the GUI-agent direction described by the survey.

### Connection to S5

The survey’s components map naturally to S5 technical sections.

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  Benchmarks and metrics.
- **S5.2 — Grounding:**
  GUI state perception and element localization.
- **S5.3 — Planning:**
  Action inference and task decomposition.
- **S5.4 — Training:**
  Data and large action models.
- **S5.5/S8 — Challenges:**
  Privacy, latency, safety, and scalability.

---

## Limitation connected to thesis

This survey does not directly solve web automation.

Use it to frame:

```text
web agents ⊂ GUI agents
```

but use primary web-agent papers for:

- benchmark results,
- architecture details,
- grounding mechanisms,
- extraction performance,
- and deployment claims.

---

## Reading decision

- **Read fully?** No, selective reading is enough
- **Depth needed:** Selective
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Definitions
  - Framework taxonomy
  - Data and models
  - Evaluation
  - Limitations and roadmap

---

## One-sentence summary

This survey maps the GUI-agent field and helps position web automation inside broader LLM-powered GUI automation.

---

## BibTeX

```bibtex
@article{zhang2024llmbrainedpreprint,
  title   = {Large Language Model-Brained GUI Agents: A Survey},
  author  = {Zhang, Chaoyun and He, Shilin and Qian, Jiaxu and Li, Bowen and Li, Liqun and Qin, Si and Kang, Yu and Ma, Minghua and Liu, Guyue and Lin, Qingwei and Rajmohan, Saravan and Zhang, Dongmei and Zhang, Qi},
  journal = {arXiv preprint arXiv:2411.18279},
  year    = {2024}
}
```

---

## Source links

- https://arxiv.org/abs/2411.18279
- https://github.com/vyokky/LLM-Brained-GUI-Agents-Survey


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2024-12 - AutoWebGLM A Large Language Model-based Web Navigating Agent.md

# Paper 293 — AutoWebGLM: A Large Language Model-based Web Navigating Agent

## Metadata

- **Title:** AutoWebGLM: A Large Language Model-based Web Navigating Agent
- **Authors:** Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, Jie Tang
- **Year:** 2024
- **Venue:** Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 2024)
- **DOI:** 10.1145/3637528.3671620
- **arXiv ID:** arXiv:2404.03648
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 AutoWebBench; S5.2 HTML simplification; S5.3 web navigation; S5.4 curriculum/RL/RFT; S5.5 loops/self-checking; S8 deployment
- **Category:** WEB-LLM / AUTOWEBGLM / TRAINED WEB NAVIGATION
- **Paper type:** System / conference paper
- **Priority:** P1
- **BibTeX key:** lai2024autowebglm

---

## Simple understanding

This is the **KDD 2024 version** of AutoWebGLM. For final thesis citation, this version should be preferred over the earlier preprint note.

AutoWebGLM is an LLM-based web-navigation agent built on ChatGLM3-6B. It aims to build an open, deployable web agent rather than relying only on proprietary frontier models.

The system uses:

```text
simplified HTML observations
a browsing operation dataset
curriculum learning
reinforcement learning
rejection sampling finetuning
AutoWebBench
browser-extension-style deployment
```

For the thesis, this is a strong S4 P1 paper because it connects web-agent systems with training, benchmarking, and real-world deployment.

---

## Notes

- **Core idea:**
  Present an open ChatGLM3-6B-based web-navigation agent trained with simplified HTML, browsing traces, curriculum learning, RL, and rejection sampling finetuning.

- **Key finding:**
  The paper reports that AutoWebGLM performs competitively with or better than advanced prompted LLM agents across web-navigation benchmarks.

- **Limitation:**
  It is primarily a navigation agent, not a complete generalized web data extraction system.

- **Additional limitation:**
  HTML simplification helps context length but may remove information needed for exact extraction.

- **Additional limitation:**
  Reward signals and self-checking remain difficult in open-ended web tasks.

- **Additional limitation:**
  Deployment through browser tooling raises privacy, permissions, and safety concerns.

- **Connects to:**
  AutoWebGLM preprint, WebAgent, WebVoyager, Mind2Web, WebArena, MiniWoB++, and AutoWebBench.

- **Use in thesis:**
  Use this as the main AutoWebGLM citation and as a major example of trained open web-navigation agents.

---

## Thesis-ready paragraph

Lai et al. present AutoWebGLM, an LLM-based web navigating agent built on ChatGLM3-6B and trained for browser interaction. The system uses simplified HTML representations, a browsing operation dataset, curriculum learning, reinforcement learning, and rejection sampling finetuning to improve webpage understanding, task decomposition, and action execution. AutoWebGLM is important because it demonstrates that smaller open models can be specialized for web navigation rather than relying entirely on prompted proprietary LLMs. It also introduces AutoWebBench, a bilingual benchmark for realistic web tasks. For generalized web automation and data extraction, AutoWebGLM is a significant step toward deployable web agents, but it remains limited by observation simplification, reward design, self-checking reliability, and the need for robust verification of extracted information.

---

## Why this paper matters for my thesis

This paper matters because it gives a more deployable direction than prompt-only agents.

The key thesis point is:

```text
Prompting is not enough for robust web automation.
```

AutoWebGLM shows a training pipeline:

```text
web traces → curriculum → RL → rejection sampling finetuning → better web agent
```

This is important for S5.4.

It also shows the importance of observation design:

```text
raw HTML too long → simplified HTML → model-readable state
```

This is important for S5.2.

---

## Important concepts to remember

### 1. Simplified HTML

A compressed and cleaned HTML representation for the LLM.

### 2. Browsing operation dataset

A dataset of web-action traces used for training.

### 3. Curriculum learning

Training from simpler browsing operations to longer tasks.

### 4. Reinforcement learning

Optimization from task success signals.

### 5. Rejection sampling finetuning

Selecting higher-quality generated actions/trajectories for fine-tuning.

### 6. AutoWebBench

A bilingual benchmark for real-world web navigation.

---

## Key evidence from the paper

### KDD publication

This version is the conference paper and should be preferred for final citation.

### System components

The paper describes webpage simplification, operation data, curriculum learning, RL, and RFT.

### Benchmark comparison

The paper compares against prompted LLM agents and reports competitive performance.

### Deployment relevance

The system is designed as a practical web-navigation agent, making it relevant for S8.

---

## Connection to earlier and later papers

### Connection to the earlier AutoWebGLM note

The preprint/earlier version gives more context, but the KDD version is the stronger citation.

### Connection to WebAgent

Both use HTML-oriented representations, but WebAgent emphasizes program synthesis while AutoWebGLM emphasizes training a web-navigation model.

### Connection to WebVoyager

WebVoyager is multimodal/live-web.

AutoWebGLM is trained HTML/navigation-oriented.

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  AutoWebBench and benchmark design.
- **S5.2 — Perception/Grounding:**
  HTML simplification and webpage representation.
- **S5.3 — Planning:**
  Navigation and task decomposition.
- **S5.4 — Training:**
  Curriculum learning, RL, and RFT.
- **S5.5 — Failure Modes:**
  Looping and self-checking failures.
- **S8 — Deployment:**
  Browser extension and practical web-agent use.

---

## Limitation connected to thesis

AutoWebGLM is a strong web-navigation agent but not a full solution.

It improves:

```text
trained browsing policy + simplified HTML + benchmarked navigation
```

but still needs:

- robust extraction verification,
- multimodal grounding for visual tasks,
- privacy-aware deployment,
- safe irreversible-action handling,
- and maintenance across changing websites.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** Very high
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Model/system overview
  - Simplified HTML
  - Browsing operation dataset
  - Curriculum learning
  - RL/RFT
  - AutoWebBench
  - Results
  - Limitations

---

## One-sentence summary

AutoWebGLM shows that trained open LLMs can become competitive web-navigation agents through simplified HTML, curated traces, curriculum learning, RL, and RFT.

---

## BibTeX

```bibtex
@inproceedings{lai2024autowebglm,
  title     = {AutoWebGLM: A Large Language Model-based Web Navigating Agent},
  author    = {Lai, Hanyu and Liu, Xiao and Iong, Iat Long and Yao, Shuntian and Chen, Yuxuan and Shen, Pengbo and Yu, Hao and Zhang, Hanchen and Zhang, Xiaohan and Dong, Yuxiao and Tang, Jie},
  booktitle = {Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  year      = {2024},
  publisher = {ACM},
  doi       = {10.1145/3637528.3671620},
  eprint    = {2404.03648},
  archivePrefix = {arXiv}
}
```

---

## Source links

- https://doi.org/10.1145/3637528.3671620
- https://arxiv.org/abs/2404.03648
- https://github.com/THUDM/AutoWebGLM


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2025-02 - GUI Agents with Foundation Models- A Comprehensive Survey.md

# Paper 294 — GUI Agents with Foundation Models: A Comprehensive Survey

## Metadata

- **Title:** GUI Agents with Foundation Models: A Comprehensive Survey
- **Authors:** Shuai Wang, Weiwen Liu, Jingxuan Chen, Yuqi Zhou, Weinan Gan, Xingshan Zeng, Yuhan Che, Shuai Yu, Xinlong Hao, Kun Shao, Bin Wang, Chuhan Wu, Yasheng Wang, Ruiming Tang, Jianye Hao
- **Year:** 2025
- **Venue:** arXiv preprint
- **DOI:** Not listed
- **arXiv ID:** arXiv:2411.04890
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 benchmarks; S5.2 GUI data/perception; S5.3 frameworks; S5.4 training/data; S8 applications
- **Category:** SURVEY / GUI AGENTS / FOUNDATION MODELS
- **Paper type:** Survey
- **Priority:** P1
- **BibTeX key:** wang2025guiagentsfoundationmodels

---

## Simple understanding

This is a compact survey of GUI agents with foundation models.

It organizes recent work around:

```text
data resources
frameworks
applications
```

For the thesis, it is useful because it places web agents inside the broader GUI-agent ecosystem. It shows the field’s movement from rule-based and RL automation toward multimodal foundation-model agents.

Use it as a survey reference, not as primary evidence for a specific web-agent result.

---

## Notes

- **Core idea:**
  Survey foundation-model-based GUI agents, focusing on datasets/resources, frameworks, and applications.

- **Key finding:**
  The survey argues that foundation models enable a shift from rule-based/RL GUI automation to multimodal, instruction-following GUI agents.

- **Limitation:**
  It is broad and relatively compact, so it cannot deeply analyze each web-agent system.

- **Additional limitation:**
  It covers mobile, web, and desktop agents; the thesis should use web-specific papers for detailed claims.

- **Connects to:**
  GUI datasets, benchmarks, mobile agents, web agents, desktop agents, and commercial GUI assistants.

- **Use in thesis:**
  Use for high-level GUI-agent context and for identifying resources/benchmark categories.

---

## Thesis-ready paragraph

Wang et al. survey GUI agents with foundation models and organize the field around data resources, frameworks, and applications. This survey is useful for a thesis on web automation because web agents are a major subset of GUI agents and share many technical problems with mobile and desktop agents, including perception, grounding, action generation, and evaluation. The paper highlights the broader shift from rule-based or reinforcement-learning GUI automation toward multimodal, instruction-following foundation-model agents. However, because it is a broad survey, it should be used mainly for taxonomy and context, while technical claims about web-agent performance should be supported by primary papers such as SeeAct, WebVoyager, WebAgent, and AutoWebGLM.

---

## Why this paper matters for my thesis

This paper matters because it helps place web automation in a bigger ecosystem.

The field is not only:

```text
browser agents
```

but also:

```text
mobile agents
desktop agents
cross-platform agents
commercial GUI assistants
```

This is useful for your thesis because many technical problems overlap:

```text
screen understanding
element grounding
trajectory data
action generation
evaluation
safety
```


---

## Important concepts to remember

### 1. Data resources

Screenshots, instructions, trajectories, UI metadata, and action labels.

### 2. Frameworks

The agent pipelines used to perceive, decide, act, and receive feedback.

### 3. Applications

Web, mobile, desktop, and commercial GUI automation.

### 4. Foundation models

Large language and multimodal models used as the agent core.

### 5. Success rate

A common but incomplete metric for GUI-agent evaluation.

---

## Key evidence from the paper

### Growth trend

The survey summarizes rapid growth in GUI agents using foundation models.

### Framework overview

It organizes work into data resources, frameworks, and applications.

### Historical shift

It contrasts traditional automation approaches with foundation-model-based GUI agents.

---

## Connection to earlier and later papers

### Connection to S4

This survey supports the claim that web agents are part of the broader GUI-agent wave.

### Connection to S5

Its datasets/frameworks/applications structure maps to evaluation, perception, training, and deployment sections.

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  Datasets, environments, and metrics.
- **S5.2 — Perception:**
  Screenshots and UI information.
- **S5.4 — Training:**
  Trajectory data and model training.
- **S8 — Deployment:**
  Applications and commercial GUI agents.

---

## Limitation connected to thesis

This survey is useful but not enough for detailed thesis claims.

It does not provide:

- a new web-agent method,
- a new benchmark,
- specific extraction evaluation,
- or a deep grounding analysis.

Use it as context.

---

## Reading decision

- **Read fully?** No, selective reading is enough
- **Depth needed:** Selective
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Data resources
  - Frameworks
  - Applications
  - Open challenges

---

## One-sentence summary

This survey gives a compact overview of foundation-model GUI agents and helps place web agents inside the broader GUI-agent ecosystem.

---

## BibTeX

```bibtex
@article{wang2025guiagentsfoundationmodels,
  title   = {GUI Agents with Foundation Models: A Comprehensive Survey},
  author  = {Wang, Shuai and Liu, Weiwen and Chen, Jingxuan and Zhou, Yuqi and Gan, Weinan and Zeng, Xingshan and Che, Yuhan and Yu, Shuai and Hao, Xinlong and Shao, Kun and Wang, Bin and Wu, Chuhan and Wang, Yasheng and Tang, Ruiming and Hao, Jianye},
  journal = {arXiv preprint arXiv:2411.04890},
  year    = {2025}
}
```

---

## Source links

- https://arxiv.org/abs/2411.04890


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2025-06 - A Survey on (M)LLM-Based GUI Agents.md

# Paper 295 — A Survey on (M)LLM-Based GUI Agents

## Metadata

- **Title:** A Survey on (M)LLM-Based GUI Agents
- **Authors:** Fei Tang, Haolei Xu, Hang Zhang, Siqi Chen, Xingyu Wu, Yongliang Shen, Wenqi Zhang, Guiyang Hou, Zeqi Tan, Yuchen Yan, Kaitao Song, Jian Shao, Weiming Lu, Jun Xiao, Yueting Zhuang
- **Year:** 2025
- **Venue:** arXiv preprint
- **DOI:** Not listed
- **arXiv ID:** arXiv:2504.13865
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 evaluation; S5.2 perception; S5.3 planning; S5.4 exploration/knowledge; S5.5 safety/errors; S8 future directions
- **Category:** SURVEY / MLLM GUI AGENTS / FOUR-COMPONENT TAXONOMY
- **Paper type:** Survey / taxonomy
- **Priority:** P1
- **BibTeX key:** tang2025survey

---

## Simple understanding

This survey is useful because it organizes modern GUI agents around four components:

```text
perception
exploration
planning
interaction
```

This is very relevant to web agents.

A web agent must:

```text
perceive the page
explore or retrieve needed knowledge
plan task steps
interact with the browser safely
```

For the thesis, this paper is most useful as a taxonomy bridge from S4 systems to S5 technical dimensions.

---

## Notes

- **Core idea:**
  Survey (M)LLM-based GUI agents using four core components: perception, exploration, planning, and interaction.

- **Key finding:**
  The survey identifies key challenges including element localization, knowledge retrieval, long-horizon planning, and safety-aware execution.

- **Limitation:**
  It is a broad GUI-agent survey, not a primary web-agent system.

- **Additional limitation:**
  It does not provide new benchmark results.

- **Additional limitation:**
  Use primary papers for specific claims about SeeAct, WebVoyager, AutoGLM, or WebAgent.

- **Connects to:**
  SeeAct, WebVoyager, AutoGLM, Agent S, GUI grounding, exploration, planning, and interaction safety.

- **Use in thesis:**
  Use as a strong S5 taxonomy source.

---

## Thesis-ready paragraph

Tang et al. survey (M)LLM-based GUI agents and organize the field around four core components: perception, exploration, planning, and interaction. This taxonomy is especially useful for LLM-based web automation because it maps directly onto the web-agent pipeline: perceiving DOM or screenshots, retrieving relevant knowledge, planning multi-step actions, and executing interactions safely. The survey identifies central challenges such as element localization, knowledge retrieval, long-horizon planning, and safety-aware execution. For this thesis, the paper is valuable as a conceptual bridge from S4’s system evolution to S5’s technical decomposition, while specific empirical claims should still be grounded in primary benchmark and system papers.

---

## Why this paper matters for my thesis

This paper matters because it gives a clean structure for S5.

The thesis can use the four components like this:

```text
Perception → S5.2
Exploration → S5.3/S5.4
Planning → S5.3
Interaction → S5.2/S5.5/S7
```

It helps convert the chronological S4 story into a technical S5 analysis.

---

## Important concepts to remember

### 1. Perception

Understanding GUI state through screenshots, DOM/XML, OCR, or multimodal models.

### 2. Exploration

Gathering knowledge from history, environment interaction, or external sources.

### 3. Planning

Decomposing tasks and deciding action sequences.

### 4. Interaction

Executing operations safely and effectively in the GUI environment.

### 5. Element localization

Finding the exact target element for clicking, typing, or selecting.

### 6. Safety-aware execution

Avoiding risky, harmful, or irreversible actions.

---

## Key evidence from the paper

### Four-component taxonomy

The abstract and structure identify perception, exploration, planning, and interaction as fundamental components.

### Challenge list

The survey highlights accurate element localization, knowledge retrieval, long-horizon planning, and safety-aware execution.

### Pipeline view

The paper frames GUI agents as an information-processing pipeline from observation to action.

---

## Connection to earlier and later papers

### Connection to SeeAct

SeeAct’s grounding bottleneck falls under perception and interaction.

### Connection to WebVoyager

WebVoyager combines perception, planning, and interaction in live websites.

### Connection to AutoGLM

AutoGLM’s planning-grounding separation maps to planning and interaction.

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  Benchmarks and static/dynamic evaluation.
- **S5.2 — Perception:**
  Interface representation and element grounding.
- **S5.3 — Planning:**
  Long-horizon planning and verification.
- **S5.4 — Training:**
  Exploration and knowledge acquisition.
- **S5.5/S7 — Failures/Safety:**
  Safety-aware execution and error modes.

---

## Limitation connected to thesis

This survey gives structure, not solution.

It helps organize:

```text
perception → exploration → planning → interaction
```

but it does not itself solve:

- web-specific DOM grounding,
- extraction verification,
- live-site safety,
- or benchmark reliability.

---

## Reading decision

- **Read fully?** No, selective reading is enough
- **Depth needed:** Selective-high
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Architecture overview
  - Perception section
  - Exploration section
  - Planning section
  - Interaction section
  - Challenges

---

## One-sentence summary

This survey gives a useful four-part taxonomy—perception, exploration, planning, interaction—for organizing modern web/GUI agent capabilities.

---

## BibTeX

```bibtex
@article{tang2025survey,
  title   = {A Survey on (M)LLM-Based GUI Agents},
  author  = {Tang, Fei and Xu, Haolei and Zhang, Hang and Chen, Siqi and Wu, Xingyu and Shen, Yongliang and Zhang, Wenqi and Hou, Guiyang and Tan, Zeqi and Yan, Yuchen and Song, Kaitao and Shao, Jian and Lu, Weiming and Xiao, Jun and Zhuang, Yueting},
  journal = {arXiv preprint arXiv:2504.13865},
  year    = {2025}
}
```

---

## Source links

- https://arxiv.org/abs/2504.13865
- https://github.com/zju-real/Awesome-GUI-Agents


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2025-06 - Large Language Model-Brained GUI Agents- A Survey.md

# Paper 296 — Large Language Model-Brained GUI Agents: A Survey

## Metadata

- **Title:** Large Language Model-Brained GUI Agents: A Survey
- **Authors:** Chaoyun Zhang, Shilin He, Jiaxu Qian, Bowen Li, Liqun Li, Si Qin, Yu Kang, Minghua Ma, Guyue Liu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
- **Year:** 2025
- **Venue:** Transactions on Machine Learning Research (TMLR), June 2025
- **DOI:** Not listed
- **arXiv ID:** arXiv:2411.18279
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 evaluation; S5.2 grounding; S5.3 planning/actions; S5.4 data/models/LAMs; S5.5 challenges; S8 deployment roadmap
- **Category:** SURVEY / LLM-POWERED GUI AGENTS / TMLR
- **Paper type:** Peer-reviewed survey
- **Priority:** P1
- **BibTeX key:** zhang2025llmbrained

---

## Simple understanding

This is the later peer-reviewed **TMLR version** of the LLM-brained GUI agents survey.

For the final thesis, this version should be preferred over the earlier preprint version.

The survey covers:

```text
foundations
frameworks
data
models
evaluation
applications
limitations
future roadmap
```

For the thesis, this is one of the best broad survey references for connecting web agents to GUI agents.

---

## Notes

- **Core idea:**
  Provide a comprehensive peer-reviewed survey of LLM-powered GUI agents across foundations, frameworks, data, models, evaluation, applications, and challenges.

- **Key finding:**
  The survey argues that LLM-powered GUI agents enable flexible natural-language-driven automation across web, mobile, desktop, and cross-platform environments.

- **Limitation:**
  It is broad across GUI platforms, so web-specific claims need primary web-agent sources.

- **Additional limitation:**
  It does not present new empirical system results.

- **Additional limitation:**
  The field evolves quickly, so very recent agents may be absent.

- **Connects to:**
  Web agents, mobile agents, desktop agents, cross-platform agents, large action models, GUI benchmarks, and deployment challenges.

- **Use in thesis:**
  Use as the preferred broad survey citation for LLM-powered GUI agents.

---

## Thesis-ready paragraph

Zhang et al. provide a comprehensive TMLR survey of LLM-powered GUI agents, defining them as agents that operate within GUI environments using LLMs as cognitive engines to generate, plan, and execute actions flexibly. The survey is valuable for this thesis because web agents are a subcategory of GUI agents and share key challenges with mobile and desktop agents: state perception, grounding, planning, action execution, safety, privacy, latency, and cross-platform generalization. The survey should be used to support the broader framing of web automation, while primary web-agent papers such as WebGPT, WebShop, WebAgent, SeeAct, WebVoyager, and AutoWebGLM provide concrete system evidence.

---

## Why this paper matters for my thesis

This paper matters because it is the best survey-level source for the broader GUI-agent field.

It helps your thesis say:

```text
web agents are not isolated;
they are part of LLM-powered GUI agents.
```

It also helps organize:

```text
data
models
evaluation
applications
limitations
```

For final writing, cite this TMLR version instead of the preprint version.

---

## Important concepts to remember

### 1. LLM-powered GUI agent

An agent using an LLM/MLLM to perceive, plan, and act in GUI environments.

### 2. Frameworks

Agent architectures for web, mobile, desktop, and cross-platform control.

### 3. Large Action Model

A model adapted or trained for GUI action generation.

### 4. Evaluation

Benchmarks, metrics, and task success protocols for GUI agents.

### 5. Roadmap

Open problems: privacy, latency, safety, human-agent interaction, customization, ethics, scalability.

---

## Key evidence from the paper

### Survey scope

The survey covers frameworks, data, models, evaluation, applications, limitations, and future roadmap.

### GUI breadth

It includes web, mobile, computer/desktop, and cross-platform GUI agents.

### Roadmap

It identifies privacy, latency, safety, and scalability as important remaining challenges.

### Peer-reviewed status

The TMLR version is preferable for final academic citation.

---

## Connection to earlier and later papers

### Connection to preprint version

This is the preferred final version of the earlier survey.

### Connection to GUI-agent systems

Agent S and AutoGLM can be positioned using this survey.

### Connection to web agents

Web agents are one platform category inside the broader GUI-agent landscape.

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  GUI benchmarks and metrics.
- **S5.2 — Perception/Grounding:**
  Environment state perception and grounding.
- **S5.3 — Planning:**
  Action inference and task decomposition.
- **S5.4 — Training:**
  Data collection and large action models.
- **S5.5/S8 — Challenges:**
  Privacy, latency, safety, reliability, and scalability.

---

## Limitation connected to thesis

This survey is not a web automation solution.

Use it to support:

```text
broad GUI-agent framing
```

but rely on web-agent papers for:

- DOM/HTML specifics,
- live-web evaluations,
- extraction tasks,
- and grounding results.

---

## Reading decision

- **Read fully?** No, selective reading is enough
- **Depth needed:** Selective-high
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Definitions
  - Frameworks
  - Data
  - Models
  - Evaluation
  - Applications
  - Challenges and roadmap

---

## One-sentence summary

This TMLR survey is the preferred broad reference for LLM-powered GUI agents and their architecture, data, models, evaluation, and challenges.

---

## BibTeX

```bibtex
@article{zhang2025llmbrained,
  title   = {Large Language Model-Brained GUI Agents: A Survey},
  author  = {Zhang, Chaoyun and He, Shilin and Qian, Jiaxu and Li, Bowen and Li, Liqun and Qin, Si and Kang, Yu and Ma, Minghua and Liu, Guyue and Lin, Qingwei and Rajmohan, Saravan and Zhang, Dongmei and Zhang, Qi},
  journal = {Transactions on Machine Learning Research},
  year    = {2025},
  eprint  = {2411.18279},
  archivePrefix = {arXiv},
  url     = {https://openreview.net/forum?id=xChvYjvXTp}
}
```

---

## Source links

- https://openreview.net/forum?id=xChvYjvXTp
- https://arxiv.org/abs/2411.18279
- https://github.com/vyokky/LLM-Brained-GUI-Agents-Survey


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2025-07 - GUI Agents- A Survey.md

# Paper 297 — GUI Agents: A Survey

## Metadata

- **Title:** GUI Agents: A Survey
- **Authors:** Dang Nguyen, Jian Chen, Yu Wang, Gang Wu, Namyong Park, Zhengmian Hu, Hanjia Lyu, Junda Wu, Ryan Aponte, Yu Xia, Xintong Li, Jing Shi, Hongjie Chen, Viet Dac Lai, Zhouhang Xie, Sungchul Kim, Ruiyi Zhang, Tong Yu, Mehrab Tanjim, Nesreen K. Ahmed, Puneet Mathur, Seunghyun Yoon, Lina Yao, Jihyung Kil, Branislav Kveton, Thien Huu Nguyen, Trung Bui, Tianyi Zhou, Ryan A. Rossi, Franck Dernoncourt
- **Year:** 2025
- **Venue:** Findings of the Association for Computational Linguistics: ACL 2025
- **DOI:** Not listed in uploaded text
- **arXiv ID:** Not listed in uploaded text
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 benchmarks; S5.2 perception; S5.3 reasoning/planning; S5.4 training; S5.5 open problems
- **Category:** SURVEY / GUI AGENTS / ACL FINDINGS
- **Paper type:** Survey
- **Priority:** P1
- **BibTeX key:** nguyen2025guiagents

---

## Simple understanding

This survey defines **GUI agents** and formalizes GUI tasks.

The definition is useful:

```text
A GUI agent is an autonomous agent that interacts with digital platforms through graphical user interfaces by observing visual elements and acting through clicking, typing, tapping, or similar operations.
```

The paper also formulates GUI-agent tasks as sequential decision problems, often as a **POMDP**.

For the thesis, this is useful because web agents are a special case of GUI agents operating in browser environments.

---

## Notes

- **Core idea:**
  Survey GUI agents powered by foundation models and organize their benchmarks, architectures, training methods, and open challenges.

- **Key finding:**
  The survey emphasizes unique GUI-agent challenges: dynamic layouts, diverse graphical designs, grounding issues, and fine-grained recognition of small scattered elements.

- **Limitation:**
  It covers GUI agents broadly, not only web agents.

- **Additional limitation:**
  It is a survey, not a new system paper.

- **Additional limitation:**
  Use primary benchmark papers for detailed empirical claims.

- **Connects to:**
  GUI-agent definitions, POMDP formulation, datasets vs environments, open-world vs closed-world benchmarks, and capability taxonomies.

- **Use in thesis:**
  Use for formal definitions and benchmark/evaluation framing.

---

## Thesis-ready paragraph

Nguyen et al. survey GUI agents and provide a useful formal definition: a GUI agent autonomously interacts with digital platforms through graphical interfaces by observing visual elements and acting through operations such as clicking, typing, and tapping. The paper also frames GUI-agent tasks as sequential decision problems, often modeled as partially observable Markov decision processes. For this thesis, this formalization is valuable because web agents are a specific type of GUI agent operating in browser environments. The survey’s organization around benchmarks, architectures, training methods, and open problems helps situate web automation within the broader GUI-agent field, while primary web-agent papers remain necessary for detailed claims about DOM, HTML, and live-web behavior.

---

## Why this paper matters for my thesis

This paper matters because it gives formal language for the thesis.

You can define web agents as:

```text
GUI agents whose environment is the web/browser.
```

Then the web-agent problem becomes:

```text
partially observable state
sequential actions
changing environment
history-dependent policy
```

This supports the academic framing of web automation as a sequential decision-making problem.

---

## Important concepts to remember

### 1. GUI agent

An autonomous agent that interacts with digital systems through graphical user interfaces.

### 2. POMDP

A partially observable Markov decision process used to formalize GUI-agent tasks.

### 3. Dataset vs environment

A static collection of examples versus an interactive dynamic system.

### 4. Open-world benchmark

A benchmark where needed information can exist outside the benchmark.

### 5. Closed-world benchmark

A benchmark where all needed information is contained inside the benchmark.

### 6. Perception, reasoning, planning, acting

A capability view of GUI-agent systems.

---

## Key evidence from the paper

### Definition

Section 2 defines GUI agents and formalizes GUI-agent tasks.

### POMDP formulation

The paper models GUI tasks as sequential interaction under partial observability.

### Benchmark taxonomy

The survey distinguishes datasets from environments and open-world from closed-world benchmarks.

### Challenges

The introduction highlights dynamic layouts, diverse graphical designs, and grounding issues.

---

## Connection to earlier and later papers

### Connection to web agents

Web agents are GUI agents specialized to web browser environments.

### Connection to S5.1

The dataset/environment distinction is important for web-agent evaluation.

### Connection to S5.2

The grounding challenge directly relates to DOM/screenshot element selection.

---

## Connection to later thesis sections

- **S5.1 — Benchmarks:**
  Dataset vs environment, open-world vs closed-world.
- **S5.2 — Perception:**
  GUI perception and grounding.
- **S5.3 — Planning:**
  Sequential decision-making formulation.
- **S5.4 — Training:**
  Training methods for GUI agents.
- **S5.5 — Failure Modes:**
  Open challenges and failure sources.

---

## Limitation connected to thesis

This survey helps formalize the problem but does not solve web automation.

Use it for definitions and evaluation categories, not for detailed system claims.

---

## Reading decision

- **Read fully?** No, selective reading is enough
- **Depth needed:** Selective
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Definition of GUI agent
  - POMDP formulation
  - Benchmarks section
  - Architecture section
  - Training section
  - Open problems

---

## One-sentence summary

This survey provides a clean formal definition and decision-process framing for GUI agents, useful for positioning web agents in S4/S5.

---

## BibTeX

```bibtex
@inproceedings{nguyen2025guiagents,
  title     = {GUI Agents: A Survey},
  author    = {Nguyen, Dang and Chen, Jian and Wang, Yu and Wu, Gang and Park, Namyong and Hu, Zhengmian and Lyu, Hanjia and Wu, Junda and Aponte, Ryan and Xia, Yu and Li, Xintong and Shi, Jing and Chen, Hongjie and Lai, Viet Dac and Xie, Zhouhang and Kim, Sungchul and Zhang, Ruiyi and Yu, Tong and Tanjim, Mehrab and Ahmed, Nesreen K. and Mathur, Puneet and Yoon, Seunghyun and Yao, Lina and Kil, Jihyung and Kveton, Branislav and Nguyen, Thien Huu and Bui, Trung and Zhou, Tianyi and Rossi, Ryan A. and Dernoncourt, Franck},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
  pages     = {22522--22538},
  year      = {2025}
}
```

---

## Source links

- Not provided in uploaded text


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2025-08 - A Survey of WebAgents- Towards Next-Generation AI Agents for Web Automation with Large Foundation Models.md

# Paper 298 — A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models

## Metadata

- **Title:** A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models
- **Authors:** Liangbo Ning, Ziran Liang, Zhuohang Jiang, Haohao Qu, Yujuan Ding, Wenqi Fan, Xiao-yong Wei, Shanru Lin, Hui Liu, Philip S. Yu, Qing Li
- **Year:** 2025
- **Venue:** arXiv preprint
- **DOI:** Not listed
- **arXiv ID:** arXiv:2503.23350
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.1 evaluation; S5.2 perception; S5.3 planning/reasoning/execution; S5.4 training/data; S7 trustworthiness; S8 future directions
- **Category:** SURVEY / WEBAGENTS / LFM-BASED WEB AUTOMATION
- **Paper type:** WebAgents survey
- **Priority:** P1
- **BibTeX key:** ning2025surveywebagents

---

## Simple understanding

This is the most directly relevant survey for your thesis because it focuses specifically on **WebAgents**.

It reviews web agents from three major perspectives:

```text
architecture
training
trustworthiness
```

It also breaks the web-agent pipeline into:

```text
perception
planning & reasoning
execution
```

For the thesis, this paper is very useful as a roadmap for S4, S5, S7, and S8.

---

## Notes

- **Core idea:**
  Survey large-foundation-model-based WebAgents for web automation, focusing on architectures, training, and trustworthiness.

- **Key finding:**
  The survey frames WebAgents as agents that perceive web environments, reason over action sequences, and execute interactions to complete user instructions.

- **Limitation:**
  It is a survey, so primary papers are still needed for exact system performance.

- **Additional limitation:**
  The field changes quickly, so later systems may not be covered.

- **Additional limitation:**
  It may include broad web applications beyond the exact focus of generalized web automation and data extraction.

- **Connects to:**
  Perception, planning/reasoning, execution, training, data, safety, robustness, privacy, and generalizability.

- **Use in thesis:**
  Use as a key web-specific survey reference and roadmap.

---

## Thesis-ready paragraph

Ning et al. provide a focused survey of WebAgents, defined as large-foundation-model-empowered agents that complete web tasks by perceiving web environments, reasoning over action sequences, and executing interactions. The survey organizes the literature around architectures, training, and trustworthiness, making it highly relevant to a thesis on LLM-based agents for generalized web automation and data extraction. Its architecture breakdown—perception, planning and reasoning, and execution—maps directly onto the technical challenges identified in S4. Its training and trustworthiness sections also support later discussions of data, fine-tuning, post-training, safety, robustness, privacy, and generalization. As a survey, it should guide structure and coverage, while primary papers should support detailed empirical claims.

---

## Why this paper matters for my thesis

This paper matters because it is directly about your thesis domain.

It gives the clean web-agent pipeline:

```text
perception → planning/reasoning → execution
```

And it gives the broader study dimensions:

```text
architecture
training
trustworthiness
```

This can help structure your thesis chapters or subsections.

---

## Important concepts to remember

### 1. WebAgent

An AI agent that automates web tasks according to user instructions.

### 2. Perception

Observing website state using screenshots, HTML, DOM, and previous actions.

### 3. Planning and reasoning

Generating action sequences to complete tasks.

### 4. Execution

Interacting with the website through browser actions or tools.

### 5. Training

Prompting, pretraining, fine-tuning, post-training, and data construction.

### 6. Trustworthiness

Safety, robustness, privacy, and generalizability.

---

## Key evidence from the paper

### Figure 1

Illustrates WebAgents perceiving, reasoning, and executing web tasks.

### Architecture section

Reviews perception, planning/reasoning, and execution.

### Training section

Covers data and training strategies for WebAgents.

### Trustworthiness section

Covers safety, robustness, privacy, and generalizability.

---

## Connection to earlier and later papers

### Connection to S4

This survey summarizes the web-agent evolution that S4 traces historically.

### Connection to S5

Its perception/planning/execution structure maps directly onto S5 technical sections.

### Connection to S7

Its trustworthiness section supports safety, privacy, robustness, and generalization discussion.

---

## Connection to later thesis sections

- **S5.1 — Evaluation:**
  Benchmarks and metrics.
- **S5.2 — Perception:**
  HTML, DOM, screenshots, and observation design.
- **S5.3 — Planning/Reasoning/Execution:**
  Action sequence generation and web interaction.
- **S5.4 — Training:**
  Data, prompting, fine-tuning, post-training.
- **S7 — Trustworthiness:**
  Safety, robustness, privacy, generalizability.
- **S8 — Future directions:**
  Deployment and open challenges.

---

## Limitation connected to thesis

This survey is a roadmap, not a primary system.

Use it to organize the field, but support detailed claims with:

```text
World of Bits
WebGPT
WebShop
WebAgent
SeeAct
WebVoyager
AutoWebGLM
WALT
```


---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High but selective
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Introduction
  - Architecture section
  - Training section
  - Trustworthiness section
  - Future directions

---

## One-sentence summary

This WebAgents survey is a key structure paper for the thesis because it directly organizes web automation agents around architecture, training, and trustworthiness.

---

## BibTeX

```bibtex
@article{ning2025surveywebagents,
  title   = {A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models},
  author  = {Ning, Liangbo and Liang, Ziran and Jiang, Zhuohang and Qu, Haohao and Ding, Yujuan and Fan, Wenqi and Wei, Xiao-yong and Lin, Shanru and Liu, Hui and Yu, Philip S. and Li, Qing},
  journal = {arXiv preprint arXiv:2503.23350},
  year    = {2025}
}
```

---

## Source links

- https://arxiv.org/abs/2503.23350


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\2025-09 - WALT- Web Agents that Learn Tools.md

# Paper 299 — WALT: Web Agents that Learn Tools

## Metadata

- **Title:** WALT: Web Agents that Learn Tools
- **Authors:** Viraj Prabhu, Yutong Dai, Matthew Fernandez, Jing Gu, Krithika Ramakrishnan, Yanqi Luo, Silvio Savarese, Caiming Xiong, Junnan Li, Zeyuan Chen, Ran Xu
- **Year:** 2025
- **Venue:** arXiv preprint / under review
- **DOI:** 10.48550/arXiv.2510.01524
- **arXiv ID:** arXiv:2510.01524
- **Thesis section:** S4 — Evolution of Web Agent Systems
- **Cross-links:** S5.2 site-function abstraction; S5.3 tool-based planning; S5.4 tool learning; S5.5 brittle UI-action failures; S6 extraction/tools; S8 efficient deployment
- **Category:** WEB AGENT / TOOL LEARNING / ACTION ABSTRACTION
- **Paper type:** Method / tool-learning web agent
- **Priority:** P1
- **BibTeX key:** prabhu2025walt

---

## Simple understanding

WALT is a forward-looking web-agent paper that shifts from step-by-step UI actions to **learned website tools**.

Most web agents operate like this:

```text
click → type → click → scroll → click → inspect → click
```

WALT argues that humans often think at a higher level:

```text
search(query)
filter(criteria)
sort(order)
create(listing)
edit(item)
delete(item)
comment(text)
upvote(item)
```

The system reverse-engineers website-provided functionality into reusable invocable tools. These tools expose robust functions already built into websites.

For my thesis, WALT matters because it suggests a next-generation direction for web automation: agents should not always reason over primitive clicks; they should discover and call higher-level website tools when possible.

---

## Notes

- **Core idea:**
  Reverse-engineer website functionality into reusable invocable tools, reducing brittle step-by-step UI reasoning.

- **Key finding:**
  WALT reports state-of-the-art success on WebArena and VisualWebArena, with fewer steps and less LLM-dependent reasoning.

- **Limitation:**
  Tool discovery must be performed per website and may require expensive upfront exploration.

- **Additional limitation:**
  Learned tools can break when websites change.

- **Additional limitation:**
  Reverse-engineering URL parameters or hidden functionality may raise security, privacy, or terms-of-service concerns.

- **Additional limitation:**
  Tool abstraction helps repeated functions but may not help rare one-off interactions.

- **Connects to:**
  Toolformer, MRKL, WebArena, VisualWebArena, skill discovery, API-using agents, and deployment efficiency.

- **Use in thesis:**
  Use as a forward-looking paper showing the transition from primitive UI actions to site-level tool abstraction.

---

## Thesis-ready paragraph

Prabhu et al. introduce WALT, a framework for web agents that learn reusable tools by reverse-engineering website-provided functionality. Instead of executing long fragile sequences of primitive UI actions, WALT exposes high-level operations such as search, filter, sort, create, edit, delete, comment, or upvote as callable tools with validated schemas. This is highly relevant to generalized web automation because it shifts the burden from step-by-step UI interaction toward robust, reusable site-level abstractions. WALT’s results on WebArena and VisualWebArena suggest that tool-based abstraction can improve success and efficiency. However, the approach also introduces new challenges: tools must be discovered, validated, maintained, and used safely as websites change. For this thesis, WALT provides an important future direction: combining LLM planning with learned website-specific tools for more reliable automation.

---

## Why this paper matters for my thesis

This paper matters because it addresses one of the biggest practical problems in web automation:

```text
primitive UI trajectories are brittle
```

A small website change can break:

```text
click element 4 → type → click element 9
```

But a high-level tool can be more stable:

```text
search(query="blue kayak", category="Boats", sort_by="price")
```

For data extraction, this is important because many websites already provide useful functions:

```text
search
filter
sort
export
download
next page
open details
```

A future web agent should discover and use these functions instead of always clicking manually.

---

## Important concepts to remember

### 1. Website-provided functionality

Built-in operations such as search, filter, sort, post, edit, delete, comment, or vote.

### 2. Tool discovery

Identifying reusable site functions and exposing them as callable tools.

### 3. Demonstrate-generate-validate loop

Explore functionality, generate tools, then test and validate them.

### 4. URL-parameter promotion

Replacing UI sequences with robust URL/API-like parameterized operations when possible.

### 5. Tool-based abstraction

Replacing many primitive UI steps with one high-level operation.

### 6. Agentic fallback

Using limited agentic steps when deterministic tool execution is insufficient.

---

## Key evidence from the paper

### Figure 1

Contrasts fragile primitive UI action sequences with one high-level tool call.

### Tool coverage

The paper describes tools for discovery, communication, and content management.

### Reported results

The paper reports strong results on WebArena and VisualWebArena.

### Efficiency

It reports fewer steps on average and improved success through discovered tools, multimodal DOM parsing, and external verification.

---

## Connection to earlier and later papers

### Connection to Toolformer

Toolformer teaches models to use tools.

WALT discovers website-specific tools for web automation.

```text
Toolformer = language model learns API calls
WALT = web agent learns site tools
```

### Connection to MRKL

MRKL argues for modular expert systems.

WALT creates website-specific modules/tools.

### Connection to WebAgent and AutoWebGLM

WebAgent/AutoWebGLM operate through programmatic actions or trained policies.

WALT abstracts common website functionality into reusable tools.

---

## Connection to later thesis sections

- **S5.2 — Representation:**
  Website-function abstraction and action representation.
- **S5.3 — Planning:**
  Planning over tools instead of primitive UI actions.
- **S5.4 — Training/Learning:**
  Tool discovery and validation.
- **S5.5 — Failure Modes:**
  Brittle UI trajectories and maintenance failure.
- **S6 — Extraction:**
  Website tools for search, filtering, sorting, and data access.
- **S8 — Deployment:**
  Tool maintenance, monitoring, efficiency, and safety.

---

## Limitation connected to thesis

WALT is promising but introduces a new maintenance problem.

It improves:

```text
primitive UI actions → reusable site tools
```

but it still needs:

- safe tool discovery,
- validation,
- monitoring after website changes,
- permission and privacy controls,
- fallback actions,
- and extraction verification.

---

## Reading decision

- **Read fully?** Yes
- **Depth needed:** High
- **Main use:** S4 P1 support paper for the evolution of web-agent systems
- **Most important parts:**
  - Abstract
  - Figure 1
  - Tool discovery method
  - Demonstrate-generate-validate loop
  - WebArena results
  - VisualWebArena results
  - Ablations
  - Limitations

---

## One-sentence summary

WALT reframes web automation from brittle UI-step reasoning to reusable website-tool invocation, but tool discovery and maintenance become new deployment challenges.

---

## BibTeX

```bibtex
@article{prabhu2025walt,
  title   = {WALT: Web Agents that Learn Tools},
  author  = {Prabhu, Viraj and Dai, Yutong and Fernandez, Matthew and Gu, Jing and Ramakrishnan, Krithika and Luo, Yanqi and Savarese, Silvio and Xiong, Caiming and Li, Junnan and Chen, Zeyuan and Xu, Ran},
  journal = {arXiv preprint arXiv:2510.01524},
  year    = {2025},
  doi     = {10.48550/arXiv.2510.01524}
}
```

---

## Source links

- https://arxiv.org/abs/2510.01524


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_full_complete_detailed_markdowns\S4_P1_full_complete_reading_index.md

# S4 P1 Full Complete Markdown Notes — Reading Index

These notes follow the same detailed structure as the uploaded Chain-of-Thought example: metadata, simple understanding, notes, thesis paragraph, why it matters, concepts, evidence, connections, later-section links, thesis limitation, reading decision, summary, BibTeX, and source links.

## Files

- Paper 285 — **Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration** — `2018-02 - Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration.md`
- Paper 286 — **DOM-Q-NET: Grounded RL on Structured Language** — `2019-02 - DOM-Q-NET- Grounded RL on Structured Language.md`
- Paper 287 — **A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis** — `2023-07 - A Real-World WebAgent with Planning Long Context Understanding and Program Synthesis.md`
- Paper 288 — **Large Language Model Powered Agents in the Web** — `2024-05 - Large Language Model Powered Agents in the Web.md`
- Paper 289 — **AutoWebGLM: Bootstrap and Reinforce A Large Language Model-based Web Navigating Agent** — `2024-10 - AutoWebGLM- Bootstrap and Reinforce A Large Language Model-based Web Navigating Agent.md`
- Paper 290 — **Agent S: An Open Agentic Framework that Uses Computers Like a Human** — `2024-10 - Agent S- An Open Agentic Framework that Uses Computers Like a Human.md`
- Paper 291 — **AutoGLM: Autonomous Foundation Agents for GUIs** — `2024-10 - AutoGLM Autonomous Foundation Agents for GUIs.md`
- Paper 292 — **Large Language Model-Brained GUI Agents: A Survey** — `2024-11 - Large Language Model-Brained GUI Agents- A Survey - preprint version.md`
- Paper 293 — **AutoWebGLM: A Large Language Model-based Web Navigating Agent** — `2024-12 - AutoWebGLM A Large Language Model-based Web Navigating Agent.md`
- Paper 294 — **GUI Agents with Foundation Models: A Comprehensive Survey** — `2025-02 - GUI Agents with Foundation Models- A Comprehensive Survey.md`
- Paper 295 — **A Survey on (M)LLM-Based GUI Agents** — `2025-06 - A Survey on (M)LLM-Based GUI Agents.md`
- Paper 296 — **Large Language Model-Brained GUI Agents: A Survey** — `2025-06 - Large Language Model-Brained GUI Agents- A Survey.md`
- Paper 297 — **GUI Agents: A Survey** — `2025-07 - GUI Agents- A Survey.md`
- Paper 298 — **A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models** — `2025-08 - A Survey of WebAgents- Towards Next-Generation AI Agents for Web Automation with Large Foundation Models.md`
- Paper 299 — **WALT: Web Agents that Learn Tools** — `2025-09 - WALT- Web Agents that Learn Tools.md`

## Suggested reading order

```text
Pre-LLM/RL web agents:
285 WGE
286 DOM-Q-NET

Real-world LLM web agents:
287 WebAgent
293 AutoWebGLM KDD version
289 AutoWebGLM extended/preprint version

Broader GUI/computer-use agents:
290 Agent S
291 AutoGLM

Survey/context papers:
288 WWW tutorial
292 GUI survey preprint
296 GUI survey TMLR version
294 GUI foundation models survey
295 (M)LLM GUI survey
297 GUI Agents survey
298 WebAgents survey

Forward-looking tool abstraction:
299 WALT
```

For final thesis citation, prefer:
- **AutoWebGLM KDD 2024** over the earlier AutoWebGLM preprint.
- **Large Language Model-Brained GUI Agents TMLR 2025** over the earlier preprint.
- Primary system papers for performance claims.
- Surveys for taxonomy, positioning, and roadmap.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\P1\S4_P1_reading_order_index.md

# S4 P1 Reading Order

Use these after S4 P0 and before writing/refining S4 synthesis.

## Files

285. **Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration** — P1 — `2018-02 - Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration.md`
286. **DOM-Q-NET: Grounded RL on Structured Language** — P1 — `2019-02 - DOM-Q-NET- Grounded RL on Structured Language.md`
287. **A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis** — P1 — `2023-07 - A Real-World WebAgent with Planning Long Context Understanding and Program Synthesis.md`
288. **Large Language Model Powered Agents in the Web** — P1 — `2024-05 - Large Language Model Powered Agents in the Web.md`
289. **AutoWebGLM: Bootstrap and Reinforce A Large Language Model-based Web Navigating Agent** — P1 — `2024-10 - AutoWebGLM- Bootstrap and Reinforce A Large Language Model-based Web Navigating Agent.md`
290. **Agent S: An Open Agentic Framework that Uses Computers Like a Human** — P1 — `2024-10 - Agent S- An Open Agentic Framework that Uses Computers Like a Human.md`
291. **AutoGLM: Autonomous Foundation Agents for GUIs** — P1 — `2024-10 - AutoGLM Autonomous Foundation Agents for GUIs.md`
292. **Large Language Model-Brained GUI Agents: A Survey** — P1 — `2024-11 - Large Language Model-Brained GUI Agents- A Survey - preprint version.md`
293. **AutoWebGLM: A Large Language Model-based Web Navigating Agent** — P1 — `2024-12 - AutoWebGLM A Large Language Model-based Web Navigating Agent.md`
294. **GUI Agents with Foundation Models: A Comprehensive Survey** — P1 — `2025-02 - GUI Agents with Foundation Models- A Comprehensive Survey.md`
295. **A Survey on (M)LLM-Based GUI Agents** — P1 — `2025-06 - A Survey on (M)LLM-Based GUI Agents.md`
296. **Large Language Model-Brained GUI Agents: A Survey** — P1 — `2025-06 - Large Language Model-Brained GUI Agents- A Survey.md`
297. **GUI Agents: A Survey** — P1 — `2025-07 - GUI Agents- A Survey.md`
298. **A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models** — P1 — `2025-08 - A Survey of WebAgents- Towards Next-Generation AI Agents for Web Automation with Large Foundation Models.md`
299. **WALT: Web Agents that Learn Tools** — P1 — `2025-09 - WALT- Web Agents that Learn Tools.md`

## Suggested reading logic

```text
Pre-LLM/RL web agents:
285 WGE → 286 DOM-Q-NET

Real-web LLM agents:
287 WebAgent → 293 AutoWebGLM final → 289 AutoWebGLM earlier version

Live/GUI foundation agents:
290 Agent S → 291 AutoGLM → 299 WALT

Surveys/context:
288 WWW tutorial → 294/295/296/297 GUI surveys → 298 WebAgents survey
```

For the final literature review, prefer primary system papers for performance claims and surveys for taxonomy/positioning.


---

## Synthesis / Writing Notes (4 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\Writing\S4_mini_synthesis_from_P0.md

# S4 Mini-Synthesis — Evolution of Web Agent Systems  
## Based on S4 P0 papers: World of Bits, WebGPT, WebShop, SeeAct, WebVoyager

## 1. Narrative

Section S4 explains how web-agent systems evolved from early reinforcement-learning environments to modern multimodal LLM agents operating on live websites.

The S4 P0 papers show a clear progression:

```text
World of Bits
→ WebGPT
→ WebShop
→ SeeAct
→ WebVoyager
```

Conceptually, this progression can be summarized as:

```text
web as RL environment
→ text-based LLM browsing
→ scalable grounded web interaction
→ multimodal web-agent grounding
→ end-to-end live multimodal web automation
```

This section is important because it moves the literature review from **general LLM-agent architectures** in S3 to **web-specific agent systems**. S3 explained how LLMs become agents through reasoning, acting, memory, tools, and planning. S4 shows how those agentic ideas are instantiated in the web environment, where agents must deal with webpages, DOM structures, screenshots, browser actions, search, navigation, dynamic content, and task success evaluation.

The central message of S4 is:

```text
Web agents evolved from low-level UI-control environments to LLM/LMM-powered systems, but reliable generalized web automation still depends on grounding, planning, verification, safety, and deployment realism.
```

---

## 2. Paper-level synthesis

### 2.1 World of Bits — The web as an agent environment

World of Bits is the historical starting point of S4. It frames the web as an open-domain interactive environment for agents.

The agent observes:

```text
screen pixels
DOM elements with coordinates
reward
```

and acts through:

```text
keyboard events
mouse events
```

This was a major shift because the web was no longer treated only as a source of text or documents. Instead, the web became an environment in which agents must perceive, act, and receive feedback.

World of Bits introduced three levels of web tasks:

```text
MiniWoB → synthetic controlled tasks
FormWoB → cached real flight-booking websites
QAWoB → crowdsourced question-answering tasks on real websites
```

For the thesis, World of Bits is important because it identifies the core technical structure of web automation:

```text
instruction → page observation → grounding → UI action → reward/feedback
```

However, World of Bits also shows why pre-LLM web agents struggled. Behavioral cloning and reinforcement learning achieved limited success, especially on keyboard-heavy and compound tasks. This reveals several early bottlenecks:

```text
sparse rewards
long horizons
low-level actions
difficult exploration
weak language understanding
weak DOM/pixel grounding
```

Therefore, World of Bits provides the pre-LLM foundation and motivates the transition toward language-model-based web agents.

---

### 2.2 WebGPT — LLM browsing with references and human feedback

WebGPT marks the transition from pre-LLM web agents to LLM-based browsing agents.

Unlike World of Bits, WebGPT does not control a full visual browser with mouse and keyboard. Instead, it creates a **text-based browsing environment** where GPT-3 can issue commands such as:

```text
Search
Click
Find in page
Quote
Scroll
Back
End
```

The system is trained using:

```text
human demonstrations → behavior cloning
human comparisons → reward model
reward model → rejection sampling / RL
```

The key innovation is that the model must collect **references** while browsing. These references support the final answer and make human evaluation of factual accuracy easier.

For the thesis, WebGPT is important because it shows that LLMs can use the web as an external information source. This connects directly to web information extraction, source-grounded question answering, and verification.

However, WebGPT is still narrow. It is mainly a long-form question-answering system. It does not solve general web automation because it does not handle:

```text
visual layout
forms
buttons
calendars
dropdowns
dynamic websites
structured extraction
DOM-level action grounding
general browser workflows
```

Thus, WebGPT is a turning point, but not a complete generalized web agent.

---

### 2.3 WebShop — Scalable grounded language interaction

WebShop introduces a scalable simulated e-commerce environment for grounded language agents.

The task is:

```text
read a shopping instruction
→ search for products
→ inspect results
→ open product pages
→ choose options
→ buy the matching product
```

WebShop is important because it combines:

```text
real-world product data
natural-language instructions
sequential decision-making
semantic web actions
automatic reward
human demonstrations
sim-to-real transfer
```

Compared with World of Bits, WebShop abstracts away low-level mouse and keyboard actions. Instead, it uses a semantic action space:

```text
search[query]
choose[button/product/option]
```

This makes the environment more compatible with language agents.

For the thesis, WebShop is crucial because it shows that web automation is not only about navigation. It requires language grounding, query reformulation, option selection, comparison, exploration, backtracking, and memory. These are also central to web data extraction, where an agent must find relevant pages, compare candidate information, and verify extracted values.

However, WebShop remains limited because it is simulated and e-commerce-specific. It does not fully represent arbitrary live websites, authentication, CAPTCHAs, dynamic JavaScript, pop-ups, real-time content, or unrestricted UI interaction.

Therefore, WebShop is a cornerstone benchmark for grounded web interaction, but not a complete generalization benchmark.

---

### 2.4 SeeAct — GPT-4V can act on the web if grounded

SeeAct introduces a modern multimodal view of web agents.

The paper’s core argument is:

```text
GPT-4V has strong potential as a generalist web agent,
but only if its plans can be grounded into correct browser actions.
```

SeeAct separates web-agent behavior into two stages:

```text
Action generation:
the model decides what should be done next in natural language

Action grounding:
the system converts that natural-language action into an executable browser event
```

This distinction is very important for the thesis because it shows that planning and grounding are different problems. A model may correctly say:

```text
Click the “Find Your Truck” button.
```

but still fail if it cannot identify the exact HTML element or visual region corresponding to that button.

SeeAct evaluates grounding strategies such as:

```text
element attributes
textual choices
image annotation
oracle grounding
```

The paper shows that GPT-4V performs strongly with oracle grounding, but automatic grounding remains far below oracle performance. This identifies **element grounding** as one of the central bottlenecks for web agents.

For the thesis, SeeAct feeds directly into S5.2 because it shows that multimodal understanding alone is insufficient. Web agents need precise alignment between:

```text
visual screenshot
HTML/DOM element
operation type
input value
browser event
```

---

### 2.5 WebVoyager — End-to-end live multimodal web automation

WebVoyager represents the modern end-to-end multimodal web-agent paradigm.

Unlike WebShop, it does not operate only in a simulated e-commerce environment. Unlike WebGPT, it is not limited to text browsing. WebVoyager uses a live browser and real websites.

Its loop is:

```text
user task
→ screenshot + interactive element text
→ LMM thought
→ browser action
→ new observation
→ repeat
→ final answer
```

The agent uses screenshots as the primary input and overlays numerical labels on interactive elements. This helps the model choose actions such as:

```text
Click [10]
Type [17]: search query
Scroll
Back
Answer
```

WebVoyager also introduces a benchmark of 643 tasks across 15 popular websites and proposes GPT-4V-based automatic trajectory evaluation. This is important because online web-agent evaluation is difficult and expensive.

For the thesis, WebVoyager is a major S4 paper because it shows the current direction of web-agent systems:

```text
live websites
multimodal input
marked interactive elements
ReAct-style reasoning
end-to-end task completion
automatic evaluation
```

However, it also shows that modern web agents still fail in predictable ways:

```text
navigation stuck
visual grounding errors
hallucination
prompt misalignment
dense text handling
long trajectories
```

These failure categories directly motivate S5.5.

---

## 3. Main conceptual contribution of S4

The main contribution of S4 is to show that web agents are not just general agents applied to a new domain. The web creates specific technical requirements.

A web agent must solve:

```text
webpage perception
DOM and visual grounding
browser action execution
search and navigation
long-horizon planning
state tracking
query reformulation
structured extraction
verification
safe interaction with live websites
```

The S4 P0 papers show the evolution of these requirements:

| Stage | Paper | Main contribution | Remaining gap |
|---|---|---|---|
| Web as environment | World of Bits | Web interaction as RL with pixels, DOM, mouse/keyboard | Low-level actions, sparse rewards, weak language reasoning |
| LLM browsing | WebGPT | GPT-3 uses text browser and references with human feedback | Text-only QA, not full web automation |
| Scalable grounded interaction | WebShop | Large-scale e-commerce benchmark with semantic actions and rewards | Simulated, domain-specific, limited action space |
| Multimodal grounding | SeeAct | GPT-4V can plan well if grounding is solved | Element grounding remains bottleneck |
| Live multimodal automation | WebVoyager | End-to-end LMM agent on real websites | Still fails through grounding, loops, hallucination, evaluation limits |

---

## 4. S4 narrative arc

The S4 narrative can be written as five steps:

```text
Step 1 — World of Bits:
The web becomes an interactive environment for agents.

Step 2 — WebGPT:
LLMs begin to browse the web through text commands and evidence collection.

Step 3 — WebShop:
Web-agent evaluation becomes scalable through realistic but simulated grounded interaction.

Step 4 — SeeAct:
Large multimodal models show strong web-agent potential, but grounding becomes the central bottleneck.

Step 5 — WebVoyager:
End-to-end multimodal agents operate on live websites, exposing real deployment and evaluation challenges.
```

This creates the following conceptual arc:

```text
environment
→ browsing
→ grounded interaction
→ multimodal grounding
→ live end-to-end automation
```

---

## 5. Refined gap after S4 P0

After S3, the gap was:

```text
General LLM-agent architectures provide the control logic of agency, but web automation requires grounding that control logic in real browser environments with reliable perception, action, verification, and safety.
```

After S4 P0, the gap becomes more web-specific:

```text
Modern web agents can browse, search, plan, and act on webpages, but reliable generalized web automation remains limited by grounding, long-horizon robustness, verification, safety, and realistic evaluation.
```

S4 shows that web agents can now:

```text
observe webpages
use DOM or screenshots
search and navigate
interact with buttons and text fields
follow natural-language tasks
collect references
use multimodal reasoning
operate on live websites
```

But they still do not fully solve:

```text
precise DOM/visual grounding
dynamic page state tracking
robust long-horizon planning
safe irreversible actions
structured data extraction verification
handling popups/CAPTCHAs/login
dense text and visual ambiguity
multi-page memory
online/offline evaluation mismatch
cost, latency, and reliability at deployment
```

So the refined S4 gap is:

```text
Web-agent systems have moved from controlled environments to live multimodal interaction, but the core unsolved problem is reliable grounding and verification across diverse, dynamic, real-world websites.
```

---

## 6. Thesis connection

For the thesis topic, **“LLM-based agents for generalized web automation and data extraction,”** S4 supports five major claims.

### Claim 1 — The web is a natural but difficult agent environment

World of Bits shows that the web is an open-domain environment with rich tasks, visual interfaces, DOM structures, and human-like actions. However, early RL methods struggled, especially on compound and keyboard-heavy tasks.

### Claim 2 — LLMs make web browsing more language-aware

WebGPT shows that LLMs can use a browser-like environment to search, navigate, collect evidence, and synthesize answers. This supports the idea that LLMs can serve as the reasoning and information-access core of web agents.

### Claim 3 — Scalable benchmarks require semantic actions and automatic rewards

WebShop shows that web-agent benchmarks can be scaled using realistic data, natural-language instructions, semantic actions, and programmatic rewards. This is important for studying grounded language interaction at scale.

### Claim 4 — Multimodal models improve web perception but do not solve grounding

SeeAct shows that GPT-4V has strong potential for web agents, but grounding natural-language plans into precise HTML elements and operations remains a major bottleneck.

### Claim 5 — Live-web systems expose real deployment failures

WebVoyager shows that end-to-end multimodal agents can operate on live websites, but failures such as navigation loops, visual grounding errors, hallucination, and prompt misalignment remain serious obstacles.

---

## 7. Thesis-ready synthesis paragraph

The evolution of web-agent systems shows a progression from early reinforcement-learning environments to modern multimodal LLM agents operating on live websites. World of Bits introduced the web as an open-domain interactive environment where agents observe pixels and DOM elements and act through keyboard and mouse commands. This established the basic perception-action structure of web automation but also revealed the limitations of low-level RL under sparse rewards and long-horizon interaction. WebGPT shifted the field toward LLM-based browsing by fine-tuning GPT-3 to search, navigate, quote references, and answer long-form questions using human feedback. WebShop then provided a scalable grounded web-interaction benchmark, using realistic e-commerce data, natural-language instructions, semantic actions, and automatic rewards. More recent systems move from text-based or simulated interaction to multimodal live-web agents. SeeAct shows that GPT-4V can generate strong web-action plans if oracle grounding is available, but automatic element grounding remains a major bottleneck. WebVoyager demonstrates an end-to-end multimodal web agent that interacts with real websites using screenshots, labeled elements, and step-by-step reasoning, achieving substantial task success but still failing through navigation loops, grounding errors, hallucination, and prompt misalignment. Together, these papers show that LLM-based web agents have become increasingly realistic and capable, but generalized web automation and data extraction still require robust DOM and visual grounding, long-horizon planning, state tracking, verification, safety constraints, and deployment-aware evaluation.

---

## 8. Limitations connected to the thesis

### 8.1 World of Bits limitation — low-level control is difficult

World of Bits uses raw keyboard and mouse actions.

For generalized web automation, this matters because low-level actions create a very large action space. The agent must learn where to move, click, type, drag, and scroll from sparse rewards. This motivates modern web agents that use higher-level semantic actions and LLM reasoning.

### 8.2 World of Bits limitation — reproducibility vs realism

FormWoB caches HTTP traffic to make real websites reproducible.

For the thesis, this matters because web-agent evaluation must balance two competing goals:

```text
reproducibility
realistic live-web behavior
```

This tension continues in later offline vs online evaluation debates.

### 8.3 WebGPT limitation — text browsing is not full automation

WebGPT can search, click, quote, and answer, but it does not interact with full visual web interfaces.

For generalized web automation, this matters because many tasks require forms, calendars, dropdowns, visual layout, account state, and structured extraction.

### 8.4 WebGPT limitation — references can mislead

References improve factual evaluation, but they can be cherry-picked or incomplete.

For web data extraction, this matters because an extracted value must be verified against the right source context, not merely accompanied by a plausible citation.

### 8.5 WebShop limitation — simulated and domain-specific

WebShop is large and realistic in product data, but it remains an e-commerce simulation.

For generalized web automation, this matters because real web tasks span many domains and include live interfaces, pop-ups, login flows, CAPTCHAs, changing layouts, and unpredictable states.

### 8.6 WebShop limitation — agents lack exploration and memory

WebShop shows that humans explore more products, reformulate queries, and remember previous items better than models.

For web extraction, this matters because agents must compare alternatives, backtrack, and remember evidence across pages.

### 8.7 SeeAct limitation — grounding is the bottleneck

SeeAct shows that GPT-4V can generate good plans with oracle grounding, but automatic grounding is much weaker.

For the thesis, this is central: a web agent cannot succeed if it cannot map high-level plans to exact DOM elements, visual targets, and operations.

### 8.8 SeeAct limitation — offline evaluation is incomplete

The paper shows discrepancies between offline and online evaluation because multiple valid plans may solve the same task.

For web-agent evaluation, this matters because fixed reference trajectories may unfairly penalize valid alternative strategies.

### 8.9 WebVoyager limitation — live agents still fail often

WebVoyager identifies major failure categories:

```text
navigation stuck
visual grounding issue
hallucination
prompt misalignment
```

For the thesis, these failures motivate a dedicated failure-mode section and support the need for robust planning, grounding, and verification.

### 8.10 WebVoyager limitation — deployment constraints remain

WebVoyager avoids login and CAPTCHA tasks and still requires careful evaluation.

For real generalized automation, this matters because many practical workflows require authentication, permissions, privacy controls, and safe handling of irreversible actions.

---

## 9. Cross-links to later sections

| Paper | Feeds |
|---|---|
| World of Bits | S5.1 benchmarks, S5.2 DOM/pixel grounding, S5.4 behavioral cloning/RL, S5.5 sparse rewards and low-level action failure, S8 reproducibility |
| WebGPT | S5.4 human feedback, S6 web QA/extraction, S7 references and truthfulness, S8 live web safety |
| WebShop | S5.1 benchmark design, S5.3 exploration/planning, S5.4 imitation/RL, S5.5 search and option-selection failures, S8 sim-to-real |
| SeeAct | S5.1 offline vs online evaluation, S5.2 visual/HTML grounding, S5.3 action generation, S5.5 grounding failure, S7 safety |
| WebVoyager | S5.1 online evaluation, S5.2 multimodal perception, S5.3 end-to-end planning, S5.5 navigation/grounding/hallucination failures, S8 deployment |

---

## 10. Transition to S5

S4 shows the evolution of web-agent systems, but it also reveals that the field has several unresolved technical problems.

S5 should therefore analyze these problems in detail.

The transition question is:

```text
What technical components determine whether a web agent succeeds or fails?
```

S5 should be organized around the main technical dimensions exposed by S4:

```text
S5.1 — Benchmarks and evaluation
How do we measure web-agent success?

S5.2 — Perception, grounding, and interface representation
How does the agent represent DOM, HTML, screenshots, elements, and actions?

S5.3 — Planning and decision-making
How does the agent choose multi-step web actions?

S5.4 — Training strategies and generalization
How do agents learn from demonstrations, rewards, feedback, synthetic data, or memory?

S5.5 — Failure modes
Why do agents fail through loops, grounding errors, hallucinations, weak verification, and unsafe actions?
```

S4 therefore prepares the literature review to move from:

```text
chronological evolution of web agents
```

to:

```text
technical decomposition of web-agent capabilities and limitations
```

---

## 11. Final S4 mini-synthesis

S4 establishes the evolution of web-agent systems from early RL-based platforms to modern multimodal LLM agents. World of Bits introduced the web as an open-domain environment where agents observe pixels and DOM structures and act through keyboard and mouse commands. WebGPT shifted the field toward LLM-based browsing, using GPT-3, a text-based browser, evidence collection, and human feedback for long-form question answering. WebShop introduced a scalable grounded web-interaction benchmark with realistic e-commerce data, natural-language instructions, semantic actions, and automatic rewards. SeeAct showed that GPT-4V has strong potential as a generalist web agent, but only if its action plans can be grounded into precise executable browser actions. WebVoyager demonstrated an end-to-end multimodal agent operating on live websites using screenshots, labeled interactive elements, and step-by-step reasoning.

Together, these papers show that web agents have become increasingly capable and realistic. The field has moved from controlled web tasks and low-level actions toward live multimodal systems that can search, browse, click, type, scroll, and answer. However, the same papers also show that generalized web automation and data extraction remain unsolved. The main open challenges are robust DOM and visual grounding, long-horizon planning, dynamic state tracking, reliable extraction verification, safe handling of live-web actions, and realistic evaluation under deployment constraints. S4 therefore motivates the next section: a technical analysis of benchmarks, grounding, planning, training, and failure modes in LLM-based web agents.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\Writing\S4_refined_synthesis_after_P1.md

# S4 Refined Synthesis — Evolution of Web Agent Systems
## Updated after S4 P0 + S4 P1 papers

## 1. What changed after adding S4 P1

The S4 P0 synthesis established the main historical arc:

```text
World of Bits
→ WebGPT
→ WebShop
→ SeeAct
→ WebVoyager
```

This gave the first web-agent progression:

```text
web as RL environment
→ text-based LLM browsing
→ scalable grounded web interaction
→ multimodal grounding
→ end-to-end live multimodal web automation
```

After adding the S4 P1 papers, the section becomes broader and more technically complete. The refined S4 narrative is now:

```text
World of Bits
→ Workflow-Guided Exploration
→ DOM-Q-NET
→ WebGPT
→ WebShop
→ WebAgent
→ SeeAct
→ WebVoyager
→ AutoWebGLM
→ Agent S / AutoGLM
→ WALT
→ WebAgent and GUI-agent surveys
```

Conceptually, this means S4 is no longer only a chronological history of web agents. It becomes a full evolution from:

```text
low-level RL browser control
→ DOM-aware RL
→ LLM browsing
→ simulated grounded web interaction
→ real-world HTML-specialized agents
→ multimodal live-web agents
→ trained/deployable web agents
→ general GUI/computer-use agents
→ tool-based web automation
```

The P1 papers add five important refinements:

1. **Pre-LLM web agents were already struggling with exploration and grounding.**  
   Workflow-Guided Exploration and DOM-Q-NET show that sparse rewards, low-level actions, and DOM representation were central problems before LLMs.

2. **Real-world websites require long HTML handling and open-ended action generation.**  
   WebAgent shows that simulated websites are too simple compared with real websites, where HTML is long, messy, dynamic, and task-irrelevant.

3. **Training and bootstrapping matter, not only prompting.**  
   AutoWebGLM shows that smaller open models can become competitive web-navigation agents through HTML simplification, trajectory data, curriculum learning, RL, and rejection sampling finetuning.

4. **Web agents are part of a broader GUI-agent and computer-use-agent movement.**  
   Agent S, AutoGLM, and GUI-agent surveys show that web automation shares core problems with mobile and desktop automation: perception, grounding, planning, memory, action execution, and safety.

5. **The next direction is action abstraction and tool learning.**  
   WALT shifts web automation away from fragile primitive UI actions toward discovered website-level tools such as `search`, `filter`, `sort`, `create`, `edit`, and `delete`.

---

## 2. Refined S4 narrative

Section S4 explains how web-agent systems evolved from early reinforcement-learning environments to modern LLM/LMM-powered agents capable of interacting with real websites and broader graphical user interfaces.

The earliest stage is represented by **World of Bits**, **Workflow-Guided Exploration**, and **DOM-Q-NET**. These papers treat web automation as a sequential decision-making problem. The web page is an environment; the agent observes pixels, DOM structures, or HTML trees; and it acts through mouse, keyboard, click, or type actions. This pre-LLM stage is important because it identifies the core difficulties of web automation before modern LLMs: sparse rewards, large action spaces, long trajectories, demonstration dependence, weak exploration, and DOM grounding.

World of Bits establishes the web as an open-domain interactive environment. Workflow-Guided Exploration then addresses the sparse-reward problem by using demonstrations to induce high-level workflows that constrain exploration. DOM-Q-NET shifts attention to webpage structure by representing the DOM as a graph and learning grounded RL policies over DOM elements. Together, these papers show that web automation is not merely text processing. It requires environment perception, structural grounding, action selection, and sequential feedback.

The second stage begins with **WebGPT**. WebGPT shifts the field from RL web-interface control to LLM-based browsing. Instead of controlling a full browser visually, GPT-3 is fine-tuned to use a text-based browser with commands such as search, click, find, quote, scroll, and end. WebGPT is important because it shows that LLMs can use the web as an external information source and can collect references to support final answers. However, it remains a browser-assisted question-answering system, not a general web automation system. It does not handle visual layout, forms, dynamic pages, DOM-level action grounding, or structured extraction.

The third stage is represented by **WebShop**. WebShop introduces a scalable simulated e-commerce environment where agents follow natural-language shopping instructions, search products, inspect results, choose options, and make purchases. It abstracts away raw mouse and keyboard actions into semantic actions such as `search[query]` and `choose[item]`. WebShop is important because it connects language grounding, product search, exploration, comparison, backtracking, memory, and automatic reward computation. However, it remains domain-specific and simulated.

The fourth stage is real-world LLM web automation, represented strongly by **WebAgent** and **AutoWebGLM**. WebAgent argues that real websites are much harder than simulated ones because they have open-ended actions, long messy HTML, and no predefined action space. It uses HTML-T5 for planning and HTML summarization, and Flan-U-PaLM for grounded program synthesis. AutoWebGLM takes a different but related direction: it builds a trained web-navigation agent on ChatGLM3-6B using HTML simplification, human-AI trajectory data, curriculum learning, reinforcement learning, and rejection sampling finetuning. These papers show that real-world web automation requires specialized observation processing, training data, task decomposition, and self-improvement.

The fifth stage is multimodal and live-web automation, represented by **SeeAct** and **WebVoyager**. SeeAct separates web-agent behavior into action generation and action grounding. It shows that GPT-4V can produce strong high-level action plans, but automatic grounding into exact HTML elements and operations remains the main bottleneck. WebVoyager then builds an end-to-end multimodal web agent that operates on real websites using screenshots, labeled interactive elements, and ReAct-style step-by-step reasoning. Together, these papers show that multimodal models bring web agents closer to human-like browsing, but grounding, navigation loops, hallucination, and evaluation remain major barriers.

The sixth stage broadens web agents into **GUI and computer-use agents**. Agent S uses experience-augmented hierarchical planning, online web knowledge, narrative memory, episodic memory, and an Agent-Computer Interface to operate computers like a human. AutoGLM develops foundation agents for web and mobile GUIs and emphasizes the separation of planning and grounding through an intermediate interface. GUI-agent surveys then place web agents inside a larger automation landscape that includes web browsers, mobile apps, desktop software, cross-platform environments, and large action models. This matters because generalized web automation is part of a broader shift from chatbots to agents that control digital interfaces.

The final forward-looking stage is **WALT**, which argues that web agents should not always rely on brittle step-by-step UI interactions. Instead, they can reverse-engineer website-provided functionality into reusable tools, such as `search`, `filter`, `sort`, `create`, `edit`, `delete`, `comment`, and `upvote`. This suggests a next-generation direction for web automation: combining LLM planning with website-specific tool discovery and validated high-level action abstractions.

---

## 3. Refined S4 architecture/evolution stack

| Stage | Main papers | Main contribution | What it adds to S4 |
|---|---|---|---|
| Web as environment | World of Bits | Webpages as interactive environments with pixels, DOM, rewards, keyboard/mouse actions | Historical foundation |
| Workflow-guided RL | Workflow-Guided Exploration | Demonstrations induce workflows to constrain sparse-reward exploration | Demonstration-guided web RL |
| DOM-aware RL | DOM-Q-NET | Graph neural network over DOM trees and factorized Q-functions | Structured DOM grounding |
| LLM text browsing | WebGPT | GPT-3 uses a text browser, quotes evidence, and learns from human feedback | LLM-based web evidence gathering |
| Grounded simulated web interaction | WebShop | Scalable e-commerce benchmark with semantic actions and automatic rewards | Language-grounded web task benchmark |
| Real-world HTML-specialized agent | WebAgent | Long HTML summarization, task decomposition, Python program synthesis | Real-web HTML and open-ended actions |
| Multimodal grounding | SeeAct | Separates action generation from action grounding; identifies grounding bottleneck | Visual/HTML grounding diagnosis |
| Live multimodal web agent | WebVoyager | End-to-end LMM agent on real websites with screenshots and labeled elements | Live-web multimodal automation |
| Trained web-navigation agent | AutoWebGLM | HTML simplification, browsing traces, curriculum learning, RL, RFT, AutoWebBench | Open trained deployable web agent |
| Computer-use GUI agent | Agent S | Hierarchical planning, web knowledge, narrative/episodic memory, ACI | Cross-application GUI automation |
| Foundation GUI agent | AutoGLM | Intermediate interface, planning-grounding separation, online curriculum RL | Deployable GUI foundation agents |
| Tool-based web automation | WALT | Reverse-engineers website functionality into reusable tools | Future direction beyond primitive UI steps |
| Survey/taxonomy layer | WebAgent + GUI-agent surveys | Architecture, training, evaluation, trustworthiness, roadmap | Organizes S5 and S7/S8 |

---

## 4. Refined conceptual contribution of S4

The central contribution of S4 is to show that **web agents evolved through successive abstractions of the web interface**.

The interface abstraction changes over time:

```text
pixels + mouse/keyboard
→ DOM and HTML structure
→ text browser commands
→ semantic actions
→ programmatic browser actions
→ screenshots + labeled elements
→ simplified HTML + trained action models
→ intermediate GUI interfaces
→ learned website tools
```

This is the key S4 idea:

```text
Progress in web agents is progress in representing, grounding, and abstracting interaction with the web.
```

Early RL agents struggled because the web interface was too large and sparse at the pixel/mouse level. DOM-aware agents improved grounding by using webpage structure. LLM browsing improved language reasoning and evidence gathering. WebShop improved scalable grounded evaluation through semantic actions. WebAgent and AutoWebGLM improved real-web handling through HTML simplification, long-context processing, program synthesis, and training. SeeAct and WebVoyager improved multimodal perception but exposed the grounding bottleneck. Agent S and AutoGLM generalized web automation to computer-use and GUI foundation agents. WALT suggests that future agents may automate websites by discovering reliable high-level tools rather than repeatedly reasoning over primitive clicks.

---

## 5. Refined gap after S4 P1

After S4 P0, the gap was:

```text
Web-agent systems have moved from controlled environments to live multimodal interaction, but the core unsolved problem is reliable grounding and verification across diverse, dynamic, real-world websites.
```

After adding S4 P1, the gap becomes more precise:

```text
Web agents have progressed from RL interface control to trained multimodal and tool-augmented systems, but generalized web automation still lacks robust cross-site grounding, long-horizon reliability, safe execution, verified extraction, and maintainable action abstractions.
```

S4 now shows that web agents can:

```text
operate in browser-like environments
use pixels, DOM, HTML, screenshots, and accessibility trees
browse textually and cite evidence
act semantically in simulated websites
summarize long HTML
generate Python automation programs
use multimodal visual understanding
train smaller open web-navigation models
use memory and hierarchical planning
control broader GUIs
learn or expose website tools
```

But they still do not fully solve:

```text
precise element grounding across arbitrary websites
visual-DOM alignment under dynamic layouts
long-horizon task reliability
safe irreversible action handling
robust verification of extracted data
evaluation beyond fixed trajectories
privacy and permission control
resistance to popups, CAPTCHAs, ads, and authentication
state tracking across multi-page workflows
maintenance when websites change
cost and latency under real deployment
```

Therefore, the refined S4 gap is:

```text
The field has developed increasingly powerful web-agent architectures, but the remaining bottleneck is making their perception, planning, action abstraction, and verification reliable enough for generalized real-world web automation and data extraction.
```

---

## 6. Thesis connection

For the thesis topic, **“LLM-based agents for generalized web automation and data extraction,”** S4 supports seven major claims.

### Claim 1 — Web automation is a sequential decision-making problem

World of Bits, Workflow-Guided Exploration, and DOM-Q-NET show that web automation is not just scraping or text extraction. It is an interactive decision problem:

```text
observe state → choose action → execute → observe new state → continue
```

This supports the thesis framing of web automation as an agentic problem.

### Claim 2 — DOM and interface representation are foundational

DOM-Q-NET, WebAgent, AutoWebGLM, SeeAct, and WebVoyager all show that the way the page is represented strongly determines agent success. Web agents may use:

```text
DOM trees
HTML snippets
simplified HTML
accessibility trees
screenshots
OCR
labeled UI elements
multimodal observations
```

This directly motivates S5.2.

### Claim 3 — LLMs improve instruction following and reasoning but do not remove grounding problems

WebGPT, WebShop, WebAgent, SeeAct, and WebVoyager show that LLMs/LMMs improve browsing, planning, and language grounding. However, SeeAct and WebVoyager show that a correct high-level plan can still fail if the agent cannot ground it into the correct element or operation.

### Claim 4 — Training and experience are needed for robust web agents

Workflow-Guided Exploration, WebAgent, AutoWebGLM, Agent S, and AutoGLM show that prompting alone is insufficient. Web agents benefit from:

```text
demonstrations
workflow constraints
self-experience
curriculum learning
reinforcement learning
rejection sampling finetuning
episodic memory
narrative memory
online learning
```

This motivates S5.4.

### Claim 5 — Generalized web automation is part of broader GUI automation

Agent S, AutoGLM, and the GUI-agent surveys show that web agents are one branch of a larger GUI-agent ecosystem. Many web challenges also appear in mobile and desktop agents:

```text
visual grounding
action abstraction
long-horizon planning
memory
safety
privacy
latency
cross-platform generalization
```

This helps broaden the thesis without losing the web-specific focus.

### Claim 6 — Future web agents may need tool abstraction, not only UI actions

WALT shows that repeatedly clicking and typing is brittle. A more reliable direction is to discover reusable site-level tools:

```text
search(query)
filter(criteria)
sort(order)
create(item)
edit(item)
delete(item)
comment(text)
```

This connects S4 back to S3 tool-use architectures and forward to S6 extraction tools and S8 deployment.

### Claim 7 — Evaluation remains unresolved

World of Bits, WebShop, SeeAct, WebVoyager, AutoWebGLM, and the surveys all expose evaluation problems:

```text
offline vs online evaluation
fixed reference trajectories vs multiple valid solutions
simulated vs live websites
human evaluation vs automatic evaluation
success rate vs extraction correctness
safety and risk evaluation
cost/latency metrics
```

This motivates S5.1.

---

## 7. Refined thesis-ready synthesis paragraph

The evolution of web-agent systems shows a progression from early reinforcement-learning interfaces to modern LLM/LMM-powered agents operating on real websites and broader graphical user interfaces. World of Bits first framed the web as an open-domain interactive environment where agents observe pixels and DOM structures and act through keyboard and mouse events. Workflow-Guided Exploration and DOM-Q-NET then addressed two early bottlenecks of web RL: sparse-reward exploration and DOM-structured action grounding. WebGPT shifted the field toward LLM-based browsing by fine-tuning GPT-3 to search, navigate, quote evidence, and answer questions with human feedback. WebShop introduced scalable grounded web interaction through a simulated e-commerce environment with semantic actions and automatic rewards. More recent systems address the gap between simulated tasks and real websites. WebAgent combines planning, long HTML summarization, and program synthesis to act on real websites, while AutoWebGLM trains an open web-navigation model using simplified HTML, browsing traces, curriculum learning, reinforcement learning, and rejection sampling finetuning. Multimodal systems such as SeeAct and WebVoyager show that large multimodal models can reason over rendered webpages and perform live browser actions, but they also reveal that precise action grounding remains a major bottleneck. Broader GUI-agent systems such as Agent S and AutoGLM extend these ideas to desktop and mobile interfaces through hierarchical planning, memory, intermediate interfaces, and online curriculum learning. Finally, WALT suggests a future direction in which agents reverse-engineer website functionality into reusable tools, reducing reliance on brittle step-by-step UI actions. Together, these works show that web agents have become increasingly capable, but generalized web automation and data extraction still require robust DOM/visual grounding, long-horizon planning, safe execution, verified extraction, realistic evaluation, and deployment-aware action abstractions.

---

## 8. Refined limitations connected to the thesis

### 8.1 Low-level action limitation

Early systems such as World of Bits operate with low-level keyboard and mouse actions.

For generalized web automation, this matters because low-level control creates large action spaces and long trajectories. A data-extraction agent should not always reason at the level of pixels and mouse movements; it needs higher-level abstractions such as DOM elements, semantic actions, API calls, or tools.

### 8.2 Sparse reward and exploration limitation

Workflow-Guided Exploration shows that RL agents struggle when reward appears only after complete task success.

For web automation, this matters because many workflows have delayed success signals. A form may only fail at submission. A product search may only be wrong after comparison. An extraction may look correct but fail later verification.

### 8.3 DOM representation limitation

DOM-Q-NET shows that DOM structure helps, but simplified benchmark DOMs do not fully capture real websites.

For generalized automation, this matters because real DOMs are long, noisy, dynamic, and often disconnected from the visible human interface.

### 8.4 Text-browser limitation

WebGPT shows that LLMs can browse textually and cite evidence, but text browsing is not full browser automation.

For the thesis, this matters because data extraction and web automation often require forms, dropdowns, dynamic widgets, tables, visual layout, authentication, and structured outputs.

### 8.5 Simulated benchmark limitation

WebShop provides scalable grounded evaluation, but it remains a simulated e-commerce environment.

For generalized automation, this matters because real websites are multi-domain, dynamic, and often not reproducible.

### 8.6 Long HTML limitation

WebAgent and AutoWebGLM show that real HTML can exceed model context limits and contain large amounts of irrelevant content.

For web extraction, this matters directly because the agent must compress the page without removing relevant evidence.

### 8.7 Program synthesis limitation

WebAgent uses generated Python programs to act on websites.

For deployment, this matters because generated code can be powerful but risky. It must be sandboxed, constrained, inspected, or verified before execution.

### 8.8 Grounding limitation

SeeAct shows the gap between action generation and action grounding.

For generalized web automation, this is central. The agent may know what to do but fail to select the correct element, operation, or input value.

### 8.9 Live-web reliability limitation

WebVoyager shows that live multimodal agents fail through navigation loops, visual grounding issues, hallucination, and prompt misalignment.

For the thesis, these failures motivate a dedicated failure-mode analysis.

### 8.10 Training-data limitation

AutoWebGLM shows the importance of high-quality web-browsing traces.

For web agents, this matters because collecting representative trajectories across websites, languages, tasks, and failure cases is expensive.

### 8.11 Planning-grounding separation limitation

AutoGLM argues that planning and grounding require separate optimization.

For web agents, this matters because flexible reasoning and precise UI control are different abilities. A single prompt or model may not optimize both well.

### 8.12 Memory limitation

Agent S shows the value of narrative and episodic memory, but memory can also be stale, irrelevant, or wrong.

For web automation, memory must be evidence-grounded and verified, especially when websites change.

### 8.13 Tool-maintenance limitation

WALT shows that learned website tools can reduce brittle UI steps.

However, for deployment, tools must be discovered, validated, updated, and monitored as websites change. This creates a new maintenance problem.

### 8.14 Survey limitation

The GUI-agent and WebAgent surveys provide useful taxonomies, but they do not replace primary system papers.

For thesis writing, use surveys to structure the field and primary papers to support technical and empirical claims.

---

## 9. Updated cross-links to later sections

| Paper | Feeds |
|---|---|
| World of Bits | S5.1 benchmarks, S5.2 DOM/pixel grounding, S5.4 RL/behavioral cloning, S5.5 sparse-reward failures, S8 reproducibility |
| Workflow-Guided Exploration | S5.3 exploration/planning, S5.4 demonstrations/RL, S5.5 sparse rewards and overfitting |
| DOM-Q-NET | S5.2 DOM representation, S5.4 RL/multitask learning, S5.5 large variable action spaces |
| WebGPT | S5.4 human feedback, S6 web QA/extraction, S7 references/truthfulness, S8 live web access risk |
| WebShop | S5.1 scalable benchmark design, S5.3 search/exploration/planning, S5.4 imitation/RL, S8 sim-to-real |
| WebAgent | S5.2 long HTML summarization, S5.3 sub-instruction planning, S5.4 self-experience, S6 programmatic extraction, S8 real-web deployment |
| SeeAct | S5.1 offline vs online evaluation, S5.2 visual/HTML grounding, S5.3 action generation, S5.5 grounding failures, S7 safety |
| WebVoyager | S5.1 online evaluation, S5.2 multimodal perception, S5.3 end-to-end planning, S5.5 navigation/grounding/hallucination failures, S8 deployment |
| AutoWebGLM | S5.1 AutoWebBench, S5.2 HTML simplification, S5.3 task decomposition, S5.4 curriculum/RL/RFT, S5.5 loop/self-check failures, S8 browser extension |
| Agent S | S5.2 GUI grounding, S5.3 hierarchical planning, S5.4 memory/experience, S5.5 GUI failures, S8 cross-platform computer use |
| AutoGLM | S5.2 intermediate interface/grounding, S5.3 planning, S5.4 online curriculum RL, S5.5 error recovery, S8 deployable foundation agents |
| GUI-agent surveys | S5.1 evaluation, S5.2 perception, S5.3 planning/action, S5.4 data/models, S5.5 limitations, S8 roadmap |
| WebAgents survey | S5.1 evaluation, S5.2 perception, S5.3 planning/reasoning/execution, S5.4 training, S7 trustworthiness |
| WALT | S5.2 action/tool abstraction, S5.3 tool-based planning, S5.4 tool learning, S5.5 brittle UI-action failures, S6 extraction tools, S8 maintenance |

---

## 10. How S4 should be written in the thesis

A strong final thesis section for S4 can be organized into six subsections:

### S4.1 Pre-LLM web agents: web as an RL environment

Use:

```text
World of Bits
Workflow-Guided Exploration
DOM-Q-NET
```

Main argument:

```text
Before LLMs, web agents were treated as RL agents in browser environments, but sparse rewards, low-level actions, and DOM grounding made generalization difficult.
```

### S4.2 LLM browsing and evidence-grounded web QA

Use:

```text
WebGPT
```

Main argument:

```text
LLMs introduced stronger language reasoning and evidence-gathering ability, but text-based browsing remained narrower than full web automation.
```

### S4.3 Scalable grounded interaction benchmarks

Use:

```text
WebShop
```

Main argument:

```text
WebShop made web-agent evaluation scalable through realistic product data, semantic actions, and automatic rewards, but remained simulated and domain-specific.
```

### S4.4 Real-world LLM web agents

Use:

```text
WebAgent
AutoWebGLM
```

Main argument:

```text
Real websites require long HTML handling, observation simplification, task decomposition, program synthesis, trajectory data, and web-specific training.
```

### S4.5 Multimodal live-web agents

Use:

```text
SeeAct
WebVoyager
```

Main argument:

```text
LMMs improve visual web understanding, but reliable browser control depends on precise grounding and robust online evaluation.
```

### S4.6 From web agents to GUI/foundation/tool agents

Use:

```text
Agent S
AutoGLM
WALT
GUI-agent surveys
WebAgents survey
```

Main argument:

```text
Web automation is becoming part of a broader GUI-agent and computer-use-agent paradigm, where planning, grounding, memory, action abstraction, trustworthiness, and deployment become central.
```

---

## 11. Final refined S4 synthesis

S4 establishes the evolution of web-agent systems from early RL-based browser environments to modern LLM/LMM-powered agents and emerging tool-based automation. Early systems such as World of Bits, Workflow-Guided Exploration, and DOM-Q-NET framed the web as an interactive decision environment and showed that web automation is difficult because of sparse rewards, low-level actions, long trajectories, and DOM grounding. WebGPT shifted the field toward LLM-based browsing, where a model can search, navigate, quote evidence, and answer questions with human feedback. WebShop then introduced a scalable grounded web-interaction benchmark with semantic actions, realistic e-commerce data, and automatic rewards.

Later systems move closer to real-world web automation. WebAgent addresses real websites through planning, long HTML summarization, and program synthesis. AutoWebGLM shows that trained open LLMs can become competitive web-navigation agents through HTML simplification, browsing traces, curriculum learning, reinforcement learning, and rejection sampling finetuning. SeeAct and WebVoyager introduce the multimodal live-web paradigm: agents use screenshots, visual reasoning, and labeled interactive elements to act on real websites. These systems show strong progress but also reveal the grounding bottleneck, navigation loops, hallucinations, and online evaluation difficulty.

The most recent direction broadens web agents into GUI and computer-use agents. Agent S and AutoGLM show that web automation shares core challenges with desktop and mobile automation: hierarchical planning, memory, intermediate interfaces, action grounding, and online learning. GUI-agent and WebAgent surveys provide the broader taxonomy of perception, planning, action, training, evaluation, and trustworthiness. WALT suggests an important future direction: instead of relying only on fragile primitive UI actions, web agents can discover and invoke high-level website tools.

Overall, S4 shows that web agents have moved from controlled web tasks toward real, multimodal, trained, and tool-augmented systems. However, generalized web automation and data extraction remain unsolved. The main remaining challenges are robust DOM and visual grounding, long-horizon planning, state tracking, verified extraction, safe execution, realistic evaluation, privacy, latency, and maintainable action abstractions. This refined S4 synthesis therefore motivates S5: a technical decomposition of the components that determine web-agent success or failure—benchmarks, perception and grounding, planning, training, and failure modes.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\Writing\S4_refined_synthesis_after_P1_updated_verified.md

# S4 Refined Synthesis — Evolution of Web Agent Systems
## Updated after S4 P0 + S4 P1 papers

## Publication-status update for S4 P1 citations

The S4 narrative remains unchanged, but the final citation metadata should use the verified venue/status below:

| Paper | Final venue/status to use |
|---|---|
| Workflow-Guided Exploration | ICLR 2018 conference paper |
| DOM-Q-NET | ICLR 2019 conference paper |
| WebAgent | ICLR 2024 conference paper |
| Large Language Model Powered Agents in the Web | WWW 2024 Companion tutorial paper |
| AutoWebGLM Bootstrap and Reinforce | arXiv extended/preprint version; use KDD 2024 AutoWebGLM for final citation |
| Agent S | ICLR 2025 Poster |
| AutoGLM | arXiv preprint |
| Large Language Model-Brained GUI Agents preprint | arXiv preprint; use TMLR 2025 version for final citation |
| AutoWebGLM | KDD 2024 conference paper |
| GUI Agents with Foundation Models | arXiv preprint |
| A Survey on (M)LLM-Based GUI Agents | arXiv preprint |
| Large Language Model-Brained GUI Agents | TMLR 2025 |
| GUI Agents: A Survey | Findings of ACL 2025 |
| A Survey of WebAgents | KDD 2025 Tutorial & Survey Track |
| WALT | ICLR 2026 Poster |


## 1. What changed after adding S4 P1

The S4 P0 synthesis established the main historical arc:

```text
World of Bits
→ WebGPT
→ WebShop
→ SeeAct
→ WebVoyager
```

This gave the first web-agent progression:

```text
web as RL environment
→ text-based LLM browsing
→ scalable grounded web interaction
→ multimodal grounding
→ end-to-end live multimodal web automation
```

After adding the S4 P1 papers, the section becomes broader and more technically complete. The refined S4 narrative is now:

```text
World of Bits
→ Workflow-Guided Exploration
→ DOM-Q-NET
→ WebGPT
→ WebShop
→ WebAgent
→ SeeAct
→ WebVoyager
→ AutoWebGLM
→ Agent S / AutoGLM
→ WALT
→ WebAgent and GUI-agent surveys
```

Conceptually, this means S4 is no longer only a chronological history of web agents. It becomes a full evolution from:

```text
low-level RL browser control
→ DOM-aware RL
→ LLM browsing
→ simulated grounded web interaction
→ real-world HTML-specialized agents
→ multimodal live-web agents
→ trained/deployable web agents
→ general GUI/computer-use agents
→ tool-based web automation
```

The P1 papers add five important refinements:

1. **Pre-LLM web agents were already struggling with exploration and grounding.**  
   Workflow-Guided Exploration and DOM-Q-NET show that sparse rewards, low-level actions, and DOM representation were central problems before LLMs.

2. **Real-world websites require long HTML handling and open-ended action generation.**  
   WebAgent shows that simulated websites are too simple compared with real websites, where HTML is long, messy, dynamic, and task-irrelevant.

3. **Training and bootstrapping matter, not only prompting.**  
   The final KDD 2024 AutoWebGLM paper shows that smaller open models can become competitive web-navigation agents through HTML simplification, trajectory data, curriculum learning, RL, and rejection sampling finetuning.

4. **Web agents are part of a broader GUI-agent and computer-use-agent movement.**  
   Agent S (ICLR 2025), AutoGLM, and GUI-agent surveys show that web automation shares core problems with mobile and desktop automation: perception, grounding, planning, memory, action execution, and safety.

5. **The next direction is action abstraction and tool learning.**  
   WALT (ICLR 2026) shifts web automation away from fragile primitive UI actions toward discovered website-level tools such as `search`, `filter`, `sort`, `create`, `edit`, and `delete`.

---

## 2. Refined S4 narrative

Section S4 explains how web-agent systems evolved from early reinforcement-learning environments to modern LLM/LMM-powered agents capable of interacting with real websites and broader graphical user interfaces.

The earliest stage is represented by **World of Bits**, **Workflow-Guided Exploration**, and **DOM-Q-NET**. These papers treat web automation as a sequential decision-making problem. The web page is an environment; the agent observes pixels, DOM structures, or HTML trees; and it acts through mouse, keyboard, click, or type actions. This pre-LLM stage is important because it identifies the core difficulties of web automation before modern LLMs: sparse rewards, large action spaces, long trajectories, demonstration dependence, weak exploration, and DOM grounding.

World of Bits establishes the web as an open-domain interactive environment. Workflow-Guided Exploration then addresses the sparse-reward problem by using demonstrations to induce high-level workflows that constrain exploration. DOM-Q-NET shifts attention to webpage structure by representing the DOM as a graph and learning grounded RL policies over DOM elements. Together, these papers show that web automation is not merely text processing. It requires environment perception, structural grounding, action selection, and sequential feedback.

The second stage begins with **WebGPT**. WebGPT shifts the field from RL web-interface control to LLM-based browsing. Instead of controlling a full browser visually, GPT-3 is fine-tuned to use a text-based browser with commands such as search, click, find, quote, scroll, and end. WebGPT is important because it shows that LLMs can use the web as an external information source and can collect references to support final answers. However, it remains a browser-assisted question-answering system, not a general web automation system. It does not handle visual layout, forms, dynamic pages, DOM-level action grounding, or structured extraction.

The third stage is represented by **WebShop**. WebShop introduces a scalable simulated e-commerce environment where agents follow natural-language shopping instructions, search products, inspect results, choose options, and make purchases. It abstracts away raw mouse and keyboard actions into semantic actions such as `search[query]` and `choose[item]`. WebShop is important because it connects language grounding, product search, exploration, comparison, backtracking, memory, and automatic reward computation. However, it remains domain-specific and simulated.

The fourth stage is real-world LLM web automation, represented strongly by **WebAgent** and **AutoWebGLM**. WebAgent argues that real websites are much harder than simulated ones because they have open-ended actions, long messy HTML, and no predefined action space. It uses HTML-T5 for planning and HTML summarization, and Flan-U-PaLM for grounded program synthesis. The final KDD 2024 AutoWebGLM paper takes a different but related direction: it builds a trained web-navigation agent on ChatGLM3-6B using HTML simplification, human-AI trajectory data, curriculum learning, reinforcement learning, and rejection sampling finetuning. These papers show that real-world web automation requires specialized observation processing, training data, task decomposition, and self-improvement.

The fifth stage is multimodal and live-web automation, represented by **SeeAct** and **WebVoyager**. SeeAct separates web-agent behavior into action generation and action grounding. It shows that GPT-4V can produce strong high-level action plans, but automatic grounding into exact HTML elements and operations remains the main bottleneck. WebVoyager then builds an end-to-end multimodal web agent that operates on real websites using screenshots, labeled interactive elements, and ReAct-style step-by-step reasoning. Together, these papers show that multimodal models bring web agents closer to human-like browsing, but grounding, navigation loops, hallucination, and evaluation remain major barriers.

The sixth stage broadens web agents into **GUI and computer-use agents**. Agent S, published as an ICLR 2025 poster, uses experience-augmented hierarchical planning, online web knowledge, narrative memory, episodic memory, and an Agent-Computer Interface to operate computers like a human. AutoGLM develops foundation agents for web and mobile GUIs and emphasizes the separation of planning and grounding through an intermediate interface. GUI-agent surveys then place web agents inside a larger automation landscape that includes web browsers, mobile apps, desktop software, cross-platform environments, and large action models. This matters because generalized web automation is part of a broader shift from chatbots to agents that control digital interfaces.

The final forward-looking stage is **WALT**, which argues that web agents should not always rely on brittle step-by-step UI interactions. Instead, they can reverse-engineer website-provided functionality into reusable tools, such as `search`, `filter`, `sort`, `create`, `edit`, `delete`, `comment`, and `upvote`. This suggests a next-generation direction for web automation: combining LLM planning with website-specific tool discovery and validated high-level action abstractions.

---

## 3. Refined S4 architecture/evolution stack

| Stage | Main papers | Main contribution | What it adds to S4 |
|---|---|---|---|
| Web as environment | World of Bits | Webpages as interactive environments with pixels, DOM, rewards, keyboard/mouse actions | Historical foundation |
| Workflow-guided RL | Workflow-Guided Exploration | Demonstrations induce workflows to constrain sparse-reward exploration | Demonstration-guided web RL |
| DOM-aware RL | DOM-Q-NET | Graph neural network over DOM trees and factorized Q-functions | Structured DOM grounding |
| LLM text browsing | WebGPT | GPT-3 uses a text browser, quotes evidence, and learns from human feedback | LLM-based web evidence gathering |
| Grounded simulated web interaction | WebShop | Scalable e-commerce benchmark with semantic actions and automatic rewards | Language-grounded web task benchmark |
| Real-world HTML-specialized agent | WebAgent | Long HTML summarization, task decomposition, Python program synthesis | Real-web HTML and open-ended actions |
| Multimodal grounding | SeeAct | Separates action generation from action grounding; identifies grounding bottleneck | Visual/HTML grounding diagnosis |
| Live multimodal web agent | WebVoyager | End-to-end LMM agent on real websites with screenshots and labeled elements | Live-web multimodal automation |
| Trained web-navigation agent | AutoWebGLM, KDD 2024 | HTML simplification, browsing traces, curriculum learning, RL, RFT, AutoWebBench | Open trained deployable web agent |
| Computer-use GUI agent | Agent S, ICLR 2025 Poster | Hierarchical planning, web knowledge, narrative/episodic memory, ACI | Cross-application GUI automation |
| Foundation GUI agent | AutoGLM, arXiv preprint | Intermediate interface, planning-grounding separation, online curriculum RL | Deployable GUI foundation agents |
| Tool-based web automation | WALT, ICLR 2026 Poster | Reverse-engineers website functionality into reusable tools | Future direction beyond primitive UI steps |
| Survey/taxonomy layer | TMLR 2025 GUI survey, ACL 2025 GUI survey, KDD 2025 WebAgents survey | Architecture, training, evaluation, trustworthiness, roadmap | Organizes S5 and S7/S8 |

---

## 4. Refined conceptual contribution of S4

The central contribution of S4 is to show that **web agents evolved through successive abstractions of the web interface**.

The interface abstraction changes over time:

```text
pixels + mouse/keyboard
→ DOM and HTML structure
→ text browser commands
→ semantic actions
→ programmatic browser actions
→ screenshots + labeled elements
→ simplified HTML + trained action models
→ intermediate GUI interfaces
→ learned website tools
```

This is the key S4 idea:

```text
Progress in web agents is progress in representing, grounding, and abstracting interaction with the web.
```

Early RL agents struggled because the web interface was too large and sparse at the pixel/mouse level. DOM-aware agents improved grounding by using webpage structure. LLM browsing improved language reasoning and evidence gathering. WebShop improved scalable grounded evaluation through semantic actions. WebAgent and AutoWebGLM improved real-web handling through HTML simplification, long-context processing, program synthesis, and training. SeeAct and WebVoyager improved multimodal perception but exposed the grounding bottleneck. Agent S and AutoGLM generalized web automation to computer-use and GUI foundation agents. WALT suggests that future agents may automate websites by discovering reliable high-level tools rather than repeatedly reasoning over primitive clicks.

---

## 5. Refined gap after S4 P1

After S4 P0, the gap was:

```text
Web-agent systems have moved from controlled environments to live multimodal interaction, but the core unsolved problem is reliable grounding and verification across diverse, dynamic, real-world websites.
```

After adding S4 P1, the gap becomes more precise:

```text
Web agents have progressed from RL interface control to trained multimodal and tool-augmented systems, but generalized web automation still lacks robust cross-site grounding, long-horizon reliability, safe execution, verified extraction, and maintainable action abstractions.
```

S4 now shows that web agents can:

```text
operate in browser-like environments
use pixels, DOM, HTML, screenshots, and accessibility trees
browse textually and cite evidence
act semantically in simulated websites
summarize long HTML
generate Python automation programs
use multimodal visual understanding
train smaller open web-navigation models
use memory and hierarchical planning
control broader GUIs
learn or expose website tools
```

But they still do not fully solve:

```text
precise element grounding across arbitrary websites
visual-DOM alignment under dynamic layouts
long-horizon task reliability
safe irreversible action handling
robust verification of extracted data
evaluation beyond fixed trajectories
privacy and permission control
resistance to popups, CAPTCHAs, ads, and authentication
state tracking across multi-page workflows
maintenance when websites change
cost and latency under real deployment
```

Therefore, the refined S4 gap is:

```text
The field has developed increasingly powerful web-agent architectures, but the remaining bottleneck is making their perception, planning, action abstraction, and verification reliable enough for generalized real-world web automation and data extraction.
```

---

## 6. Thesis connection

For the thesis topic, **“LLM-based agents for generalized web automation and data extraction,”** S4 supports seven major claims.

### Claim 1 — Web automation is a sequential decision-making problem

World of Bits, Workflow-Guided Exploration, and DOM-Q-NET show that web automation is not just scraping or text extraction. It is an interactive decision problem:

```text
observe state → choose action → execute → observe new state → continue
```

This supports the thesis framing of web automation as an agentic problem.

### Claim 2 — DOM and interface representation are foundational

DOM-Q-NET, WebAgent, AutoWebGLM, SeeAct, and WebVoyager all show that the way the page is represented strongly determines agent success. Web agents may use:

```text
DOM trees
HTML snippets
simplified HTML
accessibility trees
screenshots
OCR
labeled UI elements
multimodal observations
```

This directly motivates S5.2.

### Claim 3 — LLMs improve instruction following and reasoning but do not remove grounding problems

WebGPT, WebShop, WebAgent, SeeAct, and WebVoyager show that LLMs/LMMs improve browsing, planning, and language grounding. However, SeeAct and WebVoyager show that a correct high-level plan can still fail if the agent cannot ground it into the correct element or operation.

### Claim 4 — Training and experience are needed for robust web agents

Workflow-Guided Exploration, WebAgent, AutoWebGLM, Agent S, and AutoGLM show that prompting alone is insufficient. Web agents benefit from:

```text
demonstrations
workflow constraints
self-experience
curriculum learning
reinforcement learning
rejection sampling finetuning
episodic memory
narrative memory
online learning
```

This motivates S5.4.

### Claim 5 — Generalized web automation is part of broader GUI automation

Agent S, AutoGLM, and the GUI-agent surveys show that web agents are one branch of a larger GUI-agent ecosystem. Many web challenges also appear in mobile and desktop agents:

```text
visual grounding
action abstraction
long-horizon planning
memory
safety
privacy
latency
cross-platform generalization
```

This helps broaden the thesis without losing the web-specific focus.

### Claim 6 — Future web agents may need tool abstraction, not only UI actions

WALT shows that repeatedly clicking and typing is brittle. A more reliable direction is to discover reusable site-level tools:

```text
search(query)
filter(criteria)
sort(order)
create(item)
edit(item)
delete(item)
comment(text)
```

This connects S4 back to S3 tool-use architectures and forward to S6 extraction tools and S8 deployment.

### Claim 7 — Evaluation remains unresolved

World of Bits, WebShop, SeeAct, WebVoyager, AutoWebGLM, and the surveys all expose evaluation problems:

```text
offline vs online evaluation
fixed reference trajectories vs multiple valid solutions
simulated vs live websites
human evaluation vs automatic evaluation
success rate vs extraction correctness
safety and risk evaluation
cost/latency metrics
```

This motivates S5.1.

---

## 7. Refined thesis-ready synthesis paragraph

The evolution of web-agent systems shows a progression from early reinforcement-learning interfaces to modern LLM/LMM-powered agents operating on real websites and broader graphical user interfaces. World of Bits first framed the web as an open-domain interactive environment where agents observe pixels and DOM structures and act through keyboard and mouse events. Workflow-Guided Exploration and DOM-Q-NET then addressed two early bottlenecks of web RL: sparse-reward exploration and DOM-structured action grounding. WebGPT shifted the field toward LLM-based browsing by fine-tuning GPT-3 to search, navigate, quote evidence, and answer questions with human feedback. WebShop introduced scalable grounded web interaction through a simulated e-commerce environment with semantic actions and automatic rewards. More recent systems address the gap between simulated tasks and real websites. WebAgent combines planning, long HTML summarization, and program synthesis to act on real websites, while AutoWebGLM trains an open web-navigation model using simplified HTML, browsing traces, curriculum learning, reinforcement learning, and rejection sampling finetuning. Multimodal systems such as SeeAct and WebVoyager show that large multimodal models can reason over rendered webpages and perform live browser actions, but they also reveal that precise action grounding remains a major bottleneck. Broader GUI-agent systems such as Agent S and AutoGLM extend these ideas to desktop and mobile interfaces through hierarchical planning, memory, intermediate interfaces, and online curriculum learning. Finally, WALT suggests a future direction in which agents reverse-engineer website functionality into reusable tools, reducing reliance on brittle step-by-step UI actions. Together, these works show that web agents have become increasingly capable, but generalized web automation and data extraction still require robust DOM/visual grounding, long-horizon planning, safe execution, verified extraction, realistic evaluation, and deployment-aware action abstractions.

---

## 8. Refined limitations connected to the thesis

### 8.1 Low-level action limitation

Early systems such as World of Bits operate with low-level keyboard and mouse actions.

For generalized web automation, this matters because low-level control creates large action spaces and long trajectories. A data-extraction agent should not always reason at the level of pixels and mouse movements; it needs higher-level abstractions such as DOM elements, semantic actions, API calls, or tools.

### 8.2 Sparse reward and exploration limitation

Workflow-Guided Exploration shows that RL agents struggle when reward appears only after complete task success.

For web automation, this matters because many workflows have delayed success signals. A form may only fail at submission. A product search may only be wrong after comparison. An extraction may look correct but fail later verification.

### 8.3 DOM representation limitation

DOM-Q-NET shows that DOM structure helps, but simplified benchmark DOMs do not fully capture real websites.

For generalized automation, this matters because real DOMs are long, noisy, dynamic, and often disconnected from the visible human interface.

### 8.4 Text-browser limitation

WebGPT shows that LLMs can browse textually and cite evidence, but text browsing is not full browser automation.

For the thesis, this matters because data extraction and web automation often require forms, dropdowns, dynamic widgets, tables, visual layout, authentication, and structured outputs.

### 8.5 Simulated benchmark limitation

WebShop provides scalable grounded evaluation, but it remains a simulated e-commerce environment.

For generalized automation, this matters because real websites are multi-domain, dynamic, and often not reproducible.

### 8.6 Long HTML limitation

WebAgent and AutoWebGLM show that real HTML can exceed model context limits and contain large amounts of irrelevant content.

For web extraction, this matters directly because the agent must compress the page without removing relevant evidence.

### 8.7 Program synthesis limitation

WebAgent uses generated Python programs to act on websites.

For deployment, this matters because generated code can be powerful but risky. It must be sandboxed, constrained, inspected, or verified before execution.

### 8.8 Grounding limitation

SeeAct shows the gap between action generation and action grounding.

For generalized web automation, this is central. The agent may know what to do but fail to select the correct element, operation, or input value.

### 8.9 Live-web reliability limitation

WebVoyager shows that live multimodal agents fail through navigation loops, visual grounding issues, hallucination, and prompt misalignment.

For the thesis, these failures motivate a dedicated failure-mode analysis.

### 8.10 Training-data limitation

AutoWebGLM shows the importance of high-quality web-browsing traces.

For web agents, this matters because collecting representative trajectories across websites, languages, tasks, and failure cases is expensive.

### 8.11 Planning-grounding separation limitation

AutoGLM argues that planning and grounding require separate optimization.

For web agents, this matters because flexible reasoning and precise UI control are different abilities. A single prompt or model may not optimize both well.

### 8.12 Memory limitation

Agent S shows the value of narrative and episodic memory, but memory can also be stale, irrelevant, or wrong.

For web automation, memory must be evidence-grounded and verified, especially when websites change.

### 8.13 Tool-maintenance limitation

WALT shows that learned website tools can reduce brittle UI steps.

However, for deployment, tools must be discovered, validated, updated, and monitored as websites change. This creates a new maintenance problem.

### 8.14 Survey limitation

The GUI-agent and WebAgent surveys provide useful taxonomies, but they do not replace primary system papers.

For thesis writing, use surveys to structure the field and primary papers to support technical and empirical claims.

---

## 9. Updated cross-links to later sections

| Paper | Feeds |
|---|---|
| World of Bits | S5.1 benchmarks, S5.2 DOM/pixel grounding, S5.4 RL/behavioral cloning, S5.5 sparse-reward failures, S8 reproducibility |
| Workflow-Guided Exploration | S5.3 exploration/planning, S5.4 demonstrations/RL, S5.5 sparse rewards and overfitting |
| DOM-Q-NET | S5.2 DOM representation, S5.4 RL/multitask learning, S5.5 large variable action spaces |
| WebGPT | S5.4 human feedback, S6 web QA/extraction, S7 references/truthfulness, S8 live web access risk |
| WebShop | S5.1 scalable benchmark design, S5.3 search/exploration/planning, S5.4 imitation/RL, S8 sim-to-real |
| WebAgent | S5.2 long HTML summarization, S5.3 sub-instruction planning, S5.4 self-experience, S6 programmatic extraction, S8 real-web deployment |
| SeeAct | S5.1 offline vs online evaluation, S5.2 visual/HTML grounding, S5.3 action generation, S5.5 grounding failures, S7 safety |
| WebVoyager | S5.1 online evaluation, S5.2 multimodal perception, S5.3 end-to-end planning, S5.5 navigation/grounding/hallucination failures, S8 deployment |
| AutoWebGLM, KDD 2024 | S5.1 AutoWebBench, S5.2 HTML simplification, S5.3 task decomposition, S5.4 curriculum/RL/RFT, S5.5 loop/self-check failures, S8 browser extension |
| Agent S, ICLR 2025 Poster | S5.2 GUI grounding, S5.3 hierarchical planning, S5.4 memory/experience, S5.5 GUI failures, S8 cross-platform computer use |
| AutoGLM, arXiv preprint | S5.2 intermediate interface/grounding, S5.3 planning, S5.4 online curriculum RL, S5.5 error recovery, S8 deployable foundation agents |
| GUI-agent surveys, prefer TMLR 2025 + ACL Findings 2025 versions | S5.1 evaluation, S5.2 perception, S5.3 planning/action, S5.4 data/models, S5.5 limitations, S8 roadmap |
| WebAgents survey, KDD 2025 Tutorial & Survey Track | S5.1 evaluation, S5.2 perception, S5.3 planning/reasoning/execution, S5.4 training, S7 trustworthiness |
| WALT, ICLR 2026 Poster | S5.2 action/tool abstraction, S5.3 tool-based planning, S5.4 tool learning, S5.5 brittle UI-action failures, S6 extraction tools, S8 maintenance |

---

## 10. How S4 should be written in the thesis

A strong final thesis section for S4 can be organized into six subsections:

### S4.1 Pre-LLM web agents: web as an RL environment

Use:

```text
World of Bits
Workflow-Guided Exploration
DOM-Q-NET
```

Main argument:

```text
Before LLMs, web agents were treated as RL agents in browser environments, but sparse rewards, low-level actions, and DOM grounding made generalization difficult.
```

### S4.2 LLM browsing and evidence-grounded web QA

Use:

```text
WebGPT
```

Main argument:

```text
LLMs introduced stronger language reasoning and evidence-gathering ability, but text-based browsing remained narrower than full web automation.
```

### S4.3 Scalable grounded interaction benchmarks

Use:

```text
WebShop
```

Main argument:

```text
WebShop made web-agent evaluation scalable through realistic product data, semantic actions, and automatic rewards, but remained simulated and domain-specific.
```

### S4.4 Real-world LLM web agents

Use:

```text
WebAgent
AutoWebGLM, final KDD 2024 version
```

Main argument:

```text
Real websites require long HTML handling, observation simplification, task decomposition, program synthesis, trajectory data, and web-specific training.
```

### S4.5 Multimodal live-web agents

Use:

```text
SeeAct
WebVoyager
```

Main argument:

```text
LMMs improve visual web understanding, but reliable browser control depends on precise grounding and robust online evaluation.
```

### S4.6 From web agents to GUI/foundation/tool agents

Use:

```text
Agent S, ICLR 2025
AutoGLM, arXiv preprint
WALT, ICLR 2026
GUI-agent surveys, prefer TMLR 2025 and ACL Findings 2025 versions
WebAgents survey, KDD 2025 Tutorial & Survey Track
```

Main argument:

```text
Web automation is becoming part of a broader GUI-agent and computer-use-agent paradigm, where planning, grounding, memory, action abstraction, trustworthiness, and deployment become central.
```

---

## 11. Final refined S4 synthesis

S4 establishes the evolution of web-agent systems from early RL-based browser environments to modern LLM/LMM-powered agents and emerging tool-based automation. Early systems such as World of Bits, Workflow-Guided Exploration, and DOM-Q-NET framed the web as an interactive decision environment and showed that web automation is difficult because of sparse rewards, low-level actions, long trajectories, and DOM grounding. WebGPT shifted the field toward LLM-based browsing, where a model can search, navigate, quote evidence, and answer questions with human feedback. WebShop then introduced a scalable grounded web-interaction benchmark with semantic actions, realistic e-commerce data, and automatic rewards.

Later systems move closer to real-world web automation. WebAgent addresses real websites through planning, long HTML summarization, and program synthesis. AutoWebGLM shows that trained open LLMs can become competitive web-navigation agents through HTML simplification, browsing traces, curriculum learning, reinforcement learning, and rejection sampling finetuning. SeeAct and WebVoyager introduce the multimodal live-web paradigm: agents use screenshots, visual reasoning, and labeled interactive elements to act on real websites. These systems show strong progress but also reveal the grounding bottleneck, navigation loops, hallucinations, and online evaluation difficulty.

The most recent direction broadens web agents into GUI and computer-use agents. Agent S and AutoGLM show that web automation shares core challenges with desktop and mobile automation: hierarchical planning, memory, intermediate interfaces, action grounding, and online learning. Peer-reviewed and final survey references, including TMLR 2025 LLM-Brained GUI Agents, Findings of ACL 2025 GUI Agents, and the KDD 2025 WebAgents survey, provide the broader taxonomy of perception, planning, action, training, evaluation, and trustworthiness. WALT suggests an important future direction: instead of relying only on fragile primitive UI actions, web agents can discover and invoke high-level website tools.

Overall, S4 shows that web agents have moved from controlled web tasks toward real, multimodal, trained, and tool-augmented systems. However, generalized web automation and data extraction remain unsolved. The main remaining challenges are robust DOM and visual grounding, long-horizon planning, state tracking, verified extraction, safe execution, realistic evaluation, privacy, latency, and maintainable action abstractions. This refined S4 synthesis therefore motivates S5: a technical decomposition of the components that determine web-agent success or failure—benchmarks, perception and grounding, planning, training, and failure modes.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\Writing\S4_refined_synthesis_after_P1_updated_verified_with_central_gap.md

# S4 Refined Synthesis — Evolution of Web Agent Systems
## Updated after S4 P0 + S4 P1 papers

## Publication-status update for S4 P1 citations

The S4 narrative remains unchanged, but the final citation metadata should use the verified venue/status below:

| Paper | Final venue/status to use |
|---|---|
| Workflow-Guided Exploration | ICLR 2018 conference paper |
| DOM-Q-NET | ICLR 2019 conference paper |
| WebAgent | ICLR 2024 conference paper |
| Large Language Model Powered Agents in the Web | WWW 2024 Companion tutorial paper |
| AutoWebGLM Bootstrap and Reinforce | arXiv extended/preprint version; use KDD 2024 AutoWebGLM for final citation |
| Agent S | ICLR 2025 Poster |
| AutoGLM | arXiv preprint |
| Large Language Model-Brained GUI Agents preprint | arXiv preprint; use TMLR 2025 version for final citation |
| AutoWebGLM | KDD 2024 conference paper |
| GUI Agents with Foundation Models | arXiv preprint |
| A Survey on (M)LLM-Based GUI Agents | arXiv preprint |
| Large Language Model-Brained GUI Agents | TMLR 2025 |
| GUI Agents: A Survey | Findings of ACL 2025 |
| A Survey of WebAgents | KDD 2025 Tutorial & Survey Track |
| WALT | ICLR 2026 Poster |


## 1. What changed after adding S4 P1

The S4 P0 synthesis established the main historical arc:

```text
World of Bits
→ WebGPT
→ WebShop
→ SeeAct
→ WebVoyager
```

This gave the first web-agent progression:

```text
web as RL environment
→ text-based LLM browsing
→ scalable grounded web interaction
→ multimodal grounding
→ end-to-end live multimodal web automation
```

After adding the S4 P1 papers, the section becomes broader and more technically complete. The refined S4 narrative is now:

```text
World of Bits
→ Workflow-Guided Exploration
→ DOM-Q-NET
→ WebGPT
→ WebShop
→ WebAgent
→ SeeAct
→ WebVoyager
→ AutoWebGLM
→ Agent S / AutoGLM
→ WALT
→ WebAgent and GUI-agent surveys
```

Conceptually, this means S4 is no longer only a chronological history of web agents. It becomes a full evolution from:

```text
low-level RL browser control
→ DOM-aware RL
→ LLM browsing
→ simulated grounded web interaction
→ real-world HTML-specialized agents
→ multimodal live-web agents
→ trained/deployable web agents
→ general GUI/computer-use agents
→ tool-based web automation
```

The P1 papers add five important refinements:

1. **Pre-LLM web agents were already struggling with exploration and grounding.**  
   Workflow-Guided Exploration and DOM-Q-NET show that sparse rewards, low-level actions, and DOM representation were central problems before LLMs.

2. **Real-world websites require long HTML handling and open-ended action generation.**  
   WebAgent shows that simulated websites are too simple compared with real websites, where HTML is long, messy, dynamic, and task-irrelevant.

3. **Training and bootstrapping matter, not only prompting.**  
   The final KDD 2024 AutoWebGLM paper shows that smaller open models can become competitive web-navigation agents through HTML simplification, trajectory data, curriculum learning, RL, and rejection sampling finetuning.

4. **Web agents are part of a broader GUI-agent and computer-use-agent movement.**  
   Agent S (ICLR 2025), AutoGLM, and GUI-agent surveys show that web automation shares core problems with mobile and desktop automation: perception, grounding, planning, memory, action execution, and safety.

5. **The next direction is action abstraction and tool learning.**  
   WALT (ICLR 2026) shifts web automation away from fragile primitive UI actions toward discovered website-level tools such as `search`, `filter`, `sort`, `create`, `edit`, and `delete`.

---

## 2. Refined S4 narrative

Section S4 explains how web-agent systems evolved from early reinforcement-learning environments to modern LLM/LMM-powered agents capable of interacting with real websites and broader graphical user interfaces.

The earliest stage is represented by **World of Bits**, **Workflow-Guided Exploration**, and **DOM-Q-NET**. These papers treat web automation as a sequential decision-making problem. The web page is an environment; the agent observes pixels, DOM structures, or HTML trees; and it acts through mouse, keyboard, click, or type actions. This pre-LLM stage is important because it identifies the core difficulties of web automation before modern LLMs: sparse rewards, large action spaces, long trajectories, demonstration dependence, weak exploration, and DOM grounding.

World of Bits establishes the web as an open-domain interactive environment. Workflow-Guided Exploration then addresses the sparse-reward problem by using demonstrations to induce high-level workflows that constrain exploration. DOM-Q-NET shifts attention to webpage structure by representing the DOM as a graph and learning grounded RL policies over DOM elements. Together, these papers show that web automation is not merely text processing. It requires environment perception, structural grounding, action selection, and sequential feedback.

The second stage begins with **WebGPT**. WebGPT shifts the field from RL web-interface control to LLM-based browsing. Instead of controlling a full browser visually, GPT-3 is fine-tuned to use a text-based browser with commands such as search, click, find, quote, scroll, and end. WebGPT is important because it shows that LLMs can use the web as an external information source and can collect references to support final answers. However, it remains a browser-assisted question-answering system, not a general web automation system. It does not handle visual layout, forms, dynamic pages, DOM-level action grounding, or structured extraction.

The third stage is represented by **WebShop**. WebShop introduces a scalable simulated e-commerce environment where agents follow natural-language shopping instructions, search products, inspect results, choose options, and make purchases. It abstracts away raw mouse and keyboard actions into semantic actions such as `search[query]` and `choose[item]`. WebShop is important because it connects language grounding, product search, exploration, comparison, backtracking, memory, and automatic reward computation. However, it remains domain-specific and simulated.

The fourth stage is real-world LLM web automation, represented strongly by **WebAgent** and **AutoWebGLM**. WebAgent argues that real websites are much harder than simulated ones because they have open-ended actions, long messy HTML, and no predefined action space. It uses HTML-T5 for planning and HTML summarization, and Flan-U-PaLM for grounded program synthesis. The final KDD 2024 AutoWebGLM paper takes a different but related direction: it builds a trained web-navigation agent on ChatGLM3-6B using HTML simplification, human-AI trajectory data, curriculum learning, reinforcement learning, and rejection sampling finetuning. These papers show that real-world web automation requires specialized observation processing, training data, task decomposition, and self-improvement.

The fifth stage is multimodal and live-web automation, represented by **SeeAct** and **WebVoyager**. SeeAct separates web-agent behavior into action generation and action grounding. It shows that GPT-4V can produce strong high-level action plans, but automatic grounding into exact HTML elements and operations remains the main bottleneck. WebVoyager then builds an end-to-end multimodal web agent that operates on real websites using screenshots, labeled interactive elements, and ReAct-style step-by-step reasoning. Together, these papers show that multimodal models bring web agents closer to human-like browsing, but grounding, navigation loops, hallucination, and evaluation remain major barriers.

The sixth stage broadens web agents into **GUI and computer-use agents**. Agent S, published as an ICLR 2025 poster, uses experience-augmented hierarchical planning, online web knowledge, narrative memory, episodic memory, and an Agent-Computer Interface to operate computers like a human. AutoGLM develops foundation agents for web and mobile GUIs and emphasizes the separation of planning and grounding through an intermediate interface. GUI-agent surveys then place web agents inside a larger automation landscape that includes web browsers, mobile apps, desktop software, cross-platform environments, and large action models. This matters because generalized web automation is part of a broader shift from chatbots to agents that control digital interfaces.

The final forward-looking stage is **WALT**, which argues that web agents should not always rely on brittle step-by-step UI interactions. Instead, they can reverse-engineer website-provided functionality into reusable tools, such as `search`, `filter`, `sort`, `create`, `edit`, `delete`, `comment`, and `upvote`. This suggests a next-generation direction for web automation: combining LLM planning with website-specific tool discovery and validated high-level action abstractions.

---

## 3. Refined S4 architecture/evolution stack

| Stage | Main papers | Main contribution | What it adds to S4 |
|---|---|---|---|
| Web as environment | World of Bits | Webpages as interactive environments with pixels, DOM, rewards, keyboard/mouse actions | Historical foundation |
| Workflow-guided RL | Workflow-Guided Exploration | Demonstrations induce workflows to constrain sparse-reward exploration | Demonstration-guided web RL |
| DOM-aware RL | DOM-Q-NET | Graph neural network over DOM trees and factorized Q-functions | Structured DOM grounding |
| LLM text browsing | WebGPT | GPT-3 uses a text browser, quotes evidence, and learns from human feedback | LLM-based web evidence gathering |
| Grounded simulated web interaction | WebShop | Scalable e-commerce benchmark with semantic actions and automatic rewards | Language-grounded web task benchmark |
| Real-world HTML-specialized agent | WebAgent | Long HTML summarization, task decomposition, Python program synthesis | Real-web HTML and open-ended actions |
| Multimodal grounding | SeeAct | Separates action generation from action grounding; identifies grounding bottleneck | Visual/HTML grounding diagnosis |
| Live multimodal web agent | WebVoyager | End-to-end LMM agent on real websites with screenshots and labeled elements | Live-web multimodal automation |
| Trained web-navigation agent | AutoWebGLM, KDD 2024 | HTML simplification, browsing traces, curriculum learning, RL, RFT, AutoWebBench | Open trained deployable web agent |
| Computer-use GUI agent | Agent S, ICLR 2025 Poster | Hierarchical planning, web knowledge, narrative/episodic memory, ACI | Cross-application GUI automation |
| Foundation GUI agent | AutoGLM, arXiv preprint | Intermediate interface, planning-grounding separation, online curriculum RL | Deployable GUI foundation agents |
| Tool-based web automation | WALT, ICLR 2026 Poster | Reverse-engineers website functionality into reusable tools | Future direction beyond primitive UI steps |
| Survey/taxonomy layer | TMLR 2025 GUI survey, ACL 2025 GUI survey, KDD 2025 WebAgents survey | Architecture, training, evaluation, trustworthiness, roadmap | Organizes S5 and S7/S8 |

---

## 4. Refined conceptual contribution of S4

The central contribution of S4 is to show that **web agents evolved through successive abstractions of the web interface**.

The interface abstraction changes over time:

```text
pixels + mouse/keyboard
→ DOM and HTML structure
→ text browser commands
→ semantic actions
→ programmatic browser actions
→ screenshots + labeled elements
→ simplified HTML + trained action models
→ intermediate GUI interfaces
→ learned website tools
```

This is the key S4 idea:

```text
Progress in web agents is progress in representing, grounding, and abstracting interaction with the web.
```

Early RL agents struggled because the web interface was too large and sparse at the pixel/mouse level. DOM-aware agents improved grounding by using webpage structure. LLM browsing improved language reasoning and evidence gathering. WebShop improved scalable grounded evaluation through semantic actions. WebAgent and AutoWebGLM improved real-web handling through HTML simplification, long-context processing, program synthesis, and training. SeeAct and WebVoyager improved multimodal perception but exposed the grounding bottleneck. Agent S and AutoGLM generalized web automation to computer-use and GUI foundation agents. WALT suggests that future agents may automate websites by discovering reliable high-level tools rather than repeatedly reasoning over primitive clicks.

---

## 5. Refined gap after S4 P1

After S4 P0, the gap was:

```text
Web-agent systems have moved from controlled environments to live multimodal interaction, but the core unsolved problem is reliable grounding and verification across diverse, dynamic, real-world websites.
```

After adding S4 P1, the gap becomes more precise:

```text
Web agents have progressed from RL interface control to trained multimodal and tool-augmented systems, but generalized web automation still lacks robust cross-site grounding, long-horizon reliability, safe execution, verified extraction, and maintainable action abstractions.
```

S4 now shows that web agents can:

```text
operate in browser-like environments
use pixels, DOM, HTML, screenshots, and accessibility trees
browse textually and cite evidence
act semantically in simulated websites
summarize long HTML
generate Python automation programs
use multimodal visual understanding
train smaller open web-navigation models
use memory and hierarchical planning
control broader GUIs
learn or expose website tools
```

But they still do not fully solve:

```text
precise element grounding across arbitrary websites
visual-DOM alignment under dynamic layouts
long-horizon task reliability
safe irreversible action handling
robust verification of extracted data
evaluation beyond fixed trajectories
privacy and permission control
resistance to popups, CAPTCHAs, ads, and authentication
state tracking across multi-page workflows
maintenance when websites change
cost and latency under real deployment
```

Therefore, the refined S4 gap is:

```text
The field has developed increasingly powerful web-agent architectures, but the remaining bottleneck is making their perception, planning, action abstraction, and verification reliable enough for generalized real-world web automation and data extraction.
```

---

## 6. Thesis connection

For the thesis topic, **“LLM-based agents for generalized web automation and data extraction,”** S4 supports seven major claims.

### Claim 1 — Web automation is a sequential decision-making problem

World of Bits, Workflow-Guided Exploration, and DOM-Q-NET show that web automation is not just scraping or text extraction. It is an interactive decision problem:

```text
observe state → choose action → execute → observe new state → continue
```

This supports the thesis framing of web automation as an agentic problem.

### Claim 2 — DOM and interface representation are foundational

DOM-Q-NET, WebAgent, AutoWebGLM, SeeAct, and WebVoyager all show that the way the page is represented strongly determines agent success. Web agents may use:

```text
DOM trees
HTML snippets
simplified HTML
accessibility trees
screenshots
OCR
labeled UI elements
multimodal observations
```

This directly motivates S5.2.

### Claim 3 — LLMs improve instruction following and reasoning but do not remove grounding problems

WebGPT, WebShop, WebAgent, SeeAct, and WebVoyager show that LLMs/LMMs improve browsing, planning, and language grounding. However, SeeAct and WebVoyager show that a correct high-level plan can still fail if the agent cannot ground it into the correct element or operation.

### Claim 4 — Training and experience are needed for robust web agents

Workflow-Guided Exploration, WebAgent, AutoWebGLM, Agent S, and AutoGLM show that prompting alone is insufficient. Web agents benefit from:

```text
demonstrations
workflow constraints
self-experience
curriculum learning
reinforcement learning
rejection sampling finetuning
episodic memory
narrative memory
online learning
```

This motivates S5.4.

### Claim 5 — Generalized web automation is part of broader GUI automation

Agent S, AutoGLM, and the GUI-agent surveys show that web agents are one branch of a larger GUI-agent ecosystem. Many web challenges also appear in mobile and desktop agents:

```text
visual grounding
action abstraction
long-horizon planning
memory
safety
privacy
latency
cross-platform generalization
```

This helps broaden the thesis without losing the web-specific focus.

### Claim 6 — Future web agents may need tool abstraction, not only UI actions

WALT shows that repeatedly clicking and typing is brittle. A more reliable direction is to discover reusable site-level tools:

```text
search(query)
filter(criteria)
sort(order)
create(item)
edit(item)
delete(item)
comment(text)
```

This connects S4 back to S3 tool-use architectures and forward to S6 extraction tools and S8 deployment.

### Claim 7 — Evaluation remains unresolved

World of Bits, WebShop, SeeAct, WebVoyager, AutoWebGLM, and the surveys all expose evaluation problems:

```text
offline vs online evaluation
fixed reference trajectories vs multiple valid solutions
simulated vs live websites
human evaluation vs automatic evaluation
success rate vs extraction correctness
safety and risk evaluation
cost/latency metrics
```

This motivates S5.1.

---

## 7. Refined thesis-ready synthesis paragraph

The evolution of web-agent systems shows a progression from early reinforcement-learning interfaces to modern LLM/LMM-powered agents operating on real websites and broader graphical user interfaces. World of Bits first framed the web as an open-domain interactive environment where agents observe pixels and DOM structures and act through keyboard and mouse events. Workflow-Guided Exploration and DOM-Q-NET then addressed two early bottlenecks of web RL: sparse-reward exploration and DOM-structured action grounding. WebGPT shifted the field toward LLM-based browsing by fine-tuning GPT-3 to search, navigate, quote evidence, and answer questions with human feedback. WebShop introduced scalable grounded web interaction through a simulated e-commerce environment with semantic actions and automatic rewards. More recent systems address the gap between simulated tasks and real websites. WebAgent combines planning, long HTML summarization, and program synthesis to act on real websites, while AutoWebGLM trains an open web-navigation model using simplified HTML, browsing traces, curriculum learning, reinforcement learning, and rejection sampling finetuning. Multimodal systems such as SeeAct and WebVoyager show that large multimodal models can reason over rendered webpages and perform live browser actions, but they also reveal that precise action grounding remains a major bottleneck. Broader GUI-agent systems such as Agent S and AutoGLM extend these ideas to desktop and mobile interfaces through hierarchical planning, memory, intermediate interfaces, and online curriculum learning. Finally, WALT suggests a future direction in which agents reverse-engineer website functionality into reusable tools, reducing reliance on brittle step-by-step UI actions. Together, these works show that web agents have become increasingly capable, but generalized web automation and data extraction still require robust DOM/visual grounding, long-horizon planning, safe execution, verified extraction, realistic evaluation, and deployment-aware action abstractions.

---

## 8. Refined limitations connected to the thesis

### 8.1 Low-level action limitation

Early systems such as World of Bits operate with low-level keyboard and mouse actions.

For generalized web automation, this matters because low-level control creates large action spaces and long trajectories. A data-extraction agent should not always reason at the level of pixels and mouse movements; it needs higher-level abstractions such as DOM elements, semantic actions, API calls, or tools.

### 8.2 Sparse reward and exploration limitation

Workflow-Guided Exploration shows that RL agents struggle when reward appears only after complete task success.

For web automation, this matters because many workflows have delayed success signals. A form may only fail at submission. A product search may only be wrong after comparison. An extraction may look correct but fail later verification.

### 8.3 DOM representation limitation

DOM-Q-NET shows that DOM structure helps, but simplified benchmark DOMs do not fully capture real websites.

For generalized automation, this matters because real DOMs are long, noisy, dynamic, and often disconnected from the visible human interface.

### 8.4 Text-browser limitation

WebGPT shows that LLMs can browse textually and cite evidence, but text browsing is not full browser automation.

For the thesis, this matters because data extraction and web automation often require forms, dropdowns, dynamic widgets, tables, visual layout, authentication, and structured outputs.

### 8.5 Simulated benchmark limitation

WebShop provides scalable grounded evaluation, but it remains a simulated e-commerce environment.

For generalized automation, this matters because real websites are multi-domain, dynamic, and often not reproducible.

### 8.6 Long HTML limitation

WebAgent and AutoWebGLM show that real HTML can exceed model context limits and contain large amounts of irrelevant content.

For web extraction, this matters directly because the agent must compress the page without removing relevant evidence.

### 8.7 Program synthesis limitation

WebAgent uses generated Python programs to act on websites.

For deployment, this matters because generated code can be powerful but risky. It must be sandboxed, constrained, inspected, or verified before execution.

### 8.8 Grounding limitation

SeeAct shows the gap between action generation and action grounding.

For generalized web automation, this is central. The agent may know what to do but fail to select the correct element, operation, or input value.

### 8.9 Live-web reliability limitation

WebVoyager shows that live multimodal agents fail through navigation loops, visual grounding issues, hallucination, and prompt misalignment.

For the thesis, these failures motivate a dedicated failure-mode analysis.

### 8.10 Training-data limitation

AutoWebGLM shows the importance of high-quality web-browsing traces.

For web agents, this matters because collecting representative trajectories across websites, languages, tasks, and failure cases is expensive.

### 8.11 Planning-grounding separation limitation

AutoGLM argues that planning and grounding require separate optimization.

For web agents, this matters because flexible reasoning and precise UI control are different abilities. A single prompt or model may not optimize both well.

### 8.12 Memory limitation

Agent S shows the value of narrative and episodic memory, but memory can also be stale, irrelevant, or wrong.

For web automation, memory must be evidence-grounded and verified, especially when websites change.

### 8.13 Tool-maintenance limitation

WALT shows that learned website tools can reduce brittle UI steps.

However, for deployment, tools must be discovered, validated, updated, and monitored as websites change. This creates a new maintenance problem.

### 8.14 Survey limitation

The GUI-agent and WebAgent surveys provide useful taxonomies, but they do not replace primary system papers.

For thesis writing, use surveys to structure the field and primary papers to support technical and empirical claims.

---

## 9. Updated cross-links to later sections

| Paper | Feeds |
|---|---|
| World of Bits | S5.1 benchmarks, S5.2 DOM/pixel grounding, S5.4 RL/behavioral cloning, S5.5 sparse-reward failures, S8 reproducibility |
| Workflow-Guided Exploration | S5.3 exploration/planning, S5.4 demonstrations/RL, S5.5 sparse rewards and overfitting |
| DOM-Q-NET | S5.2 DOM representation, S5.4 RL/multitask learning, S5.5 large variable action spaces |
| WebGPT | S5.4 human feedback, S6 web QA/extraction, S7 references/truthfulness, S8 live web access risk |
| WebShop | S5.1 scalable benchmark design, S5.3 search/exploration/planning, S5.4 imitation/RL, S8 sim-to-real |
| WebAgent | S5.2 long HTML summarization, S5.3 sub-instruction planning, S5.4 self-experience, S6 programmatic extraction, S8 real-web deployment |
| SeeAct | S5.1 offline vs online evaluation, S5.2 visual/HTML grounding, S5.3 action generation, S5.5 grounding failures, S7 safety |
| WebVoyager | S5.1 online evaluation, S5.2 multimodal perception, S5.3 end-to-end planning, S5.5 navigation/grounding/hallucination failures, S8 deployment |
| AutoWebGLM, KDD 2024 | S5.1 AutoWebBench, S5.2 HTML simplification, S5.3 task decomposition, S5.4 curriculum/RL/RFT, S5.5 loop/self-check failures, S8 browser extension |
| Agent S, ICLR 2025 Poster | S5.2 GUI grounding, S5.3 hierarchical planning, S5.4 memory/experience, S5.5 GUI failures, S8 cross-platform computer use |
| AutoGLM, arXiv preprint | S5.2 intermediate interface/grounding, S5.3 planning, S5.4 online curriculum RL, S5.5 error recovery, S8 deployable foundation agents |
| GUI-agent surveys, prefer TMLR 2025 + ACL Findings 2025 versions | S5.1 evaluation, S5.2 perception, S5.3 planning/action, S5.4 data/models, S5.5 limitations, S8 roadmap |
| WebAgents survey, KDD 2025 Tutorial & Survey Track | S5.1 evaluation, S5.2 perception, S5.3 planning/reasoning/execution, S5.4 training, S7 trustworthiness |
| WALT, ICLR 2026 Poster | S5.2 action/tool abstraction, S5.3 tool-based planning, S5.4 tool learning, S5.5 brittle UI-action failures, S6 extraction tools, S8 maintenance |

---

## 10. How S4 should be written in the thesis

A strong final thesis section for S4 can be organized into six subsections:

### S4.1 Pre-LLM web agents: web as an RL environment

Use:

```text
World of Bits
Workflow-Guided Exploration
DOM-Q-NET
```

Main argument:

```text
Before LLMs, web agents were treated as RL agents in browser environments, but sparse rewards, low-level actions, and DOM grounding made generalization difficult.
```

### S4.2 LLM browsing and evidence-grounded web QA

Use:

```text
WebGPT
```

Main argument:

```text
LLMs introduced stronger language reasoning and evidence-gathering ability, but text-based browsing remained narrower than full web automation.
```

### S4.3 Scalable grounded interaction benchmarks

Use:

```text
WebShop
```

Main argument:

```text
WebShop made web-agent evaluation scalable through realistic product data, semantic actions, and automatic rewards, but remained simulated and domain-specific.
```

### S4.4 Real-world LLM web agents

Use:

```text
WebAgent
AutoWebGLM, final KDD 2024 version
```

Main argument:

```text
Real websites require long HTML handling, observation simplification, task decomposition, program synthesis, trajectory data, and web-specific training.
```

### S4.5 Multimodal live-web agents

Use:

```text
SeeAct
WebVoyager
```

Main argument:

```text
LMMs improve visual web understanding, but reliable browser control depends on precise grounding and robust online evaluation.
```

### S4.6 From web agents to GUI/foundation/tool agents

Use:

```text
Agent S, ICLR 2025
AutoGLM, arXiv preprint
WALT, ICLR 2026
GUI-agent surveys, prefer TMLR 2025 and ACL Findings 2025 versions
WebAgents survey, KDD 2025 Tutorial & Survey Track
```

Main argument:

```text
Web automation is becoming part of a broader GUI-agent and computer-use-agent paradigm, where planning, grounding, memory, action abstraction, trustworthiness, and deployment become central.
```

---



## The central S4 gap

Despite rapid progress from **World of Bits** to **WebVoyager**, no system in S4 solves all of the following together:

```text
reliable DOM grounding
+ live-web generalization
+ structured extraction
+ safe deployment
+ cost efficiency
```

This is the central S4 gap. It explains why the literature must move from a chronological evolution of web-agent systems to a technical decomposition of the remaining bottlenecks. Therefore, S5 should analyze the core components that determine whether LLM-based web agents succeed or fail: benchmarks and evaluation, perception and grounding, planning and decision-making, training and generalization, and failure modes.

---

## 11. Final refined S4 synthesis

S4 establishes the evolution of web-agent systems from early RL-based browser environments to modern LLM/LMM-powered agents and emerging tool-based automation. Early systems such as World of Bits, Workflow-Guided Exploration, and DOM-Q-NET framed the web as an interactive decision environment and showed that web automation is difficult because of sparse rewards, low-level actions, long trajectories, and DOM grounding. WebGPT shifted the field toward LLM-based browsing, where a model can search, navigate, quote evidence, and answer questions with human feedback. WebShop then introduced a scalable grounded web-interaction benchmark with semantic actions, realistic e-commerce data, and automatic rewards.

Later systems move closer to real-world web automation. WebAgent addresses real websites through planning, long HTML summarization, and program synthesis. AutoWebGLM shows that trained open LLMs can become competitive web-navigation agents through HTML simplification, browsing traces, curriculum learning, reinforcement learning, and rejection sampling finetuning. SeeAct and WebVoyager introduce the multimodal live-web paradigm: agents use screenshots, visual reasoning, and labeled interactive elements to act on real websites. These systems show strong progress but also reveal the grounding bottleneck, navigation loops, hallucinations, and online evaluation difficulty.

The most recent direction broadens web agents into GUI and computer-use agents. Agent S and AutoGLM show that web automation shares core challenges with desktop and mobile automation: hierarchical planning, memory, intermediate interfaces, action grounding, and online learning. Peer-reviewed and final survey references, including TMLR 2025 LLM-Brained GUI Agents, Findings of ACL 2025 GUI Agents, and the KDD 2025 WebAgents survey, provide the broader taxonomy of perception, planning, action, training, evaluation, and trustworthiness. WALT suggests an important future direction: instead of relying only on fragile primitive UI actions, web agents can discover and invoke high-level website tools.

Overall, S4 shows that web agents have moved from controlled web tasks toward real, multimodal, trained, and tool-augmented systems. However, generalized web automation and data extraction remain unsolved. The main remaining challenges are robust DOM and visual grounding, long-horizon planning, state tracking, verified extraction, safe execution, realistic evaluation, privacy, latency, and maintainable action abstractions. This refined S4 synthesis therefore motivates S5: a technical decomposition of the components that determine web-agent success or failure—benchmarks, perception and grounding, planning, training, and failure modes.


---

## Synthesis / Writing Notes (4 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\writing\S4_mini_synthesis_from_P0.md

# S4 Mini-Synthesis — Evolution of Web Agent Systems  
## Based on S4 P0 papers: World of Bits, WebGPT, WebShop, SeeAct, WebVoyager

## 1. Narrative

Section S4 explains how web-agent systems evolved from early reinforcement-learning environments to modern multimodal LLM agents operating on live websites.

The S4 P0 papers show a clear progression:

```text
World of Bits
→ WebGPT
→ WebShop
→ SeeAct
→ WebVoyager
```

Conceptually, this progression can be summarized as:

```text
web as RL environment
→ text-based LLM browsing
→ scalable grounded web interaction
→ multimodal web-agent grounding
→ end-to-end live multimodal web automation
```

This section is important because it moves the literature review from **general LLM-agent architectures** in S3 to **web-specific agent systems**. S3 explained how LLMs become agents through reasoning, acting, memory, tools, and planning. S4 shows how those agentic ideas are instantiated in the web environment, where agents must deal with webpages, DOM structures, screenshots, browser actions, search, navigation, dynamic content, and task success evaluation.

The central message of S4 is:

```text
Web agents evolved from low-level UI-control environments to LLM/LMM-powered systems, but reliable generalized web automation still depends on grounding, planning, verification, safety, and deployment realism.
```

---

## 2. Paper-level synthesis

### 2.1 World of Bits — The web as an agent environment

World of Bits is the historical starting point of S4. It frames the web as an open-domain interactive environment for agents.

The agent observes:

```text
screen pixels
DOM elements with coordinates
reward
```

and acts through:

```text
keyboard events
mouse events
```

This was a major shift because the web was no longer treated only as a source of text or documents. Instead, the web became an environment in which agents must perceive, act, and receive feedback.

World of Bits introduced three levels of web tasks:

```text
MiniWoB → synthetic controlled tasks
FormWoB → cached real flight-booking websites
QAWoB → crowdsourced question-answering tasks on real websites
```

For the thesis, World of Bits is important because it identifies the core technical structure of web automation:

```text
instruction → page observation → grounding → UI action → reward/feedback
```

However, World of Bits also shows why pre-LLM web agents struggled. Behavioral cloning and reinforcement learning achieved limited success, especially on keyboard-heavy and compound tasks. This reveals several early bottlenecks:

```text
sparse rewards
long horizons
low-level actions
difficult exploration
weak language understanding
weak DOM/pixel grounding
```

Therefore, World of Bits provides the pre-LLM foundation and motivates the transition toward language-model-based web agents.

---

### 2.2 WebGPT — LLM browsing with references and human feedback

WebGPT marks the transition from pre-LLM web agents to LLM-based browsing agents.

Unlike World of Bits, WebGPT does not control a full visual browser with mouse and keyboard. Instead, it creates a **text-based browsing environment** where GPT-3 can issue commands such as:

```text
Search
Click
Find in page
Quote
Scroll
Back
End
```

The system is trained using:

```text
human demonstrations → behavior cloning
human comparisons → reward model
reward model → rejection sampling / RL
```

The key innovation is that the model must collect **references** while browsing. These references support the final answer and make human evaluation of factual accuracy easier.

For the thesis, WebGPT is important because it shows that LLMs can use the web as an external information source. This connects directly to web information extraction, source-grounded question answering, and verification.

However, WebGPT is still narrow. It is mainly a long-form question-answering system. It does not solve general web automation because it does not handle:

```text
visual layout
forms
buttons
calendars
dropdowns
dynamic websites
structured extraction
DOM-level action grounding
general browser workflows
```

Thus, WebGPT is a turning point, but not a complete generalized web agent.

---

### 2.3 WebShop — Scalable grounded language interaction

WebShop introduces a scalable simulated e-commerce environment for grounded language agents.

The task is:

```text
read a shopping instruction
→ search for products
→ inspect results
→ open product pages
→ choose options
→ buy the matching product
```

WebShop is important because it combines:

```text
real-world product data
natural-language instructions
sequential decision-making
semantic web actions
automatic reward
human demonstrations
sim-to-real transfer
```

Compared with World of Bits, WebShop abstracts away low-level mouse and keyboard actions. Instead, it uses a semantic action space:

```text
search[query]
choose[button/product/option]
```

This makes the environment more compatible with language agents.

For the thesis, WebShop is crucial because it shows that web automation is not only about navigation. It requires language grounding, query reformulation, option selection, comparison, exploration, backtracking, and memory. These are also central to web data extraction, where an agent must find relevant pages, compare candidate information, and verify extracted values.

However, WebShop remains limited because it is simulated and e-commerce-specific. It does not fully represent arbitrary live websites, authentication, CAPTCHAs, dynamic JavaScript, pop-ups, real-time content, or unrestricted UI interaction.

Therefore, WebShop is a cornerstone benchmark for grounded web interaction, but not a complete generalization benchmark.

---

### 2.4 SeeAct — GPT-4V can act on the web if grounded

SeeAct introduces a modern multimodal view of web agents.

The paper’s core argument is:

```text
GPT-4V has strong potential as a generalist web agent,
but only if its plans can be grounded into correct browser actions.
```

SeeAct separates web-agent behavior into two stages:

```text
Action generation:
the model decides what should be done next in natural language

Action grounding:
the system converts that natural-language action into an executable browser event
```

This distinction is very important for the thesis because it shows that planning and grounding are different problems. A model may correctly say:

```text
Click the “Find Your Truck” button.
```

but still fail if it cannot identify the exact HTML element or visual region corresponding to that button.

SeeAct evaluates grounding strategies such as:

```text
element attributes
textual choices
image annotation
oracle grounding
```

The paper shows that GPT-4V performs strongly with oracle grounding, but automatic grounding remains far below oracle performance. This identifies **element grounding** as one of the central bottlenecks for web agents.

For the thesis, SeeAct feeds directly into S5.2 because it shows that multimodal understanding alone is insufficient. Web agents need precise alignment between:

```text
visual screenshot
HTML/DOM element
operation type
input value
browser event
```

---

### 2.5 WebVoyager — End-to-end live multimodal web automation

WebVoyager represents the modern end-to-end multimodal web-agent paradigm.

Unlike WebShop, it does not operate only in a simulated e-commerce environment. Unlike WebGPT, it is not limited to text browsing. WebVoyager uses a live browser and real websites.

Its loop is:

```text
user task
→ screenshot + interactive element text
→ LMM thought
→ browser action
→ new observation
→ repeat
→ final answer
```

The agent uses screenshots as the primary input and overlays numerical labels on interactive elements. This helps the model choose actions such as:

```text
Click [10]
Type [17]: search query
Scroll
Back
Answer
```

WebVoyager also introduces a benchmark of 643 tasks across 15 popular websites and proposes GPT-4V-based automatic trajectory evaluation. This is important because online web-agent evaluation is difficult and expensive.

For the thesis, WebVoyager is a major S4 paper because it shows the current direction of web-agent systems:

```text
live websites
multimodal input
marked interactive elements
ReAct-style reasoning
end-to-end task completion
automatic evaluation
```

However, it also shows that modern web agents still fail in predictable ways:

```text
navigation stuck
visual grounding errors
hallucination
prompt misalignment
dense text handling
long trajectories
```

These failure categories directly motivate S5.5.

---

## 3. Main conceptual contribution of S4

The main contribution of S4 is to show that web agents are not just general agents applied to a new domain. The web creates specific technical requirements.

A web agent must solve:

```text
webpage perception
DOM and visual grounding
browser action execution
search and navigation
long-horizon planning
state tracking
query reformulation
structured extraction
verification
safe interaction with live websites
```

The S4 P0 papers show the evolution of these requirements:

| Stage | Paper | Main contribution | Remaining gap |
|---|---|---|---|
| Web as environment | World of Bits | Web interaction as RL with pixels, DOM, mouse/keyboard | Low-level actions, sparse rewards, weak language reasoning |
| LLM browsing | WebGPT | GPT-3 uses text browser and references with human feedback | Text-only QA, not full web automation |
| Scalable grounded interaction | WebShop | Large-scale e-commerce benchmark with semantic actions and rewards | Simulated, domain-specific, limited action space |
| Multimodal grounding | SeeAct | GPT-4V can plan well if grounding is solved | Element grounding remains bottleneck |
| Live multimodal automation | WebVoyager | End-to-end LMM agent on real websites | Still fails through grounding, loops, hallucination, evaluation limits |

---

## 4. S4 narrative arc

The S4 narrative can be written as five steps:

```text
Step 1 — World of Bits:
The web becomes an interactive environment for agents.

Step 2 — WebGPT:
LLMs begin to browse the web through text commands and evidence collection.

Step 3 — WebShop:
Web-agent evaluation becomes scalable through realistic but simulated grounded interaction.

Step 4 — SeeAct:
Large multimodal models show strong web-agent potential, but grounding becomes the central bottleneck.

Step 5 — WebVoyager:
End-to-end multimodal agents operate on live websites, exposing real deployment and evaluation challenges.
```

This creates the following conceptual arc:

```text
environment
→ browsing
→ grounded interaction
→ multimodal grounding
→ live end-to-end automation
```

---

## 5. Refined gap after S4 P0

After S3, the gap was:

```text
General LLM-agent architectures provide the control logic of agency, but web automation requires grounding that control logic in real browser environments with reliable perception, action, verification, and safety.
```

After S4 P0, the gap becomes more web-specific:

```text
Modern web agents can browse, search, plan, and act on webpages, but reliable generalized web automation remains limited by grounding, long-horizon robustness, verification, safety, and realistic evaluation.
```

S4 shows that web agents can now:

```text
observe webpages
use DOM or screenshots
search and navigate
interact with buttons and text fields
follow natural-language tasks
collect references
use multimodal reasoning
operate on live websites
```

But they still do not fully solve:

```text
precise DOM/visual grounding
dynamic page state tracking
robust long-horizon planning
safe irreversible actions
structured data extraction verification
handling popups/CAPTCHAs/login
dense text and visual ambiguity
multi-page memory
online/offline evaluation mismatch
cost, latency, and reliability at deployment
```

So the refined S4 gap is:

```text
Web-agent systems have moved from controlled environments to live multimodal interaction, but the core unsolved problem is reliable grounding and verification across diverse, dynamic, real-world websites.
```

---

## 6. Thesis connection

For the thesis topic, **“LLM-based agents for generalized web automation and data extraction,”** S4 supports five major claims.

### Claim 1 — The web is a natural but difficult agent environment

World of Bits shows that the web is an open-domain environment with rich tasks, visual interfaces, DOM structures, and human-like actions. However, early RL methods struggled, especially on compound and keyboard-heavy tasks.

### Claim 2 — LLMs make web browsing more language-aware

WebGPT shows that LLMs can use a browser-like environment to search, navigate, collect evidence, and synthesize answers. This supports the idea that LLMs can serve as the reasoning and information-access core of web agents.

### Claim 3 — Scalable benchmarks require semantic actions and automatic rewards

WebShop shows that web-agent benchmarks can be scaled using realistic data, natural-language instructions, semantic actions, and programmatic rewards. This is important for studying grounded language interaction at scale.

### Claim 4 — Multimodal models improve web perception but do not solve grounding

SeeAct shows that GPT-4V has strong potential for web agents, but grounding natural-language plans into precise HTML elements and operations remains a major bottleneck.

### Claim 5 — Live-web systems expose real deployment failures

WebVoyager shows that end-to-end multimodal agents can operate on live websites, but failures such as navigation loops, visual grounding errors, hallucination, and prompt misalignment remain serious obstacles.

---

## 7. Thesis-ready synthesis paragraph

The evolution of web-agent systems shows a progression from early reinforcement-learning environments to modern multimodal LLM agents operating on live websites. World of Bits introduced the web as an open-domain interactive environment where agents observe pixels and DOM elements and act through keyboard and mouse commands. This established the basic perception-action structure of web automation but also revealed the limitations of low-level RL under sparse rewards and long-horizon interaction. WebGPT shifted the field toward LLM-based browsing by fine-tuning GPT-3 to search, navigate, quote references, and answer long-form questions using human feedback. WebShop then provided a scalable grounded web-interaction benchmark, using realistic e-commerce data, natural-language instructions, semantic actions, and automatic rewards. More recent systems move from text-based or simulated interaction to multimodal live-web agents. SeeAct shows that GPT-4V can generate strong web-action plans if oracle grounding is available, but automatic element grounding remains a major bottleneck. WebVoyager demonstrates an end-to-end multimodal web agent that interacts with real websites using screenshots, labeled elements, and step-by-step reasoning, achieving substantial task success but still failing through navigation loops, grounding errors, hallucination, and prompt misalignment. Together, these papers show that LLM-based web agents have become increasingly realistic and capable, but generalized web automation and data extraction still require robust DOM and visual grounding, long-horizon planning, state tracking, verification, safety constraints, and deployment-aware evaluation.

---

## 8. Limitations connected to the thesis

### 8.1 World of Bits limitation — low-level control is difficult

World of Bits uses raw keyboard and mouse actions.

For generalized web automation, this matters because low-level actions create a very large action space. The agent must learn where to move, click, type, drag, and scroll from sparse rewards. This motivates modern web agents that use higher-level semantic actions and LLM reasoning.

### 8.2 World of Bits limitation — reproducibility vs realism

FormWoB caches HTTP traffic to make real websites reproducible.

For the thesis, this matters because web-agent evaluation must balance two competing goals:

```text
reproducibility
realistic live-web behavior
```

This tension continues in later offline vs online evaluation debates.

### 8.3 WebGPT limitation — text browsing is not full automation

WebGPT can search, click, quote, and answer, but it does not interact with full visual web interfaces.

For generalized web automation, this matters because many tasks require forms, calendars, dropdowns, visual layout, account state, and structured extraction.

### 8.4 WebGPT limitation — references can mislead

References improve factual evaluation, but they can be cherry-picked or incomplete.

For web data extraction, this matters because an extracted value must be verified against the right source context, not merely accompanied by a plausible citation.

### 8.5 WebShop limitation — simulated and domain-specific

WebShop is large and realistic in product data, but it remains an e-commerce simulation.

For generalized web automation, this matters because real web tasks span many domains and include live interfaces, pop-ups, login flows, CAPTCHAs, changing layouts, and unpredictable states.

### 8.6 WebShop limitation — agents lack exploration and memory

WebShop shows that humans explore more products, reformulate queries, and remember previous items better than models.

For web extraction, this matters because agents must compare alternatives, backtrack, and remember evidence across pages.

### 8.7 SeeAct limitation — grounding is the bottleneck

SeeAct shows that GPT-4V can generate good plans with oracle grounding, but automatic grounding is much weaker.

For the thesis, this is central: a web agent cannot succeed if it cannot map high-level plans to exact DOM elements, visual targets, and operations.

### 8.8 SeeAct limitation — offline evaluation is incomplete

The paper shows discrepancies between offline and online evaluation because multiple valid plans may solve the same task.

For web-agent evaluation, this matters because fixed reference trajectories may unfairly penalize valid alternative strategies.

### 8.9 WebVoyager limitation — live agents still fail often

WebVoyager identifies major failure categories:

```text
navigation stuck
visual grounding issue
hallucination
prompt misalignment
```

For the thesis, these failures motivate a dedicated failure-mode section and support the need for robust planning, grounding, and verification.

### 8.10 WebVoyager limitation — deployment constraints remain

WebVoyager avoids login and CAPTCHA tasks and still requires careful evaluation.

For real generalized automation, this matters because many practical workflows require authentication, permissions, privacy controls, and safe handling of irreversible actions.

---

## 9. Cross-links to later sections

| Paper | Feeds |
|---|---|
| World of Bits | S5.1 benchmarks, S5.2 DOM/pixel grounding, S5.4 behavioral cloning/RL, S5.5 sparse rewards and low-level action failure, S8 reproducibility |
| WebGPT | S5.4 human feedback, S6 web QA/extraction, S7 references and truthfulness, S8 live web safety |
| WebShop | S5.1 benchmark design, S5.3 exploration/planning, S5.4 imitation/RL, S5.5 search and option-selection failures, S8 sim-to-real |
| SeeAct | S5.1 offline vs online evaluation, S5.2 visual/HTML grounding, S5.3 action generation, S5.5 grounding failure, S7 safety |
| WebVoyager | S5.1 online evaluation, S5.2 multimodal perception, S5.3 end-to-end planning, S5.5 navigation/grounding/hallucination failures, S8 deployment |

---

## 10. Transition to S5

S4 shows the evolution of web-agent systems, but it also reveals that the field has several unresolved technical problems.

S5 should therefore analyze these problems in detail.

The transition question is:

```text
What technical components determine whether a web agent succeeds or fails?
```

S5 should be organized around the main technical dimensions exposed by S4:

```text
S5.1 — Benchmarks and evaluation
How do we measure web-agent success?

S5.2 — Perception, grounding, and interface representation
How does the agent represent DOM, HTML, screenshots, elements, and actions?

S5.3 — Planning and decision-making
How does the agent choose multi-step web actions?

S5.4 — Training strategies and generalization
How do agents learn from demonstrations, rewards, feedback, synthetic data, or memory?

S5.5 — Failure modes
Why do agents fail through loops, grounding errors, hallucinations, weak verification, and unsafe actions?
```

S4 therefore prepares the literature review to move from:

```text
chronological evolution of web agents
```

to:

```text
technical decomposition of web-agent capabilities and limitations
```

---

## 11. Final S4 mini-synthesis

S4 establishes the evolution of web-agent systems from early RL-based platforms to modern multimodal LLM agents. World of Bits introduced the web as an open-domain environment where agents observe pixels and DOM structures and act through keyboard and mouse commands. WebGPT shifted the field toward LLM-based browsing, using GPT-3, a text-based browser, evidence collection, and human feedback for long-form question answering. WebShop introduced a scalable grounded web-interaction benchmark with realistic e-commerce data, natural-language instructions, semantic actions, and automatic rewards. SeeAct showed that GPT-4V has strong potential as a generalist web agent, but only if its action plans can be grounded into precise executable browser actions. WebVoyager demonstrated an end-to-end multimodal agent operating on live websites using screenshots, labeled interactive elements, and step-by-step reasoning.

Together, these papers show that web agents have become increasingly capable and realistic. The field has moved from controlled web tasks and low-level actions toward live multimodal systems that can search, browse, click, type, scroll, and answer. However, the same papers also show that generalized web automation and data extraction remain unsolved. The main open challenges are robust DOM and visual grounding, long-horizon planning, dynamic state tracking, reliable extraction verification, safe handling of live-web actions, and realistic evaluation under deployment constraints. S4 therefore motivates the next section: a technical analysis of benchmarks, grounding, planning, training, and failure modes in LLM-based web agents.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\writing\S4_refined_synthesis_after_P1.md

# S4 Refined Synthesis — Evolution of Web Agent Systems
## Updated after S4 P0 + S4 P1 papers

## 1. What changed after adding S4 P1

The S4 P0 synthesis established the main historical arc:

```text
World of Bits
→ WebGPT
→ WebShop
→ SeeAct
→ WebVoyager
```

This gave the first web-agent progression:

```text
web as RL environment
→ text-based LLM browsing
→ scalable grounded web interaction
→ multimodal grounding
→ end-to-end live multimodal web automation
```

After adding the S4 P1 papers, the section becomes broader and more technically complete. The refined S4 narrative is now:

```text
World of Bits
→ Workflow-Guided Exploration
→ DOM-Q-NET
→ WebGPT
→ WebShop
→ WebAgent
→ SeeAct
→ WebVoyager
→ AutoWebGLM
→ Agent S / AutoGLM
→ WALT
→ WebAgent and GUI-agent surveys
```

Conceptually, this means S4 is no longer only a chronological history of web agents. It becomes a full evolution from:

```text
low-level RL browser control
→ DOM-aware RL
→ LLM browsing
→ simulated grounded web interaction
→ real-world HTML-specialized agents
→ multimodal live-web agents
→ trained/deployable web agents
→ general GUI/computer-use agents
→ tool-based web automation
```

The P1 papers add five important refinements:

1. **Pre-LLM web agents were already struggling with exploration and grounding.**  
   Workflow-Guided Exploration and DOM-Q-NET show that sparse rewards, low-level actions, and DOM representation were central problems before LLMs.

2. **Real-world websites require long HTML handling and open-ended action generation.**  
   WebAgent shows that simulated websites are too simple compared with real websites, where HTML is long, messy, dynamic, and task-irrelevant.

3. **Training and bootstrapping matter, not only prompting.**  
   AutoWebGLM shows that smaller open models can become competitive web-navigation agents through HTML simplification, trajectory data, curriculum learning, RL, and rejection sampling finetuning.

4. **Web agents are part of a broader GUI-agent and computer-use-agent movement.**  
   Agent S, AutoGLM, and GUI-agent surveys show that web automation shares core problems with mobile and desktop automation: perception, grounding, planning, memory, action execution, and safety.

5. **The next direction is action abstraction and tool learning.**  
   WALT shifts web automation away from fragile primitive UI actions toward discovered website-level tools such as `search`, `filter`, `sort`, `create`, `edit`, and `delete`.

---

## 2. Refined S4 narrative

Section S4 explains how web-agent systems evolved from early reinforcement-learning environments to modern LLM/LMM-powered agents capable of interacting with real websites and broader graphical user interfaces.

The earliest stage is represented by **World of Bits**, **Workflow-Guided Exploration**, and **DOM-Q-NET**. These papers treat web automation as a sequential decision-making problem. The web page is an environment; the agent observes pixels, DOM structures, or HTML trees; and it acts through mouse, keyboard, click, or type actions. This pre-LLM stage is important because it identifies the core difficulties of web automation before modern LLMs: sparse rewards, large action spaces, long trajectories, demonstration dependence, weak exploration, and DOM grounding.

World of Bits establishes the web as an open-domain interactive environment. Workflow-Guided Exploration then addresses the sparse-reward problem by using demonstrations to induce high-level workflows that constrain exploration. DOM-Q-NET shifts attention to webpage structure by representing the DOM as a graph and learning grounded RL policies over DOM elements. Together, these papers show that web automation is not merely text processing. It requires environment perception, structural grounding, action selection, and sequential feedback.

The second stage begins with **WebGPT**. WebGPT shifts the field from RL web-interface control to LLM-based browsing. Instead of controlling a full browser visually, GPT-3 is fine-tuned to use a text-based browser with commands such as search, click, find, quote, scroll, and end. WebGPT is important because it shows that LLMs can use the web as an external information source and can collect references to support final answers. However, it remains a browser-assisted question-answering system, not a general web automation system. It does not handle visual layout, forms, dynamic pages, DOM-level action grounding, or structured extraction.

The third stage is represented by **WebShop**. WebShop introduces a scalable simulated e-commerce environment where agents follow natural-language shopping instructions, search products, inspect results, choose options, and make purchases. It abstracts away raw mouse and keyboard actions into semantic actions such as `search[query]` and `choose[item]`. WebShop is important because it connects language grounding, product search, exploration, comparison, backtracking, memory, and automatic reward computation. However, it remains domain-specific and simulated.

The fourth stage is real-world LLM web automation, represented strongly by **WebAgent** and **AutoWebGLM**. WebAgent argues that real websites are much harder than simulated ones because they have open-ended actions, long messy HTML, and no predefined action space. It uses HTML-T5 for planning and HTML summarization, and Flan-U-PaLM for grounded program synthesis. AutoWebGLM takes a different but related direction: it builds a trained web-navigation agent on ChatGLM3-6B using HTML simplification, human-AI trajectory data, curriculum learning, reinforcement learning, and rejection sampling finetuning. These papers show that real-world web automation requires specialized observation processing, training data, task decomposition, and self-improvement.

The fifth stage is multimodal and live-web automation, represented by **SeeAct** and **WebVoyager**. SeeAct separates web-agent behavior into action generation and action grounding. It shows that GPT-4V can produce strong high-level action plans, but automatic grounding into exact HTML elements and operations remains the main bottleneck. WebVoyager then builds an end-to-end multimodal web agent that operates on real websites using screenshots, labeled interactive elements, and ReAct-style step-by-step reasoning. Together, these papers show that multimodal models bring web agents closer to human-like browsing, but grounding, navigation loops, hallucination, and evaluation remain major barriers.

The sixth stage broadens web agents into **GUI and computer-use agents**. Agent S uses experience-augmented hierarchical planning, online web knowledge, narrative memory, episodic memory, and an Agent-Computer Interface to operate computers like a human. AutoGLM develops foundation agents for web and mobile GUIs and emphasizes the separation of planning and grounding through an intermediate interface. GUI-agent surveys then place web agents inside a larger automation landscape that includes web browsers, mobile apps, desktop software, cross-platform environments, and large action models. This matters because generalized web automation is part of a broader shift from chatbots to agents that control digital interfaces.

The final forward-looking stage is **WALT**, which argues that web agents should not always rely on brittle step-by-step UI interactions. Instead, they can reverse-engineer website-provided functionality into reusable tools, such as `search`, `filter`, `sort`, `create`, `edit`, `delete`, `comment`, and `upvote`. This suggests a next-generation direction for web automation: combining LLM planning with website-specific tool discovery and validated high-level action abstractions.

---

## 3. Refined S4 architecture/evolution stack

| Stage | Main papers | Main contribution | What it adds to S4 |
|---|---|---|---|
| Web as environment | World of Bits | Webpages as interactive environments with pixels, DOM, rewards, keyboard/mouse actions | Historical foundation |
| Workflow-guided RL | Workflow-Guided Exploration | Demonstrations induce workflows to constrain sparse-reward exploration | Demonstration-guided web RL |
| DOM-aware RL | DOM-Q-NET | Graph neural network over DOM trees and factorized Q-functions | Structured DOM grounding |
| LLM text browsing | WebGPT | GPT-3 uses a text browser, quotes evidence, and learns from human feedback | LLM-based web evidence gathering |
| Grounded simulated web interaction | WebShop | Scalable e-commerce benchmark with semantic actions and automatic rewards | Language-grounded web task benchmark |
| Real-world HTML-specialized agent | WebAgent | Long HTML summarization, task decomposition, Python program synthesis | Real-web HTML and open-ended actions |
| Multimodal grounding | SeeAct | Separates action generation from action grounding; identifies grounding bottleneck | Visual/HTML grounding diagnosis |
| Live multimodal web agent | WebVoyager | End-to-end LMM agent on real websites with screenshots and labeled elements | Live-web multimodal automation |
| Trained web-navigation agent | AutoWebGLM | HTML simplification, browsing traces, curriculum learning, RL, RFT, AutoWebBench | Open trained deployable web agent |
| Computer-use GUI agent | Agent S | Hierarchical planning, web knowledge, narrative/episodic memory, ACI | Cross-application GUI automation |
| Foundation GUI agent | AutoGLM | Intermediate interface, planning-grounding separation, online curriculum RL | Deployable GUI foundation agents |
| Tool-based web automation | WALT | Reverse-engineers website functionality into reusable tools | Future direction beyond primitive UI steps |
| Survey/taxonomy layer | WebAgent + GUI-agent surveys | Architecture, training, evaluation, trustworthiness, roadmap | Organizes S5 and S7/S8 |

---

## 4. Refined conceptual contribution of S4

The central contribution of S4 is to show that **web agents evolved through successive abstractions of the web interface**.

The interface abstraction changes over time:

```text
pixels + mouse/keyboard
→ DOM and HTML structure
→ text browser commands
→ semantic actions
→ programmatic browser actions
→ screenshots + labeled elements
→ simplified HTML + trained action models
→ intermediate GUI interfaces
→ learned website tools
```

This is the key S4 idea:

```text
Progress in web agents is progress in representing, grounding, and abstracting interaction with the web.
```

Early RL agents struggled because the web interface was too large and sparse at the pixel/mouse level. DOM-aware agents improved grounding by using webpage structure. LLM browsing improved language reasoning and evidence gathering. WebShop improved scalable grounded evaluation through semantic actions. WebAgent and AutoWebGLM improved real-web handling through HTML simplification, long-context processing, program synthesis, and training. SeeAct and WebVoyager improved multimodal perception but exposed the grounding bottleneck. Agent S and AutoGLM generalized web automation to computer-use and GUI foundation agents. WALT suggests that future agents may automate websites by discovering reliable high-level tools rather than repeatedly reasoning over primitive clicks.

---

## 5. Refined gap after S4 P1

After S4 P0, the gap was:

```text
Web-agent systems have moved from controlled environments to live multimodal interaction, but the core unsolved problem is reliable grounding and verification across diverse, dynamic, real-world websites.
```

After adding S4 P1, the gap becomes more precise:

```text
Web agents have progressed from RL interface control to trained multimodal and tool-augmented systems, but generalized web automation still lacks robust cross-site grounding, long-horizon reliability, safe execution, verified extraction, and maintainable action abstractions.
```

S4 now shows that web agents can:

```text
operate in browser-like environments
use pixels, DOM, HTML, screenshots, and accessibility trees
browse textually and cite evidence
act semantically in simulated websites
summarize long HTML
generate Python automation programs
use multimodal visual understanding
train smaller open web-navigation models
use memory and hierarchical planning
control broader GUIs
learn or expose website tools
```

But they still do not fully solve:

```text
precise element grounding across arbitrary websites
visual-DOM alignment under dynamic layouts
long-horizon task reliability
safe irreversible action handling
robust verification of extracted data
evaluation beyond fixed trajectories
privacy and permission control
resistance to popups, CAPTCHAs, ads, and authentication
state tracking across multi-page workflows
maintenance when websites change
cost and latency under real deployment
```

Therefore, the refined S4 gap is:

```text
The field has developed increasingly powerful web-agent architectures, but the remaining bottleneck is making their perception, planning, action abstraction, and verification reliable enough for generalized real-world web automation and data extraction.
```

---

## 6. Thesis connection

For the thesis topic, **“LLM-based agents for generalized web automation and data extraction,”** S4 supports seven major claims.

### Claim 1 — Web automation is a sequential decision-making problem

World of Bits, Workflow-Guided Exploration, and DOM-Q-NET show that web automation is not just scraping or text extraction. It is an interactive decision problem:

```text
observe state → choose action → execute → observe new state → continue
```

This supports the thesis framing of web automation as an agentic problem.

### Claim 2 — DOM and interface representation are foundational

DOM-Q-NET, WebAgent, AutoWebGLM, SeeAct, and WebVoyager all show that the way the page is represented strongly determines agent success. Web agents may use:

```text
DOM trees
HTML snippets
simplified HTML
accessibility trees
screenshots
OCR
labeled UI elements
multimodal observations
```

This directly motivates S5.2.

### Claim 3 — LLMs improve instruction following and reasoning but do not remove grounding problems

WebGPT, WebShop, WebAgent, SeeAct, and WebVoyager show that LLMs/LMMs improve browsing, planning, and language grounding. However, SeeAct and WebVoyager show that a correct high-level plan can still fail if the agent cannot ground it into the correct element or operation.

### Claim 4 — Training and experience are needed for robust web agents

Workflow-Guided Exploration, WebAgent, AutoWebGLM, Agent S, and AutoGLM show that prompting alone is insufficient. Web agents benefit from:

```text
demonstrations
workflow constraints
self-experience
curriculum learning
reinforcement learning
rejection sampling finetuning
episodic memory
narrative memory
online learning
```

This motivates S5.4.

### Claim 5 — Generalized web automation is part of broader GUI automation

Agent S, AutoGLM, and the GUI-agent surveys show that web agents are one branch of a larger GUI-agent ecosystem. Many web challenges also appear in mobile and desktop agents:

```text
visual grounding
action abstraction
long-horizon planning
memory
safety
privacy
latency
cross-platform generalization
```

This helps broaden the thesis without losing the web-specific focus.

### Claim 6 — Future web agents may need tool abstraction, not only UI actions

WALT shows that repeatedly clicking and typing is brittle. A more reliable direction is to discover reusable site-level tools:

```text
search(query)
filter(criteria)
sort(order)
create(item)
edit(item)
delete(item)
comment(text)
```

This connects S4 back to S3 tool-use architectures and forward to S6 extraction tools and S8 deployment.

### Claim 7 — Evaluation remains unresolved

World of Bits, WebShop, SeeAct, WebVoyager, AutoWebGLM, and the surveys all expose evaluation problems:

```text
offline vs online evaluation
fixed reference trajectories vs multiple valid solutions
simulated vs live websites
human evaluation vs automatic evaluation
success rate vs extraction correctness
safety and risk evaluation
cost/latency metrics
```

This motivates S5.1.

---

## 7. Refined thesis-ready synthesis paragraph

The evolution of web-agent systems shows a progression from early reinforcement-learning interfaces to modern LLM/LMM-powered agents operating on real websites and broader graphical user interfaces. World of Bits first framed the web as an open-domain interactive environment where agents observe pixels and DOM structures and act through keyboard and mouse events. Workflow-Guided Exploration and DOM-Q-NET then addressed two early bottlenecks of web RL: sparse-reward exploration and DOM-structured action grounding. WebGPT shifted the field toward LLM-based browsing by fine-tuning GPT-3 to search, navigate, quote evidence, and answer questions with human feedback. WebShop introduced scalable grounded web interaction through a simulated e-commerce environment with semantic actions and automatic rewards. More recent systems address the gap between simulated tasks and real websites. WebAgent combines planning, long HTML summarization, and program synthesis to act on real websites, while AutoWebGLM trains an open web-navigation model using simplified HTML, browsing traces, curriculum learning, reinforcement learning, and rejection sampling finetuning. Multimodal systems such as SeeAct and WebVoyager show that large multimodal models can reason over rendered webpages and perform live browser actions, but they also reveal that precise action grounding remains a major bottleneck. Broader GUI-agent systems such as Agent S and AutoGLM extend these ideas to desktop and mobile interfaces through hierarchical planning, memory, intermediate interfaces, and online curriculum learning. Finally, WALT suggests a future direction in which agents reverse-engineer website functionality into reusable tools, reducing reliance on brittle step-by-step UI actions. Together, these works show that web agents have become increasingly capable, but generalized web automation and data extraction still require robust DOM/visual grounding, long-horizon planning, safe execution, verified extraction, realistic evaluation, and deployment-aware action abstractions.

---

## 8. Refined limitations connected to the thesis

### 8.1 Low-level action limitation

Early systems such as World of Bits operate with low-level keyboard and mouse actions.

For generalized web automation, this matters because low-level control creates large action spaces and long trajectories. A data-extraction agent should not always reason at the level of pixels and mouse movements; it needs higher-level abstractions such as DOM elements, semantic actions, API calls, or tools.

### 8.2 Sparse reward and exploration limitation

Workflow-Guided Exploration shows that RL agents struggle when reward appears only after complete task success.

For web automation, this matters because many workflows have delayed success signals. A form may only fail at submission. A product search may only be wrong after comparison. An extraction may look correct but fail later verification.

### 8.3 DOM representation limitation

DOM-Q-NET shows that DOM structure helps, but simplified benchmark DOMs do not fully capture real websites.

For generalized automation, this matters because real DOMs are long, noisy, dynamic, and often disconnected from the visible human interface.

### 8.4 Text-browser limitation

WebGPT shows that LLMs can browse textually and cite evidence, but text browsing is not full browser automation.

For the thesis, this matters because data extraction and web automation often require forms, dropdowns, dynamic widgets, tables, visual layout, authentication, and structured outputs.

### 8.5 Simulated benchmark limitation

WebShop provides scalable grounded evaluation, but it remains a simulated e-commerce environment.

For generalized automation, this matters because real websites are multi-domain, dynamic, and often not reproducible.

### 8.6 Long HTML limitation

WebAgent and AutoWebGLM show that real HTML can exceed model context limits and contain large amounts of irrelevant content.

For web extraction, this matters directly because the agent must compress the page without removing relevant evidence.

### 8.7 Program synthesis limitation

WebAgent uses generated Python programs to act on websites.

For deployment, this matters because generated code can be powerful but risky. It must be sandboxed, constrained, inspected, or verified before execution.

### 8.8 Grounding limitation

SeeAct shows the gap between action generation and action grounding.

For generalized web automation, this is central. The agent may know what to do but fail to select the correct element, operation, or input value.

### 8.9 Live-web reliability limitation

WebVoyager shows that live multimodal agents fail through navigation loops, visual grounding issues, hallucination, and prompt misalignment.

For the thesis, these failures motivate a dedicated failure-mode analysis.

### 8.10 Training-data limitation

AutoWebGLM shows the importance of high-quality web-browsing traces.

For web agents, this matters because collecting representative trajectories across websites, languages, tasks, and failure cases is expensive.

### 8.11 Planning-grounding separation limitation

AutoGLM argues that planning and grounding require separate optimization.

For web agents, this matters because flexible reasoning and precise UI control are different abilities. A single prompt or model may not optimize both well.

### 8.12 Memory limitation

Agent S shows the value of narrative and episodic memory, but memory can also be stale, irrelevant, or wrong.

For web automation, memory must be evidence-grounded and verified, especially when websites change.

### 8.13 Tool-maintenance limitation

WALT shows that learned website tools can reduce brittle UI steps.

However, for deployment, tools must be discovered, validated, updated, and monitored as websites change. This creates a new maintenance problem.

### 8.14 Survey limitation

The GUI-agent and WebAgent surveys provide useful taxonomies, but they do not replace primary system papers.

For thesis writing, use surveys to structure the field and primary papers to support technical and empirical claims.

---

## 9. Updated cross-links to later sections

| Paper | Feeds |
|---|---|
| World of Bits | S5.1 benchmarks, S5.2 DOM/pixel grounding, S5.4 RL/behavioral cloning, S5.5 sparse-reward failures, S8 reproducibility |
| Workflow-Guided Exploration | S5.3 exploration/planning, S5.4 demonstrations/RL, S5.5 sparse rewards and overfitting |
| DOM-Q-NET | S5.2 DOM representation, S5.4 RL/multitask learning, S5.5 large variable action spaces |
| WebGPT | S5.4 human feedback, S6 web QA/extraction, S7 references/truthfulness, S8 live web access risk |
| WebShop | S5.1 scalable benchmark design, S5.3 search/exploration/planning, S5.4 imitation/RL, S8 sim-to-real |
| WebAgent | S5.2 long HTML summarization, S5.3 sub-instruction planning, S5.4 self-experience, S6 programmatic extraction, S8 real-web deployment |
| SeeAct | S5.1 offline vs online evaluation, S5.2 visual/HTML grounding, S5.3 action generation, S5.5 grounding failures, S7 safety |
| WebVoyager | S5.1 online evaluation, S5.2 multimodal perception, S5.3 end-to-end planning, S5.5 navigation/grounding/hallucination failures, S8 deployment |
| AutoWebGLM | S5.1 AutoWebBench, S5.2 HTML simplification, S5.3 task decomposition, S5.4 curriculum/RL/RFT, S5.5 loop/self-check failures, S8 browser extension |
| Agent S | S5.2 GUI grounding, S5.3 hierarchical planning, S5.4 memory/experience, S5.5 GUI failures, S8 cross-platform computer use |
| AutoGLM | S5.2 intermediate interface/grounding, S5.3 planning, S5.4 online curriculum RL, S5.5 error recovery, S8 deployable foundation agents |
| GUI-agent surveys | S5.1 evaluation, S5.2 perception, S5.3 planning/action, S5.4 data/models, S5.5 limitations, S8 roadmap |
| WebAgents survey | S5.1 evaluation, S5.2 perception, S5.3 planning/reasoning/execution, S5.4 training, S7 trustworthiness |
| WALT | S5.2 action/tool abstraction, S5.3 tool-based planning, S5.4 tool learning, S5.5 brittle UI-action failures, S6 extraction tools, S8 maintenance |

---

## 10. How S4 should be written in the thesis

A strong final thesis section for S4 can be organized into six subsections:

### S4.1 Pre-LLM web agents: web as an RL environment

Use:

```text
World of Bits
Workflow-Guided Exploration
DOM-Q-NET
```

Main argument:

```text
Before LLMs, web agents were treated as RL agents in browser environments, but sparse rewards, low-level actions, and DOM grounding made generalization difficult.
```

### S4.2 LLM browsing and evidence-grounded web QA

Use:

```text
WebGPT
```

Main argument:

```text
LLMs introduced stronger language reasoning and evidence-gathering ability, but text-based browsing remained narrower than full web automation.
```

### S4.3 Scalable grounded interaction benchmarks

Use:

```text
WebShop
```

Main argument:

```text
WebShop made web-agent evaluation scalable through realistic product data, semantic actions, and automatic rewards, but remained simulated and domain-specific.
```

### S4.4 Real-world LLM web agents

Use:

```text
WebAgent
AutoWebGLM
```

Main argument:

```text
Real websites require long HTML handling, observation simplification, task decomposition, program synthesis, trajectory data, and web-specific training.
```

### S4.5 Multimodal live-web agents

Use:

```text
SeeAct
WebVoyager
```

Main argument:

```text
LMMs improve visual web understanding, but reliable browser control depends on precise grounding and robust online evaluation.
```

### S4.6 From web agents to GUI/foundation/tool agents

Use:

```text
Agent S
AutoGLM
WALT
GUI-agent surveys
WebAgents survey
```

Main argument:

```text
Web automation is becoming part of a broader GUI-agent and computer-use-agent paradigm, where planning, grounding, memory, action abstraction, trustworthiness, and deployment become central.
```

---

## 11. Final refined S4 synthesis

S4 establishes the evolution of web-agent systems from early RL-based browser environments to modern LLM/LMM-powered agents and emerging tool-based automation. Early systems such as World of Bits, Workflow-Guided Exploration, and DOM-Q-NET framed the web as an interactive decision environment and showed that web automation is difficult because of sparse rewards, low-level actions, long trajectories, and DOM grounding. WebGPT shifted the field toward LLM-based browsing, where a model can search, navigate, quote evidence, and answer questions with human feedback. WebShop then introduced a scalable grounded web-interaction benchmark with semantic actions, realistic e-commerce data, and automatic rewards.

Later systems move closer to real-world web automation. WebAgent addresses real websites through planning, long HTML summarization, and program synthesis. AutoWebGLM shows that trained open LLMs can become competitive web-navigation agents through HTML simplification, browsing traces, curriculum learning, reinforcement learning, and rejection sampling finetuning. SeeAct and WebVoyager introduce the multimodal live-web paradigm: agents use screenshots, visual reasoning, and labeled interactive elements to act on real websites. These systems show strong progress but also reveal the grounding bottleneck, navigation loops, hallucinations, and online evaluation difficulty.

The most recent direction broadens web agents into GUI and computer-use agents. Agent S and AutoGLM show that web automation shares core challenges with desktop and mobile automation: hierarchical planning, memory, intermediate interfaces, action grounding, and online learning. GUI-agent and WebAgent surveys provide the broader taxonomy of perception, planning, action, training, evaluation, and trustworthiness. WALT suggests an important future direction: instead of relying only on fragile primitive UI actions, web agents can discover and invoke high-level website tools.

Overall, S4 shows that web agents have moved from controlled web tasks toward real, multimodal, trained, and tool-augmented systems. However, generalized web automation and data extraction remain unsolved. The main remaining challenges are robust DOM and visual grounding, long-horizon planning, state tracking, verified extraction, safe execution, realistic evaluation, privacy, latency, and maintainable action abstractions. This refined S4 synthesis therefore motivates S5: a technical decomposition of the components that determine web-agent success or failure—benchmarks, perception and grounding, planning, training, and failure modes.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\writing\S4_refined_synthesis_after_P1_updated_verified.md

# S4 Refined Synthesis — Evolution of Web Agent Systems
## Updated after S4 P0 + S4 P1 papers

## Publication-status update for S4 P1 citations

The S4 narrative remains unchanged, but the final citation metadata should use the verified venue/status below:

| Paper | Final venue/status to use |
|---|---|
| Workflow-Guided Exploration | ICLR 2018 conference paper |
| DOM-Q-NET | ICLR 2019 conference paper |
| WebAgent | ICLR 2024 conference paper |
| Large Language Model Powered Agents in the Web | WWW 2024 Companion tutorial paper |
| AutoWebGLM Bootstrap and Reinforce | arXiv extended/preprint version; use KDD 2024 AutoWebGLM for final citation |
| Agent S | ICLR 2025 Poster |
| AutoGLM | arXiv preprint |
| Large Language Model-Brained GUI Agents preprint | arXiv preprint; use TMLR 2025 version for final citation |
| AutoWebGLM | KDD 2024 conference paper |
| GUI Agents with Foundation Models | arXiv preprint |
| A Survey on (M)LLM-Based GUI Agents | arXiv preprint |
| Large Language Model-Brained GUI Agents | TMLR 2025 |
| GUI Agents: A Survey | Findings of ACL 2025 |
| A Survey of WebAgents | KDD 2025 Tutorial & Survey Track |
| WALT | ICLR 2026 Poster |


## 1. What changed after adding S4 P1

The S4 P0 synthesis established the main historical arc:

```text
World of Bits
→ WebGPT
→ WebShop
→ SeeAct
→ WebVoyager
```

This gave the first web-agent progression:

```text
web as RL environment
→ text-based LLM browsing
→ scalable grounded web interaction
→ multimodal grounding
→ end-to-end live multimodal web automation
```

After adding the S4 P1 papers, the section becomes broader and more technically complete. The refined S4 narrative is now:

```text
World of Bits
→ Workflow-Guided Exploration
→ DOM-Q-NET
→ WebGPT
→ WebShop
→ WebAgent
→ SeeAct
→ WebVoyager
→ AutoWebGLM
→ Agent S / AutoGLM
→ WALT
→ WebAgent and GUI-agent surveys
```

Conceptually, this means S4 is no longer only a chronological history of web agents. It becomes a full evolution from:

```text
low-level RL browser control
→ DOM-aware RL
→ LLM browsing
→ simulated grounded web interaction
→ real-world HTML-specialized agents
→ multimodal live-web agents
→ trained/deployable web agents
→ general GUI/computer-use agents
→ tool-based web automation
```

The P1 papers add five important refinements:

1. **Pre-LLM web agents were already struggling with exploration and grounding.**  
   Workflow-Guided Exploration and DOM-Q-NET show that sparse rewards, low-level actions, and DOM representation were central problems before LLMs.

2. **Real-world websites require long HTML handling and open-ended action generation.**  
   WebAgent shows that simulated websites are too simple compared with real websites, where HTML is long, messy, dynamic, and task-irrelevant.

3. **Training and bootstrapping matter, not only prompting.**  
   The final KDD 2024 AutoWebGLM paper shows that smaller open models can become competitive web-navigation agents through HTML simplification, trajectory data, curriculum learning, RL, and rejection sampling finetuning.

4. **Web agents are part of a broader GUI-agent and computer-use-agent movement.**  
   Agent S (ICLR 2025), AutoGLM, and GUI-agent surveys show that web automation shares core problems with mobile and desktop automation: perception, grounding, planning, memory, action execution, and safety.

5. **The next direction is action abstraction and tool learning.**  
   WALT (ICLR 2026) shifts web automation away from fragile primitive UI actions toward discovered website-level tools such as `search`, `filter`, `sort`, `create`, `edit`, and `delete`.

---

## 2. Refined S4 narrative

Section S4 explains how web-agent systems evolved from early reinforcement-learning environments to modern LLM/LMM-powered agents capable of interacting with real websites and broader graphical user interfaces.

The earliest stage is represented by **World of Bits**, **Workflow-Guided Exploration**, and **DOM-Q-NET**. These papers treat web automation as a sequential decision-making problem. The web page is an environment; the agent observes pixels, DOM structures, or HTML trees; and it acts through mouse, keyboard, click, or type actions. This pre-LLM stage is important because it identifies the core difficulties of web automation before modern LLMs: sparse rewards, large action spaces, long trajectories, demonstration dependence, weak exploration, and DOM grounding.

World of Bits establishes the web as an open-domain interactive environment. Workflow-Guided Exploration then addresses the sparse-reward problem by using demonstrations to induce high-level workflows that constrain exploration. DOM-Q-NET shifts attention to webpage structure by representing the DOM as a graph and learning grounded RL policies over DOM elements. Together, these papers show that web automation is not merely text processing. It requires environment perception, structural grounding, action selection, and sequential feedback.

The second stage begins with **WebGPT**. WebGPT shifts the field from RL web-interface control to LLM-based browsing. Instead of controlling a full browser visually, GPT-3 is fine-tuned to use a text-based browser with commands such as search, click, find, quote, scroll, and end. WebGPT is important because it shows that LLMs can use the web as an external information source and can collect references to support final answers. However, it remains a browser-assisted question-answering system, not a general web automation system. It does not handle visual layout, forms, dynamic pages, DOM-level action grounding, or structured extraction.

The third stage is represented by **WebShop**. WebShop introduces a scalable simulated e-commerce environment where agents follow natural-language shopping instructions, search products, inspect results, choose options, and make purchases. It abstracts away raw mouse and keyboard actions into semantic actions such as `search[query]` and `choose[item]`. WebShop is important because it connects language grounding, product search, exploration, comparison, backtracking, memory, and automatic reward computation. However, it remains domain-specific and simulated.

The fourth stage is real-world LLM web automation, represented strongly by **WebAgent** and **AutoWebGLM**. WebAgent argues that real websites are much harder than simulated ones because they have open-ended actions, long messy HTML, and no predefined action space. It uses HTML-T5 for planning and HTML summarization, and Flan-U-PaLM for grounded program synthesis. The final KDD 2024 AutoWebGLM paper takes a different but related direction: it builds a trained web-navigation agent on ChatGLM3-6B using HTML simplification, human-AI trajectory data, curriculum learning, reinforcement learning, and rejection sampling finetuning. These papers show that real-world web automation requires specialized observation processing, training data, task decomposition, and self-improvement.

The fifth stage is multimodal and live-web automation, represented by **SeeAct** and **WebVoyager**. SeeAct separates web-agent behavior into action generation and action grounding. It shows that GPT-4V can produce strong high-level action plans, but automatic grounding into exact HTML elements and operations remains the main bottleneck. WebVoyager then builds an end-to-end multimodal web agent that operates on real websites using screenshots, labeled interactive elements, and ReAct-style step-by-step reasoning. Together, these papers show that multimodal models bring web agents closer to human-like browsing, but grounding, navigation loops, hallucination, and evaluation remain major barriers.

The sixth stage broadens web agents into **GUI and computer-use agents**. Agent S, published as an ICLR 2025 poster, uses experience-augmented hierarchical planning, online web knowledge, narrative memory, episodic memory, and an Agent-Computer Interface to operate computers like a human. AutoGLM develops foundation agents for web and mobile GUIs and emphasizes the separation of planning and grounding through an intermediate interface. GUI-agent surveys then place web agents inside a larger automation landscape that includes web browsers, mobile apps, desktop software, cross-platform environments, and large action models. This matters because generalized web automation is part of a broader shift from chatbots to agents that control digital interfaces.

The final forward-looking stage is **WALT**, which argues that web agents should not always rely on brittle step-by-step UI interactions. Instead, they can reverse-engineer website-provided functionality into reusable tools, such as `search`, `filter`, `sort`, `create`, `edit`, `delete`, `comment`, and `upvote`. This suggests a next-generation direction for web automation: combining LLM planning with website-specific tool discovery and validated high-level action abstractions.

---

## 3. Refined S4 architecture/evolution stack

| Stage | Main papers | Main contribution | What it adds to S4 |
|---|---|---|---|
| Web as environment | World of Bits | Webpages as interactive environments with pixels, DOM, rewards, keyboard/mouse actions | Historical foundation |
| Workflow-guided RL | Workflow-Guided Exploration | Demonstrations induce workflows to constrain sparse-reward exploration | Demonstration-guided web RL |
| DOM-aware RL | DOM-Q-NET | Graph neural network over DOM trees and factorized Q-functions | Structured DOM grounding |
| LLM text browsing | WebGPT | GPT-3 uses a text browser, quotes evidence, and learns from human feedback | LLM-based web evidence gathering |
| Grounded simulated web interaction | WebShop | Scalable e-commerce benchmark with semantic actions and automatic rewards | Language-grounded web task benchmark |
| Real-world HTML-specialized agent | WebAgent | Long HTML summarization, task decomposition, Python program synthesis | Real-web HTML and open-ended actions |
| Multimodal grounding | SeeAct | Separates action generation from action grounding; identifies grounding bottleneck | Visual/HTML grounding diagnosis |
| Live multimodal web agent | WebVoyager | End-to-end LMM agent on real websites with screenshots and labeled elements | Live-web multimodal automation |
| Trained web-navigation agent | AutoWebGLM, KDD 2024 | HTML simplification, browsing traces, curriculum learning, RL, RFT, AutoWebBench | Open trained deployable web agent |
| Computer-use GUI agent | Agent S, ICLR 2025 Poster | Hierarchical planning, web knowledge, narrative/episodic memory, ACI | Cross-application GUI automation |
| Foundation GUI agent | AutoGLM, arXiv preprint | Intermediate interface, planning-grounding separation, online curriculum RL | Deployable GUI foundation agents |
| Tool-based web automation | WALT, ICLR 2026 Poster | Reverse-engineers website functionality into reusable tools | Future direction beyond primitive UI steps |
| Survey/taxonomy layer | TMLR 2025 GUI survey, ACL 2025 GUI survey, KDD 2025 WebAgents survey | Architecture, training, evaluation, trustworthiness, roadmap | Organizes S5 and S7/S8 |

---

## 4. Refined conceptual contribution of S4

The central contribution of S4 is to show that **web agents evolved through successive abstractions of the web interface**.

The interface abstraction changes over time:

```text
pixels + mouse/keyboard
→ DOM and HTML structure
→ text browser commands
→ semantic actions
→ programmatic browser actions
→ screenshots + labeled elements
→ simplified HTML + trained action models
→ intermediate GUI interfaces
→ learned website tools
```

This is the key S4 idea:

```text
Progress in web agents is progress in representing, grounding, and abstracting interaction with the web.
```

Early RL agents struggled because the web interface was too large and sparse at the pixel/mouse level. DOM-aware agents improved grounding by using webpage structure. LLM browsing improved language reasoning and evidence gathering. WebShop improved scalable grounded evaluation through semantic actions. WebAgent and AutoWebGLM improved real-web handling through HTML simplification, long-context processing, program synthesis, and training. SeeAct and WebVoyager improved multimodal perception but exposed the grounding bottleneck. Agent S and AutoGLM generalized web automation to computer-use and GUI foundation agents. WALT suggests that future agents may automate websites by discovering reliable high-level tools rather than repeatedly reasoning over primitive clicks.

---

## 5. Refined gap after S4 P1

After S4 P0, the gap was:

```text
Web-agent systems have moved from controlled environments to live multimodal interaction, but the core unsolved problem is reliable grounding and verification across diverse, dynamic, real-world websites.
```

After adding S4 P1, the gap becomes more precise:

```text
Web agents have progressed from RL interface control to trained multimodal and tool-augmented systems, but generalized web automation still lacks robust cross-site grounding, long-horizon reliability, safe execution, verified extraction, and maintainable action abstractions.
```

S4 now shows that web agents can:

```text
operate in browser-like environments
use pixels, DOM, HTML, screenshots, and accessibility trees
browse textually and cite evidence
act semantically in simulated websites
summarize long HTML
generate Python automation programs
use multimodal visual understanding
train smaller open web-navigation models
use memory and hierarchical planning
control broader GUIs
learn or expose website tools
```

But they still do not fully solve:

```text
precise element grounding across arbitrary websites
visual-DOM alignment under dynamic layouts
long-horizon task reliability
safe irreversible action handling
robust verification of extracted data
evaluation beyond fixed trajectories
privacy and permission control
resistance to popups, CAPTCHAs, ads, and authentication
state tracking across multi-page workflows
maintenance when websites change
cost and latency under real deployment
```

Therefore, the refined S4 gap is:

```text
The field has developed increasingly powerful web-agent architectures, but the remaining bottleneck is making their perception, planning, action abstraction, and verification reliable enough for generalized real-world web automation and data extraction.
```

---

## 6. Thesis connection

For the thesis topic, **“LLM-based agents for generalized web automation and data extraction,”** S4 supports seven major claims.

### Claim 1 — Web automation is a sequential decision-making problem

World of Bits, Workflow-Guided Exploration, and DOM-Q-NET show that web automation is not just scraping or text extraction. It is an interactive decision problem:

```text
observe state → choose action → execute → observe new state → continue
```

This supports the thesis framing of web automation as an agentic problem.

### Claim 2 — DOM and interface representation are foundational

DOM-Q-NET, WebAgent, AutoWebGLM, SeeAct, and WebVoyager all show that the way the page is represented strongly determines agent success. Web agents may use:

```text
DOM trees
HTML snippets
simplified HTML
accessibility trees
screenshots
OCR
labeled UI elements
multimodal observations
```

This directly motivates S5.2.

### Claim 3 — LLMs improve instruction following and reasoning but do not remove grounding problems

WebGPT, WebShop, WebAgent, SeeAct, and WebVoyager show that LLMs/LMMs improve browsing, planning, and language grounding. However, SeeAct and WebVoyager show that a correct high-level plan can still fail if the agent cannot ground it into the correct element or operation.

### Claim 4 — Training and experience are needed for robust web agents

Workflow-Guided Exploration, WebAgent, AutoWebGLM, Agent S, and AutoGLM show that prompting alone is insufficient. Web agents benefit from:

```text
demonstrations
workflow constraints
self-experience
curriculum learning
reinforcement learning
rejection sampling finetuning
episodic memory
narrative memory
online learning
```

This motivates S5.4.

### Claim 5 — Generalized web automation is part of broader GUI automation

Agent S, AutoGLM, and the GUI-agent surveys show that web agents are one branch of a larger GUI-agent ecosystem. Many web challenges also appear in mobile and desktop agents:

```text
visual grounding
action abstraction
long-horizon planning
memory
safety
privacy
latency
cross-platform generalization
```

This helps broaden the thesis without losing the web-specific focus.

### Claim 6 — Future web agents may need tool abstraction, not only UI actions

WALT shows that repeatedly clicking and typing is brittle. A more reliable direction is to discover reusable site-level tools:

```text
search(query)
filter(criteria)
sort(order)
create(item)
edit(item)
delete(item)
comment(text)
```

This connects S4 back to S3 tool-use architectures and forward to S6 extraction tools and S8 deployment.

### Claim 7 — Evaluation remains unresolved

World of Bits, WebShop, SeeAct, WebVoyager, AutoWebGLM, and the surveys all expose evaluation problems:

```text
offline vs online evaluation
fixed reference trajectories vs multiple valid solutions
simulated vs live websites
human evaluation vs automatic evaluation
success rate vs extraction correctness
safety and risk evaluation
cost/latency metrics
```

This motivates S5.1.

---

## 7. Refined thesis-ready synthesis paragraph

The evolution of web-agent systems shows a progression from early reinforcement-learning interfaces to modern LLM/LMM-powered agents operating on real websites and broader graphical user interfaces. World of Bits first framed the web as an open-domain interactive environment where agents observe pixels and DOM structures and act through keyboard and mouse events. Workflow-Guided Exploration and DOM-Q-NET then addressed two early bottlenecks of web RL: sparse-reward exploration and DOM-structured action grounding. WebGPT shifted the field toward LLM-based browsing by fine-tuning GPT-3 to search, navigate, quote evidence, and answer questions with human feedback. WebShop introduced scalable grounded web interaction through a simulated e-commerce environment with semantic actions and automatic rewards. More recent systems address the gap between simulated tasks and real websites. WebAgent combines planning, long HTML summarization, and program synthesis to act on real websites, while AutoWebGLM trains an open web-navigation model using simplified HTML, browsing traces, curriculum learning, reinforcement learning, and rejection sampling finetuning. Multimodal systems such as SeeAct and WebVoyager show that large multimodal models can reason over rendered webpages and perform live browser actions, but they also reveal that precise action grounding remains a major bottleneck. Broader GUI-agent systems such as Agent S and AutoGLM extend these ideas to desktop and mobile interfaces through hierarchical planning, memory, intermediate interfaces, and online curriculum learning. Finally, WALT suggests a future direction in which agents reverse-engineer website functionality into reusable tools, reducing reliance on brittle step-by-step UI actions. Together, these works show that web agents have become increasingly capable, but generalized web automation and data extraction still require robust DOM/visual grounding, long-horizon planning, safe execution, verified extraction, realistic evaluation, and deployment-aware action abstractions.

---

## 8. Refined limitations connected to the thesis

### 8.1 Low-level action limitation

Early systems such as World of Bits operate with low-level keyboard and mouse actions.

For generalized web automation, this matters because low-level control creates large action spaces and long trajectories. A data-extraction agent should not always reason at the level of pixels and mouse movements; it needs higher-level abstractions such as DOM elements, semantic actions, API calls, or tools.

### 8.2 Sparse reward and exploration limitation

Workflow-Guided Exploration shows that RL agents struggle when reward appears only after complete task success.

For web automation, this matters because many workflows have delayed success signals. A form may only fail at submission. A product search may only be wrong after comparison. An extraction may look correct but fail later verification.

### 8.3 DOM representation limitation

DOM-Q-NET shows that DOM structure helps, but simplified benchmark DOMs do not fully capture real websites.

For generalized automation, this matters because real DOMs are long, noisy, dynamic, and often disconnected from the visible human interface.

### 8.4 Text-browser limitation

WebGPT shows that LLMs can browse textually and cite evidence, but text browsing is not full browser automation.

For the thesis, this matters because data extraction and web automation often require forms, dropdowns, dynamic widgets, tables, visual layout, authentication, and structured outputs.

### 8.5 Simulated benchmark limitation

WebShop provides scalable grounded evaluation, but it remains a simulated e-commerce environment.

For generalized automation, this matters because real websites are multi-domain, dynamic, and often not reproducible.

### 8.6 Long HTML limitation

WebAgent and AutoWebGLM show that real HTML can exceed model context limits and contain large amounts of irrelevant content.

For web extraction, this matters directly because the agent must compress the page without removing relevant evidence.

### 8.7 Program synthesis limitation

WebAgent uses generated Python programs to act on websites.

For deployment, this matters because generated code can be powerful but risky. It must be sandboxed, constrained, inspected, or verified before execution.

### 8.8 Grounding limitation

SeeAct shows the gap between action generation and action grounding.

For generalized web automation, this is central. The agent may know what to do but fail to select the correct element, operation, or input value.

### 8.9 Live-web reliability limitation

WebVoyager shows that live multimodal agents fail through navigation loops, visual grounding issues, hallucination, and prompt misalignment.

For the thesis, these failures motivate a dedicated failure-mode analysis.

### 8.10 Training-data limitation

AutoWebGLM shows the importance of high-quality web-browsing traces.

For web agents, this matters because collecting representative trajectories across websites, languages, tasks, and failure cases is expensive.

### 8.11 Planning-grounding separation limitation

AutoGLM argues that planning and grounding require separate optimization.

For web agents, this matters because flexible reasoning and precise UI control are different abilities. A single prompt or model may not optimize both well.

### 8.12 Memory limitation

Agent S shows the value of narrative and episodic memory, but memory can also be stale, irrelevant, or wrong.

For web automation, memory must be evidence-grounded and verified, especially when websites change.

### 8.13 Tool-maintenance limitation

WALT shows that learned website tools can reduce brittle UI steps.

However, for deployment, tools must be discovered, validated, updated, and monitored as websites change. This creates a new maintenance problem.

### 8.14 Survey limitation

The GUI-agent and WebAgent surveys provide useful taxonomies, but they do not replace primary system papers.

For thesis writing, use surveys to structure the field and primary papers to support technical and empirical claims.

---

## 9. Updated cross-links to later sections

| Paper | Feeds |
|---|---|
| World of Bits | S5.1 benchmarks, S5.2 DOM/pixel grounding, S5.4 RL/behavioral cloning, S5.5 sparse-reward failures, S8 reproducibility |
| Workflow-Guided Exploration | S5.3 exploration/planning, S5.4 demonstrations/RL, S5.5 sparse rewards and overfitting |
| DOM-Q-NET | S5.2 DOM representation, S5.4 RL/multitask learning, S5.5 large variable action spaces |
| WebGPT | S5.4 human feedback, S6 web QA/extraction, S7 references/truthfulness, S8 live web access risk |
| WebShop | S5.1 scalable benchmark design, S5.3 search/exploration/planning, S5.4 imitation/RL, S8 sim-to-real |
| WebAgent | S5.2 long HTML summarization, S5.3 sub-instruction planning, S5.4 self-experience, S6 programmatic extraction, S8 real-web deployment |
| SeeAct | S5.1 offline vs online evaluation, S5.2 visual/HTML grounding, S5.3 action generation, S5.5 grounding failures, S7 safety |
| WebVoyager | S5.1 online evaluation, S5.2 multimodal perception, S5.3 end-to-end planning, S5.5 navigation/grounding/hallucination failures, S8 deployment |
| AutoWebGLM, KDD 2024 | S5.1 AutoWebBench, S5.2 HTML simplification, S5.3 task decomposition, S5.4 curriculum/RL/RFT, S5.5 loop/self-check failures, S8 browser extension |
| Agent S, ICLR 2025 Poster | S5.2 GUI grounding, S5.3 hierarchical planning, S5.4 memory/experience, S5.5 GUI failures, S8 cross-platform computer use |
| AutoGLM, arXiv preprint | S5.2 intermediate interface/grounding, S5.3 planning, S5.4 online curriculum RL, S5.5 error recovery, S8 deployable foundation agents |
| GUI-agent surveys, prefer TMLR 2025 + ACL Findings 2025 versions | S5.1 evaluation, S5.2 perception, S5.3 planning/action, S5.4 data/models, S5.5 limitations, S8 roadmap |
| WebAgents survey, KDD 2025 Tutorial & Survey Track | S5.1 evaluation, S5.2 perception, S5.3 planning/reasoning/execution, S5.4 training, S7 trustworthiness |
| WALT, ICLR 2026 Poster | S5.2 action/tool abstraction, S5.3 tool-based planning, S5.4 tool learning, S5.5 brittle UI-action failures, S6 extraction tools, S8 maintenance |

---

## 10. How S4 should be written in the thesis

A strong final thesis section for S4 can be organized into six subsections:

### S4.1 Pre-LLM web agents: web as an RL environment

Use:

```text
World of Bits
Workflow-Guided Exploration
DOM-Q-NET
```

Main argument:

```text
Before LLMs, web agents were treated as RL agents in browser environments, but sparse rewards, low-level actions, and DOM grounding made generalization difficult.
```

### S4.2 LLM browsing and evidence-grounded web QA

Use:

```text
WebGPT
```

Main argument:

```text
LLMs introduced stronger language reasoning and evidence-gathering ability, but text-based browsing remained narrower than full web automation.
```

### S4.3 Scalable grounded interaction benchmarks

Use:

```text
WebShop
```

Main argument:

```text
WebShop made web-agent evaluation scalable through realistic product data, semantic actions, and automatic rewards, but remained simulated and domain-specific.
```

### S4.4 Real-world LLM web agents

Use:

```text
WebAgent
AutoWebGLM, final KDD 2024 version
```

Main argument:

```text
Real websites require long HTML handling, observation simplification, task decomposition, program synthesis, trajectory data, and web-specific training.
```

### S4.5 Multimodal live-web agents

Use:

```text
SeeAct
WebVoyager
```

Main argument:

```text
LMMs improve visual web understanding, but reliable browser control depends on precise grounding and robust online evaluation.
```

### S4.6 From web agents to GUI/foundation/tool agents

Use:

```text
Agent S, ICLR 2025
AutoGLM, arXiv preprint
WALT, ICLR 2026
GUI-agent surveys, prefer TMLR 2025 and ACL Findings 2025 versions
WebAgents survey, KDD 2025 Tutorial & Survey Track
```

Main argument:

```text
Web automation is becoming part of a broader GUI-agent and computer-use-agent paradigm, where planning, grounding, memory, action abstraction, trustworthiness, and deployment become central.
```

---

## 11. Final refined S4 synthesis

S4 establishes the evolution of web-agent systems from early RL-based browser environments to modern LLM/LMM-powered agents and emerging tool-based automation. Early systems such as World of Bits, Workflow-Guided Exploration, and DOM-Q-NET framed the web as an interactive decision environment and showed that web automation is difficult because of sparse rewards, low-level actions, long trajectories, and DOM grounding. WebGPT shifted the field toward LLM-based browsing, where a model can search, navigate, quote evidence, and answer questions with human feedback. WebShop then introduced a scalable grounded web-interaction benchmark with semantic actions, realistic e-commerce data, and automatic rewards.

Later systems move closer to real-world web automation. WebAgent addresses real websites through planning, long HTML summarization, and program synthesis. AutoWebGLM shows that trained open LLMs can become competitive web-navigation agents through HTML simplification, browsing traces, curriculum learning, reinforcement learning, and rejection sampling finetuning. SeeAct and WebVoyager introduce the multimodal live-web paradigm: agents use screenshots, visual reasoning, and labeled interactive elements to act on real websites. These systems show strong progress but also reveal the grounding bottleneck, navigation loops, hallucinations, and online evaluation difficulty.

The most recent direction broadens web agents into GUI and computer-use agents. Agent S and AutoGLM show that web automation shares core challenges with desktop and mobile automation: hierarchical planning, memory, intermediate interfaces, action grounding, and online learning. Peer-reviewed and final survey references, including TMLR 2025 LLM-Brained GUI Agents, Findings of ACL 2025 GUI Agents, and the KDD 2025 WebAgents survey, provide the broader taxonomy of perception, planning, action, training, evaluation, and trustworthiness. WALT suggests an important future direction: instead of relying only on fragile primitive UI actions, web agents can discover and invoke high-level website tools.

Overall, S4 shows that web agents have moved from controlled web tasks toward real, multimodal, trained, and tool-augmented systems. However, generalized web automation and data extraction remain unsolved. The main remaining challenges are robust DOM and visual grounding, long-horizon planning, state tracking, verified extraction, safe execution, realistic evaluation, privacy, latency, and maintainable action abstractions. This refined S4 synthesis therefore motivates S5: a technical decomposition of the components that determine web-agent success or failure—benchmarks, perception and grounding, planning, training, and failure modes.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S4\writing\S4_refined_synthesis_after_P1_updated_verified_with_central_gap.md

# S4 Refined Synthesis — Evolution of Web Agent Systems
## Updated after S4 P0 + S4 P1 papers

## Publication-status update for S4 P1 citations

The S4 narrative remains unchanged, but the final citation metadata should use the verified venue/status below:

| Paper | Final venue/status to use |
|---|---|
| Workflow-Guided Exploration | ICLR 2018 conference paper |
| DOM-Q-NET | ICLR 2019 conference paper |
| WebAgent | ICLR 2024 conference paper |
| Large Language Model Powered Agents in the Web | WWW 2024 Companion tutorial paper |
| AutoWebGLM Bootstrap and Reinforce | arXiv extended/preprint version; use KDD 2024 AutoWebGLM for final citation |
| Agent S | ICLR 2025 Poster |
| AutoGLM | arXiv preprint |
| Large Language Model-Brained GUI Agents preprint | arXiv preprint; use TMLR 2025 version for final citation |
| AutoWebGLM | KDD 2024 conference paper |
| GUI Agents with Foundation Models | arXiv preprint |
| A Survey on (M)LLM-Based GUI Agents | arXiv preprint |
| Large Language Model-Brained GUI Agents | TMLR 2025 |
| GUI Agents: A Survey | Findings of ACL 2025 |
| A Survey of WebAgents | KDD 2025 Tutorial & Survey Track |
| WALT | ICLR 2026 Poster |


## 1. What changed after adding S4 P1

The S4 P0 synthesis established the main historical arc:

```text
World of Bits
→ WebGPT
→ WebShop
→ SeeAct
→ WebVoyager
```

This gave the first web-agent progression:

```text
web as RL environment
→ text-based LLM browsing
→ scalable grounded web interaction
→ multimodal grounding
→ end-to-end live multimodal web automation
```

After adding the S4 P1 papers, the section becomes broader and more technically complete. The refined S4 narrative is now:

```text
World of Bits
→ Workflow-Guided Exploration
→ DOM-Q-NET
→ WebGPT
→ WebShop
→ WebAgent
→ SeeAct
→ WebVoyager
→ AutoWebGLM
→ Agent S / AutoGLM
→ WALT
→ WebAgent and GUI-agent surveys
```

Conceptually, this means S4 is no longer only a chronological history of web agents. It becomes a full evolution from:

```text
low-level RL browser control
→ DOM-aware RL
→ LLM browsing
→ simulated grounded web interaction
→ real-world HTML-specialized agents
→ multimodal live-web agents
→ trained/deployable web agents
→ general GUI/computer-use agents
→ tool-based web automation
```

The P1 papers add five important refinements:

1. **Pre-LLM web agents were already struggling with exploration and grounding.**  
   Workflow-Guided Exploration and DOM-Q-NET show that sparse rewards, low-level actions, and DOM representation were central problems before LLMs.

2. **Real-world websites require long HTML handling and open-ended action generation.**  
   WebAgent shows that simulated websites are too simple compared with real websites, where HTML is long, messy, dynamic, and task-irrelevant.

3. **Training and bootstrapping matter, not only prompting.**  
   The final KDD 2024 AutoWebGLM paper shows that smaller open models can become competitive web-navigation agents through HTML simplification, trajectory data, curriculum learning, RL, and rejection sampling finetuning.

4. **Web agents are part of a broader GUI-agent and computer-use-agent movement.**  
   Agent S (ICLR 2025), AutoGLM, and GUI-agent surveys show that web automation shares core problems with mobile and desktop automation: perception, grounding, planning, memory, action execution, and safety.

5. **The next direction is action abstraction and tool learning.**  
   WALT (ICLR 2026) shifts web automation away from fragile primitive UI actions toward discovered website-level tools such as `search`, `filter`, `sort`, `create`, `edit`, and `delete`.

---

## 2. Refined S4 narrative

Section S4 explains how web-agent systems evolved from early reinforcement-learning environments to modern LLM/LMM-powered agents capable of interacting with real websites and broader graphical user interfaces.

The earliest stage is represented by **World of Bits**, **Workflow-Guided Exploration**, and **DOM-Q-NET**. These papers treat web automation as a sequential decision-making problem. The web page is an environment; the agent observes pixels, DOM structures, or HTML trees; and it acts through mouse, keyboard, click, or type actions. This pre-LLM stage is important because it identifies the core difficulties of web automation before modern LLMs: sparse rewards, large action spaces, long trajectories, demonstration dependence, weak exploration, and DOM grounding.

World of Bits establishes the web as an open-domain interactive environment. Workflow-Guided Exploration then addresses the sparse-reward problem by using demonstrations to induce high-level workflows that constrain exploration. DOM-Q-NET shifts attention to webpage structure by representing the DOM as a graph and learning grounded RL policies over DOM elements. Together, these papers show that web automation is not merely text processing. It requires environment perception, structural grounding, action selection, and sequential feedback.

The second stage begins with **WebGPT**. WebGPT shifts the field from RL web-interface control to LLM-based browsing. Instead of controlling a full browser visually, GPT-3 is fine-tuned to use a text-based browser with commands such as search, click, find, quote, scroll, and end. WebGPT is important because it shows that LLMs can use the web as an external information source and can collect references to support final answers. However, it remains a browser-assisted question-answering system, not a general web automation system. It does not handle visual layout, forms, dynamic pages, DOM-level action grounding, or structured extraction.

The third stage is represented by **WebShop**. WebShop introduces a scalable simulated e-commerce environment where agents follow natural-language shopping instructions, search products, inspect results, choose options, and make purchases. It abstracts away raw mouse and keyboard actions into semantic actions such as `search[query]` and `choose[item]`. WebShop is important because it connects language grounding, product search, exploration, comparison, backtracking, memory, and automatic reward computation. However, it remains domain-specific and simulated.

The fourth stage is real-world LLM web automation, represented strongly by **WebAgent** and **AutoWebGLM**. WebAgent argues that real websites are much harder than simulated ones because they have open-ended actions, long messy HTML, and no predefined action space. It uses HTML-T5 for planning and HTML summarization, and Flan-U-PaLM for grounded program synthesis. The final KDD 2024 AutoWebGLM paper takes a different but related direction: it builds a trained web-navigation agent on ChatGLM3-6B using HTML simplification, human-AI trajectory data, curriculum learning, reinforcement learning, and rejection sampling finetuning. These papers show that real-world web automation requires specialized observation processing, training data, task decomposition, and self-improvement.

The fifth stage is multimodal and live-web automation, represented by **SeeAct** and **WebVoyager**. SeeAct separates web-agent behavior into action generation and action grounding. It shows that GPT-4V can produce strong high-level action plans, but automatic grounding into exact HTML elements and operations remains the main bottleneck. WebVoyager then builds an end-to-end multimodal web agent that operates on real websites using screenshots, labeled interactive elements, and ReAct-style step-by-step reasoning. Together, these papers show that multimodal models bring web agents closer to human-like browsing, but grounding, navigation loops, hallucination, and evaluation remain major barriers.

The sixth stage broadens web agents into **GUI and computer-use agents**. Agent S, published as an ICLR 2025 poster, uses experience-augmented hierarchical planning, online web knowledge, narrative memory, episodic memory, and an Agent-Computer Interface to operate computers like a human. AutoGLM develops foundation agents for web and mobile GUIs and emphasizes the separation of planning and grounding through an intermediate interface. GUI-agent surveys then place web agents inside a larger automation landscape that includes web browsers, mobile apps, desktop software, cross-platform environments, and large action models. This matters because generalized web automation is part of a broader shift from chatbots to agents that control digital interfaces.

The final forward-looking stage is **WALT**, which argues that web agents should not always rely on brittle step-by-step UI interactions. Instead, they can reverse-engineer website-provided functionality into reusable tools, such as `search`, `filter`, `sort`, `create`, `edit`, `delete`, `comment`, and `upvote`. This suggests a next-generation direction for web automation: combining LLM planning with website-specific tool discovery and validated high-level action abstractions.

---

## 3. Refined S4 architecture/evolution stack

| Stage | Main papers | Main contribution | What it adds to S4 |
|---|---|---|---|
| Web as environment | World of Bits | Webpages as interactive environments with pixels, DOM, rewards, keyboard/mouse actions | Historical foundation |
| Workflow-guided RL | Workflow-Guided Exploration | Demonstrations induce workflows to constrain sparse-reward exploration | Demonstration-guided web RL |
| DOM-aware RL | DOM-Q-NET | Graph neural network over DOM trees and factorized Q-functions | Structured DOM grounding |
| LLM text browsing | WebGPT | GPT-3 uses a text browser, quotes evidence, and learns from human feedback | LLM-based web evidence gathering |
| Grounded simulated web interaction | WebShop | Scalable e-commerce benchmark with semantic actions and automatic rewards | Language-grounded web task benchmark |
| Real-world HTML-specialized agent | WebAgent | Long HTML summarization, task decomposition, Python program synthesis | Real-web HTML and open-ended actions |
| Multimodal grounding | SeeAct | Separates action generation from action grounding; identifies grounding bottleneck | Visual/HTML grounding diagnosis |
| Live multimodal web agent | WebVoyager | End-to-end LMM agent on real websites with screenshots and labeled elements | Live-web multimodal automation |
| Trained web-navigation agent | AutoWebGLM, KDD 2024 | HTML simplification, browsing traces, curriculum learning, RL, RFT, AutoWebBench | Open trained deployable web agent |
| Computer-use GUI agent | Agent S, ICLR 2025 Poster | Hierarchical planning, web knowledge, narrative/episodic memory, ACI | Cross-application GUI automation |
| Foundation GUI agent | AutoGLM, arXiv preprint | Intermediate interface, planning-grounding separation, online curriculum RL | Deployable GUI foundation agents |
| Tool-based web automation | WALT, ICLR 2026 Poster | Reverse-engineers website functionality into reusable tools | Future direction beyond primitive UI steps |
| Survey/taxonomy layer | TMLR 2025 GUI survey, ACL 2025 GUI survey, KDD 2025 WebAgents survey | Architecture, training, evaluation, trustworthiness, roadmap | Organizes S5 and S7/S8 |

---

## 4. Refined conceptual contribution of S4

The central contribution of S4 is to show that **web agents evolved through successive abstractions of the web interface**.

The interface abstraction changes over time:

```text
pixels + mouse/keyboard
→ DOM and HTML structure
→ text browser commands
→ semantic actions
→ programmatic browser actions
→ screenshots + labeled elements
→ simplified HTML + trained action models
→ intermediate GUI interfaces
→ learned website tools
```

This is the key S4 idea:

```text
Progress in web agents is progress in representing, grounding, and abstracting interaction with the web.
```

Early RL agents struggled because the web interface was too large and sparse at the pixel/mouse level. DOM-aware agents improved grounding by using webpage structure. LLM browsing improved language reasoning and evidence gathering. WebShop improved scalable grounded evaluation through semantic actions. WebAgent and AutoWebGLM improved real-web handling through HTML simplification, long-context processing, program synthesis, and training. SeeAct and WebVoyager improved multimodal perception but exposed the grounding bottleneck. Agent S and AutoGLM generalized web automation to computer-use and GUI foundation agents. WALT suggests that future agents may automate websites by discovering reliable high-level tools rather than repeatedly reasoning over primitive clicks.

---

## 5. Refined gap after S4 P1

After S4 P0, the gap was:

```text
Web-agent systems have moved from controlled environments to live multimodal interaction, but the core unsolved problem is reliable grounding and verification across diverse, dynamic, real-world websites.
```

After adding S4 P1, the gap becomes more precise:

```text
Web agents have progressed from RL interface control to trained multimodal and tool-augmented systems, but generalized web automation still lacks robust cross-site grounding, long-horizon reliability, safe execution, verified extraction, and maintainable action abstractions.
```

S4 now shows that web agents can:

```text
operate in browser-like environments
use pixels, DOM, HTML, screenshots, and accessibility trees
browse textually and cite evidence
act semantically in simulated websites
summarize long HTML
generate Python automation programs
use multimodal visual understanding
train smaller open web-navigation models
use memory and hierarchical planning
control broader GUIs
learn or expose website tools
```

But they still do not fully solve:

```text
precise element grounding across arbitrary websites
visual-DOM alignment under dynamic layouts
long-horizon task reliability
safe irreversible action handling
robust verification of extracted data
evaluation beyond fixed trajectories
privacy and permission control
resistance to popups, CAPTCHAs, ads, and authentication
state tracking across multi-page workflows
maintenance when websites change
cost and latency under real deployment
```

Therefore, the refined S4 gap is:

```text
The field has developed increasingly powerful web-agent architectures, but the remaining bottleneck is making their perception, planning, action abstraction, and verification reliable enough for generalized real-world web automation and data extraction.
```

---

## 6. Thesis connection

For the thesis topic, **“LLM-based agents for generalized web automation and data extraction,”** S4 supports seven major claims.

### Claim 1 — Web automation is a sequential decision-making problem

World of Bits, Workflow-Guided Exploration, and DOM-Q-NET show that web automation is not just scraping or text extraction. It is an interactive decision problem:

```text
observe state → choose action → execute → observe new state → continue
```

This supports the thesis framing of web automation as an agentic problem.

### Claim 2 — DOM and interface representation are foundational

DOM-Q-NET, WebAgent, AutoWebGLM, SeeAct, and WebVoyager all show that the way the page is represented strongly determines agent success. Web agents may use:

```text
DOM trees
HTML snippets
simplified HTML
accessibility trees
screenshots
OCR
labeled UI elements
multimodal observations
```

This directly motivates S5.2.

### Claim 3 — LLMs improve instruction following and reasoning but do not remove grounding problems

WebGPT, WebShop, WebAgent, SeeAct, and WebVoyager show that LLMs/LMMs improve browsing, planning, and language grounding. However, SeeAct and WebVoyager show that a correct high-level plan can still fail if the agent cannot ground it into the correct element or operation.

### Claim 4 — Training and experience are needed for robust web agents

Workflow-Guided Exploration, WebAgent, AutoWebGLM, Agent S, and AutoGLM show that prompting alone is insufficient. Web agents benefit from:

```text
demonstrations
workflow constraints
self-experience
curriculum learning
reinforcement learning
rejection sampling finetuning
episodic memory
narrative memory
online learning
```

This motivates S5.4.

### Claim 5 — Generalized web automation is part of broader GUI automation

Agent S, AutoGLM, and the GUI-agent surveys show that web agents are one branch of a larger GUI-agent ecosystem. Many web challenges also appear in mobile and desktop agents:

```text
visual grounding
action abstraction
long-horizon planning
memory
safety
privacy
latency
cross-platform generalization
```

This helps broaden the thesis without losing the web-specific focus.

### Claim 6 — Future web agents may need tool abstraction, not only UI actions

WALT shows that repeatedly clicking and typing is brittle. A more reliable direction is to discover reusable site-level tools:

```text
search(query)
filter(criteria)
sort(order)
create(item)
edit(item)
delete(item)
comment(text)
```

This connects S4 back to S3 tool-use architectures and forward to S6 extraction tools and S8 deployment.

### Claim 7 — Evaluation remains unresolved

World of Bits, WebShop, SeeAct, WebVoyager, AutoWebGLM, and the surveys all expose evaluation problems:

```text
offline vs online evaluation
fixed reference trajectories vs multiple valid solutions
simulated vs live websites
human evaluation vs automatic evaluation
success rate vs extraction correctness
safety and risk evaluation
cost/latency metrics
```

This motivates S5.1.

---

## 7. Refined thesis-ready synthesis paragraph

The evolution of web-agent systems shows a progression from early reinforcement-learning interfaces to modern LLM/LMM-powered agents operating on real websites and broader graphical user interfaces. World of Bits first framed the web as an open-domain interactive environment where agents observe pixels and DOM structures and act through keyboard and mouse events. Workflow-Guided Exploration and DOM-Q-NET then addressed two early bottlenecks of web RL: sparse-reward exploration and DOM-structured action grounding. WebGPT shifted the field toward LLM-based browsing by fine-tuning GPT-3 to search, navigate, quote evidence, and answer questions with human feedback. WebShop introduced scalable grounded web interaction through a simulated e-commerce environment with semantic actions and automatic rewards. More recent systems address the gap between simulated tasks and real websites. WebAgent combines planning, long HTML summarization, and program synthesis to act on real websites, while AutoWebGLM trains an open web-navigation model using simplified HTML, browsing traces, curriculum learning, reinforcement learning, and rejection sampling finetuning. Multimodal systems such as SeeAct and WebVoyager show that large multimodal models can reason over rendered webpages and perform live browser actions, but they also reveal that precise action grounding remains a major bottleneck. Broader GUI-agent systems such as Agent S and AutoGLM extend these ideas to desktop and mobile interfaces through hierarchical planning, memory, intermediate interfaces, and online curriculum learning. Finally, WALT suggests a future direction in which agents reverse-engineer website functionality into reusable tools, reducing reliance on brittle step-by-step UI actions. Together, these works show that web agents have become increasingly capable, but generalized web automation and data extraction still require robust DOM/visual grounding, long-horizon planning, safe execution, verified extraction, realistic evaluation, and deployment-aware action abstractions.

---

## 8. Refined limitations connected to the thesis

### 8.1 Low-level action limitation

Early systems such as World of Bits operate with low-level keyboard and mouse actions.

For generalized web automation, this matters because low-level control creates large action spaces and long trajectories. A data-extraction agent should not always reason at the level of pixels and mouse movements; it needs higher-level abstractions such as DOM elements, semantic actions, API calls, or tools.

### 8.2 Sparse reward and exploration limitation

Workflow-Guided Exploration shows that RL agents struggle when reward appears only after complete task success.

For web automation, this matters because many workflows have delayed success signals. A form may only fail at submission. A product search may only be wrong after comparison. An extraction may look correct but fail later verification.

### 8.3 DOM representation limitation

DOM-Q-NET shows that DOM structure helps, but simplified benchmark DOMs do not fully capture real websites.

For generalized automation, this matters because real DOMs are long, noisy, dynamic, and often disconnected from the visible human interface.

### 8.4 Text-browser limitation

WebGPT shows that LLMs can browse textually and cite evidence, but text browsing is not full browser automation.

For the thesis, this matters because data extraction and web automation often require forms, dropdowns, dynamic widgets, tables, visual layout, authentication, and structured outputs.

### 8.5 Simulated benchmark limitation

WebShop provides scalable grounded evaluation, but it remains a simulated e-commerce environment.

For generalized automation, this matters because real websites are multi-domain, dynamic, and often not reproducible.

### 8.6 Long HTML limitation

WebAgent and AutoWebGLM show that real HTML can exceed model context limits and contain large amounts of irrelevant content.

For web extraction, this matters directly because the agent must compress the page without removing relevant evidence.

### 8.7 Program synthesis limitation

WebAgent uses generated Python programs to act on websites.

For deployment, this matters because generated code can be powerful but risky. It must be sandboxed, constrained, inspected, or verified before execution.

### 8.8 Grounding limitation

SeeAct shows the gap between action generation and action grounding.

For generalized web automation, this is central. The agent may know what to do but fail to select the correct element, operation, or input value.

### 8.9 Live-web reliability limitation

WebVoyager shows that live multimodal agents fail through navigation loops, visual grounding issues, hallucination, and prompt misalignment.

For the thesis, these failures motivate a dedicated failure-mode analysis.

### 8.10 Training-data limitation

AutoWebGLM shows the importance of high-quality web-browsing traces.

For web agents, this matters because collecting representative trajectories across websites, languages, tasks, and failure cases is expensive.

### 8.11 Planning-grounding separation limitation

AutoGLM argues that planning and grounding require separate optimization.

For web agents, this matters because flexible reasoning and precise UI control are different abilities. A single prompt or model may not optimize both well.

### 8.12 Memory limitation

Agent S shows the value of narrative and episodic memory, but memory can also be stale, irrelevant, or wrong.

For web automation, memory must be evidence-grounded and verified, especially when websites change.

### 8.13 Tool-maintenance limitation

WALT shows that learned website tools can reduce brittle UI steps.

However, for deployment, tools must be discovered, validated, updated, and monitored as websites change. This creates a new maintenance problem.

### 8.14 Survey limitation

The GUI-agent and WebAgent surveys provide useful taxonomies, but they do not replace primary system papers.

For thesis writing, use surveys to structure the field and primary papers to support technical and empirical claims.

---

## 9. Updated cross-links to later sections

| Paper | Feeds |
|---|---|
| World of Bits | S5.1 benchmarks, S5.2 DOM/pixel grounding, S5.4 RL/behavioral cloning, S5.5 sparse-reward failures, S8 reproducibility |
| Workflow-Guided Exploration | S5.3 exploration/planning, S5.4 demonstrations/RL, S5.5 sparse rewards and overfitting |
| DOM-Q-NET | S5.2 DOM representation, S5.4 RL/multitask learning, S5.5 large variable action spaces |
| WebGPT | S5.4 human feedback, S6 web QA/extraction, S7 references/truthfulness, S8 live web access risk |
| WebShop | S5.1 scalable benchmark design, S5.3 search/exploration/planning, S5.4 imitation/RL, S8 sim-to-real |
| WebAgent | S5.2 long HTML summarization, S5.3 sub-instruction planning, S5.4 self-experience, S6 programmatic extraction, S8 real-web deployment |
| SeeAct | S5.1 offline vs online evaluation, S5.2 visual/HTML grounding, S5.3 action generation, S5.5 grounding failures, S7 safety |
| WebVoyager | S5.1 online evaluation, S5.2 multimodal perception, S5.3 end-to-end planning, S5.5 navigation/grounding/hallucination failures, S8 deployment |
| AutoWebGLM, KDD 2024 | S5.1 AutoWebBench, S5.2 HTML simplification, S5.3 task decomposition, S5.4 curriculum/RL/RFT, S5.5 loop/self-check failures, S8 browser extension |
| Agent S, ICLR 2025 Poster | S5.2 GUI grounding, S5.3 hierarchical planning, S5.4 memory/experience, S5.5 GUI failures, S8 cross-platform computer use |
| AutoGLM, arXiv preprint | S5.2 intermediate interface/grounding, S5.3 planning, S5.4 online curriculum RL, S5.5 error recovery, S8 deployable foundation agents |
| GUI-agent surveys, prefer TMLR 2025 + ACL Findings 2025 versions | S5.1 evaluation, S5.2 perception, S5.3 planning/action, S5.4 data/models, S5.5 limitations, S8 roadmap |
| WebAgents survey, KDD 2025 Tutorial & Survey Track | S5.1 evaluation, S5.2 perception, S5.3 planning/reasoning/execution, S5.4 training, S7 trustworthiness |
| WALT, ICLR 2026 Poster | S5.2 action/tool abstraction, S5.3 tool-based planning, S5.4 tool learning, S5.5 brittle UI-action failures, S6 extraction tools, S8 maintenance |

---

## 10. How S4 should be written in the thesis

A strong final thesis section for S4 can be organized into six subsections:

### S4.1 Pre-LLM web agents: web as an RL environment

Use:

```text
World of Bits
Workflow-Guided Exploration
DOM-Q-NET
```

Main argument:

```text
Before LLMs, web agents were treated as RL agents in browser environments, but sparse rewards, low-level actions, and DOM grounding made generalization difficult.
```

### S4.2 LLM browsing and evidence-grounded web QA

Use:

```text
WebGPT
```

Main argument:

```text
LLMs introduced stronger language reasoning and evidence-gathering ability, but text-based browsing remained narrower than full web automation.
```

### S4.3 Scalable grounded interaction benchmarks

Use:

```text
WebShop
```

Main argument:

```text
WebShop made web-agent evaluation scalable through realistic product data, semantic actions, and automatic rewards, but remained simulated and domain-specific.
```

### S4.4 Real-world LLM web agents

Use:

```text
WebAgent
AutoWebGLM, final KDD 2024 version
```

Main argument:

```text
Real websites require long HTML handling, observation simplification, task decomposition, program synthesis, trajectory data, and web-specific training.
```

### S4.5 Multimodal live-web agents

Use:

```text
SeeAct
WebVoyager
```

Main argument:

```text
LMMs improve visual web understanding, but reliable browser control depends on precise grounding and robust online evaluation.
```

### S4.6 From web agents to GUI/foundation/tool agents

Use:

```text
Agent S, ICLR 2025
AutoGLM, arXiv preprint
WALT, ICLR 2026
GUI-agent surveys, prefer TMLR 2025 and ACL Findings 2025 versions
WebAgents survey, KDD 2025 Tutorial & Survey Track
```

Main argument:

```text
Web automation is becoming part of a broader GUI-agent and computer-use-agent paradigm, where planning, grounding, memory, action abstraction, trustworthiness, and deployment become central.
```

---



## The central S4 gap

Despite rapid progress from **World of Bits** to **WebVoyager**, no system in S4 solves all of the following together:

```text
reliable DOM grounding
+ live-web generalization
+ structured extraction
+ safe deployment
+ cost efficiency
```

This is the central S4 gap. It explains why the literature must move from a chronological evolution of web-agent systems to a technical decomposition of the remaining bottlenecks. Therefore, S5 should analyze the core components that determine whether LLM-based web agents succeed or fail: benchmarks and evaluation, perception and grounding, planning and decision-making, training and generalization, and failure modes.

---

## 11. Final refined S4 synthesis

S4 establishes the evolution of web-agent systems from early RL-based browser environments to modern LLM/LMM-powered agents and emerging tool-based automation. Early systems such as World of Bits, Workflow-Guided Exploration, and DOM-Q-NET framed the web as an interactive decision environment and showed that web automation is difficult because of sparse rewards, low-level actions, long trajectories, and DOM grounding. WebGPT shifted the field toward LLM-based browsing, where a model can search, navigate, quote evidence, and answer questions with human feedback. WebShop then introduced a scalable grounded web-interaction benchmark with semantic actions, realistic e-commerce data, and automatic rewards.

Later systems move closer to real-world web automation. WebAgent addresses real websites through planning, long HTML summarization, and program synthesis. AutoWebGLM shows that trained open LLMs can become competitive web-navigation agents through HTML simplification, browsing traces, curriculum learning, reinforcement learning, and rejection sampling finetuning. SeeAct and WebVoyager introduce the multimodal live-web paradigm: agents use screenshots, visual reasoning, and labeled interactive elements to act on real websites. These systems show strong progress but also reveal the grounding bottleneck, navigation loops, hallucinations, and online evaluation difficulty.

The most recent direction broadens web agents into GUI and computer-use agents. Agent S and AutoGLM show that web automation shares core challenges with desktop and mobile automation: hierarchical planning, memory, intermediate interfaces, action grounding, and online learning. Peer-reviewed and final survey references, including TMLR 2025 LLM-Brained GUI Agents, Findings of ACL 2025 GUI Agents, and the KDD 2025 WebAgents survey, provide the broader taxonomy of perception, planning, action, training, evaluation, and trustworthiness. WALT suggests an important future direction: instead of relying only on fragile primitive UI actions, web agents can discover and invoke high-level website tools.

Overall, S4 shows that web agents have moved from controlled web tasks toward real, multimodal, trained, and tool-augmented systems. However, generalized web automation and data extraction remain unsolved. The main remaining challenges are robust DOM and visual grounding, long-horizon planning, state tracking, verified extraction, safe execution, realistic evaluation, privacy, latency, and maintainable action abstractions. This refined S4 synthesis therefore motivates S5: a technical decomposition of the components that determine web-agent success or failure—benchmarks, perception and grounding, planning, training, and failure modes.


---


Total files merged: 46
