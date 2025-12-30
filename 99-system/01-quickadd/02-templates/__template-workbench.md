










## Template Building







calculation for tag, type, status, conditional, maturity
use the output from these to build out queries that populate them selfes with correct data from frontmatter.



add metabind buttons at the queries that use fronmatter, then you can activley change the frontmatter, rebuild the dataview  and see an update query
only if inline works in code blocks

cheat sheet for queries


---
tags:
  - review-session
  - type/daily
  - year/2025
date: 2025-12-14
review-type: daily
completed: false
notes-reviewed: 0
session-duration: 0
type: review-session




``````
_folder-index-note-template


---
id: "<% tp.date.now("YYYYMMDD-HHmmss") %>"
confidence: "<% await tp.system.suggester(
    ["speculative", "provisional", "moderate", "established", "high"], 
    ["speculative", "provisional", "moderate", "established", "high"], 
    false, 
    "Choice?"
    ) %>"
maturity: "<% await tp.system.suggester(
    ["needs-review", "seedling", "developing", "budding", "evergreen"], 
    ["needs-review", "seedling", "developing", "budding", "evergreen"], 
    false, 
    "Choice?"
    ) %>"
type: "<% await tp.system.suggester(
    ["report", "topics", "reference", "prompt", "gemini-gem", "claude-project"], 
    ["report", "topics", "reference", "prompt", "gemini-gem", "claude-project"], 
    false, 
    "Choice?"
    ) %>"
aliases: "<% await tp.system.prompt("Alias?") %>"
tags:
  - "type/index"
  - "year/"<% tp.date.now("YYYY") %>"
  - tags: "<% await tp.system.suggester(
    ["pkb", "pkm", "cognitive-science", "prompt-engineering", "cosmology", "academic"], 
    ["pkb", "pkm", "cognitive-science", "prompt-engineering", "cosmology", "academic"], 
    false, 
    "Choice?"
    ) %>"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily Note]]"
  - "[[<% tp.date.now("gggg-[W]WW") %>|Weekly Note]]"
title: "<% await tp.system.prompt("Title for YAML") %>"
---

### Initial Creation: <% tp.date.now("dddd, MMMM Do, YYYY") %>

----

### 📁<% tp.file.title %>'s <small>Index Note</small>

>[! ] ### In-Note-Metadata Panel
> > [!file] #### 📝File Context
> > **Name**: `= this.file.name` | **Location**: `= this.file.folder`
> > **Size**: `= round(this.file.size / 1024, 2)` KB
> > **Aliases**: `= join(this.file.aliases, " | ")`
> > **Tags**: `= join(this.file.tags, ", ")` 
> > > [!calendar]  ##### ⌛Temporal Context
> > > **Created**: `= this.file.ctime` | **Age**: `= (date(today) - this.file.cday).days` days
> > > **Creation Year**: `= this.file.ctime.year` | **Creation Month**: `= this.file.ctime.month`
> > > **Creation Day**: `= this.file.ctime.day` | **Day of Week Created**: `= this.file.ctime.weekday`
> > > **Days Since Created**: `= (date(today) - this.file.cday).days` days
> > > **Last Edit**: `= this.file.mtime` | **Days Since Last Edit**: `= (date(today) - this.file.mday).days` days |
> > > **Staleness**: `= choice((date(today) - this.file.mday).days > 180, "🕸️ Cobwebs", choice((date(today) - this.file.mday).days > 30, "🍂 Cold", "🔥 Fresh"))`

### Files in this Folder







### Performance Metrics
#### Folder Activity Metrics (Count & Rate)
#### Recent Changes














### Linking Metrics
#### Links to this Folder's Notes
#### Orphaned Notes in this folder with no Links












``````







