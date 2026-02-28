---
title: 🗯️LLM-Chat_Useful-Dataview-Queries_🆔20251029215617
id: 20251029215648
aliases:
  - chat
  - llm
  - llm/chat
  - response
type: 🗯️llm-chat
status: ❔
priority: ❔
rating:
created: 2025-10-29T21:56:48
source: ❔
url: https://gemini.google.com/gem/5c3a909a23bf/271a0dca9f02e378
tags:
  - llm
  - llm/chat
  - prompt-engineering
  - pkb/infrastructure/automation
description: This is a record/history of a chat I had with an LLM.
version: ❔
success-rating: ❔
date created: 2025-10-29T21:56:47.000-04:00
date modified: 2025-10-29T21:59:43.789-04:00
---

> [!cite]
> **Bibliographic Information**
> - **Source Type**:: AI-Chat-History
> - **Title**:: Useful-Dataview-Queries
> - **Author(s)**:: Gemini-2.5-Pro_Gem-Dataview-Architect
> - **Year**:: 2025
> - **Publisher / Journal**::
> - **Volume / Issue**:: 001
> - **Page(s)**:: 001
> - **URL / DOI**:: <https://gemini.google.com/gem/5c3a909a23bf/271a0dca9f02e378>
> - **Date Accessed**:: 2025-10-29T21:56:48

# **Prompt Used**


# **Goal**

A collection of Dataview resources I can pull from, as needed, for my Prompt Component Project/Library.

# **Task**

Below you will find a set of data. Its purpose is, the information pertaining to my Prompt Component Library. Such as Tags, Aliases, Etc. 
I want you to use this information to generate various sets of dataview queries that I can use to build a Dashboard or MOC, or anything else for my PKB. (Personal Knowledge Base)

Let me know if there is any specific information that you need, other than what I provided.

# **Dataview Information**
This is the *Dataview information that pertains to* my project:: 🚀PROJ_🧩📝Prompting-Materials-Collection



```
- **Tags**:
	- `prompting/component`
	- `🧩pmc`
	- `component/type/{type of component is put here⬇️}`
		- *Choices for the Component Type are*:
			- `component/type/⛔constraint`
			- `component/type/🎨style`
			- `component/type/🎭persona`
			- `component/type/📐format`
			- `component/type/🏗️scaffolding`
			- `component/type/💫exemplar`
			- `component/type/🗝️key-add-in`
- **Type**:
	- `🧩component`
- **Status**:
	- `🌱seedling` - **Note**: *For new Components, may have been used a handful of times or not at all*.
	- `🌿sprout` - **Note**: *Simple, growing and starting to become used more often Component*.
	- `🪴planted` - **Note**: *A cultivated, frequently-used Component*.
	- `🌳tree` - **Note**: *A mature, well-developed and very well-used Component*.
- **Folders-Being-Used**:
	1. 03_🧩Components
		1. 01_⛔Constraint
		2. 02_🎨Style
		3. 03_🎭Persona
		4. 04_📐Format
		5. 05_🏗️Contextual-Scaffolds
		6. 06_💫Exemplars
		7. 07_🗝️Key-Add-In's
- **Relative Path to Top Level Folder**
	- 02 🚀Projects/🚀PROJ_🧩📝Prompting-Materials-Collection/Database_Prompting/Database-01-🆔20251023111403/03_🧩Components

```

# **LLM Response**

Here is a complete, ready-to-use dashboard for your Prompt Component Library, built with a mix of Dataview DQL and DataviewJS to provide you with the exact controls you need.

As **The Dataview Architect**, I don't just build queries; I design information systems. Your metadata structure is excellent, with smart redundancies (folders and tags) and clear, actionable statuses. This dashboard is designed to leverage that structure, giving you a high-level "control panel" and deep-dive "workshop" views.

-----

# 🚀 Dashboard: Prompt Component Library

This dashboard provides a complete overview of your `🚀PROJ_🧩📝Prompting-Materials-Collection`. It's organized into three sections:

1. **Mission Control:** High-level statistics on the entire library.
2. **The Component Library:** Your complete collection, grouped by functional type.
3. **The Workshop:** A maintenance and workflow view, sorted by component maturity and identifying items that need attention.

-----

## 📈 Mission Control

