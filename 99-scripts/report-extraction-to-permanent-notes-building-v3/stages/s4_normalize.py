#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""s4_normalize.py — Stage 4 (opt-in): LLM concept normalization.

For each consolidated :class:`lib.candidate.Candidate`, asks a local Ollama
model to return a canonical name, 3–5 aliases, a one-sentence definition,
and a parent-domain suggestion. The Candidate is then updated via
``dataclasses.replace`` (Candidate is frozen).

Inserted between Stage 3 and Stage 5 only when ``--llm-normalize`` is passed
to the top-level pipeline.

Input:
    ``<input-dir>/_consolidated-candidates.json`` (Stage 3 output)

Output:
    ``<output-dir>/_normalized-candidates.json`` (same envelope shape)

Constitutional guarantees (spec §2.3):
    1. **Evidence is never modified.** All bucket fields, source_reports,
       wiki_links_seen, and existing definition_body content are preserved.
       The LLM proposes a *suggested* definition only — it is written to
       ``definition_body`` exclusively when the field was empty.
    2. **No new wiki-links are invented.** This stage only touches scalar
       metadata (canonical_name, primary_name, aliases, domain).
    3. **Idempotent / cacheable.** Each candidate's request is keyed by
       ``extraction_hash``; re-runs against unchanged inputs cost zero LLM
       time.
    4. **Failure is non-fatal by default.** A per-candidate LLM failure
       leaves the original Candidate intact and is recorded in the stats
       block. ``--strict`` promotes failures to a non-zero exit.

Usage:
    python -m stages.s4_normalize _v3-output/runs/001
    python -m stages.s4_normalize _v3-output/runs/001 -o _v3-output/runs/001 \\
        --model qwen2.5:7b-instruct-q5_K_M --strict
    python -m stages.s4_normalize _v3-output/runs/001 --dry-run -v

Exit codes:
    0   success
    1   uncaught error
    2   input file missing or unreadable
    3   write permission denied
    4   no candidates found
    5   one or more candidates failed (only with --strict)
    6   Ollama unreachable
    130 interrupted (SIGINT)

Spec: §5 Phase 7 (concept normalization).
Version: 1.0.0
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

# ── sys.path injection ──────────────────────────────────────────────────
_HERE = Path(__file__).resolve().parent
_V3_ROOT = _HERE.parent
if str(_V3_ROOT) not in sys.path:
    sys.path.insert(0, str(_V3_ROOT))

import config_v3  # noqa: E402
from lib.candidate import (  # noqa: E402
    DEFAULT_DOMAIN,
    Candidate,
)
from lib.llm_client import (  # noqa: E402
    LLMError,
    OllamaClient,
    OllamaUnavailableError,
    StructuredOutputError,
)

logger = logging.getLogger(__name__)

__version__ = "1.0.0"

# ════════════════════════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════════════════════════

INPUT_FILENAME: str = "_consolidated-candidates.json"
OUTPUT_FILENAME: str = "_normalized-candidates.json"

#: Cache-key prompt-contract version. Bump when the prompt below changes
#: in a way that should invalidate every prior cached normalization.
PROMPT_CONTRACT_VERSION: str = "norm-v1"

#: Maximum aliases we'll keep, even if the model returns more.
MAX_ALIASES: int = 8

#: Maximum length for any single alias (chars). Defends against the model
#: returning a sentence in the aliases list.
MAX_ALIAS_LEN: int = 80

#: Maximum length of the definition we accept (chars). Defends against
#: runaway generations. ~400 chars ≈ 60–80 words.
MAX_DEFINITION_LEN: int = 400

SYSTEM_PROMPT: str = (
    "You are a careful, conservative academic taxonomist. Your job is to "
    "normalize a single concept name and produce a small, accurate JSON "
    "metadata record. Do not invent aliases that are not standard usage. "
    "Do not editorialize. Reply with JSON only, no preamble."
)