`````
----

> [! ] ## 🗂️File & Folder Data Metadata Queries
> > [!methodology-and-sources] What these Queries Do
> > These queries provide comprehensive folder-level intelligence: file counts, creation/modification patterns, size analytics, and temporal distributions. Essential for folder index notes and vault health monitoring.

> [! ] ### Random Note Resurfacing**
> **What This Does:**
> - Selects random notes from folder
> - Encourages serendipitous rediscovery
> - Breaks out of recency bias
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

>[! ] ### Folder Metrics
> **What This Does:**
> - Single-row dashboard showing folder health metrics
> - Tracks creation velocity (new notes per week)
> - Identifies active maintenance (modifications)
> - Monitors folder growth (total size)
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

> [! ] ### Creation Date Calendar View**
> **What This Does:**
> - Visual calendar showing when notes were created
> - Identifies temporal clusters and gaps
> - Useful for understanding knowledge capture patterns
```dataview
CALENDAR file.cday
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
```
> [#] ### Recently Created Notes (Discovery Window)**
> **What This Does:**
> - Shows notes created in last 14 days
> - "Fresh content" discovery window
> - Integration checkpoint
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

>[! ] ### Basic Folder Contents Listing
> **What This Does:**
> - Lists all files in current note's folder (excluding the index note itself)
> - Displays creation and modification timestamps
> - Alphabetically sorted for easy navigation
```dataview
TABLE file.ctime AS "Created", file.mtime AS "Modified"
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
SORT file.name ASC
```

> [! ] ### File Age Distribution
> **What This Does:**
> - Categorizes notes by temporal lifecycle
> - Visual age indicators for quick scanning
> - Identifies candidates for review or archival
> > [! ] ##### Lifecycle Stages
> > - 🌱 Fresh (< 7 days): New captures
> > - 🌿 Recent (< 30 days): Under development
> > - 🍂 Mature (< 90 days): Established content
> > - 🍁 Aged (< 1 year): Stable knowledge
> > - 🕰️ Archive (> 1 year): Historical reference
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

> [! ] ### Staleness Detection
> **What This Does:**
> - Surfaces notes untouched for 90+ days
> - Prioritizes by staleness (oldest first)
> - Shows link count to assess importance
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
----

>[! ] ## 🔗Link Analysis & Graph Intelligence
> > [!methodology-and-sources] #### What these Queires Do
> > These queries analyze the [[knowledge graph]] structure within a folder: identifying hubs, orphans, bridges, and link density patterns. Critical for maintaining a well-connected [[Personal Knowledge Base]].

> [! ] ### Orphan Note Detection**
> **What This Does:**
> - Identifies notes with zero incoming links
> - Shows outbound link count (if > 0, note is "islanded" not truly orphaned)
> - Sorted by creation date to prioritize recent orphans
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

> [! ] ### Hub Note Identification (High In-Link Count)**
> **What This Does:**
> - Identifies high-connectivity nodes (hubs)
> - Calculates total link density
> - Reveals emergent organizational centers
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

> [! ] ### Bidirectional Link Mapping**
> **What This Does:**
> - Counts bidirectional links (strongest connections)
> - Identifies mutually reinforcing concept pairs
> - Reveals conversation-like note relationships
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

> [! ] ### Link Density (Per Note)
> **What This Does:**
> - Calculates link-to-content ratio
> - Identifies under-linked content (sparse)
> - Highlights well-integrated notes (dense)
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

> [! ] ### Broken Link Detection
> **What This Does:**
> - Identifies notes with non-resolving links
> - Lists broken link targets
> - Essential for vault maintenance
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

> [! ] ### Unlinked Mention Opportunities**
> **What This Does:**
> - Identifies potential link opportunities based on name mentions
> - Prioritizes by frequency
> - Samples files for manual review
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

----

> [! ] ## 📑Content & Metadata Intelligence
> > [!methodology-and-sources] #### What these Queires Do
> > These queries analyze note contents, metadata patterns, tag usage, and property distributions. Useful for [[tag taxonomy]] management, metadata standardization, and content quality assessment.

> [! ]  ### Metadata Coverage Assessment
> **What This Does:**
> - Audits metadata completeness
> - Identifies gaps in standardization
> - Prioritizes cleanup efforts
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

> [! ] ### Word Count & Size Analytics**
> **What This Does:**
> - Categorizes notes by content depth
> - Provides folder-wide content metrics
> - Identifies stubs requiring expansion
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

> [! ] ### Modification Velocity Tracking**
> **What This Does:**
> - Calculates how actively notes are maintained
> - Identifies consistently updated vs. static notes
> - Useful for prioritizing maintenance efforts
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
> [! ] ### Least Recently Modified (LRM) Notes**
> **What This Does:**
> - Surfaces oldest unmodified notes
> - Combats "out of sight, out of mind"
> - Systematic rediscovery
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

> [! ] ### Similar Note Suggestions (Tag-Based)**
> **What This Does:**
> - Identifies notes with similar tag profiles not yet linked
> - Suggests potential knowledge connections
> - Facilitates [[networked thought]] building
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

Advanced Pattern Analysis

> Note Clustering by Shared Links**
> **What This Does:**
> - Identifies notes with highly overlapping link profiles
> - Reveals emergent topic clusters
> - Suggests [[MOC]] opportunities

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

> [!folder] ##### 📂Folder Context
> Name: `= this.file.name` | **Location**: `= this.file.folder`
> **Size**: `= round(this.file.size / 1024, 2)` KB
> **Average File Size**: `= round(sum(map(pages('"' + this.file.folder + '"'), p => p.file.size)) / length(pages('"' + this.file.folder + '"')) / 1024, 2)` KB
> **Newest Note**: `= max(map(pages('"' + this.file.folder + '"'), p => p.file.ctime))`
> - **Aliases in this folder**: `= join(flat(map(pages('"' + this.file.folder + '"'), p => p.file.aliases)), ", ")`
> - **Tags in This Folder**: `= join(flat(map(pages('"' + this.file.folder + '"'), p => p.file.tags)), ", ")`
> - **Neighbors**: `= length(pages('"' + this.file.folder + '"')) - 1` other notes here
> - **Parent Folder**: `= split(this.file.folder, "/")[length(split(this.file.folder, "/")) - 2]`
  
`````










