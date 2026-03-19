#!/usr/bin/env python3
"""
pipeline.py  -- Master Update Pipeline Orchestrator
===============================================================================
Chains all modules together: scan -> match -> update existing -> create new
-> summary report.

USAGE:
  python pipeline.py                      # Full dry run (scan, match, report)
  python pipeline.py --execute            # Apply updates + create new notes
  python pipeline.py --scan-only          # Just scan and report candidates
  python pipeline.py --match-only         # Scan + match, show match report
  python pipeline.py --update-only        # Scan + match + update (no create)
  python pipeline.py --create-only        # Scan + match + create unmatched
  python pipeline.py --include-original   # Also scan original v1 batch
  python pipeline.py --report FILE        # Write summary to file

REQUIREMENTS:
  Python 3.10+ (stdlib only, except PyYAML if available)

@author   PKB Scripting Architect
@version  1.0.0
"""

from __future__ import annotations

import argparse
import json
import sys
import io
import datetime
from pathlib import Path

# Force stdout to UTF-8 with replace fallback on Windows cp1252
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True
    )

# Ensure scripts directory is on import path
sys.path.insert(0, str(Path(__file__).parent))

from config import (
    EXTRACTION_BATCHES,
    PERMANENT_NOTES_DIR,
    PIPELINE_OUTPUT_DIR,
    OUTPUT_DIR,
)
from scan_extractions import scan_all_batches
from note_matcher import NoteMatcher, MatchReport
from note_updater import NoteUpdater, UpdateReport


# ==============================================================================
# CLI
# ==============================================================================

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pipeline.py",
        description="PKB Update Pipeline  -- scan, match, update, create.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
EXAMPLES:
  python pipeline.py                   # Full dry run
  python pipeline.py --execute         # Apply all changes
  python pipeline.py --match-only      # Just show matching report
  python pipeline.py --update-only --execute   # Update existing only
