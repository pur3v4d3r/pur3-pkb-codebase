






```dataviewjs
// CONFIGURATION
const cognitivePath = "04-library/01-cognitive-science";
const pkbPath = "04-library/02-pkb-and-pkm-learning";
const inboxPath = "00-inbox";

// DATA GATHERING
let cogNotes = dv.pages(`"${cognitivePath}"`).length;
let pkbNotes = dv.pages(`"${pkbPath}"`).length;
let inboxCount = dv.pages(`"${inboxPath}"`).length;

// RENDER METRIC CARDS
dv.span(`
<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
    <div style="background: rgba(55, 155, 55, 0.1); padding: 15px; border-radius: 10px; text-align: center; width: 30%;">
        <h2 style="margin:0;">🗃️ ${inboxCount}</h2>
        <small>Inbox Load</small>
    </div>
    <div style="background: rgba(55, 55, 155, 0.1); padding: 15px; border-radius: 10px; text-align: center; width: 30%;">
        <h2 style="margin:0;">🧠 ${cogNotes}</h2>
        <small>CogSci Knowledge Base</small>
    </div>
    <div style="background: rgba(155, 55, 55, 0.1); padding: 15px; border-radius: 10px; text-align: center; width: 30%;">
        <h2 style="margin:0;">⚙️ ${pkbNotes}</h2>
        <small>PKB Architecture</small>
    </div>
</div>
`);

// RENDER RECENT ACTIVITY
dv.header(3, "🔍 Recent Operational Output");
dv.table(["File", "Folder", "Modified"],
    dv.pages(`#project/pur3v4d3r`)
    .sort(p => p.file.mtime, "desc")
    .limit(5)
    .map(p => [p.file.link, p.file.folder, p.file.mtime])
);
```




### Full Hub System designed by Claude

`````
# 🎯 Project Pur3v4d3r Hub System Engineering

## 📊 Project Pur3v4d3r Hub System

> [!abstract] System Overview
> **Objective:** Create a comprehensive, self-updating Hub Note that serves as command center for Project Pur3v4d3r, combining project management, navigation, metrics tracking, task aggregation, and maintenance systems.
> 
> **Plugins Required:** Dataview, Templater, Meta Bind, Tasks, Charts (optional for visualizations)
> **Estimated Implementation Time:** 45-60 minutes
> **Difficulty Level:** Advanced
> **Output:** Single hub note with six integrated sections

---

## 🛠️ Implementation

### Phase 1: Core Hub Note Creation

**Step 1: Create the Hub Note File**

1. Navigate to `02_projects/01_project-pur3v4d3r/`
2. Create new note named: `project-pur3v4d3r-hub.md`
3. This will be your central command center

**Step 2: Insert Complete Hub Note Code**

Copy the entire code block below into your hub note:

```markdown
---
title: "Project Pur3v4d3r: Command Center Hub"
id: "project-pur3v4d3r-hub"
type: pkb/components/hub-notes
status: operational
tags:
  - project/pur3v4d3r
  - pkb/components/hub-notes
  - pkb/components/dashboards
  - year/2025
aliases:
  - Pur3v4d3r Hub
  - Project Hub
  - Command Center
cssclasses:
  - hub-note
---

# 🎯 Project Pur3v4d3r: Command Center

> [!abstract] Mission Statement
> **Continuous Self-Education & Cognitive Science Mastery**
> 
> This project is an ongoing experiment in self-directed learning, developing both a sophisticated Personal Knowledge Base and deep expertise in Cognitive Psychology. The goal is to integrate cognitive science principles into the foundation of both myself and my PKB, ultimately producing original academic reports based on research conducted within this system.

---

## 📍 Quick Navigation Hub

> [!info] Primary Pathways
> Strategic entry points into the project's knowledge domains.

### 🧠 Cognitive Science Domain
- [[03_notes/01_permanent-notes/01_cognitive-development|Cognitive Development Notes]]
- [[04_library/01_cognitive-science/_reference|Reference Library]]
- [[04_library/01_cognitive-science/_reports|Research Reports]]
- [[00-inbox/01-reports/01-cognitive-science|Inbox: New Cognitive Science Materials]]

### 📚 PKB & PKM Development
- [[03_notes/01_permanent-notes/02_personal-knowledge-base|PKB Permanent Notes]]
- [[04_library/02_pkb-and-pkm-learning/_reference|PKB/PKM References]]
- [[04_library/02_pkb-and-pkm-learning/_reports|PKB Reports]]
- [[00-inbox/01-reports/02_pkb-and-pkm|Inbox: PKB/PKM Materials]]

### 🔬 Additional Domains
- [[03_notes/01_permanent-notes/03_cosmology|Cosmology Notes]]
- [[03_notes/01_permanent-notes/04_prompt-engineering|Prompt Engineering Notes]]
- [[04_library/03_prompt-engineering|Prompt Engineering Library]]
- [[04_library/04_cosmology|Cosmology Library]]

### 🗂️ Organizational Centers
- [[01_daily-notes/2025|2025 Daily Notes]]
- [[00-inbox|Central Inbox]]
- [[03_notes/02_quotes|Quote Collection]]

---

## 📊 Project Dashboard

> [!tip] Live Metrics & Progress Tracking
> Auto-updating statistics on project activity and knowledge base growth.

### 📈 Knowledge Base Statistics

```dataview
TABLE WITHOUT ID
    "**" + metric + "**" AS "Metric",
    value AS "Count"
