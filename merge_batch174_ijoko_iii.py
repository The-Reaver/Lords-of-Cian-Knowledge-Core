#!/usr/bin/env python3
"""Batch 174: Lock Ijoko Chronicle III (MCD-521), continuing the territory-Chronicle third-entry
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
        "id": "MCD-521",
        "category": "phase2-territory-chronicle",
        "statement": (
            "Ijoko Chronicle III, \"The Criticism She Couldn't Dismiss\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ijoko-chronicle-iii-the-criticism-she-couldnt-dismiss."
            "md). A genuine ally's well-reasoned critique that the cooperative lending system "
            "favors established businesses nearly gets treated with the same iron resilience Adwoa "
            "uses against deniable mockery; she catches the mistake, restructures the lending "
            "priority, and develops discernment between hostility and honest criticism for the "
            "first time. An unnamed Kanja is present, uninvolved. No new named characters. Third "
            "Ijoko territory Chronicle."
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
            "batch": 174,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Ijoko Chronicle III (MCD-521). " + BATCH_NOTE,
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
