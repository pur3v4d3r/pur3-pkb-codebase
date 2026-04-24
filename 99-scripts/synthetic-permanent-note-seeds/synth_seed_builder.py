#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""synth_seed_builder.py — Build & validate synthetic permanent-note seed JSONs.

Two complementary modes for producing ``*_extracted.json`` files that the
V4/V5/V6 permanent-note pipelines consume as if they came from
``pkb_extractor.py``:

  * ``build``    — assemble a synthetic seed from a YAML concept brief
                   (zero-LLM scaffolder; deterministic).
  * ``validate`` — verify that one or more seed JSONs conform to the
                   ``synthetic_bundle.schema.json`` v1 contract AND
                   pass the V4-specific substring-discipline checks
                   that the JSON Schema cannot express.

Usage:
    # Build one seed from a brief
    python synth_seed_builder.py build briefs/spaced-retrieval.yaml \\
        --out-dir 999-report-organizing/_extractor-output/_synthetic-seeds/2026-04-24-batch

    # Validate every seed in a directory before running V6 against it
    python synth_seed_builder.py validate \\
        999-report-organizing/_extractor-output/_synthetic-seeds/2026-04-24-batch

    # Validate a single file with verbose diagnostics
    python synth_seed_builder.py validate path/to/seed_extracted.json -v

Brief format (YAML):
    concept: "Spaced Retrieval"
    domain: "cognitive-science"
    secondary_domains: ["learning-science"]
    aliases: ["Spaced Retrieval Practice"]
    broader:       ["retrieval-practice"]
    narrower:      ["expanding-retrieval"]
    related:       ["testing-effect", "desirable-difficulties"]
    prerequisites: ["long-term-memory"]
    confidence: "high"
    callouts:
      - type: "definition"
        title: "Spaced Retrieval"
        body: |
          <multi-paragraph definition body>
      - type: "key-claim"
        title: "..."
        body: "..."
      # ... more support callouts

Exit codes:
    0    success (build wrote file; validate found zero errors)
    1    uncaught error
    2    bad arguments / missing input
    4    no inputs found in target directory
    5    one or more validation errors
    130  interrupted (Ctrl+C)

