#!/usr/bin/env python3
"""Batch 50: Phase 1b, first document. Kanja's post-Mafesto tactical
architecture (the Long Mask loadout, ages 30-284) -- the Valen Protocol,
the seven-piece gear system, and two Talisman-of-Mao mechanism corrections
surfaced while cross-checking the source against the live ledger."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Kanja_Tactical_Architecture_CLEAN.docx (Google Drive fileId "
    "1bObql6Hk6X-I3qD2kYApE5_INwp0xsB4, the later, more refined revision "
    "of Kanja_Tactical_Architecture.docx fileId 1Clxmjt3qqEepg7qAqim3LOFZ978h0Hh7 "
    "-- the CLEAN version's Kinetic Absorption entry corrects the original's "
    "passive-absorption framing to the grounding/conductance mechanism locked "
    "at MCD-291, so CLEAN was used as primary source). First document drafted "
    "under Phase 1b of the pre-Book-1-era roadmap. Two labeling corrections "
    "made using this project's established compatible-reading precedent "
    "rather than escalated as open contradictions: the Foundry Anvil stage "
    "mislabel (MCD-292, same pattern as the Blueprint Eye fix in Batch 49) "
    "and the Dhar-Kael Courser cartilage sourcing read as historical/"
    "stockpiled material given the species' already-locked near-extinction "
    "status, not active harvesting of the three remaining bonded animals."
)

NEW_RULES = [
    {
        "id": "MCD-291",
        "category": "World Mechanics",
        "statement": (
            "Extends MCD-060 (Talisman of Mao, Stage 3 Internal Quench, "
            "sub1 Bone-Tempering): Kanja's Bio-Drakma skeleton does not "
            "passively absorb kinetic impact but conducts it downward "
            "into the ground -- he routes force rather than tanking it. "
            "Full effect requires grounding; the routing capacity is "
            "finite, and his soft tissue, organs, and joints remain "
            "vulnerable when grounding is unavailable (airborne, "
            "shipboard, unstable terrain) or impacts exceed the routing "
            "capacity. This refines, rather than contradicts, "
            "Bone-Tempering's existing structural-reinforcement function "
            "-- the skeleton's hardness is what makes the conductance "
            "possible in the first place."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-292",
        "category": "World Mechanics",
        "statement": (
            "Extends MCD-060 (Talisman of Mao, Stage 2 Grounded Bastion) "
            "and matches the Blueprint Eye precedent (MCD-289): the "
            "source document attributes a Forge-Coat leather-treatment "
            "process to 'Foundry Anvil data (Stage 2 Sub 1)' -- "
            "mislabeled, the same kind of stage-numbering error already "
            "caught once in this document set. Foundry Anvil is Stage 2 "
            "Sub 2 (radiance channeled into subterranean strata, "
            "recipient the Planet, per MCD-060); Stage 2 Sub 1 remains "
            "Heavy Hand. What the source actually describes is real and "
            "locked as new material once relabeled: Kanja studied "
            "Foundry Anvil's underlying materials-science data -- not a "
            "literal instance of the planet-scale function running on "
            "cloth -- to develop a treatment giving his coat's "
            "Dark-Drakma leather a liquid-shedding surface tension and a "
            "light-absorptive quality that approximates, without "
            "replicating, Mafesto's Void-Lattice."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-293",
        "category": "World Mechanics",
        "statement": (
            "Extends MCD-144 (Kanja's Book 5 density ceiling, 42,000x+) "
            "and MCD-227 (Kanja's Book 1 baseline, 6,000x resting / "
            "~18,000x combat ceiling): Kanja's Book 5 resting density is "
            "12,000x, distinct from and well below his Spike ceiling. "
            "Unlike Ozmund's fixed 15,000x resting baseline across all "
            "five books (MCD-219), Kanja's resting density itself "
            "escalates across the series (6,000x to 12,000x); the Spike "
            "ceiling does most of the escalation work (18,000x to "
            "42,000x+) on top of that rising floor."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-344",
        "category": "avatar-arsenal",
        "statement": (
            "The Valen Protocol: during the rebellion's eighth year, "
            "after the Battle of the Forge Quarter (age 26), Valen "
            "Sinisterblade -- already locked as Ezio Valcari's cousin and "
            "combat mentor, here established as Kanja's Master-at-Arms "
            "and known by the alias 'the White Lotus' -- identified "
            "Kanja's total dependency on Mafesto as a structural "
            "vulnerability and ordered him to document what the armor "
            "did that his body could not, starting immediately rather "
            "than after the armor was inevitably lost. Kanja complied "
            "from age 26 through the Trinity's surrender at age 30 "
            "(MCD-246), treating every remaining Mafesto engagement as a "
            "dual military/documentation operation."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-345",
        "category": "avatar-arsenal",
        "statement": (
            "The Deficiency Catalogue: Kanja's documentation under the "
            "Valen Protocol (ARS-344) identified seven capability "
            "categories Mafesto's absence would leave exploitable -- "
            "Kinetic Absorption, Thermal Management, Sensory "
            "Augmentation, Psychological Projection, Environmental "
            "Sealing, Offensive Amplification, and Damage Tolerance -- "
            "each becoming a design brief for his post-Mafesto gear. The "
            "documentation was recorded in a notation system embedded in "
            "the Talisman of Mao's Blueprint Eye memory and survived the "
            "Trinity's surrender intact, since the Talisman (unlike "
            "Mafesto) is bonded to Kanja's skeleton and cannot be "
            "removed or surrendered."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-346",
        "category": "avatar-arsenal",
        "statement": (
            "The Capability Map: the seven Deficiency Catalogue "
            "categories (ARS-345) map to seven gear pieces developed "
            "over the Long Mask's 284 years -- Kinetic Absorption to the "
            "Forge-Coat; Thermal Management to the Forge-Coat's "
            "integrated coolant/smoke system; Sensory Augmentation to "
            "the Sovereign Eyes; Psychological Projection to the full "
            "loadout in combination; Environmental Sealing to the Breath "
            "Collar plus the Forge-Coat's lining; Offensive Amplification "
            "to the Ironhand Gauntlets, the Rexmar Machete (already "
            "locked, ARS-020's sibling entry), and the Ironfall Boots; "
            "Damage Tolerance to the Mend-Line."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-347",
        "category": "avatar-arsenal",
        "statement": (
            "The Forge-Coat, early versions: V1 (age 33, first deployed "
            "at the Crucible Market pit) was reinforced leather over "
            "ballistic weave with copper vent-tubes mimicking Mafesto's "
            "shoulder-port silhouette -- small-arms rated only, ~12 kg, "
            "proving the Scourge persona could survive without the armor "
            "through psychological precision alone. V2 (ages 40-80, the "
            "Pirate Dawn era) replaced the base with treated sea-leather "
            "over Dead Drakma wire mesh, added the armored high collar "
            "that anchors the Long Mask's silhouette the way Mafesto's "
            "helm anchored the Scourge's, and upgraded to "
            "edged-weapon/Elite-Standard (500x) impact resistance at ~9 kg."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-348",
        "category": "avatar-arsenal",
        "statement": (
            "The Forge-Coat, peak versions: V3 (ages 80-180, the Golden "
            "Terror era -- the version documented in the Long Mask "
            "Chronicles) introduced a triple-layer composite (Dark-Drakma "
            "leather outer shell, Dead Drakma articulated plates, "
            "thermal-regulating inner lining) with deliberately graduated "
            "protection -- torso and spine armored to Branded-class "
            "(~2,500x), limbs kept lighter at Elite Standard (500x) to "
            "preserve mobility, trading limb armor for organ protection "
            "since Kanja's Bio-Drakma skeleton makes his bones harder to "
            "break than his organs are to rupture. V3 also introduced the "
            "37-compartment Pocket Architecture (expanded in V4, "
            "ARS-349). V4 (ages 180-284) raised protection to 3,200x "
            "torso / 1,500x limbs / 4,000x spine at a lighter ~10 kg "
            "through 100+ years of materials refinement, added the "
            "Foundry-Anvil-derived leather treatment (MCD-292), and "
            "settled into what the document calls 'the 5'11\" Statement': "
            "Kanja's peak Long Mask silhouette makes no attempt to "
            "replicate Mafesto's 6'1\" frame -- it is its own identity, "
            "proof that the man survives without the armor rather than "
            "the armor's ghost."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-349",
        "category": "avatar-arsenal",
        "statement": (
            "The Pocket Architecture: the Forge-Coat V4's 42 engineered "
            "compartments (up from V3's 37), invisible from the exterior "
            "and retrievable by muscle memory, organized as 8 "
            "combat-access compartments (smoke triggers, Mend-Line "
            "rupture points) reachable by forearm pressure alone, 6 "
            "weapon-storage compartments (including the back-mounted "
            "Rexmar Machete), 10 engineering-tool compartments, 6 "
            "intelligence-material compartments in the innermost layer, "
            "6 medical-supply compartments beyond the automated "
            "Mend-Line, and 6 miscellaneous compartments including "
            "rations, currency, and one compartment never documented in "
            "any inventory -- known to the crew only as 'the Captain's "
            "pocket,' which Kanja has never opened in front of anyone."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-350",
        "category": "avatar-arsenal",
        "statement": (
            "The Sovereign Eyes: standalone HUD goggles interfacing with "
            "the Talisman of Mao's Blueprint Eye (MCD-289), displaying "
            "the same structural/biological/environmental overlay data "
            "Mafesto's helm once provided. V1 (age 33) was crude "
            "copper-framed lenses whose phosphor coating produced an "
            "unintended predator-eyed glow in darkness; Kanja preserved "
            "the effect deliberately in every later version. V2 (age 60) "
            "calibrated the glow to 585 nanometers -- deep amber, "
            "empirically tested across eleven formulations and twenty "
            "engagements as the wavelength producing the strongest human "
            "fear response. V3 (age 120) integrated the goggles into the "
            "Forge-Coat's hood/collar shadow geometry, creating the "
            "'demonic eyes' signature that defines the Scourge/Long Mask "
            "legend in-world. V4 (age 240+) uses Voidstone lenses "
            "(WC-011's diamond-equivalent currency-tier gem, here used "
            "structurally rather than as currency) in Dead Drakma "
            "frames, with the amber glow modulable between "
            "active-threat, surveillance, and fully dark stealth modes."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-351",
        "category": "avatar-arsenal",
        "statement": (
            "The Breath Collar: an armored throat-guard integrated into "
            "the Forge-Coat's collar since V2 (age 40), structurally "
            "stable since V3. Three simultaneous functions: filtration "
            "(a membrane neutralizing airborne toxins and particulate "
            "Blight contamination, complementing rather than duplicating "
            "the Talisman's frequency-level Blight Immunity, MCD-060 "
            "Stage 1 Sub 2); thermal regulation (Dead Drakma channels "
            "holding breathing-zone air at constant temperature "
            "regardless of environment); and voice projection (acoustic "
            "geometry producing the distorted, lower-register 'Captain's "
            "command voice' the crew recognizes, deliberately engineered "
            "to sound less human and more authoritative)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-352",
        "category": "avatar-arsenal",
        "statement": (
            "The Ironhand Gauntlets: articulated Dead Drakma "
            "hand/wrist/forearm armor functioning as mechanical force "
            "multipliers rather than passive protection -- solid Dead "
            "Drakma knuckle plates (~3x bone density) add roughly "
            "15-20% to a bare-fist strike's kinetic output, with convex "
            "impact geometry concentrating that force into penetration "
            "rather than blunt impact, and wrist/forearm bracing "
            "preventing self-injury from the added recoil. Evolved V1 "
            "(age 35, riveted plate gloves) through V2 (age 80, "
            "articulated dexterity plus wrist brace) and V3 (age 180, "
            "reforged convex knuckles, extended forearm brace) to V4 "
            "(age 260+, blood-heated for cold-weather dexterity, "
            "fine-motor capable without removal, and knuckle plates "
            "calibrated to a specific impact harmonic the Talisman's "
            "Kinetic Buffer, MCD-060 Stage 1 Sub 3, can amplify within "
            "the Sovereign Umbrella's radius)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-353",
        "category": "avatar-arsenal",
        "statement": (
            "The Ironfall Boots: reinforced Dead Drakma boots combining "
            "impact soles (a stomp-transmitted localized tremor "
            "destabilizing opponents within ~3 meters on shared solid "
            "ground, a physics-based effect independent of relative "
            "density), articulated ankle bracing (flexing within natural "
            "range but locking at injury-causing extremes), and a "
            "retractable heel blade (spring-triggered by a specific "
            "ankle rotation, deployed eleven times across 284 years, "
            "saving Kanja's life or freedom in nine of them)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-354",
        "category": "avatar-arsenal",
        "statement": (
            "The Smoke System: the Forge-Coat's integrated "
            "shoulder-vented coolant-capsule system (twelve capsules, "
            "six per shoulder), the visual core of the Scourge/Long Mask "
            "legend. Three discharge modes: Concealment (all twelve "
            "capsules, a 10-meter obscuring cloud disrupting visual and "
            "infrared observation for ~90 seconds), Signal (one capsule "
            "through a directional nozzle, visible to 500 meters for "
            "crew communication), and Terror (two capsules discharged "
            "bilaterally in sustained flow, calibrated for "
            "visibility-through-smoke rather than concealment -- the "
            "classic Scourge silhouette). Evolved from crude copper "
            "tubing and an inaccurate scent profile (V1) through Dead "
            "Drakma capillary channels and a corrected metallic scent "
            "approximation (V2), the addition of Terror mode (V3), to "
            "V4's capsule chemistry matching the smoke's light "
            "absorption to the treated coat's surface (MCD-292), "
            "dissolving the boundary between the man and the cloud."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-355",
        "category": "avatar-arsenal",
        "statement": (
            "The Mend-Line: a field-medical system in the Forge-Coat's "
            "lining, not medicine but engineering applied to the body -- "
            "six sealed reservoirs at anatomically critical points "
            "containing a Dead-Drakma-powder compound suspended in a "
            "biological adhesive derived from Dhar-Kael Courser "
            "cartilage. Given the Dhar-Kael's locked near-extinction "
            "status (three living survivors), this cartilage is "
            "understood as historical/stockpiled trade material rather "
            "than actively harvested from the three remaining bonded "
            "animals. Manual application (compartment pressure, "
            "~3-second flow, ~7-second hardening seal) manages bleeding "
            "and structural damage only -- not pain, organ repair, or "
            "concussive injury; the V4 formulation's bond strength "
            "exceeds the tissue it covers and requires surgical tools to "
            "remove, a deliberate design choice against combat failure. "
            "Evolved from hand-applied belt pouches (V1, age 50) through "
            "lining-integrated reservoirs (V2, age 100; V3, age 200, "
            "Dhar-Kael adhesive introduced) to V4 (age 270+)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-356",
        "category": "avatar-arsenal",
        "statement": (
            "The peak integrated Long Mask loadout (~14 kg total, six "
            "layers: thermal undergarment, Ironhand Gauntlets, Ironfall "
            "Boots, the Forge-Coat, the Sovereign Eyes, and the Rexmar "
            "Machete plus the loadout's other weapons) is the detailed "
            "engineering elaboration of the already-locked Pre-Awakening "
            "Theatrics System (ARS-310, MCD-246: Forge-Coat, "
            "Hymn-Engine, Dead Drakma Decoys, Smoke-Pots). This document "
            "details the Forge-Coat and Smoke-Pots (as the Smoke System, "
            "ARS-354) in full; the Hymn-Engine and Dead Drakma Decoys "
            "remain distinct, still-undetailed elements of the Theatrics "
            "System, not superseded or folded into this gear list."
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
            "batch": 50,
            "source_doc": "Kanja_Tactical_Architecture_CLEAN.docx -- Phase 1b, first document: the Valen Protocol, the Deficiency Catalogue, the Capability Map, and the seven-piece post-Mafesto gear system (Forge-Coat, Sovereign Eyes, Breath Collar, Ironhand Gauntlets, Ironfall Boots, Smoke System, Mend-Line), plus two Talisman-of-Mao mechanism corrections (Foundry Anvil stage relabel, Bio-Drakma conductance mechanism) and a Book 5 resting-density extension",
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 2,
            "conflicts_resolved": 2,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "5.3"
    ledger["last_updated"] = "2026-09-04"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
