---
batch_name: b01-04-context-memory
batch_date: 2026-05-21
default_domain: llm-context-management
default_confidence: high
notes: |
  Context window and memory concepts covering context extension, long-context prompting,
  positional bias, recency effects, memory-augmented LLMs, and episodic/semantic/working
  memory analogies in language models.
---

# Batch: B01-04 Context and Memory

## Context Window Extension

- secondary_domains: [llm-architecture, positional-encoding, llm-training]
- aliases: [context length extension, long-context training, RoPE extension]
- broader: [transformer-architecture, llm-context-management]
- narrower: [rope-scaling, alibi-positional-encoding, yarn-extension]
- related: [long-context-prompting-strategies, positional-bias-in-context, needle-in-a-haystack-evaluation, retrieval-as-external-memory]
- prerequisites: [transformer-architecture, positional-encoding, rotary-position-embedding]
- confidence: high

**definition**: Context window extension refers to techniques for increasing the maximum token sequence length that a pretrained language model can process beyond its original training context length, without full retraining. Because standard transformer attention is computed over all positions in the context, the maximum context length is constrained by both computational cost (quadratic in sequence length) and positional encoding capacity (the model has not seen position encodings beyond its training length). Extension methods include: RoPE scaling variants (linear scaling, YaRN, LongRoPE), training on progressively longer sequences, and architectural modifications such as sliding window attention. Extended context models are needed for document-level reasoning, multi-document QA, and long conversation history.

**key_claim**: The naive assumption that models trained with context length N can be directly used at context length 2N by doubling the positional encoding scale is incorrect — performance typically degrades sharply beyond the training context length because the model has never seen positional relationships at those scales, and extension methods must carefully preserve the relative positional structure that the model learned during training while extrapolating to new lengths.

**warning**: Context window extension increases the maximum context length but does not uniformly improve retrieval from that context — models with extended context windows still exhibit the "lost in the middle" phenomenon where information in the middle of a long context is retrieved less accurately than information at the beginning or end; extended context window ≠ uniformly improved long-document understanding.

## Long-Context Prompting Strategies

- secondary_domains: [prompt-engineering, llm-context-management, rag]
- aliases: [long-context prompts, large-context prompting, extended context prompt design]
- broader: [prompt-engineering, llm-context-management]
- narrower: [map-reduce-prompting, hierarchical-summarisation-prompting]
- related: [context-window-extension, positional-bias-in-context, retrieval-as-external-memory, prompt-caching-strategies, needle-in-a-haystack-evaluation]
- prerequisites: [prompt-engineering, context-window-extension, large-language-models]
- confidence: high

**definition**: Long-context prompting strategies are techniques for effectively structuring and decomposing inputs when the source material exceeds or approaches the model's practical effective context length. Approaches include: placing the most query-relevant content at the beginning or end of the context (exploiting positional attention bias), hierarchical summarisation (summarise chunks then summarise summaries), map-reduce patterns (process segments independently then aggregate), retrieval-augmented generation (retrieve only the most relevant excerpts), and instruction placement strategies that place task instructions at both the start and end of long contexts. These strategies compensate for the degradation in retrieval accuracy observed in the middle of very long contexts.

**key_claim**: The placement of information within a long context has a predictable and large effect on retrieval accuracy — Liu et al.'s "lost in the middle" finding shows that information at the start and end of a context is retrieved far more reliably than identical information placed in the middle, making prompt position a critical engineering consideration for any retrieval or document-grounded QA task.

**warning**: Long-context prompting strategies that chunk and independently process document segments risk missing relationships that span chunk boundaries — a question whose answer requires connecting information from non-adjacent chunks will be incorrectly answered by independent chunk-processing approaches; overlap-based chunking and cross-chunk aggregation strategies add complexity without fully solving this problem.

## Needle in a Haystack Evaluation

- secondary_domains: [llm-evaluation, long-context-testing, retrieval-benchmarking]
- aliases: [NIAH, needle-in-haystack, passkey retrieval evaluation]
- broader: [llm-evaluation, context-window-evaluation]
- narrower: []
- related: [context-window-extension, long-context-prompting-strategies, positional-bias-in-context, recency-bias-in-llms]
- prerequisites: [llm-evaluation, context-window-extension, information-retrieval]
- confidence: high

