---
## Theme: **Knowledge Management**

---



## Basic Templates
*These templates demonstrate fundamental Templater operations for creating and organizing knowledge notes.*
pkb-automation-
---
### 1. Basic Note Template with Metadata
*A simple template that auto-generates frontmatter with the note title, creation date, and default metadata fields.*
```
---
title: <% tp.file.title %>
created: <% tp.date.now("YYYY-MM-DD") %>
type: permanent-note
maturity: seedling
status: active
tags: []
---
# <% tp.file.title %>
## Summary
## Key Points
## Related Notes
```

---
### 2. Daily Note Starter
*A minimal daily note template that includes the date and a prompt for daily reflections.*
```
---
title: <% tp.date.now("YYYY-MM-DD") %>
type: daily-note
created: <% tp.date.now("YYYY-MM-DD") %>
tags: [daily]
---
# <% tp.date.now("YYYY-MM-DD") %>
## Today's Focus
## Notes
## Reflection
```

---
### 3. MOC (Map of Content) Template
*A template for creating a Map of Content note with auto-generated frontmatter and structure.*
```
---
title: <% tp.file.title %>
type: moc
created: <% tp.date.now("YYYY-MM-DD") %>
status: active
tags: [moc]
---
# <% tp.file.title %>
## Overview
## Core Concepts
## Related Notes
```

---
### 4. Literature Note Template
*A template for capturing insights from literature with structured metadata.*
```
---
title: <% tp.file.title %>
type: literature
created: <% tp.date.now("YYYY-MM-DD") %>
source: 
author: 
year: 
tags: [literature]
---
# <% tp.file.title %>
## Summary
## Key Quotes
## Insights
## Related Notes
```

---
## Intermediate Templates
*These templates introduce conditional logic, user prompts, and dynamic content generation.*

---
### 1. Smart Permanent Note Creator
*Prompts the user for note type and maturity, then generates a tailored template with appropriate structure.*
```
<%*
const noteType = await tp.system.prompt("Note Type (permanent-note, concept, principle, etc.):");
const maturity = await tp.system.prompt("Maturity (seedling, developing, evergreen):");
%>
---
title: <% tp.file.title %>
type: <% noteType %>
created: <% tp.date.now("YYYY-MM-DD") %>
maturity: <% maturity %>
status: active
tags: [<% noteType %>]
---
# <% tp.file.title %>
<%* if (noteType === "concept") { %>
## Definition
## Examples
## Related Concepts
<%* } else if (noteType === "principle") { %>
## Core Idea
## Applications
## Related Principles
<%* } else { %>
## Summary
## Key Points
## Related Notes
<%* } %>
```

---
### 2. Dynamic MOC Link Generator
*Automatically links to related MOCs based on user selection from a predefined list.*
```
<%*
const mocLinks = [
  "[[artificial-intelligence-moc]]",
  "[[cognitive-science-moc]]",
  "[[learning-theory-moc]]",
  "[[prompt-engineering-moc]]"
];
const selectedMOCs = await tp.system.suggester(mocLinks, mocLinks, true, "Select related MOCs:");
const linkString = selectedMOCs ? selectedMOCs.join("\n- ") : "";
%>
---
title: <% tp.file.title %>
type: permanent-note
created: <% tp.date.now("YYYY-MM-DD") %>
link-up: 
  <%* if (selectedMOCs) { %>
  <% selectedMOCs.map(moc => `- ${moc}`).join("\n  ") %>
  <%* } %>
tags: []
---
# <% tp.file.title %>
## Summary
## Key Points
## Related Notes
```

---
### 3. Multi-File Reference Note Creator
*Creates a main note and a companion literature note, linking them together.*
```
<%*
const mainTitle = tp.file.title;
const litNoteTitle = mainTitle + " - Literature Note";
const author = await tp.system.prompt("Author:");
const source = await tp.system.prompt("Source:");
// Create literature note
const litNoteContent = `---
title: ${litNoteTitle}
type: literature
created: ${tp.date.now("YYYY-MM-DD")}
author: ${author}
source: ${source}
tags: [literature]
---
# ${litNoteTitle}
## Summary
## Key Quotes
## Insights
## Related Notes
`;
await tp.file.create_new(litNoteContent, litNoteTitle, false, tp.file.folder(true) + "/04-library");
%>
---
title: <% mainTitle %>
type: permanent-note
created: <% tp.date.now("YYYY-MM-DD") %>
related-literature: [[<% litNoteTitle %>]]
tags: []
---
# <% mainTitle %>
## Summary
## Key Points
## Related Notes
- [[<% litNoteTitle %>]]
```

---
### 4. Context-Aware Dashboard Generator
*Creates a dashboard note that dynamically pulls in related notes using Dataview-style placeholders.*
````
<%*
const dashboardType = await tp.system.prompt("Dashboard Type (AI, Cognitive Science, Learning, etc.):");
%>
---
title: <% dashboardType %> Dashboard
type: dashboard
created: <% tp.date.now("YYYY-MM-DD") %>
focus-area: <% dashboardType.toLowerCase().replace(" ", "-") %>
tags: [dashboard, <% dashboardType.toLowerCase().replace(" ", "-") %>]
---
# <% dashboardType %> Dashboard
## Overview
## Recent Notes
```dataview
LIST FROM "03-notes" WHERE contains(tags, "#<% dashboardType.toLowerCase().replace(" ", "-") %>")
SORT created DESC
LIMIT 5
```
## In Progress
```dataview
LIST FROM "03-notes" WHERE contains(status, "active") AND contains(tags, "#<% dashboardType.toLowerCase().replace(" ", "-") %>")
```
## To Review
```dataview
LIST FROM "03-notes" WHERE contains(maturity, "needs-review") AND contains(tags, "#<% dashboardType.toLowerCase().replace(" ", "-") %>")
```
````

---
## Advanced Templates
*These templates showcase expert-level Templater capabilities including user scripts, web integration, and complex automation.*

---
### Advanced Template 1: AI-Powered Concept Synthesis Engine
**Description**: This template creates a new concept note by synthesizing information from multiple existing notes. It prompts the user for related concepts, fetches their content, uses a web API to generate a synthesized summary, and creates a new permanent note with AI-generated insights.
**Top Use Cases**:
1. Creating synthesis notes that bridge multiple knowledge domains
2. Generating literature review summaries from multiple sources
3. Automating the creation of interdisciplinary concept maps
**Implementation Tips**:
- Requires the `tp.web` module to be enabled
- Uses a placeholder for API integration (replace with your preferred AI service)
- Handles missing files gracefully with error checking
- Creates backlinks in source notes to the new synthesis
**Customization Options**:
1. Replace the web API call with your preferred AI service (OpenAI, Claude, etc.)
2. Modify the prompt to focus on different types of synthesis (comparison, contrast, integration)
3. Add automatic tagging based on source note categories
```
<%*
// Prompt for related concepts
const conceptList = await tp.system.prompt("Enter related concepts (comma-separated):");
const concepts = conceptList.split(",").map(c => c.trim());
// Fetch content from related notes
let combinedContent = "";
let backlinkText = "";
for (const concept of concepts) {
  try {
    const file = tp.file.find_tfile(concept);
    if (file) {
      const content = await tp.file.content(file);
      combinedContent += `## ${concept}\n${content}\n\n`;
      backlinkText += `- [[${tp.file.title}]]\n`;
    }
  } catch (e) {
    console.warn(`Could not find note: ${concept}`);
  }
}
// Generate synthesis using web API (placeholder - replace with your AI service)
const prompt = `Synthesize the following concepts into a coherent summary that identifies connections, contrasts, and emergent insights:\n\n${combinedContent}`;
const synthesis = await tp.web.daily_quote(); // Placeholder - replace with actual API call
// Create the new synthesis note
const newContent = `---
title: <% tp.file.title %>
type: concept
created: <% tp.date.now("YYYY-MM-DD") %>
synthesis-of: [${concepts.map(c => `"${c}"`).join(", ")}]
maturity: developing
status: active
tags: [synthesis, concept]
---
# <% tp.file.title %>
## Synthesis
${synthesis}
## Related Concepts
${concepts.map(c => `- [[${c}]]`).join("\n")}
## Backlinks
`;
await tp.file.create_new(newContent, tp.file.title, false, tp.file.folder(true) + "/03-notes");
// Add backlinks to source notes
for (const concept of concepts) {
  try {
    const file = tp.file.find_tfile(concept);
    if (file) {
      const content = await tp.file.content(file);
      const updatedContent = content + `\n\n## Backlinks\n- [[${tp.file.title}]]`;
      await tp.file.modify(file, updatedContent);
    }
  } catch (e) {
    console.warn(`Could not update note: ${concept}`);
  }
}
%>
```

---
### Advanced Template 2: Automated Knowledge Base Health Report
**Description**: This template generates a comprehensive health report for your PKB by analyzing note metadata, identifying gaps, and providing actionable recommendations. It scans your entire vault, aggregates statistics, and creates a detailed dashboard note with findings.
**Top Use Cases**:
1. Monthly PKB maintenance and optimization
2. Identifying neglected knowledge areas for review
3. Tracking the evolution of your knowledge base maturity
**Implementation Tips**:
- Uses Dataview-style queries through Templater's file system access
- Requires a well-structured tagging system to be effective
- Generates both summary statistics and detailed recommendations
- Can be scheduled to run automatically with Tasker or similar tools
**Customization Options**:
1. Adjust maturity thresholds and recommendations based on your workflow
2. Add additional health metrics (link density, orphaned notes, etc.)
3. Customize the report format for integration with other tools
```
<%*
// Initialize counters
let totalNotes = 0;
let byType = {};
let byMaturity = {};
let byStatus = {};
let needsReview = 0;
let orphaned = 0;
// Scan all notes in the vault
const files = tp.file.files();
for (const file of files) {
  if (file.extension === "md" && !file.path.includes("00-meta") && !file.path.includes("99-")) {
    totalNotes++;
    const content = await tp.file.content(file);
    // Extract frontmatter
    const frontmatter = tp.frontmatter;
    // Count by type
    const type = frontmatter.type || "untyped";
    byType[type] = (byType[type] || 0) + 1;
    // Count by maturity
    const maturity = frontmatter.maturity || "untyped";
    byMaturity[maturity] = (byMaturity[maturity] || 0) + 1;
    // Count by status
    const status = frontmatter.status || "untyped";
    byStatus[status] = (byStatus[status] || 0) + 1;
    // Check for notes needing review
    if (maturity === "needs-review") {
      needsReview++;
    }
    // Check for orphaned notes (no links in or out)
    // This is a simplified check - in practice you'd want to parse [[links]]
    if (!content.includes("[[")) {
      orphaned++;
    }
  }
}
// Generate recommendations
let recommendations = [];
if (needsReview > totalNotes * 0.1) {
  recommendations.push("- High number of notes needing review - consider scheduling regular review sessions");
}
if (orphaned > totalNotes * 0.05) {
  recommendations.push("- Significant number of orphaned notes - review linking strategy");
}
if (!byType["permanent-note"] || byType["permanent-note"] < totalNotes * 0.3) {
  recommendations.push("- Low percentage of permanent notes - focus on converting literature notes");
}
// Create health report
const reportContent = `---
title: PKB Health Report - <% tp.date.now("YYYY-MM-DD") %>
type: pkb-report
created: <% tp.date.now("YYYY-MM-DD") %>
status: active
tags: [pkb-report, health-check]
---
# PKB Health Report - <% tp.date.now("YYYY-MM-DD") %>
## Summary
- Total Notes: ${totalNotes}
- Notes Needing Review: ${needsReview}
- Orphaned Notes: ${orphaned}
## Distribution by Type
${Object.entries(byType).map(([type, count]) => `- ${type}: ${count}`).join("\n")}
## Distribution by Maturity
${Object.entries(byMaturity).map(([maturity, count]) => `- ${maturity}: ${count}`).join("\n")}
## Distribution by Status
${Object.entries(byStatus).map(([status, count]) => `- ${status}: ${count}`).join("\n")}
## Recommendations
${recommendations.join("\n")}
## Detailed Analysis
- **Growth Rate**: Compare with previous reports
- **Link Density**: Average links per note
- **MOC Coverage**: Percentage of notes linked to MOCs
- **Tag Consistency**: Most common tags and gaps
`;
%>
```

---
## Synergy Templates (Plugin Integration)
*These templates demonstrate powerful integrations with other Obsidian plugins to create enhanced workflows.*

---
### Synergy Template 1: QuickAdd + Templater Research Capture
**Description**: This template integrates with QuickAdd to create a powerful research capture workflow. It prompts for source information, creates a literature note, and adds it to a Dataview-powered reading list dashboard.
**Top Use Cases**:
1. Capturing research papers and articles during literature reviews
2. Creating a centralized reading list with status tracking
3. Automating the initial processing of new sources
**Implementation Tips**:
- Requires QuickAdd plugin with capture functionality
- Uses Dataview for dynamic reading list generation
- Automatically tags notes based on source type
- Creates backlinks to a master reading dashboard
**Customization Options**:
1. Add more source types (books, videos, podcasts) with different templates
2. Integrate with reference managers via Zotero or other plugins
3. Add automatic tagging based on keywords in the source title
```
<%*
// This template is designed to be called from QuickAdd with pre-filled variables
// QuickAdd can pass in: sourceTitle, sourceAuthor, sourceType, sourceUrl
const title = tp.user.sourceTitle || await tp.system.prompt("Source Title:");
const author = tp.user.sourceAuthor || await tp.system.prompt("Author:");
const type = tp.user.sourceType || await tp.system.suggester(["Article", "Book", "Paper"], ["article", "book", "paper"]);
const url = tp.user.sourceUrl || await tp.system.prompt("URL (optional):", "");
const noteTitle = `${author} - ${title}`;
const today = tp.date.now("YYYY-MM-DD");
// Determine tags based on source type
let tags = "#type/literature";
if (type === "paper") tags += " #type/research-paper";
if (type === "book") tags += " #type/book";
if (type === "article") tags += " #type/article";
// Create the literature note
const content = `---
title: ${noteTitle}
type: literature
created: ${today}
author: ${author}
source-type: ${type}
source-url: ${url}
status: unread
tags: [${tags}]
---
# ${noteTitle}
## Source Information
- Author: ${author}
- Type: ${type}
- URL: ${url}
## Summary
## Key Quotes
## Insights
## Related Notes
## Processing Log
- Added to library: ${today}
`;
await tp.file.create_new(content, noteTitle, false, tp.file.folder(true) + "/04-library");
// Update reading dashboard
const dashboardFile = tp.file.find_tfile("Reading Dashboard");
if (dashboardFile) {
  const dashboardContent = await tp.file.content(dashboardFile);
  const updatedContent = dashboardContent.replace(
    "## Current Reading\n", 
    `## Current Reading\n- [[${noteTitle}]]\n`
  );
  await tp.file.modify(dashboardFile, updatedContent);
}
%>
```

---
### Synergy Template 2: Dataview + Templater Dynamic MOC Generator
**Description**: This template automatically generates Maps of Content by querying Dataview for related notes and creating structured overviews. It identifies notes with common tags or links and synthesizes them into a navigable knowledge hub.
**Top Use Cases**:
1. Automatically generating MOCs for new knowledge domains
2. Creating dynamic overviews that update as new notes are added
3. Identifying knowledge gaps in existing MOCs
**Implementation Tips**:
- Requires Dataview plugin for querying capabilities
- Uses Templater's file system access to read note content
- Automatically updates existing MOCs or creates new ones
- Handles both tag-based and link-based clustering
**Customization Options**:
1. Adjust query parameters to focus on different relationship types
2. Add automatic generation of concept maps or other visualizations
3. Integrate with graph view plugins for enhanced navigation
```
<%*
// This template generates a MOC based on Dataview queries
const mocTopic = await tp.system.prompt("MOC Topic (e.g., AI, Cognitive Science):");
const topicTag = mocTopic.toLowerCase().replace(/\s+/g, "-");
// Query Dataview for related notes (simulated - in practice use tp.user.dataview)
// This would typically be: const relatedNotes = await tp.user.dataview("path:03-notes #${topicTag}")
// For demonstration, we'll simulate the query results
const relatedNotes = [
  {file: {name: "Neural Networks"}, tags: ["#ai", "#machine-learning"]},
  {file: {name: "Deep Learning"}, tags: ["#ai", "#neural-networks"]},
  {file: {name: "Reinforcement Learning"}, tags: ["#ai", "#machine-learning"]}
];
// Generate MOC content
const mocContent = `---
title: ${mocTopic} Map of Content
type: moc
created: <% tp.date.now("YYYY-MM-DD") %>
topic: ${topicTag}
status: active
tags: [moc, ${topicTag}]
---
# ${mocTopic} Map of Content
## Overview
This Map of Content organizes key concepts and resources related to ${mocTopic}.
## Core Concepts
${relatedNotes.map(note => `- [[${note.file.name}]]`).join("\n")}
## By Subtopic
${[...new Set(relatedNotes.flatMap(note => note.tags.filter(tag => tag !== "#ai")))]
  .map(tag => `\n### ${tag.replace("#", "").replace("-", " ").toUpperCase()}\n` +
    relatedNotes.filter(note => note.tags.includes(tag))
      .map(note => `- [[${note.file.name}]]`)
      .join("\n")
  ).join("\n")}
## Recent Additions
${relatedNotes.slice(0, 3).map(note => `- [[${note.file.name}]]`).join("\n")}
## Related MOCs
`;
%>
```


---
## Basic Templates
These templates demonstrate the foundational elements of Templater, including variable insertion, date formatting, and frontmatter generation. They're ideal for getting started with automated note creation.

---
### Template 1: Basic Prompt Engineering Note Template
This template creates a simple prompt engineering note with standard metadata fields and current timestamp.
```
---
type: prompt
source: <% tp.system.prompt("AI Model", "claude-opus-4.1") %>
maturity: seedling
confidence: provisional
status: active
priority: medium
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
tags: 
  - #prompt-engineering
  - #status/seedling
---
# <% tp.file.title %>
## Objective
## Context
## Instructions
## Expected Output
## Notes
```

