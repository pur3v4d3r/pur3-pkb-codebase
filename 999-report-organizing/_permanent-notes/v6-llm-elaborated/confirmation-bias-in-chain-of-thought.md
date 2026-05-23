---
title: "Confirmation Bias in Chain of Thought"
aliases:
  - "Confirmation Bias in Chain of Thought"
  - "motivated reasoning in CoT"
  - "biased chain-of-thought"
  - "selective evidence weighting in LLMs"
type: permanent-note
status: enriched
confidence: high

tags:
  - permanent-note
  - v6-llm-elaborated
  - cognitive-psychology

domain: cognitive-psychology
subdomains:
  - large-language-models
  - cognitive-psychology
  - chain-of-thought-prompting
  - ai-safety

created: 2026-05-22
updated: 2026-05-22

source-type: report-extraction
source-reports:
  - "confirmation-bias-in-chain-of-thought-synthetic-seed-2026-05-22"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)"

complexity-level: advanced-practitioner
depth-level: elaborated

parent-concept: "Cognitive Bias"

related:
  - "[[Confirmation Bias]]"
  - "[[Chain-of-Thought Prompting]]"
prerequisites:
  - "[[]]"
specializes:
  - "[[Confirmation Bias]]"
broader:
  - "[[]]"
see-also:
  - "[[]]"
contrasts-with:
  - "[[]]"
contradicts:
  - "[[]]"
applies-to:
  - "[[Chain-of-Thought Prompting]]"
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

# Confirmation Bias in Chain of Thought

> [!definition] **Confirmation Bias in Chain of Thought**
> Confirmation Bias in Chain of Thought refers to a specific tendency within large language models (LLMs) where reasoning chains are constructed to favor evidence that supports initial claims while underweighting or ignoring contrary evidence. This phenomenon is distinct from general confirmation bias as it specifically pertains to the explicit reasoning process within LLMs, not broader human cognitive biases. It falls under the broader category of Cognitive Bias.

> [!attention] **Boundary**
> This concept is distinct from general confirmation bias as it specifically focuses on the chain-of-thought process within LLMs and does not encompass other forms of cognitive biases in human reasoning.

## Core Explanation

Confirmation Bias in Chain of Thought manifests when large language models generate reasoning chains that appear logically sound but are inherently biased due to their initial premises. This bias occurs because subsequent steps in the chain tend to favor information consistent with the first claim, even if contradictory evidence is available. The model's reasoning process thus becomes a confirmation exercise rather than an exploration of all relevant data.

The foundational mechanism behind this phenomenon involves how LLMs interpret and generate responses based on initial prompts or intermediate steps within their reasoning chains. When a prompt sets a direction for the chain, the model tends to reinforce that direction through subsequent steps, even if it leads to incorrect conclusions. This behavior is exacerbated by reinforcement learning from human feedback (RLHF) processes which reward coherent and consistent outputs over epistemically correct revisions.

Theoretical roots of this bias lie in how LLMs process information and generate responses based on statistical patterns learned during training. Models are trained to produce text that aligns with human preferences, often prioritizing consistency over accuracy. This creates a systematic pressure towards confirmatory reasoning, as models learn to favor outputs that maintain internal coherence rather than challenge initial assumptions.

Empirical evidence supports the notion that confirmation bias in chain-of-thought reasoning is prevalent across various LLM applications. Studies have shown that when prompted with an initial claim, subsequent steps in the model's reasoning are more likely to support this claim, even if contradictory evidence exists. This pattern persists regardless of whether the initial claim is factually correct or not.

## Mechanism

The mechanism by which confirmation bias operates within chain-of-thought reasoning involves several stages: first, an initial premise or claim is established either through a prompt or as part of the model's own intermediate steps. Second, subsequent reasoning steps are generated that selectively surface evidence and arguments supporting this initial direction. Finally, the entire reasoning chain appears logically consistent but is structurally biased towards confirmatory conclusions.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design for LLMs, confirmation bias in chain-of-thought reasoning can lead to flawed educational content if not addressed. For instance, a model tasked with explaining scientific concepts might generate explanations that favor initial assumptions over contradictory evidence, potentially misleading learners about the true nature of these concepts.

> [!example] **Application 2 — Legal argumentation**
> In legal contexts where LLMs are used to construct arguments or analyze cases, confirmation bias can result in one-sided reasoning. If a model is prompted with an initial claim that aligns with a particular legal stance, it may generate supporting evidence while underweighting opposing viewpoints, leading to biased and potentially unethical legal advice.

## Key Distinctions

> [!key-distinction] **Confirmation Bias in Chain of Thought vs General Confirmation Bias**
> While general confirmation bias refers to the tendency to seek out information that supports one's preconceptions across various cognitive processes, Confirmation Bias in Chain of Thought is specific to the reasoning chains generated by LLMs. This distinction highlights how technological systems can exhibit biases distinct from human cognition.

## Key Figures

- **John Sweller** — Contributed foundational work on cognitive load theory, which provides theoretical underpinnings for understanding how LLMs process and generate information in ways that can lead to confirmation bias in chain-of-thought reasoning.

## Open Questions

> [!open-question] **Question**
> How can we design prompts to mitigate confirmation bias in chain-of-thought reasoning?
>
> *What would resolve it:* Experimental studies comparing the effectiveness of different prompt designs on reducing confirmatory biases would provide insights into best practices for instructional and practical applications.

## Synthesis

Recognizing Confirmation Bias in Chain of Thought is crucial as it underscores the importance of critical thinking even when using advanced AI tools. By understanding how LLMs can generate seemingly logical but biased reasoning chains, users can better evaluate outputs for accuracy and fairness, ensuring that technology serves to enhance rather than distort human decision-making processes.

## Connections & Context

**Falls under:** [[Cognitive Bias]]

**Specializes:** [[Confirmation Bias]]

**Applies to:** [[Chain-of-Thought Prompting]]

**Source:** [[confirmation-bias-in-chain-of-thought-synthetic-seed-2026-05-22]]
