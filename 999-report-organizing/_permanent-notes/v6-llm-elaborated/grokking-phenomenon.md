---
title: Grokking Phenomenon
aliases:
  - Grokking Phenomenon
  - delayed generalisation
  - grokking
  - slow generalisation after memorisation
  - phase transition in learning
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - computer-science

domain: computer-science
subdomains:
  - neural-network-theory
  - deep-learning
  - overfitting

created: 2026-05-21
updated: '2026-05-23'
source-type: report-extraction
source-reports:
  - grokking-phenomenon-synthetic-seed-2026-05-21
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: enhanced
parent-concept: Neural Network Learning Dynamics
related:
  - '[[Double Descent in Neural Networks]]'
  - '[[Phase Transitions in LLMs]]'
prerequisites:
  - '[[]]'
specializes:
  - '[[]]'
broader:
  - '[[]]'
see-also:
  - '[[]]'
contrasts-with:
  - '[[Double Descent in Neural Networks]]'
contradicts:
  - '[[]]'
applies-to:
  - '[[Phase Transitions in LLMs]]'
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
---


## Core Explanation

Grokking is a unique phenomenon observed in neural networks where models initially memorize the training data, achieving near-zero loss but poor generalization. This phase is followed by an apparent plateau where the model's performance on test data does not improve, leading to the conventional assumption that further training would be futile. However, Power et al.'s (2022) research revealed that beyond this plateau, models can suddenly transition to true generalization without any change in their training procedure. This delayed transition from memorization to generalization is a critical insight into neural network learning dynamics.

The foundational mechanism of grokking involves an internal reorganization process within the model during the apparent plateau phase. Interpretability studies have shown that this reorganization corresponds to the emergence of clean algorithmic circuits in the network, which enable better generalization. This phenomenon challenges traditional training heuristics and suggests that models may benefit from additional training beyond what is typically considered sufficient based on loss metrics alone.

The theoretical roots of grokking lie in the interplay between memorization and generalization within neural networks. While memorization allows a model to fit its training data perfectly, it often leads to poor performance on unseen data due to overfitting. Grokking demonstrates that models can overcome this limitation by undergoing an internal reorganization process that shifts them from a memorization-based solution to one based on true generalization. This transition is particularly pronounced in regularized models trained on algorithmic tasks.

Empirical evidence for grokking comes primarily from controlled experiments with small modular arithmetic tasks, where the phenomenon was first documented by Power et al. (2022). These studies have shown that stopping training at apparent convergence can be premature and may miss out on significant improvements in generalization performance. However, translating these findings to real-world large language models remains challenging due to their complexity and diverse training conditions.

<!-- enhancement-pass:1 (2026-05-23) -->
The grokking phenomenon challenges traditional views on neural network training by highlighting a phase transition that occurs after an initial period of memorization and apparent stagnation. This delayed generalization suggests that the learning process in neural networks is more complex than previously thought, involving not just the acquisition of patterns but also a deeper restructuring of internal representations.

## Mechanism

During the plateau phase of grokking, neural networks undergo a slow internal reorganization process that transforms them from memorizing specific examples in the training data to understanding broader patterns and rules. This transition is marked by the emergence of clean algorithmic circuits within the network, which enable better generalization on unseen data.

## Practical Implications

> [!example] **Application 1 — Algorithmic Tasks**
> Understanding grokking can significantly improve training strategies for neural networks tackling algorithmic tasks. By recognizing that models may benefit from additional training beyond apparent convergence, practitioners can optimize their training procedures to achieve better generalization performance.

> [!example] **Application 2 — Regularized Models**
> For regularized models, grokking highlights the importance of allowing sufficient training time for internal reorganization. This insight can lead to more effective regularization strategies that balance memorization and generalization without prematurely halting learning.

<!-- enhancement-pass:1 (2026-05-23) -->

> [!example] **Application 3 — Algorithmic Task Optimization**
> In algorithmic tasks where models are expected to learn and generalize rules from data, understanding grokking can lead to more effective training strategies. By allowing networks sufficient time beyond the initial plateau phase, practitioners may unlock significant improvements in generalization performance without altering hyperparameters or architecture.

