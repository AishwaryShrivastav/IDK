#!/usr/bin/env python3
"""Baseline acoustic analysis of Vedic recitation audio.

For each input file produces, in analysis/output/<name>/:
  - f0_track.png        pitch contour (autocorrelation tracker, voiced frames only)
  - spectrogram.png     0-4 kHz log-power spectrogram
  - energy.png          RMS energy envelope with estimated syllable onsets
  - summary.json        F0 stats, syllable-rate estimate, duration

Pure numpy/scipy (no librosa); ffmpeg is used to decode mp3 -> mono wav.
Usage: .venv/bin/python analyze_recitation.py ../audio/*.mp3
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy import signal as sps
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

SR = 16000
FRAME = 1024          # 64 ms
HOP = 256             # 16 ms
F0_MIN, F0_MAX = 60.0, 400.0   # male recitation range, generous


def load_mono(path: Path) -> np.ndarray:
    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-i", str(path),
             "-ac", "1", "-ar", str(SR), tmp.name],
            check=True,
        )
        y, sr = sf.read(tmp.name, dtype="float32")
    assert sr == SR
    return y


def frame_signal(y: np.ndarray) -> np.ndarray:
    n = 1 + max(0, (len(y) - FRAME) // HOP)
    idx = np.arange(FRAME)[None, :] + HOP * np.arange(n)[:, None]
    return y[idx] * np.hanning(FRAME)


def f0_autocorr(frames: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return (f0 in Hz, voicing confidence) per frame."""
    lag_min = int(SR / F0_MAX)
    lag_max = int(SR / F0_MIN)
    spec = np.fft.rfft(frames, n=2 * FRAME, axis=1)
    ac = np.fft.irfft(np.abs(spec) ** 2, axis=1)[:, :lag_max + 1]
    ac0 = ac[:, 0] + 1e-12
    acn = ac / ac0[:, None]
    window = acn[:, lag_min:lag_max + 1]
    best = np.argmax(window, axis=1)
    conf = window[np.arange(len(best)), best]
    f0 = SR / (best + lag_min)
    return f0, conf


def analyze(path: Path, outroot: Path) -> dict:
    y = load_mono(path)
    dur = len(y) / SR
    frames = frame_signal(y)
    t = HOP * np.arange(len(frames)) / SR

    rms = np.sqrt((frames ** 2).mean(axis=1))
    db = 20 * np.log10(rms + 1e-9)
    f0, conf = f0_autocorr(frames)
    voiced = (conf > 0.55) & (db > db.max() - 35)
    f0v = np.where(voiced, f0, np.nan)

    # syllable-rate proxy: peaks in the smoothed energy envelope
    env = sps.savgol_filter(rms, 21, 3)
    peaks, _ = sps.find_peaks(env, height=env.max() * 0.15, distance=int(0.12 * SR / HOP))
    syl_rate = len(peaks) / dur

    out = outroot / path.stem
    out.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(14, 4))
    plt.plot(t, f0v, ".", ms=2)
    plt.ylim(F0_MIN, F0_MAX)
    plt.xlabel("time (s)"); plt.ylabel("F0 (Hz)")
    plt.title(f"{path.name} — pitch contour (accent analysis raw material)")
    plt.tight_layout(); plt.savefig(out / "f0_track.png", dpi=110); plt.close()

    fspec, tspec, S = sps.spectrogram(y, SR, nperseg=1024, noverlap=768)
    plt.figure(figsize=(14, 4))
    keep = fspec <= 4000
    plt.pcolormesh(tspec, fspec[keep], 10 * np.log10(S[keep] + 1e-12), shading="auto")
    plt.xlabel("time (s)"); plt.ylabel("Hz")
    plt.title(f"{path.name} — spectrogram")
    plt.tight_layout(); plt.savefig(out / "spectrogram.png", dpi=110); plt.close()

    plt.figure(figsize=(14, 3))
    plt.plot(t, env)
    plt.plot(t[peaks], env[peaks], "x")
    plt.xlabel("time (s)"); plt.ylabel("RMS energy")
    plt.title(f"{path.name} — energy envelope, {len(peaks)} onsets (~{syl_rate:.1f} syl/s)")
    plt.tight_layout(); plt.savefig(out / "energy.png", dpi=110); plt.close()

    fv = f0[voiced]
    summary = {
        "file": path.name,
        "duration_s": round(dur, 2),
        "voiced_fraction": round(float(voiced.mean()), 3),
        "f0_median_hz": round(float(np.median(fv)), 1) if len(fv) else None,
        "f0_p10_hz": round(float(np.percentile(fv, 10)), 1) if len(fv) else None,
        "f0_p90_hz": round(float(np.percentile(fv, 90)), 1) if len(fv) else None,
        "f0_range_semitones": round(float(12 * np.log2(
            np.percentile(fv, 90) / np.percentile(fv, 10))), 2) if len(fv) else None,
        "est_syllable_rate_per_s": round(syl_rate, 2),
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=2))
    return summary


def main() -> None:
    outroot = Path(__file__).parent / "output"
    results = [analyze(Path(a), outroot) for a in sys.argv[1:]]
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
