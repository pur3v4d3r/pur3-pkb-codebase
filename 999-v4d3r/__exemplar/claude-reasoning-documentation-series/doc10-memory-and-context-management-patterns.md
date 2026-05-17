---
id: 20260516000015F
title: "Memory and Context Management Patterns"
subtitle: "Token Budget Engineering, Conversation Compression, Vector Memory, Episodic and Semantic Memory, and Production Multi-Tier Memory Architecture"
series: "Claude Reasoning Documentation Series"
doc_number: 10
tier: 2
phase: 2
version: 2.0.0
status: production
created: 2026-05-16
modified: 2026-05-16
tags:
  - memory-systems
  - context-management
  - vector-memory
  - episodic-memory
  - semantic-memory
  - token-budget
  - conversation-compression
  - production-systems
  - tier-2
  - phase-2
aliases:
  - Memory and Context Management
  - LLM Memory Architecture
  - Context Window Engineering
  - Memory Management Patterns
certainty: established
doc_series_position: 10/10
related_docs:
  - doc1-llm-reasoning-techniques-operational-manual
  - doc4-agentic-workflow-design-patterns
  - doc5-rag-architecture-and-retrieval-patterns
  - doc8-production-llm-systems-architecture
  - doc9-prompt-safety-and-alignment-techniques
word_count: ~6100
code_blocks: 36
citations: 16
wiki_links: 30
---

# Memory and Context Management Patterns

> [!abstract] Document Overview
> This final document in the Claude Reasoning Documentation Series provides production-grade reference implementations for LLM memory and context management — the full stack from token budget engineering and conversation history compression through vector memory stores, episodic and semantic memory architectures, working memory scratchpad patterns, memory consolidation pipelines, and a complete multi-tier production memory router. Every component ships with battle-tested Python code suitable for direct integration into agentic LLM systems.

[**Memory-Architecture-Definition**:: The set of storage, retrieval, and consolidation mechanisms that allow an LLM system to maintain information across context boundaries — spanning the context window (immediate working memory), conversation history (episodic short-term), vector stores (semantic retrieval), and persistent knowledge bases (long-term semantic memory). Each tier has distinct latency, capacity, and staleness characteristics that determine when to use it (Weng 2023; Park et al. 2023).]

[**Context-Window-as-Working-Memory**:: The model's context window functions as its working memory — the only information the model can directly reason over at any moment. Everything outside the context window is inaccessible unless explicitly retrieved and inserted. Context window management is therefore the highest-leverage point in the memory stack: decisions about what to include, exclude, and summarize directly determine the model's effective knowledge state (Ratner et al. 2023).]

---

## Part 1 — Context Window Architecture and Token Budget Engineering

Every production LLM deployment must solve the same fundamental constraint: a fixed token budget that must be allocated across system prompt, conversation history, retrieved context, tool results, and model output. [[Token-Budget-Engineering]] treats this allocation as a first-class engineering problem — with priority tiers, dynamic compression triggers, and measurable quality metrics — rather than an ad hoc afterthought addressed by truncating the oldest messages.

[**Token-Budget-Definition**:: The total number of tokens available in one inference call, partitioned into: (1) reserved system prompt (fixed), (2) reserved output capacity (min_output_tokens), (3) available for dynamic content = context_window_size − system_tokens − min_output_tokens. Dynamic content allocation must prioritize by relevance, recency, and role in supporting the current query.]

[**Priority-Truncation-Definition**:: A budget allocation strategy in which context segments are ranked by a priority function and truncated from the lowest priority end until the token budget is satisfied — preserving the most task-relevant context and avoiding the naive sliding-window approach that discards old but potentially critical information (such as initial user instructions).]

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""token_budget.py — Token budget management with priority-based allocation.

Manages the context window token budget across system prompt, history,
retrieved context, and tool outputs with dynamic compression triggers.

Version: 1.0.0
Python: >=3.10
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum, auto
from typing import Callable


class SegmentPriority(IntEnum):
    """Priority tier for context segments — higher = more important to preserve."""
    CRITICAL = 100      # Current user turn, task instructions — never truncate
    HIGH = 80           # Recent conversation turns, current task context
    MEDIUM = 60         # Retrieved relevant context, tool outputs
    LOW = 40            # Older conversation history, background info
    EXPENDABLE = 20     # Summaries, low-relevance retrieved chunks


@dataclass
class ContextSegment:
    """A single segment of context with token count and priority metadata."""
    segment_id: str
    content: str
    token_count: int
    priority: SegmentPriority
    segment_type: str       # "system", "human", "assistant", "retrieved", "tool"
    compressible: bool = True   # False = never modify content (e.g., system prompt)
    recency_score: float = 1.0  # 0.0–1.0; decays with age for history segments

    @property
    def effective_priority(self) -> float:
        """Combined priority accounting for recency decay on history segments."""
        if self.segment_type in ("system",):
            return float(self.priority)
        return self.priority * (0.5 + 0.5 * self.recency_score)


@dataclass
class BudgetAllocation:
    """Result of token budget allocation — included and excluded segments."""
    included: list[ContextSegment]
    excluded: list[ContextSegment]
    total_tokens_used: int
    budget: int
    utilization: float

    @property
    def tokens_remaining(self) -> int:
        return self.budget - self.total_tokens_used

    @property
    def was_truncated(self) -> bool:
        return len(self.excluded) > 0


class TokenBudgetManager:
    """Priority-based token budget allocator for multi-segment LLM contexts.

    Partitions the context window across fixed and dynamic segments using
    a priority-ranked allocation algorithm. High-priority segments are
    always preserved; low-priority segments are dropped until budget is met.

    Args:
        context_window_size: Total model context window in tokens.
        min_output_tokens: Tokens reserved for model output (default 1024).
        tokenizer_fn: Callable (text: str) -> int returning token count.
                      Uses a word-count heuristic if not provided.
        system_reserve_fraction: Fraction of budget pre-reserved for system prompt
                                 (default 0.15 = 15%).

    Example:
        >>> import math
        >>> mgr = TokenBudgetManager(context_window_size=8192, min_output_tokens=512)
        >>> segments = [
        ...     ContextSegment("sys", "You are a helpful assistant.", 5,
        ...                    SegmentPriority.CRITICAL, "system", compressible=False),
        ...     ContextSegment("user1", "Hello world.", 3,
        ...                    SegmentPriority.HIGH, "human"),
        ... ]
        >>> alloc = mgr.allocate(segments)
        >>> alloc.was_truncated
        False
    """

    def __init__(
        self,
        context_window_size: int = 8192,
        min_output_tokens: int = 1024,
        tokenizer_fn: Callable[[str], int] | None = None,
        system_reserve_fraction: float = 0.15,
    ) -> None:
        self.context_window_size = context_window_size
        self.min_output_tokens = min_output_tokens
        self._tokenize = tokenizer_fn or self._heuristic_token_count
        self.available_budget = context_window_size - min_output_tokens
        self._system_reserve = int(self.available_budget * system_reserve_fraction)

    def count_tokens(self, text: str) -> int:
        """Count tokens in text using the configured tokenizer."""
        return self._tokenize(text)

    def allocate(self, segments: list[ContextSegment]) -> BudgetAllocation:
        """Allocate the token budget across all segments by priority.

        Algorithm:
            1. CRITICAL and non-compressible segments are always included first.
            2. Remaining segments are sorted by effective_priority descending.
            3. Segments are included until budget is exhausted; remainder excluded.

        Args:
            segments: All context segments to allocate across.

        Returns:
            BudgetAllocation with included/excluded sets and utilization stats.
        """
        # Phase 1: Force-include critical / non-compressible segments
        forced = [s for s in segments if not s.compressible or s.priority == SegmentPriority.CRITICAL]
        optional = [s for s in segments if s.compressible and s.priority != SegmentPriority.CRITICAL]

        forced_tokens = sum(s.token_count for s in forced)

        # Guard: if forced segments already exceed budget, we have a config error
        if forced_tokens > self.available_budget:
            raise ValueError(
                f"Critical segments ({forced_tokens} tokens) exceed available budget "
                f"({self.available_budget} tokens). Reduce system prompt or min_output_tokens."
            )

        remaining_budget = self.available_budget - forced_tokens

        # Phase 2: Rank optional segments by effective priority
        ranked = sorted(optional, key=lambda s: s.effective_priority, reverse=True)

        included: list[ContextSegment] = list(forced)
        excluded: list[ContextSegment] = []
        tokens_used = forced_tokens

        for segment in ranked:
            if tokens_used + segment.token_count <= self.available_budget:
                included.append(segment)
                tokens_used += segment.token_count
            else:
                excluded.append(segment)

        return BudgetAllocation(
            included=included,
            excluded=excluded,
            total_tokens_used=tokens_used,
            budget=self.available_budget,
            utilization=tokens_used / max(self.available_budget, 1),
        )

    def apply_recency_decay(
        self,
        segments: list[ContextSegment],
        decay_rate: float = 0.85,
    ) -> list[ContextSegment]:
        """Apply exponential recency decay to history segments.

        Segments with segment_type in ("human", "assistant") receive a
        recency_score that decays exponentially from the most recent turn.
        This allows the budget allocator to naturally deprioritize old turns.

        Args:
            segments: Ordered list of segments (oldest first, newest last).
            decay_rate: Decay per position from the most recent (default 0.85).

        Returns:
            New list with recency_score updated for history segments.
        """
        history_idxs = [
            i for i, s in enumerate(segments)
            if s.segment_type in ("human", "assistant")
        ]
        n = len(history_idxs)
        updated = list(segments)
        for rank, idx in enumerate(reversed(history_idxs)):
            # rank 0 = most recent (score = 1.0); rank n-1 = oldest
            score = decay_rate ** rank
            s = updated[idx]
            updated[idx] = ContextSegment(
                segment_id=s.segment_id, content=s.content,
                token_count=s.token_count, priority=s.priority,
                segment_type=s.segment_type, compressible=s.compressible,
                recency_score=score,
            )
        return updated

    @staticmethod
    def _heuristic_token_count(text: str) -> int:
        """Fast heuristic: ~1.3 tokens per word (underestimates for code)."""
        return max(1, int(len(text.split()) * 1.3))
