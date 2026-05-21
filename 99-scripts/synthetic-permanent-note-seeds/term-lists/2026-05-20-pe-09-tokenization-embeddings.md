---
batch_name: pe-09-tokenization-embeddings
batch_date: 2026-05-20
default_domain: nlp-tokenization
default_confidence: high
notes: |
  Seventeen concepts spanning tokenization and embedding semantics. The
  tokenization section covers the mechanics of subword tokenisation
  (BPE, vocabulary tradeoffs, whitespace effects) and its second-order
  effects on model behaviour (artifacts, boundary effects, tokenizer
  sensitivity, cross-lingual gaps). The embedding section covers the
  geometry of semantic space (text embedding models, cosine retrieval,
  embedding space geometry, late chunking) and the architectural patterns
  that produce it (sentence transformers, bi-encoder vs cross-encoder,
  Matryoshka representations, contrastive learning). Together these
  bridge the gap between raw text and the numerical substrate on which
  prompting and RAG operate.
---

# Batch: PE-09 Tokenization and Embeddings

## Byte-Pair Encoding

- domain: nlp-tokenization
- secondary_domains: [natural-language-processing, llm-tokenization, data-compression]
- aliases: [BPE, BPE tokenization, subword BPE]
- broader: [subword-tokenization]
- narrower: []
- related: [subword-tokenization, tokenization-artifacts, token-boundary-effects, vocabulary-size-tradeoffs, tokenizer-sensitivity]
- prerequisites: [natural-language-processing, language-modelling]
- confidence: high

**definition**: Byte-Pair Encoding (BPE) is a subword tokenisation algorithm originally developed for data compression that was adapted for use in neural machine translation and has since become the dominant tokenisation strategy for large language models. BPE starts with a vocabulary of individual characters (or bytes) and iteratively merges the most frequent pair of adjacent tokens in the training corpus, continuing until the vocabulary reaches a target size. The result is a vocabulary of frequent words, common morphemes, and rare character sequences, allowing the model to represent both common words as single tokens and novel or rare words as decomposed subword sequences.

**key_claim**: BPE achieves the optimal practical tradeoff between vocabulary size and the ability to represent arbitrary text by encoding frequent patterns efficiently as single tokens while retaining the ability to decompose unknown words into interpretable subword units — this property is what allows a fixed vocabulary to handle open-ended natural language without explicit out-of-vocabulary handling.

**warning**: BPE tokenisation is language and domain sensitive — a vocabulary trained on English text will over-segment text from morphologically rich languages, code, or technical domains, increasing token counts and degrading model performance on those domains even for a model with sufficient parameters to handle the content.

## Tokenization Artifacts

- domain: nlp-tokenization
- secondary_domains: [natural-language-processing, llm-reasoning]
- aliases: [tokenisation artifacts, tokenizer quirks, tokenization side effects]
- broader: [tokenization, subword-tokenization]
- narrower: []
- related: [byte-pair-encoding, token-boundary-effects, tokenizer-sensitivity, whitespace-token-effects]
- prerequisites: [byte-pair-encoding, subword-tokenization]
- confidence: high

**definition**: Tokenization Artifacts are systematic errors and failure modes in language model behaviour that originate from the tokenisation process rather than from limitations in the model's knowledge or reasoning. Examples include: models that fail to reverse strings or count characters because they operate on token sequences rather than character sequences; models that struggle with words split across unexpected token boundaries (e.g., "token" + "isation" vs "tokenisation"); models that behave differently on semantically equivalent text that tokenises differently; and models that exhibit sensitivity to leading/trailing whitespace because it changes token boundaries.

**key_claim**: Tokenization artifacts demonstrate that language models do not process language the way humans do — many apparent "reasoning failures" are actually tokenisation failures where the model's inability to solve a character-level task (e.g., anagram detection, syllable counting) reflects the fact that its input representation never contained character-level information, not that it lacks the underlying reasoning capability.

**warning**: Tokenization artifacts are stable across model scales — scaling up a model trained on BPE-tokenised text does not eliminate artifacts caused by the tokenisation scheme; only changing the tokenisation method or training a model with character-aware representations addresses the root cause.

## Token Boundary Effects

