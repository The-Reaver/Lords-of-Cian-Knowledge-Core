#!/usr/bin/env python3
"""Batch 84: Aztlan Chronicle I ("One Body, Many Hands"), the first
entry in Aztlan's own Chronicle series -- protagonist Ollin (PH2-023),
Kanja as unnamed guest. Continues LA's own run of territory Chronicles.
Authorized under Abad's blanket instruction to complete all remaining LA
and Detroit territory Chronicles uninterrupted."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Aztlan Chronicle I ('One Body, Many Hands'), chat-drafted 2026-09-09, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/aztlan-chronicle-i-one-body-many-hands.md."
)

NEW_RULES = [
    {
        "id": "MCD-347",
        "category": "World Mechanics",
        "statement": (
            "Aztlan Chronicle I ('One Body, Many Hands') is the first "
            "entry in Aztlan's own Chronicle series, per the established "
            "structure: each Phase 2 homage-era territory has its own "
            "Chronicles, with its own leader as protagonist and Kanja "
            "appearing only as an unnamed guest. During an East LA "
            "walkout, a counter-crowd attacks the march's flank where the "
            "police line thins; Ollin's forty personally drilled people "
            "hold a defensive line together. Ollin's signature ability "
            "('The Formation,' PH2-023) is shown directly in operation "
            "for the first time: the drilled group fights and moves as a "
            "single, dramatically amplified force, exactly matching the "
            "ability's stated mechanic. The ability's cost (fracturing "
            "explosively once ignored internal grievance reaches its "
            "breaking point) is deliberately not shown here -- this "
            "Chronicle is set before the ability's own already-locked "
            "backstory event (Iya's 1970 walkout over unaddressed "
            "sexism), and Ollin's closing line is a deliberate, "
            "unresolved forward reference to that future rupture rather "
            "than a payoff. An unnamed Kanja is embedded inside the "
            "formation itself during the confrontation without taking "
            "command, credit, or narrative authorship. No new named "
            "characters introduced. Slots into no existing mainline "
            "battle -- original homage-era material set in Aztlan "
            "itself, continuing Los Angeles's own run of territory "
            "Chronicles (Sankofa already has one; Atunbi, Ijoko, and "
            "Orin still do not)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = (
    'Abad: "continue uninterrupted until completion this includes test, '
    'commit, push to main origin and google drive" -- blanket '
    "authorization covering all remaining LA (4) and Detroit (5) "
    "territory Chronicles, applied per-batch as they are drafted."
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
            "batch": 84,
            "source_doc": (
                "Aztlan Chronicle I ('One Body, Many Hands', MCD-347) -- "
                "the thirteenth territory Chronicle overall and Aztlan's "
                "first (Ollin), continuing Los Angeles's own run of "
                "territory Chronicles."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "8.7"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
