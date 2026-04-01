#!/usr/bin/env python3
"""
pipeline_v2.py — Master Pipeline Orchestrator v2.0
═══════════════════════════════════════════════════════════════════════════════
End-to-end pipeline for transforming extracted reports into permanent notes,
updating existing notes, resolving wiki-links, auditing quality, and
generating a change report.

STAGES:
  0.  PRE-FLIGHT          — Validate environment, paths, dependencies
  1.  EXTRACT             — Run pkb_extractor.py on new report files → JSON + MD
  2.  BUILD NOTES         — Scan extractions → match → update existing → create new
  2b. DEDICATED NOTES     — Build 4 aggregate index notes from all callout types
  3.  GENERATE STUBS      — Create stub notes for frequently-referenced missing concepts
  4.  RESOLVE LINKS       — Rewrite wiki-links in reports to point to permanent note filenames
  5.  NORMALISE           — Normalise wiki-links in permanent notes (space→kebab)
  6.  AUDIT               — Full audit of permanent notes (resolution rate, orphans, etc.)
  7.  INDEX               — Update the permanent notes index
  8.  REPORT              — Generate a comprehensive change report
  9.  COMMIT              — Git commit all changes with a descriptive message

USAGE:
  python pipeline_v2.py                          # Full dry run
  python pipeline_v2.py --execute                # Apply all changes
  python pipeline_v2.py --stage 1                # Run only stage 1
  python pipeline_v2.py --from-stage 3           # Start from stage 3
  python pipeline_v2.py --to-stage 5             # Run stages 0-5 only
  python pipeline_v2.py --skip-extract           # Skip extraction (use existing JSON)
  python pipeline_v2.py --execute --auto-commit  # Apply + git commit
  python pipeline_v2.py --report-dir DIR         # Custom report input directory
  python pipeline_v2.py --skip-dedicated         # Skip dedicated notes build
  python pipeline_v2.py --help

REQUIREMENTS:
  Python 3.10+
  Packages: rich, click (optional: PyYAML for enhanced parsing)
  Scripts:  pkb_extractor.py, pipeline.py, audit_notes.py, generate_stubs.py,
            rewrite_report_wikilinks.py, normalise_wikilinks.py, vault_indexer.py,
            dedicated_notes_builder.py

@author   PKB Scripting Architect
@version  2.1.0
"""

from __future__ import annotations

import argparse
import datetime
import io
import json
import os
import shutil
import subprocess
import sys
import textwrap
import time
from dataclasses import dataclass, field
from pathlib import Path

from batch_tracker import mark_batch_processed

# ══════════════════════════════════════════════════════════════════════════════
# FORCE UTF-8 ON WINDOWS
# ══════════════════════════════════════════════════════════════════════════════
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding="utf-8", errors="replace", line_buffering=True
    )
if sys.stderr.encoding and sys.stderr.encoding.lower() != "utf-8":
    sys.stderr = io.TextIOWrapper(
        sys.stderr.buffer, encoding="utf-8", errors="replace", line_buffering=True
    )


# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

VAULT_ROOT = Path(r"D:\10_pur3v4d3r's-vault")
SCRIPTS_DIR = VAULT_ROOT / "99-scripts"
PIPELINE_DIR = SCRIPTS_DIR / "report-extraction-to-permanent-notes-building"
PERMANENT_NOTES_DIR = (
    VAULT_ROOT / "999-report-orginizing" / "_permanent-notes" / "_permanent-notes"
)
EXTRACTOR_OUTPUT_ROOT = VAULT_ROOT / "999-report-orginizing" / "_extractor-output"

# Report folders where wiki-links need resolution
REPORT_FOLDERS = [
    VAULT_ROOT / "999-report-orginizing" / "999-first-principles-reports",
    VAULT_ROOT / "999-report-orginizing" / "999-focused-analysis-report-generator",
    VAULT_ROOT / "999-report-orginizing" / "999-foundational-report-genrator",
    VAULT_ROOT / "999-report-orginizing" / "999-foundational-report-genrator" / "from-copilot",
    VAULT_ROOT / "999-report-orginizing" / "999-foundational-report-genrator" / "from-copilot" / "opus",
    VAULT_ROOT / "999-report-orginizing" / "999-socratic-reports",
    VAULT_ROOT / "999-report-orginizing" / "999-comparative-synthesis-report-generator",
    VAULT_ROOT / "999-report-orginizing" / "999-dialectical-re-examination-report-generator",
    VAULT_ROOT / "999-report-orginizing" / "in-pkm",
    VAULT_ROOT / "999-report-orginizing" / "llm-and-prompt-engineering",
    VAULT_ROOT / "999-report-orginizing" / "reports-to-file",
    VAULT_ROOT / "999-report-orginizing" / "999-stoicism",
    VAULT_ROOT / "999-report-orginizing" / "999-focused-analysis-report-generator-v1.1.0",
    VAULT_ROOT / "999-report-orginizing" / "999-generative-learning",
    VAULT_ROOT / "999-report-orginizing" / "srl-practice",
]

# Processed-batches tracker file for diff-aware runs
PROCESSED_BATCHES_FILE = PIPELINE_DIR / "_pipeline-output" / "_processed-batches.json"


def discover_unprocessed_report_dirs() -> list[Path]:
    """
    Auto-discover report directories that have not yet been extracted.

    Compares REPORT_FOLDERS against existing extraction batch names
    to find directories with .md files that haven't been processed yet.
    Returns a list of report directories to extract.
    """
    existing_batches = set()
    if EXTRACTOR_OUTPUT_ROOT.exists():
        for d in EXTRACTOR_OUTPUT_ROOT.iterdir():
            if d.is_dir():
                # Batch names are typically "YYYY-MM-DD-<foldername>"
                # Strip date prefix if present
                name = d.name
                parts = name.split("-", 3)
                if len(parts) >= 4 and parts[0].isdigit():
                    existing_batches.add(parts[3])
                existing_batches.add(name)

    # Also load from processed-batches tracker if it exists
    if PROCESSED_BATCHES_FILE.exists():
        try:
            data = json.loads(PROCESSED_BATCHES_FILE.read_text(encoding="utf-8"))
            existing_batches.update(data.get("processed_dirs", []))
        except (json.JSONDecodeError, KeyError):
            pass

    unprocessed = []
    for folder in REPORT_FOLDERS:
        if not folder.exists():
            continue
        # Check if this folder's name appears in any existing batch
        if folder.name in existing_batches:
            continue
        # Check if there are .md files to extract
        md_files = [
            f for f in folder.rglob("*.md")
            if not f.name.startswith("_")
            and f.name.lower() not in ("readme.md", "index.md")
        ]
        if md_files:
            unprocessed.append(folder)

    return unprocessed


