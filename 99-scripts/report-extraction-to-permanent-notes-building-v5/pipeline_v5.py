#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pipeline_v5 — Merge-aware permanent-note pipeline.

V5 sits on top of V4. It uses V4's bundle-mining (``mine_concepts`` →
``build_bundles``) and V4's rendering for fresh notes, then routes each
bundle through a tiered matcher:

    - HIT  → call merger (LLM merge prompt) → write merged note in place
             (with timestamped backup).
    - MISS → V4 condense path → write new note.

Output is V4's default directory unless ``--output-dir`` overrides it.
Reconciliation is ON by default; pass ``--no-reconcile`` to fall back to
pure-V4 generate-only behavior.

Examples:
    pipeline_v5.py --report self-determination-theory --dry-run
        Preview merges + new generations for that report.

    pipeline_v5.py --report cognitive-load-theory
        Real run: merge into existing notes, generate misses fresh.

    pipeline_v5.py --no-reconcile --report metacognition
        Disable matching → behave exactly like V4 (skip-on-collision).

    pipeline_v5.py --force-merge --match-threshold 0.95 --report sdt
        Override status protection, tighter fuzzy threshold.

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
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# ── sys.path injection: V4, V3, and lib/ for V5 ─────────────────────────
_HERE = Path(__file__).resolve().parent
_V4_DIR = _HERE.parent / "report-extraction-to-permanent-notes-building-v4"
_V3_DIR = _HERE.parent / "report-extraction-to-permanent-notes-building-v3"
# Order matters: sys.path.insert(0, ...) is LIFO. Insert in reverse
# precedence order so V5's own `lib/` package is found before V3's
# (which has its own `lib/llm_client.py`, `lib/markdown.py`).
for _p in (_V3_DIR, _V4_DIR, _HERE):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

# ── V3 + V4 reused infrastructure ───────────────────────────────────────
import config_v3  # noqa: E402
import pipeline_v4  # noqa: E402
from lib.llm_client import (  # noqa: E402
    LLMError,
    OllamaClient,
    OllamaUnavailableError,
)

# ── V5 lib (own modules) ────────────────────────────────────────────────
from v5lib.matcher import (  # noqa: E402
    DEFAULT_THRESHOLD,
    AmbiguousMatchError,
    Matcher,
    MatchResult,
)
from v5lib.merger import Merger, MergeOutcome  # noqa: E402
from v5lib.output_index import OutputIndex  # noqa: E402

# ── Optional: rich progress (already available via V4) ──────────────────
try:
    from rich.console import Console
    from rich.progress import (
        BarColumn, MofNCompleteColumn, Progress, SpinnerColumn,
        TextColumn, TimeElapsedColumn,
    )
    _RICH_AVAILABLE = True
except ImportError:  # pragma: no cover
    Console = None  # type: ignore[assignment,misc]
    Progress = None  # type: ignore[assignment,misc]
    _RICH_AVAILABLE = False

logger = logging.getLogger(__name__)
__version__ = "1.0.0"


# ════════════════════════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════════════════════════

#: Default protect-statuses (these block merge unless --force-merge).
DEFAULT_PROTECT_STATUSES: frozenset[str] = frozenset({"evergreen", "budding"})

#: Default output dir mirrors V4's.
DEFAULT_OUTPUT_DIR: Path = pipeline_v4.DEFAULT_OUTPUT_DIR
DEFAULT_INPUT_DIR: Path = pipeline_v4.DEFAULT_INPUT_DIR


# ════════════════════════════════════════════════════════════════════════════
# Result aggregation
# ════════════════════════════════════════════════════════════════════════════

@dataclass
class V5Result:
    """One bundle's outcome — either a merge or a fresh-generate."""
    bundle: Any                                    # ConceptBundle
    route: str                                     # 'merge' | 'new' | 'ambiguous' | 'failed-pre-route'
    match: MatchResult | None = None
    merge_outcome: MergeOutcome | None = None
    convert_result: Any | None = None              # pipeline_v4.ConvertResult
    error: str = ""


@dataclass
class V5Stats:
    """Aggregate counters over a run."""
    jsons: int = 0
    concepts: int = 0
    routed_merge: int = 0
    routed_new: int = 0
    merged_written: int = 0
    merged_skipped: int = 0
    merged_failed: int = 0
    new_written: int = 0
    new_skipped: int = 0
    new_unworthy: int = 0
    new_failed: int = 0
    ambiguous: int = 0
    cached: int = 0


