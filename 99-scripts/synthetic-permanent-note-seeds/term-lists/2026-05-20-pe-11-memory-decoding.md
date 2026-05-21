---
batch_name: pe-11-memory-decoding
batch_date: 2026-05-20
default_domain: llm-memory
default_confidence: high
notes: |
  Nineteen concepts across two clusters: LLM memory systems and long-context
  management (nine terms), and decoding and sampling strategies (ten terms).
  The memory section covers the types of memory architecture available to LLM-
  based agents (episodic memory, external augmentation, MANNs, compressive
  memory, working memory proxies), the challenges of long-context use (needle
  in a haystack evaluation, long-context prompting strategies, summarisation as
  compression), and the concept of context distillation. The decoding section
  covers the full range of sampling strategies (temperature, top-p, top-k,
  min-p, beam search, best-of-n) and post-hoc quality mechanisms (repetition
  penalty, frequency penalty, contrastive decoding, speculative sampling).
---

# Batch: PE-11 Memory Systems, Long Context, and Decoding

## Episodic Memory in Agents

- domain: llm-memory
- secondary_domains: [ai-agents, cognitive-science, prompt-engineering]
- aliases: [agent episodic memory, LLM episodic memory, event-based agent memory]
- broader: [external-memory-augmentation, llm-memory]
- narrower: []
- related: [external-memory-augmentation, working-memory-proxies-in-llms, memory-augmented-neural-networks, long-context-prompting-strategies, retrieval-augmented-generation]
- prerequisites: [ai-agents, in-context-learning, retrieval-augmented-generation]
- confidence: high

**definition**: Episodic Memory in Agents refers to the capability of LLM-based agents to retain and retrieve memories of specific past interactions, events, or experiences — distinct from semantic (factual) memory stored in model weights and from working memory (the current context window). Episodic memory is typically implemented by storing interaction records in an external database (vector store, key-value store, or structured database), encoding them as retrievable memories, and injecting relevant past episodes into the agent's context when they are semantically relevant to the current query. This enables the agent to personalise responses based on conversation history, learn from past mistakes, and maintain coherent long-term task state.

**key_claim**: Episodic memory is the foundational architectural element that separates stateless LLM assistants from genuinely intelligent agents — without a mechanism for persistent experience storage and retrieval, an agent cannot improve from past interactions, cannot maintain coherent relationships with users over time, and cannot execute tasks that require referencing events that occurred beyond the current context window.

**warning**: Episodic memory retrieval introduces a selection problem — the agent must decide which past episodes are relevant to the current context, and poor retrieval can inject irrelevant or misleading memories that degrade performance, making the quality of the episodic memory retrieval system as important as the memory storage itself.

## External Memory Augmentation

- domain: llm-memory
- secondary_domains: [ai-agents, retrieval-augmented-generation, llm-architecture]
- aliases: [external memory, memory augmented LLMs, retrieval memory augmentation]
- broader: [llm-memory, retrieval-augmented-generation]
- narrower: [episodic-memory-in-agents]
- related: [episodic-memory-in-agents, memory-augmented-neural-networks, retrieval-augmented-generation, long-context-prompting-strategies]
- prerequisites: [retrieval-augmented-generation, ai-agents]
- confidence: high

**definition**: External Memory Augmentation refers to the architectural pattern of supplementing a language model's in-context and parametric memory with one or more external memory stores that can be read from and written to during inference. External memory can take several forms: vector databases (semantic memories retrieved by embedding similarity), key-value stores (structured memories retrieved by exact or fuzzy key lookup), relational databases (structured facts queried by SQL), and document stores (retrieved by full-text or hybrid search). The model interacts with external memory through tool calls or retrieval operations that inject relevant memory content into the context.

**key_claim**: External memory augmentation is the primary practical mechanism for giving language models effective unlimited memory — because the context window imposes a hard limit on how much information can be directly attended to, external memory allows the effective information space of an agent to be arbitrarily large while keeping the active context focused on the most relevant subset.

