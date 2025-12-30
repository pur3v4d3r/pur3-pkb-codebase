---
aliases:
  - "Daily Note Update"
  - "Daily Note"
tags:
  - "type/report"
  - "year/2025"
  - "type/tutorial"
  - "status/in-progress"
  - "pkb"
  - "pkm"
  - "processing-workflow"
  - "cognitive-science/cognitive-load"
  - "metacognitive-pkm"
  - "cognitive-resources"
  - "pkb/optimization"
  - "automation"
  - "cognitive-pkm"
source: "local-llm"
id: "20251212190615"
created: "2025-12-12T19:06:15"
modified: "2025-12-12T19:06:15"
week: "[[2025-W50]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: "reference"
maturity: "needs-review"
confidence: "provisional"
next-review: "2025-12-19"
review-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-12-12|Daily-Note]]"
---

> [!overview] ### <span style='color: #7200ff;'>Overview</span>
> - **Title**: [[Daily Note Components]]
> - **Prompt/Topic Used**: This Out put was produced withoput having added in my metadata.



> [! ] # In-Note Metadata Panel
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
> > **Word Count**: `= this.file.size`| **Est. Read Time**: `= round(this.file.size / 1300) + " min"`
> > **Depth Class**: `= choice(this.file.size < 500, "🌱Stub", choice(this.file.size < 2000, "📄Note", "📜Essay"))`
> ----
> > [!purpose] ### 🕰️Temporal Context
> > **Created**: `= this.file.ctime` | **Age**: `= (date(today) - this.file.ctime).days + " days"`
> > **Last Touch**: `= this.file.mtime` | **Staleness**: `= choice((date(today) - this.file.mtime).days > 180, "🕸️Cobwebs", choice((date(today) - this.file.mtime).days > 30, "🍂Cold", "🔥Fresh"))`
> > **Touch Frequency**: `= choice((date(today) - this.file.mtime).days < 7, "🔥Active", choice((date(today) - this.file.mtime).days < 30, "👌Regular", "❄️Dormant"))`
> ----
> > [!topic-idea] ### 🔗Network Connectivity
> > **In-Links**: `= length(this.file.inlinks)` | **Out-Links**: `= length(this.file.outlinks)`
> > **Network Status**: `= choice(length(this.file.inlinks) = 0, "🕸️Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱Node"))`
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
> WHERE source = "local-llm"
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
> ### 2025-12-12 - Initial Creation
> *Context*: `=this.title` **by**: `=this.source`
> *Maturity*: `= this.maturity`  
> *Confidence*: `= this.confidence`
> 
> ### Tags & Classification
> *Primary Tags*: `= this.tags`  
> *Type*: `= this.type`  
> *Source*: `= this.source`









Metadata






### Daily Note Template Current
```
---
id: "<% tp.date.now("YYYYMMDD-HHmmss") %>"
date: "<% tp.date.now("YYYY-MM-DD") %>"
week: "<% tp.date.now("gggg-[W]WW")%>"
month: "<% tp.date.now("YYYY-MM") %>"
quarter: "<% tp.date.now("YYYY-[Q]Q")%>"
year: "<% tp.date.now("YYYY") %>"
type: "daily"
tags:
  - "daily"
aliases:
  - "<% tp.date.now("dddd, MMMM Do, YYYY") %>"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD", -1,) %>|Yesterday's Daily Note]]"
---
### *Daily Quote's*
>"You are just an impression and not at all the thing you claim to be"
   — Epictetus

> "Men are disturbed not by things, but by the views which they take of things."
>  — Epictetus

# <% tp.date.now("dddd, MMMM Do, YYYY") %>

> [!metrics]
>
> ### Temporal Context
> **Week**: [[<% tp.date.now("gggg-[W]WW", ) %>]]
> **This Week's Theme**:: `Critical Thinking`
> **Monthly Goal**:: `Stoicism`
> **Created**: `= this.file.ctime`
> **Modified**: `= this.file.mtime`
> **Today**: `= date(today)`
> **Tomorrow**: `= date(today) + dur(1 day)`
> **End of Month**: `= date(eom)`
> **Start of Year**: `= date(soy)`
> **Days in Current Month**: `= (date(eom) - date(som)).days`
> **Quarter**: `= "Q" + ceil(date(today).month / 3)`

**Event → Interpretation → Emotional Response**
---
> "By training ourselves to modify assent patterns at Phase Two, we can systematically alter the quality and intensity of emotions experienced at Phase Three."
> —— Claude
> [[psy-report-psychological-mechanisms-underlying-the-efficacy-and-multi-millennial-longevity-of-stoic-techniques-2025112508|Efficacy and Multi Millennial Longevity of Stoic Techniques]]

#### *Full Daily Quote's*
> [!stoic-quote] ### Stoic Quote
>  "Remember that it is not only the desire of having, but also the desire of avoiding, that is subject to our will. Remember that you are a mortal, and one of the parts of a whole. Remember that the nature of the things which you desire is not your own, but foreign. Remember that as soon as an impression [phantasia] arises, say to it: 'You are just an impression and not at all the thing you claim to be.' Then examine it by those rules which you have, and first and chiefly, by this: whether it relates to the things which are in our power, or to those which are not; and, if it relates to anything not in our power, be prepared to say: 'It is nothing to me.'"
>  	—— Epictetus, 
>  	    Discourses [Book II, Chapter 18]

> [!stoic-quote] ### Stoic Quote
> “Men are disturbed not by things, but by the views which they take of things. Thus, death is nothing terrible, else it would have appeared so to Socrates. But the terror consists in our notion of death, that it is terrible. When, therefore, we are hindered, or disturbed, or grieved, let us never impute it to others, but to ourselves; that is, to our own views. It is the action of an uninstructed person to reproach others for his own misfortunes; of one entering upon instruction, to reproach himself; and one perfectly instructed, to reproach neither others nor himself.”
> 	 —— Epictetus, 
> 	    Enchiridion (Handbook), Section V

> [!purpose] ### The One Thing to Remember
> *When something disturbing happens*, ***immediately ask*** "**Is this something I can control or something I cannot control?**" If it's something you cannot control (which includes most of what happens), then struggling against it, resenting it, or being emotionally devastated by it is irrational—you're expending energy trying to change what cannot be changed. Your only rational response is **acceptance** of the fact and **focus** on what remains within your power: how you interpret the event, what meaning you assign it, and what actions you choose to take in response.

> [! ] ### Critical Thinking
> <span style='color: #ff0075;'>Without clear purpose, thinking drifts aimlessly</span>
## <% tp.date.now("dddd, MMMM Do, YYYY") %>'s Plan
### Tasks Overview

#### Main Objective
- [ ] ` `
##### Supporting Tasks
- [ ] ` `
- [ ] ` `

### Task Workbench (Todays-Planning)

- [x] #task Go Grocery Shopping  [priority:: highest]  [repeat:: every week]  [created:: 2025-12-06]  [start:: 2025-12-13]  [due:: 2025-12-13]  [completion:: 2025-12-06]
- [ ] #task Go Grocery Shopping  [priority:: highest]  [repeat:: every week]  [created:: 2025-12-06]  [start:: 2025-12-20]  [due:: 2025-12-20]

---

## Meditations
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
		- [ ] {{PRIORITY TOMORROW HERE}} [scheduled:: <%tp.date.now("YYYY-MM-DD",1)%>] [created:: <% tp.date.now("YYYY-MM-DD")%>]

> [!ask-yourself-this] ### Routine Items
> - [ ] *Work Log*?
> - [ ] *Stoicism*?
> - [ ] *Meditation*?
>
> > [!input-and-instruction]  #### Links to Other Daily Notes.
> > - **Previous Day**: [[<% tp.date.now("YYYY-MM-DD", -1) %>]]
> > - **Next Day**: [[<% tp.date.now("YYYY-MM-DD", 1) %>]]

---

### Tomorrow's Priority

---
# Logs
### Work Log

### Thoughts Log

### Tasks

# Captures
```















## Gemini Pro 3 Output 


## 📋 Daily Note Automation Component Library

### Research Summary
In 2024-2025, the Obsidian community has shifted from static daily templates to **"Active Dashboards"**. The prevailing philosophy is *Interconnectivity*—your daily note shouldn't just be a text file, but a control center that reads and writes data to your entire vault.

**Key trends identified:**
1.  **Interactive Frontmatter**: Using **Meta Bind** to turn YAML properties into clickable buttons, dropdowns, and sliders directly in the note.
2.  **Data Visualization**: Integrating **Charts** with **DataviewJS** to visualize habits (e.g., "Stoic Virtue Adherence") rather than just listing them.
3.  **Task Aggregation**: Moving away from manual checklists to dynamic queries that pull "Overdue" and "Today's Focus" tasks automatically.

**Top Community Use Cases Identified:**
1.  **The "Stoic Compass"**: Tracking virtue practice as data points for weekly review.
2.  **Dynamic Task Workbench**: Auto-populating the "Plan" section with priority items.
3.  **Automated Retrospective**: Auto-filling the "Logs" section with files touched and completed work.

---

### Use Case 1: The "Stoic Compass" (Virtue Tracking)
**Purpose**: Transforms your text-based "Virtue Intention" into trackable data.
**Plugins Used**: Meta Bind, Dataview, Charts.
**Integration Pattern**: Meta Bind writes to frontmatter → Dataview aggregates it → Charts visualizes it.

#### 🟢 BASIC - Inline Virtue Selector
Replace the text "[Which specific virtue will I emphasize today?]" with this input.
```markdown
**Virtue Intention**: INPUT[suggestion(option(Wisdom), option(Justice), option(Courage), option(Temperance)):daily-virtue]
```
**Explanation**: This creates a dropdown menu in your note. Selecting an option automatically updates the `daily-virtue` property in your frontmatter.
**Requirement**: Add `daily-virtue` to your frontmatter properties.

#### 🟡 INTERMEDIATE - Weekly Virtue Context
Add this callout to your "Morning Meditations" to see what you've focused on this week.
```dataview
TABLE daily-virtue as "Focus"
FROM "Daily Notes"
WHERE file.day.weekyear = this.file.day.weekyear AND file.day.year = this.file.day.year
SORT file.day ASC
```
**Explanation**: A standard Dataview table showing the chosen virtue for every day of the current week. Helps ensure you aren't neglecting specific virtues.

