---
tags:
  - "type/reference"
  - "year/2025"
  - "obsidian/plugins"
  - "prompt-engineering"
  - "context-management/memory"
  - "advanced-prompting/rag"
  - "llm-architecture/context-window"
  - "status/evergreen"
aliases:
  - "Smart Connections MCP Integration"
  - "LLM Obsidian Semantic Search"
  - "Auto-Embedding Memory System"
source: "original-synthesis"
id: "20251224163000"
created: "2025-12-24T16:30:00"
modified: "2025-12-24T16:30:00"
type: "reference"
maturity: "evergreen"
confidence: "verified"
link-up:
  - "[[artificial-intelligence-moc]]"
  - "[[prompt-engineering-moc]]"
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[Engineered Meta-Cognitive Workflow Architecture Analysis]]"
  - "[[context-window-management]]"
  - "[[retrieval-augmented-generation]]"
---

> [!overview] ### <span style='color: #7200ff;'>Overview</span>
> - **Title**: [[Smart Connections LLM Integration Guide]]
> - **MOC**: `=this.link-up`
> - **Key Capability**: Automatic semantic embedding of memory files with AI-accessible retrieval via MCP

---

# 🔗 Smart Connections + LLM Memory Integration

> [!abstract] Executive Summary
> This guide demonstrates how to integrate **[[Smart Connections]]** with [[Claude]], [[Gemini]], and **Local LLMs** to create an **auto-embedding memory system**. When memory files are added to your Obsidian vault, Smart Connections automatically generates embeddings. These embeddings are then accessible to LLMs via the **Model Context Protocol (MCP)**, enabling semantic search across your entire memory bank without manual retrieval.

---

# The Integration Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        YOUR OBSIDIAN VAULT                          │
│  ┌──────────────────┐    ┌──────────────────┐    ┌──────────────┐  │
│  │  .claude/core/   │    │  .claude/task-   │    │  Your Notes  │  │
│  │  (Memory Bank)   │    │  logs/           │    │              │  │
│  └────────┬─────────┘    └────────┬─────────┘    └──────┬───────┘  │
│           │                       │                      │          │
│           └───────────────────────┼──────────────────────┘          │
│                                   ▼                                  │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              SMART CONNECTIONS PLUGIN                        │   │
│  │  • Monitors file changes                                     │   │
│  │  • Auto-generates embeddings (local or API)                  │   │
│  │  • Stores in .smart-env/smart_sources.json                   │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                   │                                  │
└───────────────────────────────────┼──────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    MCP SERVER (ob-smart-connections-mcp)            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌───────────┐  │
│  │ connection  │  │   lookup    │  │    stats    │  │  validate │  │
│  │   tool      │  │    tool     │  │    tool     │  │    tool   │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  └───────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          │                         │                         │
          ▼                         ▼                         ▼
    ┌───────────┐           ┌───────────┐           ┌───────────────┐
    │  Claude   │           │  Gemini   │           │  Local LLMs   │
    │  Desktop  │           │   (via    │           │  (Ollama,     │
    │  / API    │           │   proxy)  │           │   LM Studio)  │
    └───────────┘           └───────────┘           └───────────────┘
```

---

# Part 1: Smart Connections Configuration

## Step 1: Install & Configure Smart Connections

> [!methodology-and-sources] Plugin Setup
> 
> 1. **Install Smart Connections** from Obsidian Community Plugins
> 2. **Open Settings** → Smart Connections
> 3. **Configure Embedding Model**:
>    - **Local (Recommended)**: Uses `TaylorAI/bge-micro-v2` by default — **no API key needed**
>    - **API-based**: Can use OpenAI, Anthropic, or other providers

### Recommended Settings for Memory Integration

```yaml
# Smart Connections Settings
Embedding Model: TaylorAI/bge-micro-v2 (local, 384 dimensions)
Min Characters: 100  # Lower threshold to capture smaller memory entries
Exclude Files: 
  - Untitled
  - template*
Exclude Folders:
  - templates/
  - archive/
Include Folders:
  - .claude/     # ⬅️ CRITICAL: Include your memory directory
  - notes/
