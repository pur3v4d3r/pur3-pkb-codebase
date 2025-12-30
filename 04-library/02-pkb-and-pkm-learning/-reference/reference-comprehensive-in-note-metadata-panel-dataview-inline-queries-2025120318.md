---
aliases:
  - "DV Inline Reference"
  - "Dataview Inline Compendium"
tags:
  - "type/report"
  - "year/2025"
  - "type/analysis"
  - "status/in-progress"
  - "pkb"
  - "pkm"
  - "metadata-systems"
  - "critical-thinking/problem-solving"
  - "metacognitive-pkm"
  - "cognitive-resources"
  - "pkb/optimization"
  - "dataview-queries"
  - "cognitive-pkm"
source: "claude-sonnet-4.5"
id: "20251203183658"
created: "2025-12-03T18:36:58"
modified: "2025-12-03T18:36:58"
week: "[[2025-W49]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: "reference"
maturity: "needs-review"
confidence: "moderate"
next-review: "2025-12-10"
review-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-12-03|Daily-Note]]"
---
# Dataview Inline Queries: In-Note Metadata Panel
> [!overview]
> - **Title**:: [[Dataview Inline Queries: In-Note Metadata Panel]]
> - **Prompt/Topic Used**:: 
> - **Status**:: 🌱 `= this.maturity` | Confidence: `= this.confidence`

> [! ] # :FasClipboardList:In-Note Metadata Panel
> 
> - **Note-Type**: `= this.type`
> - **Development Status**: `= this.maturity`
> - **Epistemic Confidence**: `= this.confidence`
> - **Next Review**: `= this.next-review`
> - **Review Count**: `= this.review-count`
> - **Created**: `= this.created`
> - **Last Modified**: `= this.modified`
> 
> > [!purpose] ### 📝Content Metrics
> > [**Word Count**:: `= this.file.size`]| [**Est. Read Time**:: `= round(this.file.size / 1300) + " min"`]
> > [**Depth Class**:: `= choice(this.file.size < 500, "🌱Stub", choice(this.file.size < 2000, "📄Note", "📜Essay"))`]
> ----
> > [!purpose] ### 🕰️Temporal Context
> > [**Created**:: `= this.file.ctime`] | [**Age**:: `= (date(today) - this.file.ctime).days + " days"`]
> > [**Last Touch**:: `= this.file.mtime`] | [**Staleness**:: `= choice((date(today) - this.file.mtime).days > 180, "🕸️Cobwebs", choice((date(today) - this.file.mtime).days > 30, "🍂Cold", "🔥Fresh"))`]
> > [**Touch Frequency**:: `= choice((date(today) - this.file.mtime).days < 7, "🔥Active", choice((date(today) - this.file.mtime).days < 30, "👌Regular", "❄️Dormant"))`]
> ----
> > [!topic-idea] ### 🔗Network Connectivity
> > [**In-Links**:: `= length(this.file.inlinks)`] | [**Out-Links**:: `= length(this.file.outlinks)`]
> > [**Network Status**:: `= choice(length(this.file.inlinks) = 0, "🕸️Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱Node"))`]
> ```dataviewjs
> // SYSTEM: Semantic Bridge Engine
> // PURPOSE: Find "Sibling" notes that share the same Outlinks (Contexts)
> const current = dv.current();
> const myOutlinks = current.file.outlinks.map(l => l.path);
> 
> // 1. Filter the Vault
> const siblings = dv.pages()
>     .where(p => p.file.path !== current.file.path) // Exclude self
>     .where(p => !current.file.outlinks.map(l => l.path).includes(p.file.path)) // Exclude existing direct links
>     .map(p => {
>         // Find overlap between this page's links and the current page's links
>         const shared = p.file.outlinks.filter(l => myOutlinks.includes(l.path));
>         return { 
>             link: p.file.link, 
>             sharedCount: shared.length, 
>             sharedLinks: shared 
>         };
>     })
>     .where(p => p.sharedCount > 0) // Must share at least 1 connection
>     .sort(p => p.sharedCount, "desc") // Sort by strongest connection
>     .limit(5); // Only show top 5
> 
> // 2. Render the Bridge
> if (siblings.length > 0) {
>     dv.header(3, "Semantic Bridges (Missing Connections)");
>     dv.table(
>         ["Sibling Note", "Strength", "Shared Context"], 
>         siblings.map(s => [
>             s.link, 
>             "🔗" + s.sharedCount, 
>             s.sharedLinks.slice(0, 3).join(", ") + (s.sharedCount > 3 ? "…" : "")
>         ])
>     );
> } else {
>     dv.paragraph("*No semantic siblings found. This note is unique in its connections.*");
> }
> ```
---

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
SORT file.ctime DESC
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
### 2025-12-03 - Initial Creation
*Context*: `=this.title` **by**: `=this.source`
*Maturity*: `= this.maturity`  
*Confidence*: `= this.confidence`

### Tags & Classification
*Primary Tags*: `= this.tags`  
*Type*: `= this.type`  
*Source*: `= this.source`

---

I'll conduct a comprehensive tree-of-thoughts search to identify all available Dataview inline query patterns, organized by functional domain. Let me systematically explore the landscape of inline queries.


**REQUEST CLASSIFICATION:**
- Type: comprehensive_note → Reference Resource
- Scope: reference → Exhaustive coverage of Dataview inline queries
- Research Required: YES - This requires systematic exploration of Dataview capabilities to ensure comprehensive coverage
- Note Type: Reference Note (comprehensive resource)

**RESEARCH STRATEGY:**
I need to explore Dataview's inline query capabilities systematically across multiple dimensions:
1. Metadata properties (file, frontmatter, implicit)
2. Temporal queries (dates, durations, calculations)
3. Aggregations and calculations
4. Conditional logic and choice functions
5. Link analysis and graph metrics
6. List and array operations
7. String manipulations
8. Custom frontmatter field queries

