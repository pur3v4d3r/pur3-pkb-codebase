---
title: SPES Advanced Prompt Engineering
document_type: tier4_advanced
tier: 4
priority: critical
version: 1.0.0
status: published
prerequisites: ["Advanced Memory Architecture", "Semantic Retrieval & MCP", "Meta-Cognitive Workflows"]
estimated_time: 300-360 minutes
complexity: very_complex
last_updated: 2025-12-27
---

# Advanced Prompt Engineering for SPES

**Version**: 1.0.0  
**Document Type**: Tier 4 - Advanced Implementation  
**Audience**: Prompt engineers, AI architects, system designers  
**Time Required**: 300-360 minutes (5-6 hours)  
**Goal**: Master advanced prompt engineering techniques with production-grade implementations integrated into SPES

---

## Table of Contents

1. [System Prompt Architecture](#1-system-prompt-architecture)
2. [Few-Shot Learning Mastery](#2-few-shot-learning-mastery)
3. [Chain-of-Thought Mastery](#3-chain-of-thought-mastery)
4. [Advanced Reasoning Patterns](#4-advanced-reasoning-patterns)
5. [Prompt Optimization & Testing](#5-prompt-optimization--testing)
6. [Production Deployment](#6-production-deployment)
7. [Meta-Orchestration](#7-meta-orchestration)

---

## Overview

> **The Challenge**: Most LLM prompts are ad-hoc, unreproducible, and impossible to optimize systematically. Without proper prompt engineering, even the most powerful LLMs underperform.

> **The Solution**: **Systematic prompt engineering** that treats prompts as versioned, testable, optimizable artifacts with production deployment pipelines.

### What Makes This Different?

This document goes beyond basic prompting to cover:

| Traditional Prompting | Advanced Prompt Engineering |
|----------------------|----------------------------|
| Ad-hoc prompt writing | Systematic prompt templates |
| Trial-and-error | A/B testing with metrics |
| No version control | Git-tracked prompt registry |
| Single technique | Multi-pattern composition |
| No quality gates | Automated validation |
| Manual optimization | Data-driven improvement |

### Advanced Techniques Covered

**From Academic Research (2023-2025)**:
- Chain of Verification (CoVe)
- Contrastive Chain-of-Thought
- Faithful Chain-of-Thought
- Least-to-Most Prompting
- Program of Thoughts
- Thread of Thoughts
- Step-Back Prompting
- Tabular Chain-of-Thought
- Universal Self-Consistency

**Production Systems**:
- Prompt registry with versioning
- Confidence calibration
- Quality checkpoints
- Failure mode detection
- Performance monitoring
- Automated rollback

---

## 1. System Prompt Architecture

### 1.1 Memory-First System Prompts

**Core Principle**: System prompts should leverage SPES memory architecture from the start.

**Traditional System Prompt**:
```
You are a helpful assistant that writes code.
```

**Memory-First System Prompt**:
```python
MEMORY_FIRST_SYSTEM_PROMPT = """You are an AI assistant with access to structured memory.

**Memory Architecture**:
- **Working Memory** (.claude/activeContext.md): Current session state
- **Short-Term Memory** (.claude/task-logs/): Recent tasks and decisions
- **Long-Term Memory** (.claude/core/): Established patterns and knowledge

**Memory Access Protocol**:
1. **Session Start**: Load activeContext for current state
2. **Information Needs**: Search semantic memory via MCP lookup tool
3. **Task Execution**: Log decisions to task-logs/
4. **Pattern Discovery**: Update core/ with reusable patterns

**MCP Tools Available**:
- `lookup(query, limit, threshold)`: Semantic search across memory
- `connection(file_path, limit)`: Find related notes
- `stats()`: Memory statistics
- `validate(file_path)`: Check embedding status

**Constitutional Principles** (Score: 0-23):
- Completeness (0-2): All requirements met
- Correctness (0-2): Technically accurate
- Clarity (0-2): Clear communication
- Efficiency (0-1): Optimal approach
- Maintainability (0-1): Easy to modify
- Documentation (0-1): Well documented
- Testability (0-1): Comprehensive tests
- Bonus (+0-13): Creativity, robustness, performance, security, etc.

**Current Session Context**:
{active_context}

**Working on**: {current_task}
"""


def create_memory_aware_system_prompt(
    memory_path: Path,
    current_task: str = None
) -> str:
    """Create system prompt with current memory context."""
    
    # Load active context
    active_context_path = memory_path / "activeContext.md"
    active_context = ""
    
    if active_context_path.exists():
        content = active_context_path.read_text()
        
        # Extract currentFocus and activeFiles
        import re
        focus_match = re.search(r'currentFocus:\s*(.+)', content)
        files_match = re.search(r'activeFiles:\s*\[(.*?)\]', content, re.DOTALL)
        
        if focus_match:
            active_context += f"Current Focus: {focus_match.group(1)}\n"
        
        if files_match:
            active_files = [f.strip() for f in files_match.group(1).split(',')]
            active_context += f"Active Files: {', '.join(active_files)}\n"
    
    return MEMORY_FIRST_SYSTEM_PROMPT.format(
        active_context=active_context or "No active context",
        current_task=current_task or "No specific task"
    )


# Example usage
system_prompt = create_memory_aware_system_prompt(
    memory_path=Path(".claude"),
    current_task="Implement JWT authentication"
)

print(system_prompt)
```

### 1.2 Role Definition Best Practices

**Effective role definition** shapes model behavior:

```python
class SystemPromptBuilder:
    """
    Build production-grade system prompts with role definition.
    """
    
    def __init__(self):
        self.components = {
            'identity': None,
            'capabilities': [],
            'constraints': [],
            'output_format': None,
            'memory_context': None,
            'tools': [],
            'evaluation_criteria': []
        }
    
    def set_identity(
        self,
        role: str,
        expertise: List[str],
        personality: str = None
    ) -> 'SystemPromptBuilder':
        """Define who the AI is."""
        
        identity = f"You are {role}"
        
        if expertise:
            identity += f" with expertise in:\n"
            identity += "\n".join(f"- {exp}" for exp in expertise)
        
        if personality:
            identity += f"\n\nPersonality: {personality}"
        
        self.components['identity'] = identity
        return self
    
    def add_capabilities(self, capabilities: List[str]) -> 'SystemPromptBuilder':
        """Define what the AI can do."""
        self.components['capabilities'].extend(capabilities)
        return self
    
    def add_constraints(self, constraints: List[str]) -> 'SystemPromptBuilder':
        """Define what the AI should NOT do."""
        self.components['constraints'].extend(constraints)
        return self
    
    def set_output_format(self, format_spec: str) -> 'SystemPromptBuilder':
        """Define expected output structure."""
        self.components['output_format'] = format_spec
        return self
    
    def add_memory_context(self, memory_prompt: str) -> 'SystemPromptBuilder':
        """Add memory access instructions."""
        self.components['memory_context'] = memory_prompt
        return self
    
    def add_tools(self, tools: List[Dict]) -> 'SystemPromptBuilder':
        """Add tool usage instructions."""
        self.components['tools'].extend(tools)
        return self
    
    def add_evaluation_criteria(
        self,
        criteria: List[str]
    ) -> 'SystemPromptBuilder':
        """Add self-evaluation criteria."""
        self.components['evaluation_criteria'].extend(criteria)
        return self
    
    def build(self) -> str:
        """Build complete system prompt."""
        
        sections = []
        
        # Identity
        if self.components['identity']:
            sections.append(self.components['identity'])
        
        # Capabilities
        if self.components['capabilities']:
            sections.append("\n**Capabilities**:")
            sections.append("\n".join(
                f"- {cap}" for cap in self.components['capabilities']
            ))
        
        # Constraints
        if self.components['constraints']:
            sections.append("\n**Constraints**:")
            sections.append("\n".join(
                f"- {const}" for const in self.components['constraints']
            ))
        
        # Tools
        if self.components['tools']:
            sections.append("\n**Available Tools**:")
            for tool in self.components['tools']:
                sections.append(f"\n- `{tool['name']}`: {tool['description']}")
        
        # Memory context
        if self.components['memory_context']:
            sections.append(f"\n{self.components['memory_context']}")
        
        # Output format
        if self.components['output_format']:
            sections.append(f"\n**Output Format**:\n{self.components['output_format']}")
        
        # Evaluation criteria
        if self.components['evaluation_criteria']:
            sections.append("\n**Self-Evaluation**:")
            sections.append("After generating output, evaluate against:")
            sections.append("\n".join(
                f"- {crit}" for crit in self.components['evaluation_criteria']
            ))
        
        return "\n".join(sections)


# Example: Build a code review assistant
code_review_prompt = (
    SystemPromptBuilder()
    .set_identity(
        role="a senior code reviewer",
        expertise=[
            "Python, TypeScript, Go",
            "Software architecture and design patterns",
            "Security best practices",
            "Performance optimization"
        ],
        personality="Constructive, detail-oriented, pragmatic"
    )
    .add_capabilities([
        "Identify bugs, security issues, and anti-patterns",
        "Suggest specific improvements with code examples",
        "Explain rationale for each suggestion",
        "Prioritize feedback by severity"
    ])
    .add_constraints([
        "Do NOT rewrite entire files unless requested",
        "Do NOT suggest changes without explaining why",
        "Do NOT be overly pedantic about style (focus on substance)",
        "Do NOT approve code with security vulnerabilities"
    ])
    .add_tools([
        {
            'name': 'search_memory',
            'description': 'Search for similar code patterns in past projects'
        },
        {
            'name': 'lookup_standards',
            'description': 'Find coding standards and best practices'
        }
    ])
    .set_output_format("""
```markdown
## Summary
[High-level assessment]

## Critical Issues 🔴
[Security, bugs, breaking changes]

## Improvements 🟡
[Performance, maintainability, clarity]

## Suggestions 🟢
[Nice-to-haves, style preferences]

## Approved ✓ / Needs Work ✗
[Final verdict]
```
""")
    .add_evaluation_criteria([
        "Are all security issues identified?",
        "Are suggestions specific and actionable?",
        "Is feedback appropriately prioritized?",
        "Are code examples provided where helpful?"
    ])
    .build()
)

print(code_review_prompt)
```

### 1.3 Context Window Management

**Managing limited context effectively**:

```python
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class ContextSection:
    """Single section of context."""
    priority: int  # 1 (critical) to 5 (optional)
    content: str
    token_estimate: int
    name: str


class ContextWindowManager:
    """
    Manage context window allocation across competing needs.
    """
    
    def __init__(self, max_tokens: int = 200000):
        """
        Initialize with model's context window size.
        
        Args:
            max_tokens: Model's maximum context window
        """
        self.max_tokens = max_tokens
        self.sections: List[ContextSection] = []
    
    def add_section(
        self,
        name: str,
        content: str,
        priority: int,
        token_estimate: int = None
    ):
        """Add a context section."""
        
        if token_estimate is None:
            # Rough estimate: 1 token ≈ 4 characters
            token_estimate = len(content) // 4
        
        self.sections.append(ContextSection(
            priority=priority,
            content=content,
            token_estimate=token_estimate,
            name=name
        ))
    
    def build_context(
        self,
        reserved_for_output: int = 4000
    ) -> str:
        """
        Build optimal context within token budget.
        
        Args:
            reserved_for_output: Tokens to reserve for response
        
        Returns:
            Optimized context string
        """
        
        available_tokens = self.max_tokens - reserved_for_output
        
        # Sort by priority (1 = highest priority)
        sorted_sections = sorted(self.sections, key=lambda s: s.priority)
        
        selected_sections = []
        used_tokens = 0
        
        # Greedy selection by priority
        for section in sorted_sections:
            if used_tokens + section.token_estimate <= available_tokens:
                selected_sections.append(section)
                used_tokens += section.token_estimate
            else:
                # Try to include truncated version if high priority
                if section.priority <= 2:
                    remaining = available_tokens - used_tokens
                    if remaining > 100:  # Only if meaningful space left
                        truncated = self._truncate_section(
                            section.content,
                            remaining
                        )
                        selected_sections.append(ContextSection(
                            priority=section.priority,
                            content=truncated,
                            token_estimate=remaining,
                            name=f"{section.name} (truncated)"
                        ))
                        used_tokens = available_tokens
                        break
        
        # Build final context
        context_parts = []
        
        for section in selected_sections:
            context_parts.append(f"### {section.name}")
            context_parts.append(section.content)
            context_parts.append("")  # Blank line
        
        context_parts.append(f"**Context utilization**: {used_tokens}/{available_tokens} tokens ({used_tokens/available_tokens:.1%})")
        
        return "\n".join(context_parts)
    
    def _truncate_section(self, content: str, max_tokens: int) -> str:
        """Intelligently truncate content to fit token budget."""
        
        # Rough conversion: 4 chars per token
        max_chars = max_tokens * 4
        
        if len(content) <= max_chars:
            return content
        
        # Try to truncate at sentence boundary
        truncated = content[:max_chars]
        
        # Find last sentence ending
        for delimiter in ['. ', '.\n', '! ', '?\n']:
            last_sentence = truncated.rfind(delimiter)
            if last_sentence > max_chars * 0.8:  # Keep at least 80%
                return truncated[:last_sentence + 1] + "\n\n[Truncated for space]"
        
        # No good sentence boundary, just cut
        return truncated + "...\n\n[Truncated for space]"


# Example: Build context for code review
manager = ContextWindowManager(max_tokens=200000)

# Priority 1: Critical context
manager.add_section(
    name="System Prompt",
    content=code_review_prompt,
    priority=1,
    token_estimate=500
)

manager.add_section(
    name="Code to Review",
    content=open("auth_system.py").read(),
    priority=1
)

# Priority 2: Important reference material
manager.add_section(
    name="Security Standards",
    content="[Security best practices from memory...]",
    priority=2,
    token_estimate=1000
)

manager.add_section(
    name="Similar Past Reviews",
    content="[Retrieved from memory via MCP...]",
    priority=2,
    token_estimate=2000
)

# Priority 3: Nice-to-have context
manager.add_section(
    name="Full Project Architecture",
    content="[Large architecture diagram...]",
    priority=3,
    token_estimate=5000
)

# Priority 4: Optional background
manager.add_section(
    name="Historical Decisions",
    content="[ADRs and design docs...]",
    priority=4,
    token_estimate=10000
)

# Build optimal context
final_context = manager.build_context(reserved_for_output=4000)

print(f"Total sections: {len(manager.sections)}")
print(f"Context preview:\n{final_context[:500]}...")
```

### 1.4 Tool-Aware System Prompts

**System prompts that enable effective tool use**:

```python
MCP_AWARE_SYSTEM_PROMPT = """You are an AI assistant with access to semantic memory via Model Context Protocol (MCP).

**Available MCP Tools**:

1. **lookup(query, limit=5, threshold=0.5)**
   - Semantic search across memory
   - Returns: List of relevant documents with similarity scores
   - When to use: Finding information, patterns, past solutions
   - Example: `lookup("authentication patterns", limit=3)`

2. **connection(file_path, limit=5)**
   - Find documents related to a specific file
   - Returns: Related documents by semantic similarity
   - When to use: Exploring related concepts, finding context
   - Example: `connection("systemPatterns.md")`

3. **stats()**
   - Memory system statistics
   - Returns: Model info, file count, embedding dimensions
   - When to use: Verifying memory system health

4. **validate(file_path)**
   - Check if file has valid embeddings
   - Returns: Embedding status and metadata
   - When to use: Debugging memory issues

**Tool Usage Protocol**:

1. **Search Before Creating**: Always search memory for existing solutions before creating new ones
2. **Verify Retrieved Information**: Use multiple searches if initial results are unclear
3. **Update Memory After Tasks**: Document new patterns and solutions
4. **Link Related Concepts**: Use connection tool to build knowledge graph

**Tool Call Format**:
```json
{
  "tool": "lookup",
  "parameters": {
    "query": "your search query",
    "limit": 5,
    "threshold": 0.5
  }
}
```

**Example Workflow**:
```
User: "How do we handle authentication?"

Think: I should search memory for authentication patterns

Action: lookup("authentication patterns JWT PKCE", limit=5)

Observation: Found 3 patterns:
1. systemPatterns.md#jwt-authentication (similarity: 0.85)
2. auth-implementation.md (similarity: 0.72)
3. security-guidelines.md (similarity: 0.68)

Action: connection("systemPatterns.md#jwt-authentication")

Observation: Related files:
- auth-context.md (design decisions)
- jwt-refresh-pattern.md (implementation)
- security-review.md (audit notes)

Response: [Synthesize information from retrieved context]
```

**When NOT to Use Tools**:
- Answering from general knowledge (e.g., "What is JWT?")
- Simple calculations or transformations
- Responding to greetings or meta-questions

**Tool Errors**:
- If tool returns empty results, try broader/simpler query
- If tool fails, proceed with available knowledge and inform user
- Never invent tool results or hallucinate memory content
"""


def create_tool_aware_prompt(tools: List[Dict]) -> str:
    """Generate system prompt with tool descriptions."""
    
    prompt = "You are an AI assistant with access to tools.\n\n"
    prompt += "**Available Tools**:\n\n"
    
    for tool in tools:
        prompt += f"### {tool['name']}\n"
        prompt += f"{tool['description']}\n\n"
        
        if 'parameters' in tool:
            prompt += "**Parameters**:\n"
            for param, desc in tool['parameters'].items():
                prompt += f"- `{param}`: {desc}\n"
            prompt += "\n"
        
        if 'examples' in tool:
            prompt += "**Examples**:\n"
            for example in tool['examples']:
                prompt += f"```\n{example}\n```\n"
            prompt += "\n"
    
    prompt += "\n**Tool Usage Guidelines**:\n"
    prompt += "- Use tools when they provide value (don't overuse)\n"
    prompt += "- Explain tool calls in your reasoning\n"
    prompt += "- Handle tool errors gracefully\n"
    prompt += "- Synthesize results, don't just quote them\n"
    
    return prompt


# Example tool definitions
mcp_tools = [
    {
        'name': 'lookup',
        'description': 'Semantic search across memory for relevant information',
        'parameters': {
            'query': 'Search query (semantic, not keyword-based)',
            'limit': 'Number of results (default: 5, max: 10)',
            'threshold': 'Minimum similarity score (0-1, default: 0.5)'
        },
        'examples': [
            'lookup("authentication security patterns", limit=3)',
            'lookup("database migration errors", threshold=0.6)'
        ]
    },
    {
        'name': 'connection',
        'description': 'Find documents related to a specific file',
        'parameters': {
            'file_path': 'Path to file in memory',
            'limit': 'Number of related documents (default: 5)'
        },
        'examples': [
            'connection("core/systemPatterns.md")',
            'connection("errors/auth-timeout-2024-03-15.md", limit=3)'
        ]
    }
]

tool_prompt = create_tool_aware_prompt(mcp_tools)
print(tool_prompt)
```

---

## 2. Few-Shot Learning Mastery

### 2.1 Dynamic Example Selection

**Retrieve optimal examples from memory**:

```python
from typing import List, Dict, Tuple
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class DynamicExampleSelector:
    """
    Select optimal few-shot examples from memory.
    
    Uses semantic similarity + diversity + difficulty balancing.
    """
    
    def __init__(
        self,
        mcp_client,
        embedding_model,
        memory_path: Path
    ):
        """
        Initialize example selector.
        
        Args:
            mcp_client: MCP client for semantic search
            embedding_model: Model for generating embeddings
            memory_path: Path to memory directory
        """
        self.mcp = mcp_client
        self.embedding_model = embedding_model
        self.memory_path = Path(memory_path)
        
        # Example library location
        self.examples_path = memory_path / "examples"
        self.examples_path.mkdir(exist_ok=True)
    
    def select_examples(
        self,
        query: str,
        num_examples: int = 5,
        diversity_weight: float = 0.3,
        difficulty_target: str = "medium"
    ) -> List[Dict]:
        """
        Select optimal examples for query.
        
        Args:
            query: Task description
            num_examples: Number of examples to return
            diversity_weight: Balance between similarity and diversity (0-1)
            difficulty_target: Target difficulty (easy|medium|hard)
        
        Returns:
            List of examples with metadata
        """
        
        # 1. Semantic search for candidate examples
        candidates = self.mcp.call_tool("lookup", {
            "query": f"example: {query}",
            "limit": num_examples * 3,  # Get more candidates
            "threshold": 0.3
        })
        
        if not candidates.get('results'):
            return self._get_fallback_examples(query, num_examples)
        
        # 2. Load example details
        examples = []
        for result in candidates['results']:
            example_data = self._load_example(result['path'])
            if example_data:
                example_data['similarity'] = result['score']
                examples.append(example_data)
        
        # 3. Score examples (similarity + diversity + difficulty)
        scored_examples = self._score_examples(
            examples=examples,
            query=query,
            diversity_weight=diversity_weight,
            difficulty_target=difficulty_target
        )
        
        # 4. Select top examples
        selected = sorted(
            scored_examples,
            key=lambda x: x['final_score'],
            reverse=True
        )[:num_examples]
        
        return selected
    
    def _load_example(self, filepath: str) -> Dict:
        """Load example from file."""
        
        full_path = self.memory_path.parent / filepath
        
        if not full_path.exists():
            return None
        
        content = full_path.read_text()
        
        # Parse example structure
        # Expected format:
        # ---
        # input: [task description]
        # output: [expected output]
        # difficulty: easy|medium|hard
        # tags: [tag1, tag2, ...]
        # ---
        
        import yaml
        
        parts = content.split('---')
        if len(parts) < 3:
            return None
        
        try:
            metadata = yaml.safe_load(parts[1])
            
            return {
                'input': metadata.get('input', ''),
                'output': metadata.get('output', ''),
                'difficulty': metadata.get('difficulty', 'medium'),
                'tags': metadata.get('tags', []),
                'explanation': metadata.get('explanation', ''),
                'filepath': filepath
            }
        except Exception as e:
            print(f"Error loading example {filepath}: {e}")
            return None
    
    def _score_examples(
        self,
        examples: List[Dict],
        query: str,
        diversity_weight: float,
        difficulty_target: str
    ) -> List[Dict]:
        """Score examples based on multiple criteria."""
        
        # Generate query embedding
        query_embedding = self.embedding_model.encode(query)
        
        # Generate example embeddings
        example_embeddings = [
            self.embedding_model.encode(ex['input'])
            for ex in examples
        ]
        
        # Calculate similarity to query
        similarities = cosine_similarity(
            [query_embedding],
            example_embeddings
        )[0]
        
        # Calculate diversity (dissimilarity to other examples)
        diversity_scores = []
        for i, emb_i in enumerate(example_embeddings):
            # Average dissimilarity to all other examples
            dissimilarities = [
                1 - cosine_similarity([emb_i], [emb_j])[0][0]
                for j, emb_j in enumerate(example_embeddings)
                if i != j
            ]
            diversity_scores.append(
                np.mean(dissimilarities) if dissimilarities else 0.5
            )
        
        # Calculate difficulty match
        difficulty_map = {'easy': 0, 'medium': 1, 'hard': 2}
        target_difficulty = difficulty_map.get(difficulty_target, 1)
        
        difficulty_scores = [
            1 - abs(difficulty_map.get(ex['difficulty'], 1) - target_difficulty) / 2
            for ex in examples
        ]
        
        # Combine scores
        for i, example in enumerate(examples):
            similarity_score = similarities[i]
            diversity_score = diversity_scores[i]
            difficulty_score = difficulty_scores[i]
            
            # Weighted combination
            final_score = (
                similarity_score * (1 - diversity_weight) +
                diversity_score * diversity_weight +
                difficulty_score * 0.2
            )
            
            example['similarity_score'] = similarity_score
            example['diversity_score'] = diversity_score
            example['difficulty_score'] = difficulty_score
            example['final_score'] = final_score
        
        return examples
    
    def _get_fallback_examples(
        self,
        query: str,
        num_examples: int
    ) -> List[Dict]:
        """Get fallback examples when search fails."""
        
        # Return generic examples from examples/fallback/
        fallback_path = self.examples_path / "fallback"
        
        if not fallback_path.exists():
            return []
        
        examples = []
        for example_file in fallback_path.glob("*.md"):
            example_data = self._load_example(str(example_file))
            if example_data:
                examples.append(example_data)
        
        return examples[:num_examples]
    
    def add_example(
        self,
        input_text: str,
        output_text: str,
        difficulty: str = "medium",
        tags: List[str] = None,
        explanation: str = ""
    ) -> str:
        """
        Add new example to library.
        
        Args:
            input_text: Input/task description
            output_text: Expected output
            difficulty: easy|medium|hard
            tags: Categorization tags
            explanation: Optional explanation
        
        Returns:
            Path to created example file
        """
        
        import hashlib
        from datetime import datetime
        
        # Generate filename from input hash
        input_hash = hashlib.md5(input_text.encode()).hexdigest()[:8]
        filename = f"example-{input_hash}.md"
        filepath = self.examples_path / filename
        
        # Create example content
        content = f"""---
input: {input_text}
output: {output_text}
difficulty: {difficulty}
tags: {tags or []}
explanation: {explanation}
created: {datetime.now().isoformat()}
---

# Example: {input_text[:50]}...

## Input
{input_text}

## Expected Output
{output_text}

## Explanation
{explanation}
"""
        
        filepath.write_text(content)
        
        return str(filepath)


# Example usage
selector = DynamicExampleSelector(
    mcp_client=mcp_client,
    embedding_model=embedding_model,
    memory_path=Path(".claude")
)

# Add examples to library
selector.add_example(
    input_text="Implement user authentication with JWT",
    output_text="""```python
def authenticate_user(username: str, password: str) -> Token:
    user = User.get_by_username(username)
    if not user or not user.verify_password(password):
        raise AuthenticationError()
    
    return generate_jwt(user.id, expires_in=900)
```""",
    difficulty="medium",
    tags=["authentication", "jwt", "security"],
    explanation="Uses password verification with JWT token generation"
)

# Select examples for new query
examples = selector.select_examples(
    query="Build OAuth2 authentication",
    num_examples=3,
    diversity_weight=0.3,
    difficulty_target="medium"
)

print(f"Selected {len(examples)} examples:")
for ex in examples:
    print(f"  - {ex['input'][:50]}... (score: {ex['final_score']:.2f})")
```

### 2.2 Example Quality Metrics

**Evaluate example effectiveness**:

```python
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class ExampleQualityMetrics:
    """Metrics for example quality."""
    clarity: float  # 0-1: How clear is the example?
    representativeness: float  # 0-1: How typical is this example?
    difficulty: float  # 0-1: Difficulty level
    uniqueness: float  # 0-1: How different from other examples?
    completeness: float  # 0-1: Does it show all necessary parts?
    overall_score: float  # Weighted combination


class ExampleQualityEvaluator:
    """
    Evaluate quality of few-shot examples.
    """
    
    def __init__(self, embedding_model):
        self.embedding_model = embedding_model
    
    def evaluate_example(
        self,
        example: Dict,
        other_examples: List[Dict] = None,
        validation_set: List[Dict] = None
    ) -> ExampleQualityMetrics:
        """
        Evaluate single example quality.
        
        Args:
            example: Example to evaluate
            other_examples: Other examples in few-shot set
            validation_set: Broader set of examples for comparison
        
        Returns:
            Quality metrics
        """
        
        # 1. Clarity (based on length, structure, specificity)
        clarity = self._evaluate_clarity(example)
        
        # 2. Representativeness (similarity to validation set)
        representativeness = 0.5
        if validation_set:
            representativeness = self._evaluate_representativeness(
                example, validation_set
            )
        
        # 3. Difficulty
        difficulty = self._evaluate_difficulty(example)
        
        # 4. Uniqueness (dissimilarity to other examples)
        uniqueness = 0.5
        if other_examples:
            uniqueness = self._evaluate_uniqueness(example, other_examples)
        
        # 5. Completeness
        completeness = self._evaluate_completeness(example)
        
        # Overall score (weighted)
        overall = (
            clarity * 0.25 +
            representativeness * 0.20 +
            difficulty * 0.15 +
            uniqueness * 0.20 +
            completeness * 0.20
        )
        
        return ExampleQualityMetrics(
            clarity=clarity,
            representativeness=representativeness,
            difficulty=difficulty,
            uniqueness=uniqueness,
            completeness=completeness,
            overall_score=overall
        )
    
    def _evaluate_clarity(self, example: Dict) -> float:
        """Evaluate example clarity."""
        
        input_text = example['input']
        output_text = example['output']
        
        clarity_score = 1.0
        
        # Penalize if too short (vague)
        if len(input_text) < 20:
            clarity_score -= 0.3
        
        # Penalize if too long (verbose)
        if len(input_text) > 500:
            clarity_score -= 0.2
        
        # Reward if has clear structure (code blocks, lists, etc.)
        if '```' in output_text or any(marker in output_text for marker in ['1.', '2.', '-', '*']):
            clarity_score += 0.2
        
        # Reward if has explanation
        if example.get('explanation'):
            clarity_score += 0.1
        
        return max(0, min(1, clarity_score))
    
    def _evaluate_representativeness(
        self,
        example: Dict,
        validation_set: List[Dict]
    ) -> float:
        """Evaluate how representative example is."""
        
        # Embed example
        example_emb = self.embedding_model.encode(example['input'])
        
        # Embed validation set
        val_embeddings = [
            self.embedding_model.encode(val['input'])
            for val in validation_set
        ]
        
        # Calculate average similarity to validation set
        similarities = cosine_similarity(
            [example_emb],
            val_embeddings
        )[0]
        
        return np.mean(similarities)
    
    def _evaluate_difficulty(self, example: Dict) -> float:
        """Estimate example difficulty."""
        
        # Simple heuristics (in production, use trained model)
        difficulty_indicators = {
            'easy': ['simple', 'basic', 'straightforward'],
            'hard': ['complex', 'advanced', 'sophisticated', 'multiple']
        }
        
        input_lower = example['input'].lower()
        output_length = len(example['output'])
        
        # Count easy/hard indicators
        easy_count = sum(1 for word in difficulty_indicators['easy'] if word in input_lower)
        hard_count = sum(1 for word in difficulty_indicators['hard'] if word in input_lower)
        
        # Longer outputs typically harder
        length_factor = min(output_length / 1000, 1.0)
        
        # Combine
        difficulty = 0.5 + (hard_count - easy_count) * 0.1 + length_factor * 0.3
        
        return max(0, min(1, difficulty))
    
    def _evaluate_uniqueness(
        self,
        example: Dict,
        other_examples: List[Dict]
    ) -> float:
        """Evaluate how unique example is."""
        
        # Embed example
        example_emb = self.embedding_model.encode(example['input'])
        
        # Embed other examples
        other_embeddings = [
            self.embedding_model.encode(other['input'])
            for other in other_examples
        ]
        
        # Calculate dissimilarity to others
        similarities = cosine_similarity(
            [example_emb],
            other_embeddings
        )[0]
        
        # Uniqueness = 1 - average similarity
        return 1 - np.mean(similarities)
    
    def _evaluate_completeness(self, example: Dict) -> float:
        """Evaluate if example shows all necessary components."""
        
        completeness = 0.5
        
        # Has input
        if example.get('input'):
            completeness += 0.2
        
        # Has output
        if example.get('output'):
            completeness += 0.2
        
        # Has explanation
        if example.get('explanation'):
            completeness += 0.1
        
        return min(1, completeness)
    
    def rank_examples(
        self,
        examples: List[Dict],
        validation_set: List[Dict] = None
    ) -> List[Tuple[Dict, ExampleQualityMetrics]]:
        """
        Rank examples by quality.
        
        Returns:
            List of (example, metrics) sorted by overall score
        """
        
        evaluated = []
        
        for i, example in enumerate(examples):
            # Get other examples (excluding current)
            other_examples = examples[:i] + examples[i+1:]
            
            metrics = self.evaluate_example(
                example=example,
                other_examples=other_examples,
                validation_set=validation_set
            )
            
            evaluated.append((example, metrics))
        
        # Sort by overall score
        return sorted(evaluated, key=lambda x: x[1].overall_score, reverse=True)


# Example usage
evaluator = ExampleQualityEvaluator(embedding_model=embedding_model)

# Evaluate example set
examples = [
    {
        'input': 'Implement user login',
        'output': 'def login(user, pass): ...',
        'explanation': 'Basic login function'
    },
    {
        'input': 'Create JWT authentication with refresh tokens',
        'output': '```python\ndef authenticate():\n  ...\n```',
        'explanation': 'Complete auth system with token refresh'
    }
]

ranked = evaluator.rank_examples(examples)

print("Example Quality Ranking:")
for i, (example, metrics) in enumerate(ranked, 1):
    print(f"\n{i}. {example['input']}")
    print(f"   Overall Score: {metrics.overall_score:.2f}")
    print(f"   Clarity: {metrics.clarity:.2f}")
    print(f"   Uniqueness: {metrics.uniqueness:.2f}")
    print(f"   Completeness: {metrics.completeness:.2f}")
```

### 2.3 Contrastive Few-Shot Learning

**Show good AND bad examples**:

```python
class ContrastiveFewShotPrompt:
    """
    Build prompts with positive and negative examples.
    
    Based on: Contrastive Chain-of-Thought prompting.
    """
    
    def __init__(self):
        self.good_examples = []
        self.bad_examples = []
    
    def add_good_example(
        self,
        input_text: str,
        output_text: str,
        why_good: str
    ):
        """Add positive example."""
        self.good_examples.append({
            'input': input_text,
            'output': output_text,
            'rationale': why_good
        })
    
    def add_bad_example(
        self,
        input_text: str,
        output_text: str,
        why_bad: str
    ):
        """Add negative example."""
        self.bad_examples.append({
            'input': input_text,
            'output': output_text,
            'rationale': why_bad
        })
    
    def build_prompt(self, query: str) -> str:
        """Build contrastive prompt."""
        
        prompt = f"""Task: {query}

I'll show you examples of good and bad approaches to learn from.

"""
        
        # Good examples
        prompt += "## ✅ Good Examples (Follow These Patterns):\n\n"
        
        for i, example in enumerate(self.good_examples, 1):
            prompt += f"### Good Example {i}\n"
            prompt += f"**Input**: {example['input']}\n\n"
            prompt += f"**Output**:\n{example['output']}\n\n"
            prompt += f"**Why This Works**: {example['rationale']}\n\n"
        
        # Bad examples
        prompt += "## ❌ Bad Examples (Avoid These Patterns):\n\n"
        
        for i, example in enumerate(self.bad_examples, 1):
            prompt += f"### Bad Example {i}\n"
            prompt += f"**Input**: {example['input']}\n\n"
            prompt += f"**Output**:\n{example['output']}\n\n"
            prompt += f"**Why This Fails**: {example['rationale']}\n\n"
        
        prompt += """## Your Task

Now complete the task following the good examples and avoiding the bad examples.

**Requirements**:
1. Follow the patterns demonstrated in good examples
2. Avoid the pitfalls shown in bad examples
3. Explain your approach briefly

Begin:
"""
        
        return prompt


# Example: Code review comments
contrastive_prompt = ContrastiveFewShotPrompt()

# Good examples
contrastive_prompt.add_good_example(
    input_text="Review this function: `def calc(x): return x*2+5`",
    output_text="""**Issue**: Function name `calc` is vague
**Suggestion**: Rename to `double_and_add_five` for clarity
**Code**:
```python
def double_and_add_five(x: int) -> int:
    \"\"\"Double input and add 5.\"\"\"
    return x * 2 + 5
```
**Severity**: Low (readability improvement)""",
    why_good="Specific, actionable, includes code example, appropriate severity"
)

contrastive_prompt.add_good_example(
    input_text="Review this: `password = input('Password:')`",
    output_text="""**Issue**: Password stored in plain text variable
**Security Risk**: HIGH - password visible in logs/debugger
**Suggestion**: Use `getpass` module
**Code**:
```python
import getpass
password = getpass.getpass('Password: ')
# Process immediately, don't store
authenticate(password)
```
**Severity**: Critical (security vulnerability)""",
    why_good="Identifies security issue, explains risk, provides secure alternative"
)

# Bad examples
contrastive_prompt.add_bad_example(
    input_text="Review this function: `def process_data(data): ...`",
    output_text="This code is bad. Rewrite it.",
    why_bad="No specific issues identified, no actionable suggestions, no explanation"
)

contrastive_prompt.add_bad_example(
    input_text="Review this: `result = api.call()`",
    output_text="""**Issue**: This could be better
**Suggestion**: Add error handling
**Code**:
```python
try:
    result = api.call()
except:
    pass
```""",
    why_bad="Bare except clause is anti-pattern, 'pass' silently swallows errors"
)

# Generate prompt for new review
review_prompt = contrastive_prompt.build_prompt(
    "Review this code: `users = User.query.all()`"
)

print(review_prompt)
```

---

## 3. Chain-of-Thought Mastery

### 3.1 Zero-Shot Chain-of-Thought

**Simple "Let's think step by step" prompting**:

```python
ZERO_SHOT_COT_PROMPT = """Solve this problem step by step.

**Problem**: {problem}

**Instructions**:
1. Break down the problem into smaller steps
2. Solve each step systematically
3. Show your reasoning for each step
4. Arrive at the final answer

Let's think step by step:
"""


def zero_shot_cot(problem: str) -> str:
    """Create zero-shot CoT prompt."""
    return ZERO_SHOT_COT_PROMPT.format(problem=problem)


# Example
problem = "If a store has 15 apples and sells 2/3 of them, how many remain?"

prompt = zero_shot_cot(problem)
print(prompt)

# Expected reasoning:
# Step 1: Calculate 2/3 of 15 apples
# 2/3 * 15 = 10 apples sold
#
# Step 2: Subtract sold from total
# 15 - 10 = 5 apples remaining
#
# Answer: 5 apples remain
```

### 3.2 Few-Shot Chain-of-Thought

**CoT with examples**:

```python
class FewShotCoTPrompt:
    """
    Few-shot Chain-of-Thought prompting.
    """
    
    def __init__(self):
        self.examples = []
    
    def add_example(
        self,
        problem: str,
        reasoning: str,
        answer: str
    ):
        """Add CoT example."""
        self.examples.append({
            'problem': problem,
            'reasoning': reasoning,
            'answer': answer
        })
    
    def build_prompt(self, problem: str) -> str:
        """Build few-shot CoT prompt."""
        
        prompt = "Solve problems by thinking step-by-step.\n\n"
        
        # Add examples
        for i, ex in enumerate(self.examples, 1):
            prompt += f"**Example {i}**\n"
            prompt += f"Problem: {ex['problem']}\n\n"
            prompt += f"Reasoning:\n{ex['reasoning']}\n\n"
            prompt += f"Answer: {ex['answer']}\n\n"
            prompt += "---\n\n"
        
        # Add current problem
        prompt += f"**Your Turn**\n"
        prompt += f"Problem: {problem}\n\n"
        prompt += "Reasoning:\n"
        
        return prompt


# Build few-shot CoT
fewshot_cot = FewShotCoTPrompt()

# Add examples
fewshot_cot.add_example(
    problem="A recipe needs 2 cups of flour. You're making 3 batches. How much flour total?",
    reasoning="""Step 1: Identify the amount per batch
- Each batch needs 2 cups of flour

Step 2: Multiply by number of batches
- 2 cups/batch × 3 batches = 6 cups

Step 3: Verify the calculation
- 2 + 2 + 2 = 6 ✓""",
    answer="6 cups of flour"
)

fewshot_cot.add_example(
    problem="A store has 100 items. 30% are on sale. How many items are on sale?",
    reasoning="""Step 1: Convert percentage to decimal
- 30% = 0.30

Step 2: Calculate sale items
- 100 items × 0.30 = 30 items

Step 3: Verify makes sense
- 30% of 100 = 30 ✓ (30 is less than half of 100)""",
    answer="30 items on sale"
)

# Generate prompt for new problem
prompt = fewshot_cot.build_prompt(
    "A train travels 60 mph for 2.5 hours. How far does it travel?"
)

print(prompt)
```

### 3.3 Faithful Chain-of-Thought

**Ensure reasoning aligns with facts**:

```python
FAITHFUL_COT_TEMPLATE = """Solve this problem using ONLY verified facts from your knowledge or provided context.

**Problem**: {problem}

**Available Context**:
{context}

**Instructions**:
1. State each fact you'll use (cite source if from context)
2. Show reasoning step-by-step
3. Flag any assumptions or uncertainties
4. If you can't solve with available information, say so

**Reasoning Format**:
```
FACT 1: [Verified fact] (Source: [knowledge/context])
FACT 2: [Verified fact] (Source: [knowledge/context])

STEP 1: [Reasoning using FACT 1]
STEP 2: [Reasoning using FACT 2]
...

ASSUMPTIONS: [Any assumptions made]
UNCERTAINTIES: [What you're not sure about]

ANSWER: [Final answer]
```

Begin your faithful reasoning:
"""


class FaithfulCoT:
    """
    Faithful Chain-of-Thought with fact verification.
    """
    
    def __init__(self, mcp_client):
        self.mcp = mcp_client
    
    def generate_prompt(
        self,
        problem: str,
        search_context: bool = True
    ) -> str:
        """
        Generate faithful CoT prompt with verified context.
        
        Args:
            problem: Problem to solve
            search_context: Whether to search memory for context
        
        Returns:
            Prompt with verified facts
        """
        
        context = ""
        
        if search_context:
            # Search memory for relevant facts
            results = self.mcp.call_tool("lookup", {
                "query": problem,
                "limit": 3,
                "threshold": 0.5
            })
            
            if results.get('results'):
                context = "From Memory:\n"
                for i, result in enumerate(results['results'], 1):
                    context += f"{i}. {result['path']}: {result.get('preview', '')[:200]}...\n"
        
        return FAITHFUL_COT_TEMPLATE.format(
            problem=problem,
            context=context or "No additional context available"
        )


# Example usage
faithful_cot = FaithfulCoT(mcp_client=mcp_client)

prompt = faithful_cot.generate_prompt(
    problem="What authentication method does our system use and why?",
    search_context=True
)

print(prompt)

# Expected reasoning:
# FACT 1: System uses JWT authentication (Source: memory/systemPatterns.md)
# FACT 2: JWT chosen for stateless auth (Source: memory/auth-adr.md)
#
# STEP 1: JWT (JSON Web Tokens) identified in system patterns
# STEP 2: Decision rationale documented in ADR
# STEP 3: Benefits: stateless, scalable, standard
#
# ASSUMPTIONS: Documentation is up-to-date
# UNCERTAINTIES: None for current implementation
#
# ANSWER: System uses JWT authentication because it provides stateless,
# scalable authentication without server-side session storage.
```

### 3.4 Tabular Chain-of-Thought

**Structured table-based reasoning**:

```python
TABULAR_COT_TEMPLATE = """Solve this problem using structured table-based reasoning.

**Problem**: {problem}

**Instructions**:
1. Create a reasoning table with columns: Step | Action | Result | Verification
2. Fill each row systematically
3. Final row should contain the answer

**Reasoning Table**:

| Step | Action | Result | Verification |
|------|--------|--------|--------------|
| 1 | [What you're doing] | [Outcome] | [How you know it's correct] |
| 2 | [Next action] | [Outcome] | [Verification] |
| ... | ... | ... | ... |
| N | [Final step] | **ANSWER: [result]** | [Final check] |

Complete the table:
"""


def tabular_cot(problem: str) -> str:
    """Generate tabular CoT prompt."""
    return TABULAR_COT_TEMPLATE.format(problem=problem)


# Example
prompt = tabular_cot(
    "Calculate total cost: 3 items at $12.50 each, 15% discount, 8% tax"
)

print(prompt)

# Expected table:
# | Step | Action | Result | Verification |
# |------|--------|--------|--------------|
# | 1 | Calculate subtotal | 3 × $12.50 = $37.50 | 12.50 + 12.50 + 12.50 = 37.50 ✓ |
# | 2 | Apply 15% discount | $37.50 × 0.15 = $5.63 off | 15% of $37.50 = $5.625 ≈ $5.63 ✓ |
# | 3 | Calculate discounted price | $37.50 - $5.63 = $31.87 | Subtotal minus discount ✓ |
# | 4 | Calculate 8% tax | $31.87 × 0.08 = $2.55 | 8% of $31.87 = $2.5496 ≈ $2.55 ✓ |
# | 5 | Calculate final total | $31.87 + $2.55 = **$34.42** | Discounted price plus tax ✓ |
```

### 3.5 Domain-Specific CoT Templates

**Pre-built CoT templates for common domains**:

```python
class DomainCoTLibrary:
    """
    Library of domain-specific Chain-of-Thought templates.
    """
    
    def __init__(self, memory_path: Path):
        self.memory_path = Path(memory_path)
        self.templates_path = memory_path / "cot-templates"
        self.templates_path.mkdir(exist_ok=True)
    
    @staticmethod
    def database_design_cot() -> str:
        """CoT template for database design problems."""
        return """Design this database following systematic steps:

**Problem**: {problem}

**Step 1: Identify Entities**
- What are the main "things" we need to store?
- List all entities (users, orders, products, etc.)

**Step 2: Define Relationships**
- How do entities relate to each other?
- One-to-many? Many-to-many? One-to-one?

**Step 3: Determine Attributes**
- What fields does each entity need?
- What are the data types?
- What constraints (NOT NULL, UNIQUE, etc.)?

**Step 4: Identify Keys**
- Primary keys for each table
- Foreign keys for relationships
- Indexes for performance

**Step 5: Normalization Check**
- Is it in 3NF (Third Normal Form)?
- Any redundant data?
- Any potential anomalies?

**Step 6: Create Schema**
```sql
[Your SQL schema here]
```

Complete each step systematically:
"""
    
    @staticmethod
    def security_analysis_cot() -> str:
        """CoT template for security analysis."""
        return """Analyze security following STRIDE methodology:

**System**: {system}

**Step 1: Spoofing Threats**
- Can attackers impersonate legitimate users?
- Authentication weaknesses?
- Token/session vulnerabilities?

**Step 2: Tampering Threats**
- Can data be modified in transit?
- Input validation present?
- Data integrity checks?

**Step 3: Repudiation Threats**
- Can users deny actions?
- Audit logging present?
- Non-repudiation mechanisms?

**Step 4: Information Disclosure**
- Can sensitive data leak?
- Encryption in place?
- Access controls proper?

**Step 5: Denial of Service**
- Can system be overwhelmed?
- Rate limiting present?
- Resource exhaustion possible?

**Step 6: Elevation of Privilege**
- Can users gain unauthorized access?
- Privilege separation enforced?
- Least privilege principle followed?

**Summary**:
| Threat | Risk Level | Mitigation |
|--------|------------|------------|
| [Threat] | High/Med/Low | [Strategy] |

Complete each STRIDE category:
"""
    
    @staticmethod
    def api_design_cot() -> str:
        """CoT template for API design."""
        return """Design this API following REST best practices:

**Requirement**: {requirement}

**Step 1: Resource Identification**
- What resources are we exposing?
- Nouns (not verbs): users, orders, products

**Step 2: URL Structure**
- Collection: /resources
- Single item: /resources/{id}
- Nested: /resources/{id}/subresources

**Step 3: HTTP Methods**
- GET: Read (idempotent, safe)
- POST: Create (non-idempotent)
- PUT: Update/Replace (idempotent)
- PATCH: Partial Update (non-idempotent)
- DELETE: Remove (idempotent)

**Step 4: Request/Response Format**
```json
Request:
{
  "field": "value"
}

Response:
{
  "id": "...",
  "field": "value",
  "created_at": "ISO-8601"
}
```

**Step 5: Status Codes**
- 200 OK, 201 Created, 204 No Content
- 400 Bad Request, 401 Unauthorized, 404 Not Found
- 500 Internal Server Error

**Step 6: Error Handling**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "...",
    "details": [...]
  }
}
```

**Step 7: Pagination/Filtering**
- ?page=1&limit=20
- ?filter[status]=active
- ?sort=-created_at

Complete each step:
"""
    
    @staticmethod
    def performance_optimization_cot() -> str:
        """CoT template for performance optimization."""
        return """Optimize performance systematically:

**Problem**: {problem}

**Step 1: Measure Baseline**
- Current metrics (latency, throughput, resource usage)
- Profiling data
- Bottleneck identification

**Step 2: Identify Hotspots**
- What's slow? (CPU, I/O, Network, Memory)
- Where is time spent?
- What resources are constrained?

**Step 3: Consider Optimizations**

| Optimization | Impact | Effort | Trade-offs |
|--------------|--------|--------|------------|
| Caching | High | Low | Stale data risk |
| Indexing | High | Low | Write slowdown |
| Async I/O | Med | Med | Complexity |
| Batch processing | Med | Low | Latency increase |
| Horizontal scaling | High | High | Cost increase |

**Step 4: Implement Changes**
```[language]
[Optimized code]
```

**Step 5: Measure Improvement**
- New metrics
- Percentage improvement
- Verify no regressions

**Step 6: Validate Trade-offs**
- Acceptable?
- Any new issues introduced?

Complete optimization analysis:
"""
    
    def get_template(self, domain: str, **kwargs) -> str:
        """Get domain-specific CoT template."""
        
        templates = {
            'database': self.database_design_cot,
            'security': self.security_analysis_cot,
            'api': self.api_design_cot,
            'performance': self.performance_optimization_cot
        }
        
        if domain not in templates:
            raise ValueError(f"Unknown domain: {domain}")
        
        template = templates[domain]()
        
        # Format with kwargs
        for key, value in kwargs.items():
            template = template.replace(f'{{{key}}}', str(value))
        
        return template


# Example usage
cot_library = DomainCoTLibrary(memory_path=Path(".claude"))

# Get database design template
db_prompt = cot_library.get_template(
    'database',
    problem="E-commerce system with users, products, orders, and reviews"
)

print(db_prompt)

# Get security analysis template
security_prompt = cot_library.get_template(
    'security',
    system="JWT authentication service with refresh tokens"
)

print(security_prompt)
```

---

## 4. Advanced Reasoning Patterns

### 4.1 Chain of Verification (CoVe)

**Extract claims → Verify → Revise**:

```python
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Claim:
    """Single verifiable claim."""
    text: str
    category: str  # fact, opinion, prediction, assumption
    verifiable: bool
    verification_status: str = "unverified"  # verified, partially_verified, unverified, unknown
    evidence: str = ""


class ChainOfVerification:
    """
    Chain of Verification (CoVe) for reducing hallucinations.
    
    Based on: "Chain-of-Verification Reduces Hallucination in LLMs"
    (Dhuliawala et al., 2023)
    """
    
    def __init__(self, mcp_client, llm_generate_fn):
        self.mcp = mcp_client
        self.llm_generate = llm_generate_fn
    
    def verify_response(
        self,
        original_response: str,
        query: str
    ) -> Dict:
        """
        Verify response using CoVe protocol.
        
        Steps:
        1. Extract claims from response
        2. Verify each claim independently
        3. Classify verification status
        4. Revise response based on verification
        
        Args:
            original_response: Initial LLM response
            query: Original user query
        
        Returns:
            Dict with verified response and metadata
        """
        
        # Step 1: Extract claims
        claims = self._extract_claims(original_response)
        
        # Step 2: Verify each claim independently
        verified_claims = []
        for claim in claims:
            if claim.verifiable:
                verification = self._verify_claim(claim, query)
                verified_claims.append(verification)
            else:
                verified_claims.append(claim)
        
        # Step 3: Calculate confidence
        total_verifiable = sum(1 for c in verified_claims if c.verifiable)
        verified_count = sum(
            1 for c in verified_claims 
            if c.verification_status == "verified"
        )
        
        confidence = verified_count / total_verifiable if total_verifiable > 0 else 0.5
        
        # Step 4: Revise response if needed
        if confidence < 0.7:
            revised_response = self._revise_response(
                original_response, verified_claims
            )
        else:
            revised_response = original_response
        
        return {
            'original_response': original_response,
            'revised_response': revised_response,
            'claims': verified_claims,
            'confidence': confidence,
            'verification_passed': confidence >= 0.7
        }
    
    def _extract_claims(self, response: str) -> List[Claim]:
        """Extract verifiable claims from response."""
        
        # Use LLM to extract claims
        extraction_prompt = f"""Extract factual claims from this text:

Text: {response}

For each claim, specify:
1. The claim text
2. Category (fact/opinion/prediction/assumption)
3. Whether it's verifiable (true/false)

Output as JSON array:
```json
[
  {{
    "text": "claim text",
    "category": "fact",
    "verifiable": true
  }},
  ...
]
```
"""
        
        extraction_result = self.llm_generate(extraction_prompt)
        
        # Parse JSON (simplified - in production, use proper JSON parsing)
        import json
        try:
            claims_data = json.loads(extraction_result.strip('```json\n').strip('\n```'))
            
            claims = [
                Claim(
                    text=c['text'],
                    category=c['category'],
                    verifiable=c['verifiable']
                )
                for c in claims_data
            ]
            
            return claims
        except Exception as e:
            print(f"Error parsing claims: {e}")
            return []
    
    def _verify_claim(self, claim: Claim, original_query: str) -> Claim:
        """
        Verify a claim independently (without original context).
        
        Critical: Don't show original response during verification.
        """
        
        # Generate verification question
        verification_question = f"Verify this claim: {claim.text}"
        
        # Search memory for evidence
        search_results = self.mcp.call_tool("lookup", {
            "query": verification_question,
            "limit": 3,
            "threshold": 0.5
        })
        
        evidence = ""
        if search_results.get('results'):
            evidence = "\n".join(
                f"- {r['path']}: {r.get('preview', '')[:100]}"
                for r in search_results['results']
            )
        
        # Classify verification status
        if evidence:
            claim.verification_status = "verified"
            claim.evidence = evidence
        else:
            # Try to verify with general knowledge
            verification_prompt = f"""Is this claim factually correct?

Claim: {claim.text}

Answer ONLY: VERIFIED | PARTIALLY VERIFIED | UNVERIFIED | UNKNOWN

Explain briefly why.
"""
            
            verification_result = self.llm_generate(verification_prompt)
            
            if "VERIFIED" in verification_result and "UNVERIFIED" not in verification_result:
                claim.verification_status = "verified"
            elif "PARTIALLY VERIFIED" in verification_result:
                claim.verification_status = "partially_verified"
            elif "UNKNOWN" in verification_result:
                claim.verification_status = "unknown"
            else:
                claim.verification_status = "unverified"
            
            claim.evidence = verification_result
        
        return claim
    
    def _revise_response(
        self,
        original_response: str,
        verified_claims: List[Claim]
    ) -> str:
        """Revise response based on verification results."""
        
        # Build revision prompt
        revision_prompt = f"""Original response had some unverified claims. Revise it.

Original Response:
{original_response}

Verification Results:
"""
        
        for claim in verified_claims:
            if claim.verification_status != "verified":
                revision_prompt += f"\n❌ UNVERIFIED: {claim.text}"
                revision_prompt += f"\n   Status: {claim.verification_status}"
        
        revision_prompt += """

Revise the response to:
1. Remove or flag unverified claims
2. Add confidence qualifiers where appropriate
3. Focus on verified information

Revised response:
"""
        
        revised = self.llm_generate(revision_prompt)
        
        return revised


# Example usage
cove = ChainOfVerification(
    mcp_client=mcp_client,
    llm_generate_fn=llm_generate
)

# Initial response (may contain hallucinations)
response = """Our authentication system uses JWT tokens with PKCE. 
The tokens expire after 15 minutes and refresh tokens last 7 days. 
We process over 1 million requests per day."""

result = cove.verify_response(
    original_response=response,
    query="Describe our authentication system"
)

print(f"Confidence: {result['confidence']:.1%}")
print(f"Verification passed: {result['verification_passed']}")
print(f"\nClaims:")
for claim in result['claims']:
    print(f"  - {claim.text}")
    print(f"    Status: {claim.verification_status}")

if result['revised_response'] != result['original_response']:
    print(f"\nRevised Response:\n{result['revised_response']}")
```

### 4.2 Least-to-Most Prompting

**Decompose complex → Solve simple → Compose solution**:

```python
class LeastToMostPrompting:
    """
    Least-to-Most prompting: Break down complex problems.
    
    Based on: "Least-to-Most Prompting Enables Complex Reasoning"
    (Zhou et al., 2022)
    """
    
    def __init__(self, llm_generate_fn):
        self.llm_generate = llm_generate_fn
    
    def solve(
        self,
        problem: str,
        max_depth: int = 3
    ) -> Dict:
        """
        Solve problem using least-to-most decomposition.
        
        Args:
            problem: Complex problem to solve
            max_depth: Maximum decomposition depth
        
        Returns:
            Dict with solution and decomposition tree
        """
        
        # Phase 1: Decompose problem into subproblems
        subproblems = self._decompose(problem, max_depth)
        
        # Phase 2: Solve each subproblem (easiest first)
        solutions = []
        for subproblem in subproblems:
            solution = self._solve_subproblem(
                subproblem,
                previous_solutions=solutions
            )
            solutions.append({
                'subproblem': subproblem,
                'solution': solution
            })
        
        # Phase 3: Compose final solution
        final_solution = self._compose_solution(problem, solutions)
        
        return {
            'problem': problem,
            'subproblems': subproblems,
            'solutions': solutions,
            'final_solution': final_solution
        }
    
    def _decompose(
        self,
        problem: str,
        max_depth: int
    ) -> List[str]:
        """Decompose problem into simpler subproblems."""
        
        decomposition_prompt = f"""Break down this complex problem into {max_depth} simpler subproblems.

**Complex Problem**: {problem}

**Instructions**:
1. Identify {max_depth} subproblems (from easiest to hardest)
2. Each subproblem should be independently solvable
3. Order from simplest to most complex
4. Later subproblems can build on earlier ones

**Subproblems**:
1. [Easiest subproblem]
2. [Medium difficulty]
3. [Most complex - may use results from 1 & 2]

List the subproblems:
"""
        
        result = self.llm_generate(decomposition_prompt)
        
        # Parse subproblems (simplified)
        import re
        subproblems = re.findall(r'\d+\.\s*(.+)', result)
        
        return subproblems[:max_depth]
    
    def _solve_subproblem(
        self,
        subproblem: str,
        previous_solutions: List[Dict]
    ) -> str:
        """Solve single subproblem."""
        
        solve_prompt = f"""Solve this subproblem:

**Subproblem**: {subproblem}
"""
        
        # Add context from previous solutions
        if previous_solutions:
            solve_prompt += "\n**Context from previous subproblems**:\n"
            for prev in previous_solutions:
                solve_prompt += f"- {prev['subproblem']}\n"
                solve_prompt += f"  Solution: {prev['solution'][:100]}...\n"
        
        solve_prompt += "\n**Your solution**:\n"
        
        solution = self.llm_generate(solve_prompt)
        
        return solution
    
    def _compose_solution(
        self,
        original_problem: str,
        solutions: List[Dict]
    ) -> str:
        """Compose final solution from subproblem solutions."""
        
        composition_prompt = f"""Compose the final solution to the original problem.

**Original Problem**: {original_problem}

**Subproblem Solutions**:
"""
        
        for i, sol in enumerate(solutions, 1):
            composition_prompt += f"\n{i}. {sol['subproblem']}\n"
            composition_prompt += f"   Solution: {sol['solution']}\n"
        
        composition_prompt += """

Now synthesize these into a complete solution to the original problem:
"""
        
        final_solution = self.llm_generate(composition_prompt)
        
        return final_solution


# Example usage
l2m = LeastToMostPrompting(llm_generate_fn=llm_generate)

result = l2m.solve(
    problem="Design and implement a complete OAuth2 authentication system with PKCE",
    max_depth=3
)

print(f"Problem: {result['problem']}\n")
print("Subproblems:")
for i, subp in enumerate(result['subproblems'], 1):
    print(f"  {i}. {subp}")

print(f"\nFinal Solution:\n{result['final_solution']}")
```

### 4.3 Program of Thoughts

**Generate executable code for reasoning**:

```python
class ProgramOfThoughts:
    """
    Program of Thoughts: Use code for reasoning.
    
    Based on: "Program of Thoughts Prompting"
    (Chen et al., 2022)
    """
    
    def __init__(self):
        self.execution_history = []
    
    def solve(
        self,
        problem: str,
        language: str = "python"
    ) -> Dict:
        """
        Solve problem by generating and executing code.
        
        Args:
            problem: Problem to solve
            language: Programming language (python/javascript/etc)
        
        Returns:
            Dict with code, result, and reasoning
        """
        
        # Generate problem-solving code
        code_prompt = f"""Solve this problem by writing executable {language} code.

**Problem**: {problem}

**Instructions**:
1. Write code that solves the problem step-by-step
2. Use comments to explain your reasoning
3. Print intermediate steps for verification
4. Return the final answer

**Code**:
```{language}
# Your solution here
```
"""
        
        # In production, call LLM
        code = self._generate_code(code_prompt, language)
        
        # Execute code safely
        result = self._execute_code(code, language)
        
        # Store in history
        self.execution_history.append({
            'problem': problem,
            'code': code,
            'result': result
        })
        
        return {
            'problem': problem,
            'code': code,
            'result': result,
            'success': result.get('success', False)
        }
    
    def _generate_code(self, prompt: str, language: str) -> str:
        """Generate problem-solving code."""
        
        # Simplified - in production, use actual LLM
        if language == "python":
            return """
# Solve the problem step by step
def solve():
    # Step 1: Parse the problem
    print("Step 1: Understanding the problem")
    
    # Step 2: Identify variables
    print("Step 2: Identifying variables")
    
    # Step 3: Solve
    print("Step 3: Solving")
    result = 42  # Placeholder
    
    # Step 4: Verify
    print("Step 4: Verification")
    assert result > 0, "Result should be positive"
    
    return result

answer = solve()
print(f"Final Answer: {answer}")
"""
        
        return ""
    
    def _execute_code(self, code: str, language: str) -> Dict:
        """Execute code safely and capture output."""
        
        if language == "python":
            import io
            import sys
            
            # Capture stdout
            old_stdout = sys.stdout
            sys.stdout = captured_output = io.StringIO()
            
            try:
                # Execute code
                exec_globals = {}
                exec(code, exec_globals)
                
                # Get output
                output = captured_output.getvalue()
                
                # Restore stdout
                sys.stdout = old_stdout
                
                return {
                    'success': True,
                    'output': output,
                    'error': None
                }
            
            except Exception as e:
                sys.stdout = old_stdout
                
                return {
                    'success': False,
                    'output': captured_output.getvalue(),
                    'error': str(e)
                }
        
        return {'success': False, 'error': 'Unsupported language'}


# Example usage
pot = ProgramOfThoughts()

result = pot.solve(
    problem="Calculate compound interest: $1000 principal, 5% annual rate, 3 years, compounded monthly"
)

print(f"Code:\n{result['code']}\n")
print(f"Output:\n{result['result']['output']}")
```

### 4.4 Thread of Thoughts

**Multi-threaded parallel reasoning**:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

class ThreadOfThoughts:
    """
    Thread of Thoughts: Parallel reasoning paths.
    
    Explore multiple reasoning approaches simultaneously.
    """
    
    def __init__(self, llm_generate_fn, max_threads: int = 3):
        self.llm_generate = llm_generate_fn
        self.max_threads = max_threads
    
    def solve(
        self,
        problem: str,
        perspectives: List[str] = None
    ) -> Dict:
        """
        Solve problem from multiple perspectives simultaneously.
        
        Args:
            problem: Problem to solve
            perspectives: Different angles to explore
        
        Returns:
            Dict with solutions from each thread
        """
        
        if perspectives is None:
            perspectives = [
                "analytical approach",
                "intuitive approach",
                "systematic approach"
            ]
        
        # Launch parallel reasoning threads
        threads = {}
        
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            # Submit each perspective as separate thread
            futures = {
                executor.submit(
                    self._reason_from_perspective,
                    problem,
                    perspective
                ): perspective
                for perspective in perspectives
            }
            
            # Collect results as they complete
            for future in as_completed(futures):
                perspective = futures[future]
                try:
                    result = future.result()
                    threads[perspective] = result
                except Exception as e:
                    threads[perspective] = {'error': str(e)}
        
        # Synthesize results
        synthesis = self._synthesize_threads(problem, threads)
        
        return {
            'problem': problem,
            'perspectives': perspectives,
            'threads': threads,
            'synthesis': synthesis
        }
    
    def _reason_from_perspective(
        self,
        problem: str,
        perspective: str
    ) -> Dict:
        """Reason from specific perspective."""
        
        perspective_prompt = f"""Solve this problem from a {perspective}:

**Problem**: {problem}

**Your Perspective**: {perspective}

**Instructions**:
Use this perspective to approach the problem. Focus on what this perspective reveals.

**Reasoning**:
"""
        
        result = self.llm_generate(perspective_prompt)
        
        return {
            'perspective': perspective,
            'reasoning': result
        }
    
    def _synthesize_threads(
        self,
        problem: str,
        threads: Dict
    ) -> str:
        """Synthesize insights from all threads."""
        
        synthesis_prompt = f"""Synthesize insights from multiple reasoning perspectives:

**Problem**: {problem}

**Perspectives**:
"""
        
        for perspective, result in threads.items():
            synthesis_prompt += f"\n**{perspective}**:\n"
            synthesis_prompt += f"{result.get('reasoning', result.get('error'))}\n"
        
        synthesis_prompt += """

**Synthesis**:
1. What common insights emerge across perspectives?
2. What unique insights does each perspective provide?
3. What is the most comprehensive solution combining all insights?

Your synthesis:
"""
        
        synthesis = self.llm_generate(synthesis_prompt)
        
        return synthesis


# Example usage
tot = ThreadOfThoughts(llm_generate_fn=llm_generate, max_threads=3)

result = tot.solve(
    problem="Should we migrate from monolith to microservices?",
    perspectives=[
        "technical scalability perspective",
        "operational complexity perspective",
        "business value perspective"
    ]
)

print(f"Problem: {result['problem']}\n")
print("Thread Results:")
for perspective, thread in result['threads'].items():
    print(f"\n{perspective}:")
    print(f"{thread.get('reasoning', 'N/A')[:200]}...")

print(f"\nSynthesis:\n{result['synthesis']}")
```

### 4.5 Step-Back Prompting

**Abstract problem → Solve abstract → Apply to specific**:

```python
STEP_BACK_TEMPLATE = """Let's solve this by first stepping back to understand the general principle.

**Specific Problem**: {specific_problem}

**Step 1: Step Back**
What is the general principle or concept behind this specific problem?

General Question: {general_question}

**Step 2: Answer General Question**
[Explain the general principle]

**Step 3: Apply to Specific**
Now apply this general understanding to solve the specific problem.

**Solution**:
"""


class StepBackPrompting:
    """
    Step-Back prompting: Abstract before solving.
    
    Based on: "Take a Step Back: Evoking Reasoning via Abstraction"
    (Zheng et al., 2023)
    """
    
    def __init__(self, llm_generate_fn):
        self.llm_generate = llm_generate_fn
    
    def solve(self, specific_problem: str) -> Dict:
        """
        Solve by first abstracting to general principle.
        
        Args:
            specific_problem: Specific problem to solve
        
        Returns:
            Dict with general principle and specific solution
        """
        
        # Step 1: Generate step-back question
        general_question = self._generate_step_back_question(
            specific_problem
        )
        
        # Step 2: Answer general question
        general_answer = self._answer_general_question(
            general_question
        )
        
        # Step 3: Apply to specific problem
        specific_solution = self._apply_to_specific(
            specific_problem,
            general_question,
            general_answer
        )
        
        return {
            'specific_problem': specific_problem,
            'general_question': general_question,
            'general_answer': general_answer,
            'specific_solution': specific_solution
        }
    
    def _generate_step_back_question(
        self,
        specific_problem: str
    ) -> str:
        """Generate abstract general question."""
        
        prompt = f"""What is the general principle behind this specific problem?

Specific: {specific_problem}

General question (abstract the core concept):
"""
        
        return self.llm_generate(prompt)
    
    def _answer_general_question(self, general_question: str) -> str:
        """Answer the general question."""
        
        prompt = f"""Answer this general question:

{general_question}

Explain the general principle thoroughly:
"""
        
        return self.llm_generate(prompt)
    
    def _apply_to_specific(
        self,
        specific_problem: str,
        general_question: str,
        general_answer: str
    ) -> str:
        """Apply general principle to specific problem."""
        
        prompt = f"""Apply this general principle to solve the specific problem:

**General Principle**:
Question: {general_question}
Answer: {general_answer}

**Specific Problem**: {specific_problem}

**Solution** (applying the general principle):
"""
        
        return self.llm_generate(prompt)


# Example usage
step_back = StepBackPrompting(llm_generate_fn=llm_generate)

result = step_back.solve(
    specific_problem="How should we handle rate limiting in our API gateway?"
)

print(f"Specific Problem: {result['specific_problem']}\n")
print(f"General Question: {result['general_question']}\n")
print(f"General Answer: {result['general_answer']}\n")
print(f"Specific Solution: {result['specific_solution']}")
```

---

## 5. Prompt Optimization & Testing

### 5.1 Prompt Registry with Versioning

**Track and version prompts systematically**:

```python
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, List, Optional
import hashlib
import json

@dataclass
class PromptVersion:
    """Single version of a prompt."""
    version_id: str  # Semantic version (1.0.0)
    prompt_text: str
    prompt_hash: str
    created_at: str
    created_by: str
    
    # Deployment
    deployment_status: str  # draft, staged, active, deprecated
    deployed_at: Optional[str] = None
    deployed_by: Optional[str] = None
    
    # Exploration path
    exploration_path: str = ""  # "root → A → A.1 → A.1.2"
    techniques: List[str] = None
    complexity: str = "medium"
    
    # Performance
    predicted_quality: float = 0.0
    baseline_accuracy: Optional[float] = None
    baseline_latency_p50: Optional[float] = None
    baseline_latency_p95: Optional[float] = None
    
    # Rollback
    rollback_reference: Optional[str] = None
    auto_rollback_enabled: bool = False
    
    def __post_init__(self):
        if self.techniques is None:
            self.techniques = []


class PromptRegistry:
    """
    Production prompt registry with versioning.
    """
    
    def __init__(self, registry_path: Path):
        self.registry_path = Path(registry_path)
        self.registry_path.mkdir(exist_ok=True)
        
        self.prompts_file = registry_path / "prompts.json"
        self.versions_dir = registry_path / "versions"
        self.versions_dir.mkdir(exist_ok=True)
        
        # Load existing registry
        self.registry = self._load_registry()
    
    def _load_registry(self) -> Dict:
        """Load prompt registry from disk."""
        if self.prompts_file.exists():
            with open(self.prompts_file) as f:
                return json.load(f)
        return {}
    
    def _save_registry(self):
        """Save prompt registry to disk."""
        with open(self.prompts_file, 'w') as f:
            json.dump(self.registry, f, indent=2)
    
    def register(
        self,
        prompt_id: str,
        prompt_text: str,
        version: str,
        created_by: str = "system",
        **metadata
    ) -> PromptVersion:
        """
        Register new prompt version.
        
        Args:
            prompt_id: Unique identifier for prompt
            prompt_text: Full prompt content
            version: Semantic version (1.0.0)
            created_by: Creator identifier
            **metadata: Additional metadata
        
        Returns:
            PromptVersion object
        """
        
        # Generate hash for integrity
        prompt_hash = hashlib.sha256(
            prompt_text.encode()
        ).hexdigest()[:16]
        
        # Create version object
        prompt_version = PromptVersion(
            version_id=version,
            prompt_text=prompt_text,
            prompt_hash=prompt_hash,
            created_at=datetime.now().isoformat(),
            created_by=created_by,
            deployment_status="draft",
            **metadata
        )
        
        # Initialize prompt entry if new
        if prompt_id not in self.registry:
            self.registry[prompt_id] = {
                'versions': {},
                'active_version': None
            }
        
        # Add version
        self.registry[prompt_id]['versions'][version] = asdict(prompt_version)
        
        # Save to disk
        self._save_registry()
        
        # Save full prompt text separately
        version_file = self.versions_dir / f"{prompt_id}-{version}.txt"
        version_file.write_text(prompt_text)
        
        return prompt_version
    
    def deploy(
        self,
        prompt_id: str,
        version: str,
        deployed_by: str = "system"
    ) -> bool:
        """
        Deploy a prompt version to active.
        
        Args:
            prompt_id: Prompt identifier
            version: Version to deploy
            deployed_by: Deployer identifier
        
        Returns:
            True if successful
        """
        
        if prompt_id not in self.registry:
            raise ValueError(f"Prompt {prompt_id} not found")
        
        if version not in self.registry[prompt_id]['versions']:
            raise ValueError(f"Version {version} not found")
        
        # Get current active version (for rollback)
        current_active = self.registry[prompt_id].get('active_version')
        
        # Update version status
        version_data = self.registry[prompt_id]['versions'][version]
        version_data['deployment_status'] = 'active'
        version_data['deployed_at'] = datetime.now().isoformat()
        version_data['deployed_by'] = deployed_by
        
        # Set rollback reference to current active
        if current_active:
            version_data['rollback_reference'] = current_active
            
            # Deprecate old active version
            old_version_data = self.registry[prompt_id]['versions'][current_active]
            old_version_data['deployment_status'] = 'deprecated'
        
        # Update active version
        self.registry[prompt_id]['active_version'] = version
        
        self._save_registry()
        
        return True
    
    def get_active(self, prompt_id: str) -> str:
        """Get active prompt text."""
        
        if prompt_id not in self.registry:
            raise ValueError(f"Prompt {prompt_id} not found")
        
        active_version = self.registry[prompt_id].get('active_version')
        
        if not active_version:
            raise ValueError(f"No active version for {prompt_id}")
        
        # Load from file
        version_file = self.versions_dir / f"{prompt_id}-{active_version}.txt"
        
        return version_file.read_text()
    
    def rollback(self, prompt_id: str) -> bool:
        """Rollback to previous version."""
        
        if prompt_id not in self.registry:
            raise ValueError(f"Prompt {prompt_id} not found")
        
        current_version = self.registry[prompt_id].get('active_version')
        
        if not current_version:
            raise ValueError("No active version to rollback from")
        
        # Get rollback reference
        current_data = self.registry[prompt_id]['versions'][current_version]
        rollback_ref = current_data.get('rollback_reference')
        
        if not rollback_ref:
            raise ValueError("No rollback reference available")
        
        # Deploy rollback version
        return self.deploy(prompt_id, rollback_ref, deployed_by="auto-rollback")
    
    def list_versions(self, prompt_id: str) -> List[Dict]:
        """List all versions of a prompt."""
        
        if prompt_id not in self.registry:
            return []
        
        versions = []
        for version_id, version_data in self.registry[prompt_id]['versions'].items():
            versions.append({
                'version': version_id,
                'status': version_data['deployment_status'],
                'created_at': version_data['created_at'],
                'deployed_at': version_data.get('deployed_at'),
                'hash': version_data['prompt_hash']
            })
        
        # Sort by version (semantic versioning)
        return sorted(versions, key=lambda v: v['version'], reverse=True)


# Example usage
registry = PromptRegistry(registry_path=Path(".claude/prompts"))

# Register prompt v1.0.0
registry.register(
    prompt_id="code_review",
    prompt_text=code_review_prompt,
    version="1.0.0",
    created_by="engineer@example.com",
    techniques=["few-shot", "cot"],
    complexity="medium"
)

# Deploy to production
registry.deploy(
    prompt_id="code_review",
    version="1.0.0",
    deployed_by="ci/cd-pipeline"
)

# Get active prompt
active_prompt = registry.get_active("code_review")
print(f"Active prompt length: {len(active_prompt)} chars")

# Register improved version
registry.register(
    prompt_id="code_review",
    prompt_text="[Improved prompt with better examples]",
    version="1.1.0",
    created_by="engineer@example.com"
)

# Deploy new version
registry.deploy("code_review", "1.1.0")

# Rollback if issues detected
# registry.rollback("code_review")

# List versions
versions = registry.list_versions("code_review")
print(f"\nVersions:")
for v in versions:
    print(f"  {v['version']}: {v['status']}")
```

### 5.2 A/B Testing Framework

**Test prompt variants systematically**:

```python
from typing import Callable, Dict
import random

class PromptABTest:
    """
    A/B testing framework for prompts.
    """
    
    def __init__(
        self,
        test_name: str,
        control_prompt: str,
        variant_prompts: Dict[str, str],
        allocation: Dict[str, float] = None
    ):
        """
        Initialize A/B test.
        
        Args:
            test_name: Test identifier
            control_prompt: Baseline prompt (variant A)
            variant_prompts: Dict of variant_id → prompt_text
            allocation: Traffic allocation (e.g., {'A': 0.5, 'B': 0.3, 'C': 0.2})
        """
        self.test_name = test_name
        self.prompts = {'A': control_prompt, **variant_prompts}
        
        # Default: equal allocation
        if allocation is None:
            allocation = {
                variant: 1.0 / len(self.prompts)
                for variant in self.prompts
            }
        
        self.allocation = allocation
        self.results = {variant: [] for variant in self.prompts}
    
    def get_variant(self, user_id: str = None) -> str:
        """
        Get variant for user (deterministic if user_id provided).
        
        Args:
            user_id: User identifier for consistent assignment
        
        Returns:
            Variant ID ('A', 'B', etc.)
        """
        
        if user_id:
            # Consistent assignment based on user_id hash
            hash_val = int(hashlib.md5(user_id.encode()).hexdigest(), 16)
            rand_val = (hash_val % 1000) / 1000.0
        else:
            # Random assignment
            rand_val = random.random()
        
        # Allocate based on cumulative distribution
        cumulative = 0
        for variant, prob in sorted(self.allocation.items()):
            cumulative += prob
            if rand_val < cumulative:
                return variant
        
        return list(self.prompts.keys())[0]  # Fallback
    
    def get_prompt(self, variant: str) -> str:
        """Get prompt text for variant."""
        return self.prompts.get(variant, self.prompts['A'])
    
    def record_result(
        self,
        variant: str,
        query: str,
        response: str,
        metrics: Dict
    ):
        """
        Record test result.
        
        Args:
            variant: Variant used
            query: User query
            response: LLM response
            metrics: Performance metrics (latency, quality, etc.)
        """
        
        self.results[variant].append({
            'query': query,
            'response': response,
            'metrics': metrics,
            'timestamp': datetime.now().isoformat()
        })
    
    def analyze_results(self) -> Dict:
        """Analyze test results."""
        
        analysis = {}
        
        for variant, results in self.results.items():
            if not results:
                analysis[variant] = {'sample_size': 0}
                continue
            
            # Calculate aggregates
            sample_size = len(results)
            
            # Latency
            latencies = [r['metrics'].get('latency_ms', 0) for r in results]
            avg_latency = sum(latencies) / len(latencies)
            
            # Quality score
            quality_scores = [r['metrics'].get('quality', 0) for r in results]
            avg_quality = sum(quality_scores) / len(quality_scores)
            
            # Success rate
            successes = sum(1 for r in results if r['metrics'].get('success', False))
            success_rate = successes / sample_size
            
            analysis[variant] = {
                'sample_size': sample_size,
                'avg_latency_ms': avg_latency,
                'avg_quality': avg_quality,
                'success_rate': success_rate
            }
        
        # Determine winner
        if analysis.get('A') and analysis.get('B'):
            # Simple comparison (in production, use statistical significance)
            winner = 'A' if analysis['A']['avg_quality'] > analysis['B']['avg_quality'] else 'B'
            
            analysis['winner'] = winner
            analysis['improvement'] = (
                (analysis[winner]['avg_quality'] - analysis['A']['avg_quality']) /
                analysis['A']['avg_quality'] * 100
                if analysis['A']['avg_quality'] > 0 else 0
            )
        
        return analysis


# Example usage
ab_test = PromptABTest(
    test_name="code_review_improvements",
    control_prompt="[Original code review prompt]",
    variant_prompts={
        'B': "[Prompt with more examples]",
        'C': "[Prompt with stricter guidelines]"
    },
    allocation={'A': 0.34, 'B': 0.33, 'C': 0.33}
)

# Simulate test runs
for i in range(100):
    user_id = f"user_{i}"
    
    # Get variant
    variant = ab_test.get_variant(user_id)
    
    # Get prompt
    prompt = ab_test.get_prompt(variant)
    
    # Simulate LLM call and metrics
    # (in production, actually call LLM)
    simulated_metrics = {
        'latency_ms': random.randint(100, 500),
        'quality': random.uniform(0.7, 0.95),
        'success': random.random() > 0.1
    }
    
    # Record result
    ab_test.record_result(
        variant=variant,
        query="Review this code: ...",
        response="[LLM response]",
        metrics=simulated_metrics
    )

# Analyze results
results = ab_test.analyze_results()

print("A/B Test Results:")
for variant, metrics in results.items():
    if variant != 'winner' and variant != 'improvement':
        print(f"\nVariant {variant}:")
        print(f"  Sample size: {metrics.get('sample_size', 0)}")
        print(f"  Avg latency: {metrics.get('avg_latency_ms', 0):.0f}ms")
        print(f"  Avg quality: {metrics.get('avg_quality', 0):.2%}")
        print(f"  Success rate: {metrics.get('success_rate', 0):.2%}")

if 'winner' in results:
    print(f"\nWinner: Variant {results['winner']}")
    print(f"Improvement: {results['improvement']:.1f}%")
```

### 5.3 Automated Prompt Optimization

**Iteratively improve prompts**:

```python
class PromptOptimizer:
    """
    Automated prompt optimization using feedback.
    """
    
    def __init__(
        self,
        llm_generate_fn: Callable,
        scorer_fn: Callable
    ):
        """
        Initialize optimizer.
        
        Args:
            llm_generate_fn: Function to generate with prompts
            scorer_fn: Function to score output quality (0-1)
        """
        self.llm_generate = llm_generate_fn
        self.scorer = scorer_fn
        self.optimization_history = []
    
    def optimize(
        self,
        initial_prompt: str,
        test_cases: List[Dict],
        iterations: int = 5,
        improvement_threshold: float = 0.05
    ) -> Dict:
        """
        Optimize prompt iteratively.
        
        Args:
            initial_prompt: Starting prompt
            test_cases: List of test cases (input + expected)
            iterations: Max optimization iterations
            improvement_threshold: Min improvement to continue
        
        Returns:
            Dict with optimized prompt and history
        """
        
        current_prompt = initial_prompt
        best_score = 0
        
        for iteration in range(iterations):
            print(f"\nIteration {iteration + 1}/{iterations}")
            
            # Evaluate current prompt
            score = self._evaluate_prompt(current_prompt, test_cases)
            
            print(f"  Current score: {score:.2%}")
            
            # Record
            self.optimization_history.append({
                'iteration': iteration,
                'prompt': current_prompt,
                'score': score
            })
            
            # Check for improvement
            if score > best_score:
                improvement = score - best_score
                best_score = score
                print(f"  Improvement: +{improvement:.2%}")
                
                # Stop if improvement too small
                if improvement < improvement_threshold and iteration > 0:
                    print("  Improvement below threshold, stopping")
                    break
            else:
                print("  No improvement, stopping")
                break
            
            # Generate improved version
            current_prompt = self._improve_prompt(
                current_prompt,
                test_cases,
                score
            )
        
        # Return best prompt
        best_iteration = max(
            self.optimization_history,
            key=lambda x: x['score']
        )
        
        return {
            'optimized_prompt': best_iteration['prompt'],
            'final_score': best_iteration['score'],
            'iterations': len(self.optimization_history),
            'history': self.optimization_history
        }
    
    def _evaluate_prompt(
        self,
        prompt: str,
        test_cases: List[Dict]
    ) -> float:
        """Evaluate prompt quality on test cases."""
        
        scores = []
        
        for test_case in test_cases:
            # Generate response
            full_prompt = prompt.format(**test_case.get('variables', {}))
            full_prompt += "\n\n" + test_case['input']
            
            response = self.llm_generate(full_prompt)
            
            # Score response
            score = self.scorer(
                response,
                test_case.get('expected', ''),
                test_case.get('criteria', {})
            )
            
            scores.append(score)
        
        # Average score
        return sum(scores) / len(scores) if scores else 0
    
    def _improve_prompt(
        self,
        current_prompt: str,
        test_cases: List[Dict],
        current_score: float
    ) -> str:
        """Generate improved prompt version."""
        
        # Analyze failures
        failures = []
        
        for test_case in test_cases:
            full_prompt = current_prompt.format(**test_case.get('variables', {}))
            full_prompt += "\n\n" + test_case['input']
            
            response = self.llm_generate(full_prompt)
            score = self.scorer(response, test_case.get('expected', ''), {})
            
            if score < 0.7:  # Failed test case
                failures.append({
                    'input': test_case['input'],
                    'expected': test_case.get('expected', ''),
                    'actual': response,
                    'score': score
                })
        
        # Generate improvement
        improvement_prompt = f"""Improve this prompt based on failures:

**Current Prompt**:
{current_prompt}

**Current Score**: {current_score:.2%}

**Failures**:
"""
        
        for i, failure in enumerate(failures[:3], 1):  # Show top 3 failures
            improvement_prompt += f"\n{i}. Input: {failure['input'][:100]}..."
            improvement_prompt += f"\n   Expected: {failure['expected'][:100]}..."
            improvement_prompt += f"\n   Got: {failure['actual'][:100]}..."
            improvement_prompt += f"\n   Score: {failure['score']:.2%}\n"
        
        improvement_prompt += """

**Task**: Improve the prompt to address these failures.

**Strategies**:
1. Add more specific instructions
2. Provide better examples
3. Add constraints to prevent failures
4. Improve output format specification

**Improved Prompt**:
"""
        
        improved_prompt = self.llm_generate(improvement_prompt)
        
        return improved_prompt


# Example usage
def simple_scorer(response: str, expected: str, criteria: Dict) -> float:
    """Simple scoring function."""
    # In production, use more sophisticated scoring
    if expected.lower() in response.lower():
        return 1.0
    return 0.5


optimizer = PromptOptimizer(
    llm_generate_fn=llm_generate,
    scorer_fn=simple_scorer
)

result = optimizer.optimize(
    initial_prompt="Explain {topic} clearly and concisely.",
    test_cases=[
        {
            'variables': {'topic': 'recursion'},
            'input': 'What is recursion?',
            'expected': 'function calls itself'
        },
        {
            'variables': {'topic': 'closures'},
            'input': 'What is a closure?',
            'expected': 'function with access to outer scope'
        }
    ],
    iterations=5,
    improvement_threshold=0.05
)

print(f"\nOptimized Prompt:\n{result['optimized_prompt']}")
print(f"Final Score: {result['final_score']:.2%}")
```

---

## 6. Production Deployment

### 6.1 Confidence Calibration System

**Calibrate confidence scores**:

```python
from typing import Dict, List
import numpy as np

class ConfidenceCalibration:
    """
    Calibrate LLM confidence scores to true accuracy.
    
    Maps stated confidence → actual accuracy.
    """
    
    def __init__(self):
        self.calibration_data = []
        self.calibration_curve = None
    
    def record_prediction(
        self,
        stated_confidence: float,
        was_correct: bool
    ):
        """
        Record prediction with confidence and outcome.
        
        Args:
            stated_confidence: LLM's confidence (0-1)
            was_correct: Whether prediction was correct
        """
        
        self.calibration_data.append({
            'confidence': stated_confidence,
            'correct': was_correct
        })
    
    def build_calibration_curve(
        self,
        num_bins: int = 10
    ) -> Dict:
        """
        Build calibration curve from recorded data.
        
        Args:
            num_bins: Number of confidence bins
        
        Returns:
            Calibration curve data
        """
        
        if not self.calibration_data:
            return {}
        
        # Create bins
        bins = np.linspace(0, 1, num_bins + 1)
        
        calibration_curve = []
        
        for i in range(num_bins):
            bin_start = bins[i]
            bin_end = bins[i + 1]
            
            # Get predictions in this bin
            bin_preds = [
                p for p in self.calibration_data
                if bin_start <= p['confidence'] < bin_end
            ]
            
            if not bin_preds:
                continue
            
            # Calculate actual accuracy
            avg_confidence = np.mean([p['confidence'] for p in bin_preds])
            actual_accuracy = np.mean([p['correct'] for p in bin_preds])
            
            calibration_curve.append({
                'bin': i,
                'bin_start': bin_start,
                'bin_end': bin_end,
                'avg_confidence': avg_confidence,
                'actual_accuracy': actual_accuracy,
                'count': len(bin_preds)
            })
        
        self.calibration_curve = calibration_curve
        
        return {
            'curve': calibration_curve,
            'total_samples': len(self.calibration_data),
            'expected_calibration_error': self._calculate_ece(calibration_curve)
        }
    
    def _calculate_ece(self, curve: List[Dict]) -> float:
        """Calculate Expected Calibration Error."""
        
        total_samples = sum(bin_data['count'] for bin_data in curve)
        
        ece = 0
        for bin_data in curve:
            bin_weight = bin_data['count'] / total_samples
            calibration_error = abs(
                bin_data['avg_confidence'] - bin_data['actual_accuracy']
            )
            ece += bin_weight * calibration_error
        
        return ece
    
    def calibrate_confidence(self, stated_confidence: float) -> float:
        """
        Calibrate stated confidence to true probability.
        
        Args:
            stated_confidence: LLM's stated confidence
        
        Returns:
            Calibrated confidence
        """
        
        if not self.calibration_curve:
            return stated_confidence  # No calibration available
        
        # Find appropriate bin
        for bin_data in self.calibration_curve:
            if bin_data['bin_start'] <= stated_confidence < bin_data['bin_end']:
                return bin_data['actual_accuracy']
        
        # Fallback
        return stated_confidence


# Example usage
calibrator = ConfidenceCalibration()

# Simulate predictions
predictions = [
    (0.9, True),   # 90% confident, correct
    (0.9, True),
    (0.9, False),  # 90% confident, wrong
    (0.7, True),
    (0.7, False),
    (0.5, False),
    (0.5, True),
    (0.3, False),
    (0.3, False),
    (0.1, False),
]

for confidence, correct in predictions:
    calibrator.record_prediction(confidence, correct)

# Build calibration curve
curve_data = calibrator.build_calibration_curve(num_bins=5)

print("Calibration Curve:")
for bin_data in curve_data['curve']:
    print(f"  Confidence {bin_data['bin_start']:.1f}-{bin_data['bin_end']:.1f}: "
          f"Stated {bin_data['avg_confidence']:.2%} → "
          f"Actual {bin_data['actual_accuracy']:.2%} "
          f"({bin_data['count']} samples)")

print(f"\nExpected Calibration Error: {curve_data['expected_calibration_error']:.3f}")

# Calibrate new prediction
stated = 0.85
calibrated = calibrator.calibrate_confidence(stated)
print(f"\nStated confidence: {stated:.2%}")
print(f"Calibrated confidence: {calibrated:.2%}")
```

### 6.2 Production Monitoring

**Monitor prompt performance in production**:

```python
from collections import defaultdict
from datetime import datetime, timedelta

class PromptMonitor:
    """
    Monitor prompt performance in production.
    """
    
    def __init__(self, window_minutes: int = 60):
        self.window_minutes = window_minutes
        self.metrics = defaultdict(list)
        self.alerts = []
    
    def record_execution(
        self,
        prompt_id: str,
        prompt_version: str,
        execution_data: Dict
    ):
        """
        Record prompt execution.
        
        Args:
            prompt_id: Prompt identifier
            prompt_version: Version used
            execution_data: Execution metrics
        """
        
        self.metrics[prompt_id].append({
            'version': prompt_version,
            'timestamp': datetime.now(),
            **execution_data
        })
        
        # Check for issues
        self._check_alerts(prompt_id, execution_data)
    
    def _check_alerts(self, prompt_id: str, execution_data: Dict):
        """Check for alert conditions."""
        
        # High latency
        if execution_data.get('latency_ms', 0) > 5000:
            self._raise_alert(
                prompt_id=prompt_id,
                severity="warning",
                message=f"High latency: {execution_data['latency_ms']}ms"
            )
        
        # Low quality
        if execution_data.get('quality_score', 1.0) < 0.5:
            self._raise_alert(
                prompt_id=prompt_id,
                severity="critical",
                message=f"Low quality: {execution_data['quality_score']:.2f}"
            )
        
        # Errors
        if execution_data.get('error'):
            self._raise_alert(
                prompt_id=prompt_id,
                severity="error",
                message=f"Execution error: {execution_data['error']}"
            )
    
    def _raise_alert(
        self,
        prompt_id: str,
        severity: str,
        message: str
    ):
        """Raise monitoring alert."""
        
        alert = {
            'prompt_id': prompt_id,
            'severity': severity,
            'message': message,
            'timestamp': datetime.now()
        }
        
        self.alerts.append(alert)
        
        print(f"[{severity.upper()}] {prompt_id}: {message}")
    
    def get_statistics(self, prompt_id: str) -> Dict:
        """Get performance statistics."""
        
        if prompt_id not in self.metrics:
            return {}
        
        # Filter to time window
        cutoff = datetime.now() - timedelta(minutes=self.window_minutes)
        recent = [
            m for m in self.metrics[prompt_id]
            if m['timestamp'] > cutoff
        ]
        
        if not recent:
            return {'sample_size': 0}
        
        # Calculate stats
        latencies = [m.get('latency_ms', 0) for m in recent]
        quality_scores = [m.get('quality_score', 0) for m in recent]
        errors = sum(1 for m in recent if m.get('error'))
        
        return {
            'sample_size': len(recent),
            'avg_latency_ms': sum(latencies) / len(latencies),
            'p50_latency_ms': np.percentile(latencies, 50),
            'p95_latency_ms': np.percentile(latencies, 95),
            'p99_latency_ms': np.percentile(latencies, 99),
            'avg_quality': sum(quality_scores) / len(quality_scores),
            'error_rate': errors / len(recent),
            'window_minutes': self.window_minutes
        }
    
    def get_alerts(
        self,
        severity: str = None,
        since_minutes: int = 60
    ) -> List[Dict]:
        """Get recent alerts."""
        
        cutoff = datetime.now() - timedelta(minutes=since_minutes)
        
        alerts = [
            a for a in self.alerts
            if a['timestamp'] > cutoff
        ]
        
        if severity:
            alerts = [a for a in alerts if a['severity'] == severity]
        
        return sorted(alerts, key=lambda a: a['timestamp'], reverse=True)


# Example usage
monitor = PromptMonitor(window_minutes=60)

# Simulate production usage
for i in range(100):
    monitor.record_execution(
        prompt_id="code_review",
        prompt_version="1.1.0",
        execution_data={
            'latency_ms': random.randint(100, 800),
            'quality_score': random.uniform(0.7, 0.95),
            'input_tokens': random.randint(100, 500),
            'output_tokens': random.randint(200, 800),
            'error': None if random.random() > 0.05 else "Timeout"
        }
    )

# Get statistics
stats = monitor.get_statistics("code_review")

print("Performance Statistics (last 60 min):")
print(f"  Sample size: {stats['sample_size']}")
print(f"  Avg latency: {stats['avg_latency_ms']:.0f}ms")
print(f"  P95 latency: {stats['p95_latency_ms']:.0f}ms")
print(f"  Avg quality: {stats['avg_quality']:.2%}")
print(f"  Error rate: {stats['error_rate']:.2%}")

# Get alerts
critical_alerts = monitor.get_alerts(severity="critical", since_minutes=60)
print(f"\nCritical alerts: {len(critical_alerts)}")
```

---

## 7. Meta-Orchestration

### 7.1 Intelligent Technique Selection

**Automatically select best prompting technique**:

```python
class PromptTechniqueSelector:
    """
    Intelligently select prompting technique based on task.
    """
    
    def __init__(self):
        self.technique_map = {
            # Task characteristics → Recommended techniques
            'factual_retrieval': ['zero_shot', 'cot', 'cove'],
            'multi_step_reasoning': ['cot', 'least_to_most', 'step_back'],
            'creative_generation': ['tot', 'thread_of_thoughts'],
            'code_generation': ['cot', 'program_of_thoughts'],
            'verification_needed': ['cove', 'self_consistency'],
            'requires_examples': ['few_shot', 'few_shot_cot'],
            'complex_breakdown': ['least_to_most', 'tot'],
            'parallel_perspectives': ['thread_of_thoughts', 'tot']
        }
    
    def select_techniques(
        self,
        task_description: str,
        task_type: str = None
    ) -> List[str]:
        """
        Select optimal techniques for task.
        
        Args:
            task_description: Description of task
            task_type: Optional explicit task type
        
        Returns:
            List of recommended techniques
        """
        
        if task_type:
            return self.technique_map.get(task_type, ['zero_shot'])
        
        # Classify task automatically
        task_lower = task_description.lower()
        
        # Detect characteristics
        characteristics = []
        
        if any(word in task_lower for word in ['verify', 'check', 'validate']):
            characteristics.append('verification_needed')
        
        if any(word in task_lower for word in ['step by step', 'complex', 'breakdown']):
            characteristics.append('multi_step_reasoning')
        
        if any(word in task_lower for word in ['code', 'implement', 'function']):
            characteristics.append('code_generation')
        
        if any(word in task_lower for word in ['creative', 'design', 'brainstorm']):
            characteristics.append('creative_generation')
        
        if not characteristics:
            characteristics = ['factual_retrieval']
        
        # Get techniques for each characteristic
        all_techniques = []
        for char in characteristics:
            all_techniques.extend(self.technique_map.get(char, []))
        
        # Remove duplicates, preserve order
        techniques = []
        for t in all_techniques:
            if t not in techniques:
                techniques.append(t)
        
        return techniques


# Example usage
selector = PromptTechniqueSelector()

# Test different tasks
tasks = [
    "Verify this claim about JWT expiration times",
    "Design a complex authentication system with multiple factors",
    "Implement a rate limiter function in Python",
    "Brainstorm creative solutions for API versioning"
]

for task in tasks:
    techniques = selector.select_techniques(task)
    print(f"\nTask: {task[:60]}...")
    print(f"Recommended: {', '.join(techniques)}")
```

### 7.2 Complete SPES Integration

**Putting it all together**:

```python
class SPESPromptEngineeringSystem:
    """
    Complete SPES prompt engineering system.
    
    Integrates:
    - Memory-first prompts
    - Advanced reasoning techniques
    - Prompt registry
    - A/B testing
    - Monitoring
    - Meta-cognitive workflows (from Document 19)
    """
    
    def __init__(
        self,
        memory_path: Path,
        mcp_client,
        llm_generate_fn
    ):
        self.memory_path = Path(memory_path)
        self.mcp = mcp_client
        self.llm_generate = llm_generate_fn
        
        # Initialize components
        self.prompt_registry = PromptRegistry(
            registry_path=memory_path / "prompts"
        )
        
        self.example_selector = DynamicExampleSelector(
            mcp_client=mcp_client,
            embedding_model=embedding_model,
            memory_path=memory_path
        )
        
        self.cot_library = DomainCoTLibrary(memory_path=memory_path)
        
        self.cove = ChainOfVerification(
            mcp_client=mcp_client,
            llm_generate_fn=llm_generate_fn
        )
        
        self.monitor = PromptMonitor(window_minutes=60)
        
        self.technique_selector = PromptTechniqueSelector()
    
    def execute_task(
        self,
        task_description: str,
        use_advanced_reasoning: bool = True,
        verify_output: bool = True
    ) -> Dict:
        """
        Execute task with full prompt engineering pipeline.
        
        Args:
            task_description: Task to complete
            use_advanced_reasoning: Enable advanced techniques
            verify_output: Verify with CoVe
        
        Returns:
            Complete execution result
        """
        
        start_time = datetime.now()
        
        # 1. Select appropriate prompting techniques
        techniques = self.technique_selector.select_techniques(
            task_description
        )
        
        # 2. Build memory-aware system prompt
        system_prompt = create_memory_aware_system_prompt(
            memory_path=self.memory_path,
            current_task=task_description
        )
        
        # 3. Get relevant examples from memory
        examples = self.example_selector.select_examples(
            query=task_description,
            num_examples=3
        )
        
        # 4. Build complete prompt
        if 'cot' in techniques:
            # Use Chain-of-Thought
            prompt = "Solve this step-by-step:\n\n"
            
            # Add examples if available
            if examples:
                prompt += "Examples:\n"
                for ex in examples:
                    prompt += f"Input: {ex['input']}\n"
                    prompt += f"Output: {ex['output']}\n\n"
            
            prompt += f"Task: {task_description}\n\n"
            prompt += "Let's think step by step:\n"
        else:
            # Direct prompt
            prompt = f"{task_description}\n"
        
        # 5. Generate response
        full_prompt = f"{system_prompt}\n\n{prompt}"
        response = self.llm_generate(full_prompt)
        
        # 6. Verify with Chain of Verification if requested
        if verify_output:
            cove_result = self.cove.verify_response(
                original_response=response,
                query=task_description
            )
            
            final_response = cove_result['revised_response']
            confidence = cove_result['confidence']
        else:
            final_response = response
            confidence = 1.0
        
        # 7. Calculate execution time
        execution_time = (datetime.now() - start_time).total_seconds() * 1000
        
        # 8. Record metrics
        self.monitor.record_execution(
            prompt_id="spes_execution",
            prompt_version="1.0.0",
            execution_data={
                'latency_ms': execution_time,
                'quality_score': confidence,
                'techniques_used': techniques,
                'error': None
            }
        )
        
        return {
            'task': task_description,
            'techniques_used': techniques,
            'examples_retrieved': len(examples),
            'response': final_response,
            'confidence': confidence,
            'execution_time_ms': execution_time,
            'verified': verify_output
        }


# Example usage
spes_pe = SPESPromptEngineeringSystem(
    memory_path=Path(".claude"),
    mcp_client=mcp_client,
    llm_generate_fn=llm_generate
)

# Execute complex task
result = spes_pe.execute_task(
    task_description="Design a secure JWT authentication system with refresh tokens",
    use_advanced_reasoning=True,
    verify_output=True
)

print(f"Task: {result['task']}")
print(f"Techniques: {', '.join(result['techniques_used'])}")
print(f"Examples used: {result['examples_retrieved']}")
print(f"Confidence: {result['confidence']:.2%}")
print(f"Execution time: {result['execution_time_ms']:.0f}ms")
print(f"\nResponse:\n{result['response'][:500]}...")
```

---

## Conclusion

**Document 20 complete!** You now have the most comprehensive prompt engineering system, combining cutting-edge academic research with production-grade implementations.

### Key Achievements

✅ **System Prompt Architecture** - Memory-first prompts with MCP integration  
✅ **Few-Shot Learning Mastery** - Dynamic example selection with quality metrics  
✅ **Chain-of-Thought Mastery** - 5+ CoT variants with domain templates  
✅ **Advanced Reasoning Patterns** - CoVe, Least-to-Most, PoT, ToT, Step-Back  
✅ **Prompt Optimization** - Registry, A/B testing, automated optimization  
✅ **Production Deployment** - Confidence calibration, monitoring, alerts  
✅ **Meta-Orchestration** - Intelligent technique selection and integration  

### Production Features

| Component | Lines of Code | Status |
|-----------|---------------|--------|
| Memory-First System Prompts | ~200 | ✅ Complete |
| Context Window Manager | ~150 | ✅ Complete |
| Dynamic Example Selector | ~300 | ✅ Complete |
| Example Quality Evaluator | ~200 | ✅ Complete |
| Contrastive Few-Shot | ~100 | ✅ Complete |
| Domain CoT Library | ~250 | ✅ Complete |
| Chain of Verification | ~300 | ✅ Complete |
| Least-to-Most | ~200 | ✅ Complete |
| Program of Thoughts | ~150 | ✅ Complete |
| Thread of Thoughts | ~200 | ✅ Complete |
| Step-Back Prompting | ~150 | ✅ Complete |
| Prompt Registry | ~300 | ✅ Complete |
| A/B Testing Framework | ~250 | ✅ Complete |
| Prompt Optimizer | ~200 | ✅ Complete |
| Confidence Calibration | ~150 | ✅ Complete |
| Production Monitor | ~200 | ✅ Complete |
| Technique Selector | ~100 | ✅ Complete |
| Complete Integration | ~200 | ✅ Complete |
| **TOTAL** | **~3,500 lines** | **✅ Production-ready** |

### Advanced Techniques Covered

**20+ Cutting-Edge Patterns**:
1. ✅ Zero-Shot Chain-of-Thought
2. ✅ Few-Shot Chain-of-Thought
3. ✅ Faithful Chain-of-Thought
4. ✅ Contrastive Chain-of-Thought
5. ✅ Tabular Chain-of-Thought
6. ✅ Chain of Verification (CoVe)
7. ✅ Least-to-Most Prompting
8. ✅ Program of Thoughts
9. ✅ Thread of Thoughts
10. ✅ Step-Back Prompting
11. ✅ Self-Consistency (from Document 19)
12. ✅ Tree of Thoughts (from Document 19)
13. ✅ ReAct (from Document 19)
14. ✅ Reflection (from Document 19)
15. ✅ Constitutional AI (from Document 19)
16. ✅ Dynamic Few-Shot Selection
17. ✅ Memory-First Prompting
18. ✅ Domain-Specific Templates
19. ✅ Automated Optimization
20. ✅ Production Monitoring

---

**🎉 SPES Tier 4 Documentation Complete!**

You now have **20 comprehensive documents** (~220,000+ words) covering:

✅ **Foundational** (Docs 1-16): Architecture, memory, components, workflows  
✅ **Advanced** (Docs 17-20): Memory systems, semantic retrieval, meta-cognition, prompt engineering  

**Next Steps**: Implement these systems in your production SPES deployment!

---

*Document 20 complete - Advanced Prompt Engineering for SPES*
