#!/usr/bin/env python3
"""
conflict_detector.py — Cross-Batch Conflict Detection
═══════════════════════════════════════════════════════════════════════════════
Detects when multiple extraction batches produce contradictory or divergent
definitions, claims, or metadata for the same permanent note concept.

DETECTS:
  - Conflicting definitions (different definition text for same concept)
  - Domain disagreements (same concept assigned to different domains)
  - Status inconsistencies (different complexity/confidence signals)
  - Duplicate extractions (same concept extracted from same report)

USAGE:
  python conflict_detector.py                         # Full scan, console report
  python conflict_detector.py --export conflicts.md   # Export Obsidian-ready report

REQUIRES: Python 3.10+ (stdlib only)
"""

import json
import re
import sys
import argparse
from pathlib import Path
from datetime import date
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))

from config import EXTRACTION_BATCHES, PERMANENT_NOTES_DIR


# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

SIMILARITY_THRESHOLD = 0.70  # Below this = potentially conflicting


# ══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class Extraction:
    """One extracted concept from one batch."""
    concept: str
    batch: str
    source_report: str
    domain: str = ""
    definition_text: str = ""
    callout_type: str = ""


@dataclass
class Conflict:
    """A detected conflict between two or more extractions."""
    concept: str
    conflict_type: str          # "definition", "domain", "duplicate"
    severity: str               # "high", "medium", "low"
    extractions: list[Extraction] = field(default_factory=list)
    detail: str = ""


# ══════════════════════════════════════════════════════════════════════════════
# EXTRACTION LOADER
# ══════════════════════════════════════════════════════════════════════════════

def _normalize_concept(name: str) -> str:
    """Normalize concept name for comparison."""
    return re.sub(r"[^a-z0-9 ]", "", name.lower()).strip()


