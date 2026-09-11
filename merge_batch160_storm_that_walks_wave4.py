#!/usr/bin/env python3
"""Batch 160: Lock the Storm That Walks' fourth three-entry Alias Chronicle wave (MCD-503 through
MCD-505), continuing uninterrupted per Abad's authorization."""
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
        "id": "MCD-503",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Cost of Pushing Too Far\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-cost-of-pushing-too-far.md), the Storm That Walks "
            "Alias Chronicle X, first entry in the fourth wave. Chasing a decisive strike, Kanja "
            "pushes the fleet's timing margin too tight and loses an escort vessel and six crew to "
            "the storm's early edge -- the first genuine loss on his own side of this alias's run, "
            "prompting a permanently wider safety margin going forward. No new named characters "
            "beyond the already-locked Sephtis."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-504",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Storm That Coordinated Three Fleets\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-storm-that-coordinated-three-fleets.md), the Storm "
            "That Walks Alias Chronicle XI. A detailed large-scale combat showcase: three "
            "independent allied fleets converge on a single stronghold from separate directions "
            "using only Sephtis's storm prediction as a shared clock, no direct communication "
            "between commands, capturing the stronghold in under two hours with zero losses on "
            "Kanja's side, directly applying the wider margin from MCD-503. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-505",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Second Set of Eyes on the Sky\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-second-set-of-eyes-on-the-sky.md), the Storm That "
            "Walks Alias Chronicle XII, closing the fourth wave. Directly motivated by the loss in "
            "MCD-503, Sephtis (already locked) begins training a successor forecaster for the first "
            "time, building institutional redundancy into the storm-timing doctrine rather than "
            "leaving it dependent on one person's gift. No new named characters beyond the "
            "already-locked Sephtis. Closes the Storm That Walks' fourth three-Chronicle wave (with "
            "'The Cost of Pushing Too Far,' MCD-503, and 'The Storm That Coordinated Three Fleets,' "
            "MCD-504)."
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
            "batch": 160,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Storm That Walks' fourth three-entry Alias Chronicle wave (MCD-503 "
                "through MCD-505). " + BATCH_NOTE
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
