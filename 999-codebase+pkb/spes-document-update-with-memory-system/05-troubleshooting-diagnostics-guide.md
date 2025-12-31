---
tags:
aliases:
  - Troubleshooting Guide
  - Diagnostics
  - Problem Solving
  - System Health
status: evergreen
certainty: verified
priority: high
created: 2025-12-24
type: reference
project: prompt-engineering-templater-system
link-up: "[[999-v4d3r/__exemplar/__import/pkb+prompt-library-docs-with-memory/01-spes-master-operations-manual]]"
---

# 🔧 SPES Troubleshooting & Diagnostics Guide

> [!abstract] Problem Solving & System Maintenance
> This guide provides **diagnostic procedures, common issue resolutions, and maintenance protocols** for the SPES system. Use this when something isn't working correctly or during routine health checks.

---

## 🚨 PART I: QUICK DIAGNOSTICS

### 1.1 System Health Status Check

Run this diagnostic sequence when experiencing any issues:

```markdown
## Quick Health Check Sequence

### Step 1: Plugin Status
[ ] Dataview plugin enabled and up-to-date
[ ] Templater plugin enabled and up-to-date
[ ] QuickAdd plugin enabled (if using macros)
[ ] Meta-Bind plugin enabled (if using interactive fields)

### Step 2: Folder Structure Integrity
[ ] 02-component-library/ exists and accessible
[ ] 08-active-prompts/ exists
[ ] 00-inbox/prompt-ideas/ exists
[ ] 99-system/01-quickadd/ exists (for macros)

### Step 3: Core Query Test
Run in any note:
```dataview
LIST FROM "02-projects/_spes-sequential-prompt-engineering-system"
LIMIT 5
```
Expected: Should return 5 notes from SPES folder

### Step 4: Metadata Query Test
```dataview
TABLE type, status FROM "02-projects/_spes" WHERE type LIMIT 3
```
Expected: Should return notes with type and status fields
```

### 1.2 Common Symptoms & Quick Fixes

| Symptom | Likely Cause | Quick Fix |
|---------|--------------|-----------|
| Dataview shows no results | Path mismatch | Check exact folder path |
| Metadata not recognized | YAML syntax error | Validate frontmatter |
| Component not found | Missing type field | Add `type: component` |
| Links appear broken | Note moved/renamed | Update links manually |
| Template fails | Templater syntax | Check for unmatched tags |
| Dashboard empty | Query field names | Verify field names match schema |

---

## 📋 PART II: ISSUE CATALOG

### 2.1 Dataview Issues

#### Issue: Query Returns No Results

**Symptoms:**
- Dataview code block shows empty table/list
- "No results" message
- Query that worked before now fails

**Diagnostic Steps:**

```markdown
## Diagnose Empty Dataview Query

1. **Verify Path Exists**
   - Open file explorer in Obsidian
   - Navigate to the exact path in FROM clause
   - Confirm folder contains notes

2. **Check Path Syntax**
   - Use forward slashes: `"path/to/folder"`
   - Include quotes: `FROM "folder-name"`
   - Check for typos in folder names

3. **Test Simpler Query**
   ```dataview
   LIST FROM "02-projects"
   LIMIT 10
   ```
   If this works, problem is in filtering not path

4. **Check Field Names**
   - Field names are case-sensitive
   - Dashes vs underscores matter
   - `type` ≠ `Type` ≠ `TYPE`

5. **Validate Data Exists**
   - Open a note that should appear
   - Confirm frontmatter has expected fields
   - Check values match query filters
```

**Common Fixes:**

```markdown
## Path Issues
❌ FROM "02-component-library"
✅ FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library"

## Field Name Issues
❌ WHERE Type = "component"
✅ WHERE type = "component"

## Quote Issues
❌ WHERE status = active
✅ WHERE status = "active"

## Missing Field Filter
❌ WHERE usage-count > 5
✅ WHERE usage-count AND usage-count > 5
```

#### Issue: Query Shows Wrong Results

**Symptoms:**
- Notes appearing that shouldn't
- Notes missing that should appear
- Unexpected values in fields

**Diagnostic:**

```dataview
// Debug query - show all frontmatter from specific note
TABLE file.frontmatter
FROM "path/to/specific/note"
```

**Common Causes:**
1. **Filter Logic Error**: Using AND when OR needed (or vice versa)
2. **Type Coercion**: Number stored as string, comparison fails
3. **Null Values**: Field doesn't exist in some notes

---

### 2.2 Metadata Issues

#### Issue: Frontmatter Not Recognized

**Symptoms:**
- Fields visible in source but not queryable
- YAML shows as text instead of metadata
- Dataview treats fields as text

**Diagnostic:**