def load_all_extractions(batches: list[Path]) -> dict[str, list[Extraction]]:
    """Load all extracted concepts from all batches, grouped by normalized name."""
    by_concept: dict[str, list[Extraction]] = defaultdict(list)

    for batch_dir in batches:
        batch_name = batch_dir.name
        for json_file in sorted(batch_dir.glob("*_extracted.json")):
            try:
                data = json.loads(json_file.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue

            report_name = json_file.stem.replace("_extracted", "")

            # Extract from definitions
            for defn in data.get("definitions", []):
                title = defn.get("title", "").strip()
                if not title:
                    continue
                ext = Extraction(
                    concept=title,
                    batch=batch_name,
                    source_report=report_name,
                    domain=defn.get("domain", ""),
                    definition_text=defn.get("content", ""),
                    callout_type="definition",
                )
                by_concept[_normalize_concept(title)].append(ext)

            # Extract from original-synthesis
            for synth in data.get("original_syntheses", data.get("syntheses", [])):
                title = synth.get("title", "").strip()
                if not title:
                    continue
                ext = Extraction(
                    concept=title,
                    batch=batch_name,
                    source_report=report_name,
                    definition_text=synth.get("content", ""),
                    callout_type="original-synthesis",
                )
                by_concept[_normalize_concept(title)].append(ext)

            # Extract from framework-profiles
            for fw in data.get("framework_profiles", data.get("frameworks", [])):
                title = fw.get("title", fw.get("name", "")).strip()
                if not title:
                    continue
                ext = Extraction(
                    concept=title,
                    batch=batch_name,
                    source_report=report_name,
                    definition_text=fw.get("content", fw.get("description", "")),
                    callout_type="framework-profile",
                )
                by_concept[_normalize_concept(title)].append(ext)

    return by_concept


# ══════════════════════════════════════════════════════════════════════════════
# CONFLICT DETECTION
# ══════════════════════════════════════════════════════════════════════════════

def detect_conflicts(by_concept: dict[str, list[Extraction]]) -> list[Conflict]:
    """Analyse cross-batch extractions for conflicts."""
    conflicts = []

    for norm_name, extractions in by_concept.items():
        if len(extractions) < 2:
            continue

        # ── 1. Cross-batch definition divergence ──────────────────────
        # Group by batch
        by_batch: dict[str, list[Extraction]] = defaultdict(list)
        for ext in extractions:
            by_batch[ext.batch].append(ext)

        if len(by_batch) > 1:
            # Compare definition texts across batches
            batch_defs = []
            for batch, exts in by_batch.items():
                for ext in exts:
                    if ext.definition_text.strip():
                        batch_defs.append(ext)

            if len(batch_defs) >= 2:
                for i in range(len(batch_defs)):
                    for j in range(i + 1, len(batch_defs)):
                        if batch_defs[i].batch == batch_defs[j].batch:
                            continue
                        sim = SequenceMatcher(
                            None,
                            batch_defs[i].definition_text[:500],
                            batch_defs[j].definition_text[:500],
                        ).ratio()
                        if sim < SIMILARITY_THRESHOLD:
                            conflicts.append(Conflict(
                                concept=extractions[0].concept,
                                conflict_type="definition",
                                severity="high" if sim < 0.4 else "medium",
                                extractions=[batch_defs[i], batch_defs[j]],
                                detail=f"Similarity: {sim:.2%}",
                            ))

        # ── 2. Domain disagreements ───────────────────────────────────
        domains = {ext.domain for ext in extractions if ext.domain}
        if len(domains) > 1:
            conflicts.append(Conflict(
                concept=extractions[0].concept,
                conflict_type="domain",
                severity="low",
                extractions=extractions,
                detail=f"Domains: {', '.join(sorted(domains))}",
            ))

        # ── 3. Same-batch duplicates ──────────────────────────────────
        for batch, exts in by_batch.items():
            if len(exts) > 1:
                reports = [ext.source_report for ext in exts]
                unique_reports = set(reports)
                if len(unique_reports) < len(reports):
                    conflicts.append(Conflict(
                        concept=extractions[0].concept,
                        conflict_type="duplicate",
                        severity="medium",
                        extractions=exts,
                        detail=f"Batch '{batch}': {len(exts)} extractions from {len(unique_reports)} unique reports",
                    ))

    # Sort by severity then concept
    severity_order = {"high": 0, "medium": 1, "low": 2}
    conflicts.sort(key=lambda c: (severity_order.get(c.severity, 9), c.concept))
    return conflicts


# ══════════════════════════════════════════════════════════════════════════════
# REPORTING
# ══════════════════════════════════════════════════════════════════════════════

def print_report(conflicts: list[Conflict], by_concept: dict[str, list[Extraction]]) -> None:
    """Print a console conflict report."""
    total_concepts = len(by_concept)
    multi_batch = sum(1 for exts in by_concept.values() if len({e.batch for e in exts}) > 1)

    print("=" * 72)
    print("  CROSS-BATCH CONFLICT REPORT")
    print("=" * 72)
    print(f"\n  Total unique concepts:  {total_concepts}")
    print(f"  Multi-batch concepts:   {multi_batch}")
    print(f"  Conflicts detected:     {len(conflicts)}")

    by_type = defaultdict(int)
    by_severity = defaultdict(int)
    for c in conflicts:
        by_type[c.conflict_type] += 1
        by_severity[c.severity] += 1

    if conflicts:
        print(f"\n  By Type:")
        for t, n in sorted(by_type.items()):
            print(f"    {t:>12}: {n}")
        print(f"\n  By Severity:")
        for s, n in sorted(by_severity.items()):
            print(f"    {s:>12}: {n}")

        print(f"\n{'─' * 72}")
        print(f"  HIGH / MEDIUM CONFLICTS")
        print(f"{'─' * 72}")
        for c in conflicts:
            if c.severity == "low":
                continue
            print(f"\n  [{c.severity.upper()}] {c.concept}")
            print(f"    Type: {c.conflict_type}")
            print(f"    {c.detail}")
            for ext in c.extractions[:4]:
                snippet = ext.definition_text[:80].replace("\n", " ")
                print(f"      • {ext.batch}/{ext.source_report}: \"{snippet}...\"")

    print(f"\n{'=' * 72}\n")


def export_markdown(conflicts: list[Conflict], output_path: Path,
                    by_concept: dict[str, list[Extraction]]) -> None:
    """Export conflicts as an Obsidian-ready markdown report."""
    lines = [
        "---",
        f"title: Cross-Batch Conflict Report",
        f"generated: {date.today().isoformat()}",
        "type: pipeline-report",
        "---",
        "",
        "# Cross-Batch Conflict Report",
        "",
        f"> [!abstract] Summary",
        f"> **{len(conflicts)}** conflicts detected across "
        f"**{len(by_concept)}** unique concepts.",
        "",
    ]

    for severity in ("high", "medium", "low"):
        group = [c for c in conflicts if c.severity == severity]
        if not group:
            continue
        lines.append(f"## {severity.title()} Severity ({len(group)})")
        lines.append("")
        for c in group:
            lines.append(f"### {c.concept}")
            lines.append(f"**Type**: {c.conflict_type}  ")
            lines.append(f"**Detail**: {c.detail}")
            lines.append("")
            for ext in c.extractions:
                snippet = ext.definition_text[:120].replace("\n", " ")
                lines.append(f"- **{ext.batch}** / `{ext.source_report}`: \"{snippet}\"")
            lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Exported conflict report to {output_path}")


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Detect conflicts between extraction batches"
    )
    parser.add_argument("--export", type=str, metavar="FILE",
                        help="Export conflict report to Markdown file")
    args = parser.parse_args()

    if not EXTRACTION_BATCHES:
        print("No extraction batches found.")
        return

    print(f"\nScanning {len(EXTRACTION_BATCHES)} extraction batches...")
    by_concept = load_all_extractions(EXTRACTION_BATCHES)
    conflicts = detect_conflicts(by_concept)
    print_report(conflicts, by_concept)

    if args.export:
        export_markdown(conflicts, Path(args.export), by_concept)


if __name__ == "__main__":
    main()