#### 🔴 ADVANCED - Monthly Virtue Distribution Chart
Place this in your **Monthly Note** or a separate "Stoic Dashboard" (requires *Obsidian Charts* plugin).
```dataviewjs
/**
 * PURPOSE: Visualizes Virtue distribution for the current month
 * PLUGINS: DataviewJS + Charts
 */
const pages = dv.pages('"Daily Notes"')
    .where(p => p.file.day && p.file.day.month == dv.date("today").month);

const virtues = ["Wisdom", "Justice", "Courage", "Temperance"];
const counts = virtues.map(v => pages.where(p => p["daily-virtue"] == v).length);

const chartData = {
    type: 'doughnut',
    data: {
        labels: virtues,
        datasets: [{
            data: counts,
            backgroundColor: ['#36a2eb', '#ff6384', '#ffcd56', '#4bc0c0'],
            borderWidth: 1
        }]
    }
};

window.renderChart(chartData, this.container);
```
**Synergy Highlight**: This completes the loop. You input data daily via Meta Bind, and this script visualizes your "Stoic Balance" automatically at the end of the month.

---

### Use Case 2: Dynamic Task Workbench
**Purpose**: Replaces the manual "Task Workbench" with a self-updating view of priorities.
**Plugins Used**: Tasks Plugin, DataviewJS.
**Integration Pattern**: Uses Tasks' query engine for simple lists and DataviewJS for logic-heavy grouping.

#### 🟢 BASIC - Today's Focus
Replace your static checkbox list with this query.
```tasks
not done
(due on or before today) OR (scheduled on or before today)
priority is above low
hide backlink
short mode
```
**Explanation**: Automatically pulls any task due today or earlier that isn't low priority. No more copying incomplete tasks forward manually.

#### 🟡 INTERMEDIATE - The "Eisenhower" Split
Separates "Critical" (High Priority) from "Routine" (Normal/Low) tasks.
```dataviewjs
/**
 * PURPOSE: Separates tasks into "Critical" vs "Routine" buckets
 * PLUGINS: DataviewJS
 */
const tasks = dv.pages().file.tasks.where(t => !t.completed && (t.due && t.due <= dv.date("today")));

dv.header(4, "🔥 Critical (Do First)");
dv.taskList(tasks.where(t => t.text.includes("⏫") || t.text.includes("🔼")), false);

dv.header(4, "☕ Routine (Do Later)");
dv.taskList(tasks.where(t => !t.text.includes("⏫") && !t.text.includes("🔼")), false);
```
**Explanation**: Uses DataviewJS to parse task priority emojis (standard in Tasks plugin) and splits them into two visual lists.

#### 💎 COMMUNITY-INSPIRED - "Overdue Rollover" Button
*Inspiration: Creating an active button to "Push" overdue tasks to today.*
```markdown
```meta-bind-button
label: "🗓️ Reschedule Overdue to Today"
icon: "calendar-clock"
action:
  type: "command"
  command: "obsidian-tasks-plugin:edit-task-due-date-to-today"
```
```
**Why This Works**: Instead of seeing a wall of red overdue dates, you click one button to consciously accept and reschedule selected tasks to today. (Requires selecting the task text first, or using the command on a specific line).

---

### Use Case 3: Automated "Retro" (Log Aggregation)
**Purpose**: Fills the "Logs" section with actual activity data instead of relying on memory.
**Plugins Used**: Dataview, QuickAdd (optional).
**Integration Pattern**: Aggregates vault metadata to show *what actually happened*.

#### 🟢 BASIC - Modified Files Log
Place this under your "Work Log" heading.
```dataview
LIST 
FROM ""
WHERE file.mtime >= date(today) AND file.mtime <= date(tomorrow) AND file.name != this.file.name
```
**Explanation**: Lists every file you edited today. Instant context on where you spent your time.

#### 🟡 INTERMEDIATE - Completed Tasks Log
Place this under "Tasks" in the Logs section.
```tasks
done today
hide backlink
group by root
```
**Explanation**: Shows a record of everything checked off today, grouped by the project (folder/file) it belongs to.

#### 🔴 ADVANCED - The "Daily Timeline"
Generates a chronological timeline of your file modifications.
```dataviewjs
/**
 * PURPOSE: Chronological timeline of vault activity
 * PLUGINS: DataviewJS
 */
const files = dv.pages()
    .where(p => p.file.mtime >= dv.date("today"))
    .sort(p => p.file.mtime, "desc");

dv.table(["⏰ Time", "📂 File", "📂 Folder"], 
    files.map(p => [
        p.file.mtime.toFormat("HH:mm"),
        p.file.link,
        p.file.folder
    ])
);
```
**Synergy Highlight**: Combines file metadata with formatting to give you a precise "Audit Trail" of your day at a glance.

---

### 🔧 Implementation Guide

**Step 1: Plugin Configuration**
- **Dataview**: Enable "JavaScript Queries" in settings.
- **Tasks**: Ensure "Global Filter" is set (e.g., `#task`) if you use one.
- **Meta Bind**: No special config needed, just ensure the plugin is active.

**Step 2: Template Integration**
1.  **Backup**: Duplicate your current `Daily Note Template.md`.
2.  **Insert**:
    - Replace the "Task Workbench" checkboxes with the **Use Case 2 (Basic)** code block.
    - Replace the text under "Virtue Intention" with the **Use Case 1 (Basic)** Input.
    - Paste the **Use Case 3 (Basic)** query under "Work Log".
3.  **Frontmatter**: Add the property `daily-virtue: ""` to the YAML header of the template so Meta Bind has a target to write to.

**Step 3: Testing**
1.  Create a new Daily Note.
2.  **Test Input**: Select a virtue from the dropdown. Switch to Source Mode to verify the frontmatter updated.
3.  **Test Query**: Verify the Tasks query shows today's tasks (create a dummy task `#task test due today` if needed).

---

### 🎯 Quick Reference Table

| Use Case | Complexity | Plugins | Primary Benefit |
| :--- | :--- | :--- | :--- |
| **Virtue Selector** | Basic | Meta Bind | Frictionless data entry for habits |
| **Virtue Chart** | Advanced | Charts + Dataview | Visual feedback loop for Stoic practice |
| **Focus Tasks** | Basic | Tasks | Auto-populates daily plan |
| **Priority Split** | Intermediate | DataviewJS | Visual separation of Urgent vs. Routine |
| **Activity Log** | Basic | Dataview | Auto-documents work history |

### 🚀 Next-Level Integration Idea
**The "Stoic Morning Protocol" Button**:
Combine **Meta Bind** and **Templater**. Create a button at the top of your note that says "Start Morning Routine". When clicked, it could:
1.  Open a specific "Morning Stoic Read" note in a split pane.
2.  Insert a specific prompt into your daily note based on the day of the week (e.g., "Seneca Saturday").
3.  Scroll your daily note to the "Meditations" section automatically.














## 📋 Daily Note Automation Component Library

### Research Summary
Recent community trends in Obsidian daily note automation (2024-2025) emphasize multi-plugin synergy for creating emergent capabilities beyond simple sequential workflows. Users are moving away from isolated plugin usage toward integrated systems that leverage metadata, conditional logic, and visualization. Key patterns include using Tasks plugin metadata as input for DataviewJS analytics, combining Templater dynamic content generation with Meta Bind interactive inputs, and creating dashboard-style overviews that synthesize data across time dimensions.

The most successful implementations focus on progressive complexity scaffolding - starting with basic query functionality and layering on visualization, interactivity, and automation. Community members report highest satisfaction with solutions that reduce manual overhead while increasing insight visibility, particularly around task completion patterns, habit tracking, and reflection analysis.

**Top Community Use Cases Identified:**
1. **Task Completion Visualization**: Using Tasks metadata with DataviewJS to generate completion statistics and trend charts
2. **Reflection Pattern Analysis**: Combining Templater-generated prompts with Meta Bind inputs for DataviewJS sentiment/aggregation analysis
3. **Habit Tracking Dashboard**: Integrating Meta Bind daily inputs with Charts visualization for behavioral pattern recognition
4. **Time-Based Goal Alignment**: Leveraging frontmatter temporal properties with Dataview queries for multi-scale objective tracking
5. **Overdue Task Management**: Applying conditional logic with Tasks plugin for automated task rollover and prioritization

---

### Use Case 1: Task Completion Visualization
**Purpose**: Visualize task completion patterns and trends over time using Tasks plugin metadata
**Plugins Used**: Tasks, DataviewJS, Charts
**Integration Pattern**: Tasks metadata → DataviewJS processing → Charts visualization

#### 🟢 BASIC - Today's Task Summary
```dataview
TASK FROM "Daily Notes" 
WHERE file.day = date(today)
```
**Explanation**: This basic query retrieves all tasks from today's daily note using the Tasks plugin's metadata integration with Dataview. It automatically parses task completion status, priority, and other attributes.

**Customization Points**: 
- `"Daily Notes"`: Change to your daily notes folder path
- `date(today)`: Replace with specific date for historical views

#### 🟡 INTERMEDIATE - Weekly Task Completion Rate
```dataviewjs
/**
 * PURPOSE: Calculate and display task completion rates for the current week
 * PLUGINS: DataviewJS + Tasks plugin metadata
 * INTEGRATION: Uses DataviewJS to process Tasks plugin data across multiple files
 */

// Get current week's daily notes
const startDate = dv.date("today").startOf('week');
const endDate = dv.date("today").endOf('week');
const dailyNotes = dv.pages('"Daily Notes"')
  .where(p => p.file.day && p.file.day >= startDate && p.file.day <= endDate)
  .sort(p => p.file.day);

// Calculate completion stats
const stats = dailyNotes.map(p => {
  const tasks = p.file.tasks;
  const completed = tasks.where(t => t.completed).length;
  const total = tasks.length;
  const rate = total > 0 ? Math.round((completed/total)*100) : 0;
  
  return {
    date: p.file.day.toFormat("EEE"),
    completed: completed,
    total: total,
    rate: rate + "%"
  };
});

// Display as table
dv.table(["Day", "Completed", "Total", "Rate"], 
  stats.map(s => [s.date, s.completed, s.total, s.rate])
);
```
**Explanation**: This DataviewJS query analyzes task completion across the current week, calculating daily completion rates and presenting them in a tabular format. It demonstrates how to aggregate data from multiple files using date filtering.

**Integration Notes**: The structured output can be fed directly into the Charts plugin by copying data into chart configuration. For fully automated charting, see the ADVANCED example.

