#!/usr/bin/env python3
"""Batch 139: Lock Yara Chronicle II (MCD-464), the first of a run of territory-Chronicle second
entries covering the twelve territories that still only had one, per Abad's "#1 and #2 now"
authorization (item #2: more territory Chronicles)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "#1 and #2 now and continue uninterrupted until completion this includes test, commit, '
    'push to main origin" -- item #2, more territory Chronicles, giving a second entry to '
    'territories that still only had one.'
)

NEW_RULES = [
    {
        "id": "MCD-464",
        "category": "phase2-territory-chronicle",
        "statement": (
            "\"The Price She Wouldn't Let Them Pay\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-price-she-wouldnt-let-them-pay.md), Yara Chronicle "
            "II. A developer offers full clinic funding in exchange for Yalokona's public silence "
            "on a displacing zoning variance; she refuses, the variance passes anyway and the "
            "clinic's funding is delayed eighteen months, dramatizing the real cost of 'Unbought "
            "and Unbossed' (PH2-006) as a genuine defeat rather than a clean win. An unnamed Kanja "
            "is present in the gallery, uninvolved. No new named characters. Second Yara territory "
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
            "batch": 139,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks Yara Chronicle II (MCD-464). " + BATCH_NOTE
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
