#!/usr/bin/env python3
"""
================================================================================
SCRIPT NAME: extract_yaml.py
VERSION:     1.0.0
PURPOSE:     Extract and audit YAML frontmatter across a folder of Markdown
             files, then emit a Markdown report covering field coverage,
             value distributions, type inference, and schema gaps.

REQUIRES:    Python 3.10+. Optional: pip install pyyaml (recommended).
USAGE:       python extract_yaml.py --input "./03-notes" --recursive
OUTPUT:      <folder>/yaml-extraction-report-<date>.md
================================================================================
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from _common import (build_arg_parser, gather_markdown_files,
                     md_table, report_frontmatter, resolve_output_path,
                     safe_read, vault_relative)

try:
    import yaml  # type: ignore
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(\n|$)", re.DOTALL)


# ── Extraction ────────────────────────────────────────────────────────────────

def extract_frontmatter(text: str) -> dict | None:
    """Return parsed YAML frontmatter dict, or None if missing/malformed."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    raw = m.group(1)
    if HAS_YAML:
        try:
            data = yaml.safe_load(raw)
            return data if isinstance(data, dict) else None
        except yaml.YAMLError:
            return {"__parse_error__": True}
    # Fallback: naive key: value parser
    out: dict = {}
    for line in raw.splitlines():
        if ":" in line and not line.startswith((" ", "-", "\t")):
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def infer_type(value) -> str:
    if isinstance(value, bool):  return "boolean"
    if isinstance(value, int):   return "integer"
    if isinstance(value, float): return "float"
    if isinstance(value, list):  return "array"
    if isinstance(value, dict):  return "object"
    if value is None:            return "null"
    return "string"


# ── Aggregation ───────────────────────────────────────────────────────────────

def analyse(files: list[Path]) -> dict:
    field_counts: Counter = Counter()
    field_types: dict[str, Counter] = defaultdict(Counter)
    field_examples: dict[str, list] = defaultdict(list)
    value_dists: dict[str, Counter] = defaultdict(Counter)
    no_frontmatter: list[Path] = []
    parse_errors: list[Path] = []
    per_file: list[tuple[Path, int]] = []

    for fp in files:
        fm = extract_frontmatter(safe_read(fp))
        if fm is None:
            no_frontmatter.append(fp)
            per_file.append((fp, 0))
            continue
        if fm.get("__parse_error__"):
            parse_errors.append(fp)
            per_file.append((fp, 0))
            continue

        per_file.append((fp, len(fm)))
        for key, value in fm.items():
            field_counts[key] += 1
            t = infer_type(value)
            field_types[key][t] += 1
            if len(field_examples[key]) < 3:
                preview = str(value)[:60].replace("\n", " ")
                if preview and preview not in field_examples[key]:
                    field_examples[key].append(preview)
            # Track value distributions for low-cardinality scalar fields
            if t in ("string", "boolean", "integer"):
                value_dists[key][str(value)[:60]] += 1

    return {
        "total": len(files),
        "with_fm": len(files) - len(no_frontmatter) - len(parse_errors),
        "no_frontmatter": no_frontmatter,
        "parse_errors": parse_errors,
        "field_counts": field_counts,
        "field_types": field_types,
        "field_examples": field_examples,
        "value_dists": value_dists,
        "per_file": per_file,
    }


# ── Reporting ─────────────────────────────────────────────────────────────────

def render_report(stats: dict, root: Path, top: int) -> str:
    out = [report_frontmatter("YAML Frontmatter Extraction Report",
                              root, stats["total"], "yaml")]

    out.append("# YAML Frontmatter Extraction Report\n\n")
    out.append("## Executive Summary\n\n")
    coverage = (stats["with_fm"] / stats["total"] * 100) if stats["total"] else 0
    out.append(md_table(
        ["Metric", "Value"],
        [
            ["Files scanned", stats["total"]],
            ["Files with frontmatter", stats["with_fm"]],
            ["Files missing frontmatter", len(stats["no_frontmatter"])],
            ["Files with parse errors", len(stats["parse_errors"])],
            ["Frontmatter coverage", f"{coverage:.1f}%"],
            ["Unique field names", len(stats["field_counts"])],
            ["YAML parser", "PyYAML" if HAS_YAML else "fallback (naive)"],
        ],
    ))

    # Field coverage
    out.append("## Field Coverage\n\n")
    rows = []
    for field, count in stats["field_counts"].most_common(top):
        types = stats["field_types"][field]
        type_str = ", ".join(f"{t} ({n})" for t, n in types.most_common())
        coverage_pct = (count / stats["with_fm"] * 100) if stats["with_fm"] else 0
        examples = " · ".join(stats["field_examples"][field][:2]) or "—"
        rows.append([f"`{field}`", count, f"{coverage_pct:.0f}%", type_str, examples])
    out.append(md_table(
        ["Field", "Count", "Coverage", "Type(s)", "Examples"], rows))

    # Value distributions for top fields with limited cardinality
    out.append("## Value Distributions (low-cardinality fields)\n\n")
    shown = 0
    for field, _ in stats["field_counts"].most_common():
        dist = stats["value_dists"].get(field)
        if not dist or len(dist) > 15 or len(dist) < 2:
            continue
        out.append(f"### `{field}`\n\n")
        out.append(md_table(
            ["Value", "Count"],
            [[v, n] for v, n in dist.most_common(15)],
        ))
        shown += 1
        if shown >= 8:
            break
    if shown == 0:
        out.append("*(no fields with constrained value sets detected)*\n\n")

    # Files missing frontmatter
    out.append("## Files Missing Frontmatter\n\n")
    if stats["no_frontmatter"]:
        out.append(md_table(
            ["#", "File"],
            [[i + 1, f"[[{vault_relative(p, root)}]]"]
             for i, p in enumerate(stats["no_frontmatter"][:50])],
        ))
        if len(stats["no_frontmatter"]) > 50:
            out.append(f"*… and {len(stats['no_frontmatter']) - 50} more.*\n\n")
    else:
        out.append("*All files have frontmatter.*\n\n")

    # Parse errors
    if stats["parse_errors"]:
        out.append("## Parse Errors\n\n")
        out.append(md_table(
            ["#", "File"],
            [[i + 1, f"[[{vault_relative(p, root)}]]"]
             for i, p in enumerate(stats["parse_errors"])],
        ))

    return "".join(out)


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    args = build_arg_parser(__doc__.splitlines()[4]).parse_args()
    input_path = Path(args.input).expanduser().resolve()
    if not input_path.exists():
        sys.exit(f"❌ Input not found: {input_path}")

    excludes = [s.strip() for s in args.exclude.split(",") if s.strip()]
    files = gather_markdown_files(input_path, args.recursive, excludes)
    if not files:
        sys.exit("⚠️ No Markdown files found.")

    if not args.quiet:
        print(f"📂 Scanning {len(files)} files…")
        if not HAS_YAML:
            print("ℹ️  PyYAML not installed — using naive parser. "
                  "Install with: pip install pyyaml")

    stats = analyse(files)
    root = input_path if input_path.is_dir() else input_path.parent
    report = render_report(stats, root, args.top)

    output = resolve_output_path(args, "yaml-extraction-report")
    output.write_text(report, encoding="utf-8")
    if not args.quiet:
        print(f"✅ Report written: {output}")


if __name__ == "__main__":
    main()
