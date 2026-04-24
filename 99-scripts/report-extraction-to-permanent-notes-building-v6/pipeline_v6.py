#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pipeline_v6 — Two-pass elaborated permanent-note pipeline.

V6 layers on top of V4 (bundle mining) and reuses V3 LLM client + markdown
helpers, but replaces V4's single-pass condensation with a two-pass
(outline → elaborate) flow that produces materially richer notes:

  - Definition callout with elaborated body + Falls-under [[Parent]]
  - Core Explanation as 4-6 narrative paragraphs (prose, not bullets)
  - Mechanism, Practical Implications, Key Distinctions
  - Key Figures, Open Questions, Synthesis, Evidence narrative
  - Connections & Context block grouped by relation type

Default output dir is a NEW subdirectory:

    999-report-organizing/_permanent-notes/v6-llm-elaborated/

so V6 does not collide with V3/V4/V5 outputs.

Examples:
    pipeline_v6.py --report self-determination-theory --limit 2 --dry-run
        Plan + elaborate two concepts from one report; preview only.

    pipeline_v6.py --report cognitive-load-theory
        Real run; write enriched notes to v6 output dir.

    pipeline_v6.py --no-gate --bypass-cache --report sdt
        Force live LLM calls and run elaboration even on unworthy concepts.

Version:
    1.0.0
Python:
    >=3.10
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# ── sys.path injection: V3, V4, then V6 itself (LIFO insert order) ──────
_HERE = Path(__file__).resolve().parent
_V4_DIR = _HERE.parent / "report-extraction-to-permanent-notes-building-v4"
_V3_DIR = _HERE.parent / "report-extraction-to-permanent-notes-building-v3"
for _p in (_V3_DIR, _V4_DIR, _HERE):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

# ── Reused infrastructure ───────────────────────────────────────────────
import config_v3                                              # noqa: E402
import pipeline_v4                                            # noqa: E402
from lib.llm_client import (                                  # noqa: E402
    LLMError,
    OllamaClient,
    OllamaUnavailableError,
    StructuredOutputError,
)

# ── V6 lib ──────────────────────────────────────────────────────────────
from v6lib import elaborator, prompts, renderer               # noqa: E402

# ── Optional: rich progress ─────────────────────────────────────────────
try:
    from rich.progress import (
        BarColumn, MofNCompleteColumn, Progress, SpinnerColumn,
        TextColumn, TimeElapsedColumn,
    )
    _RICH_AVAILABLE = True
except ImportError:  # pragma: no cover
    Progress = None  # type: ignore[assignment,misc]
    _RICH_AVAILABLE = False

logger = logging.getLogger(__name__)
__version__ = "1.0.0"


# ════════════════════════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════════════════════════

DEFAULT_INPUT_DIR: Path = pipeline_v4.DEFAULT_INPUT_DIR
DEFAULT_OUTPUT_DIR: Path = (
    config_v3.VAULT_ROOT
    / "999-report-organizing"
    / "_permanent-notes"
    / "v6-llm-elaborated"
)


# ════════════════════════════════════════════════════════════════════════════
# Result aggregation
# ════════════════════════════════════════════════════════════════════════════

@dataclass
class V6Result:
    """One bundle's outcome."""
    bundle: Any
    ok: bool = True
    written_path: Path | None = None
    cached: bool = False
    skipped_reason: str = ""
    unworthy_reason: str = ""
    error: str = ""


@dataclass
class V6Stats:
    """Aggregate counters."""
    jsons: int = 0
    concepts: int = 0
    written: int = 0
    skipped: int = 0
    unworthy: int = 0
    failed: int = 0
    cached: int = 0


# ════════════════════════════════════════════════════════════════════════════
# Per-bundle execution
# ════════════════════════════════════════════════════════════════════════════