USER_PROMPT_TEMPLATE: str = """\
Concept candidate: {primary_name!r}

Existing aliases (may be empty): {aliases_list}
Current parent domain (may be a placeholder): {domain!r}
Existing one-line definition (may be empty): {definition!r}

Sample evidence excerpts from the source corpus (max 3, may be empty):
{evidence_block}

Return a JSON object with EXACTLY these fields:
{{
  "canonical_name": "the most standard, well-known form of this concept "
                    "(prefer expanded forms over acronyms, prefer the most "
                    "commonly cited variant)",
  "aliases": ["3 to 5 widely recognized alternative names; include common "
              "acronyms, expansions, and frequent paraphrases; do NOT invent"],
  "definition": "one sentence (<= 40 words) plain-English definition; "
                "leave empty string if you are not confident",
  "domain": "single short domain label (e.g. 'cognitive-psychology', "
            "'machine-learning', 'pedagogy'); use kebab-case"
}}

Rules:
- All four fields MUST be present.
- "aliases" must be a JSON array of strings (may be empty if you are uncertain).
- Do NOT include the canonical_name itself inside the aliases array.
- Do NOT invent biographical or historical claims; the definition must be
  grounded in the concept's standard meaning.
- If the candidate is clearly a non-concept (a sentence, a filename,
  a fragment), return the original primary_name as canonical_name with
  empty aliases, empty definition, and domain "unknown".
"""


# ════════════════════════════════════════════════════════════════════════════
# Result types
# ════════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class NormalizationResult:
    """Outcome of normalising a single Candidate.

    Attributes:
        candidate: The post-normalisation Candidate. On failure, identical
            to the input Candidate.
        ok: ``True`` if the LLM call succeeded and the response was applied.
        cached: ``True`` if the result was served from the cache.
        changed: ``True`` if normalization actually altered the Candidate.
        error: Error message on failure, otherwise empty string.
    """

    candidate: Candidate
    ok: bool
    cached: bool
    changed: bool
    error: str = ""


# ════════════════════════════════════════════════════════════════════════════
# Prompt construction
# ════════════════════════════════════════════════════════════════════════════

def _evidence_excerpts(candidate: Candidate, max_n: int = 3,
                       max_chars: int = 280) -> list[str]:
    """Pull up to ``max_n`` short evidence excerpts from the candidate.

    Prefers the ``evidence`` and ``insight`` buckets if present. Each
    excerpt is truncated to ``max_chars`` characters. Used to give the
    LLM enough context to disambiguate without bloating the prompt.
    """
    out: list[str] = []
    # Buckets to sample from, in priority order. Names must match
    # lib.candidate.Candidate field names exactly (see BUCKET_FIELDS).
    for bucket_name in ("evidence", "insights", "reflections",
                        "section_summaries", "examples"):
        items = getattr(candidate, bucket_name, ())
        for item in items:
            body = (item.body or "").strip().replace("\n", " ")
            if not body:
                continue
            if len(body) > max_chars:
                body = body[: max_chars - 1] + "…"
            out.append(body)
            if len(out) >= max_n:
                return out
    # Definition fallback if no evidence buckets had content.
    if not out and candidate.definition_body:
        body = candidate.definition_body.strip().replace("\n", " ")
        if len(body) > max_chars:
            body = body[: max_chars - 1] + "…"
        out.append(body)
    return out


def build_user_prompt(candidate: Candidate) -> str:
    """Render the user-prompt template for a single Candidate."""
    excerpts = _evidence_excerpts(candidate)
    if excerpts:
        evidence_block = "\n".join(f"  - {e}" for e in excerpts)
    else:
        evidence_block = "  (none)"
    aliases_list = json.dumps(list(candidate.aliases), ensure_ascii=False)
    return USER_PROMPT_TEMPLATE.format(
        primary_name=candidate.primary_name,
        aliases_list=aliases_list,
        domain=candidate.domain,
        definition=candidate.definition_body[:200],
        evidence_block=evidence_block,
    )


# ════════════════════════════════════════════════════════════════════════════
# Response validation + application
# ════════════════════════════════════════════════════════════════════════════

def _coerce_str(v: Any, *, max_len: int = 0) -> str:
    """Coerce ``v`` to a stripped string. ``max_len > 0`` truncates."""
    if v is None:
        return ""
    s = str(v).strip()
    if max_len and len(s) > max_len:
        s = s[: max_len - 1] + "…"
    return s


