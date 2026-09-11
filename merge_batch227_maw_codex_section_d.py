#!/usr/bin/env python3
"""Batch 227: Maw Codex Section D -- the 18 Branded Legends + doctrinal matchup grid,
the ten Banners + the Pits' real scale, the current Iron Council + named Shapers'
methods, deeper Cestari operational depth + the Marker Rebellion/Long Walk + betting
economics depth. Extracted via four parallel background agents reading the full
290,147-character Maw_Codex_Definitive_Edition.docx text, cross-checked against the
full live ledger for collisions before drafting, then consolidated and presented in
full for Abad's approval."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Maw_Codex_Definitive_Edition.docx (Drive fileId 1uKHTHJcZob-4oDPjrd7U0o2Nlu-bGSiv, "
    "702KB, 290,147-char extracted text), Section D full pass via four parallel "
    "background agents, each cross-checking the full live ledger for collisions before "
    "drafting, consolidated and presented in full for approval."
)

BATCH_NOTE = (
    'Abad: "I approve." Closes out the Maw Codex Section D backlog Batch 103 (2026-09-10) '
    "queued for future batches: the 18 Branded Legends (9 of 18 already fully locked via "
    "the Reclamation Chronicle/Apex field, not redrafted), the doctrinal matchup grid's "
    "real percentages (7 of 21 possible pairings quantified in the source, the rest left "
    "unasserted rather than invented), the ten Banners in full, the Pits' real scale, the "
    "current seven-seat Iron Council (Harren Bladesmith already named at MAW-051, six "
    "genuinely new names), named Shapers' methods (fills in method detail behind all 8 "
    "already-name-stubbed Shapers at MAW-051), deeper Cestari operational depth, the "
    "Marker Rebellion/Long Walk in full, and betting-economics depth. Renames: \"Kael the "
    'Undying" -> Kaedrin the Undying (a third distinct Kael would have clustered with '
    'already-locked Kael Stonehand/Kael Threnn); the Marker Rebellion\'s eleven-day gap, '
    '"the Silence" in the source -> the Hush (collided with Decimus Korr\'s already-locked '
    "epithet, MCD-092/CULT-070). Geography ruling, Abad's explicit call: the source's "
    '"Rathaan Tribal Council" (placed in the Shattered Kingdoms) is the same body as the '
    "already-locked Rathaan Federation (Lawless Reaches, POL-090); Lawless Reaches "
    "controls per the standing Atlas-controls precedent, the source's placement was the "
    "error. Silent Mara (a financial-manumission case, source's Manumission section) and "
    "the Branded Legends section's fuller profile of the same figure were independently "
    "found by two agents and merged into one rule (MAW-128) rather than drafted twice. "
    "One item deliberately left unresolved, not papered over: Silent Mara's speculative "
    "Ghost-Lattice tie carries a chronology gap against the Ghost-Lattice's established "
    "Rebellion-era founding; preserved as an explicit in-world hedge, matching the "
    "source's own hedged framing, rather than asserted as fact."
)

NEW_RULES = [
    # --- Branded Legends + doctrinal matchup grid ---
    {
        "id": "MAW-122",
        "category": "doctrinal-matchups",
        "statement": (
            "Extends MAW-025/026. The Doctrinal Matchup Grid: the Maw Codex frames "
            "inter-Pillar competition as governed by \"forty-nine rivalries\" across the "
            "seven Houses, but its own extracted text supplies hard historical win-rate "
            "percentages for only seven of the twenty-one possible unique pairings, plus "
            "one aggregate figure for Selenar's record against the field as a whole -- "
            "the remaining fourteen pairings are not quantified anywhere in the source "
            "and are not asserted here. The seven given: Dravos vs Korrath, 55%/45% -- "
            "Dravos wins if the bout runs long, Korrath wins if the crowd shifts the "
            "referee's scoring before attrition takes hold. Dravos vs Velthari, 48%/52% "
            "-- Velthari's structural kill can end the bout before Dravos's patience "
            "engages, but a Velthari fighter who fails to find the weakness quickly loses "
            "the analytical window to Dravos's endurance. Dravos vs Threnn, 51%/49%, "
            "\"functionally a coin flip\" -- two attrition doctrines colliding produces "
            "the system's longest, most punishing bouts. Korrath vs Velthari, 35%/65%, "
            "Velthari's strongest recorded matchup. Korrath vs Threnn, 52%/48%, the "
            "system's most entertaining matchup by attendance and betting volume -- the "
            "same rivalry dynamic Brennan Ironsong and Gorren the Wall embodied across "
            "seven bouts (MAW-127). Maekar vs Velthari, 58%/42%, Maekar's strongest "
            "recorded matchup and the only environmental effect that consistently defeats "
            "Velthari's structural-reading methodology, per MAW-063's venue-adjustment "
            "framework. Osseren vs Threnn, 38%/62%, Threnn's strongest recorded matchup. "
            "Selenar's record against the field is given in aggregate: the Metamethod's "
            "lowest regular-season win rate of any House (46%) against its highest "
            "championship win rate of any House (67%) -- Selenar loses to aggression and "
            "unfamiliarity and wins against preparation."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-123",
        "category": "legend-draven-first-blood",
        "statement": (
            "Extends MAW-064. Draven the First Blood (House Dravos, second generation "
            "after the Pillar's founding, 3,200x -- Branded Peak by the conditioning "
            "science of his own era -- 67 victories, 0 defeats), ~4,600 years ago, is the "
            "death MAW-064's Dead-Drakma-composite flooring standard exists to prevent. "
            "During his sixty-eighth bout the unreinforced Slab cracked under the "
            "combined density of two fighters both above 3,000x and gave way beneath "
            "them; Draven shielded his opponent's body with his own during the fall. Both "
            "survived the fall itself; Draven died of internal injuries sustained "
            "absorbing the structural debris. T.D.K.'s engineering corps redesigned Maw "
            "construction in direct response -- the standard MAW-064 already locks -- and "
            "it held for three thousand years before requiring upgrade. House Dravos's "
            "oldest ritual, older than any recorded doctrine text: every Dravos fighter "
            "touches the Slab before every bout and says Draven's name."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-124",
        "category": "legend-thessara-void-step",
        "statement": (
            "Extends MAW-119. Thessara Void-Step (House Selenar, founding generation, "
            "2,800x, 143 victories, 12 defeats), ~4,400 years ago, retired to become "
            "Selenar's first Chief Shaper and is the origin point of the technique "
            "Korrith the Scorpion independently rediscovered roughly four thousand years "
            "later -- the rediscovery Vakas recognized as a lineage rather than an "
            "innovation, escalating that Reclamation to 250% in response (MAW-119). "
            "Thessara was blind from age six; Selenar's founding Shaper recognized that "
            "years spent navigating entirely through sound, vibration, and spatial memory "
            "had given her a capacity for environmental analysis sighted fighters could "
            "not replicate. She fought by reading opponents exclusively through "
            "vibrations transmitted into the Slab's surface, determining density, stance, "
            "fatigue, and attack trajectory without any visual information at all. Her "
            "signature technique, the Void-Step -- a lateral evasion triggered by "
            "foot-pressure pattern rather than any visual cue -- became Selenar's "
            "foundational movement drill; four thousand years later Selenar still teaches "
            "it to first-month recruits by having them fight blindfolded."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-125",
        "category": "legend-kaedrin-the-undying",
        "statement": (
            "COLLISION-RENAMED: the source names this figure \"Kael the Undying\"; the "
            "ledger already carries two other Kaels -- Kael Stonehand (House Dravos, "
            "~2,000 years ago, MAW-113) and Kael Threnn, Ozmund's living Shaper (MAW-051, "
            "extended at MAW-146) -- and a third distinct \"Kael,\" the oldest legend in "
            "the system, risks exactly the proper-noun cluster this project's "
            "conventions exist to avoid. Renamed Kaedrin the Undying. Kaedrin the "
            "Undying (Unaffiliated, pre-House-system Cestari, 3,800x, record unknown -- "
            "the Ledger system did not yet exist during his career; oral tradition "
            "estimates 300+ bouts), ~4,000 years ago, is the oldest name in the "
            "Brand-Line, predating the Quiet Table by over three thousand years. He "
            "fought every day for forty consecutive years -- early Maw operations "
            "scheduled multiple daily bouts, and Kaedrin was a permanent rotation "
            "fixture, a body the system could not kill that generated reliable revenue "
            "through sheer survival volume. The Brand-Line's claim that he eventually "
            "stopped fighting because the Maw ran out of willing opponents is flagged "
            "in-world as likely mythologized rather than verified. What is verifiable: "
            "his name is the oldest in Cestari oral tradition, invoked by fighters before "
            "their first bout -- not for protection, but for endurance: \"The Cestari do "
            "not pray for survival. They pray for the strength to keep standing.\""
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-126",
        "category": "legend-essek-nightfall",
        "statement": (
            "Essek Nightfall (House Velthari, 4,400x, Proven at 6,000x, 156 victories, 2 "
            "defeats, two-time Apex Champion), ~1,100 years ago, is remembered for the "
            "silence of his victories: average bout duration twenty-three seconds, "
            "longest ever recorded ninety-one seconds (the Apex final against Gorren the "
            "Wall, extends MAW-116 -- the only opponent whose density could absorb his "
            "structural targeting long enough to force an extended engagement), twenty "
            "of his first thirty career bouts ending under ten seconds. Reckoners "
            "restructured Velthari wagering during his peak specifically because of him: "
            "rather than betting on outcomes he always won, they began offering "
            "bout-duration bets instead -- under fifteen, under ten, under five seconds "
            "-- a permanent, still-active feature of the betting architecture for any "
            "Velthari fighter (see MAW-087)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-127",
        "category": "legend-brennan-ironsong",
        "statement": (
            "Extends MAW-116. Brennan Ironsong (House Korrath, 4,200x, 189 victories, 14 "
            "defeats, Apex Champion once, never faced a Reclamation), ~900 years ago, is "
            "one half of the most famous rivalry in Maw history, against Gorren the Wall "
            "of House Threnn (MAW-116): seven bouts over twenty years, Brennan winning "
            "three and Gorren four, every bout over forty minutes and filling every seat "
            "wherever it was hosted, defining the Korrath-Threnn matchup MAW-122 still "
            "quantifies today. Their seventh and final bout is the single most-attended "
            "event in Maw history: 128,000 spectators at the Grand Maw of Karkosa, an "
            "estimated 200,000 more following via Blight-relay acoustic broadcast. Gorren "
            "won in sixty-eight minutes; Brennan's legs failed before his heart did. He "
            "sat on the Slab, watched the wall walk toward him, and smiled. Gorren "
            "offered his hand. Brennan took it. The crowd's roar registered on seismic "
            "instruments at two separate Maws in neighboring cities."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-128",
        "category": "legend-silent-mara",
        "statement": (
            "Silent Mara (Unaffiliated Cestari, 3,900x, 94 victories, 0 defeats, "
            "disappeared), ~700 years before the present, is the Maw's greatest unsolved "
            "mystery: a Cestari woman who entered the Regional Circuit with no House "
            "affiliation, won ninety-four consecutive bouts across three seasons, "
            "qualified for the Grand Circuit, and vanished the night before her first "
            "Grand Circuit bout. No body was ever found; the Ledger Office's entry for "
            "her ninety-fifth scheduled bout reads only \"No-show. Fighter status: "
            "Unknown.\" The Brand-Line's account holds she escaped via manumission "
            "purchased outright with accumulated Scrip (see MAW-079) with the assistance "
            "of unnamed operatives it calls only \"friends in the dark.\" The source "
            "speculates, explicitly hedged as unconfirmed, that those operatives were "
            "Anansi's Ghost-Lattice network (MCD-240/242). Flagged, not resolved: this "
            "hedge is preserved exactly as hedged in the source, because the chronology "
            "is genuinely uncertain against already-locked material -- Mara's "
            "disappearance is dated ~700 years before the Codex's \"present,\" while the "
            "Ghost-Lattice's established founding falls within Kanja's Rebellion (ages "
            "21-29), and nothing currently locked establishes how many calendar years "
            "separate \"now\" from the Rebellion given the Rex/Mar bloodline's extreme "
            "longevity. Mara's name is the most invoked in the Brand-Line's escape "
            "prayers: Cestari fighters say \"I want to walk like Mara\" -- to leave on "
            "one's own terms, owing nothing, with no one knowing where you went."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-129",
        "category": "legend-three-sisters-of-dravos",
        "statement": (
            "The Three Sisters of Dravos (House Dravos, Cestari-born, branded at birth, "
            "entered Dravos at ages nine, ten, and eleven; densities 4,400x/4,300x/4,100x "
            "eldest to youngest; combined record 487 victories, 23 defeats), ~400 years "
            "ago, are the only sibling champions the Maw has produced, dominating the "
            "Grand Circuit simultaneously for a decade. Their entry created a "
            "matchmaking crisis and a doctrinal paradox (Iron Patience against Iron "
            "Patience implies unlimited bout duration), resolved by Compact ruling that "
            "siblings from the same House cannot be matched against each other in "
            "licensed competition -- the Sisters' Clause, still in effect, invoked "
            "roughly thirty times since. The youngest, recorded only as Kess, won the "
            "Apex Championship at twenty-one, the youngest Apex Champion of the Trust "
            "era, defeating a Velthari champion in a forty-four-minute final whose "
            "structural analysis could never find a weakness Dravos's own conditioning "
            "had already engineered out of her."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-130",
        "category": "legend-kullen-gravedust",
        "statement": (
            "Extends MAW-101. Kullen Gravedust's Memoria doctrine, only named at "
            "MAW-101, in full: before entering the Maw at thirty, he spent sixteen years "
            "as a mortuary technician for House Morvane's patron dynasty (see MAW-140), "
            "processing an estimated 2,000 deceased Branded fighters -- learning, from "
            "the inside, exactly how every doctrine kills. He replicates the exact "
            "cause-of-death sequence of a specific historical fighter against any "
            "current opponent whose doctrinal profile matches closely enough. The effect "
            "is psychological, not physical: an opponent recognizes mid-bout that Kullen "
            "is executing the precise sequence that killed a specific historical "
            "champion of their own doctrine -- and stops fighting Kullen to fight the "
            "proof that their doctrine's failure mode already has a name and a corpse "
            "attached to it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-131",
        "category": "legend-renn-hollow",
        "statement": (
            "Extends MAW-101. Renn Hollow's political dimension, only summarized at "
            "MAW-101, in full: at 3,200x he sits over a thousand points below the "
            "typical Grand Circuit competitor -- statistically incoherent for his "
            "ranking -- and survives because that density was developed at his true "
            "biological ceiling under the Blight-reduced Keldane Hollow (MAW-144) rather "
            "than under standard Tether suppression, so his biology already operates at "
            "maximum efficiency while his opponents' bodies remain artificially capped. "
            "His technique further compensates through House Brekka's hybrid doctrine "
            "(MAW-139) -- fragments of all seven Pillar systems combined "
            "unpredictably, \"like a broken mirror reflecting seven different images "
            "simultaneously.\" The Compact is actively debating reclassifying "
            "Blight-reduced-trained fighters separately, since their biological ceiling "
            "is inherently higher at the same nominal density class; a ruling against "
            "Brekka revokes his qualification outright, while a ruling in Brekka's favor "
            "extends a competitive advantage to every fighter trained in Kanja's "
            "protection-economy territory the Trust-managed system cannot match. If he "
            "advances, the legacy of the Scourge (ARS-310) enters the Apex itself; if "
            "disqualified, the Trust implicitly concedes Tether suppression creates an "
            "unfair competitive environment."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- The Ten Banners + the Pits ---
    {
        "id": "MAW-132",
        "category": "the-banners",
        "statement": (
            "Extends MAW-030. House Vennrik (\"the Forsaken Standard\"), Karkosa's "
            "least prestigious Banner, founded ~180 years ago by Gael Vennrik, a Selenar "
            "Shaper expelled from the Compact for accepting fighters other Houses "
            "condemned as untrainable; his founding insight -- that \"untrainable\" was "
            "only as narrow as the system's own definition of \"fighter\" -- produced "
            "three Provincial Champions in its first decade. Housed in a converted "
            "manufacturing warehouse in Karkosa's outer industrial district. Doctrine: "
            "the Unorthodox -- no fixed style, fighters trained to exploit what they "
            "have, deliberately recruiting fighters standardized conditioning rejects. "
            "Roster: ~40 active fighters -- Cestari, free volunteers, military washouts, "
            "outlaws. Mark: a broken chain link on the inside of the left wrist. "
            "Vennrik's patron was House Verehimu, a minor royal noblesse-oblige gesture; "
            "the patronage lapses when Aethelgard Verehimu is assassinated (MCD-090/091), "
            "leaving Vennrik unsponsored and politically orphaned exactly when Ozmund "
            "needs an institution that won't ask about his bloodline. Extends MAW-146: "
            "Vennrik's Shaper is Kael Threnn, who accepts Ozmund without asking why her "
            "instruments can't measure his density, brands him, and assigns the bout "
            "name Venim, matching CC-014's already-locked name change."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-133",
        "category": "the-banners",
        "statement": (
            "Extends MAW-034. House Sektori (\"the Merchant's Blade\"), founded ~400 "
            "years ago, patronized by the Sektori Banking Consortium -- the Southern "
            "Seaboard's largest Scrip-lending institution -- headquartered above the "
            "Consortium's main vault in Karkosa's financial district. Doctrine: the "
            "Investment -- every fighter a portfolio, every bout a transaction, maximum "
            "return for minimum risk. Roster: ~55 active fighters, exclusively contract "
            "volunteers. Mark: a vertical coin-slash through the right ear. Sektori is "
            "the Maw's wealthiest Banner and does not develop talent so much as buy it; "
            "the Investment doctrine's risk-aversion produces the best win-loss record "
            "of any Banner and, because it forbids the escalating challenges the top 16 "
            "require, zero Apex Champions ever. Extends MAW-101: flagship fighter Ash "
            "Korren \"The Debt\" (4,500x) was acquired from a regional Standard under "
            "Scrip-Tether debt-compliance leverage after his family's estate was seized."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-134",
        "category": "the-banners",
        "statement": (
            "Extends MAW-034. House Durnwall (\"the Frontier Hammer\"), founded ~300 "
            "years ago, patronized by the Durnwall Mining Cooperative, an independent "
            "Keldane-highlands mining consortium, training compound carved into an "
            "active mine shaft -- the Maw's only Banner built from working-class "
            "infrastructure rather than aristocratic patronage, chartered after three "
            "generations of urban Banners scouting away the strongest miners for fees "
            "that enriched the acquiring House alone. Doctrine: the Endurance Grind -- "
            "conditioning through actual mine labor, at industrial scale, without "
            "controlled medical recovery. Roster: ~30 active fighters, almost "
            "exclusively from mining communities. Mark: a pickaxe cross on the back of "
            "the left hand. Extends MAW-101: flagship fighter Corra Deepstrike (4,300x) "
            "still works the morning shift and trains afternoons; she won the Southern "
            "Provincial Proving by outlasting a Dravos Contender across a "
            "sixty-two-minute fight, winning by remaining standing when the Dravos "
            "fighter sat down."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-135",
        "category": "the-banners",
        "statement": (
            "Extends MAW-034. House Aravel (\"the Velvet Fist\"), founded ~250 years "
            "ago by Lady Isenne Aravel, a former stage performer who invested her "
            "entire personal fortune believing the Maw's violence could be elevated "
            "into art; now 72, she personally approves every fighter's visual "
            "presentation and has fired Shapers for producing technically sound but "
            "\"inelegant\" winners. Compound doubles as a performance theatre in "
            "Karkosa's cultural quarter. Doctrine: the Aesthetic -- every bout "
            "choreographed for visual impact; a win that isn't beautiful counts as "
            "failure. Roster: ~35 active fighters, heavily recruited from dance and "
            "acrobatic backgrounds. Mark: a crescent moon beneath the left eye in "
            "silver-pigment scarification. Aravel is Korrath's spiritual descendant at "
            "the Banner tier -- Korrath treats entertainment as a tactical weapon, "
            "Aravel treats it as an end in itself. Extends MAW-101: flagship fighter is "
            "Ysolen \"The Dancer\" (3,400x, 31-11) -- the source names her \"Mirel,\" "
            "already renamed Ysolen at MAW-101/Batch 103 to avoid colliding with Val "
            "Mirel Kareth; this rule preserves that rename rather than reintroducing "
            "the collision."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-136",
        "category": "the-banners",
        "statement": (
            "Extends MAW-031. House Galthorn (\"the Black Ledger\"), founded ~500 years "
            "ago, is the Maw's open secret: every Shaper knows it exists and none knows "
            "who runs it. Doctrine: the Calculus -- every bout a mathematical problem "
            "whose solution is the opponent's death, calculated for the moment "
            "maximizing the patron's return. Roster: ~25 active fighters of unknown "
            "origin, medical records sealed. Mark: a small black dot beneath the left "
            "thumbnail, nearly invisible. Its licensing paperwork is immaculate -- valid "
            "Blood Writ, registered to a vacant Karkosa docklands lot, listing a Shaper "
            "no other Shaper has ever seen. The Compact's leading theory: a front for a "
            "faction within the Sovereign Trust's intelligence apparatus, training "
            "combat-ready operatives through the Maw's pipeline as cover. Four "
            "investigations closed as \"insufficient evidence\"; every investigating "
            "Shaper subsequently retired from the Compact. If Galthorn's hidden patron "
            "connects to the shadow organization behind the Trust's phantom orders "
            "(MCD-271), the Maw system is active infrastructure for that organization, "
            "not merely entertainment."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-137",
        "category": "the-banners",
        "statement": (
            "Extends MAW-032. House Draeven (\"the Second Sons\"), founded ~700 years "
            "ago, funded by rotating patronage among Karkosa's minor noble houses (the "
            "\"Second Sons' Fund\"), quartered in the military quarter beside the "
            "Trust's Officer Academy. Absorbs non-inheriting noble sons and daughters; "
            "fighters compete under assumed names and a blank heraldic shield -- no "
            "family crest -- to shield their families from stigma. Doctrine: the "
            "Discipline -- military-grade conditioning adapted from the adjacent "
            "Academy, formation-fighting principles applied to single combat. Roster: "
            "~45 active fighters, exclusively non-inheriting noble children. Alumni are "
            "disproportionately represented in bodyguard, estate-security, and "
            "private-army command roles. Several of the Unchained Legion's 25,000 "
            "trained elites are Draeven alumni who followed Ozmund because he embodied "
            "their own position -- second sons never meant to matter, given meaning by "
            "a man who rejected the inheritance they were denied; the blank shield "
            "becomes the Legion's ironic emblem."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-138",
        "category": "the-banners",
        "statement": (
            "Extends MAW-034; Rathaan homeland resolved per Abad's explicit ruling. "
            "House Rathaan (\"the Desert House\"), founded ~350 years ago, is the only "
            "Banner chartered outside Trust territorial jurisdiction, under a "
            "dispensation negotiated when excluding its fighters was judged to cost "
            "more in lost revenue than licensing a foreign House cost politically. "
            "Patron: the Rathaan Tribal Council -- confirmed the same body as the "
            "already-locked Rathaan Federation (Lawless Reaches, POL-090); the source's "
            "\"Shattered Kingdoms\" placement is an error, resolved per the standing "
            "Atlas-controls precedent and Abad's explicit ruling (Batch 227). Training "
            "camps are mobile, relocating seasonally, making Rathaan fighters outsiders "
            "everywhere they compete -- a disadvantage (no local crowd support) and a "
            "weapon (nothing for opponents to scout). Doctrine: the Dry Kill -- "
            "dehydration warfare; density-conditioned fighters at ~4,000x require "
            "roughly triple baseline hydration under sustained exertion, and Rathaan's "
            "desert biology manages water loss through adaptations no other House "
            "replicates, most effective against attrition Houses (Dravos, Threnn) that "
            "extend bout duration. Roster: ~20 active fighters, exclusively desert-born "
            "nomads. Mark: three vertical lines on the left cheek, the three water "
            "sources of the Rathaan homeland. Extends MAW-101/MAW-063: flagship fighter "
            "Sahar \"The Drought\" (4,100x) fought a ninety-three-minute Provincial "
            "final against a Threnn siege-fighter who collapsed from dehydration; Sahar "
            "drank a single cup of water afterward to a silent crowd."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-139",
        "category": "the-banners",
        "statement": (
            "Extends MAW-033. House Brekka (\"the Breaker's Yard\"), founded ~120 years "
            "ago, is the Maw's most politically provocative Banner: patronized by the "
            "Keldane Settlement Cooperative, the institutional descendant of Kanja's "
            "protection economy, built into the Stormshelter Cove infrastructure Kanja "
            "himself constructed during the Long Mask (MCD-263). Its fighters wear the "
            "Scourge's own mark openly, worn as a declared statement rather than a "
            "disguise -- the rebellion now has a seat inside the licensed system. "
            "Doctrine: the Second Chance -- fighters who broke contracts, failed other "
            "Houses, or were condemned are deconditioned and rebuilt on fragments of all "
            "seven Pillar doctrines without committing to any, producing unpredictable "
            "combinations. Roster: ~25 active fighters, all second-career. Mark: the "
            "Scourge's mark, worn openly. Positioned to absorb Red Beard's 150,000 "
            "defecting Cestari who want to keep competing under new terms -- the bridge "
            "between the old Maw and whatever it becomes afterward. Extends "
            "MAW-101/MAW-131: qualifier Renn Hollow developed at his true biological "
            "ceiling in the Blight-reduced Keldane Hollow (MAW-144) rather than under "
            "Tether suppression."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-140",
        "category": "the-banners",
        "statement": (
            "Extends MAW-034. House Morvane (\"the Widow's House\"), founded ~600 years "
            "ago, patronized by House Morvane itself -- an ancient funeral-rites "
            "dynasty managing Karkosa's death-tech processing facilities -- quartered "
            "against the capital's largest death-tech plant, beside Karkosa's central "
            "necropolis. Its access to deceased Branded fighters' post-mortem records "
            "(neural residue mapping, bioelectric-potential harvesting, Scrip-value "
            "extraction) gives it a unique analytical advantage: studying how fighters "
            "have died to derive how they can be killed more efficiently. Doctrine: the "
            "Memoria -- fighters train against simulations reconstructed from historical "
            "post-mortem data, learning what would have worked against past champions "
            "rather than what did. Roster: ~35 active fighters, recruited from mortuary "
            "workers, medical students, and death-tech staff. Mark: a small teardrop "
            "beneath the right eye in dark ink. Extends MAW-101/MAW-130: flagship "
            "fighters Kullen Gravedust and Veyren \"The Mourner\" (4,500x, record 68-4, "
            "all four losses to Korrath fighters whose theatrical unpredictability broke "
            "his analytical approach) both embody this doctrine literally, not as tactic "
            "but as how Morvane fighters process combat."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-141",
        "category": "the-banners",
        "statement": (
            "Extends MAW-034. House Tolvari (\"the Iron Cradle\"), founded ~450 years "
            "ago, patronized by the Tolvari clan, a Keldane-highland agricultural "
            "family, headquartered in farmland the compound is deliberately "
            "indistinguishable from. Doctrine: the Long Investment -- fighters acquired "
            "at the youngest permissible age under Trust charter law (twelve), developed "
            "over a ten-year program (nutrition/assessment, foundational conditioning, "
            "doctrinal education across all seven Pillars, competitive preparation) "
            "before ever entering a licensed bout, debuting at twenty-two or twenty-"
            "three with a foundation shorter programs can't match. Roster: ~60 "
            "fighters, largest of any Banner, only ~20 competition-active at a time. "
            "Mark: an oak leaf on the inner forearm. The model's cost is a "
            "fifteen-to-twenty-year return horizon, affordable only because Tolvari's "
            "agricultural wealth is independent of the Maw's boom-bust cycle. Extends "
            "MAW-101: flagship prospect Brennan \"The Oak\" (4,600x, 23-0 across three "
            "Regional seasons) is the current test of whether the model survives the "
            "jump to the Grand Circuit's higher ceiling."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-142",
        "category": "the-pits",
        "statement": (
            "Extends MAW-040. The Pits exist because the licensed system cannot "
            "satisfy actual demand: the Grand Circuit's twelve annual events plus "
            "Regional Circuit schedules produce perhaps 3,000 licensed bouts per year, "
            "against the Compact's own conservative estimate of 50,000-80,000 "
            "unlicensed bouts per year -- the Pits producing ten to twenty times the "
            "violence the licensed system produces, almost all uncounted by the Ledger "
            "Offices. A Pit is any unlicensed combat operation where people fight for "
            "stakes, from a tavern basement to a generations-old permanent institution "
            "paying a local power broker to look away. The Pits cannot be eradicated "
            "because they exist wherever violence and poverty intersect -- in Jicome, "
            "everywhere the Blight-Tether suppresses a population with nothing left to "
            "lose. Red Beard (MAW-121/MCD-084) fought his first bout in a Pit at age "
            "twelve; most Apex Champions trace their careers to a Pit fight that caught "
            "a Shaper's eye."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-143",
        "category": "the-pits",
        "statement": (
            "Extends MAW-040/MAW-142. The Pit ecosystem runs four escalating tiers. "
            "Basement Pits: two to twenty spectators, no formal rules, stakes limited "
            "to personal debts, fighters exclusively local, no scouts, no records -- "
            "invisible and ubiquitous. Circuit Pits: semi-organized, weekly or monthly "
            "cards, capacity 50-500, semi-professional locals, rudimentary win-loss "
            "records for matchmaking -- where talent first becomes visible. Named Pits "
            "(full detail at MAW-144): permanent, reputation-bearing, capacity "
            "500-5,000 -- the Maw's farm league, where House scouts send "
            "talent-evaluators the way a general sends scouts to a frontier; 30+ "
            "victories against mixed opposition can earn a Standard's contract. Blood "
            "Pits: bouts where death is the expected outcome, fighters typically "
            "coerced (debt-bonded, captured outlaws, prisoners of war, erased Cestari). "
            "Full pipeline: Pit Fighter -> Licensed Debut -> Journeyman -> Contender -> "
            "Ranked -> Elite -> Apex Contender -> Apex Champion. The mechanism "
            "connecting the worlds is the scout, whose acquisitions range from a "
            "legitimate contract offer to outright purchase of a Cestari or debt-bonded "
            "fighter. The Compact has attempted to regulate scouting three times in the "
            "last century; each attempt was blocked by Banner patrons arguing "
            "regulation creates a competitive disadvantage -- an argument the Compact's "
            "own analysts concede is mathematically correct and morally indefensible."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-144",
        "category": "the-pits",
        "statement": (
            "Extends MAW-041. The four Named Pits in full. The Crucible Market "
            "(Southern Seaboard, destroyed): an underground operation using "
            "Blight-modified fighters as security, until Kanja fought its entire "
            "security complement as the first combat test of the Forge-Coat V1 "
            "(ARS-347) and recruited the young Thermal Variant fighter who became "
            "Bloodreaver/Torian (MCD-247/ARS-090/CC-040/CC-080); its surviving "
            "operations were subsequently absorbed into Anansi's Ghost-Lattice network, "
            "a second absorption distinct from the network's original seeding. The "
            "Keldane Hollow (Keldane Reach, active): the largest active Named Pit on "
            "the Southern Seaboard, capacity ~3,000 in a natural cave system, operating "
            "under local protection-economy sponsorship; Frequency Vaccine pumps "
            "(MCD-274) keep it Blight-reduced, letting fighters develop at their true "
            "biological ceiling -- the direct source of MAW-131's Renn Hollow "
            "controversy, and where Red Beard's scouts identify Unchained Legion "
            "recruits. The Black Slab (Karkosa, location unknown): the capital's most "
            "notorious Blood Pit, invitation-only, drawing wealthy patrons who want "
            "lethal combat without medical intervention; fighters are debt-bonded "
            "workers, erased Cestari, and reportedly judicially-manipulated prisoners; "
            "death rate ~40% per bout. If prisoners are genuinely fed into it through "
            "manipulation, the same machinery producing the Trust's phantom orders "
            "(MCD-271) may be producing the bodies on its floor. The Ember Circuit "
            "(Shattered Kingdoms, mobile): a travelling operation visiting ~30 "
            "settlements per six-month cycle, each visit a three-day festival -- the "
            "most important social event of the half-year for isolated settlements too "
            "poor for a licensed Maw; where House Rathaan's scouts identify recruits "
            "(its own placement in the Shattered Kingdoms stands independently of the "
            "Rathaan Federation/Tribal Council naming question resolved at MAW-138)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Cestari operational depth ---
    {
        "id": "MAW-075",
        "category": "cestari-operations",
        "statement": (
            "Extends MAW-070. Each of the ~40 licensed Farms produces 200-800 Cestari "
            "per generation. Farm breeding is not selective in the animal-husbandry "
            "sense -- high-density pairs are matched and the Farms accept whatever "
            "biology results, leaving refinement to the Houses' later conditioning. "
            "Breeding pairs are separated immediately after conception; the mother is "
            "returned to the breeding rotation within a single recovery cycle. The "
            "infant's first human contact is the handler who performs the brand "
            "(MAW-076). System-wide, ~3,000-4,000 Cestari enter licensed competition "
            "annually; ~1,200-1,600 die within their first three seasons. Developmental "
            "failure rate: ~35%. The Farms are deliberately run at structural surplus, "
            "suppressing acquisition costs and maximizing House selection flexibility "
            "-- surplus Cestari are reassigned to handler duty (MAW-077), routed to "
            "non-competitive labor, or sold into the general economy."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-076",
        "category": "cestari-operations",
        "statement": (
            "Extends MAW-071. The brand is applied within 72 hours of birth because "
            "the numerical designation must be inscribed before a handler designation "
            "is assigned. Brand and designation are one mark: a heated iron pressed to "
            "the inner left forearm, producing a raised scar incorporating a "
            "four-to-six-digit identifier within the ownership sigil, calibrated to "
            "scar permanently without damaging arm function. It simultaneously serves "
            "as ownership proof, Ledger census record, competitive identifier (bouts "
            "scheduled by number before a name is earned), and a psychological "
            "architecture establishing property status from infancy. Free volunteers "
            "instead take a Choice-Brand -- self-selected, applied at certification -- "
            "distinguishing free fighters legally and commercially, but not physically: "
            "the Slab does not recognize the distinction, and a Choice-Branded fighter "
            "dies at the same speed as a Cestari at the same density. Red Beard never "
            "covered or removed his own brand after choosing his name, on the "
            "principle that it is evidence of what was done to him, and evidence is not "
            "something to destroy."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-077",
        "category": "cestari-operations",
        "statement": (
            "Extends MAW-071. The Handler Hierarchy runs four tiers; handlers are "
            "themselves overwhelmingly Cestari whose conditioning produced "
            "sub-competitive density, whose injuries ended competitive careers, or "
            "whose age degraded them below competitive use. Tier 1, Slab Crews: run "
            "the sixty-second reset cycle between bouts, the only handlers the "
            "audience sees and does not cheer for. Tier 2, Backstage Handlers: manage "
            "tunnels, staging, armories, Triage Stations -- a Grand Maw's event day "
            "requires ~400-600. Tier 3, Farm Handlers (MAW-075): typically the "
            "system's oldest surviving Cestari, transferred once their competitive or "
            "backstage utility declines, processing the next generation that will "
            "replace them. Tier 4, Transport Handlers: operate the barges and convoy "
            "routes between Farms, Houses, and Maws -- the most mobile Cestari in the "
            "system, and consequently the most valuable operatives for resistance, the "
            "exact infrastructure the Quiet Table exploited. Handlers carry only a "
            "numerical \"Handler-\" designation (e.g., Handler-4412, Handler-6019, Red "
            "Beard's parents) rather than a name; an informal name has no legal "
            "standing and disappears when the handler is transferred or dies. The "
            "Brand-Line holds that self-naming is the Cestari's first and most "
            "fundamental act of rebellion -- which is why Handler-4412 and Handler-6019 "
            "remained nameless in life and their son chose his name the day he walked "
            "out."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-078",
        "category": "cestari-operations",
        "statement": (
            "Extends MAW-072. The Brand-Line's four coded methods, in full. "
            "Scarification Coding: positional, directional, and layered -- "
            "sophisticated enough to encode names, locations, dates, and instructions, "
            "though its oldest conventions are lost even to current Cestari, leaving "
            "some scar-messages as unreadable artifacts carried on living bodies. Wall "
            "Inscription: a simplified version via ~200 standardized symbols; the "
            "Keldane Maw's backstage corridors are inscribed so densely the original "
            "stone is no longer visible in places. Ritual Encoding: messages embedded "
            "in pre-fight gestures Shapers dismiss as superstition, taught orally "
            "during low-supervision hours. Transport Relay (MAW-077): the network's "
            "physical backbone -- Keldane Reach to Frontier in ~3 days, the full "
            "Southern Seaboard in ~2 weeks, Southern Seaboard to Shattered Kingdoms in "
            "~6 weeks via the Frontier Maw. The Brand-Line's institutional intelligence "
            "on Shapers, patrons, and administrators is stated to exceed the Compact's "
            "own. It carries resistance coordination directly -- the Quiet Table, the "
            "Ghost-Lattice, the Unchained Legion's recruitment all route through it -- "
            "and functions as the Cestari's living archive, preserving names and "
            "histories the Ledger Offices' records erased."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-079",
        "category": "cestari-operations",
        "statement": (
            "Extends MAW-073. The 3:1 manumission ratio, fixed by T.D.K.'s original "
            "administration and never revised, was deliberately set above the average "
            "Cestari career's actual return of ~1.8:1 -- freedom is mathematically "
            "possible and structurally improbable by design. Maintenance costs accrue "
            "continuously and don't pause during injury recovery, so an injured "
            "fighter accumulates cost with zero offsetting revenue, and the "
            "manumission threshold rises with age faster than an aging, "
            "declining-revenue fighter can close the gap. Fewer than 2% of Cestari in "
            "any generation reach the threshold; the other 98% die in the system, each "
            "death recorded as a closed Scrip-value settlement. Red Beard is one of "
            "fewer than 200 Cestari in five thousand years to reach manumission, "
            "requiring over two hundred years of career revenue. A second path exists "
            "in parallel: paying the lump-sum difference to the threshold outright, a "
            "sum at mid-career typically exceeding most regional Standards' annual "
            "operating budget. Silent Mara (MAW-128) is the system's most famous case "
            "of this financial path; the administration has since raised the lump-sum "
            "overhead twice specifically to make the path harder to walk for anyone "
            "who tries to follow her."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Marker Rebellion / Long Walk ---
    {
        "id": "MAW-083",
        "category": "marker-rebellion",
        "statement": (
            "Extends MAW-074. The Marker Rebellion (~2,100 years ago) was a "
            "coordinated labor refusal, not a violent uprising: ~8,000 Cestari across "
            "seven Southern Seaboard Maws simultaneously refused to enter the Slab. "
            "The refusal held eleven days, collapsing the scheduling infrastructure "
            "entirely -- bouts cancelled, betting markets suspended (MAW-085/086), all "
            "revenue halted -- forcing the patron class to confront that their "
            "investment's productivity was entirely contingent on willing performance "
            "from people they had only ever accounted as property. It broke on the "
            "twelfth day when Trust military forces entered all seven Maws and began "
            "executing non-compliant Cestari at fifty per day, on the Slab, in front "
            "of empty seats, with handlers made to watch; competition resumed on the "
            "thirteenth. The eleven-day gap remains visible in the Ledger Offices' "
            "records only as \"scheduling disruption due to logistical recalibration.\" "
            "The Brand-Line's name for the gap, \"the Silence,\" collides with the "
            "already-locked epithet of Decimus Korr (the Silence, Three Ronin, "
            "MCD-092/CULT-070) and is renamed here to the Hush (collision-checked "
            "clean). Stands alongside the Long Walk (MAW-084) and Kanja's Long Mask "
            "liberations as the three largest resistance operations in Maw history per "
            "MAW-074."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-084",
        "category": "marker-rebellion",
        "statement": (
            "Extends MAW-074. The Long Walk (~600 years ago): Handler-9917, a "
            "Transport Handler (MAW-077/078), spent twenty-three years covertly "
            "mapping every route, storage facility, and exchange point in the Southern "
            "Seaboard's supply chain, then compiled the complete intelligence into "
            "Scarification Code across her own body -- her body as the encoded "
            "document. She engineered her own transfer to the Frontier Maw's depot and "
            "walked out during a shift change, vanishing into the Shattered Kingdoms. "
            "The Brand-Line operatives who received her distributed the full mapping "
            "within six months; three subsequent resistance operations (two "
            "food-distribution networks, one escape route) were built directly from "
            "it. She's believed to have lived ~80 further years after her escape. "
            "Framing note: the Brand-Line's own tradition holds that the Cestari "
            "experienced Kanja's Long Mask liberations as \"the Weather\" -- forces "
            "beyond their control that opened doors they then chose to walk through -- "
            "deliberately declining to credit an outsider's strategy for their "
            "freedom. Red Beard is the sole named exception: he alone knows who built "
            "the doors, and chose to walk through Ozmund's rather than Kanja's, not "
            "because Ozmund's cause was more just, but because Ozmund saw the Cestari "
            "as soldiers rather than victims."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Betting economics ---
    {
        "id": "MAW-085",
        "category": "betting-economics",
        "statement": (
            "Extends MAW-080. The seven revenue streams in full, with mechanism and "
            "share: (1) Gate Revenue, ~15% -- tiered admission, the Trust directly "
            "subsidizing free-access events in depressed regions for social-control "
            "purposes; the most visible stream, the least economically significant. "
            "(2) Betting Revenue, ~40% (MAW-080/086) -- the bouts functionally exist "
            "to generate wagering volume. (3) Sponsorship/Patronage, ~20% -- direct "
            "investment plus indirect prestige-premium return letting an "
            "Apex-producing patron leverage the win into trade agreements and "
            "influence. (4) Fighter Transfers, ~10% (MAW-095). (5) "
            "Merchandising/Likeness, ~8%, concentrated at the top -- Korrath and its "
            "Meritha Consortium patron dominate at ~30% of all Maw merchandise. (6) "
            "Scrip-Transaction Value, ~5% -- every bout generates quantifiable "
            "Scrip-value through the Tether from bioelectric/neural-residue output, "
            "aligning entertainment value with Scrip generation by design. (7) State "
            "Revenue, ~2% of output but a disproportionate share of the Trust's "
            "discretionary governance budget -- the structural reason the Maw has "
            "survived every reform movement: the Trust cannot afford to shut down what "
            "funds the Trust."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-086",
        "category": "betting-economics",
        "statement": (
            "Extends MAW-081. A Reckoner operates under a Trust Revenue Council state "
            "charter requiring demonstrated competency in probability mathematics, "
            "Scrip-accounting, and regulatory compliance, renewable every three years "
            "(shorter than the Blood Writ's five, reflecting betting's higher "
            "corruption risk); payout accuracy below 98% triggers revocation, "
            "collusion is criminally prosecuted with asset seizure. Every licensed Maw "
            "employs 20-200 Reckoners; the Grand Maw of Karkosa employs ~400 on Apex "
            "night. Despite regulation, the profession is the Maw's single most "
            "corruption-prone institution, holding an information asymmetry (medical "
            "records, House training intelligence, bout-contract detail) the Trust has "
            "never fully closed. The Reckoners' Court is the self-governing guild, "
            "independent of but adversarially productive with the Shapers' Compact. "
            "Its central enforcement mechanism is the Sealed Book, a permanent "
            "cross-Maw blacklist containing ~3,400 names over two thousand years; "
            "individual names are never disclosed, only summary statistics, fostering "
            "a decentralized mutual-suspicion surveillance effect since no Reckoner "
            "knows whether a colleague is already in it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-087",
        "category": "betting-economics",
        "statement": (
            "Extends MAW-081; cross-references MAW-063. Odds are set via a "
            "three-factor model unchanged in structure for ~1,800 years: the Ledger "
            "Record (~50%) -- win-loss record, methods of victory, density, injury "
            "history; the Doctrinal Matchup (~30%, MAW-122) -- historical head-to-head "
            "House-doctrine win rate, adjusted for individual deviation; the Venue "
            "Adjustment (~20%, fully detailed at MAW-063). Beyond outcome betting, "
            "four specialized wager classes: Duration Bets (bands from under 30 "
            "seconds to over 30 minutes, pioneered during Essek Nightfall's era, "
            "MAW-126, whose bouts were too short for outcome betting to generate "
            "volume); Method Bets (knockout, joint-collapse, thermal incapacitation, "
            "submission, stoppage, crowd-influenced decision, death -- the "
            "highest-margin product); Sequence Bets (in-bout milestones, tracked by "
            "dedicated Sequence Reckoners at the Grand Maw of Karkosa); Accumulator "
            "Bets (three-or-more consecutive outcomes on one card -- the Common "
            "Tiers' most popular and the Reckoners' most profitable single product)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-088",
        "category": "betting-economics",
        "statement": (
            "Extends MAW-081. The Scrip-Tether's metabolic suppression functions as a "
            "betting-integrity mechanism as much as population control: holding a "
            "fighter to their officially classified density tier makes bout outcomes "
            "statistically predictable, Reckoner odds accurate, and the betting "
            "economy profitable and reliably taxable. This is the specific mechanical "
            "reason Kanja's Long Mask economic operations were so structurally "
            "damaging: wherever the Frequency Vaccine (MCD-274) neutralized Tether "
            "suppression, fighters performed above their official classification in "
            "licensed competition, producing upsets the odds models had no way to "
            "price in, since those models assumed universal Tether suppression as a "
            "baseline input. Kanja did not attack the betting system directly -- he "
            "invalidated the assumption its entire odds architecture was built on."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-089",
        "category": "betting-economics",
        "statement": (
            "Extends MAW-082; cross-references MAW-022. The Osseren Starvation Ring "
            "(~400 years ago): run in coordination with twelve Reckoners across three "
            "Maws, generating ~4.7 million Scrip in fraudulent profits over six years "
            "before the Reckoners' Court broke it; all twelve entered the Sealed Book, "
            "the Compact stripped Osseren's Pillar status, House Morthen was fined the "
            "fraudulent profits plus a punitive multiplier, absorbed within a year by "
            "its pharmaceutical revenue. The Dead Pool (~700 years ago): seven "
            "Banner-tier patrons ran a forty-year betting pool on fighter deaths, "
            "using insider medical intelligence bought from corrupt Shapers and "
            "physicians, broken by a Reckoners' Court auditor's statistical anomaly "
            "detection; all seven patrons convicted and Houses dissolved, two corrupt "
            "Shapers executed on the Slab -- the only recorded instance of the Slab "
            "used for punitive execution of non-Cestari, a precedent never invoked "
            "again. The Tether Arbitrage (~150 years ago): a Reckoner consortium "
            "bribed Tether-management technicians to covertly increase specific "
            "fighters' suppression before bouts, discovered when a manipulated "
            "fighter collapsed with a non-natural metabolic-suppression signature; "
            "fourteen Reckoners Sealed-Booked, three technicians convicted, and the "
            "case brought Tether technicians under the same charter-renewal auditing "
            "as Reckoners and Shapers."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-095",
        "category": "betting-economics",
        "statement": (
            "Extends MAW-080/085; cross-references MAW-101/MAW-131. Transfer fees "
            "follow the Compact Registry's standardized valuation: Base Valuation "
            "(density class x win-loss ratio, adjusted for age/injury), Potential "
            "Premium (a Shaper's subjective assessment of trajectory -- the model's "
            "most disputed element), and House Affiliation Discount/Premium (a "
            "Pillar-origin pedigree premium; an unlicensed-Pit discount for "
            "unverified training; a rivalry premium for a transfer strengthening a "
            "direct competitor). The market's most controversial feature is the "
            "Predatory Transfer: a Standard that spends decades developing a Cestari "
            "fighter can be forced to surrender them when the Cestari's owning "
            "institution accepts a wealthier offer, since the training Standard has "
            "no ownership-law recourse. The Reformist faction's Development Credit "
            "proposal (a proportional fee to the training House regardless of "
            "ownership) remains blocked by Preservationists and the Banner patron "
            "class on market-efficiency grounds. Genuinely new detail extending Renn "
            "Hollow (MAW-131): his acquisition from the Keldane Hollow's Pit circuit "
            "carries a formal Registry notation flag, since his patron (the Keldane "
            "Settlement Cooperative) is not recognized by Trust chartering authority "
            "as a legitimate patronage entity -- a flag that remains permanently "
            "unresolved, since resolving it would force the Compact to formally rule "
            "on the protection economy's legitimacy."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-096",
        "category": "betting-economics",
        "statement": (
            "Extends MAW-080/085. The revenue architecture is a closed circular flow: "
            "audience Scrip enters as gate/wagers/merchandise; the Maw distributes it "
            "as bout purses, betting payouts, tax revenue, and Scrip-transaction value "
            "to the Tether's Central Ledger; Houses reinvest, producing better "
            "fighters and bigger audiences, restarting the cycle -- unbroken for five "
            "thousand years. The flow's structural leak is the Cestari themselves: a "
            "death on the Slab is a total write-off of acquisition/training/"
            "maintenance investment; manumission (MAW-079) is a total loss of all "
            "future revenue their continued competition would have generated -- the "
            "system is optimized to hold each Cestari in the revenue-generating band "
            "as long as biologically possible without crossing the 3:1 threshold, the "
            "engineered function of that ratio. Red Beard's 150,000-Cestari walk-out "
            "registered as the single largest revenue-stream loss in the Maw's "
            "five-thousand-year economic history -- a Scrip-value calculation the "
            "Ledger Offices' actuarial conventions were never built to compute, since "
            "the system had no column for mass, voluntary self-removal. The "
            "architecture's single point of failure is the Tether itself (MAW-088): "
            "if metabolic suppression collapses territory-wide rather than in "
            "isolated protection-economy zones, density classifications become "
            "unreliable, odds meaningless, betting collapses, and the entire revenue "
            "chain -- through to the Trust's own governance funding -- stops "
            "circulating."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Iron Council + Shaper methods ---
    {
        "id": "MAW-145",
        "category": "iron-council",
        "statement": (
            "Extends MAW-053. The current Iron Council, elected eighteen months "
            "prior, is the most politically divided in a generation, splitting 3-3 "
            "with two unpredictable swing votes. Seat 1 (Dravos domain): Harren "
            "Bladesmith (MAW-051/MAW-146), 412, former Dravos Chief Shaper, "
            "Preservationist, the Council's senior voice and the system's most "
            "successful active Shaper -- four Apex Champions trained, his fighters' "
            "survival rate exceeding the institutional average by 31%. Seat 2 "
            "(Korrath domain): Tess Merilow, 218, former Korrath instructor, "
            "Reformist -- entered after a fighter she'd medically flagged died when "
            "her patron overruled the assessment; her tabled-three-times proposal "
            "would grant Shapers absolute medical authority with no patron override. "
            "Seat 3 (Velthari domain): Dorn Keldane, 531, Velthari-trained, "
            "Independent -- the Council's most respected analyst and least "
            "predictable voter, evaluating purely on institutional efficiency. Seat 4 "
            "(Maekar domain): Sera Valorren, 167, Maekar's youngest-ever Council "
            "representative, Reformist -- of the already-locked Valorren patron "
            "family (MAW-026), renounced her family title to satisfy the Compact's "
            "noble-title bylaw, a renunciation legally binding but socially "
            "transparent. Seat 5 (Osseren domain): Kollen Ash, 389, Osseren-trained, "
            "Preservationist -- spent his career rebuilding Osseren's credibility "
            "after its Sable Kin demotion, opposing reform defensively. Seat 6 "
            "(Threnn domain): Commander Allek Greymane, 641, Threnn-affiliated and "
            "connected to the already-locked Greymantle patron dynasty (MAW-026) by "
            "marriage, Preservationist -- the Council's most hawkish voice on "
            "institutional security. Seat 7 (Selenar domain): Lyssa Veradaan, 293, "
            "Selenar-trained, Independent -- of the already-locked Veradaan patron "
            "family (MAW-026), the Council's most effective questioner, dismantling "
            "proposals by exposing hidden assumptions regardless of faction. Voting "
            "blocs: Preservationists (Harren, Kollen, Allek) and Reformists (Tess, "
            "Sera, plus one persuadable Independent) hold three seats each; Dorn and "
            "Lyssa's mutual deadlock currently preserves the status quo."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-146",
        "category": "shaper-methods",
        "statement": (
            "Extends MAW-051. Kael Threnn (\"the Gatekeeper,\" MAW-132): a former "
            "Selenar fighter (42-11) whose career ended in a spinal injury at 28, "
            "inherited command of House Vennrik on founder Gael Vennrik's death. "
            "Doctrine: there is no untrainable fighter, only an untrained Shaper -- "
            "build the program around the fighter's actual biology rather than force "
            "the biology to fit a doctrine. She is Ozmund's Shaper. Harren Bladesmith "
            "(\"the Patient Stone,\" MAW-145 Seat 1): never competed, academy-trained. "
            "Signature Method, the Crucible Rotation: fighters cycle through the Iron "
            "Hold's forty chambers (MAW-025) on a twelve-week rotation increasing "
            "load 2% weekly, gradual enough that fighters don't consciously register "
            "the difficulty -- \"teaching the body to forget that it's working.\" "
            "Issara Korrath (\"the Stage Mother,\" a former Korrath fighter, 88-7, "
            "two-time Provincial Champion), 318: trains Seyra \"the Tempest\" "
            "(MAW-101). Doctrine: narrative conditioning -- every fighter enters with "
            "a scripted three-beat dramatic arc, outcomes never scripted but the "
            "structure trained into instinct; \"a fighter who controls the narrative "
            "controls the crowd, and a fighter who controls the crowd controls the "
            "referee's scoring.\" Signature Method, the Mirror Sequence: fighters "
            "rehearse their opening sixty seconds against their own reflection in the "
            "Storm Hall's Mirror Gallery (MAW-025), synchronized to the specific "
            "venue crowd's acoustic recordings. The Ghost Surgeon (House "
            "Galthorn/MAW-136): identity unverified by any Shaper who has ever met "
            "them; Blood Writ renewals conducted entirely through intermediaries "
            "under an Old-Dominion-era remote-audit exemption the Oversight Division "
            "has failed to overturn in four attempts. Galthorn fighters exhibit a "
            "\"post-doctrinal\" style mapping to no known Pillar doctrine -- the "
            "closest comparison is Velthari efficiency stripped of analytical "
            "structure, suggesting either doctrinal innovation beyond the existing "
            "framework or a tradition predating it. Derra Thenn (\"the Anvil's "
            "Daughter\"), 187: granddaughter of Gorren the Wall (MAW-116), trained by "
            "Threnn's current Chief Shaper Valor Thenn (8,000x Proven, MAW-120). "
            "Doctrine, the Informed Advance: modifies Threnn's blind advance with "
            "limited structural awareness, pre-positioning guard against an "
            "opponent's two or three most likely vectors, reducing wasted absorption "
            "~30% while still advancing. Signature Method, the Wall Walk: fighters "
            "walk at constant pace toward a Dead Drakma wall while struck repeatedly, "
            "the wall standing in for the opponent's resistance -- the lesson being "
            "that reaching the wall is all that matters. Oren Drask (\"the "
            "Butcher,\" formerly House Osseren, now unaffiliated and "
            "Compact-censured), 340: Blood Writ suspended under investigation after "
            "three fighter deaths in forty years, his patron House Morthen (MAW-026) "
            "having pressured compressed conditioning cycles to match a rival's "
            "transfer-market pace; the outcome determines criminal prosecution or "
            "reinstatement with no consequence to Morthen. Seraph Keld (\"the Quiet "
            "Architect\"), 276: recruited young from the Keld intelligence dynasty "
            "(Velthari's patron family, MAW-026), the youngest Blood Writ recipient "
            "in five centuries; trains Torven (MAW-101). Signature Method, the "
            "Decision Tree: a branching tactical map from Selenar's Archive Library "
            "(MAW-025) covering every recorded bout an opponent has fought; she also "
            "runs Keld intelligence operatives observing rival Houses' training -- "
            "not technically prohibited, contested by Reformists as unreplicable "
            "espionage, a ban proposal failed twice, partly voted down by "
            "Preservationist Shapers who benefit from similar patron-network "
            "intelligence themselves. Maja Stormseed (\"the Breaker,\" House "
            "Brekka/MAW-139), 203: a former unaffiliated Pit fighter (31 Pit "
            "victories) discovered at the Keldane Hollow (MAW-144); trains Renn "
            "Hollow (MAW-101/MAW-131). Designed Brekka's hybrid doctrine from lived "
            "Blight-reduced experience rather than institutional study. Signature "
            "Method, the Strip: a four-week deconditioning program eliminating a "
            "fighter's prior House-installed habitual responses before rebuilding "
            "them from fragments of all seven doctrines, producing fighters who "
            "can't be predicted because they aren't running any single program."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collisions with existing ledger: {collisions}"
    assert len(NEW_RULES) == 39, f"expected 39 rules, got {len(NEW_RULES)}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 227,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Maw Codex Section D backlog: 39 new rules covering the "
                "Branded Legends + doctrinal matchup grid (MAW-122-131), the ten "
                "Banners + the Pits (MAW-132-144), the Iron Council + named Shapers' "
                "methods (MAW-145-146), and Cestari operational depth + the Marker "
                "Rebellion/Long Walk + betting economics (MAW-075-079, 083-084, "
                "085-089, 095-096). " + BATCH_NOTE
            ),
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate IDs after merge"
    print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
          f"Batches: {len(ledger['batches_completed'])}.")


if __name__ == "__main__":
    main()
