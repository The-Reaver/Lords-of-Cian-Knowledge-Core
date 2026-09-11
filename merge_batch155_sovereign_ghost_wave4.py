#!/usr/bin/env python3
"""Batch 155: Lock the Sovereign Ghost of the Great Sea's fourth three-entry Alias Chronicle wave
(MCD-488 through MCD-490), continuing uninterrupted per Abad's authorization."""
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
        "id": "MCD-488",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ship He Couldn't Reach in Time\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ship-he-couldnt-reach-in-time.md), the Sovereign "
            "Ghost of the Great Sea Alias Chronicle X, first entry in the fourth wave. A distress "
            "signal reaches the fleet too late; despite pushing the flagship past ordinary limits, "
            "the merchant vessel sinks eleven minutes before arrival and six of eighteen crew die, "
            "the first genuine loss-at-sea entry establishing real limits of distance and weather "
            "against the fleet's speed. Dol Maren (already locked) present throughout. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-489",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Manifest Written in Chains\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-manifest-written-in-chains.md), the Sovereign Ghost "
            "of the Great Sea Alias Chronicle XI. A detailed night-boarding Trinity combat showcase "
            "liberates nearly two hundred captives from a dark-running slaver vessel with a forged "
            "manifest, Mafesto's vibration-reading, a precision Obsidian Malice strike disabling the "
            "deck gun, and Onyx of Oblivion clearing the crew before the alarm spreads. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-490",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Flag From a Foreign Sea\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-flag-from-a-foreign-sea.md), the Sovereign Ghost of "
            "the Great Sea Alias Chronicle XII, closing the fourth wave. An envoy from a nation "
            "entirely outside Sovereign Trust waters formally acknowledges the fleet's reputation "
            "for restraint, offering safe harbor in good faith -- the first foreign contact the "
            "fleet has received, its letter joining Garren Hask's already-established ghost-fleet "
            "ledger (MCD-445). No new named characters. Closes the Sovereign Ghost's fourth "
            "three-Chronicle wave (with 'The Ship He Couldn't Reach in Time,' MCD-488, and 'The "
            "Manifest Written in Chains,' MCD-489)."
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
            "batch": 155,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Sovereign Ghost of the Great Sea's fourth three-entry Alias Chronicle "
                "wave (MCD-488 through MCD-490). " + BATCH_NOTE
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
