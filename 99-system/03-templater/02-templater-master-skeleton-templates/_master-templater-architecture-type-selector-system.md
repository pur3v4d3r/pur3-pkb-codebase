<%*
/**
MASTER PROMPT ARCHITECTURE: TYPE SELECTOR SYSTEM
Defines available Note Types.
Prompts user for selection via Suggester.
Generates YAML Frontmatter.
Injects a pre-filled Dataview query specific to that selection.
*/
// --- CONFIGURATION ZONE ---
// Define the display names and values for your types
const typeOptions = ["Concept", "Reference", "Person", "Project", "Meeting"];
const typeValues  = ["Concept", "Reference", "Person", "Project", "Meeting"];
// --- SYSTEM EXECUTION ---
// prompt the user (Display Options, Return Values, Throw on Cancel?, Placeholder)
const selectedType = await tp.system.suggester(
typeOptions,
typeValues,
false,
"Select the Note Type:"
);
// --- GUARD CLAUSE ---
// If the user presses ESC, stop execution to prevent creating a broken note.
if (!selectedType) {
new Notice("Template cancelled: No type selected.");
return;
}
// --- OUTPUT GENERATION --- // We use tR (Template Response) to write the file content dynamically. // This ensures the variable 'selectedType' is fully resolved before writing. _%>
type: "<% selectedType %>"
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
tags:
status/seed
<% selectedType %> Dashboard
---

[!abstract] System Context
This view aggregates all notes linked to this file (FROM [[]]) that match the <% selectedType %> classification.

```
TABLE maturity, confidence, file.folder as "Location"
FROM [[]]
WHERE type = "<% selectedType %>"
SORT maturity DESC
LIMIT 10
```
