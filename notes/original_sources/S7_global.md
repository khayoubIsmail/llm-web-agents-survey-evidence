# S7 - Security, Robustness, and Trustworthiness

Generated on: 2026-05-07 23:40

---

## P1 (37 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\01 - Testing Language Model Agents Safely in the Wild.md

# Testing Language Model Agents Safely in the Wild

## Metadata

- **Short name:** AgentMonitor / Safe Testing in the Wild
- **Authors:** Silen Naihin, David Atkinson, Marc Green, Merwane Hamadi, Craig Swift, Douglas Schonholtz, Adam Tauman Kalai, David Bau
- **Year used for thesis:** 2023
- **Venue/status:** arXiv / OpenReview preprint; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** safe testing and monitoring
- **BibTeX key:** `naihin2023testingagentswild`
- **Source PDF file:** `2023-11-Testing Language Model Agents Safely in the Wild.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Proposes safe testing-in-the-wild for language model agents using a context-sensitive monitor that audits actions, enforces safety boundaries, stops unsafe tests, and logs suspicious behavior for human review.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Proposes safe testing-in-the-wild for language model agents using a context-sensitive monitor that audits actions, enforces safety boundaries, stops unsafe tests, and logs suspicious behavior for human review.

- **Key finding:**  
  AgentMonitor can identify and stop many unsafe situations in adversarial simulations and real AutoGPT tests, but the work also shows that monitoring open-ended internet agents remains difficult as agents and environments become more complex.

- **Limitation connected to thesis:**  
  It is a monitoring framework rather than a full web-agent security benchmark; it does not directly address modern multimodal web agents, prompt injection through DOM/screenshot channels, or structured extraction safety.

- **Connects to:**  
  S7.6 defenses/governance; S8 deployment; safe sandboxing; human review.

- **Use in thesis:**  
  foundational safety-monitoring framework for testing autonomous agents on the open internet

---

## Detailed notes

- Frames safe testing as a prerequisite for safe autonomy in the wild.
- Introduces safety boundaries and action auditing before execution.
- Uses an adversarial simulated agent to test monitor behavior.
- Applies monitoring to AutoGPT-style real-world tests.
- Highlights that unsafe behavior can emerge from agent-environment interactions rather than explicit malicious user prompts.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
safe testing and monitoring
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
foundational safety-monitoring framework for testing autonomous agents on the open internet
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
It is a monitoring framework rather than a full web-agent security benchmark; it does not directly address modern multimodal web agents, prompt injection through DOM/screenshot channels, or structured extraction safety.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

AgentMonitor / Safe Testing in the Wild contributes to S7 by showing that Proposes safe testing-in-the-wild for language model agents using a context-sensitive monitor that audits actions, enforces safety boundaries, stops unsafe tests, and logs suspicious behavior for human review. The main result is that AgentMonitor can identify and stop many unsafe situations in adversarial simulations and real AutoGPT tests, but the work also shows that monitoring open-ended internet agents remains difficult as agents and environments become more complex. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, It is a monitoring framework rather than a full web-agent security benchmark; it does not directly address modern multimodal web agents, prompt injection through DOM/screenshot channels, or structured extraction safety. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

AgentMonitor / Safe Testing in the Wild shows that **Proposes safe testing-in-the-wild for language model agents using a context-sensitive monitor that audits actions, enforces safety boundaries, stops unsafe tests, and logs suspicious behavior for human review**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{naihin2023testingagentswild,
  title   = {Testing Language Model Agents Safely in the Wild},
  author  = {Silen Naihin, David Atkinson, Marc Green, Merwane Hamadi, Craig Swift, Douglas Schonholtz, Adam Tauman Kalai, David Bau},
  journal = {arXiv / OpenReview preprint; no final peer-reviewed venue confirmed in this check},
  year    = {2023},
  url     = {https://arxiv.org/abs/2311.10538}
}
```

---

## Source links

- https://arxiv.org/abs/2311.10538


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\02 - AdvAgent- Controllable Blackbox Red-teaming on Web Agents.md

# AdvAgent: Controllable Blackbox Red-teaming on Web Agents

## Metadata

- **Short name:** AdvAgent
- **Authors:** Chejian Xu, Mintong Kang, Jiawei Zhang, Zeyi Liao, Lingbo Mo, Mengqi Yuan, Huan Sun, Bo Li
- **Year used for thesis:** 2024
- **Venue/status:** arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** black-box red-teaming
- **BibTeX key:** `xu2024advagent`
- **Source PDF file:** `2024-10-AdvAgent Controllable Blackbox Red-teaming on Web Agents.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Introduces a black-box red-teaming framework that trains an adversarial prompter with reinforcement learning feedback from the target web agent.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Introduces a black-box red-teaming framework that trains an adversarial prompter with reinforcement learning feedback from the target web agent.

- **Key finding:**  
  Adversarial prompts can be optimized to be stealthy, controllable, and effective against GPT-4-based web agents across diverse web tasks.

- **Limitation connected to thesis:**  
  It focuses on attack generation rather than defense; effectiveness depends on iterative access to the agent and task-specific feedback.

- **Connects to:**  
  EIA, WASP, RedTeamCUA, SecureWebArena, S5.5 reliability failures.

- **Use in thesis:**  
  controllable adversarial prompt generation for attacking web agents

---

## Detailed notes

- Black-box setting: no internal model parameters are assumed.
- Uses RL to optimize attacker prompts from feedback.
- Targets web agents with sensitive resources and autonomous action capability.
- Useful for systematic red-teaming because attacks can be controlled by desired goal.
- Shows that prompt-injection safety cannot be treated as only a static input-filtering problem.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
black-box red-teaming
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
controllable adversarial prompt generation for attacking web agents
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
It focuses on attack generation rather than defense; effectiveness depends on iterative access to the agent and task-specific feedback.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

AdvAgent contributes to S7 by showing that Introduces a black-box red-teaming framework that trains an adversarial prompter with reinforcement learning feedback from the target web agent. The main result is that Adversarial prompts can be optimized to be stealthy, controllable, and effective against GPT-4-based web agents across diverse web tasks. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, It focuses on attack generation rather than defense; effectiveness depends on iterative access to the agent and task-specific feedback. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

AdvAgent shows that **Introduces a black-box red-teaming framework that trains an adversarial prompter with reinforcement learning feedback from the target web agent**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{xu2024advagent,
  title   = {AdvAgent: Controllable Blackbox Red-teaming on Web Agents},
  author  = {Chejian Xu, Mintong Kang, Jiawei Zhang, Zeyi Liao, Lingbo Mo, Mengqi Yuan, Huan Sun, Bo Li},
  journal = {arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check},
  year    = {2024},
  url     = {https://arxiv.org/abs/2410.17401}
}
```

---

## Source links

- https://arxiv.org/abs/2410.17401


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\03 - Attacking Vision-Language Computer Agents via Pop-ups.md

# Attacking Vision-Language Computer Agents via Pop-ups

## Metadata

- **Short name:** Pop-up Attack
- **Authors:** Yanzhe Zhang, Tao Yu, Diyi Yang
- **Year used for thesis:** 2025
- **Venue/status:** ACL 2025 Long Papers
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** visual distraction / pop-up attack
- **BibTeX key:** `zhang2025popupattack`
- **Source PDF file:** `2024-11-Attacking Vision-Language Computer Agents via Pop-ups.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Shows that VLM agents can be manipulated by carefully designed pop-ups that humans would usually ignore, causing agents to click the pop-up instead of pursuing the task.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Shows that VLM agents can be manipulated by carefully designed pop-ups that humans would usually ignore, causing agents to click the pop-up instead of pursuing the task.

- **Key finding:**  
  Integrating adversarial pop-ups into OSWorld and VisualWebArena yields high attack success and large task-success degradation; simple defenses such as telling the agent to ignore pop-ups are ineffective.

- **Limitation connected to thesis:**  
  Pop-ups are only one visual manipulation channel; the paper does not fully solve defense or cover long-term memory, cross-site attacks, or full web-OS threat chains.

- **Connects to:**  
  S5.2 visual grounding, S5.5 failure modes, DECEPTICON, dark patterns, SecureWebArena.

- **Use in thesis:**  
  visual attack paper showing that VLM computer-use agents can be steered by adversarial pop-ups

---

## Detailed notes

- Targets agents that use screenshots as observations.
- Attack does not need to directly modify the model.
- Pop-ups exploit visual salience and task-relevant distraction.
- Demonstrates that VLM agents can be more credulous than humans toward UI artifacts.
- Provides an important bridge from perception/grounding to security.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
visual distraction / pop-up attack
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
visual attack paper showing that VLM computer-use agents can be steered by adversarial pop-ups
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Pop-ups are only one visual manipulation channel; the paper does not fully solve defense or cover long-term memory, cross-site attacks, or full web-OS threat chains.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

Pop-up Attack contributes to S7 by showing that Shows that VLM agents can be manipulated by carefully designed pop-ups that humans would usually ignore, causing agents to click the pop-up instead of pursuing the task. The main result is that Integrating adversarial pop-ups into OSWorld and VisualWebArena yields high attack success and large task-success degradation; simple defenses such as telling the agent to ignore pop-ups are ineffective. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Pop-ups are only one visual manipulation channel; the paper does not fully solve defense or cover long-term memory, cross-site attacks, or full web-OS threat chains. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

Pop-up Attack shows that **Shows that VLM agents can be manipulated by carefully designed pop-ups that humans would usually ignore, causing agents to click the pop-up instead of pursuing the task**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@inproceedings{zhang2025popupattack,
  title     = {Attacking Vision-Language Computer Agents via Pop-ups},
  author    = {Yanzhe Zhang, Tao Yu, Diyi Yang},
  booktitle = {ACL 2025 Long Papers},
  year      = {2025},
  url       = {https://aclanthology.org/2025.acl-long.411/}
}
```

---

## Source links

- https://aclanthology.org/2025.acl-long.411/


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\04 - WIPI- A New Web Threat for LLM-Driven Web Agents.md

# WIPI: A New Web Threat for LLM-Driven Web Agents

## Metadata

- **Short name:** WIPI
- **Authors:** Fangzhou Wu, Shutong Wu, Yulong Cao, Chaowei Xiao
- **Year used for thesis:** 2024
- **Venue/status:** arXiv preprint; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** early web indirect prompt injection
- **BibTeX key:** `wu2024wipi`
- **Source PDF file:** `2024-02 - WIPI- A New Web Threat for LLM-Driven Web Agents.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Introduces WIPI, where malicious instructions embedded in publicly accessible webpages indirectly control LLM-driven web agents.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Introduces WIPI, where malicious instructions embedded in publicly accessible webpages indirectly control LLM-driven web agents.

- **Key finding:**  
  Black-box web prompt injections can manipulate agents by exploiting their tendency to treat webpage content as actionable task context.

- **Limitation connected to thesis:**  
  Early threat model and evaluation are narrower than later live-web and multimodal benchmarks; defenses remain mostly conceptual.

- **Connects to:**  
  InjecAgent, EIA, WASP, WAInjectBench, WebAgentGuard.

- **Use in thesis:**  
  early paper introducing web indirect prompt injection against LLM-driven web agents

---

## Detailed notes

- Clarifies how web content becomes part of the agent prompt.
- Distinguishes LLM-web-agent threats from traditional web malware.
- Uses strategies such as instruction negligence and repeated malicious instructions.
- Important historically because it frames the web itself as an adversarial prompt surface.
- Feeds the thesis argument that browser agents inherit both LLM and web-security risks.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
early web indirect prompt injection
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
early paper introducing web indirect prompt injection against LLM-driven web agents
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Early threat model and evaluation are narrower than later live-web and multimodal benchmarks; defenses remain mostly conceptual.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

WIPI contributes to S7 by showing that Introduces WIPI, where malicious instructions embedded in publicly accessible webpages indirectly control LLM-driven web agents. The main result is that Black-box web prompt injections can manipulate agents by exploiting their tendency to treat webpage content as actionable task context. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Early threat model and evaluation are narrower than later live-web and multimodal benchmarks; defenses remain mostly conceptual. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

WIPI shows that **Introduces WIPI, where malicious instructions embedded in publicly accessible webpages indirectly control LLM-driven web agents**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{wu2024wipi,
  title   = {WIPI: A New Web Threat for LLM-Driven Web Agents},
  author  = {Fangzhou Wu, Shutong Wu, Yulong Cao, Chaowei Xiao},
  journal = {arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year    = {2024},
  url     = {https://arxiv.org/abs/2402.16965}
}
```

---

## Source links

- https://arxiv.org/abs/2402.16965


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\05 - AGENTPOISON- Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases.md

# AGENTPOISON: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases

## Metadata

- **Short name:** AgentPoison
- **Authors:** Zhaorun Chen, Zhen Xiang, Chaowei Xiao, Dawn Song, Bo Li
- **Year used for thesis:** 2024
- **Venue/status:** NeurIPS 2024 conference paper
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** memory / RAG knowledge-base poisoning
- **BibTeX key:** `chen2024agentpoison`
- **Source PDF file:** `2024-07 - AGENTPOISON- Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Proposes a backdoor attack against generic and RAG-based LLM agents by poisoning memory or knowledge bases so that triggered queries retrieve malicious demonstrations.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Proposes a backdoor attack against generic and RAG-based LLM agents by poisoning memory or knowledge bases so that triggered queries retrieve malicious demonstrations.

- **Key finding:**  
  AgentPoison achieves high attack success with very low poison rates and little benign-performance degradation across several agent types.

- **Limitation connected to thesis:**  
  It assumes the attacker can poison memory or knowledge bases directly, which is stronger than later environment-injected memory poisoning settings.

- **Connects to:**  
  Poison Once, Exploit Forever; RAG; memory agents; S7.3 systemic risks.

- **Use in thesis:**  
  systemic-risk paper for long-term memory and RAG-based agent poisoning

---

## Detailed notes

- Targets retrieval rather than only the immediate prompt.
- Optimizes triggers so malicious memories are retrieved when the trigger appears.
- Shows memory modules enlarge the attack surface beyond single-session instructions.
- Highly relevant to web agents that store trajectories, preferences, or browsing history.
- Supports the thesis claim that personalization creates persistent security risk.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
memory / RAG knowledge-base poisoning
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
systemic-risk paper for long-term memory and RAG-based agent poisoning
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
It assumes the attacker can poison memory or knowledge bases directly, which is stronger than later environment-injected memory poisoning settings.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

AgentPoison contributes to S7 by showing that Proposes a backdoor attack against generic and RAG-based LLM agents by poisoning memory or knowledge bases so that triggered queries retrieve malicious demonstrations. The main result is that AgentPoison achieves high attack success with very low poison rates and little benign-performance degradation across several agent types. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, It assumes the attacker can poison memory or knowledge bases directly, which is stronger than later environment-injected memory poisoning settings. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

AgentPoison shows that **Proposes a backdoor attack against generic and RAG-based LLM agents by poisoning memory or knowledge bases so that triggered queries retrieve malicious demonstrations**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@inproceedings{chen2024agentpoison,
  title     = {AGENTPOISON: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases},
  author    = {Zhaorun Chen, Zhen Xiang, Chaowei Xiao, Dawn Song, Bo Li},
  booktitle = {NeurIPS 2024},
  year      = {2024},
  url       = {https://papers.nips.cc/paper_files/paper/2024/hash/eb113910e9c3f6242541c1652e30dfd6-Abstract-Conference.html}
}
```

---

## Source links

- https://papers.nips.cc/paper_files/paper/2024/hash/eb113910e9c3f6242541c1652e30dfd6-Abstract-Conference.html


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\06 - InjecAgent- Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents.md

# InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents

## Metadata

- **Short name:** InjecAgent
- **Authors:** Qiusi Zhan, Zhixiang Liang, Zifan Ying, Daniel Kang
- **Year used for thesis:** 2024
- **Venue/status:** Findings of ACL 2024
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** tool-agent indirect prompt injection benchmark
- **BibTeX key:** `zhan2024injecagent`
- **Source PDF file:** `2024-03-InjecAgent Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Introduces a benchmark for IPI attacks against agents that use external tools, where malicious content processed by the agent causes harmful tool use or private data exfiltration.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Introduces a benchmark for IPI attacks against agents that use external tools, where malicious content processed by the agent causes harmful tool use or private data exfiltration.

- **Key finding:**  
  Tool-integrated agents remain vulnerable; ReAct-style GPT-4 agents can follow injected attacker instructions, and reinforced hacking prompts increase attack success.

- **Limitation connected to thesis:**  
  It is broader than web agents and less focused on visual/DOM browser interaction than later web-specific benchmarks.

- **Connects to:**  
  WIPI, WASP, WebAgentGuard, tool-use safety, S3 tool agents.

- **Use in thesis:**  
  benchmark for indirect prompt injection in tool-integrated agents

---

## Detailed notes

- Contains over one thousand test cases.
- Covers user tools and attacker tools.
- Categorizes attacks into direct harm and private-data exfiltration.
- Shows why tool access changes the risk profile of LLMs.
- Useful as a pre-web-agent benchmark foundation for S7.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
tool-agent indirect prompt injection benchmark
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
benchmark for indirect prompt injection in tool-integrated agents
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
It is broader than web agents and less focused on visual/DOM browser interaction than later web-specific benchmarks.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

InjecAgent contributes to S7 by showing that Introduces a benchmark for IPI attacks against agents that use external tools, where malicious content processed by the agent causes harmful tool use or private data exfiltration. The main result is that Tool-integrated agents remain vulnerable; ReAct-style GPT-4 agents can follow injected attacker instructions, and reinforced hacking prompts increase attack success. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, It is broader than web agents and less focused on visual/DOM browser interaction than later web-specific benchmarks. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

InjecAgent shows that **Introduces a benchmark for IPI attacks against agents that use external tools, where malicious content processed by the agent causes harmful tool use or private data exfiltration**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@inproceedings{zhan2024injecagent,
  title     = {InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents},
  author    = {Qiusi Zhan, Zhixiang Liang, Zifan Ying, Daniel Kang},
  booktitle = {Findings of ACL 2024},
  year      = {2024},
  url       = {https://aclanthology.org/2024.findings-acl.624/}
}
```

