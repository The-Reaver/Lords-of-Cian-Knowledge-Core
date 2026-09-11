#!/usr/bin/env python3
"""Batch 121: Lock the Sovereign Ghost of the Great Sea's second three-entry Alias Chronicle
wave (MCD-410 through MCD-412), continuing uninterrupted through all remaining alias second
waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = 'Abad: "complete all of the Alias drafts continuously uninterrupted."'

NEW_RULES = [
    {
        "id": "MCD-410",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Wreck They Named for Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-wreck-they-named-for-him.md), Sovereign Ghost "
            "Alias Chronicle IV, first entry in the second wave. An ordinary storm sinks a "
            "merchant convoy, but rumor falsely attaches the fleet to it, triggering a formal "
            "Trust diplomatic complaint and denied insurance claims; Kanja surrenders the fleet's "
            "own navigation logs to a neutral Astral Archipelago tribunal, an unprecedented "
            "sacrifice of operational secrecy, and is cleared, forcing the insurers to honor the "
            "original claims. No new named characters beyond the already-locked Dol Maren."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-411",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Hull Told Dol Maren\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-hull-told-dol-maren.md), Sovereign Ghost "
            "Alias Chronicle V. A detailed naval technical showcase from Dol Maren's perspective "
            "(already locked, CC-120/CC-121): during a genuine hurricane, The Audit's "
            "deliberately flexible hull construction outlasts a rigid-hulled Trust blockade "
            "squadron's pursuit, disabling two pursuing ships through ordinary stress fractures "
            "Maren had already predicted. The squadron's after-action report misattributes the "
            "outcome to 'rebel naval technology' rather than patient shipwright engineering. No "
            "new named characters beyond the already-locked Dol Maren."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-412",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Girl Who Waited for Black Sails\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-girl-who-waited-for-black-sails.md), Sovereign "
            "Ghost Alias Chronicle VI, closing the second wave. A seven-year-old's family fishing "
            "boat, stranded and facing seizure by a Trust requisition vessel, is saved when the "
            "fleet simply positions itself between the two boats and holds position until the "
            "requisition captain withdraws -- no shots fired, no boarding. Decades later she tells "
            "her grandchildren the story, extending VB-060's presence doctrine into protection "
            "rather than only terror, mirroring 'What the Lantern Watch Prayed For' (MCD-379) from "
            "the rescued side. No new named characters. Closes the Sovereign Ghost of the Great "
            "Sea's second three-Chronicle wave (with 'The Wreck They Named for Him,' MCD-410, and "
            "'What the Hull Told Dol Maren,' MCD-411)."
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
            "batch": 121,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Sovereign Ghost of the Great Sea's second three-entry Alias Chronicle "
                "wave (MCD-410 through MCD-412), the fifth of eleven second waves in a continuous "
                "run. " + BATCH_NOTE
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
