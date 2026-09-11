#!/usr/bin/env python3
"""Batch 131: Lock the Blue-Collar Titan's third three-entry Alias Chronicle wave (MCD-440 through
MCD-442), continuing uninterrupted per Abad's "#1 and #2 now" authorization."""
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
        "id": "MCD-440",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Flood That Came From Below\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-flood-that-came-from-below.md), the Blue-Collar "
            "Titan Alias Chronicle VII, first entry in the third wave. A detailed flooding-tunnel "
            "Trinity showcase: Mafesto's Kinetic Transfer System reading pressure and current "
            "non-visually, Obsidian Malice breaching a jammed drainage gate in one discharge to "
            "drain a gallery flooding forty trapped workers, and Onyx of Oblivion's Whisper of "
            "Shadows/Veil Piercer/Cadence Ruin disarming six Directorate engineers sent to ensure "
            "nothing trapped below survived. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-441",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Two Gangs Under Killane\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-two-gangs-under-killane.md), the Blue-Collar Titan "
            "Alias Chronicle VIII. Kanja mediates a sixty-year-old rivalry between two tunnel crews "
            "that has cost lives through refused structural-safety information-sharing, convincing "
            "both sides to trade reports through him as intermediary until direct trust builds -- "
            "the grudge itself left unresolved, only the safety practice fixed. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-442",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Old Digger Taught Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-old-digger-taught-him.md), the Blue-Collar "
            "Titan Alias Chronicle IX, closing the third wave. An elderly Killane tunnel digger "
            "teaches Kanja decades of tactile, non-equipment tunnel knowledge his gear cannot "
            "replicate, extending the alias's non-visual sensory principle with a human source that "
            "outlasts the war and carries into later aliases. No new named characters. Closes the "
            "Blue-Collar Titan's third three-Chronicle wave (with 'The Flood That Came From Below,' "
            "MCD-440, and 'The Two Gangs Under Killane,' MCD-441)."
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
            "batch": 131,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Blue-Collar Titan's third three-entry Alias Chronicle wave (MCD-440 "
                "through MCD-442). " + BATCH_NOTE
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
