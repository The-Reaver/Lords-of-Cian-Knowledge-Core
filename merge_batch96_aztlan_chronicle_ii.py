#!/usr/bin/env python3
"""Batch 96: Aztlan Chronicle II, "The Half He Never Carried" (MCD-359)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-09, no source document. Second entry in Aztlan's own "
    "Chronicles, paying off PH2-023's own stated backstory event, left as a deliberate unresolved "
    "forward reference at the close of Aztlan Chronicle I (MCD-347). Full narrative text at "
    "docs/lords-of-cian/chronicles/aztlan-chronicle-ii-the-half-he-never-carried.md."
)

NEW_RULES = [
    {
        "id": "MCD-359",
        "category": "phase2-homage-chronicle",
        "statement": (
            "Aztlan Chronicle II, \"The Half He Never Carried\" (full narrative text at "
            "docs/lords-of-cian/chronicles/aztlan-chronicle-ii-the-half-he-never-carried.md), the "
            "second entry in Aztlan's own Chronicles, protagonist Ollin (PH2-023), not a Kanja "
            "Chronicle -- Kanja appears only as an unnamed guest, present throughout but granted no "
            "command, intervention, or resolution credit, notably including no intervention or "
            "advice at the confrontation itself. Pays off PH2-023's own stated backstory event "
            "directly: three weeks before a major march, Iya (PH2-030), having raised the same "
            "concern in six prior meetings, calls out Ollin's repeated exclusion of women from "
            "leadership credit and decision-making despite their equal organizing labor; when he "
            "again defers it, she leads every woman in the organization out that night. The march "
            "proceeds three weeks later with real, uncompensated structural losses (water shortages, "
            "lost contacts) even though 'The Formation' (PH2-023) still holds mechanically -- "
            "precisely dramatizing the ability's stated cost that ignored internal grievance costs "
            "the organization something real. Ollin's failure is deliberately not redeemed or "
            "walked back, matching PH2-023's own unsparing framing that he 'never listened to the "
            "people who built it beside him'; Iya's grievance is kept specific (real, structurally "
            "uncredited organizing labor) and is not minimized or resolved by the narrative. No new "
            "named characters -- Iya and Ollin are both already-locked figures. Fifth territory "
            "(after Xaragua, Areito, Guanin, and Uhuru) to receive a second Chronicle entry."
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
            "batch": 96,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-09, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "Aztlan Chronicle II (MCD-359), 'The Half He Never Carried' -- pays off PH2-023's "
                "own stated backstory event, Iya's 1970 walkout over unaddressed sexism, dramatized "
                "without redeeming Ollin's failure. " + BATCH_NOTE
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
