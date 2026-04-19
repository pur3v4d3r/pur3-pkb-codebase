---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Excalidraw"
aliases:
  - "Excalidraw"
type: permanent-note
status: evergreen
confidence: medium

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
  - permanent-note
  - evergreen
  - other
  - type/reference
  - source/claude-sonnet
  - maturity/needs-review
  - confidence/speculative
  - status/not-read
  - priority/low
  - year/2025
  - pkm/research
  - informational-design-pkm
  - pkm/workflow

domain: other
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-04-01
updated: 2026-04-18

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "reference-comprehensive-excalidraw-and-markmind-2025121812"
evidence-quality: medium
extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"
pipeline-version: "2.1.0"
extraction-date: "2026-04-01"

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
complexity-level: intermediate
depth-level: comprehensive

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  []

related:
  []

broader:
  []

narrower:
  []

see-also:
  - "[[Obsidian]]"
  - "[[Visual-Thinking|Visual Thinking]]"
  - "[[Knowledge-Visualization|Knowledge Visualization]]"
  - "[[Mind-Mapping|Mind Mapping]]"
  - "[[PKM]]"
  - "[[Obsidian-Basics|Obsidian Basics]]"
  - "[[Community-Plugins|Community Plugins]]"
  - "[[Markdown-Fundamentals|Markdown Fundamentals]]"
  - "[[MarkMind]]"
  - "[[Zsolt-Viczian|Zsolt Viczian]]"
  - "[[ExcaliBrain]]"
  - "[[Visual-PKM|Visual PKM]]"
  - "[[Markdown]]"
  - "[[LaTeX]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  []

enables:
  []

expansion-topics:
  []

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: medium
---

# Excalidraw

> [!definition] **Excalidraw** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> [**Excalidraw**:: A powerful yet intuitive sketching tool seamlessly integrated into [[Obsidian]], enabling creation of hand-drawn style diagrams, sketches, UI wireframes, concept maps, and visual annotations directly within your vault.]^established-stable

## Core Explanation

> [!analytical-insight] Key Insight *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> [**Visual-Thinking-Accessibility**:: Excalidraw removes the "I'm not artistic" barrier by providing hand-drawn aesthetics automatically—rough, sketch-like appearance makes imperfect drawings look intentional rather than amateur.]^established

> [!analytical-insight] Key Insight *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> [**Excalidraw-Integration-Philosophy**:: The plugin's power comes not from drawing capabilities alone, but from deep integration with [[Obsidian]]'s linking and embedding system—enabling true [[Visual-PKM]] rather than isolated sketches.]^verified-stable

## Practical Implications

> [!example] **Application**
> *Describe how this concept applies in practice.*

> [!warning] **Key Distinction** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> ExcalidrawAutomate is powerful but has a learning curve. Start with Script Library's pre-built scripts before writing custom automation. Reserve for genuinely repetitive tasks—manual drawing is often faster for one-offs.

> [!warning] **Key Distinction** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> <span style='color: #FF00DC;'>**Critical**</span>: PDF annotation features require <span style='color: #72FFF1;'>Obsidian v1.4</span>. For v1.5+, use standalone MarkMind software that integrates with Obsidian plugin. Check compatibility before relying on PDF features.

> [!warning] **Key Distinction** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> <span style='color: #FF00DC;'>**Problem**</span>: "PDF won't open in reader"
> 
> <span style='color: #27FF00;'>**Solutions**</span>:
> - Triple-check PDF.js path (must include `/web/viewer.html`)
> - Verify Obsidian version (v1.4 required for plugin)
> - Check if native Obsidian PDF reader conflicts—disable it in settings
> - Try restarting Obsidian after configuration

> [!warning] **Key Distinction** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> **Next Review**: `= this.next-review` | **Review Count**: `= this.review-count`
> **Review Status**: `= choice(this.next-review < date(today), "🔴 OVERDUE", choice(this.next-review = date(today), "🟡 Due Today", choice(dateformat(this.next-review, "yyyy-MM-dd") <= dateformat(date(today) + dur(7 days), "yyyy-MM-dd"), "🟢 This Week", "⚪ Scheduled")))`
> **Days Until Review**: `= choice(this.next-review, (this.next-review - date(today)).days + " days", "Not scheduled")`