def convert_one_v6(
    bundle: Any,
    client: OllamaClient,
    output_dir: Path,
    *,
    model: str,
    mode: str,
    dry_run: bool,
    bypass_cache: bool,
    today: dt.date,
    no_gate: bool,
) -> V6Result:
    """Run two-pass elaboration + render + atomic write for one bundle.

    Args:
        bundle: V4 ``ConceptBundle``.
        client: Open ``OllamaClient``.
        output_dir: Target directory for the rendered note.
        model: Ollama model name.
        mode: Collision policy — ``"skip"`` or ``"overwrite"``.
        dry_run: When True, run LLM calls (cached) but never write.
        bypass_cache: Force live LLM calls.
        today: Date stamp for frontmatter.
        no_gate: Disable LLM worthiness gate (run Pass B regardless).

    Returns:
        :class:`V6Result`.
    """
    dest = output_dir / f"{bundle.filename_stem}.md"

    # Collision check (V6's NEW route is a fresh-write — no merge here).
    if dest.exists() and not dry_run:
        if mode == "skip":
            return V6Result(
                bundle=bundle, ok=True, written_path=None,
                skipped_reason=f"file exists at {dest.name}",
            )
        # mode == 'overwrite' falls through

    # ── Two-pass LLM ────────────────────────────────────────────────────
    try:
        result = elaborator.elaborate_concept(
            bundle, client, model=model,
            bypass_cache=bypass_cache, no_gate=no_gate,
        )
    except (StructuredOutputError, LLMError) as e:
        return V6Result(
            bundle=bundle, ok=False,
            error=f"{type(e).__name__}: {e}",
        )

    if not result.worthy and not no_gate:
        return V6Result(
            bundle=bundle, ok=True, cached=result.cached,
            unworthy_reason=result.worthy_reason,
            skipped_reason=f"unworthy: {result.worthy_reason or '(no reason)'}",
        )
    if result.elaborate is None:
        # Defensive: should only happen when worthy=False but no_gate=True
        # would've forced Pass B; we keep this branch in case of upstream
        # exceptions surfacing without raising.
        return V6Result(
            bundle=bundle, ok=False, cached=result.cached,
            error="elaborator returned no Pass-B response",
        )

    # ── Render ──────────────────────────────────────────────────────────
    try:
        content = renderer.render_note(
            bundle, result.outline, result.elaborate,
            today=today,
            outline_contract=prompts.OUTLINE_CONTRACT_VERSION,
            elaborate_contract=prompts.ELABORATE_CONTRACT_VERSION,
        )
    except Exception as e:  # noqa: BLE001
        return V6Result(
            bundle=bundle, ok=False, cached=result.cached,
            error=f"render error: {type(e).__name__}: {e}",
        )

    if dry_run:
        return V6Result(
            bundle=bundle, ok=True, cached=result.cached,
            written_path=dest, skipped_reason="dry-run",
        )

    # ── Write atomically (delegates to V4's helper) ─────────────────────
    try:
        pipeline_v4.write_atomic(dest, content)
    except OSError as e:
        return V6Result(
            bundle=bundle, ok=False, cached=result.cached,
            error=f"OSError: {e}",
        )

    return V6Result(
        bundle=bundle, ok=True, cached=result.cached,
        written_path=dest,
    )


# ════════════════════════════════════════════════════════════════════════════
# Batch loop
# ════════════════════════════════════════════════════════════════════════════

def process_bundles(
    bundles: list[Any],
    *,
    client: OllamaClient,
    output_dir: Path,
    model: str,
    mode: str,
    dry_run: bool,
    bypass_cache: bool,
    today: dt.date,
    no_gate: bool,
) -> tuple[list[V6Result], V6Stats]:
    """Sequentially process every bundle. Returns ``(results, stats)``."""
    results: list[V6Result] = []
    stats = V6Stats(concepts=len(bundles))

    progress_ctx = _make_progress()
    with progress_ctx as progress:
        task = progress.add_task("V6 elaborating", total=len(bundles))
        for b in bundles:
            try:
                r = convert_one_v6(
                    b, client, output_dir,
                    model=model, mode=mode, dry_run=dry_run,
                    bypass_cache=bypass_cache, today=today, no_gate=no_gate,
                )
            except KeyboardInterrupt:
                raise
            except Exception as e:  # noqa: BLE001
                r = V6Result(bundle=b, ok=False,
                             error=f"{type(e).__name__}: {e}")
                logger.exception("Unexpected error for bundle %r", b.title)

            if r.cached:
                stats.cached += 1
            if not r.ok:
                stats.failed += 1
            elif r.unworthy_reason and not no_gate:
                stats.unworthy += 1
            elif r.skipped_reason and r.skipped_reason != "dry-run":
                stats.skipped += 1
            elif r.written_path is not None:
                stats.written += 1

            results.append(r)
            progress.update(task, advance=1,
                            description=f"V6 elaborating — {b.title[:40]}")
    return results, stats


