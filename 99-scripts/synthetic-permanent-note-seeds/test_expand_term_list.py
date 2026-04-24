#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for expand_term_list.

Run with:
    python -m pytest test_expand_term_list.py -v
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from textwrap import dedent

import pytest

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

import expand_term_list as etl  # noqa: E402


# ────────────────────────────────────────────────────────────────────────
# Fixtures
# ────────────────────────────────────────────────────────────────────────


def _write(p: Path, text: str) -> Path:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(dedent(text).lstrip("\n"), encoding="utf-8")
    return p


@pytest.fixture
def minimal_list_text() -> str:
    return """
    ---
    batch_name: test-batch
    batch_date: 2026-04-24
    default_domain: cognitive-science
    default_confidence: high
    notes: |
      smoke test
    ---

    ## Testing Effect

    - aliases: [retrieval-practice effect]
    - related: [spaced repetition, generation effect]
    - confidence: high

    **definition**: The Testing Effect is the empirical finding that retrieving information from memory strengthens long-term retention more than restudy.

    **key_claim**: The Testing Effect demonstrates that retrieval is itself a memory-modifying event.

    **warning**: The Testing Effect refers to low-stakes self-testing, not high-stakes evaluation.

    ## Generation Effect

    **definition**: The Generation Effect is the finding that information a learner produces is remembered better than equivalent information that is read.
    """


@pytest.fixture
def list_path(tmp_path: Path, minimal_list_text: str) -> Path:
    return _write(tmp_path / "list.md", minimal_list_text)


@pytest.fixture
def empty_perm_dir(tmp_path: Path) -> Path:
    d = tmp_path / "perm-notes"
    d.mkdir()
    return d


# ────────────────────────────────────────────────────────────────────────
# Parser — happy path
# ────────────────────────────────────────────────────────────────────────


def test_parse_term_list_happy_path(list_path: Path) -> None:
    batch = etl.parse_term_list(list_path)
    assert batch.batch_name == "test-batch"
    assert batch.batch_date == "2026-04-24"
    assert batch.default_domain == "cognitive-science"
    assert batch.default_confidence == "high"
    assert len(batch.terms) == 2

    t1 = batch.terms[0]
    assert t1.term == "Testing Effect"
    assert t1.domain == "cognitive-science"  # inherited from default
    assert t1.confidence == "high"
    assert "retrieval-practice effect" in t1.aliases
    assert "spaced repetition" in t1.related
    assert t1.definition.startswith("The Testing Effect is")
    assert t1.key_claim.startswith("The Testing Effect demonstrates")
    assert t1.warning.startswith("The Testing Effect refers")

    t2 = batch.terms[1]
    assert t2.term == "Generation Effect"
    assert t2.confidence == "high"  # inherited
    assert t2.key_claim == ""
    assert t2.warning == ""


# ────────────────────────────────────────────────────────────────────────
# Parser — error paths
# ────────────────────────────────────────────────────────────────────────


def test_parse_missing_frontmatter(tmp_path: Path) -> None:
    p = _write(tmp_path / "bad.md", "## Foo\n**definition**: x.\n")
    with pytest.raises(etl.TermListParseError, match="frontmatter"):
        etl.parse_term_list(p)


def test_parse_missing_definition(tmp_path: Path) -> None:
    p = _write(tmp_path / "bad.md", """
        ---
        batch_name: x
        batch_date: 2026-04-24
        default_domain: foo
        ---

        ## Some Term

        - aliases: [a]
    """)
    with pytest.raises(etl.TermListParseError, match="definition"):
        etl.parse_term_list(p)


def test_parse_missing_domain(tmp_path: Path) -> None:
    p = _write(tmp_path / "bad.md", """
        ---
        batch_name: x
        batch_date: 2026-04-24
        ---

        ## Some Term

        **definition**: Some Term is a thing.
    """)
    with pytest.raises(etl.TermListParseError, match="domain"):
        etl.parse_term_list(p)