```

/* ═══════════════════════════════════════════════════════════════════════
  
   ═══════════════════════════════════════════════════════════════════════
*/
/* ───────────────────────────────────────────────────────────────────────
   CONFIGURATION: PRE-DEFINED METADATA LISTS
   ─────────────────────────────────────────────────────────────────────── */
// 1. Model used
const model = [
    "",
    "",
    "",
    "",
    ""
];
// 
// GROUP A1: Tags
const groupA1_Tags = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    ""
];
// 
// GROUP B2: Tags
const groupB2_Tags = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    ""
];

```

```
aliases:
  - "<% alias1 %>"
  - "<% alias2 %>"
tags:
  - "type/permanent"
  - "year/<% year %>"
  - "<% tag1 %>"
  - "<% tag2 %>"
  - "<% tag3 %>"
  - "<% tag4 %>"
  - "<% tag5 %>"
  - "<% tag6 %>"
  - "<% tag7 %>"
  - "<% tag8 %>"
  - "<% tag9 %>"
  - "<% tag10 %>"
  - "<% tag11 %>"
source: "<% source %>"
id: "<% id %>"
created: "<% dateNow %>T<% timeNow %>"
modified: "<% dateNow %>T<% timeNow %>"
week: "[[<% tp.date.now("gggg-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% year %>]]"
type: "<% type %>"
maturity: "<% maturity %>"
confidence: "<% confidence %>"
next-review: "<% nextReview %>"
review-count: 0
link-up:
  - "<% linkUp %>"
link-related:
  - "[[<% dateNow %>|Daily-Note]]"aliases:
  - "<% alias1 %>"
  - "<% alias2 %>"
tags:
  - "type/permanent"
  - "year/<% year %>"
  - "<% tag1 %>"
  - "<% tag2 %>"
  - "<% tag3 %>"
  - "<% tag4 %>"
  - "<% tag5 %>"
  - "<% tag6 %>"
  - "<% tag7 %>"
  - "<% tag8 %>"
  - "<% tag9 %>"
  - "<% tag10 %>"
  - "<% tag11 %>"
source: "<% source %>"
id: "<% id %>"
created: "<% dateNow %>T<% timeNow %>"
modified: "<% dateNow %>T<% timeNow %>"
week: "[[<% tp.date.now("gggg-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% year %>]]"
type: "<% type %>"
maturity: "<% maturity %>"
confidence: "<% confidence %>"
next-review: "<% nextReview %>"
review-count: 0
link-up:
  - "<% linkUp %>"
link-related:
  - "[[<% dateNow %>|Daily-Note]]
``````






```
<% await tp.system.suggester(
    ["", "", "", "", "", ""], 
    ["", "", "", "", "", ""], 
    false, 
    "Choice?"
    ) %>
