---
tags:
aliases:
  - SPES Quick Start
  - Getting Started
  - 15-Minute Guide
  - Onboarding
status: evergreen
certainty: verified
priority: high
created: 2025-12-24
type: tutorial
project: prompt-engineering-templater-system
link-up: "[[00-meta/spes/01-spes-master-operations-manual]]"
---

# 🚀 SPES Quick Start Guide

> [!abstract] Get Operational in 15 Minutes
> This guide gets you creating, managing, and optimizing prompts immediately. For comprehensive documentation, see [[00-meta/spes/01-spes-master-operations-manual]].

---

## ⏱️ Minute 1-3: Understand the System

### What SPES Does

```
📝 CREATE prompts quickly using templates and reusable components
🔍 FIND relevant components through intelligent search
🧪 TEST prompts systematically with structured documentation
📊 TRACK usage, quality, and performance over time
🔄 IMPROVE through pattern detection and optimization workflows
```

### The Three Pillars (Mental Model)

| Pillar | Think of it as... | What it contains |
|--------|-------------------|------------------|
| **Component Library** | LEGO bricks | Reusable prompt pieces |
| **Sequential Workflows** | Assembly instructions | Multi-step patterns |
| **Intelligence Layer** | Quality control | Analytics & discovery |

---

## ⏱️ Minute 4-7: Create Your First Prompt

### Option A: Quick Capture (10 seconds)

For capturing an idea before you forget:

1. Open Command Palette (`Ctrl+P`)
2. Type "QuickAdd" → Select "Prompt Quick Capture"
3. Enter: Title and brief description
4. **Done!** → Saved to `00-inbox/prompt-ideas/`

### Option B: Full Prompt (2 minutes)

For a complete, ready-to-use prompt:

1. Create new note in `08-active-prompts/` folder
2. Copy this minimal template:

```markdown
---
type: prompt
id: 20251224143022
status: active
version: "1.0.0"
rating: "0.0"
confidence: speculative
maturity: seedling
source: original
created: 2025-12-24
modified: 2025-12-24
usage-count: 0
tags:
  - "year/2025"
  - "prompt-engineering"
  - "domain/general"
---

# [Your Prompt Title]

> [!abstract] Purpose
> [One sentence: What does this prompt accomplish?]

## System Context

[Background information the LLM needs]

## Instructions

[Clear directives for what to do]

## Output Format

[How the response should be structured]

## Constraints

[What NOT to do, boundaries, restrictions]
```

3. Fill in the bracketed sections
4. **Done!** → Production-ready prompt

---

## ⏱️ Minute 8-10: Use the Component Library

### Finding Components

**Quick Search** (Obsidian Search):
```
path:02-component-library tag:#persona
```

**By Type**:
- Personas: `tag:#persona`
- Instructions: `tag:#instruction`
- Constraints: `tag:#constraint`
- Formats: `tag:#format`

### Inserting Components

1. Find the component you want
2. Copy the prompt text from the component note
3. Paste into your prompt
4. **Important**: Add the component link to your metadata:

```yaml
components-used:
  - "[[component-name]]"
```

### Common Starter Components

| Need | Component to Find |
|------|-------------------|
| Expert persona | `tag:#persona tag:#expert` |
| Step-by-step | `tag:#instruction tag:#step-by-step` |
| Markdown output | `tag:#format tag:#markdown` |
| No speculation | `tag:#constraint tag:#accuracy` |

---

## ⏱️ Minute 11-13: Test Your Prompt

### Quick Test Documentation

After running your prompt, create a simple test note:

```markdown
---
type: test-result
prompt-tested: "[[my-prompt-name]]"
test-date: 2025-12-24
test-type: functional
success: true
quality-score: 7.5
---

## What I Tested
[Brief description of test scenario]

## Result Summary
- ✅ Output format correct
- ✅ Instructions followed
- ⚠️ Could be more detailed

## Next Steps
- [ ] Adjust instructions for more detail
```

### Update Your Prompt After Testing

```yaml
# Update these fields:
usage-count: 1                    # Increment
rating: "7.5"                     # Based on test
confidence: provisional           # After first test
modified: 2025-12-24              # Today's date
```

---

## ⏱️ Minute 14-15: Know Your Dashboards

### Primary Dashboard Location

`06-dashboards/prompt-engineering-dashboard.md`

### Quick Queries to Remember

**See all your prompts:**
```dataview
TABLE status, rating, maturity
FROM "08-active-prompts"
WHERE type = "prompt"
SORT rating DESC
```

**Find components by type:**
```dataview
TABLE component-type, domain, usage-count
FROM "02-component-library"
WHERE type = "component"
SORT usage-count DESC
```

**Prompts needing review:**
```dataview
LIST
FROM "08-active-prompts"
WHERE maturity = "seedling" AND created < date(today) - dur(7 days)
```

---

## ✅ You're Now Operational!

### What You Can Now Do

- [x] Capture prompt ideas quickly
- [x] Create full prompts with proper metadata
- [x] Find and use library components
- [x] Document test results
- [x] Track prompt quality

### Next Steps (When Ready)

| Want to... | Go to... |
|------------|----------|
| Learn all metadata fields | [[metadata-schema-reference]] |
| Understand workflows | [[architecture-overview]] |
| Master the full system | [[00-meta/spes/01-spes-master-operations-manual]] |
| Create custom components | [[02-component-library-reference]] |

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Dataview query empty | Check folder path matches exactly |
| Metadata not recognized | Verify YAML syntax (proper spacing, quotes) |
| Component not found | Ensure `type: component` in frontmatter |
| Note appears orphaned | Add 2+ wiki-links to related notes |

---

## 📋 Cheat Sheet: Copy-Paste Templates

### Minimal Prompt Template
```yaml
---
type: prompt
id: YYYYMMDDHHMMSS
status: active
version: "1.0.0"
rating: "0.0"
confidence: speculative
maturity: seedling
source: original
created: YYYY-MM-DD
modified: YYYY-MM-DD
usage-count: 0
tags: ["year/2025", "prompt-engineering"]
---
```

### Minimal Component Template
```yaml
---
type: component
id: YYYYMMDDHHMMSS
component-type: instruction
atomic-composite: atomic
domain: general
status: active
version: "1.0.0"
rating: "0.0"
confidence: speculative
maturity: seedling
source: original
created: YYYY-MM-DD
modified: YYYY-MM-DD
usage-count: 0
tags: ["year/2025", "prompt-engineering", "component-type/instruction"]
---
```

### Minimal Test Result Template
```yaml
---
type: test-result
prompt-tested: "[[prompt-name]]"
test-date: YYYY-MM-DD
test-type: functional
success: true
quality-score: 0.0
---
```

---

*Quick Start Version: 1.0.0 | Created: 2025-12-24*
*For full documentation: [[00-meta/spes/01-spes-master-operations-manual]]*