def _coerce_aliases(raw: Any, canonical: str) -> tuple[str, ...]:
    """Coerce the model's ``aliases`` field into a clean tuple of strings.

    - Drops non-string items.
    - Drops empties and items longer than ``MAX_ALIAS_LEN``.
    - Drops the canonical name (case-insensitive) so it doesn't double up.
    - De-duplicates while preserving order.
    - Caps at ``MAX_ALIASES``.
    """
    if not isinstance(raw, list):
        return ()
    seen: set[str] = set()
    out: list[str] = []
    canonical_lower = canonical.strip().lower()
    for item in raw:
        if not isinstance(item, str):
            continue
        s = item.strip()
        if not s or len(s) > MAX_ALIAS_LEN:
            continue
        if s.lower() == canonical_lower:
            continue
        key = s.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(s)
        if len(out) >= MAX_ALIASES:
            break
    return tuple(out)


def apply_normalization(
    candidate: Candidate,
    parsed: dict[str, Any],
) -> tuple[Candidate, bool]:
    """Apply a parsed LLM response to a Candidate.

    Returns ``(new_candidate, changed)``.

    Constitutional guarantees:
        - ``definition_body`` is only overwritten if the original was empty.
        - Existing aliases are *unioned* with the new ones (LLM aliases are
          additive; we never strip a human-curated alias).
        - Empty / missing fields in the LLM response are silently ignored.
    """
    new_canonical = _coerce_str(
        parsed.get("canonical_name"), max_len=200,
    ) or candidate.primary_name
    new_definition = _coerce_str(
        parsed.get("definition"), max_len=MAX_DEFINITION_LEN,
    )
    new_domain = _coerce_str(parsed.get("domain"), max_len=80)
    new_aliases_only = _coerce_aliases(parsed.get("aliases"), new_canonical)

    # Union with existing aliases. Preserve original order, then append new.
    seen: set[str] = set()
    union_aliases: list[str] = []
    for a in (*candidate.aliases, *new_aliases_only):
        key = a.strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        union_aliases.append(a)
    union_aliases = union_aliases[:MAX_ALIASES]

    # Definition: never overwrite a human / extracted definition.
    final_definition = candidate.definition_body or new_definition

    # Domain: only replace the placeholder default.
    if candidate.domain == DEFAULT_DOMAIN and new_domain and new_domain != "unknown":
        final_domain = new_domain
    else:
        final_domain = candidate.domain

    # canonical_name: replace; primary_name unchanged (kept as the original
    # extraction-time form to preserve provenance).
    new = replace(
        candidate,
        canonical_name=new_canonical,
        aliases=tuple(union_aliases),
        domain=final_domain,
        definition_body=final_definition,
    )
    changed = (
        new.canonical_name != candidate.canonical_name
        or new.aliases != candidate.aliases
        or new.domain != candidate.domain
        or new.definition_body != candidate.definition_body
    )
    return new, changed


# ════════════════════════════════════════════════════════════════════════════
# Per-candidate normalization
# ════════════════════════════════════════════════════════════════════════════

def normalize_candidate(
    candidate: Candidate,
    client: OllamaClient,
    *,
    model: str | None = None,
) -> NormalizationResult:
    """Normalize a single Candidate via the LLM.

    Catches every LLM error and returns ``ok=False`` with the candidate
    untouched. Callers that want hard-fail behaviour should check ``ok``
    and surface failures themselves.
    """
    user = build_user_prompt(candidate)
    try:
        rsp = client.chat_json(
            system=SYSTEM_PROMPT,
            user=user,
            model=model,
            cache_key_inputs=(
                PROMPT_CONTRACT_VERSION,
                model or client.model,
                candidate.extraction_hash,
            ),
        )
    except (OllamaUnavailableError, StructuredOutputError, LLMError) as e:
        logger.warning(
            "normalize failed for %r: %s", candidate.primary_name, e,
        )
        return NormalizationResult(
            candidate=candidate, ok=False, cached=False, changed=False,
            error=str(e),
        )

    parsed = rsp.parsed if isinstance(rsp.parsed, dict) else {}
    new_cand, changed = apply_normalization(candidate, parsed)
    return NormalizationResult(
        candidate=new_cand,
        ok=True,
        cached=rsp.cached,
        changed=changed,
    )


