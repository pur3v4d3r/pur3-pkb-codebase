---
title: "PKB System Setup Guide"
type: reference
status: evergreen
tags:
  - meta
  - setup
  - reference
created: 2026-03-14
updated: 2026-03-14
---

# PKB System Setup Guide

> [!info] **What This Covers**
> Complete installation and configuration instructions for the Permanent Notes Generator ecosystem: Templater templates, Dataview dashboards, QuickAdd macros, and supporting scripts.

---

## Prerequisites

### Required Plugins

Install these from **Settings > Community Plugins > Browse**:

| Plugin | Author | Purpose |
|--------|--------|---------|
| **Templater** | SilentVoid13 | Dynamic templates with prompts and auto-fill |
| **Dataview** | blacksmithgu | Live queries, dashboards, inline metadata |
| **QuickAdd** | chhoumann | Macros, scripts, capture workflows |

### Recommended Plugins

| Plugin | Purpose |
|--------|---------|
| **Markmap** | Mind-map visualization of note connections |
| **Charts** | Visual charts from Dataview data |
| **Kanban** | Board view for note workflow stages |

---

## Folder Structure

Create this folder structure in your vault (adjust paths to your preference, then update the scripts/templates accordingly):

```
vault-root/
├── 00-inbox/
│   ├── 01-reports/              ← Raw reports before processing
│   └── 02-topic-sets/           ← Thematic groupings
├── 03-notes/
│   └── 01_permanent-notes/      ← ALL permanent notes go here
├── 04-library/                   ← Reference material
├── 05-templates/                 ← Templater templates
│   └── permanent-note-template.md
├── 06-dashboards/                ← Dataview dashboards
│   ├── PKB-Dashboard.md
│   └── Dataview-Query-Reference.md
├── 99-scripts/
│   └── quickadd/                 ← QuickAdd user scripts
│       ├── validate-permanent-note.js
│       ├── quick-create-note.js
│       └── batch-audit-notes.js
├── 999-report-orginizing/
│   └── _extractor-output/        ← pkb_extractor.py output
└── metadata-template.md          ← YAML reference
```

---

## Step 1: Configure Templater

1. Open **Settings > Templater**
2. Set **Template folder location** to `05-templates`
3. Enable **Trigger Templater on new file creation** (optional but useful)
4. Under **Folder Templates** (optional):
   - Folder: `03-notes/01_permanent-notes`
   - Template: `05-templates/permanent-note-template.md`
   - This auto-applies the template when you create a new file in the permanent notes folder

### Place the Template

Copy `permanent-note-template.md` into your `05-templates/` folder. The template uses these Templater functions:

| Function | What It Does |
|----------|-------------|
| `tp.system.prompt()` | Opens a text input dialog |
| `tp.system.suggester()` | Opens a dropdown selection dialog |
| `tp.date.now()` | Inserts current date |
| `tp.file.rename()` | Renames the file to match the title |
| `tp.file.cursor()` | Places cursor here after template insertion |

### How to Use

- Create a new file anywhere, then run **Templater: Insert Template** (or your hotkey)
- Select `permanent-note-template`
- Fill in the prompted fields (title, domain, complexity, etc.)
- The file auto-renames to match your title
- Start writing where the cursor lands

---

## Step 2: Configure Dataview

1. Open **Settings > Dataview**
2. Under **General Settings**:
   - Enable **Enable JavaScript Queries** (required for DataviewJS blocks)
   - Enable **Enable Inline Queries** (for inline `= this.field` syntax)
   - Enable **Enable Inline JavaScript Queries** (for `$= dv.pages()...` syntax)
3. Under **Codeblock Settings**:
   - **Inline Query Prefix**: leave as `=` (default)

### Place the Dashboards

Copy these files into your `06-dashboards/` folder (or wherever you prefer):

- `PKB-Dashboard.md` — The main knowledge base overview
- `Dataview-Query-Reference.md` — Reusable query cookbook