```

> [!important] Key Configuration
> <span style='color: #FF00DC;'>**You MUST ensure your memory directory (`.claude/` or equivalent) is NOT excluded from indexing.**</span>
> 
> Check Settings → Smart Connections → Exclusions to verify.

---

## Step 2: Verify Embedding Storage Location

Smart Connections stores embeddings in one of two formats:

```
Your Vault/
├── .smart-env/
│   ├── smart_sources.json      # Single-file mode (default)
│   └── multi/                  # Multi-file AJSON mode (large vaults)
│       ├── sources_00001.ajson
│       ├── sources_00002.ajson
│       └── ...
```

> [!helpful-tip] Verification Command
> Run this in terminal to confirm embeddings exist:
> ```bash
> # Check if embeddings file exists
> ls -la "/path/to/vault/.smart-env/"
> 
> # Check embedding count
> cat "/path/to/vault/.smart-env/smart_sources.json" | jq 'keys | length'
> ```

---

# Part 2: MCP Server Setup for Claude

## Option A: Using Claude CLI (Simplest)

```bash
# Install the MCP server and register with Claude Desktop
claude mcp add ob-smart-connections \
  -e OBSIDIAN_VAULT=/path/to/your/vault \
  @yejianye/smart-connections-mcp
```

## Option B: Manual Configuration

### For Claude Desktop (macOS)

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "smart-connections": {
      "command": "npx",
      "args": ["-y", "@yejianye/smart-connections-mcp"],
      "env": {
        "OBSIDIAN_VAULT": "/Users/yourname/Documents/ObsidianVault"
      }
    }
  }
}
```

### For Claude Desktop (Windows)

Edit `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "smart-connections": {
      "command": "npx",
      "args": ["-y", "@yejianye/smart-connections-mcp"],
      "env": {
        "OBSIDIAN_VAULT": "C:\\Users\\yourname\\Documents\\ObsidianVault"
      }
    }
  }
}
```

### For Claude Desktop (Linux)

Edit `~/.config/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "smart-connections": {
      "command": "npx",
      "args": ["-y", "@yejianye/smart-connections-mcp"],
      "env": {
        "OBSIDIAN_VAULT": "/home/yourname/ObsidianVault"
      }
    }
  }
}
```

---

## Step 3: Restart Claude Desktop

After configuration, **completely quit and restart Claude Desktop** (not just close window).

---

## Step 4: Verify MCP Connection

In Claude Desktop, you should now see the Smart Connections tools available:

| Tool | Purpose | Example Query |
|------|---------|---------------|
| `lookup` | Semantic search by query text | "Find notes about authentication" |
| `connection` | Find similar notes to a specific file | "Notes related to projectbrief.md" |
| `stats` | View embedding coverage | "Show vault statistics" |
| `validate` | Check data integrity | "Validate Smart Connections" |

> [!example] Test Query
> Ask Claude: *"Search my vault for notes about 'context window management'"*
> 
> Claude will use the `lookup` tool to semantically search your embeddings.

---

# Part 3: Integration with Gemini

## Option A: Using Gemini via MCP Proxy

Gemini doesn't natively support MCP, but you can use an MCP-to-REST proxy:

### Install MCP Proxy Server

```bash
npm install -g @anthropic-ai/mcp-proxy
```

### Configure Proxy

```json
{
  "servers": {
    "smart-connections": {
      "command": "npx",
      "args": ["-y", "@yejianye/smart-connections-mcp"],
      "env": {
        "OBSIDIAN_VAULT": "/path/to/vault"
      }
    }
  },
  "port": 3100
}
```

### Call from Gemini

```python
import requests
import google.generativeai as genai

# First, get relevant context via MCP proxy
mcp_response = requests.post(
    "http://localhost:3100/tools/lookup",
    json={"query": "authentication patterns", "limit": 5}
)
context = mcp_response.json()

# Then, use Gemini with the retrieved context
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-pro')

prompt = f"""
Based on the following relevant notes from my knowledge base:

{context}

Answer my question: How should I implement user authentication?
"""

response = model.generate_content(prompt)
print(response.text)
```

## Option B: Direct Smart Connections Access (Python)

