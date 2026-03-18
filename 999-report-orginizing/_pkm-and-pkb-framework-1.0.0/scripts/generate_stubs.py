#!/usr/bin/env python3
"""
generate_stubs.py — Stub Note Generator for Missing Wiki-Link Targets
═══════════════════════════════════════════════════════════════════════════════
Creates minimal "stub" permanent notes for concepts referenced by existing
permanent notes but that have no corresponding file. This closes wiki-link
gaps and improves vault connectivity.

WORKFLOW:
  1. Runs audit_notes.run_audit() to discover missing concepts
  2. Categorizes each missing concept (concept, person, domain, tool, expansion)
  3. Generates a stub note with proper frontmatter + back-links
  4. Dry-run by default — pass --execute to write files

USAGE:
  python scripts/generate_stubs.py                   # Dry-run, show plan
  python scripts/generate_stubs.py --execute          # Write stubs to disk
  python scripts/generate_stubs.py --min-refs 15      # Only concepts with 15+ refs
  python scripts/generate_stubs.py --category concept # Only concept stubs
  python scripts/generate_stubs.py --list             # List all missing, categorized

REQUIRES: Python 3.10+ (stdlib only)
"""

import re
import sys
import argparse
from pathlib import Path
from datetime import date
from collections import defaultdict

# Ensure scripts/ is on the path for sibling imports
sys.path.insert(0, str(Path(__file__).parent))

from audit_notes import run_audit, AuditResult
from config import OUTPUT_DIR, MAX_FILENAME_LENGTH


# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

TODAY = date.today().isoformat()

# ── Category Detection ─────────────────────────────────────────────────────

# Known tool/platform names (case-insensitive matching)
TOOL_NAMES = {
    "dataview", "canvas", "obsidian", "anki", "obsidian dataview",
    "dataview plugin", "templater", "quickadd", "meta bind", "excalidraw",
    "notion", "roam research", "logseq", "zotero", "readwise",
    "hypothes.is", "hypothesis",
}

# Known broad domain/field names (exact match, case-insensitive)
DOMAIN_NAMES = {
    "educational psychology", "educational philosophy", "cognitive science",
    "knowledge management", "educational technology affordances",
    "information science", "behavioral science", "educational science",
    "educational data mining", "ecological psychology", "phenomenology",
    "pragmatism", "neuroscience", "epistemology", "philosophy",
    "linguistics", "mathematics", "systems thinking", "decision science",
    "computer science", "social psychology", "developmental psychology",
    "cognitive psychology", "learning science", "instructional design",
    "motivation research", "metacognition", "network science",
    "ontology (knowledge)", "philosophy of mind",
}

# Person name heuristics
PERSON_FIRST_NAMES = {
    "david", "john", "jean", "robert", "alfred", "charles", "james",
    "william", "richard", "carl", "george", "albert", "paul", "lev",
    "etienne", "edgar", "donald", "howard", "jerome", "noam",
    "benjamin", "daniel", "michael", "peter", "jack", "stewart",
    "gordon", "ellen", "barbara", "carol", "ann", "linda", "susan",
    "lawrence", "thomas", "karl", "hermann", "max", "ernst", "hans",
    "frederick", "frederic", "friedrich", "alexander", "barry", "dale",
    "gregory", "keith", "philip", "roger", "ronald", "stephen",
    "terry", "henry", "joseph", "mark", "brian", "chris", "christopher",
    "martin", "nelson", "patricia",
}

# Pattern for "Lastname, Firstname..." or "Firstname and Firstname"
_PERSON_COMMA_PAT = re.compile(r'^[A-Z][a-z]+,\s+[A-Z]')
_PERSON_AND_PAT = re.compile(r'^[A-Z][a-z]+ (?:and|&) [A-Z][a-z]+')

# Expansion topic heuristic: long title with colon or em-dash
EXPANSION_MIN_LENGTH = 60


# ══════════════════════════════════════════════════════════════════════════════
# CATEGORY DETECTION
# ══════════════════════════════════════════════════════════════════════════════

