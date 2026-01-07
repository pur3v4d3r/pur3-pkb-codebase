---
title: composite_project_obsidian-snippet-creator_v1
id: 20251114-200515
type: composite-project
status: active
rating: ""
version: "1.0"
source: pur3v4d3r
url: ""
tags:
  - prompt-engineering
  - pkb/infrastructure
  - type/prompt/agentic
  - status/seedling
  - source/llm
  - year/2025
aliases:
  - CSS Modification
  - CSS Snippets
  - Custom Snippets
link-up: []
link-related:
  - "[[composite_project_obsidian-theme-architect_v2]]"
---

---

`````prompt
---
id: prompt-block-v1
---

<role>
You are a senior UI/UX Designer specializing in knowledge management and text editor customization, particularly for Obsidian/Markdown-based Personal Knowledge Bases (PKBs). You have expert-level knowledge of CSS architecture, design systems, color theory, accessibility standards, and Obsidian's theming system.
</role>

<context>
I am customizing the CSS theme for my Obsidian PKB using CSS SNIPPETS. My vault contains an extensive taxonomy of custom callouts (100+ types) that serve different semantic and organizational purposes. I need a modular system of CSS snippets that allows me to quickly toggle between different visual treatments without major time investment.
</context>

<user_goal>
Transform my LIST OF ACTIVE CALLOUTS into a comprehensive, well-organized taxonomy of CUSTOM CSS SNIPPETS capable of modifying the visual appearance of my in-note CALLOUTS. This will give me a curated library of visual options to select from whenever I need a quick aesthetic or functional change to my notes.
</user_goal>

<assistants_goal>
Generate MANY usable and useful combinations of CALLOUT SNIPPET SETS using the provided Callout List and a research-expanded collection of CSS modifiers. Each snippet set should offer distinct visual hierarchy, functionality, or aesthetic while staying within the provided color palette.
</assistants_goal>

<scope>
## Quantitative Targets
- Generate **10-12 distinct CSS snippet sets**
- Each set should style **all callouts** from the provided list (100+ types)
- Create **at least 20-25 unique modifier combinations** across all sets
- Include **3-4 single-modifier sets** (baseline variations)
- Include **6-8 dual-modifier combination sets** (e.g., Hover + Gradient)
- Include **2-3 complex multi-modifier sets** (3+ combined effects)

## Coverage Requirements
- Every callout type from my active list must be addressed in each snippet
- Prioritize distinct visual differentiation between snippet sets
- Ensure each set offers a meaningfully different user experience
- Focus on practical, performance-conscious implementations
</scope>

<theme_palette>
## My Theme Colors (Base ALL Design Decisions On These)

**Primary Accent Colors:**
- Purple: `#7800F4` (Primary brand color)
- Gold: `#FFC700` (Secondary accent)
- Teal: `#72FFF1` (Tertiary accent)

**Core UI Colors:**
- Text Color: `#EAEAEA` (Primary readable text)
- Primary Background: `#17181B` (Main note background)

**Usage Guidelines:**
- Purple: Use for emphasis, primary interactive states, key information
- Gold: Use for warnings, highlights, important annotations
- Teal: Use for metadata, connections, secondary information
- Maintain readability against `#17181B` background at all times
</theme_palette>

<modifier_research_protocol>
## Known Modifiers (Starting Point)
- Hover states
- Gradient backgrounds
- Floating/elevation effects
- Scrolling animations
- Left-hand vertical bar + title (no interior background)

## Required: Expand This List

You MUST research and identify **at least 10 additional CSS modifiers/effects** suitable for callouts. For each discovered modifier, document:

1. **Technical Name**: CSS property-based name
2. **CSS Properties Involved**: Specific properties used
3. **Visual Impact**: User-perceivable effect
4. **Performance Considerations**: Animation cost, reflow triggers
5. **Best Use Case**: When this modifier adds value

### Suggested Research Areas:
- Transform effects (scale, rotate, skew, translate)
- Border animations (pulse, shimmer, gradient borders)
- Background patterns (stripes, dots, geometric)
- Text effects (text-shadow, gradient text, glow)
- Icon/title modifications
- Opacity/fade transitions
- 3D effects (perspective, depth, parallax)
- Blend modes (multiply, overlay, screen)
- Clip-path effects (shaped containers)
- Filter effects (blur, brightness, contrast)

### Modifier Documentation Format:
For each modifier you add, include a brief technical note:

```
````css
/* MODIFIER: [Name]
 * Properties: [CSS properties]
 * Performance: [Low/Medium/High cost]
 * Best For: [Use case description]
 */
 ````
```
</modifier_research_protocol>

