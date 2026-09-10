#!/usr/bin/env python3
"""Batch 115: Lock the Storm That Walks' three-entry Alias Chronicle wave (MCD-392 through
MCD-394), continuing uninterrupted through the remaining alias waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-10, no source document."

BATCH_NOTE = (
    'Abad: "continue uninterrupted until completion this includes test, commit, push to main '
    'origin" (covering all ten remaining alias waves).'
)

NEW_RULES = [
    {
        "id": "MCD-392",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Second Envelopment\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-second-envelopment.md), Storm That Walks Alias "
            "Chronicle I. Rebellion era, weeks after the Battle of the Gale Straits (MCD-242, age "
            "29). Admiral Krael's replacement builds a dispersed-squadron doctrine specifically "
            "to deny a single-line envelopment; the 22-ship arrowhead instead runs the seam "
            "between two dispersed squadrons, provoking the same friendly-fire confusion in "
            "miniature. The replacement admiral's report concludes the vulnerability isn't a "
            "formation problem but a trust problem between allied commands. Sephtis's already-"
            "locked storm-prediction role is referenced, not restaged. No new named characters. "
            "First entry in the Storm That Walks' three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-393",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Flagship That Would Not Flood\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-flagship-that-would-not-flood.md), Storm That "
            "Walks Alias Chronicle II. Rebellion era, a new Gale Straits corridor engagement. "
            "Kanja boards Krael's replacement's own flagship -- built with reinforced bulkheads "
            "and triple bilge pumps specifically to survive flooding -- directly rather than "
            "trying to sink her, demonstrating Mafesto's Kinetic Transfer System powering the "
            "boarding leap, Obsidian Malice jamming a hatch to seal the marine reserve belowdecks "
            "instead of breaching the hull, Onyx's Whisper of Shadows using storm conditions as "
            "cover, and Soulbound Edge deciding a duel with the admiral by fractions of committed "
            "intent. The flagship never takes on water and surrenders anyway. No new named "
            "characters. Second entry in the Storm That Walks' three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-394",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Admiral Krael Told His Successor\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-admiral-krael-told-his-successor.md), Storm That "
            "Walks Alias Chronicle III, closing the wave. Shortly after the Battle of the Gale "
            "Straits, Admiral Dessius Krael (already locked, 'the Gale Straits admiral') gives "
            "his successor a final briefing before resigning: Kanja's advantage isn't "
            "intelligence but patience with visible uncertainty in front of his own crew, a trust "
            "built on honesty rather than a commander never appearing wrong -- a trait Krael "
            "concludes he is too old to unlearn himself. Deliberately distinct in register from "
            "the Crow King wave's Commandant Voris entry (a kept trophy): dignified acceptance and "
            "a direct handoff rather than private obsession. No new named characters beyond "
            "Krael. Closes the Storm That Walks' three-Chronicle wave (with 'The Second "
            "Envelopment,' MCD-392, and 'The Flagship That Would Not Flood,' MCD-393)."
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
            "batch": 115,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Storm That Walks' three-entry Alias Chronicle wave (MCD-392 through "
                "MCD-394), the ninth of ten remaining alias waves. " + BATCH_NOTE
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
