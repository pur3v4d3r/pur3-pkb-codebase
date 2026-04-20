#!/usr/bin/env python3
"""
generate_notes.py — Permanent Notes Generator CLI
═══════════════════════════════════════════════════════════════════════════════
Generates permanent notes from extracted JSON report data. Reads the JSON
files produced by pkb_extractor.py v1.1.0 and creates one permanent note
per definition/original-synthesis callout.

USAGE:
  python generate_notes.py                         # Dry run, all reports
  python generate_notes.py --execute               # Write all notes
  python generate_notes.py --report 01             # Dry run, report #01
  python generate_notes.py --report 01 --execute   # Write report #01 notes
  python generate_notes.py --list                  # List available JSON files
  python generate_notes.py --preview 01            # Preview candidates from #01

REQUIREMENTS:
  Python 3.10+ (stdlib only — no external packages)

OUTPUT:
  Permanent note .md files in _permanent-notes/ directory

@author   PKB Scripting Architect
@version  1.0.0
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

# Ensure scripts directory is on the import path
sys.path.insert(0, str(Path(__file__).parent))

from config import JSON_DIR, OUTPUT_DIR
from report_parser import load_json, extract_note_candidates, NoteCandidate
from note_builder import build_permanent_note, get_output_filename, InvalidConceptNameError


# ══════════════════════════════════════════════════════════════════════════════
# FILE DISCOVERY
# ══════════════════════════════════════════════════════════════════════════════

def find_json_files(json_dir: Path, report_num: str = None) -> list[Path]:
    """
    Find JSON files to process, optionally filtered by report number.

    Args:
        json_dir: Directory containing *_extracted.json files
        report_num: Optional report number (e.g. "01", "15") to filter to
    """
    if not json_dir.exists():
        print(f"  ERROR: JSON directory not found: {json_dir}")
        sys.exit(1)

    files = sorted(json_dir.glob("*_extracted.json"))

    if report_num:
        prefix = f"{report_num.zfill(2)}-"
        files = [f for f in files if f.name.startswith(prefix)]
        if not files:
            print(f"  ERROR: No JSON file found matching report #{report_num}")
            sys.exit(1)

    return files


# ══════════════════════════════════════════════════════════════════════════════
# DEDUPLICATION
# ══════════════════════════════════════════════════════════════════════════════

def _normalize_dedup_key(name: str) -> str:
    """Normalize a concept name for deduplication.

    Strips trailing abbreviation suffixes like ' — ZPD', ' — CLE', ' — PCLE'
    and leading articles, so "Zone of Proximal Development — ZPD" and
    "Zone of Proximal Development" merge correctly.
    """
    key = name.strip().lower()
    # Remove trailing " — ABBREV" (em-dash + uppercase abbreviation)
    key = re.sub(r'\s*[—–-]\s*[a-z]{1,8}$', '', key)
    return key


def deduplicate_candidates(all_candidates: list[NoteCandidate]) -> list[NoteCandidate]:
    """
    Deduplicate candidates across reports.

    When the same concept is defined in multiple reports (e.g. Schema in
    reports 01, 09, and 27), keep the one with the longest definition body
    and merge wiki-links from all instances.
    """
    by_name: dict[str, list[NoteCandidate]] = defaultdict(list)

    for candidate in all_candidates:
        key = _normalize_dedup_key(candidate.concept_name)
        by_name[key].append(candidate)

    deduped = []
    merge_count = 0

    for key, candidates in by_name.items():
        if len(candidates) == 1:
            deduped.append(candidates[0])
        else:
            merge_count += 1
            # Keep the most comprehensive definition
            best = max(candidates, key=lambda c: len(c.definition_body))

            # Merge wiki-links and source info from all duplicates
            all_wiki_links = set(best.wiki_links)
            all_sources = {best.source_report}
            for c in candidates:
                all_wiki_links.update(c.wiki_links)
                if c.source_report:
                    all_sources.add(c.source_report)

            best.wiki_links = sorted(all_wiki_links)
            # Track that this concept appeared in multiple reports
            if len(all_sources) > 1:
                best.attribution = (
                    f"{best.attribution} "
                    f"(defined across {len(all_sources)} reports)"
                ).strip()

            deduped.append(best)

    if merge_count:
        print(f"  Merged {merge_count} concepts defined across multiple reports")

    return deduped


# ══════════════════════════════════════════════════════════════════════════════
# COMMANDS
# ══════════════════════════════════════════════════════════════════════════════

def cmd_list(json_dir: Path) -> None:
    """List all available JSON files."""
    files = find_json_files(json_dir)
    print(f"\n  Available JSON files ({len(files)}):\n")
    for f in files:
        print(f"    {f.name}")
    print()


def cmd_preview(json_dir: Path, report_num: str) -> None:
    """Preview note candidates from a specific report."""
    files = find_json_files(json_dir, report_num)

    for filepath in files:
        print(f"\n  Preview: {filepath.name}")
        print(f"  {'=' * 66}")

        data = load_json(filepath)
        candidates = extract_note_candidates(data)

        if not candidates:
            print("    No note candidates found.")
            continue

        for i, c in enumerate(candidates, 1):
            print(f"\n    [{i:02d}] {c.concept_name}")
            print(f"         Type:        {c.callout_type}")
            print(f"         Domain:      {c.domain}")
            print(f"         Attribution: {c.attribution or 'N/A'}")
            print(f"         Definition:  {c.definition_body[:100]}...")
            print(f"         Wiki-links:  {len(c.wiki_links)}")
            print(f"         Evidence:    {len(c.evidence)} items")
            print(f"         Insights:    {len(c.insights)} items")
            print(f"         Practices:   {len(c.practices)} items")
            try:
                print(f"         Filename:    {get_output_filename(c)}")
            except InvalidConceptNameError as exc:
                print(f"         Filename:    [REJECTED] {exc}")

        print(f"\n    Total candidates: {len(candidates)}")


def cmd_process(json_dir: Path, output_dir: Path,
                report_num: str = None, execute: bool = False) -> None:
    """
    Process reports and generate permanent notes.

    Default mode is dry run (preview). Use --execute to write files.
    """
    files = find_json_files(json_dir, report_num)

    mode_label = "EXECUTE — writing files" if execute else "DRY RUN — preview only"
    print(f"\n  {'=' * 66}")
    print(f"  PERMANENT NOTES GENERATOR v1.0.0")
    print(f"  Mode:    {mode_label}")
    print(f"  Reports: {len(files)}")
    print(f"  Input:   {json_dir}")
    print(f"  Output:  {output_dir}")
    print(f"  {'=' * 66}")

    # ── Phase 1: Extract candidates ───────────────────────────────────────
    print(f"\n  Phase 1: Extracting candidates from reports...\n")

    all_candidates = []
    report_stats = {}

    for filepath in files:
        try:
            data = load_json(filepath)
            candidates = extract_note_candidates(data)
            all_candidates.extend(candidates)
            report_stats[filepath.stem] = len(candidates)

            # Short report name for display
            short_name = filepath.stem[:50]
            defs = sum(1 for c in candidates if c.callout_type == "definition")
            syns = sum(1 for c in candidates if c.callout_type == "original-synthesis")
            print(f"    [OK] {short_name}...")
            print(f"         {defs} definitions, {syns} syntheses")

        except (json.JSONDecodeError, KeyError) as e:
            print(f"    [!!] {filepath.name}: ERROR — {e}")
            report_stats[filepath.stem] = -1

    # ── Phase 2: Deduplicate ──────────────────────────────────────────────
    print(f"\n  Phase 2: Deduplication...\n")
    print(f"    Raw candidates:  {len(all_candidates)}")

    deduped = deduplicate_candidates(all_candidates)
    removed = len(all_candidates) - len(deduped)

    print(f"    Duplicates:      {removed}")
    print(f"    Unique notes:    {len(deduped)}")

    # Count by type
    def_count = sum(1 for c in deduped if c.callout_type == "definition")
    syn_count = sum(1 for c in deduped if c.callout_type == "original-synthesis")
    print(f"    Definitions:     {def_count}")
    print(f"    Syntheses:       {syn_count}")

    # ── Phase 3: Generate notes ───────────────────────────────────────────
    print(f"\n  Phase 3: Generating notes...\n")

    if execute:
        output_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    skipped = 0
    errors = 0

    for candidate in sorted(deduped, key=lambda c: c.concept_name.lower()):
        try:
            filename = get_output_filename(candidate)
        except InvalidConceptNameError as exc:
            print(f"    [REJECT] {candidate.concept_name!r}: {exc}")
            errors += 1
            continue
        output_path = output_dir / filename

        # Skip existing files
        if output_path.exists():
            print(f"    [SKIP] {filename} — already exists")
            skipped += 1
            continue

        try:
            note_content = build_permanent_note(candidate)

            if execute:
                output_path.write_text(note_content, encoding="utf-8")
                print(f"    [DONE] {filename} ({len(note_content):,} chars)")
            else:
                print(f"    [DRY]  {filename}")
                print(f"           {candidate.concept_name} [{candidate.callout_type}]"
                      f" — {candidate.domain} — {len(note_content):,} chars")

            written += 1

        except Exception as e:
            print(f"    [ERR]  {filename} — {e}")
            errors += 1

    # ── Summary ───────────────────────────────────────────────────────────
    print(f"\n  {'=' * 66}")
    print(f"  SUMMARY")
    print(f"  {'=' * 66}")
    print(f"    Reports processed:     {len(files)}")
    print(f"    Notes {'written:' if execute else 'to generate:':<19}{written}")
    print(f"    Skipped (existing):    {skipped}")
    print(f"    Errors:                {errors}")

    if not execute and written > 0:
        print(f"\n    Run with --execute to write {written} files to disk.")

    print()


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Generate permanent notes from extracted report JSON data.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_notes.py                         # Dry run, all reports
  python generate_notes.py --execute               # Write all notes
  python generate_notes.py --report 01             # Dry run, report #01
  python generate_notes.py --report 01 --execute   # Write report #01 notes
  python generate_notes.py --list                  # List available JSON files
  python generate_notes.py --preview 01            # Preview candidates
        """
    )

    parser.add_argument(
        "--report", "-r", type=str, default=None,
        help="Process a specific report number (e.g. 01, 15, 30)"
    )
    parser.add_argument(
        "--execute", "-x", action="store_true",
        help="Write files to disk (default is dry run)"
    )
    parser.add_argument(
        "--list", "-l", action="store_true",
        help="List all available JSON files and exit"
    )
    parser.add_argument(
        "--preview", "-p", type=str, default=None,
        help="Preview note candidates from a specific report"
    )
    parser.add_argument(
        "--json-dir", type=Path, default=JSON_DIR,
        help=f"JSON input directory (default: {JSON_DIR})"
    )
    parser.add_argument(
        "--output-dir", type=Path, default=OUTPUT_DIR,
        help=f"Output directory (default: {OUTPUT_DIR})"
    )

    args = parser.parse_args()

    if args.list:
        cmd_list(args.json_dir)
    elif args.preview:
        cmd_preview(args.json_dir, args.preview)
    else:
        cmd_process(args.json_dir, args.output_dir, args.report, args.execute)


if __name__ == "__main__":
    main()