- domain: nlp-tokenization
- secondary_domains: [natural-language-processing, llm-reasoning, prompt-engineering]
- aliases: [tokenization boundary effects, subword boundary effects, segmentation effects]
- broader: [tokenization-artifacts, subword-tokenization]
- narrower: []
- related: [tokenization-artifacts, byte-pair-encoding, tokenizer-sensitivity, whitespace-token-effects]
- prerequisites: [byte-pair-encoding, tokenization-artifacts]
- confidence: high

**definition**: Token Boundary Effects are a class of tokenization artifact in which the precise location of subword boundaries affects model behaviour in ways that are not semantically motivated. When a word is split at different positions depending on context (e.g., whether it appears at the start of a sentence vs. after a space), the model may produce different outputs for semantically identical inputs. Token boundary effects are particularly pronounced for: numbers and arithmetic, where digit groupings affect computation; names, where capitalisation changes tokenisation; code, where indentation and punctuation create boundary shifts; and multilingual text, where cross-lingual tokenisation is often inconsistent.

**key_claim**: Token boundary effects reveal that the apparent compositional structure that LLMs display in their outputs is partly an artefact of token boundaries rather than genuine syntactic or semantic decomposition — because the model processes token-level representations, its "understanding" of word structure is shaped by the tokeniser's segmentation decisions in ways that can be exploited or inadvertently triggered.

**warning**: Token boundary effects are difficult to detect through standard benchmark evaluation because most benchmarks were designed assuming character- or word-level processing — a model may appear competent on the benchmark while systematically failing on inputs that happen to trigger pathological tokenisation boundaries, creating a hidden reliability gap.

## Vocabulary Size Tradeoffs

- domain: nlp-tokenization
- secondary_domains: [natural-language-processing, llm-architecture, resource-efficient-ai]
- aliases: [tokenizer vocabulary size, vocab tradeoffs, vocabulary selection]
- broader: [subword-tokenization, llm-architecture]
- narrower: []
- related: [byte-pair-encoding, subword-tokenization, cross-lingual-tokenization, tokenization-artifacts]
- prerequisites: [byte-pair-encoding, language-modelling]
- confidence: high

**definition**: Vocabulary Size Tradeoffs refers to the design tension in choosing the number of distinct tokens in a language model's vocabulary. A larger vocabulary means more frequent words and phrases are encoded as single tokens (shorter sequences, less compute per token, better handling of rare morphemes), but it also increases the size of the embedding matrix and the output projection layer, adds parameters that are hard to train for rare tokens, and may harm low-frequency token representations. A smaller vocabulary produces shorter models but longer token sequences with more cross-attention cost and greater sensitivity to token boundary effects.

**key_claim**: Vocabulary size is a fundamental architectural decision that propagates through training efficiency, inference cost, cross-lingual coverage, and model size — most large models converge on vocabularies of 32,000–128,000 tokens as an empirical sweet spot, but optimal vocabulary size depends critically on the target languages and domains, with larger multilingual models requiring larger vocabularies.

**warning**: Vocabulary size alone does not determine tokenisation quality — a large vocabulary trained on a biased corpus will encode that bias, over-representing some languages and underrepresenting others, and the training procedure (BPE vs. Unigram vs. WordPiece) interacts with vocabulary size in non-obvious ways that make cross-method comparison difficult.

## Subword Tokenization

- domain: nlp-tokenization
- secondary_domains: [natural-language-processing, language-modelling]
- aliases: [subword segmentation, subword encoding, subword-based tokenisation]
- broader: [tokenization]
- narrower: [byte-pair-encoding, wordpiece, unigram-language-model-tokenization]
- related: [byte-pair-encoding, vocabulary-size-tradeoffs, tokenizer-sensitivity, cross-lingual-tokenization]
- prerequisites: [language-modelling, natural-language-processing]
- confidence: high

**definition**: Subword Tokenization is the class of text segmentation methods that split text into units smaller than words but larger than individual characters — subword units that balance the expressiveness of word-level representations with the open-vocabulary coverage of character-level models. The three dominant subword methods are Byte-Pair Encoding (BPE), which greedily merges frequent pairs; WordPiece, which maximises likelihood under a language model and uses a ## prefix for continuation tokens; and Unigram, which trains a probabilistic model and prunes the vocabulary to maximise the likelihood of the corpus. All three methods produce a segmentation that encodes frequency information about the training corpus.

