#!/usr/bin/env python3
"""Batch 87: Orin Chronicle I ("What Can't Be Sold"), the first entry in
Orin's own Chronicle series -- protagonist Onilu (PH2-029), Kanja as
unnamed guest. Completes a first Chronicle entry for all five LA
territories."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Orin Chronicle I ('What Can't Be Sold'), chat-drafted 2026-09-09, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/orin-chronicle-i-what-cant-be-sold.md."
)

NEW_RULES = [
    {
        "id": "MCD-350",
        "category": "World Mechanics",
        "statement": (
            "Orin Chronicle I ('What Can't Be Sold') is the first entry "
            "in Orin's own Chronicle series, per the established "
            "structure: each Phase 2 homage-era territory has its own "
            "Chronicles, with its own leader as protagonist and Kanja "
            "appearing only as an unnamed guest. During a small "
            "storefront performance, everyone genuinely listening comes "
            "away carrying a real bond to everyone else who heard it "
            "with them. Onilu's signature ability ('The Ark,' PH2-029) "
            "is shown directly in operation for the first time, then its "
            "cost dramatized in the same episode: Onilu deliberately "
            "allows a would-be promoter to record the final number, and "
            "the binding is demonstrably absent from the resulting "
            "recording when played back to a room that never stood "
            "together in it, exactly matching PH2-029's stated "
            "limitation that commercializing the performance destroys "
            "the binding completely and permanently for that "
            "performance. An unnamed Kanja is present at the back of the "
            "room and stays after to help stack chairs, without taking "
            "command, credit, or narrative authorship. No new named "
            "characters introduced. Slots into no existing mainline "
            "battle -- original homage-era material set in Orin itself, "
            "and completes a first Chronicle entry for every one of Los "
            "Angeles's five territories (Sankofa, Aztlan, Atunbi, Ijoko, "
            "Orin), matching NYC's and Chicago's own completed sets."
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
            "batch": 87,
            "source_doc": (
                "Orin Chronicle I ('What Can't Be Sold', MCD-350) -- the "
                "sixteenth territory Chronicle overall and Orin's first "
                "(Onilu), completing a first Chronicle entry for all "
                "five Los Angeles territories, matching NYC's and "
                "Chicago's own completed sets."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "9.0"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
