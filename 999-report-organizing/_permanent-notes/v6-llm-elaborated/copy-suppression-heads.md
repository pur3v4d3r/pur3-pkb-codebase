---
title: Copy-Suppression Heads
aliases:
  - Copy-Suppression Heads
  - anti-copy heads
  - negative attention heads
  - suppression heads
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - prompt-engineering

domain: prompt-engineering
subdomains:
  - mechanistic-interpretability
  - large-language-models
  - natural-language-generation

created: 2026-05-22
updated: '2026-05-23'
source-type: report-extraction
source-reports:
  - copy-suppression-heads-synthetic-seed-2026-05-22
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: elaborated
parent-concept: Attention Head Specialization
related:
  - '[[Induction Heads]]'
  - '[[Attention Head Specialization]]'
prerequisites:
  - '[[]]'
specializes:
  - '[[]]'
broader:
  - '[[]]'
see-also:
  - '[[]]'
contrasts-with:
  - '[[Induction Heads]]'
contradicts:
  - '[[]]'
applies-to:
  - '[[]]'
formalizes:
  - '[[]]'
instance-of:
  - '[[Attention Head Specialization]]'
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
  last-diagrammed: '2026-05-23'
---

## 📊 Visual Overview

<!-- diagram-pass:1 (2026-05-23) -->

> [!abstract] **Diagram 1 — Copy-Suppression Mechanism Overview**
> *Follow the flow from input to output, noting the role of copy-suppression heads in generating creative text.*
>
> ```mermaid
> flowchart LR
>   A[Input Tokens] --> B[Attention Heads]
>   B --> C[Token Generation]
>   D[Copy-Suppression Heads] -->|Penalize Repetitive Sequences| E[Creative Output]
>   C --> E
> ```


> [!abstract] **Diagram 2 — Comparison with Induction Heads**
> *Compare the roles of copy-suppression and induction heads in generating text.*
>
> ```mermaid
> graph TD
>   A[Copy-Suppression Heads] -->|Penalize Repetitive Sequences| B[Creative Output]
>   C[Induction Heads] -->|Boost Pattern Completion| D[Adequate Recall]
> ```


> [!abstract] **Diagram 3 — Task Influence on Copy-Suppression Strength**
> *Observe how different tasks affect the strength of copy-suppression heads.*
>
> ```mermaid
> flowchart LR
>   A[Abstractive Tasks] --> B[Strong Copy-Suppression]
>   C[Extractive Tasks] --> D[Weak Copy-Suppression]
> ```

# Copy-Suppression Heads

> [!definition] **Copy-Suppression Heads**
> Copy-suppression heads are specialized attention mechanisms within transformer models that reduce the likelihood of generating tokens identical to those recently seen in the source context, thereby preventing repetitive copying and promoting more creative text generation. Unlike induction heads which enhance pattern completion, copy-suppression heads serve as an inhibitory mechanism, ensuring a balance between high fidelity (accurate recall) and high creativity (novel synthesis). This concept falls under attention head specialization, highlighting its role in fine-tuning model behavior for specific tasks.

> [!attention] **Boundary**
> This concept is distinct from induction heads which enhance pattern completion. It should not be confused with mechanisms solely focused on recall or generation without balancing both aspects.

## Core Explanation

Copy-suppression heads play a critical role in transformer models by mitigating the tendency to generate text that is merely a copy of input tokens. In practice, this mechanism ensures that when a model is tasked with paraphrasing or summarizing content, it does not default to verbatim reproduction but instead generates novel and relevant output. This balance between recall and generation is crucial for tasks requiring semantic understanding rather than rote repetition.

The tension between high fidelity (accurate copying) and high creativity (novel synthesis) is a fundamental challenge in language model design. Copy-suppression heads address this by penalizing token sequences that closely match recent source-context tokens, thereby encouraging the generation of more abstract or paraphrased content. This mechanism is particularly important for abstractive tasks where verbatim repetition would indicate failure to process input semantically.

Analysis has shown that models trained on abstractive tasks develop stronger copy-suppression capabilities compared to those trained on extractive tasks. This suggests that the strength of copy-suppression heads can be calibrated based on task requirements, allowing for a more nuanced approach to text generation where creativity and fidelity are balanced according to need.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional settings, copy-suppression heads can significantly impact how models generate educational content. For instance, when designing a model to paraphrase textbook material for accessibility purposes, strong copy-suppression ensures that the output is not merely a direct copy of the original text but rather a rephrased version that maintains the core meaning while being more accessible or engaging.

> [!example] **Application 2 — Legal document processing**
> In legal contexts where verbatim reproduction of source documents is critical, over-suppression by copy-suppression heads can lead to errors. For example, if a model tasked with summarizing a contract fails to accurately reproduce specific clauses due to excessive suppression, the summary may be legally insufficient or misleading.

## Key Distinctions

> [!key-distinction] **Copy-Suppression vs Induction**
> While induction heads enhance pattern completion by boosting the probability of generating tokens that match recent source-context sequences, copy-suppression heads operate in opposition. They penalize naive token copying to prevent repetitive patterns and encourage more creative or abstract text generation.

## Open Questions

> [!open-question] **Question**
> How can copy-suppression be calibrated to balance between creativity and fidelity?
>
> *What would resolve it:* Empirical studies comparing model performance across a range of tasks with varying levels of copy-suppression could provide insights into optimal calibration strategies.

> [!open-question] **Question**
> What are the implications for model training on different types of tasks?
>
> *What would resolve it:* Research examining how task type influences the development and effectiveness of copy-suppression mechanisms would help in tailoring models to specific applications.

## Synthesis

Understanding copy-suppression heads is crucial for advancing language model capabilities, particularly in tasks requiring abstractive text generation. By balancing fidelity and creativity, these specialized attention heads enable more nuanced and contextually appropriate outputs, enhancing the utility of transformer models across a wide range of applications.

## Connections & Context

**Falls under:** [[Attention Head Specialization]]

**Contrasts with:** [[Induction Heads]]

**Instance of:** [[Attention Head Specialization]]

**Source:** [[copy-suppression-heads-synthetic-seed-2026-05-22]]
