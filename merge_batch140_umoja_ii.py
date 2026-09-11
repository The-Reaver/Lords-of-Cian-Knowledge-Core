#!/usr/bin/env python3
"""Batch 140: Lock Umoja Chronicle II (MCD-465), continuing the territory-Chronicle second-entry
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
        "id": "MCD-465",
        "category": "phase2-territory-chronicle",
        "statement": (
            "\"The Fire That Spread Too Thin\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fire-that-spread-too-thin.md), Umoja Chronicle II. "
            "Kofi tries to extend 'One Fire' (PH2-040) to weld together a rival tenant organization "
            "outside his own established network; the unity thins and fractures within weeks, "
            "establishing that the ability accelerates trust-building rather than substituting for "
            "years of underlying relational work. An unnamed Kanja passes through during the slower "
            "rebuilding, uninvolved. No new named characters. Second Umoja territory Chronicle."
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
            "batch": 140,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Umoja Chronicle II (MCD-465). " + BATCH_NOTE,
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
