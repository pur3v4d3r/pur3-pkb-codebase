#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Smoke tests for Phase 0 scaffolding.

Verifies the v3 layout is importable and the sample fixture parses. Real
behavioral tests land alongside each phase's modules.
"""
from __future__ import annotations

from pathlib import Path

import pytest


def test_config_v3_imports() -> None:
    """``config_v3`` imports cleanly and exposes core paths."""
    import config_v3

    assert config_v3.PIPELINE_VERSION.startswith("3.")
    assert isinstance(config_v3.VAULT_ROOT, Path)
    assert isinstance(config_v3.PERMANENT_NOTES_DIR, Path)


def test_pipeline_v3_imports() -> None:
    """``pipeline_v3`` imports cleanly and exposes the stage list."""
    import pipeline_v3

    assert len(pipeline_v3.STAGES) == 12
    assert pipeline_v3.STAGES[0][1] == "extract"
    assert pipeline_v3.STAGES[-1][1] == "commit"


def test_lib_modules_importable() -> None:
    """Every ``lib/`` module imports without side effects."""
    from lib import (  # noqa: F401
        candidate,
        embeddings,
        frontmatter,
        link_validator,
        llm_client,
        markdown,
        parallel,
        state,
        ui,
    )


def test_stages_modules_importable() -> None:
    """Every ``stages/`` module imports without side effects."""
    from stages import (  # noqa: F401
        s1_extract,
        s2_validate,
        s3_consolidate,
        s4_normalize,
        s5_match,
        s6_render,
        s7_stubs,
        s8_resolve_links,
        s9_normalize_links,
        s10_audit,
        s11_moc,
        s12_commit,
    )


def test_sample_fixture_parses(sample_extracted_json: dict) -> None:
    """The canonical sample ``_extracted.json`` parses and has the v1.1 shape."""
    assert isinstance(sample_extracted_json, dict)
    # pkb_extractor v1.1.0 emits these top-level keys
    assert "document_metadata" in sample_extracted_json
    assert "extraction_metadata" in sample_extracted_json
    extraction_meta = sample_extracted_json["extraction_metadata"]
    assert extraction_meta.get("script_name") == "pkb_extractor.py"


def test_link_validator_implemented() -> None:
    """Phase 1 landed: ``is_valid_concept`` is implemented and callable."""
    from lib.link_validator import is_valid_concept

    valid, reason = is_valid_concept("Self-Determination Theory")
    assert valid is True
    assert reason == ""
