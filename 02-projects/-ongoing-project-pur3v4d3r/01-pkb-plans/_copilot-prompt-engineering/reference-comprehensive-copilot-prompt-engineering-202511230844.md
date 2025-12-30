---
aliases:
  - Obsidian Copilot Prompts
  - Copilot Prompt Design
tags:
  - year/2025
  - conceptual-learning
  - context/applied
  - obsidian/plugins/copilot
  - obsidian
  - prompt-engineering
  - 
source: claude-sonnet-4.5
id: "20251123084536"
created: 2025-11-23T08:45:36
modified: 2025-11-23T08:45:36
week: "[[2025-W47]]"
month: "[[2025-11]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: reference
maturity: needs-review
confidence: established
next-review: 2025-11-30
review-count: 0
link-count: 0
backlink-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-11-23|Daily-Note]]"
---

# Copilot Prompting



---

aliases: [Copilot Prompting, Obsidian Copilot Prompts, Copilot PE, Copilot Prompt Design]
---

> [!comprehensive-reference] 📚Comprehensive-Reference
> - **Generated**:: 2025-11-23
> - **Version**:: 1.0
> - **Type**:: Reference Documentation (Prompt Engineering in Obsidian Copilot)
> - **Scope**:: Complete guide to designing, implementing, and optimizing prompts within the Copilot for Obsidian plugin ecosystem

> [!abstract]
> **Executive Overview**
> Copilot for Obsidian is an in-vault AI assistant that provides chat-based interfaces, vault search capabilities, and powerful context processing within Obsidian's workspace. This reference note comprehensively documents [[Prompt Engineering]] techniques specific to the [[Copilot Plugin]], covering system prompt architecture, custom prompt design, placeholder templating, [[RAG]] (Retrieval-Augmented Generation) optimization, and advanced prompt patterns for knowledge work within [[03-notes/01_permanent-notes/02_personal-knowledge-base/Personal Knowledge Management]] systems.

> [!how-to-use-this]
> **Navigation Guide**
> This reference note is organized into 9 major sections covering all aspects of prompt engineering with Obsidian Copilot. Use the table of contents below for quick navigation to specific techniques, or search for specific placeholders and patterns using [[Wiki-Links]]. Each section includes practical examples, implementation code, and best practices derived from community documentation and development insights.

## 📑 Table of Contents