Version: 1.0.0
Python:  >=3.10
"""
from __future__ import annotations

# ─── Standard library ───────────────────────────────────────────────────
import argparse
import datetime as dt
import json
import logging
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

# ─── Third-party (optional) ─────────────────────────────────────────────
try:
    import yaml  # type: ignore[import-untyped]
    _YAML_AVAILABLE = True
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore[assignment]
    _YAML_AVAILABLE = False

try:
    import jsonschema  # type: ignore[import-untyped]
    _JSONSCHEMA_AVAILABLE = True
except ImportError:  # pragma: no cover
    jsonschema = None  # type: ignore[assignment]
    _JSONSCHEMA_AVAILABLE = False


# ════════════════════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════════════════════

__version__ = "1.0.0"

logger = logging.getLogger(__name__)

#: Default schema location (sibling file).
DEFAULT_SCHEMA_PATH: Path = Path(__file__).resolve().parent / "synthetic_bundle.schema.json"

#: Allowed callout types (mirror of V4 SUPPORT_CALLOUT_TYPES + concept seeds).
ALLOWED_CALLOUT_TYPES: frozenset[str] = frozenset({
    "definition", "key-claim", "key-distinction", "example", "warning",
    "claude-insight", "important", "principle-point", "evidence", "person",
    "open-question", "tension", "far-transfer", "original-synthesis",
    "section-summary",
})
PRIMARY_CONCEPT_CALLOUTS: frozenset[str] = frozenset({"definition", "key-claim"})

#: V4 hard limits (mirror of pipeline_v4 constants).
MIN_TITLE_LEN: int = 3
MAX_TITLE_LEN: int = 80
MAX_SUPPORT_CALLOUTS: int = 8

#: Title-cleaning regexes (mirror of V4 _TITLE_PAREN_RE / _TITLE_DASH_RE).
_TITLE_PAREN_RE = re.compile(r"\s*\([^)]+\)\s*$")
_TITLE_DASH_RE  = re.compile(r"\s*[—–-]\s+.+$")

#: Wiki-link target pattern (kebab-case slug).
_KEBAB_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


# ════════════════════════════════════════════════════════════════════════
# Custom exceptions
# ════════════════════════════════════════════════════════════════════════

class SeedBuilderError(Exception):
    """Base exception for synth_seed_builder."""


class BriefError(SeedBuilderError):
    """Raised when a YAML brief is malformed or missing required fields."""


class ValidationFailure(SeedBuilderError):
    """Raised when a seed JSON fails validation."""


# ════════════════════════════════════════════════════════════════════════
# Data types
# ════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class ValidationIssue:
    """One diagnostic finding from validating a seed."""
    severity: str             # "error" | "warning"
    location: str             # JSON pointer-ish path
    message: str

    def render(self) -> str:
        return f"  [{self.severity.upper()}] {self.location}: {self.message}"


@dataclass
class ValidationReport:
    """Aggregate validation outcome for one file."""
    path: Path
    issues: list[ValidationIssue] = field(default_factory=list)

    @property
    def errors(self) -> list[ValidationIssue]:
        return [i for i in self.issues if i.severity == "error"]

    @property
    def warnings(self) -> list[ValidationIssue]:
        return [i for i in self.issues if i.severity == "warning"]

    @property
    def ok(self) -> bool:
        return not self.errors


# ════════════════════════════════════════════════════════════════════════
# Helpers
# ════════════════════════════════════════════════════════════════════════

def to_kebab(s: str) -> str:
    """Lower-case, hyphen-separated slug. Mirror of V3 ``lib.markdown.to_kebab``."""
    s = (s or "").strip().lower()
    s = re.sub(r"[—–]", "-", s)
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def clean_title(raw: str) -> str:
    """Mirror of V4 ``_clean_title`` — predict what V4 will see."""
    if not raw:
        return ""
    t = raw.replace("[[", "").replace("]]", "").strip()
    t = _TITLE_PAREN_RE.sub("", t)
    t = _TITLE_DASH_RE.sub("", t)
    t = re.sub(r"\s+", " ", t).strip(" .:;,")
    return t


def bracket_link(target: str) -> str:
    """Render a bare slug as ``[[slug]]``; pass through if already bracketed."""
    target = target.strip()
    if target.startswith("[[") and target.endswith("]]"):
        return target
    return f"[[{target}]]"


def strip_brackets(target: str) -> str:
    """Reduce ``[[slug|alias]]`` → ``slug`` (or ``[[slug]]`` → ``slug``)."""
    t = target.strip().lstrip("[").rstrip("]").split("|", 1)[0].strip()
    return t


# ════════════════════════════════════════════════════════════════════════
# Brief loading & seed assembly
# ════════════════════════════════════════════════════════════════════════

def load_brief(path: Path) -> dict[str, Any]:
    """Load a YAML brief into a dict."""
    if not _YAML_AVAILABLE:
        raise SeedBuilderError(
            "PyYAML is required for `build` mode. Install with: pip install pyyaml"
        )
    if not path.exists():
        raise BriefError(f"Brief file not found: {path}")
    try:
        with path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise BriefError(f"Malformed YAML in {path}: {e}") from e
    if not isinstance(data, dict):
        raise BriefError(f"Brief root must be a mapping; got {type(data).__name__}")
    if not data.get("concept"):
        raise BriefError("Brief missing required field: 'concept'")
    if not data.get("domain"):
        raise BriefError("Brief missing required field: 'domain'")
    callouts = data.get("callouts") or []
    if not callouts:
        raise BriefError(
            "Brief missing 'callouts' (or it is empty). At minimum supply "
            "one definition callout."
        )
    return data


def build_seed(brief: dict[str, Any], *, batch_date: dt.date | None = None) -> dict[str, Any]:
    """Assemble a synthetic seed JSON from a parsed brief.

    Args:
        brief:      Parsed YAML brief mapping.
        batch_date: Date used in filenames and timestamps (defaults to today).

    Returns:
        A dict ready to be JSON-serialized into a ``*_extracted.json`` file.
    """
    batch_date = batch_date or dt.date.today()
    concept = str(brief["concept"]).strip()
    domain = to_kebab(str(brief["domain"]))
    cleaned = clean_title(concept)
    slug = to_kebab(cleaned)

    secondary_domains = [to_kebab(s) for s in (brief.get("secondary_domains") or []) if s]
    aliases = list(dict.fromkeys(
        [concept, cleaned] + [str(a).strip() for a in (brief.get("aliases") or []) if a]
    ))[:8]

    def _link_list(key: str) -> list[str]:
        out: list[str] = []
        for v in brief.get(key) or []:
            target = strip_brackets(str(v))
            if target and target not in out:
                out.append(bracket_link(target))
        return out

    frontmatter: dict[str, Any] = {
        "title": f"{cleaned} — A Synthetic Seed for the V6 Pipeline",
        "primary_domain": domain,
        "secondary_domains": secondary_domains,
        "aliases": aliases,
        "confidence": str(brief.get("confidence") or "high").lower(),
        "related":       _link_list("related"),
        "see-also":      _link_list("see-also"),
        "broader":       _link_list("broader"),
        "narrower":      _link_list("narrower"),
        "prerequisites": _link_list("prerequisites"),
    }

    callouts_in = brief.get("callouts") or []
    callouts_out: list[dict[str, Any]] = []
    for co in callouts_in:
        if not isinstance(co, dict):
            raise BriefError(f"Each callout must be a mapping; got {type(co).__name__}")
        ctype = str(co.get("type") or "").strip().lower()
        ctitle = str(co.get("title") or "").strip()
        cbody = str(co.get("body") or "").strip()
        if ctype not in ALLOWED_CALLOUT_TYPES:
            raise BriefError(
                f"Disallowed callout type {ctype!r}. Allowed: "
                f"{sorted(ALLOWED_CALLOUT_TYPES)}"
            )
        if not ctitle or not cbody:
            raise BriefError(
                f"Callout (type={ctype!r}) missing title or body."
            )
        callouts_out.append({"type": ctype, "title": ctitle, "body": cbody})

    # Harvest wiki-link targets from frontmatter + bodies for the kg block.
    targets: list[str] = []
    seen: set[str] = set()

    def _add(target: str) -> None:
        t = strip_brackets(target)
        if t and t not in seen:
            seen.add(t)
            targets.append(t)

    for key in ("related", "see-also", "broader", "narrower", "prerequisites"):
        for v in frontmatter.get(key) or []:
            _add(v)
    body_link_re = re.compile(r"\[\[([^\]\|]+)(?:\|[^\]]+)?\]\]")
    for co in callouts_out:
        for m in body_link_re.finditer(co["body"]):
            _add(m.group(1))

    seed: dict[str, Any] = {
        "extraction_metadata": {
            "script_name": "synth_seed_builder.py",
            "script_version": __version__,
            "extraction_timestamp": dt.datetime.now(dt.timezone.utc).isoformat(),
            "source_file": f"{slug}-synthetic-seed-{batch_date.isoformat()}.md",
            "synthetic": True,
            "brief_concept": concept,
        },
        "document_metadata": {"frontmatter": frontmatter},
        "extracted_items": {"callouts": callouts_out},
        "knowledge_graph": {"unique_wiki_link_targets": targets},
    }
    return seed


def filename_for(brief: dict[str, Any], *, batch_date: dt.date | None = None) -> str:
    """Return the canonical filename stem for a brief."""
    batch_date = batch_date or dt.date.today()
    cleaned = clean_title(str(brief["concept"]))
    slug = to_kebab(cleaned)
    return f"{slug}-synthetic-seed-{batch_date.isoformat()}_extracted.json"


# ════════════════════════════════════════════════════════════════════════
# Validation
# ════════════════════════════════════════════════════════════════════════

def _load_schema(schema_path: Path) -> dict[str, Any]:
    if not schema_path.exists():
        raise SeedBuilderError(f"Schema file not found: {schema_path}")
    with schema_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_seed(
    seed: dict[str, Any],
    path: Path,
    *,
    schema: dict[str, Any] | None = None,
) -> ValidationReport:
    """Validate a parsed seed dict against the v1 contract.

    Performs:
      1. JSON Schema validation (when ``jsonschema`` is installed).
      2. V4-specific substring-discipline checks (always).
      3. Hygiene checks (filename, title cleaning, support count).

    Args:
        seed:   Parsed seed JSON.
        path:   Source path (for error context only).
        schema: Pre-loaded schema dict (skips disk read).

    Returns:
        A ``ValidationReport`` aggregating all issues found.
    """
    report = ValidationReport(path=path)

    # ── JSON Schema pass ────────────────────────────────────────────────
    if schema is not None and _JSONSCHEMA_AVAILABLE:
        validator = jsonschema.Draft202012Validator(schema)
        for err in validator.iter_errors(seed):
            loc = "/" + "/".join(str(p) for p in err.absolute_path) if err.absolute_path else "/"
            report.issues.append(ValidationIssue("error", loc, err.message))
    elif schema is not None and not _JSONSCHEMA_AVAILABLE:
        report.issues.append(ValidationIssue(
            "warning", "/",
            "jsonschema not installed — schema-level checks skipped. "
            "Install with: pip install jsonschema",
        ))

    # ── V4 substring-discipline pass (cannot be expressed in JSON Schema) ──
    fm = (seed.get("document_metadata") or {}).get("frontmatter") or {}
    callouts = (seed.get("extracted_items") or {}).get("callouts") or []

    # Find the seed-concept callout (first definition; fallback to first key-claim).
    concept_callout: dict[str, Any] | None = None
    for co in callouts:
        if (co.get("type") or "").lower() == "definition":
            concept_callout = co
            break
    if concept_callout is None:
        for co in callouts:
            if (co.get("type") or "").lower() == "key-claim":
                concept_callout = co
                break

    if concept_callout is None:
        report.issues.append(ValidationIssue(
            "error", "/extracted_items/callouts",
            "No definition or key-claim callout found — V4 will mine zero "
            "concepts from this file.",
        ))
        return report

    raw_title = str(concept_callout.get("title") or "")
    cleaned = clean_title(raw_title)
    if not (MIN_TITLE_LEN <= len(cleaned) <= MAX_TITLE_LEN):
        report.issues.append(ValidationIssue(
            "error", "/extracted_items/callouts/0/title",
            f"Cleaned concept title {cleaned!r} length {len(cleaned)} "
            f"outside V4 bounds [{MIN_TITLE_LEN}, {MAX_TITLE_LEN}].",
        ))
    if cleaned != raw_title.strip():
        report.issues.append(ValidationIssue(
            "warning", "/extracted_items/callouts/0/title",
            f"Title {raw_title!r} will be cleaned by V4 to {cleaned!r}. "
            f"Pre-clean it for predictability.",
        ))

    # Substring-discipline: every support callout body or title must contain
    # the cleaned concept title (case-insensitive).
    needle = cleaned.lower()
    support_count = 0
    for idx, co in enumerate(callouts):
        if co is concept_callout:
            continue
        ctype = (co.get("type") or "").lower()
        if ctype == "definition" and co is not concept_callout:
            # A second definition is unusual but not fatal.
            report.issues.append(ValidationIssue(
                "warning", f"/extracted_items/callouts/{idx}",
                "Multiple definition callouts present — V4 deduplicates by "
                "cleaned title, only the first survives.",
            ))
        support_count += 1
        haystack = ((co.get("title") or "") + " " + (co.get("body") or "")).lower()
        if needle not in haystack:
            report.issues.append(ValidationIssue(
                "error", f"/extracted_items/callouts/{idx}",
                f"Support callout {(co.get('title') or '<untitled>')!r} does "
                f"not contain the cleaned concept title {cleaned!r} as a "
                f"case-insensitive substring — V4 will silently drop it from "
                f"the LLM context.",
            ))

    if support_count == 0:
        report.issues.append(ValidationIssue(
            "warning", "/extracted_items/callouts",
            "Zero support callouts — the LLM will have only the definition "
            "body to work from, producing a thin note.",
        ))
    if support_count > MAX_SUPPORT_CALLOUTS:
        report.issues.append(ValidationIssue(
            "warning", "/extracted_items/callouts",
            f"{support_count} support callouts present; V4 caps at "
            f"{MAX_SUPPORT_CALLOUTS} — extras will be dropped.",
        ))

    # ── Hygiene checks ──────────────────────────────────────────────────
    primary_domain = str(fm.get("primary_domain") or "")
    if primary_domain and not _KEBAB_RE.match(primary_domain):
        report.issues.append(ValidationIssue(
            "error", "/document_metadata/frontmatter/primary_domain",
            f"primary_domain {primary_domain!r} is not kebab-case "
            f"(expected pattern: lowercase + digits + hyphens).",
        ))

    kg_targets = (seed.get("knowledge_graph") or {}).get("unique_wiki_link_targets") or []
    for i, t in enumerate(kg_targets):
        if "[" in t or "]" in t or "|" in t:
            report.issues.append(ValidationIssue(
                "error", f"/knowledge_graph/unique_wiki_link_targets/{i}",
                f"Target {t!r} contains bracket or pipe — must be a bare "
                f"kebab slug.",
            ))

    if "_extracted.json" not in path.name:
        report.issues.append(ValidationIssue(
            "error", "/__filename__",
            f"Filename {path.name!r} does not end in '_extracted.json' — "
            f"V4's discover_jsons() will not pick it up.",
        ))
    if "synthetic-seed" not in path.name:
        report.issues.append(ValidationIssue(
            "warning", "/__filename__",
            f"Filename {path.name!r} lacks 'synthetic-seed' marker — "
            f"audit tools will not be able to distinguish it from organic "
            f"extractor output.",
        ))

    return report


def validate_path(
    path: Path,
    *,
    schema: dict[str, Any] | None,
) -> ValidationReport:
    """Validate a single seed JSON file."""
    if not path.exists():
        report = ValidationReport(path=path)
        report.issues.append(ValidationIssue("error", "/", f"File not found: {path}"))
        return report
    try:
        with path.open("r", encoding="utf-8") as f:
            seed = json.load(f)
    except json.JSONDecodeError as e:
        report = ValidationReport(path=path)
        report.issues.append(ValidationIssue("error", "/", f"Invalid JSON: {e}"))
        return report
    return validate_seed(seed, path, schema=schema)


def discover_seeds(target: Path) -> list[Path]:
    """Discover seed files under a path (file or directory)."""
    if target.is_file():
        return [target]
    if target.is_dir():
        return sorted(target.rglob("*_extracted.json"))
    return []


# ════════════════════════════════════════════════════════════════════════
# I/O
# ════════════════════════════════════════════════════════════════════════

def write_atomic(path: Path, content: str) -> None:
    """Atomic UTF-8 write via .tmp → replace."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(path)