**STRUCTURAL PLANNING:**
- Metadata header with appropriate tags
- Hierarchical organization by functional domain
- Each pattern with: syntax, explanation, use case, example
- Multiple variations per category
- Progressive complexity within each section
- Extensive wiki-links to related concepts
- Callouts for important patterns and tips
- Expansion section linking to advanced topics

**WIKI-LINK OPPORTUNITIES:**
[[Dataview]], [[Inline Queries]], [[Metadata]], [[Frontmatter]], [[YAML]], [[DQL]], [[Obsidian]], [[Knowledge Graph]], [[Link Analysis]], [[Temporal Queries]], [[Aggregation Functions]], [[Conditional Logic]], [[String Manipulation]], [[File Properties]], [[Dashboard Design]], [[PKB Architecture]]


---
tags: #dataview #inline-queries #reference-note #obsidian #pkb-architecture #dashboard-design
aliases: [DV Inline Reference, Dataview Inline Compendium, Inline Query Patterns, DV Inline Syntax Guide]
---

# 📊 Dataview Inline Queries: Complete Reference Compendium

> [!abstract] Overview
> This comprehensive reference catalogs all known [[Dataview]] inline query patterns, organized by functional domain. Each pattern includes syntax, explanation, use cases, and practical examples designed for [[Dashboard Design]] and [[PKB Architecture]] implementations.

> [!important] Inline Query Fundamentals
> **Syntax Structure:** `` `= <expression>` ``
> 
> Inline queries evaluate expressions in-place and render results directly in your note. They have access to:
> - **`this`**: Current file's metadata and properties
> - **File Properties**: All implicit file metadata
> - **Frontmatter**: All YAML properties
> - **Functions**: Date manipulation, math, string operations, conditionals

---

## 🏗️ I. Core Metadata & File Properties

### A. Basic File Metadata Access

> [!definition] File Metadata Queries
> These queries access implicit properties automatically maintained by [[Obsidian]] for every file.

#### 1. **File Identification**

```markdown
**File Name**: `= this.file.name`
**Full Path**: `= this.file.path`
**Folder**: `= this.file.folder`
**Extension**: `= this.file.ext`
```

**Use Case:** File navigation, breadcrumb systems, folder-based organization displays

#### 2. **Content Metrics**

```markdown
**File Size**: `= this.file.size` bytes
**File Size (KB)**: `= round(this.file.size / 1024, 2)` KB
**Word Count (Estimate)**: `= round(this.file.size / 6)` words
**Character Count**: `= this.file.size` characters
```

**Use Case:** Content depth analysis, reading time estimation, dashboard metrics

#### 3. **Temporal Properties**

```markdown
**Created**: `= this.file.ctime`
**Modified**: `= this.file.mtime`
**Created (Custom Format)**: `= dateformat(this.file.ctime, "yyyy-MM-dd HH:mm")`
**Modified (Relative)**: `= dateformat(this.file.mtime, "relative")`
**Day of Week Created**: `= dateformat(this.file.ctime, "cccc")`
**Month Created**: `= dateformat(this.file.ctime, "MMMM yyyy")`
```

**Use Case:** Temporal tracking, staleness analysis, creation date displays

### B. Link & Relationship Analysis

> [!key-claim] Network Metrics
> Link analysis queries are fundamental to [[Knowledge Graph]] health monitoring and [[Zettelkasten]] maintenance.

#### 4. **Link Counts**

```markdown
**Outgoing Links**: `= length(this.file.outlinks)`
**Incoming Links**: `= length(this.file.inlinks)`
**Total Link Count**: `= length(this.file.outlinks) + length(this.file.inlinks)`
**Link Density**: `= round((length(this.file.outlinks) + length(this.file.inlinks)) / (this.file.size / 1000), 2)` links/KB
```

**Use Case:** Hub detection, orphan identification, link density analysis

#### 5. **Link Lists**

```markdown
**All Outlinks**: `= this.file.outlinks`
**All Inlinks**: `= this.file.inlinks`
**First Outlink**: `= this.file.outlinks[0]`
**Last Outlink**: `= this.file.outlinks[length(this.file.outlinks) - 1]`
**Random Link**: `= this.file.outlinks[floor(random() * length(this.file.outlinks))]`
```

**Use Case:** Link previews, connection samples, random navigation

#### 6. **Tag Operations**

```markdown
**All Tags**: `= this.file.tags`
**Tag Count**: `= length(this.file.tags)`
**First Tag**: `= this.file.tags[0]`
**Has Specific Tag**: `= contains(this.file.tags, "#pkm")`
**Tag List (Comma Separated)**: `= join(this.file.tags, ", ")`
```

**Use Case:** Tag cloud generation, classification displays, tag filtering

### C. Frontmatter Property Access

> [!methodology-and-sources] Custom Property Queries
> Access any [[YAML]] frontmatter property using `this.<property-name>` notation. Properties can be strings, numbers, dates, lists, or objects.

#### 7. **String Properties**

```markdown
**Type**: `= this.type`
**Status**: `= this.status`
**Author**: `= this.author`
**Source**: `= this.source`
**Custom Field**: `= this.<your-field-name>`
```

**Use Case:** Metadata display panels, note classification, custom workflow tracking

#### 8. **Numeric Properties**

```markdown
**Priority**: `= this.priority`
**Version**: `= this.version`
**Rating**: `= this.rating`
**Progress**: `= this.progress`%
**Score**: `= this.score`/10
```

**Use Case:** Progress tracking, rating displays, numeric dashboards

#### 9. **Date Properties**

```markdown
**Due Date**: `= this.due`
**Published**: `= this.published`
**Review Date**: `= this.next-review`
**Date (Formatted)**: `= dateformat(this.due, "MMMM dd, yyyy")`
**Days Until Due**: `= (this.due - date(today)).days`
```

