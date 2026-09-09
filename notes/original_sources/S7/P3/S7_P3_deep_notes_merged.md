# S7 P3 Deep Notes — Security, Robustness, Trust, Risk, and Agentic Safety

**Section:** S7 — Security & Robustness  
**Priority:** P3 — supporting / contextual / extension papers  
**Purpose:** Build a deep archive of supporting papers for the S7 literature-review section, especially for risks in LLM agents, multi-agent systems, web agents, tool-use systems, privacy leakage, prompt injection, monitoring, and oversight.

---

## 0. Executive Synthesis for S7

The S7 P3 batch strengthens the security and robustness section by widening it beyond classical prompt injection and adversarial robustness. Together, these papers show that LLM-based agents introduce a broader security problem: they are not only models that generate unsafe text, but **autonomous socio-technical systems** that can remember private data, use tools, communicate with other agents, manipulate external environments, and produce real-world side effects.

The most important contribution of this batch is that it helps define S7 as a layered security problem:

1. **Model-level privacy and memorization** — LLMs can memorize and reproduce training data, including sensitive sequences.
2. **Alignment and assurance gaps** — current evaluation, interpretability, benchmarking, and safety methods are insufficient for robust assurance.
3. **Customized-agent abuse** — user-created agents/GPTs can be configured as phishing, malicious-code, or information-theft interfaces.
4. **World-model safety** — agent planning becomes riskier when the agent relies on learned environment simulators that may hallucinate, mispredict, or generalize poorly.
5. **TRiSM and governance for multi-agent systems** — trust, risk, security, privacy, explainability, lifecycle governance, and monitoring must be handled at the system level.
6. **Agent-to-agent threat propagation** — inter-agent protocols create new attack surfaces where malicious natural-language payloads can propagate across trusted channels.
7. **Formal oversight** — probabilistic LLM-as-judge evaluation is insufficient for high-stakes agent supervision; neuro-symbolic and formal verification may provide stronger guarantees.

For your thesis on **LLM-based agents for generalized web automation and data extraction**, the main S7 message should be:

> Security in LLM-based web agents is not limited to malicious prompts; it emerges from the interaction between natural-language instructions, memory, tools, browser actions, external APIs, retrieved web content, inter-agent communication, and user trust. Therefore, future web automation agents need security-aware architectures with sandboxing, provenance tracking, permission boundaries, memory governance, trajectory monitoring, and verifiable oversight.

---

## 1. Venue / Status Verification Summary

| # | Paper | Verified venue/status | Citation strength | Use in S7 |
|---|---|---|---|---|
| 1 | Emergent and Predictable Memorization in Large Language Models | NeurIPS 2023 / Advances in Neural Information Processing Systems 36 | Strong | Model-level memorization, privacy leakage, dataset auditing |
| 2 | Foundational Challenges in Assuring Alignment and Safety of Large Language Models | TMLR 2024, accepted with Survey + Expert certification | Strong | High-level safety/alignment framing, agentic and multi-agent risks |
| 3 | GPT in Sheep's Clothing: The Risk of Customized GPTs | arXiv 2024 / CoRR only found | Cautious | Customized agent abuse, malicious GPTs, phishing and malicious actions |
| 4 | World Models: The Safety Perspective | IEEE ISSRE Workshops 2024 / ISSREW | Medium-strong | Safety of world models for embodied / planning agents |
| 5 | TRiSM for Agentic AI | AI Open 2026 + arXiv 2025 | Strong for survey framing, but check final bibliographic metadata | TRiSM, AMAS risk taxonomy, governance, metrics |
| 6 | Agent2Agent Threats in Safety-Critical LLM Assistants | arXiv 2026 preprint | Cautious | A2A threat modeling, poison/trigger paths, human-centric assets |
| 7 | FORMALJUDGE: A Neuro-Symbolic Paradigm for Agentic Oversight | arXiv 2026 preprint | Cautious | Formal verification, agent oversight, LLM-as-judge limitations |

**Important citation policy for final survey:**

- Use **NeurIPS 2023**, **TMLR 2024**, **ISSREW 2024**, and **AI Open 2026** as stronger supporting sources.
- Use **GPT in Sheep's Clothing**, **Agent2Agent Threats**, and **FORMALJUDGE** as emerging/preprint evidence unless later peer-reviewed versions are confirmed.
- Do not overstate the arXiv-only 2026 papers as established consensus; frame them as early evidence of emerging research directions.

---

# 2. Paper Notes

---

## Paper 1 — Emergent and Predictable Memorization in Large Language Models

### Venue / Status

- **Final venue:** NeurIPS 2023, Advances in Neural Information Processing Systems 36.
- **Earlier version:** arXiv:2304.11158.
- **Status:** Peer-reviewed conference paper.
- **Citation caution:** Safe to cite strongly for memorization, privacy leakage, and scaling-related memorization behavior.

### Core idea

This paper studies whether the memorization behavior of a large language model can be forecast before full-scale training. Instead of only measuring average memorization after deployment, the authors ask whether specific training sequences likely to be memorized by a target model can be predicted using smaller models or partially trained checkpoints.

