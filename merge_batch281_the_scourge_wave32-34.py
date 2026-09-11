#!/usr/bin/env python3
"""Batch 281: the Scourge Alias Chronicle waves 32-34 (9 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Continues the Alias Chronicle sub-series' thirty-second, thirty-third, and thirty-fourth "
    "waves for the Scourge, under Abad's direct authorization: \"do 3 more alias wave for all "
    "eleven.\" Wave 32 opens with the sub-series' first genuine betrayal-from-within-a-freed-"
    "community failure state (a rendezvous sold to slavers for payment, defeated because the "
    "schedule had already quietly changed), then the first entry addressing the dependents of "
    "the people the crew's raids kill (a slaver's orphaned son, quietly placed rather than "
    "resolved), and closes with the sub-series' first formal multi-party tactical alliance -- a "
    "detailed joint operation with a foreign anti-slaving squadron, extending rather than "
    "repeating the established institutional-independence refusals. Wave 33 opens with Pell "
    "Ostra's own voluntary retirement, paralleling Efa Gol's, then the sub-series' first desert/"
    "arid overland environment (a salt-flat crossing where heat and thirst, not an enemy, are "
    "the antagonist), and closes on a sixty-year generational payoff extending 'The Merchant Who "
    "Changed His Trade' (a reformed slaver's grandson warning the crew of an ambush unprompted). "
    "Wave 34 opens with the sub-series' first voluntary, principled departure from the "
    "operational core (new minor named character Rowan Vail, collision-checked clean, "
    "reassigning away from the fear-based method on ethical grounds rather than age or injury), "
    "then the first entry addressing the long-term ecological cost of two centuries of the "
    "crew's own raids (reef restoration at the already-locked Salt Keep site, solved by patient "
    "labor rather than any gear), and closes the run with a symbolic full-circle return to "
    "Ash-Wharf, the persona's own origin site, for the first time in the sub-series' history. No "
    "new named characters beyond Rowan Vail, collision-checked against the full ledger before "
    "drafting. All nine entries reuse already-locked crew (Efa Gol, Garren Hask, Pell Ostra, and "
    "Efa Gol's established unnamed successor) for continuity depth, and none touches, restages, "
    "or contradicts the already-locked final night of the persona (`MCD-1022`, age 314)."
)

NEW_RULES = [
    {
        "id": "MCD-1469",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ones Who Sold Him Out\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ones-who-sold-him-out.md), the Scourge Alias "
            "Chronicle XCIV, wave 32, first entry. Age 205, V3 gear. The sub-series' first genuine "
            "betrayal-from-within-a-freed-community failure state -- distinct from every prior "
            "tactical failure (the drowned captives of `MCD-544`, the compromised route of "
            "`MCD-1238`, the tactical retreat of `MCD-1075`) in that the threat originates from "
            "someone the crew's own reputation had earned trust from, not an external enemy's "
            "skill or luck. A rendezvous cove sold to slavers for payment is defeated because the "
            "schedule had already quietly changed two nights before, a detailed Trinity ambush "
            "response following. Resolved without punishment of the informant, deliberately left "
            "open, extending the sub-series' established preference for honest, unresolved ledger "
            "entries. Reuses Efa Gol's established unnamed successor (`MCD-904`/`1240`/`1254`) and "
            "Garren Hask (`CC-115`/`116`). Onyx of Oblivion correctly absent per its L9 seal. No "
            "new named characters. First entry in wave 32."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1470",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Man Who Raised the Slaver's Son\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-man-who-raised-the-slavers-son.md), the Scourge "
            "Alias Chronicle XCV, wave 32. Age 120, V3 gear. The sub-series' first entry to "
            "directly address the dependents of the people the crew's raids kill or defeat -- a "
            "genuinely new moral register distinct from every prior entry about captives, "
            "informants, or reformed slavers, since the boy in question is neither victim nor "
            "perpetrator but an innocent bystander to both. A slaving overseer's six-year-old son, "
            "orphaned the night his father dies rather than surrender, is quietly placed with an "
            "unnamed freed-captive family rather than resolved into any tidy outcome; the boy's "
            "later fate is deliberately left unknown, matching the sub-series' established "
            "practice for open threads (`MCD-1231`, `MCD-1234`). Reuses Efa Gol (`CC-130`/`131`). "
            "No combat. Onyx of Oblivion correctly absent per its L9 seal. No new named "
            "characters. Second entry in wave 32."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1471",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fleet That Wasn't His to Command\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fleet-that-wasnt-his-to-command.md), the Scourge "
            "Alias Chronicle XCVI, wave 32, closing the wave. Age 195, V3 gear. The sub-series' "
            "first formal multi-party tactical alliance, distinct from the informal one-sided "
            "protection of 'The Signal Honest Ships Learned' (`MCD-382`) and the flat institutional "
            "refusals of 'The Contract He Wouldn't Sign' (`MCD-1017`) and 'The Insurance They Tried "
            "to Buy' (`MCD-1019`): a foreign anti-slaving squadron proposes a single time-limited "
            "joint operation against a fortified trafficking hub neither fleet can take alone, "
            "accepted on the same freely-chosen, freely-ended terms he'd offer any trusted ally, "
            "and a standing arrangement afterward is declined. A detailed full-gear combat "
            "showcase (Sovereign Eyes, Ironhand Gauntlets, the Rexmar Machete `ARS-260`, and "
            "Obsidian Malice) freeing ninety-six captives. No new named characters (the foreign "
            "commodore is unnamed and one-scene). Onyx of Oblivion correctly absent per its L9 "
            "seal. Closes wave 32 (`MCD-1469` through `MCD-1471`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1472",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Pell Ostra Set Down\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-pell-ostra-set-down.md), the Scourge Alias "
            "Chronicle XCVII, wave 33, first entry. Age 275, V4 gear. Pell Ostra's (`CC-132`/`133`) "
            "own voluntary retirement/step-back entry, paralleling Efa Gol's established retirement "
            "at age 150 (`MCD-807`) and explaining her later minimal cameo at age 308 (`MCD-1252`) "
            "as a deliberate, long-planned reduced role rather than an unexplained late reappearance. "
            "Distinct from every prior succession entry in that Ostra catches and chooses this "
            "herself before any failure occurs, directly building on her established signature "
            "measured-precision competency (`MCD-1076`). Reuses Efa Gol (`CC-130`/`131`) in an "
            "established supporting role. No combat; a craft-and-character entry. Onyx of Oblivion "
            "correctly absent per its L9 seal. No new named characters (Ostra's chosen apprentice "
            "is deliberately unnamed). First entry in wave 33."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1473",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Crossing With No Water\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-crossing-with-no-water.md), the Scourge Alias "
            "Chronicle XCVIII, wave 33. Age 155, V3 gear. The sub-series' first desert/arid "
            "overland environment, distinct from the prior land-based liberation ('The Caravan "
            "Road,' `MCD-802`, age 44, no specified terrain hardship) and every prior environmental-"
            "hazard entry (ice `MCD-1074`, altitude `MCD-1239`, flood `MCD-1245`, volcanic reef "
            "`MCD-1232`): a three-day salt-flat crossing where heat and thirst, not any armed "
            "opposition, are the real antagonist, and the reputation's usual fear weapon has no "
            "purchase on physics. Thirty-nine of forty-one captives freed, two lost before rescue "
            "reached them. No new named characters. Onyx of Oblivion correctly absent per its L9 "
            "seal. Second entry in wave 33."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1474",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Grandson Who Came to Warn Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-grandson-who-came-to-warn-him.md), the Scourge "
            "Alias Chronicle XCIX, wave 33, closing the wave. Age 230, V3 gear. Direct sixty-year "
            "generational payoff to 'The Merchant Who Changed His Trade' (`MCD-824`, age 170), "
            "extending a reformed slaver's changed legacy into the next generation choosing "
            "loyalty to the crew unprompted -- distinct from every prior redemption entry "
            "(`MCD-824`, `MCD-1247`), which showed conversion in the moment rather than its "
            "inheritance decades later. A reformed slaver's grandson travels three days to warn "
            "the crew, unprompted, of a rival-slaver ambush borrowed from an outdated decoy code; "
            "the ambush is quietly avoided rather than fought. Reuses Efa Gol's (`CC-130`/`131`) "
            "contact network and Garren Hask (`CC-115`/`116`). No new named characters (the "
            "grandson is deliberately unnamed). Onyx of Oblivion correctly absent per its L9 seal. "
            "Closes wave 33 (`MCD-1472` through `MCD-1474`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1475",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The One Who Chose to Leave\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-one-who-chose-to-leave.md), the Scourge Alias "
            "Chronicle C, wave 34, first entry. Age 198, V3 gear. The sub-series' first voluntary, "
            "principled departure from the Scourge's operational core -- distinct from Efa Gol's "
            "aging-out retirement (`MCD-807`) and Pell Ostra's failing-hands retirement "
            "(`MCD-1472`) in that the departing crew member leaves neither worn out nor replaced by "
            "failure, but on a genuine ethical disagreement with the fear-based method itself, a "
            "real institutional-health test the doctrine has not previously faced from inside its "
            "own ranks. New minor named character: Rowan Vail (a thirty-one-year decoy-line "
            "veteran under Efa Gol, collision-checked clean against the full ledger before "
            "drafting), reassigned to settlement/placement work rather than removed from "
            "continuity. Reuses Efa Gol (`CC-130`/`131`) and Garren Hask (`CC-115`/`116`). No "
            "combat. Onyx of Oblivion correctly absent per its L9 seal. First entry in wave 34."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1476",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Reef That Grew Back Wrong\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-reef-that-grew-back-wrong.md), the Scourge Alias "
            "Chronicle CI, wave 34. Age 175, V3 gear. The sub-series' first entry to address the "
            "long-term ecological cost of the crew's own operational history rather than any enemy "
            "action -- distinct from 'The Isle That Stopped Needing Him' (`MCD-814`), which showed "
            "achieved self-sufficiency, by showing instead an unglamorous cost that self-"
            "sufficiency didn't prevent and that no gear or Trinity capability can solve. Set at "
            "the already-locked Salt Keep site (`MCD-446`, age ~140) and its settlement "
            "(`MCD-545`, age ~200): decades of raid traffic and wreck debris have degraded the "
            "settlement's reef, and Kanja spends eleven days doing unglamorous manual restoration "
            "labor alongside its fishing families, unrecognized. No combat. No new named characters "
            "(the fisherman and a visiting reef-restoration elder are both deliberately unnamed). "
            "Onyx of Oblivion correctly absent per its L9 seal. Second entry in wave 34."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1477",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Coat That Went Back to Ash-Wharf\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-coat-that-went-back-to-ash-wharf.md), the Scourge "
            "Alias Chronicle CII, wave 34, closing the wave. Age 258, V4 gear. A symbolic full-"
            "circle return to Ash-Wharf (`MCD-235`/`380`), the persona's own origin site, for the "
            "first time in the sub-series' history -- a deliberately quiet, low-combat closer "
            "distinct from every prior interiority entry (`MCD-813`'s pure totaling at age 305, "
            "`MCD-830`'s and `MCD-1246`'s regret question) in that it returns physically to the "
            "place rather than only reflecting on the years. Confirms the site's rebuilding into "
            "ordinary civic life (a market square over the former bombardment ground, a rebuilt "
            "seawall) without contradicting `MCD-235`'s account of the massacre itself. No combat. "
            "No new named characters. Onyx of Oblivion correctly absent per its L9 seal. Does not "
            "touch, restage, or contradict the already-locked final night of the persona "
            "(`MCD-1022`, age 314) or its immediate approach (`MCD-1406`-`1408`). Closes wave 34 "
            "(`MCD-1475` through `MCD-1477`) and, for this run, the Scourge's Alias Chronicle "
            "output at one hundred and two total entries across thirty-four complete waves."
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
            "batch": 281,
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
