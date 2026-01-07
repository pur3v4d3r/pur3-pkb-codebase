---
tags: 
  - claude-code 
  - multi-agent-systems 
  - ai-orchestration 
  - agentic-architecture 
  - prompt-engineering 
  - agent-coordination 
  - pkm-integration
aliases: 
  - Multi-Agent Claude Code
  - Agent Orchestration
  - Subagent Systems
  - Coordinated AI Agents
status: evergreen
certainty: verified-stable
type: reference
freshness:
  domain-volatility: moderate
  last-verified: 2026-01-06
prerequisites:
  hard: 
  - Claude Code fundamentals
  - Markdown basics
  - YAML syntax
  soft: 
  - Prompt engineering
  - Software architecture patterns
  - Distributed systems concepts
enables:
  direct: 
  - Production agent workflows
  - Team coordination automation
  - Complex task decomposition
  related: 
  - MCP server integration
  - Custom command systems
  - Agentic PKM workflows
---

> [!comprehensive-reference] 📚 Multi-Agent Systems with Claude Code
> - **Generated**:: 2026-01-06
> - **Version**:: 1.0
> - **Exploration Depth**:: 3/4 (Depth-first across 5 primary dimensions)
> - **Search Count**:: 10 targeted searches
> - **Confidence**:: Verified through official documentation + real-world implementations

> [!abstract]
> **Executive Overview**
> [**Multi-Agent-Claude-Code-Architecture**:: A system where a coordinating Claude instance (the main agent) delegates specialized tasks to purpose-built subagents, each with isolated context windows, custom system prompts, and restricted tool access, enabling 90.2% performance improvements over single-agent approaches for complex development workflows.]^verified-stable
>
> Claude Code includes a native multi-agent orchestration system that transforms it from a single assistant into a coordinated team of specialists. Rather than requiring external frameworks, the architecture is file-based: agents are defined as markdown files with YAML frontmatter, stored in `.claude/agents/` directories, and automatically discovered by the main Claude instance. The coordinator pattern is elegantly simple—the main Claude agent (general-purpose) acts as the orchestrator, analyzing tasks and delegating to specialized subagents based on description matching, explicit invocation, or workflow patterns. This reference covers the complete architecture, proven coordination patterns, agent engineering best practices, and production implementation strategies.

> [!how-to-use-this]
> **Navigation Guide**
> This reference is structured for progressive understanding: start with architecture fundamentals if new to Claude Code agents, move to design patterns for orchestration strategies, then proceed to implementation details for building your system. Each section includes working examples, anti-patterns to avoid, and real-world coordination strategies. Use the synthesis section for mental models and cross-domain connections to related systems like MCP servers and custom commands.

## 📑 Table of Contents

