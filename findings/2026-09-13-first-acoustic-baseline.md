# Finding 001 — Acoustic baseline of four recitations: the narrow-band signature

**Date**: 2026-09-13 · **Status**: supported (n=4, needs more reciters)
**Data**: sound/analysis/output/*/summary.json · **Code**: sound/analysis/analyze_recitation.py

## Claim
Vedic recitation occupies an extremely narrow pitch band — the 10th-to-90th percentile of
F0 spans only **2.0–2.7 semitones** in all four samples — consistent with the traditional
description of svara as a small set of discrete adjacent tone levels rather than melodic
singing or free speech prosody.

## Evidence

| recording | tradition | F0 median | p10–p90 range | syl/s |
|---|---|---|---|---|
| ghanapatha_mayi_medha | Ghanapāṭha (KYV style) | 181.8 Hz | 2.29 st | 3.02 |
| shukla_yv_mangalacharana | Śukla YV Kāṇva | 179.8 Hz | 2.26 st | 2.78 |
| shukla_yv_adhyaya01 | Śukla YV Kāṇva | 183.9 Hz | 2.70 st | 2.92 |
| isavasya_upanishad_chant | Upaniṣad pārāyaṇa | 148.1 Hz | 2.04 st | 2.81 |

For contrast, conversational speech and song span far wider bands (order of 6-12 st for
speech, over an octave for song) — but these comparison figures need a named reference
before this finding is citable; treat them as ballpark. Note also the tight syllable-rate
clustering (2.8-3.0/s) across different reciters: recitation tempo may itself be a
transmitted parameter rather than a personal one.

## Interpretation (cautious)
The Prātiśākhya/Śikṣā literature describes accent as three relative tone levels. A ~2.3 st
working band with a median near 180 Hz would place the levels roughly a whole tone apart,
which fits the re-ga-sa description of recitation tone often given for living traditions
(named source still needed). We have not yet verified three discrete modes; that requires
accent-labeled segments (Experiment 2 in sound/00-sound-framework.md).

## Open questions
1. Is the F0 distribution trimodal (three accent levels) or continuous?
2. Is the ~1-semitone gap between the Adhyāya-1 reciter and the Ghanapāṭha reciter's *band
   width* meaningful, or personal style?
3. Absolute pitch differs (148 vs 182 Hz median) — consistent with accent being purely
   relative. More samples would make this a publishable observation about the tradition.
4. Isavasya file has voiced_fraction 0.52 (vs 0.86-0.91) — likely contains silence/gaps or
   group recitation; segment before comparing.
