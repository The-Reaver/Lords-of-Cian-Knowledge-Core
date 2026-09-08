#!/usr/bin/env python3
"""Batch 77: Guanin Chronicle I ("The Debt Comes Due"), the first entry in
Guanin's own Chronicle series -- protagonist Eri Kotoko (PH2-008), Kanja as
unnamed guest, matching the established territory-Chronicle convention
(MCD-334/335/336/339)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Guanin Chronicle I ('The Debt Comes Due'), chat-drafted 2026-09-08, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/guanin-chronicle-i-the-debt-comes-due.md."
)

NEW_RULES = [
    {
        "id": "MCD-340",
        "category": "World Mechanics",
        "statement": (
            "Guanin Chronicle I ('The Debt Comes Due') is the first entry "
            "in Guanin's own Chronicle series, per the established "
            "structure (MCD-334/335/336/339): each Phase 2 homage-era "
            "territory has its own Chronicles, with its own leader as "
            "protagonist and Kanja appearing only as an unnamed guest. Eri "
            "Kotoko (PH2-008), on the evening his six-year forced-restraint "
            "bargain finally ends, is watched by an unnamed stranger who "
            "arrives on a dockside bench and stays present but uninvolved "
            "through the night. Eri Kotoko's signature ability ('The "
            "Unanswered Blow,' PH2-008) is shown directly in operation for "
            "the first time: six years of deliberately, consciously banked "
            "provocation, released in a single precise strike against the "
            "man who actually caused it (an unnamed counting-house figure "
            "who spent those six years needling him personally, believing "
            "the silence permanent) rather than a proxy, consistent with "
            "the ability's stated deliberate-release mechanic and its cost "
            "(anger, rather than conscious release, would have reset the "
            "banked force to nothing -- the scene is explicit that no anger "
            "is shown). PH2-008's already-locked friction with Kwame Ade is "
            "not dramatized here, left open for a future entry. No new "
            "named characters introduced. Slots into no existing mainline "
            "battle -- original homage-era material set in Guanin itself."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "locked"'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 77,
            "source_doc": (
                "Guanin Chronicle I ('The Debt Comes Due', MCD-340) -- the "
                "second territory Chronicle for NYC's remaining untouched "
                "leaders (Eri Kotoko/Guanin), continuing the open-ended "
                "Phase 2 territory-Chronicle expansion (alongside Xaragua "
                "I/II, Umoja I, Yara I, Areito I) that was never gated by "
                "the Pre-Book-1 Foundation Complete milestone (Batch 75)."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "8.0"
    ledger["last_updated"] = "2026-09-08"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
