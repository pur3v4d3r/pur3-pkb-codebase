---
batch_name: pe-04-optimization-and-rag
batch_date: 2026-05-20
default_domain: prompt-engineering
default_confidence: high
notes: |
  Twenty concepts covering prompt optimisation methods and retrieval-augmented
  generation. Optimisation section spans automated prompt engineering, gradient-
  free search, DSPy, soft/prefix tuning, compression, paraphrasing, and ensemble
  strategies. RAG section covers dense retrieval, HyDE, self-RAG, corrective RAG,
  iterative retrieval, KILT, and DSP frameworks.
---

# Batch: PE-04 Prompt Optimization and Retrieval-Augmented Generation

## Automatic Prompt Engineering

- secondary_domains: [meta-learning, nlp-research]
- aliases: [APE, auto-prompt, automated prompt search]
- broader: [prompt-optimization]
- narrower: [gradient-free-prompt-optimization, evolutionary-prompt-optimization]
- related: [gradient-free-prompt-optimization, dspy-framework, prompt-paraphrasing, reflexion-based-prompt-refinement]
- prerequisites: [few-shot-prompting, large-language-models]
- confidence: high

**definition**: Automatic Prompt Engineering is the use of computational methods — including LLM-generated candidates, scoring functions, and search algorithms — to discover high-performing prompt templates without relying solely on human intuition and manual trial-and-error, typically framing prompt selection as an optimisation problem over a discrete or continuous prompt space.

**key_claim**: Automatic Prompt Engineering demonstrates that human-authored prompts are frequently sub-optimal even when written by domain experts, and that systematically searching the space of possible instructions with an automated evaluator can find prompts that generalise better across input distributions than those produced by any individual prompt engineer operating within a limited budget of manual attempts.

**warning**: Automatic Prompt Engineering risks overfitting the discovered prompts to the evaluation set used during the search process; prompts found by optimising on a fixed validation split may fail to generalise to slightly different task distributions or input styles, and the benchmark performance of automatically engineered prompts should always be validated on held-out data before deployment.

## Gradient-Free Prompt Optimization

- secondary_domains: [combinatorial-optimization, meta-learning]
- aliases: [discrete prompt optimisation, black-box prompt search]
- broader: [automatic-prompt-engineering, prompt-optimization]
- related: [automatic-prompt-engineering, evolutionary-prompt-optimization, dspy-framework, prompt-tuning]
- prerequisites: [automatic-prompt-engineering, large-language-models]
- confidence: high

**definition**: Gradient-Free Prompt Optimization refers to methods that search for better prompt templates or instructions using only forward-pass evaluations of a language model — without access to model gradients — relying instead on techniques such as genetic algorithms, hill climbing, Bayesian optimisation, beam search over candidate instructions, or LLM-as-proposer strategies.

**key_claim**: Gradient-Free Prompt Optimization is the only viable prompt optimisation approach when the target model is accessed via an API that exposes only logits or text outputs, not gradients; this practical constraint makes gradient-free methods the dominant paradigm for optimising prompts against commercial frontier models, despite their lower sample efficiency compared to gradient-based alternatives.

**warning**: Gradient-Free Prompt Optimization can be computationally expensive when the evaluation budget is limited; each evaluation requires a full model forward pass, and the discrete nature of the prompt space means small changes in wording can cause discontinuous jumps in performance, making smooth landscape assumptions from continuous optimisation inapplicable and search convergence unreliable.

## DSPy Framework

- secondary_domains: [framework-design, nlp-systems]
- aliases: [DSPy, Declarative Self-improving Python, DSPy programming model]
- broader: [automatic-prompt-engineering, gradient-free-prompt-optimization]
- related: [automatic-prompt-engineering, gradient-free-prompt-optimization, prompt-tuning, chain-of-thought-prompting]
- prerequisites: [automatic-prompt-engineering, large-language-models, few-shot-prompting]
- confidence: high

**definition**: DSPy Framework is a programming model for building language model pipelines in which the developer specifies the desired input–output behaviour of each module declaratively, and a DSPy compiler automatically optimises the prompts, few-shot demonstrations, and module configurations to maximise a user-defined metric on a development set, replacing manual prompt engineering with algorithm-driven prompt compilation.

