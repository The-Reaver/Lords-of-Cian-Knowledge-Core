#!/usr/bin/env python3
"""Batch 57: Phase 1b, seventh and final document. Codex of Holdfasts --
the fortification-typology reference. Its naming taxonomy was already
locked (HLD-001, HLD-010 through HLD-014); this batch fills in the
mechanics behind each name: garrison sizes and functions for every
Tactical Work, structural definitions for every Seat/Holdfast and
Regional Work, wallcraft component functions, and the two siege
doctrines' full step-by-step sequences. Closes out Phase 1b."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Codex_of_Holdfasts.docx (Google Drive fileId "
    "1kPNoq3QbQio_ORshHGkSyn6i25Fwbn7Y, the Lore Vault copy -- several "
    "byte-identical non-Lore-Vault copies also exist). Seventh and "
    "final document drafted under Phase 1b of the pre-Book-1-era "
    "roadmap. The fortification-typology naming taxonomy in this "
    "document was already locked (HLD-001, HLD-010 through HLD-014, "
    "confirmed clean with zero overlap at lock time); this batch adds "
    "the mechanical detail -- garrison sizes, structural functions, "
    "and full siege-doctrine sequences -- that those name-only rules "
    "did not yet carry. Purely self-contained reference material: no "
    "named characters, no plot content, no contradictions found."
)

NEW_RULES = [
    {
        "id": "HLD-015",
        "category": "fortification-tactical-works",
        "statement": (
            "Extends HLD-010 (Tactical Works, Tier S): Loophold "
            "(garrison 10-30, holds a gate/ford/road-bend via a "
            "jettied top floor for straight-down fire on the door); "
            "Crouchwork (4-12, a camouflaged half-buried nest for one "
            "heavy engine team); Drumtower (15-40, a sole-engine "
            "coastal strongpoint with a shot-turning sloped wall); "
            "Wardtower (8-25, early-warning beacon and raid-refuge); "
            "Skywarden Block (100-300, a self-sustaining anti-sky "
            "bastion against airborne Ever-Haunt); Delvework (garrison "
            "varies, a buried protective vault); Thornwork (50-150, a "
            "rapid disposable field fort); Breakwork (30-80, a "
            "detached work that breaks an assault into pieces before "
            "the main walls); Sweepway (an internal ditch-raking "
            "gallery, not a standalone garrison)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "HLD-016",
        "category": "fortification-seats-holdfasts",
        "statement": (
            "Extends HLD-011 (Seats and Holdfasts, Tier M): Moundhold "
            "(a mound keep over a working bailey, the simplest true "
            "lordly seat); Ringkeep (a Moundhold grown into a stone "
            "ring-wall); Twinward Hold (two concentric walls at "
            "different heights firing on the same point together, the "
            "hardest medium seat to storm); Quadrangle Hold (square "
            "plan, four corner towers, strength thrown to the outer "
            "perimeter rather than a central keep); Hallfast (a lesser "
            "lord's defended manor, enough to turn away raiders, not "
            "an army); Charterwall Town (a walled trade town, "
            "citizen-manned under charter); Courtfast (a fortified "
            "administrative palace); Crownhold (a ruler's citadel "
            "doubling as a province's administrative seat)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "HLD-017",
        "category": "fortification-regional-works",
        "statement": (
            "Extends HLD-012 (Regional Works, Tier L): Spurstar Fort "
            "(a bastioned artillery fort with projecting spurs giving "
            "interlocking ditch crossfire); Corehold (a city's "
            "last-resort citadel, built to hold after the city around "
            "it falls); Anglehold Fort (a simplified Spurstar with "
            "flat walls and sunken ditch-galleries instead of spurs); "
            "Wallcrown City (an entire metropolis ringed by monumental "
            "walls); Double Cordon (a besieger's doctrine, not a "
            "defender's structure -- twin earthworks around a besieged "
            "hold, the outer facing a relief army, the inner penning "
            "the garrison); Wardline (a continental frontier chain of "
            "towers, mile-forts, and depots filtering movement along a "
            "whole border)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "HLD-018",
        "category": "fortification-wallcraft-terms",
        "statement": (
            "Extends HLD-013 (wallcraft components): Toothline (a "
            "toothed wall-crown giving cover with gaps to step out and "
            "fire); Spillworks (overhanging galleries for dropping "
            "stone/scald/timber on attackers at the wall's foot); "
            "Sightslits (narrow-outside/wide-inside firing ports for a "
            "near-unhittable, wide-arc archer); Shatterskirt (a "
            "sloping stone skirt barring mining and turning dropped "
            "stone into outward shrapnel); Toothgate (a stone-groove "
            "drop-grate, often paired to trap a vanguard between two); "
            "Drop-shafts (ceiling openings between paired Toothgates "
            "for raining shot and burning liquid on trapped "
            "attackers)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "HLD-019",
        "category": "fortification-siege-doctrine",
        "statement": (
            "Extends HLD-014: the High Assault, used to crack a "
            "Twinward Hold or any high-walled seat, in five steps -- "
            "ring the hold to stop relief; fill the ditch under mobile "
            "sheds; batter the wall and foul the water; mine and fire "
            "a corner tower; storm the Killing Strip under twin firing "
            "tiers to reach the keep. The Killing Strip is the "
            "death-zone between a breached outer wall and a taller "
            "inner wall, swept by both walls' defenders "
            "simultaneously."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "HLD-020",
        "category": "fortification-siege-doctrine",
        "statement": (
            "Extends HLD-014: the Low Approach (Trenchwork Method), "
            "used against a Spurstar Fort where a direct rush dies in "
            "interlocking crossfire, in four steps -- a First Line "
            "trench dug outside engine range as a staging ground; "
            "Crook-saps cut at sharp angles so no engine can fire "
            "straight down them; a Second Line of skimming engines "
            "bouncing shot along the wall-tops to silence the spurs; a "
            "Breaching Line pounding one spur point-blank into a "
            "walkable ramp."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "HLD-021",
        "category": "fortification-tier-system",
        "statement": (
            "Extends HLD-001: Dead Drakma composite is banded into a "
            "great seat's wall core for battering resistance beyond "
            "bare masonry; Living Drakma is never spent on walls under "
            "any circumstance -- no fortification is considered worth "
            "what a single Living-Drakma blade is worth. Every named "
            "hold, tower, and line is catalogued on the Continental "
            "Atlas (by region, class, tier, and grid cell), with this "
            "Codex serving as the Atlas's structural-terminology key."
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
            "batch": 57,
            "source_doc": "Codex_of_Holdfasts.docx -- Phase 1b, seventh and final document: garrison sizes/functions for every Tactical Work, structural definitions for every Seat/Holdfast and Regional Work, wallcraft component functions, and the two siege doctrines' full sequences, extending the already-locked naming taxonomy (HLD-001/010-014). Closes out Phase 1b.",
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "6.0"
    ledger["last_updated"] = "2026-09-04"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
