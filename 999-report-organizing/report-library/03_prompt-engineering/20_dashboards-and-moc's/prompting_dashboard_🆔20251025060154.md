🚀Prompting_Dashboard_🆔20251025060154

> [!summary] Overview
> This dashboard provides a complete overview of all custom prompts and Gemini Gem Instruction Sets stored in the vault. All tables are automatically updated.

---

## ♊ Gemini Gem Instruction Sets

### Active Gems
```dataview
TABLE
  id as "ID",
  summary as "Summary",
  version as "Version",
  file.mtime as "Last Modified"
FROM #prompt-engineering AND !"Utilities/Templates"
WHERE type = "Gem" AND status = "Active"
SORT file.mtime DESC
```

### ♊ Draft Gems

```dataview
TABLE
  id as "ID",
  summary as "Summary",
  version as "Version",
  file.cday as "Created"
FROM #prompt-engineering AND !"Utilities/Templates"
WHERE type = "Gem" AND status = "Draft"
SORT file.cday DESC
```


---

## 📝 General Prompts

### Active Prompts

```dataview
TABLE
  id as "ID",
  summary as "Summary",
  file.mtime as "Last Modified"
FROM #prompt-engineering AND !"Utilities/Templates"
WHERE type = "Prompt" AND status = "Active"
SORT file.mtime DESC
```

### All Prompts

Code snippet

```dataview
LIST
  link(file.link, summary)
FROM #prompt-engineering AND !"Utilities/Templates"
WHERE type = "Prompt"
GROUP BY status
```

---

> [!how-this-dashboard-works]
> 
> - It looks for any note with the tag `#prompt-engineering` but excludes your template folder.
> - It uses the `type` field from your YAML to separate Gems from general Prompts.
> - It uses the `status` field to create different views, like "Active" vs. "Drafts," so you can easily see what you're working on.
> - The tables are sorted to show the most recently modified or created items first.



> [!your-new-workflow]
> Your day-to-day process for creating and managing prompts will now be incredibly simple:
> 
> 1.  **Create:** Hit `Cmd/Ctrl + P`, type "New Prompt or Gem", and hit Enter.
> 2.  **Define:**
>     - QuickAdd asks for the type (📝 or ♊).
>     - QuickAdd asks for the name (e.g., "Analyze-Scientific-Paper").
>     - The new note is created with the perfect filename (e.g., `♊_Prompt_Analyze-Scientific-Paper_20251012063736.md`) and all metadata pre-filled.
> 3.  **Flesh Out:** Fill in the `summary`, `version` (if it's a Gem), and paste the actual prompt into the code block.
> 4.  **Track:** Open your Dashboard. Your new creation will be there instantly, listed under the correct "Draft" section.
> 5.  **Activate:** When you're happy with it, just change the `status` field in the note from "Draft" to "Active", and it will automatically move to the "Active" table on your dashboard.
>    
>    This system gives you the structure and automation you need to manage your growing collection of powerful prompts effectively.
>    