---

## Source links

- https://aclanthology.org/2024.findings-acl.624/


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\07 - Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents.md

# Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents

## Metadata

- **Short name:** BrowserART / Refusal-Trained Agents
- **Authors:** Priyanshu Kumar, Elaine Lau, Saranya Vijayakumar, Tu Trinh, Scale Red Team, Elaine Chang, Vaughn Robinson, Sean Hendryx, Shuyan Zhou, Matt Fredrikson, Summer Yue, Zifan Wang
- **Year used for thesis:** 2024
- **Venue/status:** arXiv preprint / ICLR 2025 related presentation; no main-conference final venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** refusal transfer failure
- **BibTeX key:** `kumar2024browserart`
- **Source PDF file:** `2024-10 - Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Tests whether refusal-trained chat LLMs remain refusal-trained when wrapped as browser agents with real actions.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Tests whether refusal-trained chat LLMs remain refusal-trained when wrapped as browser agents with real actions.

- **Key finding:**  
  Models that refuse harmful chat requests can attempt harmful browser-agent tasks; jailbreak methods from chat transfer to agent settings.

- **Limitation connected to thesis:**  
  Focuses on harmful user instructions rather than malicious webpages; it does not provide a complete defense architecture.

- **Connects to:**  
  SafeArena, ST-WebAgentBench, Instruction Hierarchy, policy hierarchy.

- **Use in thesis:**  
  shows chat-model refusal alignment does not transfer reliably to browser-agent settings

---

## Detailed notes

- Introduces BrowserART as a browser-agent red-teaming suite.
- Shows that agent scaffolding changes safety behavior.
- Highlights the gap between model-level refusal and system-level action control.
- Important for thesis because web agents can perform state-changing browser actions.
- Supports governance sections on action gating and policy compliance.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
refusal transfer failure
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
shows chat-model refusal alignment does not transfer reliably to browser-agent settings
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Focuses on harmful user instructions rather than malicious webpages; it does not provide a complete defense architecture.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

BrowserART / Refusal-Trained Agents contributes to S7 by showing that Tests whether refusal-trained chat LLMs remain refusal-trained when wrapped as browser agents with real actions. The main result is that Models that refuse harmful chat requests can attempt harmful browser-agent tasks; jailbreak methods from chat transfer to agent settings. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Focuses on harmful user instructions rather than malicious webpages; it does not provide a complete defense architecture. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

BrowserART / Refusal-Trained Agents shows that **Tests whether refusal-trained chat LLMs remain refusal-trained when wrapped as browser agents with real actions**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@inproceedings{kumar2024browserart,
  title     = {Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents},
  author    = {Priyanshu Kumar, Elaine Lau, Saranya Vijayakumar, Tu Trinh, Scale Red Team, Elaine Chang, Vaughn Robinson, Sean Hendryx, Shuyan Zhou, Matt Fredrikson, Summer Yue, Zifan Wang},
  booktitle = {arXiv preprint / ICLR 2025 related presentation; no main-conference final venue confirmed in this check},
  year      = {2024},
  url       = {https://arxiv.org/abs/2410.13886}
}
```

---

## Source links

- https://arxiv.org/abs/2410.13886


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\08 - The Instruction Hierarchy- Training LLMs to Prioritize Privileged Instructions.md

# The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions

## Metadata

- **Short name:** Instruction Hierarchy
- **Authors:** Eric Wallace, Kai Xiao, Reimar Leike, Lilian Weng, Johannes Heidecke, Alex Beutel
- **Year used for thesis:** 2024
- **Venue/status:** arXiv / OpenReview preprint; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** instruction priority defense
- **BibTeX key:** `wallace2024instructionhierarchy`
- **Source PDF file:** `2024-04 - The Instruction Hierarchy- Training LLMs to Prioritize Privileged Instructions.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Defines a hierarchy of instruction priorities so models learn to follow privileged instructions and ignore lower-priority adversarial instructions.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Defines a hierarchy of instruction priorities so models learn to follow privileged instructions and ignore lower-priority adversarial instructions.

- **Key finding:**  
  Training on hierarchical conflicts improves robustness to prompt injections and jailbreaks with minimal degradation on normal capabilities.

- **Limitation connected to thesis:**  
  Model-level hierarchy helps but does not fully protect autonomous web agents that face multimodal UI manipulation, tool side effects, and cross-session memory poisoning.

- **Connects to:**  
  WebAgentGuard, Permission Manifests, ST-WebAgentBench, policy hierarchy.

- **Use in thesis:**  
  method paper for defending against prompt injection through instruction-priority training

---

## Detailed notes

- Argues that many prompt-injection failures arise because models do not distinguish instruction authority.
- Defines trusted system/developer instructions above users and external content.
- Provides a data-generation method for training priority-aware behavior.
- Useful as a conceptual defense baseline throughout S7.
- Feeds S8 governance: agents need explicit authority and permission models.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
instruction priority defense
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
method paper for defending against prompt injection through instruction-priority training
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Model-level hierarchy helps but does not fully protect autonomous web agents that face multimodal UI manipulation, tool side effects, and cross-session memory poisoning.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

Instruction Hierarchy contributes to S7 by showing that Defines a hierarchy of instruction priorities so models learn to follow privileged instructions and ignore lower-priority adversarial instructions. The main result is that Training on hierarchical conflicts improves robustness to prompt injections and jailbreaks with minimal degradation on normal capabilities. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Model-level hierarchy helps but does not fully protect autonomous web agents that face multimodal UI manipulation, tool side effects, and cross-session memory poisoning. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

Instruction Hierarchy shows that **Defines a hierarchy of instruction priorities so models learn to follow privileged instructions and ignore lower-priority adversarial instructions**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{wallace2024instructionhierarchy,
  title   = {The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions},
  author  = {Eric Wallace, Kai Xiao, Reimar Leike, Lilian Weng, Johannes Heidecke, Alex Beutel},
  journal = {arXiv / OpenReview preprint; no final peer-reviewed venue confirmed in this check},
  year    = {2024},
  url     = {https://arxiv.org/abs/2404.13208}
}
```

---

## Source links

- https://arxiv.org/abs/2404.13208


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\09 - A Survey on the Safety and Security Threats of Computer-Using Agents- JARVIS or Ultron-.md

# A Survey on the Safety and Security Threats of Computer-Using Agents: JARVIS or Ultron?

## Metadata

- **Short name:** CUA Safety Survey
- **Authors:** Ada Chen, Yongjiang Wu, Junyuan Zhang, Shu Yang, Jen-tse Huang, Kun Wang, Wenxuan Wang, Shuai Wang
- **Year used for thesis:** 2025
- **Venue/status:** arXiv survey preprint
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** survey
- **BibTeX key:** `chen2025cuasafetysurvey`
- **Source PDF file:** `2025-05 - A Survey on the Safety and Security Threats of Computer-Using Agents- JARVIS or Ultron -- v1.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Surveys threats to computer-using agents across GUI automation, web interaction, privacy, security, and misuse.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Surveys threats to computer-using agents across GUI automation, web interaction, privacy, security, and misuse.

- **Key finding:**  
  CUAs introduce a wider attack surface than chatbots because they perceive GUIs, maintain state, and execute actions on user devices or websites.

- **Limitation connected to thesis:**  
  Survey-level synthesis; does not provide a new benchmark or defense.

- **Connects to:**  
  all S7 clusters; S8 open challenges.

- **Use in thesis:**  
  survey paper organizing security and safety threats for computer-using agents

---

## Detailed notes

- Useful for taxonomy and terminology.
- Covers agent-as-victim and agent-as-attacker risks.
- Connects GUI, OS, and web-agent security.
- Good background citation for CUA threat surface.
- Helps frame why web-agent security is broader than prompt injection only.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
survey
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
survey paper organizing security and safety threats for computer-using agents
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Survey-level synthesis; does not provide a new benchmark or defense.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

CUA Safety Survey contributes to S7 by showing that Surveys threats to computer-using agents across GUI automation, web interaction, privacy, security, and misuse. The main result is that CUAs introduce a wider attack surface than chatbots because they perceive GUIs, maintain state, and execute actions on user devices or websites. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Survey-level synthesis; does not provide a new benchmark or defense. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

CUA Safety Survey shows that **Surveys threats to computer-using agents across GUI automation, web interaction, privacy, security, and misuse**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{chen2025cuasafetysurvey,
  title   = {A Survey on the Safety and Security Threats of Computer-Using Agents: JARVIS or Ultron?},
  author  = {Ada Chen, Yongjiang Wu, Junyuan Zhang, Shu Yang, Jen-tse Huang, Kun Wang, Wenxuan Wang, Shuai Wang},
  journal = {arXiv survey preprint},
  year    = {2025},
  url     = {https://arxiv.org/abs/2505.10924}
}
```

---

## Source links

- https://arxiv.org/abs/2505.10924


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\10 - AdInject- Real-World Black-Box Attacks on Web Agents via Advertising Delivery.md

# AdInject: Real-World Black-Box Attacks on Web Agents via Advertising Delivery

## Metadata

- **Short name:** AdInject
- **Authors:** Haowei Wang, Junjie Wang, Xiaojun Jia, Rupeng Zhang, Mingyang Li, Zhe Liu, Yang Liu, Qing Wang
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** advertising-delivery environmental attack
- **BibTeX key:** `wang2025adinject`
- **Source PDF file:** `2025-05 - AdInject- Real-World Black-Box Attacks on Web Agents via Advertising Delivery.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Uses ad delivery as a practical channel for injecting malicious content into the web-agent environment without controlling the target website or knowing the user task.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Uses ad delivery as a practical channel for injecting malicious content into the web-agent environment without controlling the target website or knowing the user task.

- **Key finding:**  
  Ad content can mislead VLM web agents into clicking or following attacker goals, with high attack success in many scenarios.

- **Limitation connected to thesis:**  
  Focused on advertising injection and click/steering outcomes; does not solve generalized defense against all forms of environmental manipulation.

- **Connects to:**  
  Pop-up Attack, EIA, Cross-Modal Preference Steering, dark patterns.

- **Use in thesis:**  
  realistic black-box attack channel using online advertising delivery

---

## Detailed notes

- Assumes a more realistic attacker than full website control.
- Optimizes static malicious ad content for likely task relevance.
- Shows commercial ad infrastructure can become a web-agent attack vector.
- Important for real-web deployment because ads are ubiquitous and dynamic.
- Supports the thesis gap around untrusted third-party page content.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
advertising-delivery environmental attack
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
realistic black-box attack channel using online advertising delivery
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Focused on advertising injection and click/steering outcomes; does not solve generalized defense against all forms of environmental manipulation.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

AdInject contributes to S7 by showing that Uses ad delivery as a practical channel for injecting malicious content into the web-agent environment without controlling the target website or knowing the user task. The main result is that Ad content can mislead VLM web agents into clicking or following attacker goals, with high attack success in many scenarios. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Focused on advertising injection and click/steering outcomes; does not solve generalized defense against all forms of environmental manipulation. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

AdInject shows that **Uses ad delivery as a practical channel for injecting malicious content into the web-agent environment without controlling the target website or knowing the user task**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{wang2025adinject,
  title   = {AdInject: Real-World Black-Box Attacks on Web Agents via Advertising Delivery},
  author  = {Haowei Wang, Junjie Wang, Xiaojun Jia, Rupeng Zhang, Mingyang Li, Zhe Liu, Yang Liu, Qing Wang},
  journal = {arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year    = {2025},
  url     = {https://arxiv.org/abs/2505.21499}
}
```

---

## Source links

- https://arxiv.org/abs/2505.21499


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\11 - Cross-Modal Content Optimization for Steering Web Agent Preferences.md

# Cross-Modal Content Optimization for Steering Web Agent Preferences

## Metadata

- **Short name:** Cross-Modal Preference Steering / CPS
- **Authors:** Tanqiu Jiang, Min Bai, Nikolaos Pappas, Yanjun Qi, Sandesh Swamy
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** preference manipulation
- **BibTeX key:** `jiang2025cps`
- **Source PDF file:** `2025-10 - CROSS-MODAL CONTENT OPTIMIZATION FOR STEERING WEB AGENT PREFERENCES.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Introduces Cross-Modal Preference Steering, which jointly optimizes item images and text metadata to bias VLM-based web-agent choices under a realistic publisher-level threat model.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Introduces Cross-Modal Preference Steering, which jointly optimizes item images and text metadata to bias VLM-based web-agent choices under a realistic publisher-level threat model.

- **Key finding:**  
  Cross-modal optimization is more effective and stealthier than single-modal baselines, including on movie-selection and e-commerce tasks.

- **Limitation connected to thesis:**  
  Targets selection/preference tasks rather than full automation; defenses and legal implications remain open.

- **Connects to:**  
  AdInject, dark patterns, recommendation/selection agents, S8 market fairness.

- **Use in thesis:**  
  black-box attack on web-agent selection through coordinated visual and textual content changes

---

## Detailed notes

- Attacker can edit only their own listing's image and text.
- No access to agent internals or webpage infrastructure is assumed.
- Uses transferable visual perturbations and RLHF-induced textual biases.
- Important for agent-mediated marketplaces and product curation.
- Shows that agent choice can be manipulated without explicit prompt injection text.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
preference manipulation
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
black-box attack on web-agent selection through coordinated visual and textual content changes
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Targets selection/preference tasks rather than full automation; defenses and legal implications remain open.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

Cross-Modal Preference Steering / CPS contributes to S7 by showing that Introduces Cross-Modal Preference Steering, which jointly optimizes item images and text metadata to bias VLM-based web-agent choices under a realistic publisher-level threat model. The main result is that Cross-modal optimization is more effective and stealthier than single-modal baselines, including on movie-selection and e-commerce tasks. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Targets selection/preference tasks rather than full automation; defenses and legal implications remain open. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

Cross-Modal Preference Steering / CPS shows that **Introduces Cross-Modal Preference Steering, which jointly optimizes item images and text metadata to bias VLM-based web-agent choices under a realistic publisher-level threat model**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{jiang2025cps,
  title   = {Cross-Modal Content Optimization for Steering Web Agent Preferences},
  author  = {Tanqiu Jiang, Min Bai, Nikolaos Pappas, Yanjun Qi, Sandesh Swamy},
  journal = {arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check},
  year    = {2025},
  url     = {https://arxiv.org/abs/2510.03612}
}
```

---

## Source links

- https://arxiv.org/abs/2510.03612


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\12 - EIA- Environmental Injection Attack on Generalist Web Agents for Privacy Leakage.md

# EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage

## Metadata