The work is important because memorization is a security and privacy issue: if an LLM memorizes sensitive data, it may later reproduce training sequences verbatim, including private or personally identifiable information. For safety-critical and enterprise web agents, this matters because agents often combine LLMs with memory, logs, retrieved documents, user histories, and tool outputs.

### Key contribution

The paper introduces the problem of **forecasting memorization of specific datapoints**. This is more actionable than corpus-level memorization statistics because practitioners need to know whether particular high-risk examples may be reproduced.

The study uses the Pythia model suite to evaluate memorization across model sizes and training checkpoints. It treats memorization prediction as a classification problem: if a smaller or partially trained model memorizes a sequence, can that predict whether the final larger model will memorize it?

### Method / approach

The paper uses the concept of **k-extractability**, where a sequence is considered memorized if the model can reproduce the continuation from a prompt prefix. The authors measure memorization scores by comparing greedy generations to true training continuations.

They examine two forecasting settings:

1. **Across scale:** use a smaller fully trained model to predict memorization in a larger model.
2. **Across training time:** use a partially trained checkpoint to predict memorization in the final checkpoint.

They analyze precision and recall because the practitioner’s risk depends on false negatives and false positives. In privacy-sensitive settings, false negatives are especially dangerous: the system predicts that a sequence will not be memorized, but the final model memorizes it anyway.

### Key findings

The central finding is that memorization forecasting is difficult. Smaller models and early checkpoints do not reliably predict memorization in larger or fully trained models unless a substantial fraction of compute has already been spent.

This means memorization can behave as an emergent or late-training phenomenon. The implication is that simple early checks may not be enough to guarantee that sensitive data will not be memorized.

### Limitations

The paper focuses on memorization in pretrained LLMs, not specifically on agentic systems. It does not directly evaluate web agents, browser agents, or tool-using agents. It also does not solve memorization; it primarily characterizes and forecasts it.

For your thesis, the limitation is useful: it shows that **model-level privacy risk remains unresolved even before adding agent memory, tool logs, browser traces, or retrieved web content**.

### Relevance to your thesis

This paper supports the security foundation of S7 by showing that LLMs can reproduce training sequences and that this behavior is hard to forecast. In web automation and data extraction, agents may operate over sensitive websites, user accounts, proprietary databases, forms, and extracted documents. Memorization risk therefore appears in several places:

- pretrained model data leakage;
- memory-store leakage;
- logs and traces used for agent fine-tuning;
- RAG corpora containing private content;
- browser-session artifacts;
- extracted datasets reused for model training.

### How to use it in the literature review

Use this paper in the opening part of S7 to show that privacy and leakage risk begins at the **model substrate**, before considering agent orchestration.

Suggested placement:

- S7.1 Model-level risks and privacy leakage
- S7.2 Security implications of memory and logging
- S7.5 Open challenges in privacy-preserving web agents

### Connects to

- **S2 Foundations:** scaling laws and emergent behavior.
- **S3 Agent Architectures:** memory modules and long-term context.
- **S5.5 Failure Modes:** silent leakage and unpredictable failure modes.
- **S6 Web Data Extraction:** extraction over sensitive or proprietary data.
- **S8 Open Challenges:** privacy-preserving evaluation and deployment.

### Sentence to add later

> At the model level, memorization studies show that LLMs may reproduce specific training sequences and that such behavior is difficult to predict reliably from smaller or partially trained models, making privacy leakage a foundational concern for web agents that process sensitive traces, extracted content, and user-specific data.

### Critique

This paper is valuable for S7 because it gives a rigorous empirical foundation for privacy leakage. However, it is not enough to cover agentic privacy, because web agents introduce additional leakage channels beyond pretraining memorization: persistent memory, browser history, action logs, tool outputs, APIs, external documents, and multi-agent communication. Therefore, in your review, use this paper as the **model-level privacy anchor**, then extend the discussion to agent-level privacy and system-level governance.

---

## Paper 2 — Foundational Challenges in Assuring Alignment and Safety of Large Language Models

### Venue / Status

- **Final venue:** Transactions on Machine Learning Research (TMLR), 2024.
- **OpenReview status:** Accepted by TMLR, with Survey Certification and Expert Certification.
- **Status:** Peer-reviewed long survey / research agenda.
- **Citation caution:** Safe to cite strongly as a broad safety and alignment agenda.

### Core idea

This work maps foundational challenges in assuring the alignment and safety of LLMs. It organizes the challenges into three broad categories:

1. scientific understanding of LLMs;
2. development and deployment methods;
3. sociotechnical challenges.

It is especially relevant to your S7 section because it explicitly discusses agentic LLMs, multi-agent safety, prompt injection, jailbreaks, data poisoning, interpretability limits, evaluation limitations, and governance.

### Key contribution

The paper’s main contribution is not a new algorithm but a structured safety research agenda. It identifies major unsolved assurance problems and formulates many concrete research questions.

For your literature review, its strongest role is to provide a high-level framing:

