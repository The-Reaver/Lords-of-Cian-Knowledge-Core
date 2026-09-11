#!/usr/bin/env python3
"""Batch 169: Lock Jibaro Chronicle III (MCD-516), continuing the territory-Chronicle third-entry
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
        "id": "MCD-516",
        "category": "phase2-territory-chronicle",
        "statement": (
            "Jibaro Chronicle III, \"The Week Five Doors Refused\" (full narrative text at "
            "docs/lords-of-cian/chronicles/jibaro-chronicle-iii-the-week-five-doors-refused.md). "
            "Five genuinely abandoned buildings across Jibaro are simultaneously occupied past the "
            "one-day threshold, all becoming permanently unreclaimable under 'The Occupation' "
            "(PH2-042), proving the ability scales to multiple sites at once as long as each "
            "independently meets the 'nothing to be ashamed of' standard established in Chronicle "
            "II (MCD-468). An unnamed Kanja helps carry belongings during the transition, "
            "uninvolved otherwise. No new named characters. Third Jibaro territory Chronicle."
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
            "batch": 169,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Jibaro Chronicle III (MCD-516). " + BATCH_NOTE,
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
