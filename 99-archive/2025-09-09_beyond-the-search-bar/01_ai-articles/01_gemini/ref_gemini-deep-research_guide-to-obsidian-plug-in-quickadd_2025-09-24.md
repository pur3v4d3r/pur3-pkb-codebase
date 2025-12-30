# A Comprehensive Guide to the Obsidian QuickAdd Plugin: Automating Knowledge Capture and Workflow

## Part 1: The Philosophy of Seamless Capture: Why QuickAdd Matters

### Beyond Note-Taking: The Principles of Modern PKM

Personal Knowledge Management (PKM) is the systematic process of gathering, classifying, storing, and retrieving knowledge to support daily activities and creative work.1 In its modern form, it transcends simple note-taking, aiming to construct a "Tool for Thought" or "Second Brain"—a centralized, interconnected digital environment for thinking and creating.2 The effectiveness of such a system hinges on a core principle: frictionless capture.2 The barrier between having an idea and recording it within the system must be minimal; high friction leads to lost ideas and an underutilized knowledge base.

Many PKM systems fail because they rely on complex, manual organization. Users design intricate folder hierarchies or tagging taxonomies, which creates decision fatigue with every new piece of information: "Where does this note go? What tags should I apply?".4 This friction discourages capture, leading to a state where more time is spent managing the system than thinking

_with_ it.2 Manual organization breaks down as a knowledge base scales, making automation and templates critical for maintaining consistency and enabling growth.2

QuickAdd directly addresses this fundamental challenge. It inverts the traditional workflow by front-loading organizational decisions into predefined, automated actions. Instead of manually filing a new project note, the user invokes a "New Project" command that automatically creates the note from a template, names it according to a set format, and places it in the correct folder. This strategic automation makes the daily act of knowledge capture nearly effortless, shifting the user's focus from administrative tasks to the content of their thoughts.6 By serving as the primary, automated input mechanism for a centralized knowledge base, QuickAdd facilitates the creation of a scalable, consistent, and ultimately more useful "Tool for Thought".2

### The Science of Flow: Minimizing Cognitive Load to Maximize Creativity

The pursuit of a frictionless system is not merely a matter of convenience; it is grounded in the principles of cognitive science. Cognitive Load Theory (CLT) posits that human working memory—the mental space where active information processing occurs—is a finite resource.8 Effective learning and complex problem-solving depend on the efficient use of this limited capacity. CLT identifies three types of cognitive load that compete for these resources:

1.  **Intrinsic Load**: The inherent complexity of the information itself. This is the effort required to understand a difficult concept.10
2.  **Germane Load**: The desirable mental effort dedicated to processing new information, forming connections with existing knowledge, and constructing long-term memory schemas. This is the cognitive process associated with deep work, analysis, and synthesis.11
3.  **Extraneous Load**: The unnecessary mental effort demanded by the way information is presented or the tools used to interact with it. This "noise" includes confusing user interfaces, poorly structured material, and cumbersome manual processes. It is detrimental to learning and creativity as it consumes cognitive resources that could otherwise be allocated to germane load.9

The QuickAdd plugin functions as a powerful cognitive offloading tool designed to systematically reduce extraneous load. Each manual step in the knowledge capture process—navigating to a folder, deciding on a file name, typing boilerplate text, applying standard tags—imposes a small but cumulative extraneous load. A QuickAdd workflow, such as a hotkey-triggered command to create a structured meeting note, automates these administrative steps entirely. The user is not required to expend mental energy on the file's name, location, or template; their cognitive resources are preserved for the germane task of capturing the meeting's content.

By automating the extraneous load associated with knowledge management, QuickAdd directly increases the cognitive capacity available for germane load—the actual thinking. This makes it a strategic tool for anyone engaged in knowledge work. The time invested in configuring the plugin yields significant returns by preserving the user's most valuable asset: their finite cognitive energy for the deep work that generates novel ideas and solves complex problems.8

## Part 2: Mastering the QuickAdd Toolkit: A Feature-by-Feature Guide

### Initial Setup and Core Concepts

Before creating advanced workflows, it is essential to install the plugin and understand its fundamental components.

Installation:

QuickAdd can be installed directly from within Obsidian.7

1.  Navigate to Settings > Community plugins.
2.  Ensure Restricted mode is turned off.
3.  Click Browse to open the community plugins browser.
4.  Search for "QuickAdd".
5.  Click Install, and once installation is complete, click Enable.

Core Concepts:

The foundation of QuickAdd is the Choice. A Choice is a pre-configured action that can be triggered to perform a specific task.7 All automation in QuickAdd is built by creating and combining these choices. There are four primary types of choices 15:

*   **Template**: Creates a new note based on a predefined template file.
*   **Capture**: Appends text or tasks to an existing note without needing to open it.
*   **Macro**: Chains multiple choices and other Obsidian commands into a single, powerful workflow.
*   **Multi**: A folder-like container used to organize other choices for better management.

To begin, open the QuickAdd settings, where a list of current choices is displayed. Clicking the "Add Choice" button allows for the creation of a new action, starting the journey into workflow automation.

### The Architect: Creating Notes with Template Choices

The Template choice is the most common starting point for using QuickAdd. It automates the creation of new, consistently structured notes, forming the architectural backbone of a scalable knowledge base.15 It programmatically enforces consistency, ensuring that every note of a certain type (e.g., a book note, a meeting summary) has the same properties and structure, which is vital for downstream processes like Dataview queries.2

**Step-by-Step Guide: Creating a "New Project" Template Choice**

1.  **Create the Template File**: First, create a new note that will serve as the template. For example, create a file at Templates/Project Template.md with the desired structure, including properties and headings.
2.  **Create the QuickAdd Choice**: In QuickAdd settings, click Add Choice. Name it "New Project" and select Template from the dropdown menu. Click Add Choice.
3.  **Configure the Choice**: Click the gear icon next to the newly created choice to configure its settings.
    *   **Template Path**: This is a mandatory setting. Select the template file you created in step 1 (Templates/Project Template.md).17
    *   **File Name Format**: Define how the new note's file name will be generated. This field supports dynamic variables. A common format is {{DATE}} - {{VALUE:Project Name}}. This will prepend the current date and then prompt the user for input with the label "Project Name".17
    *   **Create in folder**: Specify the destination folder for the new note, for instance, 10-Projects/. If multiple folders are specified, QuickAdd will present a suggester asking where to create the file.17
    *   **Key Settings**:
        *   **Open**: Toggle this on to automatically open the newly created note in the editor.
        *   **Increment file name**: If a file with the generated name already exists, this setting will append a number to the new file's name (e.g., Project-1.md) to avoid conflicts.17
        *   **If file already exists**: This setting defines behavior when a file with the same name exists. Options include appending content to the top or bottom of the file, overwriting it, or simply opening the existing file without modification.17
        *   **Append link**: When enabled, this will insert a link to the newly created project note in the file that was active when the choice was triggered. This is useful for linking from a daily note or a central project index.17

**Table 1: QuickAdd Format Syntax Reference Guide**

QuickAdd's power comes from its dynamic format syntax, which allows for prompts, dates, and other variables to be inserted into file names and note content.19

| Syntax | Description | Example Usage |
| --- | --- | --- |
| {{VALUE}} or {{NAME}} | Prompts the user for a single text input. Uses selected text if available. | File Name: {{VALUE}} |
| {{VALUE:Variable Name}} | Prompts the user for input using a specific label. Allows for multiple, named variables in a single workflow. | Title: {{VALUE:Book Title}} |
| {{VALUE:Var|Default}} | Prompts for input but uses a default value if the prompt is left empty. | Status: {{VALUE:Status|To-Do}} |
| {{DATE}} | Inserts the current date in YYYY-MM-DD format. | Daily Note {{DATE}}.md |
| {{DATE:<format>}} | Inserts the current date in a custom format based on Moment.js syntax. | Meeting on {{DATE:dddd, MMMM Do}} |
| {{DATE+N}} or {{DATE-N}} | Inserts a date offset from the current date by N days. | Deadline: {{DATE+7}} |
| {{VDATE:Var,Format}} | Prompts the user for a date using natural language (e.g., "tomorrow", "next Friday") and formats it. The variable Var stores the input for reuse. | Project Start: {{VDATE:startDate, YYYY-MM-DD}} |
| {{LINKCURRENT}} | Inserts a wikilink to the currently active file. Resolves to an empty string if no file is active (when configured).7 | Source: {{LINKCURRENT}} |

### The Collector: Appending Information with Capture Choices

The Capture choice is the embodiment of frictionless capture. It allows users to append information to existing notes—such as a daily log, a task list, or an inbox—without leaving their current context.6 This is critical for maintaining a flow state, as it eliminates the high cognitive cost of switching windows, navigating to a file, adding a line, and returning to the original task.

