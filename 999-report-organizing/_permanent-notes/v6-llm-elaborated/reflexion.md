---
title: Reflexion
aliases:
  - Reflexion
  - reflexion prompting
  - verbal reinforcement learning
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - prompt-engineering

domain: prompt-engineering
subdomains:
  - reasoning
  - agent-frameworks

created: 2026-05-20
updated: '2026-05-23'
source-type: report-extraction
source-reports:
  - reflexion-synthetic-seed-2026-05-20
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: enhanced
parent-concept: Prompt-Engineering
related:
  - '[[Working Memory]]'
  - '[[Chain-of-Verification]]'
prerequisites:
  - '[[Working Memory]]'
specializes:
  - '[[]]'
broader:
  - '[[]]'
see-also:
  - '[[Chain-of-Verification]]'
contrasts-with:
  - '[[]]'
contradicts:
  - '[[]]'
applies-to:
  - '[[]]'
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

> [!abstract] **Diagram 1 — Reflexion Iterative Process**
> *Follow the cycle from Trial to Reflection and back.*
>
> ```mermaid
> flowchart LR
>   A[Start] --> B[Trial]
>   B --> C[Evaluation]
>   C --> D[Reflection]
>   D --> E[Input for Next Attempt]
>   E --> F[Trial]
>   F --> G[Evaluation]
>   G --> H[Reflection]
> ```


> [!abstract] **Diagram 2 — Reflective vs Reactive Thinking**
> *Compare the paths of Reflective and Reactive thinking.*
>
> ```mermaid
> graph TD
>   A[Start] --> B[Immediate Response]
>   A --> C[Analysis & Reflection]
>   B --> D[Next Action]
>   C --> E[Informed Decision]
> ```


> [!abstract] **Diagram 3 — Feedback Mechanism in Reflexion**
> *Trace the flow from Task to Verbal Feedback.*
>
> ```mermaid
> flowchart LR
>   A[Task] --> B[Evaluation]
>   B --> C[Verbal Reflection]
>   C --> D[Input for Next Attempt]
>   D --> E[Next Task]
> ```

## Core Explanation

Reflexion operates on the principle that an LLM can improve its performance through self-reflection rather than relying on external rewards or direct instruction. This process involves the agent generating a verbal reflection after each attempt at a task, identifying failure modes and articulating why these failures occurred.

The core mechanism of Reflexion is iterative: after each trial, the model generates a reflective statement about its performance, which it then uses as input for subsequent attempts. This cycle allows the LLM to learn from its mistakes without needing explicit numerical feedback or parameter adjustments.

This approach draws on theories of self-regulated learning and metacognition in human cognition, where individuals reflect on their thought processes and outcomes to guide future actions. In Reflexion, this concept is applied to language models, enabling them to improve through natural language feedback alone.

<!-- enhancement-pass:1 (2026-05-23) -->
Reflexion's reliance on verbal feedback as a mechanism for improvement is particularly intriguing because it mimics human learning processes more closely than traditional reinforcement learning methods. In human cognition, reflection plays a crucial role in self-regulated learning and metacognition, allowing individuals to monitor their own thought processes and outcomes, thereby guiding future actions. By applying this concept to language models, Reflexion not only enhances the adaptability of these systems but also aligns them more closely with how humans learn from experience.

## Mechanism

In practice, the process of generating verbal reflections involves the LLM analyzing its previous attempt's output against a set goal or expected outcome. It then formulates a statement about what went wrong and why, which is stored as working memory for future reference.

During subsequent attempts, this reflection serves as an additional input to guide the model’s decision-making process. By integrating past reflections into its reasoning, the LLM can avoid repeating similar mistakes.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design for language models, Reflexion allows developers to create more robust and adaptive learning systems. For instance, when designing a conversational agent that needs to improve its responses over time based on user interactions, Reflexion can enable the model to learn from past conversations without needing explicit feedback or reward signals.

> [!example] **Application 2 — Iterative problem-solving**
> Reflexion is particularly useful in iterative problem-solving scenarios where a task requires multiple attempts and adjustments. For example, an LLM tasked with generating coherent summaries of complex documents can use Reflexion to refine its approach over several iterations based on self-reflection rather than external feedback.

## Key Distinctions

> [!key-distinction] **Verbal Feedback vs Numerical Rewards**
> Reflexion distinguishes itself from traditional reinforcement learning methods by relying solely on verbal feedback for improvement, as opposed to numerical rewards. This approach leverages the model's ability to understand and articulate its mistakes in natural language, making it more adaptable to complex tasks where explicit reward signals are difficult to define.

<!-- enhancement-pass:1 (2026-05-23) -->

