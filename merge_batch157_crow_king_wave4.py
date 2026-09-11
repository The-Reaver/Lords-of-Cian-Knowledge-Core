#!/usr/bin/env python3
"""Batch 157: Lock the Crow King's fourth three-entry Alias Chronicle wave (MCD-494 through
MCD-496), continuing uninterrupted per Abad's authorization."""
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
        "id": "MCD-494",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Lie That Cost Someone Else\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-lie-that-cost-someone-else.md), the Crow King Alias "
            "Chronicle X, first entry in the fourth wave. A false signal meant to redirect a "
            "Directorate patrol away from a convoy instead frightens an uninvolved farming family "
            "into the patrol's path; the convoy survives but the bystander harm is real, prompting "
            "Kanja to add a bystander-mapping verification step to the Hymn-Engine method -- the "
            "first genuine failure entry of this alias's run. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-495",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Braid and the Blade\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-braid-and-the-blade.md), the Crow King Alias "
            "Chronicle XI. A detailed hybrid showcase combining the Braid's three interleaved false "
            "signals (MCD-384) with a full Trinity combat sequence for the first time -- the "
            "deception consolidates a Reth Hollow garrison into a single position rather than "
            "scattering it, which Mafesto, Obsidian Malice, and Onyx of Oblivion then defeat "
            "directly, establishing the Hymn-Engine as an offensive setup tool, not only an evasion "
            "one. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-496",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Cipher That Learned to Listen Back\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-cipher-that-learned-to-listen-back.md), the Crow "
            "King Alias Chronicle XII, closing the fourth wave. A Directorate cryptographer cracks "
            "a partial structural signature in the Hymn-Engine's patterns; the already-locked "
            "apprentice (MCD-451) detects the erosion first and personally designs the new, more "
            "varied constructions that render the breakthrough obsolete, taking real authorship of "
            "the method's first evolution. No new named characters beyond the already-locked "
            "apprentice. Closes the Crow King's fourth three-Chronicle wave (with 'The Lie That "
            "Cost Someone Else,' MCD-494, and 'The Braid and the Blade,' MCD-495)."
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
            "batch": 157,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Crow King's fourth three-entry Alias Chronicle wave (MCD-494 through "
                "MCD-496). " + BATCH_NOTE
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