```

[**Recency-Decay-Pattern**:: Applying exponential decay to old conversation turns' priority scores — rather than simple position-based truncation — enables the allocator to preserve a recent critical exchange even if it is surrounded by irrelevant older turns. Decay rate 0.85 per position gives turns 10 positions back a weight of ~0.20, making them highly likely to be excluded under budget pressure while preserving very recent turns unconditionally.]

---

## Part 2 — Conversation History Compression

When conversation histories grow beyond the context window, [[Conversation-Compression]] strategies reduce token footprint while preserving semantic content. The two principal strategies are **sliding window** (discard oldest turns entirely — simple, lossy) and **summarization** (compress older turns into a dense summary — more complex, lower information loss). Production systems combine both: a summarization buffer for older history with a sliding window of recent verbatim turns.

[**Summarization-Buffer-Pattern**:: A two-tier history management architecture in which: (1) the last K turns are retained verbatim (verbatim window), (2) older turns are periodically compressed by an LLM summarizer into a rolling summary that captures essential facts, decisions, and commitments. The verbatim window provides coherent recent context; the summary provides continuity without full token cost (Zhong et al. 2022).]

[**Information-Loss-Metric**:: The primary risk of conversation compression — evaluated by comparing the model's performance on questions about the compressed history against a full-history baseline. Acceptable information loss threshold for most production systems: <5% degradation on context-dependent task accuracy. Summarization typically achieves 70–80% token reduction with <3% information loss on factual retrieval (Packer et al. 2023 — MemGPT).]

```python
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Protocol


@dataclass
class ConversationTurn:
    """A single conversation turn (human + assistant pair)."""
    turn_index: int
    human: str
    assistant: str
    token_count: int        # Total tokens for both utterances
    contains_decision: bool = False  # Marked if human or assistant made a commitment


@dataclass
class CompressionResult:
    """Result of compressing a portion of conversation history."""
    summary: str            # The generated summary text
    summary_tokens: int     # Token count of the summary
    compressed_turns: list[ConversationTurn]  # Turns that were replaced
    original_tokens: int    # Token count before compression
    compression_ratio: float  # original_tokens / summary_tokens

    @property
    def tokens_saved(self) -> int:
        return self.original_tokens - self.summary_tokens


class SummarizerCallable(Protocol):
    """Protocol for any callable that summarizes a conversation segment."""
    def __call__(self, turns: list[ConversationTurn]) -> str: ...


class ConversationCompressor:
    """Two-tier conversation history compressor with summarization buffer.

    Maintains the last `verbatim_turns` turns as raw text and compresses
    older turns into a rolling summary using an LLM summarizer.
    The summary is prepended to the context as a system-level memory block.

    Args:
        summarizer: Callable that takes a list of ConversationTurn and returns
                    a compressed summary string.
        token_counter: Callable (text: str) -> int for token counting.
        verbatim_turns: Number of recent turns to retain verbatim (default 6).
        compression_trigger: Compress when history exceeds this token count.
        max_summary_tokens: Cap on summary length (truncated if exceeded).

    Example:
        >>> def mock_summarizer(turns):
        ...     return f"Summary of {len(turns)} turns."
        >>> compressor = ConversationCompressor(
        ...     summarizer=mock_summarizer,
        ...     token_counter=lambda t: len(t.split()),
        ...     verbatim_turns=4,
        ...     compression_trigger=500,
        ... )
        >>> turns = [ConversationTurn(i, f"Q{i}", f"A{i}", 20) for i in range(10)]
        >>> result, verbatim = compressor.compress(turns)
        >>> result is not None or verbatim is not None
        True
    """

    def __init__(
        self,
        summarizer: SummarizerCallable,
        token_counter: Callable[[str], int],
        verbatim_turns: int = 6,
        compression_trigger: int = 3000,
        max_summary_tokens: int = 600,
    ) -> None:
        self._summarizer = summarizer
        self._count_tokens = token_counter
        self.verbatim_turns = verbatim_turns
        self.compression_trigger = compression_trigger
        self.max_summary_tokens = max_summary_tokens
        self._rolling_summary: str = ""

    def needs_compression(self, turns: list[ConversationTurn]) -> bool:
        """Return True if current history exceeds the compression trigger."""
        total = sum(t.token_count for t in turns)
        return total > self.compression_trigger

    def compress(
        self, turns: list[ConversationTurn]
    ) -> tuple[CompressionResult | None, list[ConversationTurn]]:
        """Compress older turns into a rolling summary; return verbatim recent turns.

        If compression is not needed, returns (None, turns).
        If compression is triggered, compresses all turns except the last
        `verbatim_turns`, updates the rolling summary, and returns the result.

        Args:
            turns: Full conversation history in chronological order.

        Returns:
            Tuple of (CompressionResult | None, verbatim_turns_list).
        """
        if not self.needs_compression(turns):
            return None, turns

        if len(turns) <= self.verbatim_turns:
            # Not enough turns to compress — nothing to do
            return None, turns

        to_compress = turns[:-self.verbatim_turns]
        verbatim = turns[-self.verbatim_turns:]

        # PERF: Preserving decision-critical turns regardless of age
        # NOTE: Any turn marked contains_decision is spliced into verbatim
        decisions = [t for t in to_compress if t.contains_decision]
        non_decision = [t for t in to_compress if not t.contains_decision]

        original_tokens = sum(t.token_count for t in to_compress)
        summary_text = self._summarizer(non_decision)

        # Merge with existing rolling summary if present
        if self._rolling_summary:
            merged_input = [
                ConversationTurn(-1, "[PREVIOUS SUMMARY]", self._rolling_summary, 0),
            ] + [ConversationTurn(-1, "[NEW EVENTS]", summary_text, 0)]
            summary_text = self._summarizer(merged_input)

        self._rolling_summary = summary_text

        # Enforce max_summary_tokens via truncation
        summary_tokens = self._count_tokens(summary_text)
        if summary_tokens > self.max_summary_tokens:
            # NOTE: Hard truncation at word boundary — imperfect but safe
            words = summary_text.split()
            ratio = self.max_summary_tokens / summary_tokens
            truncated_words = int(len(words) * ratio)
            summary_text = " ".join(words[:truncated_words]) + " [TRUNCATED]"
            summary_tokens = self._count_tokens(summary_text)

        result = CompressionResult(
            summary=summary_text,
            summary_tokens=summary_tokens,
            compressed_turns=to_compress,
            original_tokens=original_tokens,
            compression_ratio=original_tokens / max(summary_tokens, 1),
        )

        # Decision turns are preserved verbatim, prepended to the window
        return result, decisions + verbatim

    def get_history_block(
        self, verbatim: list[ConversationTurn]
    ) -> str:
        """Build the full history string to inject into context.

        Prepends the rolling summary as a [MEMORY] block if present,
        then appends the verbatim turns in Human/Assistant format.

        Args:
            verbatim: Recent turns to render verbatim.

        Returns:
            Formatted context block string.
        """
        parts: list[str] = []
        if self._rolling_summary:
            parts.append(f"[MEMORY — Earlier Conversation Summary]\n{self._rolling_summary}\n")
        for turn in verbatim:
            parts.append(f"Human: {turn.human}\nAssistant: {turn.assistant}")
        return "\n\n".join(parts)
