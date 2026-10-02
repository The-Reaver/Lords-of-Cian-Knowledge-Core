#!/usr/bin/env python3
"""Batch 345: Fable-model read-only review fixes to the CULT-, ASH-, and
SBD- rule-prefix blocks.

Applies the C2-C12 / E1-E7 items from the review that were cleared for
direct application (pure reconciliation/collision-resolution/stale-
cross-reference fixes against already-locked canon, no new creative
facts). Explicitly skips every NEEDS ABAD item (C1, C9, all ENRICHMENT
items) and E8 (MCD-022's Pyro pronoun, handled by a separate agent) --
none of those IDs are touched here.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Fable-model read-only review of the CULT-, ASH-, and SBD- rule-prefix "
    "blocks in canon-ledger.json against the full live ledger."
)

AMENDMENTS = {
    # C2
    "SBD-041": (
        "The SBD's own file on the Pyro Birth Incident and the Triad's origin "
        "-- authored by informant Shelton Dexton, transmitted to A.M. under "
        "full-transparency posture -- is false in its central claims, not the "
        "truth it replaces. Dexton's account (the Triad raised from birth by "
        "Pyro's mother in her own Shattered Kingdoms homeland, and Kanja's wife "
        "killed by an anomaly-class monster rather than transformed in the "
        "Living Gate containment event) directly contradicts the already-"
        "locked, correct account at MCD-131/132/133 (Pyro's mother is not "
        "dead; she inverted T.D.K.'s Living Gate into a forge and is fused "
        "into its own architecture, no longer dead but transformed). Its one "
        "accurate element -- that Pyro's birth itself was a natural birth, not "
        "a possession or ritual event -- matches MCD-022/132 and is not part "
        "of the error. Dexton reported this in complete good faith, per "
        "CC-140 -- he was himself misled by his own informant network, not "
        "knowingly lying to A.M. The file stands as a documented SBD "
        "institutional error, its source and the reason for the deception "
        "both unidentified, reserved as a future thread for either Archon "
        "Meridian's eventual SBD cleanup or Dexton's own reckoning with "
        "whoever fed him the false account."
    ),
    # C3
    "SBD-021": (
        "SBD's Varruk is rated OMEGA-PRIME threat. Named capabilities: "
        "Pattern-Scouting, Angle-Whisper, Guidance by Refusal, Cadence Break "
        "(renamed from 'Cadence Ruin' to resolve the collision with Onyx of "
        "Oblivion's blade power, ARS-020)."
    ),
    "CC-098": (
        "Varruk's morphology and capabilities: 15% larger than Argentavis "
        "magnificens (~195 lbs, 27.6 ft wingspan, hollow-bone build, the "
        "lightest of the Triad by design rather than weakness). Five "
        "capabilities: Pattern-Scouting (reconstructs a complete strategic "
        "picture from fragmentary observation), Angle-Whisper (projects "
        "compressed geometric certainty -- not words or images -- directly "
        "into a bonded mind), Cadence Break (renamed from 'Cadence Ruin' to "
        "resolve the collision with Onyx of Oblivion's blade power, ARS-020; "
        "disrupts enemy coordination via low-altitude passes and targeted-"
        "frequency screams), Storm-Lane Travel (navigates hurricane-force "
        "weather as express routes), and Guidance by Refusal (communicates "
        "danger by refusing to land on or fly a given path, never by "
        "warning)."
    ),
    "ARS-413": (
        "Extends CC-098/CC-099: Varruk's plumage runs pale cream to "
        "buff-white, deliberately stained rust-orange through iron-rich dust "
        "bathing as intentional scent-masking rather than passive coloring. "
        "His Cadence-disruption vocalization (extends the already-locked "
        "Cadence Break, CC-098) operates at ~200m radius, interfering with "
        "communication and targeting simultaneously. A distinct named "
        "behavior, the Stare: fixing a threat with unblinking intensity, "
        "producing a sensation of being observed at a level deeper than "
        "visual contact -- separate from Angle-Whisper's geometric-certainty "
        "projection. Beneath the resonance-bond with the Triad, Varruk "
        "maintains an everyday vocal register the crew reads: growls signal "
        "danger, purrs signal safety, a specific whine signals detected "
        "deception."
    ),
    "ARS-395": (
        "Sereth Vaul's Green Mark grants him a personal ~30-meter passive "
        "sensory-disruption field -- the Void Wake (renamed from the source "
        "document's 'Cadence Ruin' to resolve a real triple naming collision "
        "with Onyx of Oblivion's blade power and Varruk's disruption ability "
        "(the latter since renamed Cadence Break, CC-098), per the "
        "five-judge fleet's unanimous verdict; consistent with the "
        "Ever-Haunt's own established 'Void-' naming convention: Void-Spore, "
        "Void-Swarm, Void Hound, Void Steed, Void Weaver) -- inside which "
        "electronics, coordination signals, and technological targeting "
        "degrade; he tracks by scent, sound, vibration, and sight alone. "
        "This extends, rather than restates, the already-locked fact that he "
        "can walk inside an Ever-Haunt Anti-Resonance field and remain "
        "functional: his own body now generates a smaller-scale version of "
        "that phenomenon as a byproduct of stable Green Mark integration. "
        "The Talisman of Mao's Shadow-Pulse and the Void Wake are competing "
        "frequencies -- near Sereth specifically, the Sovereign Umbrella's "
        "protections measurably degrade for anyone nearby. His "
        "vulnerability: the Void Wake jams his own senses too, so against a "
        "target with comparable non-technological biological awareness -- "
        "Varruk's Pattern-Scouting/Angle-Whisper (CC-098) specifically -- "
        "the pursuit degrades into a pure endurance contest."
    ),
    # C4
    "ASH-047": (
        "The Black Archives sit at -52,000 ft, a hermetically sealed "
        "obsidian sphere flooded with argon gas and kept by the Blind "
        "Record-Keepers, a cloistered sect of elder initiates under "
        "permanent vows of silence who communicate only by tactile "
        "finger-signing. Three record sets are held there: the Blood "
        "Registers (every active, fulfilled, and breached dynamic contract "
        "since the Sanctuary's founding), the Purge Chronicles (the "
        "uncensored history behind the Council's Neutrality Code), and the "
        "Oblivion Seals (the real names and lineages every sworn Iron Collar "
        "surrendered at recruitment, per ASH-036). All three are physically "
        "recorded on the Cinnabar Ledger, titanium sheets stamped in "
        "cinnabar wax with lineage signets (distinct from Onyx of Oblivion's "
        "Black Ledger, ARS-020/CC-013)."
    ),
    # C5
    "CULT-156": (
        "The Caucus operates from the Deposition Vault, a sealed "
        "administrative complex in the Old Dominion Ruins, and has "
        "maintained an unbroken existence at that site for five millennia, "
        "making it one of the oldest continuously operating institutions in "
        "the Shattered Kingdoms, second in age only to the Null-Walkers' "
        "roughly eleven-thousand-year-old circuit (CULT-108/109)."
    ),
    # C6
    "CULT-140": (
        "The Slab Compact was founded roughly three hundred years ago, "
        "during the Sovereign Trust era, by a small founding generation of "
        "Maw handlers at Maw-7 at Keldane, \"the Keldane Maw\" also called "
        "\"the Slab of Judgment\" (MAW-061) -- a separate venue from "
        "Karkosa's own unnumbered Throat (MAW-060/GEO-003). They discovered "
        "a partial Old Dominion military document in the sealed sub-basement "
        "records room beneath the Maw's older military-installation "
        "foundation, the same room the Null-Walkers' circuit verse "
        "independently records (CULT-118)."
    ),
    # C7
    "CULT-187": (
        "The Keeper cabinets across the seven villages hold genuine Old "
        "Dominion administrative instruments, treated as sacred but not "
        "understood. The primary object is a density-compliance calibration "
        "rod once used to verify T.D.K.'s architects worked to "
        "specification, one piece of an incomplete three-piece Calibration "
        "Array (per CULT-035; the Array remains incomplete, and the "
        "whereabouts of its other two pieces are unestablished). Two of the "
        "seven cabinets also hold Crown-Scar documentation, records (not the "
        "procedure itself) of how T.D.K.'s governance architecture was "
        "embedded in the Verehimu bloodline's biological predecessor, "
        "written in an administrative hand and sealed in dead Drakma. Per "
        "the source material, this is among the most dangerous unlocated "
        "documentation in the Shattered Kingdoms."
    ),
    # C8
    "ASH-046": (
        "The Abyssal Foundation (-30,000 to -75,000 ft) is built as "
        "isolated concentric rings of pressure-forged eclogite (ASH-006), "
        "nitrogen-buffered from the living rock, organized into three "
        "zones: the Stygian Plazas (-35,000 to -45,000 ft, staging grounds "
        "and dormitories for active Iron Collars and retired Strikers) sit "
        "below the Iron Redoubts (-30,000 ft tier, Iron Collar barracks and "
        "trial arenas); the Silent Cloisters (-45,000 to -55,000 ft, "
        "meditation vaults and hyperbaric recovery cells) match the "
        "Abyssal Redoubts training ground already locked at ASH-037; and the "
        "Low Perimeter & Trench Gates (-65,000 to -75,000 ft) anchor the "
        "counter-seismic dampening struts into the continental plate."
    ),
    # C10
    "ASH-001": (
        "Ashkeel is a standalone basalt and eclogite monolith rising from "
        "open ocean, its peak roughly 12,600 feet above sea level and its "
        "foundations descending some 75,000 feet into the crust. It sits "
        "outside all eleven mapped continental regions of the Atlas "
        "(GEO-002), closest to the Lawless Reaches but governed by neither "
        "that region nor any nation."
    ),
    # C11
    "ASH-010": (
        "Roughly three centuries ago, a catastrophic internal betrayal and "
        "near-extinction war among the world's wet-work operatives, fixers, "
        "and intelligence brokers, remembered as the Schism, nearly wiped "
        "out that entire shadow profession -- its decisive campaign, fought "
        "and won by the founding Houses themselves, is remembered within "
        "Ashkeel as the Great Purge (ASH-050 through ASH-056). In its "
        "aftermath, the surviving Council of Strikers claimed and fortified "
        "Ashkeel, declaring it Absolute Neutral Ground."
    ),
    "ASH-054": (
        "House Vhaerlow (the Seat of the Silent Thread) governs acoustic "
        "dampening, internal surveillance, and dark-sector monitoring. "
        "Founder Vesper Vhaerlow's stalker-sect eliminated enemy sentries "
        "in total darkness and silence during the Great Purge. House "
        "Vhaerlow's signature discipline, the Acoustic Void, uses "
        "soft-soled footwraps, sound-suppressing field collars, and twin "
        "kerambits to strike through ventilation ducts without exceeding 5 "
        "decibels. House philosophy: 'Silence is not emptiness; it is the "
        "absolute discipline of withholding speech until commanded.'"
    ),
    "ASH-056": (
        "House Aurelock (the Seat of the Red Hearth) holds the Sovereign "
        "Kept Seat: custodianship of the Black Archives, the Geothermal "
        "Core, and the Purge Key (ASH-048). Founder and the citadel's first "
        "Grand Magistrate, Cassian Aurelock, bound his house to eternal "
        "neutrality after the Great Purge, surrendering all external "
        "commercial contracts to serve as the sanctuary's impartial "
        "keystone. House Aurelock's signature discipline, the Master Seal, "
        "is systemic containment and high-yield thermal weaponry, deployed "
        "solely against internal insurrection or existential external "
        "threats. House philosophy: 'The house must stand though all "
        "within it bleed. Neutrality is paid for in absolute resolve.'"
    ),
    # C12
    "SBD-010": (
        "The SBD's own official case file frames the Pyro Birth Incident as "
        "a Demaron possession narrative in which Pyro's mother died during "
        "the Living Gate event. This is deliberate in-universe "
        "unreliability, not a continuity error (logged as CONFLICT-002 in "
        "the project's early conflict tracker; see MCD-133): MCD-131/"
        "MCD-132, which narrow MCD-022, remain the objective truth. This "
        "official-file framing is distinct from, and separately sourced "
        "to, the later informant account Shelton Dexton transmitted to A.M. "
        "(SBD-041), which is false on different grounds."
    ),
    # E1
    "SBD-043": (
        "SBD-011 -- an in-world SBD asset number/designation, not this "
        "ledger's SBD- rule series -- registered as 'Sinisterblade,' "
        "resolves to Bloodreaver (Torian, Cruor-Kin biology, ARS's own "
        "already-locked Furnace Kit) rather than Valen -- the file's "
        "'Sinisterblade' label is a clerical duplicate error, colliding "
        "with Valen's own correct registry number SBD-008 (likewise an "
        "in-world asset designation, not a ledger rule ID). The dossier's "
        "classification, 'Kinetic Combat Specialist / Blood-Resonance "
        "Enforcer,' its description of an obsessive dedication to arms "
        "mastery, and its note that the subject is protective of "
        "lower-tier HVAH assets and close to 'SBD-001' (an in-world asset "
        "designation for Kanja, not a ledger rule ID) all match "
        "Bloodreaver's already-locked profile directly -- Cruor-Kin "
        "biology running blood near-boiling, the only crew member besides "
        "Kanja physically able to restrain Kanja without being crushed, "
        "and an arms-heavy kit (Temper Maul, Ventspikes, Slagline Chain). "
        "The sequential numbering of this document's asset registry "
        "(SBD-012, also an in-world asset designation -- Ghostwind, "
        "already locked) confirms the SBD-0XX series in this source "
        "catalogues the Avatar/Titan roster generally, resolving this "
        "entry cleanly rather than requiring a new identity."
    ),
    "SBD-042": (
        "The SBD's dossier on 'Subject SBD-014' (an in-world SBD asset "
        "number/designation, not this ledger's SBD- rule series) conflates "
        "two distinct individuals -- Matar (CC-067/102, a 620-year-old "
        "assassin operating through guerrilla mastery and tactical "
        "discipline rather than density) and Aeron Dusane (CC-137, an "
        "unrelated young diplomat and aerial combatant) -- under a single "
        "case file and a single classification, 'Aerial Combat Specialist "
        "/ Social Dynamics Harmonizer.' This is a misattribution error, "
        "not a real dual identity: CC-067/102 remains Matar's whole and "
        "correct profile, untouched. The error is another standing SBD "
        "institutional-reliability thread alongside SBD-041 (the false "
        "Pyro Birth file) and CC-136's overclaimed Sorya confidence "
        "ratings."
    ),
    # E2
    "CULT-030": (
        "Post-containment, the Measurist Guild's Master Surveyor has "
        "decided to offer the True Map to whoever contained T.D.K. as an "
        "institutional-survival bargaining instrument, judging the Guild's "
        "protective network of relationships (the Concordat, the Patient "
        "Caucus) too internally fractured to protect it otherwise. This has "
        "fractured the Guild along a leadership-survival line versus a "
        "'the Map is owed to the King alone' practitioner line; three "
        "senior Annotators are dead, and the Master Surveyor privately "
        "suspects one specific Annotator but has not confronted them. The "
        "True Map's disposition remains unresolved; a second, undisclosed "
        "position within the practitioner faction holds that the Map "
        "should be destroyed rather than handed over. Cross-reference "
        "note: introduces the Domus Inviolate Reader's murder (the "
        "calibration rod taken, the Crown-Scar rubbing confiscated) from "
        "the Concordat's side; new material, not a contradiction of "
        "anything locked; the Domus Inviolate material itself is now "
        "locked at CULT-187 through CULT-190."
    ),
    "CULT-063": (
        "A splinter sect called the Frequency Vigil operates inside the "
        "Pavilion's own institution and has misdirected the natural "
        "philosophy division's research for sixty years, slowing its "
        "approach to the Ten Tongues/Old Dominion construction connection "
        "by roughly two generations. The Pavilion doesn't know the Vigil "
        "exists; the misdirection reads as ordinary dead ends. The "
        "Frequency Vigil itself is now expanded at CULT-169 through "
        "CULT-181."
    ),
    "CULT-133": (
        "The full cult ecosystem originally spanned fourteen dossiers "
        "across three categories, documented across five source-material "
        "batches, and has since been extended by the Domus Inviolate, Slab "
        "Compact, Null Caucus, and Frequency Vigil (CULT-140 through "
        "CULT-193): distributed, uncoordinated maintenance of T.D.K.'s "
        "real, still partly functional infrastructure, carried out by "
        "people who mostly do not know they are maintaining it together, "
        "whose explanations are wrong in their specifics but whose "
        "observations hold up structurally."
    ),
    "CULT-139": (
        "No single actor holds a complete picture of the cult ecosystem. "
        "Fermand has the analytical capacity to assemble the scattered "
        "fragments if he can reach them, but they remain scattered across "
        "eighteen organizations (the fourteen first catalogued plus the "
        "Domus Inviolate, Slab Compact, Null Caucus, and Frequency Vigil), "
        "five nations, and eleven thousand years of oral, written, and "
        "physical record: under floorboards, in harbor sediment, in a "
        "verse tradition that will not be shared, and in a land title "
        "archive where a Meridian Register Keeper-General decodes "
        "fragments alone each night."
    ),
    "ASH-057": (
        "Named individuals: Cord-Master Theron of House Vane and "
        "Arbitrator Sela of House Kestrion sparred a ritual duel-trial in "
        "the abyssal rings at -40,000 ft, opening with the traditional "
        "greeting ('Clear boundary' / 'Open stone'), Theron fighting with "
        "the Arterial Shackle's tungsten cords against Sela's Judicial "
        "Execution shear-work, ending when Theron raised the Universal "
        "Safe-Sign (ASH-035, ASH-040) and Sela halted immediately. "
        "Post-duel aftercare for such trials takes place at the Vapor "
        "Cloister of House Moros, three levels below the trial rings at "
        "-43,000 ft, extending the mandatory-aftercare principle already "
        "locked at ASH-030."
    ),
    "ASH-048": (
        "The Geothermal Crucible (-70,000 to -75,000 ft) powers the "
        "entire monolith via a closed-loop supercritical-CO2 turbine cycle "
        "drawing on 450C mantle-boundary heat, supplemented by the "
        "Hydrostatic Siphons (deep crustal water tables, scrubbed and "
        "routed to the Promenade's bathhouses and the Spire's gardens). "
        "Waste heat vents through the central Updraft Core, driving "
        "Ashkeel's permanent internal air-circulation chimney effect. The "
        "Obsidian Floodgate (ASH-009) is triggered by a single physical "
        "key, the Purge Key, held by the Grand Magistrate (ASH-056) in the "
        "High Spire: turning it breaks the thermal expansion collars at "
        "-75,000 ft, flooding the lowest levels with high-pressure brine "
        "and steam to scour the interior and seal the monolith shut "
        "against an unrecoverable breach."
    ),
    # E3 (+ E6 for ASH-049)
    "ASH-049": (
        "The High Spire (+5,000 to +12,600 ft; the same top vertical tier "
        "ASH-032 calls 'the Obsidian Spires') holds four tiers: the "
        "Pinnacle of Retribution (the Council's apex, the Seven High "
        "Thrones carved from garnet-eclogite, and the mechanical Purge Key "
        "vault); the Chamber of the Bladeless Court (+11,000 ft, the "
        "physical seat of the arbitration already locked at ASH-040/"
        "ASH-041, all weapons banned on pain of defenestration, its Altar "
        "of the First Bond the same white-marble slab named at ASH-041); "
        "the Enclaves of the Seven Veils (+7,500 to +10,000 ft, "
        "extraterritorial embassy compounds under the same sovereignty "
        "rule as ASH-019, bound by the Three Universal Safe-Signs, "
        "matching the two oral tiers and one physical gesture already "
        "locked at ASH-040); and the Sky Terraces & Astral Atriums (+6,000 "
        "to +7,500 ft, formal galas and masquerades, including the Golden "
        "Hour Atrium's glass conservatory)."
    ),
    "ASH-039": (
        "The Basalt Codex is Ashkeel's governing legal text (referenced at "
        "ASH-030, ASH-038), formally the 'Council of Assassins, High "
        "Jurisprudence of the Flesh.' Its Section IV governs dynamic-bond "
        "contracts (the Official Register of Dynamic Bonding), filed under "
        "jurisdiction of the Sanctuary of Ashkeel. A standard registration "
        "records both parties (Dominus of record and Initiate/Pledged of "
        "record, by name, lineage tier, and station), a fixed term "
        "(traditionally three lunar rotations, renewable), and a hard "
        "ceiling of inviolable boundaries the Dominus may never cross "
        "regardless of contract terms: no permanent branding, scarring, or "
        "fracture; no third party introduced without a signed written "
        "addendum; no submersion below Tier IV (-30,000 ft, the fourth "
        "structural tier, the Iron Crucible, ASH-032; distinct from any "
        "intensity-tier usage elsewhere) in uncertified abyssal vents."
    ),
    "ASH-036": (
        "Iron Collar recruitment (ASH-016) proceeds through three Weeding "
        "Trials once a candidate reaches the baseline age of thirty: the "
        "Labyrinth of Desire (72 hours in sensory-saturated pleasure "
        "chambers under psychoactive stimulants, testing total "
        "non-response, any involuntary engagement disqualifies); the Stone "
        "Marrow (a solo 48-hour descent into unmapped geothermal fissures "
        "at -60,000 ft, testing spatial logic and resilience to sensory "
        "deprivation); and the Sovereign Severance (publicly burning "
        "family heraldry, dissolving all existing romantic/dynamic "
        "contracts, and surrendering one's given name to the Council "
        "archive). Passing candidates receive an alphanumeric "
        "strike-cipher (e.g., Sentry Null-Seven) and a welded, keyless "
        "baseline iron neck-band (the Locked Gorget, ASH-038)."
    ),
    # E6
    "ASH-025": (
        "Ars Pulsus, the Kinetic Cadence, is the discipline of rhythmic "
        "impact play. Unlike the other six High Arts, it has no single "
        "governing House or master order; it stands institutionally "
        "unassigned. It classifies impact into four sensory harmonics (the "
        "Sting, the Thud, the Bite, the Flush), enforces absolute "
        "zero-strike zones (the kidney bed T12-L3, the coccyx and spine, "
        "all major joints), and structures a scene in four movements (the "
        "Warming Ripple, the Ascent, the Plateau, the Resolution). Named "
        "implements include the Basalt Flogger, the Obsidian Dragon, the "
        "Honeycomb Paddle, and the Silk Crop."
    ),
    # E7
    "ASH-041": (
        "Contract elevation from Iron Torc to Silver Collar is a formal "
        "rite before the Council in the Chamber of the Bladeless Court, at "
        "the Altar of the First Bond (a white-marble slab, the only pale "
        "stone permitted in the monolith). A House Kestrion Magistrate "
        "confirms both parties hold a clean ledger, then orders the Iron "
        "Torc physically unlocked and removed. An Obsidian Forge-Masters "
        "apprentice presents the Silver Torc (sterling silver and "
        "titanium, no front leash-loop, engraved with the presenting "
        "house's sigil), which the Dominus locks onto the Initiate. A "
        "blood-and-bread rite follows: a drop of the Dominus's blood "
        "sealed into the collar's locking mechanism, a bite of honey and "
        "salt taken without lips touching the metal, and a formal address "
        "elevating the Initiate to Consort of the house. This sequence was "
        "directly illustrated in the Codex using Lord Teodric of House "
        "Vane elevating his Initiate Ennis to Consort, registered and "
        "archived by an Iron Collar scribe (Sentry Null-Nine) in the Black "
        "Archives."
    ),
    "ASH-014": (
        "The seven seats, their governing domains, and their founders: "
        "House Vane (Yvaine Vane), mechanical restraint and structural "
        "security; House Moros (Aurelius Moros), toxicology and apothecary "
        "medicine; House Corvessa (Lysandra Corvessa), espionage and "
        "diplomatic infiltration; House Kragmoor (Torin Kragmoor), "
        "structural engineering and siege defense; House Vhaerlow (Vesper "
        "Vhaerlow), acoustic dampening and stealth; House Kestrion (Idris "
        "Kestrion), arbitration and the Iron Collar command; House "
        "Aurelock (Cassian Aurelock), archive custody and the rock's final "
        "defenses."
    ),
    "ASH-055": (
        "House Kestrion (the Seat of the Cold Scale, ASH-016) governs the "
        "Supreme Court of Arbitration, dynamic-contract registration, and "
        "direct Iron Collar command. Founder Magistrate Idris Kestrion "
        "authored the Basalt Codex's ~1,200 articles, and once sentenced "
        "his own sworn partner to execution for an unnegotiated safe-sign "
        "breach. House Kestrion's signature discipline, the Judicial "
        "Execution, is the formal dual-shear combat doctrine used in "
        "authorized Bladeless Court duel-trials. House philosophy: "
        "'Without explicit boundaries, freedom is merely chaos. Strict "
        "obedience is the only shelter that lasts.'"
    ),
    # E5
    "ASH-026": (
        "Ars Vacui, the Sensory Void, is governed jointly by House "
        "Vhaerlow and House Moros, centered in the Sub-Basalt Wells "
        "(-30,000 to -38,000 ft). It strips external stimuli through three "
        "immersion enclaves: the Cradle of the Tide (magnesium-sulfate "
        "brine pools), the Anechoic Vaults (sound-deadened chambers), and "
        "the Cocoon of the Shadow (dermal restraint suits), and requires "
        "constant vital-sign telemetry with zero unmonitored isolation. "
        "Named gear includes the Vhaerlow Blindfold and the Acoustic Plugs "
        "of Moros. Safety tether is maintained via the Return Thread, with "
        "a mandatory Three-Stage Return triggered if heart rate exceeds "
        "110 or drops below 42 BPM for over two minutes."
    ),
    "ASH-009": (
        "Fire risk gets the same layer-specific treatment. The forges, "
        "tempering kilns, and open-flame conditioning work concentrated in "
        "the Houses' workshops are compartmentalized behind sealed "
        "firebreaks and independent ventilation zones, so a forge fire in "
        "one workshop cannot draw on or spread through the same air system "
        "serving residential tiers. Potable water runs through the "
        "hydrostatic siphons that already intercept deep aquifers before "
        "they reach habitation, and the Obsidian Floodgate remains the "
        "structure's last-resort failsafe, a mechanical purge that can "
        "flood and scour the lowest levels to seal the whole monolith off "
        "from an unrecoverable breach."
    ),
    "ASH-024": (
        "Ars Funis, the Cord & Span, is House Vane's founding discipline "
        "and its master guild is the Guild of the Flushed Tether "
        "(Promenade Tier). It governs rope suspension as a synthesis of "
        "structural engineering and kinetic meditation: cords are "
        "prepared through a four-stage rite (caustic wash, singe and "
        "scrub, beeswax/camellia/clove balm infusion, basalt-kiln "
        "tempering), rated to a minimum 850 lbs static break-strength, and "
        "load is always routed through skeletal anchor points, never soft "
        "tissue, with the pelvic cradle (the Pelvic Saddle) bearing "
        "70-80% of suspended mass. Three classical forms exist: the "
        "Grounded Tether (floor work), the Transitional Cradle "
        "(semi-suspension), and the Flight of the Basalt (full "
        "suspension). The induced trance state is termed Sopor Funis."
    ),
    "ASH-043": (
        "The Grand Promenade (informally 'the Obsidian Spine') spans "
        "nearly a vertical mile between +5,000 ft and sea level, carved as "
        "concentric amphitheater-steps around the Downdraft and Updraft "
        "air cores. It has three tiers: the Ember Galleries (high ateliers "
        "and salons), the Basalt Strand (the great concourse and grand "
        "markets), and the Baths of Forgetting (sub-sea-level hydrothermal "
        "complexes). The Spiral Ramp (the Great Incline) is a 60-foot-wide "
        "connecting concourse with brass-inlaid traffic lanes; the "
        "Heliostat Arches funnel genuine daylight down through optical "
        "shafts; the Hanging Gardens of Myrrh are suspended, "
        "atmosphere-purifying terraces along the cavern walls."
    ),
    "ASH-045": (
        "Four chartered social clubs anchor Promenade nightlife, each with "
        "its own house rule: the Black Mirror (+4,200 ft, high-society "
        "restraint, silent service, no raised voices); the Gilded Knot "
        "(+2,800 ft, suspension-art theater, spectators barred from "
        "touching performers); the House of the Velvet Vise (+1,500 ft, "
        "sensory deprivation and tactile indulgence, mandatory masking at "
        "the door); and the Thermal Baths of Forgetting (sea level, "
        "geothermal communal recovery, no weapons or commerce permitted)."
    ),
    "ASH-008": (
        "Two failure modes the original ventilation design alone would not "
        "catch are handled separately. Warm, humid air from the "
        "geothermal engines meeting cold intake air from the summit would "
        "otherwise condense heavily inside a sealed system, so each "
        "intercooler deck carries dedicated dehumidification alongside its "
        "temperature staging. And geothermal steam and brine run "
        "sulfur-rich, so every metal fitting exposed to it, lock "
        "cylinders, collar hardware, tool alloys, is specified in "
        "corrosion-resistant surgical titanium, tungsten, or blackened "
        "pattern-welded steel rather than plain iron or steel, which is "
        "also why those specific alloys already show up throughout the "
        "Houses' toolwork rather than being a purely aesthetic choice."
    ),
    "ASH-042": (
        "Silver Consort status (elevation from ASH-041) carries specific "
        "legal rights under the Basalt Codex, Section IV, Articles "
        "102-148: treble-damage protection against unauthorized "
        "third-party contact (automatically prosecuted as Assault on "
        "Sanctuary Sovereign Property, triggering an Iron Collar "
        "lethal-arrest warrant); unescorted movement on all public "
        "concourses; and the right to petition a House Kestrion Magistrate "
        "directly at the Bladeless Court, rather than requiring the "
        "Dominus to speak on their behalf. Financially, a Silver Consort "
        "holds independent guild credit (up to 5,000 Obsidian Denarii, the "
        "obsidian-stamped Scrip tokens of ASH-018, per lunar cycle without "
        "patron co-sign) across all four chartered Promenade guilds, "
        "priority commissioning access, and restricted apothecary "
        "dispensation through House Moros without a script. "
        "Diplomatically, a Consort may cast the house's guild-assembly "
        "vote, act as embassy-recognized proxy, witness probationary "
        "contracts, and, when the Dominus is absent, host foreign "
        "ambassadors and seal non-lethal alliances under the house seal."
    ),
}

# E4: category-field normalization
CULT_NETWORK_RANGE = [f"CULT-{n:03d}" for n in range(182, 194)]
ASHKEEL_CAP_RANGE = [f"ASH-{n:03d}" for n in range(23, 58)]


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}

    amended = []
    for rid, new_statement in AMENDMENTS.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        rules_by_id[rid]["statement"] = new_statement
        amended.append(rid)

    recategorized = []
    for rid in CULT_NETWORK_RANGE:
        r = rules_by_id.get(rid)
        assert r, f"missing rule {rid}"
        if r.get("category") == "Cult Network":
            r["category"] = "cult"
            recategorized.append(rid)

    for rid in ASHKEEL_CAP_RANGE:
        r = rules_by_id.get(rid)
        assert r, f"missing rule {rid}"
        if r.get("category") == "Ashkeel":
            r["category"] = "ashkeel"
            recategorized.append(rid)

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule IDs found"

    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({
        "batch": next_batch,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": 0,
        "note": (
            "Fable-model read-only review of the CULT-, ASH-, and SBD- rule "
            "blocks, applied as pure reconciliation/collision-resolution/"
            "stale-cross-reference fixes against already-locked canon, no "
            "new creative facts. Amended 37 rule statements: SBD-041 (the "
            "Dexton account's one accurate element, Pyro's natural birth, "
            "separated out from its false claims); SBD-021/CC-098/ARS-413/"
            "ARS-395 (Varruk's 'Cadence Ruin' renamed 'Cadence Break' to "
            "resolve its collision with Onyx of Oblivion's own blade power "
            "of the same name, ARS-020 -- Onyx's own Cadence Ruin, "
            "untouched everywhere else in the corpus); ASH-047 (the "
            "Ashkeel record medium renamed 'the Cinnabar Ledger' to resolve "
            "its collision with Onyx's Black Ledger, ARS-020/CC-013); "
            "CULT-156 (corrected from 'older than the Null-Walkers' circuit' "
            "to second-oldest, resolving a direct contradiction with "
            "CULT-108's own 'oldest continuously operating cult' claim); "
            "CULT-140 (Maw-7 relocated from 'in Karkosa' to 'at Keldane,' a "
            "separate venue from Karkosa's own unnumbered Throat per "
            "MAW-060/061/GEO-003); CULT-187 (the Calibration Array "
            "corrected from implied-complete to confirmed incomplete, other "
            "two pieces' whereabouts unestablished); ASH-046 (a "
            "depth-direction error, 'above' corrected to 'below,' since "
            "-35,000 to -45,000 ft is deeper than the -30,000 ft Iron "
            "Redoubts tier); ASH-001 ('all eleven mapped Shattered Kingdoms "
            "regions' corrected to 'continental regions of the Atlas,' "
            "since GEO-002's eleven regions span the whole continent); "
            "ASH-010/054/056 (the Schism's founding-Houses campaign named "
            "'the Great Purge,' reconciling it with ASH-050/054/056's own "
            "bare 'the Purge' references); SBD-010 (rewritten to "
            "distinguish the SBD's own official-file Demaron-possession "
            "narrative from the later, separately-sourced Dexton account at "
            "SBD-041, and to fix a stale MCD-022-only citation); SBD-043/042 "
            "(clarified that in-world 'SBD-0NN' asset numbers/designations "
            "are distinct from this ledger's own SBD- rule-ID series); "
            "CULT-030/063/133/139 and ASH-057/048 (stale cross-references "
            "updated to point at material that has since actually locked: "
            "the Domus Inviolate at CULT-187-190, the Frequency Vigil's own "
            "expansion at CULT-169-181, the cult ecosystem's fourteen-to-"
            "eighteen-organization count, a false 'already locked at "
            "ASH-031' claim removed, and ASH-048's Arch-Magistrate/Purge-Key "
            "terminology reconciled with ASH-056's Grand Magistrate); "
            "ASH-049/039/036 (terminology-drift clarifying parentheticals: "
            "the High Spire tied to ASH-032's 'Obsidian Spires,' Tier IV "
            "tied to ASH-032's Iron Crucible, the baseline neck-band tied "
            "to ASH-038's Locked Gorget); ASH-025 (a 'the source material "
            "names' meta-reference reworded to plain in-world prose, "
            "alongside the same fix riding along in ASH-049); ASH-041/014/"
            "055 (three character-name collisions resolved: 'Lord Corren of "
            "House Vane' -> 'Lord Teodric,' his 'Initiate Caelen' -> "
            "'Initiate Ennis,' and 'Julian Kestrion' -> 'Idris Kestrion,' "
            "collision-grepped clean before applying); and eight real-world "
            "proper-noun leaks replaced with in-world equivalents (the "
            "Thread of Ariadne -> the Return Thread; the Archimedean/"
            "Archimedes hydrostatic siphons -> the hydrostatic siphons, in "
            "both ASH-009 and ASH-048; the Hesselbach Saddle -> the Pelvic "
            "Saddle; the Baths/Thermal Baths of Lethe -> the Baths/Thermal "
            "Baths of Forgetting; blackened Damascus steel -> blackened "
            "pattern-welded steel; Obsidian Denarii tied explicitly to "
            "ASH-018's own Scrip-token system). Also normalized the "
            "category field for 12 CULT-182 through CULT-193 rules ('Cult "
            "Network' -> 'cult') and 35 ASH-023 through ASH-057 rules "
            "('Ashkeel' -> 'ashkeel') to match each prefix's own established "
            "lowercase convention. Deliberately left completely untouched: "
            "C1 (the CULT block's T.D.K.-containment-timing question across "
            "16 rules), C9 (ASH-018 vs WC-011 on Scrip circulation), all "
            "ENRICHMENT items, and E8/MCD-022 (handled by a separate agent) "
            "-- all NEEDS ABAD per the review."
        ),
    })

    old_version = float(ledger["ledger_version"])
    ledger["ledger_version"] = str(round(old_version + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(
        f"OK: {len(ledger['rules'])} total rules, "
        f"{len(ledger['batches_completed'])} batches, ledger_version "
        f"{ledger['ledger_version']}, zero duplicate IDs. "
        f"{len(amended)} rule statements amended: {', '.join(amended)}. "
        f"{len(recategorized)} rules recategorized: {', '.join(recategorized)}."
    )


if __name__ == "__main__":
    main()
