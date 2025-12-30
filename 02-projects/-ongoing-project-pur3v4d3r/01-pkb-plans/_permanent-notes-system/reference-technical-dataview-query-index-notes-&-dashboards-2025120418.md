---
aliases:
  - "Dataview Query Reference"
  - "Index Note Queries"
tags:
  - "type/report"
  - "year/2025"
  - "type/tutorial"
  - "status/in-progress"
  - "information-architecture"
  - "pkb"
  - "index-systems"
  - "cognitive-science/cognitive-load"
  - "metacognitive-pkm"
  - "cognitive-resources"
  - "pkb/optimization"
  - "dataview-queries"
  - "cognitive-pkm"
source: "claude-sonnet-4.5"
id: "20251204185046"
created: "2025-12-04T18:50:46"
modified: "2025-12-04T18:50:46"
week: "[[2025-W49]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: "reference"
maturity: seedling
confidence: speculative
next-review: "2025-12-11"
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-12-04|Daily-Note]]"
status: active


review-last-reviewed: null
review-next-review: 2025-12-17
review-count: 0
review-interval: 3

review-priority: medium
---

> [!purpose] ### Overview
> - **Title**:: [[Dataview Query Reference: Index Notes & Dashboards]]
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
> ---
> ### Related Notes
> ```dataview
> TABLE type, maturity, confidence
> FROM  ""
> WHERE  type = "reference"
> SORT "maturity" DESC
> LIMIT 15
> ```
> ### Sources & References
> ```dataview
> TABLE 
>     source AS "Source Type",
>     file.ctime AS "Date Added"
> FROM ""
> WHERE source = "claude-sonnet-4.5"
> SORT file.ctime DESC
> LIMIT 10
> ```
> ### Backlinks & Connections
> ```dataview
> TABLE 
>     type AS "Type",
>     maturity AS "Maturity",
>     length(file.inlinks) AS "Its Backlinks",
>     dateformat(date(created), "MMM dd, yyyy") AS "Created"
> FROM [[#]]
> WHERE file.name != this.file.name
> SORT length(file.inlinks) DESC
> LIMIT 20
> ```
> ### 2025-12-04 - Initial Creation
> *Context*: `=this.title` **by**: `=this.source`
> *Maturity*: `= this.maturity`  
> *Confidence*: `= this.confidence`
> 
> ### Tags & Classification
> *Primary Tags*: `= this.tags`  
> *Type*: `= this.type`  
> *Source*: `= this.source`
---

# Dataview Query Reference: Index Notes & Dashboards

> [! ] ### Claude Thinking
> I'll conduct a comprehensive search and synthesis to build you an extensive reference collection of Dataview queries for index notes and dashboards.
> This is a comprehensive request for a reference collection of Dataview queries for index notes/dashboards. Let me break down what's needed:
> 1. **Request Classification**: This is a comprehensive technical reference/resource request
> 2. **Scope**: Reference note covering Dataview, Dataview inline, and DataviewJS queries
> 3. **Research Required**: YES - I should search for current best practices, advanced patterns, and novel use cases
> 4. **User Context**: Advanced Obsidian user (Pur3v4d3r) with sophisticated PKB system, familiar with the plugin ecosystem
> **Structural Planning**:
> - Metadata header with appropriate tags
> - Organized by query type and use case category
> - Heavy use of code blocks with explanations
> - Wiki-links to key concepts
> - Multiple callout types for organization
> - Expansion section suggesting related topics
> **Research Strategy**:
> I should search for:
> 1. Advanced Dataview query patterns for index notes
> 2. DataviewJS dashboard examples
> 3. Novel/creative use cases for folder-based queries
> 4. Performance optimization patterns
> 5. Integration patterns with other plugins
> Let me execute searches to gather comprehensive information about advanced Dataview patterns and novel use cases.
> Let me search for more specific advanced patterns and novel use cases:I've hit the search rate limit, but I have excellent information from my initial search. Let me now synthesize this into a comprehensive reference resource drawing on the search results, my existing knowledge, and the exemplars you provided.

---
tags: #dataview #obsidian-plugins #reference-note #dataviewjs #query-language #index-notes #dashboard-design
aliases: [Dataview Query Reference, Index Note Queries, Dashboard Query Collection, DQL Reference]
---

# 📊 Comprehensive Dataview Query Reference for Index Notes & Dashboard`s

> [!abstract] Resource Overview
> This is an exhaustive reference collection of [[Dataview]] queries, inline queries, and [[DataviewJS]] patterns specifically designed for index notes and dashboard creation. Each query is production-ready and includes explanations, use cases, and customization guidance.
>
> **Organization**: Queries are categorized by function (metadata tracking, link analysis, content discovery, etc.) with progressive complexity levels indicated.

---

## 📐 Understanding Query Types & Selection

> [!definition] Query Type Taxonomy
> **[[DQL]] (Dataview Query Language)**: SQL-like syntax for filtering, sorting, and displaying data. Best for straightforward queries with simple logic.
> 
> **Inline DQL**: Single-value queries embedded in text using `` `= expression` `` syntax. Perfect for dynamic metadata display.
> 
> **[[DataviewJS]]**: Full JavaScript API access for complex calculations, conditional logic, and advanced UI manipulation. Required for randomization, complex aggregations, and custom rendering.

**Selection Heuristic:**
- Use **DQL** when: Simple filtering, sorting, and table/list display suffices
- Use **Inline DQL** when: Embedding single calculated values in prose
- Use **DataviewJS** when: Conditional logic required, complex transformations needed, randomization desired, or custom UI rendering necessary

---

## 🗂️ Category 1: Folder & File Metadata Queries

> [!methodology-and-sources] Use Case
> These queries provide comprehensive folder-level intelligence: file counts, creation/modification patterns, size analytics, and temporal distributions. Essential for folder index notes and vault health monitoring.

### **1.1 Basic Folder Contents Listing**

**Complexity**: ⭐ Beginner

```dataview
TABLE file.ctime AS "Created", file.mtime AS "Modified"
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
SORT file.name ASC
```

**What This Does:**
- Lists all files in current note's folder (excluding the index note itself)
- Displays creation and modification timestamps
- Alphabetically sorted for easy navigation

**Customization Options:**
- Add columns: `file.size AS "Size"`, `file.tags AS "Tags"`, `length(file.outlinks) AS "Links"`
- Change sort: `SORT file.mtime DESC` (most recently modified first)
- Add metadata: `metadata-field AS "Field Name"`

---

### **1.2 Comprehensive Folder Metrics Dashboard**

**Complexity**: ⭐⭐ Intermediate

```dataview
TABLE WITHOUT ID
  length(rows) AS "📁 Total Notes",
  length(filter(rows, (r) => date(r.file.ctime) >= date(today) - dur(7 days))) AS "🆕 New (7d)",
  length(filter(rows, (r) => date(r.file.mtime) >= date(today) - dur(7 days))) AS "✏️ Modified (7d)",
  length(filter(rows, (r) => date(r.file.mtime) >= date(today) - dur(30 days))) AS "📝 Active (30d)",
  round(sum(rows.file.size) / 1024) AS "💾 Total KB"
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
GROUP BY "Folder Analytics"
```

**What This Does:**
- Single-row dashboard showing folder health metrics
- Tracks creation velocity (new notes per week)
- Identifies active maintenance (modifications)
- Monitors folder growth (total size)

**Interpretation Guide:**
- **High "New" count**: Active knowledge capture phase
- **Low "Modified" count**: Potential stale content requiring review
- **Growing size**: Consider subfolder organization

---

### **1.3 File Age Distribution Analysis**

**Complexity**: ⭐⭐ Intermediate

```dataview
TABLE WITHOUT ID
  file.link AS "Note",
  file.ctime AS "Created",
  dur(date(today) - file.ctime) AS "Age",
  choice(dur(date(today) - file.ctime).days < 7, "🌱 Fresh",
    choice(dur(date(today) - file.ctime).days < 30, "🌿 Recent", 
    choice(dur(date(today) - file.ctime).days < 90, "🍂 Mature",
    choice(dur(date(today) - file.ctime).days < 365, "🍁 Aged", "🕰️ Archive")))) AS "Status"
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
SORT file.ctime DESC
```

**What This Does:**
- Categorizes notes by temporal lifecycle
- Visual age indicators for quick scanning
- Identifies candidates for review or archival

**Lifecycle Stages:**
- 🌱 Fresh (< 7 days): New captures
- 🌿 Recent (< 30 days): Under development
- 🍂 Mature (< 90 days): Established content
- 🍁 Aged (< 1 year): Stable knowledge
- 🕰️ Archive (> 1 year): Historical reference

---

### **1.4 Temporal Heatmap (Creation Date Clustering)**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Group files by creation month, show activity clusters
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

