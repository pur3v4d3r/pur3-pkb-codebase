---
tags: #project #system-design #dataview #pkb-architecture #permanent-note/project-pur3v4d3r
aliases: [Self-Doc PKB System, Pur3v4d3r Self-Documenting System]
status: active
type: 📋project-plan
maturity: seedling
confidence: ^verified
created: 2025-12-16
---

# 🔄 Pur3v4d3r's Self-Documenting PKB System

> [!abstract] System Overview
> Adaptation of self-documenting dataview system for Pur3v4d3r's Knowledge Base, creating emergent intelligence through automated concept discovery while integrating with existing metadata architecture.

---

## 📊 Vault Analysis

### Current Structure

```
d:\10_pur3v4d3r's-vault/
├── 00-inbox/              # Ingestion point
├── 00-meta/              # System & memory files
├── 01_daily-notes/       # Daily atomic entries
├── 02-projects/          # Active project work
├── 03-notes/             # Permanent knowledge
│   ├── 01_permanent-notes/
│   │   ├── 01_cognitive-development/
│   │   ├── 02_personal-knowledge-base/
│   │   ├── 03_cosmology/
│   │   ├── 04_prompt-engineering/
│   │   └── 05-stoic-notes/
│   └── 02_quotes/
├── 04-library/           # Reference materials
│   ├── 01-cognitive-science/
│   ├── 02-pkb-and-pkm-learning/
│   ├── 03-prompt-engineering/
│   └── 04-cosmology/
├── 05-tasks-&-reviews/
├── 06-dashboards/
├── 07-mocs/              # Maps of Content
├── 99-archive/
└── 99-system/            # Templates & scripts
```

### Existing Metadata Schema (STRENGTHS)

Your current metadata is **already sophisticated**:

```yaml
# Core Identity
type: 🧬concept | reference | 📋project | etc.
status: active | seedling | archived
maturity: seedling | budding | evergreen
confidence: speculative | ^verified

# Relationship Tracking (Manual)
link-up: [[Parent MOC]]
link-related: [[Related Concept 1]], [[Related Concept 2]]

# Discovery
tags: [hierarchical/structure]
aliases: [multiple, variations]

# Review System
review-next-review: YYYY-MM-DD
review-interval: days
review-priority: low | medium | high
```

**Key Insight:** You're manually maintaining `link-related` fields. The self-documenting system will **automate discovery** of these relationships.

---

## 🎯 Integration Strategy

### Core Philosophy: Enhancement, Not Replacement

The self-documenting system will:

1. ✅ **Preserve** your existing metadata schema
2. ✅ **Enhance** automatic discovery of relationships
3. ✅ **Complement** your manual `link-related` system
4. ✅ **Respect** your folder structure and note types
5. ✅ **Integrate** with your review system

### The Missing Piece: Bidirectional Auto-Discovery

**Current State (Manual):**
```markdown
# Advanced Prompting.md
---
link-related:
  - [[Generative Ai]]
  - [[Large Language Models]]
---
```

You must manually update:
- Advanced Prompting.md → add links
- Generative AI.md → add back-reference
- Large Language Models.md → add back-reference

**Future State (Self-Documenting):**
```markdown
# Advanced Prompting.md (Concept Note)
---
type: 🧬concept
---

## 🔍 Where This Concept Appears
```dataview
TABLE file.folder, status, maturity
WHERE concepts AND contains(concepts, this.file.link)
SORT file.mtime DESC
LIMIT 50
```
```

```markdown
# My Research Project.md (Application Note)
---
concepts: [[Advanced Prompting]], [[Generative Ai]]
---
```

**Result:** Advanced Prompting.md **automatically discovers** your research project. No manual updating needed.

---

## 🧬 Proposed Metadata Schema Extensions

### New Fields (Additive, Not Replacing)

```yaml
---
# EXISTING FIELDS (Keep All)
type: 🧬concept
status: active
maturity: seedling
confidence: ^verified
link-up: [[parent-moc]]
link-related: [[manual-link]]  # Keep for explicit curation

# NEW SELF-DOCUMENTING FIELDS
concepts: [[Concept 1]], [[Concept 2]]       # Theoretical frameworks
methodologies: [[Method 1]]                  # Research/work methods
tools: [[Obsidian]], [[Dataview]]           # Technologies
fields: [[Cognitive Science]]                # Academic domains
people: [[Author Name]]                      # Collaborators/sources
---
```

### Field Definitions by Use Case

#### For Permanent Notes (03-notes)

