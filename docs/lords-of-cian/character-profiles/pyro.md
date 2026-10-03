# Pyro (Ignis Rexmar) — Profile & Game Plan

**Status:** walkthrough drafted
**Track:** Character Chronicle (priority launch per Abad, 2026-10-03)
**Gate cleared:** NO — no Chronicle prose may be drafted or presented until this file reaches "game plan approved."

This file is the standing gate artifact for this character, per the Character Chronicle Launch
Protocol locked in `CLAUDE.md`. It is the single source of truth for who this character is before
any Chronicle is written or rewritten — not a summary produced after the fact.

Standing direction for this series (Abad, 2026-10-03): "Pyro and his Triad need to be well written.
every connective tissue must be well thought out and well placed so it's only logical." Because the
Triad Guardians (Varkul, Sorya, Varruk) are bonded to Pyro specifically (`CC-048`) and have no
existence in canon apart from that bond, their rules are pulled into this walkthrough in full rather
than left for a separate file.

Ledger snapshot used: `ledger_version` 36.3, 2,667 rules. 61 rules name Pyro, Ignis, the Living
Gate, the Triad, or the Heart's Tools directly; roughly a dozen more touch him through his mother,
his lineage, or the Dhar-Kael clade without naming him. Every one is listed below.

---

## 1. Rules Walkthrough

Every locked rule touching this character, pulled from `canon-ledger.json` and organized
thematically rather than by ID order. Each entry: `RULE-ID` — one-line paraphrase, not the full
statement (the ledger is the source of truth for exact wording).

### Biography / stats

**Name and parentage**
- `CC-047` — Hidden birth name Ignis Rexmar; Kanja's biological son; does not know his own parentage.
- `MCD-022` — "Pyro" is a ship-name; his birth was NATURAL; his mother completed the Dhar-Kael bond
  before T.D.K.'s Living Gate curse; the Demaron event is "separate from and after the birth";
  Stormbreaker's trauma is preserved, resequenced rather than replaced.
- `WC-017` — World Codex compressed account: born during a catastrophic containment event; his mother
  (Kanja's wife, a veil-reader who discovered T.D.K.'s hidden SBD architecture) was inhabited by a
  Demaron; Stormbreaker fought and won; T.D.K. had installed the Living Gate as containment; her final
  act inverted the Gate into a forge, producing the Triad "before Pyro was born in the severed instant."
- `MCD-132` — His birth and his mother's transformation into the Living Gate are two effects of one
  single event ("born in the severed instant"); narrows `MCD-022`'s "separate from and after" to
  sequentially distinct within the same event, not separated by meaningful time.

**Lineage (derived from rules that do not name him)**
- `MCD-101` — Kanja's mother is Val Saeryn Kareth (93,179 years); Ozmund's mother is her sister Val
  Mirel. Kanja and Ozmund are cousins, so Ozmund is Pyro's first cousin once removed; Pyro's paternal
  grandmother is Karesian.
- `MCD-137` — Val Saeryn (his grandmother) is alive, in deep cover.
- `MCD-025` / `MCD-091` — Maro Rexmar, Kanja's father and therefore Pyro's grandfather, is murdered at
  the Fulfillment Ceremony, Book 1's opening.

**His mother (never named anywhere in the ledger)**
- `CC-046` — Kanja's "first and only wife," a veil-reader; T.D.K. installed a voice-keyed Living Gate
  curse in her as a containment response to her discovering his hidden architecture; her pregnancy
  amplified the Gate; a Demaron inhabited her; Pyro and the three Dhar-Kael were produced as her final
  act. Its "body's vessel was ultimately ended" framing is flagged as in-universe misdirection.
- `MCD-136` — A-1 resolved: she was both the last keeper of the Dhar-Kael tradition and an
  SBD-recruited veil-reader who found T.D.K.'s architecture in the Directorate's oldest protocols; she
  completed the Dhar-Kael bond before the curse took hold.
- `MCD-040` — She was the last keeper of the Dhar-Kael tradition.
- `MCD-131` — She is NOT dead: when the Demaron took hold, the Living Gate (a voice-keyed
  breach-lattice) was deployed to seal it; she inverted the Gate into a forge, and is fused into its
  architecture, "no longer flesh in the ordinary sense"; the Triad are what she pushed outward through
  the inversion before the fusion completed.