- **Short name:** EIA
- **Authors:** Zeyi Liao, Lingbo Mo, Chejian Xu, Mintong Kang, Jiawei Zhang, Chaowei Xiao, Yuan Tian, Bo Li, Huan Sun
- **Year used for thesis:** 2025
- **Venue/status:** ICLR 2025 conference paper
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** privacy leakage via environmental injection
- **BibTeX key:** `liao2025eia`
- **Source PDF file:** `2025-03 - EIA- Environmental Injection Attack on Generalist Web Agents for Privacy Leakage.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Injects malicious but environment-adapted web elements into webpages to trick generalist web agents into leaking PII or user requests.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Injects malicious but environment-adapted web elements into webpages to trick generalist web agents into leaking PII or user requests.

- **Key finding:**  
  EIA achieves high ASR for stealing specific PII and demonstrates that generic defensive prompts are insufficient.

- **Limitation connected to thesis:**  
  Requires attacker influence over webpage elements; the defense discussion remains incomplete.

- **Connects to:**  
  WIPI, WASP, RedTeamCUA, WebAgentGuard, S6 extraction privacy.

- **Use in thesis:**  
  key web-agent privacy attack paper

---

## Detailed notes

- Targets realistic web workflows involving PII.
- Adapts injected elements to the page to reduce human detectability.
- Distinguishes specific PII leakage from full user-request leakage.
- Shows trade-off between autonomy and human inspection.
- Central S7 paper for what malicious web content can do to a web agent.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
privacy leakage via environmental injection
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
key web-agent privacy attack paper
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Requires attacker influence over webpage elements; the defense discussion remains incomplete.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

EIA contributes to S7 by showing that Injects malicious but environment-adapted web elements into webpages to trick generalist web agents into leaking PII or user requests. The main result is that EIA achieves high ASR for stealing specific PII and demonstrates that generic defensive prompts are insufficient. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Requires attacker influence over webpage elements; the defense discussion remains incomplete. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

EIA shows that **Injects malicious but environment-adapted web elements into webpages to trick generalist web agents into leaking PII or user requests**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@inproceedings{liao2025eia,
  title     = {EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage},
  author    = {Zeyi Liao, Lingbo Mo, Chejian Xu, Mintong Kang, Jiawei Zhang, Chaowei Xiao, Yuan Tian, Bo Li, Huan Sun},
  booktitle = {ICLR 2025},
  year      = {2025},
  url       = {https://openreview.net/forum?id=xMOLUzo2Lk}
}
```

---

## Source links

- https://openreview.net/forum?id=xMOLUzo2Lk


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\13 - Investigating the Impact of Dark Patterns on LLM-Based Web Agents.md

# Investigating the Impact of Dark Patterns on LLM-Based Web Agents

## Metadata

- **Short name:** LiteAgent / TrickyArena
- **Authors:** Devin Ersoy, Brandon Lee, Ananth Shreekumar, Arjun Arunasalam, Muhammad Ibrahim, Antonio Bianchi, Z. Berkay Celik
- **Year used for thesis:** 2026
- **Venue/status:** IEEE Symposium on Security and Privacy 2026
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** dark patterns benchmark
- **BibTeX key:** `ersoy2026darkpatternswebagents`
- **Source PDF file:** `2025-10 - Investigating the Impact of Dark Patterns on LLM-Based Web Agents.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Introduces LiteAgent and TrickyArena to evaluate web agents against dark patterns across controlled websites and multiple agents/LLMs.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Introduces LiteAgent and TrickyArena to evaluate web agents against dark patterns across controlled websites and multiple agents/LLMs.

- **Key finding:**  
  With a single dark pattern present, agents are susceptible on average 41% of the time; toggling visual and HTML attributes and combining patterns changes susceptibility.

- **Limitation connected to thesis:**  
  Controlled React sites cannot cover the full diversity of live web UI manipulation, and prompt-based countermeasures only partially reduce susceptibility.

- **Connects to:**  
  DECEPTICON, Dark Patterns Meet GUI Agents, S5.5 failure modes, S8 user autonomy.

- **Use in thesis:**  
  security/privacy benchmark showing web agents are susceptible to deceptive UI designs

---

## Detailed notes

- Evaluates commercial and academic web agents.
- Uses e-commerce, health portal, streaming, and news settings.
- Captures logs and screen recordings for post-hoc analysis.
- Finds vision can sometimes worsen dark-pattern susceptibility.
- Important because dark patterns are common on the real web, unlike many academic attacks.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
dark patterns benchmark
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
security/privacy benchmark showing web agents are susceptible to deceptive UI designs
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Controlled React sites cannot cover the full diversity of live web UI manipulation, and prompt-based countermeasures only partially reduce susceptibility.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

LiteAgent / TrickyArena contributes to S7 by showing that Introduces LiteAgent and TrickyArena to evaluate web agents against dark patterns across controlled websites and multiple agents/LLMs. The main result is that With a single dark pattern present, agents are susceptible on average 41% of the time; toggling visual and HTML attributes and combining patterns changes susceptibility. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Controlled React sites cannot cover the full diversity of live web UI manipulation, and prompt-based countermeasures only partially reduce susceptibility. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

LiteAgent / TrickyArena shows that **Introduces LiteAgent and TrickyArena to evaluate web agents against dark patterns across controlled websites and multiple agents/LLMs**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@inproceedings{ersoy2026darkpatternswebagents,
  title     = {Investigating the Impact of Dark Patterns on LLM-Based Web Agents},
  author    = {Devin Ersoy, Brandon Lee, Ananth Shreekumar, Arjun Arunasalam, Muhammad Ibrahim, Antonio Bianchi, Z. Berkay Celik},
  booktitle = {IEEE Symposium on Security and Privacy 2026},
  year      = {2026},
  url       = {https://sp2026.ieee-security.org/accepted-papers.html}
}
```

---

## Source links

- https://sp2026.ieee-security.org/accepted-papers.html


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\14 - Manipulating LLM Web Agents with Indirect Prompt Injection Attack via HTML Accessibility Tree.md

# Manipulating LLM Web Agents with Indirect Prompt Injection Attack via HTML Accessibility Tree

## Metadata

- **Short name:** A11y-tree IPI
- **Authors:** Sam Johnson, Viet Pham, Thai Le
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** accessibility-tree prompt injection
- **BibTeX key:** `johnson2025a11yipi`
- **Source PDF file:** `2025-07 - Manipulating LLM Web Agents with Indirect Prompt Injection Attack via HTML Accessibility Tree.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Shows that adversarial triggers embedded in webpage HTML and consumed through the accessibility tree can hijack web navigation agents.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Shows that adversarial triggers embedded in webpage HTML and consumed through the accessibility tree can hijack web navigation agents.

- **Key finding:**  
  Triggers can cause targeted and general attacks, including forced clicks and credential-exfiltration-style scenarios in BrowserGym/Llama-3.1 settings.

- **Limitation connected to thesis:**  
  Attack success depends on framework visibility, target action syntax, and model-specific trigger optimization.

- **Connects to:**  
  WIPI, WAInjectBench, WebAgentGuard, S5.2 accessibility tree representation.

- **Use in thesis:**  
  attack paper focused on universal adversarial triggers embedded in HTML/a11y tree

---

## Detailed notes

- Uses Greedy Coordinate Gradient style trigger search.
- Focuses on agents that parse HTML into an accessibility tree.
- Demonstrates that a11y-tree representations are not inherently safe.
- Shows attack paths through legitimate webpage structure rather than executable code.
- Useful for thesis discussion of representation as security boundary.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
accessibility-tree prompt injection
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
attack paper focused on universal adversarial triggers embedded in HTML/a11y tree
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Attack success depends on framework visibility, target action syntax, and model-specific trigger optimization.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

A11y-tree IPI contributes to S7 by showing that Shows that adversarial triggers embedded in webpage HTML and consumed through the accessibility tree can hijack web navigation agents. The main result is that Triggers can cause targeted and general attacks, including forced clicks and credential-exfiltration-style scenarios in BrowserGym/Llama-3.1 settings. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Attack success depends on framework visibility, target action syntax, and model-specific trigger optimization. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

A11y-tree IPI shows that **Shows that adversarial triggers embedded in webpage HTML and consumed through the accessibility tree can hijack web navigation agents**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{johnson2025a11yipi,
  title   = {Manipulating LLM Web Agents with Indirect Prompt Injection Attack via HTML Accessibility Tree},
  author  = {Sam Johnson, Viet Pham, Thai Le},
  journal = {arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year    = {2025},
  url     = {https://arxiv.org/abs/2507.14799}
}
```

---

## Source links

- https://arxiv.org/abs/2507.14799


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\15 - Mind the Web- The Security of Web Use Agents.md

# Mind the Web: The Security of Web Use Agents

## Metadata

- **Short name:** Mind the Web
- **Authors:** Avishag Shapira, Parth Atulbhai Gandhi, Edan Habler, Asaf Shabtai
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** task-aligned injection / web-use agent security
- **BibTeX key:** `shapira2025mindweb`
- **Source PDF file:** `2025-12 - Mind the Web- The Security of Web Use Agents.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Introduces task-aligned injections that frame malicious instructions as helpful task guidance in webpage comments, ads, or forum posts.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Introduces task-aligned injections that frame malicious instructions as helpful task guidance in webpage comments, ads, or forum posts.

- **Key finding:**  
  A generator model produces attacks with over 80% ASR and strong transferability across agents, environments, and LLMs.

- **Limitation connected to thesis:**  
  Mitigations are proposed conceptually; robust defenses for high-privilege browser agents remain unresolved.

- **Connects to:**  
  EIA, RedTeamCUA, WAInjectBench, WebAgentGuard, AI Kill Switch.

- **Use in thesis:**  
  high-privilege web-use agent threat model with task-aligned injections

---

## Detailed notes

- Organizes payloads by the CIA triad.
- Covers camera activation, file exfiltration, phishing, user impersonation, and denial of service.
- Attacker only needs ability to post content on websites agents may visit.
- Shows browser security mechanisms such as CSP do not block natural-language manipulation.
- Strong evidence that web agents require task-aware reasoning and execution constraints.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
task-aligned injection / web-use agent security
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
high-privilege web-use agent threat model with task-aligned injections
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Mitigations are proposed conceptually; robust defenses for high-privilege browser agents remain unresolved.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

Mind the Web contributes to S7 by showing that Introduces task-aligned injections that frame malicious instructions as helpful task guidance in webpage comments, ads, or forum posts. The main result is that A generator model produces attacks with over 80% ASR and strong transferability across agents, environments, and LLMs. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Mitigations are proposed conceptually; robust defenses for high-privilege browser agents remain unresolved. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

Mind the Web shows that **Introduces task-aligned injections that frame malicious instructions as helpful task guidance in webpage comments, ads, or forum posts**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{shapira2025mindweb,
  title   = {Mind the Web: The Security of Web Use Agents},
  author  = {Avishag Shapira, Parth Atulbhai Gandhi, Edan Habler, Asaf Shabtai},
  journal = {arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year    = {2025},
  url     = {https://arxiv.org/abs/2506.07153}
}
```

---

## Source links

- https://arxiv.org/abs/2506.07153


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\16 - RedTeamCUA- Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments.md

# RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments

## Metadata

- **Short name:** RedTeamCUA / RTC-Bench
- **Authors:** Zeyi Liao, Jaylen Jones, Linxi Jiang, Yuting Ning, Eric Fosler-Lussier, Yu Su, Zhiqiang Lin, Huan Sun
- **Year used for thesis:** 2026
- **Venue/status:** ICLR 2026 conference paper
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** hybrid web-OS adversarial benchmark
- **BibTeX key:** `liao2026redteamcua`
- **Source PDF file:** `2025-05-RedTeamCUA Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Builds a hybrid sandbox combining VM-based OS environments and Docker-based web replicas to evaluate indirect prompt injection across web and OS interfaces.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Builds a hybrid sandbox combining VM-based OS environments and Docker-based web replicas to evaluate indirect prompt injection across web and OS interfaces.

- **Key finding:**  
  RTC-Bench shows substantial CUA vulnerability; even relatively secure systems still exhibit nonzero attack success and high attempt rates.

- **Limitation connected to thesis:**  
  Sandbox realism is much stronger than prior work but still controlled; it does not fully represent the entire open web.

- **Connects to:**  
  EIA, Mind the Web, SecureWebArena, S8 deployment security.

- **Use in thesis:**  
  major CUA red-teaming benchmark for hybrid web and OS attack chains

---

## Detailed notes

- Constructs RTC-Bench with hundreds of hybrid adversarial examples.
- Separates decoupled vulnerability evaluation from full end-to-end navigation limitations.
- Covers confidentiality, integrity, and availability goals.
- Shows capability improvements can increase risk when defenses do not improve.
- Important benchmark for the thesis's safe deployment discussion.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
hybrid web-OS adversarial benchmark
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
major CUA red-teaming benchmark for hybrid web and OS attack chains
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Sandbox realism is much stronger than prior work but still controlled; it does not fully represent the entire open web.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

RedTeamCUA / RTC-Bench contributes to S7 by showing that Builds a hybrid sandbox combining VM-based OS environments and Docker-based web replicas to evaluate indirect prompt injection across web and OS interfaces. The main result is that RTC-Bench shows substantial CUA vulnerability; even relatively secure systems still exhibit nonzero attack success and high attempt rates. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Sandbox realism is much stronger than prior work but still controlled; it does not fully represent the entire open web. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

RedTeamCUA / RTC-Bench shows that **Builds a hybrid sandbox combining VM-based OS environments and Docker-based web replicas to evaluate indirect prompt injection across web and OS interfaces**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@inproceedings{liao2026redteamcua,
  title     = {RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments},
  author    = {Zeyi Liao, Jaylen Jones, Linxi Jiang, Yuting Ning, Eric Fosler-Lussier, Yu Su, Zhiqiang Lin, Huan Sun},
  booktitle = {ICLR 2026},
  year      = {2026},
  url       = {https://openreview.net/forum?id=yWwrgcBoK3}
}
```

---

## Source links

- https://openreview.net/forum?id=yWwrgcBoK3


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\17 - SafeArena- Evaluating the Safety of Autonomous Web Agents.md

# SafeArena: Evaluating the Safety of Autonomous Web Agents

## Metadata

- **Short name:** SafeArena
- **Authors:** Ada Defne Tur, Nicholas Meade, Xing Han Lù, Alejandra Zambrano, Arkil Patel, Esin Durmus, Spandana Gella, Karolina Stańczak, Siva Reddy
- **Year used for thesis:** 2025
- **Venue/status:** arXiv / OpenReview preprint; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** deliberate misuse benchmark
- **BibTeX key:** `tur2025safearena`
- **Source PDF file:** `2025-03-SafeArena Evaluating the Safety of Autonomous Web Agents.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Evaluates whether web agents comply with harmful tasks across misinformation, illegal activity, harassment, cybercrime, and social bias.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Evaluates whether web agents comply with harmful tasks across misinformation, illegal activity, harassment, cybercrime, and social bias.

- **Key finding:**  
  Leading web agents complete or attempt a nontrivial fraction of harmful tasks, showing that general web competence introduces misuse risk.

- **Limitation connected to thesis:**  
  Focuses on malicious user instructions rather than malicious web environments or cross-site memory poisoning.

- **Connects to:**  
  BrowserART, ST-WebAgentBench, RedTeamCUA, S8 governance.

- **Use in thesis:**  
  benchmark for malicious user requests to web agents

---

## Detailed notes

- Contains matched safe and harmful tasks.
- Runs in web environments where task completion can cause problematic actions.
- Introduces an agent risk assessment framework.
- Useful for separating agent-as-attacker from agent-as-victim threat models.
- Supports the S7 distinction between malicious users and malicious pages.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
deliberate misuse benchmark
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
benchmark for malicious user requests to web agents
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Focuses on malicious user instructions rather than malicious web environments or cross-site memory poisoning.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

SafeArena contributes to S7 by showing that Evaluates whether web agents comply with harmful tasks across misinformation, illegal activity, harassment, cybercrime, and social bias. The main result is that Leading web agents complete or attempt a nontrivial fraction of harmful tasks, showing that general web competence introduces misuse risk. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Focuses on malicious user instructions rather than malicious web environments or cross-site memory poisoning. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

SafeArena shows that **Evaluates whether web agents comply with harmful tasks across misinformation, illegal activity, harassment, cybercrime, and social bias**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{tur2025safearena,
  title   = {SafeArena: Evaluating the Safety of Autonomous Web Agents},
  author  = {Ada Defne Tur, Nicholas Meade, Xing Han Lù, Alejandra Zambrano, Arkil Patel, Esin Durmus, Spandana Gella, Karolina Stańczak, Siva Reddy},
  journal = {arXiv / OpenReview preprint; no final peer-reviewed venue confirmed in this check},
  year    = {2025},
  url     = {https://arxiv.org/abs/2503.04957}
}
```

---

## Source links

- https://arxiv.org/abs/2503.04957


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\18 - WAInjectBench- Benchmarking Prompt Injection Detections for Web Agents.md

# WAInjectBench: Benchmarking Prompt Injection Detections for Web Agents

## Metadata

