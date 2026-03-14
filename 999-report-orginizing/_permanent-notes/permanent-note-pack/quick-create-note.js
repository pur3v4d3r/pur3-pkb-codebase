/**
 * ═══════════════════════════════════════════════════════════════════════════
 * QUICK CREATE PERMANENT NOTE (QuickAdd Macro)
 * Rapidly create a new permanent note with guided metadata entry
 * 
 * SETUP:
 *   1. Place in your vault: 99-scripts/quickadd/quick-create-note.js
 *   2. Create a QuickAdd Macro Choice
 *   3. Add this as a User Script command
 *   4. Assign a hotkey (recommended: Alt+N or similar)
 * 
 * This script uses QuickAdd's requestInputs() for a single-page form
 * experience, then creates the note with proper metadata.
 * 
 * REQUIREMENTS: QuickAdd plugin (by chhoumann)
 * ═══════════════════════════════════════════════════════════════════════════
 */

module.exports = {
  entry: start,
  settings: {
    name: "Quick Create Permanent Note",
    author: "PKB System",
    options: {
      "Notes folder": {
        type: "text",
        defaultValue: "03-notes/01_permanent-notes",
        description: "Destination folder for permanent notes"
      },
      "Open after creation": {
        type: "toggle",
        defaultValue: true,
        description: "Open the new note after creating it"
      }
    }
  }
};

async function start(params, settings) {
  const { app, quickAddApi } = params;
  const moment = window.moment;

  // Collect all inputs in a single form
  const values = await quickAddApi.requestInputs([
    {
      id: "title",
      label: "Note Title (must match wiki-link)",
      type: "text",
      placeholder: "e.g., Cognitive Load Theory"
    },
    {
      id: "domain",
      label: "Primary Domain",
      type: "dropdown",
      options: [
        "cognitive-psychology",
        "educational-psychology",
        "philosophy",
        "neuroscience",
        "prompt-engineering",
        "computer-science",
        "decision-science",
        "epistemology",
        "learning-science",
        "linguistics",
        "mathematics",
        "systems-thinking",
        "other"
      ]
    },
    {
      id: "complexity",
      label: "Complexity Level",
      type: "dropdown",
      options: ["foundational", "intermediate", "advanced-practitioner", "expert"]
    },
    {
      id: "confidence",
      label: "Confidence",
      type: "dropdown",
      options: ["high", "medium", "low"]
    },
    {
      id: "importance",
      label: "Importance",
      type: "dropdown",
      options: ["critical", "high", "medium", "low"]
    },
    {
      id: "source",
      label: "Source Report",
      type: "text",
      defaultValue: "manual",
      placeholder: "Report title or 'manual'"
    }
  ]);

  const title = values.title?.trim();
  if (!title) {
    new Notice("No title provided. Aborting.");
    return;
  }

  const today = moment().format("YYYY-MM-DD");
  const folder = settings["Notes folder"];
  const filePath = `${folder}/${title}.md`;

  // Check if file already exists
  const existing = app.vault.getAbstractFileByPath(filePath);
  if (existing) {
    const overwrite = await quickAddApi.yesNoPrompt(
      "Note already exists",
      `"${title}" already exists. Open it instead?`
    );
    if (overwrite) {
      await app.workspace.openLinkText(filePath, "");
    }
    return;
  }

  // Build the note content
  const sourceType = values.source === "manual" ? "manual-creation" : "report-extraction";
  const extractionMethod = values.source === "manual" 
    ? "manual-authoring" 
    : "pkb-extractor-v1 → permanent-notes-generator-v1";

  const content = `---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "${title}"
aliases:
  - "${title}"
type: permanent-note
status: evergreen
confidence: ${values.confidence}

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
  - permanent-note
  - evergreen
  - ${values.domain}

domain: ${values.domain}
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: ${today}
updated: ${today}

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: ${sourceType}
source-reports:
  - "${values.source}"
evidence-quality: ${values.confidence}
extraction-method: "${extractionMethod}"

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
complexity-level: ${values.complexity}
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
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  - 

enables:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: ${values.importance}
---

# ${title}

> [!definition] **${title}**
> *Define the concept here.*



## Core Explanation



## Practical Implications

> [!example] **Application**
> *Concrete example.*



## Connections & Context


`;

  // Create the file
  const createdFile = await app.vault.create(filePath, content);
  new Notice(`Created: ${title}`);

  // Open if configured
  if (settings["Open after creation"]) {
    await app.workspace.openLinkText(filePath, "");
  }
}