#### 🔴 ADVANCED - Monthly Task Completion Heatmap
```javascript
/**
 * PURPOSE: Generate a heatmap visualization of task completion patterns over the last 30 days
 * PLUGINS: DataviewJS + Tasks + Charts (generates chart syntax)
 * INTEGRATION: Multi-plugin synergy creating emergent visualization capability
 */

// Get all daily notes from the last 30 days
const startDate = dv.date("today").minus(dv.duration("30 days"));
const dailyNotes = dv.pages('"Daily Notes"')
  .where(p => p.file.day && p.file.day >= startDate)
  .sort(p => p.file.day);

// Extract completion data per day
const taskData = dailyNotes.map(p => ({
  date: p.file.day.toFormat("yyyy-MM-dd"),
  completed: p.file.tasks.where(t => t.completed).length,
  total: p.file.tasks.length
}));

// Generate completion rates
const chartData = taskData.map(d => 
  d.total > 0 ? Math.round((d.completed/d.total)*100) : 0
);

// Create chart configuration
const chartConfig = `
\`\`\`chart
type: bar
labels: [${taskData.map(d => `"${d.date.split('-')[2]}"`).join(', ')}]
series:
  - title: Completion Rate (%)
    data: [${chartData.join(', ')}]
xAxisLabel: Day of Month
yAxisLabel: Completion Rate (%)
legend: true
width: 800
height: 300
\`\`\`
`;

// Display chart
dv.paragraph(chartConfig);
```
**Explanation**: This advanced example combines DataviewJS data processing with automated Charts plugin syntax generation to create a visual heatmap of task completion patterns. It processes 30 days of task data and automatically generates the chart configuration.

**Synergy Highlight**: The emergent capability here is automated visualization - the system goes beyond simple data aggregation to create actionable visual insights without manual chart configuration.

#### 💎 COMMUNITY-INSPIRED - Priority-Based Task Distribution
```dataviewjs
/**
 * PURPOSE: Analyze task distribution by priority level with completion insights
 * SOURCE PATTERN: Community pattern from Obsidian forum "Task Priority Analytics" thread
 * WHY THIS WORKS: Leverages Tasks plugin's priority metadata with DataviewJS grouping capabilities
 */

// Get tasks from current week
const startDate = dv.date("today").startOf('week');
const dailyNotes = dv.pages('"Daily Notes"')
  .where(p => p.file.day && p.file.day >= startDate);

// Flatten all tasks and group by priority
const allTasks = dailyNotes.flatMap(p => 
  p.file.tasks.map(t => ({
    task: t,
    priority: t.priority || "normal", // Default to normal if no priority
    completed: t.completed,
    date: p.file.day
  }))
);

// Group by priority level
const priorityGroups = {};
allTasks.forEach(t => {
  if (!priorityGroups[t.priority]) {
    priorityGroups[t.priority] = { total: 0, completed: 0 };
  }
  priorityGroups[t.priority].total++;
  if (t.completed) priorityGroups[t.priority].completed++;
});

// Calculate completion rates
const results = Object.keys(priorityGroups).map(priority => ({
  priority: priority.charAt(0).toUpperCase() + priority.slice(1),
  total: priorityGroups[priority].total,
  completed: priorityGroups[priority].completed,
  rate: Math.round((priorityGroups[priority].completed / priorityGroups[priority].total) * 100) + "%"
}));

// Display results
dv.table(["Priority", "Total Tasks", "Completed", "Completion Rate"], 
  results.map(r => [r.priority, r.total, r.completed, r.rate])
);
```
**Source Pattern**: Inspired by community discussion on Obsidian forum about leveraging Tasks plugin priority metadata for workload analysis
**Why This Works**: This pattern effectively uses the Tasks plugin's built-in priority system to provide workload distribution insights, helping users understand how they're allocating effort across different priority levels.

---

### Use Case 2: Reflection Pattern Analysis
**Purpose**: Track and analyze reflection patterns using Templater prompts and Meta Bind inputs
**Plugins Used**: Templater, Meta Bind, DataviewJS
**Integration Pattern**: Templater dynamic content + Meta Bind inputs → DataviewJS aggregation

#### 🟢 BASIC - Reflection Input Template
```
> [!input-and-instruction] 
#### Today's Virtue Focus
{{INPUT[virtue-focus]}}
#### Key Learning
{{INPUT[key-learning]}}
#### Emotional Challenge
{{INPUT[emotional-challenge]}}
```
**Explanation**: This basic Meta Bind input template creates structured reflection fields that can be tracked over time. The `{{INPUT[field-name]}}` syntax creates interactive input fields in your daily notes.

**Customization Points**: 
- Field names: Change to match your reflection framework
- Styling: Modify callout types and formatting

#### 🟡 INTERMEDIATE - Weekly Reflection Summary
```dataviewjs
/**
 * PURPOSE: Aggregate weekly reflection inputs to identify patterns and themes
 * PLUGINS: DataviewJS + Meta Bind (reading stored inputs)
 * INTEGRATION: Reads Meta Bind stored values and aggregates across time
 */

// Get current week's daily notes
const startDate = dv.date("today").startOf('week');
const endDate = dv.date("today").endOf('week');
const dailyNotes = dv.pages('"Daily Notes"')
  .where(p => p.file.day && p.file.day >= startDate && p.file.day <= endDate)
  .sort(p => p.file.day);

// Extract reflection data
const reflections = dailyNotes.map(p => ({
  date: p.file.day.toFormat("EEE"),
  virtue: p["virtue-focus"] || "Not recorded",
  learning: p["key-learning"] || "Not recorded",
  challenge: p["emotional-challenge"] || "Not recorded"
}));

// Display as table
dv.table(["Day", "Virtue Focus", "Key Learning", "Emotional Challenge"], 
  reflections.map(r => [r.date, r.virtue, r.learning, r.challenge])
);
```
**Explanation**: This DataviewJS query aggregates reflection inputs from Meta Bind fields across the current week, creating a comprehensive view of reflection patterns. It demonstrates how to read stored Meta Bind values programmatically.

**Integration Notes**: Requires consistent use of Meta Bind input fields with standardized names across daily notes. The aggregation provides insights into recurring themes and progress over time.

#### 🔴 ADVANCED - Monthly Reflection Sentiment Analysis
```javascript
/**
 * PURPOSE: Analyze sentiment patterns in reflection inputs over a month
 * PLUGINS: DataviewJS + Meta Bind + Charts (sentiment visualization)
 * INTEGRATION: Multi-plugin synergy for behavioral pattern recognition
 */

// Get last 30 days of reflection data
const startDate = dv.date("today").minus(dv.duration("30 days"));
const dailyNotes = dv.pages('"Daily Notes"')
  .where(p => p.file.day && p.file.day >= startDate)
  .sort(p => p.file.day);

// Simple sentiment scoring (community-inspired heuristic)
function scoreSentiment(text) {
  if (!text) return 0;
  
  const positiveWords = ['good', 'great', 'excellent', 'success', 'achieve', 'progress', 'improve'];
  const negativeWords = ['bad', 'terrible', 'fail', 'struggle', 'difficult', 'challenge', 'problem'];
  
  const lowerText = text.toLowerCase();
  let score = 0;
  
  positiveWords.forEach(word => {
    if (lowerText.includes(word)) score += 1;
  });
  
  negativeWords.forEach(word => {
    if (lowerText.includes(word)) score -= 1;
  });
  
  return score;
}

// Process reflection data
const sentimentData = dailyNotes.map(p => ({
  date: p.file.day.toFormat("MM-dd"),
  challenge: p["emotional-challenge"] || "",
  learning: p["key-learning"] || "",
  sentiment: scoreSentiment(p["emotional-challenge"] || "") + scoreSentiment(p["key-learning"] || "")
}));

// Generate chart data
const dates = sentimentData.map(d => `"${d.date}"`);
const sentiments = sentimentData.map(d => d.sentiment);

// Create sentiment trend chart
const chartConfig = `
\`\`\`chart
type: line
labels: [${dates.join(', ')}]
series:
  - title: Sentiment Score
    data: [${sentiments.join(', ')}]
xAxisLabel: Date
yAxisLabel: Sentiment Score
legend: true
width: 800
height: 300
\`\`\`
`;

// Display chart and summary statistics
dv.paragraph(chartConfig);

// Calculate summary stats
const avgSentiment = sentiments.reduce((a, b) => a + b, 0) / sentiments.length;
const maxSentiment = Math.max(…sentiments);
const minSentiment = Math.min(…sentiments);

dv.paragraph(`
**Sentiment Analysis Summary:**
- Average Sentiment: ${avgSentiment.toFixed(2)}
- Highest Day: ${maxSentiment}
- Lowest Day: ${minSentiment}
`);
```
**Explanation**: This advanced example performs basic sentiment analysis on reflection inputs, visualizing trends over time. It combines DataviewJS data processing with automated chart generation to create behavioral insights.

**Synergy Highlight**: The emergent capability is automated behavioral pattern recognition - the system analyzes qualitative reflection data to identify mood/emotional trends without manual coding.

#### 💎 COMMUNITY-INSPIRED - Reflection Theme Clustering
```dataviewjs
/**
 * PURPOSE: Identify recurring themes in reflection inputs using keyword clustering
 * SOURCE PATTERN: Community pattern from "Digital Stoicism" Obsidian vault
 * WHY THIS WORKS: Leverages natural language processing concepts with simple keyword matching
 */

// Get last 60 days of reflection data
const startDate = dv.date("today").minus(dv.duration("60 days"));
const dailyNotes = dv.pages('"Daily Notes"')
  .where(p => p.file.day && p.file.day >= startDate);

// Define theme keywords (community-curated list)
const themes = {
  "Control & Acceptance": ["control", "accept", "cope", "manage", "handle", "deal"],
  "Virtue Practice": ["virtue", "wisdom", "justice", "courage", "temperance", "integrity"],
  "Relationships": ["friend", "family", "colleague", "relationship", "interact", "social"],
  "Self-Improvement": ["improve", "better", "growth", "develop", "learn", "progress"],
  "Work & Productivity": ["work", "productivity", "focus", "efficiency", "task", "goal"]
};

// Extract all reflection text
const allReflections = dailyNotes.flatMap(p => [
  p["key-learning"] || "",
  p["emotional-challenge"] || "",
  p["virtue-focus"] || ""
]).join(" ").toLowerCase();

