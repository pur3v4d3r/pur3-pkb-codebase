---
batch_name: b02-03-attention-mechanisms
batch_date: 2026-05-22
default_domain: transformer-architecture
default_confidence: high
notes: |
  Fifteen concepts covering transformer attention mechanisms and their
  variants. Spans multi-head attention, cross-attention, self-attention
  patterns, head specialization, induction and copy-suppression heads,
  attention sinks, head pruning, positional encoding variants (learned,
  RoPE, ALiBi), FlashAttention, grouped-query attention, sliding-window
  attention, and sparse attention patterns. Batch 02 of the
  prompt-engineering and LLM series.
---

# Batch: B02-03 Attention Mechanisms and Architecture

## Multi-Head Attention Mechanics

- secondary_domains: [deep-learning, large-language-models, mechanistic-interpretability]
- aliases: [MHA, multi-head self-attention, transformer multi-head attention]
- broader: [transformer-architecture, attention-mechanisms]
- narrower: [grouped-query-attention, self-attention-patterns, attention-head-specialization]
- related: [cross-attention-in-transformers, flash-attention-algorithm, positional-encoding-variants]
- prerequisites: [transformer-architecture, attention-mechanisms, linear-algebra]
- confidence: high

**definition**: Multi-head attention (MHA) is the core computational mechanism of the transformer architecture in which the input representation is linearly projected into h parallel query, key, and value spaces (heads), a scaled dot-product attention operation is computed independently within each head, and the h head outputs are concatenated and projected through a learned output matrix to produce the layer's output. The multi-head structure allows different heads to attend to different positional and semantic aspects of the input simultaneously — one head may attend to syntactic dependencies, another to coreference relations, and another to semantic topic similarity — giving the layer a rich capacity to integrate diverse relational information in a single computation. The scaled dot-product scaling by $\frac{1}{\sqrt{d_k}}$ prevents softmax saturation for large key dimensions.

**key_claim**: Multi-head attention's representational power comes from the diversity of the h subspaces, not from the total parameter count — an h-head attention layer with total dimension $d$ can represent h independent relational patterns simultaneously, whereas a single-head attention layer with the same parameter count is constrained to a single relational pattern, and empirical analysis consistently shows that different heads learn qualitatively distinct and complementary attention patterns that cooperate to produce the layer's output representation.

**warning**: The apparent interpretability of individual attention heads — the common practice of visualising attention weights and attributing linguistic meaning to the resulting patterns — is methodologically misleading: high attention weight from token A to token B does not imply that information about B determines the output for A, because value vectors can be zero-valued even when attention weights are high, and the actual information flow is determined by the attention-weight-value product rather than the attention weights alone.

## Cross-Attention in Transformers

- secondary_domains: [deep-learning, sequence-to-sequence-models, natural-language-processing]
- aliases: [encoder-decoder attention, cross-modal attention, decoder attention over encoder]
- broader: [transformer-architecture, attention-mechanisms]
- related: [multi-head-attention-mechanics, self-attention-patterns, grouped-query-attention]
- prerequisites: [transformer-architecture, encoder-decoder-models, attention-mechanisms]
- confidence: high

**definition**: Cross-attention in transformers is the attention mechanism in encoder-decoder architectures in which the decoder's queries are computed from the decoder's internal state while the keys and values are computed from the encoder's output representation, allowing each decoder position to attend to any position in the encoded source sequence. Cross-attention is the primary mechanism by which encoder-decoder models align target generation with source content in machine translation, summarisation, and multimodal generation. In multimodal transformers, cross-attention connects modality-specific encoder outputs (visual, audio, or structured data) to text decoder queries, enabling the decoder to condition its generation on the encoded non-textual representation.

**key_claim**: Cross-attention in encoder-decoder models learns highly sparse alignment patterns — different heads specialise in different aspects of source-target alignment, including lexical translation, structural reordering, and phrase boundary detection — and the interpretability of cross-attention weights in translation tasks is higher than that of self-attention weights because the bilingual training signal constrains the alignment patterns to be semantically consistent with source-target correspondences rather than being free to learn arbitrary relational patterns.