**warning**: External memory augmentation creates a new failure mode — memory poisoning and memory staleness — where incorrect, outdated, or adversarially crafted memories can be retrieved and influence agent behaviour in ways that are difficult to detect, because the agent has no internal mechanism to distinguish the trustworthiness of retrieved memories from trustworthy in-context information.

## Memory-Augmented Neural Networks

- domain: llm-memory
- secondary_domains: [machine-learning, cognitive-science, neural-networks]
- aliases: [MANNs, differentiable memory, neural memory architectures, NTMs]
- broader: [llm-memory, neural-networks]
- narrower: []
- related: [external-memory-augmentation, episodic-memory-in-agents, compressive-memory-mechanisms, recurrent-neural-networks]
- prerequisites: [neural-networks, attention-mechanism, recurrent-neural-networks]
- confidence: high

**definition**: Memory-Augmented Neural Networks (MANNs) are a class of neural network architectures that couple a neural computation module with an explicit, addressable external memory store that can be read from and written to through differentiable operations — allowing the model to learn what to store and retrieve as part of end-to-end training. Pioneer architectures include Neural Turing Machines (NTMs), Differentiable Neural Computers (DNCs), and Memory Networks. In the modern LLM context, MANNs are relevant as a theoretical foundation for understanding how transformer attention acts as a form of implicit memory, and as an architectural inspiration for external memory systems used in production agents.

**key_claim**: Memory-augmented neural networks established the theoretical principle that external, differentiable memory can be integrated with neural computation to enable tasks requiring long-range information retention and structured data manipulation — tasks that recurrent networks failed on due to gradient vanishing, and that transformers can only handle within their fixed context window.

**warning**: Pure MANN architectures did not scale to the sizes required for language modelling, and transformer self-attention effectively replaced them as a practical mechanism for within-context memory — but the conceptual distinction between the computation module and the memory store remains architecturally relevant for modern LLM-agent designs that combine transformer models with external retrieval systems.

## Compressive Memory Mechanisms

- domain: llm-memory
- secondary_domains: [llm-architecture, long-context-llms, cognitive-science]
- aliases: [memory compression, context compression, compressive transformers]
- broader: [llm-memory, long-context-llms]
- narrower: []
- related: [long-context-prompting-strategies, summarization-as-compression, context-distillation, memory-augmented-neural-networks]
- prerequisites: [transformer-attention-mechanism, long-context-llms, llm-memory]
- confidence: high

**definition**: Compressive Memory Mechanisms are architectures and techniques that compress older or less relevant context into more compact representations to extend effective memory capacity beyond the context window, rather than simply discarding old context. Examples include the Compressive Transformer, which compresses the oldest activations into a secondary memory with a lossy compression operation; H2O (Heavy Hitter Oracle), which selectively retains attention heads that have contributed most to previous predictions; MemGPT, which manages a hierarchical memory system with explicit compression and promotion operations; and various recurrent summarisation approaches that distil older context into summary tokens.

**key_claim**: Compressive memory mechanisms demonstrate that the choice between exact recall and capacity is not binary — by selectively compressing information based on its predicted relevance to future queries, it is possible to retain substantially more historical context than the raw context window allows while incurring smaller degradation in recall quality than simple truncation.

**warning**: Compressive memory mechanisms introduce a lossy compression step that can produce catastrophic retrieval failures on long-range dependencies — information that appears low-priority at compression time may be critical for a query that occurs much later, and the challenge of predicting what will be relevant in the future remains unsolved, making compressive approaches less reliable than full-context attention for tasks with unpredictable long-range dependencies.

## Long-Context Prompting Strategies

- domain: llm-memory
- secondary_domains: [prompt-engineering, long-context-llms]
- aliases: [long document prompting, extended context prompting, large context prompting strategies]
- broader: [prompt-engineering, long-context-llms]
- narrower: []
- related: [needle-in-a-haystack-evaluation, context-distillation, summarization-as-compression, retrieval-augmented-generation, episodic-memory-in-agents]
- prerequisites: [prompt-engineering, long-context-llms]
- confidence: high

