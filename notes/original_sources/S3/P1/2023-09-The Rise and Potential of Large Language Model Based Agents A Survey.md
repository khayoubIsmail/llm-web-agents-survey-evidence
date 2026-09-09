# Paper 74 — The Rise and Potential of Large Language Model Based Agents: A Survey

## Metadata

- **Title:** The Rise and Potential of Large Language Model Based Agents: A Survey
- **Authors:** Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang, Junzhe Wang, Senjie Jin, Enyu Zhou, Rui Zheng, Xiaoran Fan, Xiao Wang, Limao Xiong, Yuhao Zhou, Weiran Wang, Changhao Jiang, Yicheng Zou, Xiangyang Liu, Zhangyue Yin, Shihan Dou, Rongxiang Weng, Wensen Cheng, Qi Zhang, Wenjuan Qin, Yongyan Zheng, Xipeng Qiu, Xuanjing Huang, Tao Gui
- **Year:** 2023
- **Latest arXiv version in uploaded PDF:** 2023
- **Venue:** arXiv survey / Fudan NLP Group
- **DOI:** 10.48550/arXiv.2309.07864
- **arXiv ID:** arXiv:2309.07864
- **Thesis section:** S3 — LLM Agent Architectures
- **Cross-links:** S5.1 — Evaluation; S5.2 — Perception; S5.3 — Planning; S5.4 — Memory/Generalization; S5.5 — Failure Modes; S7 — Risks; S8 — Open Challenges
- **Category:** SUR / AGENT SURVEY / TAXONOMY
- **Paper type:** Survey / taxonomy / conceptual framework
- **Priority:** P1
- **BibTeX key:** xi2023rise

---

## Simple understanding

This paper is a broad survey of **LLM-based agents**.

It starts from the general concept of agents, then explains why LLMs are suitable as the “brain” of agents. It proposes a general framework with three main parts:

```text
brain → perception → action
```

The **brain** includes natural language interaction, knowledge, memory, reasoning, planning, transferability, and generalization.

The **perception** module expands the input space beyond text, including visual, auditory, and other modalities.

The **action** module expands the output space beyond text, including tool use and embodied action.

For my thesis, this paper is important because it provides a broad taxonomy for LLM agents and helps position web agents as one application area inside the larger agent literature.

---

## Notes

- **Core idea:**
  Surveys LLM-based agents and proposes a general conceptual framework composed of brain, perception, and action modules.

- **Key finding:**
  The survey argues that LLMs are suitable foundations for agents because they provide natural language interaction, knowledge, memory, reasoning, planning, transferability, generalization, and social ability. It organizes agent applications into single-agent systems, multi-agent systems, human-agent cooperation, and agent societies.

- **Limitation:**
  The survey is broad rather than web-specific.
  For web agents, this matters because it provides useful general categories but does not deeply analyze DOM grounding, browser automation, web extraction benchmarks, anti-bot constraints, or deployment issues specific to the web.

- **Additional limitation:**
  The brain-perception-action framework is high-level.
  For web agents, this matters because each component must be concretized into technical mechanisms: DOM parsing, screenshot encoding, click actions, form filling, extraction schemas, memory retrieval, and validation.

- **Additional limitation:**
  The survey covers many applications, including agent societies, which are not central to my thesis.
  For web automation, the useful parts are mainly construction, perception/action expansion, reasoning/planning, evaluation, and risks.

- **Additional limitation:**
  The survey identifies security and trustworthiness risks but does not provide concrete mitigation mechanisms for browser agents.
  For web agents, this matters because autonomous web actions can cause privacy leaks, harmful scraping, wrong submissions, or unauthorized operations.

- **Additional limitation:**
  The survey emphasizes potential and breadth.
  For web agents, this matters because my thesis should also emphasize practical bottlenecks: robustness, verification, long-horizon reliability, grounding, latency, and cost.

- **Connects to:**
  CoALA, autonomous agent surveys, ReAct, Reflexion, Toolformer, MRKL, web agents, multi-agent systems, human-agent collaboration, and agent safety literature.

- **Use in thesis:**
  Use this survey as a high-level taxonomy of LLM-based agents. It is useful for defining the components of an LLM agent and for positioning web automation within the broader agent landscape.