def categorize(name: str) -> str:
    """
    Classify a missing concept into one of:
      concept, person, domain, tool, expansion, skip
    """
    lower = name.lower().strip()

    # 0. Skip pure numbers/years
    if re.fullmatch(r'\d{1,4}', name.strip()):
        return "skip"

    # 0b. Skip corrupted wiki-link targets (contain YAML fragments)
    if any(frag in lower for frag in ['priority:', 'aliases:', '\n', 'topic:']):
        return "skip"

    # 1. Tool check (exact match)
    if lower in TOOL_NAMES:
        return "tool"

    # 2. Domain check (exact match)
    if lower in DOMAIN_NAMES:
        return "domain"

    # 3. Expansion topic check (long title with structural punctuation)
    if len(name) >= EXPANSION_MIN_LENGTH and (":" in name or "—" in name):
        return "expansion"

    # 4. Person check
    #    a) "Collins, Brown, and Newman" pattern
    if _PERSON_COMMA_PAT.match(name):
        return "person"
    #    b) "David Ausubel" pattern — first word is a known first name
    words = name.split()
    if len(words) >= 2:
        first_lower = words[0].lower()
        # Check if first word is a known first name AND second word is
        # capitalized (surname) AND the name is short-ish (< 5 words)
        if (first_lower in PERSON_FIRST_NAMES
                and words[1][0].isupper()
                and len(words) <= 5):
            return "person"

    # 5. Multi-word academic phrases that look like person attributions
    #    e.g., "Zimmerman SRL Model", "Baddeley's Working Memory Model"
    if "'s " in name and len(words) <= 6:
        return "person"

    # Default: concept
    return "concept"


# ══════════════════════════════════════════════════════════════════════════════
# FILENAME GENERATION (reused from note_builder)
# ══════════════════════════════════════════════════════════════════════════════

def sanitize_filename(name: str) -> str:
    """Convert a concept name to a safe, Obsidian-compatible filename."""
    safe = re.sub(r'[<>:"/\\|?*\[\]()]', '', name)
    safe = re.sub(r'[\s_]+', '-', safe)
    safe = re.sub(r'-{2,}', '-', safe)
    safe = safe.strip('-')
    if len(safe) > MAX_FILENAME_LENGTH:
        safe = safe[:MAX_FILENAME_LENGTH].rstrip('-')
    return safe


# ══════════════════════════════════════════════════════════════════════════════
# STUB NOTE BUILDER
# ══════════════════════════════════════════════════════════════════════════════

def _build_aliases(name: str) -> list[str]:
    """Generate useful aliases for a stub note."""
    aliases = {name}

    # Split on em-dash
    if "—" in name:
        for part in name.split("—"):
            clean = part.strip()
            if clean and len(clean) > 3:
                aliases.add(clean)

    # Split on colon
    if ":" in name:
        pre_colon = name.split(":")[0].strip()
        if pre_colon and len(pre_colon) > 3:
            aliases.add(pre_colon)

    # Split on slash
    if "/" in name:
        for part in name.split("/"):
            clean = part.strip()
            if clean and len(clean) > 3:
                aliases.add(clean)

    return sorted(aliases)


def _infer_domain(name: str, category: str) -> str:
    """Best-effort domain inference from concept name."""
    lower = name.lower()

    domain_clues = {
        "cognitive-psychology": [
            "cognitive", "memory", "schema", "working memory", "attention",
            "dual process", "metacognit", "thinking", "reasoning",
            "dunning", "kruger", "calibration", "bias", "heuristic",
            "bayesian", "dual-process",
        ],
        "educational-psychology": [
            "learning", "pedagog", "heutagog", "andragog", "instructional",
            "motivation", "self-regulat", "feedback", "assessment",
            "scaffolding", "zone of proximal", "zpd", "curriculum",
            "teaching", "student", "learner", "competenc", "autonom",
            "apprentice", "situated", "communit", "practice",
            "capability", "mastery", "self-determin", "srl",
            "zimmerman", "jonassen", "baddeley", "kolb",
        ],
        "philosophy": [
            "epistemolog", "ontolog", "dialectic", "hermeneutic",
            "phenomenolog", "pragmati", "socratic", "ethics", "moral",
            "philosophical", "philosophy", "hegelian", "thesis",
            "antithesis", "synthesis", "aporia", "epistemic",
            "argumentation", "whitehead",
        ],
        "learning-science": [
            "pkm", "pkb", "knowledge manage", "zettelkasten", "note-",
            "knowledge graph", "knowledge base", "information",
            "spaced repetition", "retrieval practice", "elaborat",
            "flashcard", "anki", "review", "interleav",
        ],
        "neuroscience": [
            "neural", "brain", "hippocamp", "amygdala", "cortex",
            "neuroplastic", "synaptic", "neuroscien",
        ],
        "systems-thinking": [
            "system", "complex", "emergence", "network", "feedback loop",
            "activity theory",
        ],
    }

    for domain, clues in domain_clues.items():
        if any(clue in lower for clue in clues):
            return domain

    return "other"


