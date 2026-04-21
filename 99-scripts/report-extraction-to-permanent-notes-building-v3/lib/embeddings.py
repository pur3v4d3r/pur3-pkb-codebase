#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""embeddings.py — bge-small-en-v1.5 wrapper with on-disk cache.

Per spec §2.1:
    Library : sentence-transformers (torch backend, CUDA-capable)
    Model   : BAAI/bge-small-en-v1.5  (384-dim, ~33M params)
    Cache   : .npz file, lazy-loaded, append-only
    Key     : SHA-1 of (filepath, mtime, title, aliases-joined)

Public API:
    EmbeddingStore.load(path)            → load existing cache (or empty)
    EmbeddingStore.encode_missing(items) → compute + cache vectors for new keys
    EmbeddingStore.vectors_for(keys)     → look up (returns numpy array)
    EmbeddingStore.save()                → atomic write back to .npz
    cache_key(filepath, mtime, title, aliases) → str
    load_model(device=None)              → SentenceTransformer
    cosine_similarity(a, b)              → pairwise cosine
"""
from __future__ import annotations

import hashlib
import logging
import os
from collections.abc import Iterable, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)

#: Embedding model identifier.
MODEL_NAME = "BAAI/bge-small-en-v1.5"

#: Embedding dimension produced by ``MODEL_NAME``.
EMBEDDING_DIM = 384

#: Default batch size for encoding (RTX 4090 handles 64 comfortably).
DEFAULT_BATCH_SIZE = 64


def cache_key(
    filepath: str | os.PathLike[str],
    mtime: float,
    title: str,
    aliases: Iterable[str] = (),
) -> str:
    """Return the SHA-1 cache key for a note.

    The key invalidates whenever ``filepath``, file ``mtime``, ``title`` or
    the alias set change. Aliases are sorted so order does not affect the key.
    """
    parts = [
        str(filepath).replace("\\", "/"),
        f"{mtime:.6f}",
        title.strip(),
        "|".join(sorted(a.strip() for a in aliases if a)),
    ]
    blob = "\x1f".join(parts).encode("utf-8")
    return hashlib.sha1(blob).hexdigest()


@dataclass
class EmbeddingItem:
    """One thing to embed — a key + the text fed into the model."""

    key: str
    text: str


@dataclass
class EmbeddingStore:
    """In-memory key→vector map backed by a single ``.npz`` file.

    The file layout is two parallel arrays::

        keys     : (N,)        unicode  — SHA-1 hex strings
        vectors  : (N, dim)    float32  — L2-normalized embeddings

    Lookups are O(1) via the ``_index`` dict built at load time. Writes are
    append-only in memory; ``save()`` rewrites the file atomically.
    """

    path: Path
    dim: int = EMBEDDING_DIM
    _keys: list[str] = field(default_factory=list)
    _vectors: list[np.ndarray] = field(default_factory=list)
    _index: dict[str, int] = field(default_factory=dict)

    # ── load / save ───────────────────────────────────────────────────────

    @classmethod
    def load(cls, path: str | os.PathLike[str], dim: int = EMBEDDING_DIM) -> EmbeddingStore:
        """Load a cache from ``path``; return an empty store if it doesn't exist."""
        p = Path(path)
        store = cls(path=p, dim=dim)
        if not p.exists():
            logger.debug("No cache at %s; starting empty", p)
            return store
        try:
            data = np.load(p, allow_pickle=False)
            keys = data["keys"].tolist()
            vectors = data["vectors"]
            if vectors.ndim == 2 and vectors.shape[1] != dim:
                logger.warning(
                    "Cache dim mismatch (%d vs %d); discarding %s",
                    vectors.shape[1], dim, p,
                )
                return store
            store._keys = list(map(str, keys))
            if vectors.ndim == 2 and vectors.shape[0] > 0:
                store._vectors = [vectors[i] for i in range(vectors.shape[0])]
            store._index = {k: i for i, k in enumerate(store._keys)}
            logger.debug("Loaded %d vectors from %s", len(store._keys), p)
        except (OSError, KeyError, ValueError) as e:
            logger.warning("Cache load failed (%s); starting empty", e)
        return store

    def save(self) -> None:
        """Atomically write the cache to ``self.path``."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        # ``np.savez`` auto-appends ``.npz`` if missing, so we open a binary
        # file handle ourselves to control the exact tmp path.
        tmp = self.path.with_name(self.path.name + ".tmp")
        if not self._keys:
            keys_arr = np.array([], dtype="U40")
            vec_arr = np.zeros((0, self.dim), dtype=np.float32)
        else:
            keys_arr = np.array(self._keys, dtype="U40")
            vec_arr = np.vstack(self._vectors).astype(np.float32, copy=False)
        with open(tmp, "wb") as fh:
            np.savez(fh, keys=keys_arr, vectors=vec_arr)
        tmp.replace(self.path)

    # ── inspection ────────────────────────────────────────────────────────

    def __len__(self) -> int:
        return len(self._keys)

    def __contains__(self, key: object) -> bool:
        return isinstance(key, str) and key in self._index

    def keys(self) -> list[str]:
        return list(self._keys)

    def vector_for(self, key: str) -> np.ndarray | None:
        """Return the vector for ``key`` (or ``None`` if absent)."""
        idx = self._index.get(key)
        return None if idx is None else self._vectors[idx]

    def vectors_for(self, keys: Sequence[str]) -> np.ndarray:
        """Return a stacked ``(len(keys), dim)`` array; missing keys raise ``KeyError``."""
        if not keys:
            return np.zeros((0, self.dim), dtype=np.float32)
        rows = []
        for k in keys:
            idx = self._index.get(k)
            if idx is None:
                raise KeyError(f"vector not in cache: {k}")
            rows.append(self._vectors[idx])
        return np.vstack(rows).astype(np.float32, copy=False)

    def matrix(self) -> tuple[list[str], np.ndarray]:
        """Return ``(keys, matrix)`` for the entire cache (matrix may be empty)."""
        if not self._keys:
            return [], np.zeros((0, self.dim), dtype=np.float32)
        return list(self._keys), np.vstack(self._vectors).astype(np.float32, copy=False)

    # ── mutation ──────────────────────────────────────────────────────────

    def add(self, key: str, vector: np.ndarray) -> None:
        """Insert or overwrite a single vector."""
        v = np.asarray(vector, dtype=np.float32)
        if v.shape != (self.dim,):
            raise ValueError(f"expected shape ({self.dim},), got {v.shape}")
        idx = self._index.get(key)
        if idx is None:
            self._index[key] = len(self._keys)
            self._keys.append(key)
            self._vectors.append(v)
        else:
            self._vectors[idx] = v

    # ── batch encoding ────────────────────────────────────────────────────

    def encode_missing(
        self,
        items: Sequence[EmbeddingItem],
        model: SentenceTransformer,
        *,
        batch_size: int = DEFAULT_BATCH_SIZE,
        show_progress: bool = False,
    ) -> int:
        """Encode any item whose key is not yet cached.

        Returns the count of newly-encoded items. The caller is responsible
        for calling :meth:`save` to persist.
        """
        todo = [it for it in items if it.key not in self._index]
        if not todo:
            return 0
        texts = [it.text for it in todo]
        vectors = model.encode(
            texts,
            batch_size=batch_size,
            normalize_embeddings=True,
            show_progress_bar=show_progress,
            convert_to_numpy=True,
        )
        vectors = np.asarray(vectors, dtype=np.float32)
        if vectors.shape != (len(todo), self.dim):
            raise RuntimeError(
                f"encoder returned shape {vectors.shape}; expected ({len(todo)}, {self.dim})",
            )
        for it, vec in zip(todo, vectors):
            self.add(it.key, vec)
        return len(todo)


def load_model(device: str | None = None) -> SentenceTransformer:
    """Load and return the bge-small model.

    ``device`` defaults to CUDA if available, else CPU. Importing
    sentence-transformers is deferred so unit tests of pure-cache logic do
    not need the full ML stack.
    """
    from sentence_transformers import SentenceTransformer  # local import

    if device is None:
        try:
            import torch
            device = "cuda" if torch.cuda.is_available() else "cpu"
        except Exception:
            device = "cpu"
    logger.info("Loading %s on %s", MODEL_NAME, device)
    return SentenceTransformer(MODEL_NAME, device=device)


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Pairwise cosine similarity between two L2-normalized matrices.

    For unit-norm rows, ``a @ b.T`` is exactly cosine. Inputs that are not
    unit-norm are renormalized first.
    """
    a = np.asarray(a, dtype=np.float32)
    b = np.asarray(b, dtype=np.float32)
    if a.ndim == 1:
        a = a.reshape(1, -1)
    if b.ndim == 1:
        b = b.reshape(1, -1)
    a = _l2_normalize(a)
    b = _l2_normalize(b)
    return a @ b.T


def _l2_normalize(x: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(x, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1.0, norms)
    return x / norms

