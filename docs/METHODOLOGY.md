# How we unravel: the IDK method

The goal, stated plainly: read these texts the way their authors meant them to be received,
with every modern instrument we have, and find out what they actually knew. The internet
overstates it in some places and understates it in others; primary sources settle it.

## 1. The tradition already built the toolkit

The Vedas come packaged with six auxiliary sciences (Vedāṅgas) whose entire purpose is
"how to correctly receive this knowledge." We use them as our syllabus, pairing each with
its modern counterpart:

| Vedāṅga | What it does | Our text (in repo) | Modern counterpart we add |
|---|---|---|---|
| Śikṣā | phonetics — exact articulation, pitch, duration | Taittirīya Up. Śikṣāvallī | acoustic analysis (sound/) |
| Chandas | meter — syllable-count patterns | VedaWeb stanza_properties.json | statistical prosody, Piṅgala's binary math |
| Vyākaraṇa | grammar | Pāṇini's Aṣṭādhyāyī (shastras/language/) | computational parsing |
| Nirukta | etymology — why a word means what it means | Yāska's Nirukta (shastras/language/) | historical linguistics, comparative IE |
| Kalpa | ritual context | Śulba Sūtras (the geometry of altars) | history of mathematics |
| Jyotiṣa | timekeeping | Vedāṅga Jyotiṣa, Sūrya Siddhānta | archaeoastronomy — datable sky references |

The first row of that table carries the project. The tradition holds that the Veda is
primarily sound, and it built a phonetic science around that conviction a millennium before
any other culture had one. Taking that literally, with spectrograms, is reading the text
on its own terms.

## 2. The layered reading protocol (per text)

Never read a verse "flat." Every passage gets six passes:

1. **Sound** — recite/hear it. Note accents (udātta ‸ anudātta ॒ svarita ॑), meter, pauses.
2. **Words** — padapāṭha (we have it for RV and TS): the tradition's own word-segmentation,
   undoing sandhi. Then Nirukta-style etymology of key terms.
3. **Grammar** — parse morphology; note archaic forms (they date the passage).
4. **Context** — where does it sit? Which ritual, which deity, which śākhā, which stratum
   (VedaWeb strata.json tells us if a RV hymn is early or late).
5. **Commentary** — what did Sāyaṇa (14th c.), Śaṅkara (8th c.), Bhaṭṭa Bhāskara, Uvaṭa,
   Mahīdhara say? We have all of these in-repo. They disagree; the disagreements are data.
6. **Meaning-levels** — the tradition reads three registers at once: ādhibhautika (physical/
   natural), ādhidaivika (cosmic/divine), ādhyātmika (inner/consciousness). A fire hymn is
   simultaneously about combustion, about the sun, and about awareness. Most "hidden meaning"
   claims are just someone discovering register 2 or 3 exists.

## 3. The claims ledger — how we keep ourselves honest

Every "the ancients knew X" claim gets a row in `docs/CLAIMS.md` with:
- **The primary passage** (book.chapter.verse in our corpus; no secondhand quotes)
- **Earliest attestation** (manuscript/edition date; this alone kills most myths)
- **What it actually says** (our own translation from Sanskrit, not a paraphrase)
- **Verdict**: `attested-astonishing` / `plausible-reading` / `retrofitted` / `modern-fabrication`

Both failure modes are real:
- **Dismissing too much**: writing off Piṅgala's binary enumeration of meters (~3rd c. BCE),
  Pāṇini's generative grammar (a formal system computer science rediscovered in the 1950s;
  Backus-Naur form is structurally Pāṇinian), Yajurvedic altar geometry containing the
  Pythagorean relation (Śulba Sūtras, pre-Pythagoras), Kerala-school infinite series for π
  and sine (Mādhava, ~1400, centuries before Newton/Leibniz), Suśruta's surgical protocols,
  wootz/ukku crucible steel that Europe couldn't replicate until the 19th century, and the
  oral transmission system itself: ghana-pāṭha is an error-correcting code (interleaved
  redundant permutations) that preserved the Rigveda's pitch accents for 3000+ years with
  fidelity written transmission cannot match. These are real, primary-source-verifiable, and
  each one is in our corpus.
- **Believing too much**: the Vaimānika Śāstra (in repo, Tier 3) was dictated 1918–1923 by
  Subbaraya Shastry as channeled revelation; the 1974 IISc aeronautics analysis found its
  craft unflyable. "German scientists built secret tech from the Vedas" is legend, and the
  documented German story is bigger than it: a century of German Indology (Müller, Grassmann,
  Aufrecht; two of our five Rigveda editions are German), Schopenhauer calling the Upanishads
  "the consolation of my life," Schrödinger explicitly framing his view of consciousness in
  Vedantic terms (tat tvam asi, in *What is Life?*), Oppenheimer quoting the Gītā at Trinity,
  Tesla adopting ākāśa/prāṇa terminology after meeting Vivekananda. The influence on
  physicists is documented; the secret vimana labs are fiction. The ledger lets us keep
  the first without the second.

The rule of thumb that settles most cases: date the earliest physical attestation, then
read the primary passage yourself. Myths live in the gap between paraphrase and source.

## 4. The research loop

```
pick a target (hymn, sūkta, claim, sound pattern)
  → six-pass reading (above)
  → compute what can be computed (meter stats, accent contours, concordance, strata)
  → check every commentary we hold
  → write findings to findings/YYYY-MM-DD-<topic>.md   (claim → evidence → open questions)
  → each finding generates the next target
```

Findings accumulate in `findings/`; open questions are the fuel. Every claim there is
marked attested, supported, or open.

## 5. Where the deep meanings actually live (first targets)

1. **RV 10.129 (Nāsadīya Sūkta)** — creation from neither-being-nor-nonbeing; ends in
   deliberate epistemic humility ("perhaps even He does not know"). The project's namesake: IDK.
2. **RV 1.164 (the Riddle Hymn)** — asks *where speech itself lives*; says speech has four
   quarters and humans speak only the fourth. This is the seed of all later sound-metaphysics.
3. **Māṇḍūkya Upaniṣad + Gauḍapāda** — 12 verses mapping OM's phonemes (a-u-m-silence) to
   states of consciousness (waking, dream, deep sleep, turīya). The densest text we own.
4. **Taittirīya Up. Śikṣāvallī** — the tradition defining its own sound-science.
5. **Chāndogya 6 (tat tvam asi)** with Śaṅkara — the identity teaching Schrödinger cited.
6. **Sāmaveda vs. its RV sources** — what exactly does melody *add* to a verse? (First
   computational study: we have both texts.)

## 6. Division of labor

- **Human (you)**: learn the sounds and script (sanskrit/ path), recite, choose targets,
  judge meanings — meaning is not delegable.
- **AI (me)**: bulk philology — concordances, parsing, meter statistics, accent extraction
  from audio, cross-referencing commentaries, drafting finding documents for your review.
- **Neither of us**: accept a claim whose primary source we haven't read.