```python
import json
import numpy as np
from pathlib import Path

class SmartConnectionsRetriever:
    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self.embeddings_path = self.vault_path / ".smart-env" / "smart_sources.json"
        self.load_embeddings()
    
    def load_embeddings(self):
        """Load Smart Connections embeddings from file."""
        with open(self.embeddings_path, 'r') as f:
            self.sources = json.load(f)
    
    def cosine_similarity(self, a, b):
        """Calculate cosine similarity between two vectors."""
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    def search(self, query_embedding: list, top_k: int = 5) -> list:
        """Find most similar notes to query embedding."""
        results = []
        
        for source_key, source_data in self.sources.items():
            if 'vec' in source_data:
                similarity = self.cosine_similarity(
                    query_embedding, 
                    source_data['vec']
                )
                results.append({
                    'path': source_key,
                    'score': similarity,
                    'content': source_data.get('content', '')
                })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]

# Usage with Gemini
retriever = SmartConnectionsRetriever("/path/to/vault")

# Get embedding for query (using same model as Smart Connections)
# Then search
results = retriever.search(query_embedding, top_k=5)
```

---

# Part 4: Integration with Local LLMs (Ollama, LM Studio)

## Option A: Using CLI Tools

The `smart-cli` provides direct command-line access to Smart Connections:

```bash
# Install globally
npm install -g @yejianye/smart-connections-mcp

# Set vault path
export OBSIDIAN_VAULT=/path/to/your/vault

# Semantic search
smart-cli lookup "authentication implementation" --limit=5

# Find connections to specific file
smart-cli connection ".claude/core/systemPatterns.md" --limit=10

# Get stats
smart-cli stats
```

## Option B: Python Integration with Ollama

```python
import subprocess
import json
import ollama

class LocalLLMWithMemory:
    def __init__(self, vault_path: str, model: str = "llama3"):
        self.vault_path = vault_path
        self.model = model
    
    def search_memory(self, query: str, limit: int = 5) -> list:
        """Search Smart Connections via CLI."""
        result = subprocess.run(
            ["smart-cli", "lookup", query, f"--limit={limit}", "--format=json"],
            capture_output=True,
            text=True,
            env={"OBSIDIAN_VAULT": self.vault_path}
        )
        return json.loads(result.stdout)
    
    def query_with_memory(self, user_query: str) -> str:
        """Query local LLM with retrieved memory context."""
        
        # 1. Search for relevant memories
        memories = self.search_memory(user_query, limit=5)
        
        # 2. Format context
        context = "\n\n".join([
            f"[{m['score']:.2f}] {m['path']}\n{m.get('content', '')[:500]}"
            for m in memories
        ])
        
        # 3. Build prompt with memory context
        prompt = f"""You are an AI assistant with access to the following relevant notes from my knowledge base:

<memory_context>
{context}
</memory_context>

Based on this context, please answer the following question:

{user_query}

If the context doesn't contain relevant information, acknowledge that and answer based on your general knowledge."""

        # 4. Query Ollama
        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response['message']['content']

# Usage
llm = LocalLLMWithMemory("/path/to/vault", model="llama3")
response = llm.query_with_memory("How should I structure my authentication system?")
print(response)
```

## Option C: LM Studio with Memory Integration

```python
from openai import OpenAI

# LM Studio runs OpenAI-compatible API on localhost
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="not-needed"
)

def query_with_smart_connections(query: str, vault_path: str) -> str:
    """Query LM Studio with Smart Connections context."""
    
    # Get memory context via CLI
    import subprocess
    result = subprocess.run(
        ["smart-cli", "lookup", query, "--limit=5", "--format=json"],
        capture_output=True,
        text=True,
        env={"OBSIDIAN_VAULT": vault_path}
    )
    memories = json.loads(result.stdout)
    
    # Format context
    context = "\n".join([f"- {m['path']}: {m.get('content', '')[:300]}" for m in memories])
    
    # Query LM Studio
    response = client.chat.completions.create(
        model="local-model",
        messages=[
            {"role": "system", "content": f"Use this context from the user's notes:\n{context}"},
            {"role": "user", "content": query}
        ]
    )
    
    return response.choices[0].message.content
```

