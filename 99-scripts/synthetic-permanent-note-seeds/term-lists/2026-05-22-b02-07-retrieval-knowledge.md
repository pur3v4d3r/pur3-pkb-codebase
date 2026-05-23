---
batch_name: b02-07-retrieval-knowledge
batch_date: 2026-05-22
default_domain: retrieval-augmented-generation
default_confidence: high
notes: |
  Fifteen concepts covering retrieval-augmented generation and knowledge
  integration. Spans dense retrieval, sparse retrieval (BM25), hybrid
  retrieval, query rewriting, iterative retrieval, Self-RAG, Corrective
  RAG, Adaptive RAG, late interaction retrieval, cross-encoder reranking,
  reciprocal rank fusion, chunking strategies, embedding model selection,
  retrieval faithfulness, and knowledge conflict handling. Batch 02 of the
  prompt-engineering and LLM series.
---

# Batch: B02-07 Retrieval and Knowledge Integration

## Dense Retrieval for RAG

- secondary_domains: [information-retrieval, vector-databases, large-language-models]
- aliases: [neural retrieval, embedding-based retrieval, vector retrieval for RAG, dense passage retrieval]
- broader: [retrieval-augmented-generation, information-retrieval]
- narrower: [embedding-model-selection, late-interaction-retrieval]
- related: [sparse-retrieval-bm25, hybrid-retrieval-patterns, embedding-model-selection, cross-encoder-reranking]
- prerequisites: [information-retrieval, vector-embeddings, retrieval-augmented-generation]
- confidence: high

**definition**: Dense retrieval for RAG is an information retrieval approach in which documents and queries are encoded into dense vector representations using a neural encoder model, and retrieval is performed by maximum inner product search (MIPS) or approximate nearest-neighbour search (ANN) in the embedding space. Unlike sparse retrieval methods that rely on lexical term matching, dense retrieval captures semantic similarity — a document about "heart attack" will be retrieved for the query "myocardial infarction" because their embeddings are close in vector space even though they share no lexical terms. In RAG systems, dense retrieval is the primary mechanism for finding semantically relevant context documents for a given user query, and its quality is the primary determinant of the RAG system's ability to answer semantically complex questions.

**key_claim**: Dense retrieval for RAG is superior to sparse retrieval for semantically complex queries but inferior for exact-match queries (entity names, technical terms, product codes) where the embedding similarity metric provides weaker signal than lexical matching — the optimal RAG retrieval system combines dense and sparse retrieval in a hybrid architecture rather than selecting either approach exclusively, achieving dense retrieval's semantic coverage while retaining sparse retrieval's precision for exact-match queries.

**warning**: Dense retrieval quality depends critically on the alignment between the query distribution and the embedding model's training distribution — embedding models trained on generic web text produce lower-quality retrievals for domain-specific corpora (medical literature, legal documents, scientific papers) than models specifically fine-tuned on in-domain query-document pairs; deploying a generic embedding model for domain-specific RAG without domain adaptation evaluation is a common cause of RAG retrieval quality failures that are misattributed to the generation component.

## Sparse Retrieval BM25

- secondary_domains: [information-retrieval, term-weighting, large-language-models]
- aliases: [BM25 retrieval, TF-IDF retrieval, lexical retrieval, bag-of-words retrieval]
- broader: [retrieval-augmented-generation, information-retrieval]
- related: [dense-retrieval-for-rag, hybrid-retrieval-patterns, query-rewriting-for-retrieval]
- prerequisites: [information-retrieval, tf-idf, retrieval-augmented-generation]
- confidence: high

**definition**: Sparse retrieval with BM25 (Best Match 25) is an information retrieval method based on term frequency-inverse document frequency (TF-IDF) statistics, augmented with document length normalisation. BM25 scores documents by the TF-IDF relevance of the query terms that appear in the document, with diminishing returns for term frequency and normalisation for document length, and has been the dominant lexical retrieval baseline in information retrieval for decades. In RAG systems, BM25 serves as either the primary retrieval mechanism (in resource-constrained or latency-sensitive deployments) or as a component in hybrid retrieval systems where its lexical matching precision complements the semantic coverage of dense retrieval.

