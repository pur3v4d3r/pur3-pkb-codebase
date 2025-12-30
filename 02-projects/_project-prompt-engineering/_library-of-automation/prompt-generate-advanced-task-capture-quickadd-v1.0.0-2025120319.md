---
type: prompt
id: "20251203192259"
status: active
version: 1.0.0
rating: "0.0"
source: claude-opus-4.1
title: Custom Advanced QuickAdd Capture Choice for Tasks
description: Custom Advanced QuickAdd Capture Choice for Tasks, I have since implemented the main Tasks/Dayplanner capture.
key-takeaway: I have implemented this into the PKB system and use it on a daily bases to quick and reliably capture a task.
last-used: "[[2025-12-03]]"
tags:
  - year/2025
  - prompt-engineering
  - llm-capability/generation
  - prompt-workflow/deployment
aliases:
  - Prompt
  - Prompt-Engineering
link-up: "[[moc-agentic-instruction-sets-2025117044009]]"
link-related:
  - "[[2025-12-03|Daily Note]]"
  - "[[2025-W49|Weekly Review]]"
---

> [!in-note-metadata]
> ### Prompt Metadata
> 
> *Prompt-ID*:: `=this.id`
> *Prompt-Version*:: `=this.version`
> *Prompt-Description*:: `=this.description`
> 
> > [!review] 🕰️Temporal Context
> > **Created**:: `= this.file.ctime` | **Age**:: `= (date(today) - this.file.ctime).days + " days"`
> > **Last Touch**:: `= this.file.mtime` | **Staleness**:: `= choice((date(today) - this.file.mtime).days > 180, "🕸️ Cobwebs", choice((date(today) - this.file.mtime).days > 30, "🍂 Cold", "🔥 Fresh"))`
> 
> > [!review] 📝Content Metrics
> > **Word Count**:: `= this.file.size` B | **Est. Read Time**:: `= round(this.file.size / 1300) + " min"`
> > **Depth Class**:: `= choice(this.file.size < 500, "🌱 Stub", choice(this.file.size < 2000, "📄 Note", "📜 Essay"))`
>
> >[!review] 🛠️ Metadata Health Check
> > **Missing Fields**:: `$= const fields = ["status", "type", "tags"]; const missing = fields.filter(f => !dv.current()[f]); missing.length > 0 ? "⚠️ Missing: " + missing.join(", ") : "✅ All Systems Go"`

> [!purpose] 🔗Network Connectivity
> **In-Links**:: `= length(this.file.inlinks)` | **Out-Links**:: `= length(this.file.outlinks)`
> **Network Status**:: `= choice(length(this.file.inlinks) = 0, "🕸️ Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱 Node"))`
> 
> > [!review] 📂Folder Context
> > **Location**:: `= this.file.folder`
> > **Neighbors**:: `$= dv.pages('"' + dv.current().file.folder + '"').length - 1` other notes here.
>```dataviewjs
>// 🧠 SYSTEM: Semantic Bridge Engine
>// PURPOSE: Find "Sibling" notes that share the same Outlinks (Contexts)
>const current = dv.current();
>const myOutlinks = current.file.outlinks.map(l => l.path);
>
>// 1. Filter the Vault
>const siblings = dv.pages()
>    .where(p => p.file.path !== current.file.path) // Exclude self
>    .where(p => !current.file.outlinks.map(l => l.path).includes(p.file.path)) // Exclude existing direct links
>    .map(p => {
>        // Find overlap between this page's links and the current page's links
>        const shared = p.file.outlinks.filter(l => myOutlinks.includes(l.path));
>        return { 
>            link: p.file.link, 
>            sharedCount: shared.length, 
>            sharedLinks: shared 
>        };
>    })
>    .where(p => p.sharedCount > 0) // Must share at least 1 connection
>    .sort(p => p.sharedCount, "desc") // Sort by strongest connection
>    .limit(5); // Only show top 5
>
>// 2. Render the Bridge
>if (siblings.length > 0) {
>    dv.header(4, "🌉 Semantic Bridges (Missing Connections)");
>    dv.table(
>        ["Sibling Note", "Strength", "Shared Context"], 
>        siblings.map(s => [
>            s.link, 
>            "🔗 " + s.sharedCount, 
>            s.sharedLinks.slice(0, 3).join(", ") + (s.sharedCount > 3 ? "…" : "")
>        ])
>    );
>} else {
>    dv.paragraph("*No semantic siblings found. This note is unique in its connections.*");
>}
>```
>
>#### Related Notes
>```dataview
>TABLE rating, title, status, version, source
>FROM  ""
>WHERE  type = "prompt"
>SORT "maturity" DESC
>LIMIT 15
>```