This section provides a high-level summary of your component library's status.

I am using **DataviewJS** here because it allows us to fetch all the relevant pages once and then perform multiple calculations (like counts for each status) to display in a clean summary table. Standard DQL is less suited for creating custom summary tables like this.

We will use your unique project tag, `"#🧩pmc"`, as the primary data source for all queries. It's fast, folder-independent, and specific to this project.

```
// We will use DataviewJS to get all pages with the #🧩pmc tag
const pages = dv.pages("#🧩pmc");

// Now, we calculate the counts for each status
const statusCounts = {
    "🌱seedling": pages.where(p => p.Status === "🌱seedling").length,
    "🌿sprout": pages.where(p => p.Status === "🌿sprout").length,
    "🪴planted": pages.where(p => p.Status === "🪴planted").length,
    "🌳tree": pages.where(p => p.Status === "🌳tree").length,
    "No Status": pages.where(p => !p.Status).length
};
const total = pages.length;

// Finally, we render this data in a clean table
dv.table(
    ["Status", "Count"], // Headers
    Object.entries(statusCounts).map(([status, count]) => [status, count])
        .concat([["**Total Components**", `**${total}**`]]) // Add the total row
);
```

-----

## 📚 The Component Library (Grouped by Type)

This is your master library. It finds all components and groups them by their functional type.

For this, we'll use **DQL (Dataview Query Language)**. Its `GROUP BY` function is perfect for this task. The query works by:

1. Finding all pages tagged `"#🧩pmc"`.
2. Filtering the tags on each file to find the one that starts with `component/type/`.
3. Using `regexreplace` to strip that prefix, leaving only the clean type (e.g., "⛔constraint").
4. Grouping the files under these clean headers.

<!-- end list -->

```
LIST
FROM "#🧩pmc"
SORT file.name ASC
GROUP BY regexreplace(filter(file.tags, (t) => startswith(t, "component/type/")), "component/type/", "")
```

-----

## 🛠️ The Workshop (Grouped by Status)

This is your workflow view. It shows you which components are mature and ready for use (`🌳tree`) versus which are new and need development (`🌱seedling`).

This task *requires* **DataviewJS**. Your statuses have a specific logical order (`🌱` -\> `🌿` -\> `🪴` -\> `🌳`) that is not alphabetical. DQL's `GROUP BY` can only sort alphabetically, which would put `🌳tree` first. With DataviewJS, we can define a custom sort order for the groups.

This script will:

1. Define your custom `statusOrder`.
2. Get all pages with a `Status` field.
3. Group them by `Status`.
4. **Sort the groups** according to your custom order.
5. Display a table for each group, showing the component, its type, and when it was last modified.

<!-- end list -->

```
// Define the exact order you want your groups to appear in
const statusOrder = ["🌱seedling", "🌿sprout", "🪴planted", "🌳tree"];

// Get all pages that have a Status
const pages = dv.pages("#🧩pmc").where(p => p.Status);

// Group the pages by their status, then sort those GROUPS
// based on the index in our statusOrder array.
const sortedGroups = pages
    .groupBy(p => p.Status)
    .sort(g => statusOrder.indexOf(g.key));

// Loop through each sorted group and render a header and table
for (let group of sortedGroups) {
    // Add the header (e.g., "### 🌱seedling")
    dv.header(3, group.key); 
    
    // Create a table of files for that group
    dv.table(
        ["Component", "Type", "Last Modified"],
        group.rows
            .sort(r => r.file.name, 'asc') // Sort files alphabetically within the group
            .map(p => [
                p.file.link,
                // This cleans up the type tag for display
                p.file.tags.filter(t => t.startsWith("component/type/")).map(t => t.replace("component/type/", "")).join(", "),
                p.file.mtime.toFormat("yyyy-MM-dd")
            ])
    );
}
```

### 🧹 Maintenance Queues

Here are two simple **DQL** queries to find components that are missing important metadata.

> [\!todo]Components Missing a Status
> These components have the `"#🧩pmc"` tag but are missing the `Status::` field.
>
> 
> LIST
> FROM "#🧩pmc"
> WHERE !Status
> SORT file.name ASC
> 

