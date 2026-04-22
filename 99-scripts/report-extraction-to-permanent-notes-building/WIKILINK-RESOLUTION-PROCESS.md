# Wiki-Link Resolution Process — Complete Technical Reference

> **Purpose:** Step-by-step guide for diagnosing and fixing broken Obsidian wiki-links in auto-generated permanent notes and reports. Written so a future Claude session can replicate the entire process from diagnosis through fix with zero ambiguity.
>
> **Project:** `_pkm-and-pkb-framework-1.0.0`  
> **Date:** 2026-03-18  
> **Status:** Production — verified working

---

## Table of Contents

1. [The Problem](#1-the-problem)
2. [Root Cause Analysis](#2-root-cause-analysis)
3. [The Solution: Pipe Syntax](#3-the-solution-pipe-syntax)
4. [The Fix Script: `rewrite_wikilinks.py`](#4-the-fix-script-rewrite_wikilinks-py)
5. [How the Resolution Index Works](#5-how-the-resolution-index-works)
6. [Execution Procedure](#6-execution-procedure)
7. [Future-Proofing: `_pipe_link()` in Generators](#7-future-proofing-_pipe_link-in-generators)
8. [Known Edge Cases & Gotchas](#8-known-edge-cases--gotchas)
9. [Project Directory Structure](#9-project-directory-structure)
10. [Full Script Listing](#10-full-script-listing)
11. [Starter Prompt for Future Sessions](#11-starter-prompt-for-future-sessions)

---

## 1. The Problem

When auto-generating Obsidian markdown notes from structured report data, wiki-links were written using the human-readable display name:

```markdown
[[Expertise Reversal Effect (Kalyuga, Ayres, Chandler, Sweller, 2003)]]
[[Cognitive Load Theory (CLT)]]
[[zone-of-proximal-development]]
```

**Symptom in Obsidian:** These links appeared in **light red** (unresolved) in reading/preview mode, while single-word links like `[[pedagogy]]` and `[[andragogy]]` appeared in **blue** (resolved) and worked correctly.

**Scale of the problem:**
- 665 permanent notes (398 originals + 267 stubs)
- 31 report files
- ~15,000+ wiki-links total across all files
- The vast majority were broken (light red / unresolved)

---

## 2. Root Cause Analysis

### The Core Issue: Spaces ≠ Hyphens

Obsidian does **NOT** automatically resolve spaces to hyphens in filenames.

| Link in Markdown | Obsidian Looks For | Actual File on Disk | Result |
|---|---|---|---|
| `[[pedagogy]]` | `Pedagogy.md` | `Pedagogy.md` | ✅ Works |
| `[[andragogy]]` | `Andragogy.md` | `Andragogy.md` | ✅ Works |
| `[[Expertise Reversal Effect (Kalyuga, Ayres, Chandler, Sweller, 2003)]]` | `Expertise Reversal Effect.md` | `Expertise-Reversal-Effect-...-Kalyuga,...md` | ❌ Broken |
| `[[Cognitive Load Theory (CLT)]]` | `Cognitive Load Theory.md` | `Cognitive-Load-Theory.md` | ❌ Broken |

**Why single-word links worked:** No spaces = no mismatch. `Pedagogy` matches `Pedagogy.md` exactly.

**Why multi-word links broke:** The filename sanitizer (`sanitize_filename()`) replaces spaces with hyphens, but the wiki-link generation used the raw display name with spaces.

### Why Aliases Didn't Fix It

Every note had YAML aliases like:

```yaml
aliases:
  - "Expertise Reversal Effect"
```

Obsidian's alias resolution is supposed to match `[[Expertise Reversal Effect (Kalyuga, Ayres, Chandler, Sweller, 2003)]]` to a note with that alias. However, in practice this was unreliable — possibly due to:
- The vault being inside a nested project folder (`999-report-organizing/_pkm-and-pkb-framework-1.0.0/`)
- The `_permanent-notes/` directory name starting with underscore
- Obsidian's indexing not triggering on externally-modified files
- Alias resolution being less reliable than direct filename matching

**Conclusion:** Alias-based resolution cannot be relied upon. Direct filename targeting via pipe syntax is the only reliable approach.

---

## 3. The Solution: Pipe Syntax

Obsidian's pipe syntax directly targets the file by its exact filename stem:

```markdown
<!-- BEFORE (broken): Obsidian tries to find a file named "Cognitive Load Theory.md" -->
[[Cognitive Load Theory (CLT)]]

<!-- AFTER (working): Obsidian goes directly to "Cognitive-Load-Theory.md", displays "Cognitive Load Theory" -->
[[Cognitive Load Theory (CLT)|Cognitive Load Theory]]
```

### Anatomy of a Pipe Link

```
[[Cognitive Load Theory (CLT)|Cognitive Load Theory]]
 │                      │
 │                      └── Display text (what the user sees)
 └── Target (must match a filename stem EXACTLY, no .md extension)
```

### Rules

1. **Target** = the filename **without** `.md`, case-insensitive in Obsidian
2. **Display** = the human-readable text shown in reading mode
3. If target == display (single-word, no mismatch), pipe is optional: `[[pedagogy]]` works fine
4. If the filename has hyphens but the display has spaces, you **must** use pipe syntax

---

## 4. The Fix Script: `rewrite_wikilinks.py`

**Location:** `scripts/rewrite_wikilinks.py`

### What It Does

1. **Builds a resolution index** — scans all 665 permanent notes, reads their filename stems and YAML aliases, creates a lookup: `lowercase display name → filename stem`
2. **Finds all wiki-links** — regex `\[\[([^\[\]]+?)\]\]` matches every `[[...]]` in each file
3. **Rewrites where needed** — if a link's display name maps to a different filename stem, rewrites to `[[stem|display]]`
4. **Skips safe links** — already-piped links, exact filename matches, and unresolvable links are left alone

### CLI Interface

```bash
# Dry run (default) — shows all proposed changes, modifies nothing
python scripts/rewrite_wikilinks.py

# Apply changes to permanent notes only
python scripts/rewrite_wikilinks.py --scope notes --execute

# Apply changes to report files only
python scripts/rewrite_wikilinks.py --scope reports --execute

# Apply changes to everything
python scripts/rewrite_wikilinks.py --scope all --execute
```

### Critical Configuration Lines

```python
PROJECT_ROOT = Path(__file__).resolve().parent.parent
NOTES_DIR = PROJECT_ROOT / "_permanent-notes"    # Where the .md notes live
REPORTS_DIR = PROJECT_ROOT / "report-series"      # Where the report .md files live
```

> **⚠️ GOTCHA:** In the original version, `REPORTS_DIR` pointed to `extraction-material/markdown/` (the raw source copies) instead of `report-series/` (the Obsidian-facing files). This was a bug that caused the reports to not get rewritten while the notes were fixed. Always verify `REPORTS_DIR` points to the actual directory Obsidian reads from.

---

## 5. How the Resolution Index Works

The index is the heart of the rewrite process. It maps every possible display name to the correct filename stem.

### Index Construction (`build_resolution_index()`)

```
For each .md file in _permanent-notes/:
  1. Read the filename stem (e.g., "Cognitive-Load-Theory")
  2. Register it: "cognitive-load-theory" → "Cognitive-Load-Theory"
  3. Create space-version: "cognitive load theory" → "Cognitive-Load-Theory"
  4. Parse YAML aliases: ["Cognitive Load Theory", "CLT"]
  5. Register each alias: "cognitive load theory" → "Cognitive-Load-Theory"
                          "clt" → "Cognitive-Load-Theory"
```

### Conflict Resolution

When multiple notes register the same alias:
- **Prefer original notes** (longer, detailed) over **stubs** (short placeholders)
- Among originals, prefer the **longer filename stem** (more specific)
- Stub detection: file has `"stub-note"` in first 500 chars or total length < 600 chars

### Typical Index Size

For 665 notes: ~1,700+ resolvable names indexed (filenames + space versions + aliases)

---

## 6. Execution Procedure

### Step-by-Step (Copy-Paste Ready)

```bash
# 0. Navigate to the project root
cd /path/to/project-root   # e.g., 999-report-organizing/_pkm-and-pkb-framework-1.0.0

# 1. Activate the Python virtual environment
source "/path/to/vault/.venv/Scripts/activate"   # Windows Git Bash
# OR: .venv\Scripts\activate                      # Windows CMD
# OR: source .venv/bin/activate                   # macOS/Linux

# 2. DRY RUN — see what would change (ALWAYS do this first)
python scripts/rewrite_wikilinks.py --scope all

# 3. Review the output. Check:
#    - Number of rewrites looks reasonable
#    - Resolved targets look correct (hyphenated filenames)
#    - No YAML content leaking into pipe targets

# 4. EXECUTE — apply the changes
python scripts/rewrite_wikilinks.py --scope all --execute

# 5. Verify a sample file
grep '\[\[.*|.*\]\]' report-series/10-scaffolding-and-fading-pkm-framework-2026-03-14.md | head -5

# 6. Force Obsidian to reload
#    In Obsidian: Ctrl+P → "Reload app without saving"
#    OR: Close and reopen Obsidian entirely

# 7. Check that previously-broken links (light red) are now resolved (blue)
```

### Verification Commands

```bash
# Count piped vs total wiki-links per report
for f in report-series/*.md; do
  cnt=$(grep -c '\[\[.*|.*\]\]' "$f" 2>/dev/null)
  total=$(grep -c '\[\[' "$f" 2>/dev/null)
  echo "$total total, $cnt piped: $(basename "$f")"
done

# Find any remaining un-piped multi-word links (potential misses)
grep -Pn '\[\[[A-Z][a-z]+ [A-Z]' report-series/*.md | grep -v '|' | head -20

# Validate all pipe targets against actual filenames
python -c "
from pathlib import Path
import re
notes = Path('_permanent-notes')
stems = {f.stem.lower() for f in notes.glob('*.md')}
PIPE_RE = re.compile(r'\[\[([^\]|]+)\|')
broken = []
for f in list(notes.glob('*.md')) + list(Path('report-series').glob('*.md')):
    text = f.read_text(encoding='utf-8', errors='ignore')
    for m in PIPE_RE.finditer(text):
        target = m.group(1).strip()
        if target.lower() not in stems:
            broken.append((f.name, target))
print(f'{len(broken)} broken pipe targets found')
for fname, target in broken[:20]:
    print(f'  {fname}: {target}')
"
```

---

## 7. Future-Proofing: `_pipe_link()` in Generators

To prevent this problem from recurring when generating NEW notes, both `note_builder.py` and `generate_stubs.py` now include a `_pipe_link()` helper:

### In `note_builder.py` (line ~58)

```python
def _pipe_link(display_name: str) -> str:
    """Build pipe-syntax wiki-link: [[Filename-Stem|Display Name]].
    If the display name already matches the filename stem (single words),
    returns a plain link without the pipe.
    """
    stem = sanitize_filename(display_name)
    if stem == display_name:
        return f'[[{display_name}]]'
    return f'[[{stem}|{display_name}]]'
```

This is called at every point where a wiki-link is generated:
- `related_links` lists in frontmatter
- `see_also` lists
- `builds_on` / `enables` lists
- `expansion_topics` in frontmatter
- Connection links in the note body
- Wiki-link cloud in the note body

### In `generate_stubs.py`

Same logic duplicated (since it doesn't import from `note_builder`):
- `see_also` YAML generation
- `backlinks` markdown generation

### The `sanitize_filename()` Function (Source of Truth)

```python
def sanitize_filename(name: str) -> str:
    safe = re.sub(r'[<>:"/\\|?*\[\]()]', '', name)   # Remove unsafe chars
    safe = re.sub(r'[\s_]+', '-', safe)                # Spaces/underscores → hyphens
    safe = re.sub(r'-{2,}', '-', safe)                 # Collapse double hyphens
    safe = safe.strip('-')                              # Trim leading/trailing hyphens
    if len(safe) > MAX_FILENAME_LENGTH:                 # Truncate if needed (80 chars)
        safe = safe[:MAX_FILENAME_LENGTH].rstrip('-')
    return safe
```

**This is the same function used to create filenames**, ensuring the pipe target always matches the actual filename on disk.

---

## 8. Known Edge Cases & Gotchas

### 8.1 — `REPORTS_DIR` Pointing to Wrong Folder

The original script had:
```python
REPORTS_DIR = PROJECT_ROOT / "extraction-material" / "markdown"  # ❌ WRONG — source copies
```
This rewrote the extraction source files, not the Obsidian-facing reports in `report-series/`. The fix:
```python
REPORTS_DIR = PROJECT_ROOT / "report-series"  # ✅ CORRECT — Obsidian reads these
```

**Always verify:** The directories in the script must point to the same files that Obsidian actually loads.

### 8.2 — Obsidian Not Detecting External File Changes

After running the script, Obsidian may not immediately reflect changes. Solutions:
1. **Ctrl+P → "Reload app without saving"** (forces full re-index)
2. **Close Obsidian → wait 5 seconds → reopen** 
3. Obsidian's file watcher sometimes lags on bulk external changes — a reload is the safest approach

### 8.3 — YAML Frontmatter Corruption Risk

The wiki-link regex `\[\[([^\[\]]+?)\]\]` can potentially match across YAML line boundaries inside frontmatter if wiki-links appear in YAML values. Example:

```yaml
expansion_topics:
  - topic: "[[dual-coding-theory]]"
    priority: medium
  - topic: "[[Collaborative Learning]]"
```

If the regex captures across the `\n`, the pipe target could become `Dual Coding Theory"]]\n    priority: medium\n  - topic: "[[Colla` — corrupting the YAML.

**Mitigation:** The current regex uses `[^\[\]]+?` (non-greedy, no brackets), which should prevent this. But if you encounter corrupted YAML, check:
1. Pipe targets containing newlines or YAML syntax
2. Files where `expansion_topics` or `related` YAML sections look malformed

### 8.4 — 38 Known Broken Pipe Targets (As of 2026-03-18)

After the rewrite, 38 out of ~12,000 pipe links had targets not matching any filename:
- **"Straw Man Fallacy"** — target has spaces instead of hyphens (in ~10 files)
- **"Autonomy Need" / "Competence Need" / "Relatedness Need"** — targets with spaces
- **"Chinn and Brewer's Model"** — target with spaces

These are edge cases where the resolution index didn't find a match (no note exists with that exact alias) so the rewrite used the display name as-is. Fix: create stub notes for these concepts or manually add them to the index.

### 8.5 — Windows UTF-8 Console Encoding

The script requires this at the top for Windows compatibility:
```python
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
```
Without this, em-dashes (—), Unicode box-drawing characters, and emojis in filenames cause `cp1252` encoding errors on Windows.

### 8.6 — Filename Truncation

`sanitize_filename()` truncates at 80 characters (`MAX_FILENAME_LENGTH`). This means long concept names produce truncated stems:

```
"Expertise Reversal Effect — Cognitive Psychology Kalyuga, Chandler, Tuovinen & Sweller"
→ "Expertise-Reversal-Effect-—-Cognitive-Psychology-Kalyuga,-Chandler,-Tuovinen-&-S"
```

The pipe link in this case becomes:
```markdown
[[Expertise-Reversal-Effect-—-Cognitive-Psychology-Kalyuga,-Chandler,-Tuovinen-&-S|Expertise Reversal Effect]]
```

This works because the target matches the actual truncated filename on disk.

---

## 9. Project Directory Structure

```
_pkm-and-pkb-framework-1.0.0/
├── _permanent-notes/          # 665 auto-generated Obsidian notes (398 originals + 267 stubs)
│   ├── Pedagogy.md
│   ├── Cognitive-Load-Theory.md
│   ├── Expertise-Reversal-Effect-—-Cognitive-Psychology-Kalyuga,...md
│   └── ... (665 files)
├── report-series/             # 31 Obsidian-facing report files ← WHAT OBSIDIAN READS
│   ├── 01-foundations-of-knowledge-architecture-pkm-framework-2026-03-13.md
│   ├── 10-scaffolding-and-fading-pkm-framework-2026-03-14.md
│   ├── pkm-and-pkb-framework-1.0.0.md  (index/MOC)
│   └── ... (31 files)
├── extraction-material/       # Raw source data (NOT what Obsidian reads)
│   ├── json/                  # Structured JSON extractions
│   └── markdown/              # Markdown copies of reports (source, not target)
├── scripts/
│   ├── config.py              # Shared constants (MAX_FILENAME_LENGTH, etc.)
│   ├── report_parser.py       # Parses JSON extractions into NoteCandidate objects
│   ├── note_builder.py        # Generates permanent notes from NoteCandidate → .md files
│   ├── generate_notes.py      # CLI entry point for note generation
│   ├── generate_stubs.py      # Creates stub notes for concepts referenced but not generated
│   ├── audit_notes.py         # Audits alias coverage, orphan links, missing concepts
│   └── rewrite_wikilinks.py   # POST-HOC FIX: rewrites [[Display]] → [[Stem|Display]]
└── review-of-framework-codebase/  # Code review documents
```

---

## 10. Full Script Listing

The complete `rewrite_wikilinks.py` is at `scripts/rewrite_wikilinks.py` in this project. Key components:

| Function | Purpose |
|---|---|
| `build_resolution_index(notes_dir)` | Scans all notes, builds `lowercase name → stem` mapping |
| `rewrite_wikilinks_in_text(text, index)` | Regex-replaces `[[Display]]` → `[[Stem\|Display]]` in a text string |
| `process_files(files, index, execute)` | Iterates files, applies rewrite, writes if `--execute` |
| `main()` | CLI: `--execute` flag, `--scope notes\|reports\|all` |

---

## 11. Starter Prompt for Future Sessions

Copy the block below into a new Claude session. Fill in the `[PLACEHOLDER]` values with your actual paths and details.

---

````markdown
## Task: Fix Broken Obsidian Wiki-Links (Pipe Syntax Rewrite)

### Context

I have an auto-generated set of Obsidian permanent notes and reports. The wiki-links
use human-readable display names with spaces (e.g., `[[Cognitive Load Theory (CLT)]]`) but
the actual filenames use hyphens (e.g., `Cognitive-Load-Theory.md`). Obsidian does NOT
auto-resolve spaces to hyphens, so all multi-word links are broken (appear light-red).

**The fix:** Rewrite all wiki-links to use Obsidian pipe syntax:
`[[Cognitive Load Theory (CLT)|Cognitive Load Theory]]`

### My Project

- **Vault path:** `[YOUR_VAULT_PATH]`
  - Example: `D:\10_pur3v4d3r's-vault`
- **Project root:** `[YOUR_PROJECT_ROOT]`
  - Example: `999-report-organizing/_pkm-and-pkb-framework-1.0.0`
- **Permanent notes directory:** `[PROJECT_ROOT]/_permanent-notes/`
  - Contains: [NUMBER] `.md` files
- **Reports directory:** `[PROJECT_ROOT]/report-series/`
  - Contains: [NUMBER] `.md` report files
- **Scripts directory:** `[PROJECT_ROOT]/scripts/`
- **Python venv:** `[VAULT_PATH]/.venv`
- **OS:** Windows (use Git Bash or CMD)

### The Filename Sanitizer

All filenames were generated using this function (in `scripts/note_builder.py`):

```python
MAX_FILENAME_LENGTH = 80

def sanitize_filename(name: str) -> str:
    safe = re.sub(r'[<>:"/\\|?*\[\]()]', '', name)
    safe = re.sub(r'[\s_]+', '-', safe)
    safe = re.sub(r'-{2,}', '-', safe)
    safe = safe.strip('-')
    if len(safe) > MAX_FILENAME_LENGTH:
        safe = safe[:MAX_FILENAME_LENGTH].rstrip('-')
    return safe
```

### What I Need You to Do

1. **Check if `rewrite_wikilinks.py` already exists** in `scripts/`. If yes, verify its
   `NOTES_DIR` and `REPORTS_DIR` point to the correct directories (not extraction copies).

2. **If the script doesn't exist**, create it. The script must:
   - Build a resolution index from all `.md` files in the permanent notes directory
     (filename stems + YAML `aliases:` field → lowercase lookup → stem)
   - Preference originals over stubs for duplicate aliases
   - Regex-find all `[[...]]` links in each file
   - Skip links that already have pipe syntax (`|`)
   - Skip links where the display name exactly matches a filename stem
   - For all others: look up the display name in the index, rewrite to `[[stem|display]]`
   - Support `--execute` flag (dry-run by default) and `--scope notes|reports|all`
   - Include Windows UTF-8 stdout/stderr wrapper at the top of the script

3. **Run a dry run first** (`--scope all` without `--execute`), show me the output.

4. **Execute** after I confirm the dry run looks correct.

5. **Update the note generation scripts** (`note_builder.py`, `generate_stubs.py`) to
   include a `_pipe_link(display_name)` helper that generates pipe-syntax links going
   forward, so newly-generated notes don't have this problem.

6. **Verify** by grepping a sample file for pipe syntax and confirming the count looks right.

### Reference Document

The full technical reference for this process is at:
`[PROJECT_ROOT]/WIKILINK-RESOLUTION-PROCESS.md`

Read that file first — it contains the complete root cause analysis, the script's
architecture, known edge cases, and verification commands.

### Known Gotchas (Read These!)

- `REPORTS_DIR` must point to `report-series/`, NOT `extraction-material/markdown/`
- Windows needs `sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')` at script top
- After running, Obsidian needs Ctrl+P → "Reload app without saving" to pick up changes
- The regex `\[\[([^\[\]]+?)\]\]` can potentially match across YAML line boundaries — verify no YAML corruption in `expansion_topics` sections after running
- `sanitize_filename()` truncates at 80 chars — long concept names produce truncated stems, and that's expected
````

---

> **End of document.** This report plus the starter prompt should give any future Claude session everything it needs to replicate or extend this process.