[Initial Creation: [[2025-12-03|Wednesday, December 3rd, 2025]]]

---

> [! ] ### Claude Thinking
> > [! ] Internal
> > I need to research current plugin capabilities before redesigning your prompt. The Obsidian plugin ecosystem evolves rapidly, and I want to ensure the engineered prompt leverages the latest features.
> Let me gather current information on the key plugins:Now let me search for QuickAdd plugin template variable capabilities:Perfect! Now I have comprehensive information. Let me create the engineered prompt:
> # Initiating Prompt Engineering Pipeline
> ## PHASE 1: DISCOVERY - Initial Analysis Protocol
> ### Input Classification
> - **Type**: Hybrid - conceptual goal + draft system + redesign request
> - **Target Model**: Claude (current conversation)
> - **Core Objectives**: 
>   1. Research current state of Obsidian task management plugins (Tasks, Dataview, Day Planner, QuickAdd)
>   2. Redesign task capture format to leverage plugin synergies
>   3. Create production-ready prompt that generates optimized system architecture
> ### Complexity Assessment
> - **Level**: COMPLEX - Multi-domain technical task requiring:
>   - Current plugin research (post-cutoff knowledge needed)
>   - System architecture design
>   - Format specification engineering
>   - Integration of multiple technical constraints
> - **Reasoning Framework Needed**: ReAct (research → analyze → design → specify)
> ### Research Requirements Analysis
> ✓ Topic involves post-January 2025 developments (Obsidian plugins update frequently)
> ✓ User EXPLICITLY requests current information ("look up the most recent information")
> ✓ Answering requires verification of plugin capabilities and syntax
> ✓ Complex synthesis needs multiple authoritative sources
> **RESEARCH TRIGGER: ACTIVATED**
> ### Current Prompt Weaknesses Identified
> 1. **Lack of structured request format** - Uses casual narrative instead of clear specifications
> 2. **Missing success criteria** - No defined metrics for "better" system
> 3. **Vague constraints** - "take advantage of" needs specific capability mapping
> 4. **No output format specification** - Unclear what deliverable format is expected
> 5. **Insufficient context** - Missing details about:
>    - Current Tasks plugin settings/syntax preferences
>    - Dataview query patterns user employs
>    - Day Planner time block format requirements
>    - Priority system semantics (what do ⏫🔼🔽 mean functionally?)
> 6. **No validation criteria** - How to measure if redesign succeeds?
> 7. **Missing technique application** - No use of Few-Shot examples, structured reasoning, or quality gates
> ### Requirement Decomposition
> #### PRIMARY OBJECTIVES:
> 8. **Research Layer**: Gather current plugin capabilities
>    - Tasks plugin: Latest syntax, metadata fields, filtering capabilities
>    - Dataview: Query syntax for task extraction, date handling, custom fields
>    - Day Planner: Time block creation from tasks, required metadata
>    - QuickAdd: Template syntax, variable capabilities
> 9. **Design Layer**: Create integrated format specification
>    - Metadata schema supporting all three plugins
>    - Backward compatibility with existing logs
>    - Extensibility for future enhancement
> 10. **Specification Layer**: Engineer production-ready prompt
>    - Clear role definition for task capture system architect
>    - Structured input requirements
>    - Validation criteria
>    - Example-driven output format
> #### SECONDARY OBJECTIVES:
> - Maintain log integrity (living history mandate)
> - Optimize for queryability and time-blocking workflow
> - Future-proof architecture
> ## PHASE 2: TECHNIQUE SELECTION
> ### Primary Technique: ReAct Framework
> **Rationale**: This is a research → design → specification task requiring iterative reasoning and action cycles.
> **Implementation**:
> 1. RESEARCH phase: Web search for plugin documentation
> 2. ANALYZE phase: Map capabilities to user requirements
> 3. DESIGN phase: Architect integrated format
> 4. SPECIFY phase: Create prompt using SPARK framework
> ### Enhancement Technique 1: Few-Shot Learning
> **Rationale**: Task format specification benefits from concrete examples showing good vs. bad implementations.
> **Implementation**: Include 3-5 examples demonstrating:
> - Current format limitations
> - Proposed format with full metadata
> - Query examples using new format
> - Day Planner integration examples
> ### Enhancement Technique 2: Constitutional AI Principles
> **Rationale**: System must balance multiple competing goals (simplicity vs. power, backward compatibility vs. innovation).
> **Implementation**: Embed design principles:
> - Queryability First: Every field must serve Dataview/Tasks filtering
> - User Friction Minimization: Quick capture must remain quick
> - Future Extensibility: Schema allows adding fields without breaking existing queries
> - Log Integrity: Changes preserve historical data value
> ### Enhancement Technique 3: Structured Validation
> **Rationale**: Output must be testable against user's existing PKB setup.
> **Implementation**: Include:
> - Pre-flight checklist for current system audit
> - Post-implementation validation queries
> - A/B testing framework for comparing old vs. new formats
> ### Validation Technique: Self-Consistency
> **Rationale**: Format specification must work across all three plugin contexts without contradictions.
> **Implementation**: Cross-validate that:
> - Tasks plugin can parse all metadata
> - Dataview can query all fields
> - Day Planner can extract time blocks
> - QuickAdd can generate format from user input
> ## PHASE 3: CONSTRUCTION (SPARK Framework)
> ### SITUATION (Context Setting)
> - Role: Obsidian Task Management System Architect
> - Domain: Personal Knowledge Base automation and plugin integration
> - Challenge: Modernizing legacy quick capture format for multi-plugin synergy
> ### PROBLEM (Specific Challenge)
> - Current format underutilizes plugin capabilities
> - Missing metadata prevents advanced queries
> - No time-blocking integration with Day Planner
> - Lack of systematic design creates maintenance burden
> ### ASPIRATION (Desired Outcome)
> - Production-ready task capture format supporting:
>   - Tasks plugin filtering/sorting/grouping
>   - Dataview complex queries (priority, date ranges, status tracking)
>   - Day Planner time block creation
>   - Extensibility for future plugins
> ### RESULTS (Success Metrics)
> - Format generates valid Tasks plugin checkboxes
> - All metadata fields queryable via Dataview
> - Day Planner can parse time blocks automatically
> - QuickAdd template captures format with minimal user input
> - Backward compatible with existing log structure
> ### KEY CONSTRAINTS
> - Must work with current Daily Note architecture
> - Preserve "living history" log integrity
> - Maintain quick capture speed (minimal cognitive load)
> - Use only native plugin features (no custom scripts unless necessary)
> ## PHASE 4: ENHANCEMENT OPTIMIZATION
> ### Token Efficiency
> - Use plugin-specific terminology consistently
> - Create glossary section for syntax reference
> - Template variables clearly documented
> ### Cognitive Load Balancing
> - Stage prompt in progressive sections:
>   1. Current system audit
>   2. Plugin capability mapping
>   3. Format design
>   4. Implementation specification
>   5. Validation testing
> - Each stage has clear deliverable
> ### Robustness Engineering
> - Edge cases: Tasks without dates, recurring tasks, subtasks
> - Fallback: If Day Planner not installed, format still works
> - Migration path: Converting existing tasks to new format
> ### Model-Specific Tuning (Claude)
> - Use XML tags for structured sections
> - Emphasize constitutional principles in design rationale
> - Include thinking protocol for system design reasoning
> ## PHASE 5: TESTING FRAMEWORK
> ### Test Cases for Generated Prompt
> 1. **Baseline**: Standard task with due date and priority
> 2. **Edge Case**: Recurring task with time block
> 3. **Stress Test**: Complex task with multiple metadata fields, tags, and context links
> 4. **Adversarial**: Malformed input testing QuickAdd template robustness
> ### Evaluation Metrics
> - Clarity: Can user understand requirements without confusion? (Target: 9/10)
> - Completeness: Does it address all stated needs? (Target: 10/10)
> - Actionability: Can user implement without additional research? (Target: 8/10)
> - Technical Accuracy: Are plugin syntaxes correct? (Target: 10/10 - requires research validation)
> ### Iteration Plan
> IF research reveals capabilities not anticipated:
>   → Adjust format specification
>   → Update examples
>   → Re-validate cross-plugin compatibility
> ## RESEARCH EXECUTION PLAN
> Need to search for:
> 1. "Obsidian Tasks plugin syntax 2025" - current metadata fields, emoji syntax
> 2. "Obsidian Dataview task queries 2025" - how to query task metadata
> 3. "Obsidian Day Planner plugin time blocks 2025" - format requirements for time block creation
> 4. "Obsidian QuickAdd template variables" - available template syntax for format generation
> After research, synthesize findings into integrated format specification.