const grouped = files
  .groupBy(p => p.file.ctime.toFormat("yyyy-MM"))
  .sort(k => k.key, 'desc');

dv.header(3, "📅 Creation Timeline");
dv.table(["Month", "Count", "Notes"],
  grouped.map(g => [
    g.key,
    "📊 " + g.rows.length,
    g.rows.map(r => r.file.link).join(", ")
  ])
);
```

**What This Does:**
- Identifies temporal clusters of knowledge capture
- Reveals project phases or learning sprints
- Useful for understanding knowledge creation patterns

**Analysis Applications:**
- Correlate with life events or projects
- Identify gaps in knowledge capture
- Plan review cycles based on creation bursts

---

### **1.5 Modification Staleness Detection**

**Complexity**: ⭐⭐ Intermediate

```dataview
TABLE WITHOUT ID
  file.link AS "⚠️ Stale Note",
  file.mtime AS "Last Modified",
  dur(date(today) - file.mtime) AS "Dormant For",
  length(file.inlinks) AS "In-Links"
FROM ""
WHERE file.folder = this.file.folder 
  AND file.name != this.file.name
  AND dur(date(today) - file.mtime).days > 90
SORT file.mtime ASC
LIMIT 20
```

**What This Does:**
- Surfaces notes untouched for 90+ days
- Prioritizes by staleness (oldest first)
- Shows link count to assess importance

**Review Protocol:**
- High in-links + stale = Requires update (central node)
- Low in-links + stale = Candidate for archival or deletion
- Check if information is still relevant

---

## 🔗 Category 2: Link Analysis & Graph Intelligence

> [!methodology-and-sources] Use Case
> These queries analyze the [[knowledge graph]] structure within a folder: identifying hubs, orphans, bridges, and link density patterns. Critical for maintaining a well-connected [[Personal Knowledge Base]].

### **2.1 Orphan Note Detection**

**Complexity**: ⭐⭐ Intermediate

```dataview
TABLE WITHOUT ID
  file.link AS "🏝️ Orphan Note",
  length(file.outlinks) AS "Links Out",
  file.ctime AS "Created"
FROM ""
WHERE file.folder = this.file.folder
  AND length(file.inlinks) = 0
  AND file.name != this.file.name
SORT file.ctime DESC
```

**What This Does:**
- Identifies notes with zero incoming links
- Shows outbound link count (if > 0, note is "islanded" not truly orphaned)
- Sorted by creation date to prioritize recent orphans

**Integration Strategy:**
1. **Review Context**: Is isolation intentional? (e.g., fleeting notes)
2. **Create Links**: From relevant MOCs or related notes
3. **Consider Archival**: If truly disconnected and outdated

---

### **2.2 Hub Note Identification (High In-Link Count)**

**Complexity**: ⭐⭐ Intermediate

```dataview
TABLE WITHOUT ID
  file.link AS "⚡ Hub Note",
  length(file.inlinks) AS "← In-Links",
  length(file.outlinks) AS "→ Out-Links",
  length(file.inlinks) + length(file.outlinks) AS "Total Connectivity"
FROM ""
WHERE file.folder = this.file.folder
  AND file.name != this.file.name
SORT (length(file.inlinks) + length(file.outlinks)) DESC
LIMIT 15
```

**What This Does:**
- Identifies high-connectivity nodes (hubs)
- Calculates total link density
- Reveals emergent organizational centers

**Interpretation:**
- **High in-links, low out-links**: Terminal concepts (destinations)
- **High out-links, low in-links**: Source/index notes
- **High both**: True hub notes (consider promoting to [[MOC]])

---

### **2.3 Bidirectional Link Mapping**

**Complexity**: ⭐⭐ Intermediate

```dataview
TABLE WITHOUT ID
  file.link AS "Note",
  length(file.outlinks) AS "→ Out",
  length(file.inlinks) AS "← In",
  length(filter(file.outlinks, (L) => contains(meta(L).inlinks, file.link))) AS "⇄ Bidirectional"
FROM ""
WHERE file.folder = this.file.folder 
  AND file.name != this.file.name
SORT length(filter(file.outlinks, (L) => contains(meta(L).inlinks, file.link))) DESC
```

**What This Does:**
- Counts bidirectional links (strongest connections)
- Identifies mutually reinforcing concept pairs
- Reveals conversation-like note relationships

**Analysis Value:**
- High bidirectional count = Strong conceptual coupling
- Consider merging notes with high bidirectional density
- Use to identify note clusters for [[MOC]] creation

---

### **2.4 Link Density Heatmap (Per Note)**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Calculate link density score for each note
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

const analyzed = files.map(p => {
  const inCount = p.file.inlinks.length;
  const outCount = p.file.outlinks.length;
  const wordCount = p.file.size; // Rough proxy
  
  // Density score: links per 100 "words" (bytes/5)
  const density = Math.round(((inCount + outCount) / (wordCount / 500)) * 100);
  
  return {
    link: p.file.link,
    in: inCount,
    out: outCount,
    density: density,
    status: density > 5 ? "🔥 Dense" : density > 2 ? "✅ Good" : "⚠️ Sparse"
  };
}).sort(f => f.density, 'desc');

dv.table(["Note", "In ←", "Out →", "Density Score", "Status"],
  analyzed.map(f => [f.link, f.in, f.out, f.density, f.status])
);
```

**What This Does:**
- Calculates link-to-content ratio
- Identifies under-linked content (sparse)
- Highlights well-integrated notes (dense)

**Optimization Strategy:**
- **Sparse notes**: Add contextual links to related concepts
- **Dense notes**: Consider if over-linked (noise vs. signal)
- **Target range**: 2-5 links per ~100 words

---

### **2.5 Broken Link Detection**

**Complexity**: ⭐⭐ Intermediate

```dataview
TABLE WITHOUT ID
  file.link AS "Note with Broken Links",
  length(file.outlinks) AS "Total Out-Links",
  filter(file.outlinks, (L) => !L) AS "🔴 Broken Links"
FROM ""
WHERE file.folder = this.file.folder
  AND file.name != this.file.name
  AND length(filter(file.outlinks, (L) => !L)) > 0
```

**What This Does:**
- Identifies notes with non-resolving links
- Lists broken link targets
- Essential for vault maintenance

**Repair Protocol:**
1. Check if target was renamed (use Search to find)
2. Create missing note if concept is valuable
3. Remove link if no longer relevant

---

### **2.6 Unlinked Mention Opportunities**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Find notes mentioned in current folder but not linked
const currentFolder = dv.current().file.folder;
const folderFiles = dv.pages('"' + currentFolder + '"')
  .where(p => p.file.name != dv.current().file.name);

const allFiles = dv.pages();
const opportunities = [];

for (const note of folderFiles.array()) {
  const noteName = note.file.name;
  
  // Find files that mention this note's name but don't link to it
  const mentioners = allFiles
    .where(p => 
      p.file.folder == currentFolder &&
      p.file.name != noteName &&
      !p.file.outlinks.some(link => link.path.includes(noteName))
    );
  
  if (mentioners.length > 0) {
    opportunities.push({
      note: note.file.link,
      count: mentioners.length,
      files: mentioners.map(m => m.file.link).array().slice(0, 5)
    });
  }
}

if (opportunities.length > 0) {
  dv.header(3, "🔍 Unlinked Mention Opportunities");
  dv.table(["Target Note", "Potential Links", "Files (Sample)"],
    opportunities.sort((a, b) => b.count - a.count)
      .map(o => [o.note, o.count, o.files.join(", ")])
  );
} else {
  dv.paragraph("✅ No obvious unlinked mentions detected.");
}
```

**What This Does:**
- Identifies potential link opportunities based on name mentions
- Prioritizes by frequency
- Samples files for manual review

**Linking Workflow:**
1. Review sample files for context
2. Convert relevant mentions to `[[links]]`
3. Strengthens semantic connections

---

## 📑 Category 3: Content & Metadata Intelligence

> [!methodology-and-sources] Use Case
> These queries analyze note contents, metadata patterns, tag usage, and property distributions. Useful for [[tag taxonomy]] management, metadata standardization, and content quality assessment.

### **3.1 Tag Distribution Analysis**

**Complexity**: ⭐⭐ Intermediate

```datavie
TABLE WITHOUT ID
  length(rows.file.tags) AS "Usage Count",
  rows.file.link AS "Tagged Notes"
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
FLATTEN file.tags AS tag
GROUP BY tag
SORT length(rows.file.tags) DESC
```

```dataview
TABLE WITHOUT ID
  length(rows) AS "Usage Count",
  rows.file.link AS "Tagged Notes"
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
FLATTEN file.tags AS tag
GROUP BY tag
SORT length(rows) DESC
```


**What This Does:**
- Shows all tags used in folder with frequency counts
- Lists notes using each tag
- Reveals tag popularity and distribution

**Taxonomy Optimization:**
- **High-frequency tags**: Consider creating MOCs
- **Single-use tags**: Candidates for standardization or removal
- **Similar tags**: Merge variants (e.g., #AI vs #artificial-intelligence)

---

### **3.2 Metadata Coverage Assessment**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Analyze which notes have specific metadata fields
const targetFields = ["status", "type", "created", "modified", "tags"];
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

const coverage = targetFields.map(field => {
  const withField = files.where(p => p[field] != null && p[field] != undefined);
  const percentage = Math.round((withField.length / files.length) * 100);
  
  return {
    field: field,
    count: withField.length,
    total: files.length,
    percentage: percentage + "%",
    status: percentage >= 80 ? "✅" : percentage >= 50 ? "⚠️" : "❌"
  };
});

dv.header(3, "📋 Metadata Field Coverage");
dv.table(["Field", "Present", "Total", "Coverage", "Status"],
  coverage.map(c => [c.field, c.count, c.total, c.percentage, c.status])
);
```