def test_parse_invalid_batch_name(tmp_path: Path) -> None:
    p = _write(tmp_path / "bad.md", """
        ---
        batch_name: NotKebab
        batch_date: 2026-04-24
        default_domain: foo
        ---

        ## Term

        **definition**: Term is a thing.
    """)
    with pytest.raises(etl.TermListParseError, match="kebab-case"):
        etl.parse_term_list(p)


def test_parse_duplicate_term(tmp_path: Path) -> None:
    p = _write(tmp_path / "bad.md", """
        ---
        batch_name: x
        batch_date: 2026-04-24
        default_domain: foo
        ---

        ## Same Term

        **definition**: Same Term means thing.

        ## same term

        **definition**: same term again.
    """)
    with pytest.raises(etl.TermListParseError, match="duplicate"):
        etl.parse_term_list(p)


def test_parse_no_sections(tmp_path: Path) -> None:
    p = _write(tmp_path / "bad.md", """
        ---
        batch_name: x
        batch_date: 2026-04-24
        default_domain: foo
        ---

        Just prose, no H2 headings.
    """)
    with pytest.raises(etl.TermListParseError, match="no H2"):
        etl.parse_term_list(p)


def test_parse_missing_file() -> None:
    with pytest.raises(FileNotFoundError):
        etl.parse_term_list(Path("does-not-exist-anywhere.md"))


# ────────────────────────────────────────────────────────────────────────
# Inline list parser
# ────────────────────────────────────────────────────────────────────────


@pytest.mark.parametrize("raw,expected", [
    ("[a, b, c]", ["a", "b", "c"]),
    ("a, b, c", ["a", "b", "c"]),
    ("[]", []),
    ("", []),
    ("[[Wiki Link]], plain", ["Wiki Link", "plain"]),
])
def test_parse_inline_list(raw: str, expected: list[str]) -> None:
    assert etl._parse_inline_list(raw) == expected


# ────────────────────────────────────────────────────────────────────────
# Dedup gate
# ────────────────────────────────────────────────────────────────────────


def test_dedup_accepts_when_no_existing_note(
    list_path: Path, empty_perm_dir: Path,
) -> None:
    batch = etl.parse_term_list(list_path)
    decisions = etl.evaluate_dedup(
        batch.terms, permanent_notes_dir=empty_perm_dir,
    )
    assert all(d.decision == "accept" for d in decisions)


def test_dedup_skips_when_note_exists(
    list_path: Path, empty_perm_dir: Path,
) -> None:
    (empty_perm_dir / "testing-effect.md").write_text("# placeholder", encoding="utf-8")
    batch = etl.parse_term_list(list_path)
    decisions = etl.evaluate_dedup(
        batch.terms, permanent_notes_dir=empty_perm_dir,
    )
    by_term = {d.term: d for d in decisions}
    assert by_term["Testing Effect"].decision == "skip"
    assert by_term["Generation Effect"].decision == "accept"


def test_dedup_overwrite_flag_accepts_existing(
    list_path: Path, empty_perm_dir: Path,
) -> None:
    (empty_perm_dir / "testing-effect.md").write_text("x", encoding="utf-8")
    batch = etl.parse_term_list(list_path)
    decisions = etl.evaluate_dedup(
        batch.terms,
        permanent_notes_dir=empty_perm_dir,
        overwrite_existing=True,
    )
    assert all(d.decision == "accept" for d in decisions)


def test_dedup_raises_when_perm_dir_missing(
    list_path: Path, tmp_path: Path,
) -> None:
    batch = etl.parse_term_list(list_path)
    with pytest.raises(etl.DedupGateError):
        etl.evaluate_dedup(
            batch.terms, permanent_notes_dir=tmp_path / "nope",
        )


# ────────────────────────────────────────────────────────────────────────
# Brief construction
# ────────────────────────────────────────────────────────────────────────


