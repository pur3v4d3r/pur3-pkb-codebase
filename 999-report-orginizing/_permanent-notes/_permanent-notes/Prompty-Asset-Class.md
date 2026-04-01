---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Prompty Asset Class"
aliases:
  - "Prompty Asset Class"
  - "PAC"
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
  - type/reference
  - source/claude-sonnet
  - maturity/seedling
  - confidence/provisional
  - status/read
  - priority/low
  - year/2025
  - advanced-prompting/multi-modal
  - information-architecture
  - prompt-engineering

domain: other
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-04-01
updated: 2026-04-01

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "reference-comprehensive-prompty-exstenion-for-vs-code-2025122805"
evidence-quality: medium
extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"
pipeline-version: "2.1.0"
extraction-date: "2026-04-01"

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
  - "[[Comprehensive-Reference-Prompty-Exstension-for-VS-Code|**Comprehensive Reference: Prompty Exstension for VS Code**]]"
  - "[[OpenAI]]"
  - "[[Azure-OpenAI|Azure OpenAI]]"
  - "[[Anthropic]]"
  - "[[Claude-Code|Claude Code]]"
  - "[[Gemini-Code-Assist|Gemini Code Assist]]"
  - "[[LangChain]]"
  - "[[Semantic-Kernel|Semantic Kernel]]"
  - "[[Prompt-Flow|Prompt Flow]]"
  - "[[Google]]"
  - "[[Cohere]]"
  - "[[Mistral]]"
  - "[[Groq]]"
  - "[[LiteLLM]]"

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

# Prompty Asset Class

> [!definition] **Prompty Asset Class** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> [**Prompty**:: a file format specification (`.prompty`) and VS Code extension designed to enhance observability, understandability, and portability for LLM prompt development by unifying prompt content, execution context, and sample data in a single version-controlled markdown asset.]^verified-stable

## Core Explanation

> [!analytical-insight] Key Insight *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> **Central Principle**  
> The selection of a scripting platform should be driven by the specific task, the target environment, and the required performance characteristics.^verified-stable

## Practical Implications

> [!example] **Application**
> *Describe how this concept applies in practice.*

> [!warning] **Key Distinction** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> <span style='color: #FF00DC;'>**Prompty officially supports ONLY:**</span>
> - [[OpenAI]] (direct API)
> - [[Azure OpenAI]] (Azure deployment)
> - **Serverless** (GitHub Marketplace models)
> 
> <span style='color: #FF00DC;'>**NOT supported:**</span>
> - [[Anthropic]] (Claude models)
> - [[Google]] (Gemini models)
> - [[Cohere]], [[Mistral]], [[Groq]], etc.

> [!warning] **Key Distinction** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> This approach adds <span style='color: #FF00DC;'>infrastructure complexity</span> and may not support all Prompty features (preview, tracing). Consider whether simpler approaches (direct API calls, alternative tools) better serve your workflow.

> [!warning] **Key Distinction** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> **Critical Constraints**  
> - Security risks from untrusted scripts  
> - Platform-specific dependencies and compatibility  
> - Performance bottlenecks in interpreted environments^contested-active

> [!warning] **Key Distinction** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> **Next Review**: `= this.next-review` | **Review Count**: `= this.review-count`
> **Review Status**: `= choice(this.next-review < date(today), "🔴 OVERDUE", choice(this.next-review = date(today), "🟡 Due Today", choice(dateformat(this.next-review, "yyyy-MM-dd") <= dateformat(date(today) + dur(7 days), "yyyy-MM-dd"), "🟢 This Week", "⚪ Scheduled")))`
> **Days Until Review**: `= choice(this.next-review, (this.next-review - date(today)).days + " days", "Not scheduled")`

## Reflection Prompts

> [!reflection] **Reflect** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> **Reflective Questions for Personal Application**  
> *First Reflection*: What repetitive PKM tasks could you automate today using one of these platforms? How would that change your workflow?  
> *Second Reflection*: How might you design a modular PKM system where scripts act as interchangeable components, each handling a specific layer of automation?

## Concrete Examples

> [!example] **Multi-Modal Input Support** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> Prompty supports <span style='color: #72FFF1;'>images and other media</span> through Jinja2 template extensions, useful for vision-capable models like GPT-4o or Claude 3.5 Sonnet (if using proxy).