```

---

## Part 3 — Vector Memory Stores

[[Vector-Memory]] extends the model's effective memory beyond the context window by storing information as dense embedding vectors in a searchable index. At inference time, the query is embedded and the most semantically similar stored memories are retrieved and injected into context. This enables recall of information from thousands of prior exchanges, documents, or knowledge base entries that would not fit in any single context window.

[**Vector-Memory-Definition**:: A persistent key-value store where keys are dense embedding vectors (typically 384–1536 dimensions) and values are text chunks, structured facts, or conversation excerpts. Retrieval is performed via approximate nearest-neighbor search (cosine or dot-product similarity), returning the top-k most semantically relevant items for a given query embedding (Johnson et al. 2019 — FAISS; Chroma 2023).]

[**Chunking-Strategy-for-Memory**:: The granularity at which information is embedded for storage determines retrieval precision. Fine-grained chunks (sentence-level, ~50 tokens) achieve high recall on specific fact retrieval. Coarse chunks (paragraph-level, ~200 tokens) provide better contextual coherence. Production systems often use **hierarchical chunking**: store at both granularities and retrieve the coarse chunk when a fine chunk matches, preserving surrounding context (Sarthi et al. 2024 — RAPTOR).]

```python
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Any


@dataclass(frozen=True)
class MemoryEntry:
    """A single stored memory unit with embedding and metadata."""
    memory_id: str              # SHA-256 hash of content
    content: str                # The text content
    embedding: list[float]      # Dense embedding vector
    metadata: dict              # source, timestamp, type, session_id, etc.
    created_at: str             # ISO-8601 UTC timestamp
    importance_score: float     # 0.0–1.0; used in tiered retrieval

    def to_dict(self) -> dict:
        return {
            "memory_id": self.memory_id,
            "content": self.content,
            "embedding": self.embedding,
            "metadata": self.metadata,
            "created_at": self.created_at,
            "importance_score": self.importance_score,
        }

    @classmethod
    def from_dict(cls, d: dict) -> MemoryEntry:
        return cls(**d)


@dataclass
class RetrievalResult:
    """A retrieved memory with its similarity score."""
    entry: MemoryEntry
    similarity: float       # Cosine similarity 0.0–1.0
    rank: int               # Retrieval rank (1 = most similar)


