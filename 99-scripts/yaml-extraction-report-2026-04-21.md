---
title: "YAML Frontmatter Extraction Report"
doc_type: "extraction-report"
extractor: "yaml"
source: "D:/10_pur3v4d3r's-vault/99-scripts"
file_count: 10
doc_created: 2026-04-21
doc_modified: 2026-04-21
tags:
  - report/extraction
  - extractor/yaml
---

# YAML Frontmatter Extraction Report

## Executive Summary

| Metric | Value |
|---|---|
| Files scanned | 10 |
| Files with frontmatter | 2 |
| Files missing frontmatter | 8 |
| Files with parse errors | 0 |
| Frontmatter coverage | 20.0% |
| Unique field names | 10 |
| YAML parser | PyYAML |

## Field Coverage

| Field | Count | Coverage | Type(s) | Examples |
|---|---|---|---|---|
| `doc_type` | 2 | 100% | string (2) | technical-documentation · reference-note |
| `doc_created` | 2 | 100% | string (2) | 2026-03-12 · 2026-04-21 |
| `tags` | 2 | 100% | array (2) | ['readme', 'documentation', 'python', 'extraction', 'pkb-aut · ['script', 'python', 'pkb-automation', 'wikipedia', 'referen |
| `status` | 2 | 100% | string (2) | evergreen |
| `doc_id` | 1 | 50% | string (1) | readme-pkb-extractor |
| `primary_domain` | 1 | 50% | string (1) | pkb-automation |
| `title` | 1 | 50% | string (1) | Wikipedia Article Downloader — Complete Command Reference |
| `aliases` | 1 | 50% | array (1) | ['Wikipedia Downloader', 'wikipedia_downloader.py', 'Wiki Ar |
| `certainty` | 1 | 50% | string (1) | established |
| `doc_modified` | 1 | 50% | string (1) | 2026-04-21 |

## Value Distributions (low-cardinality fields)

### `doc_type`

| Value | Count |
|---|---|
| technical-documentation | 1 |
| reference-note | 1 |

### `doc_created`

| Value | Count |
|---|---|
| 2026-03-12 | 1 |
| 2026-04-21 | 1 |

## Files Missing Frontmatter

| # | File |
|---|---|
| 1 | [[broken-link-report-2026-03-19.md]] |
| 2 | [[cleanup_strategy.md]] |
| 3 | [[README-folder-review-report.md]] |
| 4 | [[README-generate-frontmatter.md]] |
| 5 | [[README-link-fixer.md]] |
| 6 | [[README-table-of-contents-generator-script-usage-examples.md]] |
| 7 | [[README-vault-indexer.md]] |
| 8 | [[toc-generator-script-README.md]] |