**key_claim**: DSPy Framework reconceptualises prompt engineering as a software engineering problem: rather than hand-tuning natural language instructions, the developer defines a task specification and a metric, and the framework's optimiser finds the prompt artefacts that satisfy the specification, enabling reproducible, version-controlled, and systematically improved LLM pipelines rather than artisanal prompt collections.

**warning**: DSPy Framework introduces significant learning curve and infrastructure overhead; the compilation step requires a labelled development set (even a small one), a metric function, and sufficient computational budget for multiple optimisation rounds, meaning it is most cost-effective for stable production pipelines and less appropriate for one-off exploratory tasks where manual prompting is faster to iterate.

## Prompt Tuning

- secondary_domains: [parameter-efficient-fine-tuning, nlp-research]
- aliases: [soft prompt tuning, learned prompts]
- broader: [parameter-efficient-fine-tuning, prompt-optimization]
- narrower: [soft-prompting, prefix-tuning]
- related: [soft-prompting, prefix-tuning, gradient-free-prompt-optimization, prompt-tuning]
- prerequisites: [large-language-models, fine-tuning, backpropagation]
- confidence: high

**definition**: Prompt Tuning is a parameter-efficient fine-tuning technique in which a small set of continuous embedding vectors — the "soft prompt" — is prepended to the input and optimised via backpropagation on a task-specific dataset while all original model weights remain frozen, allowing the model to be adapted to new tasks at a fraction of the cost of full fine-tuning.

**key_claim**: Prompt Tuning demonstrates that at sufficiently large model scale (billions of parameters), adapting only a few hundred learnable embedding vectors achieves competitive performance with full model fine-tuning on many NLP benchmarks, fundamentally changing the cost structure of task adaptation by replacing the need to train and store a full model copy per task with a small per-task prompt embedding that can be swapped in at inference time.

**warning**: Prompt Tuning requires gradient access to the model's embedding layer, making it inapplicable to API-only model deployments; additionally, the learned soft prompts are not human-interpretable and do not transfer across different model architectures or tokenisers, meaning task adaptation artefacts are tightly coupled to the specific model checkpoint they were trained against.

## Soft Prompting

- secondary_domains: [parameter-efficient-fine-tuning, nlp-research]
- aliases: [continuous prompting, learnable prompt embeddings]
- broader: [prompt-tuning]
- related: [prompt-tuning, prefix-tuning, gradient-free-prompt-optimization, automatic-prompt-engineering]
- prerequisites: [large-language-models, fine-tuning, backpropagation]
- confidence: high

**definition**: Soft Prompting is the general technique of prepending or inserting learnable continuous-valued embedding vectors into the model's input representation, where these vectors exist only in the embedding space and have no corresponding natural-language tokens, trained end-to-end against a task objective while model parameters remain fixed.

**key_claim**: Soft Prompting separates the expressiveness of task adaptation from the constraint of natural language; because the learnable vectors are unconstrained in the embedding space rather than restricted to the convex hull of token embeddings, they can represent task-relevant directions that no human-authored natural language instruction could encode, potentially accessing adaptation signal unavailable to discrete prompt engineering.

**warning**: Soft Prompting produces completely opaque adaptation: the learned embedding vectors cannot be decoded into interpretable language, there is no way to audit what task-specific information they encode, and debugging failures requires interpreting model behaviour rather than reading the prompt — which substantially raises the barrier to understanding why a soft-prompted model produces unexpected outputs.

## Prefix Tuning

- secondary_domains: [parameter-efficient-fine-tuning, nlp-research]
- aliases: [prefix vectors, trainable prefix]
- broader: [prompt-tuning, soft-prompting]
- related: [soft-prompting, prompt-tuning, gradient-free-prompt-optimization]
- prerequisites: [large-language-models, fine-tuning, transformer-attention-mechanism]
- confidence: high

**definition**: Prefix Tuning is a parameter-efficient fine-tuning method that learns a sequence of continuous vectors prepended to the key and value matrices of every transformer attention layer across the entire network depth, providing the model with a richer adaptation signal that penetrates all layers simultaneously rather than only conditioning the input embedding layer.