**key_claim**: Subword tokenization solved the fundamental open-vocabulary problem in neural language modelling — prior character-level models were slow due to long sequences and prior word-level models failed on unseen words, while subword methods achieve efficient sequence lengths with full coverage of the character set, enabling the scaling that produced modern LLMs.

**warning**: Subword tokenization is not language-neutral — methods trained on data with heavy English bias will tokenise English words into single tokens while tokenising equivalent concepts in other languages into many tokens, producing systematic disparities in the computational resources and context-window space available to different languages, which can compound into performance gaps for non-English speakers.

## Tokenizer Sensitivity

- domain: nlp-tokenization
- secondary_domains: [prompt-engineering, llm-reliability, robustness]
- aliases: [tokenization sensitivity, prompt tokenization sensitivity, tokenizer brittleness]
- broader: [tokenization-artifacts, robustness-in-llms]
- narrower: []
- related: [tokenization-artifacts, token-boundary-effects, whitespace-token-effects, prompt-sensitivity-analysis]
- prerequisites: [byte-pair-encoding, subword-tokenization, prompt-sensitivity-analysis]
- confidence: high

**definition**: Tokenizer Sensitivity refers to the phenomenon where semantically equivalent or near-equivalent prompt formulations that tokenize differently produce significantly different model outputs. Because a language model's input is a sequence of token IDs rather than raw text, two prompts that differ only in surface form (e.g., capitalisation, whitespace, punctuation, equivalent phrasings) can produce token sequences that look structurally different to the model, activating different patterns and producing divergent responses. This is a form of distributional sensitivity that is distinct from the model's semantic uncertainty.

**key_claim**: Tokenizer sensitivity is a fundamental reliability concern for production LLM deployments because it means that the model's behaviour cannot be fully characterised by the semantic content of prompts alone — surface-level variation that would be irrelevant to a human reader can trigger qualitatively different outputs, making the system harder to test, validate, and trust.

**warning**: Tokenizer sensitivity is not uniformly reduced by scaling — larger models exhibit different patterns of tokenizer sensitivity rather than necessarily lower overall sensitivity, and for certain types of sensitivity (e.g., capitalisation effects in code models), larger models can be more sensitive because they have learned more precise associations between specific token patterns and their semantic contexts.

## Cross-Lingual Tokenization

- domain: nlp-tokenization
- secondary_domains: [multilingual-nlp, language-modelling, natural-language-processing]
- aliases: [multilingual tokenization, cross-lingual segmentation, multilingual vocabulary]
- broader: [subword-tokenization, multilingual-nlp]
- narrower: []
- related: [subword-tokenization, byte-pair-encoding, vocabulary-size-tradeoffs, tokenizer-sensitivity]
- prerequisites: [subword-tokenization, multilingual-nlp]
- confidence: high

**definition**: Cross-Lingual Tokenization refers to the design of tokenisation vocabularies and algorithms that serve multiple languages within a single model, and to the study of how tokenisation choices affect cross-lingual transfer, model performance, and computational equity across languages. Multilingual models like mBERT, XLM-R, and multilingual LLaMA use a shared vocabulary trained on multilingual corpora, but the distribution of vocabulary tokens across languages is rarely proportional to language use, producing token-count disparities where a concept expressed in a single English token requires many tokens in other languages, consuming more context window and compute.

**key_claim**: Cross-lingual tokenization inequity is a systematic source of multilingual model performance gaps — languages that are tokenised less efficiently (more tokens per character) have less effective context window capacity per semantic unit and face higher computational costs per query, meaning that surface-level parameter equality between languages in a multilingual model masks deep computational inequality in practice.

**warning**: Fixing cross-lingual tokenization inequity by increasing vocabulary size alone is insufficient without also addressing the data distribution used for vocabulary training — a larger vocabulary trained on an unbalanced multilingual corpus will still over-represent high-resource languages, because the merge or likelihood-based tokenisation procedures optimise for the most frequent patterns in the training data.

## Whitespace Token Effects

