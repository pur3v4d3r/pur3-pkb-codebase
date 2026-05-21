---
tags:
  - type/guide
  - type/reference
  - obsidian
  - automation
  - year/2025
type: guide
status: complete
---

# 🏷️ Enhanced Batch Tag Suggester - Quick Reference

## Overview

The **Enhanced Batch Tag Suggester** analyzes folders in your vault and suggests missing tags based on your comprehensive 577-tag taxonomy. It helps maintain consistent tagging across your knowledge base.

---

## Quick Start

### How to Run

1. **Open Command Palette**: `Ctrl/Cmd + P`
2. **Type**: "QuickAdd"
3. **Select**: Your batch tag suggester command
4. **Follow prompts**:
   - Select taxonomy type
   - Select folder to analyze
   - Wait for processing
   - Review generated report

---

## Available Taxonomies

### 1. PKM/PKB General
**Best for**: Knowledge management notes, MOCs, system documentation
**Tags**: PKM methodology, Obsidian plugins, workflows, note types
**Dimensions**: domains, subdomains, types, status, source, context

### 2. Cognitive Science & Psychology
**Best for**: Learning theory, cognitive processes, research notes
**Tags**: Memory systems, attention, executive function, theories
**Dimensions**: domains, subdomains, types, status, source, context, mode

### 3. Prompt Engineering & LLMs
**Best for**: AI prompts, techniques, patterns, LLM notes
**Tags**: Prompting techniques, patterns, model capabilities
**Dimensions**: domains, subdomains, types, status, maturity, complexity, validation, model

### 4. Critical Thinking & Self-Development
**Best for**: Analysis, evaluation, self-improvement notes
**Tags**: Logic, evaluation, self-regulation, learning theory
**Dimensions**: domains, subdomains, types, status, source

### 5. Cross-Domain Integration
**Best for**: Notes bridging cognitive science + PKM
**Tags**: Evidence-based PKM, spaced review, memory systems design
**Dimensions**: domains, subdomains, types, status

### 6. Books & Literature Notes
**Best for**: Book summaries, literature notes
**Tags**: Subject domains + book-specific status
**Dimensions**: domains, types, status, source

### 7. Obsidian System & Meta
**Best for**: Templates, system notes, technical documentation
**Tags**: Plugins, automation, meta
**Dimensions**: domains, subdomains, types, status, context

### 8. Projects & Tasks
**Best for**: Project notes, task management
**Tags**: Project status, priority
**Dimensions**: domains, types, status, priority

### 9. Research & Academic
**Best for**: Papers, research notes, academic content
**Tags**: Research domains, academic sources
**Dimensions**: domains, types, status, source, context

### 10. Quick Capture & Inbox
**Best for**: Unprocessed notes, inbox items
**Tags**: Minimal tagging for rapid processing
**Dimensions**: types, status, priority

---

## Tag Dimensions Explained

### Domain Tags
**Purpose**: Primary subject area
**Examples**: `#pkm`, `#cognitive-science`, `#prompt-engineering`
**Usage**: Use 1 domain tag per note

### Subdomain Tags
**Purpose**: Specific topic within domain
**Examples**: `#pkm/workflow/review`, `#working-memory`, `#prompting-technique/chain-of-thought`
**Usage**: Optional but recommended for specificity

### Type Tags
**Purpose**: Kind of note
**Examples**: `#type/permanent`, `#type/moc`, `#type/reference`, `#type/technique`
**Usage**: Always use 1 type tag

### Status Tags
**Purpose**: Development stage
**Examples**: `#status/seedling`, `#status/evergreen`, `#status/in-progress`
**Usage**: Always use 1 status tag

### Source Tags
**Purpose**: Where information came from
**Examples**: `#source/book`, `#source/paper`, `#source/original`, `#source/pur3v4d3r`
**Usage**: Use when applicable (literature notes)

### Context Tags
**Purpose**: Application context
**Examples**: `#context/theoretical`, `#context/practical`, `#context/research`
**Usage**: Optional, helps with filtering

### Mode Tags (Cognitive domain)
**Purpose**: Type of cognitive engagement
**Examples**: `#mode/analytical`, `#mode/reflective`, `#mode/practical`
**Usage**: Cognitive science notes

