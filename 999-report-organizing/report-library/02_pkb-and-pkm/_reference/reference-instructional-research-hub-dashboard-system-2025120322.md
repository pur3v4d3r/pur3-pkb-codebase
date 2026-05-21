---
aliases:
  - "Dashboard Design"
  - "Dashboard Building"
tags:
  - "type/report"
  - "year/2025"
  - "type/tutorial"
  - "status/in-progress"
  - "pkb"
  - "productivity-systems"
  - "dashboard-design"
  - "cognitive-science/metacognition"
  - "cognitive-load-management"
  - "cognitive-resources"
  - "pkb/optimization"
  - "automation"
  - "cognitive-pkm"
source: "claude-sonnet-4.5"
id: "20251203223946"
created: "2025-12-03T22:39:46"
modified: "2025-12-03T22:39:46"
week: "[[2025-W49]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: "reference"
maturity: "needs-review"
confidence: "provisional"
next-review: "2025-12-10"
review-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-12-03|Daily-Note]]"
---
# Research Hub Dashboard: Complete Component System
> [!overview]
> - **Title**:: [[Research Hub Dashboard: Complete Component System]]
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

> [!overview] # 🚀 Research Hub Dashboard System
> ## Complete Component Library for Your PKB
> 
> 
> **Purpose**: This is a modular, production-ready Research/Project Hub system built specifically for your 577-tag taxonomy and metadata architecture. Each component is designed to work seamlessly with your existing Templater master template and can be mixed-and-matched to create your ideal command center
> 
> ## 📦Package Contents
> 
> *This package contains*:
> -  **6 major component categories** 
> 	- with **5-6 working examples each**
> 
> 1. **Dashboard Overview Sections** (Visual status displays)
> 2. **Dataview Block Queries** (Tables, lists, task views)
> 3. **Dataview Inline Queries** (Embedded metrics)
> 4. **Meta Bind Interactive Buttons** (Quick actions)
> 5. **Templater Initialization Logic** (Project setup automation)
> 6. **Advanced Analytics Components** (Progress tracking, visualizations)

---

# 1️⃣ DASHBOARD OVERVIEW SECTIONS

## Component 1.1: Project Health Monitor

`````markdown
## 🎯 Project Health Dashboard

> [!abstract] System Overview
> **Total Projects**: `= length(filter(pages("""type/dashboard OR type/report OR type/claude-project OR type/gemini-gem"""), (p) => p.maturity != "archived"))` active
> **You Can Work On**: `= length(filter(pages(), (p) => p.maturity = "sappling"))` stable
> **Review Queue**: `= length(filter(pages(), (p) => p.next-review != null AND date(p.next-review) <= date(today))))` due

### 📊 Maturity Distribution

| Status | Count | Percentage |
|--------|-------|------------|
| 🌱 Seedling | `= length(filter(pages(), (p) => p.maturity = "seedling"))` | `= round(length(filter(pages(), (p) => p.maturity = "seedling")) / length(pages()) * 100)`% |
| 🌿 Budding | `= length(filter(pages(), (p) => p.maturity = "budding"))` | `= round(length(filter(pages(), (p) => p.maturity = "budding")) / length(pages()) * 100)`% |
| 🌳 Developing | `= length(filter(pages(), (p) => p.maturity = "developing"))` | `= round(length(filter(pages(), (p) => p.maturity = "developing")) / length(pages()) * 100)`% |
| 🌲 Evergreen | `= length(filter(pages(), (p) => p.maturity = "evergreen"))` | `= round(length(filter(pages(), (p) => p.maturity = "evergreen")) / length(pages()) * 100)`% |

### 🎚️ Confidence Distribution

- **High/Established**: `= length(filter(pages(), (p) => p.confidence = "high" OR p.confidence = "established"))` notes
- **Moderate**: `= length(filter(pages(), (p) => p.confidence = "moderate"))` notes  
- **Provisional/Speculative**: `= length(filter(pages(), (p) => p.confidence = "provisional" OR p.confidence = "speculative"))` notes

### 📅 Temporal Metrics

**This Week's Activity**:
- Created: `= length(filter(pages(), (p) => date(p.created) >= date(today) - dur(7 days)))` new notes
- Modified: `= length(filter(pages(), (p) => date(p.modified) >= date(today) - dur(7 days)))` updated notes
- Reviewed: `= sum(filter(pages(), (p) => date(p.modified) >= date(today) - dur(7 days)).review-count)` total reviews

**Staleness Alert** 🕸️:
- Not touched in 90+ days: `= length(filter(pages(), (p) => date(today) - date(p.modified) > dur(90 days)))` notes
- Not touched in 180+ days: `= length(filter(pages(), (p) => date(today) - date(p.modified) > dur(180 days)))` notes
`````

---

## Component 1.2: Domain-Specific Focus Areas

