---
title: "Chain-of-Thought Emergence"
aliases:
  - "Chain-of-Thought Emergence"
  - "CoT capability emergence"
  - "chain-of-thought threshold"
  - "reasoning chain emergence"
type: permanent-note
status: enriched
confidence: high

tags:
  - permanent-note
  - v6-llm-elaborated
  - prompt-engineering

domain: prompt-engineering
subdomains:
  - prompt-engineering
  - reasoning
  - large-language-models

created: 2026-05-22
updated: 2026-05-22

source-type: report-extraction
source-reports:
  - "chain-of-thought-emergence-synthetic-seed-2026-05-22"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)"

complexity-level: advanced-practitioner
depth-level: elaborated

parent-concept: "Prompt Engineering"

related:
  - "[[Prompt Engineering]]"
  - "[[Scaling Laws]]"
prerequisites:
  - "[[]]"
specializes:
  - "[[Prompt Engineering]]"
broader:
  - "[[]]"
see-also:
  - "[[]]"
contrasts-with:
  - "[[]]"
contradicts:
  - "[[]]"
applies-to:
  - "[[Scaling Laws]]"
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

# Chain-of-Thought Emergence

> [!definition] **Chain-of-Thought Emergence**
> Chain-of-thought emergence is a phenomenon where providing step-by-step reasoning examples to large language models significantly improves performance only above a certain scale threshold, typically around 100 billion parameters in the original study by Wei et al., while smaller models may degrade or show no improvement. This concept falls under prompt engineering and highlights how specific prompting techniques can lead to emergent behaviors that are not simply due to scaling alone.

> [!attention] **Boundary**
> This concept is distinct from other emergent properties in large language models that do not involve prompting with chain-of-thoughts. It should not be confused with the general improvement of model capabilities solely due to scaling without specific prompting techniques.

## Core Explanation

Chain-of-thought emergence is a critical phenomenon in the field of large language model performance, where providing step-by-step reasoning examples leads to substantial improvements only for models above a certain scale threshold. This finding underscores the importance of task difficulty matching and the complexity of reasoning tasks that can be handled by different sized models. The empirical evidence suggests that smaller models often generate incoherent or incorrect reasoning chains when prompted with chain-of-thoughts, which can corrupt rather than improve their final answers.

The core mechanism behind this phenomenon lies in how larger models are capable of generating coherent and logically consistent reasoning chains, whereas smaller models struggle to maintain coherence. This is not merely a scale issue but also reflects the model's ability to handle complex logical structures required for multi-step reasoning tasks. The threshold at which chain-of-thought prompting becomes beneficial varies depending on the specific task complexity and the model’s capacity.

The theoretical underpinnings of this phenomenon are rooted in cognitive science, particularly in how humans process information through step-by-step reasoning. Large language models mimic this human-like reasoning when they can generate coherent chains of thought, leading to improved performance on tasks that require logical deduction or multi-step problem-solving.

## Mechanism

Smaller models tend to produce fragmented and incoherent reasoning chains due to their limited capacity for handling complex logical structures. As the model size increases, it gains the ability to generate coherent reasoning sequences that lead to correct conclusions. This transition from incoherence to coherence is a critical aspect of chain-of-thought emergence.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design for large language models, understanding the threshold at which chain-of-thought prompting becomes beneficial can guide the creation of more effective prompts. For tasks that require multi-step reasoning, designing prompts that match the model's capacity ensures coherent and accurate responses. Ignoring this principle may result in degraded performance or incorrect outputs.

> [!example] **Application 2 — Task difficulty matching**
> Matching task complexity to the model’s capability level is crucial for leveraging chain-of-thought prompting effectively. For tasks that are too complex, even large models might struggle with coherent reasoning chains, while overly simple tasks may not benefit from such prompts. Properly aligning task difficulty ensures optimal performance and avoids unnecessary degradation.

## Key Distinctions

> [!key-distinction] **Chain-of-thought emergence vs general scaling benefits**
> While chain-of-thought emergence specifically refers to the improvement in reasoning capabilities due to prompting with coherent chains of thought, general scaling benefits are broader improvements seen across various tasks as model size increases. Chain-of-thought emergence is a more nuanced phenomenon that highlights specific emergent behaviors tied to task complexity and model capacity.

## Key Figures

- **Wei et al.** — Their study first identified the threshold at which chain-of-thought prompting becomes beneficial, highlighting the importance of scale in generating coherent reasoning chains. Their work laid foundational insights into how model size impacts reasoning capabilities.

## Open Questions

> [!open-question] **Question**
> What are the exact thresholds for different tasks and how do they vary?
>
> *What would resolve it:* Detailed empirical studies across a range of tasks would provide specific thresholds, helping to tailor prompts more effectively based on model size and task complexity.

## Synthesis

Understanding chain-of-thought emergence is crucial for optimizing large language models in complex reasoning tasks. It bridges the gap between theoretical cognitive processes and practical applications in AI, offering insights into how models can be prompted to generate coherent logical sequences that lead to accurate conclusions.

## Connections & Context

**Falls under:** [[Prompt Engineering]]

**Specializes:** [[Prompt Engineering]]

**Applies to:** [[Scaling Laws]]

**Source:** [[chain-of-thought-emergence-synthetic-seed-2026-05-22]]
