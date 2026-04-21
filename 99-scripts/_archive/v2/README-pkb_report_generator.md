# `pkb_report_generator.py`

Generate a comprehensive Markdown analysis report for a single file or a folder of Obsidian Markdown files.

> [!abstract] What it does
> Walks the input path, parses YAML frontmatter, wiki-links, tags, callouts, embeds, headings, and code blocks, then emits a richly-formatted report containing statistics, link-graph analysis, frontmatter audit, activity timeline, ASCII + matplotlib charts, duplicate detection, rule-based recommendations, and auto-injected wiki-links to the vault's permanent-note folders.

- **Script:** [pkb_report_generator.py](pkb_report_generator.py)
- **Tests:** [test_pkb_report_generator.py](test_pkb_report_generator.py) (27/27 passing)
- **Version:** 1.0.0
- **Python:** 3.10+

---

## Installation

The script is **stdlib-only by default** — no install required. Optional dependencies enable richer features:

```bash
pip install rich matplotlib pyyaml
```

| Dependency | Enables | Fallback if missing |
|---|---|---|
| `rich` | Live progress bar during analysis | Plain `print` status |
| `matplotlib` | PNG charts (`--charts`) | ASCII charts only; `--charts` warns and skips |
| `pyyaml` | Robust YAML frontmatter parsing | Regex-based parser |

---

## Quick Start

```bash
# Analyse a folder, write report next to it
python 99-scripts/pkb_report_generator.py 03-notes

# Recurse into subfolders + PNG charts
python 99-scripts/pkb_report_generator.py 04-library --recursive --charts

# Single file
python 99-scripts/pkb_report_generator.py README.md

# Preview without writing
python 99-scripts/pkb_report_generator.py 00-inbox --recursive --dry-run -v
```

Default output: `<input-folder>/_REPORT-YYYY-MM-DD.md`

---

## CLI Reference

```
pkb_report_generator.py [OPTIONS] INPUT
```

### Positional

| Argument | Description |
|---|---|
| `INPUT` | File or folder to analyse (required) |

### Options

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| `--output` | `-o` | path | `<input>/_REPORT-YYYY-MM-DD.md` | Report output path |
| `--recursive` | `-r` | flag | off | Recurse into subdirectories (folder input only) |
| `--charts` | | flag | off | Generate PNG charts via matplotlib |
| `--vault` | | path | auto | Vault root for resolving permanent-note links |
| `--top` | | int | `20` | Top-N depth for ranked tables |
| `--workers` | | int | `8` | Thread-pool size for parallel file reads |
| `--exclude` | | str | `""` | Comma-separated extra folder names to skip |
| `--dry-run` | `-n` | flag | off | Analyse and print summary; write nothing |
| `--verbose` | `-v` | count | `0` | Increase logging (`-v` info, `-vv` debug) |
| `--quiet` | `-q` | flag | off | Suppress non-error output |
| `--no-progress` | | flag | off | Disable progress bar even if `rich` installed |
| `--version` | | flag | | Print version and exit |
| `--help` | `-h` | flag | | Show help and exit |

### Vault auto-detection

If `--vault` is omitted, the script walks up parents from `INPUT` looking for a folder containing `.obsidian/` or `00-meta/`. Found root is used to resolve wiki-links to:

- `999-report-organizing/_permanent-notes/_permanent-notes/`
- `999-report-organizing/_extractor-output/`

Override with `--vault PATH` if needed.

### Default exclusions (recursive scans)

`.git`, `.obsidian`, `.trash`, `node_modules`, `__pycache__`, `.venv`, `venv`, `.idea`, `.vscode`

Add more with `--exclude "folder1,folder2"`.

---

## Usage Examples

### Common workflows

```bash
# 1. Daily-notes folder, recursive, top-30 lists
python 99-scripts/pkb_report_generator.py 01_daily-notes -r --top 30

# 2. Generate PNG charts in a sibling folder
python 99-scripts/pkb_report_generator.py 04-library -r --charts -o reports/library.md

# 3. Single file deep-dive
python 99-scripts/pkb_report_generator.py 03-notes/some-note.md

# 4. Inbox triage preview (no files written)
python 99-scripts/pkb_report_generator.py 00-inbox -r --dry-run -vv

# 5. Skip auto-generated folders
python 99-scripts/pkb_report_generator.py 99-archive -r --exclude "raw-exports,backup"

# 6. Quiet mode for cron/CI
python 99-scripts/pkb_report_generator.py 03-notes -r -q -o /tmp/notes.md

# 7. Custom vault root
python 99-scripts/pkb_report_generator.py /external/notes --vault /external/notes
```

### Activate the venv first (Windows / git-bash)

```bash
source "/d/10_pur3v4d3r's-vault/.venv/Scripts/activate"
python 99-scripts/pkb_report_generator.py 03-notes --recursive --charts
```

---

## Report Sections

The generated Markdown report contains 16 sections, each anchored in the TOC:

