---
tags: #pkm #obsidian #reference-note #quick-reference
aliases: [Wiki-Link QRC, Linking Guide, Knowledge Graph Reference]
---

# 🔗 Quick Reference: Wiki-Link Protocol

## Discovery Heuristic: When to Create Links

**CREATE `[[Wiki-Link]]` if ANY of these are true:**

✅ Core concept central to response  
✅ Technical term requiring definition  
✅ Topic with potential for separate note  
✅ Cross-reference opportunity to existing knowledge  
✅ Subject area with exploratory depth  
✅ Framework or methodology with theoretical foundation  
✅ Person/author significant to the field  
✅ Tool or plugin in ecosystem  
✅ Process or technique with procedural knowledge  

**DO NOT link:**

❌ Generic terms not specific to domain ("things", "ideas")  
❌ Every mention of same term (link first occurrence only per section)  
❌ Common words just because notes might exist  
❌ Trivial concepts not warranting dedicated notes  

## Target Density by Note Type

| Note Type | Target Wiki-Links | Links per Section |
|-----------|-------------------|-------------------|
| **Simple Query** | 3-6 | 2-3 |
| **Atomic Note** | 5-8 | 3-5 |
| **Reference Note** | 20-40 | 5-15 |
| **MOC** | 30-100+ | N/A (primary feature) |
| **Synthesis Note** | 15-30 | 5-10 |
| **Technical Guide** | 15-40 | 5-12 |

## Link Format Patterns

**Standard Link:**
````markdown
[[Note Title]]
````

**Display Text Link:**
````markdown
[[Note Title|Display Text]]
````
Use when: Grammatical integration, shortened reference, alternative phrasing

**Section Link:**
````markdown
[[Note Title#Section Heading]]
[[Note Title#Section|Display Text]]
````

**Block Link:**
````markdown
[[Note Title#^block-id]]
````

## Quality Decision Tree
````
FOR each potential link candidate:

Does term represent discrete, learnable concept?
├─ NO → Don't link
└─ YES → Continue

Would reader benefit from dedicated note?
├─ NO → Keep as plain text
└─ YES → Continue

Does link create meaningful graph connection?
├─ NO → Reconsider
└─ YES → Continue

Has term been linked in this section already?
├─ YES → Don't link again
└─ NO → CREATE LINK [[Term]]
````

## Link Pattern Examples

> [!example] Good Linking
> [[Cognitive Load Theory]] explains how cognitive load affects learning. When load exceeds capacity, it overwhelms [[Working Memory]].
> 
> *Links key concepts once per section*

> [!warning] Over-Linking (Avoid)
> [[Cognitive Load]] theory explains how [[cognitive load]] affects learning. When [[cognitive load]] is too high, [[cognitive load]] overwhelms [[working memory]].
> 
> *Same term linked repeatedly = visual clutter*

> [!warning] Under-Linking (Avoid)
> Cognitive Load Theory explains how cognitive load affects learning through working memory constraints and schema construction.
> 
> *Missing obvious opportunities for key concepts*

## Category-Specific Linking

**Theoretical Frameworks:**
````markdown
[[Cognitive Load Theory]], [[Self-Determination Theory]], [[Dual Coding Theory]]
````

**Technical Terms:**
````markdown
[[Dataview]], [[DQL]], [[DataviewJS]], [[Meta Bind]]
````

**Methodologies:**
````markdown
[[Zettelkasten]], [[Progressive Summarization]], [[Spaced Repetition]]
````

**Processes:**
````markdown
[[Atomic Note Creation]], [[MOC Development]], [[Knowledge Graph Building]]
````

## Bi-Directional Linking Strategy

When creating links, consider:

**Forward Links** (this note → others):
- Primary connections outward

**Potential Backlinks** (others → this note):
- What existing notes should link here?
- Mention in "Related Topics" section

**Example:**
````markdown
In [[Cognitive Load Theory]]:

Forward links to:
- [[Working Memory]]
- [[Schema Theory]]
- [[Instructional Design]]

Should be linked from:
- [[Learning Theory Overview]]
- [[Educational Psychology]]
- [[Multimedia Learning]]
````

## Link Density Self-Check
````
Squint test: Can you identify 5-8 key concepts by scanning for wiki-links?
├─ YES → Good density
└─ NO → Adjust (too sparse or too dense)

Every paragraph has links?
├─ YES → Good knowledge graph building
└─ NO → Scan for missed opportunities

Every sentence has links?
├─ YES → Probably over-linking (reduce)
└─ NO → Check if key concepts are linked
````

## Integration with Display Text

**Use display text for:**

1. **Grammatical flow:**
````markdown
   theories of [[Cognitive Load Theory|cognitive load]]
````

2. **Abbreviation expansion:**
````markdown
   [[Self-Determination Theory|SDT]]
````

3. **Section-specific reference:**
````markdown
   [[Cognitive Load Theory#Intrinsic Load|intrinsic cognitive load]]
````

4. **Alternative phrasing:**
````markdown
   [[Progressive Summarization|layer-based distillation]]
````