**warning**: Decoder-only architectures that have replaced encoder-decoder models in many NLP tasks lose cross-attention as a mechanism, requiring them to perform source-target alignment implicitly through in-context self-attention over the concatenated source and target, which is less parameter-efficient for alignment-heavy tasks and makes it harder to extract explicit source-target alignments for downstream use cases such as translation quality estimation or multimodal grounding.

## Self-Attention Patterns

- secondary_domains: [mechanistic-interpretability, deep-learning, natural-language-processing]
- aliases: [intra-sequence attention patterns, self-attention structure, transformer self-attention behaviour]
- broader: [transformer-architecture, multi-head-attention-mechanics]
- narrower: [induction-heads, copy-suppression-heads, attention-sinks, attention-head-specialization]
- related: [multi-head-attention-mechanics, positional-encoding-variants]
- prerequisites: [transformer-architecture, attention-mechanisms]
- confidence: high

**definition**: Self-attention patterns refer to the characteristic structural regularities in the attention weight matrices produced by transformer self-attention layers — including diagonal patterns (attending to the current or adjacent tokens), vertical stripe patterns (attending broadly to a specific token type such as the previous token, period, or separator), block patterns (attending broadly within a clause or sentence), induction patterns (attending to tokens that previously followed similar contexts), and copy patterns (attending to tokens that should be reproduced in the output). Analysis of self-attention patterns is a central tool in mechanistic interpretability for decomposing what information different heads process and how that information is combined across layers.

**key_claim**: Self-attention patterns are not random but correspond to functionally interpretable operations that are conserved across models of different sizes and architectures — syntactic dependency resolution, semantic role labelling, coreference tracking, and n-gram completion are all recoverable from the patterns of individual attention heads, suggesting that these operations represent the natural decomposition of language understanding into modular computational primitives that transformer training consistently rediscovers.

**warning**: Self-attention pattern analysis at the level of attention weights provides an incomplete picture of transformer information processing because the model's behaviour is determined by the product of attention weights and value vectors, not by the weights alone; the same attention weight pattern can implement different computational operations depending on the value vectors, and interpretability analyses that focus exclusively on attention weights without examining value matrices will systematically misattribute the functional roles of individual heads.

## Attention Head Specialization

- secondary_domains: [mechanistic-interpretability, deep-learning, natural-language-processing]
- aliases: [head function specialization, attention head roles, transformer head diversity]
- broader: [self-attention-patterns, multi-head-attention-mechanics]
- narrower: [induction-heads, copy-suppression-heads]
- related: [head-pruning-effects, self-attention-patterns, mechanistic-interpretability]
- prerequisites: [multi-head-attention-mechanics, transformer-architecture, mechanistic-interpretability]
- confidence: high

**definition**: Attention head specialization refers to the empirical phenomenon in which different attention heads within and across transformer layers learn to perform qualitatively distinct computational functions — syntactic heads attending to subject-verb dependencies, positional heads implementing fixed-offset attention to adjacent tokens, semantic heads attending to topically related tokens, induction heads completing repeated subsequences, and copy-suppression heads suppressing the direct copying of source tokens in generation tasks. Head specialization emerges during pretraining without explicit supervision and is remarkably consistent across different models, suggesting that it reflects the natural functional decomposition of the language modelling task rather than an arbitrary solution that training happens to converge on.

**key_claim**: The degree of attention head specialization scales with model size — larger models develop more highly specialised heads that perform more precise and interpretable functions, while small models tend to develop overlapping and less precise head functions, which explains why mechanistic interpretability findings from small models (e.g., two-layer transformers) do not always transfer cleanly to large models where the same function is performed by a more specialised circuit with different routing properties.

**warning**: Identifying head specialization through post-hoc analysis of attention patterns is subject to confirmation bias — researchers typically identify the most interpretable heads and report those as evidence for specialization while failing to characterise the majority of heads that do not correspond to clean interpretable functions; the apparent high degree of specialization in published analyses is partly an artefact of selective reporting rather than a representative picture of the functional organisation of all heads.

## Induction Heads