**key_claim**: BM25 remains a competitive baseline for RAG retrieval on tasks where queries contain specific technical terms, proper nouns, or exact phrases that need to be matched in retrieved documents — dense retrieval systems consistently underperform BM25 on these query types because the embedding space collapses lexically distinct but topically related terms into similar representations, while BM25's exact term matching provides precision that dense retrieval cannot; this failure mode is particularly pronounced for queries about rare entities or domain-specific terminology not well-represented in the embedding model's training data.

**warning**: BM25 retrieval for RAG requires effective document tokenisation and preprocessing to achieve its stated performance — poor tokenisation choices (failing to handle compound words, technical notation, or domain-specific abbreviations) significantly degrade BM25 performance, and the stopword lists and stemming algorithms from general information retrieval settings may be inappropriate for domain-specific corpora; BM25 performance should be validated specifically on the target domain corpus rather than assumed to match published benchmarks from general-domain evaluations.

## Hybrid Retrieval Patterns

- secondary_domains: [information-retrieval, retrieval-augmented-generation, search-systems]
- aliases: [hybrid search, combined retrieval, sparse-dense retrieval fusion]
- broader: [retrieval-augmented-generation, information-retrieval]
- related: [dense-retrieval-for-rag, sparse-retrieval-bm25, reciprocal-rank-fusion, cross-encoder-reranking]
- prerequisites: [dense-retrieval-for-rag, sparse-retrieval-bm25, information-retrieval]
- confidence: high

**definition**: Hybrid retrieval patterns in RAG systems combine dense (semantic embedding-based) and sparse (lexical term-matching) retrieval to leverage the complementary strengths of each approach. The core pattern involves retrieving candidate documents independently using both dense and sparse retrieval systems, then fusing the retrieved sets using a score combination or rank fusion method (such as Reciprocal Rank Fusion or weighted score combination) to produce a final ranked set of documents for the generator. Hybrid retrieval addresses the well-documented failure modes of each component in isolation: dense retrieval's weakness on exact-match queries and sparse retrieval's weakness on semantically similar but lexically different queries.

**key_claim**: Hybrid retrieval consistently outperforms either dense or sparse retrieval alone on diverse query sets, with the largest gains occurring on queries that require both semantic understanding and exact lexical matching — the complementarity between dense and sparse retrieval is not a niche advantage but a fundamental property of real-world query distributions, which contain both semantically-expressed and term-specific information needs; the performance improvement from hybridisation typically ranges from 5–15% recall@10, large enough to meaningfully impact RAG answer quality.

**warning**: Hybrid retrieval introduces additional complexity in index management, query latency, and system maintenance — maintaining two separate retrieval indices (vector index and inverted index), computing two sets of retrieval results per query, and applying score fusion adds operational overhead that may be prohibitive in latency-sensitive or resource-constrained deployments; the decision to implement hybrid retrieval should be based on measured retrieval quality improvement on the specific target query distribution, not on the assumption that hybrid always outperforms single-modality retrieval for the deployment context.

## Query Rewriting for Retrieval

- secondary_domains: [information-retrieval, prompt-engineering, retrieval-augmented-generation]
- aliases: [query reformulation, query expansion for RAG, retrieval-oriented query rewriting]
- broader: [retrieval-augmented-generation, information-retrieval]
- related: [iterative-retrieval-augmentation, hybrid-retrieval-patterns, dense-retrieval-for-rag]
- prerequisites: [retrieval-augmented-generation, information-retrieval, prompt-engineering]
- confidence: high

**definition**: Query rewriting for retrieval is the process of transforming a user's original query into a form more suitable for retrieving relevant documents, using an LLM to expand, rephrase, decompose, or augment the query based on knowledge of what makes queries retrieval-friendly. Rewriting strategies include: HyDE (Hypothetical Document Embeddings — generating a hypothetical answer document and using its embedding for retrieval), multi-query expansion (generating multiple paraphrases of the query and retrieving for each), step-back prompting (rephrasing the specific query as a more general question to retrieve background knowledge), and query decomposition (splitting complex multi-hop queries into sequential simpler subqueries). Query rewriting addresses the vocabulary mismatch between user queries and document language.

