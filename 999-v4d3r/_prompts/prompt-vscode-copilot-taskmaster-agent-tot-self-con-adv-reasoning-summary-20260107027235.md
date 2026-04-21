

[Prompt Used:: 
<goal>
I need a prompt for an **Agent in VS Code Copilot**.
This will be an agent with **multiple skills embedded directly into the prompt**. Including various **Tools Use**, and **MCP Servers**.
</goal>
<task>
1. This Agent specializes in Task planning, Task execution, and overall Task preparedness.
- The agent is required to use the skills of **both** planning out Tasks [with expert level efficiency/mastery], and also **MUST** be a master at following those plans.
  - This means being *highly adaptable* to changes or errors.
  - The Agent needs to know how to logically **[1]** Think through a problem, and **[2]** logically and with extreme skill, execute that thought/plan.
    - You will show the Agent exactly how to do these things in the prompt, through the use of **CODE AND PATTERNS** 
2. The Agent will use a **Tree of Thoughts Breadth First Search pattern** for research/investigation before starting the planning phase.
  - NOTE: The Agent is required to take *in depth notes during there research phase*. [These are to be used in the planning phase.] 
  - *The Tree of Thoughts requires proper weights and values for the pruning and continuation of patterns/paths.*
    - I have uploaded to your **PROJECT KNOWLEDGE** a few resources for you to use, to guide you through the implementation of these advanced Techniques.
      - You are *required to study these*, and to use them to implement the Tree of Thought Self Consistency/Complexity into the prompt.
- **NOTE**: You will need to plan this out in a highly meticulous way.
  - This is so that the agent can easily follow a **scaffolded plan/outline** for Tree of Thoughts/Self Consistency/Complexity.
- The Agent **MUST** use *Chain of Thoughts* **ANY WERE** possible, while thinking. [You will need to structure the prompt in a away that best facilitates this.]
  - You **MUST** give plenty of both right and Wrong *CoT examples*, explicitly labeling each so the agent can see how to properly reason and how to not reason.
3. **Include the use of advanced reasoning tag markers/frameworks**. 
  - **!IMPORTANT**: I have uploaded a copy of a **master report** on *Claude THINKING TAGS*, and there use.
    - You **MUST** review this carefully and with a meticulousness and determination to find answers and understanding.
  - Use this as an *exemplar* for this Agents prompt. The Goal: **To elicit reasoning throughout the entirety of the prompt**.
4. The Agent **MUST** always perform the *Tree of Thoughts Search*, for community:
  1. Best practices
  2. Top ideas
  3. Novel use cases
  4. Community Consensus on the topic. [for context]
5. The Agent need to treat me codebase as *KNOWLEDGE AS CODE*. **This is very important**.
</task>]




















>[!claude-thinking]
I'll begin by searching your project knowledge to understand the resources you've provided, then systematically construct this comprehensive agent prompt.
Thought processThis is a complex prompt engineering request. The user wants me to create a comprehensive agent prompt for VS Code Copilot that specializes in task planning and execution, using advanced reasoning techniques including:

Tree of Thoughts with Breadth-First Search for research/investigation
Chain of Thought reasoning throughout
Advanced reasoning tag markers/frameworks
Self-consistency and complexity handling
Knowledge as Code approach to the codebase

Let me first search the project knowledge to understand the resources available, particularly:

The master report on Claude THINKING TAGS
Resources on Tree of Thoughts implementation
Self-consistency and complexity patterns

I need to be very thorough here given the user's depth preferences and the complexity of this request.I'll begin by searching your project knowledge to understand the resources you've provided, then systematically construct this comprehensive agent prompt.6 stepsSearched project for “CoT examples correct wrong reasoning patterns exemplars few-shot demonstrations”9 resultsmaster-yaml-techniques-exemplar.md5 relevant sectionstextfew-shot-learning.md2 relevant sectionstextchain-of-thought.md2 relevant sectionstextContrastive_CoT_Prompting.md2 relevant sectionstext00-overview-architecture.mdtextSKILL.mdtext01-reasoning-techniques-guide.mdtext03-cot-domain-templates.mdtextpromptpatterns.pdf2 relevant sectionsimageThought processThe user wants me to continue building the VS Code Copilot agent prompt. Let me review the transcript to understand what was already accomplished and what remains.
From the compaction summary, I can see:

Extensive research was done on project knowledge resources
Key concepts were extracted from multiple documents including:

Claude Extended Thinking Architecture Report
Tree of Thoughts implementation patterns
Self-Consistency Validation
Chain of Verification (CoVe)
Chain of Thought examples
Domain-Specialized CoT Templates
Hybrid Orchestration Pattern
Prompt Engineering Patterns
Knowledge-as-Code Principles


A comprehensive agent prompt structure was outlined including:

Reasoning Flow (Research → Planning → Execution → Verification)
Thinking Tag Structure with XML
CoT Examples (correct and wrong patterns)
Community Research Protocol
Knowledge-as-Code Treatment



The task was interrupted before the actual prompt was generated. I need to now create the comprehensive VS Code Copilot agent prompt incorporating all these elements.
Let me review more of the transcript to ensure I capture all the details that were planned, then create the full prompt.I'll review the transcript to understand exactly where we left off, then continue building the comprehensive VS Code Copilot agent prompt.4 stepsCheck end of transcript for any partial prompt that was being developedShow working fileThought processNow I have a comprehensive understanding of what was researched. The transcript shows extensive research was done but the actual prompt was not yet created - the conversation was interrupted during the research phase.
Based on the compaction summary and transcript, I now need to create the comprehensive VS Code Copilot agent prompt that incorporates:

Dual Mastery: Task planning AND execution with high adaptability
Tree of Thoughts BFS for research/investigation with note-taking
Claude-style extended thinking tags with XML structure
Chain of Thought with correct/wrong examples throughout
Self-Consistency validation for critical decisions
Chain of Verification (CoVe) for factual claims
Community research protocol for best practices
Knowledge-as-Code treatment of codebase

Let me now create this comprehensive prompt. It needs to be production-ready with scaffolded patterns, explicit examples, and all the advanced reasoning frameworks integrated properly.Now I have a complete picture of the research conducted. The conversation was interrupted before the actual prompt was created. I'll now construct the comprehensive VS Code Copilot Agent prompt incorporating all the researched frameworks and techniques.2 stepsPresented fileThought processNow let me provide a comprehensive summary for the user explaining what was built and how it addresses all their requirements.I've created the TaskMaster Agent v2.0 - a comprehensive VS Code Copilot agent prompt that integrates all the advanced reasoning frameworks from your project knowledge. Here's what's included:













🎯 Architecture Overview
The agent implements a five-phase cognitive pipeline:
RESEARCH (ToT-BFS) → PLAN (CoT) → VALIDATE (Self-Consistency) → EXECUTE (Adaptive) → VERIFY (CoVe)

📦 Components Delivered
1. Extended Thinking Architecture (Section 2)

XML-structured <thinking> blocks modeled after Claude's architecture
Four-layer cognitive state tracking:

Cognitive State Management
Reasoning Chain (CoT)
Metacognitive Checkpoints
Next Actions Planning


Thinking depth calibration (Shallow → Exhaustive)

2. Tree of Thoughts BFS (Section 3)

Complete BFS algorithm with Python implementation
Scoring system with 6 weighted dimensions:

Feasibility (0.25), Efficiency (0.20), Completeness (0.20), Risk (0.15), Novelty (0.10), Community Support (0.10)


Dynamic pruning thresholds that increase with depth
Mandatory research note-taking with categories:

Best Practices, Top Ideas, Novel Approaches, Community Consensus, Anti-Patterns



3. Chain of Thought with Examples (Section 4)

Universal CoT template (UNDERSTAND → GATHER → STRATEGIZE → EXECUTE → VERIFY)
Three fully worked examples with both ✅ CORRECT and ❌ WRONG reasoning:

Debugging a function
Choosing a data structure
API design decision (REST vs GraphQL)


Domain-specific templates (Technical CoT, Analytical CoT)

4. Self-Consistency Validation (Section 5)

Multi-path validation protocol (3-5 independent reasoning paths)
Consensus analysis with confidence scoring
Guidance on when to apply (simple → high-stakes)
Complete worked example (async vs threading decision)

5. Chain of Verification (CoVe) (Section 6)

Four-step protocol: Baseline → Plan → Execute (independent) → Final
Emphasis on independent verification to prevent confirmation bias
Worked example with Python GIL explanation showing error correction

6. Knowledge-as-Code (Section 7)

Four-layer knowledge extraction framework:

Structural (modules, classes, functions)
Semantic (domain concepts, data flows, patterns)
Evolutionary (change history, technical debt)
Operational (configuration, error handling, performance)


Code understanding protocol (must execute before any modification)
Tests-as-specification pattern

7. Community Research Protocol (Section 8)

Systematic exploration of: official docs, GitHub repos, StackOverflow, blogs
Quality signals matrix (stars, recency, source authority)
Synthesis template for best practices → recommendations

8. Adaptive Execution (Section 9)

Complete AdaptiveExecutor class implementation
Error handling decision tree (RETRY → FIX → SKIP → REPLAN → ABORT)
Reflexion pattern for learning from failures
Execution monitoring template

9. Tools & MCP Integration (Section 10)

Tool category taxonomy (file ops, code analysis, terminal, search, MCP servers)
Tool selection protocol with safety checks
Safe file modification protocol

10. Complete Workflow Integration (Section 11)

Master workflow diagram showing all phases
State machine implementation
Quick reference matrix for when to use each component


🔑 Key Features
RequirementImplementationDual Mastery (Planning + Execution)Complete pipeline with dedicated planning (CoT) and execution (Adaptive) phasesToT-BFS for ResearchFull BFS algorithm with scoring, pruning, and mandatory note-takingAdvanced Reasoning TagsClaude-style XML <thinking> blocks with cognitive state trackingCoT EverywhereIntegrated throughout with explicit correct/wrong examplesCommunity ResearchDedicated protocol for best practices, novel approaches, consensusKnowledge-as-CodeFour-layer semantic codebase understanding frameworkError HandlingAdaptive execution with Reflexion loops for learning from failuresSelf-ConsistencyMulti-path validation for critical decisionsChain of VerificationIndependent fact-checking to reduce hallucinations

📊 Prompt Statistics

Total Length: ~3,500 lines
Sections: 12 major sections
Code Examples: 15+ complete implementations
CoT Examples: 6 (3 correct, 3 wrong patterns)
Templates: 20+ reusable XML templates

