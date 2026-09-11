#!/usr/bin/env python3
"""Batch 280: Sovereign Ghost of the Great Sea Alias Chronicle waves 32-34 (9 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Continues the Alias Chronicle sub-series' thirty-second, thirty-third, and thirty-fourth "
    "waves for the Sovereign Ghost of the Great Sea, under Abad's direct authorization: \"do 3 "
    "more alias wave for all eleven.\" Wave 32 opens with the alias's first personal, one-on-one "
    "honor duel against a human combatant specifically trained and sent to fight Kanja "
    "individually (a detailed, battle-intense Trinity/Onyx showcase), then a multi-year embedded "
    "Directorate agent unmasked by his own conscience rather than by betrayal or discovery (new "
    "minor named character Fenn, collision-checked clean), and closes on the first dramatized use "
    "of the Lodestone Lens (`ARS-382`) reading a shifting seafloor at extreme range to save a "
    "convoy from an undetected natural hazard. Wave 33 opens with a tsunami disaster-relief entry "
    "-- a new environmental register with no weather signature to read and nothing for the "
    "Trinity's combat capabilities to act against, honoring real losses rather than a clean save "
    "-- then a formal maritime-tribunal appearance where Garren Hask's ledger is used as courtroom "
    "evidence for the first time, resolving a piracy accusation on documented-pattern grounds "
    "rather than a claim of innocence, and closes on the first dramatized use of the Whalebone "
    "Tether (`ARS-383`) to gently redirect a migrating, non-hostile Titan-scale sea creature rather "
    "than fight or drown it, extending the restraint doctrine to a non-sentient register. Wave 34 "
    "opens with a payoff to the previously-unnamed apprentice from \"What Dol Maren Passed Down\" "
    "(`MCD-1039`), now named (Wren Calder, collision-checked clean) and formally joining the crew "
    "as a permanent, informed-consent hull-reader; then a fabricated-weather-intelligence deception "
    "used to lure the fleet away from a real target; and closes by paying off wave 32's opening "
    "duel arc, extending the alias's established institution-disbelieves-an-honest-account register "
    "into a new instance (a defeat and an act of mercy, buried rather than a sighting report). No "
    "new named characters beyond Fenn and Wren Calder, both collision-checked against the full "
    "ledger before drafting. All nine entries reuse already-locked crew (Garren Hask, Efa Gol, Dol "
    "Maren, Danne Sok, Pell Ostra) for continuity depth."
)

NEW_RULES = [
    {
        "id": "MCD-1460",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Champion Sent to Kill a Ghost\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-champion-sent-to-kill-a-ghost.md), Sovereign Ghost "
            "of the Great Sea Alias Chronicle XCIV, wave 32, first entry in the wave. A detailed, "
            "battle-intense personal one-on-one honor duel against a Directorate-trained champion "
            "sent specifically to fight Kanja individually, distinct from every prior fleet-scale "
            "or institutional antagonist (the Fleet-Marshal arc, `MCD-952`-`957`) and from the "
            "flagship-vs-flagship seamanship duel (`MCD-799`). Highlights Onyx of Oblivion's "
            "Cadence Ruin, Soulbound Edge, and Whisper of Shadows against an opponent purpose-"
            "trained to deny rhythm-reading. Kanja wins and spares him, asking only for an honest "
            "report. The First Blade is deliberately left unnamed. Sets up the closing entry of "
            "wave 34 (`MCD-1468`). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1461",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Compass That Pointed Wrong\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-compass-that-pointed-wrong.md), Sovereign Ghost of "
            "the Great Sea Alias Chronicle XCV, wave 32. A new register: a four-year embedded, "
            "genuinely willing Directorate agent among the crew is unmasked not by betrayal or "
            "discovery but by his own conscience, refusing a final order to relay a false bearing "
            "into an ambush lane. Distinct from the hostage-coerced position leak (`MCD-1203`) and "
            "the parole-then-reprisal betrayal register (`MCD-912`). Resolved by quiet release "
            "rather than punishment or crew integration, deliberately distinct from `MCD-1466`'s "
            "permanent-joining register later in this run. Reuses Efa Gol and Garren Hask. New "
            "minor named character: Fenn (the agent) -- collision-checked clean against the full "
            "ledger. Second entry in wave 32."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1462",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Seafloor Told the Lens\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-seafloor-told-the-lens.md), Sovereign Ghost of "
            "the Great Sea Alias Chronicle XCVI, wave 32, closing the wave. A new-gear register: "
            "the first dramatized use of the Lodestone Lens (`ARS-382`) for this alias, reading a "
            "shifting seafloor hazard at extreme range from the deck to redirect a convoy no "
            "lookout could have seen coming in time -- distinct from the Sovereign Eyes' "
            "close-range Blueprint Eye HUD used throughout prior entries, and from the deliberate "
            "false channel-marker reef ambush (`MCD-772`) since this hazard is natural and "
            "undetected by anyone rather than a trap. Reuses Garren Hask and Danne Sok. No new "
            "named characters. Closes wave 32 (`MCD-1460` through `MCD-1462`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1463",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Wave That Outran the Charts\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-wave-that-outran-the-charts.md), Sovereign Ghost of "
            "the Great Sea Alias Chronicle XCVII, wave 33, first entry in the wave. A new "
            "environmental register: a tsunami strikes a coastal settlement with almost no "
            "warning, distinct from every prior storm-based entry (`MCD-953`, `MCD-1071`, "
            "`MCD-1211`, `MCD-1206`) since there is no weather signature to read in advance and "
            "nothing for the Trinity's combat capabilities to act against -- pure disaster-relief "
            "rescue work after an unstoppable natural event, honoring real losses (nineteen dead "
            "alongside forty-one saved) rather than a clean save. Reuses Pell Ostra, Dol Maren "
            "(referenced), and Garren Hask. No new named characters. First entry in wave 33."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1464",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"Sworn Before the Salt Table\" (full narrative text at "
            "docs/lords-of-cian/chronicles/sworn-before-the-salt-table.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle XCVIII, wave 33. A new institutional register: Kanja and "
            "Garren Hask are summoned unarmed to testify before a neutral maritime tribunal of "
            "merchant-nations over a formal piracy accusation, distinct from the foreign-nation "
            "reputation acknowledgment (`MCD-490`), the bilateral pact (`MCD-1040`), and the "
            "political-neutrality mediation (`MCD-1221`) since the fleet is the accused party here. "
            "Extends Garren Hask's ledger (`MCD-445`, `MCD-1219`) into evidentiary use for the "
            "first time; the accusation is dismissed on documented-pattern grounds rather than a "
            "claim of innocence, keeping the doctrine's honesty about real raiding intact. Reuses "
            "Efa Gol and Garren Hask. No new named characters. Second entry in wave 33."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1465",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Reef Where the Whales Turned Back\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-reef-where-the-whales-turned-back.md), Sovereign "
            "Ghost of the Great Sea Alias Chronicle XCIX, wave 33, closing the wave. The first "
            "dramatized use of the Whalebone Tether (`ARS-383`) for this alias, redirecting a "
            "migrating, non-hostile Titan-scale sea creature away from a shipping lane rather than "
            "fighting or subduing it -- deliberately distinct from Undertow's own first dramatized "
            "use (`MCD-951`), which drags a hostile Titan-scale creature under, extending the "
            "restraint-over-fear doctrine to a non-sentient register for the first time. Reuses Efa "
            "Gol and Garren Hask. No new named characters. Closes wave 33 (`MCD-1463` through "
            "`MCD-1465`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1466",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Hand That Asked to Stay\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-hand-that-asked-to-stay.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle C, wave 34, first entry in the wave. A payoff to the "
            "previously-unnamed apprentice from \"What Dol Maren Passed Down\" (`MCD-1039`, wave "
            "20), naming him for the first time -- Wren Calder, collision-checked clean against the "
            "full ledger -- and extending his training arc into full, permanent, informed-consent "
            "crew membership as the fleet's third hull-reader, a new register distinct from the "
            "informal stowaway-fostering practice (`MCD-1210`) and from `MCD-1461`'s quiet-release "
            "register earlier in this run. Dramatizes the mortality-gap conversation as an explicit "
            "condition of joining, consistent with `MCD-958`/`MCD-1227`. Reuses Dol Maren and "
            "Garren Hask. New minor named character: Wren Calder. First entry in wave 34."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1467",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Storm They Called a Bluff\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-storm-they-called-a-bluff.md), Sovereign Ghost of "
            "the Great Sea Alias Chronicle CI, wave 34. A new adversarial-intelligence register: a "
            "rival trading concern fabricates a storm warning to lure the fleet's protection away "
            "from a grain convoy it intends to raid, distinct from the false distress-call ambush "
            "(`MCD-954`) and the false channel-marker trap (`MCD-772`), both of which used a false "
            "position or false danger rather than a false natural-condition claim. Extends Danne "
            "Sok's charting/pattern-reading role (`MCD-779`, `MCD-782`) into weather-verification "
            "specifically; the deception is caught and the raid prevented with no casualties. "
            "Reuses Danne Sok. No new named characters. Second entry in wave 34."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1468",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Directorate Wrote About the Duel\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-directorate-wrote-about-the-duel.md), Sovereign "
            "Ghost of the Great Sea Alias Chronicle CII, wave 34, closing the wave. Closes the arc "
            "opened at `MCD-1460`: the First Blade's honest report of his defeat and the mercy "
            "shown him is disbelieved and quietly buried by his own institution, which reclassifies "
            "the duel as inconclusive and reassigns him away from open water -- extending the "
            "alias's established institution-disbelieves-an-honest-account register (`MCD-795`) "
            "into a new instance (a personal combat defeat and mercy, rather than a sighting "
            "report). The First Blade remains unnamed, consistent with `MCD-1460`. Reuses Garren "
            "Hask. No new named characters. Closes wave 34 (`MCD-1466` through `MCD-1468`) and the "
            "three-wave run (waves 32-34, `MCD-1460` through `MCD-1468`)."
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
            "batch": 280,
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
