# Starter Prompts for PKB Pipeline Agent

> [!abstract] How to Use
> Copy one of the prompts below and paste it into GitHub Copilot Chat (or Claude Code) to start the pipeline agent. Each prompt covers a different use case.

---

## 1. Full Pipeline Run (Most Common)

Use this when you want to process all existing extraction batches through the full pipeline:

```
Run the PKB Report Extraction → Permanent Notes pipeline.

1. Activate the Python venv: source ".venv/Scripts/activate"
2. cd to "D:/10_pur3v4d3r's-vault"
3. First, do a DRY RUN of the full pipeline:
   python 99-scripts/report-extraction-to-permanent-notes-building/pipeline_v2.py --verbose
4. Show me the results and confirm before executing.
5. When I confirm, run:
   python 99-scripts/report-extraction-to-permanent-notes-building/pipeline_v2.py --execute --auto-commit --verbose
6. After completion, read the pipeline report from the _pipeline-output folder and give me a summary of all changes.

Read the agent prompt at: 99-scripts/report-extraction-to-permanent-notes-building/AGENT-PROMPT.md for full execution protocol details.
```

---

## 2. Extract New Reports + Full Pipeline

Use this when you have new report files that need to be extracted first:

```
Run the full PKB pipeline including extraction of new reports.

1. Activate the Python venv: source ".venv/Scripts/activate"
2. cd to "D:/10_pur3v4d3r's-vault"
3. First, extract the new reports:
   python 99-scripts/pkb_extractor.py --input "<REPORT_FOLDER_PATH>" --output "999-report-orginizing/_extractor-output/<BATCH_NAME>" --recursive
4. Then run the full pipeline:
   python 99-scripts/report-extraction-to-permanent-notes-building/pipeline_v2.py --execute --auto-commit --verbose
5. Show me the summary of all changes.

Replace <REPORT_FOLDER_PATH> with the actual path and <BATCH_NAME> with a descriptive name like "2026-03-20-new-batch".

Read: 99-scripts/report-extraction-to-permanent-notes-building/AGENT-PROMPT.md
```

---

## 3. Update Existing Notes Only (No New Notes)

Use this to just merge new content into existing permanent notes without creating new ones:

```
Run the PKB pipeline in UPDATE-ONLY mode.

1. Activate venv: source ".venv/Scripts/activate"
2. cd "D:/10_pur3v4d3r's-vault"
3. Dry run first:
   python 99-scripts/report-extraction-to-permanent-notes-building/pipeline_v2.py --to-stage 2 --verbose
4. Show me results and confirm.
5. Execute:
   python 99-scripts/report-extraction-to-permanent-notes-building/pipeline.py --update-only --execute --verbose
6. Then run audit + commit:
   python 99-scripts/report-extraction-to-permanent-notes-building/pipeline_v2.py --execute --auto-commit --from-stage 6 --verbose
7. Show summary.

Read: 99-scripts/report-extraction-to-permanent-notes-building/AGENT-PROMPT.md
```

---

## 4. Audit + Fix Links Only (No Note Building)

Use this to just audit and fix wiki-links without creating or updating notes:

```
Run the PKB pipeline for wiki-link resolution and audit only.

1. Activate venv: source ".venv/Scripts/activate"
2. cd "D:/10_pur3v4d3r's-vault"
3. Run stages 4-8:
   python 99-scripts/report-extraction-to-permanent-notes-building/pipeline_v2.py --execute --auto-commit --from-stage 4 --to-stage 8 --verbose
4. Show me the audit results and link resolution stats.

Read: 99-scripts/report-extraction-to-permanent-notes-building/AGENT-PROMPT.md
```

---

## 5. Quick Audit (Read-Only)

Use this to just check the health of your permanent notes without changing anything:

```
Run a read-only audit of my PKB permanent notes.

1. Activate venv: source ".venv/Scripts/activate"
2. cd "D:/10_pur3v4d3r's-vault"
3. Run:
   python 99-scripts/report-extraction-to-permanent-notes-building/audit_notes.py --markdown --notes-dir="999-report-orginizing/_permanent-notes/_permanent-notes" --top=50
4. Show me the resolution rate, orphan count, and top missing concepts.
```

---

## 6. Stage-by-Stage (Maximum Control)

Use this when you want to approve each stage individually:

```
Run the PKB pipeline stage by stage. After each stage, show me the results and wait for my confirmation before running the next one.

1. Activate venv: source ".venv/Scripts/activate"
2. cd "D:/10_pur3v4d3r's-vault"

Run each stage with: python 99-scripts/report-extraction-to-permanent-notes-building/pipeline_v2.py --execute --stage N --verbose
where N is the stage number (0-9).

Start with stage 0 (pre-flight) and work through to stage 9 (git commit).

Stages:
0. Pre-flight checks
1. Extraction (skip if no new reports)
2. Build notes (scan/match/update/create)
3. Generate stubs
4. Resolve report wiki-links
5. Normalise wiki-links
6. Audit
7. Update index
8. Generate change report
9. Git commit

Read: 99-scripts/report-extraction-to-permanent-notes-building/AGENT-PROMPT.md
```
