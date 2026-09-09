#!/usr/bin/env python3
"""Batch 86: Ijoko Chronicle I ("What Laughter Couldn't Move"), the
first entry in Ijoko's own Chronicle series -- protagonist Adwoa
(PH2-027), Kanja as unnamed guest. Continues LA's own run of territory
Chronicles."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Ijoko Chronicle I ('What Laughter Couldn't Move'), chat-drafted "
    "2026-09-09, original invention, no external source document. Full "
    "narrative text at "
    "docs/lords-of-cian/chronicles/ijoko-chronicle-i-what-laughter-couldnt-move.md."
)

NEW_RULES = [
    {
        "id": "MCD-349",
        "category": "World Mechanics",
        "statement": (
            "Ijoko Chronicle I ('What Laughter Couldn't Move') is the "
            "first entry in Ijoko's own Chronicle series, per the "
            "established structure: each Phase 2 homage-era territory "
            "has its own Chronicles, with its own leader as protagonist "
            "and Kanja appearing only as an unnamed guest. Across "
            "repeated council sessions, hostile members test Adwoa "
            "(PH2-027) with deniable, sideways mockery meant to destabilize "
            "her. Adwoa's signature ability ('The Iron Hand in the "
            "Velvet Glove,' PH2-027) is shown directly in operation for "
            "the first time: every jab leaves her grip on the room "
            "visibly steadier rather than shaken, exactly matching the "
            "ability's stated mechanic. The same episode dramatizes the "
            "ability's stated cost precisely: the ability does nothing "
            "against the real, impersonal economic decline (a thinning "
            "tax base, capital flight) working against her, and the "
            "Chronicle states explicitly that this is a different fight "
            "entirely, one composure cannot touch, matching PH2-027's "
            "stated limitation rather than leaving it abstract. An "
            "unnamed Kanja is a recurring back-row presence across "
            "sessions without taking command, credit, or narrative "
            "authorship. No new named characters introduced. Slots into "
            "no existing mainline battle -- original homage-era material "
            "set in Ijoko itself, continuing Los Angeles's own run of "
            "territory Chronicles (Sankofa, Aztlan, and Atunbi already "
            "have one; only Orin still does not)."
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
            "batch": 86,
            "source_doc": (
                "Ijoko Chronicle I ('What Laughter Couldn't Move', "
                "MCD-349) -- the fifteenth territory Chronicle overall "
                "and Ijoko's first (Adwoa), continuing Los Angeles's own "
                "run of territory Chronicles."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "8.9"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