- secondary_domains: [mechanistic-interpretability, large-language-models, in-context-learning]
- aliases: [induction circuit, k-v copying heads, pattern completion heads]
- broader: [attention-head-specialization, self-attention-patterns]
- related: [copy-suppression-heads, in-context-learning-as-meta-learning, self-attention-patterns]
- prerequisites: [transformer-architecture, attention-mechanisms, mechanistic-interpretability]
- confidence: high

**definition**: Induction heads are a specific class of attention heads that implement the operation: "given the current token, find all previous occurrences of this token in the context, and attend to the token that followed each of those occurrences." This operation allows the model to complete repeated bigrams — if "[A][B] ... [A]" appears in context, the induction head boosts the probability of "[B]" following the second occurrence of "[A]." Induction heads consist of a two-head circuit: a "previous token head" that attends from each token to the preceding token, and an "induction head" proper that attends from the current token to tokens that the previous-token head found to be similar to the current token. The induction circuit is proposed as a key mechanistic substrate for in-context learning.

**key_claim**: The formation of induction heads represents a phase transition in transformer training — models undergo a sudden transition from a regime where they can only use earlier-in-training patterns to a regime where in-context learning emerges, and this transition coincides with the emergence of induction head circuits in the early layers, providing mechanistic evidence that in-context learning capability is directly implemented by induction head circuits rather than being an emergent property of deeper layers.

**warning**: While induction heads provide a compelling mechanistic story for simple pattern-completion in-context learning, they do not fully explain the rich in-context learning capability of large models — tasks requiring multi-step reasoning, concept composition, and format generalisation cannot be implemented by induction circuits alone, and the mechanistic story for higher-level in-context learning behaviours remains incomplete; claiming that induction heads explain in-context learning generally overstates what the mechanistic evidence currently supports.

## Copy-Suppression Heads

- secondary_domains: [mechanistic-interpretability, large-language-models, natural-language-generation]
- aliases: [anti-copy heads, negative attention heads, suppression heads]
- broader: [attention-head-specialization, self-attention-patterns]
- related: [induction-heads, self-attention-patterns, attention-head-specialization]
- prerequisites: [transformer-architecture, mechanistic-interpretability, attention-mechanisms]
- confidence: high

**definition**: Copy-suppression heads are attention heads that reduce the logit probability of generating tokens that are copies of recent source-context tokens, effectively functioning as the inhibitory complement to induction heads. While induction heads boost the probability of completing repeated patterns, copy-suppression heads impose a penalty on naive token copying, preventing the model from defaulting to repetitive copying when induction-based completion is not the intended behaviour. Copy-suppression is particularly important in text generation tasks where the model must paraphrase, summarise, or synthesise rather than copy, and in abstractive tasks where verbatim repetition would indicate failure to process the source semantically.

**key_claim**: Copy-suppression heads are a mechanistic implementation of the tension between recall and generation in language models — they represent the architectural substrate by which the model trades off between directly copying information from context (high fidelity, low creativity) and generating novel text (low fidelity, high creativity), and their strength calibrates the model's abstractiveness; analysis shows that models trained on abstractive tasks develop stronger copy-suppression relative to models trained on extractive tasks.

**warning**: Copy-suppression heads can over-suppress legitimate copying in tasks that require verbatim reproduction of source text — legal document processing, quote extraction, and code completion — and prompting strategies that increase the model's verbatim copying tendency (e.g., instructing "quote exactly," using the original source as the first few tokens of the output) may be partially counteracting copy-suppression head activity rather than changing the model's semantic intent, which has implications for how verbatim output fidelity requirements should be engineered.

## Attention Sinks

- secondary_domains: [mechanistic-interpretability, large-language-models, context-length]
- aliases: [attention sink tokens, initial token attention concentration, sink tokens in transformers]
- broader: [self-attention-patterns, transformer-architecture]
- related: [sliding-window-attention, streaming-llm, positional-encoding-variants, self-attention-patterns]
- prerequisites: [transformer-architecture, attention-mechanisms, mechanistic-interpretability]
- confidence: high

**definition**: Attention sinks are specific token positions — most commonly the first token (often the beginning-of-sequence token) and the most recent few tokens — to which attention heads assign disproportionately high attention weight not because those positions contain highly relevant content but because they serve as "sink" positions that absorb excess probability mass when the softmax normalisation requires positive-summing attention weights even for tokens with no meaningful relevance. The attention sink phenomenon arises from the mathematical constraint that softmax attention weights must sum to 1, forcing the model to assign probability mass somewhere even when the ideal attention distribution would be near-uniform or near-zero for most positions; sink positions serve as "safe" recipients that the model has learned to use as probability dumps.

