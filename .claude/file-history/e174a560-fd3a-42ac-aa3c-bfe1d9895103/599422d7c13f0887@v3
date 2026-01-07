---
tags: #memory-system #core #technology #stack #integrations
aliases: [Technology Stack, Tech Integration, Tools Context]
status: evergreen
certainty: ^verified
created: 2026-01-06
last_updated: 2026-01-06
memory-type: core
project: pkb-vault-operations
---

# Technology Context & Stack

> [!abstract] Purpose
> This document catalogs the complete technology stack powering the PKB vault, including tools, plugins, integrations, and their configurations. It serves as the definitive reference for "what technologies are in use and how they work together."

## Context

The vault operates as a sophisticated multi-technology ecosystem, integrating human knowledge management tools (Obsidian) with AI agent systems (Claude Code, Gemini Code Assist) and semantic retrieval infrastructure (Smart Connections + MCP). Each technology is chosen for specific capabilities and integrated to create a cohesive, intelligent knowledge system.

%%QA:tools:technology-stack%%
The technology stack combines Obsidian for knowledge management, Claude/Gemini for AI assistance, Smart Connections for semantic embedding, and MCP for agent integration, creating an intelligent PKB ecosystem.

---

## Core Technologies

### 1. Obsidian (Knowledge Management Platform)

**Version**: v1.5.0+

**Purpose**: Primary interface for PKB creation, editing, and navigation

**Key Features Used**:
- **Markdown-based**: Native `.md` file format for portability
- **Graph View**: Visual representation of [[Wiki-Link]] network
- **Community Plugins**: Extensive automation ecosystem
- **Live Preview**: Real-time rendering while editing
- **Vault Sync**: Local-first with optional cloud sync

**Configuration**:
- Location: `D:\10_pur3v4d3r's-vault`
- Hidden folders: `.obsidian`, `.smart-env`, `.trash`, `.git`
- Vault type: Markdown files with YAML frontmatter
- Linking: `[[Wiki-Link]]` format (not markdown links)

**Critical Dependencies**:
- Community Plugins (see Plugin Ecosystem section)
- CSS Snippets & Custom Theme
- Templater templates for automation
- Dataview queries for intelligence

%%QA:tools:obsidian-config%%
Obsidian configured with local-first storage at D:\10_pur3v4d3r's-vault, using markdown files with YAML frontmatter and Wiki-Link format for internal references.

---

### 2. Claude Code (AI Coding Assistant)

**Platform**: VS Code Extension + Claude Desktop

**Model**: Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)

**Capabilities**:
- Extended thinking for complex reasoning
- Long-form content generation
- System prompt engineering
- Cross-domain synthesis
- Architecture design

**Integration Points**:
- **System Prompt**: [[__LOCAL-REPO/CLAUDE.md]] — Core identity and operational protocols
- **Memory System**: Reads/writes to `.claude/` directory
- **VS Code**: Native integration for file operations
- **MCP Tools**: Accesses Smart Connections via MCP server

**Configuration**:
- Settings location: VS Code settings.json
- Claude Desktop config: `%APPDATA%\Claude\claude_desktop_config.json`
- MCP servers: Smart Connections (pending configuration)

**Operational Modes** (from system prompt):
- Note Generation Mode
- Note Refactoring Mode
- Vault Navigation Mode
- Template/Prompt Engineering Mode
- Plugin Integration Mode
- Collaboration Mode (with Gemini)

%%QA:workflow:claude-integration%%
Claude Code integrates via VS Code extension and Claude Desktop, with system prompt at __LOCAL-REPO/CLAUDE.md defining six operational modes and memory-first operation protocols.

---

### 3. Gemini Code Assist (Execution Specialist)

**Platform**: Google AI Studio / API Integration

**Model**: Gemini Pro (exact version varies)

**Capabilities**:
- Structured reasoning and planning
- Code execution and debugging
- Quick iterations
- Technical documentation
- Task decomposition

**Integration Points**:
- **System Prompt**: [[00-meta/gemini-code-assist-system-instructions.md]]
- **Shared Memory**: [[00-meta/session-memory.md]] for hand-offs
- **Coordination**: Complementary role with Claude (Claude = reasoning, Gemini = execution)

