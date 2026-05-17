---
id: 20260517000016A
title: "Claude Reasoning Documentation Series — Map of Content"
subtitle: "Complete Navigation Index, Dependency Map, Learning Pathways, and Implementation Inventory for the 10-Document LLM Engineering Reference Library"
series: "Claude Reasoning Documentation Series"
doc_type: moc
tier: 2
phase: 2
version: 1.0.0
status: production
created: 2026-05-17
modified: 2026-05-17
tags:
  - moc
  - series-index
  - llm-engineering
  - claude-reasoning
  - navigation
  - reference
  - tier-2
  - phase-2
aliases:
  - "Claude Reasoning Series MOC"
  - "LLM Engineering Series Index"
  - "Series Navigation Hub"
  - "CRDS MOC"
certainty: established
doc_series_position: MOC (meta-document)
covers_docs: [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8, doc9, doc10]
total_series_words: ~57500
total_series_code_blocks: ~301
total_series_citations: ~141
total_series_wiki_links: ~255
audit_date: 2026-05-17
audit_status: complete
---

# Claude Reasoning Documentation Series — Map of Content

> [!abstract] Series Overview
> The **Claude Reasoning Documentation Series** (CRDS) is a 10-document Tier 2 production-grade reference library covering the complete landscape of LLM engineering — from foundational reasoning architectures through production serving infrastructure, safety systems, and memory management. Each document is a standalone technical reference (~5,500–6,100 words, 30–36 code blocks, 15–16 citations) with full Python implementations, cross-series linking, and academic citation foundations. The series was generated as the Phase 2 component of the Master Exemplar Project 2026, representing the definitive Tier 2 exemplar standard for the PKB.
>
> **Total Series Volume**: ~57,500 words | ~301 code blocks | ~141 citations | ~255 wiki-links
>
> [**Series-Definition**:: A 10-document Tier 2 production-grade LLM engineering reference library covering reasoning architectures, extended thinking, agentic systems, RAG, prompt engineering, evaluation, production serving, safety/alignment, and memory management — each document a standalone implementable reference with full Python code.]

---

## 📐 Series Architecture

