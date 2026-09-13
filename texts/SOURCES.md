# Corpus Provenance — every file, where it came from, and how much to trust it

Downloaded 2026-09-13. "Authentic" here means: traceable to a named critical edition or
a maintained scholarly/practitioner corpus — never an anonymous paste site.

## Tier 1 — Critical scholarly editions (highest textual reliability)

### vedas/rigveda/vedaweb-data/  (git clone)
Source: https://github.com/VedaWebProject/vedaweb-data — University of Cologne, VedaWeb project.
The most complete machine-readable Rigveda we found:
- `rigveda/versions/vnh.csv` — van Nooten & Holland metrically restored text
- `rigveda/versions/aufrecht.csv` — Aufrecht 1877 edition
- `rigveda/versions/lubotsky.csv` — Lubotsky's Zurich text
- `rigveda/versions/padapatha.csv` — word-by-word recitation form
- `rigveda/TEI/` — full TEI XML with **accents** (udātta/svarita marked)
- `rigveda/translations/` — Griffith, Macdonell, Müller, Oldenberg (Eng); Geldner, Grassmann (De); Renou (Fr); Elizarenkova (Ru)
- `rigveda/info/stanza_properties.json` — **meter per stanza**
- `rigveda/info/strata.json` — **chronological strata** (Arnold's layers: which hymns are oldest)
- `rigveda/info/addressees.json` — deity per hymn

### GRETIL TEI plaintext (Göttingen Register of Electronic Texts in Indian Languages)
Base: https://gretil.sub.uni-goettingen.de — each file header names its printed critical edition.
- `rigveda_aufrecht_gretil.txt` — Aufrecht 1877 (data entry: van Nooten/Holland)
- `rigveda_padapatha_gretil.txt`, `rigveda_khilani_gretil.txt` (apocryphal RV hymns)
- `samaveda/samaveda_samhita_gretil.txt` — Sāmaveda Samhitā (Kauthuma)
- `atharvaveda/atharvaveda_paippalada_gretil.txt` — Paippalāda recension
- `atharvaveda/atharvaveda_parishishtas_gretil.txt`
- all of `puranas/` (14 major Purāṇas incl. Viṣṇu critical ed., Bhāgavata, Agni, Mārkaṇḍeya, Matsya, Kūrma, Liṅga I, Garuḍa, Nārada, Brahmāṇḍa, Śiva 1&7, Skanda-Revākhaṇḍa, Vāmana, Brahma)
- all of `shastras/` GRETIL files (see below)
Known gaps: GRETIL's `sa_liGgapurANa2` and `sa_skandapurANa1-31` are dead links on their server.

### GRETIL legacy archive (1_sanskr/) — older but same institution
- `atharvaveda_shaunaka_accented_gretil.htm` — **Śaunaka AV with accents**
- `atharvaveda_shaunaka_unaccented_gretil.htm`
- `yajurveda/maitrayani_samhita_accented_gretil.htm` + `_padapatha_` — Maitrāyaṇī Samhitā
- all of `upanishads/*.htm` — 17 files: Aitareya, Bṛhadāraṇyaka, Chāndogya, Īśā, Kaṭha,
  Māṇḍūkya (+ Gauḍapāda Kārikā), Praśna, Śvetāśvatara (accented + plain), Kaivalya, Garbha,
  Atharvaśiras, Nādabindu, Brahmabindu — five of them **with Śaṅkara's bhāṣya**.
  Encoding note: legacy files use combining diacritics; some are Harvard-Kyoto or CSX — check header.

## Tier 2 — Practitioner/community corpora (excellent coverage, editorially active)

### vedas/yajurveda/vishvasa_yajurveda/  (sparse git clone of vishvAsa/vedAH_yajuH)
- `taittirIyam/sArasvata-vibhAgaH/saMhitA/mUlam/` — **Taittirīya Samhitā with full svara marks**
  (vākya-krama and pañcāti-krama arrangements)
- `.../saMhitA/sAyaNaH/` — **Sāyaṇa's commentary** (the classical 14th-c. exegesis)
- `.../saMhitA/bhaTTa-bhAskara-bhAShyam/` — Bhaṭṭa Bhāskara's older commentary
- `.../saMhitA/keith/` — A.B. Keith 1914 English translation (Harvard Oriental Series 18-19)
- `vAjasaneyam/mAdhyandinam/saMhitA/` — Vājasaneyi (Śukla YV) with Uvaṭa & Mahīdhara commentaries

### Sanskrit Wikisource (sa.wikisource.org, MediaWiki API)
- `kena/mundaka/taittiriya/kaushitaki_upanishad_wikisource.txt`
- `ayurveda/sushruta_samhita_wikisource.txt` (2 of 17 subpages failed — near-duplicate chapter ranges)
Community-proofread; verify any load-bearing verse against a printed edition.

## Tier 3 — Historical curiosities (kept for study, NOT as ancient sources)

### shastras/vimana_claims/vaimanika_shastra_sanskrit*
Archive.org scan of the 1973 Sanskrit publication. **Honest provenance**: this text was
produced 1918–1923 by Pandit Subbaraya Shastry (dictated, claimed as channeled revelation
of Bharadvāja); first published 1952/1973 (Josyer). It is NOT an ancient text — no manuscript
older than ~1900 exists. An IISc aeronautics study (Mukunda et al., 1974) found the craft
designs aerodynamically unsound. Kept because studying HOW such texts form is part of the
methodology (see docs/METHODOLOGY.md on separating attested antiquity from legend).

## Audio (sound/audio/)
- `ghanapatha_mayi_medha.mp3` — Ghanapāṭha recitation (archive.org/GhanapathamayiMedha_583)
- `shukla_yv_mangalacharana_kanva.mp3`, `shukla_yv_adhyaya01_kanva.mp3` — complete Śukla YV
  pārāyaṇa in the rare **Kāṇva** śākhā (archive.org/shukla-yajur-veda_recitation)
- `isavasya_upanishad_chant.mp3` — Īśāvāsya chanting (archive.org/rare-vedic-chanting)
For more/better-provenanced audio: vedicheritage.gov.in (IGNCA/Govt of India recordings of
named reciters by śākhā) — next acquisition target.

## Still wanted
- Maitri/Maitrāyaṇīya Upaniṣad (not on Wikisource; exists in vishvAsa repos)
- Sāmaveda with gāna notation (the musical books: Grāmageya/Āraṇyageya gānas)
- Kāṇva Vājasaneyi Samhitā text (we have Mādhyandina text + Kāṇva audio)
- Saṅgīta Ratnākara (music theory), Piṅgala Chandaḥśāstra (prosody/binary math)
- vedicheritage.gov.in audio by śākhā with named reciters