**key_claim**: Attention sinks are not interpretable as evidence that the first token is semantically important — they are a mathematical artefact of the softmax normalisation constraint, and their existence has practical implications for context window management: evicting the sink token from a sliding-window KV-cache causes catastrophic attention distribution collapse, while preserving the sink token's KV state even when its surrounding tokens are evicted maintains stable attention distributions, which is the key insight exploited by the StreamingLLM architecture.

**warning**: The attention sink phenomenon creates a subtle trap in interpretability analysis — researchers analysing which tokens receive high attention in transformer forward passes will consistently identify the first token (and sometimes period tokens) as "important" based on their high received-attention weight, and this attention should not be interpreted as evidence that these tokens are semantically important for the task; the attention weight is an implementation artefact, and the actual information conveyed by sink token value vectors is minimal.

## Head Pruning Effects

- secondary_domains: [model-compression, mechanistic-interpretability, deep-learning]
- aliases: [attention head pruning, sparse attention architectures, head ablation effects]
- broader: [attention-head-specialization, model-compression]
- related: [attention-head-specialization, sparse-attention-patterns, grouped-query-attention]
- prerequisites: [transformer-architecture, model-pruning, attention-mechanisms]
- confidence: high

**definition**: Head pruning effects refer to the downstream consequences of removing individual attention heads from a trained transformer model — either through hard ablation (zeroing out head output), structured pruning (removing head parameters), or soft pruning (applying learned masks). Research on head pruning reveals that a surprisingly large fraction of attention heads can be removed with minimal effect on downstream task performance, that specific task-critical heads (whose removal causes large performance drops) are consistently identifiable across multiple random seeds and model versions, and that the most important heads for one task are often not the most important heads for other tasks, suggesting that heads are partially task-specific.

**key_claim**: Head pruning studies reveal that transformer models are substantially overparameterised in their attention heads — studies consistently find that 30–50% of attention heads can be ablated with less than 1% downstream performance degradation, that the distribution of head importance is heavy-tailed (a few critical heads account for most of the performance), and that task performance can actually improve after pruning unimportant heads due to the elimination of noise from heads that specialise in regularities irrelevant to the task.

**warning**: Head importance is strongly task-dependent and context-dependent, making head pruning decisions that generalise across tasks difficult to make reliably — a head that is expendable for classification may be critical for generation, and a head that is expendable on short contexts may be critical for long-context tasks; generalised head pruning that improves one metric at the cost of another creates hidden capability regressions that are difficult to detect without comprehensive multi-task, multi-context evaluation.

## Positional Encoding Variants

- secondary_domains: [transformer-architecture, natural-language-processing, sequence-modelling]
- aliases: [position encoding methods, transformer positional embeddings, position representation in transformers]
- broader: [transformer-architecture]
- narrower: [rotary-position-embedding, alibi-positional-encoding]
- related: [multi-head-attention-mechanics, sliding-window-attention, context-length-extension]
- prerequisites: [transformer-architecture, embedding-representations]
- confidence: high

**definition**: Positional encoding variants are the different mechanisms used to inject position information into transformer models, enabling them to distinguish tokens based on their position in the sequence in the absence of recurrence. The original transformer used sinusoidal absolute positional encodings; subsequent variants include learned absolute embeddings (BERT, GPT-2), relative positional encodings (T5, Transformer-XL), Rotary Position Embedding (RoPE, LLaMA), ALiBi (attention with linear biases), and length-generalising approaches. The choice of positional encoding significantly affects the model's ability to generalise to sequence lengths longer than those seen in training — some methods fail completely beyond the training length while others extrapolate gracefully.

**key_claim**: The choice of positional encoding is the primary architectural determinant of long-context generalisation: models with learned absolute positional embeddings fail completely beyond the training context length because they have no representation for unseen positions; models with RoPE exhibit graceful degradation beyond training length with appropriate rescaling; and models with ALiBi generalize to longer contexts than the training length without any additional modification, making positional encoding choice a critical architectural decision for systems that need to process long documents.