## Concrete Examples

> [!example] **LaTeX in Excalidraw** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> Type mathematical expressions using standard LaTeX syntax:
> ```
> $$\frac{-b \pm \sqrt{b^2-4ac}}{2a}$$
> ```
> Renders as formatted equation within your drawing.

> [!example] **Common Template Types** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> - **Daily visual journal** (date header, reflection frame, mood tracker)
> - **Meeting sketch notes** (attendees box, topics frame, action items)
> - **Concept exploration** (central idea circle, relationship arrows, evidence boxes)
> - **UI wireframe** (device frame, standard component library)
> - **System diagram** (layers frame, legend, connection key)

> [!example] **Frame Workflow** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> **Slide Show Method:**
> 1. Create frames sized 16:9 for each "slide"
> 2. Name frames: `Slide 01: Introduction`, `Slide 02: Main Concept`
> 3. Use "Slideshow" feature to present sequentially
> 4. Export as PDF with frame breaks for sharing
> 
> Result: Presentation lives in vault, fully linked to notes.

> [!example] **Boundary Use Case** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> **Project Planning Mind Map:**
> - Boundary 1: "Research Phase" (groups all research-related nodes)
> - Boundary 2: "Development Phase" (groups development nodes)
> - Boundary 3: "Testing Phase" (groups QA nodes)
> 
> Visual grouping makes phase transitions obvious at a glance.

## Connections & Context

**Related concepts:**
[[Obsidian]] · [[Visual-Thinking|Visual Thinking]] · [[Knowledge-Visualization|Knowledge Visualization]] · [[Mind-Mapping|Mind Mapping]] · [[PKM]] · [[Obsidian-Basics|Obsidian Basics]] · [[Community-Plugins|Community Plugins]] · [[Markdown-Fundamentals|Markdown Fundamentals]] · [[Obsidian]] · [[MarkMind]] · [[Visual-Thinking|Visual Thinking]] · [[PKM]] · [[Obsidian]] · [[Zsolt-Viczian|Zsolt Viczian]] · [[ExcaliBrain]] · [[Visual-PKM|Visual PKM]] · [[Obsidian]] · [[Markdown]] · [[LaTeX]] · [[Obsidian]] · [[Visual-PKM|Visual PKM]] · [[Note-Name|Note Name]] · [[Note-Name|Note Name]] · [[wiki-links]] · [[Obsidian]] · [[Templater]] · [[QuickAdd]] · [[JavaScript-Basics|JavaScript Basics]] · [[Related-Note|Related Note]]

**Related concepts** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*:
[[Visual-Thinking|Visual Thinking]] * [[Knowledge-Visualization|Knowledge Visualization]] * [[Mind-Mapping|Mind Mapping]] * [[Obsidian-Basics|Obsidian Basics]] * [[Community-Plugins|Community Plugins]] * [[Markdown-Fundamentals|Markdown Fundamentals]] * [[Zsolt-Viczian|Zsolt Viczian]] * [[Visual-PKM|Visual PKM]] * [[Note-Name|Note Name]] * [[JavaScript-Basics|JavaScript Basics]] * [[Related-Note|Related Note]] * [[Domain|Domain]] * [[Subtopic-A|Subtopic A]] * [[Subtopic-B|Subtopic B]] * [[Concept-Name|Concept Name]] * [[Related-Concept|Related Concept]] * [[Task-1|Task 1]] * [[Task-2|Task 2]] * [[Task-3|Task 3]] * [[Tasks|Tasks]] * [[outlining|outlining]] * [[PDF-annotation|PDF annotation]] * [[PDF-Name|PDF Name]] * [[Paper-Title|Paper Title]] * [[Established-Theory|Established Theory]] * [[Project-Name|Project Name]] * [[Design-Specs|Design Specs]] * [[Figma-Files|Figma Files]] * [[Person-A|Person A]] * [[Person-B|Person B]]