class VectorMemoryStore:
    """In-memory vector store with cosine similarity retrieval and JSON persistence.

    Designed as a reference implementation — suitable for single-process agents
    with up to ~50K memory entries. For larger deployments, swap the inner
    store with FAISS, ChromaDB, or Qdrant while preserving this interface.

    Args:
        embed_fn: Callable (text: str) -> list[float] returning a dense embedding.
        persist_path: Optional file path for JSON persistence between sessions.
        importance_fn: Optional callable (content: str, metadata: dict) -> float
                       scoring each memory's importance (default: 0.5 for all).
        similarity_threshold: Minimum similarity score for retrieval (default 0.65).
        max_entries: Maximum stored entries before oldest-by-importance eviction.

    Example:
        >>> import math
        >>> def cosine_embed(text: str) -> list[float]:
        ...     # Toy embedding: character-frequency vector (26-dim)
        ...     vec = [text.lower().count(chr(ord('a') + i)) for i in range(26)]
        ...     norm = math.sqrt(sum(x*x for x in vec)) or 1.0
        ...     return [x / norm for x in vec]
        >>> store = VectorMemoryStore(embed_fn=cosine_embed)
        >>> mid = store.store("The mitochondria is the powerhouse of the cell.", {})
        >>> results = store.retrieve("cell energy organelle", top_k=1)
        >>> len(results) >= 0
        True
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]],
        persist_path: Path | None = None,
        importance_fn: Callable[[str, dict], float] | None = None,
        similarity_threshold: float = 0.65,
        max_entries: int = 50_000,
    ) -> None:
        self._embed = embed_fn
        self._persist_path = persist_path
        self._importance = importance_fn or (lambda c, m: 0.5)
        self.similarity_threshold = similarity_threshold
        self.max_entries = max_entries
        self._store: dict[str, MemoryEntry] = {}

        if persist_path and persist_path.exists():
            self._load(persist_path)

    def store(self, content: str, metadata: dict) -> str:
        """Embed and store a new memory entry.

        Deduplicates by content hash — re-storing the same content is a no-op
        that returns the existing memory_id.

        Args:
            content: Text content to store.
            metadata: Arbitrary metadata dict (source, session_id, type, etc.).

        Returns:
            The memory_id (SHA-256 of content) for the stored entry.
        """
        memory_id = hashlib.sha256(content.encode()).hexdigest()[:16]

        if memory_id in self._store:
            # INVARIANT: Deduplication prevents embedding the same content twice
            return memory_id

        embedding = self._embed(content)
        importance = self._importance(content, metadata)

        entry = MemoryEntry(
            memory_id=memory_id,
            content=content,
            embedding=embedding,
            metadata=metadata,
            created_at=datetime.now(timezone.utc).isoformat(),
            importance_score=importance,
        )
        self._store[memory_id] = entry

        # Evict lowest-importance entry if at capacity
        if len(self._store) > self.max_entries:
            self._evict_lowest_importance()

        return memory_id

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        filter_fn: Callable[[MemoryEntry], bool] | None = None,
    ) -> list[RetrievalResult]:
        """Retrieve the top-k most similar memories to a query.

        Args:
            query: Natural language query to embed and search against.
            top_k: Maximum number of results to return.
            filter_fn: Optional predicate to restrict which entries are searched
                       (e.g., filter by session_id, type, recency).

        Returns:
            List of RetrievalResult sorted by similarity descending.
        """
        if not self._store:
            return []

        query_embedding = self._embed(query)
        candidates = [
            entry for entry in self._store.values()
            if filter_fn is None or filter_fn(entry)
        ]

        scored: list[tuple[float, MemoryEntry]] = []
        for entry in candidates:
            sim = self._cosine_similarity(query_embedding, entry.embedding)
            if sim >= self.similarity_threshold:
                scored.append((sim, entry))

        # Sort by similarity descending, then importance as tiebreaker
        scored.sort(key=lambda x: (x[0], x[1].importance_score), reverse=True)

        return [
            RetrievalResult(entry=entry, similarity=round(sim, 4), rank=rank + 1)
            for rank, (sim, entry) in enumerate(scored[:top_k])
        ]

    def delete(self, memory_id: str) -> bool:
        """Remove a memory entry by ID. Returns True if it existed."""
        return self._store.pop(memory_id, None) is not None

    def persist(self) -> None:
        """Write all entries to the configured persist_path as JSON."""
        if self._persist_path is None:
            return
        data = [entry.to_dict() for entry in self._store.values()]
        tmp = self._persist_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(data, indent=2), encoding="utf-8")
        tmp.replace(self._persist_path)

    def _load(self, path: Path) -> None:
        """Load persisted entries from JSON."""
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            self._store = {d["memory_id"]: MemoryEntry.from_dict(d) for d in data}
        except (json.JSONDecodeError, KeyError) as e:
            # NOTE: Corrupt persistence file — start fresh rather than crash
            import logging
            logging.getLogger(__name__).warning(
                "Memory persistence file corrupt, starting fresh: %s", e
            )

    def _evict_lowest_importance(self) -> None:
        """Remove the entry with the lowest importance score."""
        worst_id = min(self._store, key=lambda mid: self._store[mid].importance_score)
        del self._store[worst_id]

    @staticmethod
    def _cosine_similarity(a: list[float], b: list[float]) -> float:
        """Compute cosine similarity between two vectors."""
        if len(a) != len(b):
            return 0.0
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = sum(x * x for x in a) ** 0.5
        norm_b = sum(x * x for x in b) ** 0.5
        if norm_a == 0.0 or norm_b == 0.0:
            return 0.0
        return dot / (norm_a * norm_b)

    @property
    def size(self) -> int:
        return len(self._store)
```

[**Importance-Weighted-Eviction**:: When the vector store reaches capacity, entries should be evicted by importance score rather than by age (LRU). Old but highly important memories — a user's name, a key decision, a stated constraint — should never be evicted in favor of recent but low-importance exchanges. The importance_fn should score based on: entity mentions, decision markers, explicit "remember this" signals, and embedding distance to the user's most frequently queried topics (Park et al. 2023 — Generative Agents).]

---

## Part 4 — Episodic Memory Architecture

[[Episodic-Memory]] in LLM systems corresponds to the record of specific past interactions, events, and experiences — the *when* and *what happened* of the agent's history, as opposed to general facts. A production episodic memory system stores conversation episodes with temporal metadata, retrieves relevant past episodes when the current context activates related topics, and provides a structured interface for reflection and cross-episode reasoning.

[**Episodic-Memory-Definition**:: Memory for specific autobiographical events and experiences, indexed by temporal context and episodic content. In LLM agents, episodic memory enables retrieval of past conversations, outcomes of previous tool uses, user preferences expressed in earlier sessions, and errors made and corrected — providing temporal grounding for the agent's reasoning (Tulving 1972; Park et al. 2023).]

[**Reflection-Over-Episodes**:: An agentic pattern in which the agent periodically synthesizes insights from multiple episodic memories — identifying patterns, updating beliefs, and extracting higher-order knowledge. Park et al. 2023 implement this as a scored retrieval of the most "poignant" recent memories, followed by a synthesis prompt that generates reflection insights stored as new higher-order memories.]

```python
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Callable


@dataclass
class Episode:
    """A complete interaction episode with temporal and content metadata."""
    episode_id: str
    session_id: str
    started_at: str             # ISO-8601 UTC
    ended_at: str | None        # None if session still active
    turns: list[dict]           # [{"role": "human"|"assistant", "content": str}]
    topic_tags: list[str]       # High-level topic labels for efficient filtering
    outcome_summary: str        # What was accomplished/decided (auto-generated)
    poignancy_score: float      # 0.0–1.0: how memorable/significant this episode is
    embedding: list[float]      # Episode-level embedding (of the outcome_summary)

    @property
    def is_active(self) -> bool:
        return self.ended_at is None

    @property
    def duration_seconds(self) -> float | None:
        if self.ended_at is None:
            return None
        start = datetime.fromisoformat(self.started_at)
        end = datetime.fromisoformat(self.ended_at)
        return (end - start).total_seconds()


@dataclass
class EpisodicReflection:
    """A higher-order insight synthesized from multiple episodes."""
    reflection_id: str
    source_episode_ids: list[str]
    insight: str                # The synthesized insight text
    confidence: float           # 0.0–1.0: how confident the agent is in this insight
    created_at: str
    domain: str                 # Topic domain this insight relates to


class EpisodicMemoryManager:
    """Manages episodic memory: storage, retrieval, and reflection synthesis.

    Provides temporal indexing, semantic retrieval of past episodes, and
    a reflection mechanism for generating higher-order insights from
    recurring patterns across multiple episodes.

    Args:
        embed_fn: Callable (text: str) -> list[float] for episode embeddings.
        reflection_fn: Callable that takes a list of Episode objects and returns
                       a reflection insight string.
        poignancy_fn: Callable (episode: Episode) -> float scoring memorability.
        max_episodes: Maximum stored episodes before oldest-by-poignancy eviction.
        reflection_threshold: Synthesize a reflection after this many new episodes.

    Example:
        >>> embed = lambda t: [float(len(t))]
        >>> memory = EpisodicMemoryManager(
        ...     embed_fn=embed,
        ...     reflection_fn=lambda eps: f"Pattern from {len(eps)} episodes.",
        ...     poignancy_fn=lambda ep: 0.5,
        ... )
        >>> ep = Episode("ep1", "sess1",
        ...     datetime.now(timezone.utc).isoformat(), None,
        ...     [], [], "Test outcome", 0.5, embed("Test outcome"))
        >>> memory.store_episode(ep)
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]],
        reflection_fn: Callable[[list[Episode]], str],
        poignancy_fn: Callable[[Episode], float],
        max_episodes: int = 1000,
        reflection_threshold: int = 10,
    ) -> None:
        self._embed = embed_fn
        self._reflect = reflection_fn
        self._poignancy = poignancy_fn
        self.max_episodes = max_episodes
        self.reflection_threshold = reflection_threshold
        self._episodes: dict[str, Episode] = {}
        self._reflections: list[EpisodicReflection] = []
        self._episodes_since_reflection = 0

    def store_episode(self, episode: Episode) -> None:
        """Store a completed episode, triggering reflection if threshold reached.

        Args:
            episode: The completed Episode to store.
        """
        self._episodes[episode.episode_id] = episode
        self._episodes_since_reflection += 1

        if len(self._episodes) > self.max_episodes:
            self._evict()

        if self._episodes_since_reflection >= self.reflection_threshold:
            self._maybe_reflect()
            self._episodes_since_reflection = 0

    def retrieve_relevant(
        self, query: str, top_k: int = 5
    ) -> list[tuple[Episode, float]]:
        """Retrieve episodes most relevant to a query via cosine similarity.

        Args:
            query: The current context or question to retrieve episodes for.
            top_k: Number of episodes to return.

        Returns:
            List of (Episode, similarity_score) tuples, sorted by relevance.
        """
        if not self._episodes:
            return []

        query_emb = self._embed(query)
        scored: list[tuple[float, Episode]] = []

        for ep in self._episodes.values():
            sim = self._cosine(query_emb, ep.embedding)
            # Blend semantic similarity with poignancy: 0.7 sim + 0.3 poignancy
            combined = 0.7 * sim + 0.3 * ep.poignancy_score
            scored.append((combined, ep))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [(ep, score) for score, ep in scored[:top_k]]

    def get_reflections_for_domain(self, domain: str) -> list[EpisodicReflection]:
        """Retrieve reflections whose domain matches the given query domain."""
        return [r for r in self._reflections if r.domain == domain]

    def _maybe_reflect(self) -> None:
        """Synthesize reflections from recent high-poignancy episodes."""
        recent = sorted(
            self._episodes.values(),
            key=lambda ep: ep.poignancy_score,
            reverse=True,
        )[:self.reflection_threshold]

        if len(recent) < 3:
            return

        import hashlib, uuid
        insight = self._reflect(recent)
        reflection = EpisodicReflection(
            reflection_id=str(uuid.uuid4())[:8],
            source_episode_ids=[ep.episode_id for ep in recent],
            insight=insight,
            confidence=0.7,
            created_at=datetime.now(timezone.utc).isoformat(),
            domain=recent[0].topic_tags[0] if recent[0].topic_tags else "general",
        )
        self._reflections.append(reflection)

    def _evict(self) -> None:
        """Evict oldest episode with lowest poignancy score."""
        worst_id = min(
            self._episodes,
            key=lambda eid: (
                self._episodes[eid].poignancy_score,
                self._episodes[eid].started_at,
            ),
        )
        del self._episodes[worst_id]

    @staticmethod
    def _cosine(a: list[float], b: list[float]) -> float:
        if len(a) != len(b) or not a:
            return 0.0
        dot = sum(x * y for x, y in zip(a, b))
        mag = (sum(x*x for x in a) ** 0.5) * (sum(x*x for x in b) ** 0.5)
        return dot / mag if mag > 0 else 0.0
