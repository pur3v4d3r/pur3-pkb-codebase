#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ollama_embeddings.py — Ollama /api/embed wrapper with .npz cache.

Uses Ollama's native embedding endpoint (nomic-embed-text, 768-dim) rather
than the sentence-transformers model used by the main pipeline. Operates
independently of lib/embeddings.py to avoid dimension/model conflicts.

Public API:
    OllamaEmbedder(model, url, cache_path, timeout_s) — context manager
    OllamaEmbedder.encode(texts) → np.ndarray   # (N, 768) float32, L2-normed
    OllamaEmbedder.save()                        # flush cache to disk
"""
from __future__ import annotations

import hashlib
import json
import logging
from pathlib import Path
from typing import Any

import numpy as np
import requests

logger = logging.getLogger(__name__)

_EMBED_ENDPOINT = "/api/embed"


# ════════════════════════════════════════════════════════════════════════════
# Cache helpers
# ════════════════════════════════════════════════════════════════════════════

class _EmbedCache:
    """Simple key → float32-vector cache backed by a .npz file."""

    def __init__(self, path: Path | None) -> None:
        self._path = path
        self._store: dict[str, np.ndarray] = {}
        self._dirty = False
        if path is not None and path.exists():
            self._load()

    def _load(self) -> None:
        try:
            data = np.load(str(self._path), allow_pickle=False)
            keys = data["keys"].tolist()
            vecs = data["vectors"]
            for k, v in zip(keys, vecs):
                self._store[k] = v
            logger.debug("Loaded %d cached embeddings from %s", len(self._store), self._path)
        except Exception as e:
            logger.warning("Failed to load embed cache %s: %s", self._path, e)
            self._store = {}

    def get(self, key: str) -> np.ndarray | None:
        return self._store.get(key)

    def set(self, key: str, vec: np.ndarray) -> None:
        self._store[key] = vec
        self._dirty = True

    def save(self) -> None:
        if not self._dirty or self._path is None:
            return
        self._path.parent.mkdir(parents=True, exist_ok=True)
        keys = list(self._store.keys())
        vecs = np.stack(list(self._store.values()), axis=0).astype(np.float32)
        # np.savez_compressed appends .npz automatically when the path doesn't
        # end with .npz. Save to a bare-stem temp path so numpy creates
        # <stem>.tmp.npz, then rename that to the target path.
        tmp_stem = self._path.parent / (self._path.stem + ".tmp")
        np.savez_compressed(str(tmp_stem), keys=np.array(keys), vectors=vecs)
        tmp_actual = Path(str(tmp_stem) + ".npz")  # what numpy actually created
        tmp_actual.replace(self._path)
        self._dirty = False
        logger.debug("Saved %d embeddings to %s", len(keys), self._path)


def _embed_key(model: str, text: str) -> str:
    h = hashlib.sha1()
    h.update(model.encode("utf-8"))
    h.update(b"\x00")
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def _l2_normalize(arr: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(arr, axis=1, keepdims=True)
    norms = np.where(norms == 0.0, 1.0, norms)
    return arr / norms


# ════════════════════════════════════════════════════════════════════════════
# Embedder
# ════════════════════════════════════════════════════════════════════════════

class OllamaEmbedder:
    """Batch-embedding client for Ollama's /api/embed endpoint.

    Usage::

        with OllamaEmbedder(
            model="nomic-embed-text",
            url="http://localhost:11434",
            cache_path=Path("merge-embeddings.npz"),
        ) as embedder:
            vectors = embedder.encode(["text one", "text two"])
            # vectors.shape == (2, 768), float32, L2-normalized

    The cache is flushed to disk on context-manager exit.
    """

    def __init__(
        self,
        model: str,
        url: str = "http://localhost:11434",
        cache_path: Path | None = None,
        timeout_s: float = 180.0,
        batch_size: int = 32,
    ) -> None:
        self.model = model
        self.url = url.rstrip("/")
        self.timeout_s = timeout_s
        self.batch_size = batch_size
        self._cache = _EmbedCache(cache_path)
        self._session: requests.Session | None = None

    def __enter__(self) -> "OllamaEmbedder":
        self._session = requests.Session()
        return self

    def __exit__(self, *_: Any) -> None:
        self.save()
        if self._session is not None:
            self._session.close()
            self._session = None

    @property
    def session(self) -> requests.Session:
        if self._session is None:
            self._session = requests.Session()
        return self._session

    def encode(self, texts: list[str], *, show_progress: bool = True) -> np.ndarray:
        """Return L2-normalized embedding matrix for ``texts``.

        Cache-hits are served instantly; cache-misses call Ollama in batches
        of ``batch_size``.

        Args:
            texts: Input strings to embed.
            show_progress: Log progress every batch (info level).

        Returns:
            ``np.ndarray`` of shape ``(len(texts), dim)`` float32, L2-normalized.
        """
        dim = None
        keys = [_embed_key(self.model, t) for t in texts]

        # Phase 1: identify which texts need encoding
        missing_indices: list[int] = []
        for i, key in enumerate(keys):
            if self._cache.get(key) is None:
                missing_indices.append(i)

        cache_hits = len(texts) - len(missing_indices)
        if missing_indices:
            logger.info(
                "Embedding: %d cache hits, %d to encode via Ollama...",
                cache_hits, len(missing_indices),
            )

        # Phase 2: batch-encode missing texts
        for batch_start in range(0, len(missing_indices), self.batch_size):
            batch_idx = missing_indices[batch_start: batch_start + self.batch_size]
            batch_texts = [texts[i] for i in batch_idx]

            if show_progress:
                logger.info(
                    "  Embedding batch %d–%d / %d",
                    batch_start + 1,
                    min(batch_start + self.batch_size, len(missing_indices)),
                    len(missing_indices),
                )

            vecs = self._call_ollama(batch_texts)
            normed = _l2_normalize(vecs)
            dim = normed.shape[1]

            for local_i, global_i in enumerate(batch_idx):
                self._cache.set(keys[global_i], normed[local_i])

        # Phase 3: assemble result matrix
        if dim is None:
            # All from cache — determine dim from first cached vector
            first = self._cache.get(keys[0])
            dim = first.shape[0] if first is not None else 768

        result = np.zeros((len(texts), dim), dtype=np.float32)
        for i, key in enumerate(keys):
            cached = self._cache.get(key)
            if cached is not None:
                result[i] = cached
            else:
                logger.warning("Missing embedding for index %d after encoding", i)

        return result

    def save(self) -> None:
        """Flush the embedding cache to disk."""
        self._cache.save()

    def _call_ollama(self, texts: list[str]) -> np.ndarray:
        """POST to /api/embed and return raw (N, dim) float32 array."""
        endpoint = f"{self.url}{_EMBED_ENDPOINT}"
        r = self.session.post(
            endpoint,
            json={"model": self.model, "input": texts},
            timeout=self.timeout_s,
        )
        r.raise_for_status()
        data = r.json()

        # Ollama v0.3+ → {"embeddings": [[...]]}
        # Older Ollama → {"embedding": [...]} (single input only)
        if "embeddings" in data:
            raw = data["embeddings"]
        elif "embedding" in data:
            raw = [data["embedding"]]
        else:
            raise ValueError(f"Unexpected Ollama embed response keys: {list(data)}")

        if len(raw) != len(texts):
            raise ValueError(
                f"Ollama returned {len(raw)} embeddings for {len(texts)} inputs"
            )

        return np.array(raw, dtype=np.float32)

    def ping(self) -> bool:
        """Return True if Ollama responds to /api/tags."""
        try:
            r = self.session.get(f"{self.url}/api/tags", timeout=5.0)
            return r.status_code == 200
        except Exception:
            return False
