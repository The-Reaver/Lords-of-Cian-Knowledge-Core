#!/usr/bin/env python3
"""Batch 303: Ozmund Chronicle I, "The Man Who Didn't Know What He Was Protecting" (MCD-1730)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-21/22, no source document. Ozmund Verehimu's own "
    "Character Chronicle series, Chronicle I -- the first entry cleared for drafting under the "
    "Character Chronicle Launch Protocol, following the full three-step gate (Rules Walkthrough, "
    "Psychological Profile, Game Plan) at docs/lords-of-cian/character-profiles/ozmund-verehimu.md, "
    "game plan approved 2026-09-21. Full narrative text at "
    "docs/lords-of-cian/chronicles/ozmund-chronicle-i-the-man-who-didnt-know-what-he-was-protecting.md."
)

NEW_RULES = [
    {
        "id": "MCD-1730",
        "category": "kanja-alias-chronicle",
        "statement": (
            "Ozmund Chronicle I, \"The Man Who Didn't Know What He Was Protecting\" -- the first "
            "entry in Ozmund Verehimu's own Character Chronicle series, cleared for drafting under "
            "the Character Chronicle Launch Protocol once his profile+game-plan file reached 'game "
            "plan approved' (docs/lords-of-cian/character-profiles/ozmund-verehimu.md). Set strictly "
            "pre-Book-1, years before the Fulfillment Ceremony murder of Aethelgard Verehimu and Maro "
            "Rexmar (MCD-025), per Abad's standing constraint that the launch wave stays pre-ceremony "
            "until he explicitly reopens Book-1-era territory. Narrated by Red Beard (Tarn Cestari) "
            "per VB-020/022/CC-020, reconstructing a story Ozmund told him only once, years before "
            "the two of them ever met. Dramatizes the origin of the Draconis 'purity-test' dynamic "
            "(Colonel Viktor Draconis, CC-085) at its literal starting point: on a road trip with a "
            "living Aethelgard, a young Draconis -- eleven months into House Guard service -- throws "
            "himself between three attackers and the boy Ozmund during an ambush, genuinely believing "
            "his own skill alone saved them. Ozmund, whose Density Spike has been fully active and "
            "consciously controlled since infancy (MCD-024/CC-015/017, the 'no threshold to cross' "
            "psychological layer), actively suppresses it and lets himself appear afraid and "
            "helpless, so that Draconis's loyalty is never overshadowed by what he's actually "
            "protecting -- an early expression of the same dignity-through-agency value later shown "
            "in how he trains Red Beard as a soldier rather than liberates him as a victim (extends "
            "CC-090/ARS-381/MAW-084). Aethelgard names Draconis to the House Guard's inner command "
            "that same night, still unaware of the true shape of what happened. Ozmund never tells "
            "Draconis the truth, in the two decades Red Beard knew him or after -- a deliberate, "
            "unbroken choice, not mere circumstance. No new named characters; the twelve attackers "
            "are unnamed opportunists, not tied to Cassius Verehimu, Blackthorne, or any other "
            "reserved antagonist thread. The confirmed payoff (per the profile's psychological-"
            "profile discussion: whenever the truth eventually reaches Draconis, it deepens rather "
            "than breaks the relationship) remains reserved for a future, Book-1-era-or-later entry."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "locked."'


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
            "batch": 303,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-21/22, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "Ozmund Verehimu's Character Chronicle Launch Protocol gate closed -- Rules "
                "Walkthrough, Psychological Profile (ten collaboratively-layered facets), and Game "
                "Plan (narrator, pacing, reserved threads, a standing pre-Book-1 constraint on the "
                "launch wave, and Chronicle I's pitch selection) all approved in the same session, "
                "docs/lords-of-cian/character-profiles/ozmund-verehimu.md now reads 'game plan "
                "approved.' Locks Ozmund Chronicle I, 'The Man Who Didn't Know What He Was "
                "Protecting' (MCD-1730) -- the young-Draconis origin-of-the-purity-test entry, "
                "strictly pre-ceremony per Abad's own constraint. Two more pre-Book-1 pitches "
                "('What Never Had to Be Learned,' Aethelgard/discipline; 'Her Son, Not Her Line,' "
                "Val Mirel Kareth) remain queued next, order not yet fixed; two Book-1-era pitches "
                "(the Accession Games entry, the Ceremony itself) are deliberately deferred and "
                "flagged in the profile's Game Plan section until Abad reopens that window. "
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