""",
    )
    # Mode flags
    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--scan-only", action="store_true",
                      help="Only scan batches and report candidates")
    mode.add_argument("--match-only", action="store_true",
                      help="Scan + match, show match report")
    mode.add_argument("--update-only", action="store_true",
                      help="Scan + match + update existing notes (no create)")
    mode.add_argument("--create-only", action="store_true",
                      help="Scan + match + create new notes for unmatched")

    # Execution
    p.add_argument("--execute", action="store_true", default=False,
                   help="Apply changes (default: dry run)")
    p.add_argument("--include-original", action="store_true", default=False,
                   help="Also scan original v1 JSON batch")
    p.add_argument("--report", type=str, metavar="FILE",
                   help="Write JSON summary report to FILE")
    p.add_argument("--verbose", "-v", action="store_true", default=False,
                   help="Show detailed per-note output")
    return p


# ==============================================================================
# PIPELINE STAGES
# ==============================================================================

def stage_scan(include_original: bool, verbose: bool) -> list:
    """Stage 1: Scan all extraction batches for note candidates."""
    print("\n" + "=" * 72)
    print("STAGE 1: SCANNING EXTRACTION BATCHES")
    print("=" * 72)

    scan_result = scan_all_batches(include_original=include_original)

    for batch in scan_result.batches:
        n_files = len(batch.json_files)
        n_cands = len(batch.candidates)
        print(f"  {batch.name}: {n_files} JSON files -> {n_cands} candidates")

    candidates = scan_result.all_candidates
    print(f"\n  TOTAL: {len(scan_result.all_json_files)} files -> {len(candidates)} candidates")

    if verbose and candidates:
        print(f"\n  Sample candidates:")
        for c in candidates[:5]:
            print(f"    - {c.concept_name} ({c.callout_type}, from {c.source_report})")
        if len(candidates) > 5:
            print(f"    ... and {len(candidates) - 5} more")

    return candidates


def stage_match(candidates: list, verbose: bool) -> MatchReport:
    """Stage 2: Match candidates against existing permanent notes."""
    print("\n" + "=" * 72)
    print("STAGE 2: MATCHING AGAINST EXISTING NOTES")
    print("=" * 72)

    matcher = NoteMatcher()
    print(f"  Indexed {len(matcher.index)} existing permanent notes")

    match_report = matcher.match_candidates(candidates)

    print(f"\n  Match results:")
    print(f"    Matched (exact):     {sum(1 for m in match_report.matched if m.match_type == 'exact')}")
    print(f"    Matched (alias):     {sum(1 for m in match_report.matched if m.match_type == 'alias')}")
    print(f"    Matched (fuzzy):     {sum(1 for m in match_report.matched if m.match_type == 'fuzzy')}")
    print(f"    Unmatched:           {len(match_report.unmatched)}")
    print(f"    Skipped duplicates:  {len(match_report.skipped_duplicates)}")
    print(f"    Match rate:          {match_report.match_rate:.1%}")

    if verbose:
        if match_report.matched:
            print(f"\n  Matched examples:")
            for m in match_report.matched[:5]:
                note_name = m.matched_note.stem if m.matched_note else "?"
                print(f"    [ok] {m.candidate.concept_name} -> {note_name} ({m.match_type}, {m.match_score:.2f})")

        if match_report.unmatched:
            print(f"\n  Unmatched examples:")
            for m in match_report.unmatched[:5]:
                suggestions = ""
                if m.fuzzy_suggestions:
                    top = m.fuzzy_suggestions[0]
                    suggestions = f" (closest: {top[0]}, {top[1]:.2f})"
                print(f"    [x] {m.candidate.concept_name}{suggestions}")

    return match_report


def stage_update(match_report: MatchReport, execute: bool, verbose: bool) -> UpdateReport:
    """Stage 3: Update existing notes with new content from matched candidates."""
    print("\n" + "=" * 72)
    print(f"STAGE 3: UPDATING EXISTING NOTES ({'EXECUTE' if execute else 'DRY RUN'})")
    print("=" * 72)

    if not match_report.matched:
        print("  No matched notes to update.")
        return UpdateReport(dry_run=not execute)

    updater = NoteUpdater(dry_run=not execute)
    update_report = updater.update_matched(match_report.matched)

    print(f"\n  Notes processed:  {len(update_report.actions)}")
    print(f"  Notes modified:   {update_report.modified_count}")
    print(f"  Notes unchanged:  {update_report.unchanged_count}")
    print(f"  Errors:           {update_report.error_count}")

    if verbose:
        modified = [a for a in update_report.actions if a.was_modified]
        if modified:
            print(f"\n  Modified notes:")
            for a in modified[:15]:
                changes = []
                if a.source_reports_added:
                    changes.append(f"+{len(a.source_reports_added)} reports")
                if a.evidence_added:
                    changes.append(f"+{a.evidence_added} evidence")
                if a.insights_added:
                    changes.append(f"+{a.insights_added} insights")
                if a.practices_added:
                    changes.append(f"+{a.practices_added} practices")
                if a.warnings_added:
                    changes.append(f"+{a.warnings_added} warnings")
                if a.wiki_links_added:
                    changes.append(f"+{a.wiki_links_added} links")
                if a.see_also_added:
                    changes.append(f"+{a.see_also_added} see-also")
                print(f"    {a.note_path.stem}: {', '.join(changes)}")
            if len(modified) > 15:
                print(f"    ... and {len(modified) - 15} more")

        errors = [a for a in update_report.actions if a.errors]
        if errors:
            print(f"\n  Errors:")
            for a in errors:
                for err in a.errors:
                    print(f"    [!] {a.note_path.stem}: {err}")

    return update_report


def stage_create(match_report: MatchReport, execute: bool, verbose: bool) -> dict:
    """Stage 4: Create new permanent notes for unmatched candidates."""
    print("\n" + "=" * 72)
    print(f"STAGE 4: CREATING NEW NOTES ({'EXECUTE' if execute else 'DRY RUN'})")
    print("=" * 72)

    unmatched = match_report.unmatched
    if not unmatched:
        print("  No unmatched candidates  -- all concepts already have notes.")
        return {"created": 0, "skipped": 0, "errors": []}

    # Import v1 note builder
    from note_builder import build_permanent_note, get_output_filename

    output_dir = OUTPUT_DIR
    if not output_dir.exists() and execute:
        output_dir.mkdir(parents=True, exist_ok=True)

    created = 0
    skipped = 0
    errors = []
    seen_filenames = set()  # Deduplicate across candidates with same concept name

    for result in unmatched:
        candidate = result.candidate
        try:
            filename = get_output_filename(candidate)

            # Skip duplicates within this run
            if filename in seen_filenames:
                continue
            seen_filenames.add(filename)

            output_path = output_dir / filename

            if output_path.exists():
                skipped += 1
                continue

            if execute:
                content = build_permanent_note(candidate)
                output_path.write_text(content, encoding="utf-8")

            created += 1
            if verbose:
                print(f"  {'Created' if execute else 'Would create'}: {filename}")

        except Exception as e:
            errors.append(f"{candidate.concept_name}: {e}")
            if verbose:
                print(f"  [!] Error: {candidate.concept_name}: {e}")

    print(f"\n  {'Created' if execute else 'Would create'}:  {created}")
    print(f"  Already exist:  {skipped}")
    if errors:
        print(f"  Errors:         {len(errors)}")

    return {"created": created, "skipped": skipped, "errors": errors}


# ==============================================================================
# SUMMARY REPORT
# ==============================================================================

def write_report(
    report_path: str,
    candidates_count: int,
    match_report: MatchReport | None,
    update_report: UpdateReport | None,
    create_result: dict | None,
    dry_run: bool,
) -> None:
    """Write a JSON summary of pipeline execution."""
    now = datetime.datetime.now().isoformat()

    data = {
        "pipeline_run": now,
        "dry_run": dry_run,
        "scan": {
            "total_candidates": candidates_count,
        },
    }

    if match_report:
        data["match"] = {
            "matched": len(match_report.matched),
            "unmatched": len(match_report.unmatched),
            "skipped_duplicates": len(match_report.skipped_duplicates),
            "match_rate": round(match_report.match_rate, 2),
            "unmatched_concepts": [
                r.candidate.concept_name for r in match_report.unmatched
            ],
        }

    if update_report:
        data["update"] = {
            "processed": len(update_report.actions),
            "modified": update_report.modified_count,
            "unchanged": update_report.unchanged_count,
            "errors": update_report.error_count,
            "modified_notes": [
                {
                    "note": a.note_path.stem,
                    "source_reports_added": a.source_reports_added,
                    "evidence_added": a.evidence_added,
                    "insights_added": a.insights_added,
                    "practices_added": a.practices_added,
                    "wiki_links_added": a.wiki_links_added,
                }
                for a in update_report.actions
                if a.was_modified
            ],
        }

    if create_result:
        data["create"] = create_result

    # Ensure output directory exists
    out = Path(report_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    print(f"\n  Report written to: {out}")


# ==============================================================================
# MAIN
# ==============================================================================

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    dry_run = not args.execute

    print("=" * 72)
    mode_label = "(DRY RUN)" if dry_run else "*** EXECUTING ***"
    print(f"  PKB UPDATE PIPELINE {mode_label}")
    print(f"  {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 72)

    match_report = None
    update_report = None
    create_result = None

    # -- Stage 1: Scan --------------------------------------------------
    candidates = stage_scan(args.include_original, args.verbose)

    if args.scan_only:
        _print_footer(dry_run)
        if args.report:
            write_report(args.report, len(candidates), None, None, None, dry_run)
        return

    # -- Stage 2: Match -------------------------------------------------
    match_report = stage_match(candidates, args.verbose)

    if args.match_only:
        _print_footer(dry_run)
        if args.report:
            write_report(args.report, len(candidates), match_report, None, None, dry_run)
        return

    # -- Stage 3: Update existing ---------------------------------------
    if not args.create_only:
        update_report = stage_update(match_report, args.execute, args.verbose)

    # -- Stage 4: Create new --------------------------------------------
    if not args.update_only:
        create_result = stage_create(match_report, args.execute, args.verbose)

    # -- Summary --------------------------------------------------------
    _print_footer(dry_run)

    if args.report:
        write_report(
            args.report, len(candidates), match_report,
            update_report, create_result, dry_run,
        )


def _print_footer(dry_run: bool) -> None:
    print("\n" + "=" * 72)
    if dry_run:
        print("PIPELINE COMPLETE (DRY RUN  -- no files modified)")
        print("Run with --execute to apply changes.")
    else:
        print("PIPELINE COMPLETE  -- changes applied.")
    print("=" * 72)


if __name__ == "__main__":
    main()