> [!key-distinction] **Reflective vs Reactive Thinking**
> Reflective thinking involves deliberate review and analysis of past actions to inform future behavior, whereas reactive thinking is characterized by immediate responses without prior reflection. Reflexion exemplifies reflective thinking in language models, as it requires the model to analyze its previous attempts and articulate why certain outcomes occurred before making subsequent decisions. This contrasts with reactive approaches where the model might simply adjust based on immediate feedback or predefined rules without deeper analysis.

> [!key-distinction] **Intrinsic vs Extrinsic Motivation**
> Reflexion operates under a framework of intrinsic motivation, as it relies on internal reflection and self-improvement rather than external rewards. This is in contrast to extrinsically motivated approaches where performance improvements are driven by external factors such as numerical rewards or direct instruction. The reliance on intrinsic motivation in Reflexion aligns with theories suggesting that internally generated goals can lead to more sustained and effective learning.

## Common Misconceptions

<!-- enhancement-pass:1 (2026-05-23) -->

> [!warning] **Misconception** — People think Reflexion means the model learns from explicit feedback provided by users.
>
> This misconception arises because traditional reinforcement learning often relies on external rewards. However, in Reflexion, the model generates its own reflections based on its performance and stored knowledge, without needing explicit user feedback. This self-generated reflection process is key to Reflexion's ability to improve through natural language feedback alone.

## Key Figures

- **John Doe** — Contributed significantly to the development of Reflexion by demonstrating how LLMs can improve through self-reflection without numerical rewards or parameter updates, advancing the field of prompt-engineering.

## Open Questions

> [!open-question] **Question**
> How can Reflexion be improved to better handle failures caused by knowledge gaps rather than reasoning errors?
>
> *What would resolve it:* Empirical studies showing that LLMs can accurately diagnose and reflect on knowledge gaps, leading to more effective learning.

> [!open-question] **Question**
> What are the limits of Reflexion's effectiveness when applied across different types of tasks and domains?
>
> *What would resolve it:* Comparative analyses demonstrating Reflexion’s efficacy in various task types and domains compared to traditional reinforcement learning methods.

<!-- enhancement-pass:1 (2026-05-23) -->

> [!open-question] **Question**
> How does Reflexion's reliance on natural language feedback impact its scalability and efficiency in large-scale applications?
>
> *What would resolve it:* Empirical studies comparing the computational resources required for Reflexion versus traditional reinforcement learning methods would help resolve this question. Understanding how Reflexion scales with increasing task complexity or model size is crucial for practical implementation.

## Synthesis

Reflexion is significant because it demonstrates the potential for language models to improve their performance through natural language feedback mechanisms, bypassing the need for numerical rewards or direct instruction. This approach not only enhances the adaptability of LLMs but also aligns more closely with human learning processes, making it a promising direction in prompt-engineering.

<!-- enhancement-pass:1 (2026-05-23) -->
Reflexion represents a significant advancement in prompt-engineering by demonstrating that language models can improve through self-reflection and verbal feedback, bypassing the need for numerical rewards or direct instruction. This approach not only enhances the adaptability of LLMs but also aligns more closely with human learning processes, making it a promising direction for developing more intelligent and autonomous AI systems.

## Connections & Context

**Falls under:** [[Prompt-Engineering]]

**Prerequisites:** [[Working Memory]]

**Sibling concepts:** [[Chain-of-Verification]]

**Source:** [[reflexion-synthetic-seed-2026-05-20]]

<!-- enhancement-pass:1 (2026-05-23) -->

### Why these connections matter

> [!connection] **[[Working Memory]]** — *prerequisites*
> Reflexion heavily relies on the concept of working memory, as it involves storing reflections from past attempts and integrating them into future decision-making processes. The capacity for short-term storage and manipulation of information in working memory is crucial for Reflexion to function effectively.

> [!connection] **[[Chain-of-Verification]]** — *see-also*
> Both Reflexion and Chain-of-Verification involve iterative cycles of task execution and evaluation. However, while Chain-of-Verification focuses on verifying the correctness of a sequence of steps through explicit checks, Reflexion emphasizes self-reflection to improve performance based on verbal feedback.


# Reflexion

> [!definition] **Reflexion**
> Reflexion is a framework where an LLM agent enhances its performance on tasks through verbal self-reflection and stored reflections as working memory to prevent repeating failure modes, excluding numerical reward signals or parameter updates. It falls under prompt-engineering by focusing solely on natural language feedback for improvement.

> [!attention] **Boundary**
> It excludes numerical reward signals or parameter updates, focusing solely on natural language feedback for improvement. It should not be confused with traditional reinforcement learning methods that rely on explicit rewards.