def build_stub_note(
    name: str,
    category: str,
    source_notes: set[str],
    domain: str,
) -> str:
    """
    Build a complete stub note for a missing concept.

    Returns the full markdown string ready to write.
    """
    aliases = _build_aliases(name)
    alias_yaml = "\n".join(f'  - "{a}"' for a in aliases)

    # Tags based on category
    category_tag = {
        "concept": "concept-stub",
        "person": "person-stub",
        "domain": "domain-stub",
        "tool": "tool-stub",
        "expansion": "expansion-topic-stub",
    }.get(category, "concept-stub")

    # Source notes sorted and limited
    sorted_sources = sorted(source_notes)
    backlinks_display = sorted_sources[:20]
    remaining = len(sorted_sources) - len(backlinks_display)

    # Build see-also from source notes (their filenames as wiki-links)
    see_also_yaml = "\n".join(
        f'  - "[[{s}]]"' for s in sorted_sources[:10]
    )

    # Category-specific callout
    if category == "person":
        callout = (
            f'> [!definition] **{name}**\n'
            f'> *Stub note — person referenced by {len(source_notes)} permanent notes. '
            f'Expand with biographical context, key contributions, '
            f'and theoretical significance.*'
        )
    elif category == "domain":
        callout = (
            f'> [!definition] **{name}**\n'
            f'> *Stub note — academic domain/field referenced by {len(source_notes)} '
            f'permanent notes. Expand with scope, key theories, foundational '
            f'thinkers, and relationship to PKM practice.*'
        )
    elif category == "tool":
        callout = (
            f'> [!definition] **{name}**\n'
            f'> *Stub note — tool/platform referenced by {len(source_notes)} permanent '
            f'notes. Expand with purpose, key features, and PKB integration patterns.*'
        )
    elif category == "expansion":
        callout = (
            f'> [!definition] **{name}**\n'
            f'> *Stub note — expansion topic suggested for future research, referenced '
            f'by {len(source_notes)} permanent notes. This represents a potential '
            f'deep-dive area connecting multiple concepts in the PKB.*'
        )
    else:
        callout = (
            f'> [!definition] **{name}**\n'
            f'> *Stub note — concept referenced by {len(source_notes)} permanent notes. '
            f'Expand with formal definition, theoretical context, and PKM implications.*'
        )

    # Backlinks section
    backlinks_md = "\n".join(f"- [[{s}]]" for s in backlinks_display)
    if remaining > 0:
        backlinks_md += f"\n- *...and {remaining} more permanent notes*"

    note = f"""---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "{name.replace('"', "'")}"
aliases:
{alias_yaml}
type: permanent-note
status: seedling
confidence: low

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
  - permanent-note
  - seedling
  - {category_tag}
  - {domain}

domain: {domain}

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: {TODAY}
updated: {TODAY}

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: stub-generation
extraction-method: "generate-stubs-v1 (auto-generated from wiki-link audit)"
referenced-by-count: {len(source_notes)}

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
see-also:
{see_also_yaml}

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: {"high" if len(source_notes) >= 20 else "medium" if len(source_notes) >= 10 else "low"}
---

# {name}

{callout}

*Auto-generated stub — referenced by {len(source_notes)} permanent notes.*

## Referenced By

{backlinks_md}
"""
    return note


# ══════════════════════════════════════════════════════════════════════════════
# STUB PLAN (dry run data structure)
# ══════════════════════════════════════════════════════════════════════════════

class StubPlan:
    """One planned stub note."""
    def __init__(self, name: str, category: str, domain: str,
                 sources: set[str], filename: str, filepath: Path):
        self.name = name
        self.category = category
        self.domain = domain
        self.sources = sources
        self.ref_count = len(sources)
        self.filename = filename
        self.filepath = filepath


def build_stub_plans(
    audit: AuditResult,
    notes_dir: Path,
    min_refs: int = 1,
    categories: set[str] | None = None,
) -> list[StubPlan]:
    """
    Build a list of StubPlan objects from the audit's missing concepts.

    Args:
        audit:      AuditResult from run_audit()
        notes_dir:  Directory where stubs will be created
        min_refs:   Minimum number of referencing notes to generate a stub
        categories: If set, only generate stubs for these categories
    """
    plans: list[StubPlan] = []
    existing_files = {f.stem.lower() for f in notes_dir.glob('*.md')}

    for target, sources in audit.missing_concepts.items():
        if len(sources) < min_refs:
            continue

        cat = categorize(target)
        if cat == "skip":
            continue
        if categories and cat not in categories:
            continue

        domain = _infer_domain(target, cat)
        fname = sanitize_filename(target)

        # Skip if file already exists (from a prior run, or name collision)
        if fname.lower() in existing_files:
            continue

        filepath = notes_dir / f"{fname}.md"
        plans.append(StubPlan(target, cat, domain, sources, fname, filepath))

    # Sort by reference count (highest first)
    plans.sort(key=lambda p: p.ref_count, reverse=True)
    return plans


# ══════════════════════════════════════════════════════════════════════════════
# EXECUTION
# ══════════════════════════════════════════════════════════════════════════════

