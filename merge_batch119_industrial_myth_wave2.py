#!/usr/bin/env python3
"""Batch 119: Lock the Industrial Myth's second three-entry Alias Chronicle wave (MCD-404
through MCD-406), continuing uninterrupted through all remaining alias second waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = 'Abad: "complete all of the Alias drafts continuously uninterrupted."'

NEW_RULES = [
    {
        "id": "MCD-404",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ledger They Tried to Burn\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ledger-they-tried-to-burn.md), Industrial Myth "
            "Alias Chronicle IV, first entry in the second wave. A district administrator orders "
            "a raid to burn the crew's recording tent and its ledger, not realizing Ezio Valcari "
            "had already dispersed seven identical copies among ordinary-looking workers across "
            "the district; the raid destroys only a decoy and generates its own documented "
            "incident, ending the administrator's career. No new named characters beyond the "
            "already-locked Ezio Valcari."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-405",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Cost of Four Days\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-cost-of-four-days.md), Industrial Myth Alias "
            "Chronicle V. A foreman's daughter dies of a treatable fever while Kanja is still "
            "days from completing a district's testimony; the foreman directly accuses the "
            "patient, unarmed method of costing her the time she needed. Kanja does not defend "
            "himself with the method's aggregate success, instead admitting the uncertainty and "
            "the real cost some people pay for a method that saves more people overall. No new "
            "named characters; the foreman is unnamed and one-scene. A deliberately unresolved, "
            "harder entry for this wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-406",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Administrator Who Opened His Own Books\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-administrator-who-opened-his-own-books.md), "
            "Industrial Myth Alias Chronicle VI, closing the second wave. A hostile district "
            "administrator refuses to open his wage records for three days, then does so once he "
            "calculates that participating in an already-forming account of four hundred "
            "cross-corroborated worker statements gives him more control than continued silence. "
            "His own testimony becomes one of the method's most-cited examples. No new named "
            "characters; the administrator is unnamed and one-scene. Closes the Industrial Myth's "
            "second three-Chronicle wave (with 'The Ledger They Tried to Burn,' MCD-404, and "
            "'The Cost of Four Days,' MCD-405)."
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
            "batch": 119,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Industrial Myth's second three-entry Alias Chronicle wave (MCD-404 "
                "through MCD-406), the third of eleven second waves in a continuous run. "
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
