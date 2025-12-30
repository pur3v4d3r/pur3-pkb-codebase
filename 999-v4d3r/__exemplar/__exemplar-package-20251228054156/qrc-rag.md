---
tags: #quick-reference #rag #retrieval #knowledge-integration #one-pager
type: quick-reference
technique: Retrieval-Augmented Generation
category: knowledge-integration
---

# 📚 Retrieval-Augmented Generation (RAG) - Quick Reference

## One-Line Summary
Retrieve relevant documents from knowledge base, include as context in prompt, LLM generates grounded answer.

---

## When to Use
✅ **Perfect For**: Factual QA, current events, enterprise knowledge bases, reducing hallucination
❌ **Skip For**: Commonsense reasoning (LLM already knows), creative tasks, pure calculations

---

## Architecture

```
User Query
    ↓
① RETRIEVE relevant docs (vector search)
    ↓  
② FORMAT as context
    ↓
③ GENERATE answer with context
    ↓
Final Answer (grounded in docs)
```

---

## Implementation Template

```python
def rag_answer(query, knowledge_base, top_k=5):
    """
    Basic RAG implementation
    """
    # Step 1: Retrieve documents
    retrieved = knowledge_base.retrieve(query, top_k=top_k)
    
    # Step 2: Format context
    context = "\n\n".join([
        f"[{i+1}] {doc['text']}"
        for i, doc in enumerate(retrieved)
    ])
    
    # Step 3: Generate with context
    prompt = f"""Answer based on the context below.

Context:
{context}

Question: {query}

Answer:"""
    
    answer = llm.complete(prompt, temperature=0.3)
    
    return {
        'answer': answer,
        'sources': retrieved
    }
```

---

## Knowledge Base Setup

```python
from sentence_transformers import SentenceTransformer
import numpy as np

class VectorKB:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.documents = []
        self.embeddings = None
    
    def add_documents(self, docs):
        """Add documents with embeddings"""
        self.documents.extend(docs)
        texts = [d['text'] for d in docs]
        new_embs = self.model.encode(texts)
        
        if self.embeddings is None:
            self.embeddings = new_embs
        else:
            self.embeddings = np.vstack([self.embeddings, new_embs])
    
    def retrieve(self, query, top_k=5):
        """Semantic search"""
        query_emb = self.model.encode([query])[0]
        scores = np.dot(self.embeddings, query_emb)
        top_idx = np.argsort(scores)[-top_k:][::-1]
        
        return [
            {'document': self.documents[i], 'score': scores[i]}
            for i in top_idx
        ]
```

---

## Prompt Template

```
Answer the question based on the context provided.
If the context doesn't contain enough information, say so.

Context:
[Document 1] {text}

[Document 2] {text}

[Document 3] {text}

Question: {query}

Instructions:
- Base answer on context above
- Cite sources using [Document N] format
- If uncertain, acknowledge gaps

Answer:
```

---

## Performance Benchmarks
- **Natural Questions**: 54.7% (vs 32.1% LLM only) - **+22.6pp**
- **TriviaQA**: 68.4% (vs 58.3% LLM only) - **+10.1pp**
- **Hallucination Reduction**: 15% → **3-5%** with RAG

---

## Costs
- **Embedding**: One-time per document (~$0.0001 per 1K tokens)
- **Retrieval**: ~1ms per query (fast!)
- **Generation**: Same as baseline + context tokens
- **Total**: ~2-3x baseline cost

---

## Key Parameters

| Parameter | Range | Recommendation |
|-----------|-------|----------------|
| **top_k** | 3-10 | 5 for general, 10 for complex |
| **chunk_size** | 200-1000 tokens | 512 for balance |
| **embedding_model** | Various | MiniLM (fast), E5 (quality) |

---

## Document Chunking

Critical for quality retrieval:

```python
def chunk_document(text, chunk_size=512, overlap=50):
    """
    Split document with overlap
    """
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    
    return chunks
```

