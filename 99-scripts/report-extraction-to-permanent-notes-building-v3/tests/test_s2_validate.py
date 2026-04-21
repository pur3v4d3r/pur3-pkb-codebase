#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for ``stages.s2_validate``.

Covers:
- Pure-function validation against the canonical sample fixture
- Frontmatter list + scalar link stripping
- Body wiki-link stripping with a synthetic garbage-rich payload
- Callout-title flagging (advisory; titles are NOT stripped)
- File I/O round-trip via ``process_file``
- Strict-mode raises on first rejection
- CLI entry point: dry-run, exit codes, output paths, strict exit code

Run with:
    pytest tests/test_s2_validate.py -v
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from stages.s2_validate import (
    EXTRACTED_GLOB,
    FRONTMATTER_LINK_LIST_KEYS,
    FRONTMATTER_LINK_SCALAR_KEYS,
    FileReport,
    Flag,
    GarbageLinkError,
    Removal,
    aggregate_reports,
    derive_output_paths,
    discover_inputs,
    extract_target,
    main,
    process_file,
    validate_extracted,
)


# ═════════════════════════════════════════════════════════════════════════
# extract_target
# ═════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("raw,expected", [
    ("[[Self-Determination-Theory]]",                         "Self-Determination-Theory"),
    ("[[Zimmerman-SRL-Model|Zimmerman's SRL Model]]",         "Zimmerman-SRL-Model"),
    ("  [[Foo|Bar]]  ",                                       "Foo"),
    ("[[ Padded-Target | display ]]",                         "Padded-Target"),
    ("plain text, no link",                                   None),
    ("",                                                      None),
])
def test_extract_target(raw: str, expected: str | None) -> None:
    assert extract_target(raw) == expected


def test_extract_target_non_string_returns_none() -> None:
    assert extract_target(None) is None  # type: ignore[arg-type]
    assert extract_target(42) is None    # type: ignore[arg-type]


# ═════════════════════════════════════════════════════════════════════════
# Synthetic garbage-rich payload — exhaustive validation
# ═════════════════════════════════════════════════════════════════════════

@pytest.fixture
def garbage_payload() -> dict[str, Any]:
    """A minimal _extracted.json-shaped payload with mixed valid / garbage links."""
    return {
        "extraction_metadata": {"source_file": "synthetic.md"},
        "document_metadata": {
            "frontmatter": {
                "title": "Synthetic Test Doc",
                "builds_on": [
                    "[[Self-Determination-Theory]]",          # valid
                    "[[<% tp.file.title %>]]",                # templater
                    "[[Zimmerman-SRL-Model|Zimmerman]]",      # valid w/ display
                    "[[**bold**]]",                           # formatting-only
                ],
                "related": [
                    "[[priority: high]]",                     # yaml-fragment
                    "[[Autonomous-Motivation]]",              # valid
                    "[[2024]]",                               # pure-numeric
                    "[[srl-foundational-report-2026-04-20]]", # report-filename
                ],
                "link_up": "[[Integrated-Learning-System]]",  # valid scalar
                "parent": "[[<% placeholder %>]]",            # garbage scalar
            },
        },
        "extracted_items": {
            "wiki_links": [
                {"target": "Self-Determination-Theory", "display_text": None},  # valid
                {"target": "<% tp.date.now() %>",       "display_text": None},  # templater
                {"target": "Self-Regulated-Learning",   "display_text": "SRL"}, # valid
                {"target": "***",                       "display_text": None},  # formatting
                {"target": "Forethought-Phase",         "display_text": None},  # valid
                {"target": "tags: foo bar",             "display_text": None},  # yaml-fragment
            ],
            "callouts": [
                {"type": "definition", "title": "Self-Determination Theory"},   # valid
                {"type": "warning",    "title": "<% tp.file.title %>"},         # templater → flag
                {"type": "example",    "title": "This is a sentence."},         # sentence-shaped → NOT flagged (display content)
                {"type": "note",       "title": "priority: high"},              # yaml-fragment → flag
                {"type": "tip",        "title": "Some [Bracketed] Thing"},      # disallowed-chars → flag
            ],
        },
    }


def test_validate_extracted_strips_garbage_from_frontmatter_lists(
    garbage_payload: dict[str, Any],
) -> None:
    cleaned, report = validate_extracted(garbage_payload, "synthetic.md")
    fm = cleaned["document_metadata"]["frontmatter"]
    assert fm["builds_on"] == [
        "[[Self-Determination-Theory]]",
        "[[Zimmerman-SRL-Model|Zimmerman]]",
    ]
    assert fm["related"] == [
        "[[Autonomous-Motivation]]",
    ]


