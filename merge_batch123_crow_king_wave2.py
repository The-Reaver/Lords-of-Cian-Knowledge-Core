#!/usr/bin/env python3
"""Batch 123: Lock the Crow King's second three-entry Alias Chronicle wave (MCD-416 through
MCD-418), continuing uninterrupted through all remaining alias second waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = 'Abad: "complete all of the Alias drafts continuously uninterrupted."'

NEW_RULES = [
    {
        "id": "MCD-416",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Trap That Almost Closed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-trap-that-almost-closed.md), Crow King Alias "
            "Chronicle IV, first entry in the second wave. A single unbriefed private, "
            "recognizing the Hymn-Engine's sub-bass chant by ear from growing up near a "
            "work-chant district, catches what a purpose-built sensor grid missed and locates the "
            "real evacuation column; Kanja buys the evacuation's last minutes through "
            "conversation rather than force, and the private's accurate report becomes the "
            "single most useful piece of Directorate intelligence gathered against the doctrine. "
            "A genuine near-failure rather than another clean win. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-417",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"When the Crow Could Not Fly\" (full narrative text at "
            "docs/lords-of-cian/chronicles/when-the-crow-could-not-fly.md), Crow King Alias "
            "Chronicle V. The private's report (MCD-416) reaches a garrison commander in time to "
            "spring a genuine counter-encirclement on a half-evacuated compound; with no clean "
            "evasion available, Kanja fights through it instead, demonstrating Mafesto's Kinetic "
            "Transfer System, Obsidian Malice striking the encirclement's weakest coordination "
            "seam, and Onyx's Cadence Ruin buying the final evacuation window. The garrison's own "
            "doctrine review flags that every existing countermeasure assumed the Crow King's only "
            "weapon was escape. No new named characters; the garrison commander is unnamed and "
            "one-scene."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-418",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Voice That Carried Three Hundred\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-voice-that-carried-three-hundred.md), Crow King "
            "Alias Chronicle VI, closing the second wave. Years later, one of the crew's original "
            "Hymn-Engine singers -- permanently rasp-voiced from the technique's six-week "
            "rehearsal -- teaches a new recruit the real cost behind the marsh trick's mechanics: "
            "sustained, relaxed consistency rather than forced power, and a toll to her voice she "
            "has never regretted paying. No new named characters. Closes the Crow King's second "
            "three-Chronicle wave (with 'The Trap That Almost Closed,' MCD-416, and 'When the "
            "Crow Could Not Fly,' MCD-417)."
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
            "batch": 123,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Crow King's second three-entry Alias Chronicle wave (MCD-416 through "
                "MCD-418), the seventh of eleven second waves in a continuous run. " + BATCH_NOTE
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