> [\!todo]Components Missing a Type
> These components have the `"#🧩pmc"` tag but are not tagged with a `component/type/` tag.
>
> 
> LIST
> FROM "#🧩pmc"
> WHERE length(filter(file.tags, (t) => startswith(t, "component/type/"))) = 0
> SORT file.name ASC
> 

-----

This dashboard should provide a robust system for managing and growing your prompt library.

Would you like me to brainstorm some queries that could show which components are used most often (by tracking `file.inlinks`)?

# Pur3v4d3r-Response

That's great, I want to build a resource library of these, what else have you got?

# Dataview-Architect-Response

An excellent goal. A true Architect maintains a library of core blueprints. You are building your "armory" of patterns that can be deployed and adapted to any system.

I have access to a large collection of reference queries and advanced implementations. Here are several powerful blueprints, ranging from visual dashboards to advanced data processing, pulled directly from my reference library.

Here are some more patterns you can add to your collection.

-----


-----

### 2\. The Project Motivator: Evolving Progress Bar

This is a highly motivational **DataviewJS** query that combines data with visual flair. It calculates a project's progress (like word count) and displays a progress bar, but it also evolves an image based on that percentage. This is excellent for long-term projects like writing a book or completing a course.

This variant is flexible, allowing any number of images to be used.

```
const pagePath = "" // the page path from vault root
const inlineWordcount = "wordcount"; // the field your wordcount is saved in
const inlineTargetCount = "targetcount" // the field your target count is saved in
const name = "Story Progress"; // The name of your mon
const images = ["flower_growth/flowergrowth1.png", "flower_growth/flowergrowth2.png","flower_growth/flowergrowth3.png","flower_growth/flowergrowth4.png","flower_growth/flowergrowth5.png","flower_growth/flowergrowth6.png"] // Image file names to use for your mon. 


// rendering, doesn't need to be adjusted 
const page = dv.page(pagePath);
let image = images[0];
const percentage = Math.round(page[inlineWordcount] / page[inlineTargetCount] * 100);
if (images.length > 1) {
	const breakpoint = 100 / images.length;
	let i = 0;
	let currentBreakpoint = (i + 1) * breakpoint;
	while (percentage > currentBreakpoint && currentBreakpoint <= 100) {
		i++;
		currentBreakpoint = (i + 1) * breakpoint;
	}
	image = images[i]
} 

const attachments = this.app.vault.getConfig("attachmentFolderPath");
const basePath = this.app.vault.adapter.basePath

const html = `<div class="monwrapper" style="display:flex;align-items:center;">
<img src="${basePath}/${attachments}/${image}" class="mon" style="margin-right:10px;"></img>
<div>
<div class="monname">${name}</div>
<div class="progressbar"><progress max="100" value="${percentage}"></progress> Lv. ${percentage}</div></div>
</div>`;
dv.el("div", html)
```

-----


-----


-----

### 5\. The Vault Janitor: Unresolved Links

A simple, fast, and essential **DQL** query for vault maintenance. This finds all "ghost" links in your vault—links pointing to notes that do not exist yet. It's a perfect query for a "Vault Maintenance" dashboard.

This DQL query finds all outlinks that do *not* have a corresponding file and groups them by the unresolved link, showing you every file that references it.

```

```

-----

### 6\. The Synergist: Plotting with Charts Plugin

This is a conceptual blueprint. Dataview can be used as a data engine for other plugins, most notably **Obsidian Charts**.

The principle is to use **DataviewJS** to:

1.  Execute a DQL query using `await dv.tryQuery(...)` to get your data.
2.  Process and format this data into the specific JSON structure that the Charts plugin expects (e.g., `labels` and `datasets`).
3.  Call `window.renderChart(chartData, this.container)` to have the Charts plugin render a visual chart (bar, line, pie, etc.) using your Dataview-sourced data.

The reference files contain complete examples of this for "Category-Series" and "Series-Category-Value" datasets, which I can provide if you'd like to explore that synergy.

Let me know which of these patterns you'd like to explore or adapt, and I can provide further architectural guidance.

# Pur3v4d3r-Response

What about for this project ion particular?

# Dataview-Architect-Response

Here are three more advanced blueprints, adapted from my reference library, specifically for your Prompt Component project.

These move beyond simple lists and create more interactive and data-dense views.

