---
title: Hallucination Taxonomy
aliases:
  - Hallucination Taxonomy
  - LLM hallucination types
  - hallucination classification
  - confabulation taxonomy
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - prompt-engineering

domain: prompt-engineering
subdomains:
  - factuality
  - model-behaviour

created: 2026-05-20
updated: '2026-05-21'
source-type: report-extraction
source-reports:
  - hallucination-taxonomy-synthetic-seed-2026-05-20
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: enhanced
parent-concept: Prompt-Engineering
related:
  - '[[Hallucination Detection]]'
  - '[[Factual Consistency Evaluation]]'
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
  - '[[Hallucination Detection]]'
formalizes:
  - '[[]]'
instance-of:
  - '[[]]'
supports:
  - '[[Factual Consistency Evaluation]]'
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
  enhancement-passes: 1
  enhancement-model: qwen2.5:14b-instruct-q5_K_M
  enhancement-method: enhance_notes-v1
  last-enhanced: '2026-05-20'
  diagram-passes: 1
  diagram-model: qwen2.5:14b-instruct-q5_K_M
  last-diagrammed: '2026-05-21'
---

## 📊 Visual Overview

<!-- diagram-pass:1 (2026-05-21) -->

> [!abstract] **Diagram 1 — Hallucination Types Overview**
> *Identify the three types of hallucinations and their characteristics.*
>
> ```mermaid
> graph TD
>   A[Intrinsic Hallucinations]
>   B[Extrinsic Hallucinations]
>   C[Factual Hallucinations]
>   A -->|Contradicts Source Material| D[Error Origin]
>   B -->|Introduces Unverifiable Claims| E[Error Origin]
>   C -->|Contradicts Verifiable Knowledge| F[Error Origin]
> ```


> [!abstract] **Diagram 2 — Hallucination Taxonomy Flow**
> *Follow the flow to understand how errors are categorized.*
>
> ```mermaid
> flowchart LR
>   A[Source Material]
>   B[Factual Knowledge]
>   C[Output]
>   D[Intrinsic Hallucinations] -->|Contradicts Source Material|
>   E[Extrinsic Hallucinations] -->|Introduces Unverifiable Claims|
>   F[Factual Hallucinations] -->|Contradicts Verifiable Knowledge|
>   A --> D
>   B --> F
>   C --> E
> ```


> [!abstract] **Diagram 3 — Reflective vs Reactive Thinking**
> *Compare reflective and reactive thinking approaches.*
>
> ```mermaid
> graph TD
>   A[Reflective]
>   B[Reactive]
>   C[Error Detection]
>   D[Immediate Response]
>   A -->|Deliberate Review| C
>   B -->|Available Cues| D
> ```

# Hallucination Taxonomy

> [!definition] **Hallucination Taxonomy**
> Hallucination Taxonomy categorizes fabrications and factual errors produced by language models into intrinsic, extrinsic, and factual hallucinations based on their relation to source material or verifiable knowledge. It excludes non-fabrication errors such as omissions or incomplete responses, focusing solely on the types of inaccuracies that can mislead users. This taxonomy falls under prompt-engineering, providing a structured framework for understanding and addressing these issues.

> [!attention] **Boundary**
> It excludes non-fabrication errors such as omissions or incomplete responses. It should not be confused with error classification in other domains like cognitive psychology.

## Core Explanation

Hallucination Taxonomy is crucial in rigorously evaluating language models by categorizing errors into intrinsic, extrinsic, and factual hallucinations. Intrinsic hallucinations occur when the model's output contradicts provided source material, while extrinsic hallucinations introduce claims not derivable from or verifiable against the source. Factual hallucinations, on the other hand, contradict verifiable world knowledge. This taxonomy is essential for researchers to compare methods targeting different types of errors effectively.

The importance of Hallucination Taxonomy lies in its ability to provide a common language and framework for discussing and mitigating these issues. Without such a structured approach, progress in reducing hallucinations can be misleading or inconsistent across studies. For instance, improvements in one category might mask regressions in another if the taxonomy is not strictly adhered to.

The theoretical roots of Hallucination Taxonomy are grounded in the need for precise error classification within language model evaluation. This precision allows researchers and practitioners to focus on specific types of errors that can be systematically addressed through targeted interventions, rather than treating all inaccuracies as a single, undifferentiated problem.

In practice, applying this taxonomy requires careful consideration of what constitutes 'source material' in different contexts, particularly in retrieval-augmented generation (RAG) systems where the source is implicitly defined by the retrieved corpus. This ambiguity can complicate efforts to standardize measurements and comparisons across studies.

<!-- enhancement-pass:1 (2026-05-20) -->
The taxonomy's utility extends beyond mere classification; it also informs the development of mitigation strategies tailored to each hallucination type. For instance, intrinsic hallucinations might be addressed by refining how models process and integrate source material, whereas extrinsic hallucinations could require improvements in model training data or generation algorithms.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design, understanding Hallucination Taxonomy is crucial for creating prompts that minimize the risk of hallucinations. By designing prompts that clearly delineate source material and factual knowledge, designers can reduce the likelihood of extrinsic or intrinsic hallucinations. Ignoring this taxonomy could result in prompts that inadvertently introduce errors into educational content.

