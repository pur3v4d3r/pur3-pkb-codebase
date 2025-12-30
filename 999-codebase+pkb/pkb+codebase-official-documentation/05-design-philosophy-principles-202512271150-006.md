---
title: SPES/PKB Design Philosophy & Principles
document_type: philosophy
tier: 1
priority: critical
version: 2.0.0
status: published
prerequisites: []
estimated_reading_time: 45-60 minutes
last_updated: 2025-12-25
---

# SPES/PKB Design Philosophy & Principles

**Version**: 2.0.0  
**Document Type**: Foundational Philosophy  
**Audience**: System architects, contributors, advanced users  
**Purpose**: Define core values, design rationale, and decision-making framework

---

## Table of Contents

1. [Core Philosophy](#core-philosophy)
2. [Foundational Principles](#foundational-principles)
3. [Design Values](#design-values)
4. [Architectural Decisions](#architectural-decisions)
5. [Trade-offs & Constraints](#trade-offs--constraints)
6. [Anti-Patterns](#anti-patterns)
7. [Decision Framework](#decision-framework)
8. [Evolution Philosophy](#evolution-philosophy)

---

## 1. Core Philosophy

### 1.1 Vision Statement

**The SPES/PKB system exists to transform prompt engineering from ad-hoc art into systematic engineering through composable, versioned, reusable components integrated with a self-improving knowledge base.**

### 1.2 Guiding Metaphor

**"LEGO for Prompts + Living Library"**

Just as LEGO bricks are:
- **Atomic**: Single-purpose, well-defined
- **Composable**: Combine in infinite ways
- **Standardized**: Compatible interfaces
- **Reusable**: Never destroyed, always available
- **Versioned**: Different generations coexist

...SPES components are engineered building blocks for prompt construction.

Just as a library:
- **Grows organically** through continuous accretion
- **Self-organizes** through cataloging and indexing
- **Enables discovery** through cross-referencing
- **Preserves knowledge** across time
- **Serves queries** through semantic retrieval

...the PKB evolves into a second brain.

### 1.3 First Principles

**1. Composition Over Monoliths**

Complex prompts are compositions of simple components, not monolithic templates.

❌ **Anti-Pattern**: Massive prompt templates with conditionals
```
if task == "code":
    prompt = "You are expert coder... [5000 words]"
elif task == "writing":
    prompt = "You are expert writer... [5000 words]"
```

✅ **Principle**: Compose from atomic parts
```
prompt = (
    Instruction(task_specific) +
    Persona(domain_expert) +
    Format(output_structure) +
    Constraints(boundaries)
)
```

**2. Versioning Enables Evolution**

Components evolve independently. Old versions remain available for stability. New versions enable improvement.

❌ **Anti-Pattern**: Overwrite existing components
```
# This breaks all workflows using this component
edit "instruction-v1.md" -> save changes
```

✅ **Principle**: Create new versions
```
# Old workflows unaffected, new workflows benefit
create "instruction-v2.0.0.md" -> new features
```

**3. Separation of Concerns**

Each component has one responsibility. Combinations create complexity.

❌ **Anti-Pattern**: Components that do multiple things
```yaml
component: instruction-and-format-and-persona
# Tightly coupled, can't reuse parts
```

✅ **Principle**: Single responsibility
```yaml
instruction: what-to-do
persona: who-is-doing-it
format: how-to-output
# Each independently reusable
```

**4. Knowledge as Network, Not Hierarchy**

Knowledge is interconnected, not tree-structured. Enable traversal through relationships.

❌ **Anti-Pattern**: Rigid folder hierarchies
```
/topics/
  /science/
    /physics/
      /quantum/
        note.md  # Trapped in hierarchy
```

✅ **Principle**: Flat structure + semantic links
```
/notes/
  quantum-mechanics.md  # Links to: [[Wave-Particle Duality]], [[Heisenberg]]
  consciousness.md      # Links to: [[Quantum Mind Hypothesis]]
# Quantum connects to both physics AND consciousness
```

**5. Privacy & Agency First**

Users own their data. Local-first architecture. Cloud is optional enhancement, not requirement.

✅ **Guaranteed**:
- All data stored locally
- Works offline
- No telemetry
- User controls all components

⚙️ **Optional**:
- Cloud LLM APIs (user choice)
- Sync services (user choice)
- Third-party integrations (user choice)

---

## 2. Foundational Principles

### 2.1 Atomic Components

**Principle**: Every component should be as small as possible but no smaller.

**Rationale**:
- Small components are easier to understand
- Single-purpose components are easier to test
- Atomic components maximize reuse potential
- Composition creates complexity only when needed

**Application**:

```yaml
✅ Good Atomicity:
  - instruction-generate-code-v1.0.0
    Purpose: Code generation directive
    Size: 200 words
    Reusable: Yes, across all code tasks
  
  - persona-python-expert-v1.0.0
    Purpose: Python expertise role
    Size: 150 words
    Reusable: Yes, for any Python task

❌ Poor Atomicity:
  - instruction-generate-python-code-with-tests-and-docs-v1.0.0
    Purpose: Too specific, bundles multiple concerns
    Size: 1000 words
    Reusable: No, very narrow use case
```

**Guidelines**:
- Can this component be split? → If yes, split it
- Does this component have multiple purposes? → If yes, separate them
- Can I reuse parts of this component? → If no, it's too coupled

### 2.2 Explicit Over Implicit

**Principle**: Make behavior explicit through composition, not implicit through hidden logic.

**Rationale**:
- Explicit composition is easier to understand
- No hidden side effects
- Clear dependencies
- Predictable outcomes

**Application**:

```python
❌ Implicit Magic:
class Workflow:
    def execute(self):
        # Implicitly adds error handling
        # Implicitly retries
        # Implicitly logs
        # User doesn't know what's happening

✅ Explicit Composition:
class Workflow:
    def execute(self):
        return (
            self.with_error_handling()
                .with_retry(max_attempts=3)
                .with_logging(level=INFO)
                .run()
        )
        # User sees exactly what's applied
```

### 2.3 Fail Fast, Fail Loud

**Principle**: Detect errors early and report them clearly.

**Rationale**:
- Silent failures cause confusion
- Early detection prevents cascading errors
- Clear errors enable quick fixes
- Users appreciate transparency

**Application**:

```python
❌ Silent Failure:
def load_component(id):
    try:
        return components.get(id)
    except:
        return None  # User doesn't know why it failed

✅ Fail Fast:
def load_component(id):
    if id not in components:
        raise ComponentNotFoundError(
            f"Component '{id}' not found. "
            f"Available: {list(components.keys())[:5]}..."
        )
    return components[id]
```

### 2.4 Progressive Disclosure

**Principle**: Simple tasks should be simple. Complex tasks should be possible.

**Rationale**:
- Beginners aren't overwhelmed
- Experts have power when needed
- System scales with user expertise
- Default to simple, enable complex

**Application**:

```yaml
Level 1 - Minimal (Beginners):
  workflow:
    - instruction: generate-code
    input: "Create a function to sort a list"
  
  # Just the essentials, everything else uses defaults

Level 2 - Configured (Intermediate):
  workflow:
    - instruction: generate-code
    - persona: python-expert
    - format: clean-code
    input: "Create a function to sort a list"
  
  # Adding optional enhancements

Level 3 - Advanced (Experts):
  workflow:
    - instruction: generate-code
    - persona: python-expert
    - format: clean-code
    - constraints: type-hints-required
    llm: claude-code
    validation:
      - syntax-check
      - test-coverage > 80%
    retry: exponential-backoff
  
  # Full control over all parameters
```

### 2.5 Convention Over Configuration

**Principle**: Provide sensible defaults. Allow override when needed.

**Rationale**:
- Reduces cognitive load
- Faster to get started
- Consistency across system
- Experts can still customize

**Application**:

```yaml
# Default conventions (no config needed)
components/
  atomic/
    instructions/
      component-instruction-*.md  # Auto-detected
  
# Override when needed
config.yml:
  component_directories:
    - /custom/path/to/components
    - /shared/team/components
```

### 2.6 Test What You Build

**Principle**: Every component should be testable. Every workflow should have test cases.

**Rationale**:
- Tests document expected behavior
- Regressions caught early
- Confidence in changes
- Examples for users

**Application**:

```yaml
component-instruction-v2.0.0.md:
  content: [instruction text]
  
  tests:
    - input: "Generate hello world"
      expected_output_contains: "print('Hello, World!')"
      llm: claude-sonnet-4
      
    - input: "Generate factorial function"
      expected_output_contains: ["def factorial", "return"]
      llm: claude-sonnet-4
```

---

## 3. Design Values

### 3.1 Value Hierarchy

When design decisions conflict, this hierarchy guides resolution:

```
1. User Privacy & Agency
   └─ Users own and control their data
   
2. System Reliability
   └─ System should work predictably
   
3. Maintainability
   └─ Code should be easy to understand and modify
   
4. Flexibility
   └─ System should adapt to diverse needs
   
5. Performance
   └─ System should be reasonably fast
   
6. Feature Richness
   └─ Features serve the above values
```

**Example Conflict Resolution**:

**Scenario**: Should we add automatic cloud backup?

- **Privacy**: ❌ Sends data to cloud without explicit consent → VIOLATES #1
- **Decision**: No automatic cloud backup. Offer opt-in manual backup with clear disclosure.

**Scenario**: Should we cache LLM responses?

- **Reliability**: ✅ Reduces API failures
- **Performance**: ✅ Faster repeated requests
- **Privacy**: ✅ Local cache only
- **Decision**: Yes, implement local caching with TTL

### 3.2 Bias Toward Simplicity

**Guideline**: When in doubt, choose the simpler option.

**Rationale**:
- Simpler code has fewer bugs
- Simpler systems are easier to understand
- Simpler solutions are easier to maintain
- You can always add complexity later

**Examples**:

```yaml
❌ Complex First:
  # Premature optimization
  Implement distributed caching system with Redis cluster
  
✅ Simple First:
  # Start simple
  Implement in-memory cache with LRU eviction
  # Add Redis later if needed

❌ Over-Engineering:
  # Building for scale we don't have
  Multi-tenant architecture with sharding
  
✅ Right-Sizing:
  # Build for single user (actual need)
  Single-vault local system
  # Add multi-user later if demand exists
```

### 3.3 Optimize for Clarity

**Guideline**: Code is read 10x more than written. Optimize for readers.

**Rationale**:
- Clear code is maintainable
- Future-you will thank present-you
- Contributors can understand quickly
- Reduces bugs through understanding

**Examples**:

```python
❌ Clever but Cryptic:
def p(c,l): return [i for i,e in enumerate(c) if l(e)]

✅ Clear and Explicit:
def find_matching_component_indices(
    components: List[Component],
    filter_function: Callable[[Component], bool]
) -> List[int]:
    """Find indices of components matching filter.
    
    Args:
        components: List of components to search
        filter_function: Predicate to test each component
    
    Returns:
        Indices of matching components
    """
    matching_indices = []
    for index, component in enumerate(components):
        if filter_function(component):
            matching_indices.append(index)
    return matching_indices
```

### 3.4 Design for Change

**Guideline**: Assume requirements will change. Build flexibility points.

**Rationale**:
- Requirements always change
- Rigid designs break under change
- Flexible designs adapt gracefully
- Extensibility is cheaper than rewrite

**Patterns**:

```python
# ✅ Flexibility Points:

# 1. Strategy pattern for algorithms
class ContextHandoff(ABC):
    @abstractmethod
    def handoff(self, context): pass

# Easy to add new strategies without changing workflow code

# 2. Plugin architecture for LLM adapters
class LLMAdapter(ABC):
    @abstractmethod
    def generate(self, prompt): pass

# Easy to add new LLM without changing engine

# 3. Configuration-driven behavior
config.yml:
  default_llm: claude
  fallback_llm: gemini
  max_retries: 3

# Change behavior without code changes
```

---

## 4. Architectural Decisions

### 4.1 Why Obsidian (Not Other PKB Tools)

**Alternatives Considered**: Notion, Roam Research, Logseq, Custom solution

**Decision**: Obsidian

**Rationale**:
1. **Local-First**: Files are local markdown, not cloud database
2. **Plaintext**: Future-proof, never locked in
3. **Plugin Ecosystem**: Extensible (Dataview, Templater, Smart Connections)
4. **Graph View**: Native knowledge graph visualization
5. **Community**: Large active community, sustainable
6. **Performance**: Fast with large vaults (10,000+ notes)

**Trade-offs Accepted**:
- ❌ No native collaboration (vs Notion)
- ❌ No native databases (vs Notion)
- ❌ Requires local install (vs web-based tools)
- ✅ But: Privacy, ownership, longevity

### 4.2 Why Multi-LLM (Not Single Provider)

**Alternatives Considered**: Claude-only, Build for GPT, Generic interface

**Decision**: Multi-LLM adapter architecture

**Rationale**:
1. **Avoid Lock-In**: Don't depend on single vendor
2. **Use Case Optimization**: Different LLMs excel at different tasks
3. **Cost Optimization**: Mix expensive (quality) and cheap (volume)
4. **Privacy Options**: Local LLMs for sensitive data
5. **Reliability**: Fallback when primary unavailable

**Trade-offs Accepted**:
- ❌ More complexity (adapter layer)
- ❌ Testing burden (test across LLMs)
- ✅ But: Flexibility worth the cost

### 4.3 Why Component Versioning (Not Mutable Components)

**Alternatives Considered**: Mutable components, Git versioning, No versioning

**Decision**: Semantic versioning with immutable published components

**Rationale**:
1. **Reproducibility**: Old workflows work forever
2. **Confidence**: Changes won't break existing workflows
3. **Evolution**: Can improve without fear
4. **Auditability**: Clear history of changes

**Trade-offs Accepted**:
- ❌ Disk space (multiple versions)
- ❌ More files to manage
- ✅ But: Stability worth the cost

### 4.4 Why Local-First (Not Cloud-First)

**Alternatives Considered**: Cloud-hosted SaaS, Hybrid, Desktop app with cloud sync

**Decision**: Local-first with optional cloud

**Rationale**:
1. **Privacy**: Sensitive data never leaves machine (if user chooses)
2. **Ownership**: User owns their data completely
3. **Reliability**: Works offline
4. **Speed**: No network latency
5. **Control**: No vendor decisions affecting user

**Trade-offs Accepted**:
- ❌ No native collaboration
- ❌ No cross-device sync (without user setup)
- ❌ Installation required
- ✅ But: Privacy and ownership non-negotiable

### 4.5 Why Python (Not JavaScript/TypeScript)

**Alternatives Considered**: JavaScript (Obsidian-native), TypeScript, Go, Rust

**Decision**: Python for engine, JavaScript for plugins

**Rationale**:
1. **LLM SDK Ecosystem**: Best support (Anthropic, OpenAI, Google)
2. **Data Science Libraries**: NumPy, scikit-learn for embeddings
3. **Developer Pool**: Large Python community
4. **Rapid Development**: Quick iteration
5. **Obsidian Integration**: JavaScript plugins call Python engine

**Trade-offs Accepted**:
- ❌ Slower than compiled languages
- ❌ Runtime dependency
- ✅ But: Development speed and ecosystem worth it

---

## 5. Trade-offs & Constraints

### 5.1 Accepted Limitations

**Single-User Focus**

**Limitation**: No multi-user collaboration built-in

**Rationale**: 
- Adds significant complexity
- Cloud infrastructure required
- Conflicts with local-first
- Can be added later if demand exists

**Workaround**: Teams can share component libraries via Git

---

**English-Only (Initially)**

**Limitation**: Documentation and components in English

**Rationale**:
- Finite resources
- English dominant in prompt engineering
- LLMs strongest in English
- Internationalization possible later

**Workaround**: Community can contribute translations

---

**Limited Visual Interface**

**Limitation**: CLI/Obsidian interface, no dedicated GUI

**Rationale**:
- GUI development is expensive
- Obsidian provides sufficient interface
- Power users prefer CLI/text
- Can build GUI later if needed

**Workaround**: Obsidian is the GUI

---

### 5.2 Deliberate Constraints

**No Code Execution in Components**

**Constraint**: Components are declarative text, not executable code

**Rationale**:
- Security: No arbitrary code execution
- Simplicity: Just text, easy to inspect
- Portability: Works across systems
- Safety: Can't break system

**When This Hurts**: Dynamic logic in prompts
**Solution**: Use templating (Templater) in Obsidian layer

---

**No External Dependencies in Components**

**Constraint**: Components are self-contained markdown

**Rationale**:
- Portability: Components work everywhere
- No broken links to external resources
- Version control friendly
- Easy to share

**When This Hurts**: Want to reference external APIs
**Solution**: Reference in documentation, call in workflow

---

**Semantic Versioning Strictness**

**Constraint**: Breaking changes MUST bump major version

**Rationale**:
- Reliability: Users trust versions
- Predictability: Know what to expect
- Migration: Clear upgrade path

**When This Hurts**: Want to fix bad design in minor version
**Solution**: Create v2.0.0, provide migration guide

---

## 6. Anti-Patterns

### 6.1 God Component

**Anti-Pattern**: Massive component that does everything

```yaml
❌ component-do-everything-v1.0.0.md
  - Instructions for 10 different tasks
  - 5 different personas
  - Multiple output formats
  - 3000 words long
```

**Why Bad**:
- Not reusable
- Hard to test
- Difficult to understand
- Can't compose

**Solution**: Split into atomic components
```yaml
✅ component-instruction-task1-v1.0.0.md (300 words)
✅ component-instruction-task2-v1.0.0.md (300 words)
✅ component-persona-expert-v1.0.0.md (200 words)
```

### 6.2 Premature Optimization

**Anti-Pattern**: Optimizing before measuring

```python
❌ "We might have performance issues, let's add caching, 
    multi-threading, distributed processing..."
```

**Why Bad**:
- Adds complexity early
- May optimize wrong thing
- Maintenance burden
- Unknown if needed

**Solution**: Measure first, optimize second
```python
✅ 1. Build simple version
   2. Measure actual performance
   3. Identify bottleneck
   4. Optimize that specific bottleneck
   5. Measure again
```

### 6.3 Configuration Hell

**Anti-Pattern**: Everything is configurable

```yaml
❌ config.yml (500 lines of options)
  enable_feature_x: true
  feature_x_mode: advanced
  feature_x_timeout: 30
  feature_x_retries: 3
  feature_x_cache: true
  feature_x_cache_ttl: 3600
  ... (hundreds more)
```

**Why Bad**:
- Overwhelming for users
- Untested combinations
- Maintenance nightmare
- Unclear defaults

**Solution**: Convention over configuration
```yaml
✅ config.yml (20 lines of essentials)
  vault_path: /path/to/vault
  default_llm: claude
  
  # Everything else uses smart defaults
```

### 6.4 Tight Coupling

**Anti-Pattern**: Components depend on specific other components

```yaml
❌ component-instruction-with-hardcoded-persona-v1.0.0.md
  "As a Python expert (persona hardcoded), do this task..."
  
  # Can't reuse with different persona
```

**Why Bad**:
- Not composable
- Breaks separation of concerns
- Limits reuse

**Solution**: Decouple through composition
```yaml
✅ component-instruction-v1.0.0.md
  "Do this task..." (persona-agnostic)
  
  # Compose with any persona at runtime
```

### 6.5 Magic Strings

**Anti-Pattern**: Important values hardcoded as strings

```python
❌ if llm_type == "claude":  # What if typo? "cluade"
     ...
```

**Why Bad**:
- Typos cause bugs
- No autocomplete
- Hard to refactor

**Solution**: Use enums/constants
```python
✅ class LLMType(Enum):
     CLAUDE = "claude"
     GEMINI = "gemini"
   
   if llm_type == LLMType.CLAUDE:
     ...
```

---

## 7. Decision Framework

### 7.1 Adding New Features

**Question Sequence**:

```
1. Is this aligned with core philosophy?
   └─ No → Reject
   └─ Yes → Continue

2. Does this violate any foundational principles?
   └─ Yes → Reject
   └─ No → Continue

3. Can this be achieved through composition of existing features?
   └─ Yes → Don't add, document composition pattern
   └─ No → Continue

4. What is the simplest implementation?
   └─ Build that first

5. Can this be added as opt-in?
   └─ Yes → Make it opt-in
   └─ No → Ensure strong justification

6. Does this add acceptable complexity?
   └─ No → Reject
   └─ Yes → Prototype

7. Can this be tested?
   └─ No → Reject
   └─ Yes → Implement with tests
```

**Example: "Add automatic cloud sync"**

```
1. Aligned? → Privacy-first conflicts with automatic cloud
   └─ ❌ Reject or make explicit opt-in

Example: "Add new LLM adapter"

1. Aligned? → Yes, multi-LLM is core
2. Violates principles? → No
3. Composition? → No, new integration needed
4. Simplest? → Implement adapter interface
5. Opt-in? → Yes, user chooses LLM
6. Complexity? → Acceptable, follows pattern
7. Testable? → Yes
   └─ ✅ Accept, implement
```

### 7.2 Breaking Changes

**Decision Tree**:

```
Breaking change needed?
├─ Can we avoid it with backward compatibility?
│  └─ Yes → Implement backward compat
│  └─ No → Continue
│
├─ Is the current design fundamentally flawed?
│  └─ No → Find non-breaking solution
│  └─ Yes → Continue
│
├─ Do benefits outweigh migration cost?
│  └─ No → Defer or reject
│  └─ Yes → Continue
│
├─ Can we provide automated migration?
│  └─ No → Require manual migration with excellent docs
│  └─ Yes → Build migration tool
│
└─ Release as new major version with migration guide
```

### 7.3 Technical Debt

**Accept debt when**:
- ✅ Rapid prototyping for validation
- ✅ Time-sensitive feature delivery
- ✅ Learning new domain
- ✅ Temporary workaround with plan to fix

**Reject debt when**:
- ❌ Just being lazy
- ❌ Avoiding difficult refactor
- ❌ "We'll fix it later" without plan
- ❌ Impacts user-facing reliability

**Debt Management**:
```yaml
1. Document debt explicitly
   # TODO(TECH_DEBT): This is a hack because...
   # Plan: Refactor to proper solution in v2.1.0
   # Ticket: SPES-123

2. Track in backlog
   Priority: P2-P3 (not critical, but tracked)

3. Allocate time
   20% of sprint for debt paydown

4. No interest accumulation
   Don't build on top of debt
```

---

## 8. Evolution Philosophy

### 8.1 Versioning Strategy

**Component Versions**: Semantic versioning (MAJOR.MINOR.PATCH)

```yaml
v1.0.0 → v1.1.0: New optional feature
  Backward compatible: ✅
  Old workflows work: ✅
  Migration needed: ❌

v1.1.0 → v2.0.0: Breaking change
  Backward compatible: ❌
  Old workflows work: ✅ (using v1.1.0)
  Migration needed: ✅ (for v2.0.0 benefits)
```

**System Versions**: Track major architecture changes

```yaml
v1.x: Single LLM (Claude only)
v2.x: Multi-LLM architecture
v3.x: (Future) Cloud deployment option
```

### 8.2 Deprecation Policy

**Process**:

```yaml
Step 1 - Mark deprecated (v1.5.0):
  ---
  status: deprecated
  deprecated_in: v1.5.0
  superseded_by: component-v2.0.0
  removal_planned: v3.0.0 (1 year)
  ---

Step 2 - Warn users:
  # System detects deprecated component usage
  WARNING: component-v1.0.0 is deprecated.
  Use component-v2.0.0 instead.
  See: migration-guide.md

Step 3 - Grace period:
  # 1 year minimum
  # Components still work during grace period

Step 4 - Remove (v3.0.0):
  # Archive to /deprecated/
  # No longer loadable
  # Migration guide remains
```

### 8.3 Community Contributions

**Philosophy**: Open but curated

**Process**:
```yaml
1. Proposal:
   - Submit GitHub issue describing component
   - Discuss with maintainers
   - Get alignment on value

2. Implementation:
   - Fork repository
   - Implement component
   - Follow style guide
   - Add tests
   - Write documentation

3. Review:
   - Maintainer review
   - Suggest improvements
   - Iterate

4. Integration:
   - Merge to /community/ directory
   - Tag with #community-contrib
   - Credit contributor
   - Include in component index

5. Promotion (Optional):
   - Widely used community components
   - Can be promoted to /core/
   - Requires maintainer vote
```

### 8.4 Long-Term Vision

**5-Year Horizon**:

```yaml
Year 1 (2025): Foundation
  - Stable multi-LLM architecture
  - Comprehensive component library
  - Local LLM optimization
  - Strong documentation

Year 2 (2026): Expansion
  - Workflow marketplace
  - Component testing framework
  - Cloud deployment option (optional)
  - Multi-user support (optional)

Year 3 (2027): Intelligence
  - Automated prompt optimization
  - Learned LLM routing
  - Adaptive context management
  - Self-improving workflows

Year 4 (2028): Community
  - Large component library (1000+)
  - Active contributor community
  - Certifications and training
  - Ecosystem of tools

Year 5 (2029): Standard
  - Industry reference architecture
  - Adopted by organizations
  - Academic recognition
  - Sustainable open-source model
```

**Principles for Future**:
- ✅ Maintain local-first option always
- ✅ Never sacrifice privacy for features
- ✅ Keep core simple, expansion through plugins
- ✅ Backward compatibility for published components
- ✅ Community-driven evolution

---

## Summary

**Core Philosophy**: LEGO for Prompts + Living Library

**Key Principles**:
1. Composition over monoliths
2. Versioning enables evolution
3. Separation of concerns
4. Knowledge as network
5. Privacy & agency first

**Design Values** (in order):
1. User Privacy & Agency
2. System Reliability
3. Maintainability
4. Flexibility
5. Performance
6. Feature Richness

**Decision Framework**:
- Simple > Complex
- Explicit > Implicit
- Clear > Clever
- Tested > Assumed
- User-focused > Developer-convenient

**Evolution**: Stable foundation + continuous improvement + community-driven

---

**This philosophy guides all system decisions. When in doubt, return to first principles.**