-----

### 1\. The Interactive Tabbed Library (by Type)

This is a powerful **DataviewJS** pattern that transforms your "Component Library" section from a long, scrolling page into a clean, interactive "tabbed" interface. Users can click a button for each component type to load *only* those components.

This is adapted from the "Render multiple tables with tab-like buttons" blueprint.

```
// --- Configuration ---
// Define your component types and the tag or folder to filter by.
// Using folders is often faster if you have them.
const components = {
    "⛔ Constraint": '"03_🧩Components/01_⛔Constraint"',
    "🎨 Style": '"03_🧩Components/02_🎨Style"',
    "🎭 Persona": '"03_🧩Components/03_🎭Persona"',
    "📐 Format": '"03_🧩Components/04_📐Format"',
    "🏗️ Scaffolds": '"03_🧩Components/05_🏗️Contextual-Scaffolds"',
    "💫 Exemplars": '"03_🧩Components/06_💫Exemplars"',
    "🗝️ Key-Add-In's": '"03_🧩Components/07_🗝️Key-Add-In\'s"',
    "All": '"03_🧩Components"'
}
const componentNames = Object.keys(components);
const componentSources = Object.values(components);

// --- Get Elements ---
// We create a container for the buttons
const btnContainer = dv.el('div');
// We create a container where the table will be rendered
const tableContainer = dv.el('div');

// --- Functions ---
const createButton = (name) => {
    const source = components[name]; // Get the folder path for this button
    const btn = dv.el('button', name);
    btn.addEventListener('click', (event) => {
        event.preventDefault();
        // When clicked, render the table for this source
        renderTable(source, name);
    });
    return btn;
}

const renderTable = async (source, name) => {
    // Clear the container
    tableContainer.innerHTML = '';
    
    // Build the DQL query string dynamically
    const query = `
        TABLE Status, file.mtime AS "Last Modified"
        FROM ${source}
        WHERE file.name != "meta" 
        SORT file.name ASC
    `;
    
    // Create a header for the rendered table
    const header = dv.el('h3', name);
    tableContainer.append(header);
    
    // Execute the query and render the results
    const result = await dv.query(query);
    if (result.type === 'table') {
        dv.table(result.headers, result.values, tableContainer);
    } else {
        dv.el('p', 'Error or no results found.', tableContainer);
    }
}

// --- Initial Load ---
// Create all the buttons and add them to the button container
componentNames.forEach(name => {
    btnContainer.append(createButton(name));
});

// Render the "All" view by default when the page loads
renderTable(components["All"], "All Components");

```

-----

### 2\. The Component "Maturity Matrix"

This **DQL** query provides a high-density "pivot table" view of your entire library. It answers the question: "How many components of each *Type* are at each *Status*?" This is the ultimate single-glance overview.

This query uses `FLATTEN` to create a "Type" field from your tags, then `GROUP BY` on that new field. The table columns then use the `filter()` function to count items in each status.

```
TABLE WITHOUT ID
    key AS "Component Type",
    length(filter(rows.Status, (s) => s = "🌱seedling")) AS "🌱",
    length(filter(rows.Status, (s) => s = "🌿sprout")) AS "🌿",
    length(filter(rows.Status, (s) => s = "🪴planted")) AS "🪴",
    length(filter(rows.Status, (s) => s = "🌳tree")) AS "🌳",
    length(rows) AS "Total"
FROM "#🧩pmc"
FLATTEN regexreplace(filter(file.tags, (t) => startswith(t, "component/type/")), "component/type/", "") AS Type
WHERE Type AND Status
GROUP BY Type
SORT key ASC
```

-----

### 3\. The "Ready to Use" Catalog (with Styling)

This query is for the *consumer* of your library, not the maintainer. It displays a clean, beautiful table of only the mature components ("Planted" and "Tree").

It uses an advanced `TABLE` column definition, pulling a pattern from `Style dataview table columns` to color-code the status, making it visually intuitive.

