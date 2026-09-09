#!/usr/bin/env python3
"""Batch 94: Guanin Chronicle II, "What He Chose to Print" (MCD-357)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-09, no source document. Third entry in Guanin's own "
    "Chronicles, dramatizing PH2-008's already-locked, genuine unresolved public friction with "
    "Kwame Ade, first flagged as undramatized in Guanin Chronicle I's (MCD-340) own continuity "
    "notes. Full narrative text at "
    "docs/lords-of-cian/chronicles/guanin-chronicle-ii-what-he-chose-to-print.md."
)

NEW_RULES = [
    {
        "id": "MCD-357",
        "category": "phase2-homage-chronicle",
        "statement": (
            "Guanin Chronicle II, \"What He Chose to Print\" (full narrative text at "
            "docs/lords-of-cian/chronicles/guanin-chronicle-ii-what-he-chose-to-print.md), the "
            "second entry in Guanin's own Chronicles, protagonist Eri Kotoko (PH2-008), not a Kanja "
            "Chronicle -- Kanja appears only as an unnamed guest, present at two separate moments "
            "months apart, taking no side and granted no command, intervention, or resolution "
            "credit. Dramatizes PH2-008's already-locked 'real, documented public friction with "
            "Kwame Ade... kept as genuine unresolved alliance tension' for the first time: Kwame "
            "Ade's Areito press prints a pamphlet, circulated by crier, calling Eri Kotoko's patient "
            "institution-building strategy a form of collaboration; Eri Kotoko, provoked in public, "
            "does not answer in the moment, instead spending four months building a documented "
            "account of Guanin's institutions raised without violence, then publishing his own "
            "pamphlet setting that account beside Kwame Ade's words without conceding either side, "
            "closing on one precisely aimed line. This puts 'The Unanswered Blow' (PH2-008) on the "
            "page in a new register -- a banked, deliberately delayed rhetorical reply rather than "
            "physical retaliation against a wrongdoer (as in Guanin Chronicle I, MCD-340) -- while "
            "matching the ability's stated mechanic exactly (deliberate, conscious release only; "
            "anger in the moment resets it to nothing). The alliance tension is deliberately left "
            "genuinely unresolved at the close, per PH2-008's own framing, with no side conceded. "
            "Eri Kotoko's closing line carries a deliberate, ambiguous echo of Areito Chronicle II's "
            "(MCD-356) events (Adeyemi's wound) without asserting he has specific knowledge of them. "
            "No new named characters; the scene is carried by the two already-locked leaders plus "
            "unnamed criers and distributors, consistent with the world's established "
            "pre-industrial crier/pamphlet media system (PH2-049, WC-012/WC-013). First Chronicle "
            "to put two already-locked homage-era leaders in direct dialogue (at a distance, "
            "through print) with each other."
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
            "batch": 94,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-09, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "Guanin Chronicle II (MCD-357), 'What He Chose to Print' -- dramatizes PH2-008's "
                "already-locked, genuine unresolved public friction between Eri Kotoko and Kwame "
                "Ade for the first time, via a banked rhetorical reply rather than violence. "
                + BATCH_NOTE
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
