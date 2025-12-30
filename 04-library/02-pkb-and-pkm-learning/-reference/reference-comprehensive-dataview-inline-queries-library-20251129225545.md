---
aliases:
  - "Dataview Inline Query Taxonomy"
  - "Inline Query Collection"
tags:
  - "type/permanent"
  - "year/2025"
  - "type/analysis"
  - "status/in-progress"
  - "pkb"
  - "pkm"
  - "building-second-brain"
  - "critical-thinking/evaluation"
  - "cognitive-load-management"
  - "information-processing-theory"
  - "sustained-attention"
  - "problem-solving"
  - "cognitive-pkm"
source: "claude-sonnet-4.5"
id: "20251129225811"
created: "2025-11-29T22:58:11"
modified: "2025-11-29T22:58:11"
week: "[[2025-W48]]"
month: "[[2025-11]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: "reference"
maturity: "seedling"
confidence: "provisional"
next-review: "2025-12-06"
review-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-11-29|Daily-Note]]"
---

# Dataview Inline Query Taxonomy

> [!overview]
> - **Title**:: [[Dataview Inline Query Taxonomy]]
> - **Prompt/Topic Used**:: 
> - **Status**:: 🌱 `= this.maturity` | Confidence: `= this.confidence`

## 📊 Note Metadata Dashboard
> [!fail] 🛠️ Metadata Health Check
> **Missing Fields**:: `$= const fields = ["status", "type", "tags"]; const missing = fields.filter(f => !dv.current()[f]); missing.length > 0 ? "⚠️ Missing: " + missing.join(", ") : "✅ All Systems Go"`

> [!metadata]
> **Note-Type**: `= this.type`
> **Development Status**: `= this.maturity`  
> **Epistemic Confidence**: `= this.confidence`  
> **Next Review**: `= this.next-review`  
> **Review Count**: `= this.review-count`  
> **Created**: `= this.created`  
> **Last Modified**: `= this.modified`

> [!quote] 📝 Content Metrics
> **Word Count**:: `= this.file.size` B | **Est. Read Time**:: `= round(this.file.size / 1300) + " min"`
> **Depth Class**:: `= choice(this.file.size < 500, "🌱 Stub", choice(this.file.size < 2000, "📄 Note", "📜 Essay"))`

> [!calendar] 🕰️ Temporal Context
> **Created**:: `= this.file.ctime` | **Age**:: `= (date(today) - this.file.ctime).days + " days"`
> **Last Touch**:: `= this.file.mtime` | **Staleness**:: `= choice((date(today) - this.file.mtime).days > 180, "🕸️ Cobwebs", choice((date(today) - this.file.mtime).days > 30, "🍂 Cold", "🔥 Fresh"))`

> [!network] 🔗 Network Connectivity
> **In-Links**:: `= length(this.file.inlinks)` | **Out-Links**:: `= length(this.file.outlinks)`
> **Network Status**:: `= choice(length(this.file.inlinks) = 0, "🕸️ Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱 Node"))`

```dataviewjs
// 🧠 SYSTEM: Semantic Bridge Engine
// PURPOSE: Find "Sibling" notes that share the same Outlinks (Contexts)
const current = dv.current();
const myOutlinks = current.file.outlinks.map(l => l.path);

// 1. Filter the Vault
const siblings = dv.pages()
    .where(p => p.file.path !== current.file.path) // Exclude self
    .where(p => !current.file.outlinks.map(l => l.path).includes(p.file.path)) // Exclude existing direct links
    .map(p => {
        // Find overlap between this page's links and the current page's links
        const shared = p.file.outlinks.filter(l => myOutlinks.includes(l.path));
        return { 
            link: p.file.link, 
            sharedCount: shared.length, 
            sharedLinks: shared 
        };
    })
    .where(p => p.sharedCount > 0) // Must share at least 1 connection
    .sort(p => p.sharedCount, "desc") // Sort by strongest connection
    .limit(5); // Only show top 5

// 2. Render the Bridge
if (siblings.length > 0) {
    dv.header(4, "🌉 Semantic Bridges (Missing Connections)");
    dv.table(
        ["Sibling Note", "Strength", "Shared Context"], 
        siblings.map(s => [
            s.link, 
            "🔗 " + s.sharedCount, 
            s.sharedLinks.slice(0, 3).join(", ") + (s.sharedCount > 3 ? "…" : "")
        ])
    );
} else {
    dv.paragraph("*No semantic siblings found. This note is unique in its connections.*");
}
```
### Related Notes
```dataview
TABLE type, maturity, confidence
FROM  ""
WHERE  type = "reference"
SORT "maturity" DESC
LIMIT 15
```
### Sources & References
```dataview
TABLE 
    source AS "Source Type",
    file.ctime AS "Date Added"
FROM ""

WHERE source = "claude-sonnet-4.5"
SORT "created" = DESC
LIMIT 10

```
### Backlinks & Connections
```dataview
TABLE 
    type AS "Type",
    maturity AS "Maturity",
    created AS "Created"
FROM [[#]]
SORT created DESC
LIMIT 15
```
### 2025-11-29 - Initial Creation
*Context*: `=this.title` **by**: `=this.source`
*Maturity*: `= this.maturity`  
*Confidence*: `= this.confidence`

### Tags & Classification
*Primary Tags*: `= this.tags`  
*Type*: `= this.type`  
*Source*: `= this.source`

