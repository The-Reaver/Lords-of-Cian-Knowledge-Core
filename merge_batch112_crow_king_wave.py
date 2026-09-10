#!/usr/bin/env python3
"""Batch 112: Lock the Crow King's three-entry Alias Chronicle wave (MCD-383 through MCD-385),
continuing uninterrupted through the remaining alias waves."""
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
        "id": "MCD-383",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Second Scarecrow\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-second-scarecrow.md), Crow King Alias Chronicle "
            "I. Rebellion era, months after the Night of the Crow King (MCD-236, age 23). A "
            "Korren Highlands checkpoint captain, having built his doctrine specifically to deny "
            "the marsh-and-drainage-channel trick, finds the same coat-and-feather-crown "
            "scarecrow at his own open-sightline command post: the compound emptied not through "
            "concealment but through timing precise enough to move only within the checkpoint's "
            "own ninety-second patrol gap. Establishes the alias's underlying principle -- "
            "exploiting a pursuer's own procedural predictability, not terrain -- distinct from "
            "the original Hymn-Engine trick. No new named characters. First entry in the Crow "
            "King's three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-384",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"Three Hundred Voices, One Lie\" (full narrative text at "
            "docs/lords-of-cian/chronicles/three-hundred-voices-one-lie.md), Crow King Alias "
            "Chronicle II. Rebellion era, a new deployment of the Hymn-Engine (MCD-236) against a "
            "purpose-built triple-redundant thermal sensor grid designed specifically to prevent "
            "a single coordinated false signal. Three hundred voices sing three interleaved false "
            "patterns at once ('the Braid'), each sub-group falsifying exactly one of the three "
            "arrays while leaving the other two reading true from that position, so the "
            "redundant systems cross-confirm three fabricated truths instead of exposing one lie. "
            "The Coalfell compound empties over four hours undetected. No new named characters. "
            "Second entry in the Crow King's three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-385",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Commandant Voris Kept\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-commandant-voris-kept.md), Crow King Alias "
            "Chronicle III, closing the wave. Years after the Night of the Crow King, from "
            "Commandant Voris's own perspective (already locked, MCD-236). Voris has kept the "
            "original scarecrow against regulation, treating it as the only honest teacher of "
            "his career; he explains to a young inquiry officer that the Crow King's actual gift "
            "is finding the seam where a system's confidence in its own procedures becomes a "
            "blind spot, and that no defense exists short of an unpredictability no army has ever "
            "been willing to afford. Ties together both prior Chronicles' events into Voris's own "
            "retrospective understanding. No new named characters beyond the already-locked "
            "Commandant Voris. Closes the Crow King's three-Chronicle wave (with 'The Second "
            "Scarecrow,' MCD-383, and 'Three Hundred Voices, One Lie,' MCD-384)."
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
            "batch": 112,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Crow King's three-entry Alias Chronicle wave (MCD-383 through "
                "MCD-385), the sixth of ten remaining alias waves. " + BATCH_NOTE
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
