#!/usr/bin/env python3
"""Batch 118: Lock the Trench Monarch's second three-entry Alias Chronicle wave (MCD-401 through
MCD-403), continuing uninterrupted through all remaining alias second waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = 'Abad: "complete all of the Alias drafts continuously uninterrupted."'

NEW_RULES = [
    {
        "id": "MCD-401",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Man Who Wore the Name\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-man-who-wore-the-name.md), Trench Monarch Alias "
            "Chronicle IV, first entry in the second wave. An impersonator extorts three canal "
            "districts for a month claiming to act on Kanja's authority; Kanja confronts him "
            "without drawing Onyx, forces public restitution, and states the name can't be "
            "controlled from being borrowed but can be made costly to borrow falsely. No new "
            "named characters beyond the already-locked Callum Breck."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-402",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fight the Sword Couldn't Read\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fight-the-sword-couldnt-read.md), Trench Monarch "
            "Alias Chronicle V. A deliberately arrhythmic, patternless duelist defeats Onyx of "
            "Oblivion's Cadence Ruin and Veil Piercer, both of which depend on a detectable "
            "pattern to exploit; Kanja wins the twenty-minute bout through plain endurance rather "
            "than the sword's gifts -- the first established limit of Onyx's powers, consistent "
            "with and not contradicting prior showcases (MCD-369, MCD-398), which involved "
            "opponents with genuine tactical patterns. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-403",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Forehead Tavin Greer Kept Clean\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-forehead-tavin-greer-kept-clean.md), Trench "
            "Monarch Alias Chronicle VI, closing the second wave. Decades after the Dredge-Line "
            "Ambush, the already-locked Tavin Greer (CC-118) reflects that his career survived "
            "and thrived after being publicly marked, once he understood Callum Breck's chalking "
            "was never really about humiliating him personally; he kept his own precise, honest "
            "after-action report as a private dignity from that day. No new named characters "
            "beyond the already-locked Tavin Greer and referenced Callum Breck. Closes the Trench "
            "Monarch's second three-Chronicle wave (with 'The Man Who Wore the Name,' MCD-401, "
            "and 'The Fight the Sword Couldn't Read,' MCD-402)."
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
            "batch": 118,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Trench Monarch's second three-entry Alias Chronicle wave (MCD-401 "
                "through MCD-403), the second of eleven second waves in a continuous run. "
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
