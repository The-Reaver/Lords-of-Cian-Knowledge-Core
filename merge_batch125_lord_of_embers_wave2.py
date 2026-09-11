#!/usr/bin/env python3
"""Batch 125: Lock the Lord of Embers' second three-entry Alias Chronicle wave (MCD-422 through
MCD-424), continuing uninterrupted through all remaining alias second waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = 'Abad: "complete all of the Alias drafts continuously uninterrupted."'

NEW_RULES = [
    {
        "id": "MCD-422",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Can't Be Burned\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-cant-be-burned.md), Lord of Embers Alias "
            "Chronicle IV, first entry in the second wave. A Trust administrator replaces "
            "punitive burning with a merchant-guild blacklist enforced through Scrip-Tether debt "
            "leverage, a punishment with nothing physical to rebuild against; Kanja personally "
            "tours the region's merchant routes offering subsidized smithing/repair services to "
            "any guild willing to defy the blacklist, breaking it within a month by making "
            "defiance cheaper than compliance -- the same underlying 'metabolizes punishment' "
            "principle (MCD-241) generalized beyond physical destruction. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-423",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Night They Came for the Anvil\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-night-they-came-for-the-anvil.md), Lord of Embers "
            "Alias Chronicle V. A raid targets The Anvil (MCD-241) itself for its accumulated "
            "Dead Drakma stock; Kanja meets the boarders on deck rather than let the fight reach "
            "sleeping apprentices belowdecks, demonstrating Mafesto's grounding function, Obsidian "
            "Malice collapsing the boarding ramp structurally to strand the second wave, and "
            "Onyx's Whisper of Shadows/Veil Piercer clearing the deck. The raid breaks in six "
            "minutes. No new named characters; the salvage master is unnamed and one-scene."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-424",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Smith Who Resented the Crown\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-smith-who-resented-the-crown.md), Lord of Embers "
            "Alias Chronicle VI, closing the second wave. A settlement's senior smith resents the "
            "Lord of Embers' visiting reputation overshadowing his own thirty years of earned "
            "local standing; Kanja concedes the point immediately and hands the teaching credit "
            "back to the smith rather than keep it, winning genuine respect through deference "
            "rather than fame. No new named characters; the settlement smith is unnamed and "
            "one-scene. Closes the Lord of Embers' second three-Chronicle wave (with 'What Can't "
            "Be Burned,' MCD-422, and 'The Night They Came for the Anvil,' MCD-423)."
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
            "batch": 125,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Lord of Embers' second three-entry Alias Chronicle wave (MCD-422 "
                "through MCD-424), the ninth of eleven second waves in a continuous run. "
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
