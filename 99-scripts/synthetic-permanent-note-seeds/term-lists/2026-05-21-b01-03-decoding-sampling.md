---
batch_name: b01-03-decoding-sampling
batch_date: 2026-05-21
default_domain: llm-inference
default_confidence: high
notes: |
  Decoding and sampling strategies for LLMs covering temperature, top-k, top-p,
  beam search, greedy, contrastive, typical, min-p sampling, repetition penalty,
  classifier-free guidance for text, and logit bias manipulation.
---

# Batch: B01-03 Decoding and Sampling Strategies

## Temperature Sampling

- secondary_domains: [llm-inference, probabilistic-reasoning, generative-models]
- aliases: [temperature in LLMs, softmax temperature, sampling temperature]
- broader: [llm-decoding, sampling-methods]
- narrower: []
- related: [top-k-sampling, top-p-nucleus-sampling, greedy-decoding, typical-sampling, min-p-sampling]
- prerequisites: [softmax-function, language-model-inference, probability-distributions]
- confidence: high

**definition**: Temperature sampling is a decoding parameter that controls the sharpness of the next-token probability distribution during language model inference by dividing the model's logit scores by a temperature scalar T before applying the softmax function. At T=1, the distribution matches the model's trained probabilities; at T→0, the distribution collapses to a deterministic argmax (greedy decoding); at T>1, the distribution flattens, increasing entropy and randomness; at 0<T<1, the distribution sharpens, concentrating probability mass on high-probability tokens. Temperature is one of the most commonly tuned inference parameters, with lower values preferred for factual or constrained tasks and higher values preferred for creative generation.

**key_claim**: Temperature does not change which tokens are possible — it rescales the existing probability distribution without introducing new candidates — so it is only effective when the model already assigns non-trivial probability mass to desirable tokens; temperature cannot compensate for a model with a wrong distribution, it can only trade off between fidelity to the model's most likely output and diversity of generation.

**warning**: Temperature interacts non-linearly with vocabulary size and the skewness of the logit distribution — the same temperature value produces qualitatively different sampling behaviour across models with different logit scales, making temperature hyperparameters non-portable across model families; calibrating temperature by perplexity or diversity metrics on held-out data is necessary rather than reusing values from other models.

## Top-K Sampling

- secondary_domains: [llm-inference, generative-models]
- aliases: [top-K decoding, K-truncated sampling, top-k token sampling]
- broader: [llm-decoding, sampling-methods]
- narrower: []
- related: [temperature-sampling, top-p-nucleus-sampling, typical-sampling, min-p-sampling, repetition-penalty]
- prerequisites: [language-model-inference, probability-distributions, temperature-sampling]
- confidence: high

**definition**: Top-K sampling is a decoding method that restricts the next-token sampling distribution to the K highest-probability tokens at each generation step, setting all other tokens to zero probability and renormalising the K remaining probabilities to sum to one before sampling. By eliminating the long tail of low-probability tokens, top-K reduces the risk of sampling degenerate or nonsensical tokens while preserving stochastic generation. Top-K was one of the earliest truncation methods proposed for LLM decoding and remains widely used, often in combination with temperature scaling.

**key_claim**: Top-K sampling's fixed truncation threshold is its primary limitation — because the entropy of the next-token distribution varies dramatically across token positions (high-entropy contexts have flat distributions while low-entropy contexts are sharply peaked), a fixed K either over-restricts high-entropy contexts (reducing creativity) or under-restricts low-entropy contexts (risking low-quality tokens), making top-K less adaptive than nucleus (top-p) sampling.

**warning**: Top-K interacts poorly with different model architectures and vocabulary sizes — a K value that works well for one model may be too restrictive for another with a different logit scale or vocabulary, and K=40 (a common default) has no principled basis; top-K should be treated as a rough truncation heuristic rather than a principled sampling method, with top-p generally preferred for its adaptive behaviour.