// Count theme occurrences
const themeCounts = {};
Object.keys(themes).forEach(theme => {
  themeCounts[theme] = 0;
  themes[theme].forEach(keyword => {
    const matches = (allReflections.match(new RegExp(keyword, "g")) || []).length;
    themeCounts[theme] += matches;
  });
});

// Convert to array and sort by frequency
const sortedThemes = Object.keys(themeCounts)
  .map(theme => ({ theme, count: themeCounts[theme] }))
  .sort((a, b) => b.count - a.count);

// Display results
dv.table(["Theme", "Mentions"], 
  sortedThemes.map(t => [t.theme, t.count])
);
```
**Source Pattern**: Adapted from the "Digital Stoicism" community vault's reflection analysis system
**Why This Works**: This pattern effectively uses simple keyword matching to identify recurring themes in qualitative reflection data, providing insights into focus areas and personal development patterns without requiring complex NLP libraries.

---

### Use Case 3: Habit Tracking Dashboard
**Purpose**: Track and visualize daily habits using Meta Bind inputs with Charts visualization
**Plugins Used**: Meta Bind, Charts, DataviewJS
**Integration Pattern**: Meta Bind inputs + Charts visualization + DataviewJS processing

#### 🟢 BASIC - Habit Tracking Input Fields
```
> [!habit-tracker] 
#### Daily Habits
- Meditation: {{INPUT[meditation::checkbox]}}
- Exercise: {{INPUT[exercise::checkbox]}}
- Journaling: {{INPUT[journaling::checkbox]}}
- Reading: {{INPUT[reading::checkbox]}}
```
**Explanation**: This basic Meta Bind template creates checkbox inputs for daily habit tracking. The `::checkbox` modifier creates interactive checkboxes that store boolean values.

**Customization Points**: 
- Habit names: Customize to match your personal habits
- Input types: Use `::text`, `::number`, or `::select` for different data types

#### 🟡 INTERMEDIATE - Weekly Habit Completion Rate
```dataviewjs
/**
 * PURPOSE: Calculate weekly habit completion rates from Meta Bind checkbox data
 * PLUGINS: DataviewJS + Meta Bind (reading stored checkbox values)
 * INTEGRATION: Processes Meta Bind boolean values to calculate completion statistics
 */

// Get current week's daily notes
const startDate = dv.date("today").startOf('week');
const endDate = dv.date("today").endOf('week');
const dailyNotes = dv.pages('"Daily Notes"')
  .where(p => p.file.day && p.file.day >= startDate && p.file.day <= endDate)
  .sort(p => p.file.day);

// Define habits to track
const habits = ["meditation", "exercise", "journaling", "reading"];

// Calculate completion rates
const habitStats = habits.map(habit => {
  const completions = dailyNotes.filter(p => p[habit] === true).length;
  const rate = Math.round((completions / dailyNotes.length) * 100);
  return {
    habit: habit.charAt(0).toUpperCase() + habit.slice(1),
    completed: completions,
    total: dailyNotes.length,
    rate: rate + "%"
  };
});

// Display results
dv.table(["Habit", "Completed Days", "Total Days", "Completion Rate"], 
  habitStats.map(h => [h.habit, h.completed, h.total, h.rate])
);
```
**Explanation**: This DataviewJS query analyzes habit completion data from Meta Bind checkboxes across the current week, calculating completion rates for each tracked habit.

**Integration Notes**: Requires consistent use of Meta Bind checkbox fields with standardized names. The boolean values are automatically processed to calculate meaningful statistics.

#### 🔴 ADVANCED - Monthly Habit Streak Visualization
```javascript
/**
 * PURPOSE: Visualize habit streaks and consistency patterns over a month
 * PLUGINS: DataviewJS + Meta Bind + Charts (generates streak visualization)
 * INTEGRATION: Multi-plugin synergy for behavioral pattern recognition
 */

// Get last 30 days of habit data
const startDate = dv.date("today").minus(dv.duration("30 days"));
const dailyNotes = dv.pages('"Daily Notes"')
  .where(p => p.file.day && p.file.day >= startDate)
  .sort(p => p.file.day);

// Define habits to track
const habits = ["meditation", "exercise", "journaling", "reading"];

// Process streak data for each habit
habits.forEach(habit => {
  // Create array of completion status (1 for completed, 0 for missed)
  const completionData = dailyNotes.map(p => p[habit] === true ? 1 : 0);
  
  // Generate chart configuration
  const chartConfig = `
\`\`\`chart
type: bar
labels: [${dailyNotes.map((p, i) => i + 1).join(', ')}]
series:
  - title: ${habit.charAt(0).toUpperCase() + habit.slice(1)} Completion
    data: [${completionData.join(', ')}]
xAxisLabel: Day
yAxisLabel: Completed (1) / Missed (0)
legend: false
width: 600
height: 200
\`\`\`
`;
  
  // Display habit name and chart
  dv.header(3, habit.charAt(0).toUpperCase() + habit.slice(1) + " Streak");
  dv.paragraph(chartConfig);
  
  // Calculate current streak
  let currentStreak = 0;
  for (let i = completionData.length - 1; i >= 0; i--) {
    if (completionData[i] === 1) {
      currentStreak++;
    } else {
      break;
    }
  }
  
  // Calculate longest streak
  let longestStreak = 0;
  let tempStreak = 0;
  completionData.forEach(day => {
    if (day === 1) {
      tempStreak++;
      if (tempStreak > longestStreak) longestStreak = tempStreak;
    } else {
      tempStreak = 0;
    }
  });
  
  dv.paragraph(`**Current Streak**: ${currentStreak} days | **Longest Streak**: ${longestStreak} days`);
  dv.paragraph("---");
});
```
**Explanation**: This advanced example creates visual streak charts for each tracked habit, showing completion patterns over the last 30 days. It also calculates and displays current and longest streaks for each habit.

**Synergy Highlight**: The emergent capability is automated behavioral pattern recognition with visual feedback - the system not only tracks habits but provides motivational insights through streak visualization.

#### 💎 COMMUNITY-INSPIRED - Habit Correlation Analysis
```dataviewjs
/**
 * PURPOSE: Analyze correlations between different habits to identify patterns
 * SOURCE PATTERN: Community pattern from "Habit Stacking" Obsidian methodology
 * WHY THIS WORKS: Uses statistical correlation to reveal hidden behavioral relationships
 */

// Get last 90 days of habit data
const startDate = dv.date("today").minus(dv.duration("90 days"));
const dailyNotes = dv.pages('"Daily Notes"')
  .where(p => p.file.day && p.file.day >= startDate && p["meditation"] !== undefined)
  .sort(p => p.file.day);

// Define habits to analyze
const habits = ["meditation", "exercise", "journaling", "reading"];

// Calculate correlation matrix
function calculateCorrelation(habit1, habit2) {
  const data1 = dailyNotes.map(p => p[habit1] === true ? 1 : 0);
  const data2 = dailyNotes.map(p => p[habit2] === true ? 1 : 0);
  
  // Simple correlation calculation
  const n = data1.length;
  let sum1 = 0, sum2 = 0, sum1Sq = 0, sum2Sq = 0, pSum = 0;
  
  for (let i = 0; i < n; i++) {
    sum1 += data1[i];
    sum2 += data2[i];
    sum1Sq += data1[i] * data1[i];
    sum2Sq += data2[i] * data2[i];
    pSum += data1[i] * data2[i];
  }
  
  const num = pSum - (sum1 * sum2 / n);
  const den = Math.sqrt((sum1Sq - sum1 * sum1 / n) * (sum2Sq - sum2 * sum2 / n));
  
  if (den === 0) return 0;
  return num / den;
}

// Generate correlation matrix
const matrix = [];
habits.forEach(habit1 => {
  const row = [habit1.charAt(0).toUpperCase() + habit1.slice(1)];
  habits.forEach(habit2 => {
    if (habit1 === habit2) {
      row.push("1.00");
    } else {
      const corr = calculateCorrelation(habit1, habit2);
      row.push(corr.toFixed(2));
    }
  });
  matrix.push(row);
});

// Add header row
const header = ["Habit"].concat(habits.map(h => h.charAt(0).toUpperCase() + h.slice(1)));
matrix.unshift(header);

// Display correlation matrix
dv.table(header, matrix.slice(1));

// Find strongest correlations
const correlations = [];
for (let i = 0; i < habits.length; i++) {
  for (let j = i + 1; j < habits.length; j++) {
    const corr = calculateCorrelation(habits[i], habits[j]);
    correlations.push({
      habit1: habits[i],
      habit2: habits[j],
      correlation: corr
    });
  }
}

// Sort by correlation strength
correlations.sort((a, b) => Math.abs(b.correlation) - Math.abs(a.correlation));

// Display strongest correlations
dv.header(3, "Strongest Habit Correlations");
dv.list(correlations.slice(0, 5).map(c => 
  `${c.habit1.charAt(0).toUpperCase() + c.habit1.slice(1)} ↔ ${c.habit2.charAt(0).toUpperCase() + c.habit2.slice(1)}: ${c.correlation.toFixed(2)}`
));
```
**Source Pattern**: Inspired by the "Habit Stacking" community methodology for identifying reinforcing behaviors
**Why This Works**: This pattern reveals hidden relationships between habits, helping users understand which behaviors tend to reinforce each other and optimize their habit stack accordingly.

---

### Use Case 4: Time-Based Goal Alignment
**Purpose**: Track progress toward goals using frontmatter temporal properties with Dataview queries
**Plugins Used**: Dataview, Templater
**Integration Pattern**: Frontmatter properties + Dataview queries for contextual dashboards

#### 🟢 BASIC - Weekly Theme Tracker
```dataview
TABLE week, theme
FROM "Daily Notes"
WHERE week = this.week
SORT file.day
```
**Explanation**: This basic Dataview query retrieves all daily notes from the current week and displays their associated themes. It leverages the `week` frontmatter property automatically generated by your Templater template.

**Customization Points**: 
- `"Daily Notes"`: Change to your daily notes folder path
- `week`: Modify to track different temporal properties (month, quarter, etc.)

#### 🟡 INTERMEDIATE - Monthly Goal Progress
```dataviewjs
/**
 * PURPOSE: Track progress toward monthly goals using frontmatter properties
 * PLUGINS: DataviewJS + Templater-generated frontmatter
 * INTEGRATION: Uses DataviewJS to aggregate data from Templater-generated metadata
 */

