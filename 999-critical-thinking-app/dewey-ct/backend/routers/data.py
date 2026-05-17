"""
Persistent KV store for DeweyCT client data.

Backs up three localStorage blobs (portfolio, chapterProgress, srsProgress)
to a local SQLite file so that user data survives browser-cache clears.

Endpoints
---------
GET  /api/data  →  { portfolio, chapterProgress, srsProgress }
POST /api/data  →  upsert any/all keys supplied in the request body;
                   unknown keys are silently ignored.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

from fastapi import APIRouter

from services.config import DB_PATH

VALID_KEYS: frozenset[str] = frozenset({"portfolio", "chapterProgress", "srsProgress"})

router = APIRouter()


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _conn() -> sqlite3.Connection:
    """Open (or create) the SQLite DB and ensure the kv table exists."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS kv "
        "(key TEXT PRIMARY KEY, value TEXT NOT NULL)"
    )
    conn.commit()
    return conn


def _read_all() -> dict[str, Any]:
    result: dict[str, Any] = {k: None for k in VALID_KEYS}
    conn = _conn()
    try:
        rows = conn.execute("SELECT key, value FROM kv").fetchall()
    finally:
        conn.close()
    for key, raw in rows:
        if key in VALID_KEYS:
            try:
                result[key] = json.loads(raw)
            except json.JSONDecodeError:
                pass  # leave as None; client will treat missing key as empty
    return result


def _upsert(key: str, value: Any) -> None:
    conn = _conn()
    try:
        conn.execute(
            "INSERT INTO kv (key, value) VALUES (?, ?)"
            " ON CONFLICT(key) DO UPDATE SET value = excluded.value",
            (key, json.dumps(value, ensure_ascii=False)),
        )
        conn.commit()
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@router.get("")
def get_data() -> dict[str, Any]:
    """Return all persisted app data blobs."""
    return _read_all()


@router.post("")
def post_data(body: dict[str, Any]) -> dict[str, str]:
    """Upsert one or more data keys. Unknown keys are silently ignored."""
    for key in VALID_KEYS:
        if key in body:
            _upsert(key, body[key])
    return {"status": "ok"}