def test_brief_has_definition_callout_with_term_in_title(
    list_path: Path,
) -> None:
    batch = etl.parse_term_list(list_path)
    brief = etl._term_to_brief_dict(batch.terms[0])
    assert brief["concept"] == "Testing Effect"
    assert brief["domain"] == "cognitive-science"
    types = [c["type"] for c in brief["callouts"]]
    assert "definition" in types
    # Substring rule: definition title must contain the term name
    def_callout = next(c for c in brief["callouts"] if c["type"] == "definition")
    assert "Testing Effect" in def_callout["title"]


def test_brief_omits_optional_callouts_when_blank(list_path: Path) -> None:
    batch = etl.parse_term_list(list_path)
    # Generation Effect has no key_claim or warning
    brief = etl._term_to_brief_dict(batch.terms[1])
    types = [c["type"] for c in brief["callouts"]]
    assert types == ["definition"]


def test_brief_omits_empty_link_slots(list_path: Path) -> None:
    batch = etl.parse_term_list(list_path)
    brief = etl._term_to_brief_dict(batch.terms[1])  # Generation Effect: no links set
    for slot in ("aliases", "broader", "narrower", "related", "prerequisites"):
        assert slot not in brief


def test_write_brief_creates_yaml(list_path: Path, tmp_path: Path) -> None:
    batch = etl.parse_term_list(list_path)
    out = etl.write_brief(
        batch.terms[0], briefs_dir=tmp_path / "briefs", overwrite=False,
    )
    assert out.exists()
    assert out.name == "testing-effect.yaml"
    content = out.read_text(encoding="utf-8")
    assert "concept: Testing Effect" in content


def test_write_brief_refuses_overwrite(list_path: Path, tmp_path: Path) -> None:
    batch = etl.parse_term_list(list_path)
    etl.write_brief(batch.terms[0], briefs_dir=tmp_path / "b", overwrite=False)
    with pytest.raises(FileExistsError):
        etl.write_brief(batch.terms[0], briefs_dir=tmp_path / "b", overwrite=False)


# ────────────────────────────────────────────────────────────────────────
# CLI integration — expand
# ────────────────────────────────────────────────────────────────────────


def test_cli_expand_dry_run_writes_nothing(
    list_path: Path, empty_perm_dir: Path, tmp_path: Path,
) -> None:
    briefs = tmp_path / "briefs"
    seeds = tmp_path / "seeds"
    rc = etl.main([
        "-q", "expand", str(list_path),
        "--briefs-dir", str(briefs),
        "--seeds-dir", str(seeds),
        "--permanent-notes-dir", str(empty_perm_dir),
        "--dry-run",
    ])
    assert rc == 0
    assert not briefs.exists()


def test_cli_expand_writes_briefs_and_manifest(
    list_path: Path, empty_perm_dir: Path, tmp_path: Path,
) -> None:
    briefs = tmp_path / "briefs"
    seeds = tmp_path / "seeds"
    rc = etl.main([
        "-q", "expand", str(list_path),
        "--briefs-dir", str(briefs),
        "--seeds-dir", str(seeds),
        "--permanent-notes-dir", str(empty_perm_dir),
    ])
    assert rc == 0
    batch_briefs_dir = briefs / "test-batch"
    assert (batch_briefs_dir / "testing-effect.yaml").exists()
    assert (batch_briefs_dir / "generation-effect.yaml").exists()
    manifest_path = batch_briefs_dir / "manifest.json"
    assert manifest_path.exists()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["counts"]["accepted"] == 2
    assert manifest["counts"]["skipped"] == 0
    assert len(manifest["entries"]) == 2
    # warnings should fire because Generation Effect lacks key_claim/warning
    assert manifest["counts"]["warnings"] >= 2