<priority_modifiers>
## Prioritization Hierarchy

Focus development effort in this order (highest value first):

**TIER 1: Core Interactive (Must Have)**
1. Hover states - Most user interaction value
2. Left border + title styling - Matches current partial implementation
3. Gradient backgrounds - High visual appeal, low complexity

**TIER 2: Visual Enhancement (Should Have)**
4. Elevation/shadow effects - Adds depth and hierarchy
5. Border treatments - Frames and emphasis
6. Background patterns/textures - Subtle differentiation

**TIER 3: Advanced Effects (Nice to Have)**
7. Animated accents - Subtle motion for attention
8. Transform effects - Dimensional interest
9. Text effects - Title/content enhancement

**Combination Strategy:**
- Prioritize Tier 1 + Tier 1 combinations first
- Then Tier 1 + Tier 2 combinations
- Save Tier 3 combinations for complex multi-modifier sets
</priority_modifiers>

<quality_criteria>
## Every CSS Snippet Must Meet These Standards

### ✓ ACCESSIBILITY
- Maintain WCAG AA contrast ratios (minimum 4.5:1 for normal text, 3:1 for large text)
- Test all color combinations against `#17181B` background
- Ensure text remains readable in all states (default, hover, active)
- Provide sufficient visual differentiation for users with color vision deficiency

### ✓ PERFORMANCE
- Limit animations to transforms and opacity (avoid layout thrashing)
- Keep transition durations under 300ms for responsiveness
- Use `will-change` sparingly and only when necessary
- Avoid excessive box-shadow blur radius (keep under 20px)

### ✓ OBSIDIAN COMPATIBILITY
- Use Obsidian-safe selectors (`.callout[data-callout="type"]`)
- Test compatibility with Obsidian 1.4+ theming system
- Avoid overriding core Obsidian functionality
- Ensure snippets work with both Light and Dark base themes (prioritize Dark)

### ✓ VISUAL HIERARCHY
- Each snippet set should create clear differentiation between callout types
- Important callouts (e.g., "warning", "important") should be more visually prominent
- Metadata callouts should be more subtle
- Maintain consistent visual language within each set

### ✓ THEME CONSISTENCY
- Use ONLY colors from the provided palette (`#7800F4`, `#FFC700`, `#72FFF1`, `#EAEAEA`, `#17181B`)
- Derive variations using opacity/alpha channel adjustments
- Maintain the established Purple/Gold/Teal accent hierarchy

### ✓ READABILITY
- Text must remain easily readable in all states and treatments
- Avoid busy backgrounds behind text content
- Ensure sufficient padding/spacing for comfortable reading
- Title text should be clearly distinguishable from body text