- `MCD-133` — The Codex (`CC-045`/`046`) and SBD casework (`SBD-010`) all say she died; deliberate
  in-world misdirection; `MCD-131`/`132` are the sole objective account.
- `MCD-277` — "The Rat-Catcher's Apprentice" (Kanja age 96): she joins the fleet as provisions manager,
  roughly 194 years before Pyro's birth.
- `OPEN-006` (open_decisions, resolved) — Her fate was once open because Abad found the "killed"
  account unworthy of her ("too formidable"); resolved by `MCD-131`/`132`.

**Timeline and age**
- `MCD-269` — Dates the Living Gate's activation "at Pyro's birth, age ~290" (Kanja's age); the Gate
  is a real, ancient Karesian cavern-system heritage site a Trust survey team investigates at Kanja 282.
- `MCD-275` — The Karesian Survey Interdiction (Kanja 282) is the Living Gate cavern survey, part of
  the Shadow Skirmishes campaign.
- `MCD-270` — "The Birth of Fire" (Kanja 290): natural birth, and the Dhar-Kael imprinting bond
  completes between Pyro and the *juvenile* Varkul, Varruk, and Sorya; Kanja stays 12km away so the
  Talisman's output does not disrupt the bonding frequencies.
- `MCD-277` — "The Pyro Incident" (Kanja 296): first observed instance of the Triad's
  thermal-management function around him. "The Last Breakfast" (Kanja 314): the Long Mask closes on
  Pyro serving Kanja stew as the Shimmer and the Gilded Lighthouse's pendant activate.
- `MCD-272` — "The Scourge's Heir" (Kanja 308): his food-based healing is proven biologically real on
  Ironbane's nerve damage.
