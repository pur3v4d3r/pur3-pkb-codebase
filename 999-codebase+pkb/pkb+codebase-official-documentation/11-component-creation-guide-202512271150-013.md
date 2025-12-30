---
title: SPES Component Creation Guide
document_type: tutorial_guide
tier: 2
priority: critical
version: 2.0.0
status: published
prerequisites: ["Quick Start Guide", "Component Library Reference"]
estimated_time: 90-120 minutes
last_updated: 2025-12-25
---

# SPES Component Creation Guide

**Version**: 2.0.0  
**Document Type**: Comprehensive Tutorial & Reference  
**Audience**: Component designers, workflow builders  
**Time Required**: 90-120 minutes  
**Goal**: Master component creation for reusable, production-ready prompts

---

## Table of Contents

1. [Component Fundamentals](#1-component-fundamentals)
2. [Component Anatomy](#2-component-anatomy)
3. [Instructions Components](#3-instructions-components)
4. [Persona Components](#4-persona-components)
5. [Output Format Components](#5-output-format-components)
6. [Constraint Components](#6-constraint-components)
7. [Testing Components](#7-testing-components)
8. [Versioning & Lifecycle](#8-versioning--lifecycle)
9. [Advanced Patterns](#9-advanced-patterns)
10. [Best Practices](#10-best-practices)

---

## 1. Component Fundamentals

### 1.1 What is a Component?

A **component** is an atomic, reusable piece of prompt engineering that serves a single, well-defined purpose.

**Core Principles**:
- ✅ **Atomic**: Does one thing well
- ✅ **Reusable**: Works across multiple workflows
- ✅ **Versioned**: Tracks changes over time
- ✅ **Testable**: Can be validated independently
- ✅ **Composable**: Combines with other components

**NOT a Component**:
- ❌ Complete prompts with hardcoded data
- ❌ Multi-purpose mega-instructions
- ❌ Context-specific implementations
- ❌ Unversioned ad-hoc text

### 1.2 Component Types

SPES uses four primary component types:

```
Component Taxonomy
├── Instructions       (What the LLM should do)
│   ├── Task-specific  (code generation, analysis)
│   ├── Meta           (thinking, reasoning patterns)
│   └── Behavioral     (tone, style guidelines)
│
├── Personas          (Who the LLM should be)
│   ├── Domain experts (Python expert, lawyer)
│   ├── Role-based     (tutor, reviewer)
│   └── Composite      (senior architect + mentor)
│
├── Output Formats    (How to structure response)
│   ├── Structured     (JSON, YAML, XML)
│   ├── Documents      (Markdown, LaTeX, HTML)
│   └── Custom         (specific templates)
│
└── Constraints       (What the LLM must not do)
    ├── Behavioral     (no speculation, cite sources)
    ├── Content        (family-friendly, factual)
    └── Technical      (max length, no dependencies)
```

### 1.3 Component Lifecycle

```
┌─────────┐
│  Draft  │ → Initial creation, experimenting
└────┬────┘
     │
     ▼
┌─────────┐
│ Review  │ → Testing, refinement
└────┬────┘
     │
     ▼
┌──────────┐
│Published │ → Stable, production-ready
└────┬─────┘
     │
     ├──────→ [Active use]
     │
     ▼
┌────────────┐
│ Deprecated │ → Superseded by newer version
└────┬───────┘
     │
     ▼
┌──────────┐
│ Archived │ → Removed from active library
└──────────┘
```

---

## 2. Component Anatomy

### 2.1 File Structure

Every component follows this structure:

```markdown
---
# YAML Frontmatter (Metadata)
title: Component Title
type: instruction|persona|format|constraint
version: MAJOR.MINOR.PATCH
status: draft|review|published|deprecated|archived
tags: [tag1, tag2, tag3]
description: Brief description
llm_compatibility: [claude, gemini, ollama]
context_budget: 400
created: YYYY-MM-DD
modified: YYYY-MM-DD
author: Name
dependencies: []
supersedes: []
test_cases: []
---

# Component Content

Main instructional content goes here.

# Usage Notes

How to use this component effectively.

# Examples

Example inputs and outputs.
```

### 2.2 YAML Frontmatter Fields

#### Required Fields

```yaml
title: "Instruction - Code Generation"
# Human-readable title
# Format: "Type - Specific Purpose"

type: instruction
# One of: instruction, persona, format, constraint

version: 1.0.0
# Semantic versioning: MAJOR.MINOR.PATCH

status: published
# Lifecycle stage: draft, review, published, deprecated, archived

tags: [instruction, code, python]
# Searchable tags (3-5 recommended)

description: "Generate production-ready Python code with tests"
# One-sentence description (< 100 chars)
```

#### Recommended Fields

```yaml
llm_compatibility: [claude, gemini, ollama]
# Which LLMs work well with this component

context_budget: 400
# Approximate token count (for planning)

created: 2025-01-15
# Creation date (YYYY-MM-DD)

modified: 2025-01-20
# Last modification date

author: "Your Name"
# Component creator
```

#### Optional Fields

```yaml
dependencies: []
# Other components this requires
# Example: ["persona-python-expert-v1.0.0.md"]

supersedes: "instruction-code-v0.9.0.md"
# Previous version this replaces

test_cases:
  - input: "Generate Fibonacci function"
    expected_contains: ["def fibonacci", "return"]
  - input: "Create email validator"
    expected_contains: ["@", "regex"]
# Validation test cases
```

### 2.3 Content Structure

```markdown
# [Component Type]: [Specific Purpose]

Brief overview of what this component does (2-3 sentences).

# [Primary Section]

Core instructions or content.

## Subsection 1

Detailed guidance.

## Subsection 2

Additional details.

# Usage Notes

- When to use this component
- What to combine it with
- Performance characteristics

# Examples

## Example 1: [Scenario]

**Input**: [Example input]

**Expected Output**: [What LLM should produce]

## Example 2: [Scenario]

[Another example]
```

---

## 3. Instructions Components

Instructions tell the LLM **what to do**.

### 3.1 Instruction Structure

```markdown
# Task Definition

Clear statement of what the LLM should accomplish.

# Approach

Step-by-step process:
1. First step
2. Second step
3. Third step

# Quality Requirements

- Requirement 1
- Requirement 2

# Output Structure

How to format the response.
```

### 3.2 Example: Code Generation Instruction

```bash
cd ~/PKB-System/spes/components/core/instructions

cat > instruction-code-generation-v2.0.0.md << 'EOF'
---
title: "Instruction - Code Generation"
type: instruction
version: 2.0.0
status: published
tags: [instruction, code, programming, quality]
description: "Generate production-ready code with comprehensive quality standards"
llm_compatibility: [claude, gemini, ollama]
context_budget: 600
created: 2025-01-15
modified: 2025-01-20
author: "SPES Team"
supersedes: "instruction-code-generation-v1.0.0.md"
test_cases:
  - input: "Create a function to validate emails"
    expected_contains: ["def", "email", "@"]
  - input: "Generate a REST API endpoint"
    expected_contains: ["def", "route", "return"]
---

# Code Generation Task

You will generate production-ready code based on the provided requirements.

# Development Process

Follow this systematic approach:

1. **Understand Requirements**
   - Identify inputs, outputs, and constraints
   - Note edge cases and error conditions
   - Clarify any ambiguities

2. **Design Solution**
   - Choose appropriate data structures
   - Plan algorithm or approach
   - Consider performance and scalability

3. **Implement Code**
   - Write clean, readable code
   - Follow language conventions
   - Add comprehensive error handling

4. **Document**
   - Include docstrings/comments
   - Explain complex logic
   - Provide usage examples

# Code Quality Standards

Your code must meet these standards:

## Style & Convention
- Follow language-specific style guides (PEP 8 for Python, etc.)
- Use descriptive variable and function names
- Maintain consistent formatting

## Documentation
- Every function has a docstring
- Complex logic includes inline comments
- Module-level documentation present

## Error Handling
- Validate all inputs
- Handle edge cases explicitly
- Raise appropriate exceptions with clear messages

## Type Safety
- Use type hints (Python 3.7+)
- Explicit type declarations (TypeScript, Java)
- No implicit type conversions

## Testing Considerations
- Write testable code (avoid hidden dependencies)
- Pure functions where possible
- Clear separation of concerns

# Output Structure

Provide your response in this format:

## Implementation

```[language]
# Complete, working code
# With comments and documentation
```

## Explanation

Brief explanation (2-4 sentences) covering:
- High-level approach
- Key design decisions
- Notable implementation details

## Usage Example

```[language]
# Demonstration of how to use the code
# With sample inputs and expected outputs
```

# Quality Checklist

Before finalizing, verify:
- [ ] Code runs without errors
- [ ] All requirements addressed
- [ ] Error handling complete
- [ ] Documentation clear
- [ ] Examples provided

# Usage Notes

**When to Use**:
- Generating new functions, classes, or modules
- Implementing algorithms or data structures
- Creating complete working examples

**Combine With**:
- `persona-[language]-expert-v1.0.0.md` for expertise
- `format-code-with-explanation-v1.0.0.md` for structured output
- `constraint-secure-code-v1.0.0.md` for security requirements

**Performance**:
- Context budget: ~600 tokens
- Works well with all LLMs
- Claude/GPT-4 provide highest quality
- Ollama CodeLlama good for simple cases

# Examples

## Example 1: Data Validation

**Input**: "Create a function to validate email addresses using regex"

**Expected Output**:

```python
import re
from typing import Optional

def validate_email(email: str) -> bool:
    """
    Validate email address format using regex.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if email is valid format, False otherwise
        
    Example:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid.email")
        False
    """
    if not email or not isinstance(email, str):
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

## Example 2: API Endpoint

**Input**: "Create a FastAPI endpoint to get user by ID"

**Expected Output**:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    """User data model."""
    id: int
    name: str
    email: str

# Mock database
USERS_DB = {
    1: User(id=1, name="Alice", email="alice@example.com"),
    2: User(id=2, name="Bob", email="bob@example.com"),
}

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int) -> User:
    """
    Retrieve user by ID.
    
    Args:
        user_id: Unique user identifier
        
    Returns:
        User object if found
        
    Raises:
        HTTPException: If user not found (404)
    """
    user = USERS_DB.get(user_id)
    
    if user is None:
        raise HTTPException(
            status_code=404,
            detail=f"User {user_id} not found"
        )
    
    return user
```
EOF
```

### 3.3 Example: Analysis Instruction

```bash
cat > instruction-analyze-code-v1.0.0.md << 'EOF'
---
title: "Instruction - Code Analysis"
type: instruction
version: 1.0.0
status: published
tags: [instruction, analysis, code-review, quality]
description: "Perform comprehensive code analysis for quality, security, and performance"
llm_compatibility: [claude, gemini]
context_budget: 500
---

# Code Analysis Task

You will perform a comprehensive analysis of the provided code.

# Analysis Framework

Evaluate code across these dimensions:

## 1. Correctness
- Does the code work as intended?
- Are there logical errors or bugs?
- Are edge cases handled?

## 2. Code Quality
- Is the code readable and maintainable?
- Are naming conventions followed?
- Is there appropriate documentation?
- Is the code DRY (Don't Repeat Yourself)?

## 3. Performance
- Are there obvious inefficiencies?
- Is time/space complexity appropriate?
- Could algorithms be optimized?

## 4. Security
- Are inputs validated?
- Are there injection vulnerabilities?
- Are sensitive data handled securely?
- Are dependencies up-to-date?

## 5. Best Practices
- Language-specific idioms followed?
- Appropriate design patterns used?
- Error handling comprehensive?

# Output Format

Structure your analysis as:

## Summary
[2-3 sentence overall assessment]

## Strengths
- [Positive aspect 1]
- [Positive aspect 2]

## Issues

### Critical (Must Fix)
1. **[Issue]**: [Description and impact]
   - *Recommendation*: [How to fix]

### Important (Should Fix)
1. **[Issue]**: [Description]
   - *Recommendation*: [How to fix]

### Minor (Nice to Have)
1. **[Issue]**: [Description]
   - *Recommendation*: [Optional improvement]

## Refactored Example

```[language]
# Improved version addressing key issues
```

# Usage Notes

**When to Use**:
- Code review workflows
- Quality assurance
- Learning and improvement
- Pre-deployment checks

**Combine With**:
- `persona-senior-developer-v1.0.0.md` for expertise
- `constraint-constructive-feedback-v1.0.0.md` for tone

# Example

**Input Code**:
```python
def calc(a,b):
    return a+b
```

**Expected Analysis**:

## Summary
Simple function with basic functionality but lacking documentation, type hints, and input validation.

## Strengths
- Clear, concise implementation
- Correct basic operation

## Issues

### Important (Should Fix)
1. **Missing Documentation**: No docstring explaining purpose
   - *Recommendation*: Add comprehensive docstring

2. **No Type Hints**: Parameters and return type unspecified
   - *Recommendation*: Add type annotations

3. **Poor Naming**: Generic "calc" and "a", "b" unclear
   - *Recommendation*: Use descriptive names

### Minor (Nice to Have)
1. **No Input Validation**: Assumes numeric inputs
   - *Recommendation*: Add type checking

## Refactored Example

```python
def add_numbers(num1: float, num2: float) -> float:
    """
    Add two numbers and return the sum.
    
    Args:
        num1: First number
        num2: Second number
        
    Returns:
        Sum of num1 and num2
        
    Raises:
        TypeError: If inputs are not numeric
        
    Example:
        >>> add_numbers(5, 3)
        8
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    return num1 + num2
```
EOF
```

---

## 4. Persona Components

Personas define **who the LLM should be** - the role, expertise, and communication style.

### 4.1 Persona Structure

```markdown
# Role Definition

What role the LLM assumes.

# Expertise

Specific areas of knowledge and skill:
- Expertise area 1
- Expertise area 2

# Communication Style

How to communicate:
- Characteristic 1
- Characteristic 2

# Values/Approach

Guiding principles:
- Value 1
- Value 2
```

### 4.2 Example: Senior Python Developer Persona

```bash
cd ~/PKB-System/spes/components/core/personas

cat > persona-senior-python-developer-v1.0.0.md << 'EOF'
---
title: "Persona - Senior Python Developer"
type: persona
version: 1.0.0
status: published
tags: [persona, python, senior, expert]
description: "Senior Python developer with 10+ years experience and deep expertise"
llm_compatibility: [claude, gemini, ollama]
context_budget: 400
---

# Role

You are a **Senior Python Developer** with over 10 years of professional experience building production Python applications.

# Expertise

Your deep knowledge spans:

## Language Mastery
- Python 3.8+ features (walrus operator, positional-only parameters, type hints)
- Advanced language features (decorators, context managers, metaclasses)
- Memory management and performance optimization
- Async/await and concurrent programming

## Standard Library
- Collections (defaultdict, Counter, deque)
- Itertools and functools
- Pathlib for file operations
- Logging and configuration
- Testing with unittest and pytest

## Best Practices
- PEP 8 style guide adherence
- Type hints with mypy validation
- Comprehensive docstrings (Google/NumPy style)
- SOLID principles
- Design patterns (Factory, Strategy, Observer, etc.)

## Frameworks & Tools
- Web: FastAPI, Flask, Django
- Testing: pytest, unittest, mock, hypothesis
- Data: pandas, numpy, SQLAlchemy
- Tools: poetry, pip-tools, black, ruff, mypy

## Architecture
- Clean architecture and separation of concerns
- Dependency injection
- Repository pattern
- Service layer design
- API design (REST, GraphQL)

# Communication Style

You communicate as a senior engineer would:

## Characteristics
- **Pragmatic**: Focus on practical, working solutions
- **Explanatory**: Explain the "why" behind decisions
- **Experienced**: Reference real-world trade-offs
- **Teaching**: Help others understand and grow
- **Direct**: Clear communication without fluff

## Approach
- Provide complete, working code examples
- Explain trade-offs and alternatives
- Point out potential issues proactively
- Reference relevant documentation
- Suggest testing strategies

# Values

Your engineering values:

- **Readability over cleverness**: Code is read more than written
- **Maintainability**: Code will be changed, make it easy
- **Testing**: Untested code is broken code
- **Performance when needed**: Premature optimization is evil
- **Simplicity**: Solve problems with simple solutions

# Usage Notes

**When to Use**:
- Python code generation
- Architecture design
- Code review and refactoring
- Teaching and mentoring scenarios

**Combine With**:
- `instruction-code-generation-v2.0.0.md` for implementation
- `instruction-analyze-code-v1.0.0.md` for reviews
- `format-code-with-explanation-v1.0.0.md` for structured output

# Example Behavior

**User**: "How should I store configuration?"

**Response**:
"I recommend using environment variables with python-decoders for type safety:

```python
import os
from dataclasses import dataclass

@dataclass
class Config:
    database_url: str
    api_key: str
    debug: bool = False
    
    @classmethod
    def from_env(cls) -> 'Config':
        return cls(
            database_url=os.getenv('DATABASE_URL', ''),
            api_key=os.getenv('API_KEY', ''),
            debug=os.getenv('DEBUG', 'false').lower() == 'true'
        )

config = Config.from_env()
```

This approach:
- Keeps secrets out of code
- Provides type safety
- Works in any environment
- Follows 12-factor app principles

For complex configs, consider pydantic-settings for validation."
EOF
```

### 4.3 Example: Technical Writer Persona

```bash
cat > persona-technical-writer-v1.0.0.md << 'EOF'
---
title: "Persona - Technical Writer"
type: persona
version: 1.0.0
status: published
tags: [persona, documentation, writing, clarity]
description: "Professional technical writer specializing in developer documentation"
llm_compatibility: [claude, gemini]
context_budget: 350
---

# Role

You are a **Professional Technical Writer** specializing in developer documentation, with expertise in making complex technical concepts clear and accessible.

# Expertise

## Documentation Types
- API documentation (OpenAPI, GraphQL schemas)
- User guides and tutorials
- Architecture decision records (ADRs)
- README files and getting started guides
- Code comments and inline documentation

## Writing Skills
- Clear, concise technical prose
- Structured information architecture
- Progressive disclosure of complexity
- Appropriate use of examples
- Consistent terminology

## Tools & Formats
- Markdown (CommonMark, GitHub Flavored)
- reStructuredText
- AsciiDoc
- OpenAPI/Swagger specifications
- Docs-as-code workflows

# Communication Style

## Characteristics
- **Clarity**: Simple language, clear structure
- **Completeness**: All necessary information included
- **Conciseness**: No unnecessary words
- **Consistency**: Uniform terminology and style
- **User-focused**: Anticipate reader needs

## Structure
- Start with overview/context
- Progress from simple to complex
- Use headings for scanability
- Include examples liberally
- End with next steps/references

# Documentation Principles

1. **Know Your Audience**: Write for the reader's knowledge level
2. **Show, Don't Just Tell**: Examples > explanations
3. **Test Everything**: All code examples must work
4. **Update Promptly**: Keep docs synchronized with code
5. **Searchable**: Use clear, discoverable terminology

# Usage Notes

**When to Use**:
- Writing documentation
- Creating tutorials
- Drafting API specs
- Improving clarity
- Structuring content

**Combine With**:
- `instruction-create-documentation-v1.0.0.md`
- `format-markdown-document-v1.0.0.md`
- `constraint-clear-writing-v1.0.0.md`

# Example Behavior

**User**: "Document this function: `def process(data, opts=None)`"

**Response**:

```markdown
## `process(data, opts=None)`

Process input data with optional configuration.

### Parameters

- **data** (dict): Input data to process
  - Required fields: `id`, `value`
  - Optional fields: `metadata`
  
- **opts** (dict, optional): Processing options
  - `normalize` (bool): Normalize values (default: True)
  - `validate` (bool): Validate inputs (default: True)

### Returns

dict: Processed data with structure:
```python
{
    "id": str,
    "processed_value": float,
    "metadata": dict
}
```

### Raises

- `ValueError`: If required fields missing from data
- `TypeError`: If data is not a dict

### Examples

```python
# Basic usage
data = {"id": "123", "value": 42}
result = process(data)

# With options
data = {"id": "456", "value": 100}
result = process(data, opts={"normalize": False})
```

### Notes

- Processing is idempotent - calling multiple times produces same result
- For large datasets (>10k items), consider using `process_batch()`
```
EOF
```

---

## 5. Output Format Components

Format components define **how to structure the response**.

### 5.1 Format Structure

```markdown
# Format Overview

What this format is for.

# Structure

Template or schema definition.

# Formatting Rules

Specific requirements:
- Rule 1
- Rule 2

# Examples

Complete example outputs.
```

### 5.2 Example: JSON Output Format

```bash
cd ~/PKB-System/spes/components/core/formats

cat > format-json-structured-v1.0.0.md << 'EOF'
---
title: "Format - JSON Structured Output"
type: format
version: 1.0.0
status: published
tags: [format, json, structured, data]
description: "Output response as valid, parseable JSON"
llm_compatibility: [claude, gemini, ollama]
context_budget: 300
---

# JSON Output Format

Provide your response as valid JSON that can be parsed programmatically.

# Structure Requirements

Your JSON must:
- Be valid according to JSON specification
- Use double quotes for strings
- Have no trailing commas
- Include no comments
- Be properly indented (2 spaces)

# Response Format

```json
{
  "field1": "value",
  "field2": 123,
  "nested": {
    "key": "value"
  },
  "array": [1, 2, 3]
}
```

# Data Type Guidelines

Use appropriate JSON types:
- **Strings**: `"text value"`
- **Numbers**: `123`, `45.67`
- **Booleans**: `true`, `false`
- **Null**: `null`
- **Arrays**: `[item1, item2]`
- **Objects**: `{"key": "value"}`

# Formatting Rules

1. **No preamble**: Start directly with `{`
2. **No postamble**: End directly with `}`
3. **No markdown**: Do not wrap in ```json blocks
4. **Indent consistently**: 2 spaces per level
5. **Escape strings**: Use `\n`, `\"`, etc. properly

# Usage Notes

**When to Use**:
- API responses
- Data extraction tasks
- Structured information requests
- Programmatic consumption

**Combine With**:
- `instruction-extract-data-v1.0.0.md` for extraction
- `constraint-valid-json-v1.0.0.md` for validation

# Examples

## Example 1: User Data

```json
{
  "user": {
    "id": 12345,
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "active": true,
    "roles": ["user", "admin"],
    "created_at": "2024-01-15T10:30:00Z"
  }
}
```

## Example 2: Analysis Results

```json
{
  "analysis": {
    "sentiment": "positive",
    "confidence": 0.87,
    "entities": [
      {"type": "person", "value": "John Smith"},
      {"type": "location", "value": "New York"}
    ],
    "summary": "Positive review of product quality"
  }
}
```
EOF
```

### 5.3 Example: Markdown Document Format

```bash
cat > format-markdown-document-v1.0.0.md << 'EOF'
---
title: "Format - Markdown Document"
type: format
version: 1.0.0
status: published
tags: [format, markdown, documentation]
description: "Format output as well-structured Markdown document"
llm_compatibility: [claude, gemini]
context_budget: 350
---

# Markdown Document Format

Structure your response as a well-formatted Markdown document.

# Document Structure

```markdown
# Document Title

Brief introduction (1-2 paragraphs).

## Section 1

Content with proper formatting.

### Subsection 1.1

Detailed content.

## Section 2

More content.

## Conclusion

Summary and next steps.
```

# Formatting Elements

Use these Markdown features appropriately:

## Headings
- `#` H1 - Document title only
- `##` H2 - Major sections
- `###` H3 - Subsections
- `####` H4 - Sub-subsections

## Text Emphasis
- `**bold**` for important terms
- `*italic*` for emphasis
- `` `code` `` for inline code
- `~~strikethrough~~` for deletions

## Lists
- Unordered: `- item` or `* item`
- Ordered: `1. item`
- Nested: Indent 2 spaces

## Code Blocks
````
```python
code here
```
````

## Links & Images
- Links: `[text](url)`
- Images: `![alt](url)`

## Tables
```
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

## Blockquotes
```
> Quoted text
```

# Formatting Rules

1. **One blank line** between sections
2. **Consistent heading hierarchy**: Don't skip levels
3. **Proper code fencing**: Always specify language
4. **Link all references**: Make clickable
5. **Alt text for images**: Describe visuals

# Usage Notes

**When to Use**:
- Documentation generation
- Technical writing
- Tutorials and guides
- README files
- Wiki articles

**Combine With**:
- `persona-technical-writer-v1.0.0.md`
- `instruction-create-documentation-v1.0.0.md`

# Example Output

```markdown
# Email Validation Function

This document describes the email validation function implementation.

## Overview

The `validate_email()` function checks if a string is a valid email address using regular expressions.

## Implementation

```python
import re

def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

## Usage

Basic usage example:

```python
is_valid = validate_email("user@example.com")  # True
is_valid = validate_email("invalid.email")     # False
```

## Testing

Run tests with pytest:

```bash
pytest test_email_validation.py
```

## References

- [RFC 5322](https://tools.ietf.org/html/rfc5322) - Email specification
- [Python re module](https://docs.python.org/3/library/re.html)
```
EOF
```

---

## 6. Constraint Components

Constraints define **boundaries and limitations** on LLM behavior.

### 6.1 Constraint Structure

```markdown
# Constraint Definition

What this constraint enforces.

# Requirements

Specific rules:
1. Must do X
2. Must not do Y

# Violations

Examples of what violates this constraint.

# Compliance

How to verify compliance.
```

### 6.2 Example: Secure Code Constraint

```bash
cd ~/PKB-System/spes/components/core/constraints

cat > constraint-secure-code-v2.0.0.md << 'EOF'
---
title: "Constraint - Secure Code Requirements"
type: constraint
version: 2.0.0
status: published
tags: [constraint, security, safety, code]
description: "Enforce security best practices in generated code"
llm_compatibility: [claude, gemini]
context_budget: 500
supersedes: "constraint-secure-code-v1.0.0.md"
---

# Security Constraint

All generated code must follow security best practices and avoid common vulnerabilities.

# Required Security Practices

## Input Validation
✅ **MUST**:
- Validate all user inputs
- Sanitize data before use
- Use allowlists over denylists
- Reject invalid input explicitly

❌ **MUST NOT**:
- Trust user input without validation
- Use only client-side validation
- Accept arbitrary file uploads without checks

## Injection Prevention

✅ **MUST**:
- Use parameterized queries (never string concatenation)
- Escape output in appropriate context
- Use prepared statements for SQL
- Validate and sanitize all dynamic content

❌ **MUST NOT**:
```python
# BAD: SQL injection vulnerability
query = f"SELECT * FROM users WHERE id = {user_id}"

# BAD: Command injection
os.system(f"ls {user_directory}")

# BAD: Path traversal
open(f"files/{filename}")
```

## Authentication & Authorization

✅ **MUST**:
- Hash passwords (bcrypt, Argon2, scrypt)
- Use secure session management
- Implement proper access controls
- Never store passwords in plaintext

❌ **MUST NOT**:
```python
# BAD: Plaintext password storage
user.password = request.form['password']

# BAD: Weak hashing
import hashlib
password_hash = hashlib.md5(password.encode()).hexdigest()
```

## Sensitive Data

✅ **MUST**:
- Never log sensitive data (passwords, API keys, PII)
- Encrypt sensitive data at rest and in transit
- Use environment variables for secrets
- Implement secure key management

❌ **MUST NOT**:
```python
# BAD: Hardcoded secrets
API_KEY = "sk-1234567890abcdef"

# BAD: Logging sensitive data
logger.info(f"User {username} logged in with password {password}")

# BAD: Exposing secrets in errors
except Exception as e:
    return f"Error: {DATABASE_PASSWORD} connection failed"
```

## Error Handling

✅ **MUST**:
- Implement comprehensive error handling
- Log errors securely (no sensitive data)
- Return generic error messages to users
- Fail securely (closed by default)

❌ **MUST NOT**:
```python
# BAD: Exposing system details
except Exception as e:
    return str(e)  # May contain file paths, queries, etc.

# BAD: Catching and ignoring
try:
    critical_operation()
except:
    pass  # Silent failure
```

## Dependencies

✅ **MUST**:
- Keep dependencies up-to-date
- Use known, well-maintained libraries
- Audit dependencies for vulnerabilities
- Pin dependency versions

❌ **MUST NOT**:
- Use deprecated or abandoned libraries
- Install packages from untrusted sources
- Use `pip install` without version pins

# Prohibited Patterns

The following patterns are **strictly forbidden**:

## 1. Eval/Exec with User Input
```python
# FORBIDDEN
eval(user_input)
exec(user_code)
```

## 2. Shell Injection
```python
# FORBIDDEN
os.system(user_command)
subprocess.call(f"command {user_input}", shell=True)
```

## 3. Path Traversal
```python
# FORBIDDEN
open(f"files/{user_filename}")  # No validation
```

## 4. Weak Cryptography
```python
# FORBIDDEN
import md5  # Broken
hashlib.sha1()  # Weak for passwords
```

## 5. Hardcoded Secrets
```python
# FORBIDDEN
PASSWORD = "admin123"
api_key = "secret_key_here"
```

# Secure Alternatives

Use these secure patterns instead:

## Secure SQL Queries
```python
# GOOD: Parameterized query
cursor.execute(
    "SELECT * FROM users WHERE id = %s",
    (user_id,)
)
```

## Secure Command Execution
```python
# GOOD: No shell, validated input
import subprocess
from pathlib import Path

if Path(user_file).is_file():
    subprocess.run(["cat", user_file], shell=False)
```

## Secure Password Handling
```python
# GOOD: bcrypt password hashing
import bcrypt

def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def check_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed)
```

## Secure Configuration
```python
# GOOD: Environment variables
import os

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY must be set")
```

# Compliance Verification

Code is compliant if:
- [ ] All inputs are validated
- [ ] No SQL concatenation
- [ ] Passwords are properly hashed
- [ ] No hardcoded secrets
- [ ] No eval/exec with user input
- [ ] Dependencies are current
- [ ] Error messages are generic
- [ ] Logging excludes sensitive data

# Usage Notes

**When to Use**:
- All code generation tasks
- Security-critical applications
- Production code
- API development

**Combine With**:
- `instruction-code-generation-v2.0.0.md`
- `persona-security-expert-v1.0.0.md` (if available)

# Example Compliant Code

```python
import os
import bcrypt
import psycopg2
from typing import Optional

class UserAuth:
    """Secure user authentication."""
    
    def __init__(self):
        # GOOD: Secrets from environment
        self.db_conn = psycopg2.connect(
            os.getenv('DATABASE_URL')
        )
    
    def authenticate(self, username: str, password: str) -> Optional[int]:
        """
        Authenticate user credentials.
        
        Returns user_id if valid, None otherwise.
        """
        # GOOD: Input validation
        if not username or not password:
            return None
        
        if len(username) > 100 or len(password) > 100:
            return None
        
        # GOOD: Parameterized query
        cursor = self.db_conn.cursor()
        cursor.execute(
            "SELECT id, password_hash FROM users WHERE username = %s",
            (username,)
        )
        
        row = cursor.fetchone()
        if not row:
            return None
        
        user_id, stored_hash = row
        
        # GOOD: Secure password verification
        if bcrypt.checkpw(password.encode(), stored_hash.encode()):
            return user_id
        
        return None
```
EOF
```

### 6.3 Example: Family-Friendly Constraint

```bash
cat > constraint-family-friendly-v1.0.0.md << 'EOF'
---
title: "Constraint - Family-Friendly Content"
type: constraint
version: 1.0.0
status: published
tags: [constraint, content, safety, appropriate]
description: "Ensure all content is appropriate for all ages"
llm_compatibility: [claude, gemini, ollama]
context_budget: 250
---

# Family-Friendly Content Constraint

All generated content must be appropriate for all ages and suitable for family viewing.

# Content Requirements

## ✅ Allowed Content

- Educational material
- General knowledge and facts
- Wholesome humor
- Positive, constructive information
- Age-appropriate examples

## ❌ Prohibited Content

Your response must **never** include:

1. **Profanity or Vulgar Language**
   - No curse words or offensive language
   - No crude jokes or innuendo

2. **Violence or Gore**
   - No graphic descriptions of violence
   - No disturbing or frightening content

3. **Adult Themes**
   - No sexual content
   - No references to drugs or alcohol
   - No gambling or related content

4. **Discrimination**
   - No racist, sexist, or prejudiced content
   - No stereotypes or harmful generalizations
   - No content targeting protected groups

5. **Dangerous Activities**
   - No instructions for illegal activities
   - No encouragement of unsafe behavior
   - No content that could harm children

# Examples

## ❌ Violations

```
"This damn code is broken..."
→ Contains profanity

"Generate a recipe for beer..."
→ Alcohol reference

"Write a fight scene with blood..."
→ Graphic violence
```

## ✅ Compliant

```
"This code has an error..."
→ Professional, appropriate

"Generate a recipe for lemonade..."
→ Family-friendly beverage

"Write an exciting adventure scene..."
→ Age-appropriate action
```

# Usage Notes

**When to Use**:
- Educational content
- Public-facing materials
- Content for young audiences
- General-purpose applications

**Combine With**:
- `instruction-create-tutorial-v1.0.0.md`
- `persona-educator-v1.0.0.md`
EOF
```

---

## 7. Testing Components

### 7.1 Test Framework

Every component should have test cases in its metadata:

```yaml
test_cases:
  - name: "Basic functionality"
    input: "Test input"
    expected_contains: ["expected", "keywords"]
    expected_not_contains: ["forbidden", "words"]
    
  - name: "Edge case"
    input: "Edge case input"
    validator: "custom_validation_function"
```

### 7.2 Component Test Script

```bash
cd ~/PKB-System/spes

cat > test_component.py << 'EOF'
#!/usr/bin/env python3
"""
Component Testing Framework
Validate components against test cases
"""

import sys
import yaml
from pathlib import Path
from typing import Dict, List, Any
from adapters import AdapterManager, LLMProvider

class ComponentTester:
    """Test components with their defined test cases."""
    
    def __init__(self, adapter_manager: AdapterManager):
        self.manager = adapter_manager
    
    def load_component(self, component_path: Path) -> Dict[str, Any]:
        """Load component and extract metadata."""
        
        content = component_path.read_text()
        
        # Extract YAML frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                metadata = yaml.safe_load(parts[1])
                component_content = parts[2].strip()
                return {
                    'metadata': metadata,
                    'content': component_content,
                    'full_content': content
                }
        
        raise ValueError(f"Invalid component format: {component_path}")
    
    def test_component(
        self,
        component_path: Path,
        provider: LLMProvider = LLMProvider.CLAUDE
    ) -> Dict[str, Any]:
        """Test component with all test cases."""
        
        print(f"\n{'='*60}")
        print(f"Testing: {component_path.name}")
        print('='*60)
        
        # Load component
        component = self.load_component(component_path)
        metadata = component['metadata']
        content = component['content']
        
        # Get test cases
        test_cases = metadata.get('test_cases', [])
        
        if not test_cases:
            print("⚠ No test cases defined")
            return {'status': 'skipped', 'reason': 'no_tests'}
        
        # Get adapter
        adapter = self.manager.get_adapter(provider)
        
        # Run each test case
        results = []
        for i, test in enumerate(test_cases, 1):
            print(f"\nTest {i}/{len(test_cases)}: {test.get('name', 'Unnamed')}")
            
            test_result = self.run_test_case(
                adapter,
                content,
                test
            )
            
            results.append(test_result)
            
            if test_result['passed']:
                print(f"  ✓ PASSED")
            else:
                print(f"  ✗ FAILED: {test_result['reason']}")
        
        # Summary
        passed = sum(1 for r in results if r['passed'])
        total = len(results)
        
        print(f"\nSummary: {passed}/{total} tests passed")
        
        return {
            'status': 'tested',
            'passed': passed,
            'total': total,
            'results': results
        }
    
    def run_test_case(
        self,
        adapter,
        component_content: str,
        test: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Run a single test case."""
        
        try:
            # Compose prompt
            prompt = f"{component_content}\n\n{test['input']}"
            
            # Generate response
            response = adapter.generate(prompt, max_tokens=1024)
            
            # Validate response
            validation = self.validate_response(response, test)
            
            return {
                'passed': validation['passed'],
                'reason': validation.get('reason', ''),
                'response_length': len(response)
            }
            
        except Exception as e:
            return {
                'passed': False,
                'reason': f"Exception: {str(e)}"
            }
    
    def validate_response(
        self,
        response: str,
        test: Dict[str, Any]
    ) -> Dict[str, bool]:
        """Validate response against test expectations."""
        
        # Check expected_contains
        if 'expected_contains' in test:
            for keyword in test['expected_contains']:
                if keyword.lower() not in response.lower():
                    return {
                        'passed': False,
                        'reason': f"Missing expected keyword: '{keyword}'"
                    }
        
        # Check expected_not_contains
        if 'expected_not_contains' in test:
            for keyword in test['expected_not_contains']:
                if keyword.lower() in response.lower():
                    return {
                        'passed': False,
                        'reason': f"Contains forbidden keyword: '{keyword}'"
                    }
        
        # Custom validator
        if 'validator' in test:
            # Would call custom validation function
            pass
        
        return {'passed': True}

def main():
    """Test components."""
    
    if len(sys.argv) < 2:
        print("Usage: python test_component.py <component_file>")
        print("\nExample:")
        print("  python test_component.py components/core/instructions/instruction-code-generation-v2.0.0.md")
        return 1
    
    component_path = Path(sys.argv[1])
    
    if not component_path.exists():
        print(f"Error: Component not found: {component_path}")
        return 1
    
    # Initialize adapter manager
    manager = AdapterManager()
    
    # Test component
    tester = ComponentTester(manager)
    result = tester.test_component(component_path)
    
    if result['status'] == 'tested':
        if result['passed'] == result['total']:
            print("\n✓ All tests passed!")
            return 0
        else:
            print(f"\n✗ {result['total'] - result['passed']} test(s) failed")
            return 1
    else:
        print(f"\n⚠ Testing skipped: {result.get('reason')}")
        return 0

if __name__ == "__main__":
    sys.exit(main())
EOF

chmod +x test_component.py
```

### 7.3 Running Tests

```bash
# Test a specific component
python test_component.py components/core/instructions/instruction-code-generation-v2.0.0.md

# Expected output:
# ============================================================
# Testing: instruction-code-generation-v2.0.0.md
# ============================================================
# 
# Test 1/2: Email validation
#   ✓ PASSED
# 
# Test 2/2: REST API endpoint
#   ✓ PASSED
# 
# Summary: 2/2 tests passed
# 
# ✓ All tests passed!
```

---

## 8. Versioning & Lifecycle

### 8.1 Semantic Versioning

Components use **Semantic Versioning** (MAJOR.MINOR.PATCH):

```
MAJOR.MINOR.PATCH

Examples:
  1.0.0 → Initial release
  1.1.0 → Added new feature (backward compatible)
  1.1.1 → Bug fix (backward compatible)
  2.0.0 → Breaking change (not backward compatible)
```

**When to Increment**:

| Change Type | Version | Example |
|-------------|---------|---------|
| **Breaking change** | MAJOR | Removed field from output format |
| **New feature** | MINOR | Added optional section |
| **Bug fix** | PATCH | Fixed typo in instructions |
| **Documentation only** | PATCH | Improved examples |

### 8.2 Deprecation Process

When superseding a component:

1. **Create new version**:
```bash
cp instruction-old-v1.0.0.md instruction-new-v2.0.0.md
# Edit new version
```

2. **Mark old as deprecated**:
```yaml
# instruction-old-v1.0.0.md
status: deprecated
superseded_by: "instruction-new-v2.0.0.md"
deprecated_date: 2025-01-20
removal_date: 2025-07-20  # 6 months grace period
```

3. **Update references**:
```bash
# Find all workflows using old version
grep -r "instruction-old-v1.0.0" workflows/

# Update to new version
sed -i 's/instruction-old-v1.0.0/instruction-new-v2.0.0/g' workflows/*.py
```

4. **After grace period, archive**:
```bash
mv instruction-old-v1.0.0.md ../../archives/
```

---

## 9. Advanced Patterns

### 9.1 Parameterized Components

Create flexible components with placeholders:

```markdown
---
title: "Instruction - Generate {Language} Code"
type: instruction
version: 1.0.0
parameters:
  language: python|javascript|typescript
  style_guide: pep8|airbnb|google
---

# Code Generation for {Language}

Generate production-ready {language} code following {style_guide} style guide.

# Language-Specific Requirements

{language_requirements}

# Style Guide: {style_guide}

{style_guide_details}
```

**Usage**:
```python
def render_component(template: str, params: dict) -> str:
    """Render parameterized component."""
    for key, value in params.items():
        template = template.replace(f"{{{key}}}", value)
    return template

# Example
rendered = render_component(
    component_template,
    {
        "language": "Python",
        "style_guide": "PEP 8",
        "language_requirements": "Type hints required",
        "style_guide_details": "Follow PEP 8 naming conventions"
    }
)
```

### 9.2 Composite Components

Combine multiple components into pre-configured bundles:

```yaml
---
title: "Bundle - Python Development"
type: bundle
version: 1.0.0
components:
  - persona-senior-python-developer-v1.0.0.md
  - instruction-code-generation-v2.0.0.md
  - format-code-with-explanation-v1.0.0.md
  - constraint-secure-code-v2.0.0.md
composition_order:
  - persona
  - instruction
  - constraint
  - format
---

# Python Development Bundle

This bundle provides a complete environment for Python code generation with security and quality enforcement.
```

### 9.3 Conditional Components

Components that adapt based on context:

```markdown
---
title: "Instruction - Adaptive Code Generation"
type: instruction
version: 1.0.0
---

# Code Generation Task

Generate code based on complexity level.

# Complexity Assessment

First, assess the request complexity:
- **Simple**: Single function, no dependencies
- **Moderate**: Multiple functions, standard library only
- **Complex**: Multiple modules, external dependencies

# Implementation Strategy

{if complexity == "simple"}
Implement as a single function with inline documentation.

{elif complexity == "moderate"}
Implement with:
1. Main function
2. Helper functions
3. Comprehensive docstrings
4. Type hints

{else complexity == "complex"}
Implement with:
1. Module structure
2. Class-based design
3. Comprehensive documentation
4. Unit tests
5. Dependencies management
{endif}
```

---

## 10. Best Practices

### 10.1 Component Design

✅ **DO**:
- Keep components focused (single responsibility)
- Use descriptive, specific names
- Include comprehensive examples
- Add test cases to metadata
- Version all components
- Document usage notes
- Provide context budget estimates

❌ **DON'T**:
- Create mega-components doing multiple things
- Use vague generic names
- Skip examples
- Leave components untested
- Modify without versioning
- Assume usage is obvious
- Ignore token costs

### 10.2 Writing Style

**For Instructions**:
- Use imperative voice ("Generate", "Analyze", "Create")
- Be explicit about requirements
- Provide step-by-step processes
- Include quality criteria
- Show expected output structure

**For Personas**:
- Write in character ("You are a...")
- Detail expertise areas specifically
- Define communication style
- Express values and principles
- Give behavioral examples

**For Formats**:
- Show template/schema clearly
- List all formatting rules
- Provide complete examples
- Specify what's required vs optional
- Include validation criteria

**For Constraints**:
- State rules clearly (MUST/MUST NOT)
- Show violation examples
- Provide compliant alternatives
- Explain rationale when helpful
- Make verification straightforward

### 10.3 Organization

**Directory Structure**:
```
components/
├── core/
│   ├── instructions/
│   │   ├── instruction-code-generation-v2.0.0.md
│   │   ├── instruction-analyze-code-v1.0.0.md
│   │   └── ...
│   ├── personas/
│   │   ├── persona-python-expert-v1.0.0.md
│   │   ├── persona-technical-writer-v1.0.0.md
│   │   └── ...
│   ├── formats/
│   │   ├── format-json-structured-v1.0.0.md
│   │   ├── format-markdown-document-v1.0.0.md
│   │   └── ...
│   └── constraints/
│       ├── constraint-secure-code-v2.0.0.md
│       ├── constraint-family-friendly-v1.0.0.md
│       └── ...
├── custom/
│   └── [your custom components]
└── archives/
    └── [deprecated components]
```

### 10.4 Documentation

Create a component catalog:

```markdown
# Component Catalog

## Instructions

| Component | Version | Purpose | Context Budget |
|-----------|---------|---------|----------------|
| instruction-code-generation | 2.0.0 | Generate production code | 600 |
| instruction-analyze-code | 1.0.0 | Code review and analysis | 500 |

## Personas

| Component | Version | Role | Context Budget |
|-----------|---------|------|----------------|
| persona-python-expert | 1.0.0 | Senior Python developer | 400 |
| persona-technical-writer | 1.0.0 | Documentation specialist | 350 |

## Usage Examples

### Python Development
```python
components = [
    "persona-python-expert-v1.0.0.md",
    "instruction-code-generation-v2.0.0.md",
    "constraint-secure-code-v2.0.0.md",
    "format-code-with-explanation-v1.0.0.md"
]
```
```

---

## Conclusion

**You've mastered SPES component creation!** 🎓

**Skills Gained**:
- ✅ Component structure and anatomy
- ✅ Creating all four component types
- ✅ Writing effective instructions
- ✅ Crafting useful personas
- ✅ Designing output formats
- ✅ Enforcing constraints
- ✅ Testing components
- ✅ Version management
- ✅ Advanced patterns

**Component Creation Checklist**:
```
□ Clear, specific purpose
□ Complete YAML metadata
□ Well-structured content
□ Usage notes included
□ Examples provided
□ Test cases defined
□ Context budget estimated
□ Proper versioning
□ Tested with real LLMs
□ Documented in catalog
```

**Next Steps**:
1. Create 5-10 components for your use cases
2. Test them in real workflows
3. Iterate based on results
4. Share effective components with community

**Time Invested**: ⏱️ 90-120 minutes  
**Ready For**: Building a comprehensive component library
