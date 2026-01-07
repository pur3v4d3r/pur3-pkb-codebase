---
tags: #implementation-plan #memory-architecture #agent-system #mcp-integration #smart-connections
aliases: [Memory System Implementation, Agent Memory Roadmap, Semantic Memory Setup]
created: 2025-12-25
type: project-roadmap
status: active
priority: high
---

# 🗺️ Agent Memory System Implementation Roadmap

> [!abstract] Executive Summary
> This roadmap provides a comprehensive, phase-by-phase implementation plan for deploying the **Engineered Meta-Cognitive Workflow Architecture** across your agent ecosystem. The system integrates **file-based persistent memory**, **semantic retrieval via Smart Connections**, and **MCP-powered context bridging** to solve the fundamental challenge of LLM memory persistence across sessions.

---

## 📋 Implementation Overview

### System Architecture Summary

```
┌─────────────────────────────────────────────────────────────┐
│                    AGENT ECOSYSTEM                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                 │
│  │ Claude   │  │ Claude   │  │  Other   │                 │
│  │ Code     │  │ Projects │  │  Agents  │                 │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘                 │
│       │             │             │                         │
│       └─────────────┼─────────────┘                         │
│                     │ MCP Protocol                          │
│              ┌──────▼──────┐                                │
│              │   MCP       │                                │
│              │   Server    │                                │
│              └──────┬──────┘                                │
│                     │                                       │
│              ┌──────▼──────────────┐                        │
│              │ Smart Connections   │                        │
│              │ Plugin (Obsidian)   │                        │
│              └──────┬──────────────┘                        │
│                     │                                       │
│         ┌───────────▼───────────┐                           │
│         │  MEMORY VAULT         │                           │
│         │  (File System)        │                           │
│         │                       │                           │
│         │  .claude/             │                           │
│         │  ├── core/            │ ◄── Long-Term Memory     │
│         │  ├── task-logs/       │ ◄── Short-Term Memory    │
│         │  ├── plans/           │                           │
│         │  └── errors/          │                           │
│         │                       │                           │
│         │  .smart-env/          │                           │
│         │  └── embeddings.json  │ ◄── Semantic Index       │
│         └───────────────────────┘                           │
└─────────────────────────────────────────────────────────────┘
```

### Core Value Proposition

**Problem Solved**: LLMs lose all context between sessions, requiring manual reconstruction of project understanding.

**Solution**: A three-layer memory architecture with:
1. **Persistent Storage** — File-based memory survives session resets
2. **Semantic Retrieval** — Embeddings enable intelligent context recovery
3. **Event-Driven Updates** — Automated memory management during agent workflows
4. **Self-Healing** — Checksum validation and consistency enforcement

---

## 🎯 Success Criteria

### Primary Objectives

- [ ] **Objective 1**: Agents can recover full project context after session reset in <30 seconds
- [ ] **Objective 2**: Memory retrieval achieves >85% relevance score for targeted queries
- [ ] **Objective 3**: Memory files auto-update during agent workflows with zero manual intervention
- [ ] **Objective 4**: System scales to handle 50+ concurrent projects without performance degradation
- [ ] **Objective 5**: Knowledge graph integration enables cross-project pattern discovery

### Success Indicators

✅ Agent begins new session → automatically queries relevant memories → demonstrates contextual understanding within first response

✅ Memory search for "authentication patterns" returns systemPatterns.md sections + related task logs ranked by relevance

✅ Agent completes task → memory files updated with decision rationale + alternatives considered + consequences documented

✅ User queries memory connections for a file → receives semantically related memories ranked by similarity score

### Failure Indicators

❌ Agent starts session requiring full project re-briefing from user

❌ Memory searches return irrelevant results or miss critical context

❌ Memory files become stale/inconsistent with actual project state

❌ Embedding generation lags by >5 minutes, breaking real-time workflow

---

## 🔧 Prerequisites & Infrastructure Requirements

### Required Software Stack

| Component | Purpose | Installation |
|-----------|---------|--------------|
| **Obsidian** (v1.4+) | Memory vault host + graph visualization | Download from obsidian.md |
| **Smart Connections Plugin** | Embedding generation + semantic search | Install from Obsidian Community Plugins |
| **Claude Desktop / Code** | Agent platform with MCP support | Download from anthropic.com |
| **Python 3.10+** | Smart CLI tool execution | System package manager |
| **Node.js 18+** | MCP server runtime (if building custom tools) | nodejs.org |

### Optional but Recommended

- **Git** — Version control for memory vault
- **Templater Plugin** — Automated memory file templates
- **Dataview Plugin** — Advanced memory queries
- **Meta Bind Plugin** — Interactive memory management buttons

### System Resources

**Minimum Requirements**:
- 8GB RAM (for embedding generation)
- 5GB disk space (embeddings can grow large)
- Obsidian running concurrently with agents

**Recommended**:
- 16GB+ RAM
- SSD for vault storage (faster embedding I/O)
- Automated Obsidian startup on boot

---

## 📐 Architecture Design Decisions

### Memory Hierarchy Structure

**Layer 1: Long-Term Memory** (`.claude/core/`)
- **Persistence**: Permanent, rarely deleted
- **Update Frequency**: Infrequent (architectural changes only)
- **Files**:
  - `projectbrief.md` — Strategic context, goals, constraints
  - `productContext.md` — User needs, requirements, feature specs
  - `systemPatterns.md` — Design patterns, architectural decisions
  - `techContext.md` — Technology stack, dependencies, integrations
  - `activeContext.md` — Current focus, active tasks, WIP state
  - `progress.md` — Implementation timeline, milestones, blockers

**Layer 2: Short-Term Memory** (`.claude/task-logs/`)
- **Persistence**: 30-day rolling window (configurable)
- **Update Frequency**: Per-task (high frequency)
- **Format**: `YYYY-MM-DD-HH-MM-task-description.md`
- **Contents**: Task objectives, steps executed, decisions made, outcomes

**Layer 3: Working Memory** (`.claude/plans/`)
- **Persistence**: Session-duration or until task completion
- **Update Frequency**: Real-time during planning
- **Contents**: Proposed approaches, analysis, draft implementations

**Error Memory** (`.claude/errors/`)
- **Purpose**: Failure pattern recognition, learning from mistakes
- **Contents**: Error traces, root cause analysis, resolution steps

### File Format Standardization

**Universal Template** (applied to all memory types):

```markdown
---
memory-type: [core | task-log | plan | error]
created: YYYY-MM-DDTHH:MM:SS
project: project-identifier
tags: [domain-tags]
confidence: [speculative | probable | confident | verified]
status: [active | completed | deprecated]
---

# [Memory Title]

## Context
What problem/situation prompted this memory?

## Decision/Action
What was chosen or executed?

## Alternatives Considered
What other options were evaluated? Why rejected?

## Consequences
What trade-offs were accepted? What implications exist?

## Status
Current state: [planning | in-progress | completed | blocked]

## Related Memories
- [[memory-file-1]] — relationship description
- [[memory-file-2]] — relationship description

%%QA:domain:specific-topic%%
[Content with query anchors for semantic search]
```

### Semantic Retrieval Strategy

**Embedding Model**: `text-embedding-ada-002` (OpenAI) or local alternative via Smart Connections

**Retrieval Methods**:
1. **Lookup** — Semantic search across entire vault
   - Use case: "Find all authentication-related decisions"
   - Query: Natural language semantic query
   - Returns: Top-K ranked results with similarity scores

2. **Connection** — Find related memories for a specific file
   - Use case: "What memories relate to systemPatterns.md?"
   - Query: File path
   - Returns: Semantically similar memories

3. **Hybrid Search** — Combine semantic + keyword filtering
   - Use case: "Recent API design decisions with high confidence"
   - Query: Semantic query + metadata filters
   - Returns: Filtered + ranked results

### Query Anchor Protocol

**Purpose**: Create highly searchable semantic anchors within memory files

**Syntax**: `%%QA:domain:specific-topic%%`

**Examples**:
```markdown
%%QA:auth:flow%% User authentication follows OAuth 2.0...
%%QA:auth:tokens%% Access tokens expire after 15 minutes...
%%QA:arch:microservices%% Services communicate via gRPC...
%%QA:data:storage%% PostgreSQL for transactional data...
```

**Benefits**:
- Enables precise semantic retrieval
- Creates domain-organized knowledge clusters
- Supports cross-project pattern extraction

---

# 🚀 Phase-by-Phase Implementation Plan

---

## Phase 1: Foundation Setup (Days 1-2)

**Objective**: Establish infrastructure and validate basic functionality

### Subtask 1.1: Obsidian Vault Creation

**Reasoning Technique**: [[Chain of Thought]]

**Steps**:
1. Create dedicated directory: `~/memory-vault/` or `~/Documents/AgentMemory/`
2. Open Obsidian → Create new vault → Point to directory
3. Configure core settings:
   - Settings → Files & Links → Default location for new notes: "In the folder specified below"
   - Set: `.claude/core/` as default
   - Enable: "Automatically update internal links"
   - Enable: "Detect all file extensions"

**Verification**:
- [ ] Vault opens successfully in Obsidian
- [ ] Can create test note in `.claude/core/`
- [ ] Graph view displays (even if empty)

**Success Criteria**: Vault operational, basic note creation working

---

### Subtask 1.2: Smart Connections Plugin Installation

**Reasoning Technique**: [[ReAct]] (step-by-step with observation)

**Actions**:

**STEP 1**: Install Plugin
```
Obsidian → Settings → Community Plugins → Browse
Search: "Smart Connections"
Install → Enable
```

**OBSERVATION**: Plugin appears in left sidebar (brain icon)

**STEP 2**: Configure Smart Connections
```
Settings → Smart Connections:
- Local Model: OFF (use API initially for stability)
- API Provider: OpenAI
- API Key: [insert-key]
- Embedding Model: text-embedding-ada-002
- Excluded Folders: .obsidian, .trash
- Min Characters: 50
- Max Characters: 1000
```

**OBSERVATION**: Settings save without error

**STEP 3**: Create Test Memory File
```markdown
# Test Memory
Created: 2025-12-25

This is a test memory to validate embedding generation.

%%QA:test:validation%%
Smart Connections should generate embeddings for this content.
```

**OBSERVATION**: After saving, `.smart-env/embeddings.json` should be created within 30 seconds

**STEP 4**: Verify Embedding Generation
```bash
ls -la ~/memory-vault/.smart-env/
# Should show: embeddings.json
```

**OBSERVATION**: File exists and has non-zero size

**Verification**:
- [ ] Plugin installed and enabled
- [ ] API key configured correctly
- [ ] Embeddings file created automatically
- [ ] Test search returns the test memory

**Success Criteria**: Embeddings generate automatically for new files

**Failure Handling**: If embeddings don't generate:
1. Check Obsidian console for errors (Ctrl+Shift+I / Cmd+Option+I)
2. Verify API key is valid (test with curl)
3. Check file meets min character threshold (50+)
4. Force refresh: Command Palette → "Smart Connections: Refresh all embeddings"

---

### Subtask 1.3: MCP Server Configuration

**Reasoning Technique**: [[Plan-and-Solve]]

**PLAN**:
1. Locate Claude Desktop configuration file
2. Add Smart Connections MCP server entry
3. Restart Claude Desktop
4. Verify tools appear in Claude interface

**EXECUTION**:

**Step 1**: Locate Config File

**macOS**:
```bash
nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

**Windows**:
```bash
notepad %APPDATA%\Claude\claude_desktop_config.json
```

**Linux**:
```bash
nano ~/.config/Claude/claude_desktop_config.json
```

**Step 2**: Add MCP Server Configuration

```json
{
  "mcpServers": {
    "obsidian-smart-connections": {
      "command": "npx",
      "args": [
        "-y",
        "@joshuarileydev/smart-cli@latest",
        "mcp",
        "/absolute/path/to/your/memory-vault"
      ]
    }
  }
}
```

**CRITICAL**: Replace `/absolute/path/to/your/memory-vault` with actual vault path

**Examples**:
- macOS: `/Users/yourname/Documents/AgentMemory`
- Windows: `C:\\Users\\yourname\\Documents\\AgentMemory`
- Linux: `/home/yourname/Documents/AgentMemory`

**Step 3**: Restart Claude Desktop

Close completely (Cmd+Q / Alt+F4) → Reopen

**Step 4**: Verify MCP Tools Available

Open Claude Desktop → New conversation → Type:
```
Can you list your available tools?
```

**Expected Response**: Should mention tools like:
- `smart_connections_lookup`
- `smart_connections_connection`

**Verification**:
- [ ] Config file syntax valid (no JSON errors)
- [ ] Vault path is absolute and correct
- [ ] Claude Desktop restarts without errors
- [ ] MCP tools appear in available tools list
- [ ] Test query: "Use the lookup tool to search for 'test validation'"

**Success Criteria**: MCP tools functional, can execute semantic searches from Claude

**Failure Handling**:
- **Error: "Smart sources data not found"**
  - Cause: Embeddings not generated yet
  - Fix: Open Obsidian, wait 30 seconds, retry

- **Error: MCP server failed to start**
  - Cause: Invalid vault path or permissions
  - Fix: Check path is absolute, readable by Claude Desktop

- **Tools don't appear**
  - Check logs: `~/Library/Logs/Claude/mcp*.log` (macOS)
  - Verify JSON syntax with: `python -m json.tool < config.json`

---

### Subtask 1.4: Create Memory Directory Structure

**Reasoning Technique**: [[Least-to-Most]] (build foundation → complex)

**Step 1**: Create Core Directories

```bash
cd ~/memory-vault
mkdir -p .claude/core
mkdir -p .claude/task-logs
mkdir -p .claude/plans
mkdir -p .claude/errors
```

**Step 2**: Create Master Index File

`.claude/memory-index.md`:
```markdown
---
tags: #memory-system #index
type: navigation
---

# 🧠 Agent Memory Bank Index

> [!abstract] Navigation Hub
> Centralized directory for agent memory system across all projects

## 📁 Directory Structure

### Core Memory (Long-Term)
- [[projectbrief.md]] — Strategic context and goals
- [[productContext.md]] — Requirements and user needs
- [[systemPatterns.md]] — Architecture patterns and decisions
- [[techContext.md]] — Technology stack and integrations
- [[activeContext.md]] — Current focus and active tasks
- [[progress.md]] — Implementation timeline and milestones

### Task Logs (Short-Term)
Most recent task logs listed automatically via Dataview:

```dataview
LIST
FROM ".claude/task-logs"
SORT file.ctime DESC
LIMIT 10
```

### Active Plans
```dataview
LIST
FROM ".claude/plans"
WHERE status != "completed"
SORT file.mtime DESC
```

### Error Memory
```dataview
LIST
FROM ".claude/errors"
SORT file.ctime DESC
LIMIT 5
```

