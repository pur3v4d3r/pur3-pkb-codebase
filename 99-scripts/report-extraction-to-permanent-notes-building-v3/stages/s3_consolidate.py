#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""s3_consolidate.py — Stage 3: cross-batch candidate consolidation.

Reads every ``_validated.json`` produced by Stage 2, extracts one
:class:`lib.candidate.Candidate` per titled callout, then groups by
:func:`lib.candidate.normalize_name` and merges. The result is one Candidate
per concept across the entire corpus, with full provenance preserved.

Output (one JSON file):
    ``<output-dir>/_consolidated-candidates.json``

The output JSON shape::

    {
      "version": "1.0.0",
      "stats": {
        "files_read": N,
        "raw_candidates": M,
        "consolidated_candidates": K,
        "merge_compression_ratio": M / K,
        "evidence_items_total": ...,
        "evidence_loss_checksum": "OK" | "MISMATCH"
      },
      "candidates": [<Candidate.to_dict()>, ...]
    }

Phase 2 gate (spec §5 Phase 2):
    1. Run on full corpus → output produced with K << M
    2. Zero evidence loss: every (concept, evidence-body) pair from the
       source ``_validated.json`` files appears in the consolidated output.
       This module computes and embeds the checksum result in the stats block.

Usage:
    python -m stages.s3_consolidate <input-dir>
    python -m stages.s3_consolidate <input-dir> -o _v3-output/run-001
    python -m stages.s3_consolidate <input-dir> --dry-run -v

Exit codes:
    0   success
    1   uncaught error
    2   input path missing or unreadable
    3   write permission denied
    4   no validated files found
    5   evidence-loss checksum mismatch (gate failure)
    130 interrupted (SIGINT)

Spec: §3.1 (Candidate), §5 Phase 2 (consolidation).
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# ── sys.path injection so `python -m stages.s3_consolidate` and pytest
#    both resolve the sibling `lib/` package without packaging fuss.
_HERE = Path(__file__).resolve().parent
_V3_ROOT = _HERE.parent
if str(_V3_ROOT) not in sys.path:
    sys.path.insert(0, str(_V3_ROOT))

from lib.candidate import (  # noqa: E402
    BUCKET_FIELDS,
    Candidate,
    DEFAULT_COMPLEXITY,
    DEFAULT_CONFIDENCE,
    DEFAULT_DOMAIN,
    DEFAULT_IMPORTANCE,
    EvidenceItem,
    SourceReport,
    normalize_name,
)


__version__ = "1.0.0"

#: Glob pattern for Stage-2 outputs.
VALIDATED_GLOB = "*_validated.json"

#: Default output filename written into ``--output-dir``.
OUTPUT_FILENAME = "_consolidated-candidates.json"

logger = logging.getLogger(__name__)


# ════════════════════════════════════════════════════════════════════════════
# Custom exceptions
# ════════════════════════════════════════════════════════════════════════════

class ConsolidateError(Exception):
    """Base exception for s3_consolidate-specific errors."""


class EvidenceLossError(ConsolidateError):
    """Raised when the evidence-loss checksum does not match (gate failure)."""


# ════════════════════════════════════════════════════════════════════════════
# Pure functions
# ════════════════════════════════════════════════════════════════════════════

def _frontmatter_meta(payload: dict[str, Any]) -> dict[str, Any]:
    """Extract scalar metadata fields from a validated payload's frontmatter.

    Returns a dict with keys: domain, subdomains, confidence, complexity,
    importance — using safe defaults for missing keys.
    """
    fm = payload.get("document_metadata", {}).get("frontmatter", {}) or {}
    domain = fm.get("primary_domain") or fm.get("domain") or DEFAULT_DOMAIN

    sub_raw = fm.get("secondary_domains") or fm.get("subdomains") or ()
    if isinstance(sub_raw, str):
        subdomains: tuple[str, ...] = (sub_raw,)
    elif isinstance(sub_raw, (list, tuple)):
        subdomains = tuple(str(x) for x in sub_raw if x)
    else:
        subdomains = ()

    confidence = fm.get("confidence") or DEFAULT_CONFIDENCE
    complexity = fm.get("complexity") or fm.get("knowledge_level") or DEFAULT_COMPLEXITY
    importance = fm.get("importance") or DEFAULT_IMPORTANCE

    return {
        "domain": str(domain),
        "subdomains": subdomains,
        "confidence": confidence,
        "complexity": complexity,
        "importance": importance,
    }


