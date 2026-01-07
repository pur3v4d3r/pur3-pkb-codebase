---
title: SPES PKB Integration Systems
document_type: advanced_guide
tier: 3
priority: high
version: 1.0.0
status: published
prerequisites: ["Quick Start Guide", "Workflow Execution Tutorial", "Component Library Reference"]
estimated_time: 150-180 minutes
last_updated: 2025-12-25
---

# SPES PKB Integration Systems

**Version**: 1.0.0  
**Document Type**: Advanced Integration Guide  
**Audience**: Advanced users, knowledge architects  
**Time Required**: 150-180 minutes  
**Goal**: Master deep integration between SPES workflows and Obsidian PKB

---

## Table of Contents

1. [Integration Architecture](#1-integration-architecture)
2. [Smart Connections Integration](#2-smart-connections-integration)
3. [Dataview Query Patterns](#3-dataview-query-patterns)
4. [Templater Automation](#4-templater-automation)
5. [Meta Bind Interactive Elements](#5-meta-bind-interactive-elements)
6. [Workflow-to-PKB Pipelines](#6-workflow-to-pkb-pipelines)
7. [Knowledge Graph Construction](#7-knowledge-graph-construction)
8. [Memory Systems](#8-memory-systems)
9. [Advanced Integration Patterns](#9-advanced-integration-patterns)
10. [Production Examples](#10-production-examples)

---

## 1. Integration Architecture

### 1.1 Integration Layers

SPES integrates with Obsidian PKB at multiple layers:

```
┌─────────────────────────────────────────────────────────┐
│                  SPES Workflow Layer                     │
│  (Prompt composition, LLM execution, result handling)   │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              Integration Middleware                      │
│  ┌──────────┬──────────┬──────────┬──────────────────┐ │
│  │ Search   │ Template │ Query    │ Interactive      │ │
│  │ (Smart   │ (Templ-  │ (Data-   │ (Meta Bind)      │ │
│  │ Connect) │  ater)   │  view)   │                  │ │
│  └──────────┴──────────┴──────────┴──────────────────┘ │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                   Obsidian Vault                         │
│  ┌────────────┬──────────────┬────────────────────────┐ │
│  │ Notes      │ Attachments  │ Configuration          │ │
│  │ (Markdown) │ (Files)      │ (.obsidian/)           │ │
│  └────────────┴──────────────┴────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

### 1.2 Data Flow Patterns

**Pattern 1: Workflow → PKB (Capture)**
```
User Request → SPES Workflow → LLM Response → Format → Save to Vault
```

**Pattern 2: PKB → Workflow (Retrieval)**
```
Semantic Search → Relevant Notes → Inject as Context → SPES Workflow
```

**Pattern 3: Bidirectional (Interactive)**
```
Query PKB → Process with SPES → Update PKB → Trigger Automation → Repeat
```

### 1.3 File Organization Strategy

```
vault/
├── 00-meta/              # System metadata
│   ├── templates/        # Templater templates
│   ├── indexes/          # MOCs and indexes
│   └── dashboards/       # Meta Bind dashboards
│
├── 01-fleeting/          # Temporary capture
│   └── YYYY-MM-DD/       # Daily notes
│
├── 02-projects/          # Active projects
│   └── [project-name]/
│       ├── notes/
│       ├── workflows/    # Project-specific workflows
│       └── outputs/      # Generated content
│
├── 03-areas/             # Ongoing areas of responsibility
│   └── [area-name]/
│
├── 04-resources/         # Reference materials
│   ├── components/       # Reusable components
│   ├── prompts/          # Prompt templates
│   └── research/         # Research notes
│
└── 05-archives/          # Completed/inactive

.obsidian/
├── plugins/
│   ├── smart-connections/
│   ├── dataview/
│   ├── templater/
│   └── obsidian-meta-bind-plugin/
└── workspace.json

.claude/                  # SPES memory directory
├── core/                 # Core memory files
├── sessions/             # Session history
├── decisions/            # Architecture decisions
└── patterns/             # Learned patterns
```

---

## 2. Smart Connections Integration

### 2.1 Semantic Search Setup

Smart Connections enables semantic search across your vault using embeddings.

#### Configuration

```json
// .obsidian/plugins/smart-connections/data.json
{
  "api_key": "",  // Leave empty for local embeddings
  "model_key": "TaylorAI/bge-micro-v2",
  "embedding_model": "TaylorAI/bge-micro-v2",
  "smart_chat_model": "gpt-4",  // Optional
  "language": "en",
  "file_exclusions": ".obsidian,node_modules,.git",
  "folder_exclusions": "05-archives",
  "excluded_headings": "References,Changelog",
  "show_full_path": false,
  "expanded_view": true,
  "force_refresh": false,
  "show_sc_ribbon": true
}
```

#### Python Integration

```bash
cd ~/PKB-System/spes

cat > pkb_integration/smart_search.py << 'EOF'
#!/usr/bin/env python3
"""
Smart Connections Integration
Semantic search over Obsidian vault
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from sentence_transformers import SentenceTransformer
import numpy as np

class SmartSearch:
    """Semantic search over vault using same model as Smart Connections."""
    
    def __init__(self, vault_path: Path, model_name: str = "TaylorAI/bge-micro-v2"):
        self.vault_path = vault_path
        self.model = SentenceTransformer(model_name)
        self.embeddings_cache = vault_path / ".obsidian/plugins/smart-connections/embeddings.json"
        self.notes = {}
        self.embeddings = {}
        
        self._load_embeddings()
    
    def _load_embeddings(self):
        """Load cached embeddings from Smart Connections."""
        
        if self.embeddings_cache.exists():
            with open(self.embeddings_cache, 'r') as f:
                data = json.load(f)
                self.embeddings = data.get('embeddings', {})
                print(f"Loaded {len(self.embeddings)} cached embeddings")
        else:
            print("No cached embeddings found, will compute on demand")
    
    def search(
        self,
        query: str,
        limit: int = 5,
        min_similarity: float = 0.5
    ) -> List[Dict[str, Any]]:
        """
        Search vault semantically.
        
        Args:
            query: Search query
            limit: Max results to return
            min_similarity: Minimum similarity threshold (0-1)
            
        Returns:
            List of results with paths, content, and similarity scores
        """
        
        # Encode query
        query_embedding = self.model.encode(query, normalize_embeddings=True)
        
        # Get all markdown files
        md_files = list(self.vault_path.rglob("*.md"))
        
        # Compute similarities
        results = []
        for md_file in md_files:
            # Skip excluded directories
            if any(excl in str(md_file) for excl in [".obsidian", "05-archives"]):
                continue
            
            # Get embedding (from cache or compute)
            rel_path = str(md_file.relative_to(self.vault_path))
            
            if rel_path in self.embeddings:
                # Use cached embedding
                doc_embedding = np.array(self.embeddings[rel_path])
            else:
                # Compute embedding
                content = md_file.read_text(encoding='utf-8', errors='ignore')
                doc_embedding = self.model.encode(content, normalize_embeddings=True)
                self.embeddings[rel_path] = doc_embedding.tolist()
            
            # Compute similarity
            similarity = float(np.dot(query_embedding, doc_embedding))
            
            if similarity >= min_similarity:
                results.append({
                    'path': rel_path,
                    'full_path': str(md_file),
                    'similarity': similarity,
                    'preview': self._get_preview(md_file)
                })
        
        # Sort by similarity
        results.sort(key=lambda x: x['similarity'], reverse=True)
        
        return results[:limit]
    
    def _get_preview(self, file_path: Path, length: int = 200) -> str:
        """Get preview of file content."""
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            # Remove YAML frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    content = parts[2].strip()
            
            # Get first paragraph
            preview = content[:length]
            if len(content) > length:
                preview += "..."
            
            return preview
        except:
            return ""
    
    def get_related_notes(
        self,
        note_path: str,
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """Find notes related to a specific note."""
        
        full_path = self.vault_path / note_path
        
        if not full_path.exists():
            return []
        
        # Get note content
        content = full_path.read_text(encoding='utf-8', errors='ignore')
        
        # Search using note content as query
        return self.search(content, limit=limit + 1)[1:]  # Exclude self

# Example usage
if __name__ == "__main__":
    vault = Path(os.getenv("VAULT_PATH", "~/PKB-System/vault")).expanduser()
    
    searcher = SmartSearch(vault)
    
    # Test search
    results = searcher.search("machine learning optimization", limit=3)
    
    print("Search Results:")
    print("="*60)
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['path']}")
        print(f"   Similarity: {result['similarity']:.3f}")
        print(f"   Preview: {result['preview'][:100]}...")
EOF

python pkb_integration/smart_search.py
```

### 2.2 Workflow Integration Example

```python
cat > pkb_integration/context_retrieval_workflow.py << 'EOF'
#!/usr/bin/env python3
"""
Context Retrieval Workflow
Use semantic search to inject relevant context into prompts
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic
from smart_search import SmartSearch

load_dotenv()

class ContextEnhancedWorkflow:
    """Workflow with automatic context retrieval from PKB."""
    
    def __init__(self, vault_path: Path):
        self.vault = vault_path
        self.searcher = SmartSearch(vault_path)
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    def execute_with_context(
        self,
        user_query: str,
        context_limit: int = 3,
        min_similarity: float = 0.6
    ) -> str:
        """
        Execute workflow with automatic context retrieval.
        
        1. Search vault for relevant context
        2. Inject context into prompt
        3. Execute with LLM
        4. Return response
        """
        
        print("🔍 Searching vault for relevant context...")
        
        # Search for relevant notes
        relevant_notes = self.searcher.search(
            user_query,
            limit=context_limit,
            min_similarity=min_similarity
        )
        
        if relevant_notes:
            print(f"✓ Found {len(relevant_notes)} relevant notes:")
            for note in relevant_notes:
                print(f"  - {note['path']} (similarity: {note['similarity']:.3f})")
        else:
            print("  No relevant context found in vault")
        
        # Build context section
        context_section = ""
        if relevant_notes:
            context_section = "# Relevant Context from Your Knowledge Base\n\n"
            
            for i, note in enumerate(relevant_notes, 1):
                # Read full note content
                content = Path(note['full_path']).read_text(
                    encoding='utf-8',
                    errors='ignore'
                )
                
                # Remove YAML frontmatter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        content = parts[2].strip()
                
                context_section += f"## Context {i}: {note['path']}\n\n"
                context_section += f"{content}\n\n"
                context_section += "---\n\n"
        
        # Compose full prompt
        full_prompt = f"""{context_section}
# User Query

{user_query}

# Instructions

Based on the context from the knowledge base (if provided) and your knowledge, provide a comprehensive answer to the user's query. If the context is relevant, reference it in your response.
"""
        
        print("\n💭 Executing with LLM...")
        
        # Execute
        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            messages=[{"role": "user", "content": full_prompt}]
        )
        
        result = response.content[0].text
        
        print("✓ Response generated\n")
        
        return result

def main():
    """Example: Query with automatic context retrieval."""
    
    vault = Path(os.getenv("VAULT_PATH", "~/PKB-System/vault")).expanduser()
    workflow = ContextEnhancedWorkflow(vault)
    
    # User query
    query = """
    What are the best practices for prompt engineering with chain-of-thought reasoning?
    """
    
    # Execute with context retrieval
    response = workflow.execute_with_context(query, context_limit=3)
    
    print("="*60)
    print("RESPONSE")
    print("="*60)
    print(response)

if __name__ == "__main__":
    main()
EOF
```

---

## 3. Dataview Query Patterns

### 3.1 Dynamic Content Queries

Dataview enables powerful queries over vault metadata.

#### Basic Queries

```dataview
# List all workflow outputs from last 7 days
TABLE file.ctime as Created, tags
FROM "02-projects"
WHERE contains(tags, "workflow-output")
AND file.ctime >= date(today) - dur(7 days)
SORT file.ctime DESC
```

#### Component Catalog Query

```dataview
# Component library overview
TABLE 
  type as Type,
  version as Version,
  status as Status,
  context_budget as "Token Budget"
FROM "04-resources/components"
WHERE type != null
SORT type ASC, version DESC
```

#### Workflow Execution History

```dataview
# Recent workflow executions
TABLE
  workflow_name as Workflow,
  status as Status,
  duration as Duration,
  file.mtime as "Last Run"
FROM "02-projects"
WHERE workflow_name != null
SORT file.mtime DESC
LIMIT 10
```

### 3.2 JavaScript DataviewJS

More complex queries with JavaScript:

````markdown
```dataviewjs
// Find orphaned notes (no backlinks)
const pages = dv.pages()
    .where(p => p.file.inlinks.length === 0 && p.file.outlinks.length === 0)
    .sort(p => p.file.name);

dv.header(3, "Orphaned Notes");
dv.table(
    ["File", "Created", "Modified"],
    pages.map(p => [
        p.file.link,
        p.file.ctime.toFormat("yyyy-MM-dd"),
        p.file.mtime.toFormat("yyyy-MM-dd")
    ])
);
```
````

#### Component Usage Analytics

````markdown
```dataviewjs
// Analyze component usage across workflows
const workflows = dv.pages('"02-projects"')
    .where(p => p.components != null);

const componentCounts = {};

for (const workflow of workflows) {
    for (const component of workflow.components) {
        componentCounts[component] = (componentCounts[component] || 0) + 1;
    }
}

const sorted = Object.entries(componentCounts)
    .sort((a, b) => b[1] - a[1]);

dv.header(3, "Most Used Components");
dv.table(
    ["Component", "Usage Count"],
    sorted.map(([comp, count]) => [comp, count])
);
```
````

### 3.3 PKB Integration Helper

```python
cat > pkb_integration/dataview_helper.py << 'EOF'
#!/usr/bin/env python3
"""
Dataview Integration Helper
Generate Dataview queries programmatically
"""

from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime, timedelta

class DataviewQueryBuilder:
    """Build Dataview queries programmatically."""
    
    @staticmethod
    def recent_outputs(
        days: int = 7,
        project: str = None
    ) -> str:
        """Generate query for recent workflow outputs."""
        
        from_clause = f'"{project}"' if project else '"02-projects"'
        
        return f"""```dataview
TABLE 
  file.ctime as Created,
  workflow_name as Workflow,
  tags
FROM {from_clause}
WHERE contains(tags, "workflow-output")
AND file.ctime >= date(today) - dur({days} days)
SORT file.ctime DESC
```"""
    
    @staticmethod
    def component_status(status: str = None) -> str:
        """Generate query for components by status."""
        
        where_clause = f'WHERE status = "{status}"' if status else ""
        
        return f"""```dataview
TABLE
  type as Type,
  version as Version,
  context_budget as "Tokens",
  file.mtime as "Last Modified"
FROM "04-resources/components"
{where_clause}
SORT type ASC, version DESC
```"""
    
    @staticmethod
    def workflow_dashboard() -> str:
        """Generate comprehensive workflow dashboard."""
        
        return """```dataview
TABLE
  status as Status,
  steps as "Step Count",
  duration as Duration,
  file.mtime as "Last Run"
FROM "02-projects"
WHERE workflow_name != null
SORT file.mtime DESC
LIMIT 20
```"""
    
    def create_dashboard_note(self, vault_path: Path):
        """Create a dashboard note with Dataview queries."""
        
        dashboard_path = vault_path / "00-meta/dashboards/workflow-dashboard.md"
        dashboard_path.parent.mkdir(parents=True, exist_ok=True)
        
        content = f"""---
tags: [dashboard, workflows, meta]
created: {datetime.now().isoformat()}
---

# Workflow Dashboard

## Recent Executions

{self.workflow_dashboard()}

## Components by Status

### Published
{self.component_status('published')}

### In Review
{self.component_status('review')}

### Deprecated
{self.component_status('deprecated')}

## Recent Outputs (Last 7 Days)

{self.recent_outputs(days=7)}
"""
        
        dashboard_path.write_text(content)
        print(f"✓ Dashboard created: {dashboard_path}")

if __name__ == "__main__":
    import os
    vault = Path(os.getenv("VAULT_PATH", "~/PKB-System/vault")).expanduser()
    
    builder = DataviewQueryBuilder()
    builder.create_dashboard_note(vault)
EOF

python pkb_integration/dataview_helper.py
```

---

## 4. Templater Automation

### 4.1 Template Creation

Templater enables dynamic note creation with code execution.

#### Workflow Output Template

```bash
cd ~/PKB-System/vault/00-meta/templates

cat > workflow-output-template.md << 'EOF'
---
tags: [workflow-output, <% tp.file.cursor(1) %>]
created: 2025-12-27 18:46
workflow_name: <% tp.file.cursor(2) %>
status: complete
duration: <% tp.file.cursor(3) %>
---

# TIER-4-DOCUMENTATION-PLAN

**Workflow**: <% tp.file.cursor(4) %>  
**Executed**: 2025-12-27 16:53  
**Duration**: <% tp.file.cursor(5) %> seconds

## Input

<% tp.file.cursor(6) %>

## Output

<% tp.file.cursor(7) %>

## Components Used

<% tp.file.cursor(8) %>

## Metadata

- **LLM Provider**: <% tp.file.cursor(9) %>
- **Model**: <% tp.file.cursor(10) %>
- **Total Tokens**: <% tp.file.cursor(11) %>

## Related Notes

<% tp.file.cursor(12) %>

---

*Generated by SPES workflow system*
EOF
```

#### Component Template

```markdown
---
tags: [component, <% tp.file.cursor(1) %>]
created: 2025-12-27 18:46
title: <% tp.file.cursor(2) %>
type: <% tp.file.cursor(3) %>
version: 1.0.0
status: draft
context_budget: <% tp.file.cursor(4) %>
---

# TIER-4-DOCUMENTATION-PLAN

<% tp.file.cursor(5) %>

## Usage Notes

<% tp.file.cursor(6) %>

## Examples

<% tp.file.cursor(7) %>
```

### 4.2 Python-Templater Integration

```python
cat > pkb_integration/templater_integration.py << 'EOF'
#!/usr/bin/env python3
"""
Templater Integration
Create notes from workflows using templates
"""

import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

class NoteCreator:
    """Create Obsidian notes from workflow results."""
    
    def __init__(self, vault_path: Path):
        self.vault = vault_path
        self.templates = vault_path / "00-meta/templates"
    
    def create_workflow_output_note(
        self,
        workflow_name: str,
        input_data: str,
        output_data: str,
        metadata: Dict[str, Any]
    ) -> Path:
        """
        Create a note from workflow output.
        
        Args:
            workflow_name: Name of workflow
            input_data: Input to workflow
            output_data: Output from workflow
            metadata: Additional metadata
            
        Returns:
            Path to created note
        """
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{timestamp}-{workflow_name.lower().replace(' ', '-')}.md"
        
        # Determine output location
        if metadata.get('project'):
            output_dir = self.vault / f"02-projects/{metadata['project']}/outputs"
        else:
            output_dir = self.vault / "01-fleeting"
        
        output_dir.mkdir(parents=True, exist_ok=True)
        note_path = output_dir / filename
        
        # Build content
        content = f"""---
tags: [workflow-output, {metadata.get('tags', 'auto-generated')}]
created: {datetime.now().isoformat()}
workflow_name: {workflow_name}
status: complete
duration: {metadata.get('duration', 'unknown')}
---

# {workflow_name} Output

**Workflow**: {workflow_name}  
**Executed**: {datetime.now().strftime("%Y-%m-%d %H:%M")}  
**Duration**: {metadata.get('duration', 'unknown')}

## Input

{input_data}

## Output

{output_data}

## Components Used

{self._format_components(metadata.get('components', []))}

## Metadata

- **LLM Provider**: {metadata.get('llm_provider', 'unknown')}
- **Model**: {metadata.get('model', 'unknown')}
- **Total Tokens**: {metadata.get('total_tokens', 'unknown')}

## Related Notes

{self._format_related(metadata.get('related_notes', []))}

---

*Generated by SPES workflow system*
"""
        
        # Write note
        note_path.write_text(content)
        print(f"✓ Created note: {note_path.relative_to(self.vault)}")
        
        return note_path
    
    def _format_components(self, components: list) -> str:
        """Format component list."""
        if not components:
            return "- None"
        
        return "\n".join(f"- `{comp}`" for comp in components)
    
    def _format_related(self, related: list) -> str:
        """Format related notes as wiki-links."""
        if not related:
            return "- None"
        
        return "\n".join(f"- [[{note}]]" for note in related)
    
    def create_component_note(
        self,
        component_name: str,
        component_type: str,
        content: str,
        metadata: Dict[str, Any]
    ) -> Path:
        """Create a component note."""
        
        filename = f"{component_name}-v{metadata.get('version', '1.0.0')}.md"
        component_dir = self.vault / f"04-resources/components/{component_type}s"
        component_dir.mkdir(parents=True, exist_ok=True)
        
        note_path = component_dir / filename
        
        # Build content with frontmatter
        frontmatter = {
            'tags': [f'component', component_type],
            'created': datetime.now().isoformat(),
            'title': component_name,
            'type': component_type,
            'version': metadata.get('version', '1.0.0'),
            'status': metadata.get('status', 'draft'),
            'context_budget': metadata.get('context_budget', 400)
        }
        
        # Convert to YAML
        import yaml
        yaml_content = yaml.dump(frontmatter, default_flow_style=False)
        
        full_content = f"""---
{yaml_content}---

{content}
"""
        
        note_path.write_text(full_content)
        print(f"✓ Created component: {note_path.relative_to(self.vault)}")
        
        return note_path

# Example usage
if __name__ == "__main__":
    vault = Path(os.getenv("VAULT_PATH", "~/PKB-System/vault")).expanduser()
    
    creator = NoteCreator(vault)
    
    # Create example workflow output note
    note_path = creator.create_workflow_output_note(
        workflow_name="Code Generation",
        input_data="Generate a function to validate email addresses",
        output_data="""```python
import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```""",
        metadata={
            'duration': 3.2,
            'llm_provider': 'claude',
            'model': 'claude-sonnet-4-20250514',
            'total_tokens': 856,
            'components': [
                'persona-python-expert-v1.0.0',
                'instruction-code-generation-v2.0.0'
            ],
            'tags': 'python, code-generation'
        }
    )
    
    print(f"\n✓ Note created at: {note_path}")
EOF

python pkb_integration/templater_integration.py
```

---

## 5. Meta Bind Interactive Elements

### 5.1 Interactive Workflow Dashboard

Meta Bind enables interactive elements in notes.

```markdown
---
tags: [dashboard, interactive]
---

# Workflow Control Dashboard

## Quick Actions

`BUTTON[Run Daily Summary]`
```js
// Run daily summary workflow
const workflow = app.plugins.plugins['templater-obsidian'].templater;
workflow.create_new_note_from_template(
    "templates/daily-summary-workflow",
    "01-fleeting"
);
```

`BUTTON[Generate Component]`
```js
// Create new component from template
const workflow = app.plugins.plugins['templater-obsidian'].templater;
workflow.create_new_note_from_template(
    "templates/component-template",
    "04-resources/components"
);
```

## Workflow Status

`VIEW[{workflow_status}]`

## Recent Outputs

```dataview
LIST
FROM "02-projects"
WHERE contains(tags, "workflow-output")
SORT file.ctime DESC
LIMIT 5
```

## Statistics

**Total Workflows**: `VIEW[{total_workflows}]`  
**Successful**: `VIEW[{successful_workflows}]`  
**Failed**: `VIEW[{failed_workflows}]`  
**Success Rate**: `VIEW[{success_rate}]`%
```

### 5.2 Component Editor

```markdown
---
tags: [component, editor]
---

# Component Editor

## Basic Information

**Title**: `INPUT[text:component_title]`  
**Type**: `INPUT[select(option(instruction), option(persona), option(format), option(constraint)):component_type]`  
**Version**: `INPUT[text:component_version]{defaultValue: 1.0.0}`  
**Status**: `INPUT[select(option(draft), option(review), option(published)):component_status]`

## Content

**Description**: `INPUT[textArea:component_description]`

**Token Budget**: `INPUT[number:context_budget]{defaultValue: 400}`

## Actions

`BUTTON[Save Component]`
```js
// Save component with metadata
const title = this.component_title;
const type = this.component_type;
const version = this.component_version;
const status = this.component_status;

// Create note with frontmatter
// ... implementation
```

`BUTTON[Test Component]`
```js
// Test component with LLM
// ... implementation
```
```

### 5.3 Python Integration with Meta Bind

```python
cat > pkb_integration/metabind_integration.py << 'EOF'
#!/usr/bin/env python3
"""
Meta Bind Integration
Update interactive elements from Python
"""

import re
from pathlib import Path
from typing import Dict, Any

class MetaBindUpdater:
    """Update Meta Bind values in notes."""
    
    @staticmethod
    def update_view_value(
        note_path: Path,
        view_name: str,
        new_value: Any
    ):
        """Update a VIEW element's value."""
        
        content = note_path.read_text()
        
        # Pattern: `VIEW[{view_name}]`
        pattern = f"`VIEW\\[{{{{\\{view_name}\\}}}}\\]`"
        replacement = f"`VIEW[{{{{{view_name}}}}}]`"
        
        # Update the bound value in frontmatter
        # Meta Bind stores values in frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                body = parts[2]
                
                # Update or add value
                if f'{view_name}:' in frontmatter:
                    frontmatter = re.sub(
                        f'{view_name}:.*',
                        f'{view_name}: {new_value}',
                        frontmatter
                    )
                else:
                    frontmatter += f'\n{view_name}: {new_value}'
                
                # Reconstruct content
                updated = f"---{frontmatter}---{body}"
                note_path.write_text(updated)
                
                print(f"✓ Updated {view_name} = {new_value}")
    
    @staticmethod
    def update_dashboard_stats(
        dashboard_path: Path,
        stats: Dict[str, Any]
    ):
        """Update workflow dashboard statistics."""
        
        for key, value in stats.items():
            MetaBindUpdater.update_view_value(
                dashboard_path,
                key,
                value
            )

# Example usage
if __name__ == "__main__":
    import os
    vault = Path(os.getenv("VAULT_PATH", "~/PKB-System/vault")).expanduser()
    
    dashboard = vault / "00-meta/dashboards/workflow-dashboard.md"
    
    # Update statistics
    stats = {
        'total_workflows': 45,
        'successful_workflows': 42,
        'failed_workflows': 3,
        'success_rate': 93.3,
        'workflow_status': 'Running'
    }
    
    updater = MetaBindUpdater()
    updater.update_dashboard_stats(dashboard, stats)
EOF
```

---

## 6. Workflow-to-PKB Pipelines

### 6.1 Complete Integration Pipeline

```python
cat > pkb_integration/workflow_pkb_pipeline.py << 'EOF'
#!/usr/bin/env python3
"""
Complete Workflow-to-PKB Pipeline
Capture, process, and store workflow results in PKB
"""

import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List
from dotenv import load_dotenv
from anthropic import Anthropic

# Import integration modules
from smart_search import SmartSearch
from templater_integration import NoteCreator
from metabind_integration import MetaBindUpdater

load_dotenv()

class WorkflowPKBPipeline:
    """Complete pipeline integrating SPES workflows with Obsidian PKB."""
    
    def __init__(self, vault_path: Path):
        self.vault = vault_path
        self.searcher = SmartSearch(vault_path)
        self.note_creator = NoteCreator(vault_path)
        self.metabind = MetaBindUpdater()
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    def execute_workflow_with_pkb(
        self,
        workflow_name: str,
        user_input: str,
        components: List[str],
        project: str = None,
        use_context: bool = True
    ) -> Dict[str, Any]:
        """
        Execute workflow with full PKB integration.
        
        Pipeline:
        1. Search PKB for relevant context
        2. Compose prompt with context + components
        3. Execute with LLM
        4. Create output note in PKB
        5. Update dashboards
        6. Generate backlinks
        
        Returns:
            Complete execution result with metadata
        """
        
        print(f"\n{'='*60}")
        print(f"WORKFLOW: {workflow_name}")
        print(f"{'='*60}\n")
        
        start_time = datetime.now()
        
        # Step 1: Retrieve context from PKB
        context_notes = []
        if use_context:
            print("📚 Step 1: Retrieving context from PKB...")
            context_notes = self.searcher.search(
                user_input,
                limit=3,
                min_similarity=0.6
            )
            
            if context_notes:
                print(f"  ✓ Found {len(context_notes)} relevant notes")
            else:
                print("  ℹ No relevant context found")
        else:
            print("📚 Step 1: Skipping context retrieval")
        
        # Step 2: Load components
        print("\n🧩 Step 2: Loading components...")
        component_content = []
        for comp in components:
            comp_path = self._find_component(comp)
            if comp_path:
                content = comp_path.read_text()
                # Remove frontmatter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        content = parts[2].strip()
                component_content.append(content)
                print(f"  ✓ Loaded: {comp}")
            else:
                print(f"  ⚠ Not found: {comp}")
        
        # Step 3: Compose prompt
        print("\n✏️ Step 3: Composing prompt...")
        prompt = self._compose_prompt(
            user_input,
            component_content,
            context_notes
        )
        print(f"  ✓ Prompt ready ({len(prompt)} chars)")
        
        # Step 4: Execute with LLM
        print("\n🤖 Step 4: Executing with LLM...")
        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}]
        )
        
        output = response.content[0].text
        print(f"  ✓ Response received ({len(output)} chars)")
        
        # Calculate duration
        duration = (datetime.now() - start_time).total_seconds()
        
        # Step 5: Create output note
        print("\n📝 Step 5: Creating output note in PKB...")
        metadata = {
            'project': project,
            'duration': duration,
            'llm_provider': 'claude',
            'model': 'claude-sonnet-4-20250514',
            'total_tokens': response.usage.input_tokens + response.usage.output_tokens,
            'components': components,
            'tags': self._extract_tags(workflow_name),
            'related_notes': [n['path'] for n in context_notes]
        }
        
        note_path = self.note_creator.create_workflow_output_note(
            workflow_name=workflow_name,
            input_data=user_input,
            output_data=output,
            metadata=metadata
        )
        
        # Step 6: Update dashboards
        print("\n📊 Step 6: Updating dashboards...")
        self._update_dashboard_stats()
        print("  ✓ Dashboard updated")
        
        # Step 7: Generate backlinks
        print("\n🔗 Step 7: Generating backlinks...")
        self._create_backlinks(note_path, context_notes)
        print("  ✓ Backlinks created")
        
        print(f"\n{'='*60}")
        print(f"✓ WORKFLOW COMPLETE ({duration:.2f}s)")
        print(f"{'='*60}\n")
        
        return {
            'success': True,
            'output': output,
            'note_path': str(note_path.relative_to(self.vault)),
            'duration': duration,
            'tokens': metadata['total_tokens'],
            'context_used': len(context_notes)
        }
    
    def _find_component(self, component_name: str) -> Path:
        """Find component file in vault."""
        
        # Search in component directories
        for subdir in ['instructions', 'personas', 'formats', 'constraints']:
            comp_dir = self.vault / f"04-resources/components/{subdir}"
            if comp_dir.exists():
                for comp_file in comp_dir.glob(f"{component_name}*"):
                    return comp_file
        
        return None
    
    def _compose_prompt(
        self,
        user_input: str,
        components: List[str],
        context_notes: List[Dict]
    ) -> str:
        """Compose complete prompt."""
        
        sections = []
        
        # Add context if available
        if context_notes:
            context_section = "# Relevant Context from Knowledge Base\n\n"
            for note in context_notes:
                content = Path(note['full_path']).read_text(
                    encoding='utf-8',
                    errors='ignore'
                )
                # Remove frontmatter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        content = parts[2].strip()
                
                context_section += f"## {note['path']}\n\n{content}\n\n---\n\n"
            
            sections.append(context_section)
        
        # Add components
        sections.extend(components)
        
        # Add user input
        sections.append(f"# User Request\n\n{user_input}")
        
        return "\n\n".join(sections)
    
    def _extract_tags(self, workflow_name: str) -> str:
        """Extract tags from workflow name."""
        # Simple tag extraction from workflow name
        tags = workflow_name.lower().replace(' ', '-')
        return f"workflow, {tags}"
    
    def _update_dashboard_stats(self):
        """Update workflow dashboard statistics."""
        
        dashboard = self.vault / "00-meta/dashboards/workflow-dashboard.md"
        
        if not dashboard.exists():
            return
        
        # Count workflow outputs
        outputs = list(self.vault.rglob("*.md"))
        workflow_outputs = [
            p for p in outputs
            if 'workflow-output' in p.read_text(errors='ignore')
        ]
        
        stats = {
            'total_workflows': len(workflow_outputs),
            'workflow_status': 'Active',
            'last_update': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        self.metabind.update_dashboard_stats(dashboard, stats)
    
    def _create_backlinks(self, note_path: Path, context_notes: List[Dict]):
        """Create bidirectional links between output and context."""
        
        if not context_notes:
            return
        
        # Add links to output note (already done in template)
        
        # Add backlink from context notes to output
        output_link = f"[[{note_path.stem}]]"
        
        for context in context_notes:
            context_path = Path(context['full_path'])
            content = context_path.read_text(encoding='utf-8', errors='ignore')
            
            # Add backlink section if not exists
            if "## Backlinks" not in content:
                content += f"\n\n## Backlinks\n\n- {output_link}\n"
            else:
                # Append to existing backlinks
                content += f"- {output_link}\n"
            
            context_path.write_text(content, encoding='utf-8')

# Example usage
def main():
    vault = Path(os.getenv("VAULT_PATH", "~/PKB-System/vault")).expanduser()
    
    pipeline = WorkflowPKBPipeline(vault)
    
    # Execute workflow with full PKB integration
    result = pipeline.execute_workflow_with_pkb(
        workflow_name="Python Code Generation",
        user_input="Create a function to parse and validate JSON config files",
        components=[
            "persona-python-expert-v1.0.0.md",
            "instruction-code-generation-v2.0.0.md",
            "constraint-secure-code-v2.0.0.md"
        ],
        project="config-parser",
        use_context=True
    )
    
    print("\nResult Summary:")
    print(f"  Success: {result['success']}")
    print(f"  Note: {result['note_path']}")
    print(f"  Duration: {result['duration']:.2f}s")
    print(f"  Tokens: {result['tokens']}")
    print(f"  Context Notes: {result['context_used']}")

if __name__ == "__main__":
    main()
EOF
```

---

## 7. Knowledge Graph Construction

### 7.1 Automatic Link Generation

```python
cat > pkb_integration/knowledge_graph.py << 'EOF'
#!/usr/bin/env python3
"""
Knowledge Graph Construction
Automatically generate bidirectional links between related notes
"""

from pathlib import Path
from typing import List, Dict, Set, Tuple
import re
from smart_search import SmartSearch

class KnowledgeGraphBuilder:
    """Build knowledge graph through automated linking."""
    
    def __init__(self, vault_path: Path):
        self.vault = vault_path
        self.searcher = SmartSearch(vault_path)
    
    def suggest_links(
        self,
        note_path: Path,
        min_similarity: float = 0.7,
        max_suggestions: int = 5
    ) -> List[Dict]:
        """
        Suggest links for a note based on semantic similarity.
        
        Returns list of suggestions with similarity scores.
        """
        
        # Get note content
        content = note_path.read_text(encoding='utf-8', errors='ignore')
        
        # Find similar notes
        similar = self.searcher.search(
            content,
            limit=max_suggestions + 1,  # +1 to exclude self
            min_similarity=min_similarity
        )
        
        # Exclude the note itself
        suggestions = [
            s for s in similar
            if Path(s['full_path']) != note_path
        ]
        
        return suggestions[:max_suggestions]
    
    def extract_topics(self, note_path: Path) -> Set[str]:
        """Extract main topics/concepts from note."""
        
        content = note_path.read_text(encoding='utf-8', errors='ignore')
        
        # Remove frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2]
        
        # Extract headings as topics
        headings = re.findall(r'^#{1,3}\s+(.+)$', content, re.MULTILINE)
        
        # Extract wiki-links as topics
        wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
        
        # Extract tags as topics
        tags = re.findall(r'#([\w-]+)', content)
        
        # Combine and clean
        topics = set()
        for topic in headings + wikilinks + tags:
            cleaned = topic.strip().lower()
            if len(cleaned) > 2:  # Skip very short
                topics.add(cleaned)
        
        return topics
    
    def find_orphaned_notes(self) -> List[Path]:
        """Find notes with no links (orphans)."""
        
        orphans = []
        
        for note_path in self.vault.rglob("*.md"):
            # Skip special directories
            if any(skip in str(note_path) for skip in [".obsidian", "00-meta/templates"]):
                continue
            
            content = note_path.read_text(encoding='utf-8', errors='ignore')
            
            # Check for any wiki-links
            has_links = bool(re.search(r'\[\[.+\]\]', content))
            
            if not has_links:
                orphans.append(note_path)
        
        return orphans
    
    def create_topic_moc(self, topic: str) -> Path:
        """
        Create a Map of Content (MOC) for a topic.
        
        Aggregates all notes related to a topic.
        """
        
        # Search for notes about topic
        related = self.searcher.search(topic, limit=20, min_similarity=0.6)
        
        if not related:
            print(f"No notes found for topic: {topic}")
            return None
        
        # Create MOC note
        moc_dir = self.vault / "00-meta/indexes"
        moc_dir.mkdir(parents=True, exist_ok=True)
        
        moc_path = moc_dir / f"moc-{topic.lower().replace(' ', '-')}.md"
        
        # Build content
        content = f"""---
tags: [moc, {topic.lower().replace(' ', '-')}]
created: {datetime.now().isoformat()}
topic: {topic}
---

# {topic} - Map of Content

## Overview

This is a Map of Content (MOC) for **{topic}**, aggregating all related notes.

## Related Notes ({len(related)})

"""
        
        # Group by similarity
        high_relevance = [n for n in related if n['similarity'] > 0.8]
        medium_relevance = [n for n in related if 0.7 < n['similarity'] <= 0.8]
        related_content = [n for n in related if n['similarity'] <= 0.7]
        
        if high_relevance:
            content += "### High Relevance\n\n"
            for note in high_relevance:
                content += f"- [[{note['path']}]] (similarity: {note['similarity']:.2f})\n"
            content += "\n"
        
        if medium_relevance:
            content += "### Medium Relevance\n\n"
            for note in medium_relevance:
                content += f"- [[{note['path']}]] (similarity: {note['similarity']:.2f})\n"
            content += "\n"
        
        if related_content:
            content += "### Related Content\n\n"
            for note in related_content:
                content += f"- [[{note['path']}]] (similarity: {note['similarity']:.2f})\n"
        
        content += "\n---\n\n*Auto-generated by SPES Knowledge Graph Builder*\n"
        
        moc_path.write_text(content)
        print(f"✓ Created MOC: {moc_path.relative_to(self.vault)}")
        
        return moc_path
    
    def auto_link_orphans(self, dry_run: bool = True):
        """Automatically suggest links for orphaned notes."""
        
        orphans = self.find_orphaned_notes()
        
        print(f"Found {len(orphans)} orphaned notes\n")
        
        for orphan in orphans:
            print(f"\n{orphan.relative_to(self.vault)}:")
            
            suggestions = self.suggest_links(orphan, min_similarity=0.7, max_suggestions=3)
            
            if not suggestions:
                print("  No suggestions")
                continue
            
            print("  Suggested links:")
            for sugg in suggestions:
                print(f"    - [[{sugg['path']}]] (similarity: {sugg['similarity']:.2f})")
            
            if not dry_run:
                # Add links to note
                content = orphan.read_text(encoding='utf-8', errors='ignore')
                
                # Add suggested links section
                links_section = "\n\n## Suggested Links\n\n"
                for sugg in suggestions:
                    links_section += f"- [[{sugg['path']}]]\n"
                
                content += links_section
                orphan.write_text(content, encoding='utf-8')
                print("    ✓ Links added")

if __name__ == "__main__":
    import os
    from datetime import datetime
    
    vault = Path(os.getenv("VAULT_PATH", "~/PKB-System/vault")).expanduser()
    
    builder = KnowledgeGraphBuilder(vault)
    
    # Find orphans and suggest links
    print("="*60)
    print("KNOWLEDGE GRAPH BUILDER")
    print("="*60)
    
    builder.auto_link_orphans(dry_run=True)
    
    # Create MOC for a topic
    print("\n" + "="*60)
    print("CREATING MAP OF CONTENT")
    print("="*60)
    
    builder.create_topic_moc("prompt engineering")
EOF
```

---

## 8. Memory Systems

### 8.1 SPES Memory Architecture

SPES maintains memory in `.claude/` directory:

```
.claude/
├── core/
│   ├── user_preferences.json
│   ├── component_usage.json
│   └── llm_settings.json
├── sessions/
│   └── YYYY-MM-DD/
│       └── session_HHMMSS.json
├── decisions/
│   └── ADR-NNNN.md
└── patterns/
    └── learned_patterns.json
```

### 8.2 Memory Integration

```python
cat > pkb_integration/memory_system.py << 'EOF'
#!/usr/bin/env python3
"""
SPES Memory System
Persistent memory across sessions
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List

class SPESMemory:
    """Persistent memory system for SPES."""
    
    def __init__(self, vault_path: Path):
        self.vault = vault_path
        self.memory_dir = vault_path.parent / ".claude"
        self._ensure_structure()
    
    def _ensure_structure(self):
        """Ensure memory directory structure exists."""
        (self.memory_dir / "core").mkdir(parents=True, exist_ok=True)
        (self.memory_dir / "sessions").mkdir(parents=True, exist_ok=True)
        (self.memory_dir / "decisions").mkdir(parents=True, exist_ok=True)
        (self.memory_dir / "patterns").mkdir(parents=True, exist_ok=True)
    
    def record_session(
        self,
        workflow_name: str,
        input_data: str,
        output_data: str,
        metadata: Dict[str, Any]
    ):
        """Record a workflow session."""
        
        # Create session directory for today
        today = datetime.now().strftime("%Y-%m-%d")
        session_dir = self.memory_dir / "sessions" / today
        session_dir.mkdir(parents=True, exist_ok=True)
        
        # Session filename
        timestamp = datetime.now().strftime("%H%M%S")
        session_file = session_dir / f"session_{timestamp}.json"
        
        # Build session record
        session = {
            'timestamp': datetime.now().isoformat(),
            'workflow_name': workflow_name,
            'input': input_data,
            'output': output_data,
            'metadata': metadata
        }
        
        # Save
        with open(session_file, 'w') as f:
            json.dump(session, f, indent=2)
        
        print(f"✓ Session recorded: {session_file.relative_to(self.memory_dir)}")
    
    def track_component_usage(self, component: str):
        """Track component usage statistics."""
        
        usage_file = self.memory_dir / "core" / "component_usage.json"
        
        # Load existing
        if usage_file.exists():
            with open(usage_file, 'r') as f:
                usage = json.load(f)
        else:
            usage = {}
        
        # Increment count
        usage[component] = usage.get(component, 0) + 1
        
        # Save
        with open(usage_file, 'w') as f:
            json.dump(usage, f, indent=2)
    
    def get_popular_components(self, limit: int = 10) -> List[tuple]:
        """Get most-used components."""
        
        usage_file = self.memory_dir / "core" / "component_usage.json"
        
        if not usage_file.exists():
            return []
        
        with open(usage_file, 'r') as f:
            usage = json.load(f)
        
        # Sort by usage count
        sorted_components = sorted(
            usage.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        return sorted_components[:limit]
    
    def save_user_preference(self, key: str, value: Any):
        """Save a user preference."""
        
        prefs_file = self.memory_dir / "core" / "user_preferences.json"
        
        # Load existing
        if prefs_file.exists():
            with open(prefs_file, 'r') as f:
                prefs = json.load(f)
        else:
            prefs = {}
        
        # Update
        prefs[key] = value
        
        # Save
        with open(prefs_file, 'w') as f:
            json.dump(prefs, f, indent=2)
        
        print(f"✓ Saved preference: {key} = {value}")
    
    def get_user_preference(self, key: str, default: Any = None) -> Any:
        """Get a user preference."""
        
        prefs_file = self.memory_dir / "core" / "user_preferences.json"
        
        if not prefs_file.exists():
            return default
        
        with open(prefs_file, 'r') as f:
            prefs = json.load(f)
        
        return prefs.get(key, default)
    
    def learn_pattern(
        self,
        pattern_name: str,
        description: str,
        examples: List[str]
    ):
        """Record a learned pattern."""
        
        patterns_file = self.memory_dir / "patterns" / "learned_patterns.json"
        
        # Load existing
        if patterns_file.exists():
            with open(patterns_file, 'r') as f:
                patterns = json.load(f)
        else:
            patterns = {}
        
        # Add pattern
        patterns[pattern_name] = {
            'description': description,
            'examples': examples,
            'learned_at': datetime.now().isoformat()
        }
        
        # Save
        with open(patterns_file, 'w') as f:
            json.dump(patterns, f, indent=2)
        
        print(f"✓ Learned pattern: {pattern_name}")

# Example usage
if __name__ == "__main__":
    import os
    
    vault = Path(os.getenv("VAULT_PATH", "~/PKB-System/vault")).expanduser()
    
    memory = SPESMemory(vault)
    
    # Record session
    memory.record_session(
        workflow_name="Code Generation",
        input_data="Generate email validator",
        output_data="def validate_email...",
        metadata={'duration': 3.2, 'tokens': 856}
    )
    
    # Track component usage
    memory.track_component_usage("persona-python-expert-v1.0.0")
    memory.track_component_usage("instruction-code-generation-v2.0.0")
    
    # Get popular components
    popular = memory.get_popular_components(5)
    print("\nMost Used Components:")
    for comp, count in popular:
        print(f"  {comp}: {count} uses")
    
    # Save preference
    memory.save_user_preference("default_llm", "claude")
    memory.save_user_preference("prefer_local", False)
    
    # Learn pattern
    memory.learn_pattern(
        pattern_name="code_with_tests",
        description="Always generate tests alongside code",
        examples=[
            "instruction-code-generation + instruction-create-tests",
            "persona-python-expert + format-code-with-tests"
        ]
    )
EOF

python pkb_integration/memory_system.py
```

---

## 9. Advanced Integration Patterns

### 9.1 Bidirectional Sync

```python
cat > pkb_integration/bidirectional_sync.py << 'EOF'
#!/usr/bin/env python3
"""
Bidirectional Sync
Keep SPES components and PKB notes synchronized
"""

import os
from pathlib import Path
import shutil
from datetime import datetime
from typing import Set

class BidirectionalSync:
    """Sync between SPES components and PKB notes."""
    
    def __init__(self, spes_path: Path, vault_path: Path):
        self.spes = spes_path
        self.vault = vault_path
        self.sync_log = vault_path.parent / ".claude/sync_log.txt"
    
    def sync_components_to_vault(self):
        """Sync SPES components to vault resources."""
        
        spes_components = self.spes / "components/core"
        vault_components = self.vault / "04-resources/components"
        
        synced = 0
        
        for component_type in ['instructions', 'personas', 'formats', 'constraints']:
            spes_dir = spes_components / component_type
            vault_dir = vault_components / component_type
            
            if not spes_dir.exists():
                continue
            
            vault_dir.mkdir(parents=True, exist_ok=True)
            
            for component_file in spes_dir.glob("*.md"):
                vault_file = vault_dir / component_file.name
                
                # Check if needs update
                if not vault_file.exists() or \
                   component_file.stat().st_mtime > vault_file.stat().st_mtime:
                    
                    shutil.copy2(component_file, vault_file)
                    synced += 1
                    self._log(f"Synced: {component_file.name}")
        
        print(f"✓ Synced {synced} components to vault")
    
    def sync_vault_to_components(self):
        """Sync vault resources back to SPES components."""
        
        vault_components = self.vault / "04-resources/components"
        spes_components = self.spes / "components/core"
        
        synced = 0
        
        for component_type in ['instructions', 'personas', 'formats', 'constraints']:
            vault_dir = vault_components / component_type
            spes_dir = spes_components / component_type
            
            if not vault_dir.exists():
                continue
            
            spes_dir.mkdir(parents=True, exist_ok=True)
            
            for component_file in vault_dir.glob("*.md"):
                spes_file = spes_dir / component_file.name
                
                # Check if needs update
                if not spes_file.exists() or \
                   component_file.stat().st_mtime > spes_file.stat().st_mtime:
                    
                    shutil.copy2(component_file, spes_file)
                    synced += 1
                    self._log(f"Synced: {component_file.name}")
        
        print(f"✓ Synced {synced} components to SPES")
    
    def _log(self, message: str):
        """Log sync operation."""
        timestamp = datetime.now().isoformat()
        with open(self.sync_log, 'a') as f:
            f.write(f"[{timestamp}] {message}\n")

if __name__ == "__main__":
    spes = Path("~/PKB-System/spes").expanduser()
    vault = Path(os.getenv("VAULT_PATH", "~/PKB-System/vault")).expanduser()
    
    sync = BidirectionalSync(spes, vault)
    
    print("Bidirectional Sync")
    print("="*60)
    
    # Sync both ways
    sync.sync_components_to_vault()
    sync.sync_vault_to_components()
    
    print("\n✓ Sync complete")
EOF
```

---

## 10. Production Examples

### 10.1 Complete Integrated Workflow

This example demonstrates the full power of PKB integration:

```python
cat > pkb_integration/production_example.py << 'EOF'
#!/usr/bin/env python3
"""
Production Example: Research → Analysis → Documentation
Complete workflow with full PKB integration
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from workflow_pkb_pipeline import WorkflowPKBPipeline

load_dotenv()

def research_and_document_workflow():
    """
    Complete research and documentation workflow:
    1. Research topic using PKB context
    2. Analyze findings
    3. Generate documentation
    4. Create knowledge graph connections
    """
    
    vault = Path(os.getenv("VAULT_PATH", "~/PKB-System/vault")).expanduser()
    pipeline = WorkflowPKBPipeline(vault)
    
    print("\n" + "="*60)
    print("PRODUCTION WORKFLOW: Research & Documentation")
    print("="*60 + "\n")
    
    # Step 1: Research
    print("PHASE 1: RESEARCH\n")
    
    research_result = pipeline.execute_workflow_with_pkb(
        workflow_name="Topic Research",
        user_input="""
        Research best practices for implementing rate limiting in REST APIs.
        Include: algorithms, implementation strategies, and common pitfalls.
        """,
        components=[
            "persona-technical-writer-v1.0.0.md",
            "instruction-research-v1.0.0.md"
        ],
        project="api-best-practices",
        use_context=True
    )
    
    # Step 2: Analysis
    print("\nPHASE 2: ANALYSIS\n")
    
    analysis_result = pipeline.execute_workflow_with_pkb(
        workflow_name="Technical Analysis",
        user_input=f"""
        Analyze these research findings and identify:
        1. Most important recommendations
        2. Implementation complexity
        3. Trade-offs
        
        Research findings:
        {research_result['output']}
        """,
        components=[
            "persona-senior-developer-v1.0.0.md",
            "instruction-analyze-v1.0.0.md"
        ],
        project="api-best-practices",
        use_context=False  # Already have context from research
    )
    
    # Step 3: Documentation
    print("\nPHASE 3: DOCUMENTATION\n")
    
    doc_result = pipeline.execute_workflow_with_pkb(
        workflow_name="API Documentation",
        user_input=f"""
        Create comprehensive documentation for implementing rate limiting.
        
        Based on this analysis:
        {analysis_result['output']}
        
        Include:
        - Overview
        - Implementation guide
        - Code examples
        - Best practices
        - Common pitfalls
        """,
        components=[
            "persona-technical-writer-v1.0.0.md",
            "instruction-create-documentation-v1.0.0.md",
            "format-markdown-document-v1.0.0.md"
        ],
        project="api-best-practices",
        use_context=False
    )
    
    # Summary
    print("\n" + "="*60)
    print("WORKFLOW COMPLETE")
    print("="*60)
    
    print(f"\nGenerated Notes:")
    print(f"  1. Research: {research_result['note_path']}")
    print(f"  2. Analysis: {analysis_result['note_path']}")
    print(f"  3. Documentation: {doc_result['note_path']}")
    
    print(f"\nTotal Duration: {
        research_result['duration'] +
        analysis_result['duration'] +
        doc_result['duration']
    :.2f}s")
    
    print(f"\nTotal Tokens: {
        research_result['tokens'] +
        analysis_result['tokens'] +
        doc_result['tokens']
    :,}")
    
    print("\n✓ All artifacts saved to PKB with bidirectional links")

if __name__ == "__main__":
    research_and_document_workflow()
EOF
```

---

## Conclusion

**You've mastered SPES-PKB integration!** 🎓

**Integration Capabilities Unlocked**:
- ✅ Semantic search across vault
- ✅ Dynamic Dataview queries
- ✅ Templater automation
- ✅ Meta Bind interactive elements
- ✅ Workflow-to-PKB pipelines
- ✅ Knowledge graph construction
- ✅ Persistent memory systems
- ✅ Bidirectional sync
- ✅ Production workflows

**Key Files Created**:
```
pkb_integration/
├── smart_search.py              # Semantic search
├── context_retrieval_workflow.py # Context-enhanced workflows
├── dataview_helper.py           # Query generation
├── templater_integration.py     # Note creation
├── metabind_integration.py      # Interactive updates
├── workflow_pkb_pipeline.py     # Complete pipeline
├── knowledge_graph.py           # Auto-linking
├── memory_system.py             # Persistent memory
├── bidirectional_sync.py        # Component sync
└── production_example.py        # Full example
```

**Time Invested**: ⏱️ 150-180 minutes  
**Ready For**: Production-grade knowledge management with AI workflows

**Next Tier 3 Topics**:
- Testing Frameworks
- Performance Optimization  
- Advanced Workflow Patterns
- Community Contribution

Would you like to continue with another Tier 3 topic?