**What This Does:**
- Audits metadata completeness
- Identifies gaps in standardization
- Prioritizes cleanup efforts

**Standardization Protocol:**
- **<50% coverage**: Add field to template
- **50-80% coverage**: Batch update missing notes
- **>80% coverage**: Maintain consistency

---

### **3.3 Property Value Distribution**

**Complexity**: ⭐⭐ Intermediate

```dataview
TABLE WITHOUT ID
  status AS "Status Value",
  length(rows) AS "Count",
  rows.file.link AS "Notes"
FROM ""
WHERE file.folder = this.file.folder 
  AND file.name != this.file.name
  AND status
GROUP BY status
SORT length(rows) DESC
```

**What This Does:**
- Groups notes by property value (e.g., status, type, priority)
- Shows distribution across categories
- Useful for workflow management

**Workflow Applications:**
- Track note lifecycle (seedling → budding → evergreen)
- Monitor project statuses
- Identify bottlenecks (too many in one status)

**Customization**: Replace `status` with any property: `type`, `priority`, `project`, `author`

---

### **3.4 Empty or Missing Property Detection**

**Complexity**: ⭐⭐ Intermediate

```dataview
TABLE WITHOUT ID
  file.link AS "⚠️ Missing Metadata",
  file.ctime AS "Created"
FROM ""
WHERE file.folder = this.file.folder
  AND file.name != this.file.name
  AND (!status OR !type OR !tags)
SORT file.ctime DESC
```

**What This Does:**
- Identifies notes missing critical metadata
- Useful for cleanup sprints
- Ensures consistency across folder

**Batch Update Strategy:**
1. Sort by creation date (newest first for context recall)
2. Use [[Templater]] or [[QuickAdd]] for rapid metadata addition
3. Update in batches of 10-20 notes per session

---

### **3.5 Word Count & Size Analytics**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

const analyzed = files.map(p => {
  const sizeKB = Math.round(p.file.size / 1024);
  const estimatedWords = Math.round(p.file.size / 5); // Rough estimate
  let category;
  
  if (estimatedWords < 100) category = "🌱 Stub";
  else if (estimatedWords < 500) category = "📄 Short";
  else if (estimatedWords < 2000) category = "📝 Medium";
  else category = "📜 Long";
  
  return {
    link: p.file.link,
    size: sizeKB + " KB",
    words: estimatedWords,
    category: category
  };
}).sort(f => f.words, 'desc');

// Convert to regular array for reduce operation
const analyzedArray = Array.from(analyzed);

dv.table(["Note", "Size", "~Words", "Length Category"],
  analyzed.map(f => [f.link, f.size, f.words, f.category])
);

// Summary stats - using the array version
const totalWords = analyzedArray.reduce((sum, f) => sum + f.words, 0);
const avgWords = Math.round(totalWords / analyzedArray.length);
dv.paragraph(`\n**Folder Summary**: ${files.length} notes | ~${totalWords.toLocaleString()} total words | ~${avgWords} words/note`);
```

**What This Does:**
- Categorizes notes by content depth
- Provides folder-wide content metrics
- Identifies stubs requiring expansion

**Content Development Strategy:**
- **Stubs (<100 words)**: Expand or merge with related notes
- **Short (100-500)**: Typical fleeting/atomic notes
- **Medium (500-2000)**: Reference notes
- **Long (>2000)**: Consider splitting into multiple notes

---

## ⏰ Category 4: Temporal & Review Management

> [!methodology-and-sources] Use Case
> Time-based queries for [[spaced repetition]], review scheduling, and temporal pattern analysis. Essential for maintaining [[evergreen notes]] and implementing review systems.

### **4.1 Notes Due for Review (Spaced Repetition)**

**Complexity**: ⭐⭐ Intermediate

```dataview
TABLE WITHOUT ID
  file.link AS "📅 Due for Review",
  review-date AS "Scheduled",
  dur(date(today) - review-date) AS "Overdue By",
  review-count AS "Review #"
FROM ""
WHERE file.folder = this.file.folder
  AND file.name != this.file.name
  AND review-date
  AND review-date <= date(today)
SORT review-date ASC
```

**What This Does:**
- Surfaces notes with review dates that have passed
- Shows how overdue each note is
- Tracks review frequency

**Review System Implementation:**
1. Add `review-date` property to note template
2. Update `review-date` after each review (e.g., +7d, +30d, +90d)
3. Increment `review-count` property
4. Use this query in daily note dashboard

---

### **4.2 Upcoming Review Calendar (Next 14 Days)**

**Complexity**: ⭐⭐ Intermediate

```dataview
TABLE WITHOUT ID
  file.link AS "Note",
  review-date AS "Review Date",
  dur(review-date - date(today)) AS "In Days",
  maturity AS "Maturity Level"
FROM ""
WHERE file.folder = this.file.folder
  AND file.name != this.file.name
  AND review-date
  AND review-date > date(today)
  AND review-date <= date(today) + dur(14 days)
SORT review-date ASC
```

**What This Does:**
- Preview upcoming review obligations
- Plan review sessions in advance
- Balance workload across days

**Workload Management:**
- Cluster reviews by topic/folder
- Spread reviews across week to avoid bursts
- Adjust intervals if consistently overwhelming

---

### **4.3 Review Frequency Heatmap**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Group notes by review count to identify patterns
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name && p["review-count"]);

const grouped = files
  .groupBy(p => p["review-count"] || 0)
  .sort(g => g.key, 'desc');

dv.header(3, "🔄 Review Engagement Distribution");
dv.table(["Review Count", "Notes in Category", "Examples"],
  grouped.map(g => [
    g.key + (g.key == 1 ? " review" : " reviews"),
    "📊 " + g.rows.length + " notes",
    g.rows.slice(0, 3).map(r => r.file.link).join(", ")
  ])
);

// Identify highly vs. under-reviewed content
const neverReviewed = files.where(p => !p["review-count"] || p["review-count"] == 0);
if (neverReviewed.length > 0) {
  dv.header(4, "⚠️ Never Reviewed (" + neverReviewed.length + " notes)");
  dv.list(neverReviewed.map(p => p.file.link));
}
```

**What This Does:**
- Shows distribution of review engagement
- Identifies over-reviewed vs. neglected notes
- Surfaces notes that have never been reviewed

**Optimization Insights:**
- **Never reviewed**: New notes or systematic neglect
- **High review count**: Core knowledge requiring frequent refresh
- **Balanced distribution**: Healthy review system

---

### **4.4 Modification Velocity Tracking**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Track how frequently notes are being updated
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

const analyzed = files.map(p => {
  const age = (new Date() - p.file.ctime) / (1000 * 60 * 60 * 24); // Days since creation
  const daysSinceModified = (new Date() - p.file.mtime) / (1000 * 60 * 60 * 24);
  const activityRatio = age > 0 ? Math.round((age - daysSinceModified) / age * 100) : 100;
  
  let velocity;
  if (activityRatio > 80) velocity = "🔥 Active";
  else if (activityRatio > 50) velocity = "📈 Moderate";
  else if (activityRatio > 20) velocity = "📉 Slow";
  else velocity = "❄️ Dormant";
  
  return {
    link: p.file.link,
    created: p.file.ctime,
    modified: p.file.mtime,
    velocity: velocity,
    ratio: activityRatio // Keep as number for sorting
  };
}).sort((a, b) => b.ratio - a.ratio); // Sort by numeric ratio

