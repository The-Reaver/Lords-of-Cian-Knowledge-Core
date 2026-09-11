#!/usr/bin/env python3
"""Batch 124: Lock the Iron Bastard's second three-entry Alias Chronicle wave (MCD-419 through
MCD-421), continuing uninterrupted through all remaining alias second waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = 'Abad: "complete all of the Alias drafts continuously uninterrupted."'

NEW_RULES = [
    {
        "id": "MCD-419",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Column He Could Not Leave Alone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-column-he-could-not-leave-alone.md), Iron Bastard "
            "Alias Chronicle IV, first entry in the second wave. The first Iron Bastard "
            "engagement requiring protection of others -- forty wounded fighters mid-transport -- "
            "rather than a solo open-ground stand; Kanja adapts the Aegis-Talisman resonance "
            "doctrine into a moving broadcast matching the evacuation's own pace instead of a "
            "fixed stand, taking the alias's first on-page wound in the process. No new named "
            "characters; the field medic is unnamed and one-scene."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-420",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Column Built Without Metal\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-column-built-without-metal.md), Iron Bastard "
            "Alias Chronicle V. A Trust engineering corps builds a column from wood, ceramic "
            "composite, and rope lashings specifically to deny the resonance harmonic a metallic "
            "target; Kanja adapts by finding the same tension-response signature in the natural-"
            "fiber lashings holding the structure together, generalizing the Aegis-Talisman "
            "principle to any tension-bearing structure regardless of material, combined with "
            "Mafesto, Obsidian Malice, and Onyx's Cadence Ruin. No new named characters; the field "
            "observer is unnamed and one-scene."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-421",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Scholar Who Measured the Impossible\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-scholar-who-measured-the-impossible.md), Iron "
            "Bastard Alias Chronicle VI, closing the second wave. A Trust materials scholar's "
            "eleven-month honest study concludes the resonance phenomenon is applied physics, not "
            "a supernatural weapon, and that the only real defense (extreme structural redundancy) "
            "is prohibitively expensive; her accurate report is quietly shelved in favor of a "
            "politically comfortable explanation. No new named characters. Closes the Iron "
            "Bastard's second three-Chronicle wave (with 'The Column He Could Not Leave Alone,' "
            "MCD-419, and 'The Column Built Without Metal,' MCD-420)."
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
            "batch": 124,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Iron Bastard's second three-entry Alias Chronicle wave (MCD-419 "
                "through MCD-421), the eighth of eleven second waves in a continuous run. "
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