- domain: nlp-tokenization
- secondary_domains: [prompt-engineering, llm-reliability, tokenization-artifacts]
- aliases: [whitespace tokenization, leading whitespace effects, tokenizer whitespace sensitivity]
- broader: [tokenization-artifacts, tokenizer-sensitivity]
- narrower: []
- related: [tokenization-artifacts, token-boundary-effects, tokenizer-sensitivity, byte-pair-encoding]
- prerequisites: [byte-pair-encoding, tokenization-artifacts]
- confidence: high

**definition**: Whitespace Token Effects are a specific class of tokenization artifact caused by the fact that most BPE-based tokenizers treat leading whitespace as part of a token — a word preceded by a space tokenizes differently than the same word at the start of a string or after a special token. This means that prompts with subtle whitespace differences can produce different token sequences and different model outputs. Common manifestations include: differences in model behaviour when the user prompt has a leading space vs. no leading space; different tokenisations of words appearing after punctuation vs. spaces; and inconsistencies in how code models handle indentation.

**key_claim**: Whitespace token effects create a hidden input-sensitivity that affects prompt engineering reliability — prompts that appear visually identical but differ in invisible whitespace characters can produce measurably different outputs, and this sensitivity is especially pronounced for the first token after a system-prompt boundary or role separator.

**warning**: Whitespace token effects are trivially exploitable as a prompt injection or evaluation manipulation vector — an adversary who controls input text can manipulate tokenisation to shift the model into a different behavioural regime by inserting or removing whitespace characters at strategic positions, making whitespace normalisation a necessary preprocessing step in security-sensitive deployments.

## Text Embedding Models

- domain: embeddings-and-semantic-space
- secondary_domains: [natural-language-processing, retrieval-augmented-generation, semantic-search]
- aliases: [sentence embeddings, text encoders, embedding models, dense representations]
- broader: [representation-learning, natural-language-processing]
- narrower: [sentence-transformers, bi-encoder-vs-cross-encoder]
- related: [sentence-transformers, cosine-similarity-retrieval, embedding-space-geometry, retrieval-augmented-generation, dense-passage-retrieval]
- prerequisites: [neural-networks, natural-language-processing, transformer-attention-mechanism]
- confidence: high

**definition**: Text Embedding Models are neural networks that encode text (words, sentences, passages, or documents) as dense vector representations in a continuous high-dimensional space, such that semantically similar texts are mapped to nearby vectors while dissimilar texts are mapped to distant vectors. These models are trained using contrastive objectives that pull similar pairs together and push dissimilar pairs apart, typically using large corpora of (query, relevant passage) pairs or natural language inference datasets. The resulting embeddings support downstream tasks including semantic search, duplicate detection, clustering, and cross-modal retrieval.

**key_claim**: Text embedding models transform the retrieval problem from a sparse lexical matching problem (keyword overlap) into a dense semantic matching problem (geometric proximity in a learned space), enabling retrieval of semantically related content that shares no keywords — which is the core technical enabler of modern RAG systems and semantic search engines.

**warning**: Text embedding models have a fundamental context length limitation — most models encode text through pooling of transformer outputs, meaning that longer documents are compressed into a fixed-size vector at a cost of information loss, and embedding a 10,000-word document into the same dimensionality as a 10-word sentence necessarily loses fine-grained detail that may be critical for precision retrieval.

## Semantic Similarity in Prompts

- domain: embeddings-and-semantic-space
- secondary_domains: [prompt-engineering, retrieval-augmented-generation, in-context-learning]
- aliases: [prompt semantic similarity, embedding-based prompt selection, similarity-based retrieval for prompts]
- broader: [in-context-learning, retrieval-augmented-generation, text-embedding-models]
- narrower: []
- related: [text-embedding-models, cosine-similarity-retrieval, retrieval-augmented-few-shot, few-shot-example-selection, dense-passage-retrieval]
- prerequisites: [text-embedding-models, cosine-similarity-retrieval, few-shot-prompting]
- confidence: high

**definition**: Semantic Similarity in Prompts refers to the use of embedding-based similarity measures to select, rank, or retrieve content for inclusion in prompts — including few-shot examples, retrieved passages, and context documents — based on their semantic proximity to the current query or task. Rather than selecting examples by hand or at random, semantic similarity retrieval uses a text embedding model to find examples that are closest in meaning to the current input, exploiting the finding that few-shot examples semantically similar to the test instance produce better performance than random examples. This approach is fundamental to retrieval-augmented few-shot prompting and RAG system design.

