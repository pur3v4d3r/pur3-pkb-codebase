---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "FastMCP"
aliases:
  - "FastMCP"
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
  - priority/low
  - year/2025
  - artificial-intelligence
  - prompt-engineering
  - productivity

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
  - "reference-comprehensive-mcp-servers-2025122412"
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
  - "[[Comprehensive-Refernece-MCP-Servers|**Comprehensive Refernece: MCP Servers**]]"
  - "[[API-Fundamentals|API Fundamentals]]"
  - "[[JSON-RPC]]"
  - "[[AI-Agent-Architecture|AI Agent Architecture]]"
  - "[[Custom-MCP-Server-Development|Custom MCP Server Development]]"
  - "[[AI-PKB-Integration|AI-PKB Integration]]"
  - "[[Prompt-Library-Management|Prompt Library Management]]"
  - "[[Claude-Code-Workflows|Claude Code Workflows]]"
  - "[[Gemini-Code-Assist|Gemini Code Assist]]"
  - "[[Obsidian-Automation|Obsidian Automation]]"
  - "[[Claude-Code|Claude Code]]"
  - "[[Obsidian]]"
  - "[[Prompt-Engineering|Prompt Engineering]]"
  - "[[AI-Agents|AI Agents]]"
  - "[[Claude-Desktop|Claude Desktop]]"

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

# FastMCP

> [!definition] **FastMCP** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> <span style='color: #72FFF1;'>**FastMCP**</span> is a high-level Python framework that handles protocol complexities, letting developers focus on tool logic rather than JSON-RPC implementation.

## Core Explanation

> [!evidence] Supporting Evidence *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> MCP’s design allows **semantic context routing**—e.g., an AI can request “all prompts tagged #cognitive-load” via `prompt://tag/cognitive-load`.^observed-in-practice

> [!evidence] Supporting Evidence *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> Composable architecture allows **incremental adoption**—start with files, add git, then custom resources.^established

> [!analytical-insight] Key Insight *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> %%evidence: consensus%%
> MCP was <span style='color: #FF5700;'>open-sourced by Anthropic in November 2024</span> and subsequently donated to the <span style='color: #FFC700;'>Agentic AI Foundation (AAIF)</span> under the Linux Foundation (December 2025). The foundation includes governance participation from Anthropic, OpenAI, Google, Microsoft, AWS, Cloudflare, and Bloomberg—signaling industry-wide adoption of this standard.

> [!analytical-insight] Key Insight *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> %%confidence: verified%%
> The critical distinction: <span style='color: #FF00DC;'>Tools perform actions</span> (side effects), while <span style='color: #27FF00;'>Resources provide data</span> (read-only). Resources support real-time updates via `notifications/resources/list_changed` and `resources/subscribe`.

> [!analytical-insight] Key Insight *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> %%evidence: multiple-studies%%
> MCP servers enable <span style='color: #FFC700;'>unprecedented integration between AI assistants and Personal Knowledge Bases</span>, transforming static note repositories into dynamic, AI-augmented knowledge systems.

> [!analytical-insight] Key Insight *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> %%evidence: multiple-studies%%
> MCP servers transform prompt libraries from static file collections into <span style='color: #FFC700;'>dynamic, version-controlled, instantly-executable systems</span>.

> [!analytical-insight] Key Insight *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> %%confidence: confident%%
> Separating prompts from application code enables:
> - <span style='color: #27FF00;'>Independent iteration</span>: Modify prompts without code deployments
> - <span style='color: #27FF00;'>A/B testing</span>: Version-controlled experiments
> - <span style='color: #27FF00;'>Team collaboration</span>: Shared prompt libraries
> - <span style='color: #27FF00;'>Quality gates</span>: Enforce standards before execution

> [!analytical-insight] Key Insight *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> MCP enables **federated context aggregation**, where multiple servers (local, remote, cloud) are chained to form a unified knowledge layer.^established

> [!analytical-insight] Key Insight *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> A **personal knowledge server** can expose:
> - `pkb://daily-notes` → Obsidian vault
> - `prompt://library/v3` → JSON prompt library
> - `agent://claude/state` → AI agent status^verified

