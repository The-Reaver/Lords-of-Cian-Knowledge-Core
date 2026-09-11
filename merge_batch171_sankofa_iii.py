#!/usr/bin/env python3
"""Batch 171: Lock Sankofa Chronicle III (MCD-518), continuing the territory-Chronicle third-entry
run per Abad's authorization. Deliberately leaves the reserved forged-letter conspiracy thread
untouched, per standing instruction."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "work on a fourth Alias wave and a third territory entry continuously uninterrupted '
    'this includes testing, committing, pushing to origin Main." Deliberately does not advance or '
    'resolve the reserved Sankofa forged-letter conspiracy thread (PH2-021), per standing '
    'instruction.'
)

NEW_RULES = [
    {
        "id": "MCD-518",
        "category": "phase2-territory-chronicle",
        "statement": (
            "Sankofa Chronicle III, \"What He Built While Waiting\" (full narrative text at "
            "docs/lords-of-cian/chronicles/sankofa-chronicle-iii-what-he-built-while-waiting.md). "
            "With the forged-letter conspiracy from Chronicle II (MCD-360) still unresolved and "
            "deliberately left untouched here, Baálé refuses to let the uncertainty stop him from "
            "opening a new community health clinic, with Kra and Kojo (both already locked) "
            "present. An unnamed Kanja attends the opening, uninvolved. No new named characters. "
            "Third Sankofa territory Chronicle."
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
            "batch": 171,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Sankofa Chronicle III (MCD-518). " + BATCH_NOTE,
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
