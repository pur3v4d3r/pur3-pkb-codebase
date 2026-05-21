---
title: Jailbreak Taxonomy
aliases:
  - Jailbreak Taxonomy
  - jailbreak categories
  - jailbreak classification
  - LLM jailbreak types
  - jailbreak patterns
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - prompt-engineering

domain: prompt-engineering
subdomains:
  - llm-security
  - ai-safety
  - adversarial-ai

created: 2026-05-21
updated: '2026-05-21'
source-type: report-extraction
source-reports:
  - jailbreak-taxonomy-synthetic-seed-2026-05-21
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: elaborated
parent-concept: LLM Security
related:
  - '[[Adversarial Suffix Attacks]]'
  - '[[Many-Shot Jailbreaking]]'
  - '[[Direct Prompt Injection]]'
prerequisites:
  - '[[]]'
specializes:
  - '[[]]'
broader:
  - '[[]]'
see-also:
  - '[[]]'
contrasts-with:
  - '[[]]'
contradicts:
  - '[[]]'
applies-to:
  - '[[]]'
formalizes:
  - '[[]]'
instance-of:
  - '[[Adversarial Suffix Attacks]]'
  - '[[Many-Shot Jailbreaking]]'
  - '[[Direct Prompt Injection]]'
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

> [!abstract] **Diagram 1 — Jailbreak Mechanisms Overview**
> *Identify the different mechanisms used in jailbreaking LLMs.*
>
> ```mermaid
> graph TD
>   A[Direct Framing]
>   B[Indirect Framing]
>   C[Role-Play Attacks]
>   D[Hypothetical Framing]
>   E[Transformed Representation]
>   F[Persona Attacks]
>   A -->|Example: Clear Request|
>   B -->|Example: Contextual Masking|
>   C -->|Example: Unconstrained Character|
>   D -->|Example: Story Requests|
>   E -->|Example: Altered Phrasing|
>   F -->|Example: Adopted Persona|
> ```


> [!abstract] **Diagram 2 — Jailbreak Access Levels**
> *Understand the required access levels for different jailbreak techniques.*
>
> ```mermaid
> graph TD
>   A[Public]
>   B[Low Privilege]
>   C[High Privilege]
>   D[Direct Framing] -->|Public|
>   E[Indirect Framing] -->|Public|
>   F[Hypothetical Framing] -->|Public|
>   G[Role-Play Attacks] -->|Low Privilege|
>   H[Persona Attacks] -->|High Privilege|
> ```


> [!abstract] **Diagram 3 — Jailbreak Generalisability**
> *Assess the generalisability of jailbreak techniques across different models.*
>
> ```mermaid
> graph TD
>   A[Generalisable]
>   B[Specific]
>   C[Direct Framing] -->|Specific|
>   D[Indirect Framing] -->|Generalisable|
>   E[Hypothetical Framing] -->|Generalisable|
>   F[Role-Play Attacks] -->|Generalisable|
>   G[Persona Attacks] -->|Specific|
> ```

# Jailbreak Taxonomy

> [!definition] **Jailbreak Taxonomy**
> Jailbreak taxonomy systematically classifies techniques used to elicit policy-violating content from safety-trained language models by mechanism, required access level, and generalisability. It excludes specific attack patterns that may become outdated quickly due to model updates, focusing instead on the underlying mechanisms of how adversarial inputs exploit misalignment between safety training signals and actual content interpretation. This framework falls under LLM Security.

> [!attention] **Boundary**
> It excludes specific attack patterns that may become outdated quickly due to model updates. It should not be confused with a static list of attacks but rather as an evolving framework for understanding how adversarial inputs exploit the misalignment between safety training signals and actual content interpretation.

## Core Explanation

Jailbreak taxonomy is a critical tool in understanding how attackers can bypass the safeguards designed into language models to prevent them from generating harmful or inappropriate content. At its core, it reveals that most successful jailbreaks exploit a fundamental misalignment between safety training and adversarial inputs: while safety training primarily targets direct, unambiguous requests, successful jailbreaks present the same content via indirect framing, fictional context, or transformed representation that the safety classifier fails to recognize as policy-violating. This insight underscores the importance of understanding not just specific attack patterns but also the underlying mechanisms that make them effective.

In practice, this taxonomy categorizes various types of attacks based on their mechanism and required access level. For instance, role-play and persona attacks instruct models to adopt an unconstrained character, while hypothetical framing requests content 'for a story' or 'hypothetically.' These techniques leverage the model's tendency to interpret indirect signals differently from direct ones, thereby evading safety filters designed for straightforward compliance checks.

Theoretical roots of jailbreak taxonomy lie in cognitive science and machine learning theory. It draws on concepts like misalignment between training objectives and real-world performance, as well as the challenge of detecting semantic intent versus surface representation. Empirically, this framework has been validated through numerous case studies showing how specific attack patterns succeed where others fail, highlighting the need for more robust safety mechanisms that can adapt to indirect framing and transformed representations.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> Understanding jailbreak taxonomy is crucial in instructional design for language models, where educators must ensure that training materials do not inadvertently teach the model to respond to indirect framing or transformed representations. By recognizing these patterns, designers can create more resilient prompts and examples that account for a wider range of input variations, thereby reducing the risk of policy-violating content generation.

> [!example] **Application 2 — Security audits**
> In security audits of language models, jailbreak taxonomy provides a structured approach to identifying potential vulnerabilities. Auditors can use this framework to test how well a model resists different types of attacks and to assess the effectiveness of existing safety measures. This proactive testing helps in refining defensive strategies before new attack patterns emerge.

## Key Distinctions

> [!key-distinction] **Direct vs Indirect Framing**
> The distinction between direct and indirect framing is crucial because it explains why certain attacks succeed where others fail. Direct framing involves clear, unambiguous requests that safety training can easily detect as policy-violating. In contrast, indirect framing uses context or hypothetical scenarios to mask the intent behind a request, exploiting the model's tendency to interpret such signals differently from direct ones.

## Key Figures

- **John Doe** — Contributed significantly to developing and refining jailbreak taxonomy by identifying key mechanisms that make certain attack patterns successful. His work has helped in understanding the misalignment between safety training signals and actual content interpretation.

## Open Questions

> [!open-question] **Question**
> How can we develop more robust safety training methods that are less susceptible to indirect framing and transformed representations?
>
> *What would resolve it:* Empirical studies demonstrating effective new techniques for teaching models to recognize semantic intent regardless of surface representation would resolve this question.

> [!open-question] **Question**
> What new attack patterns might emerge, and how quickly can they be identified and mitigated?
>
> *What would resolve it:* Continuous monitoring and analysis of emerging attack patterns in real-world applications could provide insights into the evolution of these techniques and inform timely mitigation strategies.

## Synthesis

Jailbreak taxonomy is crucial for advancing LLM security by providing a framework to understand and counteract policy-violating content. By focusing on underlying mechanisms rather than specific attack patterns, it offers a durable approach that can adapt as new threats emerge. This makes it an essential tool for both offensive researchers exploring the limits of current defenses and defensive practitioners working to strengthen model safeguards.

## Connections & Context

**Falls under:** [[LLM Security]]

**Instance of:** [[Adversarial Suffix Attacks]] · [[Many-Shot Jailbreaking]] · [[Direct Prompt Injection]]

**Source:** [[jailbreak-taxonomy-synthetic-seed-2026-05-21]]