> [!tip] **Note on Templater Tags in Dashboard Files**
> The dashboard files use `<% tp.date.now("YYYY-MM-DD") %>` for the created/updated dates. When you first open them, run Templater to resolve these. Alternatively, replace them with a static date before placing in your vault.

---

## Step 3: Configure QuickAdd

### Initial Setup

1. Open **Settings > QuickAdd**
2. You'll create three Macro Choices (one for each script)

### Macro 1: Validate Permanent Note

1. In QuickAdd settings, type a name: `Validate Note` → click **Add Choice** → select **Macro**
2. Click the ⚙️ gear icon on the new choice → **Configure Macro**
3. Under **Macro Commands**, click **User Script** → navigate to `99-scripts/quickadd/validate-permanent-note.js`
4. Click the ⚙️ on the script to configure its settings:
   - **Append report to note**: Toggle on/off per preference
   - **Minimum wiki-links**: `8` (default)
   - **Permanent notes folder**: `03-notes/01_permanent-notes`
5. Back in QuickAdd settings, click the ⚡ lightning bolt to add it to the command palette
6. Optionally assign a hotkey in **Settings > Hotkeys** → search "QuickAdd: Validate Note"

### Macro 2: Quick Create Note

1. Add Choice: `New Permanent Note` → **Macro**
2. Configure Macro → add User Script → `99-scripts/quickadd/quick-create-note.js`
3. Configure script settings:
   - **Notes folder**: `03-notes/01_permanent-notes`
   - **Open after creation**: toggle on
4. Enable ⚡ for command palette access
5. Assign a hotkey (recommended: `Alt+N`)

### Macro 3: Batch Audit

1. Add Choice: `Batch Audit` → **Macro**
2. Configure Macro → add User Script → `99-scripts/quickadd/batch-audit-notes.js`
3. Configure script settings:
   - **Notes folder**: `03-notes/01_permanent-notes`
   - **Report folder**: `999-report-orginizing`
4. Enable ⚡ for command palette access

### Important QuickAdd Notes

- User script `.js` files must be in your vault but **NOT** in the `.obsidian/` folder or any folder starting with `.`
- Scripts have full access to the Obsidian API via `params.app`
- Scripts can access Dataview's API via `app.plugins.plugins.dataview.api`
- The `params.quickAddApi` provides prompt dialogs, suggesters, and format helpers
- Variables set in one macro command (`variables.myVar = "x"`) are available in subsequent commands in the same macro

---

## Step 4: Workflow Overview

### Creating Notes from Claude-Generated Artifacts

1. Run the **Permanent Notes Generator** Claude Project with an extracted report
2. Download each generated markdown artifact
3. Place the `.md` files directly into `03-notes/01_permanent-notes/`
4. The filenames from Claude already match wiki-link conventions
5. Run **Validate Note** (QuickAdd) on each to verify quality
6. Periodically run **Batch Audit** to check overall vault health

### Creating Notes Manually

1. Trigger **New Permanent Note** (QuickAdd hotkey)
2. Fill in the form (title, domain, complexity, etc.)
3. Note is created with full metadata skeleton
4. Write the content
5. Run **Validate Note** to check quality

### Monitoring Your PKB

1. Open `06-dashboards/PKB-Dashboard.md` for a live overview
2. Check the "Ghost Links" section for expansion opportunities
3. Check "Orphan Notes" for notes needing more connections
4. Check "Review Schedule" for notes due for update
5. Run **Batch Audit** monthly for a comprehensive quality report

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Templater tags not resolving | Run `Templater: Replace templates in active file` from command palette |
| Dataview queries show errors | Check Settings > Dataview > Enable JavaScript Queries is ON |
| QuickAdd scripts not appearing | Ensure `.js` files are NOT in `.obsidian/` folder |
| Script errors about Dataview | Make sure Dataview plugin is installed and enabled |
| File already exists error | The note title matches an existing file; QuickAdd offers to open it instead |
| Dashboard queries return empty | Check the folder path matches your actual folder structure |

---

*Setup guide version 1.0 — Last updated: 2026-03-14*
