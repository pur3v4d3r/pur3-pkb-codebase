---
tags: #meta #memory-system #quickstart #guide #sessions
aliases: [Memory System Guide, Session Start Guide, Agent Memory Usage]
status: evergreen
certainty: ^verified
created: 2026-01-06
last_updated: 2026-01-06
---

# Memory System Quickstart Guide

> [!abstract] Purpose
> Quick reference for Claude Code and Gemini Code Assist to use the agent memory system at the start of each session. This is the authoritative guide for memory system usage.

## 🚀 Session Start Protocol (Claude Code)

### Step 1: Read System Prompt
```
Read: __LOCAL-REPO/CLAUDE.md
```
**Contains**: Identity, operational modes, constitutional principles

### Step 2: Load Memory Files (Priority Order)

**Immediate Context** (read first):
1. **activeContext** — Current work-in-progress, next steps
2. **progress** — Implementation timeline, milestones

**Strategic Context** (as needed):
3. **projectbrief** — Vault purpose, goals, constraints
4. **systemPatterns** — Architectural patterns, design decisions
5. **techContext** — Technology stack, configurations

**Reference** (optional):
6. **[[00-meta/system/session-memory]]** — Human-readable session history
7. **[[00-meta/system/user-preferences]]** — Communication style, workflow patterns

### Step 3: Acknowledge Readiness

**Example Response**:
```markdown
Session initialized. Loaded memory from activeContext.md.

**Current Focus**: [summarize from activeContext]
**Last Milestone**: [from progress.md]
**Next Steps**: [from pending tasks]

Ready to continue. What would you like to work on?
```

---

## 📂 Memory System Architecture

### Two-Layer System

**1. 00-meta/ (Authoritative Metadata)**
- **Purpose**: Human-readable vault-wide metadata
- **Audience**: You (the user)
- **Update Frequency**: After significant sessions
- **Key Files**:
  - `session-memory.md` — Comprehensive session log
  - `user-preferences.md` — Workflow patterns
  - `project-tracker.md` — Active projects
  - `vault-map.md` — Structural overview
  - `mcp-setup-troubleshooting.md` — MCP configuration guide

**2. .claude/ (Agent Memory Layer)**
- **Purpose**: Agent-optimized semantic memory
- **Audience**: AI agents (Claude, Gemini)
- **Update Frequency**: Continuously during work
- **Structure**:
  - `.claude/core/` — Long-term memory (6 core files)
  - `.claude/task-logs/` — Short-term memory (30-day rolling)
  - `.claude/plans/` — Working memory (session-duration)
  - `.claude/errors/` — Error memory (failure patterns)

### Core Memory Files

| File | Purpose | When to Read |
|------|---------|--------------|
| **activeContext.md** | Current WIP, next steps | Every session start |
| **progress.md** | Timeline, milestones | Every session start |
| **projectbrief.md** | Strategic goals | When planning new work |
| **systemPatterns.md** | Architecture decisions | When making design choices |
| **techContext.md** | Tech stack, tools | When configuring or debugging |
| **memory-index.md** | Navigation hub | When unsure where info is |

---

## 🔄 Memory Update Protocol

### During Work

**Update activeContext.md**:
- Mark current task as `in_progress`
- Note blockers or issues
- Update "Currently Working On" section

**Create Task Logs** (for significant tasks):
```markdown
File: .claude/task-logs/YYYY-MM-DD-HH-MM_task-description.md

Format:
- Objective
- Steps executed
- Decisions made
- Outcome
- Related memories (wiki-links)
```

### After Task Completion

**Update progress.md**:
- Mark milestone complete
- Add actual completion date
- Log key decisions
- Update overall status percentage

**Update activeContext.md**:
- Mark task as `completed`
- Move to "Completed This Session"
- Update current focus to next task

---

## 🔍 Using Memory (Without MCP)

### Direct File Reading

**Find current focus**:
```
Read: .claude/core/activeContext.md
Look for: "Currently Working On" section
```

**Check implementation status**:
```
Read: .claude/core/progress.md
Look for: Milestone table, phase status
```

**Understand architecture**:
```
Read: .claude/core/systemPatterns.md
Look for: %%QA:architecture:*%% query anchors
```

### Search Using Grep

**Find specific topics**:
```bash
# Search core files
grep -r "memory system" .claude/core/

# Search with context
grep -A 5 -B 5 "MCP configuration" .claude/core/progress.md
```

### Query Anchor Protocol

**Format**: `%%QA:domain:topic%%`

**Namespaces**:
- `%%QA:architecture:*%%` — System design
- `%%QA:memory:*%%` — Memory system specifics
- `%%QA:workflow:*%%` — Processes and methods
- `%%QA:tools:*%%` — Technology usage
- `%%QA:setup:*%%` — Configuration procedures

