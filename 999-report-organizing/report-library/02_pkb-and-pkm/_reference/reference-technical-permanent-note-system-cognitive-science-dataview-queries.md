
# Dataview Query Library for Cognitive Science Permanent Notes

---

aliases: [Permanent Note Queries, Concept Dashboard Queries]
---

> [!abstract] Overview
> This library contains 15+ production-ready Dataview queries optimized for cognitive science permanent notes. Each query includes purpose, implementation, and customization options.

## 📑 Table of Contents

1. [[#Development Status Dashboard]]
2. [[#Review System Queries]]
3. [[#Knowledge Graph Analytics]]
4. [[#Temporal Views]]
5. [[#Source & Citation Tracking]]
6. [[#Confidence & Epistemic Status]]
7. [[#Tag-Based Discovery]]
8. [[#Cross-Reference Analysis]]

---

## 1️⃣ Development Status Dashboard

### 1.1 Maturity Overview

```
TABLE WITHOUT ID
    key AS "Maturity Level",
    length(rows) AS "Count",
    round(length(rows) / length(this.file.path) * 100, 1) + "%" AS "Percentage"
FROM "03_notes/01_permanent-notes"
WHERE type = "permanent-note" OR type = "concept"
GROUP BY maturity
SORT length(rows) DESC
```

**Purpose**: Shows distribution of notes across maturity levels  
**Customization**: Change folder path to match your structure

---

### 1.2 Notes by Maturity Level (Detailed)

```
TABLE 
    maturity AS "🌱 Status",
    confidence AS "Confidence",
    review-count AS "Reviews",
    dateformat(date(next-review), "MMM dd") AS "Next Review"
FROM "03_notes/01_permanent-notes"
WHERE type = "permanent-note" OR type = "concept"
SORT maturity ASC, confidence DESC
```

**Purpose**: Detailed view of all permanent notes with development tracking  
**Use Case**: Daily review planning

---

### 1.3 Seedlings Needing Attention

```
LIST 
    "Created: " + dateformat(date(created), "MMM dd, yyyy") + " | Reviews: " + review-count
FROM "03_notes/01_permanent-notes"
WHERE maturity = "seedling" 
      AND date(created) < date(today) - dur(14 days)
SORT created ASC
```

**Purpose**: Identify old seedlings that should be developed  
**Threshold**: Notes older than 14 days still in seedling stage

---

## 2️⃣ Review System Queries

### 2.1 Due for Review Today

```
TASK
WHERE !completed 
      AND contains(text, "Review")
      AND typeof(next-review) = "date"
      AND next-review <= date(today)
```

**Purpose**: Shows review tasks due today  
**Integration**: Works with Tasks plugin if review tasks created

---

### 2.2 Review Calendar (Next 30 Days)

```
TABLE 
    maturity AS "Status",
    confidence AS "Confidence",
    review-count AS "Reviews",
    dateformat(date(next-review), "MMM dd") AS "Due"
FROM "03_notes/01_permanent-notes"
WHERE typeof(next-review) = "date"
      AND next-review >= date(today)
      AND next-review <= date(today) + dur(30 days)
SORT next-review ASC
```

**Purpose**: 30-day review roadmap  
**Customization**: Adjust duration (e.g., `dur(60 days)` for 2 months)

---

### 2.3 Overdue Reviews

```
TABLE 
    maturity,
    dateformat(date(next-review), "MMM dd, yyyy") AS "Was Due",
    date(today) - date(next-review) AS "Days Overdue",
    review-count AS "Total Reviews"
FROM "03_notes/01_permanent-notes"
WHERE typeof(next-review) = "date"
      AND next-review < date(today)
SORT next-review ASC
```

**Purpose**: Identify neglected notes  
**Action Trigger**: Consider updating maturity level if consistently overdue

---

## 3️⃣ Knowledge Graph Analytics

### 3.1 Most Connected Notes (Hub Analysis)

```
TABLE 
    length(file.inlinks) AS "⬅️ Backlinks",
    length(file.outlinks) AS "➡️ Outlinks",
    length(file.inlinks) + length(file.outlinks) AS "Total Connections",
    maturity AS "Status"
FROM "03_notes/01_permanent-notes"
WHERE type = "permanent-note" OR type = "concept"
SORT (length(file.inlinks) + length(file.outlinks)) DESC
LIMIT 20
```

**Purpose**: Identify knowledge graph hubs  
**Insight**: High-connection notes are often core concepts

---

### 3.2 Isolated Notes (Orphans)

```
LIST 
    "Created: " + dateformat(date(created), "MMM dd") + " | Maturity: " + maturity
FROM "03_notes/01_permanent-notes"
WHERE (length(file.inlinks) = 0 OR length(file.outlinks) = 0)
      AND type = "permanent-note"
SORT created DESC
```

**Purpose**: Find disconnected notes needing integration  
**Action**: Create connections to related concepts

---

### 3.3 Backlink Network for Current Note

```dataview
TABLE 
    type AS "Type",
    maturity AS "Maturity",
    length(file.inlinks) AS "Its Backlinks",
    dateformat(date(created), "MMM dd, yyyy") AS "Created"
FROM [[#]]
WHERE file.name != this.file.name
SORT length(file.inlinks) DESC
LIMIT 20
```

**Purpose**: Shows what notes link TO the current note  
**Usage**: Embed in note template or MOC

---

### 3.4 Forward Link Network for Current Note

```
TABLE 
    type AS "Type",
    maturity AS "Maturity",
    confidence AS "Confidence"
FROM outgoing([[]])
WHERE type = "permanent-note" OR type = "concept"
SORT maturity DESC, confidence DESC
```

**Purpose**: Shows notes the current note links TO  
**Context**: Understand conceptual dependencies

---

## 4️⃣ Temporal Views

### 4.1 Recently Created Concepts (Last 30 Days)

```
TABLE 
    maturity AS "Status",
    confidence AS "Confidence",
    dateformat(date(created), "MMM dd") AS "Created",
    length(file.inlinks) AS "Backlinks"
FROM "03_notes/01_permanent-notes"
WHERE date(created) >= date(today) - dur(30 days)
      AND (type = "permanent-note" OR type = "concept")
SORT created DESC
```

**Purpose**: Track recent knowledge capture velocity  
**Metric**: High creation rate may indicate active learning period

---

### 4.2 Recently Modified Notes (Active Development)

```
TABLE 
    maturity AS "Status",
    dateformat(date(modified), "MMM dd HH:mm") AS "Last Edit",
    review-count AS "Reviews"
FROM "03_notes/01_permanent-notes"
WHERE date(modified) >= date(today) - dur(7 days)
      AND type = "permanent-note"
SORT modified DESC
LIMIT 15
```

**Purpose**: See what concepts you're actively refining  
**Insight**: Clusters of edits indicate focused study areas

---

### 4.3 Creation Timeline (This Year)

```
TABLE WITHOUT ID
    file.cday.month AS "Month",
    length(rows) AS "Notes Created"
FROM "03_notes/01_permanent-notes"
WHERE date(created).year = date(today).year
      AND type = "permanent-note"
GROUP BY file.cday.month
SORT file.cday.month ASC
```

**Purpose**: Visualize knowledge creation patterns  
**Analysis**: Identify productive vs. idle periods

---

## 5️⃣ Source & Citation Tracking

### 5.1 Notes by Source Type

```
TABLE WITHOUT ID
    source AS "Source",
    length(rows) AS "Count",
    rows.file.link AS "Notes"
FROM "03_notes/01_permanent-notes"
WHERE source AND type = "permanent-note"
GROUP BY source
SORT length(rows) DESC
```

**Purpose**: Understand where knowledge originates  
**Insight**: Over-reliance on single source type?

---

### 5.2 AI-Generated Concepts (Synthesis Review)

```
TABLE 
    source AS "AI Model",
    maturity AS "Maturity",
    confidence AS "Confidence",
    review-count AS "Human Reviews"
FROM "03_notes/01_permanent-notes"
WHERE contains(source, "claude") 
      OR contains(source, "gemini")
      OR contains(source, "gpt")
SORT confidence ASC, review-count ASC
```

**Purpose**: Track AI-assisted concept development  
**Quality Control**: Low confidence AI notes need human verification

---

### 5.3 Literature-Based Notes Needing Citations

```
TASK
WHERE !completed
      AND contains(text, "citation")
      OR contains(text, "source")
      OR contains(text, "reference")
FROM "03_notes/01_permanent-notes"
WHERE source = "book" OR source = "article" OR source = "paper"
```

**Purpose**: Find incomplete bibliographic work  
**Integration**: Works with Tasks plugin for citation todos

---

## 6️⃣ Confidence & Epistemic Status

### 6.1 Low Confidence Notes Needing Validation

```
TABLE 
    confidence AS "Confidence",
    source AS "Origin",
    review-count AS "Reviews",
    dateformat(date(created), "MMM dd") AS "Created"
FROM "03_notes/01_permanent-notes"
WHERE confidence = "speculative" OR confidence = "provisional"
      AND type = "permanent-note"
SORT review-count ASC, created ASC
```

**Purpose**: Prioritize notes needing evidence gathering  
**Action**: Research, verify claims, update confidence level

---

### 6.2 Confidence Distribution

```
TABLE WITHOUT ID
    confidence AS "Level",
    length(rows) AS "Count",
    round(length(rows) / 50 * 100, 1) + "%" AS "Percentage"
FROM "03_notes/01_permanent-notes"
WHERE confidence AND type = "permanent-note"
GROUP BY confidence
SORT 
    choice(confidence = "established", 1,
    choice(confidence = "high", 2,
    choice(confidence = "moderate", 3,
    choice(confidence = "provisional", 4, 5)))) ASC
```

**Purpose**: Assess overall epistemic health of PKB  
**Goal**: Shift distribution toward "high" and "established"

---

## 7️⃣ Tag-Based Discovery

### 7.1 Notes by Primary Domain (Tag Analysis)

```
TABLE WITHOUT ID
    tag AS "Domain",
    length(rows) AS "Notes",
    rows.file.link AS "Concepts"
FROM "03_notes/01_permanent-notes"
WHERE type = "permanent-note"
FLATTEN file.tags AS tag
WHERE startswith(tag, "#cognitive-science") 
      OR startswith(tag, "#learning-theory")
      OR startswith(tag, "#self-regulation")
GROUP BY tag
SORT length(rows) DESC
LIMIT 15
```

**Purpose**: Identify knowledge concentration areas  
**Customization**: Adjust tag prefixes to your taxonomy

---

### 7.2 Cross-Domain Concepts (Multi-Tag)

```
LIST 
    "Tags: " + join(file.tags, ", ")
FROM "03_notes/01_permanent-notes"
WHERE length(file.tags) >= 5
      AND type = "permanent-note"
SORT length(file.tags) DESC
LIMIT 20
```

**Purpose**: Find concepts spanning multiple domains  
**Insight**: High tag count indicates integrative thinking

---

## 8️⃣ Cross-Reference Analysis

### 8.1 Link-Up MOC Coverage

```
TABLE 
    link-up AS "MOC Assignment",
    maturity AS "Status",
    length(file.inlinks) AS "Backlinks"
FROM "03_notes/01_permanent-notes"
WHERE link-up
      AND type = "permanent-note"
SORT link-up ASC, maturity DESC
```

**Purpose**: Ensure notes properly connected to MOCs  
**Action**: Identify notes needing MOC assignment

---

### 8.2 Notes Without MOC Assignment

```
LIST 
    "Maturity: " + maturity + " | Created: " + dateformat(date(created), "MMM dd")
FROM "03_notes/01_permanent-notes"
WHERE !link-up OR length(link-up) = 0
      AND type = "permanent-note"
SORT created DESC
```

**Purpose**: Find notes missing structural integration  
**Action**: Assign to appropriate MOC

---

## 🎯 Advanced Composite Queries

### Master Dashboard (All Metrics)

```
TABLE WITHOUT ID
    "📊 **Metric**" AS "Metric",
    "**Count**" AS "Value"
FROM ""
WHERE file.name = this.file.name
FLATTEN [
    "Total Permanent Notes: " + length(filter(app.vault.getMarkdownFiles(), (f) => f.path.contains("permanent-notes"))),
    "Seedlings: " + length(filter(this.file.tasks, (t) => contains(t.text, "seedling"))),
    "Budding: " + length(filter(this.file.tasks, (t) => contains(t.text, "budding"))),
    "Evergreen: " + length(filter(this.file.tasks, (t) => contains(t.text, "evergreen"))),
    "Due for Review: " + length(filter(this.file.tasks, (t) => contains(t.text, "review") AND !t.completed))
] AS metrics
```

**Purpose**: Single-view PKB health check  
**Usage**: Embed in daily note or dedicated dashboard

---

## 🔧 Customization Guide

### Adjusting Folder Paths

All queries use `"03_notes/01_permanent-notes"` as the base path. Replace with your structure:

```
FROM "Your/Folder/Path"
```

### Adding Custom Fields

To track additional metadata, add fields to your template frontmatter:

```yaml
priority: high
domain: cognitive-science
audience: academic
```

Then query with:

```
WHERE priority = "high"
```

### Performance Optimization

For large vaults (>1000 notes), add LIMIT clauses:

```
SORT created DESC
LIMIT 50
```

---

## 📚 Integration Examples

### With Meta Bind Buttons

Create interactive buttons that trigger these queries dynamically:

```meta-bind-button
label: Show Overdue Reviews
action: 
  type: command
  command: : rebuild
```

### With Tasks Plugin

Many queries return TASK results that integrate with Tasks plugin views and filters.

---

## 🎓 Learning Outcomes

After implementing these queries, you'll be able to:

✅ Monitor note development lifecycle systematically  
✅ Identify knowledge gaps and orphaned concepts  
✅ Track epistemic confidence across your PKB  
✅ Optimize review scheduling based on maturity  
✅ Analyze knowledge graph topology  
✅ Discover cross-domain conceptual patterns

---

**Next Steps**: 
1. [[Meta Bind Integration Guide]] - Add interactive elements
2. [[Tasks Plugin Workflows]] - Automate review scheduling
3. [[Custom Dataview Functions]] - Extend query capabilities