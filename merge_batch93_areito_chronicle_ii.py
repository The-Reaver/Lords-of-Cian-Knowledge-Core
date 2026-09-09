#!/usr/bin/env python3
"""Batch 93: Areito Chronicle II, "The One Who Stood Where He Stood" (MCD-356)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-09, no source document. Second entry in Areito's "
    "own Chronicles, directly paying off the explicit hook left at the close of Areito Chronicle I "
    "(MCD-339). Full narrative text at "
    "docs/lords-of-cian/chronicles/areito-chronicle-ii-the-one-who-stood-where-he-stood.md."
)

NEW_RULES = [
    {
        "id": "MCD-356",
        "category": "phase2-homage-chronicle",
        "statement": (
            "Areito Chronicle II, \"The One Who Stood Where He Stood\" (full narrative text at "
            "docs/lords-of-cian/chronicles/areito-chronicle-ii-the-one-who-stood-where-he-stood.md), "
            "the second entry in Areito's own Chronicles, protagonist Kwame Ade (PH2-004), not a "
            "Kanja Chronicle -- Kanja appears only as an unnamed guest, present throughout but "
            "granted no command, intervention, or resolution credit. Set seven years after Areito "
            "Chronicle I (MCD-339): Adeyemi, a new named character (Yoruba, 'the crown befits me') "
            "and former cellmate from Kwame Ade's first prison reinvention (the same conversion "
            "PH2-004 locks as the origin of his certainty, distinct from the second-reinvention era "
            "that produced Chronicle I's three unnamed attackers), confronts him alone and unarmed, "
            "arguing that spending their shared cell-forged conviction on strangers rather than the "
            "six men who forged it with him was a betrayal wearing conviction's own clothes. Adeyemi "
            "throws one blow matching his own genuine, unhesitating certainty and it lands, drawing "
            "the first blood anyone has ever drawn from Kwame Ade -- directly dramatizing PH2-004's "
            "own stated vulnerability ('only someone matching his own absolute certainty can hurt "
            "him... the one real threat to him was always going to come from someone who once stood "
            "exactly where he stood') as a literal, physical fact for the first time. Adeyemi does "
            "not finish the blow, finding himself newly and genuinely uncertain in a way he has not "
            "been in seven years, and departs with his own arc deliberately left open -- whether he "
            "returns, and which side of his new uncertainty he lands on, is unresolved. The unnamed "
            "Kanja offers one small, wordless, uncredited act of aid (a cloth pressed into Kwame "
            "Ade's hand for the wound) after Adeyemi leaves. No collision: Adeyemi is checked against "
            "the full live ledger and confirmed distinct from the already-locked Xaragua "
            "supporting-cast figures Kwabena (PH2-014) and Kwaku (PH2-016)."
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
            "batch": 93,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-09, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "Areito Chronicle II (MCD-356), 'The One Who Stood Where He Stood' -- pays off the "
                "explicit hook left at the close of Areito Chronicle I (MCD-339), dramatizing "
                "PH2-004's stated vulnerability for the first time via a new named character, "
                "Adeyemi. " + BATCH_NOTE
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