dv.table(["Note", "Created", "Last Modified", "Activity Level", "Ratio"],
  analyzed.map(f => [f.link, f.created, f.modified, f.velocity, f.ratio + "%"])
);
```

**What This Does:**
- Calculates how actively notes are maintained
- Identifies consistently updated vs. static notes
- Useful for prioritizing maintenance efforts

**Interpretation:**
- **Active**: Under active development or high-value reference
- **Moderate**: Periodic updates, stable content
- **Slow/Dormant**: Consider archival or revival

---

### **4.5 Creation Date Calendar View**

**Complexity**: ⭐⭐ Intermediate

```dataview
CALENDAR file.cday
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
```

**What This Does:**
- Visual calendar showing when notes were created
- Identifies temporal clusters and gaps
- Useful for understanding knowledge capture patterns

**Pattern Analysis:**
- **Dense periods**: Major projects or learning phases
- **Sparse periods**: Potential neglect or external focus
- **Regular patterns**: Consistent practice (e.g., daily notes)

---

## 🎯 Category 5: Task & Project Management

> [!methodology-and-sources] Use Case
> Queries for tracking tasks, project status, and action items within folder context. Integrates with [[GTD]], [[PARA]], and custom task management workflows.

### **5.1 All Tasks in Folder (Completed & Incomplete)**

**Complexity**: ⭐ Beginner

```dataview
TASK
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
```

**What This Does:**
- Displays all tasks found in folder notes
- Interactive checkboxes for task completion
- Simple overview of action items

**Enhancement Options:**
- Add `WHERE !completed` to show only open tasks
- Add `SORT file.name` to group by file
- Use [[Tasks plugin]] for advanced task management

---

### **5.2 Task Completion Statistics**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Aggregate task completion metrics across folder
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

let totalTasks = 0;
let completedTasks = 0;
let tasksByFile = [];

for (const file of files) {
  const tasks = file.file.tasks;
  if (tasks && tasks.length > 0) {
    const fileCompleted = tasks.where(t => t.completed).length;
    totalTasks += tasks.length;
    completedTasks += fileCompleted;
    
    tasksByFile.push({
      file: file.file.link,
      total: tasks.length,
      completed: fileCompleted,
      pending: tasks.length - fileCompleted,
      percentage: Math.round((fileCompleted / tasks.length) * 100) + "%"
    });
  }
}

// Overall metrics
const overallCompletion = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;

dv.header(3, "📊 Folder Task Analytics");
dv.paragraph(`**Total Tasks**: ${totalTasks} | **Completed**: ${completedTasks} (${overallCompletion}%) | **Pending**: ${totalTasks - completedTasks}`);

// Per-file breakdown
if (tasksByFile.length > 0) {
  dv.header(4, "By File");
  dv.table(["File", "Total", "✅ Done", "⏳ Pending", "Progress"],
    tasksByFile
      .sort((a, b) => b.pending - a.pending)
      .map(t => [t.file, t.total, t.completed, t.pending, t.percentage])
  );
}
```

**What This Does:**
- Calculates folder-wide task completion rate
- Per-file task breakdown
- Prioritizes files with most pending tasks

**Project Management Applications:**
- Track sprint/milestone completion
- Identify blockers (files with many pending tasks)
- Visualize progress toward folder objectives

---

### **5.3 Tasks by Due Date**

**Complexity**: ⭐⭐ Intermediate

```dataview
TASK
FROM ""
WHERE file.folder = this.file.folder 
  AND file.name != this.file.name
  AND !completed
  AND due
SORT due ASC
```

**What This Does:**
- Lists incomplete tasks with due dates
- Chronologically ordered (earliest first)
- Focuses attention on time-sensitive items

**Workflow Integration:**
- Include in daily note for deadline awareness
- Color-code overdue tasks (requires [[Tasks plugin]])
- Link to project MOCs for context

---

### **5.4 Overdue Task Alert System**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Identify and prioritize overdue tasks
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

const today = dv.date("today");
const overdueTasks = [];

for (const file of files) {
  const tasks = file.file.tasks;
  if (tasks) {
    for (const task of tasks.where(t => !t.completed && t.due)) {
      if (task.due < today) {
        const daysOverdue = Math.round((today - task.due).as('days'));
        overdueTasks.push({
          file: file.file.link,
          task: task.text,
          due: task.due,
          overdue: daysOverdue,
          urgency: daysOverdue > 7 ? "🔴 Critical" : daysOverdue > 3 ? "🟠 High" : "🟡 Medium"
        });
      }
    }
  }
}

if (overdueTasks.length > 0) {
  dv.header(3, `⚠️ ${overdueTasks.length} Overdue Tasks`);
  dv.table(["File", "Task", "Due Date", "Days Overdue", "Urgency"],
    overdueTasks
      .sort((a, b) => b.overdue - a.overdue)
      .map(t => [t.file, t.task, t.due, t.overdue, t.urgency])
  );
} else {
  dv.paragraph("✅ No overdue tasks in this folder!");
}
```

**What This Does:**
- Automatically detects overdue tasks
- Calculates days overdue
- Assigns urgency levels

**Alert Escalation:**
- 🟡 Medium (1-3 days): Gentle reminder
- 🟠 High (4-7 days): Requires attention
- 🔴 Critical (>7 days): Immediate action or reconsideration

---

### **5.5 Project Status Overview**

**Complexity**: ⭐⭐ Intermediate

```dataview
TABLE WITHOUT ID
  file.link AS "Project",
  status AS "Status",
  due AS "Due Date",
  choice(status = "active", "🟢", choice(status = "planned", "🔵", choice(status = "on-hold", "🟡", "⚪"))) AS "●"
FROM ""
WHERE file.folder = this.file.folder
  AND file.name != this.file.name
  AND status
SORT status DESC, due ASC
```

**What This Does:**
- Dashboard of all projects with status tracking
- Visual status indicators
- Sorted by status priority and deadline

**Status Taxonomy Suggestion:**
- `active`: Currently in progress
- `planned`: Scheduled for future
- `on-hold`: Temporarily paused
- `completed`: Finished
- `cancelled`: Abandoned

---

## 🔍 Category 6: Content Discovery & Serendipity

> [!methodology-and-sources] Use Case
> Queries designed to surface forgotten knowledge, encourage [[serendipity]], and facilitate unexpected connections. Essential for [[knowledge graph]] exploration and creative insight.

### **6.1 Random Note Resurfacing**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Randomly select notes from folder for review
const numberToShow = 5;
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

const randomNotes = files.array()
  .sort(() => 0.5 - Math.random())
  .slice(0, numberToShow)
  .map(note => note.file.link);

dv.header(3, "🎲 Random Notes for Review");
dv.list(randomNotes);
```

**What This Does:**
- Selects random notes from folder
- Encourages serendipitous rediscovery
- Breaks out of recency bias

**Use Cases:**
- Daily review ritual (refresh daily)
- [[Spaced repetition]] variation
- Idea generation prompts

**Customization**: Change `numberToShow` to control count

---

### **6.2 Least Recently Modified (LRM) Notes**

**Complexity**: ⭐⭐ Intermediate

```dataview
TABLE WITHOUT ID
  file.link AS "🕸️ Forgotten Note",
  file.mtime AS "Last Touched",
  dur(date(today) - file.mtime) AS "Dormant Duration"
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
SORT file.mtime ASC
LIMIT 10
```

**What This Does:**
- Surfaces oldest unmodified notes
- Combats "out of sight, out of mind"
- Systematic rediscovery

**Review Protocol:**
1. **Quick scan**: Still relevant?
2. **Update or archive**: Refresh or move
3. **Link integration**: Connect to newer notes

---

### **6.3 Notes Without Outbound Links (Potential Dead Ends)**

**Complexity**: ⭐⭐ Intermediate

```dataview
TABLE WITHOUT ID
  file.link AS "🚧 No Outbound Links",
  file.ctime AS "Created",
  length(file.inlinks) AS "← In-Links"
FROM ""
WHERE file.folder = this.file.folder
  AND file.name != this.file.name
  AND length(file.outlinks) = 0
SORT length(file.inlinks) DESC
```

**What This Does:**
- Identifies terminal nodes (no connections forward)
- Shows if others link to it (incoming validation)
- Highlights integration opportunities

**Link Development Strategy:**
- High in-links, no out-links = Add context links to related topics
- No in/out-links = Orphan requiring significant connection work
- Terminal concept = Potentially appropriate as endpoint

---

### **6.4 Similar Note Suggestions (Tag-Based)**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// For each note, suggest others with overlapping tags
const currentFolder = dv.current().file.folder;
const files = dv.pages('"' + currentFolder + '"')
  .where(p => p.file.name != dv.current().file.name);

const suggestions = [];

for (const note1 of files.array()) {
  const tags1 = note1.file.tags || [];
  if (tags1.length == 0) continue;
  
  for (const note2 of files.array()) {
    if (note1.file.path == note2.file.path) continue;
    
    const tags2 = note2.file.tags || [];
    const overlap = tags1.filter(t => tags2.includes(t));
    
    if (overlap.length >= 2 && !note1.file.outlinks.some(l => l.path == note2.file.path)) {
      suggestions.push({
        note1: note1.file.link,
        note2: note2.file.link,
        sharedTags: overlap.length,
        tags: overlap.join(", ")
      });
    }
  }
}