- why benchmarking alone is insufficient;
- why agentic LLMs introduce novel risks;
- why multi-agent safety cannot be reduced to single-agent safety;
- why current interpretability and oversight methods remain incomplete;
- why prompt injection, poisoning, and jailbreaking should be treated as core deployment risks.

### Method / approach

The authors synthesize contemporary research across LLM safety, alignment, interpretability, evaluation, adversarial attacks, governance, and sociotechnical risk. The paper is structured as an agenda rather than a conventional systematic review.

Its taxonomy-like organization makes it useful as an umbrella reference for S7.

### Key findings / claims

The paper argues that LLM assurance is difficult because:

- LLM capabilities are hard to estimate and understand;
- emergent capabilities and scaling effects are not well characterized;
- reasoning and in-context learning are still black-box phenomena;
- agentic LLMs pose novel risks due to tool use, autonomy, and goal-directed behavior;
- multi-agent systems can exhibit correlated failures, collusion, or emergent functionality;
- jailbreaks, prompt injections, poisoning, and backdoors remain poorly understood;
- evaluations may be biased, contaminated, or confounded by scaffolding.

### Limitations

The paper is broad rather than specific to web automation. It gives strong conceptual framing but does not provide a web-agent-specific risk model. It also does not propose a concrete deployment architecture for secure browser agents.

For your thesis, this limitation creates space to argue that web-agent security needs a domain-specific treatment that combines LLM safety, web security, browser automation constraints, extraction risks, and agentic tool governance.

### Relevance to your thesis

This paper should be one of the strongest S7 references. It helps justify why **LLM-based web automation cannot rely only on benchmark performance**. The paper supports the argument that safe deployment requires assurance across model behavior, tool use, autonomy, monitoring, and governance.

For web agents, the most relevant parts are:

- prompt injection as a security threat;
- tool affordances creating side effects;
- scaffolding complicating evaluation;
- multi-agent safety risks;
- evaluation and benchmark limitations;
- need for robust oversight and monitoring.

### How to use it in the literature review

Use this paper near the beginning of S7 as the high-level safety agenda, then specialize the discussion to web agents.

Suggested placement:

- S7 introduction: security and safety as assurance problem;
- S7.2 Prompt injection and adversarial inputs;
- S7.3 Tool-use and autonomy risks;
- S7.4 Multi-agent and coordination risks;
- S7.6 Governance and oversight.

### Connects to

- **S3 Agent Architectures:** autonomy, tools, memory, planning.
- **S5.1 Benchmarks:** limitations of benchmarks for safety assurance.
- **S5.5 Failure Modes:** safety failures, correlated failures, hallucination.
- **S6 Web Data Extraction:** unsafe extraction and data leakage.
- **S8 Open Challenges:** assurance, governance, benchmark design.

### Sentence to add later

> Broader LLM safety agendas emphasize that agentic systems introduce risks beyond static model outputs, including tool-mediated side effects, prompt injection, multi-agent coordination failures, and insufficient oversight, all of which are directly relevant to autonomous web agents operating over untrusted web environments.

### Critique

This paper gives your S7 section authority and breadth. However, because it is an agenda paper, it should not replace concrete web-agent security evidence. Use it to frame the landscape, but combine it with web-specific work on indirect prompt injection, browser-agent attacks, tool-use sandboxing, and trajectory monitoring.

---

## Paper 3 — GPT in Sheep's Clothing: The Risk of Customized GPTs

### Venue / Status

- **Final venue found:** arXiv / CoRR 2024.
- **Peer-reviewed venue:** No confirmed peer-reviewed conference or journal version found in the current check.
- **Status:** Preprint / security awareness study.
- **Citation caution:** Cite cautiously as early evidence of customized-GPT misuse; do not present as definitive empirical benchmark evidence.

### Core idea

This paper studies the security and privacy risks of customized GPTs. It argues that custom GPT-like agents can be configured maliciously, even when they appear to users as helpful assistants. Because users may trust these customized agents, attackers can exploit them for phishing, unsafe coding advice, malicious code injection, or information theft.

### Key contribution

The paper proposes a threat taxonomy for malicious customized GPTs. The main categories are:

1. **Vulnerability steering** — guiding users toward insecure versions, unsafe configuration, or vulnerable practices.
2. **Malicious injection** — inserting malicious code snippets or recommending malicious libraries.
3. **Information theft** — eliciting sensitive information or exfiltrating information through actions or links.

This taxonomy is useful for your S7 section because web agents and data-extraction agents can also be customized, shared, and reused by non-expert users.

### Method / approach

The authors demonstrate how malicious custom GPTs can be created and used to carry out several attack scenarios. Examples include:

- recommending vulnerable software versions;
- generating SQL-injection-prone code;
- generating buffer-overflow-prone C code;
- injecting harmful code into user workflows;
- encouraging direct or third-party phishing.

The paper is more of a threat demonstration than a controlled large-scale study.

### Key findings

The paper shows that customized GPTs can create a false sense of trust. Users may assume that an assistant hosted on a trusted platform is safe, but the behavior of the customized assistant may have been shaped by a malicious builder.

