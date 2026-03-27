"""
config.py — Configuration for the Permanent Notes Generator
═══════════════════════════════════════════════════════════════════════════════
All paths, constants, callout mappings, and customizable settings in one place.
Edit this file to adapt the generator to your vault layout and conventions.

REQUIRES: Python 3.10+
"""

from pathlib import Path

# ══════════════════════════════════════════════════════════════════════════════
# PATHS
# ══════════════════════════════════════════════════════════════════════════════

PROJECT_ROOT = Path(__file__).parent.parent  # _pkm-and-pkb-framework-1.0.0/
JSON_DIR = PROJECT_ROOT / "extraction-material" / "json"
REPORT_DIR = PROJECT_ROOT / "report-series"
OUTPUT_DIR = PROJECT_ROOT / "_permanent-notes"

# ══════════════════════════════════════════════════════════════════════════════
# V2 PATHS — Update Pipeline
# ══════════════════════════════════════════════════════════════════════════════
# These are absolute paths for the update pipeline which operates across
# multiple extraction batches, not just the original PKM framework series.

VAULT_ROOT = Path(r"D:\10_pur3v4d3r's-vault")
SCRIPTS_DIR = VAULT_ROOT / "99-scripts" / "report-extraction-to-permanent-notes-building"

# Where existing permanent notes live (the notes we want to UPDATE)
PERMANENT_NOTES_DIR = (
    VAULT_ROOT / "999-report-orginizing"
    / "_permanent-notes" / "_permanent-notes"
)

# Extraction batch directories — each contains *_extracted.json files
EXTRACTOR_OUTPUT_ROOT = VAULT_ROOT / "999-report-orginizing" / "_extractor-output"

# Auto-discover all extraction batch directories (no more manual list)
# Add directory names here to exclude specific batches from processing.
BATCH_EXCLUDES = set()  # e.g. {"2026-03-13-test-batch"}

EXTRACTION_BATCHES = sorted(
    d for d in (EXTRACTOR_OUTPUT_ROOT.iterdir() if EXTRACTOR_OUTPUT_ROOT.exists() else [])
    if d.is_dir() and not d.name.startswith(".") and d.name not in BATCH_EXCLUDES
)

# Original 30-report batch (already processed by v1 pipeline)
ORIGINAL_JSON_DIR = (
    VAULT_ROOT / "999-report-orginizing"
    / "_pkm-and-pkb-framework-1.0.0" / "extraction-material" / "json"
)

# Output for pipeline logs and reports
PIPELINE_OUTPUT_DIR = SCRIPTS_DIR / "_pipeline-output"

# ══════════════════════════════════════════════════════════════════════════════
# MATCHING SETTINGS
# ══════════════════════════════════════════════════════════════════════════════

FUZZY_MATCH_THRESHOLD = 0.85  # SequenceMatcher ratio threshold for fuzzy match
MAX_FUZZY_CANDIDATES = 5      # How many fuzzy suggestions to show in reports

# ══════════════════════════════════════════════════════════════════════════════
# CALLOUT TYPES THAT GENERATE PERMANENT NOTES
# ══════════════════════════════════════════════════════════════════════════════
# Each callout of these types produces one permanent note per instance.
# Add "key-claim" here if you also want key claims as standalone notes.

NOTE_GENERATING_CALLOUTS = ["definition", "original-synthesis", "framework-profile"]

# ══════════════════════════════════════════════════════════════════════════════
# SUPPORTING CALLOUT TYPES (enrich notes but don't generate them)
# ══════════════════════════════════════════════════════════════════════════════

EVIDENCE_CALLOUTS = ["evidence", "what-the-evidence-suggests", "cite"]
INSIGHT_CALLOUTS = [
    "analytical-insight", "key-claim",
    "assumption-challenge", "steel-man", "comparative-finding", "tension-identified",
]
CONNECTION_CALLOUTS = ["cross-domain-connection", "connections-and-links"]
PRACTICE_CALLOUTS = ["best-practice"]
EXPANSION_CALLOUTS = ["topic-idea", "further-exploration"]
WARNING_CALLOUTS = ["warning"]
REFLECTION_CALLOUTS = ["reflection", "ask-yourself-this"]

# ══════════════════════════════════════════════════════════════════════════════
# ENHANCED REPORT CONTENT CALLOUT TYPES (v2.1 — new report generator output)
# ══════════════════════════════════════════════════════════════════════════════
# These callout types appear in the enhanced report generators (Dialectical
# Re-Examination v2, Focused Analysis v1.1) and were not previously extracted.

FLASHCARD_CALLOUTS = ["flashcard"]
PERSON_CALLOUTS = ["person"]
TENSION_CALLOUTS = ["tension", "tension-identified"]
OPEN_QUESTION_CALLOUTS = ["open-question"]
PROTOCOL_CALLOUTS = ["protocol"]
DIAGRAM_CALLOUTS = ["diagram"]
NAVIGATION_CALLOUTS = ["navigation"]
QUALITY_ASSESSMENT_CALLOUTS = ["quality-assessment"]
METHODOLOGY_CALLOUTS = ["methodology-and-sources"]
CITATION_CALLOUTS = ["cite", "citation"]