- **Short name:** WAInjectBench
- **Authors:** Yinuo Liu, Ruohan Xu, Xilong Wang, Yuqi Jia, Neil Zhenqiang Gong
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** prompt-injection detection benchmark
- **BibTeX key:** `liu2025wainjectbench`
- **Source PDF file:** `2025-12 - WAInjectBench- Benchmarking Prompt Injection Detections for Web Agents.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Constructs malicious and benign text/image datasets from multiple web-agent prompt-injection attacks and benchmarks detection methods.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Constructs malicious and benign text/image datasets from multiple web-agent prompt-injection attacks and benchmarks detection methods.

- **Key finding:**  
  Detectors can catch explicit textual instructions or visible perturbations but largely fail on attacks without explicit instructions or with imperceptible perturbations.

- **Limitation connected to thesis:**  
  Detection benchmark, not a complete runtime defense; static detection may not capture full trajectory-level risk.

- **Connects to:**  
  WebInject, WebAgentGuard, WASP, a11y-tree IPI.

- **Use in thesis:**  
  benchmark for detecting web-agent prompt injections across text and image modalities

---

## Detailed notes

- Categorizes prompt injection attacks by attacker capability, knowledge, and contaminated observation.
- Covers text and image modalities.
- Evaluates prompting, embedding, fine-tuning, and ensemble detectors.
- Shows text and image detectors fail on different attack categories.
- Important for thesis because detection must be multimodal and context-aware.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
prompt-injection detection benchmark
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
benchmark for detecting web-agent prompt injections across text and image modalities
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Detection benchmark, not a complete runtime defense; static detection may not capture full trajectory-level risk.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

WAInjectBench contributes to S7 by showing that Constructs malicious and benign text/image datasets from multiple web-agent prompt-injection attacks and benchmarks detection methods. The main result is that Detectors can catch explicit textual instructions or visible perturbations but largely fail on attacks without explicit instructions or with imperceptible perturbations. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Detection benchmark, not a complete runtime defense; static detection may not capture full trajectory-level risk. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

WAInjectBench shows that **Constructs malicious and benign text/image datasets from multiple web-agent prompt-injection attacks and benchmarks detection methods**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{liu2025wainjectbench,
  title   = {WAInjectBench: Benchmarking Prompt Injection Detections for Web Agents},
  author  = {Yinuo Liu, Ruohan Xu, Xilong Wang, Yuqi Jia, Neil Zhenqiang Gong},
  journal = {arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check},
  year    = {2025},
  url     = {https://arxiv.org/abs/2510.01354}
}
```

---

## Source links

- https://arxiv.org/abs/2510.01354


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\19 - WASP- Benchmarking Web Agent Security Against Prompt Injection Attacks.md

# WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks

## Metadata

- **Short name:** WASP
- **Authors:** Ivan Evtimov, Arman Zharmagambetov, Aaron Grattafiori, Chuan Guo, Kamalika Chaudhuri
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** web-agent prompt-injection benchmark
- **BibTeX key:** `evtimov2025wasp`
- **Source PDF file:** `2025-05 - WASP- Benchmarking Web Agent Security Against Prompt Injection Attacks.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Introduces an executable web-agent security benchmark for prompt-injection attacks under more realistic end-to-end conditions.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Introduces an executable web-agent security benchmark for prompt-injection attacks under more realistic end-to-end conditions.

- **Key finding:**  
  Web agents remain sensitive to prompt-injection attacks, and simplified single-step tests underestimate the problem.

- **Limitation connected to thesis:**  
  Benchmark focuses primarily on prompt injection and not all web-agent security risks such as dark patterns, scraping misuse, or memory poisoning.

- **Connects to:**  
  WAInjectBench, SecureWebArena, EIA, RedTeamCUA.

- **Use in thesis:**  
  end-to-end benchmark for web-agent prompt injection security

---

## Detailed notes

- Designed to simulate real-world attacks while avoiding real harm.
- Targets trajectory-level security rather than isolated model outputs.
- Useful as a bridge between attack papers and holistic security benchmarks.
- Provides realistic executable environments for evaluation.
- Shows that security needs to be assessed at system level, not only model level.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
web-agent prompt-injection benchmark
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
end-to-end benchmark for web-agent prompt injection security
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Benchmark focuses primarily on prompt injection and not all web-agent security risks such as dark patterns, scraping misuse, or memory poisoning.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

WASP contributes to S7 by showing that Introduces an executable web-agent security benchmark for prompt-injection attacks under more realistic end-to-end conditions. The main result is that Web agents remain sensitive to prompt-injection attacks, and simplified single-step tests underestimate the problem. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Benchmark focuses primarily on prompt injection and not all web-agent security risks such as dark patterns, scraping misuse, or memory poisoning. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

WASP shows that **Introduces an executable web-agent security benchmark for prompt-injection attacks under more realistic end-to-end conditions**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{evtimov2025wasp,
  title   = {WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks},
  author  = {Ivan Evtimov, Arman Zharmagambetov, Aaron Grattafiori, Chuan Guo, Kamalika Chaudhuri},
  journal = {arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check},
  year    = {2025},
  url     = {https://arxiv.org/abs/2504.18575}
}
```

---

## Source links

- https://arxiv.org/abs/2504.18575


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\20 - WebInject- Prompt Injection Attack to Web Agents.md

# WebInject: Prompt Injection Attack to Web Agents

## Metadata

- **Short name:** WebInject
- **Authors:** Xilong Wang, John Bloch, Zedian Shao, Yuepeng Hu, Shuyan Zhou, Neil Zhenqiang Gong
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** pixel-space webpage attack
- **BibTeX key:** `wang2025webinject`
- **Source PDF file:** `2025-05-WebInject Prompt Injection Attack to Web Agents.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Optimizes imperceptible perturbations in webpage raw pixels so that rendered screenshots induce a web agent to perform an attacker-specified action.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Optimizes imperceptible perturbations in webpage raw pixels so that rendered screenshots induce a web agent to perform an attacker-specified action.

- **Key finding:**  
  WebInject is highly effective and outperforms prior baselines by accounting for webpage-to-screenshot mappings.

- **Limitation connected to thesis:**  
  Assumes attacker can modify webpage source code and has limited evaluation on closed-source MLLMs.

- **Connects to:**  
  WAInjectBench, WebAgentGuard, Pop-up Attack, S5.2 visual observations.

- **Use in thesis:**  
  stealthy prompt-injection attack via webpage raw-pixel perturbations

---

## Detailed notes

- Models the non-differentiable webpage-to-screenshot mapping.
- Uses a neural approximation plus projected gradient descent.
- Does not rely on explicit malicious text instructions.
- Demonstrates why text-only prompt-injection detectors are insufficient.
- Important for web agents that rely primarily on screenshots.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
pixel-space webpage attack
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
stealthy prompt-injection attack via webpage raw-pixel perturbations
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Assumes attacker can modify webpage source code and has limited evaluation on closed-source MLLMs.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

WebInject contributes to S7 by showing that Optimizes imperceptible perturbations in webpage raw pixels so that rendered screenshots induce a web agent to perform an attacker-specified action. The main result is that WebInject is highly effective and outperforms prior baselines by accounting for webpage-to-screenshot mappings. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Assumes attacker can modify webpage source code and has limited evaluation on closed-source MLLMs. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

WebInject shows that **Optimizes imperceptible perturbations in webpage raw pixels so that rendered screenshots induce a web agent to perform an attacker-specified action**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{wang2025webinject,
  title   = {WebInject: Prompt Injection Attack to Web Agents},
  author  = {Xilong Wang, John Bloch, Zedian Shao, Yuepeng Hu, Shuyan Zhou, Neil Zhenqiang Gong},
  journal = {arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year    = {2025},
  url     = {https://arxiv.org/abs/2503.19786}
}
```

---

## Source links

- https://arxiv.org/abs/2503.19786


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\21 - Why Are Web AI Agents More Vulnerable Than Standalone LLMs- A Security Analysis.md

# Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis

## Metadata

- **Short name:** Web Agents Vulnerability Analysis
- **Authors:** Jeffrey Yang Fan Chiang, Seungjae Lee, Jia-Bin Huang, Furong Huang, Yizheng Chen
- **Year used for thesis:** 2025
- **Venue/status:** Building Trust Workshop at ICLR 2025 + arXiv preprint
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** component-level vulnerability analysis
- **BibTeX key:** `chiang2025webagentsvulnerable`
- **Source PDF file:** `2025-02-Why Are Web AI Agents More Vulnerable Than Standalone LLMs A Security Analysis.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Analyzes why web-agent scaffolds increase vulnerability compared with standalone LLMs built from the same safety-aligned models.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Analyzes why web-agent scaffolds increase vulnerability compared with standalone LLMs built from the same safety-aligned models.

- **Key finding:**  
  Three factors amplify vulnerability: embedding user goals in the system prompt, multi-step action generation, and observational capabilities.

- **Limitation connected to thesis:**  
  Diagnostic rather than a complete benchmark or defense; findings need to be extended to broader agent architectures.

- **Connects to:**  
  BrowserART, Instruction Hierarchy, WebAgentGuard, S5.5 failure analysis.

- **Use in thesis:**  
  diagnostic paper explaining why agent scaffolds are less safe than standalone LLMs

---

## Detailed notes

- Shows that agent architecture changes model safety behavior.
- Component-level analysis is more informative than aggregate success rate.
- Real websites reduce clear-denial behavior compared with mockups.
- Supports thesis claim that web-agent security is a system-level property.
- Useful for motivating architecture-level defenses.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
component-level vulnerability analysis
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
diagnostic paper explaining why agent scaffolds are less safe than standalone LLMs
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Diagnostic rather than a complete benchmark or defense; findings need to be extended to broader agent architectures.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

Web Agents Vulnerability Analysis contributes to S7 by showing that Analyzes why web-agent scaffolds increase vulnerability compared with standalone LLMs built from the same safety-aligned models. The main result is that Three factors amplify vulnerability: embedding user goals in the system prompt, multi-step action generation, and observational capabilities. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Diagnostic rather than a complete benchmark or defense; findings need to be extended to broader agent architectures. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

Web Agents Vulnerability Analysis shows that **Analyzes why web-agent scaffolds increase vulnerability compared with standalone LLMs built from the same safety-aligned models**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@inproceedings{chiang2025webagentsvulnerable,
  title     = {Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis},
  author    = {Jeffrey Yang Fan Chiang, Seungjae Lee, Jia-Bin Huang, Furong Huang, Yizheng Chen},
  booktitle = {Building Trust Workshop at ICLR 2025 + arXiv preprint},
  year      = {2025},
  url       = {https://arxiv.org/abs/2502.20383}
}
```

---

## Source links

- https://arxiv.org/abs/2502.20383


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\22 - sudo rm -rf agentic_security.md

# sudo rm -rf agentic_security

## Metadata

- **Short name:** SUDO / DETOX2TOX
- **Authors:** Sejin Lee, Jian Kim, Haon Park, Ashkan Yousefpour, Sangyoon Yu, Min Song
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** computer-use refusal bypass
- **BibTeX key:** `lee2025sudo`
- **Source PDF file:** `2025-03-sudo rm -rf agentic_security.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Introduces SUDO / DETOX2TOX, which transforms harmful requests into apparently benign screen-based interactions to bypass safeguards in computer-use agents.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Introduces SUDO / DETOX2TOX, which transforms harmful requests into apparently benign screen-based interactions to bypass safeguards in computer-use agents.

- **Key finding:**  
  Commercial computer-use agents can be induced to perform harmful tasks when the request is reframed through visual/screen context.

- **Limitation connected to thesis:**  
  Primarily focused on attack; defense guidance remains limited and may not generalize to all web-agent settings.

- **Connects to:**  
  BrowserART, RedTeamCUA, HackWorld, S8 deployment safety.

- **Use in thesis:**  
  attack framework against refusal-trained computer-use agents

---

## Detailed notes

- Targets screen-based computer-use agents.
- Shows refusal alignment may fail when task semantics are transformed through UI context.
- Relevant to web agents because browser actions are screen-mediated.
- Adds to evidence that aligned chat behavior does not imply aligned agent behavior.
- Use cautiously: venue/status and arXiv ID should be rechecked before final bibliography.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
computer-use refusal bypass
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
attack framework against refusal-trained computer-use agents
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Primarily focused on attack; defense guidance remains limited and may not generalize to all web-agent settings.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

SUDO / DETOX2TOX contributes to S7 by showing that Introduces SUDO / DETOX2TOX, which transforms harmful requests into apparently benign screen-based interactions to bypass safeguards in computer-use agents. The main result is that Commercial computer-use agents can be induced to perform harmful tasks when the request is reframed through visual/screen context. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Primarily focused on attack; defense guidance remains limited and may not generalize to all web-agent settings. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

SUDO / DETOX2TOX shows that **Introduces SUDO / DETOX2TOX, which transforms harmful requests into apparently benign screen-based interactions to bypass safeguards in computer-use agents**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{lee2025sudo,
  title   = {sudo rm -rf agentic_security},
  author  = {Sejin Lee, Jian Kim, Haon Park, Ashkan Yousefpour, Sangyoon Yu, Min Song},
  journal = {arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year    = {2025},
  url     = {https://arxiv.org/abs/2503.XXX}
}
```

---

## Source links

- https://arxiv.org/abs/2503.XXX


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\23 - A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents.md

# A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents

## Metadata

- **Short name:** Autonomy-Induced Security Risks Survey
- **Authors:** Hang Su, Jun Luo, Chang Liu, Xiao Yang, Yichi Zhang, Yinpeng Dong, Jun Zhu
- **Year used for thesis:** 2025
- **Venue/status:** arXiv survey/manuscript formatted as IEEE TPAMI; no final journal issue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** survey / autonomy risk
- **BibTeX key:** `su2025autonomyrisks`
- **Source PDF file:** `2025-06 - A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Surveys how large-model agents introduce new risks such as memory poisoning, tool misuse, reward hacking, internal-state drift, and emergent misalignment.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Surveys how large-model agents introduce new risks such as memory poisoning, tool misuse, reward hacking, internal-state drift, and emergent misalignment.

- **Key finding:**  
  Autonomy changes the security landscape because agents act over time, retain memory, call tools, and influence external environments.

- **Limitation connected to thesis:**  
  Not web-specific and includes forward-looking architectural proposals; use as background rather than evidence for specific web benchmark results.

- **Connects to:**  
  AgentPoison, Permission Manifests, S8 governance.

- **Use in thesis:**  
  broad survey of security risks introduced by autonomy, memory, tool use, and planning

---

## Detailed notes

- Organizes risk across perception, cognition, memory, and action modules.
- Introduces R2A2 as a risk-aware reflective architecture concept.
- Useful for systemic risk framing.
- Explains why isolated defenses are insufficient for multi-step agents.
- Supports S7 taxonomy by attacker model and autonomy layer.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
survey / autonomy risk
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
broad survey of security risks introduced by autonomy, memory, tool use, and planning
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Not web-specific and includes forward-looking architectural proposals; use as background rather than evidence for specific web benchmark results.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

Autonomy-Induced Security Risks Survey contributes to S7 by showing that Surveys how large-model agents introduce new risks such as memory poisoning, tool misuse, reward hacking, internal-state drift, and emergent misalignment. The main result is that Autonomy changes the security landscape because agents act over time, retain memory, call tools, and influence external environments. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Not web-specific and includes forward-looking architectural proposals; use as background rather than evidence for specific web benchmark results. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

Autonomy-Induced Security Risks Survey shows that **Surveys how large-model agents introduce new risks such as memory poisoning, tool misuse, reward hacking, internal-state drift, and emergent misalignment**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{su2025autonomyrisks,
  title   = {A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents},
  author  = {Hang Su, Jun Luo, Chang Liu, Xiao Yang, Yichi Zhang, Yinpeng Dong, Jun Zhu},
  journal = {arXiv survey/manuscript formatted as IEEE TPAMI; no final journal issue confirmed in this check},
  year    = {2025},
  url     = {https://arxiv.org/abs/2506.23844}
}
```

---

## Source links

- https://arxiv.org/abs/2506.23844


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\24 - Dark Patterns Meet GUI Agents- LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight.md

# Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight

## Metadata

- **Short name:** Dark Patterns Meet GUI Agents
- **Authors:** Jingyu Tang, Chaoran Chen, Jiawen Li, Zhiping Zhang, Bingcan Guo, Ibrahim Khalilov, Simret A. Gebreegziabher, Bingsheng Yao, Dakuo Wang, Yanfang Ye, Tianshi Li, Ziang Xiao, Yaxing Yao, Toby Jia-Jun Li
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** dark patterns and human oversight
- **BibTeX key:** `tang2025darkpatterns`
- **Source PDF file:** `2025-09 - Dark Patterns Meet GUI Agents- LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Studies how GUI agents, human users, and human-AI teams respond to 16 types of dark patterns.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Studies how GUI agents, human users, and human-AI teams respond to 16 types of dark patterns.

- **Key finding:**  
  Agents often fail to recognize dark patterns and prioritize task completion; human oversight helps but adds cognitive load and introduces its own vulnerabilities.

- **Limitation connected to thesis:**  
  Empirical setting is controlled and focused on dark patterns, not all prompt-injection/security attacks.

- **Connects to:**  
  DECEPTICON, TrickyArena, human-in-the-loop deployment, S8 autonomy.

- **Use in thesis:**  
  empirical study comparing agents, humans, and human-supervised agents under dark patterns

---

## Detailed notes

- Two-phase study: agent-only comparison, then human vs agent vs supervised team.
- Shows humans and agents have different failure modes.
- Human oversight can suffer attentional tunneling and cognitive load.
- Important for thesis because HITL is not a complete security solution.
- Supports design implications for adjustable autonomy and transparency.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
dark patterns and human oversight
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
empirical study comparing agents, humans, and human-supervised agents under dark patterns
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Empirical setting is controlled and focused on dark patterns, not all prompt-injection/security attacks.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

Dark Patterns Meet GUI Agents contributes to S7 by showing that Studies how GUI agents, human users, and human-AI teams respond to 16 types of dark patterns. The main result is that Agents often fail to recognize dark patterns and prioritize task completion; human oversight helps but adds cognitive load and introduces its own vulnerabilities. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Empirical setting is controlled and focused on dark patterns, not all prompt-injection/security attacks. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

Dark Patterns Meet GUI Agents shows that **Studies how GUI agents, human users, and human-AI teams respond to 16 types of dark patterns**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{tang2025darkpatterns,
  title   = {Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight},
  author  = {Jingyu Tang, Chaoran Chen, Jiawen Li, Zhiping Zhang, Bingcan Guo, Ibrahim Khalilov, Simret A. Gebreegziabher, Bingsheng Yao, Dakuo Wang, Yanfang Ye, Tianshi Li, Ziang Xiao, Yaxing Yao, Toby Jia-Jun Li},
  journal = {arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year    = {2025},
  url     = {https://arxiv.org/abs/2509.10723}
}
```

