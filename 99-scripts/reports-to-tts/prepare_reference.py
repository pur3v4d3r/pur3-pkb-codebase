"""prepare_reference.py — Convert MP3 voice samples into XTTS-ready WAV references.

XTTS-v2 expects a clean mono WAV reference clip, ideally 6–15 seconds long at
22050 Hz. This script:
    1. Converts each MP3 in samples/ to a 22050 Hz mono WAV.
    2. Normalizes peak amplitude to -1 dBFS to even out clip loudness.
    3. Builds a `reference_combined.wav` from the two cleanest mid-length clips
       (concatenated with 200 ms of silence between) so XTTS gets richer
       prosody coverage in a single reference.

Run:
    python prepare_reference.py            # writes WAVs into samples/_prepared/
    python prepare_reference.py --overwrite

Outputs:
    samples/_prepared/<stem>.wav           # one per source MP3
    samples/_prepared/reference_combined.wav

After running, point XTTS at any of the WAVs:
    python reports_to_tts.py REPORTS_DIR \\
        --backend xtts \\
        --speaker-wav samples/_prepared/reference_combined.wav \\
        --output-dir _audio
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from pydub import AudioSegment
from pydub.effects import normalize
from pydub.utils import which as _pydub_which

# On Windows, subprocess.Popen does not search PATH for bare program names,
# so we resolve ffmpeg/ffprobe to absolute paths and pin them on AudioSegment.
_FFMPEG = _pydub_which("ffmpeg")
_FFPROBE = _pydub_which("ffprobe")
if _FFMPEG:
    AudioSegment.converter = _FFMPEG
if _FFPROBE:
    AudioSegment.ffprobe = _FFPROBE

logger = logging.getLogger(__name__)

TARGET_SR = 22050
TARGET_CHANNELS = 1
HEADROOM_DB = 1.0
GAP_MS = 200


def convert_clip(src: Path, dst: Path) -> AudioSegment:
    """Convert a single MP3 to mono 22.05 kHz, normalize, write WAV.

    Returns:
        The processed AudioSegment (so callers can reuse it for combining).
    """
    seg = AudioSegment.from_file(src)
    seg = seg.set_frame_rate(TARGET_SR).set_channels(TARGET_CHANNELS)
    seg = normalize(seg, headroom=HEADROOM_DB)
    dst.parent.mkdir(parents=True, exist_ok=True)
    seg.export(dst, format="wav")
    logger.info("wrote %s  (%.2fs)", dst.name, seg.duration_seconds)
    return seg


def build_combined(segments: list[tuple[Path, AudioSegment]], dst: Path) -> None:
    """Concatenate the 2 best mid-length clips into a single richer reference."""
    if len(segments) < 2:
        logger.warning("need >=2 clips to build combined reference; skipping")
        return
    # Pick the two longest under 12s, or the two shortest over 6s — i.e. the
    # cleanest mid-length pair. Sort by duration, take middle two.
    by_len = sorted(segments, key=lambda t: t[1].duration_seconds)
    chosen = by_len[len(by_len) // 2 - 1 : len(by_len) // 2 + 1]
    silence = AudioSegment.silent(duration=GAP_MS, frame_rate=TARGET_SR)
    combined = chosen[0][1] + silence + chosen[1][1]
    combined.export(dst, format="wav")
    logger.info(
        "wrote %s  (%.2fs from %s + %s)",
        dst.name,
        combined.duration_seconds,
        chosen[0][0].name,
        chosen[1][0].name,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="prepare_reference",
        description="Convert MP3 voice samples to XTTS-ready WAV references.",
    )
    parser.add_argument(
        "--samples-dir",
        type=Path,
        default=Path(__file__).parent / "samples",
        help="Directory containing source MP3 samples (default: ./samples)",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Output directory for WAVs (default: <samples-dir>/_prepared)",
    )
    parser.add_argument(
        "--overwrite", action="store_true", help="Overwrite existing WAV outputs"
    )
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Increase verbosity"
    )
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose >= 2 else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    samples_dir: Path = args.samples_dir
    out_dir: Path = args.out_dir or (samples_dir / "_prepared")

    if not samples_dir.is_dir():
        logger.error("samples directory not found: %s", samples_dir)
        return 2

    mp3s = sorted(samples_dir.glob("*.mp3"))
    if not mp3s:
        logger.error("no MP3 files found in %s", samples_dir)
        return 4

    processed: list[tuple[Path, AudioSegment]] = []
    for src in mp3s:
        # Truncate the absurdly long YouTube-style filenames into stable stems.
        stem = src.stem[:60].rstrip("-_")
        dst = out_dir / f"{stem}.wav"
        if dst.exists() and not args.overwrite:
            logger.info("skip existing %s (use --overwrite to replace)", dst.name)
            seg = AudioSegment.from_file(dst)
            processed.append((src, seg))
            continue
        seg = convert_clip(src, dst)
        processed.append((src, seg))

    combined_dst = out_dir / "reference_combined.wav"
    if combined_dst.exists() and not args.overwrite:
        logger.info("skip existing %s (use --overwrite to replace)", combined_dst.name)
    else:
        build_combined(processed, combined_dst)

    print(f"\nPrepared {len(processed)} reference clip(s) in: {out_dir}")
    print("Best single reference:  pick the cleanest 6–10s clip from above")
    print(f"Richer combined reference:  {combined_dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