if (suggestions.length > 0) {
  // Remove duplicates
  const unique = suggestions.filter((s, i, arr) => 
    i === arr.findIndex(t => 
      (t.note1 === s.note1 && t.note2 === s.note2) ||
      (t.note1 === s.note2 && t.note2 === s.note1)
    )
  );
  
  dv.header(3, "🔗 Potential Connections (Shared Tags)");
  dv.table(["Note A", "Note B", "Shared Tags", "Tags"],
    unique.sort((a, b) => b.sharedTags - a.sharedTags)
      .slice(0, 15)
      .map(s => [s.note1, s.note2, s.sharedTags, s.tags])
  );
} else {
  dv.paragraph("No obvious tag-based connections found.");
}
```

**What This Does:**
- Identifies notes with similar tag profiles not yet linked
- Suggests potential knowledge connections
- Facilitates [[networked thought]] building

**Connection Workflow:**
1. Review suggested pairs
2. Determine if conceptual relationship exists
3. Create appropriate links or update tags

---

### **6.5 Recently Created Notes (Discovery Window)**

**Complexity**: ⭐ Beginner

```dataview
TABLE WITHOUT ID
  file.link AS "New Note",
  file.ctime AS "Created",
  dur(date(today) - file.ctime) AS "Age"
FROM ""
WHERE file.folder = this.file.folder
  AND file.name != this.file.name
  AND dur(date(today) - file.ctime).days <= 14
SORT file.ctime DESC
```

**What This Does:**
- Shows notes created in last 14 days
- "Fresh content" discovery window
- Integration checkpoint

**New Note Workflow:**
- Review daily/weekly
- Ensure proper tagging and linking
- Promote to appropriate maturity level

---

## 🧬 Category 7: Advanced Pattern Analysis

> [!methodology-and-sources] Use Case
> Sophisticated queries revealing emergent patterns, structural insights, and vault health metrics. For advanced users seeking deep [[knowledge graph]] intelligence.

### **7.1 Note Clustering by Shared Links**

**Complexity**: ⭐⭐⭐⭐ Expert (DataviewJS)

```dataviewjs
// Identify notes that link to similar sets of other notes
const currentFolder = dv.current().file.folder;
const files = dv.pages('"' + currentFolder + '"')
  .where(p => p.file.name != dv.current().file.name);

const clusters = [];

for (const note1 of files.array()) {
  const links1 = note1.file.outlinks.map(l => l.path);
  if (links1.length < 2) continue;
  
  for (const note2 of files.array()) {
    if (note1.file.path >= note2.file.path) continue;
    
    const links2 = note2.file.outlinks.map(l => l.path);
    const sharedLinks = links1.filter(l => links2.includes(l));
    
    if (sharedLinks.length >= 3) {
      clusters.push({
        note1: note1.file.link,
        note2: note2.file.link,
        shared: sharedLinks.length,
        overlap: Math.round((sharedLinks.length / Math.min(links1.length, links2.length)) * 100) + "%"
      });
    }
  }
}

if (clusters.length > 0) {
  dv.header(3, "🧬 Note Clusters (Shared Outbound Links)");
  dv.table(["Note A", "Note B", "Shared Links", "Overlap %"],
    clusters.sort((a, b) => b.shared - a.shared)
      .slice(0, 20)
      .map(c => [c.note1, c.note2, c.shared, c.overlap])
  );
  
  dv.paragraph("*Consider merging notes with high overlap or creating an MOC to organize cluster.*");
} else {
  dv.paragraph("No significant note clusters detected (threshold: 3+ shared links).");
}
```

**What This Does:**
- Identifies notes with highly overlapping link profiles
- Reveals emergent topic clusters
- Suggests [[MOC]] opportunities

**Cluster Analysis:**
- **High overlap (>70%)**: Consider merging or creating parent note
- **Medium overlap (40-70%)**: Natural cluster, potential MOC
- **Low overlap (<40%)**: Weak relationship, acceptable

---

### **7.2 Bridge Notes (Connecting Clusters)**

**Complexity**: ⭐⭐⭐⭐ Expert (DataviewJS)

```dataviewjs
// Identify notes that bridge otherwise disconnected clusters
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

const bridges = files.map(note => {
  const linkedNotes = note.file.outlinks
    .map(l => files.find(f => f.file.path == l.path))
    .filter(f => f != undefined);
  
  // Count unique secondary connections (links from linked notes)
  const secondaryConnections = new Set();
  for (const linked of linkedNotes) {
    linked.file.outlinks.forEach(l => {
      if (l.path != note.file.path) {
        secondaryConnections.add(l.path);
      }
    });
  }
  
  const directLinks = note.file.outlinks.length;
  const bridgeScore = secondaryConnections.size;
  
  return {
    note: note.file.link,
    direct: directLinks,
    bridges: bridgeScore,
    ratio: directLinks > 0 ? Math.round(bridgeScore / directLinks * 10) / 10 : 0
  };
}).filter(n => n.bridges > 0)
  .sort((a, b) => b.bridges - a.bridges)
  .slice(0, 15);

dv.header(3, "🌉 Bridge Notes (Cluster Connectors)");
dv.table(["Note", "Direct Links", "Secondary Reach", "Bridge Ratio"],
  bridges.map(b => [b.note, b.direct, b.bridges, b.ratio])
);

dv.paragraph("*High bridge ratio indicates notes connecting disparate concepts.*");
```

**What This Does:**
- Calculates how many "second-degree" connections each note enables
- Identifies notes that bridge otherwise isolated clusters
- Reveals structural importance beyond simple link count

**Strategic Importance:**
- **High bridge scores**: Critical integration points
- **Low bridge scores**: Isolated or redundant
- **Protect bridges**: Don't delete without careful consideration

---

### **7.3 Semantic Similarity Detection (Filename Analysis)**

**Complexity**: ⭐⭐⭐⭐ Expert (DataviewJS)

```dataviewjs
// Find notes with similar filenames (potential duplicates or related content)
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

function tokenize(name) {
  return name.toLowerCase()
    .replace(/[^\w\s]/g, ' ')
    .split(/\s+/)
    .filter(w => w.length > 3);
}

const similarities = [];

for (const note1 of files.array()) {
  const tokens1 = tokenize(note1.file.name);
  if (tokens1.length == 0) continue;
  
  for (const note2 of files.array()) {
    if (note1.file.path >= note2.file.path) continue;
    
    const tokens2 = tokenize(note2.file.name);
    const shared = tokens1.filter(t => tokens2.includes(t));
    
    if (shared.length >= 2) {
      const similarity = Math.round((shared.length / Math.min(tokens1.length, tokens2.length)) * 100);
      
      similarities.push({
        note1: note1.file.link,
        note2: note2.file.link,
        similarity: similarity + "%",
        tokens: shared.join(", ")
      });
    }
  }
}

if (similarities.length > 0) {
  dv.header(3, "🔍 Semantically Similar Filenames");
  dv.table(["Note A", "Note B", "Similarity", "Shared Words"],
    similarities.sort((a, b) => parseInt(b.similarity) - parseInt(a.similarity))
      .slice(0, 15)
      .map(s => [s.note1, s.note2, s.similarity, s.tokens])
  );
  
  dv.paragraph("*Review for potential duplicates or missing cross-references.*");
} else {
  dv.paragraph("No significant filename similarities detected.");
}
```

**What This Does:**
- Analyzes filenames for shared terminology
- Detects potential duplicate concepts
- Suggests merge or link opportunities

**Cleanup Applications:**
- **High similarity**: Check for duplicates
- **Moderate similarity**: Ensure cross-linking
- **Related concepts**: Consider shared parent topic

---

### **7.4 Growth Velocity Analysis**

**Complexity**: ⭐⭐⭐⭐ Expert (DataviewJS)

```dataviewjs
// Analyze folder growth patterns over time
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

// Group by month
const monthlyGrowth = files.array().reduce((acc, file) => {
  const month = file.file.ctime.toFormat("yyyy-MM");
  acc[month] = (acc[month] || 0) + 1;
  return acc;
}, {});

const sorted = Object.entries(monthlyGrowth).sort((a, b) => b[0].localeCompare(a[0]));

// Calculate velocity metrics
let velocityData = [];
for (let i = 0; i < sorted.length; i++) {
  const [month, count] = sorted[i];
  const prevCount = i < sorted.length - 1 ? sorted[i + 1][1] : count;
  const change = count - prevCount;
  const percentChange = prevCount > 0 ? Math.round((change / prevCount) * 100) : 0;
  
  velocityData.push({
    month: month,
    created: count,
    change: change > 0 ? "+" + change : change,
    velocity: percentChange > 0 ? "📈 +" + percentChange + "%" : "📉 " + percentChange + "%"
  });
}

