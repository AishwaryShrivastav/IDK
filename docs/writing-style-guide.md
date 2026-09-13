---
name: ai-slop-detector
description: |
  Detect and eliminate AI writing tells across sentence construction, stance,
  evidence, vocabulary, rhythm, formatting, and endings. Use whenever drafting,
  editing, reviewing, humanizing, or scoring prose: posts, articles, proposals,
  curriculum, newsletters, landing copy, outreach, docs. Also use when text
  "sounds like AI" or "sounds generic", when asked to make writing sound human,
  or when asked for an editorial pass. Trigger even if the user never says "AI
  slop". Covers 31 patterns: negative parallelism, dramatic countdowns, false
  ranges, self-answered questions, filler transitions, tricolon and anaphora
  abuse, superficial -ing analyses, disguised listicles, stakes inflation,
  invented concept labels, false suspense, patronizing analogies, hedging, vague
  and inflated attribution, process narration, excess vocabulary, puffery,
  fragment paragraphs, uniform rhythm, formatting excess, formulaic scaffolding,
  temporal openers, conclusion bloat, tidy resolution.
---

# AI Slop Detector

Two modes.

**Draft mode.** Apply the rules while writing. Nothing more needed than the
pattern list and its fixes.

**Review mode.** Score existing text against the rubric at the end, quote the
sentence that triggered each flag, and propose the rewrite.

Most patterns below are not wrong in isolation. One tricolon is elegant. One
"crucial" is fine. Density is the signal. A cluster of three or more of these in
a short passage is the tell.

---

## PART 1: SENTENCE CONSTRUCTION

### 1. Negative parallelism

The base form is "It's not X, it's Y." Before LLMs, people did not write this at
scale. Four variants, all banned:

- Base: "This isn't just technical, it's a mindset change."
- Causal: "Not because the tool failed, but because nobody read the docs."
- Dismissal: "A rebrand, not a pivot."
- Cross-sentence reframe: "The question isn't whether to optimize. The question
  is when to stop."

The cross-sentence reframe is the most common of the four and the easiest to
miss, because the negation and the correction sit in separate sentences.

**Fix:** State Y directly. Delete the negation of X entirely. If the contrast is
load-bearing, make it a real comparison with both sides argued, not a reveal.

### 2. Not X. Not Y. Just Z.

The dramatic countdown. Two or more negations build a runway before the point.

- "Not ambition. Not ego. Just a person who never learned to say enough."
- "Not broken. Not behind. Just building something with no name yet."

**Fix:** Say the actual thing. Delete the runway.

### 3. False ranges

"From X to Y" implies a spectrum with a meaningful middle. AI uses it to list two
loosely related things. "From innovation to cultural transformation" has nothing
in between.

- "From problem-solving and tool-making to scientific discovery and artistic
  expression."
- "From fundamental physics to medicine and neuroscience."

**Fix:** If there is no real spectrum, write "X and Y."

### 4. Self-answered questions

A question nobody asked, answered in the next breath for drama.

- "The result? Devastating."
- "The scary part? This attack vector is perfect for developers."

**Fix:** Merge into one declarative sentence, or describe what actually happened.

### 5. Filler transitions

Phrases that introduce a point without connecting it to the previous one.

- "It's worth noting that this approach has limitations."
- "Importantly, we must consider the broader implications."
- "Interestingly, this pattern repeats across industries."
- Also: notably, it bears mentioning, furthermore, moreover, additionally.

**Fix:** Delete the phrase and start with the point. If the connection is not
obvious without it, the structure needs work, not a bridge word.

### 6. Tricolon abuse

Rule-of-three, often stretched to four or five. One tricolon is elegant. Three
back to back is a pattern-matching failure.

- "Products solve problems; platforms create worlds. Products scale linearly;
  platforms scale exponentially."
- "Flour, water, salt, time. That's it. That's the whole secret."

**Fix:** Use two items instead of three. Break the rhythm. Three tricolons in
sequence means you have zero.

### 7. Anaphora abuse

The same sentence opening repeated in quick succession.

- "They assume users will pay. They assume developers will build. They assume
  ecosystems will emerge."
- "It wasn't the budget. It wasn't the timeline. It wasn't the team."

**Fix:** State the point once. Combine the examples into a single sentence.

### 8. Superficial -ing analyses

A trailing present participle that attaches significance, legacy, or broader
meaning to a mundane fact. Says nothing.

- "contributing to the region's rich cultural heritage"
- "underscoring its role as a dynamic hub of activity"
- "showcasing how these dishes integrated into the traditional diet"

**Fix:** Delete the phrase. If the analysis matters, give it a sentence with
actual evidence.

### 9. Listicle in a trench coat

A list wearing prose clothing. Each point wrapped in a paragraph opening with an
ordinal.

- "The first step is research. The second is drafting. The third is review."

**Fix:** Either use a real list, or write real prose with real transitions and
reasoning between the points.

---

## PART 2: STANCE AND TONE

### 10. Stakes inflation

Everything is world-historical. An API pricing post becomes a meditation on
civilization.

