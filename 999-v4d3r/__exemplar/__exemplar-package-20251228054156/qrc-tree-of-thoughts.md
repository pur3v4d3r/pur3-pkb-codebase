---
tags: #quick-reference #tree-of-thoughts #tot #one-pager
type: quick-reference
technique: Tree of Thoughts
category: reasoning
---

# 🌳 Tree of Thoughts (ToT) - Quick Reference

## One-Line Summary
Systematic exploration of reasoning paths using tree search (BFS/DFS) with explicit state evaluation and backtracking.

---

## When to Use
✅ **Perfect For**: Complex planning, problems with dead ends, Game of 24, creative writing with constraints
❌ **Skip For**: Simple factual queries, speed-critical tasks, straightforward reasoning

---

## Core Components

```
1. THOUGHT DECOMPOSITION
   Define what constitutes one "thought" (reasoning step)

2. THOUGHT GENERATOR  
   LLM generates k candidate next thoughts

3. STATE EVALUATOR
   Score each thought's promise (0-10 or IMPOSSIBLE/MAYBE/LIKELY/SOLVED)

4. SEARCH ALGORITHM
   BFS (optimal path) or DFS (lower cost)
```

---

## Implementation Template

```python
def tree_of_thoughts(problem, max_depth=4, branching=3):
    """
    BFS implementation
    """
    from collections import deque
    
    queue = deque([{'state': initial_state, 'depth': 0}])
    
    while queue:
        current = queue.popleft()
        
        # Check if solved
        if is_solved(current['state']):
            return current
        
        # Don't exceed depth
        if current['depth'] >= max_depth:
            continue
        
        # Generate next thoughts
        thoughts = generate_thoughts(current['state'], k=branching)
        
        # Evaluate and add promising ones
        for thought in thoughts:
            score = evaluate(thought)
            if score >= threshold:
                queue.append({
                    'state': thought,
                    'depth': current['depth'] + 1
                })
```

---

## Prompt Templates

### Thought Generation
```
Current state: {state}
Goal: {goal}

Generate {k} different next steps.

Next steps:
1.
2.
3.
```

### State Evaluation
```
Goal: {goal}
Current state: {state}

Rate this state:
- IMPOSSIBLE: No path to solution
- MAYBE: Uncertain
- LIKELY: Clear path visible
- SOLVED: Goal reached

Assessment:
```

---

## Performance Benchmarks
- **Game of 24**: 74% success (vs 7.3% baseline) - **10x improvement**
- **Creative Writing**: 45% preference (vs 20% standard)
- **Crosswords**: 62% success (vs 16% greedy)

---

## Costs
- **Token Cost**: 5-15x baseline (depends on branching factor & depth)
- **Latency**: High (sequential state generation)
- **Best Practices**: Use DFS for cost-sensitive, BFS for optimal solutions

---

## Common Pitfalls
❌ Too deep tree (depth > 5) → exponential explosion
❌ Poor state evaluation → explores dead ends
❌ Too low branching → misses solution
❌ No pruning → wastes tokens on hopeless paths

✅ **Fix**: Prune aggressively, limit depth, tune branching to problem

---

## Combinations

| Combine With | Benefit | Use Case |
|--------------|---------|----------|
| **Self-Consistency** | Validate solution | High-stakes planning |
| **PoT** | Code-based evaluation | Game of 24 |
| **RAG** | Knowledge-grounded reasoning | Research tasks |

---

## Example: Game of 24

**Input**: Numbers [4, 5, 6, 10], Goal: Reach 24

**Tree Exploration**:
```
Root: [4, 5, 6, 10]
  ├─ 6 × 4 = 24 ✓ SOLVED!
  ├─ 10 - 6 = 4 → [4, 4, 5]
  │   ├─ 4 + 4 = 8 → [8, 5]
  │   │   └─ 8 × 5 = 40 ✗ (wrong)
  │   └─ 4 × 5 = 20 → [20, 4]
  │       └─ 20 + 4 = 24 ✓ SOLVED!
  └─ 5 + 4 = 9 → [9, 6, 10]
      └─ ...
```

**Best Path**: 6 × 4 = 24 (depth 1, immediate solution)

---

## Research
**Yao et al. 2023** - "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
📄 https://arxiv.org/abs/2305.10601

---

**Related Techniques**: [[Graph of Thoughts]], [[Self-Consistency]], [[Program of Thoughts]]
**Full Guide**: [[01-reasoning-techniques-guide#Tree of Thoughts]]