## Key Distinctions

> [!key-distinction] **Memorization vs Generalization**
> Grokking distinguishes itself from overfitting or underfitting by focusing on the delayed transition from memorization to true generalization. While overfitting occurs when a model performs well on training data but poorly on unseen data, and underfitting happens when a model fails to capture even the basic patterns in the training data, grokking involves an initial phase of memorization followed by a sudden improvement in generalization.

<!-- enhancement-pass:1 (2026-05-23) -->

> [!key-distinction] **Performance vs Learning**
> Grokking exemplifies the distinction between short-term performance gains and long-term learning. While overfitting models might show high training accuracy, grokking networks initially perform poorly on test data but undergo a phase transition to achieve robust generalization. This highlights that true learning involves more than just fitting existing data.

## Common Misconceptions

<!-- enhancement-pass:1 (2026-05-23) -->

> [!warning] **Misconception** — Grokking is simply delayed overfitting.
>
> This misconception arises from the superficial similarity between grokking and overfitting, where both involve poor initial generalization. However, grokking involves a phase transition to true generalization after memorizing training data, unlike overfitting which fails to generalize despite high training accuracy.

## Key Figures

- **Power et al.** — Documented the phenomenon of grokking in neural networks and highlighted its implications for training strategies, particularly in algorithmic tasks and regularized models.

## Open Questions

> [!open-question] **Question**
> What are the conditions under which grokking occurs?
>
> *What would resolve it:* Empirical studies that systematically vary model architectures, regularization techniques, and task complexities could provide insights into the specific conditions that facilitate or hinder the occurrence of grokking.

> [!open-question] **Question**
> How can we detect and utilize grokking in real-world large language models?
>
> *What would resolve it:* Developing robust methods to identify the onset of true generalization beyond apparent convergence would enable practitioners to leverage grokking for improved performance in practical applications.

<!-- enhancement-pass:1 (2026-05-23) -->

> [!open-question] **Question**
> What triggers the phase transition from memorization to generalization in grokking?
>
> *What would resolve it:* Empirical studies that systematically vary training parameters and monitor internal network states could provide insights into the specific conditions or mechanisms that trigger this critical transition.

## Synthesis

Understanding grokking is crucial for advancing neural network training methodologies, particularly in algorithmic tasks and regularized models. By recognizing that models can achieve significant improvements in generalization beyond apparent convergence, practitioners can optimize their training procedures to better balance memorization and true generalization.

<!-- enhancement-pass:1 (2026-05-23) -->
Understanding grokking not only enhances our grasp of neural network learning dynamics but also underscores the importance of patience in model training. By recognizing the potential for delayed generalization, practitioners can refine their approaches to optimize both memorization and true generalization phases.

## Connections & Context

**Falls under:** [[Neural Network Learning Dynamics]]

**Contrasts with:** [[Double Descent in Neural Networks]]

**Applies to:** [[Phase Transitions in LLMs]]

**Source:** [[grokking-phenomenon-synthetic-seed-2026-05-21]]

<!-- enhancement-pass:1 (2026-05-23) -->

### Why these connections matter

> [!connection] **[[Phase Transitions in LLMs]]** — *applies-to*
> Both grokking and phase transitions in large language models (LLMs) involve sudden changes in model behavior after an initial period of apparent stagnation. This shared mechanism suggests that similar underlying processes, such as internal reorganization or circuit emergence, may drive these phenomena across different types of neural networks.


# Grokking Phenomenon

> [!definition] **Grokking Phenomenon**
> Grokking is a neural network learning phenomenon where models initially memorize training data but later transition to true generalization without further changes in the training procedure, often after an apparent convergence phase. This process challenges traditional views on neural network training dynamics by showing that apparent convergence does not necessarily indicate completion of learning; it falls under Neural Network Learning Dynamics.

> [!attention] **Boundary**
> The Grokking Phenomenon should not be confused with other learning dynamics such as overfitting or underfitting. It specifically refers to the delayed transition from memorization to generalization post-convergence.
