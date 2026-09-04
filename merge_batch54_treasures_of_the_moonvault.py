#!/usr/bin/env python3
"""Batch 54: Phase 1b, fourth document. Treasures of the Moonvault --
the Moonvault setting, Haryn Dael, the Guild-Doctrine, and the
Ever-Haunt rescue operation, plus full mechanics for the five already-
named-only gifts (ARS-330/ARS-340) this document confirms, plus four
newly invented treasures (two per Abad's request) completing all but
one of the ten-gift roster."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE_DOC = (
    "Treasures_of_the_Moonvault (Google Drive fileId "
    "1M0xmfcORo_84LKW9pjtlWhDU2M2mYRQu7BSlBJ4PLsU, the Lore Vault copy). "
    "Fourth document drafted under Phase 1b of the pre-Book-1-era "
    "roadmap. MCD-288 (Batch 49) already resolved this document's own "
    "six-gift list as an earlier draft superseded by the real locked "
    "rosters (ARS-330 Sovereign's Five, ARS-340 Captain's Five); the "
    "setting material (Moonvault, Haryn Dael, Guild-Doctrine, the "
    "Ever-Haunt rescue) was explicitly unaffected by that superseding "
    "and is drafted fresh here. Three of the five items in this "
    "document that also appear by name in ARS-330 (Wellspring Seal, "
    "Conviction, Vigil Standard) and two that appear in ARS-340 "
    "(Foldtide, Forgewright) are confirmed matches, so their full "
    "mechanics are locked from this source; 'the Suture' does not "
    "survive per MCD-288 and is not drafted."
)

SOURCE_INVENTED = (
    "Original invention, chat-drafted 2026-09-04, no source document -- "
    "per Abad's request to add two new treasures each for Ozmund and "
    "Kanja, filling in the remaining ARS-330/ARS-340 named-only slots "
    "(Bastion, King's Mantle for Ozmund; two of Undertow/Lodestone Lens/"
    "Whalebone Tether for Kanja), following the source document's own "
    "Norse-artifact homage pattern."
)

NEW_RULES = [
    {
        "id": "MCD-315",
        "category": "World Mechanics",
        "statement": (
            "The Moonvault: a hidden settlement of ~2,000 in a volcanic "
            "caldera roughly 800km beyond the Frontier Maw, its "
            "chimney-opened geometry channeling moonlight onto the only "
            "known Living Drakma deposit outside Jicome's Mao Volcano. "
            "Moonlight-forged Living Drakma achieves a lattice "
            "coherence the Mao Volcano's heat-forcing can't replicate, "
            "making Moonvault work the finest in the world for over six "
            "thousand years."
        ),
        "status": "locked",
        "source": SOURCE_DOC,
    },
    {
        "id": "MCD-316",
        "category": "World Mechanics",
        "statement": (
            "Haryn Dael: the Moonvault's ~4,200-year-old elder smith "
            "and de facto leader by accrued authority, not title. He "
            "refused the Old Dominion's choice between industrializing "
            "his craft or being treated as a security threat, walking "
            "into the Shattered Kingdoms until he found moonlight "
            "reaching Living Drakma ore. His mastery exceeds Kanja's by "
            "generational depth, not competition -- four millennia of "
            "practice versus three centuries."
        ),
        "status": "locked",
        "source": SOURCE_DOC,
    },
    {
        "id": "MCD-317",
        "category": "World Mechanics",
        "statement": (
            "The Guild-Doctrine: the forging tradition that originated "
            "Onyx of Oblivion's lineage (not this specific caldera, but "
            "this tradition), predating the Old Dominion by at least a "
            "thousand years. Its methodology is resonance -- singing "
            "frequencies the Living Drakma's sentient lattice "
            "recognizes and responds to -- rather than the Mao "
            "Volcano's heat-forcing; the smiths who refused T.D.K.'s "
            "industrialization demand were driven to the margins and "
            "eventually found the Moonvault."
        ),
        "status": "locked",
        "source": SOURCE_DOC,
    },
    {
        "id": "MCD-318",
        "category": "World Mechanics",
        "statement": (
            "The Rescue: the Moonvault's Living Drakma resonance, "
            "masked for six thousand years by the Shattered Kingdoms' "
            "ambient geological noise, became detectable when T.D.K.'s "
            "intensifying Ionic Rite operations stripped that masking "
            "away. Three Tier-2 Ever-Haunt entities besieged the "
            "caldera rim, smothering its moonlight rather than "
            "attacking directly. Kanja and Ozmund -- the first joint "
            "operation between the cousins since their mothers' "
            "generation -- cleared the siege in roughly fourteen hours "
            "without a Density Spike (too destructive for the unstable "
            "chimney structure), relying on Kanja's Forge-Coat loadout "
            "and engineering instead. Haryn recognized both men's "
            "nature on sight: Onyx's lattice pattern on Kanja's arm, "
            "and the Crown-Scar's architecture read through craft-sight "
            "on Ozmund."
        ),
        "status": "locked",
        "source": SOURCE_DOC,
    },
    {
        "id": "ARS-375",
        "category": "avatar-arsenal",
        "statement": (
            "The Wellspring Seal (Ozmund, Sovereign's Five): a Living "
            "Drakma disk that catalyzes accelerated geological "
            "refinement in contact with raw Root-Metal veins, "
            "concentrating base metals and crystallizing Voidstone "
            "precursors -- producing wealth outside the Trust's "
            "Scrip/Tether system entirely. It accelerates existing "
            "geological richness rather than creating material from "
            "nothing; a depleted vein still produces nothing."
        ),
        "status": "locked",
        "source": SOURCE_DOC,
    },
    {
        "id": "ARS-376",
        "category": "avatar-arsenal",
        "statement": (
            "The Conviction (Ozmund, Sovereign's Five): a bio-bonded "
            "Living Drakma war-lance giving Ozmund's close-range "
            "arsenal (Dragondal, Shadow's Whisper) the reach it lacks. "
            "Thrown with Density Spike active, it delivers concentrated "
            "peak-density impact through a blade-point contact area, "
            "then lattice-contracts back to its bonded wielder -- a "
            "roughly eight-second return window that leaves him without "
            "a ranged option in the interim."
        ),
        "status": "locked",
        "source": SOURCE_DOC,
    },
    {
        "id": "ARS-377",
        "category": "avatar-arsenal",
        "statement": (
            "The Vigil Standard (Ozmund, Sovereign's Five, for the "
            "Unchained Legion): a war-standard whose Living Drakma "
            "sphere neutralizes Blight Frequency suppression within a "
            "400-meter radius, letting a marching column of freed "
            "Cestari operate at true biological density rather than "
            "Tether-managed levels; its sustained amber-gold glow "
            "(visible ~2km) doubles as a battlefield rally point. The "
            "radius is fixed and cannot be safely amplified."
        ),
        "status": "locked",
        "source": SOURCE_DOC,
    },
    {
        "id": "ARS-378",
        "category": "avatar-arsenal",
        "statement": (
            "The Foldtide (Kanja, Captain's Five): a Living-Drakma-"
            "channeled warship (~40m, 12 cannon mounts, crew 120) with "
            "three escort vessels, all bio-bonded to fold -- escorts "
            "nesting inside the warship's hull, the whole fleet "
            "compressing into a carryable ~1.2m chest -- and unfold to "
            "full battle readiness in about four minutes. Requires 48 "
            "hours of moonlight exposure between deployments for "
            "lattice recovery; not usable for rapid retract-deploy "
            "cycling."
        ),
        "status": "locked",
        "source": SOURCE_DOC,
    },
    {
        "id": "ARS-379",
        "category": "avatar-arsenal",
        "statement": (
            "The Forgewright (Kanja, Captain's Five): a Living Drakma "
            "smith's hammer enabling Guild-Doctrine resonance forging "
            "(communicating structural intent directly to ore's "
            "sentient lattice) rather than the Mao Volcano's "
            "heat-forcing -- the interface that lets Kanja's existing "
            "theoretical knowledge (from Onyx's lattice-memory) become "
            "physically practicable, closing much of the gap to the "
            "Moonvault's own masters without erasing the generational "
            "difference (MCD-316)."
        ),
        "status": "locked",
        "source": SOURCE_DOC,
    },
    {
        "id": "ARS-380",
        "category": "avatar-arsenal",
        "statement": (
            "Bastion (Ozmund, Sovereign's Five): homage to Svalinn, the "
            "shield standing before the sun to protect the world from "
            "scorching. A Living Drakma plate that, driven into open "
            "ground, roots and grows into a defensive rampart within "
            "minutes via the same resonance-growth principle as the "
            "non-surviving Suture (MCD-288) -- redirected toward "
            "creating new fortification rather than repairing existing "
            "structure. Built for sheltering refugee columns overnight "
            "in hostile, unfortified territory, the Unchained Legion's "
            "most persistent tactical gap."
        ),
        "status": "locked",
        "source": SOURCE_INVENTED,
    },
    {
        "id": "ARS-381",
        "category": "avatar-arsenal",
        "statement": (
            "King's Mantle (Ozmund, Sovereign's Five): homage to "
            "Brisingamen, Freyja's sovereignty necklace. A worn Living "
            "Drakma garment that visibly signals when Ozmund's issued "
            "command is genuinely his own will versus an attempt by the "
            "Crown-Scar's command architecture to assert itself -- "
            "addressing, not curing, his established loyalty-"
            "uncertainty problem (extends MCD-052/MCD-290) by giving "
            "him and his soldiers a legible, external instrument of "
            "trust rather than blind faith in a scar he didn't choose."
        ),
        "status": "locked",
        "source": SOURCE_INVENTED,
    },
    {
        "id": "ARS-382",
        "category": "avatar-arsenal",
        "statement": (
            "The Lodestone Lens (Kanja, Captain's Five): homage to "
            "Heimdall's sight, seeing a hundred leagues and hearing "
            "grass grow. A Living Drakma lens extending Kanja's Rex "
            "tactile-geological and Mar current-reading senses (extends "
            "MCD-294/295) to extreme range from a ship's deck or "
            "vantage point -- reading coastline, seafloor composition, "
            "and Drakma-bearing terrain well beyond unaided range, "
            "complementing rather than duplicating the Sovereign Eyes' "
            "close-range Blueprint Eye HUD."
        ),
        "status": "locked",
        "source": SOURCE_INVENTED,
    },
    {
        "id": "ARS-383",
        "category": "avatar-arsenal",
        "statement": (
            "The Whalebone Tether (Kanja, Captain's Five): homage to "
            "Gleipnir, the impossible binding that chained Fenrir. A "
            "whalebone-cored Living Drakma line, unbreakable under "
            "conventional force, serving as the Foldtide's anchor-"
            "tether when folded or docked -- and, rarely, as one of the "
            "few tools capable of temporarily restraining a Titan-class "
            "target, since ordinary bindings fail against that scale of "
            "strength. Undertow, the fifth Captain's-Five item, remains "
            "undetailed and open for a future pass."
        ),
        "status": "locked",
        "source": SOURCE_INVENTED,
    },
]

BATCH_NOTE = 'Abad approved the full draft as pasted in-conversation: "lock"'


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
            "batch": 54,
            "source_doc": "Treasures_of_the_Moonvault -- Phase 1b, fourth document: the Moonvault setting, Haryn Dael, the Guild-Doctrine, and the Ever-Haunt rescue, plus full mechanics for five already-named gifts, plus four newly invented treasures (Bastion, King's Mantle, the Lodestone Lens, the Whalebone Tether) completing 9 of the 10-gift roster",
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "5.7"
    ledger["last_updated"] = "2026-09-04"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
