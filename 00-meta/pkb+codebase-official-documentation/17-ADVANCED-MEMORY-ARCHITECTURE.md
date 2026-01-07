---
title: SPES Advanced Memory Architecture
document_type: tier4_advanced
tier: 4
priority: critical
version: 1.0.0
status: published
prerequisites: ["PKB Integration Systems", "Testing Frameworks"]
estimated_time: 240-270 minutes
complexity: very_complex
last_updated: 2025-12-27
---

# Advanced Memory Architecture for SPES

**Version**: 1.0.0  
**Document Type**: Tier 4 - Advanced Implementation  
**Audience**: System architects, advanced practitioners  
**Time Required**: 240-270 minutes (4-4.5 hours)  
**Goal**: Implement production-grade three-layer cognitive memory system

---

## Table of Contents

1. [Three-Layer Memory Hierarchy](#1-three-layer-memory-hierarchy)
2. [File-Based Persistent Storage](#2-file-based-persistent-storage)
3. [Event-Driven Memory Management](#3-event-driven-memory-management)
4. [Memory Consolidation Strategies](#4-memory-consolidation-strategies)
5. [Self-Healing Mechanisms](#5-self-healing-mechanisms)
6. [Version Control for Memory](#6-version-control-for-memory)
7. [Production Implementation](#7-production-implementation)

---

## Overview

> **Critical Understanding**: LLMs face a fundamental challenge—**complete memory loss between sessions**. While context windows now reach 100K+ tokens, they cannot hold entire codebases, and accumulated knowledge vanishes when the session ends. This document presents a production-grade solution: a **three-layer cognitive memory architecture** that mirrors human memory systems.

### The Memory Challenge

**Current LLM Limitations**:
1. **Context Window Constraints**: Even 100K tokens cannot hold large projects
2. **Session Discontinuity**: Complete memory reset between conversations
3. **Attention Degradation**: Early context receives diminished focus
4. **No Learning**: Knowledge from one session doesn't transfer to the next

### The Solution: Cognitive Memory Architecture

**Core Principle**: Treat the file system as a literal extension of LLM cognition, implementing memory layers that mirror the **Atkinson-Shiffrin Model** of human memory.

```
Human Memory Model          →    LLM Memory Implementation
────────────────────────────────────────────────────────────
Working Memory (7±2 items)  →    activeContext.md (current state)
Short-Term Memory (minutes) →    task-logs/ (recent sessions)
Long-Term Memory (lifetime) →    core/ (project knowledge)
```

**Key Insight**: After each session reset, the LLM relies **ENTIRELY** on the memory bank to understand projects and continue work. This creates architectural pressure for completeness and precision.

---

## 1. Three-Layer Memory Hierarchy

### 1.1 Theoretical Foundation: Atkinson-Shiffrin Model

The **Atkinson-Shiffrin Model** (1968) describes human memory as a three-stage process:

```
Sensory Input
    ↓
Working Memory (active processing, limited capacity)
    ↓ [rehearsal/consolidation]
Short-Term Memory (temporary storage, minutes to hours)
    ↓ [encoding/consolidation]
Long-Term Memory (permanent storage, unlimited capacity)
```

**Applying to LLMs**:

| Human Memory | LLM Implementation | Storage | Duration | Purpose |
|--------------|-------------------|---------|----------|---------|
| **Working Memory** | `activeContext.md` | Single file | Current session | Active task state |
| **Short-Term Memory** | `task-logs/` directory | Multiple files | 30 days | Recent work history |
| **Long-Term Memory** | `core/` directory | 6 core files | Permanent | Project knowledge |

### 1.2 Memory Layer Specifications

#### Layer 1: Working Memory (activeContext.md)

**Purpose**: Current session state—what the LLM is actively working on RIGHT NOW.

**Capacity**: Limited to ~2,000 tokens (1-2 pages)

**Update Frequency**: Real-time (multiple times per session)

**Characteristics**:
- ✅ Highly volatile (changes constantly)
- ✅ Immediately accessible
- ✅ Contains only current context
- ✅ Compressed representation of current work

**Structure**:
```yaml
---
type: "working-memory"
version: "1.0.0"
session-id: "550e8400-e29b-41d4-a716-446655440000"
created: "2025-12-27T10:00:00Z"
modified: "2025-12-27T10:45:00Z"
status: "active"
---

# Active Context

## Current Focus
[What I'm working on RIGHT NOW - single sentence]

## Session State
- **Started**: 2025-12-27 10:00
- **Current Task**: Implementing user authentication
- **Files Modified**: 
  - `src/auth/login.py` (in progress)
  - `tests/test_auth.py` (pending)

## Recent Decisions (This Session)
| Time | Decision | Rationale |
|------|----------|-----------|
| 10:15 | Use JWT tokens | Stateless auth for microservices |
| 10:30 | PKCE extension | Mobile app security |

## Blocking Issues
- [ ] Need clarification on token expiry policy
- [ ] OAuth provider credentials pending

## Next Actions
1. Complete login endpoint implementation
2. Write unit tests for JWT generation
3. Update API documentation

## Session Notes
[Running notes from current session - stream of consciousness]
- Implemented JWT generation with 15min expiry
- Discovered edge case: simultaneous logins from different devices
- TODO: Research token revocation strategies
```

**Key Principles**:
- **Single Source of Truth** for current session
- **Updated frequently** (after every significant action)
- **Compressed format** (bullets, tables, not prose)
- **Action-oriented** (what's happening, what's next)

#### Layer 2: Short-Term Memory (task-logs/)

**Purpose**: Recent work history—tasks completed in the last 30 days.

**Capacity**: Unlimited individual files, but archived after 30 days

**Update Frequency**: Once per task completion

**Characteristics**:
- ✅ Persistent across sessions
- ✅ Searchable by date/topic
- ✅ Contains detailed implementation notes
- ✅ Includes performance evaluations

**Directory Structure**:
```
task-logs/
├── 2025-12-27-1000-implement-jwt-auth.md
├── 2025-12-27-1430-add-rate-limiting.md
├── 2025-12-26-0900-database-migration.md
└── 2025-12-25-1530-fix-login-bug.md
```

**Task Log Template**:
```yaml
---
type: "task-log"
task-id: "TASK-2025-12-27-001"
created: "2025-12-27T10:00:00Z"
completed: "2025-12-27T14:30:00Z"
status: "completed"
tags: ["authentication", "security", "backend"]
related-files:
  - "src/auth/login.py"
  - "tests/test_auth.py"
performance-score: 20
---

# Task Log: Implement JWT Authentication

## Task Information
- **Date**: 2025-12-27
- **Duration**: 4.5 hours
- **Triggered By**: Feature request FR-123
- **Related Memory**: [[systemPatterns#authentication]]

## Goal
Implement JWT-based authentication for API endpoints with PKCE extension for mobile security.

**Acceptance Criteria**:
- [ ] JWT generation with configurable expiry
- [ ] Token validation middleware
- [ ] Refresh token mechanism
- [ ] PKCE flow for mobile clients
- [ ] Unit test coverage ≥ 80%

## Implementation Details

### Approach
Chose JWT over session-based auth because:
1. **Stateless**: Scales horizontally without session store
2. **Microservices**: Works across service boundaries
3. **Mobile-friendly**: Tokens stored locally, no cookies

### Execution

**Step 1: JWT Generation**
```python
# src/auth/jwt_handler.py
import jwt
from datetime import datetime, timedelta
from typing import Dict

class JWTHandler:
    def __init__(self, secret_key: str, expiry_minutes: int = 15):
        self.secret_key = secret_key
        self.expiry_minutes = expiry_minutes
    
    def generate_token(self, user_id: str, claims: Dict = None) -> str:
        """Generate JWT access token."""
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(minutes=self.expiry_minutes),
            'iat': datetime.utcnow(),
            **(claims or {})
        }
        
        return jwt.encode(payload, self.secret_key, algorithm='HS256')
    
    def verify_token(self, token: str) -> Dict:
        """Verify and decode JWT token."""
        try:
            return jwt.decode(token, self.secret_key, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationError("Token expired")
        except jwt.InvalidTokenError:
            raise AuthenticationError("Invalid token")
```

**Step 2: Authentication Middleware**
```python
# src/middleware/auth.py
from functools import wraps
from flask import request, jsonify

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        
        if not token:
            return jsonify({'error': 'No token provided'}), 401
        
        try:
            user = jwt_handler.verify_token(token)
            request.user = user
            return f(*args, **kwargs)
        except AuthenticationError as e:
            return jsonify({'error': str(e)}), 401
    
    return decorated
```

**Step 3: PKCE Implementation**
```python
# src/auth/pkce.py
import hashlib
import base64
import secrets

def generate_code_verifier(length: int = 128) -> str:
    """Generate PKCE code verifier."""
    return base64.urlsafe_b64encode(
        secrets.token_bytes(length)
    ).decode('utf-8').rstrip('=')

def generate_code_challenge(verifier: str) -> str:
    """Generate PKCE code challenge from verifier."""
    digest = hashlib.sha256(verifier.encode('utf-8')).digest()
    return base64.urlsafe_b64encode(digest).decode('utf-8').rstrip('=')
```

### Challenges Encountered

**Challenge 1: Token Expiry Too Short**
- **Problem**: 5-minute expiry caused frequent re-authentication
- **Solution**: Increased to 15 minutes + implemented refresh tokens
- **Learning**: Balance security vs UX

**Challenge 2: Simultaneous Logins**
- **Problem**: Multiple devices should be allowed
- **Solution**: Don't invalidate previous tokens, track device IDs
- **Decision**: Add device fingerprinting in future iteration

### Decisions Made

| Decision | Alternatives Considered | Rationale |
|----------|------------------------|-----------|
| JWT over sessions | Session-based auth, OAuth2 | Stateless, scales better |
| HS256 algorithm | RS256 (asymmetric) | Simpler for single service, will migrate to RS256 when multi-service |
| 15min access tokens | 1hr, 24hr | Security vs usability balance |
| Separate refresh tokens | Long-lived access tokens | Can revoke without affecting active sessions |

## Testing & Validation

**Test Coverage**: 85% (17/20 test cases passing)

```python
# tests/test_jwt_handler.py
def test_generate_token():
    handler = JWTHandler(secret_key="test_secret")
    token = handler.generate_token("user123")
    
    assert token is not None
    assert isinstance(token, str)

def test_verify_valid_token():
    handler = JWTHandler(secret_key="test_secret")
    token = handler.generate_token("user123")
    
    payload = handler.verify_token(token)
    assert payload['user_id'] == "user123"

def test_verify_expired_token():
    handler = JWTHandler(secret_key="test_secret", expiry_minutes=0)
    token = handler.generate_token("user123")
    time.sleep(1)
    
    with pytest.raises(AuthenticationError, match="Token expired"):
        handler.verify_token(token)
```

## Performance Evaluation

### Score: 20/23

**Rewards Earned** (+13):
- +3: Comprehensive implementation (all acceptance criteria met)
- +2: Excellent test coverage (85%)
- +2: Security best practices (PKCE, short-lived tokens)
- +2: Clean code structure (separated concerns)
- +2: Good documentation (docstrings, comments)
- +2: Error handling (custom exceptions, meaningful messages)

**Penalties Incurred** (-3):
- -2: Incomplete refresh token mechanism (deferred to next task)
- -1: Missing token revocation strategy

**Threshold**: 18/23 ✓ **PASS**

### Self-Assessment
- **Strengths**: Clean implementation, good security practices, comprehensive tests
- **Improvements**: Should have completed refresh token mechanism in same session
- **Learnings**: PKCE adds significant security for mobile apps with minimal overhead

## Memory Updates Required
- [x] Update [[systemPatterns#authentication]] with JWT pattern
- [x] Update [[techContext]] with new dependencies (PyJWT)
- [x] Update [[progress]] - Auth milestone 80% complete
- [x] Update [[activeContext]] with next task

## Next Steps
1. **Immediate**: Implement refresh token rotation
2. **Soon**: Add token revocation mechanism
3. **Future**: Migrate to RS256 when multiple services

---

**Reflection Note for Future Self**:
The JWT implementation is solid but refresh tokens need completion before shipping to production. The PKCE flow was straightforward - mobile team will appreciate the security. Consider implementing a token blacklist for logout functionality.
```

**Key Principles**:
- **Complete documentation** (reproducible by another engineer)
- **Performance scoring** (quantified quality metrics)
- **Self-assessment** (meta-cognitive reflection)
- **Forward-looking** (next steps documented)

#### Layer 3: Long-Term Memory (core/)

**Purpose**: Permanent project knowledge—the foundation that persists across all sessions.

**Capacity**: 6 core files, each maintained indefinitely

**Update Frequency**: As needed (when major decisions/changes occur)

**Characteristics**:
- ✅ Most stable layer (changes infrequently)
- ✅ Authoritative project knowledge
- ✅ Referenced by all other layers
- ✅ Version controlled

**Core Files Structure**:
```
core/
├── projectbrief.md         # Strategic context: vision, objectives, constraints
├── productContext.md       # Requirements: user needs, features, success criteria
├── systemPatterns.md       # Architecture: design decisions, patterns, trade-offs
├── techContext.md          # Technology: stack, dependencies, setup
├── activeContext.md        # Working memory: current session state
└── progress.md             # Implementation: roadmap, milestones, status
```

**Example: systemPatterns.md**

```yaml
---
type: "core-memory"
version: "2.1.0"
created: "2025-11-01T00:00:00Z"
modified: "2025-12-27T14:30:00Z"
status: "active"
changelog:
  - "2.1.0": "Added JWT authentication pattern"
  - "2.0.0": "Migrated to microservices architecture"
  - "1.0.0": "Initial patterns documented"
---

# System Patterns

## Architectural Decisions

### 1. Microservices Architecture

**Context**: Monolithic application reaching scaling limits

**Decision**: Decompose into domain-driven microservices

**Rationale**:
- **Scalability**: Independent scaling of services
- **Team autonomy**: Separate teams own separate services
- **Technology diversity**: Best tool for each service
- **Fault isolation**: Service failures don't cascade

**Trade-offs Accepted**:
- ❌ Increased operational complexity
- ❌ Distributed system challenges (eventual consistency)
- ❌ Network latency between services
- ✅ Benefits outweigh costs for our scale (10M+ users)

**Implementation**:
```
Services:
├── auth-service      # Authentication, authorization
├── user-service      # User profiles, preferences
├── order-service     # Order processing
├── payment-service   # Payment integration
└── notification-service  # Email, SMS, push
```

**Communication**: gRPC for service-to-service, REST for client-facing APIs

### 2. Authentication Pattern: JWT with PKCE

**Context**: Need stateless authentication for microservices + mobile apps

**Decision**: JWT access tokens (15min) + refresh tokens (7 days) + PKCE for mobile

**Rationale**:
- **Stateless**: No session store, scales horizontally
- **Microservices-friendly**: Tokens work across services
- **Security**: PKCE prevents authorization code interception
- **UX**: 15min expiry with seamless refresh

**Alternatives Considered**:
1. **Session-based auth**: ❌ Requires shared session store
2. **OAuth2 without PKCE**: ❌ Vulnerable to mobile attacks
3. **Long-lived tokens**: ❌ Security risk if compromised

**Implementation Details**:
```python
# JWT Claims Structure
{
  "user_id": "abc123",
  "roles": ["user", "admin"],
  "device_id": "device123",
  "exp": 1640995200,
  "iat": 1640994300
}

# Refresh Token Storage
# Stored in Redis with 7-day TTL, indexed by user_id + device_id
```

**Security Measures**:
- ✅ Tokens signed with HS256 (RS256 planned for multi-service)
- ✅ Short access token lifetime (15min)
- ✅ Refresh token rotation on use
- ✅ Device fingerprinting
- ✅ Token revocation list (blacklist) for logout

**Performance Impact**: Negligible (<5ms per validation)

### 3. Database per Service Pattern

**Context**: Microservices need data autonomy

**Decision**: Each service owns its database, no direct DB access across services

**Rationale**:
- **Loose coupling**: Services can evolve independently
- **Technology fit**: Use optimal DB for each use case
- **Scalability**: Independent DB scaling

**Challenges**:
- **Data consistency**: Eventual consistency via event sourcing
- **Joins**: Implement at application level or use API composition
- **Transactions**: Saga pattern for distributed transactions

**Database Choices**:
```
auth-service:      PostgreSQL (relational, ACID)
user-service:      PostgreSQL (relational)
order-service:     PostgreSQL (relational, transactions)
payment-service:   PostgreSQL (ACID critical)
notification-service: MongoDB (flexible schema)
```

## Design Patterns

### 1. Repository Pattern

**Used In**: All services for data access

**Benefits**:
- ✅ Abstraction over data layer
- ✅ Testability (mock repositories)
- ✅ Consistency across services

**Example**:
```python
class UserRepository:
    def get_by_id(self, user_id: str) -> User: pass
    def save(self, user: User) -> None: pass
    def delete(self, user_id: str) -> None: pass
```

### 2. Circuit Breaker Pattern

**Used In**: All inter-service communication

**Benefits**:
- ✅ Fault tolerance
- ✅ Prevents cascading failures
- ✅ Graceful degradation

**Implementation**: Using `pybreaker` library

**Configuration**:
```python
breaker = CircuitBreaker(
    fail_max=5,        # Open after 5 failures
    timeout_duration=60 # Stay open for 60s
)
```

### 3. Event Sourcing

**Used In**: Order and payment services

**Benefits**:
- ✅ Complete audit trail
- ✅ Replay events for debugging
- ✅ Temporal queries (state at any point in time)

**Trade-offs**:
- ❌ Increased complexity
- ❌ Storage overhead
- ✅ Worth it for financial transactions

## Conventions

### API Design
- **REST** for client-facing APIs (HTTP/JSON)
- **gRPC** for service-to-service (Protocol Buffers)
- **Versioning**: URL-based (`/api/v1/users`)

### Error Handling
- **Structured errors**: JSON with `error` object
- **HTTP status codes**: Semantic (400, 401, 404, 500)
- **Error tracking**: Sentry for production errors

### Logging
- **Structured logging**: JSON format
- **Correlation IDs**: Track requests across services
- **Levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL

## Testing Strategy

### Unit Tests
- **Coverage**: ≥ 80%
- **Framework**: pytest
- **Mocking**: unittest.mock

### Integration Tests
- **API tests**: Test complete API flows
- **DB tests**: Test with real database (Docker)
- **Contract tests**: Pact for service contracts

### E2E Tests
- **Critical flows**: Authentication, checkout, payment
- **Framework**: Selenium for web, Appium for mobile
```

**Key Principles**:
- **Living document** (updated with each architectural decision)
- **Rationale-inclusive** (always explain "why")
- **Alternatives documented** (what was considered and rejected)
- **Pattern catalog** (reusable solutions)

### 1.3 Memory Flow & Consolidation

**How information flows through the three layers**:

```
Session Start
    ↓
Load Long-Term Memory (core/)
    ↓
Load Recent Short-Term Memory (task-logs/ from last 7 days)
    ↓
Initialize Working Memory (activeContext.md)
    ↓
[Work happens - activeContext.md updated frequently]
    ↓
Task Completion
    ↓
Create Task Log (Short-Term Memory)
    ↓
Extract Patterns → Update systemPatterns.md (Long-Term)
    ↓
Update activeContext.md for next session
    ↓
Session End
    ↓
Consolidate: Task logs → Summary → Archive after 30 days
```

**Consolidation Rules**:

| Source | Trigger | Destination | Retention |
|--------|---------|-------------|-----------|
| activeContext.md | Task completion | task-logs/ | Create new log |
| task-logs/ | Every task | systemPatterns.md | Extract patterns |
| task-logs/ | 30 days old | archive/task-logs/YYYY-MM/ | Move to archive |
| errors/ | Error resolved + 7 days | archive/errors/ | Archive resolved |

**Memory Capacity Management**:

```python
# Pseudocode for memory limits
if len(task_logs) > 100:
    archive_oldest(days=30)

if len(activeContext) > 2000_tokens:
    compress_using_chain_of_density()

if systemPatterns_changed:
    increment_version()
    create_backup()
```

---

## 2. File-Based Persistent Storage

### 2.1 Directory Structure Design

**Complete memory bank structure**:

```
.claude/
├── core/                           # Long-term memory (6 files)
│   ├── projectbrief.md             # Vision, objectives, constraints
│   ├── productContext.md           # Requirements, features
│   ├── systemPatterns.md           # Architecture decisions
│   ├── techContext.md              # Tech stack, dependencies
│   ├── activeContext.md            # Current session state
│   └── progress.md                 # Implementation roadmap
│
├── task-logs/                      # Short-term memory
│   ├── 2025-12-27-1000-jwt-auth.md
│   ├── 2025-12-27-1430-rate-limit.md
│   └── ...
│
├── errors/                         # Error pattern storage
│   ├── 2025-12-26-auth-timeout.md
│   ├── 2025-12-25-db-connection.md
│   └── ...
│
├── plans/                          # Planning artifacts
│   ├── auth-implementation-plan.md
│   ├── payment-integration-plan.md
│   └── ...
│
├── archive/                        # Archived memories
│   ├── task-logs/
│   │   ├── 2025-11/
│   │   └── 2025-10/
│   └── errors/
│       ├── 2025-11/
│       └── 2025-10/
│
├── embeddings/                     # Semantic search data
│   └── embeddings.json
│
├── versions/                       # Version history
│   ├── systemPatterns/
│   │   ├── v2.0.0.md
│   │   └── v1.0.0.md
│   └── ...
│
└── memory-index.md                 # Master navigation & checksums
```

**Design Principles**:

1. **Hierarchical Organization**: Clear separation by memory layer
2. **Chronological Naming**: Easy to find recent work (YYYY-MM-DD-HHMM-description)
3. **Archival Strategy**: Old memories archived, not deleted (can be retrieved)
4. **Single Source of Truth**: One authoritative location per concept
5. **Searchable**: Both file names and content optimized for search

### 2.2 YAML Frontmatter Specification

**Every memory file MUST have frontmatter**:

```yaml
---
# REQUIRED FIELDS
type: "core-memory" | "task-log" | "error-record" | "plan" | "working-memory"
created: "YYYY-MM-DDTHH:MM:SSZ"
modified: "YYYY-MM-DDTHH:MM:SSZ"
status: "active" | "archived" | "deprecated"

# TYPE-SPECIFIC FIELDS
version: "X.Y.Z"          # For core-memory only
task-id: "TASK-XXX"       # For task-log only
session-id: "UUID"        # For working-memory only
error-type: "auth|db|..."  # For error-record only

# OPTIONAL METADATA
tags: ["tag1", "tag2"]
priority: "critical" | "high" | "medium" | "low"
related-files: ["file1.md", "file2.md"]
related-tasks: ["TASK-001", "TASK-002"]
performance-score: 20     # For task-log only (0-23)
---
```

**Validation Rules**:

```python
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Literal

@dataclass
class MemoryMetadata:
    """Memory file frontmatter structure."""
    
    # Required
    type: Literal["core-memory", "task-log", "error-record", "plan", "working-memory"]
    created: datetime
    modified: datetime
    status: Literal["active", "archived", "deprecated"]
    
    # Optional
    version: Optional[str] = None
    task_id: Optional[str] = None
    session_id: Optional[str] = None
    error_type: Optional[str] = None
    tags: List[str] = None
    priority: Optional[str] = None
    related_files: List[str] = None
    related_tasks: List[str] = None
    performance_score: Optional[int] = None
    
    def validate(self) -> bool:
        """Validate metadata consistency."""
        
        # Type-specific validation
        if self.type == "core-memory" and not self.version:
            raise ValueError("core-memory requires version")
        
        if self.type == "task-log" and not self.task_id:
            raise ValueError("task-log requires task_id")
        
        if self.type == "working-memory" and not self.session_id:
            raise ValueError("working-memory requires session_id")
        
        # Performance score range
        if self.performance_score and not (0 <= self.performance_score <= 23):
            raise ValueError("performance_score must be 0-23")
        
        return True
```

### 2.3 Wiki-Link Protocol

**Internal linking for knowledge graph construction**:

```markdown
# Example: systemPatterns.md

## Authentication Pattern

See [[techContext#jwt-library]] for implementation details.

This pattern builds on [[projectbrief#security-requirements]].

Related error: [[errors/2025-12-26-auth-timeout]]

Implementation in [[task-logs/2025-12-27-1000-jwt-auth]].
```

**Link Syntax**:
- `[[filename]]` - Link to file (auto-resolves .md extension)
- `[[filename#heading]]` - Link to specific section
- `[[directory/filename]]` - Link with path
- `[[filename|display text]]` - Link with custom display text

**Bidirectional Links**:

Every link creates an implicit backlink:

```
systemPatterns.md → [[techContext]]
                    ↓
techContext.md  ← Backlinked from systemPatterns.md
```

**Automatic Link Suggestion**:

```python
def suggest_links(content: str, all_files: List[str]) -> List[str]:
    """Suggest wiki-links for content."""
    
    suggestions = []
    
    # Extract potential concepts (capitalized phrases, technical terms)
    concepts = extract_concepts(content)
    
    for concept in concepts:
        # Find files that might be related
        for file in all_files:
            if concept.lower() in file.lower():
                suggestions.append({
                    'concept': concept,
                    'file': file,
                    'confidence': calculate_similarity(concept, file)
                })
    
    return sorted(suggestions, key=lambda x: x['confidence'], reverse=True)
```

### 2.4 Memory Index (memory-index.md)

**Master navigation file with checksums**:

```yaml
---
type: "index"
version: "1.0.0"
created: "2025-11-01T00:00:00Z"
modified: "2025-12-27T15:00:00Z"
---

# Memory Index

## Core Memory Files

| File | Purpose | Version | Last Modified | Checksum | Status |
|------|---------|---------|---------------|----------|--------|
| [[projectbrief]] | Strategic vision | 1.0.0 | 2025-11-01 | a3f5e8d2 | ✓ Valid |
| [[productContext]] | Requirements | 1.2.0 | 2025-12-15 | b7c9a1f3 | ✓ Valid |
| [[systemPatterns]] | Architecture | 2.1.0 | 2025-12-27 | c2d4e6f8 | ✓ Valid |
| [[techContext]] | Tech stack | 1.5.0 | 2025-12-20 | d8e1f2a4 | ✓ Valid |
| [[activeContext]] | Current state | - | 2025-12-27 | e9f3a5b7 | ✓ Valid |
| [[progress]] | Roadmap | 1.3.0 | 2025-12-25 | f4a8b9c1 | ✓ Valid |

## Recent Task Logs (Last 7 Days)

| Date | Task | Score | Status |
|------|------|-------|--------|
| 2025-12-27 | [[task-logs/2025-12-27-1000-jwt-auth]] | 20/23 | ✓ Complete |
| 2025-12-27 | [[task-logs/2025-12-27-1430-rate-limit]] | 21/23 | ✓ Complete |
| 2025-12-26 | [[task-logs/2025-12-26-0900-db-migration]] | 19/23 | ✓ Complete |

## Active Error Patterns

| Date | Error | Status | Resolution |
|------|-------|--------|------------|
| 2025-12-26 | [[errors/2025-12-26-auth-timeout]] | Resolved | Increased timeout to 30s |

## Active Plans

- [[plans/auth-implementation-plan]] - 80% complete
- [[plans/payment-integration-plan]] - 30% complete

## Archive Statistics

- **Task Logs Archived**: 47
- **Errors Archived**: 12
- **Oldest Active Log**: 2025-12-01

## Integrity Checks

Last verification: 2025-12-27T15:00:00Z

**Results**:
- ✓ All core files present
- ✓ All checksums valid
- ✓ No orphaned references
- ✓ Archival rules applied

## Quick Navigation

**By Topic**:
- Authentication: [[systemPatterns#authentication]], [[task-logs/2025-12-27-1000-jwt-auth]]
- Database: [[systemPatterns#database-per-service]], [[techContext#postgresql]]
- Testing: [[systemPatterns#testing-strategy]]

**By Status**:
- Active Tasks: 2
- Blocked Tasks: 0
- Archived Tasks: 47
```

### 2.5 File Naming Conventions

**Standardized naming ensures chronological navigation**:

```python
from datetime import datetime
from typing import Literal

def generate_task_log_filename(
    description: str,
    timestamp: datetime = None
) -> str:
    """Generate standardized task log filename."""
    
    if timestamp is None:
        timestamp = datetime.now()
    
    # Format: YYYY-MM-DD-HHMM-description.md
    date_str = timestamp.strftime("%Y-%m-%d-%H%M")
    
    # Sanitize description (lowercase, replace spaces with hyphens)
    desc_clean = description.lower().replace(' ', '-')
    desc_clean = ''.join(c for c in desc_clean if c.isalnum() or c == '-')
    
    return f"{date_str}-{desc_clean}.md"

def generate_error_filename(
    error_type: str,
    timestamp: datetime = None
) -> str:
    """Generate standardized error filename."""
    
    if timestamp is None:
        timestamp = datetime.now()
    
    date_str = timestamp.strftime("%Y-%m-%d-%H%M")
    error_clean = error_type.lower().replace(' ', '-')
    
    return f"{date_str}-{error_clean}.md"

# Examples:
# generate_task_log_filename("Implement JWT Auth")
# → "2025-12-27-1000-implement-jwt-auth.md"

# generate_error_filename("Database Connection Timeout")
# → "2025-12-26-1530-database-connection-timeout.md"
```

**Benefits**:
- ✅ Chronological sorting (ls -l shows in order)
- ✅ Unique filenames (timestamp prevents collisions)
- ✅ Human-readable (description visible in filename)
- ✅ Searchable (grep by date or description)

---

## 3. Event-Driven Memory Management

**This is the heart of the advanced memory system**: Automatic memory operations triggered by workflow events.

### 3.1 Event Handler Architecture

**Event-driven workflow**:

```python
from enum import Enum
from typing import Callable, Dict, List
from dataclasses import dataclass
from datetime import datetime

class MemoryEvent(Enum):
    """Memory system events."""
    SESSION_START = "session_start"
    TASK_START = "task_start"
    ERROR_DETECTED = "error_detected"
    TASK_COMPLETE = "task_complete"
    SESSION_END = "session_end"

@dataclass
class EventContext:
    """Context passed to event handlers."""
    event: MemoryEvent
    timestamp: datetime
    data: Dict
    session_id: str

class MemoryEventManager:
    """Manages event-driven memory operations."""
    
    def __init__(self, memory_path: str):
        self.memory_path = Path(memory_path)
        self.handlers: Dict[MemoryEvent, List[Callable]] = {
            event: [] for event in MemoryEvent
        }
    
    def register_handler(
        self,
        event: MemoryEvent,
        handler: Callable[[EventContext], None]
    ):
        """Register event handler."""
        self.handlers[event].append(handler)
    
    def trigger(self, event: MemoryEvent, data: Dict = None):
        """Trigger event and execute all registered handlers."""
        
        context = EventContext(
            event=event,
            timestamp=datetime.now(),
            data=data or {},
            session_id=str(uuid.uuid4())
        )
        
        print(f"[{context.timestamp}] Event: {event.value}")
        
        for handler in self.handlers[event]:
            try:
                handler(context)
            except Exception as e:
                print(f"Handler error: {e}")
                # Don't let handler failures stop other handlers
                continue
```

### 3.2 SessionStart Handler

**Loads all memory layers and verifies integrity**:

```python
def on_session_start(context: EventContext):
    """
    Execute on session start.
    
    Responsibilities:
    1. Load .clinerules (workflow rules)
    2. Verify memory integrity (checksums)
    3. Load activeContext.md
    4. Check memory-index.md for recent activity
    5. Initialize session context
    6. Log session start
    """
    
    memory_path = Path(".claude")
    
    # Step 1: Load .clinerules
    rules_file = Path(".clinerules")
    if rules_file.exists():
        rules = rules_file.read_text()
        print(f"✓ Loaded workflow rules ({len(rules)} chars)")
    else:
        print("⚠ No .clinerules found - creating default")
        create_default_rules(rules_file)
    
    # Step 2: Verify memory integrity
    index_file = memory_path / "memory-index.md"
    if index_file.exists():
        integrity_ok = verify_memory_integrity(index_file)
        if integrity_ok:
            print("✓ Memory integrity verified")
        else:
            print("✗ Memory corruption detected - initiating recovery")
            recover_memory(memory_path)
    
    # Step 3: Load activeContext.md
    active_context = memory_path / "core" / "activeContext.md"
    if active_context.exists():
        context_data = parse_memory_file(active_context)
        print(f"✓ Loaded active context: {context_data['metadata']['modified']}")
        
        # Extract current focus
        current_focus = extract_current_focus(context_data['content'])
        print(f"  Current focus: {current_focus}")
    else:
        print("⚠ No active context - starting fresh session")
        create_initial_active_context(active_context, context.session_id)
    
    # Step 4: Load recent task logs (last 7 days)
    task_logs = load_recent_task_logs(memory_path / "task-logs", days=7)
    print(f"✓ Loaded {len(task_logs)} recent task logs")
    
    # Step 5: Initialize session context
    session_data = {
        'session_id': context.session_id,
        'start_time': context.timestamp,
        'active_context': context_data if active_context.exists() else None,
        'recent_tasks': task_logs,
        'rules': rules if rules_file.exists() else None
    }
    
    # Step 6: Log session start
    log_session_event(memory_path, "SESSION_START", session_data)
    
    print(f"\n{'='*60}")
    print(f"Session initialized: {context.session_id}")
    print(f"Started: {context.timestamp}")
    print(f"Memory path: {memory_path}")
    print(f"{'='*60}\n")
    
    return session_data


def verify_memory_integrity(index_file: Path) -> bool:
    """Verify all memory files match their checksums."""
    
    index_data = parse_memory_file(index_file)
    
    # Extract checksum table from index
    checksums = extract_checksums_from_index(index_data['content'])
    
    all_valid = True
    
    for file_info in checksums:
        file_path = index_file.parent / file_info['file']
        
        if not file_path.exists():
            print(f"✗ Missing file: {file_info['file']}")
            all_valid = False
            continue
        
        # Calculate current checksum
        current_checksum = calculate_checksum(file_path)
        expected_checksum = file_info['checksum']
        
        if current_checksum != expected_checksum:
            print(f"✗ Checksum mismatch: {file_info['file']}")
            print(f"  Expected: {expected_checksum}")
            print(f"  Got: {current_checksum}")
            all_valid = False
        else:
            print(f"✓ {file_info['file']}: {current_checksum}")
    
    return all_valid


def load_recent_task_logs(task_logs_dir: Path, days: int = 7) -> List[Dict]:
    """Load task logs from last N days."""
    
    if not task_logs_dir.exists():
        return []
    
    cutoff_date = datetime.now() - timedelta(days=days)
    
    recent_logs = []
    
    for log_file in sorted(task_logs_dir.glob("*.md"), reverse=True):
        # Extract date from filename (YYYY-MM-DD-HHMM-description.md)
        try:
            date_str = log_file.stem[:16]  # "2025-12-27-1000"
            log_date = datetime.strptime(date_str, "%Y-%m-%d-%H%M")
            
            if log_date >= cutoff_date:
                log_data = parse_memory_file(log_file)
                recent_logs.append({
                    'file': log_file.name,
                    'date': log_date,
                    'metadata': log_data['metadata'],
                    'summary': extract_summary(log_data['content'])
                })
        except (ValueError, IndexError):
            continue
    
    return recent_logs
```

### 3.3 TaskStart Handler

**Documents objectives and creates implementation plan**:

```python
def on_task_start(context: EventContext):
    """
    Execute on task start.
    
    Responsibilities:
    1. Document task objectives
    2. Create implementation plan
    3. Load relevant context from memory
    4. Identify required memory updates
    5. Create task log entry
    """
    
    memory_path = Path(".claude")
    task_description = context.data.get('description', 'Unnamed task')
    
    # Step 1: Document objectives
    objectives = {
        'description': task_description,
        'acceptance_criteria': context.data.get('acceptance_criteria', []),
        'dependencies': context.data.get('dependencies', []),
        'estimated_duration': context.data.get('estimated_duration', 'Unknown')
    }
    
    print(f"\n{'='*60}")
    print(f"TASK START: {task_description}")
    print(f"{'='*60}")
    print(f"Acceptance Criteria:")
    for i, criterion in enumerate(objectives['acceptance_criteria'], 1):
        print(f"  {i}. {criterion}")
    print()
    
    # Step 2: Create implementation plan
    plan = create_implementation_plan(
        description=task_description,
        objectives=objectives,
        context_data=context.data
    )
    
    # Save plan to plans/ directory
    plan_file = memory_path / "plans" / f"{generate_task_id()}-plan.md"
    save_memory_file(plan_file, plan)
    print(f"✓ Implementation plan created: {plan_file.name}")
    
    # Step 3: Load relevant context
    relevant_context = retrieve_relevant_context(
        query=task_description,
        memory_path=memory_path
    )
    
    print(f"\n✓ Loaded {len(relevant_context)} relevant memory files:")
    for file_ref in relevant_context:
        print(f"  - {file_ref['file']}: {file_ref['relevance']}")
    
    # Step 4: Identify required memory updates
    memory_updates_needed = identify_memory_updates(
        task_description=task_description,
        objectives=objectives
    )
    
    print(f"\n✓ Identified {len(memory_updates_needed)} memory updates needed:")
    for update in memory_updates_needed:
        print(f"  - {update['file']}: {update['reason']}")
    
    # Step 5: Create initial task log entry
    task_id = generate_task_id()
    task_log_file = memory_path / "task-logs" / generate_task_log_filename(task_description)
    
    initial_log = create_initial_task_log(
        task_id=task_id,
        description=task_description,
        objectives=objectives,
        relevant_context=relevant_context,
        memory_updates_needed=memory_updates_needed
    )
    
    save_memory_file(task_log_file, initial_log)
    print(f"\n✓ Task log created: {task_log_file.name}")
    
    # Step 6: Update activeContext.md
    update_active_context_for_task_start(
        memory_path=memory_path,
        task_id=task_id,
        description=task_description
    )
    
    print(f"✓ Active context updated")
    print(f"\nTask ID: {task_id}")
    print(f"{'='*60}\n")
    
    return {
        'task_id': task_id,
        'task_log': task_log_file,
        'plan': plan_file,
        'relevant_context': relevant_context
    }


def create_implementation_plan(
    description: str,
    objectives: Dict,
    context_data: Dict
) -> Dict:
    """Create structured implementation plan."""
    
    plan = {
        'metadata': {
            'type': 'plan',
            'created': datetime.now().isoformat(),
            'modified': datetime.now().isoformat(),
            'status': 'active',
            'task_description': description
        },
        'content': f"""# Implementation Plan: {description}

## Objectives

{chr(10).join(f'- {criterion}' for criterion in objectives['acceptance_criteria'])}

## Approach

### Phase 1: Preparation
1. Review relevant documentation
2. Identify dependencies
3. Set up test environment

### Phase 2: Implementation
1. Write failing tests (TDD)
2. Implement core functionality
3. Refactor for quality

### Phase 3: Validation
1. Run test suite
2. Performance testing
3. Code review

## Dependencies

{chr(10).join(f'- {dep}' for dep in objectives['dependencies'])}

## Estimated Duration

{objectives['estimated_duration']}

## Success Criteria

- [ ] All acceptance criteria met
- [ ] Test coverage ≥ 80%
- [ ] Performance within targets
- [ ] Documentation updated
"""
    }
    
    return plan


def retrieve_relevant_context(query: str, memory_path: Path) -> List[Dict]:
    """Retrieve relevant memory files for task."""
    
    # Simple keyword-based relevance for now
    # In production, use semantic search (covered in Doc 18)
    
    relevant = []
    
    # Search core files
    core_dir = memory_path / "core"
    for core_file in core_dir.glob("*.md"):
        content = core_file.read_text()
        
        # Calculate relevance score (simple keyword matching)
        relevance_score = calculate_keyword_relevance(query, content)
        
        if relevance_score > 0.3:  # Threshold
            relevant.append({
                'file': f"core/{core_file.name}",
                'relevance': f"{relevance_score:.2f}",
                'type': 'core-memory'
            })
    
    # Search recent task logs
    task_logs_dir = memory_path / "task-logs"
    if task_logs_dir.exists():
        for log_file in sorted(task_logs_dir.glob("*.md"), reverse=True)[:10]:
            content = log_file.read_text()
            relevance_score = calculate_keyword_relevance(query, content)
            
            if relevance_score > 0.3:
                relevant.append({
                    'file': f"task-logs/{log_file.name}",
                    'relevance': f"{relevance_score:.2f}",
                    'type': 'task-log'
                })
    
    return sorted(relevant, key=lambda x: float(x['relevance']), reverse=True)[:5]
```

### 3.4 ErrorDetected Handler

**Documents errors and applies recovery strategies**:

```python
def on_error_detected(context: EventContext):
    """
    Execute when error is detected.
    
    Responsibilities:
    1. Document error details
    2. Search memory for similar errors
    3. Apply known recovery strategy (if exists)
    4. Update error patterns
    5. Log resolution
    """
    
    memory_path = Path(".claude")
    error_info = context.data
    
    error_type = error_info.get('type', 'unknown')
    error_message = error_info.get('message', 'No message provided')
    stack_trace = error_info.get('stack_trace', '')
    
    print(f"\n{'='*60}")
    print(f"ERROR DETECTED: {error_type}")
    print(f"{'='*60}")
    print(f"Message: {error_message}")
    if stack_trace:
        print(f"\nStack Trace:")
        print(stack_trace[:500])  # First 500 chars
    print(f"{'='*60}\n")
    
    # Step 1: Document error
    error_file = memory_path / "errors" / generate_error_filename(error_type)
    
    error_doc = create_error_document(
        error_type=error_type,
        error_message=error_message,
        stack_trace=stack_trace,
        context=error_info.get('context', {})
    )
    
    save_memory_file(error_file, error_doc)
    print(f"✓ Error documented: {error_file.name}")
    
    # Step 2: Search for similar errors
    similar_errors = search_similar_errors(
        memory_path=memory_path,
        error_type=error_type,
        error_message=error_message
    )
    
    if similar_errors:
        print(f"\n✓ Found {len(similar_errors)} similar errors:")
        for similar in similar_errors:
            print(f"  - {similar['file']}: {similar['resolution_status']}")
    else:
        print("\n⚠ No similar errors found - this is a new error pattern")
    
    # Step 3: Apply recovery strategy
    recovery_strategy = None
    
    if similar_errors:
        # Use resolution from most recent similar error
        most_recent = similar_errors[0]
        if most_recent['resolution_status'] == 'resolved':
            recovery_strategy = most_recent['resolution']
            print(f"\n✓ Applying known recovery strategy:")
            print(f"  {recovery_strategy}")
            
            # Attempt automatic recovery
            recovery_success = apply_recovery_strategy(recovery_strategy, error_info)
            
            if recovery_success:
                print(f"✓ Automatic recovery successful")
                update_error_document(error_file, resolution=recovery_strategy, status='auto-resolved')
            else:
                print(f"✗ Automatic recovery failed - manual intervention needed")
                update_error_document(error_file, resolution=recovery_strategy, status='recovery-failed')
    else:
        print("\n⚠ No known recovery strategy - manual resolution required")
    
    # Step 4: Update error patterns
    update_error_patterns(
        memory_path=memory_path,
        error_type=error_type,
        error_file=error_file,
        recovery_strategy=recovery_strategy
    )
    
    # Step 5: Update activeContext with error state
    update_active_context_with_error(
        memory_path=memory_path,
        error_type=error_type,
        error_file=error_file
    )
    
    print(f"\n{'='*60}")
    print(f"Error handling complete")
    print(f"{'='*60}\n")
    
    return {
        'error_file': error_file,
        'similar_errors': similar_errors,
        'recovery_strategy': recovery_strategy,
        'auto_resolved': recovery_success if recovery_strategy else False
    }


def search_similar_errors(
    memory_path: Path,
    error_type: str,
    error_message: str
) -> List[Dict]:
    """Search for similar errors in error history."""
    
    errors_dir = memory_path / "errors"
    if not errors_dir.exists():
        return []
    
    similar = []
    
    for error_file in errors_dir.glob("*.md"):
        error_data = parse_memory_file(error_file)
        
        # Check if same error type
        if error_data['metadata'].get('error_type') == error_type:
            # Calculate message similarity
            similarity = calculate_string_similarity(
                error_message,
                extract_error_message(error_data['content'])
            )
            
            if similarity > 0.7:  # 70% similar
                similar.append({
                    'file': error_file.name,
                    'similarity': similarity,
                    'resolution_status': error_data['metadata'].get('status', 'unknown'),
                    'resolution': extract_resolution(error_data['content'])
                })
    
    return sorted(similar, key=lambda x: x['similarity'], reverse=True)


def apply_recovery_strategy(strategy: str, error_info: Dict) -> bool:
    """Attempt to apply automatic recovery strategy."""
    
    # This would contain actual recovery logic
    # For now, just simulation
    
    if "restart service" in strategy.lower():
        # Simulate service restart
        print("  → Restarting service...")
        return True
    
    if "increase timeout" in strategy.lower():
        # Simulate timeout increase
        print("  → Increasing timeout...")
        return True
    
    if "clear cache" in strategy.lower():
        # Simulate cache clear
        print("  → Clearing cache...")
        return True
    
    # Unknown strategy - can't auto-recover
    return False
```

### 3.5 TaskComplete Handler

**Evaluates performance and updates all memory layers**:

```python
def on_task_complete(context: EventContext):
    """
    Execute on task completion.
    
    Responsibilities:
    1. Evaluate performance (0-23 score)
    2. Update task log with outcomes
    3. Update all affected memory layers
    4. Extract patterns for systemPatterns.md
    5. Update activeContext.md with next steps
    6. Archive plan (if applicable)
    """
    
    memory_path = Path(".claude")
    task_id = context.data.get('task_id')
    task_description = context.data.get('description')
    
    print(f"\n{'='*60}")
    print(f"TASK COMPLETE: {task_description}")
    print(f"{'='*60}\n")
    
    # Step 1: Evaluate performance
    performance_evaluation = evaluate_task_performance(
        task_data=context.data,
        memory_path=memory_path
    )
    
    score = performance_evaluation['score']
    rewards = performance_evaluation['rewards']
    penalties = performance_evaluation['penalties']
    
    print(f"Performance Score: {score}/23")
    print(f"\nRewards (+{sum(r['points'] for r in rewards)}):")
    for reward in rewards:
        print(f"  +{reward['points']}: {reward['reason']}")
    
    if penalties:
        print(f"\nPenalties (-{sum(p['points'] for p in penalties)}):")
        for penalty in penalties:
            print(f"  -{penalty['points']}: {penalty['reason']}")
    
    # Check threshold
    threshold = 18
    if score >= threshold:
        print(f"\n✓ PASS (>= {threshold}/23)")
    else:
        print(f"\n✗ FAIL (< {threshold}/23)")
        print("⚠ Task does not meet quality standards - review required")
    
    # Step 2: Update task log
    task_log_file = find_task_log(memory_path, task_id)
    
    if task_log_file:
        update_task_log_with_completion(
            task_log_file=task_log_file,
            performance=performance_evaluation,
            completion_data=context.data
        )
        print(f"\n✓ Task log updated: {task_log_file.name}")
    
    # Step 3: Extract patterns
    patterns_extracted = extract_patterns_from_task(
        task_data=context.data,
        task_log_file=task_log_file
    )
    
    if patterns_extracted:
        print(f"\n✓ Extracted {len(patterns_extracted)} new patterns:")
        for pattern in patterns_extracted:
            print(f"  - {pattern['name']}: {pattern['description']}")
        
        # Update systemPatterns.md
        update_system_patterns(
            memory_path=memory_path,
            new_patterns=patterns_extracted
        )
        print(f"✓ systemPatterns.md updated")
    
    # Step 4: Update other affected memory layers
    memory_updates = context.data.get('memory_updates', [])
    
    for update in memory_updates:
        target_file = memory_path / update['file']
        
        if target_file.exists():
            apply_memory_update(target_file, update['changes'])
            print(f"✓ Updated: {update['file']}")
    
    # Step 5: Update activeContext.md
    update_active_context_for_task_complete(
        memory_path=memory_path,
        task_id=task_id,
        score=score,
        next_steps=context.data.get('next_steps', [])
    )
    print(f"✓ Active context updated with next steps")
    
    # Step 6: Archive plan
    plan_file = find_plan_for_task(memory_path, task_id)
    if plan_file:
        archive_plan(plan_file, memory_path)
        print(f"✓ Implementation plan archived")
    
    # Step 7: Update progress.md if milestone affected
    if context.data.get('milestone_affected'):
        update_progress_milestone(
            memory_path=memory_path,
            milestone=context.data['milestone_affected'],
            status='completed'
        )
        print(f"✓ Progress milestone updated")
    
    print(f"\n{'='*60}")
    print(f"Task completion processing finished")
    print(f"{'='*60}\n")
    
    return {
        'score': score,
        'pass': score >= threshold,
        'patterns_extracted': patterns_extracted,
        'memory_updates_applied': len(memory_updates)
    }


def evaluate_task_performance(task_data: Dict, memory_path: Path) -> Dict:
    """
    Evaluate task performance using 0-23 scoring system.
    
    Base: 10 points
    Rewards: up to +13 points
    Penalties: up to -10 points
    """
    
    base_score = 10
    rewards = []
    penalties = []
    
    # Evaluate implementation completeness
    acceptance_criteria = task_data.get('acceptance_criteria', [])
    criteria_met = task_data.get('criteria_met', [])
    
    if len(criteria_met) == len(acceptance_criteria):
        rewards.append({'points': 3, 'reason': 'All acceptance criteria met'})
    elif len(criteria_met) >= len(acceptance_criteria) * 0.8:
        rewards.append({'points': 2, 'reason': 'Most acceptance criteria met'})
    else:
        penalties.append({'points': 3, 'reason': 'Incomplete implementation'})
    
    # Evaluate test coverage
    test_coverage = task_data.get('test_coverage', 0)
    
    if test_coverage >= 90:
        rewards.append({'points': 2, 'reason': 'Excellent test coverage (≥90%)'})
    elif test_coverage >= 80:
        rewards.append({'points': 2, 'reason': 'Good test coverage (≥80%)'})
    elif test_coverage < 60:
        penalties.append({'points': 2, 'reason': 'Insufficient test coverage (<60%)'})
    
    # Evaluate code quality
    if task_data.get('linting_errors', 0) == 0:
        rewards.append({'points': 1, 'reason': 'No linting errors'})
    
    if task_data.get('type_coverage', 0) >= 90:
        rewards.append({'points': 1, 'reason': 'Excellent type coverage'})
    
    # Evaluate documentation
    if task_data.get('documentation_updated', False):
        rewards.append({'points': 2, 'reason': 'Documentation updated'})
    else:
        penalties.append({'points': 1, 'reason': 'Documentation not updated'})
    
    # Evaluate performance
    if task_data.get('performance_optimized', False):
        rewards.append({'points': 2, 'reason': 'Performance optimization included'})
    
    # Evaluate security
    if task_data.get('security_review', False):
        rewards.append({'points': 2, 'reason': 'Security best practices followed'})
    
    # Evaluate error handling
    if task_data.get('error_handling', False):
        rewards.append({'points': 2, 'reason': 'Robust error handling'})
    else:
        penalties.append({'points': 1, 'reason': 'Weak error handling'})
    
    # Calculate final score
    total_rewards = sum(r['points'] for r in rewards)
    total_penalties = sum(p['points'] for p in penalties)
    
    final_score = base_score + total_rewards - total_penalties
    final_score = max(0, min(23, final_score))  # Clamp to 0-23
    
    return {
        'score': final_score,
        'base': base_score,
        'rewards': rewards,
        'penalties': penalties,
        'threshold': 18
    }
```

### 3.6 SessionEnd Handler

**Consolidates session and ensures memory consistency**:

```python
def on_session_end(context: EventContext):
    """
    Execute on session end.
    
    Responsibilities:
    1. Consolidate session memories
    2. Update memory-index.md
    3. Recalculate all checksums
    4. Apply archival rules
    5. Document session summary
    """
    
    memory_path = Path(".claude")
    session_id = context.data.get('session_id')
    
    print(f"\n{'='*60}")
    print(f"SESSION END: {session_id}")
    print(f"{'='*60}\n")
    
    # Step 1: Consolidate session memories
    session_summary = consolidate_session_memories(
        memory_path=memory_path,
        session_id=session_id,
        session_start=context.data.get('start_time'),
        session_end=context.timestamp
    )
    
    print(f"Session Duration: {session_summary['duration']}")
    print(f"Tasks Completed: {session_summary['tasks_completed']}")
    print(f"Errors Encountered: {session_summary['errors_encountered']}")
    print(f"Memory Files Modified: {session_summary['files_modified']}")
    
    # Step 2: Update memory-index.md
    update_memory_index(memory_path, session_summary)
    print(f"\n✓ Memory index updated")
    
    # Step 3: Recalculate checksums
    checksums = recalculate_all_checksums(memory_path)
    print(f"✓ Checksums recalculated ({len(checksums)} files)")
    
    # Step 4: Apply archival rules
    archived = apply_archival_rules(memory_path)
    
    if archived:
        print(f"\n✓ Archived {len(archived)} old memories:")
        for item in archived:
            print(f"  - {item['file']} → {item['archive_location']}")
    
    # Step 5: Update activeContext with session summary
    update_active_context_for_session_end(
        memory_path=memory_path,
        session_summary=session_summary,
        next_session_context=context.data.get('next_steps', '')
    )
    print(f"✓ Active context updated for next session")
    
    # Step 6: Verify memory integrity one final time
    integrity_ok = verify_memory_integrity(memory_path / "memory-index.md")
    
    if integrity_ok:
        print(f"\n✓ Final integrity check: PASS")
    else:
        print(f"\n✗ Final integrity check: FAIL")
        print(f"⚠ Memory corruption detected - review required")
    
    print(f"\n{'='*60}")
    print(f"Session closed successfully")
    print(f"Memory bank synchronized and validated")
    print(f"{'='*60}\n")
    
    return session_summary


def consolidate_session_memories(
    memory_path: Path,
    session_id: str,
    session_start: datetime,
    session_end: datetime
) -> Dict:
    """Consolidate all memories created during session."""
    
    duration = session_end - session_start
    
    # Find all files modified during session
    files_modified = []
    tasks_completed = 0
    errors_encountered = 0
    
    # Check task logs
    task_logs_dir = memory_path / "task-logs"
    if task_logs_dir.exists():
        for log_file in task_logs_dir.glob("*.md"):
            file_mtime = datetime.fromtimestamp(log_file.stat().st_mtime)
            
            if session_start <= file_mtime <= session_end:
                files_modified.append(f"task-logs/{log_file.name}")
                tasks_completed += 1
    
    # Check errors
    errors_dir = memory_path / "errors"
    if errors_dir.exists():
        for error_file in errors_dir.glob("*.md"):
            file_mtime = datetime.fromtimestamp(error_file.stat().st_mtime)
            
            if session_start <= file_mtime <= session_end:
                files_modified.append(f"errors/{error_file.name}")
                errors_encountered += 1
    
    # Check core files
    core_dir = memory_path / "core"
    for core_file in core_dir.glob("*.md"):
        file_mtime = datetime.fromtimestamp(core_file.stat().st_mtime)
        
        if session_start <= file_mtime <= session_end:
            files_modified.append(f"core/{core_file.name}")
    
    return {
        'session_id': session_id,
        'start': session_start.isoformat(),
        'end': session_end.isoformat(),
        'duration': str(duration),
        'tasks_completed': tasks_completed,
        'errors_encountered': errors_encountered,
        'files_modified': len(files_modified),
        'files_list': files_modified
    }


def apply_archival_rules(memory_path: Path) -> List[Dict]:
    """Apply archival rules to old memories."""
    
    archived = []
    now = datetime.now()
    
    # Rule 1: Archive task logs older than 30 days
    task_logs_dir = memory_path / "task-logs"
    if task_logs_dir.exists():
        for log_file in task_logs_dir.glob("*.md"):
            # Extract date from filename
            try:
                date_str = log_file.stem[:10]  # "2025-12-27"
                file_date = datetime.strptime(date_str, "%Y-%m-%d")
                
                if (now - file_date).days > 30:
                    # Archive it
                    archive_month = file_date.strftime("%Y-%m")
                    archive_dir = memory_path / "archive" / "task-logs" / archive_month
                    archive_dir.mkdir(parents=True, exist_ok=True)
                    
                    archive_path = archive_dir / log_file.name
                    log_file.rename(archive_path)
                    
                    archived.append({
                        'file': f"task-logs/{log_file.name}",
                        'archive_location': f"archive/task-logs/{archive_month}/{log_file.name}",
                        'reason': 'Older than 30 days'
                    })
            except ValueError:
                continue
    
    # Rule 2: Archive resolved errors after 7 days
    errors_dir = memory_path / "errors"
    if errors_dir.exists():
        for error_file in errors_dir.glob("*.md"):
            error_data = parse_memory_file(error_file)
            
            if error_data['metadata'].get('status') == 'resolved':
                file_mtime = datetime.fromtimestamp(error_file.stat().st_mtime)
                
                if (now - file_mtime).days > 7:
                    archive_month = file_mtime.strftime("%Y-%m")
                    archive_dir = memory_path / "archive" / "errors" / archive_month
                    archive_dir.mkdir(parents=True, exist_ok=True)
                    
                    archive_path = archive_dir / error_file.name
                    error_file.rename(archive_path)
                    
                    archived.append({
                        'file': f"errors/{error_file.name}",
                        'archive_location': f"archive/errors/{archive_month}/{error_file.name}",
                        'reason': 'Resolved for 7+ days'
                    })
    
    return archived
```

---

## 4. Memory Consolidation Strategies

**How short-term memories become long-term knowledge**

### 4.1 Task Log Summarization

**Condensing task details into reusable patterns**:

```python
from typing import List, Dict
import re

class MemoryConsolidator:
    """Consolidates short-term memories into long-term knowledge."""
    
    def __init__(self, memory_path: Path):
        self.memory_path = Path(memory_path)
    
    def consolidate_task_logs(self, days: int = 7) -> Dict:
        """
        Consolidate recent task logs into patterns and summaries.
        
        Args:
            days: Number of days of logs to consolidate
        
        Returns:
            Consolidation results with extracted patterns
        """
        
        # Load recent task logs
        task_logs = self._load_recent_task_logs(days)
        
        if not task_logs:
            return {'status': 'no_logs', 'patterns': []}
        
        # Extract patterns
        patterns = self._extract_patterns_from_logs(task_logs)
        
        # Create summaries
        summaries = self._create_summaries(task_logs)
        
        # Update systemPatterns.md
        if patterns:
            self._update_system_patterns(patterns)
        
        # Create consolidated summary file
        self._create_consolidated_summary(summaries, patterns)
        
        return {
            'status': 'success',
            'logs_processed': len(task_logs),
            'patterns_extracted': len(patterns),
            'summaries_created': len(summaries)
        }
    
    def _extract_patterns_from_logs(self, task_logs: List[Dict]) -> List[Dict]:
        """Extract reusable patterns from task logs."""
        
        patterns = []
        
        # Group logs by similarity
        groups = self._group_similar_tasks(task_logs)
        
        for group in groups:
            if len(group) >= 2:  # Pattern if repeated at least twice
                pattern = self._identify_common_pattern(group)
                if pattern:
                    patterns.append(pattern)
        
        return patterns
    
    def _group_similar_tasks(self, task_logs: List[Dict]) -> List[List[Dict]]:
        """Group similar tasks together."""
        
        groups = []
        processed = set()
        
        for i, log1 in enumerate(task_logs):
            if i in processed:
                continue
            
            group = [log1]
            processed.add(i)
            
            for j, log2 in enumerate(task_logs[i+1:], start=i+1):
                if j in processed:
                    continue
                
                # Calculate similarity
                similarity = self._calculate_task_similarity(log1, log2)
                
                if similarity > 0.6:  # 60% similar
                    group.append(log2)
                    processed.add(j)
            
            if len(group) > 1:
                groups.append(group)
        
        return groups
    
    def _identify_common_pattern(self, similar_tasks: List[Dict]) -> Dict:
        """Identify common pattern from similar tasks."""
        
        # Extract common approach
        approaches = [task.get('approach', '') for task in similar_tasks]
        common_approach = self._find_common_elements(approaches)
        
        # Extract common challenges
        challenges = [task.get('challenges', []) for task in similar_tasks]
        common_challenges = self._find_recurring_challenges(challenges)
        
        # Extract common solutions
        solutions = [task.get('solutions', []) for task in similar_tasks]
        common_solutions = self._find_common_elements(solutions)
        
        if not common_approach and not common_solutions:
            return None
        
        return {
            'name': self._generate_pattern_name(similar_tasks),
            'description': common_approach,
            'challenges': common_challenges,
            'solutions': common_solutions,
            'frequency': len(similar_tasks),
            'examples': [task['id'] for task in similar_tasks]
        }
```

### 4.2 Chain of Density Compression

**Progressive summarization for context compression**:

```python
class ChainOfDensityCompressor:
    """
    Implements Chain of Density for progressive summarization.
    
    Based on: "From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting"
    """
    
    def __init__(self, llm_client):
        self.llm = llm_client
    
    def compress(self, text: str, iterations: int = 5) -> List[str]:
        """
        Progressively compress text using Chain of Density.
        
        Each iteration creates a denser summary by:
        1. Identifying missing key entities
        2. Adding them while maintaining length
        3. Fusing/removing less important content
        
        Args:
            text: Original text to compress
            iterations: Number of compression iterations
        
        Returns:
            List of summaries (one per iteration, increasing density)
        """
        
        summaries = []
        previous_summary = None
        
        for i in range(iterations):
            words_per_sentence = 20 - (i * 2)  # Start at 20, decrease each iteration
            
            prompt = self._build_cod_prompt(
                original_text=text,
                previous_summary=previous_summary,
                words_per_sentence=words_per_sentence,
                iteration=i
            )
            
            summary = self.llm.generate(prompt)
            summaries.append(summary)
            previous_summary = summary
        
        return summaries
    
    def _build_cod_prompt(
        self,
        original_text: str,
        previous_summary: str,
        words_per_sentence: int,
        iteration: int
    ) -> str:
        """Build Chain of Density prompt."""
        
        if iteration == 0:
            return f"""Summarize the following text. Use approximately {words_per_sentence} words per sentence.

Text:
{original_text}

Summary:"""
        
        return f"""You previously created this summary:

{previous_summary}

Now make it denser by:
1. Identifying 1-3 key entities/concepts missing from the summary
2. Adding those entities while keeping the same length (~{words_per_sentence} words per sentence)
3. Fusing or removing less important content to make room

Original text for reference:
{original_text}

Denser summary:"""
```

### 4.3 Pattern Extraction Algorithm

**Identifying reusable patterns from work history**:

```python
class PatternExtractor:
    """Extract architectural and implementation patterns from memory."""
    
    def extract_patterns(
        self,
        task_logs: List[Dict],
        min_frequency: int = 2
    ) -> List[Dict]:
        """
        Extract patterns that appear multiple times.
        
        Patterns include:
        - Architectural decisions (same approach used repeatedly)
        - Error resolutions (same fix applied to similar errors)
        - Implementation strategies (same technique for similar problems)
        - Testing approaches (same test structure)
        """
        
        patterns = {
            'architectural': [],
            'error_resolution': [],
            'implementation': [],
            'testing': []
        }
        
        # Extract architectural patterns
        architectural_decisions = []
        for log in task_logs:
            decisions = log.get('decisions', [])
            architectural_decisions.extend(decisions)
        
        arch_patterns = self._find_recurring_decisions(
            architectural_decisions,
            min_frequency
        )
        patterns['architectural'] = arch_patterns
        
        # Extract error resolution patterns
        # ... (similar extraction logic)
        
        return patterns
    
    def _find_recurring_decisions(
        self,
        decisions: List[Dict],
        min_frequency: int
    ) -> List[Dict]:
        """Find decisions that recur across tasks."""
        
        # Group by decision type
        decision_groups = {}
        
        for decision in decisions:
            decision_type = self._classify_decision(decision)
            
            if decision_type not in decision_groups:
                decision_groups[decision_type] = []
            
            decision_groups[decision_type].append(decision)
        
        # Identify patterns
        recurring_patterns = []
        
        for decision_type, group in decision_groups.items():
            if len(group) >= min_frequency:
                pattern = {
                    'type': decision_type,
                    'frequency': len(group),
                    'common_rationale': self._extract_common_rationale(group),
                    'success_rate': self._calculate_success_rate(group),
                    'recommendations': self._generate_recommendations(group)
                }
                recurring_patterns.append(pattern)
        
        return recurring_patterns
```

---

## 5. Self-Healing Mechanisms

**Automatic detection and recovery from memory corruption**

### 5.1 Checksum Verification System

**MD5-based integrity checking**:

```python
import hashlib
from pathlib import Path
from typing import Dict, List

class ChecksumValidator:
    """Validates memory integrity using MD5 checksums."""
    
    def __init__(self, memory_path: Path):
        self.memory_path = Path(memory_path)
        self.index_file = self.memory_path / "memory-index.md"
    
    def calculate_checksum(self, file_path: Path) -> str:
        """Calculate MD5 checksum of file."""
        
        md5_hash = hashlib.md5()
        
        with open(file_path, "rb") as f:
            # Read in chunks to handle large files
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)
        
        return md5_hash.hexdigest()[:8]  # First 8 characters
    
    def verify_all(self) -> Dict:
        """
        Verify all memory files against stored checksums.
        
        Returns:
            Verification results with any corruptions detected
        """
        
        # Load expected checksums from index
        expected_checksums = self._load_checksums_from_index()
        
        results = {
            'total_files': len(expected_checksums),
            'valid': [],
            'corrupted': [],
            'missing': []
        }
        
        for file_info in expected_checksums:
            file_path = self.memory_path / file_info['path']
            expected = file_info['checksum']
            
            if not file_path.exists():
                results['missing'].append({
                    'path': file_info['path'],
                    'expected_checksum': expected
                })
                continue
            
            actual = self.calculate_checksum(file_path)
            
            if actual == expected:
                results['valid'].append(file_info['path'])
            else:
                results['corrupted'].append({
                    'path': file_info['path'],
                    'expected': expected,
                    'actual': actual
                })
        
        return results
    
    def update_checksums(self) -> int:
        """
        Recalculate and update all checksums in index.
        
        Returns:
            Number of checksums updated
        """
        
        checksums = []
        
        # Calculate checksums for all memory files
        for pattern in ['core/*.md', 'task-logs/*.md', 'errors/*.md']:
            for file_path in self.memory_path.glob(pattern):
                checksum = self.calculate_checksum(file_path)
                
                checksums.append({
                    'path': str(file_path.relative_to(self.memory_path)),
                    'checksum': checksum,
                    'modified': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
                })
        
        # Update index file
        self._write_checksums_to_index(checksums)
        
        return len(checksums)
    
    def _load_checksums_from_index(self) -> List[Dict]:
        """Parse checksums from memory-index.md."""
        
        if not self.index_file.exists():
            return []
        
        content = self.index_file.read_text()
        checksums = []
        
        # Parse checksum table
        # Format: | [[filename]] | Purpose | Version | Date | checksum | Status |
        
        for line in content.split('\n'):
            if '|' in line and not line.strip().startswith('#'):
                parts = [p.strip() for p in line.split('|')]
                
                if len(parts) >= 6 and parts[5]:  # Has checksum
                    # Extract filename from wiki-link
                    filename_match = re.search(r'\[\[(.+?)\]\]', parts[1])
                    if filename_match:
                        filename = filename_match.group(1) + '.md'
                        checksums.append({
                            'path': f'core/{filename}',
                            'checksum': parts[5]
                        })
        
        return checksums
```

### 5.2 Automatic Recovery Protocols

**Self-healing when corruption is detected**:

```python
class MemoryRecoverySystem:
    """Automatic recovery from memory corruption."""
    
    def __init__(self, memory_path: Path):
        self.memory_path = Path(memory_path)
        self.backup_path = self.memory_path / "versions"
    
    def recover(self, corruption_report: Dict) -> Dict:
        """
        Attempt automatic recovery from corruption.
        
        Strategy:
        1. For missing files: Restore from backup
        2. For corrupted files: Restore from backup or version history
        3. For irrecoverable files: Mark as corrupted, alert user
        """
        
        recovery_results = {
            'recovered': [],
            'failed': [],
            'user_intervention_needed': []
        }
        
        # Recover missing files
        for missing in corruption_report.get('missing', []):
            recovered = self._restore_from_backup(missing['path'])
            
            if recovered:
                recovery_results['recovered'].append({
                    'file': missing['path'],
                    'method': 'backup_restore'
                })
            else:
                recovery_results['failed'].append({
                    'file': missing['path'],
                    'reason': 'no_backup_found'
                })
        
        # Recover corrupted files
        for corrupted in corruption_report.get('corrupted', []):
            recovered = self._restore_from_version_history(corrupted['path'])
            
            if recovered:
                recovery_results['recovered'].append({
                    'file': corrupted['path'],
                    'method': 'version_restore'
                })
            else:
                # Try merging with backup
                merged = self._attempt_merge(corrupted['path'])
                
                if merged:
                    recovery_results['user_intervention_needed'].append({
                        'file': corrupted['path'],
                        'reason': 'manual_merge_required',
                        'merge_file': merged
                    })
                else:
                    recovery_results['failed'].append({
                        'file': corrupted['path'],
                        'reason': 'irrecoverable'
                    })
        
        return recovery_results
    
    def _restore_from_backup(self, file_path: str) -> bool:
        """Restore file from most recent backup."""
        
        # Look for backup in versions/ directory
        file_name = Path(file_path).name
        backup_dir = self.backup_path / Path(file_path).parent.name
        
        if not backup_dir.exists():
            return False
        
        # Find most recent version
        versions = sorted(backup_dir.glob(f"{file_name.replace('.md', '')}-v*.md"), reverse=True)
        
        if not versions:
            return False
        
        # Restore most recent version
        target_path = self.memory_path / file_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        shutil.copy(versions[0], target_path)
        
        print(f"✓ Restored {file_path} from {versions[0].name}")
        
        return True
```

### 5.3 Conflict Resolution

**Handling contradictory information**:

```python
class ConflictResolver:
    """Resolve conflicts in memory files."""
    
    def detect_conflicts(self, memory_path: Path) -> List[Dict]:
        """
        Detect contradictory information across memory files.
        
        Conflicts include:
        - Same decision with different rationales
        - Contradictory architectural patterns
        - Inconsistent technology choices
        """
        
        conflicts = []
        
        # Load all core memory files
        core_files = {}
        core_dir = memory_path / "core"
        
        for file_path in core_dir.glob("*.md"):
            core_files[file_path.name] = parse_memory_file(file_path)
        
        # Check for version mismatches
        version_conflicts = self._check_version_consistency(core_files)
        conflicts.extend(version_conflicts)
        
        # Check for contradictory decisions
        decision_conflicts = self._check_decision_consistency(core_files)
        conflicts.extend(decision_conflicts)
        
        return conflicts
    
    def resolve_conflict(self, conflict: Dict) -> Dict:
        """
        Resolve conflict using resolution strategy.
        
        Resolution strategies:
        1. Timestamp Priority: More recent modification wins
        2. Version Priority: Higher version number wins
        3. User Decision: Flag for manual resolution
        """
        
        strategy = self._determine_resolution_strategy(conflict)
        
        if strategy == "timestamp":
            return self._resolve_by_timestamp(conflict)
        elif strategy == "version":
            return self._resolve_by_version(conflict)
        else:
            return self._flag_for_user(conflict)
    
    def _resolve_by_timestamp(self, conflict: Dict) -> Dict:
        """More recent modification wins."""
        
        files = conflict['files']
        
        # Sort by modification time
        sorted_files = sorted(
            files,
            key=lambda f: f['modified'],
            reverse=True
        )
        
        winner = sorted_files[0]
        losers = sorted_files[1:]
        
        # Update losers to match winner
        for loser in losers:
            self._update_file_content(
                file_path=loser['path'],
                new_content=winner['content']
            )
        
        # Log resolution
        self._log_conflict_resolution(conflict, winner, "timestamp")
        
        return {
            'resolved': True,
            'strategy': 'timestamp',
            'winner': winner['path']
        }
```

---

## 6. Version Control for Memory

**Semantic versioning and rollback capabilities**

### 6.1 Semantic Versioning for Core Files

```python
from dataclasses import dataclass
from typing import Literal

@dataclass
class MemoryVersion:
    """Semantic version for memory files."""
    major: int
    minor: int
    patch: int
    
    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"
    
    @classmethod
    def parse(cls, version_str: str) -> 'MemoryVersion':
        """Parse version string."""
        parts = version_str.split('.')
        return cls(
            major=int(parts[0]),
            minor=int(parts[1]),
            patch=int(parts[2])
        )
    
    def increment(
        self,
        level: Literal["major", "minor", "patch"]
    ) -> 'MemoryVersion':
        """Increment version."""
        
        if level == "major":
            return MemoryVersion(self.major + 1, 0, 0)
        elif level == "minor":
            return MemoryVersion(self.major, self.minor + 1, 0)
        else:  # patch
            return MemoryVersion(self.major, self.minor, self.patch + 1)


class MemoryVersionControl:
    """Version control for memory files."""
    
    def __init__(self, memory_path: Path):
        self.memory_path = Path(memory_path)
        self.versions_path = self.memory_path / "versions"
        self.versions_path.mkdir(exist_ok=True)
    
    def commit_version(
        self,
        file_path: Path,
        change_type: Literal["major", "minor", "patch"],
        changelog_entry: str
    ) -> MemoryVersion:
        """
        Create new version of memory file.
        
        Args:
            file_path: Path to memory file
            change_type: Type of change (major/minor/patch)
            changelog_entry: Description of changes
        
        Returns:
            New version number
        """
        
        # Parse current version from file metadata
        file_data = parse_memory_file(file_path)
        current_version_str = file_data['metadata'].get('version', '0.0.0')
        current_version = MemoryVersion.parse(current_version_str)
        
        # Increment version
        new_version = current_version.increment(change_type)
        
        # Backup current version
        self._backup_version(file_path, current_version)
        
        # Update file with new version and changelog
        self._update_version_metadata(
            file_path,
            new_version,
            changelog_entry
        )
        
        print(f"✓ Version {current_version} → {new_version}")
        print(f"  {changelog_entry}")
        
        return new_version
    
    def rollback(
        self,
        file_path: Path,
        target_version: MemoryVersion
    ) -> bool:
        """
        Rollback file to previous version.
        
        Args:
            file_path: Path to memory file
            target_version: Version to restore
        
        Returns:
            Success status
        """
        
        # Find version backup
        backup_file = self._find_version_backup(file_path, target_version)
        
        if not backup_file:
            print(f"✗ Version {target_version} not found")
            return False
        
        # Restore from backup
        shutil.copy(backup_file, file_path)
        
        print(f"✓ Rolled back to version {target_version}")
        
        return True
    
    def _backup_version(self, file_path: Path, version: MemoryVersion):
        """Backup current version before updating."""
        
        # Create version-specific backup directory
        file_name = file_path.stem
        backup_dir = self.versions_path / file_path.parent.name
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        backup_file = backup_dir / f"{file_name}-v{version}.md"
        shutil.copy(file_path, backup_file)
        
        # Clean up old versions (keep max 5)
        self._cleanup_old_versions(backup_dir, file_name, max_versions=5)
```

---

## 7. Production Implementation

**Complete working system with examples**

### 7.1 Complete Integration Example

```python
#!/usr/bin/env python3
"""
SPES Advanced Memory System - Production Implementation
Complete working example integrating all components.
"""

from pathlib import Path
from datetime import datetime
import sys

class SPESAdvancedMemory:
    """Complete advanced memory system."""
    
    def __init__(self, memory_path: str = ".claude"):
        self.memory_path = Path(memory_path)
        
        # Initialize components
        self.event_manager = MemoryEventManager(self.memory_path)
        self.consolidator = MemoryConsolidator(self.memory_path)
        self.checksum_validator = ChecksumValidator(self.memory_path)
        self.version_control = MemoryVersionControl(self.memory_path)
        
        # Register event handlers
        self._register_handlers()
        
        # Initialize directory structure
        self._initialize_structure()
    
    def _register_handlers(self):
        """Register all event handlers."""
        
        self.event_manager.register_handler(
            MemoryEvent.SESSION_START,
            on_session_start
        )
        
        self.event_manager.register_handler(
            MemoryEvent.TASK_START,
            on_task_start
        )
        
        self.event_manager.register_handler(
            MemoryEvent.ERROR_DETECTED,
            on_error_detected
        )
        
        self.event_manager.register_handler(
            MemoryEvent.TASK_COMPLETE,
            on_task_complete
        )
        
        self.event_manager.register_handler(
            MemoryEvent.SESSION_END,
            on_session_end
        )
    
    def _initialize_structure(self):
        """Create directory structure if not exists."""
        
        directories = [
            "core",
            "task-logs",
            "errors",
            "plans",
            "archive/task-logs",
            "archive/errors",
            "embeddings",
            "versions"
        ]
        
        for dir_name in directories:
            (self.memory_path / dir_name).mkdir(parents=True, exist_ok=True)
    
    # Public API
    
    def start_session(self) -> str:
        """Start new session."""
        
        session_id = str(uuid.uuid4())
        
        self.event_manager.trigger(
            MemoryEvent.SESSION_START,
            {'session_id': session_id}
        )
        
        return session_id
    
    def start_task(
        self,
        description: str,
        acceptance_criteria: List[str] = None,
        dependencies: List[str] = None
    ) -> str:
        """Start new task."""
        
        task_data = {
            'description': description,
            'acceptance_criteria': acceptance_criteria or [],
            'dependencies': dependencies or []
        }
        
        result = self.event_manager.trigger(
            MemoryEvent.TASK_START,
            task_data
        )
        
        return result['task_id']
    
    def report_error(
        self,
        error_type: str,
        error_message: str,
        stack_trace: str = "",
        context: Dict = None
    ):
        """Report error."""
        
        error_data = {
            'type': error_type,
            'message': error_message,
            'stack_trace': stack_trace,
            'context': context or {}
        }
        
        self.event_manager.trigger(
            MemoryEvent.ERROR_DETECTED,
            error_data
        )
    
    def complete_task(
        self,
        task_id: str,
        criteria_met: List[str],
        test_coverage: float,
        **kwargs
    ):
        """Complete task."""
        
        task_data = {
            'task_id': task_id,
            'criteria_met': criteria_met,
            'test_coverage': test_coverage,
            **kwargs
        }
        
        self.event_manager.trigger(
            MemoryEvent.TASK_COMPLETE,
            task_data
        )
    
    def end_session(self, session_id: str):
        """End session."""
        
        self.event_manager.trigger(
            MemoryEvent.SESSION_END,
            {'session_id': session_id}
        )
    
    # Maintenance operations
    
    def consolidate_memories(self, days: int = 7):
        """Consolidate recent memories."""
        
        return self.consolidator.consolidate_task_logs(days)
    
    def verify_integrity(self) -> Dict:
        """Verify memory integrity."""
        
        return self.checksum_validator.verify_all()
    
    def update_checksums(self):
        """Update all checksums."""
        
        return self.checksum_validator.update_checksums()


# Example usage
def main():
    """Example workflow."""
    
    # Initialize memory system
    memory = SPESAdvancedMemory()
    
    # Start session
    session_id = memory.start_session()
    
    # Start task
    task_id = memory.start_task(
        description="Implement user authentication",
        acceptance_criteria=[
            "JWT token generation",
            "Token validation middleware",
            "Refresh token mechanism",
            "Test coverage >= 80%"
        ],
        dependencies=["PyJWT library"]
    )
    
    # Work happens here...
    
    # Report error if encountered
    try:
        # Some code that might fail
        pass
    except Exception as e:
        memory.report_error(
            error_type="authentication_error",
            error_message=str(e),
            stack_trace=traceback.format_exc()
        )
    
    # Complete task
    memory.complete_task(
        task_id=task_id,
        criteria_met=["JWT generation", "Token validation", "Refresh tokens"],
        test_coverage=85.0,
        documentation_updated=True,
        security_review=True
    )
    
    # End session
    memory.end_session(session_id)
    
    # Periodic maintenance
    memory.consolidate_memories(days=7)
    memory.verify_integrity()


if __name__ == "__main__":
    main()
```

### 7.2 Migration from Simple Memory

**Step-by-step migration guide**:

```bash
#!/bin/bash
# migrate_to_advanced_memory.sh

echo "Migrating to Advanced Memory System..."

# 1. Backup existing .claude directory
echo "Step 1: Backing up existing memory..."
cp -r .claude .claude.backup.$(date +%Y%m%d-%H%M%S)

# 2. Create new directory structure
echo "Step 2: Creating advanced directory structure..."
mkdir -p .claude/{core,task-logs,errors,plans,archive/{task-logs,errors},embeddings,versions}

# 3. Migrate existing files
echo "Step 3: Migrating existing files..."

# Move core files
if [ -f .claude/project-brief.md ]; then
    mv .claude/project-brief.md .claude/core/projectbrief.md
fi

# Add YAML frontmatter to existing files
echo "Step 4: Adding metadata to existing files..."
python3 add_frontmatter.py .claude/core/

# 5. Initialize memory index
echo "Step 5: Creating memory index..."
python3 -c "
from advanced_memory import SPESAdvancedMemory
memory = SPESAdvancedMemory()
memory.update_checksums()
"

echo "Migration complete!"
echo "Backup location: .claude.backup.*"
```

---

## Conclusion

This advanced memory architecture transforms SPES from a stateless prompt engineering system into a **cognitive architecture** with persistent memory, self-healing capabilities, and production-grade reliability.

**Key Takeaways**:

1. ✅ **Three-layer hierarchy** mirrors human cognition
2. ✅ **Event-driven workflows** automate memory management
3. ✅ **Self-healing mechanisms** ensure reliability
4. ✅ **Version control** enables rollback and recovery
5. ✅ **Production-ready** with complete implementations

**Next Steps**:
- Read Document 18: Semantic Retrieval & MCP Integration
- Implement advanced memory in your project
- Contribute improvements back to SPES

---

*Document 17 complete - Advanced Memory Architecture for SPES*