**Step-by-Step Guide: Creating a "Daily Log" Capture Choice**

1.  **Create the Choice**: In QuickAdd settings, add a new choice named "Daily Log" and select the Capture type.
2.  **Configure the Destination**:
    *   **Capture To**: This field specifies the target file. To capture to the daily note, use a dynamic name like Journal/{{DATE}}.md.20
    *   **Dynamic Targeting**: This field is exceptionally versatile. Leaving it blank will prompt a suggester listing all files in the vault. Typing a folder path (e.g., CRM/) or a tag (e.g., `#people`) will filter the suggester to only show relevant files, enabling rapid capture to any note.20
    *   **Create file if it doesn't exist**: Enable this and specify a daily note template. This ensures that if the daily note for the current day does not exist, QuickAdd will create it before capturing the new information.20
3.  **Define the Capture Format**:
    *   **Capture Format**: This setting controls the structure of the appended text. It acts as a mini-template. For a timestamped log entry, use: - {{DATE:HH:mm}} {{VALUE}}.20 For a new task, a format like  
        \- \[ \] {{VALUE}} 📅 {{DATE}} would be appropriate.
4.  **Specify the Insertion Point**:
    *   **Insert after**: This powerful feature allows appending text under a specific heading or line. For a daily log, you might specify ## Log. If the heading does not exist in the target file, the Create line if not found option will add it automatically.20
    *   **Write to bottom of file**: If Insert after is not used, this toggle determines whether the new content is added to the top or bottom of the file.20
5.  **Finalize Settings**:
    *   **Task**: This simple toggle formats the captured input as a standard Markdown task (e.g., - \[ \]...).20
    *   **Append link**: This will add a link to the currently active file alongside the captured text, providing valuable context.20

### The Conductor: Automating Workflows with Macro Choices

Macros are the most advanced feature in QuickAdd, allowing users to chain multiple choices and commands into a single, automated workflow.15 They transform Obsidian from a passive note-taking tool into an active assistant by codifying personal, repetitive processes into a single, executable command.6 This act of designing a macro also encourages reflection on and refinement of one's own workflows.2

**Beginner's Macro: "Log a New Book" Workflow**

This macro will automate the process of creating a new note for a book and simultaneously adding that book to a master reading list.

1.  **Create Building Blocks**:
    *   Create a **Template Choice** named "T - New Book Note". Configure it to use a book template and name the file Books/{{VALUE:Book Title}}.md.
    *   Create a **Capture Choice** named "C - Add to Reading List". Configure it to capture to a file named Reading List.md and use the capture format - \[ \]\].
2.  **Create the Macro Choice**:
    *   In QuickAdd settings, create a new choice named "M - Log New Book" and select the Macro type.
3.  **Build the Macro**:
    *   Click the gear icon to open the Macro Builder.
    *   **Step 1**: In the dropdown, select Nested Choice and choose "T - New Book Note". Click Add. This command will run first, creating the new book note and prompting the user for the book's title.24
    *   **Step 2**: Add another Nested Choice command, this time selecting "C - Add to Reading List". Click Add. The macro will automatically pass the variable (the book title) entered in the first step to this second step, adding a link to the new note in the Reading List.md file.23

**Advanced Macro Concepts**

The Macro Builder supports various command types that unlock immense potential 24:

*   **Obsidian Command**: Executes any command available in the Obsidian command palette (e.g., "Daily notes: Open today's daily note").
*   **Editor Commands**: Manipulates text in the active editor, such as copy, paste, or select line.
*   **User Script**: Runs custom JavaScript code, enabling complex operations like fetching data from external APIs (e.g., movie or book databases) or performing advanced file manipulation.15
*   **Wait**: Pauses the macro for a specified number of milliseconds, useful when a preceding command needs time to complete.
*   **AI Assistant**: Integrates with AI providers to generate or process text within a workflow.

When developing macros, it is best practice to use modular design by breaking complex processes into smaller, reusable choices and scripts, and to include error handling within user scripts to ensure robustness.24

### The Organizer: Structuring Your Actions with Multi Choices

As a user's library of QuickAdd choices grows, the main command palette can become cluttered, reintroducing the friction the tool was designed to eliminate. The Multi choice solves this by acting as a folder to group related actions.16 This is a meta-organizational feature that ensures the QuickAdd system itself remains scalable and easy to navigate.

**Using a Multi Choice**