def _wiki_link_targets(payload: dict[str, Any]) -> tuple[str, ...]:
    """Collect the validated wiki-link targets from a payload's body."""
    items = payload.get("extracted_items") or payload.get("extracted_content") or {}
    wikis = items.get("wiki_links") if isinstance(items, dict) else None
    if not isinstance(wikis, list):
        return ()
    targets = [str(w.get("target", "")).strip() for w in wikis if isinstance(w, dict)]
    return tuple(t for t in targets if t)


def candidates_from_validated(
    payload: dict[str, Any],
    *,
    batch: str,
    file: str,
) -> list[Candidate]:
    """Build one :class:`Candidate` per titled callout in a validated payload.

    Untitled callouts are skipped (they cannot be grouped). Empty-body callouts
    are kept (the title alone may carry signal). Noise titles ("Untitled",
    "Title not specified") and titles consisting solely of markdown header
    syntax are also skipped — these are extractor artifacts that pollute the
    grouping space.
    """
    items = payload.get("extracted_items") or payload.get("extracted_content") or {}
    callouts = items.get("callouts") if isinstance(items, dict) else None
    if not isinstance(callouts, list):
        return []

    meta = _frontmatter_meta(payload)
    wiki_targets = _wiki_link_targets(payload)

    out: list[Candidate] = []
    for c in callouts:
        if not isinstance(c, dict):
            continue
        title = _clean_title(str(c.get("title", "")))
        if not title:
            continue
        # Push the cleaned title back so downstream stages see it.
        c = dict(c)
        c["title"] = title
        source = SourceReport(
            batch=batch, file=file, line=int(c.get("line_number", 0) or 0),
        )
        cand = Candidate.from_callout(
            c,
            source,
            domain=meta["domain"],
            subdomains=meta["subdomains"],
            confidence=meta["confidence"],
            complexity=meta["complexity"],
            importance=meta["importance"],
            wiki_links_seen=wiki_targets,
        )
        out.append(cand)
    return out


#: Titles that signal an extractor artifact and should never become a Candidate.
_NOISE_TITLES: frozenset[str] = frozenset({
    "untitled", "title not specified", "no title", "n/a", "none",
})

#: Strip leading markdown header markers and surrounding whitespace from a title.
_HEADER_PREFIX_RE = re.compile(r"^\s*#{1,6}\s+")

#: Match a wiki-link of the form ``[[target|display]]`` or ``[[target]]``.
#: Group 1 = target slug; group 2 = display text (may be empty).
_WIKI_LINK_RE = re.compile(r"\[\[([^\[\]|]+?)(?:\|([^\[\]]+?))?\]\]")


def _strip_wiki_links(text: str) -> str:
    """Replace ``[[target|display]]`` with ``display`` (or ``target`` if no display).

    Also removes any stray unmatched ``[[`` or ``]]`` markers so that
    downstream filename construction never sees wiki-link syntax.
    """
    if "[[" not in text and "]]" not in text:
        return text
    replaced = _WIKI_LINK_RE.sub(lambda m: (m.group(2) or m.group(1)).strip(), text)
    # Defensive: kill any orphan markers left behind by malformed input.
    return replaced.replace("[[", "").replace("]]", "")


def _clean_title(title: str) -> str:
    """Normalize a callout title; return ``""`` if it is noise."""
    cleaned = _HEADER_PREFIX_RE.sub("", title or "").strip()
    cleaned = _strip_wiki_links(cleaned).strip()
    if not cleaned:
        return ""
    if cleaned.casefold() in _NOISE_TITLES:
        return ""
    return cleaned