| # | Section | Content |
|---|---|---|
| 1 | YAML Frontmatter | Tags, status, certainty, generated-at, input path |
| 2 | Table of Contents | Anchored links to every section |
| 3 | Executive Summary | Files, words, links, tags at a glance |
| 4 | Insights | Auto-generated narrative bullets |
| 5 | Recommendations | Rule-based, severity-sorted callouts |
| 6 | File Statistics | Word/line/char/size totals + means + medians |
| 7 | Top Words | Frequency table + ASCII bar chart (stopwords filtered) |
| 8 | Tag Analysis | Frequency, top-N table, ASCII bars |
| 9 | Wiki-Link Graph | Most-linked targets, hubs, **orphans**, **broken links** |
| 10 | Frontmatter Audit | Coverage %, field-coverage table, status distribution |
| 11 | Activity Timeline | Per-month modification histogram (vertical ASCII) |
| 12 | Duplicates | SHA-256 of normalised content |
| 13 | Callouts & Embeds | Counts and types |
| 14 | Charts | PNG references (if `--charts` used) |
| 15 | File Index | Full inventory table with source links + `[[wiki-links]]` |
| 16 | Related Resources | Auto-injected wiki-links to permanent-note folders |

---

## Recommendations Engine

7 heuristic rules generate severity-sorted callouts:

| Severity | Rule |
|---|---|
| 🔴 critical | Broken wiki-links detected |
| 🔴 critical | Duplicate files (identical content) |
| 🟡 warning | Frontmatter coverage < 80% |
| 🟡 warning | Notes with no tags > 30% |
| 🟡 warning | Orphan notes (no inbound or outbound links) |
| 🔵 info | Stub notes (< 50 words) |
| 🔵 info | Long notes (> 1000 words) with no headings |

---

## Exit Codes

| Code | Meaning |
|---|---|
| `0` | Success |
| `1` | Uncaught error (logged with traceback) |
| `2` | Input path not found / not readable |
| `3` | No analysable files found |
| `4` | Invalid arguments |
| `130` | Interrupted (Ctrl+C) |

---

## Output Layout

```
<input-folder>/
├── _REPORT-2026-04-21.md          # Main report
└── _REPORT-2026-04-21_charts/     # Only if --charts
    ├── top-tags.png
    ├── timeline.png
    ├── word-distribution.png
    └── link-hubs.png
```

Override main path with `-o PATH`. Charts always go in `<report-stem>_charts/` next to the report.

---

## Testing

```bash
# Run full test suite
python -m pytest 99-scripts/test_pkb_report_generator.py -v

# Single test
python -m pytest 99-scripts/test_pkb_report_generator.py::test_link_graph_detects_orphans -v

# With coverage
python -m pytest 99-scripts/test_pkb_report_generator.py --cov=pkb_report_generator --cov-report=term-missing
```

Coverage: 27 tests across analyzers, aggregators, CLI, edge cases, and error paths.

---

## Architecture

Three-stage pipeline:

```
discover_files()  →  analyze_files_parallel()  →  render_report()
   (I/O)              (ThreadPoolExecutor)         (pure)
```

- **Pure analyzers** (`parse_frontmatter`, `analyze_text`, `link_graph`, etc.) — unit-testable in isolation, no I/O
- **I/O layer** — file reads, output writes
- **CLI layer** — argparse + logging + exception → exit-code mapping
- **Optional integrations** — `rich`, `matplotlib`, `yaml` all behind `_HAS_*` flags

Single file, ~900 lines, no required third-party dependencies.

---

## Integration

### As a library

```python
from pathlib import Path
import sys
sys.path.insert(0, "99-scripts")
import pkb_report_generator as prg

files = prg.discover_files(Path("03-notes"), recursive=True)
analyses = prg.analyze_files_parallel(files, workers=8, show_progress=False)
report_md = prg.render_report(
    analyses=analyses,
    input_path=Path("03-notes"),
    vault_root=Path("."),
    top_n=20,
    charts_dir=None,
)
Path("report.md").write_text(report_md, encoding="utf-8")
```

### As a scheduled job (Windows Task Scheduler)

```batch
"D:\10_pur3v4d3r's-vault\.venv\Scripts\python.exe" "D:\10_pur3v4d3r's-vault\99-scripts\pkb_report_generator.py" "D:\10_pur3v4d3r's-vault\03-notes" -r -q
```

### As a cron job (Linux/macOS)

```cron
0 6 * * 1  /path/to/.venv/bin/python /path/to/99-scripts/pkb_report_generator.py /path/to/notes -r -q
```

---

## Related Tools

Sibling scripts in [99-scripts/](.):

- `vault_indexer.py` — Build a JSON index of the vault
- `link_check.py` — Find broken wiki-links across the vault
- `meta_audit.py` — Validate YAML frontmatter compliance
- `broken_link_fixer.py` — Auto-fix broken wiki-links
- `generate_frontmatter.py` — Auto-add frontmatter to bare notes
- `folder_review_report.py` — Lightweight folder-level review

---

## Troubleshooting

**Q: `UnicodeEncodeError` on Windows console**
A: The script reconfigures `sys.stdout` to UTF-8 at startup. If you still see issues, run with `-q` or pipe to a file: `... > report.log 2>&1`.

**Q: `--charts` shows "matplotlib not installed"**
A: `pip install matplotlib` in your active environment. ASCII charts always render regardless.

**Q: Report says "0 files analysed"**
A: Check the path exists and contains `.md` files. Use `-v` to see which paths are scanned. Add `-r` for recursive.

**Q: Wiki-links to permanent notes show as broken**
A: Verify the folders exist at `999-report-organizing/_permanent-notes/_permanent-notes/` and `999-report-organizing/_extractor-output/`, or pass `--vault` explicitly.

**Q: Slow on large folders (1000+ files)**
A: Bump `--workers 16` (I/O-bound, threads help). For 10K+ files, consider chunking the input.

---

## License & Version

- **Version:** 1.0.0
- **Generated by:** Python Script Designer & Generator — Expert v1.0.0
- **Status:** evergreen