**key_claim**: Query rewriting via HyDE provides the largest retrieval quality improvement for knowledge-intensive questions where the user's query vocabulary differs substantially from the vocabulary of relevant documents — generating a hypothetical answer to the query and retrieving documents similar to that answer rather than to the raw query aligns the retrieval distribution with document language, and the improvement is largest for the queries where vocabulary mismatch is most severe (queries using lay terminology to ask about technical concepts).

**warning**: Query rewriting introduces latency overhead (requiring an additional LLM call before retrieval) and hallucination risk (the hypothetical document or paraphrase generated by the rewriter may introduce incorrect terms that retrieve irrelevant documents) — rewriting strategies that generate incorrect hypothetical content can actively degrade retrieval quality relative to no rewriting, particularly for queries where the LLM's knowledge of the topic is limited; query rewriting effectiveness should be validated on the specific query distribution before deploying as a standard pre-retrieval step.

## Iterative Retrieval Augmentation

- secondary_domains: [retrieval-augmented-generation, multi-step-reasoning, large-language-models]
- aliases: [iterative RAG, multi-hop retrieval, sequential retrieval augmentation]
- broader: [retrieval-augmented-generation, reasoning]
- related: [self-rag-selective-retrieval, corrective-rag-pipeline, adaptive-rag-routing, query-rewriting-for-retrieval]
- prerequisites: [retrieval-augmented-generation, multi-hop-reasoning, large-language-models]
- confidence: high

**definition**: Iterative retrieval augmentation is a RAG architecture in which retrieval and generation are interleaved in multiple rounds rather than executing retrieval once before generation. In each iteration, the model uses its current partial answer or reasoning state to formulate a retrieval query, retrieves relevant documents, incorporates the retrieved information into its reasoning, and either produces a final answer or identifies that further retrieval is needed. Iterative retrieval is essential for multi-hop questions that require assembling information from multiple documents where the second retrieval query depends on information found in the first retrieval.

**key_claim**: Iterative retrieval augmentation qualitatively changes the class of questions a RAG system can answer compared to single-retrieval architectures — single-retrieval RAG answers questions whose answer is explicitly stated in a single document, while iterative retrieval answers multi-hop questions that require chaining information across documents, comparisons between entities from different documents, and reasoning tasks that require gathering distributed facts, enabling RAG to handle the full complexity range of knowledge-intensive question answering rather than only single-document lookup questions.

**warning**: Iterative retrieval augmentation multiplies latency and API costs by the number of retrieval iterations, which can be significant for complex multi-hop queries requiring 3–5 iterations with LLM reranking at each step; the latency budget must be assessed for the deployment context, and fallback strategies (maximum iterations, early stopping when confidence is high) must be implemented to prevent unbounded inference time; production iterative RAG systems should expose iteration count and intermediate retrieval results for debugging and monitoring purposes.

## Self-RAG Selective Retrieval

- secondary_domains: [retrieval-augmented-generation, large-language-models, adaptive-inference]
- aliases: [Self-RAG, adaptive retrieval, on-demand retrieval, retrieval-on-demand]
- broader: [retrieval-augmented-generation, adaptive-rag-routing]
- related: [adaptive-rag-routing, corrective-rag-pipeline, iterative-retrieval-augmentation]
- prerequisites: [retrieval-augmented-generation, large-language-models, reinforcement-learning-from-feedback]
- confidence: high

