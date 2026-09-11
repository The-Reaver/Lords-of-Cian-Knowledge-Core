#!/usr/bin/env python3
"""Batch 187: Lock the Crow King's fifth three-entry Alias Chronicle wave (MCD-546 through
MCD-548), continuing uninterrupted per Abad's authorization."""
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
        "id": "MCD-546",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Division That Marched Itself Away\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-division-that-marched-itself-away.md), the Crow King "
            "Alias Chronicle XIII, first entry in the fifth wave. A detailed four-day deception "
            "redirects an entire three-thousand-man Directorate division by targeting its officers' "
            "own reporting channels rather than the rank and file, the largest single deception "
            "target of the alias's run. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-547",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Spy Who Read the Signals Back\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-spy-who-read-the-signals-back.md), the Crow King "
            "Alias Chronicle XIV. A Directorate intelligence officer trained in the same deception "
            "craft seeds counter-signals to poison trust in the reporting network itself rather "
            "than catch any single lie; Kanja defeats him by reusing the in-person, unforgeable-"
            "trust method from 'The Tactician Who Built a Trap From Doubt' (MCD-450), the first "
            "opponent to genuinely understand the Hymn-Engine's own mechanism. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-548",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Voice Two Generations Removed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-voice-two-generations-removed.md), the Crow King "
            "Alias Chronicle XV, closing the fifth wave. The already-locked apprentice (MCD-451, "
            "MCD-496) takes on her own student without asking permission first; Kanja endorses the "
            "third-generation transmission, the craft evolving past his own original teaching while "
            "the underlying discipline of listening before cleverness stays constant. No new named "
            "characters beyond the already-locked apprentice. Closes the Crow King's fifth "
            "three-Chronicle wave (with 'The Division That Marched Itself Away,' MCD-546, and 'The "
            "Spy Who Read the Signals Back,' MCD-547)."
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
            "batch": 187,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Crow King's fifth three-entry Alias Chronicle wave (MCD-546 through "
                "MCD-548). " + BATCH_NOTE
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
