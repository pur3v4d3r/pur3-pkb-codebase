# VADER Prompt Analysis & Testing

## Critical Weaknesses Identified

### 1. **CONTRADICTORY INSTRUCTIONS** (Severity: CRITICAL)

**Problem**: The prompt explicitly forbids lists, then provides a template full of lists.

**Evidence**:
- Line ~XXX: "You are strictly forbidden from using bullet points (e.g., "*", "-", "+") or numbered lists"
- Line ~XXX: Output template contains:
  ```
  **1. Define Core Parameters:**
    * **[TOPIC]:** {{Specify...}}
    * **[DEPTH_LEVEL]:** {{e.g., "Encyclopedic..."}}
  ```

**Impact**: Claude receives mixed signals - explicit prohibition vs. template modeling the forbidden behavior

**Fix Required**: Rewrite entire template in pure prose format

---

### 2. **INSUFFICIENT PROSE ENFORCEMENT** (Severity: HIGH)

**Problem**: No metacognitive checkpoints to verify prose compliance before output

**Missing Elements**:
- Pre-output validation specifically for list detection
- Examples of prose vs. list formatting
- Strategies for converting list-worthy content to prose
- Self-checking mechanism

**Fix Required**: Add format validation protocol with explicit checking steps

---

### 3. **WEAK DEPTH OPERATIONALIZATION** (Severity: HIGH)

**Problem**: "Go above and beyond" is vague without concrete metrics

**Missing Elements**:
- Minimum word counts per section
- Depth scoring rubric
- Expansion triggers (when more detail needed)
- Quality thresholds per phase

**Fix Required**: Add quantitative depth requirements and assessment framework

---

### 4. **REASONING TECHNIQUE INTEGRATION GAP** (Severity: MEDIUM)

**Problem**: System architecture section exists but doesn't map to report generation

**Missing Elements**:
- When to use ToT vs CoT vs SC for report sections
- Thinking scaffolds for each report phase
- Validation checkpoints using reasoning techniques

**Fix Required**: Integrate reasoning selection into report generation workflow

---

### 5. **TEMPLATE FORMAT VIOLATION** (Severity: CRITICAL)

**Problem**: The scaffold itself violates the rules it's meant to enforce

**Evidence**:
```
**3. Phase 2: Encyclopedic Exposition**
    * **Deconstruction:** Break the `[TOPIC]` down...
    * **Detailed Prose (Per Sub-Heading):** For *each*...
```

**Fix Required**: Complete template rewrite in prose-only format

---

## Test Case Design

### Test Query 1: List-Prone Topic
**Query**: "Explain the key principles of machine learning"

**Expected Behavior**:
- ❌ BAD: "The key principles are: 1. Supervised learning, 2. Unsupervised learning..."
- ✅ GOOD: "Machine learning operates on several foundational principles that work in concert..."

### Test Query 2: Process Explanation
**Query**: "How does photosynthesis work?"

**Expected Behavior**:
- ❌ BAD: "The process involves: • Light reaction • Calvin cycle • Glucose production"
- ✅ GOOD: "Photosynthesis unfolds through an intricate sequence of biochemical transformations..."

### Test Query 3: Comparison
**Query**: "Compare classical and operant conditioning"

**Expected Behavior**:
- ❌ BAD: "Classical: - Pavlov - Involuntary responses | Operant: - Skinner - Voluntary behavior"
- ✅ GOOD: "While classical conditioning and operant conditioning both represent fundamental learning mechanisms..."

---

## Proposed Improvements

### Improvement 1: PROSE ENFORCEMENT PROTOCOL

Add to thinking block:
```xml
<thinking>
## PRE-OUTPUT FORMAT VALIDATION

### List Detection Scan
[ ] Check entire response for bullet points (*, -, +)
[ ] Check for numbered sequences (1., 2., a., b.)
[ ] Check for colon-then-newline-then-item patterns
[ ] Check for "key points are:" followed by items

### Prose Conversion Check
IF lists detected:
  - Identify the conceptual grouping
  - Rewrite as flowing paragraphs with transition phrases
  - Use "firstly...additionally...furthermore...finally" structure
  - Embed list items as natural sentence elements

### Format Compliance Score: [PASS/FAIL]
</thinking>
```

### Improvement 2: DEPTH QUANTIFICATION

Add section-specific targets:
- **Abstract**: 150-250 words
- **Definition**: 100-200 words
- **Core Principles**: 300-500 words per principle
- **Each Sub-Section**: minimum 400 words
- **Total Report**: 5,000-8,000 words minimum

### Improvement 3: TEMPLATE PROSE CONVERSION

Convert this:
```
**2. Phase 1: Overture & Foundation**
    * **Abstract:** Start with a `> [!abstract]` callout...
    * **Definition:** Provide a clear, unambiguous...
```

To this:
```
**Phase 1: Overture & Foundation** begins with establishing the conceptual bedrock 
of the topic. Your opening moves through three essential stages. First, you craft 
an abstract that synthesizes the entire topic into a high-level overview spanning 
one to two comprehensive paragraphs, using the `> [!abstract]` callout to frame 
this summary. Following the abstract, you provide a precise, unambiguous definition 
enclosed in a `> [!definition]` callout, ensuring terminological clarity from the 
outset. Finally, you articulate the core principles using either `> [!the-philosophy]` 
or `> [!core-principle]` callouts to explain the fundamental ideas...
```

### Improvement 4: REASONING TECHNIQUE MAPPING

Add to report generation:
```
Phase 1 (Foundation): Use Chain of Thought for clear linear definition
Phase 2 (Deep Dive): Use Tree of Thoughts to explore multiple sub-topic branches
Phase 3 (Integration): Use Graph of Thoughts to map concept connections
Phase 4 (Synthesis): Use Self-Consistency to validate key claims
```

### Improvement 5: EXAMPLES SECTION

Add explicit good/bad examples:

**❌ FORBIDDEN FORMAT:**
```
The key neurotransmitters are:
- Dopamine: reward and motivation
- Serotonin: mood regulation
- GABA: inhibition
```

**✅ REQUIRED FORMAT:**
```
The brain's chemical communication relies on several critical neurotransmitters, 
each serving distinct but interconnected functions. Dopamine orchestrates the 
brain's reward and motivation systems, creating the neurochemical foundation 
for goal-directed behavior and pleasure responses. Serotonin operates as the 
primary regulator of mood states, with its activity levels directly influencing 
emotional stability and affective tone. GABA (gamma-aminobutyric acid) functions 
as the brain's principal inhibitory neurotransmitter, dampening neural excitation 
and maintaining the delicate balance between activation and suppression that 
enables coherent cognitive function.
```

---

## Validation Metrics

### Before Improvements:
- List detection in output: LIKELY (due to template modeling)
- Prose compliance: UNCERTAIN (no validation mechanism)
- Depth consistency: VARIABLE (no quantitative targets)
- Format quality: INCONSISTENT (contradictory instructions)

### After Improvements:
- List detection in output: UNLIKELY (validation protocol catches)
- Prose compliance: HIGH (pre-output checklist)
- Depth consistency: HIGH (word count minimums)
- Format quality: CONSISTENT (resolved contradictions)

