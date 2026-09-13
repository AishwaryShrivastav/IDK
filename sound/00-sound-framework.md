# The Sound Framework: what recitation audio can actually tell us

You asked: *what information can we get from sound — frequency, patterns, language, pitch,
effects on other things?* Here is the full inventory, split into (A) what the tradition
itself encodes in sound, (B) what signal processing can measure, (C) what effects are
scientifically testable, and (D) what to treat with suspicion.

## A. What the tradition encodes in sound (the "protocol layer")

The pāṭha system is an error-correcting code implemented in human memory:

| pāṭha (recitation mode) | pattern for words 1,2,3… | function |
|---|---|---|
| saṁhitā | 1 2 3 4 (fused, natural) | the message |
| pada | 1 / 2 / 3 / 4 (each word isolated) | word-boundary checksum |
| krama | 12 23 34 | adjacency checksum |
| jaṭā | 12 21 12 / 23 32 23 | forward-reverse interleave |
| **ghana** | 12 21 123 321 123 / 23 32 234… | full permutation redundancy |

`audio/ghanapatha_mayi_medha.mp3` is a live specimen. Any single memory error becomes
inconsistent across modes and is caught. This is why the Rigveda's pitch accents, a level
of phonetic detail most living languages have lost, survived 3000+ years of oral-only
transmission. Measuring the fidelity of this channel is our first original research
target: compare the same verse across reciters and regions, quantify the drift.

On top of accents, the Sāmaveda converts Rigvedic verses into **melody** (sāman): pitch
becomes musical contour, syllables stretch (stobha insertions: hāu, hoyi…). Sāma chant is
the documented ancestor of Indian classical music's svara system.

## B. What we can measure from the audio files (sound/analysis/)

1. **F0 / pitch contour** (fundamental frequency, Hz) — the direct acoustic correlate of
   udātta/anudātta/svarita. Testable: do the three accents form discrete pitch levels? What
   interval separates them? (Descriptions of surviving practice suggest roughly 2-4
   semitones, but we have not yet pinned a named study; open item.) Is svarita really
   a fall, a high-to-low glide, as Pāṇini describes?
2. **Duration** — is mātrā really quantized 1:2:3 (short:long:pluta)? Measure vowel lengths;
   plot the histogram; look for the predicted three modes.
3. **Rhythm/meter** — onset detection → syllable timing → does acoustic rhythm match the
   chandas (8/11/12-syllable pāda structure)? Where do reciters breathe vs. where the
   danda (।) marks say to pause?
4. **Formants (F1/F2)** — vowel quality; lets us check whether a reciter's "a" is the
   Śikṣā-prescribed saṁvṛta (closed) sound, and compare śākhā pronunciation traditions
   (e.g. Kāṇva vs Mādhyandina treatment of ḷ/ḍ).
5. **Spectral features** — harmonic structure, nasality (anusvāra/anunāsika realization),
   the visarga's breath signature.
6. **Intensity envelope** — the Śikṣāvallī's *balam* (force) parameter.
7. **Cross-reciter statistics** — transmission fidelity as a measurable quantity. Same
   verse, different lineages, different centuries of separation: how many cents of pitch
   drift, how many milliseconds of timing drift?

The working analyzer is `analysis/analyze_recitation.py` (pure numpy/scipy; ffmpeg decodes).
It produces per-file: F0 track, spectrogram, energy envelope, syllable-rate estimate, and a
summary JSON. Outputs land in `analysis/output/`.

## C. Effects on other things — what is actually testable

- **On the reciter/listener (physiology)**: peer-reviewed studies exist on chanting and slow
  breathing — OM chanting at ~5-6 breaths/min drives heart-rate variability and baroreflex
  effects (slow-breathing literature, e.g. Bernardi et al. 2001 on mantra/rosary and HRV);
  fMRI work (Kalyani et al. 2011) reported limbic deactivation during OM chanting. Recitation
  is also a breath-control protocol — measurable, real, and underexplored.
- **On rooms (acoustics)**: chanting in stone temples excites room modes; resonance at
  specific F0s is physics, measurable with a sweep + impulse response.
- **On matter (cymatics)**: sound creates standing-wave patterns in media (Chladni
  figures) — the *pattern-formation* is real physics. The claim that Sanskrit phonemes make
  *special or meaningful* patterns (e.g. "OM draws a Sri Yantra") is not supported; any tone
  makes a pattern determined by frequency and geometry, not language.

## D. Claims to handle with the ledger (docs/METHODOLOGY.md §3)

- "432 Hz is the sacred/Vedic frequency" — no ancient source specifies absolute Hz; Vedic
  accent is *relative* pitch. The śruti system (22 microtones) is relative interval structure.
- "Mantras have inherent physical power independent of any listener" — untestable as stated;
  reframe into testable pieces (physiology, acoustics, attention) and test those.
- Frequency numerology generally: the tradition's own sophistication is about **relations**
  (intervals, ratios, patterns), which is more interesting than magic constants anyway.

## First experiments (in order)

1. Run the analyzer on all four audio files for baseline plots. Done: see analysis/output/
   and findings/2026-09-13-first-acoustic-baseline.md.
2. Segment `shukla_yv_adhyaya01_kanva.mp3` against the Vājasaneyi text; label 20 accents
   by hand; check pitch-level separation → `findings/` note.
3. Mātrā histogram from the Īśāvāsya chant (we have its exact text — 18 verses).
4. Ghanapāṭha structure recovery: can we detect the 12-21-123-321-123 word-repetition
   pattern purely from the audio's self-similarity matrix? (If yes, we have read the
   error-correcting code from the signal alone.)
