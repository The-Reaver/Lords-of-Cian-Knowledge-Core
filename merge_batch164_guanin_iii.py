#!/usr/bin/env python3
"""Batch 164: Lock Guanín Chronicle III (MCD-511), continuing the territory-Chronicle third-entry
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
        "id": "MCD-511",
        "category": "phase2-territory-chronicle",
        "statement": (
            "Guanín Chronicle III, \"The Blow He Decided Not to Bank\" (full narrative text at "
            "docs/lords-of-cian/chronicles/guanin-chronicle-iii-the-blow-he-decided-not-to-bank.md)"
            ". A junior clerk's petty public insult goes entirely unanswered; Eri Kotoko explains "
            "that 'The Unanswered Blow' (PH2-008) is a deliberate choice about which wrongs deserve "
            "its weight, not a reflex triggered by any slight -- the first entry showing restraint "
            "rather than release. An unnamed Kanja is present in the hearing hall, uninvolved. No "
            "new named characters. Third Guanín territory Chronicle."
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
            "batch": 164,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Guanín Chronicle III (MCD-511). " + BATCH_NOTE,
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
