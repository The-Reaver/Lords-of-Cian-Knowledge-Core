#!/usr/bin/env python3
"""Batch 153: Lock the Industrial Myth's fourth three-entry Alias Chronicle wave (MCD-482 through
MCD-484), continuing uninterrupted per Abad's authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "work on a fourth Alias wave and a third territory entry continuously uninterrupted '
    'this includes testing, committing, pushing to origin Main."'
)

NEW_RULES = [
    {
        "id": "MCD-482",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Blade Meant for Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-blade-meant-for-him.md), the Industrial Myth Alias "
            "Chronicle X, first entry in the fourth wave. A paid assassin attacks Kanja directly "
            "during the Furnace District Strike; he disarms the man without any weapon of his own "
            "and lets him walk away unharmed, the most personal test yet of the alias's unarmed "
            "ethos. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-483",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Day Nothing Happened and Everything Did\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-day-nothing-happened-and-everything-did.md), the "
            "Industrial Myth Alias Chronicle XI. A district administrator musters his full guard "
            "force to intimidate the strike into collapse; Kanja continues the tally uninterrupted "
            "for six hours until the guards' own formation loses purpose, reframing 'combat "
            "intensity' entirely as sustained psychological craft with zero violence. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-484",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The District He Never Visited\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-district-he-never-visited.md), the Industrial Myth "
            "Alias Chronicle XII, closing the fourth wave. A mining district hundreds of miles away "
            "independently builds its own version of the tally method from an incomplete secondhand "
            "account, succeeding without any direct contact with Kanja, showing the method's real "
            "power is replicable rather than personal. Ezio Valcari (already locked) appears "
            "briefly. No new named characters. Closes the Industrial Myth's fourth three-Chronicle "
            "wave (with 'The Blade Meant for Him,' MCD-482, and 'The Day Nothing Happened and "
            "Everything Did,' MCD-483)."
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
            "batch": 153,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Industrial Myth's fourth three-entry Alias Chronicle wave (MCD-482 "
                "through MCD-484). " + BATCH_NOTE
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