```
TABLE WITHOUT ID
    "<span style='font-size:1.1em;'>" + file.link + "</span>" AS Component,
    Type,
    choice(Status = "🌳tree", 
        "<span style='color:#4CAF50; font-weight:bold;'>🌳 Tree</span>", 
        "<span style='color:#2196F3;'>🪴 Planted</span>") AS Status
FROM "#🧩pmc"
FLATTEN regexreplace(filter(file.tags, (t) => startswith(t, "component/type/")), "component/type/", "") AS Type
WHERE Status = "🪴planted" OR Status = "🌳tree"
SORT Type ASC, file.name ASC
```

# **Pur3v4d3r-Response**

any others you can find that would work with this project?

# **Dataview-Architect-Response**

Here are four more blueprints from my reference library, specifically adapted to your Prompt Component project.

These patterns focus on **Usage**, **Visual Styling**, and **Dashboard Widgets** to make your library more dynamic.

-----

### 1\. Component Usage Leaderboard (DQL)

A key part of a library is knowing what's being used. This query finds all your components and ranks them by how many other notes link *to* them. It's the best way to find your most popular and "battle-tested" components.

This is a straightforward `TABLE` query that uses the implicit field `file.inlinks` and the `length()` function to count them.

```
TABLE
    length(file.inlinks) AS "Usage Count"
FROM "#🧩pmc"
SORT length(file.inlinks) DESC
```

**To See *Who* Uses Them:**

You can add the `file.inlinks` field to see a list of the actual pages linking to each component.

```
TABLE
    length(file.inlinks) AS "Usage Count",
    file.inlinks AS "Used By"
FROM "#🧩pmc"
WHERE length(file.inlinks) > 0
SORT length(file.inlinks) DESC
```

-----

### 2\. Styled "At-a-Glance" Library (DQL)

This query is perfect for a clean dashboard view. Instead of a table, it uses a `LIST` and combines string concatenation with inline HTML styling to create a rich, dense, and visually scannable list.

This pattern allows you to see the **Status**, **Component Name**, and **Type** all in one line.

```
LIST 
    choice(Status = "🌳tree", "🌳",
    choice(Status = "🪴planted", "🪴",
    choice(Status = "🌿sprout", "🌿", 
    choice(Status = "🌱seedling", "🌱", "❓"))))
    + " **" + file.link + "**"
    + " - *(" + regexreplace(filter(file.tags, (t) => startswith(t, "component/type/")), "component/type/", "") + ")*"
FROM "#🧩pmc"
WHERE Status
SORT Status, file.name ASC
```

-----

### 3\. Library Completion Progress Bar (Inline DataviewJS)

This is a fantastic widget for your main dashboard. It uses the "progress bar" pattern to show how "mature" your entire library is, based on how many components have reached the `🌳tree` status.

This is an **inline DataviewJS query**. You paste it directly into your note (not in a code block) to render the bar.

`$= const pages = dv.pages("#🧩pmc"); const mature = pages.where(p => p.Status == "🌳tree").length; const total = pages.length; const value = Math.round((mature / total) * 100); "<progress value='" + value + "' max='100'></progress>" + " **" + value + "% Mature** (" + mature + " of " + total + " components)"`

**Renders as:**
\<progress value='20' max='100'\>\</progress\> **20% Mature** (X of Y components)
*(Value will be calculated live in your vault)*

-----

### 4\. Random Component Spotlight (DataviewJS)

This is a powerful **DataviewJS** block for a dashboard. It finds all your *mature* components (Planted or Tree) and displays **one at random**. It's an excellent way to re-discover old components and keep them in your workflow.

This query is a great example of using Javascript to extend Dataview's capabilities.

```
// 1. Find all "ready-to-use" components
const pages = dv.pages("#🧩pmc")
    .where(p => p.Status == "🪴planted" || p.Status == "🌳tree");

if (pages.length > 0) {
    // 2. Select one random page from the list
    const randomPage = pages[Math.floor(Math.random() * pages.length)];

    // 3. Display it in a clean callout
    dv.el("div", `
        > [!tip] Random Component Spotlight
        > ## ${randomPage.file.link}
        >
        > **Status:** ${randomPage.Status}
        > **Type:** ${randomPage.file.tags.filter(t => t.startsWith("component/type/")).map(t => t.replace("component/type/", ""))}
    `);

} else {
    dv.el("p", "No mature components found to feature.");
}
```

# **Pur3v4d3r-Response**

any others you can find that would work with this project?

# **Dataview-Architect-Response**