- **BibTeX key:**
  xi2023rise

---

## Thesis-ready paragraph

Xi et al. provide a comprehensive survey of large language model based agents, framing them as systems composed of a brain, perception module, and action module. In this framework, the LLM-based brain supports natural language interaction, knowledge use, memory, reasoning, planning, transferability, and generalization; perception expands the agent’s input space beyond text; and action expands the output space through tools and embodied behavior. This taxonomy is useful for situating web agents within the broader LLM-agent literature: a web agent must perceive web environments, reason and plan through an LLM-centered brain, and act through browser operations or tools. However, the survey is broad and not web-specific. It does not deeply address the technical problems that dominate generalized web automation and data extraction, such as DOM grounding, visual UI representation, structured extraction, action verification, anti-loop mechanisms, privacy constraints, and deployment cost. Therefore, the survey provides a high-level conceptual map, while later web-specific sections must analyze concrete architectures, benchmarks, and failure modes.

---

## Why this paper matters for my thesis

This paper matters because it helps define what an LLM-based agent is.

The survey says an agent can be understood through:

```text
brain
perception
action
```

For my thesis, this maps naturally to web automation:

```text
Brain:
LLM reasoning, planning, memory, task understanding

Perception:
HTML, DOM, screenshots, page text, browser state, documents

Action:
click, type, scroll, search, call APIs, extract data, submit forms
```

This gives a clean way to introduce web agents later.

The paper also helps distinguish a web agent from a chatbot:

```text
chatbot = mostly text input → text output
web agent = environment perception → decision-making → external action → feedback
```

---

## Important concepts to remember

### 1. Agent

The paper follows the AI view of an agent as an entity that:

```text
perceives its environment
makes decisions
takes actions
```

For web automation:

```text
environment = website/browser
perception = DOM/screenshot/page text
decision = choose action or extraction step
action = browser/tool operation
```

### 2. Brain

The brain is the controller of the agent.

It includes:

```text
natural language interaction
knowledge
memory
reasoning
planning
transferability
generalization
```

For web agents, this corresponds to the LLM-centered decision module.

### 3. Perception

Perception expands the agent’s input space.

The survey discusses:

```text
textual input
visual input
auditory input
other input
```

For web agents, the most important are:

```text
textual input: HTML, page text, DOM labels
visual input: screenshots, layout, icons, tables
```

### 4. Action

Action expands what the agent can do.

The survey discusses:

```text
textual output
tool use
embodied action
```

For web agents:

```text
tool use = search, browser, APIs
embodied action = clicking/typing/scrolling in the browser
```

### 5. Agent society

The paper also discusses multi-agent systems and agent societies.

For my thesis, this is background only unless I discuss multi-agent web automation.

### 6. Human-agent cooperation

The survey discusses instructor-executor and equal partnership paradigms.

For web agents, this matters when the system asks for clarification, permission, or human approval before risky actions.

---

## Key evidence from the paper

### Figure 1 — Envisioned agent society

Figure 1 shows agents acting in a simulated society with cooperation, tool use, planning, and human participation.

For the thesis, this is less central than web automation, but it helps illustrate the broad agent vision.

### Figure 2 — General framework of LLM-based agent

Figure 2 is the most important figure for my thesis.

It shows:

```text
environment → perception → brain → action → environment
```

The brain includes:

```text
memory
knowledge
decision making
planning/reasoning
```

The action module includes:

```text
text
tools
embodiment
```

This is directly useful for defining the basic structure of web agents.

### Figure 3 — Typology of the brain module

Figure 3 categorizes the brain module into:

```text
natural language interaction
knowledge
memory
reasoning and planning
transferability and generalization
```

This helps organize S3 and S5.

### Section 3 — Construction of LLM-based agents

Section 3 is the most relevant part for S3 because it explains how LLM agents are constructed.

### Section 6 — Discussion

Section 6 is useful for thesis gaps because it discusses evaluation, security, trustworthiness, scaling, and open problems.

---

## Connection to earlier and later papers

### Connection to S2 foundations

S2 explains the abilities of LLMs:

