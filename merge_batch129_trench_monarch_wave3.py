#!/usr/bin/env python3
"""Batch 129: Lock the Trench Monarch's third three-entry Alias Chronicle wave (MCD-434 through
MCD-436), continuing uninterrupted per Abad's "#1 and #2 now" authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "#1 and #2 now and continue uninterrupted until completion this includes test, commit, '
    'push to main origin."'
)

NEW_RULES = [
    {
        "id": "MCD-434",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Crown He Dug With His Own Hands\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-crown-he-dug-with-his-own-hands.md), Trench Monarch "
            "Alias Chronicle VII, first entry in the third wave. Kanja works the Warehouse Twelve "
            "dredge line by hand for three weeks straight, telling a skeptical foreman that a crown "
            "handed to him could be taken back but one he digs for himself, alongside the people "
            "who'll live under his decisions, cannot -- dramatizing the origin context behind the "
            "already-locked 'digging his own crown' quote (VB-061) for the first time on the page. "
            "No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-435",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Overseer Who Doubted the Boy\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-overseer-who-doubted-the-boy.md), Trench Monarch "
            "Alias Chronicle VIII. A skeptical Warehouse Twelve site overseer independently verifies "
            "the tally-worker trust reputation over six weeks of cross-checked figures rather than "
            "accepting any story on faith, concluding the numbers -- not the legend -- are what "
            "actually earned her respect. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-436",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Corren Halst Remembered\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-corren-halst-remembered.md), Trench Monarch Alias "
            "Chronicle IX, closing the third wave. Corren Halst (already locked, one of the three "
            "earliest crew members present at the Black Trench per Batch 41's correction), decades "
            "later, tells a younger worker that the Trench Monarch reputation had no single origin "
            "moment -- it accumulated from a hundred undramatic days nobody wrote down. No new named "
            "characters beyond the already-locked Corren Halst. Closes the Trench Monarch's third "
            "three-Chronicle wave (with 'The Crown He Dug With His Own Hands,' MCD-434, and 'The "
            "Overseer Who Doubted the Boy,' MCD-435)."
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
            "batch": 129,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Trench Monarch's third three-entry Alias Chronicle wave (MCD-434 "
                "through MCD-436). " + BATCH_NOTE
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