---

# Part 5: Automatic Embedding on Memory Addition

> [!key-claim] The Key Insight
> <span style='color: #27FF00;'>**Smart Connections automatically embeds new files when Obsidian is running.**</span>
> 
> When you add a file to your memory directory (`.claude/`), Smart Connections detects the change and generates embeddings automatically—no manual intervention required.

## How Auto-Embedding Works

1. **File Creation**: When a new `.md` file is created in your vault
2. **Smart Connections Detection**: Plugin monitors filesystem changes
3. **Embedding Generation**: New file is embedded using configured model
4. **Storage Update**: Embedding added to `.smart-env/smart_sources.json`
5. **MCP Access**: New embedding immediately available to LLMs via MCP

## Ensuring Your Memory Directory is Indexed

### Verify Indexing Status

```bash
# Check if memory files are embedded
smart-cli stats

# Look for your memory files specifically
smart-cli connection ".claude/core/activeContext.md"
```

### If Memory Files Aren't Being Indexed

1. **Check Exclusions**: Settings → Smart Connections → Exclusions
   - Remove `.claude` from excluded folders
   
2. **Check Min Characters**: Settings → Smart Connections → Min Characters
   - Lower to 50-100 if memory files are short

3. **Force Re-index**: 
   - Command Palette → "Smart Connections: Refresh all embeddings"

---

# Part 6: Complete Memory System Integration

## Enhanced Memory Bank with Smart Connections

Here's how to modify the Cline memory system to leverage Smart Connections:

### Updated `.clinerules` Section

```markdown
## Smart Connections Memory Protocol

### Automatic Embedding Integration
All memory files in `.claude/` are automatically embedded by Smart Connections.
This enables semantic retrieval across the entire memory bank.

### Retrieval Priority
1. **Semantic First**: Use `lookup` tool to find relevant context by meaning
2. **Structural Second**: Navigate file structure for known locations
3. **Connection Third**: Find related notes via `connection` tool

### Memory Retrieval Commands
When starting a session or needing context:
- "Search memory for [topic]" → Uses lookup tool
- "Find notes related to [file]" → Uses connection tool
- "Check memory bank status" → Uses stats tool

### Memory Update Verification
After adding memory:
1. Confirm file created in `.claude/` directory
2. Wait 5-10 seconds for embedding generation
3. Verify via: smart-cli connection "[new-file-path]"
```

### Session Start Protocol with Semantic Retrieval

```markdown
## Enhanced Session Start

When beginning a new session:

1. **Load Structural Context**
   - Read activeContext.md (current state)
   - Read .clinerules (workflow rules)

2. **Semantic Context Enhancement**
   - Use lookup tool: "current focus project goals"
   - Use connection tool on activeContext.md to find related memories
   - Synthesize retrieved context into working memory

3. **Gap Detection**
   - Compare task requirements to retrieved context
   - Identify missing information
   - Query specific memories as needed

Example:
"Starting new session for authentication feature. 
Let me search for relevant memories..."
[Uses lookup: "authentication security patterns"]
[Uses connection: ".claude/core/systemPatterns.md"]
"Found 5 relevant notes. Integrating context..."
```

---

# Part 7: Advanced Patterns

## Pattern 1: Query Anchors for Precise Retrieval

Add query anchors to your memory files for targeted semantic search:

```markdown
# System Patterns

%%QA:auth:flow%%
User authentication follows OAuth 2.0 with PKCE extension...

%%QA:auth:tokens%%
Access tokens expire after 15 minutes, refresh tokens after 7 days...

%%QA:arch:microservices%%
Services communicate via gRPC with REST fallback...
```

These anchors become highly searchable via:
```bash
smart-cli lookup "auth flow tokens"
```

## Pattern 2: Memory Summaries for Efficient Retrieval

Create summary files that aggregate key information:

```markdown
# Active Memory Summary
Updated: 2025-12-24

## Current Project Focus
Authentication system refactoring for microservices architecture

## Key Decisions This Week
1. Chose OAuth 2.0 + PKCE over session-based auth
2. Selected PostgreSQL for user store
3. Implemented rate limiting at API gateway

## Unresolved Questions
- Token storage strategy for mobile clients
- Refresh token rotation policy
```

