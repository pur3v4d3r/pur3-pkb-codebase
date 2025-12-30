> [!the-purpose]
> This is a database of sorts that will house all of my *Templater re-usable syntax*, that can be used to build Templates and Templater Automations.

### Core Syntax
#### Inline-Command
```cs
<% … %>
```
#### JavaScript
```cs
<%* … %>
```

### Date and Time (`tp.date`)

#### [Common-Moment.js-Format-Tokens]

| Token  | Output Example | Description               |
|:----- |:------------- |:------------------------ |
| `YYYY` | `2025`         | 4-digit year              |
| `YY`   | `25`           | 2-digit year              |
| `MMMM` | `October`      | Full month name           |
| `MMM`  | `Oct`          | Short month name          |
| `MM`   | `10`           | Month number (01-12)      |
| `DD`   | `25`           | Day of month (01-31)      |
| `Do`   | `25th`         | Day of month with ordinal |
| `dddd` | `Saturday`     | Full day name             |
| `ddd`  | `Sat`          | Short day name            |
| `HH`   | `16`           | Hour (24-hour, 00-23)     |
| `hh`   | `04`           | Hour (12-hour, 01-12)     |
| `mm`   | `02`           | Minute (00-59)            |
| `ss`   | `30`           | Second (00-59)            |
| `A`    | `PM`           | AM/PM                     |

#### [Time]-[16:02:30]
```
<% tp.date.now("HH:mm:ss") %>
```
#### [ISO]-[2025-10-31]
```cs
<% tp.date.now("YYYY-MM-DD") %>
```
#### [ISO-like]-[2025-10-10T21:10:12]
```cs
<% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
```
#### [ID]-[20251103083156]
```cs
<% tp.date.now("YYYYMMDDHHmmss") %>
```
#### [ID-Variant-02]-[20251103-083156]
```cs
<% tp.date.now('YYYYMMDD-HHmm') %>
```
#### [Saturday]
```
<% tp.date.now("dddd") %>
```
#### [SATURDAY_NOVEMBER-1ST-2025]
```cs
<% tp.date.now("dddd_MMMM-Do-YYYY_") %>
```
#### [Relative-Dates]
```
Tomorrow: <% tp.date.tomorrow("YYYY-MM-DD") %>
```
```
Yesterday: <% tp.date.yesterday("YYYY-MM-DD") %>
```
```
## 🔗 Daily Connections

**Yesterday**: [[<% tp.date.now("YYYY-MM-DD", -1, tp.file.title, "YYYY-MM-DD") %>]]
**Tomorrow**: [[<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>]]

**Weekly Note**: [[<% tp.date.now("YYYY-[W]ww") %>]]
**Monthly Note**: [[<% tp.date.now("YYYY-MM") %> Monthly Review]]
```
#### [Link-to-Daily-Note]-[[2025-11-19]]
```
link-related:
  - "<% tp.date.now('[[YYYY-MM-DD]]') %>"
```
#### [Creation-Date]-[Formatted]-[YYYY-MM-DD]
```
<% tp.file.creation_date("YYYY-MM-DD") %>
```
#### [Last-Modified]
```
<% tp.file.last_modified_date("dddd, MMMM Do YYYY @ HH:mm") %>
```

### YAML Frontmatter

#### [User-Prompt-Title]
```
<% await tp.system.prompt("Title for YAML") %>
```
#### [Type]
```
<% tp.frontmatter.type %>
```
#### [Status]
```
<% tp.frontmatter.status %>
```
#### [Version]
```
<% tp.frontmatter.version %>
```
#### [Summary]
```
<% tp.frontmatter.summary %>
```
#### [Topic]
```
<% tp.frontmatter.topic %>
```
#### [LLM-Model]
```
<% tp.frontmatter.model %>
```

### File Information (`tp.file`)

#### [File's-Title]
```
<% tp.file.title %>
```
#### [File-Path]
```
<% tp.file.path() %>
```
#### [Rename-the-File]
```
<% tp.file.rename("New Note Title") %>
```

### System and User Interaction (`tp.system`

#### [Prompt-for-Input]
```cs
 <%* const name = await tp.system.prompt("What is your name?") tR += `Hello, ${name}!` %>
```
#### [Multiple-choice]
```cs
 <%* const choice = await tp.system.suggester(["Option 1", "Option 2", "Option 3"], ["val1", "val2", "val3"], "Choose one:") tR += `You selected: ${choice}` %>
```