**Hand-off Protocol** (from [[systemPatterns]]):
1. Outgoing LLM updates session-memory.md
2. Documents current state, blockers
3. Specifies incoming LLM's tasks
4. Incoming LLM acknowledges and continues

%%QA:workflow:gemini-integration%%
Gemini Code Assist operates via Google AI Studio with system prompt at 00-meta/, coordinating with Claude through shared session-memory.md for seamless hand-offs.

---

## Semantic Retrieval Infrastructure

### 4. Smart Connections (Obsidian Plugin)

**Version**: 4.2.4 (installed: 1766786653411)

**Purpose**: Automatic semantic embedding and similarity search

**Embedding Model**:
- **Model**: TaylorAI/bge-micro-v2
- **Type**: Local (transformer-based)
- **Dimensions**: 384
- **Adapter**: Transformers

**Configuration**:
- **Location**: `.obsidian/plugins/smart-connections/`
- **Settings**: `.smart-env/smart_env.json`
- **Embeddings**: `.smart-env/multi/` (8,383+ AJSON files)
- **Min Characters**: 100 (may lower for short memories)
- **Folder Exclusions**: None (will auto-index `.claude/`)
- **File Exclusions**: Specific long filenames, PDFs, images

**How It Works**:
1. File saved in vault
2. Smart Connections detects change (~30 second latency)
3. Generates embedding using local model
4. Stores as AJSON in `.smart-env/multi/`
5. Available for semantic search immediately

**Current Status**: ✅ Operational with 8,383 embeddings

%%QA:tools:smart-connections-config%%
Smart Connections uses TaylorAI/bge-micro-v2 local model with 384 dimensions, auto-embeds files with 100 character minimum, stores embeddings as AJSON in .smart-env/multi/ directory.

---

### 5. Model Context Protocol (MCP) Server

**Package**: `@yejianye/smart-connections-mcp` (pending installation)

**Purpose**: Bridge between AI agents and Smart Connections embeddings

**Architecture**:
```
Agent Request → MCP Server → Smart Connections → Embeddings → Results
```

**Tools Provided**:
- **lookup**: Semantic search by text query
- **connection**: Find similar notes to a file
- **stats**: View embedding coverage
- **validate**: Check data integrity

**Configuration**:
- **Location**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Environment Variable**: `OBSIDIAN_VAULT=D:\10_pur3v4d3r's-vault`
- **Command**: `npx -y @yejianye/smart-connections-mcp`

**Current Status**: ⚙️ Pending configuration (Phase 2)

%%QA:tools:mcp-configuration%%
MCP server bridges agents and Smart Connections, providing lookup, connection, stats, and validate tools. Configuration pending at %APPDATA%\Claude\claude_desktop_config.json.

---

## Obsidian Plugin Ecosystem

### Core Automation Plugins

**[[Dataview]]** (Database Queries)
- **Purpose**: Query vault like a database
- **Syntax**: DataviewJS & DQL
- **Used For**: Dashboards, analytics, automated lists
- **Examples**: Task lists, project trackers, memory queries

**[[Templater]]** (Template Engine)
- **Purpose**: Dynamic template insertion with code execution
- **Syntax**: `<% %>` template tags
- **Used For**: Note creation automation, metadata generation
- **Location**: `99-system/02-templater/`

**[[QuickAdd]]** (Macro System)
- **Purpose**: Rapid note capture and macro execution
- **Used For**: Prompt capture, component insertion, workflow shortcuts
- **Macros**: Located in `99-system/01-quickadd/`

**[[Meta Bind]]** (Forms & Buttons)
- **Purpose**: Interactive forms and action buttons
- **Used For**: Status toggles, health checks, interactive metadata

**[[Tasks]]** (Task Management)
- **Purpose**: Enhanced task tracking with queries
- **Syntax**: Global filter, recurring tasks, priorities
- **Used For**: Todo tracking, project management

%%QA:tools:plugin-ecosystem%%
Core plugins include Dataview for queries, Templater for templates, QuickAdd for macros, Meta Bind for forms, and Tasks for task management, creating comprehensive automation system.

### Knowledge Management Plugins

**[[Smart Connections]]** (covered above)