## Top-P Nucleus Sampling

- secondary_domains: [llm-inference, generative-models, probabilistic-reasoning]
- aliases: [nucleus sampling, top-p sampling, p-nucleus decoding]
- broader: [llm-decoding, sampling-methods]
- narrower: []
- related: [temperature-sampling, top-k-sampling, typical-sampling, min-p-sampling, contrastive-decoding]
- prerequisites: [language-model-inference, probability-distributions, top-k-sampling]
- confidence: high

**definition**: Top-p (nucleus) sampling is a truncation-based decoding method introduced by Holtzman et al. (2020) that dynamically determines the token candidate set at each generation step by selecting the smallest set of tokens whose cumulative probability mass meets or exceeds a threshold p, then renormalising and sampling from this set. Unlike top-K which fixes the number of candidates, top-p adapts to the entropy of the current distribution: in high-entropy contexts (many plausible next tokens), the nucleus is large; in low-entropy contexts (nearly deterministic next tokens), the nucleus is small. Top-p is the most widely used truncation method in production LLM deployment.

**key_claim**: Nucleus sampling's adaptive candidate set is the key advance over top-K — by basing truncation on cumulative probability mass rather than rank, top-p remains appropriate across positions with very different distribution entropies, maintaining diversity in ambiguous contexts while staying focused in predictable contexts; this dynamic adaptation is why nucleus sampling generalises better across different tasks and contexts than top-K with any fixed K value.

**warning**: Nucleus sampling does not eliminate all failure modes — high-p values (p>0.95) in low-entropy contexts still allow sampling from a long tail of improbable tokens that happen to fall within the nucleus, and the interaction between top-p and temperature requires careful calibration since temperature-flattened distributions produce larger nuclei than temperature-sharpened ones, making the effective degree of truncation dependent on both parameters.

## Beam Search Decoding

- secondary_domains: [llm-inference, search-algorithms, generative-models]
- aliases: [beam search, breadth-first beam search, approximate Viterbi decoding]
- broader: [llm-decoding, sequence-decoding]
- narrower: [diverse-beam-search, constrained-beam-search]
- related: [greedy-decoding, temperature-sampling, top-p-nucleus-sampling, contrastive-decoding]
- prerequisites: [language-model-inference, search-algorithms, sequence-probability]
- confidence: high

**definition**: Beam search decoding is a deterministic approximate search algorithm for sequence generation that maintains a fixed number of partial hypotheses (the beam width B) at each generation step by expanding all B current hypotheses by one token and retaining the B expanded sequences with the highest cumulative log-probability. Unlike greedy decoding which commits to the single highest-probability token at each step, beam search explores multiple possible continuations simultaneously, often finding sequences with higher overall probability than greedy decoding. Beam search was the dominant decoding strategy for neural machine translation and other structured prediction tasks before large language model generation became the dominant paradigm.

**key_claim**: Beam search's dominance in structured generation tasks (translation, summarisation, code generation) does not transfer to open-ended generation tasks — in open-ended generation, beam search produces degenerate repetitive outputs because sequences with high per-token probability under an autoregressive LM are often repetitive and generic, a phenomenon called the beam search pathology; this explains why stochastic sampling methods outperform beam search for creative and conversational generation.

**warning**: Beam search with small beam widths is not meaningfully different from greedy decoding in many contexts — beam width B=4 rarely produces significantly better outputs than B=1 for large LLMs with well-calibrated distributions, and the computational cost scales linearly with B; the historical default of B=4 or B=5 from neural MT does not generalise to modern LLMs.

## Greedy Decoding

- secondary_domains: [llm-inference, deterministic-algorithms]
- aliases: [argmax decoding, greedy token selection, deterministic decoding]
- broader: [llm-decoding, sequence-decoding]
- narrower: []
- related: [beam-search-decoding, temperature-sampling, top-p-nucleus-sampling, repetition-penalty]
- prerequisites: [language-model-inference, argmax-operation]
- confidence: high

