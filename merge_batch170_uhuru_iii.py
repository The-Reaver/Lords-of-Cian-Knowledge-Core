#!/usr/bin/env python3
"""Batch 170: Lock Uhuru Chronicle III (MCD-517), continuing the territory-Chronicle third-entry
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
        "id": "MCD-517",
        "category": "phase2-territory-chronicle",
        "statement": (
            "Uhuru Chronicle III, \"What the Seat Couldn't Give the Next Man\" (full narrative text "
            "at docs/lords-of-cian/chronicles/uhuru-chronicle-iii-what-the-seat-couldnt-give-the-"
            "next-man.md). Set after Ofin's already-locked capstone death (MCD-358): his successor, "
            "elected on the same coalition, discovers 'The Override' (PH2-044) did not pass to him "
            "-- confirming directly on the page that the ability was institutional to Ofin's own "
            "endurance, not the seat itself, and the successor must build ordinary political "
            "endurance from nothing. An unnamed Kanja observes from the gallery, uninvolved. No new "
            "named characters. Third Uhuru territory Chronicle."
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
            "batch": 170,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Uhuru Chronicle III (MCD-517). " + BATCH_NOTE,
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
