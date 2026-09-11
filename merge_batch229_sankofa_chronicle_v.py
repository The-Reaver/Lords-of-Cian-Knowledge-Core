#!/usr/bin/env python3
"""Batch 229: Sankofa Chronicle V, "What Tradecraft Gave Away" -- the deepening "crack" entry."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-11, no source document. Full narrative text at "
    "docs/lords-of-cian/chronicles/sankofa-chronicle-v-what-tradecraft-gave-away.md."
)

BATCH_NOTE = (
    "Sankofa Chronicle V, \"What Tradecraft Gave Away\" -- the third Sankofa entry to touch the "
    "forged-letter/pamphlet conspiracy from Chronicles II and IV (MCD-360, MCD-1023), and the "
    "deliberate \"crack\" entry agreed to in Batch 225's pacing discussion: one deepening entry "
    "before any reveal, making the threat personal to Baale again at higher stakes than Chronicle "
    "I's face-to-face attack, forcing the conspiracy to risk real exposure. Combines two of the "
    "three options discussed then (an overreach that backfires, a defector with cold feet): a hired "
    "direct attacker (Yao, new named character, survives and is bound to Baale per \"The Turn\") is "
    "backed by a rooftop second operative who has cold feet and flees rather than firing. Yao's "
    "unwitting testimony about his own dead-drop recruitment reveals a distinctive letter-fold "
    "identical to the COINTELPRO-era forged letters from PH2-021's own backstory near-death event -- "
    "proof the current conspiracy is run by, or was taught by, someone from the original campaign "
    "never caught the first time. Deliberately does not reveal an author or name; the reveal is "
    "reserved for its own future entry. Kanja does not appear in this entry, a deliberate first for "
    "the sub-series. Collision-checked: Yao has zero prior hits anywhere in the ledger. Abad's "
    "approval, quoted verbatim: \"Approve as drafted, keep Kanja out.\""
)

NEW_RULES = [
    {
        "id": "MCD-1025",
        "category": "territory-chronicle",
        "statement": (
            "Sankofa Chronicle V, \"What Tradecraft Gave Away\" (full narrative text at "
            "docs/lords-of-cian/chronicles/sankofa-chronicle-v-what-tradecraft-gave-away.md), the "
            "fifth Sankofa territory Chronicle and the third to touch the forged-letter/pamphlet "
            "conspiracy from Chronicles II and IV (MCD-360, MCD-1023). Protagonist Baale (PH2-021), "
            "not a Kanja Chronicle. Per the pacing agreed in Batch 225: the deliberate 'crack' entry, "
            "escalating the conspiracy from information warfare to a direct assassination attempt -- "
            "its first real risk of exposure -- without resolving the mystery. A hired direct "
            "attacker, Yao (a new named character, Akan Thursday-born day-name per the standing PH2 "
            "naming convention, zero prior collisions), attacks Baale face to face at dusk; he "
            "survives the exchange and is bound to serve Baale per 'The Turn,' exactly matching the "
            "ability's mechanic. A second operative, positioned on a rooftop specifically to kill "
            "Baale by means that don't require him to survive a direct exchange (defeating the "
            "ability's own condition), has cold feet at the last second and flees without firing, "
            "left deliberately unidentified. Yao's unprompted account of his own dead-drop "
            "recruitment -- instructions folded in a distinctive three-corner tucked fold -- matches "
            "exactly the never-publicized fold used in the COINTELPRO-era forged letters from "
            "PH2-021's own backstory near-death event, proving the current conspiracy is run by, or "
            "was taught directly by, someone from the original campaign who was never caught the "
            "first time. Deliberately does not reveal an author or name; the reveal is reserved for "
            "a future entry, per Abad's explicit pacing instruction. Kra and Kojo (both already "
            "locked) reused; no other named characters. Kanja does not appear in this entry at all -- "
            "a deliberate departure from every prior Sankofa Chronicle, judged too private and "
            "personal a moment even for an unnamed witness."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 1, f"expected 1 new rule, got {len(NEW_RULES)}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 229,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-11, no source document",
            "rule_count": len(NEW_RULES),
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs found post-write!"

    print(
        f"OK. Total rules: {len(ledger['rules'])}. "
        f"Ledger version: {ledger['ledger_version']}. "
        f"Batches: {len(ledger['batches_completed'])}."
    )


if __name__ == "__main__":
    main()
