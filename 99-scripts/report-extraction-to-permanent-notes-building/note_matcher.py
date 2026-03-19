"""
note_matcher.py  -- Match Extracted Candidates to Existing Permanent Notes
===============================================================================
Builds an index of existing permanent notes (by filename stem, aliases, and
title frontmatter) then matches incoming NoteCandidate objects against them
using exact, alias, and fuzzy matching strategies.

REQUIRES: Python 3.10+ (stdlib only  -- uses difflib for fuzzy matching)
USAGE:
    from note_matcher import NoteMatcher

    matcher = NoteMatcher(permanent_notes_dir)
    matches = matcher.match_candidates(candidates)
"""

from __future__ import annotations

import re
import yaml
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Optional

from config import PERMANENT_NOTES_DIR, FUZZY_MATCH_THRESHOLD, MAX_FUZZY_CANDIDATES
from report_parser import NoteCandidate


# ==============================================================================
# DATA CLASSES
# ==============================================================================

@dataclass
class NoteIndex:
    """Index entry for a single existing permanent note."""
    filepath: Path
    stem: str           # filename without .md, lowercase
    title: str          # from frontmatter title field
    aliases: list[str]  # from frontmatter aliases array
    source_reports: list[str]  # from frontmatter source-reports

    @property
    def all_names(self) -> list[str]:
        """All name variants for this note (stem, title, aliases), lowercased."""
        names = [self.stem]
        if self.title:
            names.append(self.title.lower())
        names.extend(a.lower() for a in self.aliases)
        return list(set(names))


@dataclass
class MatchResult:
    """Result of matching a single candidate."""
    candidate: NoteCandidate
    match_type: str         # "exact" | "alias" | "fuzzy" | "none"
    matched_note: Optional[NoteIndex] = None
    match_score: float = 0.0
    fuzzy_suggestions: list[tuple[NoteIndex, float]] = field(default_factory=list)


@dataclass
class MatchReport:
    """Aggregated result of matching all candidates."""
    matched: list[MatchResult] = field(default_factory=list)
    unmatched: list[MatchResult] = field(default_factory=list)
    skipped_duplicates: list[tuple[str, str]] = field(default_factory=list)

    @property
    def match_rate(self) -> float:
        total = len(self.matched) + len(self.unmatched)
        return len(self.matched) / total if total > 0 else 0.0


# ==============================================================================
# YAML FRONTMATTER PARSER
# ==============================================================================

_FRONTMATTER_RE = re.compile(r'^---\s*\n(.*?)\n---', re.DOTALL)


def _parse_frontmatter(filepath: Path) -> dict:
    """
    Extract YAML frontmatter from a markdown file.

    Handles the comment-style section headers in the PKB's YAML
    (lines starting with # inside frontmatter are YAML comments).
    """
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}

    m = _FRONTMATTER_RE.match(text)
    if not m:
        return {}

    yaml_text = m.group(1)

    try:
        data = yaml.safe_load(yaml_text)
        return data if isinstance(data, dict) else {}
    except yaml.YAMLError:
        # Fall back to manual parsing for files with complex YAML
        return _manual_parse_frontmatter(yaml_text)


def _manual_parse_frontmatter(yaml_text: str) -> dict:
    """
    Simplified manual parser for frontmatter fields we care about:
    title, aliases, source-reports.
    """
    result: dict = {}
    lines = yaml_text.split("\n")
    current_key = ""
    current_list: list[str] = []

    for line in lines:
        stripped = line.strip()

        # Skip YAML comments and section dividers
        if stripped.startswith("#") or stripped.startswith("="):
            continue

        # Key-value pair
        kv_match = re.match(r'^(\S[\w-]+)\s*:\s*(.*)', line)
        if kv_match:
            # Save previous list if any
            if current_key and current_list:
                result[current_key] = current_list
                current_list = []

            key = kv_match.group(1)
            value = kv_match.group(2).strip()

            if value and not value.startswith("["):
                # Simple string value  -- strip quotes
                result[key] = value.strip('"').strip("'")
                current_key = key
            elif value.startswith("[") and value.endswith("]"):
                # Inline array
                inner = value[1:-1]
                result[key] = [
                    v.strip().strip('"').strip("'")
                    for v in inner.split(",") if v.strip()
                ]
                current_key = key
            else:
                current_key = key
                current_list = []
            continue

        # List item under current key
        list_match = re.match(r'^\s+-\s+(.*)', line)
        if list_match and current_key:
            val = list_match.group(1).strip().strip('"').strip("'")
            current_list.append(val)

    # Save final list
    if current_key and current_list:
        result[current_key] = current_list

    return result