**Related concepts** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*:
[[Visual-Thinking|Visual Thinking]] * [[Knowledge-Visualization|Knowledge Visualization]] * [[Mind-Mapping|Mind Mapping]] * [[Obsidian-Basics|Obsidian Basics]] * [[Community-Plugins|Community Plugins]] * [[Markdown-Fundamentals|Markdown Fundamentals]] * [[Zsolt-Viczian|Zsolt Viczian]] * [[Visual-PKM|Visual PKM]] * [[Note-Name|Note Name]] * [[JavaScript-Basics|JavaScript Basics]] * [[Related-Note|Related Note]] * [[Subtopic-A|Subtopic A]] * [[Subtopic-B|Subtopic B]] * [[Concept-Name|Concept Name]] * [[Related-Concept|Related Concept]] * [[Task-1|Task 1]] * [[Task-2|Task 2]] * [[Task-3|Task 3]] * [[PDF-annotation|PDF annotation]] * [[PDF-Name|PDF Name]] * [[Paper-Title|Paper Title]] * [[Established-Theory|Established Theory]] * [[Project-Name|Project Name]] * [[Design-Specs|Design Specs]] * [[Figma-Files|Figma Files]] * [[Person-A|Person A]] * [[Person-B|Person B]] * [[Person-C|Person C]] * [[PDF++|PDF++]] * [[System-Architecture-Mindmap|System Architecture Mindmap]]



## Methodology Notes

> [!methodology-and-sources] **Initial Settings Configuration** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> **Basic Settings Tab:**
> - **Default Folder**: Set dedicated folder (e.g., `Drawings/` or `Excalidraw/`)
> - **Template**: Create a template with your default styles (stroke width, colors, fonts)
> - **Filename Prefix/Suffix**: Organize drawings systematically
> 
> **Saving Tab:**
> - **Autosave**: Enable with 10-15 second interval
> - **Compression**: Keep enabled for vault size management
> 
> **Embed & Export Tab:**
> - **Auto-export**: Enable PNG/SVG export for markdown embedding
> - **Dark/Light Mode**: Generate both versions if you switch themes
> - **Image Type**: SVG for scalability, PNG for…

> [!methodology-and-sources] **Linking Workflow Pattern** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> **Typical Linking Workflow:**
> 1. **Create drawing** with visual concepts
> 2. **Add text elements** with `[[wiki-links]]` to related notes
> 3. **Embed key notes** using `![[]]` syntax for context
> 4. **Use frames** to organize sections
> 5. **Create block references** for granular connections
> 6. **Embed drawing** in MOCs or concept notes for navigation

> [!methodology-and-sources] **Basic Scripting Pattern** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> ```javascript
> // Initialize
> const ea = ExcalidrawAutomate;
> ea.reset();
> 
> // Configure styling
> ea.style.strokeColor = "red";
> ea.style.strokeWidth = 2;
> 
> // Add elements
> ea.addRect(-150, -50, 450, 300);
> ea.addText(-100, 70, "My Text");
> ea.addArrow([[-100,100], [100,100]]);
> 
> // Render
> await ea.create();
> ```

> [!methodology-and-sources] **Concept Sketching Process** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> **Phase 1: Capture** (5-10 min)
> - Create blank Excalidraw: "[[Concept-Name]] Sketch"
> - Central shape: Write concept name
> - Free-form brainstorm: Add surrounding ideas rapidly
> - No organization yet—pure ideation
> 
> **Phase 2: Structure** (10-15 min)
> - Group related ideas into frames
> - Draw relationship arrows with labels
> - Add color coding for categories
> - Link to existing notes: `[[Related-Concept]]`
> 
> **Phase 3: Elaborate** (15-20 min)
> - Add explanatory text elements
> - Embed supporting evidence: `![[Research-Note]]`
> - Insert images/diagrams for context
> - Create sticky notes for…

> [!methodology-and-sources] **Initial Settings** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> **Basic Tab:**
> - **Canvas Size**: Set to maximum for large mind maps
> - **Auto-save**: Enable (default 5 seconds)
> - **Default Mode**: Choose "Basic" (free) or "Rich" (paid/Catalyst)
> 
> **Display Tab:**
> - **Theme**: Match Obsidian theme or use custom
> - **Node Style**: Rounded, rectangular, or custom
> - **Layout Algorithm**: Mindmap, Tree, Outline
> 
> **PDF Annotation Tab** (if using):
> - **Storage Type**: `.annos` (JSON) or `.md` (markdown)
> - **PDF.js Path**: Required for PDF viewing—follow setup instructions
> - **Auto-create Links**: Enable for automatic reference creation

