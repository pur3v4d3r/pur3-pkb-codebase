---
tags: #spes #component-library #personas #index
aliases: [Personas Index, Role Library]
status: reference
created: 2025-12-20
---

# Personas Index

> [!abstract] Purpose
> Catalog of persona/role components. These establish identity, expertise level, and behavioral frameworks for prompts.

---

## 📋 ALL PERSONAS

```dataview
TABLE domain, rating, usage-count, performance-score, maturity
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library/atomic/personas"
WHERE type = "component"
SORT rating DESC, usage-count DESC
```

---

## 🎯 PERSONA DESIGN GUIDELINES

### What Makes a Good Persona?
1. **Specific Role**: Clear expertise area (not generic "expert")
2. **Behavioral Framework**: Implies approach and values
3. **Authority Level**: Establishes credibility
4. **Domain Alignment**: Matches task requirements

### Common Persona Patterns
- **Expert Specialist**: "You are an expert [domain] specialist with 10+ years experience..."
- **Teacher/Tutor**: "You are a patient, clear educator specializing in..."
- **Analyst**: "You are a rigorous analyst focused on..."
- **Creative Partner**: "You are a creative collaborator who..."
- **Technical Authority**: "You are a senior [role] with deep expertise in..."

### When to Use Personas
✅ Complex domain requiring expertise framing
✅ Specific behavioral approach needed (patient, rigorous, creative)
✅ Multi-turn conversations benefit from consistent identity
✅ User needs to establish authority/credibility

### When NOT to Use Personas
❌ Simple, straightforward tasks
❌ Generic "you are an AI assistant" (adds no value)
❌ Multiple conflicting identities in same prompt

---

## 🌐 BY DOMAIN

### General Personas
```dataview
LIST
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library/atomic/personas"
WHERE type = "component" AND domain = "general"
SORT rating DESC
```

### Technical Personas
```dataview
LIST
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library/atomic/personas"
WHERE type = "component" AND domain = "technical"
SORT rating DESC
```

### Creative Personas
```dataview
LIST
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library/atomic/personas"
WHERE type = "component" AND domain = "creative"
SORT rating DESC
```

### Educational Personas
```dataview
LIST
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library/atomic/personas"
WHERE type = "component" AND domain = "educational"
SORT rating DESC
```

---

*Index auto-updates via Dataview | Created: 2025-12-20*
