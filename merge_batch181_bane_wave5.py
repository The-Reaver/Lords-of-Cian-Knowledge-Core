#!/usr/bin/env python3
"""Batch 181: Lock Bane's fifth three-entry Alias Chronicle wave (MCD-528 through MCD-530)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = 'Abad: "lock it."'

NEW_RULES = [
    {
        "id": "MCD-528",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Boy Who Wanted to Be Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-boy-who-wanted-to-be-him.md), Bane Alias Chronicle "
            "XIII, first entry in the fifth wave. A young recruit, having absorbed only the fear "
            "from the Bane stories and none of the restraint, nearly kills a surrendering "
            "Directorate scout believing the reputation licenses it; Kanja stops him and states "
            "plainly that the reputation exists to prevent killing, not enable it -- the clearest "
            "statement yet of 'the fear only works if it's true' (MCD-431). No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-529",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Siege That Took Nine Days\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-siege-that-took-nine-days.md), Bane Alias Chronicle "
            "XIV. A detailed, sustained multi-day combat showcase against the fortified Threshbend "
            "depot: eight days of invisible psychological pressure (disappearing guard posts, no "
            "visible attack) break the garrison's morale before a decisive ninth-day strike -- the "
            "first sustained siege-length engagement in the Bane Chronicle series, extending the "
            "alias's patience-over-speed principle. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-530",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Danne Sok Never Told Anyone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-danne-sok-never-told-anyone.md), Bane Alias "
            "Chronicle XV, closing the fifth wave. Danne Sok (already locked, one of the three "
            "earliest crew members freed before the Black Trench) finally shares a memory kept "
            "private the whole war: the young Kanja's hands shaking for an hour after freeing him, "
            "before any alias existed -- a private counterweight to the legend, extending the "
            "'tired, not scary' theme (MCD-478) back to its literal origin. No new named characters "
            "beyond the already-locked Danne Sok. Closes Bane's fifth three-Chronicle wave (with "
            "'The Boy Who Wanted to Be Him,' MCD-528, and 'The Siege That Took Nine Days,' "
            "MCD-529)."
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
            "batch": 181,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks Bane's fifth three-entry Alias Chronicle wave (MCD-528 through MCD-530), "
                "the first alias wave five. " + BATCH_NOTE
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
