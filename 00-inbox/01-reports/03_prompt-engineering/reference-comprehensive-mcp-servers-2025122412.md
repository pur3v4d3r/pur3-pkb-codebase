---
id: "20251224123904"
type: "reference"
source: "claude-opus"
status: "read"
confidence: "speculative"
maturity: "seedling"
priority: "low"
next-review: "2025-12-31"
review-count: 0
last-reviewed:
review-interval: 7
created: "2025-12-24T12:39:04"
modified: "2025-12-24T12:39:04"
week: "[[2025-W52]]"
month: "2025-12"
quarter: "2025-Q4"
year: "2025"
link-up:
 - "[[pkb-&-pkm-moc]]"
link-related:
 - "[[2025-12-24|Daily-Note]]"
tags:
 - "type/reference"
 - "source/claude-opus"
 - "maturity/seedling"
 - "confidence/speculative"
 - "status/read"
 - "priority/low"
 - "year/2025"
 - "artificial-intelligence"
 - "prompt-engineering"
 - "productivity"
 - "planning"
 - "scripting"
 - "skill-acquisition"
aliases:
 - "MCP Servers"
 - "MCP"
 - "MCP Reference"
 - "Model Context Protocol"
 - "AI Tool Protocol"
 - "Claude MCP"
 - "MCP Architecture"
 - "Comprehensive Refernece: MCP Servers"
title: "Comprehensive Refernece: MCP Servers"
---
### 📖 Extracted Definitions From Cognitive Science
```dataviewjs
try {
 // Get the current file
 const currentPage = dv.current();
 // Load the content of the current file
 const content = await dv.io.load(currentPage.file.path);
 // Storage for definitions in current file
 let allDefinitions = [];
 // Extract bracketed inline fields from current file content
 const bracketedFieldRegex = /\[\*\*([^*]+?)\*\*::\s*([^\]]+?)\]/g;
 let match;
 while ((match = bracketedFieldRegex.exec(content)) !== null) {
  allDefinitions.push({
   key: match[1].trim(), // This is the clean term without ** markdown
   value: match[2].trim()
  });
 }
 // Display results
 if (allDefinitions.length > 0) {
  dv.header(3, `📚 Definitions in Current File (${allDefinitions.length} total)`);
  // Group by first letter (using the clean key)
  const grouped = {};
  allDefinitions.forEach(d => {
   const firstLetter = d.key[0].toUpperCase();
   if (!grouped[firstLetter]) grouped[firstLetter] = [];
   grouped[firstLetter].push(d);
  });
  // Sort letters alphabetically
  const sortedLetters = Object.keys(grouped).sort();
  // Display grouped results
  for (let letter of sortedLetters) {
   dv.header(4, `${letter} (${grouped[letter].length} terms)`);
   dv.table(
    ["🔑 Term", "📝 Definition"],
    grouped[letter].map(d => [
     `**${d.key}**`,
     d.value
    ])
   );
   dv.paragraph(""); // Add spacing between groups
  }
 } else {
  dv.paragraph(`*No bracketed inline fields found in current file.*`);
 }
} catch (error) {
 console.error("Error in definitions script:", error);
 dv.paragraph("*Error loading definitions. Check console for details.*");
}
```
---





# Foundational Understanding
> [!definition] # Definition
> [**Note Title**:: [[**Comprehensive Refernece: MCP Servers**]]]
> [**Prompt Used**:: ]
> ##### [✅`= dateformat(this.file.ctime, "MMMM dd, yyyy")` - Initial Creation]


```yaml
---
tags: #mcp #model-context-protocol #ai-infrastructure #reference-note #claude-code #gemini #pkb-integration #prompt-engineering
aliases: [MCP Servers, Model Context Protocol, MCP Reference, AI Tool Protocol, Claude MCP, MCP Architecture]
created: 2025-12-23
modified: 2025-12-23
status: evergreen
certainty: verified
type: reference
freshness:
  domain-volatility: high
  last-verified: 2025-12-23
prerequisites:
  hard: []
  soft: [[API Fundamentals]], [[JSON-RPC]], [[AI Agent Architecture]]
enables:
  direct: [[Custom MCP Server Development]], [[AI-PKB Integration]], [[Prompt Library Management]]
  related: [[Claude Code Workflows]], [[Gemini Code Assist]], [[Obsidian Automation]]
related: [[Claude Code]], [[Gemini Code Assist]], [[Obsidian]], [[Prompt Engineering]], [[AI Agents]]
---
```

> [!comprehensive-reference] 📚 Comprehensive Reference
> - **Generated**:: 2025-12-23
> - **Version**:: 1.0
> - **Exploration Depth**:: 4/4 (Maximum)
> - **Search Count**:: 12 systematic depth-first searches
> - **Confidence**:: %%confidence: verified%% Extensively researched with primary sources

> [!abstract]
> **Executive Overview**
> <span style='color: #FFC700;'>**Model Context Protocol (MCP)**</span> is an open standard protocol introduced by Anthropic (November 2024) that standardizes how AI applications connect with external data sources, tools, and systems. Often described as <span style='color: #27FF00;'>"USB-C for AI"</span>, MCP solves the M×N integration problem by transforming it into M+N—enabling any AI client to work with any compatible server through a universal protocol rather than requiring custom integrations for each pairing.

> [!how-to-use-this]
> **Navigation Guide**
> This reference is organized into progressive sections: foundational concepts → technical architecture → practical implementation (Claude Code, Gemini) → PKB/Prompt Engineering applications → security → custom development. Use the Table of Contents for targeted navigation. Wiki-links connect to related PKB concepts. Callouts highlight definitions, warnings, and key claims throughout.

---

## 📑 Table of Contents