1.  **Create the Multi Choice**: In QuickAdd settings, add a new choice, name it (e.g., "New Entry"), and select the Multi type.
2.  **Organize Other Choices**: The Multi choice will appear in the list with a dropdown arrow. To add an existing choice to it, click and hold the drag handle (the six dots) of that choice and drag it slightly below and to the right of the Multi choice's name. When successful, the choice will become indented, indicating it is now part of that group.26
3.  **Access Grouped Choices**: When the main QuickAdd command is run, "New Entry" will appear as a single option. Selecting it will then display a secondary list containing all the nested choices (e.g., "New Project," "New Meeting," "New Person"), creating a clean, hierarchical menu.27

## Part 3: Advanced Implementation and Bespoke Workflows

### The Need for Speed: Activating Choices with Hotkeys

While activating choices from the command palette is efficient, assigning dedicated hotkeys is the final step in making a workflow truly frictionless. This moves the action from a deliberate, multi-step process into subconscious muscle memory, allowing capture at the speed of thought.

**Step-by-Step Guide to Assigning a Hotkey**

1.  **Expose the Command**: In the main QuickAdd settings menu, find the choice you want to assign a hotkey to. To the right of its name is a lightning bolt icon. Click this icon to toggle it on. This action makes the specific choice available as a distinct command in Obsidian's command palette.22
2.  **Assign the Hotkey**:
    *   Navigate to Obsidian's core settings via Settings > Hotkeys.
    *   In the filter box, type the name of your QuickAdd choice (e.g., "Daily Log").
    *   The command QuickAdd: Daily Log will appear in the list.
    *   Click the + icon to the right of the command to define a custom hotkey.
    *   Press the desired key combination (e.g., Ctrl+Alt+L). It is advisable to use modifiers like Ctrl, Alt, or Shift to avoid conflicts with native Obsidian shortcuts.29

With a hotkey assigned, the "Daily Log" capture prompt can now be summoned instantly from anywhere within Obsidian, removing the last piece of friction from the activation process.

### Beyond Obsidian: Global Quick Capture

Ideas and tasks often arise when working outside of Obsidian—while browsing the web, reading an email, or using another application. Global quick capture breaks down this final barrier, making the knowledge base omnipresent and ensuring no idea is lost, regardless of context. This is achieved by using URI schemes to trigger QuickAdd commands from external automation tools.22

This advanced technique requires the Obsidian Advanced URI community plugin to be installed and enabled. The basic URI to run a QuickAdd choice is:

obsidian://advanced-uri?vault=<YOUR\_VAULT\_NAME>&commandname=QuickAdd: <CHOICE\_NAME>

**Implementation for Windows using AutoHotkey (AHK)**

AutoHotkey is a free scripting utility for Windows. A simple script can be created to bind a global hotkey that activates Obsidian and triggers a specific QuickAdd choice.31

1.  Install AutoHotkey.
2.  Create a new text file and save it with a .ahk extension.
3.  Add the following script, replacing <YOUR\_VAULT\_NAME> and <CHOICE\_NAME> with your specific details 32:  
    Code snippet  
    ; Use Ctrl+Alt+G as the global hotkey  
    ^!g::  
    Run "obsidian://advanced-uri?vault=<YOUR\_VAULT\_NAME>&commandname=QuickAdd: <CHOICE\_NAME>"  
    Return  
    
4.  Run the script. Now, pressing Ctrl+Alt+G anywhere in Windows will launch the specified QuickAdd action.

**Implementation for macOS**

On macOS, this can be achieved with several tools 32:

*   **macOS Shortcuts**: Create a new shortcut, add an "Open URLs" action, and paste the Obsidian Advanced URI. Then, in the shortcut's details, assign a keyboard shortcut to it.
*   **Alfred or Raycast**: Create a new workflow or quicklink that opens the URI, which can then be triggered via the launcher's interface or a dedicated hotkey.

Implementing global capture transforms a PKM system from an application one must consciously open into a service that is always available, fundamentally enhancing its role as a true "second brain."

### Conclusion: Building Your Personalized Thinking Environment

This guide has journeyed from the foundational philosophy of frictionless capture and cognitive load management to the practical mastery of QuickAdd's core features and their seamless integration into a daily workflow. The plugin's power lies not in its individual components, but in its capacity as a toolkit for constructing a deeply personalized thinking environment.