FROM ""
WHERE file.name = "project-pur3v4d3r-hub"
FLATTEN [
    {metric: "Total Notes", value: length(filter(app.vault.getMarkdownFiles(), (f) => !contains(f.path, ".trash")))},
    {metric: "Permanent Notes", value: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "03_notes/01_permanent-notes")))},
    {metric: "Reference Materials", value: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "04_library") && contains(f.path, "_reference")))},
    {metric: "Research Reports", value: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "_reports")))},
    {metric: "Daily Notes (2025)", value: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "01_daily-notes/2025")))}
] AS item
FLATTEN item.metric AS metric, item.value AS value
```

### 🛡️ Integrity Check (Missing Metadata)

```dataview
TABLE file.folder as "Location", file.cday as "Created"
FROM "00-inbox" OR "04_library"
WHERE !contains(file.tags, "#type") OR !contains(file.tags, "#status")
SORT file.cday desc
LIMIT 10
```
### 🎓 Domain-Specific Progress

```dataview
TABLE WITHOUT ID
    domain AS "Knowledge Domain",
    notes AS "Notes Created",
    reports AS "Reports Generated"
FROM ""
WHERE file.name = "project-pur3v4d3r-hub"
FLATTEN [
    {
        domain: "Cognitive Science",
        notes: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "01-cognitive-development") || contains(f.path, "01-cognitive-science"))),
        reports: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "01_cognitive-science/_reports")))
    },
    {
        domain: "📚 PKB/PKM",
        notes: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "02_personal-knowledge-base") || contains(f.path, "02_pkb-and-pkm"))),
        reports: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "02_pkb-and-pkm-learning/_reports")))
    },
    {
        domain: "🔬 Cosmology",
        notes: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "03_cosmology") || contains(f.path, "04_cosmology"))),
        reports: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "04_cosmology/_reports")))
    },
    {
        domain: "💡 Prompt Engineering",
        notes: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "04_prompt-engineering"))),
        reports: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "03_prompt-engineering/_reports")))
    }
] AS item
FLATTEN item.domain AS domain, item.notes AS notes, item.reports AS reports
```

### 📅 Recent Activity (Last 7 Days)

```dataview
TABLE WITHOUT ID
    file.link AS "Recently Modified",
    dateformat(file.mtime, "yyyy-MM-dd HH:mm") AS "Last Modified",
    file.folder AS "Location"
FROM "02_projects/01_project-pur3v4d3r" OR "03_notes" OR "04_library"
WHERE file.mtime >= date(today) - dur(7 days)
    AND file.name != "project-pur3v4d3r-hub"
SORT file.mtime DESC
LIMIT 15
```

### 🎯 Inbox Processing Status

```dataview
TABLE WITHOUT ID
    inbox AS "Inbox Location",
    count AS "Items to Process"
FROM ""
WHERE file.name = "project-pur3v4d3r-hub"
FLATTEN [
    {inbox: "📋 General Inbox", count: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "00-inbox") && !contains(f.path, "01-reports")))},
    {inbox: "🧠 Cognitive Science Reports", count: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "00-inbox/01-reports/01-cognitive-science")))},
    {inbox: "📚 PKB/PKM Reports", count: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "00-inbox/01-reports/02_pkb-and-pkm")))},
    {inbox: "💡 Prompt Engineering", count: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "00-inbox/01-reports/03_prompt-engineering")))},
    {inbox: "🔬 Cosmology Reports", count: length(filter(app.vault.getMarkdownFiles(), (f) => contains(f.path, "00-inbox/01-reports/04-cosmology")))}
] AS item
FLATTEN item.inbox AS inbox, item.count AS count
```

---

## ✅ Task Command Center

> [!warning] Active Task Management
> Aggregated view of all tasks across the PKB with intelligent filtering.

### 🔥 Priority Tasks (High-Urgency)

```dataview
TASK
FROM "02_projects/01_project-pur3v4d3r" OR "03_notes" OR "04_library"
WHERE !completed 
    AND (contains(text, "urgent") OR contains(text, "priority") OR contains(text, "critical"))
SORT file.mtime DESC
LIMIT 20
```

### 📅 Tasks with Due Dates

```dataview
TASK
FROM "02_projects/01_project-pur3v4d3r" OR "03_notes" OR "04_library"
WHERE !completed AND due
SORT due ASC
LIMIT 10
```

### 🧠 Domain-Specific Tasks

**Cognitive Science Tasks:**
```dataview
TASK
FROM "03_notes/01_permanent-notes/01_cognitive-development" OR "04_library/01_cognitive-science"
WHERE !completed
SORT file.mtime DESC
LIMIT 10
```

**PKB Development Tasks:**
```dataview
TASK
FROM "03_notes/01_permanent-notes/02_personal-knowledge-base" OR "04_library/02_pkb-and-pkm-learning"
WHERE !completed
SORT file.mtime DESC
LIMIT 10
```

### 📋 All Incomplete Tasks (Comprehensive View)

```dataview
TASK
FROM "02_projects" OR "03_notes" OR "04_library"
WHERE !completed
LIMIT 40
GROUP BY file.folder
SORT file.folder ASC
```

---

## 🔧 Maintenance Control Panel

> [!important] System Maintenance & Housekeeping
> Scheduled maintenance tasks to keep the PKB optimized and organized.

### Daily Maintenance Checklist

- [ ] **Process Inbox Items** - Review and categorize new materials in `00-inbox/`
- [ ] **Update Daily Note** - Complete today's daily note with reflections and links
- [ ] **Task Review** - Check priority tasks and update statuses
- [ ] **Quick Links Audit** - Verify no broken links in today's work

### Weekly Maintenance Checklist

- [ ] **Metadata Audit** - Review and standardize tags across new notes
- [ ] **Folder Organization** - Ensure files are in correct locations
- [ ] **Reference Cleanup** - Archive or delete unused reference materials
- [ ] **Permanent Notes Review** - Identify fleeting notes ready for promotion
- [ ] **Backup Verification** - Confirm vault backup completed successfully

### Monthly Maintenance Checklist

- [ ] **Plugin Updates** - Check for and install plugin updates
- [ ] **Query Optimization** - Review slow-running Dataview queries
- [ ] **Knowledge Graph Analysis** - Examine orphaned notes and link density
- [ ] **Report Generation** - Compile monthly progress report
- [ ] **Goal Alignment Review** - Assess progress toward learning objectives

### 🔍 System Health Diagnostics

**Orphaned Notes (No Inlinks):**
```dataview
LIST
FROM "03_notes" OR "04_library"
WHERE length(file.inlinks) = 0 
    AND file.name != "project-pur3v4d3r-hub"
    AND !contains(file.path, "00-inbox")
