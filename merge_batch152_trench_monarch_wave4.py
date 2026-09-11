#!/usr/bin/env python3
"""Batch 152: Lock the Trench Monarch's fourth three-entry Alias Chronicle wave (MCD-479 through
MCD-481), continuing uninterrupted per Abad's authorization."""
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
        "id": "MCD-479",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Line Cost His Own Hands\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-line-cost-his-own-hands.md), Trench Monarch "
            "Alias Chronicle X, first entry in the fourth wave. A crushing hand injury from an "
            "ordinary dredge-cart accident tests the 'digging his own crown' ethos against physical "
            "vulnerability; Kanja returns to work too early out of stubborn principle before a "
            "fellow worker's plain honesty corrects him into genuinely resting. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-480",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Line That Wouldn't Break\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-line-that-wouldnt-break.md), Trench Monarch Alias "
            "Chronicle XI. Hired enforcers raid the dredge line at shift change; a detailed "
            "close-quarters solo-blade defense (Onyx of Oblivion only, Mafesto/Obsidian Malice "
            "still dormant/undeployed pre-Black-Trench) protects unarmed workers rather than "
            "demonstrating powers cleanly, costing Kanja a shallow wound taken shielding a frozen "
            "worker. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-481",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Organizer Who Competed for the Same Crowd\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-organizer-who-competed-for-the-same-crowd.md), "
            "Trench Monarch Alias Chronicle XII, closing the fourth wave. A rival organizer's "
            "harder, more confrontational method is forced into cooperation with Kanja's patient "
            "tally approach during a joint labor dispute; the two methods prove complementary "
            "rather than either superior, resolving the dispute faster together than either alone "
            "would have. No new named characters. Closes the Trench Monarch's fourth "
            "three-Chronicle wave (with 'What the Line Cost His Own Hands,' MCD-479, and 'The Line "
            "That Wouldn't Break,' MCD-480)."
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
            "batch": 152,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Trench Monarch's fourth three-entry Alias Chronicle wave (MCD-479 "
                "through MCD-481). " + BATCH_NOTE
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
