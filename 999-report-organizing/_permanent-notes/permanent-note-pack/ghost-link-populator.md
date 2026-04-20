<%*
// ═══════════════════════════════════════════════════════════════════════════
// GHOST LINK POPULATOR TEMPLATE (Templater)
// Auto-populates when you click a [[wiki-link]] that doesn't exist yet
// 
// SETUP:
//   1. Place in your templates folder (e.g., 05-templates/)
//   2. In Templater settings, under "Folder Templates":
//      - Folder: 03-notes/01_permanent-notes
//      - Template: this file
//   3. Now when you click a red/ghost [[wiki-link]], the new file
//      auto-populates with this template
//
// The title is auto-extracted from the filename (which comes from the 
// wiki-link text), so no prompt is needed for the title.
// ═══════════════════════════════════════════════════════════════════════════

// Title comes from the filename (which matches the wiki-link)
const title = tp.file.title;
const today = tp.date.now("YYYY-MM-DD");

// Quick domain selection
const domain = await tp.system.suggester(
  ["cognitive-psychology", "educational-psychology", "philosophy", "neuroscience", 
   "prompt-engineering", "computer-science", "decision-science", "epistemology",
   "learning-science", "linguistics", "mathematics", "systems-thinking", "other"],
  ["cognitive-psychology", "educational-psychology", "philosophy", "neuroscience",
   "prompt-engineering", "computer-science", "decision-science", "epistemology",
   "learning-science", "linguistics", "mathematics", "systems-thinking", "other"],
  false, `Domain for "${title}":`
);

const complexity = await tp.system.suggester(
  ["Foundational", "Intermediate", "Advanced Practitioner", "Expert"],
  ["foundational", "intermediate", "advanced-practitioner", "expert"],
  false, "Complexity:"
);
_%>
---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "<% title %>"
aliases:
  - "<% title %>"
type: permanent-note
status: evergreen
confidence: medium

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
  - permanent-note
  - evergreen
  - <% domain %>

domain: <% domain %>
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: <% today %>
updated: <% today %>

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: ghost-link-population
source-reports:
  - "populated from wiki-link"
evidence-quality: medium
extraction-method: "manual-authoring"

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
complexity-level: <% complexity %>
depth-level: comprehensive

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  - 

related:
  - 

broader:
  - 

narrower:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: medium
---

# <% title %>

> [!definition] **<% title %>**
> <% tp.file.cursor() %>

## Core Explanation



## Practical Implications



## Connections & Context

> [!tip] **Notes Linking Here**
> Check the backlinks panel to see which notes reference this concept.
