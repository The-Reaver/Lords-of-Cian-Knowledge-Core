#!/usr/bin/env python3
"""Batch 105: VB-061, the blue-collar register quotes catalog -- five quotes attributed to
labor-adjacent aliases, extending VB-060's presence-doctrine framing without repeating it."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-10, no source document."

BATCH_NOTE = 'Abad: "lock it."'

NEW_RULES = [
    {
        "id": "VB-061",
        "category": "voice-bible-quotes",
        "statement": (
            "A standing catalog of quotes attributed to Kanja's labor-adjacent aliases, in a "
            "blue-collar register distinct from VB-060's presence-doctrine framing -- extends but "
            "does not repeat it. The Trench Monarch (age 18, his first alias): 'Every king I ever "
            "heard of inherited his crown. Mine's mud and iron, and I dug it up myself.' The "
            "Industrial Myth (age 19, Furnace District Strike, MCD-244): 'A myth doesn't clock in. "
            "I do. That's the difference between a story and a man you can find on the floor when "
            "the whistle blows.' The Blue-Collar Titan (age 20, Sewer War of Killane, MCD-234): "
            "'They keep calling it a title, like it's something I put on. It isn't. It's just what "
            "happens when you never stop being the man who worked for a living, and the work got "
            "bigger than anyone planned for.' The Lord of Embers (age 27, the Rolling Foundry "
            "Campaign, MCD-241): 'You want to burn a workingman's home down, go ahead. Just know "
            "somebody's going to be standing in the ashes with a hammer before your smoke clears -- "
            "and that somebody's going to be me.' Captain (never a Directorate classification, his "
            "own crew's name for him): 'The Directorate names what scares them. We named the man "
            "who feeds the crew before he feeds himself. That name's ours. They don't get to touch "
            "it' -- attributed to the crew collectively rather than to Kanja himself, matching the "
            "already-locked distinction that 'Captain' is affectionate and self-given, not an "
            "institutional threat-classification."
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
            "batch": 105,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks VB-061, the blue-collar register quotes catalog: five new quotes "
                "attributed to the Trench Monarch, the Industrial Myth, the Blue-Collar Titan, "
                "the Lord of Embers, and Captain -- each grounded in that alias's already-locked "
                "origin event, extending VB-060's presence-doctrine framing without repeating "
                "it. " + BATCH_NOTE
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
