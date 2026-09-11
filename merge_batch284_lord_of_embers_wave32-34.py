#!/usr/bin/env python3
"""Batch 284: Lord of Embers Alias Chronicle waves 32, 33, and 34 (9 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "Continues the Alias Chronicle sub-series' thirty-second, thirty-third, and thirty-fourth waves "
    "for the Lord of Embers, under Abad's direct authorization: \"do 3 more alias wave for all "
    "eleven.\" Wave 32 opens with a genuinely new economic register -- diffuse, untraceable "
    "debasement of the campaign's own issued trade-tokens, resolved by demoting the token to a mere "
    "receipt behind a cross-checked ledger system (MCD-1496) -- then the first real mechanical limit "
    "shown in Mafesto's core grounding function, degraded rather than disabled by waterlogged marsh "
    "terrain (MCD-1497), and closes on the alias's first active, structural diplomatic mediation "
    "between two rival settlements over a shared river, resolved through leveraged self-interest "
    "rather than deferral or force (MCD-1498). Wave 33 opens with the alias's first "
    "deliberate-capture/infiltration entry, Kanja allowing himself to be taken prisoner to surface "
    "intelligence a direct assault couldn't reach before a detailed Trinity combat showcase carries "
    "the escape (MCD-1499); a new logistics/communication register repurposing the Forge-Coat's "
    "Smoke System into a coordinated inter-site warning code, whose sudden silence -- not a signal -- "
    "saves three buried apprentices (MCD-1500); and closes on a new villain-research register, a "
    "Directorate engineer's crude reverse-engineered imitation of Mafesto catastrophically failing on "
    "its own wearer (MCD-1501). Wave 34 opens with the alias's first entry centered on Garren Hask's "
    "own aging and mortality as an ordinary human, a quiet early-warning register resolved through "
    "voluntary disclosure and a trained second set of hands (MCD-1502); a mass-evacuation showcase "
    "against a natural catastrophe (an undersea-tremor tidal surge) with zero enemy involvement, all "
    "three Trinity elements repurposed for pure evacuation logistics (MCD-1503); and closes the wave "
    "and this three-wave run on the method's independent, unprompted emergence in a village Kanja has "
    "never visited and never will, spread by circumstance and word alone with no direct teaching "
    "lineage back to him (MCD-1504). No new named characters introduced across any of the 9 entries; "
    "Garren Hask (CC-115), Ezio Valcari, and Callum Breck are all reused for continuity depth. Abad's "
    "approval: \"do 3 more alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1496",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Coin That Wouldn't Hold Its Weight\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-coin-that-wouldnt-hold-its-weight.md), Lord of Embers "
            "Alias Chronicle XCIV, first entry in the thirty-second wave. Rebellion era, age 27, the "
            "Rolling Foundry Campaign (MCD-241). A genuinely new economic register for the alias -- "
            "the campaign's own issued trade-tokens are slowly debased (shaved a sliver at a time by "
            "diffuse, untraceable civilian hands) rather than counterfeited or stolen, hurting the "
            "poorest settlements holding the most tokens hardest, with no single actor to catch or "
            "confront. Resolved not by a harder stamp but by demoting the token from currency to a "
            "mere receipt behind a cross-checked, settlement-to-settlement ledger system, extending "
            "Garren Hask's (CC-115) established ledger-keeping method into a new institutional "
            "application. Ezio Valcari appears consistent with his established documentation role. "
            "No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1497",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Marsh Wouldn't Ground\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-marsh-wouldnt-ground.md), Lord of Embers Alias "
            "Chronicle XCV, wave 32. Rebellion era, age 27, the Rolling Foundry Campaign (MCD-241). A "
            "detailed, battle-intense Trinity combat showcase in the alias's first waterlogged "
            "marshland register: a Directorate patrol picks tidal marsh ground specifically because "
            "Mafesto's Kinetic Transfer System's core grounding function degrades (not fails outright) "
            "when the ground beneath it gives rather than resists, absorbing redirected force instead "
            "of carrying it away cleanly -- a genuine, first-shown partial-efficiency limit distinct "
            "from the cold-weather heat-retention limit (MCD-1311) and the caustic-vapor gap that "
            "sidelined the system outright (MCD-1051). Kanja compensates by leaning harder on Obsidian "
            "Malice's direct discharge and Onyx of Oblivion's Cadence Ruin, which takes longer than "
            "usual to learn the marsh's irregular pulse before locating the patrol's second wave. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1498",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The River Two Villages Wouldn't Share\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-river-two-villages-wouldnt-share.md), Lord of Embers "
            "Alias Chronicle XCVI, wave 32, closing the wave. Rebellion era, age 27, the Rolling "
            "Foundry Campaign (MCD-241). A genuinely new diplomatic register for the alias: two rival "
            "settlements, locked in a generations-old dispute over a shared diversion channel, both "
            "want the campaign's forge and neither will let it be built on the other's bank. Rather "
            "than deferring to local elders (as at MCD-975) or declining to intervene in an "
            "unrelated feud (MCD-885), Kanja actively mediates through leveraged self-interest -- a "
            "forge built on a neutral moored platform at the river's center, access conditioned on "
            "the diversion channel being reopened to split flow evenly between both villages -- "
            "resolving the dispute's practical harm without pretending to resolve the underlying "
            "grievance itself. Garren Hask (CC-115) appears in his established observational role. No "
            "new named characters. Closes the Lord of Embers' thirty-second three-Chronicle wave "
            "(with \"The Coin That Wouldn't Hold Its Weight,\" MCD-1496, and \"What the Marsh Wouldn't "
            "Ground,\" MCD-1497)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1499",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Cell They Thought Would Hold Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-cell-they-thought-would-hold-him.md), Lord of Embers "
            "Alias Chronicle XCVII, first entry in the thirty-third wave. Rebellion era, age 27, the "
            "Rolling Foundry Campaign (MCD-241). The alias's first deliberate-capture/infiltration "
            "register: Kanja allows himself to be taken prisoner by a garrison patrol to surface the "
            "location of an illicit requisitioned-iron storehouse and its supply-officer operator, "
            "keeping Mafesto dormant through a patience-driven interrogation before a detailed, "
            "battle-intense Trinity combat showcase (Obsidian Malice's precision non-lethal discharge, "
            "Onyx of Oblivion's Whisper of Shadows and Veil Piercer, Mafesto grounded and current "
            "again) carries the corridor-breach escape. The storehouse's iron is recovered and its "
            "falsified ledger convicts the supply officer. Garren Hask (CC-115) appears in his "
            "established ledger-cross-checking role. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1500",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Smoke Said\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-smoke-said.md), Lord of Embers Alias Chronicle "
            "XCVIII, wave 33. Rebellion era, age 27, the Rolling Foundry Campaign (MCD-241). A "
            "genuinely new logistics/communication register: Callum Breck proposes a standardized "
            "smoke-signal relay code across the campaign's linked forge sites for early warning, "
            "repurposing the Forge-Coat gear family's established Smoke System (MCD-291-293) as "
            "coordinated inter-site signaling rather than personal concealment or terror effect. The "
            "code is tested within a week when a site's hourly all-clear pulse goes silent with no "
            "raid signal ahead of it -- the deliberately built silent-pulse protocol, not an active "
            "signal, is what actually saves three apprentices buried by a support collapse, reaching "
            "them in two hours rather than the half-day a rider would need. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1501",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What They Built From What They Saw\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-they-built-from-what-they-saw.md), Lord of Embers "
            "Alias Chronicle XCIX, wave 33, closing the wave. Rebellion era, age 27, the Rolling "
            "Foundry Campaign (MCD-241). A detailed, battle-intense Trinity combat showcase and a new "
            "villain-side-research register for the alias: a Directorate engineer builds a crude "
            "reverse-engineered imitation of Mafesto's Kinetic Transfer System from external "
            "observation alone, which catastrophically shatters its own wearer's arm on first use by "
            "feeding a blow's full charge directly into him rather than grounding it through a "
            "calibrated frame. Obsidian Malice's discharge and Onyx of Oblivion's Whisper of Shadows "
            "deny the observing engineer his notes before he can destroy or transmit them; Garren Hask "
            "(CC-115) catalogues the confiscated notebook's contents before it is burned. Distinct "
            "from the counterfeit-guild-mark arms race (MCD-1084/MCD-1316) and the doctrine-theft "
            "entry (MCD-922). No new named characters. Closes the Lord of Embers' thirty-third "
            "three-Chronicle wave (with \"The Cell They Thought Would Hold Him,\" MCD-1499, and \"What "
            "the Smoke Said,\" MCD-1500)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1502",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ledger Keeper's Slowing Hand\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ledger-keepers-slowing-hand.md), Lord of Embers Alias "
            "Chronicle C, first entry in the thirty-fourth wave. Rebellion era, age 27, the Rolling "
            "Foundry Campaign (MCD-241). The alias's first entry centered on Garren Hask's (CC-115) "
            "own aging and mortality as an ordinary human amid the campaign's long timescale: his hand "
            "begins to shake on fine ledger figures, and rather than hide it he discloses it to Kanja "
            "directly, consistent with the method's own honesty ethos. Resolved not by replacement but "
            "by training a second, steadier set of hands (an unnamed settlement clerk) to cross-check "
            "every entry alongside his own, keeping the campaign's tally as reliable as ever. Distinct "
            "from the senior smith's deliberate training bookend (MCD-887) and unplanned health-forced "
            "retirement (MCD-1312), and from Kanja's own forge-accident injury (MCD-974). No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1503",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Wave That Gave No Warning\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-wave-that-gave-no-warning.md), Lord of Embers Alias "
            "Chronicle CI, wave 34. Rebellion era, age 27, the Rolling Foundry Campaign (MCD-241). A "
            "detailed, battle-intense Trinity showcase and a genuinely new register: a mass evacuation "
            "of roughly nine hundred coastal civilians against an undersea-tremor-driven tidal surge, "
            "with zero enemy involvement and zero combat. All three Trinity elements are repurposed "
            "for pure evacuation logistics -- Mafesto's Kinetic Transfer System grounding the strain of "
            "sustained high-speed carrying rather than a blow, Obsidian Malice's discharge clearing "
            "jammed cart-tracks and a collapsed footbridge, and Onyx of Oblivion's Cadence Ruin "
            "locating trapped stragglers by rhythm rather than combat pattern. Every person on the "
            "settlement's own tally survives, the first full catastrophe in the tour to leave no gap "
            "in Garren Hask's (CC-115) ledger at all. Distinct from the tide used proactively as a "
            "weapon (MCD-880), the storm-surge flood exploited by a raid (MCD-862), and the pilgrimage "
            "crowd protected from a Directorate strike (MCD-1332). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1504",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Village He Never Reached\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-village-he-never-reached.md), Lord of Embers Alias "
            "Chronicle CII, wave 34, closing the wave and this batch's three-wave run. Rebellion era, "
            "age 27, the Rolling Foundry Campaign (MCD-241). A genuinely new register closing the run: "
            "a traveling trader reports that a village three valleys past the campaign's own furthest "
            "reach -- one Kanja will never visit during this campaign -- has independently developed "
            "open, unpaid, meritocratic smithing instruction of its own accord after a bad harvest "
            "broke its tools, entirely without direct contact, teaching, or even a name attached to "
            "the practice. Distinct from the foreign caravan's fair, reputation-blind trade (MCD-972), "
            "the disconnected-name legacy entry set generations later (MCD-1336), and the in-lineage "
            "generational-transmission entries (MCD-887, MCD-1085, MCD-1330) -- here the method "
            "spreads by circumstance and word alone, with no teaching lineage back to Kanja at all, "
            "deliberately left unconfirmed and unclaimed in the campaign's own ledger. No new named "
            "characters. Closes the Lord of Embers' thirty-fourth three-Chronicle wave (with \"The "
            "Ledger Keeper's Slowing Hand,\" MCD-1502, and \"The Wave That Gave No Warning,\" "
            "MCD-1503)."
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
            "batch": 284,
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