**definition**: Self-RAG (Self-Reflective Retrieval Augmented Generation) is a RAG architecture in which the model itself decides when to retrieve, what to retrieve, and how to use the retrieved information, using special reflection tokens inserted into the generation process. The model generates four types of reflection tokens: Retrieve tokens (should the model retrieve at this point?), ISREL tokens (is the retrieved passage relevant?), ISSUP tokens (does the generated text correctly use the retrieved content?), and ISUSE tokens (is the generated response useful overall?). These tokens enable the model to selectively retrieve only when retrieval is beneficial, to assess the quality of retrieved content, and to evaluate whether the generated response faithfully uses the retrieved information — solving the over-retrieval and under-retrieval problems of fixed-retrieval architectures.

**key_claim**: Self-RAG's selective retrieval mechanism substantially improves response quality compared to retrieve-always architectures by avoiding retrieval noise on questions where the model's parametric knowledge is sufficient and reliable — retrieve-always architectures degrade performance on questions within the model's competence by injecting retrieved passages that may be relevant but slightly different from the correct answer, introducing distraction and citation drift; selective retrieval concentrates retrieval on questions where the model genuinely lacks reliable parametric knowledge.

**warning**: Self-RAG's reflection tokens must be generated reliably for the architecture to function correctly — if the model's Retrieve decisions are miscalibrated (retrieving when parametric knowledge is sufficient, or not retrieving when it is needed), the downstream response quality is worse than either always-retrieve or never-retrieve baselines; training Self-RAG models requires careful calibration of the reflection token generation through reinforcement learning or supervised training on carefully curated reflection data, and the calibration must be validated on the specific deployment domain rather than assumed to transfer from the training distribution.

## Corrective RAG Pipeline

- secondary_domains: [retrieval-augmented-generation, quality-control, large-language-models]
- aliases: [CRAG, retrieval quality correction, self-correcting RAG]
- broader: [retrieval-augmented-generation, self-rag-selective-retrieval]
- related: [self-rag-selective-retrieval, adaptive-rag-routing, retrieval-faithfulness]
- prerequisites: [retrieval-augmented-generation, large-language-models]
- confidence: high

**definition**: Corrective RAG (CRAG) is a RAG pipeline enhancement that assesses the quality of retrieved documents and applies corrective actions when the retrieval quality is insufficient — either web-searching for higher-quality sources, decomposing the retrieved document into fine-grained knowledge strips and filtering out irrelevant strips, or flagging retrieval failure for fallback to parametric knowledge generation. CRAG introduces a lightweight retrieval evaluator that scores the relevance of retrieved documents against the query and triggers corrective actions when scores are below confidence thresholds. The corrective action architecture ensures that the generator receives either high-quality retrieved context or a clear signal that retrieval has failed, preventing the generation of responses that appear retrieval-grounded but are actually based on irrelevant retrieved content.

**key_claim**: Corrective RAG significantly improves factual accuracy over standard RAG architectures specifically on queries where the initial retrieval returns marginally relevant or partially relevant documents — standard RAG without correction generates responses that blend retrieved and parametric knowledge without detecting the quality boundary, producing responses that are harder to trace and correct than either pure parametric or pure retrieval-based responses; CRAG's retrieval quality assessment creates a quality boundary that keeps the generation strategy interpretable.

**warning**: CRAG's web-search fallback for insufficient local retrieval introduces dependencies on external search APIs that may not be available, affordable, or appropriate in all deployment contexts — enterprise RAG systems deployed on private corporate data cannot fall back to public web search, and the web-search fallback risks surfacing information that contradicts or contradicts the enterprise knowledge base; corrective actions in CRAG must be designed for the specific deployment environment, and web-search fallback should be treated as an enterprise deployment anti-pattern unless explicitly approved.

## Adaptive RAG Routing

- secondary_domains: [retrieval-augmented-generation, query-complexity, adaptive-inference]
- aliases: [Adaptive-RAG, query-complexity routing, conditional retrieval architecture]
- broader: [retrieval-augmented-generation, self-rag-selective-retrieval]
- related: [self-rag-selective-retrieval, corrective-rag-pipeline, iterative-retrieval-augmentation]
- prerequisites: [retrieval-augmented-generation, query-classification, large-language-models]
- confidence: high

