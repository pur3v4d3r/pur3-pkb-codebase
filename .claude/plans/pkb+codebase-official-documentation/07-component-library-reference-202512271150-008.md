---
title: SPES Component Library Reference
document_type: reference
tier: 1
priority: critical
version: 2.0.0
status: published
prerequisites: ["System Architecture Overview", "Design Philosophy"]
estimated_reading_time: 75-90 minutes
last_updated: 2025-12-25
---

# SPES Component Library Reference

**Version**: 2.0.0  
**Document Type**: Comprehensive Reference  
**Audience**: Prompt engineers, workflow designers, contributors  
**Purpose**: Complete guide to SPES component types, structure, and usage

---

## Table of Contents

1. [Component System Overview](#1-component-system-overview)
2. [Component Types](#2-component-types)
3. [Metadata Specification](#3-metadata-specification)
4. [Component Catalog](#4-component-catalog)
5. [Composition Patterns](#5-composition-patterns)
6. [Versioning & Lifecycle](#6-versioning--lifecycle)
7. [Creating Components](#7-creating-components)
8. [Testing Components](#8-testing-components)
9. [Best Practices](#9-best-practices)
10. [Component Index](#10-component-index)

---

## 1. Component System Overview

### 1.1 Philosophy

**Components are atomic, versioned, reusable building blocks for prompt construction.**

**Key Principles**:
- ✅ **Single Responsibility**: Each component does one thing well
- ✅ **Composition**: Complex prompts from simple parts
- ✅ **Versioning**: Components evolve without breaking existing workflows
- ✅ **Reusability**: Write once, use everywhere
- ✅ **Testability**: Components can be validated independently

### 1.2 Component Taxonomy

```
Components
├── Instructions
│   ├── Task-Specific (code generation, text analysis)
│   ├── Meta-Instructions (quality requirements)
│   └── Behavioral (tone, style, approach)
│
├── Personas
│   ├── Domain Experts (Python expert, researcher)
│   ├── Role-Based (teacher, analyst, critic)
│   └── Composite (expert + role)
│
├── Output Formats
│   ├── Structured (JSON, YAML, XML)
│   ├── Document Formats (Markdown, LaTeX, HTML)
│   └── Custom Templates
│
├── Constraints
│   ├── Behavioral Boundaries (don't do X)
│   ├── Content Filters (avoid Y)
│   └── Technical Limits (max length, required fields)
│
└── Templates
    ├── Component Templates (for creating new components)
    ├── Workflow Templates (common patterns)
    └── Metadata Templates (frontmatter schemas)
```

### 1.3 File Structure

**Standard Component File**:
```markdown
---
# === METADATA (YAML Frontmatter) ===
title: Short Descriptive Title
type: instruction|persona|format|constraint|template
version: MAJOR.MINOR.PATCH
status: draft|review|published|deprecated
created: YYYY-MM-DD
modified: YYYY-MM-DD
author: Name or Team
tags: [tag1, tag2, tag3]
description: Brief one-line description
llm_compatibility:
  claude: ["sonnet-4", "opus-4"]
  gemini: ["2.0-flash-exp"]
  gpt: ["gpt-4-turbo"]
  local: ["llama3:8b+"]
context_budget: estimated tokens
dependencies: []
supersedes: previous-version (if applicable)
---

# Component Content

[The actual prompt content that will be composed into workflows]

## Usage Notes

[Optional: Guidance on when/how to use this component]

## Examples

[Optional: Example outputs when using this component]

## Tests

[Optional: Test cases for validation]
```

---

## 2. Component Types

### 2.1 Instructions

**Purpose**: Define what the LLM should do

**When to Use**: Every workflow needs at least one instruction

**Structure**:
```markdown
---
title: Instruction - [Task Name]
type: instruction
version: 1.0.0
---

# Task Definition

You will [specific task description].

Your goal is to [desired outcome].

# Approach

Follow this process:
1. [Step 1]
2. [Step 2]
3. [Step 3]

# Quality Requirements

Your output must:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]
```

**Example - Code Generation**:
```markdown
---
title: Instruction - Generate Python Code
type: instruction
version: 2.1.0
status: published
created: 2024-11-15
modified: 2025-01-10
tags: [code-generation, python, instruction]
llm_compatibility:
  claude: ["sonnet-4", "opus-4"]
  gpt: ["gpt-4-turbo"]
  local: ["codellama:13b+"]
context_budget: 500
---

# Code Generation Task

You will generate Python code based on the user's requirements.

Your goal is to produce clean, efficient, well-documented Python code that solves the specified problem.

# Approach

1. **Understand Requirements**: Analyze the user's request to identify core functionality needed
2. **Design Solution**: Outline the approach before writing code
3. **Implement**: Write the code following Python best practices
4. **Document**: Add docstrings and inline comments
5. **Test**: Include example usage or test cases

# Code Quality Standards

Your code must:
- Follow PEP 8 style guidelines
- Include type hints for function signatures
- Have descriptive variable and function names
- Include docstrings for all functions and classes
- Handle errors appropriately
- Be efficient and readable

# Output Structure

Provide:
1. Code implementation
2. Brief explanation of approach
3. Example usage
4. Any assumptions or limitations
```

**Example - Text Analysis**:
```markdown
---
title: Instruction - Analyze Text Sentiment
type: instruction
version: 1.0.0
status: published
tags: [text-analysis, nlp, sentiment]
llm_compatibility:
  claude: ["sonnet-4", "opus-4"]
  gemini: ["2.0-flash-exp"]
  gpt: ["gpt-4-turbo"]
context_budget: 300
---

# Sentiment Analysis Task

You will analyze the sentiment of provided text and classify it as positive, negative, or neutral.

# Analysis Process

1. **Read Carefully**: Understand the full context of the text
2. **Identify Indicators**: Note words, phrases, and tone that indicate sentiment
3. **Classify**: Determine overall sentiment (positive/negative/neutral)
4. **Explain**: Provide brief justification for classification
5. **Rate Confidence**: Indicate your confidence level (high/medium/low)

# Output Requirements

Provide:
- **Sentiment**: positive | negative | neutral
- **Confidence**: high | medium | low
- **Justification**: 1-2 sentence explanation
- **Key Indicators**: 2-3 specific words/phrases that influenced decision
```

### 2.2 Personas

**Purpose**: Define who the LLM is (role, expertise, communication style)

**When to Use**: When specific expertise or perspective is needed

**Structure**:
```markdown
---
title: Persona - [Role/Expertise]
type: persona
version: 1.0.0
---

# Identity

You are a [role/profession] with [expertise description].

# Background

[Relevant experience, training, perspective]

# Communication Style

[How you communicate, explain, interact]

# Values & Priorities

[What you prioritize in your work]
```

**Example - Python Expert**:
```markdown
---
title: Persona - Python Expert Developer
type: persona
version: 2.0.0
status: published
tags: [programming, python, expert]
llm_compatibility:
  claude: ["sonnet-4", "opus-4"]
  gpt: ["gpt-4-turbo"]
  local: ["codellama:13b+"]
context_budget: 400
---

# Identity

You are a senior Python developer with 10+ years of professional experience building production systems.

# Expertise

Your areas of deep knowledge include:
- **Language Mastery**: Pythonic idioms, advanced features, performance optimization
- **Standard Library**: Comprehensive knowledge of built-in modules
- **Best Practices**: PEP 8, type hints, testing, documentation
- **Frameworks**: Django, Flask, FastAPI, asyncio
- **Tools**: pytest, mypy, black, ruff, poetry
- **Architecture**: Design patterns, SOLID principles, clean code

# Communication Style

You explain concepts clearly with:
- Concrete code examples
- Step-by-step reasoning
- Trade-off analysis when multiple approaches exist
- References to official documentation
- Practical production considerations

# Values

You prioritize:
1. **Readability**: Code is read more than written
2. **Maintainability**: Future developers (including future-you) matter
3. **Testing**: Automated tests prevent regressions
4. **Performance**: But only optimize after measuring
5. **Simplicity**: Simple solutions over clever ones
```

**Example - Technical Writer**:
```markdown
---
title: Persona - Technical Documentation Writer
type: persona
version: 1.0.0
status: published
tags: [documentation, technical-writing]
llm_compatibility:
  claude: ["sonnet-4", "opus-4"]
  gemini: ["2.0-flash-exp"]
context_budget: 350
---

# Identity

You are a professional technical writer specializing in developer documentation.

# Expertise

Your skills include:
- **Clarity**: Complex concepts explained simply
- **Structure**: Well-organized, scannable documents
- **Audience Awareness**: Adapting tone and depth to reader expertise
- **Examples**: Concrete, runnable code samples
- **Completeness**: Covering edge cases and common issues

# Communication Style

Your writing is:
- **Direct**: No unnecessary words
- **Progressive**: Simple to complex
- **Practical**: Always include examples
- **Accessible**: No unexplained jargon
- **Formatted**: Headers, lists, code blocks for readability

# Documentation Principles

1. **User-First**: Write for readers, not yourself
2. **Show + Tell**: Code examples + explanations
3. **Test Everything**: All examples must work
4. **Keep Updated**: Documentation rots quickly
5. **Cross-Reference**: Link related concepts
```

### 2.3 Output Formats

**Purpose**: Specify how the LLM should structure its response

**When to Use**: When you need consistent, structured output

**Structure**:
```markdown
---
title: Format - [Format Name]
type: format
version: 1.0.0
---

# Output Structure

Your response must follow this exact format:

[Template or specification]

# Formatting Rules

[Specific requirements for formatting]

# Example Output

[Concrete example showing expected format]
```

**Example - JSON Output**:
```markdown
---
title: Format - Structured JSON Response
type: format
version: 1.0.0
status: published
tags: [json, structured-output]
llm_compatibility:
  claude: ["sonnet-4", "opus-4"]
  gemini: ["2.0-flash-exp"]
  gpt: ["gpt-4-turbo"]
context_budget: 300
---

# Output Structure

Provide your response as valid JSON following this schema:

```json
{
  "result": "<primary result or answer>",
  "confidence": "<high|medium|low>",
  "reasoning": "<brief explanation of approach>",
  "sources": ["<source 1>", "<source 2>"],
  "metadata": {
    "processing_time_estimate": "<approximate time to complete>",
    "complexity": "<simple|moderate|complex>"
  }
}
```

# Formatting Rules

1. **Valid JSON**: Response must be parseable JSON
2. **No Additional Text**: Only the JSON object, no preamble or explanation outside it
3. **Required Fields**: All fields shown above are required
4. **String Values**: Use double quotes for strings
5. **Arrays**: Empty arrays allowed if no items

# Example Output

```json
{
  "result": "The quick brown fox jumps over the lazy dog",
  "confidence": "high",
  "reasoning": "Classic pangram containing all 26 letters of the English alphabet",
  "sources": ["common knowledge", "typography reference"],
  "metadata": {
    "processing_time_estimate": "instant",
    "complexity": "simple"
  }
}
```
```

**Example - Markdown Document**:
```markdown
---
title: Format - Obsidian Note Format
type: format
version: 1.5.0
status: published
tags: [markdown, obsidian, pkb]
llm_compatibility:
  claude: ["sonnet-4", "opus-4"]
context_budget: 400
---

# Output Structure

Generate an Obsidian-compatible markdown note following this structure:

```markdown
---
tags: [relevant, tags]
aliases: [Alternative Names]
created: YYYY-MM-DD
---

# Note Title

> [!abstract] Summary
> Brief overview of the note's content

## Main Content

[Content organized with clear headers]

### Subsection

[Detailed information with examples]

## Key Concepts

- [[Wiki Link 1]]: Brief description
- [[Wiki Link 2]]: Brief description

## Related Notes

- [[Related Note 1]]
- [[Related Note 2]]

## References

1. Source 1
2. Source 2
```

# Formatting Requirements

1. **YAML Frontmatter**: Always include tags and created date
2. **Wiki Links**: Use [[Note Title]] format for internal links
3. **Callouts**: Use Obsidian callout syntax for special sections
4. **Headers**: Use proper hierarchy (# → ## → ###)
5. **Lists**: Use `-` for unordered, `1.` for ordered
6. **No HTML**: Use markdown only (except for advanced features)

# Best Practices

- **Atomic**: Focus on one concept per note
- **Linked**: Include 5-15 wiki-links to related concepts
- **Tagged**: Use 3-5 relevant tags
- **Structured**: Use consistent header organization
- **Scannable**: Short paragraphs, clear headers
```

**Example - Code Comment Format**:
```markdown
---
title: Format - Python Docstring Standard
type: format
version: 1.0.0
status: published
tags: [python, documentation, code]
context_budget: 350
---

# Docstring Format

Use Google-style Python docstrings:

```python
def function_name(param1: Type1, param2: Type2) -> ReturnType:
    """Brief one-line description.
    
    Longer description if needed, explaining the function's purpose,
    approach, and any important details.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When param1 is invalid
        TypeError: When param2 is wrong type
    
    Example:
        >>> function_name("test", 42)
        expected_output
    """
    pass
```

# Formatting Rules

1. **First Line**: Brief description (imperative mood)
2. **Blank Line**: After first line if multi-line
3. **Args Section**: One line per parameter
4. **Returns**: Describe return value
5. **Raises**: List possible exceptions
6. **Example**: Include if helpful

# Type Hints

Always include type hints in function signature, not docstring.
```

### 2.4 Constraints

**Purpose**: Define boundaries, limitations, and prohibited behaviors

**When to Use**: To prevent unwanted outputs or enforce requirements

**Structure**:
```markdown
---
title: Constraint - [Constraint Name]
type: constraint
version: 1.0.0
---

# Boundaries

DO NOT:
- [Prohibited action 1]
- [Prohibited action 2]

REQUIRED:
- [Required action 1]
- [Required action 2]

# Scope

This constraint applies to [scope description].
```

**Example - Code Safety**:
```markdown
---
title: Constraint - Secure Code Requirements
type: constraint
version: 2.0.0
status: published
tags: [security, code-safety]
llm_compatibility:
  claude: ["sonnet-4", "opus-4"]
  gpt: ["gpt-4-turbo"]
context_budget: 400
---

# Security Requirements

Your code MUST:
- ✅ Validate all user inputs
- ✅ Use parameterized queries (no SQL string concatenation)
- ✅ Handle errors gracefully (no stack traces to users)
- ✅ Use secure random generators for security-critical operations
- ✅ Follow principle of least privilege

# Prohibited Patterns

Your code MUST NOT:
- ❌ Use `eval()` or `exec()` on user input
- ❌ Store passwords in plaintext
- ❌ Use hardcoded secrets or API keys
- ❌ Disable security features (e.g., SSL verification)
- ❌ Trust user input without validation
- ❌ Use deprecated cryptographic functions

# Input Validation

ALL user inputs must be:
1. Type-checked
2. Range-checked (for numbers)
3. Length-limited (for strings)
4. Sanitized (for special characters)
5. Validated against allowed values (when applicable)

# Example - Secure vs. Insecure

❌ **Insecure**:
```python
query = f"SELECT * FROM users WHERE id = {user_input}"
cursor.execute(query)
```

✅ **Secure**:
```python
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_input,))
```
```

**Example - Content Filter**:
```markdown
---
title: Constraint - Family-Friendly Content
type: constraint
version: 1.0.0
status: published
tags: [content-filter, safety]
context_budget: 250
---

# Content Requirements

Generated content MUST be:
- ✅ Appropriate for all ages
- ✅ Respectful and inclusive
- ✅ Free from profanity
- ✅ Non-violent
- ✅ Educational or constructive

# Prohibited Content

DO NOT generate content that:
- ❌ Contains profanity or vulgar language
- ❌ Depicts violence or gore
- ❌ Includes sexual or romantic themes
- ❌ Promotes harmful behaviors
- ❌ Contains discriminatory language
- ❌ Discusses controversial political topics

# When Unsure

If a request seems borderline:
1. Err on the side of caution
2. Explain why you're being careful
3. Offer a family-friendly alternative
```

### 2.5 Templates

**Purpose**: Provide reusable structures for creating new components or content

**When to Use**: To standardize component creation or document generation

**Example - Component Template**:
```markdown
---
title: Template - New Instruction Component
type: template
version: 1.0.0
status: published
tags: [template, meta]
---

# Component Creation Template

Use this template when creating new instruction components:

```markdown
---
title: Instruction - [Descriptive Name]
type: instruction
version: 1.0.0
status: draft
created: {{date:YYYY-MM-DD}}
modified: {{date:YYYY-MM-DD}}
author: {{author}}
tags: [instruction, {{domain}}, {{task-type}}]
description: {{one-line-description}}
llm_compatibility:
  claude: ["sonnet-4"]
  gemini: []
  gpt: []
  local: []
context_budget: {{estimated-tokens}}
dependencies: []
---

# Task Definition

You will {{task-description}}.

Your goal is to {{desired-outcome}}.

# Approach

Follow this process:
1. {{step-1}}
2. {{step-2}}
3. {{step-3}}

# Quality Requirements

Your output must:
- {{requirement-1}}
- {{requirement-2}}
- {{requirement-3}}

## Usage Notes

Use this component when {{usage-scenario}}.

## Tests

```yaml
- input: {{test-input}}
  expected_output_contains: [{{keyword-1}}, {{keyword-2}}]
```
```

# Instructions

1. Replace all {{placeholders}} with actual values
2. Delete unused sections
3. Test the component before publishing
4. Set status to 'review' when ready
```

---

## 3. Metadata Specification

### 3.1 Required Fields

```yaml
title: string (50-100 chars)
  Format: "Type - Descriptive Name"
  Example: "Instruction - Generate Python Code"

type: enum
  Values: instruction | persona | format | constraint | template

version: semver
  Format: MAJOR.MINOR.PATCH
  Example: "2.1.0"

status: enum
  Values: draft | review | published | deprecated
```

### 3.2 Recommended Fields

```yaml
created: date
  Format: YYYY-MM-DD
  Example: "2025-01-15"

modified: date
  Format: YYYY-MM-DD
  Auto-updated on changes

author: string
  Format: Name or Team
  Example: "AI Systems Team"

tags: array of strings
  Minimum: 2-3 tags
  Maximum: 7-8 tags
  Format: [domain, task-type, modifiers]

description: string (100-200 chars)
  One-line summary of component purpose
```

### 3.3 Optional Fields

```yaml
llm_compatibility: object
  Specify which LLMs work best with this component
  Example:
    claude: ["sonnet-4", "opus-4"]
    gemini: ["2.0-flash-exp"]
    gpt: ["gpt-4-turbo"]
    local: ["codellama:13b+"]

context_budget: integer
  Estimated tokens consumed by this component
  Example: 500

dependencies: array of strings
  Other components this depends on
  Example: ["persona-python-expert-v1.0.0"]

supersedes: string
  Previous version this replaces
  Example: "instruction-code-gen-v1.5.0"

test_cases: array
  Validation tests for component
```

---

## 4. Component Catalog

### 4.1 Core Instructions

| Component | Version | Purpose | Context Budget |
|-----------|---------|---------|----------------|
| `instruction-code-generation-v2.0.0` | 2.0.0 | Generate code from requirements | 500 |
| `instruction-text-analysis-v1.0.0` | 1.0.0 | Analyze text (sentiment, themes) | 300 |
| `instruction-data-extraction-v1.0.0` | 1.0.0 | Extract structured data from text | 350 |
| `instruction-summarization-v1.5.0` | 1.5.0 | Summarize documents | 400 |
| `instruction-question-answering-v1.0.0` | 1.0.0 | Answer questions from context | 300 |
| `instruction-translation-v1.0.0` | 1.0.0 | Translate between languages | 250 |
| `instruction-creative-writing-v1.0.0` | 1.0.0 | Generate creative content | 350 |

### 4.2 Core Personas

| Component | Version | Expertise | Context Budget |
|-----------|---------|-----------|----------------|
| `persona-python-expert-v2.0.0` | 2.0.0 | Python development | 400 |
| `persona-technical-writer-v1.0.0` | 1.0.0 | Documentation | 350 |
| `persona-data-scientist-v1.0.0` | 1.0.0 | Data analysis & ML | 450 |
| `persona-researcher-v1.0.0` | 1.0.0 | Academic research | 400 |
| `persona-educator-v1.0.0` | 1.0.0 | Teaching & explanation | 350 |

### 4.3 Core Formats

| Component | Version | Output Type | Context Budget |
|-----------|---------|-------------|----------------|
| `format-json-structured-v1.0.0` | 1.0.0 | JSON objects | 300 |
| `format-markdown-document-v1.0.0` | 1.0.0 | Markdown docs | 350 |
| `format-obsidian-note-v1.5.0` | 1.5.0 | Obsidian PKB notes | 400 |
| `format-code-comments-v1.0.0` | 1.0.0 | Code documentation | 350 |
| `format-yaml-config-v1.0.0` | 1.0.0 | YAML configuration | 250 |

### 4.4 Core Constraints

| Component | Version | Purpose | Context Budget |
|-----------|---------|---------|----------------|
| `constraint-secure-code-v2.0.0` | 2.0.0 | Security requirements | 400 |
| `constraint-family-friendly-v1.0.0` | 1.0.0 | Content filtering | 250 |
| `constraint-max-length-v1.0.0` | 1.0.0 | Output length limits | 150 |
| `constraint-no-external-refs-v1.0.0` | 1.0.0 | Self-contained outputs | 200 |

---

## 5. Composition Patterns

### 5.1 Basic Composition

**Minimal (Instruction Only)**:
```python
prompt = load_component("instruction-code-generation-v2.0.0")
```

**Standard (Instruction + Format)**:
```python
prompt = compose([
    load_component("instruction-code-generation-v2.0.0"),
    load_component("format-code-comments-v1.0.0")
])
```

### 5.2 Full Composition

**Complete Stack**:
```python
prompt = compose([
    load_component("instruction-code-generation-v2.0.0"),  # What to do
    load_component("persona-python-expert-v2.0.0"),        # Who does it
    load_component("format-code-comments-v1.0.0"),         # How to format
    load_component("constraint-secure-code-v2.0.0")        # Boundaries
])
```

### 5.3 Composition Order

**Recommended Order**:
```
1. System-level instructions (if any)
2. Persona
3. Task instruction
4. Constraints
5. Output format
6. Context/data
7. Final directives
```

**Example**:
```python
sections = [
    # System
    "You are an AI assistant helping with software development.",
    
    # Persona
    load_component("persona-python-expert-v2.0.0"),
    
    # Instruction
    load_component("instruction-code-generation-v2.0.0"),
    
    # Constraints
    load_component("constraint-secure-code-v2.0.0"),
    
    # Format
    load_component("format-code-comments-v1.0.0"),
    
    # Context
    f"User requirements:\n{user_input}",
    
    # Final directive
    "Generate the code now."
]

final_prompt = "\n\n".join(sections)
```

---

## 6. Versioning & Lifecycle

### 6.1 Semantic Versioning

```yaml
MAJOR.MINOR.PATCH

MAJOR: Breaking changes
  - Changed component behavior
  - Removed features
  - Incompatible with previous version
  Example: 1.5.0 → 2.0.0

MINOR: New features (backward compatible)
  - Added optional sections
  - Enhanced capabilities
  - Still works with existing workflows
  Example: 1.5.0 → 1.6.0

PATCH: Bug fixes (backward compatible)
  - Fixed typos
  - Clarified wording
  - No behavior changes
  Example: 1.5.0 → 1.5.1
```

### 6.2 Lifecycle States

```yaml
draft:
  - Initial creation
  - Still being refined
  - Not ready for production
  - May change significantly

review:
  - Content finalized
  - Awaiting validation
  - Testing in progress
  - May have minor changes

published:
  - Production-ready
  - Tested and validated
  - Immutable (new version for changes)
  - Recommended for use

deprecated:
  - Superseded by newer version
  - Still functional
  - Use newer version for new workflows
  - Will be removed in future

archived:
  - No longer available
  - Historical record only
  - Migration guide provided
```

---

## 7. Creating Components

### 7.1 Component Creation Checklist

```yaml
Pre-Creation:
  - [ ] Identify clear, single purpose
  - [ ] Check if existing component exists
  - [ ] Determine component type
  - [ ] Plan metadata (tags, compatibility)

Creation:
  - [ ] Use appropriate template
  - [ ] Write clear, concise content
  - [ ] Include usage notes
  - [ ] Add test cases
  - [ ] Estimate context budget

Review:
  - [ ] Test with target LLMs
  - [ ] Verify metadata completeness
  - [ ] Check for typos/errors
  - [ ] Validate against similar components
  - [ ] Get peer review

Publishing:
  - [ ] Set status to 'published'
  - [ ] Add to component index
  - [ ] Update documentation
  - [ ] Announce to users
```

### 7.2 Writing Guidelines

**DO**:
- ✅ Be specific and concrete
- ✅ Use imperative mood ("Generate code", not "You should generate code")
- ✅ Include examples where helpful
- ✅ Keep it focused and atomic
- ✅ Test before publishing

**DON'T**:
- ❌ Be vague or ambiguous
- ❌ Include multiple purposes
- ❌ Use overly complex language
- ❌ Assume context not provided
- ❌ Skip testing

---

## 8. Testing Components

### 8.1 Test Structure

```yaml
# In component metadata
test_cases:
  - name: Basic functionality
    input: "Generate a hello world function"
    expected_output_contains:
      - "def hello"
      - "print"
      - "Hello"
    llm: claude-sonnet-4
  
  - name: Edge case handling
    input: "Generate code with no requirements"
    expected_behavior: "Asks for clarification"
    llm: claude-sonnet-4
```

### 8.2 Validation Script

```python
def test_component(component_id: str, test_cases: list):
    """Test component against defined test cases."""
    
    component = load_component(component_id)
    results = []
    
    for test in test_cases:
        prompt = compose([component, test['input']])
        response = llm_generate(prompt, test['llm'])
        
        passed = True
        for expected in test.get('expected_output_contains', []):
            if expected.lower() not in response.lower():
                passed = False
        
        results.append({
            'test_name': test['name'],
            'passed': passed,
            'response': response
        })
    
    return results
```

---

## 9. Best Practices

### 9.1 Component Design

**Single Responsibility**:
```yaml
✅ Good:
  - instruction-generate-code-v1.0.0
  - instruction-add-comments-v1.0.0
  - instruction-write-tests-v1.0.0

❌ Bad:
  - instruction-generate-code-with-comments-and-tests-v1.0.0
  # Too much in one component
```

**Clear Naming**:
```yaml
Format: type-description-version
Good: instruction-analyze-sentiment-v1.0.0
Bad: my-cool-instruction-v1
```

**Context Budget**:
```yaml
Aim for:
  Instructions: 300-600 tokens
  Personas: 300-500 tokens
  Formats: 200-400 tokens
  Constraints: 200-400 tokens

Avoid:
  Mega-components: >1000 tokens
  Tiny components: <100 tokens (unless specific reason)
```

### 9.2 Reusability

**Make Components Generic**:
```yaml
❌ Too Specific:
  "Generate a Python Flask API endpoint for user authentication"

✅ Generic & Reusable:
  "Generate an API endpoint based on requirements"
  # Can be used for any framework, any endpoint
```

**Parameterize When Possible**:
```markdown
Instead of hardcoding:
  "Maximum response length: 500 words"

Allow configuration:
  "Maximum response length: {{max_length}} words"
```

---

## 10. Component Index

### 10.1 Quick Reference

**By Task**:
```yaml
Code Generation:
  - instruction-code-generation-v2.0.0
  - persona-python-expert-v2.0.0
  - format-code-comments-v1.0.0
  - constraint-secure-code-v2.0.0

Text Analysis:
  - instruction-text-analysis-v1.0.0
  - instruction-sentiment-analysis-v1.0.0
  - format-json-structured-v1.0.0

Documentation:
  - instruction-write-documentation-v1.0.0
  - persona-technical-writer-v1.0.0
  - format-markdown-document-v1.0.0

Knowledge Management:
  - instruction-create-pkb-note-v1.0.0
  - format-obsidian-note-v1.5.0
  - constraint-atomic-notes-v1.0.0
```

**By LLM Compatibility**:
```yaml
Optimized for Claude:
  - All components (primary target)

Optimized for Gemini:
  - instruction-fast-analysis-v1.0.0
  - instruction-batch-processing-v1.0.0

Optimized for Local LLMs:
  - instruction-simple-code-v1.0.0
  - format-minimal-json-v1.0.0
  # Smaller context budgets
```

---

## Conclusion

The SPES Component Library provides a robust, flexible foundation for prompt engineering through:

✅ **Atomic Components**: Single-purpose, reusable building blocks  
✅ **Semantic Versioning**: Stable evolution without breaking changes  
✅ **Clear Metadata**: Rich information for discovery and usage  
✅ **Composition Patterns**: Combine components for complex tasks  
✅ **Quality Standards**: Testing and validation built-in  

**Next Steps**:
1. Browse the [Component Catalog](#4-component-catalog)
2. Try [Basic Composition](#51-basic-composition) patterns
3. Create your first component using [Templates](#25-templates)
4. Contribute to the library following [Best Practices](#9-best-practices)
