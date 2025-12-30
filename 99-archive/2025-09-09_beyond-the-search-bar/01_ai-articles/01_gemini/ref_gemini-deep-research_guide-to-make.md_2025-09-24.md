# A Comprehensive Guide to the Make.md Plugin for Obsidian

## Section 1: Introduction to Make.md - The Notion-like Powerhouse for Obsidian

In the ever-expanding universe of Obsidian plugins, few are as ambitious or transformative as Make.md. It is not merely a tool that adds a single function; it is a comprehensive system designed to fundamentally alter how users interact with their notes. By layering a visually rich, database-driven interface on top of Obsidian's local-first Markdown foundation, Make.md aims to deliver the organizational power of applications like Notion without sacrificing the principles of data ownership and portability that define the Obsidian experience. This guide provides an exhaustive analysis of the Make.md plugin, exploring its core philosophy, detailing its powerful features, and contextualizing its place within the broader ecosystem to help users determine if this powerhouse plugin is the right fit for their personal knowledge management system.

### 1.1 Defining Make.md: An "Organization and Personalization Engine"

Make.md is officially described as an "Organization and Personalization Engine for your notes," a plugin that "supercharges Obsidian" with features designed to create the "perfect system personalized for your workflow and tastes".1 Its primary value proposition is to bridge the gap between the raw, text-focused nature of vanilla Obsidian and the user-friendly, database-centric structure of modern productivity apps.3

At its core, the plugin introduces three major functional pillars:

1.  **Spaces:** A customizable alternative to the standard file explorer that allows for custom sorting, visual labeling with icons, and the creation of focused workspaces.6
2.  **Contexts:** A powerful database system that transforms collections of notes into structured tables, Kanban boards, calendars, and galleries, complete with relations, formulas, and rollups.2
3.  **Maker Mode (formerly Flow Editor):** A suite of tools that streamlines the Markdown editing process with inline styling toolbars and slash commands, moving Obsidian closer to a WYSIWYG (What You See Is What You Get) experience.6

Together, these features aim to provide a cohesive, all-in-one solution for users who desire a more structured, visual, and interactive way to manage their knowledge vault.

### 1.2 The Core Philosophy: Separating Knowledge from Structure

To understand Make.md, it is essential to grasp the two foundational design principles articulated by its developer. These principles directly address some of the most significant concerns within the Obsidian community, namely data purity and the fear of "plugin lock-in".10

*   **Principle 1: Markdown notes remain clean.** The plugin is architected to ensure that a user's knowledge—the content of their Markdown files—remains free of proprietary syntax or clutter.3 This stands in stark contrast to other powerful plugins like Dataview, which often require users to embed code-like queries directly into their notes. With Make.md, the complex logic for views and databases is stored separately, preserving the portability and readability of the core notes.
*   **Principle 2: Data remains portable.** All the structural and display information created by Make.md (such as the configuration of a Space or the layout of a database view) is stored in plain SQLite files within the vault's plugin directory.3 SQLite is an open, accessible format, meaning that even if a user uninstalls the plugin, the underlying data is not lost and can be accessed by other tools.

However, a critical distinction exists between technical data portability and practical workflow dependency. While the developer has ensured that the raw Markdown files are untouched and the plugin's data is stored in an open format, many users still perceive a significant risk of lock-in.4 This perception arises not from the fear of losing files, but from the potential loss of the intricate organizational system built with the plugin. A user might spend months creating complex dashboards, databases, and custom views. If they were to disable Make.md, their notes would remain, but the entire functional superstructure—the "parallel structure" that makes the vault usable—would vanish.11 Rebuilding this system with alternative tools would be a monumental task. Therefore, while there is no technical lock-in at the file level, the investment in building a workflow creates a powerful practical dependency that potential users must consider.

### 1.3 Who is Make.md For? Identifying the Ideal User Profile

The plugin's ambitious feature set makes it a compelling choice for specific types of users, while its complexity and performance characteristics may make it unsuitable for others.

Make.md is an excellent fit for:

