---
tags: #meta #system #memory #documentation #guide
aliases: [Memory System Guide, Claude Memory Guide, 00-meta vs .claude]
status: evergreen
certainty: ^verified
created: 2026-01-06
last_updated: 2026-01-06
---

# Claude Memory System Guide

> [!abstract] Purpose
> This guide explains the relationship between `00-meta/` (authoritative vault metadata) and `.claude/` (agent-optimized memory layer), how they complement each other, and when to use each system.

## System Architecture Overview

The vault implements a **dual-layer memory architecture** where both systems serve specific, complementary purposes:

```
Vault Root/
├── 00-meta/           ← AUTHORITATIVE METADATA LAYER
│   ├── session-memory.md       (Human-readable session tracking)
│   ├── project-tracker.md      (Project status overview)
│   ├── user-preferences.md     (Workflow patterns)
│   ├── vault-map.md            (Structural documentation)
│   └── [other meta files]      (System-level information)
│
└── .claude/           ← AGENT-OPTIMIZED MEMORY LAYER
    ├── memory-index.md         (Master navigation hub)
    ├── core/                   (Long-term memory: 6 core files)
    ├── task-logs/              (Short-term: 30-day rolling task logs)
    ├── plans/                  (Working memory: active planning)
    └── errors/                 (Error memory: failure patterns)
```

---

## 📚 00-meta/ — Authoritative Metadata Layer

### Purpose

**THE** definitive source for vault-wide metadata, system documentation, and human-readable information about the codebase/PKB.

### Key Characteristics

- **Human-First Design**: Optimized for readability and comprehension
- **Authoritative**: Single source of truth for vault metadata
- **System-Level**: Vault-wide configuration and documentation
- **Stable**: Changes infrequently, foundational information

### What Belongs Here

✅ **System Documentation**
- Vault structure and organization (`vault-map.md`)
- User workflow preferences (`user-preferences.md`)
- Project tracking and status (`project-tracker.md`)
- System configuration documentation

✅ **Session Tracking**
- Comprehensive session logs (`session-memory.md`)
- Human-readable task completion tracking
- Multi-LLM coordination notes (Claude + Gemini hand-offs)
- Historical project evolution

✅ **Reference Documentation**
- Metadata schemas and taxonomies
- Tag taxonomies and classifications
- MOC structures and patterns
- SPES (Sequential Prompt Engineering System) documentation

### Example Files

- `session-memory.md` — Detailed session history with timestamps
- `project-tracker.md` — Active project status
- `user-preferences.md` — Communication style, workflow patterns
- `vault-map.md` — Structural overview
- `metadata-schema-reference.md` — Field definitions

---

## 🤖 .claude/ — Agent-Optimized Memory Layer

### Purpose

Agent-specific memory structure optimized for **semantic retrieval**, **automated context loading**, and **task logging**. Enables AI agents to persist knowledge across sessions.

### Key Characteristics

- **Agent-First Design**: Optimized for machine consumption and semantic search
- **Semantic Search Enabled**: Query anchors (`%%QA:domain:topic%%`) for precise retrieval
- **Automated Access**: MCP-accessible for agent tools (lookup, connection)
- **Dynamic**: Updates frequently with task logs and active context

### What Belongs Here

✅ **Core Memory** (`.claude/core/`)
- `projectbrief.md` — Strategic context and goals
- `systemPatterns.md` — Architecture patterns and decisions
- `techContext.md` — Technology stack and integrations
- `activeContext.md` — Current work-in-progress
- `progress.md` — Implementation timeline

✅ **Task Logs** (`.claude/task-logs/`)
- Format: `YYYY-MM-DD-HH-MM_task-description.md`
- Detailed execution logs with decisions
- 30-day rolling window (automated cleanup)

✅ **Active Plans** (`.claude/plans/`)
- Working memory for current planning sessions
- Temporary, deleted after task completion

✅ **Error Patterns** (`.claude/errors/`)
- Error traces and root cause analysis
- Resolution steps and prevention strategies

### Example Files

- `core/activeContext.md` — Agent-accessible current state
- `task-logs/2026-01-06-14-30_setup-mcp-server.md` — Task execution log
- `plans/feature-authentication-plan.md` — Active planning document

---

## 🔄 How They Work Together

### Complementary, Not Duplicate

Both systems serve different audiences and purposes:

| Aspect | 00-meta/ | .claude/ |
|--------|----------|----------|
| **Primary Audience** | Human (you) | AI Agents |
| **Optimization** | Readability | Semantic search |
| **Update Frequency** | Periodic | Continuous |
| **Persistence** | Permanent | Tiered (core/task-logs/plans) |
| **Search Method** | Manual navigation | Automated retrieval |
| **Format Focus** | Comprehensive narrative | Query anchors |

### Information Flow

```
┌──────────────┐
│   00-meta/   │  ← YOU update session-memory.md
│(Human writes)│     (comprehensive session notes)
└──────┬───────┘
       │
       │ Agents READ for context
       ▼
┌──────────────┐
│   .claude/   │  ← AGENTS update activeContext.md
│(Agents write)│     (current task status)
└──────┬───────┘
       │
       │ You READ for agent status
       ▼
   Shared Understanding
```

