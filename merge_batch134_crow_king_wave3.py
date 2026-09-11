#!/usr/bin/env python3
"""Batch 134: Lock the Crow King's third three-entry Alias Chronicle wave (MCD-449 through
MCD-451), continuing uninterrupted per Abad's "#1 and #2 now" authorization."""
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
        "id": "MCD-449",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Extraction That Never Fired a Shot\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-extraction-that-never-fired-a-shot.md), the Crow "
            "King Alias Chronicle VII, first entry in the third wave. A prisoner convoy moves "
            "through open terrain deliberately chosen to deny the Hymn-Engine's usual marsh/"
            "tree-line tricks; Kanja instead seeds false signals into the Directorate's own "
            "reporting network days in advance, extracting the prisoners via a forged relief-patrol "
            "schedule with zero combat. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-450",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Tactician Who Built a Trap From Doubt\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-tactician-who-built-a-trap-from-doubt.md), the Crow "
            "King Alias Chronicle VIII. A Directorate tactician forges orders to sow distrust "
            "within Kanja's own crew rather than attacking the Hymn-Engine directly; Kanja defeats "
            "the scheme by deliberately declining to use the Hymn-Engine at all, delivering real "
            "orders in person, unforgeable at a distance. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-451",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Apprentice Who Learned to Listen\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-apprentice-who-learned-to-listen.md), the Crow King "
            "Alias Chronicle IX, closing the third wave. The already-locked singer from 'The Voice "
            "That Carried Three Hundred' (MCD-418) becomes Kanja's apprentice, learning that the "
            "Hymn-Engine's real discipline is restraint and listening rather than cleverness, and "
            "leads her own first solo operation using a single true statement instead of any "
            "deception. No new named characters. Closes the Crow King's third three-Chronicle wave "
            "(with 'The Extraction That Never Fired a Shot,' MCD-449, and 'The Tactician Who Built "
            "a Trap From Doubt,' MCD-450)."
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
            "batch": 134,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Crow King's third three-entry Alias Chronicle wave (MCD-449 through "
                "MCD-451). " + BATCH_NOTE
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