**Use Case:** Deadline tracking, review scheduling, temporal workflows

#### 10. **List Properties**

```markdown
**All Aliases**: `= this.aliases`
**Alias Count**: `= length(this.aliases)`
**First Alias**: `= this.aliases[0]`
**Link-Up MOCs**: `= this.link-up`
**Related Notes**: `= this.link-related`
```

**Use Case:** Alternative name displays, MOC navigation, relationship tracking

---

## ⏰ II. Temporal Calculations & Date Operations

### A. Date Arithmetic

> [!example] Date Manipulation
> [[Dataview]] provides powerful date calculation capabilities using the `date()` function and duration arithmetic.

#### 11. **Age Calculations**

```markdown
**Note Age**: `= (date(today) - this.file.ctime).days` days
**Age in Weeks**: `= round((date(today) - this.file.ctime).days / 7, 1)` weeks
**Age in Months**: `= round((date(today) - this.file.ctime).days / 30, 1)` months
**Age in Years**: `= round((date(today) - this.file.ctime).years, 2)` years
```

**Use Case:** Freshness metrics, aging analysis, temporal context

#### 12. **Staleness Calculations**

```markdown
**Days Since Modified**: `= (date(today) - this.file.mtime).days`
**Weeks Since Modified**: `= round((date(today) - this.file.mtime).days / 7, 1)`
**Last Modified (Relative)**: `= dateformat(this.file.mtime, "relative")`
```

**Use Case:** Maintenance scheduling, staleness warnings, update prompts

#### 13. **Future Date Calculations**

```markdown
**Days Until Review**: `= (this.next-review - date(today)).days`
**Weeks Until Due**: `= round((this.due - date(today)).days / 7, 1)`
**Is Overdue**: `= this.due < date(today)`
**Time Remaining**: `= this.due - date(today)`
```

**Use Case:** Deadline tracking, review systems, temporal warnings

#### 14. **Date Comparisons**

```markdown
**Created This Week**: `= (date(today) - this.file.ctime).days <= 7`
**Modified This Month**: `= (date(today) - this.file.mtime).days <= 30`
**Created Before 2024**: `= this.file.ctime < date("2024-01-01")`
**Between Dates**: `= this.file.ctime >= date("2024-01-01") AND this.file.ctime <= date("2024-12-31")`
```

**Use Case:** Date filtering, temporal queries, period analysis

### B. Duration Formatting

#### 15. **Human-Readable Durations**

```markdown
**Note Age (Formatted)**: `= dur(date(today) - this.file.ctime)`
**Time Since Modification**: `= dur(date(today) - this.file.mtime)`
**Time to Deadline**: `= dur(this.due - date(today))`
```

**Use Case:** User-friendly time displays, duration visualization

#### 16. **Custom Date Formats**

```markdown
**ISO Format**: `= dateformat(this.file.ctime, "yyyy-MM-dd")`
**US Format**: `= dateformat(this.file.ctime, "MM/dd/yyyy")`
**European Format**: `= dateformat(this.file.ctime, "dd.MM.yyyy")`
**Long Format**: `= dateformat(this.file.ctime, "EEEE, MMMM dd, yyyy")`
**Time Only**: `= dateformat(this.file.ctime, "HH:mm:ss")`
**Custom Pattern**: `= dateformat(this.file.ctime, "yyyy 'Week' ww")`
```

**Use Case:** Localization, date formatting standards, custom displays

---

## 🧮 III. Mathematical Operations & Aggregations

### A. Basic Arithmetic

> [!methodology-and-sources] Numeric Calculations
> Inline queries support standard mathematical operations and functions for numeric property manipulation.

#### 17. **Simple Math**

```markdown
**Sum**: `= this.value1 + this.value2`
**Difference**: `= this.value1 - this.value2`
**Product**: `= this.value1 * this.value2`
**Quotient**: `= this.value1 / this.value2`
**Modulo**: `= this.value1 % this.value2`
**Exponentiation**: `= this.value1 ^ this.value2`
```

**Use Case:** Calculated fields, derived metrics, composite values

#### 18. **Rounding Functions**

```markdown
**Round to Integer**: `= round(this.value)`
**Round to 2 Decimals**: `= round(this.value, 2)`
**Round Down (Floor)**: `= floor(this.value)`
**Round Up (Ceiling)**: `= ceil(this.value)`
**Truncate**: `= trunc(this.value)`
```

**Use Case:** Clean numeric displays, precision control, integer conversion

#### 19. **Advanced Math Functions**

```markdown
**Absolute Value**: `= abs(this.value)`
**Square Root**: `= sqrt(this.value)`
**Minimum**: `= min(this.value1, this.value2, this.value3)`
**Maximum**: `= max(this.value1, this.value2, this.value3)`
**Average**: `= (this.value1 + this.value2 + this.value3) / 3`
```

**Use Case:** Statistical calculations, range operations, comparative metrics

### B. Percentage Calculations

#### 20. **Percentage Operations**

```markdown
**Completion Percentage**: `= round((this.completed / this.total) * 100, 1)`%
**Progress Bar**: `= round(this.progress)`% of `= this.goal`
**Percentage Change**: `= round(((this.new - this.old) / this.old) * 100, 1)`%
**Percentage of Total**: `= round((this.value / this.total) * 100, 2)`%
```

**Use Case:** Progress tracking, completion indicators, comparative analysis

### C. List Aggregations

> [!key-claim] List Operations
> When properties contain lists or arrays, [[Dataview]] provides aggregation functions for statistical analysis.

#### 21. **List Statistics**

```markdown
**List Length**: `= length(this.my-list)`
**Sum of List**: `= sum(this.numbers)`
**Average of List**: `= sum(this.numbers) / length(this.numbers)`
**Min in List**: `= min(this.numbers)`
**Max in List**: `= max(this.numbers)`
```

