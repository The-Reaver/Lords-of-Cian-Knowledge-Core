#!/usr/bin/env python3
"""Batch 183: Lock the Industrial Myth's fifth three-entry Alias Chronicle wave (MCD-534 through
MCD-536), continuing uninterrupted per Abad's authorization."""
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
        "id": "MCD-534",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Numbers He Couldn't Prove\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-numbers-he-couldnt-prove.md), the Industrial Myth "
            "Alias Chronicle XIII, first entry in the fifth wave. A dye-works administrator "
            "fabricates a plausible counter-tally with no independent way to verify either account; "
            "Kanja falls back on cross-referenced worker testimony rather than clean numbers, "
            "reaching an imperfect settlement -- the first genuine limit of the tally method. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-535",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The District Chain\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-district-chain.md), the Industrial Myth Alias "
            "Chronicle XIV. A detailed, sustained month-long campaign across three connected mill "
            "districts owned by the same regional concern: Kanja personally builds and combines "
            "three separate tallies into a single case proving coordinated wage suppression, the "
            "method's first horizontal multi-district application and largest settlement to date. "
            "No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-536",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Pell Ostra Noticed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-pell-ostra-noticed.md), the Industrial Myth Alias "
            "Chronicle XV, closing the fifth wave. Pell Ostra (already locked) volunteers to guard a "
            "tally operation and reflects on what it means to protect a deliberately unarmed "
            "persona -- ensuring nothing ever gets close enough to test the principle, rather than "
            "intercepting threats Kanja would otherwise handle himself. No new named characters "
            "beyond the already-locked Pell Ostra. Closes the Industrial Myth's fifth "
            "three-Chronicle wave (with 'The Numbers He Couldn't Prove,' MCD-534, and 'The District "
            "Chain,' MCD-535)."
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
            "batch": 183,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Industrial Myth's fifth three-entry Alias Chronicle wave (MCD-534 "
                "through MCD-536). " + BATCH_NOTE
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
