
> [! ] ### Prompt Used for Original Request 
> #### Question
> - Are there any Dataview Queries (Inline, Code Block, or JS) that can read all the Key:: Value pairs and either list, table, or chart them?
> #### Context
> - When actively reading a report I was thinking about using the Key:: Value to save definitions, key-terms, or words, Etc. But dont want to have to pull them out individually.
> #### Example:
> 
> [**Purpose confusion**:: occurs when the thinker lacks a clearly defined goal, leading to unfocused wandering rather than directed inquiry.] [**Purpose substitution**:: happens when an initial worthwhile purpose gets replaced mid-stream by a trivial or distracting purpose]—beginning research to understand a phenomenon but becoming diverted into defending a predetermined conclusion. [**Hidden purposes**:: undermine intellectual honesty when unstated agendas (protecting ego, winning arguments, maintaining comfortable beliefs) drive reasoning that claims different explicit purposes.] [**Conflicting purposes**:: create logical incoherence when a single reasoning process attempts to serve incompatible ends simultaneously—trying both to pursue truth and to avoid uncomfortable conclusions.]
> 
> #### Task
> - What way(s)/system(s) can you come up with to accomplish this?

> [! ] ### Prompt for Dataview Definitions System
```
<goal>
To add onto my current system for Keywords, Definitions, Important terms, Etc.
</goal>
<context>
I have been working on a system that uses Dataview to query `[key:: value]` pairs, that I create during active reading sessions.

- The syntax for the pair goes like this:
	- [**Key Word or Definition**:: Followed by the definition/information pertaining to the term, Etc.]

As I was reviewing some Dataviewjs queries you generated I had an idea on how to potentially improve/add to this system I'm building.
</context>
<the-idea>
Embedded Definitions Glossary

1. I Create a Query Note
	- It has dataviewjs that has been designed to query an entire folder, for the `[Key:: Value]` pairs.
		- Dataview sorts these pairs alphabetically, and then groups them in various configurations through multiple queries.
		- Some queries could contain metrics, in a styled window at the top of the query.
	- Don't forget about the other plugins that I currently use, these could provide extra benefits or new possibilities.
2. I then use the query note(s), as a template.
	- The template allows you to embed/transclude a master glossary list in any note. 
		- This glossary constantly grows, by adding new notes with `[Key:: Values]` inside, to the current *query note folder*.
- Note: What else like this is possible with Dataview.
	- Think the movie "Inception".
</the-idea>

<task>
I need you to analyze this hypothetical system addition, if its considered a functioning system (meaning if its possible) then I want you to think through it step by step (design the system) and work all out the details. 

Then generate a note that contains all the information I would need such as: Dataview Quires, Implementation instruction, If there are other synergies you think of, or Other Dataview ideas, all will be in this note.
</tas>
```















  

# Index/Library for Dataview Queries

>[! ] ### List All Inline Fields in Current Note
```
LIST rows.file.link
FROM "[[Current Note Name]]"
FLATTEN file.lists as L
WHERE meta(L).subpath
GROUP BY meta(L).subpath as "Key"
```

>[! ] ### Table of All Inline Fields with Values
- 2 Note: This query works but only so far with whole folders.
```
// 🔍 Dynamic Frontmatter Dictionary
// Iterates all files in a folder and lists every Key/Value pair found in Frontmatter
// Excludes system keys like tags, aliases, and position.

const pages = dv.pages(''); // 🟢 UPDATE YOUR FOLDER PATH HERE
const rows = [];

pages.forEach(page => {
    // Get the frontmatter object
    const fm = page.file.frontmatter;
    
    // Iterate over entries
    Object.entries(fm).forEach(([key, value]) => {
        // 🛑 Filter out unwanted keys
        if (key !== "tags" && key !== "aliases" && key !== "position") {
            // Push to rows: [Key, Value, Link to File]
            rows.push([key, value, page.file.link]);
        }
    });
});

// Render the table
dv.table(["Term", "Definition", "Source Note"], rows);
```

>[! ] ### Extract Body Inline Fields
```dataviewj
// Get current file content
const file = dv.current().file;
const content = await dv.io.load(file.path);

// Regex to match inline fields: Key:: Value
const inlineFieldRegex = /\*\*([^*]+)\*\*::\s*([^\n]+)/g;

// Extract all matches
let matches = [];
let match;
while ((match = inlineFieldRegex.exec(content)) !== null) {
    matches.push({
        term: match[1].trim(),
        definition: match[2].trim()
    });
}

// Display as table
if (matches.length > 0) {
    dv.table(
        ["Term", "Definition"],
        matches.map(m => [m.term, m.definition])
    );
} else {
    dv.paragraph("*No inline fields found in this note.*");
}
```