**definition**: Long-Context Prompting Strategies are the collection of techniques for effectively using language models with large context windows — models that support 32K to 1M+ tokens — in ways that maximise recall of relevant information and minimise the degradation in attention quality that occurs when context is extremely long. Key strategies include: placing the most critical information at the beginning or end of the context (exploiting primacy and recency effects); using explicit section markers and hierarchical headings to aid navigation; summarising background context before appending verbatim source material; using retrieval-augmented approaches to pre-select relevant context rather than loading everything; and including explicit instructions to attend to specific sections.

**key_claim**: Long-context models exhibit a "lost in the middle" effect — they recall information near the beginning and end of the context reliably but show significantly degraded recall for information placed in the middle of very long contexts — making context organisation a critical prompt engineering variable that determines whether long-context capability translates to long-context performance in practice.

**warning**: The availability of large context windows can create a false sense of security — loading all available information into a context window without curation is not equivalent to the model having processed that information meaningfully, because attention dilutes and recall degrades with context length, and a well-curated shorter prompt can outperform an uncurated long prompt on most tasks.

## Needle in a Haystack Evaluation

- domain: llm-memory
- secondary_domains: [llm-evaluation, long-context-llms, benchmark-design]
- aliases: [NIAH, NIAH benchmark, long-context recall evaluation, pressure test]
- broader: [llm-evaluation, long-context-llms]
- narrower: []
- related: [long-context-prompting-strategies, context-distillation, lm-evaluation-harness, benchmark-design]
- prerequisites: [long-context-llms, llm-evaluation]
- confidence: high

**definition**: Needle in a Haystack (NIAH) Evaluation is a methodology for testing a language model's recall ability across its full context length by embedding a specific piece of information (the "needle") at different positions within a large, otherwise irrelevant document (the "haystack") and then querying for that information. The evaluation produces a two-dimensional recall heatmap showing model accuracy as a function of both total context length and needle position within the context. NIAH tests are widely used as a diagnostic for long-context capability and have revealed characteristic failure patterns such as the "lost in the middle" effect, where recall degrades for information in the middle of very long contexts.

**key_claim**: NIAH evaluation revealed that a model's advertised maximum context length is not an accurate indicator of its practical recall ability across that context — models that claim 128K context can show dramatic recall failures at 64K tokens for needles placed in the middle of the context, demonstrating a systematic gap between context capacity and context comprehension that had not been captured by prior benchmarks.

**warning**: NIAH evaluates only verbatim or near-verbatim retrieval of a specific fact and does not measure the ability to reason over, synthesise, or integrate information from across a long context — a model that scores well on NIAH may still struggle on tasks requiring multi-hop reasoning across a long document, so NIAH is a necessary but not sufficient benchmark for long-context utility.

## Context Distillation

- domain: llm-memory
- secondary_domains: [prompt-engineering, knowledge-distillation, llm-fine-tuning]
- aliases: [prompt distillation, context compression via distillation, system prompt distillation]
- broader: [knowledge-distillation, long-context-prompting-strategies]
- narrower: []
- related: [long-context-prompting-strategies, summarization-as-compression, compressive-memory-mechanisms, knowledge-distillation, few-shot-prompting]
- prerequisites: [knowledge-distillation, prompt-engineering]
- confidence: high

**definition**: Context Distillation is the process of training a language model to internalise the knowledge or behavioural guidelines contained in a long prompt — such as a detailed system prompt, a set of few-shot examples, or a rules document — so that the model exhibits those behaviours without requiring the prompt to be included at inference time. The distillation procedure involves generating training examples using the full prompt and then fine-tuning the model on those examples without the prompt, teaching the model to reproduce the prompt-conditioned behaviour from its weights alone. This reduces inference cost and latency while preserving the behavioural benefits of the original prompt.

**key_claim**: Context distillation is the mechanism by which the knowledge in prompt engineering can be converted into parametric model improvements — it provides a principled path from "the right prompt makes this model behave correctly" to "the model behaves correctly without the prompt", making it a key technique for deploying refined prompt-derived behaviours at scale without per-request prompt overhead.