def test_validate_extracted_strips_garbage_from_frontmatter_scalars(
    garbage_payload: dict[str, Any],
) -> None:
    cleaned, _ = validate_extracted(garbage_payload, "synthetic.md")
    fm = cleaned["document_metadata"]["frontmatter"]
    assert fm["link_up"] == "[[Integrated-Learning-System]]"
    # Garbage scalar key dropped entirely.
    assert "parent" not in fm


def test_validate_extracted_strips_body_wiki_links(
    garbage_payload: dict[str, Any],
) -> None:
    cleaned, _ = validate_extracted(garbage_payload, "synthetic.md")
    targets = [w["target"] for w in cleaned["extracted_items"]["wiki_links"]]
    assert targets == [
        "Self-Determination-Theory",
        "Self-Regulated-Learning",
        "Forethought-Phase",
    ]


def test_validate_extracted_does_not_strip_callouts(
    garbage_payload: dict[str, Any],
) -> None:
    cleaned, _ = validate_extracted(garbage_payload, "synthetic.md")
    callouts = cleaned["extracted_items"]["callouts"]
    # All 5 callouts preserved — titles are display content, not link targets.
    assert len(callouts) == 5


def test_validate_extracted_flags_structural_callout_garbage(
    garbage_payload: dict[str, Any],
) -> None:
    _, report = validate_extracted(garbage_payload, "synthetic.md")
    flagged_titles = {f.text for f in report.flagged}
    flagged_reasons = {f.reason for f in report.flagged}
    assert "<% tp.file.title %>" in flagged_titles
    assert "priority: high" in flagged_titles
    assert "Some [Bracketed] Thing" in flagged_titles
    # Sentence-shaped titles are NOT flagged (titles can be sentences).
    assert "This is a sentence." not in flagged_titles
    # Valid concept title NOT flagged.
    assert "Self-Determination Theory" not in flagged_titles
    assert flagged_reasons <= {
        "templater-syntax", "template-placeholder",
        "yaml-fragment-leak", "disallowed-chars", "report-filename",
    }


def test_validate_extracted_records_removal_reasons(
    garbage_payload: dict[str, Any],
) -> None:
    _, report = validate_extracted(garbage_payload, "synthetic.md")
    reasons = {r.reason for r in report.removed}
    # Every reason represented in the synthetic payload should appear.
    assert "templater-syntax" in reasons
    assert "formatting-only" in reasons
    assert "yaml-fragment-leak" in reasons
    assert "pure-numeric" in reasons
    assert "report-filename" in reasons


def test_validate_extracted_records_contexts(
    garbage_payload: dict[str, Any],
) -> None:
    _, report = validate_extracted(garbage_payload, "synthetic.md")
    contexts = {r.context for r in report.removed}
    assert "frontmatter:builds_on" in contexts
    assert "frontmatter:related" in contexts
    assert "frontmatter:parent" in contexts
    assert "body" in contexts


def test_validate_extracted_stats_block(
    garbage_payload: dict[str, Any],
) -> None:
    _, report = validate_extracted(garbage_payload, "synthetic.md")
    stats = report.stats
    assert stats["removed_count"] == len(report.removed)
    assert stats["flagged_count"] == len(report.flagged)
    assert stats["strict_mode"] is False
    assert isinstance(stats["removed_by_reason"], dict)
    assert sum(stats["removed_by_reason"].values()) == stats["removed_count"]
    # total_links_seen >= surviving links
    surviving = len(garbage_payload["extracted_items"]["wiki_links"]) - sum(
        1 for w in garbage_payload["extracted_items"]["wiki_links"]
        if w["target"] in {"<% tp.date.now() %>", "***", "tags: foo bar"}
    )
    assert stats["total_links_seen"] >= surviving


# ═════════════════════════════════════════════════════════════════════════
# Strict mode
# ═════════════════════════════════════════════════════════════════════════

def test_strict_mode_raises_on_first_garbage(
    garbage_payload: dict[str, Any],
) -> None:
    with pytest.raises(GarbageLinkError, match=r"strict-mode rejection"):
        validate_extracted(garbage_payload, "synthetic.md", strict=True)


def test_strict_mode_passes_on_clean_payload() -> None:
    clean = {
        "document_metadata": {
            "frontmatter": {
                "builds_on": ["[[Self-Determination-Theory]]"],
            }
        },
        "extracted_items": {
            "wiki_links": [{"target": "Self-Determination-Theory"}],
            "callouts": [{"type": "definition", "title": "Self-Determination Theory"}],
        },
    }
    cleaned, report = validate_extracted(clean, "clean.md", strict=True)
    assert report.removed == []
    assert cleaned["extracted_items"]["wiki_links"] == [
        {"target": "Self-Determination-Theory"}
    ]