>[! ] ### Extract Bracketed Inline Fields from Current Note
```dataviewj
// Configuration
const currentFile = dv.current().file;

// Load file content
const content = await dv.io.load(currentFile.path);

// Regex for bracketed format: [**Key**:: Value]
const bracketedFieldRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+)\]/g;

// Extract all matches
let definitions = [];
let match;

while ((match = bracketedFieldRegex.exec(content)) !== null) {
    definitions.push({
        key: match[1].trim(),
        value: match[2].trim()
    });
}

// Display results
if (definitions.length > 0) {
    dv.header(3, `📖 Extracted Definitions (${definitions.length} found)`);
    dv.table(
        ["🔑 Term", "📝 Definition"],
        definitions.map(d => [
            `**${d.key}**`,
            d.value
        ])
    );
} else {
    dv.paragraph("*No bracketed inline fields found in this note.*");
}
```

>[! ] ### Extract from Multiple Notes in a Folder
```dataviewj
// Configuration
const folderPath = "Your-Reports-Folder"; // Change this to your folder
const pages = dv.pages(`"${folderPath}"`);

// Storage for all definitions across files
let allDefinitions = [];

// Process each file
for (let page of pages) {
    const content = await dv.io.load(page.file.path);
    const bracketedFieldRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+)\]/g;
    
    let match;
    while ((match = bracketedFieldRegex.exec(content)) !== null) {
        allDefinitions.push({
            source: page.file.link,
            key: match[1].trim(),
            value: match[2].trim()
        });
    }
}

// Display aggregated results
if (allDefinitions.length > 0) {
    dv.header(3, `📚 All Definitions Across ${folderPath} (${allDefinitions.length} total)`);
    dv.table(
        ["📄 Source", "🔑 Term", "📝 Definition"],
        allDefinitions.map(d => [
            d.source,
            `**${d.key}**`,
            d.value
        ])
    );
} else {
    dv.paragraph(`*No bracketed inline fields found in "${folderPath}".*`);
}
```

>[! ] ### Grouped by First Letter (Dictionary Style)
```dataviewj
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

>[! ] ### With Statistics and Count
```dataviewj
const currentFile = dv.current().file;
const content = await dv.io.load(currentFile.path);
const bracketedFieldRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+)\]/g;

let definitions = [];
let match;

while ((match = bracketedFieldRegex.exec(content)) !== null) {
    const def = {
        key: match[1].trim(),
        value: match[2].trim()
    };
    def.wordCount = def.value.split(/\s+/).length;
    definitions.push(def);
}

// Statistics
const totalDefs = definitions.length;
const avgWordCount = totalDefs > 0 
    ? Math.round(definitions.reduce((sum, d) => sum + d.wordCount, 0) / totalDefs)
    : 0;

// Display stats
dv.header(3, "📊 Definition Statistics");
dv.paragraph(`**Total Definitions:** ${totalDefs}`);
dv.paragraph(`**Average Definition Length:** ${avgWordCount} words`);

// Display table with word counts
if (totalDefs > 0) {
    dv.header(3, "📖 All Definitions");
    dv.table(
        ["Term", "Definition", "Words"],
        definitions.map(d => [
            `**${d.key}**`,
            d.value,
            d.wordCount
        ])
    );
}
```

>[! ] ### Callout-Style Display
```dataviewj
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

// Display as definition callouts
for (let def of definitions) {
    dv.paragraph(`> [!definition] ${def.key}\n> ${def.value}`);
}
```

>[! ] ### Bulleted List with Sub-items
```dataviewj
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

// Display as nested list
dv.header(3, "📖 Definitions");
dv.list(
    definitions.map(d => `**${d.key}**\n  - ${d.value}`)
);
```

>[! ] ## Master Glossary Across Entire Vault
```dataviewj
// Configuration
const excludeFolders = ["Templates", "Archive"]; // Folders to skip
const includeOnlyTags = null; // Set to ["#report", "#research"] to filter, or null for all notes

// Get all pages (with optional filtering)
let query = `""`;
if (includeOnlyTags) {
    query = includeOnlyTags.map(tag => `#${tag.replace('#', '')}`).join(" OR ");
}
const pages = dv.pages(query);

// Storage for all definitions
let allDefinitions = new Map(); // Use Map to deduplicate keys