**Use Case:** Collection statistics, multi-value analysis, list metrics

#### 22. **List Item Access**

```markdown
**First Item**: `= this.my-list[0]`
**Last Item**: `= this.my-list[length(this.my-list) - 1]`
**Second Item**: `= this.my-list[1]`
**Middle Item**: `= this.my-list[floor(length(this.my-list) / 2)]`
**Random Item**: `= this.my-list[floor(random() * length(this.my-list))]`
```

**Use Case:** List sampling, item extraction, random selection

---

## 🔀 IV. Conditional Logic & Choice Functions

### A. Basic Conditionals

> [!definition] Choice Function
> The `choice()` function enables conditional rendering: `choice(condition, value_if_true, value_if_false)`

#### 23. **Simple Conditionals**

```markdown
**Binary Status**: `= choice(this.status = "complete", "✅ Done", "⏳ Pending")`
**Yes/No**: `= choice(this.flag, "Yes", "No")`
**Active/Inactive**: `= choice(this.active, "🟢 Active", "⭕ Inactive")`
**Present/Missing**: `= choice(this.property, "Has Value", "No Value")`
```

**Use Case:** Status indicators, boolean displays, conditional formatting

#### 24. **Numeric Thresholds**

```markdown
**Size Category**: `= choice(this.file.size < 500, "🌱 Small", choice(this.file.size < 5000, "📄 Medium", "📜 Large"))`
**Priority Level**: `= choice(this.priority > 7, "🔴 High", choice(this.priority > 3, "🟡 Medium", "🟢 Low"))`
**Rating Stars**: `= choice(this.rating >= 4, "⭐⭐⭐⭐", choice(this.rating >= 2, "⭐⭐", "⭐"))`
```

**Use Case:** Categorical classification, threshold-based displays, visual indicators

#### 25. **Date-Based Conditions**

```markdown
**Freshness**: `= choice((date(today) - this.file.mtime).days < 7, "🔥 Fresh", choice((date(today) - this.file.mtime).days < 30, "👌 Recent", "❄️ Old"))`
**Age Category**: `= choice((date(today) - this.file.ctime).days < 30, "🌱 New", choice((date(today) - this.file.ctime).days < 180, "🌿 Growing", "🌳 Mature"))`
**Deadline Status**: `= choice(this.due < date(today), "⚠️ Overdue", choice(this.due < date(today) + dur("7 days"), "⏰ Due Soon", "✅ On Track"))`
```

**Use Case:** Temporal categorization, freshness indicators, deadline warnings

### B. Complex Nested Conditions

#### 26. **Multi-Level Classification**

```markdown
**Staleness Level**: `= choice((date(today) - this.file.mtime).days > 180, "🕸️ Cobwebs", choice((date(today) - this.file.mtime).days > 90, "🍂 Cold", choice((date(today) - this.file.mtime).days > 30, "🌤️ Cool", "🔥 Hot")))`

**Network Status**: `= choice(length(this.file.inlinks) = 0, "🕸️ Orphan", choice(length(this.file.inlinks) > 10, "⚡ Super Hub", choice(length(this.file.inlinks) > 5, "🌟 Hub", "🌱 Node")))`

**Content Depth**: `= choice(this.file.size < 500, "🌱 Stub", choice(this.file.size < 2000, "📝 Note", choice(this.file.size < 10000, "📄 Article", "📚 Document")))`
```

**Use Case:** Multi-tier classification, sophisticated categorization, nuanced indicators

#### 27. **Boolean Combinations**

```markdown
**Status Check**: `= choice(this.status = "complete" AND this.reviewed, "✅ Verified", choice(this.status = "complete", "⏳ Needs Review", "❌ Incomplete"))`

**Link Health**: `= choice(length(this.file.outlinks) > 0 AND length(this.file.inlinks) > 0, "🔗 Well Connected", choice(length(this.file.outlinks) > 0, "➡️ Outbound Only", choice(length(this.file.inlinks) > 0, "⬅️ Inbound Only", "⛔ Isolated")))`
```

**Use Case:** Complex state logic, multi-condition checking, validation displays

---

## 🔤 V. String Manipulation & Formatting

### A. String Operations

> [!methodology-and-sources] Text Processing
> [[Dataview]] provides string manipulation functions for text transformation and formatting within inline queries.

#### 28. **Basic String Functions**

```markdown
**Uppercase**: `= upper(this.title)`
**Lowercase**: `= lower(this.title)`
**Title Case**: `= upper(substring(this.title, 0, 1)) + lower(substring(this.title, 1))`
**String Length**: `= length(this.title)`
**Substring**: `= substring(this.title, 0, 20)` + "…"
```

**Use Case:** Text formatting, case conversion, truncation

#### 29. **String Concatenation**

```markdown
**Simple Join**: `= this.first-name + " " + this.last-name`
**Formatted Label**: `= this.type + ": " + this.title`
**Prefixed Value**: `= "Status: " + this.status`
**Path Construction**: `= this.folder + "/" + this.file-name`
```

**Use Case:** Label construction, composite fields, formatted displays

#### 30. **String Checks**

```markdown
**Contains Check**: `= contains(this.title, "important")`
**Starts With**: `= startswith(this.file.name, "Draft")`
**Ends With**: `= endswith(this.file.name, ".draft")`
**String Equality**: `= this.status = "complete"`
**Case Insensitive Match**: `= lower(this.type) = "reference"`
```

**Use Case:** Pattern matching, validation, conditional filtering

### B. List to String Conversion

#### 31. **Join Operations**

```markdown
**Comma Separated**: `= join(this.tags, ", ")`
**Pipe Separated**: `= join(this.categories, " | ")`
**Custom Separator**: `= join(this.aliases, " • ")`
**Newline Separated**: `= join(this.items, "\\n")`
**With Prefix**: `= join(map(this.tags, (t) => "#" + t), ", ")`
```

