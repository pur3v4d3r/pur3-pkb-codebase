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
# CALLOUT TYPES THAT GENERATE PERMANENT NOTES
# ══════════════════════════════════════════════════════════════════════════════
# Each callout of these types produces one permanent note per instance.
# Add "key-claim" here if you also want key claims as standalone notes.

NOTE_GENERATING_CALLOUTS = ["definition", "original-synthesis"]

# ══════════════════════════════════════════════════════════════════════════════
# SUPPORTING CALLOUT TYPES (enrich notes but don't generate them)
# ══════════════════════════════════════════════════════════════════════════════

EVIDENCE_CALLOUTS = ["evidence", "what-the-evidence-suggests"]
INSIGHT_CALLOUTS = ["analytical-insight", "key-claim"]
CONNECTION_CALLOUTS = ["cross-domain-connection", "connections-and-links"]
PRACTICE_CALLOUTS = ["best-practice"]
EXPANSION_CALLOUTS = ["topic-idea"]
WARNING_CALLOUTS = ["warning"]

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
MAX_EXPANSION_TOPICS = 4
MAX_WIKI_LINKS_DISPLAY = 15
MAX_RELATED_LINKS = 10
MAX_SEE_ALSO_LINKS = 8
MAX_REPORT_TAGS = 5