**Usage**:
```bash
# Find architecture information
grep "%%QA:architecture:" .claude/core/*.md

# Find workflow guidance
grep "%%QA:workflow:" .claude/core/*.md
```

---

## 🔧 MCP Integration (When Available)

### Status Check

**MCP Configured**: See [[mcp-setup-troubleshooting]] for current status

**If MCP Working**:
- Use `lookup` tool for semantic search
- Use `connection` tool for related notes
- Use `stats` tool for coverage info

**If MCP NOT Working**:
- Fall back to direct file reading (see above)
- Use grep for text search
- Check [[mcp-setup-troubleshooting]] for resolution steps

### MCP Test Queries

```
# Test availability
Can you list your available tools?

# Test search
Use the lookup tool to search for "memory system implementation"

# Test connections
Use the connection tool to find notes related to "projectbrief.md"
```

---

## 📋 Common Workflows

### Starting New Work

1. Read [[activeContext]] for current state
2. Check [[progress]] for pending milestones
3. Review [[00-meta/system/session-memory]] for context
4. Create plan in `.claude/plans/` if needed
5. Update activeContext with new task

### Resuming After Session Reset

1. Read [[activeContext]] first (immediate context)
2. Read [[progress]] for status overview
3. Check blockers section in activeContext
4. Continue from "Next Immediate Step"

### Handling Errors

1. Document error in `.claude/errors/YYYY-MM-DD_error-description.md`
2. Include: error trace, root cause, resolution steps
3. Update activeContext with blocker status
4. Cross-reference in techContext if config-related

### Completing Phase/Milestone

1. Update [[progress]] milestone table
2. Mark phase status as complete (✅)
3. Add actual completion date
4. Log key decisions in decision log
5. Update [[activeContext]] to next phase
6. Create task log summarizing phase work

---

## 🚨 Troubleshooting

### Can't Find Information

**Check order**:
1. activeContext — Recent work
2. progress — Timeline
3. memory-index — Navigation hub
4. [[00-meta/system/session-memory]] — Full history

### Memory Files Out of Date

**Update protocol**:
1. Read current state from files
2. Ask user for clarification
3. Update files with correct information
4. Document update in file's "Document History"

### Conflicting Information

**Resolution**:
1. **00-meta/** is authoritative for vault-wide info
2. **.claude/** is authoritative for agent-specific info
3. When conflict, ask user which is correct
4. Update incorrect source

---

## 📊 Memory Integrity Checks

### Before Each Session

```bash
# Verify core files exist
ls .claude/core/

# Check for recent updates
ls -lt .claude/core/ | head -6

# Verify embeddings count
ls .smart-env/multi/ | wc -l
```

### File Checksums (from memory-index.md)

**Expected files**:
- memory-index.md
- core/projectbrief.md
- core/systemPatterns.md
- core/techContext.md
- core/activeContext.md
- core/progress.md

**Validation**:
```bash
# Count should be 6
ls .claude/core/*.md | wc -l
```

---

## 🎯 Success Indicators

### Session Start (<30 seconds)

✅ Loaded activeContext.md
✅ Understood current focus
✅ Identified next steps
✅ No blockers preventing work

### During Work

✅ activeContext updated continuously
✅ Task logs created for significant work
✅ Blockers documented immediately
✅ Cross-references maintained

### Session End

✅ progress.md updated with status
✅ activeContext reflects current state
✅ All decisions documented
✅ Next session priorities clear

---

## 🔗 Related Documentation

### Authoritative Guides (00-meta/)
- [[00-meta/memory-system/claude-memory-system-guide]] — System architecture overview
- [[00-meta/memory-system/mcp-setup-troubleshooting]] — MCP configuration guide
- [[00-meta/system/session-memory]] — Session history
- [[00-meta/system/user-preferences]] — Communication preferences

### Agent Memory (.claude/)
- memory-index — Master navigation hub
- activeContext — Current WIP
- progress — Implementation status

---

## 📝 Quick Reference Card

### Every Session Start
```
1. Read: .claude/core/activeContext.md
2. Read: .claude/core/progress.md
3. Acknowledge: Current focus + next steps
```

### During Work
```
1. Update: activeContext "Currently Working On"
2. Create: Task logs for significant work
3. Document: Blockers immediately
```

### Session End
```
1. Update: progress.md milestones
2. Update: activeContext completed tasks
3. Set: Next session priorities
```

---

## Document History

- **2026-01-06**: Initial creation for memory system usage guidance
- **Status**: Active, reference every session

---

_This is the definitive guide for using the memory system. Update when workflows change._
