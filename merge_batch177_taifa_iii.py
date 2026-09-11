#!/usr/bin/env python3
"""Batch 177: Lock Taifa Chronicle III (MCD-524), continuing the territory-Chronicle third-entry
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
        "id": "MCD-524",
        "category": "phase2-territory-chronicle",
        "statement": (
            "Taifa Chronicle III, \"What Traveled Besides the Alarm\" (full narrative text at "
            "docs/lords-of-cian/chronicles/taifa-chronicle-iii-what-traveled-besides-the-alarm.md)"
            ". On the night his daughter is born, Osei unintentionally sends genuine joy rather "
            "than warning through 'Kin at a Distance' (PH2-053), felt by sworn members in three "
            "separate cities -- revealing for the first time that the bond carries positive emotion "
            "as well as danger. An unnamed Kanja passes through that week, uninvolved. No new named "
            "characters. Third Taifa territory Chronicle."
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
            "batch": 177,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Taifa Chronicle III (MCD-524). " + BATCH_NOTE,
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