# ════════════════════════════════════════════════════════════════════════
# CLI
# ════════════════════════════════════════════════════════════════════════

def configure_logging(verbosity: int, quiet: bool) -> None:
    """Configure root logging based on -v/-q flags."""
    if quiet:
        level = logging.ERROR
    elif verbosity >= 2:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )


def build_parser() -> argparse.ArgumentParser:
    """Construct the argparse CLI."""
    parser = argparse.ArgumentParser(
        prog="synth_seed_builder",
        description=(
            "Build & validate synthetic permanent-note seed JSONs for the "
            "V4/V5/V6 pipeline."
        ),
        epilog=(
            "Examples:\n"
            "  synth_seed_builder.py build briefs/spaced-retrieval.yaml \\\n"
            "      --out-dir _extractor-output/_synthetic-seeds/2026-04-24-batch\n"
            "  synth_seed_builder.py validate _extractor-output/_synthetic-seeds/2026-04-24-batch\n"
            "  synth_seed_builder.py validate path/to/one_extracted.json -v\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-v", "--verbose", action="count", default=0,
                        help="increase verbosity (repeatable: -v, -vv)")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="suppress non-error output")
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA_PATH,
                        help=f"JSON Schema path (default: {DEFAULT_SCHEMA_PATH.name})")

    sub = parser.add_subparsers(dest="command", required=True, metavar="COMMAND")

    # build subcommand
    p_build = sub.add_parser("build", help="assemble a seed JSON from a YAML brief")
    p_build.add_argument("brief", type=Path, help="path to a YAML brief file")
    p_build.add_argument("--out-dir", type=Path, required=True,
                         help="output directory for the generated seed file")
    p_build.add_argument("--batch-date", type=str, default=None,
                         help="ISO date for filename + timestamp (default: today)")
    p_build.add_argument("-n", "--dry-run", action="store_true",
                         help="print the seed to stdout instead of writing")
    p_build.add_argument("--no-validate", action="store_true",
                         help="skip post-build validation (not recommended)")

    # validate subcommand
    p_val = sub.add_parser("validate", help="validate seed JSONs against the v1 contract")
    p_val.add_argument("targets", type=Path, nargs="+",
                       help="files or directories to validate")
    p_val.add_argument("--strict-warnings", action="store_true",
                       help="treat warnings as errors (exit 5 on any warning)")

    return parser


