---
title: Repair Prompting
aliases:
  - Repair Prompting
  - code repair prompts
  - bug repair prompting
  - automated program repair prompting
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - prompt-engineering

domain: prompt-engineering
subdomains:
  - software-engineering
  - prompt-engineering
  - program-synthesis

created: 2026-05-20
updated: '2026-05-23'
source-type: report-extraction
source-reports:
  - repair-prompting-synthetic-seed-2026-05-20
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: enhanced
parent-concept: Code Generation Techniques
related:
  - '[[Self-Debugging LLMs]]'
  - '[[Execution Feedback Prompting]]'
prerequisites:
  - '[[]]'
specializes:
  - '[[]]'
broader:
  - '[[]]'
see-also:
  - '[[]]'
contrasts-with:
  - '[[Self-Debugging LLMs]]'
contradicts:
  - '[[]]'
applies-to:
  - '[[Execution Feedback Prompting]]'
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
  enhancement-passes: 1
  enhancement-model: qwen2.5:14b-instruct-q5_K_M
  enhancement-method: enhance_notes-v1
  last-enhanced: '2026-05-23'
  diagram-passes: 1
  diagram-model: qwen2.5:14b-instruct-q5_K_M
  last-diagrammed: '2026-05-23'
---

## 📊 Visual Overview

<!-- diagram-pass:1 (2026-05-23) -->

> [!abstract] **Diagram 1 — Repair Prompting Process Flow**
> *Follow the flow from input to output, noting key steps.*
>
> ```mermaid
> flowchart LR
>   A[Developer Identifies Bug] --> B[Provide Defect Info]
>   B --> C[Input Faulty Code and Info]
>   C --> D[LLM Analyzes and Corrects]
>   D --> E[Output Fixed Code]
> ```


> [!abstract] **Diagram 2 — Comparison of Repair Prompting vs Self-Debugging**
> *Compare the two approaches to understand their differences.*
>
> ```mermaid
> graph TD
>   A[Repair Prompting]
>   B[Self-Debugging]
>   C{Defect Information Provided}
>   D{Model Diagnoses Errors Alone}
>   E(Targeted Solution)
>   F(Generalized Solution)
>   G(Type I & II Errors Minimized)
>   H(Type I & II Errors Common)
>   A -->|Yes| C
>   B -->|No| D
>   C -->|Guided| E
>   D -->|Unconstrained| F
>   A -->|Minimized| G
>   B -->|Common| H
> ```


> [!abstract] **Diagram 3 — Type I & II Errors in Repair Prompting**
> *Identify the conditions leading to each error type.*
>
> ```mermaid
> stateDiagram-v2
>   [*] --> TypeIError
>   TypeIError: False Positive (Model Identifies Nonexistent Issue)
>   TypeIError --> [*]
>   [*] --> TypeIIError
>   TypeIIError: False Negative (Model Misses Real Defect)
>   TypeIIError --> [*]
> ```

## Core Explanation

Repair Prompting is a method that leverages large language models (LLMs) to correct defects in code by providing them with both the faulty code and specific information about the defect. This technique can be applied in various contexts, such as automated program repair systems or interactive development assistants, where it helps streamline the debugging process. By offering explicit details on what is wrong, Repair Prompting guides the model towards a more targeted solution rather than requiring it to regenerate the entire function from scratch.

The foundational mechanism of Repair Prompting relies on the ability of LLMs to understand and interpret natural language descriptions or other forms of defect information provided alongside the defective code. This approach constrains the revision process, focusing the model's attention on relevant sections of the code that need fixing. In practice, this means that developers can use Repair Prompting to quickly address known bugs without having to manually diagnose each issue from scratch.

The theoretical underpinnings of Repair Prompting draw upon principles of natural language processing and machine learning, particularly in how these models are trained to understand and generate code based on given prompts. By integrating defect information into the prompt, Repair Prompting leverages the model's ability to learn from examples and apply that knowledge to specific coding scenarios.

Empirically, Repair Prompting has shown promise in improving efficiency and accuracy in automated program repair systems. For instance, it can help reduce the time spent on manual debugging by automating parts of the process where defects are well-defined but their solutions are not immediately obvious.

<!-- enhancement-pass:1 (2026-05-23) -->
Repair Prompting not only aids in immediate bug fixing but also plays a crucial role in enhancing developers' understanding of their own codebases. By engaging with the process of specifying defects and observing how these descriptions guide corrections, developers can gain deeper insights into common pitfalls and best practices within their specific programming contexts.

## Practical Implications