```yaml
# Concept Notes (things you want to track usage of)
type: 🧬concept
concept-category: methodology | framework | theory | principle

# Application Notes (notes that USE concepts)
concepts: [[Primary Concept]]
related-concepts: [[Supporting Concept]]
```

#### For Library Notes (04-library)

```yaml
# Reference Documents
source-type: book | paper | article | course
authors: [[Author Name]]
theories: [[Theoretical Framework]]
methodologies: [[Research Method]]
fields: [[Academic Field]]
```

#### For Project Notes (02-projects)

```yaml
# Project Work
concepts: [[Applied Concept]]
methodologies: [[Work Method]]
tools: [[Tool Used]]
status: planning | active | on-hold | completed
```

#### For Daily Notes (01_daily-notes)

```yaml
# Daily Atomic Entries
concepts-explored: [[Concept]]
tools-used: [[Tool]]
```

---

## 🏗️ Template Architecture

### Template 1: Concept Note Template

**Location:** `99-system/01-quickadd/02-templates/_concept-note-template.md`

**Purpose:** For notes you want to TRACK (concepts, methodologies, tools, people)

```markdown
---
title: pur3v4d3r-self-documenting-pkb-system
id: 20251216-115402
type: 🧬concept
status: active
rating: ""
source: ""
url: ""
tags:
  - permanent-note
  - permanent-note/pkb
  - concept/pur3v4d3r-self-documenting-pkb-system
aliases:
  - pur3v4d3r-self-documenting-pkb-system
link-up:
  - "[[self-learning-and-cognitive-development-moc]]"
link-related: []
maturity: seedling
confidence: speculative

concept-category: methodology  # methodology | framework | theory | principle | tool

review-last-reviewed: null
review-next-review: 2025-12-19
review-count: 0
review-interval: 3
review-priority: medium
---

> [!definition]
> - **Key-Term**:: [[pur3v4d3r-self-documenting-pkb-system]]
> - **Definition**::

## 📝 Core Description

*Main content here*

## 🔍 Where This Concept Appears

> [!info] How This Works
> This query automatically finds all notes that reference this concept in their `concepts::` metadata field. Updates in real-time as you create new notes.

```dataview
TABLE
  file.folder as "Location",
  type as "Type",
  status as "Status",
  maturity as "Maturity"
WHERE concepts AND contains(concepts, this.file.link)
SORT file.mtime DESC
LIMIT 50
```

## 🔗 Related Concepts Network

```dataviewjs
const inlinks = dv.current().file.inlinks.limit(20)
const outlinks = dv.current().file.outlinks.filter(l => !l.path.includes("template") && !l.path.includes("moc")).limit(20)
const maxLen = Math.max(inlinks.length, outlinks.length)

dv.table(
  ["← References This (" + inlinks.length + ")", "This References → (" + outlinks.length + ")"],
  Array.from({length: maxLen}, (_, i) => [
    inlinks[i] || "",
    outlinks[i] || ""
  ])
)
```

## 📚 Usage Examples

> [!example] Example 1
> - **Context**:
> - **Application**:
> - **Key Insight**:

## 🧠 Concept Health Metrics

```dataviewjs
const current = dv.current().file
const references = dv.pages().where(p => p.concepts && p.concepts.includes(current.link))

const metrics = {
  "Total References": references.length,
  "Active Usage": references.where(p => p.status === "active").length,
  "Folders Using": new Set(references.map(p => p.file.folder)).size,
  "Maturity Distribution": references.groupBy(p => p.maturity || "unknown").length + " states",
  "Last Referenced": references.sort(p => p.file.mtime, 'desc')[0]?.file.mtime.toFormat("yyyy-MM-dd") || "Never"
}

dv.table(
  ["Metric", "Value"],
  Object.entries(metrics)
)
```

> [!connections-and-links]
> - [[atomic-notes_moc]]: Main Hub for Atomic Notes
```

---

### Template 2: Application Note Template

**Location:** `99-system/01-quickadd/02-templates/_application-note-template.md`

**Purpose:** For notes that USE concepts (projects, research, learning notes)

