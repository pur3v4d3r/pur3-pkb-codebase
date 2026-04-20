---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Contract-Style Prompt Structure"
aliases:
  - "Contract-Style Prompt Structure"
  - "Contract-Style-Prompt-Structure"
  - "CPS"
type: permanent-note
status: evergreen
confidence: medium

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
  - permanent-note
  - evergreen
  - other
  - claude-code
  - multi-agent-systems
  - ai-orchestration
  - agentic-architecture
  - prompt-engineering
  - agent-coordination
  - pkm-integration

domain: other
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-04-20
updated: 2026-04-20

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "multi-agent-systems-with-claude-code"
evidence-quality: medium
extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"
pipeline-version: "2.1.0"
extraction-date: "2026-04-20"

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
complexity-level: intermediate
depth-level: comprehensive

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  []

related:
  []

broader:
  []

narrower:
  []

see-also:
  - "[[claude-opus-4|Claude-Opus-4]]"
  - "[[claude-sonnet-4|Claude-Sonnet-4]]"
  - "[[skills|Skills]]"
  - "[[microservices-architecture|Microservices-Architecture]]"
  - "[[bounded-contexts|Bounded-Contexts]]"
  - "[[message-queues|Message-Queues]]"
  - "[[mapreduce|MapReduce]]"
  - "[[event-driven-architecture|Event-Driven-Architecture]]"
  - "[[circuit-breaker-pattern|Circuit-Breaker-Pattern]]"
  - "[[conways-law|Conway's-Law]]"
  - "[[agile-standups|Agile-Standups]]"
  - "[[principle-of-least-privilege|Principle-of-Least-Privilege]]"
  - "[[cognitive-load|Cognitive-Load]]"
  - "[[expertise-theory|Expertise-Theory]]"
  - "[[working-memory|Working-Memory]]"
  - "[[claude-code-basics|Claude-Code-Basics]]"
  - "[[claude.md-files|CLAUDE.md-Files]]"
  - "[[prompt-engineering-fundamentals|Prompt-Engineering-Fundamentals]]"
  - "[[yaml-syntax|YAML-Syntax]]"
  - "[[mcp-servers|MCP-Servers]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  []

enables:
  []

expansion-topics:
  []

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: medium
---

# Contract-Style Prompt Structure

> [!definition] **Contract-Style Prompt Structure** *(from [[multi-agent-systems-with-claude-code]])*
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

## Core Explanation

> [!analytical-insight] Key Insight *(from [[multi-agent-systems-with-claude-code]])*
> [**Context-Isolation-Benefit**:: Each subagent maintains a separate conversation history and context window from the main agent and other subagents, preventing the "context pollution" that degrades performance in long conversations where unrelated information competes for attention and reduces focus on the current subtask.]^verified-stable
> 
> This isolation enables:
> - **Focus**: Subagents see only information relevant to their specialized task
> - **Scale**: Main conversation doesn't bloat with…

> [!analytical-insight] Key Insight *(from [[multi-agent-systems-with-claude-code]])*
> [**Agent-Scope-Precedence**:: When agent names conflict between user-level and project-level definitions, project-level agents take precedence, allowing projects to override global agent behavior with domain-specific expertise while maintaining consistent agent names across the team.]^verified-stable

> [!analytical-insight] Key Insight *(from [[multi-agent-systems-with-claude-code]])*
> [**Coordinator-Architecture**:: The "coordinator agent" is not a separate agent file but rather the main Claude instance (general-purpose agent) that the user interacts with directly; it analyzes tasks, delegates to specialized subagents, aggregates results, and maintains high-level conversation continuity.]^verified-stable
> 
> **This is a critical architectural insight**: You don't create a separate "coordinator.md" file. Instead, you influence the main agent's coordination behavior through:
> 1.…