### Editor and Cursor (`tp.editor` & `tp.file.cursor`)
#### [Place-Cursor]
```cs
### My New Section
 <% tp.file.cursor() %>
```
#### [Get-Highlighted-Text]
```
 <%* const selection = tp.editor.get_selection() tR += `You highlighted: ${selection}` %>
```
#### [Insert-Text-at-Cursor]
```
 <%* tp.editor.insert("This text was inserted by a script.") %>
```

## JavaScript Blocks
#### Key
```cs
- await: You must use `await` for functions that are asynchronous, like `tp.system.prompt()`.
  - tR: This special variable holds the "template result". In a `<%* … %>` block, nothing is output unless you add it to `tR`. Use `tR += "your string"` to append to the output.
```


## Usable/Workable Examples



### Frontmatter
#### [Status]
```
<%* if (tp.frontmatter.type === "Gem") { tR += "v" + tp.frontmatter.version; } %>
```
```
<%* const status = tp.frontmatter.status; if (status) { tR += `[[${status}]]`; } %>
```
#### [ID]
```
<%* const emoji = tp.file.title.split('_')[0].split(' ')[0]; const id = tp.file.title.split('_').pop(); if (emoji && id) { tR += `${emoji}_${id}`; } %>
```
#### [Topic]
```
<%* const topic = tp.frontmatter.topic; if (topic) { tR += `[[${topic}]]`; } %>
```
#### [LLM-Model]
```
<%* const model = tp.frontmatter.model; if (model) { tR += `[[${model}]]`; } %>
```
#### [Version]
```
<%* if (tp.frontmatter.type === "Gem") { tR += "v" + tp.frontmatter.version; } %>
```
#### [Prompt-Code-Block]
```
---
id: prompt-block-<% tp.file.title.split('_').pop() %>
---

PASTE YOUR PROMPT OR GEM INSTRUCTION SET HERE
```

### [Full-YAML]-[Frontmatter Suggesters]
```
<%*
// Tag Suggester (Hierarchical Selection)
// GROUP A: High-Level Domains (For Tags 01 & 02)
const groupA_Tags = [
    "", "", "", "", "", 
	  "", "", "", "", "",
	  "", "", "", "", "",
	  "", "", "", "", "",
	  "", "", "", "", "",
	  "", "", "", "", "",
];  
// Tag Suggester (Hierarchical Selection)
// GROUP B: Granular Concepts (For Tags 03, 04, & 05)
const groupB_Tags = [
    // PKM & PKB
	  "", "", "", "", "",
    "", "", "", "", "",
	  "", "", "", "", "",
    "", "", "", "", "",
	  "", "", "", "", "",
    "", "", "", "", "",
    // Psychology & Cognitive
	  "", "", "", "", "",
	  "", "", "", "", "",
    "", "", "", "", "",
	  "", "", "", "", "",
    "", "", "", "", "",
	  "", "", "", "", "",
    "", "", "", "", "",
    // Prompt Engineering
	  "", "", "", "", "",
    "", "", "", "", "",
	  "", "", "", "", "",
    "", "", "", "", "",
	  "", "", "", "", "",
    "", "", "", "", "",
    // Cross-Cutting Concepts
	  "", "", "", "", "",
	  "", "", "", "", "",
	  "", "", "", "", "",
];
// Tag Suggester (Hierarchical Selection)
// GROUP A: High-Level Domains (For Tags 01 & 02)
const tag1 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 01 (Domain):");
const tag2 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 02 (Domain):");
// Tag Suggester (Hierarchical Selection)
// GROUP B: Granular Concepts (For Tags 03, 04, & 05)
const tag3 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 03 (Concept):");
const tag4 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 04 (Concept):");
const tag5 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 05 (Concept):");
const tag6 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 06 (Concept):");
// Alias system-prompt (User-Input)
const alias1 = await tp.system.prompt("Enter first alias (or press Enter to skip):");
const alias2 = await tp.system.prompt("Enter second alias (or press Enter to skip):");
// Type Suggester (User Selection for Type of Note)
const type = await tp.system.suggester(
	  "", "", "", "", "",
	  "", "", "", "", "",
	  "", "", "", "", "",
false,
    "Choose the Type:"
)
// Status Suggester (User Selection for Status of Note)
const status = await tp.system.suggester(
	  "", "", "", "", "",
	  "", "", "", "", "",
	  "", "", "", "", "",
false,
    "Choose the Status:"
)
---
aliases:
  - "<% alias1 %>"
  - "<% alias2 %>"
tags:
// Tag Placement in Note Body
// GROUP A: High-Level Domains
  - "<% tag1 %>"
  - "<% tag2 %>"
// Tag Placement in Note Body
// GROUP B: Granular Concepts
  - "<% tag3 %>"
  - "<% tag4 %>"
  - "<% tag5 %>"
  - "<% tag6 %>"
-%>
title: "<% tp.file.title %>"
id: "<% tp.date.now("YYYYMMDDHHmmss") %>"
created: "<% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>"
week: "[[<% tp.date.now("gggg-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% tp.date.now("YYYY") %>]]"
type: "<% type %>"
link-up:
  - 
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily-Note]]"
```