The series is organized into **three conceptual tiers** of LLM engineering knowledge:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                TIER A — REASONING FOUNDATIONS (Doc1–Doc3)               │
│    HOW LLMs THINK: Techniques, Extended Thinking, Architecture Theory    │
├─────────────────────────────────────────────────────────────────────────┤
│              TIER B — AGENT & RETRIEVAL SYSTEMS (Doc4–Doc6)             │
│       HOW LLMs ACT: Workflows, RAG, Prompt Optimization                  │
├─────────────────────────────────────────────────────────────────────────┤
│          TIER C — PRODUCTION INFRASTRUCTURE (Doc7–Doc10)                 │
│   HOW LLMs OPERATE: Evaluation, Serving, Safety, Memory                  │
└─────────────────────────────────────────────────────────────────────────┘
```

[**Architecture-Principle**:: The series is designed so each tier builds on the previous — you can read any document standalone, but the full arc from reasoning foundations through production infrastructure provides a complete mental model of LLM systems engineering.]

---

## 📋 Document Registry

| # | Title | ID | Words | Code Blocks | Citations | Key Implementations |
|---|-------|----|-------|-------------|-----------|---------------------|
| 1 | [[doc1-llm-reasoning-techniques-operational-manual\|LLM Reasoning Techniques Operational Manual]] | 20260213000010 | ~5,739 | 28 | 16 | `TreeOfThoughts`, `SelfConsistency`, `ChainOfVerification`, `ReActAgent`, `Reflexion` |
| 2 | [[doc2-extended-thinking-architecture-implementation-guide\|Extended Thinking Architecture Implementation Guide]] | 20260213000011 | ~7,558 | 35 | 15 | `ThinkingBudgetManager`, `CognitiveScaffold`, `MetacognitiveMonitor`, `ExtendedThinkingClient` |
| 3 | [[doc3-advanced-reasoning-architectures-theory-to-practice\|Advanced Reasoning Architectures: Theory to Practice]] | 20260213000012 | ~5,600 | 30 | 12 | `BeamSearchReasoner`, `MonteCarloPolicySelector`, `GraphOfThoughtsEngine` |
| 4 | [[doc4-agentic-workflow-design-patterns\|Agentic Workflow Design Patterns]] | 20260213000013 | ~5,800 | 30 | 12 | `ToolRegistry`, `AgentOrchestrator`, `MultiAgentSupervisor`, `CheckpointManager` |
| 5 | [[doc5-rag-architecture-and-retrieval-patterns\|RAG Architecture and Retrieval Patterns]] | 20260516000015A | ~5,500 | 30 | 15 | `HybridRetriever`, `HyDERetriever`, `ColBERTRetriever`, `RAPTORHierarchy`, `GraphRAG` |
| 6 | [[doc6-advanced-prompt-engineering-techniques\|Advanced Prompt Engineering Techniques]] | 20260516000015B | ~5,600 | 30 | 15 | `APEOptimizer`, `OPROOptimizer`, `DSPyModule`, `PromptCompressor`, `PromptTestSuite` |
| 7 | [[doc7-llm-evaluation-frameworks-and-metrics\|LLM Evaluation Frameworks and Metrics]] | 20260516000015C | ~5,700 | 32 | 15 | `EvalTaxonomy`, `BenchmarkRunner`, `EloRatingSystem`, `LLMJudge`, `RegressionSuite` |
| 8 | [[doc8-production-llm-systems-architecture\|Production LLM Systems Architecture]] | 20260516000015D | ~5,800 | 33 | 15 | `ContinuousBatcher`, `SpeculativeDecoder`, `CircuitBreaker`, `SemanticCache`, `CanaryController` |
| 9 | [[doc9-prompt-safety-and-alignment-techniques\|Prompt Safety and Alignment Techniques]] | 20260516000015E | ~5,900 | 33 | 15 | `InjectionDetector`, `ContentFilter`, `ConstitutionalAI`, `AutomatedRedTeamer`, `HHHEvaluator` |
| 10 | [[doc10-memory-and-context-management-patterns\|Memory and Context Management Patterns]] | 20260516000015F | ~6,100 | 36 | 16 | `TokenBudgetManager`, `ConversationCompressor`, `VectorMemoryStore`, `EpisodicMemoryManager`, `SemanticKnowledgeGraph` |

---

## 🗺️ Cross-Document Dependency Map

```
Doc1 ──────────────────────────────────────────────────────────────────────┐
  │  (reasoning foundations)                                                │
  ├──► Doc2 (extended thinking implementation)                              │
  │      └──► Doc3 (theoretical depth + mathematical models)               │
  │                                                                          │
  ├──► Doc4 (agentic workflows + tool integration)                          │
  │      └──► Doc5 (RAG / knowledge retrieval for agents)                  │
  │                                                                          │
  ├──► Doc6 (automated prompt optimization)                                 │
  │      └──► Doc7 (evaluation of optimized prompts)                       │
  │                                                                          │
  ├──► Doc8 (production serving infrastructure)                             │
  │      ├──► Doc9 (safety + alignment layer on top of production)         │
  │      └──► Doc10 (memory systems for production agents)                 │
  │                                                                          │
  └── All docs depend on Doc1 as the reasoning-technique foundation ────────┘

