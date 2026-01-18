---
tags: #quick-reference #cheat-sheets #decision-trees #reference-cards #practical-guide #implementation-recipes #troubleshooting
aliases: [Quick Reference, Cheat Sheets, Decision Trees, Reference Cards, Implementation Guide]
created: 2025-01-06
modified: 2025-01-06
status: evergreen
certainty: verified
type: reference
version: 1.0.0
source: claude-sonnet-4.5
category: reference-materials
priority: high
audience: [all-practitioners, developers, engineers]
prerequisites: [doc1-llm-reasoning-techniques-operational-manual]
---

# Quick Reference Library

> [!abstract] Purpose
> **[Quick-Reference-Library**:: Compact, high-density reference materials providing instant access to critical information, decision trees, troubleshooting guides, and implementation recipes - designed for rapid consultation during development and debugging.]**

---

## 📋 Reasoning Technique Selection

### Decision Tree

```
START: Choose Reasoning Technique

Does task require EXTERNAL information?
├─ YES → Does it require LEARNING from mistakes?
│         ├─ YES → REFLEXION
│         └─ NO → REACT
│
└─ NO → Does it require SYSTEMATIC EXPLORATION?
          ├─ YES → Need BACKTRACKING?
          │         ├─ YES → TREE OF THOUGHTS
          │         └─ NO → GRAPH OF THOUGHTS
          │
          └─ NO → Is MAXIMUM RELIABILITY critical?
                    ├─ YES → Content is FACTUAL?
                    │         ├─ YES → CHAIN OF VERIFICATION
                    │         └─ NO → SELF-CONSISTENCY
                    │
                    └─ NO → Requires PRECISION math?
                              ├─ YES → PROGRAM OF THOUGHTS
                              └─ NO → CHAIN OF THOUGHT
```

### Quick Selection Matrix

| Task Type | Technique | Cost | Quality | Use When |
|-----------|-----------|------|---------|----------|
| **Simple factual** | CoT | 1× | 7/10 | Clear reasoning path |
| **Math/calculation** | PoT | 1.2× | 9/10 | Precision required |
| **Needs reliability** | SC (k=5) | 5× | 8.5/10 | Cost acceptable |
| **Exploration needed** | ToT | 15× | 9/10 | Complex problem |
| **Factual claims** | CoVe | 4× | 8.5/10 | Reduce hallucination |
| **Tool required** | ReAct | 3-5× | 7.5/10 | External info needed |
| **Learning required** | Reflexion | 8× | 9/10 | Multi-trial improvement |

---

## 🔧 Implementation Cheat Sheets

### Chain of Thought

**One-Line**: Sequential reasoning with explicit steps

**Prompt Template**:
```
Question: {query}

Let's solve this step by step:
```

**When to Use**: Default for most reasoning tasks

**Cost**: ~500-1500 tokens

**Avoid If**: Need exploration, external info, or maximum reliability

---

### Self-Consistency

**One-Line**: Generate k samples, majority vote

**Code Template**:
```python
answers = []
for _ in range(k):  # k=5-10 typical
    ans = model.generate_cot(query, temperature=0.7)
    answers.append(extract_answer(ans))

final = Counter(answers).most_common(1)[0][0]
```

**When to Use**: Reliability > Cost, answerable questions

**Cost**: k × CoT cost (5-10× baseline)

**Avoid If**: Open-ended questions, tight budget

---

### Tree of Thoughts

**One-Line**: BFS/DFS through reasoning tree

**Code Template**:
```python
queue = [(initial_state, [])]
while queue and len(explored) < max_states:
    state, path = queue.pop(0)
    if is_solution(state):
        return path
    
    thoughts = generate_k_thoughts(state, k=3)
    for thought in thoughts:
        if evaluate(thought) != 'impossible':
            new_state = apply(state, thought)
            queue.append((new_state, path + [thought]))
```

**When to Use**: Complex problem, exploration needed, backtracking valuable

**Cost**: ~10-50× baseline (b^d nodes)

**Avoid If**: Simple problem, tight budget, time-critical

---

### Program of Thoughts

**One-Line**: Generate Python code, execute for precision

**Prompt Template**:
```
Problem: {query}

Write Python code to solve this:
```python
# Your code here
```

**When to Use**: Math, algorithms, multi-step calculations

**Cost**: ~1.2× baseline

**Avoid If**: Non-computational problem, no code execution

---

### ReAct

**One-Line**: Thought → Action → Observation loop

**Prompt Template**:
```
Question: {query}