1. [[#🎯 Copilot Plugin Architecture & Modes]]
2. [[#⚙️ System Prompt Engineering Fundamentals]]
3. [[#🧩 Custom Prompts - Design & Implementation]]
4. [[#🔤 Placeholder System & Variable Templating]]
5. [[#🧠 Vault QA & RAG Prompt Optimization]]
6. [[#🎨 Advanced Prompt Patterns & Techniques]]
7. [[#🔧 Prompt Configuration & Properties]]
8. [[#📊 Performance Optimization & Token Management]]
9. [[#🚀 Copilot Plus & Agentic Prompt Engineering]]

---

## 🎯 Copilot Plugin Architecture & Modes

> [!definition]
> - **Copilot for Obsidian**:: An open-source LLM interface that operates directly within Obsidian, providing chat UI with support for multiple models, custom prompts, and vault-wide question answering with local indexing for privacy-focused knowledge management.
> - **Operation Modes**:: Three distinct interaction paradigms—Chat Mode, Vault QA Mode, and Copilot Plus (premium)—each optimized for different prompt engineering strategies and use cases.

### Foundational Architecture

Copilot for Obsidian operates as an in-vault AI assistant with chat-based vault search, web and YouTube support, powerful context processing, and expanding agentic capabilities while keeping user data under local control. The plugin's architecture centers around **model-agnostic prompting**, meaning prompt engineering techniques must account for differences between [[OpenAI]], [[Anthropic]], [[Google Gemini]], [[Cohere]], and local models via [[Ollama]] or [[LM Studio]].

The core architectural components that influence prompt design include:

1. **Context Window Management**: Conversation turns (consisting of 2 messages - user input and AI response) are configurable, with more turns providing better context but using more tokens and potentially costing more.

2. **Local Indexing System**: All QA modes leverage retrieval augmentation with a local index, ensuring data isn't sent to a cloud-based vector search service, with notes always stored on the user's own device.

3. **Model Selection Framework**: Users can select preferred chat models in Model Settings to tailor plugin behavior, including models specialized for vision and reasoning tasks that enable advanced capabilities like image understanding and complex logical reasoning.

> [!key-claim]
> **Privacy-First Architecture**
> The fundamental design principle of Copilot is **data sovereignty**—the plugin is building toward a portable agentic experience with no provider lock-in, where data is always yours, you use whatever LLM you like, and commands/tools are defined over time as markdown files in your vault.

### Mode-Specific Prompt Considerations

| Mode | Primary Use Case | Prompt Strategy | Context Handling |
|------|------------------|-----------------|------------------|
| **Chat Mode** | General inquiries, explanations, or assistance that may not require searching through vault | Conversational, iterative refinement | Manual note referencing via `[[note]]` |
| **Vault QA (Basic)** | Plain language questions with answers from all notes using RAG, combining searching notes with AI responses | Query-focused, retrieval-optimized | Automatic semantic search + context injection |
| **Copilot Plus** | Advanced AI tools including @vault for enhanced vault functions, @youtube for video insights, @websearch for real-time information, and @composer for direct note editing | Tool-augmented, agentic workflows | Multi-modal context (markdown, PDF, images, URLs) |

> [!analogy]
> **Three Cognitive Modes**
> Think of Copilot's modes as three different "thinking styles":
> - **Chat Mode** = Direct conversation (like talking to a colleague)
> - **Vault QA** = Research librarian (finds relevant information first, then responds)
> - **Copilot Plus** = Executive assistant (uses tools autonomously to accomplish tasks)
> 
> Each mode requires different prompt engineering approaches because the underlying cognitive process differs.

### Technical Implementation: Fill-in-the-Middle Prompting

Copilot uses clever prompt engineering to force autoregressive transformer models to take text before and after the cursor into account by formatting input as `<text_before_cursor> <mask/> <text_after_cursor>`, with the model's task being to respond with the most logical words that can replace the `<mask/>`.

The system prompt architecture for auto-completion involves:

```markdown
Your job is to predict the most logical text that should be written at the location of the <mask/>.

THOUGHT: [Model reasons about context]
ANSWER: [Actual completion text]
```

> [!example]
> **Chain-of-Thought Auto-Completion**
> The text after THOUGHT: allows the model to reason about the context around the cursor before writing the answer in the ANSWER: section, a prompt engineering trick called Chain-of-Thought where explaining reasoning makes the model more likely to write a coherent answer by giving the attention mechanism more guidance.

---

## ⚙️ System Prompt Engineering Fundamentals

> [!definition]
> - **System Prompt**:: The foundational instruction set that defines the AI's behavior, capabilities, constraints, and output format across all interactions within a given context.
> - **Few-Shot Learning in Copilot**:: A customizable approach where users can edit existing few-shot examples or add their own via settings menu, allowing users to write example inputs and model responses for given contexts so the model learns to generate completions in their specific style.

### System Prompt Design Principles

Users can use their own system prompt and choose between different embedding providers for Vault QA. Effective system prompts for Copilot follow these architectural principles:

1. **Role Definition**: Clearly establish the AI's identity and expertise domain
2. **Output Format Specification**: Define structure, tone, and formatting expectations
3. **Constraint Declaration**: Set boundaries on behavior, content types, and scope
4. **Context Awareness**: Acknowledge the [[obsidian]] environment and [[Zettelkasten]] methodology

> [!methodology-and-sources]
> **System Prompt Template Structure**
> 
> ```markdown
> # Role & Identity
> You are [specific role] with expertise in [domain].
> 
> # Core Capabilities
> - Capability 1: [Description]
> - Capability 2: [Description]
> 
> # Output Format
> [Specify structure, use of headers, callouts, wiki-links, etc.]
> 
> # Constraints
> - Constraint 1: [Limitation]
> - Constraint 2: [Boundary]
> 
> # Context Awareness
> You are operating within an Obsidian vault structured using [methodology].
> Notes follow [naming convention]. Links use [[wiki-link]] format.
> ```

### Few-Shot Example Engineering

Few-shot examples allow reduction of prompt length, complexity, and inference costs while enabling users to customize the type of completions they expect—for instance, having the model write in their native language or generate to-do list tasks in their specific style.

**Effective Few-Shot Pattern**:

```markdown
## Example 1: [Context Type]
**Input Context:**
[Text before cursor]
<mask/>
[Text after cursor]

**Expected Output:**
[Desired completion]

## Example 2: [Different Context Type]
**Input Context:**
[Different scenario]
<mask/>
[Context]

**Expected Output:**
[Appropriate completion for this context]
```

> [!helpful-tip]
> **Style Transfer via Few-Shot**
> To train Copilot to match your writing style:
> 1. Identify 3-5 representative examples of your writing
> 2. Create few-shot examples showing input context + your typical response
> 3. Vary the contexts (explanatory, analytical, creative, technical)
> 4. The model will learn your patterns and reproduce them in new contexts

---

## 🧩 Custom Prompts - Design & Implementation

> [!definition]
> - **Custom Prompts**:: User-defined instructions or queries that can be saved and reused within Copilot, which can include placeholders for selected text, specific notes, or entire folders, making them highly versatile.
> - **Prompt Library**:: Custom prompts are stored locally in the Obsidian vault as markdown files in the `copilot-custom-prompts` folder and can be triggered with a simple `/` command in the chat input.

### Creating Custom Prompts

To create custom prompts, users open the Command Palette in Obsidian (Cmd/Ctrl + P), search for and select "Copilot: Add custom prompt", provide a unique name title and the actual prompt content.

**Two Approaches to Custom Prompts**:

1. **Persistent Custom Prompts**: Saved to vault, reusable across sessions
2. **Ad-hoc Custom Prompts**: Created by selecting "Copilot: Apply ad-hoc custom prompt" from Command Palette, entering the prompt in a modal, and pressing Enter to apply immediately without saving.

> [!methodology-and-sources]
> **Custom Prompt Creation Workflow**
> 
> **Step 1: Define Purpose & Scope**
> - What specific task will this prompt accomplish?
> - What input variations must it handle?
> - What output format is expected?
> 
> **Step 2: Design Prompt Structure**
> ```markdown
> # [Prompt Title]
> 
> ## Task Description
> [Clear explanation of what the AI should do]
> 
> ## Input Handling
> [How to process {selectedText}, {activeNote}, etc.]
> 
> ## Output Requirements
> [Format, structure, constraints]
> 
> ## Examples (Optional)
> [Sample input → expected output]
> ```
> 
> **Step 3: Implement Placeholders**
> - Use `{selectedText}` for highlighted content
> - Use `{activeNote}` for current file
> - Use `{[[Note Title]]}` for specific notes
> - Use `{#tag1, #tag2}` for tag-filtered notes
> 
> **Step 4: Test & Iterate**
> - Apply to various contexts
> - Refine based on outputs
> - Document edge cases

### Custom Prompt Best Practices

Key best practices include being specific in instructions to get the best results, using placeholders to make prompts dynamic and reusable, and considering creating prompts for common tasks like summarization, comparison, or idea generation.

> [!use-cases-and-examples]
> **Real-World Custom Prompt Applications**
> 
> **1. Zettelkasten Note Generator**
> ```markdown
> Title: "Create Atomic Note"
> 
> Analyze {selectedText} and create an atomic Zettelkasten note:
> 
> # [Concept Name]
> 
> ## Definition
> [Single-sentence definition]
> 
> ## Explanation
> [2-3 paragraphs explaining the concept]
> 
> ## Connections
> - Related to: [[Concept 1]], [[Concept 2]]
> - Contrasts with: [[Concept 3]]
> 
> ## Sources
> - {activeNote}
> 
> ## Tags
> #atomic-note #[domain]
> ```
> 
> **2. Meeting Notes Summarizer**
> ```markdown
> Title: "Structure Meeting Notes"
> 
> Transform {selectedText} into structured meeting notes:
> 
> ## Key Decisions
> - [Decision 1]
> - [Decision 2]
> 
> ## Action Items
> - [ ] Task 1 - @person - Due: date
> - [ ] Task 2 - @person - Due: date
> 
> ## Follow-up Questions
> - [Question 1]
> 
> ## Related Notes
> [[Project Note]] | [[Context Note]]
> ```
> 
> **3. Comparative Analysis Generator**
> ```markdown
> Title: "Compare Concepts"
> 
> Come up with multiple choice questions using {activeNote}, 
> and follow the format of {[[Quiz Template]]} to start a quiz session.
> ```

### Storage & Organization

Commands are automatically loaded from .md files in the custom prompts folder `copilot-custom-prompts`, and modifying the files will also update the command settings.

**Recommended Directory Structure**:

```
vault/
└── copilot-custom-prompts/
    ├── 📝 writing/
    │   ├── summarize-article.md
    │   ├── expand-concept.md
    │   └── simplify-language.md
    ├── 🧠 analysis/
    │   ├── extract-insights.md
    │   ├── compare-notes.md
    │   └── identify-patterns.md
    ├── 🏗️ structure/
    │   ├── create-moc.md
    │   ├── generate-outline.md
    │   └── link-related-notes.md
    └── 🔬 research/
        ├── synthesize-sources.md
        ├── generate-questions.md
        └── create-literature-note.md
```

> [!warning]
> **Token Consumption in Custom Prompts**
> Behind-the-scenes prompts for Copilot commands also consume tokens. Complex custom prompts with extensive instructions or multiple examples will increase API costs. Balance prompt complexity with token efficiency by:
> - Using concise, clear instructions
> - Limiting few-shot examples to 2-3 per prompt
> - Avoiding redundant context repetition

---

## 🔤 Placeholder System & Variable Templating

> [!definition]
> - **Placeholder**:: Special syntax within custom prompts that gets dynamically replaced with actual content when the prompt is executed, such as `{selectedText}` for highlighted content, `{activeNote}` for the current file, `{[[Note Title]]}` for specific notes, or `{#tag1, #tag2}` for tag-filtered notes.
> - **Variable Templating**:: The system by which Copilot substitutes placeholder tokens with vault content, enabling dynamic, context-aware prompt execution.

### Core Placeholder Types

When creating prompts, several special placeholders can be used for dynamic content injection.

| Placeholder Syntax | Content Injected | Use Case |
|-------------------|------------------|----------|
| `{selectedText}` | Currently highlighted text | Text transformation, analysis of selections |
| `{activeNote}` | Entire content of current note | Note-level operations, summaries |
| `{[[Note Title]]}` | Content of specific named note | Cross-note comparisons, template following |
| `{#tag1, #tag2}` | All notes with any of the specified tags (note: tags must be in note property to work) | Domain aggregation, topic synthesis |
| `{folder:path}` | All notes within specified folder | Batch processing, folder-level analysis |

> [!methodology-and-sources]
> **Advanced Placeholder Composition**
> 
> **Single-Context Prompts** (Basic):
> ```markdown
> Summarize this text in 3 bullet points:
> {selectedText}
> ```
> 
> **Multi-Context Prompts** (Intermediate):
> ```markdown
> Compare the concept in {selectedText} with the framework described in {[[Reference Framework]]}.
> 
> Create a comparative analysis showing:
> - Similarities
> - Differences
> - Potential synthesis
> ```
> 
> **Aggregate-Context Prompts** (Advanced):
> ```markdown
> Come up with multiple choice questions using {activeNote}, 
> and follow the format of {[[Quiz Template]]} to start a quiz session.
> ```
> 
> **Tag-Filtered Synthesis** (Expert):
> ```markdown
> Analyze all notes tagged {#cognitive-science, #learning-theory} and:
> 
> 1. Identify 5 core themes across all notes
> 2. Find contradictions or tensions
> 3. Suggest synthesis opportunities
> 4. Propose 3 new atomic notes to create
> 
> Format as a MOC (Map of Content) with wiki-links.
> ```

### Dynamic Context Injection Patterns

Placeholders can be used to do anything normally done inside ChatGPT, but directly in Obsidian, with prompts able to contain links to notes for providing context.

> [!use-cases-and-examples]
> **Progressive Context Building**
> 
> **Pattern: Layered Context Injection**
> ```markdown
> # Comprehensive Note Analysis
> 
> ## Primary Context
> Analyze {activeNote}
> 
> ## Comparative Context
> Compare insights with {[[Related Concept]]} and {[[Alternative Framework]]}
> 
> ## Domain Context
> Consider broader themes from {#domain-tag}
> 
> ## Output
> Create synthesis note showing:
> - How {activeNote} fits within domain
> - Novel connections discovered
> - Questions for further exploration
> ```
> 
> This pattern allows **progressive context enrichment**, where each placeholder layer adds sophistication to the AI's understanding.

### Placeholder Best Practices

1. **Specificity**: Use the most targeted placeholder for your need
2. **Composition**: Combine multiple placeholders for rich context
3. **Documentation**: Comment within prompts what each placeholder provides
4. **Testing**: Verify placeholder resolution with `debug mode` enabled

> [!helpful-tip]
> **Debugging Placeholder Resolution**
> Turn on debug mode in Copilot settings to see how your prompt is processed. This reveals:
> - Which placeholders were successfully resolved
> - What content was actually injected
> - Token counts for each context segment
> - Any errors in placeholder syntax

---

## 🧠 Vault QA & RAG Prompt Optimization

> [!definition]
> - **Vault QA Mode**:: A powerful feature that lets users ask questions in plain language and get answers from all notes in Obsidian using RAG (Retrieval-Augmented Generation), which combines searching notes with AI responses to find accurate and relevant information quickly.
> - **RAG (Retrieval-Augmented Generation)**:: A technique that enhances a language model's output by first retrieving relevant external information—typically using embeddings—and then generating responses based on both the query and the retrieved content.

### RAG Architecture in Copilot

The [[RAG]] pipeline in Copilot operates through several distinct stages:

**Stage 1: Indexing** (One-time / periodic)
- Embedding model choice determines indexing quality, with options including OpenAI embedding models, Google, Cohere, or local models from Ollama.
- Indexing large vaults can take time and may incur costs if using paid embedding services.
- For local setup, users can run `ollama pull nomic-embed-text` to get embedding models for privacy-focused indexing.

**Stage 2: Query Processing** (Per interaction)
- User query is converted to embedding vector
- Semantic search identifies relevant note chunks
- Hybrid search combines vector similarity with Obsidian's note graph similarity

**Stage 3: Context Injection** (Dynamic)
- Copilot does a local search through the vault and passes relevant parts to the chat model to generate answers.
- Top-k most similar chunks are selected
- Context is formatted and injected into prompt

**Stage 4: Response Generation** (LLM inference)
- AI responds with relevant information and includes Sources citations to specific notes where information was found, allowing easy tracking of sources within the vault.

> [!key-claim]
> **Local-First Privacy Model**
> All QA modes leverage retrieval augmentation with a local index, ensuring data isn't sent to a cloud-based vector search service, with notes always stored on the user's own device and nowhere else.

### Prompt Engineering for Vault QA

Vault QA is best for specific questions, with limitations since it relies on retrieval—questions like "give me an overview of my vault" won't retrieve anything because there's nothing in the query to retrieve.

**Effective Query Patterns**:

| Query Type | Ineffective Example | Effective Example | Why It Works |
|------------|---------------------|-------------------|--------------|
| **Overview** | "Tell me about my vault" | "What are the main themes I've written about regarding cognitive science?" | Provides semantic anchor for retrieval |
| **Vague Search** | "What did I write about?" | "What did I learn about spaced repetition from my reading notes?" | Specific concept enables targeted search |
| **Temporal** | "What did I do yesterday?" | "What ideas did I capture in my daily notes about project management last week?" | Combines temporal + semantic signals |
| **Comparative** | "Compare my notes" | "How do my notes on productivity conflict with or support each other?" | Defines relationship to search for |

> [!methodology-and-sources]
> **RAG-Optimized Prompt Structure**
> 
> When designing prompts for Vault QA mode, follow this pattern:
> 
> ```markdown
> [SPECIFIC CONCEPT/TOPIC] + [ACTION VERB] + [CONTEXT CONSTRAINTS]
> 
> Examples:
> 
> ✓ "spaced repetition" + "summarize key findings" + "from my reading notes"
> ✓ "cognitive load theory" + "identify applications" + "in my project notes"
> ✓ "zettelkasten methodology" + "find contradictions" + "across my permanent notes"
> ✓ "learning frameworks" + "extract principles" + "related to educational psychology"
> ```
> 
> **Anti-Patterns to Avoid**:
> - ❌ Generic verbs without semantic content ("tell me about…")
> - ❌ Questions without retrieval targets ("what's interesting in my vault?")
> - ❌ Overly broad scopes ("analyze everything I know about…")

### Embedding Model Selection & Impact

Embedding model choice affects both indexing quality and costs, with local embedding models like those from Ollama offering privacy and cost benefits but potentially being slower or less accurate than some cloud services.

**Model Characteristics & Prompt Implications**:

| Model Type | Semantic Accuracy | Speed | Cost | Best For |
|------------|------------------|-------|------|----------|
| **OpenAI text-embedding-3-small** | High | Fast | Low-medium | General-purpose, English-dominant vaults |
| **OpenAI text-embedding-3-large** | Very High | Medium | Medium-high | Technical/academic content, multi-lingual |
| **Google/Cohere Models** | High | Fast | Medium | Alternative to OpenAI, similar performance |
| **Ollama (nomic-embed-text)** | Medium-High | Slower | Free | Privacy-focused, local-first workflows |
| **LM Studio Embeddings** | Medium | Variable | Free | Local experimentation, testing |

> [!warning]
> **Embedding Model Consistency**
> Don't switch embedding models after indexing—it can break the results. Each embedding model creates a different vector space, so changing models requires complete re-indexing to maintain search quality.

### Advanced Vault QA Configuration

To customize Vault QA experience, several settings can be adjusted including Auto-Index Strategy (NEVER, ON STARTUP, or ON MODE SWITCH recommended), Embedding Model choice, Requests per Second for rate limiting, and Indexing Exclusions for folders, tags, or note name patterns.

**Auto-Index Strategy Comparison**:

```markdown
## NEVER (Manual Control)
**Use When**: Small vault, infrequent updates, cost-sensitive
**Pros**: Complete control, no surprise API charges
**Cons**: Must remember to manually update index

## ON STARTUP (Automatic Sync)
**Use When**: Frequently updated vault, generous API budget
**Pros**: Always current, no manual intervention
**Cons**: Repeated indexing costs, slower startup

## ON MODE SWITCH (Balanced) ⭐ RECOMMENDED
**Use When**: Regular Vault QA usage, moderate update frequency
**Pros**: Updates only when needed, balanced cost/freshness
**Cons**: First switch to Vault QA may trigger indexing delay
```

> [!helpful-tip]
> **Indexing Exclusion Strategy**
> Specify folders, tags, or note name patterns to exclude from indexing to help manage large vaults or keep certain information private so they are never sent to the LLM.
> 
> **Common Exclusion Patterns**:
> ```
> Folders to Exclude:
> - /99_system/
> - /archived/
> - /templates/
> 
> Tags to Exclude:
> - #private
> - #draft
> - #excalidraw
> 
> Name Patterns to Exclude:
> - *-daily-note.md
> - *-journal.md
> - scratch-*.md
> ```

### Vault QA Prompt Refinement Techniques

**Technique 1: Query Decomposition**
```markdown
Instead of: "How can I improve my learning?"

Use Series:
1. "What learning techniques have I documented in my notes?"
2. "Which of those techniques did I find most effective?"
3. "What obstacles to learning have I identified?"
4. "How do my effective techniques address those obstacles?"
```

**Technique 2: Citation-Aware Prompting**
```markdown
"Identify 3 key insights about [topic] from my notes. 

For each insight:
- Provide the core claim
- Note which source notes support it
- Identify any contradicting perspectives in my vault
"
```

Citations provided should be used to verify information in original notes, with regular index updates recommended especially after adding new notes or making significant changes to the vault.

**Technique 3: Progressive Refinement**
```markdown
Round 1: "What are the main themes in my notes about [topic]?"
[Review results]

Round 2: "Focus on [specific theme from Round 1]. What are the sub-topics?"
[Review results]

Round 3: "For [sub-topic], what are the actionable insights?"
```

---

## 🎨 Advanced Prompt Patterns & Techniques

> [!definition]
> - **Prompt Pattern**:: A reusable template structure that solves a specific class of prompting challenges through proven architectural design.
> - **Chain-of-Thought (CoT)**:: A prompt engineering trick where the model explains its reasoning before providing an answer, making it more likely to write a coherent response by giving the attention mechanism more guidance.

### Pattern 1: Iterative Refinement Chain

**Purpose**: Transform rough ideas into polished notes through multi-stage processing

**Implementation**:
```markdown
# Stage 1: Expansion
Title: "Expand Rough Note"
Take {selectedText} and expand into detailed explanation:
- Define core concepts
- Provide 2-3 examples
- Identify related ideas in my vault

# Stage 2: Structure
Title: "Add Structure"
Take {activeNote} and organize into:
## Core Concept
## Detailed Explanation  
## Examples
## Connections
## Questions

# Stage 3: Integration
Title: "Link to Vault"
Analyze {activeNote} and suggest:
- 5 existing notes to link
- 3 new atomic notes to create
- Tags to add
```

### Pattern 2: Multi-Perspective Analysis

**Purpose**: Examine concepts through different analytical lenses

**Implementation**:
```markdown
Analyze {selectedText} from multiple perspectives:

## 📊 Analytical Perspective
[Logical structure, assumptions, evidence quality]

## 🎨 Creative Perspective  
[Novel connections, metaphors, generative questions]

## 🔬 Critical Perspective
[Weaknesses, gaps, counterarguments]

## 🌍 Practical Perspective
[Applications, implementations, action steps]

## Synthesis
[Integrate insights across perspectives]
```

### Pattern 3: Zettelkasten Workflow Automation

**Purpose**: Streamline atomic note creation with proper linking

**Implementation**:
```markdown
Title: "Process Literature Note"

Transform {activeNote} (literature note) into atomic notes:

For each distinct concept in the source:

1. Create atomic note outline:
   - Title: [Concept Name]
   - Definition: [One sentence]
   - Explanation: [2-3 paragraphs]
   - Examples: [2 concrete examples]
   - Related: [3-5 related atomic notes to link]
   - Source: [[{activeNote}]]
   - Tags: [Appropriate tags]

2. Identify:
   - Structure notes (MOCs) this connects to
   - Sequences this could join
   - Emerging themes across multiple concepts

Output as checklist of notes to create.
```

### Pattern 4: Progressive Summarization

**Purpose**: Create multi-layer summaries for different contexts

**Implementation**:
```markdown
Create progressive summary layers for {activeNote}:

## Layer 1: Tweet (280 characters)
[Ultra-concise essence]

## Layer 2: Paragraph (100 words)
[Key points with minimal context]

## Layer 3: Executive Summary (250 words)
[Comprehensive overview with main arguments]

## Layer 4: Annotated Outline
[Structured breakdown with key quotes and page numbers]

Use Layer 1 for linking context, Layer 2 for MOCs, 
Layer 3 for project briefs, Layer 4 for deep dives.
```

### Pattern 5: Conceptual Bridge Building

**Purpose**: Connect disparate ideas across domains

**Implementation**:
```markdown
Build conceptual bridges between:
- Primary: {[[Note 1]]}
- Secondary: {[[Note 2]]}

## Direct Connections
[Explicit overlaps in content]

## Structural Parallels
[Similar frameworks or methodologies]

## Analogical Mappings
[Metaphorical relationships]

## Synthesis Opportunities
[Novel insights from combination]

## New Note Proposals
[Atomic notes to capture synthesized insights]
```

### Pattern 6: Adaptive Context Windowing

**Purpose**: Optimize context for token-limited models

**Implementation**:
```markdown
# Context Prioritization Protocol

## Priority 1: Essential Context (Always Include)
{activeNote} - Current working note

## Priority 2: Direct References (Include if tokens allow)
{[[Mentioned Note 1]]} {[[Mentioned Note 2]]}

## Priority 3: Domain Context (Include if tokens remain)
{#primary-domain-tag}

## Priority 4: Related Exploration (Include if budget available)
{#related-domain-tag}

Task: [Your actual request]

Note: Copilot will naturally truncate lower-priority sections if context window is exceeded.
```

> [!key-claim]
> **Context Window Strategy**
> Token limits, temperature controls, and conversation turn management are critical parameters—more turns give better context but use more tokens and may cost more. Strategic context prioritization ensures the most valuable information is retained even when approaching model limits.

### Pattern 7: Chain-of-Density (CoD) Prompting

**Purpose**: Progressively increase information density through iterations

**Implementation**:
```markdown
Title: "Density-Optimized Summary"

Create 5 iterations of {selectedText} summary, each more dense:

## Iteration 1: Sparse (50 words)
[High-level overview, basic concepts]

## Iteration 2: Basic (75 words)
[Add key details, maintain readability]

## Iteration 3: Moderate (100 words)
[Introduce technical terms, more specifics]

## Iteration 4: Dense (125 words)
[Maximum information, compact expression]

## Iteration 5: Ultra-Dense (150 words)
[Expert-level density, assumes background knowledge]

Select iteration based on target audience and context.
```

### Pattern 8: Dialectical Synthesis

**Purpose**: Resolve tensions between conflicting notes

**Implementation**:
```markdown
Perform dialectical analysis:

## Thesis
{[[Note A]]} argues:
[Key claims and reasoning]

## Antithesis
{[[Note B]]} counters:
[Opposing claims and reasoning]

## Analysis
- Points of genuine disagreement
- Points of semantic confusion
- Points of hidden agreement
- Unstated assumptions in each

## Synthesis
[Higher-order insight that resolves or transcends conflict]

## Action Items
- [ ] Create atomic note: [Synthesis concept]
- [ ] Update [[Note A]] with synthesis link
- [ ] Update [[Note B]] with synthesis link
- [ ] Tag as #resolved-tension
```

---

## 🔧 Prompt Configuration & Properties

> [!definition]
> - **Prompt Properties**:: YAML frontmatter within custom prompt notes that set modes, models, and rendering behaviors using special Copilot-specific parameters like `Copilot_mode`, `Copilot_model`, and `Copilot_render_note`.
> - **Property Scope**:: Configuration settings that apply specifically to individual prompt execution, enabling fine-grained control over behavior.

### Available Prompt Properties

Users can set certain modes when Custom Prompts execute using YAML properties in the front matter of the note containing the Custom Prompt.

**Core Property Types**:

| Property | Values | Purpose | Example |
|----------|--------|---------|---------|
| `Copilot_mode` | `chat`, `vault_qa` | Switches Copilot mode for execution (e.g., to run a prompt in chat mode even when Vault QA is selected) | `Copilot_mode: chat` |
| `Copilot_model` | Model identifier | Sets a pre-configured model for execution (e.g., `perplexity/llama-3.1-sonar-large-128k-online`) | `Copilot_model: gpt-4` |
| `Copilot_model_restore` | `true`, `false` | Indicates whether to restore the previous value of the selected model after the query is executed | `Copilot_model_restore: true` |
| `Copilot_render_note` | `true`, `false` | Executes Dataview blocks or Tasks queries and adds rendering results to context instead of raw text | `Copilot_render_note: true` |

### Implementation Examples

**Example 1: Mode-Specific Prompt**
```markdown
---
Copilot_mode: chat
Copilot_mode_restore: true
---

Generate list of tags for this note {activeNote}
```

**Use Case**: Force execution in Chat mode (faster) even when Vault QA is selected, ideal for tag generation which doesn't require vault search.

**Example 2: Model-Specific Prompt**
```markdown
---
Copilot_model: perplexity/llama-3.1-sonar-large-128k-online
Copilot_model_restore: true
---

Show the weather forecast for Moscow for the next week.
```

**Use Case**: Leverage web-search-capable model for real-time information, then restore previous model selection.

**Example 3: Dynamic Rendering**
```markdown
---
Copilot_render_note: true
---

Based on {activeNote}, plan my day.
```

**Use Case**: When `{activeNote}` contains Dataview queries or Tasks lists, execute them first so the AI sees actual results rather than query syntax.

> [!methodology-and-sources]
> **Advanced Property Composition**
> 
> **Multi-Property Configuration**:
> ```markdown
> ---
> Copilot_mode: vault_qa
> Copilot_model: claude-3-opus
> Copilot_model_restore: true
> Copilot_render_note: true
> ---
> 
> Analyze all incomplete tasks in {activeNote} alongside 
> relevant project notes from my vault.
> 
> For each task:
> 1. Identify blocking dependencies
> 2. Find related notes with solutions
> 3. Suggest next actions
> 4. Estimate time requirements
> ```
> 
> **Why This Works**:
> - `vault_qa` mode enables semantic search across vault
> - Claude Opus provides high-quality analysis
> - `render_note: true` shows actual tasks, not syntax
> - `model_restore` returns to default after execution

### Property-Based Workflow Automation

> [!use-cases-and-examples]
> **Scenario: Daily Planning Automation**
> 
> **Problem**: Daily note contains Tasks query showing today's obligations, but standard prompt execution only sees query syntax, not results.
> 
> **Solution**:
> ```markdown
> ---
> Copilot_mode: chat
> Copilot_render_note: true
> Copilot_model: gpt-4
> ---
> 
> {activeNote} contains my tasks for today.
> 
> Create optimized schedule considering:
> - Task priority and dependencies
> - Estimated time requirements  
> - Energy levels (high morning, lower afternoon)
> - Meetings (from calendar)
> 
> Output as time-blocked schedule with buffer periods.
> ```
> 
> **Result**: AI sees rendered task list (not query syntax), plans realistically, uses fast Chat mode (not Vault QA), leverages GPT-4's planning capabilities.

### Conditional Property Usage

**Pattern: Environment-Aware Prompting**

```markdown
---
# Use Ollama for local, privacy-sensitive processing
Copilot_model: ollama/mistral
Copilot_mode: chat
---

# Sensitive Data Processing
Process {selectedText} containing:
- Personal information
- Proprietary knowledge
- Draft ideas

[Processing instructions…]

Note: This prompt uses local model to ensure privacy.
```

vs.

```markdown
---
# Use Claude Opus for complex reasoning requiring high intelligence
Copilot_model: claude-3-opus
Copilot_mode: vault_qa
---

# Complex Synthesis
Analyze {#research-domain} for:
- Emergent patterns
- Theoretical contradictions
- Novel research directions

[Analysis instructions…]

Note: This prompt uses Opus for its superior reasoning capabilities.
```

> [!warning]
> **Property Limitations**
> Currently, properties are proposal features discussed in the community (as seen in Discussion #794). Verify property support in your Copilot version through documentation or testing. Core properties (`Copilot_mode`, `Copilot_model`) are implemented; others may be planned features.

---

## 📊 Performance Optimization & Token Management

> [!definition]
> - **Token**:: A small unit of text (like a word or part of a word) that AI models process when reading or generating language.
> - **Token Budget**:: Maximum tokens generated per response (default is 1000), which can be configured to balance response length with cost.

### Understanding Token Economics

Behind-the-scenes prompts for Copilot commands also consume tokens, so users must be mindful of token consumption across all interactions.

**Token Consumption Sources**:

1. **System Prompts**: Base instructions (typically 50-200 tokens)
2. **Custom Prompt Templates**: Your reusable prompts (varies widely)
3. **Context Injection**: Placeholder-resolved content (can be thousands of tokens)
4. **Conversation History**: Conversation turns (one turn = 2 messages: user input + AI response) are kept for context, with more turns using more tokens
5. **Output Generation**: AI's response (up to configured max_tokens)

> [!methodology-and-sources]
> **Token Estimation & Management**
> 
> **Rule of Thumb**: 1 token ≈ 0.75 words in English
> 
> **Quick Calculations**:
> - Small note (500 words) = ~667 tokens
> - Medium note (2000 words) = ~2,667 tokens
> - Large note (5000 words) = ~6,667 tokens
> - Complete conversation (10 turns) = variable, typically 2,000-10,000 tokens
> 
> **Copilot Command for Token Counting**:
> Use "Count total tokens" Copilot command to estimate cost before indexing large vaults, which is especially useful for users with paid embedding providers.

### Optimization Strategy 1: Context Compression

**Technique: Hierarchical Context Selection**

```markdown
# Instead of: Including entire related notes

{[[Related Note 1]]}  # Could be 5000+ tokens
{[[Related Note 2]]}  # Could be 5000+ tokens
{[[Related Note 3]]}  # Could be 5000+ tokens

Task: [Your request]

# Use: Selective referencing

## Core Context
{activeNote}

## Key References (Summaries Only)
- [[Related Note 1]]: [2-sentence summary]
- [[Related Note 2]]: [2-sentence summary]  
- [[Related Note 3]]: [2-sentence summary]

Task: [Your request]

For full details on any reference, see the linked notes.
```

**Token Savings**: From ~15,000 tokens → ~2,000 tokens (87% reduction)

### Optimization Strategy 2: Prompt Compression

**Anti-Pattern (Verbose)**:
```markdown
I would like you to please analyze the following text that I have selected 
and provide me with a comprehensive summary that includes all of the main 
points and key takeaways, formatted in a way that makes it easy to understand 
and reference later, with bullet points for each major concept discussed.

{selectedText}
```
**Token Cost**: ~65 tokens just for instructions

**Optimized Pattern (Concise)**:
```markdown
Summarize {selectedText} with:
- Main points as bullets
- Key takeaways
- Clear formatting for reference
```
**Token Cost**: ~15 tokens (77% reduction)

> [!helpful-tip]
> **The Compression Principle**
> Every word in your prompt costs tokens. Optimize by:
> 1. Removing filler words ("please", "I would like", "if possible")
> 2. Using imperative voice ("Analyze…" not "Can you analyze…")
> 3. Structuring with bullets instead of prose where appropriate
> 4. Front-loading the most important instructions

### Optimization Strategy 3: Conversation History Management

Conversation Turns setting determines number of past exchanges kept for context, with one turn consisting of 2 messages (your input and AI response)—more turns give better context but use more tokens and may cost more.

**Optimal Turn Counts by Use Case**:

| Use Case | Recommended Turns | Reasoning |
|----------|------------------|-----------|
| One-shot transformations | 1-2 | No context needed between operations |
| Iterative refinement | 3-5 | Need immediate previous responses |
| Complex reasoning chains | 5-8 | Build on accumulated insights |
| Long research sessions | 8-10 | Maintain coherent thread across many queries |

**Configuration Location**: Settings → Copilot → Model Settings → Conversation Turns

### Optimization Strategy 4: Temperature Tuning

Temperature controls randomness with default at 0.1—lower values make answers more focused, higher values make them more creative.

**Temperature Guidelines**:

```markdown
## Temperature 0.0-0.2 (Focused)
**Use For**: 
- Factual summarization
- Data extraction
- Structured formatting
- Tag generation

## Temperature 0.3-0.5 (Balanced)  
**Use For**:
- General writing
- Analysis and synthesis
- Comparative evaluations
- Default for most tasks

## Temperature 0.6-0.8 (Creative)
**Use For**:
- Brainstorming
- Idea generation
- Creative connections
- Exploratory thinking

## Temperature 0.9-1.0 (Experimental)
**Use For**:
- Highly creative writing
- Unexpected associations
- Breaking through mental blocks
```

### Optimization Strategy 5: Strategic Model Selection

Different models have vastly different token costs and capabilities. Strategic model selection based on task complexity can dramatically reduce costs.

**Model Selection Matrix**:

| Task Complexity | Recommended Model | Token Cost (Relative) | When to Use |
|-----------------|------------------|----------------------|-------------|
| **Simple** | GPT-3.5 Turbo, Claude Haiku | 1x | Tag generation, simple formatting, basic summaries |
| **Moderate** | GPT-4 Turbo, Claude Sonnet | 10x | Analysis, synthesis, structured output |
| **Complex** | GPT-4, Claude Opus | 30x | Deep reasoning, creative synthesis, multi-step logic |
| **Specialized** | Perplexity (web search) | 15x | Real-time information, current events |
| **Local** | Ollama models | Free | Privacy-sensitive content, unlimited usage |

> [!use-cases-and-examples]
> **Cost-Optimized Workflow**
> 
> **Scenario**: Processing 50 literature notes into atomic notes
> 
> **Naive Approach** (All Claude Opus):
> - 50 notes × 5 atomic notes each = 250 operations
> - Average 3,000 tokens per operation
> - Total: 750,000 tokens
> - Cost at Opus rates: ~$56.25
> 
> **Optimized Approach** (Tiered Processing):
> 1. **Extract concepts** (GPT-3.5): 50 ops × 1,500 tokens = 75,000 tokens ($0.15)
> 2. **Structure atomic notes** (GPT-4): 250 ops × 2,000 tokens = 500,000 tokens ($15.00)
> 3. **Deep synthesis** (Opus, 10 notes only): 10 ops × 5,000 tokens = 50,000 tokens ($3.75)
> 
> **Total Cost**: $18.90 (66% savings)

### Optimization Strategy 6: Caching & Reuse

**Pattern: Template-Based Reuse**

```markdown
# Create reusable note structures that avoid repetition

# Base Template (save as snippet)
Title: "Atomic Note Template"

## Definition
[One-sentence definition]

## Explanation  
[2-3 paragraphs]

## Examples
1. [Example 1]
2. [Example 2]

## Connections
- Related: [[…]]
- Contrasts: [[…]]

## Source
[[Original Source]]

# Usage in prompts
"Transform {selectedText} following standard [[Atomic Note Template]]"

# Token Savings: Template reference (10 tokens) vs. full specification (150 tokens)
```

---

## 🚀 Copilot Plus & Agentic Prompt Engineering

> [!definition]
> - **Copilot Plus**:: A paid tier offering advanced features beyond free tier, including autonomous agent with tools, enhanced vault search with time-based queries, contextual chat with richer context, and project mode for focused work across 50+ file types.
> - **Agentic Prompting**:: Prompt patterns that enable intentional use of agentic tools to accomplish tasks through the @ toolkit palette including @vault, @youtube, @websearch, and @composer.

### Agentic Tool System

Type @ in chat to launch Copilot tool palette with multiple specialized agents.

**Available Agentic Tools**:

| Tool | Capability | Prompt Pattern | Use Case |
|------|------------|----------------|----------|
| `@vault` | Provides access to enhanced vault-related functions, more powerful than Vault QA (Basic) | `@vault find all notes about [topic] created after [date]` | Time-filtered research |
| `@youtube` | Use prompt plus YouTube video URL to get quick insights and ask follow-up questions about content | `@youtube [URL] summarize main arguments` | Video content extraction |
| `@websearch` | Use web search for gathering real-time information from the internet | `@websearch latest research on [topic]` | Current information gathering |
| `@composer` | Use composer to edit notes directly within chat—organizing content, applying tags, highlighting key details, and cleaning up irrelevant info | `@composer restructure {activeNote} with proper headers` | In-chat note editing |

### Context Type Support in Copilot Plus

Context types support includes markdown, PDF, image, youtube, and URL.

**Multi-Modal Context Patterns**:

```markdown
# Pattern 1: PDF + Vault Synthesis
[Upload PDF via +Add context button]

Compare the framework in this PDF with my vault's understanding 
of the same topic from {#domain-tag}.

Identify:
- Alignments
- Contradictions  
- Novel insights in PDF not yet in vault
- Opportunities for new atomic notes

# Pattern 2: YouTube + Note Integration
@youtube [video URL]

Extract key concepts from this video and:
1. Compare with [[Related Vault Note]]
2. Identify which concepts warrant atomic notes
3. Generate atomic note outlines for top 3 concepts
4. Suggest tags and links

# Pattern 3: Web Research + Vault Update
@websearch recent developments in [topic]

Based on search results:
1. Identify which developments relate to my vault notes {#topic-tag}
2. Highlight outdated information in my notes
3. Suggest updates to [[Specific Note]]
4. Propose new notes for emerging concepts
```

### Project Mode Prompt Engineering

Projects mode enables focused work across 50+ file types, allowing users to define per-project system prompts and settings and quickly switch between different contexts such as work, personal, creative writing, etc.

> [!methodology-and-sources]
> **Project-Specific System Prompts**
> 
> **Pattern: Context-Scoped Agents**
> 
> ```markdown
> # Project: Academic Research
> System Prompt:
> 
> You are a research assistant for academic writing.
> 
> Context:
> - Working on [dissertation topic]
> - Following [citation style]
> - Target journal: [journal name]
> 
> Capabilities:
> - Synthesize literature
> - Generate citations
> - Identify research gaps
> - Structure academic arguments
> 
> Output Format:
> - Formal academic tone
> - Include citations inline
> - Flag claims needing sources
> 
> ---
> 
> # Project: Creative Writing
> System Prompt:
> 
> You are a creative writing collaborator.
> 
> Context:
> - Genre: [genre]
> - Target audience: [audience]
> - Tone: [tone preferences]
> 
> Capabilities:
> - Character development
> - Plot brainstorming
> - Dialogue refinement
> - Descriptive enhancement
> 
> Output Format:
> - Vivid, evocative language
> - Show, don't tell
> - Genre-appropriate style
> 
> ---
> 
> # Project: Technical Documentation
> System Prompt:
> 
> You are a technical documentation expert.
> 
> Context:
> - Product: [product name]
> - Audience: [technical level]
> - Style guide: [link to guide]
> 
> Capabilities:
> - API documentation
> - Code examples
> - Troubleshooting guides
> - Clear explanations
> 
> Output Format:
> - Concise, scannable
> - Code blocks with syntax highlighting
> - Step-by-step procedures
> - Warning callouts for gotchas
> ```

### Long-Term Memory Integration

Long-term memory is a tool the agent can use by itself starting from version 3.1.0, enabling the agent to remember information across sessions.

**Memory-Aware Prompt Pattern**:

```markdown
# Leveraging Long-Term Memory

[Implicit Memory Usage - No Special Syntax Needed]

## Example 1: Iterative Project Development
Session 1: "I'm starting a project on cognitive load theory applied to PKM"
Session 2: "Continue my PKM project—what should I focus on next?"
[Agent recalls context from Session 1]

## Example 2: Preference Learning
Over time: Multiple interactions show preference for structured, outline-first approach
Future prompts: Agent proactively suggests outlines before detailed content

## Example 3: Domain-Specific Context
Repeated work in a domain: Agent builds understanding of vocabulary, frameworks, key authors
Future prompts: Agent uses domain-appropriate language without prompting
```

### Autonomous Agent Workflow Patterns

**Pattern: Research Pipeline Automation**

```markdown
# Autonomous Research Agent

Goal: Investigate [topic] and update my vault

Agent Workflow:
1. @websearch latest research on [topic]
2. Identify top 3 most relevant sources
3. @websearch [source 1 details]
4. @websearch [source 2 details]  
5. @websearch [source 3 details]
6. Synthesize findings
7. @vault find related notes in my vault
8. Compare new research with existing notes
9. @composer create new atomic note: [[New Concept]]
10. @composer update [[Existing Note]] with new insights
11. Generate follow-up research questions

Output: Summary of updates + links to new/modified notes
```

**Pattern: Content Processing Pipeline**

```markdown
# PDF → Vault Integration Agent

Input: [Upload PDF via context menu]

Agent Workflow:
1. Extract key concepts from PDF
2. @vault search for related notes
3. For each key concept:
   a. Check if concept exists in vault
   b. If exists: identify updates/contradictions
   c. If new: generate atomic note outline
4. @composer create 3 new atomic notes
5. @composer update 2 existing notes with PDF insights
6. Generate MOC connecting PDF concepts to vault

Output: Processing report + direct links to all modified notes
```

### Copilot Plus Model Selection

Default chat model is "copilot-plus-flash" (Gemini Flash with one context window), subject to change based on the best available model, and is included at no extra cost with the Copilot Plus paid plan.

**Specialized Plus Models**:

- **copilot-plus-flash**: Frontier chat model with balanced speed and performance
- **copilot-plus-multilingual**: Enhanced capabilities for multi-language content
- **copilot-plus-large** (Believer plan): Powerful embedding model designed for advanced reasoning tasks such as legal notes, math formulas, and complex multilingual content

> [!helpful-tip]
> **Model Selection for Agentic Workflows**
> If choosing a favorite AI model within Copilot Plus, recommendation is to start with Gemini Flash for its balance of speed and performance included at no extra cost, with specialized tasks exploring OpenAI-compatible models like copilot-plus-multilingual or copilot-plus-large for enhanced capabilities.

---

## 🎯 Synthesis & Mastery

> [!the-philosophy]
> **The Philosophy of Copilot Prompt Engineering**
> 
> Prompt engineering in Copilot is fundamentally about **augmenting human thinking within a networked knowledge environment**. Unlike standalone LLM interfaces, Copilot prompts exist within the context of an evolving [[Personal Knowledge Base]], where each interaction should:
> 
> 1. **Strengthen the knowledge graph** through thoughtful linking
> 2. **Respect the vault's existing structure** (Zettelkasten, PARA, etc.)
> 3. **Maximize reusability** through placeholder templating
> 4. **Optimize for long-term value** over short-term convenience
> 5. **Maintain data sovereignty** through local-first privacy
> 
> The highest mastery lies not in crafting the perfect single prompt, but in building a **prompt library ecosystem** where prompts compose, reference each other, and evolve alongside your thinking.

### Cognitive Models for Prompt Design

**Model 1: The Librarian Model**
- Copilot as research assistant who finds and surfaces relevant information
- Optimize for: Specific queries, clear retrieval targets, semantic richness
- Use: Vault QA mode, tag-based aggregation, citation-aware prompting

**Model 2: The Editor Model**  
- Copilot as writing collaborator who transforms and refines content
- Optimize for: Iterative refinement, style consistency, structural clarity
- Use: Custom prompts, progressive summarization, multi-stage processing

**Model 3: The Synthesizer Model**
- Copilot as conceptual bridge-builder who connects disparate ideas
- Optimize for: Multi-note context, comparative analysis, emergence of novel insights
- Use: Advanced placeholders, multi-perspective patterns, dialectical synthesis

**Model 4: The Agent Model**
- Copilot as autonomous task executor who handles workflows end-to-end
- Optimize for: Tool composition, multi-step chains, context-aware decisions
- Use: Copilot Plus features, agentic patterns, autonomous workflows

> [!analogy]
> **The Orchestra Conductor**
> 
> Mastering Copilot prompt engineering is like conducting an orchestra. Each prompt is an instrument:
> - **Custom prompts** = strings (versatile, frequent use)
> - **Vault QA** = brass (powerful, focused application)
> - **Agentic tools** = percussion (punctuates with specific effects)
> - **System prompts** = conductor's baton (sets overall direction)
> 
> The artistry lies not in any single instrument, but in orchestrating them together—knowing when to have the strings carry the melody, when to bring in the brass for emphasis, when to let percussion punctuate, all while the conductor (system prompt) maintains coherent direction.

### Progressive Mastery Path

**Level 1: Prompt User** (Weeks 1-4)
- Master basic custom prompt creation
- Understand placeholder system
- Use built-in Copilot commands effectively
- Configure Chat vs. Vault QA modes appropriately

**Level 2: Prompt Designer** (Weeks 5-8)
- Design reusable prompt templates
- Implement advanced placeholder composition
- Optimize token usage strategically
- Create domain-specific prompt libraries

**Level 3: Prompt Architect** (Weeks 9-12)
- Engineer complex multi-stage workflows
- Design vault-integrated prompt ecosystems
- Master RAG optimization techniques
- Implement prompt properties for fine control

**Level 4: Prompt Systematizer** (Months 4-6)
- Build coherent prompt library architectures
- Create self-documenting prompt systems
- Develop prompt testing & validation workflows
- Contribute patterns back to community

**Level 5: Prompt Synthesizer** (Ongoing)
- Innovate novel prompt patterns
- Cross-pollinate techniques across domains
- Teach prompt engineering to others
- Shape evolution of Copilot capabilities

> [!key-claim]
> **The Emergent Property of Mastery**
> 
> True mastery emerges not from memorizing patterns, but from developing **prompt intuition**—the ability to immediately recognize which prompt pattern, which mode, which model, which placeholders will most effectively accomplish a given knowledge work task within your unique vault context. This intuition develops only through consistent, reflective practice.

### Common Prompt Engineering Pitfalls

| Pitfall | Manifestation | Solution |
|---------|---------------|----------|
| **Over-Specification** | Prompts so detailed they constrain creativity | Use general patterns, let model fill gaps |
| **Under-Specification** | Vague prompts producing inconsistent results | Add structure, examples, output format specs |
| **Context Bloat** | Including entire notes when summaries suffice | Hierarchical context selection, progressive detail |
| **Mode Mismatch** | Using Chat mode for vault-search tasks | Understand mode strengths, configure with properties |
| **Reusability Neglect** | Creating one-off prompts repeatedly | Build prompt library with placeholders |
| **Token Ignorance** | Unexpected costs from inefficient prompts | Monitor token usage, optimize strategically |
| **Feedback Loop Absence** | Never refining prompts based on outputs | Document what works, iterate systematically |

### Integration with PKM Workflows

**Zettelkasten Integration**:
```markdown
# Copilot as Zettelkasten Assistant

Capture Phase:
- Custom Prompt: "Extract concepts" → Identify atomic note candidates
- Vault QA: "Is this concept already in my vault?" → Check for duplicates

Elaborate Phase:  
- Custom Prompt: "Expand atomic note" → Add detail to concepts
- Vault QA: "What do I already know about X?" → Find related notes

Connect Phase:
- Custom Prompt: "Find connections" → Suggest links
- Vault QA: "Which notes relate to Y?" → Discover relationships

Reflect Phase:
- Custom Prompt: "Synthesize theme" → Create structure notes/MOCs
- Agentic: @composer "Update MOC with new links" → Maintain navigation
```

**PARA Method Integration**:
```markdown
# Copilot for PARA Organization

Projects:
- Agentic: @composer "Structure project note" → Standardize format
- Custom Prompt: "Generate project tasks" → Extract actionable items

Areas:
- Vault QA: "Summarize my understanding of [area]" → Periodic review
- Custom Prompt: "Update area MOC" → Maintain area dashboards

Resources:
- Custom Prompt: "Create literature note from [source]" → Capture
- Vault QA: "Find resources about [topic]" → Discovery

Archives:
- Custom Prompt: "Archive completed project" → Move & document
- Vault QA: "What did I learn from [archived project]?" → Retrospective
```

---

## 📊 Metadata & Attribution

> [!methodology-and-sources]
> **Research Methodology**
> 
> This reference note synthesizes information from multiple authoritative sources:
> 
> **Primary Sources**:
> - Official Copilot for Obsidian GitHub repository and documentation (github.com/logancyang/obsidian-copilot)
> - Obsidian Copilot official documentation site (obsidiancopilot.com)
> - Comprehensive feature documentation for custom prompts, settings, getting started, and vault QA
> 
> **Technical Analysis**:
> - Xebia technical deep-dive on Copilot plugin implementation and prompt engineering architecture
> - Auto-completion plugin variant analysis (j0rd1smit/obsidian-copilot-auto-completion)
> 
> **Community Resources**:
> - GitHub Discussion #794 on Custom Prompt Properties
> - Tutorial on local Copilot setup with Ollama (productivity.dev)
> - Integration guide comparing Smart Connections and Copilot (effortlessacademic.com)
> 
> **Research Queries Executed**:
> 1. "Obsidian Copilot plugin prompt engineering"
> 2. "Obsidian Copilot custom prompts advanced techniques"
> 3. "Obsidian Copilot placeholders variables context"
> 4. "Obsidian Copilot RAG embeddings vault QA"
> 5. "Obsidian Copilot system prompt custom prompt best practices"
> 
> **Synthesis Approach**:
> - Cross-referenced official documentation with community implementations
> - Validated prompt patterns through technical architecture analysis
> - Integrated user workflows from tutorial sources
> - Organized information following progressive complexity principles
> 
> **Confidence Levels**:
> - Core Features (Chat, Vault QA, Custom Prompts): 🟢 HIGH (extensively documented)
> - Advanced Properties (Copilot_model, etc.): 🟡 MEDIUM (community proposals, verify version support)
> - Agentic Features (Copilot Plus): 🟢 HIGH (official premium features)
> - Performance Optimization: 🟢 HIGH (derived from technical analysis + user reports)

---

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-23 | Initial comprehensive compilation covering all aspects of Copilot prompt engineering including system prompts, custom prompts, placeholders, RAG optimization, advanced patterns, configuration properties, performance optimization, and Copilot Plus agentic features |

---

# 🔗 Related Topics for PKB Expansion

1. **[[Copilot for Obsidian - Complete Setup & Configuration Guide]]**
   - *Connection*: This reference covers prompt engineering; a setup guide would complement with installation, API key configuration, model selection, and initial optimization
   - *Depth Potential*: Step-by-step configuration for different use cases (local-first, cloud-hybrid, Copilot Plus), troubleshooting common issues, performance benchmarking
   - *Knowledge Graph Role*: Foundational prerequisite note that ensures users can actually implement the prompt engineering techniques documented here

2. **[[RAG Architecture & Embedding Models for Personal Knowledge Management]]**
   - *Connection*: Vault QA section touches on RAG and embeddings; deeper exploration of vector search, embedding model comparison, and RAG pipeline optimization would enable advanced users
   - *Depth Potential*: Technical deep-dive into semantic search algorithms, embedding model architectures (OpenAI vs. local), chunking strategies, hybrid search techniques, local vector database options
   - *Knowledge Graph Role*: Bridges Copilot-specific implementation with broader [[Information Retrieval]] and [[Vector Databases]] concepts

3. **[[Custom Prompt Library Architecture - Design Patterns for Obsidian Vaults]]**
   - *Connection*: This note covers individual prompt patterns; a dedicated architecture guide would address organizing 50+ prompts, versioning, documentation, testing, and collaborative sharing
   - *Depth Potential*: Directory structure best practices, naming conventions, prompt inheritance patterns, testing frameworks, community sharing protocols, prompt evolution strategies
   - *Knowledge Graph Role*: Elevates prompt engineering from individual techniques to systematic library management, connecting to [[Software Architecture]] and [[Library Science]] principles

4. **[[Agentic AI Workflows in Personal Knowledge Management]]**
   - *Connection*: Copilot Plus section introduces agentic patterns; broader exploration would cover autonomous workflows beyond Copilot, including GPT Actions, LangChain integration, and multi-agent systems
   - *Depth Potential*: Tool-use patterns, chain-of-thought orchestration, error handling in autonomous systems, safety constraints, integration with Obsidian Dataview/Templater/QuickAdd for full automation
   - *Knowledge Graph Role*: Positions Copilot's agentic features within larger landscape of [[AI Agents]], [[Workflow Automation]], and [[Cognitive Augmentation]] systems


```
<thinking>
Let me analyze this request following the ReAct protocol:

**PHASE 1: ANALYZE**

Request Classification:
- Type: comprehensive_note (reference note)
- Scope: reference (exhaustive coverage)
- Research Required: YES - User explicitly requests "most up-to-date information"

The request is for a comprehensive reference note on:
1. Obsidian Copilot plugin (technical tool)
2. Specific focus on prompt engineering with Copilot
3. Requires current/recent information (post-training data)

Structural Planning:
- Information Architecture: 
  - Plugin overview and capabilities
  - Prompt engineering fundamentals in Copilot context
  - Technical configuration and setup
  - Practical prompt strategies
  - Advanced techniques
  - Best practices and workflows
  
- Wiki-Link Opportunities:
  - [[Obsidian]], [[Copilot Plugin]], [[Prompt Engineering]]
  - [[LLM]], [[Context Window]], [[System Prompts]]
  - [[RAG]], [[Semantic Search]], [[Embeddings]]
  - [[Chain-of-Thought]], [[Few-Shot Learning]]
  
- Callout Strategy:
  - [!definition] for key concepts
  - [!methodology-and-sources] for techniques
  - [!example] for concrete prompt examples
  - [!helpful-tip] for best practices
  - [!warning] for common pitfalls
  
- Metadata Planning:
  - Tags: #obsidian #copilot-plugin #prompt-engineering #llm-integration #reference-note
  - Aliases: [Copilot Prompting, Obsidian Copilot Prompts, Copilot PE]

**RESEARCH TRIGGER CRITERIA MET:**
✓ Topic involves potentially recent plugin updates
✓ User explicitly requests current information
✓ Answering requires verification of current features and best practices
✓ Complex synthesis needs authoritative sources

I need to conduct systematic web research on:
1. Obsidian Copilot plugin current features
2. Prompt engineering capabilities specific to Copilot
3. Best practices and documentation
4. Integration patterns and workflows
5. Advanced techniques and configurations

Let me begin the research phase.
</thinking>
```

```
I'll create a comprehensive reference note on Prompt Engineering with Obsidian Copilot. Let me first conduct thorough research to ensure the information is current and accurate.Now I have comprehensive research data. Let me create the exhaustive reference note on Prompt Engineering with Obsidian Copilot.
```