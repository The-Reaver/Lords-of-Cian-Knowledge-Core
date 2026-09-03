#!/usr/bin/env python3
"""Batch 49: resolve the 8 contradictions surfaced across seven newly-
triaged Lore Vault documents (Kanja_Tactical_Architecture, Rexmar_
Civilization_Codex_Entry, Treasures_of_the_Moonvault, Lauris_Anirak_
Threat_Blueprint, MRD_Five_Book_Arcs, the Complete Structural Outline,
Codex_of_Holdfasts) before drafting their new material. Two amendments
in place (WC-005, MCD-221), six new reconciliation rules."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Reconciliation pass across eight contradictions surfaced during "
    "triage of seven documents newly found in a full Lore Vault re-audit "
    "(Kanja_Tactical_Architecture.docx, Rexmar_Civilization_Codex_Entry."
    "docx, Treasures_of_the_Moonvault, Lauris_Anirak_Threat_Blueprint, "
    "MRD Five Book Arcs, My_Rivals_Distance_Complete_Structural_Outline_"
    "Definitive, Codex_of_Holdfasts.docx). Presented to Abad in-"
    "conversation before any of the seven documents' new material was "
    "drafted, since several of the new facts depend on which side of a "
    "conflict is canon. All eight resolved by explicit ruling."
)

# --- In-place amendments ---

def amend_wc005(rule):
    rule["statement"] = (
        "The Pi-Awakening occurs only within the Rexmar bloodline, not "
        "unique to any single individual: a biological threshold at "
        "exactly 314 years, shifting the bearer from passive to active, "
        "gaining remote Drakma communication and environmental tuning. "
        "Haku experienced it roughly 5,000 years ago, forcing Anu Un "
        "Ra's retreat; Kanja's own Awakening at 314 is the next "
        "occurrence T.D.K.'s containment was built to prevent."
    )
    rule["note"] = (
        "Amended in Batch 49: the Rexmar_Civilization_Codex_Entry "
        "document states Haku himself was Pi-Awakened, contradicting "
        "this rule's original 'unique to Kanja' framing -- which was "
        "already in tension with the already-locked Pi-Vulnerability "
        "material ('Haku used it 5,000 years ago... Anu built "
        "containment for the next occurrence'). Reframed to describe a "
        "bloodline-wide phenomenon rather than a single-person one."
    )


def amend_mcd221(rule):
    rule["statement"] = (
        "Book 5's three fronts (already locked in general at MCD-097) "
        "break down as: Engine front -- Kanja, Ozmund, Pyro. Gate front "
        "-- Orlok, Anansi, Ezio, Fermand, Toussaint (matching the "
        "already-locked Gate team of MCD-098). Line front -- commanded "
        "independently by Red Beard (not literally alone), comprising "
        "Anirak, Ironbane's fleet, Aethel-Gard heavy infantry, Celestial "
        "Zenith warriors under Loyalty-Quasar, and the Astral "
        "Archipelago fleet."
    )
    rule["note"] = (
        "Amended in Batch 49: the Lauris_Anirak_Threat_Blueprint and the "
        "Complete Structural Outline documents both independently "
        "describe a fuller Line front roster, contradicting this rule's "
        "original 'Red Beard, operating alone.' Reframed as Red Beard "
        "commanding the front independently of the other two fronts' "
        "oversight, not literally solo."
    )


AMENDMENTS = {
    "WC-005": amend_wc005,
    "MCD-221": amend_mcd221,
}

NEW_RULES = [
    {
        "id": "MCD-287",
        "category": "World Mechanics",
        "statement": (
            "Extends WC-013: the Moonvault caldera's Living Drakma "
            "deposit is a rare, ancient exception to Jicome-exclusivity "
            "-- an isolated vein exposed by geological erosion over "
            "millennia, not evidence of a second natural source. T.D.K.'s "
            "attempted industrialization of Living Drakma (Old Dominion "
            "era) degraded the ore into an inferior imitation rather "
            "than true ritual-forged material, which is why Guild-"
            "Doctrine smiths who refused to adapt to his process fled "
            "rather than participate -- 'cannot be industrialized' "
            "remains true of Living Drakma in its authentic form."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-288",
        "category": "World Mechanics",
        "statement": (
            "The Treasures of the Moonvault document's account of six "
            "gifts (ending 'COMPLETE') is an earlier draft of the scene "
            "later finalized as the locked Ten Gifts (Sovereign's Five, "
            "ARS-330; Captain's Five, ARS-340). The three gifts that "
            "overlap -- the Wellspring Seal, the Conviction, and the "
            "Vigil Standard, all for Ozmund -- are consistent with and "
            "confirm the first three of the locked Sovereign's Five. "
            "'The Suture' (the draft's third gift for Kanja) does not "
            "survive into canon; Kanja's locked Captain's Five stands "
            "as-is. The Moonvault's physical setting, Haryn Dael, the "
            "Guild-Doctrine tradition, and the Ever-Haunt siege/rescue "
            "operation are unaffected by this superseding and remain "
            "canon."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-343",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-341: 'Dead-Light Drakma' (used to describe "
            "Onyx's material in two independently-triaged documents) "
            "describes Onyx's outward finish -- a vantablack surface "
            "treatment -- not its fundamental composition, which remains "
            "Living Drakma as locked (MCD-023, CC-003). Separately, "
            "Onyx's SBD blackscribe origin and its claimed 'Guild-"
            "Doctrine' lineage are the same fact from two angles, not "
            "competing ones: the SBD blackscribes who crafted it were "
            "themselves trained in the older Guild-Doctrine tradition."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-289",
        "category": "World Mechanics",
        "statement": (
            "'Blueprint Eye' -- a structural/sensory analysis function "
            "surfaced through Mafesto's HUD, reading stress fractures, "
            "density, environmental composition, hidden passages, and "
            "weak points -- is a real Talisman of Mao function, but is "
            "not Stage 2 Sub 1 (which remains Heavy Hand, per MCD-060); "
            "the source document mislabeling it was an error, and was "
            "also internally inconsistent about which stage it belonged "
            "to. Blueprint Eye is locked as a Stage 1 (crew-facing) "
            "function."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-122",
        "category": "character-crew",
        "statement": (
            "Extends MCD-251: 'Fury Variant' (used throughout the "
            "Lauris_Anirak_Threat_Blueprint) and 'Kinetic-Stack Variant' "
            "(MCD-251) name the same biology -- Fury Variant is the "
            "crew/narrative register, Kinetic-Stack Variant the precise "
            "SBD/technical classification."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-290",
        "category": "World Mechanics",
        "statement": (
            "Extends MCD-052/WC-001/CC-019: the Crown-Scar's root-access "
            "tether (capable of seizing direct control of a Verehimu "
            "bearer, e.g. Ozmund) is the most powerful expression of a "
            "broader siphon architecture embedded in the Verehimu "
            "bloodline -- at lower intensity, every Crown-Scar carrier "
            "functions as a drain point, with biological potential, "
            "density, and Impact Memory pulled from living bodies and "
            "fed into T.D.K.'s Warbody across thousands of taps in the "
            "general population. The tether and the siphon are one "
            "architecture at two scales, not competing mechanisms -- per "
            "Abad's explicit ruling, the siphon reframing folds in as an "
            "additional layer rather than replacing the already-locked "
            "tether mechanism."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad resolved all 8 contradictions explicitly in-conversation, one by one; the Crown-Scar mechanism (the most significant) per his ruling: "fold in the siphon reframing as an additional layer"'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    by_id = {r["id"]: r for r in ledger["rules"]}
    for rid, fn in AMENDMENTS.items():
        assert rid in by_id, f"amendment target {rid} not found"
        fn(by_id[rid])

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 49,
            "source_doc": "Reconciliation of 8 contradictions across 7 newly-triaged Lore Vault documents, ahead of drafting their new material",
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 8,
            "conflicts_resolved": 8,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "5.2"
    ledger["last_updated"] = "2026-09-03"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
