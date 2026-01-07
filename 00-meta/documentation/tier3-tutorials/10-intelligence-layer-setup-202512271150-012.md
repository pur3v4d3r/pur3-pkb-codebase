---
title: SPES Intelligence Layer Setup Guide
document_type: configuration_guide
tier: 2
priority: critical
version: 2.0.0
status: published
prerequisites: ["Quick Start Guide", "Technology Stack Deep Dive"]
estimated_time: 90-120 minutes
last_updated: 2025-12-25
---

# SPES Intelligence Layer Setup Guide

**Version**: 2.0.0  
**Document Type**: Comprehensive Configuration Guide  
**Audience**: System administrators, advanced users  
**Time Required**: 90-120 minutes  
**Goal**: Configure all LLM providers with optimal settings

---

## Table of Contents

1. [Overview](#1-overview)
2. [Cloud LLMs Setup](#2-cloud-llms-setup)
3. [Local LLMs Setup](#3-local-llms-setup)
4. [Adapter Architecture](#4-adapter-architecture)
5. [Capability Detection](#5-capability-detection)
6. [Configuration Management](#6-configuration-management)
7. [Testing & Validation](#7-testing--validation)
8. [Optimization Strategies](#8-optimization-strategies)
9. [Troubleshooting](#9-troubleshooting)
10. [Best Practices](#10-best-practices)

---

## 1. Overview

### 1.1 Intelligence Layer Architecture

The Intelligence Layer provides a unified interface to multiple LLM providers:

```
┌─────────────────────────────────────────────────────────┐
│              Workflow Execution Layer                    │
└───────────────────┬─────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────┐
│           LLM Adapter Interface (Unified API)           │
├─────────────────────────────────────────────────────────┤
│  - generate(prompt) → response                          │
│  - stream(prompt) → token_iterator                      │
│  - get_capabilities() → capabilities                    │
│  - call_tools(prompt, tools) → response                 │
└───────────────────┬─────────────────────────────────────┘
                    │
        ┌───────────┼──────────┬──────────┬──────────┐
        ▼           ▼          ▼          ▼          ▼
    ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
    │ Claude │ │ Gemini │ │  GPT   │ │ Ollama │ │   LM   │
    │  API   │ │  API   │ │  API   │ │        │ │ Studio │
    └────────┘ └────────┘ └────────┘ └────────┘ └────────┘
```

### 1.2 Supported Providers

**Cloud Providers** (require API keys):
- ✅ **Claude API** - Primary, production-ready
- ✅ **Claude Code** - Agentic coding with filesystem access
- ✅ **Gemini** - Speed/cost optimization
- ⏳ **GPT-4** - Planned (architecture ready)

**Local Providers** (run on your machine):
- ✅ **Ollama** - Universal local LLM runtime
- ✅ **LM Studio** - GUI management, OpenAI-compatible
- ✅ **GPT4All** - Fully offline, minimal dependencies

### 1.3 Feature Matrix

| Provider | Streaming | Tools/Functions | Context | Speed | Privacy |
|----------|-----------|-----------------|---------|-------|---------|
| **Claude API** | ✅ | ✅ (MCP) | 200K | Fast | Cloud |
| **Claude Code** | ✅ | ✅ (Agentic) | 200K | Fast | Cloud |
| **Gemini** | ✅ | ✅ | 128K | Fastest | Cloud |
| **GPT-4** | ✅ | ✅ | 128K | Fast | Cloud |
| **Ollama** | ✅ | ❌ | 4-32K | Medium | Local |
| **LM Studio** | ✅ | ❌ | 4-32K | Medium | Local |
| **GPT4All** | ✅ | ❌ | 4-8K | Slow | Local |

---

## 2. Cloud LLMs Setup

### 2.1 Claude API Configuration

#### Step 1: Get API Key

1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to **API Keys**
4. Click **Create Key**
5. Copy the key (starts with `sk-ant-api03-`)

#### Step 2: Configure Environment

```bash
cd ~/PKB-System

# Add to .env
cat >> .env << 'EOF'

# Claude API Configuration
ANTHROPIC_API_KEY=sk-ant-api03-YOUR_KEY_HERE
ANTHROPIC_BASE_URL=https://api.anthropic.com
CLAUDE_DEFAULT_MODEL=claude-sonnet-4-20250514
CLAUDE_MAX_TOKENS=4096
CLAUDE_TEMPERATURE=0.7
EOF
```

#### Step 3: Configure in config.yml

```yaml
# config.yml
llm:
  providers:
    claude:
      enabled: true
      api_key: "${ANTHROPIC_API_KEY}"
      base_url: "${ANTHROPIC_BASE_URL}"
      models:
        sonnet-4:
          id: "claude-sonnet-4-20250514"
          context_window: 200000
          max_tokens: 4096
          cost_per_1k_input: 0.003
          cost_per_1k_output: 0.015
        opus-4:
          id: "claude-opus-4-20250514"
          context_window: 200000
          max_tokens: 4096
          cost_per_1k_input: 0.015
          cost_per_1k_output: 0.075
      default_model: "sonnet-4"
      timeout: 300
      max_retries: 3
      retry_delay: 1.0
```

#### Step 4: Create Adapter

```bash
cd ~/PKB-System/spes

# Create adapters directory
mkdir -p adapters

cat > adapters/claude_adapter.py << 'EOF'
#!/usr/bin/env python3
"""
Claude API Adapter
Provides unified interface to Claude models
"""

import os
from typing import Iterator, Optional, Dict, List, Any
from anthropic import Anthropic, Stream
from anthropic.types import Message, ContentBlock

class ClaudeAdapter:
    """Adapter for Claude API."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "claude-sonnet-4-20250514"):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.model = model
        self.client = Anthropic(api_key=self.api_key)
    
    def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        max_tokens: int = 4096,
        temperature: float = 0.7,
        **kwargs
    ) -> str:
        """Generate completion from prompt."""
        
        messages = [{"role": "user", "content": prompt}]
        
        params = {
            "model": self.model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": messages
        }
        
        if system:
            params["system"] = system
        
        response = self.client.messages.create(**params)
        return response.content[0].text
    
    def stream(
        self,
        prompt: str,
        system: Optional[str] = None,
        max_tokens: int = 4096,
        temperature: float = 0.7,
        **kwargs
    ) -> Iterator[str]:
        """Stream completion tokens."""
        
        messages = [{"role": "user", "content": prompt}]
        
        params = {
            "model": self.model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": messages
        }
        
        if system:
            params["system"] = system
        
        with self.client.messages.stream(**params) as stream:
            for text in stream.text_stream:
                yield text
    
    def call_tools(
        self,
        prompt: str,
        tools: List[Dict],
        system: Optional[str] = None,
        max_tokens: int = 4096,
        **kwargs
    ) -> Dict[str, Any]:
        """Execute with tool/function calling."""
        
        messages = [{"role": "user", "content": prompt}]
        
        params = {
            "model": self.model,
            "max_tokens": max_tokens,
            "messages": messages,
            "tools": tools
        }
        
        if system:
            params["system"] = system
        
        response = self.client.messages.create(**params)
        
        return {
            "content": response.content,
            "stop_reason": response.stop_reason,
            "usage": {
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens
            }
        }
    
    def get_capabilities(self) -> Dict[str, Any]:
        """Return adapter capabilities."""
        return {
            "provider": "claude",
            "model": self.model,
            "streaming": True,
            "tools": True,
            "context_window": 200000,
            "max_output_tokens": 4096,
            "supports_system_prompt": True,
            "supports_images": True,
            "supports_pdfs": True
        }

# Test the adapter
if __name__ == "__main__":
    adapter = ClaudeAdapter()
    
    # Test basic generation
    response = adapter.generate("Say 'Hello from Claude!' and nothing else.")
    print(f"Response: {response}")
    
    # Test streaming
    print("\nStreaming test:")
    for token in adapter.stream("Count from 1 to 5."):
        print(token, end="", flush=True)
    print()
    
    # Test capabilities
    caps = adapter.get_capabilities()
    print(f"\nCapabilities: {caps}")
EOF

# Test the adapter
python adapters/claude_adapter.py
```

### 2.2 Gemini Configuration

#### Step 1: Get API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with Google account
3. Click **Create API Key**
4. Copy the key (starts with `AIza`)

#### Step 2: Configure Environment

```bash
cd ~/PKB-System

cat >> .env << 'EOF'

# Gemini API Configuration
GOOGLE_API_KEY=AIzaYOUR_KEY_HERE
GEMINI_DEFAULT_MODEL=gemini-2.0-flash-exp
EOF
```

#### Step 3: Create Adapter

```bash
cd ~/PKB-System/spes/adapters

cat > gemini_adapter.py << 'EOF'
#!/usr/bin/env python3
"""
Gemini API Adapter
Provides unified interface to Gemini models
"""

import os
from typing import Iterator, Optional, Dict, List, Any
import google.generativeai as genai

class GeminiAdapter:
    """Adapter for Google Gemini API."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gemini-2.0-flash-exp"):
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        self.model_name = model
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model)
    
    def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        max_tokens: int = 8192,
        temperature: float = 0.7,
        **kwargs
    ) -> str:
        """Generate completion from prompt."""
        
        # Gemini uses system_instruction instead of system
        if system:
            self.model = genai.GenerativeModel(
                self.model_name,
                system_instruction=system
            )
        
        generation_config = {
            "temperature": temperature,
            "max_output_tokens": max_tokens,
        }
        
        response = self.model.generate_content(
            prompt,
            generation_config=generation_config
        )
        
        return response.text
    
    def stream(
        self,
        prompt: str,
        system: Optional[str] = None,
        max_tokens: int = 8192,
        temperature: float = 0.7,
        **kwargs
    ) -> Iterator[str]:
        """Stream completion tokens."""
        
        if system:
            self.model = genai.GenerativeModel(
                self.model_name,
                system_instruction=system
            )
        
        generation_config = {
            "temperature": temperature,
            "max_output_tokens": max_tokens,
        }
        
        response = self.model.generate_content(
            prompt,
            generation_config=generation_config,
            stream=True
        )
        
        for chunk in response:
            if chunk.text:
                yield chunk.text
    
    def call_tools(
        self,
        prompt: str,
        tools: List[Dict],
        system: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Execute with function calling."""
        
        # Convert tools to Gemini format
        gemini_tools = []
        for tool in tools:
            gemini_tools.append({
                "function_declarations": [{
                    "name": tool["name"],
                    "description": tool["description"],
                    "parameters": tool.get("parameters", {})
                }]
            })
        
        if system:
            model = genai.GenerativeModel(
                self.model_name,
                system_instruction=system,
                tools=gemini_tools
            )
        else:
            model = genai.GenerativeModel(
                self.model_name,
                tools=gemini_tools
            )
        
        response = model.generate_content(prompt)
        
        return {
            "content": response.text,
            "function_calls": [
                {
                    "name": part.function_call.name,
                    "args": dict(part.function_call.args)
                }
                for part in response.parts
                if hasattr(part, 'function_call')
            ]
        }
    
    def get_capabilities(self) -> Dict[str, Any]:
        """Return adapter capabilities."""
        return {
            "provider": "gemini",
            "model": self.model_name,
            "streaming": True,
            "tools": True,
            "context_window": 128000,
            "max_output_tokens": 8192,
            "supports_system_prompt": True,
            "supports_images": True,
            "supports_pdfs": False
        }

# Test the adapter
if __name__ == "__main__":
    adapter = GeminiAdapter()
    
    # Test basic generation
    response = adapter.generate("Say 'Hello from Gemini!' and nothing else.")
    print(f"Response: {response}")
    
    # Test streaming
    print("\nStreaming test:")
    for token in adapter.stream("Count from 1 to 3."):
        print(token, end="", flush=True)
    print()
    
    # Test capabilities
    caps = adapter.get_capabilities()
    print(f"\nCapabilities: {caps}")
EOF

python adapters/gemini_adapter.py
```

### 2.3 GPT-4 Configuration (Planned)

```bash
cd ~/PKB-System

cat >> .env << 'EOF'

# OpenAI API Configuration (when ready)
OPENAI_API_KEY=sk-YOUR_KEY_HERE
OPENAI_DEFAULT_MODEL=gpt-4-turbo
EOF
```

**Note**: GPT-4 adapter follows same pattern as Claude/Gemini. Implementation similar to examples above.

---

## 3. Local LLMs Setup

### 3.1 Ollama Setup

#### Step 1: Install Ollama

```bash
# macOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Verify installation
ollama --version
```

#### Step 2: Pull Models

```bash
# Recommended models for SPES

# General Purpose (4.7GB)
ollama pull llama3:8b

# Code Specialized (7.3GB)
ollama pull codellama:13b

# Fast/Lightweight (2.7GB)
ollama pull mistral:7b

# Advanced (26GB - requires 32GB+ RAM)
ollama pull mixtral:8x7b

# List installed models
ollama list
```

#### Step 3: Start Server

```bash
# Start Ollama server
ollama serve

# Or run in background
nohup ollama serve > logs/ollama.log 2>&1 &

# Verify server running
curl http://localhost:11434/api/version
```

#### Step 4: Configure Environment

```bash
cd ~/PKB-System

cat >> .env << 'EOF'

# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_DEFAULT_MODEL=llama3:8b
OLLAMA_TIMEOUT=300
EOF
```

#### Step 5: Create Adapter

```bash
cd ~/PKB-System/spes/adapters

cat > ollama_adapter.py << 'EOF'
#!/usr/bin/env python3
"""
Ollama Adapter
Provides unified interface to Ollama local LLMs
"""

import os
import requests
from typing import Iterator, Optional, Dict, List, Any
import json

class OllamaAdapter:
    """Adapter for Ollama local LLMs."""
    
    def __init__(
        self,
        base_url: Optional[str] = None,
        model: str = "llama3:8b"
    ):
        self.base_url = base_url or os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.model = model
    
    def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        max_tokens: int = 2048,
        temperature: float = 0.7,
        **kwargs
    ) -> str:
        """Generate completion from prompt."""
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens
            }
        }
        
        if system:
            payload["system"] = system
        
        response = requests.post(
            f"{self.base_url}/api/generate",
            json=payload,
            timeout=300
        )
        
        response.raise_for_status()
        return response.json()["response"]
    
    def stream(
        self,
        prompt: str,
        system: Optional[str] = None,
        max_tokens: int = 2048,
        temperature: float = 0.7,
        **kwargs
    ) -> Iterator[str]:
        """Stream completion tokens."""
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": True,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens
            }
        }
        
        if system:
            payload["system"] = system
        
        response = requests.post(
            f"{self.base_url}/api/generate",
            json=payload,
            stream=True,
            timeout=300
        )
        
        response.raise_for_status()
        
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line)
                if not chunk.get("done", False):
                    yield chunk.get("response", "")
    
    def call_tools(
        self,
        prompt: str,
        tools: List[Dict],
        **kwargs
    ) -> Dict[str, Any]:
        """Tool calling not supported in Ollama."""
        raise NotImplementedError("Ollama does not support native tool calling")
    
    def get_capabilities(self) -> Dict[str, Any]:
        """Return adapter capabilities."""
        
        # Get model info from Ollama
        try:
            response = requests.post(
                f"{self.base_url}/api/show",
                json={"name": self.model}
            )
            info = response.json()
            
            # Extract context window from modelfile
            context_window = 8192  # Default
            if "parameters" in info:
                for param in info["parameters"].split("\n"):
                    if "num_ctx" in param:
                        context_window = int(param.split()[-1])
        except:
            context_window = 8192
        
        return {
            "provider": "ollama",
            "model": self.model,
            "streaming": True,
            "tools": False,
            "context_window": context_window,
            "max_output_tokens": 2048,
            "supports_system_prompt": True,
            "supports_images": False,
            "supports_pdfs": False,
            "local": True
        }

# Test the adapter
if __name__ == "__main__":
    adapter = OllamaAdapter()
    
    # Test basic generation
    print("Testing generation...")
    response = adapter.generate("Say 'Hello from Ollama!' and nothing else.")
    print(f"Response: {response}")
    
    # Test streaming
    print("\nTesting streaming...")
    for token in adapter.stream("Count from 1 to 3."):
        print(token, end="", flush=True)
    print()
    
    # Test capabilities
    caps = adapter.get_capabilities()
    print(f"\nCapabilities: {caps}")
EOF

python adapters/ollama_adapter.py
```

### 3.2 LM Studio Setup

#### Step 1: Install LM Studio

```bash
# Download from https://lmstudio.ai

# macOS
brew install --cask lm-studio

# Or download installer directly
```

#### Step 2: Download Models

1. Open LM Studio
2. Click **Discover** tab
3. Search for models:
   - `TheBloke/Llama-2-7B-GGUF`
   - `TheBloke/CodeLlama-13B-GGUF`
   - `TheBloke/Mistral-7B-GGUF`
4. Click **Download** for desired quantization (Q4_K_M recommended)

#### Step 3: Start Server

1. Open LM Studio
2. Load a model (click to select)
3. Click **Local Server** tab
4. Click **Start Server**
5. Server runs at `http://localhost:1234`

#### Step 4: Create Adapter

```bash
cd ~/PKB-System/spes/adapters

cat > lmstudio_adapter.py << 'EOF'
#!/usr/bin/env python3
"""
LM Studio Adapter
Provides unified interface to LM Studio (OpenAI-compatible)
"""

import os
from typing import Iterator, Optional, Dict, List, Any
import requests
import json

class LMStudioAdapter:
    """Adapter for LM Studio local LLMs."""
    
    def __init__(
        self,
        base_url: Optional[str] = None,
        model: str = "local-model"
    ):
        self.base_url = base_url or "http://localhost:1234/v1"
        self.model = model
    
    def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        max_tokens: int = 2048,
        temperature: float = 0.7,
        **kwargs
    ) -> str:
        """Generate completion from prompt."""
        
        messages = []
        
        if system:
            messages.append({"role": "system", "content": system})
        
        messages.append({"role": "user", "content": prompt})
        
        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": False
        }
        
        response = requests.post(
            f"{self.base_url}/chat/completions",
            json=payload,
            timeout=300
        )
        
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    
    def stream(
        self,
        prompt: str,
        system: Optional[str] = None,
        max_tokens: int = 2048,
        temperature: float = 0.7,
        **kwargs
    ) -> Iterator[str]:
        """Stream completion tokens."""
        
        messages = []
        
        if system:
            messages.append({"role": "system", "content": system})
        
        messages.append({"role": "user", "content": prompt})
        
        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": True
        }
        
        response = requests.post(
            f"{self.base_url}/chat/completions",
            json=payload,
            stream=True,
            timeout=300
        )
        
        response.raise_for_status()
        
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith('data: '):
                    line = line[6:]  # Remove 'data: ' prefix
                    if line.strip() == '[DONE]':
                        break
                    try:
                        chunk = json.loads(line)
                        delta = chunk['choices'][0].get('delta', {})
                        if 'content' in delta:
                            yield delta['content']
                    except json.JSONDecodeError:
                        pass
    
    def get_capabilities(self) -> Dict[str, Any]:
        """Return adapter capabilities."""
        return {
            "provider": "lmstudio",
            "model": self.model,
            "streaming": True,
            "tools": False,
            "context_window": 4096,  # Varies by model
            "max_output_tokens": 2048,
            "supports_system_prompt": True,
            "supports_images": False,
            "supports_pdfs": False,
            "local": True
        }

# Test the adapter
if __name__ == "__main__":
    import sys
    
    try:
        adapter = LMStudioAdapter()
        
        # Test generation
        print("Testing generation...")
        response = adapter.generate("Say 'Hello from LM Studio!' and nothing else.")
        print(f"Response: {response}")
        
        # Test capabilities
        caps = adapter.get_capabilities()
        print(f"\nCapabilities: {caps}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure LM Studio is running with server started!")
        sys.exit(1)
EOF

python adapters/lmstudio_adapter.py
```

### 3.3 GPT4All Setup

#### Step 1: Install GPT4All

```bash
cd ~/PKB-System/spes-env

# Activate venv
source bin/activate

# Install GPT4All Python bindings
pip install gpt4all
```

#### Step 2: Download Models

Models auto-download on first use, or manually:

```python
python3 << 'EOF'
from gpt4all import GPT4All

# Download recommended models
models = [
    "mistral-7b-openorca.Q4_0.gguf",  # General purpose
    "orca-mini-3b-gguf2-q4_0.gguf",   # Fast, lightweight
]

for model_name in models:
    print(f"Downloading {model_name}...")
    model = GPT4All(model_name)
    print(f"✓ {model_name} ready")
EOF
```

#### Step 3: Create Adapter

```bash
cd ~/PKB-System/spes/adapters

cat > gpt4all_adapter.py << 'EOF'
#!/usr/bin/env python3
"""
GPT4All Adapter
Provides unified interface to GPT4All local LLMs
"""

from typing import Iterator, Optional, Dict, Any, List
from gpt4all import GPT4All

class GPT4AllAdapter:
    """Adapter for GPT4All local LLMs."""
    
    def __init__(self, model: str = "mistral-7b-openorca.Q4_0.gguf"):
        self.model_name = model
        self.model = GPT4All(model)
    
    def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        max_tokens: int = 2048,
        temperature: float = 0.7,
        **kwargs
    ) -> str:
        """Generate completion from prompt."""
        
        # GPT4All doesn't have native system prompt support
        # Prepend system message to prompt
        if system:
            full_prompt = f"System: {system}\n\nUser: {prompt}\n\nAssistant:"
        else:
            full_prompt = prompt
        
        response = self.model.generate(
            full_prompt,
            max_tokens=max_tokens,
            temp=temperature
        )
        
        return response
    
    def stream(
        self,
        prompt: str,
        system: Optional[str] = None,
        max_tokens: int = 2048,
        temperature: float = 0.7,
        **kwargs
    ) -> Iterator[str]:
        """Stream completion tokens."""
        
        if system:
            full_prompt = f"System: {system}\n\nUser: {prompt}\n\nAssistant:"
        else:
            full_prompt = prompt
        
        for token in self.model.generate(
            full_prompt,
            max_tokens=max_tokens,
            temp=temperature,
            streaming=True
        ):
            yield token
    
    def get_capabilities(self) -> Dict[str, Any]:
        """Return adapter capabilities."""
        return {
            "provider": "gpt4all",
            "model": self.model_name,
            "streaming": True,
            "tools": False,
            "context_window": 8192,
            "max_output_tokens": 2048,
            "supports_system_prompt": False,  # Simulated
            "supports_images": False,
            "supports_pdfs": False,
            "local": True,
            "offline": True
        }

# Test the adapter
if __name__ == "__main__":
    print("Initializing GPT4All (may download model on first run)...")
    adapter = GPT4AllAdapter()
    
    # Test generation
    print("\nTesting generation...")
    response = adapter.generate("Say 'Hello from GPT4All!' and nothing else.")
    print(f"Response: {response}")
    
    # Test capabilities
    caps = adapter.get_capabilities()
    print(f"\nCapabilities: {caps}")
EOF

python adapters/gpt4all_adapter.py
```

---

## 4. Adapter Architecture

### 4.1 Unified Adapter Interface

All adapters implement a common interface:

```python
# adapters/base_adapter.py
from abc import ABC, abstractmethod
from typing import Iterator, Optional, Dict, List, Any

class BaseLLMAdapter(ABC):
    """Base class for all LLM adapters."""
    
    @abstractmethod
    def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        max_tokens: int = 4096,
        temperature: float = 0.7,
        **kwargs
    ) -> str:
        """Generate a completion from the prompt."""
        pass
    
    @abstractmethod
    def stream(
        self,
        prompt: str,
        system: Optional[str] = None,
        max_tokens: int = 4096,
        temperature: float = 0.7,
        **kwargs
    ) -> Iterator[str]:
        """Stream completion tokens."""
        pass
    
    @abstractmethod
    def get_capabilities(self) -> Dict[str, Any]:
        """Return adapter capabilities."""
        pass
    
    def call_tools(
        self,
        prompt: str,
        tools: List[Dict],
        **kwargs
    ) -> Dict[str, Any]:
        """Execute with tool/function calling (optional)."""
        raise NotImplementedError(
            f"{self.__class__.__name__} does not support tool calling"
        )
```

### 4.2 Adapter Manager

Centralized management of all adapters:

```bash
cd ~/PKB-System/spes/adapters

cat > adapter_manager.py << 'EOF'
#!/usr/bin/env python3
"""
LLM Adapter Manager
Centralized access to all LLM providers
"""

import os
from typing import Optional, Dict, Any
from enum import Enum

# Import all adapters
from .claude_adapter import ClaudeAdapter
from .gemini_adapter import GeminiAdapter
from .ollama_adapter import OllamaAdapter
from .lmstudio_adapter import LMStudioAdapter
from .gpt4all_adapter import GPT4AllAdapter

class LLMProvider(Enum):
    """Available LLM providers."""
    CLAUDE = "claude"
    GEMINI = "gemini"
    GPT4 = "gpt4"
    OLLAMA = "ollama"
    LMSTUDIO = "lmstudio"
    GPT4ALL = "gpt4all"

class AdapterManager:
    """Manage all LLM adapters."""
    
    def __init__(self):
        self.adapters = {}
        self._initialize_adapters()
    
    def _initialize_adapters(self):
        """Initialize available adapters."""
        
        # Claude
        if os.getenv("ANTHROPIC_API_KEY"):
            try:
                self.adapters[LLMProvider.CLAUDE] = ClaudeAdapter()
            except Exception as e:
                print(f"Warning: Could not initialize Claude adapter: {e}")
        
        # Gemini
        if os.getenv("GOOGLE_API_KEY"):
            try:
                self.adapters[LLMProvider.GEMINI] = GeminiAdapter()
            except Exception as e:
                print(f"Warning: Could not initialize Gemini adapter: {e}")
        
        # Ollama (check if server running)
        try:
            import requests
            requests.get("http://localhost:11434/api/version", timeout=1)
            self.adapters[LLMProvider.OLLAMA] = OllamaAdapter()
        except:
            pass
        
        # LM Studio (check if server running)
        try:
            import requests
            requests.get("http://localhost:1234/v1/models", timeout=1)
            self.adapters[LLMProvider.LMSTUDIO] = LMStudioAdapter()
        except:
            pass
        
        # GPT4All (always available if installed)
        try:
            self.adapters[LLMProvider.GPT4ALL] = GPT4AllAdapter()
        except:
            pass
    
    def get_adapter(
        self,
        provider: LLMProvider,
        fallback: Optional[LLMProvider] = None
    ):
        """Get adapter for provider, with optional fallback."""
        
        if provider in self.adapters:
            return self.adapters[provider]
        
        if fallback and fallback in self.adapters:
            print(f"Warning: {provider.value} not available, using {fallback.value}")
            return self.adapters[fallback]
        
        raise ValueError(
            f"Provider {provider.value} not available. "
            f"Available: {[p.value for p in self.adapters.keys()]}"
        )
    
    def list_available(self) -> Dict[str, Dict[str, Any]]:
        """List all available adapters with capabilities."""
        
        return {
            provider.value: adapter.get_capabilities()
            for provider, adapter in self.adapters.items()
        }
    
    def auto_select(
        self,
        task_type: str,
        prefer_local: bool = False
    ) -> LLMProvider:
        """Auto-select best adapter for task type."""
        
        # Task-based selection
        if task_type == "code" and LLMProvider.CLAUDE in self.adapters:
            return LLMProvider.CLAUDE
        
        if task_type == "fast" and LLMProvider.GEMINI in self.adapters:
            return LLMProvider.GEMINI
        
        # Privacy/local preference
        if prefer_local:
            for provider in [LLMProvider.OLLAMA, LLMProvider.LMSTUDIO, LLMProvider.GPT4ALL]:
                if provider in self.adapters:
                    return provider
        
        # Default: best available cloud
        for provider in [LLMProvider.CLAUDE, LLMProvider.GEMINI]:
            if provider in self.adapters:
                return provider
        
        # Fallback: any available
        if self.adapters:
            return list(self.adapters.keys())[0]
        
        raise ValueError("No LLM adapters available!")

# Test the manager
if __name__ == "__main__":
    manager = AdapterManager()
    
    print("Available Adapters:")
    print("="*60)
    for provider, caps in manager.list_available().items():
        print(f"\n{provider.upper()}:")
        print(f"  Model: {caps['model']}")
        print(f"  Context: {caps['context_window']:,} tokens")
        print(f"  Streaming: {caps['streaming']}")
        print(f"  Tools: {caps['tools']}")
        print(f"  Local: {caps.get('local', False)}")
    
    print("\n" + "="*60)
    print("Auto-selection tests:")
    print(f"  Code task: {manager.auto_select('code').value}")
    print(f"  Fast task: {manager.auto_select('fast').value}")
    print(f"  Local preferred: {manager.auto_select('any', prefer_local=True).value}")
EOF

# Create __init__.py for package
cat > __init__.py << 'EOF'
from .adapter_manager import AdapterManager, LLMProvider
from .base_adapter import BaseLLMAdapter

__all__ = ['AdapterManager', 'LLMProvider', 'BaseLLMAdapter']
EOF

python adapters/adapter_manager.py
```

---

## 5. Capability Detection

### 5.1 Runtime Capability Check

```python
# adapters/capability_detector.py
class CapabilityDetector:
    """Detect and validate LLM capabilities at runtime."""
    
    def __init__(self, adapter):
        self.adapter = adapter
        self.capabilities = adapter.get_capabilities()
    
    def supports_streaming(self) -> bool:
        """Check if adapter supports streaming."""
        return self.capabilities.get("streaming", False)
    
    def supports_tools(self) -> bool:
        """Check if adapter supports tool/function calling."""
        return self.capabilities.get("tools", False)
    
    def get_context_window(self) -> int:
        """Get maximum context window size."""
        return self.capabilities.get("context_window", 4096)
    
    def get_max_output_tokens(self) -> int:
        """Get maximum output tokens."""
        return self.capabilities.get("max_output_tokens", 2048)
    
    def is_local(self) -> bool:
        """Check if this is a local LLM."""
        return self.capabilities.get("local", False)
    
    def estimate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Estimate cost for request (cloud LLMs only)."""
        if self.is_local():
            return 0.0
        
        input_cost = self.capabilities.get("cost_per_1k_input", 0)
        output_cost = self.capabilities.get("cost_per_1k_output", 0)
        
        total = (input_tokens / 1000 * input_cost) + (output_tokens / 1000 * output_cost)
        return round(total, 6)
    
    def can_handle_prompt(self, prompt_length: int, desired_output: int = 2048) -> bool:
        """Check if adapter can handle prompt size."""
        context_window = self.get_context_window()
        max_output = self.get_max_output_tokens()
        
        # Need room for both prompt and output
        total_needed = prompt_length + min(desired_output, max_output)
        
        return total_needed <= context_window
```

---

## 6. Configuration Management

### 6.1 Complete Configuration File

```yaml
# config.yml - Complete LLM configuration
llm:
  # Default providers
  default_cloud: claude
  default_local: ollama
  fallback: gemini
  
  # Provider configurations
  providers:
    claude:
      enabled: true
      api_key: "${ANTHROPIC_API_KEY}"
      models:
        sonnet-4:
          id: "claude-sonnet-4-20250514"
          context_window: 200000
          max_tokens: 4096
          cost_per_1k_input: 0.003
          cost_per_1k_output: 0.015
      default_model: "sonnet-4"
      timeout: 300
      max_retries: 3
    
    gemini:
      enabled: true
      api_key: "${GOOGLE_API_KEY}"
      models:
        flash-2:
          id: "gemini-2.0-flash-exp"
          context_window: 128000
          max_tokens: 8192
          cost_per_1k_input: 0.0001
          cost_per_1k_output: 0.0005
      default_model: "flash-2"
      timeout: 300
      max_retries: 3
    
    ollama:
      enabled: true
      base_url: "${OLLAMA_BASE_URL}"
      models:
        llama3-8b:
          id: "llama3:8b"
          context_window: 8192
          max_tokens: 2048
        codellama-13b:
          id: "codellama:13b"
          context_window: 16384
          max_tokens: 4096
      default_model: "llama3-8b"
      timeout: 300
    
    lmstudio:
      enabled: false  # Enable when running
      base_url: "http://localhost:1234/v1"
      default_model: "local-model"
      timeout: 300
    
    gpt4all:
      enabled: true
      models:
        mistral:
          id: "mistral-7b-openorca.Q4_0.gguf"
          context_window: 8192
          max_tokens: 2048
      default_model: "mistral"
  
  # Selection strategy
  selection:
    # Task-based routing
    code_generation: claude
    fast_analysis: gemini
    local_private: ollama
    bulk_processing: gemini
    
    # Fallback chain
    fallback_chain:
      - claude
      - gemini
      - ollama
```

---

## 7. Testing & Validation

### 7.1 Comprehensive Test Suite

```bash
cd ~/PKB-System/spes

cat > test_llm_setup.py << 'EOF'
#!/usr/bin/env python3
"""
Comprehensive LLM Setup Testing
Validates all configured providers
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from adapters import AdapterManager, LLMProvider
from dotenv import load_dotenv

load_dotenv()

def test_adapter(provider: LLMProvider, manager: AdapterManager):
    """Test a single adapter."""
    
    print(f"\n{'='*60}")
    print(f"Testing: {provider.value.upper()}")
    print('='*60)
    
    try:
        adapter = manager.get_adapter(provider)
        
        # Test 1: Capabilities
        print("\n1. Capabilities:")
        caps = adapter.get_capabilities()
        print(f"   Model: {caps['model']}")
        print(f"   Context: {caps['context_window']:,} tokens")
        print(f"   Max Output: {caps['max_output_tokens']:,} tokens")
        print(f"   Streaming: {caps['streaming']}")
        print(f"   Tools: {caps['tools']}")
        print(f"   Local: {caps.get('local', False)}")
        
        # Test 2: Basic Generation
        print("\n2. Basic Generation:")
        response = adapter.generate(
            "Respond with exactly: 'LLM test successful'",
            max_tokens=50
        )
        print(f"   Response: {response[:100]}")
        
        # Test 3: Streaming
        print("\n3. Streaming Test:")
        print("   Output: ", end="")
        for token in adapter.stream("Count: 1, 2, 3", max_tokens=20):
            print(token, end="", flush=True)
        print()
        
        # Test 4: System Prompt (if supported)
        if caps.get("supports_system_prompt", False):
            print("\n4. System Prompt:")
            response = adapter.generate(
                "What is your role?",
                system="You are a helpful math tutor.",
                max_tokens=50
            )
            print(f"   Response: {response[:100]}")
        
        print(f"\n✓ {provider.value.upper()} - All tests passed!")
        return True
        
    except Exception as e:
        print(f"\n✗ {provider.value.upper()} - Test failed: {e}")
        return False

def main():
    """Run comprehensive tests."""
    
    print("="*60)
    print("SPES LLM Setup Validation")
    print("="*60)
    
    manager = AdapterManager()
    
    # List available providers
    available = manager.list_available()
    print(f"\nFound {len(available)} available provider(s):")
    for provider in available:
        print(f"  - {provider}")
    
    if not available:
        print("\n✗ No LLM providers configured!")
        print("\nSetup required:")
        print("  1. Add API keys to .env file")
        print("  2. Start Ollama server (for local LLMs)")
        print("  3. Rerun this test")
        return 1
    
    # Test each provider
    results = {}
    for provider_str in available:
        provider = LLMProvider(provider_str)
        results[provider] = test_adapter(provider, manager)
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for r in results.values() if r)
    total = len(results)
    
    for provider, success in results.items():
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"{status}: {provider.value.upper()}")
    
    print(f"\nResults: {passed}/{total} providers passed")
    
    if passed == total:
        print("\n✓ All configured providers working correctly!")
        return 0
    else:
        print(f"\n⚠ {total - passed} provider(s) need attention")
        return 1

if __name__ == "__main__":
    sys.exit(main())
EOF

chmod +x test_llm_setup.py

# Run comprehensive test
python test_llm_setup.py
```

---

## 8. Optimization Strategies

### 8.1 Component Optimization for Local LLMs

Local LLMs have smaller context windows. Optimize components:

```python
# Component compression for local LLMs
def compress_component_for_local(component: str, target_length: int = 500) -> str:
    """Compress component for local LLM constraints."""
    
    if len(component) <= target_length:
        return component
    
    # Strategy 1: Remove examples
    if "## Examples" in component:
        component = component.split("## Examples")[0]
    
    # Strategy 2: Condense verbose sections
    # Keep only essential instructions
    
    # Strategy 3: Remove redundancy
    lines = component.split("\n")
    essential_lines = [
        line for line in lines
        if line.strip() and not line.startswith("#")
    ]
    
    return "\n".join(essential_lines[:target_length // 50])
```

### 8.2 Smart LLM Routing

```python
def route_to_optimal_llm(
    task_characteristics: dict,
    manager: AdapterManager
) -> LLMProvider:
    """Route task to optimal LLM based on characteristics."""
    
    # Privacy-sensitive → Local only
    if task_characteristics.get("privacy_sensitive"):
        for provider in [LLMProvider.OLLAMA, LLMProvider.GPT4ALL]:
            try:
                manager.get_adapter(provider)
                return provider
            except:
                pass
        raise ValueError("No local LLM available for private task")
    
    # High token count → Use largest context
    if task_characteristics.get("long_context"):
        return LLMProvider.CLAUDE  # 200K context
    
    # Speed critical → Fastest LLM
    if task_characteristics.get("latency_critical"):
        return LLMProvider.GEMINI
    
    # Cost sensitive → Cheapest option
    if task_characteristics.get("cost_sensitive"):
        # Try local first
        for provider in [LLMProvider.OLLAMA, LLMProvider.LMSTUDIO]:
            try:
                manager.get_adapter(provider)
                return provider
            except:
                pass
        return LLMProvider.GEMINI  # Cheapest cloud
    
    # Code generation → Best for code
    if task_characteristics.get("code_task"):
        return LLMProvider.CLAUDE
    
    # Default: Claude
    return LLMProvider.CLAUDE
```

---

## 9. Troubleshooting

### Common Issues and Solutions

**Issue**: "Claude API key not found"
```bash
# Solution
cat .env | grep ANTHROPIC_API_KEY
# If empty, add: ANTHROPIC_API_KEY=sk-ant-api03-...

# Reload environment
python3 -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('ANTHROPIC_API_KEY')[:20])"
```

**Issue**: "Ollama connection refused"
```bash
# Check if Ollama running
curl http://localhost:11434/api/version

# If not running
ollama serve

# Or start in background
nohup ollama serve > logs/ollama.log 2>&1 &
```

**Issue**: "Rate limit exceeded"
```python
# Add retry logic
from tenacity import retry, wait_exponential, stop_after_attempt

@retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(5))
def generate_with_retry(adapter, prompt):
    return adapter.generate(prompt)
```

---

## 10. Best Practices

### 10.1 Configuration Management
- ✅ Use environment variables for secrets
- ✅ Version control config files (without secrets)
- ✅ Document all configuration options
- ✅ Provide sensible defaults

### 10.2 Cost Optimization
- Use local LLMs for development/testing
- Route bulk tasks to cheapest provider (Gemini)
- Cache frequent requests
- Monitor token usage

### 10.3 Reliability
- Implement fallback chains
- Add retry logic with exponential backoff
- Validate adapter availability before use
- Log all LLM calls for debugging

---

## Conclusion

**You've configured the complete SPES Intelligence Layer!** 🎉

**What You've Set Up**:
- ✅ Cloud LLMs (Claude, Gemini)
- ✅ Local LLMs (Ollama, LM Studio, GPT4All)
- ✅ Unified adapter architecture
- ✅ Capability detection
- ✅ Smart routing
- ✅ Comprehensive testing

**Next Steps**:
1. Test with real workflows
2. Monitor performance and costs
3. Fine-tune routing strategies
4. Add more models as needed

**Time Invested**: ⏱️ 90-120 minutes  
**Ready For**: Production multi-LLM workflows