- [Architecture Fundamentals](#architecture-fundamentals)
  - [Native Agent System Overview](#native-agent-system-overview)
  - [File System Structure](#file-system-structure)
  - [Agent Definition Format](#agent-definition-format)
  - [Configuration Hierarchy](#configuration-hierarchy)
- [The Coordinator Pattern](#the-coordinator-pattern)
  - [Main Agent as Orchestrator](#main-agent-as-orchestrator)
  - [No Agent-to-Agent Communication](#no-agent-to-agent-communication)
  - [Delegation Mechanisms](#delegation-mechanisms)
- [Multi-Agent Design Patterns](#multi-agent-design-patterns)
  - [Sequential Pipeline Pattern](#sequential-pipeline-pattern)
  - [Parallel Execution Pattern](#parallel-execution-pattern)
  - [Shared State Coordination](#shared-state-coordination)
  - [Hook-Based Automation](#hook-based-automation)
  - [Output Style Orchestration](#output-style-orchestration)
- [Agent Engineering](#agent-engineering)
  - [System Prompt Architecture](#system-prompt-architecture)
  - [Tool Restriction Strategies](#tool-restriction-strategies)
  - [Model Selection Economics](#model-selection-economics)
  - [Description Field Optimization](#description-field-optimization)
- [Implementation Architecture](#implementation-architecture)
  - [File System Design](#file-system-design)
  - [Context Isolation Benefits](#context-isolation-benefits)
  - [Real-World Agent Examples](#real-world-agent-examples)
- [Coordination Strategies](#coordination-strategies)
  - [Task Analysis and Routing](#task-analysis-and-routing)
  - [State Management Across Agents](#state-management-across-agents)
  - [Error Handling and Rollback](#error-handling-and-rollback)
- [Production Patterns](#production-patterns)
  - [Development Workflow Integration](#development-workflow-integration)
  - [Team Collaboration Strategies](#team-collaboration-strategies)
  - [Observability and Debugging](#observability-and-debugging)
- [Synthesis & Mastery](#synthesis--mastery)
- [PKB Integration](#pkb-integration)
- [Metadata & Attribution](#metadata--attribution)
- [Related Topics for PKB Expansion](#related-topics-for-pkb-expansion)

---

## Architecture Fundamentals

### Native Agent System Overview

[**Claude-Code-Subagent-System**:: A first-class architectural feature of Claude Code (not a third-party extension) where specialized AI agents operate in isolated context windows with custom system prompts and restricted tool access, automatically discovered and invoked by the main Claude instance based on task analysis or explicit user direction.]^verified-stable

> [!definition] Subagents vs. Coordinator
> **Subagents** are specialized Claude instances with their own context windows, defined in markdown files with YAML frontmatter. The **coordinator** is not a separate file—it's the main Claude agent (the "general-purpose" agent) that you interact with directly. The coordinator analyzes tasks, routes them to appropriate subagents, and synthesizes their results.

The architecture emerged from Anthropic's internal research showing that multi-agent systems with [[Claude Opus 4]] as the lead agent and [[Claude Sonnet 4]] subagents outperformed single-agent Claude Opus 4 by [**Performance-Improvement**:: 90.2% on internal research evaluations, achieved through task decomposition into parallel, specialized workstreams that prevented context pollution and leveraged domain expertise.]^verified-stable

> [!key-claim] Context Isolation as Core Advantage
> [**Context-Isolation-Benefit**:: Each subagent maintains a separate conversation history and context window from the main agent and other subagents, preventing the "context pollution" that degrades performance in long conversations where unrelated information competes for attention and reduces focus on the current subtask.]^verified-stable
>
> This isolation enables:
> - **Focus**: Subagents see only information relevant to their specialized task
> - **Scale**: Main conversation doesn't bloat with implementation details from every subtask
> - **Parallelization**: Multiple subagents can work simultaneously without shared context conflicts
> - **Quality**: Specialized system prompts remain effective without dilution from unrelated context

> [!example] Context Pollution Scenario
> **Without subagents**: You ask Claude to "build a user dashboard with analytics." The main conversation fills with:
> - Database schema exploration
> - API endpoint debugging
> - Frontend component iterations  
> - CSS styling attempts
> - Test file generation
> - Git commit message drafting
>
> By message 50, Claude struggles to remember the original requirements because context is saturated with implementation minutiae.
>
> **With subagents**: Main agent maintains high-level orchestration ("use backend-engineer → frontend-specialist → code-reviewer"), while each specialist's detailed work happens in isolated context. Main conversation stays focused on coordination and decision points.

### File System Structure

Claude Code discovers agents through a **hierarchical file system** approach:

```
~/.claude/                          # User-level (global)
├── agents/
│   ├── code-reviewer.md           # Available in all projects
│   ├── security-auditor.md
│   └── documentation-writer.md
└── settings.json                   # Global configuration

[project-root]/
├── .claude/
│   ├── agents/                    # Project-level
│   │   ├── domain-expert.md      # Project-specific agent
│   │   ├── integration-tester.md
│   │   └── architect.md
│   └── commands/                  # Custom slash commands
│       ├── review.md
│       └── deploy.md
├── CLAUDE.md                      # Project context
└── CLAUDE.local.md                # Personal overrides (gitignored)
```

> [!key-claim] Scope Hierarchy
> [**Agent-Scope-Precedence**:: When agent names conflict between user-level and project-level definitions, project-level agents take precedence, allowing projects to override global agent behavior with domain-specific expertise while maintaining consistent agent names across the team.]^verified-stable

**Why this matters**: Your team can share project-specific agents via version control (commit `.claude/agents/*.md`), while individual developers maintain personal agents globally. A project might override the global "architect" agent with one specialized in your specific tech stack.

### Agent Definition Format

[**Agent-Definition-Structure**:: A markdown file with YAML frontmatter containing metadata (name, description, tools, model) followed by the system prompt content that defines the agent's role, capabilities, workflow, and constraints.]^verified-stable

> [!definition] Complete Agent File Format
> ```markdown
> ---
> name: agent-name
> description: When to invoke this agent (CRITICAL for auto-routing)
> tools: tool1, tool2, tool3  # Optional - inherits all if omitted
> model: sonnet|opus|haiku|inherit  # Optional - defaults to current
> permissionMode: default  # Optional
> skills: skill1, skill2  # Optional - auto-load specific skills
> ---
> 
> # System Prompt Content (Markdown)
> 
> You are an expert [domain specialist].
> 
> ## Role
> [Define specific responsibility]
> 
> ## When Invoked
> [Describe trigger conditions]
> 
> ## Workflow
> 1. [Step one]
> 2. [Step two]
> 3. [Return results in specific format]
> 
> ## Key Practices
> - [Best practice 1]
> - [Best practice 2]
> 
> ## Constraints
> - [What NOT to do]
> - [Boundary conditions]
> ```

> [!methodology-and-sources] Frontmatter Field Semantics
> **`name`** (required): Identifier for explicit invocation ("Use the code-reviewer agent..."). Should be hyphenated lowercase.
>
> **`description`** (required): [**Description-Field-Purpose**:: Natural language explanation of when this agent should be invoked; Claude analyzes this field during automatic delegation to match agent capabilities with task requirements.]^verified-stable This is the most critical field for automatic routing. Include terms like "use PROACTIVELY" or "MUST BE USED" to boost auto-activation.
>
> **`tools`** (optional): [**Tool-Restriction-Pattern**:: Comma-separated list of allowed tools (e.g., "Read, Grep, Glob") that constrains agent capabilities for safety; omitting this field allows the agent to inherit all tools available to the main thread.]^verified-stable Use this to create read-only analysis agents or restrict destructive operations.
>
> **`model`** (optional): Override the model for this specific agent. Use `haiku` for 3x cost savings on routine tasks, `opus` for complex reasoning, or `inherit` to use the main thread's model.
>
> **`permissionMode`** (optional): Control permission behavior for this agent's tool usage.
>
> **`skills`** (optional): Auto-load specific [[Skills]] when this agent is invoked, useful for domain-specific knowledge injection.

> [!example] Real-World Agent: Code Quality Reviewer
> ```markdown
> ---
> name: code-quality-reviewer
> description: Use PROACTIVELY after code is written or modified. Expert code review specialist for quality, security, and maintainability. Use immediately after implementation.
> tools: Read, Grep, Glob, Bash
> model: opus
> ---
> 
> You are a senior code reviewer ensuring high standards of code quality and security.
> 
> When invoked:
> 1. Run `git diff` to see recent changes
> 2. Focus review on modified files
> 3. Check for:
>    - Logic errors and bugs that could cause system failures
>    - Security vulnerabilities and data protection issues
>    - Performance problems impacting user experience
>    - Maintainability issues increasing technical debt
>    - Code style consistency with project standards
> 
> ## Review Priorities (in order)
> 1. **Critical bugs** - Functionality-breaking issues
> 2. **Security** - Vulnerabilities and data exposure
> 3. **Performance** - User-facing slowdowns
> 4. **Maintainability** - Technical debt accumulation
> 5. **Style** - Consistency with codebase patterns
> 
> ## Output Format
> Provide structured feedback:
> - **Critical Issues**: [List with severity]
> - **Recommendations**: [Actionable improvements]
> - **Positive Notes**: [What's done well]
> 
> Be specific with file paths and line numbers.
> ```

### Configuration Hierarchy

Claude Code uses a **scope-based precedence system** for configuration:

```
Managed (enterprise) 
    ↓ (overrides)
Project (.claude/settings.json)
    ↓ (overrides)
User (~/.claude/settings.json)
```

[**Configuration-Scope-Hierarchy**:: More specific configuration scopes override broader ones, with managed (enterprise-deployed) settings having highest precedence, followed by project-specific, then user global settings; this enables team standards enforcement while allowing project customization.]^verified-stable

> [!application-context] When Scope Matters
> **Scenario**: Your enterprise mandates certain security scanning agents must always be available. These are defined in managed settings and cannot be overridden by project or user configurations.
>
> **Your team** wants a project-specific "architect" agent that understands your microservices patterns. This lives in `.claude/agents/architect.md` and overrides any global architect agent.
>
> **You personally** prefer a different code review agent with stricter linting. This lives in `~/.claude/agents/code-reviewer.md` but is overridden by the project's version when working in team codebases.

---

## The Coordinator Pattern

### Main Agent as Orchestrator

> [!key-claim] Coordinator IS the Main Agent
> [**Coordinator-Architecture**:: The "coordinator agent" is not a separate agent file but rather the main Claude instance (general-purpose agent) that the user interacts with directly; it analyzes tasks, delegates to specialized subagents, aggregates results, and maintains high-level conversation continuity.]^verified-stable
>
> **This is a critical architectural insight**: You don't create a separate "coordinator.md" file. Instead, you influence the main agent's coordination behavior through:
> 1. Agent descriptions (what each agent does)
> 2. Output styles (workflow mode selection)
> 3. CLAUDE.md instructions (delegation patterns)
> 4. Custom commands (orchestration templates)

The main agent becomes a coordinator through **emergent behavior** rather than explicit programming. When you have well-defined agents with clear descriptions, Claude automatically recognizes opportunities for delegation:

```
User: "Build a user authentication system"

Main Agent (internal reasoning):
├─ Analyze: Complex multi-component task
├─ Decompose:
│  ├─ Requirements definition → backend-engineer agent
│  ├─ Security review → security-auditor agent  
│  └─ Test generation → test-engineer agent
├─ Delegate: Invoke agents sequentially or parallel
└─ Synthesize: Combine results, handle conflicts
```

> [!example] Implicit vs. Explicit Coordination
> **Implicit coordination** (automatic):
> ```
> User: "Review and improve the authentication module"
> 
> Main Agent: [Analyzes task]
>              [Matches "review" + "authentication" to code-reviewer's description]
>              [Automatically invokes code-reviewer agent]
>              [Returns synthesized findings]
> ```
>
> **Explicit coordination** (manual):
> ```
> User: "Use the security-auditor agent to check for vulnerabilities,
>        then use the performance-optimizer to identify bottlenecks"
> 
> Main Agent: [Invokes security-auditor as requested]
>              [Waits for results]
>              [Invokes performance-optimizer with context from security audit]
>              [Synthesizes both reports]
> ```

### No Agent-to-Agent Communication

[**Agent-Communication-Restriction**:: Subagents cannot directly invoke other subagents or communicate agent-to-agent; all coordination flows through the main agent as the central orchestrator, preventing infinite agent nesting and ensuring deterministic, traceable execution paths.]^verified-stable

> [!warning] Why No Agent-to-Agent Communication?
> **Problem**: If agents could spawn other agents recursively, you'd encounter:
> - **Infinite loops**: Agent A calls Agent B calls Agent A...
> - **Context explosion**: Each level creates new context windows
> - **Cost multipliers**: Exponential token consumption
> - **Debugging nightmares**: Non-deterministic execution trees
>
> **Solution**: All delegation goes through the main agent, creating a **star topology** instead of a mesh network.

```
❌ PROHIBITED: Mesh Network (agent-to-agent)
    
    Main Agent
    ↙    ↓    ↘
  A  →  B  →  C
  ↓  ↗  ↓  ↘  ↓
  D  →  E  →  F
    [Chaos & cycles possible]

✅ REQUIRED: Star Topology (hub-and-spoke)
    
       Main Agent
     /  |   |   \
    A   B   C   D
    
    [Deterministic, traceable]
```

> [!key-claim] Communication Through Return Values
> [**Agent-Result-Passing**:: Agents communicate indirectly by returning results to the main agent, which then incorporates that information into subsequent agent invocations or uses it to make coordination decisions; this creates an information flow mediated by the coordinator.]^verified-stable
>
> **Pattern**:
> ```
> Main Agent → Agent A (get requirements)
>   → Main Agent receives: "Feature needs authentication + role-based access"
>   → Main Agent → Agent B (design with those requirements)
>       → Main Agent receives: "Architecture uses JWT + RBAC middleware"
>       → Main Agent → Agent C (implement given architecture)
> ```

### Delegation Mechanisms

Claude Code provides three delegation mechanisms:

#### 1. Automatic Delegation (Description Matching)

[**Auto-Delegation-Mechanism**:: Claude analyzes the user's query and current context, compares it against all available agent descriptions, and automatically invokes agents whose description keywords and purpose align with the task requirements without explicit user instruction.]^verified-stable

> [!methodology-and-sources] How Auto-Delegation Works
> 1. **User query analysis**: Extract intent, domain, task type
> 2. **Agent description scan**: Compare query against all agent descriptions
> 3. **Relevance scoring**: Match keywords, trigger phrases, domain alignment
> 4. **Confidence threshold**: Only auto-invoke if match confidence is high
> 5. **Execution**: Invoke agent with query context
> 6. **Result synthesis**: Integrate agent output into response
>
> **Optimization**: Include terms like "use PROACTIVELY", "MUST BE USED", "automatically invoke when" in descriptions to boost auto-activation likelihood. This is effectively **Tool SEO** for agents.

> [!example] Auto-Delegation in Action
> **Agent definition**:
> ```yaml
> ---
> name: api-designer
> description: Use PROACTIVELY for API design tasks. REST API design specialist. Automatically invoke when designing endpoints, defining request/response schemas, or planning API architecture.
> ---
> ```
>
> **User query**: "I need to add user profile endpoints to our API"
>
> **Main Agent reasoning**: 
> - Detects "endpoints" + "API" keywords
> - Matches to api-designer description
> - Auto-invokes without user explicitly saying "use api-designer"

#### 2. Explicit Invocation (User-Directed)

[**Explicit-Invocation-Pattern**:: User directly requests a specific agent by name in their prompt, bypassing automatic matching; this gives users direct control over agent selection when they know exactly which specialist they want or when overriding automatic selection.]^verified-stable

**Syntax patterns**:
```
"Use the [agent-name] agent to [task]"
"Have [agent-name] analyze [target]"
"[agent-name]: [instruction]"
```

> [!example] When to Use Explicit Invocation
> **Scenario 1 - Override automatic selection**:
> ```
> User: "Use the security-auditor agent to review this code, 
>        not the general code-reviewer"
> ```
> Forces security-specific lens even if code-reviewer would auto-match.
>
> **Scenario 2 - Sequential orchestration**:
> ```
> User: "Use requirements-analyst to document needs, then use 
>        system-architect to design the solution, then use 
>        code-reviewer to validate the architecture"
> ```
> Explicit pipeline ensures specific order and agent selection.

#### 3. Hook-Based Invocation (Event-Driven)

[**Hook-Based-Agent-Invocation**:: Agents are automatically triggered by lifecycle events (like SubagentStop, Stop) through configured hooks that execute shell commands, enabling automated workflow chaining where completion of one agent triggers the next without main agent coordination.]^verified-stable

> [!methodology-and-sources] Hook Configuration
> Hooks are configured in `settings.json`:
> ```json
> {
>   "hooks": {
>     "SubagentStop": {
>       "command": "python .claude/scripts/queue_next_agent.py",
>       "runIn": "project"
>     },
>     "Stop": {
>       "command": "echo 'Next: Use architect-review on $(cat .queue/current-slug.txt)'",
>       "runIn": "project"
>     }
>   }
> }
> ```
>
> **Workflow**: 
> 1. Agent completes task (SubagentStop event fires)
> 2. Hook script updates queue file with next agent
> 3. Output prints to stdout: "Next: Use architect-review on 'auth-feature'"
> 4. User (or automation) invokes next agent

> [!application-context] Production Pipeline with Hooks
> **Three-stage development pipeline**:
> ```
> Stage 1: pm-spec agent
> ├─ Reads enhancement request
> ├─ Writes specification document
> ├─ Sets status: READY_FOR_ARCH
> └─ Hook prints: "Use architect-review on [feature-slug]"
> 
> Stage 2: architect-review agent  
> ├─ Validates design against platform constraints
> ├─ Produces architectural decision record (ADR)
> ├─ Sets status: READY_FOR_BUILD
> └─ Hook prints: "Use implementer-tester on [feature-slug]"
> 
> Stage 3: implementer-tester agent
> ├─ Implements code + tests
> ├─ Updates documentation
> ├─ Sets status: DONE
> └─ Hook prints: "Feature [slug] complete, ready for PR"
> ```
>
> **Queue file** (`.queue/features.md`):
> ```markdown
> ## Auth Module Overhaul
> - **Status**: READY_FOR_BUILD
> - **Assigned**: implementer-tester
> - **Last Updated**: 2026-01-06 14:32 by architect-review
> ```

---

## Multi-Agent Design Patterns

### Sequential Pipeline Pattern

[**Sequential-Pipeline-Pattern**:: A multi-stage workflow where agents execute in a fixed order, with each stage's output becoming input for the next stage; status-based handoffs ensure work only proceeds when prerequisites are complete, creating a deterministic development pipeline.]^verified-stable

> [!definition] Pipeline Stages
> The canonical three-stage pattern:
>
> **Stage 1: Requirements/Planning** (PM agent)
> - Input: User request, problem statement
> - Process: Clarifying questions, acceptance criteria definition
> - Output: Specification document, status set to READY_FOR_ARCH
> - Hand off: Architect agent triggered
>
> **Stage 2: Architecture/Design** (Architect agent)  
> - Input: Specification from PM stage
> - Process: Design review, constraint validation, ADR creation
> - Output: Architecture document, status set to READY_FOR_BUILD
> - Handoff: Implementer agent triggered
>
> **Stage 3: Implementation** (Implementer agent)
> - Input: Architecture from previous stage
> - Process: Code generation, test creation, documentation updates
> - Output: Working implementation, status set to DONE
> - Handoff: Human review or deployment pipeline

> [!example] Real-World Pipeline Implementation
> **File structure**:
> ```
> .queue/
> ├── features.md              # Master queue
> └── auth-system/
>     ├── 01-pm-spec.md        # PM agent output
>     ├── 02-architecture.md   # Architect agent output
>     └── 03-implementation/   # Implementer agent output
> ```
>
> **features.md**:
> ```markdown
> ## Feature: Auth System Upgrade
> - **Slug**: auth-system
> - **Status**: READY_FOR_BUILD
> - **Current Stage**: 02-architecture
> - **Next Action**: Use implementer-tester on 'auth-system'
> - **Assigned To**: implementer-tester
> - **Dependencies**: None
> - **Notes**: JWT tokens, OAuth2 integration, RBAC
> - **Last Updated**: 2026-01-06 14:45 by architect-review
> ```

> [!warning] Pipeline Anti-Patterns
> **❌ Skipping stages**: Don't jump from requirements directly to implementation
> - Causes architectural inconsistencies
> - Leads to rework when design flaws discovered late
>
> **❌ Parallel execution of sequential stages**: Don't run architect and implementer simultaneously
> - Creates merge conflicts
> - Implementation may not match final architecture
>
> **❌ No status tracking**: Don't rely on memory for handoffs
> - Human forgets which stage is complete
> - Multiple developers can't coordinate
>
> **✅ Solution**: Always use explicit status markers and shared state files

### Parallel Execution Pattern

[**Parallel-Execution-Pattern**:: Multiple agents work simultaneously on independent subtasks with low coupling, then return results to the main agent for synthesis; this pattern dramatically reduces total execution time for tasks with separable concerns like multi-domain research or independent module development.]^verified-stable

> [!key-claim] When Parallel Execution Shines
> [**Parallel-Execution-Use-Cases**:: Most effective for breadth-first tasks requiring exploration of multiple independent directions simultaneously, such as multi-source research, full-stack feature development with separate frontend/backend work, or comprehensive security audits with multiple specialized checks.]^verified-stable
>
> Anthropic's research system achieved **90.2% performance improvement** using parallel execution: a lead researcher agent delegated tasks to multiple Sonnet agents working simultaneously on different information sources.

> [!methodology-and-sources] Task Tool for Parallel Spawning
> The main agent uses the **Task tool** to spawn subagents in parallel within a single action:
>
> ```markdown
> Use the Task tool to spawn these subagents in parallel:
> 
> 1. **Web Documentation Agent** (subagent_type: general-purpose)
>    - Search official docs for [topic]
>    - Find best practices and patterns
>    - Locate relevant GitHub issues
> 
> 2. **Stack Overflow Agent** (subagent_type: general-purpose)  
>    - Search Stack Overflow for similar problems
>    - Find highly-voted solutions
>    - Note common pitfalls
> 
> 3. **Codebase Explorer Agent** (subagent_type: Explore)
>    - Search codebase for related patterns
>    - Find existing solutions to similar problems
>    - Identify relevant files and functions
> 
> After all agents complete, synthesize findings into report.
> ```

> [!example] Full-Stack Parallel Development
> **Scenario**: "Create a user dashboard with analytics"
>
> **Sequential approach** (slow):
> ```
> 1. backend-engineer: Build API endpoints (20 min)
> 2. frontend-specialist: Build UI components (25 min)  
> 3. database-architect: Design schema (15 min)
> Total: 60 minutes
> ```
>
> **Parallel approach** (fast):
> ```
> All three agents start simultaneously:
> 1. backend-engineer: Build API endpoints (20 min) ┐
> 2. frontend-specialist: Build UI components (25 min) ├─ Parallel
> 3. database-architect: Design schema (15 min) ┘
> 
> Main agent: Synthesize and resolve conflicts (5 min)
> Total: 30 minutes (50% time reduction)
> ```

> [!warning] Parallel Execution Pitfalls
> **⚠️ Dependency conflicts**: Agents working on interdependent components may produce incompatible interfaces
> - **Mitigation**: Main agent should define interface contracts before spawning agents
>
> **⚠️ Result coordination complexity**: Synthesizing 5+ parallel agent outputs into coherent whole
> - **Mitigation**: Structured output formats, clear success criteria
>
> **⚠️ File system conflicts**: Multiple agents modifying same files simultaneously
> - **Mitigation**: Each agent works in separate directory, main agent merges
>
> **⚠️ Error propagation**: One agent failure doesn't automatically stop others
> - **Mitigation**: Main agent monitors all parallel executions, implements timeout handling

> [!application-context] When NOT to Use Parallel Execution
> Avoid parallel agents for:
> - **Sequential dependencies**: Step B requires Step A's output
> - **Shared state modification**: Agents updating same database/file
> - **Resource contention**: Heavy computation tasks competing for system resources
> - **Complex synthesis**: Outputs require deep integration (parallel makes synthesis harder)
>
> Use sequential pipeline instead for these scenarios.

### Shared State Coordination

[**Shared-State-Coordination-Pattern**:: Agents communicate asynchronously through shared markdown files that serve as message boards; each agent reads current state, executes its task, then writes status updates and results, enabling coordination without direct agent-to-agent communication.]^verified-stable

> [!definition] The MULTI_AGENT_PLAN.md Pattern
> A structured markdown file acting as the coordination hub:
>
> ```markdown
> # Multi-Agent Development Plan
> 
> ## Task: Implement User Authentication
> - **Assigned To**: builder
> - **Status**: In Progress  
> - **Dependencies**: None
> - **Notes**: Using JWT tokens, coordinate with validator for test cases
> - **Last Updated**: 2026-01-06 14:32 by architect
> 
> ## Task: Write Integration Tests
> - **Assigned To**: validator
> - **Status**: Pending
> - **Dependencies**: Waiting for builder to complete auth module
> - **Notes**: Need to verify token expiration, refresh flow
> - **Last Updated**: 2026-01-06 14:35 by validator
> 
> ## Task: Security Audit
> - **Assigned To**: security-auditor
> - **Status**: Blocked
> - **Dependencies**: Integration tests must pass
> - **Notes**: Check for injection vulnerabilities, rate limiting
> - **Last Updated**: 2026-01-06 14:30 by project-manager
> 
> ---
> 
> ## Messages Between Agents
> 
> ### Architect → Builder (14:32)
> The authentication flow should follow this pattern:
> 1. User submits credentials
> 2. Server validates against database
> 3. Generate JWT with user roles
> 4. Return token + refresh token
> 
> **Important**: Include rate limiting on login endpoint (max 5 attempts/minute)
> 
> ### Builder → Validator (14:40)
> Auth module completed. Key endpoints:
> - POST /auth/login
> - POST /auth/refresh
> - POST /auth/logout
> 
> Test focus: Token expiration (15 min), refresh mechanism, logout invalidation
> ```

> [!methodology-and-sources] Agent Workflow with Shared State
> **Read → Execute → Write protocol**:
>
> 1. **Read phase**: Agent opens MULTI_AGENT_PLAN.md
>    - Check task status
>    - Read dependencies
>    - Review messages from other agents
>
> 2. **Execute phase**: Agent performs its specialized work
>    - Independent of other agents
>    - Can take minutes to hours
>    - Context isolated to this agent
>
> 3. **Write phase**: Agent updates shared state
>    - Set task status (In Progress → Complete)
>    - Write results/notes
>    - Leave messages for dependent agents
>    - Update timestamp
>
> 4. **Trigger next agent**: Hook or main agent reads status change, invokes next agent

> [!example] Multiple VSCode Terminals Pattern
> **Simple but powerful**: Run separate Claude Code instances in multiple terminals:
>
> ```
> Terminal 1 (architect):
> $ cd /project
> $ claude
> > I'm the architect agent. I'll read MULTI_AGENT_PLAN.md,
>   design the solution, then update my task status.
> 
> Terminal 2 (builder):  
> $ cd /project
> $ claude
> > I'm the builder agent. Waiting for architect to set
>   status READY_FOR_BUILD, then I'll implement.
> 
> Terminal 3 (validator):
> $ cd /project
> $ claude  
> > I'm the validator agent. Monitoring for status READY_FOR_TEST,
>   then I'll run integration tests.
> ```
>
> **Coordination**: Agents coordinate through the shared markdown file, no complex frameworks needed.

> [!key-claim] Simplicity Over Complexity
> [**Coordination-Simplicity-Principle**:: Markdown files as coordination mechanism outperform complex orchestration frameworks for most use cases because they're human-readable, version-controllable, easily debuggable, and don't require additional infrastructure; the simplest solution that works is often the best solution.]^verified-stable

### Hook-Based Automation

[**Hook-Based-Automation-Pattern**:: Lifecycle events (SubagentStop, Stop, ToolStart, ToolStop) trigger shell scripts that can modify shared state, queue next tasks, send notifications, or perform automated actions, enabling fully autonomous multi-agent workflows with minimal human intervention.]^verified-stable

> [!methodology-and-sources] Hook Configuration Architecture
> Hooks are defined in `settings.json` at user or project scope:
>
> ```json
> {
>   "hooks": {
>     "SubagentStop": {
>       "command": "python .claude/scripts/handle_agent_completion.py",
>       "runIn": "project",
>       "env": {
>         "QUEUE_FILE": ".queue/features.md"
>       }
>     },
>     "Stop": {
>       "command": "bash .claude/scripts/print_next_action.sh",
>       "runIn": "project"  
>     },
>     "ToolStart": {
>       "command": "echo 'Tool started: ${TOOL_NAME}'",
>       "runIn": "user"
>     }
>   }
> }
> ```
>
> **Hook script responsibilities**:
> - Read current agent's output/status
> - Update shared state files
> - Determine next agent in pipeline
> - Print next action to stdout (appears in Claude conversation)
> - Log execution for audit trail

> [!example] Autonomous Pipeline with Hooks
> **handle_agent_completion.py**:
> ```python
> import os
> import re
> from pathlib import Path
> 
> # Read queue file
> queue_file = Path(os.getenv('QUEUE_FILE', '.queue/features.md'))
> content = queue_file.read_text()
> 
> # Parse current feature status
> match = re.search(r'## Feature: (.+?)\n.*?Status: (.+?)\n', content, re.DOTALL)
> feature_name, status = match.groups()
> 
> # Determine next agent based on status
> next_agent_map = {
>     'READY_FOR_ARCH': 'architect-review',
>     'READY_FOR_BUILD': 'implementer-tester', 
>     'READY_FOR_REVIEW': 'code-quality-reviewer',
>     'DONE': None
> }
> 
> next_agent = next_agent_map.get(status)
> 
> if next_agent:
>     # Update queue file with next action
>     updated = re.sub(
>         r'(## Feature: ' + feature_name + r'.*?Next Action:).*?(\n)',
>         f'\\1 Use {next_agent} on {feature_name}\\2',
>         content,
>         flags=re.DOTALL
>     )
>     queue_file.write_text(updated)
>     
>     # Print to stdout (appears in Claude conversation)
>     print(f"\n🎯 Next Action: Use {next_agent} on '{feature_name}'")
> else:
>     print(f"\n✅ Feature '{feature_name}' complete! Ready for PR.")
> ```

> [!warning] Hook Debugging and Safety
> **⚠️ Hook failures are silent**: If your hook script has a bug, it fails silently without blocking the main agent
> - **Mitigation**: Log all hook executions to `.claude/logs/hooks.log`
>
> **⚠️ Infinite loops possible**: Poorly designed hooks can trigger each other in cycles  
> - **Mitigation**: Include loop detection (max 3 consecutive same-agent invocations)
>
> **⚠️ State file corruption**: Concurrent hook executions might corrupt shared state
> - **Mitigation**: Use file locking or atomic writes
>
> **✅ Development workflow**:
> 1. Test hook scripts manually first: `python .claude/scripts/hook.py`
> 2. Add verbose logging to track execution
> 3. Start with read-only hooks (just print info)
> 4. Gradually add state modification after validation

### Output Style Orchestration

[**Output-Style-Orchestration-Pattern**:: Special meta-prompts that change the main agent's workflow mode and orchestration behavior; different output styles activate different agent coordination patterns, tool usage strategies, and response structures optimized for specific development phases like research, planning, or execution.]^verified-stable

> [!definition] Output Style Modes
> Three primary workflow modes in Claude Code:
>
> **Research Mode** (`/output-style research`)
> - Focus: Deep exploration and understanding
> - Agent pattern: Single agent deep dives, sequential investigation
> - Tools: Heavy use of Explore, web search, documentation fetching
> - Output: Comprehensive analysis documents
>
> **Planning Mode** (`/output-style planning`)
> - Focus: Architecture and design
> - Agent pattern: Architect-focused, may invoke research agents
> - Tools: Codebase analysis, design document generation
> - Output: Architectural decision records (ADRs), design specs
>
> **Execution Mode** (`/output-style execution`)  
> - Focus: Implementation and delivery
> - Agent pattern: Multi-agent coordination (frontend + backend + testing)
> - Tools: Full tool access for code generation and testing
> - Output: Working code, tests, documentation

> [!example] Output Style Workflow
> **Phase 1 - Research**:
> ```
> User: /output-style research
>       "Help me understand authentication patterns in Next.js applications"
> 
> Main Agent:
> ├─ Invokes documentation-researcher agent
> ├─ Deep dive into Next.js auth docs
> ├─ Analyzes Auth.js, NextAuth, Clerk patterns
> └─ Produces: Comprehensive research document
> ```
>
> **Phase 2 - Planning**:
> ```
> User: /output-style planning  
>       "Design a user authentication system with role-based access"
> 
> Main Agent:
> ├─ Invokes system-architect agent
> ├─ References research from Phase 1
> ├─ Designs JWT + RBAC architecture
> └─ Produces: ADR + technical specifications
> ```
>
> **Phase 3 - Execution**:
> ```
> User: /output-style execution
>       "Implement the authentication system from the planning documents"
> 
> Main Agent:
> ├─ Analyzes: Complex multi-component task
> ├─ Spawns in parallel:
> │  ├─ backend-database-engineer: Schema + API endpoints
> │  ├─ frontend-ui-specialist: Login UI components
> │  └─ code-quality-reviewer: Validates implementation
> ├─ Synthesizes: Combines outputs, resolves conflicts
> └─ Produces: Working authentication system
> ```

> [!application-context] When to Switch Output Styles
> **Research mode**: Use when you don't fully understand the domain, technology, or requirements. Prevents premature implementation.
>
> **Planning mode**: Use when requirements are clear but implementation strategy needs design. Critical for complex features to avoid rework.
>
> **Execution mode**: Use when design is finalized and you're ready to build. Maximizes implementation speed through coordinated specialists.
>
> **Anti-pattern**: Jumping directly to execution mode without research or planning leads to:
> - Architectural inconsistencies
> - Missed requirements
> - Multiple implementation attempts (wasted time)
> - Technical debt from poor initial design

---

## Agent Engineering

### System Prompt Architecture

[**System-Prompt-Architecture-Pattern**:: A structured format for agent system prompts consisting of role definition, success criteria, workflow steps, constraints, and output format specification; this contract-style structure ensures agents understand their boundaries, responsibilities, and expected deliverables.]^verified-stable

> [!definition] Contract-Style Prompt Structure
> The optimal system prompt follows a contract format:
>
> ```markdown
> # [Agent Name] - [One-line role description]
> 
> ## Role
> You are [specific expertise/domain specialist].
> [1-2 sentences defining core responsibility]
> 
> ## When Invoked
> [Specific trigger conditions]
> [What situations require this agent]
> 
> ## Success Criteria
> This invocation succeeds when:
> - [Measurable outcome 1]
> - [Measurable outcome 2]
> - [Measurable outcome 3]
> 
> ## Workflow
> 1. [First step - be specific]
> 2. [Second step with tool usage if applicable]
> 3. [Analysis or processing step]
> 4. [Output generation step]
> 5. [Validation or review step]
> 
> ## Key Practices
> - [Best practice 1 with rationale]
> - [Best practice 2 with examples]
> - [Best practice 3 with constraints]
> 
> ## Constraints
> - [What NOT to do]
> - [Boundary conditions]
> - [Error handling requirements]
> 
> ## Output Format
> [Structured output specification]
> ```

> [!example] Production-Grade Security Auditor Agent
> ```markdown
> # Security Auditor - Application Security Specialist
> 
> ## Role
> You are an expert application security auditor specializing in web application vulnerabilities, secure coding practices, and OWASP Top 10 threat mitigation. Your primary responsibility is identifying security flaws before they reach production.
> 
> ## When Invoked
> Invoke this agent when:
> - New authentication or authorization code is written
> - API endpoints handle sensitive data
> - User input processing is implemented
> - Security-critical configuration changes occur
> - Pre-deployment security review is required
> 
> ## Success Criteria
> This audit succeeds when:
> - All OWASP Top 10 vulnerabilities are checked
> - Specific security issues are documented with severity levels
> - Remediation steps are provided with code examples
> - Risk assessment is completed (Critical/High/Medium/Low)
> 
> ## Workflow
> 1. Run `git diff` to identify changed files
> 2. Scan for common vulnerability patterns:
>    - SQL injection vectors (parameterized queries used?)
>    - XSS vulnerabilities (proper escaping/sanitization?)
>    - CSRF protection (tokens present?)
>    - Authentication flaws (weak password policies?)
>    - Authorization bypasses (proper permission checks?)
> 3. Review dependencies for known vulnerabilities:
>    - Run `npm audit` or `pip check`
>    - Check CVE databases for critical issues
> 4. Analyze configuration for security misconfigurations:
>    - Environment variables (secrets exposed?)
>    - CORS settings (too permissive?)
>    - HTTP headers (security headers missing?)
> 5. Generate structured security report
> 
> ## Key Practices
> - **Severity-first reporting**: Always list Critical and High severity issues first
> - **Actionable recommendations**: Every finding must include specific fix with code example
> - **False positive awareness**: Note when patterns are false alarms (e.g., SQL in comments)
> - **Defense in depth**: Recommend multiple layers of security, not single-point protection
> 
> ## Constraints
> - DO NOT modify code directly (read-only audit role)
> - DO NOT proceed if unable to run security scanning tools
> - DO NOT provide generic advice ("improve security") - be specific
> - DO NOT ignore warnings from automated tools - investigate all flags
> 
> ## Output Format
> ```markdown
> # Security Audit Report
> **Date**: [timestamp]
> **Files Reviewed**: [list]
> **Tool Versions**: npm audit v[X], ...
> 
> ## Critical Issues
> ### [Issue Name]
> - **Severity**: Critical
> - **Location**: [file:line]
> - **Description**: [what's vulnerable]
> - **Impact**: [attack scenario]
> - **Recommendation**: [specific fix with code]
> 
> ## High Priority Issues
> [Same structure]
> 
> ## Medium/Low Issues
> [Same structure]
> 
> ## Security Posture Summary
> - [Overall risk level]
> - [Key recommendations]
> ```
> ```

> [!key-claim] Specificity Increases Reliability
> [**Prompt-Specificity-Principle**:: Vague instructions like "be thorough" or "follow best practices" lead to inconsistent agent behavior; specific, actionable steps with concrete examples produce deterministic, reliable outputs that can be evaluated and improved iteratively.]^verified-stable
>
> **Vague (❌)**:
> ```markdown
> You are a code reviewer. Review code for quality and best practices.
> Provide helpful feedback.
> ```
>
> **Specific (✅)**:
> ```markdown
> You are a code reviewer. Execute this exact workflow:
> 1. Run `git diff --staged` to see changes
> 2. For each modified function:
>    - Check cyclomatic complexity (flag if >10)
>    - Verify all parameters have type hints (Python) or TypeScript types
>    - Ensure docstrings exist for functions >5 lines
> 3. Check for:
>    - Hardcoded credentials (search for "password", "api_key" patterns)
>    - TODO/FIXME comments in production code
>    - Console.log/print statements (should use logger)
> 4. Generate report with line-specific findings in this format:
>    [file:line] [severity] [issue] - [specific fix]
> ```

### Tool Restriction Strategies

[**Tool-Restriction-Strategy**:: Limiting agent tool access to only necessary capabilities enhances security by preventing unintended actions, improves focus by removing irrelevant options from the agent's attention, and creates specialized roles that cannot accidentally perform operations outside their domain.]^verified-stable

> [!definition] Tool Access Patterns
> **Full tool access** (omit `tools` field):
> - Agent inherits all tools from main thread
> - Use for: General-purpose agents, orchestrators, implementation agents
> - Risk: Can perform destructive operations
>
> **Read-only access** (`tools: Read, Grep, Glob`):
> - Agent can analyze but not modify
> - Use for: Code reviewers, analyzers, documentation generators
> - Safety: Cannot accidentally break anything
>
> **Restricted write** (`tools: Read, Write(src/**), Bash(npm test)`):
> - Agent can modify specific directories, run specific commands
> - Use for: Feature developers limited to their module
> - Balance: Productive but constrained
>
> **No file access** (`tools: Bash(echo *)`):
> - Agent can only run whitelisted commands
> - Use for: Specialized utilities, formatters
> - Maximum safety: Isolated execution

> [!example] Tool Restriction by Agent Type
> **Documentation Writer** (read + limited write):
> ```yaml
> tools: Read, Write(docs/**), Write(README.md), Glob
> ```
> Can read entire codebase for understanding, but only write to documentation directories.
>
> **Security Auditor** (read-only + scanning):
> ```yaml
> tools: Read, Grep, Glob, Bash(npm audit), Bash(pip check)
> ```
> Can analyze everything, run security scanners, but cannot modify code or configuration.
>
> **Test Generator** (read + test write + test execution):
> ```yaml  
> tools: Read, Write(tests/**), Bash(npm test), Bash(pytest)
> ```
> Can read source code, write test files, run tests, but cannot modify source code.
>
> **Frontend Developer** (scoped read/write):
> ```yaml
> tools: Read, Write(src/components/**), Write(src/styles/**), Bash(npm run dev)
> ```
> Limited to frontend directories, cannot touch backend or infrastructure.

> [!warning] Permission Sprawl Anti-Pattern
> **❌ Problem**: Granting broad tool access because "the agent might need it someday"
>
> **Consequences**:
> - Accidental destructive operations (agent deletes wrong files)
> - Security risks (agent can modify sensitive configs)
> - Difficult to audit (what did the agent change?)
>
> **✅ Solution**: Start with minimal tools, expand only when specific need arises
>
> ```yaml
> # Start here (minimal)
> tools: Read, Grep
> 
> # Add write only when needed
> tools: Read, Grep, Write(specific-dir/**)
> 
> # Add bash only for specific commands
> tools: Read, Grep, Write(specific-dir/**), Bash(npm test)
> ```

> [!application-context] Tool Permissions as Documentation
> Tool restrictions serve as **implicit documentation** of agent responsibilities:
>
> ```yaml
> # This agent's tools tell you its role without reading the prompt
> name: database-migration-specialist
> tools: Read(migrations/**), Write(migrations/**), Bash(alembic), Bash(psql)
> ```
>
> You can immediately understand: This agent works exclusively with database migrations, can read/write migration files, and can run database tooling. It cannot touch application code or infrastructure.

### Model Selection Economics

[**Model-Selection-Economics**:: Strategic choice of which Claude model to use for each agent based on task complexity, cost sensitivity, and performance requirements; with Haiku 4.5 achieving 90% of Sonnet 4.5's agentic performance at 3x cost savings, agents should be optimized for cost efficiency without sacrificing quality.]^verified-stable

> [!key-claim] Haiku 4.5 Revolution
> [**Haiku-4.5-Performance**:: Claude Haiku 4.5 (released October 2025) delivers 90% of Sonnet 4.5's agentic coding performance at 2x the speed and 3x cost savings ($1/$5 vs $3/$15 per million tokens), making it the optimal choice for most agent tasks and dramatically extending usage limits for subscription users.]^verified-stable
>
> **Cost comparison** (API pricing):
> - Haiku 4.5: $1 input / $5 output per million tokens
> - Sonnet 4.5: $3 input / $15 output per million tokens  
> - Opus 4: $15 input / $75 output per million tokens
>
> **For Pro subscribers**: Using Haiku agents means 3x more agent invocations within monthly limits (100 Sonnet calls = 300 Haiku calls approximately).

> [!definition] Model Selection Decision Tree
> ```
> Is this task complex reasoning or novel problem-solving?
> ├─ YES → Use Opus 4 (deepest reasoning)
> └─ NO → Is routine/repetitive work with clear patterns?
>     ├─ YES → Use Haiku 4.5 (3x cost savings, 2x speed)
>     └─ NO → Use Sonnet 4.5 (balanced default)
> 
> Special cases:
> - Orchestrator/coordinator: Sonnet 4.5 (needs maximum context understanding)
> - Quality validation: Opus 4 (critical quality gate)
> - Worker agents: Haiku 4.5 (volume tasks)
> ```

> [!example] Optimized Agent Fleet
> **Coordinator** (Sonnet 4.5):
> ```yaml
> name: project-orchestrator
> model: sonnet
> # Needs: Complex task analysis, delegation decisions, synthesis
> ```
>
> **Worker Agents** (Haiku 4.5):
> ```yaml
> name: test-generator
> model: haiku
> # Clear patterns: input → test cases → output
> 
> name: documentation-writer  
> model: haiku
> # Routine work: code → docstrings, well-defined task
> 
> name: code-formatter
> model: haiku
> # Mechanical task: code → formatted code
> ```
>
> **Quality Gates** (Opus 4):
> ```yaml
> name: architecture-reviewer
> model: opus
> # Critical decisions: design validation, long-term impact
> 
> name: security-auditor
> model: opus  
> # High stakes: security vulnerabilities must not be missed
> ```
>
> **Cost impact**: Majority of invocations use Haiku (70%), some Sonnet (25%), rare Opus (5%) = ~60-70% overall cost reduction vs. all-Sonnet fleet.

> [!methodology-and-sources] Model Selection Testing Protocol
> **How to determine optimal model for your agent**:
>
> 1. **Start with Haiku 4.5** as default
> 2. **Run 10 test invocations** on representative tasks
> 3. **Measure quality**: Does output meet success criteria?
> 4. **If quality ≥90%**: Keep Haiku (cost optimized)
> 5. **If quality 70-90%**: Test Sonnet 4.5
> 6. **If quality <70% or novel reasoning needed**: Upgrade to Opus 4
>
> **Quality regression testing**: When agents update, re-test with Haiku to see if improvements allow downgrading from Sonnet.

### Description Field Optimization

[**Description-Field-Optimization**:: Strategic crafting of the agent description to maximize automatic invocation likelihood through keyword matching, trigger phrases, and clear capability signaling; functions as "Tool SEO" where well-optimized descriptions cause agents to be selected more reliably by the main coordinator.]^verified-stable

> [!definition] Description Field Components
> An effective description contains:
>
> **1. Invocation triggers** (when to use this agent):
> ```yaml
> description: Use PROACTIVELY when designing APIs, defining endpoints, or planning REST architectures.
> ```
>
> **2. Domain keywords** (what this agent knows):
> ```yaml
> description: Expert in React, TypeScript, component architecture, hooks, and modern frontend patterns.
> ```
>
> **3. Task verbs** (what actions this agent performs):
> ```yaml
> description: Reviews code for security, analyzes vulnerabilities, audits dependencies, scans for OWASP Top 10.
> ```
>
> **4. Exclusions** (when NOT to use):
> ```yaml
> description: For backend API security only, not frontend or infrastructure security.
> ```

> [!example] Description Optimization Before/After
> **Before (❌ weak auto-activation)**:
> ```yaml
> name: api-agent
> description: Helps with API stuff
> ```
> - Too vague
> - No trigger keywords
> - No domain specificity
>
> **After (✅ strong auto-activation)**:
> ```yaml
> name: api-designer
> description: |
>   Use PROACTIVELY for REST API design tasks. Expert API architect specializing in:
>   - Endpoint design and RESTful principles
>   - Request/response schema definition (OpenAPI, JSON Schema)
>   - API versioning strategies
>   - Authentication/authorization patterns (OAuth, JWT)
>   - Rate limiting and pagination design
>   
>   Automatically invoke when:
>   - User mentions "API", "endpoint", "REST", "GraphQL"
>   - Designing backend architecture
>   - Defining service interfaces
>   - Planning microservices communication
>   
>   NOT for implementation (use backend-engineer) or frontend API consumption.
> ```

> [!key-claim] Tool SEO Trigger Phrases
> [**Tool-SEO-Triggers**:: Specific phrases that boost agent auto-activation probability include "use PROACTIVELY", "MUST BE USED", "automatically invoke when", and "triggers on"; these signal to Claude's selection mechanism that the agent should be considered aggressively for matching tasks.]^verified-stable
>
> **High-impact phrases**:
> - "Use PROACTIVELY" - Strongest signal
> - "MUST BE USED when" - Creates requirement
> - "Automatically invoke for" - Clear trigger
> - "Always call when" - Explicit mandate
>
> **Supporting phrases**:
> - "Specializing in", "Expert in" - Domain signals
> - "Handles", "Processes", "Manages" - Action verbs
> - "For [X] tasks" - Scope definition
> - "NOT for [Y]" - Boundary setting

> [!warning] Description Anti-Patterns
> **❌ Generic descriptions**:
> ```yaml
> description: General purpose assistant
> ```
> Will never auto-activate (too broad, no keywords).
>
> **❌ Implementation details in description**:
> ```yaml
> description: Runs git commands, checks files, writes code
> ```
> Describes HOW not WHEN. Put implementation in system prompt.
>
> **❌ Overlapping descriptions**:
> ```yaml
> # Agent A
> description: Code review and testing expert
> 
> # Agent B  
> description: Testing and code quality specialist
> ```
> Ambiguous overlap causes unpredictable selection.
>
> **✅ Solution**: Each agent should have clear, non-overlapping domain with distinct trigger keywords.

---

## Implementation Architecture

### File System Design

[**File-System-Agent-Architecture**:: A hierarchical directory structure where agents are defined as markdown files in `.claude/agents/` directories at user (global) and project (local) scopes, with accompanying coordination files like shared markdown state documents and custom command definitions organized in `.claude/commands/`.]^verified-stable

> [!definition] Complete Project Structure
> ```
> project-root/
> ├── .claude/
> │   ├── agents/                     # Project-specific agents
> │   │   ├── domain-expert.md       # Understands business logic
> │   │   ├── integration-tester.md  # Tests external API integrations
> │   │   └── architect.md           # System design specialist
> │   ├── commands/                   # Custom slash commands  
> │   │   ├── /review.md             # Comprehensive code review workflow
> │   │   ├── /deploy.md             # Deployment checklist execution
> │   │   └── /research.md           # Multi-agent research coordination
> │   ├── scripts/                    # Hook scripts and automation
> │   │   ├── handle_agent_completion.py
> │   │   ├── queue_next_agent.sh
> │   │   └── print_next_action.sh
> │   └── state/                      # Shared state files
> │       ├── MULTI_AGENT_PLAN.md    # Coordination hub
> │       └── features/               # Per-feature work areas
> │           ├── auth-system.md
> │           └── payment-gateway.md
> ├── CLAUDE.md                       # Project context
> ├── CLAUDE.local.md                 # Personal overrides (gitignored)
> └── .mcp.json                       # MCP server configuration
> 
> ~/.claude/                           # User-level (global)
> ├── agents/
> │   ├── code-reviewer.md            # Personal code review preferences
> │   ├── security-auditor.md         # Global security standards
> │   └── documentation-writer.md     # Consistent doc style
> ├── commands/
> │   └── /daily-standup.md           # Personal workflow automation
> └── settings.json                   # Global configuration
> ```

> [!methodology-and-sources] What to Put Where
> **Project-level** (`.claude/agents/`):
> - Domain-specific agents (e.g., "payment-processor-specialist")
> - Team-shared agents (commit to version control)
> - Project-specific workflows and standards
>
> **User-level** (`~/.claude/agents/`):
> - Personal workflow preferences  
> - Cross-project utilities (e.g., general code reviewer)
> - Individual coding style agents
>
> **Shared state** (`.claude/state/`):
> - Coordination files (MULTI_AGENT_PLAN.md)
> - Feature tracking documents
> - Agent communication logs
>
> **Scripts** (`.claude/scripts/`):
> - Hook handlers
> - Automation utilities
> - Queue management logic

> [!example] Version Control Strategy
> **Commit to Git** (team-shared):
> ```gitignore
> # .gitignore
> 
> # Commit these (team shares)
> .claude/agents/*.md
> .claude/commands/*.md
> .claude/scripts/
> CLAUDE.md
> 
> # Ignore these (personal)
> CLAUDE.local.md
> .claude/state/
> .claude/logs/
> ```
>
> **Why**: Team members all get the same specialized agents and workflows, but personal overrides and runtime state stay local.

> [!application-context] Multi-Project Agent Reuse
> **Scenario**: You work on 5 different client projects, each needs code review, but you have personal preferences.
>
> **Solution**:
> ```
> ~/.claude/agents/
> └── my-code-reviewer.md       # Your personal style
> 
> client-a/.claude/agents/
> └── react-specialist.md        # Client A uses React
> 
> client-b/.claude/agents/
> └── vue-specialist.md          # Client B uses Vue
> ```
>
> When working in client-a, you get:
> - Your personal code reviewer (from global)
> - Client A's React specialist (from project)
>
> When working in client-b, you get:
> - Same personal code reviewer (from global)
> - Client B's Vue specialist (from project)

### Context Isolation Benefits

[**Context-Isolation-Architecture**:: Each subagent operates in a completely separate conversation context window from the main agent and other subagents, preventing information from one subtask polluting attention and focus for another subtask, while allowing agents to explore deeply without bloating the main conversation.]^verified-stable

> [!key-claim] The Context Pollution Problem
> [**Context-Pollution-Degradation**:: In single-agent conversations, as context window fills with diverse information (code explorations, debugging attempts, test iterations, documentation searches), the agent's ability to maintain focus on the original task degrades because attention is distributed across unrelated context elements.]^verified-stable
>
> **Example scenario**:
> ```
> Message 1: "Build a user dashboard"
> Messages 2-20: Database schema exploration
> Messages 21-40: API endpoint debugging  
> Messages 41-60: Frontend component iterations
> Messages 61-80: CSS styling attempts
> Messages 81-100: Test file generation
> 
> Message 101: "Remind me what we're building?"
> Agent: [Struggles because 100 messages of implementation
>         details have pushed original requirements out of 
>         attention focus]
> ```

> [!example] Context Isolation in Action
> **Without isolation** (single agent):
> ```
> Main conversation (100+ messages):
> ├─ User: Build dashboard
> ├─ Claude: Exploring database schema...
> ├─ Claude: Found 12 related tables...
> ├─ Claude: Analyzing relationships...
> ├─ Claude: Let me check API endpoints...
> ├─ Claude: Endpoint 1: /api/users...
> ├─ Claude: Endpoint 2: /api/analytics...
> ├─ Claude: Now for frontend components...
> ├─ Claude: Component structure: Header, Sidebar...
> ├─ Claude: Styling approach: Tailwind CSS...
> [90 more messages of similar details]
> 
> Context: Saturated with implementation minutiae
> Focus: Diluted across many unrelated details
> ```
>
> **With isolation** (multi-agent):
> ```
> Main conversation (10 messages):
> ├─ User: Build dashboard  
> ├─ Claude: I'll coordinate specialists:
> │   1. database-architect (isolated context)
> │   2. backend-api-engineer (isolated context)
> │   3. frontend-specialist (isolated context)
> ├─ Claude: Database agent designed schema
> ├─ Claude: API agent built endpoints
> ├─ Claude: Frontend agent created UI
> └─ Claude: Dashboard complete, here's the summary
> 
> Context: High-level coordination only
> Focus: Maintained on original goal
> 
> Subagent contexts (isolated):
> ├─ database-architect: 30 messages deep on schema design
> ├─ backend-api-engineer: 40 messages on endpoint implementation
> └─ frontend-specialist: 35 messages on UI components
> 
> None of this pollutes main conversation!
> ```

> [!key-claim] Parallelization Without Context Conflicts
> [**Parallel-Context-Independence**:: Because each subagent has an isolated context window, multiple agents can work simultaneously on different aspects of a task without context conflicts or attention competition; one agent's detailed exploration doesn't interfere with another agent's focus.]^verified-stable
>
> **Sequential (shared context)**:
> ```
> Time 0-20min: Agent explores database (context fills with DB details)
> Time 20-45min: Agent builds API (context now has DB + API details)
> Time 45-70min: Agent creates UI (context saturated with all details)
> 
> Total: 70 minutes, context pollution accumulates
> ```
>
> **Parallel (isolated contexts)**:
> ```
> Time 0-20min: All three agents work simultaneously:
>   ├─ DB agent: Deep schema exploration (isolated)
>   ├─ API agent: Endpoint implementation (isolated)
>   └─ UI agent: Component development (isolated)
> 
> Time 20-25min: Main agent synthesizes all results
> 
> Total: 25 minutes, no context pollution
> ```

> [!warning] When Context Isolation Hurts
> **⚠️ Tight coupling**: If agents need continuous back-and-forth, isolation creates communication overhead
>
> **Example**: Frontend and backend need to iterate on API contract
> - **Without isolation**: Direct iteration in same context
> - **With isolation**: Must pass through main agent for each iteration
>
> **Solution**: Keep tightly coupled work in single agent, use isolation for loosely coupled tasks.

### Real-World Agent Examples

> [!example] Production Agent Library
> **1. Requirements Analyst**
> ```yaml
> ---
> name: requirements-analyst  
> description: Use PROACTIVELY at project start or when requirements are unclear. Specializes in requirements gathering, user story creation, and acceptance criteria definition.
> tools: Read, Write(docs/requirements/**), Grep
> model: sonnet
> ---
> 
> You are a product requirements analyst who transforms vague ideas into clear, actionable specifications.
> 
> When invoked:
> 1. Ask clarifying questions about:
>    - User personas and use cases
>    - Success metrics and KPIs
>    - Technical constraints and dependencies
>    - Integration requirements
> 2. Document responses in structured format:
>    - User stories (As a [user], I want [goal], so that [benefit])
>    - Acceptance criteria (Given/When/Then format)
>    - Non-functional requirements (performance, security, scalability)
> 3. Set status to READY_FOR_ARCH when complete
> 4. Save to docs/requirements/[feature-slug].md
> 
> Output format:
> # Requirements: [Feature Name]
> ## User Stories
> ## Acceptance Criteria  
> ## Technical Constraints
> ## Dependencies
> ## Success Metrics
> ```
>
> **2. System Architect**
> ```yaml
> ---
> name: system-architect
> description: Use after requirements are complete. Expert in system design, architecture patterns, and technical decision-making. Creates ADRs and validates designs against constraints.
> tools: Read, Write(docs/architecture/**), Grep, Bash(npm list)
> model: opus
> ---
> 
> You are a senior systems architect responsible for high-level design decisions.
> 
> When invoked:
> 1. Read requirements document from docs/requirements/
> 2. Analyze existing architecture (CLAUDE.md, docs/architecture/)
> 3. Design solution considering:
>    - Existing patterns and conventions
>    - Scalability and performance requirements
>    - Security and compliance needs
>    - Technical debt implications
> 4. Create Architectural Decision Record (ADR):
>    - Context: What's the situation?
>    - Decision: What's being decided?
>    - Consequences: What are the impacts?
>    - Alternatives: What else was considered?
> 5. Validate against platform constraints (check CLAUDE.md)
> 6. Set status to READY_FOR_BUILD
> 7. Save to docs/architecture/ADR-[NNNN]-[feature-slug].md
> 
> Key principles:
> - Consistency over novelty (follow existing patterns)
> - Simplicity over cleverness (prefer boring solutions)
> - Explicit over implicit (document decisions)
> ```
>
> **3. Backend Engineer**
> ```yaml
> ---
> name: backend-engineer
> description: Implements server-side features, API endpoints, database operations. Use when building backend functionality, creating services, or implementing business logic.
> tools: Read, Write(src/backend/**), Write(tests/**), Bash(npm test), Bash(npm run migrate)
> model: haiku
> ---
> 
> You are a backend engineer implementing server-side features.
> 
> When invoked:
> 1. Read architecture document
> 2. Implement based on design:
>    - Create/modify API routes
>    - Implement business logic in services layer
>    - Add database queries/migrations
>    - Write integration tests
> 3. Follow project conventions (check CLAUDE.md)
> 4. Run tests to verify: npm test
> 5. Document API endpoints in OpenAPI format
> 6. Update status: IMPLEMENTED
> 
> Standards:
> - Type safety: Use TypeScript strict mode
> - Error handling: Try-catch with proper error types
> - Validation: Use Zod/Joi for input validation
> - Testing: Write tests before implementation (TDD)
> ```

> [!example] Coordination Workflow with Real Agents
> **End-to-end feature development**:
>
> ```
> Step 1: User initiates
> User: "We need a payment processing feature"
> 
> Step 2: Requirements phase
> Main Agent → requirements-analyst agent
> └─ Agent asks clarifying questions
>     └─ Outputs: docs/requirements/payment-processing.md
>         └─ Status: READY_FOR_ARCH
> 
> Step 3: Architecture phase  
> Main Agent → system-architect agent
> └─ Agent reviews requirements
>     └─ Outputs: docs/architecture/ADR-0042-payment-processing.md
>         └─ Status: READY_FOR_BUILD
> 
> Step 4: Implementation phase (parallel)
> Main Agent → Spawns in parallel:
> ├─ backend-engineer agent
> │   └─ Implements: Payment service, Stripe integration
> ├─ frontend-engineer agent
> │   └─ Implements: Payment UI, form validation
> └─ database-engineer agent
>     └─ Implements: Payment transactions table, migrations
> 
> Step 5: Quality assurance
> Main Agent → code-quality-reviewer agent
> └─ Agent validates all implementations
>     └─ Status: READY_FOR_REVIEW
> 
> Step 6: Security audit
> Main Agent → security-auditor agent  
> └─ Agent checks for vulnerabilities
>     └─ Status: DONE (if no critical issues)
> 
> Result: Production-ready payment processing feature
> Time: ~30-40 minutes (vs. 2-3 hours single agent)
> ```

---

## Coordination Strategies

### Task Analysis and Routing

[**Task-Analysis-Routing-Strategy**:: The main agent's process of decomposing user requests into subtasks, matching subtasks to specialized agents based on capability descriptions and domain keywords, determining execution order (sequential vs. parallel), and delegating work with appropriate context to each agent.]^verified-stable

> [!definition] Routing Decision Factors
> The main agent considers:
>
> **1. Task complexity**:
> - Simple (single agent)
> - Moderate (2-3 agents sequentially)  
> - Complex (5+ agents, potentially parallel)
>
> **2. Domain matching**:
> - Keywords in user query vs. agent descriptions
> - Trigger phrase alignment
> - Explicit user requests ("use X agent")
>
> **3. Dependency analysis**:
> - Sequential: B depends on A's output
> - Parallel: A and B are independent
> - Conditional: C only needed if A finds issues
>
> **4. Resource constraints**:
> - Token budget (prefer Haiku agents for volume)
> - Time sensitivity (prefer parallel for speed)
> - Quality requirements (prefer Opus for critical tasks)

> [!example] Task Decomposition Example
> **User request**: "Refactor the authentication module for better security"
>
> **Main agent analysis**:
> ```
> Task: Authentication refactoring + security improvement
> 
> Decomposition:
> ├─ Subtask 1: Security audit (identify vulnerabilities)
> │  └─ Agent: security-auditor (read-only, Opus for thorough review)
> │  └─ Reason: Must happen first to know what to fix
> │
> ├─ Subtask 2: Code refactoring (implement fixes)
> │  └─ Agent: backend-engineer (write access, Haiku for routine refactoring)
> │  └─ Reason: Depends on security audit findings
> │
> ├─ Subtask 3: Test generation (ensure no regressions)
> │  └─ Agent: test-engineer (write tests/**, Haiku for clear patterns)
> │  └─ Reason: Can happen parallel to refactoring (independent files)
> │
> └─ Subtask 4: Final review (validate improvements)
>    └─ Agent: code-quality-reviewer (read-only, Sonnet for synthesis)
>    └─ Reason: After implementation complete
> 
> Execution plan:
> 1. security-auditor (sequential, required first)
> 2. backend-engineer + test-engineer (parallel, independent)
> 3. code-quality-reviewer (sequential, requires 2 complete)
> ```

> [!methodology-and-sources] Routing Algorithm
> Simplified pseudocode for main agent routing logic:
>
> ```python
> def route_task(user_query):
>     # 1. Parse user query
>     intent = extract_intent(user_query)
>     keywords = extract_keywords(user_query)
>     explicit_agent = check_explicit_invocation(user_query)
>     
>     if explicit_agent:
>         return [explicit_agent]  # User specified agent
>     
>     # 2. Score all agents against query
>     agent_scores = []
>     for agent in available_agents:
>         score = match_score(
>             agent.description,
>             keywords,
>             intent
>         )
>         agent_scores.append((agent, score))
>     
>     # 3. Select best matches above threshold
>     candidates = [
>         agent for agent, score in agent_scores
>         if score > CONFIDENCE_THRESHOLD
>     ]
>     
>     # 4. Determine execution strategy
>     if len(candidates) == 1:
>         return sequential([candidates[0]])
>     
>     dependencies = analyze_dependencies(candidates)
>     if has_dependencies(dependencies):
>         return sequential(order_by_dependencies(candidates))
>     else:
>         return parallel(candidates)
> ```

> [!key-claim] Adaptive Routing
> [**Adaptive-Routing-Behavior**:: The main agent learns from context and conversation history which agents are most effective for different task types; this creates implicit routing optimization where successful agent selections become more likely to be repeated for similar future tasks within the same conversation.]^verified-stable
>
> **Example**:
> ```
> Message 1: "Review this code for security"
> Main Agent → security-auditor (finds vulnerabilities)
> 
> Message 10: "Review that other module too"
> Main Agent → security-auditor (remembers previous success)
> 
> Message 20: "And the API endpoints?"  
> Main Agent → security-auditor (pattern reinforced)
> ```
>
> The conversation context teaches the main agent that "review" in this project context means "security review", not general code review.

### State Management Across Agents

[**State-Management-Pattern**:: Coordinating agent execution and maintaining consistency across multiple agents requires explicit state tracking through shared files, clear status markers, and defined handoff protocols; agents update state atomically to prevent conflicts and communicate asynchronously through state changes rather than direct messaging.]^verified-stable

> [!definition] State Management Approaches
> **1. Shared Markdown Files** (simplest):
> - Single truth source: MULTI_AGENT_PLAN.md
> - Agents read → execute → write updates
> - Human-readable state (can inspect/debug)
> - Version controlled (git tracks state changes)
>
> **2. JSON State Files** (structured):
> - .claude/state/features.json
> - Machine-readable for automation
> - Schema validation possible
> - Harder for humans to edit
>
> **3. File System State** (implicit):
> - Presence of files indicates status
> - docs/requirements/X.md exists → requirements complete
> - docs/architecture/ADR-X.md exists → design complete
> - src/features/X/ exists → implementation started
>
> **4. Git Branches** (advanced):
> - Each agent works in separate branch
> - Main agent merges when complete
> - Conflicts resolved explicitly
> - Full audit trail

> [!example] Markdown State Protocol
> **MULTI_AGENT_PLAN.md**:
> ```markdown
> # Project: User Dashboard
> **Created**: 2026-01-06  
> **Last Updated**: 2026-01-06 15:45
> 
> ## Active Features
> 
> ### Feature: Analytics Widget
> - **Slug**: analytics-widget
> - **Status**: IN_PROGRESS
> - **Assigned To**: frontend-specialist
> - **Started**: 2026-01-06 15:30
> - **Progress**: 60%
> - **Blockers**: None
> - **Next Check**: 2026-01-06 16:00
> 
> ### Feature: Export Functionality  
> - **Slug**: export-csv
> - **Status**: READY_FOR_BUILD
> - **Assigned To**: backend-engineer
> - **Dependencies**: analytics-widget (data schema)
> - **Waiting Since**: 2026-01-06 15:45
> - **Expected Start**: 2026-01-06 16:00
> 
> ## Completed Features
> 
> ### Feature: User Authentication
> - **Completed**: 2026-01-06 14:20
> - **Implemented By**: backend-engineer
> - **Reviewed By**: security-auditor
> - **Tests**: ✅ All passing
> - **Deployed**: ✅ Production
> 
> ---
> 
> ## Status Definitions
> - **PLANNING**: Requirements being gathered
> - **READY_FOR_ARCH**: Ready for architecture review
> - **READY_FOR_BUILD**: Design approved, ready for implementation
> - **IN_PROGRESS**: Active implementation
> - **READY_FOR_REVIEW**: Implementation complete, needs review
> - **BLOCKED**: Waiting on dependency or decision
> - **DONE**: Complete and verified
> 
> ---
> 
> ## Agent Communication Log
> 
> **2026-01-06 15:45 - frontend-specialist → backend-engineer**:
> Analytics widget needs these API endpoints:
> - GET /api/analytics/summary?range={7d,30d,90d}
> - GET /api/analytics/metrics?metric={users,sessions,conversions}
> 
> Response format:
> ```json
> {
>   "data": [...],
>   "meta": { "range": "7d", "total": 1234 }
> }
> ```
> 
> **2026-01-06 15:50 - backend-engineer → frontend-specialist**:
> Acknowledged. Will prioritize these endpoints after export-csv is unblocked.
> ETA: 2026-01-06 16:30
> ```

> [!methodology-and-sources] State Update Protocol
> **Atomic state updates**:
>
> ```python
> # Agent state update script
> import fcntl  # File locking for atomic operations
> from pathlib import Path
> 
> def update_agent_status(feature_slug, new_status, agent_name, notes):
>     state_file = Path('.claude/state/MULTI_AGENT_PLAN.md')
>     
>     # 1. Acquire lock (prevents concurrent writes)
>     with open(state_file, 'r+') as f:
>         fcntl.flock(f.fileno(), fcntl.LOCK_EX)
>         
>         # 2. Read current state
>         content = f.read()
>         
>         # 3. Update status for this feature
>         updated = update_feature_status(
>             content,
>             feature_slug,
>             new_status,
>             agent_name,
>             notes
>         )
>         
>         # 4. Write back atomically
>         f.seek(0)
>         f.write(updated)
>         f.truncate()
>         
>         # 5. Release lock automatically on context exit
>     
>     # 6. Log the update
>     log_state_change(feature_slug, new_status, agent_name)
> ```

> [!warning] State Synchronization Issues
> **⚠️ Race conditions**: Multiple agents updating state simultaneously
> - **Symptom**: Status updates get lost or overwritten
> - **Solution**: File locking or sequential agent execution
>
> **⚠️ Stale reads**: Agent reads old state before it's updated
> - **Symptom**: Agent makes decisions based on outdated information
> - **Solution**: Always re-read state immediately before making decisions
>
> **⚠️ Status ambiguity**: Unclear what status means
> - **Symptom**: Agents interpret status differently
> - **Solution**: Explicit status definitions documented in state file
>
> **⚠️ No rollback mechanism**: Agent updates state but fails
> - **Symptom**: State shows "complete" but work failed
> - **Solution**: Two-phase commit (tentative → confirmed) or error status

### Error Handling and Rollback

[**Error-Handling-Rollback-Strategy**:: Multi-agent systems require explicit error detection, isolation, and recovery mechanisms because agent failures can cascade; strategies include pre-flight validation, checkpointing state before destructive operations, automatic retry with exponential backoff, and graceful degradation when agents fail.]^verified-stable

> [!definition] Error Categories in Multi-Agent Systems
> **1. Agent invocation errors**:
> - Agent not found (typo in name)
> - Agent unavailable (resource limits)
> - Tool permission denied
>
> **2. Agent execution errors**:
> - Agent reaches token limit mid-task
> - Tool execution fails (file not found, command error)
> - Agent produces invalid output format
>
> **3. Coordination errors**:
> - Circular dependencies between agents
> - Conflicting state updates
> - Deadlock (agents waiting on each other)
>
> **4. Quality errors**:
> - Agent completes but output doesn't meet criteria
> - Security agent finds critical vulnerabilities
> - Test agent reports failures

> [!example] Error Handling Workflow
> **Scenario**: Backend engineer agent fails during database migration
>
> ```yaml
> # backend-engineer agent system prompt includes:
> 
> ## Error Handling Protocol
> 
> If you encounter an error:
> 1. **Classify severity**:
>    - Critical: Data loss risk, security vulnerability
>    - High: Feature broken, tests failing
>    - Medium: Partial functionality, warnings
>    - Low: Style issues, minor inconsistencies
> 
> 2. **For Critical/High errors**:
>    - STOP immediately
>    - Document error in state file with severity
>    - Set status: BLOCKED
>    - DO NOT proceed or attempt fixes blindly
>    - Example:
>      ```markdown
>      Status: BLOCKED
>      Error: Database migration failed - constraint violation
>      Severity: Critical
>      Details: Column 'user_id' has null values but NOT NULL constraint added
>      Rollback: Migration rolled back automatically
>      Required action: Manual data cleanup or migration modification needed
>      ```
> 
> 3. **For Medium errors**:
>    - Attempt automatic fix (1 retry)
>    - If retry fails, document and set status: NEEDS_REVIEW
>    - Continue with non-dependent tasks
> 
> 4. **For Low errors**:
>    - Fix automatically
>    - Note in completion message
>    - Do not block progress
> ```

> [!methodology-and-sources] Checkpoint and Rollback Pattern
> **Pre-flight checks**:
> ```markdown
> # In agent system prompt
> 
> Before any destructive operation:
> 1. Run pre-flight validations:
>    - Check all dependencies exist
>    - Verify tool permissions granted
>    - Confirm target files/dirs accessible
>    - Test commands with --dry-run if available
> 
> 2. Create checkpoint:
>    - Git: Create branch or stash changes
>    - Files: Copy to .claude/backup/[agent-name]/[timestamp]/
>    - State: Save current state to .claude/state/checkpoints/
> 
> 3. Execute operation with monitoring:
>    - Track progress in state file
>    - Log each significant action
>    - Capture all command outputs
> 
> 4. On error:
>    - Attempt automatic rollback:
>      ```bash
>      git reset --hard [checkpoint]
>      # or
>      cp -r .claude/backup/[checkpoint]/* .
>      ```
>    - Set status: ROLLED_BACK
>    - Document error for human review
> ```

> [!example] Automatic Retry Logic
> **Hook script with exponential backoff**:
> ```python
> # .claude/scripts/retry_failed_agent.py
> import time
> import subprocess
> 
> MAX_RETRIES = 3
> BASE_DELAY = 5  # seconds
> 
> def retry_agent_with_backoff(agent_name, task):
>     for attempt in range(MAX_RETRIES):
>         try:
>             result = invoke_agent(agent_name, task)
>             if result.success:
>                 return result
>             
>             # Failed but not critical - retry
>             if result.error_severity in ['medium', 'low']:
>                 delay = BASE_DELAY * (2 ** attempt)  # Exponential backoff
>                 print(f"Agent {agent_name} failed (attempt {attempt+1}/{MAX_RETRIES})")
>                 print(f"Retrying in {delay} seconds...")
>                 time.sleep(delay)
>             else:
>                 # Critical error - don't retry
>                 print(f"Critical error in {agent_name}, no retry")
>                 return result
>                 
>         except Exception as e:
>             print(f"Exception in {agent_name}: {e}")
>             if attempt == MAX_RETRIES - 1:
>                 return FailureResult(error=e)
>     
>     return FailureResult(error="Max retries exceeded")
> ```

> [!warning] Cascading Failures
> **Problem**: One agent failure causes chain reaction
>
> ```
> Agent A fails → outputs invalid data
>   → Agent B processes invalid data → produces bad output
>      → Agent C uses bad output → makes wrong decisions
>         → Entire pipeline corrupted
> ```
>
> **Solution**: Validate outputs at each stage
> ```yaml
> # In each agent system prompt
> 
> ## Output Validation
> Before setting status to COMPLETE:
> 1. Validate your output meets success criteria:
>    - Required fields present
>    - Data types correct
>    - Constraints satisfied
>    - Tests pass (if applicable)
> 
> 2. If validation fails:
>    - DO NOT mark complete
>    - Set status: VALIDATION_FAILED
>    - Document what failed
>    - Do not pass bad data to next agent
> 
> 3. Only after validation succeeds:
>    - Set status: COMPLETE
>    - Write output to expected location
>    - Update state for next agent
> ```

> [!application-context] Human-in-the-Loop for Critical Decisions
> Some errors should **always** involve humans:
>
> **Automatic handling (no human needed)**:
> - Formatting errors (auto-fix with linters)
> - Test failures in feature branches (re-run or debug)
> - Resource temporarily unavailable (retry)
>
> **Human review required**:
> - Security vulnerabilities found (assess severity, plan fixes)
> - Database migration failures (risk of data loss)
> - Conflicting agent outputs (need human judgment)
> - Architecture decisions (long-term impact)
>
> **Hook implementation**:
> ```bash
> # .claude/scripts/notify_human.sh
> 
> SEVERITY=$1
> MESSAGE=$2
> 
> if [ "$SEVERITY" == "critical" ]; then
>     # Block further execution
>     echo "❌ CRITICAL ERROR - Human review required"
>     echo "$MESSAGE"
>     echo "To continue, resolve issue and run:"
>     echo "  ./claude continue-from-checkpoint"
>     exit 1
> fi
> ```

---

## Production Patterns

### Development Workflow Integration

[**Development-Workflow-Integration-Pattern**:: Embedding multi-agent systems into standard development workflows (feature branches, PR reviews, CI/CD) by mapping agent activities to git operations, configuring agents as pre-commit hooks or CI steps, and structuring agent outputs to align with team processes like code reviews and deployment gates.]^verified-stable

> [!definition] Git-Based Workflow
> **Branch-per-agent pattern**:
> ```
> main
> ├── feature/payment-system
> │   ├── feature/payment-system-requirements (requirements-analyst)
> │   ├── feature/payment-system-architecture (system-architect)
> │   └── feature/payment-system-implementation (backend-engineer)
> ```
>
> Each agent works in its own branch, main agent merges when complete.

> [!example] Agent-Driven Feature Development
> **Step 1: Feature initialization**
> ```bash
> # User starts feature
> $ git checkout -b feature/user-notifications
> $ claude
> > "Build a user notification system"
> ```
>
> **Step 2: Agent pipeline executes**
> ```
> Main Agent orchestrates:
> 
> 1. requirements-analyst agent
>    └─ Creates: docs/requirements/notifications.md
>    └─ Creates: docs/user-stories/notifications.md
>    └─ Commits: "docs: Add notification requirements"
> 
> 2. system-architect agent
>    └─ Creates: docs/architecture/ADR-0123-notifications.md
>    └─ Commits: "docs: Add notification architecture ADR"
> 
> 3. backend-engineer + frontend-engineer (parallel)
>    ├─ backend-engineer:
>    │  └─ Creates: src/services/notifications/
>    │  └─ Creates: tests/services/notifications/
>    │  └─ Commits: "feat: Implement notification service"
>    │
>    └─ frontend-engineer:
>       └─ Creates: src/components/Notifications/
>       └─ Creates: tests/components/Notifications/
>       └─ Commits: "feat: Implement notification UI components"
> 
> 4. code-quality-reviewer agent
>    └─ Reviews: All changes
>    └─ Creates: docs/reviews/notifications-review.md
>    └─ Commits: "docs: Code review for notifications"
> 
> 5. test-engineer agent
>    └─ Creates: tests/e2e/notifications.spec.ts
>    └─ Commits: "test: Add e2e tests for notifications"
> ```
>
> **Step 3: Human review**
> ```bash
> $ git log --oneline
> a1b2c3d test: Add e2e tests for notifications
> d4e5f6g docs: Code review for notifications
> h7i8j9k feat: Implement notification UI components
> l0m1n2o feat: Implement notification service
> p3q4r5s docs: Add notification architecture ADR
> t6u7v8w docs: Add notification requirements
> 
> $ git push origin feature/user-notifications
> # Create PR for human review
> ```

> [!methodology-and-sources] Pre-Commit Hook Integration
> **Configure agents as git hooks**:
>
> `.git/hooks/pre-commit`:
> ```bash
> #!/bin/bash
> 
> # Run code-quality-reviewer before allowing commit
> echo "Running automated code review..."
> 
> # Get staged files
> STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM)
> 
> if [ -z "$STAGED_FILES" ]; then
>     exit 0
> fi
> 
> # Invoke agent for review
> claude << EOF
> Use the code-quality-reviewer agent to review these staged files:
> $STAGED_FILES
> 
> Check for:
> - Style violations
> - Potential bugs
> - Security issues
> - Missing tests
> 
> If critical issues found, exit with error to block commit.
> EOF
> 
> REVIEW_RESULT=$?
> 
> if [ $REVIEW_RESULT -ne 0 ]; then
>     echo "❌ Code review found critical issues. Fix before committing."
>     exit 1
> fi
> 
> echo "✅ Code review passed"
> exit 0
> ```

> [!application-context] CI/CD Pipeline Integration
> **GitHub Actions workflow with agents**:
>
> `.github/workflows/agent-pipeline.yml`:
> ```yaml
> name: Agent-Driven Quality Gates
> 
> on: [pull_request]
> 
> jobs:
>   security-audit:
>     runs-on: ubuntu-latest
>     steps:
>       - uses: actions/checkout@v3
>       
>       - name: Setup Claude Code
>         run: npm install -g @anthropic-ai/claude-code
>       
>       - name: Run Security Auditor Agent
>         env:
>           ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
>         run: |
>           claude --print "Use the security-auditor agent to scan for vulnerabilities in the PR diff. Report findings in GitHub Actions format." > audit-report.md
>       
>       - name: Post Results to PR
>         uses: actions/github-script@v6
>         with:
>           script: |
>             const fs = require('fs');
>             const report = fs.readFileSync('audit-report.md', 'utf8');
>             github.rest.issues.createComment({
>               issue_number: context.issue.number,
>               owner: context.repo.owner,
>               repo: context.repo.repo,
>               body: `## 🔒 Security Audit\n\n${report}`
>             });
>   
>   test-coverage:
>     runs-on: ubuntu-latest
>     steps:
>       - uses: actions/checkout@v3
>       
>       - name: Run Test Engineer Agent
>         env:
>           ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
>         run: |
>           claude --print "Use the test-engineer agent to analyze test coverage and identify untested code paths. Generate additional tests if coverage < 80%." > coverage-report.md
> ```

### Team Collaboration Strategies

[**Team-Collaboration-Pattern**:: Sharing agent definitions, coordination templates, and workflow patterns across team members through version control while allowing individual customization; establishing team conventions for agent naming, status tracking, and handoff protocols to enable asynchronous multi-developer multi-agent coordination.]^verified-stable

> [!definition] Shared vs. Personal Agents
> **Team-shared agents** (committed to git):
> - Project-specific domain experts
> - Standard workflow automation
> - Code review standards
> - Architecture validation rules
>
> **Personal agents** (local only):
> - Individual coding style preferences
> - Personal productivity automation
> - Learning/experimentation agents
> - Developer-specific workflows

> [!example] Team Agent Library
> **Project structure for team of 5 developers**:
>
> ```
> .claude/
> ├── agents/                      # Team-shared (in git)
> │   ├── README.md               # Agent usage guide
> │   ├── backend-engineer.md     # Team standard
> │   ├── frontend-engineer.md    # Team standard
> │   ├── code-reviewer.md        # Team standard
> │   ├── security-auditor.md     # Team standard
> │   └── test-engineer.md        # Team standard
> │
> ├── templates/                   # Team-shared templates
> │   ├── agent-template.md       # Template for new agents
> │   ├── feature-workflow.md     # Standard feature development flow
> │   └── bugfix-workflow.md      # Standard bug fix flow
> │
> └── docs/
>     └── AGENT_CONVENTIONS.md    # Team conventions document
> 
> ~/.claude/agents/                # Personal (not in git)
> ├── my-code-style.md            # Personal preferences
> └── learning-assistant.md       # Personal learning aid
> ```
>
> **AGENT_CONVENTIONS.md**:
> ```markdown
> # Agent Usage Conventions
> 
> ## Naming Convention
> - Use kebab-case: `backend-engineer`, not `Backend_Engineer`
> - Descriptive names: `api-designer`, not `api`
> - Role-based: `code-reviewer`, not `reviewer-agent`
> 
> ## Status Values
> All agents must use these standard statuses:
> - `PLANNING`: Requirements gathering
> - `READY_FOR_ARCH`: Architecture review needed
> - `READY_FOR_BUILD`: Implementation can start
> - `IN_PROGRESS`: Active work
> - `READY_FOR_REVIEW`: Human review needed
> - `BLOCKED`: Waiting on dependency
> - `DONE`: Complete and verified
> 
> ## Commit Message Format
> Agents should use conventional commits:
> - `feat:` for new features
> - `fix:` for bug fixes
> - `docs:` for documentation
> - `test:` for tests
> - `refactor:` for refactoring
> 
> Include agent name in commit:
> ```
> feat(notifications): Implement push notification service
> 
> Generated by: backend-engineer agent
> Task: notification-system
> ```
> 
> ## Agent Invocation
> Prefer explicit over implicit:
> ```
> ✅ "Use backend-engineer to implement the API"
> ❌ "Implement the API" (unclear which agent)
> ```
> 
> ## Conflict Resolution
> If agents produce conflicting outputs:
> 1. Human reviews both
> 2. Make decision
> 3. Document in ADR why chosen
> 4. Update agent prompts to prevent future conflicts
> ```

> [!methodology-and-sources] Asynchronous Team Collaboration
> **Scenario**: 3 developers working on same feature across timezones
>
> ```
> Developer A (US): Morning work
> ├─ Invokes: requirements-analyst agent
> ├─ Reviews: Requirements document
> ├─ Updates: MULTI_AGENT_PLAN.md with status READY_FOR_ARCH
> └─ Commits: Requirements document
> 
> Developer B (Europe): Afternoon work (A's evening)
> ├─ Pulls: Latest changes
> ├─ Sees: Status READY_FOR_ARCH
> ├─ Invokes: system-architect agent
> ├─ Reviews: Architecture design
> ├─ Updates: MULTI_AGENT_PLAN.md with status READY_FOR_BUILD
> └─ Commits: ADR document
> 
> Developer C (Asia): Morning work (B's evening)
> ├─ Pulls: Latest changes
> ├─ Sees: Status READY_FOR_BUILD
> ├─ Invokes: backend-engineer agent (implementation)
> ├─ Reviews: Implementation
> ├─ Updates: MULTI_AGENT_PLAN.md with status READY_FOR_REVIEW
> └─ Commits: Implementation + tests
> 
> Developer A: Next morning
> ├─ Pulls: Latest changes
> ├─ Sees: Status READY_FOR_REVIEW
> ├─ Invokes: code-quality-reviewer agent
> ├─ Reviews: Automated review findings
> └─ Approves: Creates PR for team review
> 
> Result: 24-hour feature completion with 3 people, minimal overlap
> ```

> [!warning] Team Coordination Pitfalls
> **⚠️ Agent divergence**: Team members modify agents locally without committing
> - **Symptom**: "It works on my machine" but not others'
> - **Solution**: Enforce `.claude/agents/` in git, personal mods in `~/.claude/`
>
> **⚠️ Status confusion**: Different status interpretations
> - **Symptom**: Work proceeds when blocked, or waits unnecessarily
> - **Solution**: Explicit status definitions in AGENT_CONVENTIONS.md
>
> **⚠️ Conflicting agent modifications**: Two devs update same agent
> - **Symptom**: Git merge conflicts in agent definitions
> - **Solution**: Treat agents like code - PR review required for changes
>
> **⚠️ No communication protocol**: Agents can't coordinate across developers
> - **Symptom**: Duplicate work, conflicting approaches
> - **Solution**: Shared state files, status updates, communication log in state

### Observability and Debugging

[**Observability-Debugging-Pattern**:: Instrumenting multi-agent systems with logging, tracing, performance metrics, and decision recording to enable post-hoc analysis of agent behavior, identification of failure patterns, and optimization of agent coordination; treating agents as distributed systems requiring full observability stack.]^verified-stable

> [!definition] Observability Layers
> **1. Execution traces**:
> - Which agents were invoked?
> - In what order?
> - With what inputs?
> - How long did each take?
>
> **2. Decision logs**:
> - Why was this agent selected?
> - What alternatives were considered?
> - What confidence score triggered selection?
>
> **3. Performance metrics**:
> - Token consumption per agent
> - Wall clock time per agent
> - Success/failure rates
> - Retry counts
>
> **4. State evolution**:
> - How did shared state change over time?
> - Which agent made which state updates?
> - Conflicts or rollbacks?

> [!example] Comprehensive Logging Setup
> **Hook script for trace logging**:
>
> `.claude/scripts/log_agent_execution.py`:
> ```python
> import json
> import time
> from datetime import datetime
> from pathlib import Path
> 
> class AgentExecutionLogger:
>     def __init__(self):
>         self.log_dir = Path('.claude/logs/executions')
>         self.log_dir.mkdir(parents=True, exist_ok=True)
>         self.session_id = datetime.now().strftime('%Y%m%d_%H%M%S')
>     
>     def log_invocation(self, agent_name, trigger, context):
>         """Log when agent is invoked"""
>         log_entry = {
>             'timestamp': datetime.now().isoformat(),
>             'session_id': self.session_id,
>             'event': 'agent_invoked',
>             'agent_name': agent_name,
>             'trigger': trigger,  # 'automatic' or 'explicit'
>             'context': {
>                 'user_query': context.get('query'),
>                 'keywords_matched': context.get('keywords'),
>                 'confidence_score': context.get('confidence'),
>                 'parent_agent': context.get('parent')
>             }
>         }
>         self._write_log(log_entry)
>     
>     def log_completion(self, agent_name, status, metrics):
>         """Log when agent completes"""
>         log_entry = {
>             'timestamp': datetime.now().isoformat(),
>             'session_id': self.session_id,
>             'event': 'agent_completed',
>             'agent_name': agent_name,
>             'status': status,  # 'success', 'failure', 'timeout'
>             'metrics': {
>                 'duration_seconds': metrics.get('duration'),
>                 'tokens_used': metrics.get('tokens'),
>                 'tools_invoked': metrics.get('tools'),
>                 'retry_count': metrics.get('retries', 0)
>             },
>             'output_summary': metrics.get('output_summary')
>         }
>         self._write_log(log_entry)
>     
>     def log_error(self, agent_name, error_type, error_details):
>         """Log agent errors"""
>         log_entry = {
>             'timestamp': datetime.now().isoformat(),
>             'session_id': self.session_id,
>             'event': 'agent_error',
>             'agent_name': agent_name,
>             'error': {
>                 'type': error_type,
>                 'message': str(error_details),
>                 'severity': self._classify_severity(error_type)
>             }
>         }
>         self._write_log(log_entry)
>     
>     def _write_log(self, entry):
>         log_file = self.log_dir / f'session_{self.session_id}.jsonl'
>         with open(log_file, 'a') as f:
>             f.write(json.dumps(entry) + '\n')
>     
>     def _classify_severity(self, error_type):
>         severity_map = {
>             'ToolPermissionDenied': 'high',
>             'TokenLimitExceeded': 'medium',
>             'InvalidOutputFormat': 'low'
>         }
>         return severity_map.get(error_type, 'medium')
> ```

> [!methodology-and-sources] Analysis Queries
> **Query patterns for debugging**:
>
> ```python
> # Find all failed agent invocations
> def find_failures(session_id):
>     log_file = f'.claude/logs/executions/session_{session_id}.jsonl'
>     failures = []
>     
>     with open(log_file) as f:
>         for line in f:
>             entry = json.loads(line)
>             if entry['event'] == 'agent_completed' and entry['status'] == 'failure':
>                 failures.append(entry)
>     
>     return failures
> 
> # Analyze agent performance  
> def agent_performance_report():
>     metrics = {}
>     
>     for log_file in Path('.claude/logs/executions').glob('*.jsonl'):
>         with open(log_file) as f:
>             for line in f:
>                 entry = json.loads(line)
>                 if entry['event'] == 'agent_completed':
>                     agent = entry['agent_name']
>                     if agent not in metrics:
>                         metrics[agent] = {
>                             'invocations': 0,
>                             'successes': 0,
>                             'failures': 0,
>                             'total_duration': 0,
>                             'total_tokens': 0
>                         }
>                     
>                     metrics[agent]['invocations'] += 1
>                     if entry['status'] == 'success':
>                         metrics[agent]['successes'] += 1
>                     else:
>                         metrics[agent]['failures'] += 1
>                     
>                     m = entry['metrics']
>                     metrics[agent]['total_duration'] += m['duration_seconds']
>                     metrics[agent]['total_tokens'] += m['tokens_used']
>     
>     # Calculate averages
>     for agent, data in metrics.items():
>         n = data['invocations']
>         data['avg_duration'] = data['total_duration'] / n
>         data['avg_tokens'] = data['total_tokens'] / n
>         data['success_rate'] = data['successes'] / n * 100
>     
>     return metrics
> 
> # Find coordination bottlenecks
> def find_bottlenecks(session_id):
>     """Identify agents that cause long wait times"""
>     log_file = f'.claude/logs/executions/session_{session_id}.jsonl'
>     events = []
>     
>     with open(log_file) as f:
>         for line in f:
>             events.append(json.loads(line))
>     
>     # Sort by timestamp
>     events.sort(key=lambda e: e['timestamp'])
>     
>     # Find gaps
>     gaps = []
>     for i in range(len(events) - 1):
>         current = datetime.fromisoformat(events[i]['timestamp'])
>         next_event = datetime.fromisoformat(events[i+1]['timestamp'])
>         gap = (next_event - current).total_seconds()
>         
>         if gap > 30:  # More than 30 second gap
>             gaps.append({
>                 'after_agent': events[i]['agent_name'],
>                 'before_agent': events[i+1]['agent_name'],
>                 'gap_seconds': gap
>             })
>     
>     return sorted(gaps, key=lambda g: g['gap_seconds'], reverse=True)
> ```

> [!example] Dashboard for Agent Monitoring
> **Visualizing agent activity**:
>
> ```python
> # Generate HTML dashboard from logs
> def generate_dashboard(output_path='agent-dashboard.html'):
>     metrics = agent_performance_report()
>     
>     html = """
>     <!DOCTYPE html>
>     <html>
>     <head>
>         <title>Agent Performance Dashboard</title>
>         <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
>         <style>
>             body { font-family: Arial, sans-serif; margin: 20px; }
>             .metric { display: inline-block; margin: 10px; padding: 15px;
>                       border: 1px solid #ccc; border-radius: 5px; }
>             .metric-value { font-size: 24px; font-weight: bold; }
>             .metric-label { color: #666; }
>         </style>
>     </head>
>     <body>
>         <h1>Multi-Agent Performance Dashboard</h1>
>         
>         <h2>Agent Success Rates</h2>
>     """
>     
>     for agent, data in metrics.items():
>         html += f"""
>         <div class="metric">
>             <div class="metric-label">{agent}</div>
>             <div class="metric-value">{data['success_rate']:.1f}%</div>
>             <div class="metric-label">
>                 {data['invocations']} invocations | 
>                 Avg: {data['avg_duration']:.1f}s, 
>                 {data['avg_tokens']:.0f} tokens
>             </div>
>         </div>
>         """
>     
>     html += """
>         <h2>Token Usage Over Time</h2>
>         <canvas id="tokenChart" width="800" height="400"></canvas>
>         
>         <script>
>             // Chart data would be populated from logs
>             const ctx = document.getElementById('tokenChart').getContext('2d');
>             const chart = new Chart(ctx, { /* chart config */ });
>         </script>
>     </body>
>     </html>
>     """
>     
>     Path(output_path).write_text(html)
>     print(f"Dashboard generated: {output_path}")
> ```

> [!key-claim] Debugging Non-Determinism
> [**Non-Determinism-Debugging**:: Agent systems are non-deterministic (same input can produce different outputs), making traditional debugging difficult; observability through comprehensive logging becomes essential to understand why an agent made specific decisions and how to reproduce or fix issues.]^verified-stable
>
> **Traditional debugging (deterministic code)**:
> - Input X → always produces Output Y
> - Reproduce by running with same input
> - Fix by changing code logic
>
> **Agent debugging (non-deterministic)**:
> - Input X → produces Output Y₁, Y₂, Y₃... (varies)
> - Reproduction requires: input + random seed + model state + prompt
> - Fix by: changing prompt, adding examples, adjusting temperature
>
> **Solution**: Log everything
> - Input (exact query text)
> - Context (what was in context window)
> - Agent selection reasoning (why this agent chosen)
> - Intermediate steps (tool calls, sub-decisions)
> - Output (full response)
> - Metadata (model, temperature, seed if available)

---

## 🎯 Synthesis & Mastery

> [!the-philosophy]
> **Core Principles Governing Multi-Agent Claude Code Systems**
>
> [**Specialization-Over-Generalization**:: Narrow, focused agents with single responsibilities outperform general-purpose agents on domain-specific tasks because specialization allows for optimized prompts, restricted tool access, and maintained focus without context pollution from unrelated concerns.]^verified-stable
>
> [**Coordination-Through-Simplicity**:: Complex orchestration frameworks are rarely necessary; simple coordination mechanisms like shared markdown files, status markers, and file-based state management prove more maintainable and debuggable than sophisticated multi-agent communication protocols.]^verified-stable
>
> [**Isolation-Enables-Scale**:: Context isolation is the architectural feature that makes multi-agent systems work at scale; without it, context windows fill with irrelevant details, attention degrades, and parallelization becomes impossible due to shared-state conflicts.]^verified-stable
>
> [**Explicit-Over-Implicit**:: Explicit agent invocation, explicit status tracking, explicit state updates, and explicit error handling create deterministic, debuggable systems; implicit coordination (hoping agents figure it out) leads to unpredictable behavior and difficult troubleshooting.]^verified-stable
>
> [**Main-Agent-As-Hub**:: The coordinator is not a separate specialized agent but rather the main Claude instance acting as orchestrator; this star topology (vs. mesh) prevents infinite agent nesting, simplifies reasoning about execution flow, and creates auditable coordination paths.]^verified-stable

> [!mental-model-anchor]
> **Connections to Foundational Mental Models**
>
> **Software Architecture**:
> - Multi-agent systems mirror [[Microservices Architecture]]: independent services (agents), clear interfaces (descriptions), centralized orchestration (main agent as API gateway)
> - Context isolation parallels [[Bounded Contexts]] in Domain-Driven Design: each agent operates within its domain boundary
> - Shared state files function as [[Message Queues]] in distributed systems: asynchronous communication, eventual consistency
>
> **Distributed Systems**:
> - Sequential pipeline pattern implements [[MapReduce]]: map (parallelize subtasks) and reduce (synthesize results)
> - Hook-based automation mirrors [[Event-Driven Architecture]]: agents publish events (status changes), hooks subscribe and react
> - Error handling follows [[Circuit Breaker Pattern]]: detect failures, prevent cascades, implement fallbacks
>
> **Team Dynamics**:
> - Agent specialization reflects [[Conway's Law]]: system architecture mirrors communication structure (agents mirror team roles)
> - Coordination strategies parallel [[Agile Standups]]: shared state files = async status updates, agents = team members reporting progress
> - Tool restriction embodies [[Principle of Least Privilege]]: agents get minimum permissions needed, reducing security risk
>
> **Cognitive Science**:
> - Context isolation prevents [[Cognitive Load]] overload: each agent processes limited, relevant information
> - Specialization leverages [[Expertise Theory]]: deep knowledge in narrow domain > shallow knowledge across broad domain
> - Explicit communication reduces [[Working Memory]] burden: written state > remembered state

> [!application-context]
> **Where/When/How to Apply Multi-Agent Systems**
>
> **When to Use Multi-Agent Architecture**:
> ✅ **Complex projects** requiring multiple domains (frontend + backend + database + security)
> ✅ **Long-running tasks** where single-agent context would saturate (migrations, refactors)
> ✅ **Parallel-capable work** where subtasks are independent (research, code generation)
> ✅ **Team environments** where multiple developers need coordination (async collaboration)
> ✅ **High-quality requirements** where specialized review gates matter (security audits, architecture validation)
>
> **When to Avoid Multi-Agent Architecture**:
> ❌ **Simple tasks** achievable in <20 messages with single agent (formatting, small fixes)
> ❌ **Tightly coupled** work requiring constant iteration (design + implementation co-evolution)
> ❌ **Rapid prototyping** where overhead of coordination outweighs benefits (spikes, POCs)
> ❌ **Solo developer** working alone without need for role separation (personal projects)
> ❌ **Learning phase** when still understanding requirements (agents need clear boundaries)
>
> **How to Apply Progressively**:
> ```
> Level 1: Single agent (baseline)
> └─ User ↔ Claude (all work in main conversation)
> 
> Level 2: Two agents (read/write separation)
> ├─ code-reviewer: Read-only analysis
> └─ implementer: Write implementation
> 
> Level 3: Sequential pipeline (3-5 agents)
> ├─ requirements-analyst
> ├─ system-architect  
> ├─ implementer
> └─ code-quality-reviewer
> 
> Level 4: Parallel coordination (5-10 agents)
> ├─ backend-engineer ┐
> ├─ frontend-engineer ├─ Parallel
> ├─ database-architect ┘
> └─ Main agent synthesizes
> 
> Level 5: Production orchestration (10+ agents)
> ├─ Complete pipeline with hooks
> ├─ Automated state management
> ├─ CI/CD integration
> └─ Team collaboration workflows
> ```

---

## 🔗 PKB Integration

> [!connections-and-links]
> **Explicit Connections to Existing PKB Concepts**
>
> **Direct Prerequisites** (must understand before this):
> - [[Claude Code Basics]] - Installation, configuration, fundamental usage
> - [[CLAUDE.md Files]] - Project context and memory system
> - [[Prompt Engineering Fundamentals]] - How to write effective agent prompts
> - [[YAML Syntax]] - Required for agent frontmatter
>
> **Sibling Concepts** (parallel systems, often used together):
> - [[MCP Servers]] - Tool integration extends agent capabilities
> - [[Custom Commands]] - Slash commands for orchestration templates
> - [[Skills System]] - Auto-loaded knowledge for agents
> - [[Output Styles]] - Meta-prompts changing orchestration behavior
> - [[Hooks System]] - Lifecycle events for automation
>
> **Child Concepts** (specialized topics that elaborate this):
> - [[Agent File Format Specification]] - Deep dive into YAML + markdown structure
> - [[Coordination Pattern Library]] - Collection of proven orchestration strategies
> - [[Tool Permission Grammar]] - Syntax for restricting agent capabilities
> - [[State Management Protocols]] - Best practices for shared state files
> - [[Agent Prompt Engineering]] - Specialized prompting for agents vs. main Claude
>
> **Cross-Domain Bridges** (connections to other fields):
> - [[Microservices Architecture]] → Agent isolation mirrors service boundaries
> - [[Distributed Systems Design]] → State management, error handling, coordination
> - [[Multi-Agent AI Systems]] → Academic research on agent coordination
> - [[Software Engineering Workflows]] → CI/CD, git integration, code review
> - [[Team Collaboration Patterns]] → Async communication, role separation

> [!atomic-candidates]
> **Concepts Warranting Extraction to Atomic Notes**
>
> These concepts have sufficient depth and cross-reference potential to become standalone atomic notes:
>
> 1. **[[Agent Definition File Format]]** - YAML frontmatter + markdown system prompt structure
>    - Why atomic: Referenced by every agent creation task, has specific syntax rules
>
> 2. **[[Context Isolation Architecture]]** - How separate context windows prevent pollution
>    - Why atomic: Core architectural principle referenced across agent design decisions
>
> 3. **[[Sequential Pipeline Pattern]]** - PM → Architect → Implementer workflow
>    - Why atomic: Reusable pattern applicable to many development workflows
>
> 4. **[[Shared State Coordination]]** - MULTI_AGENT_PLAN.md communication protocol
>    - Why atomic: Specific implementation pattern with code examples
>
> 5. **[[Tool Restriction Strategies]]** - Safety through limited tool access
>    - Why atomic: Security-critical concept with specific implementation guidance
>
> 6. **[[Model Selection Economics]]** - Haiku vs. Sonnet vs. Opus cost/performance tradeoffs
>    - Why atomic: Frequently referenced decision-making framework
>
> 7. **[[Description Field Optimization]]** - Tool SEO for agent auto-activation
>    - Why atomic: Specific technique with concrete examples and anti-patterns
>
> 8. **[[Hook-Based Automation]]** - Event-driven agent coordination
>    - Why atomic: Complex topic with code examples and integration patterns
>
> 9. **[[Error Handling in Multi-Agent Systems]]** - Rollback, retry, human-in-loop protocols
>    - Why atomic: Production-critical topic with detailed implementation strategies
>
> 10. **[[Main Agent as Coordinator]]** - Star topology orchestration architecture
>     - Why atomic: Fundamental architectural decision affecting all agent interactions

> [!synthesis-opportunities]
> **Cross-Domain Connection Potentials**
>
> **1. Multi-Agent Systems + Zettelkasten Method**
> - **Connection**: Agents as specialized note-taking assistants
> - **Potential**: Literature-note agent, permanent-note agent, index-note agent
> - **Application**: PKM workflow automation with agent specialization
>
> **2. Multi-Agent Systems + Test-Driven Development**
> - **Connection**: Test-writing agent + implementation agent coordination
> - **Potential**: Automated TDD workflow with quality gates
> - **Application**: Red-green-refactor cycle with agent separation
>
> **3. Multi-Agent Systems + Documentation Generation**
> - **Connection**: Code-analysis agent + documentation-writer agent pipeline
> - **Potential**: Automatic API docs, architecture diagrams, user guides
> - **Application**: Living documentation that stays synchronized with code
>
> **4. Multi-Agent Systems + Code Review Automation**
> - **Connection**: Multiple specialized review agents (security, performance, style)
> - **Potential**: Comprehensive automated review before human review
> - **Application**: Pre-PR quality gates reducing human review burden
>
> **5. Multi-Agent Systems + Learning Pathways**
> - **Connection**: Topic-expert agents guiding progressive learning
> - **Potential**: Personalized curriculum with agent-facilitated mastery
> - **Application**: Educational scaffolding through specialized tutoring agents

---

## 📊 Metadata & Attribution

> [!methodology-and-sources]
> **Research Methodology**
> 
> **Exploration Strategy**: Depth-first search across 5 primary dimensions:
> 1. Claude Code architecture fundamentals
> 2. Multi-agent design patterns
> 3. Prompt engineering for agents
> 4. File system implementation
> 5. Coordination logic and orchestration
>
> **Total Searches**: 10 targeted web searches
> - 3 searches on architecture and file system
> - 3 searches on coordination patterns
> - 2 searches on agent definitions and examples
> - 2 searches on prompt engineering and best practices
>
> **Primary Sources**:
> 1. **Official Documentation**:
>    - [Claude Code Docs - Subagents](https://code.claude.com/docs/en/sub-agents) - Agent definition format, invocation mechanisms
>    - [Claude Code Docs - Settings](https://code.claude.com/docs/en/settings) - Configuration hierarchy, file system structure
>    - [Anthropic Blog - CLAUDE.md](https://claude.com/blog/using-claude-md-files) - Project context and memory system
>
> 2. **Engineering Best Practices**:
>    - [Anthropic Engineering - Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system) - 90.2% improvement data, parallel execution patterns
>    - [Anthropic Engineering - Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices) - Workflow integration, TDD patterns
>
> 3. **Real-World Implementations**:
>    - [wshobson/agents](https://github.com/wshobson/agents) - 67 production agents, coordination patterns
>    - [PubNub - Subagent Best Practices](https://www.pubnub.com/blog/best-practices-for-claude-code-sub-agents/) - Three-stage pipeline, hook-based automation
>    - [bwads001/claude-code-agents](https://github.com/bwads001/claude-code-agents) - Output style orchestration
>
> 4. **Community Guides**:
>    - [ClaudeLog - Agent Engineering](https://claudelog.com/mechanics/agent-engineering/) - Model selection economics, tool SEO
>    - [Shipyard - Agent Guide](https://shipyard.build/blog/claude-code-subagents-guide/) - Practical agent personas
>
> **Confidence Distribution**:
> - **Verified-Stable** (80%): Official docs, Anthropic engineering posts, consistent across multiple sources
> - **Probable** (15%): Community best practices with strong evidence but limited official confirmation
> - **Provisional** (5%): Emerging patterns from cutting-edge implementations
>
> **Knowledge Gaps Acknowledged**:
> - Large-scale orchestration (50+ agents) remains experimental with limited documentation
> - State consistency guarantees in parallel execution under-documented
> - Advanced error recovery strategies beyond basic retry logic sparse
> - Long-term agent maintenance and versioning strategies not well established

---

## 🔗 Related Topics for PKB Expansion

1. **[[Claude Code MCP Server Integration]]**
   - **Connection**: MCP servers extend agent capabilities with external tools; agents can be configured with specific MCP servers for domain expertise
   - **Depth Potential**: Complete guide to MCP architecture, server discovery, tool integration patterns, and custom MCP server development
   - **Knowledge Graph Role**: Sibling to multi-agent systems; both are extension mechanisms but operate at different levels (tools vs. agents)
   - **Priority**: High - MCP servers frequently used alongside agents to provide specialized capabilities

2. **[[Production Agent Prompt Library]]**
   - **Connection**: Collection of battle-tested agent system prompts across domains (security, testing, documentation, architecture)
   - **Depth Potential**: 20-30 agent prompt templates with usage patterns, customization guides, and domain-specific best practices
   - **Knowledge Graph Role**: Child of this note; provides concrete implementations of agent engineering principles
   - **Priority**: High - Practical value for immediate application; accelerates agent creation

3. **[[Agentic Workflow Design Patterns]]**
   - **Connection**: Catalog of reusable coordination patterns beyond sequential pipeline (event-driven, saga pattern, choreography vs. orchestration)
   - **Depth Potential**: 10-15 patterns with diagrams, code examples, use cases, and tradeoff analysis
   - **Knowledge Graph Role**: Extension of coordination strategies; links to [[Distributed Systems Design]]
   - **Priority**: Medium - Valuable for advanced users building complex workflows

4. **[[Agent Observability and Debugging Toolkit]]**
   - **Connection**: Deep dive into observability infrastructure, logging frameworks, visualization tools, and debugging methodologies specific to multi-agent systems
   - **Depth Potential**: Complete observability stack with log analysis tools, dashboard templates, alerting strategies, and production troubleshooting playbooks
   - **Knowledge Graph Role**: Critical production support topic; connects to [[DevOps Practices]]
   - **Priority**: Medium-High - Essential for production deployments but not needed for initial experimentation

5. **[[Multi-Agent PKM Automation]]**
   - **Connection**: Applying multi-agent systems specifically to Personal Knowledge Management workflows (note generation, linking, synthesis, research)
   - **Depth Potential**: Specialized agents for Obsidian workflows, Zettelkasten automation, literature review, and knowledge synthesis
   - **Knowledge Graph Role**: Cross-domain bridge to [[PKM Systems]] and [[Knowledge Work Automation]]
   - **Priority**: High - Direct relevance to your PKB development goals

6. **[[Enterprise Multi-Agent Governance]]**
   - **Connection**: Policies, security controls, compliance requirements, and organizational standards for deploying agent systems in enterprise environments
   - **Depth Potential**: Security frameworks, audit trails, access controls, data privacy, regulatory compliance
   - **Knowledge Graph Role**: Connects to [[Enterprise Software Architecture]] and [[Security Governance]]
   - **Priority**: Low - Relevant for enterprise deployments but not personal/small team usage
