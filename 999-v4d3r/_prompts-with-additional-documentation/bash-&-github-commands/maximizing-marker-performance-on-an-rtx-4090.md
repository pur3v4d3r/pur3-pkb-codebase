

# Maximizing Marker Performance on an RTX 4090


With an **RTX 4090 (24GB VRAM)**, you are currently driving a Ferrari in a school zone. The default settings of `marker` use only about ~3GB of VRAM, meaning 85%+ of your GPU is sitting idle.

Here is exactly how to redline your 4090 for maximum throughput.

### 1. The "Bulk Processing" Config (Best for your Research Papers)

Since you are converting a library of PDFs, parallelism is king. Each "worker" in marker consumes about ~3-5GB of VRAM. Your 4090 can comfortably run **4 workers** simultaneously without crashing.

**Run this command:**

```bash
TORCH_DEVICE=cuda marker /input/papers /output/markdown --workers 4 --batch_multiplier 2

```

* **Why:** This runs 4 concurrent conversion pipelines. You will process 4 papers in the time it usually takes to do one.
* **VRAM Usage:** ~12-20GB (Leaves room for desktop overhead).

### 2. The "Single File" Config (Best for Massive Books)

If you are converting one massive PDF (e.g., a 500-page textbook), parallelism won't help. Instead, you need to increase the batch size to feed the GPU more data at once.

**Run this command:**

```bash
TORCH_DEVICE=cuda marker_single /path/to/big_book.pdf /output/dir --batch_multiplier 10

```

* **Why:** Default multiplier is 2. Crank it to 10. This forces the model to process huge chunks of pages in a single VRAM pass.
* **Warning:** If you get an OOM (Out of Memory) error, lower this to 8.

### 3. The "Speed Demon" Config (No OCR)

If your PDFs are standard ArXiv downloads (which have digital text layers), you can skip the OCR model (`surya`) entirely. This makes the 4090 nearly instant because it only needs to run layout detection, not character recognition.

**Run this command:**

```bash
OCR_ENGINE=None marker /input/papers /output/markdown --workers 8 --batch_multiplier 2

```

* **Why:** Without the heavy OCR model loaded, the VRAM footprint drops significantly, allowing you to double the worker count to **8**.

### Summary Recommendation

For your specific task of ingesting research papers: **Use Config #1 (4 Workers)**. It provides the best balance of speed and stability for mixed PDF types.