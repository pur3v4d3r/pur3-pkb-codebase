#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""llm_client.py — Ollama HTTP client + structured-output validation + cache.

Thin wrapper around ``http://localhost:11434/api/chat`` purpose-built for the
v3 pipeline. Optimised for **deterministic, cacheable, structured-JSON
responses** rather than free-form chat.

Design
------
- **Single-tenant.** Ollama serializes requests internally; we make no attempt
  at concurrency. Callers feed candidates one at a time.
- **JSON mode.** Every request sets ``format="json"`` and uses ``temperature=0``
  by default so a given (model, prompt) pair is reproducible.
- **Content-hash cache.** Successful responses are persisted under
  ``_v3-output/llm-cache/<sha1>.json``. Re-running the pipeline against
  unchanged inputs costs zero LLM time.
- **Schema validation.** Optional ``pydantic`` model parameter validates the
  parsed JSON post-hoc. Failures raise :class:`StructuredOutputError`.
- **Exponential backoff.** Transient HTTP / connection errors are retried up
  to ``max_retries`` times with 1, 2, 4 second delays.

What this module is and isn't
-----------------------------
**Is:** a small synchronous HTTP client with a cache and a JSON-shape guard.
**Isn't:** a prompt library. Prompts live with their callers (Stage 4 keeps
its prompt template in ``stages/s4_normalize.py``; synthesis prompts live in
their respective stage modules).

Public API
----------
- :class:`OllamaClient` — the client (use ``with OllamaClient(...) as c:``)
- :class:`LLMResponse` — wraps the parsed JSON + raw text + cache metadata
- :class:`LLMError` (base), :class:`OllamaUnavailableError`,
  :class:`StructuredOutputError`
- :func:`content_hash` — stable cache key builder

Spec reference: §2.2 (LLM stack), §5 Phase 7 (concept normalization).

Usage:
    from lib.llm_client import OllamaClient

    with OllamaClient(model="qwen2.5:14b") as c:
        rsp = c.chat_json(
            system="You are a careful taxonomist.",
            user='Return JSON: {"x": 1}',
            schema=MySchema,           # optional pydantic model
            cache_key_inputs=("v1", concept_text),
        )
        print(rsp.parsed)              # validated dict (or model instance)

Version:
    1.0.0
"""
from __future__ import annotations

import hashlib
import json
import logging
import time
from contextlib import AbstractContextManager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, TypeVar

import requests
from requests.exceptions import ConnectionError as ReqConnError
from requests.exceptions import RequestException, Timeout

logger = logging.getLogger(__name__)

__version__ = "1.0.0"

# ── Defaults ─────────────────────────────────────────────────────────────

DEFAULT_OLLAMA_URL: str = "http://localhost:11434"
DEFAULT_MODEL: str = "qwen2.5:7b-instruct-q5_K_M"
DEFAULT_TIMEOUT_S: float = 120.0
DEFAULT_MAX_RETRIES: int = 3
DEFAULT_TEMPERATURE: float = 0.0
DEFAULT_NUM_CTX: int = 8192
#: Cache schema version. Bump to invalidate every cached response when prompt
#: contracts change in a backwards-incompatible way.
CACHE_SCHEMA_VERSION: str = "v1"

T = TypeVar("T")


# ════════════════════════════════════════════════════════════════════════════
# Exceptions
# ════════════════════════════════════════════════════════════════════════════

class LLMError(Exception):
    """Base exception for ``llm_client`` failures."""


class OllamaUnavailableError(LLMError):
    """Raised when Ollama can't be reached after exhausting retries."""


class StructuredOutputError(LLMError):
    """Raised when the model returns invalid JSON or fails schema validation."""


# ════════════════════════════════════════════════════════════════════════════
# Cache key
# ════════════════════════════════════════════════════════════════════════════

def content_hash(parts: Iterable[Any]) -> str:
    """Return a stable SHA-1 hex digest over the given parts.

    Each part is converted to ``str`` and joined with a NUL separator.
    Order is significant. Use this for LLM cache keys so the same
    ``(model, system, user, schema_version)`` tuple resolves to the same
    cache file on every run.
    """
    h = hashlib.sha1()
    h.update(CACHE_SCHEMA_VERSION.encode("utf-8"))
    for p in parts:
        h.update(b"\x00")
        h.update(str(p).encode("utf-8"))
    return h.hexdigest()