---

## Source links

- https://arxiv.org/abs/2509.10723


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\25 - HackWorld- Evaluating Computer-Use Agents on Exploiting Web Application Vulnerabilities.md

# HackWorld: Evaluating Computer-Use Agents on Exploiting Web Application Vulnerabilities

## Metadata

- **Short name:** HackWorld
- **Authors:** Xiaoxue Ren, Penghao Jiang, Kaixin Li, Zhiyong Huang, Xiaoning Du, Jiaojiao Jiang, Zhenchang Xing, Jiamou Sun, Terry Yue Zhuo
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** web application vulnerability exploitation
- **BibTeX key:** `ren2025hackworld`
- **Source PDF file:** `2025-10 - HackWorld- EVALUATING COMPUTER-USE AGENTS ON EXPLOITING WEB APPLICATION VULNERABILITIES.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Creates a CTF-style benchmark with 36 vulnerable web applications across multiple frameworks and languages to test whether CUAs can exploit web vulnerabilities.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Creates a CTF-style benchmark with 36 vulnerable web applications across multiple frameworks and languages to test whether CUAs can exploit web vulnerabilities.

- **Key finding:**  
  Current CUAs achieve exploitation rates below 12% and show weak cybersecurity awareness, multi-step attack planning, and security-tool use.

- **Limitation connected to thesis:**  
  Low exploitation rates mean current risk is limited by capability, but future stronger agents may change this quickly.

- **Connects to:**  
  SafeArena, AI Kill Switch, WebSP-Eval, S8 security deployment.

- **Use in thesis:**  
  benchmark for CUA capability to discover and exploit web vulnerabilities through GUI interaction

---

## Detailed notes

- Uses Capture-the-Flag style objective success via hidden flags.
- Integrates Kali tools such as Burp Suite, DirBuster, Nikto, Wfuzz, and WhatWeb.
- Focuses on the agent as a potential attacker or penetration tester.
- Useful for distinguishing security capability from safety compliance.
- Shows that cyber-use web agents need explicit security-aware reasoning.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
web application vulnerability exploitation
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
benchmark for CUA capability to discover and exploit web vulnerabilities through GUI interaction
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Low exploitation rates mean current risk is limited by capability, but future stronger agents may change this quickly.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

HackWorld contributes to S7 by showing that Creates a CTF-style benchmark with 36 vulnerable web applications across multiple frameworks and languages to test whether CUAs can exploit web vulnerabilities. The main result is that Current CUAs achieve exploitation rates below 12% and show weak cybersecurity awareness, multi-step attack planning, and security-tool use. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Low exploitation rates mean current risk is limited by capability, but future stronger agents may change this quickly. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

HackWorld shows that **Creates a CTF-style benchmark with 36 vulnerable web applications across multiple frameworks and languages to test whether CUAs can exploit web vulnerabilities**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{ren2025hackworld,
  title   = {HackWorld: Evaluating Computer-Use Agents on Exploiting Web Application Vulnerabilities},
  author  = {Xiaoxue Ren, Penghao Jiang, Kaixin Li, Zhiyong Huang, Xiaoning Du, Jiaojiao Jiang, Zhenchang Xing, Jiamou Sun, Terry Yue Zhuo},
  journal = {arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check},
  year    = {2025},
  url     = {https://arxiv.org/abs/2510.12200}
}
```

---

## Source links

- https://arxiv.org/abs/2510.12200


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\26 - Security Challenges in AI Agent Deployment- Insights from a Large Scale Public Competition.md

# Security Challenges in AI Agent Deployment: Insights from a Large Scale Public Competition

## Metadata

- **Short name:** Agent Red Teaming / ART
- **Authors:** Andy Zou, Maxwell Lin, Eliot Jones, Micha Nowak, Mateusz Dziemian, Nick Winter, Alexander Grattan, Valent Nathanael, Ayla Croft, Xander Davies, Jai Patel, Robert Kirk, Nate Burnikell, Yarin Gal, Dan Hendrycks, J. Zico Kolter, Matt Fredrikson
- **Year used for thesis:** 2025
- **Venue/status:** Preprint / under review; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** large-scale public red-teaming
- **BibTeX key:** `zou2025agentredteaming`
- **Source PDF file:** `2025-07 - Security Challenges in AI Agent Deployment- Insights from a Large Scale Public Competition.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Reports a public red-teaming competition over realistic deployment scenarios, producing the ART benchmark from successful policy-violation attacks.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Reports a public red-teaming competition over realistic deployment scenarios, producing the ART benchmark from successful policy-violation attacks.

- **Key finding:**  
  Participants submitted 1.8M attacks and produced many successful policy violations; robustness does not correlate cleanly with model size or capability.

- **Limitation connected to thesis:**  
  Competition-derived attacks may not represent all real-world distributions; benchmark release details may be controlled to avoid misuse.

- **Connects to:**  
  SafeArena, RedTeamCUA, BrowserART, S8 evaluation methodology.

- **Use in thesis:**  
  large-scale evidence of prompt-injection and policy-violation risk in deployed-like agents

---

## Detailed notes

- Covers realistic agent types such as sales, shopping, email, legal, financial, and personal assistants.
- Targets confidentiality breaches, conflicting objectives, prohibited information, and prohibited actions.
- Uses direct and indirect attacks.
- Highlights transferability across models and tasks.
- Good support for arguing that red-teaming must be continuous and deployment-specific.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
large-scale public red-teaming
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
large-scale evidence of prompt-injection and policy-violation risk in deployed-like agents
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Competition-derived attacks may not represent all real-world distributions; benchmark release details may be controlled to avoid misuse.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

Agent Red Teaming / ART contributes to S7 by showing that Reports a public red-teaming competition over realistic deployment scenarios, producing the ART benchmark from successful policy-violation attacks. The main result is that Participants submitted 1.8M attacks and produced many successful policy violations; robustness does not correlate cleanly with model size or capability. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Competition-derived attacks may not represent all real-world distributions; benchmark release details may be controlled to avoid misuse. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

Agent Red Teaming / ART shows that **Reports a public red-teaming competition over realistic deployment scenarios, producing the ART benchmark from successful policy-violation attacks**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{zou2025agentredteaming,
  title   = {Security Challenges in AI Agent Deployment: Insights from a Large Scale Public Competition},
  author  = {Andy Zou, Maxwell Lin, Eliot Jones, Micha Nowak, Mateusz Dziemian, Nick Winter, Alexander Grattan, Valent Nathanael, Ayla Croft, Xander Davies, Jai Patel, Robert Kirk, Nate Burnikell, Yarin Gal, Dan Hendrycks, J. Zico Kolter, Matt Fredrikson},
  journal = {Preprint / under review; no final peer-reviewed venue confirmed in this check},
  year    = {2025},
  url     = {https://arxiv.org/abs/2507.20526}
}
```

---

## Source links

- https://arxiv.org/abs/2507.20526


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\27 - VisualTrap- A Stealthy Backdoor Attack on GUI Agents via Visual Grounding Manipulation.md

# VisualTrap: A Stealthy Backdoor Attack on GUI Agents via Visual Grounding Manipulation

## Metadata

- **Short name:** VisualTrap
- **Authors:** Ziang Ye, Yang Zhang, Wentao Shi, Xiaoyu You, Fuli Feng, Tat-Seng Chua
- **Year used for thesis:** 2025
- **Venue/status:** COLM 2025 conference paper
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** visual-grounding backdoor
- **BibTeX key:** `ye2025visualtrap`
- **Source PDF file:** `2025-07-VisualTrap A Stealthy Backdoor Attack on GUI Agents via Visual Grounding Manipulation.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Shows that poisoning visual-grounding pretraining can cause GUI agents to map correct textual plans to trigger locations rather than intended UI targets.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Shows that poisoning visual-grounding pretraining can cause GUI agents to map correct textual plans to trigger locations rather than intended UI targets.

- **Key finding:**  
  VisualTrap can hijack grounding with as little as 5% poisoned data, stealthy invisible triggers, and transfer across GUI environments even after clean fine-tuning.

- **Limitation connected to thesis:**  
  Requires poisoning during grounding pretraining or supply-chain model release; it is a training-time attack rather than live webpage content injection.

- **Connects to:**  
  S5.2 grounding, WebInject, GUI safety, model supply-chain security.

- **Use in thesis:**  
  backdoor attack targeting GUI-agent visual grounding

---

## Detailed notes

- Targets the plan-to-coordinate grounding mechanism.
- Works even when the high-level plan is correct.
- Demonstrates cross-environment transfer such as mobile/web to desktop.
- Important because web agents depend on GUI grounding models.
- Adds supply-chain risk to S7 beyond runtime prompt injection.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
visual-grounding backdoor
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
backdoor attack targeting GUI-agent visual grounding
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Requires poisoning during grounding pretraining or supply-chain model release; it is a training-time attack rather than live webpage content injection.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

VisualTrap contributes to S7 by showing that Shows that poisoning visual-grounding pretraining can cause GUI agents to map correct textual plans to trigger locations rather than intended UI targets. The main result is that VisualTrap can hijack grounding with as little as 5% poisoned data, stealthy invisible triggers, and transfer across GUI environments even after clean fine-tuning. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Requires poisoning during grounding pretraining or supply-chain model release; it is a training-time attack rather than live webpage content injection. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

VisualTrap shows that **Shows that poisoning visual-grounding pretraining can cause GUI agents to map correct textual plans to trigger locations rather than intended UI targets**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@inproceedings{ye2025visualtrap,
  title     = {VisualTrap: A Stealthy Backdoor Attack on GUI Agents via Visual Grounding Manipulation},
  author    = {Ziang Ye, Yang Zhang, Wentao Shi, Xiaoyu You, Fuli Feng, Tat-Seng Chua},
  booktitle = {COLM 2025},
  year      = {2025},
  url       = {https://openreview.net/forum?id=7HPuAkgdVm}
}
```

---

## Source links

- https://openreview.net/forum?id=7HPuAkgdVm


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\28 - WebCloak- Characterizing and Mitigating Threats from LLM-Driven Web Agents as Intelligent Scrapers.md

# WebCloak: Characterizing and Mitigating Threats from LLM-Driven Web Agents as Intelligent Scrapers

## Metadata

- **Short name:** WebCloak
- **Authors:** Xinfeng Li, Tianze Qiu, Yingbin Jin, Lixu Wang, Hanqing Guo, Xiaojun Jia, XiaoFeng Wang, Wei Dong
- **Year used for thesis:** 2026
- **Venue/status:** IEEE Symposium on Security and Privacy 2026
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** agent-as-scraper threat and defense
- **BibTeX key:** `li2026webcloak`
- **Source PDF file:** `2025-10 - WebCloak- Characterizing and Mitigating Threats from LLM-Driven Web Agents as Intelligent Scrapers.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Characterizes LLM-driven web agents as intelligent scrapers and proposes WebCloak, a dual-layer defense using structural obfuscation and semantic labyrinths.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Characterizes LLM-driven web agents as intelligent scrapers and proposes WebCloak, a dual-layer defense using structural obfuscation and semantic labyrinths.

- **Key finding:**  
  On LLMCrawlBench, WebCloak reduces scraping recall of leading LLM-driven scraping agents dramatically while preserving human visual experience.

- **Limitation connected to thesis:**  
  Defense is aimed at content protection and scraping, not general prompt injection or agent task safety.

- **Connects to:**  
  S6 extraction ethics, anti-bot, Permission Manifests, AI Kill Switch.

- **Use in thesis:**  
  website-owner defense against LLM-driven scraping agents

---

## Detailed notes

- Builds LLMCrawlBench with real-world-derived webpages and images.
- Studies LLM-to-script, LLM-native crawlers, and LLM-based web agents.
- Identifies parse-then-interpret as a common weakness of LLM scrapers.
- Shows website owners need defenses that preserve UX while disrupting agent parsing.
- Important for thesis because extraction agents can also become scraping threats.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
agent-as-scraper threat and defense
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
website-owner defense against LLM-driven scraping agents
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Defense is aimed at content protection and scraping, not general prompt injection or agent task safety.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

WebCloak contributes to S7 by showing that Characterizes LLM-driven web agents as intelligent scrapers and proposes WebCloak, a dual-layer defense using structural obfuscation and semantic labyrinths. The main result is that On LLMCrawlBench, WebCloak reduces scraping recall of leading LLM-driven scraping agents dramatically while preserving human visual experience. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Defense is aimed at content protection and scraping, not general prompt injection or agent task safety. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

WebCloak shows that **Characterizes LLM-driven web agents as intelligent scrapers and proposes WebCloak, a dual-layer defense using structural obfuscation and semantic labyrinths**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@inproceedings{li2026webcloak,
  title     = {WebCloak: Characterizing and Mitigating Threats from LLM-Driven Web Agents as Intelligent Scrapers},
  author    = {Xinfeng Li, Tianze Qiu, Yingbin Jin, Lixu Wang, Hanqing Guo, Xiaojun Jia, XiaoFeng Wang, Wei Dong},
  booktitle = {IEEE Symposium on Security and Privacy 2026},
  year      = {2026},
  url       = {https://sp2026.ieee-security.org/accepted-papers.html}
}
```

---

## Source links

- https://sp2026.ieee-security.org/accepted-papers.html


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\29 - DECEPTICON- How Dark Patterns Manipulate Web Agents.md

# DECEPTICON: How Dark Patterns Manipulate Web Agents

## Metadata

- **Short name:** DECEPTICON
- **Authors:** Phil Cuvin, Hao Zhu, Diyi Yang
- **Year used for thesis:** 2026
- **Venue/status:** arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** dark-pattern benchmark
- **BibTeX key:** `cuvin2026decepticon`
- **Source PDF file:** `2026-02 - DECEPTICON- How Dark Patterns Manipulate Web Agents .pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Introduces DECEPTICON, an environment with generated and real-world dark-pattern tasks to measure instruction-following and manipulative UI effectiveness.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Introduces DECEPTICON, an environment with generated and real-world dark-pattern tasks to measure instruction-following and manipulative UI effectiveness.

- **Key finding:**  
  Dark patterns steer state-of-the-art web agents toward malicious outcomes in over 70% of tested tasks, compared with a much lower human average; larger and more reasoning-capable models can be more susceptible.

- **Limitation connected to thesis:**  
  Focused on dark patterns, not the full range of security attacks; generated tasks need careful ecological validity checks.

- **Connects to:**  
  TrickyArena, Dark Patterns Meet GUI Agents, S8 autonomy/user agency.

- **Use in thesis:**  
  large dark-pattern benchmark for web agents

---

## Detailed notes

- Covers sneaking, urgency, misdirection, social proof, obstruction, and forced action.
- Contains generated and in-the-wild splits.
- Finds guardrails and in-context prompting do not consistently mitigate manipulation.
- Important because it treats dark patterns as adversarial web-agent attacks.
- Sharpens S7's UI manipulation subsection.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
dark-pattern benchmark
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
large dark-pattern benchmark for web agents
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Focused on dark patterns, not the full range of security attacks; generated tasks need careful ecological validity checks.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

DECEPTICON contributes to S7 by showing that Introduces DECEPTICON, an environment with generated and real-world dark-pattern tasks to measure instruction-following and manipulative UI effectiveness. The main result is that Dark patterns steer state-of-the-art web agents toward malicious outcomes in over 70% of tested tasks, compared with a much lower human average; larger and more reasoning-capable models can be more susceptible. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Focused on dark patterns, not the full range of security attacks; generated tasks need careful ecological validity checks. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

DECEPTICON shows that **Introduces DECEPTICON, an environment with generated and real-world dark-pattern tasks to measure instruction-following and manipulative UI effectiveness**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{cuvin2026decepticon,
  title   = {DECEPTICON: How Dark Patterns Manipulate Web Agents},
  author  = {Phil Cuvin, Hao Zhu, Diyi Yang},
  journal = {arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check},
  year    = {2026},
  url     = {https://arxiv.org/abs/2512.22894}
}
```