SORT file.name ASC
LIMIT 20
```

**Notes Without Tags:**
```dataview
LIST
FROM "03_notes" OR "04_library"
WHERE !file.tags
    AND file.name != "project-pur3v4d3r-hub"
SORT file.ctime DESC
LIMIT 15
```

**Old Inbox Items (>30 days):**
```dataview
TABLE
    file.ctime AS "Added",
    dateformat(date(today) - file.ctime, "d") + " days old" AS "Age"
FROM "00-inbox"
WHERE file.ctime < date(today) - dur(30 days)
SORT file.ctime ASC
LIMIT 30
```

---

## 📚 Knowledge Index & Analytics

> [!tip] Work Visualization & Productivity Metrics
> Analytical views of knowledge production and research output.

### 📝 Recent Permanent Notes

```dataview
TABLE WITHOUT ID
    file.link AS "Permanent Note",
    file.tags AS "Tags",
    dateformat(file.ctime, "yyyy-MM-dd") AS "Created"
FROM "03_notes/01_permanent-notes"
SORT file.ctime DESC
LIMIT 15
```

### 📊 Reports by Domain

```dataview
TABLE WITHOUT ID
    file.link AS "Research Report",
    file.folder AS "Domain",
    dateformat(file.ctime, "yyyy-MM-dd") AS "Completed"
FROM "04_library"
WHERE contains(file.path, "_reports")
SORT file.ctime DESC
LIMIT 20
```

### 🏆 Most Connected Notes (Link Density)

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    length(file.inlinks) AS "⬅️ Inlinks",
    length(file.outlinks) AS "➡️ Outlinks",
    length(file.inlinks) + length(file.outlinks) AS "Total Connections"
FROM "03_notes/01_permanent-notes" OR "04_library"
WHERE file.name != "project-pur3v4d3r-hub"
SORT (length(file.inlinks) + length(file.outlinks)) DESC
LIMIT 15
```

### 📅 Productivity Timeline (This Month)

```dataview
TABLE WITHOUT ID
    dateformat(file.ctime, "yyyy-MM-dd") AS "Date",
    length(rows) AS "Notes Created",
    rows.file.link AS "Notes"
FROM "03_notes" OR "04_library" OR "02_projects"
WHERE file.ctime >= date(today) - dur(30 days)
    AND file.name != "project-pur3v4d3r-hub"
GROUP BY dateformat(file.ctime, "yyyy-MM-dd")
SORT dateformat(file.ctime, "yyyy-MM-dd") DESC
```

### 🎯 Goal Tracking: Academic Report Production

```dataview
TABLE WITHOUT ID
    file.link AS "Academic Report",
    file.folder AS "Domain",
    choice(type = "cog-psy-report", "🧠 Cognitive Psychology",
           type = "pkb-report", "📚 PKB/PKM",
           type = "prompt-report", "💡 Prompt Engineering",
           type = "cosmo-report", "🔬 Cosmology",
           "📄 General") AS "Type",
    dateformat(file.ctime, "yyyy-MM-dd") AS "Published"
FROM "04_library"
WHERE contains(file.path, "_reports") 
    AND (type = "cog-psy-report" OR type = "pkb-report" OR type = "prompt-report" OR type = "cosmo-report" OR type = "report")
SORT file.ctime DESC
```

---

## 🎯 Project Status Overview

> [!abstract] High-Level Project Health

**Project Start Date:** 2025-11-21  
**Project Duration:** `= date(today) - date(2025-11-21)` days  
**Current Phase:** Continuous Development & Expansion

**Primary Objectives Status:**
- ✅ PKB Infrastructure Established
- 🔄 Cognitive Science Mastery (Ongoing)
- 🔄 Self-Education System Development (Ongoing)
- 🔄 Academic Report Production (Ongoing)
- ⏳ Expert-Level Understanding (Long-term Goal)

---

## 🔗 Quick Actions & Utilities

> [!helpful-tip] Frequently Used Operations

### Template Generation
- Create new Cognitive Science note
- Create new PKB/PKM note
- Create new Research Report
- Create new Daily Note

### Bulk Operations
- Tag all untagged notes in folder
- Move processed inbox items to library
- Generate MOC for domain
- Create weekly review note

---

## 📌 Notes & Reminders

**Hub Maintenance:** This hub note is designed to be self-updating through Dataview queries. Most sections refresh automatically when you open the note. 

**Customization:** Modify queries as needed to track different metrics or adjust filtering criteria. All queries are modular and can be extended.

**Performance:** If queries become slow, add LIMIT clauses or narrow FROM sources to specific folders.

---

