#!/usr/bin/env python3
"""Batch 68: World Atlas scoping (roadmap Step 2), resolved.

GEO-004 already flagged the locked GEO- rules as extracted from a
stale pre-correction snapshot. This batch corrects GEO-003 (adds
Lawless Reaches' capital/Maw sites, removes Khorvane as Old Dominion
Ruins' capital -- OD genuinely has none in the live source) and
GEO-005 (corrects the stale "roughly 40" Hold/Settlement estimate to
the live Gazetteer's actual count of 52 + 1 Wardline), against the
live Google Sheet audited in research/atlas-live-sheet-audit.md.
Also locks OPEN-012, deferring the sheet's undefined RA/UK/##/Throat/
Teeth artifacts, which Abad does not currently recall the intent of."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "The Lords_of_Cian_Regional_Atlas (live Google Sheet, Drive fileId "
    "1uhvmYi-52L4lpfbDn44WE1HiJwu8TgWDlGHVVPG524c, last modified "
    "2026-08-15), audited in full against the locked GEO- rules at "
    "research/atlas-live-sheet-audit.md. Corrects the stale pre-correction "
    "snapshot GEO-004 already flagged."
)

AMENDMENTS = [
    (
        "GEO-003",
        (
            "The atlas's canon-locked Capital/Maw sites, one per region: "
            "Rexhaven, Ironmere, The Spire, Praetura/Maw-15, Kairo, "
            "Skyvault, Khorvane, Karkosa/Maw-7 Slab, Frontier Maw/Moonvault, "
            "Dark Spire."
        ),
        (
            "The atlas's canon-locked Capital/Maw sites, one per region: "
            "Rexhaven (Jicome), Ironmere (Aethel-Gard), The Spire (Zenith), "
            "Praetura/Maw-15 (The Prefecture), Kairo (The Shogunate), "
            "Skyvault (Astral Archipelago), Karkosa/Maw-7 Slab (Sovereign "
            "Trust Domain), Ironhold plus the Ash Maw Scar/Maw-1 Mother/"
            "Maw-3 Belly cluster (Lawless Reaches), Frontier Maw/Moonvault "
            "(Shattered Kingdoms), Dark Spire (T.D.K. Peninsula). Old "
            "Dominion Ruins has no canon-locked capital or Maw site -- "
            "fitting its fallen-civilization theming. Khorvane is a Hold "
            "within Old Dominion Ruins, not its capital; the earlier "
            "draft's naming of Khorvane as OD's capital is corrected here, "
            "per Abad's ruling that the live Atlas source controls over "
            "the earlier stale extraction."
        ),
    ),
    (
        "GEO-005",
        (
            "Beyond canon-locked sites, the atlas names roughly 40 "
            "additional Holds and Settlements that are not canon-locked, "
            "free to rename."
        ),
        (
            "Beyond canon-locked sites, the atlas names 52 additional "
            "Holds and Settlements (23 Holds, 29 Settlements) plus one "
            "Wardline (The March, in The Prefecture), none of them "
            "canon-locked, free to rename -- correcting the earlier "
            "draft's rough estimate of 'roughly 40' against the live "
            "Atlas source's actual Gazetteer count."
        ),
    ),
]

NEW_OPEN_DECISION = {
    "id": "OPEN-012",
    "statement": (
        "What do the undefined map codes RA (10 cells, clustered in "
        "Lawless Reaches) and UK (5 cells, tied to a road named 'UK "
        "Spur') represent, and where are the canon-locked 'the Throat' "
        "and 'the Teeth' actually located?"
    ),
    "status": None,
    "note": (
        "The live Regional Atlas sheet contains these unresolved "
        "artifacts (see research/atlas-live-sheet-audit.md) with no "
        "defining legend entry anywhere. Abad does not currently recall "
        "their intended meaning, per his answer 2026-09-06 ('I have "
        "forgotten'). Deferred -- possibly resolvable by reviewing the "
        "live Sheet's native UI (cell coloring/shapes the text export "
        "can't capture) or by fresh invention later."
    ),
}

BATCH_NOTE = 'Abad: "confirmed"'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

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

    existing_open_ids = {o["id"] for o in ledger["open_decisions"]}
    assert NEW_OPEN_DECISION["id"] not in existing_open_ids, "OPEN-012 already exists"
    ledger["open_decisions"].append(NEW_OPEN_DECISION)

    ledger["batches_completed"].append(
        {
            "batch": 68,
            "source_doc": (
                "World Atlas scoping (roadmap Step 2): corrects GEO-003 "
                "(adds Lawless Reaches' capital, removes Khorvane as "
                "Old Dominion Ruins' capital) and GEO-005 (accurate "
                "Hold/Settlement count) against the live Regional Atlas "
                "Google Sheet, per research/atlas-live-sheet-audit.md. "
                "Locks OPEN-012 for the sheet's remaining undefined "
                "artifacts."
            ),
            "source_id": None,
            "rule_count": 0,
            "status": "complete",
            "conflicts_found": 2,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "7.1"
    ledger["last_updated"] = "2026-09-06"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")
    print(f"Amended: {amended}")
    print(f"Open decisions: {len(ledger['open_decisions'])}")


if __name__ == "__main__":
    main()
