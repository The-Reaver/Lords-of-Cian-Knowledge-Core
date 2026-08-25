#!/usr/bin/env python3
"""Merge Batch 25 into canon-ledger.json: Ashkeel, named characters. Closes the Ashkeel queue."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'Guild of the Extraordinary' (Google Drive fileId "
    "1cGEqnWXfUZOGSVksys32TSQninqSI_fWZ0LC7fSUGXM), Part 3 ('The Seven Seats of the High "
    "Spire' and the Altar of the Bond narrative scene). Same source document as Batches 19, "
    "22, 23, and 24; closes the Ashkeel queue from this document. House names translated "
    "throughout per ASH-014's already-locked rename (Solaas->Corvessa, Kaelen->Kragmoor, "
    "Nyxos->Vhaerlow, Thorne->Kestrion, Val-Cian->Aurelock; Vane and Moros unchanged). Every "
    "founder name and governance domain in this material matches ASH-014/ASH-015 exactly once "
    "translated, confirming this is the full-detail source those rules were originally "
    "summarized from."
)

NEW_RULES = [
    {
        "id": "ASH-050",
        "category": "Ashkeel",
        "statement": (
            "House Vane (the Seat of the Pure Cord) governs public protocols, binding "
            "ateliers, and the physical engineering of collars and harnesses. Founder Yvaine "
            "Vane designed the Grand Promenade's internal layout; during the Great Purge her "
            "operatives captured three entire strike-teams bloodless, via hogtie alone. House "
            "Vane's signature discipline, the Arterial Shackle, uses weighted tungsten cords, "
            "monofilament garrotes, and joint dislocation to kill by positional asphyxiation, "
            "leaving no marks. House philosophy: 'To control the physical form is to govern "
            "the soul. Restraint is the highest expression of mastery.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-051",
        "category": "Ashkeel",
        "statement": (
            "House Moros (the Seat of the Numbed Veil) governs the Apothecaries, bathhouse "
            "purity standards, and forensic toxicology. Founder Aurelius Moros wiped out a "
            "corrupt faction by dosing their bath oils with an odorless neurotoxin mimicking "
            "cardiac arrest in sleep. House Moros's signature discipline, the Dulled Pulse, "
            "uses micro-needles and contact poisons disguised as oils, candles, or wine, "
            "easing targets into fatal respiratory failure through pleasant sensory euphoria. "
            "House philosophy: 'Pleasure and oblivion share the same threshold. Yielding to "
            "sensation is the ultimate surrender.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-052",
        "category": "Ashkeel",
        "statement": (
            "House Corvessa (the Seat of the Mirror Edge) governs foreign diplomacy, "
            "espionage networks, and the Masking Rites. Founder Lysandra Corvessa spent "
            "fifteen years embedded in foreign courts, manipulating succession wars through "
            "pillow talk and calculated social ostracism. House Corvessa's signature "
            "discipline, the Mimic's Blade, uses micro-stilettos concealed in hairpins or "
            "corset boning and behavioral mimicry, striking at peak intimate vulnerability "
            "before vanishing via rapid identity change. House philosophy: 'Identity is a "
            "garment. True dominion belongs to the one who decides when it is stripped "
            "away.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-053",
        "category": "Ashkeel",
        "statement": (
            "House Kragmoor (the Seat of the Grave Weight) governs structural integrity of "
            "the lower vaults, kinetic foundries, and seismic defense engineering. Founder "
            "Commander Torin Kragmoor collapsed three mountain ridges during the Great Purge "
            "to trap invading forces under a million tons of basalt, securing the monolith's "
            "isolation. House Kragmoor's signature discipline, the Resonant Rupture, uses "
            "heavy ordnance and hyper-dense crushing weapons (blackened basalt maces, "
            "hydraulic polearms) to cause structural 'accidents' eliminating targets behind "
            "fortified bunkers. House philosophy: 'No ego can withstand gravity; no will can "
            "survive the weight of the stone.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-054",
        "category": "Ashkeel",
        "statement": (
            "House Vhaerlow (the Seat of the Silent Thread) governs acoustic dampening, "
            "internal surveillance, and dark-sector monitoring. Founder Vesper Vhaerlow's "
            "stalker-sect eliminated enemy sentries in total darkness and silence during the "
            "Purge. House Vhaerlow's signature discipline, the Acoustic Void, uses soft-soled "
            "footwraps, sound-suppressing field collars, and twin kerambits to strike through "
            "ventilation ducts without exceeding 5 decibels. House philosophy: 'Silence is not "
            "emptiness; it is the absolute discipline of withholding speech until commanded.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-055",
        "category": "Ashkeel",
        "statement": (
            "House Kestrion (the Seat of the Cold Scale, ASH-016) governs the Supreme Court "
            "of Arbitration, dynamic-contract registration, and direct Iron Collar command. "
            "Founder Magistrate Julian Kestrion authored the Basalt Codex's ~1,200 articles, "
            "and once sentenced his own sworn partner to execution for an unnegotiated "
            "safe-sign breach. House Kestrion's signature discipline, the Judicial Execution, "
            "is the formal dual-shear combat doctrine used in authorized Bladeless Court "
            "duel-trials. House philosophy: 'Without explicit boundaries, freedom is merely "
            "chaos. Strict obedience is the only shelter that lasts.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-056",
        "category": "Ashkeel",
        "statement": (
            "House Aurelock (the Seat of the Red Hearth) holds the Sovereign Kept Seat: "
            "custodianship of the Black Archives, the Geothermal Core, and the Purge Key "
            "(ASH-048). Founder and the citadel's first Grand Magistrate, Cassian Aurelock, "
            "bound his house to eternal neutrality after the Purge, surrendering all external "
            "commercial contracts to serve as the sanctuary's impartial keystone. House "
            "Aurelock's signature discipline, the Master Seal, is systemic containment and "
            "high-yield thermal weaponry, deployed solely against internal insurrection or "
            "existential external threats. House philosophy: 'The house must stand though all "
            "within it bleed. Neutrality is paid for in absolute resolve.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-057",
        "category": "Ashkeel",
        "statement": (
            "Named individuals: Cord-Master Theron of House Vane and Arbitrator Sela of House "
            "Kestrion sparred a ritual duel-trial in the abyssal rings at -40,000 ft, opening "
            "with the traditional greeting already locked at ASH-031's underlying material "
            "('Clear boundary' / 'Open stone'), Theron fighting with the Arterial Shackle's "
            "tungsten cords against Sela's Judicial Execution shear-work, ending when Theron "
            "raised the Universal Safe-Sign (ASH-035, ASH-040) and Sela halted immediately. "
            "Post-duel aftercare for such trials takes place at the Vapor Cloister of House "
            "Moros, three levels below the trial rings at -43,000 ft, extending the "
            "mandatory-aftercare principle already locked at ASH-030."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full draft as pasted in-conversation: "lock it". This closes out the Ashkeel material from "Guild of the Extraordinary" entirely.'


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
            "batch": 25,
            "source_doc": "Guild of the Extraordinary (Ashkeel, named characters)",
            "source_id": "1cGEqnWXfUZOGSVksys32TSQninqSI_fWZ0LC7fSUGXM",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "2.8"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
