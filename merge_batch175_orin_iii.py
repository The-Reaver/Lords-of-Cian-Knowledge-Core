#!/usr/bin/env python3
"""Batch 175: Lock Orin Chronicle III (MCD-522), continuing the territory-Chronicle third-entry run
per Abad's authorization."""
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
        "id": "MCD-522",
        "category": "phase2-territory-chronicle",
        "statement": (
            "Orin Chronicle III, \"What the Ark Wouldn't Lend Itself To\" (full narrative text at "
            "docs/lords-of-cian/chronicles/orin-chronicle-iii-what-the-ark-wouldnt-lend-itself-to."
            "md). A political operator arranges a free, non-commercial gathering to exploit 'The "
            "Ark' (PH2-029)'s communal binding toward a predetermined vote; the binding fails to "
            "take, extending the ability's known commercial-exclusion limit into a second failure "
            "mode -- manipulative intent also prevents it, suggesting the mechanism requires genuine "
            "communal choice rather than merely an absence of money. An unnamed Kanja is present, "
            "uninvolved. No new named characters. Third Orin territory Chronicle."
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
            "batch": 175,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Orin Chronicle III (MCD-522). " + BATCH_NOTE,
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
