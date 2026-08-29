#!/usr/bin/env python3
"""Batch 41: Twenty_Two_Victories_Definitive_Edition -- Kanja's Rebellion, ages 18-30."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'Twenty_Two_Victories_Definitive_Edition.docx' (Google Drive fileId "
    "1UNgPMvWCgzMBRpFIS8xH6g0NW4VRX_pj), cross-checked and corrected "
    "against the actual written manuscript chapters (Chronicle_I through "
    "Chronicle_VIII.docx, Google Drive folder 1rxU-b1bySd0NVlxK91xNn4RtjyyKms-0), "
    "which take precedence as the higher-authority source over the "
    "planning-document chronicle for the eight battles both cover. "
    "Finalizes the pre-existing draft rule WC-023 (World Codex v3.4) with "
    "the source's own precise breakdown. Two proper-noun renames applied "
    "throughout, consistent with Batch 40's precedent: 'Verehimu Wetlands' "
    "and 'Verehimu Span' (generic geography, also misspelled 'Vegehimu' in "
    "places in the source) -> Voskharen Wetlands / Voskharen Span, distinct "
    "from House Verehimu. Two manuscript-vs-planning-document corrections "
    "applied per Abad's ruling: MCD-232's Trinity-deployment clause "
    "(Mafesto was already bonded ~2 years before Black Trench and worn "
    "dormant; Black Trench is its first combat deployment as part of the "
    "complete three-piece Trinity, not a partial deployment with Mafesto "
    "unbonded) and MCD-234's claim about where Kanja first met freed "
    "Cestari fighters (the manuscript's own opening line for Maw-9 states "
    "three of his earliest crew had already fought with him at the Black "
    "Trench one battle earlier). Two optional manuscript-detail "
    "enrichments confirmed by Abad: MCD-233 gains the decoy force and "
    "demolition-charge detail; MCD-235's cruiser count is tightened to "
    "match the manuscript exactly (one sunk, two beached and burned) and "
    "notes a confirmed-deliberate naming relation (the Ash-Wharf "
    "dispensary's Adessi is an elder relative of the already-locked Nelle "
    "Adessi, not the same person)."
)

NEW_RULES = [
    {
        "id": "MCD-230",
        "category": "World Mechanics",
        "statement": (
            "Kanja's Twenty-Two Victories (ages 18-30, 12 years) break "
            "down precisely as 10 Conventional Victories, 6 Unwinnable "
            "Victories (each earning a Directorate-classified alias), and "
            "6 Operational/labor-logistics Campaigns -- correcting the "
            "earlier draft's (WC-023) imprecise 'sixteen conventional' "
            "paraphrase (a secondary source's coarser bucketing of 10 "
            "Conventional plus 6 Campaigns together). Aliases in "
            "acquisition order: the Trench Monarch (18), Bane (19, Black "
            "Trench, Unwinnable), the Industrial Myth (19, first "
            "iteration, Furnace District Strike), the Blue-Collar Titan "
            "(20, Sewer War of Killane), Sovereign Ghost of the Great Sea "
            "(21, Ghost Harbor, Unwinnable), the Scourge (22, Ash-Wharf), "
            "the Crow King (23, Unwinnable), the Iron Bastard (25, "
            "Unwinnable), the Lord of Embers (27, Unwinnable), the Storm "
            "That Walks (29, Gale Straits, Unwinnable) -- and Captain, "
            "the one name that was never a Directorate classification."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-231",
        "category": "World Mechanics",
        "statement": (
            "The Scrip-Forge Raid and the Dredge-Line Ambush, his first "
            "actions. The Scrip-Forge Raid exposed Forge-7's Drakma-"
            "content debasement (38% declared vs. 14% actual) through "
            "charcoal-rubbing evidence and a controlled thermite fire -- "
            "no weapons, no casualties, establishing his signature method "
            "of exposing systemic theft through proof rather than "
            "violence at his very first engagement. The Dredge-Line "
            "Ambush (earning the Trench Monarch alias) flooded a canal "
            "district to drown a 200-soldier punitive column's density "
            "advantage in industrial sludge while his own lighter "
            "fighters crossed on planks above, establishing his "
            "career-defining doctrine: density is not power if the "
            "terrain neutralizes it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-232",
        "category": "World Mechanics",
        "statement": (
            "The Battle of the Black Trench (Bane alias, Unwinnable). "
            "Facing Suppression Brigade Kethane's 2,000 soldiers and "
            "three Titan-class enforcers, Kanja deliberately collapsed "
            "both exits of a rock ravine to seal himself inside with the "
            "Brigade, compressing their numerical advantage into "
            "uselessness; fought nine hours in chemical fog and emerged "
            "with 93 of 120 fighters against 1,400+ Brigade losses. This "
            "is the Trinity's first combat deployment as a complete "
            "system -- Mafesto had already been bonded roughly two years "
            "earlier and worn dormant, but Black Trench is the first time "
            "Onyx, Obsidian Malice, and Mafesto all went live together in "
            "the field. 'Bane' is the Directorate's own classification "
            "for a threat that destroys the force built to destroy it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-233",
        "category": "World Mechanics",
        "statement": (
            "The Battle of Iron Shallows, his first open-field "
            "engagement: used a coastal causeway's tidal cycle to strand "
            "a 400-soldier, twelve-hauler supply convoy in rising sand "
            "and seawater while his own baseline-density fighters crossed "
            "the exposed tidal flats unharmed, cementing the "
            "terrain-physics doctrine established at the Dredge-Line. A "
            "30-fighter decoy force under Efa Gol baited the escort "
            "infantry into a frontal deployment away from the crossing "
            "point, while Pell Ostra's crew planted six buried demolition "
            "charges timed to crack the causeway's shell surface so the "
            "haulers' own weight -- not the tide alone -- opened the "
            "sinking. No casualties on either side; no alias earned."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-234",
        "category": "World Mechanics",
        "statement": (
            "The Siege of Maw-9 and the Sewer War of Killane. Maw-9: "
            "freed roughly 12,000 Cestari by undermining the arena's own "
            "load-bearing foundation arches from tunnels below, "
            "collapsing the guard tiers under the garrison's own weight "
            "rather than attacking it directly. Three freed Cestari "
            "already fighting alongside Kanja by this point -- Corren "
            "Halst, Danne Sok, and Maret Vos -- had each been freed "
            "independently before Maw-9 (by the Black Trench, age 19), "
            "forming the nucleus of his earliest crew before the mass "
            "liberation; Maw-9 added further recruits to that existing "
            "core rather than being the original meeting point. The "
            "Sewer War of Killane (Blue-Collar Titan alias reinforced): "
            "an 80-fighter, six-week infiltration through Killane's "
            "forgotten pre-modern sewer layer that diverted 600 of the "
            "city's 1,200-soldier garrison chasing sabotaged "
            "infrastructure while copying the Southern District's "
            "Scrip-Registry ledger undetected for four months -- the "
            "battle marking fifteen-year-old Ezio Valcari's first on-page "
            "appearance, already eight months into work as a junior "
            "intelligence courier."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-235",
        "category": "World Mechanics",
        "statement": (
            "The Siege of the Ghost Harbor (Sovereign Ghost of the Great "
            "Sea alias, Unwinnable) and the Ash-Wharf Massacre (birth of "
            "the Scourge persona). Ghost Harbor: escaped a six-warship "
            "blockade of a landlocked basin by exploiting the tidal draft "
            "difference between his shallow fleet and the Trust's "
            "grounded destroyers, aided by a magnetic-interference weapon "
            "improvised from melted anchor chains aboard his flagship, "
            "The Audit (the Trust capital ship captured at Iron "
            "Shallows). Ash-Wharf: detonated his own 800-ton Dead Drakma "
            "stockpile to neutralize three Trust cruisers (one capsized "
            "and sank, two ran aground on the breakwater and burned) and "
            "save roughly 4,000 evacuated civilians from a punitive "
            "bombardment, standing in his own burning coat as the harbor "
            "burned -- the unplanned, emergent origin of the Scourge "
            "persona. The Ash-Wharf's medical dispensary was run by a "
            "woman named Adessi, an elder relative of the already-locked "
            "Nelle Adessi (a distinct person, a different era) -- noted "
            "here to preempt confusion between the two."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-236",
        "category": "World Mechanics",
        "statement": (
            "The Night of the Crow King (Unwinnable). Escaped Commandant "
            "Voris's mathematically airtight three-ring encirclement "
            "(signal-jammed, thermal-sensored, zero escape vectors) of "
            "his Voskharen Wetlands compound by inventing the Hymn-Engine "
            "on the spot: a synchronized ~19 Hz sub-bass work-chant sung "
            "by 300+ fighters that produced false thermal-sensor readings "
            "across the marsh, under cover of which the compound "
            "evacuated through hand-dug drainage channels; left a "
            "coat-and-feather-crown scarecrow on the empty command "
            "platform. This is the Hymn-Engine's origin -- the same "
            "technology already locked as part of his later 284-year Long "
            "Mask theatrical disguise system."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-237",
        "category": "World Mechanics",
        "statement": (
            "The Three-Day Blackout. Working with Anansi (established "
            "here as the rebellion's engineer) and Sephtis, used nine "
            "coordinated Hymn-Engine teams to overload the feedback loops "
            "of all nine Blight Frequency relay towers on the Jicome "
            "Eastern Seaboard simultaneously, scrambling continental "
            "biological suppression for three days -- the first mass "
            "demonstration that the Blight was an artificial technology, "
            "and Kanja's own first experience of unsuppressed biological "
            "potential, framed as planting the seed of the later "
            "Pi-Awakening."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-238",
        "category": "World Mechanics",
        "statement": (
            "The Iron Bastard's Stand (Unwinnable). Alone against a "
            "2,000-soldier armored column with twelve Trust Crawlers on "
            "open ground with no exploitable terrain, broadcast Dead "
            "Drakma's own resonance harmonic through the Aegis-Talisman, "
            "vibrating every piece of Trust equipment loose across the "
            "column for 90 minutes until it retreated -- exposing that "
            "the Sovereign Trust's entire military hardware base shared a "
            "single structural vulnerability."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-239",
        "category": "World Mechanics",
        "statement": (
            "The Sacking of Fort Tidewall, the rebellion's largest "
            "conventional victory: surveyed a coastal fortress's "
            "promontory geology by ear, tunneled up through natural "
            "sea-caves at low tide, and undermined three wall sections "
            "until the garrison's own weight collapsed them into stepped "
            "ramps rather than breaches -- 2,000 fighters took an "
            "'impregnable' 800-soldier fortress without siege equipment."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-240",
        "category": "World Mechanics",
        "statement": (
            "The Payroll Raid (Industrial Myth alias reinforced) and the "
            "Night of Ten Fires (Sephtis's first major operational "
            "command). Payroll Raid: stole the Southern Garrison's "
            "payroll ledger rather than its money, exposing an "
            "eleven-year, 40% wage-skimming scheme, then redistributed "
            "the actual withheld payroll to soldiers' families with "
            "receipts showing the shortfall in red ink -- triggering "
            "mutinies in three regiments. Night of Ten Fires: coordinated "
            "Anansi's Ghost-Lattice infiltrators to plant a "
            "low-temperature incendiary in the records offices (not the "
            "vaults) of all ten Jicome Scrip-Banking houses on a shared "
            "settlement night, destroying thirty days of transaction "
            "records and collapsing the banking network's fee-collection "
            "capacity for 23 months."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-241",
        "category": "World Mechanics",
        "statement": (
            "The Lord of Embers (Unwinnable) and the Rolling Foundry "
            "Campaign. After the Sovereign Trust burned the "
            "40,000-person Free Quarter as collective punishment, Kanja "
            "rebuilt it in fourteen days using Dead Drakma salvaged from "
            "the Trust's own abandoned incendiary equipment, recruiting "
            "6,000 new fighters in the process -- the Directorate's own "
            "threat assessment coined the alias, noting he 'metabolizes' "
            "punishment rather than retaliating against it. The Rolling "
            "Foundry Campaign: an eighteen-month tour of 31 coastal "
            "settlements aboard a converted ore-barge (The Anvil), "
            "providing free smithing, repairs, and militia training to "
            "roughly 120,000 people and connecting them to Anansi's "
            "Ghost-Lattice network."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-242",
        "category": "World Mechanics",
        "statement": (
            "The naval campaigns. The Midnight Freight War (age 21, six "
            "months): captured eighteen Trust cargo haulers by exploiting "
            "predictable night-watch lapses, accumulating the ~800 tons "
            "of Dead Drakma later sacrificed at Ash-Wharf and the "
            "communications equipment that seeded Anansi's Ghost-Lattice "
            "network. The Reef-Chain Blockade (age 22, Trench Monarch "
            "reinforced at sea): sank twelve scrap-laden derelict hulks "
            "to close the Kothrane Narrows for eleven weeks, scrambling "
            "Trust navigation and capturing a second warship, renamed The "
            "Receipt. The Battle of the Gale Straits (age 29, Storm That "
            "Walks alias, Unwinnable): drove a 22-ship arrowhead through "
            "the center of Admiral Dessius Krael's 40-warship envelopment "
            "twice, provoking a friendly-fire crossfire between the "
            "Trust's own flanks, then escaped into a storm predicted to "
            "the hour by Sephtis that the heavier Trust warships couldn't "
            "survive -- the Trust recovered only 20 of 40 warships, and "
            "Krael resigned."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-243",
        "category": "World Mechanics",
        "statement": (
            "The Battle of the Falling Bridge: the first recorded use of "
            "Mafesto's Kinetic Transfer System as a structural weapon. To "
            "save his column from pursuing cavalry, Kanja struck the "
            "center span of the Voskharen Span (renamed, same collision "
            "as the Wetlands above) with a full Mafesto discharge through "
            "Obsidian Malice, deliberately collapsing the section he "
            "himself stood on to drop 400 mounted pursuers into a "
            "200-meter gorge, then climbed the wreckage back to the rim."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-244",
        "category": "World Mechanics",
        "statement": (
            "The Furnace District Strike, the purest expression of the "
            "Industrial Myth alias. Unarmed and without fighters, Kanja "
            "spent four days asking 4,000 smelting-district workers a "
            "single question -- 'How much do they owe you?' -- and Ezio "
            "compiled their answers into a documented, deliberately "
            "unpayable debt structure (averaging 340% of annual "
            "earnings). The workers struck on their own initiative; "
            "Kanja stood at the gate without violence for eleven days "
            "until the Sovereign Trust renegotiated the district's terms "
            "-- his twenty-first victory, won without a single blow."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-245",
        "category": "World Mechanics",
        "statement": (
            "The Battle of the Sovereign Pier: the final battle and the "
            "Trinity's surrender (already locked in outline via the "
            "Sovereign Pier Accords and Codex Battle 10). King Maro "
            "personally asked his son to accept the Sovereign Trust's "
            "peace terms in exchange for surrendering Mafesto, Onyx, and "
            "Obsidian Malice; before Kanja could answer, a "
            "twelve-operative Trust assassination team attacked the pier "
            "as an insurance policy, and Kanja killed nine of them and "
            "drove three into the harbor in ninety seconds, protected "
            "from their Blight-projector sidearms by the active Living "
            "Drakma sealant he'd spent hours caulking a hull with. Kanja "
            "answered his father with a single word -- 'Yes' -- and "
            "surrendered the Trinity that night, beginning the "
            "already-locked 284-year Long Mask."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = (
    'Abad approved the full draft as pasted in-conversation, including the '
    'Verehimu->Voskharen rename, the two manuscript-corrected rules '
    '(MCD-232, MCD-234), and confirming the two optional enrichments '
    '(MCD-233, MCD-235) plus the Adessi family-relation clarification: '
    '"confirming optional tightenings. the woman is a relative much older"'
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

    # Retire the imprecise draft summary now finalized by MCD-230.
    for r in ledger["rules"]:
        if r["id"] == "WC-023":
            r["status"] = "superseded"
            r["note"] = "Superseded by MCD-230 (Batch 41), which corrects the imprecise '16 conventional' paraphrase with the source document's own precise 10+6+6 breakdown."
            break

    ledger["batches_completed"].append(
        {
            "batch": 41,
            "source_doc": "Twenty_Two_Victories_Definitive_Edition.docx, cross-checked against Chronicles I-VIII manuscript chapters",
            "source_id": "1UNgPMvWCgzMBRpFIS8xH6g0NW4VRX_pj",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 2,
            "conflicts_resolved": 2,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "4.4"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