---

## Source links

- https://arxiv.org/abs/2512.22894


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\30 - Permission Manifests for Web Agents.md

# Permission Manifests for Web Agents

## Metadata

- **Short name:** agent-permissions.json
- **Authors:** Lightweight Agent Standards Working Group (LAS-WG), Samuele Marro, Alan Chan, Xinxing Ren, Lewis Hammond, Jesse Wright, Gurjyot Wanga, Tiziano Piccardi, Nuno Campos, Tobin South, Jialin Yu, Sunando Sengupta, Eric Sommerlade, Alex Pentland, Philip Torr, Jiaxin Pei
- **Year used for thesis:** 2026
- **Venue/status:** arXiv position/preprint; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** governance / permission standards
- **BibTeX key:** `marro2026permissionmanifests`
- **Source PDF file:** `2026-01 - Permission Manifests for Web Agents.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Proposes agent-permissions.json, a lightweight manifest through which websites can specify allowed and prohibited agent interactions.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Proposes agent-permissions.json, a lightweight manifest through which websites can specify allowed and prohibited agent interactions.

- **Key finding:**  
  A simple permission manifest could let compliant agents coordinate with websites, reducing blanket blocking while preserving site-owner preferences.

- **Limitation connected to thesis:**  
  Voluntary standards cannot stop malicious agents; adoption incentives and enforcement remain open.

- **Connects to:**  
  WebCloak, AI Kill Switch, S8 legal/ethical deployment.

- **Use in thesis:**  
  position paper proposing robots.txt-style permission manifests for web-agent interactions

---

## Detailed notes

- Extends the spirit of robots.txt to interactive agents.
- Distinguishes compliant from non-compliant agents.
- Can encode action rules, resource rules, API references, and human-confirmation requirements.
- Important governance layer for real-web deployment.
- Complements technical defenses rather than replacing them.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
governance / permission standards
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
position paper proposing robots.txt-style permission manifests for web-agent interactions
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Voluntary standards cannot stop malicious agents; adoption incentives and enforcement remain open.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

agent-permissions.json contributes to S7 by showing that Proposes agent-permissions.json, a lightweight manifest through which websites can specify allowed and prohibited agent interactions. The main result is that A simple permission manifest could let compliant agents coordinate with websites, reducing blanket blocking while preserving site-owner preferences. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Voluntary standards cannot stop malicious agents; adoption incentives and enforcement remain open. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

agent-permissions.json shows that **Proposes agent-permissions.json, a lightweight manifest through which websites can specify allowed and prohibited agent interactions**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{marro2026permissionmanifests,
  title   = {Permission Manifests for Web Agents},
  author  = {Lightweight Agent Standards Working Group (LAS-WG), Samuele Marro, Alan Chan, Xinxing Ren, Lewis Hammond, Jesse Wright, Gurjyot Wanga, Tiziano Piccardi, Nuno Campos, Tobin South, Jialin Yu, Sunando Sengupta, Eric Sommerlade, Alex Pentland, Philip Torr, Jiaxin Pei},
  journal = {arXiv position/preprint; no final peer-reviewed venue confirmed in this check},
  year    = {2026},
  url     = {https://arxiv.org/abs/2601.02371}
}
```

---

## Source links

- https://arxiv.org/abs/2601.02371


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\31 - Poison Once, Exploit Forever- Environment-Injected Memory Poisoning Attacks on Web Agents.md

# Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents

## Metadata

- **Short name:** eTAMP
- **Authors:** Wei Zou, Mingwen Dong, Miguel Romero Calvo, Shuaichen Chang, Jiang Guo, Dongkyu Lee, Xing Niu, Xiaofei Ma, Yanjun Qi, Jiarong Jiang
- **Year used for thesis:** 2026
- **Venue/status:** arXiv preprint / under review; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** environment-injected memory poisoning
- **BibTeX key:** `zou2026poisononce`
- **Source PDF file:** `2026-04 - Poison Once, Exploit Forever- Environment-Injected Memory Poisoning Attacks on Web Agents.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Introduces eTAMP, where one contaminated webpage observation is stored in trajectory memory and later activates on another site/task.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Introduces eTAMP, where one contaminated webpage observation is stored in trajectory memory and later activates on another site/task.

- **Key finding:**  
  eTAMP reaches substantial ASR on modern models, and environmental stress can increase susceptibility by up to 8x.

- **Limitation connected to thesis:**  
  Experiments focus on raw trajectory memory and specific benchmark environments; broader memory architectures require more study.

- **Connects to:**  
  AgentPoison, WebCoach/memory, RedTeamCUA, S8 persistent risk.

- **Use in thesis:**  
  persistent cross-session/cross-site attack on memory-augmented web agents

---

## Detailed notes

- Does not require direct memory access.
- Bypasses simple permission boundaries because the attack activates later when target-site permissions are legitimate.
- Introduces Chaos Monkey stress testing for agents.
- Shows personalization creates durable attack surfaces.
- Critical for any web agent that stores browsing histories or user preferences.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
environment-injected memory poisoning
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
persistent cross-session/cross-site attack on memory-augmented web agents
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Experiments focus on raw trajectory memory and specific benchmark environments; broader memory architectures require more study.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

eTAMP contributes to S7 by showing that Introduces eTAMP, where one contaminated webpage observation is stored in trajectory memory and later activates on another site/task. The main result is that eTAMP reaches substantial ASR on modern models, and environmental stress can increase susceptibility by up to 8x. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Experiments focus on raw trajectory memory and specific benchmark environments; broader memory architectures require more study. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

eTAMP shows that **Introduces eTAMP, where one contaminated webpage observation is stored in trajectory memory and later activates on another site/task**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{zou2026poisononce,
  title   = {Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents},
  author  = {Wei Zou, Mingwen Dong, Miguel Romero Calvo, Shuaichen Chang, Jiang Guo, Dongkyu Lee, Xing Niu, Xiaofei Ma, Yanjun Qi, Jiarong Jiang},
  journal = {arXiv preprint / under review; no final peer-reviewed venue confirmed in this check},
  year    = {2026},
  url     = {https://arxiv.org/abs/2604.02623}
}
```

---

## Source links

- https://arxiv.org/abs/2604.02623


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\32 - SecureWebArena- A Holistic Security Evaluation Benchmark for LVLM-based Web Agents.md

# SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents

## Metadata

- **Short name:** SecureWebArena
- **Authors:** Zonghao Ying, Yangguang Shao, Jianle Gan, Gan Xu, Wenxin Zhang, Quanchen Zou, Junzheng Shi, Zhenfei Yin, Mingchuan Zhang, Aishan Liu, Xianglong Liu
- **Year used for thesis:** 2026
- **Venue/status:** arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** holistic security benchmark
- **BibTeX key:** `ying2026securewebarena`
- **Source PDF file:** `2026-04 - SecureWebArena- A Holistic Security Evaluation Benchmark for LVLM-based Web Agents.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Builds SecureWebArena with realistic simulated environments, six attack vectors, and multi-layer evaluation over reasoning, behavior trajectory, and task outcome.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Builds SecureWebArena with realistic simulated environments, six attack vectors, and multi-layer evaluation over reasoning, behavior trajectory, and task outcome.

- **Key finding:**  
  Experiments on 9 LVLM agents reveal universal vulnerabilities and trade-offs between model specialization and security.

- **Limitation connected to thesis:**  
  Simulated environments improve control but cannot fully capture all live-web dynamics.

- **Connects to:**  
  WASP, SafeArena, RedTeamCUA, WebSP-Eval, S5.1 security benchmarks.

- **Use in thesis:**  
  broad security benchmark across user-level and environment-level manipulations

---

## Detailed notes

- Unifies user-level and environment-level attack sources.
- Covers jailbreak, direct prompt injection, indirect prompt injection, pop-up, distraction, and ad-style attacks.
- Uses multi-layer evaluation beyond success rate.
- Provides a strong benchmark anchor for S7.5.
- Useful when arguing that fragmented security benchmarks are insufficient.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
holistic security benchmark
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
broad security benchmark across user-level and environment-level manipulations
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Simulated environments improve control but cannot fully capture all live-web dynamics.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

SecureWebArena contributes to S7 by showing that Builds SecureWebArena with realistic simulated environments, six attack vectors, and multi-layer evaluation over reasoning, behavior trajectory, and task outcome. The main result is that Experiments on 9 LVLM agents reveal universal vulnerabilities and trade-offs between model specialization and security. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Simulated environments improve control but cannot fully capture all live-web dynamics. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

SecureWebArena shows that **Builds SecureWebArena with realistic simulated environments, six attack vectors, and multi-layer evaluation over reasoning, behavior trajectory, and task outcome**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{ying2026securewebarena,
  title   = {SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents},
  author  = {Zonghao Ying, Yangguang Shao, Jianle Gan, Gan Xu, Wenxin Zhang, Quanchen Zou, Junzheng Shi, Zhenfei Yin, Mingchuan Zhang, Aishan Liu, Xianglong Liu},
  journal = {arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check},
  year    = {2026},
  url     = {https://arxiv.org/abs/2510.10073}
}
```

---

## Source links

- https://arxiv.org/abs/2510.10073


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\33 - WebAgentGuard- A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents.md

# WebAgentGuard: A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents

## Metadata

- **Short name:** WebAgentGuard
- **Authors:** Yulin Chen, Tri Cao, Haoran Li, Yue Liu, Yibo Li, Yufei He, Le Minh Khoi, Yangqiu Song, Shuicheng Yan, Bryan Hooi
- **Year used for thesis:** 2026
- **Venue/status:** arXiv preprint; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** guard model defense
- **BibTeX key:** `chen2026webagentguard`
- **Source PDF file:** `2026-04 - WebAgentGuard- A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Runs a dedicated guard agent in parallel with the web agent, decoupling prompt-injection detection from task-completion reasoning.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Runs a dedicated guard agent in parallel with the web agent, decoupling prompt-injection detection from task-completion reasoning.

- **Key finding:**  
  WebAgentGuard achieves high recall across crafted and out-of-domain benchmarks while preserving WebArena utility and not adding agent-step latency.

- **Limitation connected to thesis:**  
  White-box attacks against the guard are not considered; synthetic training data may not cover all real-world prompt-injection styles.

- **Connects to:**  
  WAInjectBench, Instruction Hierarchy, AI Kill Switch, S8 defense architecture.

- **Use in thesis:**  
  dedicated multimodal guard model for web-agent prompt injection detection

---

## Detailed notes

- Uses screenshots and processed HTML as guard inputs.
- Builds synthetic multimodal training data spanning topics and design styles.
- Cold-starts with reasoning SFT then refines with GRPO.
- Action gateway blocks execution unless guard or user approves.
- Strong defense candidate for S7.6 but not a complete security architecture.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
guard model defense
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
dedicated multimodal guard model for web-agent prompt injection detection
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
White-box attacks against the guard are not considered; synthetic training data may not cover all real-world prompt-injection styles.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

WebAgentGuard contributes to S7 by showing that Runs a dedicated guard agent in parallel with the web agent, decoupling prompt-injection detection from task-completion reasoning. The main result is that WebAgentGuard achieves high recall across crafted and out-of-domain benchmarks while preserving WebArena utility and not adding agent-step latency. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, White-box attacks against the guard are not considered; synthetic training data may not cover all real-world prompt-injection styles. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

WebAgentGuard shows that **Runs a dedicated guard agent in parallel with the web agent, decoupling prompt-injection detection from task-completion reasoning**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{chen2026webagentguard,
  title   = {WebAgentGuard: A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents},
  author  = {Yulin Chen, Tri Cao, Haoran Li, Yue Liu, Yibo Li, Yufei He, Le Minh Khoi, Yangqiu Song, Shuicheng Yan, Bryan Hooi},
  journal = {arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year    = {2026},
  url     = {https://arxiv.org/abs/2604.12284}
}
```

---

## Source links

- https://arxiv.org/abs/2604.12284


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\34 - WebSP-Eval- Evaluating Web Agents on Website Security and Privacy Tasks.md

# WebSP-Eval: Evaluating Web Agents on Website Security and Privacy Tasks

## Metadata

- **Short name:** WebSP-Eval
- **Authors:** Guruprasad Viswanathan Ramesh, Asmit Nayak, Basieem Siddique, Kassem Fawaz
- **Year used for thesis:** 2026
- **Venue/status:** arXiv preprint; no final peer-reviewed venue confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** security/privacy task benchmark
- **BibTeX key:** `ramesh2026webspeval`
- **Source PDF file:** `2026-04 - WebSP-Eval- Evaluating Web Agents on Website Security and Privacy Tasks.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Introduces a benchmark for tasks such as cookie preference management, privacy settings, and session revocation across live websites.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Introduces a benchmark for tasks such as cookie preference management, privacy settings, and session revocation across live websites.

- **Key finding:**  
  Agents struggle with autonomous exploration and stateful UI elements such as toggles and checkboxes, which fail at high rates in many models.

- **Limitation connected to thesis:**  
  Evaluates protective user tasks rather than adversarial attacks; live-site state management remains technically challenging.

- **Connects to:**  
  S6 extraction privacy, S8 deployment, secure user workflows.

- **Use in thesis:**  
  benchmark for whether web agents can perform user-facing website security/privacy tasks

---

## Detailed notes

- Includes 200 task instances across 28 websites.
- Uses account and initial-state management with a custom Chrome extension.
- Distinguishes performance with and without explicit navigation hints.
- Shows that security/privacy tasks require state comprehension, not just navigation.
- Important for thesis because web agents may be asked to manage privacy settings.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
security/privacy task benchmark
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
benchmark for whether web agents can perform user-facing website security/privacy tasks
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Evaluates protective user tasks rather than adversarial attacks; live-site state management remains technically challenging.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

WebSP-Eval contributes to S7 by showing that Introduces a benchmark for tasks such as cookie preference management, privacy settings, and session revocation across live websites. The main result is that Agents struggle with autonomous exploration and stateful UI elements such as toggles and checkboxes, which fail at high rates in many models. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Evaluates protective user tasks rather than adversarial attacks; live-site state management remains technically challenging. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

WebSP-Eval shows that **Introduces a benchmark for tasks such as cookie preference management, privacy settings, and session revocation across live websites**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@article{ramesh2026webspeval,
  title   = {WebSP-Eval: Evaluating Web Agents on Website Security and Privacy Tasks},
  author  = {Guruprasad Viswanathan Ramesh, Asmit Nayak, Basieem Siddique, Kassem Fawaz},
  journal = {arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year    = {2026},
  url     = {https://arxiv.org/abs/2604.06367}
}
```

---

## Source links

- https://arxiv.org/abs/2604.06367


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\35 - AI Kill Switch for Malicious Web-based LLM Agents.md

# AI Kill Switch for Malicious Web-based LLM Agents

## Metadata

- **Short name:** AutoGuard / AI Kill Switch
- **Authors:** Sechan Lee, Sangdon Park
- **Year used for thesis:** 2026
- **Venue/status:** arXiv preprint / OpenReview ICLR 2026 under-review entry; no final acceptance confirmed in this check
- **Venue/status check:** re-checked from paper first page and public web sources where available
- **Priority:** S7 P1
- **S7 cluster:** defense against malicious web agents
- **BibTeX key:** `lee2026aikillswitch`
- **Source PDF file:** `2026-01 - AI Kill Switch for malicious web-based LLM agent.pdf`

---

## Simple understanding

This paper belongs to **S7 — Security, Robustness, and Trustworthiness**.

The central idea is:

```text
Proposes AutoGuard, which embeds invisible defensive prompts in the DOM to trigger malicious agents' own safety mechanisms and halt harmful tasks.
```

For your thesis, this paper helps explain one part of the security stack for LLM-based web agents: malicious web content, prompt injection, dark patterns, memory poisoning, red-teaming, agent misuse, governance, or runtime defenses.

---

## Four-note template

- **Core idea:**  
  Proposes AutoGuard, which embeds invisible defensive prompts in the DOM to trigger malicious agents' own safety mechanisms and halt harmful tasks.

- **Key finding:**  
  AutoGuard reports high defense success across malicious-agent scenarios such as PII collection, divisive content generation, and web hacking.

- **Limitation connected to thesis:**  
  Relies on the malicious agent reading and complying with safety-trigger prompts; adaptive non-compliant agents may bypass it.

- **Connects to:**  
  WebCloak, Permission Manifests, HackWorld, S8 AI control.

- **Use in thesis:**  
  website-side defensive prompt mechanism to halt malicious web-based LLM agents

---

## Detailed notes

- Frames website owners as defenders against malicious agents.
- Uses defensive prompt generation rather than traditional bot detection.
- Invisible to humans but visible to agent crawlers/parsers.
- Raises the attacker's cost by making low-effort automated misuse harder.
- Complements WebCloak but focuses on safety refusal rather than anti-scraping obfuscation.