> [!methodology-and-sources] **Outline Workflow** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> **Typical Use Pattern:**
> 1. **Capture** ideas rapidly in outline mode (keyboard-driven)
> 2. **Switch** to mind map view for visual analysis
> 3. **Reorganize** using drag-drop in visual mode
> 4. **Return** to outline for export or continued capture
> 
> Best of both: speed of text, power of visual.

> [!methodology-and-sources] **Research Annotation Process** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> **Phase 1: Initial Read & Highlight**
> 1. **Open PDF** in MarkMind reader
> 2. **Highlight** key passages (select text → highlight)
> 3. **Add comments** to highlights (right-click → add comment)
> 4. **Tag sections** with categories
> 
> **Phase 2: Link to Mind Map**
> 1. **Open mind map** (or create new)
> 2. **Create node** for concept from PDF
> 3. **Link annotation**: Right-click node → "Link PDF annotation"
> 4. **Select annotation** from list
> 5. **Bidirectional connection** established
> 
> **Phase 3: Synthesis**
> 6. **Organize** linked nodes in mind map structure
> 7. **Add boundaries** around themes
> 8.…

> [!methodology-and-sources] **Research Synthesis Workflow** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> **Step 1: Initial Pass** (20-30 min)
> - Open PDF in MarkMind
> - Highlight key claims, methods, results
> - Add brief comments to highlights
> 
> **Step 2: Structural Mapping** (15 min)
> - Create mind map: "[[Paper-Title]] - Key Concepts"
> - Root node: Paper title + authors
> - Branches: Main sections (Theory, Method, Results, Discussion)
> - Link annotations to appropriate branches
> 
> **Step 3: Synthesis** (20 min)
> - Add summary nodes synthesizing multiple highlights
> - Create boundaries grouping related findings
> - Add related links connecting concepts across sections
> - Link to existing vault notes:…

> [!methodology-and-sources] **Project Planning Workflow** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> **Setup:**
> - Create mind map: "[[Project-Name]] - Master Plan"
> - Use **Tree layout** for hierarchical structure
> 
> **Structure:**
> ```
> Project Name (Root)
> ├─ Phase 1: Research
> │  ├─ Literature Review → Due: Date, Owner: Name
> │  ├─ User Interviews → Due: Date, Owner: Name
> │  └─ Competitive Analysis → Due: Date, Owner: Name
> ├─ Phase 2: Design
> │  ├─ Wireframes → Links to [[Design-Specs]]
> │  └─ Prototypes → Links to [[Figma-Files]]
> ├─ Phase 3: Development
> │  └─ [Features as sub-nodes]
> └─ Phase 4: Launch
>     └─ [Launch tasks]
> ```
> 
> **Enhancements:**
> - Add **boundaries** around each phase (Rich Mode)
> -…

> [!methodology-and-sources] **Ideation to Organization Pipeline** *(from [[reference-comprehensive-excalidraw-and-markmind-2025121812]])*
> **Phase 1: Free Exploration** (Excalidraw)
> - Brainstorm ideas on infinite canvas
> - Draw connections, relationships, metaphors
> - No structure imposed—pure creativity
> - Duration: 15-30 minutes
> 
> **Phase 2: Structure Extraction** (MarkMind)
> - Identify key concepts from Excalidraw sketch
> - Create mind map with hierarchical organization
> - Add parent-child relationships
> - Apply taxonomy
> - Duration: 10-15 minutes
> 
> **Phase 3: Integration**
> - Embed Excalidraw sketch in mind map node: `![[Sketch.excalidraw]]`
> - OR embed mind map in note referencing sketch
> - Both views accessible from single entry point

---

## Source Attribution

**Extracted from:** [[reference-comprehensive-excalidraw-and-markmind-2025121812]]
