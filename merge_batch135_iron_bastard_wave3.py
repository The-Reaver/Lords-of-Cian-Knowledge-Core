#!/usr/bin/env python3
"""Batch 135: Lock the Iron Bastard's third three-entry Alias Chronicle wave (MCD-452 through
MCD-454), continuing uninterrupted per Abad's "#1 and #2 now" authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "#1 and #2 now and continue uninterrupted until completion this includes test, commit, '
    'push to main origin."'
)

NEW_RULES = [
    {
        "id": "MCD-452",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Bridge That Chose Its Moment\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-bridge-that-chose-its-moment.md), the Iron Bastard "
            "Alias Chronicle VII, first entry in the third wave. Holding a bridge alone as rear "
            "guard for a retreating column, Kanja lets a pursuing cavalry force fully commit onto "
            "the span before diagnostically listening to its structural tension and collapsing it "
            "from the pursued end with a single precisely timed Obsidian Malice discharge -- a "
            "timing-precision rescue/combat hybrid distinct from prior Iron Bastard entries. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-453",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Wall That Wasn't Built to Ring\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-wall-that-wasnt-built-to-ring.md), the Iron Bastard "
            "Alias Chronicle VIII. A Directorate engineer builds a packed-earth/loose-rubble berm "
            "with no tension-bearing structure for the Aegis-Talisman resonance doctrine to read, "
            "establishing a genuine, permanent category-limit of the doctrine; Kanja falls back on "
            "conventional siegecraft (sapper tunneling) rather than a resonance workaround, "
            "explicitly conceding the doctrine's real boundary. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-454",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The General Who Stopped Fighting Fair\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-general-who-stopped-fighting-fair.md), the Iron "
            "Bastard Alias Chronicle IX, closing the third wave. A Directorate general, having lost "
            "four consecutive engagements across the doctrine's full run (the original Stand, the "
            "Crawler variant, the bridge, and the berm), resigns field command and files the most "
            "honest opposing assessment of the doctrine yet produced, explicitly crediting its "
            "adaptability rather than framing his retirement as Kanja's personal defeat. No new "
            "named characters. Closes the Iron Bastard's third three-Chronicle wave (with 'The "
            "Bridge That Chose Its Moment,' MCD-452, and 'The Wall That Wasn't Built to Ring,' "
            "MCD-453)."
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
            "batch": 135,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Iron Bastard's third three-entry Alias Chronicle wave (MCD-452 through "
                "MCD-454). " + BATCH_NOTE
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
