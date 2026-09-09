#!/usr/bin/env python3
"""Batch 89: Taifa Chronicle I ("Bound Without a Word"), the first entry
in Taifa's own Chronicle series -- protagonist Osei (PH2-053), Kanja as
unnamed guest. Continues Detroit's own run of territory Chronicles."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Taifa Chronicle I ('Bound Without a Word'), chat-drafted 2026-09-09, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/taifa-chronicle-i-bound-without-a-word.md."
)

NEW_RULES = [
    {
        "id": "MCD-352",
        "category": "World Mechanics",
        "statement": (
            "Taifa Chronicle I ('Bound Without a Word') is the first "
            "entry in Taifa's own Chronicle series, per the established "
            "structure: each Phase 2 homage-era territory has its own "
            "Chronicles, with its own leader as protagonist and Kanja "
            "appearing only as an unnamed guest. When a dawn raid hits "
            "the claimed land's outer post faster than any rider could "
            "warn the other sworn cells, Osei (PH2-053) feels the need "
            "arrive whole, and sworn hands converge from three "
            "unconnected cities within minutes of each other. Osei's "
            "signature ability ('Kin at a Distance,' PH2-053) is shown "
            "directly in operation for the first time, exactly matching "
            "its stated mechanic. The ability's cost is dramatized "
            "explicitly: Osei states plainly that people who merely "
            "agree with or admire the cause, without having sworn the "
            "oath and meant it, feel nothing and are never reached, "
            "matching PH2-053's stated limitation ('cannot compel anyone "
            "who hasn't sworn it'). Yaw (PH2-053) is referenced "
            "consistently with his already-locked co-founder role, not "
            "separately detailed. The RNA's real exiled first president "
            "remains backstory-only per PH2-053's own precedent. An "
            "unnamed Kanja watches from the post's edge without taking "
            "command, credit, or narrative authorship. No new named "
            "characters introduced. Slots into no existing mainline "
            "battle -- original homage-era material set in Taifa itself, "
            "continuing Detroit's own run of territory Chronicles (Kazi "
            "already has one; Hekalu, Nyansa, and Kiti still do not)."
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
            "batch": 89,
            "source_doc": (
                "Taifa Chronicle I ('Bound Without a Word', MCD-352) -- "
                "the eighteenth territory Chronicle overall and Taifa's "
                "first (Osei), continuing Detroit's own run of territory "
                "Chronicles."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "9.2"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