# ════════════════════════════════════════════════════════════════════════════
# Routing
# ════════════════════════════════════════════════════════════════════════════

def route_bundle(
    bundle: Any,
    matcher: Matcher,
) -> tuple[str, MatchResult | None, str]:
    """Decide whether a bundle should be merged or generated fresh.

    Returns:
        Tuple ``(route, match_or_none, error_or_empty)`` where:
          - route in {"merge", "new", "ambiguous"}
          - match is the :class:`MatchResult` for "merge", else None
          - error is set when route == "ambiguous"
    """
    try:
        match = matcher.find(bundle.title, bundle.filename_stem)
    except AmbiguousMatchError as e:
        return "ambiguous", None, str(e)
    if match is None:
        return "new", None, ""
    return "merge", match, ""


def process_bundles(
    bundles: list[Any],
    *,
    matcher: Matcher,
    merger: Merger,
    client: OllamaClient,
    output_dir: Path,
    model: str,
    new_mode: str,
    dry_run: bool,
    bypass_cache: bool,
    today: dt.date,
    no_gate: bool,
    reconcile: bool,
) -> tuple[list[V5Result], V5Stats]:
    """Sequentially route + execute each bundle. Return results + stats."""
    results: list[V5Result] = []
    stats = V5Stats(concepts=len(bundles))

    progress_ctx = _make_progress()
    with progress_ctx as progress:
        task = progress.add_task("V5 reconciling", total=len(bundles))
        for b in bundles:
            # ── Route ──────────────────────────────────────────────────
            if reconcile:
                route, match, route_err = route_bundle(b, matcher)
            else:
                route, match, route_err = "new", None, ""

            r = V5Result(bundle=b, route=route, match=match)

            if route == "ambiguous":
                stats.ambiguous += 1
                r.error = route_err
                logger.warning("Ambiguous match for %r: %s", b.title, route_err)
                results.append(r)
                progress.update(task, advance=1,
                                description=f"V5 reconciling — {b.title[:40]}")
                continue

            # ── Execute ────────────────────────────────────────────────
            try:
                if route == "merge":
                    stats.routed_merge += 1
                    assert match is not None
                    outcome = merger.merge(
                        bundle=b, match=match, today=today, dry_run=dry_run,
                    )
                    r.merge_outcome = outcome
                    if outcome.cached:
                        stats.cached += 1
                    if not outcome.ok:
                        stats.merged_failed += 1
                    elif outcome.skipped:
                        stats.merged_skipped += 1
                    elif dry_run:
                        # dry-run counts as "would write" — bucket as written
                        stats.merged_written += 1
                    else:
                        stats.merged_written += 1
                else:  # route == "new"
                    stats.routed_new += 1
                    cv = pipeline_v4.convert_one(
                        b, client, output_dir,
                        model=model, mode=new_mode, dry_run=dry_run,
                        bypass_cache=bypass_cache, today=today,
                        no_gate=no_gate,
                    )
                    r.convert_result = cv
                    if cv.cached:
                        stats.cached += 1
                    if not cv.ok:
                        stats.new_failed += 1
                    elif cv.unworthy_reason and not no_gate:
                        stats.new_unworthy += 1
                    elif cv.skipped_reason and cv.skipped_reason != "dry-run":
                        stats.new_skipped += 1
                    elif cv.written_path is not None:
                        stats.new_written += 1
            except KeyboardInterrupt:
                raise
            except Exception as e:  # noqa: BLE001
                r.error = f"{type(e).__name__}: {e}"
                if route == "merge":
                    stats.merged_failed += 1
                else:
                    stats.new_failed += 1
                logger.exception("Unexpected error for bundle %r", b.title)

            results.append(r)
            progress.update(task, advance=1,
                            description=f"V5 reconciling — {b.title[:40]}")
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


def _print_summary(stats: V5Stats) -> None:
    """Print a compact run summary to stderr."""
    line = (
        f"\n=== V5 Summary ===\n"
        f"  JSONs scanned     : {stats.jsons}\n"
        f"  Concepts mined    : {stats.concepts}\n"
        f"  Routed → MERGE    : {stats.routed_merge}\n"
        f"    written/dry-ran : {stats.merged_written}\n"
        f"    skipped (protect): {stats.merged_skipped}\n"
        f"    failed          : {stats.merged_failed}\n"
        f"  Routed → NEW      : {stats.routed_new}\n"
        f"    written/dry-ran : {stats.new_written}\n"
        f"    skipped         : {stats.new_skipped}\n"
        f"    unworthy (gate) : {stats.new_unworthy}\n"
        f"    failed          : {stats.new_failed}\n"
        f"  Ambiguous matches : {stats.ambiguous}\n"
        f"  LLM cache hits    : {stats.cached}\n"
    )
    print(line, file=sys.stderr)