> [!analytical-insight] Key Insight *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> You can **bridge** MCP to Claude/Gemini by building a VS Code extension that:
> 1. Connects to MCP server
> 2. Fetches relevant context
> 3. Injects it into the AI prompt before submission^feasible

## Practical Implications

> [!example] **Application**
> *Describe how this concept applies in practice.*

> [!warning] **Key Distinction** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> <span style='color: #FF00DC;'>Gemini Code Assist MCP support is currently limited to VS Code.</span> IntelliJ integration is not available. Android Studio has separate MCP configuration through Settings → Tools → Gemini → MCP Servers.

> [!warning] **Key Distinction** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> %%evidence: single-study%%
> Security research shows tool poisoning is <span style='color: #FF00DC;'>alarmingly common</span> in MCP ecosystems. "Rug pull" scenarios occur when legitimate tools are updated with malicious content post-approval.

> [!warning] **Key Distinction** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> %%evidence: single-study%%
> Research found <span style='color: #FF00DC;'>43% of analyzed MCP servers had command injection flaws</span>—unescaped input in tools with execution capabilities, particularly dangerous with direct user input.

> [!warning] **Key Distinction** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> Broad scopes granted upfront (`files:*`, `db:*`, `admin:*`) expand the blast radius from compromised tokens and complicate revocation.

> [!warning] **Key Distinction** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> <span style='color: #FF00DC;'>STDIO servers must NEVER write to stdout</span>—this corrupts JSON-RPC communication. Use stderr for logging or dedicated log files.

> [!warning] **Key Distinction** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> **Next Review**: `= this.next-review` | **Review Count**: `= this.review-count`
> **Review Status**: `= choice(this.next-review < date(today), "🔴 OVERDUE", choice(this.next-review = date(today), "🟡 Due Today", choice(dateformat(this.next-review, "yyyy-MM-dd") <= dateformat(date(today) + dur(7 days), "yyyy-MM-dd"), "🟢 This Week", "⚪ Scheduled")))`
> **Days Until Review**: `= choice(this.next-review, (this.next-review - date(today)).days + " days", "Not scheduled")`

> [!warning] **Key Distinction** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> No official security model yet—assume all MCP connections are **trusted**. Avoid exposing servers externally.^provisional

> [!warning] **Key Distinction** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> VS Code does **not yet auto-inject** MCP context into AI assistants. Requires custom extension.^verified

> [!warning] **Key Distinction** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> **No existing extension** provides this bridge. You must build or commission one.^established

## Concrete Examples

> [!example] **The Integration Problem Solved** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> **Before MCP:**
> - Claude Desktop + GitHub = Custom integration #1
> - Claude Desktop + Slack = Custom integration #2
> - Cursor + GitHub = Custom integration #3 (different code!)
> - Each pair requires unique implementation, testing, maintenance
> 
> **After MCP:**
> - GitHub MCP Server (built once)
> - Slack MCP Server (built once)
> - Any MCP client (Claude, Cursor, custom agents) connects to any server
> - N servers + M clients = N+M components (not N×M)

> [!example] **Tool Use Cases** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> - <span style='color: #72FFF1;'>File operations</span>: Create, read, update, delete files
> - <span style='color: #72FFF1;'>API calls</span>: Weather queries, database operations
> - <span style='color: #72FFF1;'>System commands</span>: Git operations, shell execution
> - <span style='color: #72FFF1;'>Service integrations</span>: Send emails, create tickets, post messages

> [!example] **Prompt Template** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> ```json
> {
>   "name": "summarize_issues",
>   "description": "Summarize recent GitHub issues",
>   "arguments": [
>     { "name": "project", "required": true },
>     { "name": "milestone", "required": false }
>   ]
> }
> ```
> User invokes: `/summarize_issues project=my-repo milestone=v2.0`