def execute_plans(plans: list[StubPlan], dry_run: bool = True) -> dict:
    """
    Write stub notes to disk (or simulate in dry-run mode).

    Returns summary dict with counts.
    """
    summary = {
        "total": len(plans),
        "written": 0,
        "skipped": 0,
        "errors": [],
        "by_category": defaultdict(int),
    }

    for plan in plans:
        summary["by_category"][plan.category] += 1

        if dry_run:
            continue

        try:
            content = build_stub_note(
                plan.name, plan.category, plan.sources, plan.domain
            )
            plan.filepath.write_text(content, encoding='utf-8')
            summary["written"] += 1
        except Exception as e:
            summary["errors"].append(f"{plan.filename}: {e}")
            summary["skipped"] += 1

    return summary


# ══════════════════════════════════════════════════════════════════════════════
# REPORTING
# ══════════════════════════════════════════════════════════════════════════════

def print_plan_report(plans: list[StubPlan], summary: dict,
                      dry_run: bool) -> None:
    """Print a formatted report of the stub generation plan/execution."""
    mode = "DRY RUN" if dry_run else "EXECUTED"
    print('=' * 72)
    print(f'  STUB NOTE GENERATOR -- {mode}')
    print('=' * 72)

    # Category breakdown
    print(f"\n  Total stubs planned: {summary['total']}")
    print(f"  Stubs by category:")
    for cat in ["concept", "person", "domain", "tool", "expansion"]:
        count = summary["by_category"].get(cat, 0)
        if count:
            print(f"    {cat:15s}: {count:>4}")

    if not dry_run:
        print(f"\n  Written: {summary['written']}")
        if summary['errors']:
            print(f"  Errors:  {len(summary['errors'])}")
            for err in summary['errors'][:10]:
                print(f"    x {err}")

    # Top 50 stubs
    print(f"\n{'-' * 72}")
    print(f"  {'Refs':>4}  {'Category':12s}  {'Domain':24s}  Name")
    print(f"{'-' * 72}")
    for plan in plans[:50]:
        print(f"  {plan.ref_count:>4}  {plan.category:12s}  {plan.domain:24s}  {plan.name[:50]}")
    if len(plans) > 50:
        print(f"  ... and {len(plans) - 50} more")

    print(f"\n{'=' * 72}")
    if dry_run:
        print("  Pass --execute to write these stubs to disk.")
    print()


def print_list_report(plans: list[StubPlan]) -> None:
    """Print a detailed list of all planned stubs."""
    print(f"\n{'=' * 72}")
    print(f"  ALL MISSING CONCEPTS -- CATEGORIZED ({len(plans)} total)")
    print(f"{'=' * 72}\n")

    by_cat = defaultdict(list)
    for p in plans:
        by_cat[p.category].append(p)

    for cat in ["concept", "person", "domain", "tool", "expansion"]:
        items = by_cat.get(cat, [])
        if not items:
            continue
        print(f"  -- {cat.upper()} ({len(items)}) --------------------------------")
        for p in items:
            print(f"    {p.ref_count:>3} refs | {p.domain:24s} | {p.name[:60]}")
        print()


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Generate stub notes for missing wiki-link targets"
    )
    parser.add_argument(
        "--execute", action="store_true",
        help="Write stubs to disk (default: dry run only)"
    )
    parser.add_argument(
        "--min-refs", type=int, default=5,
        help="Minimum number of referencing notes (default: 5)"
    )
    parser.add_argument(
        "--category", type=str, default=None,
        choices=["concept", "person", "domain", "tool", "expansion"],
        help="Only generate stubs for this category"
    )
    parser.add_argument(
        "--list", action="store_true",
        help="List all missing concepts categorized (no generation)"
    )
    parser.add_argument(
        "--notes-dir", type=str, default=None,
        help="Override notes directory path"
    )
    args = parser.parse_args()

    notes_dir = Path(args.notes_dir) if args.notes_dir else OUTPUT_DIR

    print(f"\nRunning audit on {notes_dir} ...")
    audit = run_audit(notes_dir)
    print(f"Found {len(audit.missing_concepts)} missing concepts.\n")

    cat_filter = {args.category} if args.category else None
    plans = build_stub_plans(
        audit, notes_dir,
        min_refs=args.min_refs,
        categories=cat_filter,
    )

    if args.list:
        # For --list, show everything regardless of min_refs
        all_plans = build_stub_plans(audit, notes_dir, min_refs=1)
        print_list_report(all_plans)
        return

    if not plans:
        print(f"No stubs to generate with min-refs={args.min_refs}.")
        return

    summary = execute_plans(plans, dry_run=not args.execute)
    print_plan_report(plans, summary, dry_run=not args.execute)


if __name__ == "__main__":
    main()
