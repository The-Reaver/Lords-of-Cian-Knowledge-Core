#!/usr/bin/env python3
"""Batch 106: Lock Bane Alias Chronicles II and III (MCD-366, MCD-367), completing Bane's
three-entry Alias Chronicle wave alongside "The Pivotal Piece" (MCD-365)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-10, no source document."

BATCH_NOTE = 'Abad: "lock it."'

NEW_RULES = [
    {
        "id": "MCD-366",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Trap Built From His Own Shape\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-trap-built-from-his-own-shape.md), Bane Alias "
            "Chronicle II. Rebellion era, several months after the Battle of the Black Trench "
            "(MCD-232), within the \"Bane\" window -- not a territory Chronicle; new standalone "
            "material outside the already-locked Twenty-Two Victories list. An unnamed "
            "Directorate officer, a Black Trench survivor, spends months reverse-engineering "
            "Kanja's own ravine-sealing tactic into a countermeasure: an ambush wash rigged with "
            "Dead Drakma charges to collapse on Bane the way he collapsed one on Suppression "
            "Brigade Kethane. Bane walks in forty minutes ahead of the staged convoy, alone, and "
            "identifies the trap from the ridge road by the smell of freshly cut support timber. "
            "Standing at the wash's narrowest point with the officer's hand already on the "
            "detonation lever, he states plainly that the trap only works on someone who doesn't "
            "know it's there, and that the only genuinely undecided variable left is whether the "
            "officer will pull the lever anyway. The officer never does. Extends VB-060's "
            "\"Already-Finished Negotiation\" presence trait into a combat/ambush register -- the "
            "officer's own hesitation, not a spoken declaration, carries the trait this time. No "
            "new named characters; the officer is unnamed and one-scene, matching the "
            "Undersecretary precedent from \"The Pivotal Piece\" (MCD-365)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-367",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Conscripts Wouldn't Do\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-conscripts-wouldnt-do.md), Bane Alias "
            "Chronicle III, closing Bane's three-entry Alias Chronicle wave alongside \"The "
            "Pivotal Piece\" (MCD-365) and \"The Trap Built From His Own Shape\" (MCD-366). "
            "Rebellion era, within the \"Bane\" window, a skirmish distinct from both. A "
            "nineteen-year-old conscript holds a salt-flat causeway line the night Bane's column "
            "is reported approaching; dread outruns any order down the ditch, and roughly a third "
            "of the nine-hundred-strong line sets its weapons down and walks away before a shot "
            "is fired. Bane appears only once, at distance, walking unhurried at the head of the "
            "column; the engagement dissolves before contact, on an unrelated order from "
            "elsewhere. Decades later the surviving conscript insists: 'We didn't lose our nerve. "
            "We ran out of a fight that wasn't there to begin with.' Extends VB-060's presence "
            "trait to collective/army scale rather than one-on-one. No new named characters; the "
            "conscript, the sergeant, and the line are unnamed."
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
            "batch": 106,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks Bane Alias Chronicles II (MCD-366, 'The Trap Built From His Own Shape') "
                "and III (MCD-367, 'What the Conscripts Wouldn't Do'), completing Bane's "
                "three-entry wave alongside 'The Pivotal Piece' (MCD-365), per the standing "
                "Alias Chronicles direction (three per alias per wave). " + BATCH_NOTE
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
