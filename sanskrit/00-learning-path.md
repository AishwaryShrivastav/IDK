# Sanskrit, Sound-First: the Learning Path

Most courses teach Sanskrit as a dead written language. We do the opposite, because the
tradition did the opposite: for its first two thousand years the Veda was never written
down; it passed mouth to ear as a sound-object. So we learn it the way the Śikṣāvallī
(in our corpus: `texts/upanishads/taittiriya_upanishad_wikisource.txt`) defines the subject:

> śīkṣāṁ vyākhyāsyāmaḥ — varṇaḥ svaraḥ mātrā balam sāma santānaḥ
> "We shall explain phonetics: phoneme, pitch, duration, force, evenness, continuity."

Those six words are our curriculum.

## Stage 1 — varṇa: the phoneme table (weeks 1–3)

The varṇamālā arranges its sounds by where and how the tongue makes them, so learn it as
a map of the mouth:

| place → | velar (throat) | palatal | retroflex (tongue curled) | dental | labial (lips) |
|---|---|---|---|---|---|
| stop, unvoiced | क ka | च ca | ट ṭa | त ta | प pa |
| + aspiration | ख kha | छ cha | ठ ṭha | थ tha | फ pha |
| stop, voiced | ग ga | ज ja | ड ḍa | द da | ब ba |
| + aspiration | घ gha | झ jha | ढ ḍha | ध dha | भ bha |
| nasal | ङ ṅa | ञ ña | ण ṇa | न na | म ma |

Plus semivowels (य र ल व), sibilants (श ष स), ह, and the vowel system (अ आ इ ई उ ऊ ऋ ॠ ऌ ए ऐ ओ औ).
Every cell is a (place, manner, voice, aspiration) coordinate — a feature system modern
phonology reinvented. **Practice: say each row and feel the contact point move front-ward.**

- Learn Devanagari in parallel (it's phonemic: one symbol, one sound, no spelling ambiguity).
- Learn IAST transliteration (ā ī ū ṛ ṭ ḍ ṇ ś ṣ ṃ ḥ) — our GRETIL files use it.
- Note: GRETIL legacy .htm files sometimes use Harvard-Kyoto (A I U R T D N z S M H) — the
  file header always says which.

## Stage 2 — svara: the pitch accents (weeks 3–5)

Vedic Sanskrit is a pitch-accent language, like ancient Greek or Japanese. Three tones:

- **udātta** — raised pitch. In Devanagari Vedic texts: *unmarked*.
- **anudātta** — lowered pitch. Marked with a horizontal line below: अ॒
- **svarita** — falling glide (high→low). Marked with a vertical line above: अ॑

Open `texts/vedas/yajurveda/vishvasa_yajurveda/taittirIyam/.../mUlam/vAkya-kramaH/1/1.md`:

> इ॒षे त्वो॒र्जे त्वा॑ । (iṣé tvorjé tvā — "Thee for nourishment, thee for strength")

Read it while listening to `sound/audio/shukla_yv_adhyaya01_kanva.mp3`, matching each mark
to the pitch you hear. Accent position changes meaning (the classic case: índra-śatru "having Indra
as slayer" vs indra-śatrú "slayer of Indra"; the demon Vṛtra's fate hinged on which one
the priest said. The tradition itself tells this story of a mispronounced accent destroying
its speaker, at Taittirīya Saṁhitā 2.4.12 and Śatapatha Br. 1.6.3, as a warning).

## Stage 3 — mātrā + chandas: duration and meter (weeks 5–8)

- Vowel duration is quantized: short = 1 mātrā, long = 2, protracted (pluta) = 3.
- Meters are syllable-count frames: **Gāyatrī** 3×8, **Anuṣṭubh** 4×8 (the śloka of all
  later literature), **Triṣṭubh** 4×11 (the Rigveda's favorite), **Jagatī** 4×12.
- Piṅgala's Chandaḥśāstra enumerated all light/heavy syllable patterns with a binary-like
  calculus (~3rd c. BCE) — meter study *was* combinatorics.
- Practice: scan the Gāyatrī mantra (RV 3.62.10): tát savitúr váreṇyaṃ / bhárgo devásya
  dhīmahi / dhíyo yó naḥ pracodáyāt — count 8+8+8.

## Stage 4 — sandhi + the padapāṭha trick (weeks 8–12)

Sanskrit fuses words at boundaries (sandhi): tat + tvam + asi → tattvamasi. This is the #1
reading obstacle, and the tradition solved it for us: the **padapāṭha** editions in our corpus
(rigveda_padapatha_gretil.txt, TS pada files) give every verse pre-split. Read saṁhitā and
padapāṭha side by side and sandhi teaches itself.

## Stage 5 — grammar skeleton (months 3–6)

Just enough morphology to parse, in this order: present verbs (3 persons × 3 numbers) →
noun cases (8 cases × 3 numbers; the endings carry the syntax, which frees the word order) →
participles → the perfect and aorist (Vedic loves them). Pāṇini sits in our corpus
(shastras/language/) as the destination of this path; begin instead with a primer
(recommended: Ruppel, *Cambridge Introduction to Sanskrit*; free alternative: learnsanskrit.org).

## Stage 6 — the reading ladder (start month 2, continue forever)

Ordered by length × difficulty, all in-repo:

1. **Māṇḍūkya Upaniṣad** — 12 verses, prose, about OM itself
2. **Īśā Upaniṣad** — 18 verses (+ we have its chanted audio to follow along)
3. **Gāyatrī** (RV 3.62.10) and **Mahāmṛtyuñjaya** (RV 7.59.12) — single verses, known melodies
4. **Kaṭha Upaniṣad** — the Naciketas death-dialogue, the most beautiful narrative Sanskrit
5. **RV 10.129 Nāsadīya** — 7 verses of the hardest, deepest Sanskrit in existence
6. **RV 1.164 Riddle Hymn** — with Sāyaṇa when stuck
7. **Chāndogya 6** — tat tvam asi in context, with Śaṅkara
8. **Yoga Sūtras** (shastras/yoga/) — crisp aphoristic Sanskrit, 195 sūtras

## Tools

- Dictionary: Monier-Williams online (sanskrit-lexicon.uni-koeln.de — same Cologne team as VedaWeb)
- Morphological analysis: sanskrit.inria.fr (Heritage reader) — paste any sentence, get parse
- Our own corpus grep: every text is plaintext — `grep -r "tattvamasi" texts/` works.