**definition**: Needle in a Haystack (NIAH) evaluation is a benchmark methodology for assessing a language model's ability to retrieve a specific piece of information ("the needle") embedded at various positions within a long filler context ("the haystack"). The task typically embeds a single unique factual statement at a controlled position in a long document of semantically related but unrelated content, then asks the model a question whose answer requires recalling the needle. By varying both the position of the needle (beginning, middle, end) and the total length of the context, NIAH produces a two-dimensional performance map that reveals where and at what lengths the model's retrieval degrades.

**key_claim**: NIAH evaluation consistently reveals that long-context model performance is not uniform across context positions — all current large language models show characteristic retrieval degradation patterns, typically with the middle of long contexts being most vulnerable, demonstrating that raw context window length is a poor proxy for effective context utilisation and that position-aware evaluation is necessary.

**warning**: NIAH evaluates a highly simplified form of long-context retrieval — real document understanding tasks require integrating multiple distributed pieces of information, resolving coreference, and performing reasoning over retrieved facts, none of which are assessed by single-needle retrieval; strong NIAH performance does not imply strong multi-hop long-context reasoning.

## Positional Bias in Context

- secondary_domains: [llm-evaluation, cognitive-biases-in-ai, llm-context-management]
- aliases: [position bias, primacy-recency effect in LLMs, lost-in-the-middle effect]
- broader: [llm-context-management, context-window-evaluation]
- narrower: [lost-in-the-middle-effect, primacy-bias-in-llms, recency-bias-in-llms]
- related: [needle-in-a-haystack-evaluation, recency-bias-in-llms, long-context-prompting-strategies, context-window-extension]
- prerequisites: [transformer-architecture, positional-encoding, attention-mechanism]
- confidence: high

**definition**: Positional bias in context refers to the systematic tendency of transformer-based language models to assign different importance to information based on its position within the input context, independent of its semantic content or relevance. The most documented variant is the "lost in the middle" phenomenon in which information placed at the beginning (primacy bias) or end (recency bias) of a long context is retrieved significantly more accurately than information in the middle of the context. This bias emerges from the interaction of causal attention patterns, positional encodings, and the training distribution, which typically contains documents where important information appears at the start.

**key_claim**: Positional bias in context is not a surface-level deficiency that can be corrected purely through architectural improvements — it reflects a deep statistical regularisation learned from training data in which document structure correlates with information importance, making it a feature of how the model represents relevance rather than a bug in position encoding; prompt engineering strategies that exploit known positional biases are therefore more reliable than assuming bias-free retrieval.

**warning**: Positional bias interacts with context length non-linearly — models with extended context windows may show different positional bias profiles than the same model at its native context length, and the bias pattern can shift depending on the domain and document structure of the input; evaluating positional bias only at the model's native context length provides an incomplete picture of its long-context behaviour.

## Recency Bias in LLMs

- secondary_domains: [llm-evaluation, cognitive-biases-in-ai, conversational-ai]
- aliases: [recency effect in LLMs, serial-position recency, tail-end attention bias]
- broader: [positional-bias-in-context, llm-context-management]
- narrower: []
- related: [positional-bias-in-context, needle-in-a-haystack-evaluation, long-context-prompting-strategies, context-window-extension]
- prerequisites: [positional-bias-in-context, transformer-architecture, conversational-llms]
- confidence: high

**definition**: Recency bias in language models refers to the phenomenon in which LLMs disproportionately weight recent tokens in the context window when generating responses — information appearing closer to the end of the input receives more attention and has greater influence on the output than semantically equivalent information earlier in the context. Recency bias is most prominent in conversational settings where later turns in a conversation override earlier facts or instructions, in multi-document settings where the last document has disproportionate influence, and in chain-of-thought reasoning where later reasoning steps may contradict but override earlier valid conclusions.

**key_claim**: Recency bias in autoregressive models is partially structural — the causal attention mechanism and left-to-right generation mean the most recent tokens have the most direct access to the generation distribution, making some degree of recency effect an expected consequence of the architecture; however, the degree of recency bias exceeds what the architecture alone predicts and is amplified by training data structure, where conclusions typically follow premises.

**warning**: Recency bias in multi-turn conversations creates a specific security and reliability failure mode — a malicious later message can effectively override correct earlier instructions or facts by exploiting the model's tendency to prioritise recent context, making instruction-following and factual grounding less reliable in long conversations than in single-turn interactions.

## Memory-Augmented LLMs

