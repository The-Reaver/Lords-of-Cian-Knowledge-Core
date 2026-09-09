#!/usr/bin/env python3
"""Batch 81: Jibaro Chronicle I ("What the Walls Refused"), the first
entry in Jibaro's own Chronicle series -- protagonist Omoba (PH2-042),
Kanja as unnamed guest, matching the established territory-Chronicle
convention (MCD-334/335/336/339/340/341/342/343). Continues Chicago's own
run of territory Chronicles."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Jibaro Chronicle I ('What the Walls Refused'), chat-drafted 2026-09-09, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/jibaro-chronicle-i-what-the-walls-refused.md."
)

NEW_RULES = [
    {
        "id": "MCD-344",
        "category": "World Mechanics",
        "statement": (
            "Jibaro Chronicle I ('What the Walls Refused') is the first "
            "entry in Jibaro's own Chronicle series, per the established "
            "structure (MCD-334/335/336/339/340/341/342/343): each Phase "
            "2 homage-era territory has its own Chronicles, with its own "
            "leader as protagonist and Kanja appearing only as an unnamed "
            "guest. Omoba (PH2-042) and his people occupy a seminary "
            "building past the one-day threshold; when the diocese sends "
            "men to force them out by violence, the door itself refuses "
            "to yield. Omoba's signature ability ('The Occupation,' "
            "PH2-042) is shown directly in operation for the first time, "
            "dramatizing both its mechanic and its stated cost in the "
            "same episode: the seminary, an institution Omoba can shame "
            "into complicity, becomes permanently unreclaimable by force; "
            "an adjoining half-acre lot, never actually held a full day "
            "and belonging to no institution with anything to be ashamed "
            "of, is retaken within the hour with no resistance at all, "
            "matching PH2-042's stated limitation ('doesn't work on open "
            "ground or purely private property') precisely rather than "
            "leaving it abstract. An unnamed Kanja is embedded in the "
            "occupation from early in the week, doing ordinary logistics "
            "(carrying donated bread), without taking command, credit, or "
            "narrative authorship of the outcome. No new named characters "
            "introduced. Slots into no existing mainline battle -- "
            "original homage-era material set in Jibaro itself, "
            "continuing Chicago's own run of territory Chronicles (Umoja, "
            "Ide, and Kwan already have one; only Uhuru remains)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "lock it"'


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
            "batch": 81,
            "source_doc": (
                "Jibaro Chronicle I ('What the Walls Refused', MCD-344) -- "
                "the tenth territory Chronicle overall and Jibaro's first "
                "(Omoba), continuing Chicago's own run of territory "
                "Chronicles and the open-ended Phase 2 territory-Chronicle "
                "expansion (alongside Xaragua I/II, Umoja I, Yara I, "
                "Areito I, Guanin I, Boriken I, Ide I, Kwan I) that was "
                "never gated by the Pre-Book-1 Foundation Complete "
                "milestone (Batch 75)."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "8.4"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
