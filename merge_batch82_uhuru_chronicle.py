#!/usr/bin/env python3
"""Batch 82: Uhuru Chronicle I ("The Patience That Cost Him"), the first
entry in Uhuru's own Chronicle series -- protagonist Ofin (PH2-044),
Kanja as unnamed guest, matching the established territory-Chronicle
convention (MCD-334/335/336/339/340/341/342/343/344). Completes a first
Chronicle entry for all five Chicago territories."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Uhuru Chronicle I ('The Patience That Cost Him'), chat-drafted "
    "2026-09-09, original invention, no external source document. Full "
    "narrative text at "
    "docs/lords-of-cian/chronicles/uhuru-chronicle-i-the-patience-that-cost-him.md."
)

NEW_RULES = [
    {
        "id": "MCD-345",
        "category": "World Mechanics",
        "statement": (
            "Uhuru Chronicle I ('The Patience That Cost Him') is the first "
            "entry in Uhuru's own Chronicle series, per the established "
            "structure (MCD-334/335/336/339/340/341/342/343/344): each "
            "Phase 2 homage-era territory has its own Chronicles, with its "
            "own leader as protagonist and Kanja appearing only as an "
            "unnamed guest. Ofin (PH2-044), blocked by a hostile council "
            "bloc's repeated defeat of the fair-housing review board's "
            "funding (the same board Kwan Chronicle I's ward broker once "
            "staked one public sentence on, MCD-343), refuses to stop "
            "resubmitting it across dozens of votes. Ofin's signature "
            "ability ('The Override,' PH2-044) is shown directly in "
            "operation for the first time: the specific obstruction "
            "breaks completely and permanently once a court-ordered "
            "redistricting finally shifts the council's composition, "
            "exactly matching the ability's stated mechanic. The "
            "ability's cost is honored explicitly without resolving into "
            "the character's already-locked capstone death: the same "
            "engine wearing the obstruction down is shown visibly wearing "
            "Ofin down in turn (reduced sleep, a physician his wife wants "
            "him to see, looking older than his years), left as "
            "foreshadowing per PH2-044's own stated 'foreshadowed limit "
            "to how long he can keep paying for it' rather than paid off "
            "here -- his 1987 death at his own desk remains the "
            "deliberate, as-built capstone cost for a future entry. This "
            "Chronicle also closes the continuity thread opened in Kwan "
            "Chronicle I: the fair-housing agreement left there as 'a "
            "victory of uncertain real weight' is confirmed here, years "
            "later, as genuinely made real through Ofin's endurance "
            "rather than Kasa's original legitimacy-granting act, "
            "honoring both leaders' distinct signature abilities without "
            "either doing the other's work. An unnamed Kanja is present "
            "in City Hall's late-hour orbit across several nights without "
            "taking command, credit, or narrative authorship. No new "
            "named characters introduced. Slots into no existing "
            "mainline battle -- original homage-era material set in "
            "Uhuru itself, and completes a first Chronicle entry for "
            "every one of Chicago's five territories (Ide, Kwan, Umoja, "
            "Jibaro, Uhuru), matching NYC's own completed set."
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
            "batch": 82,
            "source_doc": (
                "Uhuru Chronicle I ('The Patience That Cost Him', "
                "MCD-345) -- the eleventh territory Chronicle overall and "
                "Uhuru's first (Ofin), completing a first Chronicle entry "
                "for all five Chicago territories, continuing the "
                "open-ended Phase 2 territory-Chronicle expansion "
                "(alongside Xaragua I/II, Umoja I, Yara I, Areito I, "
                "Guanin I, Boriken I, Ide I, Kwan I, Jibaro I) that was "
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

    ledger["ledger_version"] = "8.5"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