**definition**: Greedy decoding is the simplest LLM decoding strategy in which, at each generation step, the token with the highest probability (argmax over the vocabulary) is selected unconditionally. The resulting sequence is fully deterministic given the model weights and prompt. Greedy decoding is equivalent to temperature sampling at T→0 and produces the locally optimal token at every step, but not the globally optimal sequence — it can get trapped by locally high-probability choices that preclude better subsequent tokens. Despite its limitations, greedy decoding is used in latency-critical applications where determinism and speed are priorities.

**key_claim**: Greedy decoding's locally optimal decisions are globally suboptimal in any setting where good sequences require non-obvious intermediate tokens — the standard machine translation example shows that greedy decoding sometimes produces translations of significantly lower BLEU than beam search, precisely because the globally best translation requires committing to a token that is locally unlikely; this makes greedy decoding appropriate only for very well-behaved, low-entropy generation tasks.

**warning**: Greedy decoding's determinism is often misinterpreted as reliability — a greedy decoder that produces a confident-sounding but incorrect answer provides no epistemic uncertainty signal, whereas a sampled decoder that produces the same incorrect answer most of the time but occasionally produces the correct answer reveals the model's uncertainty; greedy decoding hides the model's distributional uncertainty behind a point estimate.

## Contrastive Decoding

- secondary_domains: [llm-inference, quality-decoding, hallucination-reduction]
- aliases: [CD decoding, amateur-expert contrast decoding, contrastive language generation]
- broader: [llm-decoding, sampling-methods]
- narrower: []
- related: [beam-search-decoding, temperature-sampling, top-p-nucleus-sampling, classifier-free-guidance-for-text]
- prerequisites: [language-model-inference, probability-distributions, language-model-scaling]
- confidence: high

**definition**: Contrastive decoding is a decoding strategy introduced by Li et al. (2022) that computes the next-token probability distribution as the difference between a large expert language model and a small amateur language model over the same prefix, after applying an adaptive truncation mask that retains only tokens where the expert's probability exceeds a threshold. The intuition is that the expert model's relative advantage over the amateur most precisely captures the expert's distinctive knowledge and capabilities — tokens that both models assign high probability are generic and uninteresting, while tokens the expert assigns much higher probability than the amateur reflect the expert's learned competence.

**key_claim**: Contrastive decoding addresses the repetition and incoherence failures of standard sampling by explicitly removing tokens that are generic (assigned high probability by both models) and tokens that are locally likely but contextually inappropriate (assigned high probability by the amateur but not the expert), producing outputs that are qualitatively more coherent and specific than standard sampling without sacrificing fluency.

**warning**: Contrastive decoding requires access to both an expert and an amateur model simultaneously during inference, doubling the memory and compute requirements, and the performance gain is sensitive to the relative scale gap between the two models — if the amateur is too weak, the contrast provides poor signal; if the amateur is too capable, the advantage is erased; selecting and maintaining the right amateur model pair is an engineering burden.

## Typical Sampling

- secondary_domains: [llm-inference, information-theory, generative-models]
- aliases: [locally typical sampling, entropy-based sampling, typicality sampling]
- broader: [llm-decoding, sampling-methods]
- narrower: []
- related: [top-p-nucleus-sampling, top-k-sampling, temperature-sampling, min-p-sampling]
- prerequisites: [language-model-inference, information-entropy, probability-distributions]
- confidence: high

**definition**: Typical sampling is a decoding method proposed by Meister et al. (2023) that selects tokens whose information content is closest to the expected information content (entropy) of the model's next-token distribution, rather than selecting the highest-probability tokens. At each generation step, tokens are ranked by how close their log-probability is to the negative entropy of the distribution (the "typical" amount of information), and the set of typical tokens is sampled from after renormalisation. The method is motivated by information-theoretic arguments that a well-generated sequence should contain tokens whose information content matches the expected entropy of the distribution throughout the sequence.

