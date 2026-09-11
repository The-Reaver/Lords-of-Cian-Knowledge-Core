#!/usr/bin/env python3
"""Batch 184: Lock the Blue-Collar Titan's fifth three-entry Alias Chronicle wave (MCD-537 through
MCD-539), continuing uninterrupted per Abad's authorization."""
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
        "id": "MCD-537",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Mine That Wouldn't Give Them Up\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-mine-that-wouldnt-give-them-up.md), the Blue-Collar "
            "Titan Alias Chronicle XIII, first entry in the fifth wave. Directorate engineers "
            "deliberately trigger a mine collapse to trap union organizers and guard every known "
            "exit; a detailed combined rescue-and-combat showcase has Kanja find and use an "
            "unmapped secondary shaft the collapse itself opened, rescuing all twelve organizers "
            "and disarming the guards before they realize the rescue already happened. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-538",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Monument He Refused to Read Dishonestly\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-monument-he-refused-to-read-dishonestly.md), the "
            "Blue-Collar Titan Alias Chronicle XIV. A structurally sound Directorate monument is "
            "hated by the district; Kanja refuses his own crew's request to fabricate a safety "
            "condemnation to justify tearing it down, insisting the district organize an honest "
            "political removal instead -- establishing that the alias's structural-honesty "
            "principle holds even against a cause he personally supports. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-539",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Guild That Made Him One of Their Own\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-guild-that-made-him-one-of-their-own.md), the "
            "Blue-Collar Titan Alias Chronicle XV, closing the fifth wave. The tradesmen's guild "
            "from 'The Guild Master's Test' (MCD-409) votes Kanja honorary membership, explicitly "
            "crediting his accumulated honest failures (the eastern gallery collapse, MCD-485; the "
            "admitted rushed reheat, MCD-409) rather than only his successes as the basis for the "
            "honor. No new named characters. Closes the Blue-Collar Titan's fifth three-Chronicle "
            "wave (with 'The Mine That Wouldn't Give Them Up,' MCD-537, and 'The Monument He "
            "Refused to Read Dishonestly,' MCD-538)."
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
            "batch": 184,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Blue-Collar Titan's fifth three-entry Alias Chronicle wave (MCD-537 "
                "through MCD-539). " + BATCH_NOTE
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