*Last Hub Review: `= date(today)`*  
*Project Days Active: `= date(today) - date(2025-11-21)`*
```

---

## 🎓 Understanding the Hub Architecture

> [!methodology-and-sources] Design Philosophy
> This hub follows a **modular six-pillar architecture**:
> 
> 1. **Navigation Hub** - Quick access to all project pathways
> 2. **Dashboard** - Live metrics and progress tracking
> 3. **Task Command Center** - Aggregated task management with domain filtering
> 4. **Maintenance Panel** - Scheduled housekeeping operations
> 5. **Knowledge Index** - Analytics on knowledge production
> 6. **Quick Actions** - Utility functions (extensible)
> 
> Each section uses Dataview queries that automatically update when you view the note, providing real-time visibility into your PKB's state.

### Key Technical Components

**Dataview Query Patterns Used:**

1. **Statistical Aggregation** - Counting notes across folders
2. **Temporal Filtering** - Recent activity tracking (last 7 days, this month)
3. **Link Density Analysis** - Most connected notes
4. **Health Diagnostics** - Orphaned notes, untagged content, old inbox items
5. **Domain Segmentation** - Separate views per knowledge domain
6. **Task Filtering** - Priority, due date, and domain-specific task views

**Why This Architecture:**
- **Self-Updating** - No manual maintenance required for metrics
- **Modular** - Easy to add/remove/modify sections
- **Scalable** - Performs well as vault grows
- **Actionable** - Each section drives specific workflows

---

## 🔧 Customization & Extension

### Adding New Sections

To add a new section to the hub:

1. **Choose Section Type:**
   - Navigation links (manual curation)
   - Dataview query (dynamic content)
   - Task aggregation (using TASK queries)
   - Metrics/analytics (TABLE queries)

2. **Insert After Appropriate Section:**
   Use `---` horizontal rules to separate major sections

3. **Query Template:**
```dataview
TABLE/LIST/TASK
FROM "your/folder/path"
WHERE [filtering condition]
SORT [field] ASC/DESC
LIMIT [number]
```

### Modifying Existing Queries

**To adjust domain filters:**
Change folder paths in `FROM` clauses:
```
FROM "03_notes/01_permanent-notes/01_cognitive-development"
```

**To change time windows:**
Modify `dur()` values:
```
WHERE file.mtime >= date(today) - dur(14 days)  # Change 7 to 14 for 2 weeks
```

**To adjust result limits:**
Change `LIMIT` values:
```
LIMIT 25  # Increase from 15 to show more results
```

### Adding Interactive Buttons (Meta Bind)

To add interactive buttons for common actions:

```markdown
`BUTTON[quick-capture]`
```

Configure in Meta Bind settings to trigger:
- Template insertion
- QuickAdd macros
- File creation workflows
- Tag operations

---

## ⚡ Performance Optimization Tips

> [!helpful-tip] Keeping Queries Fast

1. **Use Specific FROM Sources:**
   ```
   FROM "specific/folder"  # Fast
   FROM ""                  # Slower (searches entire vault)
   ```

2. **Add LIMIT Clauses:**
   Prevents large result sets from slowing render
   ```
   LIMIT 20
   ```

3. **Use Indexed Fields:**
   Queries on `file.mtime`, `file.ctime`, `file.folder` are faster than complex string operations

4. **Avoid Nested Queries:**
   Pre-filter with WHERE instead of using filter() functions when possible

5. **Cache Results:**
   Dataview automatically caches query results; reloading the note uses cached data

---

## 📚 Integration with Other Systems

### Templater Integration

Create templates that automatically link back to hub:

```markdown
---
link-up:
  - "[[project-pur3v4d3r-hub]]"
---
```

Use Templater to open hub after creating certain note types:

```javascript

```

### QuickAdd Macro Workflows

Configure QuickAdd to:
1. Capture quick note → File to inbox → Update hub automatically
2. Generate daily note → Link to hub → Jump to today's tasks section
3. Create report → Add to domain folder → Refresh hub metrics

### Commander Hotkeys

Set hotkeys to:
- `Ctrl+Alt+H` - Open Project Hub
- `Ctrl+Alt+I` - Process Inbox (jump to inbox section)
- `Ctrl+Alt+T` - View All Tasks (jump to task section)

---

## 🎯 Next Steps After Hub Implementation

**Immediate Actions:**
1. ✅ Open hub note and verify all queries execute without errors
2. ✅ Bookmark hub (right-click → Bookmark or use bookmarks plugin)
3. ✅ Set hotkey for instant hub access (Commander or Obsidian hotkeys)
4. ✅ Add hub link to daily note template

**First Week:**
- Use hub daily to review progress and process tasks
- Identify which sections you use most frequently
- Customize queries based on your workflow patterns
- Add any missing domain pathways to navigation section

**First Month:**
- Establish maintenance routines (use checklists)
- Analyze knowledge index metrics for insights
- Extend hub with custom sections for specific needs
- Consider adding Charts plugin visualizations for trends

---

## 🔗 Related Automation Opportunities

1. **[[Automated Daily Hub Review]]**
   - *Connection*: Scheduled opening of hub at specific time
   - *Implementation*: Templater + Commander + scheduled command
   - *Value*: Consistent daily engagement with project metrics

2. **[[Inbox Processing Workflow]]**
   - *Connection*: Streamline movement from inbox to appropriate folders
   - *Implementation*: QuickAdd macros with suggester menus
   - *Value*: Reduce manual file organization overhead

3. **[[Domain-Specific Dashboards]]**
   - *Connection*: Separate focused dashboards for each knowledge domain
   - *Implementation*: Hub template adapted for Cognitive Science, PKB, etc.
   - *Value*: Deep-dive views with domain-specific metrics

4. **[[Automated Report Generation]]**
   - *Connection*: Template-driven academic report creation with metadata
   - *Implementation*: Templater + Dataview for sourcing research notes
   - *Value*: Structured research output workflow

Would you like me to engineer any of these additional automations, or would you prefer to customize any section of the hub further?

`````


### _permanent-note-dashboard
````
## 📊 Note Development
   
   ### Due for Review Today
```dataview
TABLE WITHOUT ID
    key AS "Maturity Level",
    length(rows) AS "Count",
    round(length(rows) / length(this.file.path) * 100, 1) + "%" AS "Percentage"
FROM "03_notes/01_permanent-notes"
WHERE type = "permanent-note" OR type = "concept"
GROUP BY maturity
SORT length(rows) DESC
```
   
   ### Seedlings Needing Attention
```dataview
LIST 
    "Created: " + dateformat(date(created), "MMM dd, yyyy") + " | Reviews: " + review-count
FROM "03_notes/01_permanent-notes"
WHERE maturity = "seedling" 
      AND date(created) < date(today) - dur(14 days)
SORT created ASC
```

## 📈 PKB Analytics
   
   ### Maturity Distribution
```dataview
TABLE WITHOUT ID
    key AS "Maturity Level",
    length(rows) AS "Count",
    round(length(rows) / length(this.file.path) * 100, 1) + "%" AS "Percentage"
FROM "03_notes/01_permanent-notes"
WHERE type = "permanent-note" OR type = "concept"
GROUP BY maturity
SORT length(rows) DESC
```
   
   ### Recent Activity
