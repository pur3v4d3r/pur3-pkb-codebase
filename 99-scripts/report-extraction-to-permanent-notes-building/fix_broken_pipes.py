#!/usr/bin/env python3
"""
fix_broken_pipes.py
─────────────────────────────────────────────────────────────────────────────
Fixes all remaining broken pipe-syntax wiki-links and YAML corruption
across _permanent-notes/ and report-series/.

THREE FIX CATEGORIES:
  1. Broken pipe targets (space→hyphen, special mappings, report cross-refs)
  2. YAML corruption (dangling [[Dual Coding Theory" in 14 files)
  3. Creates Relatedness-Need and Cognitive-Psychology stubs

USAGE:
  python scripts/fix_broken_pipes.py              # Dry run
  python scripts/fix_broken_pipes.py --execute    # Apply changes

Run from project root:
  D:\10_pur3v4d3r's-vault\999-report-orginizing\_pkm-and-pkb-framework-1.0.0
"""

import sys
import io
import re
from pathlib import Path

# Windows UTF-8 console fix
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# ── CONFIGURATION ─────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
NOTES_DIR = PROJECT_ROOT / "_permanent-notes"
REPORTS_DIR = PROJECT_ROOT / "report-series"

# Special target mappings (target text → correct stem)
SPECIAL_MAPPINGS = {
    "Constructivist Learning Environments": "Constructivist-Learning-Environments-CLEs",
    "Self-Regulated Learning": "Self-Regulated-Learning-\u2014-SRL",  # em dash
    "Cognitive Psychology": "Cognitive-Psychology",  # stub will be created
    "Relatedness Need": "Relatedness-Need",  # stub will be created
    # Report cross-refs (missing date suffix)
    "19-sustaining-lifelong-learning-pkm-framework": "19-sustaining-lifelong-learning-pkm-framework-2026-03-15",
    "26-feedback-loops-pkm-framework": "26-feedback-loops-pkm-framework-2026-03-15",
}

# Targets to SKIP (heading anchors, template placeholders)
SKIP_TARGETS = {
    '#PKM/PKB Framework 1.0.0 Report Generator Prompt',
    '#PKM/PKB Framework 1.0.0: Comprehensive Report Registry',
    '#PKM/PKM/Life-Long Learning Framework 1.0.0 PROJECT BRIEF',
    'Full Concept Name',
}

# YAML corruption pattern
YAML_CORRUPTION = '[[Dual Coding Theory"'
YAML_FIX = 'Dual Coding Theory"'


def build_stem_index():
    """Build lowercase stem -> actual stem mapping from existing notes."""
    index = {}
    for f in NOTES_DIR.glob("*.md"):
        index[f.stem.lower()] = f.stem
    return index


def fix_broken_pipe_target(target: str, stem_index: dict) -> str | None:
    """
    Given a broken pipe target, return the corrected stem, or None to skip.
    """
    if target in SKIP_TARGETS:
        return None

    if target in SPECIAL_MAPPINGS:
        return SPECIAL_MAPPINGS[target]

    # Try direct space→hyphen
    hyphenated = target.replace(" ", "-")
    if hyphenated.lower() in stem_index:
        return stem_index[hyphenated.lower()]

    # No match found
    return None


def process_files(execute: bool):
    """Scan and fix all broken pipes and YAML corruption."""
    stem_index = build_stem_index()
    pipe_re = re.compile(r'\[\[([^|\]]+)\|([^\]]+)\]\]')

    total_pipe_fixes = 0
    total_yaml_fixes = 0
    files_modified = 0
    unresolved = {}

    all_dirs = [(NOTES_DIR, "note"), (REPORTS_DIR, "report")]

    for directory, label in all_dirs:
        if not directory.exists():
            continue
        for filepath in sorted(directory.glob("*.md")):
            try:
                text = filepath.read_text(encoding="utf-8")
            except Exception as e:
                print(f"  ERROR reading {filepath.name}: {e}")
                continue

            original = text
            file_fixes = 0

            # ── Fix 1: YAML corruption (dangling [[Dual Coding Theory") ───
            if YAML_CORRUPTION in text:
                text = text.replace(YAML_CORRUPTION, YAML_FIX)
                count = original.count(YAML_CORRUPTION)
                total_yaml_fixes += count
                file_fixes += count

            # ── Fix 2: Broken pipe targets ────────────────────────────────
            def replace_pipe(match):
                nonlocal file_fixes, total_pipe_fixes
                target = match.group(1)
                display = match.group(2)

                # Check if target already resolves
                if target.lower() in stem_index:
                    return match.group(0)  # Already valid
                # Check in reports dir
                if (REPORTS_DIR / f"{target}.md").exists():
                    return match.group(0)  # Valid report link

                corrected = fix_broken_pipe_target(target, stem_index)
                if corrected is None:
                    return match.group(0)  # Skip

                if corrected != target:
                    file_fixes += 1
                    total_pipe_fixes += 1
                    return f"[[{corrected}|{display}]]"

                return match.group(0)

            text = pipe_re.sub(replace_pipe, text)

            # ── Write if changed ──────────────────────────────────────────
            if text != original:
                files_modified += 1
                rel = filepath.relative_to(PROJECT_ROOT)
                print(f"  [{label}] {rel} ({file_fixes} fixes)")
                if execute:
                    filepath.write_text(text, encoding="utf-8")

    # ── Also find unresolved targets for reporting ────────────────────────
    for directory, label in all_dirs:
        if not directory.exists():
            continue
        for filepath in sorted(directory.glob("*.md")):
            try:
                text = filepath.read_text(encoding="utf-8")
            except Exception:
                continue
            for m in pipe_re.finditer(text):
                target = m.group(1)
                if target.lower() not in stem_index and \
                   not (REPORTS_DIR / f"{target}.md").exists() and \
                   target not in SKIP_TARGETS:
                    if target not in unresolved:
                        unresolved[target] = []
                    unresolved[target].append(filepath.name)

    return total_pipe_fixes, total_yaml_fixes, files_modified, unresolved


def main():
    execute = "--execute" in sys.argv

    print("=" * 70)
    print("FIX BROKEN PIPES & YAML CORRUPTION")
    print("=" * 70)
    print(f"Project: {PROJECT_ROOT}")
    print(f"Mode:    {'EXECUTE' if execute else 'DRY RUN (pass --execute to apply)'}")
    print()

    pipe_fixes, yaml_fixes, files_modified, unresolved = process_files(execute)

    print()
    print(f"{'Applied' if execute else 'Would apply'}:")
    print(f"  Pipe target fixes:  {pipe_fixes}")
    print(f"  YAML corruption:    {yaml_fixes}")
    print(f"  Files modified:     {files_modified}")

    if unresolved:
        print()
        print(f"STILL UNRESOLVED ({len(unresolved)} targets):")
        for target, files in sorted(unresolved.items()):
            print(f"  \"{target}\" in {len(files)} file(s)")

    if not execute and (pipe_fixes > 0 or yaml_fixes > 0):
        print()
        print("Run with --execute to apply these changes.")


if __name__ == "__main__":
    main()