# ══════════════════════════════════════════════════════════════════════════════
# DOMAIN MAPPING
# ══════════════════════════════════════════════════════════════════════════════
# Maps domain strings found in definition callout titles (and report frontmatter)
# to the permanent note template's standardized domain slugs.

DOMAIN_MAP = {
    # Raw text forms (from callout titles)
    "cognitive psychology": "cognitive-psychology",
    "educational philosophy": "educational-psychology",
    "educational psychology": "educational-psychology",
    "philosophy": "philosophy",
    "neuroscience": "neuroscience",
    "information science": "learning-science",
    "knowledge management": "learning-science",
    "library science": "learning-science",
    "cognitive science": "cognitive-psychology",
    "epistemology": "epistemology",
    "linguistics": "linguistics",
    "mathematics": "mathematics",
    "systems thinking": "systems-thinking",
    "decision science": "decision-science",
    "computer science": "computer-science",
    "prompt engineering": "prompt-engineering",
    "novel synthesis": "cognitive-psychology",
    "meta-analysis": "learning-science",
    "learning science": "learning-science",
    "developmental psychology": "educational-psychology",
    "social psychology": "cognitive-psychology",
    "motivation research": "educational-psychology",
    "instructional design": "educational-psychology",
    "self-regulated learning": "educational-psychology",
    "metacognition": "cognitive-psychology",
    "network science": "systems-thinking",
    # Slugified forms (from report frontmatter primary_domain)
    "cognitive-psychology": "cognitive-psychology",
    "educational-psychology": "educational-psychology",
    "knowledge-management": "learning-science",
    "information-science": "learning-science",
    "learning-science": "learning-science",
    "systems-thinking": "systems-thinking",
    "decision-science": "decision-science",
    "computer-science": "computer-science",
    "prompt-engineering": "prompt-engineering",
    "instructional-design": "educational-psychology",
    "psychology-of-learning": "cognitive-psychology",
    "learning-experience-design": "educational-psychology",
}

# Valid domain values (from the permanent-note-template.md)
VALID_DOMAINS = [
    "cognitive-psychology", "educational-psychology", "philosophy", "neuroscience",
    "prompt-engineering", "computer-science", "decision-science", "epistemology",
    "learning-science", "linguistics", "mathematics", "systems-thinking", "other",
]

# ══════════════════════════════════════════════════════════════════════════════
# COMPLEXITY MAPPING
# ══════════════════════════════════════════════════════════════════════════════
# Maps report knowledge_level values to permanent note complexity-level values.

KNOWLEDGE_LEVEL_TO_COMPLEXITY = {
    "introductory": "foundational",
    "intermediate": "intermediate",
    "advanced": "advanced-practitioner",
    "expert": "expert",
    "developing": "intermediate",
    "established": "advanced-practitioner",
}

# ══════════════════════════════════════════════════════════════════════════════
# DEDICATED AGGREGATE NOTE CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════
# The dedicated notes builder (dedicated_notes_builder.py) aggregates specific
# callout types from ALL extraction batches into four master index notes.

DEDICATED_NOTE_FILES = {
    "definitions": "_Master-Definition-Index.md",
    "references":  "_Master-Reference-Index.md",
    "connections":  "_Master-PKB-Connections-Index.md",
    "expansions":  "_Master-Expansion-Topics-Index.md",
}

# Callout types feeding each dedicated note
DEDICATED_DEFINITION_CALLOUTS = ["definition"]
DEDICATED_REFERENCE_CALLOUTS = ["cite", "citation", "references", "bibliography"]
DEDICATED_CONNECTION_CALLOUTS = ["connections-and-links", "connection-ideas", "connections"]
DEDICATED_EXPANSION_CALLOUTS = ["topic-idea", "further-exploration"]

# ══════════════════════════════════════════════════════════════════════════════
# FILE NAMING
# ══════════════════════════════════════════════════════════════════════════════

MAX_FILENAME_LENGTH = 80  # Max characters for filename stem (excluding .md)

# ══════════════════════════════════════════════════════════════════════════════
# CONTENT LIMITS
# ══════════════════════════════════════════════════════════════════════════════
# Caps on supporting content per note to keep notes focused.

MAX_EVIDENCE_PER_NOTE = 3
MAX_INSIGHTS_PER_NOTE = 2
MAX_CONNECTIONS_PER_NOTE = 2
MAX_PRACTICES_PER_NOTE = 2
MAX_WARNINGS_PER_NOTE = 1
MAX_REFLECTIONS_PER_NOTE = 2
MAX_EXPANSION_TOPICS = 4
MAX_WIKI_LINKS_DISPLAY = 15
MAX_RELATED_LINKS = 10
MAX_SEE_ALSO_LINKS = 8
MAX_REPORT_TAGS = 5

# Enhanced content limits (v2.1)
MAX_FLASHCARDS_PER_NOTE = 5
MAX_PERSONS_PER_NOTE = 3
MAX_TENSIONS_PER_NOTE = 2
MAX_OPEN_QUESTIONS_PER_NOTE = 2
MAX_PROTOCOLS_PER_NOTE = 2
MAX_DIAGRAMS_PER_NOTE = 1
MAX_CITATIONS_PER_NOTE = 5
MAX_METHODOLOGY_PER_NOTE = 1
