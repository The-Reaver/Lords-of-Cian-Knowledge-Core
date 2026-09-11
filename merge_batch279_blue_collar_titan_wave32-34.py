#!/usr/bin/env python3
"""Batch 279: Blue-Collar Titan Alias Chronicle waves 32-34 (9 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "Continues the Alias Chronicle sub-series' thirty-second, thirty-third, and thirty-fourth waves "
    "for the Blue-Collar Titan, under Abad's direct authorization: \"do 3 more alias wave for all "
    "eleven.\" Wave 32 opens with the alias's first winter/frost-heave hazard (\"The Frost That "
    "Cracked What Fire Never Could,\" a slow, cyclical threat extending Mafesto's Kinetic Transfer "
    "System into a sustained multi-cycle reading register), then its first contagious-illness/"
    "public-health engineering entry (\"What the Ventilation Couldn't Cure,\" entirely non-combat and "
    "explicit that rerouted airflow buys time rather than curing anyone), and closes with the alias's "
    "first entry where a Kanja-taught worker applies an honestly taught trade in service of the "
    "opposing side by free political disagreement rather than coercion or defection (\"The Apprentice "
    "Who Chose the Other Side\"). Wave 33 opens with the alias's first drought/water-scarcity crisis, "
    "deliberately inverting every prior flooding entry (\"The Well That Went Dry\"), then its first "
    "disability-accommodation register, building adaptive gear around one worker's actual remaining "
    "capability rather than lowering a certification standard (\"The Hand He Rebuilt to Hold a "
    "Tool\"), and closes with the alias's first entry locating a genuine physical limit inside "
    "Kanja's own sustained exhaustion, finally applying his own fatigue rule to himself (\"What He "
    "Couldn't Lift Twice\"). Wave 34 opens with the alias's first formal legal-testimony register, "
    "Kanja and Maret Vos testifying as expert witnesses in a Sovereign Trust corruption trial "
    "unrelated to the war (\"The Witness Stand Under the City,\" the one-hundredth Blue-Collar Titan "
    "Chronicle overall), then its first cross-border technical-diplomacy register, refusing exclusive "
    "paid instruction in favor of open teaching (\"The Trade They Wanted to Buy From Him\"), and "
    "closes with the alias's first graceful institutional handoff extended to a founding crew member "
    "rather than to Kanja himself, moving Corren Halst from front-line rotation into a training-hall "
    "role as her old dock injury catches up with her (\"The Rotation Corren Halst Finally Took\"). No "
    "new named characters across any of the nine entries -- every new figure (the healer, the former "
    "apprentice, the old digger, the certification board, the contractor, the magistrate, the "
    "tribunal clerk, the foreign envoys) is deliberately kept unnamed and one-scene, and every "
    "returning figure (Corren Halst, Danne Sok, Efa Gol, Dol Maren, Maret Vos, Pell Ostra) is reused "
    "from already-locked crew, collision-checked clean against the full ledger before drafting. "
    "Abad's approval: \"do 3 more alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1451",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Frost That Cracked What Fire Never Could\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-frost-that-cracked-what-fire-never-could.md), "
            "Blue-Collar Titan Alias Chronicle XCIV, wave 32, opening the wave. The alias's first "
            "winter/frost-heave hazard: repeated freeze-thaw expansion works invisibly on "
            "sound-looking timber shoring over days rather than a single dramatic event. Extends "
            "Mafesto's Kinetic Transfer System (ARS-010) into a new sustained, slow-timescale "
            "reading register, distinct from the density-sensing (MCD-1068), thermal-gradient "
            "(MCD-1181), and vibration-signature (MCD-1400) applications already locked. No Trinity "
            "combat; no enemy involved. Reuses already-locked crew member Corren Halst. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1452",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Ventilation Couldn't Cure\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-ventilation-couldnt-cure.md), Blue-Collar Titan "
            "Alias Chronicle XCV, wave 32. The alias's first contagious-illness/public-health "
            "engineering register, entirely non-combat and explicitly outside Kanja's own competence "
            "to cure: he reroutes a shared ventilation duct to isolate a barracks fever's air supply "
            "from the rest of the shelter, explicitly framed on the page as buying the healers time "
            "rather than curing anyone, extending the alias's structural-honesty ethos into a "
            "register where the honest answer is 'I can't fix this.' No Trinity, no enemy, no "
            "combat. Reuses already-locked crew member Danne Sok. The healer is a new, deliberately "
            "unnamed one-scene character (collision-checked clean). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1453",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Apprentice Who Chose the Other Side\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-apprentice-who-chose-the-other-side.md), Blue-Collar "
            "Titan Alias Chronicle XCVI, wave 32, closing the wave. The alias's first entry where a "
            "taught skill is used against the cause without malice or coercion: a Kanja-trained "
            "former apprentice is found working an honest reconstruction job for the Trust side by "
            "free, informed political disagreement, and Kanja declines to treat it as betrayal, "
            "affirming that teaching a trade honestly cannot be conditioned on loyalty to how it's "
            "used. Distinct from the coerced-informant register of MCD-1005 and the defector-"
            "integration payoff of MCD-1190. The unnamed apprentice is deliberately distinct from the "
            "orphan-boy mentorship lineage of MCD-653/MCD-1036/MCD-1195 (collision-checked clean). "
            "Reuses already-locked crew member Efa Gol. No new named characters. Closes wave 32 (with "
            "MCD-1451 and MCD-1452)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1454",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Well That Went Dry\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-well-that-went-dry.md), Blue-Collar Titan Alias "
            "Chronicle XCVII, wave 33, opening the wave. The alias's first drought/water-scarcity "
            "crisis, a purely civil-engineering register with zero enemy, zero combat, and zero "
            "Trinity showcase beyond Obsidian Malice's already-established quarrying application "
            "(MCD-655) -- deliberately inverting every prior flooding register (MCD-440, MCD-486, "
            "MCD-1193) rather than repeating any of them: Kanja locates and opens a deeper, "
            "untouched aquifer after the district's shallow wells run dry. Reuses already-locked "
            "crew member Dol Maren. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1455",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Hand He Rebuilt to Hold a Tool\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-hand-he-rebuilt-to-hold-a-tool.md), Blue-Collar Titan "
            "Alias Chronicle XCVIII, wave 33. The alias's first disability-accommodation register: "
            "an old digger who lost a hand is barred from certification by a standard chisel's "
            "design rather than any competence gap, and Kanja builds adaptive gear -- a shoulder-"
            "and-forearm harness with a re-angled chisel head -- fitted to the man's actual remaining "
            "capability, getting him certified on the strength of his own cut seam. Extends the "
            "dignity-of-labor theme (VB-061) and the standard-versus-capability distinction "
            "established at MCD-1069. The old digger and certification board are new, deliberately "
            "unnamed one-scene figures (collision-checked clean; distinct from the two-handed elderly "
            "Killane digger of MCD-442). Reuses already-locked crew member Pell Ostra. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1456",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What He Couldn't Lift Twice\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-he-couldnt-lift-twice.md), Blue-Collar Titan Alias "
            "Chronicle XCIX, wave 33, closing the wave. The alias's first entry locating a genuine "
            "physical limit inside Kanja's own sustained exhaustion, extending 'The Watch That "
            "Forgot to Rest' (MCD-1189, where he imposed hard rotation caps on others) by finally "
            "applying that same rule to himself after three sleepless days leave his grip failing "
            "mid-lift. Deliberately framed around physical labor fatigue rather than tactical "
            "judgment, keeping it distinct from the same-shaped register already used for a "
            "different alias (Bane's MCD-1059). Reuses already-locked crew members Corren Halst and "
            "Danne Sok. No new named characters. Closes wave 33 (with MCD-1454 and MCD-1455)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1457",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Witness Stand Under the City\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-witness-stand-under-the-city.md), Blue-Collar Titan "
            "Alias Chronicle C, wave 34, opening the wave -- the one-hundredth Blue-Collar Titan "
            "Chronicle overall. The alias's first formal legal-testimony register, distinct from the "
            "informal report-forcing-accountability entry (MCD-663) and the sustained-custody/"
            "interrogation register (MCD-1006): Kanja and Maret Vos testify as expert witnesses in a "
            "Sovereign Trust corruption trial over fraudulent tenement construction unrelated to the "
            "war, deliberately understated by Kanja's own explicit choice rather than dramatic. "
            "Reuses already-locked crew member Maret Vos. The contractor, magistrate, and tribunal "
            "clerk are new, deliberately unnamed one-scene figures (collision-checked clean). No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1458",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Trade They Wanted to Buy From Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-trade-they-wanted-to-buy-from-him.md), Blue-Collar "
            "Titan Alias Chronicle CI, wave 34. The alias's first cross-border technical-diplomacy "
            "register, distinct from the domestic materials-trade negotiation (MCD-1007) and the "
            "single-individual guild-barrier entry (MCD-1069): foreign envoys offer to pay for "
            "exclusive tunnel-engineering instruction, and Kanja refuses the exclusivity while "
            "accepting the teaching itself, extending the open-knowledge ethos into a diplomatic "
            "register for the first time. Reuses already-locked crew member Efa Gol as the visit's "
            "security lead. The envoys and their settlement are new, deliberately unnamed and "
            "unplaced figures (collision-checked clean; no proper noun introduced). No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1459",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Rotation Corren Halst Finally Took\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-rotation-corren-halst-finally-took.md), Blue-Collar "
            "Titan Alias Chronicle CII, wave 34, closing the wave. The alias's first graceful "
            "institutional handoff extended to a founding crew member rather than to Kanja himself "
            "-- mirroring his own declined permanent workers'-council seat (MCD-1183) -- as Corren "
            "Halst's long-standing dock-era leg injury forces her off front-line ladder rotation and "
            "into leading the crew's training hall instead, her expertise redirected rather than "
            "retired. Distinct from the aging/mortality registers applied to secondary figures "
            "(MCD-1185). Reuses already-locked crew members Corren Halst and Danne Sok. No new named "
            "characters. Closes wave 34 (with MCD-1457 and MCD-1458) and this run's three-wave arc "
            "(waves 32-34)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)
    assert len(NEW_RULES) == 9, f"expected 9 new rules, got {len(NEW_RULES)}"
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"
    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"
    ledger["rules"].extend(NEW_RULES)
    ledger["batches_completed"].append(
        {
            "batch": 279,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-11, no source document",
            "rule_count": len(NEW_RULES),
            "note": BATCH_NOTE,
        }
    )
    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())
    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")
    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs found post-write!"
    print(
        f"OK. Total rules: {len(ledger['rules'])}. "
        f"Ledger version: {ledger['ledger_version']}. "
        f"Batches: {len(ledger['batches_completed'])}."
    )


if __name__ == "__main__":
    main()
