#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for synth_seed_builder.

Run with:
    pytest test_synth_seed_builder.py -v
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

import synth_seed_builder as sb


# ─── Fixtures ───────────────────────────────────────────────────────────

@pytest.fixture
def minimal_brief() -> dict:
    return {
        "concept": "Spaced Retrieval",
        "domain": "cognitive-science",
        "aliases": ["Spaced Retrieval Practice"],
        "related": ["testing-effect", "desirable-difficulties"],
        "broader": ["retrieval-practice"],
        "callouts": [
            {
                "type": "definition",
                "title": "Spaced Retrieval",
                "body": (
                    "Spaced Retrieval is a learning technique that combines "
                    "retrieval practice with distributed practice over time.\n\n"
                    "**See also:** [[testing-effect]], [[retrieval-practice]]"
                ),
            },
            {
                "type": "key-claim",
                "title": "Retention scales with spacing interval",
                "body": (
                    "The Spaced Retrieval effect shows that retention scales "
                    "with the spacing interval up to a domain-specific optimum."
                ),
            },
            {
                "type": "example",
                "title": "Vocabulary review schedule",
                "body": (
                    "A learner reviewing 50 vocabulary items via Spaced Retrieval "
                    "at expanding intervals (1d, 3d, 7d) shows substantially "
                    "better one-month retention than blocked review."
                ),
            },
        ],
    }


@pytest.fixture
def schema() -> dict:
    return sb._load_schema(sb.DEFAULT_SCHEMA_PATH)


# ─── Title cleaning ─────────────────────────────────────────────────────

@pytest.mark.parametrize("raw,expected", [
    ("Spaced Retrieval", "Spaced Retrieval"),
    ("Spaced Retrieval (Bjork, 1994)", "Spaced Retrieval"),
    ("Spaced Retrieval — a memory technique", "Spaced Retrieval"),
    ("  Spaced Retrieval  ", "Spaced Retrieval"),
    ("[[Spaced Retrieval]]", "Spaced Retrieval"),
    ("", ""),
])
def test_clean_title(raw: str, expected: str) -> None:
    assert sb.clean_title(raw) == expected


# ─── Kebab transform ────────────────────────────────────────────────────

@pytest.mark.parametrize("raw,expected", [
    ("Spaced Retrieval", "spaced-retrieval"),
    ("Cognitive Science", "cognitive-science"),
    ("Already-Kebab", "already-kebab"),
    ("Mixed — Punctuation!", "mixed-punctuation"),
])
def test_to_kebab(raw: str, expected: str) -> None:
    assert sb.to_kebab(raw) == expected


# ─── build_seed happy path ──────────────────────────────────────────────

def test_build_seed_happy_path(minimal_brief: dict) -> None:
    seed = sb.build_seed(minimal_brief)
    assert seed["extraction_metadata"]["script_name"] == "synth_seed_builder.py"
    assert seed["extraction_metadata"]["synthetic"] is True
    fm = seed["document_metadata"]["frontmatter"]
    assert fm["primary_domain"] == "cognitive-science"
    assert "Spaced Retrieval" in fm["aliases"]
    assert any("[[testing-effect]]" == x for x in fm["related"])
    callouts = seed["extracted_items"]["callouts"]
    assert len(callouts) == 3
    assert callouts[0]["type"] == "definition"
    targets = seed["knowledge_graph"]["unique_wiki_link_targets"]
    assert "testing-effect" in targets
    assert "retrieval-practice" in targets
    # Bare-slug invariant.
    for t in targets:
        assert "[" not in t and "|" not in t


def test_filename_for(minimal_brief: dict) -> None:
    import datetime as dt
    name = sb.filename_for(minimal_brief, batch_date=dt.date(2026, 4, 24))
    assert name == "spaced-retrieval-synthetic-seed-2026-04-24_extracted.json"


# ─── load_brief errors ──────────────────────────────────────────────────

def test_load_brief_missing_file(tmp_path: Path) -> None:
    with pytest.raises(sb.BriefError, match="not found"):
        sb.load_brief(tmp_path / "nope.yaml")


def test_load_brief_missing_concept(tmp_path: Path) -> None:
    p = tmp_path / "bad.yaml"
    p.write_text("domain: x\ncallouts: []\n", encoding="utf-8")
    with pytest.raises(sb.BriefError, match="concept"):
        sb.load_brief(p)


def test_load_brief_missing_callouts(tmp_path: Path) -> None:
    p = tmp_path / "bad.yaml"
    p.write_text("concept: X\ndomain: y\n", encoding="utf-8")
    with pytest.raises(sb.BriefError, match="callouts"):
        sb.load_brief(p)


# ─── validate_seed ──────────────────────────────────────────────────────

def test_validate_seed_clean(minimal_brief: dict, schema: dict, tmp_path: Path) -> None:
    seed = sb.build_seed(minimal_brief)
    fname = sb.filename_for(minimal_brief)
    report = sb.validate_seed(seed, tmp_path / fname, schema=schema)
    assert report.ok, "Clean seed should validate cleanly: " + str([i.render() for i in report.errors])