Doc5 ◄──► Doc10   (RAG ↔ Memory: retrieval strategies are shared)
Doc4 ◄──► Doc8    (Agents ↔ Serving: deployment of agent infrastructure)
Doc6 ◄──► Doc9    (Prompting ↔ Safety: all prompts must pass safety gates)
Doc7 ◄──► Doc8    (Eval ↔ Serving: evaluation drives production decisions)
```

[**Dependency-Principle**:: Doc1 is the universal prerequisite — every other document assumes knowledge of the 8 core reasoning techniques. Doc8 (Production) sits at the integration point where agent systems (Doc4), RAG (Doc5), and evaluation (Doc7) converge in a deployed system.]

---

## 🛤️ Learning Pathways

### Pathway 1: Foundation First *(New to LLM Engineering)*
> Read in series order. Build from reasoning primitives → deployment.

```
Doc1 → Doc2 → Doc3 → Doc4 → Doc5 → Doc6 → Doc7 → Doc8 → Doc9 → Doc10
```

**Est. reading time**: ~40 hours (including code study and experimentation)  
**Key milestone**: After Doc4, you can build basic agentic systems. After Doc8, you can deploy them.

---

### Pathway 2: Production Engineer *(Building/Deploying LLM Systems)*
> Start with architecture and infrastructure, reference reasoning docs as needed.

```
Doc8 → Doc4 → Doc7 → Doc9 → Doc10 → Doc5 → Doc1
```

**Priority focus**: Doc8 (serving), Doc9 (safety), Doc10 (memory) are the operational core.

---

### Pathway 3: AI Researcher *(Theoretical Depth First)*
> Follow the theoretical arc from foundations through mathematical models.

```
Doc3 → Doc1 → Doc2 → Doc6 → Doc7 → Doc5
```

**Key focus**: Doc3 provides the mathematical formulations; Doc7 provides rigorous evaluation methodology.

---

### Pathway 4: Safety-First Engineer *(Alignment & Robustness)*
> Start with safety, understand the systems you're making safe, then memory.

```
Doc9 → Doc8 → Doc1 → Doc6 → Doc7 → Doc10
```

**Key focus**: Doc9 (constitutional AI, RLHF mechanics, red-teaming) is the entry point.

---

### Pathway 5: Memory Systems Specialist *(Context Window Engineering)*
> Deep-dive into memory before production context.

```
Doc10 → Doc5 → Doc2 → Doc8 → Doc4
```

**Key focus**: Doc10 → Doc5 covers the full retrieval-memory stack (vector store → RAG → token budget).

---

## 📄 Document Profiles

### Doc1 — LLM Reasoning Techniques Operational Manual
**ID**: 20260213000010 | **Words**: ~5,739 | **Code Blocks**: 28 | **Citations**: 16

The **universal entry point** for the series. Provides operational protocols for 8 reasoning techniques: [[Tree-of-Thoughts]], [[Self-Consistency]], [[Chain-of-Verification]], [[Program-of-Thoughts]], [[ReAct]], [[Reflexion]], [[Graph-of-Thoughts]], and [[Chain-of-Thought]]. Each technique has a complete Python implementation, empirical benchmarks, and a selection decision tree.

**Key Implementations**: `TreeOfThoughts` (BFS/DFS with state-value scoring), `SelfConsistency` (k-sample ensemble with majority vote), `ChainOfVerification` (4-stage baseline → question → verification → revised answer), `ReActAgent` (Thought→Action→Observation loops), `Reflexion` (episodic memory + self-evaluation loop)

**Cross-links**: Feeds into every subsequent document — Doc2 uses ToT/SC patterns for thinking architecture, Doc4 uses ReAct for agent design, Doc7 benchmarks all 8 techniques.

[**Doc1-Role**:: The reasoning primitive library that all other documents depend on — mastery of Doc1's 8 techniques is the prerequisite for effective use of the rest of the series.]

---

### Doc2 — Extended Thinking Architecture Implementation Guide
**ID**: 20260213000011 | **Words**: ~7,558 | **Code Blocks**: 35 | **Citations**: 15

The most detailed document in the series (~7,558 words). Covers Claude's `<thinking>` tag architecture: XML semantic structure, dual-process cognitive asymmetry, thinking mode configuration (enabled/disabled/auto/interleaved), token budget management, and advanced patterns including multi-turn collaborative thinking and metacognitive scaffolding.

**Key Implementations**: `ThinkingBudgetManager` (adaptive token allocation with recency decay), `CognitiveScaffold` (structured reasoning templates for systematic analysis and comparative evaluation), `MetacognitiveMonitor` (3-level uncertainty tracking), `ExtendedThinkingClient` (API wrapper with retry and token optimization)

**Cross-links**: Doc3 provides the theoretical foundations behind why extended thinking works; Doc10 extends these concepts to full memory architecture.

[**Doc2-Role**:: The definitive implementation guide for Claude's extended thinking — foundational for anyone deploying Claude in production with extended reasoning requirements.]

---

### Doc3 — Advanced Reasoning Architectures: Theory to Practice
**ID**: 20260213000012 | **Words**: ~5,600 | **Code Blocks**: 30 | **Citations**: 12

Bridges academic research with engineering implementation. Provides mathematical formulations for [[Beam-Search-in-Reasoning]], [[Monte-Carlo-Tree-Search]] applied to reasoning, [[Graph-of-Thoughts]] as a DAG traversal problem, and empirical performance analysis across benchmark datasets. Includes comparative analysis of all Doc1 techniques on complexity, compute cost, and accuracy tradeoffs.

**Key Implementations**: `BeamSearchReasoner` (beam width + scoring function), `MonteCarloPolicySelector` (UCB1 bandit for node selection), `GraphOfThoughtsEngine` (DAG merge operations), `ReasoningBenchmarkSuite` (systematic evaluation harness)

**Cross-links**: Prerequisites: Doc1 (techniques), Doc2 (architecture). Feeds forward into Doc7 (evaluation methodology) and Doc6 (prompt optimization informed by theoretical analysis).

[**Doc3-Role**:: The theoretical backbone of the series — transforms technique recipes into principled engineering choices backed by formal analysis.]

---

### Doc4 — Agentic Workflow Design Patterns
**ID**: 20260213000013 | **Words**: ~5,800 | **Code Blocks**: 30 | **Citations**: 12

Production patterns for building agent systems. Covers 8 canonical agentic architectures: sequential, parallel, conditional branching, loop/retry, hierarchical delegation, map-reduce, event-driven, and human-in-the-loop. Includes multi-agent coordination protocols, tool registry management, and failure recovery patterns.

**Key Implementations**: `ToolRegistry` (dynamic tool registration with schema validation), `AgentOrchestrator` (workflow DAG execution with async dispatch), `MultiAgentSupervisor` (delegation + result aggregation), `CheckpointManager` (resumable long-running workflows), `HumanApprovalGate` (interrupt + resume with human feedback)

**Cross-links**: Doc1 (ReAct/Reflexion power individual agents), Doc5 (RAG provides knowledge retrieval for agents), Doc8 (production serving for agent deployments), Doc10 (memory enables stateful agents).

[**Doc4-Role**:: The engineering blueprint for production agent systems — the practical counterpart to Doc1's theoretical reasoning techniques.]

---

### Doc5 — RAG Architecture and Retrieval Patterns
**ID**: 20260516000015A | **Words**: ~5,500 | **Code Blocks**: 30 | **Citations**: 15

Complete RAG implementation guide from naive retrieval to advanced architectures. Covers [[Hybrid-Retrieval]] (dense + sparse BM25 fusion), [[HyDE]] (hypothetical document embedding), [[ColBERT]] late-interaction retrieval, [[RAPTOR]] hierarchical summarization trees, and [[GraphRAG]] entity-relationship retrieval. Includes chunking strategies, re-ranking, and context window management.

**Key Implementations**: `HybridRetriever` (RRF fusion of dense cosine + BM25), `HyDERetriever` (query expansion via LLM-generated hypothetical doc), `ColBERTRetriever` (MaxSim late interaction), `RAPTORHierarchy` (recursive summarization tree + leaf/summary routing), `GraphRAG` (entity extraction + community detection + structured context)

**Cross-links**: Doc4 (agents use RAG for knowledge access), Doc10 (memory system and RAG are complementary retrieval strategies), Doc7 (RAG evaluation methodology).

[**Doc5-Role**:: The retrieval engineering reference — covers the full spectrum from simple vector lookup to graph-structured community-based retrieval.]

---

### Doc6 — Advanced Prompt Engineering Techniques
**ID**: 20260516000015B | **Words**: ~5,600 | **Code Blocks**: 30 | **Citations**: 15

Automated prompt optimization beyond manual crafting. Covers [[Automatic-Prompt-Engineer]] (APE — sampling + scoring + selection), [[OPRO]] (optimization by prompting, meta-prompt iteration), [[DSPy]] (declarative prompt signatures with automatic teleprompter compilation), [[Meta-Prompting]] (LLM-generated prompt variants), prompt compression, and systematic A/B testing frameworks.

**Key Implementations**: `APEOptimizer` (proposal → score → select cycle), `OPROOptimizer` (meta-prompt with trajectory history), `DSPyModule` (declarative signature + few-shot bootstrapping), `PromptCompressor` (token reduction via information-density scoring), `PromptTestSuite` (paired statistical significance testing)

**Cross-links**: Doc1 (CoT/ToT patterns are the prompt structures being optimized), Doc3 (theoretical analysis guides optimization objectives), Doc7 (evaluation metrics used to score prompt variants), Doc9 (safety gates applied to all prompt candidates).

[**Doc6-Role**:: Transforms prompt engineering from art to systematic engineering — automated optimization pipelines replace manual prompt tuning.]

---

### Doc7 — LLM Evaluation Frameworks and Metrics
**ID**: 20260516000015C | **Words**: ~5,700 | **Code Blocks**: 32 | **Citations**: 15

Systematic evaluation methodology for every stage of the LLM lifecycle. Covers [[Evaluation-Taxonomy]] (capability, alignment, robustness, safety), benchmark construction and execution, [[Elo-Rating-Systems]] for model comparison, [[LLM-as-Judge]] implementation with bias mitigation, regression suites, and production monitoring dashboards.

**Key Implementations**: `EvalTaxonomy` (capability/alignment/robustness/safety classification tree), `BenchmarkRunner` (parallel execution + statistical confidence intervals), `EloRatingSystem` (Bradley-Terry model, K-factor adaptive), `LLMJudge` (prompted evaluation with position-bias mitigation via swap testing), `RegressionSuite` (change-detection with baseline pinning), `ProductionMonitor` (latency/quality/cost dashboards)

**Cross-links**: Doc1 (benchmarks for all 8 reasoning techniques), Doc6 (evaluation scores drive prompt optimization), Doc8 (production monitoring extends Doc7's metrics to deployed systems), Doc9 (safety evaluation is a specialized evaluation subdomain).

[**Doc7-Role**:: The measurement layer of the series — every other document's implementations require Doc7's evaluation harnesses to validate correctness and performance.]

---

### Doc8 — Production LLM Systems Architecture
**ID**: 20260516000015D | **Words**: ~5,800 | **Code Blocks**: 33 | **Citations**: 15

The infrastructure and serving engineering reference. Covers [[Continuous-Batching]] (dynamic slot allocation for throughput), [[Speculative-Decoding]] (draft-verify with rejection sampling), [[Circuit-Breaker-Pattern]] (failure isolation + fallback routing), [[Semantic-Caching]] (embedding-similarity cache lookup), [[Canary-Deployment]] (progressive traffic shifting + automated rollback), and shadow deployment testing.

**Key Implementations**: `ContinuousBatcher` (priority queue with SLA-aware slot management), `SpeculativeDecoder` (k-token draft + token-by-token verification with acceptance probability), `CircuitBreaker` (CLOSED/OPEN/HALF_OPEN state machine), `FallbackRouter` (model-tier cascade with latency budget), `SemanticCache` (cosine similarity lookup + cache-aside pattern), `CanaryController` (weighted routing + statistical significance testing for rollback)

**Cross-links**: Doc4 (agent infrastructure is deployed via Doc8 patterns), Doc7 (evaluation metrics fed into canary traffic routing decisions), Doc9 (safety layer sits between serving infrastructure and user traffic), Doc10 (memory systems deployed as a separate serving tier).

[**Doc8-Role**:: The production anchor of the series — where all upstream engineering work meets operational reality. Reliability, cost, and latency tradeoffs are resolved here.]

---

### Doc9 — Prompt Safety and Alignment Techniques
**ID**: 20260516000015E | **Words**: ~5,900 | **Code Blocks**: 33 | **Citations**: 15

Defense-in-depth safety architecture. Covers multi-layer prompt injection defense (detection → normalization → quarantine), [[Constitutional-AI]] (16-principle self-critique + revision loop), [[RLHF]] mechanics with KL-divergence penalty (PPO-KL implementation), automated [[Red-Teaming]] with adversarial variation generation, [[Bias-Detection]] across demographic dimensions, and real-time [[HHH-Evaluation]] (Helpful/Harmless/Honest) production monitoring.

**Key Implementations**: `InjectionDetector` (role-play/command injection/context poisoning pattern detection), `ContentFilter` (multi-taxonomy harm classification), `ConstitutionalAI` (iterative self-critique with principle pool), `PPO_KL_Trainer` (policy gradient with KL penalty and reference model), `AutomatedRedTeamer` (genetic algorithm for adversarial variation), `BiasDetector` (demographic parity + equalized odds scoring), `HHHEvaluator` (online helpfulness/harmlessness/honesty scoring with calibrated thresholds)

**Cross-links**: Doc1 (reasoning techniques that must remain safe), Doc4 (agent actions require safety gating), Doc6 (all optimized prompts must pass safety evaluation), Doc8 (safety layer integrated into serving infrastructure).

[**Doc9-Role**:: The trust layer of the series — makes deployed LLM systems safe, fair, and aligned with human values through programmatic safety engineering rather than post-hoc filtering.]

---

### Doc10 — Memory and Context Management Patterns
**ID**: 20260516000015F | **Words**: ~6,100 | **Code Blocks**: 36 | **Citations**: 16

The final and most complex document. Covers the complete memory stack: [[Token-Budget-Management]] (priority-ranked context allocation with exponential recency decay), [[Conversation-Compression]] (two-tier summarization buffer + rolling summary merging), [[Vector-Memory]] (cosine retrieval + SHA-256 dedup + importance-weighted eviction), [[Episodic-Memory]] (0.7×similarity + 0.3×poignancy blended retrieval + periodic reflection synthesis), [[Semantic-Knowledge-Graph]] (triple extraction + BFS neighborhood traversal + contradiction detection), [[Memory-Consolidation]] (episodic → KG + vector promotion pipeline), [[Working-Memory-Scratchpad]] (typed state accumulation + user-safe rendering), and the full [[Multi-Tier-Memory-Router]] (waterfall KG → episodic → vector → history with per-tier token-budget gating).

**Key Implementations**: `TokenBudgetManager` (CRITICAL/HIGH/MEDIUM/LOW/EXPENDABLE priority tiers + `apply_recency_decay()`), `ConversationCompressor` (decision-critical turn preservation + rolling merge), `VectorMemoryStore` (SHA-256 dedup + cosine retrieval + JSON persistence + importance-weighted eviction), `EpisodicMemoryManager` (Park et al. 2023 Generative Agents architecture, poignancy-scoring + reflection synthesis), `SemanticKnowledgeGraph` (BFS neighborhood traversal + confidence-based relation dedup), `MemoryConsolidationPipeline` (episodic-to-KG-and-vector promotion), `WorkingMemoryScratchpad` (observation/plan/correction typed entries + `<scratchpad>` tag rendering), `ProductionMemoryRouter` (waterfall retrieval with latency timing per tier)

**Cross-links**: Doc1 (memory enables Reflexion's episodic learning), Doc4 (stateful agents require memory backends), Doc5 (RAG is the retrieval complement to structured memory), Doc8 (memory systems deployed as a separate production tier), Doc9 (memory must be audited for safety — no harmful content persistence).

[**Doc10-Role**:: The culmination of the series — integrates retrieval (Doc5), agents (Doc4), and serving (Doc8) with a principled cognitive architecture for LLM memory systems.]

---

## ⚙️ Implementation Inventory

A cross-series reference of all major Python classes by category:

### Reasoning Primitives (Doc1–Doc3)
| Class | Document | Function |
|-------|----------|----------|
| `TreeOfThoughts` | Doc1 | BFS/DFS state-space search with value scoring |
| `SelfConsistency` | Doc1 | k-sample ensemble with majority vote aggregation |
| `ChainOfVerification` | Doc1 | 4-stage baseline → questions → independent verify → revise |
| `ReActAgent` | Doc1 | Thought→Action→Observation loop with tool registry |
| `Reflexion` | Doc1 | Multi-trial self-critique with episodic memory |
| `ThinkingBudgetManager` | Doc2 | Adaptive token budget with recency decay |
| `MetacognitiveMonitor` | Doc2 | 3-level uncertainty tracking + self-correction protocol |
| `BeamSearchReasoner` | Doc3 | Width-controlled beam with scoring function |
| `MonteCarloPolicySelector` | Doc3 | UCB1 bandit for reasoning node selection |

### Agent & Retrieval Systems (Doc4–Doc6)
| Class | Document | Function |
|-------|----------|----------|
| `ToolRegistry` | Doc4 | Dynamic tool registration with JSON schema validation |
| `AgentOrchestrator` | Doc4 | Async DAG execution with checkpoint support |
| `MultiAgentSupervisor` | Doc4 | Delegation protocol + result aggregation |
| `HybridRetriever` | Doc5 | RRF fusion: dense cosine + BM25 sparse |
| `HyDERetriever` | Doc5 | Hypothetical document embedding for query expansion |
| `RAPTORHierarchy` | Doc5 | Recursive summarization tree construction + routing |
| `GraphRAG` | Doc5 | Entity extraction + community detection + structured context |
| `APEOptimizer` | Doc6 | Automatic prompt proposal → score → select cycle |
| `OPROOptimizer` | Doc6 | Meta-prompt with trajectory history for iterative refinement |
| `DSPyModule` | Doc6 | Declarative prompt signatures with bootstrapped few-shot |
| `PromptCompressor` | Doc6 | Information-density scoring for token reduction |

### Production Infrastructure (Doc7–Doc10)
| Class | Document | Function |
|-------|----------|----------|
| `BenchmarkRunner` | Doc7 | Parallel eval execution with statistical confidence |
| `EloRatingSystem` | Doc7 | Bradley-Terry model with adaptive K-factor |
| `LLMJudge` | Doc7 | Prompted eval with swap-test bias mitigation |
| `ContinuousBatcher` | Doc8 | SLA-aware slot management for throughput optimization |
| `SpeculativeDecoder` | Doc8 | Draft model + token-by-token rejection sampling |
| `CircuitBreaker` | Doc8 | CLOSED/OPEN/HALF_OPEN failure isolation state machine |
| `SemanticCache` | Doc8 | Cosine-similarity cache lookup + cache-aside pattern |
| `CanaryController` | Doc8 | Weighted routing + statistical significance rollback |
| `ConstitutionalAI` | Doc9 | 16-principle iterative self-critique + revision |
| `AutomatedRedTeamer` | Doc9 | Genetic algorithm for adversarial prompt variation |
| `HHHEvaluator` | Doc9 | Online HHH scoring with calibrated production thresholds |
| `TokenBudgetManager` | Doc10 | Priority-tier context allocation + recency decay |
| `VectorMemoryStore` | Doc10 | Cosine retrieval + SHA-256 dedup + importance eviction |
| `EpisodicMemoryManager` | Doc10 | Park et al. Generative Agents + poignancy-blended retrieval |
| `SemanticKnowledgeGraph` | Doc10 | Triple extraction + BFS traversal + contradiction detection |
| `ProductionMemoryRouter` | Doc10 | Waterfall KG→episodic→vector→history with budget gating |

---

## 🔑 Key Concepts Index

An alphabetical index of major concepts in the series with their primary document reference:

| Concept | Primary Doc | Related Docs |
|---------|-------------|--------------|
| [[Alignment]] | Doc9 | Doc7 |
| [[Agentic-Workflows]] | Doc4 | Doc1, Doc8 |
| [[Automatic-Prompt-Engineer]] (APE) | Doc6 | Doc7 |
| [[Beam-Search]] (reasoning) | Doc3 | Doc1 |
| [[Circuit-Breaker-Pattern]] | Doc8 | — |
| [[Chain-of-Thought]] | Doc1 | Doc2, Doc3 |
| [[Chain-of-Verification]] | Doc1 | Doc3 |
| [[ColBERT-Retrieval]] | Doc5 | — |
| [[Constitutional-AI]] | Doc9 | Doc6 |
| [[Continuous-Batching]] | Doc8 | — |
| [[Conversation-Compression]] | Doc10 | Doc2 |
| [[DSPy]] | Doc6 | Doc7 |
| [[Elo-Rating-System]] | Doc7 | — |
| [[Episodic-Memory]] | Doc10 | Doc1 |
| [[Extended-Thinking]] | Doc2 | Doc1, Doc3 |
| [[Graph-of-Thoughts]] | Doc1 | Doc3 |
| [[GraphRAG]] | Doc5 | Doc4 |
| [[HyDE]] (Hypothetical Document Embedding) | Doc5 | Doc6 |
| [[KL-Divergence-Penalty]] (RLHF) | Doc9 | — |
| [[LLM-as-Judge]] | Doc7 | Doc9 |
| [[Memory-Consolidation]] | Doc10 | Doc5 |
| [[Metacognitive-Monitoring]] | Doc2 | Doc1 |
| [[Monte-Carlo-Tree-Search]] (reasoning) | Doc3 | Doc1 |
| [[Multi-Agent-Systems]] | Doc4 | Doc8 |
| [[OPRO]] | Doc6 | Doc7 |
| [[PPO-KL]] (policy gradient) | Doc9 | — |
| [[Production-Monitoring]] | Doc7 | Doc8, Doc9 |
| [[Prompt-Injection-Defense]] | Doc9 | Doc6 |
| [[RAPTOR]] | Doc5 | Doc10 |
| [[ReAct]] | Doc1 | Doc4 |
| [[Red-Teaming]] | Doc9 | Doc7 |
| [[Reflexion]] | Doc1 | Doc10 |
| [[Retrieval-Augmented-Generation]] | Doc5 | Doc4, Doc10 |
| [[RLHF]] | Doc9 | Doc7 |
| [[Semantic-Caching]] | Doc8 | Doc5 |
| [[Semantic-Knowledge-Graph]] | Doc10 | Doc5 |
| [[Self-Consistency]] | Doc1 | Doc3, Doc6 |
| [[Speculative-Decoding]] | Doc8 | — |
| [[Token-Budget-Management]] | Doc10 | Doc2 |
| [[Tree-of-Thoughts]] | Doc1 | Doc2, Doc3 |
| [[Vector-Memory]] | Doc10 | Doc5 |
| [[Working-Memory-Scratchpad]] | Doc10 | Doc2 |

---

## 🔍 Audit Notes (Day 22 — 2026-05-17)

> [!important] Audit Findings
> The following issues were identified and documented during the Phase 2 Day 22 cross-document audit. Items marked ✅ are fixed; items marked ⚠️ are deferred to Day 23.

**Issue 1 — Doc10 Broken `related_docs` Link** ✅ FIXED
- `doc5-rag-architecture.md` → corrected to `doc5-rag-architecture-and-retrieval-patterns.md`

**Issue 2 — Phantom Phase 1 Files** ⚠️ DEFERRED
- `doc5-quick-reference-library.md` (v1.0.0, 2025-01-06) — Phase 1 helper document, not part of canonical 10-doc series
- `doc6-integration-patterns-cookbook.md` (v1.0.0, 2025-01-06) — Phase 1 helper document, not part of canonical 10-doc series
- **Decision**: Leave files in place (they have value as reference material). Rename or archive in Day 23 to avoid namespace confusion with canonical doc5/doc6.

**Issue 3 — Frontmatter Schema Variance** ⚠️ DEFERRED to Day 23
- **Doc1–4** (Phase 1 format): Missing `title`, `subtitle`, `series`, `doc_number`, `tier`, `phase`, `doc_series_position` fields
- **Doc5–6** (Phase 2 early format): Use `series_position`/`series_total` instead of `doc_series_position`; use `prerequisites` instead of `related_docs`
- **Doc7–10** (Phase 2 mature format): Canonical schema — all series fields present
- **Doc9**: Uses `.md` file extensions in `related_docs` values; Doc7/8 do not
- **Recommendation**: Standardize all 10 docs to Doc7–10 schema in Day 23 schema normalization pass

**Issue 4 — 00-SERIES-OVERVIEW-AND-USAGE-GUIDE.md Outdated** ⚠️ DEFERRED to Day 23
- Current file covers only Phase 1 (6 documents, outdated word count, no Doc7–10)
- **Decision**: Update or replace with a pointer to this MOC document in Day 23

[**Audit-Summary**:: 1 critical link broken → fixed. 3 structural issues identified and deferred to Day 23 schema normalization. Series is semantically complete and navigable; schema variance is cosmetic, not functional.]

---

## 📊 Series Statistics Summary

| Metric | Total |
|--------|-------|
| **Documents** | 10 |
| **Approximate total words** | ~57,500 |
| **Total code blocks** | ~301 |
| **Total citations** | ~141 |
| **Total wiki-links** | ~255 |
| **Unique Python classes implemented** | 41+ |
| **Unique academic papers cited** | ~90 (estimated unique, ~141 total with overlaps) |
| **Series generation period** | Phase 1: 2026-02-13 (Doc1–4) / Phase 2: 2026-05-16 (Doc5–10) |
| **Tier** | 2 (Production-Grade Reference Implementations) |

---

## 🔗 Related Topics for PKB Expansion

1. **[[Transformer-XL-and-Extended-Context-Architectures]]**
   - *Connection*: Doc2 and Doc10 rely on context window mechanics; Transformer-XL's recurrence mechanism is the precursor to modern context extension techniques
   - *Depth Potential*: Covers sliding window attention, recurrence-based memory, and the theoretical limits of positional encoding — deepens understanding of Doc10's token budget management
   - *Knowledge Graph Role*: Bridges CRDS with foundational Transformer architecture literature

2. **[[Generative-Agents-Architecture]]** (Park et al. 2023)
   - *Connection*: Doc10's `EpisodicMemoryManager` is directly derived from the Generative Agents paper — poignancy scoring, reflection synthesis, and retrieval blending
   - *Depth Potential*: Full analysis of the 25-agent simulation, the observation-reflection-planning architecture, and emergent social behavior
   - *Knowledge Graph Role*: The key academic predecessor to production episodic memory systems

3. **[[vLLM-and-PagedAttention]]**
   - *Connection*: Doc8's continuous batching and KV cache management are implemented in vLLM — understanding PagedAttention at the kernel level deepens Doc8 mastery
   - *Depth Potential*: Block-level KV cache management, preemption strategies, chunked prefill — the engineering substrate beneath Doc8's serving patterns
   - *Knowledge Graph Role*: Connects CRDS serving architecture to the open-source inference stack

4. **[[DSPy-Framework-Deep-Dive]]**
   - *Connection*: Doc6 introduces DSPy's declarative optimization paradigm but covers only the surface — a dedicated note would cover teleprompters (COPRO, MIPRO), optimizers, and assertions in depth
   - *Depth Potential*: Full teleprompter implementation, assertion-driven optimization, and the LMQL/Outlines integration for structured outputs
   - *Knowledge Graph Role*: Extends Doc6's automated prompt engineering into a full framework analysis

---

*Series generated: Phase 1 — 2026-02-13 through 2026-05-16 (Doc1–4) | Phase 2 — 2026-05-16 (Doc5–10)*
*MOC generated: 2026-05-17 (Phase 2 Day 22 — Post-Series Audit)*
*Total CRDS generation time: Phase 2 Days 15–22*
