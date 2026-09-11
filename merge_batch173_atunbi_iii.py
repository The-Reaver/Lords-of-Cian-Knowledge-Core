#!/usr/bin/env python3
"""Batch 173: Lock Atunbi Chronicle III (MCD-520), continuing the territory-Chronicle third-entry
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
        "id": "MCD-520",
        "category": "phase2-territory-chronicle",
        "statement": (
            "Atunbi Chronicle III, \"The Ones Who Wanted It Faster\" (full narrative text at "
            "docs/lords-of-cian/chronicles/atunbi-chronicle-iii-the-ones-who-wanted-it-faster.md). "
            "A younger cohort presses Oluwole for faster, more visible action; rather than dismiss "
            "or capitulate, he negotiates a genuine, ongoing accommodation between urgency and "
            "patience, extending both the fast-failure (MCD-348) and slow-success (MCD-469) "
            "precedents into an internal generational tension rather than an external threat. An "
            "unnamed Kanja listens throughout, uninvolved. No new named characters. Third Atunbi "
            "territory Chronicle."
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
            "batch": 173,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Atunbi Chronicle III (MCD-520). " + BATCH_NOTE,
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
