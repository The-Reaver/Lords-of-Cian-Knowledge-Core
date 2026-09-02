#!/usr/bin/env python3
"""Batch 42: Long_Mask_Chronicles_Definitive_Edition.docx (Kanja's 284-year
Long Mask disguised period, ages 30-314) -- condensed extraction covering all
67 Tier-1 battles, 10 Tier-2 campaigns, and the ~50-entry Tier-3 ledger."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'Long_Mask_Chronicles_Definitive_Edition.docx' (Google Drive, Lore Vault "
    "folder) -- Kanja Rexmar's 284-year 'Long Mask' disguised period (ages "
    "30-314), covering 67 Tier-1 battles, 10 Tier-2 campaigns, and roughly 50 "
    "Tier-3 ledger entries. Extracted via four parallel background-agent "
    "summarization passes (lines 1-850, 800-1967, 1460-2119, 2100-2514) "
    "followed by manual synthesis, collision-checking, and condensation into "
    "narrative-cluster rules (1-4 source battles/campaigns per rule), "
    "following the same approach used for Twenty_Two_Victories (Batch 41). "
    "Two continuity reconciliations pre-agreed by Abad before drafting were "
    "applied where the relevant scenes appeared: Lauris Letitia's Forged "
    "Triad recalibration (MCD-267) does not overwrite her true origin at "
    "MCD-176 -- Kanja's role is a major rebuild/recalibration extending his "
    "already-locked maintenance-authority relationship (MCD-204), not "
    "original forging; and Fermand Aurelias's post-Citadel resilience "
    "(MCD-268) is locked as trained/conditioned physiology and extreme "
    "mental fortitude, not an inherent biological grant, consistent with his "
    "already-locked baseline at CC-033, with his escape framed as "
    "substantially his own doing rather than a passive rescue. Several "
    "proper-noun collision checks were run against the live ledger before "
    "drafting: 'Commodore Veska' (this document) vs. 'Veska Karth-Ven' "
    "(Lauris's Kares Prime instructor) and 'Admiral Vos' (this document) vs. "
    "'Maret Vos' (locked crew member) are both coincidental homonyms across "
    "unrelated characters/eras, not renamed; the Krael family name across "
    "this document (Dessius Krael II, age 100; Krael III, age 222 and 298) "
    "is locked as an intentional three-generation dynasty descending from "
    "the already-locked Admiral Dessius Krael ('the Gale Straits admiral'); "
    "Stormreaver/Kairo's 'Zephyr-Frame' is read as forged flight equipment "
    "layered onto his already-locked Aero Variant/Falcon-Pack biology, not a "
    "contradiction; and 'the Living Gate's cavern system' (an ancient "
    "Karesian heritage site surveyed by the Trust at age 282) is read as the "
    "same Living Gate later activated as T.D.K.'s containment mechanism at "
    "Pyro's birth (age ~290, MCD-131/132) -- an existing ancient structure "
    "T.D.K. later weaponized, not a separate location, and not a "
    "contradiction of the already-locked birth sequence. All naming/identity "
    "calls above were presented to Abad in-conversation for override before "
    "locking."
)

NEW_RULES = [
    {
        "id": "MCD-246",
        "category": "World Mechanics",
        "statement": (
            "At age 30, Kanja surrendered the Trinity (Mafesto, Onyx, "
            "Obsidian Malice) to the vault at L9 in the Karkosa Complex "
            "under his father's peace deal with the Sovereign Trust, "
            "retaining only the Talisman of Mao, the Aegis-Talisman, and "
            "the Rexmar Machete. The 284-year Long Mask persona that "
            "followed comprised 67 Tier-1 battles, 10 Tier-2 campaigns, and "
            "roughly 50 Tier-3 ledger entries (120+ operations total), "
            "tracked by Onyx as a running seconds-count from the Sovereign "
            "Pier treaty. This extends the already-locked Pre-Awakening "
            "Theatrics System (ARS-310: Forge-Coat, Hymn-Engine, Dead "
            "Drakma Decoys, Smoke-Pots) with its founding logic: the "
            "Talisman of Mao's Blueprint Eye lets Kanja map financial and "
            "legal structures the way he once mapped physical ones, making "
            "'the man' rather than the Trinity the crew's core weapon."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-247",
        "category": "World Mechanics",
        "statement": (
            "First Long Mask operations (ages 31-35): the Unarmed Siege of "
            "Maw-3 (31) freed 12,000 Cestari purely through forged/"
            "legitimate financial and legal pressure, no violence. The "
            "Crucible Market raid (33) is the era's first crew recruitment "
            "-- Torian, later Bloodreaver (Cruor-Kin biology, near-boiling "
            "blood), extracted from an illegal fighting pit; also the "
            "first proof the Talisman's Kinetic Buffer absorbs thermal "
            "energy, not just kinetic. The False Dragon's Wake (35) "
            "establishes the crew's 'legend is the weapon' doctrine and "
            "the Trust's 'Standing Order 44-B' (avoid direct engagement "
            "with BANE-class threats) as the standing reason enemy "
            "commanders negotiate rather than fight -- both recur "
            "throughout the rest of the Long Mask era."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-248",
        "category": "World Mechanics",
        "statement": (
            "Doctrine-establishing operations (ages 36-44): the Phantom "
            "Fleet Action (36) originates Dead Drakma Decoys at naval "
            "scale as a recurring fleet tactic. The Hymn of Saltmarsh (38) "
            "establishes the Hymn-Engine's 'precision beam, not wall of "
            "sound' doctrine as its standard deployment for the next 250 "
            "years. The White Void Duel (40) is the origin scene for the "
            "already-locked Sinisterblade (Valen Valcari, Sinister "
            "Bloodline, age 23 at the time), who publicly tested whether "
            "'the man or the equipment' made the Scourge dangerous and, "
            "having lost, chose to join. The Apprentice's Proof (44) is "
            "Anansi's first solo command (a bureaucratic-forgery armory "
            "raid, executed in half his 72-hour deadline) and establishes "
            "him as the Long Mask's explicit leadership-succession/"
            "redundancy -- 'if the Captain is compromised, the network "
            "survives.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-249",
        "category": "World Mechanics",
        "statement": (
            "Tier-2 Campaign C1, the Dock-Clearing Operations (ages "
            "31-38): four minor port raids (Portside Dockmaster's Office, "
            "Keldane Fish Market, Ashfall Fueling Station, Thornwall "
            "Signal Post) that seeded the Long Mask's three founding "
            "tradecraft pillars -- forged paperwork, economic pressure, "
            "and theatrical chemistry (the Smoke-Pot formula took 7 "
            "attempts) -- running in parallel with the era's named "
            "battles."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-250",
        "category": "World Mechanics",
        "statement": (
            "Pirate Dawn opens (ages 48-52): the Night of Black Sails (48) "
            "is the origin of the Scourge as a literal commercial/visual "
            "brand -- black Dead-Drakma-thread sailcloth flown in the Gale "
            "Straits crescent formation, recognized and surrendered to on "
            "sight without verification. The Boiling Strait (52) is "
            "Bloodreaver's first major naval engagement, reverse-venting "
            "his Furnace Harness to raise a steam plume that overheats an "
            "enemy Blight projector -- establishing 'fight the "
            "environment, not the enemy' as explicit crew doctrine."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-251",
        "category": "World Mechanics",
        "statement": (
            "The Chain Harbor Massacre (age 55) is the crew recruitment of "
            "Anirak, later Blades Fury (Kinetic-Stack Variant, momentum "
            "accumulates with consecutive strikes, Maw-raised since age "
            "12): found mid-mutiny, already freeing captive Cestari by "
            "hand when the fleet arrived. Kanja recruited her by offering "
            "to build weapons for her biology rather than suppress it -- "
            "the Twin Fangs, the Siren's Voice, and the Triform Morning "
            "Star (already locked at ARS-130) are forged here. Establishes "
            "her four-person unit as the first sub-crew loyal to a "
            "lieutenant rather than to Kanja directly."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-252",
        "category": "World Mechanics",
        "statement": (
            "The Fog Bank Gambit (age 62) -- 8 ships running 48 distinct "
            "acoustic/visual signatures to convince a 16-cutter Trust "
            "fleet it faced 30+ vessels -- becomes the Scourge fleet's "
            "standard anti-pursuit doctrine for the next two centuries and "
            "directly explains the Trust's later inability to estimate the "
            "fleet's true size. The Tremor of Vastok (age 70) is "
            "Stormbreaker's (Kaelen, Seismic Variant) recruitment: "
            "Kanja's Talisman (Grounded Bastion) resonated with and "
            "stabilized his uncontrolled gravity output on contact, "
            "letting Kanja offer control instead of suppression ahead of "
            "an incoming Trust containment team -- a recruitment template "
            "('Trust sends containment team, Kanja arrives first, offers "
            "to teach not cage') that recurs at Chain Harbor and the "
            "Breathing Dark."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-253",
        "category": "World Mechanics",
        "statement": (
            "The Coin-Weight Raid (age 78) -- Anansi's forgers produce 4.2 "
            "million 'corrected' Scrip-notes at their officially specified "
            "value and non-violently swap them for the Trust's debased "
            "60%-value notes across 247 settlements -- is the origin of "
            "Kanja's 'Industrial Myth' epithet ('he does not fight the "
            "economy, he corrects the arithmetic'). The Siege of the "
            "Breathing Dark (age 85) recruits Dreadlord (Azar, Stagnant "
            "Variant, involuntary dread-aura), approached unarmed by "
            "Kanja walking into the aura itself; the crew's unifying "
            "equipment philosophy is stated explicitly here for the first "
            "time -- 'he does not suppress, he directs' -- applying "
            "retroactively to Bloodreaver's heat, Stormbreaker's gravity, "
            "and Azar's dread alike."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-254",
        "category": "World Mechanics",
        "statement": (
            "The Meridian Crossing (age 90): the Sovereign Trust commits "
            "its last major naval asset (20 warships under Commodore "
            "Veska -- an unrelated, coincidentally-named Trust officer, "
            "not Lauris's instructor Veska Karth-Ven) against Kanja's 14 "
            "ships in deep water chosen to deny his usual terrain/acoustic "
            "tricks. Six Avatars operating invisibly beneath two decoy "
            "ships disable 7 of 20 ships in 4 minutes without a shot "
            "fired, forcing the Trust's doctrine to pivot from anti-fleet "
            "to anti-personnel targeting -- the strategic shift that makes "
            "the Talisman's later stealth capabilities load-bearing for "
            "the rest of the era."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-255",
        "category": "World Mechanics",
        "statement": (
            "Tier-2 Campaigns C2 (the Southern Sweep, ages 50-70) and C3 "
            "(the Scrip-Correction Campaign, ages 58-80). C2 is a 20-year "
            "settlement-liberation campaign (Brinewell, Coppermouth, "
            "Tideglass, Ashcoral, Windbreak) converting the Scourge brand "
            "into physical infrastructure via a repeatable pattern: "
            "undercut Trust extraction, demonstrate an infrastructure "
            "fix, integrate into the Ghost-Lattice. C3 is the Coin-Weight "
            "Raid's 22-year lead-up: the Mint Intercept (58, corrected "
            "printing plates), the Debt Ledger Raid (65, exposing the "
            "Scrip-Tether debt trap as mathematically unpayable), and the "
            "Bonding House Collapse (72, legal suits bankrupting/settling "
            "three Southern bonding houses) -- together degrading Southern "
            "Scrip-Tether financial infrastructure by roughly 30% before "
            "the Coin-Weight Raid itself."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-256",
        "category": "World Mechanics",
        "statement": (
            "Golden Terror opens (ages 95-105): the Lighthouse Deception "
            "(95) and the Century Mark (100) are minor/status operations; "
            "the Century Mark marks the Talisman of Mao's first explicit "
            "transition from Stage 1 toward Stage 2. The Masquerade of "
            "Ironport (105) opens Part III ('The Golden Terror') with "
            "Kanja infiltrating a Trust gala in his actual gear worn as a "
            "'costume,' stealing a 340-name guest registry and harbor "
            "codes later reused in the Dead Fleet Rises."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-257",
        "category": "World Mechanics",
        "statement": (
            "The Vanishing of Pier 19 (age 110) recruits Voidbreaker (Jax, "
            "Spatial-Displacement Variant, age 22) after he accidentally "
            "folds an entire warehouse depot into a pocket the size of a "
            "tennis ball; equipment forged: Phase-Rippers, Void-Marker "
            "Darts, Null-Cloak. The Dead Fleet Rises (age 120) -- 20 "
            "derelict hulks disguised as a Scourge fleet luring away a "
            "12-warship Trust group for 16 hours while Anansi's team "
            "copies 40 years of Trust financial records -- is the first "
            "trace of the shadow organization operating inside the "
            "Trust's own financial architecture, later confirmed at the "
            "Proxy War (age 305) and tied to Book 1's already-locked "
            "investigation."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-258",
        "category": "World Mechanics",
        "statement": (
            "The Wind That Robbed the Treasury (age 130) recruits "
            "Ghostwind (Sylas, 19, Hollowed Density biology, near-"
            "undetectable), caught after redistributing stolen treasury "
            "funds to 23 settlements over 7 months; equipment: Slipstream "
            "Harness, Wind-Razors, Vane-Compass. The Requiem at Gallows "
            "Bay (age 140) is a full theatrical rescue of 200 political "
            "prisoners, unintentionally filmed by the Trust's own "
            "propaganda crew and later leaked as Scourge recruitment "
            "material. The Blackboard Lesson (age 148) is a purely "
            "humanitarian infiltration -- Kanja personally correcting 47 "
            "cadets' dangerously outdated navigation charts at the "
            "Trust's Naval Academy, later formally adopted."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-259",
        "category": "World Mechanics",
        "statement": (
            "The Parley of the Raptor's Nest (age 155) recruits Stormreaver "
            "(Kairo, aerial biology with the forged Zephyr-Frame flight "
            "harness and Dual-Spectrum Insight Lenses), the only "
            "recruitment achieved through zero violence and initiated by "
            "the recruit's own choice after three years' observation; he "
            "becomes the crew's explicit moral-compass/mediator. The "
            "Archive Fire (age 170) has Ghostwind remove only the physical "
            "locks from sealed Trust archives (leaving the records "
            "themselves untouched), letting suppressed rebellion-era "
            "history spread uncontrollably through academia. The Iron "
            "Carnival (age 185) is a full-theatrical, zero-violence "
            "garrison evacuation at Fort Gallan enabling an 11-hour "
            "unopposed study of new Trust hardware."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-260",
        "category": "World Mechanics",
        "statement": (
            "At the Second Century Mark (age 200), Trust Governor Maren "
            "Tallis negotiates a 12-year truce recognizing the Scourge's "
            "economy has outgrown Trust taxation; this battle is also "
            "where the Talisman of Mao's Stage 2-to-3 transition (the "
            "'Governor's Shackle') is named explicitly for the first "
            "time, with an in-text 114-year countdown to Pi-Awakening "
            "(200+114=314, consistent with the already-locked age-314 "
            "threshold). The Generational Test (age 205) is the first "
            "battle where Kanja, visibly slowed, delegates combat "
            "entirely to an Avatar (Stormbreaker) rather than fighting "
            "himself -- the turning point the text marks as 'from here "
            "forward, the Avatars fought, the Captain directed.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-261",
        "category": "World Mechanics",
        "statement": (
            "The Breath That Broke the Blockade (age 210) recruits "
            "Soulreaver Zora (26, Atmospheric Pressure Variant, "
            "fisherman's daughter), whose grief-driven wind ability is "
            "weaponized into a 60-knot corridor breaking a 20-warship "
            "blockade; equipment forged specifically to let her fight "
            "without needing to grieve: the Scream, Lung-Collapse "
            "grenades, the Gale-Shield. The Cartographer's War (age 215) "
            "counters a Trust attempt to legally erase 47 settlements "
            "(120,000 people) from official maps by distributing superior "
            "charts before the ratification deadline."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-262",
        "category": "World Mechanics",
        "statement": (
            "The Memory Keeper (age 225) is a 12-hour crew-wide "
            "transcription sprint saving 34,000 of 40,000 pages of "
            "Ghost-Lattice archives from a simultaneous 31-location Trust "
            "raid -- this archive becomes explicitly load-bearing for "
            "Book 1's later investigation. The Sleeping Giant (age 240) "
            "is the origin of Kanja's late-era 'immobility as a weapon' "
            "doctrine: alone in a corridor against 12 Branded commandos, "
            "his passive Kinetic Buffer and Bio-Drakma-tempered skeleton "
            "do the work of combat he can no longer physically perform, "
            "explicitly framed as a preview of the eventual Pi-Awakening."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-263",
        "category": "World Mechanics",
        "statement": (
            "The Orphan's Harbor (age 250): Kanja consolidates 220 years "
            "of accumulated war orphans into a permanent sanctuary, "
            "Stormshelter Cove (already locked as Sovereign Trust Domain "
            "territory at MCD-110/MAW-033; this adds physical detail -- a "
            "basalt-cliff, deep-water inlet -- and layers the new "
            "institution onto the existing site without contradicting "
            "it), housing 2,000 children within 5 years. The Orphan's "
            "Harbor becomes the Ghost-Lattice's primary talent pipeline -- "
            "three-quarters of its couriers, forgers, and analysts in the "
            "era's final decades are Harbor graduates."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-264",
        "category": "World Mechanics",
        "statement": (
            "Tier-2 Campaign C4, the Maw Cascade (ages 105-165): a "
            "60-year campaign combining legal/financial pressure with "
            "direct liberation across four Maw facilities -- Maw-4 (105, "
            "insurance-challenge template, 6,000 freed, prompting the "
            "Trust's Maw Preservation Act which permanently closes that "
            "legal avenue), Maw-6 (125, transport interdiction, 4,200 "
            "freed), Maw-11 (140, an inside job using Ghostwind "
            "infiltration and a Hymn-Engine counter-frequency device, "
            "3,800 freed, Anirak's former facility), and Maw-15 (165, "
            "public-pressure campaign via Ezio's published financial "
            "records, 5,100 freed). Total: roughly 19,100 Cestari freed, "
            "dropping the Southern Seaboard's operational Maw count from "
            "12 to 7."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-265",
        "category": "World Mechanics",
        "statement": (
            "Tier-2 Campaign C5, the Blight Tower Raids (ages 108-180): a "
            "sustained campaign against the Trust's Blight Frequency "
            "suppression network -- the Calibration Theft (108, stolen "
            "technical manuals used to redesign the Hymn-Engine), the "
            "Relay Chain Disruption (145, a 0.3-degree antenna "
            "misalignment opening an 18-month, 15km-wide corridor of "
            "reduced suppression), and the Frequency Vaccine (180, "
            "Anansi's portable counter-frequency generator, 47 units "
            "deployed into the water-pump infrastructure of all 47 "
            "protection-economy settlements) -- explicitly framed in-text "
            "as the Talisman of Mao's Blight Immunity function 'expressed "
            "through engineering' at population scale."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-266",
        "category": "World Mechanics",
        "statement": (
            "Tier-2 Campaign C6, the Merchant Accord (ages 80-200): a "
            "120-year campaign transforming the Scourge brand into a "
            "parallel commercial government -- the First Charter (80, 37 "
            "vessels, 15% protection rate vs. the Trust's 40-60% "
            "taxation, elected merchant council), the Tariff War (120, 17 "
            "independent commercial docks built in response to punitive "
            "Trust tariffs, which are repealed within 5 years), the "
            "Currency Standard (155, the Coin-Weight Raid's corrected "
            "Scrip formalized as the alliance's official currency, "
            "~500,000 notes/year), and the Mutual Defense Compact (200, "
            "alongside Governor Tallis's truce) -- converting the "
            "alliance into a full maritime confederation with its own "
            "currency, governance, infrastructure, and defense force."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-267",
        "category": "World Mechanics",
        "statement": (
            "Lauris Letitia's exfiltration (age 260): Lauris, then a "
            "12-year Sovereign Trust field contractor, was identified by "
            "Ezio's intelligence network after her own reports began "
            "revealing she was independently reading the Trust's "
            "containment architecture the way Kanja reads buildings; she "
            "defected cleanly, walking away rather than being extracted "
            "from captivity. In the months after her arrival, Kanja "
            "performed a major recalibration and rebuild of her existing "
            "Forged Triad (Spine of Dagon, Aristocrat) and the Phalanx -- "
            "extending his already-locked role as her equipment's ongoing "
            "maintenance authority (MCD-204) -- rather than forging them "
            "for the first time; her original commissioning of those "
            "weapons remains locked at MCD-176, predating Kanja's birth "
            "by centuries. Attia's Rite is not part of this scene and "
            "keeps its own separately-locked delivery (MCD-204, Era G)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-268",
        "category": "World Mechanics",
        "statement": (
            "Fermand Aurelias's escape (age 270): after nine years of "
            "systematic stress-testing at the Black Iron Citadel, Fermand "
            "-- a pure human with no exotic biology (per the already-"
            "locked CC-033) -- survived through trained physiological "
            "conditioning and extreme mental fortitude developed under "
            "the ordeal, not an inherent biological grant; his 'Baroque "
            "Tongue' speech pattern is confirmed as a self-taught survival "
            "mechanism, not forged. His escape was substantially his own "
            "doing: over three weeks he memorized extraction coordinates "
            "delivered by Ghostwind and destroyed the evidence himself, "
            "meeting Voidbreaker's arrival already composed and prepared; "
            "the Voidbreaker fold served as the assist for the final "
            "physical extraction, not a passive rescue of a helpless "
            "captive. Kanja recruited him onto Ezio's intelligence team, "
            "forging the Palimpsest (memory-blade rapier) and the "
            "Archive-Cask."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-269",
        "category": "World Mechanics",
        "statement": (
            "The Shimmer Incident (age 282) is the first externally-"
            "documented sign of Kanja's body itself changing -- a "
            "light-bending distortion field around him, observed and "
            "measured by a Trust patrol -- as the Governor's Shackle "
            "approaches its final stages; near this same location, a "
            "Trust survey team separately investigates an ancient "
            "Karesian cavern-system heritage site already known as 'the "
            "Living Gate' (the same Living Gate later activated as "
            "T.D.K.'s containment mechanism at Pyro's birth, age ~290 -- "
            "this predates that event and establishes it as a real, "
            "ancient physical location rather than something built from "
            "nothing). The Cestari Overture (age 285) is Red Beard's "
            "(Tarn Cestari) first contact via the Brand-Line, a "
            "multi-year correspondence opening 29 years ahead of his "
            "already-locked Book 1 defection."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-270",
        "category": "World Mechanics",
        "statement": (
            "The Birth of Fire (age 290): Pyro's natural birth and the "
            "Dhar-Kael imprinting bond completing between him and the "
            "juvenile Varkul, Varruk, and Sorya (already locked in "
            "detail) occur with Kanja required to stay 12km away so the "
            "Talisman's output doesn't disrupt the bonding frequencies -- "
            "consistent with, and adding texture to, the already-locked "
            "birth/Living Gate timeline (MCD-022, MCD-131/132). The Last "
            "Lighthouse (age 295) is Kanja's otherwise-inexplicable "
            "capture of the Gilded Lighthouse, whose ancient Living "
            "Drakma cladding resonates with the Governor's Shackle and "
            "eases his weight briefly -- already consistent with the "
            "locked CC-005/MCD-060/061 identification of the Lighthouse "
            "as the future Pi-Awakening site."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-271",
        "category": "World Mechanics",
        "statement": (
            "By the Weight of Years (age 300), Kanja cannot stand unaided "
            "on bad days, and the crew handles a Trust probe entirely on "
            "its own for the first time (Valen impersonating the Scourge "
            "persona). The Proxy War (age 305) is Ezio and Fermand's "
            "discovery that the Sovereign Trust is being covertly "
            "puppeted by an internal shadow organization issuing "
            "'phantom orders' via stolen authorization codes -- the "
            "culmination of the thread first traced at the Dead Fleet "
            "Rises (age 120) and the direct seed of Book 1's already-"
            "locked Sovereignty Summit investigation."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-272",
        "category": "World Mechanics",
        "statement": (
            "The Scourge's Heir (age 308) confirms Pyro's food-based "
            "healing ability (Thermal Variant biology passively infusing "
            "Aethelgard-adjacent healing energy into meals he cooks) as "
            "biologically real, first proven on Ironbane's nerve damage. "
            "By the 314th Year (age 313) the Governor's Shackle sits at "
            "99.9% and the Shimmer's radius has grown to 800m. The Eve of "
            "Awakening (age 314) -- the final Tier-1 battle of the Long "
            "Mask -- has the crew repel a Trust patrol with zero input "
            "from Kanja, closing the era with 'the mask has become the "
            "face.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-273",
        "category": "World Mechanics",
        "statement": (
            "Tier-2 Campaign C7, the Generational Wars (ages 200-280): "
            "four defensive engagements driven by generational turnover "
            "in Trust command, each ending in the incumbent commander's "
            "professional collapse rather than battlefield defeat -- "
            "Commander Vareth's Probe (205, cross-referenced to the "
            "Generational Test), Admiral Torren's commercial blockade "
            "(230, countered by the Harbor Chain), General Brack's inland "
            "campaign against Ghost-Lattice infrastructure (255, "
            "collapsed by an exposed embezzlement scandal), and the "
            "Phantom Orders (275) -- the point at which Ezio and Fermand "
            "first identify the 'parasitic authentication pattern' that "
            "becomes the Proxy War."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-274",
        "category": "World Mechanics",
        "statement": (
            "Tier-2 Campaign C8, the Harbor Chain (ages 230-260), built "
            "in response to Admiral Torren's blockade: the Overland "
            "Connection (232, a 400km interior supply route), the "
            "Independent Port Network (245, expanding to 31 independent "
            "commercial harbors, each fitted with a Frequency Vaccine "
            "pump), and the Sanctuary Harbors (258, three fortified "
            "anchorages designed to shelter the entire merchant fleet, "
            "defended in Trust war-games by a cited subset of ten "
            "Avatars -- not a recount of the already-locked 19-Avatar "
            "total at MCD-140 -- and never activated during the Long Mask "
            "era)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-275",
        "category": "World Mechanics",
        "statement": (
            "Tier-2 Campaign C9, the Shadow Skirmishes (ages 280-310): "
            "four engagements retroactively forming the pattern behind "
            "the Proxy War -- the Karesian Survey Interdiction (282, the "
            "Living Gate cavern-system survey referenced at MCD-269); the "
            "Verehimu Surveillance Operation (290, targeting House "
            "Verehimu, the noble bloodline, not the geographic region "
            "already renamed Voskharen at Batch 40, via credentials from "
            "a Trust official three years dead); the Officer Reassignment "
            "Pattern (298, exposing that competent officers including "
            "Commodore Veska, 'young Krael' (Krael III, per MCD-277), and "
            "Governor Tallis were quietly sidelined rather than "
            "promoted); and the Pre-Positioning (308, Trust assets "
            "repositioning toward the Gilded Lighthouse's coordinates "
            "without the Trust's own knowledge of why)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-276",
        "category": "World Mechanics",
        "statement": (
            "Tier-2 Campaign C10, the Crew's Solo Operations (ages "
            "300-314): three engagements run with zero tactical input "
            "from Kanja, distinct from delegated command -- the Merchant "
            "Escort Action (302, Valen independently executing the "
            "Meridian Crossing deployment model), the Refugee Corridor "
            "(307, Zora, Dreadlord, and Ghostwind relocating 4,000 people "
            "from a Trust forced-labor transport with Kanja learning of "
            "it only afterward), and the Final Patrol (313, the last "
            "engagement before the Eve of Awakening, resolved and "
            "reported to Kanja only after the fact)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-277",
        "category": "World Mechanics",
        "statement": (
            "Tier-3 ledger highlights: the Rat-Catcher's Apprentice (age "
            "96) dates Pyro's mother's joining the fleet as provisions "
            "manager, well before his birth. The Dog Watch (age 248) "
            "places Varruk's first appearance 42 years before the "
            "Triad's bonding with Pyro (~290), consistent with MCD-270's "
            "Birth of Fire dating. The Iron Wedding (198) is Ironbane's "
            "crew-officiated marriage. The Old Admiral's Grandson (222) "
            "is Krael III's back-channel meeting with Kanja, per the "
            "genealogy resolved at MCD-254/MCD-275. The Pyro Incident "
            "(296) is the first observed instance of the Triad's "
            "thermal-management function around Pyro. The Final Forge "
            "(304) is the literal last item Kanja ever personally forges. "
            "The Countdown Annotation (310) gives precise late-stage "
            "figures: Bone-Tempering 99.7% complete, the Governor's "
            "Shackle at 99.7% capacity, voluntary movement at ~15% of "
            "peak, Shimmer visible to 1,200m. The Final Coat Fitting "
            "(312) is Valen's formal fitting for the Forge-Coat as the "
            "era's next legend-bearer. The Last Breakfast (314) closes "
            "the Long Mask on Pyro serving Kanja stew as the Shimmer and "
            "the Gilded Lighthouse's pendant activate."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = (
    'Abad approved the full 32-rule draft as pasted in-conversation, '
    'including all proper-noun collision resolutions (Veska, Vos, Krael '
    'genealogy, Stormreaver/Zephyr-Frame, and the Living Gate cavern-system '
    'identity call) and the two pre-agreed reconciliations (Lauris\'s Triad '
    'recalibration at MCD-267, Fermand\'s trained resilience at MCD-268): '
    '"continue"'
)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 42,
            "source_doc": "Long_Mask_Chronicles_Definitive_Edition.docx (Kanja's 284-year Long Mask period, ages 30-314; 67 battles + 10 campaigns + ~50 ledger entries condensed into 32 rules)",
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 2,
            "conflicts_resolved": 2,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "4.5"
    ledger["last_updated"] = "2026-09-02"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
