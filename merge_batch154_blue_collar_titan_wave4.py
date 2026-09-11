#!/usr/bin/env python3
"""Batch 154: Lock the Blue-Collar Titan's fourth three-entry Alias Chronicle wave (MCD-485 through
MCD-487), continuing uninterrupted per Abad's authorization."""
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
        "id": "MCD-485",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Even He Couldn't Save\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-even-he-couldnt-save.md), the Blue-Collar Titan "
            "Alias Chronicle X, first entry in the fourth wave. Decades of unaddressed structural "
            "decay in the eastern gallery prove beyond even Kanja's skill to save; every worker "
            "clears safely but the gallery itself collapses permanently, the first genuine "
            "structural-failure entry of this alias's run. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-486",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ticking Room\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ticking-room.md), the Blue-Collar Titan Alias "
            "Chronicle XI. Directorate holdouts trap fourteen workers in a chamber on a flooding "
            "timer; a detailed, explicitly time-pressured Trinity rescue -- Mafesto's rock-penetrating "
            "sensing, a forced door breach, Onyx of Oblivion's Cadence Ruin -- saves all fourteen "
            "with minutes to spare, distinct from the third wave's flooding-tunnel entry. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-487",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Lecture Hall Didn't Know What to Do With Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-lecture-hall-didnt-know-what-to-do-with-him.md), the "
            "Blue-Collar Titan Alias Chronicle XII, closing the fourth wave. A Sovereign Trust "
            "engineering college invites Kanja to lecture on tunnel-reading; he teaches the tactile "
            "method learned from the old Killane digger (MCD-442) to a formal academic setting, "
            "arguing formal models and hands-on knowledge are complementary rather than competing. "
            "No new named characters. Closes the Blue-Collar Titan's fourth three-Chronicle wave "
            "(with 'What Even He Couldn't Save,' MCD-485, and 'The Ticking Room,' MCD-486)."
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
            "batch": 154,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Blue-Collar Titan's fourth three-entry Alias Chronicle wave (MCD-485 "
                "through MCD-487). " + BATCH_NOTE
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