For agentic systems, this is important because customization is a major feature of modern agents: users can provide instructions, documents, tools, and actions. These same customization surfaces become attack surfaces.

### Limitations

The paper has several limitations:

- It is arXiv-only in the current check.
- It is demonstration-heavy rather than benchmark-heavy.
- Some examples depend on specific platform capabilities and policies at the time of writing.
- It focuses on custom GPTs, not specifically browser agents or web extraction agents.

However, its conceptual value is high because the risk pattern generalizes: **when users can create or share agents, malicious configuration becomes a security threat**.

### Relevance to your thesis

This paper is useful for discussing **agent customization as an attack surface**. In your thesis, generalized web automation may involve agents that users configure for scraping, form filling, search, monitoring, extraction, and workflow automation. A malicious or poorly specified agent could:

- exfiltrate extracted data;
- scrape prohibited or private content;
- leak API keys or credentials;
- recommend unsafe code for scraping pipelines;
- bypass website restrictions;
- manipulate users into granting permissions;
- call external APIs with sensitive payloads.

### How to use it in the literature review

Use this as a supporting example in a subsection on malicious or untrusted agents.

Suggested placement:

- S7.2 Prompt injection and malicious instruction design;
- S7.3 Tool/action misuse;
- S7.5 User trust, customization, and deployment risk.

### Connects to

- **S3 Agent Architectures:** user-defined agent profiles, tools, and actions.
- **S6 Web Data Extraction:** malicious scraping and exfiltration risks.
- **S7 Security:** phishing, malicious code, information theft.
- **S8 Open Challenges:** safe customization and agent marketplaces.

### Sentence to add later

> Customized GPT-style agents illustrate that agent configuration itself can become a security boundary: malicious builders may embed unsafe instructions, phishing behavior, or harmful code suggestions into agents that appear benign to end users.

### Critique

This is a useful P3 paper, but it should not be a central pillar of S7. Its value is in illustrating a concrete deployment risk: the agent’s instructions and tools may be controlled by someone other than the end user. For an ACM Computing Surveys version, use it briefly and pair it with stronger peer-reviewed work on prompt injection, third-party app privacy, and agent security frameworks.

---

## Paper 4 — World Models: The Safety Perspective

### Venue / Status

- **Final venue:** IEEE 35th International Symposium on Software Reliability Engineering Workshops, ISSREW 2024.
- **Earlier version:** arXiv:2411.07690.
- **Status:** Workshop / conference-workshop paper.
- **Citation caution:** Good supporting citation for world-model safety, especially in embodied/safety-critical settings. It is not primarily about web agents.

### Core idea

This paper reviews world models from a safety perspective. A world model is intended to help an agent predict future environment states, fill in missing information, and support planning. The paper focuses especially on embodied AI and safety-critical domains such as autonomous driving and robotics.

The central argument is that if agents rely on learned world models, then the safety of the agent depends partly on the reliability, robustness, and trustworthiness of the world model.

### Key contribution

The paper provides a taxonomy of world-model techniques and traces their evolution, including:

- RNN-based world models;
- transformer-based world models;
- diffusion-based world models;
- other generative and simulation-based approaches.

It then analyzes safety deficiencies and proposes research directions for trustworthy world models.

### Method / approach

The paper is a survey-style review. It organizes the development of world models chronologically and technically, then discusses safety implications.

The visual timeline of world-model techniques is especially useful for showing how world models evolved from simple recurrent environment predictors to multimodal generative simulators.

### Key findings / arguments

The paper argues that current world models are risky in safety-critical use cases because they may:

- hallucinate plausible but incorrect future states;
- fail under distribution shift;
- generalize poorly to unseen environments;
- produce unsafe plans if used for planning;
- encode incomplete or biased representations of the environment;
- lack verifiable safety guarantees.

### Limitations

The paper focuses on embodied agents rather than web agents. Web automation environments are digital rather than physical, but the underlying principle still applies: agents operate with an implicit or explicit model of the environment. For web agents, the “world model” may include assumptions about DOM state, website behavior, user intent, API effects, task progress, and hidden page dynamics.

### Relevance to your thesis

For web automation and data extraction, the world-model perspective is useful because web agents must predict the consequences of actions:

- clicking a button;
- submitting a form;
- navigating to a page;
- accepting cookies;
- triggering downloads;
- interacting with account settings;
- executing scraping actions;
- deciding whether extracted information is complete.

If the agent’s environment model is wrong, it may click destructive controls, submit incorrect data, loop, misclassify content, or leak information.

### How to use it in the literature review

Use this paper as a bridge between S5.3 planning and S7 safety:

- In S5.3, world models support planning.
- In S7, world models become a safety risk when their predictions are wrong.

Suggested placement:

- S7.3 Safety risks from planning and environment modeling;
- S7.4 Distribution shift and unsafe generalization;
- S8 open challenge on verifiable world models for web agents.

### Connects to

- **S5.3 Planning & Reasoning:** world models for planning.
- **S5.5 Failure Modes:** hallucinated state transitions, distribution shift.
- **S7 Security & Robustness:** unsafe action selection.
- **S8 Open Challenges:** verified environment modeling for agents.

