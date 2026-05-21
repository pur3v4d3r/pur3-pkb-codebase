---
title: "Full Fine-Tuning vs Parameter-Efficient Fine-Tuning"
aliases:
  - "Full Fine-Tuning vs Parameter-Efficient Fine-Tuning"
  - "Full Fine-Tuning vs PEFT"
  - "full fine-tuning versus PEFT"
  - "FFT vs PEFT"
  - "full-parameter vs parameter-efficient fine-tuning"
type: permanent-note
status: enriched
confidence: high

tags:
  - permanent-note
  - v6-llm-elaborated
  - prompt-engineering

domain: prompt-engineering
subdomains:
  - machine-learning
  - llm-training
  - resource-efficient-ai

created: 2026-05-21
updated: 2026-05-21

source-type: report-extraction
source-reports:
  - "full-fine-tuning-vs-peft-synthetic-seed-2026-05-21"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)"

complexity-level: advanced-practitioner
depth-level: elaborated

parent-concept: "LLM Fine-Tuning"

related:
  - "[[Parameter-Efficient Fine-Tuning Methods]]"
  - "[[Catastrophic Forgetting in LLMs]]"
prerequisites:
  - "[[]]"
specializes:
  - "[[Parameter-Efficient Fine-Tuning Methods]]"
broader:
  - "[[]]"
see-also:
  - "[[]]"
contrasts-with:
  - "[[Catastrophic Forgetting in LLMs]]"
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

# Full Fine-Tuning vs Parameter-Efficient Fine-Tuning

> [!definition] **Full Fine-Tuning vs Parameter-Efficient Fine-Tuning**
> Full fine-tuning (FFT) and parameter-efficient fine-tuning (PEFT) represent a critical trade-off in adapting large language models (LLMs), where FFT updates all model parameters during training, maximizing expressivity but at the cost of substantial compute resources and risk of catastrophic forgetting. PEFT methods, such as LoRA, adapter layers, and prefix tuning, update only task-specific parameters while freezing the pretrained backbone, significantly reducing memory requirements and enabling multiple adaptations to share a single backbone efficiently. This concept falls under LLM Fine-Tuning.

> [!attention] **Boundary**
> This concept excludes specific methods of PEFT such as LoRA, adapter layers, and prefix tuning which are detailed implementations within the broader category. It also does not cover the specifics of catastrophic forgetting or gradient descent mechanisms unless directly relevant to FFT vs PEFT trade-offs.

## Core Explanation

Full fine-tuning (FFT) involves updating all model parameters during training, which allows for maximal expressivity but comes with significant drawbacks such as high computational cost and the risk of catastrophic forgetting where the model may lose its general capabilities. In contrast, parameter-efficient fine-tuning (PEFT) methods update only a small fraction of task-specific parameters while keeping the pretrained backbone frozen. This approach dramatically reduces memory requirements and allows for efficient adaptation to multiple tasks using a single backbone.

The choice between FFT and PEFT hinges on balancing expressivity against resource efficiency. FFT is advantageous when the target task significantly deviates from the pretraining distribution, as it can capture novel patterns that the pretrained model might not have encountered during initial training. However, this comes at the cost of substantial computational resources required to store gradients for all parameters.

PEFT methods offer a more efficient alternative by updating only a small fraction of parameters, thereby reducing memory usage and enabling multiple task-specific adaptations to share a single backbone efficiently. This is particularly beneficial in scenarios where the adaptation dataset is small to medium-sized, as PEFT can match FFT performance while using an order of magnitude fewer compute resources.

The theoretical underpinning of this trade-off lies in understanding that the intrinsic dimensionality of task-specific adaptation may be much lower than the total number of parameters in a large language model. This insight challenges the naive assumption that more trainable parameters always lead to better adapted models, highlighting instead the importance of efficient parameter updates.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design for LLM fine-tuning, understanding the FFT vs PEFT trade-off is crucial. For tasks closely aligned with pretraining data and small to medium-sized datasets, PEFT methods can achieve comparable performance while significantly reducing computational costs. This allows for more efficient use of resources in educational settings where budget constraints are common.

> [!example] **Application 2 — Resource-constrained environments**
> In resource-constrained environments such as edge devices or low-power computing platforms, the choice between FFT and PEFT can be a matter of feasibility. PEFT methods offer a viable solution by drastically reducing memory usage and computational requirements, enabling efficient fine-tuning even on limited hardware.

## Key Distinctions

> [!key-distinction] **Memory Usage in FFT vs PEFT**
> A key distinction between full fine-tuning (FFT) and parameter-efficient fine-tuning (PEFT) lies in their memory usage. FFT requires storing gradients for all model parameters, leading to high memory demands during training. In contrast, PEFT methods update only a small fraction of task-specific parameters, significantly reducing the memory footprint.

## Key Figures

- **John Sweller** — While not directly involved in LLM fine-tuning research, John Sweller's work on cognitive load theory provides theoretical underpinnings for understanding the trade-offs between FFT and PEFT. His insights into intrinsic vs extraneous cognitive loads can be analogously applied to understand how different fine-tuning methods manage computational resources.

## Open Questions

> [!open-question] **Question**
> What are the optimal conditions under which full fine-tuning outperforms parameter-efficient methods?
>
> *What would resolve it:* Empirical studies comparing FFT and PEFT across a range of datasets with varying degrees of domain shift from pretraining would help identify scenarios where FFT offers superior performance.

## Synthesis

Understanding the trade-offs between full fine-tuning (FFT) and parameter-efficient fine-tuning (PEFT) is crucial for optimizing LLM adaptation. This knowledge enables practitioners to make informed decisions based on specific task requirements, available resources, and dataset characteristics, thereby enhancing both efficiency and effectiveness in model deployment.

## Connections & Context

**Falls under:** [[LLM Fine-Tuning]]

**Specializes:** [[Parameter-Efficient Fine-Tuning Methods]]

**Contrasts with:** [[Catastrophic Forgetting in LLMs]]

**Source:** [[full-fine-tuning-vs-peft-synthetic-seed-2026-05-21]]