Thought: [reasoning]
Action: [tool_name(args)]
Observation: [result]
... (repeat)
Thought: I now know the final answer
Final Answer: [answer]
```

**When to Use**: Need external tools/info, search required

**Cost**: ~3-5× baseline (k tool calls)

**Avoid If**: No tools needed, all info in prompt

---

## 🐛 Troubleshooting Guide

### Common Issues

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| **Hallucinated facts** | No verification | Use CoVe or SC |
| **Math errors** | Natural language arithmetic | Use PoT |
| **Stuck in loop** | Poor termination condition | Add max iterations, check logic |
| **Contradictory reasoning** | No validation | Add validation checkpoints |
| **Wrong tool** | Poor tool selection | Improve tool descriptions |
| **Timeout** | Too many iterations | Reduce max_iterations |
| **High cost** | Expensive technique | Use cheaper technique or cache |

### Debugging Checklist

- [ ] Validate inputs (format, completeness)
- [ ] Check reasoning mode appropriate for task
- [ ] Verify tool availability and permissions
- [ ] Confirm token budget sufficient
- [ ] Review thinking blocks for errors
- [ ] Test with simpler technique first
- [ ] Check for infinite loops
- [ ] Validate output format

---

## 📊 Performance Benchmarks (Quick Ref)

### Accuracy Improvements

| Technique | GSM8K Math | HotpotQA | Improvement |
|-----------|------------|----------|-------------|
| **CoT** | 74.4% | 29.4% | Baseline |
| **SC (k=40)** | 91.3% | - | +17pp |
| **PoT** | 84.8% | - | +10pp |
| **ToT** | - | - | +62pp (Game24) |
| **ReAct** | - | 35.1% | +6pp |
| **Reflexion** | - | 52.0% | +23pp |

### Cost Multipliers

| Technique | Token Multiplier | Time Multiplier |
|-----------|------------------|-----------------|
| CoT | 1× | 1× |
| SC (k=5) | 5× | 1× (parallel) |
| SC (k=10) | 10× | 1× (parallel) |
| PoT | 1.2× | 1.1× |
| CoVe | 4× | 4× |
| ToT (b=3, d=4) | 15-30× | 10-20× |
| ReAct | 3-5× | 3-5× |

---

## 🎯 Common Patterns

### Pattern: Conditional Verification

```python
result = cot(query)
if confidence(result) < 0.8:
    result = cove(query)  # Expensive verification only if needed
return result
```

### Pattern: Progressive Enhancement

```python
# Start cheap, escalate if needed
result = cot(query)
if not satisfactory(result):
    result = self_consistency(query, k=5)
if not satisfactory(result):
    result = tot(query)
return result
```

### Pattern: Hybrid Exploration + Validation

```python
candidates = tot(query, return_top_k=3)  # Explore
validated = self_consistency_vote(candidates)  # Validate
return validated
```

---

## 🔑 Key Formulas

### Token Cost Estimation

```
Cost($) = (input_tokens × $0.003 + output_tokens × $0.015) / 1000

Example CoT:
- Input: 200 tokens ($0.0006)
- Output: 800 tokens ($0.012)
- Total: $0.0126

Example SC (k=5):
- 5× CoT = $0.063
```

### Sample Size for Accuracy

```
Self-Consistency accuracy ≈ base_accuracy + c√k
where c ≈ 0.05, k = samples

Example:
Base (CoT): 70%
SC (k=5): 70% + 0.05√5 = 81.2%
SC (k=10): 70% + 0.05√10 = 85.8%
```

---

## 🚀 Production Quickstart

### Minimal Working Example

```python
from anthropic import Anthropic

client = Anthropic(api_key="...")

# Basic CoT
response = client.messages.create(
    model="claude-sonnet-4",
    max_tokens=2000,
    messages=[{
        "role": "user",
        "content": "Question: ...\n\nLet's think step by step:"
    }]
)

# With Extended Thinking
response = client.messages.create(
    model="claude-sonnet-4",
    max_tokens=4000,
    thinking_mode="enabled",
    messages=[{"role": "user", "content": "..."}]
)

# Parse response
for block in response.content:
    if block.type == "thinking":
        print("Thinking:", block.text)
    elif block.type == "text":
        print("Response:", block.text)
```

---

**End of Quick Reference Library**