### ✓ MODULARITY
- Each snippet file must be self-contained and independent
- No conflicts when multiple snippets are enabled (though this isn't the intended use)
- Easy to toggle on/off without breaking layout
- No dependencies on external resources

### ✓ RESPONSIVE DESIGN
- Snippets must work gracefully at various note widths
- Avoid fixed pixel widths; prefer percentages or relative units
- Test assumptions at 600px, 800px, 1200px note widths
- Ensure mobile-friendly (for Obsidian Mobile users)
</quality_criteria>

<naming_convention>
## File Naming Pattern

Use this consistent naming structure for all snippet files:

**Format:** `callouts-[primary-modifier]-[secondary-modifier]-[color-accent].css`

**Examples:**
- `callouts-hover-glow-purple.css`
- `callouts-gradient-floating-teal.css`
- `callouts-animated-border-gold.css`
- `callouts-3d-shadow-purple-gold.css`
- `callouts-minimal-leftbar-teal.css`

**Rules:**
- Use lowercase with hyphens (kebab-case)
- Primary modifier first, then secondary
- Color accent last
- Keep names descriptive but concise (max 5 segments)
- Avoid abbreviations unless universally understood

**Directory Structure Suggestion:**

```
````
📁 CSS Snippets/
  📁 Callouts/
    📁 Single-Modifier/
    📁 Dual-Modifier/
    📁 Multi-Modifier/
````
```

</naming_convention>

<example_snippets>
## Reference Examples (Your Output Should Match This Format)

### Example 1: Single Modifier - Hover Glow Effect
````css
/* ═══════════════════════════════════════════════════════════════
 * CSS SNIPPET: Hover Glow Effect - Purple Accent
 * ═══════════════════════════════════════════════════════════════
 * Purpose: Adds subtle purple glow on hover for emphasis and interactivity
 * Affects: All custom callouts from user taxonomy
 * Modifier: Hover + Glow
 * Performance: Low (transform + box-shadow only)
 * File: callouts-hover-glow-purple.css
 * ═══════════════════════════════════════════════════════════════ */

/* Base state for all callouts */
.callout {
    transition: all 0.25s ease-out;
    border-left: 3px solid rgba(120, 0, 244, 0.6);
}

/* Hover state - purple glow */
.callout:hover {
    border-left-color: #7800F4;
    box-shadow: -4px 0 12px rgba(120, 0, 244, 0.3),
                0 2px 8px rgba(120, 0, 244, 0.15);
    transform: translateX(3px);
}

/* Specific callout: key-claim - Enhanced emphasis */
.callout[data-callout="key-claim"] {
    border-left-width: 4px;
    background: linear-gradient(to right, rgba(120, 0, 244, 0.08), transparent 60%);
}

.callout[data-callout="key-claim"]:hover {
    box-shadow: -6px 0 15px rgba(120, 0, 244, 0.4),
                0 3px 10px rgba(120, 0, 244, 0.2);
}

/* Specific callout: warning - Gold accent override */
.callout[data-callout="warning"] {
    border-left-color: rgba(255, 199, 0, 0.6);
}

.callout[data-callout="warning"]:hover {
    border-left-color: #FFC700;
    box-shadow: -4px 0 12px rgba(255, 199, 0, 0.3),
                0 2px 8px rgba(255, 199, 0, 0.15);
}

/* Continue pattern for all 100+ callouts… */
```
````

### Example 2: Dual Modifier - Gradient Background + Floating Effect
````css
```
/* ═══════════════════════════════════════════════════════════════
 * CSS SNIPPET: Gradient Float - Teal Accent
 * ═══════════════════════════════════════════════════════════════
 * Purpose: Combines subtle gradient backgrounds with elevation on hover
 * Affects: All custom callouts from user taxonomy
 * Modifiers: Gradient Background + Floating/Elevation
 * Performance: Medium (gradient + box-shadow + transform)
 * File: callouts-gradient-float-teal.css
 * ═══════════════════════════════════════════════════════════════ */

/* Base state - gradient background */
.callout {
    background: linear-gradient(
        135deg,
        rgba(114, 255, 241, 0.05) 0%,
        rgba(23, 24, 27, 0) 70%
    );
    border-left: 2px solid rgba(114, 255, 241, 0.4);
    border-radius: 4px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Hover state - floating elevation */
.callout:hover {
    background: linear-gradient(
        135deg,
        rgba(114, 255, 241, 0.12) 0%,
        rgba(23, 24, 27, 0) 70%
    );
    border-left-color: #72FFF1;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3),
                0 1px 3px rgba(114, 255, 241, 0.2);
    transform: translateY(-2px);
}

/* Specific callout: definition - Enhanced gradient */
.callout[data-callout="definition"] {
    background: linear-gradient(
        135deg,
        rgba(114, 255, 241, 0.08) 0%,
        rgba(120, 0, 244, 0.03) 100%
    );
}

.callout[data-callout="definition"]:hover {
    background: linear-gradient(
        135deg,
        rgba(114, 255, 241, 0.15) 0%,
        rgba(120, 0, 244, 0.06) 100%
    );
}

/* Continue pattern for all callouts… */

</example_snippets>

<organization_structure>
## Required Output Structure

Organize your response using this exact hierarchical structure:

# 🎨 CSS SNIPPET TAXONOMY FOR OBSIDIAN CALLOUTS

## 📋 Quick Navigation
- [Single Modifier Snippets](#single-modifier-snippets)
- [Dual Modifier Combinations](#dual-modifier-combinations)
- [Multi-Modifier Complex Sets](#multi-modifier-complex-sets)
- [Modifier Reference Guide](#modifier-reference-guide)

---

## 🔍 Modifier Reference Guide

### Discovered Modifiers
[List all CSS modifiers researched, with technical documentation]

1. **Hover States**
   - Properties: `:hover`, `transition`, `transform`
   - Performance: Low
   - Best For: Interactive emphasis

2. **Gradient Backgrounds**
   - Properties: `background: linear-gradient()`
   - Performance: Low
   - Best For: Subtle visual differentiation

[Continue for all 15+ modifiers discovered…]

---

## 🎯 CATEGORY 1: Single Modifier Snippets

### 1.1 Hover Effects Collection

#### Snippet Set 1A: Hover Glow - Purple
- **File Name:** `callouts-hover-glow-purple.css`
- **Visual Description:** Subtle purple glow and slight rightward shift on hover
- **Best Use Case:** General-purpose emphasis with primary brand color
- **Modifiers Used:** Hover + Box Shadow + Transform
```css
[COMPLETE CSS CODE HERE - ALL 100+ CALLOUTS]
```

#### Snippet Set 1B: Hover Glow - Gold
[Same structure as above…]

#### Snippet Set 1C: Hover Scale - Teal
[Same structure…]

### 1.2 Gradient Background Collection

#### Snippet Set 2A: Diagonal Gradient - Purple/Teal
[Same structure…]

[Continue for all single-modifier variations…]

---

## 🔗 CATEGORY 2: Dual Modifier Combinations

### 2.1 Hover + Gradient Sets

#### Snippet Set 3A: Gradient Float - Teal
[Complete structure with code…]

#### Snippet Set 3B: Gradient Glow - Purple/Gold
[Complete structure with code…]

### 2.2 Floating + Border Animation Sets

#### Snippet Set 4A: Elevated Border Pulse - Purple
[Complete structure with code…]

[Continue for all dual-modifier combinations…]

---

## ⚡ CATEGORY 3: Multi-Modifier Complex Sets

### 3.1 Advanced Visual Systems

#### Snippet Set 9A: 3D Depth System - Full Spectrum
- **File Name:** `callouts-3d-depth-animated-full.css`
- **Visual Description:** Combines perspective transforms, animated gradients, and hover depth
- **Best Use Case:** High-impact notes requiring strong visual hierarchy
- **Modifiers Used:** 3D Transform + Gradient + Hover + Shadow + Border Animation
```css
[COMPLETE CSS CODE HERE - ALL 100+ CALLOUTS]
```

[Continue for remaining complex sets…]

---

## 📊 Snippet Set Comparison Matrix

| Snippet Set | Primary Effect | Secondary Effect | Performance | Visual Impact | Best For |
|-------------|---------------|------------------|-------------|---------------|----------|
| 1A: Hover Glow Purple | Hover | Glow | Low | Medium | General use |
| 1B: Hover Glow Gold | Hover | Glow | Low | Medium | Warnings/attention |
[Complete table for all 10-12 sets…]

---

## 🚀 Implementation Guide

### How to Use These Snippets

1. **Navigate to:** Settings → Appearance → CSS Snippets
2. **Place files in:** `[Vault]/.obsidian/snippets/`
3. **Enable ONE snippet** at a time (they're designed as alternatives, not layers)
4. **Reload Obsidian** or toggle snippet off/on to see changes
5. **Experiment freely** - snippets are non-destructive

### Recommended Workflows

**For Daily Notes:** Use `callouts-hover-glow-purple.css` (subtle, non-distracting)
**For Project Planning:** Use `callouts-gradient-float-teal.css` (clear hierarchy)
**For Important Documents:** Use `callouts-3d-depth-animated-full.css` (maximum impact)

---

## 🎨 Customization Notes

All snippets use your theme palette exclusively. To customize further:

- **Change accent color:** Find/replace hex codes
- **Adjust intensity:** Modify `rgba()` alpha values
- **Tune animation speed:** Edit `transition` duration values
- **Modify hover distance:** Adjust `transform: translateX/Y()` values

---

### Required for Each Snippet Set:
1. **Descriptive header comment block** (as shown in examples)
2. **Complete CSS code** covering ALL 100+ callouts
3. **File name suggestion** following naming convention
4. **Visual description** (1-2 sentences)
5. **Best use case** (when to choose this set)
6. **Modifiers used** (list of effects combined)
7. **Performance note** (Low/Medium/High)

</organization_structure>

<edge_case_handling>
## Handling Special Situations

### If Color Combinations Create Readability Issues:
- **Solution 1:** Fall back to single accent color with opacity variations
- **Solution 2:** Increase contrast by darkening/lightening base colors
- **Solution 3:** Provide alternative high-contrast version in comment
- **Documentation:** Note the issue in snippet header comments

### If 100+ Callouts Create Unmanageable Snippet Length:
- **Preferred Approach:** Use CSS attribute selectors and base classes
- **Pattern:**

```
````css
  /* Base style for ALL callouts */
  .callout { /* common properties */ }
  
  /* Specific overrides only when needed */
  .callout[data-callout="warning"] { /* unique properties */ }
````
```
- **Grouping Strategy:** Semantically group similar callouts
  - Example: All `analysis-*` callouts share base style
  - Example: All `phase-*` callouts share progressive color scheme

### If Modifier Combinations Don't Work Well Together:
- **Test First:** Before including, mentally verify the combination makes visual sense
- **Skip Conflicts:** Don't force combinations that compete visually
- **Document Why:** If skipping an obvious combination, note why in reference guide
- **Alternative:** Suggest a better combination that achieves similar goals

### If Performance Concerns Arise:
- **Prioritize:** Favor `transform` and `opacity` over other properties
- **Simplify:** Reduce blur radius, animation complexity, or gradient stops
- **Note It:** Document performance cost in snippet header
- **Provide Lite Version:** Offer a performance-optimized alternative

</edge_case_handling>

<constraints>
## Non-Negotiable Requirements

1. **Modularity:** Each CSS snippet file must be completely self-contained and independently functional
2. **Comments:** Every snippet MUST begin with a detailed header comment block including:
   - Purpose statement
   - Affected elements (specific callout types)
   - Modifiers used
   - Performance rating
   - File name suggestion
3. **Completeness:** Each snippet set must address ALL callouts in the provided list
4. **Validation:** Every snippet must meet ALL quality criteria specified above
5. **Format Consistency:** Follow the example snippet format exactly
6. **Organization:** Present output in the specified hierarchical structure
7. **Documentation:** Include implementation guide and customization notes
8. **Testing:** Mentally validate each snippet against Obsidian's rendering engine

</constraints>

<task>
## Your Execution Instructions

1. **Research Phase:** Identify and document at least 10 additional CSS modifiers beyond the 5 provided
2. **Design Phase:** Plan 10-12 distinct snippet sets using single, dual, and multi-modifier combinations
3. **Implementation Phase:** Write complete CSS code for each snippet set, covering all 100+ callouts
4. **Organization Phase:** Structure output according to specified hierarchy
5. **Documentation Phase:** Provide comparison matrix, implementation guide, and customization notes
6. **Validation Phase:** Verify all snippets meet quality criteria and constraints

## Prioritization:
- Start with Tier 1 modifiers (hover, borders, gradients)
- Use provided color palette exclusively
- Focus on practical, usable combinations
- Ensure distinct visual differentiation between sets
- Maintain performance consciousness throughout

</task>

<output>
## Deliverable Specification

A comprehensive, well-organized taxonomy of 10-12 CSS snippet sets, structured according to the organization template, with:

- Complete, production-ready CSS code for each set
- All 100+ callouts addressed in each set
- Clear documentation and implementation guidance
- Modifier reference guide with research findings
- Comparison matrix for quick selection
- Customization notes for user modifications

**Format:** Markdown document with embedded CSS code blocks
**Tone:** Professional yet accessible, technical but not academic
**Length:** Comprehensive - prioritize completeness over brevity

</output>

<user_active_callout_list>
## My 100+ Active Callouts (Must Style ALL of These)

"key-claim", "casual-link", "evidence", "confusion", "counter-argument", "no-evidence", "connection-ideas", "to-do", "read-complete", "reading-in-progress", "read-asap", "insight", "principle-point", "shot-idea", "lighting-setup", "composition", "post-processing", "cosmos-concept", "equation", "thought-experiment", "project-link", "hub-moc", "revist", "definition", "connections-and-links", "pre-read-questions", "pre-read-thoughts", "the-purpose", "important-links", "choice-a", "choice-b", "document", "capture", "tasks", "the-philosophy", "analogy", "ask-yourself-this", "question", "summary", "abstract", "how-to-use-this", "the-goal", "the-mission", "outcome", "methodology-and-sources", "starting-message", "phase-one", "phase-two", "phase-three", "phase-four", "how-to-use", "gemini-pro-response", "message", "key-changes", "how-this-dashboard-works", "your-new-workflow", "changes-from-prompting-dashboard", "helpful-tip", "the-start", "related-topics-to-consider", "key", "topic-idea", "plan", "math", "kanban", "note-toolbar", "links-to-related-notes", "thoughts", "start-of-chat", "atomic-concept", "further-exploration", "what-this-does", "analysis-rhetorical", "analysis-logical", "analysis-contextual", "analysis-cognitive", "project-kickstarter", "zettelkasten-incubator", "problem-clarity-solution", "disposition", "description", "use-cases-and-examples", "core-principle", "warning", "constraints-and-pitfalls", "quick-reference", "purpose", "argument", "review", "feynman-technique", "fleeting-thought", "work-log-entry", "left-off-reading-at", "in-note-metadata", "input-and-instruction", "iteration-and-versioning", "topic-name", "comprehensive-reference", "related-topics-for-pkb-expansion", "answer", "tags-taxonomy", "questions"
</user_active_callout_list>

`````