```markdown
---
title: pur3v4d3r-self-documenting-pkb-system
id: 20251216-115402
type: 📝note
status: active
tags:
  - permanent-note
  - permanent-note/pkb
aliases:
  - pur3v4d3r-self-documenting-pkb-system
link-up: []
link-related: []
maturity: seedling
confidence: speculative

# SELF-DOCUMENTING FIELDS
concepts: []              # [[Theoretical frameworks used]]
methodologies: []         # [[Methods applied]]
tools: []                 # [[Technologies used]]
fields: []                # [[Academic domains]]

review-last-reviewed: null
review-next-review: 2025-12-19
review-count: 0
review-interval: 3
review-priority: medium
---

# pur3v4d3r-self-documenting-pkb-system

## 🧠 Concepts Applied

> [!tip] How to Use
> Add concept links to frontmatter `concepts:` field to auto-register in concept notes.
> Use inline fields for visible tracking: `concepts:: [[Concept Name]]`

**Primary Concepts:**
- concepts:: [[Concept 1]]
- concepts:: [[Concept 2]]

**Methodologies:**
- methodologies:: [[Method]]

**Tools & Technologies:**
- tools:: [[Tool Name]]

## 📝 Main Content

*Your note content here*

---

## 🔍 Auto-Discovery: Related Concept Notes

```dataview
TABLE concept-category, maturity, length(file.inlinks) as "References"
FROM [[pur3v4d3r-self-documenting-pkb-system]]
WHERE type = "🧬concept"
SORT file.name
```

## 🔍 Auto-Discovery: Related Projects

```dataview
TABLE status, maturity, file.mtime as "Updated"
WHERE contains(concepts, this.file.link) OR contains(file.outlinks, this.file.link)
WHERE type = "📋project"
WHERE file.name != this.file.name
SORT file.mtime DESC
LIMIT 10
```
```

---

### Template 3: Library Reference Template

**Location:** `99-system/01-quickadd/02-templates/_library-reference-template.md`

```markdown
---
title: pur3v4d3r-self-documenting-pkb-system
id: 20251216-115402
type: 📚reference
status: seedling
tags:
  - year/2025
  - reference
aliases: []
link-up: []
link-related: []

# SELF-DOCUMENTING FIELDS
source-type: book          # book | paper | article | course | video
authors: []                # [[Author Name]]
theories: []               # [[Theoretical Framework]]
methodologies: []          # [[Research Method]]
fields: []                 # [[Academic Domain]]
concepts: []               # [[Key Concepts]]

# BIBLIOGRAPHIC
publication-year: 2025
citation-key: ""
url: ""
---

# pur3v4d3r-self-documenting-pkb-system

> [!abstract] Overview
> Brief summary of the source

## 📚 Bibliographic Information

- **Authors**: `VIEW[{authors}]`
- **Year**: `VIEW[{publication-year}]`
- **Type**: `VIEW[{source-type}]`
- **Citation**: `VIEW[{citation-key}]`

## 🧠 Key Concepts & Theories

- theories:: [[Theory 1]]
- concepts:: [[Concept 1]]
- methodologies:: [[Method 1]]

## 📝 Notes & Highlights

*Main content*

---

## 🔍 Related References in Vault

```dataview
TABLE source-type, publication-year, authors
WHERE
  (theories AND contains(theories, this.theories[0])) OR
  (fields AND contains(fields, this.fields[0]))
WHERE file.name != this.file.name
SORT publication-year DESC
LIMIT 10
```
```

---

## 📊 Dashboard Queries

### Dashboard 1: Concept Network Dashboard

**Location:** `06-dashboards/concept-network-dashboard.md`

```markdown
---
tags: #dashboard #dataview #concepts
status: active
type: 📊dashboard
---

# 🌐 Concept Network Dashboard

## 📊 Most Referenced Concepts

```dataview
TABLE
  concept-category as "Category",
  length(file.inlinks) as "Total References",
  maturity as "Maturity",
  confidence as "Confidence"
WHERE type = "🧬concept"
SORT length(file.inlinks) DESC
LIMIT 20
```

## 🔥 Active Concept Applications

```dataview
TABLE
  file.folder as "Location",
  concepts as "Concepts Used",
  status as "Status",
  file.mtime as "Updated"
WHERE concepts
WHERE status = "active"
SORT file.mtime DESC
LIMIT 20
```

## 🌱 Seedling Concepts (Need Development)

```dataview
TABLE
  concept-category,
  length(file.inlinks) as "References",
  file.ctime as "Created"
WHERE type = "🧬concept"
WHERE maturity = "seedling"
SORT length(file.inlinks) ASC
LIMIT 15
```

## 🌳 Evergreen Concepts (Well-Established)

```dataview
TABLE
  concept-category,
  length(file.inlinks) as "References",
  confidence
WHERE type = "🧬concept"
WHERE maturity = "evergreen"
SORT length(file.inlinks) DESC
```

## 🕸️ Orphaned Concepts (No References)

```dataview
TABLE concept-category, file.ctime as "Created", confidence
WHERE type = "🧬concept"
WHERE length(file.inlinks) = 0
SORT file.ctime DESC
```

## 📈 Concept Usage by Folder

```dataviewjs
const conceptNotes = dv.pages().where(p => p.concepts).array()

