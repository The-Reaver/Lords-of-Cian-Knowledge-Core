#!/usr/bin/env python3
"""Batch 29: World Adaptation Blueprint, Sections I-II (mechanism + timeline)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'World_Adaptation_Blueprint' (Google Drive fileId "
    "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA, Lore Vault), Section I "
    "('The Mechanism -- How the World Hardens') and Section II ('The "
    "Timeline -- Five Books of Hardening')."
)

NEW_RULES = [
    {
        "id": "MCD-142",
        "category": "World Mechanics",
        "statement": (
            "The Talisman of Mao has operated the Grounded Bastion stage "
            "(MCD-060) fully autonomously for three hundred years, without "
            "Kanja's knowledge or authorization -- he believes it is merely "
            "a synchronization server with a density suppressor. Its "
            "mission is preventing his Aethelgard Kinetic Radiance from "
            "detonating outward and killing him; planetary structural "
            "repair is a means to that end, since a planet that fractures "
            "under the combat he's destined for is a planet on which he "
            "can't survive. Mechanically: the Talisman broadcasts a tuning "
            "pulse that aligns dormant Living Drakma ore veins running "
            "through the crust beneath three of the four continents (Living "
            "Drakma being a self-repairing, resonance-responsive "
            "crystalline organism, sourced from the Mao Volcano). Foundry "
            "Anvil channels compensatory tuning pulses into the crust "
            "within roughly 2,000 km of any high-density combat event, "
            "distributing impact load through the mineral grain; Heavy "
            "Hand extends micro-reinforcement to surfaces and structures "
            "in direct contact with the Avatars; Architectural "
            "Reinforcement gradually converts existing constructed "
            "structures (bridges, harbor walls, defensive walls) toward "
            "Living Drakma resonance over time, extending MCD-061's "
            "Gravity-Fetter/overflow mechanic to a planetary scale. None "
            "of this is detectable to the unaided eye; it registers to the "
            "Blueprint Eye as amber resonance signatures, to Orlok's "
            "Density Sight as anomalous mass distribution, and to "
            "Toussaint's Death-Impression Reading as a forensic absence of "
            "damage that should have occurred."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-143",
        "category": "World Mechanics",
        "statement": (
            "Lauris Letitia is treated as the biological proof-of-concept "
            "for what the planet of Cian is undergoing. Her Kares Prime "
            "physiology (Hexa-Lamellar Lattice, Gravimetabolic "
            "Architecture, WC-002/WC-006) hardened across countless "
            "generations under crushing homeworld gravity through ordinary "
            "survival pressure, not intentional engineering -- bodies that "
            "didn't adapt didn't survive, and the surviving compromises "
            "stacked into her present density. The Talisman's three-century "
            "tuning pulse is performing the equivalent operation on Cian's "
            "crust, bedrock, harbor walls, and atmosphere on a geological "
            "timescale: the world is becoming, functionally, a Karesian "
            "planet."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-144",
        "category": "World Mechanics",
        "statement": (
            "Combat density ceilings escalate on a fixed schedule across "
            "the five books, and the world's response escalates to match, "
            "staying just far enough behind that Book 5's climax is the "
            "first time the planet's response is visibly insufficient: "
            "Book 1, 2,000-4,000x (Branded), world response imperceptible "
            "without diagnostic tools; Book 2, 5,000-8,000x (Proven), "
            "detectable to the Blueprint Eye and Karesian proprioception; "
            "Book 3, 8,000-16,000x (High Proven/Lower Sovereign), "
            "measurable to Density Sight; Book 4, 16,000-22,000x "
            "(Sovereign, brief S-tier bursts), macro-visible, and the book "
            "where Sephtis shares his theory with Kanja directly; Book 5, "
            "20,000-42,000x+ (S-tier collision, Limitless at impact), the "
            "system visibly at capacity throughout."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-145",
        "category": "World Mechanics",
        "statement": (
            "T.D.K., during his Era 11-12 containment program, "
            "independently performed his own geological hardening of his "
            "subterranean kingdom using Ionic Rite resonance loops "
            "(CULT-001, CULT-005) embedded in the deep crust, both to "
            "contain the Ever-Haunt and to maintain structural integrity "
            "against the mantle's pressure -- this predates and is "
            "independent of the Talisman's tuning pulse. Where the two "
            "systems' effects overlap at the Broken Meridian, the "
            "interaction is constructive: hardening doubles versus either "
            "system alone. In Book 5, the Orlok-Vakas collision at the "
            "Broken Meridian gate exceeds local tuning and nearly breaches "
            "it; the Talisman performs an emergency power reallocation to "
            "save the gate, leaving the rest of the planet's hardening at "
            "a deficit for approximately 48 hours -- the exact window "
            "T.D.K. times his climactic attack around. The system's "
            "absolute failure ceiling is approximately 42,000x sustained "
            "at a single contact point for over 0.4 seconds against "
            "unprepared substrate; beyond that, catastrophic de-coherence "
            "cascades to the Mao reservoir itself. This threshold is never "
            "crossed on-page (Avatars strike each other, not the planet), "
            "except for the Book 5 deficit window, during which several "
            "minor named catastrophes occur off-page as evidence the "
            "system was briefly down."
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
            "batch": 29,
            "source_doc": "World_Adaptation_Blueprint (Sections I-II: mechanism + timeline)",
            "source_id": "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "3.2"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