```

```
aliases:
  - "<% alias1 %>"
  - "<% alias2 %>"
tags:
  - "type/permanent"
  - "year/<% year %>"
  - "<% tag1 %>"
  - "<% tag2 %>"
  - "<% tag3 %>"
  - "<% tag4 %>"
  - "<% tag5 %>"
  - "<% tag6 %>"
  - "<% tag7 %>"
  - "<% tag8 %>"
  - "<% tag9 %>"
  - "<% tag10 %>"
  - "<% tag11 %>"
source: "<% source %>"
id: "<% id %>"
created: "<% dateNow %>T<% timeNow %>"
modified: "<% dateNow %>T<% timeNow %>"
week: "[[<% tp.date.now("gggg-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% year %>]]"
type: "<% type %>"
maturity: "<% maturity %>"
confidence: "<% confidence %>"
next-review: "<% nextReview %>"
review-count: 0
link-up:
  - "<% linkUp %>"
link-related:
  - "[[<% dateNow %>|Daily-Note]]"
```

```
## Standardized YAML Frontmatter Format w/ Templater Logic for Universal Template

---
title: "<% await tp.system.prompt("Title for YAML") %>"
id: "<% tp.date.now("YYYYMMDD-HHmmss") %>"
date: "<% tp.date.now("YYYY-MM-DD") %>"
week: "<% tp.date.now("gggg-[W]WW")%>"
month: "<% tp.date.now("YYYY-MM") %>"
quarter: "<% tp.date.now("YYYY-[Q]Q")%>"
year: "<% tp.date.now("YYYY") %>"
type: "<% await tp.system.suggester(
    ["report", "topics", "reference", "prompt", "gemini-gem", "claude-project"], 
    ["report", "topics", "reference", "prompt", "gemini-gem", "claude-project"], 
    false, 
    "Choice?"
    ) %>"
tags: "<% await tp.system.suggester(
    ["pkb", "pkm", "cognitive-science", "prompt-engineering", "cosmology", "academic"], 
    ["pkb", "pkm", "cognitive-science", "prompt-engineering", "cosmology", "academic"], 
    false, 
    "Choice?"
    ) %>"
aliases: "<% await tp.system.prompt("Alias?") %>"
maturity: "<% await tp.system.suggester(
    ["needs-review", "seedling", "developing", "budding", "evergreen"], 
    ["needs-review", "seedling", "developing", "budding", "evergreen"], 
    false, 
    "Choice?"
    ) %>"
confidence: "<% await tp.system.suggester(
    ["speculative", "provisional", "moderate", "established", "high"], 
    ["speculative", "provisional", "moderate", "established", "high"], 
    false, 
    "Choice?"
    ) %>"
next-review: "<% tp.date.now("YYYY-MM-DD", 7) %>
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily Note]]"
  - "[[<% tp.date.now("gggg-[W]WW") %>|Weekly Review]]"
