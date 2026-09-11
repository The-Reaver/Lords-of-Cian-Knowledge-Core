#!/usr/bin/env python3
"""Batch 126: Lock the Storm That Walks' second three-entry Alias Chronicle wave (MCD-425
through MCD-427), continuing uninterrupted through all remaining alias second waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = 'Abad: "complete all of the Alias drafts continuously uninterrupted."'

NEW_RULES = [
    {
        "id": "MCD-425",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Storm That Came Early\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-storm-that-came-early.md), Storm That Walks Alias "
            "Chronicle IV, first entry in the second wave. Sephtis's storm prediction misses by "
            "two hours, the first genuine failure of the doctrine's supporting infrastructure; "
            "Kanja compresses the arrowhead formation's approach to close the engagement faster "
            "rather than abort, at the cost of damage to two smaller vessels, and the fleet clears "
            "just ahead of the storm's actual, revised arrival. Sephtis's own account of the "
            "miscalculation becomes required study, proof the doctrine survives honest error. No "
            "new named characters beyond the already-locked Sephtis, referenced not appearing "
            "on-page."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-426",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Dark Water Ambush\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-dark-water-ambush.md), Storm That Walks Alias "
            "Chronicle V. A moonless-night raid from three directions at once is met with Mafesto's "
            "non-visual Kinetic Transfer System, Obsidian Malice's pressure-guided blind discharge, "
            "and Onyx's Whisper of Shadows, all operating without reliance on sight -- extending "
            "the same non-visual-combat principle established in Bane's 'What the Fog Remembers' "
            "(MCD-398) into full darkness at sea. Two of three raiding vessels are disabled; no "
            "survivor gets a clean account of what stopped them. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-427",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Weight Sephtis Carried Alone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-weight-sephtis-carried-alone.md), Storm That Walks "
            "Alias Chronicle VI, closing the second wave. From Sephtis's own perspective (already "
            "locked): the private hours of self-doubt behind every calm, confident storm "
            "prediction, and his reflection on the miscalculation dramatized in 'The Storm That "
            "Came Early' (MCD-425) -- the real job being willing to be wrong in front of people "
            "whose lives depend on him, not the mathematics itself. No new named characters "
            "beyond the already-locked Sephtis. Closes the Storm That Walks' second three-"
            "Chronicle wave (with 'The Storm That Came Early,' MCD-425, and 'The Dark Water "
            "Ambush,' MCD-426)."
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
            "batch": 126,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Storm That Walks' second three-entry Alias Chronicle wave (MCD-425 "
                "through MCD-427), the tenth of eleven second waves in a continuous run. "
                + BATCH_NOTE
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