# Pipeline output directory for logs and reports
PIPELINE_OUTPUT_DIR = PIPELINE_DIR / "_pipeline-output"
PIPELINE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Timestamp for this run
RUN_TIMESTAMP = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
RUN_ID = f"pipeline-run-{RUN_TIMESTAMP}"

# Minimum stub reference threshold
DEFAULT_MIN_STUB_REFS = 3

# ══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ══════════════════════════════════════════════════════════════════════════════


@dataclass
class StageResult:
    """Result from a single pipeline stage."""

    stage_num: int
    stage_name: str
    success: bool
    duration_secs: float = 0.0
    summary: str = ""
    details: dict = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    skipped: bool = False


@dataclass
class PipelineReport:
    """Aggregate report for an entire pipeline run."""

    run_id: str
    timestamp: str
    dry_run: bool
    stages: list[StageResult] = field(default_factory=list)
    notes_before: int = 0
    notes_after: int = 0
    notes_created: int = 0
    notes_updated: int = 0
    stubs_created: int = 0
    links_rewritten: int = 0
    audit_resolution_rate: float = 0.0
    audit_orphans: int = 0
    errors: list[str] = field(default_factory=list)


# ══════════════════════════════════════════════════════════════════════════════
# PIPELINE STATE (for --resume)
# ══════════════════════════════════════════════════════════════════════════════

PIPELINE_STATE_FILE = PIPELINE_OUTPUT_DIR / "_pipeline-state.json"


def _load_pipeline_state() -> dict:
    """Load the last pipeline run state, or empty dict."""
    if PIPELINE_STATE_FILE.exists():
        try:
            return json.loads(PIPELINE_STATE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def _save_pipeline_state(state: dict) -> None:
    """Persist pipeline state to disk."""
    PIPELINE_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    PIPELINE_STATE_FILE.write_text(
        json.dumps(state, indent=2, default=str), encoding="utf-8"
    )


def _update_stage_state(state: dict, stage_num: int, result: StageResult) -> None:
    """Update state dict after a stage completes."""
    completed = state.get("completed_stages", [])
    if result.success and stage_num not in completed:
        completed.append(stage_num)
    state["completed_stages"] = sorted(completed)
    state["last_stage"] = stage_num
    state["last_timestamp"] = datetime.datetime.now().isoformat()
    state["run_id"] = RUN_ID
    _save_pipeline_state(state)


# ══════════════════════════════════════════════════════════════════════════════
# UTILITIES
# ══════════════════════════════════════════════════════════════════════════════


def count_notes(directory: Path) -> int:
    """Count .md files in a directory."""
    if not directory.exists():
        return 0
    return len(list(directory.glob("*.md")))


def run_python_script(
    script_path: Path,
    args: list[str],
    cwd: Path | None = None,
    timeout: int = 600,
) -> subprocess.CompletedProcess:
    """Run a Python script as a subprocess and capture output."""
    cmd = [sys.executable, str(script_path)] + args
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(cwd) if cwd else None,
        timeout=timeout,
        env=env,
    )


def print_header(text: str, char: str = "═", width: int = 72) -> None:
    """Print a visual stage header."""
    print(f"\n{char * width}")
    print(f"  {text}")
    print(f"{char * width}")


def print_subheader(text: str) -> None:
    """Print a visual sub-header."""
    print(f"\n  ── {text} {'─' * max(1, 60 - len(text))}")


