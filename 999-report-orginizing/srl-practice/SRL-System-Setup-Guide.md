# ═══════════════════════════════════════════════════════════════════════════
# SRL READING SYSTEM — INSTALLATION & SETUP GUIDE
# Complete setup instructions for the Zimmerman SRL Reading System
# ═══════════════════════════════════════════════════════════════════════════

## System Overview

This is an **8-document Obsidian-native system** implementing Zimmerman's Cyclical SRL Model for reading complex academic texts within your PKB. It integrates Forethought Phase preparation, Self-Reflection Phase evaluation, long-term calibration tracking, and mastery-oriented motivational design.

### Document Inventory

| # | File | Type | Purpose |
|---|------|------|---------|
| 1 | `SRL-Dashboard-MOC.md` | Dashboard/MOC | Central navigation hub with Dataview analytics and Meta Bind buttons |
| 2 | `SRL-Reading-Session-Template.md` | Templater Template | Master session template — Forethought (5 zones) + Self-Reflection (6 zones) |
| 3 | `SRL-Living-Learning-Agenda.md` | Persistent Note | Forward-planning handoff node — the physical feedback loop |
| 4 | `SRL-Calibration-Log.md` | Dataview Dashboard | Long-term calibration tracking with automated analytics |
| 5 | `SRL-Quick-Reference-Cards.md` | Reference Note | 5 reference cards: goal language, attribution retraining, mastery grammar, adaptive inference checklist, implementation survival guide |
| 6 | `SRL-Monthly-Review-Template.md` | Templater Template | Periodic meta-reflection across sessions |
| 7 | `SRL-Framework-Activation-Template.md` | Templater Template | Specialized Forethought for new theoretical frameworks |
| 8 | `SRL-Self-Explanation-Scaffold.md` | Scaffold Note | Performance-phase deep processing tool for complex sections |

---

## Prerequisites

### Required Plugins

| Plugin | Purpose in System | Required? |
|--------|------------------|-----------|
| **Templater** | Dynamic templates (session, monthly review, framework activation) | ✅ Required |
| **Dataview** | Automated session analytics, calibration tracking, attribution patterns | ✅ Required |
| **Meta Bind** | Interactive buttons on dashboard, inline selects in templates | ✅ Required |
| **Tasks** | Checkbox tracking across documents | ✅ Required |

### Recommended Plugins

| Plugin | Purpose | Required? |
|--------|---------|-----------|
| **QuickAdd** | One-click session creation from command palette | Recommended |
| **Charts** | Visual calibration trend charts (enhance Calibration Log) | Optional |
| **Tracker** | Habit tracking for session consistency | Optional |
| **Commander** | Custom hotkeys for SRL workflow | Optional |

### Plugin Installation Verification

1. Open Obsidian Settings (`Ctrl/Cmd + ,`)
2. Navigate to **Community Plugins**
3. Verify each required plugin is installed and **enabled**:
   - [x] Templater
   - [x] Dataview
   - [x] Meta Bind
   - [x] Tasks
4. If any plugin is missing:
   - Click **Browse** in Community Plugins
   - Search for the plugin name
   - Click **Install** then **Enable**

---

## Installation Steps

### Step 1: Create Folder Structure

Create the following folders in your vault:

```
Your Vault/
├── _templates/              ← If you don't already have this
├── SRL-System/              ← System documents live here
├── SRL-Sessions/            ← Individual session notes
└── SRL-Reviews/             ← Monthly review notes
```

**How to create folders:**
- Right-click in the file explorer panel → "New folder"
- Or use your OS file manager in the vault directory

### Step 2: Place Files

Move the downloaded files to the correct locations:

| File | Destination |
|------|------------|
| `SRL-Reading-Session-Template.md` | `_templates/` |
| `SRL-Monthly-Review-Template.md` | `_templates/` |
| `SRL-Framework-Activation-Template.md` | `_templates/` |
| `SRL-Dashboard-MOC.md` | `SRL-System/` |
| `SRL-Living-Learning-Agenda.md` | `SRL-System/` |
| `SRL-Calibration-Log.md` | `SRL-System/` |
| `SRL-Quick-Reference-Cards.md` | `SRL-System/` |
| `SRL-Self-Explanation-Scaffold.md` | `SRL-System/` |

### Step 3: Configure Templater

1. Open **Settings** → **Templater**
2. Set **Template Folder Location** to `_templates` (or wherever your templates folder is)
3. Enable **Trigger Templater on new file creation** (optional but recommended)
4. Under **Folder Templates** (optional):
   - Folder: `SRL-Sessions` → Template: `_templates/SRL-Reading-Session-Template.md`

### Step 4: Configure Dataview

1. Open **Settings** → **Dataview**
2. Ensure **Enable JavaScript Queries** is ON (required for DataviewJS blocks in Calibration Log and Dashboard)
3. Ensure **Enable Inline Queries** is ON
4. Set **Refresh Interval** to a reasonable value (e.g., 2500ms)

### Step 5: Configure Meta Bind

1. Open **Settings** → **Meta Bind**
2. No special configuration needed — the buttons and inline selects in the templates will work with default settings
3. **Important:** Meta Bind buttons work in **Reading Mode** — switch to Reading Mode to use the dashboard buttons

### Step 6: Set Up QuickAdd (Recommended)

This creates a one-click command to start a new reading session:

1. Open **Settings** → **QuickAdd**
2. Click **Add Choice** at the top
3. **Name:** "New SRL Reading Session"
4. **Type:** Template
5. Click the ⚙️ gear icon on the new choice:
   - **Template Path:** `_templates/SRL-Reading-Session-Template.md`
   - **File Name Format:** `{{DATE:YYYY-MM-DD}}-{{TIME:HHmm}}-srl-session`
   - **Create in folder:** `SRL-Sessions`
   - Enable **Open** (auto-open the new note)