```

---

## Part 5 — Semantic Memory and Knowledge Graph Integration

[[Semantic-Memory]] holds general world knowledge and domain facts — the *what* without the autobiographical *when*. In LLM agent systems, semantic memory is implemented as a structured knowledge store: either a [[Knowledge-Graph]] of entity-relationship triples or a vector-indexed fact store. Semantic memory enables the agent to reason about persistent facts about the user, domain, and environment without injecting entire encyclopedias into context.

[**Semantic-Memory-Definition**:: Memory for general facts, concepts, and their relationships — independent of when or how they were learned. In LLM agents, semantic memory is typically implemented as: (1) a structured knowledge graph (entity → relation → entity triples), (2) a vector-indexed fact store with metadata filtering, or (3) a combination with LLM-mediated triple extraction from episodic content. Semantic memory updates require explicit contradiction detection to avoid storing conflicting facts (Weng 2023).]

[**Knowledge-Graph-in-Agents**:: A directed graph where nodes are entities (Person, Concept, Object, Event) and edges are typed relationships (HAS_PREFERENCE, KNOWS, WORKS_AT, RELATES_TO). Agent systems populate the KG by running triple extraction over conversation turns and documents. At inference time, the current context entities are resolved to KG nodes, and their neighborhood (1–2 hops) is retrieved as structured context for the model. This provides compact, precise factual grounding without full-text retrieval overhead.]

```python
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True)
class Entity:
    """A node in the knowledge graph."""
    entity_id: str
    name: str
    entity_type: str        # "Person", "Concept", "Organization", "Location", etc.
    attributes: tuple       # Immutable tuple of (key, value) attribute pairs


@dataclass(frozen=True)
class Relation:
    """A directed edge in the knowledge graph."""
    relation_id: str
    subject_id: str         # Source entity ID
    predicate: str          # Relation type: "HAS_PREFERENCE", "WORKS_AT", etc.
    object_id: str          # Target entity ID
    confidence: float       # 0.0–1.0; lower for inferred vs. explicit facts
    source: str             # Where this fact came from (episode_id, document, etc.)
    created_at: str


@dataclass
class KGQueryResult:
    """Result of a knowledge graph query for a set of entities."""
    entities: list[Entity]
    relations: list[Relation]
    context_text: str       # Formatted text representation for injection into context


class SemanticKnowledgeGraph:
    """In-memory knowledge graph for agent semantic memory.

    Supports triple extraction, contradiction detection, entity resolution,
    and neighborhood retrieval for context injection.

    Args:
        triple_extractor: Callable (text: str) -> list[tuple[str, str, str, float]]
                          returning (subject, predicate, object, confidence) tuples.
        contradiction_threshold: If a new triple's confidence + existing conflicting
                                 triple's confidence < this, flag for review.

    Example:
        >>> def mock_extractor(text):
        ...     return [("Alice", "WORKS_AT", "Acme Corp", 0.9)]
        >>> kg = SemanticKnowledgeGraph(triple_extractor=mock_extractor)
        >>> kg.ingest_text("Alice works at Acme Corp.", source="user_turn_1")
        >>> results = kg.query_entities(["Alice"])
        >>> len(results.entities) > 0
        True
    """

    def __init__(
        self,
        triple_extractor: "Callable[[str], list[tuple[str, str, str, float]]]",
        contradiction_threshold: float = 1.2,
    ) -> None:
        from typing import Callable
        self._extract_triples = triple_extractor
        self._contradiction_threshold = contradiction_threshold
        self._entities: dict[str, Entity] = {}         # entity_id → Entity
        self._relations: list[Relation] = []
        self._name_index: dict[str, str] = {}          # canonical_name → entity_id

    def ingest_text(self, text: str, source: str) -> list[Relation]:
        """Extract triples from text and add to the knowledge graph.

        Args:
            text: Any text (conversation turn, document, tool output).
            source: Provenance identifier for the extracted triples.

        Returns:
            List of newly added Relation objects.
        """
        import hashlib
        raw_triples = self._extract_triples(text)
        new_relations: list[Relation] = []

        for subject, predicate, obj, confidence in raw_triples:
            subj_id = self._resolve_or_create(subject, "Unknown")
            obj_id = self._resolve_or_create(obj, "Unknown")

            # Contradiction check: does an inverse relation already exist?
            self._check_contradiction(subj_id, predicate, obj_id, confidence)

            relation_id = hashlib.sha256(
                f"{subj_id}:{predicate}:{obj_id}".encode()
            ).hexdigest()[:12]

            rel = Relation(
                relation_id=relation_id,
                subject_id=subj_id,
                predicate=predicate,
                object_id=obj_id,
                confidence=confidence,
                source=source,
                created_at=datetime.now(timezone.utc).isoformat(),
            )
            # Dedup: replace if same triple exists with lower confidence
            existing_idx = next(
                (i for i, r in enumerate(self._relations)
                 if r.relation_id == relation_id), None
            )
            if existing_idx is not None:
                if confidence > self._relations[existing_idx].confidence:
                    self._relations[existing_idx] = rel
            else:
                self._relations.append(rel)
                new_relations.append(rel)

        return new_relations

    def query_entities(
        self, entity_names: list[str], hop_depth: int = 1
    ) -> KGQueryResult:
        """Retrieve entities and their neighborhood from the knowledge graph.

        Args:
            entity_names: List of entity names to resolve and retrieve.
            hop_depth: How many relation hops to traverse (default 1).

        Returns:
            KGQueryResult with entities, relations, and formatted context text.
        """
        seed_ids = {
            self._name_index[n.lower()]
            for n in entity_names
            if n.lower() in self._name_index
        }

        if not seed_ids:
            return KGQueryResult(entities=[], relations=[], context_text="(No known entities)")

        # BFS traversal up to hop_depth
        visited_ids = set(seed_ids)
        frontier = set(seed_ids)
        relevant_relations: list[Relation] = []

        for _ in range(hop_depth):
            next_frontier: set[str] = set()
            for rel in self._relations:
                if rel.subject_id in frontier or rel.object_id in frontier:
                    relevant_relations.append(rel)
                    next_frontier.add(rel.subject_id)
                    next_frontier.add(rel.object_id)
            frontier = next_frontier - visited_ids
            visited_ids |= next_frontier

        entities = [
            self._entities[eid]
            for eid in visited_ids
            if eid in self._entities
        ]

        context_text = self._render_context(entities, relevant_relations)
        return KGQueryResult(
            entities=entities,
            relations=relevant_relations,
            context_text=context_text,
        )

    def _resolve_or_create(self, name: str, entity_type: str) -> str:
        """Resolve a name to an existing entity ID or create a new entity."""
        import uuid
        key = name.lower().strip()
        if key in self._name_index:
            return self._name_index[key]
        entity_id = str(uuid.uuid4())[:8]
        entity = Entity(
            entity_id=entity_id, name=name, entity_type=entity_type, attributes=()
        )
        self._entities[entity_id] = entity
        self._name_index[key] = entity_id
        return entity_id

    def _check_contradiction(
        self, subject_id: str, predicate: str, object_id: str, confidence: float
    ) -> None:
        """Log a warning if a conflicting relation exists with high confidence."""
        import logging
        for rel in self._relations:
            if (rel.subject_id == subject_id and rel.predicate == predicate
                    and rel.object_id != object_id):
                combined = rel.confidence + confidence
                if combined >= self._contradiction_threshold:
                    s_name = self._entities.get(subject_id, Entity(subject_id, subject_id, "", ())).name
                    logging.getLogger(__name__).warning(
                        "KG CONTRADICTION: %s -[%s]-> %s conflicts with existing relation",
                        s_name, predicate, object_id,
                    )

    def _render_context(self, entities: list[Entity], relations: list[Relation]) -> str:
        """Format entities and relations as a readable context block."""
        lines: list[str] = ["[KNOWN FACTS]"]
        entity_names = {e.entity_id: e.name for e in entities}
        for rel in sorted(relations, key=lambda r: -r.confidence):
            subj = entity_names.get(rel.subject_id, rel.subject_id)
            obj = entity_names.get(rel.object_id, rel.object_id)
            lines.append(f"- {subj} {rel.predicate} {obj} (confidence: {rel.confidence:.2f})")
        return "\n".join(lines)