**definition**: Adaptive RAG routing is a RAG architecture that classifies incoming queries by complexity before retrieval and routes each query to the most appropriate retrieval and generation strategy: (1) no retrieval (direct parametric answer for simple factual queries the model can answer reliably), (2) single-step retrieval (standard retrieve-then-generate for moderately complex queries), or (3) iterative multi-step retrieval (repeated retrieval-generation cycles for complex multi-hop queries). The routing decision is made by a classifier trained on query-complexity labels or by using the LLM itself to self-assess the query's complexity. Adaptive routing reduces latency and cost by avoiding expensive multi-step retrieval for simple queries while ensuring complex queries receive sufficient retrieval depth.

**key_claim**: Adaptive RAG routing achieves better latency-quality trade-offs than fixed-strategy RAG architectures because the optimal retrieval strategy varies dramatically by query type — simple queries suffer from retrieval latency overhead and retrieval noise without quality benefit, while complex queries suffer from insufficient retrieval depth in single-step architectures; routing enables each query to be handled with its optimal strategy rather than applying a single fixed strategy to all queries with necessarily suboptimal results.

**warning**: Adaptive RAG routing quality is bounded by the router's accuracy — misclassified queries receive the wrong retrieval strategy, which can be worse than applying the default strategy uniformly; a router that incorrectly classifies complex multi-hop queries as simple consistently fails on the most challenging queries in the evaluation set, producing a quality profile that looks good on average (simple queries are handled correctly) but fails dramatically on the hardest cases; router performance must be specifically evaluated on the complex query subset rather than relying on aggregate accuracy.

## Late Interaction Retrieval

- secondary_domains: [information-retrieval, neural-information-retrieval, retrieval-augmented-generation]
- aliases: [ColBERT retrieval, MaxSim retrieval, fine-grained token interaction retrieval]
- broader: [dense-retrieval-for-rag, information-retrieval]
- related: [dense-retrieval-for-rag, cross-encoder-reranking, embedding-model-selection]
- prerequisites: [dense-retrieval-for-rag, neural-information-retrieval, retrieval-augmented-generation]
- confidence: high

**definition**: Late interaction retrieval is a neural information retrieval paradigm (exemplified by ColBERT) that encodes queries and documents into sets of token-level embeddings rather than a single document embedding, and computes relevance scores using maximum similarity aggregation across all query-document token pairs (MaxSim). This approach preserves the fine-grained token-level interactions that are necessary for precise relevance estimation while remaining significantly faster than cross-encoder reranking (which requires joint encoding of each query-document pair). Late interaction retrieval achieves near-cross-encoder accuracy at a fraction of cross-encoder latency, making it viable for first-stage retrieval in latency-sensitive applications.

**key_claim**: Late interaction retrieval's MaxSim scoring mechanism makes it substantially more robust to query-document vocabulary mismatch than single-vector dense retrieval while remaining much more scalable than cross-encoder reranking — the token-level matching aligns specific query terms with their counterpart evidence terms in documents even when the document and query use different surrounding context, a precision advantage that single-vector retrieval loses by compressing all document information into one vector and cross-encoder achieves but at prohibitive latency cost.

**warning**: Late interaction retrieval requires significantly more index storage than single-vector dense retrieval because storing a token embedding vector for every token in every document rather than a single vector per document multiplies the index size by the average document length in tokens; this storage multiplier (typically 50–200x for document lengths of 50–200 tokens) makes late interaction retrieval impractical for very large corpora without aggressive compression techniques (product quantisation, binary embeddings), and storage and memory planning must account for this overhead before selecting late interaction retrieval as the production retrieval architecture.

## Cross-Encoder Reranking

- secondary_domains: [information-retrieval, neural-information-retrieval, retrieval-augmented-generation]
- aliases: [reranking, cross-encoder scoring, pointwise reranking]
- broader: [retrieval-augmented-generation, information-retrieval]
- related: [dense-retrieval-for-rag, late-interaction-retrieval, reciprocal-rank-fusion]
- prerequisites: [information-retrieval, neural-information-retrieval, retrieval-augmented-generation]
- confidence: high

