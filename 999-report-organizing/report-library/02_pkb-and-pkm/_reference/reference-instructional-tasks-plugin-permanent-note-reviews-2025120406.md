---
aliases:
  - "Tasks Plugin"
  - "Permanent Note Reviews"
tags:
  - "type/report"
  - "year/2025"
  - "type/tutorial"
  - "status/in-progress"
  - "productivity-systems"
  - "pkb"
  - "review-system"
  - "self-improvement/productivity"
  - "skill-acquisition"
  - "cognitive-resources"
  - "pkb/optimization"
  - "tasks-plugin"
  - "cognitive-pkm"
source: "claude-sonnet-4.5"
id: "20251204063215"
created: "2025-12-04T06:32:15"
modified: "2025-12-04T06:32:15"
week: "[[2025-W49]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: "tutorial"
maturity: "needs-review"
confidence: "speculative"
next-review: "2025-12-11"
review-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-12-04|Daily-Note]]"
---

> [!purpose] ### Overview
> - **Title**:: [[Tasks Plugin Integration for Permanent Note Reviews]]
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

# Tasks Plugin Integration for Permanent Note Reviews


# Tasks Plugin Integration for Permanent Note Reviews

---
tags: #tasks-plugin #review-system #automation #spaced-repetition
aliases: [Review Task Automation, Spaced Repetition System]
---

> [!abstract] Overview
> This guide implements an intelligent review system using the Tasks plugin, automating spaced repetition schedules based on note maturity levels and confidence ratings.

## 📑 Table of Contents

