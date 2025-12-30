---
aliases:
  - Meta Bind
  - Cognitive Science Notes
tags:
  - type/report
  - year/2025
  - type/tutorial
  - status/in-progress
  - vault-architecture
  - cognitive-science
  - metadata-systems
  - critical-thinking/problem-solving
  - cognitive-load-management
  - extended-cognition
  - pkb/optimization
  - meta-bind
  - cognitive-pkm
source: claude-sonnet-4.5
id: "20251204063623"
created: 2025-12-04T06:36:23
modified: 2025-12-04T06:36:23
week: "[[2025-W49]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: tutorial
maturity: seedling
confidence: speculative
next-review: 2025-12-11
review-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-12-04|Daily-Note]]"
---

> [!purpose] ### Overview
> - **Title**:: [[Meta Bind Integration for Cognitive Science Notes]]
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
WHERE  type = "tutorial"
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
### 2025-12-04 - Initial Creation
*Context*: `=this.title` **by**: `=this.source`
*Maturity*: `= this.maturity`  
*Confidence*: `= this.confidence`

### Tags & Classification
*Primary Tags*: `= this.tags`  
*Type*: `= this.type`  
*Source*: `= this.source`
---

# Meta Bind Integration for Cognitive Science Notes


# Meta Bind Integration for Cognitive Science Notes

---
tags: #meta-bind #interactive-notes #automation #reference
aliases: [Interactive Note Elements, Meta Bind Buttons]
---

> [!abstract] Overview
> This guide provides production-ready Meta Bind components for interactive permanent note management. Includes buttons, input fields, progress trackers, and status toggles.

## 📑 Table of Contents