# ════════════════════════════════════════════════════════════════════════════
# Orchestration
# ════════════════════════════════════════════════════════════════════════════

def normalize_all(
    candidates: list[Candidate],
    client: OllamaClient,
    *,
    model: str | None = None,
    progress_every: int = 10,
) -> tuple[list[Candidate], dict[str, Any]]:
    """Normalize every Candidate sequentially. Ollama is single-tenant.

    Returns:
        (normalized_candidates, stats)
    """
    out: list[Candidate] = []
    n_ok = 0
    n_cached = 0
    n_changed = 0
    n_failed = 0
    failures: list[dict[str, str]] = []

    total = len(candidates)
    for i, cand in enumerate(candidates, 1):
        result = normalize_candidate(cand, client, model=model)
        out.append(result.candidate)
        if result.ok:
            n_ok += 1
            if result.cached:
                n_cached += 1
            if result.changed:
                n_changed += 1
        else:
            n_failed += 1
            failures.append({
                "primary_name": cand.primary_name,
                "extraction_hash": cand.extraction_hash,
                "error": result.error,
            })
        if i % progress_every == 0 or i == total:
            logger.info(
                "normalized %d/%d  (ok=%d cache=%d changed=%d failed=%d)",
                i, total, n_ok, n_cached, n_changed, n_failed,
            )

    stats: dict[str, Any] = {
        "candidates_in": total,
        "candidates_out": len(out),
        "ok": n_ok,
        "cached": n_cached,
        "changed": n_changed,
        "failed": n_failed,
        "model": model or client.model,
        "prompt_contract_version": PROMPT_CONTRACT_VERSION,
    }
    if failures:
        # Cap surfaced failures so the stats block stays readable; the full
        # list is in the logs.
        stats["failures_sample"] = failures[:20]
    return out, stats


# ════════════════════════════════════════════════════════════════════════════
# I/O
# ════════════════════════════════════════════════════════════════════════════

def load_consolidated(path: Path) -> tuple[list[Candidate], dict[str, Any]]:
    """Load a Stage-3 consolidated payload and return (candidates, raw_payload)."""
    with path.open("r", encoding="utf-8") as fh:
        payload = json.load(fh)
    raw_cands = payload.get("candidates", []) or []
    cands = [Candidate.from_dict(d) for d in raw_cands]
    return cands, payload