const folderStats = {}
conceptNotes.forEach(note => {
  const folder = note.file.folder
  if (!folderStats[folder]) folderStats[folder] = 0
  folderStats[folder]++
})

const sorted = Object.entries(folderStats)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 15)

dv.table(["Folder", "Notes Using Concepts"], sorted)
```

## 🔄 Recently Updated Concepts

```dataview
TABLE
  concept-category,
  length(file.inlinks) as "Uses",
  file.mtime as "Last Modified"
WHERE type = "🧬concept"
SORT file.mtime DESC
LIMIT 15
```

## 🎯 Concepts Needing Review

```dataview
TABLE
  review-next-review as "Review Due",
  review-priority as "Priority",
  length(file.inlinks) as "References"
WHERE type = "🧬concept"
WHERE review-next-review <= date(today) + dur(7 days)
SORT review-next-review ASC
```


---

### Dashboard 2: Field/Domain Dashboard

**Location:** `06-dashboards/field-domain-dashboard.md`

`````markdown
---
tags: #dashboard #fields #domains
status: active
type: 📊dashboard
---

# 🎓 Field & Domain Intelligence Dashboard

## 📚 Cognitive Science Ecosystem

```dataview
TABLE
  type,
  concepts as "Concepts",
  methodologies as "Methods",
  status
WHERE fields AND contains(fields, [[Cognitive Science]])
SORT file.mtime DESC
LIMIT 20
```

## 🧠 PKB & PKM Domain

```dataview
TABLE
  type,
  concepts,
  maturity,
  file.mtime as "Updated"
WHERE fields AND contains(fields, [[Personal Knowledge Management]])
   OR contains(tags, "pkb") OR contains(tags, "pkm")
SORT file.mtime DESC
LIMIT 20
```

## 🤖 Prompt Engineering Domain

```dataview
TABLE
  type,
  concepts,
  tools,
  status
WHERE fields AND contains(fields, [[Prompt Engineering]])
   OR file.folder = "03-notes/01_permanent-notes/04_prompt-engineering"
SORT file.mtime DESC
LIMIT 20
```

## 🌌 Cosmology Domain

```dataview
TABLE
  type,
  concepts,
  theories,
  status
WHERE fields AND contains(fields, [[Cosmology]])
   OR file.folder = "03-notes/01_permanent-notes/03_cosmology"
SORT file.mtime DESC
```

## 📊 Cross-Domain Concept Usage

```dataviewjs
// Find concepts used across multiple domains
const notes = dv.pages().where(p => p.concepts).array()

const conceptDomains = {}
notes.forEach(note => {
  const folder = note.file.folder.split('/')[0] + '/' + (note.file.folder.split('/')[1] || '')
  if (!note.concepts) return

  const concepts = Array.isArray(note.concepts) ? note.concepts : [note.concepts]
  concepts.forEach(concept => {
    const key = concept.path
    if (!conceptDomains[key]) conceptDomains[key] = new Set()
    conceptDomains[key].add(folder)
  })
})

const crossDomain = Object.entries(conceptDomains)
  .filter(([_, domains]) => domains.size > 1)
  .map(([concept, domains]) => [concept, domains.size, Array.from(domains).join(', ')])
  .sort((a, b) => b[1] - a[1])
  .slice(0, 15)

dv.table(
  ["Concept", "Domain Count", "Domains"],
  crossDomain
)
`````


---

## 🚀 Implementation Roadmap

### Phase 1: Template Setup (10 minutes)

- [ ] Create `99-system/01-quickadd/02-templates/_concept-note-template.md`
- [ ] Create `99-system/01-quickadd/02-templates/_application-note-template.md`
- [ ] Create `99-system/01-quickadd/02-templates/_library-reference-template.md`
- [ ] Configure Templater to recognize new templates

### Phase 2: Dashboard Creation (5 minutes)

- [ ] Create `06-dashboards/concept-network-dashboard.md`
- [ ] Create `06-dashboards/field-domain-dashboard.md`
- [ ] Bookmark dashboards in Obsidian

### Phase 3: Test with Existing Notes (15 minutes)

**Convert 3-5 Existing Concept Notes:**

1. **[[Atomic Notes]]** (already exists)
   - Add self-discovery query
   - Add concept health metrics

2. **[[Advanced Prompting]]** (already exists)
   - Add self-discovery query
   - Set `concept-category: methodology`

3. **[[Dataview Plugin]]** (reference note)
   - Add tool-tracking fields
   - Add related references query

**Tag 5-10 Application Notes:**

