#!/usr/bin/env python3
"""Batch 70: first step of the Chronicles I-VIII rewrite (roadmap Step 3).

Locks GEO-006, placing Killane and Ash Harbor within Jicome's existing
Atlas grid (neither existed anywhere in the live Regional Atlas, per
the Chronicle VI/VII/VIII audit), and amends GEO-005's Hold/Settlement
count from 52 to 54 to include them.

This is the first of the Chronicles I-VIII rewrite passes -- Chronicle
III's corrected text (Hask's age fixed 53->54, Corren Halst/Danne Sok/
Maret Vos added as Black Trench participants per MCD-234's Batch-41
correction and Chronicle V's own back-reference) is saved separately at
docs/lords-of-cian/chronicles/chronicle-iii-the-battle-of-the-black-trench.md,
not tracked as ledger rules of its own (matching the existing Chronicle
IX-XI precedent of full narrative text living outside canon-ledger.json,
with only the structural facts locked here)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Chronicles I-VIII rewrite (roadmap Step 3), cross-checked against "
    "research/atlas-live-sheet-audit.md via 8 parallel background-agent "
    "chapter audits, 2026-09-06. Killane (MCD-234, Sewer War of Killane) "
    "and Ash Harbor (MCD-235, Siege of the Ghost Harbor) do not appear "
    "anywhere in the live Regional Atlas Google Sheet; placed fresh "
    "within Jicome's existing grid rather than left unmapped."
)

NEW_RULES = [
    {
        "id": "GEO-006",
        "category": "atlas-canon-sites",
        "statement": (
            "Beyond GEO-003's Capital/Maw roster, two Jicome-region sites "
            "carry Rebellion-era narrative weight and are locked here "
            "rather than left as free-to-rename flavor: Killane (Hold, "
            "Corehold-class fortress-city, cell C09, Jicome's southern "
            "district -- site of the Sewer War of Killane, MCD-234) and "
            "Ash Harbor (Settlement, Port-class, cell A09, Jicome's "
            "southern coast -- site of the Siege of the Ghost Harbor, "
            "MCD-235, informally renamed Ghost Harbor after the battle, "
            "per the Chronicle's own in-story renaming). GEO-005's count "
            "updates from 52 to 54 (24 Holds, 30 Settlements) to include "
            "them."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

AMENDMENTS = [
    (
        "GEO-005",
        (
            "Beyond canon-locked sites, the atlas names 52 additional "
            "Holds and Settlements (23 Holds, 29 Settlements) plus one "
            "Wardline (The March, in The Prefecture), none of them "
            "canon-locked, free to rename -- correcting the earlier "
            "draft's rough estimate of 'roughly 40' against the live "
            "Atlas source's actual Gazetteer count."
        ),
        (
            "Beyond canon-locked sites, the atlas names 52 additional "
            "Holds and Settlements (23 Holds, 29 Settlements) plus one "
            "Wardline (The March, in The Prefecture), none of them "
            "canon-locked, free to rename -- correcting the earlier "
            "draft's rough estimate of 'roughly 40' against the live "
            "Atlas source's actual Gazetteer count. Two further sites, "
            "Killane and Ash Harbor, are canon-locked separately at "
            "GEO-006 rather than counted among these free-to-rename 52."
        ),
    ),
]

BATCH_NOTE = 'Abad: "lock it"'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    amended = []
    for rule_id, old_tail, new_tail in AMENDMENTS:
        found = False
        for rule in ledger["rules"]:
            if rule["id"] == rule_id:
                assert old_tail in rule["statement"], f"old_tail not found in {rule_id}"
                rule["statement"] = rule["statement"].replace(old_tail, new_tail)
                found = True
        assert found, f"{rule_id} not found"
        amended.append(rule_id)

    ledger["batches_completed"].append(
        {
            "batch": 70,
            "source_doc": (
                "Chronicles I-VIII rewrite (roadmap Step 3), first pass: "
                "locks GEO-006 (Killane, Ash Harbor placed within "
                "Jicome's Atlas grid) and amends GEO-005's count. "
                "Chronicle III's corrected narrative text (Hask's age "
                "fix, Corren Halst/Danne Sok/Maret Vos added to the "
                "Black Trench) saved at "
                "docs/lords-of-cian/chronicles/"
                "chronicle-iii-the-battle-of-the-black-trench.md."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "7.3"
    ledger["last_updated"] = "2026-09-06"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")
    print(f"Amended: {amended}")


if __name__ == "__main__":
    main()
