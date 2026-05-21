



### Dataview Queries Simple to Advanced
```
You are a world-class Obsidian PKB Architect and Dataview plugin expert. You have a deep understanding of both standard Dataview Query Language (DQL) and the full DataviewJS API, including its use of Luxon for date/time manipulation.

Your task is to generate a comprehensive list of Dataview queries to be used as inspiration and educational examples for a user building their own PKB. You must generate a wide variety of queries, ranging from simple to highly advanced.

The examples must be centered around the theme of: **[INSERT THEME HERE]**

 **CRITICAL FORMATTING RULE:** All code blocks you generate MUST use plain Markdown backticks (```) with **NO language identifier** (do NOT use \`\`\`dataview or \`\`\`dataviewjs). This is to ensure the code is stored as inert text and does not auto-execute within an Obsidian note.

 You must follow this structure precisely:

 ---

 ## 🚀 Simple Queries (DQL)

 *Provide 3-4 examples of basic DQL queries (e.g., `LIST`, `TABLE`) using simple tags, folders, or task statuses. Enclose them in plain code blocks.*

 ---

 ## 🛠️ Intermediate Queries (DQL)

 *Provide 3-4 examples of more complex DQL queries. These should include functions like `FLATTEN`, `GROUP BY`, `contains()`, `length()`, and calculations or manipulations of fields (e.g., `TABLE date(today) - file.cday AS Age`). Enclose them in plain code blocks.*

 ---

 ## 🔬 Advanced Queries (DataviewJS)

 *Provide 2-3 examples of powerful DataviewJS queries.*

 **For each DataviewJS query, you MUST first provide a plain-English "Plan" that explains:**
 1.  What data it aims to find.
 2.  What logic/filters it will apply.
 3.  What the final output will look like (e.g., "A table with…" or "A task list…").

 *After the plan, provide the complete, functional DataviewJS code in a plain code block.
```


## DQL Queries

```
LIST
FROM #project 
WHERE status = "active"

TASK
WHERE !completed

TABLE priority, dueDate
FROM #project
WHERE status != "complete"
SORT priority ASC

TASK
WHERE !completed
GROUP BY file.link

TABLE file.mtime AS "Last Modified"
FROM #project
WHERE status = "active" AND (date(today) - file.mtime).days > 30
SORT file.mtime ASC

TABLE T.text AS Task, file.link AS Project
FROM #project
FLATTEN file.tasks AS T
WHERE !T.completed

TABLE WITHOUT ID key AS "unresolved link", rows.file.link AS "referencing file"
FROM "10 Example Data"
FLATTEN file.outlinks as outlinks
WHERE !(outlinks.file) AND !(contains(meta(outlinks).path, "/"))
GROUP BY outlinks

```


## Dataviewjs Queries

```
const projects = dv.pages("#project");

const data = projects.map(p => {
    const totalTasks = p.file.tasks.length;
    const completedTasks = p.file.tasks.filter(t => t.completed).length;
    
    let percentage = 0;
    if (totalTasks > 0) {
        percentage = Math.round((completedTasks / totalTasks) * 100);
    }

    const progressBarLength = 10; // 10 blocks wide
    const filledBlocks = Math.round((percentage / 100) * progressBarLength);
    const emptyBlocks = progressBarLength - filledBlocks;
    
    const progressBar = "🟩".repeat(filledBlocks) + "⬜️".repeat(emptyBlocks);

    return [
        p.file.link,
        progressBar,
        `${percentage}%`
    ];
});

dv.table(["Project", "Progress", "Percent"], data);
##########################################################################################################################################################################
const today = dv.date("today");
const nextWeek = dv.date("today").plus({ days: 7 });

const tasks = dv.pages().file.tasks
    .where(t => 
        !t.completed &&
        t.due &&
        t.due >= today &&
        t.due <= nextWeek
    )
    .sort(t => t.due);

if (tasks.length > 0) {
    dv.header(3, "Upcoming Deadlines: Next 7 Days");
    dv.taskList(tasks);
} else {
    dv.paragraph("✅ No tasks due in the next 7 days!");
}
##########################################################################################################################################################################
```




### The Habit Tracker: DVJS Heatmap Calendar

This is a cornerstone of many dashboards. Instead of a simple list, this **DataviewJS** query renders a full-year GitHub-style heatmap. It's perfect for visualizing habits, workouts, content creation, or any daily metric.

This variant maps data intensity (like your `Squats` field) to a color scale.

```d
dv.span("** 😊 Title 😥**") /* optional ⏹️💤⚡⚠🧩↑↓⏳📔💾📁📝🔄📝f𔀀⌨️🕸️📅🔍✨ */

const calendarData = {
    year: 2023,  // (optional) defaults to current year
    colors: {    // (optional) defaults to green
        blue:        ["#8cb9ff", "#69a3ff", "#428bff", "#1872ff", "#0058e2"], // first entry is considered default if supplied
        green:       ["#c6e48b", "#7bc96f", "#49af5d", "#2e8840", "#196127"],
        red:         ["#ff9e82", "#ff7b55", "#ff4d1a", "#e73400", "#bd2a00"],
        orange:      ["#ffa244", "#fd7f00", "#dd6f00", "#bf6000", "#9b4e00"],
        pink:        ["#ff96cb", "#ff70b8", "#ff3a9d", "#ee0077", "#c30062"],
        orangeToRed: ["#ffdf04", "#ffbe04", "#ff9a03", "#ff6d02", "#ff2c01"]
    },
    showCurrentDayBorder: true, // (optional) defaults to true
    defaultEntryIntensity: 4,   // (optional) defaults to 4
    intensityScaleStart: 10,    // (optional) defaults to lowest value passed to entries.intensity
    intensityScaleEnd: 100,     // (optional) defaults to highest value passed to entries.intensity
    entries: [],                // (required) populated in the DataviewJS loop below
}

//DataviewJS loop
const pages = dv.pages('"Journal/Daily"').where(t=> t.Squats)


for (let page of pages) {
    //dv.span("<br>" + page.file.name) // uncomment for troubleshooting
    calendarData.entries.push({
        date: page.file.name,        // (required) Format YYYY-MM-DD
        intensity: page.Squats,      // (required) the data you want to track, will map color intensities automatically
        content: await dv.span(`[[${page.file.name}|⚡]]`),           // (optional) Add text to the date cell
        color: "green",  // (optional) Reference from *calendarData.colors*. If no color is supplied; colors[0] is used
    })
}

renderHeatmapCalendar(this.container, calendarData)
```


### The Task Architect: Color-Coded Tasks

This **DataviewJS** script demonstrates how to take programmatic control over the `dv.taskList()` renderer. It finds tasks and prepends a colored bar based on task metadata (like `priority`), allowing you to visually distinguish tasks without complex CSS.

This variant uses a `map` object, which is a robust pattern that makes it easy to add or change your priority colors.

```
// define pages
const pages = dv.pages('"10 Example Data/projects"')

// OPEN TASKS
const tasks = pages.file.tasks.where(t => t.priority && !t.completed)

const priorityColorMap = {
	low: "rgb(55 166 155)",
	medium: "orange",
	high: "red",
}

// regex to remove the field priority in text
const regex = /\[priority[^\]]+\]/g

// assign colors according to priority
for (let task of tasks) {
	task.visual = getColorCode(task.priority) + task.text.replace(regex, "");
}

// render open tasks
const order = Object.keys(priorityColorMap)
dv.taskList(tasks.sort((a, b) => order.indexOf(b.priority) - order.indexOf(a.priority)), false)

// COMPLETED TASKS
const done = pages.file.tasks.where(t => t.completed)

// render completed tasks and add a limit to the number of the listed tasks (sorted by the completion date - need to activate auto-completion in dataview settings)
if (done.length >= 1) {
    dv.taskList(done.sort(t =>  t.priority &&  t.completion, 'desc').limit(10), false)
}

// change opacity of completed tasks
this.container.querySelectorAll("li.task-list-item.is-checked").forEach(s => s.style.opacity = "30%")

function getColorCode(priority) {
	const color = priorityColorMap[priority] ?? "grey";
	return `<span style='border-left: 3px solid ${color};'>&nbsp;</span>`
}
```

### The Interactive Dashboard: Tabbed Views

This is a powerful **DataviewJS** *architecture* for building a UI within a single page. It generates HTML buttons that, when clicked, re-run a function to render different Dataview tables or lists within the *same block*. This allows you to create "tabs" (e.g., "Watching," "Watched," "Stopped") for a media dashboard.

```
const createButton = (name) => {
	const btn = dv.el('button', name)
	btn.addEventListener('click', (event) => {
		event.preventDefault()
		removeTable()
		renderTable(name)
	})
	
	return btn
}

const buttons = ['Watching', 'Going to watch', 'Watched all', 'Stopped watching']

const renderTable = (name) => {
	const pages = dv.pages('"10 Example Data/shows"').where(page => page.status == name)
		
	dv.header(2, name)
	dv.table(
	['Title', 'Rating', 'Runtime', 'Seasons', 'Episodes'], 
	pages.map(page => [page.file.link, page.rating, page.runtime, page.seasons, page.episodes]))
}

const removeTable = () => {
	this.container.lastChild.remove()
	this.container.lastChild.remove()
}

buttons.forEach(button => createButton(button))

renderTable('Watching')
```

