---

### Initial Creation: <% tp.date.now("dddd, MMMM Do, YYYY") %>
```

```
last-used: "<% tp.date.now("YYYY-MM-DD") %>"
key-takeaway: "<% await tp.system.prompt("Description of Prompts Top Feature") %>"
description: "<% await tp.system.prompt("Description of Prompt") %>"
tags:
  - "year/2025"
  - "prompt-engineering/anatomy/instruction"
  - "prompt-pattern/output-format/markdown"
  - "llm-capability/generation"
  - "llm-architecture/model-family/gemini"
  - "advanced-prompting/agents"
  - "prompt-workflow/deployment"
aliases:
  - "Prompt"
  - "Prompt-Engineering"
link-up: "[[moc-agentic-instruction-sets-2025117044009]]"
```

```
<% tp.date.now("dddd, MMMM Do, YYYY") %>
```



```
← [[<% tp.date.now("gggg-[W]WW", -7) %>|Last Week]] | [[<% tp.date.now("gggg-[W]WW", 7) %>|Next Week]] →

📅 [[<% tp.date.now("YYYY-MM") %>|This Month]] | [[<% tp.date.now("YYYY-[Q]Q") %>|This Quarter]] | [[<% tp.date.now("YYYY") %>|This Year]]

This auto-generates contextual navigation without manual date calculation.
```

**Alternative: Automatic Migration with Templater**
 
 Some users prefer fully automated task migration where incomplete tasks automatically move to the next period's note. This requires Templater 
 
```
<%*
const lastWeek = tp.date.now("gggg-[W]WW", -7);
const lastWeekPath = `01-journal/02-weekly/${lastWeek}.md`;
const lastWeekFile = app.vault.getAbstractFileByPath(lastWeekPath);
if (lastWeekFile) {
const content = await app.vault.read(lastWeekFile);
const incompleteTasks = content
.split('\n')
.filter(line => line.includes('- [ ]'));
if (incompleteTasks.length > 0) {
tR += "## ⏰ Rolled Over from Last Week\n\n";
tR += incompleteTasks.join('\n');
 }
 }
%>
```
### Dynamic Period Completion Percentage

Calculate how far through a period you are for progress context:

 [!example]
 **Week Completion Progress Bar**
 
 ```
 
<% 
const dayOfWeek = moment().isoWeekday(); // 1=Monday, 7=Sunday
const percentComplete = ((dayOfWeek / 7) * 100).toFixed(0);
const filled = Math.round(dayOfWeek / 7 * 10);
const empty = 10 - filled;
%>
 
**Day <%= dayOfWeek %> of 7** (<%= percentComplete %>% complete)
 
[<%= '█'.repeat(filled) %><%= '░'.repeat(empty) %>]
 ```
This visual indicator provides immediate context for where you are in the week.

### Custom Navigation Bars with Smart Links

Create sophisticated navigation that adapts based on current date:

> [!example]
> **Smart Multi-Level Navigation**
> 

```
<%*
// Get current date components
const today = moment();
const yesterday = moment().subtract(1, 'days');
const tomorrow = moment().add(1, 'days');
const thisWeek = moment().format('gggg-[W]WW');
const lastWeek = moment().subtract(7, 'days').format('gggg-[W]WW');
const nextWeek = moment().add(7, 'days').format('gggg-[W]WW');
const thisMonth = moment().format('YYYY-MM');
const thisQuarter = moment().format('YYYY-[Q]Q');
const thisYear = moment().format('YYYY');
%>

## 🧭 Navigation
 
**Daily**: ← [[<%= yesterday.format('YYYY-MM-DD') %>|Yesterday]] | [[<%= tomorrow.format('YYYY-MM-DD') %>|Tomorrow]] →
 
**Weekly**: ← [[<%= lastWeek %>|Last Week]] | [[<%= nextWeek %>|Next Week]] →
 
