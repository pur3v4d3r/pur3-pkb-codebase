---
memory-type: index
created: 2026-01-06
modified: 2026-01-06
project: memory-system-implementation
tags: [#memory-system, #index, #navigation]
confidence: verified
status: active
---

# 🧠 Agent Memory Bank Index

> [!abstract] Navigation Hub
> Centralized directory for agent memory system. This index provides navigation to all memory layers and documents the relationship between [[00-meta]] (authoritative vault metadata) and `.claude/` (agent-optimized memory layer).

## 📐 Memory System Architecture

**System Purpose**: Enable persistent cross-session context for AI agents via semantic retrieval

**Integration**: Smart Connections Plugin → MCP Server → Claude Desktop

**Key Distinction**:
- [[00-meta]] = Authoritative vault-wide metadata (human-readable, system documentation)
- `.claude/` = Agent-specific memory layer (semantic search optimized, task logging)

%%QA:memory:system-architecture%%
The memory system uses a complementary dual-structure approach where 00-meta/ serves as the authoritative vault metadata source, while .claude/ provides agent-optimized memory with semantic retrieval via Smart Connections MCP integration.

---

## 📁 Directory Structure

### Core Memory (Long-Term)

**Location**: `.claude/core/`

**Persistence**: Permanent, rarely deleted

**Update Frequency**: Infrequent (architectural changes only)

| File | Purpose | Status |
|------|---------|--------|
| [[projectbrief]] | Strategic context, goals, constraints | ⚙️ Initializing |
| [[systemPatterns]] | Architecture patterns, design decisions | ⚙️ Initializing |
| [[techContext]] | Technology stack, integrations | ⚙️ Initializing |
| [[activeContext]] | Current focus, active tasks, WIP | ⚙️ Initializing |
| [[progress]] | Implementation timeline, milestones | ⚙️ Initializing |
| [[productContext]] | (Future) User needs, requirements | 📝 Planned |

### Task Logs (Short-Term)

**Location**: `.claude/task-logs/`

**Persistence**: 30-day rolling window

**Format**: `YYYY-MM-DD-HH-MM_task-description.md`

**Contents**: Task objectives, steps executed, decisions made, outcomes

Recent task logs listed automatically:
```dataview
LIST
FROM ".claude/task-logs"
SORT file.ctime DESC
LIMIT 10
```

### Active Plans (Working Memory)

**Location**: `.claude/plans/`

**Persistence**: Session-duration or until task completion

**Contents**: Proposed approaches, analysis, draft implementations

Active plans:
```dataview
LIST
FROM ".claude/plans"
WHERE status != "completed"
SORT file.mtime DESC
```

### Error Memory

**Location**: `.claude/errors/`

**Purpose**: Failure pattern recognition, learning from mistakes

**Contents**: Error traces, root cause analysis, resolution steps

Recent errors:
```dataview
LIST
FROM ".claude/errors"
SORT file.ctime DESC
LIMIT 5
```

---

## 🔗 Relationship to 00-meta/

**[[00-meta]]** is the **authoritative source** for vault-wide metadata:
- [[00-meta/system/session-memory|session-memory.md]] — Human-readable session tracking
- [[00-meta/system/project-tracker|project-tracker.md]] — Project status and priorities
- [[00-meta/system/user-preferences|user-preferences.md]] — Workflow patterns
- [[00-meta/system/vault-map|vault-map.md]] — Structural overview

**`.claude/`** provides **agent-optimized memory**:
- Semantic search via query anchors (`%%QA:domain:topic%%`)
- MCP-accessible for automated context retrieval
- Granular task logging for agent learning
- Event-driven automation hooks

%%QA:memory:meta-claude-relationship%%
00-meta/ and .claude/ are complementary: 00-meta/ is authoritative human-readable metadata, while .claude/ is agent-optimized with semantic search capabilities via MCP integration.

---

## 🔍 Semantic Retrieval via MCP

### Available Tools

**Via Claude Desktop with Smart Connections MCP**:

| Tool | Purpose | Example Query |
|------|---------|---------------|
| `lookup` | Semantic search by text | "Find notes about authentication patterns" |
| `connection` | Find similar notes to a file | "Notes related to systemPatterns.md" |
| `stats` | View embedding coverage | "Show memory bank statistics" |
| `validate` | Check data integrity | "Validate Smart Connections data" |

### Query Anchor Protocol

**Syntax**: `%%QA:domain:specific-topic%%`

**Purpose**: Create highly searchable semantic anchors within memory files

**Namespaces**:
- `%%QA:architecture:*%%` — System design decisions
- `%%QA:memory:*%%` — Memory system specifics
- `%%QA:errors:*%%` — Error patterns and solutions
- `%%QA:workflow:*%%` — Process and methodology
- `%%QA:tools:*%%` — Technology and tool usage

%%QA:retrieval:query-anchors%%
Query anchors use the format %%QA:domain:topic%% to create semantic search landmarks. Namespacing by domain enables precise retrieval of specific knowledge areas.

---

## 📊 Memory Integrity

### Checksums (Auto-Updated)

| File | Last Modified | Checksum |
|------|---------------|----------|
| `memory-index.md` | 2026-01-06 | - |
| `core/projectbrief.md` | - | - |
| `core/systemPatterns.md` | - | - |
| `core/techContext.md` | - | - |
| `core/activeContext.md` | - | - |
| `core/progress.md` | - | - |

### Validation Commands

```bash
# Check Smart Connections indexing status
smart-cli stats

# Verify memory files are embedded
smart-cli connection ".claude/memory-index.md"

# Test semantic search
smart-cli lookup "memory system architecture"
```

---

## 🚀 Quick Start Guide

### For New Sessions

1. **Load Context**: Read [[activeContext]] for current focus
2. **Check Tasks**: Review recent task logs
3. **Semantic Search**: Use MCP lookup tool for specific information

### For Task Completion

1. **Log Task**: Create entry in `.claude/task-logs/` with format `YYYY-MM-DD-HH-MM_task-name.md`
2. **Update Context**: Modify [[activeContext]] with new status
3. **Document Decisions**: Add to [[systemPatterns]] if architectural
4. **Update Progress**: Log milestone in [[progress]]

### For Errors

1. **Create Error Log**: `.claude/errors/YYYY-MM-DD_error-type.md`
2. **Document**: Error trace, root cause, resolution
3. **Cross-Reference**: Link to related task logs
4. **Update Patterns**: Add to [[systemPatterns]] if recurring

%%QA:workflow:quick-start%%
New sessions begin by reading activeContext, checking recent task logs, and using semantic search for specific information. Task completion requires logging in task-logs/, updating activeContext, and documenting decisions in systemPatterns.

---

## 📝 Standard Metadata Format

All memory files MUST use this frontmatter:

```yaml
---
memory-type: [core | task-log | plan | error]
created: YYYY-MM-DD
modified: YYYY-MM-DD
project: project-identifier
tags: [#domain, #type, #status]
confidence: [speculative | provisional | moderate | established | verified]
status: [active | completed | deprecated]
---
```

**Template Location**: `.claude/templates/memory-template.md` (to be created)

---

## 🔧 System Status

**Implementation Phase**: Phase 1 — Foundation Setup

**Smart Connections**: ✅ Operational (8,383 embeddings)

**MCP Server**: ⚙️ Pending configuration

**Core Files**: ⚙️ Initializing

**Last Updated**: 2026-01-06

---

## 🔗 Related Documentation

- [[999-codebase+pkb/integrating-smart-connection-with-memory-system/memory-system-implementation-roadmap|Memory System Implementation Roadmap]]
- [[999-codebase+pkb/integrating-smart-connection-with-memory-system/smart-connections-llm-integration-guide|Smart Connections Integration Guide]]
- [[__LOCAL-REPO/CLAUDE|CLAUDE.md System Prompt]]
- [[00-meta/system/session-memory|00-meta Session Memory]]

%%QA:memory:documentation-links%%
Complete implementation documentation is available in 999-codebase+pkb/integrating-smart-connection-with-memory-system/ directory, including roadmap, integration guide, and setup scripts.
