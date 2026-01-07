---
title: SPES Semantic Retrieval & MCP Integration
document_type: tier4_advanced
tier: 4
priority: high
version: 1.0.0
status: published
prerequisites: ["Advanced Memory Architecture", "PKB Integration Systems"]
estimated_time: 260-300 minutes
complexity: very_complex
last_updated: 2025-12-27
---

# Semantic Retrieval & MCP Integration for SPES

**Version**: 1.0.0  
**Document Type**: Tier 4 - Advanced Implementation  
**Audience**: System architects, ML engineers, advanced practitioners  
**Time Required**: 260-300 minutes (4.5-5 hours)  
**Goal**: Implement production-grade semantic memory retrieval using Smart Connections and MCP

---

## Table of Contents

1. [Vector Embeddings Fundamentals](#1-vector-embeddings-fundamentals)
2. [Smart Connections Plugin Configuration](#2-smart-connections-plugin-configuration)
3. [Model Context Protocol (MCP) Deep Dive](#3-model-context-protocol-mcp-deep-dive)
4. [Query Anchor System](#4-query-anchor-system)
5. [Hybrid Retrieval Strategies](#5-hybrid-retrieval-strategies)
6. [Integration with Advanced Memory](#6-integration-with-advanced-memory)

---

## Overview

> **The Limitation**: In Document 17, we built a sophisticated three-layer memory architecture. However, retrieval is **structural**, not **semantic**. You must know which file to look in. If you ask "What do we know about authentication?", the system can't automatically find relevant information across all memory files.

> **The Solution**: **Semantic retrieval** using vector embeddings. Every memory file is automatically converted into a mathematical representation (embedding) that captures its meaning. When you query the memory bank, the system finds semantically similar content—even if exact keywords don't match.

### The Semantic Retrieval Architecture

```
Memory File Created/Updated
    ↓
Smart Connections Plugin (Obsidian)
    ↓
Automatic Embedding Generation (local or API)
    ↓
Storage in .smart-env/smart_sources.json
    ↓
MCP Server Exposes Embeddings
    ↓
LLM Queries via MCP Tools (lookup, connection)
    ↓
Semantic Search Returns Relevant Content
```

**Example Query Evolution**:

```
Structural (Document 17):
  "Load task-logs/2025-12-27-1000-jwt-auth.md"
  → Requires knowing exact file name

Semantic (Document 18):
  "What have we learned about authentication security?"
  → Finds ALL relevant content across files
  → Returns: JWT implementation, PKCE patterns, error logs, decisions
```

### Key Technologies

| Technology | Role | Why Essential |
|------------|------|---------------|
| **Vector Embeddings** | Convert text to numerical representation | Enables similarity search |
| **Smart Connections** | Obsidian plugin for auto-embedding | Automatic, transparent to user |
| **MCP (Model Context Protocol)** | Exposes embeddings to LLMs | Standard interface for tools |
| **Hybrid Retrieval** | Combine keyword + semantic | Best of both worlds |

---

## 1. Vector Embeddings Fundamentals

### 1.1 What Are Vector Embeddings?

**Vector embeddings** are numerical representations of text that capture semantic meaning.

**Example**:

```
Text: "The user logs in with username and password"

Embedding: [0.23, -0.45, 0.78, 0.12, ..., -0.34]
            ↑
         384 dimensions (for bge-micro-v2)
```

**Key Property**: Semantically similar texts have similar embeddings.

```python
import numpy as np

# Example embeddings (simplified to 5 dimensions)
text1 = "user authentication with password"
embedding1 = np.array([0.8, 0.2, -0.1, 0.5, 0.3])

text2 = "login system using credentials"  
embedding2 = np.array([0.7, 0.3, -0.2, 0.6, 0.4])  # Similar to text1

text3 = "database query optimization"
embedding3 = np.array([-0.3, 0.9, 0.5, -0.7, 0.1])  # Different from text1

# Cosine similarity (measures semantic closeness)
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print(f"text1 vs text2: {cosine_similarity(embedding1, embedding2):.3f}")  # ~0.98 (very similar)
print(f"text1 vs text3: {cosine_similarity(embedding1, embedding3):.3f}")  # ~0.12 (different)
```

### 1.2 Embedding Model Comparison

**Available embedding models**:

| Model | Dimensions | Speed | Quality | Cost | Use Case |
|-------|------------|-------|---------|------|----------|
| **TaylorAI/bge-micro-v2** | 384 | ⚡⚡⚡ Fast | Good | Free (local) | **Recommended for SPES** |
| **nomic-embed-text** | 768 | ⚡⚡ Medium | Better | Free (local) | Large vaults |
| **text-embedding-3-small** | 1536 | ⚡ Slow (API) | Better | $0.02/1M tokens | Cloud preferred |
| **text-embedding-3-large** | 3072 | 🐌 Very slow | Best | $0.13/1M tokens | Maximum quality |

**Dimension Trade-offs**:

| Dimensions | Storage | Speed | Quality | Best For |
|------------|---------|-------|---------|----------|
| 384 | 1.5 KB/doc | Fast | Good | <10K notes, fast retrieval |
| 768 | 3 KB/doc | Medium | Better | 10K-50K notes |
| 1536 | 6 KB/doc | Slow | Better | 50K-100K notes |
| 3072 | 12 KB/doc | Very slow | Best | >100K notes, maximum precision |

**Recommendation for SPES**: 
- **Start with `bge-micro-v2` (384 dims)** - Free, fast, good quality
- **Upgrade to `nomic-embed-text` (768 dims)** if quality insufficient
- **Use API models** only if local models don't meet needs

### 1.3 How Semantic Search Works

**Step-by-step semantic search process**:

```python
# 1. INDEXING PHASE (happens when memory files are created/updated)

def index_memory_file(file_path: str, embedding_model):
    """Generate and store embedding for memory file."""
    
    # Read file content
    content = read_file(file_path)
    
    # Generate embedding
    embedding = embedding_model.encode(content)
    # → [0.23, -0.45, 0.78, ..., -0.34]  (384 numbers)
    
    # Store in index
    index.add(file_path, embedding)


# 2. QUERY PHASE (happens when you search memory)

def search_memory(query: str, embedding_model, top_k: int = 5):
    """Find most relevant memory files for query."""
    
    # Generate query embedding
    query_embedding = embedding_model.encode(query)
    # → [0.21, -0.43, 0.81, ..., -0.31]
    
    # Find similar embeddings
    results = index.search(query_embedding, top_k=top_k)
    
    # Results ranked by similarity:
    # [
    #   {"file": "task-logs/jwt-auth.md", "score": 0.92},
    #   {"file": "systemPatterns.md", "score": 0.87},
    #   {"file": "errors/auth-timeout.md", "score": 0.81}
    # ]
    
    return results
```

**Similarity Metrics**:

```python
import numpy as np

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    Cosine similarity: angle between vectors.
    Range: -1 to 1 (1 = identical, 0 = orthogonal, -1 = opposite)
    
    Most common for embeddings.
    """
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def dot_product_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    Dot product: magnitude-aware similarity.
    Range: -∞ to +∞
    
    Faster than cosine, good for pre-normalized embeddings.
    """
    return np.dot(a, b)


def euclidean_distance(a: np.ndarray, b: np.ndarray) -> float:
    """
    Euclidean distance: straight-line distance.
    Range: 0 to ∞ (0 = identical, larger = more different)
    
    Less common for embeddings, but useful for spatial problems.
    """
    return np.linalg.norm(a - b)
```

**Which to use?**
- ✅ **Cosine similarity** - Standard for embeddings (normalized)
- ✅ **Dot product** - Fast alternative if embeddings are normalized
- ❌ **Euclidean distance** - Rarely used for semantic search

### 1.4 Embedding Generation Pipeline

**Complete embedding generation system**:

```python
from pathlib import Path
from typing import List, Dict
import numpy as np
from sentence_transformers import SentenceTransformer
import json

class EmbeddingGenerator:
    """Generate and manage embeddings for memory files."""
    
    def __init__(
        self,
        model_name: str = "TaylorAI/bge-micro-v2",
        device: str = "cpu"
    ):
        """
        Initialize embedding model.
        
        Args:
            model_name: HuggingFace model name
            device: 'cpu' or 'cuda'
        """
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name, device=device)
        self.model_name = model_name
        self.dimensions = self.model.get_sentence_embedding_dimension()
        
        print(f"✓ Model loaded: {self.dimensions} dimensions")
    
    def encode_text(self, text: str) -> np.ndarray:
        """
        Generate embedding for text.
        
        Args:
            text: Text to embed
        
        Returns:
            Embedding vector (numpy array)
        """
        # Normalize whitespace
        text = " ".join(text.split())
        
        # Generate embedding
        embedding = self.model.encode(
            text,
            normalize_embeddings=True  # Normalize for cosine similarity
        )
        
        return embedding
    
    def encode_file(self, file_path: Path) -> Dict:
        """
        Generate embedding for entire file.
        
        Args:
            file_path: Path to file
        
        Returns:
            Dict with embedding and metadata
        """
        # Read file
        content = file_path.read_text(encoding='utf-8')
        
        # Extract frontmatter (don't embed it)
        content_without_frontmatter = self._remove_frontmatter(content)
        
        # Generate embedding
        embedding = self.encode_text(content_without_frontmatter)
        
        return {
            'file': str(file_path),
            'embedding': embedding.tolist(),  # Convert to list for JSON
            'dimensions': len(embedding),
            'model': self.model_name,
            'length': len(content_without_frontmatter)
        }
    
    def encode_chunks(
        self,
        file_path: Path,
        chunk_size: int = 500,
        overlap: int = 50
    ) -> List[Dict]:
        """
        Generate embeddings for file chunks (for large files).
        
        Args:
            file_path: Path to file
            chunk_size: Characters per chunk
            overlap: Overlap between chunks
        
        Returns:
            List of chunk embeddings
        """
        content = file_path.read_text(encoding='utf-8')
        content_clean = self._remove_frontmatter(content)
        
        # Split into chunks
        chunks = self._create_chunks(content_clean, chunk_size, overlap)
        
        # Generate embeddings for all chunks
        chunk_embeddings = []
        
        for i, chunk in enumerate(chunks):
            embedding = self.encode_text(chunk['text'])
            
            chunk_embeddings.append({
                'file': str(file_path),
                'chunk_id': i,
                'start': chunk['start'],
                'end': chunk['end'],
                'text': chunk['text'],
                'embedding': embedding.tolist()
            })
        
        return chunk_embeddings
    
    def _remove_frontmatter(self, content: str) -> str:
        """Remove YAML frontmatter from content."""
        
        if content.startswith('---'):
            # Find end of frontmatter
            end_marker = content.find('---', 3)
            if end_marker != -1:
                return content[end_marker + 3:].strip()
        
        return content
    
    def _create_chunks(
        self,
        text: str,
        chunk_size: int,
        overlap: int
    ) -> List[Dict]:
        """Split text into overlapping chunks."""
        
        chunks = []
        start = 0
        
        while start < len(text):
            end = min(start + chunk_size, len(text))
            
            chunks.append({
                'start': start,
                'end': end,
                'text': text[start:end]
            })
            
            # Move to next chunk with overlap
            start = end - overlap
            
            if start >= len(text) - overlap:
                break
        
        return chunks


# Example usage
if __name__ == "__main__":
    # Initialize generator
    generator = EmbeddingGenerator()
    
    # Embed single file
    result = generator.encode_file(Path(".claude/core/systemPatterns.md"))
    print(f"Generated embedding: {len(result['embedding'])} dimensions")
    
    # Embed file in chunks (for large files)
    chunks = generator.encode_chunks(
        Path(".claude/core/systemPatterns.md"),
        chunk_size=500
    )
    print(f"Generated {len(chunks)} chunk embeddings")
```

### 1.5 Vector Index Storage

**Efficient storage for embeddings**:

```python
import json
import numpy as np
from typing import List, Dict, Tuple
from pathlib import Path

class VectorIndex:
    """Simple vector index for semantic search."""
    
    def __init__(self, dimensions: int):
        self.dimensions = dimensions
        self.embeddings: List[np.ndarray] = []
        self.metadata: List[Dict] = []
    
    def add(self, embedding: np.ndarray, metadata: Dict):
        """
        Add embedding to index.
        
        Args:
            embedding: Vector embedding
            metadata: Associated metadata (file path, etc.)
        """
        if len(embedding) != self.dimensions:
            raise ValueError(f"Expected {self.dimensions} dims, got {len(embedding)}")
        
        self.embeddings.append(embedding)
        self.metadata.append(metadata)
    
    def search(
        self,
        query_embedding: np.ndarray,
        top_k: int = 5,
        threshold: float = 0.0
    ) -> List[Tuple[Dict, float]]:
        """
        Search for similar embeddings.
        
        Args:
            query_embedding: Query vector
            top_k: Number of results to return
            threshold: Minimum similarity score
        
        Returns:
            List of (metadata, score) tuples
        """
        if len(self.embeddings) == 0:
            return []
        
        # Calculate similarities
        similarities = []
        
        for i, embedding in enumerate(self.embeddings):
            similarity = self._cosine_similarity(query_embedding, embedding)
            
            if similarity >= threshold:
                similarities.append((self.metadata[i], similarity))
        
        # Sort by similarity (highest first)
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        # Return top k
        return similarities[:top_k]
    
    def _cosine_similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        """Calculate cosine similarity."""
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    def save(self, path: Path):
        """Save index to disk."""
        data = {
            'dimensions': self.dimensions,
            'embeddings': [emb.tolist() for emb in self.embeddings],
            'metadata': self.metadata
        }
        
        with open(path, 'w') as f:
            json.dump(data, f)
    
    @classmethod
    def load(cls, path: Path) -> 'VectorIndex':
        """Load index from disk."""
        with open(path, 'r') as f:
            data = json.load(f)
        
        index = cls(dimensions=data['dimensions'])
        index.embeddings = [np.array(emb) for emb in data['embeddings']]
        index.metadata = data['metadata']
        
        return index
```

---

## 2. Smart Connections Plugin Configuration

### 2.1 Installation & Setup

**Smart Connections** is an Obsidian plugin that automatically generates embeddings for your notes.

**Installation Steps**:

```bash
# 1. Open Obsidian
# 2. Settings → Community Plugins → Browse
# 3. Search "Smart Connections"
# 4. Install + Enable

# OR install manually:
cd /path/to/vault/.obsidian/plugins
git clone https://github.com/brianpetro/obsidian-smart-connections.git smart-connections
cd smart-connections
npm install
npm run build
```

**First-Time Configuration**:

1. **Open Smart Connections Settings**
2. **Choose Embedding Model**:
   - Local (Recommended): `TaylorAI/bge-micro-v2`
   - API: OpenAI, Anthropic, etc.

3. **Configure Folders**:
   ```
   Include Folders:
     - .claude/
     - notes/
     - projects/
   
   Exclude Folders:
     - templates/
     - archive/
     - .trash/
   ```

4. **Set Parameters**:
   ```
   Min Characters: 100
   Max Characters: 5000
   Embedding Model: TaylorAI/bge-micro-v2
   Auto-Refresh: On file save
   ```

### 2.2 Optimal Settings for Memory Integration

**Complete configuration for SPES memory bank**:

```json
{
  "smart_connections_settings": {
    "embedding_model": "TaylorAI/bge-micro-v2",
    "model_type": "local",
    "dimensions": 384,
    
    "file_includes": [
      ".claude/core",
      ".claude/task-logs",
      ".claude/errors",
      ".claude/plans"
    ],
    
    "file_excludes": [
      ".claude/archive",
      ".claude/versions",
      "templates",
      ".trash"
    ],
    
    "min_chars": 100,
    "max_chars": 5000,
    
    "chunk_size": 500,
    "chunk_overlap": 50,
    
    "auto_refresh": true,
    "refresh_on_save": true,
    "refresh_interval": 300,
    
    "storage": {
      "type": "json",
      "path": ".smart-env/smart_sources.json",
      "format": "single_file"
    },
    
    "search": {
      "top_k": 10,
      "threshold": 0.3,
      "use_cache": true
    }
  }
}
```

**Key Settings Explained**:

| Setting | Value | Rationale |
|---------|-------|-----------|
| `min_chars: 100` | 100 | Small enough to capture brief notes |
| `max_chars: 5000` | 5000 | Reasonable chunk size for context |
| `chunk_size: 500` | 500 | Balance between granularity and context |
| `chunk_overlap: 50` | 50 | 10% overlap prevents boundary issues |
| `refresh_on_save: true` | true | Immediate embedding updates |
| `threshold: 0.3` | 0.3 | Minimum similarity (30% match) |

### 2.3 Embedding Storage Format

**Smart Connections stores embeddings in `.smart-env/`**:

```
vault/
└── .smart-env/
    ├── smart_sources.json      # Single-file mode (default)
    └── multi/                  # Multi-file AJSON mode (large vaults)
        ├── sources_00001.ajson
        ├── sources_00002.ajson
        └── ...
```

**Storage Format** (smart_sources.json):

```json
{
  "version": "2.0.0",
  "model": "TaylorAI/bge-micro-v2",
  "dimensions": 384,
  "sources": {
    ".claude/core/systemPatterns.md": {
      "path": ".claude/core/systemPatterns.md",
      "mtime": 1703721600,
      "size": 15234,
      "embedding": [0.23, -0.45, 0.78, ...],  // 384 numbers
      "chunks": [
        {
          "id": 0,
          "start": 0,
          "end": 500,
          "embedding": [0.21, -0.43, 0.81, ...]
        },
        {
          "id": 1,
          "start": 450,
          "end": 950,
          "embedding": [0.19, -0.41, 0.79, ...]
        }
      ]
    },
    ".claude/task-logs/2025-12-27-1000-jwt-auth.md": {
      "path": ".claude/task-logs/2025-12-27-1000-jwt-auth.md",
      "mtime": 1703725200,
      "size": 8456,
      "embedding": [0.15, -0.38, 0.65, ...],
      "chunks": [...]
    }
  }
}
```

### 2.4 Index Management

**Managing embeddings for optimal performance**:

```python
from pathlib import Path
import json
from datetime import datetime

class SmartConnectionsManager:
    """Manage Smart Connections embeddings."""
    
    def __init__(self, vault_path: Path):
        self.vault_path = Path(vault_path)
        self.embeddings_file = vault_path / ".smart-env" / "smart_sources.json"
    
    def get_stats(self) -> dict:
        """Get embedding statistics."""
        
        if not self.embeddings_file.exists():
            return {"status": "not_initialized"}
        
        data = json.loads(self.embeddings_file.read_text())
        
        total_files = len(data.get('sources', {}))
        total_chunks = sum(
            len(source.get('chunks', []))
            for source in data.get('sources', {}).values()
        )
        
        return {
            "status": "active",
            "model": data.get('model'),
            "dimensions": data.get('dimensions'),
            "total_files": total_files,
            "total_chunks": total_chunks,
            "storage_size": self.embeddings_file.stat().st_size / 1024 / 1024,  # MB
            "last_updated": datetime.fromtimestamp(
                self.embeddings_file.stat().st_mtime
            ).isoformat()
        }
    
    def verify_embeddings(self) -> dict:
        """Verify all files have embeddings."""
        
        data = json.loads(self.embeddings_file.read_text())
        sources = data.get('sources', {})
        
        # Check which memory files are embedded
        memory_files = list(self.vault_path.glob(".claude/**/*.md"))
        
        embedded = []
        missing = []
        
        for file_path in memory_files:
            rel_path = str(file_path.relative_to(self.vault_path))
            
            if rel_path in sources:
                embedded.append(rel_path)
            else:
                missing.append(rel_path)
        
        return {
            "embedded": embedded,
            "missing": missing,
            "coverage": len(embedded) / len(memory_files) if memory_files else 0
        }
    
    def force_refresh(self):
        """Force refresh all embeddings."""
        
        # Trigger Smart Connections refresh
        # This is done through Obsidian's command palette:
        # "Smart Connections: Refresh all embeddings"
        
        print("To refresh embeddings:")
        print("1. Open Obsidian")
        print("2. Command Palette (Ctrl/Cmd + P)")
        print("3. Run: Smart Connections: Refresh all embeddings")
        print("4. Wait for completion (check status bar)")
    
    def check_freshness(self, max_age_seconds: int = 300) -> dict:
        """Check if embeddings are fresh."""
        
        if not self.embeddings_file.exists():
            return {"status": "missing"}
        
        age = datetime.now().timestamp() - self.embeddings_file.stat().st_mtime
        
        return {
            "status": "fresh" if age < max_age_seconds else "stale",
            "age_seconds": age,
            "last_updated": datetime.fromtimestamp(
                self.embeddings_file.stat().st_mtime
            ).isoformat()
        }


# Usage
manager = SmartConnectionsManager(Path("/path/to/vault"))

stats = manager.get_stats()
print(f"Indexed: {stats['total_files']} files, {stats['total_chunks']} chunks")
print(f"Storage: {stats['storage_size']:.2f} MB")

verification = manager.verify_embeddings()
print(f"Coverage: {verification['coverage']*100:.1f}%")
if verification['missing']:
    print(f"Missing embeddings for {len(verification['missing'])} files")
```

### 2.5 Troubleshooting Embedding Generation

**Common issues and solutions**:

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Embeddings not generating** | `.smart-env/` empty | 1. Check Obsidian is running<br>2. Check plugin is enabled<br>3. Check file size > min_chars |
| **Files not indexed** | Some files missing from index | 1. Check exclusion settings<br>2. Verify file size<br>3. Force refresh |
| **Slow embedding** | Takes minutes to index | 1. Switch to smaller model<br>2. Reduce chunk_size<br>3. Use multi-file storage |
| **High memory usage** | Obsidian sluggish | 1. Use smaller embedding model<br>2. Reduce dimensions<br>3. Exclude large files |
| **Stale embeddings** | Search returns old content | 1. Enable auto-refresh<br>2. Force manual refresh<br>3. Check refresh_on_save |

**Diagnostic Commands**:

```python
# Check if Smart Connections is working
def diagnose_smart_connections(vault_path: Path):
    """Run diagnostics on Smart Connections setup."""
    
    print("Smart Connections Diagnostic")
    print("=" * 60)
    
    # 1. Check .smart-env directory
    smart_env = vault_path / ".smart-env"
    if not smart_env.exists():
        print("✗ .smart-env directory not found")
        print("  → Smart Connections may not be initialized")
        return
    
    print("✓ .smart-env directory exists")
    
    # 2. Check embeddings file
    embeddings_file = smart_env / "smart_sources.json"
    if not embeddings_file.exists():
        print("✗ smart_sources.json not found")
        print("  → No embeddings have been generated")
        return
    
    print("✓ smart_sources.json exists")
    
    # 3. Check embeddings content
    data = json.loads(embeddings_file.read_text())
    
    print(f"  Model: {data.get('model', 'unknown')}")
    print(f"  Dimensions: {data.get('dimensions', 'unknown')}")
    print(f"  Files indexed: {len(data.get('sources', {}))}")
    
    # 4. Check recent updates
    mtime = embeddings_file.stat().st_mtime
    age = datetime.now().timestamp() - mtime
    
    print(f"  Last updated: {age/60:.1f} minutes ago")
    
    if age > 3600:  # 1 hour
        print("  ⚠ Embeddings may be stale")
    
    print("\n✓ Smart Connections is working correctly")


# Run diagnostic
diagnose_smart_connections(Path("/path/to/vault"))
```

---

## 3. Model Context Protocol (MCP) Deep Dive

### 3.1 What is MCP?

**Model Context Protocol (MCP)** is a standard for connecting LLMs to external tools and data sources.

**Architecture**:

```
┌──────────────────────────────────────────────────────┐
│                     LLM (Claude)                     │
│  "Find relevant memories about authentication"      │
└────────────────────┬─────────────────────────────────┘
                     │ MCP Protocol
                     ↓
┌──────────────────────────────────────────────────────┐
│                   MCP Server                         │
│  - Exposes tools (lookup, connection, stats)        │
│  - Connects to data sources (Smart Connections)     │
│  - Handles tool invocation                          │
└────────────────────┬─────────────────────────────────┘
                     │
                     ↓
┌──────────────────────────────────────────────────────┐
│              Data Source (Smart Connections)         │
│  - Vector embeddings in .smart-env/                 │
│  - Semantic search capabilities                      │
└──────────────────────────────────────────────────────┘
```

**MCP vs Direct API**:

| Approach | Pros | Cons |
|----------|------|------|
| **Direct API** | Simple, direct access | Tightly coupled, hard to change |
| **MCP** | Standardized, composable | Extra layer of abstraction |

**Why MCP for SPES?**
- ✅ **Standard interface**: Works with multiple LLM platforms
- ✅ **Composable**: Multiple MCP servers can coexist
- ✅ **Maintainable**: Change data source without changing LLM code
- ✅ **Extensible**: Easy to add new tools

### 3.2 MCP Server Architecture

**Complete MCP server for Smart Connections**:

```typescript
// mcp-server.ts
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import fs from 'fs';
import path from 'path';

interface SmartConnection {
  path: string;
  embedding: number[];
  chunks?: Array<{
    id: number;
    start: number;
    end: number;
    embedding: number[];
  }>;
}

interface SmartSources {
  version: string;
  model: string;
  dimensions: number;
  sources: { [key: string]: SmartConnection };
}

class SmartConnectionsMCPServer {
  private server: Server;
  private vaultPath: string;
  private embeddingsData: SmartSources | null = null;
  
  constructor(vaultPath: string) {
    this.vaultPath = vaultPath;
    this.server = new Server(
      {
        name: 'smart-connections-mcp',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );
    
    this.setupToolHandlers();
    this.loadEmbeddings();
  }
  
  private loadEmbeddings(): void {
    const embeddingsPath = path.join(
      this.vaultPath,
      '.smart-env',
      'smart_sources.json'
    );
    
    try {
      const data = fs.readFileSync(embeddingsPath, 'utf-8');
      this.embeddingsData = JSON.parse(data);
      console.error(`✓ Loaded embeddings for ${Object.keys(this.embeddingsData!.sources).length} files`);
    } catch (error) {
      console.error('✗ Failed to load embeddings:', error);
      this.embeddingsData = null;
    }
  }
  
  private setupToolHandlers(): void {
    // List available tools
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [
        {
          name: 'lookup',
          description: 'Semantic search across vault using natural language query',
          inputSchema: {
            type: 'object',
            properties: {
              query: {
                type: 'string',
                description: 'Natural language search query',
              },
              limit: {
                type: 'number',
                description: 'Maximum number of results (default: 10)',
                default: 10,
              },
              threshold: {
                type: 'number',
                description: 'Minimum similarity score 0-1 (default: 0.3)',
                default: 0.3,
              },
            },
            required: ['query'],
          },
        },
        {
          name: 'connection',
          description: 'Find notes connected/similar to a specific file',
          inputSchema: {
            type: 'object',
            properties: {
              file_path: {
                type: 'string',
                description: 'Path to file to find connections for',
              },
              limit: {
                type: 'number',
                description: 'Maximum number of connections (default: 5)',
                default: 5,
              },
            },
            required: ['file_path'],
          },
        },
        {
          name: 'stats',
          description: 'Get statistics about Smart Connections embeddings',
          inputSchema: {
            type: 'object',
            properties: {},
          },
        },
        {
          name: 'validate',
          description: 'Validate embeddings exist for specific files',
          inputSchema: {
            type: 'object',
            properties: {
              file_paths: {
                type: 'array',
                items: { type: 'string' },
                description: 'List of file paths to validate',
              },
            },
            required: ['file_paths'],
          },
        },
      ],
    }));
    
    // Handle tool calls
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;
      
      if (!this.embeddingsData) {
        return {
          content: [
            {
              type: 'text',
              text: 'Error: Smart Connections embeddings not loaded. Ensure Obsidian is running and embeddings are generated.',
            },
          ],
        };
      }
      
      switch (name) {
        case 'lookup':
          return this.handleLookup(args);
        
        case 'connection':
          return this.handleConnection(args);
        
        case 'stats':
          return this.handleStats();
        
        case 'validate':
          return this.handleValidate(args);
        
        default:
          throw new Error(`Unknown tool: ${name}`);
      }
    });
  }
  
  private async handleLookup(args: any) {
    const query = args.query as string;
    const limit = (args.limit as number) || 10;
    const threshold = (args.threshold as number) || 0.3;
    
    // Generate query embedding
    // In production, this would use the same model as Smart Connections
    // For now, we'll use a placeholder
    const queryEmbedding = await this.generateEmbedding(query);
    
    // Search for similar embeddings
    const results = this.semanticSearch(queryEmbedding, limit, threshold);
    
    // Format results
    const formattedResults = results.map((result, index) => {
      const content = this.loadFileContent(result.path);
      return `
## Result ${index + 1}: ${result.path} (similarity: ${result.score.toFixed(3)})

${content.substring(0, 500)}${content.length > 500 ? '...' : ''}
`;
    }).join('\n\n---\n\n');
    
    return {
      content: [
        {
          type: 'text',
          text: `Found ${results.length} results for "${query}":\n\n${formattedResults}`,
        },
      ],
    };
  }
  
  private async handleConnection(args: any) {
    const filePath = args.file_path as string;
    const limit = (args.limit as number) || 5;
    
    // Get embedding for target file
    const source = this.embeddingsData!.sources[filePath];
    
    if (!source) {
      return {
        content: [
          {
            type: 'text',
            text: `Error: File "${filePath}" not found in embeddings index.`,
          },
        ],
      };
    }
    
    // Find similar files
    const results = this.semanticSearch(source.embedding, limit + 1, 0.0)
      .filter(r => r.path !== filePath)  // Exclude the file itself
      .slice(0, limit);
    
    const connections = results.map((result, index) => 
      `${index + 1}. ${result.path} (similarity: ${result.score.toFixed(3)})`
    ).join('\n');
    
    return {
      content: [
        {
          type: 'text',
          text: `Connected notes to "${filePath}":\n\n${connections}`,
        },
      ],
    };
  }
  
  private async handleStats() {
    const totalFiles = Object.keys(this.embeddingsData!.sources).length;
    const totalChunks = Object.values(this.embeddingsData!.sources)
      .reduce((sum, source) => sum + (source.chunks?.length || 0), 0);
    
    const stats = `
Smart Connections Statistics:

Model: ${this.embeddingsData!.model}
Dimensions: ${this.embeddingsData!.dimensions}
Total Files: ${totalFiles}
Total Chunks: ${totalChunks}
Version: ${this.embeddingsData!.version}
`;
    
    return {
      content: [
        {
          type: 'text',
          text: stats,
        },
      ],
    };
  }
  
  private async handleValidate(args: any) {
    const filePaths = args.file_paths as string[];
    
    const results = filePaths.map(path => ({
      path,
      exists: path in this.embeddingsData!.sources,
    }));
    
    const summary = results.map(r => 
      `${r.exists ? '✓' : '✗'} ${r.path}`
    ).join('\n');
    
    return {
      content: [
        {
          type: 'text',
          text: `Embedding validation:\n\n${summary}`,
        },
      ],
    };
  }
  
  private async generateEmbedding(text: string): Promise<number[]> {
    // In production, use the same model as Smart Connections
    // For demonstration, return dummy embedding
    
    // This would actually call the embedding model:
    // const model = new SentenceTransformer('TaylorAI/bge-micro-v2');
    // return model.encode(text);
    
    return Array(this.embeddingsData!.dimensions).fill(0);
  }
  
  private semanticSearch(
    queryEmbedding: number[],
    limit: number,
    threshold: number
  ): Array<{ path: string; score: number }> {
    const results: Array<{ path: string; score: number }> = [];
    
    for (const [path, source] of Object.entries(this.embeddingsData!.sources)) {
      const similarity = this.cosineSimilarity(queryEmbedding, source.embedding);
      
      if (similarity >= threshold) {
        results.push({ path, score: similarity });
      }
    }
    
    // Sort by similarity (highest first)
    results.sort((a, b) => b.score - a.score);
    
    return results.slice(0, limit);
  }
  
  private cosineSimilarity(a: number[], b: number[]): number {
    const dotProduct = a.reduce((sum, val, i) => sum + val * b[i], 0);
    const magnitudeA = Math.sqrt(a.reduce((sum, val) => sum + val * val, 0));
    const magnitudeB = Math.sqrt(b.reduce((sum, val) => sum + val * val, 0));
    
    return dotProduct / (magnitudeA * magnitudeB);
  }
  
  private loadFileContent(filePath: string): string {
    try {
      const fullPath = path.join(this.vaultPath, filePath);
      return fs.readFileSync(fullPath, 'utf-8');
    } catch (error) {
      return `[Error loading file: ${filePath}]`;
    }
  }
  
  async run(): Promise<void> {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('Smart Connections MCP Server running on stdio');
  }
}

// Start server
const vaultPath = process.env.VAULT_PATH || process.argv[2];

if (!vaultPath) {
  console.error('Usage: node mcp-server.js <vault-path>');
  process.exit(1);
}

const server = new SmartConnectionsMCPServer(vaultPath);
server.run().catch(console.error);
```

### 3.3 MCP Tool Implementations

**The four core tools**:

#### Tool 1: `lookup` - Semantic Search

```typescript
/**
 * Semantic search across entire vault.
 * 
 * Use cases:
 * - "Find all notes about authentication"
 * - "What do we know about JWT security?"
 * - "Show me error patterns related to database"
 * 
 * Parameters:
 * - query: Natural language search query
 * - limit: Max results (default: 10)
 * - threshold: Min similarity 0-1 (default: 0.3)
 * 
 * Returns: Ranked list of matching notes with similarity scores
 */
```

**Example Usage**:

```json
{
  "tool": "lookup",
  "arguments": {
    "query": "authentication security best practices",
    "limit": 5,
    "threshold": 0.5
  }
}
```

**Example Response**:

```
Found 5 results for "authentication security best practices":

## Result 1: .claude/core/systemPatterns.md (similarity: 0.872)

# System Patterns

## Authentication Pattern: JWT with PKCE

**Context**: Need stateless authentication for microservices + mobile apps

**Decision**: JWT access tokens (15min) + refresh tokens (7 days) + PKCE for mobile
...

## Result 2: .claude/task-logs/2025-12-27-1000-jwt-auth.md (similarity: 0.814)

# Task Log: Implement JWT Authentication

Implemented JWT-based authentication with PKCE extension for mobile security...

## Result 3: .claude/errors/2025-12-26-auth-timeout.md (similarity: 0.753)

# Error: Authentication Timeout

Error occurred when JWT tokens not refreshed properly...
```

#### Tool 2: `connection` - Find Related Notes

```typescript
/**
 * Find notes semantically related to a specific file.
 * 
 * Use cases:
 * - "What other notes relate to this authentication doc?"
 * - "Find similar error logs"
 * - "Show me related patterns"
 * 
 * Parameters:
 * - file_path: Path to source file
 * - limit: Max connections (default: 5)
 * 
 * Returns: List of related files with similarity scores
 */
```

**Example Usage**:

```json
{
  "tool": "connection",
  "arguments": {
    "file_path": ".claude/core/systemPatterns.md",
    "limit": 5
  }
}
```

**Example Response**:

```
Connected notes to ".claude/core/systemPatterns.md":

1. .claude/task-logs/2025-12-27-1000-jwt-auth.md (similarity: 0.845)
2. .claude/core/techContext.md (similarity: 0.792)
3. .claude/errors/2025-12-26-auth-timeout.md (similarity: 0.731)
4. .claude/plans/auth-implementation-plan.md (similarity: 0.698)
5. .claude/task-logs/2025-12-25-oauth-setup.md (similarity: 0.654)
```

#### Tool 3: `stats` - Embedding Statistics

```typescript
/**
 * Get statistics about Smart Connections index.
 * 
 * Use cases:
 * - Verify embeddings are working
 * - Check index coverage
 * - Diagnose performance issues
 * 
 * Parameters: None
 * 
 * Returns: Index statistics (model, files, chunks, etc.)
 */
```

#### Tool 4: `validate` - Verify Embeddings

```typescript
/**
 * Validate specific files have embeddings.
 * 
 * Use cases:
 * - Check if new files are indexed
 * - Verify critical files are searchable
 * - Debugging embedding issues
 * 
 * Parameters:
 * - file_paths: Array of paths to check
 * 
 * Returns: Validation status for each file
 */
```

### 3.4 MCP Client Configuration

**Configuring Claude Desktop to use MCP server**:

```json
// ~/Library/Application Support/Claude/claude_desktop_config.json (macOS)
// %APPDATA%\Claude\claude_desktop_config.json (Windows)

{
  "mcpServers": {
    "smart-connections": {
      "command": "node",
      "args": [
        "/path/to/mcp-server.js",
        "/path/to/obsidian/vault"
      ],
      "env": {
        "VAULT_PATH": "/path/to/obsidian/vault"
      }
    }
  }
}
```

**For multiple LLM platforms**:

```json
{
  "mcpServers": {
    "smart-connections": {
      "command": "node",
      "args": ["/path/to/mcp-server.js", "/path/to/vault"]
    }
  },
  
  "platforms": {
    "claude": {
      "enabled": true,
      "servers": ["smart-connections"]
    },
    
    "gemini": {
      "enabled": true,
      "servers": ["smart-connections"]
    },
    
    "local-llm": {
      "enabled": true,
      "servers": ["smart-connections"],
      "endpoint": "http://localhost:1234/v1"
    }
  }
}
```

**Verification**:

```bash
# 1. Test MCP server directly
node /path/to/mcp-server.js /path/to/vault

# 2. Check Claude Desktop logs
tail -f ~/Library/Logs/Claude/mcp-smart-connections.log

# 3. In Claude Desktop, verify tools appear:
# Type: "What tools do you have access to?"
# Should list: lookup, connection, stats, validate
```

### 3.5 Production MCP Deployment

**Complete production setup with monitoring and error handling**:

```typescript
// production-mcp-server.ts
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import fs from 'fs';
import path from 'path';
import { createLogger, transports, format } from 'winston';

// Production logging
const logger = createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: format.combine(
    format.timestamp(),
    format.errors({ stack: true }),
    format.json()
  ),
  transports: [
    new transports.File({ filename: 'mcp-server-error.log', level: 'error' }),
    new transports.File({ filename: 'mcp-server.log' }),
  ],
});

if (process.env.NODE_ENV !== 'production') {
  logger.add(new transports.Console({
    format: format.simple(),
  }));
}

class ProductionSmartConnectionsMCP {
  private server: Server;
  private vaultPath: string;
  private embeddingsData: SmartSources | null = null;
  private embeddingCache: Map<string, number[]> = new Map();
  private requestCount: number = 0;
  private errorCount: number = 0;
  private lastRefresh: Date = new Date();
  
  constructor(vaultPath: string, config: MCPConfig = {}) {
    this.vaultPath = vaultPath;
    this.config = {
      maxCacheSize: config.maxCacheSize || 1000,
      refreshInterval: config.refreshInterval || 300000, // 5 minutes
      enableMetrics: config.enableMetrics !== false,
      ...config
    };
    
    this.server = new Server(
      {
        name: 'smart-connections-mcp',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );
    
    this.setupToolHandlers();
    this.loadEmbeddings();
    this.startBackgroundTasks();
    
    logger.info('Smart Connections MCP Server initialized', {
      vaultPath: this.vaultPath,
      config: this.config
    });
  }
  
  private startBackgroundTasks(): void {
    // Auto-refresh embeddings
    if (this.config.refreshInterval > 0) {
      setInterval(() => {
        this.loadEmbeddings();
      }, this.config.refreshInterval);
    }
    
    // Metrics reporting
    if (this.config.enableMetrics) {
      setInterval(() => {
        this.reportMetrics();
      }, 60000); // Every minute
    }
    
    // Cache cleanup
    setInterval(() => {
      this.cleanupCache();
    }, 300000); // Every 5 minutes
  }
  
  private loadEmbeddings(): void {
    const embeddingsPath = path.join(
      this.vaultPath,
      '.smart-env',
      'smart_sources.json'
    );
    
    try {
      const data = fs.readFileSync(embeddingsPath, 'utf-8');
      this.embeddingsData = JSON.parse(data);
      this.lastRefresh = new Date();
      
      logger.info('Embeddings loaded successfully', {
        fileCount: Object.keys(this.embeddingsData!.sources).length,
        timestamp: this.lastRefresh
      });
    } catch (error) {
      this.errorCount++;
      logger.error('Failed to load embeddings', {
        error: error.message,
        path: embeddingsPath
      });
      
      this.embeddingsData = null;
    }
  }
  
  private cleanupCache(): void {
    if (this.embeddingCache.size > this.config.maxCacheSize) {
      // Remove oldest 20% of cache
      const toRemove = Math.floor(this.embeddingCache.size * 0.2);
      const keys = Array.from(this.embeddingCache.keys());
      
      for (let i = 0; i < toRemove; i++) {
        this.embeddingCache.delete(keys[i]);
      }
      
      logger.debug('Cache cleaned up', {
        removed: toRemove,
        remaining: this.embeddingCache.size
      });
    }
  }
  
  private reportMetrics(): void {
    const metrics = {
      requestCount: this.requestCount,
      errorCount: this.errorCount,
      cacheSize: this.embeddingCache.size,
      embeddingsLoaded: this.embeddingsData !== null,
      fileCount: this.embeddingsData ? Object.keys(this.embeddingsData.sources).length : 0,
      lastRefresh: this.lastRefresh,
      uptime: process.uptime()
    };
    
    logger.info('MCP Server metrics', metrics);
    
    // Reset counters
    this.requestCount = 0;
    this.errorCount = 0;
  }
  
  private async handleLookupWithRetry(args: any, retries: number = 3): Promise<any> {
    for (let attempt = 1; attempt <= retries; attempt++) {
      try {
        return await this.handleLookup(args);
      } catch (error) {
        logger.warn(`Lookup attempt ${attempt} failed`, {
          query: args.query,
          error: error.message
        });
        
        if (attempt === retries) {
          throw error;
        }
        
        // Wait before retry (exponential backoff)
        await new Promise(resolve => setTimeout(resolve, 1000 * attempt));
      }
    }
  }
  
  private validateRequest(args: any, requiredFields: string[]): void {
    for (const field of requiredFields) {
      if (!(field in args)) {
        throw new Error(`Missing required field: ${field}`);
      }
    }
  }
  
  async run(): Promise<void> {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    
    logger.info('Smart Connections MCP Server running on stdio');
    
    // Graceful shutdown
    process.on('SIGTERM', async () => {
      logger.info('SIGTERM received, shutting down gracefully');
      await this.server.close();
      process.exit(0);
    });
    
    process.on('SIGINT', async () => {
      logger.info('SIGINT received, shutting down gracefully');
      await this.server.close();
      process.exit(0);
    });
  }
}
```

**Production Configuration** (`mcp-config.json`):

```json
{
  "vault_path": "/path/to/vault",
  "logging": {
    "level": "info",
    "file": "/var/log/mcp-server.log",
    "maxSize": "10m",
    "maxFiles": 5
  },
  "performance": {
    "maxCacheSize": 2000,
    "refreshInterval": 300000,
    "requestTimeout": 30000,
    "maxConcurrentRequests": 10
  },
  "monitoring": {
    "enableMetrics": true,
    "metricsPort": 9090,
    "healthCheckPort": 9091
  },
  "embeddings": {
    "model": "TaylorAI/bge-micro-v2",
    "dimensions": 384,
    "batchSize": 100
  }
}
```

### 3.6 Error Handling & Edge Cases

**Comprehensive error handling**:

```typescript
class ErrorHandler {
  static async handleToolError(
    toolName: string,
    error: Error,
    context: any
  ): Promise<ToolResponse> {
    logger.error(`Tool error: ${toolName}`, {
      error: error.message,
      stack: error.stack,
      context
    });
    
    // Specific error handling
    if (error.message.includes('ENOENT')) {
      return {
        content: [{
          type: 'text',
          text: `Error: File not found. Ensure Obsidian vault path is correct and files exist.`
        }],
        isError: true
      };
    }
    
    if (error.message.includes('embeddings not loaded')) {
      return {
        content: [{
          type: 'text',
          text: `Error: Smart Connections embeddings not initialized. Please:
1. Ensure Obsidian is running
2. Smart Connections plugin is enabled
3. Embeddings have been generated (check .smart-env/ directory)
4. Try running "Smart Connections: Refresh embeddings" in Obsidian`
        }],
        isError: true
      };
    }
    
    if (error.message.includes('timeout')) {
      return {
        content: [{
          type: 'text',
          text: `Error: Request timed out. The vault may be too large or embeddings are being regenerated. Please try again.`
        }],
        isError: true
      };
    }
    
    // Generic error
    return {
      content: [{
        type: 'text',
        text: `Error: ${error.message}\n\nPlease check the MCP server logs for details.`
      }],
      isError: true
    };
  }
}
```

**Edge Cases**:

| Edge Case | Handling Strategy |
|-----------|-------------------|
| **Empty vault** | Return helpful message, suggest adding files |
| **No embeddings** | Detect and guide user through setup |
| **Stale embeddings** | Auto-refresh or warn user |
| **Large queries** | Truncate and warn |
| **Invalid file paths** | Validate and suggest corrections |
| **Concurrent requests** | Queue and process sequentially |
| **Memory pressure** | Implement LRU cache eviction |
| **Vault moved** | Detect and request new path |

### 3.7 Performance Optimization

**Optimizing MCP server performance**:

```typescript
class PerformanceOptimizer {
  private queryCache: LRUCache<string, any>;
  private embeddingPool: EmbeddingPool;
  
  constructor() {
    this.queryCache = new LRUCache({
      max: 500,
      ttl: 1000 * 60 * 5 // 5 minutes
    });
    
    this.embeddingPool = new EmbeddingPool({
      maxWorkers: 4,
      queueSize: 100
    });
  }
  
  async optimizedLookup(
    query: string,
    options: SearchOptions
  ): Promise<SearchResult[]> {
    // 1. Check cache
    const cacheKey = `${query}:${JSON.stringify(options)}`;
    const cached = this.queryCache.get(cacheKey);
    
    if (cached) {
      logger.debug('Cache hit', { query });
      return cached;
    }
    
    // 2. Generate embedding (pooled)
    const queryEmbedding = await this.embeddingPool.encode(query);
    
    // 3. Parallel search across chunks
    const results = await this.parallelSearch(
      queryEmbedding,
      options
    );
    
    // 4. Cache results
    this.queryCache.set(cacheKey, results);
    
    return results;
  }
  
  private async parallelSearch(
    queryEmbedding: number[],
    options: SearchOptions
  ): Promise<SearchResult[]> {
    const sources = Object.entries(this.embeddingsData.sources);
    const batchSize = 100;
    const batches = [];
    
    // Split into batches
    for (let i = 0; i < sources.length; i += batchSize) {
      batches.push(sources.slice(i, i + batchSize));
    }
    
    // Process batches in parallel
    const batchResults = await Promise.all(
      batches.map(batch => this.searchBatch(batch, queryEmbedding, options))
    );
    
    // Merge and sort results
    return batchResults
      .flat()
      .sort((a, b) => b.score - a.score)
      .slice(0, options.limit);
  }
}
```

**Performance Benchmarks**:

| Operation | Small Vault (<1K files) | Medium Vault (1K-10K) | Large Vault (>10K) |
|-----------|-------------------------|----------------------|-------------------|
| **Lookup** | <100ms | 100-500ms | 500ms-2s |
| **Connection** | <50ms | 50-200ms | 200-800ms |
| **Stats** | <10ms | <10ms | <10ms |
| **Validate** | <20ms | 20-100ms | 100-500ms |

**Optimization Checklist**:

- ✅ Cache frequently queried embeddings
- ✅ Batch process large searches
- ✅ Use connection pooling
- ✅ Implement request queuing
- ✅ Lazy-load large embeddings
- ✅ Pre-compute common queries
- ✅ Use efficient similarity algorithms

### 3.8 Multi-Platform Configuration

**Configuring MCP for different LLM platforms**:

#### Claude Desktop

```json
// ~/Library/Application Support/Claude/claude_desktop_config.json
{
  "mcpServers": {
    "smart-connections": {
      "command": "node",
      "args": ["/path/to/mcp-server.js", "/path/to/vault"],
      "env": {
        "NODE_ENV": "production",
        "LOG_LEVEL": "info",
        "VAULT_PATH": "/path/to/vault"
      }
    }
  }
}
```

#### Gemini via Proxy

```json
// gemini-mcp-config.json
{
  "mcp": {
    "servers": {
      "smart-connections": {
        "url": "http://localhost:3000/mcp",
        "auth": {
          "type": "bearer",
          "token": "${GEMINI_MCP_TOKEN}"
        }
      }
    }
  }
}
```

**Proxy Server** (for Gemini):

```typescript
// mcp-proxy.ts
import express from 'express';
import { spawn } from 'child_process';

const app = express();
app.use(express.json());

let mcpProcess: any = null;

app.post('/mcp', async (req, res) => {
  const { method, params } = req.body;
  
  // Start MCP server if not running
  if (!mcpProcess) {
    mcpProcess = spawn('node', ['mcp-server.js', process.env.VAULT_PATH]);
  }
  
  // Forward request to MCP server
  // ... (implementation details)
  
  res.json(result);
});

app.listen(3000, () => {
  console.log('MCP proxy listening on port 3000');
});
```

#### Local LLMs (Ollama, LM Studio)

```json
// local-llm-config.json
{
  "model": "llama3:8b",
  "tools": {
    "mcp_servers": [
      {
        "name": "smart-connections",
        "url": "stdio://node /path/to/mcp-server.js /path/to/vault"
      }
    ]
  },
  "system_prompt": "You have access to semantic memory via Smart Connections MCP server. Use the lookup tool to find relevant information."
}
```

### 3.9 Monitoring & Observability

**Complete monitoring setup**:

```typescript
// monitoring.ts
import { Counter, Histogram, Gauge } from 'prom-client';

export class MCPMetrics {
  private requestCounter: Counter;
  private errorCounter: Counter;
  private requestDuration: Histogram;
  private embeddingsGauge: Gauge;
  private cacheHitRate: Gauge;
  
  constructor() {
    this.requestCounter = new Counter({
      name: 'mcp_requests_total',
      help: 'Total MCP requests',
      labelNames: ['tool', 'status']
    });
    
    this.errorCounter = new Counter({
      name: 'mcp_errors_total',
      help: 'Total MCP errors',
      labelNames: ['tool', 'error_type']
    });
    
    this.requestDuration = new Histogram({
      name: 'mcp_request_duration_seconds',
      help: 'MCP request duration',
      labelNames: ['tool'],
      buckets: [0.01, 0.05, 0.1, 0.5, 1, 2, 5]
    });
    
    this.embeddingsGauge = new Gauge({
      name: 'mcp_embeddings_count',
      help: 'Number of indexed embeddings'
    });
    
    this.cacheHitRate = new Gauge({
      name: 'mcp_cache_hit_rate',
      help: 'Cache hit rate percentage'
    });
  }
  
  recordRequest(tool: string, status: 'success' | 'error', duration: number): void {
    this.requestCounter.inc({ tool, status });
    this.requestDuration.observe({ tool }, duration);
  }
  
  recordError(tool: string, errorType: string): void {
    this.errorCounter.inc({ tool, error_type: errorType });
  }
  
  updateEmbeddingsCount(count: number): void {
    this.embeddingsGauge.set(count);
  }
  
  updateCacheHitRate(rate: number): void {
    this.cacheHitRate.set(rate);
  }
}
```

**Grafana Dashboard** (JSON):

```json
{
  "dashboard": {
    "title": "Smart Connections MCP Server",
    "panels": [
      {
        "title": "Request Rate",
        "targets": [
          {
            "expr": "rate(mcp_requests_total[5m])"
          }
        ]
      },
      {
        "title": "Error Rate",
        "targets": [
          {
            "expr": "rate(mcp_errors_total[5m])"
          }
        ]
      },
      {
        "title": "Request Duration (p99)",
        "targets": [
          {
            "expr": "histogram_quantile(0.99, mcp_request_duration_seconds)"
          }
        ]
      },
      {
        "title": "Cache Hit Rate",
        "targets": [
          {
            "expr": "mcp_cache_hit_rate"
          }
        ]
      }
    ]
  }
}
```

### 3.10 Troubleshooting Guide

**Common issues and solutions**:

#### Issue: MCP Server Not Connecting

**Symptoms**:
- Tools don't appear in LLM interface
- Connection timeout errors
- "Server not responding" messages

**Diagnosis**:

```bash
# 1. Check MCP server process
ps aux | grep mcp-server

# 2. Check logs
tail -f /var/log/mcp-server.log

# 3. Test server directly
echo '{"method": "tools/list"}' | node mcp-server.js /path/to/vault

# 4. Verify config
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

**Solutions**:

1. **Restart MCP server**:
   ```bash
   pkill -f mcp-server
   # Claude Desktop will auto-restart it
   ```

2. **Verify paths are absolute**:
   ```json
   {
     "command": "node",
     "args": [
       "/Users/username/mcp/mcp-server.js",  // ✓ Absolute
       "/Users/username/vault"                // ✓ Absolute
     ]
   }
   ```

3. **Check Node.js version**:
   ```bash
   node --version  # Should be v18+
   ```

#### Issue: Embeddings Not Found

**Symptoms**:
- "Embeddings not loaded" errors
- Empty search results
- "smart_sources.json not found"

**Diagnosis**:

```bash
# 1. Check if Smart Connections has generated embeddings
ls -la /path/to/vault/.smart-env/

# 2. Verify embeddings file exists and is valid
cat /path/to/vault/.smart-env/smart_sources.json | jq '.version'

# 3. Check embedding count
cat /path/to/vault/.smart-env/smart_sources.json | jq '.sources | length'
```

**Solutions**:

1. **Force Smart Connections refresh**:
   - Open Obsidian
   - Command Palette (Cmd/Ctrl + P)
   - Run: "Smart Connections: Refresh all embeddings"
   - Wait for completion

2. **Check Smart Connections settings**:
   - Verify model is downloaded
   - Check folder inclusions/exclusions
   - Verify min character threshold

3. **Manual verification**:
   ```python
   import json
   
   with open('.smart-env/smart_sources.json') as f:
       data = json.load(f)
   
   print(f"Model: {data['model']}")
   print(f"Files: {len(data['sources'])}")
   print(f"Dimensions: {data['dimensions']}")
   ```

#### Issue: Slow Search Performance

**Symptoms**:
- Searches taking >5 seconds
- Timeout errors
- High memory usage

**Diagnosis**:

```bash
# 1. Check vault size
find /path/to/vault -name "*.md" | wc -l

# 2. Check embeddings file size
du -h /path/to/vault/.smart-env/smart_sources.json

# 3. Monitor server performance
node --inspect mcp-server.js /path/to/vault
# Then use Chrome DevTools profiler
```

**Solutions**:

1. **Implement caching**:
   ```typescript
   // Add to mcp-server.ts
   const queryCache = new LRUCache({ max: 1000 });
   ```

2. **Reduce dimensions**:
   - Switch to smaller embedding model
   - TaylorAI/bge-micro-v2 (384) instead of larger models

3. **Exclude large files**:
   ```json
   {
     "file_excludes": [
       "archive/**",
       "*.excalidraw",
       "**/*.png"
     ]
   }
   ```

4. **Use multi-file storage for large vaults**:
   - Smart Connections Settings → Storage → Multi-file AJSON

#### Issue: Inconsistent Results

**Symptoms**:
- Same query returns different results
- Expected documents not appearing
- Relevance seems off

**Diagnosis**:

```bash
# 1. Check embedding freshness
stat -f "%Sm" .smart-env/smart_sources.json

# 2. Verify file modifications
find .claude -name "*.md" -mtime -1

# 3. Check for embedding staleness
python scripts/check_embedding_freshness.py
```

**Solutions**:

1. **Force refresh after file changes**:
   ```typescript
   // Add file watcher to mcp-server
   fs.watch(vaultPath, { recursive: true }, (event, filename) => {
     if (filename.endsWith('.md')) {
       scheduleEmbeddingRefresh();
     }
   });
   ```

2. **Verify semantic similarity**:
   ```python
   # Test query
   query = "authentication security"
   results = mcp_client.call_tool("lookup", {"query": query})
   
   for r in results:
       print(f"{r['score']:.3f}: {r['file']}")
   ```

3. **Adjust threshold**:
   ```json
   {
     "threshold": 0.3  // Lower = more results, higher = more precise
   }
   ```

---

## 4. Query Anchor System

### 4.1 Query Anchor Syntax

**Query anchors** are special markers embedded in memory files that make specific sections highly discoverable.

**Syntax**: `%%QA:domain:topic%%`

**Example**:

```markdown
# Authentication System

%%QA:auth:flow%%
The user authentication flow follows OAuth 2.0 with PKCE extension:

1. Client requests authorization code
2. User authenticates with identity provider
3. Authorization code exchanged for tokens
4. Access token used for API requests
5. Refresh token used to obtain new access tokens

%%QA:auth:tokens%%
Token management strategy:
- Access tokens: 15-minute expiry
- Refresh tokens: 7-day expiry with rotation
- Token storage: httpOnly cookies for web, secure storage for mobile

%%QA:auth:security%%
Security measures implemented:
- PKCE for mobile apps (prevents code interception)
- Token rotation on refresh
- Device fingerprinting
- Rate limiting on authentication endpoints
```

**Benefits**:

1. **Targeted Retrieval**: Query "auth flow" finds exactly the right section
2. **Organizational**: Anchors act as semantic bookmarks
3. **Discoverable**: Easy to see what topics are covered
4. **Composable**: Multiple anchors can target same content

### 4.2 Anchor Naming Conventions

**Best practices for anchor names**:

```
%%QA:{domain}:{topic}:{subtopic}%%

Examples:
%%QA:auth:flow:oauth%%
%%QA:auth:tokens:refresh%%
%%QA:db:schema:users%%
%%QA:api:endpoints:create-user%%
%%QA:deploy:strategy:blue-green%%
```

**Domain Categories**:

| Domain | Description | Examples |
|--------|-------------|----------|
| `auth` | Authentication & authorization | `auth:flow`, `auth:tokens`, `auth:rbac` |
| `db` | Database & data model | `db:schema`, `db:queries`, `db:migration` |
| `api` | API design & endpoints | `api:rest`, `api:graphql`, `api:versioning` |
| `deploy` | Deployment & operations | `deploy:strategy`, `deploy:rollback`, `deploy:monitoring` |
| `test` | Testing strategies | `test:unit`, `test:integration`, `test:e2e` |
| `perf` | Performance optimization | `perf:caching`, `perf:queries`, `perf:bundling` |
| `sec` | Security practices | `sec:encryption`, `sec:validation`, `sec:audit` |

### 4.3 Strategic Anchor Placement

**Where to place anchors**:

```python
def should_add_anchor(section_content: str) -> bool:
    """
    Determine if section warrants a query anchor.
    
    Add anchor if section:
    - Explains a key concept or pattern
    - Documents a critical decision
    - Describes an implementation approach
    - Provides troubleshooting guidance
    - Contains reusable knowledge
    """
    
    # Add anchor if:
    return (
        len(section_content) > 200 and  # Substantial content
        (
            "how to" in section_content.lower() or
            "approach" in section_content.lower() or
            "pattern" in section_content.lower() or
            "implementation" in section_content.lower() or
            "decision" in section_content.lower()
        )
    )
```

**Example: Anchored systemPatterns.md**:

```markdown
# System Patterns

## Authentication

%%QA:auth:pattern:jwt%%
### JWT Authentication Pattern

**Decision**: Use JWT access tokens + refresh tokens

**Rationale**:
- Stateless: Scales horizontally without session store
- Microservices-friendly: Works across service boundaries
- Mobile-compatible: Tokens stored locally

%%QA:auth:implementation:pkce%%
### PKCE Implementation

**What**: Proof Key for Code Exchange prevents authorization code interception

**Why**: Mobile apps can't securely store client secrets

**How**:
1. Generate code verifier (random string)
2. Create code challenge (SHA256 hash of verifier)
3. Send challenge with authorization request
4. Send verifier with token request
5. Server validates challenge matches verifier

%%QA:auth:security:token-rotation%%
### Token Rotation Strategy

**Problem**: Long-lived refresh tokens pose security risk

**Solution**: Rotate refresh tokens on each use

**Implementation**:
- Client uses refresh token to get new access token
- Server issues NEW refresh token, invalidates old one
- If old token reused → security breach detected → revoke all tokens

## Database

%%QA:db:pattern:per-service%%
### Database per Service Pattern

**Decision**: Each microservice owns its database

**Rationale**:
- Loose coupling: Services evolve independently
- Technology fit: Use optimal DB for each use case
- Scalability: Independent DB scaling

%%QA:db:challenge:consistency%%
### Eventual Consistency Challenge

**Problem**: No cross-service transactions

**Solution**: Event sourcing + Saga pattern

**Trade-off**: Accept eventual consistency for autonomy
```

### 4.4 Anchor-Based Search

**Searching with query anchors**:

```python
class AnchorSearch:
    """Search using query anchors for targeted retrieval."""
    
    def __init__(self, vault_path: Path):
        self.vault_path = Path(vault_path)
    
    def search_anchors(
        self,
        domain: str = None,
        topic: str = None,
        subtopic: str = None
    ) -> List[Dict]:
        """
        Search for query anchors.
        
        Args:
            domain: Domain filter (e.g., 'auth')
            topic: Topic filter (e.g., 'flow')
            subtopic: Subtopic filter (e.g., 'oauth')
        
        Returns:
            List of matching anchor locations with content
        """
        
        # Build search pattern
        pattern_parts = ["%%QA"]
        if domain:
            pattern_parts.append(domain)
        if topic:
            pattern_parts.append(topic)
        if subtopic:
            pattern_parts.append(subtopic)
        
        pattern = ":".join(pattern_parts) + (":" if len(pattern_parts) < 4 else "")
        
        results = []
        
        # Search all memory files
        for file_path in self.vault_path.glob(".claude/**/*.md"):
            content = file_path.read_text()
            
            # Find all anchors matching pattern
            for match in re.finditer(rf'{re.escape(pattern)}[^%]*%%', content):
                anchor = match.group()
                
                # Extract content after anchor (next 500 chars)
                start = match.end()
                end = min(start + 500, len(content))
                section_content = content[start:end]
                
                results.append({
                    'file': str(file_path.relative_to(self.vault_path)),
                    'anchor': anchor.strip('%'),
                    'content': section_content,
                    'position': match.start()
                })
        
        return results
    
    def search_by_query(self, query: str) -> List[Dict]:
        """
        Search anchors using natural language query.
        
        Converts query to anchor pattern:
        - "auth flow" → %%QA:auth:flow%%
        - "database per service" → %%QA:db:*:per-service%%
        """
        
        # Extract domain and topic from query
        domain, topic = self._parse_query(query)
        
        return self.search_anchors(domain=domain, topic=topic)
    
    def _parse_query(self, query: str) -> Tuple[str, str]:
        """Parse query into domain and topic."""
        
        # Domain keywords
        domain_keywords = {
            'auth': ['auth', 'authentication', 'login', 'security'],
            'db': ['database', 'data', 'schema', 'query'],
            'api': ['api', 'endpoint', 'rest', 'graphql'],
            'deploy': ['deploy', 'deployment', 'release'],
        }
        
        query_lower = query.lower()
        
        # Find matching domain
        domain = None
        for dom, keywords in domain_keywords.items():
            if any(kw in query_lower for kw in keywords):
                domain = dom
                break
        
        # Extract topic (remaining words)
        topic = query_lower
        if domain:
            for kw in domain_keywords[domain]:
                topic = topic.replace(kw, '').strip()
        
        return domain, topic


# Example usage
searcher = AnchorSearch(Path("/path/to/vault"))

# Search by domain
auth_anchors = searcher.search_anchors(domain="auth")
print(f"Found {len(auth_anchors)} auth-related anchors")

# Search by domain + topic
token_anchors = searcher.search_anchors(domain="auth", topic="tokens")
print(f"Found {len(token_anchors)} token-related anchors")

# Natural language search
results = searcher.search_by_query("authentication flow")
for result in results:
    print(f"{result['file']}: {result['anchor']}")
```

### 4.5 Dynamic Anchor Generation

**Automatically generate anchors for existing content**:

```python
import re
from typing import List, Tuple

class AnchorGenerator:
    """Generate query anchors for existing content."""
    
    def __init__(self):
        # Patterns that indicate anchorable content
        self.anchor_patterns = [
            (r'##\s+([^#\n]+)', 'section_heading'),
            (r'\*\*Decision\*\*:', 'decision'),
            (r'\*\*Pattern\*\*:', 'pattern'),
            (r'\*\*Implementation\*\*:', 'implementation'),
            (r'\*\*Problem\*\*:', 'problem'),
        ]
    
    def generate_anchors(self, file_path: Path) -> List[Tuple[int, str]]:
        """
        Generate anchor suggestions for file.
        
        Returns:
            List of (line_number, suggested_anchor) tuples
        """
        
        content = file_path.read_text()
        lines = content.split('\n')
        
        suggestions = []
        
        # Detect domain from file path
        domain = self._detect_domain(file_path)
        
        # Find sections that should have anchors
        for i, line in enumerate(lines):
            # Check if line matches anchor patterns
            for pattern, pattern_type in self.anchor_patterns:
                if re.match(pattern, line):
                    topic = self._extract_topic(line, pattern_type)
                    
                    # Generate anchor
                    anchor = self._build_anchor(domain, topic, pattern_type)
                    
                    # Check if anchor already exists nearby
                    if not self._has_anchor_nearby(lines, i):
                        suggestions.append((i, anchor))
        
        return suggestions
    
    def _detect_domain(self, file_path: Path) -> str:
        """Detect domain from file path or content."""
        
        path_str = str(file_path).lower()
        
        if 'auth' in path_str:
            return 'auth'
        elif 'database' in path_str or 'db' in path_str:
            return 'db'
        elif 'api' in path_str:
            return 'api'
        elif 'deploy' in path_str:
            return 'deploy'
        
        return 'general'
    
    def _extract_topic(self, line: str, pattern_type: str) -> str:
        """Extract topic from line."""
        
        # Remove markdown formatting
        topic = re.sub(r'[#*]', '', line).strip()
        
        # Remove pattern prefix
        topic = re.sub(r'Decision:|Pattern:|Implementation:|Problem:', '', topic).strip()
        
        # Convert to lowercase, replace spaces with hyphens
        topic = topic.lower().replace(' ', '-')
        
        return topic
    
    def _build_anchor(self, domain: str, topic: str, pattern_type: str) -> str:
        """Build anchor string."""
        
        # Shorten topic if too long
        topic_parts = topic.split('-')[:3]  # Max 3 words
        topic_short = '-'.join(topic_parts)
        
        return f"%%QA:{domain}:{topic_short}:%%"
    
    def _has_anchor_nearby(self, lines: List[str], line_num: int, window: int = 3) -> bool:
        """Check if anchor exists within window of lines."""
        
        start = max(0, line_num - window)
        end = min(len(lines), line_num + window)
        
        for i in range(start, end):
            if '%%QA:' in lines[i]:
                return True
        
        return False
    
    def apply_suggestions(
        self,
        file_path: Path,
        suggestions: List[Tuple[int, str]]
    ) -> Path:
        """
        Apply anchor suggestions to file.
        
        Returns:
            Path to modified file
        """
        
        lines = file_path.read_text().split('\n')
        
        # Apply suggestions in reverse order (to preserve line numbers)
        for line_num, anchor in reversed(suggestions):
            # Insert anchor before the line
            lines.insert(line_num, anchor)
        
        # Write back to file
        file_path.write_text('\n'.join(lines))
        
        return file_path


# Example usage
generator = AnchorGenerator()

# Generate suggestions
suggestions = generator.generate_anchors(
    Path(".claude/core/systemPatterns.md")
)

print(f"Generated {len(suggestions)} anchor suggestions:")
for line_num, anchor in suggestions:
    print(f"  Line {line_num}: {anchor}")

# Apply suggestions
if input("Apply suggestions? (y/n): ").lower() == 'y':
    generator.apply_suggestions(
        Path(".claude/core/systemPatterns.md"),
        suggestions
    )
    print("✓ Anchors added")
```

---

## 5. Hybrid Retrieval Strategies

**Combining keyword search + semantic search for best results**

### 5.1 Why Hybrid Retrieval?

**Limitations of pure approaches**:

| Approach | Strengths | Weaknesses |
|----------|-----------|------------|
| **Keyword Only** | ✅ Exact matches<br>✅ Fast<br>✅ Simple | ❌ Misses synonyms<br>❌ No semantic understanding<br>❌ Word order matters |
| **Semantic Only** | ✅ Finds related content<br>✅ Synonym-aware<br>✅ Context-sensitive | ❌ May miss exact terms<br>❌ Slower<br>❌ Less predictable |
| **Hybrid** | ✅ Best of both<br>✅ Tunable balance<br>✅ Robust | ❌ More complex<br>❌ Requires tuning |

**Example where each fails**:

```
Query: "JWT token refresh mechanism"

Keyword search finds:
- ✓ Documents mentioning "JWT", "token", "refresh"
- ✗ Misses: "authentication renewal process" (same concept, different words)

Semantic search finds:
- ✓ Documents about authentication renewal
- ✓ OAuth token management
- ✗ May rank generic auth docs higher than specific JWT docs

Hybrid search finds:
- ✓ JWT-specific documents (keyword boost)
- ✓ Related authentication concepts (semantic)
- ✓ Best balance of precision and recall
```

### 5.2 BM25 Keyword Search

**BM25** (Best Matching 25) is the industry-standard keyword search algorithm.

```python
import math
from collections import Counter
from typing import List, Dict

class BM25:
    """BM25 keyword search algorithm."""
    
    def __init__(self, k1: float = 1.5, b: float = 0.75):
        """
        Initialize BM25.
        
        Args:
            k1: Term frequency saturation parameter (1.2-2.0)
            b: Length normalization parameter (0-1)
        """
        self.k1 = k1
        self.b = b
        self.corpus_size = 0
        self.avgdl = 0
        self.doc_freqs = []
        self.idf = {}
        self.doc_len = []
        self.documents = []
    
    def fit(self, documents: List[str]):
        """
        Build BM25 index from documents.
        
        Args:
            documents: List of document texts
        """
        self.corpus_size = len(documents)
        self.documents = documents
        
        # Calculate document lengths
        self.doc_len = [len(doc.split()) for doc in documents]
        self.avgdl = sum(self.doc_len) / self.corpus_size
        
        # Calculate document frequencies
        df = {}
        for doc in documents:
            words = set(doc.lower().split())
            for word in words:
                df[word] = df.get(word, 0) + 1
        
        # Calculate IDF (Inverse Document Frequency)
        for word, freq in df.items():
            self.idf[word] = math.log(
                (self.corpus_size - freq + 0.5) / (freq + 0.5) + 1
            )
    
    def search(self, query: str, top_k: int = 10) -> List[Tuple[int, float]]:
        """
        Search documents using BM25.
        
        Args:
            query: Search query
            top_k: Number of results to return
        
        Returns:
            List of (doc_index, score) tuples
        """
        query_words = query.lower().split()
        
        scores = []
        
        for doc_idx, doc in enumerate(self.documents):
            doc_words = doc.lower().split()
            word_counts = Counter(doc_words)
            
            score = 0
            for word in query_words:
                if word not in self.idf:
                    continue
                
                # Term frequency in document
                tf = word_counts[word]
                
                # BM25 formula
                idf = self.idf[word]
                numerator = tf * (self.k1 + 1)
                denominator = tf + self.k1 * (
                    1 - self.b + self.b * (self.doc_len[doc_idx] / self.avgdl)
                )
                
                score += idf * (numerator / denominator)
            
            scores.append((doc_idx, score))
        
        # Sort by score (highest first)
        scores.sort(key=lambda x: x[1], reverse=True)
        
        return scores[:top_k]


# Example usage
documents = [
    "JWT authentication with refresh tokens",
    "OAuth 2.0 authorization flow",
    "User login and session management",
    "Database query optimization strategies",
]

bm25 = BM25()
bm25.fit(documents)

results = bm25.search("JWT token refresh", top_k=3)

for doc_idx, score in results:
    print(f"Score {score:.3f}: {documents[doc_idx]}")
```

### 5.3 Reciprocal Rank Fusion

**RRF** combines rankings from multiple search methods.

```python
from typing import List, Dict, Tuple

class ReciprocalRankFusion:
    """
    Reciprocal Rank Fusion for combining search results.
    
    Paper: "Reciprocal Rank Fusion outperforms Condorcet and individual Rank Learning Methods"
    """
    
    def __init__(self, k: int = 60):
        """
        Initialize RRF.
        
        Args:
            k: Constant for RRF formula (typically 60)
        """
        self.k = k
    
    def fuse(
        self,
        rankings: List[List[Tuple[str, float]]],
        weights: List[float] = None
    ) -> List[Tuple[str, float]]:
        """
        Fuse multiple rankings using RRF.
        
        Args:
            rankings: List of rankings (each is list of (doc_id, score))
            weights: Optional weights for each ranking
        
        Returns:
            Fused ranking
        """
        if weights is None:
            weights = [1.0] * len(rankings)
        
        # Calculate RRF scores
        rrf_scores = {}
        
        for ranking, weight in zip(rankings, weights):
            for rank, (doc_id, _) in enumerate(ranking, start=1):
                rrf_score = weight / (self.k + rank)
                
                if doc_id in rrf_scores:
                    rrf_scores[doc_id] += rrf_score
                else:
                    rrf_scores[doc_id] = rrf_score
        
        # Sort by RRF score
        fused = sorted(
            rrf_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        return fused


# Example usage
keyword_results = [
    ("doc1", 0.95),
    ("doc2", 0.87),
    ("doc3", 0.76),
]

semantic_results = [
    ("doc2", 0.92),
    ("doc4", 0.88),
    ("doc1", 0.81),
]

rrf = ReciprocalRankFusion(k=60)

fused_results = rrf.fuse(
    [keyword_results, semantic_results],
    weights=[0.4, 0.6]  # 40% keyword, 60% semantic
)

print("Fused rankings:")
for doc_id, score in fused_results:
    print(f"  {doc_id}: {score:.4f}")
```

### 5.4 Complete Hybrid Search Implementation

**Production-ready hybrid search system**:

```python
from pathlib import Path
from typing import List, Dict, Tuple
import numpy as np

class HybridSearch:
    """
    Hybrid search combining BM25 keyword search + semantic search.
    """
    
    def __init__(
        self,
        embedding_generator: EmbeddingGenerator,
        vault_path: Path,
        alpha: float = 0.5
    ):
        """
        Initialize hybrid search.
        
        Args:
            embedding_generator: For generating query embeddings
            vault_path: Path to vault
            alpha: Balance between keyword (0) and semantic (1)
                   0.0 = pure keyword
                   0.5 = balanced
                   1.0 = pure semantic
        """
        self.embedding_gen = embedding_generator
        self.vault_path = Path(vault_path)
        self.alpha = alpha
        
        # Initialize BM25
        self.bm25 = BM25()
        
        # Initialize vector index
        self.vector_index = VectorIndex(dimensions=embedding_generator.dimensions)
        
        # Load and index documents
        self._index_documents()
    
    def _index_documents(self):
        """Index all memory documents."""
        
        documents = []
        document_paths = []
        
        # Load all memory files
        for file_path in self.vault_path.glob(".claude/**/*.md"):
            content = file_path.read_text()
            
            # Remove frontmatter
            content_clean = self._remove_frontmatter(content)
            
            documents.append(content_clean)
            document_paths.append(str(file_path.relative_to(self.vault_path)))
            
            # Generate and add embedding
            embedding = self.embedding_gen.encode_text(content_clean)
            self.vector_index.add(embedding, {'path': document_paths[-1]})
        
        # Build BM25 index
        self.bm25.fit(documents)
        
        self.documents = documents
        self.document_paths = document_paths
        
        print(f"✓ Indexed {len(documents)} documents")
    
    def search(
        self,
        query: str,
        top_k: int = 10,
        rerank: bool = True
    ) -> List[Dict]:
        """
        Hybrid search.
        
        Args:
            query: Search query
            top_k: Number of results
            rerank: Use RRF for fusion (vs simple weighted average)
        
        Returns:
            List of search results with scores
        """
        
        # 1. Keyword search (BM25)
        keyword_results = self.bm25.search(query, top_k=top_k * 2)
        
        # 2. Semantic search
        query_embedding = self.embedding_gen.encode_text(query)
        semantic_results = self.vector_index.search(
            query_embedding,
            top_k=top_k * 2,
            threshold=0.0
        )
        
        # 3. Fuse results
        if rerank:
            final_results = self._fuse_rrf(keyword_results, semantic_results, top_k)
        else:
            final_results = self._fuse_weighted(keyword_results, semantic_results, top_k)
        
        return final_results
    
    def _fuse_rrf(
        self,
        keyword_results: List[Tuple[int, float]],
        semantic_results: List[Tuple[Dict, float]],
        top_k: int
    ) -> List[Dict]:
        """Fuse using Reciprocal Rank Fusion."""
        
        # Convert to common format
        keyword_rankings = [
            (self.document_paths[idx], score)
            for idx, score in keyword_results
        ]
        
        semantic_rankings = [
            (result['path'], score)
            for result, score in semantic_results
        ]
        
        # Apply RRF
        rrf = ReciprocalRankFusion(k=60)
        fused = rrf.fuse(
            [keyword_rankings, semantic_rankings],
            weights=[1 - self.alpha, self.alpha]
        )
        
        # Format results
        results = []
        for path, score in fused[:top_k]:
            # Find document index
            doc_idx = self.document_paths.index(path)
            
            results.append({
                'path': path,
                'score': score,
                'preview': self.documents[doc_idx][:200] + "..."
            })
        
        return results
    
    def _fuse_weighted(
        self,
        keyword_results: List[Tuple[int, float]],
        semantic_results: List[Tuple[Dict, float]],
        top_k: int
    ) -> List[Dict]:
        """Fuse using weighted average."""
        
        # Normalize scores to 0-1
        keyword_scores = self._normalize_scores([s for _, s in keyword_results])
        semantic_scores = self._normalize_scores([s for _, s in semantic_results])
        
        # Combine scores
        combined = {}
        
        # Add keyword scores
        for (idx, _), norm_score in zip(keyword_results, keyword_scores):
            path = self.document_paths[idx]
            combined[path] = (1 - self.alpha) * norm_score
        
        # Add semantic scores
        for (result, _), norm_score in zip(semantic_results, semantic_scores):
            path = result['path']
            if path in combined:
                combined[path] += self.alpha * norm_score
            else:
                combined[path] = self.alpha * norm_score
        
        # Sort and return top k
        sorted_results = sorted(
            combined.items(),
            key=lambda x: x[1],
            reverse=True
        )[:top_k]
        
        # Format results
        results = []
        for path, score in sorted_results:
            doc_idx = self.document_paths.index(path)
            
            results.append({
                'path': path,
                'score': score,
                'preview': self.documents[doc_idx][:200] + "..."
            })
        
        return results
    
    def _normalize_scores(self, scores: List[float]) -> List[float]:
        """Normalize scores to 0-1 range."""
        
        if not scores:
            return []
        
        min_score = min(scores)
        max_score = max(scores)
        
        if max_score == min_score:
            return [1.0] * len(scores)
        
        return [
            (score - min_score) / (max_score - min_score)
            for score in scores
        ]
    
    def _remove_frontmatter(self, content: str) -> str:
        """Remove YAML frontmatter."""
        
        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                return content[end + 3:].strip()
        
        return content


# Example usage
embedding_gen = EmbeddingGenerator()
hybrid = HybridSearch(
    embedding_generator=embedding_gen,
    vault_path=Path("/path/to/vault"),
    alpha=0.6  # 60% semantic, 40% keyword
)

results = hybrid.search("JWT token refresh mechanism", top_k=5)

print("Hybrid search results:")
for i, result in enumerate(results, 1):
    print(f"\n{i}. {result['path']} (score: {result['score']:.4f})")
    print(f"   {result['preview']}")
```

### 5.5 Tuning Hybrid Search Parameters

**Optimizing the alpha parameter**:

```python
def evaluate_search_quality(
    hybrid_search: HybridSearch,
    test_queries: List[Dict[str, any]],
    alpha_values: List[float]
) -> Dict[float, float]:
    """
    Evaluate hybrid search quality across different alpha values.
    
    Args:
        hybrid_search: HybridSearch instance
        test_queries: List of {"query": str, "relevant_docs": List[str]}
        alpha_values: Alpha values to test
    
    Returns:
        Dict mapping alpha to mean average precision (MAP)
    """
    
    results = {}
    
    for alpha in alpha_values:
        hybrid_search.alpha = alpha
        
        precisions = []
        
        for test in test_queries:
            query = test['query']
            relevant_docs = set(test['relevant_docs'])
            
            # Search
            search_results = hybrid_search.search(query, top_k=10)
            
            # Calculate precision
            retrieved_docs = [r['path'] for r in search_results]
            
            # Average precision
            ap = 0
            relevant_found = 0
            
            for i, doc in enumerate(retrieved_docs, 1):
                if doc in relevant_docs:
                    relevant_found += 1
                    precision_at_i = relevant_found / i
                    ap += precision_at_i
            
            ap /= len(relevant_docs) if relevant_docs else 1
            precisions.append(ap)
        
        # Mean average precision
        results[alpha] = sum(precisions) / len(precisions)
    
    return results


# Example: Find optimal alpha
test_queries = [
    {
        "query": "JWT authentication",
        "relevant_docs": [
            ".claude/core/systemPatterns.md",
            ".claude/task-logs/2025-12-27-1000-jwt-auth.md"
        ]
    },
    {
        "query": "database migration strategy",
        "relevant_docs": [
            ".claude/task-logs/2025-12-26-0900-db-migration.md"
        ]
    }
]

alpha_values = [0.0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0]

map_scores = evaluate_search_quality(hybrid, test_queries, alpha_values)

print("Alpha tuning results (MAP scores):")
for alpha, map_score in sorted(map_scores.items()):
    print(f"  α={alpha:.1f}: {map_score:.3f}")

# Use best alpha
best_alpha = max(map_scores.items(), key=lambda x: x[1])[0]
print(f"\n✓ Optimal alpha: {best_alpha}")
```

---

## 6. Integration with Advanced Memory

**Bringing it all together**: Smart Connections + MCP + Advanced Memory

### 6.1 Enhanced Session Start

**Automatic semantic context loading**:

```python
def on_session_start_with_semantic(context: EventContext):
    """
    Enhanced session start with semantic retrieval.
    
    Extends Document 17's on_session_start with semantic capabilities.
    """
    
    memory_path = Path(".claude")
    
    # 1. Standard memory loading (from Document 17)
    print("Loading structural memory...")
    
    # Load .clinerules
    rules = load_rules()
    
    # Load activeContext.md
    active_context = load_active_context(memory_path)
    
    # Verify integrity
    verify_memory_integrity(memory_path)
    
    # 2. SEMANTIC ENHANCEMENT - Load relevant context
    print("\nEnhancing with semantic retrieval...")
    
    # Extract current focus from activeContext
    current_focus = extract_current_focus(active_context)
    
    if current_focus:
        # Use MCP to find semantically related content
        semantic_context = mcp_client.call_tool(
            "lookup",
            {
                "query": current_focus,
                "limit": 5,
                "threshold": 0.5
            }
        )
        
        print(f"✓ Found {len(semantic_context['results'])} related notes:")
        for result in semantic_context['results']:
            print(f"  - {result['file']} (similarity: {result['score']:.2f})")
    
    # 3. Load connected notes for key files
    print("\nFinding connected notes...")
    
    core_files = [
        ".claude/core/systemPatterns.md",
        ".claude/core/activeContext.md"
    ]
    
    for core_file in core_files:
        connections = mcp_client.call_tool(
            "connection",
            {
                "file_path": core_file,
                "limit": 3
            }
        )
        
        print(f"✓ {core_file} connected to:")
        for conn in connections['results']:
            print(f"  - {conn['file']}")
    
    # 4. Synthesize loaded context
    session_context = {
        'session_id': context.session_id,
        'structural_context': active_context,
        'semantic_context': semantic_context,
        'connections': connections,
        'ready': True
    }
    
    print(f"\n{'='*60}")
    print("Session initialized with semantic enhancement")
    print(f"Loaded: {len(semantic_context['results'])} semantic matches")
    print(f"Connected: {len(connections['results'])} related notes")
    print(f"{'='*60}\n")
    
    return session_context
```

### 6.2 Semantic Task Planning

**Use semantic search to inform implementation plans**:

```python
def create_implementation_plan_with_context(
    task_description: str,
    memory_path: Path,
    mcp_client
) -> Dict:
    """
    Create implementation plan enhanced with semantic context.
    
    Steps:
    1. Search for similar past tasks
    2. Find relevant patterns
    3. Identify related errors
    4. Generate informed plan
    """
    
    print(f"Creating plan for: {task_description}")
    print("=" * 60)
    
    # 1. Search for similar tasks
    print("\n1. Searching for similar past tasks...")
    
    similar_tasks = mcp_client.call_tool(
        "lookup",
        {
            "query": f"task: {task_description}",
            "limit": 3,
            "threshold": 0.6
        }
    )
    
    if similar_tasks['results']:
        print(f"✓ Found {len(similar_tasks['results'])} similar tasks:")
        for task in similar_tasks['results']:
            print(f"  - {task['file']}")
    
    # 2. Find relevant architectural patterns
    print("\n2. Finding relevant patterns...")
    
    patterns = mcp_client.call_tool(
        "lookup",
        {
            "query": f"pattern: {task_description}",
            "limit": 2,
            "threshold": 0.5
        }
    )
    
    # 3. Check for related errors
    print("\n3. Checking for related errors...")
    
    related_errors = mcp_client.call_tool(
        "lookup",
        {
            "query": f"error: {task_description}",
            "limit": 2,
            "threshold": 0.4
        }
    )
    
    # 4. Generate informed plan
    print("\n4. Generating implementation plan...")
    
    plan = {
        'task': task_description,
        'similar_tasks': similar_tasks['results'],
        'relevant_patterns': patterns['results'],
        'known_pitfalls': related_errors['results'],
        'phases': []
    }
    
    # Add preparation phase
    plan['phases'].append({
        'name': 'Preparation',
        'steps': [
            f"Review similar task: {similar_tasks['results'][0]['file']}"
            if similar_tasks['results'] else "Research best practices",
            
            f"Apply pattern: {patterns['results'][0]['file']}"
            if patterns['results'] else "Design approach",
            
            f"Avoid error: {related_errors['results'][0]['file']}"
            if related_errors['results'] else "Identify risks"
        ]
    })
    
    # Add implementation phase
    plan['phases'].append({
        'name': 'Implementation',
        'steps': [
            "Write failing tests (TDD)",
            "Implement core functionality",
            "Refactor for quality"
        ]
    })
    
    # Add validation phase
    plan['phases'].append({
        'name': 'Validation',
        'steps': [
            "Run test suite",
            "Performance testing",
            "Security review"
        ]
    })
    
    print("\n✓ Plan created with semantic context")
    print(f"  Learned from {len(similar_tasks['results'])} similar tasks")
    print(f"  Applying {len(patterns['results'])} relevant patterns")
    print(f"  Avoiding {len(related_errors['results'])} known pitfalls")
    
    return plan
```

### 6.3 Intelligent Error Recovery

**Use semantic search to find similar error resolutions**:

```python
def on_error_detected_with_semantic(
    context: EventContext,
    mcp_client
):
    """
    Enhanced error detection with semantic error matching.
    
    Extends Document 17's on_error_detected with semantic capabilities.
    """
    
    memory_path = Path(".claude")
    error_info = context.data
    
    error_type = error_info.get('type', 'unknown')
    error_message = error_info.get('message', '')
    
    print(f"\n{'='*60}")
    print(f"ERROR DETECTED: {error_type}")
    print(f"{'='*60}\n")
    
    # 1. Document error (from Document 17)
    error_file = memory_path / "errors" / generate_error_filename(error_type)
    error_doc = create_error_document(error_info)
    save_memory_file(error_file, error_doc)
    
    # 2. SEMANTIC SEARCH for similar errors
    print("Searching for similar errors semantically...")
    
    semantic_matches = mcp_client.call_tool(
        "lookup",
        {
            "query": f"error: {error_type} {error_message}",
            "limit": 5,
            "threshold": 0.6
        }
    )
    
    # 3. Analyze matches for resolution patterns
    resolutions = []
    
    for match in semantic_matches['results']:
        if 'errors/' in match['file']:
            # Extract resolution from error file
            error_content = load_file_content(memory_path / match['file'])
            resolution = extract_resolution(error_content)
            
            if resolution:
                resolutions.append({
                    'source': match['file'],
                    'resolution': resolution,
                    'similarity': match['score']
                })
    
    # 4. Apply most relevant resolution
    if resolutions:
        best_resolution = resolutions[0]
        
        print(f"\n✓ Found similar error with resolution:")
        print(f"  Source: {best_resolution['source']}")
        print(f"  Similarity: {best_resolution['similarity']:.2f}")
        print(f"  Resolution: {best_resolution['resolution']}")
        
        # Attempt automatic recovery
        success = apply_recovery_strategy(
            best_resolution['resolution'],
            error_info
        )
        
        if success:
            print(f"\n✓ Automatic recovery successful!")
            update_error_document(error_file, resolution=best_resolution['resolution'], status='auto-resolved')
        else:
            print(f"\n✗ Automatic recovery failed - manual intervention needed")
    else:
        print("\n⚠ No similar errors found - this appears to be a new error pattern")
    
    return {
        'error_file': error_file,
        'semantic_matches': semantic_matches['results'],
        'resolutions_found': len(resolutions),
        'auto_recovered': success if resolutions else False
    }
```

### 6.4 Memory Update Verification

**Verify memory updates are semantically indexed**:

```python
class SemanticMemoryManager:
    """
    Manages memory with semantic verification.
    
    Ensures all memory updates are properly embedded and searchable.
    """
    
    def __init__(self, memory_path: Path, mcp_client):
        self.memory_path = Path(memory_path)
        self.mcp = mcp_client
    
    def update_memory_file(
        self,
        file_path: Path,
        content: str,
        verify_embedding: bool = True
    ):
        """
        Update memory file and verify embedding.
        
        Args:
            file_path: Path to memory file
            content: New content
            verify_embedding: Wait for and verify embedding generation
        """
        
        # Write file
        file_path.write_text(content)
        print(f"✓ Updated: {file_path}")
        
        if verify_embedding:
            # Wait for Smart Connections to generate embedding
            print("  Waiting for embedding generation...")
            time.sleep(5)  # Give Smart Connections time to process
            
            # Verify embedding exists
            rel_path = str(file_path.relative_to(self.memory_path.parent))
            
            validation = self.mcp.call_tool(
                "validate",
                {"file_paths": [rel_path]}
            )
            
            if validation['results'][0]['exists']:
                print(f"  ✓ Embedding generated and indexed")
            else:
                print(f"  ⚠ Embedding not yet generated - may need manual refresh")
    
    def verify_semantic_accessibility(
        self,
        key_concepts: List[str]
    ) -> Dict[str, bool]:
        """
        Verify key concepts are semantically discoverable.
        
        Args:
            key_concepts: List of concepts that should be findable
        
        Returns:
            Dict mapping concept to whether it's discoverable
        """
        
        results = {}
        
        for concept in key_concepts:
            # Search for concept
            search_results = self.mcp.call_tool(
                "lookup",
                {
                    "query": concept,
                    "limit": 5,
                    "threshold": 0.3
                }
            )
            
            # Check if any results found
            discoverable = len(search_results['results']) > 0
            results[concept] = discoverable
            
            if discoverable:
                print(f"✓ '{concept}' is semantically discoverable")
                print(f"  Top result: {search_results['results'][0]['file']}")
            else:
                print(f"✗ '{concept}' not easily discoverable")
        
        return results


# Example usage
memory_mgr = SemanticMemoryManager(
    memory_path=Path(".claude"),
    mcp_client=mcp_client
)

# Update a memory file
memory_mgr.update_memory_file(
    file_path=Path(".claude/core/systemPatterns.md"),
    content=updated_patterns_content,
    verify_embedding=True
)

# Verify key concepts are discoverable
key_concepts = [
    "JWT authentication",
    "database per service",
    "event sourcing"
]

accessibility = memory_mgr.verify_semantic_accessibility(key_concepts)

if all(accessibility.values()):
    print("\n✓ All key concepts are semantically accessible")
else:
    missing = [c for c, accessible in accessibility.items() if not accessible]
    print(f"\n⚠ Some concepts not discoverable: {missing}")
```

### 6.5 Complete Integration Example

**Full workflow with semantic memory**:

```python
#!/usr/bin/env python3
"""
Complete SPES workflow with semantic memory integration.
"""

from pathlib import Path
from advanced_memory import SPESAdvancedMemory
from semantic_memory import SemanticMemoryManager, HybridSearch, MCPClient

def main():
    """Complete workflow example."""
    
    # Initialize systems
    memory = SPESAdvancedMemory(memory_path=".claude")
    mcp = MCPClient(vault_path="/path/to/vault")
    semantic_mgr = SemanticMemoryManager(
        memory_path=Path(".claude"),
        mcp_client=mcp
    )
    
    # 1. START SESSION with semantic enhancement
    print("\n" + "="*60)
    print("STARTING SESSION")
    print("="*60)
    
    session_id = memory.start_session()
    
    # Get semantic context
    current_focus = "implementing user authentication"
    
    semantic_context = mcp.call_tool(
        "lookup",
        {"query": current_focus, "limit": 5}
    )
    
    print(f"\nFound {len(semantic_context['results'])} related notes")
    
    # 2. START TASK with semantic planning
    print("\n" + "="*60)
    print("STARTING TASK")
    print("="*60)
    
    task_description = "Implement JWT authentication with refresh tokens"
    
    # Create plan informed by semantic search
    plan = create_implementation_plan_with_context(
        task_description=task_description,
        memory_path=Path(".claude"),
        mcp_client=mcp
    )
    
    task_id = memory.start_task(
        description=task_description,
        acceptance_criteria=["JWT generation", "Token validation", "Refresh mechanism"],
        dependencies=["PyJWT library"]
    )
    
    # 3. WORK (with semantic assistance available)
    print("\n" + "="*60)
    print("WORKING ON TASK")
    print("="*60)
    
    # Simulate work...
    
    # If error occurs, use semantic error matching
    try:
        # Some code that might fail
        pass
    except Exception as e:
        on_error_detected_with_semantic(
            context=EventContext(
                event=MemoryEvent.ERROR_DETECTED,
                data={
                    'type': 'authentication_error',
                    'message': str(e),
                    'stack_trace': traceback.format_exc()
                }
            ),
            mcp_client=mcp
        )
    
    # 4. COMPLETE TASK
    print("\n" + "="*60)
    print("COMPLETING TASK")
    print("="*60)
    
    memory.complete_task(
        task_id=task_id,
        criteria_met=["JWT generation", "Token validation", "Refresh mechanism"],
        test_coverage=85.0,
        documentation_updated=True
    )
    
    # 5. VERIFY semantic accessibility of new knowledge
    print("\n" + "="*60)
    print("VERIFYING SEMANTIC ACCESSIBILITY")
    print("="*60)
    
    accessibility = semantic_mgr.verify_semantic_accessibility([
        "JWT authentication",
        "refresh token rotation",
        "PKCE mobile security"
    ])
    
    # 6. END SESSION
    print("\n" + "="*60)
    print("ENDING SESSION")
    print("="*60)
    
    memory.end_session(session_id)
    
    print("\n✓ Workflow complete with semantic integration")
    print(f"  Session: {session_id}")
    print(f"  Task: {task_id}")
    print(f"  Semantic context loaded: {len(semantic_context['results'])} notes")
    print(f"  All concepts accessible: {all(accessibility.values())}")


if __name__ == "__main__":
    main()
```

---

## Conclusion

**Document 18 complete!** You now have a production-grade semantic retrieval system that transforms SPES memory from structural navigation to intelligent semantic search.

### Key Achievements

✅ **Vector Embeddings**: Local models (bge-micro-v2) for free, fast semantic search  
✅ **Smart Connections**: Automatic embedding generation for all memory files  
✅ **MCP Integration**: Standard protocol connecting LLMs to semantic memory  
✅ **Query Anchors**: Strategic markers for targeted retrieval  
✅ **Hybrid Search**: Best of keyword + semantic for robust retrieval  
✅ **Complete Integration**: Seamless enhancement of Document 17's memory system  

---

## 7. Best Practices & Production Patterns

### 7.1 Semantic Memory Design Patterns

**Pattern 1: Progressive Enhancement**

Start with structural memory (Document 17), then add semantic layer gradually:

```
Week 1: Basic memory (activeContext, task-logs, core)
Week 2: Add Smart Connections
Week 3: Deploy MCP server
Week 4: Implement query anchors
Week 5: Enable hybrid search
Week 6: Optimize and tune
```

**Benefits**:
- ✅ Each layer adds value independently
- ✅ Can roll back if issues arise
- ✅ Team learns incrementally
- ✅ Identify bottlenecks early

**Pattern 2: Semantic-First Query Strategy**

Always try semantic search before structural navigation:

```python
def find_information(query: str, memory_path: Path):
    """
    Semantic-first information retrieval.
    """
    
    # 1. Try semantic search first
    semantic_results = mcp_client.call_tool("lookup", {
        "query": query,
        "limit": 5,
        "threshold": 0.5
    })
    
    if semantic_results['results']:
        return semantic_results['results']
    
    # 2. Fall back to structural search
    structural_results = search_by_filename(query, memory_path)
    
    if structural_results:
        return structural_results
    
    # 3. Fall back to grep
    grep_results = grep_search(query, memory_path)
    
    return grep_results
```

**Pattern 3: Anchor-Driven Documentation**

Structure all documentation around query anchors:

```markdown
# Feature Documentation Template

%%QA:feature:overview%%
## Overview
[High-level description]

%%QA:feature:use-cases%%
## Use Cases
[When to use this feature]

%%QA:feature:implementation%%
## Implementation
[How to implement]

%%QA:feature:examples%%
## Examples
[Complete working examples]

%%QA:feature:troubleshooting%%
## Troubleshooting
[Common issues and solutions]
```

**Pattern 4: Semantic Validation in CI/CD**

Verify documentation is semantically discoverable:

```yaml
# .github/workflows/semantic-validation.yml
name: Semantic Validation

on: [push, pull_request]

jobs:
  validate-discoverability:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Generate embeddings
        run: |
          npm install
          node generate-embeddings.js
      
      - name: Test key concepts
        run: |
          python test-semantic-search.py \
            --concepts "authentication,database,deployment" \
            --threshold 0.5
```

### 7.2 Performance Tuning Guide

**Optimization Checklist**:

| Level | Optimization | Expected Improvement |
|-------|--------------|---------------------|
| **L1: Quick Wins** | Enable query caching | 50-80% faster repeated queries |
| | Use smaller embedding model | 2-3x faster embedding generation |
| | Exclude archived files | 20-40% smaller index |
| **L2: Moderate Effort** | Implement connection pooling | 30-50% faster under load |
| | Add request queuing | Handle 3-5x more concurrent requests |
| | Pre-compute common queries | Instant results for frequent queries |
| **L3: Significant Effort** | Use vector database (Pinecone/Weaviate) | 5-10x faster for large vaults (>10K files) |
| | Implement sharding | Linear scalability to 100K+ files |
| | GPU acceleration | 10-20x faster embedding generation |

**Tuning Parameters**:

```python
# Performance tuning configuration
TUNING_CONFIG = {
    # Small vault (<1K files)
    "small": {
        "embedding_model": "TaylorAI/bge-micro-v2",
        "dimensions": 384,
        "chunk_size": 500,
        "cache_size": 500,
        "refresh_interval": 300,  # 5 minutes
    },
    
    # Medium vault (1K-10K files)
    "medium": {
        "embedding_model": "nomic-embed-text",
        "dimensions": 768,
        "chunk_size": 750,
        "cache_size": 2000,
        "refresh_interval": 600,  # 10 minutes
        "use_multi_file_storage": True,
    },
    
    # Large vault (>10K files)
    "large": {
        "embedding_model": "text-embedding-3-small",
        "dimensions": 1536,
        "chunk_size": 1000,
        "cache_size": 5000,
        "refresh_interval": 900,  # 15 minutes
        "use_multi_file_storage": True,
        "use_vector_db": True,
        "vector_db": "pinecone",
    }
}
```

### 7.3 Security Considerations

**Protecting Sensitive Memory**:

```python
class SecureSemanticMemory:
    """
    Semantic memory with security controls.
    """
    
    def __init__(self, vault_path: Path, security_config: Dict):
        self.vault_path = Path(vault_path)
        self.security_config = security_config
        
        # Files that should never be embedded
        self.excluded_patterns = [
            "**/*secret*",
            "**/*password*",
            "**/*api-key*",
            ".env",
            "**/.credentials/**"
        ]
        
        # Encryption for sensitive embeddings
        self.encryption_key = self._load_encryption_key()
    
    def should_embed(self, file_path: Path) -> bool:
        """Check if file should be embedded."""
        
        # Check exclusion patterns
        for pattern in self.excluded_patterns:
            if file_path.match(pattern):
                logger.warning(f"Skipping sensitive file: {file_path}")
                return False
        
        # Check file metadata for sensitivity markers
        if self._is_marked_sensitive(file_path):
            return False
        
        return True
    
    def embed_with_encryption(self, content: str) -> bytes:
        """Embed and encrypt sensitive content."""
        
        # Generate embedding
        embedding = self.embedding_model.encode(content)
        
        # Encrypt embedding
        encrypted = self._encrypt(embedding.tobytes(), self.encryption_key)
        
        return encrypted
    
    def search_encrypted(self, query: str) -> List[Dict]:
        """Search encrypted embeddings."""
        
        query_embedding = self.embedding_model.encode(query)
        
        # Decrypt and search
        results = []
        for encrypted_embedding, metadata in self.encrypted_index:
            # Decrypt
            embedding = self._decrypt(encrypted_embedding, self.encryption_key)
            
            # Calculate similarity
            similarity = cosine_similarity(query_embedding, embedding)
            
            if similarity > self.threshold:
                results.append({
                    'metadata': metadata,
                    'score': similarity
                })
        
        return results
```

**Access Control**:

```python
class AccessControlledMCP:
    """MCP server with access control."""
    
    def __init__(self, access_policy: Dict):
        self.access_policy = access_policy
    
    def authorize_request(
        self,
        user_id: str,
        tool_name: str,
        args: Dict
    ) -> bool:
        """Authorize tool request."""
        
        # Check user permissions
        user_perms = self.access_policy.get(user_id, {})
        
        # Check tool access
        if tool_name not in user_perms.get('allowed_tools', []):
            logger.warning(f"Unauthorized tool access: {user_id} -> {tool_name}")
            return False
        
        # Check file path restrictions
        if 'query' in args:
            query = args['query']
            
            # Block queries for restricted topics
            for restricted in user_perms.get('restricted_topics', []):
                if restricted.lower() in query.lower():
                    logger.warning(f"Blocked restricted query: {query}")
                    return False
        
        return True
```

**Security Checklist**:

- [ ] Exclude sensitive files from embedding
- [ ] Encrypt embeddings for confidential projects
- [ ] Implement access control for multi-user setups
- [ ] Audit all semantic searches
- [ ] Rotate encryption keys regularly
- [ ] Monitor for data exfiltration attempts
- [ ] Use secure MCP transport (TLS)
- [ ] Validate all file paths (prevent directory traversal)

### 7.4 Monitoring & Observability

**Comprehensive monitoring setup**:

```python
class SemanticMemoryMonitoring:
    """Monitor semantic memory system health."""
    
    def __init__(self):
        self.metrics = {
            'search_latency': [],
            'cache_hit_rate': 0,
            'embedding_freshness': 0,
            'index_size': 0,
            'error_rate': 0
        }
    
    def collect_metrics(self):
        """Collect system metrics."""
        
        return {
            'search_performance': {
                'p50': np.percentile(self.metrics['search_latency'], 50),
                'p95': np.percentile(self.metrics['search_latency'], 95),
                'p99': np.percentile(self.metrics['search_latency'], 99),
            },
            'cache': {
                'hit_rate': self.metrics['cache_hit_rate'],
                'size': len(self.query_cache)
            },
            'embeddings': {
                'count': self.get_embedding_count(),
                'freshness_seconds': self.get_embedding_age(),
                'size_mb': self.get_index_size_mb()
            },
            'errors': {
                'rate': self.metrics['error_rate'],
                'recent': self.get_recent_errors(limit=10)
            }
        }
    
    def health_check(self) -> Dict[str, str]:
        """Comprehensive health check."""
        
        checks = {
            'embeddings_loaded': 'ok' if self.embeddings_data else 'fail',
            'mcp_server': 'ok' if self.ping_mcp() else 'fail',
            'smart_connections': 'ok' if self.check_smart_connections() else 'fail',
            'cache_healthy': 'ok' if self.cache_size < self.max_cache_size else 'warn',
            'freshness': 'ok' if self.embedding_age < 600 else 'warn'
        }
        
        return checks
```

**Alerting Rules**:

```yaml
# prometheus-alerts.yml
groups:
  - name: semantic_memory
    rules:
      - alert: HighSearchLatency
        expr: mcp_request_duration_seconds{quantile="0.99"} > 2
        for: 5m
        annotations:
          summary: "High search latency detected"
          
      - alert: EmbeddingsStale
        expr: (time() - mcp_embeddings_last_refresh_timestamp) > 3600
        annotations:
          summary: "Embeddings haven't refreshed in over 1 hour"
          
      - alert: HighErrorRate
        expr: rate(mcp_errors_total[5m]) > 0.1
        annotations:
          summary: "Error rate above 10%"
          
      - alert: CacheThrashing
        expr: rate(mcp_cache_evictions_total[5m]) > 10
        annotations:
          summary: "High cache eviction rate"
```

### 7.5 Troubleshooting Workflows

**Systematic troubleshooting approach**:

```python
class SemanticMemoryDiagnostics:
    """Diagnostic tools for semantic memory issues."""
    
    def run_full_diagnostic(self) -> Dict:
        """Run complete diagnostic suite."""
        
        print("Running Semantic Memory Diagnostics...")
        print("=" * 60)
        
        results = {}
        
        # 1. Check Smart Connections
        print("\n1. Checking Smart Connections...")
        results['smart_connections'] = self.check_smart_connections()
        
        # 2. Check MCP Server
        print("\n2. Checking MCP Server...")
        results['mcp_server'] = self.check_mcp_server()
        
        # 3. Check Embeddings Quality
        print("\n3. Checking Embeddings Quality...")
        results['embeddings'] = self.check_embeddings_quality()
        
        # 4. Check Search Performance
        print("\n4. Checking Search Performance...")
        results['performance'] = self.check_search_performance()
        
        # 5. Check Integration
        print("\n5. Checking Memory Integration...")
        results['integration'] = self.check_memory_integration()
        
        # Generate report
        self.generate_diagnostic_report(results)
        
        return results
    
    def check_smart_connections(self) -> Dict:
        """Check Smart Connections status."""
        
        checks = {}
        
        # Check plugin is installed
        plugin_path = self.vault_path / ".obsidian" / "plugins" / "smart-connections"
        checks['plugin_installed'] = plugin_path.exists()
        
        # Check embeddings exist
        embeddings_file = self.vault_path / ".smart-env" / "smart_sources.json"
        checks['embeddings_exist'] = embeddings_file.exists()
        
        if checks['embeddings_exist']:
            # Check embeddings are recent
            age = time.time() - embeddings_file.stat().st_mtime
            checks['embeddings_fresh'] = age < 3600  # Less than 1 hour old
            
            # Check embedding count
            with open(embeddings_file) as f:
                data = json.load(f)
                checks['embedding_count'] = len(data.get('sources', {}))
                checks['embedding_model'] = data.get('model')
        
        return checks
    
    def check_embeddings_quality(self) -> Dict:
        """Check embedding quality with test queries."""
        
        test_queries = [
            ("authentication", [".claude/core/systemPatterns.md"]),
            ("error handling", [".claude/errors/"]),
            ("recent work", [".claude/task-logs/"])
        ]
        
        results = []
        
        for query, expected_paths in test_queries:
            search_results = self.mcp_client.call_tool("lookup", {
                "query": query,
                "limit": 5
            })
            
            # Check if expected paths are in results
            found = any(
                any(exp in r['path'] for exp in expected_paths)
                for r in search_results['results']
            )
            
            results.append({
                'query': query,
                'expected': expected_paths,
                'found': found,
                'top_result': search_results['results'][0]['path'] if search_results['results'] else None
            })
        
        return results
    
    def suggest_fixes(self, diagnostic_results: Dict) -> List[str]:
        """Generate fix suggestions based on diagnostics."""
        
        suggestions = []
        
        # Smart Connections issues
        if not diagnostic_results['smart_connections']['plugin_installed']:
            suggestions.append(
                "Install Smart Connections plugin in Obsidian"
            )
        
        if not diagnostic_results['smart_connections']['embeddings_exist']:
            suggestions.append(
                "Generate embeddings: Run 'Smart Connections: Refresh all embeddings' in Obsidian"
            )
        
        if not diagnostic_results['smart_connections'].get('embeddings_fresh', True):
            suggestions.append(
                "Embeddings are stale. Force refresh or enable auto-refresh."
            )
        
        # MCP Server issues
        if not diagnostic_results['mcp_server']['running']:
            suggestions.append(
                "Start MCP server or check Claude Desktop config"
            )
        
        # Performance issues
        if diagnostic_results['performance']['avg_latency'] > 1.0:
            suggestions.append(
                "High search latency detected. Consider:\n"
                "  - Using smaller embedding model\n"
                "  - Enabling query caching\n"
                "  - Reducing vault size"
            )
        
        return suggestions
```

### 7.6 Migration & Upgrade Paths

**Upgrading from Simple Memory to Semantic Memory**:

```bash
#!/bin/bash
# migrate-to-semantic.sh

echo "Migrating to Semantic Memory System..."
echo "======================================"

# 1. Backup existing memory
echo "\n1. Creating backup..."
tar -czf memory-backup-$(date +%Y%m%d).tar.gz .claude/

# 2. Install Smart Connections
echo "\n2. Setting up Smart Connections..."
cat << EOF
Please complete these steps in Obsidian:
1. Settings → Community Plugins → Browse
2. Search "Smart Connections"
3. Install and Enable
4. Configure:
   - Model: TaylorAI/bge-micro-v2
   - Include folders: .claude/
   - Min chars: 100
5. Run: Smart Connections: Refresh all embeddings
6. Wait for completion (check status bar)

Press Enter when complete...
EOF
read

# 3. Install MCP server
echo "\n3. Installing MCP server..."
npm install @modelcontextprotocol/sdk
cp mcp-server.js /usr/local/bin/

# 4. Configure Claude Desktop
echo "\n4. Configuring Claude Desktop..."
CLAUDE_CONFIG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"

if [ -f "$CLAUDE_CONFIG" ]; then
    # Backup existing config
    cp "$CLAUDE_CONFIG" "$CLAUDE_CONFIG.backup"
fi

# Add MCP server config
cat > "$CLAUDE_CONFIG" << EOF
{
  "mcpServers": {
    "smart-connections": {
      "command": "node",
      "args": [
        "/usr/local/bin/mcp-server.js",
        "$(pwd)"
      ]
    }
  }
}
EOF

echo "✓ MCP server configured"

# 5. Verify setup
echo "\n5. Verifying setup..."
python3 << 'PYTHON'
from pathlib import Path
import json

vault_path = Path.cwd()

# Check Smart Connections
smart_env = vault_path / ".smart-env"
if smart_env.exists():
    print("✓ Smart Connections directory exists")
    
    embeddings = smart_env / "smart_sources.json"
    if embeddings.exists():
        with open(embeddings) as f:
            data = json.load(f)
        print(f"✓ Embeddings loaded: {len(data.get('sources', {}))} files")
    else:
        print("✗ No embeddings found - run refresh in Obsidian")
else:
    print("✗ Smart Connections not initialized")

# Check MCP config
mcp_config = Path.home() / "Library/Application Support/Claude/claude_desktop_config.json"
if mcp_config.exists():
    with open(mcp_config) as f:
        config = json.load(f)
    if "smart-connections" in config.get("mcpServers", {}):
        print("✓ MCP server configured")
    else:
        print("✗ MCP server not in config")
else:
    print("✗ Claude Desktop config not found")
PYTHON

echo "\n======================================"
echo "Migration complete!"
echo "Restart Claude Desktop to activate MCP server"
echo "======================================"
```

### What's Next

**Document 19**: Meta-Cognitive Workflows (~12,000 words)
- Constitutional AI with performance scoring (0-23 system)
- ReAct framework (Reasoning-Action-Observation loops)
- Reflection prompting for continuous improvement
- Tree of Thoughts for multi-path reasoning
- Chain of Density for progressive summarization
- Self-consistency prompting for validation

**Document 20**: Advanced Prompt Engineering (~10,000 words)
- Memory-first system prompts
- Self-verification loops
- Automatic prompt optimization
- Context window management
- Prompt chaining orchestration

**Document 21**: Production Deployment & Operations (~10,000 words)
- Multi-environment strategy (dev/staging/prod)
- Blue-green deployments
- Monitoring & observability
- A/B testing for prompts
- Incident response runbooks

**Document 22**: Knowledge Graph & Advanced RAG (~10,000 words)
- Graph construction from wiki-links
- Semantic clustering & communities
- Multi-hop reasoning
- Advanced RAG patterns
- Vector database migration

---

*Document 18 complete - Semantic Retrieval & MCP Integration for SPES*