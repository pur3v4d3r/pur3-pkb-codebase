---
tags: #quick-reference #self-consistency #ensemble #one-pager
type: quick-reference
technique: Self-Consistency
category: reasoning
---

# 🎯 Self-Consistency - Quick Reference

## One-Line Summary
Generate multiple reasoning paths (temperature > 0), vote on final answers for robust majority consensus.

---

## When to Use
✅ **Perfect For**: Mathematical reasoning, commonsense QA, any task where answer has clear right/wrong
❌ **Skip For**: Creative writing (no "correct" answer), single-fact lookup, latency-critical tasks

---

## Algorithm

```
INPUT: Question
OUTPUT: Most consistent answer

1. Generate N diverse reasoning paths
   (same question, temperature 0.7-1.0, N = 3-10)

2. Extract final answer from each path

3. Vote: Return majority answer

4. Optional: Calculate confidence = majority_count / N
```

---

## Implementation Template

```python
def self_consistency(question, num_samples=5, temperature=0.7):
    """
    Self-Consistency implementation
    """
    from collections import Counter
    
    # Generate diverse reasoning paths
    answers = []
    for _ in range(num_samples):
        response = llm.complete(
            question,
            temperature=temperature
        )
        answer = extract_final_answer(response)
        answers.append(answer)
    
    # Vote on answers
    answer_counts = Counter(answers)
    final_answer = answer_counts.most_common(1)[0][0]
    confidence = answer_counts[final_answer] / num_samples
    
    return {
        'answer': final_answer,
        'confidence': confidence,
        'all_answers': answers
    }
```

---

## Prompt Template

```
Question: {question}

Let's solve this step by step:

[LLM generates reasoning]

Therefore, the answer is: [final answer]
```

**Key**: Ask N times with temperature > 0 for diverse paths

---

## Parameter Tuning

| Parameter | Low Value | High Value | Recommendation |
|-----------|-----------|------------|----------------|
| **N (samples)** | 3 | 10-20 | 5 for standard, 10 for critical |
| **Temperature** | 0.5 | 1.0 | 0.7-0.8 for good diversity |

**Trade-off**: More samples = higher confidence but linear cost increase

---

## Performance Benchmarks
- **GSM8K (Math)**: 74.4% (vs 46.9% CoT alone) - **+27.5pp**
- **StrategyQA**: 76.2% (vs 68.7% CoT alone) - **+7.5pp**
- **ARC (Science)**: 81.5% (vs 75.2% CoT alone) - **+6.3pp**

**Pattern**: Consistent +5-15pp improvement across reasoning tasks

---

## Costs
- **Token Cost**: N × baseline (5 samples = 5x cost)
- **Latency**: Can parallelize! (5 samples = 1x latency if parallel)
- **Best Practice**: Start with N=3, increase for critical tasks

---

## Answer Extraction

Critical step: Extract final answer reliably

```python
def extract_final_answer(response):
    """
    Extract answer from reasoning chain
    """
    # Pattern 1: "Therefore, ..."
    if "therefore" in response.lower():
        return extract_after_keyword(response, "therefore")
    
    # Pattern 2: "The answer is ..."
    if "answer is" in response.lower():
        return extract_after_keyword(response, "answer is")
    
    # Pattern 3: Last sentence
    return response.split('.')[-2].strip()
```

---

## Common Pitfalls
❌ Temperature too low (0.0-0.3) → identical answers (voting useless)
❌ Temperature too high (>1.2) → nonsense answers
❌ Poor answer extraction → different phrasings counted as different answers
❌ N too small (N=2) → ties, low confidence

✅ **Fix**: Use temp 0.7-0.8, normalize answers before voting, N ≥ 5

---

## Advanced: Adaptive Sample Count

```python
def adaptive_self_consistency(question, min_samples=3, max_samples=10):
    """
    Stop early if high confidence reached
    """
    from collections import Counter
    
    answers = []
    
    for i in range(max_samples):
        # Generate answer
        answer = generate_answer(question, temperature=0.7)
        answers.append(answer)
        
        # Check confidence after min_samples
        if i >= min_samples - 1:
            counts = Counter(answers)
            max_count = counts.most_common(1)[0][1]
            confidence = max_count / len(answers)
            
            # Stop if high confidence
            if confidence >= 0.7:  # 70%+ agree
                break
    
    final = Counter(answers).most_common(1)[0][0]
    return final
```

---

## Combinations

| Combine With | Benefit | Use Case |
|--------------|---------|----------|
| **Chain of Thought** | Base method | Always use together |
| **ToT** | Validate ToT solution | High-stakes decisions |
| **PoT** | Vote on program outputs | Critical calculations |

**Note**: Self-Consistency enhances any technique that can generate multiple attempts

---

## Confidence Interpretation

| Confidence | Interpretation | Action |
|------------|----------------|--------|
| **≥ 80%** | Very high agreement | Trust answer |
| **60-79%** | Moderate agreement | Acceptable |
| **40-59%** | Low agreement | Increase N or investigate |
| **< 40%** | No consensus | Problem unclear or very hard |

---

## Example: Math Problem

**Question**: "Roger has 5 tennis balls. He buys 2 cans, each with 3 balls. How many balls does he have?"

**5 Samples**:
```
Sample 1: "5 + 2×3 = 5 + 6 = 11 balls" → 11
Sample 2: "2 cans × 3 balls = 6. 5 + 6 = 11" → 11
Sample 3: "He has 5, buys 6 more, total 11" → 11
Sample 4: "Initial 5 + (2×3) = 11 balls" → 11
Sample 5: "2 + 3 = 5 cans? No, 2 cans... 11 total" → 11
```

**Vote**: 11 appears 5/5 times → **100% confidence** → Answer: 11

---

## Research
**Wang et al. 2022** - "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
📄 https://arxiv.org/abs/2203.11171

---

**Related Techniques**: [[Chain of Thought]], [[Tree of Thoughts]], [[Program of Thoughts]]
**Full Guide**: [[01-reasoning-techniques-guide#Self-Consistency]]
