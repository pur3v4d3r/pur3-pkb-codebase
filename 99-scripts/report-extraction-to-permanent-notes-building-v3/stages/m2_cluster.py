#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""m2_cluster.py — Phase 2: Embed all stubs, compute cosine similarity, cluster.

Reads 01_scan.json. Generates Ollama embeddings for each stub (cached).
Computes full N×N cosine similarity matrix. Pairs above SIMILARITY_THRESHOLD
are grouped via union-find into clusters.

Pairs where score ≥ AUTO_MERGE_THRESHOLD are flagged `auto_merge=True`
(they bypass LLM verification and interactive review).

Output: merge-state/02_clusters.json
"""
from __future__ import annotations

import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np

_HERE = Path(__file__).resolve().parent.parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import config_merge
from lib.ollama_embeddings import OllamaEmbedder

logger = logging.getLogger(__name__)


# ════════════════════════════════════════════════════════════════════════════
# Union-Find
# ════════════════════════════════════════════════════════════════════════════

class UnionFind:
    """Path-compressed weighted union-find for clustering overlapping pairs."""

    def __init__(self, n: int) -> None:
        self._parent = list(range(n))
        self._rank = [0] * n

    def find(self, x: int) -> int:
        while self._parent[x] != x:
            self._parent[x] = self._parent[self._parent[x]]  # path compression
            x = self._parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self._rank[rx] < self._rank[ry]:
            rx, ry = ry, rx
        self._parent[ry] = rx
        if self._rank[rx] == self._rank[ry]:
            self._rank[rx] += 1

    def clusters(self) -> dict[int, list[int]]:
        """Return {root: [member_indices]} for groups with 2+ members."""
        from collections import defaultdict
        groups: dict[int, list[int]] = defaultdict(list)
        for i in range(len(self._parent)):
            groups[self.find(i)].append(i)
        return {k: v for k, v in groups.items() if len(v) >= 2}


# ════════════════════════════════════════════════════════════════════════════
# Main
# ════════════════════════════════════════════════════════════════════════════

def _load_scan(state_dir: Path) -> dict[str, Any]:
    path = state_dir / config_merge.SCAN_STATE_FILE
    if not path.exists():
        raise FileNotFoundError(f"Run --scan first. Missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _embedding_text(stub: dict[str, Any]) -> str:
    """Build the text to embed for a stub."""
    title = stub.get("title", "")
    defn = (stub.get("definition_text") or "").strip()
    if defn:
        return f"{title} — {defn[:200]}"
    return title


def run(state_dir: Path | None = None) -> dict[str, Any]:
    """Embed stubs, cluster by cosine similarity, write 02_clusters.json."""
    state_dir = state_dir or config_merge.MERGE_STATE_DIR

    scan = _load_scan(state_dir)
    stubs: list[dict[str, Any]] = scan["stubs"]
    tier0_clusters: list[dict[str, Any]] = scan.get("tier0_clusters", [])

    logger.info("Loaded %d stubs from scan.", len(stubs))

    # Build set of (path_a, path_b) pairs already covered by TIER-0
    tier0_pairs: set[frozenset[str]] = set()
    for c in tier0_clusters:
        paths = [m["path"] for m in c["members"]]
        for i, pa in enumerate(paths):
            for pb in paths[i + 1:]:
                tier0_pairs.add(frozenset({pa, pb}))

    # ── Embedding ──────────────────────────────────────────────────────────

    texts = [_embedding_text(s) for s in stubs]
    path_index = [s["path"] for s in stubs]

    logger.info("Generating embeddings via Ollama (%s)...", config_merge.EMBEDDING_MODEL)

    with OllamaEmbedder(
        model=config_merge.EMBEDDING_MODEL,
        url=config_merge.OLLAMA_URL,
        cache_path=config_merge.MERGE_EMBED_CACHE,
        timeout_s=config_merge.EMBED_REQUEST_TIMEOUT_S,
        batch_size=config_merge.EMBED_BATCH_SIZE,
    ) as embedder:
        if not embedder.ping():
            raise RuntimeError(
                f"Ollama not reachable at {config_merge.OLLAMA_URL}. "
                "Ensure Ollama is running before running --cluster."
            )
        vectors = embedder.encode(texts, show_progress=True)

    logger.info("Embeddings ready. Shape: %s", vectors.shape)

    # ── Cosine similarity matrix ───────────────────────────────────────────
    # vectors are already L2-normalized → cosine = dot product

    logger.info("Computing %d×%d cosine similarity matrix...", len(stubs), len(stubs))
    sim: np.ndarray = (vectors @ vectors.T).astype(np.float32)

    # ── Find pairs above threshold ─────────────────────────────────────────

    N = len(stubs)
    rows, cols = np.triu_indices(N, k=1)
    scores = sim[rows, cols]

    mask = scores >= config_merge.SIMILARITY_THRESHOLD
    candidate_rows = rows[mask]
    candidate_cols = cols[mask]
    candidate_scores = scores[mask]

    logger.info(
        "Pairs above threshold %.2f: %d (out of %d)",
        config_merge.SIMILARITY_THRESHOLD,
        int(mask.sum()),
        len(scores),
    )

    # ── Union-Find clustering ──────────────────────────────────────────────

    uf = UnionFind(N)
    # Track max pairwise score per potential cluster root (for auto_merge flag)
    pair_score_map: dict[tuple[int, int], float] = {}

    for i, j, s in zip(
        candidate_rows.tolist(),
        candidate_cols.tolist(),
        candidate_scores.tolist(),
    ):
        pa, pb = path_index[i], path_index[j]
        # Skip pairs already covered by the same TIER-0 cluster
        if frozenset({pa, pb}) in tier0_pairs:
            continue
        uf.union(i, j)
        pair_score_map[(min(i, j), max(i, j))] = float(s)

    raw_clusters = uf.clusters()
    logger.info("Clusters found: %d", len(raw_clusters))

    # ── Build cluster output objects ───────────────────────────────────────

    clusters: list[dict[str, Any]] = []
    for cluster_idx, (root, members) in enumerate(sorted(raw_clusters.items())):
        member_paths = [path_index[m] for m in members]

        # Compute pairwise scores within this cluster
        cluster_scores: list[float] = []
        for ii in range(len(members)):
            for jj in range(ii + 1, len(members)):
                a, b = min(members[ii], members[jj]), max(members[ii], members[jj])
                s = pair_score_map.get((a, b), float(sim[members[ii], members[jj]]))
                cluster_scores.append(s)

        max_score = max(cluster_scores) if cluster_scores else 0.0
        mean_score = float(np.mean(cluster_scores)) if cluster_scores else 0.0
        auto_merge = max_score >= config_merge.AUTO_MERGE_THRESHOLD

        clusters.append({
            "cluster_id": f"c2-{cluster_idx:04d}",
            "tier": 1,
            "auto_merge": auto_merge,
            "members": [{"path": p} for p in sorted(member_paths)],
            "max_pair_score": round(max_score, 4),
            "mean_pair_score": round(mean_score, 4),
        })

    # Drop oversized clusters — single-linkage Union-Find can chain unrelated
    # stubs transitively, producing huge spurious clusters.
    oversized = [c for c in clusters if len(c["members"]) > config_merge.MAX_CLUSTER_SIZE]
    clusters = [c for c in clusters if len(c["members"]) <= config_merge.MAX_CLUSTER_SIZE]
    if oversized:
        logger.info(
            "Dropped %d oversized cluster(s) (>%d members): %s",
            len(oversized),
            config_merge.MAX_CLUSTER_SIZE,
            ", ".join(f'{c["cluster_id"]}({len(c["members"])} members)' for c in oversized),
        )

    auto_count = sum(1 for c in clusters if c["auto_merge"])
    logger.info(
        "Clusters: %d total (%d auto-merge, %d need LLM)",
        len(clusters), auto_count, len(clusters) - auto_count,
    )

    output: dict[str, Any] = {
        "generated_at": datetime.now().isoformat(),
        "similarity_threshold": config_merge.SIMILARITY_THRESHOLD,
        "auto_merge_threshold": config_merge.AUTO_MERGE_THRESHOLD,
        "total_stubs": len(stubs),
        "tier0_clusters_excluded": len(tier0_clusters),
        "total_clusters": len(clusters),
        "auto_merge_clusters": auto_count,
        "clusters": clusters,
    }

    out_path = state_dir / config_merge.CLUSTER_STATE_FILE
    _write_json_atomic(out_path, output)
    logger.info("Phase 2 complete → %s", out_path)
    return output


def _write_json_atomic(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)