**Use Case:** List formatting, tag displays, multi-value rendering

#### 32. **Advanced List Formatting**

```markdown
**Numbered List**: `= join(map(this.items, (item, idx) => (idx + 1) + ". " + item), "\\n")`
**Bullet List**: `= join(map(this.tasks, (t) => "• " + t), "\\n")`
**Tagged Items**: `= join(map(this.links, (l) => "[[" + l + "]]"), ", ")`
```

**Use Case:** Custom list rendering, formatted outputs, structured displays

---

## 📊 VI. Advanced Patterns & Composite Queries

### A. Reading Time Estimation

> [!example] Content Analysis
> Combine multiple metrics to derive useful composite values for [[Dashboard Design]].

#### 33. **Reading Time Variants**

```markdown
**Est. Read Time (Minutes)**: `= round(this.file.size / 1300)` min
**Read Time (Detailed)**: `= floor(this.file.size / 1300)` min `= (this.file.size % 1300) / 1300 * 60` sec
**Read Time Range**: `= round(this.file.size / 1500)` - `= round(this.file.size / 1000)` min
**Words Per Minute**: `= round(this.file.size / 6 / this.read-time)` WPM (if read-time property exists)
```

**Use Case:** Reading time displays, content consumption planning, time budgeting

### B. Health & Quality Metrics

#### 34. **Note Quality Indicators**

```markdown
**Link Density**: `= round((length(this.file.outlinks) + length(this.file.inlinks)) / (this.file.size / 1000), 2)` links/KB
**Link Ratio**: `= round(length(this.file.inlinks) / length(this.file.outlinks), 2)` (inbound/outbound)
**Tag Density**: `= round(length(this.file.tags) / (this.file.size / 1000), 1)` tags/KB
**Metadata Completeness**: `= round((length(keys(this)) / 15) * 100, 1)`% (assuming 15 expected fields)
```

**Use Case:** Quality assessment, [[Zettelkasten]] health, maintenance prioritization

#### 35. **Activity Metrics**

```markdown
**Touch Frequency**: `= choice((date(today) - this.file.mtime).days < 7, "🔥 Active", choice((date(today) - this.file.mtime).days < 30, "👌 Regular", "❄️ Dormant"))`
**Edit Velocity**: `= round((date(today) - this.file.ctime).days / (this.review-count || 1), 1)` days/edit
**Engagement Score**: `= round(length(this.file.inlinks) + length(this.file.outlinks) + (this.review-count || 0) * 2)`
```

**Use Case:** Activity tracking, engagement analysis, interaction metrics

### C. Maturity & Development Tracking

> [!key-claim] Progressive Development
> Use conditional logic and numeric thresholds to track note maturity through development stages.

#### 36. **Maturity Indicators**

```markdown
**Maturity Status**: `= this.maturity`
**Maturity Icon**: `= choice(this.maturity = "evergreen", "🌳", choice(this.maturity = "budding", "🌿", choice(this.maturity = "developing", "🌱", "🌾")))`
**Confidence Level**: `= this.confidence`
**Confidence Badge**: `= choice(this.confidence = "high", "🟢", choice(this.confidence = "moderate", "🟡", "🔴"))`
```

**Use Case:** Development stage tracking, maturity visualization, confidence indicators

#### 37. **Review Scheduling**

```markdown
**Next Review**: `= this.next-review`
**Days Until Review**: `= (this.next-review - date(today)).days`
**Review Status**: `= choice(this.next-review < date(today), "⚠️ Review Overdue", choice((this.next-review - date(today)).days < 3, "⏰ Review Soon", "✅ Scheduled"))`
**Review Count**: `= this.review-count`
**Average Review Interval**: `= round((date(today) - this.file.ctime).days / (this.review-count || 1))` days
```

**Use Case:** [[03-notes/01_permanent-notes/01_cognitive-development/Spaced Repetition]] systems, review tracking, maintenance scheduling

---

## 🎨 VII. Visual & Dashboard Elements

### A. Emoji Status Indicators

> [!helpful-tip] Visual Enhancement
> Emoji-based indicators provide quick visual scanning in dashboards and metadata panels.

#### 38. **Status Icons**

```markdown
**Completion Status**: `= choice(this.status = "complete", "✅", choice(this.status = "in-progress", "⏳", "⭕"))`
**Priority Indicator**: `= choice(this.priority > 7, "🔴", choice(this.priority > 4, "🟡", "🟢"))`
**Type Icon**: `= choice(this.type = "reference", "📚", choice(this.type = "moc", "🗺️", choice(this.type = "permanent", "💎", "📝")))`
```

**Use Case:** Quick status recognition, visual dashboards, at-a-glance assessment

#### 39. **Progress Bars (Text-Based)**

```markdown
**Simple Progress**: `= repeat("█", floor(this.progress / 10))` `= repeat("░", 10 - floor(this.progress / 10))` `= this.progress`%
**Completion Bar**: `= "[" + repeat("=", floor(this.completion * 20)) + repeat(" ", 20 - floor(this.completion * 20)) + "]"`
```

**Use Case:** Visual progress tracking, completion indicators, goal visualization

### B. Composite Dashboard Panels

#### 40. **Metadata Summary Panel**

```markdown
**File**: `= this.file.name` | **Type**: `= this.type`
**Created**: `= dateformat(this.file.ctime, "yyyy-MM-dd")` | **Age**: `= (date(today) - this.file.ctime).days` days
**Modified**: `= dateformat(this.file.mtime, "yyyy-MM-dd")` | **Staleness**: `= (date(today) - this.file.mtime).days` days
**Size**: `= round(this.file.size / 1024, 2)` KB | **Est. Read**: `= round(this.file.size / 1300)` min
**Links In**: `= length(this.file.inlinks)` | **Links Out**: `= length(this.file.outlinks)`
```

