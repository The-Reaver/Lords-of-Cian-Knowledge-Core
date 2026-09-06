#!/usr/bin/env python3
"""Batch 72: Efa Gol and Pell Ostra dossiers (roadmap Step 4, part 1).

Both were thin, single-mention crew members (MCD-233 only). Sourced
from the Chronicles I-VIII manuscript, already fetched in full for the
Step 3 rewrite pass (Batches 70-71) -- same pattern as Batch 48's
Hask/Breck/Maren dossiers: one identity/background rule, one arc rule,
per character."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Chronicles I-VIII manuscript (Google Drive, 'My Rivals Distance' folder), "
    "fetched in full for the Chronicles I-VIII rewrite pass (Batches 70-71), "
    "roadmap Step 4 backlog triage, 2026-09-06."
)

NEW_RULES = [
    {
        "id": "CC-130",
        "category": "character-crew",
        "statement": (
            "Efa Gol: a cargo-press operator at Warehouse Twelve before "
            "the rebellion, recruited in its early wave. Blunt, precise "
            "demeanor -- the text pairs her assessment style directly "
            "against panic: she reads a man surveying a problem "
            "correctly because she's done the same herself. Commands "
            "decoy and diversion forces repeatedly across the "
            "Rebellion: the 30-fighter decoy at Iron Shallows "
            "(MCD-233, age 19) and, per Chronicle VII/VIII's own "
            "back-references, the diversion force at the Maw-9 "
            "liberation (age 20) as well -- nothing in MCD-234 names a "
            "diversion commander, so this extends rather than "
            "conflicts with it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-131",
        "category": "character-crew",
        "statement": (
            "Efa Gol's pair-partner, dock rigger Tam Sullen (31), dies "
            "under her watch at the Black Trench (age 19) -- she kills "
            "the two soldiers responsible, covers Sullen's body so the "
            "enemy can't count the dead, and her hands shake for "
            "exactly ten seconds before she picks her weapon back up "
            "and returns to the fog alone, re-pairing with another "
            "single fighter rather than breaking the way Callum Breck "
            "does after Nev Torr's death (CC-119) -- the text frames "
            "this as the crew's pair-system design working as "
            "intended, not as Gol being harder than Breck. Pilots the "
            "fourth ship through Ghost Harbor's reef gap (age 21), "
            "trusting Breck's called bearing outright. Commands the "
            "wharf evacuation's crowd flow at the Ash-Wharf Massacre "
            "(age 22, MCD-242), her voice 'a current' civilians follow "
            "without needing it raised."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-132",
        "category": "character-crew",
        "statement": (
            "Pell Ostra: a demolitions and chemistry specialist present "
            "from the Black Trench onward (age 19) -- no recruitment "
            "origin is given in the source material, so none is "
            "asserted here. Marked by a signature trait distinct from "
            "every other named crew member: she talks to her materials "
            "rather than to people, addressing charges, acid, and "
            "compounds by what she's asking them to do, the way a "
            "colleague requests cooperation rather than commands "
            "obedience."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-133",
        "category": "character-crew",
        "statement": (
            "Pell Ostra's arc: inspects and resolders the detonation "
            "wiring at the Black Trench (age 19), improvising thrown "
            "shear-pins mid-battle as the most precisely balanced "
            "objects she owns. Part of the six-charge demolition crew "
            "at Iron Shallows (MCD-233, age 19). At Killane (age 20), "
            "collects hydrochloric waste-pipe acid over four days to "
            "dissolve the Registry vault's mortar ceiling and "
            "separately loosens the garrison's artillery-platform "
            "bolts with the same compound. At Ghost Harbor (age 21), "
            "works incendiary devices during the siege's waiting "
            "period. At the Ash-Wharf Massacre (age 22, MCD-242), "
            "scales the Scrip-Forge Raid's original accelerant by "
            "roughly a thousandfold to detonate the rebellion's entire "
            "800-ton Dead Drakma stockpile rather than let it fall "
            "into a naval engagement that would kill more civilians "
            "than the bombardment itself -- asks no questions, "
            "understanding the arithmetic ('supplies rebuild... the "
            "dead do not') as her own form of the crew's shared ethic."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "lock it"'


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
            "batch": 72,
            "source_doc": (
                "Roadmap Step 4 backlog triage, part 1: Efa Gol and "
                "Pell Ostra dossiers (CC-130 through CC-133), sourced "
                "from the Chronicles I-VIII manuscript already fetched "
                "for Batches 70-71, matching the Batch 48 Hask/Breck/"
                "Maren dossier pattern."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "7.5"
    ledger["last_updated"] = "2026-09-06"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