**key_claim**: Semantically similar few-shot examples consistently outperform random or hand-crafted fixed examples across diverse tasks, because the semantic proximity between example and test instance reduces the distribution gap the model must bridge — effectively narrowing the task scope within the context window to the specific sub-domain most relevant to the current query.

**warning**: Semantic similarity retrieval can introduce a feedback loop in which examples that are too similar to the test instance cause the model to copy surface patterns rather than reason about the underlying task, and in adversarial settings, a retrieval corpus that has been poisoned with adversarially crafted documents can steer the model's behaviour by exploiting the assumption that retrieved documents are relevant and trustworthy.

## Cosine Similarity Retrieval

- domain: embeddings-and-semantic-space
- secondary_domains: [information-retrieval, retrieval-augmented-generation, linear-algebra]
- aliases: [cosine distance search, cosine similarity search, cosine nearest-neighbour retrieval]
- broader: [text-embedding-models, information-retrieval]
- narrower: []
- related: [text-embedding-models, embedding-space-geometry, dense-passage-retrieval, approximate-nearest-neighbour]
- prerequisites: [linear-algebra, text-embedding-models]
- confidence: high

**definition**: Cosine Similarity Retrieval is the most common approach to finding semantically similar texts in an embedding space, using the cosine of the angle between two embedding vectors as the similarity metric. Cosine similarity measures directional alignment rather than magnitude — two embeddings that point in the same direction are considered similar regardless of their absolute norms — which makes it robust to differences in vector magnitude that arise from variable-length input texts. In practice, cosine retrieval is implemented through approximate nearest-neighbour (ANN) algorithms (FAISS, ScaNN, HNSW) that scale to billions of vectors by trading small amounts of recall for large gains in query speed.

**key_claim**: Cosine similarity is the appropriate metric for retrieval over normalised embedding spaces because it measures semantic direction (what the text is *about*) rather than magnitude (how much text there is) — in embedding models trained with contrastive objectives, the semantic content of a passage is encoded in the direction of its embedding vector, making cosine the natural similarity measure.

**warning**: Cosine similarity assumes that the embedding space is approximately isotropic — that all directions carry equal semantic signal — but in practice embedding spaces are highly anisotropic, with certain directions encoding generic frequency information rather than semantics, which means that cosine retrieval can surface many high-scoring but semantically irrelevant results when queries are in low-information-density regions of the embedding space.

## Embedding Space Geometry

- domain: embeddings-and-semantic-space
- secondary_domains: [representation-learning, nlp, linear-algebra]
- aliases: [semantic space geometry, representation space geometry, latent space structure]
- broader: [text-embedding-models, representation-learning]
- narrower: []
- related: [text-embedding-models, cosine-similarity-retrieval, matryoshka-representation-learning, contrastive-learning-embeddings, superposition-hypothesis]
- prerequisites: [text-embedding-models, linear-algebra, representation-learning]
- confidence: high

**definition**: Embedding Space Geometry refers to the structural properties of the high-dimensional vector spaces produced by text embedding models — the patterns, regularities, and pathologies that shape how semantic relationships are encoded. Key geometric phenomena include: linear analogy structure (king - man + woman ≈ queen), anisotropy (embeddings cluster in a narrow cone rather than filling the space uniformly), isotropy failure (the average cosine similarity between random pairs is high rather than near zero), neighbourhood structure (whether the space supports meaningful k-nearest-neighbour retrieval), and the geometry of subspaces corresponding to specific semantic dimensions.

**key_claim**: Embedding space geometry determines the practical utility of embedding-based retrieval more than any individual model's benchmark scores — an embedding space that is anisotropic or that does not separate semantically distinct concepts into well-defined neighbourhoods will produce poor retrieval quality regardless of the model's performance on static evaluation datasets.

**warning**: Common embedding space pathologies — high anisotropy, collapsed representations, and poor isotropy — are often invisible in standard embedding benchmarks that measure pairwise similarity on curated datasets, but they manifest as degraded retrieval quality on real-world query distributions, meaning that benchmark scores are insufficient proxies for production retrieval quality.

## Late Chunking

