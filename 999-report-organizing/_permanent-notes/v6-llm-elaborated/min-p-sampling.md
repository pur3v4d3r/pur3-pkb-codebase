---
title: Min-P Sampling
aliases:
  - Min-P Sampling
  - minimum probability sampling
  - min-p decoding
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - prompt-engineering

domain: prompt-engineering
subdomains:
  - llm-generation
  - prompt-engineering

created: 2026-05-20
updated: '2026-05-23'
source-type: report-extraction
source-reports:
  - min-p-sampling-synthetic-seed-2026-05-20
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: enhanced
parent-concept: LLM Decoding Strategies
related:
  - '[[Top-P Nucleus Sampling]]'
  - '[[Temperature-Sampling]]'
prerequisites:
  - '[[]]'
specializes:
  - '[[]]'
broader:
  - '[[]]'
see-also:
  - '[[]]'
contrasts-with:
  - '[[Top-P Nucleus Sampling]]'
contradicts:
  - '[[]]'
applies-to:
  - '[[Temperature-Sampling]]'
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
  last-enhanced: '2026-05-20'
  diagram-passes: 1
  diagram-model: qwen2.5:14b-instruct-q5_K_M
  last-diagrammed: '2026-05-23'
---

## 📊 Visual Overview

<!-- diagram-pass:1 (2026-05-23) -->

> [!abstract] **Diagram 1 — Min-P Sampling Process Flow**
> *Follow the flow from input to output, noting key steps.*
>
> ```mermaid
> flowchart LR
>   A[Input Sequence] --> B[Determine Highest Probability]
>   B --> C[Set Relative Threshold p_min]
>   C --> D[Filter Tokens Below Threshold]
>   D --> E[Select Token for Output]
> ```


> [!abstract] **Diagram 2 — Min-P vs Top-P Comparison**
> *Compare the dynamic threshold of Min-P with static top-p.*
>
> ```mermaid
> graph TD
>   A[Top-P Sampling]
>   B[Min-P Sampling]
>   C[Highest Probability Token]
>   D[Cumulative Threshold]
>   E[Relative Threshold p_min]
>   F[Filter Tokens Below Threshold]
>   G[Select Token for Output]
>   A -->|Cumulative Threshold| F
>   B -->|Highest Probability Token| C
>   C -->|Set Relative Threshold| E
>   E -->|Filter Tokens Below Threshold| F
>   F -->|Select Token for Output| G
> ```

# Min-P Sampling

> [!definition] **Min-P Sampling**
> Min-P Sampling is a decoding strategy that filters out tokens whose probability falls below a fraction p_min of the highest-probability token's probability, thereby dynamically adjusting its nucleus based on model confidence rather than using static thresholds like top-k or cumulative cutoffs like top-p. It falls under LLM Decoding Strategies.

> [!attention] **Boundary**
> It should not be confused with absolute thresholding methods like top-k or cumulative probability cutoffs like top-p. It dynamically adjusts its nucleus based on model confidence, unlike static thresholds used in other sampling techniques.

## Core Explanation

Min-P Sampling operates by setting a relative threshold for token selection that scales with the highest-probability token's probability, ensuring that only tokens above this dynamic threshold are considered during generation. This mechanism allows Min-P to adaptively exclude low-confidence options while preserving high-quality alternatives, making it particularly effective in scenarios where maintaining coherent output is crucial despite high model uncertainty.

In practice, Min-P Sampling dynamically adjusts its nucleus size based on the distribution of probabilities assigned by the language model at each step of generation. When the highest probability token has a very high likelihood (e.g., 0.9), tokens with probabilities below p_min times this value are filtered out, ensuring that only highly probable options are considered. Conversely, in cases where the probability distribution is more evenly spread, Min-P continues to exclude low-probability tokens relative to the highest one, maintaining a focus on high-confidence predictions.

The theoretical underpinning of Min-P Sampling lies in its ability to balance quality and diversity by filtering out tokens that are likely to be garbage or irrelevant at higher temperatures. This approach contrasts with top-p sampling, which uses a cumulative probability cutoff to define the nucleus, potentially including many low-probability tokens as temperature increases.

Empirically, Min-P Sampling has been shown to provide better quality-diversity tradeoffs than top-p at high temperatures by more aggressively filtering out incoherent low-probability tokens while preserving genuine alternatives. This makes it particularly valuable for creative or exploratory modes of generation where maintaining coherent output is essential.

<!-- enhancement-pass:1 (2026-05-20) -->
Min-P Sampling's dynamic nature allows it to adaptively respond to varying levels of model uncertainty, which is particularly advantageous in complex or ambiguous contexts where the distribution of token probabilities can shift dramatically from one generation step to another. This adaptability not only enhances coherence but also supports more nuanced exploration of potential outputs by filtering out tokens that are likely to introduce noise or confusion.

