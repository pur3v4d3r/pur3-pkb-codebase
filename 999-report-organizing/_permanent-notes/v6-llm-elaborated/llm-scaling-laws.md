---
title: LLM Scaling Laws
aliases:
  - LLM Scaling Laws
  - neural scaling laws
  - Chinchilla scaling
  - Kaplan scaling laws
  - compute-optimal scaling
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - computer-science

domain: computer-science
subdomains:
  - machine-learning-theory
  - empirical-ml
  - neural-scaling

created: 2026-05-21
updated: '2026-05-23'
source-type: report-extraction
source-reports:
  - llm-scaling-laws-synthetic-seed-2026-05-21
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: enhanced
parent-concept: Neural Network Training
related:
  - '[[Emergent Abilities in LLMS]]'
  - '[[Parameter-Efficient Fine-Tuning]]'
prerequisites:
  - '[[]]'
specializes:
  - '[[]]'
broader:
  - '[[]]'
see-also:
  - '[[]]'
contrasts-with:
  - '[[Emergent Abilities in LLMS]]'
contradicts:
  - '[[]]'
applies-to:
  - '[[Parameter-Efficient Fine-Tuning]]'
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

LLM scaling laws emerged from a series of groundbreaking studies by Kaplan et al. (2020) and Hoffmann et al. (2022), which revealed systematic patterns in how model performance scales with increases in parameters, training tokens, and compute budget. Initially, the field observed that larger models generally outperformed smaller ones, leading to a focus on parameter scaling as the primary driver of improved performance.

However, Hoffmann et al.'s Chinchilla study introduced a critical shift by demonstrating that optimal model performance for a given compute budget is achieved not just through increasing parameters but also by ensuring adequate training data. The Chinchilla model (70B parameters, 1.4T tokens) outperformed the much larger Gopher model (280B parameters, 300B tokens), highlighting that equal scaling of model size and training tokens is crucial for compute-optimal performance.

This finding underscores a fundamental shift in how large language models are trained, emphasizing the importance of balanced scaling between model size and training data. The empirical nature of these laws means they are grounded in specific model architectures, tokenizers, data mixes, and training procedures, limiting their direct applicability to scenarios outside these parameters.

<!-- enhancement-pass:1 (2026-05-23) -->
The empirical nature of LLM scaling laws means that they are highly contingent on specific training conditions, such as data quality and diversity, model architecture, and the tokenizer used. These factors can significantly influence how performance scales with parameters and tokens, making it crucial for researchers to carefully control these variables in their experiments.

Recent advancements in hardware technology have also impacted the applicability of scaling laws. As compute resources become more powerful and cost-effective, the balance between model size and training data may shift, potentially altering the optimal ratios identified by early studies like Chinchilla's.

## Practical Implications

> [!example] **Application 1 — Resource Allocation**
> LLM scaling laws inform efficient resource allocation in large language models. By understanding the optimal ratios between model size and training data, practitioners can allocate compute budgets more effectively, ensuring that neither parameter nor token scarcity limits performance. Ignoring these principles could lead to undertrained or oversized models, both of which are inefficient.

> [!example] **Application 2 — Model Design**
> In designing large language models, scaling laws guide the balance between model complexity and training data volume. Models that adhere to these ratios tend to perform better within given compute constraints, making them more practical for deployment in real-world applications where resource efficiency is critical.

## Key Distinctions

> [!key-distinction] **Compute-Efficient vs Compute-Optimal Scaling**
> LLM scaling laws distinguish between compute-efficient and compute-optimal approaches. While compute-efficient training focuses on maximizing the use of available compute resources, compute-optimal strategies aim to achieve the best performance within a fixed budget by balancing model size with training data volume.

<!-- enhancement-pass:1 (2026-05-23) -->

> [!key-distinction] **Intrinsic vs Extraneous Load in Scaling Laws**
> The distinction between intrinsic and extraneous load is crucial for understanding LLM scaling laws. Intrinsic load refers to the inherent complexity of tasks that a model must perform, while extraneous load encompasses design-imposed difficulties such as inefficient training procedures or suboptimal resource allocation. By minimizing extraneous load through optimal scaling practices, researchers can better isolate intrinsic challenges and improve overall performance.