**warning**: Context distillation can inadvertently encode the distribution-specific biases of the examples used for distillation — if the training examples generated under the full prompt represent a narrow distribution, the distilled model may fail to generalise the desired behaviour to prompts that differ from the distillation distribution, reproducing the failure modes of narrow fine-tuning rather than the generalisation benefits of the original prompt.

## Summarisation as Compression

- domain: llm-memory
- secondary_domains: [natural-language-generation, prompt-engineering, long-context-llms]
- aliases: [summarisation for context compression, recursive summarisation, context summarisation]
- broader: [compressive-memory-mechanisms, long-context-prompting-strategies]
- narrower: []
- related: [compressive-memory-mechanisms, context-distillation, long-context-prompting-strategies, chain-of-density-summarization]
- prerequisites: [natural-language-generation, long-context-prompting-strategies]
- confidence: high

**definition**: Summarisation as Compression is the technique of using a language model to produce compact summaries of earlier context segments — conversation history, document sections, or prior reasoning chains — as a mechanism for extending effective context length beyond the model's window limit. In practice, this is implemented through rolling summarisation (periodically summarising the oldest portion of the context to free space for new information), hierarchical summarisation (summarising increasingly coarser chunks to produce a multi-level memory representation), or query-specific compression (summarising context to retain only information relevant to the current query).

**key_claim**: Summarisation as compression enables persistent agents to maintain coherent conversation history and task state across arbitrarily long interactions — the lossy nature of summarisation is acceptable for most conversational contexts because the compressed summary retains the semantically important events while discarding verbatim details, preserving conversational coherence at the cost of precise recall.

**warning**: Summarisation as compression introduces an irreversible information loss — once context is summarised, the original details are gone, and if the summary omits information that becomes relevant later in the interaction, that information is unrecoverable without reprocessing the original source, making the timing and granularity of summarisation decisions critical for high-stakes applications.

## Working Memory Proxies in LLMs

- domain: llm-memory
- secondary_domains: [cognitive-science, prompt-engineering, ai-agents]
- aliases: [working memory simulation, scratchpad memory, chain-of-thought as working memory]
- broader: [llm-memory, cognitive-science-foundations]
- narrower: []
- related: [episodic-memory-in-agents, external-memory-augmentation, chain-of-thought-prompting, working-memory-constraints-in-prompts]
- prerequisites: [cognitive-science, llm-memory, chain-of-thought-prompting]
- confidence: high

**definition**: Working Memory Proxies in LLMs refers to the mechanisms by which language models simulate working memory — the cognitive system responsible for temporary information maintenance and manipulation during complex reasoning — using the context window rather than a dedicated neurological architecture. Chain-of-thought reasoning acts as an explicit working memory proxy by externalising intermediate computation steps into the context, where they persist and can be referenced by subsequent reasoning steps. Scratchpads, explicit note-taking instructions, and structured reasoning formats serve similar functions, allowing models to maintain state across complex multi-step operations that would fail if only relying on implicit in-weights computation.

**key_claim**: Chain-of-thought prompting works primarily through its function as a working memory proxy — by externalising intermediate reasoning steps into the context window, it converts tasks that require maintaining multiple active constraints in parallel (which the model cannot do reliably in a single forward pass) into sequential token generation where each step can attend to all prior steps, effectively converting a working-memory-limited single-step task into a working-memory-unlimited sequential task.

**warning**: Working memory proxies in LLMs are limited by the quality of the model's self-monitoring — a model that makes an error in an intermediate reasoning step will build subsequent steps on that error, producing a reasoning chain where confidence accumulates on a faulty foundation; unlike human working memory, the model has no metacognitive mechanism to flag that an intermediate step is likely wrong.

## Temperature Sampling