---
### Template 2: Daily Prompt Review Template
Creates a daily review note for tracking prompt performance and iterations.
```
---
type: prompt-report
date: <% tp.date.now("YYYY-MM-DD") %>
related-prompts: []
status: active
tags:
  - #prompt-engineering
  - #type/report
  - #status/in-progress
---
# Prompt Review - <% tp.date.now("YYYY-MM-DD") %>
## Prompts Tested Today
## Performance Metrics
- Accuracy: 
- Relevance: 
- Creativity: 
- Efficiency: 
## Key Insights
## Next Iterations
## Resources
```

---
### Template 3: Prompt Component Template
A modular template for creating reusable prompt components.
```
---
type: prompt
subtype: component
category: <% tp.system.prompt("Component Category", "reasoning") %>
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #prompt-engineering
  - #modular-prompt
---
# <% tp.file.title %>
## Purpose
[Describe what this component does]
## Usage
[Describe how to use this component]
## Parameters
- [List any parameters needed]
## Example Implementation
```

---
### Template 4: Simple Prompt Template with Context
A straightforward template for capturing prompts with contextual information.
```
---
type: prompt
domain: <% tp.system.prompt("Domain", "general") %>
complexity: <% tp.system.prompt("Complexity", "medium") %>
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #prompt-engineering
  - #<% tp.frontmatter.domain %>
---
# <% tp.file.title %>
## Context
Created on: <% tp.date.now("YYYY-MM-DD HH:mm") %>
Domain: [[<% tp.frontmatter.domain %>]]
Complexity: <% tp.frontmatter.complexity %>
## Prompt
## Expected Output
## Notes
```

---
## Intermediate Templates
These templates introduce conditional logic, loops, and user interaction to create more dynamic and context-aware templates.

---
### Template 1: Adaptive Prompt Template Generator
This template dynamically generates different prompt structures based on user-selected type and includes conditional sections.
```
<%*
const promptType = await tp.system.prompt("Prompt Type", "analysis");
const complexity = await tp.system.prompt("Complexity Level", "medium");
const includeExamples = await tp.system.prompt("Include Examples? (y/n)", "y");
%>
---
type: prompt
prompt-type: <% promptType %>
complexity: <% complexity %>
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #prompt-engineering
  - #type/<% promptType %>
  - #complexity/<% complexity %>
---
# <% tp.file.title %>
## Role
<%* if (promptType === "analysis") { %>
You are an expert analyst specializing in breaking down complex information.
<%* } else if (promptType === "creative") { %>
You are a creative genius with the ability to generate innovative ideas.
<%* } else { %>
You are a helpful AI assistant with expertise in <% promptType %>.
<%* } %>
## Task
<% tp.system.prompt("Describe the task") %>
## Context
Created: <% tp.date.now("YYYY-MM-DD") %>
Type: <% promptType %>
Complexity: <% complexity %>
<%* if (includeExamples.toLowerCase() === "y") { %>
## Examples
1. <% tp.system.prompt("Example 1") %>
2. <% tp.system.prompt("Example 2") %>
<%* } %>
## Instructions
<% tp.system.prompt("Detailed instructions") %>
## Constraints
<% tp.system.prompt("Constraints or limitations") %>
## Output Format
<% tp.system.prompt("Expected output format") %>
```

---
### Template 2: Multi-Prompt Project Template
Creates a comprehensive prompt engineering project with multiple related prompts and tracking metadata.
```
<%*
const projectName = await tp.system.prompt("Project Name");
const projectDomain = await tp.system.prompt("Domain", "general");
const numPrompts = parseInt(await tp.system.prompt("Number of prompts to create", "3"));
const promptNames = [];
for (let i = 1; i <= numPrompts; i++) {
  promptNames.push(await tp.system.prompt(`Prompt ${i} Name`));
}
%>
---
type: prompt-project
project-name: <% projectName %>
domain: <% projectDomain %>
prompt-count: <% numPrompts %>
status: active
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #prompt-engineering
  - #project/<% projectName.toLowerCase().replace(/\s+/g, '-') %>
---
# <% projectName %> Prompt Engineering Project
## Project Overview
Domain: [[<% projectDomain %>]]
Created: <% tp.date.now("YYYY-MM-DD") %>
Status: Active
## Prompts in this Project
<%* for (let i = 0; i < promptNames.length; i++) { %>
- [[<% promptNames[i] %>]]
<%* } %>
## Project Goals
## Implementation Timeline
## Success Metrics
## Resources & References
```

---
### Template 3: Prompt Evaluation Template with Scoring
This template creates a structured evaluation framework for testing and scoring prompts.
```
<%*
const promptName = await tp.system.prompt("Prompt Name");
const evaluator = await tp.system.prompt("Evaluator Name", tp.config.username);
const testCases = parseInt(await tp.system.prompt("Number of test cases", "3"));
%>
---
type: prompt-evaluation
prompt: [[<% promptName %>]]
evaluator: <% evaluator %>
date: <% tp.date.now("YYYY-MM-DD") %>
status: in-progress
tags:
  - #prompt-engineering
  - #evaluation
  - #<% promptName.toLowerCase().replace(/\s+/g, '-') %>
---
# Prompt Evaluation: <% promptName %>
## Evaluation Details
- Evaluator: <% evaluator %>
- Date: <% tp.date.now("YYYY-MM-DD") %>
- Prompt: [[<% promptName %>]]
## Scoring Criteria
Scale: 1-5 (1=Poor, 3=Average, 5=Excellent)
<%* for (let i = 1; i <= testCases; i++) { %>
### Test Case <% i %>
Prompt: <% tp.system.prompt(`Test Case ${i} Prompt`) %>
Response: <% tp.system.prompt(`Test Case ${i} Response`) %>
Evaluation:
- Accuracy: <% tp.system.prompt("Accuracy (1-5)", "3") %>
- Relevance: <% tp.system.prompt("Relevance (1-5)", "3") %>
- Clarity: <% tp.system.prompt("Clarity (1-5)", "3") %>
- Creativity: <% tp.system.prompt("Creativity (1-5)", "3") %>
Notes: <% tp.system.prompt(`Test Case ${i} Notes`) %>

---
<%* } %>
## Overall Assessment
Strengths:
Weaknesses:
Recommendations:
Final Score: <% tp.system.prompt("Overall Score (1-5)", "3") %> / 5
```

---
## Advanced Templates
These sophisticated templates showcase expert-level Templater capabilities including user scripts, complex automation workflows, and multi-file operations.

---
### Advanced Template 1: Modular Prompt Builder System
**Description:** This template creates an entire prompt engineering framework with component-based architecture. It generates a master prompt file along with individual component files, establishes linking relationships, and creates a documentation dashboard. The system allows users to build complex prompts by combining modular components like role definitions, task descriptions, and output formats.
**Top Use Cases:**
1. Building a library of reusable prompt components for consistent AI interactions
2. Creating complex multi-step prompting workflows with version-controlled components
3. Establishing a team-based prompt engineering system with shared components
**Implementation Tips:**
- Store component templates in a dedicated folder structure (e.g., `/03-notes/prompt-components/`)
- Use consistent naming conventions for components to enable easy discovery
- Implement a versioning system for components to track improvements over time
- Consider using Dataview queries in the dashboard to dynamically show component usage
**Customization Options:**
1. Add category-based organization by modifying the folder structure generation
2. Implement dependency tracking between components using backlinks
3. Extend to include automated testing of component combinations
```
<%*
// Main prompt information
const promptName = await tp.system.prompt("Main Prompt Name");
const description = await tp.system.prompt("Prompt Description");
const domain = await tp.system.prompt("Domain", "general");
// Component selection
const components = [];
const componentTypes = ["role", "task", "context", "constraints", "output-format"];
for (const type of componentTypes) {
  const componentName = await tp.system.prompt(`Component for ${type} (or leave blank)`);
  if (componentName) {
    components.push({
      type: type,
      name: componentName,
      content: await tp.system.prompt(`Content for ${type} component`)
    });
  }
}
// Create component files
const componentLinks = [];
for (const component of components) {
  const componentFileName = `${component.name.replace(/\s+/g, '-')}-${component.type}`;
  const componentPath = `03-notes/prompt-components/${componentFileName}.md`;
  // Create component file
  const componentContent = `---
type: prompt-component
component-type: ${component.type}
related-prompt: [[${promptName}]]
created: ${tp.date.now("YYYY-MM-DD")}
tags:
  - #prompt-engineering
  - #component/${component.type}
---
# ${component.name} (${component.type})
## Content
${component.content}
## Usage
This component is used in [[${promptName}]]`;
  await tp.file.create_new(componentContent, componentFileName, false, "03-notes/prompt-components");
  componentLinks.push(`[[${componentFileName}]]`);
}
// Create main prompt file
const mainPromptContent = `---
type: prompt
subtype: modular
domain: ${domain}
components: [${componentLinks.join(', ')}]
created: ${tp.date.now("YYYY-MM-DD")}
status: active
tags:
  - #prompt-engineering
  - #modular-prompt
  - #domain/${domain}
---
# ${promptName}
## Description
${description}
## Components
<%* for (const component of components) { %>
### ${component.type.charAt(0).toUpperCase() + component.type.slice(1)}
[[${component.name.replace(/\s+/g, '-')}-${component.type}]]
<% } %>
## Full Prompt Construction
<%* for (const component of components) { %>
${component.content}
<% } %>
## Usage Instructions
## Version History
- ${tp.date.now("YYYY-MM-DD")}: Initial creation`;
await tp.file.create_new(mainPromptContent, promptName, false, "03-notes");
// Create dashboard
const dashboardContent = `---
type: dashboard
dashboard-type: prompt-components
domain: ${domain}
created: ${tp.date.now("YYYY-MM-DD")}
tags:
  - #prompt-engineering
  - #dashboard
---
# Prompt Component Dashboard: ${domain}
## Overview
This dashboard tracks all prompt components in the ${domain} domain.
## Component Library
<%* for (const component of components) { %>
- [[${component.name.replace(/\s+/g, '-')}-${component.type}]] (${component.type})
<% } %>
## Recently Created Components
- [[${promptName}]] (main prompt)
## Usage Statistics
## Maintenance Schedule
`;
await tp.file.create_new(dashboardContent, `prompt-dashboard-${domain}`, false, "06-dashboards");
tR += `Modular prompt system created successfully!
- Main prompt: [[${promptName}]]
- Components: ${componentLinks.join(', ')}
- Dashboard: [[prompt-dashboard-${domain}]]`;
%>
```

---
### Advanced Template 2: Prompt Testing & Version Control System
**Description:** This comprehensive template creates a full prompt testing and version control system. It generates multiple versions of a prompt, creates test cases, runs automated evaluations, and produces detailed comparison reports. The system tracks performance metrics across versions and provides recommendations for improvements.
**Top Use Cases:**
1. Systematic A/B testing of prompt variations to optimize performance
2. Version-controlled prompt development with automated evaluation metrics
3. Collaborative prompt engineering with detailed performance tracking
**Implementation Tips:**
- Integrate with external APIs for automated testing if available
- Use consistent evaluation criteria across all versions for valid comparisons
- Implement a naming convention that includes version numbers and creation dates
- Consider adding git-like functionality for tracking changes between versions
**Customization Options:**
1. Add integration with specific AI model APIs for automated testing
2. Implement statistical analysis of test results for significance testing
3. Extend to include user feedback collection mechanisms
```
<%*
// Base prompt information
const basePromptName = await tp.system.prompt("Base Prompt Name");
const versionCount = parseInt(await tp.system.prompt("Number of versions to create", "3"));
const testCasesCount = parseInt(await tp.system.prompt("Number of test cases", "5"));
// Create test cases
const testCases = [];
for (let i = 1; i <= testCasesCount; i++) {
  testCases.push({
    id: i,
    input: await tp.system.prompt(`Test Case ${i} Input`),
    expected: await tp.system.prompt(`Test Case ${i} Expected Output (optional)`)
  });
}
// Create versions
const versions = [];
for (let v = 1; v <= versionCount; v++) {
  const versionName = `${basePromptName}-v${v}`;
  const modifications = await tp.system.prompt(`Modifications for version ${v}`);
  const versionContent = `---
type: prompt
version: ${v}
base-prompt: [[${basePromptName}]]
modifications: ${modifications}
created: ${tp.date.now("YYYY-MM-DD")}
status: testing
tags:
  - #prompt-engineering
  - #version-control
  - #testing
---
# ${versionName}
## Modifications from Base
${modifications}
## Full Prompt Content
${await tp.system.prompt(`Full prompt content for version ${v}`)}
## Test Cases
<%* for (const testCase of testCases) { %>
### Test Case ${testCase.id}
Input: ${testCase.input}
Expected: ${testCase.expected || "N/A"}
Response: 
Evaluation:
- Accuracy: 
- Relevance: 
- Clarity: 
- Efficiency: 
Notes:

---
<%* } %>
`;
  await tp.file.create_new(versionContent, versionName, false, "03-notes");
  versions.push(versionName);
}
// Create test plan
const testPlanContent = `---
type: test-plan
prompt: [[${basePromptName}]]
versions: [${versions.map(v => `[[${v}]]`).join(', ')}]
test-cases: ${testCasesCount}
created: ${tp.date.now("YYYY-MM-DD")}
status: active
tags:
  - #prompt-engineering
  - #testing
  - #test-plan
---
# Test Plan: ${basePromptName}
## Overview
Testing ${versionCount} versions of ${basePromptName} against ${testCasesCount} test cases.
## Versions
<%* for (const version of versions) { %>
- [[${version}]]
<%* } %>
## Test Cases
<%* for (const testCase of testCases) { %>
### Test Case ${testCase.id}
Input: ${testCase.input}
Expected Output: ${testCase.expected || "N/A"}

---
<%* } %>
## Evaluation Criteria
1. Accuracy (0-10)
2. Relevance (0-10)
3. Clarity (0-10)
4. Efficiency (0-10)
5. Overall Score (0-10)
## Testing Schedule
Start: ${tp.date.now("YYYY-MM-DD")}
Estimated Completion: ${tp.date.now("YYYY-MM-DD", 7)}
## Results Tracking
`;
await tp.file.create_new(testPlanContent, `test-plan-${basePromptName}`, false, "05-tasks-&-reviews");
// Create comparison report template
const comparisonReportContent = `---
type: comparison-report
prompt: [[${basePromptName}]]
versions: [${versions.map(v => `[[${v}]]`).join(', ')}]
created: ${tp.date.now("YYYY-MM-DD")}
status: pending
tags:
  - #prompt-engineering
  - #report
  - #comparison
---
# Comparison Report: ${basePromptName}
## Executive Summary
## Version Performance
<%* for (const version of versions) { %>
### [[${version}]]
Average Score: 
Strengths:
Weaknesses:

---
<%* } %>
## Detailed Analysis by Test Case
<%* for (const testCase of testCases) { %>
### Test Case ${testCase.id}: ${testCase.input.substring(0, 50)}...
<%* for (const version of versions) { %>
- [[${version}]]: 
<%* } %>

---
<%* } %>
## Recommendations
## Next Steps
`;
await tp.file.create_new(comparisonReportContent, `comparison-${basePromptName}`, false, "06-dashboards");
tR += `Prompt testing system created successfully!
- Base prompt: [[${basePromptName}]]
- Versions: ${versions.map(v => `[[${v}]]`).join(', ')}
- Test plan: [[test-plan-${basePromptName}]]
- Comparison report template: [[comparison-${basePromptName}]]`;
%>
```

---
## Synergy Templates (Plugin Integration)
These templates demonstrate powerful integrations between Templater and other Obsidian plugins to create sophisticated workflows.

---
### Synergy Template 1: Dataview-Powered Prompt Component Library
**Description:** This template integrates Templater with Dataview to create a dynamic prompt component library dashboard. It automatically generates a searchable, filterable interface for all prompt components in your vault, showing metadata, usage statistics, and related prompts. The template creates both the component files and a Dataview-powered dashboard that updates automatically as you add new components.
**Top Use Cases:**
1. Creating a searchable knowledge base of prompt engineering components
2. Tracking component usage and effectiveness across different projects
3. Building a collaborative prompt engineering resource with team visibility
**Implementation Tips:**
- Ensure all component files have consistent metadata fields for proper Dataview querying
- Use inline fields in component files to track usage statistics
- Implement a tagging system that allows for multi-dimensional filtering
- Consider adding automated backlink tracking to show where components are used
**Customization Options:**
1. Add custom CSS styling to improve the visual presentation of the dashboard
2. Implement sorting and filtering options based on performance metrics
3. Extend to include component rating systems from multiple users
```
<%*
// Create multiple prompt components
const componentCount = parseInt(await tp.system.prompt("Number of components to create", "5"));
const components = [];
for (let i = 1; i <= componentCount; i++) {
  const componentName = await tp.system.prompt(`Component ${i} Name`);
  const componentType = await tp.system.prompt(`Component ${i} Type`, "role");
  const description = await tp.system.prompt(`Component ${i} Description`);
  const example = await tp.system.prompt(`Component ${i} Example Usage`);
  const componentContent = `---
type: prompt-component
component-type: ${componentType}
category: ${await tp.system.prompt(`Component ${i} Category`, "general")}
complexity: ${await tp.system.prompt(`Component ${i} Complexity`, "medium")}
created: ${tp.date.now("YYYY-MM-DD")}
author: ${tp.config.username}
usage-count: 0
rating: 0
tags:
  - #prompt-engineering
  - #component/${componentType}
  - #complexity/${await tp.system.prompt(`Component ${i} Complexity`, "medium")}
---
# ${componentName}
## Description
${description}
## Type
${componentType.charAt(0).toUpperCase() + componentType.slice(1)}
## Content
${await tp.system.prompt(`Component ${i} Full Content`)}
## Example Usage
${example}
## Related Components
`;
  const fileName = `${componentName.replace(/\s+/g, '-')}-${componentType}`;
  await tp.file.create_new(componentContent, fileName, false, "03-notes/prompt-components");
  components.push({
    name: componentName,
    file: fileName,
    type: componentType
  });
}
// Create Dataview dashboard
const dashboardContent = `---
type: dashboard
dashboard-type: component-library
created: ${tp.date.now("YYYY-MM-DD")}
tags:
  - #prompt-engineering
  - #dashboard
  - #dataview
