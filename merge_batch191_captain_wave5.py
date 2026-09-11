#!/usr/bin/env python3
"""Batch 191: Lock Captain's fifth three-entry Alias Chronicle wave (MCD-558 through MCD-560),
completing a fifth wave for all eleven aliases in this continuous run."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do a wave through all the aliases. do this continuously, uninterrupted, this includes '
    'rigorous testing, committing, and pushing to origin Main." Completes fifth waves for all '
    'eleven aliases (Bane, Trench Monarch, Industrial Myth, Blue-Collar Titan, Sovereign Ghost of '
    'the Great Sea, the Scourge, the Crow King, the Iron Bastard, the Lord of Embers, the Storm '
    'That Walks, and Captain).'
)

NEW_RULES = [
    {
        "id": "MCD-558",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Nine Days Nobody Slept\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-nine-days-nobody-slept.md), Captain Alias Chronicle "
            "XVI, first entry in the fifth wave. A detailed nine-day siege endurance showcase: "
            "Kanja deliberately declines to use his biological advantage for extra rest, moving "
            "constantly among the exhausted crew instead so nobody carries the grinding hardship "
            "believing themselves more alone in it than he is. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-559",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Enemy Who Asked to Stay\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-enemy-who-asked-to-stay.md), Captain Alias Chronicle "
            "XVII. A captured Directorate officer asks to join the crew rather than accept parole or "
            "custody; Kanja extends the same gradual, tested trust-building process given to any "
            "unproven newcomer rather than either blanket suspicion or immediate acceptance. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-560",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Efa Gol Saw From the Start\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-efa-gol-saw-from-the-start.md), Captain Alias "
            "Chronicle XVIII, closing the fifth wave. Efa Gol (already locked, present since "
            "Warehouse Twelve) offers a synthesizing reflection across every alias Kanja has "
            "carried, explaining why 'Captain' -- the name his own crew chose rather than one "
            "assigned by fear or classification -- means the most to the people who lived every day "
            "of the war alongside him. No new named characters beyond the already-locked Efa Gol. "
            "Closes Captain's fifth three-Chronicle wave (with 'The Nine Days Nobody Slept,' "
            "MCD-558, and 'The Enemy Who Asked to Stay,' MCD-559)."
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
            "batch": 191,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks Captain's fifth three-entry Alias Chronicle wave (MCD-558 through MCD-560), "
                "completing a fifth wave for all eleven aliases. " + BATCH_NOTE
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
