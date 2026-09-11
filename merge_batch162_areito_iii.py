#!/usr/bin/env python3
"""Batch 162: Lock Areíto Chronicle III (MCD-509), starting a run of territory-Chronicle third
entries across the 19 territories that had two, per Abad's authorization (item #2: a third
territory entry, continuously)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "work on a fourth Alias wave and a third territory entry continuously uninterrupted '
    'this includes testing, committing, pushing to origin Main." Item #2: a third territory-'
    'Chronicle entry, continuing across all territories that had only two.'
)

NEW_RULES = [
    {
        "id": "MCD-509",
        "category": "phase2-territory-chronicle",
        "statement": (
            "Areíto Chronicle III, \"The Two Houses He Brought to One Table\" (full narrative text "
            "at docs/lords-of-cian/chronicles/areito-chronicle-iii-the-two-houses-he-brought-to-"
            "one-table.md). Kwame Ade mediates a decade-old split between two tenant associations, "
            "discovering the grievance had outlived its own cause -- a patient, non-combat "
            "community-reconciliation entry distinct from his physical-vulnerability and Adeyemi "
            "Chronicles. An unnamed Kanja is present, uninvolved. No new named characters. Third "
            "Areíto territory Chronicle."
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
            "batch": 162,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Areíto Chronicle III (MCD-509). " + BATCH_NOTE,
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
