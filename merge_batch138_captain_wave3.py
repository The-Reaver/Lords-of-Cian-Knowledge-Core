#!/usr/bin/env python3
"""Batch 138: Lock Captain's third three-entry Alias Chronicle wave (MCD-461 through MCD-463),
completing a third wave for all eleven aliases in this continuous run."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "#1 and #2 now and continue uninterrupted until completion this includes test, commit, '
    'push to main origin" -- completes third waves for all eleven aliases (Bane, Trench Monarch, '
    'Industrial Myth, Blue-Collar Titan, Sovereign Ghost of the Great Sea, the Scourge, the Crow '
    'King, the Iron Bastard, the Lord of Embers, the Storm That Walks, and Captain).'
)

NEW_RULES = [
    {
        "id": "MCD-461",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Day the Whole Crew Fought as One\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-day-the-whole-crew-fought-as-one.md), Captain Alias "
            "Chronicle VII, first entry in the third wave. A detailed combat showcase built around "
            "coordinated command rather than solo heroics: Kanja maps a Directorate strongpoint and "
            "directs Efa Gol's decoy force, Pell Ostra's demolition team, and Callum Breck's "
            "assault element (all already locked) through a three-vector plan, his own Trinity held "
            "mostly in reserve. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-462",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The New Hand's First Night\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-new-hands-first-night.md), Captain Alias Chronicle "
            "VIII. A late-joining recruit learns from Callum Breck (already locked) the difference "
            "between the crew's old and new names for Kanja and uses 'Captain' for the first time, "
            "showing how the alias's culture propagates to new arrivals rather than being held only "
            "by veterans. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-463",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Crew Toasted To\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-crew-toasted-to.md), Captain Alias Chronicle "
            "IX, closing the third wave. An informal crew toast tradition gathers Corren Halst, "
            "Pell Ostra, Garren Hask, and Efa Gol (all already locked), each invoking an "
            "already-locked alias-era phrase, closing not only Captain's third wave but the full "
            "eleven-alias third-wave run with a warm, collective scene. No new named characters. "
            "Closes Captain's third three-Chronicle wave (with 'The Day the Whole Crew Fought as "
            "One,' MCD-461, and 'The New Hand's First Night,' MCD-462)."
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
            "batch": 138,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks Captain's third three-entry Alias Chronicle wave (MCD-461 through MCD-463), "
                "completing a third wave for all eleven aliases. " + BATCH_NOTE
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
