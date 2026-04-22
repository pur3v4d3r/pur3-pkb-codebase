"""MOC Builder — Phase 2: Cluster Discovery.

Reads `_inventory.json` and produces `_clusters.json` plus a human-readable
`_clusters-report.md` summarising domains, tag co-occurrence, and hub notes.

Usage:
    python 99-scripts/moc-builder/moc_cluster.py
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

VAULT = Path(r"D:\10_pur3v4d3r's-vault")
OUT_DIR = VAULT / "999-report-organizing" / "_maps-of-content-for-permenent-notes"
INVENTORY = OUT_DIR / "_inventory.json"
CLUSTERS_JSON = OUT_DIR / "_clusters.json"
CLUSTERS_MD = OUT_DIR / "_clusters-report.md"


def load() -> list[dict[str, Any]]:
    return json.loads(INVENTORY.read_text(encoding="utf-8"))


def main() -> int:
    if not INVENTORY.exists():
        print(f"ERROR: run moc_inventory.py first ({INVENTORY} missing)")
        return 2

    manifest = load()

    # Signal 1 — group by domain
    by_domain: dict[str, list[str]] = defaultdict(list)
    for note in manifest:
        domain = (note.get("domain") or "UNCATEGORIZED").strip() or "UNCATEGORIZED"
        by_domain[domain].append(note["filename"])

    # Signal 2 — tag frequency
    tag_counts: Counter[str] = Counter()
    for note in manifest:
        for tag in note.get("tags") or []:
            if isinstance(tag, str):
                tag_counts[tag] += 1

    # Signal 3 — hub identification (top 5 % by referenced-by-count)
    sorted_notes = sorted(
        manifest, key=lambda n: int(n.get("referenced_by_count") or 0), reverse=True
    )
    cutoff_idx = max(1, len(sorted_notes) // 20)
    hub_threshold = max(20, int(sorted_notes[cutoff_idx].get("referenced_by_count") or 0))
    hubs = [
        {"filename": n["filename"], "count": int(n.get("referenced_by_count") or 0)}
        for n in manifest
        if int(n.get("referenced_by_count") or 0) >= hub_threshold
    ]
    hubs.sort(key=lambda h: h["count"], reverse=True)

    # Signal 4 — outlink-degree centrality
    outlink_targets: Counter[str] = Counter()
    for note in manifest:
        for link in note.get("outlinks") or []:
            outlink_targets[link] += 1
    most_linked = outlink_targets.most_common(50)

    domains_sorted = dict(
        sorted(by_domain.items(), key=lambda kv: -len(kv[1]))
    )

    result = {
        "domains": {k: v for k, v in domains_sorted.items()},
        "domain_sizes": {k: len(v) for k, v in domains_sorted.items()},
        "top_tags": tag_counts.most_common(50),
        "hubs": hubs,
        "most_linked_targets": most_linked,
        "stats": {
            "total_notes": len(manifest),
            "domains_count": len(by_domain),
            "uncategorized_count": len(by_domain.get("UNCATEGORIZED", [])),
            "hub_threshold": hub_threshold,
            "hub_count": len(hubs),
        },
    }
    CLUSTERS_JSON.write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # Human-readable report
    lines: list[str] = [
        "# Cluster Discovery Report",
        "",
        f"- **Total notes**: {result['stats']['total_notes']}",
        f"- **Distinct domains**: {result['stats']['domains_count']}",
        f"- **Uncategorized notes**: {result['stats']['uncategorized_count']}",
        f"- **Hub threshold (refs)**: {result['stats']['hub_threshold']}",
        f"- **Hub count**: {result['stats']['hub_count']}",
        "",
        "## Domains by size",
        "",
        "| Domain | Notes | Tier candidate |",
        "|---|---:|---|",
    ]
    for domain, members in domains_sorted.items():
        n = len(members)
        if n >= 30:
            tier = "Tier-1"
        elif n >= 10:
            tier = "Tier-1 / Tier-2"
        elif n >= 3:
            tier = "Tier-2"
        else:
            tier = "merge upward"
        lines.append(f"| `{domain}` | {n} | {tier} |")

    lines += ["", "## Top 30 tags", "", "| Tag | Count |", "|---|---:|"]
    for tag, count in tag_counts.most_common(30):
        lines.append(f"| `{tag}` | {count} |")

    lines += ["", "## Top 30 hub notes (by referenced-by-count)", "",
              "| Note | Refs |", "|---|---:|"]
    for h in hubs[:30]:
        lines.append(f"| [[{h['filename']}]] | {h['count']} |")

    lines += ["", "## Top 30 outlink targets (most-linked-to notes)", "",
              "| Target | Inbound links |", "|---|---:|"]
    for target, count in most_linked[:30]:
        lines.append(f"| [[{target}]] | {count} |")

    CLUSTERS_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Clusters written -> {CLUSTERS_JSON}")
    print(f"Report written   -> {CLUSTERS_MD}")
    print(f"Domains discovered: {len(by_domain)}, hubs: {len(hubs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