**Hierarchical**: [[<%= thisWeek %>|This Week]] → [[<%= thisMonth %>|This Month]] → [[<%= thisQuarter %>|This Quarter]] → [[<%= thisYear %>|This Year]]
```


```
### Morning

- **Prospective Visualization**: 
	- [What challenges might today present?] 
	- [How do I want to respond?] 

- **Virtue Intention**: 
	- [Which specific virtue will I emphasize today?] 
		- [Wisdom], [Justice], [Courage], [Temperance]

- **Control Dichotomy**: 
	- [What is within versus outside my control today?]

- **Implementation Intentions**: 
	- [If [specific situation], then I will [specific response]].

### Evening

- **Event Documentation**: 
- [What significant events occurred?]
	- [Factual recording]

- **Judgment Analysis**: 
	- [What interpretations/judgments did I make?] 
		- [Were they based on what's controllable?]

- **Emotional Inventory**: 
	- [When did I experience strong emotions?] 
		- [What thoughts generated them?]

- **Virtue Assessment**: 
	- [Did I act according to my morning intention?] 
		- [Where did I succeed or fail?]

- **Cognitive Reframing**: 
	- [Select one problematic reaction and systematically reframe using Stoic principles.]

- **Lesson Extraction**: 
	- [What did I learn today about myself, others, or effective action?]

- **Tomorrow's Commitment**: 
	- [Based on today's reflection, what specific intention will I set for tomorrow?]
```





## Permanent Note Update
`````
# <% title %>
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

## Foundational Understanding
> [!definition]
> [**Title**:: [[<% title %>]]]
> [**Definition**:: ]

### Outline 

## Key Principles
1. 
2. 
3. 

## Related Notes
```dataview
TABLE type, maturity, confidence
FROM  ""
WHERE  type = "<% type %>"
SORT "maturity" DESC
LIMIT 15
```

### Direct Connections
- [[Concept 1]]
- [[Concept 2]]
- [[Concept 3]]

## Practical Applications

> [!example] Application 1
> *Description*: 

> [!example] Application 2
> *Description*: 

> [!example] Application 3
> *Description*:

> [!example] Application 4
> *Description*:

> [!example] Application 5
> *Description*:

> [!example] Application 6
> *Description*:

## Evolution Log

> [!timeline] Development History
> `= this.review-count` total reviews

### <% dateNow %> - Initial Creation
**Context**: `= this.source`
**Maturity**: `= this.maturity`  
**Confidence**: `= this.confidence`

## Sources and Reference

### Primary Sources
- 

### Supporting Material
- 

## 🔗Backlinks & Connections

```dataview
TABLE 
    type AS "Type",
    maturity AS "Maturity",
    created AS "Created"
FROM [[#]]
SORT created DESC
LIMIT 15
```

## 📈Review System

> [!important] Review Schedule
> - **Next Review**: `= this.next-review`
> - **Review Frequency**: Based on maturity level
>   - *Seedling*: Weekly
>   - *Budding*: Bi-weekly
>   - *Developing*: Monthly
>   - *Evergreen*: Quarterly

## 🏷️Tags & Classification

Primary Tags: `= this.tags`  
Type: `= this.type`  
Source: `= this.source`

---
`````

## Report Update
````

> [!overview]
> - **Title**:: [[<% title %>]]
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
WHERE  type = "<% type %>"
SORT "maturity" DESC
LIMIT 15
```
### Sources & References
```dataview
TABLE 
    source AS "Source Type",
    file.ctime AS "Date Added"
FROM ""
WHERE source = "<% source %>"
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
### <% dateNow %> - Initial Creation
*Context*: `=this.title` **by**: `=this.source`
*Maturity*: `= this.maturity`  
*Confidence*: `= this.confidence`

### Tags & Classification
*Primary Tags*: `= this.tags`  
*Type*: `= this.type`  
*Source*: `= this.source`

---

# <% title %>

*{{PASTE REPORT HERE}}*
````



