**definition**: Cross-encoder reranking is a retrieval post-processing step that rescores a set of candidate documents retrieved by a fast first-stage retriever (dense or sparse) using a cross-encoder model that jointly encodes the query and each candidate document together, enabling fine-grained interaction-based relevance scoring. Cross-encoders are slower than bi-encoders (requiring one forward pass per query-document pair rather than one pass per document in an offline index) but more accurate because joint encoding allows the model to detect precise evidence alignment, negation, and contextual relevance. Reranking is applied to the top-k candidates from first-stage retrieval rather than to the full corpus, making its latency acceptable for real-time RAG applications.

**key_claim**: Cross-encoder reranking is the highest-accuracy retrieval stage available for RAG systems and is essential for tasks requiring precise document selection (factual question answering, citation-based generation) where the first-stage retrieval returns many partially-relevant candidates; the improvement from adding reranking to a dense first-stage retrieval system typically exceeds the improvement achievable by upgrading the first-stage retriever alone, making reranking a higher-priority investment than embedding model upgrade for improving RAG precision.

**warning**: Cross-encoder reranking is significantly more expensive than first-stage retrieval in terms of inference latency — scoring k candidates with a cross-encoder requires k separate forward passes, making it 10–100x more expensive per query than first-stage retrieval; the reranking budget (maximum k candidates and cross-encoder model size) must be calibrated against the latency budget, and the retrieval pipeline must be designed with fallback logic for high-traffic periods where reranking latency would exceed acceptable response time bounds.

## Reciprocal Rank Fusion

- secondary_domains: [information-retrieval, rank-aggregation, retrieval-augmented-generation]
- aliases: [RRF, rank fusion, hybrid search fusion]
- broader: [hybrid-retrieval-patterns, information-retrieval]
- related: [hybrid-retrieval-patterns, dense-retrieval-for-rag, sparse-retrieval-bm25, cross-encoder-reranking]
- prerequisites: [information-retrieval, rank-aggregation, retrieval-augmented-generation]
- confidence: high

**definition**: Reciprocal Rank Fusion (RRF) is a rank aggregation algorithm that combines document rankings from multiple retrieval systems (e.g., dense and sparse retrieval) into a unified ranking by computing a reciprocal rank score for each document in each ranking and summing those scores. The RRF score for a document d combining rankings from k systems is: RRF(d) = Σ 1/(rank_i(d) + c), where rank_i(d) is document d's rank in system i and c is a constant (typically 60) that prevents very highly-ranked documents from dominating the fusion. RRF is parameter-free, robust to score scale differences between retrieval systems, and empirically outperforms weighted score combination approaches that require calibration.

**key_claim**: RRF's robustness advantage over weighted score combination fusion makes it the preferred fusion method for hybrid RAG retrieval in production systems — weighted combination requires per-deployment tuning of combination weights that may change as the query distribution evolves, while RRF's parameter-free design (with the single constant c = 60 working well across diverse task distributions) eliminates the tuning overhead while achieving equivalent or superior fusion quality on most real-world query distributions.

**warning**: RRF assumes that the two retrieval systems being fused produce independently valid rankings, which is violated when both systems are based on the same embedding model or trained on the same data — fusing the results of two dense retrievers using the same base embedding model with RRF produces marginal or no improvement over either system alone because the rankings are correlated; effective RRF fusion requires genuinely diverse retrieval signals (dense and sparse, or different embedding model families) where the retrieval failures of one system are likely to be successes of the other.

## Chunking Strategies for RAG

- secondary_domains: [retrieval-augmented-generation, document-processing, information-retrieval]
- aliases: [document chunking, text segmentation for RAG, passage splitting strategies]
- broader: [retrieval-augmented-generation, document-processing]
- related: [dense-retrieval-for-rag, embedding-model-selection, retrieval-faithfulness]
- prerequisites: [retrieval-augmented-generation, text-segmentation, information-retrieval]
- confidence: high