// Get all daily notes for current month
const currentMonth = dv.date("today").toFormat("yyyy-MM");
const dailyNotes = dv.pages('"Daily Notes"')
  .where(p => p.file.day && p.file.day.toFormat("yyyy-MM") === currentMonth)
  .sort(p => p.file.day);

// Extract unique monthly goals
const monthlyGoals = […new Set(dailyNotes.map(p => p.monthlygoal || p["Monthly Goal"] || "Not specified"))];

// For each goal, calculate progress
monthlyGoals.forEach(goal => {
  if (goal === "Not specified") return;
  
  const goalNotes = dailyNotes.filter(p => 
    (p.monthlygoal || p["Monthly Goal"]) === goal
  );
  
  const totalDays = goalNotes.length;
  const daysWithProgress = goalNotes.filter(p => 
    p["key-learning"] || p["emotional-challenge"] || p.meditation === true
  ).length;
  
  const progress = Math.round((daysWithProgress / totalDays) * 100);
  
  dv.header(3, goal);
  dv.paragraph(`Progress: ${progress}% (${daysWithProgress}/${totalDays} days with activity)`);
});
```
**Explanation**: This DataviewJS query analyzes monthly goal progress by examining activity levels in daily notes associated with each goal. It demonstrates how to use Templater-generated frontmatter for goal tracking.

**Integration Notes**: Requires consistent use of monthly goal frontmatter properties. The progress calculation is based on the presence of reflection or habit data as indicators of goal engagement.

#### 🔴 ADVANCED - Quarterly Objective Dashboard
```javascript
/**
 * PURPOSE: Create a comprehensive dashboard for tracking quarterly objectives
 * PLUGINS: DataviewJS + Templater + Charts (multi-dimensional goal tracking)
 * INTEGRATION: Multi-plugin synergy for strategic objective visualization
 */

// Get all daily notes for current quarter
const currentQuarter = "Q" + Math.ceil((dv.date("today").month + 1) / 3);
const currentYear = dv.date("today").year;
const quarterStart = dv.date(`${currentYear}-0${(Math.ceil((dv.date("today").month + 1) / 3) - 1) * 3 + 1}-01`);
const quarterEnd = quarterStart.plus({ months: 3 }).minus({ days: 1 });

const dailyNotes = dv.pages('"Daily Notes"')
  .where(p => p.file.day && p.file.day >= quarterStart && p.file.day <= quarterEnd)
  .sort(p => p.file.day);

// Define quarterly objectives (from frontmatter or manual list)
const objectives = [
  { name: "Stoicism Practice", key: "stoicism-practice" },
  { name: "Critical Thinking Development", key: "critical-thinking" },
  { name: "Physical Health", key: "physical-health" },
  { name: "Professional Growth", key: "professional-growth" }
];

// Create dashboard header
dv.header(2, `Q${Math.ceil((dv.date("today").month + 1) / 3)} ${currentYear} Objectives Dashboard`);

// Process each objective
objectives.forEach(obj => {
  dv.header(3, obj.name);
  
  // Filter notes related to this objective
  const objNotes = dailyNotes.filter(p => 
    (p[obj.key] === true) || 
    (p.theme && p.theme.toLowerCase().includes(obj.key.split('-')[0])) ||
    (p["Monthly Goal"] && p["Monthly Goal"].toLowerCase().includes(obj.key.split('-')[0]))
  );
  
  const totalDays = dailyNotes.length;
  const activeDays = objNotes.length;
  const progress = Math.round((activeDays / totalDays) * 100);
  
  // Create progress visualization
  const progressBar = "█".repeat(Math.floor(progress / 5)) + "░".repeat(20 - Math.floor(progress / 5));
  
  dv.paragraph(`${progressBar} ${progress}%`);
  dv.paragraph(`Active on ${activeDays} of ${totalDays} days`);
  
  // Show recent activity
  if (objNotes.length > 0) {
    const recentNotes = objNotes.slice(-3);
    dv.paragraph("**Recent Activity:**");
    dv.list(recentNotes.map(p => 
      `${p.file.day.toFormat("MM/dd")}: ${p["key-learning"] || "No learning recorded"}`
    ));
  }
  
  dv.paragraph("---");
});
```
**Explanation**: This advanced example creates a comprehensive dashboard for tracking quarterly objectives, combining data from multiple frontmatter properties and recent activity to provide strategic insights.

**Synergy Highlight**: The emergent capability is multi-dimensional goal tracking that synthesizes temporal metadata, thematic content, and activity patterns into a single strategic overview.

#### 💎 COMMUNITY-INSPIRED - Annual Progress Visualization
```dataviewjs
/**
 * PURPOSE: Visualize annual progress toward major life objectives
 * SOURCE PATTERN: Community pattern from "Yearly Planning" Obsidian workflow
 * WHY THIS WORKS: Uses calendar-based visualization to make long-term progress tangible
 */

// Get all daily notes for current year
const currentYear = dv.date("today").year;
const startDate = dv.date(`${currentYear}-01-01`);
const endDate = dv.date(`${currentYear}-12-31`);

const dailyNotes = dv.pages('"Daily Notes"')
  .where(p => p.file.day && p.file.day.year === currentYear)
  .sort(p => p.file.day);

// Define annual objectives
const annualObjectives = [
  { name: "Philosophy Practice", key: "stoicism" },
  { name: "Health & Fitness", key: "health" },
  { name: "Learning & Growth", key: "learning" },
  { name: "Relationships", key: "relationships" }
];

// Create calendar visualization
dv.header(2, `${currentYear} Progress Calendar`);

annualObjectives.forEach(obj => {
  dv.header(3, obj.name);
  
  // Create month-by-month visualization
  const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  
  let calendar = "| Month | Progress |\n|-------|----------|\n";
  
  months.forEach((month, index) => {
    const monthStart = dv.date(`${currentYear}-${String(index + 1).padStart(2, '0')}-01`);
    const monthEnd = monthStart.endOf('month');
    
    const monthNotes = dailyNotes.filter(p => 
      p.file.day >= monthStart && p.file.day <= monthEnd
    );
    
    const activeNotes = monthNotes.filter(p => 
      (p[obj.key] === true) || 
      (p.theme && p.theme.toLowerCase().includes(obj.key)) ||
      (p["Monthly Goal"] && p["Monthly Goal"].toLowerCase().includes(obj.key))
    );
    
    const progress = monthNotes.length > 0 ? 
      Math.round((activeNotes.length / monthNotes.length) * 100) : 0;
    
    // Create visual bar
    const bar = "█".repeat(Math.floor(progress / 10));
    
    calendar += `| ${month} | ${bar} ${progress}% |\n`;
  });
  
  dv.paragraph(calendar);
});
```
**Source Pattern**: Adapted from the community's "Yearly Planning" workflow that emphasizes visual progress tracking
**Why This Works**: This pattern makes long-term progress tangible through calendar-based visualization, helping users maintain motivation and identify seasonal patterns in their objective pursuit.

---

### Use Case 5: Overdue Task Management
**Purpose**: Automatically identify and manage overdue tasks using Tasks plugin conditional logic
**Plugins Used**: Tasks, DataviewJS
**Integration Pattern**: Conditional logic + Tasks plugin for automated task workflows

#### 🟢 BASIC - Overdue Task List
```dataview
TASK FROM "Daily Notes" 
WHERE !completed AND due < date(today)
SORT due ASC
```
**Explanation**: This basic query retrieves all overdue tasks (not completed and due date before today) from daily notes, sorted by due date. It leverages the Tasks plugin's metadata integration with Dataview.

**Customization Points**: 
- `"Daily Notes"`: Change to your daily notes folder path
- Sorting: Modify to prioritize by different criteria (priority, creation date, etc.)

#### 🟡 INTERMEDIATE - Smart Overdue Task Rollover
```dataviewjs
/**
 * PURPOSE: Automatically identify overdue tasks and suggest rollover actions
 * PLUGINS: DataviewJS + Tasks plugin metadata
 * INTEGRATION: Uses conditional logic to process overdue tasks intelligently
 */

// Get all overdue tasks
const overdueTasks = dv.pages('"Daily Notes"').file.tasks
  .where(t => !t.completed && t.due && t.due < dv.date("today"))
  .sort(t => t.due, 'asc');

// Group by priority for handling suggestions
const priority… (The response was truncated because it has reached the token limit. Try to increase the token limit if you need a longer response.)

























































# QWEN NOT METaDATa

## 📋 Daily Note Automation Component Library

### Research Summary
Based on current Obsidian community practices (2024-2025), daily notes have evolved beyond simple journaling to become comprehensive personal operating systems. The most effective implementations leverage plugin synergies to create emergent capabilities:

1. **Task Orchestration**: Combining Tasks plugin with Dataview filtering and Meta Bind interactive controls creates dynamic task management dashboards that adapt to context and priority.

2. **Activity Intelligence**: DataviewJS queries of file metadata combined with Charts visualization provide powerful insights into work patterns and knowledge base evolution.

3. **Habit Formation Systems**: Meta Bind input fields integrated with Templater persistence and Charts tracking create comprehensive behavior modification tools.

4. **Temporal Navigation**: Periodic Notes integration with Homepage plugin and Dataview queries enables seamless temporal browsing and review workflows.

5. **Data Visualization Pipelines**: Multi-plugin workflows that pipe data from Tasks → DataviewJS → Charts create automated reporting dashboards.

**Top Community Use Cases Identified:**
1. **Task Management Dashboard**: Interactive task filtering and visualization using Tasks + Dataview + Meta Bind
2. **Recent Activity Tracker**: Automated display of recently modified notes using Dataview metadata queries
3. **Habit Monitoring System**: Interactive habit tracking with visualization using Meta Bind + Charts
4. **Daily Schedule Overview**: Calendar integration and event visualization using Dataview + Tasks
5. **Progress Visualization**: Automated charts showing completion rates using DataviewJS + Charts

---

### Use Case 1: Task Management Dashboard
**Purpose**: Create an interactive dashboard for managing today's tasks with filtering and statistics
**Plugins Used**: Tasks, Dataview, DataviewJS, Meta Bind
**Integration Pattern**: Tasks provides task data, Dataview displays filtered views, Meta Bind adds interactivity, DataviewJS calculates statistics

#### 🟢 BASIC - Today's Tasks Overview
```cs
TASK
FROM "Daily Notes" 
WHERE file.day = date(today)
SORT priority DESC
```
**Explanation**: This basic query displays all tasks from today's daily note, sorted by priority. It uses the Tasks plugin's native integration with Dataview to automatically parse and display tasks.