```dataview
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
   
   ### Knowledge Graph Health
```dataview
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

## 🔍 Discovery Queries
   
   ### By Confidence Level
```dataview
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
   
   ### Orphaned Notes
```dataview
LIST 
    "Created: " + dateformat(date(created), "MMM dd") + " | Maturity: " + maturity
FROM "03_notes/01_permanent-notes"
WHERE (length(file.inlinks) = 0 OR length(file.outlinks) = 0)
      AND type = "permanent-note"
SORT created DESC
```
`````

### _task-dashboard
````
---
aliases:
  - TASKS Dashboard
  - Tasks
  - Task
  - Task Dashboard
---

dataviewjs
```

// === CONFIGURATION ===
const DAYS_THRESHOLD_OLD = 90; // Tasks older than this are flagged as "stale"
const DAYS_THRESHOLD_RECENT = 7; // Tasks newer than this are "recent"
// === DATA COLLECTION ===
let tasksByFile = {};
let now = dv.luxon.DateTime.now();
for (let page of dv.pages()) {
    if (!page.file.tasks) continue;
    let incompleteTasks = page.file.tasks.filter(t => !t.completed);
    if (incompleteTasks.length > 0) {
        let fileAge = page.file.cday ? 
            now.diff(page.file.cday, 'days').days : null;
        tasksByFile[page.file.path] = {
            link: page.file.link,
            name: page.file.name,
            folder: page.file.folder,
            tags: page.file.tags || [],
            created: page.file.cday,
            modified: page.file.mtime,
            fileAge: fileAge,
            taskCount: incompleteTasks.length,
            tasks: incompleteTasks,
            // Enhanced classifications
            isStale: fileAge && fileAge > DAYS_THRESHOLD_OLD,
            isRecent: fileAge && fileAge < DAYS_THRESHOLD_RECENT,
            hasHighPriority: incompleteTasks.some(t => 
                t.text.includes("🔴") || 
                t.text.toLowerCase().includes("urgent") ||
                t.text.toLowerCase().includes("high priority")
            ),
            hasDeadline: incompleteTasks.some(t =>
                t.text.includes("📅") ||
                t.text.includes("due") ||
                t.text.match(/\d{4}-\d{2}-\d{2}/)
            ),
            hasContext: (page.file.tags || []).length > 0
        };
    }
}
// === ANALYTICS ===
let allFiles = Object.values(tasksByFile);
let totalTasks = allFiles.reduce((sum, f) => sum + f.taskCount, 0);
let staleFiles = allFiles.filter(f => f.isStale);
let priorityFiles = allFiles.filter(f => f.hasHighPriority);
let untaggedFiles = allFiles.filter(f => !f.hasContext);
// === HEADER OVERVIEW ===
dv.header(1, "🧹 Task Cleanup Command Center");
dv.paragraph(`
| Metric | Count |
|--------|-------|
| 📂 Files with Tasks | ${allFiles.length} |
| ✅ Total Incomplete Tasks | ${totalTasks} |
| ⏰ Stale Files (>${DAYS_THRESHOLD_OLD}d) | ${staleFiles.length} |
| 🔴 High Priority Files | ${priorityFiles.length} |
| 🏷️ Untagged Files | ${untaggedFiles.length} |
`);
// === PRIORITY SECTION ===
if (priorityFiles.length > 0) {
    dv.header(2, "🔴 High Priority Tasks (Action Required)");
    dv.table(
        ["File", "Tasks", "Folder", "Last Modified"],
        priorityFiles
            .sort((a, b) => b.taskCount - a.taskCount)
            .map(f => [
                f.link,
                f.taskCount,
                f.folder || "Root",
                f.modified ? f.modified.toFormat("yyyy-MM-dd") : "—"
            ])
    );
}
// === STALE TASKS SECTION ===
if (staleFiles.length > 0) {
    dv.header(2, `⏰ Stale Files (>${DAYS_THRESHOLD_OLD} days old)`);
    dv.table(
        ["File", "Tasks", "Age (days)", "Tags", "Last Modified"],
        staleFiles
            .sort((a, b) => b.fileAge - a.fileAge)
            .map(f => [
                f.link,
                f.taskCount,
                Math.round(f.fileAge),
                f.tags.length > 0 ? f.tags.slice(0, 2).join(", ") : "❌ None",
                f.modified ? f.modified.toFormat("yyyy-MM-dd") : "—"
            ])
    );
}
// === UNTAGGED SECTION ===
if (untaggedFiles.length > 0) {
    dv.header(2, "🏷️ Untagged Files (Needs Context)");
    dv.table(
        ["File", "Tasks", "Folder"],
        untaggedFiles
            .sort((a, b) => b.taskCount - a.taskCount)
            .slice(0, 10) // Limit to top 10
            .map(f => [
                f.link,
                f.taskCount,
                f.folder || "Root"
            ])
    );
    if (untaggedFiles.length > 10) {
        dv.paragraph(`*… and ${untaggedFiles.length - 10} more untagged files*`);
    }
}
// === COMPREHENSIVE TASK LIST ===
dv.header(2, "📋 All Tasks by File (Sorted by Task Count)");
let sortedFiles = allFiles.sort((a, b) => b.taskCount - a.taskCount);
for (let file of sortedFiles) {
    let indicators = [];
    if (file.hasHighPriority) indicators.push("🔴");
    if (file.isStale) indicators.push("⏰");
    if (file.hasDeadline) indicators.push("📅");
    if (!file.hasContext) indicators.push("🏷️?");
    let indicatorString = indicators.length > 0 ? ` ${indicators.join(" ")}` : "";
    dv.header(3, `${file.name} (${file.taskCount} tasks)${indicatorString}`);
    dv.paragraph(`📂 **Location:** ${file.folder || "Root"} | 🏷️ **Tags:** ${file.tags.length > 0 ? file.tags.join(", ") : "None"}`);
    dv.taskList(file.tasks, false);
}
// === LEGEND ===
dv.header(2, "🔑 Indicator Legend");
dv.paragraph(`
- 🔴 = Contains high-priority tasks
- ⏰ = File is stale (>${DAYS_THRESHOLD_OLD} days old)
- 📅 = Contains tasks with deadlines
- 🏷️? = File lacks tags (needs categorization)
`);
```

