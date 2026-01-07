









999-v4d3r\__exemplar\__exemplar-package-20251228054156


D:\10_pur3v4d3r's-vault\999-v4d3r\__exemplar\__exemplar-package-20251228054156\prompt-patterns.pdf

999-v4d3r\__exemplar\__exemplar-package-20251228054156\prompt-patterns.pdf




marker_single 999-v4d3r\__exemplar\__exemplar-package-20251228054156\prompt-patterns.pdf 999-v4d3r\__exemplar\__exemplar-package-20251228054156: OUTPUT_DIR [OPTIONS]


The correct bash command to generate the markdown version of the specified PDF file using `marker_single` would be:

```bash
marker_single '999-v4d3r\__exemplar\__exemplar-package-20251228054156\prompt-patterns.pdf' --output_format markdown
```






---

## tags: [cli-reference, pdf-conversion, ocr, machine-learning, python-tooling] aliases: [Marker CLI, Datalab Marker Commands, marker_single, marker-pdf] created: 2026-01-07 status: evergreen certainty: confident

# ⚙️ Marker CLI Reference & Command Guide

This document provides an exhaustive reference for **Marker** (`datalab-to/marker`), a deep learning pipeline for converting PDF documents into Markdown, JSON, and HTML. It details every available executable, command-line argument, environment variable, and configuration option found in the repository.

> [!key-claim] **Core Architecture**
> Marker operates not just as an OCR tool but as a full **document layout analysis pipeline**. It employs a cascade of models:
> 1. **Layout Detection**: Identifies columns, headers, and reading order (using Surya).
> 2. **Character Recognition**: Extracts text via OCR (Surya or Tesseract) only when necessary.
> 3. **Formatting**: Reconstructs tables, equations (to LaTeX), and code blocks using heuristic and model-based post-processing.
> 
> 

---

## 📦 Installation & Setup

Before executing commands, ensure Marker is installed. It requires Python 3.9+ and PyTorch.

```bash
# Install via pip
pip install marker-pdf

# Or install from source for the latest experimental features
git clone https://github.com/datalab-to/marker.git
cd marker
pip install -e .

```

> [!warning] **System Dependencies**
> If using `ocrmypdf` or `tesseract` backends instead of the default `surya`, ensure you have the system binaries installed (e.g., `apt-get install tesseract-ocr`).

---

## 🚀 Primary Commands

Marker exposes two primary entry points: `marker_single` for individual files and `marker` for batch processing folders.

### 1. `marker_single` (Single File Conversion)

This is the standard command for converting a specific PDF file.

**Syntax:**

```bash
marker_single [INPUT_FILE] [optional: OUTPUT_DIR] [OPTIONS]

```

#### Core Arguments

| Argument | Type | Description |
| --- | --- | --- |
| `[INPUT_FILE]` | **Positional** | Path to the source PDF, image, or supported document. |
| `--output_dir` | `Path` | Directory to save the output. If omitted, uses `settings.OUTPUT_DIR`. |
| `--output_format` | `String` | Format of the result. Options: `markdown` (default), `json`, `html`, `chunks`. |
| `--page_range` | `String` | Specific pages to process. Format: `"0,5-10,20"` (0-indexed). |
| `--max_pages` | `Int` | Maximum number of pages to process. |
| `--start_page` | `Int` | Page index to start processing from. |
| `--langs` | `String` | Comma-separated list of document languages (e.g., `"English,Spanish"`) for OCR guidance. |

#### Advanced Processing Flags

| Flag | Description |
| --- | --- |
| `--use_llm` | Enables LLM-based post-processing for higher accuracy in tables, forms, and layout. Requires configured backend (e.g., Gemini, OpenAI). |
| `--llm_service` | Specifies the LLM service class. Default: `marker.services.gemini.GoogleGeminiService`. |
| `--force_ocr` | Forces OCR on *all* pages, ignoring embedded text layers. Use for "digital-born" PDFs with corrupt text encoding. |
| `--strip_existing_ocr` | Strips existing OCR text layer and re-runs OCR. Useful for fixing bad legacy OCR. |
| `--redo_inline_math` | Uses the LLM to re-transcribe inline math expressions for higher LaTeX fidelity (requires `--use_llm`). |
| `--paginate_output` | Inserts page delimiters (`\n\n{PAGE_NUMBER}\n\n`) in the output Markdown/Text. |
| `--disable_image_extraction` | Prevents extraction of images from the PDF. If `--use_llm` is on, images are described instead. |
| `--block_correction_prompt` | Custom instruction prompt passed to the LLM for post-processing logic (e.g., "Format all dates as YYYY-MM-DD"). |

#### Debugging & Configuration

| Flag | Description |
| --- | --- |
| `--debug` | Enables verbose logging and saves intermediate debug images/JSONs to a `debug/` folder. |
| `--batch_multiplier` | Multiplier for default batch sizes (default: 2). Increase for faster processing on high-VRAM GPUs; decrease if OOM occurs. |
| `--config_json` | Path to a JSON file containing override settings for the pipeline. |
| `--processors` | Override default processor modules (expert use only). |

---

### 2. `marker` (Batch/Folder Conversion)

Optimized for converting entire directories of documents in parallel.

**Syntax:**

```bash
marker [INPUT_FOLDER] [optional: OUTPUT_FOLDER] [OPTIONS]

```

> [!methodology-and-sources] **Batch Efficiency**
> The `marker` command differs from `marker_single` by managing a worker pool. It loads the model into shared memory (or separate processes depending on configuration) to avoid the overhead of model initialization for every file.