# ==============================================================================
# NOTE INDEX BUILDER
# ==============================================================================

def build_note_index(notes_dir: Path) -> list[NoteIndex]:
    """
    Build an index of all existing permanent notes from a directory.

    Reads each .md file, extracts frontmatter title, aliases, and
    source-reports for matching purposes.
    """
    index: list[NoteIndex] = []

    if not notes_dir.exists():
        return index

    for md_file in sorted(notes_dir.glob("*.md")):
        fm = _parse_frontmatter(md_file)
        stem = md_file.stem.lower()

        title = fm.get("title", "")
        if isinstance(title, str):
            title = title.strip('"').strip("'")
        else:
            title = ""

        aliases_raw = fm.get("aliases", [])
        if isinstance(aliases_raw, list):
            aliases = [str(a).strip('"').strip("'") for a in aliases_raw if a]
        elif isinstance(aliases_raw, str):
            aliases = [aliases_raw] if aliases_raw else []
        else:
            aliases = []

        source_reports_raw = fm.get("source-reports", [])
        if isinstance(source_reports_raw, list):
            source_reports = [str(s) for s in source_reports_raw if s]
        elif isinstance(source_reports_raw, str):
            source_reports = [source_reports_raw] if source_reports_raw else []
        else:
            source_reports = []

        index.append(NoteIndex(
            filepath=md_file,
            stem=stem,
            title=title,
            aliases=aliases,
            source_reports=source_reports,
        ))

    return index


# ==============================================================================
# NORMALIZATION
# ==============================================================================

