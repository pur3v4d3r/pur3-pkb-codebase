#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""elaborator — V6 two-pass orchestrator.

Owns the (Pass A → Pass B) flow for one ConceptBundle:

    1. ``run_outline``    → calls Ollama with the outline contract.
    2. ``run_elaborate``  → calls Ollama with the elaboration contract,
                            feeding in the outline as additional context.
    3. ``elaborate_concept`` → convenience wrapper returning both responses
                            plus a combined ``cached`` flag.

The elaborator is independent of the renderer and the merger — it only
produces validated response objects. The pipeline orchestrator is
responsible for routing them downstream.

Version:
    1.0.0
Python:
    >=3.10
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any

from lib.llm_client import (
    LLMError,
    OllamaClient,
    OllamaUnavailableError,
    StructuredOutputError,
)

from . import prompts

logger = logging.getLogger(__name__)


# ════════════════════════════════════════════════════════════════════════════
# Result aggregate
# ════════════════════════════════════════════════════════════════════════════

@dataclass
class ElaborateResult:
    """Aggregate output of the two-pass run for one bundle."""
    outline: Any                 # OutlineResponse | dict
    elaborate: Any | None        # ElaborateResponse | dict | None when unworthy
    outline_cached: bool = False
    elaborate_cached: bool = False
    worthy: bool = True
    worthy_reason: str = ""

    @property
    def cached(self) -> bool:
        """Both passes hit cache."""
        return self.outline_cached and (
            self.elaborate is None or self.elaborate_cached
        )


# ════════════════════════════════════════════════════════════════════════════
# Support-block formatting (mirrors V4 _build_user_prompt logic)
# ════════════════════════════════════════════════════════════════════════════

def format_support_block(bundle: Any) -> str:
    """Render a ConceptBundle's supporting callouts as a flat text block.

    Args:
        bundle: A V4 ``ConceptBundle`` (duck-typed via ``.support``).

    Returns:
        Multi-line string. Empty-callout case returns a placeholder
        compatible with the prompt templates.
    """
    support = getattr(bundle, "support", None) or []
    if not support:
        return "(No additional supporting callouts found.)"
    lines: list[str] = []
    for sc in support:
        head = f"- [{sc.type}] {sc.title}".strip()
        body = (sc.body or "").replace("\n", " ").strip()
        if body:
            head += f": {body}"
        lines.append(head)
    return "\n".join(lines)


# ════════════════════════════════════════════════════════════════════════════
# Pass A — Outline
# ════════════════════════════════════════════════════════════════════════════

def run_outline(
    bundle: Any,
    client: OllamaClient,
    *,
    model: str,
    bypass_cache: bool,
) -> tuple[Any, bool]:
    """Run Pass A. Returns ``(OutlineResponse, cached)``.

    Raises:
        OllamaUnavailableError: server unreachable.
        StructuredOutputError: invalid JSON / schema violation.
        LLMError: any other LLM failure.
    """
    user_prompt = prompts.build_outline_user_prompt(
        title=bundle.title,
        report_title=getattr(bundle, "report_title", "") or "",
        domain=getattr(bundle, "domain", "") or "",
        aliases=list(getattr(bundle, "aliases", []) or []),
        related_links=list(getattr(bundle, "related_links", []) or [])[:15],
        definition_body=getattr(bundle, "definition_body", "") or "",
        support_block=format_support_block(bundle),
    )
    schema = prompts.OutlineResponse if prompts._PYDANTIC_AVAILABLE else None
    rsp = client.chat_json(
        system=prompts.OUTLINE_SYSTEM_PROMPT,
        user=user_prompt,
        schema=schema,
        model=model,
        cache_key_inputs=(
            prompts.OUTLINE_CONTRACT_VERSION,
            model,
            bundle.title.lower(),
            getattr(bundle, "report_stem", "") or "",
            (getattr(bundle, "definition_body", "") or "")[:300],
        ),
        bypass_cache=bypass_cache,
    )
    return rsp.parsed, rsp.cached