### Sentence to add later

> World-model research suggests that agent safety depends not only on policy alignment but also on the reliability of the agent’s internal environment model, since inaccurate predictions about future states can lead to unsafe plans and unintended side effects.

### Critique

This is not a core web-agent paper, but it is strategically useful because it expands your safety discussion from “prompt attacks” to “unsafe environment modeling.” For your thesis, adapt the concept carefully: web agents do not need physical-world simulation, but they still need robust models of web state, task progress, action consequences, and extraction completeness.

---

## Paper 5 — TRiSM for Agentic AI: A Review of Trust, Risk, and Security Management in LLM-based Agentic Multi-Agent Systems

### Venue / Status

- **Final venue found:** AI Open, 2026.
- **Earlier version:** arXiv:2506.04133.
- **Status:** Review/survey paper.
- **Citation caution:** Strong for system-level TRiSM framing, but verify final bibliographic details before final thesis submission because the uploaded version is an arXiv version.

### Core idea

This paper adapts the Trust, Risk, and Security Management (TRiSM) perspective to LLM-based Agentic Multi-Agent Systems (AMAS). It argues that agentic AI requires system-level governance because risks arise from autonomy, tool use, memory, multi-agent coordination, emergent behavior, and lifecycle drift.

### Key contribution

The paper contributes:

1. a TRiSM framework for agentic AI;
2. a risk taxonomy for AMAS;
3. a mapping of risks to controls;
4. discussion of explainability, ModelOps, security, privacy, and governance;
5. evaluation templates and proposed metrics such as Component Synergy Score (CSS) and Tool Utilization Efficacy (TUE).

For S7, this is one of the most relevant papers because it treats agent security as a **system-level lifecycle problem**, not only a model-level vulnerability problem.

### Method / approach

The paper conducts a structured review of literature on agentic AI, multi-agent LLM systems, security, privacy, governance, explainability, and risk management.

It distinguishes traditional agents from LLM-based agentic systems and identifies AMAS components such as:

- LLM core;
- planning/reasoning module;
- memory module;
- communication middleware;
- task manager/orchestrator;
- tool interface;
- monitoring and governance layer;
- human-in-the-loop interface;
- security gateway and privacy layer.

### Key findings / arguments

The paper argues that AMAS introduce risks such as:

- prompt injection;
- memory poisoning;
- tool misuse;
- data leakage;
- agent collusion;
- emergent misbehavior;
- coordination failures;
- lifecycle governance failures;
- weak accountability and auditability.

It emphasizes that these risks require technical, organizational, and governance controls.

### Limitations

The paper is broad and includes many conceptual elements. Some proposed metrics and frameworks may require further empirical validation. It is also not specific to web automation or web data extraction.

For your thesis, use it as a high-level framework but specialize it to browser/web agents.

### Relevance to your thesis

This paper is highly useful for your S7 because generalized web agents are exactly the kind of system that needs TRiSM-style controls. They operate with:

- tools and APIs;
- browser actions;
- external websites;
- user credentials;
- persistent memory;
- extracted data;
- multi-step plans;
- monitoring and logs;
- possible multi-agent coordination.

Thus, your web-agent security section can adapt the TRiSM layers to web automation:

- **Trust:** explainable actions, user control, provenance.
- **Risk:** destructive actions, privacy leakage, scraping misuse, legal/compliance risk.
- **Security:** prompt injection, tool abuse, credential leakage, sandboxing.
- **Governance:** audit logs, permission boundaries, lifecycle evaluation.

### How to use it in the literature review

Use this as a central S7 support paper for system-level risk management.

Suggested placement:

- S7.1 From model safety to agentic system risk;
- S7.4 Multi-agent security and governance;
- S7.6 Monitoring, auditability, and lifecycle controls.

### Connects to

- **S3 Agent Architectures:** memory, planning, tool use, orchestration.
- **S5.1 Benchmarks:** evaluation metrics for trust and tool use.
- **S5.5 Failure Modes:** coordination failure and emergent behavior.
- **S6 Web Data Extraction:** privacy and compliance risks.
- **S8 Open Challenges:** governance and trustworthy deployment.

### Sentence to add later

> TRiSM-oriented analyses of agentic multi-agent systems show that security must be managed across the full agent lifecycle, including explainability, ModelOps, tool-use governance, privacy controls, auditability, and coordinated risk management.

### Critique

This paper is very useful for organizing S7, but it should not be treated as the final word. It is stronger as a framework than as empirical evidence. In your final survey, you can use it to define dimensions of security and governance, then cite more targeted works for prompt injection, browser-agent attacks, privacy leakage, sandboxing, and execution monitoring.

---

## Paper 6 — Agent2Agent Threats in Safety-Critical LLM Assistants: A Human-Centric Taxonomy

### Venue / Status

- **Final venue found:** arXiv:2602.05877.
- **Peer-reviewed venue:** No confirmed conference or journal version found in the current check.
- **Status:** 2026 preprint.
- **Citation caution:** Cite cautiously as emerging work on A2A threat modeling.

### Core idea