// Process each file
for (let page of pages) {
    // Skip excluded folders
    const folderPath = page.file.folder;
    if (excludeFolders.some(excluded => folderPath.includes(excluded))) {
        continue;
    }
    
    const content = await dv.io.load(page.file.path);
    const bracketedFieldRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+)\]/g;
    
    let match;
    while ((match = bracketedFieldRegex.exec(content)) !== null) {
        const key = match[1].trim();
        const value = match[2].trim();
        
        // If key already exists, collect multiple sources
        if (allDefinitions.has(key)) {
            const existing = allDefinitions.get(key);
            existing.sources.push(page.file.link);
            // Optionally: append definitions or keep first occurrence
        } else {
            allDefinitions.set(key, {
                key: key,
                value: value,
                sources: [page.file.link]
            });
        }
    }
}

// Convert Map to array and sort alphabetically
const sortedDefinitions = Array.from(allDefinitions.values())
    .sort((a, b) => a.key.localeCompare(b.key));

// Display results
if (sortedDefinitions.length > 0) {
    dv.header(2, `📚 Master Glossary (${sortedDefinitions.length} terms)`);
    dv.table(
        ["🔑 Term", "📝 Definition", "📄 Sources"],
        sortedDefinitions.map(d => [
            `**${d.key}**`,
            d.value,
            d.sources.join(", ")
        ])
    );
} else {
    dv.paragraph("*No definitions found in vault.*");
}
```

>[! ] ### Combine Frontmatter + Inline Fields
```dataviewj
const currentFile = dv.current().file;
const content = await dv.io.load(currentFile.path);

// Extract frontmatter definitions (if you have a custom "definitions" key)
const frontmatterDefs = currentFile.frontmatter?.definitions || {};

// Extract inline bracketed fields
const bracketedFieldRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+)\]/g;
let inlineDefs = [];
let match;

while ((match = bracketedFieldRegex.exec(content)) !== null) {
    inlineDefs.push({
        key: match[1].trim(),
        value: match[2].trim(),
        source: "Inline"
    });
}

// Combine frontmatter and inline definitions
let allDefs = [
    …Object.entries(frontmatterDefs).map(([k, v]) => ({
        key: k,
        value: v,
        source: "Frontmatter"
    })),
    …inlineDefs
];

// Display combined
if (allDefs.length > 0) {
    dv.header(3, "📖 All Definitions (Frontmatter + Inline)");
    dv.table(
        ["Term", "Definition", "Source"],
        allDefs.map(d => [
            `**${d.key}**`,
            d.value,
            d.source
        ])
    );
}
```

>[! ] ## Search Definitions by Keyword
```dataviewj
const searchTerm = "purpose"; // Change this to search different terms
const currentFile = dv.current().file;
const content = await dv.io.load(currentFile.path);
const bracketedFieldRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+)\]/g;

let definitions = [];
let match;

while ((match = bracketedFieldRegex.exec(content)) !== null) {
    const key = match[1].trim();
    const value = match[2].trim();
    
    // Case-insensitive search in both key and value
    if (key.toLowerCase().includes(searchTerm.toLowerCase()) ||
        value.toLowerCase().includes(searchTerm.toLowerCase())) {
        definitions.push({ key, value });
    }
}

if (definitions.length > 0) {
    dv.header(3, `🔎 Definitions containing "${searchTerm}" (${definitions.length} found)`);
    dv.table(
        ["Term", "Definition"],
        definitions.map(d => [`**${d.key}**`, d.value])
    );
} else {
    dv.paragraph(`*No definitions found containing "${searchTerm}".*`);
}
```

>[! ] ### Export to CSV (for external processing)
```dataviewj
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