**Customization Points**: 
- `"Daily Notes"`: Change to your daily notes folder path
- `date(today)`: Can be modified to `date(yesterday)` or `date(tomorrow)`
- `priority`: Sort by other task properties like `due`, `created`, or `completed`

#### 🟡 INTERMEDIATE - Filterable Task Dashboard
```cs
/**
 * PURPOSE: Create a filterable task dashboard with completion statistics
 * PLUGINS: Tasks + DataviewJS + Meta Bind (for filter controls)
 * INTEGRATION: DataviewJS processes Tasks data, calculates stats, formats output
 */

// Get today's tasks from the current daily note
const todayNote = dv.current();
const allTasks = todayNote.file.tasks;
const completedTasks = allTasks.where(t => t.completed);
const incompleteTasks = allTasks.where(t => !t.completed);

// Display statistics
dv.paragraph(`**Task Summary**: ${allTasks.length} total | ${completedTasks.length} completed | ${incompleteTasks.length} remaining`);

// Display incomplete tasks grouped by priority
dv.header(3, "High Priority Tasks");
dv.taskList(incompleteTasks.where(t => t.priority == "high"));

dv.header(3, "Medium Priority Tasks");
dv.taskList(incompleteTasks.where(t => t.priority == "medium"));

dv.header(3, "Low Priority Tasks");
dv.taskList(incompleteTasks.where(t => t.priority == "low"));

// Display recently completed tasks
dv.header(3, "Recently Completed");
dv.taskList(completedTasks.sort(t => t.completion, 'desc').limit(5));
```
**Explanation**: This DataviewJS script creates a comprehensive task dashboard that shows task statistics, groups incomplete tasks by priority, and displays recently completed tasks. It leverages the Tasks plugin's metadata to access task properties.

**Integration Notes**: To make this truly interactive, pair with Meta Bind input fields for dynamic filtering. The script can be modified to read filter values from Meta Bind properties.

#### 🔴 ADVANCED - Interactive Priority Matrix
```
/**
 * PURPOSE: Create an Eisenhower Matrix-style task visualization with interactive filtering
 * PLUGINS: Tasks + DataviewJS + Meta Bind + Charts
 * SYNERGY: Combines task metadata, interactive controls, and visualization
 */

// Eisenhower Matrix quadrants based on urgency and importance
function categorizeTask(task) {
  const isUrgent = task.due && task.due <= dv.date("today").plus(dv.duration("2 days"));
  const isImportant = task.priority === "high" || task.tags.includes("#important");
  
  if (isUrgent && isImportant) return "Do First";
  if (!isUrgent && isImportant) return "Schedule";
  if (isUrgent && !isImportant) return "Delegate";
  return "Eliminate";
}

// Get tasks and categorize them
const todayNote = dv.current();
const tasks = todayNote.file.tasks.where(t => !t.completed);
const matrix = {
  "Do First": [],
  "Schedule": [],
  "Delegate": [],
  "Eliminate": []
};

tasks.forEach(task => {
  const quadrant = categorizeTask(task);
  matrix[quadrant].push(task);
});

// Display matrix as tables
for (const [quadrant, quadrantTasks] of Object.entries(matrix)) {
  if (quadrantTasks.length > 0) {
    dv.header(3, `${quadrant} (${quadrantTasks.length})`);
    dv.taskList(quadrantTasks);
  }
}

// Generate completion stats for Charts plugin
const completedToday = todayNote.file.tasks.where(t => 
  t.completed && t.completion.toFormat("yyyy-MM-dd") === dv.date("today").toFormat("yyyy-MM-dd")
).length;

const completionRate = todayNote.file.tasks.length > 0 ? 
  Math.round((completedToday / todayNote.file.tasks.length) * 100) : 0;

// Output data for charting (can be piped to Charts plugin)
dv.paragraph(`Completion Data: ${completionRate}%|${completedToday}|${todayNote.file.tasks.length - completedToday}`);
```
**Explanation**: This advanced script creates an Eisenhower Matrix visualization by analyzing task urgency (based on due dates) and importance (based on priority and tags). It categorizes tasks into four quadrants and displays them accordingly.

**Synergy Highlight**: The script demonstrates emergent capability by combining:
- Tasks plugin metadata (priority, due dates, tags)
- DataviewJS logic processing
- Structured output for Charts plugin integration
- Dynamic categorization based on multiple criteria

#### 💎 COMMUNITY-INSPIRED - Smart Task Rollover System
```cs
/**
 * PURPOSE: Automatically identify and suggest tasks for rollover to tomorrow
 * COMMUNITY PATTERN: Inspired by "Progressive Summarization" approach to task management
 * INTEGRATION: Tasks + DataviewJS + Templater (for tomorrow's note generation)
 */

// Get today's incomplete tasks
const todayNote = dv.current();
const incompleteTasks = todayNote.file.tasks.where(t => !t.completed);

// Categorize tasks for rollover decisions
const rolloverCandidates = incompleteTasks.filter(task => {
  // Roll over tasks that are:
  // 1. High priority
  // 2. Have near-term due dates
  // 3. Were created recently (still relevant)
  
  const isHighPriority = task.priority === "high";
  const isDueSoon = task.due && task.due <= dv.date("today").plus(dv.duration("3 days"));
  const isRecent = task.created && task.created >= dv.date("today").minus(dv.duration("7 days"));
  
  return isHighPriority || isDueSoon || isRecent;
});

// Display rollover suggestions
if (rolloverCandidates.length > 0) {
  dv.header(3, "📋 Suggested Tasks for Tomorrow");
  dv.paragraph("*These tasks are recommended for rollover based on priority, due dates, and recency*");
  
  // Create suggested tasks for tomorrow (without completion status)
  const suggestedTasks = rolloverCandidates.map(task => {
    let taskText = `- [ ] ${task.text}`;
    if (task.due) taskText += ` 📅 ${task.due.toFormat("yyyy-MM-dd")}`;
    if (task.priority) taskText += ` ${'🔺'.repeat(task.priority === 'high' ? 1 : task.priority === 'medium' ? 1 : 0)}`;
    if (task.tags.length > 0) taskText += ` ${task.tags.join(' ')}`;
    return taskText;
  });
  
  dv.list(suggestedTasks);
  
  // Generate Templater code for automatic rollover
  dv.paragraph(`
**To automatically rollover these tasks:**
1. Copy the tasks above
2. Paste into tomorrow's daily note
3. Or use this Templater snippet:
\`\`\`javascript
<%*
const tasks = \`\${suggestedTasks.join('\\n')}\`;
tR += tasks;
%>\`\`\`
  `);
}
```
**Source Pattern**: Community pattern from "Smart Task Management" workflows that use machine learning concepts for task prioritization
**Why This Works**: This approach goes beyond simple "incomplete task" rollover by applying intelligent filtering based on multiple factors, reducing decision fatigue while maintaining focus on important work.

---

### Use Case 2: Recent Activity Tracker
**Purpose**: Automatically display recently created or modified notes to maintain awareness of knowledge base activity
**Plugins Used**: Dataview, DataviewJS
**Integration Pattern**: Dataview metadata queries combined with time-based filtering and sorting

#### 🟢 BASIC - Recently Modified Notes
```cs
TABLE file.mtime as "Modified", file.ctime as "Created"
FROM ""
WHERE file.folder != ".obsidian" AND file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 10
```
**Explanation**: This query displays the 10 most recently modified files in your vault (excluding Obsidian system files), showing both modification and creation times, sorted by most recent first.

**Customization Points**:
- `dur(7 days)`: Adjust timeframe (e.g., `dur(1 day)`, `dur(30 days)`)
- `LIMIT 10`: Change number of results displayed
- `file.folder != ".obsidian"`: Add additional folder exclusions as needed

#### 🟡 INTERMEDIATE - Activity Heatmap
```cs
/**
 * PURPOSE: Visualize editing activity patterns over the last week
 * PLUGINS: DataviewJS (primary) + Charts (data preparation)
 * INTEGRATION: Process file metadata to create time-based activity insights
 */

// Get files modified in the last 7 days
const startDate = dv.date("today").minus(dv.duration("7 days"));
const recentFiles = dv.pages("")
  .where(p => p.file.mtime && p.file.mtime >= startDate && p.file.folder !== ".obsidian")
  .sort(p => p.file.mtime, 'desc');

// Group by day and count modifications
const activityByDay = {};
for (let i = 0; i < 7; i++) {
  const day = dv.date("today").minus(dv.duration(`${i} days`));
  const dayKey = day.toFormat("yyyy-MM-dd");
  activityByDay[dayKey] = 0;
}

recentFiles.forEach(file => {
  const dayKey = file.file.mtime.toFormat("yyyy-MM-dd");
  if (activityByDay.hasOwnProperty(dayKey)) {
    activityByDay[dayKey]++;
  }
});

// Prepare data for display
const days = Object.keys(activityByDay).reverse();
const counts = days.map(day => activityByDay[day]);

// Display as table
dv.table(
  ["Date", "Activity Count"],
  days.map((day, index) => [day, counts[index]])
);

// Output formatted data for Charts plugin
dv.paragraph(`**Chart Data**: ${JSON.stringify({labels: days, data: counts})}`);
```
**Explanation**: This DataviewJS script creates an activity heatmap by counting file modifications per day over the last week. It groups files by modification date and prepares data for visualization.

**Integration Notes**: The script outputs formatted data that can be directly used with the Charts plugin. The structured approach makes it easy to create bar charts or line graphs showing activity trends.

#### 🔴 ADVANCED - Intelligent Activity Digest
```cs
/**
 * PURPOSE: Create a smart digest of recent activity with categorization and insights
 * PLUGINS: DataviewJS + file metadata analysis + content categorization
 * SYNERGY: Combines metadata analysis with content-based categorization
 */

// Get recent activity (last 3 days)
const startDate = dv.date("today").minus(dv.duration("3 days"));
const recentFiles = dv.pages("")
  .where(p => 
    p.file.mtime && 
    p.file.mtime >= startDate && 
    p.file.folder !== ".obsidian" &&
    p.file.name !== dv.current().file.name
  )
  .sort(p => p.file.mtime, 'desc');