This paper studies security risks arising from inter-agent communication, especially in safety-critical LLM assistants such as in-vehicle agents. It argues that protocols such as Agent-to-Agent (A2A) can create new attack surfaces because natural-language payloads can propagate between agents through authenticated channels.

The core insight is that authentication of the sender does not guarantee safety of the content. A compromised or malicious agent can send payloads that are syntactically valid but semantically harmful.

### Key contribution

The paper proposes **AgentHeLLM**, a threat-modeling framework that separates:

- **what is being protected** — human-centric assets;
- **how it is attacked** — attack paths.

It introduces a graph-based attack model distinguishing:

1. **Poison paths** — malicious data propagation paths.
2. **Trigger paths** — activation actions that cause dormant payloads to affect the target system.

This separation is useful because existing taxonomies often mix assets, attacks, and consequences.

### Method / approach

The paper adapts safety-critical threat analysis principles to LLM-based agents. It critiques component-centric taxonomies and proposes a two-dimensional taxonomy:

- **Assets:** life and bodily health, mental well-being, privacy and personal data, knowledge/thought/belief, economic resources, reputation/dignity, social relationships/trust.
- **Attack paths:** actor nodes, datasource nodes, interaction edges, poison paths, trigger paths, activation phases.

It also introduces an attack-path suggestion tool for discovering multi-stage threats.

### Key findings / arguments

The paper argues that agent-to-agent protocols amplify prompt-borne risks because:

- malicious payloads can propagate across trusted agent channels;
- receiving agents may treat agent-originated content with the same privilege as user input;
- metadata, file parts, data parts, task status messages, and descriptions may carry hidden instructions;
- persistent memory can store poisoned content for later activation;
- safety-critical contexts make failures more severe.

### Limitations

The paper is preprint-only in the current check and focuses on automotive assistants, not web agents. Its risk categories may need adaptation to web automation.

However, the A2A risk model is highly relevant to future web agents because web automation systems may increasingly use multiple agents, MCP tools, browser agents, API agents, extraction agents, verification agents, and report-writing agents.

### Relevance to your thesis

This paper is especially useful if your thesis discusses multi-agent web automation. A generalized web automation system may include:

- a planner agent;
- a browser-control agent;
- an extraction agent;
- a verifier agent;
- a memory/retrieval agent;
- an API/tool agent;
- a report generator.

If these agents communicate through natural language, malicious web content or poisoned intermediate results can propagate from one agent to another. For example:

1. A webpage contains an indirect prompt injection.
2. The browser agent summarizes it.
3. The planner agent treats the summary as trusted instruction.
4. The extraction agent leaks sensitive content to an external endpoint.
5. The verifier agent fails to detect the contamination because the payload appears as internal agent context.

This is directly relevant to web agents.

### How to use it in the literature review

Use it in the subsection on multi-agent and protocol-level threats.

Suggested placement:

- S7.4 Multi-agent communication threats;
- S7.5 Protocols, tool interfaces, and attack propagation;
- S8 open challenge on secure agent-to-agent communication.

### Connects to

- **S3 Agent Architectures:** multi-agent communication protocols.
- **S5.5 Failure Modes:** cascading failures and hidden triggers.
- **S6 Web Data Extraction:** poisoned web content and extraction workflows.
- **S7 Security:** prompt propagation, protocol-level risk.
- **S8 Open Challenges:** secure MCP/A2A-style tool and agent protocols.

### Sentence to add later

> Emerging work on agent-to-agent threat modeling suggests that inter-agent communication can propagate prompt-borne attacks through authenticated channels, making content validation, provenance tracking, and privilege separation essential for multi-agent web automation systems.

### Critique

This is not yet a mature, peer-reviewed reference, but it is very relevant to the direction of agentic web automation. Use it cautiously to signal emerging threats. It can help make your survey modern by connecting web-agent security to new protocol ecosystems such as A2A and MCP-style agent/tool communication.

---

## Paper 7 — FORMALJUDGE: A Neuro-Symbolic Paradigm for Agentic Oversight

### Venue / Status

- **Final venue found:** arXiv:2602.11136.
- **Peer-reviewed venue:** No confirmed conference or journal version found in the current check.
- **Status:** 2026 preprint.
- **Citation caution:** Cite cautiously as emerging work on formal oversight; do not treat the reported numbers as settled without peer review.

### Core idea

This paper critiques the dominant **LLM-as-a-Judge** oversight paradigm. It argues that probabilistic LLMs are unreliable supervisors for other probabilistic LLM agents because they may inherit similar biases, hallucinations, persuasion vulnerabilities, and failure modes.

The proposed alternative is **FORMALJUDGE**, a neuro-symbolic framework that uses LLMs to translate natural-language requirements and agent trajectories into formal specifications, then verifies compliance using Dafny and Z3 SMT solving.

### Key contribution

The key contribution is a **Formal-of-Thought** architecture:

1. Top-down decomposition of human intent into atomic verifiable constraints.
2. Extraction of atomic facts from agent trajectories.
3. Translation into Dafny specifications.
4. Deterministic verification using Z3.
5. Final safety judgment based on formal proof rather than subjective LLM scoring.