def _normalize(name: str) -> str:
    """
    Normalize a concept name for matching.

    Strips wiki-link brackets, lowercases, normalizes whitespace and hyphens.
    'Cognitive Load Theory' -> 'cognitive load theory'
    '[[Cognitive-Load-Theory]]' -> 'cognitive load theory'
    """
    # Strip wiki-link brackets
    name = re.sub(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', r'\1', name)
    # Replace hyphens with spaces
    name = name.replace("-", " ")
    # Normalize whitespace
    name = re.sub(r'\s+', ' ', name).strip().lower()
    return name


def _stem_normalize(name: str) -> str:
    """
    Normalize to filename-stem format.

    'Cognitive Load Theory' -> 'cognitive-load-theory'
    """
    normalized = _normalize(name)
    return normalized.replace(" ", "-")


# ==============================================================================
# MATCHER
# ==============================================================================

class NoteMatcher:
    """
    Matches NoteCandidate objects to existing permanent notes.

    Matching strategies (in priority order):
    1. EXACT: candidate concept_name stem matches note filename stem
    2. ALIAS: candidate concept_name matches a note's alias or title
    3. FUZZY: difflib.SequenceMatcher ratio exceeds threshold
    """

    def __init__(
        self,
        notes_dir: Optional[Path] = None,
        threshold: float = FUZZY_MATCH_THRESHOLD,
    ):
        self.notes_dir = notes_dir or PERMANENT_NOTES_DIR
        self.threshold = threshold
        self.index = build_note_index(self.notes_dir)

        # Build lookup maps
        self._stem_map: dict[str, NoteIndex] = {}
        self._name_map: dict[str, NoteIndex] = {}

        for entry in self.index:
            # Map by stem
            self._stem_map[entry.stem] = entry

            # Map by all name variants
            for name in entry.all_names:
                norm = _normalize(name)
                if norm and norm not in self._name_map:
                    self._name_map[norm] = entry

    def _exact_match(self, concept_name: str) -> Optional[NoteIndex]:
        """Try exact match on filename stem."""
        stem = _stem_normalize(concept_name)
        return self._stem_map.get(stem)

    def _alias_match(self, concept_name: str) -> Optional[NoteIndex]:
        """Try matching against title and aliases."""
        norm = _normalize(concept_name)
        return self._name_map.get(norm)

    def _fuzzy_match(self, concept_name: str) -> list[tuple[NoteIndex, float]]:
        """Find fuzzy matches above threshold, sorted by score descending."""
        norm = _normalize(concept_name)
        scores: list[tuple[NoteIndex, float]] = []

        for entry in self.index:
            best_score = 0.0
            for name in entry.all_names:
                entry_norm = _normalize(name)
                ratio = SequenceMatcher(None, norm, entry_norm).ratio()
                best_score = max(best_score, ratio)

            if best_score >= self.threshold:
                scores.append((entry, best_score))

        scores.sort(key=lambda x: -x[1])
        return scores[:MAX_FUZZY_CANDIDATES]

    def match_single(self, candidate: NoteCandidate) -> MatchResult:
        """Match a single candidate against the note index."""
        concept = candidate.concept_name

        # Strategy 1: Exact stem match
        exact = self._exact_match(concept)
        if exact:
            return MatchResult(
                candidate=candidate,
                match_type="exact",
                matched_note=exact,
                match_score=1.0,
            )

        # Strategy 2: Alias/title match
        alias = self._alias_match(concept)
        if alias:
            return MatchResult(
                candidate=candidate,
                match_type="alias",
                matched_note=alias,
                match_score=0.95,
            )

        # Strategy 3: Fuzzy match
        fuzzy = self._fuzzy_match(concept)
        if fuzzy and fuzzy[0][1] >= self.threshold:
            return MatchResult(
                candidate=candidate,
                match_type="fuzzy",
                matched_note=fuzzy[0][0],
                match_score=fuzzy[0][1],
                fuzzy_suggestions=fuzzy,
            )

        # No match
        return MatchResult(
            candidate=candidate,
            match_type="none",
            fuzzy_suggestions=fuzzy,  # include near-misses for reporting
        )

    def match_candidates(self, candidates: list[NoteCandidate]) -> MatchReport:
        """
        Match a list of candidates, deduplicating by concept name.

        When multiple candidates share the same concept_name, they are
        matched once to the same note  -- the pipeline's updater handles
        merging content from multiple source reports.
        """
        report = MatchReport()
        seen: dict[str, MatchResult] = {}  # normalized_name -> result

        for candidate in candidates:
            norm_key = _normalize(candidate.concept_name)

            if norm_key in seen:
                # Already matched this concept  -- record as duplicate
                report.skipped_duplicates.append(
                    (candidate.concept_name, candidate.source_report)
                )
                # Still include it in the appropriate bucket so the updater
                # can merge all source data
                existing = seen[norm_key]
                if existing.match_type != "none":
                    report.matched.append(MatchResult(
                        candidate=candidate,
                        match_type=existing.match_type,
                        matched_note=existing.matched_note,
                        match_score=existing.match_score,
                    ))
                else:
                    report.unmatched.append(MatchResult(
                        candidate=candidate,
                        match_type="none",
                    ))
                continue

            result = self.match_single(candidate)
            seen[norm_key] = result

            if result.match_type != "none":
                report.matched.append(result)
            else:
                report.unmatched.append(result)

        return report


# ==============================================================================
# CLI
# ==============================================================================

def main() -> None:
    import sys
    from scan_extractions import scan_all_batches

    print("Building note index...")
    matcher = NoteMatcher()
    print(f"  Indexed {len(matcher.index)} existing permanent notes\n")

    print("Scanning extraction batches...")
    scan = scan_all_batches()
    candidates = scan.all_candidates
    print(f"  Found {len(candidates)} candidates across {len(scan.all_json_files)} files\n")

    print("Matching candidates to existing notes...")
    report = matcher.match_candidates(candidates)

    # Summary
    print("\n" + "=" * 72)
    print("MATCHING REPORT")
    print("=" * 72)
    print(f"  Total candidates:     {len(candidates)}")
    print(f"  Matched (update):     {len(report.matched)}")
    print(f"  Unmatched (create):   {len(report.unmatched)}")
    print(f"  Skipped duplicates:   {len(report.skipped_duplicates)}")
    print(f"  Match rate:           {report.match_rate:.1%}")

    # Match type breakdown
    type_counts: dict[str, int] = {}
    for m in report.matched:
        type_counts[m.match_type] = type_counts.get(m.match_type, 0) + 1
    if type_counts:
        print(f"\n  Match types:")
        for mtype, count in sorted(type_counts.items(), key=lambda x: -x[1]):
            print(f"    {mtype:>8}: {count}")

    # Show unmatched with near-misses
    if "--unmatched" in sys.argv:
        print(f"\n{'-' * 72}")
        print("UNMATCHED CANDIDATES:")
        for result in report.unmatched[:50]:
            concept = result.candidate.concept_name
            source = result.candidate.source_report
            near = ""
            if result.fuzzy_suggestions:
                best = result.fuzzy_suggestions[0]
                near = f"  (near: {best[0].stem} @ {best[1]:.2f})"
            print(f"  {concept} ← {source}{near}")

    print("=" * 72)


if __name__ == "__main__":
    main()