- domain: llm-decoding
- secondary_domains: [llm-generation, prompt-engineering, information-theory]
- aliases: [temperature parameter, sampling temperature, generation temperature]
- broader: [llm-decoding]
- narrower: []
- related: [top-p-nucleus-sampling, top-k-sampling, min-p-sampling, greedy-decoding, llm-generation]
- prerequisites: [llm-decoding, probability-theory]
- confidence: high

**definition**: Temperature Sampling is a decoding parameter that controls the sharpness of the probability distribution from which the next token is sampled by dividing the model's logits by the temperature value before applying the softmax function. A temperature of 1.0 leaves the model's learned probabilities unchanged. Temperatures below 1.0 sharpen the distribution, making it more deterministic and concentrated on high-probability tokens — reducing diversity and increasing consistency. Temperatures above 1.0 flatten the distribution, increasing the probability of low-probability tokens — increasing diversity and creativity at the cost of coherence.

**key_claim**: Temperature is the most intuitive and universally applicable decoding parameter — it directly controls the exploration-exploitation tradeoff in generation, allowing the same model to be configured for deterministic, reproducible outputs (low temperature, near-zero) for factual tasks and for creative, diverse outputs (higher temperature) for generative tasks, without changing any other system component.

**warning**: Temperature interacts non-linearly with the model's calibration — a model that is overconfident in its wrong predictions will produce even more overconfident wrong predictions at low temperatures, while a model that is underconfident in its correct predictions will produce incoherent outputs at high temperatures, meaning that the optimal temperature is model-specific and task-specific and cannot be determined without empirical evaluation.

## Top-P Nucleus Sampling

- domain: llm-decoding
- secondary_domains: [llm-generation, prompt-engineering]
- aliases: [nucleus sampling, top-p sampling, cumulative probability sampling]
- broader: [llm-decoding]
- narrower: []
- related: [temperature-sampling, top-k-sampling, min-p-sampling, llm-generation]
- prerequisites: [llm-decoding, probability-theory, temperature-sampling]
- confidence: high

**definition**: Top-P Nucleus Sampling (Holtzman et al., 2020) is a decoding strategy that at each token generation step considers only the smallest set of tokens whose cumulative probability mass exceeds a threshold p, and samples from that set with probabilities renormalised to sum to 1. Unlike top-k which always uses the same number of candidates, top-p dynamically adjusts the candidate set size based on the distribution shape — when the model is highly confident, the nucleus may contain only 1–2 tokens; when the model is uncertain, the nucleus may contain hundreds of tokens. This adaptive behaviour produces more coherent text than fixed top-k by avoiding forced sampling from very low-probability tokens when a confident prediction exists.

**key_claim**: Top-p sampling improves generation quality over top-k by adapting the vocabulary truncation to the model's confidence at each step — when the model has a strong preference (peaky distribution), top-p respects that preference by using a small candidate set, while top-k would force sampling from many low-probability alternatives, introducing incoherence.

**warning**: Top-p and temperature are typically both applied in production systems, and they interact — a high temperature flattens the distribution (making the nucleus larger) while a low temperature sharpens it (making the nucleus smaller), so the effective behaviour of top-p depends on the temperature setting, and setting them independently without considering their interaction can produce unexpected generation characteristics.

## Top-K Sampling

- domain: llm-decoding
- secondary_domains: [llm-generation, prompt-engineering]
- aliases: [k-sampling, top-k decoding, k-best sampling]
- broader: [llm-decoding]
- narrower: []
- related: [temperature-sampling, top-p-nucleus-sampling, min-p-sampling, greedy-decoding]
- prerequisites: [llm-decoding, probability-theory]
- confidence: high

**definition**: Top-K Sampling is a decoding strategy that restricts the vocabulary of candidate tokens at each generation step to the K most probable tokens according to the model's distribution, then samples from these K tokens with probabilities renormalised to sum to 1. All tokens outside the top K are assigned zero probability. The parameter K is a fixed integer — typically values between 10 and 100 for natural language generation. Top-K was widely used before nucleus sampling became standard, and is still used in combination with temperature and top-p in many production configurations.

