#!/usr/bin/env python3
"""Merge Batch 22 into canon-ledger.json: Ashkeel, the Seven High Arts."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'Guild of the Extraordinary' (Google Drive fileId "
    "1cGEqnWXfUZOGSVksys32TSQninqSI_fWZ0LC7fSUGXM), Part 7 / 'Master Codex of the Basalt "
    "Citadel, Volume I: Foundations & The Seven High Arts', Point 3. Same source document as "
    "Batch 19 (Ashkeel founding and governance). House names translated to match ASH-014's "
    "already-locked renaming: Nyxos->Vhaerlow, Solaas->Corvessa, Thorne->Kestrion (Vane and "
    "Moros unchanged). 'The Vapor of Cian' renamed to 'the Obsidian Vapor' and 'the Nyxos "
    "Blindfold' renamed to 'the Vhaerlow Blindfold' per Abad's naming corrections, 2026-08-25."
)

NEW_RULES = [
    {
        "id": "ASH-023",
        "category": "Ashkeel",
        "statement": (
            "Ashkeel formalizes seven master disciplines collectively known as the Seven High "
            "Arts, each governed by specific Houses and taught through a dedicated master guild "
            "or order: Ars Funis (the Cord & Span, rope-craft and suspension), Ars Pulsus (the "
            "Kinetic Cadence, impact and sensation), Ars Vacui (the Sensory Void, deprivation "
            "and immersion), Ars Acûs et Minium (the Needle & Cinnabar, piercing and "
            "contract tattooing), Ars Foci (the Hearth Service, domestic protocol), Ars Vaginae "
            "et Acuminis (the Edge & Sheath, arousal regulation), and Ars Unguenti (the Scent & "
            "Balm, apothecary aftercare)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-024",
        "category": "Ashkeel",
        "statement": (
            "Ars Funis, the Cord & Span, is House Vane's founding discipline and its master "
            "guild is the Guild of the Flushed Tether (Promenade Tier). It governs rope "
            "suspension as a synthesis of structural engineering and kinetic meditation: cords "
            "are prepared through a four-stage rite (caustic wash, singe and scrub, "
            "beeswax/camellia/clove balm infusion, basalt-kiln tempering), rated to a minimum "
            "850 lbs static break-strength, and load is always routed through skeletal anchor "
            "points, never soft tissue, with the pelvic cradle (the Hesselbach Saddle) bearing "
            "70-80% of suspended mass. Three classical forms exist: the Grounded Tether (floor "
            "work), the Transitional Cradle (semi-suspension), and the Flight of the Basalt "
            "(full suspension). The induced trance state is termed Sopor Funis."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-025",
        "category": "Ashkeel",
        "statement": (
            "Ars Pulsus, the Kinetic Cadence, is the discipline of rhythmic impact play. Unlike "
            "the other six High Arts, the source material names no single governing House or "
            "master order for it, it stands institutionally unassigned. It classifies impact "
            "into four sensory harmonics (the Sting, the Thud, the Bite, the Flush), enforces "
            "absolute zero-strike zones (the kidney bed T12-L3, the coccyx and spine, all major "
            "joints), and structures a scene in four movements (the Warming Ripple, the Ascent, "
            "the Plateau, the Resolution). Named implements include the Basalt Flogger, the "
            "Obsidian Dragon, the Honeycomb Paddle, and the Silk Crop."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-026",
        "category": "Ashkeel",
        "statement": (
            "Ars Vacui, the Sensory Void, is governed jointly by House Vhaerlow and House "
            "Moros, centered in the Sub-Basalt Wells (-30,000 to -38,000 ft). It strips "
            "external stimuli through three immersion enclaves: the Cradle of the Tide "
            "(magnesium-sulfate brine pools), the Anechoic Vaults (sound-deadened chambers), "
            "and the Cocoon of the Shadow (dermal restraint suits), and requires constant "
            "vital-sign telemetry with zero unmonitored isolation. Named gear includes the "
            "Vhaerlow Blindfold and the Acoustic Plugs of Moros. Safety tether is maintained "
            "via the Thread of Ariadne, with a mandatory Three-Stage Return triggered if heart "
            "rate exceeds 110 or drops below 42 BPM for over two minutes."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-027",
        "category": "Ashkeel",
        "statement": (
            "Ars Acûs et Minium, the Needle & Cinnabar, covers dermal piercing, temporary "
            "suspension piercing, and permanent contract tattooing. Its master order is the "
            "Scribes of the Crimson Point, jointly of House Kestrion and House Moros, operating "
            "under mandatory scribe-witness and sterile-crucible protocol. Permanent contract "
            "marks (the Contract Codex) are tattooed beneath the left clavicle in cinnabar ink "
            "at Silver Collar elevation, with a hash mark added per contract renewal. Flesh "
            "suspension via curved steel hooks is termed Scapular Flight (upper back) or Oculus "
            "Hang (chest); the spinal furrow and inguinal canal/femoral vein are strict "
            "zero-piercing zones."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-028",
        "category": "Ashkeel",
        "statement": (
            "Ars Foci, the Hearth Service, is the foundational discipline of domestic protocol, "
            "governed by House Vane and the Wardens of the Lower Hearth. It defines four "
            "classical postures (the Resting Bond, the Stone Flank, the Chalice Dais, the "
            "Prostration of the Altar) and a fixed morning-vestment ritual (the Wake, the Steam "
            "Tray, the Attendance, the Vesting, the Collar Check, 05:30-06:30). It is treated as "
            "prerequisite to the dynamic hierarchy the other six Arts operate within."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-029",
        "category": "Ashkeel",
        "statement": (
            "Ars Vaginae et Acuminis, the Edge & Sheath, governs arousal regulation and release "
            "control. Its master order is the Wardens of the Silver Lock, jointly of House "
            "Corvessa and House Moros. Devices are custom-molded, locked via a bespoke "
            "four-bladed Signet Key kept on the Dominus's neck chain, and removed every 72 "
            "hours under Council health edict for inspection. The edging ritual (the Nine "
            "Waves) runs four stages, Ignition, Crest, Still Command, Descent, and release "
            "itself is termed the Sovereign Harvest, granted only under specified conditions."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-030",
        "category": "Ashkeel",
        "statement": (
            "Ars Unguenti, the Scent & Balm, is Ashkeel's apothecary aftercare discipline, "
            "legally mandated under the Basalt Codex, Section IV, Articles 190-214, with a "
            "compulsory 60-minute post-scene grounding window. Its master order is the "
            "Apothecaries of the Cloistered Flask, House Moros. Four formulations are "
            "canonical: the Blue Resin (bruise/hyperemia treatment), the Cord-Balm "
            "(friction/dermal restoration), the Obsidian Vapor (olfactory de-escalation, "
            "distilled frankincense, atlas cedarwood, and sweet spikenard, slowing respiration "
            "to 6 breaths/minute), and the Crucible Nectar (electrolyte/glucose draught). Legal "
            "penalties attach to aftercare failure: a Dominus may not leave the premises for at "
            "least two hours after a Tier III/IV scene, and leaving a Vessel unattended and "
            "cold (\"the Cold Floor Infraction\") suspends the Dominus's registry."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the draft as pasted in-conversation, with two corrections (rename "the Vapor of Cian" and update "the Nyxos Blindfold" to match the Vhaerlow rename), then confirmed: "lock it"'


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
            "batch": 22,
            "source_doc": "Guild of the Extraordinary (Ashkeel, Seven High Arts)",
            "source_id": "1cGEqnWXfUZOGSVksys32TSQninqSI_fWZ0LC7fSUGXM",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "2.5"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