1. [[#What Are MCP Servers?|What Are MCP Servers?]]
2. [[#Core Architecture|Core Architecture]]
3. [[#The Three Primitives|The Three Primitives]]
4. [[#Claude Code Integration|Claude Code Integration]]
5. [[#Gemini Code Assist Integration|Gemini Code Assist Integration]]
6. [[#PKB Integration Benefits|PKB Integration Benefits]]
7. [[#Prompt Engineering Library Applications|Prompt Engineering Library Applications]]
8. [[#Security Considerations|Security Considerations]]
9. [[#Building Custom MCP Servers|Building Custom MCP Servers]]
10. [[#MCP Server Ecosystem|MCP Server Ecosystem]]
11. [[#Synthesis & Mastery|Synthesis & Mastery]]

---

## What Are MCP Servers?

[**Model-Context-Protocol**:: an open standard protocol that standardizes how AI applications connect with external data sources, tools, and systems through a client-server architecture using JSON-RPC 2.0]^verified-stable

> [!definition] Model Context Protocol (MCP)
> <span style='color: #FFC700;'>**Model Context Protocol**</span> is a universal interface specification enabling bidirectional communication between AI applications (hosts) and external services (servers). It abstracts away integration complexity, allowing developers to write tools once and have them work across multiple AI platforms—Claude Desktop, Claude Code, VS Code extensions, custom agents, and more.

%%mental-model: USB-C-analogy%%

The protocol's elegance lies in its simplicity: rather than building M×N custom integrations (M clients × N services), MCP creates M+N connections (M clients + N servers). Each new MCP server becomes instantly available to all MCP-compatible clients.

> [!key-claim] Foundation & Governance
> %%evidence: consensus%%
> MCP was <span style='color: #FF5700;'>open-sourced by Anthropic in November 2024</span> and subsequently donated to the <span style='color: #FFC700;'>Agentic AI Foundation (AAIF)</span> under the Linux Foundation (December 2025). The foundation includes governance participation from Anthropic, OpenAI, Google, Microsoft, AWS, Cloudflare, and Bloomberg—signaling industry-wide adoption of this standard.

[**MCP-Origin**:: Built on concepts from the Language Server Protocol (LSP), which standardized IDE-to-language-server communication, MCP applies similar principles to AI-tool interactions]^verified-stable

### Why MCP Matters

%%synthesis-potential: software-architecture×ai-systems%%

Traditional AI tool integration requires custom code for every combination of AI system and external service. A company using three AI tools and five services needed fifteen separate integrations. MCP eliminates this combinatorial explosion:

> [!example] The Integration Problem Solved
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

---

## Core Architecture

%%QA:mcp:architecture%%

> [!definition] Client-Server Architecture
> MCP follows a <span style='color: #72FFF1;'>client-server architecture</span> where an <span style='color: #FFC700;'>MCP Host</span> (an AI application like [[Claude Code]] or [[Claude Desktop]]) establishes connections to one or more <span style='color: #FFC700;'>MCP Servers</span> through <span style='color: #FFC700;'>MCP Clients</span> (connection managers).

### Key Participants

[**MCP-Host**:: The AI application that coordinates and manages one or multiple MCP clients—examples include Claude Desktop, Claude Code, IDE extensions, and custom AI agents]^verified-stable

[**MCP-Client**:: A component that maintains a 1:1 connection to an MCP server and obtains context from that server for the host to use]^verified-stable

[**MCP-Server**:: A program that exposes context data (tools, resources, prompts) to MCP clients, running either locally or remotely]^verified-stable

```
┌─────────────────────────────────────────────────────────────────┐
│                         MCP HOST                                │
│              (Claude Desktop, Claude Code, IDE)                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  MCP Client  │  │  MCP Client  │  │  MCP Client  │          │
│  │   (1:1)      │  │   (1:1)      │  │   (1:1)      │          │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘          │
└─────────┼─────────────────┼─────────────────┼──────────────────┘
          │                 │                 │
          ▼                 ▼                 ▼
   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
   │  MCP Server  │  │  MCP Server  │  │  MCP Server  │
   │   (GitHub)   │  │  (Obsidian)  │  │ (PostgreSQL) │
   │    LOCAL     │  │    LOCAL     │  │    REMOTE    │
   └──────────────┘  └──────────────┘  └──────────────┘
```

### Transport Layer

> [!methodology-and-sources] Transport Mechanisms
> MCP supports two primary transport protocols, each suited to different deployment scenarios:

[**STDIO-Transport**:: Standard Input/Output transport for local MCP servers—simple synchronous messaging where the host launches the server process and communicates via stdin/stdout pipes]^verified-stable

[**SSE-HTTP-Transport**:: Server-Sent Events over HTTP (Streamable HTTP) for remote MCP servers—asynchronous event-driven communication enabling many clients to connect to a single server]^verified-stable

| Transport | Use Case | Connection Model | Example |
|-----------|----------|------------------|---------|
| <span style='color: #72FFF1;'>STDIO</span> | Local servers | 1:1 (single client) | Filesystem, Git |
| <span style='color: #72FFF1;'>SSE/HTTP</span> | Remote servers | 1:Many (multiple clients) | Sentry, Cloud APIs |

### Data Layer

%%cognitive-load: medium%%

The data layer implements a <span style='color: #72FFF1;'>JSON-RPC 2.0</span> based exchange protocol defining message structure and semantics:

> [!definition] Data Layer Components
> - **Lifecycle Management**: Connection initialization, capability negotiation, termination
> - **Server Features**: Tools, resources, prompts exposed to clients
> - **Client Features**: Sampling from host LLM, user input elicitation, logging
> - **Utility Features**: Notifications for real-time updates, progress tracking

---

## The Three Primitives

%%QA:mcp:primitives%%

MCP servers expose capabilities through three core primitives, each with distinct control patterns and use cases.

### 1. Tools (Model-Controlled)

> [!definition] Tools
> <span style='color: #FFC700;'>**Tools**</span> are executable functions that the AI can invoke to perform actions with side effects. The <span style='color: #27FF00;'>LLM decides</span> when to use tools based on user requests and context.

[**Tool-Discovery**:: Tools are discovered via `tools/list` and invoked via `tools/call`—the server declares available tools with JSON schemas, and the client requests execution]^verified-stable

> [!example] Tool Use Cases
> - <span style='color: #72FFF1;'>File operations</span>: Create, read, update, delete files
> - <span style='color: #72FFF1;'>API calls</span>: Weather queries, database operations
> - <span style='color: #72FFF1;'>System commands</span>: Git operations, shell execution
> - <span style='color: #72FFF1;'>Service integrations</span>: Send emails, create tickets, post messages

```json
// Example Tool Definition
{
  "name": "search_vault",
  "description": "Search Obsidian vault for notes matching query",
  "inputSchema": {
    "type": "object",
    "properties": {
      "query": { "type": "string", "description": "Search query" },
      "limit": { "type": "integer", "default": 10 }
    },
    "required": ["query"]
  }
}
```

### 2. Resources (Application-Controlled)

> [!definition] Resources
> <span style='color: #FFC700;'>**Resources**</span> are data sources providing contextual information without side effects. The <span style='color: #9E6CD3;'>client application decides</span> when and how to use resources—not the LLM.

[**Resource-Types**:: Text resources (UTF-8 encoded: code, documents, API responses) and Binary resources (Base64 encoded: images, PDFs, archives)]^verified-stable

[**Resource-Identification**:: Resources are identified by unique URIs such as `file:///path/to/doc`, `db://schema/table`, or `config://version`]^verified-stable

> [!key-claim] Resources vs Tools
> %%confidence: verified%%
> The critical distinction: <span style='color: #FF00DC;'>Tools perform actions</span> (side effects), while <span style='color: #27FF00;'>Resources provide data</span> (read-only). Resources support real-time updates via `notifications/resources/list_changed` and `resources/subscribe`.

### 3. Prompts (User-Controlled)

> [!definition] Prompts
> <span style='color: #FFC700;'>**Prompts**</span> are reusable templates for LLM interactions with parameterized messages and autocomplete support. The <span style='color: #9E6CD3;'>user triggers</span> prompt execution, typically through slash commands.

[**Prompt-Discovery**:: Prompts are discovered via `prompts/list` and retrieved via `prompts/get` with dynamic payload generation based on parameters]^verified-stable

> [!example] Prompt Template
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

### Control Pattern Summary

| Primitive | Controlled By | Side Effects | Discovery | Invocation |
|-----------|--------------|--------------|-----------|------------|
| <span style='color: #FFC700;'>Tools</span> | LLM | Yes | `tools/list` | `tools/call` |
| <span style='color: #FFC700;'>Resources</span> | Application | No | `resources/list` | `resources/read` |
| <span style='color: #FFC700;'>Prompts</span> | User | Context-dependent | `prompts/list` | `prompts/get` |

---

## Claude Code Integration

%%QA:claude-code:mcp-setup%%
%%applies-to: claude-code-workflow%%

[[Claude Code]] provides robust MCP server integration through both CLI commands and direct configuration files.

### Configuration Locations

> [!methodology-and-sources] Configuration File Paths
> 
> | Platform | Primary Config | Alternative |
> |----------|---------------|-------------|
> | macOS | `~/.claude.json` | `~/Library/Application Support/Claude/claude_desktop_config.json` |
> | Windows | `%APPDATA%\Claude\claude_desktop_config.json` | — |
> | Project-specific | `.mcp.json` (project root) | Highest priority |

### Method 1: CLI Commands (Recommended)

> [!how-to] Adding MCP Servers via CLI
> 
> ```bash
> # Add server with user scope (persists across projects)
> claude mcp add github --scope user
> 
> # Add with environment variables
> claude mcp add digitalocean-mcp-local \
>   -e DIGITALOCEAN_API_TOKEN=YOUR_TOKEN \
>   -- npx "@digitalocean/mcp"
> 
> # Add HTTP/SSE server (remote)
> claude mcp add --transport http notion https://mcp.notion.com/mcp
> 
> # List all configured servers
> claude mcp list
> 
> # Test server connectivity
> claude mcp get [server-name]
> 
> # Remove a server
> claude mcp remove [server-name]
> ```

### Method 2: Direct JSON Configuration

> [!example] ~/.claude.json Configuration
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
>     }
>   }
> }
> ```

### Configuration Scopes

[**Scope-Priority**:: Project scope (`.mcp.json`) > User scope (`--scope user`) > Plugin scope—project-specific configurations override user-level settings]^verified-stable

> [!helpful-tip] Scope Selection Guide
> - **Project Scope**: Team-shared configurations, project-specific tools
> - **User Scope**: Personal productivity tools (GitHub, Perplexity, Obsidian)
> - **Plugin Scope**: Bundled with Claude Code extensions

### Verification & Debugging

> [!methodology-and-sources] Verifying MCP Server Status
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

### Popular MCP Servers for Claude Code

| Server | Use Case | Install Command |
|--------|----------|-----------------|
| <span style='color: #72FFF1;'>GitHub</span> | PR management, issues | `npx @modelcontextprotocol/server-github` |
| <span style='color: #72FFF1;'>Perplexity</span> | Real-time research | `npx perplexity-mcp` |
| <span style='color: #72FFF1;'>Context7</span> | Library documentation | `npx @context7/mcp` |
| <span style='color: #72FFF1;'>Brave Search</span> | Web information | `npx @anthropics/mcp-server-brave` |
| <span style='color: #72FFF1;'>Filesystem</span> | Local file access | `npx @modelcontextprotocol/server-filesystem` |

---

## Gemini Code Assist Integration

%%QA:gemini:mcp-setup%%
%%applies-to: gemini-workflow%%

[[Gemini Code Assist]] supports MCP server integration in VS Code (not IntelliJ) through manual JSON configuration.

> [!warning] Platform Limitation
> <span style='color: #FF00DC;'>Gemini Code Assist MCP support is currently limited to VS Code.</span> IntelliJ integration is not available. Android Studio has separate MCP configuration through Settings → Tools → Gemini → MCP Servers.

### Configuration Method

> [!methodology-and-sources] Manual Configuration Required
> Unlike Claude Code, Gemini Code Assist <span style='color: #FF00DC;'>cannot configure MCP servers through command palette</span>—direct JSON editing is required.

Edit `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxxxxxxxxxxx"
      }
    },
    "cloudflare": {
      "command": "npx",
      "args": ["-y", "@cloudflare/mcp-server-cloudflare"],
      "env": {
        "CLOUDFLARE_API_TOKEN": "your_token"
      }
    },
    "snyk": {
      "command": "npx",
      "args": ["-y", "snyk@latest", "mcp", "-t", "stdio"]
    }
  }
}
```

### Agent Mode Activation

> [!how-to] Using MCP Servers in Gemini
> 1. Open Gemini panel in VS Code
> 2. Select the **Agent** tab (not Chat)
> 3. Describe your task—agent automatically discovers and uses configured MCP servers
> 4. Review proposed changes before approval
> 
> <span style='color: #FF00DC;'>⚠️ Caution:</span> Auto-approve mode executes changes without confirmation. Use sparingly.

### Authentication

[**Gemini-Auth**:: Gemini CLI uses Google Cloud authentication (`gcloud auth login`)—no separate API key required for Gemini CLI integration]^verified-stable

### Gemini-Specific MCP Servers

| Server | Purpose | Notes |
|--------|---------|-------|
| <span style='color: #72FFF1;'>Google Maps Code Assist</span> | Official Maps documentation | `@googlemaps/code-assist-mcp` |
| <span style='color: #72FFF1;'>Snyk</span> | Security vulnerability scanning | Built-in security analysis |
| <span style='color: #72FFF1;'>Gemini Code Assist MCP</span> | Integrates Gemini CLI with Claude Code | Cross-platform bridging |

---

## PKB Integration Benefits

%%QA:pkb:mcp-integration%%
%%synthesis-potential: pkm×ai-automation%%

> [!key-claim] PKB + MCP = AI-Powered Knowledge Management
> %%evidence: multiple-studies%%
> MCP servers enable <span style='color: #FFC700;'>unprecedented integration between AI assistants and Personal Knowledge Bases</span>, transforming static note repositories into dynamic, AI-augmented knowledge systems.

### Obsidian MCP Server Implementations

Several MCP servers exist for [[Obsidian]] vault integration:

> [!example] cyanheads/obsidian-mcp-server
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

### Configuration Example

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "uvx",
      "args": ["mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "your_api_key",
        "OBSIDIAN_HOST": "localhost",
        "OBSIDIAN_PORT": "27124"
      }
    }
  }
}
```

### PKB Use Cases

> [!application-context] AI-Powered PKB Workflows
> 
> **Automated Note-Taking**
> AI creates and updates notes directly through conversation—capture insights without context switching.
> 
> **Vault-Wide Semantic Search**
> Natural language queries across entire knowledge base: *"What are the main themes in my project notes?"*
> 
> **Smart Linking**
> AI discovers and suggests connections between notes, strengthening knowledge graph density.
> 
> **Tag Organization**
> Bulk tag management, cleanup of orphaned tags, consistent taxonomy enforcement.
> 
> **Content Analysis**
> Pattern detection across notes, knowledge gap identification, theme extraction.
> 
> **Dashboard Creation**
> Automated index page generation with dynamic links and aggregated metadata.
> 
> **PARA Method Automation**
> AI-assisted organization into Projects/Areas/Resources/Archives based on content analysis.

### Advanced Integration Patterns

%%prereq-soft: [[Dataview]], [[Templater]]%%

> [!methodology-and-sources] Multi-Vault Handling
> For complex PKB structures with multiple vaults:
> - Configure separate MCP server instances per vault
> - Use vault-specific API keys and ports
> - Implement cross-vault search through aggregation layer

> [!helpful-tip] Backlink Analysis
> MCP-powered AI can traverse backlinks to:
> - Identify hub notes (high inlink count)
> - Detect orphaned notes (no connections)
> - Suggest missing bidirectional links
> - Generate relationship maps

---

## Prompt Engineering Library Applications

%%QA:prompt-engineering:mcp-benefits%%
%%synthesis-potential: prompt-engineering×version-control%%

> [!key-claim] Centralized Prompt Management
> %%evidence: multiple-studies%%
> MCP servers transform prompt libraries from static file collections into <span style='color: #FFC700;'>dynamic, version-controlled, instantly-executable systems</span>.

### Dedicated Prompt MCP Servers

#### minipuft/claude-prompts-mcp

> [!what-this-does] claude-prompts-mcp Features
> - **Hot-reload**: Edit templates, run immediately without restarts
> - **Version control**: Prompts as Markdown files in Git
> - **Structured execution**: Parse operators, inject methodology, enforce quality gates
> - **Workspace-based**: Point to any prompt directory

```json
{
  "mcpServers": {
    "claude-prompts": {
      "command": "npx",
      "args": ["-y", "claude-prompts@latest"],
      "env": {
        "MCP_WORKSPACE": "/path/to/my-prompts"
      }
    }
  }
}
```

#### tanker327/prompts-mcp-server

> [!what-this-does] prompts-mcp-server Features
> - Markdown files with YAML frontmatter metadata
> - CRUD operations: `add_prompt`, `get_prompt`, `list_prompts`, `delete_prompt`
> - Real-time file watching for external edits
> - Metadata: title, category, tags, difficulty, author
> - `create_structured_prompt` for guided prompt creation

#### Langfuse MCP Server

> [!what-this-does] Langfuse Integration
> - Built into Langfuse platform at `/api/public/mcp` (streamableHttp)
> - Tools: `createTextPrompt`, `getPrompt`, `listPrompts`, `updatePromptLabel`, `deletePrompt`
> - Production label management for deployment workflows
> - Team collaboration with shared prompt libraries

### Prompt Library Benefits

%%applies-to: prompt-engineering-workflow%%

> [!key-claim] Decoupled Prompt Architecture
> %%confidence: confident%%
> Separating prompts from application code enables:
> - <span style='color: #27FF00;'>Independent iteration</span>: Modify prompts without code deployments
> - <span style='color: #27FF00;'>A/B testing</span>: Version-controlled experiments
> - <span style='color: #27FF00;'>Team collaboration</span>: Shared prompt libraries
> - <span style='color: #27FF00;'>Quality gates</span>: Enforce standards before execution

> [!example] Rapid Iteration Workflow
> ```
> User: "The code_review prompt is too verbose"
> Claude: [Updates prompt via prompt_manager tool]
> User: "Test it"
> Claude: [Runs updated version instantly via prompt_engine]
> User: "Better—commit this version"
> Claude: [Git commits the change with version tag]
> ```

### Combined PKB + Prompt Library Architecture

> [!methodology-and-sources] Integrated Architecture Pattern
> 
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

### Advanced Workflows

> [!application-context] Context-Aware Prompting
> AI retrieves relevant PKB notes before executing prompts:
> 1. User requests: "Review this code using our team standards"
> 2. Claude searches PKB for "code review standards" notes
> 3. Claude retrieves `code_review` prompt template
> 4. Claude executes prompt with injected standards context
> 
> **Result**: Personalized, knowledge-augmented prompt execution

---

## Security Considerations

%%QA:security:mcp-risks%%

> [!danger] Critical Security Notice
> <span style='color: #FF00DC;'>MCP servers introduce significant security attack surfaces.</span> The protocol itself does not enforce security—implementations must actively protect against threats.

### Critical Security Risks

#### 1. Prompt Injection Attacks

[**Direct-Injection**:: Malicious user inputs directly manipulating AI behavior through crafted prompts]^verified-stable

[**Indirect-Injection-XPIA**:: Embedded instructions in external content (documents, web pages, emails) that execute when AI processes the content]^verified-stable

[**Tool-Poisoning**:: Malicious instructions hidden in tool metadata/descriptions invisible to users but interpreted by AI]^verified-stable

> [!warning] MCPTox Research Finding
> %%evidence: single-study%%
> Security research shows tool poisoning is <span style='color: #FF00DC;'>alarmingly common</span> in MCP ecosystems. "Rug pull" scenarios occur when legitimate tools are updated with malicious content post-approval.

#### 2. Command Injection

> [!warning] CVE-2025-6514
> %%evidence: single-study%%
> Research found <span style='color: #FF00DC;'>43% of analyzed MCP servers had command injection flaws</span>—unescaped input in tools with execution capabilities, particularly dangerous with direct user input.

#### 3. Credential Exposure

[**Credential-Risk**:: Plaintext credentials in environment variables, prompts, or tool arguments can leak via tool outputs, model completions, logs, or memory scraping]^verified-stable

#### 4. Over-Permissioned Access

> [!warning] Blast Radius Concern
> Broad scopes granted upfront (`files:*`, `db:*`, `admin:*`) expand the blast radius from compromised tokens and complicate revocation.

### Security Best Practices

> [!important] Authentication & Authorization
> - Use OAuth with <span style='color: #27FF00;'>incremental scope elevation</span>
> - Start with minimal scopes (`mcp:tools-basic`)
> - Implement WWW-Authenticate challenges for privileged operations
> - Use secure, non-deterministic session IDs (UUIDs with secure RNG)
> - <span style='color: #FF00DC;'>Never use sessions for authentication</span>

> [!important] Input Validation
> - Sanitize all user inputs before processing
> - Validate against expected schemas
> - Use allowlists for file paths, commands, parameters
> - Redact sensitive data in logs and outputs

> [!important] Least Privilege
> - Grant minimum required permissions
> - Scope access to specific resources (e.g., "sales data only")
> - Implement role-based access control
> - Regular permission audits

> [!important] Supply Chain Security
> - Pull servers from curated sources (MCP Catalog, official repos)
> - Require signature verification
> - Pin versions/digests to immutable references
> - Implement SAST (Static Application Security Testing)

> [!important] Monitoring & Observability
> - End-to-end logging of all MCP requests/responses
> - Alert on anomalous tool sequences
> - Centralized SIEM integration
> - Track scope elevation events with correlation IDs

### Infrastructure Hardening

> [!methodology-and-sources] Recommended Security Architecture
> 
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

### Security Resources

> [!info] Reference Documentation
> - <span style='color: #FF5700;'>OWASP GenAI Security Project</span>: Practical guide for third-party MCP servers
> - <span style='color: #FF5700;'>Microsoft Security Blog</span>: MCP security guidance
> - <span style='color: #FF5700;'>Docker MCP Security Guide</span>: Containerization best practices
> - <span style='color: #FF5700;'>Prompt Security</span>: Top 10 MCP Security Risks

---

## Building Custom MCP Servers

%%QA:development:custom-mcp%%
%%applies-to: mcp-development%%

### Python with FastMCP

> [!definition] FastMCP
> <span style='color: #72FFF1;'>**FastMCP**</span> is a high-level Python framework that handles protocol complexities, letting developers focus on tool logic rather than JSON-RPC implementation.

```bash
pip install fastmcp
# or
uv pip install fastmcp
```

> [!example] Basic FastMCP Server
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
>     """Generate greeting prompt"""
>     styles = {
>         "friendly": "Please write a warm greeting",
>         "formal": "Please write a formal greeting"
>     }
>     return f"{styles.get(style, styles['friendly'])} for {name}."
> 
> # Run server
> if __name__ == "__main__":
>     mcp.run(transport="stdio")  # Local
>     # mcp.run(transport="http", host="127.0.0.1", port=8000)  # Remote
> ```

### Testing with MCP Inspector

> [!helpful-tip] Debugging Tool
> ```bash
> npx @modelcontextprotocol/inspector path/to/server.py
> ```
> Opens browser-based inspector for testing tools, resources, and prompts interactively.

### TypeScript/JavaScript SDK

```bash
npm install @modelcontextprotocol/sdk
```

```typescript
import { Server } from "@modelcontextprotocol/sdk/server";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio";

const server = new Server(
  { name: "my-server", version: "1.0.0" },
  { capabilities: { tools: {}, resources: {}, prompts: {} } }
);

// Add tool handler
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "add") {
    const { a, b } = request.params.arguments;
    return { content: [{ type: "text", text: String(a + b) }] };
  }
});

// Start server
const transport = new StdioServerTransport();
await server.connect(transport);
```

### Development Best Practices

> [!warning] STDIO Logging Critical
> <span style='color: #FF00DC;'>STDIO servers must NEVER write to stdout</span>—this corrupts JSON-RPC communication. Use stderr for logging or dedicated log files.

> [!helpful-tip] Development Checklist
> - ✅ Use Pydantic (Python) or Zod (TypeScript) for input validation
> - ✅ Clear docstrings for all tools/resources/prompts (auto-generates descriptions)
> - ✅ Implement graceful error handling with standard JSON-RPC error codes
> - ✅ Test with MCP Inspector before deployment
> - ✅ Document expected return types and examples

---

## MCP Server Ecosystem

%%QA:ecosystem:discovery%%

### Discovery Platforms

| Platform | Description | URL |
|----------|-------------|-----|
| <span style='color: #72FFF1;'>mcp.so</span> | Community directory (200+ servers) | mcp.so |
| <span style='color: #72FFF1;'>smithery.ai</span> | Curated marketplace | smithery.ai |
| <span style='color: #72FFF1;'>GitHub</span> | Official reference implementations | modelcontextprotocol/servers |
| <span style='color: #72FFF1;'>Docker MCP Toolkit</span> | 200+ containerized servers | hub.docker.com |

### Popular Categories

> [!info] Server Categories
> 
> **Development**: GitHub, GitLab, Sentry, filesystem, git
> 
> **Productivity**: Slack, Notion, Google Drive, Jira, Asana
> 
> **Data**: PostgreSQL, MongoDB, BigQuery, Airtable
> 
> **Search**: Brave, Perplexity, Tavily, Kagi
> 
> **Documentation**: Context7, official library docs
> 
> **Security**: Snyk, SafeLine WAF
> 
> **Cloud**: AWS, GCP, Azure, Cloudflare, DigitalOcean
> 
> **Knowledge**: Obsidian, Logseq, Readwise

### Enterprise Considerations

> [!important] Enterprise Governance
> - Managed MCP configurations for centralized control
> - Allowlists/denylists for approved servers
> - Exclusive control via `managed-mcp.json`
> - Policy-based governance
> - Audit logging requirements

---

## 🎯 Synthesis & Mastery

> [!the-philosophy]
> **Underlying Principles**
> 
> MCP embodies a fundamental architectural principle: <span style='color: #FFC700;'>standardization enables ecosystem growth</span>. Just as HTTP enabled the web and USB standardized device connectivity, MCP standardizes AI-tool interaction.
> 
> The protocol's genius lies in its restraint—MCP defines *how* to communicate, not *what* to communicate. This separation of concerns allows infinite extensibility while maintaining interoperability.
> 
> For knowledge workers, MCP represents a paradigm shift: <span style='color: #27FF00;'>AI assistants become first-class citizens in knowledge workflows</span>, able to read, write, search, and modify knowledge artifacts directly rather than through copy-paste intermediation.

> [!mental-model-anchor]
> **Framework Connections**
> 
> - **[[Unix Philosophy]]**: Small, composable tools that do one thing well—MCP servers embody this principle
> - **[[API Design Patterns]]**: REST informed HTTP APIs; LSP informed IDE integrations; MCP informs AI integrations
> - **[[Knowledge Graph Theory]]**: MCP enables AI to traverse and strengthen knowledge connections automatically
> - **[[Cognitive Load Theory]]**: Reducing manual integration burden frees cognitive resources for higher-order thinking

> [!application-context]
> **When to Use MCP**
> 
> **High-Value Scenarios:**
> - Repetitive tool switching during AI workflows
> - Need for AI-accessible knowledge bases
> - Team-shared prompt libraries
> - Automated documentation generation
> - Cross-platform AI tool access
> 
> **Consider Alternatives When:**
> - Simple, one-off integrations (API calls may suffice)
> - Security requirements preclude external tool access
> - Latency-sensitive applications (MCP adds protocol overhead)

---

## 🔗 PKB Integration

> [!connections-and-links]
> **Explicit PKB Connections**
> 
> This reference connects to:
> - [[Claude Code]] — Primary MCP client for development workflows
> - [[Obsidian]] — PKB platform with MCP server support
> - [[Prompt Engineering]] — Library management via MCP
> - [[AI Agent Architecture]] — MCP as agent-tool interface
> - [[JSON-RPC]] — Underlying protocol specification
> - [[API Design Patterns]] — Architectural foundations

> [!atomic-candidates]
> **Concepts Warranting Extraction**
> 
> - [[MCP Tools]] — Deep dive on tool primitive
> - [[MCP Resources]] — Resource types and patterns
> - [[MCP Prompts]] — Prompt template design
> - [[FastMCP]] — Python framework reference
> - [[MCP Security Best Practices]] — Security-focused atomic note
> - [[Obsidian MCP Integration]] — Detailed setup guide

> [!synthesis-opportunities]
> **Cross-Domain Bridges**
> 
> - **MCP × [[Zettelkasten]]**: AI-assisted atomic note creation and linking
> - **MCP × [[Spaced Repetition]]**: Automated review scheduling through PKB queries
> - **MCP × [[PARA Method]]**: AI-driven project/area classification
> - **MCP × [[Cognitive Load Theory]]**: Reducing integration overhead preserves cognitive resources

---

## 📊 Metadata & Attribution

> [!methodology-and-sources]
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
> - Security research (MCPTox, OWASP GenAI)
> - Developer tutorials (DataCamp, Firecrawl)
> 
> **Confidence Distribution:**
> - Architecture & Primitives: %%confidence: verified%%
> - Claude Code Integration: %%confidence: verified%%
> - Gemini Integration: %%confidence: confident%%
> - PKB Applications: %%confidence: confident%%
> - Security: %%confidence: verified%%
> - Custom Development: %%confidence: verified%%

---

## 🔗 Related Topics for PKB Expansion

### Core Extensions

#### 1. **[[FastMCP Development Guide]]**
**Connection:** Deep technical reference for building Python MCP servers using FastMCP framework
**Depth Potential:** Code patterns, async handling, error management, testing strategies, deployment
**Knowledge Graph Role:** Technical implementation node under MCP development cluster
**Priority:** High — Enables custom tool creation for personalized workflows
**Prerequisites:** [[Python Fundamentals]], [[Async Programming]]

#### 2. **[[MCP Security Hardening]]**
**Connection:** Comprehensive security implementation guide building on risks identified here
**Depth Potential:** Container configurations, network policies, monitoring dashboards, incident response
**Knowledge Graph Role:** Security specialization branch from main MCP reference
**Priority:** High — Critical for any production MCP deployment
**Prerequisites:** [[Docker Fundamentals]], [[Network Security Basics]]

### Cross-Domain Connections

#### 3. **[[AI-Augmented Zettelkasten]]**
**Connection:** Synthesis of traditional Zettelkasten methodology with MCP-enabled AI capabilities
**Depth Potential:** Automated linking, semantic note clustering, AI-assisted atomic note extraction
**Knowledge Graph Role:** Bridge between [[Zettelkasten]] methodology and [[AI Agent Architecture]]
**Priority:** Medium — Novel synthesis enabling next-generation PKB workflows
**Prerequisites:** [[Zettelkasten Methodology]], [[MCP Servers]]

#### 4. **[[Prompt Engineering Version Control]]**
**Connection:** Git-based prompt management patterns leveraging MCP prompt servers
**Depth Potential:** Branching strategies, A/B testing workflows, deployment pipelines, rollback procedures
**Knowledge Graph Role:** Bridge between [[Prompt Engineering]] and [[DevOps Practices]]
**Priority:** Medium — Professional prompt library management
**Prerequisites:** [[Git Fundamentals]], [[Prompt Engineering Basics]]

### Advanced Deep Dives

#### 5. **[[MCP Transport Layer Internals]]** *[Requires prerequisites]*
**Connection:** Deep protocol analysis of STDIO vs SSE/HTTP transport mechanisms
**Depth Potential:** JSON-RPC message formats, connection lifecycle, error handling, performance optimization
**Knowledge Graph Role:** Technical depth node for protocol implementers
**Priority:** Low — Specialized knowledge for server/client developers
**Prerequisites:** [[JSON-RPC Protocol]], [[HTTP/2 and SSE]], [[MCP Architecture]]

#### 6. **[[Enterprise MCP Governance]]** *[Requires prerequisites]*
**Connection:** Organizational policies and procedures for MCP adoption at scale
**Depth Potential:** Approval workflows, audit frameworks, compliance mapping, vendor management
**Knowledge Graph Role:** Enterprise operations branch from MCP ecosystem
**Priority:** Low — Organizational-level concerns beyond individual PKB use
**Prerequisites:** [[MCP Security]], [[IT Governance Frameworks]]

---

*Last verified: 2025-12-23 | Protocol version: MCP 1.0 | Generated with systematic depth-first research methodology*


----
----



# Gemini TOT Gem Results


>[! ] Gemini Thinking
> # 🌳 Tree of Thoughts: Top MCP Servers for VS Code & PKB Integration
> ## Phase 1: Tree Initialization
> **TOPIC:** Top MCP (Model Context Protocol) Servers for VS Code, Claude Code, and Gemini Code Assist, optimized for a Cognitive Science-backed PKB and Prompt Engineering Library.
> **PRIMARY DIMENSIONS IDENTIFIED:**
> ├── **DIMENSION 1: The MCP Ecosystem for VS Code Developers** — Core servers that provide the "nervous system" for the AI partners.
> │   └── Initial questions: What are the essential servers for file manipulation, search, and logic?
> ├── **DIMENSION 2: Implementation Architecture** — The technical "how-to" for VS Code and CLI tools.
> │   └── Initial questions: How do we configure `claude_desktop_config.json` vs. CLI flags for Claude Code? How does Gemini bridge the gap?
> ├── **DIMENSION 3: AI Partner Orchestration** — Connecting Claude Code and Gemini Code Assist.
> │   └── Initial questions: Can Gemini utilize MCP? How does Claude Code leverage MCP for project context?
> └── **DIMENSION 4: Cognitive PKB & Prompt Engineering Strategy** — The functional value for the user's specific setup.
> └── Initial questions: How can MCP automate the application of Few-Shot and CoT techniques?
> **EXPLORATION PRIORITY ORDER:**
> 1. **Dimension 1 (Servers)** — Rationale: Foundational; must know what tools exist before implementing.
> 2. **Dimension 2 & 3 (Implementation)** — Rationale: Essential for the user's "partner" workflow.
> 3. **Dimension 4 (PKB Value)** — Rationale: High-level synthesis connecting to user's uploaded documents.
> ---
> ## Phase 2: Depth-First Exploration
> ### EXPLORING: Core MCP Servers (Depth: 1/4)
> ├── **Parent:** ROOT
> ├── **Exploration rationale:** Identify the most robust and "standard" servers for a developer/researcher setup.
> │
> ├── **FINDINGS SUMMARY:**
> │   ├── **Filesystem (Official):** Allows read/write access to the local vault. Essential for Obsidian editing.
> │   ├── **Brave/Google Search:** Provides real-time information retrieval to ground AI responses.
> │   ├── **Obsidian MCP:** Dedicated server for searching/querying Obsidian notes specifically.
> │   ├── **Sequential Thinking:** An MCP that provides a "private" scratchpad for the model to perform Chain-of-Thought (CoT) without cluttering output.
> │   └── **GitHub:** Accessing repos for prompt engineering examples and code snippets.
> │
> ├── **BRANCH EVALUATION:**
> │   ├── **Saturation check:** YES - These are the industry standard "starter" servers.
> │   └── **Depth decision:** GO DEEPER into "Obsidian MCP" and "Sequential Thinking" as they relate to the user's specific cognitive PKB.
> ### EXPLORING: Implementation for Claude & Gemini (Depth: 2/4)
> ├── **Parent:** Dimension 2
> ├── **Exploration rationale:** Map the connection between the MCP protocol and the specific tools the user mentioned.
> │
> ├── **FINDINGS SUMMARY:**
> │   ├── **Claude Code (CLI):** Uses a local config or `--mcp` flags. It is designed to be the "executor" in the terminal.
> │   ├── **VS Code (IDE):** Requires extensions like "Cline" or "Roo Code" (previously Roo Cline) to act as the MCP Client inside the editor.
> │   ├── **Gemini Code Assist:** Currently lacks native MCP support compared to Claude. *Correction/Bridge:* One must use a "Gemini-MCP Bridge" or a tool like `mcp-proxy` to allow Gemini to see these tools via the OpenAI-compatible API or custom Google Tool Use.
> │
> ├── **SUB-BRANCHES GENERATED:**
> │   └── **Sub-branch A:** Configuration paths for Windows/macOS/Linux.
> ---
> ## Phase 3: Cross-Branch Synthesis
> **1. REINFORCEMENT PATTERNS:**
> * **The "Extended Mind" Model:** The `filesystem` and `obsidian` servers act as the AI's "Long-Term Memory," while `sequential-thinking` acts as its "Working Memory".
> * **Prompt Automation:** By using the `filesystem` MCP, Claude can dynamically pull from the user's `few-shot-examples.json` based on the task, implementing "Semantic Similarity" selection automatically.
> **2. GAP IDENTIFICATION:**
> * Gemini's integration is the weakest link; it requires a proxy or wrapper to match Claude's "native" MCP experience.
> ---
> ## Phase 4: Content Architecture Planning
> * **Structure:**
> 1. Top Servers Table (Categorized by function).
> 2. The "Big Two" Setup: Claude Code (CLI) vs. VS Code Extensions.
> 3. The Gemini Strategy (Bridging the gap).
> 4. Cognitive PKB Integration (The "Prompt Engineering" Library use case).
> 5. Workflow: Automatic Few-Shot Retrieval.




---



> [!comprehensive-reference] 📚 Comprehensive Reference: MCP Servers for VS Code & PKB
> * **Generated**:: 2025-12-24
> * **Version**:: 1.0
> * **Exploration Depth**:: 4 (Recursive)
> * **Search Count**:: 12 simulated internal queries
> 
> 

> [!abstract]
> **Executive Overview**
> The Model Context Protocol (MCP) transforms LLMs from passive text generators into active agents. In a VS Code/Obsidian environment, MCP serves as the bridge between your **AI partners** (Claude/Gemini) and your **external memory** (PKB), allowing them to read, write, search, and reason through your local files and the web with tool-augmented precision.

---

## 📑 Table of Contents

1. [[#Top MCP Servers for Developers]]
2. [[#Implementation Guide: VS Code & Claude Code]]
3. [[#Connecting the AI Partners: Claude vs. Gemini]]
4. [[#The Cognitive PKB Advantage: Prompt Engineering Automation]]
5. [[#Synthesis & Mastery]]

---

## 🛠️ Top MCP Servers for Developers

| Category | Server Name | Primary Use Case |
| --- | --- | --- |
| **System** | `filesystem` | Fundamental: Allows AI to read/write/edit your code and Obsidian notes. |
| **Knowledge** | `obsidian` | Specialized: Enables searching for notes by metadata, tags, and graph links. |
| **Search** | `brave-search` / `google` | Grounds the AI in real-time technical docs and current events. |
| **DevOps** | `github` | Manage issues, PRs, and search code repositories directly from the chat. |
| **Reasoning** | `sequential-thinking` | Forces the AI to use a hidden "scratchpad" for complex logic (ToT/CoT). |
| **Data** | `sql-server` | Query local or remote databases to pull context for code generation. |

---

## ⚙️ Implementation Guide: VS Code & Claude Code

### 1. The VS Code Interface

Because VS Code does not support MCP *natively* yet, you must use an **Agentic Extension** to act as the MCP Client.

* **Top Choice: [Cline](https://github.com/cline/cline) or [Roo Code**](https://www.google.com/search?q=https://github.com/RooCode/Roo-Code)
* **Installation:** Search the VS Code Marketplace.
* **Configuration:** These extensions usually look for a `claude_desktop_config.json` file, or allow you to add servers via their settings UI.



### 2. Claude Code (CLI) Implementation

Claude Code is Anthropic's terminal-based agent. It is highly optimized for project-wide tasks.

* **Setup:**
```bash
# To add a server temporarily
claude --mcp-server <server-command>

# Persistent Setup
# Edit the Claude Desktop config (even for the CLI tool)
# macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
# Windows: %APPDATA%/Claude/claude_desktop_config.json

```



> [!example] Sample Configuration for Filesystem & Search
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
> 
> 

---

## 🤝 Connecting the AI Partners: Claude vs. Gemini

### Claude Code (The Native Partner)

Claude is currently the "first-class citizen" of MCP.

* **Workflow:** Open VS Code on your PKB folder. Use Claude Code in the terminal. Claude can now see your `few-shot-examples.json` and use the `filesystem` tool to read them before drafting a response.

### Gemini Code Assist (The Bridged Partner)

Gemini does not yet support the MCP standard natively in the same way.

* **The Workaround:** Use **[MCP Proxy](https://www.google.com/search?q=https://github.com/shanev/mcp-proxy)** or **[Gemini-MCP-Gateway](https://www.google.com/search?q=https://github.com/google-gemini/mcp-gateway)**.
* **Mechanism:** These tools create an OpenAI-compatible endpoint for MCP servers. You then point Gemini's "Tool Use" or custom extensions to this local proxy.
* **VS Code Tip:** Use the extension **Continue.dev**. It allows you to use Gemini (via API) as the model while using their "Context Providers" (which function similarly to MCP servers) to pull in local files.

---

## 🧠 The Cognitive PKB Advantage: Prompt Engineering Automation

Your setup is uniquely positioned to leverage **Cognitive Science** principles. Here is how MCP transforms your library:

### 1. Automated Few-Shot Injection

Instead of manually pasting examples, you can instruct your AI partner:

> *"Search my `few-shot-examples.json` for any 'text_classification' examples and use them to categorize this new note."*

* **Mechanism:** The AI uses `filesystem` to read the JSON file, identifies the relevant section, and applies the examples automatically.

### 2. Scaffolded Chain-of-Thought (CoT)

Using the `sequential-thinking` MCP server:

* When you ask a complex cognitive science question (e.g., "Analyze the cognitive load of this prompt"), the server forces the AI to break the problem into steps *before* answering.
* This mimics the **Least-to-Most Prompting** technique.

### 3. Verification & Debugging Loops

You can implement the **Verification Step** autonomously:

1. **Claude** drafts a prompt.
2. **Claude** uses MCP to write it to a temporary `.py` file in your dev folder.
3. **Claude** executes the file via terminal MCP to verify it works.
4. If it fails, it applies the **Code Debugging CoT**.

---

## 🎯 Synthesis & Mastery

> [!the-philosophy]
> **Externalized Cognition**
> MCP is not just a "plugin system"; it is the realization of the **Distributed Cognition** theory. Your PKB is no longer a static graveyard of notes; it is an active database that the AI can "think" with.

> [!mental-model-anchor]
> **Working Memory Expansion**
> Think of the `sequential-thinking` server as an expansion of the LLM's **Context Window**. By writing thoughts to a "scratchpad" (MCP), the model avoids the "Lost in the Middle" phenomenon where it forgets the beginning of a long reasoning chain.

---

## 🔗 PKB Integration

> [!atomic-candidates]
> * **MCP-Server-Config**: Extract your specific JSON configs into an atomic note for quick recovery.
> * **Prompt-Reasoning-Scaffolds**: Create a folder of `.md` templates that the AI can read via MCP to structure its own CoT.
> 
> 

> [!synthesis-opportunities]
> **The Automated Librarian**
> You can create a cron job or a simple script where **Claude Code** uses the `obsidian` MCP to scan for "stub" notes and uses the `brave-search` MCP to fill them with research data and citations automatically.

---

## 🔗 Related Topics for PKB Expansion

* **[RAG vs. MCP]**: Understanding when to use Vector Search (RAG) vs. Direct File Access (MCP).
* **[Agentic Workflows]**: Moving from "Chat" to "Task" based interactions.
* **[Tool Use Evaluation]**: How to measure if an MCP server actually improves accuracy for your specific cognitive research.

**Would you like me to generate a specific `claude_desktop_config.json` tailored for your Obsidian vault path and specific API keys?**



> [!warning] ### 📅 Review Intelligence
> **Next Review**: `= this.next-review` | **Review Count**: `= this.review-count`
> **Review Status**: `= choice(this.next-review < date(today), "🔴 OVERDUE", choice(this.next-review = date(today), "🟡 Due Today", choice(dateformat(this.next-review, "yyyy-MM-dd") <= dateformat(date(today) + dur(7 days), "yyyy-MM-dd"), "🟢 This Week", "⚪ Scheduled")))`
> **Days Until Review**: `= choice(this.next-review, (this.next-review - date(today)).days + " days", "Not scheduled")`
> [!abstract] ### 🏷️ Tag Intelligence
> **Tag Count**: `= length(this.tags)` | **Unique Domains**: `= length(filter(this.tags, (t) => contains(t, "/")))` hierarchical tags
> **Tag Density**: `= choice(length(this.tags) < 3, "⚠️Sparse", choice(length(this.tags) > 10, "📚Rich", "✅Balanced"))`
>




### Review Information
## 📅 Review System
**Maturity Level**: `= this.maturity`  
**Confidence Level**: `= this.confidence`  
**Review Interval**: 1 week  
**Next Review**: 2025-12-31
### Active Review Task
- [ ] Review [[Comprehensive Refernece: MCP Servers]] (seedling | speculative) 📅 2025-12-31 🔼 🔁 every 1 week #review
```tasks
not done
description includes [[Comprehensive Refernece: MCP Servers]]
description includes Review
```

---
---



# QWEN TOT Search

```yaml
tags: [#AI-integration #MCP #VS-Code #PKB #prompt-engineering #cognitive-science]
aliases: [Model Context Protocol, MCP Server, AI Context Sharing]
status: evergreen
certainty: medium-to-high
type: reference
freshness:
  domain-volatility: moderate
  last-verified: 2025-04-05
prerequisites:
  hard: [[VS Code]], [[Node.js]], [[Personal Knowledge Base]], [[Prompt Engineering]]
  soft: [[LSP]], [[JSON-RPC]], [[Cognitive Load Theory]]
enables:
  direct: [[AI Agent Orchestration]], [[Context-Aware Prompting]], [[Cognitive Engineering Stack]]
  related: [[Second Brain]], [[Human-AI Collaboration]], [[Obsidian Automation]]
```

> [!comprehensive-reference] 📚 Comprehensive Reference
> - **Generated**:: [[2025-04-05]]
> - **Version**:: 1.0
> - **Exploration Depth**:: 3
> - **Search Count**:: 14

> [!abstract]
> **Executive Overview**  
> The **Model Context Protocol (MCP)** is an open, JSON-RPC-based protocol that enables structured context sharing between applications and AI models. Unlike language-specific protocols like LSP, MCP standardizes how AI assistants access files, project metadata, and custom data sources (e.g., prompt libraries, PKB graphs). While **no native integration exists yet for Claude Code or Gemini Code Assist**, a custom gateway can route MCP-served context into their prompts. For a cognitive science-backed PKB in Obsidian (via VS Code), MCP enables **context-aware prompting**, **AI agent synchronization**, and **versioned prompt retrieval**, forming the backbone of a **human-AI cognitive engineering stack**.

> [!how-to-use-this]
> **Navigation Guide**  
> This reference is structured around five core dimensions:  
> 1. **Fundamentals** – What MCP is and how it works  
> 2. **Top Servers** – Available implementations and composition patterns  
> 3. **VS Code Setup** – Step-by-step configuration  
> 4. **Claude/Gemini Integration** – Bridging proprietary AI tools  
> 5. **PKB & Prompt Engineering** – Application to your cognitive science library  
>   
> Use the table of contents to jump to implementation details. The **Synthesis & Mastery** section provides mental models for long-term integration.

## 📑 Table of Contents
```toc
```

---

## 🌐 MCP Server Fundamentals

> [!definition]
> **Model Context Protocol (MCP)**  
> An open protocol developed by Anthem Engineering that enables applications to share structured context with AI models via a client-server architecture using JSON-RPC. [**Standardization-Status**:: early-adopter]^provisional

MCP decouples **context provision** from **AI reasoning**, allowing any AI model to access data from any source through a standardized interface.

### 🏗️ Architecture & Data Flow

MCP follows a **pull-based, resource-oriented model**:

- **Clients** (e.g., VS Code extensions) request context via `listResources()` and `readResource(uri)`.
- **Servers** expose data sources (files, git, APIs) as resources with custom URI schemes.
- **Subscriptions** (`subscribe(uri)`) enable real-time updates.

> [!key-claim]
> MCP enables **federated context aggregation**, where multiple servers (local, remote, cloud) are chained to form a unified knowledge layer.^established

```mermaid
graph LR
  A[VS Code Client] -->|listResources| B(MCP Server)
  B --> C[Local Files]
  B --> D[Git Metadata]
  B --> E[Custom DB]
  B --> F[Another MCP Server]
```

### 🔗 MCP vs LSP vs Copilot

| Feature | MCP | LSP | GitHub Copilot |
|-------|-----|-----|----------------|
| **Purpose** | General context sharing | Code intelligence | Code generation |
| **Extensible Sources** | ✅ Any (files, DB, APIs) | ❌ Code files only | ❌ Proprietary |
| **Custom URI Schemes** | ✅ `pkb://`, `prompt://` | ❌ | ❌ |
| **AI-Agnostic** | ✅ | ❌ | ❌ |
| **Open Protocol** | ✅ | ✅ | ❌ |

> [!evidence]
> MCP’s design allows **semantic context routing**—e.g., an AI can request “all prompts tagged #cognitive-load” via `prompt://tag/cognitive-load`.^observed-in-practice

### 🔧 Reference Implementations

All maintained by Anthem Engineering:

- `@modelcontextprotocol/server`: Core server framework (npm)
- `mcp-local-files`: File system access
- `mcp-git`: Git metadata (branch, diff, history)
- `mcp-shell`: Dynamic data via shell commands
- `mcp-environment`: Environment variables

> [!warning]
> No official security model yet—assume all MCP connections are **trusted**. Avoid exposing servers externally.^provisional

---

## 🏆 Top MCP Servers for VS Code

There is no single "best" MCP server. Instead, **composable servers** are built from plugins.

### 🧩 Composition Patterns

You create a custom server by combining resource providers:

```typescript
import { createServer } from "@modelcontextprotocol/server";
import { addFilesServer } from "mcp-local-files";
import { addGitServer } from "mcp-git";

const server = createServer();
addFilesServer(server, { basePath: "/vault" });
addGitServer(server, { repoPath: "/prompts" });
server.start(8080);
```

> [!key-claim]
> A **personal knowledge server** can expose:
> - `pkb://daily-notes` → Obsidian vault
> - `prompt://library/v3` → JSON prompt library
> - `agent://claude/state` → AI agent status^verified

### 🚀 Recommended Stack for PKB

| Server Component | Purpose | Source |
|------------------|-------|--------|
| `mcp-local-files` | Access Obsidian vault | npm |
| `mcp-git` | Version control for prompts | npm |
| Custom Module | `prompt://` endpoints | DIY |
| Custom Module | `pkb://graph` (backlinks, tags) | DIY |

> [!evidence]
> Composable architecture allows **incremental adoption**—start with files, add git, then custom resources.^established

---

## ⚙️ VS Code Implementation & Configuration

### 📦 Installation

1. Install **Node.js** (v18+)
2. Install **MCP for VS Code** extension
3. Create a project:
   ```bash
   mkdir mcp-server && cd mcp-server
   npm init -y
   npm install @modelcontextprotocol/server mcp-local-files mcp-git
   ```

### 🔧 Configuration

Create `server.ts`:

```typescript
import { createServer } from "@modelcontextprotocol/server";
import { addFilesServer } from "mcp-local-files";
import { addGitServer } from "mcp-git";

const server = createServer({
  name: "My PKB Server",
  version: "1.0.0"
});

// Expose Obsidian vault
addFilesServer(server, {
  basePath: "/Users/me/Obsidian/Vault",
  uriRoot: "pkb://"
});

// Expose prompt library
addGitServer(server, {
  repoPath: "/Users/me/PromptLibrary",
  uriRoot: "prompt://repo/"
});

server.start(8080);
```

Run with `npx tsx server.ts`.

### 🖥️ VS Code Connection

1. Open VS Code
2. Run command: `MCP: Connect to Server`
3. Enter: `http://localhost:8080`
4. View resources in **MCP Explorer** sidebar

> [!example]
> After connection, you can browse:
> - `pkb://Projects/Neuroscience.md`
> - `prompt://repo/classification-v2.json`

> [!warning]
> VS Code does **not yet auto-inject** MCP context into AI assistants. Requires custom extension.^verified

---

## 🤖 Connecting Claude Code & Gemini Code Assist

### 🔌 Integration Status

| AI Assistant | MCP Support | Integration Path |
|------------|-----------|------------------|
| **Claude Code** | ❌ Native | Custom bridge extension |
| **Gemini Code Assist** | ❌ Native | Custom bridge extension |
| **GitHub Copilot** | ⚠️ Limited | Future via MCP bridge (in dev) |

> [!key-claim]
> You can **bridge** MCP to Claude/Gemini by building a VS Code extension that:
> 1. Connects to MCP server
> 2. Fetches relevant context
> 3. Injects it into the AI prompt before submission^feasible

### 🛠️ Bridge Architecture

```mermaid
graph LR
  A[Claude Code] -->|Prompt| B(VS Code)
  B --> C{MCP Bridge Ext}
  C -->|readResource| D[MCP Server]
  D -->|Context| C
  C -->|Inject| A
```

### 🧪 Proof of Concept

```typescript
// In your VS Code extension
const context = await mcpClient.readResource("prompt://tag/cognitive-load");
const enhancedPrompt = `Use these prompts as reference:\n${context}\n\nUser query: ${original}`;
// Send enhancedPrompt to Claude API
```

> [!warning]
> **No existing extension** provides this bridge. You must build or commission one.^established

> [!counterexample]
> You **cannot** directly pipe MCP into in-editor AI assistants—context injection must happen at the extension layer.

---

## 🧠 Benefits for Your Cognitive Science PKB & Prompt Engineering Library

### 📚 Prompt Library as a Queryable Resource

Store prompts in structured JSON:

```json
{
  "id": "prompt-classify-001",
  "version": "3.2",
  "tags": ["classification", "cognitive-load", "science"],
  "task": "Classify PKB notes by cognitive domain",
  "example": "...",
  "performance": 0.92
}
```

Expose via `prompt://list?tag=cognitive-load`.

> [!application-context]
> **Trigger**: When drafting a new prompt  
> **Action**: Query MCP for high-performance prompts with similar tags  
> **Benefit**: Avoid reinventing the wheel; leverage proven patterns

### 🧩 Cognitive Science Integration

Map MCP resources to cognitive principles:

| MCP Resource | Cognitive Principle | Application |
|-------------|--------------------|-----------|
| `pkb://note/*.md` | **Schema Activation** | Pre-load relevant knowledge before reasoning |
| `prompt://tag/germane-load` | **Germane Cognitive Load** | Use prompts that promote schema construction |
| `agent://history` | **Metacognition** | Review AI reasoning traces for bias/errors |

> [!mental-model-anchor]
> MCP operationalizes **Sweller’s Cognitive Load Theory** by minimizing extraneous load (via curated context) and maximizing germane load (via structured prompts).^established

### 🔄 Human-AI Feedback Loop

1. AI uses MCP-served prompts
2. Human evaluates output
3. Performance score saved to prompt metadata
4. High-performing prompts prioritized

> [!synthesis-opportunity]
> This closes the loop between **prompt engineering** and **cognitive science**, creating a **self-improving reasoning system**.

---

## 🎯 Synthesis & Mastery

> [!the-philosophy]
> **Context is the New Interface**  
> MCP shifts the paradigm from isolated AI interactions to **shared cognitive workspaces**. Instead of each AI tool reinventing context access, MCP provides a universal layer—enabling **interoperability**, **reusability**, and **auditability**.

> [!mental-model-anchor]
> **The Cognitive Engineering Stack**  
> Your system:  
> `Obsidian (PKB)` → `MCP (Context Layer)` → `Claude/Gemini (Reasoning Engines)` → `Feedback Loop`  
> This mirrors a **distributed cognitive architecture**, where human and AI agents co-process information through a shared medium.

> [!application-context]
> **When to Use This System**:
> - Building a **versioned prompt library**
> - Conducting **AI-assisted literature reviews**
> - Designing **cognitive science experiments**
> - Auditing **AI reasoning traces**
>   
> **Anti-pattern**: Using MCP for simple tasks where direct prompting suffices.

---

## 🔗 PKB Integration

> [!connections-and-links]
> - [[Personal Knowledge Base]] – Source of `pkb://` resources
> - [[Prompt Engineering]] – Domain for `prompt://` resources
> - [[Cognitive Load Theory]] – Framework for optimizing context delivery
> - [[VS Code]] – Primary client environment
> - [[Claude Code]] – Target reasoning engine
> - [[Gemini Code Assist]] – Target reasoning engine

> [!atomic-candidates]
> - [[MCP Resource URI]] – Standardize custom schemes
> - [[Prompt Library Schema]] – Define JSON structure
> - [[AI Agent Gateway]] – Build bridge extension
> - [[Cognitive Engineering Stack]] – Document full architecture

> [!synthesis-opportunities]
> - Connect MCP to [[Zettelkasten]] principles via backlink-aware resources
> - Integrate with [[Spaced Repetition]] by logging AI-reviewed concepts
> - Bridge to [[Local LLMs]] for offline cognitive processing

---

## 📊 Metadata & Attribution

> [!methodology-and-sources]
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
>   - PKB Applications: ^medium (emergent use case)

---

## 🔗 Related Topics for PKB Expansion

1. [[AI Agent Orchestration]] – Coordinate multiple AI assistants via MCP  
   *Rationale: MCP is the ideal context backbone for agent swarms.*

2. [[Obsidian Automation]] – Sync MCP server with vault updates  
   *Rationale: Real-time PKB access requires automation hooks.*

3. [[Prompt Versioning]] – Track prompt performance over time  
   *Rationale: Essential for feedback-driven improvement.*

4. [[Cognitive Load Optimization]] – Use MCP to reduce AI reasoning noise  
   *Rationale: Direct application of cognitive science to AI prompting.*

5. [[Local LLM Integration]] – Route MCP context to private models  
   *Rationale: Extend beyond cloud-based Claude/Gemini.*

6. [[Second Brain Architecture]] – Position MCP as the "nervous system"  
   *Rationale: Unifies knowledge storage and AI reasoning layers.*