### Maturity Tags (Prompt Engineering domain)
**Purpose**: Technique maturity
**Examples**: `#maturity/emerging`, `#maturity/established`, `#maturity/standard`
**Usage**: Prompt engineering notes

### Complexity Tags (Prompt Engineering domain)
**Purpose**: Skill level required
**Examples**: `#complexity/basic`, `#complexity/advanced`, `#complexity/expert`
**Usage**: Prompt engineering notes

### Model Tags (Prompt Engineering domain)
**Purpose**: Which LLM models apply
**Examples**: `#model/claude`, `#model/gpt`, `#model/agnostic`
**Usage**: Prompt engineering notes

### Validation Tags (Prompt Engineering domain)
**Purpose**: Testing status
**Examples**: `#validation/tested`, `#validation/reported`, `#validation/theoretical`
**Usage**: Prompt engineering notes

---

## Generated Report Structure

The script generates a markdown report with:

### 1. Header Information
- Generation date & time
- Taxonomy used
- Folder analyzed
- Statistics summary
- Coverage percentage

### 2. Summary Statistics
- Missing domain tags count
- Missing type tags count
- Missing status tags count
- Other missing dimensions

### 3. Detailed Suggestions
For each file needing tags:
- File name (as wikilink)
- Full path
- Existing tags (if any)
- Suggested tags with options

### 4. Taxonomy Reference
Complete list of available tags in the selected taxonomy

---

## Example Workflow

### Scenario: Tagging Permanent Notes

```
1. Run script → Select "PKM/PKB General"
2. Select folder → "03-notes/01_permanent-notes"
3. Wait for processing (shows progress every 10 files)
4. Review report:
   - "tag-suggestions_03-notes-01_permanent-notes_2025-12-14.md"
5. For each suggestion:
   - Open the note
   - Add suggested tags to frontmatter
   - Save
6. Re-run to verify 100% coverage
```

### Scenario: Tagging Cognitive Science Notes

```
1. Run script → Select "Cognitive Science & Psychology"
2. Select folder → "03-notes/01_permanent-notes/01_cognitive-development"
3. Review report for:
   - Missing domain tags (#cognitive-science, #learning-theory, etc.)
   - Missing subdomain tags (#working-memory, #metacognition, etc.)
   - Missing mode tags (#mode/analytical, etc.)
4. Batch update tags using report as guide
```

### Scenario: Tagging Prompt Engineering Notes

```
1. Run script → Select "Prompt Engineering & LLMs"
2. Select folder → "02-projects/prompt-library"
3. Review report for:
   - Technique tags (#prompting-technique/*)
   - Model compatibility (#model/*)
   - Validation status (#validation/*)
   - Complexity level (#complexity/*)
4. Update based on testing and use cases
```

---

## Tips & Best Practices

### 1. Start with High-Value Folders
- Permanent notes first
- MOCs and dashboards second
- Fleeting/inbox notes last

### 2. Run Iteratively
- First pass: Add domain + type + status
- Second pass: Add subdomains and context
- Third pass: Add specialized dimensions

### 3. Use Reports as Checklists
- Print or split screen the report
- Work through suggestions systematically
- Re-run to track progress

### 4. Taxonomy Selection Strategy
**Use PKM/PKB General for**:
- System notes
- Templates
- Workflows
- MOCs

**Use Cognitive Science for**:
- Learning notes
- Memory research
- Educational content

**Use Prompt Engineering for**:
- AI prompts
- Technique documentation
- LLM experiments

**Use Cross-Domain for**:
- Integration notes
- Evidence-based PKM
- Applied cognitive science

### 5. Tag Density Guidelines
- **Simple notes**: 3-5 tags
- **Reference notes**: 5-8 tags
- **Integration notes**: 6-10 tags
- **Avoid**: More than 10 tags (over-classification)

### 6. Hierarchical Tagging Pattern
Always progress from general → specific:
```
#cognitive-science        [L1: Domain]
#memory-systems          [L3: System]
#working-memory          [L3: Specific]
#phonological-loop       [L4: Mechanism]
```