#### Batch-Specific Arguments

| Argument | Type | Description |
| --- | --- | --- |
| `--workers` | `Int` | Number of parallel conversion processes. Default: 1. Scale this based on available VRAM/CPU cores. |
| `--max` | `Int` | Maximum number of files to process from the input directory. |
| `--min_length` | `Int` | Minimum character count required in a PDF to be considered valid for processing. |
| `--metadata_file` | `Path` | Path to a JSON file mapping filenames to metadata (like languages). Format: `{"file.pdf": {"languages": ["English"]}}`. |

*Note: `marker` also accepts most `marker_single` flags (like `--output_format`, `--force_ocr`, `--use_llm`) to apply them globally to the batch.*

---

## 🛠️ Environment Variables & Configuration

Marker relies heavily on environment variables for hardware and backend configuration. These can be set in your shell or in a `local.env` file in the root directory.

### Hardware & Performance

| Variable | Default | Description |
| --- | --- | --- |
| `TORCH_DEVICE` | *(Auto)* | Force specific device (`cuda`, `mps`, `cpu`). |
| `INFERENCE_RAM` | *(Auto)* | VRAM limit per GPU in GB. Set this if using multiple GPUs or if auto-detection fails. |
| `VRAM_PER_TASK` | *(Auto)* | Estimated VRAM usage per task. Tuning this helps the scheduler pack more workers. |
| `OMP_NUM_THREADS` | `1` | Controls CPU threads per worker. Keep low if running many workers on GPU. |

### OCR & Models

| Variable | Default | Description |
| --- | --- | --- |
| `OCR_ENGINE` | `surya` | OCR backend. Options: `surya` (accurate, slow), `ocrmypdf` (fast, requires tesseract), `None`. |
| `OCR_ALL_PAGES` | `false` | Global override to force OCR on every page. |
| `TESSDATA_PREFIX` | *(System)* | Path to Tesseract data folder (required only if using `ocrmypdf` engine). |
| `DEFAULT_LANG` | `English` | Fallback language if detection fails or isn't specified. |

### LLM Integration (If using `--use_llm`)

| Variable | Description |
| --- | --- |
| `GEMINI_API_KEY` | API key for Google Gemini (default backend). |
| `OPENAI_API_KEY` | API key if using OpenAI services. |
| `OPENAI_BASE_URL` | Base URL for OpenAI-compatible endpoints (e.g., vLLM, Ollama). |
| `ANTHROPIC_API_KEY` | API key for Claude integration. |

---

## 🔬 Auxiliary Scripts & Tools

The repository contains additional utility scripts often used for benchmarking or development.

### `benchmark.py`

Compares Marker's performance against reference text or other tools like Nougat.

```bash
python benchmark.py [data/pdfs] [data/references] [report.json] --nougat

```

* `--nougat`: Flag to run Nougat on the same data for comparison.

### `chunk_convert.sh` (Legacy/Helper)

A bash shell wrapper often found in forks or older versions to handle batched chunk processing, though modern usage prefers the `marker` python entry point.

---

## 💡 Usage Examples

### 1. High-Fidelity Research Paper Conversion

Convert a scientific paper, forcing OCR to ensure equations in figures are captured, and outputting to JSON for data analysis.

```bash
marker_single /docs/research_paper.pdf \
  --output_dir ./output \
  --output_format json \
  --force_ocr \
  --langs English

```

### 2. LLM-Enhanced Processing (The "Expert" Mode)

Use Gemini to clean up the output, merge tables across pages, and fix LaTeX formatting.

```bash
export GEMINI_API_KEY="your_key_here"
marker_single contract.pdf \
  --use_llm \
  --redo_inline_math \
  --block_correction_prompt "Ensure all financial tables preserve their exact row/column structure."

```

### 3. Mass Processing on a GPU Cluster

Convert a library of 1000 books using 4 parallel workers on a CUDA device.

```bash
export TORCH_DEVICE=cuda
export INFERENCE_RAM=24  # For a 24GB GPU
marker /library/books ./library_markdown \
  --workers 4 \
  --output_format markdown \
  --min_length 500

```

---

## 🔗 Related Topics for PKB Expansion

1. **[[Surya OCR]]**
* **Connection**: The underlying engine Marker uses for OCR and layout analysis.
* **Depth Potential**: High. Understanding Surya's attention mechanisms explains Marker's layout capabilities.
* **Knowledge Graph Role**: A child node of **Optical Character Recognition** and sibling to **Tesseract**.


2. **[[Retrieval Augmented Generation (RAG)]]**
* **Connection**: Marker is a primary "ingestion" tool for RAG pipelines, converting binary PDFs into semantic chunks.
* **Depth Potential**: Extremely High. Covers chunking strategies, embedding overlap, and metadata preservation.
* **Knowledge Graph Role**: The functional application layer downstream of Marker.


3. **[[PDF Internal Structure]]**
* **Connection**: Explains *why* tools like Marker are necessary (PDF is a print format, not a data format).
* **Depth Potential**: Moderate. Covers PostScript, text streams, and font encoding maps.
* **Knowledge Graph Role**: Foundational theory supporting **Data Extraction**.


4. **[[Layout Analysis Models]]**
* **Connection**: The theoretical class of models (like DiT or LayoutLM) that Marker employs to segment pages.
* **Depth Potential**: High. Involves computer vision and transformer architectures.
* **Knowledge Graph Role**: A technical sub-domain of **Computer Vision**.