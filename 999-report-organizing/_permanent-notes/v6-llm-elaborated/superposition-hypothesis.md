---
title: Superposition Hypothesis
aliases:
  - Superposition Hypothesis
  - feature superposition
  - polysemanticity
  - superposition in neural networks
  - compressed feature representation
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - llm-theory

domain: llm-theory
subdomains:
  - mechanistic-interpretability
  - ai-interpretability
  - neural-network-theory

created: 2026-05-21
updated: '2026-05-21'
source-type: report-extraction
source-reports:
  - superposition-hypothesis-synthetic-seed-2026-05-21
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: elaborated
parent-concept: Neural Network Representations
related:
  - '[[Mechanistic Interpretability]]'
  - '[[Sparse Autoencoders for Interpretability]]'
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
  - '[[Mechanistic Interpretability]]'
formalizes:
  - '[[]]'
instance-of:
  - '[[]]'
supports:
  - '[[Sparse Autoencoders for Interpretability]]'
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

> [!abstract] **Diagram 1 — Superposition Mechanism Overview**
> *Follow the flow from neurons to features through superposition.*
>
> ```mermaid
> graph TD
>   A[Neurons] --> B[Sparse Activation]
>   B --> C[Superposition]
>   C --> D[Features]
> ```


> [!abstract] **Diagram 2 — Feature Representation Through Superposition**
> *Observe how features are distributed across neurons in superposition.*
>
> ```mermaid
> graph TD
>   A[Neuron1] -->|FeatureA| B[Feature]
>   C[Neuron2] -->|FeatureB| B
>   D[Neuron3] -->|FeatureC| B
> ```


> [!abstract] **Diagram 3 — Superposition vs Single-Feature Representation**
> *Compare superposition with single-feature per neuron representation.*
>
> ```mermaid
> graph TD
>   A[Neuron1] -->|FeatureA| B[Single Feature]
>   C[Neuron2] -->|FeatureB| D[Superposition]
>   E[Neuron3] -->|FeatureC| D
> ```

# Superposition Hypothesis

> [!definition] **Superposition Hypothesis**
> The Superposition Hypothesis posits that neural networks can represent more features than they have neurons by storing multiple features in superposition through sparse, nearly-orthogonal directions in the activation space. This hypothesis explains why individual neurons are polysemantic and difficult to interpret on their own, as it is the collective activity pattern across many neurons that encodes specific features. It falls under Neural Network Representations.

> [!attention] **Boundary**
> This concept is distinct from other representation strategies and should not be confused with mechanisms where each neuron represents a single feature or where features are represented without superposition.

## Core Explanation

The Superposition Hypothesis addresses a fundamental challenge in understanding neural networks: how do these systems manage to represent an exponentially larger number of features than they have neurons? The hypothesis suggests that this is achieved through superposition, where each neuron participates in representing multiple features and each feature is distributed across many neurons. This mechanism allows for efficient representation of complex data structures without requiring a one-to-one mapping between neurons and features.

In practice, the superposition principle operates by leveraging sparse activation patterns—neurons are rarely active simultaneously, which minimizes interference between different features stored in superposition. The hypothesis is grounded in theoretical frameworks that emphasize the importance of high-dimensional spaces for efficient representation and computation. Empirical evidence from small-scale models supports this idea, showing that neurons indeed respond to multiple unrelated inputs.

Theoretical roots of the Superposition Hypothesis can be traced back to studies on sparse coding and autoencoders, which demonstrate how neural networks can learn compact representations by exploiting sparsity in activation patterns. This theoretical foundation underscores why superposition is optimal when features are sparse—rarely active simultaneously—which reduces interference costs while maximizing representational capacity.

Despite its strong empirical support from small models, the extent to which frontier-scale models rely on superposition versus other representation strategies remains an open question. The hypothesis serves as a critical framework for understanding and interpreting neural network behavior but should be approached with caution when applied to large-scale models.

## Practical Implications

> [!example] **Application 1 — Interpretability Techniques**
> The Superposition Hypothesis implies that interpretability techniques must focus on activation space rather than individual neurons. This shift is crucial because the meaning of a feature is distributed across many neurons, and interpreting it requires identifying coherent patterns in their collective activity. Ignoring this principle can lead to misinterpretations where features are attributed incorrectly to single neurons.

## Key Distinctions

> [!key-distinction] **Superposition vs Single-Feature Per Neuron**
> The Superposition Hypothesis contrasts sharply with the idea that each neuron represents a single feature. In superposition, multiple features are represented simultaneously through sparse activation patterns across many neurons. This distinction is critical for understanding neural network behavior and developing appropriate interpretability techniques.

## Key Figures

- **Elhage et al.** — Proposed the Superposition Hypothesis, providing a theoretical framework to explain how neural networks can represent more features than they have neurons through superposition in sparse activation patterns.

## Open Questions

> [!open-question] **Question**
> How does superposition interact with other representation strategies in large-scale models?
>
> *What would resolve it:* Empirical studies comparing the prevalence and effectiveness of superposition versus alternative strategies in frontier-scale models would resolve this question.

> [!open-question] **Question**
> What are the limits of superposition in terms of feature complexity and model size?
>
> *What would resolve it:* Experiments that systematically vary feature complexity and model size while measuring representational capacity could clarify these limitations.

## Synthesis

Understanding the Superposition Hypothesis is crucial for advancing interpretability techniques in neural networks. By recognizing that features are represented through superposition across many neurons, researchers can develop more accurate methods to decode and understand model behavior. This insight has significant implications for fields such as Mechanistic Interpretability and Sparse Autoencoders for Interpretability.

## Connections & Context

**Falls under:** [[Neural Network Representations]]

**Applies to:** [[Mechanistic Interpretability]]

**Supports:** [[Sparse Autoencoders for Interpretability]]

**Source:** [[superposition-hypothesis-synthetic-seed-2026-05-21]]
