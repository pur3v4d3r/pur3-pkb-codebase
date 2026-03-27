---
type: reference-guide
status: evergreen
created: 2026-03-26
updated: 2026-03-26
tags:
  - srl-system
  - meta-bind
  - obsidian-plugin
  - reference-guide
  - button-setup
aliases:
  - "Meta Bind Button Guide"
  - "SRL Button Setup"
  - "Meta Bind Setup Instructions"
---

# 🔧 Meta Bind Button Setup Guide for SRL System

> [!abstract] Purpose
> This guide documents how Meta Bind buttons are configured in the SRL system, explains the syntax, and provides instructions for creating future buttons. Use this as a reference whenever you need to add, modify, or troubleshoot Meta Bind buttons.

---

## 📋 Current Button Inventory

### SRL-Dashboard-MOC.md — 6 Buttons

| Button ID | Label | Type | Action |
|-----------|-------|------|--------|
| `new-srl-session` | 📖 New Reading Session | `templaterCreateNote` | Creates session in `srl-sessions/` |
| `open-learning-agenda` | 📋 Learning Agenda | `open` | Opens [[SRL-Living-Learning-Agenda]] |
| `open-calibration-log` | 📊 Calibration Log | `open` | Opens [[SRL-Calibration-Log]] |
| `open-reference-cards` | 🃏 Reference Cards | `open` | Opens [[SRL-Quick-Reference-Cards]] |
| `new-monthly-review` | 📈 Monthly Review | `templaterCreateNote` | Creates review in `srl-reviews/` |
| `new-framework-activation` | 🧬 Framework Activation | `templaterCreateNote` | Creates activation in `srl-sessions/` |

### INPUT Fields in Templates

| Template | Field | Bound Property | Options |
|----------|-------|----------------|---------|
| SRL-Reading-Session-Template | Zone 2 Complexity | `complexity` | High, Moderate, Low |
| SRL-Reading-Session-Template | Zone 1 Comprehension | `comprehension-level` | Full, Substantial, Partial, Minimal |
| SRL-Monthly-Review-Template | Comprehension Trend | `comprehension-trend` | Improving, Flat, Variable, Declining |
| SRL-Monthly-Review-Template | Process Goal Trend | `process-goal-trend` | Improving, Flat, Variable, Declining |
| SRL-Monthly-Review-Template | Efficacy Trend | `efficacy-trend` | Increasing, Stable, Decreasing |
| SRL-Monthly-Review-Template | Calibration Trend | `calibration-trend` | Decreasing, Stable, Increasing |
| SRL-Monthly-Review-Template | Miscalibration Direction | `miscalibration-direction` | Overconfident, Underconfident, Well-calibrated |
| SRL-Monthly-Review-Template | Efficacy Comparison | `efficacy-comparison` | Higher, Same, Lower |

---

## 🏗️ Vault Path Reference

These are the actual paths used in this vault. **All Meta Bind button paths must use these exact paths.**

| Resource | Vault-Relative Path |
|----------|-------------------|
| **Templater Template Folder** | `99-system/01-quickadd/02-templates/` |
| **SRL System Documents** | `999-report-orginizing/srl-practice/srl-system/` |
| **SRL Session Notes** | `999-report-orginizing/srl-practice/srl-sessions/` |
| **SRL Review Notes** | `999-report-orginizing/srl-practice/srl-reviews/` |
| **SRL Reading Session Template** | `99-system/01-quickadd/02-templates/SRL-Reading-Session-Template.md` |
| **SRL Monthly Review Template** | `99-system/01-quickadd/02-templates/SRL-Monthly-Review-Template.md` |
| **SRL Framework Activation Template** | `99-system/01-quickadd/02-templates/SRL-Framework-Activation-Template.md` |

---

## 📖 Meta Bind Button Syntax Reference

### Button Definition (Code Block)

Define buttons using a `meta-bind-button` fenced code block. These can be placed in any note.

````markdown
```meta-bind-button
label: "Button Label Text"
id: unique-button-id
style: primary
actions:
  - type: actionType
    param1: value1
    param2: value2
```
````

### Inline Button Reference

Reference any defined button inline using backtick syntax:

```markdown
`BUTTON[unique-button-id]`
```

The referenced button must be defined either:
1. **In the same note** — as a `meta-bind-button` code block with matching `id`
2. **Globally** — in Meta Bind Settings → Button Templates

### Button Styles

| Style | Appearance |
|-------|-----------|
| `primary` | Blue/accent colored, prominent |
| `default` | Standard gray button |
| `destructive` | Red, for dangerous actions |
| `plain` | Minimal, text-only appearance |

---

## ⚡ Action Types

### 1. `open` — Open a Note

Opens an existing note by wiki-link. Obsidian resolves the link by name regardless of folder.

````markdown
```meta-bind-button
label: "📋 Open Note"
id: open-my-note
style: default
actions:
  - type: open
    link: "[[Note-Name]]"
```
````

### 2. `templaterCreateNote` — Create Note from Templater Template

Creates a new note using a Templater template. Templater prompts and logic execute on creation.

````markdown
```meta-bind-button
label: "📖 New Session"
id: create-session
style: primary
actions:
  - type: templaterCreateNote
    templateFile: "99-system/01-quickadd/02-templates/Your-Template.md"
    folderPath: "path/to/output/folder"
    fileName: ""
```
````

**Parameters:**
- `templateFile` — Vault-relative path to the Templater template file
- `folderPath` — Vault-relative path to the folder where the new note is created
- `fileName` — Filename for the new note (empty string `""` prompts user or uses template logic)

> [!warning] Path Format
> - Use **forward slashes** `/` only (not backslashes)
> - Paths are **relative to vault root** (no leading slash)
> - Do NOT include the `.md` extension in `fileName`
> - The `templateFile` path MUST include `.md`

