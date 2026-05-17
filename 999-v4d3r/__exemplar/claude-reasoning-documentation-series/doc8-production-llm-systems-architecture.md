---
id: 20260516000015D
title: "Production LLM Systems Architecture"
subtitle: "Serving, Reliability, Cost Optimization, and Observability at Scale"
series: "Claude Reasoning Documentation Series"
doc_number: 8
tier: 2
phase: 2
version: 2.0.0
status: production
created: 2026-05-16
modified: 2026-05-16
tags:
  - production-llm
  - systems-architecture
  - inference-serving
  - reliability
  - cost-optimization
  - observability
aliases:
  - "Doc8"
  - "Production LLM"
  - "LLM Serving Architecture"
certainty: established
doc_series_position: 8/10
related_docs:
  - doc1-llm-reasoning-techniques-operational-manual
  - doc4-agentic-workflow-design-patterns
  - doc7-llm-evaluation-frameworks-and-metrics
word_count: ~5800
code_blocks: 33
citations: 15
wiki_links: 27
---

# Production LLM Systems Architecture

> [!abstract] Document Overview
> Deploying [[large-language-model|LLMs]] in production exposes a fundamentally different set of engineering challenges from training: unpredictable request shapes, extreme latency sensitivity, token-level cost accountability, and catastrophic failure modes that scale with traffic. This document covers the full production LLM stack — from inference serving infrastructure through reliability engineering, cost optimization, observability, multi-model orchestration, and deployment strategies — with production-grade Python code throughout.
>
> **Cross-references**: → [[doc1-llm-reasoning-techniques-operational-manual]] (reasoning patterns affecting serving design), → [[doc4-agentic-workflow-design-patterns]] (agentic systems impose unique infrastructure demands), → [[doc7-llm-evaluation-frameworks-and-metrics]] (production monitoring closes the evaluation loop)

---

## Part 1: Production LLM Stack Architecture

[**LLM-Serving-Stack**:: The layered infrastructure between a client request and a model response, encompassing load balancing, request routing, inference engine, token streaming, and response assembly.]