- domain: embeddings-and-semantic-space
- secondary_domains: [retrieval-augmented-generation, text-embedding-models, information-retrieval]
- aliases: [late interaction chunking, contextual chunking, jina late chunking]
- broader: [chunking-strategies, text-embedding-models]
- narrower: []
- related: [text-embedding-models, cosine-similarity-retrieval, retrieval-augmented-generation, chunking-strategies, long-context-prompting-strategies]
- prerequisites: [text-embedding-models, retrieval-augmented-generation]
- confidence: high

**definition**: Late Chunking is a text embedding strategy in which long-form documents are first encoded in full by a long-context embedding model, so that each token receives a contextually-informed representation from the entire document, and then the token-level embeddings are mean-pooled within the boundaries of the desired chunks to produce chunk-level embeddings. This contrasts with early chunking, where the document is split into chunks before encoding, so each chunk's embedding is computed without access to context from other parts of the document. Late chunking retains cross-chunk contextual information in the resulting chunk embeddings.

**key_claim**: Late chunking addresses the core limitation of early chunking — that context boundaries cut off information that the embedding model would use to resolve coreference, disambiguate terms, and represent discourse structure — by ensuring that each chunk's embedding is informed by the full document before pooling, producing embeddings that more faithfully represent what a chunk means in context.

**warning**: Late chunking requires a long-context embedding model capable of processing the full document in a single forward pass, which limits its applicability to documents within the model's context window and is computationally more expensive than early chunking — it also does not help for retrieval across documents, where the full inter-document context is not available during encoding.

## Sentence Transformers

- domain: embeddings-and-semantic-space
- secondary_domains: [natural-language-processing, text-embedding-models, semantic-search]
- aliases: [SBERT, Sentence-BERT, sentence encoder, bi-encoder sentence embedding]
- broader: [text-embedding-models]
- narrower: []
- related: [text-embedding-models, bi-encoder-vs-cross-encoder, contrastive-learning-embeddings, semantic-similarity-in-prompts, cosine-similarity-retrieval]
- prerequisites: [transformer-attention-mechanism, text-embedding-models]
- confidence: high

**definition**: Sentence Transformers (SBERT) are transformer-based models fine-tuned to produce semantically meaningful fixed-size embeddings for sentences and paragraphs, using a siamese or triplet network architecture to train the model on sentence-pair tasks (semantic textual similarity, natural language inference). The key innovation of the original SBERT paper (Reimers and Gurevych, 2019) was demonstrating that standard BERT, when used for semantic similarity by computing similarity between [CLS] representations, was orders of magnitude slower for pairwise comparison than necessary — and that fine-tuning with a siamese structure produced embeddings that could be compared with cosine similarity at inference time, enabling scalable semantic search.

**key_claim**: Sentence Transformers solved the practical scalability problem of semantic search with BERT-class models — by producing embeddings that can be indexed once and searched offline rather than requiring a full cross-encoder forward pass per query-document pair, they reduced the cost of semantic retrieval from O(n) forward passes per query to a single embedding plus a vector search, making it economically viable at scale.

**warning**: Sentence Transformer models are highly sensitive to the domain and the nature of the sentence-pair tasks used for fine-tuning — an SBERT model trained on NLI and STS may produce poor embeddings for specialised domains (e.g., legal text, biomedical literature, code) where the semantic relationships differ structurally from the fine-tuning distribution.

## Bi-Encoder vs Cross-Encoder

- domain: embeddings-and-semantic-space
- secondary_domains: [information-retrieval, natural-language-processing, semantic-search]
- aliases: [dual encoder vs cross encoder, bi-encoder architecture, cross-encoder reranking]
- broader: [text-embedding-models, information-retrieval]
- narrower: []
- related: [sentence-transformers, text-embedding-models, dense-passage-retrieval, cosine-similarity-retrieval]
- prerequisites: [transformer-attention-mechanism, text-embedding-models, sentence-transformers]
- confidence: high

**definition**: The Bi-Encoder vs Cross-Encoder distinction describes two architectural approaches to computing relevance between a query and a document. A bi-encoder encodes query and document independently into separate embeddings and computes their similarity using a lightweight function (typically cosine similarity); it is efficient because document embeddings can be pre-computed and indexed. A cross-encoder encodes the concatenated (query, document) pair in a single forward pass, allowing full attention between query and document tokens; it is more accurate because it models their interaction directly but is too slow for first-stage retrieval over large corpora. In production systems, bi-encoders are used for retrieval and cross-encoders for re-ranking.

