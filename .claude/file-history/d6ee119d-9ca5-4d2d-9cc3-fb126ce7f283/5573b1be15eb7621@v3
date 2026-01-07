---
tags: #meta #readme #index #navigation #system
aliases: [00-meta README, Meta Index, Meta Navigation]
status: evergreen
certainty: ^verified
created: 2026-01-06
last_updated: 2026-01-06
---

# 00-meta: Authoritative Vault Metadata & Documentation

> [!abstract] Purpose
> This is **THE** authoritative meta folder for all vault-wide metadata, system documentation, and human-readable information about the codebase/PKB. All vault metadata originates here.

---

## 📁 Folder Organization

### 🖥️ [system/](system/) — Core Vault Metadata
**Purpose**: Essential vault-wide metadata and configuration
**Audience**: Human (you) and AI agents
**Update Frequency**: After significant sessions

| File | Purpose | When to Read |
|------|---------|--------------|
| **[session-memory.md](system/session-memory.md)** | Comprehensive session log | Session start, context recovery |
| **[user-preferences.md](system/user-preferences.md)** | Communication style, workflow patterns | New agent sessions |
| **[project-tracker.md](system/project-tracker.md)** | Active project status | Planning new work |
| **[vault-map.md](system/vault-map.md)** | Structural overview | Understanding organization |
| **[metadata-schema-reference.md](system/metadata-schema-reference.md)** | Field definitions | Creating/updating notes |

### 🧠 [memory-system/](memory-system/) — AI Memory System
**Purpose**: Agent memory system documentation and guides
**Audience**: AI agents (Claude Code, Gemini)
**Update Frequency**: When memory system changes

| File | Purpose | When to Read |
|------|---------|--------------|
| **[memory-system-quickstart.md](memory-system/memory-system-quickstart.md)** | Session start protocol | **EVERY session start** |
| **[claude-memory-system-guide.md](memory-system/claude-memory-system-guide.md)** | System architecture overview | Understanding memory layers |
| **[mcp-setup-troubleshooting.md](memory-system/mcp-setup-troubleshooting.md)** | MCP configuration guide | MCP setup/debugging |

### 📚 [spes/](spes/) — Sequential Prompt Engineering System
**Purpose**: Complete SPES documentation suite
**Audience**: Human and AI for prompt engineering
**Update Frequency**: When SPES system evolves

| File | Purpose | When to Read |
|------|---------|--------------|
| **[00-spes-documentation-index.md](spes/00-spes-documentation-index.md)** | SPES master index | **Start here** |
| **[01-spes-master-operations-manual.md](spes/01-spes-master-operations-manual.md)** | Complete system reference | Deep understanding |
| **[02-spes-quick-start-guide.md](spes/02-spes-quick-start-guide.md)** | 15-minute quick start | Fast productivity |
| **[03-llm-integration-protocol.md](spes/03-llm-integration-protocol.md)** | AI assistant instructions | Operating as SPES Librarian |
| **[04-component-library-reference.md](spes/04-component-library-reference.md)** | Component creation guide | Building prompts |
| **[05-troubleshooting-diagnostics-guide.md](spes/05-troubleshooting-diagnostics-guide.md)** | Problem solving | Fixing issues |

### 🔗 [reference/](reference/) — Reference Guides & Navigation
**Purpose**: Reference materials and navigational MOCs
**Audience**: Human and AI
**Update Frequency**: When references change

| File | Purpose | When to Read |
|------|---------|--------------|
| **[reference-moc.md](reference/reference-moc.md)** | Master reference navigation | Finding resources |
| **[tag-taxonomy.md](reference/tag-taxonomy.md)** | Tag system reference | Tagging notes |

### 📦 [archive/](archive/) — Large/Generated Files
**Purpose**: Historical and generated documentation
**Audience**: Reference only
**Update Frequency**: Rarely

| File | Size | Purpose |
|------|------|---------|
| **folder-index.md** | 896 KB | Generated folder listing |
| **folder-structure-.claude-2025-12-23.md** | 110 KB | Historical structure |
| **pkb-master-documentation.md** | 256 KB | PKB master docs |
| **structure_2025-12-24T23-31-40-934Z.txt** | <1 KB | Structure snapshot |

---

## 🚀 Quick Start Guides

### For AI Agents (Claude Code/Gemini) at Session Start

**Priority Reading Order**:
1. ✅ **[[memory-system/memory-system-quickstart]]** — Read FIRST every session
2. **[[.claude/core/activeContext]]** — Current work-in-progress
3. **[[.claude/core/progress]]** — Implementation timeline
4. **[[system/session-memory]]** — Full session history
5. **[[system/user-preferences]]** — Communication style

### For Human (Pur3v4d3r)

**Common Tasks**:
- **Update session log**: Edit [system/session-memory.md](system/session-memory.md)
- **Track projects**: Edit [system/project-tracker.md](system/project-tracker.md)
- **Use SPES**: Start at [spes/00-spes-documentation-index.md](spes/00-spes-documentation-index.md)
- **Find references**: Browse [reference/reference-moc.md](reference/reference-moc.md)

---

## 🔄 Relationship with .claude/ Memory System

### Complementary, Not Duplicate