```markdown
## Check YAML Validity

1. **Verify Delimiters**
   - Must start with exactly `---` on line 1
   - Must end with exactly `---`
   - No spaces before delimiters

2. **Check Indentation**
   - Use spaces, not tabs
   - Consistent indentation levels
   - Arrays properly formatted

3. **Validate Quotes**
   - Strings with special chars need quotes
   - Version numbers need quotes: `"1.0.0"`
   - Dates can be unquoted: `2025-12-24`

4. **Test in YAML Validator**
   - Copy frontmatter to online YAML validator
   - Fix any syntax errors reported
```

**Common Syntax Errors:**

```yaml
## ❌ BROKEN EXAMPLES

# Missing end delimiter
---
type: prompt
status: active
[content starts here without closing ---]

# Tab indentation (invisible!)
---
type: prompt
	status: active  # Tab before status

# Colon in value without quotes
---
title: My Prompt: A Guide  # Colon breaks parsing
# Fix: title: "My Prompt: A Guide"

# Unquoted version number
---
version: 1.0.0  # Interpreted as number 1
# Fix: version: "1.0.0"
```

```yaml
## ✅ CORRECT EXAMPLES

---
type: prompt
id: "20251224143022"
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
aliases:
  - "My Prompt"
  - "Prompt Name"
---
```

#### Issue: Fields Have Wrong Type

**Symptoms:**
- Number comparisons fail
- Sort order unexpected
- Filters don't match

**Diagnostic:**

```dataview
TABLE typeof(rating), rating, typeof(usage-count), usage-count
FROM "08-active-prompts"
LIMIT 5
```

**Fixes:**

```yaml
## Number Fields (store WITHOUT quotes for numeric operations)
usage-count: 0
performance-score: 8.5

## BUT for version-like patterns (store WITH quotes)
version: "1.0.0"  # Semantic versioning is string
rating: "7.5"     # If you want string comparison
```

---

### 2.3 Component Issues

#### Issue: Component Not Found in Search

**Symptoms:**
- Component exists but doesn't appear in searches
- Dataview queries miss the component
- Tag searches don't find it

**Diagnostic Checklist:**

```markdown
## Component Discovery Checklist

1. **Verify Type Field**
   [ ] Frontmatter has `type: component`
   [ ] Not `type: prompt` or other value

2. **Verify Location**
   [ ] File is in 02-component-library/ folder
   [ ] Not in inbox or active prompts

3. **Verify Component-Type**
   [ ] Has `component-type: [valid value]`
   [ ] Value from: persona, instruction, constraint, format, context, example

4. **Verify Tags**
   [ ] Includes `prompt-engineering` tag
   [ ] Includes `component-type/[type]` tag
   [ ] Tags formatted correctly: `tag-name` not `Tag Name`

5. **Test Direct Query**
   ```dataview
   TABLE type, component-type
   FROM "02-component-library"
   WHERE file.name = "component-name"
   ```
```

#### Issue: Component Conflicts Not Working

**Symptoms:**
- Using conflicting components together
- No warning when selecting incompatible components

**Root Cause:**
- `conflicts-with` field not populated
- Field names misspelled
- Links not using correct format

**Fix:**

```yaml
# Ensure conflicts-with uses proper wiki-link format
conflicts-with:
  - "[[component-a]]"
  - "[[component-b]]"

# NOT these formats
conflicts-with:
  - component-a        # Missing brackets
  - "component-a"      # Missing brackets
  - [[component-a]]    # Missing quotes
```

---

### 2.4 Template Issues

#### Issue: Templater Script Fails

**Symptoms:**
- Template produces error
- Inserted content is wrong
- Variables not replaced

**Diagnostic:**

```markdown
## Template Debugging Steps

1. **Check Syntax**
   - Opening: `
   - Closing: `
   - No nested template tags

2. **Check Variable Names**
   - `tp.date.now()` not `tp.date.Now()`
   - `tp.file.title` not `tp.file.name` (different!)

3. **Check Async Operations**
   - Suggester: `await tp.system.suggester()`
   - Prompt: `await tp.system.prompt()`
   - Missing await = undefined

4. **Enable Debug Mode**
   - Templater settings → Debug
   - Check console for errors
```

**Common Template Errors:**

```javascript
// ❌ Missing await
const choice = tp.system.suggester(["A", "B"], ["a", "b"]);
// Returns Promise, not value

// ✅ With await
const choice = await tp.system.suggester(["A", "B"], ["a", "b"]);

// ❌ Wrong function name
tp.date.today("YYYY-MM-DD")
// No such function

// ✅ Correct function
tp.date.now("YYYY-MM-DD")

// ❌ Typo in property
tp.file.titel
// Undefined

// ✅ Correct property
tp.file.title
```

---

### 2.5 Link Issues

#### Issue: Broken Wiki-Links

**Symptoms:**
- Links appear grayed out
- "Create note" prompt appears
- Graph shows orphan nodes

**Diagnostic:**