# ════════════════════════════════════════════════════════════════════════════
# Response wrapper
# ════════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class LLMResponse:
    """The parsed and (optionally) validated result of one chat call.

    Attributes:
        parsed: The JSON-parsed payload (a ``dict`` or pydantic model
            instance when a ``schema`` was provided).
        raw_text: The model's full assistant message text.
        model: Identifier of the model that produced this response.
        cached: ``True`` when the response was served from the on-disk cache.
        cache_key: The SHA-1 hex digest used as the cache file stem.
        elapsed_s: Wall-clock duration of the chat call (0.0 for cache hits).
        prompt_tokens: Tokens consumed by the prompt (``None`` if Ollama
            didn't report it).
        eval_tokens: Tokens emitted by the assistant (``None`` if not
            reported).
    """

    parsed: Any
    raw_text: str
    model: str
    cached: bool
    cache_key: str
    elapsed_s: float = 0.0
    prompt_tokens: int | None = None
    eval_tokens: int | None = None


# ════════════════════════════════════════════════════════════════════════════
# Client
# ════════════════════════════════════════════════════════════════════════════

@dataclass
class OllamaClient(AbstractContextManager["OllamaClient"]):
    """Synchronous Ollama HTTP client tuned for structured-output use.

    Attributes:
        model: Default model identifier (e.g. ``"qwen2.5:14b"``). Per-call
            ``model=`` argument overrides this.
        url: Base URL of the Ollama server.
        cache_dir: Directory for cached JSON responses. ``None`` disables
            caching entirely.
        timeout_s: Per-request HTTP timeout.
        max_retries: Maximum retry attempts on transient failure.
        temperature: Default sampling temperature (0.0 = greedy/deterministic).
        num_ctx: Context window length to request from Ollama.
    """

    model: str = DEFAULT_MODEL
    url: str = DEFAULT_OLLAMA_URL
    cache_dir: Path | None = None
    timeout_s: float = DEFAULT_TIMEOUT_S
    max_retries: int = DEFAULT_MAX_RETRIES
    temperature: float = DEFAULT_TEMPERATURE
    num_ctx: int = DEFAULT_NUM_CTX
    _session: requests.Session | None = field(default=None, init=False, repr=False)
    _stats: dict[str, int] = field(default_factory=dict, init=False, repr=False)

    # ─── Lifecycle ───────────────────────────────────────────────────────

    def __enter__(self) -> OllamaClient:
        self._session = requests.Session()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:  # noqa: ANN001
        if self._session is not None:
            self._session.close()
            self._session = None

    @property
    def session(self) -> requests.Session:
        if self._session is None:
            self._session = requests.Session()
        return self._session

    # ─── Stats ───────────────────────────────────────────────────────────

    @property
    def stats(self) -> dict[str, int]:
        """Read-only counter snapshot: ``cache_hits``, ``calls``, ``retries``."""
        return dict(self._stats)

    def _bump(self, key: str) -> None:
        self._stats[key] = self._stats.get(key, 0) + 1

    # ─── Health check ────────────────────────────────────────────────────

    def ping(self) -> bool:
        """Return ``True`` if Ollama responds to ``/api/tags`` within timeout."""
        try:
            r = self.session.get(f"{self.url}/api/tags", timeout=min(5.0, self.timeout_s))
            return r.status_code == 200
        except (RequestException, ConnectionError):
            return False

    def list_models(self) -> list[str]:
        """Return the list of installed model names (or empty on failure)."""
        try:
            r = self.session.get(f"{self.url}/api/tags", timeout=min(10.0, self.timeout_s))
            r.raise_for_status()
            data = r.json()
        except (RequestException, ValueError, KeyError):
            return []
        return [str(m.get("name", "")) for m in data.get("models", []) if m.get("name")]

    # ─── Cache I/O ───────────────────────────────────────────────────────

    def _cache_path(self, key: str) -> Path | None:
        if self.cache_dir is None:
            return None
        return self.cache_dir / f"{key}.json"

    def _read_cache(self, key: str) -> dict[str, Any] | None:
        path = self._cache_path(key)
        if path is None or not path.exists():
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            logger.warning("Cache read failed for %s: %s", path, e)
            return None

    def _write_cache(self, key: str, payload: dict[str, Any]) -> None:
        path = self._cache_path(key)
        if path is None:
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(path.suffix + ".tmp")
        try:
            tmp.write_text(
                json.dumps(payload, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            tmp.replace(path)
        except OSError as e:
            logger.warning("Cache write failed for %s: %s", path, e)

    # ─── Core: chat → JSON ───────────────────────────────────────────────

    def chat_json(
        self,
        *,
        system: str,
        user: str,
        schema: type[T] | None = None,
        cache_key_inputs: Iterable[Any] | None = None,
        model: str | None = None,
        temperature: float | None = None,
        num_ctx: int | None = None,
        bypass_cache: bool = False,
    ) -> LLMResponse:
        """Send a chat request expecting a JSON-shaped reply.

        Args:
            system: System prompt (sets the role).
            user: User message (the actual query).
            schema: Optional pydantic ``BaseModel`` subclass. When provided,
                the parsed JSON is validated and ``LLMResponse.parsed`` is
                an instance of that model.
            cache_key_inputs: Iterable of stable inputs used to compute the
                cache key. ``None`` falls back to ``(model, system, user)``.
                Provide a stable fingerprint when the prompt embeds variable
                content you want included in the key.
            model: Override the default model for this call.
            temperature: Override the default temperature for this call.
            num_ctx: Override the default context window for this call.
            bypass_cache: When ``True``, skip the cache for both read and
                write (forces a live LLM call).

        Returns:
            :class:`LLMResponse`

        Raises:
            OllamaUnavailableError: All retries exhausted, transport-level.
            StructuredOutputError: The model returned malformed JSON or the
                payload failed schema validation.
        """
        chosen_model = model or self.model
        chosen_temp = self.temperature if temperature is None else float(temperature)
        chosen_ctx = self.num_ctx if num_ctx is None else int(num_ctx)

        key_parts = (
            list(cache_key_inputs)
            if cache_key_inputs is not None
            else [chosen_model, system, user]
        )
        key = content_hash(key_parts)

        if not bypass_cache:
            cached = self._read_cache(key)
            if cached is not None:
                self._bump("cache_hits")
                parsed = self._validate_or_pass(cached.get("parsed", {}), schema)
                return LLMResponse(
                    parsed=parsed,
                    raw_text=str(cached.get("raw_text", "")),
                    model=str(cached.get("model", chosen_model)),
                    cached=True,
                    cache_key=key,
                    elapsed_s=0.0,
                    prompt_tokens=cached.get("prompt_tokens"),
                    eval_tokens=cached.get("eval_tokens"),
                )

        body = {
            "model": chosen_model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "stream": False,
            "format": "json",
            "options": {
                "temperature": chosen_temp,
                "num_ctx": chosen_ctx,
            },
        }

        payload = self._post_with_retries(f"{self.url}/api/chat", body)
        raw_text = self._extract_message(payload)
        parsed_dict = self._parse_json(raw_text)
        parsed = self._validate_or_pass(parsed_dict, schema)

        # Cache writes always store the *parsed dict*, not the schema
        # instance, so the cache stays JSON-roundtrippable.
        if not bypass_cache:
            self._write_cache(key, {
                "model": chosen_model,
                "raw_text": raw_text,
                "parsed": parsed_dict,
                "prompt_tokens": payload.get("prompt_eval_count"),
                "eval_tokens": payload.get("eval_count"),
            })

        self._bump("calls")
        return LLMResponse(
            parsed=parsed,
            raw_text=raw_text,
            model=chosen_model,
            cached=False,
            cache_key=key,
            elapsed_s=float(payload.get("total_duration", 0)) / 1e9,
            prompt_tokens=payload.get("prompt_eval_count"),
            eval_tokens=payload.get("eval_count"),
        )

    # ─── HTTP with retries ───────────────────────────────────────────────

    def _post_with_retries(self, url: str, body: dict[str, Any]) -> dict[str, Any]:
        delay = 1.0
        last_exc: Exception | None = None
        for attempt in range(self.max_retries + 1):
            try:
                r = self.session.post(url, json=body, timeout=self.timeout_s)
                r.raise_for_status()
                return r.json()
            except (Timeout, ReqConnError) as e:
                last_exc = e
                logger.warning(
                    "Ollama transport failure (attempt %d/%d): %s",
                    attempt + 1, self.max_retries + 1, e,
                )
            except RequestException as e:
                # HTTP-level error (4xx/5xx). Retry 5xx, fail fast on 4xx.
                resp = getattr(e, "response", None)
                if resp is not None and 400 <= resp.status_code < 500:
                    raise OllamaUnavailableError(
                        f"Ollama returned {resp.status_code}: {resp.text[:300]}",
                    ) from e
                last_exc = e
                logger.warning(
                    "Ollama HTTP error (attempt %d/%d): %s",
                    attempt + 1, self.max_retries + 1, e,
                )
            except ValueError as e:
                # JSONDecodeError on the transport-level response (rare)
                raise OllamaUnavailableError(f"Ollama returned non-JSON: {e}") from e

            if attempt < self.max_retries:
                self._bump("retries")
                time.sleep(delay)
                delay *= 2

        raise OllamaUnavailableError(
            f"Ollama unreachable after {self.max_retries + 1} attempts: {last_exc}",
        )

    # ─── Parsing helpers ─────────────────────────────────────────────────

    @staticmethod
    def _extract_message(payload: dict[str, Any]) -> str:
        """Pull the assistant message string out of an Ollama /api/chat reply."""
        msg = payload.get("message")
        if not isinstance(msg, dict):
            raise StructuredOutputError(
                f"Ollama response missing 'message' object: {payload!r}"[:300],
            )
        content = msg.get("content")
        if not isinstance(content, str) or not content.strip():
            raise StructuredOutputError("Ollama 'message.content' was empty")
        return content

    @staticmethod
    def _parse_json(raw: str) -> dict[str, Any]:
        """Parse a JSON object string. Tolerates leading/trailing whitespace
        and stray text *before* the first ``{``.

        Ollama's ``format=json`` is normally clean, but defensive parsing
        avoids spurious failures when a model emits a prefix like
        ``"Here is the JSON: {...}"`` despite the format directive.
        """
        text = raw.strip()
        if not text:
            raise StructuredOutputError("Empty response body")
        # Fast path: clean JSON
        try:
            obj = json.loads(text)
        except json.JSONDecodeError:
            # Slow path: locate the outermost {...} balanced span
            start = text.find("{")
            end = text.rfind("}")
            if start == -1 or end == -1 or end < start:
                raise StructuredOutputError(
                    f"No JSON object found in response: {text[:200]!r}",
                ) from None
            try:
                obj = json.loads(text[start:end + 1])
            except json.JSONDecodeError as e:
                raise StructuredOutputError(
                    f"JSON parse failed: {e}; body={text[:200]!r}",
                ) from e
        if not isinstance(obj, dict):
            raise StructuredOutputError(
                f"Expected JSON object, got {type(obj).__name__}",
            )
        return obj

    @staticmethod
    def _validate_or_pass(data: dict[str, Any], schema: type[T] | None) -> Any:
        """Validate ``data`` against the optional pydantic schema."""
        if schema is None:
            return data
        # Lazy import: pydantic is heavy and only required when validating.
        try:
            from pydantic import BaseModel, ValidationError
        except ImportError as e:  # pragma: no cover
            raise LLMError("pydantic is required for schema validation") from e
        if not isinstance(schema, type) or not issubclass(schema, BaseModel):
            raise LLMError(f"schema must subclass pydantic.BaseModel, got {schema!r}")
        try:
            return schema.model_validate(data)
        except ValidationError as e:
            raise StructuredOutputError(
                f"Schema validation failed for {schema.__name__}: {e}",
            ) from e