**Use Case:** Comprehensive metadata displays, note overview panels

#### 41. **Network Status Panel**

```markdown
**In-Links**: `= length(this.file.inlinks)` | **Out-Links**: `= length(this.file.outlinks)`
**Network Status**: `= choice(length(this.file.inlinks) = 0, "🕸️ Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱 Node"))`
**Link Ratio**: `= round(length(this.file.inlinks) / (length(this.file.outlinks) || 1), 2)`
**First Inlink**: `= this.file.inlinks[0]`
**First Outlink**: `= this.file.outlinks[0]`
```

**Use Case:** [[Knowledge Graph]] health monitoring, link analysis, connection tracking

---

## 🔧 VIII. Utility Patterns & Advanced Techniques

### A. Null Handling & Fallbacks

> [!warning] Defensive Programming
> Always account for missing properties to prevent broken queries and maintain dashboard stability.

#### 42. **Null Coalescing**

```markdown
**With Fallback**: `= this.property || "Not Set"`
**Numeric Fallback**: `= this.count || 0`
**Date Fallback**: `= this.due || "No Deadline"`
**List Fallback**: `= this.tags || []`
**Chained Fallback**: `= this.primary || this.secondary || "Default"`
```

**Use Case:** Error prevention, graceful degradation, default value handling

#### 43. **Existence Checks**

```markdown
**Property Exists**: `= choice(this.property, "✅ Present", "❌ Missing")`
**Has Value**: `= choice(this.value, this.value, "N/A")`
**Non-Empty List**: `= choice(length(this.list || []) > 0, "Has Items", "Empty")`
**Valid Date**: `= choice(this.date, dateformat(this.date, "yyyy-MM-dd"), "No Date")`
```

**Use Case:** Validation, completeness checking, data quality monitoring

### B. Random & Dynamic Content

#### 44. **Random Selection**

```markdown
**Random Number**: `= floor(random() * 100)`
**Random List Item**: `= this.list[floor(random() * length(this.list))]`
**Random Link**: `= this.file.outlinks[floor(random() * length(this.file.outlinks))]`
**Random Tag**: `= this.file.tags[floor(random() * length(this.file.tags))]`
```

**Use Case:** Random navigation, surprise connections, serendipitous discovery

#### 45. **Current Timestamp Queries**

```markdown
**Current Date**: `= date(today)`
**Current Date (Formatted)**: `= dateformat(date(today), "yyyy-MM-dd")`
**Current Year**: `= dateformat(date(today), "yyyy")`
**Current Month**: `= dateformat(date(today), "MMMM")`
**Day of Year**: `= dateformat(date(today), "DDD")`
**Week Number**: `= dateformat(date(today), "ww")`
```

**Use Case:** Dynamic date references, current context displays, temporal anchoring

### C. Complex Calculations

> [!methodology-and-sources] Advanced Computation
> Combine multiple query patterns for sophisticated derived metrics and analytical displays.

#### 46. **Compound Metrics**

```markdown
**Knowledge Density**: `= round((length(this.file.outlinks) * 2 + length(this.file.inlinks)) / ((this.file.size / 1000) || 1), 2)`
**Engagement Index**: `= round((length(this.file.inlinks) * 3 + this.review-count * 2 + length(this.file.outlinks)) / ((date(today) - this.file.ctime).days || 1) * 100, 1)`
**Maturity Score**: `= round((this.review-count * 10 + length(this.file.inlinks) * 5 + length(this.file.outlinks) * 2 + (this.file.size / 1000)) / 4, 1)`
```

**Use Case:** Custom scoring systems, ranking algorithms, quality assessment

#### 47. **Weighted Averages**

```markdown
**Weighted Score**: `= round((this.score1 * 0.5 + this.score2 * 0.3 + this.score3 * 0.2), 2)`
**Composite Rating**: `= round((this.quality * 0.4 + this.utility * 0.3 + this.completeness * 0.3) * 10, 1)`/10
```

**Use Case:** Composite metrics, prioritization scores, multi-factor evaluation

---

## 🧩 IX. Integration Patterns with Dataview Queries

### A. Complementary Inline Queries for Tables

> [!example] Hybrid Usage
> Inline queries work alongside standard [[DQL]] table/list queries to create comprehensive dashboard systems.

#### 48. **Pre-Query Summary Statistics**

```markdown
**Total Notes in Query**: `= length(dv.pages('"folder"'))`
**Average File Size**: `= round(sum(map(dv.pages('"folder"'), p => p.file.size)) / length(dv.pages('"folder"')) / 1024, 2)` KB
**Most Recent**: `= max(map(dv.pages('"folder"'), p => p.file.mtime))`
```

**Use Case:** Query result previews, aggregate statistics, data overview

#### 49. **Post-Query Analysis**

```markdown
**Notes With Tag**: `= length(filter(dv.pages(), p => contains(p.file.tags, "#important")))`
**Orphan Count**: `= length(filter(dv.pages(), p => length(p.file.inlinks) = 0))`
**Hub Count**: `= length(filter(dv.pages(), p => length(p.file.inlinks) > 5))`
```

**Use Case:** Collection statistics, filtered counts, health metrics

### B. File List Filtering

#### 50. **Conditional File Collections**

```markdown
**Recent Files**: `= filter(dv.pages(), p => (date(today) - p.file.mtime).days < 7)`
**Large Files**: `= filter(dv.pages(), p => p.file.size > 10000)`
**Well-Connected**: `= filter(dv.pages(), p => length(p.file.inlinks) > 3)`
**By Type**: `= filter(dv.pages(), p => p.type = "reference")`
```

**Use Case:** Dynamic collections, filtered views, conditional aggregation

---

## 📈 X. Specialized Use Cases

### A. Research & Academic Tracking

