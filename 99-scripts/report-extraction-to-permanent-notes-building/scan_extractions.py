"""
scan_extractions.py  -- Batch Scanner for JSON Extraction Files
===============================================================================
Walks all configured extraction batch directories and collects every
*_extracted.json file, parsing each into NoteCandidate objects using
the existing report_parser module.

REQUIRES: Python 3.10+
USAGE:
    # As module (imported by pipeline.py)
    from scan_extractions import scan_all_batches

    # As standalone CLI
    python scan_extractions.py              # Summary of all batches
    python scan_extractions.py --list       # List every JSON file found
    python scan_extractions.py --stats      # Detailed per-batch statistics
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from config import (
    EXTRACTION_BATCHES,
    EXTRACTOR_OUTPUT_ROOT,
    ORIGINAL_JSON_DIR,
    NOTE_GENERATING_CALLOUTS,
    EVIDENCE_CALLOUTS,
    INSIGHT_CALLOUTS,
    CONNECTION_CALLOUTS,
    PRACTICE_CALLOUTS,
    WARNING_CALLOUTS,
    EXPANSION_CALLOUTS,
    MAX_EVIDENCE_PER_NOTE,
    MAX_INSIGHTS_PER_NOTE,
    MAX_CONNECTIONS_PER_NOTE,
    MAX_PRACTICES_PER_NOTE,
    MAX_WARNINGS_PER_NOTE,
    MAX_EXPANSION_TOPICS,
)
from report_parser import (
    NoteCandidate,
    ReportMetadata,
    load_json,
    extract_report_metadata,
    parse_definition_title,
    parse_synthesis_title,
)


# ==============================================================================
# DATA CLASSES
# ==============================================================================

@dataclass
class BatchResult:
    """Results from scanning a single extraction batch."""
    batch_path: Path
    json_files: list[Path] = field(default_factory=list)
    candidates: list[NoteCandidate] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def name(self) -> str:
        return self.batch_path.name


@dataclass
class ScanResult:
    """Aggregated results from scanning all extraction batches."""
    batches: list[BatchResult] = field(default_factory=list)

    @property
    def all_candidates(self) -> list[NoteCandidate]:
        return [c for b in self.batches for c in b.candidates]

    @property
    def all_json_files(self) -> list[Path]:
        return [f for b in self.batches for f in b.json_files]

    @property
    def total_errors(self) -> list[str]:
        return [e for b in self.batches for e in b.errors]


# ==============================================================================
# JSON FILE DISCOVERY
# ==============================================================================

def find_json_files(root: Path) -> list[Path]:
    """
    Recursively find all *_extracted.json files under a directory.

    Handles the varied directory layouts:
      - batch/reports/domain/json/*.json
      - batch/domain/reports/json/*.json
      - batch/json/*.json
    """
    if not root.exists():
        return []
    return sorted(root.rglob("*_extracted.json"))


# ==============================================================================
# CANDIDATE EXTRACTION (mirrors generate_notes.py logic)
# ==============================================================================

def _extract_wiki_links(items: list[dict]) -> list[str]:
    """Extract all wiki-link targets from extracted_items.wiki_links."""
    links = []
    for item in items:
        target = item.get("target", "")
        if target:
            links.append(target)
    return links


def _collect_supporting(callouts: list[dict], types: list[str], limit: int) -> list[str]:
    """Collect body text from supporting callouts of specified types."""
    results = []
    for c in callouts:
        if c.get("type", "").lower() in types and len(results) < limit:
            body = c.get("body", "").strip()
            if body:
                results.append(body)
    return results


def extract_candidates_from_json(json_path: Path) -> tuple[list[NoteCandidate], list[str]]:
    """
    Parse a single JSON extraction file and return note candidates.

    This replicates the core logic from generate_notes.py but is designed
    for batch scanning across arbitrary extraction directories.

    Returns:
        (candidates, errors) tuple
    """
    candidates = []
    errors = []

    try:
        data = load_json(json_path)
    except Exception as e:
        return [], [f"Failed to load {json_path.name}: {e}"]

    if not data:
        return [], [f"Empty or invalid JSON: {json_path.name}"]

    # Extract report-level metadata
    try:
        metadata = extract_report_metadata(data)
    except Exception as e:
        errors.append(f"Metadata extraction failed for {json_path.name}: {e}")
        metadata = ReportMetadata(
            doc_id="",
            source_file=json_path.stem.replace("_extracted", ""),
            primary_domain="",
            secondary_domains=[],
            analytical_focus="",
            series_position="",
            builds_on=[],
            feeds_into=[],
            confidence="medium",
            knowledge_level="intermediate",
            tags=[],
            related_concepts=[],
            aliases=[],
        )

    items = data.get("extracted_items", {})
    callouts = items.get("callouts", [])
    wiki_links_raw = items.get("wiki_links", [])
    wiki_links = _extract_wiki_links(wiki_links_raw)

    # Collect supporting content from callouts
    evidence = _collect_supporting(callouts, EVIDENCE_CALLOUTS, MAX_EVIDENCE_PER_NOTE)
    insights = _collect_supporting(callouts, INSIGHT_CALLOUTS, MAX_INSIGHTS_PER_NOTE)
    connections = _collect_supporting(callouts, CONNECTION_CALLOUTS, MAX_CONNECTIONS_PER_NOTE)
    practices = _collect_supporting(callouts, PRACTICE_CALLOUTS, MAX_PRACTICES_PER_NOTE)
    warnings = _collect_supporting(callouts, WARNING_CALLOUTS, MAX_WARNINGS_PER_NOTE)

    # Extract expansion topics
    expansion_topics = []
    for c in callouts:
        if c.get("type", "").lower() in EXPANSION_CALLOUTS:
            body = c.get("body", "").strip()
            if body and len(expansion_topics) < MAX_EXPANSION_TOPICS:
                expansion_topics.append(body)

    # Process note-generating callouts
    for callout in callouts:
        ctype = callout.get("type", "").lower()
        if ctype not in NOTE_GENERATING_CALLOUTS:
            continue

        title = callout.get("title", "").strip()
        body = callout.get("body", "").strip()

        if not title and not body:
            continue

        # Parse title based on callout type
        if ctype == "definition":
            concept_name, domain, attribution = parse_definition_title(title or body)
        elif ctype == "original-synthesis":
            concept_name = parse_synthesis_title(title, body)
            domain = metadata.primary_domain or "other"
            attribution = ""
        else:
            concept_name = title or "Untitled"
            domain = metadata.primary_domain or "other"
            attribution = ""

        if not concept_name or concept_name.lower() in ("untitled", ""):
            continue

        # Strip HTML tags (e.g. <span> color coding from report formatting)
        concept_name = re.sub(r'<[^>]+>', '', concept_name).strip()

        # Strip leading markdown artifacts (e.g. "# Definition" from callout titles)
        concept_name = re.sub(r'^#+\s*', '', concept_name).strip()
        # Strip leading/trailing bold/italic markers
        concept_name = re.sub(r'^\*+|\*+$', '', concept_name).strip()
        # Strip emoji and non-ASCII characters (keep only ASCII-printable)
        concept_name = re.sub(r'[^\x20-\x7E]', '', concept_name).strip()

        # Skip invalid concept names
        if not concept_name or len(concept_name) < 3:
            continue
        if re.match(r'^\{.*\}$', concept_name):
            # Template placeholder like {Term} or {Title-of-the-Synthesis}
            continue
        if re.match(r'^[^a-zA-Z]*$', concept_name):
            # No alphabetic characters at all (symbol-only)
            continue
        # Blocklist: generic section headers that are not real concepts
        BLOCKLIST = {
            "purpose", "definition", "tools", "resources", "prompts",
            "feedback", "mastery", "information", "overview", "summary",
            "introduction", "conclusion", "references", "background",
            "methodology", "results", "discussion", "appendix",
            "core definition", "core concept", "key terms",
            "understanding", "script",
        }
        if concept_name.lower() in BLOCKLIST:
            continue

        candidate = NoteCandidate(
            concept_name=concept_name,
            callout_type=ctype,
            domain=domain,
            attribution=attribution,
            definition_body=body,
            source_report=metadata.source_file,
            line_number=callout.get("line_number", 0),
            report_metadata=metadata,
            evidence=evidence,
            insights=insights,
            connections=connections,
            practices=practices,
            warnings=warnings,
            expansion_topics=expansion_topics,
            wiki_links=wiki_links,
        )
        candidates.append(candidate)

    return candidates, errors


# ==============================================================================
# BATCH SCANNING
# ==============================================================================

def scan_batch(batch_path: Path) -> BatchResult:
    """Scan a single extraction batch directory."""
    result = BatchResult(batch_path=batch_path)

    json_files = find_json_files(batch_path)
    result.json_files = json_files

    for jf in json_files:
        candidates, errs = extract_candidates_from_json(jf)
        result.candidates.extend(candidates)
        result.errors.extend(errs)

    return result


def scan_all_batches(
    batch_dirs: Optional[list[Path]] = None,
    include_original: bool = False,
) -> ScanResult:
    """
    Scan all configured extraction batches and return unified results.

    Args:
        batch_dirs: Override batch directories (default: EXTRACTION_BATCHES from config)
        include_original: If True, also scan the original 30-report batch
    """
    dirs = batch_dirs or list(EXTRACTION_BATCHES)

    if include_original and ORIGINAL_JSON_DIR.exists():
        dirs.append(ORIGINAL_JSON_DIR)

    result = ScanResult()
    for batch_dir in dirs:
        if not batch_dir.exists():
            result.batches.append(BatchResult(
                batch_path=batch_dir,
                errors=[f"Directory not found: {batch_dir}"],
            ))
            continue
        result.batches.append(scan_batch(batch_dir))

    return result


# ==============================================================================
# CLI
# ==============================================================================

def _print_summary(result: ScanResult) -> None:
    """Print a summary report of all scanned batches."""
    print("\n" + "=" * 72)
    print("EXTRACTION BATCH SCANNER  -- Summary")
    print("=" * 72)

    total_files = 0
    total_candidates = 0

    for batch in result.batches:
        n_files = len(batch.json_files)
        n_cands = len(batch.candidates)
        total_files += n_files
        total_candidates += n_cands
        status = "[ok]" if not batch.errors else f"[!] ({len(batch.errors)} errors)"
        print(f"\n  {batch.name}")
        print(f"    JSON files:  {n_files:>5}")
        print(f"    Candidates:  {n_cands:>5}")
        print(f"    Status:      {status}")

    print(f"\n{'-' * 72}")
    print(f"  TOTAL FILES:      {total_files}")
    print(f"  TOTAL CANDIDATES: {total_candidates}")
    if result.total_errors:
        print(f"  TOTAL ERRORS:     {len(result.total_errors)}")
    print("=" * 72 + "\n")


def _print_list(result: ScanResult) -> None:
    """Print every JSON file found."""
    for batch in result.batches:
        print(f"\n-- {batch.name} --")
        for jf in batch.json_files:
            print(f"  {jf.name}")
        if not batch.json_files:
            print("  (none)")


def _print_stats(result: ScanResult) -> None:
    """Print detailed per-batch statistics."""
    _print_summary(result)

    # Concept frequency across all batches
    concept_counts: dict[str, int] = {}
    for c in result.all_candidates:
        key = c.concept_name.lower().strip()
        concept_counts[key] = concept_counts.get(key, 0) + 1

    # Concepts appearing in multiple reports (cross-references)
    multi_source = {k: v for k, v in concept_counts.items() if v > 1}
    if multi_source:
        print(f"\nConcepts appearing in multiple reports ({len(multi_source)}):")
        for name, count in sorted(multi_source.items(), key=lambda x: -x[1])[:30]:
            print(f"  {count}x  {name}")

    # Domain distribution
    domain_counts: dict[str, int] = {}
    for c in result.all_candidates:
        d = c.domain or "unknown"
        domain_counts[d] = domain_counts.get(d, 0) + 1
    if domain_counts:
        print(f"\nDomain distribution:")
        for d, count in sorted(domain_counts.items(), key=lambda x: -x[1]):
            print(f"  {count:>5}  {d}")

    # Errors detail
    if result.total_errors:
        print(f"\nErrors ({len(result.total_errors)}):")
        for err in result.total_errors[:20]:
            print(f"  [!] {err}")
        if len(result.total_errors) > 20:
            print(f"  ... and {len(result.total_errors) - 20} more")


def main() -> None:
    args = sys.argv[1:]

    print("Scanning extraction batches...")
    result = scan_all_batches()

    if "--list" in args:
        _print_list(result)
    elif "--stats" in args:
        _print_stats(result)
    else:
        _print_summary(result)


if __name__ == "__main__":
    main()