- "This will fundamentally reshape how we think about everything."
- "will define the next era of computing"
- "This isn't just a presentation. It's the argument you've been building your
  whole career."

**Fix:** Match stakes to subject. A good API is a good API.

### 11. Invented concept labels

Abstract problem-nouns (paradox, trap, creep, divide, vacuum, inversion) welded
to domain words and deployed as if rigorously defined. Names a thing to skip the
argument. Two or more in one piece is a strong signal.

- "the supervision paradox", "the acceleration trap", "workload creep",
  "the complexity divide"

**Fix:** Describe the phenomenon. If it has no established definition, don't name
it like it does.

### 12. False suspense

Announcing a revelation before an unremarkable point.

- "Here's the kicker."
- "Here's where it gets interesting."
- "Here's what most people miss."

**Fix:** Delete the setup. If the point is interesting it needs no announcement.

### 13. Patronizing analogies

Teacher mode by default. Often produces a metaphor less clear than the concept.

- "Think of it as a Swiss Army knife for your workflow."
- "Think of it like a highway system for data."

**Fix:** Explain the actual thing. If a metaphor genuinely beats direct
explanation, use it without the "Think of it as" scaffolding.

### 14. Simplicity assertion

Declaring a point obvious instead of proving it. Includes the privileged-insight
reveal.

- "The reality is simpler and less flattering."
- "The path forward is not complicated."
- "But none of them is the real story. The real story is..."

**Fix:** Make the argument. Let the reader judge whether it's simple.

### 15. Hedging both ways

Presenting every side with equal weight and never landing. Reads as balanced,
functions as evasion.

**Fix:** Commit to a position you would defend under challenge. Name the strongest
objection and answer it, rather than laundering it into a "on the other hand."

---

## PART 3: EVIDENCE AND ATTRIBUTION

### 16. Vague attribution

Claims assigned to unnamed authorities.

- "Experts argue that this approach has drawbacks."
- "Studies show adoption is accelerating."
- "Observers have cited the initiative as a turning point."

**Fix:** Name the person, the study, the number. If you can't, say what you
actually know and flag the gap.

### 17. Source-count inflation

A distinct failure from 16. Presenting one person's view as widely held, or
writing "several publications have cited" when it means two.

**Fix:** Count them. Two is "two." One person's opinion is that person's opinion.

### 18. Process narration

Text that describes the process that produced it instead of stating findings.
Flagged as a recent addition to Wikipedia's field guide.

- "Based on the available information, the company has three subsidiaries."
- "After reviewing the sources, the bridge opened in 1932."
- "Upon closer analysis..."

**Fix:** State the fact. "The bridge opened in 1932." The fact needs no escort.

### 19. Orphan "this"

A sentence opening with "This" and no clear antecedent. "This is important."
This what?

**Fix:** Name the referent, or restructure so the subject is explicit.

---

## PART 4: VOCABULARY

### 20. Excess vocabulary

Kobak et al. analysed 15 million PubMed abstracts and found an unprecedented
post-2022 surge in style words, estimating at least 10% of 2024 abstracts were
LLM-processed. A follow-up PubMed study found 103 of 135 candidate terms rose
meaningfully in 2024, led by "delve", "underscore", "primarily", "meticulous",
and "boast".

Two caveats that matter more than the list:

1. **The list turns over by model generation.** The 2023-2024 markers (delve,
   tapestry, testament, meticulous, intricate) faded through 2025; by mid-2025
   only emphasizing, enhance, highlighting and showcasing survived. A list built
   in 2024 misses recent output and flags old human writing that merely sounds
   formal.
2. **Density is the signal, not the word.** One "delve" means nothing. Fifteen in
   four paragraphs means something. Treat every entry as a hint, never a verdict.

Default-avoid, single justified use acceptable:

delve, underscore, showcase, meticulous, intricate, pivotal, realm, testament,
tapestry, landscape, ecosystem, paradigm, synergy, robust, seamless, leverage,
harness, streamline, crucial, foster, navigate, unlock, boast, align with,
emphasize, enhance, highlight, ever-evolving, game-changer, cutting-edge,
innovative, utilize, underpinnings, commendable.

Transitions: furthermore, moreover, additionally, consequently, notably,
importantly, interestingly, "it's worth noting".

Closers: in summary, in conclusion, overall, ultimately.

**Fix:** Use the plain word. "Field" not "landscape". "Mix" not "tapestry".
"System" not "ecosystem" unless you mean an actual ecosystem.

### 21. Puffery descriptors

Generic, positive, or exaggerated adjectives applied indiscriminately. Regression
to the mean: specific facts smoothed into statements that could describe
anything.

- "a rich and vibrant community"
- "a truly transformative approach"
- "stands as a testament to the enduring spirit of"

**Fix:** Replace the adjective with the fact that earned it. If no fact earns it,
cut the sentence.

---

## PART 5: RHYTHM AND PARAGRAPH

### 22. Fragment paragraphs