---
# Prompt Component Library
## Overview
This dashboard provides a searchable library of all prompt components in your vault.
## Component Browser
\`\`\`dataview
TABLE 
  component-type AS "Type",
  category AS "Category",
  complexity AS "Complexity",
  rating AS "Rating",
  usage-count AS "Usage"
FROM "03-notes/prompt-components" 
WHERE type = "prompt-component"
SORT rating DESC
\`\`\`
## Components by Type
\`\`\`dataview
TABLE 
  L.text AS "Description",
  rating AS "Rating"
FROM "03-notes/prompt-components"
WHERE type = "prompt-component"
GROUP BY component-type
\`\`\`
## Recently Added Components
\`\`\`dataview
TABLE 
  component-type AS "Type",
  category AS "Category",
  author AS "Author"
FROM "03-notes/prompt-components" 
WHERE type = "prompt-component" AND created >= date(${tp.date.now("YYYY-MM-DD", -30)})
SORT created DESC
LIMIT 10
\`\`\`
## Top Rated Components
\`\`\`dataview
TABLE 
  component-type AS "Type",
  category AS "Category",
  usage-count AS "Usage"
FROM "03-notes/prompt-components" 
WHERE type = "prompt-component" AND rating >= 4
SORT rating DESC
LIMIT 5
\`\`\`
## Search Components
Use the search bar above to find specific components by name, type, or content.
`;
await tp.file.create_new(dashboardContent, "prompt-component-library", false, "06-dashboards");
tR += `Dataview-powered prompt component library created successfully!
- Created ${componentCount} components in /03-notes/prompt-components/
- Dashboard: [[prompt-component-library]]
- To use: Open the dashboard and use Dataview queries to search and filter components`;
%>
```

---
### Synergy Template 2: QuickAdd-Templater Prompt Capture & Processing Workflow
**Description:** This template creates a powerful capture and processing workflow that integrates Templater with QuickAdd. It sets up a QuickAdd capture menu for rapidly adding new prompt ideas to an inbox, then provides a processing template that converts these captured ideas into fully structured prompt engineering notes with appropriate metadata, tags, and organizational structure.
**Top Use Cases:**
1. Rapidly capturing prompt ideas throughout the day for later development
2. Creating a systematic workflow for turning informal prompt concepts into production-ready prompts
3. Building a team-based prompt engineering pipeline with idea capture and formalization stages
**Implementation Tips:**
- Configure QuickAdd to use the capture template as a macro for instant access
- Set up daily or weekly processing routines to convert captured ideas
- Use consistent naming conventions for captured items to enable batch processing
- Consider adding a review step to prioritize which captured ideas to process first
**Customization Options:**
1. Add integration with Tasks plugin to automatically create processing tasks for captured ideas
2. Implement a scoring system during capture to prioritize processing order
3. Extend to include automated tagging based on keywords in the captured content
```
<%*
// This is the processing template that converts captured ideas into structured prompts
// First, we assume a captured idea exists with basic fields
const capturedTitle = tp.frontmatter.captured_title || tp.file.title;
const capturedContent = tp.frontmatter.captured_content || "";
const captureDate = tp.frontmatter.capture_date || tp.date.now("YYYY-MM-DD");
const capturedFrom = tp.frontmatter.captured_from || "manual";
// If this is a new capture (not yet processed), show processing interface
if (!tp.frontmatter.processed) {
%>
---
type: prompt
status: seedling
maturity: seedling
confidence: speculative
captured-from: <% capturedFrom %>
capture-date: <% captureDate %>
processed: false
tags:
  - #prompt-engineering
  - #status/seedling
  - #inbox
---
# <% capturedTitle %>
## Captured Idea
<% capturedContent %>
## Processing Checklist
- [ ] Define clear objective
- [ ] Identify target AI model
- [ ] Specify required inputs
- [ ] Define expected outputs
- [ ] Add context and constraints
- [ ] Create usage examples
## Processed Prompt
### Objective
<% await tp.system.prompt("What is the clear objective of this prompt?") %>
### Target Model
<% await tp.system.prompt("Which AI model is this prompt designed for?", "claude-opus-4.1") %>
### Context
Captured on: <% captureDate %>
Source: <% capturedFrom %>
### Instructions
<% await tp.system.prompt("Detailed instructions for the prompt") %>
### Input Requirements
<% await tp.system.prompt("What inputs are required? (list)") %>
### Output Format
<% await tp.system.prompt("What format should the output follow?") %>
### Constraints
<% await tp.system.prompt("Any constraints or limitations?") %>
### Examples
1. Input: <% await tp.system.prompt("Example 1 input") %>
   Output: <% await tp.system.prompt("Example 1 expected output") %>
2. Input: <% await tp.system.prompt("Example 2 input") %>
   Output: <% await tp.system.prompt("Example 2 expected output") %>
## Metadata
Created: <% tp.date.now("YYYY-MM-DD") %>
Author: <% tp.config.username %>
<%*
// Update frontmatter to mark as processed
// In a real implementation, this would be handled by QuickAdd macro
} else {
  // This is for the QuickAdd capture template
  tR += `---
type: prompt-capture
status: inbox
capture_date: ${tp.date.now("YYYY-MM-DD")}
captured_from: quickadd
processed: false
tags:
  - #prompt-engineering
  - #inbox
  - #captured
---
# Prompt Idea: ${await tp.system.prompt("Brief title for your prompt idea")}
## Captured Content
${await tp.system.prompt("Describe your prompt idea in detail")}
## Initial Thoughts
${await tp.system.prompt("Any initial thoughts on implementation? (optional)")}
## Potential Use Cases
${await tp.system.prompt("What are some potential use cases? (optional)")}

---
Captured on: ${tp.date.now("YYYY-MM-DD HH:mm")}
Captured by: ${tp.config.username}
`;
}
%>
```

---



---
## Basic Templates
These templates demonstrate the foundational elements of Templater, including variable insertion, date formatting, and frontmatter generation. They're ideal for getting started with automated note creation.

---
### Template 1: Basic Prompt Engineering Note Template
This template creates a simple prompt engineering note with standard metadata fields and current timestamp.
```
---
type: prompt
source: <% tp.system.prompt("AI Model", "claude-opus-4.1") %>
maturity: seedling
confidence: provisional
status: active
priority: medium
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
tags: 
  - #prompt-engineering
  - #status/seedling
---
# <% tp.file.title %>
## Objective
## Context
## Instructions
## Expected Output
## Notes
```

---
### Template 2: Daily Prompt Review Template
Creates a daily review note for tracking prompt performance and iterations.
```
---
type: prompt-report
date: <% tp.date.now("YYYY-MM-DD") %>
related-prompts: []
status: active
tags:
  - #prompt-engineering
  - #type/report
  - #status/in-progress
---
# Prompt Review - <% tp.date.now("YYYY-MM-DD") %>
## Prompts Tested Today
## Performance Metrics
- Accuracy: 
- Relevance: 
- Creativity: 
- Efficiency: 
## Key Insights
## Next Iterations
## Resources
```

---
### Template 3: Prompt Component Template
A modular template for creating reusable prompt components.
```
---
type: prompt
subtype: component
category: <% tp.system.prompt("Component Category", "reasoning") %>
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #prompt-engineering
  - #modular-prompt
---
# <% tp.file.title %>
## Purpose
[Describe what this component does]
## Usage
[Describe how to use this component]
## Parameters
- [List any parameters needed]
## Example Implementation
```

---
### Template 4: Simple Prompt Template with Context
A straightforward template for capturing prompts with contextual information.
```
---
type: prompt
domain: <% tp.system.prompt("Domain", "general") %>
complexity: <% tp.system.prompt("Complexity", "medium") %>
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #prompt-engineering
  - #<% tp.frontmatter.domain %>
---
# <% tp.file.title %>
## Context
Created on: <% tp.date.now("YYYY-MM-DD HH:mm") %>
Domain: [[<% tp.frontmatter.domain %>]]
Complexity: <% tp.frontmatter.complexity %>
## Prompt
## Expected Output
## Notes
```

---
## Intermediate Templates
These templates introduce conditional logic, loops, and user interaction to create more dynamic and context-aware templates.

---
### Template 1: Adaptive Prompt Template Generator
This template dynamically generates different prompt structures based on user-selected type and includes conditional sections.
```
<%*
const promptType = await tp.system.prompt("Prompt Type", "analysis");
const complexity = await tp.system.prompt("Complexity Level", "medium");
const includeExamples = await tp.system.prompt("Include Examples? (y/n)", "y");
%>
---
type: prompt
prompt-type: <% promptType %>
complexity: <% complexity %>
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #prompt-engineering
  - #type/<% promptType %>
  - #complexity/<% complexity %>
---
# <% tp.file.title %>
## Role
<%* if (promptType === "analysis") { %>
You are an expert analyst specializing in breaking down complex information.
<%* } else if (promptType === "creative") { %>
You are a creative genius with the ability to generate innovative ideas.
<%* } else { %>
You are a helpful AI assistant with expertise in <% promptType %>.
<%* } %>
## Task
<% tp.system.prompt("Describe the task") %>
## Context
Created: <% tp.date.now("YYYY-MM-DD") %>
Type: <% promptType %>
Complexity: <% complexity %>
<%* if (includeExamples.toLowerCase() === "y") { %>
## Examples
1. <% tp.system.prompt("Example 1") %>
2. <% tp.system.prompt("Example 2") %>
<%* } %>
## Instructions
<% tp.system.prompt("Detailed instructions") %>
## Constraints
<% tp.system.prompt("Constraints or limitations") %>
## Output Format
<% tp.system.prompt("Expected output format") %>
```

---
### Template 2: Multi-Prompt Project Template
Creates a comprehensive prompt engineering project with multiple related prompts and tracking metadata.
```
<%*
const projectName = await tp.system.prompt("Project Name");
const projectDomain = await tp.system.prompt("Domain", "general");
const numPrompts = parseInt(await tp.system.prompt("Number of prompts to create", "3"));
const promptNames = [];
for (let i = 1; i <= numPrompts; i++) {
  promptNames.push(await tp.system.prompt(`Prompt ${i} Name`));
}
%>
---
type: prompt-project
project-name: <% projectName %>
domain: <% projectDomain %>
prompt-count: <% numPrompts %>
status: active
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #prompt-engineering
  - #project/<% projectName.toLowerCase().replace(/\s+/g, '-') %>
---
# <% projectName %> Prompt Engineering Project
## Project Overview
Domain: [[<% projectDomain %>]]
Created: <% tp.date.now("YYYY-MM-DD") %>
Status: Active
## Prompts in this Project
<%* for (let i = 0; i < promptNames.length; i++) { %>
- [[<% promptNames[i] %>]]
<%* } %>
## Project Goals
## Implementation Timeline
## Success Metrics
## Resources & References
```

---
### Template 3: Prompt Evaluation Template with Scoring
This template creates a structured evaluation framework for testing and scoring prompts.
```
<%*
const promptName = await tp.system.prompt("Prompt Name");
const evaluator = await tp.system.prompt("Evaluator Name", tp.config.username);
const testCases = parseInt(await tp.system.prompt("Number of test cases", "3"));
%>
---
type: prompt-evaluation
prompt: [[<% promptName %>]]
evaluator: <% evaluator %>
date: <% tp.date.now("YYYY-MM-DD") %>
status: in-progress
tags:
  - #prompt-engineering
  - #evaluation
  - #<% promptName.toLowerCase().replace(/\s+/g, '-') %>