> [!example] **Git Workflow Pattern** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> ```bash
> # Create feature branch for prompt iteration
> git checkout -b prompts/improve-customer-support
> 
> # Edit basic.prompty, test iterations
> # Commit when satisfied with results
> git add prompts/customer-support.prompty
> git commit -m "Improve customer support prompt tone and structure"
> 
> # Push for team review
> git push origin prompts/improve-customer-support
> ```

> [!example] **Modified .prompty for Non-OpenAI Providers** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> Create a custom frontmatter field to document target provider:
> 
> ```yaml
> ---
> name: Code Review Assistant
> provider: anthropic                    # Custom field
> model_id: claude-sonnet-4-5-20250929  # Custom field
> execution: manual                      # Custom field: manual | api | cli
> 
> model:
>   api: chat
>   configuration:
>     # Leave as template - won't execute via Prompty
>     type: openai_compatible
>   parameters:
>     max_tokens: 4000
>     temperature: 0.3
> 
> sample:
>   code: |
>     def example():
>         pass
> ---
> # System
> You are an expert code reviewer...
> ```

## Connections & Context

**Cross-report connections** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*:
- [[Prompt-Engineering|Prompt Engineering]]
- [[Version-Control|Version Control]]
- [[Markdown]]
- [[Jinja2]]
- [[Claude-Code|Claude Code]]
- [[Obsidian]]
- [[LLM-Development-Tools|LLM Development Tools]]
- [[YAML]]