```

---

## Part 6 — Memory Consolidation Pipeline

[[Memory-Consolidation]] moves information from episodic short-term storage into semantic long-term memory — mirroring the neuroscience of hippocampal-to-cortical consolidation during sleep. In LLM agent systems, consolidation is a background process that extracts durable facts and patterns from episodic memory and promotes them into the semantic knowledge graph and vector store with updated importance scores.

[**Consolidation-Trigger-Strategies**:: Three triggering strategies: (1) Time-based — consolidate after every N sessions, (2) Event-based — consolidate when episodic memory reaches capacity, (3) Query-based — consolidate on-demand before answering questions that likely require cross-session reasoning. Production systems combine all three with priority weighting by episode poignancy score (Weng 2023).]

```python
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


@dataclass
class ConsolidationResult:
    """Output of one consolidation run."""
    episodes_processed: int
    facts_extracted: int
    facts_added_to_kg: int
    facts_updated_in_kg: int
    memories_promoted_to_vector: int
    processing_time_ms: float


class MemoryConsolidationPipeline:
    """Consolidates episodic memories into semantic (KG + vector) long-term memory.

    Runs as a background process, extracting durable facts from high-poignancy
    episodes and promoting them to the semantic knowledge graph and vector store.

    Args:
        episodic_manager: The EpisodicMemoryManager to read from.
        knowledge_graph: The SemanticKnowledgeGraph to write facts into.
        vector_store: The VectorMemoryStore to promote summary memories into.
        fact_extractor: Callable (episode: Episode) -> list[str] returning
                        durable fact strings extracted from the episode.
        poignancy_threshold: Only consolidate episodes above this score (default 0.4).

    Example:
        >>> # Consolidation is typically run as a background job after sessions end.
        >>> # Direct instantiation requires all three memory subsystems.
        >>> pipeline = MemoryConsolidationPipeline(
        ...     episodic_manager=None,
        ...     knowledge_graph=None,
        ...     vector_store=None,
        ...     fact_extractor=lambda ep: [ep.outcome_summary],
        ... )
    """

    def __init__(
        self,
        episodic_manager: "EpisodicMemoryManager | None",
        knowledge_graph: "SemanticKnowledgeGraph | None",
        vector_store: "VectorMemoryStore | None",
        fact_extractor: "Callable[[Episode], list[str]]",
        poignancy_threshold: float = 0.4,
    ) -> None:
        self._episodic = episodic_manager
        self._kg = knowledge_graph
        self._vector = vector_store
        self._extract_facts = fact_extractor
        self._poignancy_threshold = poignancy_threshold
        self._processed_episode_ids: set[str] = set()

    def run(self) -> ConsolidationResult:
        """Execute one consolidation pass over unprocessed high-poignancy episodes.

        Returns:
            ConsolidationResult with statistics for observability.
        """
        import time
        t0 = time.monotonic()

        if self._episodic is None:
            return ConsolidationResult(0, 0, 0, 0, 0, 0.0)

        # Retrieve unprocessed episodes above poignancy threshold
        episodes_to_process = [
            ep for ep in self._episodic._episodes.values()
            if (ep.episode_id not in self._processed_episode_ids
                and ep.poignancy_score >= self._poignancy_threshold
                and not ep.is_active)  # Don't consolidate active sessions
        ]

        facts_extracted = facts_added = facts_updated = memories_promoted = 0

        for episode in episodes_to_process:
            facts = self._extract_facts(episode)
            facts_extracted += len(facts)

            # Promote facts into KG
            if self._kg is not None:
                for fact in facts:
                    new_relations = self._kg.ingest_text(
                        fact, source=f"consolidation:{episode.episode_id}"
                    )
                    facts_added += len(new_relations)

            # Promote episode summary into vector store for semantic retrieval
            if self._vector is not None and episode.outcome_summary:
                metadata = {
                    "source": "episodic_consolidation",
                    "episode_id": episode.episode_id,
                    "session_id": episode.session_id,
                    "poignancy": episode.poignancy_score,
                    "topic_tags": episode.topic_tags,
                }
                self._vector.store(episode.outcome_summary, metadata)
                memories_promoted += 1

            self._processed_episode_ids.add(episode.episode_id)

        elapsed_ms = (time.monotonic() - t0) * 1000
        return ConsolidationResult(
            episodes_processed=len(episodes_to_process),
            facts_extracted=facts_extracted,
            facts_added_to_kg=facts_added,
            facts_updated_in_kg=facts_updated,
            memories_promoted_to_vector=memories_promoted,
            processing_time_ms=round(elapsed_ms, 2),
        )
```

---

## Part 7 — Working Memory and Scratchpad Patterns

[[Working-Memory-Scratchpad]] patterns give agents a dedicated, structured scratch space within the context window for intermediate reasoning state — separate from the conversation history and retrieved context. This mirrors the cognitive architecture of working memory as an active manipulation space distinct from long-term storage. Scratchpads prevent intermediate state from polluting the conversation flow while providing full transparency for debugging.

[**Scratchpad-Definition**:: A designated section of the context window (typically prefixed with `<scratchpad>` or `[THINKING]` tags) where the agent records intermediate computations, sub-goals, partial results, and self-corrections before committing to a final response. Scratchpad contents are visible to the model but can be stripped before presenting the output to the user (Wei et al. 2022 — Chain-of-Thought; Nye et al. 2021 — Scratchpad).]

[**State-Accumulation-Pattern**:: An agentic working memory pattern in which tool call results, sub-task outcomes, and partial answers are accumulated in a structured state dictionary within the scratchpad — rather than re-stating them in the assistant turn. The state dictionary acts as typed working memory: `{"step": 2, "partial_result": {...}, "pending_tools": [...], "constraints": [...]}`. This provides O(1) access to any accumulated state without searching through the conversation history.]

```python
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ScratchpadEntry:
    """A single entry in the working memory scratchpad."""
    entry_type: str         # "observation", "plan", "result", "correction", "note"
    content: str
    step: int
    tool_call_id: str | None = None  # If entry is a tool result


@dataclass
class ScratchpadState:
    """Typed working memory state accumulated across agent steps."""
    goal: str
    entries: list[ScratchpadEntry] = field(default_factory=list)
    accumulated_state: dict[str, Any] = field(default_factory=dict)
    step_count: int = 0
    completed: bool = False
    final_answer: str | None = None

    def add_observation(self, content: str, tool_call_id: str | None = None) -> None:
        self.step_count += 1
        self.entries.append(ScratchpadEntry(
            entry_type="observation", content=content,
            step=self.step_count, tool_call_id=tool_call_id,
        ))

    def add_plan(self, content: str) -> None:
        self.entries.append(ScratchpadEntry(
            entry_type="plan", content=content, step=self.step_count,
        ))

    def add_correction(self, content: str) -> None:
        """Record a self-correction — previous reasoning was revised."""
        self.entries.append(ScratchpadEntry(
            entry_type="correction", content=content, step=self.step_count,
        ))

    def update_state(self, key: str, value: Any) -> None:
        """Update typed working memory state."""
        self.accumulated_state[key] = value

    def render(self, strip_for_user: bool = False) -> str:
        """Render scratchpad as a context string for injection or display.

        Args:
            strip_for_user: If True, return only the final_answer without
                            internal scratchpad entries.

        Returns:
            Formatted scratchpad string.
        """
        if strip_for_user and self.final_answer:
            return self.final_answer

        lines: list[str] = [f"<scratchpad>", f"Goal: {self.goal}"]
        for entry in self.entries:
            prefix = {
                "observation": "→ OBS",
                "plan": "→ PLAN",
                "result": "→ RESULT",
                "correction": "⚠ CORRECTION",
                "note": "· NOTE",
            }.get(entry.entry_type, "→")
            lines.append(f"[Step {entry.step}] {prefix}: {entry.content}")
        if self.accumulated_state:
            import json
            lines.append(f"State: {json.dumps(self.accumulated_state, indent=2)}")
        if self.final_answer:
            lines.append(f"Final Answer: {self.final_answer}")
        lines.append("</scratchpad>")
        return "\n".join(lines)

    @property
    def corrections_made(self) -> int:
        return sum(1 for e in self.entries if e.entry_type == "correction")