### Sorting (Alphabetical)
> [!info]
> - By default, the suggester shows the list in the exact order you defined in the array. If your array is messy, the list is messy.
> - To ensure similar items are always grouped together regardless of how you pasted them, simply add .sort() to the end of your array definition or before the suggester call.
```cs
// Sorts the list alphabetically before showing it to you
// This ensures "pkm/workflow/capture" sits right next to "pkm/workflow/process"
const tag4 = await tp.system.suggester(
    groupC_Tags.sort(), 
    groupC_Tags.sort(), 
    false, 
    "Select Tag 04"
);
```












### Visual "Pretty Print" (Recommended)
> [!info]
> - You can programmatically transform the "Display" list to use arrows and emojis, while keeping the "Result" list as the raw tag. This makes scanning the hierarchy much easier.
> - Replace your Input System section with this logic:
```cs
// … [Keep your large arrays above] …
// --- HELPER FUNCTION: FORMAT TAGS FOR DISPLAY ---
// This turns "pkm/theory/foundations" into "🧠 PKM > Theory > Foundations"
// It improves readability without changing the actual tag output.
function formatTagsForDisplay(tags) {
    return tags.map(tag => {
        let icon = "🔹"; // Default
        if (tag.startsWith("pkm") || tag.startsWith("pkb")) icon = "🧠";
        else if (tag.startsWith("cognitive") || tag.startsWith("learning")) icon = "🎓";
        else if (tag.startsWith("prompt") || tag.startsWith("llm")) icon = "🤖";
        else if (tag.startsWith("obsidian")) icon = "💎";
        
        // Replace slashes with arrows for readability
        let cleanText = tag.split("/").join("  ›  ");
        
        // Return the formatted string
        return `${icon} ${cleanText}`;
    });
}

// --- INPUT SYSTEM ---

// 1. Generate Display Arrays
const groupA_Display = formatTagsForDisplay(groupA_Tags);
const groupB_Display = formatTagsForDisplay(groupB_Tags);
const groupC_Display = formatTagsForDisplay(groupC_Tags);

// … [Title/Alias Prompts] …

// 2. Tag Suggesters (Using Display Array, Returning Real Tag)
// Syntax: tp.system.suggester(DISPLAY_LIST, REAL_VALUE_LIST)

const tag4 = await tp.system.suggester(groupC_Display, groupC_Tags, false, "Select Tag 04 (Group C):");
// (Repeat for tag5, tag6, etc.)

```
> [!to-implement]
> **(Visual "Pretty Print")**, you need to add a small helper function to your script and update how you call the `suggester`.
> 
> ### Here is exactly what you need to do.
> ##### Step 1: Locate the "Input System" Section
> 
> Scroll to the bottom of your script, right after the closing bracket `];` of the `groupC_Tags` array.
> 
> ##### Step 2: Replace the Bottom Section
> 
> **Delete everything** from the end of `groupC_Tags` down to the bottom of the file, and **paste this code block** in its place.
> 
> This code adds the icon logic (`formatTagsForDisplay`) and updates the suggesters to show you the "Pretty" version while inserting the "Real" tag into your note.

