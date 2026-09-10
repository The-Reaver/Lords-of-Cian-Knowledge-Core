#!/usr/bin/env python3
"""Batch 114: Lock the Lord of Embers' three-entry Alias Chronicle wave (MCD-389 through
MCD-391), continuing uninterrupted through the remaining alias waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-10, no source document."

BATCH_NOTE = (
    'Abad: "continue uninterrupted until completion this includes test, commit, push to main '
    'origin" (covering all ten remaining alias waves).'
)

NEW_RULES = [
    {
        "id": "MCD-389",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Second Burning\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-second-burning.md), Lord of Embers Alias "
            "Chronicle I. Rebellion era, weeks after the Free Quarter's fourteen-day rebuild "
            "(MCD-241, age 27). A garrison prefect, believing the first rebuild succeeded only "
            "because of salvaged Trust incendiary equipment, burns a second district and recovers "
            "every scrap before withdrawing; Kanja and 6,000 fighters rebuild in eleven days "
            "anyway, stripping the district's own undamaged western half for material rather than "
            "relying on salvage, proving the alias's 'metabolizes punishment' trait was never "
            "about equipment. The prefect's own report is quoted: 'material denial achieved; "
            "strategic objective not achieved; unknown variable identified as the population "
            "itself.' No new named characters. First entry in the Lord of Embers' three-Chronicle "
            "wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-390",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Forge Refused to Return\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-forge-refused-to-return.md), Lord of Embers "
            "Alias Chronicle II. Rebellion era, during the Rolling Foundry Campaign (MCD-241, age "
            "27), aboard The Anvil. A raiding detachment strikes an active re-forging session at "
            "a coastal settlement with incendiary charges; Kanja fights deliberately away from "
            "the forge and its sixty unarmed apprentices, demonstrating Mafesto's Kinetic "
            "Transfer System absorbing a thrown charge's blast directly into stored kinetic "
            "charge, Obsidian Malice discharging it into the raiders' line, and Onyx's Cadence "
            "Ruin redirecting a three-charge volley as one collapsible pattern into open water. "
            "No apprentice is harmed and the season's tool-stock finishes on schedule. No new "
            "named characters. Second entry in the Lord of Embers' three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-391",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"An Apprenticeship That Outlasted the War\" (full narrative text at "
            "docs/lords-of-cian/chronicles/an-apprenticeship-that-outlasted-the-war.md), Lord of "
            "Embers Alias Chronicle III, closing the wave. Set during the Rolling Foundry "
            "Campaign (MCD-241), from the perspective of a fourteen-year-old settlement resident "
            "(one of the 120,000 reached across the eighteen-month tour) whom Kanja personally "
            "teaches to true a bent hinge, using the lesson to speak obliquely about patience "
            "under pressure. She becomes her settlement's own smith and, decades later, passes "
            "the same lesson to her own apprentices. No new named characters. Closes the Lord of "
            "Embers' three-Chronicle wave (with 'The Second Burning,' MCD-389, and 'What the "
            "Forge Refused to Return,' MCD-390)."
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

    ledger["batches_completed"].append(
        {
            "batch": 114,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Lord of Embers' three-entry Alias Chronicle wave (MCD-389 through "
                "MCD-391), the eighth of ten remaining alias waves. " + BATCH_NOTE
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