*   **The Notion Migrant:** Users accustomed to Notion's powerful databases, visual page building, and integrated workflows will find Make.md to be the closest equivalent within the Obsidian ecosystem.3 It replicates much of Notion's core functionality while providing the benefits of local-first data ownership.
*   **The Visually-Oriented User:** Individuals who want to personalize their vault with icons, colors, banners, and custom dashboards without needing to write custom CSS will find the plugin's tools intuitive and powerful.7
*   **The "All-in-One" System Builder:** Users who prefer a single, cohesive plugin to handle file management, database organization, and editing will appreciate Make.md's integrated approach. It can replace the need to install, configure, and maintain a dozen separate, single-purpose plugins.13

Conversely, Make.md may not be the best choice for:

*   **Markdown Purists and Minimalists:** Users who value Obsidian for its simplicity and speed may find the plugin's extensive UI changes and feature set to be "bloated" and intrusive.4
*   **Users with Large Vaults or Performance Sensitivities:** The plugin has a well-documented history of performance issues, and users with tens of thousands of notes may experience significant slowdowns or instability.4

### 1.4 Installation and Initial Setup

Getting started with Make.md is straightforward. The process involves navigating to Obsidian's settings and installing it from the community plugins browser.

1.  Open Obsidian and go to Settings > Community plugins.
2.  Ensure that "Restricted mode" is turned off.
3.  Click Browse to open the community plugins list.
4.  Search for "MAKE.md" and click Install.
5.  Once installed, click Enable to activate the plugin.

Upon first activation, Make.md presents a "Welcome" guide that walks the user through its main features and concepts.10 It is highly recommended that new users immediately visit the plugin's settings pane. Here, the main components—Spaces, Contexts, and Maker Mode—can be individually enabled or disabled. For users concerned about performance, a prudent approach is to disable all but the most desired feature initially, and then enable others incrementally to gauge their impact on the vault's responsiveness.5

## Section 2: Deep Dive: The Three Pillars of Make.md

Make.md's functionality is built upon three core pillars that work in concert to transform the Obsidian experience. Understanding each of these components is key to leveraging the plugin's full potential.

### 2.1 Pillar I: 'Spaces' - Taming Your File Explorer

The 'Spaces' feature is a direct response to one of the common limitations of vanilla Obsidian: its rigid, alphabetically sorted file explorer. 'Spaces' provides a customizable, alternative file navigation pane designed to help users organize their vault around contexts and workflows rather than a strict folder hierarchy.6

#### Core Concept

'Spaces' acts as a visual layer over the existing file system. It allows users to create curated "workspaces" by pinning specific folders and notes, arranging them in any order, and adding visual cues like icons and colors.7 This enables a user to, for example, create a "Current Projects" space that shows only the three folders relevant to their immediate work, hiding the clutter of their broader archive.

#### Walkthrough: Building Your First Space

1.  **Creating a Space:** In the left sidebar, the Make.md plugin adds a new icon. Clicking this opens the Spaces view. A + button allows the creation of a new Space. The user can then give it a name (e.g., "Academic Research") and select an emoji or icon for quick identification.18
2.  **Adding Content:** The most intuitive way to populate a Space is to drag and drop folders and notes directly from Obsidian's default file explorer into the Space. This action does not move the actual files on the disk; it simply creates a link or "pin" within that specific Space's view.19
3.  **Custom Sorting:** Once items are in a Space, they can be manually reordered via drag-and-drop. A user can place their most important project folder at the top, followed by a specific note, and then another folder, regardless of their alphabetical order. This custom sorting is a key feature missing from the default file explorer.15
4.  **Visual Customization:** Right-clicking on any file or folder within a Space reveals a context menu that allows the user to assign a color or an emoji. This provides a powerful visual shorthand for identifying different types of content at a glance.7

#### Advanced Technique: "Smart Spaces"

Beyond manual curation, Make.md offers "Smart Spaces." These are dynamic collections that automatically populate based on user-defined filters, serving as a powerful, no-code alternative to writing complex Dataview queries. For instance, a user could create a Smart Space that automatically displays all notes containing the tag #pkb and where a property status is not done.21 This space would update in real-time as notes are tagged or their properties change.

