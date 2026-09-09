#!/usr/bin/env python3
"""Batch 97: Sankofa Chronicle II, "What His Gift Could Not Reach" (MCD-360)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-09, no source document. Second entry in Sankofa's "
    "own Chronicles, dramatizing PH2-021's own stated vulnerability, left as live unresolved "
    "tension at the close of Sankofa Chronicle I (MCD-346). Full narrative text at "
    "docs/lords-of-cian/chronicles/sankofa-chronicle-ii-what-his-gift-could-not-reach.md."
)

NEW_RULES = [
    {
        "id": "MCD-360",
        "category": "phase2-homage-chronicle",
        "statement": (
            "Sankofa Chronicle II, \"What His Gift Could Not Reach\" (full narrative text at "
            "docs/lords-of-cian/chronicles/sankofa-chronicle-ii-what-his-gift-could-not-reach.md), "
            "the second entry in Sankofa's own Chronicles, protagonist Baale (PH2-021), not a Kanja "
            "Chronicle -- Kanja appears only as an unnamed guest, present across the night and the "
            "one who finds and delivers a second forged letter, without taking command, credit, or "
            "resolution authorship, and explicitly not identifying or investigating the letters' "
            "author. Dramatizes PH2-021's own stated vulnerability directly for the first time: a "
            "forged letter, shaped in the same manner as the real COINTELPRO-style letters behind "
            "Baale's already-locked backstory near-death event (kept backstory-only, not restaged "
            "here), reaches Kojo (introduced in Sankofa Chronicle I, MCD-346, left open as a minor "
            "recurring figure) claiming falsely to carry Baale's own hand and threatening Kojo's "
            "old crew. Kojo brings it directly to Baale rather than acting on it, resolving this "
            "instance of the threat through an ordinary act of trust rather than 'The Turn' itself, "
            "which requires a direct face-to-face attack and is confirmed explicitly useless "
            "against a conspiracy that never shows its face. A second, unsigned, unaddressed letter "
            "left to be found confirms the threat is not finished. The letters' true author is "
            "deliberately left unidentified and the threat deliberately left unresolved, consistent "
            "with PH2-021's own framing. No new named characters; no new proper nouns requiring a "
            "collision check. Sixth territory (after Xaragua, Areito, Guanin, Uhuru, and Aztlan) to "
            "receive a second Chronicle entry."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "lock it."'


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
            "batch": 97,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-09, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "Sankofa Chronicle II (MCD-360), 'What His Gift Could Not Reach' -- dramatizes "
                "PH2-021's own stated vulnerability, a faceless coordinated threat Baale's gift "
                "cannot reach, deliberately leaving the threat unresolved. " + BATCH_NOTE
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
