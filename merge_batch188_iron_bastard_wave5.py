#!/usr/bin/env python3
"""Batch 188: Lock the Iron Bastard's fifth three-entry Alias Chronicle wave (MCD-549 through
MCD-551), continuing uninterrupted per Abad's authorization."""
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
        "id": "MCD-549",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Day of Ten Engines\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-day-of-ten-engines.md), the Iron Bastard Alias "
            "Chronicle XIII, first entry in the fifth wave. A detailed combat showcase against ten "
            "simultaneous siege engines assaulting a causeway; Kanja reads and disables nine in "
            "sequence, explicitly taking the extra seconds to verify each reading despite time "
            "pressure, directly applying the doubled-verification discipline learned from 'The "
            "Frequency He Read Wrong' (MCD-497). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-550",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Wall That Lied to Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-wall-that-lied-to-him.md), the Iron Bastard Alias "
            "Chronicle XIV. A Directorate engineer builds a wall with deliberately falsified stress "
            "signatures designed to deceive the resonance doctrine's own diagnostic method into a "
            "confident but wrong discharge; Kanja's doubled verification catches the deception and "
            "finds the wall's genuine, unrelated weak point instead -- the first deliberate, "
            "engineered deception of the doctrine's mechanism itself. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-551",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Scholar Finally Published\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-scholar-finally-published.md), the Iron Bastard "
            "Alias Chronicle XV, closing the fifth wave. The Trust scholar from MCD-421 finally "
            "publishes his once-shelved research through an independent academy years later, "
            "extending the doctrine's honesty-outlasts-suppression theme into institutional "
            "legitimization achieved through patience. No new named characters beyond the already-"
            "locked scholar. Closes the Iron Bastard's fifth three-Chronicle wave (with 'The Day of "
            "Ten Engines,' MCD-549, and 'The Wall That Lied to Him,' MCD-550)."
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
            "batch": 188,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Iron Bastard's fifth three-entry Alias Chronicle wave (MCD-549 through "
                "MCD-551). " + BATCH_NOTE
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
