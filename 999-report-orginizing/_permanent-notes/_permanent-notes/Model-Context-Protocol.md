---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Model Context Protocol"
aliases:
  - "Model Context Protocol"
  - "MCP"
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
  - source/claude-opus
  - maturity/seedling
  - confidence/speculative
  - status/read

domain: other
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-03-19
updated: 2026-03-20

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "reference-comprehensive-mcp-servers-2025122412"
  - "reference-comprehensive-mcp-servers-2025122412.md"
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
  - "[[Comprehensive-Refernece-MCP-Servers|**Comprehensive Refernece: MCP Servers**]]"
  - "[[API-Fundamentals|API Fundamentals]]"
  - "[[JSON-RPC]]"
  - "[[AI-Agent-Architecture|AI Agent Architecture]]"
  - "[[Custom-MCP-Server-Development|Custom MCP Server Development]]"
  - "[[AI-PKB-Integration|AI-PKB Integration]]"
  - "[[Prompt-Library-Management|Prompt Library Management]]"
  - "[[Claude-Code-Workflows|Claude Code Workflows]]"
  - "[[**Comprehensive-Refernece:-MCP-Servers**|**Comprehensive Refernece: MCP Servers**]]"
  - "[[API-Fundamentals|API Fundamentals]]"
  - "[[JSON-RPC|JSON-RPC]]"
  - "[[AI-Agent-Architecture|AI Agent Architecture]]"
  - "[[Custom-MCP-Server-Development|Custom MCP Server Development]]"
  - "[[AI-PKB-Integration|AI-PKB Integration]]"
  - "[[Prompt-Library-Management|Prompt Library Management]]"
  - "[[Claude-Code-Workflows|Claude Code Workflows]]"

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

# Model Context Protocol

> [!definition] **Model Context Protocol**
> <span style='color: #FFC700;'>**Model Context Protocol**</span> is a universal interface specification enabling bidirectional communication between AI applications (hosts) and external services (servers). It abstracts away integration complexity, allowing developers to write tools once and have them work across multiple AI platforms—Claude Desktop, Claude Code, VS Code extensions, custom agents, and more.

## Core Explanation

> [!evidence] Supporting Evidence
> MCP’s design allows **semantic context routing**—e.g., an AI can request “all prompts tagged #cognitive-load” via `prompt://tag/cognitive-load`.^observed-in-practice

> [!evidence] Supporting Evidence
> Composable architecture allows **incremental adoption**—start with files, add git, then custom resources.^established

> [!analytical-insight] Key Insight
> %%evidence: consensus%%
> MCP was <span style='color: #FF5700;'>open-sourced by Anthropic in November 2024</span> and subsequently donated to the <span style='color: #FFC700;'>Agentic AI Foundation (AAIF)</span> under the Linux Foundation (December 2025). The foundation includes governance participation from Anthropic, OpenAI, Google, Microsoft, AWS, Cloudflare, and Bloomberg—signaling industry-wide adoption of this standard.

> [!analytical-insight] Key Insight
> %%confidence: verified%%
> The critical distinction: <span style='color: #FF00DC;'>Tools perform actions</span> (side effects), while <span style='color: #27FF00;'>Resources provide data</span> (read-only). Resources support real-time updates via `notifications/resources/list_changed` and `resources/subscribe`.

## Practical Implications

> [!example] **Application**
> *Describe how this concept applies in practice.*

> [!warning] **Key Distinction**
> <span style='color: #FF00DC;'>Gemini Code Assist MCP support is currently limited to VS Code.</span> IntelliJ integration is not available. Android Studio has separate MCP configuration through Settings → Tools → Gemini → MCP Servers.

## Connections & Context

**Cross-report connections:**
- [[Claude-Code|Claude Code]]
- [[Obsidian]]
- [[Prompt-Engineering|Prompt Engineering]]
- [[AI-Agent-Architecture|AI Agent Architecture]]
- [[JSON-RPC]]
- [[API-Design-Patterns|API Design Patterns]]

**Cross-report connections:**
- [[Personal-Knowledge-Base|Personal Knowledge Base]]
- [[Prompt-Engineering|Prompt Engineering]]
- [[Cognitive-Load-Theory|Cognitive Load Theory]]
- [[VS-Code|VS Code]]
- [[Claude-Code|Claude Code]]
- [[Gemini-Code-Assist|Gemini Code Assist]]

**Related concepts:**
[[Comprehensive-Refernece-MCP-Servers|**Comprehensive Refernece: MCP Servers**]] · [[API-Fundamentals|API Fundamentals]] · [[JSON-RPC]] · [[AI-Agent-Architecture|AI Agent Architecture]] · [[Custom-MCP-Server-Development|Custom MCP Server Development]] · [[AI-PKB-Integration|AI-PKB Integration]] · [[Prompt-Library-Management|Prompt Library Management]] · [[Claude-Code-Workflows|Claude Code Workflows]] · [[Gemini-Code-Assist|Gemini Code Assist]] · [[Obsidian-Automation|Obsidian Automation]] · [[Claude-Code|Claude Code]] · [[Gemini-Code-Assist|Gemini Code Assist]] · [[Obsidian]] · [[Prompt-Engineering|Prompt Engineering]] · [[AI-Agents|AI Agents]]

**Related concepts** *(from reference-comprehensive-mcp-servers-2025122412.md)*:
[[**Comprehensive-Refernece:-MCP-Servers**|**Comprehensive Refernece: MCP Servers**]] * [[API-Fundamentals|API Fundamentals]] * [[AI-Agent-Architecture|AI Agent Architecture]] * [[Custom-MCP-Server-Development|Custom MCP Server Development]] * [[AI-PKB-Integration|AI-PKB Integration]] * [[Prompt-Library-Management|Prompt Library Management]] * [[Claude-Code-Workflows|Claude Code Workflows]] * [[Gemini-Code-Assist|Gemini Code Assist]] * [[Obsidian-Automation|Obsidian Automation]] * [[Claude-Code|Claude Code]] * [[Prompt-Engineering|Prompt Engineering]] * [[AI-Agents|AI Agents]] * [[Claude-Desktop|Claude Desktop]] * [[Dataview|Dataview]] * [[Templater|Templater]]

**Cross-report connections** *(from reference-comprehensive-mcp-servers-2025122412.md)*:
- [[Claude-Code|Claude Code]]
- [[Obsidian|Obsidian]]
- [[Prompt-Engineering|Prompt Engineering]]
- [[AI-Agent-Architecture|AI Agent Architecture]]
- [[JSON-RPC|JSON-RPC]]

**Cross-report connections** *(from reference-comprehensive-mcp-servers-2025122412.md)*:
- [[Personal-Knowledge-Base|Personal Knowledge Base]]
- [[Prompt-Engineering|Prompt Engineering]]
- [[Cognitive-Load-Theory|Cognitive Load Theory]]
- [[VS-Code|VS Code]]
- [[Claude-Code|Claude Code]]



