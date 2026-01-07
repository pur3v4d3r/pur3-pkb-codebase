---
title: SPES/PKB Technology Stack Deep Dive
document_type: technical_reference
tier: 1
priority: critical
version: 2.0.0
status: published
prerequisites: ["System Architecture Overview"]
estimated_reading_time: 90-120 minutes
last_updated: 2025-12-25
---

# SPES/PKB Technology Stack Deep Dive

**Version**: 2.0.0  
**Document Type**: Technical Reference  
**Audience**: Developers, system architects, advanced users  
**Purpose**: Comprehensive technical specifications for all stack components

---

## Table of Contents

1. [Stack Overview](#1-stack-overview)
2. [Knowledge Base Layer](#2-knowledge-base-layer)
3. [LLM Integration Layer](#3-llm-integration-layer)
4. [Python Runtime & Libraries](#4-python-runtime--libraries)
5. [Embedding & Vector Search](#5-embedding--vector-search)
6. [Development Tools](#6-development-tools)
7. [Configuration Management](#7-configuration-management)
8. [Installation & Setup](#8-installation--setup)
9. [Version Compatibility Matrix](#9-version-compatibility-matrix)
10. [Troubleshooting Guide](#10-troubleshooting-guide)

---

## 1. Stack Overview

### 1.1 Technology Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                      │
│  Obsidian GUI, CLI Tools, Interactive Dashboards            │
└─────────────────────────────────────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  Knowledge Management Layer                  │
│  Obsidian v1.5.0+, Plugins, Markdown Processing             │
└─────────────────────────────────────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Memory & Retrieval Layer                   │
│  Smart Connections, MCP Server, Embeddings                   │
└─────────────────────────────────────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Workflow Execution Layer                   │
│  Python 3.10+, Workflow Engine, State Management            │
└─────────────────────────────────────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    LLM Integration Layer                     │
│  Anthropic SDK, Google SDK, OpenAI SDK, Ollama API          │
└─────────────────────────────────────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                         LLM Providers                        │
│  Claude, Gemini, GPT-4, Ollama, LM Studio, GPT4All          │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Core Technologies Summary

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| **KB** | Obsidian | v1.5.0+ | Knowledge base interface |
| **KB** | Markdown | CommonMark | Note format |
| **Plugin** | Smart Connections | v1.8.0+ | Semantic search |
| **Plugin** | Dataview | v0.5.55+ | Metadata queries |
| **Plugin** | Templater | v2.0.0+ | Template automation |
| **Plugin** | Meta Bind | v1.0.0+ | Interactive elements |
| **Runtime** | Python | 3.10-3.12 | Workflow engine |
| **LLM** | Anthropic SDK | v0.18.0+ | Claude integration |
| **LLM** | Google AI SDK | v0.3.0+ | Gemini integration |
| **LLM** | OpenAI SDK | v1.0.0+ | GPT integration |
| **Local** | Ollama | Latest | Local LLM runtime |
| **Embedding** | SentenceTransformers | v2.2.0+ | Embeddings |
| **Vector** | NumPy/scikit-learn | Latest | Similarity search |

---

## 2. Knowledge Base Layer

### 2.1 Obsidian

**Version**: v1.5.0 or higher

**Installation**:
```bash
# macOS
brew install --cask obsidian

# Windows
winget install Obsidian.Obsidian

# Linux (AppImage)
wget https://github.com/obsidianmd/obsidian-releases/releases/download/v1.5.3/Obsidian-1.5.3.AppImage
chmod +x Obsidian-1.5.3.AppImage
./Obsidian-1.5.3.AppImage
```

**Configuration**:
```json
// .obsidian/app.json (key settings)
{
  "vimMode": false,
  "showLineNumber": true,
  "spellcheck": true,
  "spellcheckLanguages": ["en-US"],
  "baseFontSize": 16,
  "theme": "obsidian",
  "useMarkdownLinks": true,
  "newLinkFormat": "shortest",
  "attachmentFolderPath": "attachments"
}
```

**File Watcher Settings**:
```json
// .obsidian/workspace.json
{
  "autoSaveInterval": 2000,
  "autoPairBrackets": true,
  "autoPairMarkdown": true,
  "smartIndentList": true,
  "foldHeading": true,
  "foldIndent": true
}
```

**Performance Tuning**:
```yaml
Recommended Settings:
  Max File Size: 10MB (default)
  Index Throttle: 100ms
  File Watcher: Enabled
  Cache: Enabled
  
Performance with Large Vaults:
  1,000 notes: Instant
  10,000 notes: <1s indexing
  100,000 notes: 5-10s indexing (on SSD)
```

### 2.2 Markdown Specification

**Supported**: CommonMark + Obsidian Extensions

**Core Syntax**:
```markdown
# Headers
## H2
### H3

**Bold** and *italic*

- Bullet lists
  - Nested items
- Another item

1. Numbered lists
2. Item two

[Links](https://example.com)

![Images](path/to/image.png)

`Inline code`

```language
Code blocks
```

> Blockquotes
```

**Obsidian Extensions**:
```markdown
# Wiki-links
[[Note Title]]
[[Note Title|Display Text]]
[[Note Title#Heading]]
[[Note Title#^block-id]]

# Embeds
![[Other Note]]
![[Image.png]]
![[PDF.pdf#page=5]]

# Tags
#tag
#nested/tag

# Callouts
> [!note]
> Content

> [!warning]
> Alert content

# Footnotes
Text with footnote[^1]

[^1]: Footnote content

# Task lists
- [ ] Unchecked
- [x] Checked

# Tables
| Column 1 | Column 2 |
|----------|----------|
| Data     | Data     |

# Highlighting
==Highlighted text==

# Comments
%% This is a comment %%
```

**Metadata (YAML Frontmatter)**:
```yaml
---
tags: [tag1, tag2]
aliases: [Alternative Name]
created: 2025-01-01
modified: 2025-01-15
status: published
---
```

### 2.3 Vault Structure

**Recommended Organization**:
```
vault-root/
├── .obsidian/                  # Obsidian configuration
│   ├── plugins/
│   ├── themes/
│   ├── app.json
│   └── workspace.json
│
├── .smart-env/                 # Smart Connections data
│   ├── embeddings.json
│   └── config.json
│
├── .claude/                    # SPES memory
│   ├── core/
│   ├── sessions/
│   ├── decisions/
│   └── patterns/
│
├── 00-meta/                    # System notes
│   ├── dashboards/
│   ├── indexes/
│   └── templates/
│
├── 01-fleeting/                # Quick captures
│
├── 02-projects/                # Active projects
│
├── 03-areas/                   # Ongoing responsibilities
│
├── 04-resources/               # Reference material
│
├── 05-archives/                # Completed/inactive
│
└── attachments/                # Media files
```

**File Naming Conventions**:
```yaml
Notes:
  Format: descriptive-title.md
  Avoid: spaces, special chars
  Example: cognitive-load-theory.md

Dates (in filename):
  Format: YYYY-MM-DD
  Example: 2025-01-15-meeting-notes.md

Templates:
  Prefix: template-
  Example: template-daily-note.md

Indexes/MOCs:
  Suffix: -index or -moc
  Example: programming-moc.md
```

---

## 3. LLM Integration Layer

### 3.1 Anthropic Claude

**SDK**: `anthropic` Python package

**Installation**:
```bash
pip install anthropic==0.18.0
# or
pip install anthropic>=0.18.0,<1.0.0
```

**Configuration**:
```python
import anthropic
import os

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)
```

**Environment Variables**:
```bash
# .env
ANTHROPIC_API_KEY=sk-ant-api03-...
ANTHROPIC_BASE_URL=https://api.anthropic.com  # Optional override
```

**API Usage**:
```python
# Basic completion
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

# Streaming
with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Tell me a story"}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

# System prompts
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system="You are a helpful assistant.",
    messages=[
        {"role": "user", "content": "Help me with Python"}
    ]
)

# Tool use (MCP)
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    tools=[
        {
            "name": "search",
            "description": "Search the knowledge base",
            "input_schema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"}
                }
            }
        }
    ],
    messages=[{"role": "user", "content": "Search for Python"}]
)
```

**Rate Limits** (as of Dec 2025):
```yaml
Claude API (Paid Tier):
  Requests per minute: 1000
  Tokens per minute: 100,000
  Tokens per day: 10,000,000
  
Claude API (Free Tier):
  Requests per minute: 5
  Tokens per minute: 40,000
  
Recommended Handling:
  - Implement exponential backoff
  - Monitor rate limit headers
  - Queue requests when near limit
```

**Error Handling**:
```python
from anthropic import APIError, RateLimitError

try:
    response = client.messages.create(...)
except RateLimitError as e:
    # Wait and retry
    time.sleep(e.retry_after or 60)
    response = client.messages.create(...)
except APIError as e:
    # Handle other API errors
    print(f"API error: {e}")
```

### 3.2 Google Gemini

**SDK**: `google-generativeai` Python package

**Installation**:
```bash
pip install google-generativeai==0.3.0
```

**Configuration**:
```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
```

**API Usage**:
```python
# Basic completion
model = genai.GenerativeModel('gemini-2.0-flash-exp')
response = model.generate_content("Hello, Gemini!")
print(response.text)

# Streaming
response = model.generate_content(
    "Tell me a story",
    stream=True
)
for chunk in response:
    print(chunk.text, end="", flush=True)

# System instructions
model = genai.GenerativeModel(
    'gemini-2.0-flash-exp',
    system_instruction="You are a helpful assistant."
)

# Multi-turn conversation
chat = model.start_chat(history=[])
response = chat.send_message("Hello!")
response = chat.send_message("How are you?")

# Function calling
def search_knowledge(query: str) -> dict:
    return {"results": ["result1", "result2"]}

tools = [search_knowledge]
model = genai.GenerativeModel(
    'gemini-2.0-flash-exp',
    tools=tools
)
response = model.generate_content("Search for Python")
```

**Rate Limits**:
```yaml
Gemini Free Tier:
  Requests per minute: 15
  Requests per day: 1500
  
Gemini Paid Tier:
  Requests per minute: 360
  Tokens per minute: 4,000,000
```

### 3.3 OpenAI GPT

**SDK**: `openai` Python package

**Installation**:
```bash
pip install openai==1.0.0
```

**Configuration**:
```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
```

**API Usage**:
```python
# Chat completion
response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

# Streaming
stream = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")

# Function calling
functions = [
    {
        "name": "search",
        "description": "Search knowledge base",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"}
            }
        }
    }
]
response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[{"role": "user", "content": "Search for Python"}],
    tools=[{"type": "function", "function": f} for f in functions]
)
```

### 3.4 Ollama (Local LLMs)

**Installation**:
```bash
# macOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Or download from https://ollama.ai/download

# Verify installation
ollama --version
```

**Starting Server**:
```bash
# Start Ollama server
ollama serve

# Server runs on http://localhost:11434
```

**Model Management**:
```bash
# List available models
ollama list

# Pull a model
ollama pull llama3:8b
ollama pull codellama:13b
ollama pull mistral:7b
ollama pull mixtral:8x7b

# Remove a model
ollama rm llama3:8b

# Show model info
ollama show llama3:8b
```

**API Usage** (Python):
```python
import requests

def ollama_generate(prompt: str, model: str = "llama3:8b") -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

# Streaming
def ollama_stream(prompt: str, model: str = "llama3:8b"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line)
            if not chunk.get("done"):
                yield chunk["response"]

# Chat API
def ollama_chat(messages: list, model: str = "llama3:8b"):
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": model,
            "messages": messages,
            "stream": False
        }
    )
    return response.json()["message"]["content"]
```

**Modelfile Customization**:
```dockerfile
# custom-model.modelfile

FROM llama3:8b

# Set parameters
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER top_k 40

# System message
SYSTEM """
You are a helpful Python programming assistant.
"""

# Create custom model
# ollama create custom-python -f custom-model.modelfile
```

**Performance Tuning**:
```yaml
Context Window Optimization:
  # Reduce context for faster inference
  ollama run llama3:8b --context-length 2048
  
GPU Acceleration:
  # Automatic if GPU available
  # Metal (macOS), CUDA (NVIDIA), ROCm (AMD)
  
CPU Threads:
  # Set thread count
  ollama run llama3:8b --threads 8
  
Quantization:
  # Smaller models for faster inference
  ollama pull llama3:8b-q4_0  # 4-bit quantized
```

### 3.5 LM Studio

**Installation**:
```bash
# Download from https://lmstudio.ai
# Available for macOS, Windows, Linux

# macOS
brew install --cask lm-studio

# Or download .dmg installer
```

**Model Management**:
```yaml
Via GUI:
  1. Open LM Studio
  2. Browse models in "Discover" tab
  3. Download desired models
  4. Models stored in ~/lm-studio/models/

Supported Formats:
  - GGUF (preferred)
  - GPTQ
  - AWQ
```

**Starting API Server**:
```yaml
Steps:
  1. Open LM Studio
  2. Load a model
  3. Click "Local Server" tab
  4. Click "Start Server"
  
Server Details:
  Endpoint: http://localhost:1234/v1
  Compatible with: OpenAI API
```

**API Usage** (OpenAI-compatible):
```python
from openai import OpenAI

# Point to LM Studio
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="not-needed"
)

response = client.chat.completions.create(
    model="local-model",  # Any loaded model
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)
```

### 3.6 GPT4All

**Installation**:
```bash
pip install gpt4all
```

**Python Usage**:
```python
from gpt4all import GPT4All

# Initialize (auto-downloads model if needed)
model = GPT4All("mistral-7b-openorca.Q4_0.gguf")

# Generate
response = model.generate("Hello, how are you?")

# Streaming
for token in model.generate("Tell me a story", streaming=True):
    print(token, end="", flush=True)

# Chat session
with model.chat_session():
    response1 = model.generate("Hello!")
    response2 = model.generate("What's the weather?")
    # Context maintained

# Custom parameters
response = model.generate(
    "Write Python code",
    max_tokens=500,
    temp=0.7,
    top_p=0.9,
    top_k=40
)
```

**Available Models**:
```yaml
Recommended Models:
  - mistral-7b-openorca.Q4_0.gguf (General)
  - gpt4all-falcon-q4_0.gguf (Code)
  - orca-mini-3b-gguf2-q4_0.gguf (Fast, lightweight)
  
Model Directory:
  macOS: ~/Library/Application Support/nomic.ai/GPT4All/
  Linux: ~/.local/share/nomic.ai/GPT4All/
  Windows: %LOCALAPPDATA%\nomic.ai\GPT4All\
```

---

## 4. Python Runtime & Libraries

### 4.1 Python Version

**Required**: Python 3.10, 3.11, or 3.12

**Installation**:
```bash
# macOS (Homebrew)
brew install python@3.12

# Linux (apt)
sudo apt update
sudo apt install python3.12

# Verify
python3 --version
```

**Virtual Environment Setup**:
```bash
# Create venv
python3 -m venv spes-env

# Activate
source spes-env/bin/activate  # macOS/Linux
.\spes-env\Scripts\activate   # Windows

# Deactivate
deactivate
```

### 4.2 Core Dependencies

**requirements.txt**:
```txt
# LLM SDKs
anthropic>=0.18.0,<1.0.0
google-generativeai>=0.3.0,<1.0.0
openai>=1.0.0,<2.0.0

# Embeddings & ML
sentence-transformers>=2.2.0
numpy>=1.24.0
scikit-learn>=1.3.0
torch>=2.0.0  # For SentenceTransformers

# API & Networking
requests>=2.31.0
aiohttp>=3.9.0
httpx>=0.25.0
sse-starlette>=1.6.0

# Data Processing
pyyaml>=6.0
jsonschema>=4.17.0
pydantic>=2.0.0
python-dotenv>=1.0.0

# Utilities
tenacity>=8.2.0  # Retry logic
loguru>=0.7.0    # Logging
click>=8.1.0     # CLI
rich>=13.0.0     # Terminal formatting
```

**Installation**:
```bash
pip install -r requirements.txt
```

### 4.3 Development Dependencies

**requirements-dev.txt**:
```txt
# Testing
pytest>=7.4.0
pytest-asyncio>=0.21.0
pytest-cov>=4.1.0
pytest-mock>=3.11.0

# Code Quality
black>=23.7.0      # Formatting
ruff>=0.0.285      # Linting
mypy>=1.5.0        # Type checking
isort>=5.12.0      # Import sorting

# Documentation
mkdocs>=1.5.0
mkdocs-material>=9.2.0
mkdocstrings>=0.22.0

# Profiling
py-spy>=0.3.0
memory-profiler>=0.61.0
```

### 4.4 Package Management

**Using pip**:
```bash
# Install from requirements
pip install -r requirements.txt

# Install package
pip install anthropic

# Install with version constraint
pip install "anthropic>=0.18.0,<1.0.0"

# Upgrade package
pip install --upgrade anthropic

# List installed
pip list

# Show package info
pip show anthropic
```

**Using pip-tools** (recommended for dependency management):
```bash
# Install pip-tools
pip install pip-tools

# Create requirements.in
cat > requirements.in << EOF
anthropic>=0.18.0
google-generativeai>=0.3.0
sentence-transformers
EOF

# Compile to locked requirements.txt
pip-compile requirements.in

# Install from locked file
pip-sync requirements.txt

# Update dependencies
pip-compile --upgrade requirements.in
```

**Using Poetry** (alternative):
```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Initialize project
poetry init

# Add dependencies
poetry add anthropic google-generativeai

# Install dependencies
poetry install

# Run script
poetry run python script.py
```

---

## 5. Embedding & Vector Search

### 5.1 Sentence Transformers

**Installation**:
```bash
pip install sentence-transformers
```

**Model Selection**:
```yaml
TaylorAI/bge-micro-v2:
  Dimensions: 384
  Speed: Very Fast
  Quality: Good
  Use: Default choice
  Size: 33MB
  
all-MiniLM-L6-v2:
  Dimensions: 384
  Speed: Very Fast
  Quality: Good
  Use: General purpose
  Size: 80MB

BAAI/bge-small-en-v1.5:
  Dimensions: 384
  Speed: Fast
  Quality: Better
  Use: Higher quality needed
  Size: 133MB

BAAI/bge-base-en-v1.5:
  Dimensions: 768
  Speed: Medium
  Quality: Best
  Use: Production quality
  Size: 438MB
```

**Usage**:
```python
from sentence_transformers import SentenceTransformer
import numpy as np

# Load model
model = SentenceTransformer('TaylorAI/bge-micro-v2')

# Generate embeddings
texts = [
    "This is a sentence",
    "This is another sentence"
]
embeddings = model.encode(texts)
# Shape: (2, 384)

# Compute similarity
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)[0][0]
# Value: 0.0 to 1.0

# Batch encoding (efficient)
large_corpus = ["text1", "text2", ...]  # 10,000 items
embeddings = model.encode(
    large_corpus,
    batch_size=32,
    show_progress_bar=True
)
```

**Performance Optimization**:
```python
# Use GPU if available
model = SentenceTransformer(
    'TaylorAI/bge-micro-v2',
    device='cuda'  # or 'mps' for Apple Silicon
)

# Normalize embeddings for faster cosine similarity
embeddings = model.encode(
    texts,
    normalize_embeddings=True
)
# Now can use dot product instead of cosine similarity

# Multi-processing for large batches
from sentence_transformers import SentenceTransformer
import torch

model = SentenceTransformer('TaylorAI/bge-micro-v2')
pool = model.start_multi_process_pool()
embeddings = model.encode_multi_process(
    texts,
    pool,
    batch_size=32
)
model.stop_multi_process_pool(pool)
```

### 5.2 Vector Search Implementation

**In-Memory Search** (for small datasets <10K):
```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class VectorIndex:
    def __init__(self):
        self.embeddings = []
        self.metadata = []
    
    def add(self, embedding: np.ndarray, metadata: dict):
        self.embeddings.append(embedding)
        self.metadata.append(metadata)
    
    def search(self, query_embedding: np.ndarray, top_k: int = 5):
        # Compute similarities
        similarities = cosine_similarity(
            [query_embedding],
            self.embeddings
        )[0]
        
        # Get top k indices
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Return results
        results = []
        for idx in top_indices:
            results.append({
                'metadata': self.metadata[idx],
                'similarity': similarities[idx]
            })
        
        return results
```

**FAISS** (for large datasets >10K):
```bash
pip install faiss-cpu  # or faiss-gpu
```

```python
import faiss
import numpy as np

class FAISSIndex:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatIP(dimension)  # Inner product
        self.metadata = []
    
    def add(self, embeddings: np.ndarray, metadata: list):
        # Normalize for cosine similarity
        faiss.normalize_L2(embeddings)
        self.index.add(embeddings.astype('float32'))
        self.metadata.extend(metadata)
    
    def search(self, query: np.ndarray, top_k: int = 5):
        # Normalize query
        faiss.normalize_L2(query.reshape(1, -1))
        
        # Search
        similarities, indices = self.index.search(
            query.reshape(1, -1).astype('float32'),
            top_k
        )
        
        # Return results
        results = []
        for idx, sim in zip(indices[0], similarities[0]):
            results.append({
                'metadata': self.metadata[idx],
                'similarity': float(sim)
            })
        
        return results
    
    def save(self, path: str):
        faiss.write_index(self.index, path)
    
    @classmethod
    def load(cls, path: str, dimension: int):
        obj = cls(dimension)
        obj.index = faiss.read_index(path)
        return obj
```

### 5.3 Smart Connections Configuration

**Plugin Configuration**:
```json
// .obsidian/plugins/smart-connections/data.json
{
  "api_provider": "transformers",
  "transformers_model_id": "TaylorAI/bge-micro-v2",
  "transformers_batch_size": 50,
  "embed_input_min_chars": 100,
  "skip_sections": [],
  "excluded_folders": ["templates", "archive"],
  "file_exclusions": "node_modules,*.jpg,*.png",
  "show_full_path": false,
  "expanded_view": true,
  "language": "en",
  "log_render": false,
  "log_render_files": false,
  "recently_sent_retry_notice": false
}
```

**Embedding Generation**:
```yaml
Automatic:
  - New file created → Auto-embedded after save
  - File modified → Re-embedded on save
  - Vault opened → Missing embeddings generated
  
Manual:
  - Command palette: "Smart Connections: Force Refresh"
  - Right-click file: "Smart Connections: Embed File"
  
Storage:
  Location: .smart-env/embeddings.json
  Format: JSON array
  Size: ~1KB per note (average)
```

---

## 6. Development Tools

### 6.1 Code Formatting

**Black** (Python formatter):
```bash
# Install
pip install black

# Format file
black script.py

# Format directory
black src/

# Check without modifying
black --check src/

# Configuration: pyproject.toml
[tool.black]
line-length = 100
target-version = ['py310']
include = '\.pyi?$'
```

**isort** (Import sorting):
```bash
# Install
pip install isort

# Sort imports
isort script.py

# Configuration: pyproject.toml
[tool.isort]
profile = "black"
line_length = 100
```

### 6.2 Linting

**Ruff** (Fast Python linter):
```bash
# Install
pip install ruff

# Lint
ruff check src/

# Fix auto-fixable issues
ruff check --fix src/

# Configuration: pyproject.toml
[tool.ruff]
line-length = 100
target-version = "py310"
select = ["E", "F", "I", "N", "W"]
ignore = ["E501"]  # Line too long (handled by black)
```

### 6.3 Type Checking

**mypy**:
```bash
# Install
pip install mypy

# Type check
mypy src/

# Configuration: pyproject.toml
[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

**Type hints example**:
```python
from typing import List, Dict, Optional, Union, Callable

def process_components(
    component_ids: List[str],
    config: Dict[str, Any],
    callback: Optional[Callable[[str], None]] = None
) -> Union[List[Component], None]:
    """Process components with type safety."""
    pass
```

### 6.4 Testing

**pytest**:
```bash
# Install
pip install pytest pytest-asyncio pytest-cov

# Run tests
pytest tests/

# With coverage
pytest --cov=src tests/

# Specific test
pytest tests/test_component.py::test_load_component

# Configuration: pyproject.toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
```

**Test example**:
```python
import pytest
from spes.components import ComponentLoader

def test_load_component():
    loader = ComponentLoader()
    component = loader.load("instruction-v1.0.0")
    assert component is not None
    assert component.version == "1.0.0"

@pytest.mark.asyncio
async def test_async_workflow():
    workflow = Workflow(...)
    result = await workflow.execute()
    assert result.success

@pytest.fixture
def mock_llm():
    class MockLLM:
        def generate(self, prompt):
            return "Mock response"
    return MockLLM()

def test_with_mock(mock_llm):
    response = mock_llm.generate("test")
    assert response == "Mock response"
```

---

## 7. Configuration Management

### 7.1 Environment Variables

**.env file**:
```bash
# LLM API Keys
ANTHROPIC_API_KEY=sk-ant-api03-...
GOOGLE_API_KEY=AIza...
OPENAI_API_KEY=sk-...

# Vault Configuration
VAULT_PATH=/Users/username/vault
SPES_PATH=/Users/username/spes

# LLM Endpoints
OLLAMA_BASE_URL=http://localhost:11434
LMSTUDIO_BASE_URL=http://localhost:1234

# MCP Configuration
MCP_SERVER_PORT=3000
MCP_SERVER_HOST=localhost

# Default LLMs
DEFAULT_CLOUD_LLM=claude
DEFAULT_LOCAL_LLM=ollama
FALLBACK_LLM=gemini

# Performance
MAX_WORKERS=4
CACHE_TTL=3600

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/spes.log
```

**Loading in Python**:
```python
from dotenv import load_dotenv
import os

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
VAULT_PATH = os.getenv("VAULT_PATH")
```

### 7.2 Configuration Files

**config.yml**:
```yaml
# System Configuration
system:
  name: "SPES"
  version: "2.0.0"
  vault_path: "${VAULT_PATH}"

# Component Library
components:
  directories:
    - "components/core"
    - "components/community"
  cache_enabled: true
  cache_ttl: 3600

# LLM Configuration
llm:
  default_provider: "claude"
  fallback_provider: "gemini"
  
  providers:
    claude:
      model: "claude-sonnet-4-20250514"
      max_tokens: 4096
      temperature: 0.7
    
    gemini:
      model: "gemini-2.0-flash-exp"
      max_tokens: 8192
      temperature: 0.7
    
    ollama:
      base_url: "http://localhost:11434"
      model: "llama3:8b"
      context_window: 8192

# Workflow Engine
workflow:
  max_concurrent: 4
  retry_attempts: 3
  retry_delay: 1.0
  timeout: 300

# Memory & Embeddings
memory:
  embedding_model: "TaylorAI/bge-micro-v2"
  chunk_size: 512
  chunk_overlap: 50
  batch_size: 32

# MCP
mcp:
  enabled: true
  server_port: 3000
  server_host: "localhost"

# Logging
logging:
  level: "INFO"
  file: "logs/spes.log"
  max_size: 10485760  # 10MB
  backup_count: 5
```

**Loading configuration**:
```python
import yaml
import os
from string import Template

def load_config(path: str = "config.yml") -> dict:
    with open(path) as f:
        content = f.read()
    
    # Substitute environment variables
    template = Template(content)
    content = template.safe_substitute(os.environ)
    
    return yaml.safe_load(content)

config = load_config()
vault_path = config["system"]["vault_path"]
```

---

## 8. Installation & Setup

### 8.1 Quick Start Installation

```bash
# 1. Install Obsidian
brew install --cask obsidian  # macOS

# 2. Create vault directory
mkdir -p ~/PKB-System/vault
cd ~/PKB-System

# 3. Install Python 3.10+
brew install python@3.12

# 4. Create virtual environment
python3 -m venv spes-env
source spes-env/bin/activate

# 5. Install Python dependencies
cat > requirements.txt << EOF
anthropic>=0.18.0
google-generativeai>=0.3.0
sentence-transformers>=2.2.0
numpy>=1.24.0
scikit-learn>=1.3.0
pyyaml>=6.0
python-dotenv>=1.0.0
EOF

pip install -r requirements.txt

# 6. Configure environment
cat > .env << EOF
ANTHROPIC_API_KEY=your-api-key-here
VAULT_PATH=$HOME/PKB-System/vault
EOF

# 7. Install Obsidian plugins (via Obsidian GUI)
# - Smart Connections
# - Dataview
# - Templater

# 8. (Optional) Install Ollama for local LLMs
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull llama3:8b
```

### 8.2 Verification

```bash
# Check Python
python3 --version  # Should be 3.10+

# Check Python packages
pip list | grep anthropic
pip list | grep sentence-transformers

# Check Obsidian plugins
# Open Obsidian, Settings → Community Plugins
# Verify: Smart Connections, Dataview enabled

# Check Ollama (if installed)
ollama list

# Test API connectivity
python3 << EOF
from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=100,
    messages=[{"role": "user", "content": "Hello!"}]
)
print("✓ Claude API working")
print(response.content[0].text)
EOF
```

---

## 9. Version Compatibility Matrix

### 9.1 Tested Configurations

| Component | Version | Python | macOS | Windows | Linux | Status |
|-----------|---------|--------|-------|---------|-------|--------|
| Obsidian | v1.5.3 | N/A | ✅ M2 | ✅ 11 | ✅ Ubuntu 22.04 | Stable |
| Smart Connections | v1.8.2 | N/A | ✅ | ✅ | ✅ | Stable |
| Dataview | v0.5.56 | N/A | ✅ | ✅ | ✅ | Stable |
| Python | 3.10 | N/A | ✅ | ✅ | ✅ | Stable |
| Python | 3.11 | N/A | ✅ | ✅ | ✅ | Stable |
| Python | 3.12 | N/A | ✅ | ✅ | ✅ | Stable |
| anthropic | 0.18.0 | 3.10+ | ✅ | ✅ | ✅ | Stable |
| google-ai | 0.3.2 | 3.10+ | ✅ | ✅ | ✅ | Stable |
| sentence-transformers | 2.2.2 | 3.10+ | ✅ | ✅ | ✅ | Stable |
| Ollama | 0.1.20 | N/A | ✅ M2 | ✅ | ✅ | Stable |

### 9.2 Known Issues

```yaml
Smart Connections v1.8.0 on Windows:
  Issue: Slow embedding generation
  Workaround: Upgrade to v1.8.2+
  
Ollama on macOS Intel:
  Issue: Limited model support
  Workaround: Use smaller models (7B max)
  
SentenceTransformers on M1/M2:
  Issue: Requires Rosetta for some models
  Workaround: Install native ARM build of PyTorch first
```

---

## 10. Troubleshooting Guide

### 10.1 Common Issues

**Issue**: `ModuleNotFoundError: No module named 'anthropic'`

**Solution**:
```bash
# Ensure virtual environment is activated
source spes-env/bin/activate

# Install package
pip install anthropic

# Verify installation
pip show anthropic
```

---

**Issue**: Smart Connections not generating embeddings

**Solution**:
```yaml
1. Check plugin enabled:
   Obsidian → Settings → Community Plugins → Smart Connections (ON)

2. Check model downloaded:
   - Plugin will auto-download on first use
   - Check: .smart-env/ directory exists

3. Force refresh:
   - Ctrl+P → "Smart Connections: Force Refresh"

4. Check console for errors:
   - View → Toggle Developer Tools → Console
```

---

**Issue**: Ollama connection refused

**Solution**:
```bash
# Check if Ollama is running
curl http://localhost:11434/api/version

# If not running, start it
ollama serve

# Verify models available
ollama list
```

---

**Issue**: Out of memory when generating embeddings

**Solution**:
```yaml
Option 1 - Reduce batch size:
  # In Smart Connections settings
  batch_size: 16  # Down from 32

Option 2 - Use smaller model:
  # Switch to all-MiniLM-L6-v2
  model: "sentence-transformers/all-MiniLM-L6-v2"

Option 3 - Increase swap:
  # macOS: Automatic
  # Linux: Check /etc/fstab
```

---

**Issue**: API rate limit errors

**Solution**:
```python
# Implement exponential backoff
from tenacity import retry, wait_exponential, stop_after_attempt

@retry(
    wait=wait_exponential(multiplier=1, min=4, max=60),
    stop=stop_after_attempt(5)
)
def call_llm_api(prompt):
    return client.messages.create(...)
```

---

**Issue**: Slow workflow execution

**Solution**:
```yaml
Diagnosis:
  1. Profile execution:
     python -m cProfile -o profile.stats script.py
  
  2. Identify bottleneck:
     python -m pstats profile.stats
     > sort cumtime
     > stats 10

Solutions:
  - Use streaming for faster perceived performance
  - Cache component compilation
  - Use local LLM for non-critical steps
  - Parallelize independent steps
```

---

## Conclusion

This technology stack provides a robust, flexible foundation for the SPES/PKB system, balancing:
- **Local-first privacy** (Obsidian, local LLMs)
- **Cloud power** (Claude, Gemini, GPT-4)
- **Performance** (Efficient embeddings, caching)
- **Developer experience** (Modern Python tooling)
- **User experience** (Obsidian GUI, CLI automation)

All components are actively maintained, well-documented, and production-ready.