// Categorize files by content type
function categorizeFile(file) {
  // Check for task-related files
  if (file.file.tasks && file.file.tasks.length > 0) return "Task Management";
  
  // Check for meeting notes (common patterns)
  if (file.file.name.toLowerCase().includes("meeting") || 
      file.file.name.toLowerCase().includes("sync") ||
      file.tags.includes("#meeting")) return "Meetings";
  
  // Check for project files
  if (file.tags.includes("#project") || 
      file.tags.includes("#work") ||
      file.file.folder.includes("Projects")) return "Projects";
  
  // Check for learning/content files
  if (file.tags.includes("#learning") || 
      file.tags.includes("#book") ||
      file.tags.includes("#article")) return "Learning";
  
  // Default category
  return "General";
}

// Group files by category
const categories = {};
recentFiles.forEach(file => {
  const category = categorizeFile(file);
  if (!categories[category]) categories[category] = [];
  categories[category].push(file);
});

// Display categorized activity
dv.header(2, "Recent Activity Digest");
dv.paragraph(`*${recentFiles.length} files modified in the last 3 days*`);

for (const [category, files] of Object.entries(categories)) {
  if (files.length > 0) {
    dv.header(3, `${category} (${files.length})`);
    dv.list(files.slice(0, 5).map(f => 
      `${f.file.link} (${f.file.mtime.toFormat("hh:mm a")})`
    ));
  }
}

// Highlight most significant changes
const largestChanges = recentFiles
  .sort((a, b) => b.file.size - a.file.size)
  .slice(0, 3);

if (largestChanges.length > 0) {
  dv.header(3, "Significant Updates");
  dv.paragraph("*Files with the largest content changes*");
  dv.list(largestChanges.map(f => 
    `${f.file.link} (+${Math.round(f.file.size/1024)}KB)`
  ));
}
```
**Explanation**: This advanced script creates an intelligent activity digest by categorizing recent files based on content analysis. It groups files by type (tasks, meetings, projects, etc.) and highlights significant changes based on file size differences.

**Synergy Highlight**: The script demonstrates emergent capability by combining:
- File metadata analysis (modification time, size)
- Content-based categorization (tags, filenames, folder structure)
- Intelligent sorting and highlighting
- Structured presentation for quick scanning

#### 💎 COMMUNITY-INSPIRED - Collaborative Activity Tracker
```cs
/**
 * PURPOSE: Track activity across multiple authors/contributors in a shared vault
 * COMMUNITY PATTERN: Inspired by team knowledge management workflows
 * INTEGRATION: File metadata + frontmatter analysis for contributor tracking
 */

// Get recent activity from all contributors
const startDate = dv.date("today").minus(dv.duration("7 days"));
const recentFiles = dv.pages("")
  .where(p => 
    p.file.mtime && 
    p.file.mtime >= startDate && 
    p.file.folder !== ".obsidian" &&
    p.file.name !== dv.current().file.name
  )
  .sort(p => p.file.mtime, 'desc');

// Extract contributor information (assuming frontmatter contains 'author' field)
const contributorActivity = {};

recentFiles.forEach(file => {
  // Default to file modifier if no author specified
  const contributor = file.author || file.file.frontmatter?.author || "Unknown";
  
  if (!contributorActivity[contributor]) {
    contributorActivity[contributor] = {
      files: 0,
      totalSize: 0,
      lastActivity: file.file.mtime,
      fileLinks: []
    };
  }
  
  contributorActivity[contributor].files++;
  contributorActivity[contributor].totalSize += file.file.size;
  if (file.file.mtime > contributorActivity[contributor].lastActivity) {
    contributorActivity[contributor].lastActivity = file.file.mtime;
  }
  if (contributorActivity[contributor].fileLinks.length < 5) {
    contributorActivity[contributor].fileLinks.push(file.file.link);
  }
});

// Display contributor leaderboard
dv.header(2, "Contributor Activity (Last 7 Days)");

const sortedContributors = Object.entries(contributorActivity)
  .sort(([,a], [,b]) => b.files - a.files);

dv.table(
  ["Contributor", "Files Modified", "Total Size", "Last Active", "Recent Files"],
  sortedContributors.map(([name, data]) => [
    name,
    data.files,
    `${Math.round(data.totalSize/1024)}KB`,
    data.lastActivity.toFormat("yyyy-MM-dd"),
    data.fileLinks
  ])
);

// Generate team activity summary
const totalFiles = sortedContributors.reduce((sum, [,data]) => sum + data.files, 0);
const activeContributors = sortedContributors.length;
dv.paragraph(`**Team Summary**: ${activeContributors} contributors modified ${totalFiles} files this week`);
```
**Source Pattern**: Community pattern from shared vault management workflows, particularly popular in team knowledge bases
**Why This Works**: This approach leverages frontmatter metadata to track contributions across team members, providing valuable insights for collaborative environments while maintaining individual privacy through optional author fields.

---

### Use Case 3: Habit Monitoring System
**Purpose**: Track daily habits with interactive input controls and visualization
**Plugins Used**: Meta Bind, Charts, Templater, DataviewJS
**Integration Pattern**: Meta Bind for data input, Templater for persistence, DataviewJS for aggregation, Charts for visualization

#### 🟢 BASIC - Simple Habit Tracker
```cs
**Today's Habits**:
- [ ] Exercise 🔸
- [ ] Read 30 minutes 🔸
- [ ] Journal 🔸
- [ ] Meditate 🔸
```
**Explanation**: This basic habit tracker uses standard markdown checkboxes with visual indicators. While simple, it provides immediate feedback on daily progress.

**Customization Points**:
- Add/remove habits based on personal goals
- Change visual indicators (🔸, ⭐, ✅, etc.)
- Add due dates or time constraints using Tasks plugin syntax

#### 🟡 INTERMEDIATE - Interactive Habit Dashboard
```cs
**🎯 Habit Tracker**

