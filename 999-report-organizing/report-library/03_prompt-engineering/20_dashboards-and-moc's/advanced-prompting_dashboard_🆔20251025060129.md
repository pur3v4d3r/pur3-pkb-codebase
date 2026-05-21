---
aliases:
  - 🚀 Prompt-Engineering-Advanced_Dashboard
tags: []
title: 🚀 Prompt-Engineering-Dashboard_Advanced
date created: 2025-10-12T07:26:48.000-04:00
date modified: 2025-10-12T08:52:39.737-04:00
---

# 🚀 Advanced-Prompting_Dashboard_🆔20251025060129

## 📊 Status Overview

```dataviewjs
const pages = dv.pages('#prompt-engineering AND -"Utilities/Templates"');
const groups = pages.groupBy(p => p.status);

// Create a simple bar chart visualization
let chartData = {
    type: 'bar',
    data: {
        labels: groups.map(g => g.key).array(),
        datasets: [{
            label: 'Prompt Count',
            data: groups.map(g => g.rows.length).array(),
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)', // Active
                'rgba(255, 206, 86, 0.2)', // Draft
                'rgba(255, 99, 132, 0.2)'  // Archived
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(255, 99, 132, 1)'
            ],
            borderWidth: 1
        }]
    }
};

window.renderChart(chartData, this.container);
```

# Current Active Prompts and Gems
```dataview
TABLE
  summary as "Objective",
  model as "LLM",
  file.mtime as "Last Modified"
FROM "04⚜️References/03_AI/01_Prompting"
WHERE status = "⚡Active"
SORT file.mtime DESC
```

## 🛠️ Drafts & In-Progress

*These are prompts currently under development.*
```dataview
TABLE status as "⚡Active"
FROM "folder04⚜️References/03_AI/01_Prompting"
WHERE status = "Active"
SORT file.mtime DESC
```

# Archived Prompt and Gems
```dataview
TABLE
  summary as "Objective",
  model as "LLM",
  file.mtime as "Last Modified"
FROM "04⚜️References/03_AI/01_Prompting"
WHERE status = "🗄️Archived"
SORT file.mtime DESC
```







































 

> [!your-new-workflow]
>  **Establish a Versioning Workflow**
>
> 
> *Your prompts will evolve. A formal workflow ensures you don't lose good versions while experimenting.*
>
>**The Workflows:**
> 
> 
>The Workflow (Stage-01):
> 1. Use the command palette (`Ctrl/Cmd+P`) and select **"File: Make a copy of the current file"**. 
> 2. Rename the new file to reflect the version change: `♊_Gem_Analyze-Paper_v1.1_...md`.
> 3. Rename the new file to reflect the version change: `♊_Gem_Analyze-Paper_v1.1_...md`.1. In the new `v1.1` file:
> 4. Change the `version:` YAML field to `1.1`.
> 5. In the `related:` field, link back to the original: `related: [[♊_Gem_Analyze-Paper_v1.0_...md]]`.
> 6. Start a new entry in the `🧪 Iteration & Test Log`.
> 7. In the original `v1.0` file:
> 8. Change its `status:` to "Archived".
> 
> 
> The Workflow (Stage-02):
> 1. You have `♊_Gem_Analyze-Paper_v1.0_...md` and its status is "Active". You think you can improve it.
> 2. Use the command palette (`Ctrl/Cmd+P`) and select **"File: Make a copy of the current file"**.
> 3. Rename the new file to reflect the version change: `♊_Gem_Analyze-Paper_v1.1_...md`.
> 4. Rename the new file to reflect the version change: `♊_Gem_Analyze-Paper_v1.1_...md`.
> 5. In the new `v1.1` file:
> 6. Change the `version:` YAML field to `1.1`.
> 7. In the `related:` field, link back to the original: `related: [[♊_Gem_Analyze-Paper_v1.0_...md]]`.
> 8. Start a new entry in the `🧪 Iteration & Test Log`.
> 9. In the original `v1.0` file:
> 10. Change its `status:` to "Archived".
>  
  
> [!changes-from-prompting-dashboard]
>
> - **Why this is an upgrade:**
> 	- **DataviewJS Chart:** The chart at the top (which requires the **Charts** plugin) gives you a quick visual summary of your collection's status. It's a great motivating tool.
> 	- **Grouped by Purpose:** This is a game-changer. As your collection grows, you won't think of prompts by their name, but by what they _do_. This query organizes them into collapsible sections like "Summarization," "Analysis," etc., making it easy to find the right tool for the job.




1.  **Create:** Hit `Cmd/Ctrl + P`, type "New Prompt or Gem", and hit Enter.
2.  **Define:**
    * QuickAdd asks for the type (📝 or ♊).
    * QuickAdd asks for the name (e.g., "Analyze-Scientific-Paper").
    * The new note is created with the perfect filename (e.g., `♊_Prompt_Analyze-Scientific-Paper_20251012063736.md`) and all metadata pre-filled.
3.  **Flesh Out:** Fill in the `summary`, `version` (if it's a Gem), and paste the actual prompt into the code block.
4.  **Track:** Open your Dashboard. Your new creation will be there instantly, listed under the correct "Draft" section.
5.  **Activate:** When you're happy with it, just change the `status` field in the note from "Draft" to "Active", and it will automatically move to the "Active" table on your dashboard.

This system gives you the structure and automation you need to manage your growing collection of powerful prompts effectively.











Your dashboard will automatically move the old version out of the "Active" list, keeping your workspace focused on the latest and greatest versions while maintaining a complete history.

