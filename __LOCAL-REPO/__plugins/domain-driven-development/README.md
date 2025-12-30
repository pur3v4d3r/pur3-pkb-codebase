# Domain-Driven Development Plugin

Code quality framework that embeds Clean Architecture, SOLID principles, and Domain-Driven Design patterns into your development workflow through persistent memory updates and contextual skills.

Focused on:

- **Clean Architecture** - Separation of concerns with layered architecture boundaries
- **Domain-Driven Design** - Ubiquitous language and bounded contexts for complex domains
- **SOLID Principles** - Single responsibility, open-closed, and dependency inversion patterns
- **Code Quality Standards** - Consistent formatting, naming conventions, and anti-pattern avoidance

## Overview

The DDD plugin implements battle-tested software architecture principles that have proven essential for building maintainable, scalable systems. It provides commands to configure AI-assisted development with established best practices, and skills that guide code generation toward high-quality patterns.

The plugin is based on foundational works including Eric Evans' "Domain-Driven Design" (2003), Robert C. Martin's "Clean Architecture" (2017), and the SOLID principles that have become industry standards for object-oriented design.

These principles address the core challenge of software development: **managing complexity**. By establishing clear boundaries between business logic and infrastructure, using domain-specific naming, and following proven design patterns, teams can build systems that remain understandable and modifiable as they grow.

## Quick Start

```bash
# Install the plugin
/plugin install ddd@NeoLabHQ/context-engineering-kit

# Set up code formatting standards in CLAUDE.md
/ddd:setup-code-formating

# The software-architecture skill activates automatically when writing code
# alternatively, you can ask Claude to use DDD directly
> claude "Use DDD skill to implement user authentication"
```

[Usage Examples](./usage-examples.md)

## Commands Overview

### /ddd:setup-code-formating - Code Style Configuration

Establishes consistent code formatting rules and style guidelines by updating your project's CLAUDE.md file with enforced standards.

- Purpose - Configure AI-assisted development with consistent code style
- Output - Updated CLAUDE.md with formatting rules

```bash
/ddd:setup-code-formating
```

#### Arguments

None required - creates standard formatting configuration.

#### How It Works

1. **Configuration Detection**: Checks for existing CLAUDE.md in the project root
2. **Standards Application**: Adds or updates the Code Style Rules section with:
   - Semicolon usage rules
   - Quote style enforcement
   - Curly brace conventions
   - Indentation standards
   - Import ordering guidelines

3. **Persistent Memory**: Rules are written to CLAUDE.md, ensuring all future AI interactions follow the same standards

**Formatting Rules Applied**

The command configures the following standards:

| Rule | Setting | Purpose |
|------|---------|---------|
| Semicolons | No semicolons | Cleaner, modern JavaScript/TypeScript |
| Quotes | Single quotes | Consistency across codebase |
| Curly braces | Minimal (no unnecessary) | Reduced visual noise |
| Indentation | 2 spaces | Readable, compact code |
| Import order | External, Internal, Types | Logical organization |

#### Usage Examples

```bash
# Basic setup - adds formatting rules to CLAUDE.md
/ddd:setup-code-formating

# Typically used during project initialization
/sdd:00-setup Use React, TypeScript, Node.js
/tech-stack:add-typescript-best-practices
/ddd:setup-code-formating
```

#### Best Practices

- Run early in project setup - Establish standards before significant code is written
- Combine with linting tools - Use ESLint/Prettier to enforce rules automatically
- Team alignment - Ensure all team members use the same CLAUDE.md configuration
- Review generated rules - Adjust the CLAUDE.md output if your project has different conventions

## Skills Overview

### software-architecture - Quality-Focused Development Guidance

The software-architecture skill provides comprehensive guidance for writing high-quality, maintainable code. It activates automatically when users engage in code writing, architecture design, or code analysis tasks.

#### What It Provides

**General Principles**

- **Early Return Pattern**: Prefer early returns over nested conditions for improved readability
- **DRY (Don't Repeat Yourself)**: Create reusable functions and modules to avoid duplication
- **Function Decomposition**: Break down long functions (>80 lines) into smaller, focused units
- **File Size Limits**: Keep files under 200 lines; split when necessary
- **Arrow Functions**: Prefer arrow functions over function declarations

**Library-First Approach**

The skill emphasizes leveraging existing solutions before writing custom code:

```
ALWAYS search for existing solutions before writing custom code:
1. Check npm/package registries for existing libraries
2. Evaluate SaaS solutions and third-party APIs
3. Consider whether custom code is truly justified
```

Custom code is justified only when:
- Implementing specific business logic unique to the domain
- Performance-critical paths require special optimization
- External dependencies would be overkill for the use case
- Security-sensitive code requires full control
- Existing solutions don't meet requirements after thorough evaluation

**Clean Architecture and DDD Principles**

The skill enforces architectural boundaries:

- **Domain Layer**: Business entities independent of frameworks
- **Use Case Layer**: Application-specific business rules
- **Interface Layer**: Controllers, presenters, gateways
- **Infrastructure Layer**: Frameworks, databases, external services

**Naming Conventions**

| Avoid | Prefer | Reason |
|-------|--------|--------|
| `utils.js` | `OrderCalculator.js` | Domain-specific purpose |
| `helpers/misc.js` | `UserAuthenticator.js` | Clear responsibility |
| `common/shared.js` | `InvoiceGenerator.js` | Single bounded context |

**Anti-Patterns to Avoid**

The skill warns against common architectural mistakes:

- **NIH (Not Invented Here) Syndrome**: Don't build custom auth when Auth0/Supabase exists; don't write custom state management instead of Redux/Zustand
- **Mixing Concerns**: Business logic in UI components, database queries in controllers
- **Generic Naming**: `utils.js` with 50 unrelated functions, `helpers/misc.js` as a dumping ground

**Code Quality Standards**

- Proper error handling with typed catch blocks
- Maximum 3 levels of nesting
- Functions under 50 lines when possible
- Files under 200 lines when possible

#### When It Activates

The skill automatically applies when:
- Writing new code or features
- Designing system architecture
- Analyzing existing code
- Reviewing code for quality issues
- Refactoring legacy code

## Foundation

The DDD plugin is based on foundational software engineering literature that has shaped modern development practices:

### Core Literature

- **[Domain-Driven Design](https://www.domainlanguage.com/ddd/)** (Eric Evans, 2003) - Introduced ubiquitous language, bounded contexts, and strategic design patterns for managing complex domains
- **[Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)** (Robert C. Martin, 2012/2017) - Defines dependency rules and layer boundaries for maintainable systems
- **[SOLID Principles](https://en.wikipedia.org/wiki/SOLID)** (Robert C. Martin, 2000s) - Five principles of object-oriented design that promote maintainability

### Key Concepts Applied

| Concept | Source | Application in Plugin |
|---------|--------|----------------------|
| Ubiquitous Language | Evans (DDD) | Domain-specific naming conventions |
| Bounded Contexts | Evans (DDD) | Module and file organization |
| Dependency Inversion | Martin (SOLID) | Layer separation rules |
| Single Responsibility | Martin (SOLID) | Function and file size limits |
| Separation of Concerns | General | Business logic isolation |