**Cross-report connections** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*:
- [[#Technical-Specifications|#Technical Specifications]]
- [[#Implementation-&-Application|#Implementation & Application]]

**Cross-report connections** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*:
- [[First-Principles|First Principles]]
- [[Systems-Thinking|Systems Thinking]]
- [[Second-Order-Effects|Second-Order Effects]]
- [[Constraint-Theory|Constraint Theory]]
- [[Mental-Models|Mental Models]]

**Related concepts:**
[[Comprehensive-Reference-Prompty-Exstension-for-VS-Code|**Comprehensive Reference: Prompty Exstension for VS Code**]] · [[OpenAI]] · [[Azure-OpenAI|Azure OpenAI]] · [[Anthropic]] · [[Claude-Code|Claude Code]] · [[Gemini-Code-Assist|Gemini Code Assist]] · [[LangChain]] · [[Semantic-Kernel|Semantic Kernel]] · [[Prompt-Flow|Prompt Flow]] · [[Prompt-Flow|Prompt Flow]] · [[LangChain]] · [[Semantic-Kernel|Semantic Kernel]] · [[OpenAI]] · [[Azure-OpenAI|Azure OpenAI]] · [[Anthropic]] · [[Google]] · [[Cohere]] · [[Mistral]] · [[Groq]] · [[LiteLLM]] · [[Claude-Code|Claude Code]] · [[Claude-Code|Claude Code]] · [[Claude-Code|Claude Code]] · [[Gemini-Code-Assist|Gemini Code Assist]] · [[Obsidian]] · [[OpenAI]] · [[Azure-OpenAI|Azure OpenAI]] · [[Claude]] · [[Gemini]] · [[Obsidian]]

**Related concepts** *(from reference-comprehensive-prompty-exstenion-for-vs-code-2025122805.md)*:
[[Claude-Code|Claude Code]] * [[Gemini-Code-Assist|Gemini Code Assist]] * [[Semantic-Kernel|Semantic Kernel]] * [[Prompt-Flow|Prompt Flow]] * [[Dataview|Dataview]] * [[customer-support.prompty|customer-support.prompty]] * [[error-handling.prompty|error-handling.prompty]] * [[escalation.prompty|escalation.prompty]] * [[Prompt-Engineering|Prompt Engineering]] * [[Version-Control|Version Control]] * [[LLM-Development-Tools|LLM Development Tools]] * [[LiteLLM-Unified-API-Gateway|LiteLLM Unified API Gateway]] * [[Prompt-Versioning-&-Git-Workflows|Prompt Versioning & Git Workflows]] * [[Jinja2-Templating-for-Dynamic-Prompts|Jinja2 Templating for Dynamic Prompts]] * [[Python|Python]] * [[LLM|LLM]] * [[Obsidian-+-VS-Code-Dual-Editor-Workflow|Obsidian + VS Code Dual-Editor Workflow]] * [[VS-Code|VS Code]] * [[Prompt-Engineering-Framework-Comparison|Prompt Engineering Framework Comparison]] * [[Claude-Code-vs.-GitHub-Copilot-vs.-Cursor|Claude Code vs. GitHub Copilot vs. Cursor]] * [[PKM-Automation|PKM Automation]] * [[VS-Code-Extensions|VS Code Extensions]] * [[Scripting-Platforms|Scripting Platforms]] * [[Python-for-PKM|Python for PKM]] * [[JavaScript-for-Automation|JavaScript for Automation]] * [[Templating-Systems|Templating Systems]] * [[advanced|advanced]] * [[wiki-links|wiki-links]] * [[Advanced-Scripting-Techniques|Advanced Scripting Techniques]] * [[Historical-Development-of-Scripting-Languages|Historical Development of Scripting Languages]]

**Cross-report connections** *(from reference-comprehensive-prompty-exstenion-for-vs-code-2025122805.md)*:
- [[Prompt-Engineering|Prompt Engineering]]
- [[Version-Control|Version Control]]
- [[Markdown|Markdown]]
- [[Jinja2|Jinja2]]
- [[Claude-Code|Claude Code]]

**Cross-report connections** *(from reference-comprehensive-prompty-exstenion-for-vs-code-2025122805.md)*:
- [[First-Principles|First Principles]]
- [[Systems-Thinking|Systems Thinking]]
- [[Second-Order-Effects|Second-Order Effects]]
- [[Constraint-Theory|Constraint Theory]]
- [[Mental-Models|Mental Models]]




## Methodology Notes

> [!methodology-and-sources] **Configuration Strategy** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> For <span style='color: #27FF00;'>team collaboration</span>: Use workspace-level `settings.json` with environment variable placeholders. For <span style='color: #FFC700;'>personal experimentation</span>: Use user-level settings or inline configuration.

> [!methodology-and-sources] **Iterative Prompt Engineering Cycle** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> Prompty optimizes the <span style='color: #FFC700;'>write → test → observe → refine</span> cycle:
> 
> 1. **Write** prompt in markdown with Jinja2 templates
> 2. **Test** with sample data via live preview
> 3. **Observe** output and verbose API trace
> 4. **Refine** prompt based on results
> 5. **Version** changes in Git
> 6. **Generate** production code when satisfied

> [!methodology-and-sources] **Git + Obsidian + Prompty Workflow** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> 1. **Store** `.prompty` files in Obsidian vault (under version control)
> 2. **Open vault** in VS Code (where Obsidian and Prompty extensions coexist)
> 3. **Edit** prompts using Prompty features (OpenAI) or markdown (others)
> 4. **Commit** changes to Git
> 5. **Link** prompts from Obsidian notes using wiki-links
> 6. **Query** prompt library using Dataview

> [!methodology-and-sources] **Research Methodology** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> **Exploration Tree:** Depth-first across 5 primary dimensions
> 1. Core Functionality & Architecture
> 2. Technical Implementation (file format, Jinja2, execution)
> 3. Workflow Integration (VS Code, version control, providers)
> 4. Practical Applications (best practices, workflows)
> 5. Ecosystem & Tooling (alternatives, complementary tools)
> 
> **Total Searches:** 12 targeted queries
> **Primary Sources:**
> - [Microsoft Prompty GitHub Repository](https://github.com/microsoft/prompty)
> - [Prompty.ai Official Documentation](https://prompty.ai)
> - [VS Code Marketplace…

> [!methodology-and-sources] **Untitled** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> **Practical Framework**  
> 1. Identify the core task (e.g., note generation, data parsing).  
> 2. Match task to scripting platform based on performance and ecosystem.  
> 3. Integrate via CLI, API, or extension system.  
> 4. Automate via scheduled tasks, hooks, or UI triggers.

> [!methodology-and-sources] **Untitled** *(from [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]])*
> **Research Methodology**  
> - Synthesis Approach: Tree-of-Thoughts decomposition  
> - Confidence Level: Per-claim tagging (40–60% density)  
> - Self-Verification: 3 key claims re-validated

---

## Source Attribution

**Extracted from:** [[reference-comprehensive-prompty-exstenion-for-vs-code-2025122805]]