**warning**: Positional encoding choice interacts with the model's use of position information in ways that are not fully understood, and simply replacing one positional encoding with another in a trained model is not trivially possible without retraining — the model's weights in attention layers are co-adapted with the positional encoding scheme used during training, and applying a different encoding at inference time to extend context length produces qualitatively different attention patterns that may not correspond to the model's intended behaviour.

## Rotary Position Embedding

- secondary_domains: [transformer-architecture, large-language-models, context-length]
- aliases: [RoPE, rotary positional encoding, rotary embeddings]
- broader: [positional-encoding-variants, transformer-architecture]
- related: [alibi-positional-encoding, positional-encoding-variants, context-length-extension, flash-attention-algorithm]
- prerequisites: [transformer-architecture, positional-encoding-variants, linear-algebra]
- confidence: high

**definition**: Rotary Position Embedding (RoPE) is a positional encoding scheme that encodes absolute position information in the frequency domain by applying a rotation matrix to the query and key vectors before computing attention, with the rotation angle proportional to the token's absolute position. The key property of RoPE is that the inner product between a rotated query vector and a rotated key vector is a function only of their relative position (position difference), naturally implementing relative positional encoding within the standard dot-product attention computation without requiring explicit relative bias matrices. RoPE has been adopted in LLaMA, Mistral, Falcon, and numerous other open-weight models due to its strong long-context performance and efficient implementation.

**key_claim**: RoPE's fundamental mathematical property — that relative position information is preserved through the rotation operation — enables it to generalise more gracefully to longer sequences than absolute encoding schemes, but its practical context extension capability is still bounded by the maximum frequency seen during training; beyond roughly 2x the training length, RoPE attention deteriorates because the model's attention patterns become unstable for rotation angles not represented in training, motivating context window extension techniques such as YaRN, LongRoPE, and dynamic NTK scaling.

**warning**: RoPE-based context extension techniques (NTK scaling, YaRN, LongRoPE) that modify the frequency basis without retraining the model introduce a mismatch between the positional encoding frequencies seen during training and those used at inference time; this mismatch produces progressive degradation in attention quality with increasing sequence length even when using "extended" versions, and the performance gains from these techniques should be validated empirically on the specific task and length regime rather than assuming that theoretical length extension guarantees practical performance preservation.

## ALiBi Positional Encoding

- secondary_domains: [transformer-architecture, large-language-models, context-length]
- aliases: [Attention with Linear Biases, ALiBi, linear bias positional encoding]
- broader: [positional-encoding-variants, transformer-architecture]
- related: [rotary-position-embedding, positional-encoding-variants, sliding-window-attention]
- prerequisites: [transformer-architecture, positional-encoding-variants]
- confidence: high

**definition**: ALiBi (Attention with Linear Biases) is a positional encoding approach that adds a fixed, non-learned linear bias to each attention score based on the distance between query and key positions, with the bias proportional to the negative of the distance (closer tokens receive less penalty, farther tokens receive more penalty). Unlike RoPE, ALiBi does not modify the query or key vectors and adds no parameters to the model — the positional information is injected entirely through post-softmax attention score modification. The key practical advantage of ALiBi is that models trained with it generalise substantially better to sequence lengths longer than the training length than models using learned absolute or RoPE encodings, enabling a form of length extrapolation without fine-tuning.

**key_claim**: ALiBi's length extrapolation advantage comes from the universality of the linear bias formulation — at any sequence length, the bias applied to a given query-key distance is the same as it was during training, avoiding the out-of-distribution positional encoding problem that causes RoPE and absolute encoding methods to deteriorate at lengths beyond the training maximum; empirical evaluations consistently show that ALiBi models retain higher perplexity quality at 2x–5x training length than RoPE models without any modification, though at the cost of somewhat lower in-distribution performance.

**warning**: ALiBi's linear distance penalty imposes a specific prior on attention patterns — that recency is always beneficial and distance is always a penalty — which may not be appropriate for all tasks; tasks requiring long-range dependency resolution (legal document analysis, code completion over long files) are disadvantaged by the strong linear bias against attending to distant tokens, and ALiBi's good perplexity extrapolation on language modelling does not guarantee good performance on downstream tasks requiring long-range integration at lengths beyond training.

