---
tags: #meta #mcp #troubleshooting #setup #configuration
aliases: [MCP Troubleshooting, MCP Setup Guide, Claude Desktop MCP]
status: evergreen
certainty: ^verified
created: 2026-01-06
last_updated: 2026-01-06
---

# MCP Setup & Troubleshooting Guide

> [!abstract] Purpose
> This document provides troubleshooting guidance for MCP (Model Context Protocol) server configuration with Claude Desktop, documenting known issues and solutions for enabling semantic memory retrieval.

## Context

The memory system implementation (documented in [[.claude/memory-index]]) requires an MCP server to enable Claude Desktop to perform semantic searches across the vault using Smart Connections embeddings. This guide documents the setup process and known issues encountered.

---

## Problem: Node.js ESM Module Error with @yejianye/smart-connections-mcp

### Issue Description

**Error**: `ERR_UNSUPPORTED_ESM_URL_SCHEME`
```
Error [ERR_UNSUPPORTED_ESM_URL_SCHEME]: Only URLs with a scheme in: file, data, and node are supported by the default ESM loader. On Windows, absolute paths must be valid file:// URLs. Received protocol 'c:'
```

**Affected Package**: `@yejianye/smart-connections-mcp` v1.0.0
**Node.js Version**: v22.19.0
**Platform**: Windows 11

### Root Cause

The package has a Node.js ESM module loading issue on Windows with Node.js v22. The error occurs when the MCP server attempts to load modules using Windows absolute paths (e.g., `C:\path\to\file`) which Node.js ESM loader does not accept without `file://` protocol prefix.

### Log Location

`%APPDATA%\Claude\logs\mcp-server-smart-connections.log`

**Key log entries**:
- Server initializes successfully
- Connection established
- Module loading fails immediately after initialization
- Server disconnects due to process exit

---

## Alternative Solution: @connorbritain/obsidian-mcp-server

### Package Information

- **Package**: `@connorbritain/obsidian-mcp-server` v0.2.3
- **Installation**: `npm install -g @connorbritain/obsidian-mcp-server`
- **Repository**: https://github.com/ConnorBritain/obsidian-mcp-server
- **Features**: Core tools, graph analytics, semantic search

### Prerequisites

This package requires the **Local REST API** plugin for Obsidian:

1. **Install Plugin**:
   - Open Obsidian
   - Settings → Community Plugins → Browse
   - Search for "Local REST API"
   - Install and enable

2. **Get API Key**:
   - Settings → Community Plugins → Local REST API → Settings
   - Copy the auto-generated API key

3. **Verify Plugin Running**:
   - Default host: `127.0.0.1`
   - Default port: `27124`
   - Default protocol: `https`

### Configuration

**Claude Desktop Config Location**: `%APPDATA%\Claude\claude_desktop_config.json`

**Current Configuration** (as of 2026-01-06):
```json
{
  "globalShortcut": "Ctrl+Space",
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["-y", "@connorbritain/obsidian-mcp-server"],
      "env": {
        "OBSIDIAN_VAULT_PATH": "D:\\10_pur3v4d3r's-vault"
      }
    }
  }
}
```

**Required Environment Variables**:
```json
{
  "OBSIDIAN_API_KEY": "your-api-key-here",
  "OBSIDIAN_VAULT_PATH": "D:\\10_pur3v4d3r's-vault",
  "OBSIDIAN_HOST": "127.0.0.1",
  "OBSIDIAN_PORT": "27124",
  "OBSIDIAN_PROTOCOL": "https"
}
```

**Complete Configuration Example**:
```json
{
  "globalShortcut": "Ctrl+Space",
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["-y", "@connorbritain/obsidian-mcp-server"],
      "env": {
        "OBSIDIAN_API_KEY": "your-local-rest-api-key",
        "OBSIDIAN_VAULT_PATH": "D:\\10_pur3v4d3r's-vault",
        "OBSIDIAN_HOST": "127.0.0.1",
        "OBSIDIAN_PORT": "27124",
        "OBSIDIAN_PROTOCOL": "https"
      }
    }
  }
}
```

---

## Testing MCP Connection

### Restart Claude Desktop

**CRITICAL**: Complete restart required (not just window close)
1. Close all Claude Desktop windows
2. Exit from system tray if present
3. Reopen Claude Desktop
4. Wait for MCP initialization (~5 seconds)

### Test Queries

**1. List Available Tools**:
```
Can you list your available tools?
```
**Expected**: Should show `obsidian_*` tools (e.g., `obsidian_search`, `obsidian_read_note`)