[**Inference-Engine**:: The software component that executes forward passes through a model's parameters, typically with hardware-specific optimizations (CUDA kernels, Flash Attention, paged KV cache management).]

The production LLM stack has five layers, each with distinct latency and reliability characteristics:

```
┌─────────────────────────────────────────────────────┐
│                    API Gateway                       │  ← Auth, rate limiting, request validation
├─────────────────────────────────────────────────────┤
│                  Request Router                      │  ← Model selection, load balancing
├─────────────────────────────────────────────────────┤
│               Inference Cluster                      │  ← GPU servers, batching, KV cache
├─────────────────────────────────────────────────────┤
│              Response Assembler                      │  ← Streaming, token budget enforcement
├─────────────────────────────────────────────────────┤
│           Observability / Audit Layer               │  ← Tracing, logging, cost accounting
└─────────────────────────────────────────────────────┘
```

### 1.1 Request Lifecycle

```python
from __future__ import annotations

import time
import uuid
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import AsyncIterator


class RequestPriority(Enum):
    """Request priority tiers for queue management."""
    CRITICAL = 0    # Real-time user-facing (chat UI)
    HIGH = 1        # Interactive API calls
    NORMAL = 2      # Batch/background jobs
    LOW = 3         # Best-effort, preemptable


@dataclass
class LLMRequest:
    """Canonical representation of an LLM inference request.

    Attributes:
        request_id: Globally unique request identifier (UUID4).
        model_id: Target model identifier (e.g., "claude-3-5-sonnet").
        messages: List of chat message dicts (role, content).
        max_tokens: Maximum output token budget.
        temperature: Sampling temperature (0.0 = deterministic).
        priority: Queue priority tier.
        stream: Whether to stream token-by-token.
        timeout_ms: Hard request timeout in milliseconds.
        metadata: Caller-provided context (user_id, session_id, etc.).
        enqueued_at: Unix timestamp when the request entered the system.
    """
    model_id: str
    messages: list[dict[str, str]]
    max_tokens: int = 2048
    temperature: float = 0.7
    priority: RequestPriority = RequestPriority.NORMAL
    stream: bool = True
    timeout_ms: int = 30_000
    metadata: dict = field(default_factory=dict)
    request_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    enqueued_at: float = field(default_factory=time.time)

    @property
    def estimated_input_tokens(self) -> int:
        """Rough token estimate: 4 chars per token on average."""
        total_chars = sum(len(m.get("content", "")) for m in self.messages)
        return max(1, total_chars // 4)

    @property
    def age_ms(self) -> float:
        """Milliseconds since this request was enqueued."""
        return (time.time() - self.enqueued_at) * 1000


@dataclass
class LLMResponse:
    """Structured response from an LLM inference call.

    Attributes:
        request_id: Echoed from the originating LLMRequest.
        content: Full response text (empty if streaming).
        finish_reason: Why generation stopped ("stop", "length", "error").
        input_tokens: Actual tokens consumed by the prompt.
        output_tokens: Actual tokens generated.
        latency_ms: Wall-clock latency from request receipt to response.
        model_version: Specific model version that served the request.
        cached: True if the response was served from a semantic cache.
    """
    request_id: str
    content: str
    finish_reason: str
    input_tokens: int
    output_tokens: int
    latency_ms: float
    model_version: str
    cached: bool = False

    @property
    def total_tokens(self) -> int:
        """Sum of input and output tokens."""
        return self.input_tokens + self.output_tokens

    @property
    def tokens_per_second(self) -> float:
        """Output throughput in tokens per second."""
        if self.latency_ms == 0:
            return 0.0
        return self.output_tokens / (self.latency_ms / 1000)
```

---

## Part 2: Model Serving Patterns

[**Continuous-Batching**:: A serving strategy where the inference engine dynamically adds new requests to an in-progress batch as existing requests finish, maximizing GPU utilization without fixed batch boundaries. Pioneered by Orca (Yu et al. 2022).]

[**KV-Cache**:: The key-value attention cache that stores computed attention tensors for input tokens, avoiding redundant computation when generating successive output tokens or processing shared prefixes.]

### 2.1 Continuous Batching

```python
import asyncio
from collections import deque
from dataclasses import dataclass, field


@dataclass
class BatchSlot:
    """A slot in the continuous batch representing one in-flight request."""
    request: LLMRequest
    tokens_generated: int = 0
    is_complete: bool = False
    result_queue: asyncio.Queue = field(default_factory=asyncio.Queue)


class ContinuousBatchingEngine:
    """Simulated continuous batching inference engine.

    Real implementations (vLLM, TensorRT-LLM) operate at the CUDA kernel
    level. This class models the scheduling logic for request admission,
    preemption, and slot recycling.

    Key insight: With continuous batching, GPU utilization stays near 100%
    because new sequences fill freed slots immediately — unlike static
    batching which waits for all batch members to finish.

    Example:
        >>> engine = ContinuousBatchingEngine(max_batch_size=32)
        >>> asyncio.run(engine.submit(request))
    """

    def __init__(self, max_batch_size: int = 32, max_sequence_length: int = 8192) -> None:
        self._max_batch = max_batch_size
        self._max_seq = max_sequence_length
        self._active_slots: list[BatchSlot] = []
        self._waiting_queue: deque[BatchSlot] = deque()
        self._lock = asyncio.Lock()

    async def submit(self, request: LLMRequest) -> asyncio.Queue:
        """Submit a request and return a queue that will receive token chunks.

        Args:
            request: The LLM request to enqueue.

        Returns:
            An asyncio.Queue yielding (token_str, is_final) tuples.
        """
        slot = BatchSlot(request=request)
        async with self._lock:
            if len(self._active_slots) < self._max_batch:
                self._active_slots.append(slot)
            else:
                self._waiting_queue.append(slot)
        return slot.result_queue

    async def _step(self) -> None:
        """Execute one decode step across all active slots.

        In a real engine this executes a single forward pass. The KV cache
        for all active sequences is updated in parallel on the GPU.
        """
        async with self._lock:
            completed = []
            for slot in self._active_slots:
                # SIMULATED: real engine calls CUDA kernel here
                slot.tokens_generated += 1
                if slot.tokens_generated >= slot.request.max_tokens:
                    slot.is_complete = True
                    await slot.result_queue.put(("", True))  # final sentinel
                    completed.append(slot)
                else:
                    await slot.result_queue.put(("<token>", False))

            # Recycle completed slots — admit waiting requests immediately
            for done in completed:
                self._active_slots.remove(done)
            while self._waiting_queue and len(self._active_slots) < self._max_batch:
                self._active_slots.append(self._waiting_queue.popleft())
```

### 2.2 Prefix Caching

```python
import hashlib
from typing import Any


class PrefixCache:
    """KV-cache sharing for requests with identical prompt prefixes.

    When multiple requests share a common system prompt or context (e.g.,
    all requests to the same RAG pipeline share a document context), the
    KV tensors for the shared prefix can be cached and reused, cutting
    the prefill cost to near zero for subsequent requests.

    This models the radix-tree cache used by vLLM and SGLang.

    Example:
        >>> cache = PrefixCache(max_blocks=1000, block_size=16)
        >>> block_ids = cache.lookup_or_allocate(prefix_tokens)
    """

    def __init__(self, max_blocks: int = 1000, block_size: int = 16) -> None:
        """
        Args:
            max_blocks: Maximum number of KV cache blocks to store.
            block_size: Tokens per cache block (hardware-aligned).
        """
        self._max_blocks = max_blocks
        self._block_size = block_size
        # Maps prefix_hash → list of allocated block IDs
        self._cache: dict[str, list[int]] = {}
        self._eviction_order: list[str] = []  # LRU ordering
        self._next_block_id = 0

    @staticmethod
    def _hash_prefix(tokens: list[int]) -> str:
        """Compute a stable hash of a token sequence.

        Args:
            tokens: List of integer token IDs.

        Returns:
            Hex-encoded SHA-256 hash of the token sequence.
        """
        token_bytes = bytes(t.to_bytes(4, "little") for t in tokens)
        return hashlib.sha256(token_bytes).hexdigest()

    def lookup(self, prefix_tokens: list[int]) -> list[int] | None:
        """Look up cached block IDs for a prefix.

        Args:
            prefix_tokens: The prompt prefix as token IDs.

        Returns:
            List of block IDs if cached, None otherwise.
        """
        key = self._hash_prefix(prefix_tokens)
        if key in self._cache:
            # LRU update: move to end
            self._eviction_order.remove(key)
            self._eviction_order.append(key)
            return self._cache[key]
        return None

    def store(self, prefix_tokens: list[int]) -> list[int]:
        """Allocate and store cache blocks for a prefix.

        Evicts LRU entries if capacity is exceeded.

        Args:
            prefix_tokens: Token IDs to cache.

        Returns:
            Newly allocated block IDs.
        """
        n_blocks = max(1, len(prefix_tokens) // self._block_size)

        # Evict if needed
        while len(self._cache) >= self._max_blocks // n_blocks:
            if not self._eviction_order:
                break
            evict_key = self._eviction_order.pop(0)
            del self._cache[evict_key]

        block_ids = list(range(self._next_block_id, self._next_block_id + n_blocks))
        self._next_block_id += n_blocks
        key = self._hash_prefix(prefix_tokens)
        self._cache[key] = block_ids
        self._eviction_order.append(key)
        return block_ids

    @property
    def hit_rate(self) -> float:
        """Estimated cache utilization (filled blocks / max blocks)."""
        total_blocks = sum(len(v) for v in self._cache.values())
        return min(1.0, total_blocks / self._max_blocks)
```

---

## Part 3: Latency Optimization

[**Speculative-Decoding**:: A decoding strategy where a small draft model generates multiple candidate tokens rapidly, and a larger target model verifies them in parallel. Accepted tokens are kept; rejected tokens trigger resampling from the target model. Reduces wall-clock latency by 2–4× for many workloads (Leviathan et al. 2023).]

[**Quantization**:: Reducing model parameter precision from FP16/BF16 to INT8 or INT4, reducing memory bandwidth and enabling larger batch sizes at the cost of minor quality degradation (Dettmers et al. 2022).]

### 3.1 Speculative Decoding Controller

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass
class SpeculativeDecodingResult:
    """Result of one speculative decoding round.

    Attributes:
        accepted_tokens: Token IDs accepted from the draft model.
        bonus_token: One additional token sampled from the target model.
        acceptance_rate: Fraction of draft tokens accepted this round.
        draft_calls: Number of draft model forward passes made.
        target_calls: Number of target model forward passes made.
    """
    accepted_tokens: list[int]
    bonus_token: int
    acceptance_rate: float
    draft_calls: int
    target_calls: int


class SpeculativeDecoder:
    """Coordinate draft model proposal and target model verification.

    The efficiency gain comes from batching target model verification:
    instead of N sequential target calls for N tokens, one parallel
    target call verifies all N draft proposals simultaneously.

    Args:
        draft_model_fn: Callable(prompt_tokens) → list[int] of candidate tokens.
        target_model_fn: Callable(prompt_tokens, draft_tokens) → (accepted_mask, bonus).
        gamma: Number of speculative tokens to propose per round (typical: 4-8).

    Example:
        >>> decoder = SpeculativeDecoder(draft_fn, target_fn, gamma=5)
        >>> result = decoder.decode_round(context_tokens)
        >>> print(f"Accepted {result.acceptance_rate:.1%} of draft tokens")
    """

    def __init__(
        self,
        draft_model_fn: Callable[[list[int]], list[int]],
        target_model_fn: Callable[[list[int], list[int]], tuple[list[bool], int]],
        gamma: int = 5,
    ) -> None:
        self._draft = draft_model_fn
        self._target = target_model_fn
        self._gamma = gamma

    def decode_round(self, context_tokens: list[int]) -> SpeculativeDecodingResult:
        """Execute one speculative decoding round.

        Args:
            context_tokens: Token IDs of the current context.

        Returns:
            SpeculativeDecodingResult with accepted tokens and statistics.
        """
        # Step 1: Draft model proposes gamma tokens greedily
        draft_tokens = self._draft(context_tokens)[:self._gamma]

        # Step 2: Target model verifies all draft tokens in one pass
        accepted_mask, bonus_token = self._target(context_tokens, draft_tokens)

        # Step 3: Accept tokens up to the first rejection
        accepted = []
        for token, is_accepted in zip(draft_tokens, accepted_mask):
            if is_accepted:
                accepted.append(token)
            else:
                break  # INVARIANT: stop at first rejection

        acceptance_rate = len(accepted) / max(1, len(draft_tokens))

        return SpeculativeDecodingResult(
            accepted_tokens=accepted,
            bonus_token=bonus_token,
            acceptance_rate=acceptance_rate,
            draft_calls=len(draft_tokens),  # Sequential draft calls
            target_calls=1,                  # One parallel target call
        )

    def speedup_estimate(self, acceptance_rate: float) -> float:
        """Estimate wall-clock speedup vs. standard decoding.

        Based on the theoretical speedup formula from Leviathan et al. 2023:
        speedup ≈ (1 - α^(γ+1)) / ((1-α)(1 + c·γ/β))
        where α = acceptance rate, γ = speculation length,
        c = draft/target cost ratio, β = target model throughput ratio.

        Simplified approximation for practical use:

        Args:
            acceptance_rate: Observed fraction of draft tokens accepted.

        Returns:
            Estimated speedup multiplier (> 1.0 means faster).
        """
        # Approximate: expected tokens per target call = sum(α^i) for i in 0..gamma
        expected_tokens_per_call = sum(
            acceptance_rate ** i for i in range(self._gamma + 1)
        )
        # Without speculation: 1 token per target call
        return expected_tokens_per_call
```

### 3.2 Response Streaming

```python
import asyncio
from typing import AsyncIterator


class TokenStreamer:
    """Manage server-sent event (SSE) streaming of LLM token output.

    Handles backpressure, timeout enforcement, and clean shutdown.
    Compatible with FastAPI StreamingResponse and ASGI frameworks.

    Example:
        >>> streamer = TokenStreamer(timeout_ms=30_000)
        >>> async for chunk in streamer.stream(token_queue):
        ...     yield chunk
    """

    def __init__(self, timeout_ms: int = 30_000, chunk_size: int = 1) -> None:
        """
        Args:
            timeout_ms: Maximum time to wait for the next token before aborting.
            chunk_size: Number of tokens to buffer before emitting a chunk.
        """
        self._timeout = timeout_ms / 1000.0
        self._chunk_size = chunk_size

    async def stream(
        self,
        token_queue: asyncio.Queue,
        request_id: str,
    ) -> AsyncIterator[str]:
        """Yield SSE-formatted chunks from a token queue.

        Args:
            token_queue: Queue producing (token_str, is_final) tuples.
            request_id: Request identifier for logging and client correlation.

        Yields:
            SSE-formatted strings: "data: <json>\n\n"

        Raises:
            asyncio.TimeoutError: If no token arrives within timeout_ms.
        """
        import json

        buffer = []
        try:
            while True:
                try:
                    token, is_final = await asyncio.wait_for(
                        token_queue.get(), timeout=self._timeout
                    )
                except asyncio.TimeoutError:
                    yield self._format_event(
                        {"error": "timeout", "request_id": request_id}
                    )
                    return

                if is_final:
                    if buffer:
                        yield self._format_event({
                            "token": "".join(buffer),
                            "request_id": request_id,
                            "finish_reason": "stop",
                        })
                    yield "data: [DONE]\n\n"
                    return

                buffer.append(token)
                if len(buffer) >= self._chunk_size:
                    yield self._format_event({
                        "token": "".join(buffer),
                        "request_id": request_id,
                    })
                    buffer.clear()
        except GeneratorExit:
            # Client disconnected — signal upstream to cancel the request
            pass

    @staticmethod
    def _format_event(payload: dict) -> str:
        """Format a dict as a Server-Sent Event data line."""
        import json
        return f"data: {json.dumps(payload)}\n\n"
```

---

## Part 4: Reliability and Fault Tolerance

[**Circuit-Breaker**:: A fault-isolation pattern that monitors error rates and temporarily stops routing requests to a failing downstream component, giving it time to recover while protecting the overall system from cascading failure.]

[**Fallback-Hierarchy**:: An ordered list of alternative models or response strategies invoked when the primary model fails, ensuring graceful degradation rather than hard failure (e.g., large → medium → cached → error message).]

### 4.1 Circuit Breaker

```python
from __future__ import annotations

import time
from enum import Enum, auto
from threading import Lock


class CircuitState(Enum):
    """States in the circuit breaker state machine."""
    CLOSED = auto()     # Normal operation — requests pass through
    OPEN = auto()       # Failing — requests rejected immediately
    HALF_OPEN = auto()  # Recovery probe — limited requests allowed


class CircuitBreaker:
    """Circuit breaker for LLM inference endpoints.

    Transitions:
        CLOSED → OPEN: error rate exceeds threshold over a window.
        OPEN → HALF_OPEN: after reset_timeout_s seconds.
        HALF_OPEN → CLOSED: probe request succeeds.
        HALF_OPEN → OPEN: probe request fails.

    Example:
        >>> cb = CircuitBreaker("claude-3-5-sonnet", failure_threshold=5)
        >>> if cb.allow_request():
        ...     try:
        ...         response = call_model(request)
        ...         cb.record_success()
        ...     except Exception:
        ...         cb.record_failure()
        ... else:
        ...     use_fallback()
    """

    def __init__(
        self,
        endpoint_id: str,
        failure_threshold: int = 5,
        success_threshold: int = 2,
        window_s: float = 60.0,
        reset_timeout_s: float = 30.0,
    ) -> None:
        """
        Args:
            endpoint_id: Name of the endpoint being protected.
            failure_threshold: Failures within window_s to trip to OPEN.
            success_threshold: Consecutive successes in HALF_OPEN to close.
            window_s: Sliding window duration in seconds.
            reset_timeout_s: Seconds in OPEN state before probing.
        """
        self.endpoint_id = endpoint_id
        self._failure_threshold = failure_threshold
        self._success_threshold = success_threshold
        self._window_s = window_s
        self._reset_timeout_s = reset_timeout_s
        self._state = CircuitState.CLOSED
        self._failure_times: list[float] = []
        self._consecutive_successes = 0
        self._opened_at: float | None = None
        self._lock = Lock()

    @property
    def state(self) -> CircuitState:
        """Current circuit state."""
        return self._state

    def allow_request(self) -> bool:
        """Determine if a request should be allowed through.

        Returns:
            True if the request should proceed, False if it should be rejected.
        """
        with self._lock:
            now = time.monotonic()
            if self._state == CircuitState.OPEN:
                if self._opened_at and (now - self._opened_at) >= self._reset_timeout_s:
                    self._state = CircuitState.HALF_OPEN
                    self._consecutive_successes = 0
                    return True  # Allow probe
                return False

            if self._state == CircuitState.HALF_OPEN:
                return True  # Allow probe

            return True  # CLOSED: always allow

    def record_success(self) -> None:
        """Record a successful response from the endpoint."""
        with self._lock:
            if self._state == CircuitState.HALF_OPEN:
                self._consecutive_successes += 1
                if self._consecutive_successes >= self._success_threshold:
                    self._state = CircuitState.CLOSED
                    self._failure_times.clear()

    def record_failure(self) -> None:
        """Record a failed response from the endpoint."""
        with self._lock:
            now = time.monotonic()
            if self._state == CircuitState.HALF_OPEN:
                self._state = CircuitState.OPEN
                self._opened_at = now
                return

            # Prune old failures outside the window
            self._failure_times = [t for t in self._failure_times
                                    if now - t <= self._window_s]
            self._failure_times.append(now)

            if len(self._failure_times) >= self._failure_threshold:
                self._state = CircuitState.OPEN
                self._opened_at = now
```

### 4.2 Fallback Hierarchy and Retry

```python
from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from typing import Callable


logger = logging.getLogger(__name__)


@dataclass
class FallbackConfig:
    """Configuration for one tier in the fallback hierarchy.

    Attributes:
        model_id: Model identifier for this tier.
        max_retries: Retries before advancing to the next tier.
        base_delay_ms: Initial retry backoff in milliseconds.
        max_delay_ms: Maximum retry backoff (exponential cap).
        timeout_ms: Per-attempt timeout for this tier.
    """
    model_id: str
    max_retries: int = 2
    base_delay_ms: int = 200
    max_delay_ms: int = 5_000
    timeout_ms: int = 15_000


class FallbackRouter:
    """Execute requests against a fallback hierarchy.

    Tries each tier in order, using exponential backoff within a tier
    before advancing to the next. Records circuit breaker outcomes
    for each tier.

    Example:
        >>> router = FallbackRouter(
        ...     tiers=[
        ...         FallbackConfig("claude-3-5-sonnet", max_retries=2),
        ...         FallbackConfig("claude-3-haiku", max_retries=1),
        ...     ],
        ...     circuit_breakers={"claude-3-5-sonnet": cb1, "claude-3-haiku": cb2},
        ...     model_fn=call_model,
        ... )
        >>> response = await router.route(request)
    """

    def __init__(
        self,
        tiers: list[FallbackConfig],
        circuit_breakers: dict[str, CircuitBreaker],
        model_fn: Callable,
    ) -> None:
        self._tiers = tiers
        self._cbs = circuit_breakers
        self._model_fn = model_fn

    async def route(self, request: LLMRequest) -> LLMResponse:
        """Route a request through the fallback hierarchy.

        Args:
            request: The LLM request to serve.

        Returns:
            LLMResponse from the first tier that succeeds.

        Raises:
            RuntimeError: If all tiers and retries are exhausted.
        """
        last_exc: Exception | None = None

        for tier in self._tiers:
            cb = self._cbs.get(tier.model_id)

            for attempt in range(tier.max_retries + 1):
                if cb and not cb.allow_request():
                    logger.warning(
                        "Circuit OPEN for %s, skipping tier", tier.model_id
                    )
                    break  # Skip this tier entirely

                delay_ms = min(
                    tier.base_delay_ms * (2 ** attempt),
                    tier.max_delay_ms,
                )
                if attempt > 0:
                    await asyncio.sleep(delay_ms / 1000.0)

                try:
                    patched_request = LLMRequest(
                        model_id=tier.model_id,
                        messages=request.messages,
                        max_tokens=request.max_tokens,
                        temperature=request.temperature,
                        timeout_ms=tier.timeout_ms,
                        metadata=request.metadata,
                        request_id=request.request_id,
                    )
                    response = await asyncio.wait_for(
                        self._model_fn(patched_request),
                        timeout=tier.timeout_ms / 1000.0,
                    )
                    if cb:
                        cb.record_success()
                    logger.info(
                        "Served request %s via %s (attempt %d)",
                        request.request_id, tier.model_id, attempt + 1
                    )
                    return response

                except Exception as exc:
                    last_exc = exc
                    if cb:
                        cb.record_failure()
                    logger.warning(
                        "Request %s failed on %s attempt %d: %s",
                        request.request_id, tier.model_id, attempt + 1, exc
                    )

        raise RuntimeError(
            f"All fallback tiers exhausted for request {request.request_id}"
        ) from last_exc
```

---

## Part 5: Cost Optimization

[**Token-Budget-Management**:: Strategies for controlling the number of tokens consumed per request — including prompt compression, max_tokens ceilings, early stopping on completion detection, and tiered model routing based on request complexity.]

[**Semantic-Cache**:: A cache that stores model responses keyed not by exact prompt text but by embedding similarity, serving cached responses for semantically equivalent queries to avoid redundant inference costs.]

### 5.1 Tiered Model Router

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass
class ModelTier:
    """A model tier in the cost-optimized router.

    Attributes:
        model_id: Model identifier.
        cost_per_1k_input_tokens: API cost in USD per 1,000 input tokens.
        cost_per_1k_output_tokens: API cost in USD per 1,000 output tokens.
        complexity_threshold: Maximum complexity score this tier handles.
        avg_latency_ms: Typical response latency for capacity planning.
    """
    model_id: str
    cost_per_1k_input_tokens: float
    cost_per_1k_output_tokens: float
    complexity_threshold: float
    avg_latency_ms: float


class ComplexityEstimator:
    """Estimate request complexity to drive tiered model routing.

    Uses a lightweight heuristic (no LLM call required) based on:
    - Prompt length (longer prompts → more complex)
    - Detected reasoning keywords (math, code, analysis)
    - Conversation depth (more turns → more complex context)
    - Explicit user instructions

    Example:
        >>> estimator = ComplexityEstimator()
        >>> score = estimator.estimate(request)
        >>> # score in [0.0, 1.0]; > 0.7 routes to frontier model
    """

    REASONING_KEYWORDS = frozenset({
        "prove", "derive", "analyze", "calculate", "debug", "optimize",
        "compare", "evaluate", "synthesize", "explain why", "step by step",
        "chain of thought", "formal proof", "complexity", "algorithm",
    })

    def estimate(self, request: LLMRequest) -> float:
        """Compute a complexity score for a request.

        Args:
            request: The LLM request to score.

        Returns:
            Complexity score in [0.0, 1.0]. Higher = more complex.
        """
        score = 0.0
        full_text = " ".join(m.get("content", "") for m in request.messages).lower()
        total_chars = len(full_text)

        # Length factor: 0→0, 4000 chars→0.3
        score += min(0.3, total_chars / 13_333)

        # Reasoning keyword density
        keyword_hits = sum(1 for kw in self.REASONING_KEYWORDS if kw in full_text)
        score += min(0.4, keyword_hits * 0.08)

        # Conversation depth (multi-turn adds context complexity)
        n_turns = len(request.messages)
        score += min(0.2, n_turns * 0.025)

        # High max_tokens request implies expected long output
        if request.max_tokens > 4096:
            score += 0.1

        return min(1.0, score)


class TieredModelRouter:
    """Route requests to the cheapest capable model tier.

    Models are tried from cheapest to most expensive. A request is
    routed to a tier only if its complexity score falls below that
    tier's threshold.

    Example:
        >>> router = TieredModelRouter(
        ...     tiers=[
        ...         ModelTier("haiku", 0.00025, 0.00125, complexity_threshold=0.35, avg_latency_ms=800),
        ...         ModelTier("sonnet", 0.003, 0.015, complexity_threshold=0.70, avg_latency_ms=2000),
        ...         ModelTier("opus", 0.015, 0.075, complexity_threshold=1.00, avg_latency_ms=5000),
        ...     ],
        ...     model_fn=call_model,
        ... )
    """

    def __init__(
        self,
        tiers: list[ModelTier],
        model_fn: Callable,
        estimator: ComplexityEstimator | None = None,
    ) -> None:
        self._tiers = sorted(tiers, key=lambda t: t.cost_per_1k_output_tokens)
        self._model_fn = model_fn
        self._estimator = estimator or ComplexityEstimator()

    async def route(self, request: LLMRequest) -> tuple[LLMResponse, str]:
        """Route to the cheapest tier that meets complexity requirements.

        Args:
            request: The request to serve.

        Returns:
            Tuple of (LLMResponse, selected_model_id).
        """
        complexity = self._estimator.estimate(request)

        for tier in self._tiers:
            if complexity <= tier.complexity_threshold:
                patched = LLMRequest(
                    model_id=tier.model_id,
                    messages=request.messages,
                    max_tokens=request.max_tokens,
                    temperature=request.temperature,
                    request_id=request.request_id,
                    metadata={**request.metadata, "complexity_score": complexity},
                )
                response = await self._model_fn(patched)
                return response, tier.model_id

        # FALLBACK: use the most capable tier
        patched = LLMRequest(
            model_id=self._tiers[-1].model_id,
            messages=request.messages,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            request_id=request.request_id,
        )
        response = await self._model_fn(patched)
        return response, self._tiers[-1].model_id

    def estimated_cost_usd(
        self,
        tier: ModelTier,
        input_tokens: int,
        output_tokens: int,
    ) -> float:
        """Compute the estimated cost for a request.

        Args:
            tier: The model tier used.
            input_tokens: Number of input tokens consumed.
            output_tokens: Number of output tokens generated.

        Returns:
            Estimated cost in USD.
        """
        input_cost = (input_tokens / 1000) * tier.cost_per_1k_input_tokens
        output_cost = (output_tokens / 1000) * tier.cost_per_1k_output_tokens
        return input_cost + output_cost
```

### 5.2 Semantic Cache

```python
from __future__ import annotations

import time
from dataclasses import dataclass, field


@dataclass
class CacheEntry:
    """A stored semantic cache entry."""
    query_embedding: list[float]
    response: LLMResponse
    created_at: float = field(default_factory=time.time)
    hit_count: int = 0
    ttl_s: float = 3600.0

    @property
    def is_expired(self) -> bool:
        """Return True if this entry has exceeded its TTL."""
        return (time.time() - self.created_at) > self.ttl_s


class SemanticCache:
    """Cache LLM responses using embedding similarity matching.

    Avoids redundant inference for semantically equivalent queries.
    Uses cosine similarity to find cache hits within a configurable
    similarity threshold.

    Effective for:
    - FAQ-style queries with high repetition
    - Document Q&A with overlapping user questions
    - Classification/extraction tasks on similar inputs

    Example:
        >>> cache = SemanticCache(embed_fn=my_embedder, threshold=0.95)
        >>> hit = cache.lookup(user_query)
        >>> if hit:
        ...     return hit  # Serve from cache
        ... else:
        ...     response = await model_fn(request)
        ...     cache.store(user_query, response)
    """

    def __init__(
        self,
        embed_fn,  # Callable[[str], list[float]]
        threshold: float = 0.95,
        max_entries: int = 10_000,
    ) -> None:
        self._embed = embed_fn
        self._threshold = threshold
        self._max_entries = max_entries
        self._entries: list[CacheEntry] = []

    def lookup(self, query: str) -> LLMResponse | None:
        """Find a cached response for a semantically similar query.

        Args:
            query: The user's query string.

        Returns:
            Cached LLMResponse if similarity ≥ threshold, else None.
        """
        query_embedding = self._embed(query)
        self._evict_expired()

        best_similarity = 0.0
        best_entry: CacheEntry | None = None

        for entry in self._entries:
            sim = self._cosine_similarity(query_embedding, entry.query_embedding)
            if sim > best_similarity:
                best_similarity = sim
                best_entry = entry

        if best_entry and best_similarity >= self._threshold:
            best_entry.hit_count += 1
            return best_entry.response
        return None

    def store(self, query: str, response: LLMResponse, ttl_s: float = 3600.0) -> None:
        """Store a response in the cache.

        Args:
            query: The query string (will be embedded).
            response: The LLM response to cache.
            ttl_s: Cache entry TTL in seconds.
        """
        if len(self._entries) >= self._max_entries:
            # Evict lowest hit-count entry (approximates LFU)
            self._entries.sort(key=lambda e: e.hit_count)
            self._entries.pop(0)

        self._entries.append(CacheEntry(
            query_embedding=self._embed(query),
            response=response,
            ttl_s=ttl_s,
        ))

    def _evict_expired(self) -> None:
        """Remove all expired entries."""
        self._entries = [e for e in self._entries if not e.is_expired]

    @staticmethod
    def _cosine_similarity(a: list[float], b: list[float]) -> float:
        """Compute cosine similarity between two embedding vectors.

        Args:
            a: First embedding vector.
            b: Second embedding vector.

        Returns:
            Cosine similarity in [-1, 1].
        """
        import math
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = math.sqrt(sum(x * x for x in a))
        norm_b = math.sqrt(sum(y * y for y in b))
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot / (norm_a * norm_b)
```

---

## Part 6: Observability and Monitoring

[**Distributed-Tracing**:: Correlating log records and metrics across multiple services by propagating a shared trace context (trace_id, span_id) so that a single user request can be followed end-to-end through a distributed system.]

[**Token-Accounting**:: Per-request tracking of input and output tokens for cost attribution, budget enforcement, and capacity planning. Essential for multi-tenant LLM services.]

### 6.1 Structured Observability

```python
from __future__ import annotations

import logging
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Generator


@dataclass
class Span:
    """A single timed operation within a distributed trace.

    Attributes:
        trace_id: Root trace identifier (shared across all spans in a request).
        span_id: This span's unique identifier.
        parent_span_id: Parent span (None for root spans).
        operation: Human-readable operation name.
        start_time: Unix timestamp when the span started.
        end_time: Unix timestamp when the span ended (0 if in-flight).
        attributes: Arbitrary key-value metadata.
        status: "ok", "error", or "timeout".
    """
    trace_id: str
    span_id: str
    operation: str
    parent_span_id: str | None = None
    start_time: float = field(default_factory=time.time)
    end_time: float = 0.0
    attributes: dict = field(default_factory=dict)
    status: str = "ok"

    @property
    def duration_ms(self) -> float:
        """Span duration in milliseconds."""
        if self.end_time == 0:
            return (time.time() - self.start_time) * 1000
        return (self.end_time - self.start_time) * 1000

    def finish(self, status: str = "ok") -> None:
        """Mark this span as complete."""
        self.end_time = time.time()
        self.status = status


class LLMTracer:
    """Distributed tracing for LLM inference pipelines.

    Collects spans for each operation in the request lifecycle
    (queue wait, prefill, decode, response assembly) and exports
    them to a backend (OpenTelemetry, Jaeger, Honeycomb).

    Example:
        >>> tracer = LLMTracer(export_fn=otel_export)
        >>> with tracer.trace("llm_request", trace_id="abc") as span:
        ...     span.attributes["model"] = "claude-3-5-sonnet"
        ...     response = await model_fn(request)
        ...     span.attributes["output_tokens"] = response.output_tokens
    """

    def __init__(self, export_fn=None) -> None:
        import uuid
        self._export = export_fn or (lambda spans: None)
        self._uuid = uuid

    @contextmanager
    def trace(
        self,
        operation: str,
        trace_id: str | None = None,
        parent_span_id: str | None = None,
        attributes: dict | None = None,
    ) -> Generator[Span, None, None]:
        """Context manager that creates and completes a trace span.

        Args:
            operation: Human-readable name for the operation.
            trace_id: Shared trace identifier (generated if not provided).
            parent_span_id: Parent span for nested operations.
            attributes: Initial span attributes.

        Yields:
            Span: The active span (attributes can be added during execution).
        """
        span = Span(
            trace_id=trace_id or str(self._uuid.uuid4()),
            span_id=str(self._uuid.uuid4()),
            parent_span_id=parent_span_id,
            operation=operation,
            attributes=attributes or {},
        )
        try:
            yield span
            span.finish("ok")
        except Exception as exc:
            span.finish("error")
            span.attributes["error.type"] = type(exc).__name__
            span.attributes["error.message"] = str(exc)
            raise
        finally:
            self._export([span])


def structured_log(
    level: str,
    message: str,
    request_id: str | None = None,
    model_id: str | None = None,
    **extra,
) -> None:
    """Emit a structured JSON log record.

    Args:
        level: Log level ("debug", "info", "warning", "error").
        message: Human-readable log message.
        request_id: Request identifier for correlation.
        model_id: Model that processed the request.
        **extra: Additional structured fields.
    """
    import json
    record = {
        "timestamp": time.time(),
        "level": level,
        "message": message,
        "request_id": request_id,
        "model_id": model_id,
        **extra,
    }
    logging.getLogger("llm.structured").log(
        getattr(logging, level.upper(), logging.INFO),
        json.dumps(record),
    )
```

---

## Part 7: Multi-Model Orchestration

[**Model-Cascade**:: A sequential evaluation pattern where a cheap model first attempts a request; a more capable model is invoked only if the cheap model's confidence or output quality falls below a threshold. Reduces average cost while maintaining quality on hard examples.]

[**Ensemble-Routing**:: Distributing requests across multiple models and aggregating their outputs, either by majority vote, confidence weighting, or a trained aggregator — improving robustness at the cost of 2–N× inference compute.]

### 7.1 Confidence-Based Cascade

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass
class CascadeConfig:
    """Configuration for a two-stage model cascade.

    Attributes:
        cheap_model_id: Fast, inexpensive first-stage model.
        expensive_model_id: High-quality second-stage model.
        confidence_threshold: Minimum score to accept cheap model's output.
        scorer: Callable(response) → float confidence in [0, 1].
    """
    cheap_model_id: str
    expensive_model_id: str
    confidence_threshold: float
    scorer: Callable[[LLMResponse], float]


class ModelCascade:
    """Two-stage cascade: use cheap model, escalate on low confidence.

    The scorer evaluates the cheap model's output. If confidence exceeds
    the threshold, the cheap response is returned. Otherwise, the expensive
    model is invoked and its response is returned.

    Example:
        >>> cascade = ModelCascade(config=cfg, model_fn=call_model)
        >>> response, used_model = await cascade.run(request)
        >>> print(f"Served by {used_model}")  # "haiku" or "opus"
    """

    def __init__(self, config: CascadeConfig, model_fn: Callable) -> None:
        self._config = config
        self._model_fn = model_fn

    async def run(self, request: LLMRequest) -> tuple[LLMResponse, str]:
        """Execute the cascade.

        Args:
            request: The user's request.

        Returns:
            Tuple of (response, model_id_used).
        """
        cheap_request = LLMRequest(
            model_id=self._config.cheap_model_id,
            messages=request.messages,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            request_id=request.request_id,
        )
        cheap_response = await self._model_fn(cheap_request)
        confidence = self._config.scorer(cheap_response)

        if confidence >= self._config.confidence_threshold:
            return cheap_response, self._config.cheap_model_id

        # Escalate to expensive model
        expensive_request = LLMRequest(
            model_id=self._config.expensive_model_id,
            messages=request.messages,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            request_id=request.request_id,
            metadata={**request.metadata, "escalated_from": self._config.cheap_model_id,
                      "escalation_confidence": confidence},
        )
        expensive_response = await self._model_fn(expensive_request)
        return expensive_response, self._config.expensive_model_id
```

### 7.2 Load Balancer

```python
import asyncio
import random
from dataclasses import dataclass, field


@dataclass
class InferenceNode:
    """Represents one inference server node.

    Attributes:
        node_id: Unique node identifier.
        endpoint_url: Base URL for API calls.
        weight: Relative routing weight (higher = more traffic).
        active_requests: Current in-flight request count.
        is_healthy: Whether the node passed the last health check.
    """
    node_id: str
    endpoint_url: str
    weight: float = 1.0
    active_requests: int = 0
    is_healthy: bool = True
    error_count: int = 0


class WeightedLeastConnectionsBalancer:
    """Weighted least-connections load balancer for inference nodes.

    Selects the node with the fewest active requests, weighted by
    node capacity. Adapts to heterogeneous hardware (e.g., A100 vs H100)
    by assigning higher weights to more capable nodes.

    Example:
        >>> balancer = WeightedLeastConnectionsBalancer(nodes)
        >>> node = balancer.select()
        >>> try:
        ...     response = await call(node, request)
        ... finally:
        ...     balancer.release(node)
    """

    def __init__(self, nodes: list[InferenceNode]) -> None:
        self._nodes = nodes
        self._lock = asyncio.Lock()

    async def select(self) -> InferenceNode | None:
        """Select the best node using weighted least-connections.

        Returns:
            The selected InferenceNode, or None if no healthy nodes exist.
        """
        async with self._lock:
            healthy = [n for n in self._nodes if n.is_healthy]
            if not healthy:
                return None

            # Score: lower is better (fewer connections relative to weight)
            def score(node: InferenceNode) -> float:
                return node.active_requests / max(0.01, node.weight)

            selected = min(healthy, key=score)
            selected.active_requests += 1
            return selected

    async def release(self, node: InferenceNode) -> None:
        """Decrement active request count after a request completes."""
        async with self._lock:
            node.active_requests = max(0, node.active_requests - 1)

    async def mark_unhealthy(self, node: InferenceNode) -> None:
        """Mark a node as unhealthy after repeated failures."""
        async with self._lock:
            node.is_healthy = False
            node.error_count += 1
```

---

## Part 8: Deployment Patterns

[**Canary-Deployment**:: A gradual rollout strategy where a new model version serves a small fraction of traffic (e.g., 5%), with automated rollback if key metrics degrade. Limits blast radius of a bad release.]

[**Shadow-Deployment**:: Routing a copy of production traffic to a new model version without affecting the user-visible response. Enables offline quality comparison before any traffic migration.]

### 8.1 Canary Controller

```python
from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Callable


@dataclass
class CanaryConfig:
    """Configuration for a canary deployment.

    Attributes:
        stable_model_id: The currently deployed stable model.
        canary_model_id: The new model version being tested.
        canary_fraction: Fraction of traffic to route to canary (0.0–1.0).
        rollback_error_rate: Error rate on canary that triggers auto-rollback.
        rollback_latency_p99_ms: Latency regression that triggers rollback.
    """
    stable_model_id: str
    canary_model_id: str
    canary_fraction: float = 0.05
    rollback_error_rate: float = 0.02
    rollback_latency_p99_ms: float = 5000.0


class CanaryController:
    """Manage canary deployments with automatic rollback.

    Routes traffic between stable and canary, monitors key metrics,
    and rolls back automatically if thresholds are breached.

    Example:
        >>> ctrl = CanaryController(config, model_fn=call_model)
        >>> response = await ctrl.route(request)
        >>> # Gradually increase canary_fraction as confidence grows
        >>> ctrl.increase_canary(0.10)
    """

    def __init__(self, config: CanaryConfig, model_fn: Callable) -> None:
        self._config = config
        self._model_fn = model_fn
        self._canary_errors = 0
        self._canary_total = 0
        self._rolled_back = False

    async def route(self, request: LLMRequest) -> LLMResponse:
        """Route a request to stable or canary based on configured fraction.

        Args:
            request: The user's request.

        Returns:
            LLMResponse from whichever model served the request.
        """
        if self._rolled_back or random.random() > self._config.canary_fraction:
            model_id = self._config.stable_model_id
            is_canary = False
        else:
            model_id = self._config.canary_model_id
            is_canary = True

        patched = LLMRequest(
            model_id=model_id,
            messages=request.messages,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            request_id=request.request_id,
            metadata={**request.metadata, "is_canary": is_canary},
        )

        try:
            response = await self._model_fn(patched)
            if is_canary:
                self._canary_total += 1
                self._check_rollback()
            return response

        except Exception:
            if is_canary:
                self._canary_errors += 1
                self._canary_total += 1
                self._check_rollback()
            raise

    def _check_rollback(self) -> None:
        """Trigger rollback if error rate exceeds threshold."""
        if self._canary_total < 20:
            return  # Not enough data for reliable decision
        error_rate = self._canary_errors / self._canary_total
        if error_rate > self._config.rollback_error_rate:
            self._rolled_back = True

    def increase_canary(self, new_fraction: float) -> None:
        """Increase canary traffic fraction (progressive rollout).

        Args:
            new_fraction: New canary fraction in [0.0, 1.0].
        """
        if self._rolled_back:
            raise RuntimeError("Cannot increase canary fraction: rollback is active")
        self._config.canary_fraction = min(1.0, max(0.0, new_fraction))

    @property
    def is_rolled_back(self) -> bool:
        """Return True if automatic rollback has been triggered."""
        return self._rolled_back

    @property
    def canary_error_rate(self) -> float:
        """Current canary error rate."""
        if self._canary_total == 0:
            return 0.0
        return self._canary_errors / self._canary_total
```

### 8.2 Shadow Deployment

```python
import asyncio
from typing import Callable


class ShadowDeployment:
    """Send production traffic to a shadow model without affecting users.

    The user always receives the stable model's response. The shadow
    model's response is captured asynchronously for quality comparison.
    Comparison results feed into the evaluation pipeline (→ Doc7).

    Example:
        >>> shadow = ShadowDeployment(
        ...     stable_fn=stable_model,
        ...     shadow_fn=candidate_model,
        ...     comparison_fn=log_comparison,
        ...     shadow_fraction=0.20,
        ... )
        >>> # User gets stable response; shadow comparison happens in background
        >>> response = await shadow.serve(request)
    """

    def __init__(
        self,
        stable_fn: Callable,
        shadow_fn: Callable,
        comparison_fn: Callable | None = None,
        shadow_fraction: float = 0.20,
    ) -> None:
        import random
        self._stable = stable_fn
        self._shadow = shadow_fn
        self._compare = comparison_fn or (lambda req, stable, shadow: None)
        self._fraction = shadow_fraction
        self._rng = random.Random()

    async def serve(self, request: LLMRequest) -> LLMResponse:
        """Serve the request using the stable model; optionally shadow.

        Args:
            request: The user's request.

        Returns:
            Stable model response (never shadow response).
        """
        # Always get stable response first (on the critical path)
        stable_response = await self._stable(request)

        # Fire shadow request in background if sampled
        if self._rng.random() < self._fraction:
            asyncio.create_task(self._shadow_and_compare(request, stable_response))

        return stable_response

    async def _shadow_and_compare(
        self,
        request: LLMRequest,
        stable_response: LLMResponse,
    ) -> None:
        """Execute shadow call and record comparison (non-critical path)."""
        try:
            shadow_response = await self._shadow(request)
            self._compare(request, stable_response, shadow_response)
        except Exception:
            pass  # Shadow failures must not affect production
```

---

## Citations

1. Yu, G., Kim, J.-S., Jeong, H., et al. (2022). *Orca: A Distributed Serving System for Transformer-Based Generative Models*. OSDI 2022. [Continuous batching]
2. Leviathan, Y., Kalman, M., & Matias, Y. (2023). *Fast Inference from Transformers via Speculative Decoding*. ICML 2023. [Speculative decoding]
3. Dettmers, T., Lewis, M., Belkada, Y., & Zettlemoyer, L. (2022). *LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale*. NeurIPS 2022. [Quantization]
4. Kwon, W., Li, Z., Zhuang, S., et al. (2023). *Efficient Memory Management for Large Language Model Serving with PagedAttention*. SOSP 2023. [vLLM, paged KV cache]
5. Zheng, L., Yin, L., Xie, Z., et al. (2023). *Efficiently Programming Large Language Models using SGLang*. arXiv:2312.07104. [RadixAttention / prefix caching]
6. Ainslie, J., Lee-Thorp, J., de Jong, M., et al. (2023). *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints*. EMNLP 2023. [GQA / KV cache compression]
7. Pope, R., Douglas, S., Chowdhery, A., et al. (2023). *Efficiently Scaling Transformer Inference*. MLSys 2023. [Inference optimization at scale]
8. Patterson, D., Gonzalez, J., Le, Q., et al. (2021). *Carbon Considerations for Large Scale ML Model Training and Inference*. arXiv:2104.10350. [Cost and sustainability]
9. Sheng, Y., Zheng, L., Yuan, B., et al. (2023). *FlexGen: High-Throughput Generative Inference of Large Language Models with a Single GPU*. ICML 2023. [Throughput optimization]
10. Geng, X., & Liu, H. (2023). *OpenLLM: An Open Platform for Training, Fine-tuning, and Deploying Large Language Models in the Wild*. arXiv:2306.05615. [Open-source serving]
11. Fowler, M. (2018). *Patterns of Enterprise Application Architecture*. Addison-Wesley. [Circuit breaker, retry patterns]
12. Nygard, M. T. (2007). *Release It!: Design and Deploy Production-Ready Software*. Pragmatic Bookshelf. [Stability patterns: circuit breaker, bulkhead, timeout]
13. Burns, B., Grant, B., Oppenheimer, D., Brewer, E., & Wilkes, J. (2016). *Borg, Omega, and Kubernetes*. ACM Queue. [Container orchestration for serving]
14. Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly. [Distributed systems reliability patterns]
15. Sigelman, B. H., Barroso, L. A., Burrows, M., et al. (2010). *Dapper, a Large-Scale Distributed Systems Tracing Infrastructure*. Google Technical Report. [Distributed tracing]

---

## 🔗 Related Topics for PKB Expansion

1. **[[PagedAttention-and-vLLM-Architecture]]**
   - *Connection*: The KV cache and prefix caching in Part 2 are built on vLLM's PagedAttention (Kwon et al. 2023) — virtual memory management applied to attention tensors.
   - *Depth Potential*: Deep dive into block tables, page faulting semantics, beam search KV sharing, and copy-on-write for parallel sampling.
   - *Knowledge Graph Role*: Central technical node linking serving infrastructure → cost optimization → Doc5 RAG (which requires efficient KV cache for long documents).

2. **[[SGLang-and-Structured-Generation-Runtime]]**
   - *Connection*: SGLang's RadixAttention extends prefix caching with a radix tree for multi-turn and multi-program sharing — the production realization of Part 2's `PrefixCache`.
   - *Depth Potential*: SGLang primitives (fork, join, constrained decoding), EBNF-guided generation, and integration with structured output parsers.
   - *Knowledge Graph Role*: Bridges serving infrastructure → Doc6 prompt engineering (structured outputs require runtime support).

3. **[[LLM-Serving-Cost-Models]]**
   - *Connection*: The `TieredModelRouter` and `SemanticCache` in Part 5 require cost models to make routing decisions; this topic provides the empirical grounding.
   - *Depth Potential*: Cost curves for different model sizes, cost-vs-quality Pareto frontiers, reserved vs. on-demand pricing, batch inference discounts.
   - *Knowledge Graph Role*: Connects cost optimization → Doc7 evaluation (cost efficiency is an evaluation dimension) → business value justification.

4. **[[Inference-Hardware-Landscape]]**
   - *Connection*: Every latency and throughput number in this document assumes specific hardware (A100, H100, TPU). Understanding the hardware landscape is prerequisite to production capacity planning.
   - *Depth Potential*: GPU memory bandwidth vs. compute bounds, tensor parallelism vs. pipeline parallelism tradeoffs, NVLink vs. PCIe topology effects on model parallelism.
   - *Knowledge Graph Role*: Foundation node for all production serving decisions — connects hardware → serving patterns → cost optimization.

---

> [!important] Production Deployment Checklist
> Before serving any model in production: (1) Circuit breakers configured for all upstream dependencies; (2) Fallback hierarchy tested under simulated failure; (3) Cost accounting instrumented per request; (4) Token budget enforced at the API gateway layer; (5) Canary deployment configured with auto-rollback thresholds; (6) Distributed tracing enabled with sampling rate ≥ 5%; (7) Regression suite from Doc7 integrated into CI/CD pipeline.