```markdown
## Find Broken Links

### Method 1: Obsidian Core
- Settings → Files & Links → Check for broken links
- Or use link-checking community plugin

### Method 2: Manual Search
Search for: `[[` and review suggested completions
Links without autocomplete suggestions may be broken

### Method 3: Dataview Query
```dataview
LIST file.outlinks
FROM "02-projects/_spes"
WHERE any(file.outlinks, (l) => !dv.page(l))
```
```

**Common Causes:**
1. **Note Renamed**: Link points to old name
2. **Note Deleted**: Referenced note no longer exists
3. **Typo in Link**: Spelling error in target name
4. **Case Sensitivity**: Some systems are case-sensitive

**Fixes:**
1. Use "Update links on rename" setting
2. Create placeholder note if needed
3. Use link autocomplete to verify targets
4. Run link check after bulk operations

#### Issue: Orphan Notes

**Symptoms:**
- Notes with no incoming links
- Notes with no outgoing links
- Graph shows disconnected nodes

**Detection Query:**

```dataview
TABLE length(file.inlinks) as "Inlinks", length(file.outlinks) as "Outlinks"
FROM "02-projects/_spes"
WHERE length(file.inlinks) = 0 OR length(file.outlinks) < 2
```

**Resolution Protocol:**

```markdown
## Fix Orphan Notes

For each orphan:

1. **Add Outgoing Links (minimum 2)**
   - Link to related concepts
   - Link to parent MOC
   - Link to prerequisite or extension topics

2. **Create Incoming Links**
   - Add to relevant MOC
   - Link from related notes
   - Add to link-related field of connected notes

3. **Update Metadata**
   - Add link-up field pointing to parent
   - Update link-related array

4. **Verify Fix**
   - Re-run orphan query
   - Check graph view for connections
```

---

## 🔄 PART III: MAINTENANCE PROCEDURES

### 3.1 Daily Maintenance

```markdown
## Daily SPES Health Check (5 minutes)

### Quick Scan
- [ ] Review inbox for new captures
- [ ] Check dashboard for alerts
- [ ] Note any issues encountered today

### Quick Query Check
Run this to spot obvious problems:
```dataview
TABLE status, maturity
FROM "02-projects/_spes"
WHERE type = "prompt" AND status != "archived"
SORT modified DESC
LIMIT 10
```

### Capture Processing
- [ ] Process inbox items (develop or delete)
- [ ] Update any in-progress prompts
```

### 3.2 Weekly Maintenance

```markdown
## Weekly SPES Health Check (30 minutes)

### Metadata Audit
```dataview
TABLE type, status, confidence
FROM "02-projects/_spes"
WHERE !type OR !status OR !confidence
```
Fix any notes with missing required fields.

### Orphan Check
```dataview
LIST
FROM "02-projects/_spes"
WHERE length(file.inlinks) = 0 AND length(file.outlinks) = 0
```
Connect or archive orphan notes.

### Review Queue
```dataview
TABLE maturity, review-next
FROM "02-projects/_spes"
WHERE type = "prompt" AND review-next <= date(today)
SORT review-next ASC
```
Process overdue reviews.

### Component Health
```dataview
TABLE component-type, usage-count, performance-score
FROM "02-component-library"
WHERE type = "component"
SORT usage-count ASC
LIMIT 10
```
Identify underused components - consider deprecation or promotion.

### Link Integrity
- [ ] Run link checker
- [ ] Fix any broken links
- [ ] Update outdated links
```

### 3.3 Monthly Maintenance

```markdown
## Monthly SPES Health Check (2 hours)

### Comprehensive Metadata Audit
```dataview
TABLE 
  choice(!type, "MISSING TYPE", "✓") as "Type",
  choice(!status, "MISSING", "✓") as "Status",
  choice(!version, "MISSING", "✓") as "Version",
  choice(!tags, "MISSING", "✓") as "Tags",
  choice(!created, "MISSING", "✓") as "Created"
FROM "02-projects/_spes"
```
Target: 100% compliance on required fields.

### Usage Analytics Review
```dataview
TABLE type, sum(rows.usage-count) as "Total Uses"
FROM "02-projects/_spes"
GROUP BY type
```
Review which note types getting most use.

### Performance Analysis
```dataview
TABLE 
  round(average(rows.rating), 1) as "Avg Rating",
  sum(rows.usage-count) as "Total Uses"
FROM "02-projects/_spes"
WHERE type = "component"
GROUP BY component-type
```
Identify high/low performing component categories.

### Archive Candidates
```dataview
LIST
FROM "02-projects/_spes"
WHERE status = "deprecated" OR 
  (usage-count = 0 AND created < date(today) - dur(90 days))
```
Move to archive.

### Documentation Review
- [ ] Review MOCs for accuracy
- [ ] Update dashboards if queries changed
- [ ] Verify templates still work
- [ ] Check for documentation gaps

### System Improvements
- [ ] Identify optimization opportunities
- [ ] Note new patterns to document
- [ ] Plan component additions
- [ ] Schedule any needed refactoring
```

---

## 📊 PART IV: DIAGNOSTIC QUERIES

### 4.1 System Overview Queries

**Total System Inventory:**
```dataview
TABLE type, COUNT(file.name) as "Count"
FROM "02-projects/_spes"
GROUP BY type
```

**Status Distribution:**
```dataview
TABLE status, COUNT(file.name) as "Count"
FROM "02-projects/_spes"
GROUP BY status
```

**Maturity Distribution:**
```dataview
TABLE maturity, COUNT(file.name) as "Count"
FROM "02-projects/_spes"
WHERE type = "prompt" OR type = "component"
GROUP BY maturity
```

### 4.2 Quality Queries

**Low Confidence Items:**
```dataview
TABLE type, confidence, created
FROM "02-projects/_spes"
WHERE confidence = "speculative"
SORT created DESC
```

**High Rating Items:**
```dataview
TABLE type, rating, usage-count
FROM "02-projects/_spes"
WHERE rating >= 8.0
SORT rating DESC
```

**Never Used Components:**
```dataview
TABLE component-type, domain, created
FROM "02-component-library"
WHERE usage-count = 0
SORT created ASC
```

### 4.3 Health Queries

**Metadata Completeness:**
```dataview
TABLE 
  file.name,
  choice(type, "✓", "✗") as "type",
  choice(status, "✓", "✗") as "status",
  choice(version, "✓", "✗") as "version",
  choice(tags, "✓", "✗") as "tags"
FROM "02-projects/_spes"
WHERE !type OR !status OR !version OR !tags
```

**Old Seedlings (Stalled Development):**
```dataview
TABLE type, created, modified
FROM "02-projects/_spes"
WHERE maturity = "seedling" AND created < date(today) - dur(30 days)
SORT created ASC
```

**Recently Modified:**
```dataview
TABLE type, status, modified
FROM "02-projects/_spes"
WHERE modified >= date(today) - dur(7 days)
SORT modified DESC
```

---

## 🆘 PART V: EMERGENCY PROCEDURES

### 5.1 Corrupted Frontmatter Recovery

**Symptoms:**
- Note content shifted into metadata area
- YAML parsing completely fails
- Note appears empty

**Recovery:**

```markdown
## Frontmatter Recovery Steps

1. **Backup Current State**
   - Copy entire note content to clipboard
   - Save as separate file outside vault

2. **Extract Content**
   - Open note in external text editor
   - Identify where real content begins
   - Copy content portion

3. **Rebuild Note**
   - Create new note with fresh template
   - Paste content into body
   - Manually populate frontmatter

4. **Verify Links**
   - Check incoming links still work
   - Fix any broken backlinks
```

### 5.2 Mass Update Recovery

**If bulk update goes wrong:**

```markdown
## Bulk Update Recovery

1. **Stop Immediately**
   - Don't run additional commands
   - Note what was changed

2. **Check Git Status**
   ```bash
   git status
   git diff
   ```

3. **Selective Revert**
   ```bash
   git checkout -- path/to/specific/file.md
   ```

4. **Full Revert (if needed)**
   ```bash
   git checkout HEAD~1 -- path/to/folder/
   ```

5. **Verify Recovery**
   - Run health check queries
   - Spot check several notes
```

### 5.3 Complete System Restore

**When all else fails:**

```markdown
## Full System Restore

1. **Identify Last Good State**
   - Check git log for good commit
   - Or identify backup timestamp

2. **Backup Current State**
   - Even if broken, keep copy
   - May need to recover specific items

3. **Restore from Backup**
   - Git: `git checkout [commit-hash]`
   - File backup: Replace folder contents

4. **Run Full Health Check**
   - All diagnostic queries
   - Plugin functionality test
   - Template test

5. **Document Incident**
   - What went wrong
   - How it was fixed
   - Prevention measures
```

---

## 🔗 Related Topics for PKB Expansion

### 1. **[[Obsidian Plugin Troubleshooting]]**
- *Connection*: Plugin-specific issues beyond SPES
- *Priority*: High - Foundation for system operation

### 2. **[[Git Version Control for Obsidian]]**
- *Connection*: Backup and recovery procedures
- *Priority*: High - Data protection

### 3. **[[Dataview Query Optimization]]**
- *Connection*: Performance when queries slow down
- *Priority*: Medium - System performance

### 4. **[[Automated Health Monitoring]]**
- *Connection*: Proactive issue detection
- *Priority*: Medium - Preventive maintenance

---

*Guide Version: 1.0.0 | Created: 2025-12-24 | Status: Production Ready*
*Authoritative Reference for SPES Troubleshooting & Maintenance*
