---
title: Prompt Injection
aliases:
  - Prompt Injection
  - prompt injection attack
  - instruction injection
  - indirect prompt injection
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - prompt-engineering

domain: prompt-engineering
subdomains:
  - security
  - adversarial-prompting

created: 2026-05-20
updated: '2026-05-21'
source-type: report-extraction
source-reports:
  - prompt-injection-synthetic-seed-2026-05-20
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: elaborated
parent-concept: Adversarial Attacks on AI Systems
related:
  - '[[Tool Use in LLMs]]'
  - '[[Jailbreaking]]'
  - '[[Instruction Hierarchy Conflict]]'
prerequisites:
  - '[[]]'
specializes:
  - '[[Tool Use in LLMs]]'
broader:
  - '[[]]'
see-also:
  - '[[]]'
contrasts-with:
  - '[[Jailbreaking]]'
contradicts:
  - '[[]]'
applies-to:
  - '[[Instruction Hierarchy Conflict]]'
formalizes:
  - '[[]]'
instance-of:
  - '[[]]'
supports:
  - '[[]]'
refines:
  - '[[]]'

review-frequency: quarterly
mastery-stage: budding
importance: medium
provenance:
  pipeline-version: v6.0.0
  outline-contract: v6-outline-v1
  elaborate-contract: v6-elaborate-v1
  passes: 2
  diagram-passes: 1
  diagram-model: qwen2.5:14b-instruct-q5_K_M
  last-diagrammed: '2026-05-21'
---

## 📊 Visual Overview

<!-- diagram-pass:1 (2026-05-21) -->

> [!abstract] **Diagram 1 — Prompt Injection Process Flow**
> *Follow the flow from input to output, noting where malicious instructions are injected and how they affect model behavior.*
>
> ```mermaid
> flowchart LR
>   A[Untrusted Input] --> B[LLM Processing]
>   B --> C[Malicious Instructions Embedded]
>   C --> D[Model Output Manipulated]
> ```


> [!abstract] **Diagram 2 — Prompt Injection vs Other Attacks**
> *Compare Prompt Injection with other adversarial attacks to understand their distinct characteristics.*
>
> ```mermaid
> graph TD
>   A[Prompt Injection] -->|Embeds Malicious Instructions| B[LLM Processing]
>   C[Model Poisoning] -->|Alters Training Data| D[System Behavior Induced]
>   E[Evasion Attack] -->|Manipulates Input Data| F[Bypasses Detection]
> ```


> [!abstract] **Diagram 3 — Agentic System Threat Model**
> *Identify the potential threats in agentic systems due to Prompt Injection.*
>
> ```mermaid
> flowchart LR
>   A[LLM with External Authority] --> B[Untrusted Input]
>   B --> C[Malicious Instructions Embedded]
>   C --> D[Unauthorized Actions or Data Exfiltration]
> ```

# Prompt Injection

> [!definition] **Prompt Injection**
> Prompt Injection is an adversarial attack where malicious instructions are embedded into data processed by large language models (LLMs), aiming to override or augment the system prompt's instructions and redirect the model’s behavior, potentially leading to unauthorized actions or information exfiltration. This concept specifically excludes other forms of security vulnerabilities that do not involve embedding such instructions within the data. It falls under adversarial attacks on AI systems.

> [!attention] **Boundary**
> This concept specifically refers to attacks targeting LLMs through untrusted inputs and should not be confused with other forms of security vulnerabilities that do not involve embedding malicious instructions within data processed by the models.

## Core Explanation

Prompt Injection represents a sophisticated form of attack where an adversary embeds malicious instructions into untrusted inputs processed by LLMs, thereby manipulating the model's behavior to perform actions contrary to its intended purpose. This can range from exfiltrating sensitive information to executing unauthorized commands with real-world consequences.

The foundational mechanism behind Prompt Injection lies in exploiting the way LLMs process and interpret input data. By embedding specific instructions within untrusted inputs, attackers can manipulate the model's output without altering the system prompt itself, making detection challenging due to the indistinguishability of malicious from legitimate instructions.

This attack vector is particularly dangerous in agentic systems where LLMs have authority over external resources. Unlike single-turn chat applications, agentic LLMs act on their instructions through tool calls with real-world consequences, amplifying the potential harm caused by injected prompts that could lead to unauthorized actions or data exfiltration.

The theoretical underpinnings of Prompt Injection highlight the inherent limitations in current LLM architectures. These models cannot reliably distinguish between trusted and adversarial instructions within untrusted inputs, making it difficult to implement robust defenses against such attacks.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design for LLMs, Prompt Injection poses a significant threat as malicious instructions can be embedded within training data or user inputs. This could lead to the model generating harmful content or performing unauthorized actions based on these injected prompts, undermining the integrity and safety of the system.

> [!example] **Application 2 — Agentic systems**
> In agentic systems where LLMs have authority over external resources, Prompt Injection can result in severe consequences. For instance, an injected prompt could instruct the model to exfiltrate user data or make unauthorized API calls, leading to privacy breaches and security vulnerabilities that persist beyond a single conversation session.

## Key Distinctions

> [!key-distinction] **Prompt Injection vs other forms of adversarial attacks**
> While Prompt Injection involves embedding malicious instructions within untrusted inputs processed by LLMs, other forms of adversarial attacks may target different aspects of the system. For example, model poisoning attacks alter training data to induce specific behaviors in the model, whereas evasion attacks manipulate input data to bypass detection mechanisms without necessarily embedding new instructions.

## Open Questions

> [!open-question] **Question**
> Can Prompt Injection be reliably detected?
>
> *What would resolve it:* A reliable method for detecting malicious instructions embedded within untrusted inputs processed by LLMs would resolve this question, potentially involving advanced natural language processing techniques or machine learning models trained to identify suspicious patterns.

> [!open-question] **Question**
> What are the most effective strategies for mitigating Prompt Injection risks in LLMs?
>
> *What would resolve it:* Strategies that effectively mitigate the risk of Prompt Injection would involve a combination of input sanitization, instruction hierarchy separation, and output monitoring. Evidence demonstrating their efficacy across various attack scenarios would resolve this question.

## Synthesis

Understanding Prompt Injection is crucial for securing LLMs against adversarial attacks that exploit the model's processing capabilities to perform unauthorized actions or exfiltrate information. This concept underscores the need for robust security measures in agentic systems where models have authority over external resources, highlighting the importance of continuous research and development in this area.

## Connections & Context

**Falls under:** [[Adversarial Attacks on AI Systems]]

**Specializes:** [[Tool Use in LLMs]]

**Contrasts with:** [[Jailbreaking]]

**Applies to:** [[Instruction Hierarchy Conflict]]

**Source:** [[prompt-injection-synthetic-seed-2026-05-20]]