### 3. `updateMetadata` — Update Frontmatter Property

Updates a YAML frontmatter property on the current note.

````markdown
```meta-bind-button
label: "🌱 Set Seedling"
id: set-seedling
style: default
actions:
  - type: updateMetadata
    bindTarget: "status"
    evaluate: false
    value: "seedling"
```
````

**Parameters:**
- `bindTarget` — The frontmatter property to update
- `value` — The value to set
- `evaluate` — Set `true` to evaluate `value` as JavaScript expression

### 4. `command` — Run an Obsidian Command

Runs any command from the Obsidian command palette.

````markdown
```meta-bind-button
label: "🔄 Reload"
id: reload-vault
style: default
actions:
  - type: command
    command: "app:reload"
```
````

### 5. `js` — Run JavaScript

Runs custom JavaScript. Requires `enableJs: true` in Meta Bind settings (already enabled).

````markdown
```meta-bind-button
label: "📊 Calculate"
id: run-calc
style: default
actions:
  - type: js
    file: "path/to/script.js"
```
````

### 6. Multiple Actions

Buttons can chain multiple actions sequentially:

````markdown
```meta-bind-button
label: "Complete & Navigate"
id: complete-and-go
style: primary
actions:
  - type: updateMetadata
    bindTarget: "status"
    evaluate: false
    value: "complete"
  - type: open
    link: "[[Next-Note]]"
```
````

---

## 📝 INPUT Field Syntax Reference

### Inline Select (Dropdown)

Place inline within any note to create a dropdown bound to a frontmatter property:

```markdown
`INPUT[inlineSelect(option(Value1), option(Value2), option(Value3)):frontmatter-property]`
```

**Example from SRL Session Template:**
```markdown
`INPUT[inlineSelect(option(High), option(Moderate), option(Low)):complexity]`
```

This creates a dropdown that writes the selected value to the `complexity` frontmatter property.

### Other Input Types

```markdown
`INPUT[text:property-name]`           — Text input
`INPUT[number:property-name]`         — Number input
`INPUT[toggle:property-name]`         — Boolean toggle
`INPUT[date:property-name]`           — Date picker
`INPUT[slider(minValue(1), maxValue(10)):property-name]`  — Slider
`INPUT[textArea:property-name]`       — Multi-line text
```

---

## 🔨 How to Create a New Button

### Step-by-Step Process

1. **Decide the action type** — What should the button do? (open, create, update, command)

2. **Choose a unique ID** — Use kebab-case, descriptive: `new-srl-session`, `open-calibration-log`

3. **Write the button definition** — Place the `meta-bind-button` code block in your note:

````markdown
```meta-bind-button
label: "🏷️ Your Button Label"
id: your-button-id
style: default
actions:
  - type: open
    link: "[[Target-Note]]"
```
````

4. **Add inline reference** (optional) — If you want the button rendered inline elsewhere in the same note:

```markdown
`BUTTON[your-button-id]`
```

5. **Test** — Switch to Reading Mode or Live Preview and click the button

### For Global Buttons (Available Across All Notes)

1. Open **Settings → Meta Bind → Button Templates**
2. Add a new template with your button configuration
3. Reference it from any note using `BUTTON[template-id]`

### For `templaterCreateNote` Buttons Specifically

1. Ensure the **template file exists** at the specified path
2. Ensure the **output folder exists** in your vault
3. Verify the template path matches your Templater template folder setting
4. Test by clicking the button — Templater prompts should appear

---

## 🔍 Troubleshooting

### Buttons Don't Render
- **Switch to Reading Mode or Live Preview** — buttons don't render in Source mode
- Verify Meta Bind plugin is **enabled** in Community Plugins settings
- Check for YAML syntax errors in the button code block

### `BUTTON[id]` Shows as Plain Text
- Verify the button definition with that `id` exists in the **same note** or in **global Button Templates**
- Check the `id` matches exactly (case-sensitive)
- Ensure the button code block uses the correct language identifier: `meta-bind-button`

### `templaterCreateNote` Fails
- Verify `templateFile` path is correct (vault-relative, forward slashes, includes `.md`)
- Verify `folderPath` exists in the vault
- Ensure Templater plugin is installed and enabled
- Check Templater's template folder setting includes the template location

### INPUT Fields Don't Work
- Verify the syntax: `INPUT[type(options):property]` — wrapped in backticks
- The frontmatter property will be created automatically if it doesn't exist
- Check Meta Bind's `excludedFolders` setting doesn't include your note's folder

### Values Not Saving
- Check the `syncInterval` in Meta Bind settings (default 200ms is fine)
- Ensure the note isn't in an excluded folder
- Verify the frontmatter property name matches exactly

---

## 📐 Conventions for This Vault

1. **Button IDs** — Use kebab-case: `new-srl-session`, `open-calibration-log`
2. **Template paths** — Always start from vault root: `99-system/01-quickadd/02-templates/`
3. **Output folders** — Use full vault-relative paths: `999-report-orginizing/srl-practice/srl-sessions/`
4. **Inline references** — Place `BUTTON[id]` references in a Quick Actions section at the top of notes
5. **Button definitions** — Place `meta-bind-button` code blocks below the inline references in the same note
6. **INPUT fields** — Use inside templates that Templater creates; the INPUT renders in the created note

---

> [!connections-and-links]
> - [[SRL-Dashboard-MOC]] — The primary note containing the SRL system buttons
> - [[SRL-System-Setup-Guide]] — Full installation guide for the SRL system
> - [[SRL-Reading-Session-Template]] — Template with INPUT inline select fields
> - [[SRL-Monthly-Review-Template]] — Template with INPUT inline select fields
