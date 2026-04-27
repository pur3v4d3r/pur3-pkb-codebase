tags: [pkb-maintenance, data-hygiene, prompt-engineering, obsidian-structure] created: 2025-12-30 status: evergreen certainty: confident

🛡️ Repository Cleanup & Hygiene Strategy

1. Analysis of Current "Bloat" Factors

Based on the directory structure provided (structure_2025-12-30...), your prompt-engineering-2025 repository is suffering from "dump-site syndrome." This occurs when GitHub repositories are cloned indiscriminately into a PKB without sanitization.

The 6GB Weight Calculation

Text files (Markdown, Code) are negligible in size. A 6GB folder size typically indicates three specific culprits:

Hidden .git History: If you cloned generative-ai-for-beginners or similar repos, the hidden .git folder contains the entire version history of that project. This is often hundreds of megabytes per repo.

Uncompressed Media Assets: The file list shows images/01-lesson-banner.png (700KB). Educational repos are notoriously heavy with high-res PNGs and sometimes video files for tutorials.

Dependency Locking: node_modules or site-packages if any code was installed.

2. The Pruning Taxonomy

The accompanying python script (repo_pruner.py) uses a Quarantine-First methodology. We do not delete; we displace. This preserves data integrity while immediately solving the clutter issue.

A. dev_bloat_and_repos

Target: _generative-ai-for-beginners-main, .git, node_modules.

Rationale: These are structural artifacts, not knowledge artifacts. A PKB needs the content of a prompt, not the React framework used to build the dashboard that displays the prompt.

Action: Move entire subdirectory trees.

B. media_assets

Target: *.png, *.jpg, *.mp4.

Rationale: In a text-first Prompt Engineering PKB, images are often secondary. Unless an image is a diagram of a transformer architecture, it is noise.

Action: Move files while mirroring the folder structure, so you can re-link them later if specific images prove critical.

C. bulk_generated_clutter

Target: Personalized Home Maintenance..., Subscription-Based....

Rationale: The snippet reveals a flood of similarly named files (4KB each). This suggests a programmatic output or a "dataset" of prompts rather than curated notes. These flood the file explorer and destroy search relevance.

Action: Aggregate these into a single archive folder.

3. Post-Pruning Structure Recommendations

Once the script has run, your remaining directory should be primarily .md and .txt files. Here is how to restructure them for an Obsidian-based PKB:

📂 Recommended Folder Hierarchy

Prompt-Engineering-PKB/
├── 00_Meta/
│   ├── Templates/
│   └── Tags/
├── 10_Core_Concepts/        <-- "What is Few-Shot?", "Chain of Density"
├── 20_Prompt_Patterns/      <-- The actual prompts, categorized
│   ├── Coding/
│   ├── Creative_Writing/
│   └── System_Architecture/
├── 30_References/           <-- Academic papers, documentation
└── 99_Archive/              <-- The destination of the cleanup script
    ├── media_assets/
    ├── dev_bloat/
    └── bulk_clutter/


🧠 Knowledge Graph Integration Strategy

After pruning, use Dataview to dynamically organize the remaining prompts without moving them physically. Add YAML frontmatter to the cleaned files:

---
type: prompt
domain: coding
model: gpt-4
utility: high
---


Then, creates a "Map of Content" (MOC) using this query:

TABLE without id file.link as "Prompt", domain, model
FROM "20_Prompt_Patterns"
WHERE type = "prompt"
SORT file.name ASC


4. Next Steps for the User

Configure: Open repo_pruner.py and ensure SOURCE_DIR points to your actual folder path.

Dry Run: Run the script as-is (default is dry_run=True). Check the console output to see what would happen.

Execute: Change dry_run=False and run again.

Verify: Check the _quarantine folder. If the prompt-engineering folder size has dropped significantly (it should), you can delete the quarantine folder or move it to external cold storage.

🔗 Related Topics for PKB Expansion

[[Algorithmic File Organization]]

Connection: Automating file management via Python scripts.

Depth Potential: Writing scripts to auto-tag files based on content using NLP.

Knowledge Graph Role: Methodology > Automation.

[[Obsidian Dataview Architecture]]

Connection: How to view your files once they are cleaned.

Depth Potential: Advanced JavaScript queries for vault statistics.

Knowledge Graph Role: Tools > Obsidian.

[[Git-Based Knowledge Versioning]]

Connection: Alternatives to keeping .git folders inside the vault (using git submodules).

Depth Potential: Managing knowledge graphs as software repositories.

Knowledge Graph Role: Methodology > Version Control.

[[Prompt Engineering Taxonomies]]

Connection: How to name the files you kept (CO-STAR, RTF frameworks).

Depth Potential: Theoretical frameworks for prompt categorization.

Knowledge Graph Role: Theory > Taxonomy.