```javascript
// … [Your groupA_Tags, groupB_Tags, and groupC_Tags arrays are above here] …

// --- HELPER FUNCTION: PRETTY PRINT TAGS ---
// This function adds icons and arrows for the UI, but keeps the original tag for the file.
function formatTagsForDisplay(tags) {
    return tags.map(tag => {
        let icon = "🔹"; // Default bullet
        
        // 1. Assign Icons based on Domain Keywords
        if (tag.startsWith("pkm") || tag.startsWith("pkb") || tag.startsWith("note-taking")) icon = "🧠";
        else if (tag.startsWith("cognitive") || tag.startsWith("critical") || tag.startsWith("learning") || tag.startsWith("self")) icon = "🎓";
        else if (tag.startsWith("prompt") || tag.startsWith("llm") || tag.startsWith("advanced-prompting")) icon = "🤖";
        else if (tag.startsWith("obsidian")) icon = "💎";
        else if (tag.startsWith("type/")) icon = "📑";
        else if (tag.startsWith("status/")) icon = "🚦";
        else if (tag.startsWith("context/")) icon = "🌐";
        else if (tag.startsWith("source/")) icon = "📚";
        else if (tag.startsWith("maturity/")) icon = "🍷";
        else if (tag.startsWith("mode/")) icon = "⚙️";
        
        // 2. Formatting: Replace slashes with visual arrows
        // Example: "pkm/theory/foundations" BECOMES "🧠 pkm › theory › foundations"
        let cleanText = tag.split("/").join("  ›  ");
        
        return `${icon} ${cleanText}`;
    });
}

// --- INPUT SYSTEM ---

// 1. Prepare Display Arrays (What you SEE vs What you GET)
// We sort the tags alphabetically first so related items group together in the UI
const sortedA = groupA_Tags.sort();
const sortedB = groupB_Tags.sort();
const sortedC = groupC_Tags.sort();

const groupA_Display = formatTagsForDisplay(sortedA);
const groupB_Display = formatTagsForDisplay(sortedB);
const groupC_Display = formatTagsForDisplay(sortedC);

// 2. Text Prompts
const title = await tp.system.prompt("Enter Note Title (Concept Name):");
const alias1 = await tp.system.prompt("Enter Alias 1 (Press Enter to skip):");
const alias2 = await tp.system.prompt("Enter Alias 2 (Press Enter to skip):");

// 3. Metadata Suggesters
const type = await tp.system.suggester(typeList, typeList, false, "Select Note TYPE:");
const source = await tp.system.suggester(sourceList, sourceList, false, "Select SOURCE / ORIGIN:");
const linkUp = await tp.system.suggester(linkUpList, linkUpList, false, "Select LINK-UP MOC:");

// 4. Tag Suggesters (Hierarchical Selection)
// Syntax: await tp.system.suggester(DISPLAY_LIST, REAL_VALUE_LIST, throw_on_cancel, placeholder)

// Tag 01 & 02: High Level Domains (Group A)
const tag1 = await tp.system.suggester(groupA_Display, sortedA, false, "Select Tag 01 (Domain - Group A):");
const tag2 = await tp.system.suggester(groupA_Display, sortedA, false, "Select Tag 02 (Domain - Group A):");

// Tag 03: Sub-Domain (Group B)
const tag3 = await tp.system.suggester(groupB_Display, sortedB, false, "Select Tag 03 (Sub-Domain - Group B):");

// Tag 04 - 08: Granular Concepts (Group C)
// We use the Display list for the UI, but the code returns the Original Tag from the sorted list
const tag4 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 04 (Granular - Group C):");
const tag5 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 05 (Granular - Group C):");
const tag6 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 06 (Granular - Group C):");
const tag7 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 07 (Granular - Group C):");
const tag8 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 08 (Granular - Group C):");

// 5. Date Calculations
const dateNow = tp.date.now("YYYY-MM-DD");
const timeNow = tp.date.now("HH:mm:ss");
const year = tp.date.now("YYYY");
const id = tp.date.now("YYYYMMDDHHmmss");
_%>
```
> [!why-this-works]
> 1.  **Sorting:** I added `.sort()` to the arrays. This ensures that even if you pasted the tags in a random order in the code, `pkm/workflow/capture` will appear right next to `pkm/workflow/process` in the dropdown menu.
> 2.  **Display vs. Real:** The `tp.system.suggester` function takes two lists.
>       * List 1 (`groupC_Display`): Shows **"🧠 pkm › workflow › capture"**
>       * List 2 (`sortedC`): Actually types **"pkm/workflow/capture"** into your file.

