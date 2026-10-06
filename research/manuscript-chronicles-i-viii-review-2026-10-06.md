# Manuscript Chronicles I-VIII: upload comparison and live-ledger review, 2026-10-06

Scope: Abad's 2026-10-06 upload of the eight manuscript Chronicles (Rebellion, Kanja ages 18-22) and the Voice Progression Sheet. Nothing in `canon-ledger.json`, git, or any existing file was changed by this review, except the appended section in `research/trinity-on-page-census-2026-10-06.md`. No fix below has been applied. Every proposed fix is marked **M** (mechanical: realigns to an already-locked fact, no new fact) or **R** (needs Abad's ruling).

Line numbers are lines of the new repo files in `docs/lords-of-cian/chronicles/`.

## 1. Files added (step 1)

Plain-text extractions were not used. The five chapters were converted straight from the original `.docx` files, paragraph by paragraph, and checked afterwards: every body paragraph of each upload matches the markdown file, in the same order. The only text dropped is the document-metadata block and the duplicated title lines.

| File | Words (body) | Age / phase |
|---|---:|---|
| `chronicle-i-the-scrip-forge-raid.md` | ~9,640 | 18, Phase 1 |
| `chronicle-ii-the-dredge-line-ambush.md` | ~7,890 | 18, Phase 1 |
| `chronicle-iv-iron-shallows.md` | ~6,020 | 19, Phase 1 |
| `chronicle-v-the-siege-of-maw-9.md` | ~7,900 | 20, Phase 1 |
| `chronicle-vii-the-siege-of-the-ghost-harbor.md` | ~5,710 | 21, Phase 2 |

Conventions copied from `chronicle-iii-*.md`: `# Chronicle N: Title`, one italic header note, `---`, body, `• • •` scene dividers. Header notes carry the source file, "Abad's upload, 2026-10-06", the Batch 70 status (I, II, IV, V clean; IV with its one undramatized `ARS-341`/`342` gap; VII needed only `GEO-006`), and the Book 1 gate pointing at the Trinity census.

Three formatting choices, none touching prose:
- Scene and coda headings in I and II (`SCENE 1: ...`, `CODA: THE LEDGER OF ONYX`) are set as `##`, because they are bold headings in the upload.
- Whole-paragraph italics are kept as `*...*` (the Onyx codas of V and VII, the Forge-7 notice text, the closing "End of Chronicle" line). The existing III, VI and VIII files dropped italics; the Onyx codas are identifiable by italics in the upload, so I kept them.
- V keeps the upload's "The Lords of Cian | My Rival's Distance" subtitle line. VII keeps the upload's curly quotes; I, II, IV and V are straight-quoted in the upload. Left as supplied.

## 2. Uploaded III, VI, VIII against the repo versions (step 2)

Method: paragraph-level comparison of the `.docx` text against the repo file body (header note excluded), with typographic quotes normalized for the first pass and compared exactly for the second.

**Result: the uploads are the pre-correction originals. Every text difference is a known Batch 70/71 correction. No later edits by Abad were found in any of the three.** Nothing was applied.

| Chapter | Text differences (all known) |
|---|---|
| III | Hask "fifty-three" -> "fifty-four". Two inserted paragraphs on Halst/Sok/Vos at the western wall (Batch 70). One closing sentence block added to the exit-scene paragraph (Halst/Sok/Vos sitting by the rubble). The upload's metadata block and the duplicate "CHRONICLE III" title line are not in the repo file. |
| VI | Two paragraphs replaced: the Blue-Collar Titan/4,000-worker paragraph (now a Scrip-Forge callback) and "liberated twelve thousand human beings from a quarry" -> "from Maw-9". The upload's metadata block, "CHRONICLE VI", "Age 20" and the "The Lords of Cian | My Rival's Distance" line are not in the repo file. |
| VIII | Two paragraphs replaced: *The Receipt* captured "during a patrol intercept south of the Jicome Strait" -> "during the eleven-week Reef-Chain Blockade ..."; "charcoal rubbings from Killane" -> "from the Scrip-Forge Raid". The upload's metadata block, bold "VIII", "THE ASH-WHARF MASSACRE" and the age subtitle are not in the repo file. |