def consolidate(candidates: Iterable[Candidate]) -> list[Candidate]:
    """Group ``candidates`` by ``grouping_key`` and merge each group.

    Groups are emitted in deterministic alphabetical order of the grouping
    key; merge order within a group is the input order.
    """
    groups: dict[str, Candidate] = {}
    for cand in candidates:
        key = cand.grouping_key
        if not key:
            continue
        existing = groups.get(key)
        groups[key] = cand if existing is None else existing.merge(cand)
    return [groups[k] for k in sorted(groups)]


# ════════════════════════════════════════════════════════════════════════════
# Evidence-loss checksum (Phase 2 gate)
# ════════════════════════════════════════════════════════════════════════════

def evidence_signature(items: Iterable[EvidenceItem]) -> Counter[tuple[str, str]]:
    """Return a multiset of ``(concept_grouping_key, body)`` pairs.

    Two consolidations with identical signatures lost no evidence content.
    """
    sig: Counter[tuple[str, str]] = Counter()
    for it in items:
        sig[(normalize_name(it.title), it.body)] += 1
    return sig


def raw_evidence_signature(raw: Iterable[Candidate]) -> Counter[tuple[str, str]]:
    sig: Counter[tuple[str, str]] = Counter()
    for c in raw:
        for it in c.all_items():
            sig[(normalize_name(it.title), it.body)] += 1
    return sig


def consolidated_evidence_signature(
    consolidated: Iterable[Candidate],
) -> Counter[tuple[str, str]]:
    sig: Counter[tuple[str, str]] = Counter()
    for c in consolidated:
        for it in c.all_items():
            sig[(normalize_name(it.title), it.body)] += 1
    return sig


# ════════════════════════════════════════════════════════════════════════════
# I/O layer
# ════════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class DiscoveredFile:
    """A validated input file with its inferred batch label."""
    path: Path
    batch: str
    file: str


def discover_inputs(input_path: Path) -> list[DiscoveredFile]:
    """Find every ``*_validated.json`` under ``input_path`` (file or dir)."""
    if not input_path.exists():
        raise FileNotFoundError(f"input path not found: {input_path}")
    if input_path.is_file():
        return [DiscoveredFile(
            path=input_path,
            batch=input_path.parent.name,
            file=input_path.name,
        )]
    out: list[DiscoveredFile] = []
    for p in sorted(input_path.rglob(VALIDATED_GLOB)):
        out.append(DiscoveredFile(path=p, batch=p.parent.name, file=p.name))
    return out


