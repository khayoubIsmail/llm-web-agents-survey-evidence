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
