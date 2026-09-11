#!/usr/bin/env python3
"""Batch 130: Lock the Industrial Myth's third three-entry Alias Chronicle wave (MCD-437 through
MCD-439), continuing uninterrupted per Abad's "#1 and #2 now" authorization."""
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
        "id": "MCD-437",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Family Behind the Numbers\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-family-behind-the-numbers.md), the Industrial Myth "
            "Alias Chronicle VII, first entry in the third wave. Kanja sets the tally sheets aside "
            "for an afternoon during the Furnace District Strike to sit with a three-generation "
            "hauler family the aggregate numbers can only gesture toward, offering the grandmother "
            "honesty rather than a guarantee. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-438",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Man Who Wanted to Fight\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-man-who-wanted-to-fight.md), the Industrial Myth "
            "Alias Chronicle VIII. A rival hauler-organizer with three failed strikes behind him "
            "arrives intending to burn the district administrator's offices rather than wait out "
            "the four-day tally; Kanja persuades him to hold his following back, arguing patience "
            "produces an undeniable precedent that force alone cannot, testing the alias's unarmed "
            "ethos against internal movement pressure rather than an external threat. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-439",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Ezio Valcari Understood By Then\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-ezio-valcari-understood-by-then.md), the Industrial "
            "Myth Alias Chronicle IX, closing the third wave. Ezio Valcari (already locked) reflects "
            "on four days of tally work, explicitly articulating why the numbers-first method "
            "outlasts fear-based leverage, directly cross-referencing the events of 'The Man Who "
            "Wanted to Fight' (MCD-438). No new named characters beyond the already-locked Ezio "
            "Valcari. Closes the Industrial Myth's third three-Chronicle wave (with 'The Family "
            "Behind the Numbers,' MCD-437, and 'The Man Who Wanted to Fight,' MCD-438)."
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
            "batch": 130,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Industrial Myth's third three-entry Alias Chronicle wave (MCD-437 "
                "through MCD-439). " + BATCH_NOTE
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