def load_validated(path: Path) -> dict[str, Any]:
    """Load and JSON-parse a validated payload."""
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def write_output(
    candidates: list[Candidate],
    stats: dict[str, Any],
    output_path: Path,
) -> None:
    """Write the consolidated-candidates JSON snapshot."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": __version__,
        "stats": stats,
        "candidates": [c.to_dict() for c in candidates],
    }
    with output_path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2, sort_keys=False)


# ════════════════════════════════════════════════════════════════════════════
# Orchestration
# ════════════════════════════════════════════════════════════════════════════

def run_consolidation(
    inputs: list[DiscoveredFile],
) -> tuple[list[Candidate], list[Candidate], dict[str, Any]]:
    """Execute the full Stage-3 pipeline against discovered inputs.

    Returns:
        (raw_candidates, consolidated, stats)

    Raises:
        EvidenceLossError: if the pre/post evidence checksum mismatches.
    """
    raw: list[Candidate] = []
    for inp in inputs:
        try:
            payload = load_validated(inp.path)
        except json.JSONDecodeError as e:
            logger.error("skipping %s — invalid JSON: %s", inp.path, e)
            continue
        raw.extend(candidates_from_validated(
            payload, batch=inp.batch, file=inp.file,
        ))
    consolidated = consolidate(raw)

    raw_sig = raw_evidence_signature(raw)
    consolidated_sig = consolidated_evidence_signature(consolidated)
    checksum_ok = raw_sig == consolidated_sig

    by_bucket: Counter[str] = Counter()
    for c in consolidated:
        for bf in BUCKET_FIELDS:
            by_bucket[bf] += len(getattr(c, bf))

    stats: dict[str, Any] = {
        "files_read": len(inputs),
        "raw_candidates": len(raw),
        "consolidated_candidates": len(consolidated),
        "merge_compression_ratio": (
            round(len(raw) / len(consolidated), 3) if consolidated else 0.0
        ),
        "evidence_items_total": sum(by_bucket.values()),
        "evidence_items_by_bucket": dict(by_bucket),
        "definitions_seen": sum(1 for c in consolidated if c.definition_body),
        "evidence_loss_checksum": "OK" if checksum_ok else "MISMATCH",
    }

    if not checksum_ok:
        missing = raw_sig - consolidated_sig
        extra = consolidated_sig - raw_sig
        raise EvidenceLossError(
            f"evidence-loss checksum mismatch: "
            f"{sum(missing.values())} missing, {sum(extra.values())} extra"
        )

    return raw, consolidated, stats


# ════════════════════════════════════════════════════════════════════════════
# CLI
# ════════════════════════════════════════════════════════════════════════════

def build_parser() -> argparse.ArgumentParser:
    """Construct the Stage 3 argument parser."""
    parser = argparse.ArgumentParser(
        prog="s3_consolidate",
        description="Stage 3: cross-batch candidate consolidation.",
        epilog=(
            "Examples:\n"
            "  python -m stages.s3_consolidate _v3-output/phase-1-gate\n"
            "  python -m stages.s3_consolidate _v3-output/phase-1-gate -o _v3-output/runs/001\n"
            "  python -m stages.s3_consolidate _v3-output/phase-1-gate --dry-run -v\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("input", type=Path,
                        help="Validated-JSON file or directory to scan recursively.")
    parser.add_argument("-o", "--output-dir", type=Path, default=None,
                        help=f"Directory to write {OUTPUT_FILENAME} into "
                             f"(default: input dir).")
    parser.add_argument("-n", "--dry-run", action="store_true",
                        help="Compute everything but do not write the snapshot.")
    parser.add_argument("-v", "--verbose", action="count", default=0,
                        help="Increase logging verbosity (repeatable).")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="Suppress non-error output.")
    parser.add_argument("--version", action="version",
                        version=f"%(prog)s {__version__}")
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
        force=True,
    )


def main(argv: list[str] | None = None) -> int:
    """Stage 3 CLI entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    try:
        inputs = discover_inputs(args.input)
    except FileNotFoundError as e:
        logger.error("%s", e)
        return 2

    if not inputs:
        logger.error("no %s files found under %s", VALIDATED_GLOB, args.input)
        return 4

    logger.info("Discovered %d validated file(s)", len(inputs))

    try:
        _raw, consolidated, stats = run_consolidation(inputs)
    except EvidenceLossError as e:
        logger.error("Phase 2 gate FAILED: %s", e)
        return 5
    except KeyboardInterrupt:
        logger.warning("Interrupted")
        return 130
    except Exception:
        logger.exception("Unexpected error during consolidation")
        return 1

    logger.warning(
        "Done. files=%d  raw=%d  consolidated=%d  "
        "compression=%.2fx  evidence_items=%d  checksum=%s",
        stats["files_read"],
        stats["raw_candidates"],
        stats["consolidated_candidates"],
        stats["merge_compression_ratio"],
        stats["evidence_items_total"],
        stats["evidence_loss_checksum"],
    )
    if args.verbose:
        logger.info("Evidence by bucket:")
        for bucket, n in sorted(
            stats["evidence_items_by_bucket"].items(),
            key=lambda kv: -kv[1],
        ):
            if n:
                logger.info("  %-22s %d", bucket, n)

    if args.dry_run:
        logger.warning("dry-run: snapshot not written")
        return 0

    output_dir = args.output_dir or (
        args.input if args.input.is_dir() else args.input.parent
    )
    output_path = output_dir / OUTPUT_FILENAME

    try:
        write_output(consolidated, stats, output_path)
    except PermissionError as e:
        logger.error("Permission denied writing %s: %s", output_path, e)
        return 3

    logger.warning("Wrote %s", output_path)
    return 0


# ════════════════════════════════════════════════════════════════════════════
# Entry point
# ════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    sys.exit(main())