# ═════════════════════════════════════════════════════════════════════════
# Real fixture — sanity check against the actual extractor output
# ═════════════════════════════════════════════════════════════════════════

def test_validate_real_sample_fixture(sample_extracted_json: dict[str, Any]) -> None:
    """The canonical real sample should validate without raising and preserve
    the bulk of its links (it's a real, reasonably clean report)."""
    cleaned, report = validate_extracted(sample_extracted_json, "sample.md")
    assert "extracted_items" in cleaned
    assert "document_metadata" in cleaned
    # Real reports have many links; removal rate should be modest.
    stats = report.stats
    assert stats["total_links_seen"] > 0
    if stats["total_links_seen"] >= 10:
        # No realistic sane report loses >50% of its links to validation.
        assert stats["removed_count"] / stats["total_links_seen"] < 0.5


# ═════════════════════════════════════════════════════════════════════════
# I/O layer
# ═════════════════════════════════════════════════════════════════════════

def test_derive_output_paths_strips_extracted_suffix(tmp_path: Path) -> None:
    src = tmp_path / "myreport_extracted.json"
    src.touch()
    validated, report = derive_output_paths(src, output_dir=None)
    assert validated.name == "myreport_validated.json"
    assert report.name == "myreport_validation-report.json"
    assert validated.parent == tmp_path


def test_derive_output_paths_with_output_dir(tmp_path: Path) -> None:
    src = tmp_path / "in" / "myreport_extracted.json"
    src.parent.mkdir()
    src.touch()
    out = tmp_path / "out"
    validated, report = derive_output_paths(src, output_dir=out)
    assert validated == out / "myreport_validated.json"
    assert report == out / "myreport_validation-report.json"


def test_derive_output_paths_handles_non_extracted_suffix(tmp_path: Path) -> None:
    src = tmp_path / "weird_name.json"
    src.touch()
    validated, _ = derive_output_paths(src, output_dir=None)
    assert validated.name == "weird_name_validated.json"


def test_discover_inputs_single_file(tmp_path: Path) -> None:
    src = tmp_path / "x_extracted.json"
    src.write_text("{}", encoding="utf-8")
    assert discover_inputs(src) == [src]


def test_discover_inputs_directory_globs(tmp_path: Path) -> None:
    (tmp_path / "a_extracted.json").write_text("{}", encoding="utf-8")
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "b_extracted.json").write_text("{}", encoding="utf-8")
    (tmp_path / "ignore_me.json").write_text("{}", encoding="utf-8")
    found = discover_inputs(tmp_path)
    names = sorted(p.name for p in found)
    assert names == ["a_extracted.json", "b_extracted.json"]


def test_discover_inputs_missing_path_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        discover_inputs(tmp_path / "does-not-exist")


def test_process_file_writes_outputs(
    tmp_path: Path, garbage_payload: dict[str, Any],
) -> None:
    src = tmp_path / "demo_extracted.json"
    src.write_text(json.dumps(garbage_payload), encoding="utf-8")
    report = process_file(src, output_dir=None, strict=False, dry_run=False)
    validated_path = tmp_path / "demo_validated.json"
    report_path = tmp_path / "demo_validation-report.json"
    assert validated_path.exists()
    assert report_path.exists()
    # Validated JSON parses and has links stripped.
    cleaned = json.loads(validated_path.read_text(encoding="utf-8"))
    targets = [w["target"] for w in cleaned["extracted_items"]["wiki_links"]]
    assert "<% tp.date.now() %>" not in targets
    # Report JSON has expected shape.
    rep = json.loads(report_path.read_text(encoding="utf-8"))
    assert rep["source_file"].endswith("demo_extracted.json")
    assert rep["stats"]["removed_count"] == report.stats["removed_count"]
    assert rep["stats"]["removed_count"] > 0


def test_process_file_dry_run_writes_nothing(
    tmp_path: Path, garbage_payload: dict[str, Any],
) -> None:
    src = tmp_path / "demo_extracted.json"
    src.write_text(json.dumps(garbage_payload), encoding="utf-8")
    report = process_file(src, output_dir=None, strict=False, dry_run=True)
    assert not (tmp_path / "demo_validated.json").exists()
    assert not (tmp_path / "demo_validation-report.json").exists()
    assert report.stats["removed_count"] > 0


# ═════════════════════════════════════════════════════════════════════════
# Aggregate reports
# ═════════════════════════════════════════════════════════════════════════

