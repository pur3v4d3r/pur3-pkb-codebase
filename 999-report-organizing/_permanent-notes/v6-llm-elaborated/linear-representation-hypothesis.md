---
title: "Linear Representation Hypothesis"
aliases:
  - "Linear Representation Hypothesis"
  - "linear geometry of concepts"
  - "linear embedding of features"
  - "linear representation theory in LLMs"
type: permanent-note
status: enriched
confidence: high

tags:
  - permanent-note
  - v6-llm-elaborated
  - mechanistic-interpretability

domain: mechanistic-interpretability
subdomains:
  - large-language-models
  - mechanistic-interpretability
  - representation-learning
  - geometry-of-representations

created: 2026-05-22
updated: 2026-05-22

source-type: report-extraction
source-reports:
  - "linear-representation-hypothesis-synthetic-seed-2026-05-22"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)"

complexity-level: advanced-practitioner
depth-level: elaborated

parent-concept: "Mechanistic Interpretability"

related:
  - "[[Probing Classifiers]]"
  - "[[Representation Engineering]]"
  - "[[Concept Activation Vectors]]"
prerequisites:
  - "[[]]"
specializes:
  - "[[]]"
broader:
  - "[[]]"
see-also:
  - "[[]]"
contrasts-with:
  - "[[]]"
contradicts:
  - "[[]]"
applies-to:
  - "[[Probing Classifiers]]"
  - "[[Representation Engineering]]"
formalizes:
  - "[[]]"
instance-of:
  - "[[]]"
supports:
  - "[[Concept Activation Vectors]]"
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

# Linear Representation Hypothesis

> [!definition] **Linear Representation Hypothesis**
> The Linear Representation Hypothesis posits that large language models encode concepts as linear directions within high-dimensional activation spaces, allowing for predictable behavior changes through interventions on these directions. This approximation does not capture all complexities such as polysemanticity and non-linear interactions between concept representations, highlighting its limitations in fully explaining model mechanics. It falls under the broader domain of Mechanistic Interpretability.

> [!attention] **Boundary**
> This hypothesis is an approximation rather than a precise mechanistic claim; it does not account for all complexities such as polysemanticity, superposition, context-dependence, and non-linear interactions between concept representations.

## Core Explanation

The Linear Representation Hypothesis suggests that concepts within large language models are represented as linear directions in high-dimensional spaces. This means that a specific concept, such as 'is a mammal' or 'positive sentiment,' corresponds to a consistent direction in the model's activation space. The hypothesis is grounded in empirical evidence from probing classifiers and representation engineering experiments, which consistently find that binary properties can be reliably identified by training linear probes on these directions.

The theoretical roots of this hypothesis are found in word2vec-style vector arithmetic, where operations like 'king - man + woman ≈ queen' demonstrate the linearity of concept representations. This approach extends to transformer hidden states, indicating a broader applicability across different types of language models. The core idea is that these linear directions can be manipulated to predictably alter model behavior.

In practice, interventions on these linear directions modify model behavior in predictable ways. For instance, adding or subtracting the direction associated with 'positive sentiment' from activation vectors can change the model's output regarding sentiment analysis tasks. This empirical evidence supports the hypothesis as a useful approximation for understanding how language models represent and process information.

However, it is important to note that while linear representations are effective in many cases, they do not capture all complexities of concept representation within these models. Limitations such as polysemanticity (where multiple concepts share directions), superposition (more concepts than dimensions encoded non-orthogonally), and context-dependence (the same concept encoded differently in different contexts) highlight the need for a more nuanced understanding beyond simple linear approximations.

## Practical Implications

> [!example] **Application 1 — Activation Steering**
> The Linear Representation Hypothesis enables activation steering, where model behavior is controlled by manipulating concept directions in the activation space. For example, to enhance a language model's ability to recognize positive sentiment, one could add the direction associated with 'positive sentiment' to the input activations. This intervention would predictably increase the likelihood of positive sentiment being recognized.

> [!example] **Application 2 — Concept Manipulation**
> Understanding that concepts are represented as linear directions allows for targeted manipulation of model behavior in specific scenarios. For instance, if a language model tends to misinterpret certain grammatical structures, one could identify and adjust the direction associated with those structures to improve accuracy.

## Key Distinctions

> [!key-distinction] **Linear vs Non-Linear Interactions**
> While the Linear Representation Hypothesis posits that concepts are represented as linear directions in high-dimensional spaces, it does not fully capture non-linear interactions between these directions. This distinction is crucial because while linear approximations can be useful for many applications, they may fail to explain complex linguistic phenomena where non-linear relationships play a significant role.

## Open Questions

> [!open-question] **Question**
> How consistent is linearity across different contexts and models?
>
> *What would resolve it:* Empirical studies comparing the consistency of linear representations in various contexts and across different language models would help resolve this question.

> [!open-question] **Question**
> What are the limitations of linear representations in capturing complex linguistic phenomena?
>
> *What would resolve it:* Further research into non-linear interactions between concept directions could provide insights into these limitations.

## Synthesis

The Linear Representation Hypothesis is a critical tool for understanding and manipulating large language models. By approximating concepts as linear directions, it provides a practical framework for controlling model behavior through activation steering and probing classifiers. However, recognizing its limitations in capturing complex linguistic phenomena underscores the need for continued research into more nuanced representations.

## Connections & Context

**Falls under:** [[Mechanistic Interpretability]]

**Applies to:** [[Probing Classifiers]] · [[Representation Engineering]]

**Supports:** [[Concept Activation Vectors]]

**Source:** [[linear-representation-hypothesis-synthetic-seed-2026-05-22]]
