<%*
// ═══════════════════════════════════════════════════════════════════════════
// PERMANENT NOTE TEMPLATE (Templater)
// For use with the Permanent Notes Generator PKB system
// 
// SETUP: 
//   1. Place this file in your Templater templates folder
//   2. In Templater settings, set your template folder path
//   3. Trigger via: Templater > Insert Template, or assign a hotkey
//   4. Optionally, assign this as a folder template for 03-notes/01_permanent-notes/
//
// REQUIREMENTS: Templater plugin (by SilentVoid13)
// COMPATIBLE WITH: Templater 1.x and 2.x syntax
// ═══════════════════════════════════════════════════════════════════════════

// Prompt for core metadata
const title = await tp.system.prompt("Note Title (must match wiki-link exactly):");
if (!title) return;

const domain = await tp.system.suggester(
  ["cognitive-psychology", "educational-psychology", "philosophy", "neuroscience", 
   "prompt-engineering", "computer-science", "decision-science", "epistemology",
   "learning-science", "linguistics", "mathematics", "systems-thinking", "other"],
  ["cognitive-psychology", "educational-psychology", "philosophy", "neuroscience",
   "prompt-engineering", "computer-science", "decision-science", "epistemology",
   "learning-science", "linguistics", "mathematics", "systems-thinking", "other"],
  false, "Select primary domain:"
);

const complexity = await tp.system.suggester(
  ["Foundational", "Intermediate", "Advanced Practitioner", "Expert"],
  ["foundational", "intermediate", "advanced-practitioner", "expert"],
  false, "Complexity level:"
);

const confidence = await tp.system.suggester(
  ["High - Well-established knowledge", "Medium - Emerging or debated", "Low - Speculative or preliminary"],
  ["high", "medium", "low"],
  false, "Confidence level:"
);

const sourceReport = await tp.system.prompt("Source report title (or 'manual' if hand-written):", "manual");

// Generate aliases prompt
const aliasInput = await tp.system.prompt("Aliases (comma-separated, e.g. 'CLT, Cognitive Overload Theory'):", "");
const aliases = aliasInput ? aliasInput.split(",").map(a => a.trim()).filter(a => a.length > 0) : [];

// Generate the date
const today = tp.date.now("YYYY-MM-DD");

// Build aliases YAML
let aliasYaml = "";
if (aliases.length > 0) {
  aliasYaml = aliases.map(a => `  - "${a}"`).join("\n");
} else {
  aliasYaml = `  - "${title}"`;
}

// Rename file to match title
await tp.file.rename(title);
_%>
---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "<% title %>"
aliases:
<% aliasYaml %>
type: permanent-note
status: evergreen
confidence: <% confidence %>

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
source-type: <% sourceReport === "manual" ? "manual-creation" : "report-extraction" %>
source-reports:
  - "<% sourceReport %>"
evidence-quality: <% confidence %>
extraction-method: "<% sourceReport === "manual" ? "manual-authoring" : "pkb-extractor-v1 → permanent-notes-generator-v1" %>"

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
complexity-level: <% complexity %>
depth-level: comprehensive

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  - "[[]]"

related:
  - "[[]]"

broader:
  - "[[]]"

narrower:
  - "[[]]"

see-also:
  - "[[]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  - "[[]]"

enables:
  - "[[]]"

expansion-topics:
  - topic: "[[]]"
    description: ""
    priority: medium

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: medium
---

# <% title %>

> [!definition] **<% title %>**
> *Define the concept here in 1-2 precise sentences.*

<% tp.file.cursor() %>

## Core Explanation



## Practical Implications

> [!example] **Application**
> *Concrete example of this concept in practice.*



## Connections & Context



## Key Distinctions

> [!warning] **Common Misconception**
> *What people often get wrong about this concept.*