**key_claim**: The bi-encoder/cross-encoder hybrid architecture — retrieve with bi-encoder, rerank with cross-encoder — is the standard production pattern for neural retrieval because it optimally separates the tasks that each architecture is suited for: bi-encoders provide the scalability needed to search millions of documents, while cross-encoders provide the precision needed to order the top candidates after the search space has been narrowed.

**warning**: The quality gap between bi-encoder and cross-encoder relevance scoring is substantial for queries that require understanding fine-grained semantic dependencies between query and document — for such queries, using a bi-encoder without reranking significantly degrades precision, and the number of candidates passed to the cross-encoder (the "top-k") is a critical hyperparameter that trades off quality against latency.

## Matryoshka Representation Learning

- domain: embeddings-and-semantic-space
- secondary_domains: [representation-learning, text-embedding-models, information-retrieval]
- aliases: [MRL, Matryoshka embeddings, nested representations, variable-size embeddings]
- broader: [text-embedding-models, representation-learning]
- narrower: []
- related: [text-embedding-models, embedding-space-geometry, cosine-similarity-retrieval, late-chunking]
- prerequisites: [text-embedding-models, representation-learning]
- confidence: high

**definition**: Matryoshka Representation Learning (MRL) is a training paradigm for producing embedding models that encode information in a nested, hierarchical manner across dimensions, such that truncating the embedding vector to a smaller dimension still yields a useful and coherent representation. Named after Russian nesting dolls (Matryoshka), MRL trains the model with a loss that simultaneously optimises multiple dimensionality checkpoints — e.g., the first 64, 128, 256, 512, 1024, and 2048 dimensions all independently encode task-relevant information — so that the first d dimensions always form a complete embedding at that resolution.

**key_claim**: Matryoshka embeddings provide a practical solution to the storage and compute cost tradeoffs in large-scale retrieval — by training a single model that supports multiple embedding sizes, MRL allows operators to choose the dimensionality that satisfies their latency and storage budget without retraining, and empirically produces embeddings where truncation to 2× smaller dimensionality loses only 1–5% of retrieval quality.

**warning**: Matryoshka representations are not equally structured at all dimensionalities — the information in earlier dimensions is selected by the training loss to be the most task-relevant information, but what "most relevant" means depends on the training task, meaning that MRL embeddings used for a different downstream task than their training objective may not have the most useful information concentrated in the first d dimensions.

## Contrastive Learning Embeddings

- domain: embeddings-and-semantic-space
- secondary_domains: [representation-learning, text-embedding-models, self-supervised-learning]
- aliases: [contrastive representation learning, SimCSE, InfoNCE training, contrastive sentence embeddings]
- broader: [representation-learning, self-supervised-learning]
- narrower: []
- related: [text-embedding-models, sentence-transformers, matryoshka-representation-learning, embedding-space-geometry]
- prerequisites: [representation-learning, neural-networks, text-embedding-models]
- confidence: high

**definition**: Contrastive Learning for Embeddings is a training paradigm in which an embedding model is trained to map similar inputs to nearby vectors and dissimilar inputs to distant vectors, using a loss function that contrasts positive pairs (similar inputs, ideally sharing the same meaning) against negative pairs (dissimilar inputs or in-batch random samples). Seminal approaches include SimCSE (which uses dropout as a data augmentation to create positive pairs from a single sentence), InfoNCE (which maximises mutual information between positive pairs), and supervised contrastive learning (which uses human-labelled semantic similarity as the positive/negative signal).

**key_claim**: Contrastive learning is the dominant training paradigm for text embedding models because it directly optimises the geometric property that makes embeddings useful for retrieval — the separation of similar and dissimilar texts in the embedding space — without requiring intermediate supervision signals like pairwise similarity scores, enabling effective training from large unsupervised corpora.

**warning**: Contrastive learning is highly sensitive to the quality and construction of the negative samples — easy negatives (random sentences) produce embeddings that cannot distinguish subtle semantic differences, while false negatives (pairs that are labelled dissimilar but are actually semantically related) actively harm embedding quality, making negative mining strategy a critical hyperparameter with large practical impact on downstream retrieval quality.