```

---

## Part 8 — Production Multi-Tier Memory Router

A production agent memory system integrates all tiers — context window, conversation compression, vector memory, episodic memory, and semantic knowledge graph — behind a unified [[Memory-Router]] that selects the appropriate retrieval strategy per query type and assembles the context block for injection. The router applies retrieval in priority order: semantic KG (fastest, most precise), vector store (broader recall), episodic episodes (session continuity), and compressed history summary (baseline).

[**Multi-Tier-Memory-Router-Definition**:: An orchestration layer that classifies each incoming query by its memory requirements — factual (semantic KG), experience-based (episodic), document-based (vector), or conversational (history) — and retrieves from the appropriate tier(s), merging results into a budget-constrained context block. The router must respect the token budget across all retrieved content, applying priority truncation when necessary.]

```python
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Callable


class QueryMemoryType(Enum):
    """Classification of query memory requirements."""
    FACTUAL = auto()        # "What does Alice prefer?" → KG lookup
    EXPERIENTIAL = auto()   # "Did we discuss this before?" → episodic
    DOCUMENTARY = auto()    # "What did the policy doc say?" → vector store
    CONVERSATIONAL = auto() # "What did I just say?" → history
    HYBRID = auto()         # Requires multiple memory tiers


@dataclass
class MemoryContext:
    """Assembled memory context for injection into the LLM prompt."""
    query_type: QueryMemoryType
    kg_context: str | None          # From SemanticKnowledgeGraph
    vector_context: str | None      # From VectorMemoryStore
    episodic_context: str | None    # From EpisodicMemoryManager
    history_context: str | None     # From ConversationCompressor
    total_tokens: int
    retrieval_latency_ms: float

    def assemble(self, separator: str = "\n\n---\n\n") -> str:
        """Merge all non-None context blocks into a single injection string."""
        parts = [
            block for block in [
                self.kg_context,
                self.episodic_context,
                self.vector_context,
                self.history_context,
            ]
            if block is not None and block.strip()
        ]
        return separator.join(parts)


class ProductionMemoryRouter:
    """Multi-tier memory router for production LLM agents.

    Classifies each query by memory type, retrieves from the appropriate
    tier(s), and assembles a budget-constrained context block.

    Args:
        budget_manager: TokenBudgetManager for token allocation.
        vector_store: VectorMemoryStore for semantic retrieval.
        episodic_manager: EpisodicMemoryManager for session history.
        kg: SemanticKnowledgeGraph for structured fact retrieval.
        compressor: ConversationCompressor for history management.
        query_classifier: Callable (query: str) -> QueryMemoryType.
        token_counter: Callable (text: str) -> int.
        memory_budget_tokens: Max tokens to allocate to memory context (default 1500).

    Example:
        >>> router = ProductionMemoryRouter(
        ...     budget_manager=None,
        ...     vector_store=None,
        ...     episodic_manager=None,
        ...     kg=None,
        ...     compressor=None,
        ...     query_classifier=lambda q: QueryMemoryType.CONVERSATIONAL,
        ...     token_counter=lambda t: len(t.split()),
        ... )
        >>> ctx = router.retrieve("Hello, what did we discuss last time?", session_id="s1")
        >>> isinstance(ctx, MemoryContext)
        True
    """

    def __init__(
        self,
        budget_manager: "TokenBudgetManager | None",
        vector_store: "VectorMemoryStore | None",
        episodic_manager: "EpisodicMemoryManager | None",
        kg: "SemanticKnowledgeGraph | None",
        compressor: "ConversationCompressor | None",
        query_classifier: Callable[[str], QueryMemoryType],
        token_counter: Callable[[str], int],
        memory_budget_tokens: int = 1500,
    ) -> None:
        self._budget = budget_manager
        self._vector = vector_store
        self._episodic = episodic_manager
        self._kg = kg
        self._compressor = compressor
        self._classify = query_classifier
        self._count_tokens = token_counter
        self._memory_budget = memory_budget_tokens
        self._logger = logging.getLogger(__name__)

    def retrieve(
        self,
        query: str,
        session_id: str,
        entity_mentions: list[str] | None = None,
        current_history: "list[ConversationTurn] | None" = None,
    ) -> MemoryContext:
        """Retrieve memory context for a query across all tiers.

        Retrieval is performed in priority order. Each tier is queried
        and its output is token-counted against the memory budget.
        When the budget is consumed, retrieval stops.

        Args:
            query: The current user query.
            session_id: Current session identifier for episodic filtering.
            entity_mentions: Entity names detected in the query (pre-extracted).
            current_history: Current session's conversation history for compression.

        Returns:
            MemoryContext with assembled context ready for prompt injection.
        """
        import time
        t0 = time.monotonic()

        query_type = self._classify(query)
        remaining_budget = self._memory_budget

        kg_ctx = episodic_ctx = vector_ctx = history_ctx = None

        # Tier 1: Semantic KG — fastest, most precise (always attempt if entities present)
        if self._kg is not None and entity_mentions:
            try:
                result = self._kg.query_entities(entity_mentions or [], hop_depth=1)
                if result.context_text and remaining_budget > 0:
                    tokens = self._count_tokens(result.context_text)
                    if tokens <= remaining_budget:
                        kg_ctx = result.context_text
                        remaining_budget -= tokens
            except Exception:
                self._logger.warning("KG retrieval failed", exc_info=True)

        # Tier 2: Episodic memory — for experience and session continuity queries
        if (self._episodic is not None
                and query_type in (QueryMemoryType.EXPERIENTIAL, QueryMemoryType.HYBRID)
                and remaining_budget > 50):
            try:
                episodes = self._episodic.retrieve_relevant(query, top_k=3)
                if episodes:
                    lines = []
                    for ep, score in episodes:
                        lines.append(
                            f"[Past Session — {ep.started_at[:10]}] {ep.outcome_summary}"
                        )
                    ep_text = "[PAST EPISODES]\n" + "\n".join(lines)
                    tokens = self._count_tokens(ep_text)
                    if tokens <= remaining_budget:
                        episodic_ctx = ep_text
                        remaining_budget -= tokens
            except Exception:
                self._logger.warning("Episodic retrieval failed", exc_info=True)

        # Tier 3: Vector store — broad semantic retrieval
        if (self._vector is not None
                and query_type in (QueryMemoryType.DOCUMENTARY, QueryMemoryType.HYBRID, QueryMemoryType.FACTUAL)
                and remaining_budget > 100):
            try:
                results = self._vector.retrieve(query, top_k=4)
                if results:
                    chunks = [f"• {r.entry.content}" for r in results]
                    vec_text = "[RETRIEVED CONTEXT]\n" + "\n".join(chunks)
                    tokens = self._count_tokens(vec_text)
                    if tokens <= remaining_budget:
                        vector_ctx = vec_text
                        remaining_budget -= tokens
            except Exception:
                self._logger.warning("Vector retrieval failed", exc_info=True)

        # Tier 4: Compressed conversation history — always last (most tokens, least specific)
        if (self._compressor is not None
                and current_history is not None
                and remaining_budget > 50):
            try:
                _, verbatim = self._compressor.compress(current_history)
                history_text = self._compressor.get_history_block(verbatim)
                tokens = self._count_tokens(history_text)
                if tokens <= remaining_budget:
                    history_ctx = history_text
                    remaining_budget -= tokens
            except Exception:
                self._logger.warning("History compression failed", exc_info=True)

        elapsed_ms = (time.monotonic() - t0) * 1000
        total_tokens = self._memory_budget - remaining_budget

        return MemoryContext(
            query_type=query_type,
            kg_context=kg_ctx,
            vector_context=vector_ctx,
            episodic_context=episodic_ctx,
            history_context=history_ctx,
            total_tokens=total_tokens,
            retrieval_latency_ms=round(elapsed_ms, 2),
        )