1. [[#Status Management Buttons]]
2. [[#Review System Automation]]
3. [[#Interactive Metadata Fields]]
4. [[#Progress Tracking]]
5. [[#Quick Action Buttons]]
6. [[#View Fields (Display Only)]]

---
```meta-bind-button
id: maturity-seedling
label: 🌱 Seedling
style: default
action:
  type: updateMetadata
  bindTarget: maturity
  evaluate: false
  value: seedling
```
## 1️⃣ Status Management Buttons

### 1.1 Maturity Level Progression

Add these buttons to quickly update note maturity:

```markdown
## 🌱 Development Status

**Current Maturity**: `VIEW[{maturity}]`

`BUTTON[maturity-seedling]`
`BUTTON[maturity-budding]`
`BUTTON[maturity-developing]`
`BUTTON[maturity-evergreen]`

```

**Button Configuration** (Settings → Meta Bind → Button Templates):

```yaml
# Button Template: maturity-seedling
id: maturity-seedling
label: 🌱 Seedling
style: default
action:
  type: updateMetadata
  bindTarget: maturity
  evaluate: false
  value: seedling
```

```yaml
# Button Template: maturity-budding
id: maturity-budding
label: 🌿 Budding
style: default
action:
  type: updateMetadata
  bindTarget: maturity
  evaluate: false
  value: budding
  

```

```meta-bind-button
label: maturity-budding
icon: 🌿Budding
style: default
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: maturity-budding
hidden: false
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: budding

```

```yaml
# Button Template: maturity-developing
id: maturity-developing
label: 🌳 Developing
style: primary
action:
  type: updateMetadata
  bindTarget: maturity
  evaluate: false
  value: developing
```

```yaml
# Button Template: maturity-evergreen
id: maturity-evergreen
label: 🌲 Evergreen
style: primary
action:
  type: updateMetadata
  bindTarget: maturity
  evaluate: false
  value: evergreen
```

**Usage**: Click button to instantly update frontmatter `maturity` field.

---

### 1.2 Confidence Level Toggle

```markdown
## 📊 Epistemic Status

**Current Confidence**: `VIEW[{confidence}]`

`BUTTON[conf-speculative]` | `BUTTON[conf-provisional]` | `BUTTON[conf-moderate]` | `BUTTON[conf-high]` | `BUTTON[conf-established]`
```

**Button Templates**:

```yaml
# Button Template: conf-speculative
id: conf-speculative
label: ❓ Speculative
style: default
action:
  type: updateMetadata
  bindTarget: confidence
  evaluate: false
  value: speculative
```

```yaml
# Button Template: conf-provisional
id: conf-provisional
label: ⚠️ Provisional
style: default
action:
  type: updateMetadata
  bindTarget: confidence
  evaluate: false
  value: provisional
```

```yaml
# Button Template: conf-moderate
id: conf-moderate
label: ➡️ Moderate
style: default
action:
  type: updateMetadata
  bindTarget: confidence
  evaluate: false
  value: moderate
```

```yaml
# Button Template: conf-high
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
# Button Template: conf-established
id: conf-established
label: ⭐ Established
style: primary
action:
  type: updateMetadata
  bindTarget: confidence
  evaluate: false
  value: established
```

---

## 2️⃣ Review System Automation

### 2.1 Complete Review & Schedule Next

```markdown
## 📅 Review System

**Last Review**: `VIEW[{modified}]`  
**Next Review**: `VIEW[{next-review}]`  
**Total Reviews**: `VIEW[{review-count}]`

`BUTTON[complete-review]`
```

**Button Template**:

```yaml
# Button Template: complete-review
id: complete-review
label: ✅ Mark Reviewed
style: primary
actions:
  - type: updateMetadata
    bindTarget: review-count
    evaluate: true
    value: "meta.review-count + 1"
  
  - type: updateMetadata
    bindTarget: modified
    evaluate: true
    value: "date.now"
  
  - type: updateMetadata
    bindTarget: next-review
    evaluate: true
    value: |
      if (meta.maturity === "seedling") {
        return date(date.now).plus({days: 7}).toFormat("yyyy-MM-dd");
      } else if (meta.maturity === "budding") {
        return date(date.now).plus({days: 14}).toFormat("yyyy-MM-dd");
      } else if (meta.maturity === "developing") {
        return date(date.now).plus({days: 30}).toFormat("yyyy-MM-dd");
      } else if (meta.maturity === "evergreen") {
        return date(date.now).plus({days: 90}).toFormat("yyyy-MM-dd");
      } else {
        return date(date.now).plus({days: 7}).toFormat("yyyy-MM-dd");
      }
```

**How It Works**:
1. Increments `review-count` by 1
2. Updates `modified` to current date/time
3. Sets `next-review` based on maturity level:
   - Seedling: 7 days
   - Budding: 14 days
   - Developing: 30 days
   - Evergreen: 90 days

---

### 2.2 Flag for Urgent Review

```markdown
`BUTTON[flag-review]`
```

```yaml
# Button Template: flag-review
id: flag-review
label: 🚩 Flag for Review
style: destructive
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: needs-review
  
  - type: updateMetadata
    bindTarget: next-review
    evaluate: true
    value: date.now
  
  - type: createNote
    folderPath: 00_inbox
    fileName: "Review Needed - {{title}}"
    content: |
      # Review Needed: {{title}}
      
      **Flagged**: {{date.now}}
      **Reason**: [Add reason here]
      
      [[{{fileName}}]]
```

**Purpose**: Creates review task note and sets immediate review date

---

## 3️⃣ Interactive Metadata Fields

### 3.1 Editable Inline Fields

Instead of static frontmatter, create editable fields directly in note body:

```markdown
## 📝 Quick Edit Metadata

**Title**: `INPUT[text:title]`  
**Type**: `INPUT[select(option(concept), option(principle), option(framework), option(theory)):type]`  
**Maturity**: `INPUT[select(option(seedling), option(budding), option(developing), option(evergreen)):maturity]`  
**Confidence**: `INPUT[select(option(speculative), option(provisional), option(moderate), option(high), option(established)):confidence]`  
**Next Review**: `INPUT[date:next-review]`
```

**Features**:
- Real-time frontmatter updates
- No need to edit raw YAML
- Dropdown selections prevent typos

---

### 3.2 Dynamic Tag Editor

```markdown
## 🏷️ Tag Management

**Primary Domain**: `INPUT[text:tag1]`  
**Secondary Domain**: `INPUT[text:tag2]`  
**Sub-Domain**: `INPUT[text:tag3]`  
**Granular Tags**: `INPUT[textArea(2):tags]`
```

**Usage**: 
- Edit tags in-place
- `textArea` for multi-line tag lists
- Auto-updates frontmatter

---

## 4️⃣ Progress Tracking

### 4.1 Development Progress Bar

```markdown
## 📊 Development Progress

**Maturity Level**: `VIEW[{maturity}]`

```meta-bind
INPUT[progressBar(
  value(meta.maturity = "seedling" ? 25 : 
        meta.maturity = "budding" ? 50 : 
        meta.maturity = "developing" ? 75 : 100)
):_inlineProgress]
```

**Completion**: `VIEW[{_inlineProgress}]`%
```

**Visual Indicator**:
- Seedling: 25% progress
- Budding: 50% progress
- Developing: 75% progress
- Evergreen: 100% progress

---

### 4.2 Review Streak Counter

```markdown
## 🔥 Review Streak

**Total Reviews**: `VIEW[{review-count}]`  
**Current Streak**: `VIEW[{review-streak}]`

```meta-bind
INPUT[progressBar(
  value(meta.review-count * 10)
):_reviewProgress]
```

**Goal**: 10 reviews = 100%
```

---

## 5️⃣ Quick Action Buttons

### 5.1 Open Related Notes

```markdown
`BUTTON[open-link-up]` | `BUTTON[open-related]`
```

```yaml
# Button Template: open-link-up
id: open-link-up
label: 📚 Open MOC
action:
  type: open
  link: "{{meta.link-up[0]}}"
  newTab: true
```

```yaml
# Button Template: open-related
id: open-related
label: 🔗 Open Related
action:
  type: command
  command: "dataview: execute-query"
  args:
    query: |
      LIST
      FROM [[{{fileName}}]]
      SORT file.ctime DESC
      LIMIT 10
```

---

### 5.2 Create Linked Literature Note

```markdown
`BUTTON[create-literature-note]`
```

```yaml
# Button Template: create-literature-note
id: create-literature-note
label: 📖 Create Literature Note
style: primary
action:
  type: createNote
  folderPath: 02_literature-notes
  fileName: "LIT-{{date.now:YYYYMMDDHHmmss}}-{{title}}"
  openNote: true
  content: |
    ---
    type: literature
    source: "{{meta.source}}"
    related-concept: "[[{{fileName}}]]"
    created: {{date.now}}
    ---
    
    # Literature Note: {{title}}
    
    **Related Concept**: [[{{fileName}}]]
    **Source**: {{meta.source}}
    
    ## Summary
    
    
    ## Key Quotes
    
    
    ## Connections to [[{{fileName}}]]
    
```

**Purpose**: Quickly create supporting literature note linked to current concept

---

### 5.3 Export to Anki Flashcard

```markdown
`BUTTON[export-anki]`
```

```yaml
# Button Template: export-anki
id: export-anki
label: 🎴 Create Flashcard
action:
  type: createNote
  folderPath: 99_anki-export
  fileName: "ANKI-{{title}}"
  content: |
    ---
    anki-deck: Cognitive Science
    anki-type: Basic
    ---
    
    # {{title}} - Flashcard
    
    ## Front
    What is {{title}}?
    
    ## Back
    {{meta.definition}}
    
    Source: [[{{fileName}}]]
```

---

## 6️⃣ View Fields (Display Only)

### 6.1 Metadata Dashboard

```markdown
## 📊 Note Statistics

| Metric | Value |
|--------|-------|
| **Created** | `VIEW[{created}]` |
| **Modified** | `VIEW[{modified}]` |
| **Maturity** | `VIEW[{maturity}]` |
| **Confidence** | `VIEW[{confidence}]` |
| **Review Count** | `VIEW[{review-count}]` |
| **Next Review** | `VIEW[{next-review}]` |
| **Backlinks** | `VIEW[length({file.inlinks})]` |
| **Outlinks** | `VIEW[length({file.outlinks})]` |
```

**Purpose**: Live-updating stats without Dataview query

---

### 6.2 Conditional Status Badges

`````markdown
## Status Indicators

```meta-bind-js-view
{maturity} as maturity
{confidence} as confidence
---
if (maturity === "seedling") {
  return "🌱 **New Concept** - Needs Development";
} else if (maturity === "budding") {
  return "🌿 **Growing** - Basic Structure Established";
} else if (maturity === "developing") {
  return "🌳 **Maturing** - Active Refinement";
} else if (maturity === "evergreen") {
  return "🌲 **Established** - Stable & Well-Supported";
} else {
  return "❓ Status Unknown";
}
```

**Alert Level**: 
```meta-bind-js-view
{confidence} as confidence
---
if (confidence === "speculative" || confidence === "provisional") {
  return "⚠️ LOW CONFIDENCE - Verify Claims";
} else if (confidence === "moderate") {
  return "➡️ MODERATE - Generally Reliable";
} else {
  return "✅ HIGH CONFIDENCE - Well-Validated";
}
```
`````

---

## 🔧 Setup Instructions

### Step 1: Install Meta Bind Plugin

1. Open Obsidian Settings
2. Community Plugins → Browse
3. Search "Meta Bind"
4. Install and Enable

### Step 2: Configure Button Templates

1. Settings → Meta Bind → Button Templates
2. Copy each button template from this guide
3. Paste into button template configuration
4. Save

### Step 3: Add to Note Template

Copy desired sections into your Templater template at appropriate locations.

### Step 4: Test Functionality

1. Create new note from template
2. Click buttons to verify metadata updates
3. Check frontmatter changes in source mode

---

## 🎯 Advanced Patterns

### Multi-Action Button (Review + Maturity Update)

```yaml
id: advance-maturity-and-review
label: 🚀 Advance & Review
style: primary
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: true
    value: |
      if (meta.maturity === "seedling") return "budding";
      if (meta.maturity === "budding") return "developing";
      if (meta.maturity === "developing") return "evergreen";
      return meta.maturity;
  
  - type: updateMetadata
    bindTarget: review-count
    evaluate: true
    value: "meta.review-count + 1"
  
  - type: updateMetadata
    bindTarget: modified
    evaluate: true
    value: date.now
```

**Purpose**: Single-click maturity progression with review tracking

---

### Conditional Button Display

```meta-bind-js-view
{maturity} as maturity
---
if (maturity === "seedling") {
  return `BUTTON[maturity-budding]`;
} else if (maturity === "budding") {
  return `BUTTON[maturity-developing]`;
} else if (maturity === "developing") {
  return `BUTTON[maturity-evergreen]`;
} else {
  return "✅ Already Evergreen!";
}
```

**Purpose**: Only show "next step" button based on current status

---
`BUTTON[example-id]` 
## 📚 Integration with Other Plugins

### With Tasks Plugin

```markdown
- [ ] Review [[{{fileName}}]] `BUTTON[complete-review-task]` 📅 {{meta.next-review}}
```

### With Dataview Inline Queries

```markdown
**Notes at Same Maturity**: `= length(filter(app.vault.getMarkdownFiles(), (f) => f.frontmatter?.maturity === this.maturity))`
```

### With Calendar Plugin

```markdown
`BUTTON[add-to-calendar]`
```

```yaml
id: add-to-calendar
label: 📅 Add Review to Calendar
action:
  type: createNote
  folderPath: 01_calendar
  fileName: "{{meta.next-review}}"
  content: |
    # {{meta.next-review}}
    
    ## Reviews Due
    - [ ] Review [[{{fileName}}]]
```

---

## 🎓 Learning Outcomes

After implementing Meta Bind:

✅ One-click status updates (no manual YAML editing)  
✅ Intelligent review scheduling based on maturity  
✅ Visual progress indicators for note development  
✅ Quick-action workflows for common tasks  
✅ Real-time metadata editing without source mode  
✅ Conditional UI elements based on note state

---

**Next Steps**:
1. [[Tasks Plugin Integration]] - Automate review task creation
2. [[Advanced Meta Bind Scripting]] - Custom JavaScript actions
3. [[Dashboard Design Patterns]] - Combine queries + buttons