**key_claim**: Prefix Tuning's layer-wise injection of learnable prefix vectors provides a more expressive adaptation mechanism than input-layer-only soft prompting because each attention layer receives task-specific context directly, allowing the prefix to shape intermediate representations rather than relying on the model's forward pass to propagate task information from the input embedding through all subsequent layers.

**warning**: Prefix Tuning increases KV-cache memory requirements at inference time proportional to the prefix sequence length multiplied by the number of layers, since the prefix key–value pairs must be stored and attended to in every layer for every generated token — a cost that becomes significant for long prefixes or large models deployed in memory-constrained production environments.

## Prompt Compression

- secondary_domains: [inference-efficiency, nlp-systems]
- aliases: [context compression, prompt distillation, prompt pruning]
- broader: [token-budget-management, prompt-optimization]
- related: [token-budget-management, context-window-management, prompt-paraphrasing, kv-cache-mechanics]
- prerequisites: [large-language-models, context-window-management]
- confidence: high

**definition**: Prompt Compression is the set of techniques that reduce the token length of a prompt while preserving the task-relevant information it contains, including methods such as extractive summarisation of retrieved documents, learned compression networks that encode long contexts into shorter token sequences, and LLM-based distillation that rewrites verbose instructions into semantically equivalent but more concise forms.

**key_claim**: Prompt Compression directly reduces inference cost and latency for long-context tasks; because transformer attention scales quadratically with sequence length, halving the prompt length can reduce attention computation by approximately 75%, and empirical results show that aggressive compression (retaining only 10–30% of tokens) incurs surprisingly small performance penalties on downstream tasks when the compression preserves the information most predictive of the correct output.

**warning**: Prompt Compression optimised for token reduction can inadvertently remove context that is not obviously task-relevant but is critical for edge-case handling; compression models trained on average-case performance profiles may systematically discard information that matters for the long tail of inputs, leading to selectively degraded performance on atypical queries that are precisely the cases where robust handling matters most.

## Prompt Paraphrasing

- secondary_domains: [nlp-research, robustness]
- aliases: [instruction paraphrasing, prompt rewriting, equivalent prompt generation]
- broader: [prompt-optimization, automatic-prompt-engineering]
- related: [automatic-prompt-engineering, prompt-sensitivity-analysis, prompt-ensembling, gradient-free-prompt-optimization]
- prerequisites: [large-language-models, prompt-formatting]
- confidence: high

**definition**: Prompt Paraphrasing is the systematic generation of semantically equivalent alternative phrasings of a prompt instruction or context, used either as a source of candidates in automated prompt search, as a robustness evaluation method to measure how sensitive a model is to surface-level instruction variation, or as an ensemble technique that averages predictions across multiple paraphrases to reduce variance.

**key_claim**: Prompt Paraphrasing reveals a fundamental fragility in LLM task specification: semantically equivalent instructions can produce performance differences of 10–40 percentage points on structured benchmarks, demonstrating that model performance is partly a function of the specific surface form of the instruction rather than its meaning — a finding with serious implications for prompt engineering reliability and evaluation validity.

**warning**: Prompt Paraphrasing-based ensembles improve robustness but multiply inference cost proportionally to the number of paraphrases sampled; in production systems where latency and cost are constrained, the reliability gains from paraphrase ensembling must be weighed against the option of investing the same compute budget in a single, carefully selected high-performing prompt formulation.

## Prompt Ensembling

- secondary_domains: [ensemble-methods, robustness]
- aliases: [multi-prompt ensembling, prompt aggregation]
- broader: [prompt-optimization, ensemble-methods]
- related: [prompt-paraphrasing, self-consistency-sampling, boosted-prompt-ensembles, automatic-prompt-engineering]
- prerequisites: [large-language-models, ensemble-methods, few-shot-prompting]
- confidence: high

**definition**: Prompt Ensembling is the technique of querying a language model with multiple distinct prompts for the same input and aggregating the resulting outputs — through majority voting, probability averaging, or learned combination weights — to produce a final answer that is more robust and accurate than any single prompt's response.

**key_claim**: Prompt Ensembling trades compute for reliability in a predictable manner; because different prompts activate different aspects of the model's knowledge and induce different error patterns, their outputs are partially decorrelated, and aggregation reduces variance proportionally to the decorrelation, making prompt ensembling a principled approach to improving precision on tasks where individual prompt sensitivity is high and compute is not constrained.