- secondary_domains: [llm-architecture, ai-agents, knowledge-management]
- aliases: [memory-augmented language models, external memory LLMs, long-term memory LLMs]
- broader: [llm-context-management, ai-agents]
- narrower: [retrieval-augmented-generation, episodic-memory-in-agents, working-memory-simulation-in-llms]
- related: [retrieval-as-external-memory, episodic-memory-in-agents, semantic-memory-in-agents, working-memory-simulation-in-llms, retrieval-augmented-generation]
- prerequisites: [large-language-models, retrieval-augmented-generation, vector-databases]
- confidence: high

**definition**: Memory-augmented LLMs are language model systems that extend the model's effective information storage and retrieval beyond the finite context window by integrating external memory mechanisms — typically vector stores, key-value databases, episodic buffers, or compressed summary states — that the model can read from and write to during inference. Memory augmentation architectures range from simple RAG (retrieve-then-generate) to more sophisticated systems with explicit episodic memory for conversation history, semantic memory for domain knowledge, and procedural memory for learned task strategies. The goal is to enable LLMs to maintain coherent, personalised, and factually grounded responses across sessions and documents that exceed any feasible context window.

**key_claim**: Memory augmentation addresses the fundamental statelessness of standard LLM inference — base LLMs have no persistent state between API calls, making them unsuitable for longitudinal tasks, personalised assistance, or multi-session projects without explicit memory systems; effective memory architecture is therefore not an optional enhancement but a prerequisite for LLM systems that must maintain task context across interactions.

**warning**: Memory augmentation introduces retrieval errors that compound with generation errors — a memory system that retrieves the wrong past fact will cause the model to generate a contextually incoherent response that may appear confident and fluent, creating a failure mode that is harder to detect than a simple knowledge gap; memory system design must include retrieval accuracy monitoring and explicit handling of low-confidence retrievals.

## Episodic Memory in Agents

- secondary_domains: [ai-agents, cognitive-architecture, memory-systems]
- aliases: [episodic agent memory, event-based memory, experience replay in agents]
- broader: [memory-augmented-llms, ai-agents]
- narrower: []
- related: [semantic-memory-in-agents, working-memory-simulation-in-llms, memory-augmented-llms, retrieval-as-external-memory]
- prerequisites: [ai-agents, memory-augmented-llms, episodic-memory-in-cognitive-science]
- confidence: high

**definition**: Episodic memory in AI agents refers to the storage and retrieval of specific past experiences — individual interaction records, tool use episodes, task outcomes, and contextual facts — in a manner analogous to the episodic memory system in human cognition. In agent architectures, episodic memory is typically implemented as a vector store or structured log of timestamped experience tuples that the agent can query when faced with similar situations, enabling it to recall what it did before, how it succeeded or failed, and what context was relevant. Episodic memory enables agents to personalise responses, avoid repeating mistakes, and maintain long-running task state across multiple sessions.

**key_claim**: Episodic memory is the memory modality most directly responsible for agent personalisation and task continuity — without episodic memory, every agent interaction starts from the same blank state regardless of prior history, making the agent incapable of the kind of context-sensitive adaptation that human users expect from a productive AI assistant; the richness of an agent's episodic memory directly constrains the depth of the relational context it can maintain.

**warning**: Episodic memory systems face a storage and retrieval scalability problem — as the number of stored episodes grows, the noise in vector similarity retrieval increases and the latency of memory access grows, making naive approaches to episodic storage degrade gracefully rather than catastrophically; hierarchical summarisation of episodic memory (compressing old episodes into semantic summaries) is necessary at scale but introduces information loss.

## Semantic Memory in Agents

- secondary_domains: [ai-agents, knowledge-representation, memory-systems]
- aliases: [factual memory in agents, knowledge store, world model memory]
- broader: [memory-augmented-llms, ai-agents]
- narrower: []
- related: [episodic-memory-in-agents, working-memory-simulation-in-llms, memory-augmented-llms, retrieval-augmented-generation]
- prerequisites: [ai-agents, memory-augmented-llms, knowledge-representation]
- confidence: high

**definition**: Semantic memory in AI agents refers to the long-term storage of general world knowledge, domain facts, and learned relationships in a form that the agent can retrieve and reason over during task execution — analogous to the semantic memory system in human cognition that stores factual knowledge independent of the episodic context in which it was acquired. In agent implementations, semantic memory is typically encoded in structured knowledge bases, vector stores containing factual documents, or the model's own parametric weights, and is queried by similarity search or symbolic lookup when the agent needs domain-specific facts. Semantic memory is distinct from episodic memory (records of specific experiences) and working memory (current context).