The ultimate goal is not to implement every possible automation, but to thoughtfully identify and eliminate the specific points of friction within one's own creative and intellectual processes.2 The most effective system is one that evolves with its user, starting with a single, simple workflow—automating the creation of a daily note or the capture of a fleeting task—and gradually expanding as new needs and opportunities for efficiency are discovered. By leveraging the principles of automation, QuickAdd empowers users to build a system that minimizes administrative overhead, preserves cognitive energy, and ultimately serves as a powerful, silent partner in the process of thinking, learning, and creating.

#### Works cited

1.  Personal knowledge management - Wikipedia, accessed September 24, 2025, [https://en.wikipedia.org/wiki/Personal\_knowledge\_management](https://en.wikipedia.org/wiki/Personal_knowledge_management)
2.  Personal Knowledge Management at Scale - Analyzing 8,000 Notes ..., accessed September 24, 2025, [https://www.dsebastien.net/personal-knowledge-management-at-scale-analyzing-8-000-notes-and-64-000-links/](https://www.dsebastien.net/personal-knowledge-management-at-scale-analyzing-8-000-notes-and-64-000-links/)
3.  Personal Knowledge Management at Scale - Analyzing 8,000 Notes and 64,000 Links : r/PKMS - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/PKMS/comments/1ii4x11/personal\_knowledge\_management\_at\_scale\_analyzing/](https://www.reddit.com/r/PKMS/comments/1ii4x11/personal_knowledge_management_at_scale_analyzing/)
4.  What if it could be easy? Imagining a frictionless note taking system, accessed September 24, 2025, [https://elizabethbutlermd.com/easy-note-taking/](https://elizabethbutlermd.com/easy-note-taking/)
5.  A Complete Guide to Tagging for Personal Knowledge Management - Forte Labs, accessed September 24, 2025, [https://fortelabs.com/blog/a-complete-guide-to-tagging-for-personal-knowledge-management/](https://fortelabs.com/blog/a-complete-guide-to-tagging-for-personal-knowledge-management/)
6.  Using the Obsidian Quick Add Plugin - Fork My Brain, accessed September 24, 2025, [https://notes.nicolevanderhoeven.com/system/cards/Using+the+Obsidian+Quick+Add+Plugin](https://notes.nicolevanderhoeven.com/system/cards/Using+the+Obsidian+Quick+Add+Plugin)
7.  QuickAdd for Obsidian, accessed September 24, 2025, [https://www.obsidianstats.com/plugins/quickadd](https://www.obsidianstats.com/plugins/quickadd)
8.  Managing cognitive load optimises learning | Australian Education Research Organisation, accessed September 24, 2025, [https://www.edresearch.edu.au/summaries-explainers/explainers/managing-cognitive-load-optimises-learning](https://www.edresearch.edu.au/summaries-explainers/explainers/managing-cognitive-load-optimises-learning)
9.  Balancing cognitive load in design work: A conceptual and narrative review - DRS Digital Library, accessed September 24, 2025, [https://dl.designresearchsociety.org/cgi/viewcontent.cgi?article=3426&context=drs-conference-papers](https://dl.designresearchsociety.org/cgi/viewcontent.cgi?article=3426&context=drs-conference-papers)
10.  Optimizing Lectures From a Cognitive Load Perspective - PMC, accessed September 24, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7369498/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7369498/)
11.  Reduce cognitive load - CATL Teaching Improvement Guide | UW-La Crosse, accessed September 24, 2025, [https://www.uwlax.edu/catl/guides/teaching-improvement-guide/how-can-i-improve/reduce-cognitive-load/](https://www.uwlax.edu/catl/guides/teaching-improvement-guide/how-can-i-improve/reduce-cognitive-load/)
12.  Challenging Cognitive Load Theory: The Role of Educational Neuroscience and Artificial Intelligence in Redefining Learning Efficacy - PMC - PubMed Central, accessed September 24, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11852728/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11852728/)
13.  Six Strategies You May Not Be Using To Reduce Cognitive Load - The eLearning Coach, accessed September 24, 2025, [https://theelearningcoach.com/learning/reduce-cognitive-load/](https://theelearningcoach.com/learning/reduce-cognitive-load/)
14.  QuickAdd for Obsidian - GitHub, accessed September 24, 2025, [https://github.com/chhoumann/quickadd](https://github.com/chhoumann/quickadd)
15.  Getting Started | QuickAdd, accessed September 24, 2025, [https://quickadd.obsidian.guide/docs/](https://quickadd.obsidian.guide/docs/)
16.  Obsidian QuickAdd - Fork My Brain, accessed September 24, 2025, [https://notes.nicolevanderhoeven.com/Obsidian+QuickAdd](https://notes.nicolevanderhoeven.com/Obsidian+QuickAdd)
17.  Template | QuickAdd, accessed September 24, 2025, [https://quickadd.obsidian.guide/docs/Choices/TemplateChoice](https://quickadd.obsidian.guide/docs/Choices/TemplateChoice)
18.  QuickAdd pick from template and append title : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/1hw8f47/quickadd\_pick\_from\_template\_and\_append\_title/](https://www.reddit.com/r/ObsidianMD/comments/1hw8f47/quickadd_pick_from_template_and_append_title/)
19.  Format syntax | QuickAdd, accessed September 24, 2025, [https://quickadd.obsidian.guide/docs/FormatSyntax](https://quickadd.obsidian.guide/docs/FormatSyntax)
20.  Capture | QuickAdd, accessed September 24, 2025, [https://quickadd.obsidian.guide/docs/Choices/CaptureChoice](https://quickadd.obsidian.guide/docs/Choices/CaptureChoice)
21.  QuickAdd Macro: Showing a list of files to Capture automatically - Obsidian Forum, accessed September 24, 2025, [https://forum.obsidian.md/t/quickadd-macro-showing-a-list-of-files-to-capture-automatically/41185](https://forum.obsidian.md/t/quickadd-macro-showing-a-list-of-files-to-capture-automatically/41185)
22.  Quick add workflow (into daily notes) using QuickAdd, Advanced ..., accessed September 24, 2025, [https://forum.obsidian.md/t/quick-add-workflow-into-daily-notes-using-quickadd-advanced-uri-and-shortcuts-ios-and-macos/74664](https://forum.obsidian.md/t/quick-add-workflow-into-daily-notes-using-quickadd-advanced-uri-and-shortcuts-ios-and-macos/74664)
23.  Obsidian Quick add - YouTube, accessed September 24, 2025, [https://www.youtube.com/watch?v=s8wSP80Ha3A](https://www.youtube.com/watch?v=s8wSP80Ha3A)
24.  Macros | QuickAdd, accessed September 24, 2025, [https://quickadd.obsidian.guide/docs/Choices/MacroChoice](https://quickadd.obsidian.guide/docs/Choices/MacroChoice)
25.  QuickAdd Plugin - Share & showcase - Obsidian Forum, accessed September 24, 2025, [https://forum.obsidian.md/t/quickadd-plugin/20032](https://forum.obsidian.md/t/quickadd-plugin/20032)
26.  Multis | QuickAdd, accessed September 24, 2025, [https://quickadd.obsidian.guide/docs/Choices/MultiChoice](https://quickadd.obsidian.guide/docs/Choices/MultiChoice)
27.  Quick add : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/1e8o136/quick\_add/](https://www.reddit.com/r/ObsidianMD/comments/1e8o136/quick_add/)
28.  Combining QuickAdd and Buttons help. : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/1b2byt9/combining\_quickadd\_and\_buttons\_help/](https://www.reddit.com/r/ObsidianMD/comments/1b2byt9/combining_quickadd_and_buttons_help/)
29.  Hotkeys - Obsidian Help, accessed September 24, 2025, [https://help.obsidian.md/hotkeys](https://help.obsidian.md/hotkeys)
30.  way to quickly add tasks in obsidian. : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/1ee4wq4/way\_to\_quickly\_add\_tasks\_in\_obsidian/](https://www.reddit.com/r/ObsidianMD/comments/1ee4wq4/way_to_quickly_add_tasks_in_obsidian/)
31.  Global hotkey to launch Obsidian and open QuickAdd capture window using AutoHotKey script - Share & showcase, accessed September 24, 2025, [https://forum.obsidian.md/t/global-hotkey-to-launch-obsidian-and-open-quickadd-capture-window-using-autohotkey-script/22626](https://forum.obsidian.md/t/global-hotkey-to-launch-obsidian-and-open-quickadd-capture-window-using-autohotkey-script/22626)
32.  Open QuickAdd from your Desktop, accessed September 24, 2025, [https://quickadd.obsidian.guide/docs/Misc/AHK\_OpenQuickAddFromDesktop](https://quickadd.obsidian.guide/docs/Misc/AHK_OpenQuickAddFromDesktop)
33.  My Best Practices and Principles for Personal Knowledge Management (PKM) \[WIP\], accessed September 24, 2025, [https://anthonytd.com/pkm-best-practices/](https://anthonytd.com/pkm-best-practices/)