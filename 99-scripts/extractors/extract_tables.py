#!/usr/bin/env python3
"""
================================================================================
SCRIPT NAME: extract_tables.py
VERSION:     1.0.0
PURPOSE:     Extract every GFM-style Markdown table from a folder of Markdown
             files and emit a Markdown report on table count, dimensions,
             column-header patterns, alignment usage, and per-file density.

REQUIRES:    Python 3.10+. No external dependencies.
USAGE:       python extract_tables.py --input "./03-notes" --recursive
OUTPUT:      <folder>/tables-extraction-report-<date>.md
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

# A separator row for GFM tables, e.g. | --- | :--- | ---: | :---: |
SEPARATOR_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")
# Strip code fences before scanning so pipe characters in code don't fool us
CODE_FENCE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)


def split_row(line: str) -> list[str]:
    """Split a Markdown table row into trimmed cell values."""
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def detect_alignments(separator_line: str) -> list[str]:
    out = []
    for cell in split_row(separator_line):
        left = cell.startswith(":")
        right = cell.endswith(":")
        if left and right:   out.append("center")
        elif right:          out.append("right")
        elif left:           out.append("left")
        else:                out.append("default")
    return out


def extract(text: str) -> list[dict]:
    """Find tables: a header line followed immediately by a separator line."""
    text = CODE_FENCE_RE.sub("", text)
    lines = text.splitlines()
    out: list[dict] = []
    i = 0
    while i < len(lines) - 1:
        header = lines[i]
        separator = lines[i + 1]
        if "|" in header and SEPARATOR_RE.match(separator):
            headers = split_row(header)
            alignments = detect_alignments(separator)
            # Collect data rows
            data_rows: list[list[str]] = []
            j = i + 2
            while j < len(lines) and "|" in lines[j] and lines[j].strip():
                data_rows.append(split_row(lines[j]))
                j += 1
            out.append({
                "headers": headers,
                "alignments": alignments,
                "rows": data_rows,
                "row_count": len(data_rows),
                "col_count": len(headers),
                "line_start": i + 1,
            })
            i = j
        else:
            i += 1
    return out


def analyse(files: list[Path]) -> dict:
    header_counts: Counter = Counter()
    align_counts: Counter = Counter()
    col_count_dist: Counter = Counter()
    row_count_buckets: Counter = Counter()
    per_file: list[dict] = []
    total_tables = 0
    total_rows = 0
    files_with_tables = 0

    for fp in files:
        tables = extract(safe_read(fp))
        if tables:
            files_with_tables += 1
        per_file.append({
            "path": fp,
            "count": len(tables),
            "rows": sum(t["row_count"] for t in tables),
            "max_cols": max((t["col_count"] for t in tables), default=0),
        })
        for t in tables:
            total_tables += 1
            total_rows += t["row_count"]
            col_count_dist[t["col_count"]] += 1
            for h in t["headers"]:
                if h:
                    header_counts[h.lower()] += 1
            for a in t["alignments"]:
                align_counts[a] += 1
            # Bucket row sizes
            r = t["row_count"]
            bucket = ("0 rows" if r == 0 else
                      "1–5"   if r <= 5  else
                      "6–20"  if r <= 20 else
                      "21–50" if r <= 50 else "50+")
            row_count_buckets[bucket] += 1

    return {
        "total_files": len(files),
        "files_with_tables": files_with_tables,
        "total_tables": total_tables,
        "total_rows": total_rows,
        "header_counts": header_counts,
        "align_counts": align_counts,
        "col_count_dist": col_count_dist,
        "row_count_buckets": row_count_buckets,
        "per_file": per_file,
    }


def render_report(stats: dict, root: Path, top: int) -> str:
    out = [report_frontmatter("Table Extraction Report",
                              root, stats["total_files"], "tables")]
    out.append("# Table Extraction Report\n\n")

    # Summary
    out.append("## Executive Summary\n\n")
    avg_rows = (stats["total_rows"] / stats["total_tables"]) if stats["total_tables"] else 0
    out.append(md_table(["Metric", "Value"], [
        ["Files scanned", stats["total_files"]],
        ["Files containing tables", stats["files_with_tables"]],
        ["Total tables", stats["total_tables"]],
        ["Total data rows", stats["total_rows"]],
        ["Avg rows per table", f"{avg_rows:.1f}"],
        ["Unique header labels", len(stats["header_counts"])],
    ]))

    # Column-count distribution
    out.append("## Column-Count Distribution\n\n")
    out.append(md_table(
        ["Columns", "Tables"],
        [[k, v] for k, v in sorted(stats["col_count_dist"].items())],
    ))

    # Row-size buckets
    out.append("## Table-Size Buckets (data rows)\n\n")
    bucket_order = ["0 rows", "1–5", "6–20", "21–50", "50+"]
    out.append(md_table(
        ["Row range", "Tables"],
        [[b, stats["row_count_buckets"].get(b, 0)] for b in bucket_order],
    ))

    # Alignment usage
    out.append("## Column Alignment Usage\n\n")
    out.append(md_table(
        ["Alignment", "Columns"],
        [[k, v] for k, v in stats["align_counts"].most_common()],
    ))

    # Top header labels — surfaces semantic patterns
    out.append("## Most Common Header Labels\n\n")
    out.append(md_table(
        ["Header label", "Occurrences"],
        [[f"`{h}`", n] for h, n in stats["header_counts"].most_common(top)],
    ))

    # Top files by table density
    out.append("## Files with Most Tables\n\n")
    ranked = sorted(stats["per_file"], key=lambda r: r["count"], reverse=True)
    rows = []
    for r in ranked[:top]:
        if r["count"] == 0:
            continue
        rows.append([
            f"[[{vault_relative(r['path'], root)}]]",
            r["count"], r["rows"], r["max_cols"],
        ])
    out.append(md_table(
        ["File", "Tables", "Total rows", "Widest table (cols)"], rows))

    return "".join(out)


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
        print(f"📂 Scanning {len(files)} files for tables…")

    stats = analyse(files)
    root = input_path if input_path.is_dir() else input_path.parent
    report = render_report(stats, root, args.top)

    output = resolve_output_path(args, "tables-extraction-report")
    output.write_text(report, encoding="utf-8")
    if not args.quiet:
        print(f"✅ Report written: {output}")
        print(f"   {stats['total_tables']} tables ("
              f"{stats['total_rows']} data rows).")


if __name__ == "__main__":
    main()
