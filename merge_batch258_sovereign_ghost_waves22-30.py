#!/usr/bin/env python3
"""Batch 258: Sovereign Ghost of the Great Sea Alias Chronicle waves 22-30 (27 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Sovereign Ghost of the Great Sea's twenty-second through thirtieth Alias Chronicle waves "
    "(9 waves, 27 entries), drafted under Abad's blanket authorization to continue all eleven "
    "aliases' waves 22-30 uninterrupted. Genuinely new registers never used in the alias's prior 63 "
    "entries: an internal fever within the fleet's own crew, a crew member's betrayal under coercion "
    "(family held hostage), first contact with an unknown people past the edge of every known chart, "
    "a declined bounty resolved through the raiding's own economic root cause, a weeks-long dead calm, "
    "Efa Gol's own near-break testing her restraint doctrine against her Black Trench trauma, "
    "large-scale drought/famine relief, a previously reformed captain wrongly re-accused years later, "
    "an orphaned stowaway becoming the seed of informal fostering, combat fought through an active "
    "storm rather than around it, a rival Trust auditor's own private honest ledger, the fleet's first "
    "sea-burial rite for a natural-cause death, institutional growth (verifying distress calls after "
    "the Fleet-Marshal arc), a voluntarily surrendered prize ship, a war widow's hard accountability "
    "confrontation, a legacy visit to a now self-sufficient rescued town, Dol Maren refusing to "
    "commercialize safety knowledge, the original ledger's physical retirement and a second volume "
    "begun, a fully submerged wreck dive rescue, declining to arbitrate a succession dispute, Corren "
    "Halst declining to weaponize found corruption evidence, the fleet caught genuinely under-strength "
    "mid-refit, an anonymous benefactor's quiet reciprocity, a large unorganized reunion of rescued "
    "civilians, a captured smuggler released whole on principle, a permanent unrecovered loss at sea, "
    "and a reflective ensemble closer. One new minor named character: Mirella, a deceased cook (\"What "
    "They Buried at Sea,\" MCD-1213) -- collision-checked clean against the full ledger. No other new "
    "named characters; every other entry reuses already-locked crew (Garren Hask, Dol Maren he/him, "
    "Efa Gol she/her, Pell Ostra she/her, Danne Sok, Corren Halst, Callum Breck). Abad's approval: "
    "\"lets do this 22nd Alias Chronicle wave for any/all of the eleven aliases to the 30th wave and "
    "you are to continue uninterrupted until completion this includes rigorous testing, commit, push "
    "to main origin.\""
)

NEW_RULES = [
    {
        "id": "MCD-1202",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fever That Didn't Care About Flags\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fever-that-didnt-care-about-flags.md), Sovereign Ghost "
            "of the Great Sea Alias Chronicle LXIV, wave 22, first entry in the wave. A genuinely new "
            "register: an internal medical crisis aboard the fleet's own ship rather than a rescued or "
            "enemy vessel -- a fever traced to spoiled grain kills three crew before Efa Gol and Pell "
            "Ostra contain it, with Kanja staying aboard to sit with the sick rather than fight "
            "anything. Extends Garren Hask's ledger with a new category: deaths the fleet itself is "
            "responsible for reckoning. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1203",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Man Who Sold Their Position\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-man-who-sold-their-position.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXV, wave 22. A dark new register: a young crew member leaks "
            "fleet positions to a Trust intelligence officer after his family is taken hostage; Kanja "
            "buys the family's freedom from a Jicome debtor's hold rather than punish the informant, "
            "extending Callum Breck's own established voice on forgiveness. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1204",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Charts Couldn't Show\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-charts-couldnt-show.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXVI, wave 22, closing the wave. First contact beyond the edge "
            "of Danne Sok's own charts and beyond the Sovereign Trust conflict entirely -- an unknown "
            "island people met through Dol Maren's shipwright's craft rather than diplomacy or "
            "combat, trading freely with a fleet whose reputation means nothing to them. No new named "
            "characters. Closes wave 22."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1205",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Bounty He Wouldn't Claim\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-bounty-he-wouldnt-claim.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXVII, wave 23, first entry in the wave. A new economic "
            "register: Kanja declines a merchant guild's ten-thousand-scrip bounty to eliminate a "
            "rival pirate crew, instead tracing the raiding to the guild's own price-fixing and "
            "resolving the root cause rather than the surface conflict. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1206",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Wind That Wouldn't Come\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-wind-that-wouldnt-come.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXVIII, wave 23. A twenty-four-day dead calm strands the fleet "
            "and a rescued convoy, a pure patience/endurance test against an unbeatable natural "
            "condition; a frightened child directly questions whether the legend is even real, and "
            "Kanja answers honestly. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1207",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Vow Efa Gol Almost Broke\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-vow-efa-gol-almost-broke.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXIX, wave 23, closing the wave. A character-depth entry for "
            "Efa Gol: a parleying soldier's Black Trench unit markings nearly trigger her own restraint "
            "to break, confirmed afterward to not be one of the two men responsible for Tam Sullen's "
            "death. No new named characters. Closes wave 23."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1208",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Harbor That Starved Anyway\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-harbor-that-starved-anyway.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXX, wave 24, first entry in the wave. A new large-scale "
            "register: six weeks of pure trade logistics feed a drought-stricken harbor town with zero "
            "combat, the fleet running supply routes rather than patrol routes. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1209",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Reformed Man's Trial\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-reformed-mans-trial.md), Sovereign Ghost of the Great "
            "Sea Alias Chronicle LXXI, wave 24. Tests the restraint doctrine's long-term credibility: a "
            "captain paroled four years earlier is wrongly re-accused of an atrocity committed by an "
            "unrelated crew borrowing his old black-sail markings; Kanja clears him publicly. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1210",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Smallest Boat Carried\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-smallest-boat-carried.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXXII, wave 24, closing the wave. A warm new register: an "
            "unlisted six-year-old stowaway found aboard a seized slaver's tender, with no family to "
            "return to, becomes the seed of an informal, fleet-wide fostering practice. No new named "
            "characters. Closes wave 24."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1211",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Squall That Broke the Line\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-squall-that-broke-the-line.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXXIII, wave 25, first entry in the wave. A detailed "
            "battle-intense full-Trinity combat showcase fought through active storm conditions rather "
            "than around them, against a Trust flotilla commander exploiting the weather -- the "
            "Sovereign Eyes' overlay, Mafesto's grounding tested against combined wave and cannon "
            "impact, Obsidian Malice's sound-targeting, and Onyx of Oblivion's Whisper of Shadows and "
            "Soulbound Edge disarming rather than killing the commander. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1212",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ledger's Twin\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ledgers-twin.md), Sovereign Ghost of the Great Sea "
            "Alias Chronicle LXXIV, wave 25. Garren Hask meets a Trust auditor who has kept his own "
            "private, meticulous account of the fleet's true conduct against falsified official "
            "reports, an opposite-number parallel record-keeper rather than an informant or defector. "
            "No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1213",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What They Buried at Sea\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-they-buried-at-sea.md), Sovereign Ghost of the Great "
            "Sea Alias Chronicle LXXV, wave 25, closing the wave. The fleet's own sea-burial rite for a "
            "crew member who died of natural causes -- Mirella, a long-serving cook, aged fifty-one, "
            "the alias's first funeral for a death that isn't a mortality-gap dramatization. New minor "
            "named character: Mirella (deceased cook, no surname) -- collision-checked clean against "
            "the full ledger. Closes wave 25."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1214",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Signal They Almost Answered\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-signal-they-almost-answered.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXXVI, wave 26, first entry in the wave. A growth/adaptation "
            "callback to the Fleet-Marshal's staged distress-call ambush (MCD-954): the fleet now "
            "verifies distress calls before answering, exposing an opportunistic raiding crew's copycat "
            "rigged-hull attempt before it can spring. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1215",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Captain Who Gave Up His Ship\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-captain-who-gave-up-his-ship.md), Sovereign Ghost of "
            "the Great Sea Alias Chronicle LXXVII, wave 26. A new register: a dismasted Trust corvette "
            "captain voluntarily surrenders his ship whole, cargo and commission, rather than be "
            "captured -- the crew is freed per standard practice and the vessel becomes the fleet's "
            "unnamed fourth working ship. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1216",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Widow's Question\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-widows-question.md), Sovereign Ghost of the Great Sea "
            "Alias Chronicle LXXVIII, wave 26, closing the wave. A hard accountability register: a war "
            "widow confronts Kanja over her husband's death in \"The Captain Who Didn't Believe in "
            "Ghosts\" (MCD-774), the alias's own first reputation failure; Kanja answers with honesty "
            "rather than excuse or comfort. No new named characters. Closes wave 26."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1217",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ones Who Stayed Behind\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ones-who-stayed-behind.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXXIX, wave 27, first entry in the wave. A legacy register: "
            "Kanja revisits the undefended civilian town from \"The Night the Coast Held\" (MCD-781) "
            "to find it has since built its own watchtower, breakwater, and coastal-watch discipline, "
            "proof of lasting impact rather than a new rescue. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1218",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Storm-Chart Dol Maren Refused to Sell\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-storm-chart-dol-maren-refused-to-sell.md), Sovereign "
            "Ghost of the Great Sea Alias Chronicle LXXX, wave 27. An ethics register for Dol Maren: he "
            "turns down a merchant house's exclusive-licensing fortune for his weather-reading and "
            "hull technique, distributing the method freely instead, extending his established "
            "give-it-away pattern (MCD-771). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1219",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Night the Ledger Ran Out of Room\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-night-the-ledger-ran-out-of-room.md), Sovereign Ghost "
            "of the Great Sea Alias Chronicle LXXXI, wave 27, closing the wave. A structural/archival "
            "milestone: Garren Hask's original ledger (MCD-445) is physically completed and retired, "
            "a second volume begun aboard The Ledger with the long-serving crew present. No new named "
            "characters. Closes wave 27."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1220",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Depth They Weren't Meant to Reach\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-depth-they-werent-meant-to-reach.md), Sovereign Ghost "
            "of the Great Sea Alias Chronicle LXXXII, wave 28, first entry in the wave. A new "
            "environmental register: a fully submerged dive rescue inside a sunk wreck's flooded lower "
            "decks, stripped of gear advantage, saving four trapped survivors including two children "
            "through repeated dives alone. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1221",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Peace That Cost a Throne\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-peace-that-cost-a-throne.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXXXIII, wave 28. A new political-neutrality register: Kanja "
            "declines to lend the fleet's reputation to settle an island principality's succession "
            "dispute, instead mediating a witnessed, inclusive council that resolves it independently "
            "of the fleet's own influence. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1222",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Corren Halst Wouldn't Report\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-corren-halst-wouldnt-report.md), Sovereign Ghost of "
            "the Great Sea Alias Chronicle LXXXIV, wave 28, closing the wave. A character-depth entry "
            "for Corren Halst: he finds unrelated evidence of Trust corruption aboard a boarded ship "
            "and, given the choice, delivers it quietly to a garrison chaplain rather than use it as "
            "leverage against the Trust. No new named characters. Closes wave 28."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1223",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fleet That Wasn't Ready\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fleet-that-wasnt-ready.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXXXV, wave 29, first entry in the wave. A new vulnerability "
            "register: The Ledger is caught mid-refit and under-crewed, the other two flagships too "
            "far to reinforce, forcing an imperfect Trinity combat showcase where two raiders escape "
            "and real damage is taken -- the fleet's own vulnerability recorded honestly rather than "
            "smoothed over. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1224",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Debt Paid in Silence\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-debt-paid-in-silence.md), Sovereign Ghost of the Great "
            "Sea Alias Chronicle LXXXVI, wave 29. A reciprocity register: an anonymous benefactor, "
            "revealed to be a merchant captain freed years earlier from a Trust prison hold, quietly "
            "resupplies the fleet at unmarked points without acknowledgment or announcement. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1225",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Reunion at Ghost Harbor\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-reunion-at-ghost-harbor.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXXXVII, wave 29, closing the wave. An unorganized, large-scale "
            "gathering of rescued civilians across the alias's history convenes at Ghost Harbor, "
            "reuniting the freed slaver captives, the fisherman's daughter, the reformed captain, the "
            "self-sufficient town, and wreck survivors; Garren Hask tallies four hundred and eleven "
            "names present. No new named characters. Closes wave 29."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1226",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Last Ship They Let Go\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-last-ship-they-let-go.md), Sovereign Ghost of the Great "
            "Sea Alias Chronicle LXXXVIII, wave 30, first entry in the wave. A closing moral-throughline "
            "register: a captured medicine-smuggling blockade-runner, sympathetic and non-profiteering, "
            "is released entirely -- ship, cargo, and captain -- choosing trust over enforcement of the "
            "letter of the law. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1227",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Sea Never Gave Back\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-sea-never-gave-back.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXXXIX, wave 30. A deliberately hard, unresolved register: "
            "despite saving thirty-one of a capsized fishing fleet's crew, one young deckhand's body is "
            "never recovered after a six-hour search, the alias's first permanent loss with no "
            "confirmation of death either way. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1228",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ghost Fleet's Own Reckoning\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ghost-fleets-own-reckoning.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle XC, wave 30, closing the wave. A reflective ensemble closer: "
            "Garren Hask, Kanja, Efa Gol, and the long-serving crew review the ledger's second volume "
            "and synthesize waves 22-30's genuinely new failures, costs, and gifts of the restraint "
            "doctrine. No new named characters. Closes wave 30 and the full nine-wave run (waves 22-30, "
            "MCD-1202 through MCD-1228)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 27, f"expected 27 new rules, got {len(NEW_RULES)}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    for r in NEW_RULES:
        assert r["category"] == "kanja-alias-chronicle", f"bad category on {r['id']}: {r['category']}"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 258,
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