**warning**: Prompt Ensembling assumes that errors across prompts are independent or at least partially decorrelated; if all ensemble members share a systematic bias (e.g., all prompts reinforce the same misconception), aggregation will amplify rather than cancel the error, and the ensemble will be confidently wrong — making prompt diversity an essential prerequisite for effective ensembling rather than an optional enhancement.

## Boosted Prompt Ensembles

- secondary_domains: [ensemble-methods, meta-learning]
- aliases: [adaptive prompt ensembles, boosted prompting]
- broader: [prompt-ensembling, ensemble-methods]
- related: [prompt-ensembling, automatic-prompt-engineering, prompt-paraphrasing]
- prerequisites: [prompt-ensembling, large-language-models, boosting-algorithms]
- confidence: high

**definition**: Boosted Prompt Ensembles are an ensemble construction strategy in which prompts are added to the ensemble sequentially, with each new prompt weighted to compensate for errors made by the current ensemble — analogous to boosting in classical machine learning — producing an ensemble where successive members are specifically designed to address the residual mistakes of their predecessors.

**key_claim**: Boosted Prompt Ensembles improve over naive uniform-weight ensembles by concentrating diversity on the error-prone regions of the input space; while a uniform ensemble reduces variance uniformly across all inputs, a boosted ensemble directs additional capacity toward the examples that the existing members collectively fail on, making the performance improvement on difficult instances disproportionately large relative to the number of ensemble members added.

**warning**: Boosted Prompt Ensembles require a held-out error signal to guide the boosting process, which means they need a labelled development set and multiple rounds of evaluation before deployment; in rapid-iteration settings or low-data regimes, the overhead of boosting calibration may outweigh its performance benefits compared to a simpler uniform ensemble of diverse prompts.

## Evolutionary Prompt Optimization

- secondary_domains: [evolutionary-algorithms, meta-learning]
- aliases: [genetic prompt search, evolutionary prompt search, EvoPrompt]
- broader: [gradient-free-prompt-optimization, automatic-prompt-engineering]
- related: [gradient-free-prompt-optimization, automatic-prompt-engineering, prompt-paraphrasing, dspy-framework]
- prerequisites: [automatic-prompt-engineering, gradient-free-prompt-optimization, large-language-models]
- confidence: high

**definition**: Evolutionary Prompt Optimization applies evolutionary algorithm principles — selection, crossover, and mutation — to the search for optimal prompt templates, maintaining a population of candidate prompts that are evaluated on a fitness function (task performance), recombined, and mutated across generations to progressively discover higher-performing prompt formulations.

**key_claim**: Evolutionary Prompt Optimization handles non-convex, discontinuous prompt fitness landscapes more effectively than greedy hill-climbing because the population-based search maintains diversity and can escape local optima through crossover operations that combine beneficial features from multiple independently-developed candidate prompts — a qualitative advantage that greedy methods cannot replicate by construction.

**warning**: Evolutionary Prompt Optimization has high computational cost because evaluating each member of a population requires forward passes on a validation set across potentially hundreds of generations; the total evaluation budget can reach thousands of model calls, making it cost-prohibitive for large models or large validation sets, and practitioners must carefully balance population size against the number of generations to stay within budget.

## Reflexion-Based Prompt Refinement

- secondary_domains: [self-improvement, iterative-refinement]
- aliases: [reflexion prompt loop, iterative prompt refinement via reflection]
- broader: [automatic-prompt-engineering, reflexion]
- related: [reflexion, self-refine, automatic-prompt-engineering, dspy-framework, chain-of-verification]
- prerequisites: [automatic-prompt-engineering, reflexion, large-language-models]
- confidence: high

**definition**: Reflexion-Based Prompt Refinement is an iterative prompt optimisation technique in which the model is prompted to reflect on the failures of a previous prompt version — identifying what went wrong and why — and to generate an improved prompt that addresses the identified failure modes, using linguistic reasoning about the prompt's shortcomings rather than gradient-based optimisation to drive improvement.