**key_claim**: Typical sampling produces outputs with more consistent local coherence than top-p sampling on tasks requiring narrative consistency, because it explicitly avoids both the safest tokens (which produce repetitive, generic text) and the most surprising tokens (which produce jarring non-sequiturs), keeping generation within the information-theoretically typical region of the distribution that corresponds to natural language patterns.

**warning**: Typical sampling's advantage over top-p is modest in practice and task-dependent — empirical comparisons show mixed results across different generation tasks, and the information-theoretic motivation, while elegant, does not straightforwardly predict which tasks benefit from typical sampling; it is a research-grade technique rather than a production default.

## Min-P Sampling

- secondary_domains: [llm-inference, generative-models, sampling-methods]
- aliases: [minimum probability sampling, min-p threshold decoding, adaptive floor sampling]
- broader: [llm-decoding, sampling-methods]
- narrower: []
- related: [top-p-nucleus-sampling, top-k-sampling, temperature-sampling, typical-sampling]
- prerequisites: [language-model-inference, probability-distributions, top-p-nucleus-sampling]
- confidence: high

**definition**: Min-P sampling is a decoding method that sets a dynamic probability floor at each generation step by scaling the minimum acceptable token probability as a fraction of the highest-probability token's probability: a token is included in the candidate set if its probability exceeds min_p × max_probability. Unlike top-p which computes a cumulative mass threshold, min-P computes a relative floor — maintaining a fixed ratio between the maximum and minimum acceptable probabilities rather than a fixed cumulative mass. This means the candidate set is empty except near the maximum in highly peaked distributions and broad in flat distributions, adapting more smoothly to distribution shape than top-p.

**key_claim**: Min-P sampling resolves a specific failure mode of top-p sampling where the nucleus becomes pathologically large in high-entropy contexts — top-p with p=0.95 on a near-uniform distribution over 50,000 tokens allows sampling of tokens with probability as low as 0.95/50000, while min-P with threshold 0.05 would retain only tokens within 5% of the top probability; this makes min-P particularly effective for creative generation at high temperatures where top-p tends to sample degenerate tokens.

**warning**: Min-P is a recently proposed method (2024) with limited empirical evaluation relative to top-p and top-K — while its theoretical properties are appealing, the appropriate default threshold value is not well-established across model families, and like all sampling hyperparameters it requires tuning rather than a universal default; it has not yet displaced top-p as the standard recommendation.

## Repetition Penalty

- secondary_domains: [llm-inference, text-generation-quality]
- aliases: [repeat penalty, frequency penalty, anti-repetition scoring, no-repeat-ngram]
- broader: [llm-decoding, inference-quality-control]
- narrower: [no-repeat-ngram-constraint, frequency-penalty, presence-penalty]
- related: [temperature-sampling, top-p-nucleus-sampling, greedy-decoding, beam-search-decoding]
- prerequisites: [language-model-inference, softmax-function, token-generation]
- confidence: high

**definition**: Repetition penalty is a decoding heuristic that discourages the model from generating tokens that have already appeared in the current context by modifying the logit scores of previously generated tokens before sampling. In the most common formulation (Keskar et al., 2019), the logit of any token already present in the context is divided by a penalty coefficient greater than 1 (reducing positive logits) or multiplied by it (amplifying negative logits), making the already-seen token less likely. OpenAI's API exposes a related concept as frequency penalty (scales penalty by count) and presence penalty (flat penalty for any appearance).

**key_claim**: Repetition penalty is a necessary patch for a systematic failure mode of neural language models — because autoregressive LLMs compute next-token probabilities conditioned on local context, they are biased toward repeating high-probability tokens from the recent context, especially in deterministic or low-temperature decoding; repetition penalty breaks the positive feedback loop between generating a token and subsequently increasing its probability in the context, but at the cost of a hyperparameter that must be tuned carefully to avoid suppressing legitimate repetition (e.g., character names, technical terms).