> [!key-claim] Research Workflows
> Inline queries support sophisticated academic and research tracking systems within [[PKB Architecture]].

#### 51. **Citation & Reference Tracking**

```markdown
**Citation Count**: `= this.citations`
**Reference List**: `= join(this.references, ", ")`
**Has Bibliography**: `= choice(this.references, "✅ References Present", "⚠️ No References")`
**Source Type**: `= this.source-type`
**Publication Year**: `= this.year`
```

**Use Case:** Academic note management, citation tracking, bibliography systems

#### 52. **Reading List Management**

```markdown
**Read Status**: `= choice(this.read, "✅ Read", "📚 Unread")`
**Pages**: `= this.pages` | **Progress**: `= round((this.pages-read / this.pages) * 100, 1)`%
**Time to Read**: `= round(this.pages * 2)` minutes (2 min/page)
**Priority**: `= this.priority` | **Due**: `= this.due`
```

**Use Case:** Reading queue management, progress tracking, time estimation

### B. Project & Task Management

#### 53. **Project Metrics**

```markdown
**Project Status**: `= this.project-status`
**Completion**: `= this.completion`%
**Tasks Complete**: `= this.tasks-done`/`= this.tasks-total`
**Days Active**: `= (date(today) - this.project-start).days`
**Projected End**: `= this.project-start + dur(this.estimated-days + " days")`
```

**Use Case:** Project dashboards, timeline tracking, completion monitoring

#### 54. **Habit & Goal Tracking**

```markdown
**Current Streak**: `= this.streak` days
**Longest Streak**: `= this.longest-streak` days
**Success Rate**: `= round((this.completed / this.attempts) * 100, 1)`%
**Last Completion**: `= this.last-completed`
**Next Target**: `= this.next-target`
```

**Use Case:** Habit tracking, goal monitoring, streak visualization

### C. Content Management

> [!methodology-and-sources] Publishing Workflows
> Track content through editorial pipelines with status-based inline queries.

#### 55. **Editorial Workflow**

```markdown
**Draft Status**: `= this.draft-status`
**Word Target**: `= this.word-count`/`= this.target-words` (`= round((this.word-count / this.target-words) * 100, 1)`%)
**Editor**: `= this.editor`
**Last Edit**: `= this.last-edited`
**Publish Date**: `= this.publish-date`
```

**Use Case:** Content pipelines, publishing workflows, editorial tracking

#### 56. **Version Control**

```markdown
**Version**: `= this.version`
**Last Modified By**: `= this.modified-by`
**Change Summary**: `= this.changes`
**Previous Version**: `= this.previous-version`
**Revision Count**: `= this.revision-count`
```

**Use Case:** Version tracking, change management, collaborative editing

---

## 🎓 XI. Learning & Skill Development

### A. Learning Path Tracking

> [!example] Educational Applications
> [[Andragogy]] principles applied through inline query tracking systems.

#### 57. **Study Progress**

```markdown
**Mastery Level**: `= this.mastery-level`
**Study Time**: `= this.study-time` hours
**Review Interval**: `= this.review-interval` days
**Next Review**: `= this.file.mtime + dur(this.review-interval + " days")`
**Retention Rate**: `= round((this.correct / this.attempts) * 100, 1)`%
```

**Use Case:** [[03-notes/01_permanent-notes/01_cognitive-development/Spaced Repetition]], learning analytics, study scheduling

#### 58. **Skill Progression**

```markdown
**Skill Level**: `= this.skill-level`/10
**XP Points**: `= this.xp`
**Next Level At**: `= this.next-level-xp`
**Progress to Next**: `= round((this.xp / this.next-level-xp) * 100, 1)`%
**Achievements**: `= length(this.achievements)`
```

**Use Case:** Gamification, skill tracking, progression systems

### B. Concept Relationships

#### 59. **Knowledge Graph Metrics**

```markdown
**Concept Type**: `= this.concept-type`
**Prerequisites**: `= join(this.prerequisites, ", ")`
**Related Concepts**: `= length(this.related)`
**Depth Level**: `= this.depth-level`
**Domain**: `= this.domain`
```

**Use Case:** Concept mapping, prerequisite tracking, learning hierarchies

---

## 🌐 XII. Multi-Property Patterns

### A. Comprehensive Status Panels

> [!helpful-tip] Dashboard Composition
> Combine multiple inline queries in callouts to create rich, informative metadata panels.

#### 60. **Complete Metadata Dashboard**

```markdown
> [!abstract] Note Overview
> **Type**: `= this.type` | **Status**: `= this.status` | **Maturity**: `= this.maturity`
> **Created**: `= dateformat(this.file.ctime, "yyyy-MM-dd")` | **Age**: `= (date(today) - this.file.ctime).days` days
> **Modified**: `= dateformat(this.file.mtime, "yyyy-MM-dd")` | **Staleness**: `= (date(today) - this.file.mtime).days` days
> **Size**: `= round(this.file.size / 1024, 2)` KB | **Words**: `= round(this.file.size / 6)` | **Read Time**: `= round(this.file.size / 1300)` min
> **In-Links**: `= length(this.file.inlinks)` | **Out-Links**: `= length(this.file.outlinks)` | **Tags**: `= length(this.file.tags)`
> **Link Status**: `= choice(length(this.file.inlinks) = 0, "🕸️ Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱 Node"))`
> **Freshness**: `= choice((date(today) - this.file.mtime).days < 7, "🔥 Fresh", choice((date(today) - this.file.mtime).days < 30, "👌 Recent", "❄️ Stale"))`
```

**Use Case:** Comprehensive note headers, full metadata displays, dashboard integration

#### 61. **Health & Quality Panel**