# ════════════════════════════════════════════════════════════════════════════
# UI helpers
# ════════════════════════════════════════════════════════════════════════════

def _make_progress():  # noqa: ANN202
    if _RICH_AVAILABLE:
        return Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            TimeElapsedColumn(),
            transient=False,
        )

    class _NoopProgress:
        def __enter__(self): return self
        def __exit__(self, *a, **kw): return False
        def add_task(self, description, total=None): return 0
        def update(self, *a, **kw): pass
    return _NoopProgress()


def _print_summary(stats: V6Stats) -> None:
    line = (
        f"\n=== V6 Summary ===\n"
        f"  JSONs scanned     : {stats.jsons}\n"
        f"  Concepts mined    : {stats.concepts}\n"
        f"  Written/dry-ran   : {stats.written}\n"
        f"  Skipped (collision): {stats.skipped}\n"
        f"  Unworthy (gate)   : {stats.unworthy}\n"
        f"  Failed            : {stats.failed}\n"
        f"  LLM cache hits    : {stats.cached}\n"
    )
    print(line, file=sys.stderr)


def _write_report(results: list[V6Result], path: Path) -> None:
    """Serialize per-bundle outcomes for human review."""
    payload = []
    for r in results:
        payload.append({
            "title": r.bundle.title,
            "slug": r.bundle.filename_stem,
            "report_stem": getattr(r.bundle, "report_stem", ""),
            "ok": r.ok,
            "cached": r.cached,
            "written_path": str(r.written_path) if r.written_path else None,
            "skipped_reason": r.skipped_reason,
            "unworthy_reason": r.unworthy_reason,
            "error": r.error,
        })
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    logger.info("Wrote V6 report → %s", path)


# ════════════════════════════════════════════════════════════════════════════
# CLI
# ════════════════════════════════════════════════════════════════════════════

def build_parser() -> argparse.ArgumentParser:
    """Construct the V6 CLI parser."""
    p = argparse.ArgumentParser(
        prog="pipeline_v6",
        description=(
            "V6 Two-Pass Elaborator: produces materially richer permanent "
            "notes via outline → elaborate LLM passes. Outputs to a "
            "dedicated v6 directory by default; safe to run alongside V3-V5."
        ),
        epilog=(
            "Examples:\n"
            "  pipeline_v6.py --report self-determination-theory --limit 2 --dry-run\n"
            "      Preview elaborated notes for two concepts.\n\n"
            "  pipeline_v6.py --report cognitive-load-theory\n"
            "      Real run: write enriched notes to v6 output dir.\n\n"
            "  pipeline_v6.py --bypass-cache --no-gate --report sdt\n"
            "      Force live LLM + skip worthiness gate.\n\n"
            "  pipeline_v6.py --report-runs runs/2026-04-23-v6-log.json\n"
            "      Write a JSON audit log of all per-bundle outcomes.\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--version", action="version",
                   version=f"%(prog)s {__version__}")
    p.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT_DIR,
                   help=f"Directory of *_extracted.json (default: {DEFAULT_INPUT_DIR})")
    p.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR,
                   help=f"Output dir (default: {DEFAULT_OUTPUT_DIR})")
    p.add_argument("--report", type=str, default=None,
                   help="Substring filter on JSON filename stem.")
    p.add_argument("--limit", type=int, default=None,
                   help="Process at most N concept candidates total.")
    p.add_argument("--include-key-claims", action="store_true",
                   help="Include [!key-claim] callouts as concept candidates.")

    p.add_argument("--mode", choices=("skip", "overwrite"), default="skip",
                   help=("Behavior on filename collision in the v6 output dir "
                         "(default: skip). V6 has no in-place merger yet."))

    p.add_argument("-n", "--dry-run", action="store_true",
                   help="Run LLM calls (cache them) but do not write any files.")
    p.add_argument("--bypass-cache", action="store_true",
                   help="Force live LLM calls; ignore cached responses.")
    p.add_argument("--model", type=str,
                   default=config_v3.LLM_MODEL_SYNTHESIZE,
                   help=f"Ollama model (default: {config_v3.LLM_MODEL_SYNTHESIZE}).")
    p.add_argument("--no-gate", action="store_true",
                   help="Disable LLM worthiness gate (always run Pass B).")
    p.add_argument("--report-runs", type=Path, default=None,
                   help="Write a JSON audit log of all per-bundle outcomes.")
    p.add_argument("--strict", action="store_true",
                   help="Exit non-zero on any failure.")
    p.add_argument("-v", "--verbose", action="count", default=0,
                   help="Increase logging verbosity (repeatable).")
    p.add_argument("-q", "--quiet", action="store_true",
                   help="Suppress non-error output.")
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
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
        force=True,
    )


