#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for lib.embeddings — pure cache + key logic (no model required).

Run with:
    pytest tests/test_embeddings.py -v
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

_HERE = Path(__file__).resolve().parent
_V3_ROOT = _HERE.parent
if str(_V3_ROOT) not in sys.path:
    sys.path.insert(0, str(_V3_ROOT))

from lib.embeddings import (  # noqa: E402
    EMBEDDING_DIM,
    EmbeddingItem,
    EmbeddingStore,
    cache_key,
    cosine_similarity,
)


# ─── cache_key ───────────────────────────────────────────────────────────

def test_cache_key_is_stable() -> None:
    k1 = cache_key("notes/Foo.md", 1.0, "Foo", ["bar", "baz"])
    k2 = cache_key("notes/Foo.md", 1.0, "Foo", ["bar", "baz"])
    assert k1 == k2


def test_cache_key_alias_order_irrelevant() -> None:
    k1 = cache_key("notes/Foo.md", 1.0, "Foo", ["bar", "baz"])
    k2 = cache_key("notes/Foo.md", 1.0, "Foo", ["baz", "bar"])
    assert k1 == k2


def test_cache_key_path_separators_normalized() -> None:
    k1 = cache_key("notes/Foo.md", 1.0, "Foo", [])
    k2 = cache_key("notes\\Foo.md", 1.0, "Foo", [])
    assert k1 == k2


def test_cache_key_invalidates_on_path() -> None:
    k1 = cache_key("notes/Foo.md", 1.0, "Foo", [])
    k2 = cache_key("notes/Bar.md", 1.0, "Foo", [])
    assert k1 != k2


def test_cache_key_invalidates_on_mtime() -> None:
    k1 = cache_key("notes/Foo.md", 1.0, "Foo", [])
    k2 = cache_key("notes/Foo.md", 2.0, "Foo", [])
    assert k1 != k2


def test_cache_key_invalidates_on_title() -> None:
    k1 = cache_key("notes/Foo.md", 1.0, "Foo", [])
    k2 = cache_key("notes/Foo.md", 1.0, "Bar", [])
    assert k1 != k2


def test_cache_key_invalidates_on_aliases() -> None:
    k1 = cache_key("notes/Foo.md", 1.0, "Foo", ["a"])
    k2 = cache_key("notes/Foo.md", 1.0, "Foo", ["a", "b"])
    assert k1 != k2


# ─── EmbeddingStore: load on missing ─────────────────────────────────────

def test_load_missing_returns_empty(tmp_path: Path) -> None:
    store = EmbeddingStore.load(tmp_path / "nope.npz")
    assert len(store) == 0
    assert store.keys() == []


# ─── EmbeddingStore: add + lookup ────────────────────────────────────────

def test_add_and_lookup() -> None:
    store = EmbeddingStore(path=Path("ignored"))
    v = np.ones(EMBEDDING_DIM, dtype=np.float32)
    store.add("k1", v)
    assert "k1" in store
    assert len(store) == 1
    np.testing.assert_array_equal(store.vector_for("k1"), v)


def test_add_overwrites_existing() -> None:
    store = EmbeddingStore(path=Path("ignored"))
    v1 = np.ones(EMBEDDING_DIM, dtype=np.float32)
    v2 = np.full(EMBEDDING_DIM, 2.0, dtype=np.float32)
    store.add("k", v1)
    store.add("k", v2)
    assert len(store) == 1
    np.testing.assert_array_equal(store.vector_for("k"), v2)


def test_add_rejects_wrong_shape() -> None:
    store = EmbeddingStore(path=Path("ignored"))
    with pytest.raises(ValueError):
        store.add("k", np.zeros(7, dtype=np.float32))


def test_vectors_for_returns_stacked() -> None:
    store = EmbeddingStore(path=Path("ignored"))
    store.add("a", np.full(EMBEDDING_DIM, 0.1, dtype=np.float32))
    store.add("b", np.full(EMBEDDING_DIM, 0.2, dtype=np.float32))
    m = store.vectors_for(["b", "a"])
    assert m.shape == (2, EMBEDDING_DIM)
    assert m[0, 0] == pytest.approx(0.2)
    assert m[1, 0] == pytest.approx(0.1)


def test_vectors_for_missing_raises() -> None:
    store = EmbeddingStore(path=Path("ignored"))
    with pytest.raises(KeyError):
        store.vectors_for(["does-not-exist"])


def test_vectors_for_empty_returns_empty_matrix() -> None:
    store = EmbeddingStore(path=Path("ignored"))
    m = store.vectors_for([])
    assert m.shape == (0, EMBEDDING_DIM)


def test_matrix_returns_keys_and_array() -> None:
    store = EmbeddingStore(path=Path("ignored"))
    store.add("a", np.ones(EMBEDDING_DIM, dtype=np.float32))
    store.add("b", np.zeros(EMBEDDING_DIM, dtype=np.float32))
    keys, mat = store.matrix()
    assert keys == ["a", "b"]
    assert mat.shape == (2, EMBEDDING_DIM)


def test_matrix_empty_store() -> None:
    store = EmbeddingStore(path=Path("ignored"))
    keys, mat = store.matrix()
    assert keys == []
    assert mat.shape == (0, EMBEDDING_DIM)