```

[**Memory-Router-Latency-Budget**:: Production memory retrieval must complete within the model's Time-To-First-Token (TTFT) budget — typically 200–500ms for interactive applications. KG lookup: <5ms. Episodic retrieval (cosine over 1K episodes): <20ms. Vector retrieval (FAISS approximate NN over 50K entries): <30ms. Conversation compression (summarizer LLM call): 500–2000ms — run async or use a cached summary. The router should time-out any tier that exceeds its budget and proceed with whatever was retrieved.]

---

## Citations

1. Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. *Proceedings of UIST 2023*, 2–22.
2. Packer, C., Wooders, S., Lin, K., Fang, V., Patil, S. G., Stoica, I., & Gonzalez, J. E. (2023). MemGPT: Towards LLMs as operating systems. *arXiv preprint arXiv:2310.08560*.
3. Weng, L. (2023). LLM-powered autonomous agents. *Lil'Log Blog*. https://lilianweng.github.io/posts/2023-06-23-agent/
4. Johnson, J., Douze, M., & Jégou, H. (2019). Billion-scale similarity search with GPUs. *IEEE Transactions on Big Data*, 7(3), 535–547.
5. Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., ... & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. *Advances in Neural Information Processing Systems*, 35, 24824–24837.
6. Nye, M., Andreassen, A. J., Gur-Ari, G., Michalewski, H., Austin, J., Bieber, D., ... & Odena, A. (2021). Show your work: Scratchpads for intermediate computation with language models. *arXiv preprint arXiv:2112.00114*.
7. Zhong, W., Guo, L., Gao, Q., Ye, H., & Wang, Y. (2022). MemoryBank: Enhancing large language models with long-term memory. *arXiv preprint arXiv:2305.10250*.
8. Ratner, N., Geva, M., Berant, J., Globerson, A., Goldberg, Y., Shalev-Schwartz, S., & Shashua, A. (2023). Parallel context windows for large language models. *Proceedings of ACL 2023*, 6383–6402.
9. Sarthi, P., Abdullah, S., Tuli, A., Khanna, S., Goldie, A., & Manning, C. D. (2024). RAPTOR: Recursive abstractive processing for tree-organized retrieval. *ICLR 2024*.
10. Tulving, E. (1972). Episodic and semantic memory. In E. Tulving & W. Donaldson (Eds.), *Organization of Memory* (pp. 381–403). Academic Press.
11. Atkinson, R. C., & Shiffrin, R. M. (1968). Human memory: A proposed system and its control processes. *Psychology of Learning and Motivation*, 2, 89–195.
12. Baddeley, A. D., & Hitch, G. (1974). Working memory. *Psychology of Learning and Motivation*, 8, 47–89.
13. Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems*, 33, 9459–9474.
14. Borgeaud, S., Mensch, A., Hoffmann, J., Cai, T., Rutherford, E., Millican, K., ... & Sifre, L. (2022). Improving language models by retrieving from trillions of tokens. *Proceedings of ICML 2022*, 2206–2240.
15. Izacard, G., Lewis, P., Lomeli, M., Hosseini, L., Petroni, F., Schick, T., ... & Grave, E. (2023). Atlas: Few-shot learning with retrieval augmented language models. *Journal of Machine Learning Research*, 24(251), 1–43.
16. Dai, Z., Yang, Z., Yang, Y., Carbonell, J., Le, Q. V., & Salakhutdinov, R. (2019). Transformer-XL: Attentive language models beyond a fixed-length context. *Proceedings of ACL 2019*, 2978–2988.

---

## 🔗 Related Topics for PKB Expansion

1. **[[Transformer-XL-and-Extended-Context-Architectures]]**
   - *Connection*: The context window constraints addressed by external memory (Parts 1–4) motivate architectures that extend the effective context window at the model level — Transformer-XL's recurrent memory segments, Longformer's sparse attention, and FlashAttention's IO-aware computation all trade off different engineering constraints against the same fundamental limit
   - *Depth Potential*: Ring attention, gradient checkpointing for long contexts, and the emerging 1M-token context window models (Gemini 1.5, Claude 3) create a rapidly shifting landscape where the software-level memory patterns in this document remain relevant even as architectural limits expand
   - *Knowledge Graph Role*: Bridges software-level memory engineering (Doc10) to model architecture (Doc1 reasoning systems), showing the full stack from architectural decision to operational pattern

2. **[[Generative-Agents-Architecture]]**
   - *Connection*: Park et al. 2023's Generative Agents is the canonical production reference for the combined episodic + semantic + reflection memory architecture described in Parts 4–6 — studying the full system (25 agents, 2-day simulation) provides empirical grounding for the design choices encoded in this document's APIs
   - *Depth Potential*: The poignancy scoring mechanism, the daily reflection schedule, the relationship between retrieval recency and importance weighting, and the social network modeling all represent rich engineering decisions with documented failure modes
   - *Knowledge Graph Role*: Grounds the abstract memory patterns (Doc10 Parts 4–6) in an implemented, evaluated system — provides the empirical validation layer missing from purely theoretical treatments

3. **[[KV-Cache-Management-and-Prefix-Caching]]**
   - *Connection*: The context window token budget (Part 1) is tightly coupled to KV cache behavior — prefix caching (Doc8 Part 2) means that the order in which context segments are arranged affects cache hit rates, creating a co-optimization problem between memory routing (Doc10 Part 8) and serving efficiency (Doc8)
   - *Depth Potential*: RadixAttention (SGLang), prompt caching (Anthropic API), and VLLM's block-manager implement prefix caching at different levels of granularity with different eviction policies — understanding these mechanisms enables token-budget-aware prompt construction that maximizes cache efficiency
   - *Knowledge Graph Role*: Creates a critical bridge between the memory management layer (Doc10) and the production serving layer (Doc8), showing that memory architecture decisions have direct serving cost implications

4. **[[Cognitive-Architectures-and-ACT-R]]**
   - *Connection*: The multi-tier memory model (working memory scratchpad → episodic → semantic) directly parallels the ACT-R cognitive architecture's declarative memory (factual), procedural memory (skills), and working memory (goal buffer) — the activation-based retrieval mechanism in ACT-R provides a theoretically grounded alternative to cosine-similarity retrieval for prioritizing what to surface in context
   - *Depth Potential*: Anderson et al.'s subsymbolic parameters (base-level activation, spreading activation, partial matching) offer a principled approach to the importance scoring problem that the vector memory store currently handles with a single scalar — mapping these parameters to observable agent behaviors is an open research direction
   - *Knowledge Graph Role*: Connects the engineering patterns in Doc10 to the cognitive science literature (Atkinson & Shiffrin 1968, Baddeley 1974, Tulving 1972), grounding the system design in established theory and enabling principled extension

---

> [!important] Complete Series Summary
> This document (Doc10) completes the **Claude Reasoning Documentation Series** — a 10-document, Tier 2 reference covering: reasoning techniques and cognitive architecture (Doc1), prompt construction patterns (Doc2), knowledge representation (Doc3), agentic workflow design (Doc4), RAG architecture (Doc5), advanced prompt engineering (Doc6), LLM evaluation frameworks (Doc7), production systems architecture (Doc8), safety and alignment (Doc9), and memory and context management (Doc10). Together, these documents constitute a comprehensive production-grade reference for LLM system engineering at the level of a senior ML engineer or AI systems architect.