> [!example] **Application 2 — Content moderation**
> In content moderation, Hallucination Taxonomy helps identify and mitigate harmful misinformation generated by language models. By classifying errors as intrinsic, extrinsic, or factual hallucinations, moderators can apply targeted strategies to address specific types of inaccuracies. Ignoring this taxonomy might lead to ineffective or overly broad moderation policies that fail to address the root causes of misinformation.

## Key Distinctions

> [!key-distinction] **Intrinsic vs Extrinsic Hallucinations**
> The distinction between intrinsic and extrinsic hallucinations is critical for understanding where errors originate. Intrinsic hallucinations arise when a model's output contradicts provided source material, indicating an issue with how the model processes or interprets that information. Extrinsic hallucinations introduce claims not derivable from or verifiable against the source, suggesting a failure in generating coherent and consistent outputs based on available data.

<!-- enhancement-pass:1 (2026-05-20) -->

> [!key-distinction] **Reflective vs Reactive Thinking**
> Reflective thinking involves deliberate review and analysis of information before responding, which can help catch errors. In contrast, reactive thinking relies on immediate responses based on available cues without deeper consideration. Reflective approaches are more likely to prevent hallucinations by allowing for error detection during the generation process.

> [!key-distinction] **Type I vs Type II Error**
> In the context of Hallucination Taxonomy, Type I errors (false positives) occur when a model incorrectly identifies factual information as false or contradictory. Conversely, Type II errors (false negatives) happen when actual inaccuracies are overlooked. Understanding these error types is crucial for developing robust detection and correction mechanisms.

## Common Misconceptions

<!-- enhancement-pass:1 (2026-05-20) -->

> [!warning] **Misconception** — People think Hallucination Taxonomy only applies to large language models.
>
> While the taxonomy was developed with large language models in mind, its principles can be applied to any system that generates text or information. This includes smaller models and even non-AI systems where fabricated claims might arise.

## Key Figures

- **John Sweller** — While John Sweller is known for his work in cognitive load theory rather than directly contributing to Hallucination Taxonomy, the principles of cognitive load can inform how we understand and mitigate intrinsic hallucinations by focusing on reducing extraneous cognitive demands placed on language models.

## Open Questions

> [!open-question] **Question**
> How can we standardize the application of Hallucination Taxonomy across different studies?
>
> *What would resolve it:* Developing clear guidelines and best practices for defining source material in various contexts would help ensure consistent taxonomy application, facilitating more reliable cross-study comparisons.

> [!open-question] **Question**
> What are the most effective methods for mitigating specific types of hallucinations?
>
> *What would resolve it:* Empirical studies comparing different mitigation strategies across intrinsic, extrinsic, and factual hallucinations would provide evidence-based recommendations for reducing these errors in language models.

<!-- enhancement-pass:1 (2026-05-20) -->

> [!open-question] **Question**
> How do different training methodologies impact the likelihood of hallucinations?
>
> *What would resolve it:* Investigating how various training techniques influence model behavior could reveal strategies to reduce hallucination rates. This might involve analyzing the effects of data augmentation, regularization methods, or specific architectural choices.

## Synthesis

Understanding Hallucination Taxonomy is crucial for advancing the evaluation and improvement of language models. By providing a structured framework for classifying errors, it enables researchers to develop targeted strategies for mitigating specific types of inaccuracies, leading to more reliable and trustworthy AI systems.

<!-- enhancement-pass:1 (2026-05-20) -->
By integrating insights from cognitive psychology and machine learning, Hallucination Taxonomy not only aids in identifying errors but also guides the development of more robust AI systems capable of generating accurate and reliable information.

## Evidence

Hallucination Taxonomy is essential for rigorous research into language model errors because without a shared taxonomy, methods targeting different hallucination types are compared on incompatible metrics. This can lead to misleading conclusions about progress in reducing inaccuracies. For instance, improvements in one category might mask regressions in another if the taxonomy is not strictly adhered to.

## Connections & Context

**Falls under:** [[Prompt-Engineering]]

**Applies to:** [[Hallucination Detection]]

**Supports:** [[Factual Consistency Evaluation]]

**Source:** [[hallucination-taxonomy-synthetic-seed-2026-05-20]]

<!-- enhancement-pass:1 (2026-05-20) -->

### Why these connections matter

> [!connection] **[[Factual Consistency Evaluation]]** — *supports*
> Hallucination Taxonomy supports Factual Consistency Evaluation by providing a structured approach to identify and categorize inaccuracies. This taxonomy enables evaluators to systematically assess the consistency of generated content with known facts, enhancing the reliability of evaluations.