**definition**: Chunking strategies for RAG refer to the methods used to divide source documents into retrievable units (chunks) that are embedded and indexed for retrieval. The chunking decision determines the granularity of retrieval: coarse chunks preserve more context per retrieved unit but may include irrelevant surrounding text; fine chunks are more precise but may lack sufficient context for the generator. Chunking strategies range from fixed-size overlapping windows (e.g., 256-token chunks with 64-token overlap) to semantic chunking (splitting at paragraph or section boundaries), to hierarchical chunking (indexing at multiple granularities and retrieving at the most appropriate level), to small-to-large retrieval (indexing fine chunks but retrieving the surrounding context window of any matching chunk).

**key_claim**: Chunking strategy is a dominant determinant of RAG system quality that is frequently under-optimised relative to embedding model and retrieval algorithm selection — the chunking strategy determines both the precision of retrieved passages (fine chunks surface specific evidence) and the completeness of context available to the generator (coarse chunks include necessary surrounding context), and the optimal chunking granularity varies substantially by document type, query type, and generator context window size; task-specific chunking validation is essential and generic chunking parameters are rarely optimal.

**warning**: Sentence-level or fixed-token-boundary chunking is the most common and most error-prone chunking approach — splitting at token boundaries interrupts sentences and removes semantic context required for correct interpretation, while sentence-level splitting fragments information that spans multiple sentences (lists, tables, multi-sentence arguments) into chunks that are individually incomplete; semantic chunking at paragraph or section boundaries preserves linguistic units but produces variable-length chunks that challenge embedding model capacity and retrieval scoring; no single chunking strategy dominates across all document types, requiring domain-specific validation.

## Embedding Model Selection

- secondary_domains: [dense-retrieval-for-rag, natural-language-processing, machine-learning]
- aliases: [retrieval model selection, encoder selection for RAG, embedding architecture choice]
- broader: [dense-retrieval-for-rag, retrieval-augmented-generation]
- related: [dense-retrieval-for-rag, chunking-strategies-for-rag, late-interaction-retrieval]
- prerequisites: [dense-retrieval-for-rag, embedding-models, retrieval-augmented-generation]
- confidence: high

**definition**: Embedding model selection for RAG refers to the process of choosing or training the neural encoder used to produce dense vector representations of queries and documents for dense retrieval. Selection criteria include: embedding dimension (higher dimensions may capture more nuance but increase index size and retrieval cost), maximum input token length (models with longer context windows chunk documents more coarsely), domain alignment (models fine-tuned on in-domain data outperform generic models for domain-specific corpora), symmetric vs. asymmetric retrieval (separate query and document encoders can outperform single-encoder models), and benchmark performance on representative retrieval tasks. Common embedding model families include SBERT, E5, GTE, BGE, and text-embedding-* from OpenAI.

**key_claim**: Domain-adapted embedding models consistently outperform general-purpose embedding models for domain-specific RAG applications, often by margins that exceed the gains from architectural improvements in the retrieval pipeline — fine-tuning an embedding model on 10,000–50,000 in-domain query-document pairs using contrastive learning (supervised or synthetic) typically improves retrieval recall@10 by 5–20% on domain-specific queries compared to the best publicly available generic model, making domain embedding adaptation a high-ROI investment for production RAG deployments in specialised domains.

**warning**: Embedding model selection based solely on public benchmark performance (MTEB) may not translate to retrieval quality on the specific target corpus and query distribution — public benchmarks use general-domain corpora and query distributions that may differ substantially from enterprise or domain-specific deployment contexts; embedding model evaluation must be conducted on a representative sample of the target corpus and query distribution before finalising model selection, and the selected model's retrieval quality should be validated end-to-end by measuring the RAG system's downstream answer quality, not only the intermediate retrieval metrics.

## Retrieval Faithfulness

- secondary_domains: [retrieval-augmented-generation, factual-accuracy, hallucination]
- aliases: [RAG faithfulness, source attribution accuracy, retrieval-grounded generation]
- broader: [retrieval-augmented-generation, factual-accuracy]
- related: [knowledge-conflict-in-rag, corrective-rag-pipeline, retrieval-faithfulness]
- prerequisites: [retrieval-augmented-generation, hallucination, factual-accuracy]
- confidence: high

