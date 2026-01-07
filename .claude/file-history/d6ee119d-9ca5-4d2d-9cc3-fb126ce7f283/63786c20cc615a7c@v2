---
memory-type: core
created: 2026-01-06
modified: 2026-01-06
project: pkb-vault-operations
tags: [#memory-system, #core, #strategy, #pkb, #vault-purpose]
confidence: verified
status: active
---

# Project Brief: Personal Knowledge Base & Multi-LLM Collaboration Vault

> [!abstract] Strategic Context
> This vault serves as a Personal Knowledge Base (PKB) optimized for multi-LLM collaboration, combining human knowledge management with AI agent memory persistence. The vault integrates [[Obsidian]], [[Claude Code]], [[Gemini Code Assist]], and semantic retrieval systems to create a living, queryable knowledge graph.

## Context

### Why This Exists

**Problem Statement**: Traditional PKBs are optimized for human navigation but lack agent-accessible memory structures. AI agents lose context between sessions, requiring manual re-briefing and context reconstruction.

**Solution**: A dual-layer architecture combining:
1. **Human Layer** ([[00-meta]]) — Authoritative metadata, readable documentation
2. **Agent Layer** (`.claude/`) — Semantic search optimized memory with MCP integration

%%QA:strategy:vault-purpose%%
The vault solves the context persistence problem for AI agents while maintaining human-readable knowledge management. It uses Smart Connections for semantic embedding and MCP for agent-accessible retrieval.

---

## Project Goals

### Primary Objectives

1. **Knowledge Graph Building**
   - Comprehensive [[Wiki-Link]] network across all notes
   - Semantic relationships discoverable via embeddings
   - Cross-project pattern recognition

2. **Agent Memory Persistence**
   - Context survives session resets
   - Agents recover project state in <30 seconds
   - Task logging enables learning from past work

3. **Multi-LLM Coordination**
   - [[Claude Code]] and [[Gemini Code Assist]] share memory
   - Hand-off protocols preserve context
   - Complementary strengths utilized (Claude: reasoning, Gemini: execution)

4. **Prompt Engineering Excellence**
   - [[SPES|Sequential Prompt Engineering System]] component library
   - Reusable prompt patterns
   - Meta-cognitive workflow optimization

%%QA:goals:agent-memory%%
Agent memory persistence enables agents to recover project context after session resets by reading core memory files and using semantic search to retrieve relevant task logs and decisions.

---

## Scope & Constraints

### In Scope

**Knowledge Management**:
- PKB architecture using [[Zettelkasten]]-inspired principles
- [[MOC|Maps of Content]] for domain navigation
- Atomic notes with high [[Wiki-Link]] density
- [[Dataview]], [[Templater]], and [[QuickAdd]] automation

**Agent Integration**:
- [[Smart Connections]] auto-embedding system
- [[MCP|Model Context Protocol]] semantic retrieval
- Memory hierarchy (Core → Task-logs → Plans → Errors)
- [[Query Anchor Protocol]] for precise search

**Prompt Engineering**:
- [[SPES]] component library
- Prompt templates and macros
- Constitutional AI patterns
- Meta-cognitive frameworks

**Development Projects**:
- Technical research and documentation
- Code examples and implementations
- LLM application patterns
- Agent SDK development

%%QA:scope:in-scope%%
In-scope activities include PKB architecture, agent integration via Smart Connections MCP, prompt engineering system development, and technical project documentation.

### Out of Scope

❌ **NOT a task manager** — Use [[00-meta/project-tracker]] or external tools for project management

❌ **NOT a CRM** — Customer/contact management handled externally

❌ **NOT source code versioning** — Code lives in external repos, linked via [[__LOCAL-REPO]]

❌ **NOT a publishing platform** — Notes are for internal knowledge, not public content

### Constraints

**Environment**:
- Windows 11 operating system
- Obsidian as vault interface
- VS Code with Claude Code extension
- Git for version control

**Technical Limits**:
- Smart Connections: 8,383+ embeddings (currently)
- MCP server: Single vault path configuration
- Query response time: <30 seconds target
- Embedding latency: ~30 seconds for new files

%%QA:constraints:technical%%
Technical constraints include Windows environment, Smart Connections embedding capacity (8k+ currently), and MCP single-vault limitation. Target response time for semantic search is under 30 seconds.

---

## Success Criteria

### Measurable Outcomes

**Agent Context Recovery**:
- [ ] Cold start → Full context in <30 seconds
- [ ] Semantic search relevance >85%
- [ ] Zero manual context re-briefing

**Knowledge Graph Quality**:
- [ ] Every note has 2+ [[Wiki-Link|Wiki-Links]] in and out
- [ ] Orphan notes <5% of total
- [ ] MOCs cover all major domains

**Prompt Engineering System**:
- [ ] [[SPES]] Phase 1 complete ✅
- [ ] Component library operational
- [ ] Reusable patterns documented

**Memory System**:
- [ ] Smart Connections MCP configured
- [ ] Core memory files initialized
- [ ] Task logging automated

%%QA:success:metrics%%
Success is measured by agent context recovery speed (<30s), semantic search relevance (>85%), knowledge graph connectivity (orphans <5%), and SPES completion (Phase 1 done).

---

## Stakeholders & Roles

**Primary User** (pur3v4d3rpk):
- Role: Project Manager, Knowledge Architect
- Delegates tasks to AI agents
- Defines strategic direction
- Reviews and approves implementations

**[[Claude Code]]**:
- Role: PKB Architect, Prompt Component Librarian
- Strengths: Extended thinking, nuanced language, system prompts
- Responsibilities: Complex reasoning, long-form content, cross-domain synthesis

**[[Gemini Code Assist]]**:
- Role: Execution Specialist, Code Generator
- Strengths: Structured reasoning, code execution, quick iterations
- Responsibilities: Technical documentation, code generation, task decomposition

**Smart Connections Plugin**:
- Role: Semantic Embedding Engine
- Automatically indexes vault content
- Generates embeddings (TaylorAI/bge-micro-v2 model)
- Stores in `.smart-env/multi/` for MCP access

%%QA:roles:stakeholders%%
The vault has three primary stakeholders: the user (pur3v4d3rpk) as project manager, Claude Code for reasoning and architecture, and Gemini Code Assist for execution and code generation. Smart Connections provides semantic embedding infrastructure.

---

## Strategic Alignment

### Active Projects (from [[00-meta/session-memory]])

1. **[[SPES|Sequential Prompt Engineering System]]** — ✅ Phase 1 complete
2. **Memory System** — 🟡 Implementation in progress (THIS PROJECT)
3. **Self-Documenting Dataview** — 📝 Planned
4. **Prompt Engineering System Integration** — 📝 Planned

### Current Focus

**Priority 1**: Memory system foundation (Phase 1-2)
- Create `.claude/` structure ✅
- Initialize core memory files ⚙️
- Configure MCP server 📝
- Test semantic retrieval 📝

**Priority 2**: Agent optimization
- Query anchor implementation
- Event-driven automation
- Performance scoring

**Priority 3**: Knowledge graph enrichment
- Increase [[Wiki-Link]] density
- Build domain MOCs
- Cross-reference validation

%%QA:alignment:current-focus%%
Current strategic focus is on memory system foundation (Phase 1-2), specifically creating the .claude/ structure, initializing core files, configuring MCP server, and testing semantic retrieval.

---

## Related Memories

- [[systemPatterns]] — Architecture and design decisions
- [[techContext]] — Technology stack and integrations
- [[activeContext]] — Current work-in-progress
- [[progress]] — Implementation timeline and milestones
- [[00-meta/session-memory]] — Human-readable session tracking
- [[00-meta/project-tracker]] — Project status overview
- [[memory-index|Memory Index]] — Navigation hub for memory system

%%QA:memory:related-files%%
Related memory files include systemPatterns (architecture), techContext (technology), activeContext (current work), progress (timeline), and 00-meta files for authoritative vault metadata.

---

## Query Anchors for Semantic Search

%%QA:strategy:pkb-architecture%%
The PKB uses a dual-layer architecture: human-readable metadata in 00-meta/ and agent-optimized memory in .claude/ with Smart Connections semantic search via MCP integration.

%%QA:goals:multi-llm-coordination%%
Multi-LLM coordination leverages Claude's reasoning strengths and Gemini's execution capabilities through shared memory and hand-off protocols documented in session-memory.md.

%%QA:success:agent-context-recovery%%
Agent context recovery success is defined as: cold start to full context in under 30 seconds, with semantic search relevance exceeding 85%, and zero manual re-briefing required.

---

## Document History

- **2026-01-06**: Initial creation during Phase 1 foundation setup
- **Status**: Active, evolving as vault grows

---

_This is a living document. Update as strategic priorities shift or new projects emerge._