### Visual Separators (The "Fake Header" Trick)
> [!info]
> - If you want distinct visual breaks between categories (e.g., between PKM and Prompt Engineering), you can inject "separator" lines into the array.

> [!danger]
> **Warning**: If you accidentally click a separator, it will try to output that line as a tag. You have to be careful not to select them.
```cs
// 1. Define Separators
const separator = "──────────────";

// 2. Create a Master List with Separators injected
// You would have to manually construct this or push arrays together
const groupC_WithHeaders = [
    --- PKM SECTION ${separator},
    …groupC_Tags.filter(t => t.startsWith("pkm")),
    
    --- COGNITIVE SECTION ${separator},
    …groupC_Tags.filter(t => t.startsWith("cognitive")),
    
    // etc…
];

// 3. Use in Suggester
const tag4 = await tp.system.suggester(groupC_WithHeaders, groupC_WithHeaders);
```

----

----
----
### Tag-Suggester-System
#### [Tag-Suggester-Group-A]-[Empty]
```cs
// Tag Suggester (Hierarchical Selection)

const groupA_Tags = [
    "", "", "", "", "", 
    "", "", "", 
    "", "", "", 
    "", "", "", 
    "", "", "", 
    "", "", "", 
    "", "", "", ""
];
```
```cs
// Tag Suggester (Hierarchical Selection)
// GROUP A: High-Level Domains (For Tags 01 & 02)

const tag1 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 01 (Domain):");
const tag2 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 02 (Domain):");
```
```cs
// Tag Placement in Note Body
// GROUP A: High-Level Domains
  - "<% tag1 %>"
  - "<% tag2 %>"
```
#### [Tag-Suggester-Group-B]-[Empty]
```cs
// Tag Suggester (Hierarchical Selection)
// GROUP B: Granular Concepts (For Tags 03, 04, & 05)

const groupB_Tags = [
    // PKM & PKB
	  "", "", "", 
    "", "", "",
	  "", "", "", 
    "", "", "",
	  "", "", "", 
    "", "", "",
    // Psychology & Cognitive
	  "", "", "", 
	  "", "", "", 
    "", "", "",
	  "", "", "", 
    "", "", "",
	  "", "", "", 
    "", "", "",
    // Prompt Engineering
	  "", "", "", 
    "", "", "",
	  "", "", "", 
    "", "", "",
	  "", "", "", 
    "", "", "",
 	  "", "", "", 
    "", "", "",
    // Cross-Cutting Concepts
    "concept/emergence", "concept/atomic-notes", "concept/transfer",
    "concept/first-principles", "concept/synthesis", "concept/flow-state"
];
```
```cs
// Tag Suggester (Hierarchical Selection)
// GROUP B: Granular Concepts (For Tags 03, 04, & 05)

const tag3 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 03 (Concept):");
const tag4 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 04 (Concept):");
const tag5 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 05 (Concept):");
const tag6 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 06 (Concept):");
const tag7 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 07 (Concept):");
const tag8 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 08 (Concept):");
```
```cs
// Tag Placement in Note Body
// GROUP B: Granular Concepts
  - "<% tag3 %>"
  - "<% tag4 %>"
  - "<% tag5 %>"
  - "<% tag6 %>"
  - "<% tag7 %>"
  - "<% tag8 %>"
```
### Middle Logic Section for 8 (Eight) Tags
```cs
// 3. Tag Suggesters (Hierarchical Selection)
// Tag 01 & 02: High Level Domains or Dimensions (Group A)
const tag1 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 01 (Domain/Dimension - Group A):");
const tag2 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 02 (Domain/Dimension - Group A):");
// Tag 03: Sub-Domain / Category (Group B)
const tag3 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 03 (Sub-Domain - Group B):");
const tag4 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 04 (Sub-Domain - Group B):");
// Tag 04 - 08: Granular Concepts / Specifics (Group C)
const tag5 = await tp.system.suggester(groupC_Tags, groupC_Tags, false, "Select Tag 05 (Granular Concept - Group C):");
const tag6 = await tp.system.suggester(groupC_Tags, groupC_Tags, false, "Select Tag 06 (Granular Concept - Group C):");
const tag7 = await tp.system.suggester(groupC_Tags, groupC_Tags, false, "Select Tag 07 (Granular Concept - Group C):");
const tag8 = await tp.system.suggester(groupC_Tags, groupC_Tags, false, "Select Tag 08 (Granular Concept - Group C):");
```