## Flash Attention Algorithm

- secondary_domains: [hardware-aware-algorithms, deep-learning, efficient-transformers]
- aliases: [FlashAttention, IO-aware attention, memory-efficient attention]
- broader: [transformer-architecture, efficient-deep-learning]
- related: [multi-head-attention-mechanics, grouped-query-attention, flash-attention-2, context-length]
- prerequisites: [transformer-architecture, GPU-memory-hierarchy, attention-mechanisms]
- confidence: high

**definition**: FlashAttention is a hardware-aware exact attention algorithm that computes the standard scaled dot-product attention result while dramatically reducing GPU memory bandwidth usage by exploiting the memory hierarchy: rather than materialising the full $n \times n$ attention matrix in GPU HBM (high-bandwidth memory), it tiles the computation to operate on attention blocks that fit entirely in GPU SRAM (on-chip cache), computing the softmax incrementally using the numerically stable online softmax algorithm. FlashAttention produces mathematically identical outputs to standard attention but requires $O(n)$ memory for the attention matrix rather than $O(n^2)$, enabling training and inference on sequences that are 5–10x longer than standard attention allows on the same GPU hardware.

**key_claim**: FlashAttention's speedup comes not from algorithmic approximation but from IO complexity reduction — the standard attention algorithm is not compute-bound but memory-bandwidth-bound on modern GPUs because it repeatedly writes and reads the $n \times n$ attention matrix from HBM, while FlashAttention fuses all attention operations into a single CUDA kernel that reads and writes HBM only once, reducing HBM access by a factor proportional to the SRAM/HBM bandwidth ratio and achieving wall-clock speedups of 2–4x over optimised standard attention on typical sequence lengths.

**warning**: FlashAttention's compatibility guarantees cover the standard scaled dot-product attention computation, but extensions to non-standard attention variants — custom attention biases, head-specific masks, and attention sinks management — require custom FlashAttention kernel modifications rather than being automatically supported; engineers integrating FlashAttention into novel attention architectures must verify that their specific attention variant is supported by the version of FlashAttention they are using, as incompatible use can produce silent numerical errors or incorrect gradients rather than explicit errors.

## Grouped-Query Attention

- secondary_domains: [efficient-transformers, large-language-models, inference-optimisation]
- aliases: [GQA, grouped query attention heads, shared key-value heads]
- broader: [multi-head-attention-mechanics, efficient-transformers]
- related: [multi-head-attention-mechanics, flash-attention-algorithm, kv-cache, inference-optimisation]
- prerequisites: [multi-head-attention-mechanics, transformer-architecture, KV-cache]
- confidence: high

**definition**: Grouped-Query Attention (GQA) is a generalisation of multi-head attention in which multiple query heads share the same set of key and value heads, reducing the number of distinct key-value head pairs while preserving the full number of query heads. In standard MHA with h heads, there are h distinct key-value pairs; in Multi-Query Attention (MQA), all h query heads share a single key-value pair; in GQA, queries are partitioned into g groups, each sharing one key-value pair. GQA interpolates between MHA and MQA, achieving inference throughput close to MQA while maintaining generation quality close to full MHA. GQA has been adopted in Llama 2, Llama 3, Mistral, Gemma, and most other recent open-weight models due to its significant KV-cache memory reduction.

**key_claim**: GQA's primary deployment benefit is KV-cache memory reduction: the KV-cache for a transformer during inference stores all past key-value pairs for the attention computation, growing linearly with sequence length and batch size; GQA reduces KV-cache memory by a factor of h/g (typically 4–8x), enabling substantially longer sequences, larger batch sizes, or both within the same GPU memory budget, while generation quality loss relative to full MHA is consistently small enough to be preferred on quality-efficiency trade-off grounds.

**warning**: GQA's quality advantages are demonstrated primarily on long-sequence generation tasks where KV-cache bottlenecks dominate; on short-sequence tasks with small batch sizes, the quality difference between MHA and GQA is minimal and the throughput advantage is also small, meaning that GQA does not universally dominate MHA and the choice should be driven by the deployment context's specific sequence length and batch size distribution rather than adopted uncritically as a universal improvement.

