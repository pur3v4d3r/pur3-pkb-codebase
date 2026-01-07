---
tags: #integration-patterns #implementation-recipes #code-examples #production-patterns #best-practices #common-scenarios
aliases: [Integration Cookbook, Implementation Recipes, Practical Patterns, Code Examples]
created: 2025-01-06
modified: 2025-01-06
status: evergreen
certainty: verified
type: cookbook
version: 1.0.0
source: claude-sonnet-4.5
category: practical-implementation
priority: high
audience: [developers, engineers, implementers]
prerequisites: [doc1-llm-reasoning-techniques-operational-manual, doc4-agentic-workflow-design-patterns]
---

# Integration Patterns Cookbook

> [!abstract] Purpose
> **[Integration-Patterns-Cookbook**:: Collection of battle-tested implementation recipes for common reasoning and agentic workflow scenarios - providing copy-paste ready code with explanations for rapid integration into production systems.]**

---

## 📚 Recipe Index

### Reasoning Patterns
1. [[#Recipe 1 Multi-Step Math Problem Solver]]
2. [[#Recipe 2 Research Assistant with Verification]]
3. [[#Recipe 3 Code Generation with Validation]]
4. [[#Recipe 4 Multi-Document Analysis]]

### Agentic Workflows
5. [[#Recipe 5 Task Planning and Execution]]
6. [[#Recipe 6 Iterative Content Refinement]]
7. [[#Recipe 7 Multi-Agent Collaboration]]
8. [[#Recipe 8 Error Recovery Pipeline]]

### Production Patterns
9. [[#Recipe 9 Caching and Rate Limiting]]
10. [[#Recipe 10 Monitoring and Logging]]
11. [[#Recipe 11 Cost Optimization]]
12. [[#Recipe 12 Quality Assurance Pipeline]]

---

## Recipe 1: Multi-Step Math Problem Solver

**Scenario**: Solve complex math problems with guaranteed precision

**Pattern**: Program of Thoughts + Validation

**Implementation**:

```python
import ast
import operator

class MathSolver:
    """
    Solve math problems using PoT pattern.
    """
    
    def solve(self, problem):
        """
        Generate code and execute for precision.
        """
        # Generate Python code
        code_prompt = f"""
Problem: {problem}

Write Python code to solve this problem. Use clear variable names.
Print the final answer.

```python
"""
        code_response = self.model.generate(code_prompt, temperature=0.3)
        code = self.extract_code(code_response)
        
        # Execute code safely
        try:
            result = self.safe_execute(code)
            
            # Validate result makes sense
            if self.validate_result(result, problem):
                return {
                    'answer': result,
                    'code': code,
                    'confidence': 'high'
                }
        except Exception as e:
            # Fallback to CoT if code fails
            return self.fallback_cot(problem)
    
    def safe_execute(self, code):
        """
        Execute code in restricted environment.
        """
        allowed_names = {
            'abs': abs, 'round': round, 'min': min, 'max': max,
            'sum': sum, 'len': len, 'range': range
        }
        
        local_vars = {}
        exec(code, {"__builtins__": allowed_names}, local_vars)
        
        # Extract printed output or return value
        return local_vars.get('result', local_vars.get('answer'))

# Usage
solver = MathSolver(model)
result = solver.solve("If a train travels 120 km in 2 hours, how far in 5 hours?")
print(result['answer'])  # 300.0
```

---

## Recipe 2: Research Assistant with Verification

**Scenario**: Answer questions with fact-checking

**Pattern**: RAG + Chain of Verification

**Implementation**:

```python
class ResearchAssistant:
    """
    RAG with verification for factual accuracy.
    """
    
    def __init__(self, retriever, model):
        self.retriever = retriever
        self.model = model
    
    def research(self, question):
        """
        Retrieve, answer, verify, correct.
        """
        # Stage 1: Retrieve documents
        docs = self.retriever.retrieve(question, top_k=5)
        
        # Stage 2: Generate initial answer
        context = "\n\n".join([d.content for d in docs])
        initial_answer = self.model.generate(f"""
Context: {context}

Question: {question}

Based on the context, answer the question:
""")
        
        # Stage 3: Extract verifiable claims
        claims = self.extract_claims(initial_answer)
        
        # Stage 4: Verify each claim independently
        verifications = []
        for claim in claims:
            # IMPORTANT: Verify WITHOUT showing initial answer
            verification = self.model.generate(f"""
Context: {context}

Is this statement supported by the context?
Statement: {claim}

Answer (Yes/No with explanation):
""")
            verifications.append((claim, verification))
        
        # Stage 5: Generate corrected answer if needed
        has_errors = any('No' in v[1] for v in verifications)
        
        if has_errors:
            corrected_answer = self.model.generate(f"""
Question: {question}
Context: {context}
Initial answer: {initial_answer}

Verification results:
{self.format_verifications(verifications)}

Generate a corrected answer addressing the verification issues:
""")
            return {
                'answer': corrected_answer,
                'verified': True,
                'corrections_made': True
            }
        
        return {
            'answer': initial_answer,
            'verified': True,
            'corrections_made': False
        }

# Usage
assistant = ResearchAssistant(retriever, model)
result = assistant.research("When was Marie Curie born?")
print(result['answer'])
```

---

## Recipe 3: Code Generation with Validation

**Scenario**: Generate and validate code before deployment

**Pattern**: Iterative Refinement + Testing

**Implementation**:

```python
class CodeGenerator:
    """
    Generate code with automatic testing and refinement.
    """
    
    def generate_function(self, specification, test_cases):
        """
        Generate code and iteratively fix until tests pass.
        """
        max_attempts = 3
        
        for attempt in range(max_attempts):
            # Generate code
            code = self.generate_code(specification, attempt)
            
            # Run tests
            test_results = self.run_tests(code, test_cases)
            
            if test_results['all_passed']:
                return {
                    'code': code,
                    'status': 'success',
                    'attempts': attempt + 1
                }
            
            # Generate fix based on failures
            specification = self.add_test_feedback(
                specification,
                test_results['failures']
            )
        
        return {
            'code': code,
            'status': 'failed_validation',
            'attempts': max_attempts,
            'failures': test_results['failures']
        }
    
    def generate_code(self, spec, attempt):
        """
        Generate code with refinement context.
        """
        prompt = f"""
Generate a Python function for:
{spec}

Function should be production-ready with:
- Type hints
- Docstring
- Error handling
- Input validation

```python
"""
        return self.model.generate(prompt, temperature=0.3)
    
    def run_tests(self, code, test_cases):
        """
        Execute test cases against generated code.
        """
        results = {'all_passed': True, 'failures': []}
        
        # Execute code to define function
        local_scope = {}
        exec(code, local_scope)
        
        # Get the function (assume first function defined)
        func_name = [k for k in local_scope if callable(local_scope[k])][0]
        func = local_scope[func_name]
        
        # Run test cases
        for test in test_cases:
            try:
                result = func(*test['input'])
                if result != test['expected']:
                    results['all_passed'] = False
                    results['failures'].append({
                        'input': test['input'],
                        'expected': test['expected'],
                        'got': result
                    })
            except Exception as e:
                results['all_passed'] = False
                results['failures'].append({
                    'input': test['input'],
                    'error': str(e)
                })
        
        return results

# Usage
generator = CodeGenerator(model)

spec = "Function that calculates factorial of n"
tests = [
    {'input': [0], 'expected': 1},
    {'input': [5], 'expected': 120},
    {'input': [10], 'expected': 3628800}
]

result = generator.generate_function(spec, tests)
print(result['code'])
```

---

## Recipe 4: Multi-Document Analysis

**Scenario**: Synthesize information across multiple documents

**Pattern**: Parallel Retrieval + Synthesis

**Implementation**:

```python
from concurrent.futures import ThreadPoolExecutor

class MultiDocAnalyzer:
    """
    Analyze and synthesize across multiple documents.
    """
    
    def analyze_documents(self, query, documents):
        """
        Parallel analysis then synthesis.
        """
        # Phase 1: Analyze each document in parallel
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {
                executor.submit(self.analyze_single, doc, query): doc
                for doc in documents
            }
            
            doc_analyses = []
            for future in futures:
                doc = futures[future]
                analysis = future.result()
                doc_analyses.append({
                    'document': doc.title,
                    'analysis': analysis
                })
        
        # Phase 2: Synthesize across analyses
        synthesis = self.synthesize(query, doc_analyses)
        
        return synthesis
    
    def analyze_single(self, document, query):
        """
        Extract relevant information from single document.
        """
        prompt = f"""
Document: {document.content}

Query: {query}

Extract key information from this document relevant to the query:
"""
        return self.model.generate(prompt)
    
    def synthesize(self, query, doc_analyses):
        """
        Synthesize insights across document analyses.
        """
        analyses_text = "\n\n".join([
            f"Document {i+1} ({a['document']}):\n{a['analysis']}"
            for i, a in enumerate(doc_analyses)
        ])
        
        prompt = f"""
Query: {query}

Individual Document Analyses:
{analyses_text}

Synthesize a comprehensive answer integrating information across all documents.
Identify agreements, disagreements, and unique insights from each source.

Synthesis:
"""
        return self.model.generate(prompt)

# Usage
analyzer = MultiDocAnalyzer(model)
docs = load_documents(["doc1.pdf", "doc2.pdf", "doc3.pdf"])
result = analyzer.analyze_documents("What are key trends?", docs)
```

---

## Recipe 5: Task Planning and Execution

**Scenario**: Break down complex task and execute systematically

**Pattern**: Hierarchical Task Decomposition

**Implementation**:

```python
class TaskPlanner:
    """
    Plan and execute complex tasks hierarchically.
    """
    
    def execute_task(self, goal, max_depth=2):
        """
        Decompose and solve recursively.
        """
        return self.solve(goal, depth=0, max_depth=max_depth)
    
    def solve(self, task, depth, max_depth):
        """
        Recursive task solving with decomposition.
        """
        # Base case: Atomic task or max depth reached
        if self.is_atomic(task) or depth >= max_depth:
            return self.execute_atomic(task)
        
        # Decompose into subtasks
        subtasks = self.decompose(task)
        
        # Solve each subtask
        subtask_results = []
        for subtask in subtasks:
            result = self.solve(subtask, depth + 1, max_depth)
            subtask_results.append({
                'subtask': subtask,
                'result': result
            })
            
            # Check if failure requires stopping
            if not result['success'] and subtask['critical']:
                return {
                    'success': False,
                    'error': f"Critical subtask failed: {subtask['description']}"
                }
        
        # Synthesize results
        return self.synthesize(task, subtask_results)
    
    def decompose(self, task):
        """
        Break task into subtasks.
        """
        prompt = f"""
Task: {task}

Break this into 3-5 subtasks that can be completed independently.
For each subtask specify:
- Description
- Is it critical to overall task? (true/false)
- Estimated complexity (low/medium/high)

Format as JSON array.
"""
        response = self.model.generate(prompt)
        return json.loads(response)
    
    def is_atomic(self, task):
        """
        Check if task is simple enough to solve directly.
        """
        complexity = self.estimate_complexity(task)
        return complexity == 'low'

# Usage
planner = TaskPlanner(model)
result = planner.execute_task(
    "Create a quarterly sales report with trends and forecasts"
)
```

---

## Recipe 6: Iterative Content Refinement

**Scenario**: Generate high-quality content through critique cycles

**Pattern**: Generate → Critique → Refine

**Implementation**:

```python
class ContentRefiner:
    """
    Iteratively improve content quality.
    """
    
    def generate_refined_content(self, brief, max_iterations=3):
        """
        Iterative refinement until quality threshold met.
        """
        # Initial generation
        content = self.generate(brief)
        
        for iteration in range(max_iterations):
            # Critique
            critique = self.critique(content, brief)
            
            # Check quality
            if critique['quality_score'] >= 8:
                return {
                    'content': content,
                    'iterations': iteration + 1,
                    'final_score': critique['quality_score']
                }
            
            # Refine based on critique
            content = self.refine(content, critique, brief)
        
        return {
            'content': content,
            'iterations': max_iterations,
            'final_score': critique['quality_score']
        }
    
    def critique(self, content, brief):
        """
        Generate critique with scoring.
        """
        prompt = f"""
Brief: {brief}
Content: {content}

Critique this content:
1. Clarity (1-10):
2. Accuracy (1-10):
3. Completeness (1-10):
4. Engagement (1-10):

Overall score (1-10):
Key weaknesses:
Specific improvements needed:
"""
        response = self.model.generate(prompt)
        return self.parse_critique(response)
    
    def refine(self, content, critique, brief):
        """
        Improve content based on critique.
        """
        prompt = f"""
Original brief: {brief}
Current content: {content}

Critique identified these issues:
{critique['weaknesses']}

Improvements needed:
{critique['improvements']}

Generate improved version addressing all critique points:
"""
        return self.model.generate(prompt)

# Usage
refiner = ContentRefiner(model)
result = refiner.generate_refined_content(
    "Blog post explaining quantum computing for beginners"
)
print(result['content'])
```

---

## Recipe 9: Caching and Rate Limiting

**Scenario**: Optimize costs and manage API limits

**Pattern**: Semantic Caching + Token Bucket

**Implementation**:

```python
import hashlib
import time
from collections import deque

class CachedModel:
    """
    Model with semantic caching and rate limiting.
    """
    
    def __init__(self, model, cache_ttl=3600, rate_limit=100):
        self.model = model
        self.cache = {}
        self.cache_ttl = cache_ttl
        
        # Token bucket for rate limiting
        self.rate_limit = rate_limit
        self.tokens = rate_limit
        self.last_refill = time.time()
        self.token_refill_rate = rate_limit / 60  # per second
    
    def generate(self, prompt, **kwargs):
        """
        Generate with caching and rate limiting.
        """
        # Check cache
        cache_key = self.get_cache_key(prompt, kwargs)
        cached = self.check_cache(cache_key)
        if cached:
            return cached
        
        # Rate limiting
        self.wait_for_token()
        
        # Generate
        result = self.model.generate(prompt, **kwargs)
        
        # Cache result
        self.cache[cache_key] = {
            'result': result,
            'timestamp': time.time()
        }
        
        return result
    
    def get_cache_key(self, prompt, kwargs):
        """
        Generate cache key from prompt and parameters.
        """
        # Include key parameters in hash
        key_params = {
            'prompt': prompt,
            'temperature': kwargs.get('temperature', 0.7),
            'max_tokens': kwargs.get('max_tokens', 1000)
        }
        key_string = json.dumps(key_params, sort_keys=True)
        return hashlib.sha256(key_string.encode()).hexdigest()
    
    def check_cache(self, cache_key):
        """
        Check cache for valid entry.
        """
        if cache_key in self.cache:
            entry = self.cache[cache_key]
            age = time.time() - entry['timestamp']
            
            if age < self.cache_ttl:
                return entry['result']
            else:
                del self.cache[cache_key]
        
        return None
    
    def wait_for_token(self):
        """
        Implement token bucket rate limiting.
        """
        # Refill tokens
        now = time.time()
        elapsed = now - self.last_refill
        refill_amount = elapsed * self.token_refill_rate
        self.tokens = min(self.rate_limit, self.tokens + refill_amount)
        self.last_refill = now
        
        # Wait if no tokens available
        if self.tokens < 1:
            wait_time = (1 - self.tokens) / self.token_refill_rate
            time.sleep(wait_time)
            self.tokens = 1
        
        # Consume token
        self.tokens -= 1

# Usage
cached_model = CachedModel(model, cache_ttl=3600, rate_limit=100)
result = cached_model.generate("What is the capital of France?")
```

---

## Recipe 10: Monitoring and Logging

**Scenario**: Track performance and debug issues

**Pattern**: Structured Logging + Metrics

**Implementation**:

```python
import logging
import json
from datetime import datetime

class MonitoredAgent:
    """
    Agent with comprehensive monitoring.
    """
    
    def __init__(self, model):
        self.model = model
        self.logger = self.setup_logging()
        self.metrics = MetricsCollector()
    
    def setup_logging(self):
        """
        Configure structured logging.
        """
        logger = logging.getLogger('agent')
        logger.setLevel(logging.INFO)
        
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def execute_monitored(self, task):
        """
        Execute with monitoring.
        """
        request_id = generate_id()
        start_time = time.time()
        
        # Log start
        self.logger.info(f"Starting task", extra={
            'request_id': request_id,
            'task': task,
            'timestamp': datetime.now().isoformat()
        })
        
        try:
            # Execute
            result = self.execute(task)
            
            # Record success metrics
            latency = time.time() - start_time
            self.metrics.record('task_success', {
                'request_id': request_id,
                'latency_seconds': latency,
                'task_type': classify_task(task)
            })
            
            self.logger.info(f"Task completed", extra={
                'request_id': request_id,
                'latency_seconds': latency,
                'status': 'success'
            })
            
            return result
            
        except Exception as e:
            # Record failure metrics
            self.metrics.record('task_failure', {
                'request_id': request_id,
                'error_type': type(e).__name__,
                'error_message': str(e)
            })
            
            self.logger.error(f"Task failed", extra={
                'request_id': request_id,
                'error': str(e),
                'status': 'failed'
            })
            
            raise

class MetricsCollector:
    """
    Collect and aggregate metrics.
    """
    
    def __init__(self):
        self.metrics = defaultdict(list)
    
    def record(self, metric_name, data):
        """
        Record metric data point.
        """
        self.metrics[metric_name].append({
            'timestamp': time.time(),
            'data': data
        })
    
    def get_summary(self, metric_name, time_window_seconds=3600):
        """
        Get metric summary for time window.
        """
        now = time.time()
        recent = [
            m for m in self.metrics[metric_name]
            if now - m['timestamp'] < time_window_seconds
        ]
        
        return {
            'count': len(recent),
            'data_points': recent
        }
```

---

**End of Integration Patterns Cookbook**