#### [Example]-[Tag-Suggester-Group-A]
```cs
// Tag Suggester (Hierarchical Selection)
// GROUP A: High-Level Domains (For Tags 01 & 02)

const groupA_Tags = [
    "pkm", "pkb", "note-taking", "knowledge-workflow", "obsidian", 
    "information-architecture", "knowledge-graph", "digital-garden", 
    "productivity", "cognitive-science", "critical-thinking", 
    "self-regulation", "learning-theory", "self-improvement", 
    "prompt-engineering", "prompting-technique", "prompt-pattern", 
    "llm-capability", "llm-architecture", "advanced-prompting", 
    "prompt-safety", "context-management", "prompt-workflow", "cosmology"
];
```
```cs
// Tag Suggester (Hierarchical Selection)
// GROUP A: High-Level Domains (For Tags 01 & 02)

const tag1 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 01 (Domain):");
const tag2 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 02 (Domain):");
```
```cs
// Tag Placement in Note Body
// GROUP A: High-Level Domains
  - "<% tag1 %>"
  - "<% tag2 %>"
```
#### [Example]-[Tag-Suggester-Group-B]
```cs
// Tag Suggester (Hierarchical Selection)
// GROUP B: Granular Concepts (For Tags 03, 04, & 05)

const groupB_Tags = [
    // PKM & PKB
    "pkm/theory", "pkm/methodology", "pkm/workflow", "pkb/architecture", 
    "pkb/design", "pkb/components", "note-taking/zettelkasten", 
    "obsidian/plugins", "obsidian/advanced", "knowledge-graph/theory",
    
    // Psychology & Cognitive
    "cognitive-science/metacognition", "cognitive-science/memory", 
    "cognitive-science/attention", "cognitive-science/mental-models",
    "critical-thinking/analysis", "critical-thinking/logic", 
    "self-regulation/goal-setting", "learning-theory/constructivism",
    "self-improvement/deliberate-practice", "self-improvement/mental-models",
    
    // Prompt Engineering
    "prompt-engineering/principles", "prompt-engineering/optimization",
    "prompting-technique/chain-of-thought", "prompting-technique/reasoning", 
    "prompting-technique/few-shot", "prompting-technique/meta-prompting",
    "prompt-pattern/persona", "prompt-pattern/context-control",
    "llm-capability/reasoning", "llm-architecture/transformer",
    "advanced-prompting/agents", "advanced-prompting/rag",
    "prompt-safety/alignment", "context-management/window",
    
    // Cross-Cutting Concepts
    "concept/emergence", "concept/atomic-notes", "concept/transfer",
    "concept/first-principles", "concept/synthesis", "concept/flow-state"
];
```
```cs
// Tag Suggester (Hierarchical Selection)
// GROUP B: Granular Concepts (For Tags 03, 04, & 05)

const tag3 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 03 (Concept):");
const tag4 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 04 (Concept):");
const tag5 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 05 (Concept):");
const tag6 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 06 (Concept):");
const tag7 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 07 (Concept):");
const tag8 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 08 (Concept):");
```
```cs
// Tag Placement in Note Body
// GROUP B: Granular Concepts
  - "<% tag3 %>"
  - "<% tag4 %>"
  - "<% tag5 %>"
  - "<% tag6 %>"
  - "<% tag7 %>"
  - "<% tag8 %>"
```