> [!example] **~/.claude.json Configuration** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> ```json
> {
>   "mcpServers": {
>     "github": {
>       "command": "npx",
>       "args": ["-y", "@modelcontextprotocol/server-github"],
>       "env": {
>         "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxxxxxxxxxxx"
>       }
>     },
>     "obsidian": {
>       "command": "uvx",
>       "args": ["mcp-obsidian"],
>       "env": {
>         "OBSIDIAN_API_KEY": "your_api_key",
>         "OBSIDIAN_HOST": "localhost",
>         "OBSIDIAN_PORT": "27124"
>       }
>     },
>     "perplexity": {
>       "command": "npx",
>       "args": ["-y", "perplexity-mcp"],
>       "env": {
>         "PERPLEXITY_API_KEY": "pplx_xxxxxxxxxxxx"
>       }
>    …

> [!example] **cyanheads/obsidian-mcp-server** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> **Capabilities:**
> - `read_note`: Retrieve note content with metadata
> - `write_note`: Create/update notes with YAML frontmatter support
> - `search`: Full-text and semantic search across vault
> - `manage_tags`: Bulk tag operations and cleanup
> - `list_files`: Directory traversal with filtering
> - `delete_file`: Safe note deletion
> 
> **Requirements:**
> - Obsidian "Local REST API" community plugin enabled
> - API key generated from plugin settings

> [!example] **Rapid Iteration Workflow** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> ```
> User: "The code_review prompt is too verbose"
> Claude: [Updates prompt via prompt_manager tool]
> User: "Test it"
> Claude: [Runs updated version instantly via prompt_engine]
> User: "Better—commit this version"
> Claude: [Git commits the change with version tag]
> ```

> [!example] **Basic FastMCP Server** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> ```python
> from fastmcp import FastMCP
> 
> # Create server
> mcp = FastMCP("My Server Name")
> 
> # Add tool
> @mcp.tool()
> def add(a: int, b: int) -> int:
>     """Add two numbers"""
>     return a + b
> 
> # Add static resource
> @mcp.resource("config://version")
> def get_version() -> str:
>     """Get server version"""
>     return "1.0.0"
> 
> # Add dynamic resource with template
> @mcp.resource("greeting://{name}")
> def get_greeting(name: str) -> str:
>     """Get personalized greeting"""
>     return f"Hello, {name}!"
> 
> # Add prompt
> @mcp.prompt()
> def greet_user(name: str, style: str = "friendly") -> str:
>     """Generate…

> [!example] **Sample Configuration for Filesystem & Search** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> ```json
> {
>   "mcpServers": {
>     "filesystem": {
>       "command": "npx",
>       "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/your/obsidian/vault"]
>     },
>     "brave-search": {
>       "command": "npx",
>       "args": ["-y", "@modelcontextprotocol/server-brave-search"],
>       "env": { "BRAVE_API_KEY": "YOUR_KEY_HERE" }
>     }
>   }
> }
> 
> ```

> [!example] **Untitled** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> After connection, you can browse:
> - `pkb://Projects/Neuroscience.md`
> - `prompt://repo/classification-v2.json`

## Connections & Context

**Cross-report connections** *(from [[reference-comprehensive-mcp-servers-2025122412]])*:
- [[Claude-Code|Claude Code]]
- [[Obsidian]]
- [[Prompt-Engineering|Prompt Engineering]]
- [[AI-Agent-Architecture|AI Agent Architecture]]
- [[JSON-RPC]]
- [[API-Design-Patterns|API Design Patterns]]

**Cross-report connections** *(from [[reference-comprehensive-mcp-servers-2025122412]])*:
- [[Personal-Knowledge-Base|Personal Knowledge Base]]
- [[Prompt-Engineering|Prompt Engineering]]
- [[Cognitive-Load-Theory|Cognitive Load Theory]]
- [[VS-Code|VS Code]]
- [[Claude-Code|Claude Code]]
- [[Gemini-Code-Assist|Gemini Code Assist]]

**Related concepts:**
[[Comprehensive-Refernece-MCP-Servers|**Comprehensive Refernece: MCP Servers**]] · [[API-Fundamentals|API Fundamentals]] · [[JSON-RPC]] · [[AI-Agent-Architecture|AI Agent Architecture]] · [[Custom-MCP-Server-Development|Custom MCP Server Development]] · [[AI-PKB-Integration|AI-PKB Integration]] · [[Prompt-Library-Management|Prompt Library Management]] · [[Claude-Code-Workflows|Claude Code Workflows]] · [[Gemini-Code-Assist|Gemini Code Assist]] · [[Obsidian-Automation|Obsidian Automation]] · [[Claude-Code|Claude Code]] · [[Gemini-Code-Assist|Gemini Code Assist]] · [[Obsidian]] · [[Prompt-Engineering|Prompt Engineering]] · [[AI-Agents|AI Agents]] · [[Claude-Code|Claude Code]] · [[Claude-Desktop|Claude Desktop]] · [[Claude-Code|Claude Code]] · [[Gemini-Code-Assist|Gemini Code Assist]] · [[Obsidian]] · [[Dataview]] · [[Templater]] · [[Unix-Philosophy|Unix Philosophy]] · [[API-Design-Patterns|API Design Patterns]] · [[Knowledge-Graph-Theory|Knowledge Graph Theory]] · [[Cognitive-Load-Theory|Cognitive Load Theory]] · [[Claude-Code|Claude Code]] · [[Obsidian]] · [[Prompt-Engineering|Prompt Engineering]] · [[AI-Agent-Architecture|AI Agent Architecture]]

**Related concepts** *(from reference-comprehensive-mcp-servers-2025122412.md)*:
[[API-Fundamentals|API Fundamentals]] * [[AI-Agent-Architecture|AI Agent Architecture]] * [[Custom-MCP-Server-Development|Custom MCP Server Development]] * [[AI-PKB-Integration|AI-PKB Integration]] * [[Prompt-Library-Management|Prompt Library Management]] * [[Claude-Code-Workflows|Claude Code Workflows]] * [[Gemini-Code-Assist|Gemini Code Assist]] * [[Obsidian-Automation|Obsidian Automation]] * [[Claude-Code|Claude Code]] * [[Prompt-Engineering|Prompt Engineering]] * [[AI-Agents|AI Agents]] * [[Claude-Desktop|Claude Desktop]] * [[Unix-Philosophy|Unix Philosophy]] * [[API-Design-Patterns|API Design Patterns]] * [[Knowledge-Graph-Theory|Knowledge Graph Theory]] * [[Cognitive-Load-Theory|Cognitive Load Theory]] * [[MCP-Tools|MCP Tools]] * [[MCP-Resources|MCP Resources]] * [[MCP-Prompts|MCP Prompts]] * [[MCP-Security-Best-Practices|MCP Security Best Practices]] * [[Obsidian-MCP-Integration|Obsidian MCP Integration]] * [[Zettelkasten|Zettelkasten]] * [[Spaced-Repetition|Spaced Repetition]] * [[PARA-Method|PARA Method]] * [[FastMCP-Development-Guide|FastMCP Development Guide]] * [[Python-Fundamentals|Python Fundamentals]] * [[Async-Programming|Async Programming]] * [[MCP-Security-Hardening|MCP Security Hardening]] * [[Docker-Fundamentals|Docker Fundamentals]] * [[Network-Security-Basics|Network Security Basics]]

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

**Related concepts** *(from [[reference-comprehensive-mcp-servers-2025122412]])*:
[[API-Fundamentals|API Fundamentals]] * [[AI-Agent-Architecture|AI Agent Architecture]] * [[Custom-MCP-Server-Development|Custom MCP Server Development]] * [[AI-PKB-Integration|AI-PKB Integration]] * [[Prompt-Library-Management|Prompt Library Management]] * [[Claude-Code-Workflows|Claude Code Workflows]] * [[Gemini-Code-Assist|Gemini Code Assist]] * [[Obsidian-Automation|Obsidian Automation]] * [[Claude-Code|Claude Code]] * [[Prompt-Engineering|Prompt Engineering]] * [[AI-Agents|AI Agents]] * [[Claude-Desktop|Claude Desktop]] * [[Unix-Philosophy|Unix Philosophy]] * [[API-Design-Patterns|API Design Patterns]] * [[Knowledge-Graph-Theory|Knowledge Graph Theory]] * [[Cognitive-Load-Theory|Cognitive Load Theory]] * [[MCP-Tools|MCP Tools]] * [[MCP-Resources|MCP Resources]] * [[MCP-Prompts|MCP Prompts]] * [[MCP-Security-Best-Practices|MCP Security Best Practices]] * [[Obsidian-MCP-Integration|Obsidian MCP Integration]] * [[Spaced-Repetition|Spaced Repetition]] * [[PARA-Method|PARA Method]] * [[FastMCP-Development-Guide|FastMCP Development Guide]] * [[Python-Fundamentals|Python Fundamentals]] * [[Async-Programming|Async Programming]] * [[MCP-Security-Hardening|MCP Security Hardening]] * [[Docker-Fundamentals|Docker Fundamentals]] * [[Network-Security-Basics|Network Security Basics]] * [[AI-Augmented-Zettelkasten|AI-Augmented Zettelkasten]]

**Cross-report connections** *(from [[reference-comprehensive-mcp-servers-2025122412]])*:
- [[Claude-Code|Claude Code]]
- [[Obsidian|Obsidian]]
- [[Prompt-Engineering|Prompt Engineering]]
- [[AI-Agent-Architecture|AI Agent Architecture]]
- [[JSON-RPC|JSON-RPC]]

**Cross-report connections** *(from [[reference-comprehensive-mcp-servers-2025122412]])*:
- [[Personal-Knowledge-Base|Personal Knowledge Base]]
- [[Prompt-Engineering|Prompt Engineering]]
- [[Cognitive-Load-Theory|Cognitive Load Theory]]
- [[VS-Code|VS Code]]
- [[Claude-Code|Claude Code]]

**Related concepts** *(from [[reference-comprehensive-mcp-servers-2025122412]])*:
[[API-Fundamentals|API Fundamentals]] * [[AI-Agent-Architecture|AI Agent Architecture]] * [[Custom-MCP-Server-Development|Custom MCP Server Development]] * [[AI-PKB-Integration|AI-PKB Integration]] * [[Prompt-Library-Management|Prompt Library Management]] * [[Claude-Code-Workflows|Claude Code Workflows]] * [[Gemini-Code-Assist|Gemini Code Assist]] * [[Obsidian-Automation|Obsidian Automation]] * [[Claude-Code|Claude Code]] * [[Prompt-Engineering|Prompt Engineering]] * [[AI-Agents|AI Agents]] * [[Claude-Desktop|Claude Desktop]] * [[Unix-Philosophy|Unix Philosophy]] * [[API-Design-Patterns|API Design Patterns]] * [[Knowledge-Graph-Theory|Knowledge Graph Theory]] * [[Cognitive-Load-Theory|Cognitive Load Theory]] * [[MCP-Tools|MCP Tools]] * [[MCP-Resources|MCP Resources]] * [[MCP-Prompts|MCP Prompts]] * [[MCP-Security-Best-Practices|MCP Security Best Practices]] * [[Obsidian-MCP-Integration|Obsidian MCP Integration]] * [[Spaced-Repetition|Spaced Repetition]] * [[PARA-Method|PARA Method]] * [[FastMCP-Development-Guide|FastMCP Development Guide]] * [[Python-Fundamentals|Python Fundamentals]] * [[Async-Programming|Async Programming]] * [[MCP-Security-Hardening|MCP Security Hardening]] * [[Docker-Fundamentals|Docker Fundamentals]] * [[Network-Security-Basics|Network Security Basics]] * [[AI-Augmented-Zettelkasten|AI-Augmented Zettelkasten]]

**Cross-report connections** *(from [[reference-comprehensive-mcp-servers-2025122412]])*:
- [[Claude-Code|Claude Code]]
- [[Obsidian|Obsidian]]
- [[Prompt-Engineering|Prompt Engineering]]
- [[AI-Agent-Architecture|AI Agent Architecture]]
- [[JSON-RPC|JSON-RPC]]

**Cross-report connections** *(from [[reference-comprehensive-mcp-servers-2025122412]])*:
- [[Personal-Knowledge-Base|Personal Knowledge Base]]
- [[Prompt-Engineering|Prompt Engineering]]
- [[Cognitive-Load-Theory|Cognitive Load Theory]]
- [[VS-Code|VS Code]]
- [[Claude-Code|Claude Code]]










## Methodology Notes

> [!methodology-and-sources] **Transport Mechanisms** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> MCP supports two primary transport protocols, each suited to different deployment scenarios:

> [!methodology-and-sources] **Configuration File Paths** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> | Platform | Primary Config | Alternative |
> |----------|---------------|-------------|
> | macOS | `~/.claude.json` | `~/Library/Application Support/Claude/claude_desktop_config.json` |
> | Windows | `%APPDATA%\Claude\claude_desktop_config.json` | — |
> | Project-specific | `.mcp.json` (project root) | Highest priority |

> [!methodology-and-sources] **Verifying MCP Server Status** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> ```bash
> # Check server status interactively
> /mcp
> 
> # Debug mode for troubleshooting
> claude --debug
> 
> # View server logs (macOS)
> tail -f ~/Library/Logs/Claude/mcp-server-[name].log
> ```

> [!methodology-and-sources] **Manual Configuration Required** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> Unlike Claude Code, Gemini Code Assist <span style='color: #FF00DC;'>cannot configure MCP servers through command palette</span>—direct JSON editing is required.

> [!methodology-and-sources] **Multi-Vault Handling** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> For complex PKB structures with multiple vaults:
> - Configure separate MCP server instances per vault
> - Use vault-specific API keys and ports
> - Implement cross-vault search through aggregation layer

> [!methodology-and-sources] **Integrated Architecture Pattern** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> ```
> Obsidian Vault: /knowledge-base/
> ├── /prompts/          ← Prompt templates with metadata
> │   ├── code_review.md
> │   ├── summarize.md
> │   └── analyze.md
> ├── /projects/         ← Project documentation
> ├── /references/       ← Research and resources
> └── /meta/             ← Prompt performance notes
> 
> Prompt MCP Workspace: Points to /knowledge-base/prompts/
> Obsidian MCP: Points to /knowledge-base/
> 
> Both accessible simultaneously to Claude/Gemini
> ```

> [!methodology-and-sources] **Recommended Security Architecture** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> **Containerization**: Isolate MCP servers in Docker containers
> ```bash
> docker run --read-only --network=restricted mcp-server
> ```
> 
> **Network Limits**: Restrict egress, implement allowlists
> 
> **Resource Limits**: CPU, memory, execution time constraints
> 
> **Gateway/Middleware**: Policy enforcement layers (MCP Manager, Docker Gateway)
> - Intercept, scan, log all requests/responses
> - Verify signatures, redact secrets, restrict egress

> [!methodology-and-sources] **Untitled** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> **Research Methodology**
> 
> **Exploration Approach:** Tree-of-Thoughts depth-first search across 5 primary dimensions
> 
> **Total Searches:** 12 systematic web searches covering:
> - MCP architecture fundamentals
> - Claude Code integration specifics
> - Gemini Code Assist configuration
> - Obsidian MCP servers
> - Prompt management MCP tools
> - Security vulnerabilities and best practices
> - Custom server development (FastMCP, TypeScript SDK)
> 
> **Primary Sources:**
> - modelcontextprotocol.io (Official specification)
> - Anthropic documentation
> - GitHub repositories (modelcontextprotocol/*)
> - Security research…

> [!methodology-and-sources] **Untitled** *(from [[reference-comprehensive-mcp-servers-2025122412]])*
> **Research Methodology**
> - **Exploration tree**: 5 dimensions, 14 searches, depth-first traversal
> - **Total searches**: 14
> - **Primary sources**:
>   - [Anthem Engineering MCP GitHub](https://github.com/anthem-engineering/model-context-protocol)
>   - [MCP NPM Packages](https://www.npmjs.com/search?q=mcp)
>   - [VS Code Marketplace: MCP Extension](https://marketplace.visualstudio.com/items?itemName=AnthemLabs.mcp)
> - **Confidence distribution**:
>   - Fundamentals: ^high
>   - Implementation: ^high
>   - Claude/Gemini Integration: ^medium (workaround-dependent)
>   - PKB Applications: ^medium (emergent use…

---

## Source Attribution

**Extracted from:** [[reference-comprehensive-mcp-servers-2025122412]]
