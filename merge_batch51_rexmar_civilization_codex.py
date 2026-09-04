#!/usr/bin/env python3
"""Batch 51: Phase 1b, second document. The Rexmar Civilization Codex
Entry -- the Rex and Mar bloodlines, the Haku designation and lineage,
the Drakma tradition and variant taxonomy, the Fall and Recovery Point,
and the Rexmar combat tradition. 19 new MCD- rules, all extending
already-locked material rather than introducing standalone new lore."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Rexmar_Civilization_Codex_Entry.docx (Google Drive fileId "
    "1dNbJttiWk1HK7cmPI8JP_SUd9xyFqPvQ, the Lore Vault copy -- two other "
    "non-Lore-Vault copies exist, an identical Google Doc conversion and "
    "an earlier draft with a differing byline; the Lore Vault .docx was "
    "used as primary per the ledger's own authority_order rule). Second "
    "document drafted under Phase 1b of the pre-Book-1-era roadmap; this "
    "document is also the original source for two contradictions Batch "
    "49 already resolved (WC-005's Pi-Awakening reframe, MCD-221's Line "
    "front roster). Two items were flagged to Abad before drafting and "
    "resolved by his explicit ruling: pre-Kanja Rexmar longevity via "
    "indomitable will rather than biological enhancement (resolves the "
    "Val Saeryn Kareth/Maro Rexmar timeline question, MCD-309/MCD-310), "
    "and the extraction era ('The Fall') being read as institutional/"
    "prominence decline rather than any loss of individual capability "
    "(MCD-308). Haku the Unifier's fate is deliberately left unaddressed "
    "per Abad's own instruction, not asserted either way. One further "
    "reconciliation applied using this project's established "
    "compatible-reading precedent, not separately escalated: the "
    "Dark-Drakma material contradiction with the already-locked ARS-348 "
    "(Living Drakma) resolved as a folding technique normally applied to "
    "Dead Drakma, with Kanja's Forge-Coat as a documented rare exception "
    "(MCD-302)."
)

NEW_RULES = [
    {
        "id": "MCD-294",
        "category": "World Mechanics",
        "statement": (
            "The Rex bloodline: mountain people of Jicome's volcanic "
            "highlands, positional combat doctrine (hold ground, "
            "fortify, convert terrain into a killing field), broad "
            "frames and core-concentrated musculature built for "
            "sustained load-bearing defense. Their forging tradition "
            "began as stubborn mining rather than smithing mastery; "
            "millennia of tactile contact with raw Drakma in volcanic "
            "seams produced a biologically inherited "
            "metallic-composition sensitivity no other population has."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-295",
        "category": "World Mechanics",
        "statement": (
            "The Mar bloodline: sea people of Jicome's coastline and "
            "archipelago, kinetic combat doctrine (strike, withdraw, "
            "reposition, using the sea's mechanics as a weapon), long "
            "limbs and fast-twitch musculature with oxygen-processing "
            "rates beyond standard biology. Their navigation tradition "
            "(barometric pressure read through inner-ear sensitivity, "
            "storms predicted by tasting salt content) is the Mar "
            "counterpart to the Rex forging tradition -- reading water "
            "instead of stone."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-296",
        "category": "World Mechanics",
        "statement": (
            "The War of the Two Crowns and the Unification: roughly 400 "
            "years of internal Rex-Mar warfare, reducing the combined "
            "population by approximately 60%, ending not in treaty but "
            "in a founding marriage. The first Rexmar child expressed "
            "both bloodlines simultaneously -- Rex positional stability "
            "and Mar kinetic fluidity without compromise in either "
            "direction -- a combat architecture neither line could "
            "produce alone."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-297",
        "category": "World Mechanics",
        "statement": (
            "The Haku designation: not a conferred title but a "
            "biological marker, observed rather than ceremonially "
            "awarded, confirmed when an individual's body expresses "
            "full Rex-Mar convergence. Rex means king of land, Mar "
            "means king of sea, Haku is the point where both converge; "
            "'Rexmar' itself originates from Haku's marriage to his "
            "bride. The designation appears irregularly across "
            "generations, sometimes skipping twenty."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-298",
        "category": "World Mechanics",
        "statement": (
            "The Brutality-to-Peace Evolution: pre-unification Rex and "
            "Mar were the most violent peoples in the world, a response "
            "to Jicome's lethal geology and seas rather than cultural "
            "deficiency. The War of the Two Crowns' near-self-extinction "
            "forced a deliberate, engineered peace -- violence redirected "
            "and subordinated to collective survival rather than "
            "eliminated. This is the direct cultural inheritance Kanja "
            "draws on: a leader who treats violence as a costed tool, "
            "not because he lacks the capacity for it, but because his "
            "civilization already paid its price in full once."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-299",
        "category": "World Mechanics",
        "statement": (
            "Jicome's unconquered status: volcanic highlands and mapped "
            "reef systems make the terrain itself the primary defender, "
            "with seismic/toxic/lava hazards the Rexmar people have "
            "tracked for millennia doing work no army needs to. Rexmar "
            "military doctrine is organizational rather than numerical "
            "-- every fighter trained in both positional and kinetic "
            "combat, with no separate infantry/naval divisions. Extends "
            "the already-locked Pre-Awakening Theatrics System's "
            "Hymn-Engine (ARS-310): the crew's acoustic "
            "Hymn-synchronization is the direct descendant of this same "
            "battlefield coordination tradition, not a Kanja invention "
            "from nothing."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-300",
        "category": "World Mechanics",
        "statement": (
            "The Drakma Monopoly and labor-warfare integration: Jicome's "
            "indispensability (sole Drakma source) rather than military "
            "strength is what has kept it unconquered -- conquest "
            "destroys the forging infrastructure conquest would want, "
            "so every power that calculated the arithmetic chose "
            "negotiation over invasion, T.D.K. included. Rexmar "
            "doctrine draws no line between soldier and worker: smiths "
            "are trained to wield what they forge, shipwrights to fight "
            "from what they build, giving an effectively 100% adult "
            "combatant mobilization rate, each one a specialist "
            "defending infrastructure they personally understand."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-301",
        "category": "World Mechanics",
        "statement": (
            "Drakma physics: a metallic lattice compound unique to "
            "Jicome's geology, responsive rather than alive -- its "
            "molecular bonding shifts measurably in response to "
            "biological contact (pressure, temperature, bioelectric "
            "signature) without implying agency. Dead Drakma is the "
            "lattice extracted and stabilized into a fixed, "
            "biologically inert crystalline state -- structurally "
            "superior, enduring, the world's standard high-tier "
            "engineering material. Living Drakma retains full "
            "biological responsiveness, bonding with and adapting to "
            "its wielder; producing it requires the Rexmar biological "
            "inheritance and is otherwise impossible."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-302",
        "category": "World Mechanics",
        "statement": (
            "The Drakma Variant Taxonomy, extending MCD-023/CC-003 "
            "(Bio-Drakma) and ARS-343 (Dead-Light Drakma): beyond Dead "
            "and Living Drakma (MCD-301), six named variants exist -- "
            "Dead-Light Drakma (vantablack, light-absorbing; per ARS-343 "
            "this names Onyx of Oblivion's outward finish, not a "
            "separate base composition, consistent with this document's "
            "own simplified reference use of the term); Dark-Drakma (a "
            "Damascus-pattern folding technique producing layered "
            "density gradients, standardly applied to Dead Drakma -- "
            "this is the composition of a named but otherwise "
            "undetailed item, 'the Old Dragon' -- with Kanja's own "
            "Forge-Coat leather (ARS-348) as a rare exception where his "
            "unmatched mastery applies the same folding technique to "
            "Living Drakma instead, not a contradiction of the standard "
            "definition); Tool Drakma (impact-storage, Obsidian Malice's "
            "composition, consistent with its already-locked "
            "delayed-discharge mechanic); Bio-Drakma (biological "
            "integration via bloodstream, Kanja's skeleton after 300 "
            "years of Internal Quench, already locked); Heritage Drakma "
            "(carries prior wielders' impact memory -- Mafesto carries "
            "the legacy of three named Rexmar ancestors, Turey, Amaru, "
            "Yabura, matching the already-locked royal genealogy "
            "exactly); Impact-Drakma (non-Newtonian, flexible until "
            "impact then instantly rigid, Anansi's suit composition)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-303",
        "category": "World Mechanics",
        "statement": (
            "Why Jicome is Drakma's sole source and the forging "
            "tradition can't be replicated elsewhere: three "
            "simultaneous geological conditions (a unique magma/"
            "deep-ocean-substrate pressure environment, millennia of "
            "sustained thermal cycling, and trace mineral content in "
            "the groundwater) exist nowhere else and can't be "
            "industrially synthesized -- attempts produce only inferior "
            "Dead-Drakma approximations. Separately, raw Drakma requires "
            "Rexmar hands specifically: a tactile sensitivity to lattice "
            "structure developed across millennia of contact, without "
            "which a smith works the material blind. Kanja, carrying "
            "both the Rex tactile inheritance and the Mar "
            "material-reading instinct, is the convergence point of "
            "both requirements at once."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-304",
        "category": "World Mechanics",
        "statement": (
            "Haku the Unifier's method, roughly 5,000 years before Book "
            "1: he unified the remaining warring Rexmar tribes not "
            "through campaign but through single combat, deliberately "
            "including handicap matches (fighting two or three of a "
            "tribe's best simultaneously), then declining to occupy or "
            "garrison the tribes he defeated -- staying instead to build "
            "alongside the warriors he'd just beaten. This is the "
            "detail that made the unification read as legitimate rather "
            "than imposed: strength demonstrated in the only terms the "
            "tribes already respected, followed by showing them what "
            "that strength was for."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-305",
        "category": "World Mechanics",
        "statement": (
            "Extends the already-locked Deposition rules (Anu Un Ra's "
            "strategic withdrawal ~5,000 years ago, precipitated by "
            "Haku's overstretch campaigns and Verehimu's betrayal): "
            "Haku's Pi-Awakened biology itself actively degraded "
            "T.D.K.'s operational infrastructure in the engagement zone "
            "during the campaign -- his Predictive Oracles lost "
            "accuracy, his containment protocols failed, his Champions "
            "suffered resonance effects making sustained engagement with "
            "Haku impossible. General Baryon's single scar above his "
            "left eye dates from these campaigns; Sereth Vaul's "
            "already-locked 314-year Karkosa Preparation (Silencer's "
            "operation) is built on studying the pre-Awakening signature "
            "approximation these campaigns first exposed."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-306",
        "category": "World Mechanics",
        "statement": (
            "The biological dimension of the Pi-Awakening: T.D.K.'s "
            "Exchange Protocol can adapt to augmented density and to "
            "cultivated refinement, but not to the Pi-Awakening "
            "frequency, because adaptation requires modeling the "
            "biological architecture producing it, and that "
            "architecture (the Rex-Mar bloodline convergence, tested "
            "repeatedly against the hardest available opposition at "
            "deliberate disadvantage) cannot be modeled without "
            "replicating conditions T.D.K. cannot reproduce. He "
            "calculated for a Pi-Awakened Rexmar appearing again. He "
            "did not calculate for the recovery point's specific origin "
            "(MCD-310)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-307",
        "category": "World Mechanics",
        "statement": (
            "Why Kanja carries the Haku name: not honorific, but the "
            "Rexmar bloodline's own biological confirmation, identified "
            "from birth as matching or exceeding the convergence that "
            "forced T.D.K.'s withdrawal. Already extends the locked fact "
            "that 'Haku' is Kanja's middle name taken from this ancestor "
            "-- this adds that the naming was observation of an "
            "already-present fact, not aspiration or ceremony."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-308",
        "category": "World Mechanics",
        "statement": (
            "The Fall, per Abad's explicit ruling: what the Old "
            "Dominion's centuries-long extraction (knowledge "
            "acquisition, dependency creation through industrial Dead "
            "Drakma facilities, cultural erosion via institutional "
            "displacement, and generational attrition) actually broke "
            "down was the Rexmar people's influence, territorial "
            "prominence, and institutional protection of their land and "
            "sea holdings -- not their individual combat or forging "
            "capability, which persisted intact throughout. The "
            "Sovereign Trust's later Blight Frequency suppression is a "
            "separate, additional biological-suppression layer on top "
            "of this institutional decline, not evidence the decline "
            "itself was ever a capability loss."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-309",
        "category": "World Mechanics",
        "statement": (
            "Per Abad's explicit ruling: pre-Kanja Rexmar bloodline "
            "members (Rex and Mar alike) are not biologically enhanced "
            "the way Kanja is, but are capable of unusually long "
            "lifespans through indomitable will and spirit rather than "
            "biology -- consistent with this world's general "
            "long-lifespan convention without requiring Karesian blood. "
            "This is what makes it plausible for a figure like Maro "
            "Rexmar to have lived across a very long span; it is "
            "deliberately NOT extended to assert anything about Haku "
            "the Unifier's own fate, which stays unaddressed and open."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-310",
        "category": "World Mechanics",
        "statement": (
            "Kanja as the Recovery Point: his birth converges two "
            "bloodlines the extraction (MCD-308) was structured to keep "
            "separate -- the Rexmar forging/combat inheritance, and the "
            "Karesian inheritance through his mother, Val Saeryn Kareth, "
            "which gives him the Kinetic Concentration/density "
            "architecture the Rexmar line alone does not carry. Val "
            "Saeryn identified the Pi-Awakening frequency as T.D.K.'s "
            "one unprocessable vulnerability and chose Maro Rexmar "
            "accordingly, well before the genuine love that followed -- "
            "both true at once, and viable across the long span "
            "involved per MCD-309."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-311",
        "category": "World Mechanics",
        "statement": (
            "The Rexmar combat tradition is an engineering discipline "
            "applied to violence, not a martial art: fighters are "
            "taught structural analysis (identifying a target's failure "
            "point, applying force the way a smith strikes a flawed "
            "weld) rather than forms. This is biological, not merely "
            "trained -- Rex inheritance produces instinctive "
            "load-distribution reading (from millennia of rock-face and "
            "fortification analysis), Mar inheritance produces "
            "instinctive motion-as-geometry tracking (from millennia of "
            "current and tidal-shift reading), and the Haku convergence "
            "expresses both simultaneously, which is why an "
            "eighteen-year-old Kanja with no formal military training "
            "could produce results the Sovereign Trust's own analysts "
            "classified as unwinnable."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-312",
        "category": "World Mechanics",
        "statement": (
            "The Leadership Template and the Twenty-Two Victories, "
            "extending MCD-230/232/234/242: Kanja's crew-building "
            "repeats Haku's unification method (MCD-304) at individual "
            "scale -- demonstrating supremacy in terms already "
            "respected, then showing what that supremacy is for, rather "
            "than recruiting through offered power or position. The "
            "Twenty-Two Victories read the same way: each was an "
            "engineering solution to a labor or military problem (the "
            "Scrip-Forge Raid as labor action, the Sewer War of Killane "
            "using mining-terrain knowledge, etc.), consistent with and "
            "extending rather than duplicating the already-locked battle "
            "roster. New tactical detail for the already-named, "
            "already-counted 'Storm That Walks' Unwinnable Victory (age "
            "29, Gale Straits, MCD-230): twelve raiders driven through "
            "forty warships in arrowhead formation, twice, escaping "
            "into a storm."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full draft as pasted in-conversation: "lockes"'


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
            "batch": 51,
            "source_doc": "Rexmar_Civilization_Codex_Entry.docx -- Phase 1b, second document: the Rex/Mar bloodlines, the Haku designation and lineage, the Drakma tradition and variant taxonomy, the Fall and Recovery Point, and the Rexmar combat tradition",
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 3,
            "conflicts_resolved": 3,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "5.4"
    ledger["last_updated"] = "2026-09-04"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