def test_validate_seed_missing_definition(schema: dict, tmp_path: Path) -> None:
    seed = {
        "document_metadata": {"frontmatter": {"title": "X", "primary_domain": "x"}},
        "extracted_items": {"callouts": [
            {"type": "example", "title": "E", "body": "body"},
        ]},
    }
    report = sb.validate_seed(seed, tmp_path / "x_extracted.json", schema=schema)
    assert not report.ok
    assert any("definition" in i.message.lower() for i in report.errors)


def test_validate_seed_substring_violation(minimal_brief: dict, schema: dict, tmp_path: Path) -> None:
    seed = sb.build_seed(minimal_brief)
    # Sabotage one support body: strip the concept name.
    seed["extracted_items"]["callouts"][1]["body"] = "Totally unrelated text without the keyword."
    seed["extracted_items"]["callouts"][1]["title"] = "Unrelated title"
    fname = sb.filename_for(minimal_brief)
    report = sb.validate_seed(seed, tmp_path / fname, schema=schema)
    assert not report.ok
    assert any("substring" in i.message.lower() for i in report.errors)


def test_validate_seed_bad_filename(minimal_brief: dict, schema: dict, tmp_path: Path) -> None:
    seed = sb.build_seed(minimal_brief)
    report = sb.validate_seed(seed, tmp_path / "wrong-suffix.json", schema=schema)
    assert any("_extracted.json" in i.message for i in report.errors)


def test_validate_seed_non_kebab_domain(minimal_brief: dict, schema: dict, tmp_path: Path) -> None:
    seed = sb.build_seed(minimal_brief)
    seed["document_metadata"]["frontmatter"]["primary_domain"] = "Cognitive Science"
    fname = sb.filename_for(minimal_brief)
    report = sb.validate_seed(seed, tmp_path / fname, schema=schema)
    assert any("kebab" in i.message.lower() for i in report.errors)


# ─── discover_seeds ─────────────────────────────────────────────────────

def test_discover_seeds_dir(tmp_path: Path) -> None:
    (tmp_path / "a_extracted.json").write_text("{}")
    (tmp_path / "b_extracted.json").write_text("{}")
    (tmp_path / "ignore.txt").write_text("nope")
    found = sb.discover_seeds(tmp_path)
    assert len(found) == 2


def test_discover_seeds_file(tmp_path: Path) -> None:
    p = tmp_path / "x_extracted.json"
    p.write_text("{}")
    assert sb.discover_seeds(p) == [p]


def test_discover_seeds_nonexistent(tmp_path: Path) -> None:
    assert sb.discover_seeds(tmp_path / "missing") == []


# ─── CLI integration ────────────────────────────────────────────────────

def test_cli_help(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(SystemExit) as exc:
        sb.main(["--help"])
    assert exc.value.code == 0
    out = capsys.readouterr().out
    assert "build" in out and "validate" in out


def test_cli_version(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(SystemExit) as exc:
        sb.main(["--version"])
    assert exc.value.code == 0


def test_cli_build_dry_run(tmp_path: Path, minimal_brief: dict, capsys: pytest.CaptureFixture) -> None:
    import yaml
    brief_path = tmp_path / "brief.yaml"
    brief_path.write_text(yaml.safe_dump(minimal_brief), encoding="utf-8")
    out_dir = tmp_path / "out"
    rc = sb.main([
        "build", str(brief_path), "--out-dir", str(out_dir),
        "--dry-run", "--no-validate",
    ])
    assert rc == 0
    # Dry-run must not create the output directory.
    assert not (out_dir / sb.filename_for(minimal_brief)).exists()
    out = capsys.readouterr().out
    assert "Spaced Retrieval" in out
    parsed = json.loads(out)
    assert parsed["extraction_metadata"]["synthetic"] is True


def test_cli_build_writes_file(tmp_path: Path, minimal_brief: dict) -> None:
    import yaml
    brief_path = tmp_path / "brief.yaml"
    brief_path.write_text(yaml.safe_dump(minimal_brief), encoding="utf-8")
    out_dir = tmp_path / "out"
    rc = sb.main(["build", str(brief_path), "--out-dir", str(out_dir)])
    assert rc == 0
    written = out_dir / sb.filename_for(minimal_brief)
    assert written.exists()
    seed = json.loads(written.read_text(encoding="utf-8"))
    assert seed["document_metadata"]["frontmatter"]["primary_domain"] == "cognitive-science"


def test_cli_validate_clean_dir(tmp_path: Path, minimal_brief: dict) -> None:
    import yaml
    brief_path = tmp_path / "brief.yaml"
    brief_path.write_text(yaml.safe_dump(minimal_brief), encoding="utf-8")
    out_dir = tmp_path / "out"
    sb.main(["build", str(brief_path), "--out-dir", str(out_dir)])
    rc = sb.main(["validate", str(out_dir)])
    assert rc == 0


def test_cli_validate_no_inputs(tmp_path: Path) -> None:
    rc = sb.main(["validate", str(tmp_path / "empty")])
    assert rc == 4