#### Critical Analysis

While 'Spaces' is one of the plugin's most beloved features for bringing order to chaotic vaults 11, it is not without its problems. Community feedback frequently highlights that the feature can be "very slow and laggy when trying to create and edit spaces".11 Users have also reported instances where a Space fails to load its contents or becomes unresponsive, forcing them to revert to the standard file explorer and defeating the purpose of the feature.22

### 2.2 Pillar II: 'Contexts' - Building True Databases in Your Vault

The 'Contexts' feature is Make.md's answer to Notion's databases. It is the engine that transforms unstructured collections of Markdown notes into highly structured, queryable databases that can be visualized in multiple ways.7

#### Core Concept

A 'Context' defines a set of properties (fields, like Status, Due Date, Priority) for a specific collection of notes. This collection can be defined either by the folder the notes are in or by a tag they share. Once a context is established, these notes can be viewed and manipulated as entries in a database.23

#### Folder Contexts vs. Tag Contexts

Make.md provides two primary ways to define a collection of notes for a database:

*   **Folder Contexts:** This approach is ideal for self-contained sets of notes, such as a project, a collection of meeting minutes, or chapters of a book. Any note residing within the designated folder automatically becomes part of the database and inherits its properties.23
*   **Tag Contexts:** This method is better suited for organizing notes of the same _type_ that may be scattered across the entire vault. For example, a `#book `tag context can be used to create a comprehensive media library, pulling in book notes from various project and archive folders.23

#### Walkthrough: Creating a Project Database

1.  **Defining the Context:** Begin by creating a new folder named "Projects." In the 'Spaces' view, click on this folder. This will open the folder note. Within this view, there will be an option to create a new Context and associate it with the "Projects" folder.
2.  **Adding Properties:** Once the context is created, the user can define its structure by adding properties. For a project tracker, one might add:
    *   Status: A Select type property with options like "To Do," "In Progress," and "Done."
    *   DueDate: A Date type property to track deadlines.
    *   Priority: A Select type property with options like "High," "Medium," and "Low".19
