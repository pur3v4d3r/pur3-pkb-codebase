---
batch_name: 2026-04-25-batch-02-pkm-architecture
batch_date: 2026-04-25
default_domain: pkm
default_confidence: high
notes: |
  PKM & Knowledge Architecture cluster. Seeds the foundational
  notetaking-method concepts (Zettelkasten lineage, Forte's CODE/PARA
  lineage, MOC architecture) so downstream notes link into a coherent
  PKM sub-graph.
---

# Batch: PKM & Knowledge Architecture

## Progressive Summarization

- secondary_domains: [notetaking, knowledge-management]
- aliases: [PS]
- broader: [note-making-vs-note-taking]
- related: [evergreen-notes, literature-notes, atomic-notes, commonplace-book]
- prerequisites: [personal-knowledge-management]

**definition**: Progressive Summarization is Tiago Forte's notetaking technique in which a captured source is distilled in successive layers — bolding the key passages, then highlighting the most essential of those bolds, then writing an executive summary — so that future re-encounters with the note can land at whichever depth the situation requires.

**key_claim**: Progressive Summarization treats compression as a future-discoverability problem rather than a comprehension problem: each layer is added at the moment of demonstrated demand, which prevents the upfront-summarization tax that derails most highlighting workflows.

**warning**: Progressive Summarization is often performed all-at-once on capture, which collapses it back into ordinary highlighting and loses the temporal structure that makes the method work; the layers are valuable only when they are added at separate moments of genuine re-engagement.

## Literature Notes

- secondary_domains: [zettelkasten, notetaking]
- aliases: [reference notes, source notes]
- broader: [zettelkasten]
- related: [fleeting-notes, evergreen-notes, atomic-notes, progressive-summarization]
- prerequisites: [zettelkasten]

**definition**: Literature Notes are the second layer of the Zettelkasten workflow — restatements of source material in the reader's own words, indexed to the source — that sit between raw fleeting notes and the permanent atomic-note network and serve as the staging area for ideas that may eventually become permanent.

**key_claim**: Literature Notes are not a summary archive; their purpose is to force the act of reformulation that exposes whether a source has actually been understood, which is why copy-pasted highlights cannot substitute for them even when they look superficially complete.

**warning**: Treating Literature Notes as the final destination of a reading session — instead of as input to the permanent-note layer — produces a growing pile of source-keyed notes that never fuse into the writer's own thinking, which is the most common failure mode of beginner Zettelkasten practice.

## Fleeting Notes

- secondary_domains: [zettelkasten, notetaking]
- aliases: [scratch notes, capture notes]
- broader: [zettelkasten]
- related: [literature-notes, evergreen-notes, atomic-notes]
- prerequisites: [zettelkasten]

**definition**: Fleeting Notes are the first layer of the Zettelkasten workflow — short, low-friction captures of in-the-moment thoughts, observations, or quotes — that are deliberately discardable and serve only as raw material to be processed within a short window into Literature or Permanent notes.

**key_claim**: Fleeting Notes derive their value from being processed quickly and then discarded; their permanence is a workflow anti-pattern, because an inbox of unprocessed Fleeting Notes silently degrades the trust the writer places in capture itself.

**warning**: The most common Fleeting Notes failure is treating them as durable storage — using a "captures" folder as a perpetual inbox — which inverts the design and recreates the read-it-later graveyard the layer was meant to prevent.

## Commonplace Book

- secondary_domains: [intellectual-history, notetaking]
- aliases: [commonplace, florilegium]
- broader: [personal-knowledge-management]
- related: [zettelkasten, literature-notes, progressive-summarization]
- prerequisites: [personal-knowledge-management]

**definition**: A Commonplace Book is the historical predecessor to modern personal knowledge management — a hand-kept manuscript in which a reader copies, indexes, and cross-references quotations, observations, and arguments encountered across many sources, organizing them by topic for later rhetorical or intellectual reuse.

**key_claim**: The Commonplace Book is the institutional memory of how literate cultures handled cross-source synthesis before databases, and its core mechanic — topical re-grouping of fragments excerpted from many works — is the direct ancestor of every tag-based and link-based PKM system that followed.

**warning**: Romanticizing the Commonplace Book as a complete model for digital PKM ignores its most important constraint: hand-copying enforced selectivity, and the modern frictionless equivalent (clipping at scale) reproduces the form while destroying the discipline that gave it value.

## Knowledge Graph Topology

- secondary_domains: [graph-theory, knowledge-management]
- aliases: [PKM graph topology]
- broader: [knowledge-graph]
- related: [maps-of-content, atomic-notes, the-link-supremacy-thesis]
- prerequisites: [knowledge-graph]