1. [[#Automated Review Task Creation]]
2. [[#Spaced Repetition Configuration]]
3. [[#Review Task Queries]]
4. [[#Templater Integration for Auto-Tasks]]
5. [[#Review Completion Workflows]]

---

## 1️⃣ Automated Review Task Creation

### 1.1 Add to Enhanced Template

Insert this section into your permanent note template (after Evolution Log section):

````markdown
---

## 📅 Review Tasks

> [!important] Automated Review Schedule
> Tasks are auto-generated based on maturity level. Mark complete when reviewed, new task will generate automatically.

```tasks
not done
description includes {{title}}
sort by due
```

### Initial Review Task
- [ ] Review concept: [[<% title %>]] 📅 <% nextReview %> ⏫ 🔁 every <% maturity === "seedling" ? "1 week" : maturity === "budding" ? "2 weeks" : maturity === "developing" ? "1 month" : "3 months" %>

---
````

**How It Works**:
- Creates recurring task linked to note title
- Due date set via `nextReview` variable from template
- Recurrence interval based on maturity level
- Tasks query shows all pending reviews for THIS note

---

### 1.2 Manual Task Creation (For Existing Notes)

For notes created before implementing this system:

```markdown
- [ ] Review [[Note Title]] 📅 2024-11-21 ⏫ 🔁 every 1 week
```

**Task Components Explained**:
- `[ ]` - Task checkbox
- `[[Note Title]]` - Link to note being reviewed
- `📅 2024-11-21` - Due date (Tasks plugin syntax)
- `⏫` - High priority emoji (Tasks recognizes this)
- `🔁 every 1 week` - Recurrence rule

---

## 2️⃣ Spaced Repetition Configuration

### 2.1 Maturity-Based Review Intervals

| Maturity Level | Review Frequency | Reasoning |
|----------------|------------------|-----------|
| **Seedling** | Every 7 days | Frequent review to develop understanding |
| **Budding** | Every 14 days | Bi-weekly reinforcement as concept solidifies |
| **Developing** | Every 30 days | Monthly check-ins for refinement |
| **Evergreen** | Every 90 days | Quarterly maintenance for stable concepts |
| **Needs Review** | Immediate | Flagged for urgent attention |

---

### 2.2 Confidence-Adjusted Intervals

For notes with low confidence despite high maturity, use shorter intervals:

```markdown
<%*
// In your Templater template, calculate review interval
let baseInterval = 7; // Default: 1 week
if (maturity === "seedling") {
    baseInterval = 7;
} else if (maturity === "budding") {
    baseInterval = 14;
} else if (maturity === "developing") {
    baseInterval = 30;
} else if (maturity === "evergreen") {
    baseInterval = 90;
}
// Adjust for low confidence
if (confidence === "speculative" || confidence === "provisional") {
    baseInterval = Math.max(7, baseInterval / 2);
}
const nextReview = tp.date.now("YYYY-MM-DD", baseInterval);
_%>
- [ ] Review [[<% title %>]] 📅 <% nextReview %> ⏫ 🔁 every <% baseInterval %> days
```

**Logic**:
- Low confidence halves review interval
- Minimum interval remains 7 days
- Ensures frequent revisiting of uncertain content

---

## 3️⃣ Review Task Queries

### 3.1 Daily Review Dashboard

Create a daily note section or dedicated review dashboard:

`````markdown
# Daily Review Dashboard

## ⚡ Due Today

```tasks
not done
due today
description includes Review
sort by priority
```

## ⏰ Due This Week

```tasks
not done
due before in 7 days
description includes Review
sort by due
limit 20
```

## 🚨 Overdue Reviews

```tasks
not done
due before today
description includes Review
sort by due
```
```

---

### 3.2 Maturity-Specific Review Lists

```markdown
## 🌱 Seedling Reviews (Weekly Cadence)

```tasks
not done
description includes Review
description includes seedling
sort by due
```

## 🌿 Budding Reviews (Bi-Weekly Cadence)

```tasks
not done
description includes Review  
description includes budding
sort by due
```

## 🌳 Developing Reviews (Monthly Cadence)

```tasks
not done
description includes Review
description includes developing
sort by due
```

## 🌲 Evergreen Reviews (Quarterly Cadence)

```tasks
not done
description includes Review
description includes evergreen
sort by due
```
`````

**Customization**: Add maturity level to task description:
```markdown
- [ ] Review [[Note]] (seedling) 📅 2024-11-21
```

---

### 3.3 Priority-Based Review Queue

`````markdown
## 🔥 High Priority Reviews

```tasks
not done
description includes Review
priority is high
sort by due
limit 10
```

## ⚠️ Low Confidence Notes Needing Review

```tasks
not done
description includes Review
(description includes speculative) OR (description includes provisional)
sort by due
```
`````

---

## 4️⃣ Templater Integration for Auto-Tasks

### 4.1 Enhanced Template with Task Generation

Update your Templater template's review section:

`````javascript
<%*
// Calculate review interval based on maturity
let intervalDays = 7;
let intervalText = "1 week";
if (maturity === "seedling") {
    intervalDays = 7;
    intervalText = "1 week";
} else if (maturity === "budding") {
    intervalDays = 14;
    intervalText = "2 weeks";
} else if (maturity === "developing") {
    intervalDays = 30;
    intervalText = "1 month";
} else if (maturity === "evergreen") {
    intervalDays = 90;
    intervalText = "3 months";
}
// Adjust for confidence
if (confidence === "speculative" || confidence === "provisional") {
    intervalDays = Math.ceil(intervalDays / 2);
    intervalText = `${intervalDays} days`;
}
const nextReview = tp.date.now("YYYY-MM-DD", intervalDays);
const priority = (confidence === "speculative" || confidence === "provisional") ? "⏫" : "🔼";
_%>

## 📅 Review System

**Maturity Level**: `= this.maturity`  
**Confidence Level**: `= this.confidence`  
**Review Interval**: <% intervalText %>  
**Next Review**: <% nextReview %>

### Active Review Task

- [ ] Review [[<% title %>]] (<%maturity%> | <%confidence%>) 📅 <% nextReview %> <% priority %> 🔁 every <% intervalText %> #review

```tasks
not done
description includes [[<% title %>]]
description includes Review
```

**Review Checklist**:
- [ ] Definition still accurate?
- [ ] New connections identified?
- [ ] Applications validated?
- [ ] Confidence level appropriate?
- [ ] Maturity level still correct?
`````

---

### 4.2 Post-Template-Execution Hook (Advanced)

For automatic task file creation in a dedicated folder:

`````javascript
<%*
tp.hooks.on_all_templates_executed(async () => {
    const taskContent = `
---
type: review-task
target: "[[${title}]]"
maturity: ${maturity}
confidence: ${confidence}
created: ${dateNow}
---
# Review Task: ${title}
**Target Note**: [[${title}]]  
**Maturity**: ${maturity}  
**Confidence**: ${confidence}
## Task
- [ ] Review [[${title}]] 📅 ${nextReview} ${priority} 🔁 every ${intervalText} #review
**Checklist**:
- [ ] Verify definition accuracy
- [ ] Identify new connections
- [ ] Validate practical applications
- [ ] Assess confidence level
- [ ] Update maturity if needed
---
[[${title}|← Return to Concept]]
`;
    // Create task note in dedicated folder
    await tp.file.create_new(
        taskContent,
        `REVIEW-${id}-${title}`,
        false,
        "05_tasks/reviews"
    );
});
%>
`````

**Benefits**:
- Centralized review task storage
- Separate from concept notes
- Queryable via Dataview for analytics

---

## 5️⃣ Review Completion Workflows

### 5.1 Manual Review Completion

When completing a review task:

1. **Check the task box** - Task recurs automatically
2. **Update note metadata** - Increment `review-count`, update `modified`
3. **Assess status changes** - Adjust `maturity` or `confidence` if needed

**Meta Bind Button** (from previous guide):
```markdown
`BUTTON[complete-review]`
```

This single button handles all three steps automatically.

---

### 5.2 Review Completion Template Snippet

Create a Templater template for quick review notes:

**File**: `Templates/review-completion.md`

`````markdown
<%*
const targetNote = await tp.system.prompt("Note being reviewed (title):");
const reviewDate = tp.date.now("YYYY-MM-DD");
const observations = await tp.system.prompt("Key observations:", "", false, true);
const maturityChange = await tp.system.suggester(
    ["No Change", "Advance Maturity", "Needs More Development"],
    ["no-change", "advance", "regress"]
);
const confidenceChange = await tp.system.suggester(
    ["No Change", "Increase Confidence", "Decrease Confidence"],
    ["no-change", "increase", "decrease"]
);
_%>

---
type: review-log
target: [[<% targetNote %>]]
date: <% reviewDate %>
---

# Review Log: <% targetNote %>

**Date**: <% reviewDate %>  
**Reviewer**: [Your Name]

## Observations

<% observations %>

## Status Changes

- **Maturity**: <% maturityChange %>
- **Confidence**: <% confidenceChange %>

## Actions Taken

- [ ] Updated frontmatter
- [ ] Added new connections
- [ ] Refined definition
- [ ] Added practical examples

## Next Review

Scheduled via recurring task.

---

[[<% targetNote %>|← Return to Concept]]
`````

**Usage**:
1. Complete review task
2. Run this template
3. Link review log to concept note

---

### 5.3 Automated Review Analytics

Track review completion rates:

```
TABLE WITHOUT ID
    date AS "Review Date",
    target AS "Concept Reviewed",
    "[[" + file.name + "|Log]]" AS "Details"
FROM "05_tasks/review-logs"
WHERE type = "review-log"
SORT date DESC
LIMIT 20
```

**Review Streak Calculation**:

```
TABLE 
    length(rows) AS "Reviews Completed",
    min(rows.date) AS "First Review",
    max(rows.date) AS "Last Review",
    round((date(today) - min(rows.date)).days / length(rows), 1) + " days" AS "Avg Interval"
FROM "05_tasks/review-logs"
GROUP BY target
SORT length(rows) DESC
```

---

## 🎯 Advanced Automation Patterns

### Pattern 1: Batch Review Session

Create a daily note template section:

`````markdown
## 📚 Batch Review Session

```tasks
not done
due today
description includes Review
sort by priority
```

**Session Workflow**:
1. Click task to open concept note
2. Read and assess
3. Click `BUTTON[complete-review]`
4. Mark task complete (auto-recurs)
5. Move to next task
```

---

### Pattern 2: Review Reminder Notifications

Use Tasks plugin's built-in reminder syntax:

```markdown
- [ ] Review [[Note Title]] 📅 2024-11-21 ⏰ 09:00 ⏫ 🔁 every 1 week
```

**⏰ 09:00** triggers OS notification at 9:00 AM on due date.

---

### Pattern 3: Confidence-Triggered Emergency Reviews

Automatically create urgent review tasks for low-confidence notes:

```javascript
<%*
// In template
if (confidence === "speculative" || confidence === "provisional") {
    const urgentReview = tp.date.now("YYYY-MM-DD", 1); // Tomorrow
    tR += `\n- [ ] 🚨 URGENT: Verify claims in [[${title}]] 📅 ${urgentReview} ⏫ #urgent-review\n`;
}
%>
`````

---

```
## 🔧 Setup Checklist

- [ ] Tasks plugin installed and enabled
- [ ] Review task format added to permanent note template
- [ ] Review dashboard created (daily note or dedicated page)
- [ ] Meta Bind complete-review button configured
- [ ] Review log template created (optional)
- [ ] Test: Create note → Check task generates → Complete task → Verify recurrence
```

---

## 📊 Review System Analytics

### Completion Rate Dashboard

```
TABLE WITHOUT ID
    "Total Concepts" AS "Metric",
    length(filter(app.vault.getMarkdownFiles(), (f) => f.frontmatter?.type === "permanent-note")) AS "Count"
WHERE file.name = this.file.name
```

```
TABLE WITHOUT ID
    "Completed Reviews (Last 30 Days)" AS "Metric",
    length(filter(app.vault.getMarkdownFiles(), (f) => 
        f.frontmatter?.type === "review-log" AND 
        (date(today) - date(f.frontmatter.date)).days <= 30
    )) AS "Count"
WHERE file.name = this.file.name
```

### Average Review Interval

```
const notes = dv.pages('"03_notes/01_permanent-notes"')
    .where(p => p.type === "permanent-note" && p["review-count"] > 0);

const avgReviews = notes.array().reduce((sum, p) => sum + p["review-count"], 0) / notes.length;

dv.paragraph(`**Average Reviews per Note**: ${avgReviews.toFixed(1)}`);
```

---

## 🎓 Learning Outcomes

After implementing Tasks integration:

✅ Automated spaced repetition system  
✅ Zero manual review scheduling  
✅ Intelligent intervals based on maturity  
✅ Priority queuing for low-confidence notes  
✅ Completion tracking and analytics  
✅ Seamless integration with daily workflows

---

**Next Steps**:
1. [[Review Analytics Dashboard]] - Visualize review patterns
2. [[Advanced Task Automation with QuickAdd]] - Macro-driven workflows
3. [[Spaced Repetition Science]] - Optimize intervals based on research