# ════════════════════════════════════════════════════════════════════════════
# Pass B — Elaborate
# ════════════════════════════════════════════════════════════════════════════

def run_elaborate(
    bundle: Any,
    outline: Any,
    client: OllamaClient,
    *,
    model: str,
    bypass_cache: bool,
) -> tuple[Any, bool]:
    """Run Pass B given a Pass-A outline. Returns ``(ElaborateResponse, cached)``.

    Raises:
        OllamaUnavailableError: server unreachable.
        StructuredOutputError: invalid JSON / schema violation.
        LLMError: any other LLM failure.
    """
    user_prompt = prompts.build_elaborate_user_prompt(
        title=bundle.title,
        report_title=getattr(bundle, "report_title", "") or "",
        domain=getattr(bundle, "domain", "") or "",
        definition_body=getattr(bundle, "definition_body", "") or "",
        support_block=format_support_block(bundle),
        outline=outline,
    )
    schema = prompts.ElaborateResponse if prompts._PYDANTIC_AVAILABLE else None
    # Cache key includes the outline's canonical_title + section count so a
    # changed outline forces a fresh elaboration even with the same source.
    sections = getattr(outline, "section_outline", None) or []
    section_sig = "|".join(
        (getattr(s, "section", None) or s.get("section", "")) for s in sections
    )
    rsp = client.chat_json(
        system=prompts.ELABORATE_SYSTEM_PROMPT,
        user=user_prompt,
        schema=schema,
        model=model,
        cache_key_inputs=(
            prompts.ELABORATE_CONTRACT_VERSION,
            model,
            bundle.title.lower(),
            getattr(bundle, "report_stem", "") or "",
            getattr(outline, "canonical_title", "") or "",
            getattr(outline, "seed_definition", "")[:200] or "",
            section_sig,
        ),
        bypass_cache=bypass_cache,
    )
    return rsp.parsed, rsp.cached


# ════════════════════════════════════════════════════════════════════════════
# Two-pass convenience wrapper
# ════════════════════════════════════════════════════════════════════════════

def elaborate_concept(
    bundle: Any,
    client: OllamaClient,
    *,
    model: str,
    bypass_cache: bool,
    no_gate: bool = False,
) -> ElaborateResult:
    """End-to-end two-pass elaboration for one bundle.

    The outline pass acts as the worthiness gate. When ``worthy=False``
    (and ``no_gate`` is False), Pass B is SKIPPED to save tokens.

    Args:
        bundle: A V4 ``ConceptBundle``.
        client: An open ``OllamaClient``.
        model: Model name (e.g. ``qwen2.5:7b-instruct-q5_K_M``).
        bypass_cache: Force live LLM calls.
        no_gate: When True, run Pass B even for unworthy outlines.

    Returns:
        :class:`ElaborateResult`.

    Raises:
        OllamaUnavailableError, StructuredOutputError, LLMError.
    """
    outline, outline_cached = run_outline(
        bundle, client, model=model, bypass_cache=bypass_cache,
    )
    worthy = bool(getattr(outline, "worthy", True))
    worthy_reason = str(getattr(outline, "worthy_reason", "") or "").strip()

    if not worthy and not no_gate:
        logger.info("Outline marked unworthy: %s — %s",
                    bundle.title, worthy_reason or "(no reason)")
        return ElaborateResult(
            outline=outline,
            elaborate=None,
            outline_cached=outline_cached,
            elaborate_cached=False,
            worthy=False,
            worthy_reason=worthy_reason,
        )

    elaborate, elaborate_cached = run_elaborate(
        bundle, outline, client, model=model, bypass_cache=bypass_cache,
    )
    return ElaborateResult(
        outline=outline,
        elaborate=elaborate,
        outline_cached=outline_cached,
        elaborate_cached=elaborate_cached,
        worthy=worthy,
        worthy_reason=worthy_reason,
    )


__all__ = [
    "ElaborateResult",
    "format_support_block",
    "run_outline",
    "run_elaborate",
    "elaborate_concept",
]
