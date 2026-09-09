#!/usr/bin/env python3
"""Batch 91: Nyansa Chronicle I ("The Word That Stuck"), the first
entry in Nyansa's own Chronicle series -- protagonist Adisa (PH2-057),
Kanja as unnamed guest. Continues Detroit's own run of territory
Chronicles."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Nyansa Chronicle I ('The Word That Stuck'), chat-drafted 2026-09-09, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/nyansa-chronicle-i-the-word-that-stuck.md."
)

NEW_RULES = [
    {
        "id": "MCD-354",
        "category": "World Mechanics",
        "statement": (
            "Nyansa Chronicle I ('The Word That Stuck') is the first "
            "entry in Nyansa's own Chronicle series, per the established "
            "structure: each Phase 2 homage-era territory has its own "
            "Chronicles, with its own leader as protagonist and Kanja "
            "appearing only as an unnamed guest. Adisa (PH2-057) names, "
            "aloud, his own organizing committee's unexamined exclusion "
            "of night-shift workers from its votes; the argument never "
            "returns to its old unresolved shape afterward, and the "
            "night shift wins its vote within the month. Adisa's "
            "signature ability ('The Long Correction,' PH2-057) is shown "
            "directly in operation for the first time, exactly matching "
            "its stated mechanic. The same episode dramatizes the "
            "ability's stated cost via a deliberate contrast case: Adisa "
            "tries the identical technique on a rival faction leader "
            "whose program has no latent doubt underneath it, and it "
            "fails completely, matching PH2-057's stated limitation "
            "('can't implant a belief that isn't already half-formed "
            "there'). Adisa's real co-theorist and life partner (homage "
            "to Grace Lee Boggs) remains backstory-only per PH2-057's own "
            "precedent and is not referenced on-page. The rival faction "
            "leader is deliberately left unnamed. An unnamed Kanja "
            "watches from the back of both meetings without taking "
            "command, credit, or narrative authorship. No new named "
            "characters introduced. Slots into no existing mainline "
            "battle -- original homage-era material set in Nyansa "
            "itself, continuing Detroit's own run of territory "
            "Chronicles (Kazi, Taifa, and Hekalu already have one; only "
            "Kiti still does not)."
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
            "batch": 91,
            "source_doc": (
                "Nyansa Chronicle I ('The Word That Stuck', MCD-354) -- "
                "the twentieth territory Chronicle overall and Nyansa's "
                "first (Adisa), continuing Detroit's own run of "
                "territory Chronicles."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "9.4"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
