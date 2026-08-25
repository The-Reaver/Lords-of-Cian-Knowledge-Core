#!/usr/bin/env python3
"""Batch 30: World Adaptation Blueprint, Section V (world response pattern + capacity)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'World_Adaptation_Blueprint' (Google Drive fileId "
    "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA, Lore Vault), Section V "
    "('The World as Character -- Response Pattern, Capacity, Ceiling'), "
    "5.1 and 5.2/5.5. Section IV (Reader Breadcrumbs) reviewed and "
    "deliberately not extracted -- it is writer's-room scene-placement "
    "notes restating Sections I/II/V's facts as breadcrumbs, not new "
    "world-building. Section V's 5.3/5.4 (the ceiling and failure mode) "
    "also not re-extracted here, already locked at MCD-145."
)

NEW_RULES = [
    {
        "id": "MCD-146",
        "category": "World Mechanics",
        "statement": (
            "The Talisman of Mao's planetary protection (MCD-142) runs a "
            "fixed four-phase response to applied density stress: "
            "Detection (continuous Sovereign Umbrella monitoring, ~0.04 "
            "second latency); Pre-Stress Reinforcement (a lattice-coherence "
            "pulse to a ~200-meter radius around the projected impact "
            "point, compensating 30-60% of the impact depending on local "
            "Living Drakma density); Distributive Absorption (force spread "
            "laterally through the reinforced mineral grain, so a "
            "2-meter-radius crater instead distributes as visible strain "
            "across ~15 meters); and Post-Stress Re-Tuning (4 hours for "
            "small impacts, up to 96 hours for Sovereign-tier ones, during "
            "which the affected zone sits at reduced capacity -- "
            "sequential strikes within this window are absorbed less "
            "effectively, the mechanism behind the Book 5 48-hour deficit "
            "at MCD-145)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-147",
        "category": "World Mechanics",
        "statement": (
            "The system's capacity is bounded by three finite resources. "
            "Living Drakma deposit density is distributed unevenly across "
            "the crust -- heaviest beneath Jicome (the Mao Volcano "
            "region), the Verehimu Wetlands, the Broken Meridian, and "
            "certain coastal seams, much thinner under the Sovereign "
            "Trust's interior holdings -- so combat fought near Mao is "
            "measurably better protected than combat fought in the "
            "Trust's interior. Talisman broadcast power is shared in real "
            "time across all three Stages simultaneously (Sovereign "
            "Umbrella, Grounded Bastion, Internal Quench) and currently "
            "runs at 99.9% utilization, a 0.1% margin between functioning "
            "and collapse; the Pi-Awakening cascade, when it triggers, "
            "temporarily redistributes this power and elevates risk during "
            "the redistribution window. Re-tuning latency (MCD-146) is a "
            "hard physical floor that cannot be shortened. During the Book "
            "5 48-hour reallocation deficit, the harbor floor at Karkosa "
            "still holds T.D.K.'s landing because three centuries of "
            "pre-loading kept its local capacity above threshold even at "
            "reduced power; elsewhere on the planet during the same "
            "window, it does not -- a small Verehimu Archipelago island "
            "partially submerges, a Sovereign Trust coastal cliff "
            "collapses with a fishing village on it, and two aging bridges "
            "fail, roughly 400 dead combined, reported off-page as "
            "evidence of the deficit rather than depicted directly."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full draft as pasted in-conversation: "lock it"'


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
            "batch": 30,
            "source_doc": "World_Adaptation_Blueprint (Section V: world response pattern + capacity)",
            "source_id": "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "3.3"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