// Generate CSV content
let csv = "Term,Definition\n";
definitions.forEach(d => {
    // Escape quotes and wrap in quotes for CSV
    const escapedValue = d.value.replace(/"/g, '""');
    csv += `"${d.key}","${escapedValue}"\n`;
});

// Display download button (requires manual copy)
dv.header(3, "📥 CSV Export");
dv.paragraph("Copy the content below and save as `definitions.csv`:");
dv.paragraph("```csv\n" + csv + "\n```");
```



>[! ]  ### "Current Note" Extractor
> 
> - Place this code block at the top or bottom of your Report note. It will automatically find every `[**Key**:: Value]` in the file and list them.
> > [! ] **How it works**
> > This script loads the raw text of the current file, uses a "Regular Expression" to find patterns matching `[**Something**:: Something else]`, and displays them in a neat Markdown table.
```dataviewj
// 1. Get the current file content
const fileContent = await dv.io.load(dv.current().file.path);

// 2. Define the Regex pattern
// Matches: [**Term**:: Definition]
// Group 1: The Term (between ** and **)
// Group 2: The Definition (after :: and before ])
const regex = /\[\*\*(.*?)\*\*::\s*(.*?)\]/g;

// 3. Extract matches
let matches = [];
let match;
while ((match = regex.exec(fileContent)) !== null) {
    // match[1] is the Key, match[2] is the Value
    matches.push([match[1], match[2]]);
}

// 4. Render the Table
if (matches.length > 0) {
    dv.header(3, "📖 Key Terms & Definitions");
    dv.table(
        ["Term", "Definition"], 
        matches.map(m => [`**${m[0]}**`, m[1]])
    );
} else {
    dv.paragraph("_No definitions found in this note._");
}
```

>[! ] ### "Master Glossary" Dashboard
> 
> Create a new note called `[[Master Glossary]]`. Use this script to scan **all notes** in a specific folder (e.g., "Reports") and aggregate every definition you've ever written.
```dataviewj
// CONFIGURATION: Folder to search
const folder = "03_notes"; // Change this to your folder path

// Get all files in that folder
const files = dv.pages(`"${folder}"`);
let allDefinitions = [];

// Loop through each file
for (let page of files) {
    // Load the raw content of the file
    const content = await dv.io.load(page.file.path);
    
    // Regex to find [**Term**:: Definition]
    const regex = /\[\*\*(.*?)\*\*::\s*(.*?)\]/g;
    let match;
    
    // Extract all matches in this file
    while ((match = regex.exec(content)) !== null) {
        allDefinitions.push({
            term: match[1],
            def: match[2],
            link: page.file.link
        });
    }
}

// Sort alphabetically by Term
allDefinitions.sort((a, b) => a.term.localeCompare(b.term));

// Render the Global Table
dv.header(2, "🌍 System-Wide Glossary");
dv.table(
    ["Term", "Definition", "Source Note"],
    allDefinitions.map(d => [`**${d.term}**`, d.def, d.link])
);
```

>[! ] ### The "Clean Syntax" Alternative
> 
> If you decide you don't need the bolding inside the brackets and prefer using standard properties like `(Purpose confusion:: occurs when…)` or `[Purpose confusion:: occurs when…]` (no stars), you can use this simpler script which is slightly faster as it doesn't need to read the raw file text:
```dataviewj
// Only works if you use [Key:: Value] without the **stars** inside
const page = dv.current();
const excluded = ["file", "tags", "aliases", "cssclasses", "date", "cover", "type"]; // Add fields to hide

let definitions = [];
for (let [key, value] of Object.entries(page)) {
    if (excluded.includes(key)) continue;
    definitions.push([key, value]);
}

dv.table(["Term", "Definition"], definitions);
```













































----

> [! ] ## 🔧 Solutions for Definition Text Wrapping
> 
> [!important] The Problem
> [[Dataview]] tables have default CSS that constrains column widths, causing long text to truncate with "…" in Reading mode. This affects all table-based queries.

> [! ] ## ✅ Solution 1: CSS Snippet (Global Fix - Recommended)
> 
> This fixes **all** Dataview tables in your vault to wrap text properly.
> 
> ### Step-by-Step Installation:
> 
> ##### Step 1: Create CSS Snippet
> 1. Open Obsidian Settings (`Ctrl/Cmd + ,`)
> 2. Navigate to **Appearance** → **CSS snippets**
> 3. Click the folder icon 📁 to open your snippets folder
> 4. Create a new file named `dataview-table-wrapping.css`
> 
> ##### Step 2: Add This CSS Code
```css
/* Force Dataview tables to wrap long text */
.table-view-table {
    table-layout: auto !important;
}

.table-view-table td,
.table-view-table th {
    white-space: normal !important;
    word-wrap: break-word !important;
    max-width: none !important;
    vertical-align: top !important;
}

/* Specific styling for definition columns */
.table-view-table td:nth-child(2),
.table-view-table td:last-child {
    min-width: 300px;
    max-width: 600px;
}

/* Ensure proper spacing */
.table-view-table td {
    padding: 8px 12px !important;
    line-height: 1.6 !important;
}
```
> [! ] 
> ##### Step 3: Enable the Snippet
> 1. Return to Settings → Appearance → CSS snippets
> 2. Find `dataview-table-wrapping` in the list
> 3. Toggle it **ON** (the toggle should turn purple/blue)
> 4. Reload any notes with tables to see the effect
> > [!helpful-tip] Instant Results
> > Once enabled, all Dataview tables will automatically wrap text without modifying any queries. This is the cleanest solution for vault-wide consistency.