> [!analytical-insight] Key Insight *(from [[multi-agent-systems-with-claude-code]])*
> [**Agent-Result-Passing**:: Agents communicate indirectly by returning results to the main agent, which then incorporates that information into subsequent agent invocations or uses it to make coordination decisions; this creates an information flow mediated by the coordinator.]^verified-stable
> 
> **Pattern**:
> ```
> Main Agent → Agent A (get requirements)
>   → Main Agent receives: "Feature needs authentication + role-based access"
>   → Main Agent → Agent B (design with those requirements)
>       → Main…

> [!analytical-insight] Key Insight *(from [[multi-agent-systems-with-claude-code]])*
> [**Parallel-Execution-Use-Cases**:: Most effective for breadth-first tasks requiring exploration of multiple independent directions simultaneously, such as multi-source research, full-stack feature development with separate frontend/backend work, or comprehensive security audits with multiple specialized checks.]^verified-stable
> 
> Anthropic's research system achieved **90.2% performance improvement** using parallel execution: a lead researcher agent delegated tasks to multiple Sonnet agents…

> [!analytical-insight] Key Insight *(from [[multi-agent-systems-with-claude-code]])*
> [**Coordination-Simplicity-Principle**:: Markdown files as coordination mechanism outperform complex orchestration frameworks for most use cases because they're human-readable, version-controllable, easily debuggable, and don't require additional infrastructure; the simplest solution that works is often the best solution.]^verified-stable

> [!analytical-insight] Key Insight *(from [[multi-agent-systems-with-claude-code]])*
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
> You are a code reviewer. Execute this exact…

> [!analytical-insight] Key Insight *(from [[multi-agent-systems-with-claude-code]])*
> [**Haiku-4.5-Performance**:: Claude Haiku 4.5 (released October 2025) delivers 90% of Sonnet 4.5's agentic coding performance at 2x the speed and 3x cost savings ($1/$5 vs $3/$15 per million tokens), making it the optimal choice for most agent tasks and dramatically extending usage limits for subscription users.]^verified-stable
> 
> **Cost comparison** (API pricing):
> - Haiku 4.5: $1 input / $5 output per million tokens
> - Sonnet 4.5: $3 input / $15 output per million tokens  
> - Opus 4: $15 input /…

> [!analytical-insight] Key Insight *(from [[multi-agent-systems-with-claude-code]])*
> [**Tool-SEO-Triggers**:: Specific phrases that boost agent auto-activation probability include "use PROACTIVELY", "MUST BE USED", "automatically invoke when", and "triggers on"; these signal to Claude's selection mechanism that the agent should be considered aggressively for matching tasks.]^verified-stable
> 
> **High-impact phrases**:
> - "Use PROACTIVELY" - Strongest signal
> - "MUST BE USED when" - Creates requirement
> - "Automatically invoke for" - Clear trigger
> - "Always call when" - Explicit…

> [!analytical-insight] Key Insight *(from [[multi-agent-systems-with-claude-code]])*
> [**Context-Pollution-Degradation**:: In single-agent conversations, as context window fills with diverse information (code explorations, debugging attempts, test iterations, documentation searches), the agent's ability to maintain focus on the original task degrades because attention is distributed across unrelated context elements.]^verified-stable
> 
> **Example scenario**:
> ```
> Message 1: "Build a user dashboard"
> Messages 2-20: Database schema exploration
> Messages 21-40: API endpoint debugging …

