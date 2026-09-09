#!/usr/bin/env python3
"""Batch 95: Uhuru Chronicle II, "What He Finished First" (MCD-358)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-09, no source document. Second entry in Uhuru's own "
    "Chronicles, paying off PH2-044's own stated capstone cost, explicitly flagged as unresolved in "
    "Uhuru Chronicle I's (MCD-345) continuity notes. Full narrative text at "
    "docs/lords-of-cian/chronicles/uhuru-chronicle-ii-what-he-finished-first.md."
)

NEW_RULES = [
    {
        "id": "MCD-358",
        "category": "phase2-homage-chronicle",
        "statement": (
            "Uhuru Chronicle II, \"What He Finished First\" (full narrative text at "
            "docs/lords-of-cian/chronicles/uhuru-chronicle-ii-what-he-finished-first.md), the "
            "second entry in Uhuru's own Chronicles, protagonist Ofin (PH2-044), not a Kanja "
            "Chronicle -- Kanja appears only as an unnamed guest, present in City Hall's late-hour "
            "orbit throughout the night but explicitly sent home and absent from the room itself at "
            "the moment of Ofin's death, granted no intervention or resolution authorship. Pays off "
            "PH2-044's own stated capstone cost directly: the last standing obstruction, a "
            "years-long appointment blockade, breaks completely and permanently one final time on "
            "the page ('The Override' shown in full effect), and the same night, having sent "
            "everyone home to sit alone with the win and finish some paperwork in his own hand, "
            "Ofin dies of a heart attack at his own desk -- dramatizing PH2-044's stated mechanic "
            "('the same engine that breaks every wall against him burns him from the inside') as "
            "immediately and literally as the ability's own text implies. Kept explicitly 'as-built, "
            "not flipped' per PH2-044's own instruction, matching the real historical record of "
            "Harold Washington being found by his own staff the following morning: nothing is "
            "prevented, altered, or intervened upon. Kasa (PH2-038) and Omoba (PH2-042) are "
            "referenced consistently with their already-locked coalition roles, not independently "
            "detailed here. No new named characters; no new proper nouns requiring a collision "
            "check. Closes Ofin's own arc as the deliberate capstone cost his signature ability "
            "always foreshadowed."
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
            "batch": 95,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-09, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "Uhuru Chronicle II (MCD-358), 'What He Finished First' -- pays off PH2-044's own "
                "stated capstone cost, Ofin's 1987 death at his own desk, kept as-built per that "
                "rule's own instruction. " + BATCH_NOTE
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