**key_claim**: Reflexion-Based Prompt Refinement leverages the model's meta-linguistic reasoning ability to perform targeted, interpretable prompt improvements without requiring numerical optimisation infrastructure; because the improvement process is expressed in natural language, each refinement step is auditable, and the reasoning behind each change can be inspected, making this approach uniquely aligned with the transparency and controllability requirements of production prompt engineering workflows.

**warning**: Reflexion-Based Prompt Refinement can enter an improvement loop where the model generates plausible-sounding critiques and revisions that do not actually address the root cause of the failures; the model may overfit its reflections to the specific failure examples provided, producing a revised prompt that resolves the presented examples while introducing new failure modes on other input types not represented in the reflection context.

## Retrieval-Augmented Generation

- secondary_domains: [information-retrieval, knowledge-intensive-nlp]
- aliases: [RAG, retrieve-then-generate, retrieval-grounded generation]
- broader: [knowledge-intensive-nlp]
- narrower: [self-rag, corrective-rag, iterative-retrieval, retrieval-augmented-few-shot]
- related: [dense-passage-retrieval, hyde-hypothetical-document-embeddings, self-rag, knowledge-intensive-nlp, demonstrate-search-predict]
- prerequisites: [large-language-models, information-retrieval, embedding-models]
- confidence: high

**definition**: Retrieval-Augmented Generation is an architecture that augments a language model's generation process by first retrieving relevant documents or passages from an external corpus using a query derived from the input, then conditioning the generation on both the original input and the retrieved evidence — enabling the model to ground its responses in up-to-date, verifiable external knowledge rather than relying solely on parametric memory.

**key_claim**: Retrieval-Augmented Generation separates the knowledge storage problem from the reasoning problem; rather than requiring the LLM to memorise all world knowledge during pretraining, RAG externalises knowledge storage to a retrievable corpus, making knowledge updates cheap (reindex the corpus) and providing natural attribution (the retrieved documents serve as citations), fundamentally changing the reliability and maintainability profile of knowledge-intensive applications.

**warning**: Retrieval-Augmented Generation introduces retrieval as a critical failure point that is often harder to debug than generation failures; if the retriever returns irrelevant, misleading, or adversarially crafted documents, the generator will confidently incorporate that content into its response — a failure mode called "retrieval poisoning" — and because the generation appears grounded in cited sources, these errors may be more trusted and less scrutinised than uncited hallucinations.

## Dense Passage Retrieval

- secondary_domains: [information-retrieval, embedding-models]
- aliases: [DPR, bi-encoder retrieval, dense retrieval]
- broader: [retrieval-augmented-generation, information-retrieval]
- related: [retrieval-augmented-generation, hyde-hypothetical-document-embeddings, self-rag, embedding-models]
- prerequisites: [information-retrieval, embedding-models, large-language-models]
- confidence: high

**definition**: Dense Passage Retrieval is an information retrieval method in which both queries and passages are encoded into dense vector representations by dual encoder neural networks, and retrieval is performed by finding passages whose embeddings have the highest inner product or cosine similarity with the query embedding — replacing traditional sparse keyword matching with semantic vector search.

**key_claim**: Dense Passage Retrieval achieves substantially better recall than sparse BM25 retrieval on semantically complex queries where the query and relevant passage share little lexical overlap, because dense encoders can learn to represent the semantic relationship between question intent and answer content regardless of surface vocabulary — but this advantage comes at the cost of requiring large-scale training data and approximate nearest-neighbour indexing infrastructure.

**warning**: Dense Passage Retrieval is sensitive to distribution shift between the queries seen during encoder training and the queries at deployment time; an encoder trained on a specific domain's query–passage pairs may fail to generalise to out-of-domain queries that use different vocabulary, framing, or conceptual granularity, and this degradation can be silent because top-ranked results still look superficially relevant while being semantically mismatched.

## HyDE Hypothetical Document Embeddings

- secondary_domains: [information-retrieval, zero-shot-retrieval]
- aliases: [HyDE, hypothetical document embeddings, query expansion via generation]
- broader: [retrieval-augmented-generation, dense-passage-retrieval]
- related: [dense-passage-retrieval, retrieval-augmented-generation, zero-shot-prompting]
- prerequisites: [dense-passage-retrieval, large-language-models, information-retrieval]
- confidence: high

