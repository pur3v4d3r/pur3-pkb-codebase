# reports_to_tts — Academic-Reports → Audio Pipeline

Converts your Obsidian-flavored academic markdown reports into spoken-audio
files via a pluggable TTS backend.

## Installation

```bash
# Universal deps (always required)
pip install pydub mutagen

# Plus ffmpeg on PATH:
#   Windows: scoop install ffmpeg   |  choco install ffmpeg
#   macOS:   brew install ffmpeg
#   Linux:   apt install ffmpeg     |  dnf install ffmpeg

# Pick ONE (or more) backend:
pip install edge-tts                # default — free, no key, MP3 output
pip install kokoro soundfile        # local GPU, fast, high quality
pip install TTS                     # Coqui XTTS-v2 — voice cloning
```

## Basic usage

```bash
# Single report → ./report.mp3
python reports_to_tts.py path/to/report.md

# Whole folder → side-by-side .mp3 next to each .md
python reports_to_tts.py path/to/reports/

# Whole folder → all audio files into one output dir
python reports_to_tts.py path/to/reports/ --output-dir ./_audio
```

## Common modes

| Goal | Command |
| --- | --- |
| Default (Edge, Aria, MP3) | `python reports_to_tts.py reports/` |
| Slower delivery | `python reports_to_tts.py reports/ --rate -10` |
| Different Edge voice | `python reports_to_tts.py reports/ --voice en-US-JennyNeural` |
| Local GPU (Kokoro) | `python reports_to_tts.py reports/ --backend kokoro --voice af_bella` |
| Voice-clone (XTTS) | `python reports_to_tts.py r.md --backend xtts --speaker-wav voice_ref.wav` |
| WAV instead of MP3 | `python reports_to_tts.py r.md --format wav` |
| Replace existing audio | `python reports_to_tts.py reports/ --overwrite` |
| Preview chunking only | `python reports_to_tts.py reports/ --dry-run -vv` |

## Hitting the husky-alto voice goal

> *Husky, lived-in female voice, lower register. Rich alto with noticeable
> gravel and vocal fry on sustained vowels. Thirties, American, conversational
> and warm. Speaks unhurriedly with a slight smile in the tone.*

| Backend | Closest match | Notes |
| --- | --- | --- |
| `edge` (default) | `en-US-AriaNeural` at `--rate -10` | Warm, conversational alto. Lacks gravel/fry. Good baseline. |
| `edge` alt | `en-US-AvaMultilingualNeural` | Slightly lower, similarly warm. |
| `kokoro` | `af_bella` | Rich alto. Slightly more polished than husky. |
| `xtts` ★ | Reference-clip cloning via `--speaker-wav voice.wav` | The only realistic path to actually capture *husky + gravel + fry*. Provide a 6-15 s clean clip of the target voice. |

## Voice IDs (full lists)

```bash
# Edge — list all neural voices:
edge-tts --list-voices

# Kokoro — voicebank prefixes: a*=American f, am*=American m, b*=British f, bm*=British m
# Common picks: af_bella, af_heart, af_sarah, am_adam
```

## Configuration

| Option | Default | Description |
| --- | --- | --- |
| `--backend` | `edge` | `edge` \| `kokoro` \| `xtts` |
| `--voice` | per-backend default | Backend-specific voice ID |
| `--speaker-wav` | — | XTTS reference clip for cloning |
| `--rate` | `0` | Percent adjust (e.g. `-10` = 10% slower) |
| `--pitch` | `0` | Hz adjust (Edge only) |
| `--format` | `mp3` | `mp3` \| `wav` \| `ogg` |
| `--chunk-chars` | per-backend | Per-request character ceiling |
| `--output-dir` | next to input | Where to write audio |
| `--overwrite` | off | Replace existing audio files |
| `--strict` | off | Non-zero exit if any report fails |

## Exit codes

| Code | Meaning |
| --- | --- |
| 0 | All reports succeeded (or were skipped because output existed) |
| 1 | Uncaught error |
| 2 | Input path does not exist |
| 3 | Bad CLI argument value |
| 4 | No `.md` files found under the input |
| 5 | Required dependency missing (pydub / ffmpeg) |
| 6 | Selected backend not installed |
| 7 | At least one report failed and `--strict` was set |
| 130 | Interrupted (Ctrl+C) |

## What gets stripped from the markdown

- YAML frontmatter (parsed for `title`, `author`, then dropped)
- Fenced & inline code blocks (not spoken)
- HTML tags
- Image references (`![]()`)
- Link URLs (`[text](url)` → "text"; `[[Target|Display]]` → "Display")
- Emphasis markers (`**`, `*`, `_`, `~~`)
- Markdown table dividers (`---|---`)
- Horizontal rules
- Blockquote markers and list bullets

Headings become natural section pauses (~700 ms) with the heading text spoken;
sentence breaks within a section get a shorter pause (~250 ms).

## Tests

```bash
pip install pytest
pytest test_reports_to_tts.py -v
```

The test suite covers markdown cleaning, chunking, frontmatter parsing, the
backend factory's error path, and a stubbed end-to-end synthesis flow. Live
backend calls are not tested — they require external services or large
local models.

## Integration

### As a library

```python
from reports_to_tts import (
    load_report, build_backend, BackendConfig, synthesize_report,
)
from pathlib import Path

backend = build_backend("edge", BackendConfig(voice="en-US-AriaNeural", rate_pct=-10))
report = load_report(Path("report.md"))
result = synthesize_report(
    report, backend,
    out_dir=Path("./_audio"),
    out_format="mp3",
    chunk_chars=4000,
    overwrite=False,
    dry_run=False,
)
print(result.output_path, result.duration_ms)
```

### As a scheduled job

Run nightly to synthesize any new reports:

```bash
# Windows Task Scheduler — daily 02:00
python D:\10_pur3v4d3r's-vault\99-scripts\reports-to-tts\reports_to_tts.py ^
  D:\10_pur3v4d3r's-vault\999-report-organizing\__pur3v4d3r-house-voice-reports ^
  --output-dir D:\10_pur3v4d3r's-vault\999-report-organizing\_audio ^
  --backend edge --voice en-US-AriaNeural --rate -10 -v
```
