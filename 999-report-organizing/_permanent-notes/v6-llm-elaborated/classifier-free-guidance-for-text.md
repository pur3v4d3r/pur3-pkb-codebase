---
title: Classifier-Free Guidance for Text
aliases:
  - Classifier-Free Guidance for Text
  - CFG for text
  - text classifier-free guidance
  - language model CFG
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - prompt-engineering

domain: prompt-engineering
subdomains:
  - llm-inference
  - controlled-generation
  - diffusion-analogies

created: 2026-05-21
updated: '2026-05-21'
source-type: report-extraction
source-reports:
  - classifier-free-guidance-for-text-synthetic-seed-2026-05-21
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: elaborated
parent-concept: Language Model Inference Techniques
related:
  - '[[Contrastive Decoding]]'
  - '[[Logit Bias Manipulation]]'
prerequisites:
  - '[[]]'
specializes:
  - '[[]]'
broader:
  - '[[]]'
see-also:
  - '[[]]'
contrasts-with:
  - '[[Contrastive Decoding]]'
  - '[[Logit Bias Manipulation]]'
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
  diagram-passes: 1
  diagram-model: qwen2.5:14b-instruct-q5_K_M
  last-diagrammed: '2026-05-21'
---

## 📊 Visual Overview

<!-- diagram-pass:1 (2026-05-21) -->

> [!abstract] **Diagram 1 — CFG Process Flowchart**
> *Follow the steps from input to output generation.*
>
> ```mermaid
> flowchart LR
>   A[Input Prompt] --> B[Conditional Distribution]
>   C[Unconditional Distribution] --> D[Weighted Combination]
>   B --> D
>   E[Guidance Scale] --> D
>   D --> F[Final Sampling Distribution]
> ```


> [!abstract] **Diagram 2 — CFG Mechanism Diagram**
> *Observe the formula and its components for CFG.*
>
> ```mermaid
> graph TD
>   A[Unconditional Logits] --> B{+}
>   C[Conditional Logits] --> D{-}
>   E[Guidance Scale] --> F{*}
>   G[Difference] --> H{+}
>   B --> I[Weighted Sum]
>   D --> H
>   F --> H
> ```

# Classifier-Free Guidance for Text

> [!definition] **Classifier-Free Guidance for Text**
> Classifier-free guidance (CFG) for text is an inference technique that amplifies the influence of conditioning signals in autoregressive language models by combining conditional and unconditional next-token distributions. Unlike other decoding methods such as contrastive decoding or logit bias manipulation, CFG specifically computes a weighted sum of these distributions to steer generation towards desired attributes or instructions. It falls under Language Model Inference Techniques.

> [!attention] **Boundary**
> This concept excludes other decoding methods like contrastive decoding, logit bias manipulation, or sampling techniques such as temperature sampling and top-p nucleus sampling. It should not be confused with image diffusion CFG methods which are adapted for text generation.

## Core Explanation

Classifier-free guidance (CFG) for text is an innovative technique that enhances the control over language model outputs by amplifying conditioning signals through a weighted combination of conditional and unconditional next-token distributions. This method allows for more precise generation of text that adheres closely to specified conditions, such as system prompts or class labels, while maintaining computational efficiency compared to other methods like contrastive decoding or logit bias manipulation.

At the heart of CFG is its ability to balance between output consistency and fluency by adjusting a guidance scale parameter. This parameter determines how strongly the model's generation is influenced by the conditioning signal, with higher values leading to outputs that are more consistent but potentially less fluent. The technique requires two forward passes per generation step—one for the conditional distribution given the prompt and condition, and another for the unconditional distribution without the condition—doubling the computational cost of inference.

The theoretical underpinning of CFG lies in its ability to leverage the natural representation capabilities of language models for counterfactual scenarios. By comparing how a model generates text with and without conditioning information, CFG can isolate and amplify the impact of that information on subsequent tokens. This approach is particularly effective when the condition is expressed in a format where the unconditional model can naturally represent the absence of that condition.

Empirically, CFG has shown promise in various controlled generation tasks, such as generating text under specific stylistic constraints or following detailed instructions. However, its effectiveness and limitations are highly dependent on the guidance scale parameter, which must be carefully tuned to avoid amplifying artifacts or producing repetitive outputs.

## Mechanism

The mechanism of CFG for text involves computing a weighted combination of conditional and unconditional next-token distributions at each generation step. Specifically, it calculates logits_final as logits_unconditional + guidance_scale × (logits_conditional − logits_unconditional). This formula amplifies the influence of the conditioning signal by adding a scaled difference between the conditional and unconditional logits to the unconditional distribution.

This process ensures that the final sampling distribution is more heavily influenced by the specified condition, thereby steering generation towards outputs that are more consistent with the desired attributes or instructions. The guidance scale parameter controls how strongly this amplification occurs, allowing for fine-grained control over the balance between output consistency and fluency.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design, CFG can be used to generate text that closely follows specific guidelines or instructions. For example, when designing educational materials, CFG allows for the generation of content that adheres strictly to a given curriculum or learning objective. This ensures that generated text is not only relevant but also consistent with the intended teaching goals.

> [!example] **Application 2 — Content moderation**
> In content moderation, CFG can help in generating text that avoids certain undesirable attributes such as toxicity or inappropriate language. By conditioning on a set of rules or guidelines, CFG ensures that generated text is safe and appropriate for public consumption. This application highlights the importance of carefully tuning the guidance scale to balance between strict adherence to rules and maintaining natural language fluency.

## Key Distinctions

> [!key-distinction] **Classifier-Free Guidance vs Contrastive Decoding**
> While both classifier-free guidance (CFG) and contrastive decoding aim to enhance control over text generation, they differ in their approach. CFG combines conditional and unconditional distributions using a weighted sum, whereas contrastive decoding directly compares the likelihood of tokens under different conditions without combining them. This distinction is crucial as it affects how each method handles conditioning information and influences the trade-offs between output consistency and fluency.

> [!key-distinction] **Weighted Distribution Combination vs Direct Logit Bias**
> CFG for text uses a weighted combination of conditional and unconditional distributions to amplify the influence of conditioning signals, while logit bias manipulation directly modifies logits without combining distributions. This difference impacts how each method balances output consistency with fluency and computational efficiency.

## Open Questions

> [!open-question] **Question**
> What are the optimal guidance scales and conditions for effective use of CFG for text?
>
> *What would resolve it:* Empirical studies comparing different guidance scales across various generation tasks would provide insights into the best practices.

> [!open-question] **Question**
> How can we mitigate the trade-off between output consistency and fluency in high guidance scale scenarios?
>
> *What would resolve it:* Research exploring post-processing techniques or hybrid methods that combine CFG with other decoding strategies could help address this issue.

## Synthesis

Classifier-free guidance (CFG) for text represents a significant advancement in language model inference, particularly for tasks requiring controlled generation. By amplifying the influence of conditioning signals through a weighted combination of distributions, CFG enables more precise control over output attributes while maintaining computational efficiency. This technique is especially valuable in scenarios where adherence to specific instructions or guidelines is crucial.

However, the effectiveness of CFG depends on careful tuning of its parameters and understanding of its limitations. Future research should focus on optimizing guidance scales for different tasks and mitigating trade-offs between consistency and fluency.

## Connections & Context

**Falls under:** [[Language Model Inference Techniques]]

**Contrasts with:** [[Contrastive Decoding]] · [[Logit Bias Manipulation]]

**Source:** [[classifier-free-guidance-for-text-synthetic-seed-2026-05-21]]