```
// Collect all incomplete tasks with enhanced metadata
let tasksByFile = {};
for (let page of dv.pages()) {
    if (!page.file.tasks) continue;
    let incompleteTasks = page.file.tasks.filter(t => !t.completed);
    if (incompleteTasks.length > 0) {
        tasksByFile[page.file.path] = {
            link: page.file.link,
            name: page.file.name,
            folder: page.file.folder,
            tags: page.file.tags || [],
            created: page.file.cday,
            modified: page.file.mtime,
            taskCount: incompleteTasks.length,
            tasks: incompleteTasks,
            // Detect priority indicators
            highPriority: incompleteTasks.some(t =>
                t.text.includes("🔴") ||
                t.text.includes("urgent") ||
                t.text.includes("URGENT") ||
                t.text.includes("high priority")
            )
        };
    }
}
// Sort by task count (most tasks first)
let sortedFiles = Object.values(tasksByFile)
    .sort((a, b) => b.taskCount - a.taskCount);
// Generate output table
dv.header(2, "📊 Task Cleanup Overview");
dv.paragraph(`**Total Files with Tasks:** ${sortedFiles.length} | **Total Tasks:** ${sortedFiles.reduce((sum, f) => sum + f.taskCount, 0)}`);
dv.table(
    ["File", "Folder", "Tasks", "Priority", "Tags", "Last Modified"],
    sortedFiles.map(f => [
        f.link,
        f.folder || "Root",
        f.taskCount,
        f.highPriority ? "🔴 HIGH" : "—",
        f.tags.length > 0 ? f.tags.slice(0, 3).join(", ") : "None",
        f.modified ? f.modified.toFormat("yyyy-MM-dd") : "Unknown"
    ])
);
// Show actual tasks grouped by file
dv.header(2, "📝 Tasks by File");
for (let file of sortedFiles) {
    dv.header(3, `${file.name} (${file.taskCount} tasks)`);
    dv.taskList(file.tasks, false);
}
```

```
TASK
WHERE !completed
GROUP BY file.link
SORT file.name ASC
LIMIT 5
```

```
TASK
WHERE !completed
FLATTEN file.tags as fileTags
FLATTEN file.cday as created
GROUP BY file.link
SORT file.mtime DESC
LIMIT 20
```
`````


### Command Center
````
### 🧩Knowledge Graph Command Center

```yaml
---
tags: #pkm #dashboard #dataview-js #obsidian #meta
aliases: [Cognitive Science Dashboard, PKM Control Panel]
created: 2025-11-22
---
```

> [!abstract]
> **System Overview**
> This dashboard utilizes **DataviewJS** to aggregate data from the `#cognitive-science` and `#pkm` domains. It provides:
>
>   * **Taxonomy Breakdown**: File counts by nested sub-category.
>   * **Freshness Metrics**: Tracking recent modifications.
>   * **Gardening Queue**: Identifying "stub" notes (under 100 words) to develop.

-----

## 📊 Domain Analytics & Taxonomy

This script dynamically renders your nested tag hierarchy, showing you exactly where your focus has been.

```dataviewjs
// ⚙️ CONFIGURATION
const targetTags = ["#cognitive-science", "#pkm"];
const ignoreFolder = "Templates";

// 🧠 LOGIC
// 1. Get all pages that have ANY of our target tags
let pagePool = dv.pages(targetTags.join(" or "))
    .where(p => !p.file.path.includes(ignoreFolder));

let breakdown = [];

targetTags.forEach(rootTag => {
    // 2. Filter pages that belong to this specific root domain
    let domainPages = pagePool.where(p => p.file.tags.some(t => t.startsWith(rootTag)));
    
    // 3. Collect all unique relevant tags
    let allTags = new Set();
    domainPages.forEach(p => {
        p.file.tags.forEach(t => {
            // FIX: We now check if the tag starts with the rootTag (including the #)
            // This ensures #pkm/structure is captured under #pkm
            if (t.startsWith(rootTag)) {
                allTags.add(t);
            }
        });
    });

    // 4. Build the table rows
    if (allTags.size === 0) {
        // Optional: Handle empty states gracefully
    } else {
        Array.from(allTags).sort().forEach(tag => {
            // Count notes with this specific tag
            let count = domainPages.where(p => p.file.tags.includes(tag)).length;
            
            // Calculate depth for indentation (e.g. #pkm = 0, #pkm/structure = 1)
            let depth = tag.split("/").length - 1;
            let indent = "⠀".repeat(depth * 2); 
            
            // Assign status icon based on volume
            let status = count > 10 ? "🌳" : (count > 3 ? "🌱" : "🪹");
            
            breakdown.push([
                `${indent} ${status} **${tag}**`,
                count,
                `<progress value="${count}" max="20"></progress>` 
            ]);
        });
    }
});

// 🎨 RENDER
dv.header(3, "🗂️ Taxonomy Distribution");

if (breakdown.length === 0) {
    dv.paragraph("⚠️ **No tags found.** Make sure you have created at least one note with tags like `#pkm` or `#cognitive-science`.");
} else {
    dv.table(["Domain / Sub-Category", "Note Count", "Density"], breakdown);
}
```

-----

## 🚧 The Incubator (Gardening Queue)

This section uses logic to identify notes that are "Seedlings" (short, atomic concepts) requiring expansion, specifically within your CogSci and PKM domains.

```dataviewjs
// ⚙️ CONFIGURATION
const minWords = 200; 
const limit = 10;
// 🔧 FIX: Access luxon via dv
const luxon = dv.luxon; 

dv.header(3, "🌱 Seedlings Needing Water (Short Notes)");

