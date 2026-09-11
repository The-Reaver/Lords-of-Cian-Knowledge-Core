#!/usr/bin/env python3
"""Batch 158: Lock the Iron Bastard's fourth three-entry Alias Chronicle wave (MCD-497 through
MCD-499), continuing uninterrupted per Abad's authorization."""
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
        "id": "MCD-497",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Frequency He Read Wrong\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-frequency-he-read-wrong.md), the Iron Bastard Alias "
            "Chronicle X, first entry in the fourth wave. A hidden old repair inside a support "
            "tower carries an unaccounted-for second tension; the resulting resonance discharge "
            "causes a wider, uncontained collapse that injures two Directorate engineers -- the "
            "first genuine misdiagnosis of the doctrine's run, prompting Kanja to trade speed for "
            "deeper diagnostic listening going forward. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-498",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Rigging Remembered\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-rigging-remembered.md), the Iron Bastard Alias "
            "Chronicle XI. A detailed naval application of the Aegis-Talisman resonance doctrine, "
            "its first use at sea: a Directorate blockade ship's precisely tensioned rigging is "
            "diagnosed and brought down in a controlled collapse, breaking the blockade without a "
            "shot fired or hull breached, directly applying the caution learned in MCD-497. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-499",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Student Who Chose Restraint\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-student-who-chose-restraint.md), the Iron Bastard "
            "Alias Chronicle XII, closing the fourth wave. A young engineer trained in diagnostic "
            "listening comes close to using the technique on a Trust granary out of personal "
            "resentment, then chooses restraint and honestly confesses the temptation to Kanja "
            "afterward -- the first entry testing the doctrine's ethical transmission to a student "
            "rather than only its technical mechanics. No new named characters. Closes the Iron "
            "Bastard's fourth three-Chronicle wave (with 'The Frequency He Read Wrong,' MCD-497, "
            "and 'What the Rigging Remembered,' MCD-498)."
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
            "batch": 158,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Iron Bastard's fourth three-entry Alias Chronicle wave (MCD-497 through "
                "MCD-499). " + BATCH_NOTE
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
