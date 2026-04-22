#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""m3_verify.py — Phase 3: LLM verification of cluster merge candidates.

For each cluster from Phase 2:
  - TIER-0 clusters → pass through (names are identical, no LLM needed)
  - auto_merge clusters (score ≥ 0.95) → pass through (skip LLM)
  - Others → one OllamaClient.chat_json() call; keep only merge=True results

Cache key is stable across reruns (sorted member titles + prompt version),
so re-running after interruption costs zero LLM calls for already-verified clusters.

Output: merge-state/03_verified.json
"""
from __future__ import annotations

import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

_HERE = Path(__file__).resolve().parent.parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import config_merge
from lib.llm_client import OllamaClient, OllamaUnavailableError, StructuredOutputError

logger = logging.getLogger(__name__)

try:
    from pydantic import BaseModel, field_validator

    class VerifyResponse(BaseModel):
        merge: bool
        reasoning: str
        primary_title: Optional[str] = None

        @field_validator("reasoning")
        @classmethod
        def _reasoning_nonempty(cls, v: str) -> str:
            v = (v or "").strip()
            if not v:
                raise ValueError("reasoning must be non-empty")
            return v

    _PYDANTIC_AVAILABLE = True

except ImportError:
    VerifyResponse = None  # type: ignore[assignment,misc]
    _PYDANTIC_AVAILABLE = False


# ════════════════════════════════════════════════════════════════════════════
# Prompts
# ════════════════════════════════════════════════════════════════════════════

_SYSTEM_PROMPT = (
    "You are a rigorous knowledge-base curator. Your task is to judge whether "
    "a set of permanent notes describes the same underlying concept and should "
    "be merged into a single note.\n\n"
    "Be conservative: when in doubt, do NOT merge. Distinct concepts that merely "
    "share a domain, are related, or complement each other should NOT be merged — "
    "only merge when the notes are clearly redundant descriptions of one concept.\n\n"
    "Respond with valid JSON only. No preamble or explanation outside the JSON object."
)


def _build_user_prompt(members: list[dict[str, Any]]) -> str:
    lines = ["Permanent notes to evaluate:\n"]
    for i, m in enumerate(members, 1):
        defn = (m.get("definition_text") or "").strip()
        if not defn:
            defn = "(no definition available)"
        sources = ", ".join(m.get("source_reports") or [])
        lines += [
            f"Note {i}:",
            f"  Title: {m['title']!r}",
            f"  Domain: {m.get('domain', 'unknown')!r}",
            f"  Definition: {defn[:250]!r}",
            f"  Sources: [{sources}]",
            "",
        ]
    lines += [
        "Output JSON with exactly these keys:",
        '{',
        '  "merge": true or false,',
        '  "reasoning": "one sentence explaining the decision",',
        '  "primary_title": "the best canonical title from the list above, or null if merge=false"',
        '}',
    ]
    return "\n".join(lines)


# ════════════════════════════════════════════════════════════════════════════
# Helpers
# ════════════════════════════════════════════════════════════════════════════

def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Run previous phase first. Missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _build_stubs_index(scan: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {s["path"]: s for s in scan["stubs"]}


def _verify_cache_key(member_titles: list[str]) -> list[Any]:
    return [config_merge.VERIFY_PROMPT_VERSION, config_merge.LLM_MODEL_VERIFY, *sorted(member_titles)]


def _verify_cluster(
    cluster: dict[str, Any],
    stubs_index: dict[str, dict[str, Any]],
    client: OllamaClient,
) -> dict[str, Any] | None:
    """Run LLM verification; returns enriched cluster dict or None if merge=False."""
    members_data = [
        stubs_index[m["path"]]
        for m in cluster["members"]
        if m["path"] in stubs_index
    ]
    if len(members_data) < 2:
        return None

    titles = [m["title"] for m in members_data]
    user_prompt = _build_user_prompt(members_data)

    try:
        rsp = client.chat_json(
            system=_SYSTEM_PROMPT,
            user=user_prompt,
            schema=VerifyResponse if _PYDANTIC_AVAILABLE else None,
            cache_key_inputs=_verify_cache_key(titles),
        )
    except (OllamaUnavailableError, StructuredOutputError) as e:
        logger.warning("LLM verification failed for cluster %s: %s", cluster["cluster_id"], e)
        return None

    if _PYDANTIC_AVAILABLE and isinstance(rsp.parsed, VerifyResponse):
        merge = rsp.parsed.merge
        reasoning = rsp.parsed.reasoning
        primary_title = rsp.parsed.primary_title
    else:
        parsed = rsp.parsed if isinstance(rsp.parsed, dict) else {}
        merge = bool(parsed.get("merge", False))
        reasoning = str(parsed.get("reasoning", ""))
        primary_title = parsed.get("primary_title")

    if not merge:
        logger.debug(
            "LLM rejected merge for %s: %s",
            cluster["cluster_id"], reasoning[:100],
        )
        return None

    return {
        **cluster,
        "llm_merge": True,
        "llm_reasoning": reasoning,
        "llm_primary_title": primary_title,
        "llm_cached": rsp.cached,
    }


# ════════════════════════════════════════════════════════════════════════════
# Main
# ════════════════════════════════════════════════════════════════════════════

def run(state_dir: Path | None = None) -> dict[str, Any]:
    """Verify clusters via LLM; write 03_verified.json."""
    state_dir = state_dir or config_merge.MERGE_STATE_DIR

    scan = _load_json(state_dir / config_merge.SCAN_STATE_FILE)
    cluster_data = _load_json(state_dir / config_merge.CLUSTER_STATE_FILE)

    stubs_index = _build_stubs_index(scan)
    tier0_clusters: list[dict[str, Any]] = scan.get("tier0_clusters", [])
    clusters: list[dict[str, Any]] = cluster_data["clusters"]

    verified: list[dict[str, Any]] = []
    llm_confirmed = 0
    auto_passed = 0
    tier0_passed = len(tier0_clusters)
    llm_rejected = 0
    llm_errors = 0

    # TIER-0: pass through unconditionally
    for c in tier0_clusters:
        verified.append({
            **c,
            "llm_merge": True,
            "llm_reasoning": "TIER-0: identical normalized title",
            "llm_primary_title": None,
            "llm_cached": True,
        })

    logger.info(
        "Verifying %d clusters (%d auto-merge, %d need LLM)...",
        len(clusters),
        sum(1 for c in clusters if c["auto_merge"]),
        sum(1 for c in clusters if not c["auto_merge"]),
    )

    # Separate auto-merge from LLM-needed
    auto_merge_clusters = [c for c in clusters if c["auto_merge"]]
    llm_needed = [c for c in clusters if not c["auto_merge"]]

    # auto_merge: pass through
    for c in auto_merge_clusters:
        verified.append({
            **c,
            "llm_merge": True,
            "llm_reasoning": f"Auto-merge: similarity ≥ {config_merge.AUTO_MERGE_THRESHOLD}",
            "llm_primary_title": None,
            "llm_cached": True,
        })
        auto_passed += 1

    # LLM-needed: verify via Ollama
    if llm_needed:
        logger.info("Running LLM verification for %d clusters...", len(llm_needed))
        with OllamaClient(
            model=config_merge.LLM_MODEL_VERIFY,
            url=config_merge.OLLAMA_URL,
            cache_dir=config_merge.LLM_CACHE_DIR,
            timeout_s=config_merge.LLM_REQUEST_TIMEOUT_S,
            max_retries=config_merge.LLM_MAX_RETRIES,
        ) as client:
            for i, cluster in enumerate(llm_needed):
                if i % 50 == 0 and i > 0:
                    logger.info("  LLM: %d / %d...", i, len(llm_needed))
                result = _verify_cluster(cluster, stubs_index, client)
                if result is not None:
                    verified.append(result)
                    llm_confirmed += 1
                    if not result.get("llm_cached"):
                        logger.debug("LLM confirmed merge: %s", cluster["cluster_id"])
                else:
                    llm_rejected += 1

    logger.info(
        "Verification summary: %d tier-0 pass-through, %d auto-merge, "
        "%d LLM confirmed, %d LLM rejected, %d errors",
        tier0_passed, auto_passed, llm_confirmed, llm_rejected, llm_errors,
    )

    output: dict[str, Any] = {
        "generated_at": datetime.now().isoformat(),
        "total_input_clusters": len(clusters) + len(tier0_clusters),
        "tier0_passed": tier0_passed,
        "auto_merge_passed": auto_passed,
        "llm_confirmed": llm_confirmed,
        "llm_rejected": llm_rejected,
        "total_verified": len(verified),
        "verified_clusters": verified,
    }

    out_path = state_dir / config_merge.VERIFIED_STATE_FILE
    _write_json_atomic(out_path, output)
    logger.info("Phase 3 complete → %s", out_path)
    return output


def _write_json_atomic(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)
