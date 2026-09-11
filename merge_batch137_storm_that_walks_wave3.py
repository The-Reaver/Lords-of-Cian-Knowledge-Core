#!/usr/bin/env python3
"""Batch 137: Lock the Storm That Walks' third three-entry Alias Chronicle wave (MCD-458 through
MCD-460), continuing uninterrupted per Abad's "#1 and #2 now" authorization."""
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
        "id": "MCD-458",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Battle Fought Inside the Storm\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-battle-fought-inside-the-storm.md), the Storm That "
            "Walks Alias Chronicle VII, first entry in the third wave. Rather than timing around a "
            "storm, Kanja takes the fleet directly into its leading edge, using Mafesto's charge-"
            "absorption, a wave-timed Obsidian Malice discharge, and Onyx of Oblivion's ship-to-ship "
            "boarding to defeat a Directorate fleet already scattered by the weather itself -- the "
            "storm's active conditions used as a direct combat weapon rather than a timing tool. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-459",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Merchant Fleet He Chose to Save\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-merchant-fleet-he-chose-to-save.md), the Storm That "
            "Walks Alias Chronicle VIII. With no Directorate target in a storm's predicted path, "
            "Kanja spends three days escorting a forty-vessel civilian merchant convoy onto a safer "
            "course, a pure humanitarian rescue with zero combat, establishing the doctrine's use "
            "beyond tactical timing. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-460",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Officer Who Learned to Trust the Sky\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-officer-who-learned-to-trust-the-sky.md), the Storm "
            "That Walks Alias Chronicle IX, closing the third wave. A newly transferred, initially "
            "skeptical naval officer comes to trust Sephtis's (already locked) storm-timing "
            "doctrine after watching it enable the merchant-fleet rescue of MCD-459, directly "
            "referencing the earlier miss of 'The Storm That Came Early' (MCD-425) as proof the "
            "confidence isn't recklessness. No new named characters beyond the already-locked "
            "Sephtis. Closes the Storm That Walks' third three-Chronicle wave (with 'The Battle "
            "Fought Inside the Storm,' MCD-458, and 'The Merchant Fleet He Chose to Save,' "
            "MCD-459)."
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
            "batch": 137,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Storm That Walks' third three-entry Alias Chronicle wave (MCD-458 "
                "through MCD-460). " + BATCH_NOTE
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