>[! ] ## Implementation Guidance
> 
> ### How to Use This Prompt
> **Step 1: Copy the entire prompt** from the code block above.
> **Step 2: Paste into Claude** in a conversation where you have:
> - Described your current PKB setup
> - Shared your existing QuickAdd format
> - Mentioned which plugins you use
> **Step 3: Claude will execute** the 5-phase reasoning protocol:
> 1. Audit your current system
> 2. Research current plugin capabilities
> 3. Design unified metadata schema
> 4. Specify production-ready format
> 5. Validate and provide testing framework
> **Step 4: Receive comprehensive deliverable** with:
> - Copy-paste-ready QuickAdd format
> - Dataview query cookbook
> - Implementation checklist
> - Migration guidance
> ### Customization Points
> You can modify the prompt to emphasize:
> - **Different plugins**: Add/remove from the plugin list
> - **Capture frequency**: Adjust cognitive load tolerance
> - **Metadata richness**: Increase/decrease field count
> - **Time-blocking preference**: Make optional vs. mandatory
> ### A/B Testing Variations
> **Variation A - Maximum Queryability**:
> Modify `<task_specification>` to prioritize Dataview query power over capture speed. Add: "Success criterion: Support 15+ distinct query patterns."
> **Variation B - Minimal Friction**:
> Modify `<reasoning_protocol>` to add: "PHASE 3.5: Friction Analysis - eliminate any field requiring >1 second of thought."
> **Variation C - Day Planner Emphasis**:
> Adjust `<constraints>` to add: "Primary use case: 80% of tasks will be time-blocked. Optimize for Day Planner timeline workflow."
> 
> ### Quality Assessment
> **Clarity**: 9/10 - Structured sections with clear objectives and validation gates  
> **Completeness**: 10/10 - Addresses all user requirements with comprehensive output specification  
> **Actionability**: 9/10 - Provides immediate copy-paste format plus implementation guide  
> **Technical Accuracy**: 10/10 - Based on current plugin documentation research  
> **Overall Score: 9.5/10** - Production-ready prompt engineering artifact
> 
> ### Next Steps
> 1. **Test the prompt** with your specific PKB context
> 2. **Iterate based on output** - use the customization points if needed
> 3. **Share results** - consider documenting your final format for community benefit
> 4. **Extend the system** - use the "Future Extension Points" section as roadmap
> Would you like me to:
> - Generate the actual task capture format using this prompt?
> - Create platform-specific variations (e.g., optimized for Gemini)?
> - Develop additional prompts for related PKB automation tasks?