## 🔍 Quick Search Patterns

**Find authentication decisions**:
```
smart-cli lookup "authentication security patterns"
```

**Find recent API changes**:
```
smart-cli lookup "API design decisions" --limit 5
```

**Find connections for system patterns**:
```
smart-cli connection ".claude/core/systemPatterns.md"
```

## 📊 Memory Statistics

- Total Memories: `= length(file.lists.file)`
- Last Updated: `= date(now)`
- Active Projects: [manual count or query]

---

*This index is auto-generated. Do not edit the query blocks directly.*
```

**Step 3**: Create Template Files

Create `.claude/core/projectbrief.md`:
```markdown
---
memory-type: core
created: {{date:YYYY-MM-DDTHH:mm:ss}}
project: [project-identifier]
tags: [#project-brief, #strategic-context]
confidence: confident
status: active
---

# Project Brief: [Project Name]

## Strategic Context
**What problem are we solving?**

**Who are we building for?**

**What success looks like?**

## Goals & Objectives
1. Primary Goal:
2. Secondary Goals:
3. Stretch Goals:

## Constraints
**Technical**: 
**Business**: 
**Timeline**: 
**Resources**: 

## Key Stakeholders
- **Product Owner**: 
- **Technical Lead**: 
- **End Users**: 

## Success Metrics
- Metric 1: [definition + target]
- Metric 2: [definition + target]

## Related Memories
- [[productContext.md]] — Requirements detail
- [[systemPatterns.md]] — Architectural approach

%%QA:project:overview%%
[Additional context for semantic search]
```

Repeat for other core files: `productContext.md`, `systemPatterns.md`, `techContext.md`, `activeContext.md`, `progress.md`

**Verification**:
- [ ] All directories created
- [ ] memory-index.md present and renders correctly
- [ ] Template files created in core/
- [ ] Dataview queries work (if plugin installed)
- [ ] Graph view shows connections between core files

**Success Criteria**: Complete directory structure established with navigable index

---

### Subtask 1.5: Foundation Validation Test

**Reasoning Technique**: [[Self-Consistency]] (test multiple paths)

**Test 1: End-to-End Memory Creation**

1. Create new memory file:
```markdown
# Test Decision Record
Created: 2025-12-25

## Context
Testing end-to-end memory system functionality

## Decision
Using PostgreSQL for primary data store

## Alternatives
- MySQL: Rejected due to limited JSON support
- MongoDB: Rejected due to team expertise gap

## Consequences
- Requires PostgreSQL expertise on team
- Strong ACID guarantees benefit transactional workflows

%%QA:data:database-choice%%
PostgreSQL selected for ACID compliance and team familiarity
```

2. Save file in `.claude/core/`
3. Wait 10 seconds for embedding generation
4. Open Claude Desktop → New conversation
5. Query: "Use the lookup tool to search for database decisions"

**Expected Result**: Search returns the new memory file with high relevance score

**Test 2: Connection Discovery**

1. Create second related file referencing first:
```markdown
# API Design Decisions

## Database Integration
We're using PostgreSQL (see [[test-decision-record.md]]) for data persistence.

%%QA:arch:api-design%%
REST API with PostgreSQL backend
```

2. Query: `smart-cli connection ".claude/core/test-decision-record.md"`

**Expected Result**: Returns the API design file as a related memory

**Test 3: Cross-Project Isolation** (if multiple projects)

1. Create memories in different project namespaces
2. Verify searches can filter by project tag
3. Ensure no cross-contamination

**Verification**:
- [ ] New memories generate embeddings within 30 seconds
- [ ] Lookup searches return relevant results
- [ ] Connection searches find related memories
- [ ] Memory index displays new files in Dataview queries
- [ ] Graph view shows relationship links

**Success Criteria**: All three tests pass, system demonstrates full functionality

**Phase 1 Completion Checkpoint**:
✅ Obsidian vault operational
✅ Smart Connections generating embeddings automatically
✅ MCP server connected to Claude Desktop
✅ Directory structure complete with templates
✅ End-to-end validation tests passing

---

## Phase 2: Agent Workflow Integration (Days 3-5)

**Objective**: Enable agents to read, update, and maintain memories during task execution

### Subtask 2.1: Define Agent Memory Protocols

**Reasoning Technique**: [[Constitutional AI]] (establish rules and rewards)

**Protocol Document**: `.clinerules` (project root or `.claude/core/.clinerules`)

```markdown
# Agent Memory Management Protocol

## Constitutional Principles

### Principle 1: Memory-First Operation
**Rule**: After each session reset, I rely ENTIRELY on my MEMORY BANK to understand projects.
**Implication**: Memory files must be comprehensive enough to reconstruct full context.
**Reward**: +5 points for demonstrating memory-based context recovery in first response.
**Penalty**: -10 points if requesting information that exists in memory.

### Principle 2: Real-Time Memory Updates
**Rule**: Update relevant memory files IMMEDIATELY after completing tasks or making decisions.
**Implication**: Memory should never lag behind actual project state.
**Reward**: +3 points per completed task with updated memory.
**Penalty**: -5 points if memory becomes stale (user points out outdated info).

### Principle 3: Semantic Clarity
**Rule**: Write memory content with semantic search in mind—use clear, descriptive language.
**Implication**: Avoid jargon without definition; include query anchors.
**Reward**: +2 points for well-structured query anchors.
**Penalty**: -3 points if memory searches fail to retrieve relevant content.

### Principle 4: Connection Maintenance
**Rule**: Create [[wiki-links]] to related memories; maintain knowledge graph.
**Implication**: Every memory should connect to at least 2 others.
**Reward**: +2 points for well-connected memories (3+ bi-directional links).
**Penalty**: -3 points for orphan memories (0 connections).

## Performance Scoring

Track cumulative score:
- 100+: Excellent memory management
- 50-99: Good, with room for improvement
- 0-49: Needs attention
- Negative: Critical issues requiring protocol review

## Event-Driven Handlers

### On TaskStart
1. Query relevant memories: `smart-cli lookup "[task description keywords]"`
2. Load related memories: `smart-cli connection "[most-relevant-file]"`
3. Synthesize context → Include in working memory
4. Create task-specific plan in `.claude/plans/`

### On Decision Made
1. Document decision in appropriate core file (systemPatterns.md, techContext.md, etc.)
2. Include: Context, Decision, Alternatives, Consequences
3. Add query anchors: `%%QA:domain:topic%%`
4. Link to related memories

### On Task Complete
1. Create task log in `.claude/task-logs/YYYY-MM-DD-HH-MM-task.md`
2. Update `activeContext.md` with new state
3. Update `progress.md` with milestone achievement
4. Verify memory consistency

### On Error Encountered
1. Create error record in `.claude/errors/YYYY-MM-DD-error-type.md`
2. Include: Error trace, Root cause, Resolution steps, Prevention strategy
3. Tag with error category for future pattern recognition

## Template Usage

### Task Log Template
```markdown
---
memory-type: task-log
created: {{date:YYYY-MM-DDTHH:mm:ss}}
project: {{project-id}}
task-type: [feature|bugfix|refactor|research]
status: completed
confidence: confident
---

# Task: [Brief Title]

## Objective
What was the goal?

## Approach
What strategy was used?

## Execution Steps
1. Step 1
2. Step 2
3. Step 3

## Outcome
What was delivered?

## Decisions Made
- Decision 1: Rationale
- Decision 2: Rationale

## Lessons Learned
What would be done differently?

## Related Memories
- [[relevant-memory-1]]
- [[relevant-memory-2]]

%%QA:task:{{task-type}}%%
```

## Validation Checkpoints

Before completing any task, verify:
- [ ] All relevant memory files updated
- [ ] Task log created with full documentation
- [ ] Query anchors added for searchability
- [ ] Wiki-links to related memories present
- [ ] Consistency check passed (no contradictions)

---

**Performance Self-Assessment**: 
After each session, review:
- How many memories were queried at session start?
- How many memories were updated during session?
- Were updates made immediately or delayed?
- Do memory searches return expected results?
- Is the knowledge graph growing appropriately?
```

**Verification**:
- [ ] `.clinerules` file created and accessible
- [ ] Constitutional principles clearly defined
- [ ] Event handlers specify exact actions
- [ ] Template formats standardized
- [ ] Scoring mechanism established

**Success Criteria**: Clear protocol document that agents can reference for memory management guidance

---

### Subtask 2.2: Agent Session Start Automation

**Reasoning Technique**: [[ReAct]] (Reasoning + Acting loop)

**Goal**: Automate context recovery at the beginning of each agent session

**Implementation**: Create a "session start script" or prompt template

**Session Start Prompt Template**:

```markdown
# Agent Session Initialization Protocol

You are beginning a new session. Follow this protocol to recover project context:

## Step 1: Identify Project Context
**Thought**: What project am I working on? Check for project identifier in conversation history or working directory.

**Action**: 
- Check current directory for project name
- Look for `.claude/core/projectbrief.md`
- Identify project from user's first message

**Observation**: [Agent fills: Project identified as X]

---

## Step 2: Load Core Memory Files
**Thought**: I need to understand the strategic context and current state.

**Action**: Read these files in order:
1. `.claude/core/projectbrief.md` — Strategic overview
2. `.claude/core/activeContext.md` — Current focus
3. `.claude/core/progress.md` — Recent achievements

**Observation**: [Agent fills: Summarize key points from each file]

---

## Step 3: Semantic Context Enhancement
**Thought**: Are there specific topics I should deeply understand for today's work?

**Action**: Based on activeContext.md, identify key focus areas and query memories:

Example:
If activeContext says "Implementing authentication system":
- Query: smart-cli lookup "authentication security patterns"
- Query: smart-cli connection ".claude/core/systemPatterns.md"

**Observation**: [Agent fills: Retrieved X relevant memories with Y average relevance score]

---

## Step 4: Synthesize Working Context
**Thought**: I now have enough context to begin productive work.

**Action**: Create internal working memory summary:

```
PROJECT: [name]
CURRENT FOCUS: [from activeContext]
KEY DECISIONS: [from retrieved memories]
ACTIVE CONSTRAINTS: [from projectbrief]
READY FOR: [type of work expected]
```

**Observation**: Context synthesis complete. Ready to engage with user.

---

## Step 5: Greet User with Context Awareness
**Thought**: Demonstrate contextual understanding to build trust.

**Action**: Respond to user with:
- Acknowledgment of project
- Summary of current state
- Readiness confirmation

Example:
"I've loaded the context for [Project Name]. I see we're currently focused on [active task] and have recently completed [recent milestone]. I'm ready to continue work on [expected next steps]. What would you like to tackle today?"

---

## Validation Checklist
Before proceeding with user's request:
- [ ] Project identified correctly
- [ ] Core memory files read
- [ ] Semantic queries executed for relevant topics
- [ ] Working context synthesized
- [ ] No obvious context gaps

**Performance Score**: [Agent self-scores based on .clinerules]
- Did I query memories proactively? (+5)
- Did I demonstrate context understanding? (+5)
- Did I avoid asking for information in memory? (+5)
Total: ___/15 points
```

**Deployment**:
1. Save as `.claude/session-start-protocol.md`
2. Configure Claude Code / Projects to load this file at session start
3. For Claude Code: Add to `.claude/core/` so it's always loaded
4. For manual use: User can paste at session start

**Verification**:
- [ ] Protocol template created
- [ ] Agent follows steps when prompted
- [ ] Memory queries execute successfully
- [ ] Context synthesis demonstrates understanding
- [ ] User receives context-aware greeting

**Success Criteria**: Agent demonstrates full project understanding within first response without requiring user to provide context

---

### Subtask 2.3: Real-Time Memory Update Workflow

**Reasoning Technique**: [[Decomposed Prompting]] (specialized handlers for different update types)

**Implementation**: Create handler functions for different memory update scenarios

**Handler 1: Decision Documentation**

**Trigger**: Agent makes architectural or technical decision

**Process**:
```python
def document_decision(
    decision_title: str,
    context: str,
    chosen_approach: str,
    alternatives: list[str],
    consequences: str,
    target_file: str  # e.g., "systemPatterns.md" or "techContext.md"
):
    """
    Append decision to appropriate memory file.
    """
    
    decision_entry = f"""
---

## Decision: {decision_title}
**Date**: {datetime.now().isoformat()}
**Status**: Active

### Context
{context}

### Chosen Approach
{chosen_approach}

### Alternatives Considered
{'\n'.join([f'- {alt}' for alt in alternatives])}

### Consequences
{consequences}

### Related Memories
- [[Related memory 1]]
- [[Related memory 2]]

%%QA:decisions:{decision_title.lower().replace(' ', '-')}%%
"""
    
    # Append to target file
    with open(f".claude/core/{target_file}", "a") as f:
        f.write(decision_entry)
    
    # Log the update
    print(f"✅ Decision documented in {target_file}")
    print(f"   Embeddings will update within 30 seconds")
```

**Agent Instruction**:
```
When you make a significant decision (architecture, technology choice, design pattern):
1. Identify the appropriate core memory file (systemPatterns, techContext, etc.)
2. Document using the Decision format
3. Include all required sections (Context, Decision, Alternatives, Consequences)
4. Add query anchor: %%QA:domain:topic%%
5. Confirm update: "Decision documented in [file]"
```

**Handler 2: Task Completion Logging**

**Trigger**: Agent completes a task

**Process**:
```python
def create_task_log(
    task_title: str,
    objective: str,
    approach: str,
    steps: list[str],
    outcome: str,
    decisions_made: dict[str, str],
    lessons_learned: str,
    related_memories: list[str]
):
    """
    Create task log file in task-logs/ directory.
    """
    
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")
    filename = f".claude/task-logs/{timestamp}-{task_title.lower().replace(' ', '-')}.md"
    
    content = f"""---
memory-type: task-log
created: {datetime.now().isoformat()}
project: [current-project-id]
task-type: [feature|bugfix|refactor|research]
status: completed
confidence: confident
---

# Task: {task_title}

## Objective
{objective}

## Approach
{approach}

## Execution Steps
{'\n'.join([f'{i+1}. {step}' for i, step in enumerate(steps)])}

## Outcome
{outcome}

## Decisions Made
{'\n'.join([f'- **{k}**: {v}' for k, v in decisions_made.items()])}

## Lessons Learned
{lessons_learned}

## Related Memories
{'\n'.join([f'- [[{mem}]]' for mem in related_memories])}

%%QA:task:{task_title.lower().replace(' ', '-')}%%
"""
    
    with open(filename, "w") as f:
        f.write(content)
    
    # Update activeContext.md
    update_active_context(task_title, outcome)
    
    # Update progress.md
    update_progress(task_title)
    
    print(f"✅ Task log created: {filename}")
```

**Agent Instruction**:
```
After completing each task:
1. Create task log with all required sections
2. Update activeContext.md with new current state
3. Update progress.md with milestone achievement
4. Add wiki-links to related memories
5. Confirm: "Task logged in [filename], memory updated"
```

**Handler 3: Error Documentation**

**Trigger**: Agent encounters an error or failure

**Process**:
```python
def document_error(
    error_type: str,
    error_trace: str,
    root_cause: str,
    resolution_steps: str,
    prevention_strategy: str
):
    """
    Create error record for future pattern recognition.
    """
    
    timestamp = datetime.now().strftime("%Y-%m-%d")
    filename = f".claude/errors/{timestamp}-{error_type.lower().replace(' ', '-')}.md"
    
    content = f"""---
memory-type: error
created: {datetime.now().isoformat()}
error-category: {error_type}
resolution-status: resolved
---

# Error: {error_type}

## Error Trace
```
{error_trace}
```

## Root Cause Analysis
{root_cause}

## Resolution Steps
{resolution_steps}

## Prevention Strategy
{prevention_strategy}

## Related Errors
[Add links to similar past errors]

%%QA:error:{error_type.lower().replace(' ', '-')}%%
"""
    
    with open(filename, "w") as f:
        f.write(content)
    
    print(f"✅ Error documented: {filename}")
    print(f"   Future similar errors can reference this resolution")
```

**Agent Instruction**:
```
When encountering errors:
1. Document error with full trace
2. Perform root cause analysis
3. Document resolution steps
4. Propose prevention strategy
5. Check for similar past errors: smart-cli lookup "error [error-type]"
6. Link to related error memories
```

**Verification**:
- [ ] Decision documentation handler defined
- [ ] Task logging handler defined
- [ ] Error documentation handler defined
- [ ] Agent instructions clear and actionable
- [ ] File creation tested successfully
- [ ] Embeddings generate for new files

**Success Criteria**: Agents can execute all three handler types during normal workflow, creating properly formatted memory files automatically

---

### Subtask 2.4: Memory Consistency Validation

**Reasoning Technique**: [[Reflexion]] (self-evaluation and correction)

**Goal**: Ensure memory files remain consistent and don't contradict each other

**Implementation**: Create validation script

**Consistency Check Script**: `.claude/scripts/validate-memory-consistency.py`

```python
#!/usr/bin/env python3
"""
Memory Consistency Validation Script

Checks for:
1. Orphan memories (no connections to other files)
2. Contradictory information across files
3. Stale activeContext (not updated in 7+ days)
4. Missing query anchors in core files
5. Broken wiki-links
"""

import os
import re
from datetime import datetime, timedelta
from pathlib import Path

def check_orphan_memories(vault_path: str) -> list:
    """Find memory files with zero wiki-links."""
    orphans = []
    memory_dir = Path(vault_path) / ".claude"
    
    for md_file in memory_dir.rglob("*.md"):
        with open(md_file, 'r') as f:
            content = f.read()
            
        # Count wiki-links
        wiki_links = re.findall(r'\[\[([^\]]+)\]\]', content)
        
        if len(wiki_links) == 0:
            orphans.append(str(md_file))
    
    return orphans

def check_stale_active_context(vault_path: str) -> bool:
    """Check if activeContext.md hasn't been updated in 7+ days."""
    active_context_path = Path(vault_path) / ".claude/core/activeContext.md"
    
    if not active_context_path.exists():
        return True  # Missing is considered stale
    
    modified_time = datetime.fromtimestamp(active_context_path.stat().st_mtime)
    age = datetime.now() - modified_time
    
    return age > timedelta(days=7)

def check_missing_query_anchors(vault_path: str) -> list:
    """Find core files without query anchors."""
    missing = []
    core_dir = Path(vault_path) / ".claude/core"
    
    for md_file in core_dir.glob("*.md"):
        with open(md_file, 'r') as f:
            content = f.read()
        
        # Check for query anchors
        if not re.search(r'%%QA:', content):
            missing.append(str(md_file))
    
    return missing

def check_broken_links(vault_path: str) -> list:
    """Find broken wiki-links (files that don't exist)."""
    broken = []
    memory_dir = Path(vault_path) / ".claude"
    
    for md_file in memory_dir.rglob("*.md"):
        with open(md_file, 'r') as f:
            content = f.read()
        
        # Extract all wiki-links
        wiki_links = re.findall(r'\[\[([^\]]+)\]\]', content)
        
        for link in wiki_links:
            # Handle display text: [[file|display]]
            target = link.split('|')[0]
            
            # Check if target file exists
            target_path = memory_dir / f"{target}.md"
            if not target_path.exists():
                broken.append({
                    'source': str(md_file),
                    'broken_link': link,
                    'target': str(target_path)
                })
    
    return broken

def run_validation(vault_path: str):
    """Run all validation checks and report."""
    print("🔍 Running Memory Consistency Validation...\n")
    
    # Check 1: Orphan memories
    orphans = check_orphan_memories(vault_path)
    if orphans:
        print("⚠️  ORPHAN MEMORIES DETECTED:")
        for orphan in orphans:
            print(f"   - {orphan}")
        print(f"   Action: Add [[wiki-links]] to connect these files\n")
    else:
        print("✅ No orphan memories detected\n")
    
    # Check 2: Stale active context
    if check_stale_active_context(vault_path):
        print("⚠️  STALE ACTIVE CONTEXT:")
        print("   activeContext.md hasn't been updated in 7+ days")
        print("   Action: Update with current project state\n")
    else:
        print("✅ activeContext.md is up-to-date\n")
    
    # Check 3: Missing query anchors
    missing_qa = check_missing_query_anchors(vault_path)
    if missing_qa:
        print("⚠️  MISSING QUERY ANCHORS:")
        for file in missing_qa:
            print(f"   - {file}")
        print(f"   Action: Add %%QA:domain:topic%% anchors for searchability\n")
    else:
        print("✅ All core files have query anchors\n")
    
    # Check 4: Broken wiki-links
    broken = check_broken_links(vault_path)
    if broken:
        print("⚠️  BROKEN WIKI-LINKS:")
        for item in broken[:10]:  # Show first 10
            print(f"   - {item['source']}")
            print(f"     Link: [[{item['broken_link']}]]")
            print(f"     Target missing: {item['target']}")
        if len(broken) > 10:
            print(f"   ... and {len(broken) - 10} more")
        print(f"   Action: Fix broken links or create missing files\n")
    else:
        print("✅ No broken wiki-links detected\n")
    
    # Summary
    total_issues = len(orphans) + len(missing_qa) + len(broken)
    if check_stale_active_context(vault_path):
        total_issues += 1
    
    if total_issues == 0:
        print("🎉 All memory consistency checks passed!")
    else:
        print(f"📊 Total issues found: {total_issues}")
        print(f"   Recommended: Fix these issues to maintain memory quality")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python validate-memory-consistency.py /path/to/vault")
        sys.exit(1)
    
    vault_path = sys.argv[1]
    run_validation(vault_path)
```

**Agent Instruction for Consistency Checks**:
```
Weekly (or after major changes), run consistency validation:

1. Execute: python .claude/scripts/validate-memory-consistency.py /path/to/vault
2. Review output for warnings
3. Fix identified issues:
   - Orphans: Add [[wiki-links]] to related memories
   - Stale activeContext: Update with current state
   - Missing query anchors: Add %%QA:domain:topic%%
   - Broken links: Create missing files or fix links
4. Re-run validation until all checks pass
```

**Automated Validation** (Optional):
- Add to git pre-commit hook
- Schedule as daily cron job
- Integrate into CI/CD pipeline

**Verification**:
- [ ] Validation script created and executable
- [ ] Script correctly identifies orphan memories
- [ ] Script detects stale activeContext
- [ ] Script finds missing query anchors
- [ ] Script catches broken wiki-links
- [ ] Agent can run script and fix issues

**Success Criteria**: Validation script runs successfully, identifies issues, and agents can remediate problems

---

### Phase 2 Completion Checkpoint

✅ Agent memory protocols defined and documented
✅ Session start automation working (context recovery in first response)
✅ Real-time memory update handlers implemented
✅ Memory consistency validation script operational
✅ Agents demonstrate full workflow integration (start → work → update → validate)

---

## Phase 3: Advanced Features & Optimization (Days 6-8)

**Objective**: Enhance the system with advanced capabilities, optimize performance, and add power-user features

### Subtask 3.1: Semantic Query Optimization

**Reasoning Technique**: [[Tree of Thoughts]] (explore multiple query strategies)

**Goal**: Improve memory retrieval precision and recall

**Branch A: Hybrid Search (Semantic + Keyword)**

**Approach**: Combine semantic embeddings with traditional keyword filtering

**Implementation**:
```python
def hybrid_search(
    semantic_query: str,
    keyword_filters: list[str] = None,
    metadata_filters: dict = None,
    top_k: int = 10
):
    """
    Perform hybrid search combining semantic and keyword matching.
    
    Args:
        semantic_query: Natural language query for embedding search
        keyword_filters: Must-contain keywords (AND logic)
        metadata_filters: Frontmatter filters (e.g., {'confidence': 'verified'})
        top_k: Number of results to return
    
    Returns:
        Ranked results combining both search methods
    """
    
    # Step 1: Semantic search (get top 50)
    semantic_results = smart_cli_lookup(semantic_query, limit=50)
    
    # Step 2: Apply keyword filters
    if keyword_filters:
        semantic_results = [
            r for r in semantic_results
            if all(kw.lower() in r['content'].lower() for kw in keyword_filters)
        ]
    
    # Step 3: Apply metadata filters
    if metadata_filters:
        semantic_results = [
            r for r in semantic_results
            if all(r['metadata'].get(k) == v for k, v in metadata_filters.items())
        ]
    
    # Step 4: Re-rank and return top_k
    return semantic_results[:top_k]

# Usage
results = hybrid_search(
    semantic_query="authentication security patterns",
    keyword_filters=["OAuth", "token"],
    metadata_filters={"confidence": "verified", "status": "active"},
    top_k=5
)
```

**Branch B: Query Rewriting**

**Approach**: Automatically expand queries with synonyms and related terms

**Implementation**:
```python
def rewrite_query(original_query: str) -> list[str]:
    """
    Generate query variations for better recall.
    
    Examples:
    - "auth" → ["auth", "authentication", "authorization", "login"]
    - "DB" → ["DB", "database", "data store", "persistence layer"]
    """
    
    # Domain-specific synonym expansion
    synonyms = {
        "auth": ["authentication", "authorization", "login", "access control"],
        "DB": ["database", "data store", "persistence", "storage"],
        "API": ["API", "endpoint", "interface", "service"],
        # ... expand with domain vocabulary
    }
    
    # Extract keywords from query
    keywords = original_query.lower().split()
    
    # Expand with synonyms
    expanded_queries = [original_query]  # Always include original
    
    for keyword in keywords:
        if keyword in synonyms:
            for syn in synonyms[keyword]:
                expanded_queries.append(
                    original_query.replace(keyword, syn)
                )
    
    return expanded_queries

# Usage
queries = rewrite_query("auth DB integration")
# Returns: [
#   "auth DB integration",
#   "authentication DB integration",
#   "auth database integration",
#   "authentication database integration",
#   ...
# ]

# Execute all queries and merge results
all_results = []
for q in queries:
    results = smart_cli_lookup(q, limit=10)
    all_results.extend(results)

# Deduplicate and rank by frequency
final_results = deduplicate_and_rank(all_results)
```

**Branch C: Query Anchors + Semantic Search**

**Approach**: Leverage query anchors for precise retrieval, then expand semantically

**Implementation**:
```python
def anchor_guided_search(domain: str, topic: str, expand: bool = True):
    """
    Use query anchors for precision, then expand with semantic search.
    
    Args:
        domain: Domain namespace (e.g., "auth", "data", "arch")
        topic: Specific topic (e.g., "flow", "tokens", "patterns")
        expand: Whether to expand with semantic search
    
    Returns:
        Anchor matches + semantically related content
    """
    
    # Step 1: Exact anchor match
    anchor = f"%%QA:{domain}:{topic}%%"
    anchor_results = keyword_search(anchor)  # Simple grep
    
    if not expand:
        return anchor_results
    
    # Step 2: Extract content near anchors
    anchor_content = []
    for result in anchor_results:
        # Get content within 200 chars of anchor
        anchor_content.append(
            extract_context_around_anchor(result['file'], anchor)
        )
    
    # Step 3: Semantic expansion
    semantic_query = f"{domain} {topic} " + " ".join(anchor_content)
    expanded_results = smart_cli_lookup(semantic_query, limit=10)
    
    # Step 4: Merge and deduplicate
    return merge_results(anchor_results, expanded_results)

# Usage
results = anchor_guided_search("auth", "flow", expand=True)
# Returns: Exact anchor matches + semantically similar content
```

**Evaluation & Selection**:

| Approach | Precision | Recall | Speed | Complexity |
|----------|-----------|--------|-------|------------|
| Hybrid Search | High | High | Medium | Medium |
| Query Rewriting | Medium | Very High | Slow | Low |
| Anchor-Guided | Very High | Medium | Fast | Medium |

**Decision**: Implement **Hybrid Search** as default, with **Anchor-Guided** as optional precision mode

**Agent Instruction**:
```
When querying memory:
1. Default: Use hybrid search with domain keywords
   Example: hybrid_search("auth patterns", keywords=["OAuth"], filters={"confidence": "verified"})

2. For precision: Use anchor-guided search
   Example: anchor_guided_search("auth", "flow")

3. For exploration: Use query rewriting
   Example: rewrite_query("API design") → execute all variations
```

**Verification**:
- [ ] Hybrid search function implemented
- [ ] Query rewriting function implemented
- [ ] Anchor-guided search function implemented
- [ ] Performance testing shows improved retrieval quality
- [ ] Agent can select appropriate search strategy

**Success Criteria**: Memory retrieval precision >90% for well-formed queries

---

### Subtask 3.2: Cross-Project Pattern Extraction

**Reasoning Technique**: [[Chain of Density]] (progressive summarization)

**Goal**: Extract common patterns across multiple projects for reuse

**Implementation**: Pattern Mining Script

**`.claude/scripts/extract-patterns.py`**:
```python
#!/usr/bin/env python3
"""
Cross-Project Pattern Extraction

Analyzes memory files across all projects to identify:
1. Recurring architectural patterns
2. Common error-resolution pairs
3. Frequently referenced technologies
4. Best practices that appear in multiple projects
"""

import os
import re
from collections import Counter, defaultdict
from pathlib import Path

def find_all_project_memories(vault_path: str) -> dict:
    """
    Scan for memory directories across all projects.
    Assumes projects have .claude/ or .cline/ directories.
    """
    projects = {}
    
    for root, dirs, files in os.walk(vault_path):
        if ".claude" in dirs or ".cline" in dirs:
            project_name = Path(root).name
            memory_dir = Path(root) / (".claude" if ".claude" in dirs else ".cline")
            projects[project_name] = memory_dir
    
    return projects

def extract_decisions(memory_dir: Path) -> list:
    """Extract all documented decisions from a project."""
    decisions = []
    
    core_files = memory_dir / "core"
    if not core_files.exists():
        return decisions
    
    for md_file in core_files.glob("*.md"):
        with open(md_file, 'r') as f:
            content = f.read()
        
        # Find decision blocks
        decision_pattern = r'## Decision: (.+?)\n.*?### Chosen Approach\n(.+?)(?=\n###|\n---|\Z)'
        matches = re.findall(decision_pattern, content, re.DOTALL)
        
        for title, approach in matches:
            decisions.append({
                'title': title.strip(),
                'approach': approach.strip(),
                'project': md_file.parent.parent.parent.name,
                'file': str(md_file)
            })
    
    return decisions

def extract_error_patterns(memory_dir: Path) -> list:
    """Extract error-resolution pairs."""
    error_patterns = []
    
    errors_dir = memory_dir / "errors"
    if not errors_dir.exists():
        return error_patterns
    
    for error_file in errors_dir.glob("*.md"):
        with open(error_file, 'r') as f:
            content = f.read()
        
        # Extract error type and resolution
        error_type_match = re.search(r'error-category: (.+)', content)
        resolution_match = re.search(r'## Resolution Steps\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
        
        if error_type_match and resolution_match:
            error_patterns.append({
                'type': error_type_match.group(1).strip(),
                'resolution': resolution_match.group(1).strip(),
                'project': error_file.parent.parent.parent.name,
                'file': str(error_file)
            })
    
    return error_patterns

def extract_tech_stack(memory_dir: Path) -> dict:
    """Extract technology choices from techContext.md."""
    tech_file = memory_dir / "core" / "techContext.md"
    
    if not tech_file.exists():
        return {}
    
    with open(tech_file, 'r') as f:
        content = f.read()
    
    # Simple keyword extraction (could be enhanced with NLP)
    tech_keywords = [
        "PostgreSQL", "MySQL", "MongoDB", "Redis",
        "React", "Vue", "Angular", "Svelte",
        "Python", "JavaScript", "TypeScript", "Go", "Rust",
        "Docker", "Kubernetes", "AWS", "GCP", "Azure",
        # ... expand with domain vocabulary
    ]
    
    found_tech = {}
    for tech in tech_keywords:
        if tech.lower() in content.lower():
            # Extract context around mention
            context_match = re.search(
                f'.{{0,100}}{re.escape(tech)}.{{0,100}}',
                content,
                re.IGNORECASE
            )
            if context_match:
                found_tech[tech] = context_match.group(0).strip()
    
    return found_tech

def generate_pattern_report(vault_path: str, output_file: str = None):
    """
    Generate cross-project pattern analysis report.
    """
    projects = find_all_project_memories(vault_path)
    
    print(f"🔍 Found {len(projects)} projects with memory systems\n")
    
    # Aggregate data
    all_decisions = []
    all_errors = []
    all_tech = defaultdict(list)
    
    for project_name, memory_dir in projects.items():
        print(f"Analyzing: {project_name}")
        
        decisions = extract_decisions(memory_dir)
        all_decisions.extend(decisions)
        
        errors = extract_error_patterns(memory_dir)
        all_errors.extend(errors)
        
        tech = extract_tech_stack(memory_dir)
        for t, context in tech.items():
            all_tech[t].append((project_name, context))
    
    # Analyze patterns
    print(f"\n📊 Pattern Analysis:")
    print(f"   Total decisions documented: {len(all_decisions)}")
    print(f"   Total error resolutions: {len(all_errors)}")
    print(f"   Technologies identified: {len(all_tech)}")
    
    # Find recurring patterns
    decision_titles = [d['title'] for d in all_decisions]
    decision_freq = Counter(decision_titles)
    
    print(f"\n🔁 Recurring Decisions (appearing in 2+ projects):")
    for decision, count in decision_freq.most_common(10):
        if count >= 2:
            print(f"   - {decision} ({count} projects)")
            # Show which projects
            projects_with_decision = [
                d['project'] for d in all_decisions if d['title'] == decision
            ]
            print(f"     Projects: {', '.join(set(projects_with_decision))}")
    
    error_types = [e['type'] for e in all_errors]
    error_freq = Counter(error_types)
    
    print(f"\n🐛 Common Errors (appearing in 2+ projects):")
    for error, count in error_freq.most_common(10):
        if count >= 2:
            print(f"   - {error} ({count} occurrences)")
    
    print(f"\n💻 Technology Frequency:")
    tech_freq = {tech: len(projects) for tech, projects in all_tech.items()}
    for tech, count in sorted(tech_freq.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"   - {tech}: {count} projects")
    
    # Generate markdown report
    if output_file:
        generate_markdown_report(
            output_file,
            all_decisions,
            all_errors,
            all_tech,
            decision_freq,
            error_freq
        )
        print(f"\n📝 Detailed report saved to: {output_file}")

def generate_markdown_report(
    output_file: str,
    decisions: list,
    errors: list,
    tech: dict,
    decision_freq: Counter,
    error_freq: Counter
):
    """Generate detailed markdown report."""
    
    report = f"""---
tags: #pattern-analysis #cross-project #knowledge-extraction
created: {datetime.now().isoformat()}
type: analysis-report
---

# Cross-Project Pattern Analysis

> [!abstract] Overview
> Automated extraction of patterns, decisions, and best practices across {len(set([d['project'] for d in decisions]))} projects.

## 🔁 Recurring Architectural Decisions

Decisions that appear in multiple projects indicate established best practices or common requirements.

"""
    
    for decision, count in decision_freq.most_common(20):
        if count >= 2:
            report += f"\n### {decision} ({count} projects)\n\n"
            
            # Find all instances
            instances = [d for d in decisions if d['title'] == decision]
            
            for instance in instances:
                report += f"**{instance['project']}**:\n"
                report += f"{instance['approach'][:200]}...\n\n"
            
            report += f"[[View details]]({instances[0]['file']})\n\n---\n"
    
    report += f"\n## 🐛 Common Error Patterns\n\n"
    
    for error, count in error_freq.most_common(15):
        if count >= 2:
            report += f"\n### {error} ({count} occurrences)\n\n"
            
            # Find resolution strategies
            resolutions = [e['resolution'] for e in errors if e['type'] == error]
            
            # Show most common resolution
            resolution_freq = Counter(resolutions)
            most_common_resolution = resolution_freq.most_common(1)[0][0]
            
            report += f"**Most Common Resolution**:\n{most_common_resolution}\n\n"
            report += "---\n"
    
    report += f"\n## 💻 Technology Stack Analysis\n\n"
    
    tech_freq = {t: len(projects) for t, projects in tech.items()}
    
    for t, count in sorted(tech_freq.items(), key=lambda x: x[1], reverse=True)[:20]:
        report += f"- **{t}**: {count} projects\n"
    
    report += f"\n## 📚 Recommended Actions\n\n"
    report += f"1. **Create Reusable Decision Templates**: For decisions appearing in 3+ projects\n"
    report += f"2. **Build Error Resolution Playbook**: Document common error patterns and proven solutions\n"
    report += f"3. **Standardize Tech Stack**: Consider codifying frequently used technologies as defaults\n"
    report += f"4. **Extract Best Practices**: Document successful approaches from multiple projects\n\n"
    
    with open(output_file, 'w') as f:
        f.write(report)

if __name__ == "__main__":
    import sys
    from datetime import datetime
    
    if len(sys.argv) < 2:
        print("Usage: python extract-patterns.py /path/to/workspace [output.md]")
        sys.exit(1)
    
    workspace = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else None
    
    generate_pattern_report(workspace, output)
```

**Agent Instruction**:
```
Quarterly or when onboarding new projects:

1. Run pattern extraction:
   python .claude/scripts/extract-patterns.py /path/to/workspace pattern-analysis.md

2. Review generated report for:
   - Decisions made in 3+ projects → Consider creating reusable templates
   - Common errors with proven resolutions → Build error playbook
   - Frequently used technologies → Update default tech stack guidance
   
3. Extract best practices:
   - Create ".claude/best-practices/" directory
   - Document proven patterns as reusable templates
   - Link from projectbrief.md templates

Example:
If "OAuth 2.0 + PKCE" appears in 5 projects:
→ Create ".claude/best-practices/auth-oauth-pkce-template.md"
→ Reference this in future authentication decisions
```

**Verification**:
- [ ] Pattern extraction script created
- [ ] Script correctly identifies recurring decisions
- [ ] Script finds common error patterns
- [ ] Script generates markdown report
- [ ] Report provides actionable insights

**Success Criteria**: Pattern analysis reveals at least 3 cross-project opportunities for standardization or template creation

---

### Subtask 3.3: Performance Optimization

**Reasoning Technique**: [[Self-Consistency]] (test multiple optimization approaches)

**Goal**: Ensure system remains fast even with large memory vaults (10K+ notes)

**Optimization Path 1: Embedding Generation Efficiency**

**Problem**: Large vaults take minutes to re-index

**Solution**: Incremental embedding updates

**Implementation**:
```python
def incremental_embed(vault_path: str):
    """
    Only re-embed files that have changed since last embedding.
    """
    
    embeddings_file = Path(vault_path) / ".smart-env" / "embeddings.json"
    
    if not embeddings_file.exists():
        # First time: full indexing
        print("First-time indexing: this may take a while...")
        smart_connections_refresh_all()
        return
    
    # Load existing embeddings
    with open(embeddings_file, 'r') as f:
        embeddings_data = json.load(f)
    
    # Find files modified since last embedding
    last_embed_time = datetime.fromtimestamp(embeddings_file.stat().st_mtime)
    
    modified_files = []
    for md_file in Path(vault_path).rglob("*.md"):
        file_mtime = datetime.fromtimestamp(md_file.stat().st_mtime)
        
        if file_mtime > last_embed_time:
            modified_files.append(str(md_file))
    
    if not modified_files:
        print("✅ No files modified, embeddings up-to-date")
        return
    
    print(f"🔄 Re-embedding {len(modified_files)} modified files...")
    
    # Smart Connections can be configured for selective refresh
    # (Implementation depends on plugin capabilities)
    # For now: trigger full refresh (plugin handles incremental automatically)
    smart_connections_refresh_all()
    
    print(f"✅ Embeddings updated")

# Schedule this instead of full refresh
```

**Configuration**:
- Smart Connections → Settings → "Auto-update embeddings": ON
- This enables automatic incremental updates

**Optimization Path 2: Query Result Caching**

**Problem**: Same queries executed repeatedly waste API calls

**Solution**: Cache query results with TTL (time-to-live)

**Implementation**:
```python
import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path

class QueryCache:
    def __init__(self, cache_dir: str, ttl_minutes: int = 60):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.ttl = timedelta(minutes=ttl_minutes)
    
    def _cache_key(self, query: str, params: dict = None) -> str:
        """Generate cache key from query + params."""
        cache_input = f"{query}:{json.dumps(params, sort_keys=True)}"
        return hashlib.md5(cache_input.encode()).hexdigest()
    
    def get(self, query: str, params: dict = None):
        """Retrieve cached result if valid."""
        key = self._cache_key(query, params)
        cache_file = self.cache_dir / f"{key}.json"
        
        if not cache_file.exists():
            return None
        
        # Check TTL
        file_age = datetime.now() - datetime.fromtimestamp(cache_file.stat().st_mtime)
        
        if file_age > self.ttl:
            cache_file.unlink()  # Expired, delete
            return None
        
        with open(cache_file, 'r') as f:
            return json.load(f)
    
    def set(self, query: str, results: list, params: dict = None):
        """Cache query results."""
        key = self._cache_key(query, params)
        cache_file = self.cache_dir / f"{key}.json"
        
        with open(cache_file, 'w') as f:
            json.dump(results, f)
    
    def clear(self):
        """Clear all cached queries."""
        for cache_file in self.cache_dir.glob("*.json"):
            cache_file.unlink()

# Usage
cache = QueryCache(".claude/.query-cache", ttl_minutes=60)

def cached_lookup(query: str, limit: int = 10):
    """Lookup with caching."""
    
    # Check cache first
    cached_result = cache.get(query, {'limit': limit})
    
    if cached_result:
        print(f"💾 Cache hit for: {query}")
        return cached_result
    
    # Cache miss: execute query
    print(f"🔍 Executing query: {query}")
    results = smart_cli_lookup(query, limit=limit)
    
    # Cache the results
    cache.set(query, results, {'limit': limit})
    
    return results

# Agent instruction: Use cached_lookup instead of smart_cli_lookup
```

**Optimization Path 3: Lazy Loading**

**Problem**: Loading all memories at session start is slow

**Solution**: Load on-demand based on user's first query

**Implementation**:
```python
def lazy_session_start():
    """
    Minimal session initialization, load details on-demand.
    """
    
    # Load only essential context
    essential_files = [
        ".claude/core/activeContext.md",  # Current state
        ".claude/memory-index.md"          # Navigation
    ]
    
    context = {}
    for file in essential_files:
        with open(file, 'r') as f:
            context[Path(file).stem] = f.read()
    
    print("✅ Essential context loaded")
    print("📋 Current focus:", extract_current_focus(context['activeContext']))
    print("\n💡 I'll load additional context based on your request...")
    
    return context

def on_demand_context_load(user_query: str):
    """
    Load relevant context based on user's query.
    """
    
    # Semantic search for relevant memories
    relevant_memories = smart_cli_lookup(user_query, limit=5)
    
    # Load full content for top 3
    loaded_content = []
    for memory in relevant_memories[:3]:
        with open(memory['path'], 'r') as f:
            loaded_content.append(f.read())
    
    return loaded_content

# Agent workflow:
# 1. Session start: lazy_session_start()
# 2. User message: on_demand_context_load(user_message)
# 3. Work with loaded context
```

**Performance Benchmarking**:

```python
import time

def benchmark_session_start():
    """Compare session start times."""
    
    # Full load
    start = time.time()
    full_load_session_start()  # Loads all core files + queries
    full_time = time.time() - start
    
    # Lazy load
    start = time.time()
    lazy_session_start()  # Loads minimal + on-demand
    lazy_time = time.time() - start
    
    print(f"\n⏱️  Performance Comparison:")
    print(f"   Full Load: {full_time:.2f}s")
    print(f"   Lazy Load: {lazy_time:.2f}s")
    print(f"   Improvement: {((full_time - lazy_time) / full_time * 100):.1f}%")

benchmark_session_start()
```

**Recommended Configuration**:
- **For vaults <1000 notes**: Full load (comprehensive context)
- **For vaults 1000-5000 notes**: Hybrid (essential + top 10 semantic results)
- **For vaults >5000 notes**: Lazy load (minimal + on-demand)

**Verification**:
- [ ] Incremental embedding configured
- [ ] Query caching implemented
- [ ] Lazy loading option available
- [ ] Performance benchmarks show improvement
- [ ] Large vault testing (if available)

**Success Criteria**: Session start time <5 seconds for vaults up to 5000 notes

---

### Subtask 3.4: Knowledge Graph Visualization

**Reasoning Technique**: [[Decomposed Prompting]] (specialized visualization for different views)

**Goal**: Provide visual representations of memory relationships

**Implementation**: Create graph generation scripts

**Script 1: Project Knowledge Graph**

**`.claude/scripts/generate-knowledge-graph.py`**:
```python
#!/usr/bin/env python3
"""
Generate knowledge graph visualization from memory files.
"""

import re
from pathlib import Path
import json

def extract_links(md_file: Path) -> dict:
    """Extract all wiki-links from a markdown file."""
    
    with open(md_file, 'r') as f:
        content = f.read()
    
    # Extract wiki-links
    links = re.findall(r'\[\[([^\]]+)\]\]', content)
    
    # Remove display text if present: [[file|display]] → file
    links = [link.split('|')[0] for link in links]
    
    return {
        'file': md_file.name,
        'links': links
    }

def build_graph_data(vault_path: str) -> dict:
    """Build graph data structure."""
    
    memory_dir = Path(vault_path) / ".claude"
    
    nodes = []
    edges = []
    
    # Scan all markdown files
    for md_file in memory_dir.rglob("*.md"):
        node_data = {
            'id': md_file.stem,
            'label': md_file.stem,
            'type': get_node_type(md_file),
            'path': str(md_file)
        }
        nodes.append(node_data)
        
        # Extract links
        link_data = extract_links(md_file)
        
        for target in link_data['links']:
            edges.append({
                'source': md_file.stem,
                'target': target
            })
    
    return {
        'nodes': nodes,
        'edges': edges
    }

def get_node_type(md_file: Path) -> str:
    """Determine node type based on location."""
    
    if "core" in md_file.parts:
        return "core"
    elif "task-logs" in md_file.parts:
        return "task-log"
    elif "plans" in md_file.parts:
        return "plan"
    elif "errors" in md_file.parts:
        return "error"
    else:
        return "other"

def export_to_mermaid(graph_data: dict, output_file: str):
    """Export graph as Mermaid diagram."""
    
    mermaid = "```mermaid\ngraph LR\n"
    
    # Node styling by type
    node_styles = {
        'core': ':::coreStyle',
        'task-log': ':::taskStyle',
        'plan': ':::planStyle',
        'error': ':::errorStyle'
    }
    
    # Add nodes
    for node in graph_data['nodes']:
        node_id = node['id'].replace('-', '_')
        node_label = node['label']
        style = node_styles.get(node['type'], '')
        
        mermaid += f'    {node_id}["{node_label}"]{style}\n'
    
    # Add edges
    for edge in graph_data['edges']:
        source = edge['source'].replace('-', '_')
        target = edge['target'].replace('-', '_')
        
        mermaid += f'    {source} --> {target}\n'
    
    # Add styling
    mermaid += """
    classDef coreStyle fill:#FFD700,stroke:#333,stroke-width:2px
    classDef taskStyle fill:#72FFF1,stroke:#333,stroke-width:1px
    classDef planStyle fill:#9E6CD3,stroke:#333,stroke-width:1px
    classDef errorStyle fill:#FF00DC,stroke:#333,stroke-width:1px
```
    """
    
    mermaid += "\n```"
    
    with open(output_file, 'w') as f:
        f.write(mermaid)

def export_to_json(graph_data: dict, output_file: str):
    """Export graph as JSON for custom visualization."""
    
    with open(output_file, 'w') as f:
        json.dump(graph_data, f, indent=2)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python generate-knowledge-graph.py /path/to/vault [output.md]")
        sys.exit(1)
    
    vault_path = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "knowledge-graph.md"
    
    print("🔍 Building knowledge graph...")
    graph_data = build_graph_data(vault_path)
    
    print(f"   Nodes: {len(graph_data['nodes'])}")
    print(f"   Edges: {len(graph_data['edges'])}")
    
    print(f"\n📊 Exporting to Mermaid...")
    export_to_mermaid(graph_data, output_file)
    
    print(f"\n📊 Exporting to JSON...")
    json_output = output_file.replace('.md', '.json')
    export_to_json(graph_data, json_output)
    
    print(f"\n✅ Graph exported:")
    print(f"   Mermaid: {output_file}")
    print(f"   JSON: {json_output}")
```

**Agent Instruction**:
```
To visualize knowledge graph:

1. Generate graph:
   python .claude/scripts/generate-knowledge-graph.py /path/to/vault knowledge-graph.md

2. View in Obsidian:
   - Open knowledge-graph.md
   - Mermaid diagram renders automatically

3. Analyze graph structure:
   - Identify isolated nodes (need more connections)
   - Find hub nodes (highly connected - good MOC candidates)
   - Detect orphaned memories (zero connections)
   
4. Update based on insights:
   - Add missing connections
   - Create MOCs for hub topics
   - Link orphan memories to relevant nodes
```

**Script 2: Temporal Evolution Graph**

**Shows how knowledge evolves over time**:

```python
def generate_temporal_graph(vault_path: str, days_back: int = 30):
    """
    Show how memory network has evolved over time.
    """
    
    cutoff_date = datetime.now() - timedelta(days=days_back)
    
    memory_dir = Path(vault_path) / ".claude"
    
    timeline = defaultdict(list)
    
    for md_file in memory_dir.rglob("*.md"):
        created_time = datetime.fromtimestamp(md_file.stat().st_ctime)
        
        if created_time >= cutoff_date:
            day_key = created_time.strftime("%Y-%m-%d")
            timeline[day_key].append(md_file.stem)
    
    # Generate timeline visualization
    timeline_md = "# Memory Evolution Timeline\n\n"
    
    for day in sorted(timeline.keys()):
        timeline_md += f"\n## {day} ({len(timeline[day])} memories)\n\n"
        
        for memory in timeline[day]:
            timeline_md += f"- [[{memory}]]\n"
    
    return timeline_md
```

**Verification**:
- [ ] Knowledge graph generation script working
- [ ] Mermaid output renders correctly in Obsidian
- [ ] JSON export valid
- [ ] Temporal evolution visualization created
- [ ] Agent can interpret and act on graph insights

**Success Criteria**: Knowledge graph reveals structural patterns (hubs, orphans, clusters) that guide memory organization improvements

---

### Phase 3 Completion Checkpoint

✅ Advanced search capabilities implemented (hybrid, query rewriting, anchor-guided)
✅ Cross-project pattern extraction working
✅ Performance optimizations deployed
✅ Knowledge graph visualization available
✅ System scales to handle large memory vaults efficiently

---

## Phase 4: Multi-Agent Coordination (Days 9-10)

**Objective**: Enable multiple agents to share and coordinate through common memory system

### Subtask 4.1: Agent Identity & Namespace Management

**Reasoning Technique**: [[Constitutional AI]] (establish rules for multi-agent operation)

**Goal**: Prevent conflicts when multiple agents access same memory vault

**Implementation**: Agent Identity Protocol

**`.claude/agent-registry.json`**:
```json
{
  "agents": [
    {
      "id": "claude-code-001",
      "type": "code",
      "platform": "Claude Code",
      "capabilities": ["code-generation", "debugging", "refactoring"],
      "primary_projects": ["project-a", "project-b"],
      "last_active": "2025-12-25T10:30:00Z"
    },
    {
      "id": "claude-desktop-research",
      "type": "research",
      "platform": "Claude Desktop",
      "capabilities": ["research", "synthesis", "documentation"],
      "primary_projects": ["project-a", "project-c"],
      "last_active": "2025-12-25T09:15:00Z"
    },
    {
      "id": "claude-project-planning",
      "type": "planning",
      "platform": "Claude Project",
      "capabilities": ["planning", "architecture", "decision-making"],
      "primary_projects": ["project-a"],
      "last_active": "2025-12-25T11:00:00Z"
    }
  ],
  "coordination_rules": {
    "conflict_resolution": "last-write-wins",
    "lock_timeout_seconds": 300,
    "update_notification": true
  }
}
```

**Agent Session Start with Identity**:
```markdown
## Multi-Agent Session Start Protocol

### Step 1: Identify Self
I am [agent-id] of type [agent-type]
My capabilities: [list]
My primary projects: [list]

### Step 2: Check Agent Registry
Read .claude/agent-registry.json
Update my last_active timestamp
Record: "Agent [id] starting session at [timestamp]"

### Step 3: Check for Concurrent Activity
Query: Are other agents currently active on this project?
If yes:
  - Load their recent updates (last 1 hour)
  - Identify potential conflicts
  - Coordinate if needed

### Step 4: Namespace Selection
For memory updates, use namespaced files when appropriate:
- Shared: .claude/core/ (all agents contribute)
- Agent-specific: .claude/agents/[agent-id]/ (private notes)

### Step 5: Proceed with Standard Session Start
[Resume normal session start protocol]
```

**File Locking Protocol**:

**`.claude/locks/[filename].lock`**:
```json
{
  "locked_by": "claude-code-001",
  "locked_at": "2025-12-25T10:30:00Z",
  "operation": "updating systemPatterns.md",
  "expected_duration_seconds": 60
}
```

**Lock Management**:
```python
import fcntl
import time
from pathlib import Path

class MemoryFileLock:
    def __init__(self, file_path: str, agent_id: str):
        self.file_path = Path(file_path)
        self.agent_id = agent_id
        self.lock_dir = Path(".claude/locks")
        self.lock_dir.mkdir(exist_ok=True)
        self.lock_file = self.lock_dir / f"{self.file_path.stem}.lock"
    
    def acquire(self, timeout: int = 30) -> bool:
        """Acquire lock on file."""
        
        start_time = time.time()
        
        while True:
            if not self.lock_file.exists():
                # Create lock
                lock_data = {
                    'locked_by': self.agent_id,
                    'locked_at': datetime.now().isoformat(),
                    'file': str(self.file_path)
                }
                
                with open(self.lock_file, 'w') as f:
                    json.dump(lock_data, f)
                
                return True
            
            # Check if lock is stale
            with open(self.lock_file, 'r') as f:
                lock_data = json.load(f)
            
            lock_age = datetime.now() - datetime.fromisoformat(lock_data['locked_at'])
            
            if lock_age.total_seconds() > 300:  # 5 min timeout
                print(f"⚠️  Stale lock detected, breaking...")
                self.lock_file.unlink()
                continue
            
            # Check timeout
            if time.time() - start_time > timeout:
                print(f"❌ Could not acquire lock on {self.file_path.name}")
                return False
            
            print(f"⏳ Waiting for lock (held by {lock_data['locked_by']})")
            time.sleep(2)
    
    def release(self):
        """Release lock on file."""
        
        if self.lock_file.exists():
            self.lock_file.unlink()

# Usage
lock = MemoryFileLock(".claude/core/systemPatterns.md", agent_id="claude-code-001")

if lock.acquire(timeout=30):
    try:
        # Update file
        with open(".claude/core/systemPatterns.md", "a") as f:
            f.write("\n## New Decision\n...")
    finally:
        lock.release()
else:
    print("Could not update file - locked by another agent")
```

**Agent Instruction**:
```
When updating shared memory files:

1. Acquire lock:
   lock = MemoryFileLock(file_path, my_agent_id)
   if lock.acquire():
       # Update file
       lock.release()

2. If lock acquisition fails:
   - Wait and retry (max 3 attempts)
   - Fall back to creating agent-specific note
   - Log coordination issue for later merge

3. Always release locks in finally block
   (prevents stale locks on error)
```

**Verification**:
- [ ] Agent registry file created
- [ ] Identity protocol defined
- [ ] File locking mechanism implemented
- [ ] Tested with simulated concurrent access
- [ ] Stale lock detection working

**Success Criteria**: Multiple agents can safely update shared memories without conflicts

---

### Subtask 4.2: Agent Communication Protocol

**Reasoning Technique**: [[ReAct]] (agents reason about coordination needs)

**Goal**: Enable agents to leave messages/tasks for each other

**Implementation**: Agent Mailbox System

**`.claude/agent-mailbox/`**:
```
agent-mailbox/
├── inbox/
│   ├── claude-code-001-inbox.md
│   ├── claude-desktop-research-inbox.md
│   └── claude-project-planning-inbox.md
└── sent/
    ├── 2025-12-25-message-001.md
    ├── 2025-12-25-message-002.md
    └── ...
```

**Message Format**:
```markdown
---
from: claude-code-001
to: claude-project-planning
sent: 2025-12-25T10:30:00Z
priority: high
status: unread
type: request
---

# Task Request: Architecture Review Needed

## Context
I've implemented the authentication service and need architecture review before proceeding to deployment.

## What I Need
1. Review systemPatterns.md for consistency with overall architecture
2. Validate OAuth 2.0 implementation against security requirements
3. Approve database schema changes

## Files to Review
- [[systemPatterns.md]] — New authentication section
- [[auth-service-implementation.md]] — Task log
- `.claude/code/auth-service/` — Implementation

## Urgency
High - blocking deployment scheduled for tomorrow

## Action Requested
Please review and either:
- ✅ Approve → I'll proceed to deployment
- ⚠️ Request changes → Document concerns in this thread

---

**Response Thread**:
[Recipient's response will be appended here]
```

**Mailbox Check Protocol**:
```python
def check_mailbox(agent_id: str):
    """Check for new messages in agent's inbox."""
    
    inbox_file = Path(f".claude/agent-mailbox/inbox/{agent_id}-inbox.md")
    
    if not inbox_file.exists():
        return []
    
    with open(inbox_file, 'r') as f:
        content = f.read()
    
    # Parse messages (separated by ---)
    messages = content.split('\n---\n')
    
    unread = []
    for msg in messages:
        if 'status: unread' in msg:
            unread.append(parse_message(msg))
    
    return unread

def send_message(from_agent: str, to_agent: str, message_content: str):
    """Send message to another agent."""
    
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")
    message_file = Path(f".claude/agent-mailbox/sent/{timestamp}-{from_agent}-to-{to_agent}.md")
    
    # Create message
    with open(message_file, 'w') as f:
        f.write(message_content)
    
    # Add to recipient's inbox
    inbox_file = Path(f".claude/agent-mailbox/inbox/{to_agent}-inbox.md")
    
    with open(inbox_file, 'a') as f:
        f.write(f"\n\n---\n\n{message_content}")
    
    print(f"✉️  Message sent to {to_agent}")

# Agent session start: check_mailbox(my_agent_id)
```

**Agent Instruction**:
```
At session start:

1. Check mailbox:
   messages = check_mailbox(my_agent_id)
   
2. If unread messages:
   - Prioritize by urgency
   - Load referenced memory files
   - Respond or take requested action
   - Mark as read
   
3. During work:
   - If blocked on other agent's input:
     send_message(my_id, target_agent, request)
   
   - If completing review requested by another:
     send_message(my_id, requester, response)
```

**Verification**:
- [ ] Mailbox directory structure created
- [ ] Message sending working
- [ ] Message receiving working
- [ ] Priority handling implemented
- [ ] Thread continuation working

**Success Criteria**: Agents can asynchronously request and provide input to each other via mailbox system

---

### Subtask 4.3: Collaborative Memory Updates

**Reasoning Technique**: [[Self-Consistency]] (validate multi-agent contributions)

**Goal**: Multiple agents can contribute to same memory file without conflicts

**Implementation**: Merge-Friendly Update Format

**Append-Only Contributions**:
```markdown
## Decision: Database Choice
**Date**: 2025-12-24
**Decided By**: claude-project-planning
**Status**: Active

### Context
Need persistent storage for user data...

---

## Update: Performance Benchmarks
**Date**: 2025-12-25
**Updated By**: claude-code-001
**Type**: Evidence

Ran performance tests:
- PostgreSQL: 5000 req/s
- MongoDB: 4200 req/s
- MySQL: 4800 req/s

Recommendation: PostgreSQL confirmed as optimal choice.

Related: [[performance-benchmark-results.md]]

---

## Update: Migration Concerns
**Date**: 2025-12-25
**Updated By**: claude-desktop-research
**Type**: Risk Assessment

Research findings on PostgreSQL migration:
- Existing MySQL data requires schema conversion
- Estimated migration time: 2-3 days
- Risk: Potential downtime during migration

Recommendation: Plan migration during low-traffic period.

Related: [[database-migration-research.md]]
```

**Update Validation**:
```python
def validate_multi_agent_contributions(file_path: str) -> dict:
    """
    Check if multi-agent contributions are consistent.
    """
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract all agent contributions
    contributions = re.findall(
        r'\*\*Updated By\*\*: ([\w-]+)',
        content
    )
    
    # Check for contradictions
    contradictions = detect_contradictions(content)
    
    # Check for consensus
    consensus_decisions = extract_decisions(content)
    
    report = {
        'total_contributors': len(set(contributions)),
        'contributors': list(set(contributions)),
        'contradictions_found': len(contradictions),
        'contradictions': contradictions,
        'consensus_reached': all_agree(consensus_decisions)
    }
    
    return report

def detect_contradictions(content: str) -> list:
    """
    Simple contradiction detection (can be enhanced with NLP).
    """
    
    contradictions = []
    
    # Look for explicit conflict markers
    if "contradicts" in content.lower():
        # Extract context
        conflicts = re.findall(
            r'(.{100}contradicts.{100})',
            content,
            re.IGNORECASE
        )
        contradictions.extend(conflicts)
    
    # Look for opposing recommendations
    positive = re.findall(r'Recommendation: (.+)', content)
    
    # Simple check: do recommendations conflict?
    # (More sophisticated: use semantic similarity)
    
    return contradictions

# Agent instruction
```

**Conflict Resolution Protocol**:
```
When detecting contradictions:

1. Document the conflict:
   ## ⚠️ CONFLICT DETECTED
   **Date**: [timestamp]
   **Between**: [agent-1] and [agent-2]
   **Issue**: [description]
   
2. Request resolution:
   - If minor: Propose synthesis
   - If major: Escalate to planning agent or user

3. Once resolved:
   - Create resolution section
   - Link to conflict documentation
   - Update status to "resolved"
```

**Verification**:
- [ ] Append-only contribution format working
- [ ] Multi-agent updates don't overwrite each other
- [ ] Contradiction detection catches conflicts
- [ ] Resolution protocol clear

**Success Criteria**: 3+ agents can contribute to same memory file, contradictions are detected and resolved

---

### Phase 4 Completion Checkpoint

✅ Agent identity and namespace management working
✅ Agent communication via mailbox system operational
✅ Collaborative memory updates functioning
✅ Conflict detection and resolution protocol established
✅ Multi-agent coordination tested successfully

---

## Phase 5: Production Hardening & Monitoring (Days 11-12)

**Objective**: Ensure system reliability, add monitoring, establish maintenance protocols

### Subtask 5.1: Error Handling & Recovery

**Reasoning Technique**: [[Reflexion]] (learn from failures)

**Goal**: Graceful degradation when components fail

**Implementation**: Comprehensive Error Handling

**Error Scenarios & Responses**:

**Scenario 1: Obsidian Not Running**
```python
def check_obsidian_running():
    """Verify Obsidian is running before operations requiring it."""
    
    # Check for .smart-env/ directory (indicates Smart Connections active)
    smart_env = Path(vault_path) / ".smart-env"
    
    if not smart_env.exists():
        return False
    
    # Check if embeddings.json is recent (updated within 5 minutes)
    embeddings_file = smart_env / "embeddings.json"
    
    if not embeddings_file.exists():
        return False
    
    file_age = datetime.now() - datetime.fromtimestamp(embeddings_file.stat().st_mtime)
    
    return file_age.total_seconds() < 300

# Usage in agent workflow
if not check_obsidian_running():
    print("⚠️  Obsidian not detected - embedding generation unavailable")
    print("   Continuing with file-based memory only...")
    print("   (Embeddings will generate when Obsidian starts)")
    
    # Degrade gracefully: use file navigation instead of semantic search
    fallback_to_file_navigation()
```

**Scenario 2: MCP Server Unavailable**
```python
def safe_semantic_lookup(query: str, fallback: bool = True):
    """
    Semantic lookup with fallback to keyword search.
    """
    
    try:
        # Attempt MCP semantic search
        results = smart_cli_lookup(query, limit=10)
        return results
        
    except ConnectionError as e:
        print(f"⚠️  MCP Server unavailable: {e}")
        
        if not fallback:
            return []
        
        print("   Falling back to keyword search...")
        
        # Keyword-based search as fallback
        keywords = query.split()
        results = []
        
        for md_file in Path(".claude").rglob("*.md"):
            with open(md_file, 'r') as f:
                content = f.read().lower()
            
            if all(kw.lower() in content for kw in keywords):
                results.append({
                    'path': str(md_file),
                    'score': calculate_keyword_relevance(content, keywords)
                })
        
        # Sort by relevance
        results.sort(key=lambda x: x['score'], reverse=True)
        
        return results[:10]
```

**Scenario 3: Corrupted Memory File**
```python
def validate_memory_file(file_path: str) -> bool:
    """
    Validate memory file integrity.
    """
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Check for required frontmatter
        if not content.startswith('---'):
            print(f"⚠️  Missing frontmatter: {file_path}")
            return False
        
        # Parse frontmatter
        frontmatter_match = re.search(r'---\n(.*?)\n---', content, re.DOTALL)
        
        if not frontmatter_match:
            print(f"⚠️  Invalid frontmatter format: {file_path}")
            return False
        
        # Check for basic structure
        required_sections = ['memory-type', 'created']
        frontmatter = frontmatter_match.group(1)
        
        for section in required_sections:
            if section not in frontmatter:
                print(f"⚠️  Missing required field '{section}': {file_path}")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error validating {file_path}: {e}")
        return False

def auto_repair_memory_file(file_path: str):
    """
    Attempt automatic repair of corrupted memory file.
    """
    
    # Backup original
    backup_path = f"{file_path}.backup"
    shutil.copy(file_path, backup_path)
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Attempt repairs
    repaired = content
    
    # Add missing frontmatter
    if not repaired.startswith('---'):
        frontmatter = f"""---
memory-type: unknown
created: {datetime.now().isoformat()}
status: needs-review
---

"""
        repaired = frontmatter + repaired
    
    # Write repaired version
    with open(file_path, 'w') as f:
        f.write(repaired)
    
    print(f"🔧 Auto-repaired: {file_path}")
    print(f"   Backup saved: {backup_path}")
    print(f"   Please review and update frontmatter manually")
```

**Scenario 4: Embedding Generation Failure**
```python
def handle_embedding_failure(file_path: str, error: Exception):
    """
    Handle failures in embedding generation.
    """
    
    error_log = {
        'file': file_path,
        'error': str(error),
        'timestamp': datetime.now().isoformat(),
        'action_taken': 'queued_for_retry'
    }
    
    # Log error
    error_file = Path(".claude/errors/embedding-errors.json")
    
    if error_file.exists():
        with open(error_file, 'r') as f:
            errors = json.load(f)
    else:
        errors = []
    
    errors.append(error_log)
    
    with open(error_file, 'w') as f:
        json.dump(errors, f, indent=2)
    
    # Queue for retry
    retry_queue = Path(".claude/.retry-queue.json")
    
    if retry_queue.exists():
        with open(retry_queue, 'r') as f:
            queue = json.load(f)
    else:
        queue = []
    
    queue.append({
        'file': file_path,
        'retry_count': 0,
        'next_retry': (datetime.now() + timedelta(minutes=5)).isoformat()
    })
    
    with open(retry_queue, 'w') as f:
        json.dump(queue, f, indent=2)
    
    print(f"⚠️  Embedding failed for {file_path}")
    print(f"   Queued for retry in 5 minutes")
    print(f"   Error logged to: {error_file}")
```

**Agent Instruction**:
```
Robust error handling protocol:

1. Before semantic operations:
   - Check Obsidian running: check_obsidian_running()
   - If not: Warn user, use file navigation

2. For all MCP calls:
   - Wrap in try-except
   - Catch ConnectionError, TimeoutError
   - Fall back to keyword search

3. For file operations:
   - Validate file integrity: validate_memory_file()
   - If corrupted: auto_repair_memory_file()
   - Always backup before destructive ops

4. For embedding failures:
   - Log error
   - Queue for retry
   - Continue without blocking workflow

Never fail silently - always inform user of degraded mode.
```

**Verification**:
- [ ] Obsidian detection working
- [ ] MCP fallback functional
- [ ] File validation catches corruption
- [ ] Auto-repair restores basic structure
- [ ] Retry queue prevents permanent failures

**Success Criteria**: System continues functioning (with degraded capabilities) even when components fail

---

### Subtask 5.2: Performance Monitoring

**Reasoning Technique**: [[Chain of Thought]] (step-by-step metrics collection)

**Goal**: Track system health and performance over time

**Implementation**: Metrics Collection System

**`.claude/metrics/performance-log.jsonl`**:
```jsonl
{"timestamp": "2025-12-25T10:30:00Z", "operation": "session_start", "duration_ms": 2340, "memories_loaded": 12, "success": true}
{"timestamp": "2025-12-25T10:31:15Z", "operation": "semantic_search", "query": "auth patterns", "duration_ms": 450, "results_found": 8, "success": true}
{"timestamp": "2025-12-25T10:32:00Z", "operation": "memory_update", "file": "systemPatterns.md", "duration_ms": 120, "success": true}
{"timestamp": "2025-12-25T10:33:30Z", "operation": "embedding_generation", "files_processed": 3, "duration_ms": 4200, "success": true}
```

**Metrics Tracker**:
```python
import json
from datetime import datetime

class MetricsTracker:
    def __init__(self, log_file: str = ".claude/metrics/performance-log.jsonl"):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(exist_ok=True, parents=True)
    
    def log_operation(
        self,
        operation: str,
        duration_ms: float,
        success: bool,
        **metadata
    ):
        """Log a single operation with timing."""
        
        entry = {
            'timestamp': datetime.now().isoformat(),
            'operation': operation,
            'duration_ms': duration_ms,
            'success': success,
            **metadata
        }
        
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(entry) + '\n')
    
    def analyze_performance(self, hours_back: int = 24):
        """Analyze recent performance metrics."""
        
        cutoff = datetime.now() - timedelta(hours=hours_back)
        
        operations = defaultdict(list)
        
        with open(self.log_file, 'r') as f:
            for line in f:
                entry = json.loads(line)
                
                op_time = datetime.fromisoformat(entry['timestamp'])
                
                if op_time >= cutoff:
                    operations[entry['operation']].append(entry)
        
        # Calculate statistics
        report = {}
        
        for op, entries in operations.items():
            durations = [e['duration_ms'] for e in entries]
            successes = sum(1 for e in entries if e['success'])
            
            report[op] = {
                'total_calls': len(entries),
                'success_rate': successes / len(entries) if entries else 0,
                'avg_duration_ms': sum(durations) / len(durations) if durations else 0,
                'p95_duration_ms': np.percentile(durations, 95) if durations else 0,
                'p99_duration_ms': np.percentile(durations, 99) if durations else 0
            }
        
        return report

# Usage
metrics = MetricsTracker()

# Log operation
start = time.time()
results = smart_cli_lookup("auth patterns")
duration = (time.time() - start) * 1000

metrics.log_operation(
    operation="semantic_search",
    duration_ms=duration,
    success=len(results) > 0,
    query="auth patterns",
    results_found=len(results)
)

# Analyze
report = metrics.analyze_performance(hours_back=24)
print(json.dumps(report, indent=2))
```

**Performance Dashboard**:

**`.claude/dashboards/performance-dashboard.md`**:
```markdown
---
tags: #dashboard #metrics #performance
---

# 📊 Memory System Performance Dashboard

> [!abstract] Live Metrics
> Auto-updated dashboard showing system health and performance

## Last 24 Hours

### Session Start Performance
```dataviewjs
// Calculate average session start time
const metrics = JSON.parse(
    await dv.io.load(".claude/metrics/performance-log.jsonl")
);

const sessionStarts = metrics
    .filter(m => m.operation === "session_start")
    .slice(-20);

const avgDuration = sessionStarts
    .reduce((sum, m) => sum + m.duration_ms, 0) / sessionStarts.length;

dv.paragraph(`**Average**: ${(avgDuration/1000).toFixed(2)}s`);
dv.paragraph(`**P95**: ${(Math.max(...sessionStarts.map(m => m.duration_ms))/1000).toFixed(2)}s`);
```

### Semantic Search Performance
```dataviewjs
const searches = metrics
    .filter(m => m.operation === "semantic_search")
    .slice(-50);

const avgDuration = searches
    .reduce((sum, m) => sum + m.duration_ms, 0) / searches.length;

dv.paragraph(`**Average**: ${avgDuration.toFixed(0)}ms`);
dv.paragraph(`**Success Rate**: ${(searches.filter(s => s.success).length / searches.length * 100).toFixed(1)}%`);
```

### Memory Updates
```dataviewjs
const updates = metrics
    .filter(m => m.operation === "memory_update")
    .slice(-100);

dv.paragraph(`**Total Updates (24h)**: ${updates.length}`);
dv.paragraph(`**Most Updated File**: ${mostFrequent(updates.map(u => u.file))}`);
```

### Embedding Generation
```dataviewjs
const embeddings = metrics
    .filter(m => m.operation === "embedding_generation")
    .slice(-20);

const totalFiles = embeddings
    .reduce((sum, m) => sum + (m.files_processed || 0), 0);

dv.paragraph(`**Files Embedded (24h)**: ${totalFiles}`);
dv.paragraph(`**Average Generation Time**: ${(embeddings.reduce((sum, m) => sum + m.duration_ms, 0) / embeddings.length / 1000).toFixed(2)}s`);
```

## Health Indicators

### 🟢 Healthy
- Session start <5s
- Search latency <500ms
- Success rate >95%
- Embedding lag <30s

### 🟡 Degraded
- Session start 5-10s
- Search latency 500ms-1s
- Success rate 90-95%
- Embedding lag 30s-2min

### 🔴 Critical
- Session start >10s
- Search latency >1s
- Success rate <90%
- Embedding lag >2min

**Current Status**: [Auto-calculated based on metrics]
```

**Agent Instruction**:
```
Track all significant operations:

1. Wrap operations with metrics:
   ```
   metrics = MetricsTracker()
   
   start = time.time()
   result = operation()
   duration = (time.time() - start) * 1000
   
   metrics.log_operation(
       operation="operation_name",
       duration_ms=duration,
       success=bool(result),
       **additional_metadata
   )
   ```

2. Review dashboard daily:
   - Open .claude/dashboards/performance-dashboard.md
   - Check for degraded indicators
   - Investigate anomalies

3. Monthly performance review:
   - Run: metrics.analyze_performance(hours_back=720)
   - Export report
   - Identify optimization opportunities
```

**Verification**:
- [ ] Metrics logging working
- [ ] Performance analysis generating reports
- [ ] Dashboard displaying live data
- [ ] Health indicators calculating correctly

**Success Criteria**: Performance metrics provide actionable insights for system optimization

---

### Subtask 5.3: Backup & Recovery

**Reasoning Technique**: [[Plan-and-Solve]] (comprehensive backup strategy)

**Goal**: Prevent data loss, enable recovery from corruption

**Implementation**: Automated Backup System

**Backup Strategy**:

**Daily Incremental Backups**:
```bash
#!/bin/bash
# .claude/scripts/backup-incremental.sh

VAULT_PATH="/path/to/memory-vault"
BACKUP_DIR="/path/to/backups"
DATE=$(date +%Y-%m-%d)

# Create daily backup directory
mkdir -p "$BACKUP_DIR/$DATE"

# Backup only changed files (incremental)
rsync -av --delete \
    --backup --backup-dir="$BACKUP_DIR/$DATE" \
    "$VAULT_PATH/.claude/" \
    "$BACKUP_DIR/current/"

echo "✅ Incremental backup completed: $BACKUP_DIR/$DATE"

# Cleanup old backups (keep 30 days)
find "$BACKUP_DIR" -type d -mtime +30 -exec rm -rf {} \;

# Verify backup integrity
BACKUP_SIZE=$(du -sh "$BACKUP_DIR/current" | cut -f1)
echo "📦 Current backup size: $BACKUP_SIZE"
```

**Weekly Full Backups**:
```bash
#!/bin/bash
# .claude/scripts/backup-full.sh

VAULT_PATH="/path/to/memory-vault"
BACKUP_DIR="/path/to/backups/weekly"
DATE=$(date +%Y-%m-%d)

# Create compressed full backup
tar -czf "$BACKUP_DIR/memory-vault-$DATE.tar.gz" \
    -C "$VAULT_PATH" \
    .claude/

echo "✅ Full backup created: memory-vault-$DATE.tar.gz"

# Upload to cloud storage (optional)
# aws s3 cp "$BACKUP_DIR/memory-vault-$DATE.tar.gz" s3://my-backups/

# Keep only last 4 weeks
find "$BACKUP_DIR" -name "*.tar.gz" -mtime +28 -delete
```

**Recovery Procedures**:

**Scenario: Restore Single File**:
```bash
# Find latest backup of specific file
FILENAME="systemPatterns.md"
BACKUP_FILE=$(find /path/to/backups -name "$FILENAME" -type f | sort | tail -1)

# Restore
cp "$BACKUP_FILE" "/path/to/memory-vault/.claude/core/$FILENAME"

echo "✅ Restored $FILENAME from backup"
```

**Scenario: Restore Entire Memory System**:
```bash
# Stop Obsidian (to prevent conflicts)
# ...

# Restore from most recent full backup
tar -xzf /path/to/backups/weekly/memory-vault-2025-12-25.tar.gz \
    -C /path/to/memory-vault/

# Restart Obsidian
# Trigger re-embedding: Smart Connections → Refresh all embeddings

echo "✅ Full restore completed"
```

**Scenario: Point-in-Time Recovery**:
```python
def point_in_time_restore(target_date: datetime, vault_path: str, backup_dir: str):
    """
    Restore vault state to specific date.
    """
    
    # Find backup closest to target date
    backup_date = find_closest_backup(target_date, backup_dir)
    
    if not backup_date:
        print(f"❌ No backup found for {target_date}")
        return
    
    print(f"📅 Restoring to {backup_date}...")
    
    # Create safety backup of current state
    safety_backup = Path(backup_dir) / "before-restore" / datetime.now().isoformat()
    safety_backup.mkdir(parents=True, exist_ok=True)
    
    shutil.copytree(
        Path(vault_path) / ".claude",
        safety_backup / ".claude"
    )
    
    print(f"💾 Current state backed up to: {safety_backup}")
    
    # Restore target backup
    backup_path = Path(backup_dir) / backup_date
    
    shutil.rmtree(Path(vault_path) / ".claude")
    shutil.copytree(
        backup_path / ".claude",
        Path(vault_path) / ".claude"
    )
    
    print(f"✅ Restored to {backup_date}")
    print(f"⚠️  Restart Obsidian and refresh embeddings")
```

**Git Integration** (recommended):
```bash
# Initialize git in vault
cd /path/to/memory-vault
git init

# Add .gitignore
cat > .gitignore << EOF
.obsidian/
.smart-env/embeddings.json
.claude/.query-cache/
.claude/locks/
EOF

# Commit current state
git add .claude/
git commit -m "Memory state: $(date +%Y-%m-%d)"

# Daily auto-commit
cat > .claude/scripts/git-auto-commit.sh << 'EOF'
#!/bin/bash
cd /path/to/memory-vault

git add .claude/
git commit -m "Auto-commit: $(date +%Y-%m-%d-%H-%M)"

# Optional: Push to remote
# git push origin main
EOF

chmod +x .claude/scripts/git-auto-commit.sh

# Add to cron for daily execution
# 0 23 * * * /path/to/memory-vault/.claude/scripts/git-auto-commit.sh
```

**Agent Instruction**:
```
Backup awareness protocol:

1. Before destructive operations:
   - Check last backup time
   - If >24 hours: Trigger immediate backup
   
2. After significant changes:
   - Log backup recommendation
   - User should review and commit
   
3. If corruption detected:
   - Alert user immediately
   - Suggest point-in-time restore
   - Provide recovery options

4. Weekly backup verification:
   - Run: bash .claude/scripts/backup-full.sh
   - Verify: ls -lh /path/to/backups/weekly
   - Test restore (in separate directory)
```

**Verification**:
- [ ] Incremental backup script working
- [ ] Full backup script creating archives
- [ ] Single file restore tested
- [ ] Full restore tested
- [ ] Git integration (if used) committing correctly

**Success Criteria**: Complete memory system can be restored from backups within 5 minutes

---

### Subtask 5.4: Maintenance Automation

**Reasoning Technique**: [[Decomposed Prompting]] (specialized maintenance tasks)

**Goal**: Automated routine maintenance to keep system healthy

**Implementation**: Maintenance Scheduler

**`.claude/scripts/maintenance-tasks.py`**:
```python
#!/usr/bin/env python3
"""
Automated maintenance tasks for memory system.
Run daily/weekly/monthly.
"""

import shutil
from pathlib import Path
from datetime import datetime, timedelta

class MaintenanceTasks:
    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self.memory_dir = self.vault_path / ".claude"
    
    def task_cleanup_old_task_logs(self, days_to_keep: int = 30):
        """Archive task logs older than X days."""
        
        print(f"🧹 Cleaning up task logs older than {days_to_keep} days...")
        
        task_logs_dir = self.memory_dir / "task-logs"
        archive_dir = self.memory_dir / "archive" / "task-logs"
        archive_dir.mkdir(parents=True, exist_ok=True)
        
        cutoff_date = datetime.now() - timedelta(days=days_to_keep)
        
        archived_count = 0
        
        for log_file in task_logs_dir.glob("*.md"):
            file_date = datetime.fromtimestamp(log_file.stat().st_ctime)
            
            if file_date < cutoff_date:
                # Move to archive
                shutil.move(str(log_file), str(archive_dir / log_file.name))
                archived_count += 1
        
        print(f"   ✅ Archived {archived_count} old task logs")
    
    def task_cleanup_stale_locks(self, timeout_minutes: int = 30):
        """Remove locks older than timeout."""
        
        print(f"🔓 Removing stale locks (>{timeout_minutes} min old)...")
        
        locks_dir = self.memory_dir / "locks"
        
        if not locks_dir.exists():
            print(f"   ℹ️  No locks directory")
            return
        
        cutoff = datetime.now() - timedelta(minutes=timeout_minutes)
        
        removed_count = 0
        
        for lock_file in locks_dir.glob("*.lock"):
            lock_age = datetime.fromtimestamp(lock_file.stat().st_mtime)
            
            if lock_age < cutoff:
                lock_file.unlink()
                removed_count += 1
        
        print(f"   ✅ Removed {removed_count} stale locks")
    
    def task_validate_memory_integrity(self):
        """Run integrity checks on all memory files."""
        
        print("🔍 Validating memory file integrity...")
        
        issues = []
        
        for md_file in self.memory_dir.rglob("*.md"):
            if not validate_memory_file(str(md_file)):
                issues.append(str(md_file))
        
        if issues:
            print(f"   ⚠️  Found {len(issues)} files with issues:")
            for issue in issues[:10]:  # Show first 10
                print(f"      - {issue}")
            
            if len(issues) > 10:
                print(f"      ... and {len(issues) - 10} more")
        else:
            print(f"   ✅ All memory files valid")
    
    def task_optimize_embeddings(self):
        """Rebuild embeddings index for optimization."""
        
        print("⚡ Optimizing embeddings index...")
        
        # Trigger Smart Connections refresh
        # (Requires Obsidian running)
        
        embeddings_file = self.vault_path / ".smart-env" / "embeddings.json"
        
        if not embeddings_file.exists():
            print("   ⚠️  Embeddings file not found - Obsidian may not be running")
            return
        
        # Check if rebuild needed (embeddings file >7 days old)
        file_age = datetime.now() - datetime.fromtimestamp(embeddings_file.stat().st_mtime)
        
        if file_age.days > 7:
            print("   🔄 Triggering full embedding rebuild...")
            # Command to trigger Smart Connections refresh
            # (Implementation depends on Smart Connections API)
            print("   ℹ️  Manual action required: Open Obsidian → Smart Connections → Refresh")
        else:
            print(f"   ✅ Embeddings are recent ({file_age.days} days old)")
    
    def task_generate_memory_report(self):
        """Generate summary report of memory system state."""
        
        print("📊 Generating memory system report...")
        
        report = f"""# Memory System Report
Generated: {datetime.now().isoformat()}

## Summary Statistics
- Total Memory Files: {len(list(self.memory_dir.rglob('*.md')))}
- Core Memory Files: {len(list((self.memory_dir / 'core').glob('*.md')))}
- Task Logs: {len(list((self.memory_dir / 'task-logs').glob('*.md')))}
- Error Records: {len(list((self.memory_dir / 'errors').glob('*.md')))}

## Recent Activity (7 days)
"""
        
        recent_cutoff = datetime.now() - timedelta(days=7)
        recent_files = [
            f for f in self.memory_dir.rglob("*.md")
            if datetime.fromtimestamp(f.stat().st_mtime) >= recent_cutoff
        ]
        
        report += f"- Files Modified: {len(recent_files)}\n"
        report += f"- Most Active Directory: {self.find_most_active_directory(recent_files)}\n"
        
        # Write report
        report_file = self.memory_dir / "reports" / f"maintenance-report-{datetime.now().strftime('%Y-%m-%d')}.md"
        report_file.parent.mkdir(exist_ok=True)
        
        with open(report_file, 'w') as f:
            f.write(report)
        
        print(f"   ✅ Report saved: {report_file}")
    
    def find_most_active_directory(self, files: list) -> str:
        """Identify directory with most recent activity."""
        
        from collections import Counter
        
        dirs = [f.parent.name for f in files]
        
        if not dirs:
            return "None"
        
        return Counter(dirs).most_common(1)[0][0]
    
    def run_daily_maintenance(self):
        """Execute daily maintenance tasks."""
        
        print("🔧 Running Daily Maintenance\n")
        
        self.task_cleanup_stale_locks()
        self.task_validate_memory_integrity()
        
        print("\n✅ Daily maintenance complete\n")
    
    def run_weekly_maintenance(self):
        """Execute weekly maintenance tasks."""
        
        print("🔧 Running Weekly Maintenance\n")
        
        self.task_cleanup_old_task_logs()
        self.task_optimize_embeddings()
        self.task_generate_memory_report()
        
        print("\n✅ Weekly maintenance complete\n")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python maintenance-tasks.py /path/to/vault [daily|weekly]")
        sys.exit(1)
    
    vault_path = sys.argv[1]
    frequency = sys.argv[2]
    
    maintenance = MaintenanceTasks(vault_path)
    
    if frequency == "daily":
        maintenance.run_daily_maintenance()
    elif frequency == "weekly":
        maintenance.run_weekly_maintenance()
    else:
        print("❌ Invalid frequency. Use 'daily' or 'weekly'")
        sys.exit(1)
```

**Scheduling**:

**macOS/Linux (cron)**:
```bash
# Edit crontab
crontab -e

# Add daily maintenance (runs at 11 PM)
0 23 * * * /usr/bin/python3 /path/to/vault/.claude/scripts/maintenance-tasks.py /path/to/vault daily

# Add weekly maintenance (runs Sunday at midnight)
0 0 * * 0 /usr/bin/python3 /path/to/vault/.claude/scripts/maintenance-tasks.py /path/to/vault weekly
```

**Windows (Task Scheduler)**:
```powershell
# Create daily task
$action = New-ScheduledTaskAction -Execute "python" -Argument "C:\path\to\vault\.claude\scripts\maintenance-tasks.py C:\path\to\vault daily"
$trigger = New-ScheduledTaskTrigger -Daily -At 11PM
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "MemorySystemDailyMaintenance"

# Create weekly task
$action = New-ScheduledTaskAction -Execute "python" -Argument "C:\path\to\vault\.claude\scripts\maintenance-tasks.py C:\path\to\vault weekly"
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 12AM
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "MemorySystemWeeklyMaintenance"
```

**Agent Instruction**:
```
Maintenance awareness:

1. Check last maintenance run:
   - View .claude/reports/maintenance-report-YYYY-MM-DD.md
   - If >7 days old: Alert user

2. Before major operations:
   - Check for stale locks
   - Validate memory integrity
   - If issues found: Run maintenance

3. After extended downtime:
   - Trigger embedding optimization
   - Rebuild embeddings index
   - Validate all memory files

4. Monthly review:
   - Analyze maintenance reports
   - Identify recurring issues
   - Optimize maintenance tasks
```

**Verification**:
- [ ] Maintenance script running successfully
- [ ] Daily tasks executing automatically
- [ ] Weekly tasks executing automatically
- [ ] Maintenance reports generating
- [ ] Agents respect maintenance schedule

**Success Criteria**: System self-maintains with minimal manual intervention

---

### Phase 5 Completion Checkpoint

✅ Comprehensive error handling implemented
✅ Performance monitoring operational
✅ Backup and recovery procedures tested
✅ Automated maintenance running on schedule
✅ System hardened for production use

---

# 🎯 Implementation Success Verification

## Final System Validation

### End-to-End Test Scenario

**Test Objective**: Validate complete workflow from session reset to memory recovery

**Procedure**:

1. **Initial State**: Agent completes task, updates memories
2. **Session Reset**: Completely close agent platform (simulate reset)
3. **Recovery Test**: Agent starts new session
4. **Success Criteria**:
   - Agent recovers project context within 30 seconds
   - Demonstrates understanding of recent work
   - Can continue task without user re-briefing
   - Memory searches return relevant context

**Expected Output**:
```
Agent: I've loaded the context for Project Authentication System.

Recent progress:
- Completed OAuth 2.0 + PKCE implementation (see task log 2025-12-25-14-30)
- Database schema updated with user_tokens table
- Current focus: Rate limiting implementation at API gateway

Active blockers:
- Awaiting architecture review from planning agent
- Token rotation policy needs decision

I'm ready to continue. What would you like to work on?
```

### Performance Benchmarks

| Metric | Target | Acceptable | Critical |
|--------|--------|------------|----------|
| Session Start Time | <5s | <10s | >10s |
| Semantic Search Latency | <500ms | <1s | >1s |
| Memory Update Time | <200ms | <500ms | >500ms |
| Embedding Generation | <30s | <2min | >2min |
| Multi-Agent Coordination | <5s | <10s | >10s |

### Health Check Checklist

- [ ] **Infrastructure**: Obsidian running with Smart Connections active
- [ ] **MCP Integration**: Tools available in Claude Desktop/Code
- [ ] **Memory Files**: All core files present and valid
- [ ] **Embeddings**: Index up-to-date (<24h old)
- [ ] **Agent Identity**: Registry current with all active agents
- [ ] **Backups**: Latest backup <24h old
- [ ] **Maintenance**: Last maintenance run successful
- [ ] **Error Rate**: <5% failures in last 24h

---

# 📚 Operational Runbooks

## Runbook 1: New Agent Onboarding

**Scenario**: Adding a new agent to the ecosystem

**Steps**:
1. Assign unique agent ID (e.g., `claude-analysis-001`)
2. Add entry to `.claude/agent-registry.json`
3. Create agent-specific directory: `.claude/agents/[agent-id]/`
4. Create mailbox: `.claude/agent-mailbox/inbox/[agent-id]-inbox.md`
5. Provide agent with:
   - Session start protocol
   - Memory management guidelines
   - Coordination rules
6. Test agent can:
   - Query existing memories
   - Create new memories
   - Send/receive mailbox messages
   - Respect file locks

**Verification**: Agent successfully recovers context in first session

---

## Runbook 2: Memory System Migration

**Scenario**: Moving to new vault or platform

**Steps**:
1. **Backup**: Create full backup of current system
2. **Export**: Copy entire `.claude/` directory
3. **Setup New Vault**:
   - Install Obsidian + Smart Connections
   - Configure MCP server with new vault path
4. **Import**: Copy `.claude/` to new vault
5. **Rebuild Embeddings**:
   - Open Obsidian with new vault
   - Smart Connections → Refresh all embeddings
6. **Verify**: Test semantic searches return expected results
7. **Update Agent Configs**: Point all agents to new vault path
8. **Gradual Cutover**:
   - Run both systems in parallel for 1 week
   - Sync changes bidirectionally
   - Full cutover once validated

**Rollback**: Restore from backup, revert agent configs

---

## Runbook 3: Performance Degradation Response

**Scenario**: System becomes slow (session start >10s)

**Diagnosis**:
1. Check Obsidian running: `ps aux | grep Obsidian`
2. Check embedding file age: `stat .smart-env/embeddings.json`
3. Check vault size: `du -sh .claude/`
4. Review performance metrics: `python analyze-performance.py --last 24h`

**Common Causes & Fixes**:

**Cause 1: Embeddings Stale**
- **Symptom**: Embedding file >7 days old
- **Fix**: Trigger refresh: Smart Connections → Refresh all
- **Prevention**: Enable auto-refresh in plugin settings

**Cause 2: Vault Too Large**
- **Symptom**: >10K files, >5GB
- **Fix**: Archive old task logs, move to separate vault
- **Prevention**: Run weekly cleanup maintenance

**Cause 3: MCP Server Timeout**
- **Symptom**: Search queries failing/slow
- **Fix**: Restart Claude Desktop, check MCP logs
- **Prevention**: Monitor MCP server health

**Cause 4: Concurrent Agent Conflicts**
- **Symptom**: File lock timeouts
- **Fix**: Stagger agent sessions, increase timeout
- **Prevention**: Better coordination via mailbox

---

## Runbook 4: Data Corruption Recovery

**Scenario**: Memory file becomes corrupted or deleted

**Immediate Actions**:
1. **Stop All Agents**: Prevent further corruption
2. **Identify Scope**: Single file or systemic?
3. **Restore from Backup**:
   ```bash
   # Find latest good backup
   ls -lt /path/to/backups/ | head -5
   
   # Restore specific file
   cp /path/to/backup/systemPatterns.md .claude/core/
   
   # Or full restore
   tar -xzf /path/to/backup/memory-vault-2025-12-25.tar.gz
   ```
4. **Validate Restore**: Run validation script
5. **Rebuild Embeddings**: Trigger Smart Connections refresh
6. **Resume Operations**: Restart agents

**Post-Incident**:
- Document what caused corruption
- Update validation checks to catch earlier
- Review backup frequency (increase if needed)

---

# 🎓 Training & Best Practices

## For Users

### Daily Workflow

**Morning**:
1. Open Obsidian (starts Smart Connections embedding)
2. Review performance dashboard
3. Check for agent mailbox messages
4. Start agent sessions as needed

**During Work**:
- Agents handle memory updates automatically
- Review agent decisions periodically
- Respond to agent coordination requests via mailbox

**Evening**:
- Review memory updates made during day
- Run daily maintenance if not automated
- Backup if significant changes made

### Weekly Tasks

- Review maintenance reports
- Validate backup integrity
- Run pattern extraction analysis
- Update project goals in core memory files

### Monthly Tasks

- Performance analysis and optimization
- Cross-project pattern review
- Archive old completed projects
- Update agent capabilities in registry

## For Agents

### Memory Creation Guidelines

**DO**:
- ✅ Create atomic, focused memory files
- ✅ Use descriptive, searchable titles
- ✅ Include comprehensive context
- ✅ Add query anchors `%%QA:domain:topic%%`
- ✅ Link to related memories
- ✅ Update immediately after decisions

**DON'T**:
- ❌ Create duplicate memories
- ❌ Use vague titles like "Notes" or "Misc"
- ❌ Leave memories disconnected (no links)
- ❌ Delay updates (memory lag)
- ❌ Overwrite without appending (lose history)

### Search Strategy Guidelines

**Simple Queries**: Use direct semantic search
```
smart-cli lookup "authentication patterns"
```

**Complex Queries**: Use hybrid search
```
hybrid_search(
    semantic_query="API design patterns",
    keywords=["REST", "GraphQL"],
    filters={"confidence": "verified"}
)
```

**Precision Needed**: Use anchor-guided search
```
anchor_guided_search("auth", "flow", expand=True)
```

**Exploration**: Use query rewriting
```
for query in rewrite_query("database optimization"):
    results = smart_cli_lookup(query)
```

---

# 🔮 Future Enhancements

## Potential Extensions (Post-Implementation)

### Enhancement 1: Natural Language Memory Queries

**Concept**: Query memory using full natural language questions

**Implementation**:
```python
def natural_language_query(question: str) -> str:
    """
    Answer questions by querying memory and synthesizing response.
    """
    
    # Extract query intent
    intent = classify_question(question)
    
    # Retrieve relevant memories
    memories = smart_cli_lookup(question, limit=5)
    
    # Synthesize answer
    answer = synthesize_from_memories(question, memories)
    
    return answer

# Example
q = "What authentication approach did we decide on and why?"
answer = natural_language_query(q)
# Returns: "We chose OAuth 2.0 + PKCE based on decision documented
#           in systemPatterns.md on 2025-12-24. The rationale was..."
```

### Enhancement 2: Memory Summarization

**Concept**: Auto-generate summaries of memory collections

**Implementation**:
- Daily summary of all memory updates
- Project-level summary on demand
- Cross-project theme extraction

### Enhancement 3: Proactive Memory Suggestions

**Concept**: Agent suggests memory creation based on conversation

**Implementation**:
```python
def detect_memory_opportunity(conversation: list) -> dict:
    """
    Analyze conversation for knowledge worth capturing.
    """
    
    # Look for decision points
    decisions = extract_decisions(conversation)
    
    # Look for new knowledge
    knowledge = extract_learnings(conversation)
    
    # Suggest memory creation
    if decisions or knowledge:
        return {
            'suggested_memory_type': 'decision' if decisions else 'knowledge',
            'suggested_title': generate_title(decisions or knowledge),
            'suggested_content': format_as_memory(decisions or knowledge)
        }
    
    return None

# Usage during conversation
if memory_opp := detect_memory_opportunity(conversation_history):
    print(f"💡 Memory suggestion: {memory_opp['suggested_title']}")
    print(f"   Create this memory? [y/n]")
```

### Enhancement 4: Visual Memory Browser

**Concept**: Interactive UI for exploring memory graph

**Implementation**:
- Force-directed graph visualization
- Search and filter interface
- Timeline view
- Heatmap of memory density

---

# 📊 Metrics & KPIs

## Success Indicators

### Quantitative Metrics

| Metric | Baseline | 30-Day Target | 90-Day Target |
|--------|----------|---------------|---------------|
| Session Context Recovery | 100% manual | 90% automated | 95% automated |
| Memory Staleness | N/A | <24h lag | <1h lag |
| Search Relevance | N/A | 80% precision | 90% precision |
| Agent Coordination | Manual | 70% automated | 90% automated |
| System Uptime | N/A | 95% | 99% |

### Qualitative Metrics

- **User Satisfaction**: Agents require less manual context provision
- **Productivity**: Time saved on context reconstruction
- **Knowledge Retention**: Information survives session resets
- **Collaboration**: Agents coordinate effectively via shared memory
- **Reliability**: System degrades gracefully under failures

---

# 🏁 Conclusion & Next Actions

## Implementation Phases Summary

**Phase 1 (Days 1-2)**: Foundation Setup
- ✅ Obsidian + Smart Connections configured
- ✅ MCP server connected
- ✅ Directory structure established
- ✅ Basic functionality validated

**Phase 2 (Days 3-5)**: Agent Workflow Integration
- ✅ Memory protocols defined
- ✅ Session automation working
- ✅ Real-time updates implemented
- ✅ Consistency validation operational

**Phase 3 (Days 6-8)**: Advanced Features
- ✅ Semantic query optimization
- ✅ Cross-project pattern extraction
- ✅ Performance optimizations
- ✅ Knowledge graph visualization

**Phase 4 (Days 9-10)**: Multi-Agent Coordination
- ✅ Agent identity management
- ✅ Communication protocols
- ✅ Collaborative memory updates
- ✅ Conflict resolution

**Phase 5 (Days 11-12)**: Production Hardening
- ✅ Error handling and recovery
- ✅ Performance monitoring
- ✅ Backup and recovery
- ✅ Automated maintenance

## Immediate Next Steps for Implementation

### For Users:

**Week 1**:
1. **Day 1**: Complete Phase 1 (Foundation Setup)
2. **Day 2**: Validate end-to-end workflow
3. **Day 3**: Begin Phase 2 (Agent Integration)
4. **Day 4-5**: Deploy session automation
5. **Weekend**: Test with real projects

**Week 2**:
1. Complete Phases 3-4
2. Enable multi-agent coordination
3. Tune performance settings
4. Establish monitoring

**Month 1**:
- Run system in production
- Collect performance metrics
- Iterate based on learnings
- Train additional agents

### For Agents:

**Session 1** (First Use):
1. Read session start protocol
2. Execute memory recovery
3. Demonstrate context understanding
4. Update memories with first task

**Ongoing**:
- Follow memory management protocols
- Use semantic search for context retrieval
- Coordinate via mailbox when needed
- Self-assess performance using scoring system

---

## Support & Resources

**Documentation**:
- This roadmap (operational reference)
- Original analysis document (theoretical foundation)
- Script comments (implementation details)

**Troubleshooting**:
- Check performance dashboard for degradation
- Review error logs in `.claude/errors/`
- Consult runbooks for common scenarios
- Validate system health via checklist

**Community**:
- Smart Connections Discord
- Obsidian Forum
- Claude Developer Community

---

> [!success] Implementation Readiness
> This roadmap provides a comprehensive, phase-by-phase implementation plan with:
> - ✅ **52 concrete subtasks** with verification criteria
> - ✅ **Executable code examples** in Python, Bash, JSON
> - ✅ **4 operational runbooks** for common scenarios
> - ✅ **Performance targets** and success metrics
> - ✅ **Error handling** and recovery procedures
> - ✅ **Automated maintenance** scripts
> - ✅ **Multi-agent coordination** protocols
> 
> **Total Estimated Implementation Time**: 12 days (compressed schedule) to 3-4 weeks (standard pace)
> 
> **Critical Success Factors**:
> 1. Obsidian + Smart Connections reliability
> 2. MCP server stability
> 3. Agent discipline in following protocols
> 4. Regular maintenance execution
> 5. Iterative refinement based on metrics

---

*Document Status: COMPLETE*  
*Implementation Status: READY*  
*Next Action: Begin Phase 1, Subtask 1.1*