def main(argv: list[str] | None = None) -> int:
    """V6 entry point.

    Returns:
        0   success
        1   uncaught error
        2   input dir not found
        4   no JSONs / no concepts mined
        5   strict mode + failures
        6   Ollama unreachable
        130 KeyboardInterrupt
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    # ── Discover JSONs (V4 helper) ──────────────────────────────────────
    try:
        json_paths = pipeline_v4.discover_jsons(
            args.input_dir, report_filter=args.report,
        )
    except FileNotFoundError as e:
        logger.error("%s", e); return 2
    if not json_paths:
        logger.error("No *_extracted.json under %s (filter=%r)",
                     args.input_dir, args.report)
        return 4
    logger.info("Discovered %d JSON file(s)", len(json_paths))

    # ── Build bundles (V4 helper) ───────────────────────────────────────
    bundles: list[Any] = []
    for jp in json_paths:
        try:
            payload = pipeline_v4.load_payload(jp)
        except (OSError, json.JSONDecodeError, ValueError) as e:
            logger.warning("Skip %s: %s", jp.name, e)
            continue
        report_stem = jp.stem.removesuffix("_extracted")
        bundles.extend(pipeline_v4.build_bundles(
            payload, report_stem=report_stem,
            include_key_claims=args.include_key_claims,
        ))
        if args.limit and len(bundles) >= args.limit:
            bundles = bundles[: args.limit]
            break

    if not bundles:
        logger.error("No concept candidates mined.")
        return 4
    logger.info("Mined %d concept candidate(s)", len(bundles))

    args.output_dir.mkdir(parents=True, exist_ok=True)
    config_v3.LLM_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    today = dt.date.today()

    # ── Run with shared LLM client ──────────────────────────────────────
    try:
        with OllamaClient(
            model=args.model,
            url=config_v3.OLLAMA_URL,
            cache_dir=config_v3.LLM_CACHE_DIR,
            timeout_s=config_v3.LLM_REQUEST_TIMEOUT_S,
            max_retries=config_v3.LLM_MAX_RETRIES,
        ) as client:
            try:
                results, stats = process_bundles(
                    bundles,
                    client=client,
                    output_dir=args.output_dir,
                    model=args.model,
                    mode=args.mode,
                    dry_run=args.dry_run,
                    bypass_cache=args.bypass_cache,
                    today=today,
                    no_gate=args.no_gate,
                )
            except OllamaUnavailableError as e:
                logger.error("Ollama unreachable mid-run: %s", e); return 6
    except OllamaUnavailableError as e:
        logger.error("Ollama unreachable on startup: %s", e); return 6
    except KeyboardInterrupt:
        logger.warning("Interrupted by user"); return 130

    stats.jsons = len(json_paths)
    _print_summary(stats)

    if args.report_runs:
        try:
            _write_report(results, args.report_runs)
        except OSError as e:
            logger.warning("Could not write run report: %s", e)

    if args.strict and stats.failed > 0:
        return 5
    return 0


# ════════════════════════════════════════════════════════════════════════════
# Entry-point guard
# ════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    sys.exit(main())
