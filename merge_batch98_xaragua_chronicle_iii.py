#!/usr/bin/env python3
"""Batch 98: Xaragua Chronicle III, "Where the Table Began" (MCD-361)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-09, no source document. Third Xaragua Chronicle "
    "written, chronologically the earliest by decades. This is the flagged prequel material Batch "
    "67 held open: 'the intended place to show the vulnerable, breaking version of him before this "
    "stillness was earned.' Full narrative text at "
    "docs/lords-of-cian/chronicles/xaragua-chronicle-iii-where-the-table-began.md."
)

NEW_RULES = [
    {
        "id": "MCD-361",
        "category": "phase2-homage-chronicle",
        "statement": (
            "Xaragua Chronicle III, \"Where the Table Began\" (full narrative text at "
            "docs/lords-of-cian/chronicles/xaragua-chronicle-iii-where-the-table-began.md), the "
            "third Xaragua Chronicle written but chronologically the earliest of all three by "
            "decades -- it precedes both Xaragua Chronicle II (MCD-337) and Xaragua Chronicle I "
            "(MCD-334), matching the same write-order-versus-in-universe-order pattern MCD-337 "
            "already established. Protagonist Arturo Salvatierra Duho (PH2-061), decades before "
            "'de la Muerte.' Dramatizes for the first time the loss PH2-061 already locks (his "
            "dock-boy cohort -- Nzila, Tunde, and Bendu, three new named characters, "
            "collision-checked against the full live ledger, zero prior hits -- lost to war and "
            "Xaragua's own street war, leaving only Arturo and Yaisa) and the origin of all three "
            "faces of 'Blood Debt': the protective face's first real use (saving Yaisa, dying in a "
            "cellar), the dark reverse's one deliberate, formative use (against the man responsible "
            "for the street war, deliberately left unnamed), and the personal cost of the reverse "
            "face landing visibly and permanently in his own aging, consistent with PH2-061's "
            "statement that 'every true use of the reverse face visibly ages him.' Also dramatizes "
            "the founding moment of 'No Blood at My Table' and the Five Families' original "
            "two-person nucleus (Arturo and Yaisa), matching PH2-061's framing that this is 'his "
            "direct answer to that decade -- a debt he is still paying, not resolved grief.' An "
            "unnamed Kanja appears only briefly and at the margins, one indistinct face among "
            "several strangers helping in the aftermath, given no dialogue and no interaction with "
            "Arturo -- deliberately consistent with why Arturo does not recognize or remember him "
            "by the time of Xaragua Chronicle II, decades later, where their first real meeting is "
            "written as a first meeting. Yaisa (PH2-062) appears as a wounded survivor, not yet "
            "Arturo's second-in-command. This Chronicle slots into no existing MCD- rule -- "
            "original homage-era material set in Xaragua itself, decades before any other Xaragua "
            "Chronicle."
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
            "batch": 98,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-09, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "Xaragua Chronicle III (MCD-361), 'Where the Table Began' -- the flagged Arturo "
                "prequel material held open since Batch 67, showing the vulnerable, breaking "
                "version of him and the founding of 'No Blood at My Table.' " + BATCH_NOTE
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