**key_claim**: Top-K sampling prevents the generation of clearly low-probability, incoherent tokens (which pure temperature sampling allows) by enforcing a hard cutoff below which tokens are never selected — but its fixed cardinality is a weakness, because an appropriate vocabulary size varies substantially across generation contexts, and a fixed K is simultaneously too small in uncertain contexts (cutting off reasonable alternatives) and too large in confident contexts (allowing poor alternatives).

**warning**: Top-K sampling with a small K value in combination with low temperature can cause mode collapse in long-form generation — the interaction between a small candidate set and high probability concentration can create degenerate repetitive loops where the most probable token at each step leads back to tokens seen recently, producing repetitive or circular text.

## Beam Search Decoding

- domain: llm-decoding
- secondary_domains: [natural-language-generation, sequence-to-sequence-models]
- aliases: [beam search, beam decoding, breadth-first decoding]
- broader: [llm-decoding]
- narrower: [constrained-beam-search]
- related: [temperature-sampling, top-p-nucleus-sampling, best-of-n-sampling, constrained-beam-search, greedy-decoding]
- prerequisites: [llm-decoding, dynamic-programming]
- confidence: high

**definition**: Beam Search Decoding is a deterministic decoding algorithm that maintains a beam of the B most probable partial sequences at each generation step, expanding each by all possible next tokens, and pruning back to the top-B sequences by cumulative log-probability. By simultaneously tracking multiple high-probability hypotheses, beam search produces more globally coherent sequences than greedy decoding (which commits irrevocably to the highest probability token at each step) — particularly for tasks with a strong correct answer structure, such as translation, summarisation, and code generation.

**key_claim**: Beam search is the appropriate decoding strategy for sequence-to-sequence tasks where the output has a well-defined correct answer and global coherence matters more than diversity — translation and code generation benefit from beam search's ability to recover from locally suboptimal token choices, while open-ended text generation is better served by sampling methods that avoid the repetitive, safe outputs that beam search tends to produce.

**warning**: Beam search exhibits a well-documented failure mode for open-ended generation — it produces bland, repetitive, and high-probability text because it systematically prefers safe completions that have been seen frequently in training data, a problem that became visible at scale and was a key motivation for the development of sampling-based decoding strategies.

## Min-P Sampling

- domain: llm-decoding
- secondary_domains: [llm-generation, prompt-engineering]
- aliases: [minimum probability sampling, min-p decoding]
- broader: [llm-decoding]
- narrower: []
- related: [temperature-sampling, top-p-nucleus-sampling, top-k-sampling, llm-generation]
- prerequisites: [llm-decoding, top-p-nucleus-sampling, temperature-sampling]
- confidence: high

**definition**: Min-P Sampling is a decoding strategy that filters the vocabulary by removing any tokens whose probability falls below a fraction p_min of the probability of the highest-probability token. Rather than using an absolute threshold (top-k) or a cumulative probability cutoff (top-p), min-p uses a relative threshold that scales with the model's confidence — when the most likely token has probability 0.9, tokens with probability below 0.09 (p_min=0.1) are excluded; when the distribution is flat and the most likely token has probability 0.05, the cutoff is 0.005. This produces a nucleus that scales dynamically with the model's confidence state.

**key_claim**: Min-P sampling provides better quality-diversity tradeoffs than top-p at higher temperatures by more aggressively filtering incoherent low-probability tokens while preserving genuine alternatives — at high temperatures where top-p's nucleus becomes very large and includes many garbage tokens, min-p's relative threshold continues to exclude tokens that are far below the best option, maintaining generation quality in creative or exploratory modes.

**warning**: Min-P is sensitive to the specific value of p_min in a way that differs from top-p's sensitivity to p — because min-p sets a relative threshold, small changes to p_min can dramatically change the effective vocabulary size when the model's confidence distribution is multimodal, making it require more careful calibration than top-p in some generation regimes.

## Repetition Penalty

