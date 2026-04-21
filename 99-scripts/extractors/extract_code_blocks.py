#!/usr/bin/env python3
"""
================================================================================
SCRIPT NAME: extract_code_blocks.py
VERSION:     1.0.0
PURPOSE:     Extract every fenced code block from Markdown files and emit a
             report covering language distribution, line/character volume,
             top files by code density, and (optional) full code listings.

REQUIRES:    Python 3.10+. No external dependencies.
USAGE:       python extract_code_blocks.py --input "./03-notes" --recursive
OUTPUT:      <folder>/code-blocks-extraction-report-<date>.md
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

# Capture fenced code blocks: ```lang\n…body…\n```  (and ~~~ variant)
FENCE_RE = re.compile(
    r"(?P<fence>^|\n)(?P<marker>```|~~~)(?P<lang>[\w+\-.#]*)\s*\n"
    r"(?P<body>.*?)\n(?P=marker)(?=\n|$)",
    re.DOTALL,
)


def extract(text: str) -> list[dict]:
    blocks = []
    for m in FENCE_RE.finditer(text):
        lang = (m.group("lang") or "").strip().lower() or "(none)"
        body = m.group("body")
        line_start = text[:m.start()].count("\n") + 1
        blocks.append({
            "lang": lang,
            "body": body,
            "lines": body.count("\n") + 1 if body else 0,
            "chars": len(body),
            "line_start": line_start,
        })
    return blocks


def analyse(files: list[Path]) -> dict:
    lang_counts: Counter = Counter()
    lang_lines: Counter = Counter()
    lang_files: dict[str, set] = defaultdict(set)
    per_file: list[dict] = []
    all_blocks: list[tuple[Path, dict]] = []
    files_with_blocks = 0

    for fp in files:
        text = safe_read(fp)
        blocks = extract(text)
        if blocks:
            files_with_blocks += 1
        per_file.append({
            "path": fp,
            "count": len(blocks),
            "lines": sum(b["lines"] for b in blocks),
            "langs": Counter(b["lang"] for b in blocks),
        })
        for b in blocks:
            lang_counts[b["lang"]] += 1
            lang_lines[b["lang"]] += b["lines"]
            lang_files[b["lang"]].add(fp)
            all_blocks.append((fp, b))

    return {
        "total_files": len(files),
        "files_with_blocks": files_with_blocks,
        "total_blocks": sum(lang_counts.values()),
        "total_lines": sum(lang_lines.values()),
        "lang_counts": lang_counts,
        "lang_lines": lang_lines,
        "lang_files": lang_files,
        "per_file": per_file,
        "all_blocks": all_blocks,
    }


def render_report(stats: dict, root: Path, top: int) -> str:
    out = [report_frontmatter("Code Block Extraction Report",
                              root, stats["total_files"], "code-blocks")]
    out.append("# Code Block Extraction Report\n\n")

    # Summary
    out.append("## Executive Summary\n\n")
    out.append(md_table(["Metric", "Value"], [
        ["Files scanned", stats["total_files"]],
        ["Files containing code blocks", stats["files_with_blocks"]],
        ["Total code blocks", stats["total_blocks"]],
        ["Total code lines", stats["total_lines"]],
        ["Unique languages", len(stats["lang_counts"])],
        ["Avg blocks per file (with code)",
         f"{(stats['total_blocks'] / stats['files_with_blocks']):.1f}"
         if stats["files_with_blocks"] else "0"],
    ]))

    # Language distribution
    out.append("## Language Distribution\n\n")
    rows = []
    for lang, count in stats["lang_counts"].most_common(top):
        rows.append([
            f"`{lang}`",
            count,
            stats["lang_lines"][lang],
            len(stats["lang_files"][lang]),
            f"{(count / stats['total_blocks'] * 100):.1f}%",
        ])
    out.append(md_table(
        ["Language", "Blocks", "Lines", "Files", "% of blocks"], rows))

    # Top files by code density
    out.append("## Top Files by Code Volume\n\n")
    ranked = sorted(stats["per_file"], key=lambda r: r["lines"], reverse=True)
    rows = []
    for r in ranked[:top]:
        if r["count"] == 0:
            continue
        langs = ", ".join(f"{l} ({n})" for l, n in r["langs"].most_common(3))
        rows.append([
            f"[[{vault_relative(r['path'], root)}]]",
            r["count"], r["lines"], langs,
        ])
    out.append(md_table(["File", "Blocks", "Lines", "Languages"], rows))

    # Untagged / language-less blocks audit
    untagged = stats["lang_counts"].get("(none)", 0)
    if untagged:
        out.append("## ⚠️ Untagged Code Blocks\n\n")
        out.append(f"{untagged} block(s) lack a language identifier "
                   "(e.g. ```` ``` ```` instead of ```` ```python ````). "
                   "Adding language hints improves syntax highlighting.\n\n")
        rows = []
        for fp, blk in stats["all_blocks"]:
            if blk["lang"] == "(none)":
                preview = (blk["body"].splitlines()[0] if blk["body"] else "")[:50]
                rows.append([
                    f"[[{vault_relative(fp, root)}]]",
                    blk["line_start"], blk["lines"], f"`{preview}`",
                ])
                if len(rows) >= 30:
                    break
        out.append(md_table(["File", "Line", "Lines", "First line preview"], rows))

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
        print(f"📂 Scanning {len(files)} files for code blocks…")

    stats = analyse(files)
    root = input_path if input_path.is_dir() else input_path.parent
    report = render_report(stats, root, args.top)

    output = resolve_output_path(args, "code-blocks-extraction-report")
    output.write_text(report, encoding="utf-8")
    if not args.quiet:
        print(f"✅ Report written: {output}")
        print(f"   {stats['total_blocks']} blocks across "
              f"{len(stats['lang_counts'])} languages.")


if __name__ == "__main__":
    main()