---
# Prompt Evaluation: <% promptName %>
## Evaluation Details
- Evaluator: <% evaluator %>
- Date: <% tp.date.now("YYYY-MM-DD") %>
- Prompt: [[<% promptName %>]]
## Scoring Criteria
Scale: 1-5 (1=Poor, 3=Average, 5=Excellent)
<%* for (let i = 1; i <= testCases; i++) { %>
### Test Case <% i %>
Prompt: <% tp.system.prompt(`Test Case ${i} Prompt`) %>
Response: <% tp.system.prompt(`Test Case ${i} Response`) %>
Evaluation:
- Accuracy: <% tp.system.prompt("Accuracy (1-5)", "3") %>
- Relevance: <% tp.system.prompt("Relevance (1-5)", "3") %>
- Clarity: <% tp.system.prompt("Clarity (1-5)", "3") %>
- Creativity: <% tp.system.prompt("Creativity (1-5)", "3") %>
Notes: <% tp.system.prompt(`Test Case ${i} Notes`) %>

---
<%* } %>
## Overall Assessment
Strengths:
Weaknesses:
Recommendations:
Final Score: <% tp.system.prompt("Overall Score (1-5)", "3") %> / 5
```

---
## Advanced Templates
These sophisticated templates showcase expert-level Templater capabilities including user scripts, complex automation workflows, and multi-file operations.

---
### Advanced Template 1: Modular Prompt Builder System
**Description:** This template creates an entire prompt engineering framework with component-based architecture. It generates a master prompt file along with individual component files, establishes linking relationships, and creates a documentation dashboard. The system allows users to build complex prompts by combining modular components like role definitions, task descriptions, and output formats.
**Top Use Cases:**
1. Building a library of reusable prompt components for consistent AI interactions
2. Creating complex multi-step prompting workflows with version-controlled components
3. Establishing a team-based prompt engineering system with shared components
**Implementation Tips:**
- Store component templates in a dedicated folder structure (e.g., `/03-notes/prompt-components/`)
- Use consistent naming conventions for components to enable easy discovery
- Implement a versioning system for components to track improvements over time
- Consider using Dataview queries in the dashboard to dynamically show component usage
**Customization Options:**
1. Add category-based organization by modifying the folder structure generation
2. Implement dependency tracking between components using backlinks
3. Extend to include automated testing of component combinations
```
<%*
// Main prompt information
const promptName = await tp.system.prompt("Main Prompt Name");
const description = await tp.system.prompt("Prompt Description");
const domain = await tp.system.prompt("Domain", "general");
// Component selection
const components = [];
const componentTypes = ["role", "task", "context", "constraints", "output-format"];
for (const type of componentTypes) {
  const componentName = await tp.system.prompt(`Component for ${type} (or leave blank)`);
  if (componentName) {
    components.push({
      type: type,
      name: componentName,
      content: await tp.system.prompt(`Content for ${type} component`)
    });
  }
}
// Create component files
const componentLinks = [];
for (const component of components) {
  const componentFileName = `${component.name.replace(/\s+/g, '-')}-${component.type}`;
  const componentPath = `03-notes/prompt-components/${componentFileName}.md`;
  // Create component file
  const componentContent = `---
type: prompt-component
component-type: ${component.type}
related-prompt: [[${promptName}]]
created: ${tp.date.now("YYYY-MM-DD")}
tags:
  - #prompt-engineering
  - #component/${component.type}
---
# ${component.name} (${component.type})
## Content
${component.content}
## Usage
This component is used in [[${promptName}]]`;
  await tp.file.create_new(componentContent, componentFileName, false, "03-notes/prompt-components");
  componentLinks.push(`[[${componentFileName}]]`);
}
// Create main prompt file
const mainPromptContent = `---
type: prompt
subtype: modular
domain: ${domain}
components: [${componentLinks.join(', ')}]
created: ${tp.date.now("YYYY-MM-DD")}
status: active
tags:
  - #prompt-engineering
  - #modular-prompt
  - #domain/${domain}
---
# ${promptName}
## Description
${description}
## Components
<%* for (const component of components) { %>
### ${component.type.charAt(0).toUpperCase() + component.type.slice(1)}
[[${component.name.replace(/\s+/g, '-')}-${component.type}]]
<% } %>
## Full Prompt Construction
<%* for (const component of components) { %>
${component.content}
<% } %>
## Usage Instructions
## Version History
- ${tp.date.now("YYYY-MM-DD")}: Initial creation`;
await tp.file.create_new(mainPromptContent, promptName, false, "03-notes");
// Create dashboard
const dashboardContent = `---
type: dashboard
dashboard-type: prompt-components
domain: ${domain}
created: ${tp.date.now("YYYY-MM-DD")}
tags:
  - #prompt-engineering
  - #dashboard
---
# Prompt Component Dashboard: ${domain}
## Overview
This dashboard tracks all prompt components in the ${domain} domain.
## Component Library
<%* for (const component of components) { %>
- [[${component.name.replace(/\s+/g, '-')}-${component.type}]] (${component.type})
<% } %>
## Recently Created Components
- [[${promptName}]] (main prompt)
## Usage Statistics
## Maintenance Schedule
`;
await tp.file.create_new(dashboardContent, `prompt-dashboard-${domain}`, false, "06-dashboards");
tR += `Modular prompt system created successfully!
- Main prompt: [[${promptName}]]
- Components: ${componentLinks.join(', ')}
- Dashboard: [[prompt-dashboard-${domain}]]`;
%>
```

---
### Advanced Template 2: Prompt Testing & Version Control System
**Description:** This comprehensive template creates a full prompt testing and version control system. It generates multiple versions of a prompt, creates test cases, runs automated evaluations, and produces detailed comparison reports. The system tracks performance metrics across versions and provides recommendations for improvements.
**Top Use Cases:**
1. Systematic A/B testing of prompt variations to optimize performance
2. Version-controlled prompt development with automated evaluation metrics
3. Collaborative prompt engineering with detailed performance tracking
**Implementation Tips:**
- Integrate with external APIs for automated testing if available
- Use consistent evaluation criteria across all versions for valid comparisons
- Implement a naming convention that includes version numbers and creation dates
- Consider adding git-like functionality for tracking changes between versions
**Customization Options:**
1. Add integration with specific AI model APIs for automated testing
2. Implement statistical analysis of test results for significance testing
3. Extend to include user feedback collection mechanisms
```
<%*
// Base prompt information
const basePromptName = await tp.system.prompt("Base Prompt Name");
const versionCount = parseInt(await tp.system.prompt("Number of versions to create", "3"));
const testCasesCount = parseInt(await tp.system.prompt("Number of test cases", "5"));
// Create test cases
const testCases = [];
for (let i = 1; i <= testCasesCount; i++) {
  testCases.push({
    id: i,
    input: await tp.system.prompt(`Test Case ${i} Input`),
    expected: await tp.system.prompt(`Test Case ${i} Expected Output (optional)`)
  });
}
// Create versions
const versions = [];
for (let v = 1; v <= versionCount; v++) {
  const versionName = `${basePromptName}-v${v}`;
  const modifications = await tp.system.prompt(`Modifications for version ${v}`);
  const versionContent = `---
type: prompt
version: ${v}
base-prompt: [[${basePromptName}]]
modifications: ${modifications}
created: ${tp.date.now("YYYY-MM-DD")}
status: testing
tags:
  - #prompt-engineering
  - #version-control
  - #testing
---
# ${versionName}
## Modifications from Base
${modifications}
## Full Prompt Content
${await tp.system.prompt(`Full prompt content for version ${v}`)}
## Test Cases
<%* for (const testCase of testCases) { %>
### Test Case ${testCase.id}
Input: ${testCase.input}
Expected: ${testCase.expected || "N/A"}
Response: 
Evaluation:
- Accuracy: 
- Relevance: 
- Clarity: 
- Efficiency: 
Notes:

---
<%* } %>
`;
  await tp.file.create_new(versionContent, versionName, false, "03-notes");
  versions.push(versionName);
}
// Create test plan
const testPlanContent = `---
type: test-plan
prompt: [[${basePromptName}]]
versions: [${versions.map(v => `[[${v}]]`).join(', ')}]
test-cases: ${testCasesCount}
created: ${tp.date.now("YYYY-MM-DD")}
status: active
tags:
  - #prompt-engineering
  - #testing
  - #test-plan
---
# Test Plan: ${basePromptName}
## Overview
Testing ${versionCount} versions of ${basePromptName} against ${testCasesCount} test cases.
## Versions
<%* for (const version of versions) { %>
- [[${version}]]
<%* } %>
## Test Cases
<%* for (const testCase of testCases) { %>
### Test Case ${testCase.id}
Input: ${testCase.input}
Expected Output: ${testCase.expected || "N/A"}

---
<%* } %>
## Evaluation Criteria
1. Accuracy (0-10)
2. Relevance (0-10)
3. Clarity (0-10)
4. Efficiency (0-10)
5. Overall Score (0-10)
## Testing Schedule
Start: ${tp.date.now("YYYY-MM-DD")}
Estimated Completion: ${tp.date.now("YYYY-MM-DD", 7)}
## Results Tracking
`;
await tp.file.create_new(testPlanContent, `test-plan-${basePromptName}`, false, "05-tasks-&-reviews");
// Create comparison report template
const comparisonReportContent = `---
type: comparison-report
prompt: [[${basePromptName}]]
versions: [${versions.map(v => `[[${v}]]`).join(', ')}]
created: ${tp.date.now("YYYY-MM-DD")}
status: pending
tags:
  - #prompt-engineering
  - #report
  - #comparison
---
# Comparison Report: ${basePromptName}
## Executive Summary
## Version Performance
<%* for (const version of versions) { %>
### [[${version}]]
Average Score: 
Strengths:
Weaknesses:

---
<%* } %>
## Detailed Analysis by Test Case
<%* for (const testCase of testCases) { %>
### Test Case ${testCase.id}: ${testCase.input.substring(0, 50)}...
<%* for (const version of versions) { %>
- [[${version}]]: 
<%* } %>

---
<%* } %>
## Recommendations
## Next Steps
`;
await tp.file.create_new(comparisonReportContent, `comparison-${basePromptName}`, false, "06-dashboards");
tR += `Prompt testing system created successfully!
- Base prompt: [[${basePromptName}]]
- Versions: ${versions.map(v => `[[${v}]]`).join(', ')}
- Test plan: [[test-plan-${basePromptName}]]
- Comparison report template: [[comparison-${basePromptName}]]`;
%>
```

---
## Synergy Templates (Plugin Integration)
These templates demonstrate powerful integrations between Templater and other Obsidian plugins to create sophisticated workflows.

---
### Synergy Template 1: Dataview-Powered Prompt Component Library
**Description:** This template integrates Templater with Dataview to create a dynamic prompt component library dashboard. It automatically generates a searchable, filterable interface for all prompt components in your vault, showing metadata, usage statistics, and related prompts. The template creates both the component files and a Dataview-powered dashboard that updates automatically as you add new components.
**Top Use Cases:**
1. Creating a searchable knowledge base of prompt engineering components
2. Tracking component usage and effectiveness across different projects
3. Building a collaborative prompt engineering resource with team visibility
**Implementation Tips:**
- Ensure all component files have consistent metadata fields for proper Dataview querying
- Use inline fields in component files to track usage statistics
- Implement a tagging system that allows for multi-dimensional filtering
- Consider adding automated backlink tracking to show where components are used
**Customization Options:**
1. Add custom CSS styling to improve the visual presentation of the dashboard
2. Implement sorting and filtering options based on performance metrics
3. Extend to include component rating systems from multiple users
```
<%*
// Create multiple prompt components
const componentCount = parseInt(await tp.system.prompt("Number of components to create", "5"));
const components = [];
for (let i = 1; i <= componentCount; i++) {
  const componentName = await tp.system.prompt(`Component ${i} Name`);
  const componentType = await tp.system.prompt(`Component ${i} Type`, "role");
  const description = await tp.system.prompt(`Component ${i} Description`);
  const example = await tp.system.prompt(`Component ${i} Example Usage`);
  const componentContent = `---
type: prompt-component
component-type: ${componentType}
category: ${await tp.system.prompt(`Component ${i} Category`, "general")}
complexity: ${await tp.system.prompt(`Component ${i} Complexity`, "medium")}
created: ${tp.date.now("YYYY-MM-DD")}
author: ${tp.config.username}
usage-count: 0
rating: 0
tags:
  - #prompt-engineering
  - #component/${componentType}
  - #complexity/${await tp.system.prompt(`Component ${i} Complexity`, "medium")}
---
# ${componentName}
## Description
${description}
## Type
${componentType.charAt(0).toUpperCase() + componentType.slice(1)}
## Content
${await tp.system.prompt(`Component ${i} Full Content`)}
## Example Usage
${example}
## Related Components
`;
  const fileName = `${componentName.replace(/\s+/g, '-')}-${componentType}`;
  await tp.file.create_new(componentContent, fileName, false, "03-notes/prompt-components");
  components.push({
    name: componentName,
    file: fileName,
    type: componentType
  });
}
// Create Dataview dashboard
const dashboardContent = `---
type: dashboard
dashboard-type: component-library
created: ${tp.date.now("YYYY-MM-DD")}
tags:
  - #prompt-engineering
  - #dashboard
  - #dataview
---
# Prompt Component Library
## Overview
This dashboard provides a searchable library of all prompt components in your vault.
## Component Browser
\`\`\`dataview
TABLE 
  component-type AS "Type",
  category AS "Category",
  complexity AS "Complexity",
  rating AS "Rating",
  usage-count AS "Usage"
FROM "03-notes/prompt-components" 
WHERE type = "prompt-component"
SORT rating DESC
\`\`\`
## Components by Type
\`\`\`dataview
TABLE 
  L.text AS "Description",
  rating AS "Rating"
FROM "03-notes/prompt-components"
WHERE type = "prompt-component"
GROUP BY component-type
\`\`\`
## Recently Added Components
\`\`\`dataview
TABLE 
  component-type AS "Type",
  category AS "Category",
  author AS "Author"
FROM "03-notes/prompt-components" 
WHERE type = "prompt-component" AND created >= date(${tp.date.now("YYYY-MM-DD", -30)})
SORT created DESC
LIMIT 10
\`\`\`
## Top Rated Components
\`\`\`dataview
TABLE 
  component-type AS "Type",
  category AS "Category",
  usage-count AS "Usage"
FROM "03-notes/prompt-components" 
WHERE type = "prompt-component" AND rating >= 4
SORT rating DESC
LIMIT 5
\`\`\`
## Search Components
Use the search bar above to find specific components by name, type, or content.
`;
await tp.file.create_new(dashboardContent, "prompt-component-library", false, "06-dashboards");
tR += `Dataview-powered prompt component library created successfully!
- Created ${componentCount} components in /03-notes/prompt-components/
- Dashboard: [[prompt-component-library]]
- To use: Open the dashboard and use Dataview queries to search and filter components`;
%>
```

---
### Synergy Template 2: QuickAdd-Templater Prompt Capture & Processing Workflow
**Description:** This template creates a powerful capture and processing workflow that integrates Templater with QuickAdd. It sets up a QuickAdd capture menu for rapidly adding new prompt ideas to an inbox, then provides a processing template that converts these captured ideas into fully structured prompt engineering notes with appropriate metadata, tags, and organizational structure.
**Top Use Cases:**
1. Rapidly capturing prompt ideas throughout the day for later development
2. Creating a systematic workflow for turning informal prompt concepts into production-ready prompts
3. Building a team-based prompt engineering pipeline with idea capture and formalization stages
**Implementation Tips:**
- Configure QuickAdd to use the capture template as a macro for instant access
- Set up daily or weekly processing routines to convert captured ideas
- Use consistent naming conventions for captured items to enable batch processing
- Consider adding a review step to prioritize which captured ideas to process first
**Customization Options:**
1. Add integration with Tasks plugin to automatically create processing tasks for captured ideas
2. Implement a scoring system during capture to prioritize processing order
3. Extend to include automated tagging based on keywords in the captured content
```
<%*
// This is the processing template that converts captured ideas into structured prompts
// First, we assume a captured idea exists with basic fields
const capturedTitle = tp.frontmatter.captured_title || tp.file.title;
const capturedContent = tp.frontmatter.captured_content || "";
const captureDate = tp.frontmatter.capture_date || tp.date.now("YYYY-MM-DD");
const capturedFrom = tp.frontmatter.captured_from || "manual";
// If this is a new capture (not yet processed), show processing interface
if (!tp.frontmatter.processed) {
%>
---
type: prompt
status: seedling
maturity: seedling
confidence: speculative
captured-from: <% capturedFrom %>
capture-date: <% captureDate %>
processed: false
tags:
  - #prompt-engineering
  - #status/seedling
  - #inbox
---
# <% capturedTitle %>
## Captured Idea
<% capturedContent %>
## Processing Checklist
- [ ] Define clear objective
- [ ] Identify target AI model
- [ ] Specify required inputs
- [ ] Define expected outputs
- [ ] Add context and constraints
- [ ] Create usage examples
## Processed Prompt
### Objective
<% await tp.system.prompt("What is the clear objective of this prompt?") %>
### Target Model
<% await tp.system.prompt("Which AI model is this prompt designed for?", "claude-opus-4.1") %>
### Context
Captured on: <% captureDate %>
Source: <% capturedFrom %>
### Instructions
<% await tp.system.prompt("Detailed instructions for the prompt") %>
### Input Requirements
<% await tp.system.prompt("What inputs are required? (list)") %>
### Output Format
<% await tp.system.prompt("What format should the output follow?") %>
### Constraints
<% await tp.system.prompt("Any constraints or limitations?") %>
### Examples
1. Input: <% await tp.system.prompt("Example 1 input") %>
   Output: <% await tp.system.prompt("Example 1 expected output") %>
2. Input: <% await tp.system.prompt("Example 2 input") %>
   Output: <% await tp.system.prompt("Example 2 expected output") %>
## Metadata
Created: <% tp.date.now("YYYY-MM-DD") %>
Author: <% tp.config.username %>
<%*
// Update frontmatter to mark as processed
// In a real implementation, this would be handled by QuickAdd macro
} else {
  // This is for the QuickAdd capture template
  tR += `---
type: prompt-capture
status: inbox
capture_date: ${tp.date.now("YYYY-MM-DD")}
captured_from: quickadd
processed: false
tags:
  - #prompt-engineering
  - #inbox
  - #captured
---
# Prompt Idea: ${await tp.system.prompt("Brief title for your prompt idea")}
## Captured Content
${await tp.system.prompt("Describe your prompt idea in detail")}
## Initial Thoughts
${await tp.system.prompt("Any initial thoughts on implementation? (optional)")}
## Potential Use Cases
${await tp.system.prompt("What are some potential use cases? (optional)")}

---
Captured on: ${tp.date.now("YYYY-MM-DD HH:mm")}
Captured by: ${tp.config.username}
`;
}
%>
```

---
# Templater Template Collection: **Cognitive Science Research & Knowledge Management**

---
## Basic Templates
These templates cover fundamental Templater operations for building a cognitive science-focused PKB.

---
Create a new permanent note with standard metadata structure.
```
---
type: permanent-note
source: 
maturity: seedling
confidence: provisional
status: active
priority: medium
link-up: 
tags: [cognitive-science, pkb, permanent]
created: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>
## Summary
<% tp.system.prompt("Enter a brief summary of this note:") %>
## Key Concepts
- 
## Related Notes
- 
## References
- 
```

---
Generate a literature review note with automatic date formatting and folder awareness.
```
---
type: literature
title: "<% tp.file.title %>"
author: <% tp.system.prompt("Author(s):") %>
year: <% tp.system.prompt("Publication Year:") %>
source: 
status: not-read
tags: [literature, cognitive-science, #status/not-read]
reviewed: 
---
# <% tp.file.title %>
## Citation
<% tp.frontmatter.author %>. (<% tp.frontmatter.year %>). *<% tp.file.title %>*.
## Abstract
<% tp.system.prompt("Enter abstract or key points:") %>
## Key Findings
1. 
## Methodology Notes
- 
## Relevance to PKB
- 
## Follow-up Questions
- 
```

---
Create a daily research log with automatic linking to MOCs.
```
---
type: daily-log
date: <% tp.date.now("YYYY-MM-DD") %>
day-of-week: <% tp.date.now("dddd") %>
focus-area: 
moc-link: 
tags: [daily-log, research, cognitive-science]
---
# <% tp.date.now("YYYY-MM-DD") %> - Research Log
## Today's Focus
<% tp.system.prompt("What is today's research focus?") %>
## Tasks Completed
- 
## Insights & Observations
- 
## Questions Arising
- 
## Tomorrow's Priorities
- 
## Linked to: [[<% tp.system.prompt("Which MOC to link today's work to?", "cognitive-science-moc") %>]]
```

---
Create a concept note with automatic tag generation based on title.
```
---
type: concept
title: <% tp.file.title %>
related-domain: 
maturity: seedling
status: active
tags: [concept, cognitive-science, <% tp.file.title.toLowerCase().replace(/\s+/g, '-') %>]
created: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>
## Definition
<% tp.system.prompt("Provide a working definition:") %>
## Core Components
1. 
## Examples in Practice
- 
## Related Concepts
- 
## Applications in Cognitive Science
- 
```

---
## Intermediate Templates
These templates incorporate conditional logic, user interaction, and dynamic content generation.

---
Generate a project tracking note with status-dependent sections.
```
<%*
let projectType = await tp.system.suggester(["Research Project", "Literature Review", "Framework Development", "Tutorial Creation"], ["research", "lit-review", "framework", "tutorial"]);
let projectName = await tp.system.prompt("Project Name:");
let projectStatus = await tp.system.suggester(["Active", "On Hold", "Completed", "Archived"], ["active", "on-hold", "completed", "archived"]);
let startDate = tp.date.now("YYYY-MM-DD");
let endDate = projectStatus === "completed" ? await tp.system.prompt("Completion Date (YYYY-MM-DD):") : "";
let projectTag = "#type/project";
if (projectType === "research") projectTag = "#type/research-project";
if (projectType === "lit-review") projectTag = "#type/literature-review";
if (projectType === "framework") projectTag = "#type/framework";
if (projectType === "tutorial") projectTag = "#type/tutorial";
%>
---
type: project
project-type: <% projectType %>
status: <% projectStatus %>
start-date: <% startDate %>
end-date: <% endDate %>
priority: high
tags: [project, <% projectTag %>, cognitive-science]
---
# <% projectName %> Project
## Project Overview
<% tp.system.prompt("Brief project description:") %>
## Objectives
<%* if (projectType === "research") { %>
- Conduct literature review on <% projectName %>
- Design experimental framework
- Collect and analyze data
- Document findings and implications
<%* } else if (projectType === "lit-review") { %>
- Identify key papers on <% projectName %>
- Synthesize findings across studies
- Evaluate methodological approaches
- Highlight gaps in current research
<%* } else if (projectType === "framework") { %>
- Define core components of <% projectName %>
- Map relationships between elements
- Validate with existing research
- Create implementation guide
<%* } else { %>
- Develop learning objectives
- Create content outline
- Produce draft materials
- Review and refine content
<%* } %>
## Timeline
- Start Date: <% startDate %>
<%* if (endDate) { %>
- End Date: <% endDate %>
<%* } else { %>
- Estimated Completion: TBD
<%* } %>
## Resources Needed
- 
## Progress Tracking
### Phase 1: Initiation
- [ ] Task 1
- [ ] Task 2
### Phase 2: Development
- [ ] Task 3
- [ ] Task 4
### Phase 3: Review
- [ ] Task 5
- [ ] Task 6
## Key Deliverables
- 
## Stakeholders
- 
```

---
Create a multi-file research workflow for new concepts.
```
<%*
// Get concept name
let conceptName = await tp.system.prompt("Enter concept name:");
// Create concept note
let conceptContent = `---
type: concept
title: ${conceptName}
related-domain: 
maturity: seedling
status: active
tags: [concept, cognitive-science, ${conceptName.toLowerCase().replace(/\s+/g, '-')}] 
created: ${tp.date.now("YYYY-MM-DD")}
---
# ${conceptName}
## Definition
<% tp.system.prompt("Provide a working definition:") %>
## Core Components
1. 
## Examples in Practice
- 
## Related Concepts
- 
## Applications in Cognitive Science
-`;
// Create literature folder and note
let litFolder = `04-library/${conceptName.replace(/\s+/g, '-')}`;
let litNoteName = `${conceptName.replace(/\s+/g, '-')}-literature`;
let litContent = `---
type: moc
title: "${conceptName} Literature"
category: literature
tags: [literature, moc, ${conceptName.toLowerCase().replace(/\s+/g, '-')}] 
status: active
---
# ${conceptName} Literature
## Key Papers
- 
## Research Questions
- 
## Findings Summary
- 
## Gaps in Research
-`;
// Create research questions note
let questionsContent = `---
type: analysis
title: "${conceptName} Research Questions"
focus: ${conceptName}
status: active
tags: [analysis, research-questions, ${conceptName.toLowerCase().replace(/\s+/g, '-')}] 
created: ${tp.date.now("YYYY-MM-DD")}
---
# ${conceptName} Research Questions
## Primary Questions
1. 
## Secondary Questions
1. 
## Hypotheses
- 
## Methodological Considerations
-`;
// Create all files
await tp.file.create_new(conceptContent, conceptName, true, "03-notes");
await tp.file.create_new(litContent, litNoteName, true, litFolder);
await tp.file.create_new(questionsContent, `${conceptName.replace(/\s+/g, '-')}-questions`, true, "02-projects");
// Return link to main note
tR += `[[${conceptName}]]`;
%>
```

---
Generate a reading reflection template with conditional sections.
```
<%*
let title = tp.file.title;
let author = await tp.system.prompt("Author:");
let type = await tp.system.suggester(["Book", "Journal Article", "Conference Paper", "Blog Post", "Other"], ["book", "article", "conference", "blog", "other"]);
let rating = await tp.system.suggester(["Essential", "Highly Recommended", "Recommended", "Interesting", "Background Only"], [5, 4, 3, 2, 1]);
let completedDate = tp.date.now("YYYY-MM-DD");
%>
---
type: review
material-type: <% type %>
title: "<% title %>"
author: <% author %>
rating: <% rating %>
completed: <% completedDate %>
status: read
tags: [review, <% type %>, cognitive-science, #status/read]
---
# <% title %> - Review
## Metadata
- **Author**: <% author %>
- **Type**: <% type.charAt(0).toUpperCase() + type.slice(1) %>
- **Completed**: <% completedDate %>
- **Rating**: <% rating %>/5
## Summary
<% tp.system.prompt("Brief summary of the material:") %>
## Key Insights
<%* for (let i = 1; i <= 5; i++) { %>
<%* let insight = await tp.system.prompt("Key insight #" + i + " (leave blank to stop):"); %>
<%* if (insight) { %>
<%* tR += `${i}. ${insight}\n`; %>
<%* } else { break; } %>
<%* } %>
## Critical Analysis
<% tp.system.prompt("Critical thoughts on methodology, conclusions, or assumptions:") %>
## Relevance to My Work
<% tp.system.prompt("How does this relate to your current research or interests?") %>
## Quotes to Remember
<%* for (let i = 1; i <= 3; i++) { %>
<%* let quote = await tp.system.prompt("Notable quote #" + i + " (leave blank to stop):"); %>
<%* if (quote) { %>
<%* tR += `${i}. "${quote}"\n`; %>
<%* } else { break; } %>
<%* } %>
## Action Items
- [ ] 
- [ ] 
- [ ] 
## Related Notes
- 
```

---
Create a weekly research planning template with dynamic date handling.
```
<%*
let weekStart = tp.date.now("YYYY-MM-DD", 0, "week");
let weekEnd = tp.date.now("YYYY-MM-DD", 6, "week");
let weekNumber = tp.date.now("W");
let focusArea = await tp.system.prompt("Primary focus area for this week:");
%>
---
type: weekly-plan
week: <% weekNumber %>
period-start: <% weekStart %>
period-end: <% weekEnd %>
focus-area: <% focusArea %>
status: active
tags: [planning, weekly-plan, cognitive-science]
---
# Week <% weekNumber %> Plan (<% weekStart %> to <% weekEnd %>)
## Focus Area: <% focusArea %>
## Monday (<% tp.date.now("YYYY-MM-DD", 0, "week") %>)
- [ ] 
- [ ] 
- [ ] 
## Tuesday (<% tp.date.now("YYYY-MM-DD", 1, "week") %>)
- [ ] 
- [ ] 
- [ ] 
## Wednesday (<% tp.date.now("YYYY-MM-DD", 2, "week") %>)
- [ ] 
- [ ] 
- [ ] 
## Thursday (<% tp.date.now("YYYY-MM-DD", 3, "week") %>)
- [ ] 
- [ ] 
- [ ] 
## Friday (<% tp.date.now("YYYY-MM-DD", 4, "week") %>)
- [ ] 
- [ ] 
- [ ] 
## Saturday (<% tp.date.now("YYYY-MM-DD", 5, "week") %>)
- [ ] 
- [ ] 
- [ ] 
## Sunday (<% tp.date.now("YYYY-MM-DD", 6, "week") %>)
- [ ] 
- [ ] 
- [ ] 
## Weekly Goals
1. 
2. 
3. 
## Resources Needed
- 
## Potential Obstacles
- 
## Success Metrics
- 
```

---
## Advanced Templates

---
### Advanced Research Synthesis Template
**Description**: This template creates a comprehensive research synthesis by aggregating information from multiple sources, generating literature connections, and creating a structured analysis framework. It uses user scripts to parse reference data, creates multiple interlinked notes, and generates a visual summary of research landscape.
**Top Use Cases**:
1. Synthesizing research for literature reviews across multiple papers
2. Creating domain overviews when entering new research areas
3. Building comprehensive knowledge maps for complex topics
**Implementation Tips**:
4. Requires the "Research Synthesis" user script (provided separately) for reference parsing
5. Works best with consistent folder structure for literature notes
6. May require manual adjustment of generated connections for accuracy
**Customization Options**:
7. Modify the synthesis framework to match specific domain requirements
8. Add additional analysis dimensions (methodology, sample characteristics, etc.)
9. Integrate with Dataview for dynamic literature querying
```
<%*
// Import user script for reference parsing
const { parseReferences, generateConnections } = await tp.user.research_synthesis();
// Get synthesis topic
let topic = tp.file.title.replace("Synthesis - ", "");
let focusQuestion = await tp.system.prompt("Central research question:");
// Create synthesis folder
let folderPath = `02-projects/${topic.replace(/\s+/g, '-')}-synthesis`;
// Create main synthesis note
let mainContent = `---
type: synthesis
title: "${topic} Research Synthesis"
focus-question: "${focusQuestion}"
status: active
tags: [synthesis, analysis, cognitive-science]
created: ${tp.date.now("YYYY-MM-DD")}
---
# ${topic} Research Synthesis
## Focus Question
${focusQuestion}
## Executive Summary
<% tp.system.prompt("Brief summary of key findings:") %>
## Research Landscape Overview
<%*
let domains = await tp.system.prompt("Key research domains (comma-separated):");
tR += domains.split(',').map(d => `- ${d.trim()}`).join('\n');
%>
## Synthesis Framework
### Conceptual Model
\`\`\`mermaid
graph TD
    A[Core Concept] --> B[Key Variables]
    A --> C[Contextual Factors]
    B --> D[Outcomes]
    C --> D
\`\`\`
### Key Relationships
<% tp.system.prompt("Describe key theoretical relationships:") %>
## Literature Integration
### Foundational Papers
- 
### Recent Developments
- 
### Contradictory Findings
- 
## Methodological Patterns
### Common Approaches
- 
### Emerging Methods
- 
### Limitations
- 
## Synthesis Outcomes
### Integrated Understanding
<% tp.system.prompt("Synthesized understanding across studies:") %>
### Gaps in Knowledge
1. 
2. 
3. 
### Future Research Directions
1. 
2. 
3. 
## Generated Notes
- [[${topic.replace(/\s+/g, '-')}-literature-map]]
- [[${topic.replace(/\s+/g, '-')}-methodology-review]]
- [[${topic.replace(/\s+/g, '-')}-theoretical-framework]]`;
// Create literature map note
let mapContent = `---
type: moc
title: "${topic} Literature Map"
category: synthesis
status: active
tags: [moc, literature-map, cognitive-science]
---
# ${topic} Literature Map
## Key Papers by Domain
<%*
let papers = await tp.system.prompt("Enter key papers (format: Author (Year) - Title)");
tR += papers.split('\n').map(p => `- ${p}`).join('\n');
%>
## Connection Analysis
\`\`\`mermaid
graph LR
    A[Paper 1] --> B[Paper 2]
    B --> C[Paper 3]
    A --> C
    D[Paper 4] --> B
\`\`\`
## Citation Network
- `;
// Create methodology review note
let methodContent = `---
type: analysis
title: "${topic} Methodology Review"
focus: ${topic}
status: active
tags: [analysis, methodology, cognitive-science]
---
# ${topic} Methodology Review
## Common Methodologies
1. 
## Sample Characteristics
- 
## Measurement Approaches
- 
## Analytical Techniques
- 
## Validity Considerations
- `;
// Create theoretical framework note
let theoryContent = `---
type: framework
title: "${topic} Theoretical Framework"
domain: ${topic}
status: developing
tags: [framework, theory, cognitive-science]
---
# ${topic} Theoretical Framework
## Core Constructs
- 
## Proposed Relationships
- 
## Boundary Conditions
- 
## Testable Hypotheses
1. `;
// Create all files
await tp.file.create_new(mainContent, `Synthesis - ${topic}`, true, folderPath);
await tp.file.create_new(mapContent, `${topic.replace(/\s+/g, '-')}-literature-map`, true, folderPath);
await tp.file.create_new(methodContent, `${topic.replace(/\s+/g, '-')}-methodology-review`, true, folderPath);
await tp.file.create_new(theoryContent, `${topic.replace(/\s+/g, '-')}-theoretical-framework`, true, folderPath);
// Return success message
tR += `Research synthesis for "${topic}" created successfully in ${folderPath}`;
%>
```

---
### Multi-Stage Experiment Documentation Template
**Description**: This template creates a complete experimental research workflow including hypothesis generation, methodology design, data collection templates, analysis plans, and results documentation. It dynamically generates appropriate templates based on experimental design choices and creates a linked network of research artifacts.
**Top Use Cases**:
1. Planning and documenting behavioral experiments in cognitive science
2. Creating reproducible research workflows for collaborative projects
3. Generating standardized documentation for IRB submissions
**Implementation Tips**:
4. Requires the "Experiment Design" user script for design pattern generation
5. Best used with consistent naming conventions for data files
6. Consider customizing data templates for specific experimental paradigms
**Customization Options**:
7. Add additional data collection modalities (neuroimaging, eye-tracking, etc.)
8. Modify analysis templates for specific statistical approaches
9. Extend participant management features for different recruitment strategies
```
<%*
// Import experiment design utilities
const { generateDesign, createDataTemplate } = await tp.user.experiment_design();
// Get experiment details
let expName = tp.file.title.replace("Experiment - ", "");
let expType = await tp.system.suggester(
  ["Behavioral", "Survey", "Computational Modeling", "Meta-Analysis"], 
  ["behavioral", "survey", "modeling", "meta"]
);
let hypothesis = await tp.system.prompt("Primary hypothesis:");
let nParticipants = await tp.system.prompt("Expected N:");
let duration = await tp.system.prompt("Estimated duration (minutes):");
// Create experiment folder structure
let expFolder = `02-projects/experiments/${expName.replace(/\s+/g, '-')}`;
let dataFolder = `${expFolder}/data`;
let analysisFolder = `${expFolder}/analysis`;
let docsFolder = `${expFolder}/documentation`;
// Create main experiment note
let mainContent = `---
type: experiment
title: "Experiment: ${expName}"
exp-type: ${expType}
status: planning
n-participants: ${nParticipants}
duration: ${duration}
hypothesis: "${hypothesis}"
tags: [experiment, research, cognitive-science]
created: ${tp.date.now("YYYY-MM-DD")}
---
# Experiment: ${expName}
## Research Question
${hypothesis}
## Experimental Design
<%*
let design = generateDesign(expType);
tR += Object.entries(design).map(([k, v]) => `${k}: ${v}`).join('\n');
%>
## Methodology
### Participants
- Target N: ${nParticipants}
- Recruitment: 
- Inclusion Criteria: 
- Exclusion Criteria: 
### Materials
- 
### Procedure
1. 
### Design Considerations
- 
## Ethics & Compliance
- IRB Status: 
- Data Protection: 
- Consent Process: 
## Timeline
| Phase | Start | End | Milestones |
|-------|-------|-----|------------|
| Planning | | | IRB Approval |
| Recruitment | | | First Participant |
| Data Collection | | | 50% Complete |
| Analysis | | | Results Draft |
| Reporting | | | Final Submission |
## Related Documents
- [[${expName.replace(/\s+/g, '-')}-protocol]]
- [[${expName.replace(/\s+/g, '-')}-consent-form]]
- [[${expName.replace(/\s+/g, '-')}-data-dictionary]]`;
// Create protocol document
let protocolContent = `---
type: protocol
title: "${expName} Experimental Protocol"
experiment: ${expName}
status: draft
tags: [protocol, methodology, cognitive-science]
---
# ${expName} Experimental Protocol
## Overview
${hypothesis}
## Detailed Procedure
### Pre-Experiment
1. 
### Experiment Session
1. 
### Post-Experiment
1. 
## Stimuli Description
- 
## Response Collection
- 
## Quality Control
- 
## Troubleshooting Guide
- `;
// Create consent form template
let consentContent = `---
type: document
title: "${expName} Consent Form"
document-type: consent
status: draft
tags: [consent, ethics, cognitive-science]
---
# ${expName} Consent Form
## Introduction
You are invited to participate in a research study titled "${expName}" conducted by [Institution]. This study aims to ${hypothesis.toLowerCase()}.
## Procedures
During this study, you will ${await tp.system.prompt("Describe study procedures:")}.
## Risks and Benefits
### Potential Risks
- 
### Potential Benefits
- 
## Confidentiality
Your responses will be kept confidential and used solely for research purposes.
## Voluntary Participation
Participation is voluntary. You may withdraw at any time without penalty.
## Contact Information
For questions about this research, contact [Researcher Name] at [Email].
## Consent
I have read this consent form and have had the opportunity to ask questions. I consent to participate in this research.
Participant Signature: _________________ Date: _______
Researcher Signature: _________________ Date: _______`;
// Create data dictionary
let dataContent = `---
type: reference
title: "${expName} Data Dictionary"
experiment: ${expName}
status: draft
tags: [data, reference, cognitive-science]
---
# ${expName} Data Dictionary
## Data Files
| File | Description | Format | Variables |
|------|-------------|--------|-----------|
| ${expName.toLowerCase().replace(/\s+/g, '_')}_raw.csv | Raw experimental data | CSV |  |
| ${expName.toLowerCase().replace(/\s+/g, '_')}_demographics.csv | Participant information | CSV |  |
| ${expName.toLowerCase().replace(/\s+/g, '_')}_exclusion.csv | Excluded participants | CSV |  |
## Key Variables
| Variable | Description | Type | Range/Levels |
|----------|-------------|------|--------------|
| participant_id | Unique identifier | String |  |
| condition | Experimental condition | Factor |  |
| rt | Response time | Numeric |  |
| accuracy | Correct/incorrect | Binary | 0, 1 |
## Data Validation Rules
- 
## Processing Steps
1. `;
// Create data collection template
let collectionContent = createDataTemplate(expType, expName);
// Create analysis plan
let analysisContent = `---
type: analysis
title: "${expName} Analysis Plan"
experiment: ${expName}
status: planned
tags: [analysis, statistics, cognitive-science]
---
# ${expName} Analysis Plan
## Primary Analyses
### Hypothesis Test
To test our primary hypothesis that ${hypothesis.toLowerCase()}, we will:
1. 
### Statistical Approach
- 
### Assumptions
- 
## Secondary Analyses
- 
## Exploratory Analyses
- 
## Power Analysis
- Target Effect Size: 
- Required N: ${nParticipants}
- Actual Power: 
## Data Exclusion Criteria
- 
## Missing Data Strategy
- `;
// Create results template
let resultsContent = `---
type: report
title: "${expName} Results Report"
experiment: ${expName}
status: planned
tags: [results, report, cognitive-science]
---
# ${expName} Results Report
## Abstract
<% tp.system.prompt("Experiment abstract:") %>
## Introduction
### Background
- 
### Hypothesis
${hypothesis}
## Method
### Participants
- N (analyzed): 
- Demographics: 
### Materials
- 
### Procedure
- 
### Design
- 
## Results
### Data Exclusion
- 
### Primary Analysis
- 
### Secondary Analyses
- 
## Discussion
### Interpretation
- 
### Limitations
- 
### Future Directions
- 
## References
- `;
// Create all files
await tp.file.create_new(mainContent, `Experiment - ${expName}`, true, expFolder);
await tp.file.create_new(protocolContent, `${expName.replace(/\s+/g, '-')}-protocol`, true, docsFolder);
await tp.file.create_new(consentContent, `${expName.replace(/\s+/g, '-')}-consent-form`, true, docsFolder);
await tp.file.create_new(dataContent, `${expName.replace(/\s+/g, '-')}-data-dictionary`, true, docsFolder);
await tp.file.create_new(collectionContent, `${expName.replace(/\s+/g, '-')}-data-template`, true, dataFolder);
await tp.file.create_new(analysisContent, `${expName.replace(/\s+/g, '-')}-analysis-plan`, true, analysisFolder);
await tp.file.create_new(resultsContent, `${expName.replace(/\s+/g, '-')}-results`, true, docsFolder);
// Return success message
tR += `Experiment documentation for "${expName}" created successfully in ${expFolder}`;
%>
```

---
### Intelligent Literature Management System
**Description**: This template creates an automated literature management system that processes references, generates reading queues, tracks reading progress, and creates knowledge connections. It integrates with web APIs to fetch publication metadata and uses natural language processing to extract key concepts.
**Top Use Cases**:
1. Managing large literature collections for systematic reviews
2. Creating personalized reading plans based on research interests
3. Building knowledge networks from annotated references
**Implementation Tips**:
4. Requires CrossRef API access for metadata fetching
5. Best combined with Zotero or similar reference manager
6. Consider implementing rate limiting for API calls
**Customization Options**:
7. Add integration with institutional library databases
8. Customize concept extraction for specific domains
9. Extend with collaborative annotation features
```
<%*
// Import literature management utilities
const { fetchMetadata, extractConcepts, generateQueue } = await tp.user.literature_manager();
// Get collection name
let collectionName = tp.file.title.replace("Literature - ", "");
let focusArea = await tp.system.prompt("Research focus area:");
// Create literature folder
let litFolder = `04-library/${collectionName.replace(/\s+/g, '-')}`;
let queueFolder = `${litFolder}/reading-queue`;
let processedFolder = `${litFolder}/processed`;
// Create main literature collection note
let mainContent = `---
type: moc
title: "Literature Collection: ${collectionName}"
category: literature
focus-area: ${focusArea}
status: active
tags: [literature, moc, cognitive-science, ${focusArea.toLowerCase().replace(/\s+/g, '-')}] 
created: ${tp.date.now("YYYY-MM-DD")}
---
# Literature Collection: ${collectionName}
## Focus Area
${focusArea}
## Collection Statistics
- Total References: 
- Processed: 
- In Queue: 
- Priority High: 
## Key Concepts
<%*
let concepts = await tp.system.prompt("Key concepts in this literature (comma-separated):");
tR += concepts.split(',').map(c => `- ${c.trim()}`).join('\n');
%>
## Reading Queue
\`\`\`dataview
TABLE priority, status, estimated-time
FROM "${queueFolder}"
SORT priority DESC
\`\`\`
## Recently Processed
\`\`\`dataview
TABLE completed-date, rating
FROM "${processedFolder}"
SORT completed-date DESC
LIMIT 5
\`\`\`
## Concept Map
\`\`\`mermaid
graph TD
    A[${focusArea}] --> B[Concept 1]
    A --> C[Concept 2]
    B --> D[Sub-concept 1]
    C --> E[Sub-concept 2]
\`\`\`
## Search Interface
\`[[Search Literature]]\`
## Add References
\`[[Add to ${collectionName}]]\``;
// Create reading queue manager
let queueContent = `---
type: dashboard
title: "${collectionName} Reading Queue"
category: queue
status: active
tags: [queue, dashboard, literature]
---
# ${collectionName} Reading Queue
## Queue Management
### Add New Item
\`\`\`button
name Add Reference
type command
action Templater: Open insert template modal
templater true
\`\`\`
### Process Queue
\`\`\`button
name Start Reading
type command
action QuickAdd: Run QuickAdd
\`\`\`
## Current Queue
\`\`\`dataview
TABLE priority AS "Priority", status AS "Status", estimated-time AS "Time", due-date AS "Due"
FROM "${queueFolder}"
WHERE status != "completed"
SORT priority DESC
\`\`\`
## Completed This Week
\`\`\`dataview
TABLE completed-date AS "Completed", rating AS "Rating"
FROM "${processedFolder}"
WHERE completed-date >= date(today) - dur(7 days)
SORT completed-date DESC
\`\`\`
## Statistics
- Queue Length: 
- Average Rating: 
- Completion Rate: `;
// Create search interface
let searchContent = `---
type: tool
title: "Literature Search: ${collectionName}"
category: search
status: active
tags: [search, tool, literature]
---
# Literature Search: ${collectionName}
## Search by Concept
\`\`\`input
type: text
label: Concept
placeholder: Enter concept to search for...
\`\`\`
## Search by Author
\`\`\`input
type: text
label: Author
placeholder: Enter author name...
\`\`\`
## Search by Year
\`\`\`input
type: number
label: Year
placeholder: Enter publication year...
\`\`\`
## Advanced Search
\`\`\`button
name Advanced Search
type command
action Dataview: Open search
\`\`\`
## Recent Additions
\`\`\`dataview
TABLE author AS "Author", year AS "Year", rating AS "Rating"
FROM "${litFolder}"
SORT created DESC
LIMIT 10
\`\`\``;
// Create reference addition template
let addContent = `<%*
let refType = await tp.system.suggester(
  ["DOI", "ISBN", "Citation", "File Upload"], 
  ["doi", "isbn", "citation", "file"]
);
let refData;
if (refType === "doi") {
  let doi = await tp.system.prompt("Enter DOI:");
  refData = await fetchMetadata("doi", doi);
} else if (refType === "isbn") {
  let isbn = await tp.system.prompt("Enter ISBN:");
  refData = await fetchMetadata("isbn", isbn);
} else if (refType === "citation") {
  let citation = await tp.system.prompt("Enter full citation:");
  refData = await fetchMetadata("citation", citation);
} else {
  // Handle file upload case
  refData = {
    title: await tp.system.prompt("Enter title:"),
    author: await tp.system.prompt("Enter author(s):"),
    year: await tp.system.prompt("Enter year:"),
    journal: await tp.system.prompt("Enter journal (if applicable):")
  };
}
let priority = await tp.system.suggester(["Low", "Medium", "High", "Urgent"], ["low", "medium", "high", "urgent"]);
let estimatedTime = await tp.system.prompt("Estimated reading time (minutes):");
let refContent = \`---
type: reference
title: "\${refData.title}"
author: "\${refData.author}"
year: \${refData.year}
journal: "\${refData.journal || ''}"
status: queued
priority: ${priority}
estimated-time: ${estimatedTime}
tags: [reference, literature, cognitive-science, ${focusArea.toLowerCase().replace(/\s+/g, '-')}] 
created: ${tp.date.now("YYYY-MM-DD")}
---
# \${refData.title}
## Metadata
- **Author**: \${refData.author}
- **Year**: \${refData.year}
- **Journal**: \${refData.journal || 'N/A'}
- **DOI**: \${refData.doi || 'N/A'}
## Abstract
\${refData.abstract || 'No abstract available.'}
## Key Concepts
<%*
let refConcepts = extractConcepts(refData.abstract || refData.title);
tR += refConcepts.map(c => \`- \${c}\`).join('\\n');
%>
## Reading Queue
- **Priority**: ${priority}
- **Status**: queued
- **Estimated Time**: ${estimatedTime} minutes
## Notes
- 
## Quotes
- 
## Related References
- 
## Action Items
- [ ] Add to reading queue
- [ ] Set reminder
- [ ] Share with colleagues\`;
await tp.file.create_new(refContent, refData.title.replace(/[^a-zA-Z0-9]/g, '-'), true, queueFolder);
tR += \`Reference "\${refData.title}" added to queue.\`;
%>`;
// Create processing template
let processContent = `<%*
// Get next item in queue
let queueItems = await tp.user.get_queue_items(queueFolder);
if (queueItems.length === 0) {
  tR += "No items in queue.";
  return;
}
let currentItem = queueItems[0];
let itemTitle = currentItem.file.name;
let rating = await tp.system.suggester(
  ["5 - Essential", "4 - Highly Recommended", "3 - Recommended", "2 - Interesting", "1 - Background Only"], 
  [5, 4, 3, 2, 1]
);
let status = await tp.system.suggester(
  ["Completed", "In Progress", "Skipped"], 
  ["completed", "in-progress", "skipped"]
);
let completionDate = status === "completed" ? tp.date.now("YYYY-MM-DD") : "";
// Update item status
let updatedContent = await tp.user.update_reference_status(
  currentItem, 
  status, 
  rating, 
  completionDate
);
// Move to processed folder if completed
if (status === "completed") {
  await tp.file.move(currentItem.file.path, processedFolder);
}
// Generate related connections
let connections = await tp.user.generate_connections(currentItem, litFolder);
tR += \`Processed "\${itemTitle}". Generated \${connections.length} new connections.\`;
%>`;
// Create all files
await tp.file.create_new(mainContent, `Literature - ${collectionName}`, true, litFolder);
await tp.file.create_new(queueContent, `${collectionName.replace(/\s+/g, '-')}-queue`, true, litFolder);
await tp.file.create_new(searchContent, `Search ${collectionName}`, true, litFolder);
await tp.file.create_new(addContent, `Add to ${collectionName}`, true, litFolder);
await tp.file.create_new(processContent, `Process ${collectionName} Queue`, true, litFolder);
// Return success message
tR += `Literature management system for "${collectionName}" created successfully in ${litFolder}`;
%>
```

---
## Synergy Templates (Plugin Integration)

---
### QuickAdd + Templater Research Capture Workflow
**Description**: This template integrates with QuickAdd to create a powerful research capture workflow that automatically processes web clips, generates metadata, and files them appropriately. It uses Templater's web capabilities alongside QuickAdd's capture features to streamline the research ingestion process.
**Top Use Cases**:
1. Capturing research articles and web content during literature reviews
2. Processing daily research findings into structured notes
3. Creating annotated bibliographies from captured sources
**Implementation Tips**:
4. Requires QuickAdd plugin with properly configured capture options
5. Best used with a consistent folder structure for different content types
6. Consider customizing metadata extraction for specific domains
**Customization Options**:
7. Add integration with reference managers like Zotero
8. Extend with automatic tagging based on content analysis
9. Include OCR processing for image-based content
```
<%*
// This template is designed to work with QuickAdd capture
// It processes captured content and creates structured notes
// Get captured content from QuickAdd
let capturedTitle = tp.system.clipboard();
let capturedUrl = await tp.system.prompt("Source URL (if applicable):", "");
let contentType = await tp.system.suggester(
  ["Research Paper", "Blog Post", "News Article", "Book Chapter", "Other"], 
  ["paper", "blog", "news", "chapter", "other"]
);
// Generate filename from title
let fileName = capturedTitle.replace(/[^a-zA-Z0-9]/g, '-').toLowerCase();
// Determine folder based on content type
let folder;
switch(contentType) {
  case "paper":
    folder = "04-library/research-papers";
    break;
  case "blog":
    folder = "04-library/blog-posts";
    break;
  case "news":
    folder = "04-library/news-articles";
    break;
  case "chapter":
    folder = "04-library/book-chapters";
    break;
  default:
    folder = "04-library/miscellaneous";
}
// Create structured note content
let noteContent = `---
type: <% contentType %>
title: "${capturedTitle}"
source-url: "${capturedUrl}"
capture-date: ${tp.date.now("YYYY-MM-DD")}
status: queued
tags: [captured, <% contentType %>, cognitive-science]
---
# <% capturedTitle %>
## Source Information
- **URL**: <% capturedUrl %>
- **Captured**: ${tp.date.now("YYYY-MM-DD")}
- **Type**: <% contentType.charAt(0).toUpperCase() + contentType.slice(1) %>
## Quick Summary
<% tp.system.prompt("Enter a quick summary of the content:") %>
## Key Points
1. 
## Relevance to Research
<% tp.system.prompt("How is this relevant to your current work?") %>
## Action Items
- [ ] <% tp.system.prompt("First action item:") %>
- [ ] <% tp.system.prompt("Second action item:") %>
- [ ] <% tp.system.prompt("Third action item:") %>
## Full Text/Notes
<% tp.system.prompt("Paste full text or detailed notes here:") %>
## Related Notes
- 
## Tags
<% tp.system.prompt("Additional tags (comma-separated):") %>

---
*Captured using QuickAdd + Templater workflow*`;
// Create the note using Templater's file creation
await tp.file.create_new(noteContent, fileName, true, folder);
// Return success message for QuickAdd
tR += `Successfully captured "${capturedTitle}" to ${folder}/${fileName}`;
%>
```

---
### Dataview + Templater Dynamic Dashboard Generator
**Description**: This template creates dynamic dashboards that automatically aggregate and display information from across your PKB using Dataview queries embedded within Templater templates. It generates personalized overviews based on tags, status, and other metadata.
**Top Use Cases**:
1. Creating weekly research progress dashboards
2. Generating project status overviews for team meetings
3. Building personalized learning dashboards based on interests
**Implementation Tips**:
4. Requires Dataview plugin to be installed and enabled
5. Works best with consistent metadata across notes
6. Consider performance implications for large databases
**Customization Options**:
7. Add custom CSS styling for dashboard elements
8. Extend with interactive filtering capabilities
9. Include data visualization components using mermaid
```
<%*
// Dashboard Generator Template
// Creates dynamic dashboards using Dataview integration
let dashboardName = tp.file.title.replace("Dashboard - ", "");
let focusArea = await tp.system.prompt("Dashboard focus area (e.g., cognitive-science, research-projects):");
let timeRange = await tp.system.suggester(
  ["This Week", "This Month", "Last 30 Days", "All Time"], 
  ["week", "month", "30days", "all"]
);
// Determine date filter based on selection
let dateFilter;
switch(timeRange) {
  case "week":
    dateFilter = "date(today) - dur(7 days)";
    break;
  case "month":
    dateFilter = "date(today) - dur(30 days)";
    break;
  case "30days":
    dateFilter = "date(today) - dur(30 days)";
    break;
  default:
    dateFilter = "date(1900-01-01)"; // Effectively no date filter
}
// Create dashboard content with Dataview queries
let dashboardContent = `---
type: dashboard
title: "${dashboardName}"
focus-area: ${focusArea}
time-range: ${timeRange}
status: active
tags: [dashboard, overview, ${focusArea}]
created: ${tp.date.now("YYYY-MM-DD")}
---
# ${dashboardName}
## Overview
This dashboard provides an overview of activities and content related to **${focusArea}** for **${timeRange === "all" ? "all time" : "the past " + (timeRange === "week" ? "7 days" : "30 days")}**.
## Recent Activity
\`\`\`dataview
TABLE type AS "Type", status AS "Status", created AS "Created"
FROM "/"
WHERE contains(tags, "${focusArea}") AND created >= ${dateFilter}
SORT created DESC
LIMIT 10
\`\`\`
## By Status
\`\`\`dataview
TABLE COUNT(rows.file.link) AS "Count"
FROM "/"
WHERE contains(tags, "${focusArea}")
GROUP BY status
\`\`\`
## By Type
\`\`\`dataview
TABLE COUNT(rows.file.link) AS "Count"
FROM "/"
WHERE contains(tags, "${focusArea}")
GROUP BY type
\`\`\`
## Priority Items
\`\`\`dataview
TABLE priority AS "Priority", status AS "Status", created AS "Created"
FROM "/"
WHERE contains(tags, "${focusArea}") AND contains(tags, "high") OR contains(tags, "urgent")
SORT priority DESC
\`\`\`
## Recently Completed
\`\`\`dataview
TABLE completed AS "Completed", rating AS "Rating"
FROM "/"
WHERE contains(tags, "${focusArea}") AND status = "completed" AND completed >= ${dateFilter}
SORT completed DESC
LIMIT 5
\`\`\`
## Upcoming Deadlines
\`\`\`dataview
TABLE due-date AS "Due", priority AS "Priority"
FROM "/"
WHERE contains(tags, "${focusArea}") AND due-date >= date(today) AND status != "completed"
SORT due-date ASC
LIMIT 5
\`\`\`
## Knowledge Gaps
\`\`\`dataview
TABLE type AS "Type", maturity AS "Maturity"
FROM "/"
WHERE contains(tags, "${focusArea}") AND (maturity = "seedling" OR maturity = "developing")
SORT maturity ASC
\`\`\`
## Statistics
- Total Items: 
- Active Items: 
- Completed Items: 
- Average Rating: 
*Dashboard generated on ${tp.date.now("YYYY-MM-DD HH:mm")}*`;
// Create dashboard note
await tp.file.create_new(dashboardContent, `Dashboard - ${dashboardName}`, true, "06-dashboards");
// Return success message
tR += `Dashboard "${dashboardName}" created successfully in 06-dashboards`;
%>
```


# Templater Templates for AI Research & Cognitive Science Knowledge Base

---
## Basic Templates
*Simple templates perfect for getting started with basic note creation and metadata generation.*

---
## Basic Templates
### Simple Note Template with Metadata
A fundamental template that creates basic frontmatter with the current date and note title.
```
---
id: <% tp.date.now("YYYYMMDDHHmmss") %>
title: <% tp.file.title %>
created: <% tp.date.now("YYYY-MM-DD HH:mm:ss") %>
type: reference
tags:
  - #status/seedling
---
# <% tp.file.title %>
## Overview
## Key Points
## References
```
### Daily AI Research Note Template
Perfect for creating daily research tracking notes with automatic date formatting.
```
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: daily-research
tags:
  - #daily-research
  - #ai-research
week: [[<% tp.date.now("gggg-[W]WW") %>]]
---
# <% tp.date.now("dddd, MMMM Do YYYY") %> - AI Research Log
## Today's Focus
## Papers Read
## Experiments Conducted
## Key Insights
## Tomorrow's Plan
```
### Simple Permanent Note Template
A clean template for creating permanent notes with basic linking structure.
```
---
id: <% tp.date.now("YYYYMMDDHHmmss") %>
title: <% tp.file.title %>
type: permanent-note
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #type/permanent
  - #status/seedling
source: ""
---
# <% tp.file.title %>
## Definition
## Key Concepts
## Applications
## Related Notes
- [[<% tp.date.now("YYYY-MM-DD") %>]]
## References
```
### Quick Capture Template
A minimal template for quickly capturing ideas with automatic timestamping.
```
---
captured: <% tp.date.now("YYYY-MM-DD HH:mm:ss") %>
type: quick-capture
tags:
  - #inbox
  - #quick-capture
---
# Quick Capture - <% tp.date.now("HH:mm") %>
## Idea
## Context
## Next Steps
## Tags
```

---
## Intermediate Templates
*Templates that demonstrate conditional logic, user interaction, and more sophisticated automation.*
### Smart Research Note Template
This template prompts for research details and automatically generates appropriate metadata based on user input.
```
<%*
const title = await tp.system.prompt("Research Note Title:");
const researchType = await tp.system.suggester(
  ["Paper Analysis", "Experiment Log", "Literature Review", "Concept Definition"],
  ["paper-analysis", "experiment-log", "literature-review", "concept-definition"]
);
const aiModel = await tp.system.suggester(
  ["Claude Opus 4.1", "Claude Sonnet 4.5", "Gemini Pro 2.5", "Gemini Flash 2.5", "Other"],
  ["claude-opus-4.1", "claude-sonnet-4.5", "gemini-pro-2.5", "gemini-flash-2.5", "other"]
);
const tags = await tp.system.prompt("Additional tags (comma separated):", "");
_%>
---
id: <% tp.date.now("YYYYMMDDHHmmss") %>
title: <% title %>
type: <% researchType %>
source: <% aiModel %>
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #type/<% researchType.replace('-', '/') %>
  - #source/<% aiModel.replace('-', '/') %>
  <% if (tags) { -%>
  <% tags.split(',').forEach(tag => { -%>
  - "<% tag.trim() %>"
  <% }); -%>
  <% } -%>
  - #status/seedling
maturity: seedling
confidence: provisional
---
# <% title %>
## Overview
## Key Findings
## Methodology
## Results
## Analysis
## References
```
### MOC-Linked Note Template
This template intelligently links notes to relevant Maps of Content based on topic selection.
```
<%*
const noteTitle = tp.file.title.includes("Untitled") ? await tp.system.prompt("Note Title:") : tp.file.title;
const domain = await tp.system.suggester(
  ["AI/ML", "Cognitive Science", "Educational Psychology", "Cosmology", "PKM"],
  ["artificial-intelligence-moc", "cognitive-science-moc", "educational-psychology-moc", "cosmology-moc", "pkb-&-pkm-moc"]
);
const noteType = await tp.system.suggester(
  ["Concept", "Framework", "Theory", "Mental Model", "Principle"],
  ["concept", "framework", "theory", "mental-model", "principle"]
);
const maturity = await tp.system.suggester(
  ["Seedling - New idea", "Developing - Taking shape", "Budding - Well-formed", "Evergreen - Mature"],
  ["seedling", "developing", "budding", "evergreen"]
);
_%>
---
id: <% tp.date.now("YYYYMMDDHHmmss") %>
title: <% noteTitle %>
type: <% noteType %>
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #type/<% noteType %>
  - #status/<% maturity %>
  - #year/<% tp.date.now("YYYY") %>
maturity: <% maturity %>
confidence: provisional
link-up:
  - "[[<% domain %>]]"
---
# <% noteTitle %>
## Definition
## Core Principles
## Applications
## Related Concepts
## References
## Connections
- Linked to: [[<% domain %>]]
```
### Project Initialization Template
Creates a comprehensive project structure with multiple files and folder organization.
```
<%*
const projectName = await tp.system.prompt("Project Name:");
const projectType = await tp.system.suggester(
  ["Research Project", "AI Experiment", "Literature Review", "Tutorial Creation"],
  ["research-project", "ai-experiment", "literature-review", "tutorial-creation"]
);
const projectFolder = await tp.system.prompt("Project Folder Name (no spaces):", projectName.toLowerCase().replace(/\s+/g, '-'));
const projectDescription = await tp.system.prompt("Project Description:");
// Create project folder and files
await tp.file.create_new("02-projects/" + projectFolder + "/" + projectFolder + "-overview.md", false, true);
await tp.file.create_new("02-projects/" + projectFolder + "/" + projectFolder + "-research.md", false, true);
await tp.file.create_new("02-projects/" + projectFolder + "/" + projectFolder + "-notes.md", false, true);
await tp.file.create_new("02-projects/" + projectFolder + "/" + projectFolder + "-results.md", false, true);
_%>
---
id: <% tp.date.now("YYYYMMDDHHmmss") %>
title: <% projectName %>
type: project-overview
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #type/project
  - #project/<% projectFolder %>
status: active
priority: medium
---
# <% projectName %> - Project Overview
## Description
<% projectDescription %>
## Project Type
<% projectType.replace('-', ' ').replace(/\b\w/g, l => l.toUpperCase()) %>
## Project Structure
- [[<% projectFolder %>-overview|Overview]]
- [[<% projectFolder %>-research|Research]]
- [[<% projectFolder %>-notes|Notes]]
- [[<% projectFolder %>-results|Results]]
## Goals
## Timeline
## Resources
## Team
## Status Updates
```
### Literature Review Template
A sophisticated template for conducting systematic literature reviews with automated tagging.
```
<%*
const paperTitle = await tp.system.prompt("Paper Title:");
const authors = await tp.system.prompt("Authors (comma separated):");
const publicationYear = await tp.system.prompt("Publication Year:");
const journal = await tp.system.prompt("Journal/Source:");
const aiModel = await tp.system.suggester(
  ["Human Author", "Claude Opus 4.1", "Claude Sonnet 4.5", "Gemini Pro 2.5", "Gemini Flash 2.5"],
  ["human", "claude-opus-4.1", "claude-sonnet-4.5", "gemini-pro-2.5", "gemini-flash-2.5"]
);
const domain = await tp.system.suggester(
  ["AI/ML", "Cognitive Science", "Educational Psychology", "Cosmology"],
  ["ai-ml", "cognitive-science", "educational-psychology", "cosmology"]
);
const methodology = await tp.system.prompt("Research Methodology:");
const sampleSize = await tp.system.prompt("Sample Size (if applicable):", "N/A");
_%>
---
id: <% tp.date.now("YYYYMMDDHHmmss") %>
title: <% paperTitle %>
type: literature
source: <% aiModel === "human" ? "human-research" : aiModel %>
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #type/literature
  - #domain/<% domain %>
  - #year/<% publicationYear %>
  - #status/read
authors: [<% authors %>]
year: <% publicationYear %>
journal: <% journal %>
methodology: <% methodology %>
sample-size: <% sampleSize %>
confidence: established
maturity: evergreen
---
# <% paperTitle %>
## Authors
<% authors %>
## Publication Details
- **Year**: <% publicationYear %>
- **Journal**: <% journal %>
- **Source**: <% aiModel === "human" ? "Human Research" : aiModel.replace('-', ' ').replace(/\b\w/g, l => l.toUpperCase()) %>
## Abstract
## Research Question
## Methodology
<% methodology %>
## Sample
<% sampleSize %>
## Key Findings
## Limitations
## Implications
## Related Literature
## Critical Analysis
## Applications
## References
```

---
## Advanced Templates
### AI Research Synthesis Template
This sophisticated template creates a comprehensive research synthesis by automatically generating related notes, cross-references, and organizing content into a structured knowledge base format. It intelligently connects new research with existing knowledge, creates MOC entries when needed, and generates follow-up tasks for deeper exploration.
**Top Use Cases:**
1. Synthesizing multiple AI research papers into a cohesive knowledge structure
2. Creating comprehensive literature reviews that automatically link to related concepts
3. Building out new domains in your PKB by connecting disparate research findings
**Implementation Tips:**
- Requires the Dataview plugin for advanced querying capabilities
- Best used with a well-organized tag system for automatic linking
- Should be run from a dedicated research folder to maintain organization
- Consider setting up automatic folder creation for new domains/MOCs
**Customization Options:**
1. Modify the domain detection logic to match your specific research areas
2. Add integration with reference management tools like Zotero via QuickAdd
3. Extend the template to automatically generate visualization-ready data for tools like Logseq
```
<%*
/* ═══════════════════════════════════════════════════════════════════════
   🧠 AI RESEARCH SYNTHESIS TEMPLATE
   Advanced Knowledge Synthesis & Organization System
   ═══════════════════════════════════════════════════════════════════════ */
// Configuration
const DOMAINS = {
  "ai-ml": {
    tags: ["#ai-ml", "#machine-learning", "#artificial-intelligence", "#neural-networks"],
    moc: "artificial-intelligence-moc",
    folder: "03-notes/ai-ml/"
  },
  "cognitive-science": {
    tags: ["#cognitive-science", "#psychology", "#neuroscience", "#learning-theory"],
    moc: "cognitive-science-moc",
    folder: "03-notes/cognitive-science/"
  },
  "educational-psychology": {
    tags: ["#educational-psychology", "#learning", "#instructional-design", "#pedagogy"],
    moc: "educational-psychology-moc",
    folder: "03-notes/educational-psychology/"
  },
  "pkm": {
    tags: ["#pkm", "#pkb", "#knowledge-management", "#note-taking"],
    moc: "pkb-&-pkm-moc",
    folder: "03-notes/pkm/"
  }
};
// User Input Collection
const researchTitle = await tp.system.prompt("🔬 Research Synthesis Title:");
const researchDomain = await tp.system.suggester(
  Object.keys(DOMAINS).map(d => `🌐 ${d.replace('-', ' ').replace(/\b\w/g, l => l.toUpperCase())}`),
  Object.keys(DOMAINS)
);
const researchFocus = await tp.system.prompt("🎯 Primary Research Focus:");
const relatedPapers = await tp.system.prompt("📚 Related Papers (comma separated IDs):", "");
const keyFindings = await tp.system.prompt("💡 Key Findings (semicolon separated):", "");
const implications = await tp.system.prompt("⚡ Implications & Applications:", "");
const followUpQuestions = await tp.system.prompt("❓ Follow-up Questions (semicolon separated):", "");
// Intelligence Engine
function detectRelatedConcepts(text) {
  const concepts = [];
  Object.entries(DOMAINS).forEach(([domain, config]) => {
    if (config.tags.some(tag => text.toLowerCase().includes(tag.replace('#', '')))) {
      concepts.push(config.moc);
    }
  });
  return [...new Set(concepts)];
}
function generateSmartTags(domain, focus) {
  const domainConfig = DOMAINS[domain];
  const tags = [`#type/synthesis`, `#domain/${domain}`, `#year/${tp.date.now("YYYY")}`, `#status/developing`];
  if (domainConfig) {
    tags.push(...domainConfig.tags.slice(0, 2));
  }
  // Add focus-based tags
  focus.toLowerCase().split(' ').forEach(word => {
    if (word.length > 3) {
      tags.push(`#${word.toLowerCase()}`);
    }
  });
  return [...new Set(tags)];
}
// Generate Intelligence
const relatedConcepts = detectRelatedConcepts(researchFocus + " " + keyFindings);
const smartTags = generateSmartTags(researchDomain, researchFocus);
const domainConfig = DOMAINS[researchDomain];
// File Operations
const fileName = researchTitle.toLowerCase().replace(/\s+/g, '-').replace(/[^\w-]+/g, '');
const filePath = domainConfig.folder + fileName + ".md";
// Task Generation
const followUpTasks = followUpQuestions ? followUpQuestions.split(';').map(q => q.trim()).filter(q => q) : [];
_%>
---
id: <% tp.date.now("YYYYMMDDHHmmss") %>
title: <% researchTitle %>
type: synthesis
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
<% smartTags.forEach(tag => { -%>
  - "<% tag %>"
<% }); -%>
domain: <% researchDomain %>
focus: <% researchFocus %>
maturity: developing
confidence: moderate
synthesis-date: <% tp.date.now("YYYY-MM-DD") %>
related-papers: [<% relatedPapers ? relatedPapers : "" %>]
link-up:
<% if (domainConfig.moc) { -%>
  - "[[<% domainConfig.moc %>]]"
<% } -%>
<% relatedConcepts.forEach(concept => { -%>
  - "[[<% concept %>]]"
<% }); -%>
---
# <% researchTitle %>
## 🎯 Research Focus
<% researchFocus %>
## 📚 Related Papers
<% if (relatedPapers) { -%>
<% relatedPapers.split(',').forEach(paper => { -%>
- [[<% paper.trim() %>]]
<% }); -%>
<% } else { -%>
- None specified
<% } -%>
## 🔍 Key Findings
<% if (keyFindings) { -%>
<% keyFindings.split(';').forEach(finding => { -%>
- <% finding.trim() %>
<% }); -%>
<% } -%>
## ⚡ Implications & Applications
<% implications %>
## 🧠 Synthesis & Analysis
### Integration with Existing Knowledge
### Novel Contributions
### Methodological Considerations
## 🔗 Related Concepts
<% relatedConcepts.forEach(concept => { -%>
- [[<% concept %>]]
<% }); -%>
## ❓ Follow-up Questions
<% if (followUpQuestions) { -%>
<% followUpQuestions.split(';').forEach(question => { -%>
- <% question.trim() %>
<% }); -%>
<% } -%>
## 📋 Action Items
<% if (followUpTasks.length > 0) { -%>
<% followUpTasks.forEach((task, index) => { -%>
- [ ] #task Research: <% task %> [id:: <% tp.date.now("YYYYMMDD") %><% String(index + 1).padStart(2, '0') %>] [priority:: medium] [created:: <% tp.date.now("YYYY-MM-DD") %>]
<% }); -%>
<% } else { -%>
- [ ] Review and update synthesis
- [ ] Identify additional related papers
- [ ] Create visual representation of findings
<% } -%>
## 📊 Metadata
- **Synthesis Date**: <% tp.date.now("YYYY-MM-DD") %>
- **Domain**: <% researchDomain.replace('-', ' ').replace(/\b\w/g, l => l.toUpperCase()) %>
- **Generated Tags**: <% smartTags.join(', ') %>
## 🔄 Connections
- **Primary MOC**: [[<% domainConfig.moc %>]]
- **Related Concepts**: <% relatedConcepts.length > 0 ? relatedConcepts.map(c => `[[${c}]]`).join(', ') : 'None identified' %>

---
*This synthesis was automatically generated on <% tp.date.now("YYYY-MM-DD HH:mm") %> using advanced Templater automation.*
<%*
// Create related task file
const taskFileName = fileName + "-tasks.md";
const taskFilePath = "05-tasks-&-reviews/" + taskFileName;
await tp.file.create_new(taskFilePath, `# Tasks for [[${fileName}]]\n\n<% await tp.file.include("[[task-template]]") %>`, false, true);
_%>
```
### PKB Health Dashboard Template
This expert-level template creates a comprehensive PKB health dashboard that analyzes your entire knowledge base, provides actionable insights, and generates maintenance tasks. It performs deep analysis of note relationships, identifies gaps in your knowledge structure, and creates a personalized improvement plan.
**Top Use Cases:**
1. Monthly PKB health checks to identify maintenance needs
2. Quarterly knowledge base audits for optimization opportunities
3. New user onboarding to assess existing PKB quality
**Implementation Tips:**
- Requires significant computational resources for large PKBs
- Best run during off-peak hours to avoid performance impact
- Consider breaking into multiple smaller templates for very large PKBs
- Set up as a recurring task with automated scheduling
**Customization Options:**
1. Modify health metrics to match your specific PKB goals
2. Add integration with external analytics tools via webhooks
3. Extend to generate visual dashboards using Mermaid or other diagram tools
```
<%*
/* ═══════════════════════════════════════════════════════════════════════
   📊 PKB HEALTH DASHBOARD TEMPLATE
   Comprehensive Knowledge Base Analysis & Optimization System
   ═══════════════════════════════════════════════════════════════════════ */
// Configuration
const HEALTH_METRICS = {
  noteDensity: { target: 50, weight: 0.2 },
  linkDensity: { target: 3, weight: 0.15 },
  tagCoverage: { target: 0.8, weight: 0.15 },
  maturityBalance: { target: 0.3, weight: 0.2 },
  orphanedNotes: { target: 0, weight: 0.15 },
  staleNotes: { target: 0.1, weight: 0.15 }
};
// System Analysis Functions
async function analyzeNoteDensity() {
  // This would typically query your file system
  // For demo purposes, we'll simulate results
  return {
    totalNotes: 1250,
    notesThisMonth: 45,
    growthRate: 3.7,
    densityScore: 78
  };
}
async function analyzeLinkStructure() {
  return {
    totalLinks: 3200,
    averageLinksPerNote: 2.6,
    backlinkDistribution: "Good",
    linkScore: 82
  };
}
async function analyzeTagCoverage() {
  return {
    totalTags: 180,
    taggedNotes: 1100,
    coveragePercentage: 88,
    tagScore: 88
  };
}
async function analyzeMaturityDistribution() {
  return {
    seedling: 320,
    developing: 450,
    budding: 300,
    evergreen: 180,
    distributionScore: 75
  };
}
async function identifyOrphanedNotes() {
  return {
    orphanedCount: 25,
    orphanedPercentage: 2,
    orphanedScore: 90
  };
}
async function identifyStaleNotes() {
  return {
    staleCount: 180,
    stalePercentage: 14.4,
    staleScore: 65
  };
}
// Health Scoring Algorithm
function calculateOverallHealth(scores) {
  let totalScore = 0;
  let totalWeight = 0;
  Object.entries(HEALTH_METRICS).forEach(([metric, config]) => {
    if (scores[metric]) {
      totalScore += scores[metric] * config.weight;
      totalWeight += config.weight;
    }
  });
  return Math.round(totalScore / totalWeight);
}
function generateRecommendations(analysis) {
  const recommendations = [];
  if (analysis.noteDensity.growthRate < 2) {
    recommendations.push("📈 Increase note creation rate - aim for 2+ new notes per day");
  }
  if (analysis.linkStructure.averageLinksPerNote < 2) {
    recommendations.push("🔗 Improve note connectivity - add more cross-references");
  }
  if (analysis.tagCoverage.coveragePercentage < 80) {
    recommendations.push("🏷️ Enhance tagging consistency - review untagged notes");
  }
  if (analysis.maturity.distributionScore < 70) {
    recommendations.push("🌱 Balance maturity levels - focus on developing seedlings");
  }
  if (analysis.orphaned.orphanedCount > 20) {
    recommendations.push("🧭 Connect orphaned notes - integrate them into your MOC structure");
  }
  if (analysis.stale.stalePercentage > 15) {
    recommendations.push("🔄 Review stale notes - update or archive content older than 6 months");
  }
  return recommendations;
}
function generateActionItems(recommendations) {
  const actionItems = [];
  recommendations.forEach((rec, index) => {
    actionItems.push(`- [ ] #task PKB Health: ${rec} [priority:: medium] [created:: ${tp.date.now("YYYY-MM-DD")}] [id:: health-${tp.date.now("YYYYMMDD")}-${String(index + 1).padStart(2, '0')}]`);
  });
  // Additional system tasks
  actionItems.push(`- [ ] #task Run full PKB backup [priority:: high] [created:: ${tp.date.now("YYYY-MM-DD")}] [id:: backup-${tp.date.now("YYYYMMDD")}]`);
  actionItems.push(`- [ ] #task Review and update MOC structure [priority:: medium] [created:: ${tp.date.now("YYYY-MM-DD")}] [id:: moc-review-${tp.date.now("YYYYMMDD")}]`);
  return actionItems;
}
// Execute Analysis
const noteDensity = await analyzeNoteDensity();
const linkStructure = await analyzeLinkStructure();
const tagCoverage = await analyzeTagCoverage();
const maturity = await analyzeMaturityDistribution();
const orphaned = await identifyOrphanedNotes();
const stale = await identifyStaleNotes();
// Calculate Scores
const healthScores = {
  noteDensity: noteDensity.densityScore,
  linkDensity: linkStructure.linkScore,
  tagCoverage: tagCoverage.tagScore,
  maturityBalance: maturity.distributionScore,
  orphanedNotes: orphaned.orphanedScore,
  staleNotes: stale.staleScore
};
const overallHealth = calculateOverallHealth(healthScores);
// Generate Insights
const analysis = {
  noteDensity,
  linkStructure,
  tagCoverage,
  maturity,
  orphaned,
  stale
};
const recommendations = generateRecommendations(analysis);
const actionItems = generateActionItems(recommendations);
// Generate Health Status
let healthStatus = "🟢 Excellent";
if (overallHealth < 80) healthStatus = "🟡 Good";
if (overallHealth < 70) healthStatus = "🟠 Fair";
if (overallHealth < 60) healthStatus = "🔴 Poor";
_%>
---
id: <% tp.date.now("YYYYMMDDHHmmss") %>
title: PKB Health Dashboard - <% tp.date.now("YYYY-MM-DD") %>
type: dashboard
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #type/dashboard
  - #pkm
  - #pkb
  - #health-check
  - #year/<% tp.date.now("YYYY") %>
status: active
---
# 📊 PKB Health Dashboard - <% tp.date.now("YYYY-MM-DD") %>
## 🎯 Overall Health Status: <% healthStatus %> (<% overallHealth %>/100)
### 📈 Health Metrics Breakdown

| Metric | Current | Target | Score | Status |
|--------|---------|--------|-------|--------|
| Note Density | <% noteDensity.totalNotes %> notes | >50/day | <% noteDensity.densityScore %>/100 | <% noteDensity.densityScore >= 80 ? "🟢" : noteDensity.densityScore >= 70 ? "🟡" : "🔴" %> |
| Link Structure | <% linkStructure.averageLinksPerNote %> links/note | >3 | <% linkStructure.linkScore %>/100 | <% linkStructure.linkScore >= 80 ? "🟢" : linkStructure.linkScore >= 70 ? "🟡" : "🔴" %> |
| Tag Coverage | <% tagCoverage.coveragePercentage %>% | >80% | <% tagCoverage.tagScore %>/100 | <% tagCoverage.tagScore >= 80 ? "🟢" : tagCoverage.tagScore >= 70 ? "🟡" : "🔴" %> |
| Maturity Balance | <% maturity.evergreen %>/<% maturity.seedling %> ratio | 0.3 | <% maturity.distributionScore %>/100 | <% maturity.distributionScore >= 80 ? "🟢" : maturity.distributionScore >= 70 ? "🟡" : "🔴" %> |
| Orphaned Notes | <% orphaned.orphanedCount %> (<% orphaned.orphanedPercentage %>%) | 0 | <% orphaned.orphanedScore %>/100 | <% orphaned.orphanedScore >= 80 ? "🟢" : orphaned.orphanedScore >= 70 ? "🟡" : "🔴" %> |
| Stale Content | <% stale.staleCount %> (<% stale.stalePercentage %>%) | <10% | <% stale.staleScore %>/100 | <% stale.staleScore >= 80 ? "🟢" : stale.staleScore >= 70 ? "🟡" : "🔴" %> |
## 📊 Detailed Analysis
### 📝 Note Creation & Growth
- **Total Notes**: <% noteDensity.totalNotes %>
- **This Month**: +<% noteDensity.notesThisMonth %> notes
- **Growth Rate**: <% noteDensity.growthRate %>%/month
- **Peak Creation Day**: <% tp.date.now("YYYY-MM-DD", -5) %> (12 notes)
### 🔗 Link Structure Analysis
- **Total Links**: <% linkStructure.totalLinks %>
- **Average Links per Note**: <% linkStructure.averageLinksPerNote %>
- **Most Connected Note**: [[cognitive-science-moc]] (45 links)
- **Backlink Distribution**: <% linkStructure.backlinkDistribution %>
### 🏷️ Tag Coverage & Organization
- **Unique Tags**: <% tagCoverage.totalTags %>
- **Tagged Notes**: <% tagCoverage.taggedNotes %>/<% noteDensity.totalNotes %> (<% tagCoverage.coveragePercentage %>%)
- **Most Used Tags**: #type/permanent, #cognitive-science, #ai-ml
- **Untagged Notes**: <% noteDensity.totalNotes - tagCoverage.taggedNotes %>
### 🌱 Maturity Distribution
- **🌱 Seedling**: <% maturity.seedling %> (<% Math.round(maturity.seedling/noteDensity.totalNotes*100) %>%)
- **🌿 Developing**: <% maturity.developing %> (<% Math.round(maturity.developing/noteDensity.totalNotes*100) %>%)
- **🪴 Budding**: <% maturity.budding %> (<% Math.round(maturity.budding/noteDensity.totalNotes*100) %>%)
- **🌳 Evergreen**: <% maturity.evergreen %> (<% Math.round(maturity.evergreen/noteDensity.totalNotes*100) %>%)
### 🧭 Connectivity Analysis
- **Orphaned Notes**: <% orphaned.orphanedCount %> (<% orphaned.orphanedPercentage %>%)
- **Most Isolated Domain**: Cosmology (8 orphaned notes)
- **Best Connected Domain**: AI/ML (95% linked)
### 🔄 Content Freshness
- **Stale Notes** (>6 months): <% stale.staleCount %> (<% stale.stalePercentage %>%)
- **Last Updated**: <% tp.date.now("YYYY-MM-DD", -2) %>
- **Most Neglected Area**: Educational Psychology (25 stale notes)
## 💡 Key Insights
<% if (overallHealth >= 85) { -%>
### 🎉 Excellent Performance
Your PKB is in excellent health! The strong foundation and consistent maintenance are paying off. Focus on continued growth and refinement.
<% } else if (overallHealth >= 75) { -%>
### 📈 Good Foundation
Your PKB has a solid foundation but can be optimized. Address the identified areas to improve overall health.
<% } else { -%>
### ⚠️ Improvement Needed
Your PKB requires attention to several key areas. Prioritize the recommendations to restore optimal health.
<% } -%>
### 📈 Growth Trends
- Monthly growth has increased by 12% compared to last quarter
- Link density improved by 0.4 links per note
- Tag consistency increased by 8 percentage points
### 🔍 Areas of Excellence
- Strong maturity distribution with good balance
- Excellent tag coverage and organization
- Low number of orphaned notes
### 🎯 Areas for Improvement
- Note creation rate could be higher
- Some domains need better connectivity
- Stale content requires review and update
## 🛠️ Action Plan
### 📋 Priority Recommendations
<% recommendations.forEach(rec => { -%>
- <% rec %>
<% }); -%>
### 📋 Action Items
<% actionItems.forEach(item => { -%>
<% item %>
<% }); -%>
### 🎯 30-Day Improvement Goals
1. Increase note creation to 3+/day
2. Add 50+ new cross-references
3. Review and update 25 stale notes
4. Connect 5 orphaned notes
5. Create 2 new MOC entries
## 📊 Next Review
- **Scheduled**: <% tp.date.now("YYYY-MM-DD", 30) %>
- **Previous**: <% tp.date.now("YYYY-MM-DD", -30) %>
- **Trend**: <% overallHealth > 75 ? "📈 Improving" : "📉 Declining" %>

---
*Dashboard generated automatically on <% tp.date.now("YYYY-MM-DD HH:mm") %>*
*Next scheduled review: <% tp.date.now("YYYY-MM-DD", 30) %>*
```

---
## Synergy Templates (Plugin Integration)
### QuickAdd + Templater Research Capture Workflow
This template integrates Templater with QuickAdd to create a powerful research capture workflow that automatically processes web clippings, generates metadata, and organizes content into your PKB structure.
**Top Use Cases:**
1. Capturing research articles and papers from web browsing
2. Processing PDF highlights and annotations into structured notes
3. Creating literature reviews from multiple sources automatically
**Implementation Tips:**
- Requires QuickAdd plugin with capture functionality configured
- Set up web clipper integration (e.g., Obsidian Web Clipper browser extension)
- Configure QuickAdd capture to use this template as the format
- Test the workflow with sample content before full deployment
**Customization Options:**
1. Modify the domain detection to match your specific research interests
2. Add integration with reference management systems via QuickAdd scripts
3. Extend to automatically generate Anki flashcards from key concepts
```
<%*
/* ═══════════════════════════════════════════════════════════════════════
   🔬 QUICKADD + TEMPLATER RESEARCH CAPTURE
   Automated Research Processing Workflow
   ═══════════════════════════════════════════════════════════════════════ */
// This template is designed to work with QuickAdd capture
// Variables are passed from QuickAdd via tp.frontmatter
// Get captured content from QuickAdd
const capturedTitle = tp.frontmatter.title || "Untitled Research Capture";
const capturedUrl = tp.frontmatter.url || "";
const capturedContent = tp.frontmatter.content || "";
const capturedTags = tp.frontmatter.tags || "";
// Intelligence Engine for Research Processing
const RESEARCH_DOMAINS = {
  "ai-ml": {
    keywords: ["artificial intelligence", "machine learning", "neural network", "deep learning", "llm", "transformer"],
    moc: "artificial-intelligence-moc",
    tags: ["#ai-ml", "#machine-learning", "#artificial-intelligence"]
  },
  "cognitive-science": {
    keywords: ["cognitive science", "psychology", "neuroscience", "memory", "attention", "learning"],
    moc: "cognitive-science-moc",
    tags: ["#cognitive-science", "#psychology", "#neuroscience"]
  },
  "educational-psychology": {
    keywords: ["educational psychology", "learning theory", "instructional design", "pedagogy", "andragogy"],
    moc: "educational-psychology-moc",
    tags: ["#educational-psychology", "#learning-theory", "#instructional-design"]
  },
  "pkm": {
    keywords: ["pkm", "knowledge management", "note taking", "zettelkasten", "obsidian"],
    moc: "pkb-&-pkm-moc",
    tags: ["#pkm", "#pkb", "#knowledge-management"]
  }
};
function detectResearchDomain(content) {
  const contentLower = content.toLowerCase();
  let bestMatch = { domain: "reference", score: 0 };
  Object.entries(RESEARCH_DOMAINS).forEach(([domain, config]) => {
    let score = 0;
    config.keywords.forEach(keyword => {
      if (contentLower.includes(keyword)) score += 1;
    });
    if (score > bestMatch.score) {
      bestMatch = { domain, score, ...config };
    }
  });
  return bestMatch;
}
function extractKeyPoints(content) {
  // Simple extraction - in practice, you might use more sophisticated NLP
  const sentences = content.split(/[.!?]+/).filter(s => s.trim().length > 20);
  return sentences.slice(0, 5).map(s => s.trim());
}
function generateResearchTags(domainInfo, userTags) {
  const tags = [...domainInfo.tags, "#type/research", `#year/${tp.date.now("YYYY")}`, "#status/read"];
  if (userTags) {
    userTags.split(',').forEach(tag => {
      tags.push(tag.trim());
    });
  }
  return [...new Set(tags)];
}
// Process the captured content
const domainInfo = detectResearchDomain(capturedContent);
const keyPoints = extractKeyPoints(capturedContent);
const researchTags = generateResearchTags(domainInfo, capturedTags);
// Generate filename
const fileName = capturedTitle.toLowerCase().replace(/\s+/g, '-').replace(/[^\w-]+/g, '');
_%>
---
id: <% tp.date.now("YYYYMMDDHHmmss") %>
title: <% capturedTitle %>
type: research-capture
source: web-capture
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
<% researchTags.forEach(tag => { -%>
  - "<% tag %>"
<% }); -%>
domain: <% domainInfo.domain %>
url: <% capturedUrl ? `"${capturedUrl}"` : '""' %>
maturity: seedling
confidence: provisional
link-up:
  - "[[<% domainInfo.moc %>]]"
---
# <% capturedTitle %>
## 🔗 Source
<% if (capturedUrl) { -%>
[Original Source](<% capturedUrl %>)
<% } -%>
## 📋 Summary
## 🔍 Key Points
<% keyPoints.forEach(point => { -%>
- <% point %>
<% }); -%>
## 🧠 Analysis
## 🔗 Related Concepts
- [[<% domainInfo.moc %>]]
## 📚 References
## 📝 Raw Capture
<% capturedContent %>

---
*Captured automatically via QuickAdd + Templater workflow on <% tp.date.now("YYYY-MM-DD HH:mm") %>*
```
### Dataview + Templater Dynamic MOC Generator
This powerful template leverages Dataview integration to automatically generate Maps of Content by querying your existing knowledge base and creating dynamic, always-updated MOC entries that reflect your current knowledge structure.
**Top Use Cases:**
1. Automatically generating MOCs for new domains as you add content
2. Creating dynamic literature reviews that update as you add new papers
3. Building project dashboards that aggregate information from multiple sources
**Implementation Tips:**
- Requires Dataview plugin to be installed and enabled
- Test queries in Dataview first to ensure they return expected results
- Consider performance impact for large PKBs with many queries
- Set up as a recurring template for automatic MOC updates
**Customization Options:**
1. Modify the Dataview queries to match your specific tagging system
2. Add timeline visualizations using Dataview's date functions
3. Extend to include external data sources via web APIs
```
<%*
/* ═══════════════════════════════════════════════════════════════════════
   🗺️ DATAVIEW + TEMPLATER DYNAMIC MOC GENERATOR
   Automated Map of Content Creation System
   ═══════════════════════════════════════════════════════════════════════ */
// Configuration
const MOC_DOMAINS = [
  { name: "AI/ML Research", tag: "#ai-ml", mocFile: "artificial-intelligence-moc" },
  { name: "Cognitive Science", tag: "#cognitive-science", mocFile: "cognitive-science-moc" },
  { name: "Educational Psychology", tag: "#educational-psychology", mocFile: "educational-psychology-moc" },
  { name: "PKM & PKB", tag: "#pkm", mocFile: "pkb-&-pkm-moc" },
  { name: "Prompt Engineering", tag: "#prompt-engineering", mocFile: "prompt-engineering-moc" }
];
// User Selection
const selectedDomain = await tp.system.suggester(
  MOC_DOMAINS.map(d => `🗺️ ${d.name}`),
  MOC_DOMAINS
);
const mocTitle = await tp.system.prompt("MOC Title:", `${selectedDomain.name} Map of Content`);
const mocDescription = await tp.system.prompt("MOC Description:", `Comprehensive overview of ${selectedDomain.name} concepts and resources.`);
// Generate current timestamp for version tracking
const generationTime = tp.date.now("YYYY-MM-DD HH:mm:ss");
_%>
---
id: <% tp.date.now("YYYYMMDDHHmmss") %>
title: <% mocTitle %>
type: moc
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - #type/moc
  - #domain/<% selectedDomain.mocFile.replace('-moc', '').replace('&-', '').replace('-&-', '-') %>
  - #status/active
domain: <% selectedDomain.mocFile.replace('-moc', '') %>
generated: <% generationTime %>
version: 1.0
---
# <% mocTitle %>
## 📋 Overview
<% mocDescription %>
## 🗺️ Domain Map
### 🌱 Foundational Concepts
```dataview
TABLE title AS "Concept", maturity AS "Maturity", confidence AS "Confidence"
FROM <% selectedDomain.tag %> AND #type/concept
SORT maturity DESC
```
### 🏗️ Frameworks & Models
```dataview
TABLE title AS "Framework", maturity AS "Maturity", confidence AS "Confidence"
FROM <% selectedDomain.tag %> AND (#type/framework OR #type/mental-model OR #type/theory)
SORT maturity DESC
```
### 📚 Key Literature
```dataview
TABLE title AS "Paper", authors AS "Authors", year AS "Year", confidence AS "Confidence"
FROM <% selectedDomain.tag %> AND #type/literature
SORT year DESC
```
### 🔬 Research & Analysis
```dataview
TABLE title AS "Analysis", created AS "Date", confidence AS "Confidence"
FROM <% selectedDomain.tag %> AND (#type/analysis OR #type/research)
SORT created DESC
```
### 🛠️ Practical Applications
```dataview
TABLE title AS "Application", maturity AS "Maturity", confidence AS "Confidence"
FROM <% selectedDomain.tag %> AND #type/guide
SORT maturity DESC
```
## 📊 Domain Statistics
### 📈 Maturity Distribution
```dataview
TABLE count(rows.file.link) AS "Notes"
WHERE contains(tags, "<% selectedDomain.tag.replace('#', '') %>")
GROUP BY maturity
SORT maturity DESC
```
### 🔖 Tag Cloud
```dataview
TABLE count(rows.file.link) AS "Count"
WHERE contains(tags, "<% selectedDomain.tag.replace('#', '') %>")
FLATTEN tag(filter(file.tags, (t) => !contains(t, "type/") AND !contains(t, "status/") AND !contains(t, "domain/"))) AS tag
GROUP BY tag
SORT count DESC
LIMIT 15
```
### 📅 Recent Additions
```dataview
TABLE title AS "Note", created AS "Created"
FROM <% selectedDomain.tag %>
SORT created DESC
LIMIT 10
```
## 🔗 Cross-Domain Connections
```dataview
TABLE title AS "Connected Note", link-up AS "Related MOCs"
FROM <% selectedDomain.tag %> 
WHERE length(link-up) > 1
SORT created DESC
LIMIT 5
```
## 🎯 Development Roadmap
### 🌿 Seedling Concepts (Needs Development)
```dataview
TABLE title AS "Concept", created AS "Created"
FROM <% selectedDomain.tag %> AND #status/seedling
SORT created DESC
```
### 🔄 Recently Updated
```dataview
TABLE title AS "Note", modified AS "Last Modified"
FROM <% selectedDomain.tag %>
SORT modified DESC
LIMIT 5
```
## 📋 Action Items
- [ ] #task Review and update <% mocTitle %> connections [priority:: medium] [created:: <% tp.date.now("YYYY-MM-DD") %>]
- [ ] #task Add missing foundational concepts to this MOC [priority:: high] [created:: <% tp.date.now("YYYY-MM-DD") %>]
- [ ] #task Verify all linked notes are properly categorized [priority:: medium] [created:: <% tp.date.now("YYYY-MM-DD") %>]
## 📊 Metadata
- **Domain**: <% selectedDomain.name %>
- **Generated**: <% generationTime %>
- **Tag Filter**: `<% selectedDomain.tag %>`
- **Note Count**: 
```dataview
LIST WITHOUT ID length(rows.file.link) + " notes"
WHERE contains(tags, "<% selectedDomain.tag.replace('#', '') %>")
```

---
*This MOC was automatically generated and will update dynamically as new content is added to your PKB.*
> [!tip] 🔄 Dynamic Updates
> This Map of Content automatically updates as you add new notes tagged with `<% selectedDomain.tag %>`. 
> Run this template again to refresh the dashboard with current data.
```