**2. Search Vault**:
```
Use the obsidian search tool to find notes about "memory system implementation"
```
**Expected**: Returns relevant notes from .claude/ directory

**3. Read Note**:
```
Read the note at .claude/core/projectbrief.md
```
**Expected**: Returns full note content

**4. Graph Query** (if vault path configured):
```
Show me notes connected to projectbrief.md
```
**Expected**: Returns linked notes from graph

### Success Criteria

✅ **MCP tools appear in tools list**
✅ **Search returns relevant vault notes**
✅ **Read operations work correctly**
✅ **No connection errors in logs**

---

## Troubleshooting Steps

### Issue: MCP Server Not Loading

**Check logs**:
```bash
# View most recent MCP log
ls -lt "C:\Users\pur3v4d3rpk\AppData\Roaming\Claude\logs" | head -5

# Read specific MCP server log
cat "C:\Users\pur3v4d3rpk\AppData\Roaming\Claude\logs\mcp-server-obsidian.log"
```

**Common causes**:
- API key not set or incorrect
- Obsidian Local REST API plugin not running
- Port conflict (another service using 27124)
- Vault path incorrect or inaccessible

### Issue: "Server Disconnected" Error

**Check**:
1. Obsidian is running with vault open
2. Local REST API plugin is enabled
3. API key matches between Obsidian and config
4. No firewall blocking localhost connections

### Issue: Tools Available but Returning Errors

**Verify**:
1. Vault path in config matches actual vault location
2. Notes have been indexed by Smart Connections
3. `.smart-env/multi/` directory contains embeddings (AJSON files)

### Issue: JSON Syntax Error in Config

**Validate JSON**:
```bash
# Test JSON syntax
cat "C:\Users\pur3v4d3rpk\AppData\Roaming\Claude\claude_desktop_config.json" | python -m json.tool
```

**Common mistakes**:
- Missing commas between sections
- Trailing commas before closing braces
- Single backslashes in Windows paths (use `\\`)
- Unescaped quotes in strings

---

## Known Limitations

### @connorbritain/obsidian-mcp-server

**Requires**:
- Local REST API plugin (external dependency)
- Obsidian running at all times
- API key management

**Does NOT support**:
- Direct Smart Connections embedding access
- Offline operation (Obsidian must be running)
- Multi-vault without configuration

### Smart Connections Integration

**Current Status**:
- Smart Connections embeddings: 8,383 files in `.smart-env/multi/`
- Model: TaylorAI/bge-micro-v2 (384 dimensions)
- Auto-indexing enabled (no folder exclusions)

**MCP Integration**:
- Indirect via Local REST API (Obsidian must query embeddings)
- Not direct embedding file access

---

## Alternative Approaches (Future Consideration)

### Option 1: Custom MCP Server

Build custom MCP server that:
- Reads `.smart-env/multi/` AJSON files directly
- Performs semantic search without Obsidian running
- Uses same embedding model for queries

**Pros**: No Obsidian dependency, faster queries
**Cons**: Requires development, maintenance

### Option 2: Downgrade Node.js

Try Node.js v20 LTS with `@yejianye/smart-connections-mcp`:
```bash
nvm install 20
nvm use 20
npm install -g @yejianye/smart-connections-mcp
```

**Pros**: Original package might work
**Cons**: Requires Node.js version management

### Option 3: Wait for Package Update

Monitor `@yejianye/smart-connections-mcp` for Windows ESM fix:
- GitHub issues: Check for similar reports
- Package updates: Watch for v1.0.1+

---

## Decision Log

### 2026-01-06: MCP Package Switch

**Decision**: Switch from `@yejianye/smart-connections-mcp` to `@connorbritain/obsidian-mcp-server`

**Reason**: ERR_UNSUPPORTED_ESM_URL_SCHEME error blocks usage on Windows with Node.js v22

**Trade-offs**:
- ✅ Working MCP integration possible
- ⚠️ Requires Local REST API plugin setup
- ⚠️ Adds dependency on Obsidian running

**Status**: Pending Local REST API key configuration

---

## Related Documentation

- [[claude-memory-system-guide]] — Overview of dual-layer architecture
- [[.claude/memory-index]] — Agent memory system navigation
- [[.claude/core/techContext]] — Complete technology stack
- [[.claude/core/progress]] — Implementation timeline and status

---

## Document History

- **2026-01-06**: Initial creation documenting MCP setup issues and solutions
- **Status**: Active troubleshooting guide

---

_Update this document when new MCP-related issues are discovered or resolved._