**00-meta/** (Authoritative Metadata Layer):
- Human-readable vault metadata
- Comprehensive narrative documentation
- Permanent vault-wide information
- Source of truth for system config

**.claude/** (Agent-Optimized Memory Layer):
- Agent-specific semantic memory
- Query anchors for semantic search
- Task logs with 30-day rolling window
- Working memory and error patterns

### Information Flow

```
┌──────────────┐
│   00-meta/   │  ← YOU update session-memory.md
│ (Human writes)│     (comprehensive session notes)
└──────┬───────┘
       │
       │ Agents READ for context
       ▼
┌──────────────┐
│   .claude/   │  ← AGENTS update activeContext.md
│(Agents write) │     (current task status)
└──────┬───────┘
       │
       │ You READ for agent status
       ▼
   Shared Understanding
```

### Cross-References

**From 00-meta to .claude**:
- [[system/session-memory]] links to [[.claude/core/activeContext]]
- [[memory-system/memory-system-quickstart]] references [[.claude/memory-index]]

**From .claude to 00-meta**:
- [[.claude/core/activeContext]] links to [[system/session-memory]]
- [[.claude/memory-index]] acknowledges [[00-meta]] as authoritative source

---

## 📋 Usage Protocols

### Session Start Protocol

**For Claude Code**:
```
1. Read: 00-meta/memory-system/memory-system-quickstart.md
2. Load: .claude/core/activeContext.md
3. Load: .claude/core/progress.md
4. Reference: 00-meta/system/session-memory.md (if needed)
5. Acknowledge: Current focus + next steps
```

**For Gemini Code Assist**:
```
1. Read: 00-meta/system/session-memory.md (full context)
2. Check: .claude/core/activeContext.md (current state)
3. Coordinate: Check for hand-off notes
4. Continue: From documented next steps
```

### Update Protocol

**After Significant Work**:
1. Human updates **[system/session-memory.md](system/session-memory.md)** with high-level summary
2. Agents update **[[.claude/core/activeContext]]** with detailed task status
3. Agents update **[[.claude/core/progress]]** with milestone completion
4. Both reference each other for full context

---

## 🔍 Finding Information

### By Category

| Need | Look In |
|------|---------|
| **Current agent work** | .claude/core/activeContext.md |
| **Session history** | system/session-memory.md |
| **Project status** | system/project-tracker.md |
| **User preferences** | system/user-preferences.md |
| **Memory system guide** | memory-system/memory-system-quickstart.md |
| **SPES documentation** | spes/00-spes-documentation-index.md |
| **References & guides** | reference/reference-moc.md |
| **Archive materials** | archive/ folder |

### Search Strategies

**Direct Navigation**:
```bash
# List all system files
ls 00-meta/system/

# Search for topic
grep -r "topic" 00-meta/
```

**Wiki-Link Navigation**:
- Start at this README
- Follow wiki-links to relevant documents
- Use MOC files (reference-moc.md, spes-index.md)

---

## 📊 Maintenance

### Regular Updates

**After Each Session**:
- Update [system/session-memory.md](system/session-memory.md)
- Check [system/project-tracker.md](system/project-tracker.md)

**When Preferences Change**:
- Update [system/user-preferences.md](system/user-preferences.md)

**When System Evolves**:
- Update [system/vault-map.md](system/vault-map.md)
- Update memory system docs in memory-system/

### Integrity Checks

**Verify Structure**:
```bash
# Check all subdirectories exist
ls -la 00-meta/

# Verify key files present
ls 00-meta/system/session-memory.md
ls 00-meta/memory-system/memory-system-quickstart.md
```

**Check Cross-References**:
- Ensure wiki-links resolve correctly
- Verify paths after file moves
- Update references after reorganization

---

## 🎯 Success Indicators

### Well-Organized System

✅ **Files properly categorized** in subdirectories
✅ **README navigates to all key documents**
✅ **Cross-references work** (no broken links)
✅ **Agents find information** in <30 seconds
✅ **Human finds information** quickly

### Healthy Metadata

✅ **session-memory.md updated** after each significant session
✅ **project-tracker.md reflects** current project status
✅ **user-preferences.md captures** workflow patterns
✅ **Memory system docs sync** with .claude/ implementation

---

## 🔗 Related Documentation

### Within This Folder
- **Quick Start**: [[memory-system/memory-system-quickstart]] (AI agents start here)
- **SPES**: [[spes/00-spes-documentation-index]] (Prompt engineering system)
- **References**: [[reference/reference-moc]] (Master reference hub)

### External Links
- **Agent Memory**: [[.claude/memory-index]] (Agent memory navigation)
- **System Prompt**: [[__LOCAL-REPO/CLAUDE]] (Claude Code identity)
- **Agents**: [[__LOCAL-REPO/__agents/___README/agents]] (99 specialized agents)

---

## 📝 Document History

- **2026-01-06**: Initial README creation
  - Organized files into subdirectories (system, memory-system, spes, reference, archive)
  - Created master navigation structure
  - Documented relationship with .claude/ memory system
- **Status**: Active, update when organization changes

---

## 🚨 Important Notes

### For AI Agents

1. **00-meta is AUTHORITATIVE** for vault-wide metadata
2. **Read memory-system-quickstart.md** at EVERY session start
3. **Update .claude/ memory**, NOT 00-meta/ (unless documenting in session-memory)
4. **Cross-reference both systems** for complete context

### For Human

1. **00-meta is YOUR space** for comprehensive documentation
2. **Check .claude/core/activeContext.md** to see what agents are doing
3. **Update session-memory.md** after significant work
4. **This README is the master index** - bookmark it

---

_This is the definitive 00-meta organization guide. Update when structure evolves._
