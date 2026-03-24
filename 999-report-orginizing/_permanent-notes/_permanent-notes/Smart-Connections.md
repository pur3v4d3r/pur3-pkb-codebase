---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Smart Connections"
aliases:
  - "Smart Connections"
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
  - type/report
  - year/2025
  - type/analysis
  - status/in-progress
  - pkb

domain: other
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-03-24
updated: 2026-03-24

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "reference-comprehensive-text-generator-plugin-complete-api-interface-reference-2025121507"
  - "reference-comprehensive-text-generator-plugin-complete-api-interface-reference-2025121507.md"
evidence-quality: medium
extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
complexity-level: intermediate
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
  - "[[Text-Generator-Plugin-Complete-API-Interface-Reference|Text Generator Plugin: Complete API Interface Reference]]"
  - "[[Templater]]"
  - "[[Dataview]]"
  - "[[Claude-API|Claude API]]"
  - "[[Prompt-Engineering|Prompt Engineering]]"
  - "[[PKB-Automation|PKB Automation]]"
  - "[[Obsidian]]"
  - "[[API]]"
  - "[[Text-Generator-Plugin:-Complete-API-Interface-Reference|Text Generator Plugin: Complete API Interface Reference]]"
  - "[[Templater|Templater]]"
  - "[[Dataview|Dataview]]"
  - "[[Claude-API|Claude API]]"
  - "[[Prompt-Engineering|Prompt Engineering]]"
  - "[[PKB-Automation|PKB Automation]]"
  - "[[Obsidian|Obsidian]]"
  - "[[API|API]]"

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

# Smart Connections

> [!definition] **Smart Connections**
> [**Smart-Connections**:: An [[Obsidian]] plugin that provides local-first [[Semantic Search]] using [[AI Embeddings]]. It enables finding conceptually related notes even when they don't share explicit links or keywords. The plugin runs entirely on-device after initial embedding, requiring no API calls for search functionality.]

## Core Explanation

<!-- Expand this section with deeper explanation -->

## Practical Implications

> [!example] **Application**
> *Describe how this concept applies in practice.*

> [!warning] **Key Distinction**
> Your API key provides direct access to your Anthropic account and billing. Never share templates containing hardcoded keys, and consider using environment variables for team vaults. TGP stores the key in Obsidian's plugin data, which is not encrypted by default.

## Connections & Context

**Related concepts:**
[[Text-Generator-Plugin-Complete-API-Interface-Reference|Text Generator Plugin: Complete API Interface Reference]] · [[Templater]] · [[Dataview]] · [[Claude-API|Claude API]] · [[Prompt-Engineering|Prompt Engineering]] · [[PKB-Automation|PKB Automation]] · [[Obsidian]] · [[API]] · [[Large-Language-Models|Large Language Models]] · [[Template-Engineering|Template Engineering]] · [[Claude-Projects|Claude Projects]] · [[PKB]] · [[Obsidian]]

**Related concepts** *(from reference-comprehensive-text-generator-plugin-complete-api-interface-reference-2025121507.md)*:
[[Text-Generator-Plugin:-Complete-API-Interface-Reference|Text Generator Plugin: Complete API Interface Reference]] * [[Claude-API|Claude API]] * [[Prompt-Engineering|Prompt Engineering]] * [[PKB-Automation|PKB Automation]] * [[Large-Language-Models|Large Language Models]] * [[Template-Engineering|Template Engineering]] * [[Claude-Projects|Claude Projects]] * [[OpenAI|OpenAI]] * [[Anthropic-Claude|Anthropic Claude]] * [[Google-Gemini|Google Gemini]] * [[HuggingFace|HuggingFace]] * [[Ollama|Ollama]] * [[Template-System|Template System]] * [[ChatGPT|ChatGPT]] * [[Claude.ai|Claude.ai]]


## Methodology Notes

> [!methodology-and-sources] **Context Assembly Pattern**
> When TGP processes a template, it assembles the final prompt through these layers:
> 1. **System Prompt**: Base instructions for model behavior
> 2. **Template Prompt**: Your specific task instructions
> 3. **Context Variables**: Automatically populated from your note/selection
> 4. **User Input**: Any additional input you provide at generation time

---

## Source Attribution

**Extracted from:** [[reference-comprehensive-text-generator-plugin-complete-api-interface-reference-2025121507]]
