---
tags: #memory-system #core #skills #capabilities
aliases: [Active Skills, Installed Skills, Skill Registry]
status: evergreen
certainty: ^verified
created: 2026-01-06
last_updated: 2026-01-06
memory-type: core
---

# Active Skills Registry

> [!abstract] Purpose
> This document tracks all active skills installed in `.claude/skills/`, their purposes, trigger conditions, and integration with the PKB workflow.

## Installation Summary

**Total Active Skills**: 20
**Installation Dates**:
- Batch 1 (6 skills): 2026-01-06
- Batch 2 (7 skills): 2026-01-07
**Location**: `d:\10_pur3v4d3r's-vault\.claude\skills\`

---

## Tier 1: Core PKB Skills (Newly Installed)

### 1. skill-creator
**Purpose**: Meta-skill for creating new skills
**Trigger**: When user wants to create/update skills
**Key Features**:
- Progressive disclosure design (metadata → SKILL.md → bundled resources)
- Skill initialization scripts
- Quality assurance protocols
- Packaging and distribution

**Impact**: Force multiplier - enables building custom PKB-specific skills

**References**: `SKILL.md` (210 lines)

---

### 2. prompt-engineering
**Purpose**: Advanced prompt pattern frameworks
**Trigger**: Creating, optimizing, or implementing prompts
**Key Features**:
- Few-shot learning implementation
- Chain-of-thought reasoning
- Prompt optimization workflows
- Template systems architecture
- System prompt design

**Impact**: Direct alignment with SPES Active Project #3

**References**: `SKILL.md` (302 lines), `references/` (5 pattern files)

**Integration**:
- SPES Component Library
- Sequential Workflow Engine
- Prompt templates and macros

---

### 3. verification-before-completion
**Purpose**: Quality enforcement & honesty protocol
**Trigger**: Before claiming work complete, fixed, or passing
**Key Features**:
- Iron Law: "NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE"
- Gate function (identify → run → read → verify → claim)
- Red-green cycle for regression tests
- Prevents "should work now" without evidence

**Impact**: Prevents false completion claims, enforces testing

**References**: `SKILL.md` (140 lines)

**Aligns With**: CLAUDE.md loop prevention protocol

---

### 4. systematic-debugging
**Purpose**: Root cause analysis before fixes
**Trigger**: Any bug, test failure, or unexpected behavior
**Key Features**:
- Iron Law: "NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST"
- 4-phase process (root cause → pattern → hypothesis → implementation)
- Multi-component system diagnostics
- Backward data flow tracing
- 3-fix rule (question architecture after 3 failed attempts)

**Impact**: Faster problem resolution, fewer rework cycles

**References**: `SKILL.md` (297 lines), `root-cause-tracing.md`, `defense-in-depth.md`, `condition-based-waiting.md`

**Aligns With**: CLAUDE.md thinking protocol, loop prevention

---

### 5. subagent-driven-development
**Purpose**: Multi-agent coordination patterns
**Trigger**: Complex tasks requiring multiple specialized agents
**Key Features**:
- Spec reviewer → Implementer → Quality reviewer workflow
- Systematic delegation with verification
- Agent output validation
- Cross-agent handoff protocols

**Impact**: Systematic task decomposition with quality gates

**References**: `SKILL.md` + 3 agent prompts

**Integration**: Works with Task tool and parallel agent execution

---

### 6. __scientific-skills
**Purpose**: 125+ scientific computing capabilities
**Trigger**: Scientific computing, research, data analysis tasks
**Key Features**:
- 26+ scientific databases (PubMed, ChEMBL, UniProt, etc.)
- 54+ Python packages (RDKit, Scanpy, PyTorch Lightning, etc.)
- Multi-omics workflows
- Literature review and scientific writing
- Statistical analysis and visualization

**Impact**: Massive domain expertise expansion for PKB development

**References**: `README.md`, `docs/scientific-skills.md`, `docs/examples.md`

**Domains Covered**:
- Bioinformatics & Genomics
- Cheminformatics & Drug Discovery
- Machine Learning & AI
- Data Analysis & Visualization
- Scientific Communication

---

## Pre-Existing Skills (Previously Installed)

### 7. anthropic-api-expert
**Purpose**: Anthropic Claude API expertise
**Trigger**: Anthropic, Claude, API, prompt engineering questions
**Installed**: 2025-12-31

---

### 8. claude-code
**Purpose**: Claude Code CLI expertise
**Trigger**: Claude Code, CLI, skills, commands, hooks questions
**Installed**: 2025-12-25

---

### 9. claude-command-builder
**Purpose**: Interactive slash command creator
**Trigger**: Creating commands, slash commands, command templates
**Installed**: 2025-12-25

---

### 10. claude-hook-builder
**Purpose**: Interactive hook creator
**Trigger**: Creating hooks, PreToolUse, PostToolUse, hook validation
**Installed**: 2025-12-25

---

### 11. claude-mcp-expert
**Purpose**: Model Context Protocol (MCP) integration
**Trigger**: MCP, MCP servers, installation, configuration questions
**Installed**: 2025-12-25

---

### 12. claude-settings-expert
**Purpose**: settings.json configuration expertise
**Trigger**: settings.json, permissions, allow/deny rules, sandbox questions
**Installed**: 2025-12-25

---

### 13. claude-skill-builder
**Purpose**: Skill creation and scaffolding
**Trigger**: Creating skills, building skills, skill templates
**Installed**: 2025-12-25

---

## Skill Activation Protocol

**How Skills Work**:
1. **Metadata loaded** — All skill names + descriptions always in context (~100 words each)
2. **Skill triggers** — When user request matches description keywords
3. **SKILL.md loaded** — Full skill instructions loaded (<5k words)
4. **Resources accessed** — Bundled resources loaded as needed

**Current Behavior**:
- Skills automatically trigger based on keyword matching in descriptions
- No manual invocation needed
- Multiple skills can activate simultaneously for complex tasks

---

## Integration with PKB Systems

### SPES (Sequential Prompt Engineering System)
**Active Skills**: prompt-engineering, skill-creator
**Use Case**: Component library development, template creation, workflow design

### Memory System
**Active Skills**: verification-before-completion, systematic-debugging
**Use Case**: Quality enforcement, error prevention, loop avoidance

### Research & Analysis
**Active Skills**: __scientific-skills
**Use Case**: Literature review, data analysis, cognitive science research

### Development Workflow
**Active Skills**: subagent-driven-development, verification-before-completion, systematic-debugging
**Use Case**: Task decomposition, quality gates, systematic problem-solving

---

## Skill Usage Statistics

**Session**: 2026-01-06
**Skills Installed This Session**: 6
**Total Skills Active**: 13
**Skills Used**: (to be tracked)

---

## Next Steps

1. **Test skill activation** with trigger keywords
2. **Create PKB-specific skills** using skill-creator
3. **Integrate with SPES** prompt engineering workflows
4. **Document skill usage patterns** in session-memory

---

## Query Anchors Summary

This document contains query anchors for:
- `%%QA:skills:*%%` — Skill tracking and metadata
- `%%QA:capabilities:*%%` — Capability inventory

---

## Document History

- **2026-01-06 22:50**: Initial creation after Tier 1 skill installation
- **Status**: Active, updated after skill installations

---

_This file should be updated when skills are added, removed, or significantly changed._
