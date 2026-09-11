#!/usr/bin/env python3
"""Batch 117: Lock Bane's second three-entry Alias Chronicle wave (MCD-398 through MCD-400),
under Abad's instruction to complete all Alias drafts continuously uninterrupted."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "complete all of the Alias drafts continuously uninterrupted" (starting a second '
    'wave for every alias, beginning with Bane).'
)

NEW_RULES = [
    {
        "id": "MCD-398",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Fog Remembers\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-fog-remembers.md), Bane Alias Chronicle IV, "
            "first entry in Bane's second three-Chronicle wave. Rebellion era, a new engagement "
            "in terrain deliberately mirroring the Black Trench's chemical fog and confined "
            "ground (MCD-232), staged by a detachment testing whether forcing those exact "
            "conditions without Kanja's own choice reverses the advantage. Demonstrates Mafesto's "
            "non-visual Kinetic Transfer System reading impact through plating rather than sight, "
            "Obsidian Malice's precisely sound-targeted discharge, and Onyx's Whisper of Shadows "
            "and Cadence Ruin unmaking a six-week-rehearsed ambush in eleven minutes -- the "
            "detachment commander concludes they copied the conditions without understanding why "
            "they worked: 'he doesn't need his eyes to know where you are.' No new named "
            "characters. First armor-and-weapon showcase specifically under the Bane alias."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-399",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Agent Who Stopped Filing Reports\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-agent-who-stopped-filing-reports.md), Bane Alias "
            "Chronicle V. Rebellion era, a Directorate agent embedded six months among Kanja's own "
            "recruited dockworkers files useful weekly intelligence until witnessing him carry an "
            "injured recruit two miles rather than wait for a cart; three attempts to write an "
            "honest threat assessment collapse into a two-line request for reassignment -- the "
            "only genuinely honest report in the agent's file, and the only one that later proves "
            "correct. No new named characters; the agent and handler are unnamed and one-scene. "
            "Second entry in Bane's second three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-400",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The File That Would Not Close\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-file-that-would-not-close.md), Bane Alias "
            "Chronicle VI, closing Bane's second three-Chronicle wave. Rebellion era, a "
            "documentary-register account of the Directorate's own difficulty formally "
            "classifying the alias, dramatizing the origin of MCD-232's own locked classification "
            "language ('a threat that destroys the force built to destroy it') as an admission "
            "that no standard threat taxonomy fit him, not a confident label -- his pattern being "
            "the total absence of a consistent operational signature. No new named characters; the "
            "analyst is unnamed and one-scene. Closes Bane's second three-Chronicle wave (with "
            "'What the Fog Remembers,' MCD-398, and 'The Agent Who Stopped Filing Reports,' "
            "MCD-399)."
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
            "batch": 117,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks Bane's second three-entry Alias Chronicle wave (MCD-398 through MCD-400), "
                "the first of eleven second waves in a continuous run. " + BATCH_NOTE
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