This summary file becomes a high-value semantic anchor.

## Pattern 3: Cross-Reference Validation

Use connections to validate memory consistency:

```python
def validate_memory_coherence(vault_path: str):
    """Check if core memory files are semantically connected."""
    
    core_files = [
        ".claude/core/projectbrief.md",
        ".claude/core/systemPatterns.md",
        ".claude/core/activeContext.md"
    ]
    
    for file in core_files:
        connections = smart_cli_connection(file, limit=5)
        
        # Check if core files reference each other
        core_connections = [c for c in connections if c['path'] in core_files]
        
        if len(core_connections) < 2:
            print(f"⚠️ {file} may be drifting from core context")
            print(f"   Consider updating cross-references")
```

---

# Troubleshooting

> [!warning] Common Issues

### Issue: "Smart sources data not found"

**Cause**: Smart Connections hasn't indexed yet or embeddings file missing.

**Solution**:
1. Open Obsidian and wait for indexing to complete
2. Check: `ls /path/to/vault/.smart-env/`
3. Run: Command Palette → "Smart Connections: Refresh all embeddings"

### Issue: Memory files not appearing in search

**Cause**: Files excluded from indexing or too short.

**Solution**:
1. Check exclusion settings
2. Lower "Min Characters" threshold
3. Verify file has enough content to embed

### Issue: MCP connection failing

**Cause**: Claude Desktop not configured correctly.

**Solution**:
1. Verify JSON syntax in config file
2. Check vault path is absolute and exists
3. Restart Claude Desktop completely
4. Check logs: `~/Library/Logs/Claude/mcp*.log`

### Issue: Embeddings not updating

**Cause**: Obsidian not running or Smart Connections paused.

**Solution**:
1. Ensure Obsidian is running with vault open
2. Check Smart Connections isn't paused (ribbon icon)
3. Force refresh: Command Palette → "Smart Connections: Refresh all embeddings"

---

# 🔗 Related Topics for PKB Expansion

## Core Extensions

### 1. **[[Retrieval-Augmented Generation Patterns]]**
**Connection**: This integration is fundamentally a RAG system—understanding RAG deeply improves implementation
**Depth Potential**: Chunking strategies, hybrid retrieval, re-ranking, context injection patterns
**Priority**: High - Critical for optimizing retrieval quality

### 2. **[[Model Context Protocol Specification]]**
**Connection**: MCP is the bridge enabling this integration—understanding the protocol enables custom tools
**Depth Potential**: Tool creation, resource management, prompt injection, multi-server coordination
**Priority**: High - Enables building custom memory tools

## Cross-Domain Connections

### 3. **[[Embedding Models Comparison]]**
**Connection**: Smart Connections uses embeddings—model choice affects retrieval quality
**Depth Potential**: Local vs API models, dimension tradeoffs, domain-specific fine-tuning
**Priority**: Medium - Optimization opportunity for specialized domains

### 4. **[[Vector Database Architectures]]**
**Connection**: At scale, JSON storage may need upgrading to proper vector DB
**Depth Potential**: Pinecone, Weaviate, Chroma, Milvus comparison; scaling considerations
**Priority**: Low (until vault exceeds 10K+ notes)

---

> [!abstract] Summary
> 
> **The Integration Flow**:
> 1. <span style='color: #FFC700;'>**Add memory file**</span> to `.claude/` directory
> 2. <span style='color: #27FF00;'>**Smart Connections auto-embeds**</span> (when Obsidian is running)
> 3. <span style='color: #72FFF1;'>**MCP Server exposes**</span> embeddings to LLMs
> 4. <span style='color: #9E6CD3;'>**LLMs query semantically**</span> via `lookup` and `connection` tools
> 
> **Key Requirements**:
> - Smart Connections installed and indexing your memory directory
> - MCP server configured for your LLM platform
> - Obsidian running during memory additions (for auto-embedding)
> 
> **Result**: A self-updating semantic memory bank where every addition is automatically searchable by meaning, not just keywords.

---
