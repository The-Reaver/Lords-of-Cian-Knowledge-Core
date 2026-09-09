#!/usr/bin/env python3
"""Batch 85: Atunbi Chronicle I ("What Takes Root"), the first entry in
Atunbi's own Chronicle series -- protagonist Oluwole (PH2-025), Kanja as
unnamed guest. Continues LA's own run of territory Chronicles."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Atunbi Chronicle I ('What Takes Root'), chat-drafted 2026-09-09, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/atunbi-chronicle-i-what-takes-root.md."
)

NEW_RULES = [
    {
        "id": "MCD-348",
        "category": "World Mechanics",
        "statement": (
            "Atunbi Chronicle I ('What Takes Root') is the first entry "
            "in Atunbi's own Chronicle series, per the established "
            "structure: each Phase 2 homage-era territory has its own "
            "Chronicles, with its own leader as protagonist and Kanja "
            "appearing only as an unnamed guest. A demolition crew "
            "attacks a garden lot Oluwole (PH2-025) has held and worked "
            "at dawn, before the block can organize a response. "
            "Oluwole's signature ability ('Don't Move, Improve,' "
            "PH2-025) is shown directly in operation for the first time "
            "-- the ground he has stayed rooted on has become genuinely "
            "more resilient -- while the scene also dramatizes the "
            "ability's stated cost precisely: the demolition crew takes "
            "a third of the garden before the ability's own slow "
            "mechanism can do anything about it, exactly matching "
            "PH2-025's stated limitation ('useless against anything fast "
            "enough to strike and leave before it takes hold'). What "
            "actually stops the attack is ordinary human numbers "
            "arriving in time, not the gift itself, stated plainly on "
            "the page rather than left implicit. An unnamed Kanja is "
            "present helping turn soil across several mornings and "
            "during the confrontation without taking command, credit, or "
            "narrative authorship. No new named characters introduced. "
            "Slots into no existing mainline battle -- original "
            "homage-era material set in Atunbi itself, continuing Los "
            "Angeles's own run of territory Chronicles (Sankofa and "
            "Aztlan already have one; Ijoko and Orin still do not)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = (
    'Abad: "continue uninterrupted until completion this includes test, '
    'commit, push to main origin and google drive" -- blanket '
    "authorization covering all remaining LA and Detroit territory "
    "Chronicles, applied per-batch as they are drafted."
)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 85,
            "source_doc": (
                "Atunbi Chronicle I ('What Takes Root', MCD-348) -- the "
                "fourteenth territory Chronicle overall and Atunbi's "
                "first (Oluwole), continuing Los Angeles's own run of "
                "territory Chronicles."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "8.8"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
