#!/usr/bin/env python3
"""Batch 145: Lock Ijoko Chronicle II (MCD-470), continuing the territory-Chronicle second-entry
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
        "id": "MCD-470",
        "category": "phase2-territory-chronicle",
        "statement": (
            "\"The Ledger She Built From Nothing\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ledger-she-built-from-nothing.md), Ijoko Chronicle "
            "II. Adwoa spends three years building a local currency/cooperative-lending system to "
            "slow the tax-base flight explicitly left untouched by 'The Iron Hand in the Velvet "
            "Glove' (PH2-027) in Chronicle I, an ordinary-competence achievement distinct from the "
            "ability itself. An unnamed Kanja sits through several early planning sessions, "
            "uninvolved. No new named characters. Second Ijoko territory Chronicle."
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
            "batch": 145,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Ijoko Chronicle II (MCD-470). " + BATCH_NOTE,
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