```text
language understanding
instruction following
reasoning
alignment
long-context
multimodality
```

This survey explains how those abilities are placed into an agent framework.

### Connection to ReAct

ReAct is an example of the action/feedback loop inside the action and brain modules.

### Connection to Reflexion

Reflexion is part of memory and planning/reflection.

### Connection to Toolformer and MRKL

Toolformer and MRKL are examples of tool-using action modules.

### Connection to CoALA

CoALA gives a more precise cognitive architecture vocabulary.

This survey gives a broader taxonomy:

```text
Xi et al. = broad agent landscape
CoALA = detailed cognitive architecture framework
```

### Connection to web agents

The survey positions web agents as a type of LLM-based agent with:

```text
digital environment
text/visual perception
tool/browser actions
planning and memory
```

---

## Connection to later thesis sections

- **S3 — LLM Agent Architectures:**
  Use this survey to introduce broad LLM-agent construction.

- **S5.1 — Web Agent Benchmarks and Evaluation:**
  The survey discusses agent evaluation dimensions such as utility, sociability, values, and continual evolution.

- **S5.2 — Perception, Grounding, and Interface Representation:**
  Its perception module supports the discussion of textual, visual, and multimodal inputs.

- **S5.3 — Planning and Decision-Making:**
  The brain module includes reasoning and planning.

- **S5.4 — Training Strategies and Generalization:**
  The brain module includes memory, transferability, generalization, and continual learning.

- **S5.5 — Limitations and Failure Modes:**
  Broad agent risks and failures feed into failure taxonomy.

- **S7 — Security, Robustness, and Trustworthiness:**
  The survey discusses adversarial robustness, trustworthiness, and risks.

- **S8 — Open Challenges and Deployment Realities:**
  The survey’s open problems help frame deployment challenges.

---

## Limitation connected to thesis

This survey gives a broad map, but it does not solve the specific technical problems of generalized web automation.

For my thesis, a web agent requires:

```text
browser environment perception
DOM and visual grounding
action execution
state tracking
task planning
structured extraction
verification
privacy/safety control
deployment reliability
```

The survey mainly gives:

```text
general agent taxonomy
high-level construction framework
broad application categories
open problems
```

Therefore, it should be used to position the thesis, not as direct evidence that web automation is solved.

---

## Reading decision

- **Read fully?** No, selective deep reading
- **Depth needed:** Medium-high
- **Main use:** Broad taxonomy and positioning
- **Most important parts:**
  - Abstract
  - Introduction
  - Figure 2
  - Figure 3
  - Section 3: construction of LLM-based agents
  - Section 3.1: brain
  - Section 3.2: perception
  - Section 3.3: action
  - Section 6.2: evaluation
  - Section 6.3: security/trustworthiness
  - Section 6.5: open problems

---

## One-sentence summary

This survey organizes LLM-based agents around brain, perception, and action modules, providing a broad taxonomy that helps position web agents, but it remains too general to address web-specific grounding, extraction, verification, and deployment challenges.

---

## BibTeX

```bibtex
@article{xi2023rise,
  title   = {The Rise and Potential of Large Language Model Based Agents: A Survey},
  author  = {Xi, Zhiheng and Chen, Wenxiang and Guo, Xin and He, Wei and Ding, Yiwen and Hong, Boyang and Zhang, Ming and Wang, Junzhe and Jin, Senjie and Zhou, Enyu and Zheng, Rui and Fan, Xiaoran and Wang, Xiao and Xiong, Limao and Zhou, Yuhao and Wang, Weiran and Jiang, Changhao and Zou, Yicheng and Liu, Xiangyang and Yin, Zhangyue and Dou, Shihan and Weng, Rongxiang and Cheng, Wensen and Zhang, Qi and Qin, Wenjuan and Zheng, Yongyan and Qiu, Xipeng and Huang, Xuanjing and Gui, Tao},
  journal = {arXiv preprint arXiv:2309.07864},
  year    = {2023},
  doi     = {10.48550/arXiv.2309.07864}
}
```

---

## Source links

- arXiv: https://arxiv.org/abs/2309.07864
- Repository: https://github.com/WooooDyy/LLM-Agent-Paper-List