// Get pages in domain, exclude huge files
const seedlings = dv.pages("#cognitive-science or #pkm")
    .where(p => p.file.size < 10000) 
    .where(p => {
         // Calculate time difference
         const now = luxon.DateTime.now();
         const lastEdit = p.file.mtime;
         // Safety check: if file has no mtime, skip it
         if (!lastEdit) return false; 
         
         const diffDays = now.diff(lastEdit, 'days').days;
         return diffDays > 7; // Show notes not touched in a week
    })
    .sort(p => p.file.mtime, "desc")
    .limit(limit);

if (seedlings.length === 0) {
    dv.paragraph("🌱 All seedlings are well-watered! (No stale short notes found)");
} else {
    dv.table(
        ["Note", "Last Edited", "Link Density"], 
        seedlings.map(p => [
            p.file.link,
            p.file.mtime.toRelative(), 
            p.file.outlinks.length + " 🔗"
        ])
    );
}
```

```dataviewjs
// ⚙️ CONFIGURATION
const minWords = 200; // Notes under this count appear here
const limit = 10; // Max rows to show

dv.header(3, "🌱 Seedlings Needing Water (Short Notes)");

// Get pages in domain, exclude huge files, sort by length ascending
const seedlings = dv.pages("#cognitive-science or #pkm")
    .where(p => p.file.size < 10000) // Quick filter for massive files
    .where(p => {
         // Accurate word count requires reading file content - usually expensive.
         // Instead we rely on file size as proxy or just list recently created.
         // For 'stale' notes (not touched in 30 days):
         const now = luxon.DateTime.now();
         const lastEdit = p.file.mtime;
         const diffDays = now.diff(lastEdit, 'days').days;
         return diffDays > 7; // Show notes not touched in a week
    })
    .sort(p => p.file.mtime, "desc")
    .limit(limit);

dv.table(
    ["Note", "Last Edited", "Link Density"], 
    seedlings.map(p => [
        p.file.link,
        p.file.mtime.toRelative(), 
        p.file.outlinks.length + " 🔗"
    ])
);
```

-----

## 🧠 Active Research Workbench

A view of what you are currently working on (notes edited in the last 3 days).

```dataviewjs
// ⚙️ CONFIGURATION
const daysBack = 3;

dv.header(3, "🔥 Hot Topics (Last 72 Hours)");

// We use dv.luxon directly inside the code to prevent reference errors
const recent = dv.pages("#cognitive-science or #pkm")
    .where(p => {
        // 1. Get the current time using dv.luxon directly
        const now = dv.luxon.DateTime.now();
        
        // 2. Get the file's last modification time
        const lastEdit = p.file.mtime;
        
        // 3. Safety check: ignore files without a date
        if (!lastEdit) return false;
        
        // 4. Compare: Is the file newer than (Now minus 3 days)?
        return lastEdit > now.minus({ days: daysBack });
    })
    .sort(p => p.file.mtime, "desc");

if (recent.length === 0) {
    dv.paragraph("*No active research in these domains recently.*");
} else {
    dv.list(recent.map(p => {
        // Add emoji based on tag
        let icon = p.file.tags.includes("#pkm") ? "🗄️" : "🧠";
        return `${icon} ${p.file.link} (${p.file.mtime.toFormat("h:mm a")})`;
    }));
}
```

## 🔧 Technical Explanation

### How the Scripts Work

1.  **`dv.pages()`**: This is the primary function to fetch file data. We pass the query string `"#cognitive-science or #pkm"` to limit the scope to your specific domains.
2.  **`.where()`**: This acts as a filter using JavaScript arrow functions.
      * Example: `p => !p.file.path.includes("Templates")` filters out any file residing in the Templates folder.
3.  **Visual Logic**:
      * In the **Taxonomy Distribution**, I implemented a visual indentation system (`"⠀".repeat(depth * 2)`) to mimic a folder tree structure inside a flat table.
      * The `<progress>` HTML tag is rendered directly by Obsidian, giving you a visual "density" bar for each topic.

### Customization Guide

> [!tip] **Modify the Variables**
> Look for the `// ⚙️ CONFIGURATION` section at the top of each code block.
>
>   * **Add Tags**: Change `const targetTags = […]` to include other areas like `#philosophy`.
>   * **Adjust Thresholds**: Change `const minWords = 200` to change what you consider a "Seedling" note.

-----

## 🔍 Self-Critique Analysis

### Format Compliance

**Metadata**: [✅ Present] - Includes tiered tags and aliases.
**Code**: [✅ DataviewJS] - Uses advanced JS as requested, not basic SQL-like Dataview.
**Structure**: [✅ Clear Hierarchy] - Separated by function (Analytics vs. Gardening vs. Recents).

### Content Quality

**Depth**: The scripts provide actual utility (taxonomy parsing) rather than just listing files.
**Visualization**: Added HTML progress bars and tree-indentation logic for better UX.
**Performance**: Limited heavy file reads to ensure the dashboard loads quickly.

### Top Improvements

1.  **Word Count limitation**: DataviewJS does not automatically read file content (word count) without async/await operations which can slow down a dashboard. I used **file size** and **edit date** as proxies for performance stability.
2.  **Mobile Compatibility**: The HTML progress bars generally work well on mobile, but the indentation might wrap on very small screens.

-----

**Would you like me to explain how to add a "Random Note Resurfacer" button using the `dv.el` (element) function to encourage Spaced Repetition?**
`````

### Health Dashboard
````
> [!the-purpose] A central control panel to find and fix metadata and structural issues in the vault.

# Section 1: Metadata Integrity

*This section finds notes with* **missing or empty metadata fields**.

## 1.1: Notes Missing Required Fields

*Finds notes* that are *supposed to have a certain field* but **don't**. *This is crucial for data consistency.*

### Projects Missing a 'status'

**Explanation:** This query looks in **all notes tagged** `#project` **OR** in the `Projects/ folder`. The `WHERE !status` line *finds any note in that group that does not have a status field in its frontmatter.*

```
LIST
FROM #project OR "Projects/"
WHERE !status
```