def format_duration(secs: float) -> str:
    """Format seconds into human-readable duration."""
    if secs < 60:
        return f"{secs:.1f}s"
    mins = int(secs // 60)
    remaining = secs % 60
    return f"{mins}m {remaining:.0f}s"


# ══════════════════════════════════════════════════════════════════════════════
# STAGE 0: PRE-FLIGHT CHECKS
# ══════════════════════════════════════════════════════════════════════════════


def stage_preflight(report_dir: Path | None = None) -> StageResult:
    """Validate environment, paths, and dependencies."""
    start = time.time()
    errors = []
    details = {}

    print_header("STAGE 0: PRE-FLIGHT CHECKS")

    # Check Python version
    ver = sys.version_info
    if ver < (3, 10):
        errors.append(f"Python 3.10+ required, found {ver.major}.{ver.minor}")
    print(f"  Python: {sys.version.split()[0]} ✓")

    # Check critical directories
    dirs_to_check = {
        "Vault root": VAULT_ROOT,
        "Scripts directory": SCRIPTS_DIR,
        "Pipeline directory": PIPELINE_DIR,
        "Permanent notes": PERMANENT_NOTES_DIR,
        "Extractor output": EXTRACTOR_OUTPUT_ROOT,
    }
    for name, path in dirs_to_check.items():
        if path.exists():
            print(f"  {name}: {path.name}/ ✓")
        else:
            errors.append(f"{name} not found: {path}")
            print(f"  {name}: MISSING ✗")

    # Check critical scripts exist
    scripts_to_check = {
        "pkb_extractor.py": SCRIPTS_DIR / "pkb_extractor.py",
        "pipeline.py": PIPELINE_DIR / "pipeline.py",
        "audit_notes.py": PIPELINE_DIR / "audit_notes.py",
        "generate_stubs.py": PIPELINE_DIR / "generate_stubs.py",
        "rewrite_report_wikilinks.py": PIPELINE_DIR / "rewrite_report_wikilinks.py",
        "vault_indexer.py": SCRIPTS_DIR / "vault_indexer.py",
    }
    for name, path in scripts_to_check.items():
        if path.exists():
            print(f"  Script {name}: ✓")
        else:
            errors.append(f"Missing script: {path}")
            print(f"  Script {name}: MISSING ✗")

    # Count existing notes
    note_count = count_notes(PERMANENT_NOTES_DIR)
    details["existing_notes"] = note_count
    print(f"\n  Existing permanent notes: {note_count}")

    # Count extraction batches with content
    batch_dirs = [d for d in EXTRACTOR_OUTPUT_ROOT.iterdir() if d.is_dir()] if EXTRACTOR_OUTPUT_ROOT.exists() else []
    json_count = sum(
        len(list(d.rglob("*_extracted.json"))) for d in batch_dirs
    )
    details["extraction_batches"] = len(batch_dirs)
    details["json_files"] = json_count
    print(f"  Extraction batches: {len(batch_dirs)} ({json_count} JSON files)")

    # Check git
    try:
        result = subprocess.run(
            ["git", "status", "--short"],
            capture_output=True, text=True, cwd=str(VAULT_ROOT), timeout=10
        )
        details["git_available"] = result.returncode == 0
        print(f"  Git: {'available ✓' if result.returncode == 0 else 'not available ✗'}")
    except (FileNotFoundError, subprocess.TimeoutExpired):
        details["git_available"] = False
        print("  Git: not found")

    # Custom report dir check
    if report_dir:
        if report_dir.exists():
            md_count = len(list(report_dir.rglob("*.md")))
            details["report_dir"] = str(report_dir)
            details["report_files"] = md_count
            print(f"\n  Report input dir: {report_dir}")
            print(f"  Report files to extract: {md_count}")
        else:
            errors.append(f"Report directory not found: {report_dir}")

    duration = time.time() - start
    success = len(errors) == 0
    summary = f"Pre-flight {'PASSED' if success else 'FAILED'} — {note_count} existing notes, {json_count} JSON files"

    return StageResult(
        stage_num=0, stage_name="Pre-Flight", success=success,
        duration_secs=duration, summary=summary, details=details, errors=errors
    )


# ══════════════════════════════════════════════════════════════════════════════
# STAGE 1: EXTRACTION
# ══════════════════════════════════════════════════════════════════════════════


def stage_extract(
    report_dir: Path | None = None,
    output_dir: Path | None = None,
    execute: bool = False,
) -> StageResult:
    """Run pkb_extractor.py on report files to produce JSON extractions."""
    start = time.time()
    errors = []
    details = {}

    print_header("STAGE 1: EXTRACTION (Reports → JSON)")

    if not report_dir:
        print("  No --report-dir specified; skipping extraction.")
        print("  (Using existing JSON files from extraction batches)")
        return StageResult(
            stage_num=1, stage_name="Extraction", success=True,
            duration_secs=time.time() - start,
            summary="Skipped — using existing extractions",
            skipped=True,
        )

    report_dir = Path(report_dir)
    if not report_dir.exists():
        errors.append(f"Report directory not found: {report_dir}")
        return StageResult(
            stage_num=1, stage_name="Extraction", success=False,
            duration_secs=time.time() - start,
            summary="FAILED — directory not found", errors=errors,
        )

    # Determine output directory
    if output_dir is None:
        batch_name = f"{datetime.date.today().isoformat()}-{report_dir.name}"
        output_dir = EXTRACTOR_OUTPUT_ROOT / batch_name

    md_files = list(report_dir.rglob("*.md"))
    # Filter out index files, READMEs, etc.
    md_files = [
        f for f in md_files
        if not f.name.startswith("_")
        and f.name.lower() not in ("readme.md", "index.md")
    ]

    details["input_dir"] = str(report_dir)
    details["output_dir"] = str(output_dir)
    details["report_count"] = len(md_files)

    print(f"  Input:  {report_dir}")
    print(f"  Output: {output_dir}")
    print(f"  Reports found: {len(md_files)}")

    if not md_files:
        print("  No report files found to extract.")
        return StageResult(
            stage_num=1, stage_name="Extraction", success=True,
            duration_secs=time.time() - start,
            summary="No reports to extract", details=details,
        )

    if not execute:
        print(f"\n  DRY RUN — would extract {len(md_files)} reports to {output_dir.name}/")
        return StageResult(
            stage_num=1, stage_name="Extraction", success=True,
            duration_secs=time.time() - start,
            summary=f"Would extract {len(md_files)} reports (dry run)",
            details=details, skipped=True,
        )

    # Run extraction
    extractor_script = SCRIPTS_DIR / "pkb_extractor.py"
    args = [
        "--input", str(report_dir),
        "--output", str(output_dir),
        "--recursive",
    ]
    print(f"\n  Running: pkb_extractor.py --input {report_dir.name} --output {output_dir.name}")

    result = run_python_script(extractor_script, args, cwd=VAULT_ROOT, timeout=1200)

    if result.returncode != 0:
        errors.append(f"Extractor failed: {result.stderr[:500]}")
        print(f"  ERROR: Extractor returned code {result.returncode}")
        if result.stderr:
            print(f"  STDERR: {result.stderr[:300]}")
    else:
        json_count = len(list(output_dir.rglob("*_extracted.json"))) if output_dir.exists() else 0
        details["json_produced"] = json_count
        print(f"  Extraction complete: {json_count} JSON files produced")

    duration = time.time() - start
    success = len(errors) == 0
    summary = f"Extracted {details.get('json_produced', 0)} files from {len(md_files)} reports"

    return StageResult(
        stage_num=1, stage_name="Extraction", success=success,
        duration_secs=duration, summary=summary, details=details, errors=errors,
    )


# ══════════════════════════════════════════════════════════════════════════════
# STAGE 2: BUILD NOTES (Scan → Match → Update → Create)
# ══════════════════════════════════════════════════════════════════════════════


def stage_build_notes(execute: bool = False, include_original: bool = False) -> StageResult:
    """Run the existing pipeline.py: scan → match → update existing → create new."""
    start = time.time()
    errors = []
    details = {}

    print_header("STAGE 2: BUILD NOTES (Scan → Match → Update → Create)")

    notes_before = count_notes(PERMANENT_NOTES_DIR)
    details["notes_before"] = notes_before

    args = ["--verbose"]
    if execute:
        args.append("--execute")
    if include_original:
        args.append("--include-original")

    # Write report to pipeline output
    report_file = PIPELINE_OUTPUT_DIR / f"{RUN_ID}-build-report.json"
    args.extend(["--report", str(report_file)])

    print(f"  Notes before: {notes_before}")
    print(f"  Running: pipeline.py {' '.join(args)}")

    result = run_python_script(PIPELINE_DIR / "pipeline.py", args, cwd=VAULT_ROOT, timeout=600)

    # Print stdout (the pipeline's own detailed output)
    if result.stdout:
        for line in result.stdout.strip().split("\n"):
            print(f"    {line}")

    if result.returncode != 0:
        errors.append(f"pipeline.py failed (code {result.returncode})")
        if result.stderr:
            errors.append(result.stderr[:500])

    # Parse the JSON report if it was written
    notes_after = count_notes(PERMANENT_NOTES_DIR)
    details["notes_after"] = notes_after
    details["notes_created"] = notes_after - notes_before

    if report_file.exists():
        try:
            build_data = json.loads(report_file.read_text(encoding="utf-8"))
            details["build_report"] = build_data
            if "match" in build_data:
                details["matched"] = build_data["match"].get("matched", 0)
                details["unmatched"] = build_data["match"].get("unmatched", 0)
            if "update" in build_data:
                details["updated"] = build_data["update"].get("modified", 0)
            if "create" in build_data:
                details["created"] = build_data["create"].get("created", 0)
        except (json.JSONDecodeError, KeyError):
            pass

    print(f"\n  Notes after: {notes_after} (Δ {notes_after - notes_before})")

    duration = time.time() - start
    success = len(errors) == 0
    created = details.get("created", notes_after - notes_before)
    updated = details.get("updated", 0)
    summary = f"Created {created} new, updated {updated} existing notes"

    return StageResult(
        stage_num=2, stage_name="Build Notes", success=success,
        duration_secs=duration, summary=summary, details=details, errors=errors,
    )


# ══════════════════════════════════════════════════════════════════════════════
# STAGE 2b: BUILD DEDICATED AGGREGATE NOTES
# ══════════════════════════════════════════════════════════════════════════════


def stage_build_dedicated_notes(execute: bool = False) -> StageResult:
    """Build the 4 dedicated aggregate index notes from all extraction data."""
    start = time.time()
    errors = []
    details = {}

    print_header("STAGE 2b: BUILD DEDICATED AGGREGATE NOTES")

    args = []
    if execute:
        args.append("--execute")

    print(f"  Running: dedicated_notes_builder.py {' '.join(args) or '(dry run)'}")

    result = run_python_script(
        PIPELINE_DIR / "dedicated_notes_builder.py", args, cwd=VAULT_ROOT, timeout=600,
    )

    if result.stdout:
        for line in result.stdout.strip().split("\n"):
            print(f"    {line}")

    if result.returncode != 0:
        errors.append(f"dedicated_notes_builder.py failed (code {result.returncode})")
        if result.stderr:
            errors.append(result.stderr[:500])

    # Parse key numbers from output
    for line in (result.stdout or "").split("\n"):
        lower = line.lower().strip()
        if "definitions:" in lower:
            try:
                details["definitions"] = int(lower.split(":")[-1].strip())
            except ValueError:
                pass
        if "references:" in lower:
            try:
                details["references"] = int(lower.split(":")[-1].strip())
            except ValueError:
                pass
        if "connections:" in lower:
            try:
                details["connections"] = int(lower.split(":")[-1].strip())
            except ValueError:
                pass
        if "expansions:" in lower:
            try:
                details["expansions"] = int(lower.split(":")[-1].strip())
            except ValueError:
                pass
        if "new permanent notes" in lower or "would create" in lower:
            try:
                for word in lower.split():
                    if word.isdigit():
                        details["def_notes_created"] = int(word)
                        break
            except (ValueError, IndexError):
                pass

    duration = time.time() - start
    success = len(errors) == 0
    defs = details.get("definitions", "?")
    refs = details.get("references", "?")
    summary = f"Dedicated notes: {defs} defs, {refs} refs collected"

    return StageResult(
        stage_num=2, stage_name="Dedicated Notes (2b)", success=success,
        duration_secs=duration, summary=summary, details=details, errors=errors,
    )


# ══════════════════════════════════════════════════════════════════════════════
# STAGE 3: GENERATE STUBS
# ══════════════════════════════════════════════════════════════════════════════


def stage_generate_stubs(
    execute: bool = False,
    min_refs: int = DEFAULT_MIN_STUB_REFS,
) -> StageResult:
    """Create stub notes for missing wiki-link targets."""
    start = time.time()
    errors = []
    details = {}

    print_header("STAGE 3: GENERATE STUBS (Gap-Fill)")

    notes_before = count_notes(PERMANENT_NOTES_DIR)
    details["notes_before"] = notes_before

    args = [f"--min-refs={min_refs}", f"--notes-dir={PERMANENT_NOTES_DIR}"]
    if execute:
        args.append("--execute")

    print(f"  Min references: {min_refs}")
    print(f"  Running: generate_stubs.py {' '.join(args)}")

    result = run_python_script(PIPELINE_DIR / "generate_stubs.py", args, cwd=VAULT_ROOT, timeout=300)

    if result.stdout:
        for line in result.stdout.strip().split("\n"):
            print(f"    {line}")

    if result.returncode != 0:
        errors.append(f"generate_stubs.py failed (code {result.returncode})")
        if result.stderr:
            errors.append(result.stderr[:500])

    notes_after = count_notes(PERMANENT_NOTES_DIR)
    details["notes_after"] = notes_after
    details["stubs_created"] = notes_after - notes_before

    print(f"\n  Stubs created: {notes_after - notes_before}")

    duration = time.time() - start
    success = len(errors) == 0
    summary = f"Created {notes_after - notes_before} stub notes (min-refs={min_refs})"

    return StageResult(
        stage_num=3, stage_name="Generate Stubs", success=success,
        duration_secs=duration, summary=summary, details=details, errors=errors,
    )


# ══════════════════════════════════════════════════════════════════════════════
# STAGE 4: RESOLVE WIKI-LINKS IN REPORTS
# ══════════════════════════════════════════════════════════════════════════════


def stage_resolve_report_links(execute: bool = False) -> StageResult:
    """Rewrite wiki-links in report files to pipe syntax."""
    start = time.time()
    errors = []
    details = {}

    print_header("STAGE 4: RESOLVE WIKI-LINKS IN REPORTS")

    args = ["--verbose"]
    if execute:
        args.append("--execute")

    print(f"  Running: rewrite_report_wikilinks.py {' '.join(args)}")

    result = run_python_script(
        PIPELINE_DIR / "rewrite_report_wikilinks.py", args, cwd=VAULT_ROOT, timeout=300,
    )

    if result.stdout:
        lines = result.stdout.strip().split("\n")
        # Show summary lines
        for line in lines:
            if any(kw in line.lower() for kw in ["total", "rewrite", "resolved", "unresolved", "files", "summary"]):
                print(f"    {line}")
        # Count rewrites from output
        rewrite_count = 0
        for line in lines:
            if "rewrit" in line.lower() and ("link" in line.lower() or "→" in line):
                rewrite_count += 1
        details["links_rewritten"] = rewrite_count

    if result.returncode != 0:
        errors.append(f"rewrite_report_wikilinks.py failed (code {result.returncode})")
        if result.stderr:
            errors.append(result.stderr[:500])

    duration = time.time() - start
    success = len(errors) == 0
    summary = f"Processed report wiki-links ({details.get('links_rewritten', 'N/A')} rewrites)"

    return StageResult(
        stage_num=4, stage_name="Resolve Report Links", success=success,
        duration_secs=duration, summary=summary, details=details, errors=errors,
    )


# ══════════════════════════════════════════════════════════════════════════════
# STAGE 5: NORMALISE WIKI-LINKS IN PERMANENT NOTES
# ══════════════════════════════════════════════════════════════════════════════


def stage_normalise_links(execute: bool = False) -> StageResult:
    """Normalise wiki-links vault-wide (space→kebab-case)."""
    start = time.time()
    errors = []
    details = {}

    print_header("STAGE 5: NORMALISE WIKI-LINKS")

    args = [
        f"--vault={VAULT_ROOT}",
        f"--perm-dir=999-report-orginizing/_permanent-notes/_permanent-notes",
        "--add-aliases",
    ]
    if execute:
        args.append("--execute")

    print(f"  Running: normalise_wikilinks.py {' '.join(args[:2])}...")

    result = run_python_script(SCRIPTS_DIR / "normalise_wikilinks.py", args, cwd=VAULT_ROOT, timeout=600)

    if result.stdout:
        lines = result.stdout.strip().split("\n")
        for line in lines:
            if any(kw in line.lower() for kw in ["total", "rewrit", "alias", "skipped", "phase", "summary"]):
                print(f"    {line}")

    if result.returncode != 0:
        errors.append(f"normalise_wikilinks.py failed (code {result.returncode})")
        if result.stderr:
            errors.append(result.stderr[:500])

    duration = time.time() - start
    success = len(errors) == 0
    summary = "Wiki-link normalisation complete"

    return StageResult(
        stage_num=5, stage_name="Normalise Links", success=success,
        duration_secs=duration, summary=summary, details=details, errors=errors,
    )


# ══════════════════════════════════════════════════════════════════════════════
# STAGE 6: AUDIT
# ══════════════════════════════════════════════════════════════════════════════


def stage_audit() -> StageResult:
    """Run audit_notes.py to measure quality metrics."""
    start = time.time()
    errors = []
    details = {}

    print_header("STAGE 6: AUDIT PERMANENT NOTES")

    report_file = PIPELINE_OUTPUT_DIR / f"{RUN_ID}-audit-report.md"
    args = ["--markdown", f"--notes-dir={PERMANENT_NOTES_DIR}", "--top=30"]

    print(f"  Running: audit_notes.py --markdown")

    result = run_python_script(PIPELINE_DIR / "audit_notes.py", args, cwd=VAULT_ROOT, timeout=300)

    if result.stdout:
        lines = result.stdout.strip().split("\n")
        for line in lines:
            if any(kw in line.lower() for kw in [
                "total", "resolv", "unresolv", "orphan", "missing", "rate", "connect"
            ]):
                print(f"    {line}")

        # Try to parse key metrics from output
        for line in lines:
            lower = line.lower()
            if "resolution" in lower and "%" in line:
                try:
                    pct = float(line.split("%")[0].split()[-1])
                    details["resolution_rate"] = pct
                except (ValueError, IndexError):
                    pass
            if "orphan" in lower:
                try:
                    for word in line.split():
                        if word.isdigit():
                            details["orphan_count"] = int(word)
                            break
                except (ValueError, IndexError):
                    pass

    if result.returncode != 0:
        errors.append(f"audit_notes.py failed (code {result.returncode})")
        if result.stderr:
            errors.append(result.stderr[:500])

    duration = time.time() - start
    success = len(errors) == 0
    rate = details.get("resolution_rate", "N/A")
    orphans = details.get("orphan_count", "N/A")
    summary = f"Resolution rate: {rate}%, Orphans: {orphans}"

    return StageResult(
        stage_num=6, stage_name="Audit", success=success,
        duration_secs=duration, summary=summary, details=details, errors=errors,
    )


# ══════════════════════════════════════════════════════════════════════════════
# STAGE 7: INDEX
# ══════════════════════════════════════════════════════════════════════════════


def stage_index(execute: bool = False) -> StageResult:
    """Update the permanent notes index using vault_indexer.py."""
    start = time.time()
    errors = []
    details = {}

    print_header("STAGE 7: UPDATE INDEX")

    if not execute:
        print("  DRY RUN — would re-index permanent notes directory")
        return StageResult(
            stage_num=7, stage_name="Index", success=True,
            duration_secs=time.time() - start,
            summary="Would update index (dry run)",
            skipped=True,
        )

    args = [
        "--input", str(PERMANENT_NOTES_DIR),
        "--name", ".permanent-notes-index",
        "--exclude", "_pipeline-output,test-output",
    ]

    print(f"  Running: vault_indexer.py --input {PERMANENT_NOTES_DIR.name}")

    result = run_python_script(SCRIPTS_DIR / "vault_indexer.py", args, cwd=VAULT_ROOT, timeout=300)

    if result.stdout:
        lines = result.stdout.strip().split("\n")
        for line in lines[-10:]:
            print(f"    {line}")

    if result.returncode != 0:
        errors.append(f"vault_indexer.py failed (code {result.returncode})")
        if result.stderr:
            errors.append(result.stderr[:500])

    duration = time.time() - start
    success = len(errors) == 0
    summary = "Index updated"

    return StageResult(
        stage_num=7, stage_name="Index", success=success,
        duration_secs=duration, summary=summary, details=details, errors=errors,
    )


# ══════════════════════════════════════════════════════════════════════════════
# STAGE 8: CHANGE REPORT
# ══════════════════════════════════════════════════════════════════════════════


def stage_report(report: PipelineReport) -> StageResult:
    """Generate a comprehensive change report (JSON + Markdown)."""
    start = time.time()
    errors = []

    print_header("STAGE 8: GENERATE CHANGE REPORT")

    # JSON report
    json_path = PIPELINE_OUTPUT_DIR / f"{RUN_ID}-report.json"
    md_path = PIPELINE_OUTPUT_DIR / f"{RUN_ID}-report.md"

    report_data = {
        "run_id": report.run_id,
        "timestamp": report.timestamp,
        "dry_run": report.dry_run,
        "summary": {
            "notes_before": report.notes_before,
            "notes_after": report.notes_after,
            "notes_created": report.notes_created,
            "notes_updated": report.notes_updated,
            "stubs_created": report.stubs_created,
            "links_rewritten": report.links_rewritten,
            "audit_resolution_rate": report.audit_resolution_rate,
            "audit_orphans": report.audit_orphans,
        },
        "stages": [
            {
                "num": s.stage_num,
                "name": s.stage_name,
                "success": s.success,
                "skipped": s.skipped,
                "duration": round(s.duration_secs, 2),
                "summary": s.summary,
                "errors": s.errors,
            }
            for s in report.stages
        ],
        "errors": report.errors,
    }

    try:
        json_path.write_text(json.dumps(report_data, indent=2, default=str), encoding="utf-8")
        print(f"  JSON report: {json_path.name}")
    except Exception as e:
        errors.append(f"Failed to write JSON report: {e}")

    # Markdown report
    mode_str = "DRY RUN" if report.dry_run else "EXECUTED"
    md = f"""---
title: "Pipeline Run Report — {report.run_id}"
doc_type: pipeline-report
doc_created: {datetime.date.today().isoformat()}
status: reference
tags:
  - pipeline
  - automation
  - permanent-notes
---

# Pipeline Run Report

> [!abstract] Summary
> **Run ID:** {report.run_id}
> **Mode:** {mode_str}
> **Timestamp:** {report.timestamp}

## Key Metrics

| Metric | Value |
|--------|-------|
| Notes before | {report.notes_before} |
| Notes after | {report.notes_after} |
| Notes created | {report.notes_created} |
| Notes updated | {report.notes_updated} |
| Stubs created | {report.stubs_created} |
| Links rewritten | {report.links_rewritten} |
| Resolution rate | {report.audit_resolution_rate}% |
| Orphan notes | {report.audit_orphans} |

## Stage Results

| # | Stage | Status | Duration | Summary |
|---|-------|--------|----------|---------|
"""
    for s in report.stages:
        status = "✅" if s.success else ("⏭️" if s.skipped else "❌")
        md += f"| {s.stage_num} | {s.stage_name} | {status} | {format_duration(s.duration_secs)} | {s.summary} |\n"

    if report.errors:
        md += "\n## Errors\n\n"
        for err in report.errors:
            md += f"- {err}\n"

    md += f"\n---\n*Generated by pipeline_v2.py at {report.timestamp}*\n"

    try:
        md_path.write_text(md, encoding="utf-8")
        print(f"  Markdown report: {md_path.name}")
    except Exception as e:
        errors.append(f"Failed to write Markdown report: {e}")

    duration = time.time() - start
    success = len(errors) == 0
    summary = f"Reports written to {PIPELINE_OUTPUT_DIR.name}/"

    return StageResult(
        stage_num=8, stage_name="Change Report", success=success,
        duration_secs=duration, summary=summary, errors=errors,
    )


# ══════════════════════════════════════════════════════════════════════════════
# STAGE 9: GIT COMMIT
# ══════════════════════════════════════════════════════════════════════════════


def stage_commit(report: PipelineReport, execute: bool = False) -> StageResult:
    """Git commit all pipeline changes with a descriptive message."""
    start = time.time()
    errors = []
    details = {}

    print_header("STAGE 9: GIT COMMIT")

    if not execute:
        print("  DRY RUN — would commit pipeline changes")
        return StageResult(
            stage_num=9, stage_name="Git Commit", success=True,
            duration_secs=time.time() - start,
            summary="Would commit (dry run)",
            skipped=True,
        )

    # Build commit message
    parts = []
    if report.notes_created > 0:
        parts.append(f"+{report.notes_created} new notes")
    if report.notes_updated > 0:
        parts.append(f"~{report.notes_updated} updated")
    if report.stubs_created > 0:
        parts.append(f"+{report.stubs_created} stubs")
    if report.links_rewritten > 0:
        parts.append(f"~{report.links_rewritten} links resolved")

    summary_parts = ", ".join(parts) if parts else "pipeline maintenance run"
    commit_subject = f"PKB Pipeline: {summary_parts}"

    commit_body = textwrap.dedent(f"""\
        Pipeline v2 run: {report.run_id}
        
        Notes: {report.notes_before} → {report.notes_after}
        Created: {report.notes_created} | Updated: {report.notes_updated} | Stubs: {report.stubs_created}
        Wiki-link resolution rate: {report.audit_resolution_rate}%
        Orphan notes: {report.audit_orphans}
        
        Stages executed:
    """)
    for s in report.stages:
        icon = "✓" if s.success else ("⏭" if s.skipped else "✗")
        commit_body += f"  [{icon}] {s.stage_name}: {s.summary}\n"

    commit_msg = f"{commit_subject}\n\n{commit_body}"
    details["commit_message"] = commit_msg

    print(f"  Commit message: {commit_subject}")

    try:
        # Stage all changes in relevant directories
        stage_paths = [
            "999-report-orginizing/_permanent-notes/",
            "999-report-orginizing/_extractor-output/",
            "99-scripts/report-extraction-to-permanent-notes-building/_pipeline-output/",
        ]
        # Also stage modified report folders
        for folder in REPORT_FOLDERS:
            if folder.exists():
                rel = folder.relative_to(VAULT_ROOT)
                stage_paths.append(str(rel) + "/")

        for path in stage_paths:
            subprocess.run(
                ["git", "add", path],
                cwd=str(VAULT_ROOT), capture_output=True, timeout=30,
            )

        # Commit
        result = subprocess.run(
            ["git", "commit", "-m", commit_msg],
            capture_output=True, text=True, cwd=str(VAULT_ROOT), timeout=30,
        )

        if result.returncode == 0:
            print(f"  Committed successfully ✓")
            details["committed"] = True
        elif "nothing to commit" in (result.stdout + result.stderr).lower():
            print(f"  Nothing to commit (no changes)")
            details["committed"] = False
        else:
            errors.append(f"Git commit failed: {result.stderr[:300]}")
            print(f"  Commit failed: {result.stderr[:200]}")

    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        errors.append(f"Git error: {e}")

    duration = time.time() - start
    success = len(errors) == 0
    summary = "Changes committed" if details.get("committed") else "No changes to commit"

    return StageResult(
        stage_num=9, stage_name="Git Commit", success=success,
        duration_secs=duration, summary=summary, details=details, errors=errors,
    )


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════


def build_cli() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pipeline_v2.py",
        description="PKB Report Extraction → Permanent Notes Pipeline v2",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            EXAMPLES:
              python pipeline_v2.py                               # Full dry run
              python pipeline_v2.py --execute                     # Execute all stages
              python pipeline_v2.py --execute --auto-commit       # Execute + git commit
              python pipeline_v2.py --stage 2                     # Only run Build Notes
              python pipeline_v2.py --from-stage 3 --execute      # Run stages 3-9
              python pipeline_v2.py --skip-extract --execute      # Skip extraction
              python pipeline_v2.py --report-dir /path/to/reports # Extract from specific dir
        """),
    )

    p.add_argument("--execute", action="store_true", default=False,
                   help="Apply changes (default: dry run)")
    p.add_argument("--auto-commit", action="store_true", default=False,
                   help="Git commit all changes after pipeline completes")

    # Stage selection
    stage_group = p.add_argument_group("Stage Selection")
    stage_group.add_argument("--stage", type=int, metavar="N",
                             help="Run only stage N (0-9)")
    stage_group.add_argument("--from-stage", type=int, metavar="N", default=0,
                             help="Start from stage N (default: 0)")
    stage_group.add_argument("--to-stage", type=int, metavar="N", default=9,
                             help="Run through stage N (default: 9)")
    stage_group.add_argument("--skip-extract", action="store_true", default=False,
                             help="Skip extraction stage (use existing JSON)")
    stage_group.add_argument("--skip-dedicated", action="store_true", default=False,
                             help="Skip dedicated aggregate notes build (stage 2b)")
    stage_group.add_argument("--resume", action="store_true", default=False,
                             help="Resume from the last successfully completed stage")

    # Input configuration
    input_group = p.add_argument_group("Input Configuration")
    input_group.add_argument("--report-dir", type=str, metavar="DIR",
                             help="Directory of report .md files to extract")
    input_group.add_argument("--output-dir", type=str, metavar="DIR",
                             help="Output directory for new extractions")
    input_group.add_argument("--auto-discover", action="store_true", default=False,
                             help="Auto-discover unprocessed report directories and extract them")
    input_group.add_argument("--include-original", action="store_true", default=False,
                             help="Include original v1 extraction batch")
    input_group.add_argument("--min-stub-refs", type=int, default=DEFAULT_MIN_STUB_REFS,
                             help=f"Minimum references for stub generation (default: {DEFAULT_MIN_STUB_REFS})")

    # Output
    p.add_argument("--verbose", "-v", action="store_true", default=False,
                   help="Show detailed output from each stage")

    return p


# ══════════════════════════════════════════════════════════════════════════════
# MAIN ORCHESTRATOR
# ══════════════════════════════════════════════════════════════════════════════


def main() -> None:
    parser = build_cli()
    args = parser.parse_args()

    execute = args.execute
    auto_commit = args.auto_commit

    # Determine which stages to run
    if args.stage is not None:
        start_stage = args.stage
        end_stage = args.stage
    else:
        start_stage = args.from_stage
        end_stage = args.to_stage

    if args.skip_extract and start_stage <= 1:
        start_stage = max(start_stage, 0)  # Still run preflight

    report_dir = Path(args.report_dir) if args.report_dir else None
    output_dir = Path(args.output_dir) if args.output_dir else None
    auto_discover = getattr(args, 'auto_discover', False)
    resume = getattr(args, 'resume', False)

    # Handle --resume: load last state and advance start_stage
    pipeline_state: dict = {}
    if resume:
        pipeline_state = _load_pipeline_state()
        completed = pipeline_state.get("completed_stages", [])
        if completed:
            resume_from = max(completed) + 1
            if resume_from > start_stage:
                print(f"  ♻️  Resuming: stages {completed} already completed → starting at stage {resume_from}")
                start_stage = resume_from
        else:
            print("  ♻️  No previous state found — starting from the beginning.")
    else:
        # Fresh run — clear any old state
        pipeline_state = {"completed_stages": [], "run_id": RUN_ID}

    # Pipeline report
    pipeline_report = PipelineReport(
        run_id=RUN_ID,
        timestamp=datetime.datetime.now().isoformat(),
        dry_run=not execute,
    )

    # Banner
    mode = "DRY RUN" if not execute else "*** EXECUTING ***"
    print_header(f"PKB PIPELINE v2.0 — {mode}", "█", 72)
    print(f"  Run ID: {RUN_ID}")
    print(f"  Stages: {start_stage} → {end_stage}")
    if report_dir:
        print(f"  Report input: {report_dir}")
    if auto_commit:
        print(f"  Auto-commit: YES")
    print()

    # ── Stage 0: Pre-Flight ─────────────────────────────────────────────
    if start_stage <= 0 <= end_stage:
        result = stage_preflight(report_dir)
        pipeline_report.stages.append(result)
        _update_stage_state(pipeline_state, 0, result)
        pipeline_report.notes_before = result.details.get("existing_notes", 0)
        if not result.success:
            print("\n  ❌ Pre-flight failed. Fix errors above before continuing.")
            _finalize(pipeline_report)
            return

    # ── Stage 1: Extract ────────────────────────────────────────────────
    if start_stage <= 1 <= end_stage and not args.skip_extract:
        if auto_discover and not report_dir:
            # Auto-discover unprocessed report directories
            unprocessed = discover_unprocessed_report_dirs()
            if unprocessed:
                print(f"\n  Auto-discovered {len(unprocessed)} unprocessed report directories:")
                for d in unprocessed:
                    print(f"    • {d.name}")
                for disco_dir in unprocessed:
                    result = stage_extract(disco_dir, None, execute)
                    pipeline_report.stages.append(result)
                    _update_stage_state(pipeline_state, 1, result)
                    if result.success and execute:
                        mark_batch_processed(disco_dir)
                    if not result.success:
                        print(f"\n  ❌ Extraction failed for {disco_dir.name}.")
            else:
                print("\n  Auto-discover: No unprocessed report directories found.")
                pipeline_report.stages.append(StageResult(
                    stage_num=1, stage_name="Extraction", success=True,
                    summary="Auto-discover found no new directories", skipped=True,
                ))
        else:
            result = stage_extract(report_dir, output_dir, execute)
            pipeline_report.stages.append(result)
            _update_stage_state(pipeline_state, 1, result)
            if result.success and execute and report_dir:
                mark_batch_processed(report_dir)
            if not result.success:
                print("\n  ❌ Extraction failed. Check errors above.")
                _finalize(pipeline_report)
                return
    elif args.skip_extract and start_stage <= 1:
        pipeline_report.stages.append(StageResult(
            stage_num=1, stage_name="Extraction", success=True,
            summary="Skipped (--skip-extract)", skipped=True,
        ))

    # ── Stage 2: Build Notes ────────────────────────────────────────────
    if start_stage <= 2 <= end_stage:
        result = stage_build_notes(execute, args.include_original)
        pipeline_report.stages.append(result)
        _update_stage_state(pipeline_state, 2, result)
        pipeline_report.notes_created = result.details.get("created", result.details.get("notes_created", 0))
        pipeline_report.notes_updated = result.details.get("updated", 0)

    # ── Stage 2b: Dedicated Notes ───────────────────────────────────────
    if start_stage <= 2 <= end_stage and not args.skip_dedicated:
        result = stage_build_dedicated_notes(execute)
        pipeline_report.stages.append(result)

    # ── Stage 3: Generate Stubs ─────────────────────────────────────────
    if start_stage <= 3 <= end_stage:
        result = stage_generate_stubs(execute, args.min_stub_refs)
        pipeline_report.stages.append(result)
        _update_stage_state(pipeline_state, 3, result)
        pipeline_report.stubs_created = result.details.get("stubs_created", 0)

    # ── Stage 4: Resolve Report Links ───────────────────────────────────
    if start_stage <= 4 <= end_stage:
        result = stage_resolve_report_links(execute)
        pipeline_report.stages.append(result)
        _update_stage_state(pipeline_state, 4, result)
        pipeline_report.links_rewritten = result.details.get("links_rewritten", 0)

    # ── Stage 5: Normalise Links ────────────────────────────────────────
    if start_stage <= 5 <= end_stage:
        result = stage_normalise_links(execute)
        pipeline_report.stages.append(result)
        _update_stage_state(pipeline_state, 5, result)

    # ── Stage 6: Audit ──────────────────────────────────────────────────
    if start_stage <= 6 <= end_stage:
        result = stage_audit()
        pipeline_report.stages.append(result)
        _update_stage_state(pipeline_state, 6, result)
        pipeline_report.audit_resolution_rate = result.details.get("resolution_rate", 0)
        pipeline_report.audit_orphans = result.details.get("orphan_count", 0)

    # ── Stage 7: Index ──────────────────────────────────────────────────
    if start_stage <= 7 <= end_stage:
        result = stage_index(execute)
        pipeline_report.stages.append(result)
        _update_stage_state(pipeline_state, 7, result)

    # Finalize counts
    pipeline_report.notes_after = count_notes(PERMANENT_NOTES_DIR)

    # ── Stage 8: Change Report ──────────────────────────────────────────
    if start_stage <= 8 <= end_stage:
        result = stage_report(pipeline_report)
        pipeline_report.stages.append(result)
        _update_stage_state(pipeline_state, 8, result)

    # ── Stage 9: Git Commit ─────────────────────────────────────────────
    if start_stage <= 9 <= end_stage and auto_commit:
        result = stage_commit(pipeline_report, execute)
        pipeline_report.stages.append(result)
        _update_stage_state(pipeline_state, 9, result)
    elif auto_commit and not execute:
        print("\n  ⚠️  --auto-commit ignored in dry-run mode")

    # ── Final Summary ───────────────────────────────────────────────────
    _finalize(pipeline_report)


def _finalize(report: PipelineReport) -> None:
    """Print final summary."""
    print_header("PIPELINE COMPLETE", "█", 72)

    total_time = sum(s.duration_secs for s in report.stages)
    passed = sum(1 for s in report.stages if s.success)
    failed = sum(1 for s in report.stages if not s.success and not s.skipped)
    skipped = sum(1 for s in report.stages if s.skipped)

    print(f"  Mode:     {'DRY RUN' if report.dry_run else 'EXECUTED'}")
    print(f"  Duration: {format_duration(total_time)}")
    print(f"  Stages:   {passed} passed, {failed} failed, {skipped} skipped")
    print(f"  Notes:    {report.notes_before} → {report.notes_after}")
    print(f"            +{report.notes_created} created, ~{report.notes_updated} updated, +{report.stubs_created} stubs")

    if report.audit_resolution_rate > 0:
        print(f"  Quality:  {report.audit_resolution_rate}% link resolution, {report.audit_orphans} orphans")

    if report.dry_run:
        print(f"\n  ℹ️  DRY RUN — no files were modified.")
        print(f"  Run with --execute to apply changes.")
        print(f"  Run with --execute --auto-commit to apply + commit.")

    all_errors = []
    for s in report.stages:
        all_errors.extend(s.errors)
    if all_errors:
        print(f"\n  ⚠️  Errors encountered:")
        for err in all_errors[:10]:
            print(f"    • {err}")
        if len(all_errors) > 10:
            print(f"    ... and {len(all_errors) - 10} more")


if __name__ == "__main__":
    main()
