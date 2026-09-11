#!/usr/bin/env python3
"""Batch 167: Lock Kwan Chronicle III (MCD-514), continuing the territory-Chronicle third-entry run
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
        "id": "MCD-514",
        "category": "phase2-territory-chronicle",
        "statement": (
            "Kwan Chronicle III, \"The Landlord Who Changed His Own Mind\" (full narrative text at "
            "docs/lords-of-cian/chronicles/kwan-chronicle-iii-the-landlord-who-changed-his-own-"
            "mind.md). A property owner genuinely opposed to open housing is invited to explain his "
            "opposition honestly at a public forum, and talks himself out of his own position while "
            "preparing to argue it -- 'The Invitation' (PH2-038) shown producing unplanned "
            "self-persuasion in an actual opponent rather than only activating latent sympathy. An "
            "unnamed Kanja is present, uninvolved. No new named characters. Third Kwan territory "
            "Chronicle."
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
            "batch": 167,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Kwan Chronicle III (MCD-514). " + BATCH_NOTE,
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