**definition**: Knowledge Graph Topology is the structural shape of a personal knowledge graph — the distribution of node degrees, the presence and size of connected components, the prevalence of hubs versus orphans — and is the lens through which the health of a notes network can be diagnosed independently of the content of any single note.

**key_claim**: Knowledge Graph Topology, not raw note count, predicts whether a PKM will support discovery: a graph with hubs and short path lengths surfaces unexpected connections, while a graph with the same notes but tree-like topology behaves like a folder system that merely happens to support links.

**warning**: Optimizing Knowledge Graph Topology by adding links indiscriminately — to make the network look denser — produces a graph in which everything is close to everything and nothing is meaningfully proximate, which destroys the discriminative value that made topology informative in the first place.

## Evergreen Notes

- secondary_domains: [zettelkasten, notetaking]
- aliases: [evergreen note]
- broader: [atomic-notes]
- related: [zettelkasten, literature-notes, progressive-summarization, maps-of-content]
- prerequisites: [zettelkasten]

**definition**: Evergreen Notes are Andy Matuschak's formulation of permanent notes — notes that are atomic, concept-oriented, densely linked, and continually refined over years rather than written once and archived — and that are designed to compound in value as the network around them grows.

**key_claim**: Evergreen Notes treat the note as a position the writer is willing to defend at this date, which is why their refinement is a first-class long-running activity rather than a write-once-and-archive event, and why the refactoring habit is the load-bearing mechanism of the practice.

**warning**: Evergreen Notes degrade into a vanity collection when the refinement habit lapses — once notes stop being revisited and re-linked, the network loses its compounding property and becomes indistinguishable from any other static notes folder.

## Maps of Content

- secondary_domains: [zettelkasten, notetaking]
- aliases: [MOC, MOCs]
- broader: [knowledge-graph-topology]
- related: [atomic-notes, evergreen-notes, knowledge-graph]
- prerequisites: [atomic-notes]

**definition**: Maps of Content are curated index notes — popularized by Nick Milo's LYT framework — that group, sequence, and contextualize a set of related atomic notes, providing the navigational scaffolding that pure tag-and-link networks lack while preserving the atomic structure of the underlying notes.

**key_claim**: Maps of Content resolve the tension between atomicity and navigability: the atomic notes carry the load-bearing knowledge, while the MOC carries the editorial perspective on how those notes should be encountered, and conflating the two layers degrades both.

**warning**: A common Maps of Content failure mode is to write the MOC first as a placeholder for notes that do not yet exist; this re-creates a folder hierarchy with extra steps and forfeits the bottom-up emergent-structure property that made MOCs a useful intermediate layer.

## Atomic Notes

- secondary_domains: [zettelkasten, notetaking]
- aliases: [atomic note, zettel]
- broader: [zettelkasten]
- related: [evergreen-notes, maps-of-content, the-link-supremacy-thesis]
- prerequisites: [zettelkasten]

**definition**: Atomic Notes are notes that capture exactly one self-contained idea per file, named so that the note's title itself is a usable claim or concept, which makes each note independently linkable and reusable across multiple contexts without requiring the surrounding context that produced it.

**key_claim**: Atomic Notes are what make a notes network behave like a knowledge graph rather than a document store: only when each idea has its own addressable identity can it become a node that other ideas connect to, which is the precondition for emergent structure.

**warning**: Pursuing atomicity as a length target — splitting any note over N words — misses the principle, which is conceptual unity; a 1,500-word note about one idea is more atomic than three 200-word notes that fragment a single argument.

## Knowledge Graph

- secondary_domains: [graph-theory, knowledge-management]
- aliases: [PKM knowledge graph]
- broader: [externalized-cognitive-architecture]
- related: [atomic-notes, knowledge-graph-topology, maps-of-content, zettelkasten]
- prerequisites: [personal-knowledge-management]

**definition**: A Knowledge Graph in the PKM context is a network whose nodes are atomic concept-notes and whose edges are typed or untyped links between them, treated as the primary representation of the writer's knowledge rather than as a navigation aid layered on top of folders.

**key_claim**: A Knowledge Graph differs from a hyperlinked document collection in that the graph itself — its nodes, edges, and emergent topology — is the artifact being maintained, which is why graph-aware tools surface affordances (orphan detection, hub analysis, link suggestion) that document-centric tools cannot.

**warning**: A Knowledge Graph is not automatically valuable because it exists; without disciplined atomicity and link curation, the same set of notes produces a graph that reflects only the accidents of historical capture rather than any defensible ontology of the domain.