## Sliding Window Attention

- secondary_domains: [efficient-transformers, long-context-modelling, large-language-models]
- aliases: [local attention, windowed attention, sliding window self-attention]
- broader: [sparse-attention-patterns, efficient-transformers]
- related: [sparse-attention-patterns, flash-attention-algorithm, attention-sinks, alibi-positional-encoding, context-length]
- prerequisites: [transformer-architecture, attention-mechanisms, efficient-deep-learning]
- confidence: high

**definition**: Sliding window attention is a local attention mechanism in which each token attends only to a fixed-size window of the most recent w tokens (and optionally a small fixed set of global tokens such as the sequence-start token), rather than attending to all previous tokens. This reduces the attention computation from $O(n^2)$ to $O(nw)$, enabling efficient processing of long sequences. Mistral 7B uses sliding window attention with window size 4096 combined with a rolling buffer KV-cache, which enables fast inference over arbitrarily long sequences by evicting old KV-cache entries while preserving the window. In stacked layers, information from beyond the window propagates via multi-layer receptive field growth, with the effective receptive field growing proportionally to the product of window size and number of layers.

**key_claim**: Sliding window attention's practical long-context capability is larger than the nominal window size suggests because the stacking of layers multiplies the effective receptive field: with window size w and l layers, a token can indirectly access information from up to $w \times l$ positions back, meaning a 4096-window 32-layer model has an effective receptive field of up to 131,072 tokens for information that has accumulated across layers, though deep-stacked information is diluted and fine-grained facts from distant tokens are less reliably accessible than facts from the immediate window.

**warning**: Sliding window attention fails on tasks that explicitly require attending to information outside the window, regardless of how many layers are stacked — questions about the very first paragraph of a very long document cannot be answered through multi-layer receptive field accumulation alone if the document's first paragraph was evicted from the window in earlier layers; hybrid attention architectures that interleave sliding window layers with full-attention layers on a sparse schedule achieve better long-context performance than pure sliding window architectures for this reason.

## Sparse Attention Patterns

- secondary_domains: [efficient-transformers, large-language-models, sequence-modelling]
- aliases: [sparse self-attention, structured sparse attention, approximate attention]
- broader: [transformer-architecture, efficient-transformers]
- narrower: [sliding-window-attention]
- related: [sliding-window-attention, flash-attention-algorithm, grouped-query-attention, attention-sinks]
- prerequisites: [transformer-architecture, attention-mechanisms, efficient-deep-learning]
- confidence: high

**definition**: Sparse attention patterns are attention mechanisms that restrict which query-key pairs can interact, computing attention only over a sparse subset of the $n^2$ possible pairs to reduce the computational complexity from $O(n^2)$ to sub-quadratic. Structured sparse attention patterns include local window patterns (each token attends to its w nearest neighbours), strided patterns (attend to every k-th token), global-local combinations (a fixed set of global tokens attends to all positions while all other tokens attend locally), and axial attention (attend along one dimension at a time in 2D data). Approximate sparse attention approaches include Longformer (window + global), BigBird (window + global + random), and Reformer (locality-sensitive hashing to approximate nearest-neighbour attention).

**key_claim**: The quality of sparse attention patterns on downstream tasks is determined by how well the sparsity pattern captures the true task-relevant attention distribution — patterns that align with the linguistic structure of the task (local for syntax, global for discourse) approximate full attention closely, while patterns that are task-agnostic (random sparsity, fixed striding) require significantly more sparse connections to match full-attention quality; this means that the best sparse attention patterns are task-adaptive rather than universal, and universal sparse patterns should be evaluated for task-specific degradation rather than assumed to be transparent substitutes for full attention.

**warning**: Sparse attention mechanisms introduce implementation complexity that can introduce subtle correctness errors — the masking logic for structured sparse patterns must correctly handle boundary conditions, padding, and causal masking simultaneously, and errors in mask construction can produce silent attention pattern violations that cause incorrect outputs without triggering exceptions; any sparse attention implementation should be verified against brute-force full-attention outputs on a range of sequence lengths, including edge cases at pattern boundaries.