**[[Excalidraw]]** (Diagramming)
- **Purpose**: Hand-drawn diagrams and visual notes
- **Format**: `.excalidraw.md` files

**[[Kanban]]** (Project Boards)
- **Purpose**: Visual project management
- **Format**: `.kanban.md` files with card lanes

### Enhancement Plugins

**[[Advanced Tables]]** (Table Editing)
- **Purpose**: Excel-like table manipulation
- **Features**: Formula support, formatting

**[[Linter]]** (Markdown Formatting)
- **Purpose**: Automated markdown standardization
- **Used For**: Consistent formatting, metadata validation

---

## Development Tools

### 6. VS Code (IDE)

**Version**: Latest stable

**Purpose**: Development environment for Claude Code and vault operations

**Extensions Used**:
- **Claude Code**: AI assistant integration
- **Markdown All in One**: Enhanced markdown support
- **YAML**: Frontmatter editing

**Configuration**:
- Workspace: `D:\10_pur3v4d3r's-vault`
- Settings: `.vscode/settings.json`

### 7. Git (Version Control)

**Purpose**: Vault version history and backup

**Configuration**:
- **Remote**: (if configured, typically GitHub)
- **Branch**: `main`
- **Status** (from root):
  ```
  D __LOCAL-REPO/_library/_pof/papers/README.md
  D __LOCAL-REPO/_library/_pof/papers/arxiv_papers_for_human_review.csv
  D __LOCAL-REPO/_library/_pof/papers/blacklist.csv
  D __LOCAL-REPO/_library/_pof/papers/master_papers.csv
  ?? __LOCAL-REPO/_library/research-papers/
  ```

**Commit Protocol** (from Claude system prompt):
- User explicitly requests commits
- Claude drafts commit message
- Adds co-authorship: `Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>`

%%QA:tools:version-control%%
Git provides version control with main branch, Claude can create commits when explicitly requested, includes AI co-authorship attribution in commit messages.

---

## Diagnostic & Maintenance Tools

### 8. Vault Diagnostic Scripts

**Location**: `_scripts/`

**Available Tools**:

**vscan (vault_scan.py)**
- **Purpose**: Anti-duplication check before note creation
- **Command**: `vscan "search term"`
- **Checks**: Exact matches, alias matches, fuzzy suggestions

**orphan (orphan_check.py)**
- **Purpose**: Find notes with insufficient connections
- **Protocol**: ≥2 incoming + ≥2 outgoing links
- **Command**: `orphan`

**linkcheck (link_check.py)**
- **Purpose**: Identify broken [[Wiki-Links]]
- **Protocol**: Zero broken links allowed
- **Command**: `linkcheck`

**metaudit (meta_audit.py)**
- **Purpose**: Validate YAML frontmatter compliance
- **Requirements**: tags, aliases, status, certainty fields
- **Command**: `metaudit`

**Status**: ✅ All production ready

%%QA:tools:diagnostic-scripts%%
Four diagnostic scripts (vscan, orphan, linkcheck, metaudit) ensure vault health through anti-duplication checks, graph connectivity monitoring, link validation, and metadata compliance.

---

## Formatting & Styling

### 9. Custom Theme: Pur3v4d3r Imperial

**Location**: `.obsidian/themes/pur3v4d3r-imperial/`

**Version**: v0.5.0 (850 lines, Phases 1-4 complete)