- domain: llm-decoding
- secondary_domains: [llm-generation, natural-language-generation, prompt-engineering]
- aliases: [repeat penalty, anti-repetition penalty, repetition suppression]
- broader: [llm-decoding]
- narrower: []
- related: [frequency-penalty-effects, temperature-sampling, top-p-nucleus-sampling, llm-generation]
- prerequisites: [llm-decoding]
- confidence: high

**definition**: Repetition Penalty is a post-processing modification to token logits that reduces the probability of tokens that have already appeared in the current generation context, discouraging the model from repeating the same words, phrases, or patterns within a single output. Implemented as a multiplicative penalty applied to logits of previously seen tokens (logits are divided by the penalty factor if they are positive and multiplied if they are negative), repetition penalty directly reduces the frequency with which the model loops or produces repetitive filler. The penalty can apply uniformly to all tokens in the context or can decay with distance from the current position.

**key_claim**: Repetition penalty addresses a failure mode that is most severe in small or quantised models — the tendency to loop into repetitive phrases or sentences when the model's probability distribution collapses onto a small set of high-frequency tokens — but at high penalty values it suppresses legitimate repetition (e.g., proper nouns, technical terms that must recur) and can degrade coherence by forcing the model to avoid necessary referential repetition.

**warning**: Repetition penalty and temperature interact — a high repetition penalty with high temperature can produce incoherent text that avoids repetition by choosing increasingly improbable diverse tokens, while a high repetition penalty with low temperature can cause the model to terminate early or become stuck when all plausible continuations involve tokens already used, so the two parameters should be tuned jointly.

## Frequency Penalty Effects

- domain: llm-decoding
- secondary_domains: [llm-generation, prompt-engineering, openai-api]
- aliases: [frequency penalty, presence penalty, diversity penalty]
- broader: [llm-decoding]
- narrower: []
- related: [repetition-penalty, temperature-sampling, top-p-nucleus-sampling]
- prerequisites: [llm-decoding, repetition-penalty]
- confidence: high

**definition**: Frequency Penalty is a decoding modifier (used in the OpenAI API and similar systems) that applies a negative reward to tokens proportional to how many times they have already appeared in the generated output — the more times a token has appeared, the more its probability is reduced for future generation. Unlike repetition penalty (which applies a fixed multiplicative penalty to any repeated token regardless of frequency), frequency penalty applies an additive penalty that scales linearly with count, progressively discouraging the model from using tokens it has already used many times. Presence penalty is a related parameter that applies a fixed penalty for any token that has appeared at least once, regardless of frequency.

**key_claim**: Frequency penalty and presence penalty serve different text diversity objectives: frequency penalty primarily reduces the overuse of high-frequency words (articles, conjunctions, specific domain terms used repeatedly), producing more lexically varied text; presence penalty primarily encourages topic diversity by discouraging the model from returning to any concept already mentioned, which can be counterproductive for focused analytical writing where topic consistency is desirable.

**warning**: Frequency penalty can produce unnatural text when applied to content that inherently requires repetition — technical documentation that must repeatedly reference a technical term, legal text with mandatory boilerplate, or multi-step instructions that must refer to the same object at each step are all degraded by high frequency penalties, making it a generation-diversity tool that is inappropriate for precision writing tasks.

## Contrastive Decoding

- domain: llm-decoding
- secondary_domains: [llm-generation, llm-alignment, hallucination-reduction]
- aliases: [CD decoding, adaptive contrastive decoding, CAD]
- broader: [llm-decoding]
- narrower: []
- related: [temperature-sampling, top-p-nucleus-sampling, hallucination-reduction, speculative-sampling]
- prerequisites: [llm-decoding, hallucination-reduction]
- confidence: high

**definition**: Contrastive Decoding is a search objective for language model generation that produces text by maximising the difference in log-probability between a large expert model and a small amateur model evaluated on the same sequence. The intuition is that both models share similar content but differ in quality — the expert model assigns higher probability to coherent, factual text while the amateur model does not penalise as strongly for incoherence or hallucination, so the difference between their log-probabilities captures a "quality" signal that can guide generation toward more faithful outputs. Contrastive decoding has been shown to reduce factual hallucination and improve coherence in long-form generation.