> [!example] **Application 1 — Automated Program Repair**
> In automated program repair, Repair Prompting can significantly enhance the efficiency and effectiveness of bug fixing. By providing a model with detailed defect information alongside the faulty code, developers can quickly generate corrected versions without having to manually diagnose each issue from scratch. This not only saves time but also ensures that fixes are more targeted and less likely to introduce new defects.

> [!example] **Application 2 — Interactive Development Assistants**
> Interactive development assistants benefit greatly from Repair Prompting by offering real-time feedback on code issues. When a developer encounters a bug, they can use Repair Prompting to get immediate suggestions for corrections based on the specific defect information provided. This interactive approach not only speeds up the debugging process but also helps developers learn from their mistakes and improve their coding skills over time.

## Key Distinctions

> [!key-distinction] **Repair Prompting vs Self-Debugging**
> While both Repair Prompting and self-debugging aim to correct defects in code, they differ fundamentally in how they approach the task. Repair Prompting relies on explicit defect information provided by developers or automated tools, guiding the model towards a more targeted solution. In contrast, self-debugging involves models diagnosing errors from the code alone without additional guidance, which can be less precise and more time-consuming.

<!-- enhancement-pass:1 (2026-05-23) -->

> [!key-distinction] **Type I vs Type II Errors in Repair Prompting**
> In the context of automated program repair, Type I errors (false positives) occur when a model incorrectly identifies an issue where there is none, while Type II errors (false negatives) happen when it fails to detect a real defect. Understanding these error types helps refine how defect information is provided in Repair Prompting, aiming for more accurate and reliable bug fixes.

## Open Questions

> [!open-question] **Question**
> How can the reliability of Repair Prompting be improved to avoid introducing new defects?
>
> *What would resolve it:* Further research into refining defect descriptions and incorporating broader context could help improve the reliability of Repair Prompting.

> [!open-question] **Question**
> What are the long-term impacts of using Repair Prompting in automated program repair systems?
>
> *What would resolve it:* Longitudinal studies tracking the performance and maintenance costs associated with code repaired through Repair Prompting would provide valuable insights into its long-term effectiveness.

<!-- enhancement-pass:1 (2026-05-23) -->

> [!open-question] **Question**
> How does the specificity and clarity of defect descriptions impact the effectiveness of Repair Prompting?
>
> *What would resolve it:* Further research into how varying levels of detail in defect descriptions affect model performance could provide insights into optimizing this aspect of Repair Prompting.

## Synthesis

Repair Prompting stands out as a powerful technique in code generation, offering significant improvements over traditional debugging methods. By providing explicit defect information to constrain the model's revision process, it enables more efficient and accurate bug fixing. This not only saves time but also enhances overall code quality by focusing on targeted corrections rather than broad regenerations.

Moreover, Repair Prompting integrates seamlessly with other techniques like Execution Feedback Prompting, where feedback is used iteratively to improve code generation. Together, these methods form a robust framework for enhancing the reliability and efficiency of automated program repair systems.

<!-- enhancement-pass:1 (2026-05-23) -->
Repair Prompting, by integrating explicit defect information with LLM capabilities, not only accelerates the debugging process but also fosters a deeper understanding among developers. This dual benefit positions it as a pivotal technique in modern code generation and maintenance practices.

## Connections & Context

**Falls under:** [[Code Generation Techniques]]

**Contrasts with:** [[Self-Debugging LLMs]]

**Applies to:** [[Execution Feedback Prompting]]

**Source:** [[repair-prompting-synthetic-seed-2026-05-20]]

<!-- enhancement-pass:1 (2026-05-23) -->

### Why these connections matter

> [!connection] **[[Execution Feedback Prompting]]** — *applies-to*
> Repair Prompting can be seen as a specific application of Execution Feedback Prompting in the context of code repair. Both techniques leverage feedback to improve outcomes, but Repair Prompting focuses on correcting defects based on explicit information about what is wrong, whereas Execution Feedback Prompting may use broader execution data.


# Repair Prompting

> [!definition] **Repair Prompting**
> Repair Prompting is a technique within code generation that involves presenting a model with defective code and specific defect information to generate a corrected version of the code. Unlike self-debugging, where models diagnose errors without explicit defect descriptions, Repair Prompting provides clear guidance on what needs fixing, thereby narrowing down the solution space. It falls under Code Generation Techniques.

> [!attention] **Boundary**
> It excludes self-debugging, where models diagnose errors without explicit defect descriptions. It should not be confused with general code regeneration from scratch.