def write_output(
    candidates: list[Candidate],
    upstream_payload: dict[str, Any],
    stats: dict[str, Any],
    output_path: Path,
) -> None:
    """Write the normalized-candidates JSON snapshot."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": __version__,
        "upstream_version": upstream_payload.get("version", ""),
        "upstream_stats": upstream_payload.get("stats", {}),
        "stats": stats,
        "candidates": [c.to_dict() for c in candidates],
    }
    with output_path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2, sort_keys=False)


# ════════════════════════════════════════════════════════════════════════════
# CLI
# ════════════════════════════════════════════════════════════════════════════

def build_parser() -> argparse.ArgumentParser:
    """Construct the Stage 4 argument parser."""
    parser = argparse.ArgumentParser(
        prog="s4_normalize",
        description="Stage 4 (opt-in): LLM concept normalization + alias mining.",
        epilog=(
            "Examples:\n"
            "  python -m stages.s4_normalize _v3-output/runs/001\n"
            "  python -m stages.s4_normalize _v3-output/runs/001 --strict\n"
            "  python -m stages.s4_normalize _v3-output/runs/001 \\\n"
            "      --model qwen2.5:14b -o _v3-output/runs/001 -v\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "input", type=Path,
        help="Directory containing _consolidated-candidates.json (Stage 3 output) "
             "OR a path to that file directly.",
    )
    parser.add_argument(
        "-o", "--output-dir", type=Path, default=None,
        help=f"Directory to write {OUTPUT_FILENAME} into (default: input dir).",
    )
    parser.add_argument(
        "--model", type=str, default=config_v3.LLM_MODEL_NORMALIZE,
        help=f"Ollama model id (default: {config_v3.LLM_MODEL_NORMALIZE}).",
    )
    parser.add_argument(
        "--ollama-url", type=str, default=config_v3.OLLAMA_URL,
        help=f"Ollama base URL (default: {config_v3.OLLAMA_URL}).",
    )
    parser.add_argument(
        "--cache-dir", type=Path, default=config_v3.LLM_CACHE_DIR,
        help=f"Directory for LLM response cache (default: "
             f"{config_v3.LLM_CACHE_DIR}). Use 'NONE' to disable.",
    )
    parser.add_argument(
        "--limit", type=int, default=0,
        help="Process only the first N candidates (debug).",
    )
    parser.add_argument(
        "--strict", action="store_true",
        help="Exit non-zero if any candidate normalization fails.",
    )
    parser.add_argument(
        "-n", "--dry-run", action="store_true",
        help="Run normalization but do not write the output file.",
    )
    parser.add_argument(
        "-v", "--verbose", action="count", default=0,
        help="Increase logging verbosity (repeatable).",
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true",
        help="Suppress non-error output.",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}",
    )
    return parser


def configure_logging(verbosity: int, quiet: bool) -> None:
    """Configure the root logger from CLI verbosity flags."""
    if quiet:
        level = logging.ERROR
    elif verbosity >= 2:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def _resolve_input(input_path: Path) -> Path:
    """Accept either a directory or a file; return the JSON file path."""
    if input_path.is_dir():
        candidate = input_path / INPUT_FILENAME
        if not candidate.exists():
            raise FileNotFoundError(
                f"{INPUT_FILENAME} not found in {input_path}",
            )
        return candidate
    return input_path


def main(argv: list[str] | None = None) -> int:
    """Stage 4 entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    try:
        input_file = _resolve_input(args.input)
    except FileNotFoundError as e:
        logger.error("%s", e)
        return 2

    try:
        candidates, upstream = load_consolidated(input_file)
    except (OSError, json.JSONDecodeError) as e:
        logger.error("failed to load %s: %s", input_file, e)
        return 2

    if not candidates:
        logger.error("no candidates found in %s", input_file)
        return 4

    if args.limit and args.limit > 0:
        candidates = candidates[: args.limit]
        logger.info("limit=%d → processing first %d candidates",
                    args.limit, len(candidates))

    cache_dir: Path | None
    if str(args.cache_dir).upper() == "NONE":
        cache_dir = None
    else:
        cache_dir = Path(args.cache_dir)

    try:
        with OllamaClient(
            model=args.model,
            url=args.ollama_url,
            cache_dir=cache_dir,
            timeout_s=config_v3.LLM_REQUEST_TIMEOUT_S,
            max_retries=config_v3.LLM_MAX_RETRIES,
        ) as client:
            if not client.ping():
                logger.error("Ollama unreachable at %s", args.ollama_url)
                return 6
            if args.model not in client.list_models():
                logger.warning(
                    "Model %r is not in the Ollama tag list; "
                    "Ollama will attempt to pull on first use.",
                    args.model,
                )
            normalized, stats = normalize_all(
                candidates, client, model=args.model,
            )
    except OllamaUnavailableError as e:
        logger.error("Ollama unreachable: %s", e)
        return 6
    except KeyboardInterrupt:
        logger.warning("Interrupted by user")
        return 130

    logger.warning(
        "normalized %d candidates: ok=%d cached=%d changed=%d failed=%d",
        stats["candidates_in"], stats["ok"], stats["cached"],
        stats["changed"], stats["failed"],
    )

    if args.dry_run:
        logger.warning("--dry-run: skipping write")
        return 5 if (args.strict and stats["failed"]) else 0

    output_dir = args.output_dir or input_file.parent
    output_path = output_dir / OUTPUT_FILENAME
    try:
        write_output(normalized, upstream, stats, output_path)
    except PermissionError as e:
        logger.error("write denied: %s", e)
        return 3
    except OSError as e:
        logger.error("write failed: %s", e)
        return 1

    logger.warning("wrote %s", output_path)
    return 5 if (args.strict and stats["failed"]) else 0


# ════════════════════════════════════════════════════════════════════════════
# Entry-point guard
# ════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    sys.exit(main())
