#!/usr/bin/env python3
"""Batch 331: Phase 1.5 Atlas fable-review fixes (mechanical/reconciliation subset).

Applies the subset of the Atlas consistency review's findings that are pure
reconciliation against already-locked canon (no new creative/worldbuilding
facts): GEO-003's missing Rathaan Prime capital site, and GEO-006's
self-contradicting Hold/Settlement count wording against GEO-005.

The review's larger findings (C2 Verehimu/Voskharen Wetlands, C3 "aboard
the Karkosa", C5 the Teeth's placement, C6 MCD-094's area/population-weight
mismatch, E3 MCD-112's Southern Seaboard flag, and the EN1-EN9 enrichment
clusters -- Portside, the Kessic region, naval geography, Kesmara, House
Verehimu's seat, etc.) are new creative/worldbuilding decisions, not
reconciliation, and are deliberately NOT resolved here -- they remain
queued for Abad's own ruling, per the project's draft-then-approval
discipline.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Phase 1.5 fable-review of the World Atlas (GEO-001 through GEO-006) "
    "against the full Chronicle corpus and canon-ledger.json, following "
    "Phase 1's completion (Batches 320-330). Mechanical/reconciliation "
    "subset only."
)

AMENDMENTS = {
    "GEO-003": (
        "The atlas's canon-locked Capital/Maw sites, one per region: Rexhaven (Jicome), "
        "Ironmere (Aethel-Gard), The Spire (Zenith), Praetura/Maw-15 (The Prefecture), "
        "Kairo (The Shogunate), Skyvault (Astral Archipelago), Karkosa/The Throat "
        "(Sovereign Trust Domain), Ironhold plus Rathaan Prime and the Ash Maw Scar/"
        "Maw-1 Mother/Maw-3 Belly cluster (Lawless Reaches), Frontier Maw/Moonvault "
        "(Shattered Kingdoms), Dark Spire (T.D.K. Peninsula). Old Dominion Ruins has "
        "no canon-locked capital or Maw site -- fitting its fallen-civilization "
        "theming. Khorvane is a Hold within Old Dominion Ruins, not its capital; the "
        "earlier draft's naming of Khorvane as OD's capital is corrected here, per "
        "Abad's ruling that the live Atlas source controls over the earlier stale "
        "extraction. Corrected 2026-09-10 (Batch 103): the Karkosa capital venue is "
        "the unnumbered Throat (MAW-060); Maw-7 'the Keldane Maw'/'Slab of Judgment' "
        "(MAW-061) is a separate venue at Keldane, not Karkosa -- the earlier 'Maw-7 "
        "Slab' label for Karkosa was a stale pre-MAW-060/061 shorthand. Corrected "
        "2026-10-02 (Batch 331): the Lawless Reaches entry was missing Rathaan Prime "
        "(cell J20, Thornwork S), the live Atlas's fifth named Lawless Reaches "
        "Capital/Maw site and the Rathaan Federation's own seat (POL-090/POL-107)."
    ),
    "GEO-006": (
        "Beyond GEO-003's Capital/Maw roster, two Jicome-region sites carry "
        "Rebellion-era narrative weight and are locked here rather than left as "
        "free-to-rename flavor: Killane (Hold, Corehold-class fortress-city, cell "
        "C09, Jicome's southern district -- site of the Sewer War of Killane, "
        "MCD-234) and Ash Harbor (Settlement, Port-class, cell A09, Jicome's "
        "southern coast -- site of the Siege of the Ghost Harbor, MCD-235, "
        "informally renamed Ghost Harbor after the battle, per the Chronicle's own "
        "in-story renaming; grows to city scale over the Long Mask era, MCD-1352). "
        "With these two canon-locked additions the Gazetteer's Hold/Settlement total "
        "becomes 54 (24 Holds, 30 Settlements), of which GEO-005's 52 remain free to "
        "rename -- corrected 2026-10-02 (Batch 331) to resolve a wording "
        "contradiction between GEO-005 and this rule over whether the 52 included or "
        "excluded these two sites; they are, and always were, excluded from the "
        "free-to-rename 52 and additional to it."
    ),
}


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}

    amended = []
    for rid, new_statement in AMENDMENTS.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        rules_by_id[rid]["statement"] = new_statement
        amended.append(rid)

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule IDs found"

    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({
        "batch": next_batch,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": 0,
        "note": (
            "Phase 1.5 Atlas fable-review, mechanical subset. Amends GEO-003 (adds "
            "the missing Rathaan Prime capital site to the Lawless Reaches entry) "
            "and GEO-006 (resolves a GEO-005/GEO-006 wording contradiction over "
            "whether Killane/Ash Harbor are included in or additional to the 52 "
            "free-to-rename Holds/Settlements -- they are additional). Also fixes, "
            "prose-only (no ledger-statement change needed): a Kessic-region "
            "collision in two Bane Chronicles (MCD-681/683, the rumor's "
            "never-visited location renamed 'the Brinemoor salt flats' to resolve a "
            "contradiction with Kanja's own directly-established Kessic history); a "
            "second near-collision in a Scourge Chronicle (MCD-822, 'Varrow' renamed "
            "'Callow' to resolve a one-letter collision with the already-locked "
            "antagonist Lord Varro Dominael); and a real-world proper-noun leak "
            "('COINTELPRO') in Sankofa Chronicle V's narrative prose (MCD-1025), "
            "reworded to plain descriptive prose. The review's larger findings -- "
            "the Verehimu/Voskharen Wetlands naming question, whether 'the Karkosa' "
            "is the crew's own base or the enemy capital, the Teeth's Atlas "
            "placement, MCD-094's area-vs-population-weight framing, MCD-112's "
            "Southern Seaboard flag, and a full Portside/Kessic-region/naval-"
            "geography/Kesmara/House-Verehimu-seat enrichment pass -- are new "
            "creative/worldbuilding decisions, not reconciliation, and remain "
            "queued for Abad's own ruling rather than resolved here."
        ),
    })

    old_version = float(ledger["ledger_version"])
    ledger["ledger_version"] = str(round(old_version + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(
        f"OK: {len(ledger['rules'])} total rules, {len(ledger['batches_completed'])} "
        f"batches, ledger_version {ledger['ledger_version']}, zero duplicate IDs. "
        f"{len(amended)} rule statements amended: {', '.join(amended)}."
    )


if __name__ == "__main__":
    main()