> [!analytical-insight] Key Insight *(from [[multi-agent-systems-with-claude-code]])*
> [**Parallel-Context-Independence**:: Because each subagent has an isolated context window, multiple agents can work simultaneously on different aspects of a task without context conflicts or attention competition; one agent's detailed exploration doesn't interfere with another agent's focus.]^verified-stable
> 
> **Sequential (shared context)**:
> ```
> Time 0-20min: Agent explores database (context fills with DB details)
> Time 20-45min: Agent builds API (context now has DB + API details)
> Time 45-70min:…

> [!analytical-insight] Key Insight *(from [[multi-agent-systems-with-claude-code]])*
> [**Adaptive-Routing-Behavior**:: The main agent learns from context and conversation history which agents are most effective for different task types; this creates implicit routing optimization where successful agent selections become more likely to be repeated for similar future tasks within the same conversation.]^verified-stable
> 
> **Example**:
> ```
> Message 1: "Review this code for security"
> Main Agent → security-auditor (finds vulnerabilities)
> 
> Message 10: "Review that other module too"
> Main…

> [!analytical-insight] Key Insight *(from [[multi-agent-systems-with-claude-code]])*
> [**Non-Determinism-Debugging**:: Agent systems are non-deterministic (same input can produce different outputs), making traditional debugging difficult; observability through comprehensive logging becomes essential to understand why an agent made specific decisions and how to reproduce or fix issues.]^verified-stable
> 
> **Traditional debugging (deterministic code)**:
> - Input X → always produces Output Y
> - Reproduce by running with same input
> - Fix by changing code logic
> 
> **Agent debugging…

## Practical Implications

> [!example] **Application**
> *Describe how this concept applies in practice.*

> [!warning] **Key Distinction** *(from [[multi-agent-systems-with-claude-code]])*
> **Problem**: If agents could spawn other agents recursively, you'd encounter:
> - **Infinite loops**: Agent A calls Agent B calls Agent A...
> - **Context explosion**: Each level creates new context windows
> - **Cost multipliers**: Exponential token consumption
> - **Debugging nightmares**: Non-deterministic execution trees
> 
> **Solution**: All delegation goes through the main agent, creating a **star topology** instead of a mesh network.

> [!warning] **Key Distinction** *(from [[multi-agent-systems-with-claude-code]])*
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
> **✅…

> [!warning] **Key Distinction** *(from [[multi-agent-systems-with-claude-code]])*
> **⚠️ Dependency conflicts**: Agents working on interdependent components may produce incompatible interfaces
> - **Mitigation**: Main agent should define interface contracts before spawning agents
> 
> **⚠️ Result coordination complexity**: Synthesizing 5+ parallel agent outputs into coherent whole
> - **Mitigation**: Structured output formats, clear success criteria
> 
> **⚠️ File system conflicts**: Multiple agents modifying same files simultaneously
> - **Mitigation**: Each agent works in separate…

> [!warning] **Key Distinction** *(from [[multi-agent-systems-with-claude-code]])*
> **⚠️ Hook failures are silent**: If your hook script has a bug, it fails silently without blocking the main agent
> - **Mitigation**: Log all hook executions to `.claude/logs/hooks.log`
> 
> **⚠️ Infinite loops possible**: Poorly designed hooks can trigger each other in cycles  
> - **Mitigation**: Include loop detection (max 3 consecutive same-agent invocations)
> 
> **⚠️ State file corruption**: Concurrent hook executions might corrupt shared state
> - **Mitigation**: Use file locking or atomic writes
> 
> **✅…

> [!warning] **Key Distinction** *(from [[multi-agent-systems-with-claude-code]])*
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
> # Add bash only for…

> [!warning] **Key Distinction** *(from [[multi-agent-systems-with-claude-code]])*
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
> Ambiguous overlap causes…

> [!warning] **Key Distinction** *(from [[multi-agent-systems-with-claude-code]])*
> **⚠️ Tight coupling**: If agents need continuous back-and-forth, isolation creates communication overhead
> 
> **Example**: Frontend and backend need to iterate on API contract
> - **Without isolation**: Direct iteration in same context
> - **With isolation**: Must pass through main agent for each iteration
> 
> **Solution**: Keep tightly coupled work in single agent, use isolation for loosely coupled tasks.

> [!warning] **Key Distinction** *(from [[multi-agent-systems-with-claude-code]])*
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
> -…

> [!warning] **Key Distinction** *(from [[multi-agent-systems-with-claude-code]])*
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
>    -…

> [!warning] **Key Distinction** *(from [[multi-agent-systems-with-claude-code]])*
> **⚠️ Agent divergence**: Team members modify agents locally without committing
> - **Symptom**: "It works on my machine" but not others'
> - **Solution**: Enforce `.claude/agents/` in git, personal mods in `~/.claude/`
> 
> **⚠️ Status confusion**: Different status interpretations
> - **Symptom**: Work proceeds when blocked, or waits unnecessarily
> - **Solution**: Explicit status definitions in AGENT_CONVENTIONS.md
> 
> **⚠️ Conflicting agent modifications**: Two devs update same agent
> - **Symptom**: Git…

## Concrete Examples

> [!example] **Context Pollution Scenario** *(from [[multi-agent-systems-with-claude-code]])*
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
> **With subagents**: Main agent maintains high-level orchestration ("use backend-engineer → frontend-specialist → code-reviewer"), while each specialist's detailed work happens in isolated…

> [!example] **Real-World Agent: Code Quality Reviewer** *(from [[multi-agent-systems-with-claude-code]])*
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
>    - Performance problems…

> [!example] **Implicit vs. Explicit Coordination** *(from [[multi-agent-systems-with-claude-code]])*
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
>              [Invokes…

> [!example] **Auto-Delegation in Action** *(from [[multi-agent-systems-with-claude-code]])*
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

> [!example] **When to Use Explicit Invocation** *(from [[multi-agent-systems-with-claude-code]])*
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

> [!example] **Real-World Pipeline Implementation** *(from [[multi-agent-systems-with-claude-code]])*
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
> - **Last Updated**:…

> [!example] **Full-Stack Parallel Development** *(from [[multi-agent-systems-with-claude-code]])*
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

> [!example] **Multiple VSCode Terminals Pattern** *(from [[multi-agent-systems-with-claude-code]])*
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
> **Coordination**: Agents coordinate through the…

> [!example] **Autonomous Pipeline with Hooks** *(from [[multi-agent-systems-with-claude-code]])*
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
> next_agent =…

> [!example] **Output Style Workflow** *(from [[multi-agent-systems-with-claude-code]])*
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
> └─ Produces: ADR + technical…

> [!example] **Production-Grade Security Auditor Agent** *(from [[multi-agent-systems-with-claude-code]])*
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
> ## Success…

> [!example] **Tool Restriction by Agent Type** *(from [[multi-agent-systems-with-claude-code]])*
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
> Can read source code, write test files, run tests, but cannot…

> [!example] **Optimized Agent Fleet** *(from [[multi-agent-systems-with-claude-code]])*
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
> name:…

> [!example] **Description Optimization Before/After** *(from [[multi-agent-systems-with-claude-code]])*
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
>   - User…

> [!example] **Version Control Strategy** *(from [[multi-agent-systems-with-claude-code]])*
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

> [!example] **Context Isolation in Action** *(from [[multi-agent-systems-with-claude-code]])*
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
> Focus: Diluted across many unrelated…

> [!example] **Production Agent Library** *(from [[multi-agent-systems-with-claude-code]])*
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
>    - Integration…

> [!example] **Coordination Workflow with Real Agents** *(from [[multi-agent-systems-with-claude-code]])*
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
> │…

> [!example] **Task Decomposition Example** *(from [[multi-agent-systems-with-claude-code]])*
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
> │  └─ Agent:…

> [!example] **Markdown State Protocol** *(from [[multi-agent-systems-with-claude-code]])*
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
> -…

> [!example] **Error Handling Workflow** *(from [[multi-agent-systems-with-claude-code]])*
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
>     …

> [!example] **Automatic Retry Logic** *(from [[multi-agent-systems-with-claude-code]])*
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
>                …

> [!example] **Agent-Driven Feature Development** *(from [[multi-agent-systems-with-claude-code]])*
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
> 3. backend-engineer + frontend-engineer…

> [!example] **Team Agent Library** *(from [[multi-agent-systems-with-claude-code]])*
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
> │  …

> [!example] **Comprehensive Logging Setup** *(from [[multi-agent-systems-with-claude-code]])*
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
>            …

> [!example] **Dashboard for Agent Monitoring** *(from [[multi-agent-systems-with-claude-code]])*
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
>            …

## Connections & Context

**Cross-report connections** *(from [[multi-agent-systems-with-claude-code]])*:
- [[claude-code-basics|Claude-Code-Basics]]
- [[claude.md-files|CLAUDE.md-Files]]
- [[prompt-engineering-fundamentals|Prompt-Engineering-Fundamentals]]
- [[yaml-syntax|YAML-Syntax]]
- [[mcp-servers|MCP-Servers]]
- [[custom-commands|Custom-Commands]]
- [[skills-system|Skills-System]]
- [[output-styles|Output-Styles]]
- [[hooks-system|Hooks-System]]
- [[agent-file-format-specification|Agent-File-Format-Specification]]

**Related concepts:**
[[claude-opus-4|Claude-Opus-4]] · [[claude-sonnet-4|Claude-Sonnet-4]] · [[skills|Skills]] · [[microservices-architecture|Microservices-Architecture]] · [[bounded-contexts|Bounded-Contexts]] · [[message-queues|Message-Queues]] · [[mapreduce|MapReduce]] · [[event-driven-architecture|Event-Driven-Architecture]] · [[circuit-breaker-pattern|Circuit-Breaker-Pattern]] · [[conways-law|Conway's-Law]] · [[agile-standups|Agile-Standups]] · [[principle-of-least-privilege|Principle-of-Least-Privilege]] · [[cognitive-load|Cognitive-Load]] · [[expertise-theory|Expertise-Theory]] · [[working-memory|Working-Memory]] · [[claude-code-basics|Claude-Code-Basics]] · [[claude.md-files|CLAUDE.md-Files]] · [[prompt-engineering-fundamentals|Prompt-Engineering-Fundamentals]] · [[yaml-syntax|YAML-Syntax]] · [[mcp-servers|MCP-Servers]] · [[custom-commands|Custom-Commands]] · [[skills-system|Skills-System]] · [[output-styles|Output-Styles]] · [[hooks-system|Hooks-System]] · [[agent-file-format-specification|Agent-File-Format-Specification]] · [[coordination-pattern-library|Coordination-Pattern-Library]] · [[tool-permission-grammar|Tool-Permission-Grammar]] · [[state-management-protocols|State-Management-Protocols]] · [[agent-prompt-engineering|Agent-Prompt-Engineering]] · [[microservices-architecture|Microservices-Architecture]]

## Methodology Notes

> [!methodology-and-sources] **Frontmatter Field Semantics** *(from [[multi-agent-systems-with-claude-code]])*
> **`name`** (required): Identifier for explicit invocation ("Use the code-reviewer agent..."). Should be hyphenated lowercase.
> 
> **`description`** (required): [**Description-Field-Purpose**:: Natural language explanation of when this agent should be invoked; Claude analyzes this field during automatic delegation to match agent capabilities with task requirements.]^verified-stable This is the most critical field for automatic routing. Include terms like "use PROACTIVELY" or "MUST BE USED" to boost auto-activation.
> 
> **`tools`** (optional): [**Tool-Restriction-Pattern**:: Comma-separated list of…

> [!methodology-and-sources] **How Auto-Delegation Works** *(from [[multi-agent-systems-with-claude-code]])*
> 1. **User query analysis**: Extract intent, domain, task type
> 2. **Agent description scan**: Compare query against all agent descriptions
> 3. **Relevance scoring**: Match keywords, trigger phrases, domain alignment
> 4. **Confidence threshold**: Only auto-invoke if match confidence is high
> 5. **Execution**: Invoke agent with query context
> 6. **Result synthesis**: Integrate agent output into response
> 
> **Optimization**: Include terms like "use PROACTIVELY", "MUST BE USED", "automatically invoke when" in descriptions to boost auto-activation likelihood. This is effectively **Tool SEO** for agents.

> [!methodology-and-sources] **Hook Configuration** *(from [[multi-agent-systems-with-claude-code]])*
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

> [!methodology-and-sources] **Task Tool for Parallel Spawning** *(from [[multi-agent-systems-with-claude-code]])*
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
>    - Search codebase for related…

> [!methodology-and-sources] **Agent Workflow with Shared State** *(from [[multi-agent-systems-with-claude-code]])*
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
> 4. **Trigger next agent**: Hook or main agent reads status change, invokes next…

> [!methodology-and-sources] **Hook Configuration Architecture** *(from [[multi-agent-systems-with-claude-code]])*
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
> - Update shared state…

> [!methodology-and-sources] **Model Selection Testing Protocol** *(from [[multi-agent-systems-with-claude-code]])*
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

> [!methodology-and-sources] **What to Put Where** *(from [[multi-agent-systems-with-claude-code]])*
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

> [!methodology-and-sources] **Routing Algorithm** *(from [[multi-agent-systems-with-claude-code]])*
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
>         agent_scores.append((agent,…

> [!methodology-and-sources] **State Update Protocol** *(from [[multi-agent-systems-with-claude-code]])*
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
>     …

---

## Source Attribution

**Extracted from:** [[multi-agent-systems-with-claude-code]]