**definition**: HyDE Hypothetical Document Embeddings is a zero-shot dense retrieval technique in which the language model first generates a hypothetical answer document for a query, and then retrieves real documents by embedding the generated hypothetical document rather than the original query — bridging the semantic gap between short question-style queries and longer answer-style passages in the retrieval corpus.

**key_claim**: HyDE Hypothetical Document Embeddings solves the query–document vocabulary mismatch problem at zero training cost; by having the LLM generate a document in the same style and vocabulary as the retrieval corpus, the embedding comparison is transformed from a question-to-answer embedding comparison (high mismatch) to an answer-to-answer embedding comparison (low mismatch), enabling high-recall retrieval without any fine-tuning of the retrieval encoder.

**warning**: HyDE Hypothetical Document Embeddings propagates hallucinations into the retrieval stage; if the LLM generates a confident but factually incorrect hypothetical document, the subsequent retrieval will return real documents that are topically similar to the wrong content rather than to the true answer, making the downstream generation condition on a misleading retrieval context that appears well-supported.

## Self-RAG

- secondary_domains: [retrieval, self-supervised-learning]
- aliases: [self-reflective RAG, Self-RAG]
- broader: [retrieval-augmented-generation]
- related: [retrieval-augmented-generation, corrective-rag, chain-of-verification, reflexion]
- prerequisites: [retrieval-augmented-generation, large-language-models, fine-tuning]
- confidence: high

**definition**: Self-RAG is a retrieval-augmented generation framework in which the model is trained to dynamically decide whether to retrieve at all for a given input, to critique the relevance and supportedness of retrieved passages inline, and to assess whether its own generated segments are supported by the retrieved evidence — inserting special reflection tokens that make the retrieval and self-critique process explicit and controllable.

**key_claim**: Self-RAG addresses the fundamental limitation of standard RAG systems that retrieve unconditionally for every input; by training the model to judge when retrieval is helpful and when the parametric knowledge suffices, Self-RAG reduces noise from irrelevant retrievals on knowledge-sufficient queries while focusing retrieval capacity on genuinely knowledge-demanding ones, improving both efficiency and factual accuracy simultaneously.

**warning**: Self-RAG requires fine-tuning the language model on reflection-token supervision, making it inapplicable to API-only models; the quality of the self-critique is only as good as the training signal used to teach the reflection tokens, and if the training data underrepresents certain failure modes, the model's inline self-critique will be confidently wrong on exactly those cases it was not trained to recognise.

## Corrective RAG

- secondary_domains: [retrieval, error-correction]
- aliases: [CRAG, corrective retrieval, retrieval with validation]
- broader: [retrieval-augmented-generation]
- related: [retrieval-augmented-generation, self-rag, chain-of-verification, hallucination-detection]
- prerequisites: [retrieval-augmented-generation, large-language-models]
- confidence: high

**definition**: Corrective RAG is a retrieval-augmented generation strategy that adds a lightweight relevance evaluator to the retrieval stage; if the evaluator judges retrieved documents to be irrelevant or ambiguous, the system triggers a corrective action — such as web search, query reformulation, or decomposition into sub-queries — before passing the context to the generator, rather than blindly conditioning on potentially unhelpful retrievals.

**key_claim**: Corrective RAG dramatically reduces the impact of retrieval failures by treating the retrieved context as a hypothesis to be validated rather than a fact to be accepted; by interposing a quality gate between retrieval and generation, it breaks the assumption in standard RAG that whatever the retriever returns is beneficial, and empirical results show it substantially reduces hallucination rates on questions where the initial retrieval is insufficient.

**warning**: Corrective RAG adds latency and complexity to the retrieval pipeline; when the relevance evaluator triggers corrective retrieval, the total number of retrieval and generation calls approximately doubles, making Corrective RAG unsuitable for latency-sensitive applications where the first-pass retrieval failure rate is high enough to make the average-case latency unacceptable.

## Iterative Retrieval