```markdown
> [!check] Note Health
> **Completeness**: `= choice(this.type AND this.status AND this.maturity, "✅ Complete", "⚠️ Missing Fields")`
> **Link Density**: `= round((length(this.file.outlinks) + length(this.file.inlinks)) / (this.file.size / 1000), 2)` links/KB
> **Content Depth**: `= choice(this.file.size < 500, "🌱 Stub", choice(this.file.size < 2000, "📄 Note", "📜 Article"))`
> **Update Frequency**: `= choice((date(today) - this.file.mtime).days < 7, "🔥 Active", choice((date(today) - this.file.mtime).days < 30, "👌 Regular", "❄️ Dormant"))`
> **Quality Score**: `= round((length(this.file.inlinks) * 2 + length(this.file.outlinks) + (this.file.size / 1000)) / 3, 1)`/10
```

**Use Case:** Quality monitoring, health checks, maintenance prioritization

### B. Temporal Tracking Panels

#### 62. **Time-Based Analytics**

```markdown
> [!calendar] Temporal Metrics
> **Created**: `= dateformat(this.file.ctime, "EEEE, MMMM dd, yyyy 'at' HH:mm")`
> **Age**: `= (date(today) - this.file.ctime).days` days (`= round((date(today) - this.file.ctime).days / 7, 1)` weeks)
> **Last Modified**: `= dateformat(this.file.mtime, "EEEE, MMMM dd, yyyy 'at' HH:mm")`
> **Days Since Edit**: `= (date(today) - this.file.mtime).days`
> **Edit Frequency**: `= round((date(today) - this.file.ctime).days / (this.review-count || 1), 1)` days/edit
> **Next Review**: `= this.next-review` (`= (this.next-review - date(today)).days` days)
```

**Use Case:** Temporal analysis, maintenance scheduling, activity tracking

---

## 💡 XIII. Creative & Experimental Patterns

### A. Serendipity & Discovery

> [!example] Serendipitous Navigation
> Create random connection opportunities to facilitate [[Zettelkasten]] exploration.

#### 63. **Random Discovery Prompts**

```markdown
**Random Outlink**: `= this.file.outlinks[floor(random() * length(this.file.outlinks))]`
**Random Inlink**: `= this.file.inlinks[floor(random() * length(this.file.inlinks))]`
**Random Tag**: `= this.file.tags[floor(random() * length(this.file.tags))]`
**Surprise Connection**: `= choice(random() > 0.5, this.file.outlinks[0], this.file.inlinks[0])`
```

**Use Case:** Serendipitous discovery, random exploration, connection finding

#### 64. **Discovery Metrics**

```markdown
**Connection Potential**: `= length(this.file.outlinks) * length(this.file.inlinks)`
**Unexplored Links**: `= length(filter(this.file.outlinks, l => !contains(this.file.inlinks, l)))`
**Bidirectional Connections**: `= length(filter(this.file.outlinks, l => contains(this.file.inlinks, l)))`
```

**Use Case:** Link analysis, connection opportunities, graph exploration

### B. Experimental Composite Scores

#### 65. **Custom Ranking Systems**

```markdown
**Note Value Score**: `= round((length(this.file.inlinks) * 5 + length(this.file.outlinks) * 2 + this.review-count * 10 + (this.file.size / 1000) * 3) / 20, 1)`
**Influence Score**: `= round(length(this.file.inlinks) * log(length(this.file.outlinks) + 1), 2)`
**Activity Index**: `= round((this.review-count + length(this.file.inlinks) + length(this.file.outlinks)) / ((date(today) - this.file.ctime).days || 1) * 100, 1)`
```

**Use Case:** Custom ranking, prioritization algorithms, value assessment

#### 66. **Predictive Metrics**

```markdown
**Days Until Stale**: `= choice((date(today) - this.file.mtime).days < 30, 30 - (date(today) - this.file.mtime).days, "Already Stale")`
**Projected Links**: `= round(length(this.file.outlinks) * ((date(today) - this.file.ctime).days / 30), 1)`
**Growth Rate**: `= round((this.file.size - (this.initial-size || 1000)) / ((date(today) - this.file.ctime).days || 1), 1)` bytes/day
```

**Use Case:** Trend analysis, growth tracking, predictive modeling

---

## 🔗 Related Topics for PKB Expansion

1. **[[DataviewJS Advanced Patterns]]**
   - *Connection*: DataviewJS provides programmatic query capabilities beyond inline syntax
   - *Depth Potential*: Complex filtering, custom rendering, dynamic dashboard generation
   - *Knowledge Graph Role*: Advanced automation layer for [[Dashboard Design]]

2. **[[Templater Integration with Dataview]]**
   - *Connection*: Combining [[Templater]] dynamic content generation with Dataview queries
   - *Depth Potential*: Template-time vs render-time query execution, macro patterns
   - *Knowledge Graph Role*: Template automation architecture in [[PKB Architecture]]

3. **[[Meta Bind Reactive Fields]]**
   - *Connection*: Interactive metadata manipulation that triggers Dataview updates
   - *Depth Potential*: Button actions, input fields, view fields integrated with inline queries
   - *Knowledge Graph Role*: Interactive dashboard components in [[Obsidian]] automation

4. **[[Knowledge Graph Analytics Formulas]]**
   - *Connection*: Advanced metrics for measuring [[Knowledge Graph]] health and structure
   - *Depth Potential*: PageRank-inspired algorithms, clustering coefficients, betweenness centrality
   - *Knowledge Graph Role*: Quantitative analysis of [[Zettelkasten]] network properties

---

> [!important] Usage Notes
> - **Performance**: Inline queries are evaluated each time the note is viewed. For large vaults, minimize complex calculations in frequently accessed notes.
> - **Fallback Values**: Always use `||` operator for properties that might be missing to prevent query failures.
> - **Date Formats**: Use `dateformat()` for consistent temporal displays across your vault.
> - **Testing**: Test complex inline queries in scratch notes before deploying to production templates.
> - **Documentation**: Comment inline queries in templates to explain calculation logic for future reference.