**warning**: Repetition penalty can severely degrade output quality on tasks that require consistent use of specific terminology — applying a penalty to all repeated tokens will suppress repeated technical terms, proper nouns, or task-required phrases; the distinction between undesirable verbatim repetition and legitimate contextually necessary repetition cannot be made by simple count-based penalties and requires more sophisticated generation constraints.

## Classifier-Free Guidance for Text

- secondary_domains: [llm-inference, controlled-generation, diffusion-analogies]
- aliases: [CFG for text, text classifier-free guidance, language model CFG]
- broader: [llm-decoding, controlled-text-generation]
- narrower: []
- related: [contrastive-decoding, logit-bias-manipulation, temperature-sampling, top-p-nucleus-sampling]
- prerequisites: [language-model-inference, classifier-free-guidance, logit-arithmetic]
- confidence: high

**definition**: Classifier-free guidance (CFG) for text is an inference technique that adapts the image diffusion CFG method to autoregressive language models by computing a weighted combination of conditional and unconditional next-token distributions. At each generation step, the model produces a conditional distribution p(token | prompt, condition) and an unconditional distribution p(token | condition_removed), and the final sampling distribution is constructed as: logits_final = logits_unconditional + guidance_scale × (logits_conditional − logits_unconditional). This amplifies the influence of the conditioning signal, steering generation more strongly toward the desired attribute or instruction.

**key_claim**: CFG for text provides a computationally efficient mechanism for amplifying the influence of conditioning information beyond what standard sampling achieves, producing outputs that are more strongly consistent with the specified condition at the cost of slightly reduced fluency at high guidance scales — it is particularly effective when the condition is expressed in a format (e.g., a system prompt or class label) where the unconditional model can naturally represent the counterfactual.

**warning**: CFG for text requires two forward passes per generation step (conditional and unconditional), doubling inference cost, and the guidance scale is highly sensitive — low values produce little effect while high values amplify artefacts and cause repetitive or incoherent outputs; the unconditional distribution is also ambiguous in open-ended LLM contexts where the notion of "no condition" is not well-defined.

## Logit Bias Manipulation

- secondary_domains: [llm-inference, controlled-generation, prompt-engineering]
- aliases: [logit bias, token bias injection, token suppression, logit adjustment]
- broader: [llm-decoding, inference-quality-control]
- narrower: []
- related: [repetition-penalty, temperature-sampling, classifier-free-guidance-for-text, structured-output-enforcement]
- prerequisites: [language-model-inference, softmax-function, token-generation]
- confidence: high

**definition**: Logit bias manipulation is a technique for controlling the token distribution of a language model at inference time by directly adding a fixed scalar value to the logit of specific tokens before the softmax is applied, increasing or decreasing their probability of being sampled. An additive logit bias of +100 effectively forces the token to always be sampled (near-certain selection), while a bias of -100 effectively suppresses it to near-zero probability. OpenAI's API and many open-source serving frameworks expose logit bias as a mapping from token IDs to scalar adjustments, enabling fine-grained control over the vocabulary without retraining.

**key_claim**: Logit bias manipulation is the lowest-level practical control mechanism available at inference time and is particularly useful for hard constraints that must be enforced absolutely — constraining the model to use specific formatting tokens, suppressing specific vocabulary items (e.g., explicit words or competitor brand names), or forcing the model to produce a specific sequence of tokens; these absolute constraints cannot be achieved reliably through prompt engineering alone.

**warning**: Logit bias manipulation interacts unpredictably with model coherence — suppressing a token does not teach the model to avoid the corresponding concept, it only removes that token from the output, so the model may substitute semantically equivalent tokens or produce incoherent text when its natural completion involves the suppressed token; it is a post-hoc output filter rather than a mechanism for changing the model's underlying generation strategy.