---

## Threat model / safety model

Use this paper under the following S7 attacker-model lens:

```text
defense against malicious web agents
```

The important question is:

```text
Who is malicious?
- the webpage/environment?
- the user?
- the agent itself?
- the agent's memory or model supply chain?
- the website owner defending against malicious agents?
```

This paper helps answer that question by clarifying one concrete attack or defense pathway.

---

## Thesis relevance

For **LLM-based agents for generalized web automation and data extraction**, this paper matters because a web agent must not only complete tasks. It must also:

```text
- distinguish trusted user intent from untrusted webpage content
- avoid leaking private data
- avoid unsafe or unauthorized actions
- resist deceptive UI and visual manipulation
- handle adversarial or poisoned memory
- respect site-owner and user permissions
- preserve provenance and auditability
- remain robust under real web deployment constraints
```

The specific relevance of this paper is:

```text
website-side defensive prompt mechanism to halt malicious web-based LLM agents
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Relies on the malicious agent reading and complying with safety-trigger prompts; adaptive non-compliant agents may bypass it.
```

Use this limitation to support the S7 gap:

```text
Current web-agent security research exposes many attack vectors,
but no unified architecture yet provides robust protection across:
malicious webpage content,
visual and DOM-level manipulation,
dark patterns,
privacy leakage,
memory poisoning,
agent misuse,
permission governance,
and safe deployment.
```

---

## Cross-links

| Thesis section | Connection |
|---|---|
| **S5.1** | security benchmarks and evaluation realism |
| **S5.2** | visual/DOM/a11y representation as an attack surface |
| **S5.3** | planning and action execution under adversarial conditions |
| **S5.4** | training or fine-tuning safer agents and guards |
| **S5.5** | reliability/failure modes exposed by security stress tests |
| **S6** | extraction privacy, scraping misuse, provenance, and source trust |
| **S8** | deployment governance, legal/ethical constraints, permission systems |

---

## Thesis-ready paragraph

AutoGuard / AI Kill Switch contributes to S7 by showing that Proposes AutoGuard, which embeds invisible defensive prompts in the DOM to trigger malicious agents' own safety mechanisms and halt harmful tasks. The main result is that AutoGuard reports high defense success across malicious-agent scenarios such as PII collection, divisive content generation, and web hacking. This is important for the thesis because generalized web automation and web data extraction must operate on an adversarial, dynamic, and partially trusted web. However, Relies on the malicious agent reading and complying with safety-trigger prompts; adaptive non-compliant agents may bypass it. Therefore, this paper should be used as evidence that web-agent security must be treated as a system-level property involving representation, planning, memory, permissions, monitoring, and verification.

---

## One-sentence summary

AutoGuard / AI Kill Switch shows that **Proposes AutoGuard, which embeds invisible defensive prompts in the DOM to trigger malicious agents' own safety mechanisms and halt harmful tasks**, but robust web-agent deployment still requires unified defenses across representation, action control, privacy, memory, and governance.

---

## BibTeX

```bibtex
@inproceedings{lee2026aikillswitch,
  title     = {AI Kill Switch for Malicious Web-based LLM Agents},
  author    = {Sechan Lee, Sangdon Park},
  booktitle = {arXiv preprint / OpenReview ICLR 2026 under-review entry; no final acceptance confirmed in this check},
  year      = {2026},
  url       = {https://arxiv.org/abs/2511.13725}
}
```

---

## Source links

- https://arxiv.org/abs/2511.13725


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\S7_P1_reading_index_and_venue_status.md

# S7 P1 — Reading Index and Venue/Status Check

## Corpus status

```text
S7 P0 = 0
S7 P1 expected = 35 papers
S7 P1 processed = 35 papers
Duplicates removed = 0
```

## Important overlap note

The dark-pattern papers are **not duplicates**:

```text
Dark Patterns Meet GUI Agents
→ human/agent/supervised-agent empirical study

Investigating the Impact of Dark Patterns on LLM-Based Web Agents
→ LiteAgent + TrickyArena controlled security benchmark, IEEE S&P 2026

DECEPTICON
→ 700-task generated + real-world dark-pattern environment
```

They should be grouped together, not merged.

## Reading order

| # | Year | Paper | Venue/status | BibTeX key | Cluster |
|---:|---:|---|---|---|---|
| 1 | 2023 | AgentMonitor / Safe Testing in the Wild | arXiv / OpenReview preprint; no final peer-reviewed venue confirmed in this check | `naihin2023testingagentswild` | safe testing and monitoring |
| 2 | 2024 | AdvAgent | arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check | `xu2024advagent` | black-box red-teaming |
| 3 | 2025 | Pop-up Attack | ACL 2025 Long Papers | `zhang2025popupattack` | visual distraction / pop-up attack |
| 4 | 2024 | WIPI | arXiv preprint; no final peer-reviewed venue confirmed in this check | `wu2024wipi` | early web indirect prompt injection |
| 5 | 2024 | AgentPoison | NeurIPS 2024 conference paper | `chen2024agentpoison` | memory / RAG knowledge-base poisoning |
| 6 | 2024 | InjecAgent | Findings of ACL 2024 | `zhan2024injecagent` | tool-agent indirect prompt injection benchmark |
| 7 | 2024 | BrowserART / Refusal-Trained Agents | arXiv preprint / ICLR 2025 related presentation; no main-conference final venue confirmed in this check | `kumar2024browserart` | refusal transfer failure |
| 8 | 2024 | Instruction Hierarchy | arXiv / OpenReview preprint; no final peer-reviewed venue confirmed in this check | `wallace2024instructionhierarchy` | instruction priority defense |
| 9 | 2025 | CUA Safety Survey | arXiv survey preprint | `chen2025cuasafetysurvey` | survey |
| 10 | 2025 | AdInject | arXiv preprint; no final peer-reviewed venue confirmed in this check | `wang2025adinject` | advertising-delivery environmental attack |
| 11 | 2025 | Cross-Modal Preference Steering / CPS | arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check | `jiang2025cps` | preference manipulation |
| 12 | 2025 | EIA | ICLR 2025 conference paper | `liao2025eia` | privacy leakage via environmental injection |
| 13 | 2026 | LiteAgent / TrickyArena | IEEE Symposium on Security and Privacy 2026 | `ersoy2026darkpatternswebagents` | dark patterns benchmark |
| 14 | 2025 | A11y-tree IPI | arXiv preprint; no final peer-reviewed venue confirmed in this check | `johnson2025a11yipi` | accessibility-tree prompt injection |
| 15 | 2025 | Mind the Web | arXiv preprint; no final peer-reviewed venue confirmed in this check | `shapira2025mindweb` | task-aligned injection / web-use agent security |
| 16 | 2026 | RedTeamCUA / RTC-Bench | ICLR 2026 conference paper | `liao2026redteamcua` | hybrid web-OS adversarial benchmark |
| 17 | 2025 | SafeArena | arXiv / OpenReview preprint; no final peer-reviewed venue confirmed in this check | `tur2025safearena` | deliberate misuse benchmark |
| 18 | 2025 | WAInjectBench | arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check | `liu2025wainjectbench` | prompt-injection detection benchmark |
| 19 | 2025 | WASP | arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check | `evtimov2025wasp` | web-agent prompt-injection benchmark |
| 20 | 2025 | WebInject | arXiv preprint; no final peer-reviewed venue confirmed in this check | `wang2025webinject` | pixel-space webpage attack |
| 21 | 2025 | Web Agents Vulnerability Analysis | Building Trust Workshop at ICLR 2025 + arXiv preprint | `chiang2025webagentsvulnerable` | component-level vulnerability analysis |
| 22 | 2025 | SUDO / DETOX2TOX | arXiv preprint; no final peer-reviewed venue confirmed in this check | `lee2025sudo` | computer-use refusal bypass |
| 23 | 2025 | Autonomy-Induced Security Risks Survey | arXiv survey/manuscript formatted as IEEE TPAMI; no final journal issue confirmed in this check | `su2025autonomyrisks` | survey / autonomy risk |
| 24 | 2025 | Dark Patterns Meet GUI Agents | arXiv preprint; no final peer-reviewed venue confirmed in this check | `tang2025darkpatterns` | dark patterns and human oversight |
| 25 | 2025 | HackWorld | arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check | `ren2025hackworld` | web application vulnerability exploitation |
| 26 | 2025 | Agent Red Teaming / ART | Preprint / under review; no final peer-reviewed venue confirmed in this check | `zou2025agentredteaming` | large-scale public red-teaming |
| 27 | 2025 | VisualTrap | COLM 2025 conference paper | `ye2025visualtrap` | visual-grounding backdoor |
| 28 | 2026 | WebCloak | IEEE Symposium on Security and Privacy 2026 | `li2026webcloak` | agent-as-scraper threat and defense |
| 29 | 2026 | DECEPTICON | arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check | `cuvin2026decepticon` | dark-pattern benchmark |
| 30 | 2026 | agent-permissions.json | arXiv position/preprint; no final peer-reviewed venue confirmed in this check | `marro2026permissionmanifests` | governance / permission standards |
| 31 | 2026 | eTAMP | arXiv preprint / under review; no final peer-reviewed venue confirmed in this check | `zou2026poisononce` | environment-injected memory poisoning |
| 32 | 2026 | SecureWebArena | arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check | `ying2026securewebarena` | holistic security benchmark |
| 33 | 2026 | WebAgentGuard | arXiv preprint; no final peer-reviewed venue confirmed in this check | `chen2026webagentguard` | guard model defense |
| 34 | 2026 | WebSP-Eval | arXiv preprint; no final peer-reviewed venue confirmed in this check | `ramesh2026webspeval` | security/privacy task benchmark |
| 35 | 2026 | AutoGuard / AI Kill Switch | arXiv preprint / OpenReview ICLR 2026 under-review entry; no final acceptance confirmed in this check | `lee2026aikillswitch` | defense against malicious web agents |

## Main S7 P1 taxonomy

```text
1. Safe testing and monitoring
   - Testing Language Model Agents Safely in the Wild

2. Indirect prompt injection and malicious web content
   - WIPI
   - InjecAgent
   - EIA
   - WASP
   - WebInject
   - A11y-tree IPI
   - Mind the Web
   - WAInjectBench
   - WebAgentGuard

3. Visual, GUI, and content manipulation
   - Pop-up Attack
   - AdInject
   - Cross-Modal Preference Steering
   - VisualTrap

4. Dark patterns and manipulative UI
   - Dark Patterns Meet GUI Agents
   - Investigating Dark Patterns
   - DECEPTICON

5. Memory and persistent attacks
   - AgentPoison
   - Poison Once, Exploit Forever

6. Agent misuse and dangerous autonomy
   - BrowserART / Refusal-Trained Browser Agents
   - SafeArena
   - HackWorld
   - AI Kill Switch

7. Holistic red-teaming and benchmarks
   - Security Challenges in AI Agent Deployment
   - RedTeamCUA
   - SecureWebArena
   - WebSP-Eval

8. Governance and standards
   - Instruction Hierarchy
   - Permission Manifests
   - CUA and autonomy-risk surveys
```

## Final S7 P1 conclusion

```text
S7 P1 shows that web-agent security is not a single prompt-injection problem.
It is a layered system problem involving webpage content, UI design, visual grounding,
memory, tool/action execution, privacy, scraping misuse, permissions, monitoring, and governance.
```


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\P1\S7_P1_venue_status_report.md

# S7 P1 — Venue / Status Report

## Final status table

| Paper | Venue/status used | Public source |
|---|---|---|
| AgentMonitor / Safe Testing in the Wild | arXiv / OpenReview preprint; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2311.10538 |
| AdvAgent | arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check | https://arxiv.org/abs/2410.17401 |
| Pop-up Attack | ACL 2025 Long Papers | https://aclanthology.org/2025.acl-long.411/ |
| WIPI | arXiv preprint; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2402.16965 |
| AgentPoison | NeurIPS 2024 conference paper | https://papers.nips.cc/paper_files/paper/2024/hash/eb113910e9c3f6242541c1652e30dfd6-Abstract-Conference.html |
| InjecAgent | Findings of ACL 2024 | https://aclanthology.org/2024.findings-acl.624/ |
| BrowserART / Refusal-Trained Agents | arXiv preprint / ICLR 2025 related presentation; no main-conference final venue confirmed in this check | https://arxiv.org/abs/2410.13886 |
| Instruction Hierarchy | arXiv / OpenReview preprint; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2404.13208 |
| CUA Safety Survey | arXiv survey preprint | https://arxiv.org/abs/2505.10924 |
| AdInject | arXiv preprint; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2505.21499 |
| Cross-Modal Preference Steering / CPS | arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check | https://arxiv.org/abs/2510.03612 |
| EIA | ICLR 2025 conference paper | https://openreview.net/forum?id=xMOLUzo2Lk |
| LiteAgent / TrickyArena | IEEE Symposium on Security and Privacy 2026 | https://sp2026.ieee-security.org/accepted-papers.html |
| A11y-tree IPI | arXiv preprint; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2507.14799 |
| Mind the Web | arXiv preprint; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2506.07153 |
| RedTeamCUA / RTC-Bench | ICLR 2026 conference paper | https://openreview.net/forum?id=yWwrgcBoK3 |
| SafeArena | arXiv / OpenReview preprint; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2503.04957 |
| WAInjectBench | arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check | https://arxiv.org/abs/2510.01354 |
| WASP | arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check | https://arxiv.org/abs/2504.18575 |
| WebInject | arXiv preprint; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2503.19786 |
| Web Agents Vulnerability Analysis | Building Trust Workshop at ICLR 2025 + arXiv preprint | https://arxiv.org/abs/2502.20383 |
| SUDO / DETOX2TOX | arXiv preprint; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2503.XXX |
| Autonomy-Induced Security Risks Survey | arXiv survey/manuscript formatted as IEEE TPAMI; no final journal issue confirmed in this check | https://arxiv.org/abs/2506.23844 |
| Dark Patterns Meet GUI Agents | arXiv preprint; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2509.10723 |
| HackWorld | arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check | https://arxiv.org/abs/2510.12200 |
| Agent Red Teaming / ART | Preprint / under review; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2507.20526 |
| VisualTrap | COLM 2025 conference paper | https://openreview.net/forum?id=7HPuAkgdVm |
| WebCloak | IEEE Symposium on Security and Privacy 2026 | https://sp2026.ieee-security.org/accepted-papers.html |
| DECEPTICON | arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check | https://arxiv.org/abs/2512.22894 |
| agent-permissions.json | arXiv position/preprint; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2601.02371 |
| eTAMP | arXiv preprint / under review; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2604.02623 |
| SecureWebArena | arXiv preprint / OpenReview entry; no final accepted venue confirmed in this check | https://arxiv.org/abs/2510.10073 |
| WebAgentGuard | arXiv preprint; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2604.12284 |
| WebSP-Eval | arXiv preprint; no final peer-reviewed venue confirmed in this check | https://arxiv.org/abs/2604.06367 |
| AutoGuard / AI Kill Switch | arXiv preprint / OpenReview ICLR 2026 under-review entry; no final acceptance confirmed in this check | https://arxiv.org/abs/2511.13725 |

## Confirmed final venues found

```text
InjecAgent → Findings of ACL 2024
AgentPoison → NeurIPS 2024
EIA → ICLR 2025
Attacking VLM Agents via Pop-ups → ACL 2025 Long Papers
VisualTrap → COLM 2025
RedTeamCUA → ICLR 2026
Investigating the Impact of Dark Patterns on LLM-Based Web Agents → IEEE S&P 2026
WebCloak → IEEE S&P 2026
```

## Preprint / workshop / under-review statuses

For papers where no final proceedings or journal venue was confirmed, the note keeps a conservative status:

```text
arXiv preprint
OpenReview entry
workshop/preprint
under review
```

These should be rechecked once more before final thesis bibliography export.


---

## Synthesis / Writing Notes (1 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\Writing\S7_P1_full_refined_synthesis.md

# S7 P1 Refined Synthesis — Security, Robustness, and Trustworthiness

## 1. Purpose of S7

S7 answers the question:

```text
Can LLM-based web agents be trusted to act safely on the real web?
```

The answer from the P1 literature is:

```text
not yet.
```

The S7 P1 corpus shows that web-agent security is not one problem. It is a stack of interacting vulnerabilities:

```text
prompt injection
indirect prompt injection
visual manipulation
dark patterns
privacy leakage
memory poisoning
malicious user requests
malicious agent misuse
scraping misuse
weak permission systems
weak monitoring and guardrails
```

There is no S7 P0 paper because the section is not centered on one canonical method. It is a threat-model section.

---

## 2. Corrected S7 P1 corpus status

```text
S7 P0 = 0
S7 P1 = 35 papers
Duplicates = 0
```

Important overlap:

