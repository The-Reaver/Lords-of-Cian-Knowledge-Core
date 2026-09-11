#!/usr/bin/env python3
"""Batch 149: Lock Nyansa Chronicle II (MCD-474), continuing the territory-Chronicle second-entry
run per Abad's "#1 and #2 now" authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "#1 and #2 now and continue uninterrupted until completion this includes test, commit, '
    'push to main origin" -- item #2, more territory Chronicles.'
)

NEW_RULES = [
    {
        "id": "MCD-474",
        "category": "phase2-territory-chronicle",
        "statement": (
            "\"The Cost of Being Corrected\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-cost-of-being-corrected.md), Nyansa Chronicle II. "
            "The committee member successfully corrected in Chronicle I ('The Word That Stuck,' "
            "MCD-354) faces quiet social ostracism from his own faction for having genuinely "
            "changed his position; Adisa acknowledges the real cost 'The Long Correction' "
            "(PH2-057) never promised to soften. An unnamed Kanja walks with the man on several "
            "evenings, uninvolved. No new named characters. Second Nyansa territory Chronicle."
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
            "batch": 149,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Nyansa Chronicle II (MCD-474). " + BATCH_NOTE,
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
