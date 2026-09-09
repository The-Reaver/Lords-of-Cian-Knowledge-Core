#!/usr/bin/env python3
"""Batch 92: Kiti Chronicle I ("What Wore Down Instead"), the first
entry in Kiti's own Chronicle series -- protagonist Owusu (PH2-059),
Kanja as unnamed guest. Completes a first Chronicle entry for all five
Detroit territories, and closes out territory-Chronicle coverage for
every homage-era city."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Kiti Chronicle I ('What Wore Down Instead'), chat-drafted 2026-09-09, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/kiti-chronicle-i-what-wore-down-instead.md."
)

NEW_RULES = [
    {
        "id": "MCD-355",
        "category": "World Mechanics",
        "statement": (
            "Kiti Chronicle I ('What Wore Down Instead') is the first "
            "entry in Kiti's own Chronicle series, per the established "
            "structure: each Phase 2 homage-era territory has its own "
            "Chronicles, with its own leader as protagonist and Kanja "
            "appearing only as an unnamed guest. A manufactured scandal, "
            "run for three weeks by the old machine, is meant to wear "
            "Owusu (PH2-059) down; instead his next election comes in "
            "stronger. Owusu's signature ability ('The Long Tenure,' "
            "PH2-059) is shown directly in operation for the first time: "
            "sustained attrition against him while he holds the seat "
            "strengthens his grip rather than weakening it, exactly "
            "matching the ability's stated mechanic. The ability's cost "
            "is stated explicitly as foreshadowing rather than "
            "dramatized in the moment, matching the same restraint used "
            "for Ofin's capstone cost in Uhuru Chronicle I (MCD-345): "
            "Owusu states plainly, unprompted, that the strength is "
            "purely institutional and lapses completely the instant he "
            "leaves the seat, matching PH2-059's stated limitation "
            "exactly. The old machine's operatives are deliberately left "
            "unnamed. An unnamed Kanja is a quiet presence around the "
            "office across the stretch without taking command, credit, "
            "or narrative authorship. No new named characters "
            "introduced. Slots into no existing mainline battle -- "
            "original homage-era material set in Kiti itself, and "
            "completes a first Chronicle entry for every one of "
            "Detroit's five territories (Kazi, Taifa, Hekalu, Nyansa, "
            "Kiti), which in turn completes territory-Chronicle coverage "
            "at the first-Chronicle level for all four homage-era "
            "cities built so far (NYC, Chicago, LA, Detroit)."
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
            "batch": 92,
            "source_doc": (
                "Kiti Chronicle I ('What Wore Down Instead', MCD-355) -- "
                "the twenty-first territory Chronicle overall and Kiti's "
                "first (Owusu), completing a first Chronicle entry for "
                "all five Detroit territories and closing out "
                "territory-Chronicle coverage for every homage-era city "
                "built so far (NYC, Chicago, LA, Detroit)."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "9.5"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