def test_cli_expand_skips_existing(
    list_path: Path, empty_perm_dir: Path, tmp_path: Path,
) -> None:
    (empty_perm_dir / "testing-effect.md").write_text("x", encoding="utf-8")
    briefs = tmp_path / "briefs"
    rc = etl.main([
        "-q", "expand", str(list_path),
        "--briefs-dir", str(briefs),
        "--seeds-dir", str(tmp_path / "seeds"),
        "--permanent-notes-dir", str(empty_perm_dir),
    ])
    assert rc == 0
    batch_briefs_dir = briefs / "test-batch"
    assert not (batch_briefs_dir / "testing-effect.yaml").exists()
    assert (batch_briefs_dir / "generation-effect.yaml").exists()
    manifest = json.loads(
        (batch_briefs_dir / "manifest.json").read_text(encoding="utf-8")
    )
    assert manifest["counts"]["accepted"] == 1
    assert manifest["counts"]["skipped"] == 1


def test_cli_expand_missing_file_returns_2(tmp_path: Path) -> None:
    rc = etl.main([
        "-q", "expand", str(tmp_path / "nope.md"),
        "--permanent-notes-dir", str(tmp_path),
    ])
    assert rc == 2


def test_cli_expand_malformed_returns_4(
    tmp_path: Path, empty_perm_dir: Path,
) -> None:
    bad = _write(tmp_path / "bad.md", "no frontmatter here\n")
    rc = etl.main([
        "-q", "expand", str(bad),
        "--permanent-notes-dir", str(empty_perm_dir),
    ])
    assert rc == 4


# ────────────────────────────────────────────────────────────────────────
# CLI integration — run (expand + build-batch)
# ────────────────────────────────────────────────────────────────────────


def test_cli_run_full_pipeline_produces_seeds(
    list_path: Path, empty_perm_dir: Path, tmp_path: Path,
) -> None:
    briefs = tmp_path / "briefs"
    seeds = tmp_path / "seeds"
    rc = etl.main([
        "-q", "run", str(list_path),
        "--briefs-dir", str(briefs),
        "--seeds-dir", str(seeds),
        "--permanent-notes-dir", str(empty_perm_dir),
    ])
    assert rc == 0
    seed_dir = seeds / "2026-04-24-test-batch"
    seed_files = sorted(seed_dir.glob("*_extracted.json"))
    assert len(seed_files) == 2
    names = [f.name for f in seed_files]
    assert any("testing-effect-synthetic-seed-2026-04-24" in n for n in names)
    assert any("generation-effect-synthetic-seed-2026-04-24" in n for n in names)
    # spot-check one seed has the canonical V4 schema keys
    sample = json.loads(seed_files[0].read_text(encoding="utf-8"))
    for key in ("extraction_metadata", "document_metadata",
                "extracted_items", "knowledge_graph"):
        assert key in sample


# ────────────────────────────────────────────────────────────────────────
# CLI integration — build-batch
# ────────────────────────────────────────────────────────────────────────


def test_cli_build_batch_missing_manifest_returns_5(tmp_path: Path) -> None:
    rc = etl.main([
        "-q", "build-batch", str(tmp_path / "nope.json"),
    ])
    assert rc == 5


def test_cli_build_batch_malformed_manifest_returns_5(tmp_path: Path) -> None:
    bad = tmp_path / "manifest.json"
    bad.write_text("{not json", encoding="utf-8")
    rc = etl.main(["-q", "build-batch", str(bad)])
    assert rc == 5


# ────────────────────────────────────────────────────────────────────────
# CLI surface
# ────────────────────────────────────────────────────────────────────────


def test_cli_help(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(SystemExit) as exc:
        etl.main(["--help"])
    assert exc.value.code == 0
    out = capsys.readouterr().out
    assert "expand" in out
    assert "build-batch" in out
    assert "run" in out


def test_cli_version(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(SystemExit) as exc:
        etl.main(["--version"])
    assert exc.value.code == 0
    out = capsys.readouterr().out
    assert etl.__version__ in out