> [!key-distinction] **Performance vs Learning in Scaling Laws**
> LLM scaling laws often focus on immediate performance gains rather than long-term learning outcomes. However, understanding the distinction between these two concepts is vital for assessing the true impact of scaling strategies. While a model may achieve high performance within a given budget, sustained improvements over time require careful consideration of both intrinsic and extraneous factors that influence learning.

## Common Misconceptions

<!-- enhancement-pass:1 (2026-05-23) -->

> [!warning] **Misconception** — People often believe that simply increasing the number of parameters will always lead to better model performance.
>
> This misconception arises from an oversimplified view of LLM scaling laws. While larger models can sometimes outperform smaller ones, the relationship between parameter count and performance is not linear. Optimal performance requires a balanced approach where both model size and training data volume are scaled appropriately.

## Key Figures

- **Hoffmann et al.** — Chinchilla scaling law researchers who demonstrated that optimal performance for large language models requires balanced scaling of parameters and training tokens, challenging previous assumptions about the dominance of parameter scaling.
- **Kaplan et al.** — Pioneers in LLM scaling laws research who first established empirical power-law relationships between model scale and performance, laying foundational insights that were later refined by subsequent studies.

## Open Questions

> [!open-question] **Question**
> How do architectural innovations affect the validity of scaling laws?
>
> *What would resolve it:* Experimental validation on a range of architectures would determine if scaling laws remain consistent or require adjustment with new model designs.

> [!open-question] **Question**
> What are the implications for training models beyond current compute budgets?
>
> *What would resolve it:* Further research into extrapolating scaling laws to larger scales could provide insights into future trends in large language model performance and resource requirements.

<!-- enhancement-pass:1 (2026-05-23) -->

> [!open-question] **Question**
> How do advancements in hardware technology affect the validity of existing scaling laws?
>
> *What would resolve it:* Further research into how changes in compute resources impact optimal scaling ratios would help resolve this question. This could involve re-evaluating scaling laws with newer, more powerful hardware to determine if and how these principles need adjustment.

## Synthesis

LLM scaling laws are crucial for optimizing the design, training, and deployment of large language models. By balancing model size with training data volume within given compute budgets, these laws enable practitioners to achieve optimal performance efficiently. Understanding these principles is essential for advancing the field of neural network training in practical applications.

<!-- enhancement-pass:1 (2026-05-23) -->
LLM scaling laws serve as a critical framework for optimizing the design and training of large language models within practical constraints. By balancing model size with training data volume and compute budget, practitioners can achieve optimal performance efficiently, making these laws indispensable in advancing neural network training practices.

## Connections & Context

**Falls under:** [[Neural Network Training]]

**Contrasts with:** [[Emergent Abilities in LLMS]]

**Applies to:** [[Parameter-Efficient Fine-Tuning]]

**Source:** [[llm-scaling-laws-synthetic-seed-2026-05-21]]

<!-- enhancement-pass:1 (2026-05-23) -->

### Why these connections matter

> [!connection] **[[Parameter-Efficient Fine-Tuning]]** — *applies-to*
> LLM scaling laws provide foundational insights into resource allocation that directly inform parameter-efficient fine-tuning strategies. By understanding the optimal ratios between model size and training data, practitioners can apply these principles to fine-tune models more efficiently, ensuring that neither parameter nor token scarcity limits performance.


# LLM Scaling Laws

> [!definition] **LLM Scaling Laws**
> LLM scaling laws describe empirical power-law relationships between model performance and scale (parameters N, training tokens D), as well as compute budget C in language models, discovered through systematic experimentation. These laws exclude theoretical frameworks not grounded in empirical data or those that do not specifically address the scaling of parameters, training tokens, and compute budget. It falls under Neural Network Training.

> [!attention] **Boundary**
> This concept excludes theoretical frameworks not grounded in empirical data or those that do not specifically address the scaling of parameters, training tokens, and compute budget. It should not be confused with general machine learning performance metrics without a focus on scale relationships.