# ─── EmbeddingStore: roundtrip ───────────────────────────────────────────

def test_save_and_load_roundtrip(tmp_path: Path) -> None:
    p = tmp_path / "cache.npz"
    s1 = EmbeddingStore(path=p)
    s1.add("a", np.full(EMBEDDING_DIM, 0.5, dtype=np.float32))
    s1.add("b", np.full(EMBEDDING_DIM, -0.25, dtype=np.float32))
    s1.save()
    assert p.exists()

    s2 = EmbeddingStore.load(p)
    assert len(s2) == 2
    assert s2.keys() == ["a", "b"]
    np.testing.assert_allclose(s2.vector_for("a"), s1.vector_for("a"))
    np.testing.assert_allclose(s2.vector_for("b"), s1.vector_for("b"))


def test_save_empty_store(tmp_path: Path) -> None:
    p = tmp_path / "cache.npz"
    s1 = EmbeddingStore(path=p)
    s1.save()
    assert p.exists()
    s2 = EmbeddingStore.load(p)
    assert len(s2) == 0


def test_load_dim_mismatch_returns_empty(tmp_path: Path) -> None:
    p = tmp_path / "cache.npz"
    s1 = EmbeddingStore(path=p, dim=10)
    s1.add("k", np.ones(10, dtype=np.float32))
    s1.save()
    s2 = EmbeddingStore.load(p, dim=EMBEDDING_DIM)
    assert len(s2) == 0


# ─── encode_missing (with stub model) ────────────────────────────────────

class _StubModel:
    """Mimics SentenceTransformer.encode for unit testing."""

    def __init__(self) -> None:
        self.calls: list[list[str]] = []

    def encode(self, texts, **_kwargs):
        self.calls.append(list(texts))
        # Return deterministic L2-normalized vectors based on text hash.
        out = np.zeros((len(texts), EMBEDDING_DIM), dtype=np.float32)
        for i, t in enumerate(texts):
            h = hash(t) & 0xFFFFFFFF
            out[i, h % EMBEDDING_DIM] = 1.0
        return out


def test_encode_missing_only_encodes_new_keys() -> None:
    store = EmbeddingStore(path=Path("ignored"))
    model = _StubModel()
    items = [EmbeddingItem(key="a", text="alpha"), EmbeddingItem(key="b", text="beta")]
    n = store.encode_missing(items, model)
    assert n == 2
    assert len(store) == 2
    # Second call: nothing new.
    n2 = store.encode_missing(items, model)
    assert n2 == 0
    assert len(model.calls) == 1


def test_encode_missing_filters_partial() -> None:
    store = EmbeddingStore(path=Path("ignored"))
    store.add("a", np.ones(EMBEDDING_DIM, dtype=np.float32))
    model = _StubModel()
    items = [EmbeddingItem(key="a", text="alpha"), EmbeddingItem(key="b", text="beta")]
    n = store.encode_missing(items, model)
    assert n == 1
    assert model.calls == [["beta"]]


def test_encode_missing_empty() -> None:
    store = EmbeddingStore(path=Path("ignored"))
    n = store.encode_missing([], _StubModel())
    assert n == 0


# ─── cosine_similarity ───────────────────────────────────────────────────

def test_cosine_identical_vectors() -> None:
    v = np.ones((1, EMBEDDING_DIM), dtype=np.float32)
    sim = cosine_similarity(v, v)
    assert sim.shape == (1, 1)
    assert sim[0, 0] == pytest.approx(1.0, abs=1e-6)


def test_cosine_orthogonal_vectors() -> None:
    a = np.zeros((1, EMBEDDING_DIM), dtype=np.float32)
    b = np.zeros((1, EMBEDDING_DIM), dtype=np.float32)
    a[0, 0] = 1.0
    b[0, 1] = 1.0
    sim = cosine_similarity(a, b)
    assert sim[0, 0] == pytest.approx(0.0, abs=1e-6)


def test_cosine_handles_1d_inputs() -> None:
    a = np.ones(EMBEDDING_DIM, dtype=np.float32)
    b = np.ones(EMBEDDING_DIM, dtype=np.float32)
    sim = cosine_similarity(a, b)
    assert sim.shape == (1, 1)
    assert sim[0, 0] == pytest.approx(1.0, abs=1e-6)


def test_cosine_renormalizes_non_unit_inputs() -> None:
    a = np.full((1, EMBEDDING_DIM), 5.0, dtype=np.float32)
    b = np.full((1, EMBEDDING_DIM), 0.1, dtype=np.float32)
    sim = cosine_similarity(a, b)
    assert sim[0, 0] == pytest.approx(1.0, abs=1e-5)


def test_cosine_pairwise_matrix() -> None:
    a = np.eye(3, EMBEDDING_DIM, dtype=np.float32)  # 3 unit basis vectors
    b = np.eye(3, EMBEDDING_DIM, dtype=np.float32)
    sim = cosine_similarity(a, b)
    assert sim.shape == (3, 3)
    np.testing.assert_allclose(sim, np.eye(3), atol=1e-6)