This is important because web agents often execute multi-step trajectories where safety depends on whether the whole trajectory satisfies constraints, not whether an LLM judge subjectively approves the final answer.

### Method / approach

The framework separates neural and symbolic roles:

- The LLM handles semantic extraction and specification compilation.
- The formal verifier handles logical composition and proof checking.

The authors evaluate the method on benchmarks covering behavioral safety, constraint adherence, and deception detection. The paper reports improvement over LLM-as-judge baselines and claims weak-to-strong oversight capability.

### Key findings / claims

The paper claims that FORMALJUDGE:

- improves average performance over LLM-as-judge baselines;
- can detect deception from stronger agents using smaller judge models;
- supports iterative refinement using formal feedback;
- is less vulnerable to persuasive manipulation because the verifier checks grounded facts rather than reasoning narratives.

### Limitations

The paper is recent and preprint-only. Its claims need careful validation. Formal verification depends on the correctness of specification extraction; if the LLM extracts the wrong facts or misses a constraint, the formal proof may be formally valid but semantically incomplete.

For real web agents, additional challenges remain:

- mapping browser actions to formal predicates;
- representing DOM changes and web state;
- handling stochastic page behavior;
- formalizing user intent;
- verifying extraction completeness;
- checking legal/compliance constraints;
- scaling verification over long trajectories.

### Relevance to your thesis

This paper is very relevant to the future direction of secure web agents because browser automation creates verifiable trajectories:

- visited URLs;
- clicked DOM elements;
- form submissions;
- extracted fields;
- tool/API calls;
- memory writes;
- downloads;
- final outputs.

These trajectories could be checked against formal or semi-formal constraints:

- never submit credentials to untrusted domains;
- do not click destructive actions without confirmation;
- do not export personal data to external APIs;
- verify extracted data source provenance;
- respect robots.txt or policy constraints;
- ensure every extracted record has a traceable source;
- stop if a webpage contains prompt-injection instructions.

### How to use it in the literature review

Use it in S7 as an emerging oversight direction.

Suggested placement:

- S7.6 Monitoring, verification, and oversight;
- S8 open challenge: formal or neuro-symbolic verification for web-agent trajectories.

### Connects to

- **S5.1 Evaluation:** LLM-as-judge limitations.
- **S5.5 Failure Modes:** deception, silent failures, constraint violations.
- **S6 Web Data Extraction:** provenance and extraction verification.
- **S7 Security:** oversight and safety constraints.
- **S8 Open Challenges:** verifiable web automation.

### Sentence to add later

> Recent neuro-symbolic oversight work argues that LLM-as-judge evaluation is insufficient for high-stakes agents and explores formal verification of agent trajectories, suggesting a promising direction for checking web-agent actions against explicit safety, privacy, and provenance constraints.

### Critique

This is one of the most interesting P3 papers for your future research direction, but it must be handled carefully. Its promise is strong: web-agent trajectories are naturally structured and may be more verifiable than open-ended conversations. Its weakness is that formal specifications are hard to derive from natural-language goals and dynamic web environments. In your survey, present it as an open research direction rather than a solved solution.

---

# 3. S7 Section-Level Synthesis

## 3.1 What S7 should argue

S7 should argue that security and robustness for LLM-based web agents must be treated as a **multi-layer assurance problem**.

A strong S7 narrative could be:

1. LLMs already have model-level risks such as memorization and privacy leakage.
2. Agentic systems add autonomy, tools, memory, and external action.
3. Web environments are untrusted and adversarial by default.
4. Multi-agent systems create propagation channels for malicious instructions and poisoned context.
5. Evaluation alone is insufficient because failures can be silent, delayed, or hidden inside trajectories.
6. Robust deployment requires sandboxing, access control, provenance, monitoring, privacy governance, and possibly formal verification.

## 3.2 Recommended S7 subsection structure

```text
S7 Security, Robustness, and Trustworthy Deployment

S7.1 Model-Level Risks: Memorization, Privacy Leakage, and Data Contamination
S7.2 Prompt Injection, Jailbreaks, and Malicious Web Content
S7.3 Tool-Use and Browser-Action Risks
S7.4 Memory, Multi-Agent Communication, and Attack Propagation
S7.5 Trust, Risk, Security Management, and Governance
S7.6 Monitoring, Oversight, and Verification of Agent Trajectories
S7.7 Summary: Why Secure Web Automation Requires System-Level Assurance
```

## 3.3 How the S7 P3 papers fit

| Subsection | Papers to use | Function |
|---|---|---|
| S7.1 | Emergent and Predictable Memorization | Model-level privacy and memorization |
| S7.2 | Foundational Challenges; GPT in Sheep's Clothing | Prompt injection, malicious GPTs, jailbreaks, user trust |
| S7.3 | World Models; FORMALJUDGE | Planning/action risk and formal checking |
| S7.4 | Agent2Agent Threats; TRiSM | Multi-agent communication, collusion, memory poisoning |
| S7.5 | TRiSM; Foundational Challenges | Governance, lifecycle risk, auditability |
| S7.6 | FORMALJUDGE; TRiSM | Oversight, trajectory verification, trust metrics |

