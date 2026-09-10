# S8 P2 Paper 04 — Agent A/B: Automated and Scalable A/B Testing on Live Websites with Interactive LLM Agents

## Metadata

- **Title:** Agent A/B: Automated and Scalable A/B Testing on Live Websites with Interactive LLM Agents
- **Year:** 2025/2026
- **Verified venue/status:** CHI EA 2026 / ACM DOI 10.1145/3772363.3799039
- **Peer-reviewed status:** Yes
- **Thesis section:** S8 — Open Challenges, Deployment, Sustainability, Efficiency, Human-Agent Collaboration, Adoption, and Future Directions
- **Main category:** web-agent-based UX simulation and scalable A/B testing
- **S8 role:** agent-based UX evaluation and scalable A/B testing
- **Priority:** P2
- **Recommended citation strength:** Strong citation
- **Recommended reading depth:** Medium to high
- **BibTeX key:** `bautomatedscalableb2025`

---

## Simple understanding

Agent A/B uses large numbers of persona-driven LLM agents to simulate web A/B tests on live websites. It aims to provide early behavioral evidence before committing real user traffic.

In simple terms:

```text
Problem → Web/GUI agents are moving from benchmarks toward real-world deployment.
Challenge → Deployment introduces issues that are not fully captured by task success alone.
Paper → This work studies one open challenge: runtime, collaboration, energy, latency, usability, adoption, production, interoperability, or values.
Goal → Help define what future web-agent systems must solve beyond benchmark accuracy.
```

For S8, the first goal is to understand **which open challenge the paper represents**.

---

## Core idea

Deploy LLM agents with personas to evaluate alternative interface designs at scale.

This paper mainly contributes to:

```text
web-agent-based UX simulation and scalable A/B testing
```

In the broader S8 pipeline, it fits here:

```text
benchmark success
→ real deployment constraints
→ runtime / cost / latency / energy / values / adoption / collaboration issue
→ future research direction
```

---

## Key finding / main claim

In an Amazon.com case study with 1,000 agents, agent-based outcomes aligned directionally with a parallel human A/B experiment.

For S8, the important question is:

```text
What limitation of current LLM-based web agents does this paper expose, and what direction does it suggest?
```

Typical S8 open-challenge dimensions include:

- safe runtime and post-facto validation,
- human-agent collaboration,
- sustainability and energy consumption,
- latency and system efficiency,
- usability and agentic ROI,
- platform interoperability and walled gardens,
- cross-device orchestration,
- sandboxing and human takeover,
- production measurement and reliability,
- real-world adoption and usage,
- values, preferences, and behavior alignment.

---

## Key evidence to extract from the paper

When reading this paper, extract these evidence points:

- **CHI EA 2026 ACM version.**
- **1,000 agents, 500 per condition.**
- **Reduced filter list produced more purchases and surfaced subgroup patterns.**

Also extract, if available:

- system architecture,
- benchmark or study design,
- number of users/tasks/agents/websites/devices,
- metrics used,
- empirical result,
- design implications,
- and future-work/open-challenge statements.

---

## Limitations

- **Limitation 1:** Agent simulations complement but do not replace human testing.
- **Limitation 2:** Persona fidelity and behavioral realism remain open challenges.
- **Limitation 3:** Live-web evaluation depends on website stability and agent execution reliability.

General thesis-level limitation:

```text
S8 papers often describe frontier challenges rather than mature solutions.
Use them to motivate future research directions, not always as definitive technical answers.
```

---

## Venue/status caution

Use as a stronger source. Verified status: **CHI EA 2026 / ACM DOI 10.1145/3772363.3799039**.

For final thesis writing:

```text
confirmed conference/ACM/AAAI/ACL venue → stronger citation
demo/workshop → useful system evidence
arXiv/technical/working paper → recent direction, cite cautiously
older arXiv version superseded by final version → cite final version only
```

---

## Relation to S8

This paper belongs in **S8** because S8 discusses open challenges and future directions for generalized LLM-based web automation and data extraction.

Its role is:

```text
Agent A/B: Automated and Scalable A/B Testing on Live Websites with Interactive LLM Agents
→ agent-based UX evaluation and scalable A/B testing
→ P2 support for open-challenges/future-directions discussion
```

Use the paper after explaining the challenge first.  
Do not introduce it only as “P2”; introduce the open challenge it supports.

---

## Relation to the thesis topic

Your thesis topic is:

```text
LLM-based agents for generalized web automation and data extraction
```

This paper matters because generalized web automation is not only about completing tasks. It also requires:

```text
safe execution
human intervention
low latency
cost and energy awareness
real-world usability
production reliability
interoperability
adoption evidence
value-sensitive behavior
```

The paper supports that pipeline by improving or analyzing:

```text
agent-based UX evaluation and scalable A/B testing
```

---

## How to use this paper in the literature review

Recommended use:

- Use it as **P2 support** in S8.
- Extract one precise open challenge.
- Extract one quantitative result or design principle.
- Extract one limitation.
- Compare it with nearby S8 papers.
- If it is a preprint/working paper/technical report, phrase claims cautiously.

Suggested thesis sentence:

> Agent A/B: Automated and Scalable A/B Testing on Live Websites with Interactive LLM Agents contributes to S8 by highlighting **web-agent-based UX simulation and scalable A/B testing**, showing that generalized web agents must be evaluated not only by task success but also by deployment constraints such as safety, cost, latency, collaboration, sustainability, production reliability, and user values.

---

## Comparison with nearby S8 papers

Compare this paper with:

```text
GoEX / AgentBay → runtime, sandboxing, and safe execution
CowPilot → human-agent collaboration
Sustainability papers → energy and CO2-aware evaluation
Agentic ROI / Measuring Agents in Production / Adoption study → usability, production, and adoption
What Limits Agentic Systems Efficiency? → latency and system overhead
UFO3 → cross-device distributed orchestration
Agent A/B / Behavioral Fabric → HCI, UX, values, and behavioral evaluation
Walled Gardens → interoperability and ecosystem-level implications
```

The comparison question is:

```text
Does this paper address infrastructure, collaboration, sustainability, efficiency, usability, adoption, interoperability, or value alignment?
```

---

## Reading decision

- **Keep in S8 P2:** Yes
- **Read fully?** Yes, if it becomes part of the S8 backbone.
- **Depth needed:** Medium to high
- **Main use:** Support discussion of web-agent-based UX simulation and scalable A/B testing
- **Most important parts to read:**
  - Abstract and introduction
  - Problem statement
  - System or conceptual framework
  - Main evaluation or evidence
  - Design implications
  - Limitations and future work

---

## One-sentence summary

Agent A/B: Automated and Scalable A/B Testing on Live Websites with Interactive LLM Agents is a P2 source for S8 because it helps explain **web-agent-based UX simulation and scalable A/B testing**, but it should be cited according to its verified venue/status and used mainly to enrich the open-challenges and future-directions section.

---

## BibTeX placeholder

```bibtex
@misc{bautomatedscalableb2025,
  title = {Agent A/B: Automated and Scalable A/B Testing on Live Websites with Interactive LLM Agents},
  year = {2025/2026},
  note = {CHI EA 2026 / ACM DOI 10.1145/3772363.3799039. Verify final bibliographic metadata before thesis submission.}
}
```
