#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared pytest fixtures for the v3 pipeline test suite."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

FIXTURES_DIR: Path = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixtures_dir() -> Path:
    """Return the path to the fixtures directory."""
    return FIXTURES_DIR


@pytest.fixture
def sample_extracted_json() -> dict:
    """Return the parsed contents of the canonical sample _extracted.json."""
    path = FIXTURES_DIR / "sample_extracted.json"
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)