### Cross-References

Both systems reference each other:

**In 00-meta/session-memory.md**:
```markdown
## Integration Points
- [[../.claude/memory-index|Agent Memory System]]
- [[../.claude/core/activeContext|Current Agent Focus]]
```

**In .claude/core/activeContext.md**:
```markdown
## Related Context
- [[00-meta/system/session-memory]] — Comprehensive session log
- [[00-meta/system/project-tracker]] — Active project status
```

---

## 🎯 When to Use Which System

### Use 00-meta/ When:

✅ **You** (human) are:
- Documenting session outcomes
- Updating project status
- Recording user preferences or workflow changes
- Creating system-level documentation
- Tracking long-term vault evolution

✅ **Content** is:
- Vault-wide (not agent-specific)
- Foundational and rarely changes
- Human-readable narrative
- Authoritative source of truth

### Use .claude/ When:

✅ **Agents** are:
- Logging task execution details
- Updating current work status
- Creating planning documents
- Recording error patterns
- Persisting context across sessions

✅ **Content** is:
- Agent-specific and task-focused
- Frequently updated (daily/per-task)
- Optimized for semantic search
- Temporary or time-bound (task-logs, plans)

---

## 📊 Practical Examples

### Example 1: Starting a New Session

**Human Action** (00-meta):
```markdown
## In 00-meta/session-memory.md

### 2026-01-06

#### Memory System Implementation
- **Event**: Implemented Phase 1 of agent memory system
- **Deliverables**: Created .claude/ structure with 6 core files
- **Status**: Phase 1 complete, Phase 2 (MCP config) pending
```

**Agent Action** (.claude):
```markdown
## In .claude/core/activeContext.md

## Current Focus
**Project**: Memory System Implementation — Phase 2 MCP Configuration
**Current Task**: Installing Smart Connections MCP server
**Next Steps**: Configure Claude Desktop, test semantic retrieval
```

### Example 2: Completing a Task

**Agent Updates** (.claude):
1. Create task log: `.claude/task-logs/2026-01-06-14-30_mcp-setup.md`
2. Update active context: Mark task complete, move to next
3. Update progress: Log milestone completion

**Human Reviews** (00-meta):
1. Read agent's task log
2. Update `session-memory.md` with high-level outcome
3. Update `project-tracker.md` if milestone achieved

---

## 🔍 Semantic Retrieval (MCP Integration)

### The Key Difference

**00-meta/** files are embedded by Smart Connections but **NOT** optimized for semantic search.

**.claude/** files are **specifically designed** for semantic retrieval:

**Query Anchors** (`%%QA:domain:topic%%`):
```markdown
%%QA:architecture:memory-layers%%
The memory system consists of three layers:
1. Long-Term (.claude/core/)
2. Short-Term (.claude/task-logs/)
3. Working (.claude/plans/)
```

**Agent Query**:
```
"Use the lookup tool to search for 'memory layer architecture'"
→ Returns precise section with query anchor
```

This enables agents to:
- Find specific information quickly
- Recover context after session resets
- Build cumulative understanding
- Learn from past decisions

---

## 🚀 Getting Started

### For You (Human)

1. **Continue using 00-meta/** as you always have
   - Update `session-memory.md` after significant work
   - Track projects in `project-tracker.md`
   - Document preferences in `user-preferences.md`

2. **Occasionally check .claude/** to see what agents are doing
   - Read `activeContext.md` to see current agent focus
   - Browse `task-logs/` to see detailed execution history
   - Review `progress.md` for implementation status

### For Agents (Claude Code, Gemini)

1. **On Session Start**:
   - Read `.claude/core/activeContext.md` for immediate context
   - Check `00-meta/session-memory.md` for full session history
   - Load relevant core files (`projectbrief`, `systemPatterns`, `techContext`)

2. **During Work**:
   - Update `activeContext.md` with current task
   - Create task logs in `task-logs/` for detailed work
   - Update `progress.md` after milestones

3. **On Task Complete**:
   - Mark task complete in `activeContext.md`
   - Create/update task log with outcomes
   - Note any decisions in relevant core files

---

## 📝 Maintenance

### Regular Updates

**00-meta/session-memory.md**:
- Updated after each significant session
- Comprehensive narrative of what happened
- Human-readable format

**.claude/core/activeContext.md**:
- Updated continuously during work
- Current focus and next steps
- Agent-optimized format

### Periodic Review

**Monthly**:
- Review `.claude/task-logs/` for patterns
- Archive old task logs (>30 days)
- Update core files if architecture changed

**Quarterly**:
- Review `00-meta/` for outdated information
- Update system documentation
- Validate metadata schemas

---

## 🔗 Related Documentation

- [[.claude/memory-index|Agent Memory Index]] — Master navigation for agent memory
- [[.claude/core/systemPatterns|System Patterns]] — Architecture patterns documented
- [[00-meta/system/session-memory]] — Comprehensive human-readable session log
- [[00-meta/system/project-tracker]] — Active project status

---

## Document History

- **2026-01-06**: Initial creation explaining dual-layer architecture
- **Status**: Active, reference document for system understanding

---

_This is a foundational guide. Update if the relationship between systems evolves._