**Best Practices**:
- Chunk size 256-512 tokens (balance specificity vs context)
- Overlap 10-20% (preserve continuity)
- Respect semantic boundaries (paragraphs, sections)

---

## Common Pitfalls
❌ Documents too long → poor retrieval granularity
❌ No overlap → context breaks at chunk boundaries  
❌ Generic embeddings → poor domain performance
❌ No metadata → can't filter results
❌ top_k too low → miss relevant docs

✅ **Fix**: Chunk properly, tune top_k, use metadata filtering

---

## Advanced: Reranking

```python
def rag_with_rerank(query, kb, initial_k=20, final_k=5):
    """
    Retrieve many, rerank with LLM, keep best
    """
    # Initial retrieval (broad)
    candidates = kb.retrieve(query, top_k=initial_k)
    
    # Rerank with LLM
    reranked = []
    for doc in candidates:
        score_prompt = f"""Rate relevance (0-10):

Query: {query}
Document: {doc['text'][:200]}...

Score:"""
        score = float(llm.complete(score_prompt, temp=0.0))
        reranked.append({**doc, 'llm_score': score})
    
    # Sort by LLM score, take top final_k
    reranked.sort(key=lambda x: x['llm_score'], reverse=True)
    top_docs = reranked[:final_k]
    
    # Generate with reranked docs
    return rag_answer_from_docs(query, top_docs)
```

**Benefit**: +5-10pp accuracy vs basic RAG
**Cost**: Adds N LLM calls for scoring

---

## Advanced: Hybrid Search

```python
def hybrid_retrieval(query, kb):
    """
    Combine semantic (dense) + keyword (sparse)
    """
    # Semantic retrieval
    semantic_results = kb.semantic_search(query, top_k=10)
    
    # Keyword retrieval (BM25)
    keyword_results = kb.keyword_search(query, top_k=10)
    
    # Merge and deduplicate
    combined = merge_results(
        semantic_results,
        keyword_results,
        weights={'semantic': 0.7, 'keyword': 0.3}
    )
    
    return combined[:5]
```

**Benefit**: Better on both semantic and exact match queries

---

## Combinations

| Combine With | Benefit | Use Case |
|--------------|---------|----------|
| **CoVe** | Verify retrieved facts | High-accuracy needs |
| **Self-Refine** | Polish answer quality | Content generation |
| **ReAct** | Agent-driven retrieval | Multi-step research |

---

## Metadata Filtering

```python
# Add metadata during indexing
kb.add_documents([
    {
        'text': 'Document content...',
        'metadata': {
            'source': 'research_paper',
            'date': '2023-05-15',
            'category': 'medicine'
        }
    }
])

# Filter during retrieval
results = kb.retrieve(
    query,
    filters={'category': 'medicine', 'date': {'$gte': '2023-01-01'}}
)
```

---

## Production Checklist
- [ ] Documents chunked appropriately (256-512 tokens)
- [ ] Embeddings generated and indexed
- [ ] Metadata included (source, date, category)
- [ ] top_k tuned for use case
- [ ] Citation format specified in prompt
- [ ] Fallback for "not enough context" cases
- [ ] Monitoring retrieval quality

---

## Example: Customer Support

**Knowledge Base**: Product documentation, FAQs, support articles

**Query**: "How do I reset my password?"

**Retrieved**:
```
[1] To reset password: Go to Settings > Security > Reset Password
[2] Password requirements: 12+ chars, uppercase, number, symbol
[3] If forgot password: Click "Forgot?" on login page
```

**Answer**: "To reset your password, go to Settings > Security > Reset Password [1]. If you've forgotten your password, click 'Forgot Password?' on the login page [3]."

---

## Research
**Lewis et al. 2020** - "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
📄 https://arxiv.org/abs/2005.11401

---

**Related Techniques**: [[Generated Knowledge]], [[Recitation-Augmented]], [[Chain of Verification]]
**Full Guide**: [[05-knowledge-integration-guide#RAG]]