Formatting-only differences (not text): the repo files drop italics (the upload's VI and VIII codas are whole-paragraph italics, the VIII "ONYX:" label is bold-italic); the upload of VIII uses curly quotes (65 apostrophes, 12 pairs of double quotes) where the repo file uses straight quotes.

One point worth Abad's attention, found while doing this comparison: the three Halst/Sok/Vos paragraphs in repo III are Batch 70 insertions, not Abad's text. Ledger rules cite them as "the manuscript's own locked account" (`MCD-533`, `MCD-641`, `MCD-1137`) and `CC-158`/`159`/`160` say the three "found each other on the docks before finding Kanja". Abad's own III never says that, and his V (L13) opens with the three simply "paired with Trench veterans". V does not contradict the docks account, but it does not support it either. See R-17.

**Voice Progression Sheet:** text-identical to `docs/lords-of-cian/voice/voice-progression-sheet.md`. 97 paragraphs against 97, no word differing. The mirror carries markdown artifacts the docx does not (`###` prefixes on the phase sub-headings, stray `*` after four "What ..." labels). No curly quotes or dashes in either. No update needed.

## 3. Review of I, II, IV, V, VII against the live ledger (step 3)

### 3.1 Mechanical gate results

`python3 scripts/connective_tissue_check.py <file>` on each new file:

| File | Exit | Cited IDs (all locked) | Genuinely new names (rule hits: none) |
|---|---:|---|---|
| I | 0 | none | Oren Tull (assayer), Anvil Street, Phase One/Two (not names) |
| II | 0 | none | Torren Vace, Lock Gate Three/Seven/Twelve, Warehouse Row, Article Fourteen |
| IV | 0 | `ARS-341` (header note) | Ren Voss (also in V), Dock-Row Nine |
| V | 0 | none | Furnace Quarter, Pier Street, Southern Command, Dock-Row Nine, Ren Voss |
| VII | 0 | `GEO-006` (header note) | Port Authority, Southern Naval Command |

The rest of each "NEW" list is sentence-initial words, scene headings, and hyphenated compounds, not names. The script only trims the header note when a file has three or more `---` separators; these files have one, so the header notes were scanned too. That is why `ARS-341` and `GEO-006` are listed. Near-collisions worth a look: **Tomas** (I L213, a dockworker; `MCD-093`/`CC-124` Tomas Grieve, and the project already renamed a "Tomas" at Batch 98 and a "Toma" at Batch 330 for this), **Ren Voss** (Ren Oshaal `CC-138`; Voss in `MAW-101`/`148`, `POL-102`).

Onyx voice check (`scripts/onyx_voice_check.py`). It is tuned to Phase 4 drafts, so the whole-file run is meaningless for these Phase 1-2 chapters: the prose is third-person Kanja by design. I ran it on the coda text alone (I, II, IV, V, VII). Phase 3-4 thresholds ("the Captain" count, Iron/Rust verdicts) do not apply at ages 18-21 and are ignored. Real hits:

| Coda | Hit |
|---|---|
| I (L373) | first person: "I record this. The first entry." |
| II (L399) | first person: "the way I calculate mass" |
| IV (L209) | first person, twice: "I hold no new names ... a word I do not yet possess" |
| II | tense: coda is mostly past ("The column entered ... The soldiers sank"), present-tense count 4 against past 6 |
| V | sentence cadence: fragments 23 percent (threshold 30); full sentences with present-perfect ("It has recorded ...") |
| V, VII | clean on first person ("the blade" throughout) |

No semicolons anywhere in the prose of the five chapters.

### 3.2 Findings, mechanical (M)

**M-1. V: Maret Vos is she/her; `CC-160` locks he/him (Batch 226 ruling, and `MCD-533`/`CC-160`).**
File `chronicle-v-the-siege-of-maw-9.md`, L17, L19, L213. 16 gendered words. Quotes: "Maret Vos was the one who spoke first. She spoke because ..."; "the place where she had been born"; "She emerged from the pipe into the morning light with dust in her hair and the expression of a woman who had walked through the place where she had been born". Corren Halst, Danne Sok, Maren, Breck and Hask are all correct in all five chapters.
Fix: she -> he, her -> his, herself -> himself, "a woman" -> "a man" in those three paragraphs.

**M-2. V: "arena" x8; `VB-050` bans "arena (as venue)" and the Batch 374 precedent replaced it in `MCD-234`.**
L37 (dialogue: "the maintenance tunnel layout beneath the arena floor"), L57, L147 ("perimeter arches of the arena seating"), L149, L155 ("sand-floored arena"), L165, L185, L223.
Fix: "quarry floor" / "the sand floor" / "the tiered seating" as each sentence needs. L155 also calls the facility "a stadium built into the earth"; "stadium" is not on the list but sits in the same family, optional. VII L35 "a natural amphitheater" describes rock, not a venue, and is fine.

**M-3. VII: Breck's call is stated as 26 words and quoted as 30; `CC-119` locks 26.**
L161: "Nineteen feet at the narrows. The reef is volcanic. Sharp edges. Keep the helm two points to starboard past the second warship and hold until the current pulls you clear." (30 words by count). L163 "Twenty-six words", L165 "Hask wrote all twenty-six words", L255 in the Onyx coda "Twenty-six words".
Fix: cut four words from the speech to reach 26 (for example drop "The reef is volcanic."). The count language stays.

**M-4. VII: "A Trust capital ship captured during the Battle of Iron Shallows"; `MCD-235` (amended Batch 349) and `MCD-285` lock "escort warship"/"escort vessel".**
L23. Fix: "escort warship". Related and not mechanical: R-8.

**M-5. IV and V: Sera's age cannot be reached from `CC-117` plus the chapters' own intervals.**
`CC-117`/I L315: Sera is four months old at the Raid. II is three weeks later. III has "the fourth week of scouting" plus "the next two weeks" and Nev Torr "joined after the Dredge-Line", so the Black Trench falls roughly 6 to 10 weeks after the Dredge-Line, about 2 to 3 months after the Raid. IV L7: Iron Shallows is "four months after the Black Trench". V L233 / IV L169: the sidearm is carried "six months" from Iron Shallows to Maw-9.
Result: Sera is about 10 to 11 months at Iron Shallows and about 16 to 17 months at Maw-9.
Quotes: IV L23 "His daughter Sera was eight months old."; V L121 "The child was ten months old now, teething".
Fix: IV "about ten months" (or "nearly a year"); V "a year and a half". The exact words are Abad's to pick, the arithmetic is not in doubt.

**M-6. V: Sephtis calls Kanja at the Black Trench "a twenty-year-old"; `MCD-232`/`CC-119` put the Black Trench at age 19.**
L93: "the Trench was the most dangerous thing I have seen a twenty-year-old survive". Fix: "a nineteen-year-old". (Kanja is 20 at Maw-9, which is where the confusion arises.)

**M-7. Ledger side: `CC-132` (Pell Ostra) is stale against II.**
`CC-132`: "present from the Black Trench onward (age 19) -- no recruitment origin is given in the source material, so none is asserted here." II L103 introduces her at the Dredge-Line (age 18): "a woman named Pell Ostra who had been maintaining the Dredge-Line's lock system for twenty-two years", L141 "grey hair tied back with a cable tie and the face of a woman who had been solving mechanical problems for longer than Kanja had been alive", and she machines the shear-pins, pulls the release cord on Lock Gate Seven (L251), and re-installs the gates (L341).
Fix: amend `CC-132`/`CC-133` to add the Dredge-Line lock-mechanic origin and 22 years of service. The manuscript controls. Nothing in the rule has to be withdrawn.

**M-8. Ledger side: `CC-121` timing.**
`CC-121`: Maren "becomes the fleet's shipwright from Ghost Harbor onward (ages 21-22)". VII L19 has him assessing and refitting the two sardine boats before the siege ("Ribs are good ... Planking needs three days"). Fix: change "from Ghost Harbor onward" to "from the fleet's first acquisitions (age 20-21) onward".

### 3.3 Findings, needing Abad's ruling (R)

**R-1. V: the Maw-9 quarry's builders and age against locked Old Dominion chronology, and Sephtis "watched them build it". (Most load-bearing.)**
Quotes (V): L41 "Old Dominion construction. The builders kept records. The records survived because nobody cares about quarry engineering from two centuries ago."; L57 "drawn in the drafting conventions of the Old Dominion's civil engineering bureau"; L93 Sephtis: "a quarry whose structural engineering I understand better than the men who built it, because I watched them build it"; L115, L169, L203, L171 (two centuries, "Old Dominion engineers who had laid it", "two hundred years").
Conflicts: `WC-020`/`CC-057` (the Old Dominion fell about 5,000 years ago); `MAW-010` (the Maw was created by Anu Un Ra during the Old Dominion, as state infrastructure); `MAW-090`/`MAW-091` (Era III, the Sovereign Trust, is about 2,000 to 300 years ago); `CC-037` (Sephtis is 1,997 years old, so he cannot have watched Old Dominion engineers build anything).
The two readings that fit: (a) Maw-9 is a licensed Era III Maw built about 200 years ago, laid out to Old Dominion pattern plans held by the Trust's engineering bureau, so Sephtis genuinely watched it built and "Old Dominion" becomes "Old Dominion-pattern" in four or five places; or (b) Maw-9 is an Old Dominion-era Maw, the "two centuries" are replaced by a very large figure, and Sephtis's claim is changed to having studied rather than watched. (a) keeps `CC-037` and the chapter's best line. Recommend (a). Needs a ruling because it picks which fact moves.

**R-2. V: Maret Vos's birthplace, and where Danne Sok is from.**
L15: Vos "born in the breeding pens of Maw-6, ... freed at age sixteen when Maw-6 suffered a partial roof collapse"; Sok "a heavy-tier striker from Maw-9 itself". But L17, L19 and L213 have Vos describing Maw-9's arches from nineteen years of knowing it, and "the place where she had been born" is Maw-9 ("walked through the place where she had been born and found it empty"). L15 against L17-L213 is a contradiction inside V. `CC-160`/`MCD-234` give no origin. Option: Vos born at Maw-9, L15 "Maw-6" changed to "Maw-9"; Sok's origin then needs a second look so both are not "from Maw-9 itself".

**R-3. Tech level across I, II, IV, V, VII (the Batch 363 held question: does `PH2-049`'s "pre-industrial, no engines, no firearms" bind mainline Cian?).**
`WC-012`/`WC-013`/`CULT-199`/`PH2-049` against these lines:
- I L263-L291: "the steam engine on the ground floor that powered the entire operation", drive shafts, cargo elevator (six uses of "steam engine").
- II L25 hydraulic cargo press (also IV L81); L167 "its motor a low hum"; L173 "a stopwatch"; L277 patrol boats' "propulsion systems ... Forge ash clogged the intake manifolds".
- IV L33, L85-L117: "armored scout vehicles", "the exhaust from the engine stacks", "The driver gunned the engine. The wheels spun", "twelve-ton armored vehicle".
- V L139 "a headlamp"; L161 "a mounted scope"; L199 a negated "electronic authorization".
- VII L23 "still warm from its own boilers"; L193 "gun ports ... the gunners"; L219 "One Marine lowered his rifle".
Mixed evidence in the ledger: mainline rules lock siege guns (`CC-121`), Trust Crawlers (`MCD-238`) and, at `ARS-426`, small arms "only" as SBD issue. They do not lock steam engines, motors or engine-driven vehicles; the ledger's "steam" is vapor (`MCD-250`, `ASH-048`) and its "engines" are siege engines or geothermal (`HLD-020`, `MCD-549`, `ASH-008`). Needs one rule, not twelve edits: either state that `PH2-049` is homage-World only and set mainline's ceiling (steam power, wheeled vehicles, small arms), or edit the chapters.

**R-4. Pistols and rifles in Trust hands against `ARS-426`.**
IV L169 "a standard-issue Dead Drakma officer's pistol with the Trust seal on the grip", carried six months and held again at V L233 ("the trophy from Iron Shallows"); I L49 "government sidearm" on the Forge-7 guards; VII L219 a rifle. `ARS-426` locks small arms as SBD-issue, culturally coded as a mark of cowardice, useless against density-scaled combatants. Trust Army and civil guards are not SBD. Options: (a) the weapon is an SBD-issue sidearm (the convoy commander is read as an SBD attachment), (b) a one-line ruling extending `ARS-426` to Trust officers, (c) rename the prop (a Trust "officer's signal-pistol"?). R-3 and R-4 should be ruled together.

**R-5. Onyx's first person in manuscript codas (`VB-063` ruling 1: "the blade, never I").**
I L373 "I record this. The first entry."; II L399 "the way I calculate mass"; IV L209 "I hold no new names ... a word I do not yet possess". (Repo III's closing also uses "I keep them ... I hold".) V and VII use "the blade" throughout. `VB-063` says "Articles follow the manuscript codas" but also "never 'I'" with Kanja Chronicle IV's sealing line as the single exception. Needs one ruling: amend `VB-063` to record I-IV as the earlier convention, or change the codas to "the blade".

**R-6. II: Sera's naming ceremony.**
I L175-L179: the ceremony is the sixth day, the day of the raid's sixth night; `CC-117`: Breck "misses [it] to execute the raid". II L323: Sera "would be named next week in a ceremony he had missed the preparation for", L355 "the naming-ceremony crowd, thirty people, his wife's family". Three weeks have passed since the raid. Choose: the ceremony was held (and missed) three weeks ago, or it was postponed. Edits at II L323 and possibly L355.

**R-7. IV against V: the three anonymous deliveries.**
- Who found the chart: IV L183 "Kanja found a rolled sheepskin tube in the bottom of the ammunition crate he was carrying" against V L51 "The chart was found by Ostra while sorting ammunition after the engagement. She had carried it to Kanja".
- Medium: IV L33 "a single sheet of pressed linen paper" against V L49 "hand-drawn on vellum ... on parchment"; the chart is a sheepskin tube in IV, parchment in V, and sail-cloth in VII L27.
- Channel and timing: IV L31 "the same channel as the medical crate three months prior" against V L47 (the crate was left on the field-hospital dock, three days after the Trench; Iron Shallows is four months after the Trench).

**R-8. VII: how The Audit was captured, and when the fleet was "acquired".**
L23: "captured during the Battle of Iron Shallows when Kanja was nineteen, the engagement where three rebel trawlers had drawn a warship into a reef channel at low tide and held position while the Trust crew abandoned their grounded vessel". IV has no ship and no trawlers, only 170 fighters on foot and 30 decoys, and the whole fleet of trawlers is acquired after Killane (VII L13, L17). `MCD-285` already reconciles it: an escort vessel responding to the stranded convoy ran aground and was boarded by Kanja's fighters. L13 also reads "Between the Sewer War of Killane and his twenty-first birthday, Kanja acquired nine vessels", yet The Audit, the ninth, was taken at 19, before Killane. Suggested: replace the trawler clause with the `MCD-285` mechanism ("an escort warship that ran aground answering the stranded convoy"); L13 becomes "By his twenty-first birthday Kanja held nine vessels." (Boilers at L23 fall under R-3.)

**R-9. V against VII: Hask's ledger pages.**
V L107 "a sheaf of twelve" at Maw-9; V L223 "already eleven pages longer than it had been that morning" (so twenty-three after the day); VII L13 "grown from one page to twelve and was now threatening a thirteenth", L51 "The ledger's thirteenth page". Choose which number moves.

**R-10. I L281: Trinity items already "forged" by Kanja at 18.**
"He had forged an armor system and a sentient-bonded war club and a talisman that regulated the metabolic output of a Living Drakma network". Against `ARS-010`/`ARS-030` (forged at the Mao Volcano, forger unnamed), `MCD-232` (Mafesto bonded about two years before the Trench), `MCD-142` (the Talisman has run autonomously for three centuries "without Kanja's knowledge ... he believes it is merely a synchronization server"), `ARS-345` (bonded to his skeleton). Two points: Kanja as the forger is not locked, and `ARS-030` does not make Obsidian Malice sentient (Onyx is the sentient piece). Needs a ruling on wording.

**R-11. Names.**
- I L213 "a dockworker named Tomas" (rename per the Batch 98/330 precedent against Tomas Grieve, `MCD-093`).
- IV L9 and V L105 "Ren Voss" (Ren Oshaal, Voss in the Maw rules). V L105 lists Ren Voss and the Dock-Row Nine sailmakers as "the newest arrivals" at Maw-9 but IV L9 has both arriving before Iron Shallows with the same four words ("We heard about the Trench").
Minor; Abad's call.

**R-12. Sephtis's age against "before the Sovereign Trust existed".**
VII L25 "holding a tiller since before the Sovereign Trust existed"; L203 "he had been sailing before the Sovereign Trust was founded"; `CC-037` gives 1,997 years and `MAW-091` dates the Trust's era from "~2,000" years ago. A three-year margin inside an approximate figure: either fine as is or soften both lines to "since the Trust's earliest years". Low.

**R-13. I: internal timing slips.**
L173 "falls on the seventh night from now ... We execute on the sixth night" (and "Six days"); L257 "propped open at 0145 by the last man of Hask's team ... as he exited the building" while the team enters at 0200 and exits at about 0241. No ledger rule is involved. Low.

**R-14. Halst's manumission by streak.**
V L15 Halst "had won his manumission after forty-seven consecutive bouts". `MAW-073`/`MAW-079` make manumission a 3:1 Scrip ratio with fewer than 200 in 5,000 years crossing it. Compatible if the streak earned the ratio. A one-clause gloss in V or a note in `CC-158` closes it. Low.

**R-15. `MCD-286`'s statistic is not in I.**
`MCD-286` and repo VIII attribute "1.2 million workers underpaid by 40% over twelve years" to the Scrip-Forge Raid's rubbings. Chronicle I's own evidence is 14 against 38 percent, "three years", "twelve thousand families" (L39, L87-L89, L337). Not a contradiction (the rule says "additionally"), but a reader of VIII will look for it in I. Options: add one line to I, or leave as is.

**R-16. VB-050 structures, throughout.**
The banned structures (balanced antithesis such as "It was not approval. It was acknowledgment.", and briefing-room dialogue where a character explains the plan: I Scene 2, II Scenes 1-2, IV L47-L65, V L33-L41) run through all five chapters: about 8 to 13 antithesis constructions in each. The Batch 363 audit did not treat the manuscript as bound. One ruling: the Voice Bible exclusion list governs new drafting only, or it governs the manuscript too.

**R-17. Batch 70 insertions in III are repo text, not the upload.**
See section 2. `MCD-533`, `MCD-641`, `MCD-1137` and `CC-158`/`159`/`160` cite them as "the manuscript's own locked account". Abad's V (L13-L15) is consistent with the docks account but does not state it. Ruling needed only if Abad wants the manuscript itself to carry that line.

### 3.4 Checked and found clean

- **Crew dossiers.** `CC-115`: Hask 31 years' tenure (I L93, II L77, V L25), named *The Audit* (VII L23), counts 12,006 at Maw-9 (V L219). `CC-116`: "Kanja" in place of "boy" (II L369). `CC-117`: Breck 22, Pier Nine night shift, daughter born four months before the raid. `CC-118`: Breck chalks THE TRENCH MONARCH on Greer (II L325). `CC-119`: Breck's four months of silence, two words at Iron Shallows (IV L159), the channel call at Ghost Harbor (VII L161; word count aside, M-3). `CC-120`: Maren mid-30s, father's Crane Six 34 years (I L131, II L169). `CC-121`: 17 plank-bridges, four working guns from eight (IV L15), Maw-9 math verified (V L177). `CC-130`/`131`: Efa Gol, Warehouse Twelve press, the Iron Shallows 30-fighter decoy (IV L79-L81), the Maw-9 diversion (V L113), the fourth ship through the reef gap (VII L201). Pronouns correct for Gol, Ostra, Hask, Breck and Maren in all five chapters; only Vos is wrong (M-1).
- **Hask's age.** I L93 "fifty-three" (age 18); repo III "fifty-four" (age 19). II, IV, V and VII state no age. Progression holds; nothing to increment.
- **Trinity mechanics.** No Trinity power is used on the page in any of the five. Mafesto appears once, dormant and inert (IV L75), and "the operation did not require the Trinity"; the Black Trench stays the first combat deployment (`MCD-232`). Obsidian Malice and Onyx's five named powers never appear. No Heartline (`ARS-437`), Dark Ledger, Last Ward or Lunar Resonance. Onyx's bond is keyed to the age-17 pawn-shop acquisition (I L29, L201; `ARS-020`/`ARS-341`, which already names I and V as depicting it).
- **Kill doctrine.** No kill by Kanja in any of the five: the Raid, Dredge-Line, Iron Shallows and Maw-9 are all bloodless, and Ghost Harbor is a bloodless escape. `CC-161`, `MCD-1881`, `MCD-1882` are not engaged. II L71 states "No killing" as doctrine, consistent with `CC-161`'s costed-default framing.
- **Twenty-Two Victories.** `MCD-231` (Forge-7, 38 against 14 percent, 200-soldier column, planks over sludge), `MCD-232` (93 of 120), `MCD-233` (400 infantry, twelve haulers, Gol's thirty, Ostra's six charges, no casualties, no alias), `MCD-234` (about 12,000 freed, load-bearing arches undermined from below), `MCD-235` and `GEO-006` (Ash Harbor, six warships, reef gap, anchor-chain lodestone, renamed Ghost Harbor), and the alias ages (`MCD-230`: Trench Monarch 18, Bane 19, Sovereign Ghost 21) all agree.
- **Industrial Myth timing (age 21).** None of the five uses the alias. V L105 has smelters from "the Furnace Quarter" joining the fleet, which does not touch the Furnace District Strike (`MCD-244`).
- **Atlas.** Rexhaven as capital (`MCD-110`), Ash Harbor on Jicome's southern coast as a reef-gap basin (`GEO-006`), the Southern District. Unplaced and not contradicting anything: Portside, Lower Portside, Dock-Row Six/Nine, Pier Street, Anvil Street, the Dredge-Line, Iron Shallows, the Furnace Quarter, Maw-9's own site. They stay in the Atlas enrichment queue.
- **Real-world proper nouns.** None. (Earth units appear throughout: feet, inches, pounds, gallons, and "Tuesday" at IV L29; the ledger uses meters and has no pounds or gallons. Optional.)
- **Child safety.** The Cestari children and infants at Maw-9 (V L19, L207, L221) are described without any sexual content, consistent with the locked Cestari material.
- **Voice Progression Sheet, Phase 1.** Body averages 11.6 to 15.0 words per sentence (I 11.7, II 11.6, IV 15.0, V 13.8) against the sheet's "15-25" for Phase 1; VII 11.8 sits inside Phase 2's "10-18". No Iron/Rust verdicts in any prose body, no Onyx direct address in the body. Informational only.

## 4. Counts and ordering

| Class | Count |
|---|---:|
| Mechanical (M) | 8 (6 in the chapters, 2 ledger-side) |
| Needs a ruling (R) | 17 |
| Total | 25 |

Top items to take first: **R-1** (Maw-9's builders and Sephtis against Old Dominion chronology), **M-1** (Vos's pronouns), **R-3 with R-4** (one tech-level ruling), **R-5** (first-person codas against `VB-063`), **R-8** (The Audit's capture), **M-5** (Sera's age). The three ledger rules that need touching if Abad agrees with the proposed fixes: `CC-132`/`CC-133`, `CC-121`, and (R-1 depending) `MAW-010`/`MAW-090` notes.