In contrast to static threshold methods like top-k, which rely on a fixed number of highest-probability tokens regardless of their actual likelihoods, Min-P Sampling ensures that the selection process remains sensitive to the model's current confidence levels. This sensitivity can lead to more consistent and reliable outputs across different input scenarios, as it avoids including low-probability tokens that might be artifacts of noise or overfitting.

## Practical Implications

> [!example] **Application 1 — Creative Writing**
> In creative writing, Min-P Sampling can enhance the quality and coherence of generated text by filtering out low-probability tokens that are likely to be incoherent or irrelevant. This ensures that the output remains focused on high-confidence predictions while still allowing for a diverse range of possible outcomes.

> [!example] **Application 2 — High-Temperature Generation**
> At higher temperatures, where top-p sampling may include many low-probability tokens leading to incoherent text, Min-P Sampling continues to exclude tokens that are far below the best option. This helps maintain generation quality and coherence even when exploring more diverse or unexpected outcomes.

## Key Distinctions

> [!key-distinction] **Min-P vs Top-P**
> Unlike top-p sampling, which uses a cumulative probability cutoff to define its nucleus, Min-P Sampling sets a relative threshold that scales with the highest-probability token's likelihood. This dynamic adjustment allows Min-P to more effectively filter out low-confidence tokens while preserving high-quality alternatives.

<!-- enhancement-pass:1 (2026-05-20) -->

> [!key-distinction] **Reflective vs Reactive Thinking**
> Min-P Sampling embodies reflective thinking by dynamically adjusting its nucleus based on the model's current confidence levels, whereas static threshold methods like top-k represent reactive thinking by applying a fixed rule without considering context. This distinction is crucial as Min-P allows for more thoughtful and adaptive generation processes that can better handle complex or uncertain input scenarios.

> [!key-distinction] **Intrinsic vs Extrinsic Load**
> Min-P Sampling reduces intrinsic cognitive load on the model by filtering out low-probability tokens, which are often less relevant or coherent. This contrasts with top-p sampling, where a higher extrinsic load is imposed due to including many low-probability tokens that may not contribute meaningfully to the output quality.

## Common Misconceptions

<!-- enhancement-pass:1 (2026-05-20) -->

> [!warning] **Misconception** — Min-P Sampling always produces more coherent text than other methods.
>
> While Min-P Sampling often enhances coherence by filtering out low-probability tokens, its effectiveness can vary depending on the specific context and model confidence levels. In some cases, particularly with highly confident models, top-p sampling might still produce coherent outputs while offering greater diversity.

## Open Questions

> [!open-question] **Question**
> How does min-p sampling perform compared to other methods at different model confidence levels?
>
> *What would resolve it:* Comparative studies across various model confidence levels would provide insights into the relative performance of Min-P Sampling versus top-p and top-k.

> [!open-question] **Question**
> What is the optimal calibration of p_min for various generation tasks?
>
> *What would resolve it:* Experimental tuning of p_min values in different scenarios could help identify the best settings for maintaining quality while maximizing diversity.

## Synthesis

Min-P Sampling stands out as a valuable addition to the LLM decoding toolkit, especially for creative or exploratory modes of generation. By dynamically adjusting its nucleus based on model confidence, it offers better quality-diversity tradeoffs than top-p at high temperatures, making it an essential tool for maintaining coherent output in scenarios where exploration is key.

<!-- enhancement-pass:1 (2026-05-20) -->
Min-P Sampling emerges as a sophisticated decoding strategy that leverages dynamic thresholds to enhance both coherence and diversity in generated text. By adapting its nucleus size based on model confidence, it offers a flexible approach that can be finely tuned for different generation tasks, making it an indispensable tool in the LLM decoding toolkit.

## Connections & Context

**Falls under:** [[LLM Decoding Strategies]]

**Contrasts with:** [[Top-P Nucleus Sampling]]

**Applies to:** [[Temperature-Sampling]]

**Source:** [[min-p-sampling-synthetic-seed-2026-05-20]]

<!-- enhancement-pass:1 (2026-05-20) -->

### Why these connections matter

> [!connection] **[[Temperature-Sampling]]** — *applies-to*
> Min-P Sampling is especially effective in high-temperature scenarios where the probability distribution becomes more spread out, making it crucial to filter out low-probability tokens that could lead to incoherent text. By dynamically adjusting its nucleus based on model confidence, Min-P Sampling helps maintain output quality even as temperature increases.

> [!connection] **[[Top-P Nucleus Sampling]]** — *contrasts-with*
> While both methods aim to improve generation quality by filtering out low-probability tokens, they differ fundamentally in their approach. Top-P uses a cumulative probability cutoff that includes many low-probability tokens as temperature increases, whereas Min-P sets a relative threshold based on the highest-probability token's likelihood, ensuring more aggressive exclusion of irrelevant options.
