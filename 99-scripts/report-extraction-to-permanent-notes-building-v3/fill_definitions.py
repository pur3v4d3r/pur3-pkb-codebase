#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fill_definitions.py — LLM-fill the empty `> [!definition]` callouts.

After ``migrate_to_vault.py``, ~933 of the migrated notes still contain a
placeholder definition::

    > [!definition] {Title}
    > *Definition pending -- derived from N source report(s).*

This script targets ONLY those files and ONLY the placeholder line. It
sends Qwen2.5-7B (via Ollama) a tight prompt grounded in the file's
existing ``## Core Explanation`` evidence callouts (NOT the model's
training data alone) and surgically replaces the placeholder with a 1-2
sentence scholarly definition.

Crucially this script is NON-DESTRUCTIVE:
    - It never touches `## Core Explanation`
    - It never touches `## Connections` / `**Related:**`
    - It never touches the frontmatter except setting `definition-source: llm-filled`
    - It only rewrites the one ``*Definition pending*`` line

Usage::

    python fill_definitions.py --dry-run --limit 5
    python fill_definitions.py --limit 50
    python fill_definitions.py
    python fill_definitions.py --bypass-cache --limit 3   # debug

Exit codes:
    0   success
    1   uncaught error
    2   target dir missing
    4   no candidate files
    5   strict mode + at least one failure
    6   Ollama unavailable
    130 interrupted
"""
from __future__ import annotations

import argparse
import logging
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field, field_validator

# Local infra (sibling modules)
_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import config_v3  # noqa: E402
from lib.llm_client import (  # noqa: E402
    LLMError,
    OllamaClient,
    OllamaUnavailableError,
    StructuredOutputError,
)


# ============================================================================
# Constants
# ============================================================================

__version__ = "1.0.0"

PROMPT_CONTRACT_VERSION = "fill-def-v1"

DEFAULT_TARGET_DIR: Path = Path(
    "D:/00-inbox/v3-pipeline-permanet-note-leftovers/_triage-output/_vault-ready"
)

DEFAULT_LLM_CACHE_DIR: Path = config_v3.LLM_CACHE_DIR / "fill_definitions"

#: The placeholder pattern to detect + replace.
_PLACEHOLDER_RE = re.compile(
    r"(> \[!definition\][^\n]*\n)(> \*Definition pending[^\n]*\*\n)",
)

#: Frontmatter block.
_FM_RE = re.compile(r"^(---\s*\n)(.*?)(\n---\s*\n)", re.DOTALL)

#: Everything from after the definition callout up to ## Connections (or EOF).
#: Captures whatever sections the report-extraction pipeline emitted:
#: Core Explanation, Practical Implications, Examples, Reflections, etc.
_EVIDENCE_BLOCK_RE = re.compile(
    r"\*Definition pending[^\n]*\*\s*\n(.*?)(?=^##\s+Connections\b|\Z)",
    re.DOTALL | re.MULTILINE,
)

SYSTEM_PROMPT = """You are a scholarly knowledge base author writing concise definitions for
a Personal Knowledge Base. Read the supplied evidence carefully and write
ONE accurate definition for the named concept, in 1-2 sentences.

Hard rules:
- Use ONLY facts that are supported by the supplied evidence; do not
  invent specifics, dates, citations, or biographical claims.
- Neutral scholarly tone. No marketing language. No "in this article".
- Do not start with "This is..." or "Refers to..." -- start with the
  noun phrase being defined.
- Reply with valid JSON only -- no markdown fences, no preamble.
"""

USER_PROMPT_TEMPLATE = """Concept: {title!r}
Domain: {domain}

Evidence from source reports (use this as your grounding):
---
{evidence}
---

Return JSON of shape:
{{
  "definition": "<1-2 sentence definition of the concept>"
}}

