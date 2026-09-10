#!/usr/bin/env python3
"""Batch 103: Maw Codex fuller pass -- Sections A/B/C/E (the Reclamation Chronicle, venue
tactical profiles, the Four Eras, the Apex field) plus Section D's four ready rules (Pillar
compounds, Pillar patrons, the Blood Writ, the Compact's organs/factions). Resolves G-1/G-2/G-3
contradictions and the naming collisions flagged during drafting, blended logically against
already-locked canon per Abad's authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Maw_Codex_Definitive_Edition_3.docx (Abad-uploaded 2026-09-10), full pass via background "
    "agent read of the complete 290,977-char extracted text, cross-checked against all 31 "
    "already-locked MAW- rules and the full live ledger."
)

BATCH_NOTE = (
    'Abad: "lock Sections A/B/C/E as Batch 103 (20 rules) -- self-contained except MAW-115 needs '
    'G-1 and MAW-013 needs G-2. Section D\'s four drafted rules could ride along or wait. The '
    'larger Section D inventory (Legends, Banners, Iron Council, etc.) would be future batches. '
    'fix the contradictions logically against our Ledger. Blended in logically."'
)

NEW_RULES = [
    # --- Section A: The Reclamation Chronicle ---
    {
        "id": "MAW-013",
        "category": "maw-reclamation",
        "statement": (
            "The Reclamation Records are the Maw's longest continuous historical document. Vargo "
            "Vakas has returned approximately one hundred times in roughly five thousand years, "
            "and every Reclamation is inscribed on the sub-basement walls of the Grand Archive "
            "beneath the Grand Maw of Karkosa, in a continuous chronicle that transitions through "
            "six successive writing systems as the civilizations above it rose and fell. Aggregate "
            "outcomes across the ~100 events: approximately 40 Survival with Honor (champion "
            "Proven), approximately 25 Survival with Silence (title retained, no elevation), "
            "approximately 30 Deaths, and the remainder Exceptions -- the exact Exception count is "
            "not asserted here; the Codex's own tally is internally inconsistent across three "
            "passages and is left open rather than forced to a single figure. Longest Reclamation "
            "bout on record: eleven minutes (the Iron Veil, ~1,200 years ago, MAW-115). Shortest: "
            "eight seconds, against an unnamed early Old Dominion champion whose fraudulent title "
            "was so obvious that Vakas struck once and walked away. Highest Proven elevation: "
            "8,000x (Valor Thenn, ~100 years ago, MAW-023/MAW-120). Three champions are confirmed "
            "to have faced Vakas twice: Graves (died in the second), Ashmark Kren (survived both), "
            "and one unnamed Old Dominion-era champion whose second encounter is recorded only as "
            "\"The Founder returned. The champion did not.\""
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-014",
        "category": "maw-reclamation",
        "statement": (
            "The Reclamation is self-correcting by precedent, not by rule. On at least two "
            "recorded occasions, after killing a champion whose title was fraudulent, Vakas "
            "remained standing on the Slab and demanded the next-ranked contender fight him "
            "immediately -- the post-Haku Reclamation (~2,800 years ago, Graves, MAW-111) and the "
            "Osseren Reclamation (~800 years ago, Gorren the Wall, MAW-116). Both replacement "
            "contenders were Proven, and in both cases the same hour produced the system's worst "
            "failure and its highest recorded elevation to that date, measured by the same judge. "
            "The institutional lesson the Grand Archive draws: when corruption produces a "
            "champion, Vakas removes the corruption and then finds the real one in the same "
            "sitting."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-110",
        "category": "maw-reclamation",
        "statement": (
            "R-1, the First Reclamation (~4,800 years ago). Champion unknown; the Ledger system "
            "did not yet exist and the Grand Archive's earliest inscription is pictographic. "
            "Outcome: Death. The record depicts a large figure standing over a smaller horizontal "
            "figure on a flat surface, hand raised, surrounded by pictographs the Archive's "
            "scholars read as a crowd in silence. No name, no House affiliation, no other detail "
            "survives. R-~15, the First Exception (~4,100 years ago). Champion recorded under the "
            "Archive designation \"The Unnamed Who Stood\" -- no House, no era-verifiable "
            "identity, possibly Cestari. Outcome: Exception, survival, and the first confirmed "
            "Proven elevation in history. The inscription transitions from pictographic to early "
            "Old Dominion script at this entry, dating it to the period when T.D.K.'s "
            "administrative apparatus was formalizing. The record describes a champion who "
            "\"stood when standing was impossible and struck when striking was unthinkable,\" and "
            "notes the Founder's departure with a line translating approximately as: \"The system "
            "has produced one who justifies the system.\" This event created the Exception as a "
            "category -- before it the Reclamation was understood as binary (survive or die) -- "
            "and is the origin point of the Proven tier itself."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-111",
        "category": "maw-reclamation",
        "statement": (
            "R-~40, the Post-Haku Reclamation (~2,800 years ago). The most politically significant "
            "Reclamation on record. The reigning Apex Champion had been installed, not earned, "
            "through an arrangement between three Banner-tier Houses that seized control of the "
            "Grand Circuit Council during the post-Haku institutional vacuum. Vakas did not "
            "escalate, test, or evaluate: he identified the fraud and killed the champion in under "
            "thirty seconds, before a Throat crowd still rebuilding from the Haku war's damage. He "
            "then remained on the Slab and demanded the next contender. Graves (House Threnn, "
            "4,100x, 178-31), ranked second, walked on immediately, still carrying the adrenaline "
            "of having watched the previous champion die, and applied the Inevitable -- advance, "
            "absorb, do not deviate. Vakas Proved him at 5,400x and left. Graves faced Vakas a "
            "second time fifty years later at 5,400x and age seventy-eight, advanced into him "
            "without deviation as he had into everything, and was killed at the nine-minute mark; "
            "the Iron Council's records note that Vakas stood over the body for approximately "
            "thirty seconds before leaving the Slab, the longest pause the Founder has ever taken "
            "after a kill. The system's lesson from R-~40: the Founder's judgment does not respect "
            "political transitions. Governments can change. The standard cannot."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-112",
        "category": "maw-reclamation",
        "statement": (
            "R-~48, Lirra Chain-Singer's Exception (~2,400 years ago). Lirra Chain-Singer (House "
            "Korrath, 3,600x, 201-19), the fighter whose competitive popularity had already saved "
            "the Storm School from post-Haku dissolution, triggered the first Exception of the "
            "post-Haku era and the first recorded escalation beyond the standard 150%. Vakas "
            "escalated to 220%. The bout lasted eight minutes. Lirra fought with chain-weapons "
            "wielded in rhythmic patterns producing audible harmonic sequences, and used sustained "
            "resonance vibration to disrupt the Founder's footing -- the same physics that would "
            "inform the Hymn-Engine's acoustic warfare doctrine roughly two thousand years later, "
            "and a direct technical ancestor of Seyra the Tempest's current-era blade acoustics "
            "(MAW-101). Vakas stopped the fight and spoke two words: \"Keep singing.\" Korrath "
            "inscribed them above the Storm Hall's entrance, where they remain. The doctrinal "
            "significance: entertainment was validated as a genuine form of combat excellence by "
            "the one judge whose approval cannot be purchased. Vakas judged Lirra not despite her "
            "theatricality but because of it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-113",
        "category": "maw-reclamation",
        "statement": (
            "R-~60, Kael Stonehand (House Dravos, competition density unrecorded), ~2,000 years "
            "ago. A textbook Reclamation: no Exception, no escalation, no narrative. Vakas tested "
            "at standard 150% for six minutes; Kael absorbed everything and was Proven at 6,400x. "
            "The Grand Archive's full record reads: \"The champion did not advance. The champion "
            "did not retreat. The champion stood. The Founder stopped.\" The significance is "
            "doctrinal rather than dramatic -- the Iron Patience was validated against the "
            "strongest possible opponent, and Kael took that validation into retirement to write "
            "\"The Patient Stone,\" the curriculum House Dravos still runs two thousand years "
            "later. A Reclamation that produced no spectacle produced the most influential "
            "training text in Maw history. R-~64, Hallen Emberstrike (House Maekar, density "
            "unrecorded), ~1,800 years ago, Proven at 5,600x, Survival with Honor. The first "
            "Maekar champion to face Vakas, and the first deployment of the Forge-Fist -- focused "
            "thermal output capable of softening Dead Drakma armor on contact -- against the "
            "Founder. Vakas absorbed the heat without visible discomfort, but the Grand Archive "
            "records thermal discoloration on the Slab surface beneath his feet after the bout: "
            "Hallen's heat had passed through the Founder's stance into the floor. The body was "
            "unaffected; the floor was not. Maekar's Shapers have studied that thermal-transfer "
            "data for eighteen centuries trying to establish whether a sufficiently intense "
            "Forge-Fist could affect Vakas directly. They have not succeeded, and the open "
            "question is Maekar's primary engine of innovation."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-114",
        "category": "maw-reclamation",
        "statement": (
            "R-~70, Mordecai the Harvest (~1,500 years ago). Mordecai the Harvest (House Osseren, "
            "4,700x, 267-8, four-time Apex Champion) produced the only Reclamation in which Vakas "
            "paused mid-combat to reassess. Osseren's structural-reading doctrine identified a "
            "micro-fracture in Vakas's left tibial plate -- a flaw in the Abyssal Bile "
            "augmentation that no fighter had detected across more than two thousand years of "
            "Reclamations -- and Mordecai struck it with calibrated force producing a stress "
            "cascade the Founder had to physically arrest by shifting his stance. The Grand "
            "Archive's notation: \"The Founder moved his left foot. He had not moved his left "
            "foot in seventeen Reclamations.\" Vakas did not escalate; he stopped the bout and "
            "Proved Mordecai at 7,500x, the highest elevation recorded to that date. Formally "
            "logged as Survival with Honor, borderline Exception. The load-bearing revelation: "
            "Vargo Vakas is not invulnerable. The Abyssal Bile's engineering carries flaws "
            "invisible to standard analysis but detectable through Osseren's structural-reading "
            "methodology. This has been the single most closely guarded item in the Shapers' "
            "Compact's classified archive for fifteen centuries."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-115",
        "category": "legend-iron-veil",
        "statement": (
            "R-~76, the Iron Veil's Exception (~1,200 years ago) -- extends MAW-024. The defining "
            "Reclamation. The Iron Veil (House Velthari, 4,600x, 188-0) faced Vakas with the "
            "Structural Kill refined to its theoretical limit and located the same tibial "
            "micro-fracture Mordecai had found three hundred years earlier (MAW-114) -- the flaw "
            "had not repaired, because Vakas's Abyssal Bile biology resists modification even by "
            "its own regenerative processes. She targeted it; he adapted; she adapted to his "
            "adaptation. The cycle ran eleven minutes, the longest Reclamation bout in history: an "
            "analytical war between a doctrine built to find weakness and a Founder whose "
            "eighteen thousand years had eliminated nearly every weakness available to find. Vakas "
            "escalated to 300%, the highest escalation ever recorded -- at 300% of 4,600x he was "
            "operating at approximately 13,800x against a fighter of less than half that density. "
            "The Iron Veil survived not by matching output but by predicting his movements through "
            "the Slab's vibration patterns and positioning to absorb the minimum possible force "
            "from each strike while sustaining her counter-attack on the fracture. The strategy "
            "was never winning; it was not-losing long enough for the Founder to recognize the "
            "achievement. Vakas stopped and spoke one word -- \"Sufficient\" -- which the "
            "Resonance Dome carried to the entire crowd, and which Velthari inscribed above the "
            "Still Point's entrance. She was Proved at 6,200x, a lower elevation than her "
            "analytical mastery warranted, because Vakas's judgment is biological rather than "
            "meritocratic: the Abyssal Bile resonance unlocks what the body can sustain, and her "
            "body was built for precision rather than density. Her real name was never recorded; "
            "she did not want it known, and Velthari honors this."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-116",
        "category": "maw-reclamation",
        "statement": (
            "R-~84, the Osseren Reclamation and Gorren the Wall (~800 years ago). First bout: "
            "Death. An unnamed Osseren champion, installed through the same bout-rigging machinery "
            "Sable Kin would later expose (MAW-022). Vakas detected the fraud biologically rather "
            "than administratively: the champion's measured density was inconsistent with their "
            "competitive record, indicating victories engineered through opponent suppression "
            "rather than earned capability. He killed the champion in approximately forty seconds. "
            "The Archive's record: \"The Founder tested for authenticity. Found none.\" The death "
            "triggered the Shapers' Compact investigation that Sable Kin's exposure would later "
            "complete -- the Reclamation performing its designed function as quality control on a "
            "corruption that no amount of preparation can survive. Second bout: Gorren the Wall "
            "(House Threnn, 4,900x, 301-14, three-time consecutive Apex Champion), Proven at "
            "7,800x, Survival with Honor. As in the post-Haku Reclamation (MAW-111), Vakas "
            "remained on the Slab and accepted the next contender. Vakas hit Gorren with "
            "everything at 150% for four minutes. Gorren did not move, retreat, change stance, or "
            "counterattack; he absorbed the Founder's strikes the way earth absorbs rain. Vakas "
            "stopped and told the Iron Council: \"That one is honest.\" Gorren retired to Shaping "
            "and trained three subsequent Apex Champions; the Threnn compound's main gate carries "
            "his name, as does the verb -- to \"gorren\" means to stand and take punishment until "
            "the punishment apologizes."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-117",
        "category": "maw-reclamation",
        "statement": (
            "R-~90, Dural the Scarmaker (~500 years ago). Dural the Scarmaker (House Maekar, "
            "4,800x, 212-11, three-time Apex Champion), Proven at 6,800x, Survival with Honor. "
            "Vakas tested at standard 150%; the Forge-Fist's focused thermal output struck the "
            "Founder's torso and was absorbed without visible reaction. Six minutes. Vakas's "
            "assessment to the Iron Council: \"He burns clean,\" which Maekar inscribed at the "
            "Ember Floor's entrance. In the Founder's lexicon \"clean\" means the power is "
            "biological rather than synthetic -- the heat is earned, not engineered, and the "
            "fighter is real. It is the highest compliment available in his vocabulary because it "
            "confirms the exact quality the Reclamation exists to verify. Context: the Shapers' "
            "Compact had previously investigated whether Dural's thermal output constituted "
            "prohibited weapon augmentation and concluded his biology was entirely natural Variant "
            "biology. The Compact could not ban a fighter for being too hot."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-118",
        "category": "maw-reclamation",
        "statement": (
            "R-~94, Ashmark Kren's Exception (~150 years ago). Ashmark Kren (free contractor, "
            "unaffiliated, 4,200x, 156-22, twice Apex Champion non-consecutively) is the only "
            "fighter in Reclamation history to receive the Proven elevation during the bout rather "
            "than after it. Ashmark had won manumission, left the Maw, built a life outside it, "
            "and returned voluntarily as a free contractor -- his stated position being \"The Maw "
            "does not own me. I own the Maw. I choose to be here. The choice is the freedom.\" "
            "Vakas escalated to 200%. At the seven-minute mark the Abyssal Bile resonance "
            "interacted with Ashmark's biology and triggered the Proven cascade mid-fight: his "
            "density spiked from 4,200x to 5,800x in approximately two seconds, producing a "
            "visible shockwave across the Slab, and his next strike was the first blow of the bout "
            "Vakas answered with a defensive response rather than absorption. The Grand Archive "
            "records it in three sentences: \"The champion's mass shifted. The Founder adjusted. "
            "The champion struck. The Founder blocked.\" Ashmark establishes that the Proven "
            "elevation is not a post-Reclamation reward but a biological event the resonance can "
            "trigger under sufficient authenticity and sustained intensity -- and the voluntary "
            "re-entry into a system he had already earned the right to leave may itself have been "
            "the authenticity signal the resonance required. He is also one of only three "
            "champions to face Vakas twice, and the only one to survive both (MAW-013)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-119",
        "category": "maw-reclamation",
        "statement": (
            "R-~96, Korrith the Scorpion's Exception (~180 years ago). Korrith the Scorpion (House "
            "Selenar, 4,600x, 134-9, two-time Apex Champion), Proven at 7,200x, Exception, Vakas "
            "escalated to 250%, nine minutes. Korrith's competitive innovation was compressing the "
            "Metamethod's assessment window from thirty seconds to roughly five by attacking "
            "during the analysis and reading the opponent's response to pressure as live "
            "diagnostic data. In the Reclamation he redirected a Founder-weight strike by reading "
            "the Slab's vibration pattern and predicting its trajectory before it arrived -- the "
            "identical technique Thessara Void-Step pioneered four thousand years earlier, which "
            "Vakas recognized as a lineage rather than an innovation, and which the Archive notes "
            "as the reason for the escalation. The Archive's notation: \"The champion heard what "
            "the Founder's feet told the stone. The stone remembered.\" Korrith spent his "
            "retirement building an analytical database that expanded Selenar's Archive Library by "
            "roughly 40%."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-120",
        "category": "living-legend-valor-thenn",
        "statement": (
            "R-~98, Valor Thenn's Proving (~100 years ago) -- extends MAW-023. Valor Thenn (House "
            "Threnn, 4,900x -- the absolute Branded Peak ceiling -- 198-6, three-time Apex "
            "Champion), Proven at 8,000x, Survival with Honor, standard 150% engagement. For seven "
            "minutes the densest non-synthetic fighter in Maw history walked toward the densest "
            "synthetic entity in the world, applying the Inevitable; neither stopped, neither "
            "retreated. The Slab cracked twice during the bout, the combined output exceeding the "
            "Throat's 15,000x specification for the first time in that venue's operational "
            "history. Vakas stopped; no words were recorded. At 8,000x Valor occupied a range the "
            "density-tier taxonomy had not anticipated -- heavier than Proven, lighter than "
            "Synthetic Apex -- and the Shapers' Compact created the \"Upper Proven\" designation "
            "for him. His retirement was forced by a knee injury in his 199th bout, a "
            "joint-collapse inflicted by an Osseren specialist targeting the one structural "
            "weakness 8,000x cannot eliminate: the knee is still a joint, even at the top of the "
            "world. He is approximately 130 years old, alive, and serves as House Threnn's Chief "
            "Shaper -- at 8,000x even diminished by age and injury, one of the most dangerous "
            "non-Titan entities on the planet, and, through Threnn's Ferrenhall-block patron "
            "connections to Trust military command, a potential adversary or ally depending on how "
            "the political landscape shifts."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-121",
        "category": "character-red-beard",
        "statement": (
            "R-~99, Red Beard's Proving (~50-80 years ago) -- extends MCD-084. Red Beard / Tarn "
            "Cestari (unaffiliated Cestari, public 4,800x, 247 victories, the longest career in "
            "recorded Maw history), Proven at 7,000x, Survival with Honor, approximately five "
            "minutes at standard 150%. He faced the Founder at the Throat, not the Slab of Maw-7 "
            "where his parents, Handler-4412 and Handler-6019 of the Quiet Table, had been "
            "executed (MCD-084) -- the Reclamation is held exclusively at the Throat per MAW-013. "
            "He fought with no doctrine -- with the accumulated weight of two centuries inside the "
            "machine, and with density earned across two hundred years of honest labor on the Slab "
            "rather than technique. Vakas stopped; no words were recorded. The crowd of 120,000 at "
            "the Throat produced an acoustic response that the Resonance Dome amplified into a "
            "physical phenomenon, registered by the seismic instruments at the Keldane Maw roughly "
            "400 kilometres away. The Brand-Line carried the news within hours: the son of the "
            "handlers who fed the hungry had been judged by the Founder and found worthy. What the "
            "Brand-Line does not carry, and what only Ozmund and Red Beard know, is that the "
            "Proving was the beginning rather than the end -- the 7,000x elevation broke the "
            "Blight-Tether's artificial ceiling, and Ozmund's subsequent secret training pushed "
            "him through the broken ceiling to 16,000x and climbing (MCD-084). When he walks "
            "150,000 Cestari out of the Maw, the world will believe a 4,800x legend is leading the "
            "march, and will be wrong by a factor of more than three."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Section B: Venue tactical profiles ---
    {
        "id": "MAW-063",
        "category": "venue-tactical-profiles",
        "statement": (
            "The Grand Maws are not interchangeable. Each venue's architecture, climate, crowd "
            "demographics, and acoustics create a competitive environment that favors specific "
            "doctrines and punishes others, and Reckoners formally weight this as the Venue "
            "Adjustment (roughly 20% of the odds calculation, MAW-081). The seven named venues' "
            "profiles: The Throat (Grand Maw of Karkosa) -- acoustic amplification via the "
            "Resonance Dome. Favors Korrath (crowd energy as a weapon) and Maekar (the Dome's heat "
            "retention raises ambient temperature). Punishes Velthari (acoustic interference "
            "disrupts structural reading) and Selenar (the Dome's overwhelming stimulus overloads "
            "the Metamethod's analysis phase). The Mother (Maw-1, Lawless Reaches) -- elliptical "
            "Slab geometry plus permanent humidity. Favors mobile fighters (the long axis) and "
            "Maekar (thermal biology evaporates accumulating moisture). Punishes Rathaan (humidity "
            "violates their dehydration adaptation) and stationary fighters (the short axis is a "
            "trap). The Slab of Judgment (Maw-7, Keldane) -- intimate scale, small and highly "
            "knowledgeable crowd. Favors technical fighters, particularly Velthari and Osseren, "
            "because the crowd rewards precision. Punishes theatrical fighters; the Keldane crowd "
            "sees through performance. The Teeth (Maw-12, Frontier) -- political tension, "
            "passionate crowd, standing riot risk. Favors fighters carrying political symbolism "
            "(Trust-versus-Shattered-Kingdoms narratives) and psychological warriors. Punishes "
            "fighters who need controlled environments. The Belly (Maw-3, subterranean) -- "
            "enclosed space, reverberant acoustics, claustrophobic. Favors Threnn (confined "
            "advance) and Dravos (attrition in limited space). Punishes Korrath (no room for "
            "theatrical movement) and Rathaan (no environmental heat advantage). The Drowning "
            "Floor (Maw-15, coastal) -- water level varies mid-bout. Favors adaptive fighters, "
            "especially the Selenar Metamethod, which thrives on environmental disruption, plus "
            "anyone with aquatic conditioning. Punishes density-dependent fighters, because water "
            "reduces traction for heavy-footed styles. The Scar (Ash Maw, Lawless Reaches) -- "
            "unregulated, no medical mandate, partially ruined, its surrounding territory held by "
            "whichever regional power currently controls it. Favors survivors, particularly "
            "fighters from Pit backgrounds, and Brekka's hybrid doctrine. Punishes fighters "
            "dependent on institutional protections, regulated bout conditions, and predictable "
            "environments."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-064",
        "category": "venue-construction",
        "statement": (
            "Extends MAW-062. Slab construction follows the specification T.D.K.'s engineering "
            "corps issued after Draven the First Blood's death (~4,600 years ago), when the "
            "combined density of two fighters above 3,000x cracked an early Maw's unreinforced "
            "floor: Dead Drakma composite layered over basalt bedrock, rated for sustained density "
            "loads to 5,000x. Grand Maws hosting Grand Circuit events upgrade to 10,000x; the "
            "Throat alone is triple-layered composite over volcanic basalt rated to 15,000x, the "
            "only specification in the world accounting for a Density Spike event occurring during "
            "competition. The Slab surface is treated with a mineral compound that absorbs blood "
            "and biological debris to prevent footing degradation, refreshed between bouts by a "
            "handler crew working a sixty-second sweep-treat-confirm-clear cycle whose efficiency "
            "is one of the Compact's operational-quality metrics. Seating runs six concentric "
            "tiers on an explicit social hierarchy: Tier 1 the Slab Ring (Shapers, medical staff, "
            "House representatives, scouting fighters; protected by a density-rated Dead Drakma "
            "barrier wall); Tier 2 the Noble Tier (patron families, high nobility, Trust "
            "officials, diplomatic guests, and the best sight lines in any venue); Tiers 3-5 the "
            "Common Tiers (roughly 80% of capacity, graduated pricing, and the source of the "
            "crowd's acoustic energy); Tier 6 the Handler's Gallery (highest and farthest, "
            "unreserved and free, for Maw staff, Cestari handlers, and anyone too poor or too "
            "stigmatized for the Common Tiers). Crowd flow runs through 40-80 radial corridors "
            "called vomitoria, calibrated to fill a venue in roughly thirty minutes and evacuate "
            "it in under fifteen -- a riot-response specification, not a convenience, established "
            "after an early-era frontier-Maw riot killed 400 spectators whose exits could not "
            "handle a panicked egress. Backstage, every Grand Maw carries service tunnels, "
            "staging areas, armories, holding cells, and secure subterranean corridors connecting "
            "directly to nearby House compounds; the critical space is the Triage Station, a full "
            "medical facility directly beneath the Slab, reachable through a hatch openable in "
            "under four seconds, staffed by physicians employed by the venue rather than any House "
            "and whose authority over fighter treatment supersedes the attending Shaper's during "
            "an active emergency."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-065",
        "category": "regional-grand-maws",
        "statement": (
            "Extends MAW-060/061, individual venue detail. The Throat (Karkosa, 120,000, ~4,800 "
            "years old, record attendance 128,000). Occupies the geographic centre of the "
            "capital. Its Resonance Dome is an engineered acoustic shell capturing and redirecting "
            "the crowd's vocal energy downward onto the Slab; fighters describe the resulting "
            "pressure as standing inside a bell someone is ringing. Beneath it are seven levels of "
            "service tunnels, three Triage Stations, an armory the size of a small military "
            "installation, a Ledger Office occupying an entire sub-level, and the Grand Archive -- "
            "the Maw's official historical repository, holding inscribed records of every bout "
            "fought in the venue since the Ledger system began ~3,500 years ago, and incidentally "
            "the most comprehensive record of Cestari death in the world. Every Apex Championship "
            "for three thousand years and every Reclamation have been held here; Vakas's seismic "
            "approach signature is calibrated specifically to the Throat's monitoring instruments. "
            "The Mother (Maw-1, 85,000, ~4,900 years). T.D.K.'s prototype and the oldest Maw in "
            "the world, predating the Throat, retaining the original elliptical design abandoned "
            "before the circular format became standard; the asymmetry creates a positional "
            "element no other Grand Maw has. Permanent humidity forces surface re-treatment three "
            "times per event day. The Slab of Judgment (Maw-7, 45,000, ~2,200 years, post-Haku "
            "reconstruction). Where Red Beard's parents were executed (MCD-084). Its backstage "
            "corridors are the most densely Brand-Line-inscribed surfaces in the system -- the "
            "handlers gave up cleaning them centuries ago and the messages are now part of the "
            "architecture. The crowd does not cheer a fighter; it examines one. It also hosted the "
            "Reclamation ~350 years ago in which Vakas killed a champion installed by Osseren's "
            "rigging (MAW-116), so the Keldane crowd judges everything twice: once for the sport, "
            "once for the morality. The Teeth (Maw-12, 32,000, ~800 years). Draws audiences from "
            "both Trust territory and the Shattered Kingdoms into the same tiers; security is "
            "military-grade, with border-force perimeter patrols and vomitoria chokepoints "
            "sealable in under thirty seconds, and it still records more crowd-violence incidents "
            "than any other Grand Maw, averaging two per season. The Belly (Maw-3, 28,000, ~3,800 "
            "years). The only fully subterranean Grand Maw, in an expanded natural limestone "
            "cavern. Sound does not echo, it reverberates, building through a bout until crowd and "
            "impacts merge into a single amplified harmonic. Ceiling roughly fifteen metres above "
            "the Slab. Site of Kanja's Unarmed Siege (Long Mask Battle XXIII), where collapsing "
            "the structure would have killed the Cestari he came for, so he instead infiltrated "
            "the ventilation system, introduced a sleep agent, and walked them out through the "
            "service tunnels while the audience slept -- the Long Mask's only zero-casualty "
            "engagement of its type. The Drowning Floor (Maw-15, 38,000, ~1,500 years). Slab "
            "built at sea level inside a retaining basin floodable to roughly two feet of seawater "
            "via tidal gates that open at unpredictable points mid-bout. Designed as a spectacle "
            "venue rather than a fair one; the Compact has debated banning the water feature for "
            "over five hundred years and never resolved it, because the venue's events are the "
            "regional circuit's most commercially successful and the betting markets sell "
            "specialized wagers on when the water will decide the outcome. Atmosphere is carnival "
            "rather than cathedral. The Scar (the Ash Maw, 22,000, ~4,500 years). Built into the "
            "ruins of T.D.K.'s original court complex, partly destroyed in the Haku war and never "
            "rebuilt: cracked walls, upper tiers open to the sky, impact marks on the Slab from "
            "the engagement that ended the Old Dominion's capital. It sits outside the Compact's "
            "regulatory authority entirely -- no Blood Writ requirement, no medical mandates, no "
            "welfare standards, governed by whichever regional power currently holds the "
            "surrounding territory. Death rates run roughly 400% of the licensed system's average. "
            "Its competitors are the desperate, the legendary, or those trialling techniques the "
            "Compact's safety standards prohibit."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-066",
        "category": "regional-grand-maws",
        "statement": (
            "The Grand Maw system's numbering (MAW-061: Maw-1 the Mother, Maw-3 the Belly, Maw-7 "
            "the Keldane Maw/Slab of Judgment, Maw-12 the Teeth, Maw-15 the Drowning Floor, plus "
            "the unnumbered Throat and Ash Maw/Scar) is the Sovereign Trust's capital-registry "
            "Grand Circuit numbering. It is administratively distinct from at least one regional "
            "network's own local numbering -- the Maw Codex's own internal commentary notes that "
            "'the Southern Maw network is numbered separately from the capital system.' Historical "
            "references naming a numbered Maw outside a clear Grand Circuit context -- the Siege "
            "of Maw-9 (MCD-234) and the Maw Cascade operation at Maw-15 (MCD-264) among them -- "
            "refer to facilities in that separate regional registry, and are not assumed to be the "
            "same physical venues as their Grand Circuit numeral counterparts absent other "
            "evidence. This resolves an apparent Maw-1/Maw-9 conflation in the Maw Codex's own "
            "account of a Kanja liberation episode as a numbering-system mismatch rather than a "
            "location contradiction."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Section C: The Four Eras of the Maw ---
    {
        "id": "MAW-091",
        "category": "maw-eras",
        "statement": (
            "Extends MAW-090. Era I, the Old Dominion (~5,000-3,000 years ago, ~2,000 years). "
            "Governance: T.D.K. (Anu Un Ra), direct state control. Character: the Maw as state "
            "instrument -- maximum institutional control, maximum cruelty, maximum efficiency. "
            "This era established every structure every later era inherited: the Pillar system, "
            "the Cestari caste, the Slab construction standards, the Reclamation cycle, and the "
            "Scrip-Tether integration that made the Maw inseparable from the economy. Its defining "
            "tension is that T.D.K.'s system was brutally effective and self-correcting through "
            "the Reclamation, so it produced genuine excellence alongside genuine atrocity -- an "
            "unresolved five-thousand-year argument over whether the excellence exists because of "
            "the cruelty or despite it. Era II, the Post-Haku Transition (~3,000-2,000 years ago, "
            "~1,000 years). Governance: fragmented, multiple competing authorities, no central "
            "state. The Haku war broke T.D.K.'s empire but left the Maw intact because it was too "
            "economically essential to destroy and too institutionally embedded to dismantle, "
            "producing a system with no master: Pillars operating independently, unregulated "
            "emerging Banners, collapsed medical mandates, voluntary fighter welfare, and "
            "estimated death rates three to four times the Old Dominion average. It produced the "
            "Maw's most desperate legends -- Graves, Lirra Chain-Singer, and a body of anonymous "
            "fighters whose names survive only in the Brand-Line because the Ledger Offices did "
            "not operate consistently. Era III, the Sovereign Trust (~2,000-200 years ago, ~1,800 "
            "years). Governance: centralized state regulation through the Trust. The longest and "
            "most productive era: standardized competition rules, medical mandates, formalized "
            "Compact authority, and full integration of the Maw economy into the Scrip-Tether "
            "architecture. Its defining achievement is the Grand Circuit itself, established "
            "roughly 1,500 years ago, which created the career ladder, persistent record-keeping, "
            "and celebrity economy that made the Maw culturally central rather than merely "
            "economically important -- before it the Maw was an industry, after it the Maw was a "
            "civilization's identity. Its defining failure is that the system's moral "
            "contradictions became visible to the population consuming its product, through the "
            "Sable Kin exposure, the Dead Pool, and the Tether Arbitrage; the Compact's Reformist "
            "faction emerged in this era in response. Era IV, the Modern Era (~200 years ago to "
            "present). Governance: Sovereign Trust nominally, with the protection economy "
            "operating as a parallel system. Character: disruption. It begins with Kanja Haku "
            "Rexmar's campaign against the Maw's infrastructure -- the Siege of Maw-9, the Night "
            "of Ten Fires, the Coin-Weight Raid, the Maw Cascade, the Frequency Vaccine -- each "
            "attacking a different structural element, none destroying the system, all weakening "
            "it. Its defining development is the emergence of fighters from Blight-reduced zones "
            "whose true biological density exceeds the Tether-managed ceiling: the Tether's "
            "suppression is no longer universal, so the odds models are no longer reliable, so the "
            "betting economy is no longer stable, so the revenue streams are no longer "
            "predictable. The system is encountering a variable it was not designed to process -- "
            "a population the Tether does not control. CONFLICT-CHECK carried forward from "
            "MAW-090: a proposed 'Era V' conflicts with MCD-100; MCD-100 controls."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-092",
        "category": "shaper-compact",
        "statement": (
            "The Shapers' Compact was founded during the Era II-Era III transition, established "
            "by the first generation of Shapers who judged that professional self-regulation was "
            "preferable to having the emerging Sovereign Trust impose an administrative framework "
            "from outside. Its founding charter, preserved in the Compact's Registry, opens with "
            "the sentence that has defined its institutional purpose for two thousand years: 'We "
            "regulate ourselves so that no one else needs to.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Section E: the Apex field ---
    {
        "id": "MAW-101",
        "category": "apex-championship",
        "statement": (
            "Extends/completes MAW-100. The Apex Championship field is a sixteen-fighter, "
            "single-elimination, three-day tournament at the Grand Maw of Karkosa, seeded by "
            "Grand Circuit ranking. The named field, in seed order: #1 Drennan 'The Patient,' "
            "4,700x, House Dravos, reigning champion, pure Iron Patience, never knocked down -- he "
            "treats every hit as information rather than injury, and the betting markets call him "
            "'the favorite to bore Vakas to death,' which he takes as a compliment. #2 Dray Voss "
            "'The Inheritor,' 4,700x, Dravos, direct descendant of Voss Dravos, doctrinally "
            "orthodox, top-five ranked six consecutive years, two Apex finals and two losses, "
            "fighting like a man serving a sentence. #3 Ash Korren 'The Debt,' 4,500x, House "
            "Sektori, acquired from a regional Standard under Scrip-Tether debt-compliance "
            "leverage after his family's estate was seized; hybrid Dravos endurance over Sektori "
            "risk-management, the most conservative and hardest-to-exploit competitor in a "
            "generation, needing roughly four more years of Grand Circuit purses to clear the debt "
            "against roughly 60% odds of surviving them. #4 Seyra 'The Tempest,' 3,900x, House "
            "Korrath, youngest Grand Circuit qualifier in a century at twenty-three; twin blades "
            "geometrically calibrated to produce tonal feedback on impact, so the crowd chants in "
            "rhythm with her strikes -- physics, not frequency-craft, and a phenomenon the "
            "referees have no framework for scoring. #5 Kullen Gravedust, 4,800x, House Morvane, "
            "sixteen years a mortuary technician before entering the Maw at thirty; replicates the "
            "exact death-sequences of historical fighters against current opponents whose "
            "doctrinal profiles match the historical models. #6 Torven (no other name), 4,400x, "
            "House Velthari, 54-1, silent, with no fighting style of his own because Velthari "
            "fighters use the opponent's; the Reckoners cannot set reliable odds on him. #7 "
            "Brennan 'The Oak,' 4,600x, House Tolvari, 23-0, product of a ten-year developmental "
            "program, moving with the technical sophistication of a fighter twice his age. #8 "
            "Corra Deepstrike, 4,300x, House Durnwall, born in the mines, still works the morning "
            "shift and trains in the afternoon; won the Southern Provincial Proving by outlasting "
            "a Dravos Contender conditioned for forty-five-minute bouts across a sixty-two-minute "
            "fight. #9 Sahar 'The Drought,' 4,100x, House Rathaan, dehydration warfare; longest "
            "bout ninety-three minutes, ended by his Threnn opponent collapsing from dehydration. "
            "#10 Veyren 'The Mourner,' 4,500x, Morvane, 68-4, a former mortuary technician who "
            "processes every opponent as a future corpse whose failure mode he has already "
            "studied; all four losses to Korrath fighters whose theatrical unpredictability broke "
            "his analytical approach. #11 Tella Brightblade, 3,700x, Korrath, great-granddaughter "
            "of Dorne Brightblade, the field's most watchable competitor, intending to become the "
            "first Brightblade to win the Brightblade Prize. #12 Renn Hollow, 3,200x, House "
            "Brekka -- over a thousand points below the typical Grand Circuit competitor and alive "
            "because he developed at his true biological ceiling in the Blight-reduced Keldane "
            "Hollow rather than under Tether suppression; his qualification is under active "
            "Compact challenge and is the Maw's live political flashpoint. #13 Ysolen 'The "
            "Dancer,' 3,400x, House Aravel, 31-11, a former acrobat, the highest merchandising "
            "value in the qualifier field. #14 Venim, density UNMEASURED, House Vennrik -- Ozmund, "
            "entering as the lowest seed with no doctrinal profile for any opponent to analyse. "
            "#15-16 are deliberately left open in the source as unnamed Provincial Provings "
            "qualifiers, reserved for narrative flexibility. CONFLICT-CHECK: the source frames "
            "this as Book 1's tournament; per MCD-100 and MAW-100, book placement is Book 3 and "
            "MCD-100 controls."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Section D: four ready rules ---
    {
        "id": "MAW-025",
        "category": "pillar-compounds",
        "statement": (
            "Each Pillar's compound encodes its doctrine architecturally. Dravos -- the Iron "
            "Hold, on a basalt promontory above the Karkosa coastal flats, built in concentric "
            "rings: administration and medical outer ring; forty graduated-density conditioning "
            "chambers using Dead Drakma weighting embedded in the floors; and the Crucible, a "
            "sealed training Slab replicating Grand Circuit combat at 120% intensity. Beneath it "
            "are the Quiet Rooms -- lightless, soundless cells where fighters spend seventy-two "
            "hours before certification. Korrath -- the Storm Hall, on a wind-battered "
            "southern-ocean cliffside, with an open-air training Slab in a natural amphitheatre "
            "where training continues through storms so fighters learn to read a crowd's acoustic "
            "signature through interference; its Mirror Gallery is a corridor of polished panels "
            "where technically perfect strikes that look awkward are retrained until they look "
            "elegant. Velthari -- the Still Point, underground in a converted mining complex "
            "beneath the Keldane highland plateau, entered through a single surface door disguised "
            "as an agricultural storehouse, run under total environmental control with acoustic "
            "dampening; its Echo Chamber amplifies every sound a hundredfold so fighters learn to "
            "hold clinical precision while their own biology screams at them. Maekar -- the Forge "
            "Tier, cut into a dormant volcanic ridge with training levels running 40-65 degrees C; "
            "its deepest level, the Ember Floor, operates at roughly 90 degrees C on a "
            "volcanic-glass Slab that cracks under peak thermal-kinetic output and is swept and "
            "replaced after every session. Osseren -- the Anatomy, a converted hospital complex in "
            "Karkosa's medical district, holding the Bone Library: over 3,000 skeletal specimens "
            "from deceased Branded fighters spanning ~2,500 years, catalogued by density class, "
            "House, style, and cause of death, and handled by first-year recruits learning what "
            "death looks like from the inside before learning to cause it. Threnn -- a "
            "decommissioned military fortification on the Keldane coast, Dead-Drakma-plated, whose "
            "training walls are rebuilt annually because advanced trainees practise the advance "
            "drill against real structural targets. Selenar -- the Archive, a cavern network "
            "beneath the Karkosa highlands whose walls carry training marks predating the House's "
            "own records; its central space is not a Slab but the largest collection of recorded "
            "bout data in the world, maintained continuously for roughly 3,500 years, plus seven "
            "training Slabs configured to replicate each Pillar's doctrine, through which recruits "
            "rotate to learn each doctrine from the receiving end."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-026",
        "category": "pillar-patrons",
        "statement": (
            "Dravos is patronized by the Ferrenhall, old Karkosa banking, mining, and political "
            "aristocracy -- the longest active patron relationship in the system at roughly 1,100 "
            "years; the current patriarch holds a seat on the Sovereign Trust's Economic Council "
            "and treats Dravos's competitive record as political currency. Korrath is patronized "
            "not by a noble house but by the Meritha Consortium, a commercial alliance of merchant "
            "families controlling much of Karkosa's entertainment, hospitality, and luxury-goods "
            "sectors; their interest is brand synergy rather than prestige, and Korrath "
            "merchandise outsells every other Pillar combined, returning roughly fivefold on their "
            "investment. Velthari is patronized by the Keld, the oldest intelligence dynasty in "
            "Karkosa -- not publicly wealthy, prominent, or visible, but the capital's premier "
            "information brokers, who recruit their operatives from Velthari retirees because "
            "structural analysis of a body translates directly to structural analysis of an "
            "institution. Maekar is patronized by the Valorren, who control Karkosa's "
            "metallurgical industry -- foundries, smelters, and refineries processing Keldane "
            "highland ore -- and read their patronage thematically, as forgers funding fighters "
            "forged in heat. Osseren is patronized by the Morthen, who control Karkosa's medical "
            "and pharmaceutical industry: Morthen physicians staff the House's medical facilities, "
            "Morthen pharmaceuticals supply its conditioning programs, and Morthen research draws "
            "on the Bone Library's clinical data. It is the system's most ethically fraught "
            "arrangement -- the family profiting from healing also profits from the institution "
            "creating the injuries -- and the Morthen have calculated that owning both sides of "
            "the equation is more profitable than owning either. Threnn is patronized by the "
            "Greymantle, military aristocracy whose line has produced Trust generals and fortress "
            "commanders for over a thousand years; their patronage is ideological, and the current "
            "patriarch is the only patron who regularly trains alongside his House's fighters. "
            "Selenar is patronized by the Veradaan, a scholarly family producing academics and "
            "institutional theorists for over eight hundred years; the current patriarch holds a "
            "professorship at Karkosa's central university and publishes pseudonymous analyses of "
            "Grand Circuit bouts that are read by every Shaper in the system, none of whom know "
            "their author patronizes the House whose doctrine those analyses serve."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-052",
        "category": "shaper-compact",
        "statement": (
            "Extends MAW-050. A Blood Writ candidate must satisfy the Shapers' Compact's "
            "Certification Board in five domains. Fighter Conditioning: three years supervised "
            "under a licensed Shaper, then a practical in which the candidate designs and executes "
            "a twelve-week conditioning program on a volunteer whose measurable improvement must "
            "exceed the regional baseline by at least 15% -- if the subject is injured during the "
            "program, the candidate fails. Medical Triage: certification in combat-trauma "
            "assessment, field stabilization, and recovery-protocol design, with the operative "
            "standard being the ability to determine within sixty seconds of a bout's end whether "
            "a fighter returns within two weeks, needs extended recovery, or must retire "
            "permanently; miscalculation in either direction is grounds for revocation. "
            "Contractual Law: demonstrated command of Maw charter law, bout contracts, transfer "
            "agreements, and welfare mandates, with personal liability -- including criminal "
            "prosecution where a violation causes death -- for signing a contract that breaches "
            "welfare standards. Competitive Strategy: written and live examination on doctrinal "
            "weakness analysis and matchmaking, containing a deliberate ethical trap -- one "
            "hypothetical matchup involves a fighter whose medical records show concealed "
            "vulnerability, and the only passing answer is to decline the bout. Fighter Identity: "
            "three complete identity packages (name, visual presentation, crowd-engagement "
            "strategy, career narrative arc), assessed for viability rather than creativity, on "
            "the principle that a fighter without an identity is a body. The Writ renews on a "
            "five-year compliance audit by the Compact's Oversight Division covering survival "
            "rate, medical compliance, contractual integrity, and patron-relationship "
            "transparency. Revocation triggers are: a fighter death rate exceeding 200% of the "
            "regional average over any rolling two-year period; conviction for bout-rigging or "
            "match-fixing; conviction for betting on one's own fighters; failure to disclose a "
            "fighter's medical condition materially affecting a bout; and any criminal conviction "
            "involving violence against a fighter off the Slab. Revocation is permanent, with no "
            "appeal, and bars the individual from practising, advising, or entering a licensed "
            "Maw's backstage area for life."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-053",
        "category": "shaper-compact",
        "statement": (
            "Extends MAW-050. The Compact operates through three bodies. The Iron Council: seven "
            "elected senior Shapers on three-year terms, one seat per Pillar doctrinal domain, "
            "though a seat-holder need not be affiliated with that Pillar and need only "
            "demonstrate mastery of its principles. The Council sets standards, adjudicates "
            "disputes, certifies or strips Apex Championships, and performs its most critical "
            "function -- presenting the Apex Champion to Vakas in Reclamation years, with "
            "authority to refuse certification where it suspects corruption, which has occurred "
            "seven times in recorded history. The Oversight Division: forty full-time auditors "
            "conducting Writ renewals, investigating complaints, and monitoring welfare compliance "
            "across all licensed Houses, operating independently of the Council, reporting without "
            "editorial filtering, and able to escalate past patron pressure directly to the "
            "Council under whistleblower protection. The Registry: the administrative backbone "
            "holding the master list of licensed Shapers, active Writs, transfer records, and "
            "filed bout contracts -- without which no bout is legal, no transfer binding, and no "
            "championship certified. Three ideological factions have dominated Compact politics "
            "for five centuries. The Preservationists hold that the Compact exists to maintain "
            "institutional continuity, resist reforms disrupting the House hierarchy or expanding "
            "fighter rights, and argue that five thousand years of stability is itself the "
            "evidence the system works; they are led informally by Dravos-affiliated Shapers. The "
            "Reformists hold that the Compact must evolve or repeat T.D.K.'s administrative "
            "collapse, and push for expanded medical mandates, retirement protections, "
            "betting-integrity regulation, and limits on patron interference, arguing the current "
            "model is unsustainable because it depends on a Cestari labor supply whose moral "
            "legitimacy is increasingly contested; they are led informally by younger, largely "
            "Banner-affiliated Shapers. The Independents are numerically dominant at roughly 50% "
            "of membership but organizationally weak because they do not coordinate; their "
            "fragmented voting defaults to the status quo, since reform requires affirmative "
            "majorities their blocs rarely produce, and converting Independents is the Reformists' "
            "central strategic problem."
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

    ledger["rules"].extend(NEW_RULES)

    # --- Amend MAW-024 in place (G-1): narrow the "only" claim, combined reading ---
    found_024 = False
    for r in ledger["rules"]:
        if r["id"] == "MAW-024":
            found_024 = True
            r["statement"] = (
                "The Iron Veil (House Velthari) retired 188-0, the only undefeated Apex Champion "
                "in Maw history and the only Reclamation Exception survivor to face Vakas at his "
                "maximum recorded 300% escalation (R-~76, MAW-115). Four other fighters have "
                "survived a Reclamation Exception at lower escalations -- \"The Unnamed Who "
                "Stood\" (R-~15, MAW-110), Lirra Chain-Singer (R-~48, 220%, MAW-112), Ashmark Kren "
                "(R-~94, 200%, MAW-118), and Korrith the Scorpion (R-~96, 250%, MAW-119) -- but "
                "none retired undefeated. Narrowed 2026-09-10 (Batch 103) to resolve a "
                "self-contradiction in the Maw Codex's own account, which separately named four "
                "other Exception survivors; the Iron Veil's distinguishing claim is undefeated "
                "record plus maximum escalation, not sole survival."
            )
            break
    assert found_024, "MAW-024 not found for amendment"

    # --- Amend GEO-003 in place (G-3 related): fix Karkosa venue mislabel ---
    found_geo003 = False
    for o in ledger["rules"]:
        if o["id"] == "GEO-003":
            found_geo003 = True
            o["statement"] = o["statement"].replace(
                "Karkosa/Maw-7 Slab (Sovereign Trust Domain)",
                "Karkosa/The Throat (Sovereign Trust Domain)",
            )
            o["statement"] += (
                " Corrected 2026-09-10 (Batch 103): the Karkosa capital venue is the unnumbered "
                "Throat (MAW-060); Maw-7 'the Keldane Maw'/'Slab of Judgment' (MAW-061) is a "
                "separate venue at Keldane, not Karkosa -- the earlier 'Maw-7 Slab' label for "
                "Karkosa was a stale pre-MAW-060/061 shorthand."
            )
            break
    assert found_geo003, "GEO-003 not found for amendment"

    ledger["batches_completed"].append(
        {
            "batch": 103,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Maw Codex fuller pass, Sections A/B/C/E (the Reclamation Chronicle, venue "
                "tactical profiles, the Four Eras, the Apex field) plus Section D's four ready "
                "rules (Pillar compounds/patrons, the Blood Writ, the Compact's organs/factions) "
                "-- 24 new rules. Naming collisions resolved by renaming: Draveen -> Ferrenhall "
                "(Dravos's patron dynasty, avoiding the Dravos/Draveen/Draeven/Draven cluster) "
                "and Mirel 'The Dancer' -> Ysolen 'The Dancer' (Apex field #13, avoiding "
                "confusion with Val Mirel Kareth). Contradictions resolved logically against the "
                "live ledger per Abad's authorization: G-1, MAW-024 amended in place to narrow "
                "the Iron Veil's 'only' claim to undefeated-record-plus-maximum-escalation rather "
                "than sole Exception survival, since the Codex's own Chronicle names four other "
                "Exception survivors. G-2, MAW-013 deliberately omits a specific Exception count "
                "rather than pick one, since the Codex's own tally is internally inconsistent "
                "three ways. G-3, new rule MAW-066 clarifies the Grand Maw capital-registry "
                "numbering is administratively distinct from at least one regional network's own "
                "local numbering (per the Codex's own commentary), resolving the Maw-1/Maw-9 "
                "conflation without asserting MCD-234/MCD-264 share a venue with MAW-061's "
                "numbered list; GEO-003 amended in place to fix a stale 'Karkosa/Maw-7 Slab' "
                "mislabel to 'Karkosa/The Throat,' and MAW-063's Mother/Scar venue profiles "
                "aligned to GEO-003's already-locked Lawless Reaches cluster rather than the "
                "Codex's own Southern Seaboard/Shattered Kingdoms claims, since the Atlas "
                "controls per established precedent. Section D's larger remaining inventory (the "
                "18 Branded Legends, the doctrinal matchup grid's percentages, the ten Banners in "
                "full, the Pits' real scale, the current Iron Council's seven named seats, named "
                "Shapers' methods, Cestari operational depth, the Marker Rebellion/Long Walk in "
                "full, betting economics depth) remains queued for future batches. "
                + BATCH_NOTE
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