def _write_report(results: list[V5Result], path: Path) -> None:
    """Serialize results to JSON for human review."""
    payload = []
    for r in results:
        item: dict[str, Any] = {
            "title": r.bundle.title,
            "slug": r.bundle.filename_stem,
            "report_stem": getattr(r.bundle, "report_stem", ""),
            "route": r.route,
            "error": r.error,
        }
        if r.match is not None:
            item["match"] = {
                "path": str(r.match.path),
                "tier": r.match.tier,
                "score": r.match.score,
                "matched_against": r.match.matched_against,
            }
        if r.merge_outcome is not None:
            mo = r.merge_outcome
            item["merge_outcome"] = {
                "ok": mo.ok,
                "skipped": mo.skipped,
                "skipped_reason": mo.skipped_reason,
                "backup_path": str(mo.backup_path) if mo.backup_path else None,
                "change_summary": mo.change_summary,
                "cached": mo.cached,
                "error": mo.error,
            }
        if r.convert_result is not None:
            cv = r.convert_result
            item["convert_result"] = {
                "ok": cv.ok,
                "cached": cv.cached,
                "written_path": str(cv.written_path) if cv.written_path else None,
                "skipped_reason": cv.skipped_reason,
                "unworthy_reason": cv.unworthy_reason,
                "error": cv.error,
            }
        payload.append(item)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    logger.info("Wrote merge report → %s", path)


# ════════════════════════════════════════════════════════════════════════════
# CLI
# ════════════════════════════════════════════════════════════════════════════

def _parse_protect_set(arg: str) -> frozenset[str]:
    return frozenset(s.strip().lower() for s in arg.split(",") if s.strip())


def build_parser() -> argparse.ArgumentParser:
    """Construct the V5 CLI parser."""
    p = argparse.ArgumentParser(
        prog="pipeline_v5",
        description=(
            "V5 Reconciler: merge-aware permanent-note pipeline. "
            "For each concept, either merge into the existing note or "
            "generate fresh via V4. Reconciliation is ON by default."
        ),
        epilog=(
            "Examples:\n"
            "  pipeline_v5.py --report self-determination-theory --dry-run\n"
            "      Preview routing + merges for one report.\n\n"
            "  pipeline_v5.py --report cognitive-load-theory\n"
            "      Real run: merge hits, generate misses.\n\n"
            "  pipeline_v5.py --no-reconcile\n"
            "      Disable V5 routing; behave like pure V4 (skip on collision).\n\n"
            "  pipeline_v5.py --force-merge --match-threshold 0.95\n"
            "      Override status protection; tighter fuzzy threshold.\n\n"
            "  pipeline_v5.py --report-merges runs/2026-04-23-merge-log.json\n"
            "      Write a JSON audit log of every routing decision.\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    p.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT_DIR,
                   help=f"Directory of *_extracted.json files (default: {DEFAULT_INPUT_DIR})")
    p.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR,
                   help=f"Output dir (default: {DEFAULT_OUTPUT_DIR})")
    p.add_argument("--report", type=str, default=None,
                   help="Substring filter on JSON filename stem.")
    p.add_argument("--limit", type=int, default=None,
                   help="Process at most N concept candidates total.")
    p.add_argument("--include-key-claims", action="store_true",
                   help="Include [!key-claim] callouts as concept candidates.")

    # ── V5-specific ──────────────────────────────────────────────────────
    rg = p.add_mutually_exclusive_group()
    rg.add_argument("--reconcile", dest="reconcile", action="store_true",
                    default=True, help="Enable V5 merge routing (default: on).")
    rg.add_argument("--no-reconcile", dest="reconcile", action="store_false",
                    help="Disable V5; behave like pure V4 generate-only.")
    p.add_argument("--match-threshold", type=float, default=DEFAULT_THRESHOLD,
                   help=f"Fuzzy match threshold 0..1 (default: {DEFAULT_THRESHOLD}).")
    p.add_argument("--protect-statuses", type=str,
                   default="evergreen,budding",
                   help=("Comma-separated statuses that block merge unless "
                         "--force-merge (default: evergreen,budding)."))
    p.add_argument("--force-merge", action="store_true",
                   help="Override --protect-statuses; merge even into protected notes.")
    p.add_argument("--no-backup", action="store_true",
                   help="Skip creating a .bak.<timestamp> sibling before merging.")
    p.add_argument("--report-merges", type=Path, default=None,
                   help="Write a JSON audit log of all routing decisions to this path.")

    # ── V4 collision mode (only used for the NEW route) ──────────────────
    p.add_argument("--new-mode", choices=("skip", "overwrite"), default="skip",
                   help=("Behavior for the NEW route when an output file with "
                         "that slug somehow exists (rare — would imply matcher "
                         "miss + filename collision). Default: skip."))

    # ── Standard ─────────────────────────────────────────────────────────
    p.add_argument("-n", "--dry-run", action="store_true",
                   help="Run LLM calls (cache them) but do not write any files.")
    p.add_argument("--bypass-cache", action="store_true",
                   help="Force live LLM calls; ignore cached responses.")
    p.add_argument("--model", type=str, default=config_v3.LLM_MODEL_SYNTHESIZE,
                   help=f"Ollama model (default: {config_v3.LLM_MODEL_SYNTHESIZE}).")
    p.add_argument("--no-gate", action="store_true",
                   help="Disable LLM worthiness gate for the NEW route.")
    p.add_argument("--strict", action="store_true",
                   help="Exit non-zero on any failure.")
    p.add_argument("-v", "--verbose", action="count", default=0,
                   help="Increase logging verbosity (repeatable).")
    p.add_argument("-q", "--quiet", action="store_true",
                   help="Suppress non-error output.")
    return p