- secondary_domains: [information-retrieval, multi-hop-reasoning]
- aliases: [multi-hop retrieval, iterative document gathering, adaptive retrieval]
- broader: [retrieval-augmented-generation]
- related: [retrieval-augmented-generation, self-rag, demonstrate-search-predict, dense-passage-retrieval]
- prerequisites: [retrieval-augmented-generation, dense-passage-retrieval, large-language-models]
- confidence: high

**definition**: Iterative Retrieval is a multi-round retrieval strategy in which the language model generates a partial response or intermediate reasoning step, uses that intermediate output to formulate a new retrieval query, retrieves additional documents, and integrates the new evidence before continuing generation — repeating this cycle until the model has gathered sufficient evidence to produce a complete, well-supported response.

**key_claim**: Iterative Retrieval is necessary for multi-hop question answering where the answer to the final question requires first answering intermediate questions that cannot be identified from the original query alone; single-pass RAG fails on these tasks because the initial retrieval query cannot anticipate the intermediate concepts needed to bridge from the question to the answer, while iterative retrieval can follow the reasoning chain to collect the required evidence at each step.

**warning**: Iterative Retrieval amplifies both the benefits and risks of retrieval in proportion to the number of rounds; each additional retrieval round introduces a new opportunity for the retriever to return a misleading document, and the model's growing reasoning context may increase susceptibility to distractor passages that are relevant to intermediate conclusions but inconsistent with the final correct answer.

## Knowledge-Intensive NLP

- secondary_domains: [nlp-research, information-retrieval]
- aliases: [KI-NLP, knowledge-grounded NLP, KILT benchmark]
- broader: [retrieval-augmented-generation, natural-language-processing]
- related: [retrieval-augmented-generation, dense-passage-retrieval, hallucination-detection, factual-consistency-evaluation]
- prerequisites: [large-language-models, information-retrieval, natural-language-processing]
- confidence: high

**definition**: Knowledge-Intensive NLP refers to natural language processing tasks that require access to specific world knowledge beyond what can be inferred from the immediate input alone — including open-domain question answering, fact verification, slot filling, and entity linking — and the research agenda concerned with building systems that can retrieve and reason over external knowledge to perform these tasks reliably.

**key_claim**: Knowledge-Intensive NLP establishes a fundamental architectural dichotomy between parametric knowledge (stored in model weights, fixed at training time) and non-parametric knowledge (stored in retrievable corpora, updatable at inference time); the design choice between these storage modes determines the system's trade-offs between knowledge freshness, update cost, attribution capability, and inference latency in ways that have profound implications for production deployment.

**warning**: Knowledge-Intensive NLP benchmarks measure performance on specific knowledge domains and question types that may not represent the knowledge-intensity profile of a target application; a system that achieves state-of-the-art performance on KILT or Natural Questions may still fail on domain-specific knowledge-intensive tasks because the required knowledge is absent from the retrieval corpus or represented at insufficient granularity.

## Demonstrate Search Predict

- secondary_domains: [pipeline-design, retrieval]
- aliases: [DSP, demonstrate-search-predict framework]
- broader: [retrieval-augmented-generation, automatic-prompt-engineering]
- related: [retrieval-augmented-generation, dspy-framework, iterative-retrieval, few-shot-prompting]
- prerequisites: [retrieval-augmented-generation, few-shot-prompting, large-language-models]
- confidence: high

**definition**: Demonstrate Search Predict is a compositional framework for knowledge-intensive NLP tasks that decomposes inference into three programmatic stages — demonstrate (retrieve or generate few-shot demonstrations), search (retrieve relevant passages using an intermediate query), and predict (generate the final answer conditioned on demonstrations and retrieved passages) — with each stage's behaviour specified programmatically and optimised jointly.

**key_claim**: Demonstrate Search Predict shows that the composition of retrieval and generation can be expressed as a modular program with explicit inter-stage interfaces, enabling systematic optimisation of each stage independently before joint optimisation — a modular decomposition that inspired the later DSPy framework and established the principle that RAG systems should be designed as programs rather than monolithic end-to-end prompts.

**warning**: Demonstrate Search Predict's multi-stage architecture introduces latency at each stage and requires careful orchestration to avoid cascading errors where a bad demonstration retrieved in the first stage biases both the search query in the second stage and the prediction in the third stage, producing a correlated error chain that is harder to debug than the independent failures in a simpler single-stage RAG system.