**key_claim**: Contrastive decoding offers a principled way to improve generation faithfulness without fine-tuning by using the amateur model as a representation of low-quality generation patterns to avoid — the method exploits the assumption that errors and hallucinations are more probable under the amateur model, so subtracting amateur log-probabilities removes those patterns from the generation distribution.

**warning**: Contrastive decoding requires access to two models of different sizes during inference, doubling (or more) the computational cost compared to standard sampling — and the quality improvement is sensitive to how well the small model characterises the "bad" generation distribution, which varies across tasks and domains, making it an advanced technique with significant infrastructure and calibration requirements.

## Speculative Sampling

- domain: llm-decoding
- secondary_domains: [llm-inference-optimisation, llm-decoding]
- aliases: [speculative decoding, draft-then-verify, assisted decoding]
- broader: [llm-decoding, inference-optimisation]
- narrower: []
- related: [beam-search-decoding, temperature-sampling, llm-inference-optimisation, best-of-n-sampling]
- prerequisites: [llm-decoding, inference-optimisation]
- confidence: high

**definition**: Speculative Sampling (also called speculative decoding) is an inference acceleration technique that uses a small, fast draft model to propose a sequence of K candidate tokens, and then uses the large target model to evaluate all K tokens in a single parallel forward pass, accepting or rejecting each proposed token based on whether the target model's probability for that token exceeds the draft model's probability. Accepted tokens are kept; the first rejected token is resampled from the target distribution. Because transformer forward passes are often compute-bounded rather than bandwidth-bounded for small batch sizes, the parallel verification of K tokens is not much more expensive than verifying 1 token, while producing K tokens' worth of output.

**key_claim**: Speculative sampling provides 2–4× inference speedup with zero degradation in output quality — the key insight is that if the draft model's proposals are accepted, the target model's verification step is essentially free relative to generating K tokens sequentially, making speculative sampling practically appealing for latency-sensitive deployments without compromising the integrity of the target model's distribution.

**warning**: Speculative sampling's speedup depends on the draft model's acceptance rate — if the draft model's distribution diverges significantly from the target model's distribution, most tokens will be rejected, negating the speedup, so the choice of draft model (typically a 7B model drafting for a 70B target) requires careful alignment of training data and instruction-tuning distributions to maintain a high acceptance rate.

## Best-of-N Sampling

- domain: llm-decoding
- secondary_domains: [llm-generation, prompt-engineering, reinforcement-learning-from-human-feedback]
- aliases: [BoN sampling, best-of-n, rejection sampling, sample and select]
- broader: [llm-decoding, inference-scaling]
- narrower: []
- related: [temperature-sampling, speculative-sampling, process-reward-models, outcome-reward-models, inference-scaling-laws]
- prerequisites: [llm-decoding, reward-model-design]
- confidence: high

**definition**: Best-of-N Sampling is a generation strategy in which the model generates N independent candidate completions for the same prompt, scores each candidate using an external reward model or verifier, and returns the highest-scoring candidate as the final output. It is the simplest form of inference-time scaling: by spending N times the compute at inference time to generate N candidates, the expected quality of the best candidate improves systematically as N increases. BoN sampling has been shown to be remarkably competitive with more expensive RL-based methods for certain tasks, and it is the reference strategy against which more sophisticated search methods are benchmarked.

**key_claim**: Best-of-N sampling demonstrates that inference-time compute is a powerful lever for improving output quality — for a wide range of tasks, spending N times the computation at inference time to sample and select among N candidates produces better results than spending N times the computation during training, because the selection step can target the specific query rather than the average of the training distribution.

**warning**: The effectiveness of best-of-n sampling depends entirely on the quality of the scoring function — if the verifier or reward model is imprecise, biased, or gameable, the selected "best" sample may be the one that best games the scorer rather than the one of highest actual quality, reproducing the reward hacking failure mode of RL training but at inference time.