`````markdown
## 🧠 Domain Activity Centers

### Cognitive Science Research `VIEW[{length(filter(pages(#cognitive-science), (p) => p))}]` notes

``` 
TABLE 
    maturity AS "📊 Maturity",
    confidence AS "🎯 Confidence",
    choice(date(today) - date(modified) < dur(7 days), "🔥 Fresh", choice(date(today) - date(modified) < dur(30 days), "✅ Active", "🕸️ Stale")) AS "Status"
FROM #cognitive-science
WHERE type != "moc"
SORT modified DESC
LIMIT 10
```

### Prompt Engineering Projects `VIEW[{length(filter(pages(#prompt-engineering), (p) => p))}]` notes

``` 
TABLE
    maturity AS "📊 Maturity",
    confidence AS "🎯 Confidence",
    file.mtime AS "Last Modified"
FROM #prompt-engineering  
WHERE type != "moc"
SORT file.mtime DESC
LIMIT 10
```

### PKB/PKM System Development `VIEW[{length(filter(pages(#pkb OR #pkm OR #obsidian), (p) => p))}]` notes

``` 
TABLE
    maturity AS "📊 Maturity",
    type AS "Type",
    file.mtime AS "Last Modified"
FROM #pkb OR #pkm OR #obsidian
WHERE type != "moc"
SORT file.mtime DESC
LIMIT 10
```

### Cosmology Research `VIEW[{length(filter(pages(#cosmology), (p) => p))}]` notes

``` 
TABLE
    maturity AS "📊 Maturity",
    confidence AS "🎯 Confidence",
    file.ctime AS "Created"
FROM #cosmology
WHERE type != "moc"
SORT file.ctime DESC
LIMIT 10
```
`````

---

## Component 1.3: Review Queue Management

`````markdown
## 📅 Review Queue & Maintenance

> [!important] Overdue Reviews
> **Items Requiring Attention**: `= length(filter(pages(), (p) => p.next-review != null AND date(p.next-review) < date(today)))` overdue

### Due This Week

``` 
TABLE
    choice(maturity = "seedling", "🌱", choice(maturity = "budding", "🌿", choice(maturity = "developing", "🌳", "🌲"))) AS "Mat",
    next-review AS "📅 Due",
    review-count AS "🔄 Reviews",
    choice(date(today) - date(next-review) > dur(0 days), "⚠️ OVERDUE", "✅ On Track") AS "Status"
FROM ""
WHERE next-review != null
    AND date(next-review) <= date(today) + dur(7 days)
SORT next-review ASC
LIMIT 20
```

### Upcoming Reviews (Next 30 Days)

``` 
TABLE
    maturity AS "Maturity",
    next-review AS "Scheduled",
    review-count AS "Total Reviews",
    round((date(next-review) - date(today)).days) + " days" AS "Time Remaining"
FROM ""
WHERE next-review != null
    AND date(next-review) > date(today) + dur(7 days)
    AND date(next-review) <= date(today) + dur(30 days)
SORT next-review ASC
```

### Review History (Last 7 Days)

```dataview
TABLE
    maturity AS "Maturity",
    review-count AS "Total Reviews",
    modified AS "Last Reviewed"
FROM ""
WHERE date(modified) >= date(today) - dur(7 days)
    AND review-count > 0
SORT modified DESC
LIMIT 15
```
`````

---

## Component 1.4: Tag Taxonomy Navigator

````markdown
## 🏷️ Tag Taxonomy Overview

### Meta-Dimension Tags

**Type Distribution**:
```dataview
TABLE
    rows.file.link AS "Notes",
    length(rows) AS "Count"
FROM ""
WHERE type != null
GROUP BY type
SORT length(rows) DESC
```

**Status Tracking**:
- 🌱 Seedling: `= length(filter(pages(), (p) => contains(p.tags, "status/seedling") OR p.maturity = "seedling"))` notes
- 🚧 In Progress: `= length(filter(pages(), (p) => contains(p.tags, "status/in-progress")))` notes
- ✅ Complete: `= length(filter(pages(), (p) => contains(p.tags, "status/complete")))` notes
- ⭐ Evergreen: `= length(filter(pages(), (p) => contains(p.tags, "status/evergreen") OR p.maturity = "evergreen"))` notes

### Domain Tags (L1/L2)

```dataview
TABLE WITHOUT ID
    choice(contains(string(tags), "cognitive-science"), "🧠", choice(contains(string(tags), "prompt-engineering"), "💬", choice(contains(string(tags), "pkm"), "💎", choice(contains(string(tags), "cosmology"), "🌌", "📄")))) AS "Icon",
    file.link AS "Note",
    maturity AS "Maturity"
FROM ""
WHERE contains(tags, "cognitive-science") OR contains(tags, "prompt-engineering") OR contains(tags, "pkb") OR contains(tags, "pkm") OR contains(tags, "cosmology")
SORT file.mtime DESC
LIMIT 20
```

### Sub-Domain Tags (L3 Parent Paths)

**PKM/PKB Paths** (`GROUP C1`):
```dataview
LIST
FROM ""
WHERE contains(string(tags), "pkb/") OR contains(string(tags), "pkm/") OR contains(string(tags), "obsidian/")
SORT file.mtime DESC
LIMIT 15
```

**Cognitive Science Paths** (`GROUP C2`):
```dataview
LIST
FROM ""
WHERE contains(string(tags), "cognitive-science/") OR contains(string(tags), "learning-theory/") OR contains(string(tags), "self-regulation/")
SORT file.mtime DESC
LIMIT 15
```
````

---

## Component 1.5: Network Analytics

`````markdown
## 🕸️ Knowledge Graph Analytics

### Hub Notes (Highest Connectivity)

```dataview
TABLE
    length(file.inlinks) AS "⬅️ Backlinks",
    length(file.outlinks) AS "➡️ Outlinks",
    length(file.inlinks) + length(file.outlinks) AS "🔗 Total",
    maturity AS "Maturity"
FROM ""
WHERE length(file.inlinks) + length(file.outlinks) > 5
SORT (length(file.inlinks) + length(file.outlinks)) DESC
LIMIT 20
```

### Orphan Notes (Needs Linking)

```dataview
TABLE
    type AS "Type",
    maturity AS "Maturity",
    file.ctime AS "Created"
FROM ""
WHERE length(file.inlinks) = 0
    AND type != "moc"
    AND type != "fleeting"
SORT file.ctime DESC
LIMIT 15
```

### Recently Connected Notes

```dataview
TABLE
    length(file.inlinks) AS "Backlinks",
    length(file.outlinks) AS "Outlinks",
    file.mtime AS "Modified"
FROM ""
WHERE date(file.mtime) >= date(today) - dur(7 days)
    AND (length(file.inlinks) > 0 OR length(file.outlinks) > 0)
SORT file.mtime DESC
LIMIT 15
```

### Link-Up MOC Network

**Primary Domain Hubs**:
- [[artificial-intelligence-moc]] → `= length(filter(pages(), (p) => contains(p.link-up, "artificial-intelligence-moc")))` notes
- [[cognitive-science-moc]] → `= length(filter(pages(), (p) => contains(p.link-up, "cognitive-science-moc")))` notes
- [[cosmology-moc]] → `= length(filter(pages(), (p) => contains(p.link-up, "cosmology-moc")))` notes
- [[prompt-engineering-moc]] → `= length(filter(pages(), (p) => contains(p.link-up, "prompt-engineering-moc")))` notes
- [[pkb-&-pkm-moc]] → `= length(filter(pages(), (p) => contains(p.link-up, "pkb-&-pkm-moc")))` notes
`````

---

## Component 1.6: Source & Context Tracker

`````markdown
## 📚 Source Distribution & Context Analysis

### Source Origins

```dataview
TABLE
    rows.file.link AS "Notes",
    length(rows) AS "Count"
FROM ""
WHERE source != null
GROUP BY source
SORT length(rows) DESC
```

### AI-Generated Content Tracking

**Claude-Sourced**:
```dataview
TABLE
    type AS "Type",
    maturity AS "Maturity",
    file.ctime AS "Created"
FROM ""
WHERE source = "claude-opus-4.1" OR source = "claude-sonnet-4.5"
SORT file.ctime DESC
LIMIT 10
```

**Gemini-Sourced**:
```dataview
TABLE
    type AS "Type",
    maturity AS "Maturity",
    file.ctime AS "Created"
FROM ""
WHERE contains(source, "gemini")
SORT file.ctime DESC
LIMIT 10
```

### Context Distribution

- 📖 Reference: `= length(filter(pages(), (p) => contains(p.tags, "context/reference")))` notes
- 🔬 Research: `= length(filter(pages(), (p) => contains(p.tags, "context/research")))` notes
- 🛠️ Applied: `= length(filter(pages(), (p) => contains(p.tags, "context/applied")))` notes
- 📚 Tutorial: `= length(filter(pages(), (p) => contains(p.tags, "context/tutorial")))` notes
`````

---

# 2️⃣ DATAVIEW BLOCK QUERIES

## Component 2.1: Active Projects Master List

````markdown
## 🚀 Active Projects

```dataview
TABLE WITHOUT ID
    file.link AS "Project",
    choice(maturity = "seedling", "🌱", choice(maturity = "budding", "🌿", choice(maturity = "developing", "🌳", "🌲"))) AS "📊",
    confidence AS "Confidence",
    source AS "Source",
    next-review AS "Next Review",
    choice(date(today) - date(file.mtime) < dur(7 days), "🔥", choice(date(today) - date(file.mtime) < dur(30 days), "✅", "🕸️")) AS "Activity"
FROM ""
WHERE (type = "dashboard" OR type = "claude-project" OR type = "gemini-gem" OR type = "report" OR type = "pkb-report" OR type = "prompt-report" OR type = "cog-sci-report")
    AND (maturity != "archived" AND maturity != "complete")
SORT file.mtime DESC
LIMIT 25
```
````

---

## Component 2.2: Domain-Filtered Research Notes

````markdown
## 🧠 Cognitive Science Notes

```dataview
TABLE
    choice(maturity = "seedling", "🌱", choice(maturity = "budding", "🌿", choice(maturity = "developing", "🌳", "🌲"))) AS "Maturity",
    choice(confidence = "speculative", "❓", choice(confidence = "provisional", "⚠️", choice(confidence = "moderate", "➡️", choice(confidence = "high", "✅", "⭐")))) AS "Confidence",
    type AS "Type",
    review-count AS "Reviews",
    round((date(today) - date(file.ctime)).days) AS "Age (days)"
FROM #cognitive-science OR #cognitive-psychology OR #neuroscience OR #learning-theory
WHERE type != "moc"
SORT file.mtime DESC
LIMIT 30
```

## 💬 Prompt Engineering Collection

```dataview
TABLE
    maturity AS "Maturity",
    confidence AS "Confidence",
    source AS "Source",
    choice(contains(string(tags), "prompting-technique"), "🎯 Technique", choice(contains(string(tags), "prompt-pattern"), "📋 Pattern", choice(contains(string(tags), "llm-"), "🤖 LLM", "💡 General"))) AS "Category"
FROM #prompt-engineering
WHERE type != "moc"
SORT file.mtime DESC
LIMIT 30
```

## 💎 PKB System Notes

```dataview
TABLE
    maturity AS "Maturity",
    choice(contains(string(tags), "obsidian"), "💎 Obsidian", choice(contains(string(tags), "dataview"), "📊 Dataview", choice(contains(string(tags), "templater"), "📝 Templater", "🔧 General"))) AS "Tool",
    type AS "Type",
    file.mtime AS "Modified"
FROM #pkb OR #pkm OR #obsidian OR #zettelkasten OR #dataview OR #templater
WHERE type != "moc"
SORT file.mtime DESC
LIMIT 30
```
````

---

## Component 2.3: Maturity-Based Review Queues

````markdown
## 🌱 Seedling Notes (Weekly Review Required)

```dataview
TABLE
    type AS "Type",
    confidence AS "Confidence",
    next-review AS "Next Review",
    review-count AS "Reviews",
    choice(date(next-review) < date(today), "🚨 OVERDUE", choice(date(next-review) <= date(today) + dur(3 days), "⚠️ Soon", "✅ Scheduled")) AS "Status"
FROM ""
WHERE maturity = "seedling"
    AND next-review != null
SORT next-review ASC
LIMIT 20
```

## 🌿 Budding Notes (Bi-weekly Review)

```dataview
TABLE
    type AS "Type",
    confidence AS "Confidence",
    next-review AS "Next Review",
    review-count AS "Reviews",
    round((date(today) - date(file.ctime)).days) AS "Age"
FROM ""
WHERE maturity = "budding"
    AND next-review != null
SORT next-review ASC
LIMIT 20
```

## 🌳 Developing Notes (Monthly Review)

```dataview
TABLE
    type AS "Type",
    confidence AS "Confidence",
    next-review AS "Next Review",
    review-count AS "Reviews"
FROM ""
WHERE maturity = "developing"
    AND next-review != null
SORT next-review ASC
LIMIT 20
```

## 🌲 Evergreen Notes (Quarterly Audit)

```dataview
TABLE
    type AS "Type",
    confidence AS "Confidence",
    review-count AS "Total Reviews",
    file.mtime AS "Last Modified"
FROM ""
WHERE maturity = "evergreen"
SORT file.mtime DESC
LIMIT 20
```
````

---

## Component 2.4: Temporal Analysis Queries

````markdown
## 📅 Created This Week

```dataview
TABLE
    type AS "Type",
    maturity AS "Maturity",
    source AS "Source",
    file.ctime AS "Created"
FROM ""
WHERE date(file.ctime) >= date(today) - dur(7 days)
SORT file.ctime DESC
```

## ✏️ Modified This Week

```dataview
TABLE
    type AS "Type",
    maturity AS "Maturity",
    file.ctime AS "Originally Created",
    file.mtime AS "Last Modified",
    round((date(today) - date(file.ctime)).days) AS "Age"
FROM ""
WHERE date(file.mtime) >= date(today) - dur(7 days)
    AND date(file.ctime) < date(file.mtime) - dur(1 days)
SORT file.mtime DESC
```

## 🕸️ Stale Notes (90+ Days Untouched)

```dataview
TABLE
    type AS "Type",
    maturity AS "Maturity",
    file.mtime AS "Last Modified",
    round((date(today) - date(file.mtime)).days) AS "Days Stale",
    choice(length(file.inlinks) = 0, "🔴 Orphan", choice(length(file.inlinks) < 3, "🟡 Low Links", "🟢 Connected")) AS "Link Status"
FROM ""
WHERE date(today) - date(file.mtime) > dur(90 days)
    AND type != "moc"
    AND type != "fleeting"
SORT (date(today) - date(file.mtime)).days DESC
LIMIT 30
```

## 🔄 High-Activity Notes (Most Reviews)

```dataview
TABLE
    review-count AS "Total Reviews",
    maturity AS "Maturity",
    confidence AS "Confidence",
    file.ctime AS "Created",
    file.mtime AS "Last Modified"
FROM ""
WHERE review-count > 5
SORT review-count DESC
LIMIT 20
```
````

---

## Component 2.5: Tag-Based Discovery Queries

````markdown
## 🏷️ Recent Notes by Primary Tag

### Type: Reports

```dataview
TABLE
    choice(type = "cog-sci-report", "🧠 Cognitive", choice(type = "prompt-report", "💬 Prompting", choice(type = "pkb-report", "💎 PKB", choice(type = "cosmo-report", "🌌 Cosmology", "📊 General")))) AS "Category",
    maturity AS "Maturity",
    confidence AS "Confidence",
    file.ctime AS "Created"
FROM ""
WHERE contains(type, "report")
SORT file.ctime DESC
LIMIT 20
```

### Mode: Analytical vs Practical

**Analytical Mode**:
```dataview
TABLE
    type AS "Type",
    maturity AS "Maturity",
    file.mtime AS "Modified"
FROM ""
WHERE contains(string(tags), "mode/analytical")
SORT file.mtime DESC
LIMIT 15
```

**Practical Mode**:
```dataview
TABLE
    type AS "Type",
    maturity AS "Maturity",
    file.mtime AS "Modified"
FROM ""
WHERE contains(string(tags), "mode/practical")
SORT file.mtime DESC
LIMIT 15
```

### Nature: Conceptual vs Procedural

```dataview
TABLE
    choice(contains(string(tags), "nature/conceptual"), "💡 Conceptual", choice(contains(string(tags), "nature/procedural"), "⚙️ Procedural", choice(contains(string(tags), "nature/declarative"), "📋 Declarative", "🔄 Reflective"))) AS "Nature",
    type AS "Type",
    maturity AS "Maturity"
FROM ""
WHERE contains(string(tags), "nature/")
SORT file.mtime DESC
LIMIT 20
```
````

---

## Component 2.6: Cross-Reference & Linking Analysis

````markdown
## 🔗 Highly Connected Notes (Network Hubs)

```dataview
TABLE
    length(file.inlinks) AS "⬅️ In",
    length(file.outlinks) AS "➡️ Out",
    length(file.inlinks) + length(file.outlinks) AS "Total",
    maturity AS "Mat",
    choice(type = "moc", "🗺️ MOC", choice(type = "reference", "📚 Ref", "📄 Note")) AS "Type"
FROM ""
WHERE length(file.inlinks) + length(file.outlinks) >= 10
SORT (length(file.inlinks) + length(file.outlinks)) DESC
LIMIT 25
```

## 🎯 Notes Linking to Specific MOC

**Cognitive Science MOC Network**:
```dataview
LIST
FROM [[cognitive-science-moc]]
SORT file.mtime DESC
LIMIT 20
```

**Prompt Engineering MOC Network**:
```dataview
LIST
FROM [[prompt-engineering-moc]]
SORT file.mtime DESC
LIMIT 20
```

## 🔍 Orphan Detection (Zero Backlinks)

```dataview
TABLE
    type AS "Type",
    maturity AS "Maturity",
    length(file.outlinks) AS "Outlinks",
    round((date(today) - date(file.ctime)).days) AS "Age"
FROM ""
WHERE length(file.inlinks) = 0
    AND type != "moc"
    AND type != "fleeting"
    AND type != "dashboard"
SORT file.ctime DESC
LIMIT 25
```
````

---

# 3️⃣ DATAVIEW INLINE QUERIES

## Component 3.1: Metadata Display Inline Queries

````markdown
## 📊 Note Metadata Dashboard

| Metric | Value |
|--------|-------|
| **Development Status** | `= choice(this.maturity = "seedling", "🌱 Seedling", choice(this.maturity = "budding", "🌿 Budding", choice(this.maturity = "developing", "🌳 Developing", "🌲 Evergreen")))` |
| **Epistemic Confidence** | `= choice(this.confidence = "speculative", "❓ Speculative", choice(this.confidence = "provisional", "⚠️ Provisional", choice(this.confidence = "moderate", "➡️ Moderate", choice(this.confidence = "high", "✅ High", "⭐ Established"))))` |
| **Note Type** | `= this.type` |
| **Primary Source** | `= this.source` |
| **Created** | `= this.created` |
| **Last Modified** | `= this.modified` |
| **Note Age** | `= round((date(today) - date(this.created)).days)` days old |
| **Days Since Update** | `= round((date(today) - date(this.modified)).days)` days ago |
| **Next Review** | `= this.next-review` |
| **Review Count** | `= this.review-count` reviews |
| **Backlinks** | `= length(this.file.inlinks)` notes link here |
| **Outlinks** | `= length(this.file.outlinks)` notes linked from here |
| **Total Connectivity** | `= length(this.file.inlinks) + length(this.file.outlinks)` connections |
```

---

## Component 3.2: Conditional Status Indicators

```markdown
## 🎯 Status Indicators

**Review Status**: `= choice(date(this.next-review) < date(today), "🚨 OVERDUE - Review Needed", choice(date(this.next-review) <= date(today) + dur(3 days), "⚠️ DUE SOON - Within 3 Days", "✅ On Schedule"))`

**Maturity Progress**: `= choice(this.maturity = "seedling", "🌱 Early Stage - Needs Weekly Reviews", choice(this.maturity = "budding", "🌿 Growing - Bi-weekly Reviews", choice(this.maturity = "developing", "🌳 Maturing - Monthly Reviews", "🌲 Stable - Quarterly Audits")))`

**Confidence Level**: `= choice(this.confidence = "speculative" OR this.confidence = "provisional", "⚠️ LOW CONFIDENCE - Verify Claims", choice(this.confidence = "moderate", "➡️ MODERATE - Generally Reliable", "✅ HIGH CONFIDENCE - Well-Validated"))`

**Activity Status**: `= choice(date(today) - date(this.modified) < dur(7 days), "🔥 FRESH - Recently Updated", choice(date(today) - date(this.modified) < dur(30 days), "✅ ACTIVE - Current", choice(date(today) - date(this.modified) < dur(90 days), "🕐 AGING - Consider Review", "🕸️ STALE - Needs Attention")))`

**Link Health**: `= choice(length(this.file.inlinks) = 0, "🔴 ORPHAN - No Backlinks", choice(length(this.file.inlinks) < 3, "🟡 ISOLATED - Few Connections", choice(length(this.file.inlinks) < 10, "🟢 CONNECTED - Good Integration", "⭐ HUB - Highly Connected")))`

**Network Position**: `= choice(length(this.file.inlinks) + length(this.file.outlinks) > 20, "🌐 MAJOR HUB - Central to Knowledge Graph", choice(length(this.file.inlinks) + length(this.file.outlinks) > 10, "🔗 CONNECTOR - Well-Integrated", choice(length(this.file.inlinks) + length(this.file.outlinks) > 5, "🌱 NODE - Developing Connections", "📄 ISOLATED - Minimal Links")))`
````

---

## Component 3.3: Dynamic Counters & Aggregations

````markdown
## 📈 Vault Statistics

**Total Note Count**: `= length(pages())` notes in vault

**Domain Breakdown**:
- 🧠 Cognitive Science: `= length(filter(pages(), (p) => contains(p.tags, "cognitive-science")))` notes
- 💬 Prompt Engineering: `= length(filter(pages(), (p) => contains(p.tags, "prompt-engineering")))` notes
- 💎 PKB/PKM: `= length(filter(pages(), (p) => contains(p.tags, "pkb") OR contains(p.tags, "pkm") OR contains(p.tags, "obsidian")))` notes
- 🌌 Cosmology: `= length(filter(pages(), (p) => contains(p.tags, "cosmology")))` notes

**Type Distribution**:
- 📚 Reference Notes: `= length(filter(pages(), (p) => p.type = "reference"))` 
- 💡 Permanent Notes: `= length(filter(pages(), (p) => p.type = "permanent-note" OR p.type = "permanent"))` 
- 📊 Reports: `= length(filter(pages(), (p) => contains(p.type, "report")))` 
- 🗺️ MOCs: `= length(filter(pages(), (p) => p.type = "moc"))` 
- 🌱 Fleeting: `= length(filter(pages(), (p) => p.type = "fleeting"))` 

**Maturity Distribution**:
- 🌱 Seedling: `= length(filter(pages(), (p) => p.maturity = "seedling"))` (`= round(length(filter(pages(), (p) => p.maturity = "seedling")) / length(pages()) * 100)`%)
- 🌿 Budding: `= length(filter(pages(), (p) => p.maturity = "budding"))` (`= round(length(filter(pages(), (p) => p.maturity = "budding")) / length(pages()) * 100)`%)
- 🌳 Developing: `= length(filter(pages(), (p) => p.maturity = "developing"))` (`= round(length(filter(pages(), (p) => p.maturity = "developing")) / length(pages()) * 100)`%)
- 🌲 Evergreen: `= length(filter(pages(), (p) => p.maturity = "evergreen"))` (`= round(length(filter(pages(), (p) => p.maturity = "evergreen")) / length(pages()) * 100)`%)

**Review Queue Size**: `= length(filter(pages(), (p) => p.next-review != null AND date(p.next-review) <= date(today)))` notes due for review

**This Week's Activity**:
- ➕ Created: `= length(filter(pages(), (p) => date(p.created) >= date(today) - dur(7 days)))` new notes
- ✏️ Modified: `= length(filter(pages(), (p) => date(p.modified) >= date(today) - dur(7 days)))` updated notes
- 🔄 Reviewed: `= sum(filter(pages(), (p) => date(p.modified) >= date(today) - dur(7 days)).review-count)` total reviews completed
````

---

## Component 3.4: Temporal Calculations

````markdown
## ⏰ Time-Based Analytics

**Note Lifecycle**:
- Created `= round((date(today) - date(this.created)).days)` days ago on `= this.created`
- Last modified `= round((date(today) - date(this.modified)).days)` days ago on `= this.modified`
- Time between creation and last edit: `= round((date(this.modified) - date(this.created)).days)` days

**Review Scheduling**:
- Next review scheduled for: `= this.next-review`
- Days until next review: `= choice(date(this.next-review) != null, round((date(this.next-review) - date(today)).days), "Not scheduled")`
- Review status: `= choice(date(this.next-review) < date(today), "⚠️ OVERDUE", "✅ On schedule")`
- Days overdue: `= choice(date(this.next-review) < date(today), round((date(today) - date(this.next-review)).days), 0)`

**Activity Metrics**:
- Total reviews completed: `= this.review-count`
- Average days between reviews: `= choice(this.review-count > 0, round((date(today) - date(this.created)).days / this.review-count), "N/A")`
- Staleness indicator: `= choice(date(today) - date(this.modified) > dur(180 days), "🕸️ VERY STALE (180+ days)", choice(date(today) - date(this.modified) > dur(90 days), "🕐 STALE (90+ days)", choice(date(today) - date(this.modified) > dur(30 days), "🕐 AGING (30+ days)", "✅ FRESH")))`

**Temporal Context**:
- Created in week: `= this.week`
- Created in month: `= this.month`
- Created in quarter: `= this.quarter`
- Created in year: `= this.year`
```

---

## Component 3.5: Progress Calculations & Percentages

````markdown
## 📊 Progress Indicators

**Maturity Progress Bar**:
Progress toward Evergreen: `= "<progress value='" + choice(this.maturity = "seedling", "25", choice(this.maturity = "budding", "50", choice(this.maturity = "developing", "75", "100"))) + "' max='100'></progress> " + choice(this.maturity = "seedling", "25%", choice(this.maturity = "budding", "50%", choice(this.maturity = "developing", "75%", "100%")))`

**Confidence Progress**:
Epistemic Certainty: `= "<progress value='" + choice(this.confidence = "speculative", "20", choice(this.confidence = "provisional", "40", choice(this.confidence = "moderate", "60", choice(this.confidence = "high", "80", "100")))) + "' max='100'></progress> " + choice(this.confidence = "speculative", "20%", choice(this.confidence = "provisional", "40%", choice(this.confidence = "moderate", "60%", choice(this.confidence = "high", "80%", "100%"))))`

**Review Completion Rate**:
Reviews Completed: `= this.review-count` of `= choice(this.maturity = "seedling", round((date(today) - date(this.created)).weeks), choice(this.maturity = "budding", round((date(today) - date(this.created)).weeks / 2), choice(this.maturity = "developing", round((date(today) - date(this.created)).months), round((date(today) - date(this.created)).months / 3))))` expected

**Link Density Score**:
Connection Score: `= round((length(this.file.inlinks) + length(this.file.outlinks)) / length(pages()) * 100, 1)`% of vault connected

**Domain Coverage**:
Tags Applied: `= length(this.tags)` tags from 577-tag taxonomy (`= round(length(this.tags) / 577 * 100, 1)`% coverage)
````

---

## Component 3.6: Contextual Reference Displays

````markdown
## 🔗 Contextual References

**Link-Up MOC**: Connected to `= this.link-up` for navigation

**Related Notes**: 
- This note connects to `= length(this.file.outlinks)` other notes
- `= length(this.file.inlinks)` notes reference this one
- Total graph position: `= length(this.file.inlinks) + length(this.file.outlinks)` connections

**Same Domain Notes**: 
`= length(filter(pages(), (p) => contains(string(p.tags), split(string(this.tags), ",")[3]))))` other notes in same primary domain

**Same Maturity Level**: 
`= length(filter(pages(), (p) => p.maturity = this.maturity)) - 1` other notes at `= this.maturity` level

**Same Confidence Level**:
`= length(filter(pages(), (p) => p.confidence = this.confidence)) - 1` other notes with `= this.confidence` confidence

**Created Same Week**:
`= length(filter(pages(), (p) => p.week = this.week)) - 1` other notes created during `= this.week`

**Source Siblings**: 
`= length(filter(pages(), (p) => p.source = this.source)) - 1` other notes from `= this.source`
````

---

# 4️⃣ META BIND INTERACTIVE BUTTONS

## Component 4.1: Maturity Progression System

````markdown
## 🌱 Development Status Controls

**Current Maturity**: `VIEW[{maturity}]`

`BUTTON[mat-seedling]` `BUTTON[mat-budding]` `BUTTON[mat-developing]` `BUTTON[mat-evergreen]`

---

**Button Template Configurations** (Add to Settings → Meta Bind → Button Templates):

```yaml
# Button 1: Seedling
id: mat-seedling
label: 🌱 Seedling
style: default
action:
  type: updateMetadata
  bindTarget: maturity
  evaluate: false
  value: seedling
```

```yaml
# Button 2: Budding
id: mat-budding
label: 🌿 Budding
style: default
action:
  type: updateMetadata
  bindTarget: maturity
  evaluate: false
  value: budding
```

```yaml
# Button 3: Developing
id: mat-developing
label: 🌳 Developing
style: primary
action:
  type: updateMetadata
  bindTarget: maturity
  evaluate: false
  value: developing
```

```yaml
# Button 4: Evergreen
id: mat-evergreen
label: 🌲 Evergreen
style: primary
action:
  type: updateMetadata
  bindTarget: maturity
  evaluate: false
  value: evergreen
```
````

---

## Component 4.2: Confidence Level Toggle

````markdown
## 🎯 Epistemic Confidence Controls

**Current Confidence**: `VIEW[{confidence}]`

`BUTTON[conf-spec]` `BUTTON[conf-prov]` `BUTTON[conf-mod]` `BUTTON[conf-high]` `BUTTON[conf-est]`

---

**Button Templates**:

```yaml
# Speculative
id: conf-spec
label: ❓ Speculative
style: default
action:
  type: updateMetadata
  bindTarget: confidence
  evaluate: false
  value: speculative
```

```yaml
# Provisional
id: conf-prov
label: ⚠️ Provisional
style: default
action:
  type: updateMetadata
  bindTarget: confidence
  evaluate: false
  value: provisional
```

```yaml
# Moderate
id: conf-mod
label: ➡️ Moderate
style: default
action:
  type: updateMetadata
  bindTarget: confidence
  evaluate: false
  value: moderate
```

```yaml
# High
id: conf-high
label: ✅ High
style: primary
action:
  type: updateMetadata
  bindTarget: confidence
  evaluate: false
  value: high
```

```yaml
# Established
id: conf-est
label: ⭐ Established
style: primary
action:
  type: updateMetadata
  bindTarget: confidence
  evaluate: false
  value: established
```
````

---

## Component 4.3: Smart Review Completion Button

````markdown
## 📅 Review System

**Last Review**: `VIEW[{modified}]`  
**Next Review**: `VIEW[{next-review}]`  
**Total Reviews**: `VIEW[{review-count}]`

`BUTTON[complete-review]`

---

**Button Template** (Advanced - Maturity-Based Scheduling):

```yaml
id: complete-review
label: ✅ Complete Review
style: primary
actions:
  # Step 1: Increment review counter
  - type: updateMetadata
    bindTarget: review-count
    evaluate: true
    value: "meta['review-count'] + 1"
  
  # Step 2: Update modified timestamp
  - type: updateMetadata
    bindTarget: modified
    evaluate: true
    value: "date.now"
  
  # Step 3: Calculate next review based on maturity
  - type: updateMetadata
    bindTarget: next-review
    evaluate: true
    value: |
      const maturity = meta.maturity;
      const today = moment();
      if (maturity === "seedling") {
        return today.add(7, 'days').format("YYYY-MM-DD");
      } else if (maturity === "budding") {
        return today.add(14, 'days').format("YYYY-MM-DD");
      } else if (maturity === "developing") {
        return today.add(30, 'days').format("YYYY-MM-DD");
      } else if (maturity === "evergreen") {
        return today.add(90, 'days').format("YYYY-MM-DD");
      } else {
        return today.add(7, 'days').format("YYYY-MM-DD");
      }
```

**How It Works**:
1. Increments `review-count` by 1
2. Updates `modified` to current timestamp
3. Calculates next review based on maturity level:
   - 🌱 Seedling → 7 days
   - 🌿 Budding → 14 days
   - 🌳 Developing → 30 days
   - 🌲 Evergreen → 90 days
````

---

## Component 4.4: Quick Action Toolbar

````markdown
## ⚡ Quick Actions

| Action | Button |
|--------|--------|
| Archive Note | `BUTTON[quick-archive]` |
| Mark Complete | `BUTTON[quick-complete]` |
| Reset to Seedling | `BUTTON[quick-reset]` |
| Boost Confidence | `BUTTON[quick-boost-conf]` |
| Add to Review Queue | `BUTTON[quick-add-review]` |

---

**Button Templates**:

```yaml
# Archive Note
id: quick-archive
label: 📦 Archive
style: default
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: archived
  - type: updateMetadata
    bindTarget: tags
    evaluate: false
    value: "[\"type/archived\"]"
```

```yaml
# Mark Complete
id: quick-complete
label: ✅ Complete
style: primary
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: evergreen
  - type: updateMetadata
    bindTarget: confidence
    evaluate: false
    value: established
  - type: updateMetadata
    bindTarget: modified
    evaluate: true
    value: "date.now"
```

```yaml
# Reset to Seedling
id: quick-reset
label: 🔄 Reset
style: default
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: seedling
  - type: updateMetadata
    bindTarget: confidence
    evaluate: false
    value: provisional
  - type: updateMetadata
    bindTarget: review-count
    evaluate: false
    value: 0
```

```yaml
# Boost Confidence
id: quick-boost-conf
label: ⬆️ Boost Confidence
style: default
action:
  type: updateMetadata
  bindTarget: confidence
  evaluate: true
  value: |
    const current = meta.confidence;
    if (current === "speculative") return "provisional";
    if (current === "provisional") return "moderate";
    if (current === "moderate") return "high";
    if (current === "high") return "established";
    return current;
```

```yaml
# Add to Review Queue
id: quick-add-review
label: 📅 Schedule Review
style: default
actions:
  - type: updateMetadata
    bindTarget: next-review
    evaluate: true
    value: "moment().add(7, 'days').format('YYYY-MM-DD')"
```
````

---

## Component 4.5: Type Selector Buttons

````markdown
## 📑 Note Type Controls

**Current Type**: `VIEW[{type}]`

### Primary Types
`BUTTON[type-perm]` `BUTTON[type-ref]` `BUTTON[type-lit]` `BUTTON[type-fleet]`

### Report Types
`BUTTON[type-cog-report]` `BUTTON[type-prompt-report]` `BUTTON[type-pkb-report]`

---

**Button Templates**:

```yaml
id: type-perm
label: 💡 Permanent
style: default
action:
  type: updateMetadata
  bindTarget: type
  evaluate: false
  value: permanent-note
```

```yaml
id: type-ref
label: 📚 Reference
style: default
action:
  type: updateMetadata
  bindTarget: type
  evaluate: false
  value: reference
```

```yaml
id: type-lit
label: 📖 Literature
style: default
action:
  type: updateMetadata
  bindTarget: type
  evaluate: false
  value: literature
```

```yaml
id: type-fleet
label: 🌱 Fleeting
style: default
action:
  type: updateMetadata
  bindTarget: type
  evaluate: false
  value: fleeting
```

```yaml
id: type-cog-report
label: 🧠 Cog-Sci Report
style: primary
action:
  type: updateMetadata
  bindTarget: type
  evaluate: false
  value: cog-sci-report
```

```yaml
id: type-prompt-report
label: 💬 Prompt Report
style: primary
action:
  type: updateMetadata
  bindTarget: type
  evaluate: false
  value: prompt-report
```

```yaml
id: type-pkb-report
label: 💎 PKB Report
style: primary
action:
  type: updateMetadata
  bindTarget: type
  evaluate: false
  value: pkb-report
```
````

---

## Component 4.6: Multi-Action Workflow Buttons

`````markdown
## 🎯 Advanced Workflows

**Finalize Note** (Complete → Evergreen → High Confidence → Schedule Long Review):  
`BUTTON[workflow-finalize]`

**Quick Review** (Increment Counter → Update Timestamp → Next Review +7 Days):  
`BUTTON[workflow-quick-review]`

**Promote Note** (Advance Maturity → Boost Confidence → Update Tags):  
`BUTTON[workflow-promote]`

---

**Button Templates**:

```yaml
id: workflow-finalize
label: 🏁 Finalize Note
style: primary
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: evergreen
  - type: updateMetadata
    bindTarget: confidence
    evaluate: false
    value: high
  - type: updateMetadata
    bindTarget: modified
    evaluate: true
    value: "date.now"
  - type: updateMetadata
    bindTarget: next-review
    evaluate: true
    value: "moment().add(90, 'days').format('YYYY-MM-DD')"
  - type: updateMetadata
    bindTarget: tags
    evaluate: true
    value: |
      const currentTags = meta.tags || [];
      if (!currentTags.includes("status/complete")) {
        currentTags.push("status/complete");
      }
      return currentTags;
```

```yaml
id: workflow-quick-review
label: ⚡ Quick Review
style: default
actions:
  - type: updateMetadata
    bindTarget: review-count
    evaluate: true
    value: "meta['review-count'] + 1"
  - type: updateMetadata
    bindTarget: modified
    evaluate: true
    value: "date.now"
  - type: updateMetadata
    bindTarget: next-review
    evaluate: true
    value: "moment().add(7, 'days').format('YYYY-MM-DD')"
```

```yaml
id: workflow-promote
label: ⬆️ Promote Note
style: primary
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: true
    value: |
      const current = meta.maturity;
      if (current === "seedling") return "budding";
      if (current === "budding") return "developing";
      if (current === "developing") return "evergreen";
      return current;
  - type: updateMetadata
    bindTarget: confidence
    evaluate: true
    value: |
      const current = meta.confidence;
      if (current === "speculative") return "provisional";
      if (current === "provisional") return "moderate";
      if (current === "moderate") return "high";
      return current;
  - type: updateMetadata
    bindTarget: modified
    evaluate: true
    value: "date.now"
```
`````

---

# 5️⃣ TEMPLATER INITIALIZATION LOGIC

## Component 5.1: Research Project Template

````javascript
<%*
/* ═════════════════════════════════════════════════════════════════════
   RESEARCH PROJECT INITIALIZATION TEMPLATE
   Extends your master template for project-specific needs
   ═════════════════════════════════════════════════════════════════════ */
// ─────────────────────────────────────────────────────────────────────
// STEP 1: BASIC PROJECT INFORMATION
// ─────────────────────────────────────────────────────────────────────
const projectTitle = await tp.system.prompt("Enter Project Title:");
if (projectTitle == null) { return; }
const projectGoal = await tp.system.prompt("What is the primary goal/research question?");
const projectScope = await tp.system.prompt("Define scope (what's included/excluded):");
// ─────────────────────────────────────────────────────────────────────
// STEP 2: PROJECT-SPECIFIC METADATA
// ─────────────────────────────────────────────────────────────────────
const projectType = await tp.system.suggester(
    ["🧠 Cognitive Science Research", "💬 Prompt Engineering Project", "💎 PKB System Development", "🌌 Cosmology Study", "🔬 General Research"],
    ["cog-sci-report", "prompt-report", "pkb-report", "cosmo-report", "research"],
    false,
    "Select Project Type:"
);
const projectDomain = await tp.system.suggester(
    ["cognitive-science", "prompt-engineering", "pkb", "pkm", "cosmology", "multi-domain"],
    ["cognitive-science", "prompt-engineering", "pkb", "pkm", "cosmology", "multi-domain"],
    false,
    "Select Primary Domain:"
);
const projectPriority = await tp.system.suggester(
    ["🔴 High Priority", "🟡 Medium Priority", "🟢 Low Priority"],
    ["high", "medium", "low"],
    false,
    "Set Project Priority:"
);
const projectStatus = await tp.system.suggester(
    ["Planning", "Active Research", "Analysis", "Writing", "Review", "Complete"],
    ["planning", "active", "analysis", "writing", "review", "complete"],
    false,
    "Current Project Status:"
);
// ─────────────────────────────────────────────────────────────────────
// STEP 3: TIMELINE SETUP
// ─────────────────────────────────────────────────────────────────────
const startDate = tp.date.now("YYYY-MM-DD");
const targetDuration = await tp.system.prompt("Target duration in days (e.g., 30, 60, 90):");
const targetEndDate = tp.date.now("YYYY-MM-DD", parseInt(targetDuration));
// ─────────────────────────────────────────────────────────────────────
// STEP 4: LINK-UP MOCs (FROM YOUR MASTER TEMPLATE)
// ─────────────────────────────────────────────────────────────────────
const linkUpList = [
    "[[artificial-intelligence-moc]]",
    "[[cognitive-science-moc]]",
    "[[cosmology-moc]]",
    "[[educational-psychology-moc]]",
    "[[learning-theory-moc]]",
    "[[neuroscience-moc]]",
    "[[pkb-&-pkm-moc]]",
    "[[prompt-engineering-moc]]"
];
const linkUp = await tp.system.suggester(linkUpList, linkUpList, false, "Select Link-Up MOC:");
// ─────────────────────────────────────────────────────────────────────
// STEP 5: STANDARD METADATA (FROM YOUR MASTER TEMPLATE)
// ─────────────────────────────────────────────────────────────────────
const dateNow = tp.date.now("YYYY-MM-DD");
const timeNow = tp.date.now("HH:mm:ss");
const year = tp.date.now("YYYY");
const id = tp.date.now("YYYYMMDDHHmmss");
const maturity = "seedling"; // Projects start as seedlings
const confidence = "provisional"; // Initial confidence
const nextReview = tp.date.now("YYYY-MM-DD", 7); // Weekly reviews for new projects
_%>
---
aliases:
  - "<% projectTitle %>"
  - "<% projectTitle %> Project"
tags:
  - "type/<% projectType %>"
  - "year/<% year %>"
  - "<% projectDomain %>"
  - "status/<% projectStatus %>"
  - "priority/<% projectPriority %>"
source: "original-synthesis"
id: "<% id %>"
created: "<% dateNow %>T<% timeNow %>"
modified: "<% dateNow %>T<% timeNow %>"
week: "[[<% tp.date.now("gggg-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% year %>]]"
type: "<% projectType %>"
maturity: "<% maturity %>"
confidence: "<% confidence %>"
next-review: "<% nextReview %>"
review-count: 0
project-status: "<% projectStatus %>"
project-priority: "<% projectPriority %>"
start-date: "<% startDate %>"
target-end-date: "<% targetEndDate %>"
actual-end-date: ""
progress-percentage: 0
link-up:
  - "<% linkUp %>"
link-related:
  - "[[<% dateNow %>|Daily-Note]]"
---

# <% projectTitle %>

> [!abstract] Project Overview
> **Goal**: <% projectGoal %>
> **Scope**: <% projectScope %>
> **Status**: `= this.project-status` | **Priority**: `= this.project-priority`
> **Timeline**: `= this.start-date` → `= this.target-end-date` (`= round((date(this.target-end-date) - date(this.start-date)).days)` days)

## 📊 Project Dashboard

**Development Status**: `= this.maturity`  
**Confidence Level**: `= this.confidence`  
**Progress**: `= this.progress-percentage`%  
**Next Review**: `= this.next-review`

<progress value="<% tp.file.cursor() %>" max="100"></progress>

---

## 🎯 Research Questions

1. 
2. 
3. 

---

## 📚 Literature & Resources

### Key Papers

- [ ] Paper 1:
- [ ] Paper 2:
- [ ] Paper 3:

### Reference Materials

- 
- 
- 

---

## 🔬 Methodology

### Approach

### Data Collection

### Analysis Plan

---

## 📝 Progress Log

### <% dateNow %> - Project Initiated

**Activities**:
- 

**Insights**:
- 

**Next Steps**:
- [ ] 
- [ ] 

---

## 🔗 Related Notes

```dataview
TABLE
    type AS "Type",
    maturity AS "Maturity",
    file.mtime AS "Modified"
FROM ""
WHERE contains(link-related, this.file.link)
    OR contains(this.file.outlinks, file.link)
SORT file.mtime DESC
LIMIT 10
```

---

## 📅 Review Schedule

> [!important] Review Cadence
> - **Weekly Status Reviews**: Every Monday
> - **Monthly Deep Dive**: First Monday of month
> - **Milestone Reviews**: At each phase completion

**Review Checklist**:
- [ ] Progress vs. timeline assessment
- [ ] Research questions still relevant?
- [ ] New connections identified?
- [ ] Adjust scope if needed?
- [ ] Update maturity/confidence levels?
````

---

## Component 5.2: Domain-Specific Conditional Templates

`````javascript
<%*
/* ═════════════════════════════════════════════════════════════════════
   DOMAIN-SPECIFIC NOTE TEMPLATE
   Conditional sections based on selected domain
   ═════════════════════════════════════════════════════════════════════ */
// … [Previous master template tag selection code] …
// After tag selection, determine domain and inject appropriate sections
const primaryDomain = tag3; // tag3 is the L1/L2 domain from your master template
let domainSpecificSections = "";
// ─────────────────────────────────────────────────────────────────────
// COGNITIVE SCIENCE DOMAIN
// ─────────────────────────────────────────────────────────────────────
if (primaryDomain === "cognitive-science" || primaryDomain === "cognitive-psychology" || primaryDomain === "neuroscience") {
    domainSpecificSections = `
## 🧠 Cognitive Mechanisms
### Core Processes
**Memory Systems**:
- 
**Attention Components**:
- 
**Executive Functions**:
- 
### Neural Correlates
**Brain Regions Involved**:
- 
**Neural Pathways**:
- 
---
## 📊 Empirical Evidence
### Key Studies
\`\`\`dataview
TABLE
    source AS "Source",
    confidence AS "Confidence",
    file.ctime AS "Added"
FROM #empirical-research OR #neuroscience OR #cognitive-science
WHERE contains(file.outlinks, this.file.link)
SORT file.ctime DESC
LIMIT 10
\`\`\`
### Experimental Paradigms
- 
---
## 🎓 Educational Applications
### Learning Implications
### Instructional Design Considerations
`;
}
// ─────────────────────────────────────────────────────────────────────
// PROMPT ENGINEERING DOMAIN
// ─────────────────────────────────────────────────────────────────────
else if (primaryDomain === "prompt-engineering" || primaryDomain === "artificial-intelligence") {
    domainSpecificSections = `
## 💬 Prompt Pattern Analysis
### Core Components
**Input Structure**:
\`\`\`
[Example prompt structure]
\`\`\`
**Expected Output**:
\`\`\`
[Example output]
\`\`\`
### Variations & Adaptations
| Variation | Use Case | Effectiveness |
|-----------|----------|---------------|
|           |          |               |
---
## 🤖 Model-Specific Performance
### Claude Performance
**Strengths**:
- 
**Limitations**:
- 
### Gemini Performance
**Strengths**:
- 
**Limitations**:
- 
---
## 🎯 Optimization Strategies
### Token Efficiency
### Context Management
### Error Handling
---
## 📝 Prompt Templates
\`\`\`dataview
TABLE
    choice(contains(string(tags), "prompt-pattern"), "📋 Pattern", "💡 General") AS "Category",
    validation AS "Validation",
    file.mtime AS "Updated"
FROM #prompting-technique OR #prompt-pattern
WHERE contains(file.outlinks, this.file.link)
SORT file.mtime DESC
LIMIT 10
\`\`\`
`;
}
// ─────────────────────────────────────────────────────────────────────
// PKB/PKM DOMAIN
// ─────────────────────────────────────────────────────────────────────
else if (primaryDomain === "pkb" || primaryDomain === "pkm" || primaryDomain === "obsidian") {
    domainSpecificSections = `
## 💎 PKB Implementation
### System Architecture
**Components**:
- 
**Data Flow**:
\`\`\`mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Storage]
    C --> D[Retrieval]
\`\`\`
### Plugin Integration
| Plugin | Function | Configuration |
|--------|----------|---------------|
|        |          |               |
---
## 🔧 Technical Configuration
### Dataview Queries
\`\`\`dataview
[Example query specific to this implementation]
\`\`\`
### Templater Scripts
\`\`\`javascript
// [Example script]
\`\`\`
---
## 📊 Metrics & Analytics
**System Health**:
- Total notes: \`= length(pages())\`
- Orphan count: \`= length(filter(pages(), (p) => length(p.file.inlinks) = 0))\`
- Average connectivity: \`= round(sum(pages().file.inlinks.length) / length(pages()), 1)\`
---
## 🔗 Related Implementation Notes
\`\`\`dataview
TABLE
    choice(contains(string(tags), "dataview"), "📊 Dataview", choice(contains(string(tags), "templater"), "📝 Templater", "🔧 General")) AS "Tool",
    maturity AS "Maturity",
    file.mtime AS "Modified"
FROM #obsidian OR #dataview OR #templater OR #pkb
WHERE contains(file.outlinks, this.file.link)
SORT file.mtime DESC
LIMIT 10
\`\`\`
`;
}
// ─────────────────────────────────────────────────────────────────────
// COSMOLOGY DOMAIN
// ─────────────────────────────────────────────────────────────────────
else if (primaryDomain === "cosmology") {
    domainSpecificSections = `
## 🌌 Cosmological Context
### Theoretical Framework
**Core Principles**:
- 
**Mathematical Models**:
- 
### Observational Evidence
**Key Observations**:
- 
**Instruments/Missions**:
- 
---
## 📏 Quantitative Analysis
### Key Parameters
| Parameter | Value | Uncertainty | Source |
|-----------|-------|-------------|--------|
|           |       |             |        |
### Calculations
\`\`\`
[Relevant equations and calculations]
\`\`\`
---
## 🔭 Related Research
\`\`\`dataview
TABLE
    source AS "Source",
    confidence AS "Confidence",
    file.ctime AS "Added"
FROM #cosmology
WHERE contains(file.outlinks, this.file.link)
SORT file.ctime DESC
LIMIT 10
\`\`\`
`;
}
// ─────────────────────────────────────────────────────────────────────
// DEFAULT/MULTI-DOMAIN
// ─────────────────────────────────────────────────────────────────────
else {
    domainSpecificSections = `
## 📚 Core Content
### Key Concepts
### Relationships
### Applications
---
## 🔗 Related Notes
\`\`\`dataview
TABLE
    type AS "Type",
    maturity AS "Maturity",
    file.mtime AS "Modified"
FROM ""
WHERE contains(file.outlinks, this.file.link)
SORT file.mtime DESC
LIMIT 10
\`\`\`
`;
}
// Return the domain-specific sections to be inserted
tR += domainSpecificSections;
_%>
`````
---
## Component 5.3: Auto-Tag Suggestion Based on Content
````javascript
<%*
/* ═════════════════════════════════════════════════════════════════════
   INTELLIGENT TAG SUGGESTION SYSTEM
   Analyzes note title and suggests relevant tags from your taxonomy
   ═════════════════════════════════════════════════════════════════════ */
// Get note title
const title = await tp.system.prompt("Enter Note Title:");
if (title == null) { return; }
const titleLower = title.toLowerCase();
// ─────────────────────────────────────────────────────────────────────
// TAG SUGGESTION ENGINE
// ─────────────────────────────────────────────────────────────────────
// Keyword → Tag Mappings
const keywordTagMap = {
    // Memory-related
    "memory": ["working-memory", "episodic-memory", "semantic-memory", "cognitive-science/memory"],
    "recall": ["retrieval", "memory", "cognitive-science/memory"],
    "encoding": ["encoding", "memory", "cognitive-science/memory"],
    
    // Attention-related
    "attention": ["attention", "selective-attention", "sustained-attention", "cognitive-science/attention"],
    "focus": ["attention", "cognitive-control", "self-regulation"],
    
    // Learning-related
    "learning": ["learning-processes", "skill-acquisition", "learning-theory"],
    "spaced": ["spacing-effect", "spaced-repetition", "learning-processes"],
    "retrieval practice": ["retrieval-practice-pkm", "testing-effect", "active-recall"],
    
    // PKM-related
    "obsidian": ["obsidian", "pkb", "obsidian/plugins"],
    "dataview": ["dataview", "dataview-queries", "obsidian/plugins"],
    "template": ["templater", "note-templates", "automation"],
    "linking": ["linking-strategy", "bidirectional-links", "knowledge-graph"],
    
    // Prompt Engineering
    "prompt": ["prompt-engineering", "prompting-technique"],
    "chain": ["chain-of-thought", "prompting-technique/chain-of-thought"],
    "llm": ["llm-architecture", "artificial-intelligence"],
    "claude": ["model/claude", "llm-architecture"],
    
    // Research & Analysis
    "research": ["research", "empirical-research", "concept/research"],
    "analysis": ["analysis", "critical-thinking/analysis"],
    "experiment": ["experimental-design", "empirical-research"]
};
// Suggest tags based on title keywords
let suggestedTags = [];
for (const [keyword, tags] of Object.entries(keywordTagMap)) {
    if (titleLower.includes(keyword)) {
        suggestedTags.push(…tags);
    }
}
// Remove duplicates
suggestedTags = […new Set(suggestedTags)];
// ─────────────────────────────────────────────────────────────────────
// PRESENT SUGGESTIONS TO USER
// ─────────────────────────────────────────────────────────────────────
let selectedTags = [];
if (suggestedTags.length > 0) {
    const useSuggestions = await tp.system.prompt(
        `Found ${suggestedTags.length} suggested tags based on title. View suggestions? (y/n):`
    );
    
    if (useSuggestions && useSuggestions.toLowerCase() === "y") {
        // Multi-select suggested tags
        for (const tag of suggestedTags) {
            const include = await tp.system.prompt(
                `Include tag "${tag}"? (y/n):`
            );
            if (include && include.toLowerCase() === "y") {
                selectedTags.push(tag);
            }
        }
    }
}
// ─────────────────────────────────────────────────────────────────────
// COMBINE WITH MANUAL TAG SELECTION
// ─────────────────────────────────────────────────────────────────────
// Then proceed with your normal tag selection from master template
// The selectedTags array now contains pre-selected tags based on title
// Example: Add suggested tags to frontmatter
// (This would be combined with your existing tag selection logic)
_%>
````

---

## Component 5.4: Progress Percentage Calculator

````javascript
<%*
/* ═════════════════════════════════════════════════════════════════════
   PROJECT PROGRESS CALCULATOR
   Calculates progress percentage based on completed tasks
   ═════════════════════════════════════════════════════════════════════ */
// ─────────────────────────────────────────────────────────────────────
// FUNCTION: Calculate Progress
// ─────────────────────────────────────────────────────────────────────
async function calculateProgress() {
    const content = await tp.file.content;
    
    // Count total tasks
    const totalTasks = (content.match(/- \[ \]/g) || []).length + 
                      (content.match(/- \[x\]/g) || []).length;
    
    // Count completed tasks
    const completedTasks = (content.match(/- \[x\]/g) || []).length;
    
    // Calculate percentage
    const progressPercentage = totalTasks > 0 
        ? Math.round((completedTasks / totalTasks) * 100)
        : 0;
    
    return {
        total: totalTasks,
        completed: completedTasks,
        percentage: progressPercentage
    };
}
// ─────────────────────────────────────────────────────────────────────
// USAGE: Update Progress in Frontmatter
// ─────────────────────────────────────────────────────────────────────
// This would be triggered by a Templater command or button
const progress = await calculateProgress();
// Update frontmatter (would need QuickAdd or Manual Update)
// For button integration, see Meta Bind section
_%>

## 📊 Project Progress

**Total Tasks**: <%= progress.total %>  
**Completed**: <%= progress.completed %>  
**Progress**: <%= progress.percentage %>%

<progress value="<%= progress.percentage %>" max="100"></progress>

### Task Breakdown

#### Completed ✅

```tasks
done
path includes {{query.file.path}}
sort by done
```

#### Pending ⏳

```tasks
not done
path includes {{query.file.path}}
sort by priority
```
````

---

## Component 5.5: Automated Metadata Validation

`````javascript
<%*
/* ═════════════════════════════════════════════════════════════════════
   METADATA VALIDATION SYSTEM
   Ensures all required fields are populated correctly
   ═════════════════════════════════════════════════════════════════════ */
// ─────────────────────────────────────────────────────────────────────
// VALIDATION RULES
// ─────────────────────────────────────────────────────────────────────
const requiredFields = [
    "type",
    "maturity",
    "confidence",
    "created",
    "tags"
];
const validMaturityLevels = ["seedling", "budding", "developing", "evergreen", "archived"];
const validConfidenceLevels = ["speculative", "provisional", "moderate", "high", "established"];
// ─────────────────────────────────────────────────────────────────────
// VALIDATION FUNCTION
// ─────────────────────────────────────────────────────────────────────
async function validateMetadata() {
    const file = tp.file.find_tfile(tp.file.path(true));
    const cache = app.metadataCache.getFileCache(file);
    const frontmatter = cache?.frontmatter || {};
    
    const errors = [];
    const warnings = [];
    
    // Check required fields
    for (const field of requiredFields) {
        if (!frontmatter[field]) {
            errors.push(`❌ Missing required field: ${field}`);
        }
    }
    
    // Validate maturity value
    if (frontmatter.maturity && !validMaturityLevels.includes(frontmatter.maturity)) {
        errors.push(`❌ Invalid maturity value: ${frontmatter.maturity}`);
    }
    
    // Validate confidence value
    if (frontmatter.confidence && !validConfidenceLevels.includes(frontmatter.confidence)) {
        errors.push(`❌ Invalid confidence value: ${frontmatter.confidence}`);
    }
    
    // Check for minimum tag count (your system uses ~8-11 tags)
    if (frontmatter.tags && frontmatter.tags.length < 3) {
        warnings.push(`⚠️ Low tag count: ${frontmatter.tags.length} (recommend 8+)`);
    }
    
    // Check for next-review date
    if (!frontmatter['next-review']) {
        warnings.push(`⚠️ No next-review date set`);
    }
    
    // Check for link-up MOC
    if (!frontmatter['link-up'] || frontmatter['link-up'].length === 0) {
        warnings.push(`⚠️ No link-up MOC assigned`);
    }
    
    // Check date formatting
    if (frontmatter.created && !/^\d{4}-\d{2}-\d{2}/.test(frontmatter.created)) {
        errors.push(`❌ Invalid created date format: ${frontmatter.created}`);
    }
    
    return {
        errors,
        warnings,
        isValid: errors.length === 0
    };
}
// ─────────────────────────────────────────────────────────────────────
// DISPLAY VALIDATION RESULTS
// ─────────────────────────────────────────────────────────────────────
const validation = await validateMetadata();
if (!validation.isValid || validation.warnings.length > 0) {
_%>

> [!warning] Metadata Validation Report
> 
> **Status**: <%= validation.isValid ? "✅ Valid (with warnings)" : "❌ Invalid" %>
> 
<%_ if (validation.errors.length > 0) { _%>
> **Errors**:
<%_   for (const error of validation.errors) { _%>
> - <%= error %>
<%_   } _%>
<%_ } _%>
> 
<%_ if (validation.warnings.length > 0) { _%>
> **Warnings**:
<%_   for (const warning of validation.warnings) { _%>
> - <%= warning %>
<%_   } _%>
<%_ } _%>

<%_ } _%>
`````

---

## Component 5.6: Smart Review Scheduler

````javascript
<%*
/* ═════════════════════════════════════════════════════════════════════
   SMART REVIEW SCHEDULER
   Calculates optimal next review date based on multiple factors
   ═════════════════════════════════════════════════════════════════════ */
// ─────────────────────────────────────────────────────────────────────
// CONFIGURATION
// ─────────────────────────────────────────────────────────────────────
const reviewIntervals = {
    // Base intervals by maturity (in days)
    maturity: {
        "seedling": 7,
        "budding": 14,
        "developing": 30,
        "evergreen": 90
    },
    
    // Confidence modifiers (multiply base interval)
    confidence: {
        "speculative": 0.7,    // Review more frequently
        "provisional": 0.85,
        "moderate": 1.0,
        "high": 1.2,
        "established": 1.5     // Review less frequently
    },
    
    // Type modifiers
    type: {
        "fleeting": 0.5,       // Review very frequently
        "literature": 1.0,
        "permanent-note": 1.0,
        "reference": 1.3,
        "moc": 1.5,
        "report": 1.2
    }
};
// ─────────────────────────────────────────────────────────────────────
// CALCULATION FUNCTION
// ─────────────────────────────────────────────────────────────────────
function calculateNextReview(maturity, confidence, type, reviewCount = 0) {
    // Get base interval
    let interval = reviewIntervals.maturity[maturity] || 7;
    
    // Apply confidence modifier
    const confMod = reviewIntervals.confidence[confidence] || 1.0;
    interval *= confMod;
    
    // Apply type modifier
    const typeMod = reviewIntervals.type[type] || 1.0;
    interval *= typeMod;
    
    // Apply spacing effect (increase interval with review count)
    // Each review extends the interval by 10%
    if (reviewCount > 0) {
        interval *= (1 + (reviewCount * 0.1));
    }
    
    // Round to nearest day
    interval = Math.round(interval);
    
    // Calculate next review date
    return moment().add(interval, 'days').format("YYYY-MM-DD");
}
// ─────────────────────────────────────────────────────────────────────
// USAGE EXAMPLE
// ─────────────────────────────────────────────────────────────────────
const maturity = tp.file.cursor(1);  // Get from frontmatter or suggester
const confidence = tp.file.cursor(2);
const type = tp.file.cursor(3);
const reviewCount = 0;  // From frontmatter
const nextReview = calculateNextReview(maturity, confidence, type, reviewCount);
_%>
next-review: "<%= nextReview %>"
````

---

# 6️⃣ ADVANCED ANALYTICS COMPONENTS

## Component 6.1: Progress Bar Generator (DataviewJS)

````markdown
## 📊 Visual Progress Tracking

```dataviewjs
// Maturity Progress Bars for All Notes

const pages = dv.pages().where(p => p.maturity);

// Group by maturity level
const grouped = pages.groupBy(p => p.maturity);

// Maturity levels in order
const maturityOrder = ["seedling", "budding", "developing", "evergreen"];
const maturityIcons = {
    "seedling": "🌱",
    "budding": "🌿",
    "developing": "🌳",
    "evergreen": "🌲"
};

// Calculate totals
const totalNotes = pages.length;

dv.header(3, "Maturity Distribution");
dv.paragraph(`Total Notes: ${totalNotes}`);

// Display progress bar for each maturity level
for (const level of maturityOrder) {
    const count = pages.where(p => p.maturity === level).length;
    const percentage = Math.round((count / totalNotes) * 100);
    const icon = maturityIcons[level] || "📄";
    
    const barWidth = Math.floor(percentage / 2); // Scale to 50 chars max
    const bar = "█".repeat(barWidth) + "░".repeat(50 - barWidth);
    
    dv.paragraph(`${icon} **${level}**: ${count} notes (${percentage}%)`);
    dv.paragraph(`\`${bar}\``);
}
```
````

---

## Component 6.2: Network Analysis (DataviewJS)

````markdown
## 🕸️ Knowledge Graph Network Analysis

```dataviewjs
// Calculate Network Metrics

const pages = dv.pages();

// Calculate connectivity metrics
const metrics = pages.map(p => {
    const inlinks = p.file.inlinks.length;
    const outlinks = p.file.outlinks.length;
    const total = inlinks + outlinks;
    
    return {
        file: p.file.link,
        maturity: p.maturity,
        inlinks: inlinks,
        outlinks: outlinks,
        total: total,
        ratio: outlinks > 0 ? (inlinks / outlinks).toFixed(2) : 0
    };
}).sort(p => p.total, 'desc');

// Calculate average connectivity
const avgInlinks = metrics.array().reduce((sum, p) => sum + p.inlinks, 0) / metrics.length;
const avgOutlinks = metrics.array().reduce((sum, p) => sum + p.outlinks, 0) / metrics.length;
const avgTotal = metrics.array().reduce((sum, p) => sum + p.total, 0) / metrics.length;

dv.header(3, "Network Statistics");
dv.paragraph(`**Average Backlinks**: ${avgInlinks.toFixed(1)}`);
dv.paragraph(`**Average Outlinks**: ${avgOutlinks.toFixed(1)}`);
dv.paragraph(`**Average Total Connections**: ${avgTotal.toFixed(1)}`);

dv.header(3, "Most Connected Notes (Top 20)");
dv.table(
    ["Note", "Maturity", "⬅️ In", "➡️ Out", "Total", "Ratio"],
    metrics.array().slice(0, 20).map(p => [
        p.file,
        p.maturity,
        p.inlinks,
        p.outlinks,
        p.total,
        p.ratio
    ])
);

// Identify orphans and hubs
const orphans = metrics.where(p => p.inlinks === 0).length;
const hubs = metrics.where(p => p.total > 10).length;

dv.paragraph(`\n**Orphan Notes**: ${orphans}`);
dv.paragraph(`**Hub Notes** (10+ connections): ${hubs}`);
```

````

---

## Component 6.3: Review Heatmap (DataviewJS)

````markdown
## 📅 Review Activity Heatmap

```dataviewjs
// Generate review activity heatmap for past 12 weeks

const weeks = 12;
const today = moment();
const startDate = moment().subtract(weeks, 'weeks');

// Get all notes with review activity
const pages = dv.pages().where(p => p.modified);

// Create week buckets
const weekBuckets = {};
for (let i = 0; i < weeks; i++) {
    const weekStart = moment().subtract(i, 'weeks').startOf('week');
    const weekKey = weekStart.format("YYYY-[W]WW");
    weekBuckets[weekKey] = 0;
}

// Count reviews per week
for (const page of pages) {
    const modifiedDate = moment(page.modified);
    if (modifiedDate.isAfter(startDate)) {
        const weekKey = modifiedDate.startOf('week').format("YYYY-[W]WW");
        if (weekBuckets[weekKey] !== undefined) {
            weekBuckets[weekKey]++;
        }
    }
}

// Find max for scaling
const maxReviews = Math.max(…Object.values(weekBuckets));

// Display heatmap
dv.header(3, "Review Activity (Past 12 Weeks)");

const rows = [];
for (const [week, count] of Object.entries(weekBuckets).reverse()) {
    const percentage = maxReviews > 0 ? Math.round((count / maxReviews) * 100) : 0;
    const intensity = percentage > 75 ? "🟥" : percentage > 50 ? "🟧" : percentage > 25 ? "🟨" : "⬜";
    const bar = "█".repeat(Math.floor(count / 2));
    
    rows.push([week, intensity, count, bar]);
}

dv.table(
    ["Week", "Heat", "Reviews", "Activity"],
    rows
);
```

````

---

## Component 6.4: Tag Cloud Generator (DataviewJS)

````markdown
## 🏷️ Tag Frequency Analysis

```dataviewjs
// Generate tag frequency distribution

const pages = dv.pages();

// Count tag occurrences
const tagCounts = {};

for (const page of pages) {
    if (page.tags) {
        for (const tag of page.tags) {
            const tagStr = String(tag);
            tagCounts[tagStr] = (tagCounts[tagStr] || 0) + 1;
        }
    }
}

// Sort by frequency
const sortedTags = Object.entries(tagCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 50); // Top 50 tags

dv.header(3, "Top 50 Most Used Tags");

// Display as table with frequency bars
const rows = sortedTags.map(([tag, count]) => {
    const percentage = Math.round((count / pages.length) * 100);
    const bar = "█".repeat(Math.floor(percentage / 2));
    
    return [
        tag,
        count,
        `${percentage}%`,
        bar
    ];
});

dv.table(
    ["Tag", "Count", "% of Notes", "Distribution"],
    rows
);

// Tag Category Breakdown
dv.header(3, "Tag Category Distribution");

const categories = {
    "Type": sortedTags.filter(([tag]) => tag.startsWith("type/")),
    "Status": sortedTags.filter(([tag]) => tag.startsWith("status/")),
    "Domain": sortedTags.filter(([tag]) => !tag.includes("/")),
    "Sub-Domain": sortedTags.filter(([tag]) => tag.includes("/") && !tag.startsWith("type/") && !tag.startsWith("status/"))
};

for (const [category, tags] of Object.entries(categories)) {
    const totalCount = tags.reduce((sum, [, count]) => sum + count, 0);
    dv.paragraph(`**${category}**: ${tags.length} unique tags, ${totalCount} total occurrences`);
}
```

````

---

## Component 6.5: Staleness Report (DataviewJS)

````markdown
## 🕸️ Staleness & Maintenance Report

```dataviewjs
// Identify notes needing attention based on staleness

const pages = dv.pages().where(p => p.type !== "moc");
const today = moment();

// Categorize by staleness
const categories = {
    "🔥 Fresh (< 7 days)": [],
    "✅ Active (7-30 days)": [],
    "🕐 Aging (30-90 days)": [],
    "🕸️ Stale (90-180 days)": [],
    "🧟 Zombie (180+ days)": []
};

for (const page of pages) {
    const modified = moment(page.modified);
    const daysSince = today.diff(modified, 'days');
    
    const item = {
        file: page.file.link,
        type: page.type,
        maturity: page.maturity,
        days: daysSince,
        inlinks: page.file.inlinks.length
    };
    
    if (daysSince < 7) {
        categories["🔥 Fresh (< 7 days)"].push(item);
    } else if (daysSince < 30) {
        categories["✅ Active (7-30 days)"].push(item);
    } else if (daysSince < 90) {
        categories["🕐 Aging (30-90 days)"].push(item);
    } else if (daysSince < 180) {
        categories["🕸️ Stale (90-180 days)"].push(item);
    } else {
        categories["🧟 Zombie (180+ days)"].push(item);
    }
}

// Display summary
dv.header(3, "Staleness Distribution");

for (const [category, items] of Object.entries(categories)) {
    const count = items.length;
    const percentage = Math.round((count / pages.length) * 100);
    dv.paragraph(`${category}: **${count}** notes (${percentage}%)`);
}

// Show most concerning stale notes
dv.header(3, "Most Concerning Stale Notes");
dv.paragraph("*Notes untouched for 90+ days with high connectivity (valuable but neglected)*");

const concerningStale = pages
    .where(p => today.diff(moment(p.modified), 'days') > 90)
    .where(p => p.file.inlinks.length > 5)
    .sort(p => today.diff(moment(p.modified), 'days'), 'desc')
    .slice(0, 20);

dv.table(
    ["Note", "Type", "Maturity", "Days Stale", "Backlinks"],
    concerningStale.map(p => [
        p.file.link,
        p.type,
        p.maturity,
        today.diff(moment(p.modified), 'days'),
        p.file.inlinks.length
    ])
);
```

````

---

## Component 6.6: Domain Activity Dashboard (DataviewJS)

````markdown
## 🧠 Domain-Specific Activity Tracking

```dataviewjs
// Track activity across your 4 primary domains

const domains = {
    "🧠 Cognitive Science": dv.pages("#cognitive-science OR #neuroscience OR #cognitive-psychology"),
    "💬 Prompt Engineering": dv.pages("#prompt-engineering OR #artificial-intelligence"),
    "💎 PKB/PKM": dv.pages("#pkb OR #pkm OR #obsidian"),
    "🌌 Cosmology": dv.pages("#cosmology")
};

const today = moment();

dv.header(3, "Domain Activity Summary (Past 30 Days)");

const summaryData = [];

for (const [domain, pages] of Object.entries(domains)) {
    const total = pages.length;
    const created = pages.where(p => today.diff(moment(p.created), 'days') <= 30).length;
    const modified = pages.where(p => today.diff(moment(p.modified), 'days') <= 30).length;
    const evergreen = pages.where(p => p.maturity === "evergreen").length;
    const avgReviews = pages.array().reduce((sum, p) => sum + (p['review-count'] || 0), 0) / total;
    
    summaryData.push([
        domain,
        total,
        created,
        modified,
        evergreen,
        avgReviews.toFixed(1)
    ]);
}

dv.table(
    ["Domain", "Total Notes", "Created (30d)", "Modified (30d)", "Evergreen", "Avg Reviews"],
    summaryData
);

// Show most active domain
const mostActive = summaryData.reduce((max, current) => 
    current[3] > max[3] ? current : max
);

dv.paragraph(`\n**Most Active Domain**: ${mostActive[0]} (${mostActive[3]} notes modified in past 30 days)`);

// Recent notes per domain
dv.header(3, "Recent Activity by Domain");

for (const [domain, pages] of Object.entries(domains)) {
    dv.header(4, domain);
    
    const recentNotes = pages
        .sort(p => p.file.mtime, 'desc')
        .slice(0, 5);
    
    dv.table(
        ["Note", "Maturity", "Modified"],
        recentNotes.map(p => [
            p.file.link,
            p.maturity,
            moment(p.modified).fromNow()
        ])
    );
}
```

````

---

# 📦 IMPLEMENTATION GUIDE

## Installation & Setup

### Step 1: Install Required Plugins

Ensure these plugins are installed and enabled:
- ✅ Dataview
- ✅ Templater
- ✅ Meta Bind
- ✅ Tasks (optional, for task tracking)
- ✅ Charts (optional, for visualizations)

### Step 2: Configure Meta Bind Button Templates

1. Open Settings → Meta Bind → Button Templates
2. Copy all button template YAML from Component 4 sections
3. Paste each template into Meta Bind configuration
4. Save settings

### Step 3: Create Dashboard Template

1. Create new note: `Research Project Hub Template.md`
2. Copy desired sections from Components 1-6
3. Arrange sections in preferred order
4. Add your master template Templater logic at top

### Step 4: Initialize Your First Project

1. Create new note
2. Trigger Templater (Ctrl/Cmd + P → "Templater: Create new note from template")
3. Select your new Research Project Hub template
4. Fill in prompted information
5. Watch as your dashboard populates automatically

---

## Component Selection Guide

**For a Minimal Dashboard** (Lightweight):
- Component 1.1: Project Health Monitor
- Component 2.1: Active Projects Master List
- Component 3.1: Metadata Display Inline Queries
- Component 4.3: Smart Review Completion Button

**For a Full-Featured Hub** (Comprehensive):
- All Component 1 sections (Overview)
- Components 2.1-2.4 (Block queries)
- Components 3.1-3.6 (Inline queries)
- Components 4.1-4.6 (Meta Bind buttons)
- Components 6.1-6.6 (Analytics)

**For Domain-Specific Work**:
- Component 1.2: Domain-Specific Focus Areas
- Component 2.2: Domain-Filtered Research Notes
- Component 5.2: Domain-Specific Conditional Templates
- Component 6.6: Domain Activity Dashboard

**For Review-Focused**:
- Component 1.3: Review Queue Management
- Component 2.3: Maturity-Based Review Queues
- Component 4.3: Smart Review Completion Button
- Component 6.3: Review Heatmap

---

## Customization Tips

### Adjust Query Limits

All `LIMIT` values in Dataview queries can be adjusted:
```
LIMIT 20  ← Change to your preferred number
```

### Modify Review Intervals

In Templater Component 5.6, adjust these values:
```
const reviewIntervals = {
    maturity: {
        "seedling": 7,    ← Change to preferred days
        "budding": 14,    ← Change to preferred days
        // etc.
    }
}
```

### Change Progress Bar Colors

In DataviewJS Component 6.3, modify intensity thresholds:
```
const intensity = percentage > 75 ? "🟥" : 
                  percentage > 50 ? "🟧" : 
                  percentage > 25 ? "🟨" : "⬜";
```

---

## Troubleshooting

### Dataview Queries Not Working

**Issue**: Query shows no results  
**Fix**: Check that your frontmatter fields match exactly (case-sensitive):
- `maturity` not `Maturity`
- `next-review` not `next_review`

### Meta Bind Buttons Not Updating

**Issue**: Button click does nothing  
**Fix**: 
1. Verify button template is saved in Meta Bind settings
2. Check that `bindTarget` field name matches your frontmatter exactly
3. Enable Meta Bind button debugging in settings

### Templater Variables Not Populating

**Issue**: `<% variable %>` shows in output instead of value  
**Fix**:
1. Ensure Templater plugin is enabled
2. Check that file has `.md` extension
3. Verify template syntax (backticks for JavaScript blocks)

### Progress Bars Not Displaying

**Issue**: HTML progress tag shows as text  
**Fix**: Ensure you're in Reading View (not Editing View) when viewing progress bars

---

## Performance Optimization

For large vaults (1000+ notes):

1. **Limit Query Scope**:
   ```
   FROM "02_projects"  ← Limit to specific folder
   WHERE type = "report"
   LIMIT 20
   ```

2. **Use Inline Queries Sparingly**: Too many inline queries on one page can slow rendering

3. **Cache DataviewJS Results**: For complex calculations, consider caching results in frontmatter

4. **Reduce Review Queue Size**: Focus on notes actually needing attention:
   ```
   WHERE date(next-review) <= date(today) + dur(3 days)
   ```

---

**This complete component library gives you everything needed to build a world-class Research/Project Hub tailored to your exact PKB architecture.** Mix and match components, customize to your workflow, and enjoy a self-documenting, self-organizing system that scales with your knowledge base! 🚀