6. Repeat for Monthly Review and Framework Activation if desired
7. Optionally add to command palette via **Manage Macros** or **Commander**

### Step 7: Customize Frontmatter Placeholders

The templates use `{{date}}` and `{{time}}` placeholders in persistent notes (Learning Agenda, Calibration Log, etc.). Replace these with the actual date when you first create these notes, or let Templater handle them if you create them through Templater.

### Step 8: Initial Setup of Persistent Notes

Open each persistent note and complete the initial setup:

1. **SRL-Living-Learning-Agenda:**
   - Fill in your current distal learning goals
   - Add your initial reading queue
   - Leave other sections empty — they'll be populated through sessions

2. **SRL-Calibration-Log:**
   - No initial setup needed — it auto-populates from session data
   - Verify the Dataview queries render (may show "No data" initially — that's expected)

3. **SRL-Dashboard-MOC:**
   - Verify Meta Bind buttons render in Reading Mode
   - Verify Dataview queries render (will show empty/no-data initially)
   - Adjust template paths in the Meta Bind button configurations if your template folder is different from `_templates/`

---

## Verification Checklist

After installation, verify the system works:

- [x] Templates folder contains all 3 template files
- [x] SRL-System folder contains all 4 system documents + scaffold
- [x] SRL-Sessions and SRL-Reviews folders exist
- [x] Templater is configured with correct template folder path
- [x] Dataview JavaScript queries are enabled
- [x] Meta Bind buttons render in Reading Mode on the Dashboard
- [ ] Creating a new note in SRL-Sessions triggers the session template (if folder templates configured)
- [x] QuickAdd "New SRL Reading Session" appears in command palette (if configured)
- [ ] Wiki-links in templates resolve to your existing permanent notes

---

## First Session Walkthrough

### Before Your First Session

1. **Read** the Quick Reference Cards (Card 5: Early Implementation Survival Guide)
2. **Open** the SRL Dashboard MOC and review the Scaffold Fading Schedule
3. **Remember:** Start with ONLY Zones 1 and 3 of Forethought + Zone 1 of Self-Reflection

### Running Your First Session

1. Use QuickAdd or Templater to create a new session note
2. Fill in the text title, type, and schema level when prompted
3. Complete **Zone 1** (Prior Knowledge Activation) — even briefly
4. Complete **Zone 3** (Goal Setting) — set ONE specific comprehension criterion
5. Skip Zones 2, 4, 5 for now
6. **Read** your text with your process goals in mind
7. After reading, complete **Zone 1** of Self-Reflection (Cold Reconstruction)
8. Skip remaining Self-Reflection zones for now
9. Update the Living Learning Agenda with one carry-forward item

### Building Up Over Weeks 2-8

Follow the scaffold fading schedule in the Dashboard MOC. Add one new zone every 1-2 weeks as the existing zones become more fluent.

---

## Troubleshooting

### Dataview queries show no results
- Ensure your session notes have the `#srl-session` tag in their frontmatter
- Ensure `reflection-completed: true` is set in frontmatter after completing Self-Reflection
- Check that Dataview JavaScript is enabled in Dataview settings

### Meta Bind buttons don't work
- Switch to **Reading Mode** (buttons don't render in Edit/Live Preview)
- Verify the template paths in button configurations match your actual template paths
- Check Meta Bind plugin is enabled

### Templater prompts don't appear
- Ensure Templater is enabled
- Ensure the file is being created through Templater (not just a regular new note)
- Check that Templater's template folder path is correct

### Wiki-links show as unresolved
- Some wiki-links reference notes that may not yet exist in your PKB
- This is expected — create permanent notes as your knowledge grows
- Core notes like [[Zimmerman's-Cyclical-SRL-Model]], [[Self-Efficacy]], etc. should already exist

---

## Customization Guide

### Adding Custom Process Goals
Edit the Session Template's Zone 3 to include process goals relevant to your reading context. The default goals are good starting points but should evolve as your practice develops.

### Modifying Comprehension Criterion Templates
The Quick Reference Cards contain fill-in-the-blank templates. Add your own domain-specific templates as you discover what works for your reading material.

### Adding Strategy Tags
The Living Learning Agenda contains a starter vocabulary of strategy tags. Add new tags as you discover new strategies. Keep the vocabulary small and stable — too many tags reduces queryability.

### Integrating with Existing PKB Workflows
- The session template creates notes compatible with your existing tag taxonomy
- Wiki-links use your actual permanent note names
- Strategy tags can be added to your existing tag hierarchy
- The Calibration Log queries can be embedded in existing MOCs via Dataview

---

## Theoretical Grounding

This system synthesizes three comprehensive reports on Zimmerman's SRL model:

1. **Focused Analysis Report** — Deep theoretical architecture with 5 practical tools
2. **Operational Guide** — 7 complete templates with zone-based architecture
3. **Practitioner Architecture** — Generativity-based calibration and closing-the-loop mechanisms

Key theoretical influences:
- Zimmerman's Cyclical SRL Model (2000, 2002)
- Bandura's Self-Efficacy Theory (1997)
- Achievement Goal Theory (Dweck, Ames, Elliot)
- Self-Determination Theory (Deci & Ryan)
- Weiner's Attribution Theory (1985)
- Formative Assessment (Black & Wiliam, 1998)
- Chi et al.'s Self-Explanation Research (1994)

---

*SRL Reading System v1.0 — Generated for PKB Integration*
*Based on Zimmerman's Cyclical SRL Model*
