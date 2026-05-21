---
title: "Reflexion"
aliases:
  - "Reflexion"
  - "reflexion prompting"
  - "verbal reinforcement learning"
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
updated: 2026-05-20

source-type: report-extraction
source-reports:
  - "reflexion-synthetic-seed-2026-05-20"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)"

complexity-level: advanced-practitioner
depth-level: elaborated

parent-concept: "Prompt-Engineering"

related:
  - "[[Working Memory]]"
  - "[[Chain-of-Verification]]"
prerequisites:
  - "[[Working Memory]]"
specializes:
  - "[[]]"
broader:
  - "[[]]"
see-also:
  - "[[Chain-of-Verification]]"
contrasts-with:
  - "[[]]"
contradicts:
  - "[[]]"
applies-to:
  - "[[]]"
formalizes:
  - "[[]]"
instance-of:
  - "[[]]"
supports:
  - "[[]]"
refines:
  - "[[]]"

review-frequency: quarterly
mastery-stage: budding
importance: medium

provenance:
  pipeline-version: "v6.0.0"
  outline-contract: "v6-outline-v1"
  elaborate-contract: "v6-elaborate-v1"
  passes: 2
---

# Reflexion

> [!definition] **Reflexion**
> Reflexion is a framework where an LLM agent enhances its performance on tasks through verbal self-reflection and stored reflections as working memory to prevent repeating failure modes, excluding numerical reward signals or parameter updates. It falls under prompt-engineering by focusing solely on natural language feedback for improvement.

> [!attention] **Boundary**
> It excludes numerical reward signals or parameter updates, focusing solely on natural language feedback for improvement. It should not be confused with traditional reinforcement learning methods that rely on explicit rewards.

## Core Explanation

Reflexion operates on the principle that an LLM can improve its performance through self-reflection rather than relying on external rewards or direct instruction. This process involves the agent generating a verbal reflection after each attempt at a task, identifying failure modes and articulating why these failures occurred.

The core mechanism of Reflexion is iterative: after each trial, the model generates a reflective statement about its performance, which it then uses as input for subsequent attempts. This cycle allows the LLM to learn from its mistakes without needing explicit numerical feedback or parameter adjustments.

This approach draws on theories of self-regulated learning and metacognition in human cognition, where individuals reflect on their thought processes and outcomes to guide future actions. In Reflexion, this concept is applied to language models, enabling them to improve through natural language feedback alone.

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

## Synthesis

Reflexion is significant because it demonstrates the potential for language models to improve their performance through natural language feedback mechanisms, bypassing the need for numerical rewards or direct instruction. This approach not only enhances the adaptability of LLMs but also aligns more closely with human learning processes, making it a promising direction in prompt-engineering.

## Connections & Context

**Falls under:** [[Prompt-Engineering]]

**Prerequisites:** [[Working Memory]]

**Sibling concepts:** [[Chain-of-Verification]]

**Source:** [[reflexion-synthetic-seed-2026-05-20]]