### Modular-Inserts
#### [Tag][Multi-Purpose]
```cs
["psychology", "psychology/educational", "psychology/cognitive", "informational-architecture", "pkb", "pkm", "planning", "prompt-engineering", "component-library", "project", "pkm/workflow", "pkb/infastucture", "pkm/workflow", "pkm/automation", "pkm/methodology", "education/pkb"],
["psychology", "psychology/educational", "psychology/cognitive", "informational-architecture", "pkb", "pkm", "planning", "prompt-engineering", "component-library", "project", "pkm/workflow", "pkm/automation", "pkm/methodology", "education", "education/pkb"],
```
```cs
["Psychology", "Philosophy", "Education", "PKM", "Methodology", "Prompt Engineering", "Critical-Thinking", "Project-Pur3v4d3r", "Source/Claude/Sonnet", "Source/Claude/Opus", "Source/Gemini"],
  ["psychology", "philosophy", "education", "pkm", "methodology", "prompt-engineering", "critical-thinking", "project-pur3v4d3r", "source/llm/clade/sonnet", "source/llm/claude/opus", "source/llm/gemini"],
```
#### [Source]-[LLM]
```cs
["source/llm", "source/pur3v4d3r", "source/llm/claude", "source/llm/claude/sonnet", "source/llm/claude/opus", "source/llm/gemini", "source/llm/chat", "source/reference"],
["source/llm", "source/pur3v4d3r", "source/llm/claude", "source/llm/claude/sonnet", "source/llm/claude/opus", "source/llm/gemini", "source/llm/chat", "source/reference"],
```
#### [Source]-[Pedagogy-Scaffolds]
```cs
["🌩️♊URG011", "", "", "🧱First-Principles-Claude", "Gemini-2.5-Pro", "Claude-4.5-Sonnet", "Claude-4.1-Opus", "⚛️Foundational-Gemini", "⚛️Foundational-Claude", "🕸️Systems-01"], 
    ["🌩️♊URG011_v1.1_🆔20251022221217", "🌩️🐲URG012_🆔20251023000722", "🧱first-principle-gemini", "🧱first-principles-claude", "gemini-2.5-pro", "claude-4.5-sonnet", "claude-4.1-opus", "⚛️foundational-gemini", "⚛️foundational-claude", "🕸️Systems-01"],
```
```c
🌩️♊URG011_v1.1_🆔20251022221217
🌩️🐲URG012_🆔20251023000722

🧱First-Prin-01
🧱First-Prin-02
📖Narrative-01
📖Narrative-02
🏛️Socratic-01
🏛️Socratic-02
🕸️Systems-01
🕸️Systems-02

🧱First-Principles-01
🧱First-Principles-02
📖Narrative-Driven-01
📖Narrative-Driven-02
🏛️Socratic-Inquiry-01
🏛️Socratic-Inquiry-02
🕸️Systems-Thinking-01
🕸️Systems-Thinking-02

🌗Comparative-Analysis-01
🌗Comparative-Analysis-02
🔬Case-Study-Method-01
🔬Case-Study-Method-02
⚙️Problem-Based-01
⚙️Problem-Based-02
⚖️The-Socratic-Synthesis-01
⚖️The-Socratic-Synthesis-02
```
#### [Type]-[Reports]
```
<%* const choice = await tp.system.suggester(["cog-psy/report", "pkb/pkm/report", "prompt/report","cosmo/report","edu/report", "report"], ["cog-psy/report", "pkb/pkm/report", "prompt/report","cosmo/report","edu/report", "report"], "Choose one:") tR += `${choice}` %>
```
#### [Type]-[Note]
```cs
<%* const type = await tp.system.suggester (["Reference", "LLM Chat", "Fleeting Thought", "literature Note", "MOC", "Project", "Template", "Other"], ["reference", "llm-chat", "fleeting", "literature-note", "moc", "project", "template", "other"], false, "Choose the Type:") %>
```
#### [Source]-[LLM]
```c
<% await tp.system.suggester(["Gemini-Pro", "Gemini-Flash", "Claude", "🦖Pur3v4d3r", "ChatGPT"], ["gemini-2.5-pro", "gemini-2.5-flash", "claude", "🦖pur3v4d3r", "chatgpt"], false, "Choose one:") %>
```














#### [User-Prompt][Alias]
```c
const alias1 = await tp.system.prompt("Enter first alias (or press Enter to skip):");
const alias2 = await tp.system.prompt("Enter second alias (or press Enter to skip):");
```






