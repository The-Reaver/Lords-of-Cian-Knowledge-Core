#!/usr/bin/env python3
"""Batch 189: Lock the Lord of Embers' fifth three-entry Alias Chronicle wave (MCD-552 through
MCD-554), continuing uninterrupted per Abad's authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do a wave through all the aliases. do this continuously, uninterrupted, this includes '
    'rigorous testing, committing, and pushing to origin Main."'
)

NEW_RULES = [
    {
        "id": "MCD-552",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Night All Five Forges Burned at Once\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-night-all-five-forges-burned-at-once.md), the Lord "
            "of Embers Alias Chronicle XVI, first entry in the fifth wave. A detailed, large-scale "
            "combat showcase: a coordinated Directorate assault hits five linked forge sites "
            "simultaneously, and Kanja moves between all five within a single hour using Mafesto's "
            "converted charge, Obsidian Malice, and Onyx of Oblivion, none of the sites falling. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-553",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Smith Who Built Their Weapons\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-smith-who-built-their-weapons.md), the Lord of "
            "Embers Alias Chronicle XVII. A captured Directorate smith who forged the siege engines "
            "that killed rebel fighters is offered work rather than punishment, testing "
            "'metabolizes punishment' against a skilled enemy craftsman rather than only civilians "
            "or economic pressure, over the crew's own genuine anger. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-554",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Old Smith Saw in the Ashes\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-old-smith-saw-in-the-ashes.md), the Lord of "
            "Embers Alias Chronicle XVIII, closing the fifth wave. The campaign's recurring senior "
            "smith (first referenced in MCD-502) finds Kanja alone at the forge the night after the "
            "five-site attack, witnessing the private toll behind the reputation for the first "
            "time. No new named characters. Closes the Lord of Embers' fifth three-Chronicle wave "
            "(with 'The Night All Five Forges Burned at Once,' MCD-552, and 'The Smith Who Built "
            "Their Weapons,' MCD-553)."
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
            "batch": 189,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Lord of Embers' fifth three-entry Alias Chronicle wave (MCD-552 through "
                "MCD-554). " + BATCH_NOTE
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
