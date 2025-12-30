---
tags: #quick-reference #cove #verification #quality-assurance #one-pager
type: quick-reference
technique: Chain of Verification
category: quality-assurance
---

# ✅ Chain of Verification (CoVe) - Quick Reference

## One-Line Summary
Generate answer → Plan verification questions → Answer verifications independently → Revise with verification results.

---

## When to Use
✅ **Perfect For**: Factual writing, biographies, lists, reducing hallucination, high-accuracy needs
❌ **Skip For**: Creative content, opinion pieces, already verified (RAG), speed-critical

---

## Four-Step Process

```
① BASELINE: Generate initial response
    ↓
② PLAN: Create verification questions for claims
    ↓
③ EXECUTE: Answer verifications INDEPENDENTLY
    ↓
④ FINAL: Generate revised response with corrections
```

**Key Innovation**: Step ③ is independent - LLM doesn't see initial response, preventing confirmation bias

---

## Implementation Template

```python
def chain_of_verification(query):
    """
    CoVe implementation
    """
    # Step 1: Generate baseline response
    baseline = llm.complete(f"Answer: {query}")
    
    # Step 2: Plan verifications
    plan_prompt = f"""Response: {baseline}

Generate verification questions for factual claims:
1."""
    questions = llm.complete(plan_prompt)
    
    # Step 3: Execute verifications INDEPENDENTLY
    verified = []
    for q in parse_questions(questions):
        # CRITICAL: No baseline shown
        answer = llm.complete(f"Answer: {q}", temp=0.0)
        verified.append({'question': q, 'answer': answer})
    
    # Step 4: Generate final with corrections
    final_prompt = f"""Initial: {baseline}

Verifications: {format_verifications(verified)}

Provide corrected final answer:"""
    
    final = llm.complete(final_prompt)
    
    return {
        'baseline': baseline,
        'final': final,
        'verifications': verified
    }
```

---

## Prompt Templates

### Step 1: Baseline
```
Answer this question:

{query}

Answer:
```

### Step 2: Plan Verifications
```
Response: {baseline_response}

This response makes factual claims.
Generate verification questions:

1. [Question for claim 1]
2. [Question for claim 2]
3. [Question for claim 3]
```

### Step 3: Execute (INDEPENDENT!)
```
Answer this factual question:

{verification_question}

Answer:
```

**Critical**: NO baseline response shown!

### Step 4: Final Revision
```
Original: {baseline}

Verification results:
Q: {q1}
A: {a1}

Q: {q2}  
A: {a2}

Based on verifications, provide corrected answer:
```

---

## Performance Benchmarks
- **Long-form QA**: 16% hallucination (vs 38% baseline) - **-58% reduction**
- **Biographies**: 23% hallucination (vs 45% baseline) - **-49% reduction**
- **Lists**: 26% hallucination (vs 52% baseline) - **-50% reduction**

**Pattern**: Consistently halves hallucination rate

---

## Costs
- **Token Cost**: ~4x baseline (4 sequential LLM calls)
- **Latency**: ~4x baseline (cannot parallelize fully)
- **Best Practice**: Use for high-value content where accuracy critical

---

## Why Independent Verification Works

❌ **Joint Verification** (showing baseline):
```
Initial: "Hillary Clinton born in NYC"
Verify: Was Hillary Clinton born in NYC?
→ LLM rationalizes: "Yes, as stated above..."
```

✅ **Independent Verification** (no baseline shown):
```
Verify: Was Hillary Clinton born in NYC?
→ LLM retrieves fresh: "No, Chicago, Illinois"
```

**Benefit**: Prevents confirmation bias where LLM defends initial errors

---

## Verification Question Design

**Good Verification Questions**:
- ✅ "Was Marie Curie born in 1867?" (specific, binary)
- ✅ "What year did Marie Curie discover radium?" (specific fact)
- ✅ "Was Marie Curie the first person to win two Nobel Prizes?" (checkable claim)