- `CC-101` — Pyro is "roughly 24-36 at Book 1," younger than Abyss (~45, "the crew's youngest adult
  recruit").
- `CC-110` — Sephtis has known Kanja is Pyro's father for 24 years.

**Age math (Kanja's age is the only clock canon gives; Pyro's age = Kanja's age minus ~290)**

| Kanja's age | Event | Rule | Pyro's age |
|---|---|---|---|
| 96 | Mother joins the fleet as provisions manager | `MCD-277` | — (~194 years before birth) |
| 248 | Varruk's first appearance ("the Dog Watch") | `MCD-277` | — (42 years before birth) |
| 282 | Trust survey of the Living Gate cavern system | `MCD-269`/`275` | — (8 years before birth) |
| ~290 | Birth of Fire; Gate activation; Triad imprint | `MCD-269`/`270` | 0 |
| 296 | The Pyro Incident (Triad thermal management first seen) | `MCD-277` | ~6 |
| 304 | The Final Forge (Kanja's last forging) | `MCD-277` | ~14 |
| 308 | The Scourge's Heir (food healing proven) | `MCD-272` | ~18 |
| 314 | The Last Breakfast; Long Mask ends; Pi-Awakening | `MCD-277`, `CC-005` | ~24 |
| Book 1 opening | Fulfillment Ceremony | `MCD-091` | ~24 or ~36 (see below) |

Book 1's offset from the Sovereign Pier (Kanja age 30, `MCD-246`) is an open question:
- **284-year reading** (the Long Mask's own length, `CC-005`/`MCD-246`; Red Beard's defection 29 years
  after Kanja 285, `MCD-269`; Book 1 contains the Pi-Awakening, `WC-022`): Book 1 sits at Kanja 314,
  so Pyro is **~24** at Book 1. Sephtis's "24 years" (`CC-110`) then means he has known since the
  birth itself.
- **296-year reading** (`MCD-091`: Ceremony and Pier "roughly 296 years apart"): Book 1 sits at Kanja
  326, so Pyro is **~36** at Book 1 — but the Last Breakfast/Pi-Awakening at 314 (`MCD-277`) would
  then fall twelve years *before* Book 1 opens, which `WC-022` (Pi-Awakening inside Book 1) does not
  allow. Sephtis's "24 years" would then date his knowledge to Pyro age ~12.
- `CC-101`'s "roughly 24-36" hedges across both readings rather than picking one.

**Stats**
- No density figure for Pyro is locked anywhere in the ledger, at any age.
- `MCD-223` — His Book 5 peak is deliberately unlocked: no density numbers, full potential sealed
  behind a reality-scar; locked baseline is Thermal Variant, Metabolic Overdrive, and Causal
  Convergence only.
- `MCD-140` — He is one of the nineteen Avatars under the Talisman of Mao's Sovereign Umbrella
  (Varkul, Sorya, and Varruk are three more of the nineteen).
- `MCD-139` (superseded) — Earlier count of 16 Avatars "with Pyro counted among them"; replaced by
  `MCD-140`.

### Relationships

**Kanja (father)**
- `CC-079` — Kanja considers Pyro his son, knows it, and hides it from Pyro; Stormbreaker and Azar
  (Dreadlord) also know or suspect; Pyro does not.
- `MCD-270` — Kanja is kept 12km away at the birth.
- `MCD-277` — The Last Breakfast: Pyro serves Kanja stew on the last morning of the Long Mask.
- `ARS-421` — The Rexmar Apron is carried "as dramatic-irony/identity texture against Mafesto, his
  unclaimed inheritance he doesn't know exists."
- `ARS-414` — When Pyro eventually learns his father's identity, Sorya is the one who can show him his
  own history from outside his own perspective.

**Those who know his parentage**
- `CC-079` — Kanja; Stormbreaker and Azar know or suspect.
- `CC-110` — Sephtis, for 24 years, never disclosed.
- `CC-045` — Stormbreaker (Kaelen) fought and defeated the Demaron in Pyro's mother with Kanja's
  consent, and serves as Pyro's guardian without Pyro knowing this history.
- `MCD-252` — Stormbreaker recruited at Kanja 70 (Seismic Variant); `MCD-253` — Azar recruited at
  Kanja 85 (Stagnant Variant, dread-aura). Both well before the birth.

**The Triad Guardians (bonded to him specifically)**
- `CC-048` — Varkul, Varruk, and Sorya are permanently and non-transferably bonded to Pyro
  specifically, not to the ship or crew.
- `CC-095` — Varkul's hierarchy: Pyro first, ship second, crew third; the bond manifests as
  Indomitable Will; extended separation from Pyro causes increasing, non-lethal strain.
- `CC-097` — Sorya's hierarchy: Pyro first, the Oath second, ship third — but if Pyro and the Oath
  conflict, the Oath wins; if anyone (Kanja or Pyro included) breaks a sworn vow, she becomes the
  instrument of correction.
- `CC-099` — Varruk's hierarchy: Pyro first, pattern second, ship third; always knows the safest path
  to Pyro; the most visibly bonded in daily life; abandons reconnaissance if Pyro is threatened.
- `ARS-414` — Sorya's Witness Shriek gives ~3 seconds of sensory confusion that Varkul and Varruk use
  to extract Pyro from danger.
- `ARS-421` — Keeping Pyro emotionally stable is part of the Triad's role, because his Thermal Vents
  fire under fear or anger.
- `MCD-277` — The Pyro Incident (Kanja 296) is the first observed Triad thermal-management.

**His mother**
- `MCD-131` — Alive, fused into the Living Gate's architecture; no rule records any contact,
  awareness, or reunion between them.

**Wider crew and cast**
- `MCD-272` — Ironbane: the first person Pyro's food-healing is proven on (nerve damage).
- `CC-123` — Nelle Adessi widens her clinic doorway for Varkul unasked, giving Pyro a room "where
  people are healed rather than broken."
- `CC-126` — When Nelle dies, "Pyro loses the one space in his life that wasn't about war."
- `MCD-221` — Book 5 Engine front: Kanja, Ozmund, Pyro (father, father's cousin, son).
- `ARS-403` / `ARS-414` — Sephtis calls Sorya "the True Log," his highest compliment.
- `CC-101` — Abyss is older than Pyro and the youngest "adult recruit."

### Abilities / gear

**Pyro**
- `MCD-223` — Locked baseline: Thermal Variant biology, Metabolic Overdrive, Causal Convergence;
  peak sealed behind a reality-scar; no density figures.
- `ARS-190` — Carries no Living Drakma weapons: the Cian-Feast Kit, Thermal Vents, the Rexmar Apron.
- `ARS-421` — The three "Heart's Tools": the Cian-Feast Kit (ordinary Dead Drakma kitchen tools made
  into weapons by his grip heating metal to searing, cauterizing temperature; kitchen awareness doubles
  as combat instinct; his food's performance/healing effect is what the crew calls "eating well before
  a fight"); Thermal Vents (warming radiance at rest, involuntary heat surges under stress, a 5m
  directed thermal blast under fear or anger); the Rexmar Apron (no mechanical function; identity
  texture).
- `MCD-272` — Food-based healing: Thermal Variant biology passively infuses "Aethelgard-adjacent"
  healing energy into food he cooks; proven on Ironbane at Kanja 308.
- `CULT-197` — Pyro's thermal flash-heating is part of the anti-Ever-Haunt light-vulnerability toolkit
  (with Ironbane's discharge and Anirak's strobe).
- `CULT-198` — His thermal output can suppress, not cure, Green Mark contamination.

**The Dhar-Kael clade**
- `MCD-040` — Three companion species bonded symbiotically with Karesian biology: Tide-Back Coursers
  (Varkul), Oath-Raptors (Varruk), Apex-Felines (Sorya); imprint happens during a juvenile window; the
  bond is permanent, biological, non-transferable; three survivors remain, and the clade dies with them.
- `ARS-200` — The Triad are the last three Dhar-Kael.
- `MCD-041` — The Vael Kem fed on the Dhar-Kael and drove them near to extinction; the Rexmar military
  tradition was forged in that war.
- `ARS-355` / `CC-100` / `ARS-431` — Dhar-Kael Courser cartilage in the Mend-Line, the Mercy Draught,
  and the Verity Vein is historical/stockpiled material, never harvested from the three living animals.

**Varkul (TRIAD-1)**
- `CC-049` — "Drown-Warden" Varkul; homage Svadilfari; ~4,025 lb Land Form and an 88%-larger
  Hydro-Titan Form.
- `MCD-020` — His morphing is a natural adaptive response to habitat, not a power; the Harrow Ring is
  hydrodynamic physics.
- `CC-094` — Land Form (mass displacement, scent tracking, Harrow Presence discipline-collapse) and
  Hydro-Titan Form (Hydro-Inertia, the Breach, Snap-Turn, Wake Distortion, Living Depth Charge).
- `CC-095` — Bond as Indomitable Will; vulnerable to Blight Frequencies, Abyssal Bile-Salts, and
  separation from Pyro.
- `ARS-412` — Bioluminescent threat-markings, Drakma-carbonate hooves, three-layer bio-armor, the
  Density Compression Charge; the Guardian Clause confines the Harrow Ring to Pyro-vowed defense only.

**Sorya (TRIAD-3)**
- `CC-050` — Homage Muninn (Memory); Vow-Taste is her primary betrayal detection.
- `CC-096` — 1,150-1,300+ lbs, melanistic, emerald eyes; Witness-Scouting, Vow-Taste, Shard-Recall,
  Mimic Speech, Long-Haul Endurance, Stealth-Dominance.
- `CC-097` — Bound to the Oath above all; vulnerable to Blight Frequencies, Abyssal Bile-Salts, and
  the Oath Paradox.
- `CC-136` — A real five-technique predation layer (Black-Rosette Vanish, Throatline Shear,
  Green-Eye Fixation Trap, Bone-Engine Pin, Silent-Break Commit); the SBD's "CONFIRMED" ratings on it
  are overclaimed.
- `ARS-414` — The Witness Shriek; the future reveal function toward Pyro.

**Varruk (TRIAD-2)**
- `CC-051` — Homage Huginn (Thought); aerial reconnaissance; Angle-Whisper.
- `CC-098` — ~195 lbs, 27.6 ft wingspan; Pattern-Scouting, Angle-Whisper, Cadence Break,
  Storm-Lane Travel, Guidance by Refusal.
- `CC-099` — Bond as navigational certainty; grounded in enclosed spaces; Cadence Saturation.
- `ARS-413` — Rust-stained plumage, ~200m Cadence vocalization, the Stare, everyday growl/purr/whine
  register.
- `ARS-395` — Sereth Vaul's Void Wake degrades against Varruk into a pure endurance contest.

**How the SBD sees the Triad**
- `SBD-020` — "Miremaw Varkul" is a "living preservation clause"; the SBD is barred from capturing,
  bonding, or commanding him.
- `SBD-021` — Varruk rated OMEGA-PRIME.
- `SBD-022` — Sorya rated OMEGA-PRIME (conditional), a "living archive."
- `SBD-044` — Varkul rated OMEGA-PRIME and regarded as the strongest non-human in the setting;
  density-unrated, ceiling never shown maxed.
- `SBD-045` — Varruk's five-tactic "Offensive Capability Suite" is contested, resting on a corrupted
  informant stream.
- `CULT-199` — The "Stone, Iron, Meat" documentation lexicon and the Continuity Lock for Triad files.
- `CULT-200` / `MCD-1727` — The Oracle Conflict Map's six domains include Demaron Ingress Mechanism,
  Vessel Termination Necessity Logic, Triad Bond Mechanics, and Harrow Ring Clause Conditions — every
  one touching Pyro's birth or bond.

### Already-locked plot beats (book-level or Chronicle-level)

**Pre-Book-1 (Long Mask, Kanja ages 282-314)**
- `MCD-269` / `MCD-275` — The Living Gate cavern survey (282).
- `MCD-270` — The Birth of Fire (290).
- `MCD-277` — The Pyro Incident (296); the Last Breakfast (314).
- `MCD-272` — The Scourge's Heir (308).

**Book 1, "The Deposed King"**
- No Pyro-specific Book 1 beat is locked. He is present at the Last Breakfast as the Pi-Awakening
  begins (`MCD-277`), and the Pi-Awakening sits inside Book 1 (`WC-022`). His grandfather Maro dies at
  the opening (`MCD-025`/`091`).

**Book 3, "The Dark Monarch"**
- `MCD-093` / `CC-123` / `CC-125` / `CC-126` — Nelle Adessi's clinic is his one room outside war; the
  Ronin kill her; he loses that space.

**Book 5, "The Miner's Son"**
- `MCD-097` / `WC-022` — "Pyro peaks."
- `MCD-221` — He fights on the Engine front with Kanja and Ozmund.
- `MCD-223` — The peak is significant but carries no committed figures or new abilities.

**Chronicle level**
- None. See the corpus section below.

### Reserved / unresolved threads
Things already flagged in the ledger as deliberately open, not yet paid off, or explicitly held
back for a future book/Chronicle. These constrain what the profile and game plan may touch.
- `MCD-223` — His Book 5 peak capability: no density numbers, no added abilities, sealed behind a
  reality-scar.
- `CC-047` / `CC-079` / `ARS-414` — The parentage reveal: he does not know; when and how he learns is
  unlocked, except that Sorya will be the one to show him his history from outside.
- `MCD-131` / `MCD-133` — His mother is alive and fused into the Gate, while every in-world record says
  she is dead. Whether she can perceive, act, communicate, or be reached is not locked.
- `SBD-041` / `CC-140` — Who fed Shelton Dexton the false Pyro Birth account, and why: reserved for
  Archon Meridian's eventual SBD cleanup or Dexton's own reckoning. `CLAUDE.md` (Batch 301 notes) records
  the same item as "reserved as a future Archon-network correction-scene hook."
- `SBD-044` — Varkul's own arc: unaware of the SBD's surveillance apparatus, he discovers it and turns
  aggressive, intended to intersect Archon Meridian's unknowing dismantling of his father's SBD
  architecture (`MCD-122`/`130`); worthy opponents for the Triad are to be drawn from SBD captive stock
  and Hollow Shogunate holdings.
- `SBD-010` / `MCD-133` — The SBD's official Demaron-possession file, kept false by design.
- `MCD-1729` — Cinderhilt is real; what it has actually fought is open. Its only link to Pyro is the
  false Dexton account.
- `CULT-200` / `MCD-1727` — The SBD's own incident on this event is "permanently held open, never
  closed" under the Tighten posture if flagged.
- `MCD-099` — Archon Meridian stays an unresolved third force after Book 5.
- "Causal Convergence" (`MCD-223`) is named but never defined anywhere in the ledger.

### Existing Chronicle corpus (if any)
For a character with Chronicles already locked (backfill case): a list of what's already been
written and what it already establishes, so the profile is a synthesis of demonstrated
characterization, not a competing invention.
- **None.** A grep of all 1,505 files in `docs/lords-of-cian/chronicles/` for "Pyro" and "Ignis"
  returns zero matches. The Triad (Varkul, Sorya, Varruk), "Dhar-Kael," "Living Gate," "Demaron," and
  "veil-reader" also return zero matches. This is a fresh launch, not a backfill.
- Silent overlap: several locked Alias Chronicles are set inside Pyro's lifetime (Kanja 290-314) and
  never mention him — among them `MCD-493` (age 300), `MCD-1477` (305-314), `MCD-1472` (308),
  `MCD-1252` and `MCD-1255` (314), and `MCD-1022` ("The Last Coat He Ever Wore," 314, the night the
  Scourge coat comes off — the same year as the Last Breakfast, `MCD-277`).
- Outside the Chronicles: `ozmund-verehimu.md` mentions him once (the `MCD-221` Engine-front line).
  `kanja-haku-rexmar.md` does not mention him at all. `character-chronicle-gameplan.md` lists him and
  the Triad in Tier 2 ("could run as one shared thread or three separate ones, undecided").

### Connective-tissue findings
Contradictions and gaps among his rules, and between rules and the Chronicles. Quoted with IDs. Not
resolved here.

1. **His age at Book 1.** `MCD-091`: Ceremony and Pier "roughly 296 years apart" (Pyro ~36). Against
   it: `CC-005` "Long Mask persona lasted 284 years, ending when the Gravity-Fetter pendant was severed"
   + `MCD-277` "The Last Breakfast (314) closes the Long Mask on Pyro serving Kanja stew" + `WC-022`
   Book 1 includes the "Pi-Awakening" (Pyro ~24). `CC-101` hedges: "roughly 24-36 at Book 1."
2. **When Sephtis learned.** `CC-110`: "He has known Kanja is Pyro's father for 24 years." On the
   284 reading that is since birth; on the 296 reading, since Pyro was ~12. Neither rule says how he
   learned (`CC-110`'s Chrono-Anchor bells only verify claims against his own memory).
3. **Who knows, versus what the records say.** `CC-047`: Pyro "does not know his own parentage";
   `CC-079`: Kanja "hides it from Pyro." But in-world records name the mother as Kanja's wife:
   `CC-046` "Kanja's first and only wife"; `WC-017` "his mother (Kanja's wife...)"; `SBD-041`
   "Kanja's wife killed by an anomaly-class monster." The SBD and the Codex therefore record the
   lineage that Pyro himself lacks, and no rule says whether Pyro knows who his mother was married to.
   `CC-079` lists only Kanja, Stormbreaker, and Azar; `CC-110` adds Sephtis; `ARS-414` implies Sorya
   holds the history. Ozmund, Lauris, Onyx, and the rest of the crew are not addressed.
4. **Where the Triad came from.** Produced at the event: `WC-017` "her final act inverted the Gate into
   a forge, producing the Triad Guardians"; `MCD-131` "what she pushed outward through that inversion";
   `CC-046` "produced as her final act." Already existing: `MCD-040` "Three survivors remain" of an
   ancient clade the Vael Kem hunted (`MCD-041`); `MCD-277` "Varruk's first appearance 42 years before
   the Triad's bonding with Pyro (~290)"; `MCD-270` the bond forms with "the juvenile Varkul, Varruk,
   and Sorya." Varruk is seen at Kanja 248 yet is still "juvenile" at 290, and "produced" at 290.
5. **Whose bond it is.** `MCD-022`: "The Dhar-Kael bond was completed by his mother (the last keeper)
   BEFORE T.D.K.'s Living Gate curse"; `MCD-136` repeats it. But `MCD-040`: "The bond is permanent,
   biological, non-transferable," and `CC-048`: bonded "to Pyro specifically"; `MCD-270`: the
   imprint completes "between him and the juvenile" Triad at birth. If the mother completed a bond
   first, no rule says with whom, or how it became Pyro's.
6. **Order of events at the birth.** `MCD-022`: "The Demaron event is separate from and after the
   birth." `WC-017`/`CC-046`: the Demaron inhabits her and Stormbreaker wins *before* Pyro is born.
   `MCD-132` narrows it to "sequentially distinct within the same event." On the Gate: `MCD-131` says
   it "was deployed" when "the Demaron entity took hold"; `CC-046`/`MCD-136` say it was installed
   earlier as a response to her discovery, and "her pregnancy amplified the Gate" before the Demaron
   came. When the Gate was set, and whether Stormbreaker's fight came before or after the inversion,
   is not fixed.
7. **What the Living Gate is.** A curse in her body: `CC-046` "installed a voice-keyed 'Living Gate'
   curse into Kanja's first and only wife"; `MCD-131` "voice-keyed breach-lattice." A place: `MCD-269`
   "an ancient Karesian cavern-system heritage site already known as 'the Living Gate'... a real,
   ancient physical location." Whether the birth happened in the cavern, and whether she is now
   physically in it, is not stated.
8. **T.D.K. acting during dormancy.** `MCD-070`: the Great Breach (Book 1 epilogue) is when "T.D.K.'s
   5,000-year dormancy ends." Yet `CC-046`/`MCD-136` have T.D.K. install a curse in response to her
   discovery about 24 years before Book 1. `CULT-008` (SBD built on his legacy architecture with
   backdoors) could bridge this, but no rule says the curse was automatic or legacy.
9. **Kanja's distance and consent.** `MCD-270`: Kanja "required to stay 12km away" at the birth.
   `CC-045`: Stormbreaker fought the Demaron "with Kanja's consent." Compatible only if consent was
   given from a distance or beforehand. Not stated.
10. **Her two identities and her history.** `MCD-277`: she joins the fleet as "provisions manager" at
    Kanja 96. `MCD-136`: an "SBD-recruited veil-reader" who found T.D.K.'s architecture "buried in the
    Directorate's oldest protocols." When the SBD recruited her, when she married Kanja, and her name
    are all unlocked.
11. **The two false SBD accounts.** `SBD-010`: the official file, "a Demaron possession narrative in
    which Pyro's mother died during the Living Gate event." `SBD-041`: Dexton's separate file, "the
    Triad raised from birth by Pyro's mother in her own Shattered Kingdoms homeland, and Kanja's wife
    killed by an anomaly-class monster." `MCD-1729` names that monster Cinderhilt. Both are locked as
    false; `SBD-041`'s "raised from birth" also collides with `MCD-277` (Varruk at 248).
12. **The Archon hook is thin.** `SBD-041` reserves the false file for "Archon Meridian's eventual SBD
    cleanup or Dexton's own reckoning"; `SBD-044` ties Varkul's arc to Archon's "unknowing dismantling
    of his father's SBD architecture." No rule says what Archon or his network ever learns about Pyro,
    his mother, or the Gate.
13. **Varkul's epithet.** "Drown-Warden Varkul" (`CC-049`, `MCD-140`) versus "Miremaw Varkul"
    (`SBD-020`, `SBD-044`). No rule says whether "Miremaw" is an SBD designation or a second name.
14. **Undefined ability.** `MCD-223` locks "Causal Convergence" as part of his baseline; it is defined
    nowhere. "Metabolic Overdrive" is defined only through `ARS-421`'s cross-reference to food effects.
    `MCD-272` calls his healing "Aethelgard-adjacent," the same word as Kanja's "Aethelgard Kinetic
    Radiance" (`MCD-142`), implying inheritance from Kanja; no rule says so.
15. **"Heir" in public.** `MCD-272` titles the Kanja-308 entry "The Scourge's Heir," while `CC-047`/
    `CC-079` keep the parentage hidden from Pyro. No rule says whether the crew or the world call him
    an heir, and on what grounds.
16. **The Rexmar name on him.** `ARS-190`/`ARS-421` give a boy who does not know he is a Rexmar an item
    called "the Rexmar Apron." Whether that name is in-world, who gave it, and why are unstated.
17. **Maturation and child-safety.** He is roughly 0-24 across Kanja 290-314. `MCD-277`'s Pyro Incident
    puts him at ~6; `MCD-272` at ~18. No rule locks his maturation rate (his biology is part Karesian
    via `MCD-101`, Thermal Variant, and Dhar-Kael-bonded). `CC-101` calls Abyss "the crew's youngest
    adult recruit" and says Pyro "is younger," leaving open whether Pyro counts as an adult even at
    Book 1. Any pre-Book-1 Chronicle set at Kanja 290-308 depicts a child or adolescent, and must be
    treated under the child-safety hard stop: no sexualized content of any kind, and his involuntary
    heat surges under fear (`ARS-421`) written as a child's distress, not a weapon showcase.
18. **The Onyx account.** `VB-062` gives every significant event in Kanja's life an Onyx account;
    `ARS-437` (the Heartline) carries body signals only, and Onyx was sealed at L9 for Pyro's entire
    pre-Book-1 life. No rule says what, if anything, the Dark Ledger logged at Kanja 290, when Kanja
    was 12km away from his son's birth.
19. **Book 1-4 placement.** Apart from the Last Breakfast (`MCD-277`), Book 3's Nelle beats
    (`CC-123`/`126`), and Book 5 (`MCD-097`/`221`/`223`), no Book 1, 2, or 4 role for Pyro is locked.
    The Triad have no locked book-level beat at all.
20. **Corpus silence.** Zero Chronicles mention Pyro or the Triad, though locked Alias Chronicles cover
    Kanja 300-314 (`MCD-493`, `MCD-1472`, `MCD-1477`, `MCD-1252`, `MCD-1255`, `MCD-1022`). Whether
    their silence means he was off the page or absent from the fleet is unstated; a two-ton courser
    and a raptor with a 27-foot wingspan living aboard would be hard to leave out of a scene.

---

## 2. Psychological Profile

Built collaboratively with Abad, not handed to him finished. Draft proposals go here marked
**PROPOSED**, and are corrected in place (not appended-and-superseded) once discussed —
this file always reflects current understanding, not a batch-log history of how we got there.

- **Core wound / formative event:**
- **Defense mechanisms:**
- **Values — what they will not compromise:**
- **How they hold contradiction** (the specific tension that makes them dramatically interesting):
- **Relationship patterns:**
- **What breaks them / their real vulnerability:**
- **Defining emotional throughline** (the equivalent of Lauris's combat-joy, Daba's
  discipline-over-mass doctrine, Arturo's chosen-family-as-answer-to-loss):

**Abad's ruling, verbatim, once given:**

---

## 3. Game Plan

- **Narrator / voice:** (confirm against Voice Bible rules if one is already locked; propose one
  if not, and get it confirmed before drafting)
- **Voice spec, gated (Abad, 2026-10-03):** name the governing voice document(s) and quote the
  rules that bind this series -- `docs/lords-of-cian/voice/voice-bible-definitive.md` (the
  narrator's own sheet, hard constraints, exclusion list) and, for any Onyx-narrated or
  Onyx-voiced passage, `docs/lords-of-cian/voice/voice-progression-sheet.md`, with the Phase
  that governs each entry's in-world age stated explicitly. Every draft gets a voice check
  against this spec (sentence length, articles, tense, naming, verdict register, banned words
  and structures, dialogue 50% rule) before it is presented to Abad; a draft that fails is
  redrafted, not presented with the failures listed. For Onyx, the standing rulings are locked at
  `VB-063`, and `scripts/onyx_voice_check.py` must report PASS on every line for a Phase 4 entry;
  the final test is reading the draft beside the "ONYX:" coda in
  `docs/lords-of-cian/chronicles/chronicle-viii-the-ash-wharf-massacre.md` -- if it is not
  recognizably the same instrument, it is redrafted.
- **Connective-tissue gate, mandatory (Abad, 2026-10-03):** every draft for this series passes
  the third non-negotiable rule in `CLAUDE.md` before it is presented. That means
  `scripts/connective_tissue_check.py` exits 0, an independent reviewer reads the draft against
  every rule the script lists, any changed fact is propagated everywhere it is stated, and the
  draft is presented with a connective-tissue note. The Section 1 findings above must be resolved
  or queued before this gate clears.
- **Pacing convention:** single continuous sequence, or multi-strand (and why — what about this
  character's life/role actually calls for a split)
- **Reserved threads for this series** (deliberately not touched yet, carried over from the
  walkthrough plus anything new identified during profile discussion)
- **Chronicle I candidates** (2-3 pitches, not one pre-committed draft):
  1.
  2.
  3.
- **Abad's pick / direction:**

---

## 4. Chronicle Log

Updated as each wave locks. One line per entry: numeral, title, rule ID, one-sentence summary,
batch number.

-