**definition**: Retrieval faithfulness refers to the degree to which a RAG system's generated responses are grounded in and consistent with the retrieved source documents, rather than introducing information from the model's parametric knowledge that contradicts or extends beyond the retrieved context. A faithful RAG response cites only claims that can be traced to specific retrieved passages, acknowledges when the retrieved documents do not contain sufficient information to answer the query, and does not embellish retrieved facts with parametric knowledge that may be incorrect or outdated. Retrieval faithfulness is distinct from factual accuracy: a response can be faithful (grounded in retrieved documents) but inaccurate (if the retrieved documents contain incorrect information), and a response can be accurate but unfaithful (if the correct information comes from parametric memory rather than retrieval).

**key_claim**: Retrieval faithfulness and answer accuracy are distinct and sometimes conflicting objectives in RAG systems — optimising strictly for faithfulness (only generating claims directly stated in retrieved documents) reduces answer accuracy when retrieved documents are incomplete or outdated, while optimising for accuracy (generating the best available answer) reduces faithfulness when the model supplements insufficient retrievals with parametric knowledge; production RAG systems must explicitly specify which objective takes precedence for their use case and must measure both objectives separately.

**warning**: Retrieval faithfulness evaluation is substantially harder than faithfulness appears — LLMs are capable of generating text that sounds like it is grounded in retrieved passages while subtly modifying facts (paraphrasing with changed quantities, adding causation that the source only implies, merging claims from different documents incorrectly), making surface-level citation accuracy checks insufficient for faithfulness validation; reliable faithfulness evaluation requires fine-grained claim-level entailment checking that verifies each generated claim against the source passages rather than checking only whether source passages were cited.

## Knowledge Conflict in RAG

- secondary_domains: [retrieval-augmented-generation, factual-accuracy, knowledge-integration]
- aliases: [context-parameter conflict, retrieval-memory conflict, conflicting knowledge in RAG]
- broader: [retrieval-augmented-generation, factual-accuracy]
- related: [retrieval-faithfulness, corrective-rag-pipeline, self-rag-selective-retrieval]
- prerequisites: [retrieval-augmented-generation, factual-accuracy, hallucination]
- confidence: high

**definition**: Knowledge conflict in RAG refers to the situation in which the information retrieved from the knowledge base contradicts the factual knowledge stored in the model's parameters — the retrieved context says one thing and the model's internal representation says another — requiring the model to adjudicate between two conflicting information sources when generating its response. Knowledge conflicts arise from: temporal inconsistency (the model's training knowledge is outdated, the retrieved knowledge is current), domain specificity (the retrieved document contains domain-authoritative information that conflicts with the model's more general parametric representation), and error (either the retrieved document or the model's parametric knowledge contains an incorrect fact).

**key_claim**: LLMs consistently show a context-priority bias in knowledge conflicts — when the retrieved context explicitly states information that contradicts the model's parametric knowledge, most instruction-tuned models prioritise the retrieved context over parametric knowledge when the conflict is clearly stated in the retrieved passage, but resolve conflicts in favour of parametric knowledge when the retrieved passage is indirect or requires inference; this asymmetric conflict resolution reflects the instruction-tuning distribution rather than a principled information-priority mechanism, and the model's conflict resolution behaviour can be shifted substantially through explicit prompting instructions about information priority.

**warning**: Knowledge conflict detection is a prerequisite for reliable knowledge conflict resolution, but detecting conflicts requires the model to have reliable access to its own parametric knowledge about the conflicting claim — a model with incorrect or uncertain parametric knowledge may fail to recognise that the retrieved context conflicts with parametric knowledge, silently defaulting to one source without acknowledging the conflict; production RAG systems should implement explicit conflict detection as a separate verification step rather than relying on the generator to implicitly detect and resolve all conflicts correctly.
