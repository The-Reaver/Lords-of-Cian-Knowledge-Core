#!/usr/bin/env python3
"""Batch 180: Lock Kiti Chronicle III (MCD-527), completing a third territory-Chronicle entry
across every one of the 19 territories that had two (Xaragua already had four), per Abad's
authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "work on a fourth Alias wave and a third territory entry continuously uninterrupted '
    'this includes testing, committing, pushing to origin Main." Completes a third territory-'
    'Chronicle entry across all 19 territories that had two, giving every one of the 20 homage-era '
    'territories at least three Chronicles.'
)

NEW_RULES = [
    {
        "id": "MCD-527",
        "category": "phase2-territory-chronicle",
        "statement": (
            "Kiti Chronicle III, \"The Day He Decided to Leave It Behind\" (full narrative text at "
            "docs/lords-of-cian/chronicles/kiti-chronicle-iii-the-day-he-decided-to-leave-it-"
            "behind.md). Decades after the illness that first revealed 'The Long Tenure' (PH2-059)"
            "'s institutional nature, Owusu deliberately and voluntarily resigns his seat rather "
            "than hold it until circumstance forces the choice, closing his arc with a permanent, "
            "self-determined loss of the strength distinct from Chronicle II's temporary "
            "illness-forced lapse (MCD-475). An unnamed Kanja is present at his departure, "
            "uninvolved. No new named characters. Third Kiti territory Chronicle."
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
            "batch": 180,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks Kiti Chronicle III (MCD-527), completing a third territory-Chronicle entry "
                "across all 19 territories that had two. " + BATCH_NOTE
            ),
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