---

## Understanding Suggestions

### "needs-domain-tag"
**Meaning**: Note missing primary subject area
**Action**: Add one domain tag (#pkm, #cognitive-science, etc.)

### "needs-type-tag"
**Meaning**: Note classification missing
**Action**: Add type (#type/permanent, #type/reference, etc.)

### "needs-status-tag"
**Meaning**: Development stage unclear
**Action**: Add status (#status/evergreen, #status/seedling, etc.)

### "needs-source-tag"
**Meaning**: Has source references but no source tag
**Action**: Add source (#source/book, #source/paper, etc.)

### Specific Tag Suggestions
**Meaning**: Script detected relevant keywords
**Action**: Review suggestion and add if appropriate

---

## Report Locations

Reports saved to: `99-system/reports/`

**Naming pattern**:
`tag-suggestions_[folder-path]_[date].md`

**Example**:
`tag-suggestions_03-notes-01_permanent-notes_2025-12-14.md`

---

## Advanced Usage

### Analyzing Multiple Folders
Run script once per folder:
1. Permanent notes
2. MOCs
3. Projects
4. Library/reference

Compare coverage across folders.

### Tracking Coverage Over Time
Run monthly and compare:
- Files processed
- Coverage percentage
- Most common missing tags

### Custom Taxonomy Addition
To add custom taxonomy:
1. Edit `batch-tag-suggester.js`
2. Add new taxonomy object
3. Define dimensions
4. Add to taxonomy list

---

## Troubleshooting

### "No suggestions generated"
**Cause**: All notes properly tagged
**Solution**: ✅ Success! Your folder is fully tagged

### Script runs slowly
**Cause**: Large folder (100+ notes)
**Solution**: Normal - progress shown every 10 files

### Report not opening
**Cause**: File path issue
**Solution**: Navigate manually to `99-system/reports/`

### Tags not detected
**Cause**: Tags in wrong format (no # prefix)
**Solution**: Use `#tag-name` format in frontmatter

---

## Integration with Review System

The batch tagger complements the review system:

1. **Run batch tagger** → Identify missing tags
2. **Update tags** → Improve discoverability
3. **Run bulk review metadata** → Add review scheduling
4. **Use review dashboard** → Maintain notes

---

## Quick Command Reference

```bash
# Command Palette Commands
Ctrl/Cmd + P → "QuickAdd: [Your batch tag command]"

# Expected Folders to Analyze
- 03-notes/01_permanent-notes/*
- 04-library/*
- 02-projects/*
- 06-dashboards/

# Report Output
99-system/reports/tag-suggestions_*.md
```

---

## Tag Count Targets by Note Type

| Note Type | Recommended Tags | Example |
|-----------|------------------|---------|
| Fleeting | 2-3 | type + status + priority |
| Literature | 4-6 | domain + type + status + source |
| Permanent | 5-8 | domain + subdomain + type + status + context |
| MOC | 6-10 | domain + multiple subdomains + type + status |
| Reference | 5-7 | domain + type + status + source + context |
| Framework | 7-10 | domain + subdomains + type + status + mode |

---

## Next Steps

After running the batch tagger:

1. ✅ Review generated report
2. ✅ Update high-priority notes first
3. ✅ Batch update similar notes together
4. ✅ Re-run to verify coverage
5. ✅ Schedule weekly/monthly tag maintenance
6. ✅ Integrate with review system for ongoing maintenance

---

## Related Documentation

- **Tag Taxonomy**: [_reference-taxonomy-pur3v4d3r-tags-202511190109.md](_reference-taxonomy-pur3v4d3r-tags-202511190109.md)
- **Review System**: [05-tasks-&-reviews/IMPLEMENTATION-GUIDE.md](../../05-tasks-&-reviews/IMPLEMENTATION-GUIDE.md)
- **Bulk Metadata Update**: [bulk-update-review-metadata.js](../03-templater/01-templater-scripts/bulk-update-review-metadata.js)

---

**Last Updated**: 2025-12-14
**Script Location**: [99-system/01-quickadd/01-scripts/batch-tag-suggester.js](../01-quickadd/01-scripts/batch-tag-suggester.js)