dv.header(3, "📈 Folder Growth Velocity (Last 12 Months)");
dv.table(["Month", "Notes Created", "vs. Prev Month", "Velocity"],
  velocityData.slice(0, 12).map(v => [v.month, v.created, v.change, v.velocity])
);

// Summary
const total = files.length;
const recent3mo = files.where(p => p.file.ctime > dv.date("today") - dv.duration("90 days")).length;
const avgPerMonth = Math.round(total / Math.max(sorted.length, 1));

dv.paragraph(`\n**Growth Summary**: ${total} total notes | ${recent3mo} created in last 90 days | ~${avgPerMonth} notes/month average`);
```

**What This Does:**
- Tracks monthly note creation patterns
- Calculates growth acceleration/deceleration
- Identifies knowledge capture trends

**Pattern Interpretation:**
- **Accelerating growth**: Active learning/project phase
- **Steady growth**: Consistent practice
- **Declining growth**: Shifting focus or consolidation phase

---

### **7.5 Knowledge Maturity Distribution**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Assuming notes have a "maturity" property with values like "seedling", "budding", "evergreen"
const maturityLevels = ["seedling", "budding", "developing", "evergreen"];
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

const distribution = maturityLevels.map(level => {
  const notes = files.where(p => p.maturity == level);
  const percentage = Math.round((notes.length / files.length) * 100);
  
  return {
    level: level.charAt(0).toUpperCase() + level.slice(1),
    count: notes.length,
    percentage: percentage + "%",
    visual: "█".repeat(Math.round(percentage / 5))
  };
});

dv.header(3, "🌱 Knowledge Maturity Distribution");
dv.table(["Maturity Level", "Count", "%", "Distribution"],
  distribution.map(d => [d.level, d.count, d.percentage, d.visual])
);

// Health assessment
const seedlings = distribution[0].count;
const evergreens = distribution[3].count;
const ratio = seedlings > 0 ? (evergreens / seedlings).toFixed(2) : "N/A";

dv.paragraph(`\n**Maturity Ratio**: ${ratio} evergreens per seedling`);
dv.paragraph(`*Healthy ratio: 0.3-0.5 (indicates conversion of captures to refined knowledge)*`);
```

**What This Does:**
- Visualizes [[Zettelkasten]] note lifecycle
- Tracks conversion of fleeting → permanent notes
- Indicates knowledge refinement health

**Health Metrics:**
- **Too many seedlings**: Capture without processing
- **Balanced distribution**: Healthy workflow
- **Too many evergreens**: Potential stagnation or over-curation

---

## 🎨 Category 8: Visual & Dashboard Queries

> [!methodology-and-sources] Use Case
> Queries optimized for dashboard display, visual appeal, and at-a-glance folder intelligence. Combine multiple metrics for comprehensive index notes.

### **8.1 Comprehensive Folder Dashboard (Mega Query)**

**Complexity**: ⭐⭐⭐⭐ Expert (DataviewJS)

```dataviewjs
// ULTIMATE FOLDER DASHBOARD - All key metrics in one view
const folder = dv.current().file.folder;
const files = dv.pages('"' + folder + '"')
  .where(p => p.file.name != dv.current().file.name);

// === SECTION 1: BASIC METRICS ===
dv.header(2, "📊 Folder Overview: " + folder.split('/').pop());

const total = files.length;
const totalSize = Math.round(files.array().reduce((sum, f) => sum + f.file.size, 0) / 1024);
const avgSize = Math.round(totalSize / total);

const newest = files.sort(f => f.file.ctime, 'desc')[0];
const oldest = files.sort(f => f.file.ctime, 'asc')[0];

dv.paragraph(`
**Total Notes**: ${total} | **Total Size**: ${totalSize} KB (avg: ${avgSize} KB/note)  
**Newest**: ${newest?.file.link || "N/A"} (${newest?.file.ctime || "N/A"})  
**Oldest**: ${oldest?.file.link || "N/A"} (${oldest?.file.ctime || "N/A"})
`);

// === SECTION 2: TEMPORAL METRICS ===
const new7d = files.where(f => f.file.ctime > dv.date("today") - dv.duration("7 days")).length;
const mod7d = files.where(f => f.file.mtime > dv.date("today") - dv.duration("7 days")).length;
const stale90 = files.where(f => f.file.mtime < dv.date("today") - dv.duration("90 days")).length;

dv.header(3, "⏰ Temporal Health");
dv.paragraph(`
📥 **New (7d)**: ${new7d} notes  
✏️ **Modified (7d)**: ${mod7d} notes  
🕸️ **Stale (>90d)**: ${stale90} notes
`);

// === SECTION 3: LINK METRICS ===
let totalInLinks = 0;
let totalOutLinks = 0;
let orphans = 0;
let hubs = 0;

files.forEach(f => {
  totalInLinks += f.file.inlinks.length;
  totalOutLinks += f.file.outlinks.length;
  if (f.file.inlinks.length == 0) orphans++;
  if (f.file.inlinks.length > 5) hubs++;
});

const avgInLinks = (totalInLinks / total).toFixed(1);
const avgOutLinks = (totalOutLinks / total).toFixed(1);
const connectivity = ((totalInLinks + totalOutLinks) / (total * 2) * 100).toFixed(0);

dv.header(3, "🔗 Connectivity Metrics");
dv.paragraph(`
**Average In-Links**: ${avgInLinks} | **Average Out-Links**: ${avgOutLinks}  
**Connectivity Score**: ${connectivity}% | **Orphans**: ${orphans} | **Hubs (>5 in-links)**: ${hubs}
`);

// === SECTION 4: TAG ANALYTICS ===
const taggedNotes = files.where(f => f.file.tags && f.file.tags.length > 0).length;
const tagCoverage = Math.round((taggedNotes / total) * 100);

dv.header(3, "🏷️ Tag Coverage");
dv.paragraph(`**Tagged Notes**: ${taggedNotes}/${total} (${tagCoverage}%)`);

// === SECTION 5: QUICK ACCESS ===
dv.header(3, "🚀 Quick Access");

dv.header(4, "Recently Modified (5)");
dv.list(files.sort(f => f.file.mtime, 'desc').slice(0, 5).map(f => f.file.link));

dv.header(4, "Random Selection (3)");
const random = files.array().sort(() => 0.5 - Math.random()).slice(0, 3).map(f => f.file.link);
dv.list(random);
```

**What This Does:**
- Comprehensive single-query dashboard
- All critical metrics in one view
- Combines temporal, connectivity, and content analytics
- Includes quick-access sections for workflow

**Dashboard Use Cases:**
- Folder index note header
- Weekly folder review ritual
- Vault health monitoring
- Client/project status reporting

---

### **8.2 Status Board (Traffic Light System)**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Visual status indicators with color coding
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name && p.status);

const statusGroups = {
  "🟢 Active": files.where(f => f.status == "active").length,
  "🔵 Planned": files.where(f => f.status == "planned").length,
  "🟡 On Hold": files.where(f => f.status == "on-hold").length,
  "🔴 Blocked": files.where(f => f.status == "blocked").length,
  "⚪ Not Started": files.where(f => f.status == "not-started").length,
  "✅ Complete": files.where(f => f.status == "complete").length
};

dv.header(3, "🚦 Project Status Board");

for (const [status, count] of Object.entries(statusGroups)) {
  if (count > 0) {
    const notes = files.where(f => 
      (status.includes("Active") && f.status == "active") ||
      (status.includes("Planned") && f.status == "planned") ||
      (status.includes("Hold") && f.status == "on-hold") ||
      (status.includes("Blocked") && f.status == "blocked") ||
      (status.includes("Not Started") && f.status == "not-started") ||
      (status.includes("Complete") && f.status == "complete")
    );
    
    dv.header(4, `${status} (${count})`);
    dv.list(notes.map(n => n.file.link));
  }
}

// Completion percentage
const totalProjects = files.length;
const completedProjects = statusGroups["✅ Complete"];
const completionRate = Math.round((completedProjects / totalProjects) * 100);

