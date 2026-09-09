#!/usr/bin/env python3
"""Batch 88: Kazi Chronicle I ("The Line That Heard Him"), the first
entry in Kazi's own Chronicle series -- protagonist Irin (PH2-051),
Kanja as unnamed guest. Opens Detroit's own run of territory
Chronicles."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Kazi Chronicle I ('The Line That Heard Him'), chat-drafted 2026-09-09, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/kazi-chronicle-i-the-line-that-heard-him.md."
)

NEW_RULES = [
    {
        "id": "MCD-351",
        "category": "World Mechanics",
        "statement": (
            "Kazi Chronicle I ('The Line That Heard Him') is the first "
            "entry in Kazi's own Chronicle series, per the established "
            "structure: each Phase 2 homage-era territory has its own "
            "Chronicles, with its own leader as protagonist and Kanja "
            "appearing only as an unnamed guest. When a foreman keeps "
            "the assembly line running around a jammed press rather than "
            "relieving the two men absorbing its backlog, Irin (PH2-051) "
            "calls a halt from his own station. Irin's signature ability "
            "('The Line Stops,' PH2-051) is shown directly in operation "
            "for the first time: every man bound into the same "
            "production chain feels the halt instantly, without a word "
            "passed hand to hand, exactly matching the ability's stated "
            "mechanic. The same episode dramatizes the ability's stated "
            "cost precisely: three outside hires brought in to break the "
            "standstill feel nothing at all, since they were never "
            "structurally bound into the same chain of labor, exactly "
            "matching PH2-051's stated limitation. The foreman is "
            "deliberately left unnamed, matching established precedent "
            "for undetailed antagonists. An unnamed Kanja is hired onto "
            "the line itself for the week and present at his own station "
            "without taking command, credit, or narrative authorship. No "
            "new named characters introduced. Slots into no existing "
            "mainline battle -- original homage-era material set in Kazi "
            "itself, and opens Detroit's own run of territory Chronicles "
            "(Taifa, Hekalu, Nyansa, and Kiti still have none)."
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
            "batch": 88,
            "source_doc": (
                "Kazi Chronicle I ('The Line That Heard Him', MCD-351) -- "
                "the seventeenth territory Chronicle overall and Kazi's "
                "first (Irin), opening Detroit's own run of territory "
                "Chronicles."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "9.1"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