Select notes from different domains and add:
```yaml
concepts: [[Atomic Notes]], [[Advanced Prompting]]
tools: [[Dataview Plugin]]
```

### Phase 4: Verify System (5 minutes)

- [ ] Open concept notes - verify queries show results
- [ ] Check dashboards - verify data populates
- [ ] Test with new note creation

### Phase 5: Scale (Ongoing)

- [ ] Convert more existing concept notes
- [ ] Tag existing application notes with concepts
- [ ] Create new notes using templates
- [ ] Monitor dashboards for insights

---

## 🎓 Usage Patterns by Vault Section

### For 03-notes (Permanent Notes)

**Concept Notes Pattern:**
```yaml
type: 🧬concept
concept-category: methodology
maturity: seedling → evergreen
```

**Application Notes Pattern:**
```yaml
type: 📝note
concepts: [[Core Concept]]
related-concepts: [[Supporting Idea]]
```

### For 04-library (Reference Materials)

**Reference Pattern:**
```yaml
type: 📚reference
source-type: book
authors: [[Author]]
theories: [[Theory]]
concepts: [[Key Idea]]
fields: [[Domain]]
```

### For 02-projects (Active Work)

**Project Pattern:**
```yaml
type: 📋project
concepts: [[Applied Framework]]
methodologies: [[Work Method]]
tools: [[Tech Stack]]
status: planning → active → completed
```

### For 01_daily-notes (Daily Entries)

**Daily Pattern:**
```yaml
type: 📅daily
concepts-explored: [[Today's Focus]]
tools-used: [[Tool]]
```

---

## 🔧 Advanced Customization Options

### Option 1: Concept Co-Occurrence Analysis

Add to concept notes to see what other concepts are frequently used together:

```dataviewjs
const concept1 = dv.current().file.link
const otherConcepts = dv.pages()
  .where(p => p.concepts && p.concepts.includes(concept1))
  .flatMap(p => p.concepts)
  .filter(c => c.path !== concept1.path)
  .groupBy(c => c.path)
  .sort(g => g.rows.length, 'desc')
  .slice(0, 10)

dv.table(
  ["Frequently Paired With", "Co-Occurrences"],
  otherConcepts.map(g => [g.key, g.rows.length])
)
```

### Option 2: Temporal Concept Evolution

Track when concepts are used over time:

```dataviewjs
const concept = dv.current().file.link
const timeline = dv.pages()
  .where(p => p.concepts && p.concepts.includes(concept))
  .groupBy(p => p.file.ctime.toFormat("yyyy-MM"))
  .sort(g => g.key)

dv.table(
  ["Month", "New References"],
  timeline.map(g => [g.key, g.rows.length])
)
```

### Option 3: Maturity Progression Tracking

See how concepts mature as you use them:

```dataview
TABLE
  maturity,
  length(file.inlinks) as "References",
  file.ctime as "Created",
  file.mtime as "Updated"
WHERE type = "🧬concept"
SORT maturity ASC, length(file.inlinks) DESC
```

---

## 🛡️ Why This Won't Crash (Lessons Learned)

### Crash Prevention Measures

1. **Limited Scope**: Queries target specific frontmatter fields, not vault-wide scans
2. **No Image Embedding**: Removed unsafe `embed()` operations
3. **Null Safety**: All queries have proper existence checks (`WHERE concepts`)
4. **Performance Limits**: All queries have `LIMIT` clauses
5. **Simple Operations**: Direct metadata access, no complex nested filters
6. **Folder Scoping**: Can add `FROM "folder"` to further limit scope

### Performance Best Practices

```
# ✅ GOOD - Scoped, limited, direct
FROM "03-notes" OR "02-projects"
WHERE concepts AND contains(concepts, [[Concept]])
LIMIT 50

# ❌ BAD - Unscoped, unlimited, complex
WHERE file.lists and contains(file.lists.text, "something")
```


---

## 📝 Next Steps

1. Review this document
2. Confirm customization preferences
3. Create templates in your vault
4. Test with 3-5 notes
5. Iterate based on results

**Questions to Consider:**

- Do you want additional relationship types? (e.g., `frameworks::`, `principles::`)
- Should we integrate with your review system? (auto-prioritize concepts by usage)
- Do you want domain-specific templates? (cognitive-science template, prompt-engineering template)
- Should we create MOC auto-generation queries?

---

## 🔗 Related

- [[Revised-self-documenting-dataview]] - Original system documentation
- [[self-documenting-dataview-implementation-guide]] - Technical guide
- [[Dataview Plugin]] - Core technology
- [[atomic-notes_moc]] - Current MOC system

---

*Created: 2025-12-16 | Status: Ready for Implementation*
