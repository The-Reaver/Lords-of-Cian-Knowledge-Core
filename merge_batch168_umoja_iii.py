#!/usr/bin/env python3
"""Batch 168: Lock Umoja Chronicle III (MCD-515), continuing the territory-Chronicle third-entry
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
        "id": "MCD-515",
        "category": "phase2-territory-chronicle",
        "statement": (
            "Umoja Chronicle III, \"The Fire That Crossed the City\" (full narrative text at "
            "docs/lords-of-cian/chronicles/umoja-chronicle-iii-the-fire-that-crossed-the-city.md). "
            "Twelve workplaces across the district, each genuinely organized by Kofi over years, "
            "walk out together within the same hour under 'One Fire' (PH2-040), defeating a citywide "
            "wage cut -- the ability's first district-wide success, directly consistent with the "
            "limit shown in Chronicle II (MCD-465): it amplifies genuine existing relationships "
            "rather than manufacturing them. An unnamed Kanja is present at the rally, uninvolved. "
            "No new named characters. Third Umoja territory Chronicle."
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
            "batch": 168,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Umoja Chronicle III (MCD-515). " + BATCH_NOTE,
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