3.  **Populating Data:** Now, any new note created inside the "Projects" folder will automatically be part of this database. The defined properties will appear at the top of the note (similar to Obsidian's core Properties view), ready to be filled in.
4.  **Creating Views:** The true power of Contexts lies in its multiple views. Within the "Projects" folder note view, the user can switch between different layouts:
    *   **Table View:** Displays all project notes in a familiar spreadsheet format, with each note as a row and each property as a column. Data can be sorted and filtered directly from the column headers.13
    *   **Board View:** Creates a Kanban board. By selecting the Status property as the grouping field, the view will automatically generate columns for "To Do," "In Progress," and "Done," with project notes appearing as cards that can be dragged between columns.13
    *   Other available views include Calendars (grouped by a date property) and Galleries (for visually-focused notes).

#### Advanced Technique: Relations, Formulas, and Rollups

Make.md's database capabilities extend to advanced features that enable complex system building, directly competing with Notion's functionality.1

*   **Relations:** This allows for the linking of entries between two different databases. For example, a "Projects" database can be related to a "Tasks" database, allowing a user to link specific tasks to each project and see these connections from either note.24
*   **Formulas and Rollups:** These features enable calculations and data aggregation. A user could create a rollup property in the "Projects" database that automatically calculates and displays the percentage of linked tasks that have been marked as "Done."

### 2.3 Pillar III: 'Maker Mode' & The Future 'Basics' Plugin

The third pillar of Make.md focuses on enhancing the core writing and editing experience, aiming to make Markdown more accessible and fluid for users who may not be comfortable with its syntax.6

#### Core Concept

'Maker Mode' (which subsumes the older 'Flow Editor' and 'Flow Styler' concepts) is a collection of UI enhancements that bring WYSIWYG-style editing to Obsidian.

#### Walkthrough: Streamlined Editing

1.  **Slash Command:** On any new line in the editor, typing a forward slash (/) invokes the 'Make Menu' (or 'Flow Menu'). This pop-up provides a searchable list of Markdown elements, allowing a user to quickly insert a callout, a table, or other formatted blocks without needing to remember the specific syntax.9
2.  **Inline Styler:** When text is selected, a small formatting toolbar appears, offering one-click options for applying bold, italics, highlights, and other common styles.9
3.  **Flow Blocks:** This feature transforms embedded notes (!\[\[Note\]\]) into editable blocks. Instead of seeing a static preview, the user can edit the content of the embedded note directly in place, without having to open it in a separate pane. This functionality was inspired by and is based on the popular 'Hover Editor' plugin.1

#### The 'Basics' Plugin Spinoff

In response to significant community feedback, the developer announced with the 1.0 release that these editing features would be spun off into a separate, standalone plugin called 'Basics'.10 This decision represents a pivotal strategic shift. A primary and persistent criticism of Make.md has been its monolithic, "all-in-one" nature, which many users find bloated.11 By separating the editing enhancements from the core organization and database engine, the developer directly addresses this complaint. This fragmentation allows users who only want the improved editing experience to install 'Basics' without the performance overhead of the full Make.md suite. It signals a potential move toward a more modular ecosystem, aligning better with the broader Obsidian philosophy and potentially widening the appeal of the developer's tools to a larger user base.

## Section 3: Make.md in the Obsidian Ecosystem: A Comparative Analysis

Make.md does not exist in a vacuum. To make an informed decision, a user must understand how its features, particularly its database functionality, compare to other prominent solutions within the Obsidian ecosystem. The two most important comparisons are with the core 'Bases' plugin and the community-favorite 'Dataview' plugin.

### 3.1 Make.md 'Contexts' vs. Obsidian 'Bases'

This is the most direct comparison, pitting the feature-rich community plugin against the new, officially supported core plugin. Both aim to provide a user-friendly, GUI-driven way to create databases from notes.

*   **Data Storage:** This is the fundamental architectural difference. 'Bases' works directly with Obsidian's native properties system, reading and writing all data to the YAML frontmatter of the Markdown files.25 'Contexts', in contrast, stores its view configurations and some metadata in a separate SQLite database file, which keeps the note frontmatter cleaner but introduces an external dependency that is specific to the plugin.3
*   **Feature Set:** As a more mature solution, Make.md's 'Contexts' currently offers a more advanced feature set. Crucially, it supports relations between databases and rollup fields for data aggregation, capabilities that are not yet present in 'Bases'.24
*   **Performance and Stability:** As a core plugin developed by the Obsidian team, 'Bases' is generally regarded as being faster, more lightweight, and more stable.14 Make.md has a reputation for being more resource-intensive and prone to bugs, particularly in large vaults.5
*   **Integration:** 'Bases' is designed to feel like a natural extension of the core Obsidian application. Make.md, on the other hand, introduces more significant UI changes, such as replacing the file explorer with 'Spaces', which some users find disruptive to their established workflows.14

### 3.2 Make.md 'Contexts' vs. 'Dataview'

This comparison is less about features and more about philosophy: a visual, no-code approach versus a powerful, code-driven one.

*   **Ease of Use:** Make.md is vastly more accessible to non-technical users. Its graphical interface for building queries and views is intuitive for anyone familiar with Notion.28 Dataview, conversely, has a steep learning curve, requiring users to learn its SQL-like Dataview Query Language (DQL) or, for maximum power, JavaScript (DataviewJS).14
*   **Flexibility and Power:** Dataview is unquestionably the more powerful and flexible tool. Its query language allows for the creation of highly specific and complex queries, aggregations, and custom visualizations that are simply not possible through Make.md's graphical interface.14
*   **Data Entry:** A key advantage of Make.md is that its views are interactive. Users can edit properties directly within a table view, just like in a spreadsheet.13 Dataview is primarily a tool for  
    _displaying_ data; to edit a property, the user must navigate to the source note and change it there.
*   **Note "Pollution":** As mentioned previously, Dataview queries are embedded within Markdown code blocks in notes. Some users feel this "pollutes" their notes with non-content syntax, which runs counter to the principle of clean, portable knowledge files.10 Make.md's design philosophy explicitly avoids this by storing view configurations separately.

### 3.3 The All-in-One vs. Modular Approach

Ultimately, the choice between Make.md and a combination of other plugins reflects a fundamental preference in workflow design.

*   **The Make.md Approach:** Offers a single, integrated suite where all components are designed to work together seamlessly. This can reduce the friction of finding, installing, and maintaining multiple plugins and ensures a consistent user experience.13
*   **The Modular Approach:** Involves curating a collection of smaller, single-purpose plugins to achieve a similar outcome (e.g., using 'Bases' for databases, 'Iconize' for file icons, and 'Folder Note' for folder dashboards). This approach grants the user greater control, often results in better performance, and avoids the "feature bloat" of a monolithic plugin. Many experienced Obsidian users explicitly state their preference for this modularity, finding that standalone plugins are often more powerful and customizable for their specific function.5

### Table: Database Plugin Feature Comparison

To summarize the key differences, the following table provides an at-a-glance comparison of the three primary database solutions in Obsidian.

| Feature | Make.md 'Contexts' | Obsidian 'Bases' (Core) | Dataview (Community) |
| --- | --- | --- | --- |
| Ease of Use | GUI-driven, Notion-like | GUI-driven, simple setup | Requires learning DQL/JS |
| Primary Data Source | SQLite database file | Note Properties (Frontmatter) | Note Properties & Inline Fields |
| Core Functionality | Views, Relations, Formulas, Rollups | Views, Formulas, Sorting, Filtering | Complex Queries, Aggregation, JS API |
| Performance | Mixed reports, can be slow in large vaults | Generally fast and stable | Can be slow on very complex queries |
| Data Portability | Notes are clean; structural data is in SQLite | Excellent; all data is in Markdown frontmatter | Excellent; all data is in Markdown files |
| Best For | Visual users wanting an all-in-one, Notion-like experience with powerful database features without code. | Users wanting simple, fast, and officially supported database views that integrate cleanly with core Obsidian. | Power users and developers needing maximum query flexibility, custom scripting, and fine-grained control. |

## Section 4: The Community Verdict: Performance, Stability, and Practical Realities

While the feature list of Make.md is impressive, its practical implementation has been a subject of intense discussion within the Obsidian community. A comprehensive understanding of the plugin requires addressing the most common and significant user-reported issues.

### 4.1 Addressing the Performance Elephant in the Room

The most frequently cited criticism of Make.md is its impact on performance. Across Reddit and the official Obsidian forums, user reports consistently describe the plugin as "slow and laggy" 11, noting long startup times 5 and instances of the application freezing, particularly in vaults with a large number of notes.15

These performance issues are not merely isolated bugs but are likely an inherent consequence of the plugin's ambitious scope. Obsidian is fundamentally a fast, file-based application. Make.md layers a complex, database-driven user interface on top of this foundation. Features like the 'Spaces' custom file explorer, real-time database views in 'Contexts', and constant file indexing require significant computational resources.1 This creates an unavoidable performance overhead. Users seeking Notion-level functionality within Obsidian must be prepared for a potential trade-off in speed and responsiveness. The expectation of getting a feature-rich graphical interface for free in terms of performance is unrealistic; the added functionality comes at a computational cost.

### 4.2 Navigating the Bugs and Stability Concerns

Beyond general slowness, users have reported a variety of specific bugs and stability issues that can disrupt workflows. Common complaints include:

*   'Spaces' views failing to load or becoming completely unresponsive, forcing a return to the default file explorer.22
*   'Contexts' and their associated properties failing to update in real-time or behaving unreliably, especially with select/multi-select fields.11
*   Incompatibilities with other popular community plugins, such as Linter, or conflicts with core Obsidian behaviors like tag parsing.5
*   Past issues with sync services that could lead to data duplication or merge conflicts, although the developer has stated that these have been improved.11

It is important to note that the developer is known to be active and highly responsive to feedback, frequently pushing updates to address these problems.5 However, the sheer complexity of the plugin means that it can feel less stable than simpler, single-purpose alternatives, leading some users to conclude that it is not yet ready for "heavy use" in mission-critical workflows.22

### 4.3 Is Make.md Safe? Debunking Myths and Clarifying Risks

Concerns about the plugin's safety generally fall into two categories: data lock-in and data corruption. As established, the fear of data lock-in stems from workflow dependency rather than file incompatibility. Your Markdown notes themselves are safe.3

The risk of data corruption, while low, is non-zero. Some users have reported that uninstalling the plugin has inadvertently messed up their file and folder structures.4 While the developer's intent is for the plugin to be non-destructive, its deep integration with the vault's structure means that bugs can have unintended consequences.

The consensus is that Make.md is "safe" in that it is a well-known, open-source plugin from a reputable developer and contains no malicious code.4 However, its complexity and history of bugs mean it carries a higher intrinsic risk of causing unintended issues in a vault compared to simpler plugins. Therefore, users should proceed with caution and follow best practices for data protection.14

## Section 5: Conclusion and Actionable Recommendations

Make.md stands as one of the most ambitious and powerful plugins in the Obsidian ecosystem. It successfully brings a Notion-like experience of visual organization and structured databases to a local-first, Markdown-based environment. However, this power comes at a cost, and potential users must weigh the benefits against well-documented drawbacks in performance and stability.

### 5.1 Final Verdict: Is Make.md Worth Installing?

There is no simple answer. The value of Make.md is entirely dependent on a user's individual priorities and tolerance for its trade-offs. For some, it is a "fantastic" and "core" part of their workflow that finally makes Obsidian usable for their needs.11 For others, it is a plugin that is "cool in concept but not so much in execution," ultimately uninstalled in favor of more lightweight, modular alternatives.5

Make.md is likely worth installing if:

*   You are migrating from Notion and want to replicate its database and workspace features as closely as possible.
*   You prioritize a visual, graphical interface for managing your notes and are willing to accept a potential performance hit.
*   You prefer an all-in-one, integrated system over curating and maintaining multiple specialized plugins.

It may not be the right choice if:

*   You prioritize speed, simplicity, and a minimalist writing environment.
*   You have a very large vault and are sensitive to application startup times and UI lag.
*   You are a power user who prefers the ultimate flexibility of code-based tools like Dataview.

### 5.2 Roadmap for New Users: A 4-Step Safety Protocol

For those who decide that Make.md's features align with their goals, approaching its implementation with caution is paramount. Following a structured protocol can significantly mitigate the risks discussed throughout this guide.

1.  **Rule #1: Test in a Sandbox Vault.** This is the single most critical step. Before installing Make.md in your primary vault, create a complete copy of your vault or a new, separate test vault. Experiment with the plugin's features in this safe environment to assess its performance and stability with your data and workflows. This prevents any potential bugs from affecting your critical information.4
2.  **Start Incrementally.** Do not enable all of the plugin's features at once. In the settings, begin by enabling only 'Spaces'. Use it for a few days to see how it performs. If satisfied, enable 'Contexts'. This gradual approach helps in identifying which specific feature might be causing performance bottlenecks and makes the learning curve more manageable.
3.  **Backup Your Vault Religiously.** This is a golden rule for any complex Obsidian setup, but it is especially true with Make.md. Implement a robust backup strategy. This could involve using a cloud sync service with version history (like Obsidian Sync or Dropbox) or, for more advanced users, setting up a version control system like Git.31 Regular backups ensure that you can always revert to a stable state if the plugin causes any unforeseen issues.
4.  **Engage with the Community.** The official Make.md Discord server is an invaluable resource. It is highly active, and the developer is often present to answer questions and provide support.10 If you encounter a problem or have a question about a specific workflow, this is the best place to get timely and accurate help from both the developer and the experienced user community.

### 5.3 Final Thoughts: The Future of Make.md in a Maturing Obsidian Ecosystem

Make.md remains a pioneering project that continues to push the boundaries of what is possible within Obsidian. With the recent introduction of the core 'Bases' plugin, it faces its first piece of official competition, which will likely spur further innovation. The strategic decision to spin off the 'Basics' plugin suggests a move towards a more modular and flexible future, which could address the community's primary criticisms.

Ultimately, Make.md's enduring value lies in its role as a bridge. It connects users who need the security and longevity of local-first Markdown with the user-friendly, powerful interfaces of modern, database-centric applications. Despite its imperfections, it offers a compelling vision for a more structured and personalized future for personal knowledge management in Obsidian.

#### Works cited

1.  Make-md/makemd - GitHub, accessed September 24, 2025, [https://github.com/Make-md/makemd](https://github.com/Make-md/makemd)
2.  make.md, accessed September 24, 2025, [https://www.make.md/](https://www.make.md/)
3.  How do you transition away from Make.md? : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/1b5krnq/how\_do\_you\_transition\_away\_from\_makemd/](https://www.reddit.com/r/ObsidianMD/comments/1b5krnq/how_do_you_transition_away_from_makemd/)
4.  Is the make.md plugin safe? : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/1ioqttb/is\_the\_makemd\_plugin\_safe/](https://www.reddit.com/r/ObsidianMD/comments/1ioqttb/is_the_makemd_plugin_safe/)
5.  What's your thoughts on Make.MD plugin? : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/1ghg2k7/whats\_your\_thoughts\_on\_makemd\_plugin/](https://www.reddit.com/r/ObsidianMD/comments/1ghg2k7/whats_your_thoughts_on_makemd_plugin/)
6.  make-md - Obsidian Hub, accessed September 24, 2025, [https://publish.obsidian.md/hub/02+-+Community+Expansions/02.05+All+Community+Expansions/Plugins/make-md](https://publish.obsidian.md/hub/02+-+Community+Expansions/02.05+All+Community+Expansions/Plugins/make-md)
7.  Getting Started - make.md, accessed September 24, 2025, [https://www.make.md/docs/Getting%20Started](https://www.make.md/docs/Getting%20Started)
8.  MAKE.md - Obsidian Stats, accessed September 24, 2025, [https://www.obsidianstats.com/plugins/make-md](https://www.obsidianstats.com/plugins/make-md)
9.  Make-md/Obsidian-Basics: Basics for Markdown editing in ... - GitHub, accessed September 24, 2025, [https://github.com/Make-md/Obsidian-Basics](https://github.com/Make-md/Obsidian-Basics)
10.  Make.md 1.0 is now available, organization and personalization for Obsidian inspired by Notion : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/1hmdsf6/makemd\_10\_is\_now\_available\_organization\_and/](https://www.reddit.com/r/ObsidianMD/comments/1hmdsf6/makemd_10_is_now_available_organization_and/)
11.  Make.md : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/12prhi0/makemd/](https://www.reddit.com/r/ObsidianMD/comments/12prhi0/makemd/)
12.  Thoughts on Make.MD? : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/14yjvxa/thoughts\_on\_makemd/](https://www.reddit.com/r/ObsidianMD/comments/14yjvxa/thoughts_on_makemd/)
13.  This browser extension completely changed how I use Obsidian - XDA Developers, accessed September 24, 2025, [https://www.xda-developers.com/browser-extension-completely-changed-how-i-use-obsidian/](https://www.xda-developers.com/browser-extension-completely-changed-how-i-use-obsidian/)
14.  Bases VS Dataview VS Make.md : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/1n3yo5p/bases\_vs\_dataview\_vs\_makemd/](https://www.reddit.com/r/ObsidianMD/comments/1n3yo5p/bases_vs_dataview_vs_makemd/)
15.  Make "Spaces" by Make.md a separate plugin or develop another one with the same functions, but fast and lightweight - Obsidian Forum, accessed September 24, 2025, [https://forum.obsidian.md/t/make-spaces-by-make-md-a-separate-plugin-or-develop-another-one-with-the-same-functions-but-fast-and-lightweight/93901](https://forum.obsidian.md/t/make-spaces-by-make-md-a-separate-plugin-or-develop-another-one-with-the-same-functions-but-fast-and-lightweight/93901)
16.  Alternative to Make.md - Help - Obsidian Forum, accessed September 24, 2025, [https://forum.obsidian.md/t/alternative-to-make-md/89147](https://forum.obsidian.md/t/alternative-to-make-md/89147)
17.  Plugin similar to MAKE.md Spaces? : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/11t2tha/plugin\_similar\_to\_makemd\_spaces/](https://www.reddit.com/r/ObsidianMD/comments/11t2tha/plugin_similar_to_makemd_spaces/)
18.  Make.md - spaces - Help - Obsidian Forum, accessed September 24, 2025, [https://forum.obsidian.md/t/make-md-spaces/96446](https://forum.obsidian.md/t/make-md-spaces/96446)
19.  Make.md Plugin - John's Digital Galaxy - John Mavrick, accessed September 24, 2025, [https://notes.johnmavrick.com/USV/Make.md+Plugin](https://notes.johnmavrick.com/USV/Make.md+Plugin)
20.  Make.md or not? Alternative plugins to recreate functions? : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/1lt7wux/makemd\_or\_not\_alternative\_plugins\_to\_recreate/](https://www.reddit.com/r/ObsidianMD/comments/1lt7wux/makemd_or_not_alternative_plugins_to_recreate/)
21.  Make.md has been updated! : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/12nt6qv/makemd\_has\_been\_updated/](https://www.reddit.com/r/ObsidianMD/comments/12nt6qv/makemd_has_been_updated/)
22.  MAKE.md - Help - Obsidian Forum, accessed September 24, 2025, [https://forum.obsidian.md/t/make-md/55662](https://forum.obsidian.md/t/make-md/55662)
23.  Lists and Databases - make.md, accessed September 24, 2025, [https://www.make.md/docs/Getting%20Started/Lists%20and%20Databases](https://www.make.md/docs/Getting%20Started/Lists%20and%20Databases)
24.  Obsidian Make.md Plugin - Database Relation - Offline Notion Alternative - YouTube, accessed September 24, 2025, [https://www.youtube.com/watch?v=kuC3Xd7k6lU](https://www.youtube.com/watch?v=kuC3Xd7k6lU)
25.  Bases v Make - Knowledge management - Obsidian Forum, accessed September 24, 2025, [https://forum.obsidian.md/t/bases-v-make/104579](https://forum.obsidian.md/t/bases-v-make/104579)
26.  Introduction to Bases - Obsidian Help, accessed September 24, 2025, [https://help.obsidian.md/bases](https://help.obsidian.md/bases)
27.  Obsidian Bases: Obsidian's Biggest Upgrade (Complete Guide) - YouTube, accessed September 24, 2025, [https://www.youtube.com/watch?v=9Yt52zJIIG0](https://www.youtube.com/watch?v=9Yt52zJIIG0)
28.  Dataview-like GUI that renders to markdown or code block - Obsidian Forum, accessed September 24, 2025, [https://forum.obsidian.md/t/dataview-like-gui-that-renders-to-markdown-or-code-block/32709](https://forum.obsidian.md/t/dataview-like-gui-that-renders-to-markdown-or-code-block/32709)
29.  blacksmithgu/obsidian-dataview: A data index and query language over Markdown files, for https://obsidian.md - GitHub, accessed September 24, 2025, [https://github.com/blacksmithgu/obsidian-dataview](https://github.com/blacksmithgu/obsidian-dataview)
30.  Does MAKE.md work? : r/ObsidianMD - Reddit, accessed September 24, 2025, [https://www.reddit.com/r/ObsidianMD/comments/1k8w12x/does\_makemd\_work/](https://www.reddit.com/r/ObsidianMD/comments/1k8w12x/does_makemd_work/)
31.  The Easiest Way to Setup Obsidian Git (to backup notes) - Share & showcase, accessed September 24, 2025, [https://forum.obsidian.md/t/the-easiest-way-to-setup-obsidian-git-to-backup-notes/51429](https://forum.obsidian.md/t/the-easiest-way-to-setup-obsidian-git-to-backup-notes/51429)
32.  The Best Beginner Friendly Obsidian Plugin - Make.md Tutorial - YouTube, accessed September 24, 2025, [https://www.youtube.com/watch?v=ISpII6nsego](https://www.youtube.com/watch?v=ISpII6nsego)