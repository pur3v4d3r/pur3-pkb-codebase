#!/usr/bin/env python3
"""
================================================================================
SCRIPT NAME: extract_callouts.py
VERSION:     1.0.0
PURPOSE:     Extract every Obsidian callout (`> [!type] Title \n > body …`)
             from a folder of Markdown files and emit a Markdown report on
             callout type distribution, foldable usage, title patterns,
             and per-file density.

REQUIRES:    Python 3.10+. No external dependencies.
USAGE:       python extract_callouts.py --input "./03-notes" --recursive
OUTPUT:      <folder>/callouts-extraction-report-<date>.md
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

# Header line of a callout: > [!type]±  Optional Title
CALLOUT_HEADER_RE = re.compile(
    r"^(?P<indent>\s*)>\s*\[!(?P<type>[\w\-+]+)\](?P<fold>[+-]?)\s*(?P<title>.*)$"
)


def extract(text: str) -> list[dict]:
    """Walk lines, identify callout headers, capture body until block ends."""
    lines = text.splitlines()
    out: list[dict] = []
    i = 0
    while i < len(lines):
        m = CALLOUT_HEADER_RE.match(lines[i])
        if not m:
            i += 1
            continue
        callout_type = m.group("type").lower()
        fold = m.group("fold") or ""
        title = m.group("title").strip()
        line_start = i + 1
        body_lines: list[str] = []
        i += 1
        while i < len(lines):
            line = lines[i]
            stripped = line.lstrip()
            if stripped.startswith(">"):
                body_lines.append(stripped[1:].lstrip())
                i += 1
            else:
                break
        out.append({
            "type": callout_type,
            "fold": fold,             # '', '+' (open), '-' (collapsed)
            "title": title,
            "body": "\n".join(body_lines).strip(),
            "body_lines": len(body_lines),
            "line_start": line_start,
        })
    return out


def analyse(files: list[Path]) -> dict:
    type_counts: Counter = Counter()
    type_files: dict[str, set] = defaultdict(set)
    fold_counts: Counter = Counter()
    title_word_counts: Counter = Counter()
    nested_count = 0
    per_file: list[dict] = []
    titled = 0
    untitled = 0
    total = 0

    for fp in files:
        callouts = extract(safe_read(fp))
        per_file.append({
            "path": fp,
            "count": len(callouts),
            "types": Counter(c["type"] for c in callouts),
        })
        for c in callouts:
            total += 1
            type_counts[c["type"]] += 1
            type_files[c["type"]].add(fp)
            fold_label = {"+": "open (+)",
                          "-": "collapsed (-)"}.get(c["fold"], "default")
            fold_counts[fold_label] += 1
            if c["title"]:
                titled += 1
                for w in re.findall(r"[A-Za-z][A-Za-z\-']{2,}", c["title"].lower()):
                    title_word_counts[w] += 1
            else:
                untitled += 1
            if "[!" in c["body"]:
                nested_count += 1

    return {
        "total_files": len(files),
        "total_callouts": total,
        "type_counts": type_counts,
        "type_files": type_files,
        "fold_counts": fold_counts,
        "title_word_counts": title_word_counts,
        "titled": titled,
        "untitled": untitled,
        "nested_count": nested_count,
        "per_file": per_file,
    }


def render_report(stats: dict, root: Path, top: int) -> str:
    out = [report_frontmatter("Callout Extraction Report",
                              root, stats["total_files"], "callouts")]
    out.append("# Callout Extraction Report\n\n")

    # Summary
    out.append("## Executive Summary\n\n")
    avg = (stats["total_callouts"] / stats["total_files"]) if stats["total_files"] else 0
    out.append(md_table(["Metric", "Value"], [
        ["Files scanned", stats["total_files"]],
        ["Total callouts", stats["total_callouts"]],
        ["Unique callout types", len(stats["type_counts"])],
        ["Titled callouts", stats["titled"]],
        ["Untitled callouts", stats["untitled"]],
        ["Nested callouts (body contains `[!`)", stats["nested_count"]],
        ["Avg callouts per file", f"{avg:.1f}"],
    ]))

    # Type distribution
    out.append("## Callout Type Distribution\n\n")
    rows = []
    for ctype, count in stats["type_counts"].most_common(top):
        rows.append([
            f"`[!{ctype}]`",
            count,
            len(stats["type_files"][ctype]),
            f"{(count / stats['total_callouts'] * 100):.1f}%",
        ])
    out.append(md_table(
        ["Type", "Count", "Files", "% of all callouts"], rows))

    # Fold state distribution
    out.append("## Foldable State\n\n")
    out.append(md_table(
        ["Fold marker", "Count"],
        [[k, v] for k, v in stats["fold_counts"].most_common()],
    ))

    # Top files by callout density
    out.append("## Files with Highest Callout Density\n\n")
    ranked = sorted(stats["per_file"], key=lambda r: r["count"], reverse=True)
    rows = []
    for r in ranked[:top]:
        if r["count"] == 0:
            continue
        types = ", ".join(f"{t} ({n})" for t, n in r["types"].most_common(3))
        rows.append([
            f"[[{vault_relative(r['path'], root)}]]",
            r["count"], types,
        ])
    out.append(md_table(["File", "Callouts", "Top types"], rows))

    # Common title words (signals topical patterns)
    out.append("## Common Title Words\n\n")
    if stats["title_word_counts"]:
        out.append(md_table(
            ["Word", "Frequency in titles"],
            [[w, n] for w, n in stats["title_word_counts"].most_common(top)],
        ))
    else:
        out.append("*No titled callouts found.*\n\n")

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
        print(f"📂 Scanning {len(files)} files for callouts…")

    stats = analyse(files)
    root = input_path if input_path.is_dir() else input_path.parent
    report = render_report(stats, root, args.top)

    output = resolve_output_path(args, "callouts-extraction-report")
    output.write_text(report, encoding="utf-8")
    if not args.quiet:
        print(f"✅ Report written: {output}")
        print(f"   {stats['total_callouts']} callouts across "
              f"{len(stats['type_counts'])} types.")


if __name__ == "__main__":
    main()