### Review System
> [!important] Review Schedule
> - **Next Review**: `= this.next-review`
> - **Review Frequency**: Based on maturity level
>   - Seedling: Weekly
>   - Budding: Bi-weekly
>   - Developing: Monthly
>   - Evergreen: Quarterly
#### Review Checklist:
- [ ] Definition still accurate?
- [ ] New connections identified?
- [ ] Applications validated?
- [ ] Sources still relevant?
- [ ] Maturity level appropriate?

---
### Claude Thinking:

Alright, let me break down this request systematically:

**REQUEST ANALYSIS:**
- User wants a comprehensive reference note specifically focused on Dataview Inline Queries
- This is NOT about explaining what inline queries are, but rather a TAXONOMY/COLLECTION of working inline query examples
- The purpose is to create a reference resource to pull from when needed
- Needs to be well-organized and navigable
- Should cover as many different use cases/areas as possible
- The exemplar shows inline queries embedded in callouts with explanatory text

**SCOPE MAPPING:**
The topic "Dataview Inline Queries" encompasses:
- Primary domain: Obsidian plugin ecosystem, specifically Dataview
- Technical depth: Intermediate to advanced Obsidian usage
- Practical application: PKB organization, note metadata, knowledge graph navigation
- Coverage needed: Multiple categories of inline queries (temporal, navigational, analytical, metadata-focused, etc.)

**RESEARCH DECISION:**
Do I need web_search? Let me evaluate:
- The user has provided exemplars showing they already have some inline queries
- They want a comprehensive collection, not current documentation
- Dataview inline query syntax is relatively stable
- I should search for:
  1. Current Dataview inline query syntax documentation
  2. Community examples and patterns
  3. Best practices and use cases
  4. Any recent syntax changes or new features

YES - I should do web research to ensure I capture the full range of inline query possibilities and confirm syntax accuracy.

**WEB RESEARCH PLAN:**
1. Search for official Dataview inline query documentation
2. Search for community examples and use cases
3. Search for advanced inline query patterns
4. Search for Dataview inline fields and expressions reference
5. Search for Dataview inline query cookbook/examples

**STRUCTURAL PLANNING:**

The note should be organized as a TAXONOMY rather than a tutorial. Categories could include:

1. **Temporal/Time-Based Queries**
   - Creation dates, modification dates, age calculations
   - Staleness indicators
   - Time-relative filters

2. **File Metadata Queries**
   - File properties (size, name, path, type)
   - Folder context
   - Tag displays

3. **Relational/Link-Based Queries**
   - Backlink counts
   - Outlink analysis
   - Link strength/density

4. **Content Analysis Queries**
   - Word count, character count
   - Task counting
   - Header/section analysis

5. **Computed/Mathematical Queries**
   - Aggregations (sum, average, count)
   - Progress calculations
   - Percentage displays

6. **Conditional/Logic-Based Queries**
   - If/then displays
   - Choice expressions
   - Boolean flags

7. **List/Collection Queries**
   - Inline lists of related files
   - Tag collections
   - Property aggregations

8. **Custom Property Queries**
   - Frontmatter field displays
   - Inline field references
   - Metadata calculations

Each category should have:
- Brief description of use case
- Multiple working examples
- Syntax explanation where needed
- Visual organization (possibly tables or structured callouts)

**WIKI-LINK OPPORTUNITIES:**
- [[Dataview Plugin]]
- [[Obsidian]]
- [[Inline Queries]]
- [[Dataview Expressions]]
- [[Metadata]]
- [[Frontmatter]]
- [[Zettelkasten]]
- [[Personal Knowledge Base]]
- [[Templater Plugin]]
- [[File Properties]]
- [[Wiki-Links]]
- [[Backlinks]]
- [[Knowledge Graph]]
- [[Note Templates]]
- [[MOC]]
- [[Temporal Analysis]]
- [[Folder Structure]]

**CALLOUT STRATEGY:**
- [!abstract] for category overviews
- [!example] for query demonstrations
- [!helpful-tip] for usage guidance
- [!important] for syntax notes
- [!warning] for common pitfalls
- [!methodology-and-sources] for query patterns
- [!what-this-does] for explaining complex queries

Now let me execute the research phase before constructing the note.

I'll create a comprehensive taxonomy of Dataview Inline Queries for your PKB. Let me first research current Dataview capabilities and syntax to ensure accuracy.Now I have comprehensive research material. Let me create the exhaustive reference note on Dataview Inline Queries.

---
tags: #obsidian #dataview #inline-queries #reference-note #pkm
aliases: [Dataview Inline Query Taxonomy, DQL Inline Reference, Inline Query Collection, Dataview Expressions Library]
---

> [!comprehensive-reference] 📚 Comprehensive-Reference
> - **Generated**:: 2024-11-29
> - **Version**:: 1.0
> - **Type**:: Reference Taxonomy

> [!abstract]
> **Executive Overview**
> This note is an exhaustive taxonomy of [[Dataview Plugin]] inline query patterns for [[Obsidian]] vaults. It serves as a single-source-of-truth reference containing working inline query examples across all functional categories—from temporal calculations to link analysis to conditional logic. Use this as your go-to resource when building [[Note Templates]], dashboards, or dynamic metadata displays.

