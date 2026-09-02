#!/usr/bin/env python3
"""Batch 47: reconcile the five ledger-side conflicts surfaced by the full
Chronicles-I-VIII-vs-entire-ledger compliance pass (8 parallel background
agents, one per chapter). Three new rules, one amendment in place."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Reconciliation from the full Chronicles I-VIII compliance pass "
    "(Abad's standing instruction, 2026-08-25: once the ledger is more "
    "complete, cross-check every written chapter against the *entire* "
    "locked ledger, not just its original batch pairing). Eight parallel "
    "background agents read each chapter in full and cross-referenced it "
    "against all 733 rules; eight apparent conflicts surfaced across "
    "five chapters (III, V, VI, VII, VIII). Four were resolved here as "
    "ledger reconciliations (compatible readings requiring new or "
    "amended rules, not manuscript changes); four others were "
    "manuscript-side slips (misattributed battle details in chapter "
    "closing/summary passages) left for Abad's own editing pass rather "
    "than bent into the ledger."
)

# --- In-place amendment ---

def amend_wc002(rule):
    rule["statement"] = (
        "World physics is primarily Mass-Displacement (density/weight/"
        "gravimetabolic biology) rather than a mysticism-based magic "
        "system; this does not exclude frequency-craft (the Ten Tongues, "
        "WC-021) as a real, distinct, non-mystical technical system "
        "operating alongside mass-displacement physics -- both are "
        "physical phenomena, not supernatural ones."
    )
    rule["note"] = (
        "Amended in Batch 47 to resolve an apparent conflict raised by "
        "Chronicle III's use of frequency-craft language for the Cadence "
        "Ruin/Aegis-Talisman effects -- the chapter is consistent once "
        "this rule's original absolutist 'not frequency-craft' framing "
        "(promoted from a long-dormant draft in Batch 45 without close "
        "individual scrutiny) is narrowed to describe the *primary* "
        "physics rather than exclude the already-locked Tongues system "
        "entirely."
    )


NEW_RULES = [
    {
        "id": "ARS-341",
        "category": "avatar-arsenal",
        "statement": (
            "Onyx of Oblivion's true origin (SBD blackscribe-crafted, "
            "royal Karesian, predating Kanja's smithing career by "
            "millennia -- MCD-023, CC-003) and its acquisition story "
            "(recovered by Kanja from a dockside pawn shop at seventeen "
            "-- ARS-020, consistently depicted in the written "
            "manuscript's Chronicles I and V) are not in conflict: the "
            "blade's ancient nature was unknown to both the pawnbroker "
            "and Kanja at the time of purchase, having passed through an "
            "untold chain of custody before ending up anonymously "
            "shelved in an ordinary dockside shop. Its true nature was "
            "only recognized once Kanja bonded with it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-342",
        "category": "avatar-arsenal",
        "statement": (
            "Obsidian Malice's charge cycle operates at two different "
            "timescales, not in conflict: the already-locked 3-5 second "
            "recharge (ARS-030) is its active, in-combat discharge cycle "
            "once deployed; a separate, much slower passive accumulation "
            "occurs while the weapon sits dormant and unused (as it did "
            "for roughly two years before the Black Trench, mirroring "
            "Mafesto's parallel two-year dormancy, MCD-232) -- the "
            "two-years figure describes banked charge from disuse, not "
            "the combat recharge rate."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-285",
        "category": "World Mechanics",
        "statement": (
            "The Battle of Iron Shallows (age 19, MCD-233) had a "
            "secondary naval element alongside its primary, documented "
            "land/causeway convoy-stranding action: a Trust escort "
            "vessel, responding to the stranded convoy, ran aground and "
            "was boarded and captured by Kanja's fighters, becoming the "
            "flagship later named The Audit (already locked as captured "
            "'at Iron Shallows,' MCD-235). Consistent with, not a "
            "replacement for, MCD-233's zero-casualties/no-alias land "
            "engagement."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-286",
        "category": "World Mechanics",
        "statement": (
            "Extends MCD-231: the Scrip-Forge Raid's charcoal-rubbing "
            "evidence (age 18) additionally documented a Sovereign "
            "Trust-wide wage-underpayment scheme -- roughly 1.2 million "
            "workers underpaid by 40% over twelve years -- beyond the "
            "raid's original Forge-7 Drakma-debasement finding. This "
            "statistic belongs to the Scrip-Forge Raid's evidence chain, "
            "not the separate Sewer War of Killane (MCD-234), which used "
            "a different method (four months of undetected Scrip-"
            "Registry copying)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full draft as pasted in-conversation: "is editor approved"'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    by_id = {r["id"]: r for r in ledger["rules"]}
    assert "WC-002" in by_id
    amend_wc002(by_id["WC-002"])

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 47,
            "source_doc": "Chronicles I-VIII full-ledger compliance pass -- reconciliation of 4 of 8 surfaced conflicts (Onyx's origin, WC-002's frequency-craft framing, Obsidian Malice's charge model, Iron Shallows' naval element, Scrip-Forge Raid evidence extension); the other 4 (Chronicle VI's Furnace District/Maw-9 slips, Chronicle VIII's Receipt-capture and Killane-label slips) left as a manuscript-editing punch list, not ledger changes",
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 8,
            "conflicts_resolved": 4,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "5.0"
    ledger["last_updated"] = "2026-09-02"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