def configure_logging(verbosity: int, quiet: bool) -> None:
    """Wire up root logger from CLI flags."""
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
    """V5 entry point.

    Returns:
        Exit code:
          0  success
          1  uncaught error
          2  input dir not found
          4  no JSONs / no concepts mined
          5  strict mode + failures
          6  Ollama unreachable
          7  output dir build error
        130  KeyboardInterrupt
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    # ── Discover JSONs ─────────────────────────────────────────────────
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

    # ── Build bundles via V4 ───────────────────────────────────────────
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

    # ── Build output index ─────────────────────────────────────────────
    args.output_dir.mkdir(parents=True, exist_ok=True)
    idx = OutputIndex(output_dir=args.output_dir)
    try:
        idx.build()
    except Exception as e:  # noqa: BLE001
        logger.error("OutputIndex build failed: %s", e)
        return 7
    logger.info("Indexed %d existing note(s) in output dir", len(idx))

    matcher = Matcher(index=idx, threshold=args.match_threshold)
    protect = _parse_protect_set(args.protect_statuses)

    # ── Run pipeline with shared LLM client ────────────────────────────
    config_v3.LLM_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    today = dt.date.today()

    try:
        with OllamaClient(
            model=args.model,
            url=config_v3.OLLAMA_URL,
            cache_dir=config_v3.LLM_CACHE_DIR,
            timeout_s=config_v3.LLM_REQUEST_TIMEOUT_S,
            max_retries=config_v3.LLM_MAX_RETRIES,
        ) as client:
            merger = Merger(
                client=client,
                model=args.model,
                protect_statuses=protect,
                force=args.force_merge,
                backup=not args.no_backup,
                bypass_cache=args.bypass_cache,
            )
            try:
                results, stats = process_bundles(
                    bundles,
                    matcher=matcher,
                    merger=merger,
                    client=client,
                    output_dir=args.output_dir,
                    model=args.model,
                    new_mode=args.new_mode,
                    dry_run=args.dry_run,
                    bypass_cache=args.bypass_cache,
                    today=today,
                    no_gate=args.no_gate,
                    reconcile=args.reconcile,
                )
            except OllamaUnavailableError as e:
                logger.error("Ollama unreachable mid-run: %s", e); return 6
    except OllamaUnavailableError as e:
        logger.error("Ollama unreachable on startup: %s", e); return 6
    except KeyboardInterrupt:
        logger.warning("Interrupted by user"); return 130

    stats.jsons = len(json_paths)
    _print_summary(stats)

    if args.report_merges:
        try:
            _write_report(results, args.report_merges)
        except OSError as e:
            logger.warning("Could not write merge report: %s", e)

    if args.no_backup and stats.routed_merge > 0 and not args.dry_run:
        logger.warning(
            "Ran with --no-backup. %d merge(s) overwrote without backup.",
            stats.merged_written,
        )

    failed = stats.merged_failed + stats.new_failed
    if args.strict and failed > 0:
        return 5
    return 0


# ════════════════════════════════════════════════════════════════════════════
# Entry-point guard
# ════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    sys.exit(main())