```text
Dark Patterns Meet GUI Agents
Investigating the Impact of Dark Patterns on LLM-Based Web Agents
DECEPTICON
```

These are not duplicates. They cover the same broad phenomenon but with different study designs and roles.

---

## 3. S7 taxonomy by attacker model

## 3.1 What the web does to the agent

This is the largest S7 cluster.

It includes:

```text
WIPI
InjecAgent
EIA
WASP
WebInject
A11y-tree IPI
Mind the Web
WAInjectBench
WebAgentGuard
RedTeamCUA
SecureWebArena
```

The central idea is:

```text
webpage content is untrusted input, but web agents often treat it as task-relevant instruction.
```

The web can attack the agent through:

```text
visible text
HTML/DOM
accessibility tree
screenshots
pixel perturbations
pop-ups
ads
comments
reviews
forum posts
task-aligned fake guidance
```

The important thesis conclusion is:

```text
a web agent must separate user intent from webpage content.
```

This is harder than normal prompt filtering because the webpage is simultaneously:

```text
the task environment
the data source
the observation stream
the attack surface
```

---

## 3.2 What the user or attacker makes the agent do

This cluster includes:

```text
BrowserART / Refusal-Trained Browser Agents
SafeArena
HackWorld
Security Challenges in AI Agent Deployment
AI Kill Switch
```

The core lesson is:

```text
even if the base LLM refuses harmful chat requests,
the same model wrapped as an agent may attempt harmful browser actions.
```

Risks include:

```text
misinformation posting
illegal transactions
cybercrime
web vulnerability exploitation
unauthorized data access
policy violations
unsafe tool use
```

This matters because web agents are not only text generators. They can act.

For the thesis, the implication is:

```text
security must be enforced at the action layer, not only the language layer.
```

---

## 3.3 Visual and GUI manipulation

This cluster includes:

```text
Pop-up Attack
WebInject
VisualTrap
AdInject
Cross-Modal Preference Steering
```

The key idea is:

```text
agent perception is attackable.
```

Agents that rely on screenshots, visual grounding, and multimodal content can be manipulated by:

```text
pop-ups
ads
imperceptible visual perturbations
poisoned visual-grounding training data
cross-modal product/listing changes
stealthy visual-textual preference steering
```

This links S7 to S5.2:

```text
representation is not neutral.
```

If the observation format is vulnerable, the planning and action layers will inherit that vulnerability.

---

## 3.4 Dark patterns and manipulative interfaces

This cluster includes:

```text
Dark Patterns Meet GUI Agents
Investigating the Impact of Dark Patterns on LLM-Based Web Agents
DECEPTICON
```

The key finding across the cluster is:

```text
web agents are highly susceptible to manipulative UI designs.
```

This is different from prompt injection. A dark pattern may not contain an obvious malicious instruction. It can manipulate through:

```text
default choices
hidden costs
misdirection
urgency
social proof
obstruction
forced action
trick questions
```

This is thesis-relevant because a generalized web automation agent will meet dark patterns frequently on real websites.

The central lesson is:

```text
security includes user autonomy, not only malware or data leakage.
```

---

## 3.5 Memory poisoning and persistent attacks

This cluster includes:

```text
AgentPoison
Poison Once, Exploit Forever
```

The main lesson is:

```text
agent memory turns one-time exposure into long-term vulnerability.
```

AgentPoison studies poisoning memory or RAG knowledge bases.

Poison Once, Exploit Forever goes further by showing environment-injected trajectory memory poisoning:

```text
one contaminated webpage observation
→ stored in memory
→ retrieved later
→ activates on a different website or task
```

This is critical for web agents because personalization and memory are often proposed as ways to improve web-agent generalization.

The S7 implication is:

```text
memory improves capability, but also expands the attack surface across sessions and websites.
```

---

## 3.6 Defenses, governance, and permission systems

This cluster includes:

```text
Instruction Hierarchy
Testing Language Model Agents Safely in the Wild
WebAgentGuard
Permission Manifests
AI Kill Switch
WebCloak
```

The defense landscape is still fragmented.

Current defense ideas include:

```text
instruction-priority training
runtime monitors
dedicated guard models
website permission manifests
DOM-embedded defensive prompts
structural obfuscation against scrapers
human approval
action gateways
least privilege
```

The key limitation is:

```text
no defense covers all attack channels.
```

For example:

```text
Instruction Hierarchy helps with instruction conflict,
but not visual perturbation or poisoned grounding.

WebAgentGuard detects prompt injection,
but may not cover all adaptive attacks.

Permission Manifests help compliant agents,
but not malicious non-compliant agents.

WebCloak protects website assets from scraping,
but does not secure the user's agent.

AI Kill Switch exploits agents' own safety mechanisms,
but may fail against agents that ignore safety triggers.
```

---

## 4. Main S7 thesis gap

The S7 gap is:

```text
Current web-agent security research identifies many vulnerabilities,
but there is no unified architecture that jointly handles:
- untrusted webpage content,
- prompt injection,
- visual and DOM attacks,
- dark patterns,
- privacy leakage,
- malicious user requests,
- agent misuse against websites,
- scraping misuse,
- memory poisoning,
- action authorization,
- permission compliance,
- monitoring,
- and provenance-preserving extraction.
```

For the thesis, this should connect directly to S6 and S8:

```text
an extraction-capable web agent must be secure because extraction often involves
private data, site policies, untrusted pages, and potentially adversarial content.
```

---

## 5. Thesis-ready S7 synthesis paragraph

The S7 P1 literature shows that security, robustness, and trustworthiness are now central barriers to deploying LLM-based web agents. Early work such as WIPI, InjecAgent, and EIA demonstrates that web agents are vulnerable to indirect prompt injection because webpage content is processed as part of the agent’s observation and reasoning context. Later benchmarks such as WASP, WAInjectBench, RedTeamCUA, and SecureWebArena broaden this into executable and multimodal security evaluation, covering text, HTML, screenshots, pop-ups, and hybrid web–OS attack paths. Visual attacks such as Pop-up Attack, WebInject, VisualTrap, AdInject, and Cross-Modal Preference Steering show that the agent’s perceptual layer is itself an attack surface: screenshots, visual grounding, ads, product thumbnails, and metadata can all manipulate agent actions. A separate line of work on dark patterns—Dark Patterns Meet GUI Agents, TrickyArena, and DECEPTICON—shows that agents are also vulnerable to manipulative interface design even without explicit malicious prompt text. Memory attacks such as AgentPoison and Poison Once, Exploit Forever reveal that agent memory can convert a single exposure into persistent cross-session compromise. In parallel, SafeArena, BrowserART, HackWorld, and public red-teaming studies show that agents can be misused to perform unsafe actions, violate policies, or attempt web exploitation. Defense papers such as Instruction Hierarchy, AgentMonitor, WebAgentGuard, Permission Manifests, WebCloak, and AI Kill Switch propose partial mitigations, but none provides complete coverage across all attack surfaces. The resulting thesis gap is clear: generalized web automation and data extraction require a security architecture that separates trusted user intent from untrusted web content, validates actions before execution, protects memory, preserves provenance, respects permissions, and remains robust to visual, textual, and interface-level manipulation.

---

## 6. Cross-links to later sections

| Cluster | Feeds |
|---|---|
| Prompt injection / IPI | S8 security obstacle; S6 source trust |
| Visual manipulation | S5.2 representation risk; S5.5 failure modes |
| Dark patterns | S8 user autonomy and safe deployment |
| Memory poisoning | S5.4 memory/self-improvement; S8 persistent risk |
| Agent misuse | S8 governance and permission systems |
| WebCloak / Permission Manifests | S6 scraping/access-control/legal constraints |
| WebAgentGuard / AI Kill Switch | S8 defense architecture |
| WebSP-Eval | S8 privacy/security task evaluation |

---

## 7. Final S7 conclusion

```text
S7 shows that secure web agents require more than better prompts.
They require a full trust architecture:
trusted instruction hierarchy,
untrusted-content isolation,
multimodal injection detection,
permission-aware action control,
memory sanitation,
source provenance,
human approval for sensitive actions,
and deployment governance.
```


---

## Synthesis / Writing Notes (1 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S7\writing\S7_P1_full_refined_synthesis.md

# S7 P1 Refined Synthesis — Security, Robustness, and Trustworthiness

## 1. Purpose of S7

S7 answers the question:

```text
Can LLM-based web agents be trusted to act safely on the real web?
```

The answer from the P1 literature is:

```text
not yet.
```

The S7 P1 corpus shows that web-agent security is not one problem. It is a stack of interacting vulnerabilities:

```text
prompt injection
indirect prompt injection
visual manipulation
dark patterns
privacy leakage
memory poisoning
malicious user requests
malicious agent misuse
scraping misuse
weak permission systems
weak monitoring and guardrails
```

There is no S7 P0 paper because the section is not centered on one canonical method. It is a threat-model section.

---

## 2. Corrected S7 P1 corpus status

```text
S7 P0 = 0
S7 P1 = 35 papers
Duplicates = 0
```

Important overlap:

```text
Dark Patterns Meet GUI Agents
Investigating the Impact of Dark Patterns on LLM-Based Web Agents
DECEPTICON
```

These are not duplicates. They cover the same broad phenomenon but with different study designs and roles.

---

## 3. S7 taxonomy by attacker model

## 3.1 What the web does to the agent

This is the largest S7 cluster.

It includes:

```text
WIPI
InjecAgent
EIA
WASP
WebInject
A11y-tree IPI
Mind the Web
WAInjectBench
WebAgentGuard
RedTeamCUA
SecureWebArena
```

The central idea is:

```text
webpage content is untrusted input, but web agents often treat it as task-relevant instruction.
```

The web can attack the agent through:

```text
visible text
HTML/DOM
accessibility tree
screenshots
pixel perturbations
pop-ups
ads
comments
reviews
forum posts
task-aligned fake guidance
```

The important thesis conclusion is:

```text
a web agent must separate user intent from webpage content.
```

This is harder than normal prompt filtering because the webpage is simultaneously:

```text
the task environment
the data source
the observation stream
the attack surface
```

---

## 3.2 What the user or attacker makes the agent do

This cluster includes:

```text
BrowserART / Refusal-Trained Browser Agents
SafeArena
HackWorld
Security Challenges in AI Agent Deployment
AI Kill Switch
```

The core lesson is:

```text
even if the base LLM refuses harmful chat requests,
the same model wrapped as an agent may attempt harmful browser actions.
```

Risks include:

```text
misinformation posting
illegal transactions
cybercrime
web vulnerability exploitation
unauthorized data access
policy violations
unsafe tool use
```

This matters because web agents are not only text generators. They can act.

For the thesis, the implication is:

```text
security must be enforced at the action layer, not only the language layer.
```

---

## 3.3 Visual and GUI manipulation

This cluster includes:

```text
Pop-up Attack
WebInject
VisualTrap
AdInject
Cross-Modal Preference Steering
```

The key idea is:

```text
agent perception is attackable.
```

Agents that rely on screenshots, visual grounding, and multimodal content can be manipulated by:

```text
pop-ups
ads
imperceptible visual perturbations
poisoned visual-grounding training data
cross-modal product/listing changes
stealthy visual-textual preference steering
```

This links S7 to S5.2:

```text
representation is not neutral.
```

If the observation format is vulnerable, the planning and action layers will inherit that vulnerability.

---

## 3.4 Dark patterns and manipulative interfaces

This cluster includes:

```text
Dark Patterns Meet GUI Agents
Investigating the Impact of Dark Patterns on LLM-Based Web Agents
DECEPTICON
```

The key finding across the cluster is:

```text
web agents are highly susceptible to manipulative UI designs.
```

This is different from prompt injection. A dark pattern may not contain an obvious malicious instruction. It can manipulate through:

```text
default choices
hidden costs
misdirection
urgency
social proof
obstruction
forced action
trick questions
```

This is thesis-relevant because a generalized web automation agent will meet dark patterns frequently on real websites.

The central lesson is:

```text
security includes user autonomy, not only malware or data leakage.
```

---

## 3.5 Memory poisoning and persistent attacks

This cluster includes:

```text
AgentPoison
Poison Once, Exploit Forever
```

The main lesson is:

```text
agent memory turns one-time exposure into long-term vulnerability.
```

AgentPoison studies poisoning memory or RAG knowledge bases.

Poison Once, Exploit Forever goes further by showing environment-injected trajectory memory poisoning:

```text
one contaminated webpage observation
→ stored in memory
→ retrieved later
→ activates on a different website or task
```

This is critical for web agents because personalization and memory are often proposed as ways to improve web-agent generalization.

The S7 implication is:

```text
memory improves capability, but also expands the attack surface across sessions and websites.
```

---

## 3.6 Defenses, governance, and permission systems

This cluster includes:

```text
Instruction Hierarchy
Testing Language Model Agents Safely in the Wild
WebAgentGuard
Permission Manifests
AI Kill Switch
WebCloak
```

The defense landscape is still fragmented.

Current defense ideas include:

```text
instruction-priority training
runtime monitors
dedicated guard models
website permission manifests
DOM-embedded defensive prompts
structural obfuscation against scrapers
human approval
action gateways
least privilege
```

The key limitation is:

```text
no defense covers all attack channels.
```

For example:

```text
Instruction Hierarchy helps with instruction conflict,
but not visual perturbation or poisoned grounding.

WebAgentGuard detects prompt injection,
but may not cover all adaptive attacks.

Permission Manifests help compliant agents,
but not malicious non-compliant agents.

WebCloak protects website assets from scraping,
but does not secure the user's agent.

AI Kill Switch exploits agents' own safety mechanisms,
but may fail against agents that ignore safety triggers.
```

---

## 4. Main S7 thesis gap

The S7 gap is:

```text
Current web-agent security research identifies many vulnerabilities,
but there is no unified architecture that jointly handles:
- untrusted webpage content,
- prompt injection,
- visual and DOM attacks,
- dark patterns,
- privacy leakage,
- malicious user requests,
- agent misuse against websites,
- scraping misuse,
- memory poisoning,
- action authorization,
- permission compliance,
- monitoring,
- and provenance-preserving extraction.
```

For the thesis, this should connect directly to S6 and S8:

```text
an extraction-capable web agent must be secure because extraction often involves
private data, site policies, untrusted pages, and potentially adversarial content.
```

---

## 5. Thesis-ready S7 synthesis paragraph

The S7 P1 literature shows that security, robustness, and trustworthiness are now central barriers to deploying LLM-based web agents. Early work such as WIPI, InjecAgent, and EIA demonstrates that web agents are vulnerable to indirect prompt injection because webpage content is processed as part of the agent’s observation and reasoning context. Later benchmarks such as WASP, WAInjectBench, RedTeamCUA, and SecureWebArena broaden this into executable and multimodal security evaluation, covering text, HTML, screenshots, pop-ups, and hybrid web–OS attack paths. Visual attacks such as Pop-up Attack, WebInject, VisualTrap, AdInject, and Cross-Modal Preference Steering show that the agent’s perceptual layer is itself an attack surface: screenshots, visual grounding, ads, product thumbnails, and metadata can all manipulate agent actions. A separate line of work on dark patterns—Dark Patterns Meet GUI Agents, TrickyArena, and DECEPTICON—shows that agents are also vulnerable to manipulative interface design even without explicit malicious prompt text. Memory attacks such as AgentPoison and Poison Once, Exploit Forever reveal that agent memory can convert a single exposure into persistent cross-session compromise. In parallel, SafeArena, BrowserART, HackWorld, and public red-teaming studies show that agents can be misused to perform unsafe actions, violate policies, or attempt web exploitation. Defense papers such as Instruction Hierarchy, AgentMonitor, WebAgentGuard, Permission Manifests, WebCloak, and AI Kill Switch propose partial mitigations, but none provides complete coverage across all attack surfaces. The resulting thesis gap is clear: generalized web automation and data extraction require a security architecture that separates trusted user intent from untrusted web content, validates actions before execution, protects memory, preserves provenance, respects permissions, and remains robust to visual, textual, and interface-level manipulation.

---

## 6. Cross-links to later sections

| Cluster | Feeds |
|---|---|
| Prompt injection / IPI | S8 security obstacle; S6 source trust |
| Visual manipulation | S5.2 representation risk; S5.5 failure modes |
| Dark patterns | S8 user autonomy and safe deployment |
| Memory poisoning | S5.4 memory/self-improvement; S8 persistent risk |
| Agent misuse | S8 governance and permission systems |
| WebCloak / Permission Manifests | S6 scraping/access-control/legal constraints |
| WebAgentGuard / AI Kill Switch | S8 defense architecture |
| WebSP-Eval | S8 privacy/security task evaluation |

---

## 7. Final S7 conclusion

```text
S7 shows that secure web agents require more than better prompts.
They require a full trust architecture:
trusted instruction hierarchy,
untrusted-content isolation,
multimodal injection detection,
permission-aware action control,
memory sanitation,
source provenance,
human approval for sensitive actions,
and deployment governance.
```


---


Total files merged: 39