**Poor Verification Questions**:
- ❌ "Is the response accurate?" (too vague)
- ❌ "Tell me about Marie Curie" (not verification, just repeats task)
- ❌ "Are all facts correct?" (doesn't specify which facts)

**Pattern**: One verification per factual claim, specific and checkable

---

## Common Pitfalls
❌ Showing baseline during verification → confirmation bias persists
❌ Vague verification questions → unhelpful answers
❌ Too few verifications → miss errors
❌ Verifying opinions/interpretations → not factually checkable

✅ **Fix**: Independent context, specific questions, verify facts not opinions

---

## Advanced: Factored Verification

Break complex claims into sub-claims:

```python
def factored_verification(claim):
    """
    Verify complex claim by parts
    """
    # Claim: "Marie Curie won Nobel Prize in Physics in 1903"
    
    sub_verifications = [
        "Did Marie Curie win a Nobel Prize?",  # Base fact
        "Was it in Physics?",  # Field
        "Was it in 1903?",  # Year
    ]
    
    for q in sub_verifications:
        answer = verify_independently(q)
        if "no" in answer.lower():
            return {'verified': False, 'failed_at': q}
    
    return {'verified': True}
```

**Benefit**: Pinpoints exactly what's wrong in complex claims

---

## Combinations

| Combine With | Benefit | Use Case |
|--------------|---------|----------|
| **RAG** | Verify against retrieved docs | Document-based QA |
| **Self-Refine** | Verify + improve quality | Content creation |
| **ToT** | Verify ToT solution paths | Complex reasoning |

**Best**: RAG + CoVe = retrieve knowledge, then verify against it

---

## Example: Biography

**Query**: "Write brief bio of Marie Curie"

**① Baseline**:
```
Marie Curie (1867-1934) discovered radium in 1898.
She won Nobel Prize in 1903, first woman to win.
Won second Nobel in 1911, first person to win two.
```

**② Verification Questions**:
```
1. Was Marie Curie born in 1867?
2. Did she discover radium in 1898?
3. Did she win Nobel Prize in 1903?
4. Was she first woman to win Nobel?
5. Did she win second Nobel in 1911?
6. Was she first to win two Nobel Prizes?
```

**③ Independent Verification** (no baseline shown):
```
1. Yes, 1867 ✓
2. Yes, December 1898 (also polonium July 1898) ⚠️
3. Yes, Physics 1903 ✓
4. Yes, first woman ✓
5. Yes, Chemistry 1911 ✓
6. Yes, first person ✓
```

**④ Final (Corrected)**:
```
Marie Curie (1867-1934) discovered polonium (July 1898)
and radium (December 1898). She won Nobel Prize in 
Physics in 1903, first woman to win. Won second Nobel 
in Chemistry in 1911, first person to win two Nobel Prizes.
```

**Change**: Added polonium, specified discovery months

---

## Verification Success Rate

Monitor how often verifications find errors:

```python
def track_verification_impact(baseline, verified):
    """
    Measure verification effectiveness
    """
    changes = count_edits(baseline, verified)
    
    if changes > 0:
        return {
            'corrections_made': changes,
            'effectiveness': 'high'  # Found and fixed errors
        }
    else:
        return {
            'corrections_made': 0,
            'effectiveness': 'low_or_accurate'  # Either baseline was good or verifications missed errors
        }
```

**Target**: 20-40% of responses should be corrected (indicates working)

---

## Production Checklist
- [ ] Baseline generation at temp 0.5-0.7 (moderate creativity)
- [ ] Verification questions specific and factual
- [ ] Independent verification (NO baseline context)
- [ ] Verification at temp 0.0 (deterministic)
- [ ] Final revision incorporates all verifications
- [ ] Monitor correction rate (should be 20-40%)

---

## Fast Variant: Critical Facts Only

For cost reduction, verify only critical facts:

```python
def verify_critical_only(response):
    """
    Verify only high-risk claims
    """
    # Identify factual claims
    claims = extract_factual_claims(response)
    
    # Score criticality
    critical = [
        c for c in claims
        if is_critical(c)  # Numbers, dates, names, causal claims
    ]
    
    # Verify only critical (~30% of all claims)
    verifications = [verify(c) for c in critical]
    
    return revise_critical_only(response, verifications)
```

**Benefit**: ~40% cost reduction with ~80% effectiveness retention

---

## Research
**Dhuliawala et al. 2023** - "Chain-of-Verification Reduces Hallucination in Large Language Models"
📄 https://arxiv.org/abs/2309.11495

---

**Related Techniques**: [[Self-Refine]], [[RAG]], [[Recitation-Augmented]]
**Full Guide**: [[04-quality-assurance-guide#Chain of Verification]]
