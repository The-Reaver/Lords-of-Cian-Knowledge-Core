#!/usr/bin/env python3
"""Batch 108: Lock the Industrial Myth's three-entry Alias Chronicle wave (MCD-371 through
MCD-373), continuing uninterrupted through the remaining alias waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-10, no source document."

BATCH_NOTE = (
    'Abad: "continue uninterrupted until completion this includes test, commit, push to main '
    'origin" (covering all ten remaining alias waves).'
)

NEW_RULES = [
    {
        "id": "MCD-371",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Worst-Off First\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-worst-off-first.md), Industrial Myth Alias "
            "Chronicle I. Rebellion era, unarmed throughout, matching MCD-244's stated ethos. At "
            "a dye-works district that stages its best-treated workers at the front gate for the "
            "visiting crew, Kanja instead goes first to the dye-vat handlers at the yard's "
            "far edge -- the worst-treated, never previously asked anything by a visitor -- and "
            "works backward toward the front gate, documenting testimony in the order asked "
            "rather than the order offered. Establishes 'start with the worst-treated' as the "
            "Industrial Myth's own signature discipline. No new named characters. First entry in "
            "the Industrial Myth's three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-372",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Hand That Stayed Open\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-hand-that-stayed-open.md), Industrial Myth Alias "
            "Chronicle II. Rebellion era, unarmed throughout. A forty-strong garrison column sent "
            "to break up ledger-taking at a weaving district finds Kanja seated, unarmed, holding "
            "only the ledger itself; the standoff holds until two soldiers quietly lower their "
            "own weapons and the captain withdraws, unable to locate a fight that was never "
            "actually offered. Extends VB-060's presence trait into a register where the "
            "'already-decided' quality is the certainty that violence has no target to land on. "
            "No new named characters; the captain is unnamed and one-scene. Second entry in the "
            "Industrial Myth's three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-373",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Boy Who Kept the Numbers Honest\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-boy-who-kept-the-numbers-honest.md), Industrial "
            "Myth Alias Chronicle III, closing the wave. Set during the Furnace District Strike "
            "itself (MCD-244, age 21), from Ezio Valcari's perspective (already a locked named "
            "character, roughly sixteen at this point). Dramatizes Ezio's unstated corrective "
            "role in the strike's documented method: cross-checking worker testimony against the "
            "district's own production records and quietly adjusting entries upward whenever a "
            "frightened worker under-claimed what they were actually owed, rather than accepting "
            "testimony at face value. No new named characters beyond the already-locked Ezio "
            "Valcari. Closes the Industrial Myth's three-Chronicle wave (with 'The Worst-Off "
            "First,' MCD-371, and 'The Hand That Stayed Open,' MCD-372)."
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
            "batch": 108,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Industrial Myth's three-entry Alias Chronicle wave (MCD-371 through "
                "MCD-373), the second of ten remaining alias waves. " + BATCH_NOTE
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
