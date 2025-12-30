---
created: "<% tp.date.now("YYYY-MM-DD") %>"
week: "<% tp.date.now("gggg-[W]WW")%>"
month: "<% tp.date.now("YYYY-MM") %>"
quarter: "<% tp.date.now("YYYY-[Q]Q")%>"
year: "<% tp.date.now("YYYY") %>"
id: "<% tp.date.now("YYYYMMDD-HHmmss") %>"
type: person-profile
person_type: <% await tp.system.suggester(["Academic Researcher", "Theorist/Philosopher", "Author/Writer", "Practitioner/Innovator", "Interdisciplinary Scholar"], ["researcher", "theorist", "author", "practitioner", "interdisciplinary"]) %>
primary_discipline: "<% await tp.system.prompt("Primary academic discipline/field") %>"
research_area: 
  - "<% await tp.system.prompt("Research area 1") %>"
aliases:
  - <% tp.file.title %>
tags:
  - pkm/research
  - cognitive-science
  - learning-theory/andragogy
  - learning-science
  - educational-psychology
  - expertise-development
  - encoding
  - type/permanent
  - context/research
  - source/documentation
  - context/theoretical
  - nature/declarative
---

# <% tp.file.title %>

> [!abstract] Academic Overview
> [**Primary Role**:: <% tp.frontmatter.person_type %>]
> [**Discipline**:: <% tp.frontmatter.primary_discipline %>]
> [**Institution**:: ]
> [**Research Focus**:: <% tp.frontmatter.research_area %>]

---

## 👤 Biographical Context

**Education:**
- 
- 

**Career Highlights:**
- 
- 

**Current Position:**


**Notable Affiliations:**
- 

---

## 🎓 Academic Contributions

### Primary Research Areas

**Area 1**: 
- Core questions addressed:
- Methodological approach:
- Unique perspective/contribution:

**Area 2**: 
- Core questions addressed:
- Methodological approach:
- Unique perspective/contribution:

### Key Publications

> [!evidence] Foundational Works

**Publication 1:**
- **Title**: 
- **Year**: 
- **Type**: [Book | Journal Article | Monograph | Report]
- **Significance**: 
- **Link**: 

**Publication 2:**
- **Title**: 
- **Year**: 
- **Type**: 
- **Significance**: 
- **Link**: 

**Publication 3:**
- **Title**: 
- **Year**: 
- **Type**: 
- **Significance**: 
- **Link**: 

### Theoretical Frameworks & Concepts

> [!key-claim] Major Contributions to Field

**Concept/Framework 1**: [[Concept Name]]
- **Description**: 
- **Origin**: [Which work introduced this]
- **Impact**: 
- **Critiques**: 

**Concept/Framework 2**: [[Concept Name]]
- **Description**: 
- **Origin**: 
- **Impact**: 
- **Critiques**: 

---

## 💡 Intellectual Influence

### Why I Admire Their Work

**Core Ideas That Resonate:**
1. 
2. 
3. 

**Methodological Lessons:**


**Conceptual Clarity:**


### How Their Work Informs Mine

> [!thought-experiment] Integration Points

**My Research Areas Influenced:**
- [[My Research Topic 1]]: 
- [[My Research Topic 2]]: 

**Frameworks I've Adopted:**
- 

**Questions They've Inspired Me to Explore:**
- 
- 

---

## 🔗 Intellectual Network

**Frequent Collaborators:**
- [[Collaborator 1]]
- [[Collaborator 2]]

**Intellectual Lineage:**
- **Mentors/Influences**: 
- **Students/Mentees**: 

**Academic Debates/Discourse:**
- **In dialogue with**: 
- **Critical responses to**: 
- **Building on work of**: 

---

## 📚 Reading Notes & Synthesis

### Works I've Read
```
TABLE 
  file.link AS "Note",
  author AS "Author",
  year AS "Year",
  type AS "Type"
FROM [[<% tp.file.title %>]]
WHERE type = "literature-note" OR contains(file.tags, "literature-note")
SORT year DESC
```

### Key Quotes & Concepts

> [!quote] Notable Quote 1
> "Quote text here"
> 
> **Source**: [Publication/Context]
> **Significance**: 

> [!quote] Notable Quote 2
> "Quote text here"
> 
> **Source**: 
> **Significance**: 

---

## 🎯 Further Exploration

**Works I Want to Read:**
- [ ] [Publication title]
- [ ] [Publication title]

**Talks/Lectures to Watch:**
- [ ] [Talk title] - [Link]

**Research Questions to Investigate:**
- 
- 

**Related Scholars to Explore:**
- [[Person Name 1]]
- [[Person Name 2]]

---

## 🔖 External Resources

**Primary Website**: 

**Academic Profiles:**
- Google Scholar: 
- ORCID: 
- ResearchGate: 
- Academia.edu: 

**Social/Public Scholarship:**
- Twitter/X: 
- Blog: 
- Podcast Appearances: 

**Institutional Profile**: 

---

## 📝 Personal Notes & Reflections



---

*Profile Created: <% tp.date.now("YYYY-MM-DD") %>*
*Last Updated: <% tp.date.now("YYYY-MM-DD") %>*