**Physical Health**:
INPUT[toggle:title(Exercise):value([[Habits#Exercise]])]
INPUT[toggle:title(Morning Stretch):value([[Habits#Stretch]])]

**Mental Wellness**:
INPUT[toggle:title(Meditate):value([[Habits#Meditate]])]
INPUT[toggle:title(Journal):value([[Habits#Journal]])]

**Learning & Growth**:
INPUT[toggle:title(Read 30 min):value([[Habits#Reading]])]
INPUT[toggle:title(Skill Practice):value([[Habits#Practice]])]

**Tracking Notes**:
INPUT[textArea:title(Reflection):class(editor):placeholder(What went well? What could be improved?)]
```
**Explanation**: This intermediate habit tracker uses Meta Bind input fields to create interactive toggles that can persist data across sessions. Each toggle is linked to a specific location in a Habits note for long-term tracking.

**Integration Notes**: 
- Requires Meta Bind plugin with proper configuration
- Links to a central Habits note for data persistence
- Includes text area for qualitative reflection
- Can be enhanced with Templater for automatic date stamping

#### 🔴 ADVANCED - Comprehensive Habit Monitoring System
```cs
/**
 * PURPOSE: Create a full habit tracking system with visualization and streak tracking
 * PLUGINS: Meta Bind + DataviewJS + Charts + Templater
 * SYNERGY: Combines interactive input, data aggregation, visualization, and automation
 */

// Configuration
const HABIT_TRACKER_NOTE = "Habits/Tracking"; // Central habit tracking note
const HABITS = [
  { id: "exercise", name: "Exercise", icon: "💪" },
  { id: "meditate", name: "Meditate", icon: "🧘" },
  { id: "read", name: "Read 30min", icon: "📚" },
  { id: "journal", name: "Journal", icon: "✍️" },
  { id: "sleep", name: "Good Sleep", icon: "😴" }
];

// Generate today's habit tracking interface
dv.header(2, "🎯 Daily Habit Tracker");

HABITS.forEach(habit => {
  dv.paragraph(`
**${habit.icon} ${habit.name}**:
INPUT[toggle:title(Completed):value([[${HABIT_TRACKER_NOTE}#${habit.id}-${dv.date('today').toFormat('yyyy-MM-dd')}]])]
  `);
});

// Calculate streaks and statistics
const habitData = dv.page(HABIT_TRACKER_NOTE);
if (habitData) {
  dv.header(3, "📊 Progress Overview");
  
  const streaks = {};
  const weeklyData = {};
  
  HABITS.forEach(habit => {
    // Calculate current streak (simplified - would need more complex logic in practice)
    const todayKey = `${habit.id}-${dv.date('today').toFormat('yyyy-MM-dd')}`;
    const completed = habitData[todayKey] || false;
    streaks[habit.name] = completed ? "✅ Today" : "❌ Missed";
    
    // Weekly completion (last 7 days)
    let weeklyCount = 0;
    for (let i = 0; i < 7; i++) {
      const dateKey = dv.date('today').minus(dv.duration(`${i} days`)).toFormat('yyyy-MM-dd');
      const habitKey = `${habit.id}-${dateKey}`;
      if (habitData[habitKey]) weeklyCount++;
    }
    weeklyData[habit.name] = `${weeklyCount}/7 days`;
  });
  
  dv.table(
    ["Habit", "Today", "This Week"],
    HABITS.map(habit => [
      `${habit.icon} ${habit.name}`,
      streaks[habit.name],
      weeklyData[habit.name]
    ])
  );
  
  // Generate chart data for weekly overview
  const labels = HABITS.map(h => h.name);
  const data = HABITS.map(habit => {
    const count = parseInt(weeklyData[habit.name].split('/')[0]);
    return count;
  });
  
  dv.paragraph(`**Weekly Chart Data**: Labels: [${labels.join(', ')}] | Data: [${data.join(', ')}]`);
}
```
**Explanation**: This advanced habit tracking system creates interactive toggle inputs for each habit, calculates streaks and weekly completion rates, and prepares data for visualization. It demonstrates how multiple plugins can work together to create a comprehensive tracking solution.

**Synergy Highlight**: The system demonstrates emergent capability by combining:
- Meta Bind for interactive data input
- DataviewJS for data processing and calculations
- Centralized data storage in a dedicated note
- Structured output for Charts plugin integration
- Templater-compatible structure for automation

#### 💎 COMMUNITY-INSPIRED - Gamified Habit Achievement System
```cs
**🏆 Habit Achievement Dashboard**

<%*
// Generate dynamic habit tracking with achievement badges
const habits = [
  { id: "exercise", name: "Fitness Enthusiast", icon: "💪", threshold: 20 },
  { id: "meditate", name: "Mindfulness Master", icon: "🧘", threshold: 30 },
  { id: "read", name: "Bookworm", icon: "📚", threshold: 15 },
  { id: "journal", name: "Reflection Guru", icon: "✍️", threshold: 25 }
];
const habitData = dv.page("Habits/Tracking");
let achievements = 0;
let totalPossible = habits.length;
habits.forEach(habit => {
  // Count completions for this habit
  let completionCount = 0;
  for (let i = 0; i < habit.threshold; i++) {
    const dateKey = dv.date('today').minus(dv.duration(`${i} days`)).toFormat('yyyy-MM-dd');
    const habitKey = `${habit.id}-${dateKey}`;
    if (habitData && habitData[habitKey]) completionCount++;
  }
  
  // Determine achievement level
  let badge = "⚪ Not Started";
  if (completionCount >= habit.threshold) {
    badge = "🏆 Completed";
    achievements++;
  } else if (completionCount >= habit.threshold * 0.75) {
    badge = "🥇 Gold Progress";
  } else if (completionCount >= habit.threshold * 0.5) {
    badge = "🥈 Silver Progress";
  } else if (completionCount >= habit.threshold * 0.25) {
    badge = "🥉 Bronze Progress";
  } else if (completionCount > 0) {
    badge = "🟢 Started";
  }
  
  tR += `
**${habit.icon} ${habit.name}** (${completionCount}/${habit.threshold} days)
Progress: ${'█'.repeat(Math.floor(completionCount/habit.threshold*10))}${'░'.repeat(10-Math.floor(completionCount/habit.threshold*10))} ${Math.round(completionCount/habit.threshold*100)}%
Badge: ${badge}
INPUT[toggle:title(Completed Today):value([[Habits/Tracking#${habit.id}-${tp.date.now('YYYY-MM-DD')}]])]
---
`;
});
const overallProgress = Math.round(achievements/totalPossible*100);
tR += `
**Overall Progress**: ${achievements}/${totalPossible} Achievements (${overallProgress}%)
🏆 **Level**: ${overallProgress >= 80 ? "Habit Master" : overallProgress >= 60 ? "Consistency Champion" : overallProgress >= 40 ? "Building Momentum" : "Just Starting"}
`;
%>
```
**Source Pattern**: Community pattern inspired by gamification techniques in productivity apps like Habitica and Streaks
**Why This Works**: This approach leverages psychological principles of gamification by providing visual progress indicators, achievement badges, and level-based motivation. The Templater integration allows for dynamic calculation of progress and personalized feedback.

---

### Use Case 4: Daily Schedule Overview
**Purpose**: Display and manage daily schedule with calendar integration
**Plugins Used**: Tasks, Dataview, DataviewJS
**Integration Pattern**: Tasks for scheduling, Dataview for display, DataviewJS for time-based organization

#### 🟢 BASIC - Simple Schedule Display
```cs
TASK
FROM "Daily Notes"
WHERE file.day = date(today) AND due = date(today)
SORT due ASC
```
**Explanation**: This basic query displays all tasks scheduled for today, sorted by due time. It leverages the Tasks plugin's date parsing to automatically filter and organize scheduled items.

**Customization Points**:
- `date(today)`: Can be changed to view other days
- Add time-based sorting with `SORT due.hour ASC`
- Filter by specific tags or priorities

#### 🟡 INTERMEDIATE - Time-Blocked Schedule
```cs
/**
 * PURPOSE: Create a time-blocked schedule view with duration tracking
 * PLUGINS: Tasks + DataviewJS
 * INTEGRATION: Process task metadata to create structured schedule
 */

// Get today's scheduled tasks
const todayNote = dv.current();
const scheduledTasks = todayNote.file.tasks
  .where(t => t.due && t.due.toFormat("yyyy-MM-dd") === dv.date("today").toFormat("yyyy-MM-dd"))
  .sort(t => t.due);

// Group tasks by time periods
const timeBlocks = {
  "Morning (6AM-12PM)": [],
  "Afternoon (12PM-6PM)": [],
  "Evening (6PM-10PM)": [],
  "Night (10PM-6AM)": []
};

scheduledTasks.forEach(task => {
  if (task.due) {
    const hour = task.due.hour;
    if (hour >= 6 && hour < 12) {
      timeBlocks["Morning (6AM-12PM)"].push(task);
    } else if (hour >= 12 && hour < 18) {
      timeBlocks["Afternoon (12PM-6PM)"].push(task);
    } else if (hour >= 18 && hour < 22) {
      timeBlocks["Evening (6PM-10PM)"].push(task);
    } else {
      timeBlocks["Night (10PM-6AM)"].push(task);
    }
  }
});

// Display time-blocked schedule
dv.header(2, "📅 Daily Schedule");

for (const [block, tasks] of Object.entries(timeBlocks)) {
  if (tasks.length > 0) {
    dv.header(3, block);
    dv.taskList(tasks);
  }
}

// Calculate total scheduled time (assuming 30min default, customizable with emoji)
const totalTasks = scheduledTasks.length;
const estimatedMinutes = scheduledTasks.reduce((total, task) => {
  // Look for time indicators in task text (e.g., "☕30m", "⏱60m")
  const timeMatch = task.text.match(/[⏱☕⚡](\d+)m/);
  return total + (timeMatch ? parseInt(timeMatch[1]) : 30);
}, 0);

dv.paragraph(`**Schedule Summary**: ${totalTasks} tasks | ~${estimatedMinutes} minutes scheduled`);
```
**Explanation**: This intermediate schedule viewer organizes tasks into time blocks (morning, afternoon, evening, night) and estimates total scheduled time based on duration indicators in task text.

**Integration Notes**:: Tasks can include time estimates using emoji indicators:
- ⏱60m (generic time)
- ☕30m (coffee break time)
- ⚡15m (quick task)

#### 🔴 ADVANCED - Integrated Calendar & Task System
```cs
/**
 * PURPOSE: Create a comprehensive schedule system integrating calendar events and tasks
 * PLUGINS: Tasks + DataviewJS + file metadata + external calendar (conceptual)
 * SYNERGY: Combines multiple data sources for unified scheduling view
 */

// Get today's data
const today = dv.date("today");
const todayNote = dv.current();

// 1. Get scheduled tasks from Tasks plugin
const scheduledTasks = todayNote.file.tasks
  .where(t => t.due && t.due.toFormat("yyyy-MM-dd") === today.toFormat("yyyy-MM-dd"))
  .sort(t => t.due);

// 2. Get calendar events (conceptual - would integrate with actual calendar plugin)
// For demo purposes, we'll simulate calendar events
const calendarEvents = [
  { title: "Team Standup", start: dv.date("today").set({ hour: 9, minute: 0 }), 
    end: dv.date("today").set({ hour: 9, minute: 30 }), type: "meeting" },
  { title: "Lunch Break", start: dv.date("today").set({ hour: 12, minute: 0 }), 
    end: dv.date("today").set({ hour: 13, minute: 0 }), type: "break" },
  { title: "Client Call", start: dv.date("today").set({ hour: 14, minute: 0 }), 
    end: dv.date("today").set({ hour: 15, minute: 0 }), type: "meeting" }
];

// 3. Combine and sort all scheduled items
const allScheduleItems = [];

// Add tasks
scheduledTasks.forEach(task => {
  if (task.due) {
    allScheduleItems.push({
      title: task.text,
      start: task.due,
      type: "task",
      completed: task.completed,
      priority: task.priority
    });
  }
});

// Add calendar events
calendarEvents.forEach(event => {
  allScheduleItems.push({
    title: event.title,
    start: event.start,
    end: event.end,
    type: "event",
    category: event.type
  });
});

// Sort by start time
allScheduleItems.sort((a, b) => a.start - b.start);

// Display integrated schedule
dv.header(2, "🗓️ Integrated Daily Schedule");

// Group by time blocks
const timeGroups = {};
allScheduleItems.forEach(item => {
  const hour = item.start.hour;
  const timeBlock = `${Math.floor(hour/2) * 2}:00-${Math.floor(hour/2) * 2 + 2}:00`;
  if (!timeGroups[timeBlock]) timeGroups[timeBlock] = [];
  timeGroups[timeBlock].push(item);
});

for (const [timeBlock, items] of Object.entries(timeGroups)) {
  dv.header(3, timeBlock);
  
  items.forEach(item => {
    let icon = "📋";
    if (item.type === "event") icon = item.category === "meeting" ? "👥" : "⏸️";
    if (item.type === "task" && item.completed) icon = "✅";
    
    let priorityIndicator = "";
    if (item.priority === "high") priorityIndicator = "🔺";
    else if (item.priority === "medium") priorityIndicator = "🔸";
    
    const timeDisplay = item.start.toFormat("h:mm a");
    dv.paragraph(`${icon} **${timeDisplay}**: ${item.title} ${priorityIndicator}`);
  });
}

// Schedule analytics
const totalItems = allScheduleItems.length;
const completedTasks = allScheduleItems.filter(item => item.type === "task" && item.completed).length;
const meetingCount = allScheduleItems.filter(item => item.type === "event").length;

dv.paragraph(`
**Schedule Analytics**:
- Total items: ${totalItems}
- Completed tasks: ${completedTasks}/${scheduledTasks.length}
- Meetings: ${meetingCount}
- Free time blocks: ${Object.keys(timeGroups).length - meetingCount - scheduledTasks.length}
`);
```
**Explanation**: This advanced schedule system integrates tasks and calendar events into a unified timeline view. It demonstrates how multiple data sources can be combined to create a comprehensive scheduling solution.

**Synergy Highlight**:: The system demonstrates emergent capability by combining
- Tasks plugin scheduling data
- Conceptual calendar event integration
- Time-based organization and sorting
- Visual categorization with icons
- Schedule analytics and optimization insights

---

## 📖 Extracted Definitions
```dataviewjs
const currentFile = dv.current().file;
const content = await dv.io.load(currentFile.path);
const bracketedFieldRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+)\]/g;

let definitions = [];
let match;

while ((match = bracketedFieldRegex.exec(content)) !== null) {
    definitions.push({
        key: match[1].trim(),
        value: match[2].trim()
    });
}

// Group by first letter
const grouped = {};
definitions.forEach(d => {
    const firstLetter = d.key[0].toUpperCase();
    if (!grouped[firstLetter]) grouped[firstLetter] = [];
    grouped[firstLetter].push(d);
});

// Display grouped results
const sortedLetters = Object.keys(grouped).sort();

for (let letter of sortedLetters) {
    dv.header(4, `${letter}`);
    dv.table(
        ["Term", "Definition"],
        grouped[letter].map(d => [`**${d.key}**`, d.value])
    );
}
```
---