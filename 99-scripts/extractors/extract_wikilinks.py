#!/usr/bin/env python3
"""
================================================================================
SCRIPT NAME: extract_wikilinks.py
VERSION:     1.0.0
PURPOSE:     Extract every Obsidian wiki-link ([[Target]], [[Target|Alias]],
             [[Target#Heading]], ![[Embed]]) from a folder of Markdown files
             and emit a Markdown report on link usage, top targets, alias
             patterns, embed usage, and link density per file.

REQUIRES:    Python 3.10+. No external dependencies.
USAGE:       python extract_wikilinks.py --input "./03-notes" --recursive
OUTPUT:      <folder>/wikilinks-extraction-report-<date>.md
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

# Wiki-link pattern: optional embed prefix !, [[target(#heading)?(|alias)?]]
WIKILINK_RE = re.compile(
    r"(?P<embed>!?)\[\["
    r"(?P<target>[^\]\|#\n]+)"
    r"(?:#(?P<heading>[^\]\|\n]+))?"
    r"(?:\|(?P<alias>[^\]\n]+))?"
    r"\]\]"
)
# Strip code blocks/inline code so links inside snippets don't count
CODE_FENCE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")


def strip_code(text: str) -> str:
    text = CODE_FENCE_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def extract(text: str) -> list[dict]:
    cleaned = strip_code(text)
    out = []
    for m in WIKILINK_RE.finditer(cleaned):
        out.append({
            "target": m.group("target").strip(),
            "heading": (m.group("heading") or "").strip() or None,
            "alias": (m.group("alias") or "").strip() or None,
            "embed": bool(m.group("embed")),
        })
    return out


def analyse(files: list[Path]) -> dict:
    target_counts: Counter = Counter()
    alias_counts: Counter = Counter()
    heading_link_counts: Counter = Counter()
    embed_counts: Counter = Counter()
    target_sources: dict[str, set] = defaultdict(set)
    per_file: list[dict] = []
    total_links = 0
    total_embeds = 0
    total_aliased = 0
    total_heading = 0

    for fp in files:
        links = extract(safe_read(fp))
        per_file.append({
            "path": fp,
            "count": len(links),
            "embeds": sum(1 for l in links if l["embed"]),
            "aliased": sum(1 for l in links if l["alias"]),
        })
        for link in links:
            total_links += 1
            target_counts[link["target"]] += 1
            target_sources[link["target"]].add(fp)
            if link["embed"]:
                total_embeds += 1
                embed_counts[link["target"]] += 1
            if link["alias"]:
                total_aliased += 1
                alias_counts[(link["target"], link["alias"])] += 1
            if link["heading"]:
                total_heading += 1
                heading_link_counts[f"{link['target']}#{link['heading']}"] += 1

    return {
        "total_files": len(files),
        "total_links": total_links,
        "total_embeds": total_embeds,
        "total_aliased": total_aliased,
        "total_heading": total_heading,
        "unique_targets": len(target_counts),
        "target_counts": target_counts,
        "alias_counts": alias_counts,
        "heading_link_counts": heading_link_counts,
        "embed_counts": embed_counts,
        "target_sources": target_sources,
        "per_file": per_file,
    }


def render_report(stats: dict, root: Path, top: int) -> str:
    out = [report_frontmatter("Wiki-Link Extraction Report",
                              root, stats["total_files"], "wikilinks")]
    out.append("# Wiki-Link Extraction Report\n\n")

    # Summary
    out.append("## Executive Summary\n\n")
    avg = (stats["total_links"] / stats["total_files"]) if stats["total_files"] else 0
    out.append(md_table(["Metric", "Value"], [
        ["Files scanned", stats["total_files"]],
        ["Total wiki-links", stats["total_links"]],
        ["Unique link targets", stats["unique_targets"]],
        ["Embeds (`![[…]]`)", stats["total_embeds"]],
        ["Aliased links (`[[…|alias]]`)", stats["total_aliased"]],
        ["Heading links (`[[…#section]]`)", stats["total_heading"]],
        ["Avg links per file", f"{avg:.1f}"],
    ]))

    # Top linked targets
    out.append("## Most-Linked Targets (hubs)\n\n")
    rows = []
    for target, count in stats["target_counts"].most_common(top):
        rows.append([
            f"[[{target}]]",
            count,
            len(stats["target_sources"][target]),
        ])
    out.append(md_table(["Target", "Link count", "Distinct source files"], rows))

    # Top files by link density
    out.append("## Files with Highest Link Density\n\n")
    ranked = sorted(stats["per_file"], key=lambda r: r["count"], reverse=True)
    rows = []
    for r in ranked[:top]:
        if r["count"] == 0:
            continue
        rows.append([
            f"[[{vault_relative(r['path'], root)}]]",
            r["count"], r["embeds"], r["aliased"],
        ])
    out.append(md_table(["File", "Links", "Embeds", "Aliased"], rows))

    # Files with zero outgoing links
    isolated = [r for r in stats["per_file"] if r["count"] == 0]
    out.append(f"## Files with Zero Outgoing Links ({len(isolated)})\n\n")
    if isolated:
        out.append(md_table(
            ["#", "File"],
            [[i + 1, f"[[{vault_relative(r['path'], root)}]]"]
             for i, r in enumerate(isolated[:30])],
        ))
        if len(isolated) > 30:
            out.append(f"*… and {len(isolated) - 30} more.*\n\n")

    # Alias patterns
    out.append("## Alias Patterns\n\n")
    if stats["alias_counts"]:
        out.append(md_table(
            ["Target", "Alias used", "Count"],
            [[f"[[{t}]]", f"`{a}`", n]
             for (t, a), n in stats["alias_counts"].most_common(top)],
        ))
    else:
        out.append("*No aliased links found.*\n\n")

    # Top embeds
    if stats["embed_counts"]:
        out.append("## Most-Embedded Targets\n\n")
        out.append(md_table(
            ["Target", "Embed count"],
            [[f"[[{t}]]", n] for t, n in stats["embed_counts"].most_common(top)],
        ))

    # Top heading links
    if stats["heading_link_counts"]:
        out.append("## Most-Linked Headings\n\n")
        out.append(md_table(
            ["Target#Heading", "Count"],
            [[f"`{h}`", n]
             for h, n in stats["heading_link_counts"].most_common(top)],
        ))

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
        print(f"📂 Scanning {len(files)} files for wiki-links…")

    stats = analyse(files)
    root = input_path if input_path.is_dir() else input_path.parent
    report = render_report(stats, root, args.top)

    output = resolve_output_path(args, "wikilinks-extraction-report")
    output.write_text(report, encoding="utf-8")
    if not args.quiet:
        print(f"✅ Report written: {output}")
        print(f"   {stats['total_links']} links → "
              f"{stats['unique_targets']} unique targets.")


if __name__ == "__main__":
    main()