The definition must be standalone and accurate. JSON only, no fences.
"""


logger = logging.getLogger(__name__)


# ============================================================================
# Schema
# ============================================================================

class DefinitionResponse(BaseModel):
    definition: str = Field(..., min_length=10, max_length=600)

    @field_validator("definition")
    @classmethod
    def _no_placeholder(cls, v: str) -> str:
        v = v.strip()
        bad = ("definition pending", "todo", "tbd", "n/a")
        low = v.lower()
        if any(b in low for b in bad):
            raise ValueError("model returned a placeholder definition")
        if not v:
            raise ValueError("definition is empty")
        return v


# ============================================================================
# Data
# ============================================================================

@dataclass
class Candidate:
    path: Path
    title: str
    domain: str
    evidence: str  # the trimmed Core Explanation section


@dataclass
class FillResult:
    path: Path
    title: str
    ok: bool
    cached: bool = False
    error: str = ""
    new_definition: str = ""


# ============================================================================
# Scanning + extraction
# ============================================================================

def parse_frontmatter(text: str) -> tuple[dict[str, Any], str, str]:
    """Return (frontmatter dict, frontmatter raw block, body)."""
    m = _FM_RE.match(text)
    if not m:
        return {}, "", text
    raw_block = m.group(0)
    try:
        fm = yaml.safe_load(m.group(2)) or {}
        if not isinstance(fm, dict):
            return {}, "", text
    except yaml.YAMLError:
        return {}, "", text
    body = text[m.end():]
    return fm, raw_block, body


def has_placeholder(text: str) -> bool:
    return bool(_PLACEHOLDER_RE.search(text))


def extract_evidence(body: str, *, max_chars: int = 4000) -> str:
    """Pull everything between the definition callout and ## Connections.

    This captures whatever evidence sections the v3 pipeline emitted:
    Core Explanation, Practical Implications, Examples, Reflections,
    Additional Material, Methodology & Sources, etc.
    """
    m = _EVIDENCE_BLOCK_RE.search(body)
    if not m:
        return ""
    raw = m.group(1).strip()
    # Drop callout-type markers (`> [!evidence]`, `> [!example]`, etc.) for
    # prompt clarity; keep the prose underneath.
    cleaned = re.sub(r"^>\s*\[![^\]]+\][^\n]*\n", "", raw, flags=re.MULTILINE)
    cleaned = re.sub(r"^>\s?", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    if len(cleaned) > max_chars:
        cleaned = cleaned[:max_chars] + "\n[... truncated ...]"
    return cleaned


def scan_candidates(target_dir: Path) -> list[Candidate]:
    """Find all files containing the placeholder definition."""
    candidates: list[Candidate] = []
    for p in sorted(target_dir.rglob("*.md")):
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            logger.warning("Cannot read %s: %s", p, e)
            continue
        if not has_placeholder(text):
            continue
        fm, _, body = parse_frontmatter(text)
        title = str(fm.get("title", p.stem)).strip()
        domain = str(fm.get("domain", "general")).strip() or "general"
        evidence = extract_evidence(body)
        candidates.append(Candidate(path=p, title=title, domain=domain, evidence=evidence))
    logger.info("Found %d candidates with placeholder definitions", len(candidates))
    return candidates


# ============================================================================
# LLM call
# ============================================================================

def fill_one(
    cand: Candidate,
    client: OllamaClient,
    *,
    bypass_cache: bool,
) -> FillResult:
    if not cand.evidence:
        return FillResult(
            path=cand.path, title=cand.title, ok=False,
            error="no evidence section found in body",
        )
    user = USER_PROMPT_TEMPLATE.format(
        title=cand.title,
        domain=cand.domain,
        evidence=cand.evidence,
    )
    cache_inputs = (PROMPT_CONTRACT_VERSION, client.model, cand.title,
                    cand.domain, cand.evidence)
    try:
        resp = client.chat_json(
            system=SYSTEM_PROMPT,
            user=user,
            schema=DefinitionResponse,
            cache_key_inputs=cache_inputs,
            bypass_cache=bypass_cache,
        )
    except StructuredOutputError as e:
        return FillResult(path=cand.path, title=cand.title, ok=False,
                          error=f"schema/parse failure: {e}")
    except LLMError as e:
        return FillResult(path=cand.path, title=cand.title, ok=False,
                          error=f"llm error: {e}")
    parsed: DefinitionResponse = resp.parsed  # type: ignore[assignment]
    return FillResult(
        path=cand.path, title=cand.title, ok=True,
        cached=resp.cached, new_definition=parsed.definition.strip(),
    )


# ============================================================================
# Patching
# ============================================================================

def _patch_body(body: str, definition: str) -> str:
    """Replace the placeholder line with the new definition (single line)."""
    one_line = re.sub(r"\s+", " ", definition).strip()
    return _PLACEHOLDER_RE.sub(
        lambda m: f"{m.group(1)}> {one_line}\n",
        body,
        count=1,
    )


def _stamp_frontmatter(fm: dict[str, Any], model: str) -> dict[str, Any]:
    out = dict(fm)
    prov = out.get("provenance")
    if not isinstance(prov, dict):
        prov = {}
    prov["definition-source"] = "llm-filled"
    prov["definition-model"] = model
    prov["definition-filled-at"] = date.today().isoformat()
    out["provenance"] = prov
    return out


def write_patched(path: Path, definition: str, *, model: str) -> None:
    text = path.read_text(encoding="utf-8")
    fm, fm_block, body = parse_frontmatter(text)
    if not fm_block:
        logger.warning("No frontmatter in %s, writing body-only patch", path)
        new_text = _patch_body(text, definition)
    else:
        new_fm = _stamp_frontmatter(fm, model)
        new_fm_yaml = yaml.safe_dump(new_fm, sort_keys=False, allow_unicode=True,
                                     default_flow_style=False, width=120)
        new_body = _patch_body(body, definition)
        new_text = f"---\n{new_fm_yaml}---\n{new_body}"
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(new_text, encoding="utf-8")
    tmp.replace(path)


# ============================================================================
# Orchestration
# ============================================================================

def run(
    target_dir: Path,
    *,
    model: str,
    cache_dir: Path,
    limit: int | None,
    dry_run: bool,
    bypass_cache: bool,
) -> tuple[list[FillResult], dict[str, int]]:
    candidates = scan_candidates(target_dir)
    if limit is not None:
        candidates = candidates[:limit]

    results: list[FillResult] = []
    stats: dict[str, int] = {
        "candidates": len(candidates), "ok": 0, "cached": 0,
        "failed": 0, "no_evidence": 0,
    }
    if not candidates:
        return results, stats

    cache_dir.mkdir(parents=True, exist_ok=True)
    with OllamaClient(model=model, url=config_v3.OLLAMA_URL,
                      cache_dir=cache_dir) as client:
        if not client.ping():
            raise OllamaUnavailableError(f"Ollama not responding at {config_v3.OLLAMA_URL}")
        logger.info("Ollama OK; model=%s; %d candidates",
                    model, len(candidates))
        for i, cand in enumerate(candidates, 1):
            res = fill_one(cand, client, bypass_cache=bypass_cache)
            results.append(res)
            if res.ok:
                stats["ok"] += 1
                if res.cached:
                    stats["cached"] += 1
                if not dry_run:
                    try:
                        write_patched(cand.path, res.new_definition, model=model)
                    except OSError as e:
                        logger.error("Write failed for %s: %s", cand.path, e)
                        res.ok = False
                        res.error = f"write failed: {e}"
                        stats["ok"] -= 1
                        stats["failed"] += 1
            else:
                stats["failed"] += 1
                if "no evidence" in res.error:
                    stats["no_evidence"] += 1
            if i % 25 == 0 or i == len(candidates):
                logger.info("Progress: %d/%d (ok=%d, cached=%d, failed=%d)",
                            i, len(candidates), stats["ok"], stats["cached"],
                            stats["failed"])
    return results, stats


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="fill_definitions",
        description=(
            "LLM-fill the *Definition pending* placeholder in migrated "
            "vault notes. Surgical: touches only the definition line and "
            "the provenance block."
        ),
        epilog=(
            "Examples:\n"
            "  python fill_definitions.py --dry-run --limit 3\n"
            "      Run 3 LLM calls, preview only.\n"
            "  python fill_definitions.py --limit 50\n"
            "      Patch first 50 placeholder files in place.\n"
            "  python fill_definitions.py\n"
            "      Patch all placeholder files in place.\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--target-dir", type=Path, default=DEFAULT_TARGET_DIR,
                   help=f"Directory to scan (default: {DEFAULT_TARGET_DIR}).")
    p.add_argument("--model", default=config_v3.LLM_MODEL_SYNTHESIZE,
                   help=f"Ollama model (default: {config_v3.LLM_MODEL_SYNTHESIZE}).")
    p.add_argument("--cache-dir", type=Path, default=DEFAULT_LLM_CACHE_DIR,
                   help=f"LLM response cache dir (default: {DEFAULT_LLM_CACHE_DIR}).")
    p.add_argument("--limit", type=int, default=None, metavar="N",
                   help="Process only the first N candidates.")
    p.add_argument("-n", "--dry-run", action="store_true",
                   help="Run LLM calls + cache writes, but do not modify files.")
    p.add_argument("--bypass-cache", action="store_true",
                   help="Force live LLM calls; ignore cached responses.")
    p.add_argument("--strict", action="store_true",
                   help="Exit non-zero if any fill fails.")
    p.add_argument("-v", "--verbose", action="count", default=0)
    p.add_argument("-q", "--quiet", action="store_true")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return p


def configure_logging(verbosity: int, quiet: bool) -> None:
    if quiet:
        level = logging.ERROR
    elif verbosity >= 2:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(level=level,
                        format="%(asctime)s [%(levelname)s] %(message)s",
                        datefmt="%H:%M:%S")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    if not args.target_dir.is_dir():
        logger.error("Target directory not found: %s", args.target_dir)
        return 2

    try:
        results, stats = run(
            args.target_dir, model=args.model, cache_dir=args.cache_dir,
            limit=args.limit, dry_run=args.dry_run, bypass_cache=args.bypass_cache,
        )
    except OllamaUnavailableError as e:
        logger.error("Ollama unavailable: %s", e)
        logger.error("Hint: start Ollama (`ollama serve`) and confirm the "
                     "model is pulled: `ollama pull %s`", args.model)
        return 6
    except KeyboardInterrupt:
        logger.warning("Interrupted")
        return 130
    except Exception:  # noqa: BLE001
        logger.exception("Unexpected error")
        return 1

    if stats["candidates"] == 0:
        logger.warning("No placeholder definitions found in %s", args.target_dir)
        return 4

    print()
    print("=" * 64)
    tag = "  (DRY-RUN -- no files modified)" if args.dry_run else ""
    print(f"  DEFINITION-FILL SUMMARY{tag}")
    print("=" * 64)
    print(f"  Candidates scanned:     {stats['candidates']:>5}")
    print(f"  Successfully filled:    {stats['ok']:>5}")
    print(f"    of which cached:      {stats['cached']:>5}")
    print(f"  Failed:                 {stats['failed']:>5}")
    print(f"    no evidence in body:  {stats['no_evidence']:>5}")
    print(f"  Model:                  {args.model}")
    print(f"  Cache dir:              {args.cache_dir}")
    print("=" * 64)

    # Show a sample on dry-run for sanity-check
    if args.dry_run and results:
        ok = [r for r in results if r.ok][:3]
        if ok:
            print("\n  Sample definitions (first 3 OK):")
            for r in ok:
                print(f"\n  [{r.title}]")
                print(f"  -> {r.new_definition}")
            print()

    if args.strict and stats["failed"] > 0:
        return 5
    return 0


if __name__ == "__main__":
    sys.exit(main())