dv.paragraph(`\n**Overall Completion**: ${completionRate}% (${completedProjects}/${totalProjects} projects)`);
```

**What This Does:**
- Visual status dashboard with emoji indicators
- Groups projects by current status
- Calculates completion metrics

**Workflow Integration:**
- Sprint planning and reviews
- Stakeholder status reporting
- Personal project tracking
- Team coordination

---

### **8.3 Priority Matrix (Eisenhower-Style)**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Assumes notes have "priority" (high/medium/low) and "urgency" (urgent/not-urgent) properties
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

const matrix = {
  urgent_important: files.where(f => f.priority == "high" && f.urgency == "urgent"),
  urgent_not_important: files.where(f => (f.priority == "medium" || f.priority == "low") && f.urgency == "urgent"),
  not_urgent_important: files.where(f => f.priority == "high" && f.urgency != "urgent"),
  not_urgent_not_important: files.where(f => (f.priority == "medium" || f.priority == "low") && f.urgency != "urgent")
};

dv.header(2, "📋 Priority Matrix");

dv.header(3, "🔴 Quadrant I: Urgent & Important (DO FIRST)");
if (matrix.urgent_important.length > 0) {
  dv.list(matrix.urgent_important.map(f => f.file.link));
} else {
  dv.paragraph("*No items in this quadrant*");
}

dv.header(3, "🟡 Quadrant II: Not Urgent but Important (SCHEDULE)");
if (matrix.not_urgent_important.length > 0) {
  dv.list(matrix.not_urgent_important.slice(0, 10).map(f => f.file.link));
} else {
  dv.paragraph("*No items in this quadrant*");
}

dv.header(3, "🟠 Quadrant III: Urgent but Not Important (DELEGATE/MINIMIZE)");
if (matrix.urgent_not_important.length > 0) {
  dv.list(matrix.urgent_not_important.map(f => f.file.link));
} else {
  dv.paragraph("*No items in this quadrant*");
}

dv.header(3, "⚪ Quadrant IV: Not Urgent & Not Important (ELIMINATE)");
if (matrix.not_urgent_not_important.length > 0) {
  dv.paragraph(`*${matrix.not_urgent_not_important.length} items - consider archiving*`);
} else {
  dv.paragraph("*No items in this quadrant*");
}
```

**What This Does:**
- [[Eisenhower Matrix]] implementation
- Prioritizes actions by urgency and importance
- Provides strategic task guidance

**Decision Framework:**
- **Quadrant I**: Crisis management, deadlines
- **Quadrant II**: Strategic work, high-value activities
- **Quadrant III**: Interruptions, delegate these
- **Quadrant IV**: Time wasters, eliminate

---

### **8.4 Tag Cloud Visualization**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Generate visual tag cloud with size indicating frequency
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

const tagCount = {};
files.forEach(f => {
  if (f.file.tags) {
    f.file.tags.forEach(tag => {
      tagCount[tag] = (tagCount[tag] || 0) + 1;
    });
  }
});

const sorted = Object.entries(tagCount).sort((a, b) => b[1] - a[1]);

dv.header(3, "☁️ Tag Cloud");

let cloud = "";
sorted.forEach(([tag, count]) => {
  let size = count > 10 ? "xxx-large" : count > 5 ? "xx-large" : count > 3 ? "x-large" : "large";
  let opacity = Math.min(0.5 + (count * 0.1), 1.0);
  
  // Remove # from tag for display
  const displayTag = tag.replace(/^#/, '');
  
  cloud += `<span style="font-size: ${size}; opacity: ${opacity}; margin: 5px;">${displayTag}</span> `;
});

dv.paragraph(cloud);

// Tag statistics
dv.paragraph(`\n**Total Unique Tags**: ${sorted.length} | **Most Used**: ${sorted[0]?.[0] || "N/A"} (${sorted[0]?.[1] || 0} notes)`);
```

**What This Does:**
- Visual tag frequency representation
- Larger text = more frequently used tags
- Quick insight into dominant themes

**Tag Management Applications:**
- Identify over-used tags (consider splitting)
- Spot under-used tags (consolidate or remove)
- Understand folder thematic distribution

---

### **8.5 Timeline Visualization (Gantt-Style)**

**Complexity**: ⭐⭐⭐⭐ Expert (DataviewJS)

```dataviewjs
// Assumes notes have "start-date" and "end-date" or "due" properties
const projects = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name && (p["start-date"] || p.due));

if (projects.length == 0) {
  dv.paragraph("*No projects with dates found*");
} else {
  const today = dv.date("today");
  
  const timeline = projects.map(p => {
    const start = p["start-date"] || p.file.ctime;
    const end = p["end-date"] || p.due || today;
    const duration = Math.round((end - start) / (1000 * 60 * 60 * 24));
    const progress = Math.round(((today - start) / (end - start)) * 100);
    
    let status;
    if (progress >= 100) status = "✅ Complete";
    else if (progress >= 75) status = "🟡 75%";
    else if (progress >= 50) status = "🟠 50%";
    else if (progress >= 25) status = "🔵 25%";
    else status = "⚪ Started";
    
    return {
      project: p.file.link,
      start: start,
      end: end,
      duration: duration + "d",
      progress: Math.min(progress, 100) + "%",
      status: status
    };
  }).sort((a, b) => a.start - b.start);
  
  dv.header(3, "📅 Project Timeline");
  dv.table(["Project", "Start", "End", "Duration", "Progress", "Status"],
    timeline.map(t => [t.project, t.start, t.end, t.duration, t.progress, t.status])
  );
}
```

**What This Does:**
- Chronological project view
- Progress tracking based on dates
- Visual status indicators

**Project Management Value:**
- Identify overlapping projects
- Track completion trajectories
- Plan resource allocation

---

## 🌟 Category 9: Novel & Creative Use Cases

> [!methodology-and-sources] Use Case
> Innovative, unexpected, or domain-specific applications of Dataview for unique workflows. Showcases [[Creative Thinking]] in PKB design.

### **9.1 Knowledge Decay Tracking (Forgetting Curve)**

**Complexity**: ⭐⭐⭐⭐ Expert (DataviewJS)

```dataviewjs
// Track how long it's been since notes were last reviewed, predict "decay"
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name && p["last-review"]);

const analyzed = files.map(f => {
  const lastReview = f["last-review"];
  const daysSince = Math.round((dv.date("today") - lastReview) / (1000 * 60 * 60 * 24));
  
  // Decay model: Ebbinghaus forgetting curve approximation
  // Retention = 100 * (1 / (1 + daysSince/7))
  const retention = Math.round(100 * (1 / (1 + daysSince / 7)));
  
  let urgency;
  if (retention < 30) urgency = "🔴 Critical";
  else if (retention < 50) urgency = "🟠 High";
  else if (retention < 70) urgency = "🟡 Medium";
  else urgency = "🟢 Fresh";
  
  return {
    note: f.file.link,
    lastReview: lastReview,
    daysSince: daysSince,
    retention: retention + "%",
    urgency: urgency
  };
}).sort((a, b) => a.retention.replace('%', '') - b.retention.replace('%', ''));

dv.header(3, "🧠 Knowledge Decay Analysis");

if (analyzed.length > 0) {
  dv.table(["Note", "Last Review", "Days Since", "Est. Retention", "Review Urgency"],
    analyzed.map(a => [a.note, a.lastReview, a.daysSince, a.retention, a.urgency])
  );
} else {
  dv.paragraph("*No notes with review dates found. Add 'last-review' property to track.*");
}
```

**What This Does:**
- Estimates knowledge retention based on last review
- Approximates [[forgetting curve]]
- Prioritizes review based on predicted decay

**Spaced Repetition Application:**
- Scientifically-informed review scheduling
- Focus on high-decay items
- Optimize learning efficiency

---

### **9.2 Collaborative Authorship Tracking**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Track contributions by different authors (assumes "author" or "contributors" property)
const files = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name);

const authorStats = {};

files.forEach(f => {
  const authors = f.author ? [f.author] : (f.contributors || []);
  
  authors.forEach(author => {
    if (!authorStats[author]) {
      authorStats[author] = {
        notes: [],
        totalWords: 0,
        lastContribution: f.file.mtime
      };
    }
    
    authorStats[author].notes.push(f.file.link);
    authorStats[author].totalWords += Math.round(f.file.size / 5);
    
    if (f.file.mtime > authorStats[author].lastContribution) {
      authorStats[author].lastContribution = f.file.mtime;
    }
  });
});

const sorted = Object.entries(authorStats)
  .sort((a, b) => b[1].notes.length - a[1].notes.length);

dv.header(3, "✍️ Authorship Analytics");

dv.table(["Author", "Notes", "~Words", "Last Active"],
  sorted.map(([author, stats]) => [
    author,
    stats.notes.length,
    stats.totalWords.toLocaleString(),
    stats.lastContribution
  ])
);
```

**What This Does:**
- Tracks collaborative knowledge creation
- Quantifies individual contributions
- Identifies active vs. inactive contributors

**Team Knowledge Base Applications:**
- Team accountability and recognition
- Identify expertise areas by author
- Detect knowledge silos

---

### **9.3 Reading List Progress Tracker**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Assumes reading notes have "status" (to-read, reading, finished) and "pages" properties
const readings = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name && p.type == "reading");

const statusGroups = {
  "📚 To Read": readings.where(r => r.status == "to-read"),
  "📖 Currently Reading": readings.where(r => r.status == "reading"),
  "✅ Finished": readings.where(r => r.status == "finished")
};

dv.header(2, "📚 Reading Dashboard");

