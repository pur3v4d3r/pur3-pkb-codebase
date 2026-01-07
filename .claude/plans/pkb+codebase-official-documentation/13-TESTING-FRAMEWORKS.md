---
title: SPES Testing Frameworks
document_type: advanced_guide
tier: 3
priority: critical
version: 1.0.0
status: published
prerequisites: ["Component Creation Guide", "Workflow Execution Tutorial", "Intelligence Layer Setup"]
estimated_time: 120-150 minutes
last_updated: 2025-12-25
---

# SPES Testing Frameworks

**Version**: 1.0.0  
**Document Type**: Advanced Testing Guide  
**Audience**: QA engineers, advanced developers  
**Time Required**: 120-150 minutes  
**Goal**: Build comprehensive test coverage for production SPES workflows

---

## Table of Contents

1. [Testing Philosophy](#1-testing-philosophy)
2. [Component Testing](#2-component-testing)
3. [Workflow Testing](#3-workflow-testing)
4. [LLM Output Validation](#4-llm-output-validation)
5. [Integration Testing](#5-integration-testing)
6. [Performance Testing](#6-performance-testing)
7. [Regression Testing](#7-regression-testing)
8. [Test Automation](#8-test-automation)
9. [CI/CD Integration](#9-cicd-integration)
10. [Quality Metrics](#10-quality-metrics)

---

## 1. Testing Philosophy

### 1.1 Test Pyramid for AI Workflows

Traditional test pyramids need adaptation for LLM-based systems:

```
        ┌─────────────┐
        │   E2E Tests │  Manual validation, exploratory
        │   (Manual)  │  ~5% of effort
        └─────────────┘
       ┌───────────────┐
       │  Integration  │  Multi-component workflows
       │     Tests     │  ~15% of effort
       └───────────────┘
      ┌─────────────────┐
      │  Workflow Tests │  Single workflow validation
      │                 │  ~30% of effort
      └─────────────────┘
     ┌───────────────────┐
     │  Component Tests  │  Individual component quality
     │                   │  ~30% of effort
     └───────────────────┘
    ┌─────────────────────┐
    │   Output Validation │  LLM response checking
    │       (Fuzzy)       │  ~20% of effort
    └─────────────────────┘
```

### 1.2 Unique Challenges

**LLM Non-Determinism**:
- Same prompt → different outputs
- Cannot use exact string matching
- Need fuzzy validation strategies

**Context Sensitivity**:
- Output quality depends on prompt composition
- Component interaction effects
- Token budget constraints

**Cost Constraints**:
- Each test call costs money (cloud LLMs)
- Need to balance coverage vs. cost
- Use local LLMs for frequent tests

### 1.3 Testing Strategy

```python
# testing/test_strategy.py
from enum import Enum

class TestLevel(Enum):
    """Test levels in order of execution."""
    UNIT = 1          # Component structure, metadata
    INTEGRATION = 2   # Component composition
    WORKFLOW = 3      # Full workflow execution
    PERFORMANCE = 4   # Speed, token usage
    REGRESSION = 5    # Historical baselines

class TestCostTier(Enum):
    """Cost tiers for test execution."""
    FREE = "local"        # Local LLMs, no API cost
    LOW = "gemini"        # Cheap cloud LLM
    MEDIUM = "claude"     # Production LLM
    HIGH = "manual"       # Human evaluation

# Test execution strategy
STRATEGY = {
    TestLevel.UNIT: TestCostTier.FREE,       # Fast, local
    TestLevel.INTEGRATION: TestCostTier.LOW,  # Gemini
    TestLevel.WORKFLOW: TestCostTier.MEDIUM,  # Claude
    TestLevel.PERFORMANCE: TestCostTier.LOW,  # Gemini
    TestLevel.REGRESSION: TestCostTier.HIGH   # Manual
}
```

---

## 2. Component Testing

### 2.1 Complete Component Test Suite

This comprehensive test suite validates all aspects of component quality:

```python
#!/usr/bin/env python3
"""
Component Testing Framework
Validate component structure, metadata, and quality
"""

import yaml
import pytest
from pathlib import Path
from typing import Dict, Any, List

class ComponentValidator:
    """Validate component files."""
    
    REQUIRED_FIELDS = [
        'title', 'type', 'version', 'status', 'tags', 'description'
    ]
    
    VALID_TYPES = ['instruction', 'persona', 'format', 'constraint']
    VALID_STATUSES = ['draft', 'review', 'published', 'deprecated', 'archived']
    
    @staticmethod
    def load_component(component_path: Path) -> Dict[str, Any]:
        """Load and parse component file."""
        
        content = component_path.read_text(encoding='utf-8')
        
        if not content.startswith('---'):
            raise ValueError("Component must start with YAML frontmatter")
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            raise ValueError("Invalid frontmatter structure")
        
        metadata = yaml.safe_load(parts[1])
        component_content = parts[2].strip()
        
        return {
            'path': component_path,
            'metadata': metadata,
            'content': component_content,
            'full_text': content
        }
    
    def validate_metadata(self, component: Dict[str, Any]) -> List[str]:
        """Validate component metadata returns list of errors."""
        
        errors = []
        metadata = component['metadata']
        
        # Check required fields
        for field in self.REQUIRED_FIELDS:
            if field not in metadata:
                errors.append(f"Missing required field: {field}")
        
        # Validate type
        if 'type' in metadata:
            if metadata['type'] not in self.VALID_TYPES:
                errors.append(f"Invalid type: {metadata['type']}")
        
        # Validate status
        if 'status' in metadata:
            if metadata['status'] not in self.VALID_STATUSES:
                errors.append(f"Invalid status: {metadata['status']}")
        
        # Validate version format (semantic versioning)
        if 'version' in metadata:
            version = str(metadata['version'])
            parts = version.split('.')
            if len(parts) != 3:
                errors.append(f"Invalid version format: {version}")
            else:
                try:
                    [int(p) for p in parts]
                except ValueError:
                    errors.append(f"Version must be numeric: {version}")
        
        # Validate tags
        if 'tags' in metadata:
            tags = metadata['tags']
            if not isinstance(tags, list):
                errors.append("Tags must be a list")
            elif len(tags) == 0:
                errors.append("Tags cannot be empty")
        
        # Validate description length
        if 'description' in metadata:
            desc = metadata['description']
            if len(desc) > 200:
                errors.append(f"Description too long: {len(desc)} chars")
        
        return errors
    
    def validate_content(self, component: Dict[str, Any]) -> List[str]:
        """Validate component content quality."""
        
        errors = []
        content = component['content']
        
        # Check minimum length
        if len(content) < 100:
            errors.append(f"Content too short: {len(content)} chars")
        
        # Check for placeholder text
        placeholders = ['TODO', 'FIXME', 'TBD', 'PLACEHOLDER']
        for placeholder in placeholders:
            if placeholder in content:
                errors.append(f"Contains placeholder: {placeholder}")
        
        # Check for headings
        if not any(line.startswith('#') for line in content.split('\n')):
            errors.append("No headings found in content")
        
        # Check for examples (recommended)
        if 'example' not in content.lower():
            errors.append("Warning: No examples found")
        
        return errors
```

**Save as**: `testing/test_components.py`

### 2.2 Quality Metrics Calculator

Measures component quality across multiple dimensions:

```python
class ComponentMetrics:
    """Calculate quality metrics for components."""
    
    def calculate_completeness(self, component: Dict) -> float:
        """Calculate completeness score (0-1)."""
        
        score = 0.0
        max_score = 10.0
        
        metadata = component['metadata']
        content = component['content']
        
        # Required fields (4 points)
        required_present = sum(
            1 for field in ComponentValidator.REQUIRED_FIELDS
            if field in metadata
        )
        score += (required_present / len(ComponentValidator.REQUIRED_FIELDS)) * 4
        
        # Recommended fields (2 points)
        if 'llm_compatibility' in metadata:
            score += 1
        if 'context_budget' in metadata:
            score += 1
        
        # Examples (2 points)
        if 'example' in content.lower():
            score += 2
        
        # Usage notes (2 points)
        if 'usage' in content.lower():
            score += 2
        
        return score / max_score
    
    def calculate_overall_quality(self, component: Dict) -> Dict[str, float]:
        """Calculate all quality metrics."""
        
        completeness = self.calculate_completeness(component)
        clarity = self.calculate_clarity(component)
        maintainability = self.calculate_maintainability(component)
        
        # Weighted average
        overall = (
            completeness * 0.4 +
            clarity * 0.3 +
            maintainability * 0.3
        )
        
        return {
            'completeness': completeness,
            'clarity': clarity,
            'maintainability': maintainability,
            'overall': overall
        }
```

**Quality Standards**:
- **Completeness**: ≥ 0.8 (80%)
- **Clarity**: ≥ 0.7 (70%)
- **Maintainability**: ≥ 0.7 (70%)
- **Overall**: ≥ 0.75 (75%)

---

## 3. Workflow Testing

### 3.1 Workflow Test Framework

Complete framework for testing workflow execution:

```python
class WorkflowTester:
    """Test workflow execution with fuzzy validation."""
    
    def test_workflow(
        self,
        workflow_name: str,
        components: List[str],
        test_input: str,
        validators: List[callable]
    ) -> Dict[str, Any]:
        """Execute and validate workflow."""
        
        # Load components
        component_content = self._load_components(components)
        
        # Compose prompt
        prompt = "\n\n".join(component_content + [test_input])
        
        # Execute with test LLM
        adapter = self.manager.get_adapter(self.test_llm)
        response = adapter.generate(prompt, max_tokens=2048)
        
        # Validate output
        validation_results = []
        all_passed = True
        
        for validator in validators:
            result = validator(response)
            validation_results.append({
                'validator': validator.__name__,
                'passed': result
            })
            if not result:
                all_passed = False
        
        return {
            'status': 'passed' if all_passed else 'failed',
            'response': response,
            'validation_results': validation_results
        }
```

### 3.2 Validation Functions

Pre-built validators for common checks:

```python
def validate_contains_keywords(keywords: List[str]):
    """Validator: response contains all keywords."""
    def validator(response: str) -> bool:
        response_lower = response.lower()
        return all(kw.lower() in response_lower for kw in keywords)
    return validator

def validate_min_length(min_length: int):
    """Validator: response meets minimum length."""
    def validator(response: str) -> bool:
        return len(response) >= min_length
    return validator

def validate_has_code_block():
    """Validator: response contains code block."""
    def validator(response: str) -> bool:
        return '```' in response
    return validator

def validate_no_errors():
    """Validator: no error keywords in response."""
    def validator(response: str) -> bool:
        error_keywords = ['error', 'failed', 'cannot', 'unable']
        response_lower = response.lower()
        return not any(kw in response_lower for kw in error_keywords)
    return validator
```

**Example Test**:
```python
result = tester.test_workflow(
    workflow_name="Code Generation",
    components=[
        "personas/persona-senior-python-developer-v1.0.0.md",
        "instructions/instruction-code-generation-v2.0.0.md"
    ],
    test_input="Create a function to validate email addresses using regex.",
    validators=[
        validate_contains_keywords(['def', 'email', 'regex']),
        validate_has_code_block(),
        validate_min_length(100),
        validate_no_errors()
    ]
)

assert result['status'] == 'passed'
```

---

## 4. LLM Output Validation

### 4.1 Fuzzy Validation Strategies

LLM outputs are non-deterministic - exact matching fails. Use fuzzy validators:

```python
class LLMValidator:
    """Fuzzy validators for non-deterministic outputs."""
    
    @staticmethod
    def semantic_similarity(
        response: str,
        expected_concepts: List[str],
        threshold: float = 0.7
    ) -> bool:
        """Check if response covers expected concepts."""
        
        response_lower = response.lower()
        present = sum(
            1 for concept in expected_concepts
            if concept.lower() in response_lower
        )
        ratio = present / len(expected_concepts)
        return ratio >= threshold
    
    @staticmethod
    def structure_validator(
        response: str,
        required_sections: List[str]
    ) -> bool:
        """Validate response has required sections."""
        
        import re
        headings = re.findall(r'^#{1,3}\s+(.+)$', response, re.MULTILINE)
        headings_lower = [h.lower() for h in headings]
        
        for section in required_sections:
            section_lower = section.lower()
            if not any(section_lower in h for h in headings_lower):
                return False
        return True
    
    @staticmethod
    def code_quality_validator(response: str) -> Dict[str, bool]:
        """Validate code quality in response."""
        
        import re
        code_blocks = re.findall(r'```(?:\w+)?\n(.*?)\n```', response, re.DOTALL)
        
        if not code_blocks:
            return {'has_code': False}
        
        code = "\n".join(code_blocks)
        
        return {
            'has_code': True,
            'has_functions': 'def ' in code or 'function ' in code,
            'has_docstrings': '"""' in code or "'''" in code,
            'has_comments': '#' in code or '//' in code,
            'has_type_hints': ': ' in code and '->' in code,
            'reasonable_length': 50 < len(code) < 5000
        }
    
    @staticmethod
    def json_validator(response: str) -> bool:
        """Validate that response contains valid JSON."""
        
        import re
        import json
        
        json_match = re.search(r'(\{.*\}|\[.*\])', response, re.DOTALL)
        if not json_match:
            return False
        
        try:
            json.loads(json_match.group(1))
            return True
        except json.JSONDecodeError:
            return False
```

### 4.2 Validation Patterns

**Pattern 1: Semantic Coverage**
```python
# Check if key concepts are present (fuzzy)
validator.semantic_similarity(
    response,
    expected_concepts=['rate limiting', 'algorithm', 'threshold'],
    threshold=0.7  # 70% of concepts must be present
)
```

**Pattern 2: Structure Validation**
```python
# Check document structure
validator.structure_validator(
    response,
    required_sections=['Introduction', 'Implementation', 'Examples']
)
```

**Pattern 3: Code Quality**
```python
# Validate code characteristics
quality = validator.code_quality_validator(response)
assert quality['has_code']
assert quality['has_functions']
assert quality['has_docstrings']
```

---

## 5. Integration Testing

### 5.1 Multi-Component Integration

Test how components work together:

```python
class IntegrationTester:
    """Test component integration."""
    
    def test_persona_instruction_integration(
        self,
        persona_component: str,
        instruction_component: str,
        test_input: str
    ) -> dict:
        """Test persona + instruction integration."""
        
        # Load components
        persona_content = self._load_component(persona_component)
        instruction_content = self._load_component(instruction_component)
        
        # Compose and execute
        prompt = f"{persona_content}\n\n{instruction_content}\n\n{test_input}"
        response = self.adapter.generate(prompt, max_tokens=2048)
        
        # Validate integration effects
        return {
            'response': response,
            'persona_influenced_tone': self._check_tone(response, persona_component),
            'instruction_influenced_structure': self._check_structure(response)
        }
```

**Integration Test Example**:
```python
def test_python_expert_code_generation(tester):
    """Test Python expert persona with code generation."""
    
    result = tester.test_persona_instruction_integration(
        persona_component="persona-senior-python-developer-v1.0.0.md",
        instruction_component="instruction-code-generation-v2.0.0.md",
        test_input="Create a function to parse JSON config files."
    )
    
    assert result['persona_influenced_tone']  # Technical tone
    assert result['instruction_influenced_structure']  # Code + explanation
    assert '```python' in result['response']  # Python code present
```

---

## 6. Performance Testing

### 6.1 Latency Benchmarking

Measure and track workflow performance:

```python
class PerformanceTester:
    """Benchmark workflow performance."""
    
    def benchmark_workflow(
        self,
        workflow_name: str,
        components: List[str],
        test_input: str,
        provider: LLMProvider,
        iterations: int = 3
    ) -> Dict:
        """Benchmark complete workflow."""
        
        times = []
        
        for i in range(iterations):
            start = time.time()
            response = self._execute_workflow(components, test_input, provider)
            end = time.time()
            
            times.append({
                'total': end - start,
                'response_length': len(response)
            })
        
        return {
            'workflow': workflow_name,
            'provider': provider.value,
            'timing': {
                'mean_s': statistics.mean(t['total'] for t in times),
                'min_s': min(t['total'] for t in times),
                'max_s': max(t['total'] for t in times)
            },
            'output': {
                'mean_chars': statistics.mean(t['response_length'] for t in times)
            }
        }
```

**Performance Targets**:
- **Component Load**: < 10ms
- **Simple Workflow**: < 5s (local LLM)
- **Complex Workflow**: < 30s (cloud LLM)
- **Tokens/Second**: > 50 (cloud), > 20 (local)

---

## 7. Regression Testing

### 7.1 Baseline Comparison

Track changes over time:

```python
class RegressionTester:
    """Test for regressions against baselines."""
    
    def save_baseline(self, test_name: str, output: str):
        """Save output as baseline."""
        baseline_file = self.baseline_dir / f"{test_name}.json"
        baseline = {
            'output': output,
            'created_at': datetime.now().isoformat()
        }
        with open(baseline_file, 'w') as f:
            json.dump(baseline, f, indent=2)
    
    def compare_outputs(
        self,
        current: str,
        baseline: str,
        tolerance: float = 0.1
    ) -> Dict:
        """Compare current vs baseline."""
        
        from difflib import SequenceMatcher
        
        similarity = SequenceMatcher(None, current, baseline).ratio()
        passed = similarity >= (1 - tolerance)
        
        return {
            'passed': passed,
            'similarity': similarity,
            'tolerance': tolerance
        }
```

**Regression Test Workflow**:
1. **First Run**: Save as baseline
2. **Subsequent Runs**: Compare to baseline
3. **Acceptable Variance**: 10-15% difference allowed
4. **Update Baseline**: When intentional changes made

---

## 8. Test Automation

### 8.1 Automated Test Runner

Complete test suite runner:

```bash
#!/bin/bash
# testing/run_tests.sh

echo "SPES Test Suite"

# 1. Unit Tests (Components)
pytest testing/test_components.py --verbose

# 2. Integration Tests
pytest testing/test_integration.py --verbose

# 3. Workflow Tests
pytest testing/test_workflows.py --verbose

# 4. Performance Tests (optional)
if [ "$RUN_PERF" = "true" ]; then
    pytest testing/test_performance.py --verbose -m slow
fi

# 5. Regression Tests
pytest testing/test_regression.py --verbose

# Generate reports
python testing/generate_metrics.py

echo "✓ Test run complete"
echo "Reports in: testing/reports/"
```

**Usage**:
```bash
# Run full suite
./testing/run_tests.sh

# Run specific level
pytest testing/test_components.py -v

# Run with performance tests
RUN_PERF=true ./testing/run_tests.sh
```

---

## 9. CI/CD Integration

### 9.1 GitHub Actions Workflow

```yaml
name: SPES Test Suite

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      env:
        GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
      run: |
        pytest testing/ --cov=spes --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        files: ./coverage.xml
```

---

## 10. Quality Metrics

### 10.1 Metrics Dashboard

Track quality over time:

```python
class MetricsDashboard:
    """Generate quality metrics dashboard."""
    
    def collect_metrics(self) -> dict:
        """Collect all metrics."""
        return {
            'components': {
                'total': self._count_components(),
                'by_type': self._components_by_type(),
                'quality_scores': self._quality_scores()
            },
            'workflows': {
                'total': self._count_workflows(),
                'success_rate': self._workflow_success_rate()
            },
            'performance': {
                'avg_latency': self._avg_latency(),
                'tokens_per_second': self._tokens_per_second()
            }
        }
    
    def generate_dashboard(self, metrics: dict) -> str:
        """Generate Markdown dashboard."""
        return f"""
# SPES Quality Dashboard

## Components
- Total: {metrics['components']['total']}
- Average Quality: {metrics['components']['quality_scores']['average']:.2%}

## Workflows
- Total: {metrics['workflows']['total']}
- Success Rate: {metrics['workflows']['success_rate']:.2%}

## Performance
- Average Latency: {metrics['performance']['avg_latency']:.2f}s
- Tokens/Second: {metrics['performance']['tokens_per_second']:.1f}
"""
```

**Key Metrics to Track**:
- Component count and quality scores
- Test coverage percentage
- Workflow success rates
- Average latency by provider
- Token usage and costs
- Regression test results

---

## Conclusion

**You've built a comprehensive testing framework!** 🎓

**Testing Capabilities**:
- ✅ Component structure validation
- ✅ Component quality metrics
- ✅ Workflow execution testing
- ✅ LLM output validation (fuzzy)
- ✅ Integration testing
- ✅ Performance benchmarking
- ✅ Regression testing
- ✅ Test automation
- ✅ CI/CD integration
- ✅ Quality metrics dashboard

**Testing Strategy Summary**:

| Test Level | Tool | Cost | Frequency |
|------------|------|------|-----------|
| **Unit** | Pytest | Free | Every commit |
| **Integration** | Pytest + Gemini | Low | Daily |
| **Workflow** | Pytest + Claude | Medium | Pre-release |
| **Performance** | Benchmarks | Low | Weekly |
| **Regression** | Manual + Auto | High | Major releases |

**Best Practices**:
1. **Start with unit tests** - cheapest, fastest feedback
2. **Use local LLMs** for development testing
3. **Reserve cloud LLMs** for critical path validation
4. **Track baselines** to detect regressions
5. **Automate everything** possible
6. **Monitor metrics** over time

**Time Invested**: ⏱️ 120-150 minutes  
**Ready For**: Production testing and quality assurance

**Next Steps**:
1. Set up test infrastructure
2. Run baseline tests
3. Configure CI/CD
4. Establish quality thresholds
5. Monitor and iterate

Would you like to continue with Performance Optimization or Advanced Workflow Patterns?
