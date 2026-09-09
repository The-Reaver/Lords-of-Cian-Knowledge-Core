#!/usr/bin/env python3
"""Batch 90: Hekalu Chronicle I ("Whoever Sits Down"), the first entry
in Hekalu's own Chronicle series -- protagonist Adom (PH2-055), Kanja as
unnamed guest. Continues Detroit's own run of territory Chronicles."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Hekalu Chronicle I ('Whoever Sits Down'), chat-drafted 2026-09-09, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/hekalu-chronicle-i-whoever-sits-down.md."
)

NEW_RULES = [
    {
        "id": "MCD-353",
        "category": "World Mechanics",
        "statement": (
            "Hekalu Chronicle I ('Whoever Sits Down') is the first entry "
            "in Hekalu's own Chronicle series, per the established "
            "structure: each Phase 2 homage-era territory has its own "
            "Chronicles, with its own leader as protagonist and Kanja "
            "appearing only as an unnamed guest. A rival cooperative "
            "owner, suspicious of Adom's (PH2-055) table, freely chooses "
            "to sit and eat, and returns days later with an unprompted "
            "joint wage-floor proposal he cannot fully explain offering. "
            "Adom's signature ability ('The Common Table,' PH2-055) is "
            "shown directly in operation for the first time, exactly "
            "matching its stated mechanic. The ability's cost is "
            "dramatized explicitly through both the rival's own required "
            "free choice to sit and a referenced past case of a man who "
            "sat down without ever meaning to be there and left entirely "
            "unchanged, matching PH2-055's stated limitation ('cannot be "
            "forced on the unwilling'). An unnamed Kanja is seated at the "
            "table itself throughout without taking command, credit, or "
            "narrative authorship. No new named characters introduced. "
            "Slots into no existing mainline battle -- original "
            "homage-era material set in Hekalu itself, continuing "
            "Detroit's own run of territory Chronicles (Kazi and Taifa "
            "already have one; Nyansa and Kiti still do not)."
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
            "batch": 90,
            "source_doc": (
                "Hekalu Chronicle I ('Whoever Sits Down', MCD-353) -- "
                "the nineteenth territory Chronicle overall and Hekalu's "
                "first (Adom), continuing Detroit's own run of territory "
                "Chronicles."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "9.3"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
