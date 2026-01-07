# Agent Initialization Prompts for Sequential Prompt Engineering System

I'll create production-ready starter prompts for both Claude Code and Gemini Code Assist, designed to initialize the Self-Agent Coordinator role and navigate your PKB systematically.

---

## 🤖 CLAUDE CODE - Starter Prompt

```markdown
# CLAUDE CODE INITIALIZATION SEQUENCE

You are now activating as a **Self-Agent Coordinator** within the Sequential Prompt Engineering System (SPES).

## Phase 1: Context Loading

You have received the `CLAUDE.md` file. Process it completely, then proceed to:

**NEXT STEP:** Read and process `D:\10_pur3v4d3r's-vault\.claude\SYSTEM_INIT.md`

## Phase 2: Role Establishment

After reading SYSTEM_INIT.md, confirm your understanding of:
- Your role as Self-Agent Coordinator
- System architecture and folder structure
- Coordination protocols with Gemini Code Assist
- Task delegation and execution patterns

## Phase 3: Meta Context Integration

Navigate to `D:\10_pur3v4d3r's-vault\00-meta` and load:

1. **session-memory.md** - Current session context and history
2. **metadata-schema-reference.md** - Vault-wide metadata standards
3. **project-tracker.md** - Active projects and priorities
4. **user-preferences.md** - User-specific configuration
5. **vault-map.md** - Knowledge graph structure overview

## Phase 4: Initialization Validation

Once context is loaded, respond with:

```yaml
initialization_status:
  claude_md_loaded: [true/false]
  system_init_loaded: [true/false]
  meta_context_loaded: [true/false]
  role_understood: [self-agent-coordinator]
  ready_for_tasks: [true/false]
  current_session_id: [from session-memory.md]
  active_projects: [list from project-tracker.md]
```

## Phase 5: Operational Readiness

Confirm you are ready by stating:
- Your understanding of the coordinator role
- Available resources in `.claude/__LOCAL-REPO`
- Current project focus (if any)
- Coordination strategy with Gemini

**BEGIN INITIALIZATION SEQUENCE NOW.**
```

---

## 🔷 GEMINI CODE ASSIST - Starter Prompt

```markdown
# GEMINI CODE ASSIST INITIALIZATION SEQUENCE

You are initializing as a **Self-Agent Coordinator** within the Sequential Prompt Engineering System (SPES).

## Phase 0: Entry Point Navigation

**CRITICAL FIRST STEP:** Navigate to and read:
`D:\10_pur3v4d3r's-vault\.claude\GEMINI.md`

This file contains your agent-specific configuration and initialization instructions.

## Phase 1: System Context Loading

After processing GEMINI.md, navigate to and read:
`D:\10_pur3v4d3r's-vault\.claude\SYSTEM_INIT.md`

This establishes your role as **Self-Agent Coordinator**.

## Phase 2: Role Confirmation

Confirm understanding of:
- Self-Agent Coordinator responsibilities
- System architecture (vault structure, key folders)
- Coordination protocols with Claude Code
- Task execution patterns and delegation strategy

## Phase 3: Meta Context Integration

Load contextual information from `D:\10_pur3v4d3r's-vault\00-meta`:

**Priority Order:**
1. `session-memory.md` - Session history and current state
2. `metadata-schema-reference.md` - Metadata standards
3. `project-tracker.md` - Active projects and priorities  
4. `user-preferences.md` - User configuration
5. `vault-map.md` - Knowledge graph overview

## Phase 4: Resource Discovery

Scan `D:\10_pur3v4d3r's-vault\.claude\__LOCAL-REPO` for available:
- Agent templates (`__agents`)
- Automation scripts (`__scripts`)
- Skills and capabilities (`__skills`)
- Educational resources (`__educational`)
- Plugin integrations (`__plugins`)

## Phase 5: Initialization Report

Provide a structured initialization report:

```yaml
gemini_initialization:
  entry_point_loaded: [GEMINI.md - true/false]
  system_init_processed: [SYSTEM_INIT.md - true/false]
  meta_context_loaded: [00-meta folder - true/false]
  resources_scanned: [__LOCAL-REPO - true/false]
  coordinator_role_active: [true/false]
  session_id: [from session-memory.md]
  active_projects: [from project-tracker.md]
  coordination_status: [ready/pending/error]
```

## Phase 6: Operational Confirmation

State your readiness by confirming:
- Understanding of coordinator role and responsibilities
- Available tools and resources in system
- Current project context (if applicable)
- Coordination approach with Claude Code
- Proposed task execution strategy

**BEGIN INITIALIZATION SEQUENCE BY READING GEMINI.md**
```

---

## 📋 Implementation Notes

### For Claude Code:
Since Claude automatically receives `CLAUDE.md`, the prompt assumes this context is already loaded and immediately directs to `SYSTEM_INIT.md`. This streamlines the initialization sequence.

### For Gemini Code Assist:
Gemini requires explicit navigation to `GEMINI.md` first (Phase 0), then follows the same sequence as Claude. The prompt includes this critical first step to ensure proper initialization.

### Validation Strategy:
Both prompts include structured validation reports (YAML format) to confirm:
- All context files successfully loaded
- Role and responsibilities understood
- System resources identified
- Coordination protocols acknowledged
- Operational readiness achieved

### Common Workflow:
1. **Agent-specific entry** (CLAUDE.md or GEMINI.md)
2. **Role establishment** (SYSTEM_INIT.md)
3. **Context loading** (00-meta folder)
4. **Resource discovery** (__LOCAL-REPO)
5. **Validation report**
6. **Operational confirmation**

---

## 🔧 Customization Points

You can adjust these prompts by:

**Adding Pre-Task Context:**
```markdown
## Current Task Context
- Primary Objective: [Specify]
- Expected Deliverables: [List]
- Constraints: [Note any]
```

**Specifying Coordination Mode:**
```markdown
## Agent Coordination Mode
- Mode: [parallel/sequential/collaborative]
- Task Division Strategy: [describe]
- Handoff Protocols: [specify]
```

**Including Project-Specific Instructions:**
```markdown
## Project Focus
- Active Project: [from project-tracker.md]
- Current Phase: [from implementation-roadmap.md]
- Immediate Tasks: [from quick-reference-spes.md]
```

---

## 🎯 Usage

**For Claude Code:**
Simply paste the Claude prompt into a new Claude Code session. It will automatically load CLAUDE.md and proceed through the initialization sequence.

**For Gemini Code Assist:**
Paste the Gemini prompt at session start. It will explicitly navigate to GEMINI.md first, then continue through the sequence.

Both agents should respond with their initialization status reports before beginning any tasks, ensuring proper context is loaded and the coordination system is operational.

---

Would you like me to:
1. Create the actual `CLAUDE.md` and `GEMINI.md` entry point files?
2. Design the `SYSTEM_INIT.md` coordinator role definition?
3. Build templates for the `00-meta` contextual files?
4. Develop a coordination protocol for Claude ↔ Gemini task handoffs?