**key_claim**: Semantic memory is the agent memory modality most analogous to RAG — both represent the store of retrievable world knowledge that grounds agent responses in facts rather than parametric hallucinations; the key distinction from episodic memory is that semantic memory stores decontextualised facts (e.g., "Python is a dynamically typed language") while episodic memory stores contextualised experiences (e.g., "when I debugged the user's Python script last session, the error was a type mismatch").

**warning**: The boundary between semantic and episodic memory in AI agents is blurrier than in the neuroscientific analogy — most practical agent implementations use a single unified vector store for both fact-type and experience-type memories, which conflates the retrieval characteristics (recency-weighted for episodic, relevance-weighted for semantic) and can cause retrieval to return outdated specific experiences when general facts are needed and vice versa.

## Working Memory Simulation in LLMs

- secondary_domains: [ai-agents, cognitive-architecture, llm-context-management]
- aliases: [working memory in LLMs, scratchpad memory, in-context working memory]
- broader: [memory-augmented-llms, llm-context-management]
- narrower: []
- related: [episodic-memory-in-agents, semantic-memory-in-agents, chain-of-thought-prompting, scratchpad-reasoning]
- prerequisites: [working-memory-in-cognitive-science, large-language-models, chain-of-thought-prompting]
- confidence: high

**definition**: Working memory simulation in LLMs refers to the use of the active context window — including chain-of-thought intermediate steps, scratchpad notation, and accumulated partial results — as a functional analogue to the human working memory system that temporarily holds and manipulates information during active reasoning. Unlike episodic or semantic memory which persist across turns, working memory is the space of currently active information that the model is operating on: the current task state, recent reasoning steps, and partial computations. Chain-of-thought prompting and scratchpad techniques explicitly leverage this working memory capacity by externalising intermediate reasoning steps into text, making them available for subsequent reasoning steps.

**key_claim**: Chain-of-thought prompting works precisely because it simulates working memory externalisation — by writing intermediate reasoning steps into the context, CoT prevents the model from having to maintain multiple reasoning states in its latent space simultaneously, transforming a hard working-memory-limited computation into a sequence of simpler, single-step operations that each fit within the model's effective working memory capacity.

**warning**: Working memory in LLMs is bounded by the context window and is not persistent — complex multi-step tasks that require accumulating state across many interaction turns quickly exhaust the available working memory space, and context window truncation discards old working memory content that may still be required; agent designs that rely on in-context working memory for long tasks must explicitly manage context through summarisation or external state storage.

## Retrieval as External Memory

- secondary_domains: [retrieval-augmented-generation, knowledge-management, llm-architecture]
- aliases: [retrieval-based memory, RAG as memory, external knowledge retrieval]
- broader: [memory-augmented-llms, retrieval-augmented-generation]
- narrower: []
- related: [retrieval-augmented-generation, episodic-memory-in-agents, semantic-memory-in-agents, memory-augmented-llms, context-window-extension]
- prerequisites: [retrieval-augmented-generation, vector-databases, dense-passage-retrieval]
- confidence: high

**definition**: Retrieval as external memory is the paradigm in which a language model's knowledge is extended at inference time by querying an external document store, knowledge base, or episodic memory repository and injecting retrieved content into the active context. Rather than relying on the parametric knowledge encoded in model weights during training — which is frozen, potentially outdated, and limited in scope — the model dynamically accesses relevant information from an external, updateable store. This architecture separates knowledge storage (external memory) from knowledge processing (model computation), enabling knowledge updates without retraining and scaling stored knowledge independently of model parameters.

**key_claim**: Retrieval as external memory decouples knowledge currency from model retraining, solving the temporal knowledge cutoff problem inherent in parametric LLMs — by storing knowledge externally, the system can incorporate new facts by adding to the retrieval store rather than fine-tuning the model; this separation of concerns is the key architectural insight behind RAG and is increasingly seen as a prerequisite for production LLM deployments in rapidly changing knowledge domains.

**warning**: External memory retrieval introduces a retrieval quality ceiling — if the retriever fails to surface relevant documents, the generator has no access to the needed information regardless of its parametric knowledge, and retrieval failures compound silently when the model generates a fluent but factually unsupported response; monitoring retrieval recall, not just generation quality, is essential for maintaining system-level accuracy.
