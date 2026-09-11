#!/usr/bin/env python3
"""Batch 178: Lock Hekalu Chronicle III (MCD-525), continuing the territory-Chronicle third-entry
run per Abad's authorization."""
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
        "id": "MCD-525",
        "category": "phase2-territory-chronicle",
        "statement": (
            "Hekalu Chronicle III, \"The Table That Needed Setting Again\" (full narrative text at "
            "docs/lords-of-cian/chronicles/hekalu-chronicle-iii-the-table-that-needed-setting-"
            "again.md). The rival owner bonded in Chronicle I has quietly drifted from the "
            "mutual-obligation network over a year of neglect; Adom seeks him out and renews the "
            "bond, establishing for the first time that 'The Common Table' (PH2-055) requires "
            "periodic renewal rather than binding permanently on a single choice. An unnamed Kanja "
            "is present, uninvolved. No new named characters. Third Hekalu territory Chronicle."
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
            "batch": 178,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Hekalu Chronicle III (MCD-525). " + BATCH_NOTE,
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
