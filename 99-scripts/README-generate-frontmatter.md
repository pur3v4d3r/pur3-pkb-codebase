# `generate_frontmatter.py` — README

A Python utility that reviews a single markdown note and generates (or
updates) a PKB-compliant YAML frontmatter block for it.

It auto-extracts what it can (title, dates, tags, wiki-links, summary,
keywords) and either prompts you for the rest (interactive mode) or fills
sensible defaults (non-interactive mode).

---

## What the script extracts automatically

| Field | Source |
|---|---|
| `title` | Existing frontmatter → first `# H1` → humanised filename |
| `doc_created` | Existing frontmatter → `YYYY-MM-DD` prefix in filename → file ctime |
| `doc_modified` | Today's date |
| `doc_id` | `PERM-<initials>-<created-date>` |
| `aliases` | Variants of the title (cased, lowercase, slugged) |
| `tags` | `#hashtags` found in the body (deduplicated, capped) |
| `related_concepts` | `[[wiki-links]]` found in the body |
| `summary` | First non-empty paragraph after the H1 |
| `keywords` | Top-frequency content words (stopwords filtered) |
| `author` | Existing frontmatter → `CONFIG["default_author"]` |

Anything still missing is either asked for interactively or filled from
`CONFIG["defaults"]` in non-interactive mode.

---

## Installation

From the vault root:

```bash
# Activate your existing venv
source .venv/Scripts/activate          # Git Bash / WSL
# .venv\Scripts\activate              # PowerShell

# Install dependencies
pip install python-frontmatter rich click pyyaml
```

---

## Usage

The script takes one positional argument: the path to a markdown file.

### 1. Preview only (recommended first run)

```bash
python 99-scripts/generate_frontmatter.py "path/to/note.md" --dry-run
```

Prints the proposed frontmatter to the terminal. Nothing is written.

### 2. Interactive write (default)

```bash
python 99-scripts/generate_frontmatter.py "path/to/note.md"
```

You'll be prompted to confirm/edit each field, then asked to confirm the
write. A `.bak` copy is created next to the file by default.

### 3. Fully automatic (no prompts, defaults applied)

```bash
python 99-scripts/generate_frontmatter.py "path/to/note.md" --non-interactive
```

### 4. Replace existing frontmatter completely

By default the script **merges** with any existing frontmatter (preserving
fields you've already set). Use `--overwrite` to start from scratch:

```bash
python 99-scripts/generate_frontmatter.py "path/to/note.md" --overwrite
```

### 5. Skip the backup file

```bash
python 99-scripts/generate_frontmatter.py "path/to/note.md" --no-backup
```

---

## All flags

| Flag | Default | Effect |
|---|---|---|
| `--dry-run` | off | Print proposed frontmatter; do not modify the file |
| `--non-interactive` | off | Skip all prompts; use defaults |
| `--overwrite` | off | Replace existing frontmatter entirely (default = merge) |
| `--backup` / `--no-backup` | `--backup` | Write `<file>.md.bak` before modifying |
| `--help` | — | Show the click help screen |

---

## Examples

```bash
# Preview frontmatter for the metadata template itself
python 99-scripts/generate_frontmatter.py "metadata-template.md" --dry-run

# Generate non-interactively for a daily note
python 99-scripts/generate_frontmatter.py "01_daily-notes/2026-04-21.md" --non-interactive

# Force a clean rewrite, skip backup
python 99-scripts/generate_frontmatter.py "00-inbox/some-note.md" --overwrite --no-backup
```

---

## Customisation

All tunables live in the `CONFIG` block near the top of the script:

```python
CONFIG = {
    "default_author": "GitHub Copilot",
    "defaults": {
        "doc_type":         "Permanent Note",
        "primary_domain":   "General",
        "knowledge_level":  "developing",
        "status":           "draft",
        ...
    },
    "max_inferred_tags":     8,
    "max_inferred_keywords": 10,
    "max_inferred_related":  10,
    "stopwords": { ... },
}
```

Edit those values to match your vault conventions. No other code changes
needed.

---

## Safety notes

- Always run `--dry-run` first on unfamiliar notes.
- The default `--backup` writes `<note>.md.bak` so you can recover if the
  generated frontmatter is wrong.
- Existing frontmatter is **preserved by default** — `--overwrite` is
  opt-in.
- The script only operates on the single file you pass in. It is **not**
  recursive. For batch operations, wrap it in a shell loop:

```bash
# Bash: apply non-interactively to every note in a folder
for f in 00-inbox/*.md; do
  python 99-scripts/generate_frontmatter.py "$f" --non-interactive --no-backup
done
```

---

## Exit codes

| Code | Meaning |
|---|---|
| `0` | Success (or dry run completed) |
| `1` | File is not markdown, or frontmatter parsing failed |

---

## Troubleshooting

**`Missing dependencies`** — install the four required packages listed in
the Installation section.

**Existing frontmatter shows up wrong / duplicated** — your file probably
has malformed YAML. Open it in VS Code, fix the YAML manually, then re-run
with `--overwrite`.

**Tags inferred from code blocks** — the script strips fenced code blocks
before tag extraction, but inline `#hashtag` mentions in prose will still
be captured. Edit them out interactively, or remove them from the body.

**Want a different field set** — edit the `build_frontmatter()` function;
each field is assigned on its own line for easy add/remove.