def test_aggregate_reports_sums_correctly() -> None:
    r1 = FileReport(source_file="a.json")
    r1.removed = [Removal("x", "templater-syntax", "body")]
    r1.stats = {
        "total_links_seen": 10, "removed_count": 1, "flagged_count": 0,
        "removed_by_reason": {"templater-syntax": 1}, "flagged_by_reason": {},
        "strict_mode": False,
    }
    r2 = FileReport(source_file="b.json")
    r2.removed = [
        Removal("y", "templater-syntax", "body"),
        Removal("z", "pure-numeric", "frontmatter:related"),
    ]
    r2.stats = {
        "total_links_seen": 20, "removed_count": 2, "flagged_count": 1,
        "removed_by_reason": {"templater-syntax": 1, "pure-numeric": 1},
        "flagged_by_reason": {"yaml-fragment-leak": 1},
        "strict_mode": False,
    }
    summary = aggregate_reports([r1, r2])
    assert summary["files_processed"] == 2
    assert summary["total_removed"] == 3
    assert summary["total_flagged"] == 1
    assert summary["total_links_seen"] == 30
    assert summary["removal_rate"] == pytest.approx(3 / 30)
    assert summary["removed_by_reason"]["templater-syntax"] == 2
    assert summary["removed_by_reason"]["pure-numeric"] == 1


# ═════════════════════════════════════════════════════════════════════════
# CLI
# ═════════════════════════════════════════════════════════════════════════

def test_cli_help_lists_strict_links_flag(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(SystemExit) as excinfo:
        main(["--help"])
    assert excinfo.value.code == 0
    out = capsys.readouterr().out
    assert "--strict-links" in out
    assert "--dry-run" in out


def test_cli_missing_input_returns_2(tmp_path: Path) -> None:
    rc = main([str(tmp_path / "nope")])
    assert rc == 2


def test_cli_dry_run_returns_0_and_writes_nothing(
    tmp_path: Path, garbage_payload: dict[str, Any],
) -> None:
    src = tmp_path / "demo_extracted.json"
    src.write_text(json.dumps(garbage_payload), encoding="utf-8")
    rc = main([str(src), "--dry-run"])
    assert rc == 0
    assert not (tmp_path / "demo_validated.json").exists()


def test_cli_writes_outputs(
    tmp_path: Path, garbage_payload: dict[str, Any],
) -> None:
    src = tmp_path / "demo_extracted.json"
    src.write_text(json.dumps(garbage_payload), encoding="utf-8")
    out = tmp_path / "out"
    rc = main([str(src), "-o", str(out)])
    assert rc == 0
    assert (out / "demo_validated.json").exists()
    assert (out / "demo_validation-report.json").exists()


def test_cli_strict_mode_returns_5_on_garbage(
    tmp_path: Path, garbage_payload: dict[str, Any],
) -> None:
    src = tmp_path / "demo_extracted.json"
    src.write_text(json.dumps(garbage_payload), encoding="utf-8")
    rc = main([str(src), "--strict-links"])
    assert rc == 5


def test_cli_strict_mode_returns_0_on_clean_payload(tmp_path: Path) -> None:
    src = tmp_path / "clean_extracted.json"
    src.write_text(json.dumps({
        "document_metadata": {
            "frontmatter": {"builds_on": ["[[Self-Determination-Theory]]"]}
        },
        "extracted_items": {
            "wiki_links": [{"target": "Self-Determination-Theory"}],
            "callouts": [],
        },
    }), encoding="utf-8")
    rc = main([str(src), "--strict-links"])
    assert rc == 0


def test_cli_empty_directory_returns_0(tmp_path: Path) -> None:
    rc = main([str(tmp_path)])
    assert rc == 0


# ═════════════════════════════════════════════════════════════════════════
# Constants exported
# ═════════════════════════════════════════════════════════════════════════

def test_constants_exposed() -> None:
    assert EXTRACTED_GLOB == "*_extracted.json"
    assert "builds_on" in FRONTMATTER_LINK_LIST_KEYS
    assert "related" in FRONTMATTER_LINK_LIST_KEYS
    assert "link_up" in FRONTMATTER_LINK_SCALAR_KEYS


def test_dataclass_to_dict_round_trip() -> None:
    r = Removal("Foo", "templater-syntax", "body")
    assert r.to_dict() == {"target": "Foo", "reason": "templater-syntax", "context": "body"}
    f = Flag("X", "yaml-fragment-leak", "callout-title")
    assert f.to_dict() == {"text": "X", "reason": "yaml-fragment-leak", "context": "callout-title"}
