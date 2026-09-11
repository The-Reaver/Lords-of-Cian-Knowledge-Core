#!/usr/bin/env python3
"""Batch 252: Sankofa Chronicle VI, "The Hand That Wrote the First Letter" -- the reveal."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-11, no source document. Full narrative text at "
    "docs/lords-of-cian/chronicles/sankofa-chronicle-vi-the-hand-that-wrote-the-first-letter.md."
)

BATCH_NOTE = (
    "Sankofa Chronicle VI, \"The Hand That Wrote the First Letter\" -- the reveal entry, closing the "
    "forged-letter/pamphlet conspiracy arc opened in Chronicle II (MCD-360) and deepened in Chronicles "
    "IV and V (MCD-1023/MCD-1025), per the pacing agreed in Batch 225: the reveal should tie the "
    "author to someone from the COINTELPRO-era backstory conspiracy who was never caught the first "
    "time. Names the author: Babatunde (new named character, Yoruba, zero prior collisions), a "
    "founding-era courier from Sankofa's earliest days who was coerced into working for an unnamed "
    "counterintelligence operation and personally forged the original letters from PH2-021's own "
    "backstory near-death event. His decades of continued operation are framed as a self-perpetuated, "
    "never-formally-closed assignment rather than an ongoing institutional program, keeping the "
    "apparatus itself unnamed even in resolution. Babatunde does not attack Baale at the reveal, so "
    "\"The Turn\" is never triggered -- deliberately honoring PH2-021's own stated limitation to the "
    "end: the ability has nothing to offer against a threat that simply stops rather than strikes. "
    "Resolution is exposure and public naming, not violence or captivity. Kra, Kojo, and Yao reused; "
    "Kanja does not appear, matching Chronicle V's precedent. Abad's approval: \"lock it.\""
)

NEW_RULES = [
    {
        "id": "MCD-1092",
        "category": "territory-chronicle",
        "statement": (
            "Sankofa Chronicle VI, \"The Hand That Wrote the First Letter\" (full narrative text at "
            "docs/lords-of-cian/chronicles/sankofa-chronicle-vi-the-hand-that-wrote-the-first-letter.md), "
            "the sixth Sankofa territory Chronicle and the reveal to the forged-letter/pamphlet "
            "conspiracy from Chronicles II, IV, and V (MCD-360/MCD-1023/MCD-1025). Protagonist Baale "
            "(PH2-021), not a Kanja Chronicle. Over roughly a year, Yao (bound via \"The Turn\" in "
            "Chronicle V) traces the dead-drop payment chain backward through its cutouts to a lease "
            "record naming the conspiracy's author: Babatunde (a new named character, Yoruba, zero "
            "prior collisions), a founding-era errand-runner/courier from Sankofa's earliest days -- "
            "recognized by Baale personally. Babatunde confesses to personally forging the original "
            "COINTELPRO-era letters that nearly killed Baale and Kra (PH2-021's backstory event) after "
            "being coerced by an unnamed counterintelligence operation; his decades of continued "
            "escalation (the private letter, the public pamphlets, the hired assassination attempt) are "
            "explained as a self-perpetuated, never-formally-closed assignment rather than an ongoing "
            "institutional program -- the apparatus itself is deliberately left unnamed even in "
            "resolution. Babatunde does not attack Baale at the confrontation, so \"The Turn\" is never "
            "triggered, honoring PH2-021's own stated mechanic precisely to the end: the ability has "
            "nothing to offer against a threat that simply stops rather than strikes. Baale resolves it "
            "through public exposure and naming rather than violence or captivity, consistent with his "
            "established restraint (Chronicle III's clinic, Chronicle IV's transparency). Kra, Kojo, "
            "and Yao (all already locked) reused; no other named characters. Kanja does not appear in "
            "this entry, matching Chronicle V's precedent. Closes the six-entry forged-letter/pamphlet "
            "conspiracy arc."
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
            "batch": 252,
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
