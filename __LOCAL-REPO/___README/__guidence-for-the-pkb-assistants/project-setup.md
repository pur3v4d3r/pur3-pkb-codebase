# Project Setup

Initialize new projects with established best practices, coding standards, and tooling from day one.

## When to Use

- Starting a new project from scratch
- Onboarding an existing codebase to Context Engineering Kit
- Establishing consistent development standards across a team
- Setting up AI-assisted development infrastructure

## Plugins needed for this workflow

- [SDD](../plugins/sdd/README.md)
- [Tech Stack](../plugins/tech-stack/README.md)
- [DDD](../plugins/ddd/README.md)
- [MCP](../plugins/mcp/README.md)
- [Docs](../plugins/docs/README.md)

## Workflow

### How It Works

```md
┌─────────────────────────────────────────────┐
│ 1. Establish Project Constitution           │
│    (create specs/constitution.md)           │
└────────────────────┬────────────────────────┘
                     │
                     │ define tech stack and architecture principles
                     ▼
┌─────────────────────────────────────────────┐
│ 2. Setup Language Best Practices            │
│    (update CLAUDE.md)                       │
└────────────────────┬────────────────────────┘
                     │
                     │ add language-specific guidelines
                     ▼
┌─────────────────────────────────────────────┐
│ 3. Setup Code Quality Standards             │
│    (update CLAUDE.md)                       │
└────────────────────┬────────────────────────┘
                     │
                     │ add formatting and style rules
                     ▼
┌─────────────────────────────────────────────┐
│ 4. Setup MCP Servers (optional)             │
│    (configure external tools)               │
└────────────────────┬────────────────────────┘
                     │
                     │ enable documentation and code retrieval
                     ▼
┌─────────────────────────────────────────────┐
│ 5. Document Project Setup                   │
│    (update docs/ directory)                 │
└─────────────────────────────────────────────┘
```

### 0. Init claude code

Use the `/init` command to initialize your project.

```bash
claude /init
```

After LLM completes, review the `CLAUDE.md` file and adjust any principles or constraints. 

### 1. Establish project constitution

Use the `/sdd:00-setup` command to create your project's governing principles and development guidelines. This creates `specs/constitution.md` which guides all subsequent development.

```bash
/sdd:00-setup Use FastAPI, PostgreSQL, pytest, follow Clean Architecture
```

After LLM completes, review `specs/constitution.md` and adjust any principles or constraints. This file serves as the source of truth for architectural decisions.

### 2. Setup language best practices

Use the `/tech-stack:add-typescript-best-practices` command to add language-specific coding standards to your `CLAUDE.md` file.

```bash
/tech-stack:add-typescript-best-practices
```

After LLM completes, review the added guidelines in `CLAUDE.md`. These rules ensure consistent code style and patterns across all AI-assisted development.

### 3. Setup code quality standards

Use the `/ddd:setup-code-formating` command to establish code formatting rules and style guidelines.

```bash
/ddd:setup-code-formating
```

After LLM completes, review the formatting rules added to `CLAUDE.md`. These standards ensure consistent code structure following Clean Architecture and SOLID principles.

### 4. Setup MCP servers (optional)

Use MCP commands to integrate external tools that enhance AI capabilities. Choose based on your project needs:

**For documentation retrieval** - loads documentation for specific technologies:

```bash
/mcp:setup-context7-mcp
```

**For semantic code retrieval** - enables advanced code search and editing:

```bash
/mcp:setup-serena-mcp
```

After LLM completes for each command, follow the setup instructions provided. MCP servers extend Claude's capabilities with project-specific context.

### 5. Document project setup

Use the `/docs:update-docs` command to generate initial project documentation based on your setup.

```bash
/docs:update-docs
```

After LLM completes, review the generated documentation in the `docs/` directory. This provides a foundation for onboarding team members and maintaining project knowledge.

## What You Get

After completing this workflow, your project will have:

- **`specs/constitution.md`** - Project principles and architectural guidelines
- **`CLAUDE.md`** - AI assistant configuration with coding standards
- **`docs/`** - Initial project documentation
- **MCP integrations** - Enhanced tooling for documentation and code retrieval (if configured)