Very short sentences or fragments as standalone paragraphs for manufactured
emphasis. RLHF pushed models toward one-thought-per-sentence writing that
requires no mental state-keeping. No one writes first drafts this way.

- "He published this. Openly. In a book. As a priest."
- "The policy changed. No announcement. New terms. Same checkbox."

**Fix:** Combine into real sentences. Let thoughts develop across clauses.
Occasional short sentences are fine; a paragraph of nothing but fragments is a
tell.

### 23. Uniform rhythm

The opposite failure. Paragraphs shaped like rectangles: three sentences, each
15-20 words, each subject-verb-object. Monotonous, statistically safe, and as
diagnostic as any word list.

**Fix:** Deliberately vary. Put a four-word sentence next to a thirty-word one.

### 24. The four-beat progression

AI sentences and paragraphs default to open, expand, contrast, resolve. Every
unit completes its own arc.

**Fix:** Break at least one beat per section. Open on the contrast. Or expand and
stop, without resolving.

---

## PART 6: STRUCTURE AND FORMATTING

### 25. Formatting excess

- Boldface sprayed across a paragraph for emphasis
- Title Case In Headings
- Emoji in headers or bullet points
- Bulleted lists where prose would do

**Fix:** Sentence case headings. Bold only for genuine labels. Lists only when
content is list-shaped.

### 26. Formulaic section scaffolding

Rigid predictable sections that appear regardless of subject: "Challenges",
"Future Prospects", "Key Takeaways", "Benefits and Drawbacks", "Conclusion".

**Fix:** Let the argument determine the sections. If a heading could sit on any
article about any topic, delete it.

### 27. Phrasal templates left unedited

Fill-in-the-blank scaffolding surviving into the output: "[insert example here]",
"as an AI language model", "Certainly! Here's a...", bracketed placeholders.

**Fix:** Proofread the seams.

### 28. Unicode decoration

Arrows, curly quotes, em dashes used as dramatic pauses. Real writers in a text
editor produce straight quotes and ASCII.

- "Input -> Processing -> Output"
- Curly quotes instead of straight ones

**Fix:** Straight quotes, standard ASCII. Write "leads to" instead of an arrow.
Replace dramatic em dashes with a comma or split the sentence.

---

## PART 7: OPENINGS AND ENDINGS

### 29. Temporal openers

Paragraphs or posts opening with temporal generalization instead of the subject.

- "In today's fast-paced landscape..."
- "As we move into 2026..."
- "In an era defined by..."

**Fix:** Open on the specific thing.

### 30. Conclusion bloat and the stated lesson

Two related failures. The summary paragraph that restates what was just said, and
the closing sentence that explains what the point meant.

- "In summary, navigating this space requires..."
- "And that's the real lesson here: sometimes less is more."

**Fix:** Delete both. End on the last substantive point.

### 31. Tidy resolution

Every thread closed, every tension resolved, no loose ends. Human writing leaves
things unfinished. Structural analysis of AI versus pre-AI fiction found tidy
endings among the most reliable discriminators.

**Fix:** Let one tangent go somewhere and not fully resolve. Leave a question you
haven't answered.

---

## REWRITE MOVES

The inversions, applied to AI-shaped text, flipped three of four flagged samples
to reading as human under blind evaluation:

1. Name real things. Swap "studies show" for the actual study.
2. Cut the stated lesson. Delete the sentence explaining what the point meant.
3. Commit to an opinion you would have to defend, instead of hedging both ways.
4. Leave one thread open.
5. Include the one detail only you would know.

---

## SCORING RUBRIC

Score 1-10 per dimension. Quote the sentence that triggered each deduction.

| Dimension | Question |
|-----------|----------|
| Construction | Varied sentences, or negative parallelism, false ranges, self-answered questions, disguised listicles? |
| Stance | Stakes matched to subject, or inflated? Committed, or hedging both ways? |
| Evidence | Named sources and real numbers, or "experts argue" and inflated counts? |
| Vocabulary | Plain and specific, or a cluster of excess-vocabulary markers and puffery? |
| Rhythm | Real variation, or fragment spray and 15-20 word rectangles? |
| Structure | Argument-driven sections, or boilerplate scaffolding and formatting excess? |
| Ending | Ends on substance, or summary bloat, stated lesson, tidy resolution? |

Below 45/70: revise before delivering.
Below 30/70: rewrite rather than edit.

---

## SOURCES

- Wikipedia:Signs of AI writing, WikiProject AI Cleanup. The 15,000-word field
  guide. Source for formatting excess, formulaic scaffolding, puffery, phrasal
  templates, and process narration (the last added via the talk page in 2026).
- Kobak et al., "Delving into ChatGPT usage in academic writing through excess
  vocabulary", 15M PubMed abstracts.
- PubMed follow-up study, 135 candidate terms against 84 controls, 2000-2024.
- isitslop.io on vocabulary turnover by model era and density over word-matching.
- Bloomberry, four-beat sentence progression and temporal-generalization openers.
- StationX structural detector, 30 features scored on 61,608 stories; source for
  the rewrite moves and the tidy-resolution tell.
