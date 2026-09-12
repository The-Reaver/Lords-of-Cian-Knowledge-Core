#!/usr/bin/env python3
"""Batch 287: Kazi (Detroit) supporting-cast additions -- Tunji and Femi."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-12, no source document."

BATCH_NOTE = (
    "Fills a real gap PH2-051 itself flagged: Kunle (Ken Cockrel Sr.) and Kalamu (a Watson/Hamlin "
    "composite) already fill Irin's 'two founding co-organizers' slot as the legal/press lieutenants, "
    "but the actual in-plant strike leadership behind DRUM's May 1968 wildcat was never homaged. "
    "Web-researched and confirmed via Wayne State's Reuther Library and contemporary accounts: Chuck "
    "Wooten, described as 'the guiding force' alongside General Baker among Black workers on the Dodge "
    "Main floor, and Ron March, who won election to Local 3's own trustee seat in 1969 -- DRUM's first "
    "electoral foothold inside the union itself. Two new rules lock them as a distinct pair (shop-floor "
    "organizing and the ballot box) rather than crowding or contradicting the already-locked "
    "legal/press lieutenant framing: Tunji (homage to Wooten) and Femi (homage to March). Both names "
    "collision-checked clean against the full ledger before drafting. No Chronicle drafted yet -- just "
    "the character additions. Abad's approval: \"lock it.\""
)

NEW_RULES = [
    {
        "id": "PH2-065",
        "category": "phase2-homage-detroit-supporting-cast",
        "statement": (
            "Tunji, homage to Chuck Wooten, Irin's (PH2-051) closest in-plant organizing partner -- "
            "Yoruba, 'reunited/gathered together.' Where Irin calls the halt, Tunji is the one who "
            "already has the floor lined up to answer it: the shop-floor organizer who turns "
            "individual grievances into a single standing readiness before Irin ever needs to act. "
            "Distinct from Kunle (PH2-063) and Kalamu (PH2-064), who work the courtroom and the press "
            "rather than the floor itself."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-066",
        "category": "phase2-homage-detroit-supporting-cast",
        "statement": (
            "Femi, homage to Ron March, the DRUM organizer who won election to the union local's own "
            "trustee seat -- Yoruba, 'love me.' Proof the movement could win standing inside the very "
            "institution it was built to pressure, not just outside it; Femi's seat is a foothold, not "
            "a truce, and Irin treats it as one more front rather than a victory that settles anything."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 2, f"expected 2 new rules, got {len(NEW_RULES)}"
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 287,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-12, no source document",
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
