---
type: "prompt"
id: "20251219052221"
status: "active"
version: "1.0.0"
rating: "0.0"
source: "claude-sonnet-4.5"
title: "Bulk QuickAdd Macros"
description: "To generate multipl QuickAdd Macro Idea I can use in my PKB."
key-takeaway: "Part of a Bulk Automation Series."
last-used: "[[2025-12-19]]"
tags:
  - "year/2025"
  - "prompt-engineering"
  - "llm-capability/generation"
  - "prompt-workflow/deployment"
aliases:
  - "Prompt"
  - "Prompt-Engineering"
link-up: "[[moc-agentic-instruction-sets-2025117044009]]"
link-related:
  - "[[2025-12-19|Daily Note]]"
  - "[[2025-W51|Weekly Review]]"
---



[Initial Creation: [[2025-12-19|Friday, December 19th, 2025]]]

---
>[! ] Key Features of This QuickAdd Macro Prompt
> ## 1. **Workflow-Centric Structure**
> Unlike code-focused prompts, this is about **workflow engineering**:
> - Step sequences
> - Variable flows
> - Conditional branching
> - Multi-file operations
> - Template orchestration
> ## 2. **Progressive Complexity Architecture**
> | Tier | Steps | Features | Count |
> |------|-------|----------|-------|
> | **Basic** | 2-4 | Linear workflows, simple captures | 3-4 macros |
> | **Intermediate** | 4-8 | Conditionals, scripts, multi-file | 3-4 macros |
> | **Advanced** | 8+ | Complex branching, orchestration | 2-3 macros |
> | **Compound** | Multiple macros | Cross-macro systems | 2-3 systems |
> | **TOTAL** | - | - | **10-14 macros** |
> ## 3. **Comprehensive Documentation Hierarchy**
> **Basic Macros (6 components):**
> 1. Macro Name
> 2. Purpose
> 3. Configuration Steps
> 4. Variables Used
> 5. Templates
> 6. Expected Outcome
> **Intermediate Macros (8 components):**
> 1-6 from Basic, plus:
> 7. Scripts
> 8. Conditional Logic
> 9. Setup Requirements
> **Advanced Macros (10 components):**
> 10. Macro Name & Purpose
> 11. Architecture Overview
> 12. Complete Step-by-Step Configuration
> 13. Variables & Data Flow
> 14. All Templates
> 15. All Scripts
> 16. Top Use Cases
> 17. Setup Requirements
> 18. Customization Options
> 19. Troubleshooting Guide
> **Compound Macros (8 components):**
> 20. System Name & Purpose
> 21. System Architecture
> 22. Individual Macro Configurations
> 23. Shared Resources
> 24. Integration Patterns
> 25. Top Use Cases
> 26. Complete Setup Guide
> 27. Customization & Extension
> ## 4. **Extensive Generation Guidelines**
> ### QuickAdd-Specific Knowledge
> - **Step Types Reference** (Capture, Template, Macro, Command, Script, Choice, AI)
> - **Variable System** (naming, sources, scope, transformation)
> - **Configuration Best Practices** (naming, organization, testing)
> - **Template Integration** (storage, naming, documentation)
> - **Script Integration** (interfaces, async handling, error reporting)
> >[! ] Workflow Design Patterns
> > - Linear Capture
> > - Conditional Routing
> > - Multi-File Creation
> > - Process & Organize
> > - Review & Update
> > - Hierarchical Workflow
> > ### Testing & Debugging
> > - 8-point testing checklist
> > - Debugging tips and tools
> > - Validation methodology
> > ### Performance Optimization
> > - Optimization tips
> > - Scalability considerations
> > - User experience guidelines
> > ## 5. **UI Configuration Focus**
> > Unlike script/query prompts that generate code files, this generates:
> > - **Step-by-step UI configuration instructions**
> > - "Go to QuickAdd settings → Add New Macro → Click gear icon → Add Step → Select Capture…"
> > - Exact settings for each step
> > - Variable assignment instructions
> > - Template path specifications
> > This matches how QuickAdd actually works (UI-configured workflows, not code files).
> > ---
> 
> >[! ] 📊 Comparison Across All Prompts
> > 
> > | Aspect | Dataview | Templater | Scripts | **Macros** |
> > |--------|----------|-----------|---------|------------|
> > | **Output Type** | Queries | Templates | JS Files | **UI Configurations** |
> > | **File Format** | DQL/JS | Markdown+Templater | .js files | **Settings-based** |
> > | **Execution** | Inline rendering | Template insertion | External call | **Workflow steps** |
> > | **Complexity Tiers** | 4 | 4 | 4 | **4** |
> > | **Total Outputs** | 11-15 | 10-15 | 12-19 | **10-14 macros** |
> > | **Primary Value** | Data queries | Content generation | Automation logic | **Workflow orchestration** |
> > | **Key Feature** | Dynamic data | Dynamic templates | Pure code | **Multi-step processes** |
> > | **Learning Curve** | Medium | Medium | High | **Medium-High** |
> > | **Integration** | Charts, JS Engine | QuickAdd, plugins | Templater/QuickAdd | **Everything** |
> > | **Variable Handling** | N/A | `<% %>` syntax | `params.variables` | **Native variable system** |
> > | **Conditional Logic** | Limited (filters) | Templater logic | Full JavaScript | **Choice steps + scripts** |
> > | **Multi-File** | No | Limited | Yes (via code) | **Yes (via steps)** |
> > ---
> # 🚀 Usage Instructions
> **To use this macro generation prompt:**
> 1. **Copy the entire prompt** from the markdown block above
> 2. **Replace `[INSERT THEME HERE]`** with your desired workflow theme:
>    - Examples: "Project Initialization", "Inbox Processing", "Weekly Review", "Literature Note Workflow", "Meeting Notes", "Research Paper Processing"
> 3. **Paste into Claude** (or your LLM of choice)
> 4. **Receive 10-14 macro configurations** across all complexity tiers with complete documentation
> 5. **Configure in QuickAdd:**
>    - Open Obsidian Settings → QuickAdd
>    - Click "Manage Macros"
>    - Follow step-by-step instructions from generated output
>    - Configure each step exactly as documented
>    - Assign variables as specified
>    - Link templates and scripts
> 6. **Create supporting resources:**
>    - Save templates to `99-system/templates/`
>    - Save scripts to `99-system/scripts/quickadd/`
>    - Test templates independently first
>    - Test scripts before integration
> 7. **Test macros incrementally:**
>    - Test each step individually
>    - Verify variable flow
>    - Check file creation
>    - Validate conditional branches
> 8. **Iterate with new themes** for unlimited workflow ideas
> 
> ----
> 
> ## 💡Pro Tips for Macro Configuration
> 1. **Start Simple, Build Up**
>    - Configure basic 2-step macros first
>    - Test thoroughly before adding complexity
>    - Add one step at a time
> 2. **Document as You Build**
>    - Keep notes on what each step does
>    - Document variable purposes
>    - Record why you made certain choices
> 3. **Use Consistent Naming**
>    - Variables: `camelCase` (e.g., `projectName`)
>    - Macros: "Verb Noun" format (e.g., "Create Project Note")
>    - Templates: Match their purpose (e.g., `project-init-template.md`)
> 4. **Test with Edge Cases**
>    - Empty inputs
>    - Special characters
>    - Very long strings
>    - Unusual folder structures
> 5. **Version Your Macros**
>    - Export macro configs regularly (QuickAdd settings → backup)
>    - Keep copies of working versions
>    - Document major changes
> 6. **Modularize Complex Workflows**
>    - Break into sub-macros
>    - Create reusable components
>    - Use nested macros for shared steps
> 7. **Optimize for User Experience**
>    - Minimize prompts (use smart defaults)
>    - Provide clear feedback (notices)
>    - Make commonly-used macros easily accessible
>    - Consider hotkey assignments
> 8. **Learn from Generated Examples**
>    - Study the step sequences
>    - Understand variable flow patterns
>    - Note error handling approaches
>    - Adapt patterns to your needs
> 9. **Combine with Other Prompts**
>    - Use Script Generation Prompt for complex logic
>    - Use Templater Template Prompt for template content
>    - Build complete systems across all tools
> 10. **Iterate and Refine**
>     - First version doesn't need to be perfect
>     - Gather usage patterns
>     - Simplify based on actual use
>     - Remove unnecessary steps

