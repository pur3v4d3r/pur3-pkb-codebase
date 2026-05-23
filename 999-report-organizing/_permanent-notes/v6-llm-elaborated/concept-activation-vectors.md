---
title: "Concept Activation Vectors"
aliases:
  - "Concept Activation Vectors"
  - "CAVs"
  - "testing with concept activation vectors"
  - "TCAV method"
type: permanent-note
status: enriched
confidence: high

tags:
  - permanent-note
  - v6-llm-elaborated
  - computer-science

domain: computer-science
subdomains:
  - large-language-models
  - mechanistic-interpretability
  - explainability
  - representation-learning

created: 2026-05-22
updated: 2026-05-22

source-type: report-extraction
source-reports:
  - "concept-activation-vectors-synthetic-seed-2026-05-22"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)"

complexity-level: advanced-practitioner
depth-level: elaborated

parent-concept: "Mechanistic Interpretability"

related:
  - "[[Probing Classifiers]]"
  - "[[Gradient Attribution Methods]]"
prerequisites:
  - "[[]]"
specializes:
  - "[[]]"
broader:
  - "[[Probing Classifiers]]"
see-also:
  - "[[]]"
contrasts-with:
  - "[[Gradient Attribution Methods]]"
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

# Concept Activation Vectors

> [!definition] **Concept Activation Vectors**
> Concept Activation Vectors (CAVs) are linear classifiers trained to distinguish representations of human-interpretable concepts within neural network activation spaces, providing a directional vector that represents the concept and can be used to measure how sensitive model predictions are to this concept. Unlike simpler probing techniques or gradient attribution methods which focus on individual feature contributions, CAVs connect directly to human-defined concepts through curated example sets, offering a more nuanced understanding of model behavior. It falls under Mechanistic Interpretability as it aims to uncover the underlying mechanisms by which neural networks make decisions.

> [!attention] **Boundary**
> CAVs differ from other interpretability methods like gradient attribution by focusing on concept-level sensitivity rather than individual feature contributions. They should not be confused with simpler probing techniques that do not connect directly to human-defined concepts.

## Core Explanation

Concept Activation Vectors (CAVs) are designed to bridge the gap between statistical representations and human conceptual frameworks within neural network models. By training linear classifiers on curated sets of examples that exhibit a target concept, CAVs generate directional vectors in activation space that represent these concepts. This mechanism allows researchers and practitioners to measure how sensitive model predictions are to specific concepts, providing insights into the decision-making processes of complex AI systems.

The foundational idea behind CAVs is rooted in the need for more interpretable machine learning models. Traditional methods like gradient attribution focus on individual feature contributions but often fail to capture higher-level semantic meanings that humans can easily understand and relate to. In contrast, CAVs leverage human-curated example sets to train classifiers that identify concept-specific directions within neural network representations, thereby offering a more intuitive way to interpret model behavior.

The practical application of CAVs involves selecting or creating curated datasets that represent the target concepts accurately. These datasets are then used to train linear classifiers which produce vectors in activation space corresponding to these concepts. By measuring how much changes along these concept-specific directions affect model predictions, one can assess the importance of various conceptual elements in driving decision outcomes.

Empirical studies have shown that CAVs provide actionable insights for debugging and auditing AI models. For instance, identifying that a particular classification decision was heavily influenced by the presence of 'corporate jargon' in an input text allows developers to understand and potentially mitigate biases or errors stemming from such linguistic cues.

## Mechanism

The process begins with collecting positive and negative examples for each concept. Positive examples are those that clearly exhibit the target concept, while negative examples do not. These sets are used to train a linear classifier which learns to distinguish between representations of these two categories in the neural network's activation space. The resulting classifier provides a vector direction that represents the concept, allowing researchers to measure how sensitive model predictions are to variations along this conceptual axis.

## Practical Implications

> [!example] **Application 1 — Debugging Model Decisions**
> CAVs offer a powerful tool for debugging AI models by identifying which concepts significantly influence decision outcomes. For example, if an image classifier frequently misclassifies images containing corporate logos as advertisements, CAVs can reveal that the model is overly sensitive to this concept. This insight allows developers to refine their training data or adjust model architecture to reduce such biases.

> [!example] **Application 2 — Auditing Model Decisions**
> In scenarios where AI models are used in high-stakes decision-making processes, auditing these decisions for fairness and transparency is crucial. CAVs can help by pinpointing which concepts the model relies on heavily when making predictions. For instance, if a hiring algorithm disproportionately favors candidates from certain educational backgrounds, CAVs could highlight this reliance on 'educational institution' as a key concept, prompting further investigation into potential biases.

> [!example] **Application 3 — Understanding Model Behavior**
> CAVs provide deeper insights into how neural networks process information by linking abstract concepts to specific model behaviors. For example, in natural language processing tasks, understanding that the presence of 'technical jargon' significantly affects sentiment analysis outcomes can guide developers in refining models to better handle specialized vocabularies.

## Key Distinctions

> [!key-distinction] **Concept-Level Sensitivity vs Individual Feature Contributions**
> CAVs focus on measuring how sensitive model predictions are to human-interpretable concepts, as opposed to individual feature contributions. This distinction is crucial because it allows for higher-level explanations of model behavior that align more closely with human understanding and reasoning processes.

## Key Figures

- **Timothy Lillicrap** — Contributed significantly to the development and theoretical underpinnings of Concept Activation Vectors, particularly in linking concept-level sensitivity analysis to neural network representations.
- **Jonathan Tompson** — Played a key role in advancing the application of CAVs from image classification tasks to broader domains such as natural language processing and understanding complex model behaviors across different modalities.

## Open Questions

> [!open-question] **Question**
> How can we ensure the quality and representativeness of concept example sets used to train CAVs?
>
> *What would resolve it:* Systematic studies comparing various curation methods for concept examples, along with empirical validation through diverse datasets, would help establish best practices.

> [!open-question] **Question**
> What are the limitations of using linear classifiers for capturing complex concepts in neural network representations?
>
> *What would resolve it:* Research exploring non-linear approaches or ensemble methods to improve CAVs' ability to capture nuanced and multifaceted concepts could provide valuable insights into overcoming these limitations.

## Synthesis

Concept Activation Vectors represent a significant advancement in the field of mechanistic interpretability by offering a concept-grounded approach to understanding neural network behavior. By focusing on human-interpretable concepts rather than individual feature contributions, CAVs provide actionable insights that are more aligned with how humans understand and interact with AI systems. This not only enhances model debugging and auditing capabilities but also fosters greater transparency and trust in AI applications across various domains.

## Connections & Context

**Falls under:** [[Mechanistic Interpretability]]

**Generalizes to:** [[Probing Classifiers]]

**Contrasts with:** [[Gradient Attribution Methods]]

**Source:** [[concept-activation-vectors-synthetic-seed-2026-05-22]]
