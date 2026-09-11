#!/usr/bin/env python3
"""Batch 127: Lock the Captain's second three-entry Alias Chronicle wave (MCD-428 through
MCD-430), completing the eleventh and final second wave in this continuous run."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "complete all of the Alias drafts continuously uninterrupted" -- completes second '
    'waves for all eleven aliases (Bane, Trench Monarch, Industrial Myth, Blue-Collar Titan, '
    'Sovereign Ghost of the Great Sea, the Scourge, the Crow King, the Iron Bastard, the Lord of '
    'Embers, the Storm That Walks, and Captain).'
)

NEW_RULES = [
    {
        "id": "MCD-428",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Day Captain Could Not Save Everyone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-day-captain-could-not-save-everyone.md), Captain "
            "Alias Chronicle IV, first entry in the second wave. Three crew deaths in a structural "
            "collapse neither skill nor doctrine could have prevented test the crew's trust in the "
            "name for the first time; Callum Breck (already locked) tells him plainly that the "
            "crew doesn't call him Captain because he's perfect, but because he's the one who sits "
            "with the casualty report instead of looking away from it. No new named characters "
            "beyond the already-locked Callum Breck and referenced Garren Hask."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-429",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Charge He Spent on One Person\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-charge-he-spent-on-one-person.md), Captain Alias "
            "Chronicle V. Pell Ostra (already locked, CC-132/CC-133) is pinned beneath a support "
            "beam when a structure collapses six minutes ahead of her own timeline; Kanja "
            "demonstrates Mafesto's Kinetic Transfer System reading the collapse non-visually and "
            "Obsidian Malice clearing a path through rubble, rescuing her twelve seconds before "
            "total collapse -- the Trinity's full resources spent on a single crew member rather "
            "than a battle, the most personal scale yet for the Captain's crew-protective register."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-430",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Last Thing the Old Hand Said\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-last-thing-the-old-hand-said.md), Captain Alias "
            "Chronicle VI, closing the second wave. A founding dockhand, present since before Pier "
            "Nine had a name for any of it, formally retires when his hands finally give out; he "
            "tells Kanja that what mattered across every alias he'd carried (Trench Monarch, "
            "Captain) was never the word itself but that each was honestly earned in front of "
            "people watching closely enough to know the difference. A quiet, undramatic ending "
            "rather than a battle. No new named characters. Closes the Captain's second three-"
            "Chronicle wave (with 'The Day Captain Could Not Save Everyone,' MCD-428, and 'The "
            "Charge He Spent on One Person,' MCD-429) and completes second waves for all eleven "
            "aliases."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collisions with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 127,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Captain's second three-entry Alias Chronicle wave (MCD-428 through "
                "MCD-430), the eleventh and final second wave in this continuous run. Every named "
                "alias now has two completed three-Chronicle waves (six entries each). "
                + BATCH_NOTE
            ),
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate IDs after merge"
    print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
          f"Batches: {len(ledger['batches_completed'])}.")


if __name__ == "__main__":
    main()