---

# 4. Ready-to-Add Paragraph for S7

Modern LLM-based web agents inherit security risks from both language models and autonomous software systems. At the model level, memorization studies show that LLMs may reproduce specific training sequences and that such behavior is difficult to forecast reliably, creating privacy risks when agents process sensitive traces, extracted records, or user-specific documents. At the system level, safety agendas emphasize that agentic LLMs introduce additional risks through tool use, memory, external actions, prompt injection, and multi-agent coordination. Customized GPT-style systems further show that agent configuration itself can become a malicious interface, enabling phishing, unsafe code suggestions, or information theft. These risks are amplified in multi-agent and protocol-based environments, where prompt-borne payloads may propagate between agents through apparently trusted communication channels. Consequently, secure web automation requires more than output filtering: it requires permission boundaries, sandboxed execution, provenance tracking, memory governance, audit logs, trajectory monitoring, and stronger oversight mechanisms, including emerging neuro-symbolic or formal verification approaches for checking whether agent actions satisfy privacy, safety, and task constraints.

---

# 5. Tools, Frameworks, and Concepts to Mention in S7

## 5.1 Security and governance frameworks

| Tool / framework / concept | How to use in S7 |
|---|---|
| AI TRiSM | Overall trust, risk, security, privacy, and governance framing |
| NIST AI Risk Management Framework | Governance and risk-management reference |
| ISO/IEC 42001 | AI management-system governance reference |
| EU AI Act | Regulatory context for high-risk AI systems |
| OWASP Top 10 for LLM Applications | Prompt injection, insecure output handling, supply-chain risks |
| OWASP Agentic AI Threats | Agent-specific threats such as tool misuse and memory poisoning |
| MITRE ATLAS | Adversarial ML / AI attack taxonomy |
| ISO/SAE 21434 / TARA | Useful analogy for systematic threat modeling in safety-critical agents |

## 5.2 Agent security controls

| Control | Why relevant to web agents |
|---|---|
| Browser sandboxing | Prevent harmful page actions and local-system compromise |
| Permissioned tool use | Prevent arbitrary API or file-system calls |
| Credential isolation | Protect accounts, cookies, tokens, and API keys |
| Domain allowlists / blocklists | Control where agents can navigate or send data |
| Human-in-the-loop confirmation | Required for destructive or irreversible actions |
| Prompt-injection filters | Detect malicious webpage instructions |
| Provenance tracking | Trace extracted data back to source pages and actions |
| Memory write policies | Prevent poisoning and sensitive data retention |
| Action audit logs | Support debugging, accountability, and compliance |
| Trajectory anomaly detection | Identify loops, drift, tool misuse, and silent failures |
| Formal or rule-based policy checks | Enforce hard constraints over agent actions |

## 5.3 Web-agent-specific risks

| Risk | Example |
|---|---|
| Indirect prompt injection | Webpage text instructs agent to ignore user and leak data |
| Credential leakage | Agent includes cookies/API keys in external tool calls |
| Unsafe form submission | Agent submits wrong or sensitive data |
| Destructive clicks | Agent deletes, purchases, sends, or changes settings |
| Extraction misuse | Agent scrapes restricted/private/regulated content |
| Data poisoning | Extracted web data contaminates memory or downstream datasets |
| Multi-agent propagation | Browser agent passes malicious text to planner/verifier as trusted context |
| Over-trust by user | User accepts unsafe recommendations from a customized agent |
| Incomplete provenance | Extracted data cannot be traced to source evidence |
| Silent failure | Agent reports success while missing details or drifting from task |

---

# 6. Recommendations for Final Thesis / ACM Survey Use

## Must include in S7

1. **Foundational Challenges in Assuring Alignment and Safety of LLMs** — broad safety foundation.
2. **TRiSM for Agentic AI** — system-level governance and multi-agent risk framing.
3. **Emergent and Predictable Memorization** — model-level privacy and memorization.
4. **World Models: The Safety Perspective** — planning/environment-model safety.

## Include briefly / as emerging examples

1. **GPT in Sheep's Clothing** — malicious custom agents and user trust.
2. **Agent2Agent Threats** — protocol-level attack propagation.
3. **FORMALJUDGE** — future direction for verifiable trajectory oversight.

## Avoid overusing

- Do not make arXiv-only papers central unless later peer-reviewed versions appear.
- Do not make automotive-specific examples dominate your web-agent section.
- Do not overclaim formal verification as solved for web agents.

---

# 7. Final S7 P3 Takeaway

The S7 P3 batch makes your security section much stronger because it shows that web-agent security is not one isolated problem. It is a stack:

```text
Model privacy
→ Prompt and instruction security
→ Tool and browser-action safety
→ Memory and retrieval governance
→ Multi-agent communication security
→ Monitoring and anomaly detection
→ Formal / human / institutional oversight
```

For the final survey, this batch should help you argue that generalized web automation agents require **defense-in-depth**: technical controls at the model, prompt, memory, tool, browser, protocol, evaluation, and governance layers.