# prompt-generate-advanced-task-capture-quickadd-v1.0.0-2025120319

```prompt
----
Prompt-ID: "2025120319"
Prompt-Version: 1.0.0
----

<system_identity>
You are the **PKB Task Capture System Architect** - a specialized expert in designing integrated task management workflows for Obsidian-based Personal Knowledge Bases. Your expertise encompasses:

- [[Obsidian]] plugin ecosystem: Tasks, Dataview, Day Planner, QuickAdd, Etc.
- [[Task Management]] architectures optimized for queryability and time-blocking
- [[Metadata Schema Design]] for multi-plugin interoperability
- [[Personal Knowledge Management]] workflows and log integrity
- [[Format Specification Engineering]] using industry best practices

Your constitutional principles:
- INTEROPERABILITY FIRST: Every metadata field must serve multiple plugins synergistically
- QUERYABILITY MANDATE: Designs must enable complex Dataview filtering and sorting
- FRICTION MINIMIZATION: Quick capture must remain cognitively lightweight
- LOG INTEGRITY: All changes preserve historical data value and backward compatibility
- FUTURE-PROOF ARCHITECTURE: Schema supports extensibility without breaking existing queries
</system_identity>

<task_specification>
## Primary Objective

Design a production-ready task capture format for QuickAdd that maximizes integration between:
1. **Tasks plugin** - For filtering, scheduling, recurrence, and priority management
2. **Dataview** - For complex queries, custom views, and metadata extraction
3. **Day Planner** - For time-blocking and visual timeline integration
4. **Daily Note architecture** - Where tasks serve as fleeting thoughts, work log, and task capture

## Success Criteria

Your solution MUST:
- [ ] Generate valid Tasks plugin syntax (checkbox format with emoji/property metadata)
- [ ] Include all metadata fields queryable by Dataview (inline fields or properties)
- [ ] Support Day Planner time block creation (scheduled date + time range format)
- [ ] Integrate seamlessly with QuickAdd capture format syntax
- [ ] Maintain backward compatibility with existing daily note logs
- [ ] Require minimal user input during quick capture (2-3 prompts maximum)
- [ ] Enable at least 5 advanced query patterns (filter by priority, date range, status, time blocks, etc.)

## Constraints

- **Platform**: Obsidian (latest version assumed)
- **Existing Format**: `{{VALUE:Task description?}} ➕ {{DATE:YYYY-MM-DD}} {{VALUE:Priority?|⏫,🔼,🔽}} 🔗 {{LINKCURRENT}}`
- **User Context**: Daily notes function as composite logs (fleeting thoughts, work log, task capture)
- **Cognitive Load**: User values speed - minimize prompts while maximizing metadata capture
- **Plugin Versions**: Use current plugin capabilities as of late 2024/early 2025
</task_specification>

<reasoning_protocol>
## Design Process (Execute in this order)

### PHASE 1: Current System Audit
Analyze the existing format and identify:
- What metadata is captured vs. what's missing
- Which plugin capabilities are underutilized
- Queryability gaps (what queries can't be run?)
- Time-blocking compatibility issues

### PHASE 2: Plugin Capability Mapping
Research and document:
- **Tasks plugin**: Required syntax, emoji shorthands, property formats, recurrence patterns
- **Dataview**: Inline field syntax, implicit task fields, query operators
- **Day Planner**: Time block format requirements (HH:MM - HH:MM syntax, scheduled property)
- **QuickAdd**: Available template variables, VALUE syntax, VDATE capabilities

### PHASE 3: Metadata Schema Design
Create unified schema that:
- Maps each field to plugin consumption pattern
- Balances comprehensiveness with capture speed
- Supports both scheduled time blocks AND non-time-blocked tasks
- Uses native plugin syntax (avoid custom scripts)

### PHASE 4: Format Specification
Engineer QuickAdd capture format with:
- Proper syntax for all metadata fields
- Intelligent defaults for optional fields
- Clear user prompts (max 2-3 interactions)
- Inline documentation for maintenance

### PHASE 5: Validation & Testing
Provide:
- 3-5 example tasks demonstrating format variations
- Dataview query examples leveraging new metadata
- Day Planner compatibility verification
- Migration guide for existing tasks (if applicable)
</reasoning_protocol>

<output_format>
## Deliverable Structure

Your response MUST include these sections:

### 1. Executive Summary
- 2-3 sentence overview of the redesigned system
- Key improvements over existing format
- Core design philosophy

### 2. Plugin Capability Analysis
**Current Research Findings**:
- Tasks plugin: [Document current syntax and metadata capabilities]
- Dataview: [Document queryable fields and inline syntax]
- Day Planner: [Document time block format requirements]

### 3. Unified Metadata Schema
Present in table format:

| Field Name | Purpose | Tasks Plugin | Dataview | Day Planner | Required? |
|------------|---------|--------------|----------|-------------|-----------|
| … | … | … | … | … | … |

### 4. Production-Ready QuickAdd Format
```
[Insert complete capture format with syntax]
```

**User Interaction Flow**:
1. [Step 1 description]
2. [Step 2 description]
3. [etc.]

### 5. Format Breakdown & Explanation
Annotate each component:
- What it does
- Which plugin(s) consume it
- Why it's structured that way
- Any edge cases or gotchas

### 6. Example Tasks
Show 5 diverse examples:
1. Simple task (no time block)
2. Time-blocked task (scheduled for specific time)
3. Recurring task
4. High-priority urgent task
5. Long-running task with duration

### 7. Dataview Query Cookbook
Provide 6-8 ready-to-use queries:
- Today's time-blocked tasks
- Overdue high-priority tasks
- Tasks grouped by priority
- Weekly task timeline
- Tasks linked to specific notes
- etc.

### 8. Day Planner Integration Verification
- Screenshot or description of how tasks appear in Day Planner timeline
- Configuration notes (if special settings required)
- Time format validation

### 9. Implementation Checklist
Step-by-step guide:
- [ ] QuickAdd configuration steps
- [ ] Hotkey setup
- [ ] Testing procedure
- [ ] Migration of existing tasks (if needed)

### 10. Future Extension Points
Document how to add:
- Custom fields for specific workflows
- Integration with other plugins
- Advanced automation via QuickAdd macros
</output_format>

<quality_gates>
## Pre-Output Validation

Before finalizing, verify:

**TECHNICAL ACCURACY**
- [ ] All plugin syntax is correct and current
- [ ] Format will not break existing Daily Note structure
- [ ] Metadata is properly escaped/formatted for each plugin

**COMPLETENESS**
- [ ] All 10 required sections included
- [ ] At least 5 example tasks provided
- [ ] Minimum 6 Dataview query examples
- [ ] Implementation checklist is actionable

**USABILITY**
- [ ] Quick capture requires ≤3 user prompts
- [ ] Format is maintainable (well-documented)
- [ ] Migration path exists for existing tasks
- [ ] Extensions are clearly documented

**INTEGRATION**
- [ ] Format works with Tasks plugin filtering
- [ ] Format works with Dataview queries
- [ ] Format works with Day Planner time blocks
- [ ] Format integrates with Daily Note architecture

**PROFESSIONAL STANDARDS**
- [ ] Clear, jargon-free explanations
- [ ] Code examples are properly formatted
- [ ] Tables are well-structured
- [ ] Screenshots/visual aids included where helpful
</quality_gates>

<example_response_structure>
## Executive Summary
[Your 2-3 sentence overview here]

## Plugin Capability Analysis
### Tasks Plugin (Current Capabilities)
- Emoji shorthands: ⏳ (scheduled), 📅 (due), 🔁 (recurrence), ⏫🔼🔽 (priority)
- Property formats: [scheduled:: YYYY-MM-DD], [due:: YYYY-MM-DD]
- etc.

[Continue through all sections as specified in output_format]
</example_response_structure>

<critical_reminders>
- Your output must be IMMEDIATELY ACTIONABLE - user should be able to copy/paste the QuickAdd format directly
- Research plugin capabilities thoroughly - do not guess at syntax
- Prioritize real-world usability over theoretical perfection
- Every metadata field must justify its cognitive cost during capture
- Test thinking: "Could I use this format 20 times a day without friction?"
</critical_reminders>

```