**Color Scheme**:
- **Primary**: Red (#E50000)
- **Secondary**: Grey (#E0E0E0)
- **Background**: Black (#0A0A0A)

**Features Implemented**:
- Code blocks with dual-color borders
- Card elevated callouts with 3D shadows
- Ordered/unordered list styling
- Tables with red gradient headers
- Horizontal rules (minimalist thin red)
- Tags system (pill-shaped, 6 categories)

**Design Philosophy**:
- Zero animations (performance-focused)
- Dark mode only
- Source/Live Preview priority
- Zero `!important` flags in theme (uses theme authority)

%%QA:tools:custom-theme%%
Custom theme Pur3v4d3r Imperial uses red/grey/black color scheme, 850 lines consolidated from 52 CSS snippets, implements code blocks, callouts, lists, tables, and tags with performance-focused design.

---

## Technology Integration Map

```
┌─────────────────────────────────────────────────────────────┐
│                      USER INTERACTION                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Obsidian    │  │  VS Code     │  │ Claude       │      │
│  │  (Editing)   │  │  (Coding)    │  │ Desktop      │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
└─────────┼──────────────────┼──────────────────┼──────────────┘
          │                  │                  │
          ▼                  ▼                  ▼
┌─────────────────────────────────────────────────────────────┐
│                    VAULT FILESYSTEM                         │
│  D:\10_pur3v4d3r's-vault\                                   │
│  ├── .obsidian/      (Obsidian config)                     │
│  ├── .smart-env/     (Smart Connections embeddings)        │
│  ├── .claude/        (Agent memory layer)                  │
│  ├── 00-meta/        (Authoritative metadata)              │
│  ├── 01-07/          (Content organization)                │
│  └── __LOCAL-REPO/   (External examples)                   │
└─────────────────────────────────────────────────────────────┘
          │                  │                  │
          ▼                  ▼                  ▼
┌─────────────────────────────────────────────────────────────┐
│                    AUTOMATION LAYER                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Smart Conn.  │  │  Dataview    │  │ Templater    │      │
│  │ (Embeddings) │  │  (Queries)   │  │ (Templates)  │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
└─────────┼──────────────────┼──────────────────┼──────────────┘
          │                  │                  │
          ▼                  ▼                  ▼
┌─────────────────────────────────────────────────────────────┐
│                    INTELLIGENCE LAYER                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ MCP Server   │  │  Claude AI   │  │  Gemini AI   │      │
│  │ (Retrieval)  │  │  (Reasoning) │  │  (Execution) │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

%%QA:architecture:integration-map%%
Technology integration spans four layers: User Interaction (Obsidian/VS Code/Claude Desktop), Vault Filesystem (local storage), Automation Layer (Smart Connections/Dataview/Templater), and Intelligence Layer (MCP/Claude/Gemini).

---

## Technology Decision Rationale

### Why Obsidian?

**Chosen For**:
- ✅ Local-first storage (data ownership)
- ✅ Markdown format (future-proof, portable)
- ✅ Extensive plugin ecosystem
- ✅ Graph view for knowledge connections
- ✅ Active community and development

**Trade-offs**:
- ⚠️ Desktop-only (no native web interface)
- ⚠️ Plugin conflicts possible
- ⚠️ Sync requires separate solution

### Why Smart Connections?

**Chosen For**:
- ✅ Local embedding model (no API costs, privacy)
- ✅ Automatic indexing (no manual triggers)
- ✅ MCP integration available
- ✅ Semantic search beyond keywords

**Trade-offs**:
- ⚠️ 30-second embedding latency
- ⚠️ Requires Obsidian running
- ⚠️ Limited to 384 dimensions (vs 1536 for OpenAI)

### Why MCP?

**Chosen For**:
- ✅ Standardized protocol for agent tools
- ✅ Anthropic official support
- ✅ Extensible to multiple agents
- ✅ Smart Connections integration exists

**Trade-offs**:
- ⚠️ Configuration complexity
- ⚠️ Claude Desktop dependency
- ⚠️ Windows path escaping issues (JSON)

%%QA:architecture:technology-decisions%%
Technology choices prioritize local-first storage (Obsidian), privacy (local embeddings), and agent integration (MCP protocol), accepting trade-offs like desktop-only interface and configuration complexity.

---

## Related Memories

- [[projectbrief]] — Strategic context for technology choices
- [[systemPatterns]] — Architectural patterns these technologies enable
- [[activeContext]] — Current technology configuration tasks
- [[progress]] — Technology implementation timeline
- [[memory-index]] — Navigation hub

---

## Query Anchors Summary

This document contains query anchors for:
- `%%QA:tools:*%%` — All technology configurations
- `%%QA:workflow:*%%` — Integration patterns
- `%%QA:architecture:*%%` — System design rationale

---

## Document History

- **2026-01-06**: Initial creation during Phase 1 foundation setup
- **Current Status**: Active, evolving as new technologies are added

---

_This is a living document. Update when technologies are added, removed, or reconfigured._