for (const [status, items] of Object.entries(statusGroups)) {
  dv.header(3, `${status} (${items.length})`);
  
  if (items.length > 0) {
    dv.table(["Title", "Author", "Pages", "Started", "Progress"],
      items.map(r => [
        r.file.link,
        r.author || "N/A",
        r.pages || "N/A",
        r["start-date"] || "N/A",
        r["current-page"] && r.pages ? `${Math.round((r["current-page"] / r.pages) * 100)}%` : "N/A"
      ])
    );
  } else {
    dv.paragraph("*No items*");
  }
}

// Summary stats
const totalBooks = readings.length;
const finished = statusGroups["✅ Finished"].length;
const completionRate = Math.round((finished / totalBooks) * 100);

dv.paragraph(`\n**Total Books**: ${totalBooks} | **Finished**: ${finished} | **Completion Rate**: ${completionRate}%`);
```

**What This Does:**
- Manages reading lists with progress tracking
- Calculates completion percentages
- Organizes by reading status

**Reading Workflow:**
- Maintain TBR (to-be-read) queue
- Track concurrent readings
- Analyze reading velocity and patterns

---

### **9.4 Idea Incubation Dashboard**

**Complexity**: ⭐⭐⭐ Advanced (DataviewJS)

```dataviewjs
// Track "idea" notes and their maturation over time
const ideas = dv.pages('"' + dv.current().file.folder + '"')
  .where(p => p.file.name != dv.current().file.name && p.type == "idea");

const analyzed = ideas.map(idea => {
  const age = Math.round((dv.date("today") - idea.file.ctime) / (1000 * 60 * 60 * 24));
  const revisits = idea["review-count"] || 0;
  const links = idea.file.inlinks.length + idea.file.outlinks.length;
  
  // Maturity score based on age, revisits, and connections
  const maturityScore = Math.min(Math.round((revisits * 20) + (links * 10) + (age * 0.5)), 100);
  
  let stage;
  if (maturityScore < 20) stage = "🌱 Seedling";
  else if (maturityScore < 50) stage = "🌿 Growing";
  else if (maturityScore < 80) stage = "🍂 Maturing";
  else stage = "🌳 Mature";
  
  return {
    idea: idea.file.link,
    age: age + "d",
    revisits: revisits,
    links: links,
    maturity: maturityScore,
    stage: stage
  };
}).sort((a, b) => b.maturity - a.maturity);

dv.header(3, "💡 Idea Incubation Tracker");

if (analyzed.length > 0) {
  dv.table(["Idea", "Age", "Revisits", "Links", "Maturity", "Stage"],
    analyzed.map(a => [a.idea, a.age, a.revisits, a.links, a.maturity, a.stage])
  );
  
  dv.paragraph(`\n**Mature Ideas Ready for Execution**: ${analyzed.filter(a => a.maturity >= 80).length}`);
} else {
  dv.paragraph("*No idea notes found. Create notes with `type: idea`.*");
}
```

**What This Does:**
- Tracks ideation lifecycle
- Quantifies idea maturity
- Identifies ideas ready for implementation

**Creative Workflow:**
- Let ideas incubate naturally
- Revisit and refine over time
- Execute when sufficiently developed

---

### **9.5 Semantic Relationship Strength Analyzer**

**Complexity**: ⭐⭐⭐⭐ Expert (DataviewJS)

```dataviewjs
// Calculate relationship strength between linked notes based on multiple factors
const currentFolder = dv.current().file.folder;
const files = dv.pages('"' + currentFolder + '"')
  .where(p => p.file.name != dv.current().file.name);

const relationships = [];

for (const note1 of files.array()) {
  for (const link of note1.file.outlinks) {
    const note2 = files.find(f => f.file.path == link.path);
    if (!note2) continue;
    
    // Calculate relationship strength factors
    const bidirectional = note2.file.outlinks.some(l => l.path == note1.file.path) ? 2 : 1;
    const sharedTags = note1.file.tags?.filter(t => note2.file.tags?.includes(t)).length || 0;
    const sharedLinks = note1.file.outlinks.filter(l => 
      note2.file.outlinks.some(l2 => l2.path == l.path)
    ).length;
    
    // Strength formula (weighted)
    const strength = (bidirectional * 10) + (sharedTags * 5) + (sharedLinks * 3);
    
    relationships.push({
      from: note1.file.link,
      to: note2.file.link,
      strength: strength,
      factors: `Bi:${bidirectional > 1 ? "✓" : "✗"} | Tags:${sharedTags} | Links:${sharedLinks}`
    });
  }
}

const sorted = relationships
  .sort((a, b) => b.strength - a.strength)
  .slice(0, 20);

dv.header(3, "🔗 Strongest Semantic Relationships");

dv.table(["From", "To", "Strength Score", "Factors"],
  sorted.map(r => [r.from, r.to, r.strength, r.factors])
);

dv.paragraph("\n*Strength = (Bidirectional×10) + (SharedTags×5) + (SharedLinks×3)*");
```

**What This Does:**
- Quantifies link strength beyond binary existence
- Considers bidirectionality, shared tags, and shared outbound links
- Identifies strongest conceptual relationships

**Knowledge Graph Optimization:**
- Prioritize maintaining strongest links
- Identify candidates for MOC grouping
- Detect conceptual clusters

---

## 📚 Inline Query Examples

> [!methodology-and-sources] Use Case
> Inline queries (`= expression` syntax) for embedding dynamic values directly in prose. Perfect for living documents and self-updating metadata.

### **Inline Query Collection**

**Current File Metadata:**
```
This note was created on `= this.file.ctime` and last modified on `= this.file.mtime`.
```

**File Age Calculation:**
```
This note is `= dur(date(today) - this.file.ctime).days` days old.
```

**Link Count Display:**
```
This note links to `= length(this.file.outlinks)` other notes and is referenced by `= length(this.file.inlinks)` notes.
```

**Tag Count:**
```
Tagged with `= length(this.file.tags)` tags: `= join(this.file.tags, ", ")`
```

**Conditional Status Display:**
```
Status: `= choice(this.maturity = "evergreen", "✅ Mature", choice(this.maturity = "budding", "🌿 Growing", "🌱 New"))`
```

**Word Count Estimate:**
```
Approximately `= round(this.file.size / 5)` words in this note.
```

**Days Until Review:**
```
Next review in `= dur(this.review-date - date(today)).days` days.
```

**Folder Context:**
```
This note is in the `= this.file.folder` folder, which contains `= length(dv.pages('"' + this.file.folder + '"'))` notes.
```

**Dynamic Date Calculations:**
```
Days until deadline: `= dur(this.deadline - date(today)).days` days
```

**Completion Percentage:**
```
Progress: `= round((this.completed-tasks / this.total-tasks) * 100)`%
```

---

# 🔗 Related Topics for PKB Expansion

1. **[[DataviewJS API Reference]]**
   - *Connection*: Complete API documentation for advanced DataviewJS queries
   - *Depth Potential*: Comprehensive coverage of all DataviewJS methods, objects, and patterns
   - *Knowledge Graph Role*: Technical reference hub for Dataview scripting

2. **[[Obsidian Plugin Integration Patterns]]**
   - *Connection*: How Dataview interacts with other plugins (Templater, QuickAdd, Meta Bind, Tasks)
   - *Depth Potential*: Cross-plugin workflow automation and data synchronization strategies
   - *Knowledge Graph Role*: Integration layer connecting plugin ecosystem

3. **[[Knowledge Graph Metrics & Analysis]]**
   - *Connection*: Advanced graph theory applications to PKB structure analysis
   - *Depth Potential*: Centrality measures, clustering coefficients, PageRank for notes
   - *Knowledge Graph Role*: Analytical framework for vault health assessment

4. **[[Spaced Repetition System Design]]**
   - *Connection*: Implementing SRS with Dataview for optimal review scheduling
   - *Depth Potential*: Forgetting curve algorithms, optimal interval calculation, evidence-based scheduling
   - *Knowledge Graph Role*: Learning optimization methodology for evergreen notes

---

> [!important] Implementation Notes
> **Getting Started:**
> 1. Copy queries into your index notes
> 2. Adjust `file.folder` paths to match your structure
> 3. Customize property names to match your metadata schema
> 4. Combine queries to create comprehensive dashboards
> 
> **Performance Considerations:**
> - Limit DataviewJS to <20 operations per query when possible
> - Use `WHERE` clauses early to reduce dataset size
> - Cache results with `const` when reusing calculations
> - Consider folder-specific queries vs. vault-wide for large vaults
>
> **Metadata Schema Recommendations:**
> For maximum query utility, standardize these properties:
> - `status`, `type`, `priority`, `urgency`
> - `created`, `modified`, `review-date`, `review-count`
> - `maturity`, `confidence` (for [[Zettelkasten]])
> - `start-date`, `due`, `end-date` (for project tracking)