### Sources Missing an 'author'

**Explanation:** Same logic. **Finds all notes tagged** `#source` **OR** in the `Sources/ folder` that are **missing an author field**.

```
LIST
FROM #source OR "Sources/"
WHERE !author
```

## 1.2: Notes with Empty Fields

*Finds notes* that **have a field, but you left it blank** (e.g., `author:`). *This is different from a missing field.*

**Explanation:** The `WHERE author = null` command specifically *finds notes where the* **author key exists**, but **no value** *was provided.* This is a common oversight.

```
LIST
WHERE author = null
```

# Section 2: Content Staleness & Review

This section finds notes that are "outdated" or need your attention.

## 2.1: Stale 'In-Progress' Notes

*Finds notes* that you marked as '**in-progress**' but *haven't actually modified in a long time*. These are your "stuck" projects.

**Explanation:** This finds all notes tagged `#project` where the status is `"in-progress"` AND the file's modification time `file.mtime` is older than 30 days ago. *You can change 30 days to 2 weeks or 6 months to fit your needs.*

```
LIST
FROM #project
WHERE status = "in-progress" AND file.mtime < (date(today) - dur(30 days))
```

## 2.2: Notes Due for Review

*Finds all notes where* you've set a **review-date** that is **today** or in the **past**.

**Explanation:** This is a *simple but powerful query.* It compares the **review-date field against date(today)** *and shows you everything* **that's due**.

```
LIST
WHERE review-date <= date(today)
```

# Section 3: Structural Integrity

This section finds "orphaned" notes and broken links, ensuring your vault is well-connected.

## 3.1: Orphaned Notes

Finds notes that are not linked from any other note. These are "floating" notes with no connections.

**Explanation:** `file.inlinks` is a *list of all notes linking to the* **current note**. `length(file.inlinks) = 0` **finds all notes** *where this list is* **empty.**

**Refinement (Optional):** You might want to **exclude your homepage, MOCs, or daily notes** from this list, as *they are often "starting points" and may have no inlinks*.

```
LIST
WHERE length(file.inlinks) = 0
```

```
LIST
WHERE length(file.inlinks) = 0 AND !contains(file.tags, "#moc") AND file.name != "Homepage"
```

## 3.2: Notes with No Outgoing Links

Finds "**dead-end**" notes. *These notes are easy to get to, but lead nowhere.* They are often unfinished stubs.

**Explanation:** `file.outlinks` is a list of all links in the current note. This query finds all notes where that list is empty.

```
LIST
WHERE length(file.outlinks) = 0
```

# Section 4: Task & Placeholder Cleanup

This section finds stray tasks and placeholder text you may have forgotten.

## 4.1: Stray 'TODO' Placeholders

Finds any note where you wrote "TODO", "TBD", or "TK" (common journalistic placeholder for "To Come") in the body of the note, outside of a formal task.

Explanation: contains(file.content, "…") searches the entire text of every note in your vault for the specified string. This is a "heavy" query, but perfect for a maintenance dashboard.

```
LIST
WHERE contains(file.content, "TBD") OR contains(file.content, "TK") OR contains(file.content, "TODO")
```

## 4.2: All Incomplete Tasks

A simple query to gather all incomplete tasks from your entire vault in one place.

**Explanation:** This uses the TASK query type. It finds all checkboxes `(- [ ])` in your vault and lists them, but only shows the ones that are not completed.

```
TASK
WHERE !completed
```

# Section 5: Tag Consistency

This section is fantastic for cleaning up your tagging system. It finds inconsistencies (e.g., `#book` vs. `#books`).

## 5.1: All Tags and Their Usage Count

This query lists every single tag in your vault and how many times it's used. You will immediately be able to see typos or duplicates.

**Explanation:**
`FROM "":` Gets all notes in the vault.
`FLATTEN file.tags AS tag:` Takes the list of tags on each note (e.g., `[#book, #fiction]`) and creates a new row for each tag.
`GROUP BY tag:` Groups all those new rows by the tag name.
`TABLE length(rows) AS "Count":` Creates a table showing the tag name and how many rows (i.e., notes) are in that group.

```
TABLE length(rows) AS "Count"
FROM ""
FLATTEN file.tags AS tag
GROUP BY tag
SORT length(rows) DESC
Explanation:
```

`````

### Random Dashboard

````
---
title:
aliases:
  - Pur3v4d3r Dashboard
  - Project Dashboard
tags:
  - year/2025
  - source/llm/claude/sonnet
  - pkb
  - cognitive-science
id: "20251118052239"
created: 2025-11-18T05:22:39
week: "[[2025-W47]]"
month: "[[2025-11]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: reference
link-up:
  - 
link-related:
  - "[[2025-11-18|Daily-Note]]"
  - "[[permeant-note_moc]]"
---

---

## 📊 Dataview Query Tools

> [!what-this-does]
> **Automated Reporting for Validation**
> 
> Use these [[dataview]] queries to monitor refactoring progress and identify issues:

### Query 1: Notes Without Proper Tags
```dataview
TABLE file.name AS "Note", file.tags AS "Current Tags"
FROM ""
WHERE !contains(file.tags, "#domain") OR !contains(file.tags, "#type")
SORT file.name ASC
LIMIT 10
```

### Query 2: Notes with Old Naming Pattern
```dataview
LIST
FROM ""
WHERE !contains(file.name, "🆔") OR !contains(file.name, "_")
SORT file.name ASC
LIMIT 10
```

### Query 3: Tag Usage Statistics
```dataview
TABLE length(rows) AS "Count"
FROM ""
FLATTEN file.tags AS tag
GROUP BY tag
SORT length(rows) DESC
LIMIT 35
```

### Query 4: Recent Changes (Monitor Migration Progress)
```dataview
TABLE file.mtime AS "Last Modified"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 20
```

---

```dataview
TABLE length(rows) AS "Usage Count"
FROM ""
FLATTEN file.tags AS tag
GROUP BY tag
SORT length(rows) ASC
LIMIT 50
```
````