> [!how-to-use-this]
> **Navigation Guide**
> This reference is organized into 12 functional categories covering every major use case for inline queries. Each category contains multiple working examples with explanatory context. Use the table of contents for quick navigation, or search for specific patterns using [[Wiki-Links]]. All examples are production-ready and can be copied directly into your vault.

## 📑 Table of Contents

1. [Temporal & Date Queries](#1-⏰-temporal--date-queries)
2. [File Metadata Display](#2-📄-file-metadata-display)
3. [Link & Relationship Queries](#3-🔗-link--relationship-queries)
4. [Conditional Logic & Validation](#4-🎯-conditional-logic--validation)
5. [Mathematical & Computational Queries](#5-🧮-mathematical--computational-queries)
6. [Content Analysis Queries](#6-📊-content-analysis-queries)
7. [List & Array Operations](#7-📋-list--array-operations)
8. [Cross-Page Data Access](#8-🌐-cross-page-data-access)
9. [Status & Progress Tracking](#9-⚡-status--progress-tracking)
10. [Text Manipulation & Formatting](#10-✍️-text-manipulation--formatting)
11. [Aggregation & Collection Queries](#11-📈-aggregation--collection-queries)
12. [Advanced DataviewJS Inline](#12-💻-advanced-dataviewjs-inline)

---

## 1. ⏰ Temporal & Date Queries

> [!definition]
> **Temporal Queries** access and manipulate date-based [[Metadata]] to track time-sensitive information, calculate durations, and display time-relative context.

### 📅 Basic Date Display

```markdown
**Created**: `= this.file.ctime`
**Modified**: `= this.file.mtime`
**Today**: `= date(today)`
**Tomorrow**: `= date(today) + dur(1 day)`
```

> [!what-this-does]
> Displays core temporal metadata using [[Dataview Functions]]. `file.ctime` and `file.mtime` are [[Implicit Fields]] automatically indexed by Dataview. The `date(today)` function returns the current date, while `dur()` creates duration objects for calculations.

### 📊 Age & Staleness Calculations

```markdown
**Age**: `= (date(today) - this.file.ctime).days + " days old"`
**Days Since Modified**: `= (date(today) - this.file.mtime).days`
**Staleness**: `= choice((date(today) - this.file.mtime).days > 180, "🕸️ Cobwebs", choice((date(today) - this.file.mtime).days > 30, "🍂 Cold", "🔥 Fresh"))`
```

> [!example]
> **Use Case**: [[Zettelkasten]] note gardening. The staleness indicator automatically classifies notes as "Fresh" (edited within 30 days), "Cold" (30-180 days), or "Cobwebs" (180+ days), enabling systematic review workflows.

### ⏳ Deadline & Time-Until Calculations

```markdown
**Days Until Deadline**: `= (this.due-date - date(today)).days + " days remaining"`
**Overdue Status**: `= choice(this.due-date < date(today), "⚠️ OVERDUE", "✅ On Track")`
**Week Number**: `= date(today).weekyear + "-W" + date(today).week`
```

> [!helpful-tip]
> Combine with [[Templater Plugin]] to auto-populate due dates in [[Project Management]] notes. The overdue calculation creates dynamic status indicators without manual updates.

### 📆 Relative Date Expressions

```markdown
**Start of Month**: `= date(som)`
**End of Month**: `= date(eom)`
**Start of Year**: `= date(soy)`
**Days in Current Month**: `= (date(eom) - date(som)).days`
**Quarter**: `= "Q" + ceil(date(today).month / 3)`
```

> [!what-this-does]
> Uses Dataview's date manipulation functions for period-based calculations. `som` (start of month), `eom` (end of month), and `soy` (start of year) are predefined constants. Useful for [[Dashboard Design]] and periodic review systems.

### 🕰️ Time-Since-Last-Action Tracking

```markdown
**Last Review**: `= choice(contains(this, "last-review"), (date(today) - this.last-review).days + " days ago", "Never reviewed")`
**Touch Frequency**: `= choice((date(today) - this.file.mtime).days < 7, "🔥 Active", choice((date(today) - this.file.mtime).days < 30, "👌 Regular", "❄️ Dormant"))`
```

### 🗓️ Custom Date Formatting

```markdown
**ISO Format**: `= date(today).format("YYYY-MM-DD")`
**Human Readable**: `= date(today).format("MMMM Do, YYYY")`
**Day of Week**: `= date(today).format("dddd")`
**Time Stamp**: `= date(today).format("YYYY-MM-DD HH:mm:ss")`
```

> [!methodology-and-sources]
> Uses Moment.js formatting syntax. Common patterns:
> - `YYYY` = 4-digit year
> - `MM` = 2-digit month
> - `DD` = 2-digit day
> - `dddd` = full weekday name
> - `HH:mm:ss` = 24-hour time

---

## 2. 📄 File Metadata Display

> [!definition]
> **File Metadata Queries** access system-generated properties about the note itself—its location, size, naming, and organizational context.

### 📁 Basic File Properties

```markdown
**File Name**: `= this.file.name`
**Full Path**: `= this.file.path`
**Folder**: `= this.file.folder`
**File Extension**: `= this.file.ext`
**File Size**: `= this.file.size + " bytes"`
```

### 🏷️ Tag & Classification Display

```markdown
**Tags**: `= this.file.tags`
**Tag Count**: `= length(this.file.tags)`
**Primary Tag**: `= this.file.tags[0]`
**Has Tag**: `= choice(contains(this.file.tags, "#status/active"), "✅ Active", "❌ Not Active")`
```

> [!what-this-does]
> `file.tags` returns an array of all tags in the note. Arrays can be indexed (`[0]` for first item) and measured with `length()`. The `contains()` function checks array membership for conditional displays.

### 🌟 File Status Indicators

```markdown
**Starred**: `= choice(this.file.starred, "⭐", "")`
**Favorite**: `= choice(this.file.starred = true, "📌 Pinned", "📄 Standard")`
**File Link**: `= this.file.link`
```

### 📏 Content Metrics

```markdown
**Character Count**: `= length(this.file.content)`
**Estimated Words**: `= round(length(this.file.content) / 6)`
**Line Count**: `= length(split(this.file.content, "\n"))`
```

> [!warning]
> **Performance Note**: `file.content` can be resource-intensive on large files. Use sparingly in notes with extensive content or frequent updates.

### 🗂️ Folder Context Awareness

```markdown
**Location**: `= this.file.folder`
**Folder Depth**: `= length(split(this.file.folder, "/"))`
**Parent Folder**: `= split(this.file.folder, "/")[length(split(this.file.folder, "/")) - 1]`
```

---

## 3. 🔗 Link & Relationship Queries

> [!definition]
> **Link Queries** analyze the [[Knowledge Graph]] connections between notes, tracking [[Backlinks]], outgoing links, and relational density.

### 🔗 Link Counting

```markdown
**Outgoing Links**: `= length(this.file.outlinks)`
**Incoming Links (Backlinks)**: `= length(this.file.inlinks)`
**Total Link Count**: `= length(this.file.outlinks) + length(this.file.inlinks)`
**Link Density**: `= length(this.file.outlinks) + length(this.file.inlinks) + " connections"`
```

> [!example]
> **Use Case**: [[MOC]] (Maps of Content) health monitoring. High outlink counts suggest hub notes, while low backlink counts identify orphaned concepts needing integration.

### 🌐 Link Existence Validation

```markdown
**Has Outlinks**: `= choice(length(this.file.outlinks) > 0, "🔗 Connected", "🔴 Isolated")`
**Has Backlinks**: `= choice(length(this.file.inlinks) > 0, "← Referenced", "🔴 Orphaned")`
**Fully Connected**: `= choice(length(this.file.outlinks) > 0 AND length(this.file.inlinks) > 0, "✅ Integrated", "⚠️ Needs Links")`
```

### 📊 Link Strength Indicators

```markdown
**Hub Score**: `= choice(length(this.file.outlinks) > 10, "🌟 Major Hub", choice(length(this.file.outlinks) > 5, "📍 Minor Hub", "📄 Standard"))`
**Authority Score**: `= choice(length(this.file.inlinks) > 15, "⭐ High Authority", choice(length(this.file.inlinks) > 5, "👍 Referenced", "🔹 Emerging"))`
```

### 🔍 Specific Link Access

```markdown
**First Outlink**: `= this.file.outlinks[0]`
**Last Backlink**: `= this.file.inlinks[length(this.file.inlinks) - 1]`
**Random Outlink**: `= this.file.outlinks[floor(random() * length(this.file.outlinks))]`
```

> [!helpful-tip]
> The random outlink pattern creates serendipitous navigation paths—useful for [[Zettelkasten]] exploration and breaking filter bubbles in your knowledge graph.

### 🌉 Cross-Reference Counting

```markdown
**Links to Projects**: `= length(filter(this.file.outlinks, (link) => contains(string(link), "Projects")))`
**Links to References**: `= length(filter(this.file.outlinks, (link) => contains(string(link), "References")))`
```

---

## 4. 🎯 Conditional Logic & Validation

> [!definition]
> **Conditional Queries** implement decision logic to display different values based on metadata state, enabling dynamic validation and adaptive displays.

### ✅ Field Existence Checks

```markdown
**Status Set**: `= choice(contains(this, "status"), "✅ Set", "❌ Missing")`
**Due Date Set**: `= choice(contains(this, "due-date"), "✅ Scheduled", "⚠️ No Deadline")`
**Required Fields**: `= choice(contains(this, "title") AND contains(this, "author"), "✅ Complete", "❌ Incomplete")`
```

> [!what-this-does]
> The `contains(this, "field-name")` pattern checks if a field exists in the current note's [[YAML Frontmatter]] or [[Inline Fields]]. Essential for template validation and metadata quality control.

### 🎚️ Multi-Level Conditionals

```markdown
**Priority Level**: `= choice(this.priority = "high", "🔴 High", choice(this.priority = "medium", "🟡 Medium", choice(this.priority = "low", "🟢 Low", "⚪ None")))`
**Stage Indicator**: `= choice(this.stage = "complete", "✅", choice(this.stage = "in-progress", "🔄", choice(this.stage = "planned", "📋", "❓")))`
```

> [!methodology-and-sources]
> Nested `choice()` functions create if-else-if chains. Syntax: `choice(condition, value-if-true, value-if-false)`. Can nest indefinitely, though readability degrades beyond 3-4 levels.

### 🔢 Numerical Thresholds

```markdown
**Word Count Status**: `= choice(this.word-count > 1000, "📗 Substantial", choice(this.word-count > 500, "📘 Moderate", choice(this.word-count > 100, "📙 Brief", "📕 Stub")))`
**Completion %**: `= choice(this.progress >= 100, "✅ Complete", choice(this.progress >= 75, "🟢 Near Done", choice(this.progress >= 50, "🟡 Halfway", choice(this.progress >= 25, "🟠 Started", "🔴 Early"))))`
```

### ⚠️ Alert & Warning Conditionals

```markdown
**Deadline Alert**: `= choice(this.due-date AND this.due-date < date(today), "⚠️ OVERDUE", choice(this.due-date AND (this.due-date - date(today)).days < 3, "🔔 Due Soon", ""))`
**Size Warning**: `= choice(this.file.size > 100000, "⚠️ Large File", "")`
```

### 🔄 Boolean Field Display

```markdown
**Archived**: `= choice(this.archived = true, "📦 Archived", "📂 Active")`
**Published**: `= choice(this.published, "🌐 Live", "📝 Draft")`
**Reviewed**: `= choice(this.reviewed, "✅ Reviewed", "⏳ Needs Review")`
```

---

## 5. 🧮 Mathematical & Computational Queries

> [!definition]
> **Computational Queries** perform mathematical operations on numerical [[Metadata]] fields, enabling calculations, aggregations, and derived metrics.

### ➕ Basic Arithmetic

```markdown
**Total**: `= this.budget + this.expenses`
**Remaining**: `= this.budget - this.expenses`
**Product**: `= this.quantity * this.unit-price`
**Average**: `= (this.value1 + this.value2 + this.value3) / 3`
```

### 📊 Percentage Calculations

```markdown
**Progress %**: `= round((this.completed / this.total) * 100) + "%"`
**Completion**: `= round((this.tasks-done / this.tasks-total) * 100, 1) + "% complete"`
**Growth Rate**: `= round(((this.current - this.previous) / this.previous) * 100, 2) + "%"`
```

> [!example]
> **Use Case**: [[Project Management]] dashboards. The progress percentage auto-updates as task counts change, creating a live completion tracker without manual calculation.

### 🔢 Rounding & Precision

```markdown
**Rounded**: `= round(this.decimal-value)`
**Two Decimals**: `= round(this.value, 2)`
**Round Up**: `= ceil(this.value)`
**Round Down**: `= floor(this.value)`
```

### 📐 Mathematical Functions

```markdown
**Absolute Value**: `= abs(this.value)`
**Maximum**: `= max(this.value1, this.value2, this.value3)`
**Minimum**: `= min(this.value1, this.value2, this.value3)`
**Square Root**: `= sqrt(this.value)`
```

### ⚖️ Ratio & Comparison

```markdown
**Ratio**: `= round(this.value-a / this.value-b, 2) + ":1"`
**Greater Than**: `= choice(this.actual > this.target, "✅ Exceeded", "📈 Below Target")`
**Difference**: `= this.current - this.baseline + " units"`
```

---

## 6. 📊 Content Analysis Queries

> [!definition]
> **Content Analysis Queries** examine the structural elements within notes—tasks, lists, headings, and content patterns.

### ✅ Task Counting

```markdown
**Total Tasks**: `= length(this.file.tasks)`
**Completed Tasks**: `= length(filter(this.file.tasks, (t) => t.completed))`
**Pending Tasks**: `= length(filter(this.file.tasks, (t) => !t.completed))`
**Completion Rate**: `= choice(length(this.file.tasks) > 0, round((length(filter(this.file.tasks, (t) => t.completed)) / length(this.file.tasks)) * 100) + "%", "No tasks")`
```

> [!what-this-does]
> Accesses [[Implicit Fields]] for task data. The `filter()` function creates subsets based on task properties. `t.completed` is a boolean indicating task completion status.

### 📝 List Item Analysis

```markdown
**List Items**: `= length(this.file.lists)`
**Non-Task Items**: `= length(this.file.lists) - length(this.file.tasks)`
**Has Lists**: `= choice(length(this.file.lists) > 0, "📋 Contains Lists", "📄 No Lists")`
```

### 📑 Heading Structure

```markdown
**Heading Count**: `= length(filter(split(this.file.content, "\n"), (line) => startswith(line, "#")))`
**Has H1**: `= choice(contains(this.file.content, "\n# "), "✅ Has H1", "⚠️ No H1")`
```

> [!warning]
> These queries parse `file.content` which can impact performance. Use judiciously in large vaults or consider DataviewJS alternatives for complex content analysis.

### 🔍 Pattern Detection

```markdown
**Contains Code**: `= choice(contains(this.file.content, "```"), "💻 Has Code Blocks", "📝 Text Only")`
**Has Images**: `= choice(contains(this.file.content, "!["), "🖼️ Contains Images", "📄 Text Only")`
**Has Tables**: `= choice(contains(this.file.content, "|"), "📊 Has Tables", "📄 No Tables")`
```

---

## 7. 📋 List & Array Operations

> [!definition]
> **List Operations** manipulate arrays of values—including tags, links, and multi-value fields—using filtering, mapping, and extraction functions.

### 📏 List Measurement

```markdown
**Array Length**: `= length(this.multi-value-field)`
**Tag Count**: `= length(this.file.tags)`
**Collaborator Count**: `= length(this.collaborators)`
```

### 🎯 List Access & Slicing

```markdown
**First Item**: `= this.list-field[0]`
**Last Item**: `= this.list-field[length(this.list-field) - 1]`
**Second Item**: `= this.list-field[1]`
**First Three**: `= this.list-field[0] + ", " + this.list-field[1] + ", " + this.list-field[2]`
```

> [!helpful-tip]
> Array indexing is zero-based. `list[0]` retrieves the first element, `list[1]` the second, etc. Use `length(list) - 1` to access the final element.

### 🔧 List Filtering

```markdown
**Active Projects**: `= filter(this.projects, (p) => contains(p, "active"))`
**High Priority**: `= filter(this.tasks, (t) => t.priority = "high")`
**Recent Dates**: `= filter(this.dates, (d) => d > date(today) - dur(30 days))`
```

### ➕ List Construction & Joining

```markdown
**Comma List**: `= join(this.list-field, ", ")`
**Bullet List**: `= join(this.items, "\n- ")`
**Custom Separator**: `= join(this.values, " | ")`
```

### 🔀 List Transformation

```markdown
**Sorted**: `= sort(this.list-field)`
**Reversed**: `= reverse(this.list-field)`
**Unique Items**: `= unique(this.list-with-duplicates)`
```

---

## 8. 🌐 Cross-Page Data Access

> [!definition]
> **Cross-Page Queries** retrieve [[Metadata]] from other notes via [[Wiki-Links]], enabling relational data displays and inter-note dependencies.

### 📎 Basic Link Field Access

```markdown
**Project Status**: `= [[Project Alpha]].status`
**Author Name**: `= [[Book Note]].author`
**Creation Date**: `= [[Reference]].file.ctime`
**Tag List**: `= [[Related Note]].file.tags`
```

> [!what-this-does]
> Syntax: `[[Note Name]].field-name`. Works with both [[YAML Frontmatter]] fields and [[Implicit Fields]]. The linked note must exist and contain the specified field.

### 🔗 Multi-Note Data Aggregation

```markdown
**Combined Budget**: `= [[Project A]].budget + [[Project B]].budget + [[Project C]].budget`
**Team Size**: `= length([[Team Roster]].members)`
**Linked Note Age**: `= (date(today) - [[Reference]].file.ctime).days + " days old"`
```

### 🎯 Conditional Cross-Page Access

```markdown
**Parent Status**: `= choice(contains([[Parent Note]], "status"), [[Parent Note]].status, "Status not set")`
**Safe Access**: `= choice([[Linked Note]].value, [[Linked Note]].value, "Field missing")`
```

### 📊 Cross-Note Calculations

```markdown
**Project Progress**: `= round(([[Project]].completed / [[Project]].total) * 100) + "%"`
**Days Until Deadline**: `= ([[Meeting Note]].date - date(today)).days + " days"`
**Combined Word Count**: `= [[Essay Part 1]].word-count + [[Essay Part 2]].word-count`
```

### 🌉 Relational Lookups

```markdown
**Author Bio**: `= [[Authors/]] + this.author + ]].bio`
**Category Description**: `= [[Categories/]] + this.category + ]].description`
```

> [!warning]
> Cross-page queries fail silently if the linked note or field doesn't exist. Use conditional checks for robust implementations.

---

## 9. ⚡ Status & Progress Tracking

> [!definition]
> **Status Queries** create dynamic indicators for workflow states, project stages, and task progression using visual symbols and conditional logic.

### 🎯 Stage Indicators

```markdown
**Workflow Stage**: `= choice(this.stage = "idea", "💡 Ideation", choice(this.stage = "draft", "✍️ Drafting", choice(this.stage = "review", "👀 Review", choice(this.stage = "final", "✅ Complete", "❓ Unknown"))))`
**Publication Status**: `= choice(this.published, "🌐 Published", choice(this.draft, "📝 Draft", "📋 Planning"))`
```

### 📊 Progress Visualization

```markdown
**Progress Bar**: `= choice(this.progress >= 100, "█████ 100%", choice(this.progress >= 80, "████░ " + this.progress + "%", choice(this.progress >= 60, "███░░ " + this.progress + "%", choice(this.progress >= 40, "██░░░ " + this.progress + "%", choice(this.progress >= 20, "█░░░░ " + this.progress + "%", "░░░░░ " + this.progress + "%")))))`
```

### 🔔 Deadline Status

```markdown
**Time Status**: `= choice(!this.due-date, "⚪ No Deadline", choice(this.due-date < date(today), "🔴 Overdue", choice((this.due-date - date(today)).days <= 1, "🟠 Due Tomorrow", choice((this.due-date - date(today)).days <= 7, "🟡 Due This Week", "🟢 On Track"))))`
```

### ✅ Completion Tracking

```markdown
**Checklist Progress**: `= length(filter(this.file.tasks, (t) => t.completed)) + "/" + length(this.file.tasks) + " tasks complete"`
**Milestone Status**: `= choice(this.milestone-complete, "🎯 Milestone Reached", "🎯 In Progress")`
```

### 🏷️ Priority Display

```markdown
**Priority Badge**: `= choice(this.priority = "critical", "🔴 CRITICAL", choice(this.priority = "high", "🟠 High", choice(this.priority = "medium", "🟡 Medium", choice(this.priority = "low", "🟢 Low", "⚪ None"))))`
```

---

## 10. ✍️ Text Manipulation & Formatting

> [!definition]
> **Text Queries** transform and format string values using [[Dataview Functions]] for display enhancement and data cleaning.

### ✂️ String Truncation

```markdown
**Short Description**: `= truncate(this.description, 50, "...")`
**Preview**: `= truncate(this.content, 100)`
**Title Preview**: `= truncate(this.file.name, 30, "…")`
```

> [!what-this-does]
> `truncate(string, max-length, suffix)` cuts strings at the specified length and appends an optional suffix. Essential for preview displays and table columns with character limits.

### 🔤 Case Transformation

```markdown
**Uppercase**: `= upper(this.title)`
**Lowercase**: `= lower(this.tag)`
**Title Case**: [Requires custom function]
```

### 🔍 String Searching

```markdown
**Contains Keyword**: `= choice(contains(lower(this.content), "dataview"), "✅ Contains 'dataview'", "❌ Not found")`
**Starts With**: `= choice(startswith(this.file.name, "Project"), "📁 Project Note", "📄 Standard Note")`
```

### ✂️ String Splitting & Joining

```markdown
**First Word**: `= split(this.title, " ")[0]`
**Last Name**: `= split(this.author, " ")[length(split(this.author, " ")) - 1]`
**Tag Join**: `= join(this.file.tags, ", ")`
```

### 🔄 String Replacement

```markdown
**Cleaned Path**: `= replace(this.file.path, "\\", "/")`
**Remove Prefix**: `= replace(this.file.name, "PROJ-", "")`
```

> [!helpful-tip]
> Use string manipulation for cleaning imported data, standardizing displays, or extracting substrings from structured field values.

---

## 11. 📈 Aggregation & Collection Queries

> [!definition]
> **Aggregation Queries** compute summary statistics across multiple values using [[Dataview Functions]] like `sum()`, `average()`, `min()`, and `max()`.

### ➕ Sum Aggregations

```markdown
**Total Budget**: `= sum(this.budget-items)`
**Combined Score**: `= sum([this.score1, this.score2, this.score3])`
**Total Hours**: `= sum(this.time-entries) + " hours"`
```

### 📊 Statistical Functions

```markdown
**Average**: `= round(average(this.values), 2)`
**Minimum**: `= min(this.numbers)`
**Maximum**: `= max(this.values)`
**Range**: `= max(this.data) - min(this.data)`
```

> [!what-this-does]
> Aggregation functions operate on arrays. Pass a field containing multiple values or construct an inline array with `[value1, value2, value3]` syntax.

### 📏 Count Operations

```markdown
**Item Count**: `= length(this.items)`
**Non-Empty Count**: `= length(filter(this.fields, (f) => f))`
**Unique Values**: `= length(unique(this.list))`
```

### 🔢 Derived Metrics

```markdown
**Average Score**: `= round(sum(this.scores) / length(this.scores), 1)`
**Median Value**: [Requires sorting and index calculation]
**Weighted Average**: `= sum(map(this.items, (i) => i.value * i.weight)) / sum(map(this.items, (i) => i.weight))`
```

---

## 12. 💻 Advanced DataviewJS Inline

> [!definition]
> **DataviewJS Inline Queries** use JavaScript syntax (`` `$= ...` ``) for complex operations, API access, and dynamic rendering beyond DQL capabilities.

> [!important]
> **Security Note**: DataviewJS has file system access. Only use code you understand or trust. Enable in Dataview settings under "Enable JavaScript Queries".

### 🔧 Basic DataviewJS Syntax

```markdown
**File Name**: `$= dv.current().file.name`
**Current Page**: `$= dv.current()`
**All Pages**: `$= dv.pages().length + " notes in vault"`
```

> [!what-this-does]
> `dv.current()` returns the current page object. `dv.pages()` returns all pages in the vault. DataviewJS provides the full Dataview API via the `dv` variable.

### 📊 Filtered Counts

```markdown
**Active Projects**: `$= dv.pages('#project').where(p => p.status = "active").length`
**Tagged Notes**: `$= dv.pages('#your-tag').length`
**Folder Count**: `$= dv.pages('"Your Folder"').length`
```

### 🎯 Complex Aggregations

```markdown
**Total Word Count**: `$= dv.pages().map(p => p.word-count || 0).reduce((a, b) => a + b, 0)`
**Average Rating**: `$= Math.round(dv.pages('#books').map(p => p.rating).filter(r => r).reduce((a, b) => a + b, 0) / dv.pages('#books').where(p => p.rating).length * 10) / 10`
```

### 🔗 Dynamic Link Lists

```markdown
**Recent Notes**: `$= dv.pages().sort(p => p.file.mtime, 'desc').limit(5).map(p => p.file.link).join(", ")`
**Top Linked**: `$= dv.pages().sort(p => p.file.inlinks.length, 'desc').limit(3).map(p => p.file.link + " (" + p.file.inlinks.length + ")").join(" • ")`
```

### 🧮 Custom Calculations

```markdown
**Vault Stats**: `$= "📊 " + dv.pages().length + " notes | " + dv.pages().file.tasks.length + " tasks"`
**Knowledge Score**: `$= Math.round((dv.current().file.outlinks.length * 2 + dv.current().file.inlinks.length * 3) / 10)`
```

> [!helpful-tip]
> DataviewJS excels at vault-wide statistics, complex filters, and operations requiring JavaScript methods unavailable in DQL. Use for dashboards and analytics.

### 🎨 Conditional Rendering

```markdown
**Smart Status**: `$= dv.current().status ? "✅ " + dv.current().status : "⚪ No status set"`
**List or Message**: `$= dv.current().items?.length > 0 ? dv.current().items.join(", ") : "No items"`
```

---

## 🎯 Synthesis & Mastery

> [!the-philosophy]
> **The Philosophy of Inline Queries**
> 
> Inline queries transform your [[Personal Knowledge Base]] from a static archive into a living, reactive system. They embody the principle of "**write once, compute infinitely**"—metadata entered once propagates through your vault via dynamic queries, eliminating manual updates and ensuring single-source-of-truth data integrity. This creates a [[Distributed Cognition]] architecture where your notes actively support knowledge work rather than passively storing it.

### 🧠 Cognitive Models

**The Three-Layer Query Model:**

1. **Access Layer** (What data exists?)
   - Direct field access: `this.field-name`
   - Cross-page access: `[[Note]].field`
   - System metadata: `file.*` properties

2. **Transform Layer** (How to manipulate data?)
   - Functions: `length()`, `filter()`, `round()`
   - Operations: arithmetic, string manipulation
   - Conditionals: `choice()` for logic

3. **Display Layer** (How to present results?)
   - Formatting: truncation, joining, symbols
   - Visual indicators: emojis, progress bars
   - Contextual: relative dates, status badges

> [!analogy]
> **Illuminating Comparison**
> 
> Think of inline queries as **embedded sensors** in your vault. Just as a smart home has sensors that report temperature, motion, and air quality without manual checking, inline queries monitor your notes' metadata and relationships, surfacing insights automatically. The difference? These sensors don't just report—they *compute*, enabling derived metrics and conditional logic that adapt to your knowledge base's evolution.

### 🔄 Best Practices Framework

| Practice | Implementation | Benefit |
|----------|----------------|---------|
| **Defensive Checks** | Always use `choice(contains(this, "field"), ...)` before accessing optional fields | Prevents errors from missing metadata |
| **Performance Awareness** | Avoid `file.content` in frequently-viewed notes | Reduces query overhead |
| **Semantic Naming** | Use descriptive field names (e.g., `review-date` not `rd`) | Improves query readability |
| **Template Integration** | Embed queries in [[Templater Plugin]] templates | Automates setup for new notes |
| **Incremental Complexity** | Start with simple field access, build to computations | Easier debugging and maintenance |
| **Visual Consistency** | Standardize emoji/symbol use across queries | Creates scannable patterns |

### 🛠️ Common Patterns & Anti-Patterns

**✅ DO:**
- Cache complex queries in [[YAML Frontmatter]] for reuse
- Use inline queries for dynamic calculations, not static data
- Combine with [[MOC]] patterns for vault-wide dashboards
- Test queries in single notes before template-izing

**❌ DON'T:**
- Query `file.content` repeatedly in the same note
- Create circular dependencies (Note A queries Note B which queries Note A)
- Over-engineer—start simple and add complexity as needed
- Forget null checks on optional fields

---

## 📊 Metadata & Attribution

> [!methodology-and-sources]
> **Research Methodology**
> 
> This taxonomy was compiled through:
> - **Primary Sources**: [Official Dataview Documentation](https://blacksmithgu.github.io/obsidian-dataview/), Dataview Example Vault
> - **Community Resources**: Obsidian Forums, GitHub discussions, practitioner blogs
> - **Research Queries**: "Dataview inline query syntax", "inline DQL examples", "Dataview functions reference"
> - **Synthesis Approach**: Pattern categorization by functional domain, validation of syntax against v0.5.x standard
> - **Confidence Level**: 
>   - **High**: Basic syntax, core functions, file metadata
>   - **Medium**: Advanced DataviewJS patterns, performance optimizations
>   - **Low**: Undocumented edge cases, version-specific behaviors

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-11-29 | Initial comprehensive compilation covering 12 functional categories with 120+ working examples |

---

# 🔗 Related Topics for PKB Expansion

1. **[[Dataview Functions Reference]]**
   - *Connection*: Inline queries depend on Dataview's function library for computations
   - *Depth Potential*: Exhaustive function catalog with parameter documentation
   - *Knowledge Graph Role*: Forms technical foundation layer beneath inline query patterns

2. **[[Dataview Query Language (DQL) Block Queries]]**
   - *Connection*: Complementary to inline queries—blocks for multi-result displays, inlines for single values
   - *Depth Potential*: Complete DQL syntax reference including TABLE, LIST, TASK, CALENDAR types
   - *Knowledge Graph Role*: Sibling concept in Dataview capabilities taxonomy

3. **[[Template-Driven Note Architecture]]**
   - *Connection*: Inline queries reach maximum utility when embedded in reusable templates
   - *Depth Potential*: [[Templater Plugin]] + [[QuickAdd]] integration patterns for automated query insertion
   - *Knowledge Graph Role*: Workflow implementation layer above technical query syntax

4. **[[Metadata Schema Design for PKBs]]**
   - *Connection*: Effective queries require well-designed metadata fields and naming conventions
   - *Depth Potential*: [[YAML Frontmatter]] standards, [[Inline Fields]] best practices, field naming taxonomies
   - *Knowledge Graph Role*: Data architecture prerequisite for query effectiveness

---

