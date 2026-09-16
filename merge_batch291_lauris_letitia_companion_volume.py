#!/usr/bin/env python3
"""Batch 291: Lauris Letitia Chronicle Companion Volume -- Era F Operations 1-22
genuinely-new material, age reconciliation, MCD-141 supersede, and optional
texture rules from the Era A-C, Era D-E, and Era F ops 23-40 extraction agents."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE_MAIN = (
    "'Lauris_Letitia_Chronicle_1.docx' (uploaded directly by Abad 2026-09-15), a fuller "
    "'Companion Volume' edition of the same underlying Lauris Letitia chronicle already "
    "extracted from World_Adaptation_Blueprint Section VI (Batches 28-38, MCD-140 through "
    "MCD-217). Processed via 5 parallel background extraction agents (Era A-C, Era D-E, "
    "Era F Operations 1-22, Era F Operations 23-40 + Defection + Ezio meeting, Era G-H). "
    "~90% of the document (Eras A-E, G-H, and Era F's back half) matched already-locked "
    "canon near word-for-word -- confirmed redundant, no new rules drafted from it, per "
    "the established Complete_Chronicle_Definitive_Edition/MRD-Five-Book-Arcs precedent. "
    "The genuinely new material is Era F Operations 1-22 (her first 22 Sealbound "
    "Directorate contracts), plus minor optional texture flagged by the Era A-C and "
    "Era D-E agents and one optional aggregate-totals rule from the Era F ops 23-40 agent."
)

BATCH_NOTE = (
    "Abad answered five synthesis questions in one message, verbatim: \"6,000\" (her "
    "present-day age, resolving a real contradiction between this document's own "
    "'~4,000 at present' framing and the already-locked MCD-174 departure age (~4,000) "
    "plus MCD-175 arrival timing (~2,000 years before Book 1's present), which sum to "
    "~6,000) / \"approve\" (superseding MCD-141, which contradicts the already-locked, "
    "later-drafted MCD-151 on whether the Kareth War-Order's founding expedition left "
    "Kares Prime during or before the K-strand decline -- MCD-151 controls, corroborated "
    "a third time by this document's own Era A material) / \"approve draft 1 through "
    "draft 9\" (the Era F Operations 1-22 agent's nine candidate rules, covering Sample "
    "K-403, the Twin Anomaly, Settlement K-447's resonance-keyed cluster, the two-phase "
    "Vask of the Hollow clearance, the Brokenwall/Velaris planted-node outbreaks, the "
    "Petite Catastrophe alias origin, the Long Pursuit's institutional-blindness "
    "confirmation, the escalating-independence arc, and her non-combat operational range) "
    "/ \"yes\" (a follow-up pass filling in Operations 2, 5, 11, 13, 17, and 21, which the "
    "Era F ops 1-22 agent had deliberately left undrafted pending the required Voskharen "
    "rename) / \"yes\" (locking the optional, lower-priority texture rules both the Era "
    "A-C and Era D-E agents flagged as skippable, plus the Era F ops 23-40 agent's single "
    "optional career-aggregate-totals rule). Two corrections applied in place as a direct "
    "consequence of the age ruling: MCD-212's and MCD-215's own 'roughly 4,000 years old' "
    "phrasing corrected to 'roughly 6,000' to match. The required Verehimu-to-Voskharen "
    "geographic rename (per the established MCD-185/190/207 precedent, avoiding collision "
    "with House Verehimu) is applied throughout the six newly-drafted operations. "
    "Operations 11, 17, and 21 turned out to already have compressed coverage locked at "
    "MCD-179/183/185/211/212 (the Tide-Wraith species reveal, the Drowning Vault's breach "
    "and its ~200 secured subjects) -- those three are drafted here as tactical-mechanics "
    "extensions of the already-locked rules rather than restatements, avoiding redundancy."
)

NEW_RULES = [
    # --- Age reconciliation ---
    {
        "id": "MCD-1533",
        "category": "World Mechanics",
        "statement": (
            "Lauris's present-day age at the start of My Rival's Distance Book 1 is "
            "approximately 6,000 years, not the ~4,000 given informally elsewhere: "
            "MCD-174 (departure from Kares Prime at ~4,000) plus MCD-175 (arrival on Cian "
            "~2,000 years before Book 1's present) sum to ~6,000, and that arithmetic "
            "controls. This Companion Volume's own Era A/B framing asserted she is "
            "'~4,000 years old at present,' directly conflicting with the already-locked "
            "departure/arrival chronology; Abad's ruling settled it at 6,000. MCD-212's "
            "and MCD-215's own 'roughly 4,000 years old' / 'roughly 4,000 years' phrasing "
            "are corrected in place to 'roughly 6,000' to match; no other locked rule "
            "states her present-day age numerically."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    # --- DRAFT-1 through DRAFT-9, Era F Operations 1-22 agent (approved verbatim) ---
    {
        "id": "MCD-1534",
        "category": "World Mechanics",
        "statement": (
            "During Operation 4 (the Korren Smuggling Ring, Apprentice Contracts), Lauris "
            "recovered a sealed item designated 'Sample K-403' from smuggler Therik Voll's "
            "stores and delivered it to the Directorate's Coastal Containment Office as "
            "the contract specified, without disclosing that she recognized it on sight as "
            "a fragment of Karesian biological material. She would later determine, "
            "through her own accumulated archival research, that the fragment had been "
            "pulled from a Korren Highlands archaeological site roughly seven years before "
            "the contract, and that it is one of approximately a dozen such Karesian "
            "biological fragments scattered across the Sealbound Directorate's various "
            "containment archives -- each one residue of the engineering tradition's long "
            "processing of Karesian source material. Sample K-403 remains filed, "
            "unrecovered, in the Directorate's Coastal Containment archive as of the "
            "present-day timeline."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1535",
        "category": "World Mechanics",
        "statement": (
            "Operation 6 (the Twin Anomaly, Apprentice Contracts) pitted Lauris against "
            "coordinated assassin twins, Velek and Velka, whose paired kinetic-load-"
            "sharing capability Lauris judged biologically inconsistent with their "
            "claimed origin (unsupervised exposure to a Living Drakma deposit) and "
            "indicative instead of deliberate engineering. She terminated both. Before "
            "the compound's demolition destroyed the twins' development records, she "
            "photographed several pages; the photographs remain in her personal archive, "
            "unanalyzed, and she privately suspects -- without confirmation -- that the "
            "twins were a product of the same engineering tradition she would later "
            "identify as T.D.K.'s. She has not yet shown the photographs to Sephtis, whom "
            "she expects would recognize them."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1536",
        "category": "World Mechanics",
        "statement": (
            "Operation 12 (Settlement K-447, Established Hunter period) revealed that a "
            "hostile cluster of 73 subjects had been generated from a dormant Ionic Rite "
            "resonance node buried beneath the settlement's central square, reactivated "
            "when the settlement's roughly 340 murdered civilians were arranged into a "
            "precise nested-ring geometric figure -- a deliberate resonance-keying act, "
            "not spontaneous ritual. Lauris terminated the cluster, excavated and "
            "examined the node, then reburied it without reporting its existence to the "
            "Directorate. She never determined who arranged the bodies or who possessed "
            "the keying knowledge required to do so; the identity of that actor remains "
            "an open question in her personal archive."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1537",
        "category": "World Mechanics",
        "statement": (
            "Operation 14 (the Vask of the Hollow, Established Hunter period) was, at the "
            "time, the most extensive Ionic Rite-derived facility Lauris had encountered: "
            "a 14-kilometer subterranean gallery system that had defeated six prior "
            "Directorate exploration teams and reduced a seventh from twelve members to "
            "two. Lauris cleared it alone over 18 days, terminating approximately 720 "
            "engineered hostile entities whose biology combined Karesian-derived density "
            "features with Cian-born human substrate -- the point at which she privately "
            "concluded the pattern she'd been noticing since Operation 3 was 'no longer "
            "subtle.' Roughly two years later, Operation 20 found the facility's sealed "
            "perimeter breached again by a new population (~320 subjects) generated by "
            "the same central resonance node, still active beneath the Directorate's "
            "seal; Lauris cleared the new population, then located and destroyed the "
            "central node itself, permanently ending the site's regenerative capability "
            "-- the only revision to Directorate containment doctrine (central-node "
            "destruction over perimeter sealing alone) her entire Directorate career "
            "produced. The fourteen smaller redundancy nodes her Operation 20 clearance "
            "missed were later found and destroyed in Operation 36 (already locked, "
            "MCD-191)."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1538",
        "category": "World Mechanics",
        "statement": (
            "Operations 16 (Brokenwall) and 22 (Velaris, Established Hunter period) were "
            "mass civilian density-anomaly outbreaks -- roughly 200 and roughly 600 "
            "simultaneous afflicted subjects respectively -- that Lauris cleared through "
            "sustained, discrete precision-strike engagement (22 and 47 continuous hours "
            "respectively) rather than her usual single extended combat-progression "
            "climb, preserving the large majority of each city's unaffected population. "
            "In both cases she privately traced the outbreak's true cause to a small "
            "planted Ionic Rite-derived resonance node hidden in the city's central "
            "plaza, deliberately activated from outside to trigger the outbreak; at "
            "Velaris she destroyed the node outright rather than merely rebury it as she "
            "had at Brokenwall. The Directorate filed both outbreaks as Cause Unknown, "
            "never learning the true mechanism. The two activations, roughly eighteen "
            "months apart, indicated a deliberate hand weaponizing Ionic Rite technology "
            "against Cian civilian populations -- whether Anu Un Ra's own apparatus "
            "selectively reasserting control (consistent with CULT-008's framing) or a "
            "separate actor is left deliberately unresolved; Lauris never identified the "
            "source during her Directorate career."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1539",
        "category": "World Mechanics",
        "statement": (
            "Lauris's Established Hunter-period nicknames (the Wall That Walks, "
            "Heavy-Ordnance Letitia, the Thing That Won't Move, the Petite Catastrophe, "
            "the Compact Siege; already locked at MCD-179) never originated in "
            "Directorate records, which referred to her only by external-asset "
            "designation; they were coined informally by contractors, field teams, and "
            "operation survivors who needed language for what they had witnessed, and by "
            "Operation 22 every senior contractor in the Directorate's external pool had "
            "heard at least three of them. 'The Petite Catastrophe' specifically "
            "originated from a perimeter-watch enforcer's after-action report on the "
            "Velaris clearance (Operation 22): 'She was a five-foot girl walking through "
            "the streets of Velaris terminating 600 people... The city was big. She was "
            "small. The catastrophe was the same shape.' The line was reproduced in "
            "subsequent Directorate contractor briefings and the alias attached "
            "permanently."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1540",
        "category": "World Mechanics",
        "statement": (
            "Operation 19 (the Long Pursuit, Established Hunter period) targeted Kaerith "
            "Vossen, a defected senior contractor five prior Directorate acquisition "
            "teams had failed to locate across three years. Lauris's 23-month pursuit "
            "used no physical tracking; she instead conducted approximately 80 "
            "interviews with current and former Directorate contractors and officers, "
            "building a predictive model of Vossen's decision-making accurate enough to "
            "intercept him at a safe-house six days ahead of his arrival. The "
            "interviews, conducted for tactical purposes, incidentally produced Lauris's "
            "first systematic confirmation -- corroborated by many independent "
            "interviewees rather than her own archival inference alone -- that the "
            "Directorate's senior staff did not understand their own institution's "
            "inherited Ionic Rite foundations or its ongoing processing of Karesian "
            "source material; they believed the containment doctrine was native "
            "Directorate methodology. This operation substantially built the "
            "evidentiary basis for Lauris's eventual Disillusionment."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1541",
        "category": "World Mechanics",
        "statement": (
            "Across the Established Hunter period, the Directorate's operational trust "
            "in Lauris escalated past its own standard framework: by Operation 14 it had "
            "stopped assigning her a supervising mentor, by Operation 17 it had stopped "
            "assigning her support teams, and by Operation 22 it was issuing her only "
            "contracts no other contractor in its pool could plausibly complete. By the "
            "period's close she had become the institution's default response to "
            "problems it could not otherwise resolve -- and, per Vael Korr-Drennen's own "
            "later retrospective assessment, the Directorate's 'economic peak' in its "
            "use of her: operating at full capability within a stable, predictable "
            "procedural relationship the institution did not yet recognize as building "
            "toward its own eventual rupture."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1542",
        "category": "World Mechanics",
        "statement": (
            "Lauris's Apprentice- and Established Hunter-period contracts demonstrate an "
            "operational range beyond direct combat: walking unopposed and unhurried "
            "through a hostile civilian line whose members did not read her petite frame "
            "as a threat until too late (Operation 1); a 14-kilometer open-water night "
            "swim and a stone-wall breach-by-disassembly to extract a hostage with zero "
            "paramilitary casualties (Operation 2); a calibrated acquisition of a "
            "smuggling boss via a single collarbone-fracturing contact strike at a "
            "restaurant table rather than an assault on his fortified warehouse "
            "(Operation 4); and an underwater hull-climb boarding of a fugitive naval "
            "captain's crewed vessel (Operation 13). Her Directorate reputation rests as "
            "much on patient, minimal-force precision as on raw combat capability."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    # --- Follow-up pass: Operations 2, 5, 11, 13, 17, 21 (Voskharen rename applied) ---
    {
        "id": "MCD-1543",
        "category": "World Mechanics",
        "statement": (
            "Operation 2 (the Sister-of-Voren Abduction, Apprentice Contracts) tasked "
            "Lauris with recovering Sister Vaneth of Voren, a Directorate-affiliated "
            "archivist abducted from a records facility in Coastal Voskharen by "
            "Vorenist religious paramilitaries and held on a fortified former "
            "Directorate watch-station island roughly 14 kilometers offshore, as an "
            "alternative to a projected 200-enforcer Directorate assault (40-60 "
            "enforcer casualties, ~30% chance of the hostage's death). Lauris swam the "
            "14 kilometers overnight, breached the perimeter's stacked-stone wall by "
            "disassembling it at contact density rather than forcing it (avoiding the "
            "percussive signature of a forced entry), located and extracted the "
            "archivist within roughly seven minutes of entering the central building, "
            "and departed before the approximately 60 paramilitaries realized the "
            "position had been breached. Total engagement time was approximately 47 "
            "minutes; no paramilitary was killed, the contract having specified "
            "acquisition rather than termination."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1544",
        "category": "World Mechanics",
        "statement": (
            "Operation 5 (the Maelstrom Beast, Apprentice Contracts) sent Lauris into "
            "the deep tidal channels of the Voskharen Wetlands to terminate a "
            "14-meter, ~40,000-kilogram apex predator (density ~1,800x) that had killed "
            "roughly 200 Voskharen coastal-community residents over three months and "
            "evaded the Directorate's standard offshore-artillery response by "
            "withdrawing into channels no Directorate assault gear could navigate. "
            "Lauris walked the channel floor for three hours to the entity's "
            "22-meter-deep primary chamber (Karesian density being incompatible with "
            "floating), survived both its bite (teeth fracturing against her sternum) "
            "and a full-body compression coil (~80,000 kilograms of force, distributed "
            "laterally by her Hexa-Lamellar Lattice), then severed its spine and "
            "terminated it with the Spine of Dagon, drawn and swung underwater. Total "
            "engagement, entry to emergence with the body, was approximately seven "
            "hours -- the largest single opponent by mass she had engaged on Cian to "
            "that point, though its density fell below Branded-tier thresholds."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1545",
        "category": "World Mechanics",
        "statement": (
            "The two Tide-Wraith engagements MCD-185 references in passing (Operation "
            "11's juvenile, Operation 21's adult, both in the Voskharen Trench) shared "
            "a common tactical geometry beyond Lauris's own underwater-walking "
            "approach: a hardened Directorate vessel deployed as bait at a known "
            "feeding zone, with Lauris engaging the entity when it surfaced to attack. "
            "Operation 11's juvenile (~38 meters, ~280,000 kilograms, ~4,400x density, "
            "four rings of jaw teeth) breached directly under the vessel's bow; Lauris "
            "severed its jaw at the first tooth-ring with the Spine of Dagon during the "
            "closure motion, then walked down its spine during its dive attempt to "
            "sever its primary motor ganglion, terminating it in roughly ninety seconds "
            "with zero crew casualties. Operation 21's adult (~60 meters, ~880,000 "
            "kilograms, ~6,000x density, five tooth-rings, a larger and more developed "
            "dorsal pressure-plate), encountered eighty months later on an upgraded "
            "vessel built from Operation 11's own operational data, approached more "
            "cautiously and at greater range; Lauris used the same jaw-severing and "
            "spine-pursuit technique at correspondingly greater scale, terminating it "
            "in roughly three minutes. The species' slow multi-stage growth (juvenile "
            "to apex adult across at least eighty months) and its retrieved adult-stage "
            "biological profile led Lauris to privately suspect -- consistent with "
            "MCD-185's later confirmation that the species was engineered rather than "
            "naturally evolved -- that the Tide-Wraiths were bred and deliberately "
            "released into the Voskharen Trench by the same tradition responsible for "
            "the Ionic Rite architecture she had been encountering since Operation 3."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1546",
        "category": "World Mechanics",
        "statement": (
            "Operation 13 (the Captain Drenneth Acquisition, Established Hunter period) "
            "tasked Lauris with acquiring Captain Drenneth of the Voskharen Naval "
            "Authority -- a defector who had stolen three Directorate-classified "
            "vessel-control protocols, destroyed the Authority's primary armory, and "
            "assassinated two senior officers -- without sinking his flagship, the Iron "
            "Veth, so the stolen protocols could be recovered intact. Lauris located "
            "the vessel through roughly three months of independent intelligence work, "
            "boarded it at night during a refueling stop via underwater hull-climb "
            "(adapting the lattice-grip vertical-ascent technique she had developed at "
            "Karth-Ven for cliff faces to wooden hull surfaces), and acquired Drenneth "
            "in his quarters using the same calibrated collarbone-fracturing contact "
            "strike as Operation 4's smuggling-boss acquisition. Of the roughly 18 crew "
            "aboard during the boarding, six were terminated and twelve disabled "
            "non-lethally through Phalanx-supported strikes during her exit; Drenneth "
            "was delivered alive, and a subsequent Directorate recovery team retrieved "
            "the protocols intact. Lauris later learned, outside the contract's scope, "
            "that Drenneth died during Directorate processing despite her having "
            "delivered him alive -- her private assessment being that her own "
            "procedural cleanliness and the Directorate's were not the same standard. "
            "Coincidental homonym, not a collision: unrelated to Drenneth "
            "Threnarr-Vask, Lauris's Sister-Hold archivist mentor (MCD-162/164)."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1547",
        "category": "World Mechanics",
        "statement": (
            "Operation 17, the breach clearance MCD-179 references (a submerged "
            "Directorate facility roughly 1,200 meters deep in the Voskharen Trench, "
            "viable for Lauris without pressurized equipment via Karesian Ironstorm "
            "Blood's oxygen-binding capacity), was a 30-hour-window race against "
            "secondary-containment failure following a primary breach. Lauris "
            "descended by controlled Phalanx-arrested fall (four hours), engaged and "
            "terminated the 23 released subjects -- combat-capable Karesian-derived "
            "constructs, density ~4,000-6,000x, trained in disciplinary forms drawn "
            "from Karesian source material, consistent with the Salt-Locked Archive's "
            "guardian construct (Op. 15) -- across roughly 14 hours, then manually "
            "reconstructed the breached primary containment barrier over a further 8 "
            "hours, resealing it with 4 hours to spare in the 30-hour window. The "
            "reconstruction is what left the roughly 200 additional Karesian-derived "
            "subjects MCD-179 describes secured behind the reseal rather than "
            "released; Lauris's later Operation-25 return and full site inspection "
            "(MCD-183) revealed the true scale and nature of what her Operation-17 "
            "reseal had preserved."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    # --- Optional texture: Era A-C agent ---
    {
        "id": "MCD-1548",
        "category": "World Mechanics",
        "statement": (
            "The oldest Karesian archive, preserved in the Iron-Halls of Vask, traces "
            "the species back only approximately 34,000 years -- at which point "
            "Hexa-Lamellar Lattice, Gravimetabolic Architecture, and Ironstorm Blood "
            "biology were already fully present. Karesian biology was not engineered or "
            "selected by any council; it emerged across an evolutionary span longer "
            "than the species' own written memory, and the archive itself is "
            "understood, even by Karesians, to record only the period during which the "
            "species could write, not the civilization's full true age, which is "
            "deliberately left older and unknown."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1549",
        "category": "World Mechanics",
        "statement": (
            "Kares Prime's binary-star light, filtered through its dense atmosphere, "
            "produces perpetual amber-and-bronze illumination that Karesian eyes "
            "evolved to register directly at wavelengths Cian-born humans cannot "
            "perceive without compensating equipment. The Karesian phrase karth-mor "
            "('the body that does not betray') names the species' own understanding of "
            "its non-aging biology (extends MCD-149) as a gift reciprocated through the "
            "discipline of conditioning -- a Karesian who stops conditioning eventually "
            "falls to opponents a conditioned Karesian would have defeated."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1550",
        "category": "World Mechanics",
        "statement": (
            "Before the K-strand decline, Kares Prime's isolation from the outside "
            "world was a matter of choice rather than incapacity: Karesians traded "
            "sparsely and asymmetrically through orbital trade-points in low planetary "
            "orbit, exchanging Living Drakma micro-particulate, high-gravity-forged "
            "metalwork, and Ironstorm-Blood-derived biological products for textiles, "
            "foodstuffs, and archivally valuable information -- the same trade contact "
            "T.D.K. later used as the vector for his K-strand-degrading agent (extends "
            "MCD-153). Prior to Lauris's own arrival, Cian-side awareness of Kares "
            "Prime existed only as imprecise 'high-gravity people' references in "
            "Sephtis's older archival sources, generally dismissed there as legend."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1551",
        "category": "World Mechanics",
        "statement": (
            "Vask Karth-Ven's name translates approximately as 'the witnessed-walking "
            "deep-place,' applied retroactively during the Sister-Hold era once the "
            "karth-ven cultural concept (an achieved state of fully processing weighty, "
            "identity-defining information, already locked at MCD-172) had become "
            "central to the civilization's self-understanding -- the same root that "
            "later names the Karth-Sera curriculum developed for Lauris (MCD-169)."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1552",
        "category": "World Mechanics",
        "statement": (
            "The Karesian civilization's full response to the K-strand catastrophe -- "
            "from the First Affected Cohort's detection through the Last Conclave's "
            "three decisions -- unfolded across approximately 75,000 years (five "
            "generations of roughly 15,000 years each): the first two generations "
            "spent investigating the cause, the next three attempting interventions "
            "that ultimately failed to restore the male population before the Last "
            "Conclave convened. By Cian standards this is a long span; by the "
            "civilization's own ~100,000-year lifespan standard, it was a desperately "
            "short window to respond to an existential crisis."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1553",
        "category": "World Mechanics",
        "statement": (
            "By age 10, Lauris tracked within cohort norms on physical conditioning and "
            "lineage education and marginally above cohort norms on archival training. "
            "Within her assembled Threnarr Sister-Hold, her closest personal bonds were "
            "with Selene (closest bond), Drenneth Threnarr-Vask (experienced by Lauris "
            "as a wise elder), and Mira Threnarr-Olmedrin (her physical training "
            "instructor, a close working relationship despite Mira's cool temperament). "
            "Her closest cohort friend was Velith, one of the 47 parthenogenically-"
            "conceived children raised alongside her at Threnarr specifically to "
            "obscure her true status (already locked at MCD-165), with whom she shared "
            "early observation-recording exercises before Velith's death when Lauris "
            "was approximately 1,200 (already locked at MCD-165)."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    # --- Optional texture: Era D-E agent ---
    {
        "id": "MCD-1554",
        "category": "World Mechanics",
        "statement": (
            "Vask Karth-Ven, the smallest of the twelve surviving Vasks (~480 residents "
            "at the time of Lauris's relocation), was founded in the late cooperative "
            "era specifically as a combat-training center and survived the "
            "consolidation because the Iron-Speakers recognized the diminished "
            "civilization needed a way to develop combat capability against "
            "non-Karesian incursions it could no longer deter through demographic "
            "weight alone. Its structures are built directly into a deep-mountain ridge "
            "along the spine of Kares Prime's primary continent -- training halls cut "
            "into living stone, residence chambers in deeper galleries, deliberation "
            "rooms of unworked mountain rock. Its central training floor is a 60-meter "
            "circular platform of high-gravity-forged Drakma, continuously calibrated "
            "for 28,000 years before Lauris's arrival; over her training it would "
            "develop a more detailed combat-reading of her than of any other Karesian "
            "in the Vask's recorded history."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1555",
        "category": "World Mechanics",
        "statement": (
            "From achieving karth-ven at 1,841 until her decision to depart at ~3,400 "
            "(a span of roughly 1,560 years), Lauris served as Kares Prime's de facto "
            "resident high-tier combatant -- an informal role, since the Sister-Hold "
            "era had no formal high-tier combat designation; the civilization simply "
            "deployed her when a situation required her capability. Across this period "
            "she conducted approximately 23 documented operational deployments: six "
            "defensive operations against non-Karesian incursions at orbital "
            "trade-points, eight geological emergency responses in the pattern of the "
            "Vask Threnarr mining rescue (MCD-171), three inter-Vask security "
            "operations during resource-scarcity conflicts between Karesians (all "
            "resolved without lethal force -- her presence alone was generally "
            "sufficient to redirect the conflict toward deliberation), four training "
            "engagements she requested herself, serving as primary opponent for "
            "promising combatants from other Vasks as she began to feel responsibility "
            "for developing the next generation's capability, and the Vask Olmedrin "
            "defense (MCD-173), the period's sole operation approaching the upper limit "
            "of her capability."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1556",
        "category": "World Mechanics",
        "statement": (
            "At age 1,840, the year she confronted Selene about why she was different "
            "(MCD-172), Lauris's static density had stabilized at approximately "
            "14,000x, with combat-sustained capacity (extended engagement) approaching "
            "18,000x and combat-progression capacity (a sustained 90+-minute "
            "engagement) approaching 22,000x -- figures that predate both her Vask "
            "Olmedrin peak (25,000x single-engagement density at age 2,800, MCD-173) "
            "and her eventual Cian-era operational range (MCD-209)."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1557",
        "category": "World Mechanics",
        "statement": (
            "On Kares Prime, before Lauris transferred its naming authority to Kanja's "
            "forge (MCD-204), the crowd-management discipline later renamed Attia's "
            "Rite on Cian carried a Karesian name of uncertain etymology, translating "
            "approximately as 'the rite of the open hand.' The name itself predates "
            "Lauris; the Karth-Sera curriculum's version of the discipline (developed "
            "age 1,800-2,400 under the Karth-Ven Sister-Hold) is an adaptation of an "
            "older Karesian movement form, not an original invention of the curriculum."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1558",
        "category": "World Mechanics",
        "statement": (
            "Six recorded lines from Lauris's Kares Prime era, alongside the quotes "
            "already locked at MCD-166/171/172/173/174: Selene, on learning of Lauris's "
            "first anomalous density reading -- 'I knew, the moment she was born, that "
            "this would happen eventually. I did not know it would happen this soon.' "
            "Veska Karth-Ven, observing Lauris's lack of fatigue during her twentieth "
            "year of training -- 'The child does not stop. We end the session because "
            "we tire. She continues. She would continue indefinitely if we did not stop "
            "her.' Lauris's own archive entry closing the Vask Threnarr mining rescue "
            "-- 'The shaft is sealed. The Hold continues.' Lauris declining formal "
            "acknowledgment after the Vask Olmedrin defense -- 'They came for the Vask. "
            "The Vask is intact. The acknowledgment is not necessary.' Lauris's archive "
            "entry on Selene's death -- 'Thirty seconds. The Hold continues. Selene "
            "does not.' Lauris's final recorded line on departing Kares Prime -- 'The "
            "world is below me. It will be below me for the rest of my life. I will "
            "continue.'"
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    {
        "id": "MCD-1559",
        "category": "World Mechanics",
        "statement": (
            "Karesian parthenogenic conception required Sister-Hold initiation, which "
            "became unavailable as the population continued its decline; consequently "
            "most of Lauris's 47-child cohort (MCD-165) -- the civilization's "
            "functional final generation, though never told so -- would live for tens "
            "of thousands of years without producing children of their own, a detail "
            "underlying why Lauris's own conception absorbed the entirety of the "
            "civilization's remaining preservation capacity (MCD-159)."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
    # --- Optional texture: Era F ops 23-40 agent ---
    {
        "id": "MCD-1560",
        "category": "World Mechanics",
        "statement": (
            "Across her forty documented Sealbound Directorate contracts (Operations "
            "1-40, spanning the Apprentice, Established, Specialist, and "
            "Disillusionment sub-eras), Lauris terminated approximately 4,800 hostile "
            "subjects, cleared approximately 60 architectural sites of varying scale, "
            "conducted approximately 80 target acquisitions/terminations, and recovered "
            "approximately 14 sealed artifacts of various provenance -- completing "
            "every contract assigned to her without exception."
        ),
        "status": "locked",
        "source": SOURCE_MAIN,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 28, f"expected 28 new rules, got {len(NEW_RULES)}"
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    # Amend MCD-141: supersede in favor of MCD-151.
    amended = {"MCD-141": False, "MCD-212": False, "MCD-215": False}
    for r in ledger["rules"]:
        if r["id"] == "MCD-141":
            r["status"] = "superseded"
            r["note"] = (
                "Superseded by MCD-151, which directly contradicts this rule's claim "
                "that the Kareth War-Order's founding expedition left Kares Prime "
                "'during a period of catastrophic decline' -- MCD-151 states the "
                "expedition departed 'before any biological decline had begun.' "
                "Independently corroborated a third time by the Lauris Letitia "
                "Chronicle Companion Volume's own Era A material, which explicitly "
                "sides with MCD-151's framing. Abad's approval, Batch 291: \"approve\"."
            )
            amended["MCD-141"] = True
        elif r["id"] == "MCD-212":
            r["statement"] = r["statement"].replace(
                "roughly 4,000 years old, the final pure-blood Karesian",
                "roughly 6,000 years old (corrected from an earlier ~4,000 figure, "
                "MCD-1533), the final pure-blood Karesian",
            )
            amended["MCD-212"] = True
        elif r["id"] == "MCD-215":
            r["statement"] = r["statement"].replace(
                "no romantic partner across her roughly 4,000 years",
                "no romantic partner across her roughly 6,000 years (corrected from "
                "an earlier ~4,000 figure, MCD-1533)",
            )
            amended["MCD-215"] = True

    assert all(amended.values()), f"failed to amend: {amended}"

    ledger["batches_completed"].append(
        {
            "batch": 291,
            "date": str(date.today()),
            "source": SOURCE_MAIN,
            "rule_count": len(NEW_RULES),
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs found post-write!"

    print(
        f"OK. Total rules: {len(ledger['rules'])}. "
        f"Ledger version: {ledger['ledger_version']}. "
        f"Batches: {len(ledger['batches_completed'])}."
    )


if __name__ == "__main__":
    main()
