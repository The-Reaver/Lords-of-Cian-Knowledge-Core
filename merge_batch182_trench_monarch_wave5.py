#!/usr/bin/env python3
"""Batch 182: Lock the Trench Monarch's fifth three-entry Alias Chronicle wave (MCD-531 through
MCD-533), continuing uninterrupted per Abad's authorization: "do a wave through all the aliases. do
this continuously, uninterrupted, this includes rigorous testing, committing, and pushing to origin
Main."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do a wave through all the aliases. do this continuously, uninterrupted, this includes '
    'rigorous testing, committing, and pushing to origin Main."'
)

NEW_RULES = [
    {
        "id": "MCD-531",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Table Across from the Owners\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-table-across-from-the-owners.md), Trench Monarch "
            "Alias Chronicle XIII, first entry in the fifth wave. Kanja negotiates directly with "
            "site ownership for the first time, in a formal room rather than through an "
            "intermediary or a crowd, settling a wage dispute purely on the strength of already-"
            "verified tally sheets. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-532",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Hunt for One Man\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-hunt-for-one-man.md), Trench Monarch Alias Chronicle "
            "XIV. A detailed, sustained single-night pursuit (Onyx of Oblivion only, consistent with "
            "the pre-Black-Trench timeline) through the district's dockside geography stops a "
            "professional killer contracted to silence a wage-dispute witness before he can testify, "
            "ending in a capture rather than a kill. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-533",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Maret Vos Carried From Before\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-maret-vos-carried-from-before.md), Trench Monarch "
            "Alias Chronicle XV, closing the fifth wave. Maret Vos (already locked, one of the three "
            "earliest crew members freed before the Black Trench) finally shares his own account of "
            "being freed -- quieter and less dramatized than Corren Halst's (MCD-436) or Danne "
            "Sok's (MCD-530), completing a trilogy of early-crew perspectives on the man before any "
            "alias existed. No new named characters beyond the already-locked Maret Vos. Closes the "
            "Trench Monarch's fifth three-Chronicle wave (with 'The Table Across from the Owners,' "
            "MCD-531, and 'The Hunt for One Man,' MCD-532)."
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
            "batch": 182,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Trench Monarch's fifth three-entry Alias Chronicle wave (MCD-531 "
                "through MCD-533). " + BATCH_NOTE
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