# Reviews
```
---
type: weekly-review
date: <% tp.date.now("YYYY-MM-DD") %>
week: <% tp.date.now("gggg-[W]WW") %>
month: <% tp.date.now("YYYY-MM") %>
quarter: <% tp.date.now("YYYY-[Q]Q") %>
year: <% tp.date.now("YYYY") %>
status: draft
tags: [#weekly-review, #gtd, #planning]
---

# Week <% tp.date.now("WW") %>: <% tp.date.now("MMMM DD") %> - <% tp.date.now("MMMM DD", 6, tp.file.title, "gggg-[W]WW") %>

← [[<% tp.date.now("gggg-[W]WW", -7) %>|Last Week]] | [[<% tp.date.now("gggg-[W]WW", 7) %>|Next Week]] →
📅 [[<% tp.date.now("YYYY-MM") %>|This Month]] | [[<% tp.date.now("YYYY-[Q]Q") %>|This Quarter]]

---
---
type: monthly-review
date: <% tp.date.now("YYYY-MM-DD") %>
month: <% tp.date.now("YYYY-MM") %>
quarter: <% tp.date.now("YYYY-[Q]Q") %>
year: <% tp.date.now("YYYY") %>
status: draft
tags: [#monthly-review, #reflection, #planning]
---

# <% tp.date.now("MMMM YYYY") %> Review

← [[<% tp.date.now("YYYY-MM", -1, tp.file.title, "YYYY-MM") %>|Last Month]] | [[<% tp.date.now("YYYY-MM", 1, tp.file.title, "YYYY-MM") %>|Next Month]] →
📅 [[<% tp.date.now("YYYY-[Q]Q") %>|This Quarter]] | [[<% tp.date.now("YYYY") %>|This Year]]

---
---
type: monthly-review
date: <% tp.date.now("YYYY-MM-DD") %>
month: <% tp.date.now("YYYY-MM") %>
quarter: <% tp.date.now("YYYY-[Q]Q") %>
year: <% tp.date.now("YYYY") %>
status: draft
tags: [#monthly-review, #reflection, #planning]
---

# <% tp.date.now("MMMM YYYY") %> Review

← [[<% tp.date.now("YYYY-MM", -1, tp.file.title, "YYYY-MM") %>|Last Month]] | [[<% tp.date.now("YYYY-MM", 1, tp.file.title, "YYYY-MM") %>|Next Month]] →
📅 [[<% tp.date.now("YYYY-[Q]Q") %>|This Quarter]] | [[<% tp.date.now("YYYY") %>|This Year]]

---
---
type: quarterly-review
date: <% tp.date.now("YYYY-MM-DD") %>
quarter: <% tp.date.now("YYYY-[Q]Q") %>
year: <% tp.date.now("YYYY") %>
status: draft
tags: [#quarterly-review, #strategy, #okr]
---

# Q<% tp.date.now("Q YYYY") %> Review

← [[<% tp.date.now("YYYY-[Q]Q", -3, tp.file.title, "YYYY-[Q]Q") %>|Last Quarter]] | [[<% tp.date.now("YYYY-[Q]Q", 3, tp.file.title, "YYYY-[Q]Q") %>|Next Quarter]] →
📅 [[<% tp.date.now("YYYY") %>|This Year]]

---
---
type: annual-review
date: <% tp.date.now("YYYY-MM-DD") %>
year: <% tp.date.now("YYYY") %>
status: draft
tags: [#annual-review, #life-reflection, #planning]
---

# <% tp.date.now("YYYY") %> Annual Review

← [[<% tp.date.now("YYYY", -1, tp.file.title, "YYYY") %>|Last Year]] | [[<% tp.date.now("YYYY", 1, tp.file.title, "YYYY") %>|Next Year]] →
---

```



















### [Full-Templates]

#### [Example]-[Creating-a-Dynamic-Zettelkasten-Note]
```
<%*
// 1. Create a unique ID based on the current datetime
const uid = tp.date.now("YYYYMMDDHHmmss")
// 2. Prompt the user for a title
const title = await tp.system.prompt("Enter note title:")
// 3. Rename the file to match the UID and Title
await tp.file.rename(`${uid} - ${title}`)
// 4. Build the output string
let output = ""
output += `# ${title}\n\n`
output += `**ID:** ${uid}\n`
output += `**Tags:** #zettel \n`
output += `**Created:** ${tp.date.now("YYYY-MM-DD @ HH:mm")}\n\n`
output += "## Note\n\n"
output += `<% tp.file.cursor() %>\n\n` // Place cursor here
output += "## Connections\n"
// 5. Send the final string to the template result
tR = output
%>
```