---

# prompt-bulk-quickadd-macros-v1.0.0-2025121905

`````prompt
----
Prompt-ID: "2025121905"
Prompt-Version: 1.0.0
----

`````markdown
You are a world-class Obsidian automation expert specializing in QuickAdd Macro design and workflow engineering. You have deep expertise in designing multi-step automation workflows, variable passing, conditional logic, template integration, and creating sophisticated capture-to-organization pipelines.
Your task is to generate a comprehensive collection of QuickAdd Macro configurations to be used as inspiration and educational examples for a user building their own PKB automation system. You must generate a wide variety of macros, ranging from simple linear workflows to highly advanced conditional pipelines.
The examples must be centered around the theme of: **[INSERT THEME HERE]**
**CRITICAL FORMATTING RULE:** All code/template blocks you generate MUST use plain Markdown backticks (```) with **NO language identifier** (do NOT use ```javascript, ```yaml, etc.). This is to ensure the code is stored as inert text and does not auto-execute within an Obsidian note.
**MACRO DOCUMENTATION FORMAT:** Each macro must be documented with its complete configuration, including all steps, templates, scripts, and variable flows in a way that can be manually configured in QuickAdd settings.
You must follow this structure precisely:

---
## Basic Macros (2-4 Steps)
*Provide 3-4 examples of fundamental QuickAdd macros. These should demonstrate:
- Simple linear workflows (2-4 steps)
- Basic Capture → Template pattern
- Simple variable usage
- Single-destination file creation
- Basic user prompts
For each macro, provide:
- **Macro Name** (what to name it in QuickAdd)
- **Purpose** (1-2 sentences explaining what it does)
- **Step-by-Step Configuration** (detailed UI setup instructions)
- **Variables Used** (list with descriptions)
- **Templates** (if any, in plain code blocks)
- **Expected Outcome** (what happens when executed)
Use this format:*
```
### [Macro Name]
**Purpose:** [What this macro accomplishes]
**Configuration Steps:**
1. [Step 1: Type, settings, details]
2. [Step 2: Type, settings, details]
3. [Step 3: Type, settings, details]
**Variables:**
- `variableName`: [Description and how it's populated]
**Templates:** [If any templates are used, include their content in plain code blocks]
**Execution Flow:** [Step-by-step description of what happens when macro runs]
**Usage:** [How to trigger this macro]
```

---
## Intermediate Macros (4-8 Steps)
*Provide 3-4 examples of more complex QuickAdd macros. These should include:
- Multi-step workflows (4-8 steps)
- Conditional choices (IF/THEN patterns)
- User script integration
- Variable transformations between steps
- Multiple file creation or updates
- Folder logic based on inputs
- Template + Capture combinations
For each macro, provide:
- **Macro Name**
- **Purpose** (2-3 sentences)
- **Step-by-Step Configuration** (detailed UI setup)
- **Variables Used** (comprehensive list with data flow)
- **Templates** (all template content in plain code blocks)
- **Scripts** (if any, with file names and basic logic description)
- **Conditional Logic** (if any, explain branching)
- **Expected Outcome**
- **Setup Requirements** (any prerequisites)
Use the same format as Basic Macros but with more detail.*

---
## Advanced Macros (8+ Steps)
*Provide 2-3 examples of sophisticated QuickAdd macros demonstrating expert-level workflow engineering.*
**For each Advanced Macro, you MUST provide:**
1. **Macro Name & Purpose**
   - Name for QuickAdd configuration
   - Comprehensive description (3-4 sentences) of workflow and problem solved
2. **Architecture Overview**
   - High-level flow diagram (text-based)
   - Key decision points
   - Data transformation pipeline
   - File creation/update points
3. **Complete Step-by-Step Configuration**
   - Every step numbered and detailed
   - Exact settings for each step
   - Variable assignments at each stage
   - Conditional logic configuration
   - Script attachments and parameters
4. **Variables & Data Flow**
   - Complete variable list with types and sources
   - Variable transformations between steps
   - Variable scope and persistence
   - Default values and validation
5. **All Templates**
   - Every template used, with clear names
   - Complete template content in plain code blocks
   - Templater syntax usage notes
   - Variable insertion points
6. **All Scripts**
   - Script file names and locations
   - Script purpose and logic description
   - Input parameters and return values
   - Error handling notes
   - (Full script code in separate Script Generation Prompt)
7. **Top Use Cases**
   - 2-3 specific scenarios where this macro excels
   - Benefits over manual workflows
   - Time/effort savings estimation
8. **Setup Requirements**
   - Prerequisites (plugins, folders, templates, scripts)
   - One-time configuration steps
   - Folder structure requirements
   - Template location setup
9. **Customization Options**
   - 2-3 ways to adapt the macro
   - Optional steps that can be added/removed
   - Variable modifications for different workflows
   - Alternative branching logic
10. **Troubleshooting Guide**
    - Common issues and solutions
    - Variable debugging tips
    - Step failure recovery
    - Testing methodology
*After the documentation, provide a **Configuration Summary** in a structured format that can be used as a checklist during setup.*
These advanced macros should demonstrate:
- **Complex conditional branching** (multiple choice points, nested conditions)
- **Loop-like behavior** (recursive choices, iterative captures)
- **Multi-file workflows** (creating/updating several files in sequence)
- **Intelligent routing** (different outcomes based on inputs)
- **Template orchestration** (multiple templates working together)
- **Script-heavy automation** (leveraging multiple user scripts)
- **Cross-folder organization** (smart filing based on metadata)
- **Metadata-driven workflows** (using frontmatter to control flow)

---
## Compound Macros (Multi-Macro Systems)
*Provide 2-3 examples of macro systems where multiple macros work together to create sophisticated workflows.*
**For each Compound Macro System, you MUST provide:**
1. **System Name & Purpose**
   - Overall system name
   - Comprehensive description of the compound workflow
   - How multiple macros interact
2. **System Architecture**
   - List of all macros in the system
   - How they call or depend on each other
   - Shared resources (templates, scripts, variables)
   - Data flow between macros
3. **Individual Macro Configurations**
   - Complete configuration for each macro in the system
   - How each macro contributes to overall workflow
   - Trigger methods for each
4. **Shared Resources**
   - Templates used across multiple macros
   - Scripts shared between macros
   - Variable naming conventions for consistency
   - Folder structure requirements
5. **Integration Patterns**
   - How macros trigger each other
   - Variable passing between macros
   - File creation dependencies
   - Synchronization points
6. **Top Use Cases**
   - 2-3 scenarios for the complete system
   - Advantages of multi-macro approach
   - Workflow examples from start to finish
7. **Complete Setup Guide**
   - Order of macro creation
   - Shared resource setup
   - Testing sequence
   - Validation checklist
8. **Customization & Extension**
   - How to add new macros to the system
   - How to modify workflow paths
   - Optional enhancement suggestions
These compound systems should demonstrate:
- **Hierarchical workflows** (master macro calling sub-macros)
- **Parallel processing** (multiple macros for different content types)
- **Lifecycle management** (macros for create → update → archive)
- **Review systems** (capture → process → review → archive chains)
- **Project ecosystems** (init → track → update → complete macros)
- **Content pipelines** (ingest → process → organize → publish workflows)

---
## Context: Your PKB Metadata & Structure
This is my metadata quick reference and folder structure for you to use when configuring the macros.
### Available Options for Metadata Fields
#### type
- analysis, claude-project, cog-sci-report, concept, cosmo-report, dashboard, definition, edu-report, experiment, framework, gemini-gem, guide, literature, mental-model, moc, pattern, permanent-note, pkb-report, principle, prompt, prompt-report, reference, report, review, theory, tutorial
#### source
- claude-opus-4.1, claude-sonnet-4.5, gemini-flash-2.5, gemini-flash-3.0, gemini-pro-2.5, gemini-pro-3.0
#### maturity
- needs-review, seedling, developing, budding, evergreen
#### confidence
- speculative, provisional, moderate, established, high
#### status
- active, archived, deprecated
#### priority
- low, medium, high, urgent
#### link-up (MOCs)
- `[[artificial-intelligence-moc]]`, `[[cognitive-science-moc]]`, `[[cosmology-moc]]`, `[[educational-psychology-moc]]`, `[[learning-theory-moc]]`, `[[neuroscience-moc]]`, `[[pkb-&-pkm-moc]]`, `[[practical-philosophy-moc]]`, `[[prompt-engineering-moc]]`
#### Tags
#pkm, #pkb, #prompt-engineering, #cognitive-science, #cosmology, #type/report, #type/reference, #type/permanent, #status/complete, #status/in-progress, #status/not-read, #status/read, #status/seedling, #status/budding, #status/developing, #status/evergreen, #status/needs-review, #year/2025, #cognitive-pkm, #cognitive-enhancement, #cognitive-training, #automation, #quickadd, #workflow
### Folder Hierarchy
#### Level 0: Core Infrastructure
- 00-inbox/ → Ingestion & triage zone
- 00-meta/ → System memory & configuration
- 000_database/ → Database storage
#### Level 1: Temporal Organization
- 01-daily-notes/ → Atomic daily entries (time-indexed)
#### Level 2-7: Content Layers
- 02-projects/ → Active project documentation
- 03-notes/ → Core knowledge atoms
- 04-library/ → Reference materials & resources
- 05-tasks-&-reviews/ → GTD & reflection systems
- 06-dashboards/ → Overview & summary pages
- 07-mocs/ → Maps of Content (graph hubs)
#### Level 99: System Management
- 99-archive/ → Deprecated/completed content
- 99-system/ → System configuration files
  - 99-system/templates/ → Template storage
  - 99-system/scripts/quickadd/ → QuickAdd scripts location

---
## Macro Generation Guidelines
### QuickAdd Step Types Reference
**CAPTURE**
- Purpose: Create a new file with user input
- Settings: Format, file name format, created file location, append/prepend
- Variable capture: Automatically captures input as `{{VALUE}}`
- Use for: New notes, journal entries, inbox items
**TEMPLATE**
- Purpose: Insert template at cursor or create file from template
- Settings: Template path, file name format (if creating file), folder
- Variable usage: Can use all QuickAdd variables in template
- Use for: Structured content, frontmatter generation, boilerplate
**MACRO (Nested)**
- Purpose: Call another macro as a step
- Settings: Which macro to execute
- Variable passing: Shares variable scope with parent
- Use for: Reusable sub-workflows, modular design
**OBSIDIAN COMMAND**
- Purpose: Execute any Obsidian command
- Settings: Command to execute
- Variable context: Variables persist but command may not use them
- Use for: Plugin integrations, workspace manipulation
**USER SCRIPT**
- Purpose: Execute custom JavaScript
- Settings: Script file path
- Variable manipulation: Can read and set QuickAdd variables
- Use for: Complex logic, data transformation, API calls
**CHOICE**
- Purpose: Present user with options, branch workflow
- Settings: Choice options (list of sub-macros or choices)
- Variable impact: User selection can be captured
- Use for: Conditional branching, workflow routing
**AI ASSISTANT** (if enabled)
- Purpose: Generate content using AI
- Settings: Prompt, model, parameters
- Variable usage: Can use variables in prompts
- Use for: Content generation, summarization, transformation
### Variable System Best Practices
**Variable Naming:**
- Use descriptive names: `projectName`, `targetFolder`, `sourceType`
- Use camelCase for consistency
- Prefix by source: `input_`, `script_`, `template_`, `system_`
- Document purpose in macro configuration
**Variable Sources:**
- `{{VALUE}}` - Captured input from user
- `{{DATE}}`, `{{TIME}}` - System date/time (various formats)
- `{{VAULTNAME}}` - Current vault name
- Custom variables from scripts: `{{variableName}}`
- Template variables from Templater: `<% tp.* %>`
**Variable Scope:**
- Variables persist across all steps in a macro
- Variables are shared with nested macros
- Variables are cleared after macro completes
- Use scripts to persist data between macro runs (write to files)
**Variable Transformation:**
- Use scripts to modify variables between steps
- Format dates: `{{DATE:YYYY-MM-DD}}`
- String manipulation: via user scripts
- Conditional values: via choice steps or scripts
### Configuration Best Practices
**Macro Organization:**
1. **Name clearly:** "Create Project Note", not "New Note"
2. **Group related macros:** Use folders in QuickAdd settings
3. **Document purpose:** Add description in macro settings
4. **Test incrementally:** Build and test step-by-step
5. **Version control:** Export macro configs regularly
**Step Design:**
6. **Order matters:** Plan sequence before configuring
7. **Fail gracefully:** Add validation at critical points
8. **Provide feedback:** Use notices for user confirmation
9. **Handle errors:** Scripts should catch and report errors
10. **Keep modular:** Break complex workflows into sub-macros
**Template Integration:**
11. **Store templates centrally:** `99-system/templates/`
12. **Use consistent naming:** Match template name to purpose
13. **Document variables:** Comment which variables template expects
14. **Test independently:** Verify templates work before macro integration
15. **Version templates:** Keep copies of working versions
**Script Integration:**
16. **Store scripts centrally:** `99-system/scripts/quickadd/`
17. **Document interfaces:** Clear input/output for each script
18. **Handle async properly:** Use async/await in scripts
19. **Return values:** Scripts should return status/data
20. **Error messages:** Scripts should report failures clearly
### Workflow Design Patterns
**Pattern 1: Linear Capture**
```
Capture Input → Format Data → Create File → Open File
```
Use for: Simple note creation, quick entry
**Pattern 2: Conditional Routing**
```
Capture Input → Choice (Type?) → Branch A or B → Create File
```
Use for: Multi-type captures (project/note/task)
**Pattern 3: Multi-File Creation**
```
Capture Input → Script (Generate Data) → Create File 1 → Create File 2 → Link Files
```
Use for: Projects with multiple related files
**Pattern 4: Process & Organize**
```
Capture → Template → Script (Analyze) → Move to Folder → Update Index
```
Use for: Inbox processing, content triage
**Pattern 5: Review & Update**
```
Script (Find Files) → Choice (Select File) → Update Template → Script (Update Metadata)
```
Use for: Periodic reviews, status updates
**Pattern 6: Hierarchical Workflow**
```
Master Macro → Choice → Sub-Macro A or Sub-Macro B → Shared Final Step
```
Use for: Complex workflows with shared steps
### Testing & Validation
**Testing Checklist:**
1. **Test with minimal input:** Does it handle empty values?
2. **Test with edge cases:** Special characters, long strings, etc.
3. **Test variable flow:** Are variables available when needed?
4. **Test script execution:** Do scripts complete without errors?
5. **Test file creation:** Files created in correct locations?
6. **Test template rendering:** Variables properly substituted?
7. **Test conditional branches:** All paths work correctly?
8. **Test error conditions:** Graceful failure when things go wrong?
**Debugging Tips:**
- Enable QuickAdd debug mode in settings
- Check console (Ctrl+Shift+I) for errors
- Add `new Notice()` in scripts to trace execution
- Test scripts independently before integration
- Verify template paths are correct
- Check variable names match exactly (case-sensitive)
### Documentation Standards
Each macro configuration should include:
**In Macro Settings (QuickAdd UI):**
- Clear macro name
- Description of purpose
- Notes about required setup
- List of templates/scripts used
**In Supporting Documentation:**
- Complete step-by-step setup guide
- Variable list with descriptions
- Template content with annotations
- Script summaries (full code in script files)
- Example execution with screenshots or walkthrough
- Troubleshooting common issues
### Performance Considerations
**Optimization Tips:**
1. **Minimize script steps:** Combine operations when possible
2. **Cache data:** If scripts read files, cache results
3. **Avoid nested loops:** In scripts processing multiple files
4. **Use efficient Obsidian API calls:** Batch operations when available
5. **Limit choice options:** Too many slow down UI
**Scalability Considerations:**
6. **Test with large vaults:** Some operations slow with many files
7. **Avoid full vault scans:** Filter by folder when possible
8. **Consider async operations:** For long-running scripts
9. **Provide progress feedback:** For multi-step processes
10. **Allow cancellation:** User should be able to abort
**For themes involving:**
- **Capture workflows** → Focus on quick entry, minimal friction, smart defaults, automatic organization
- **Project management** → Emphasize initialization workflows, status tracking, milestone automation, project closure
- **Content processing** → Highlight inbox triage, categorization, enrichment, filing automation
- **Review systems** → Feature periodic review selection, status updates, completion tracking
- **Research workflows** → Showcase literature processing, source tracking, synthesis automation
- **Linking & Navigation** → Demonstrate automatic cross-referencing, MOC updates, graph building

---
## Output Format Reminder
Each macro configuration should:
- Use plain backticks (```) with NO language identifier for all code/template blocks
- Provide complete, step-by-step UI configuration instructions
- Include all templates in full (not just references)
- Describe script logic clearly (full code in Script Generation Prompt)
- Show exact variable names and usage
- Provide clear testing steps
- Include troubleshooting guidance
- Be ready to manually configure in QuickAdd (no import/export formats)
**Macro documentation structure:**
1. Name and Purpose (clear, concise)
2. Step-by-Step Configuration (numbered, detailed)
3. Variables Used (list with descriptions and data flow)
4. Templates (full content in code blocks)
5. Scripts (descriptions and interfaces)
6. Execution Flow (what happens when run)
7. Setup Requirements (prerequisites)
8. Testing Steps (how to verify it works)
9. Customization Options (how to adapt)
10. Troubleshooting (common issues and solutions)
Provide comprehensive, production-ready macro configurations that demonstrate the full power of QuickAdd workflow automation while remaining accessible, well-documented, and immediately configurable by users of varying skill levels.
`````

---



