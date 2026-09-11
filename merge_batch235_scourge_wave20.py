#!/usr/bin/env python3
"""Batch 235: The Scourge Alias Chronicle wave 20 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Scourge's twentieth Alias Chronicle wave (MCD-1041 through MCD-1043), three entries "
    "exploring registers not yet used in the prior nineteen waves: a first three-way combat "
    "engagement (slavers and a Sovereign Trust salvage patrol both hostile for different reasons, "
    "age 58, V2 gear, extending MCD-1017's institutional-refusal doctrine into an active combat "
    "priority); a moral-complexity entry testing the crew's reunion-network doctrine against freed "
    "children with no traceable origin at all (age 142, V3 gear, extending MCD-1020's reunion-"
    "network thread into a case where the method itself doesn't apply); and a quieter closer where "
    "the non-lethal-surrender doctrine is enforced from within the crew, against a crew member's own "
    "rage, rather than tested by an outside party (age 190, V3 gear). One new minor, one-scene named "
    "character (Sena, a current crew member) was introduced in the closing entry, collision-checked "
    "against the full live ledger and confirmed clean; no other new named characters. Onyx of "
    "Oblivion correctly absent throughout per its L9 seal across the 284-year Long Mask (MCD-246, "
    "ARS-310). Abad's approval: \"doorway for all the aliases that remain\" (approval of Bane's "
    "individually-presented wave 20 plus blanket authorization to continue the same wave for the "
    "remaining ten aliases)."
)

NEW_RULES = [
    {
        "id": "MCD-1041",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Three-Cornered Fight\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-three-cornered-fight.md), The Scourge Alias "
            "Chronicle LVIII, wave 20. Age 58, V2 gear. A detailed combat showcase against two "
            "hostile parties who never coordinate with each other -- slavers trying to run captives "
            "out to a waiting Sovereign Trust salvage cutter, and the cutter's own crew trying to "
            "seize the ship's cargo as confiscated property under Trust salvage law. The Scourge "
            "frees the hold, denies both parties their claim, and disables the cutter's rigging with "
            "a single non-lethal Obsidian Malice discharge rather than letting either side identify "
            "him -- extending 'The Contract He Wouldn't Sign' (MCD-1017) into an operational "
            "priority: staying unclaimed by Trust jurisdiction even mid-rescue. Onyx of Oblivion "
            "correctly absent per its L9 seal. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1042",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ones Too Young to Say Where From\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ones-too-young-to-say-where-from.md), The Scourge "
            "Alias Chronicle LIX, wave 20. Age 142, V3 gear. A slaving depot's back compartment "
            "holds nineteen children, some born in captivity, none able to name a port or a family "
            "to be traced back to -- the crew's decades-old reunion-network doctrine (MCD-1020) has "
            "nothing to trace for the first time. Efa Gol and Kanja improvise a forward-looking use "
            "of the same network instead, vetting freed-captive settlements as placements rather "
            "than finding blood relatives, explicitly naming the guesswork involved and leaving the "
            "outcome of every placement unresolved and unknown for years. Onyx of Oblivion correctly "
            "absent per its L9 seal. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1043",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Blade She Almost Didn't Sheathe\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-blade-she-almost-didnt-sheathe.md), The Scourge "
            "Alias Chronicle LX, wave 20, closing the wave. Age 190, V3 gear. Sena, a new minor "
            "one-scene named crew member and former captive herself, nearly kills an already-"
            "surrendered slaving captain out of her own remembered trauma; Kanja talks her down "
            "without force, explaining the doctrine's real mechanism -- every honored surrender is "
            "future people who never have to be rescued because the fight never happens -- and she "
            "sheathes the blade herself, anger intact. The sub-series' first entry where the "
            "non-lethal-surrender doctrine is enforced from inside the crew rather than tested from "
            "outside or by Kanja's own temper (distinct from MCD-829, MCD-447, MCD-492). Onyx of "
            "Oblivion correctly absent per its L9 seal. Closes the Scourge's twentieth wave (with "
            "'The Three-Cornered Fight,' MCD-1041, and 'The Ones Too Young to Say Where From,' "
            "MCD-1042)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 3, f"expected 3 new rules, got {len(NEW_RULES)}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 235,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-11, no source document",
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
