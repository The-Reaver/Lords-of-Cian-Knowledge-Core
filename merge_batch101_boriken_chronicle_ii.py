#!/usr/bin/env python3
"""Batch 101: Boriken Chronicle II, "What Memory Could Carry Back" (MCD-364)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-10, no source document. Second entry in Boriken's "
    "own Chronicles, extending (not paying off a pre-flagged hook) a specific, deliberate detail "
    "in Boriken Chronicle I's (MCD-341) own wording. Full narrative text at "
    "docs/lords-of-cian/chronicles/boriken-chronicle-ii-what-memory-could-carry-back.md."
)

NEW_RULES = [
    {
        "id": "MCD-364",
        "category": "phase2-homage-chronicle",
        "statement": (
            "Boriken Chronicle II, \"What Memory Could Carry Back\" (full narrative text at "
            "docs/lords-of-cian/chronicles/boriken-chronicle-ii-what-memory-could-carry-back.md), "
            "the second entry in Boriken's own Chronicles, protagonist Guani (PH2-010), not a "
            "Kanja Chronicle -- Kanja appears only as an unnamed guest, present across four years "
            "of reconstruction sessions, transcribing others' memories without contributing any of "
            "his own or taking command, credit, or resolution authorship. Extends a specific, "
            "deliberate detail in Boriken Chronicle I's (MCD-341) own wording: the church hall's "
            "six-year debt ledger, burned in the raid, 'cannot be fully rebuilt from the memory of "
            "the forty people who held pieces of it' -- implying partial recovery, dramatized here "
            "for the first time. Over four years of monthly sessions, the original forty "
            "contributors dwindle to twenty-six (through relocation, attrition, and death) while "
            "reconstructing roughly four-fifths of the six-year account from memory alone. Dona "
            "Alma, a new minor named character (collision-checked against the full live ledger, "
            "zero prior hits), dies shortly after recovering a key eleven-month gap in the ledger, "
            "in keeping with the Chronicle's theme of memory as a finite, mortal resource. Guani "
            "explicitly reframes the unnamed Commissioner's original arson as a category error -- "
            "burning a record while mistaking it for the debt itself, which lived on in the people "
            "who remembered it -- and states plainly that some portion of what burned is "
            "permanently, irrecoverably gone, honoring rather than resolving that loss. The unnamed "
            "Commissioner from Chronicle I is referenced but not brought back on-page; his fate "
            "stays deliberately unaddressed. No new proper nouns beyond Dona Alma requiring a "
            "collision check. Eighth territory overall (after Xaragua, Areito, Guanin, Uhuru, "
            "Aztlan, Sankofa, and Kazi) to receive a second Chronicle entry."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "lock it."'


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
            "batch": 101,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-10, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "Boriken Chronicle II (MCD-364), 'What Memory Could Carry Back' -- extends "
                "Boriken Chronicle I's own wording that the burned ledger 'cannot be fully "
                "rebuilt,' dramatizing four-fifths partial recovery across four years. "
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