def cmd_build(args: argparse.Namespace) -> int:
    """Handle the ``build`` subcommand."""
    try:
        brief = load_brief(args.brief)
    except BriefError as e:
        logger.error("Brief error: %s", e)
        return 4

    batch_date: dt.date
    if args.batch_date:
        try:
            batch_date = dt.date.fromisoformat(args.batch_date)
        except ValueError as e:
            logger.error("Invalid --batch-date %r: %s", args.batch_date, e)
            return 2
    else:
        batch_date = dt.date.today()

    seed = build_seed(brief, batch_date=batch_date)
    fname = filename_for(brief, batch_date=batch_date)
    payload = json.dumps(seed, indent=2, ensure_ascii=False)

    if args.dry_run:
        sys.stdout.write(payload + "\n")
        logger.info("Dry-run: would write %s (%d bytes)", fname, len(payload))
    else:
        out_path = args.out_dir / fname
        write_atomic(out_path, payload)
        logger.info("Wrote %s (%d bytes)", out_path, len(payload))

    if not args.no_validate:
        try:
            schema = _load_schema(args.schema)
        except SeedBuilderError as e:
            logger.warning("Skipping validation: %s", e)
            return 0
        # Validate the in-memory seed against the synthetic path the
        # filename WOULD have, so filename hygiene checks fire.
        synthetic_path = (args.out_dir if not args.dry_run else Path(".")) / fname
        report = validate_seed(seed, synthetic_path, schema=schema)
        _print_report(report)
        if report.errors:
            return 5
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    """Handle the ``validate`` subcommand."""
    try:
        schema = _load_schema(args.schema)
    except SeedBuilderError as e:
        logger.error("%s", e)
        return 2

    paths: list[Path] = []
    for t in args.targets:
        found = discover_seeds(t)
        if not found:
            logger.warning("No *_extracted.json files under %s", t)
        paths.extend(found)
    if not paths:
        logger.error("No seed files to validate.")
        return 4

    total_errors = 0
    total_warnings = 0
    failed_files = 0
    for p in paths:
        report = validate_path(p, schema=schema)
        _print_report(report)
        total_errors += len(report.errors)
        total_warnings += len(report.warnings)
        if not report.ok:
            failed_files += 1

    summary = (
        f"\n=== Validation summary: {len(paths)} file(s), "
        f"{failed_files} with errors, {total_errors} error(s), "
        f"{total_warnings} warning(s) ==="
    )
    logger.warning(summary)

    if total_errors > 0:
        return 5
    if args.strict_warnings and total_warnings > 0:
        return 5
    return 0


def _print_report(report: ValidationReport) -> None:
    """Pretty-print a validation report."""
    status = "OK " if report.ok else "FAIL"
    logger.warning("[%s] %s", status, report.path)
    for issue in report.issues:
        logger.warning(issue.render())


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    try:
        if args.command == "build":
            return cmd_build(args)
        if args.command == "validate":
            return cmd_validate(args)
        parser.error(f"Unknown command: {args.command}")
        return 2
    except KeyboardInterrupt:
        logger.warning("Interrupted by user")
        return 130
    except SeedBuilderError as e:
        logger.error("%s", e)
        return 1
    except Exception:
        logger.exception("Unexpected error")
        return 1


# ════════════════════════════════════════════════════════════════════════
# Entry-point guard
# ════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    sys.exit(main())
