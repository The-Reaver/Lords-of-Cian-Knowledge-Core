#!/usr/bin/env python3
"""Batch 276: Bane Alias Chronicle waves 32, 33, and 34 (9 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "Continues the Alias Chronicle sub-series' thirty-second, thirty-third, and thirty-fourth waves "
    "for Bane, under Abad's direct authorization: \"do 3 more alias wave for all eleven.\" Wave 32 "
    "opens with a tidal sea-cave extraction run entirely against a natural deadline, with Obsidian "
    "Malice withheld the whole operation on the water-safety principle established in \"What the "
    "River Carried Between Them\" (MCD-1100), then a garrison commander's wager duel fought with a "
    "plain blade and the Trinity deliberately stood down entirely -- the first time Onyx, Mafesto, "
    "and Obsidian Malice are excluded from an engagement's terms before it begins rather than limited "
    "mid-fight -- and closes on the campaign's supply-chain sabotage reaching an enemy garrison's own "
    "starving families, extending 'the fear only works if it's true' (MCD-431) to dependents rather "
    "than combatants for the first time. Wave 33 opens with the run's first hostage crisis, VB-060's "
    "'Already-Finished Negotiation' presence trait used purely defensively with zero counter-threat "
    "offered; then criminal opportunists in crude replica gear extorting merchants under Bane's name "
    "for profit, resolved through public exposure and restitution rather than violence; and closes on "
    "the sub-series' first purely celebratory, entirely conflict-free entry, Toran's (MCD-1099) "
    "wedding. Wave 34 opens with a deserted former recruit found coerced into serving the enemy, met "
    "with the same amnesty logic already extended to enemy soldiers (MCD-1102); then the run's first "
    "formal, proactive prisoner-exchange negotiation, deliberately slow and procedural rather than "
    "tense; and closes the full run on legend-drift pushed to its furthest, least controllable point "
    "-- an unverifiable uprising three provinces away invoking Bane's name, a place and people he will "
    "likely never reach or confirm. No new named characters across all nine entries -- every returning "
    "character reuses already-locked crew (Corren Halst, Danne Sok, Efa Gol, Toran); every new proper "
    "noun (none were needed for named characters or places) was collision-checked clean before "
    "drafting."
)

NEW_RULES = [
    {
        "id": "MCD-1424",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Tide That Wrote the Deadline\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-tide-that-wrote-the-deadline.md), Bane Alias "
            "Chronicle XCIV, wave 32. New environmental register: a tidal sea-cave extraction of six "
            "captured couriers, run entirely against a natural deadline (the cave mouth floods on "
            "schedule) rather than an enemy-imposed or exhaustion-driven one -- Obsidian Malice is "
            "withheld for the entire operation on the water-safety principle established in 'What the "
            "River Carried Between Them' (MCD-1100), and Mafesto's Kinetic Transfer System shows a "
            "new environmental nuance, reduced footing reliability on wet slick rock (distinct from "
            "the marsh/silt total failure of MCD-697), forcing Cadence Ruin's rock-resonance reading "
            "to carry most of the infiltration. No new named characters -- Corren Halst and Danne Sok "
            "reused. Opens wave 32."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1425",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Duel That Would Cost Nothing But Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-duel-that-would-cost-nothing-but-him.md), Bane Alias "
            "Chronicle XCV, wave 32. First entry to stage an entire engagement with the Trinity "
            "excluded from the terms before it begins rather than merely unused or malfunctioning: a "
            "garrison commander offers formal single combat, plain blade only, to decide an entire "
            "siege's outcome and spare both sides further casualties. Bane accepts on those exact "
            "terms -- Onyx sheathed, Mafesto and Obsidian Malice left with the column -- and wins "
            "through patience and Valen Sinisterblade's own training (MCD-291/292) rather than any "
            "augmented power, isolating his raw swordsmanship as the sole deciding factor for the "
            "first time since 'The Fight He Couldn't Walk Away From' (MCD-476), which still involved "
            "Onyx. The garrison surrenders whole per the wager's terms. No new named characters -- the "
            "commander is unnamed and one-scene; Corren Halst reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1426",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Enemy's Own Children Were Owed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-enemys-own-children-were-owed.md), Bane Alias "
            "Chronicle XCVI, wave 32, closing wave 32. First entry to extend 'the fear only works if "
            "it's true' (MCD-431) to the dependents of enemy soldiers rather than to enemies, "
            "civilians, or captives themselves: the same supply-chain sabotage that starved the "
            "Threshbend depot into surrender (MCD-700) is found to be reaching a garrison town's own "
            "military families, and Bane redirects captured grain to the civilian quarter over Corren "
            "Halst's strategic objection, stating the campaign's target was the garrison's capacity to "
            "fight, not its children's next meal. No new named characters -- the woman and her family "
            "are unnamed; Corren Halst and Danne Sok reused. Closes wave 32."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1427",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Hostage at the Gate\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-hostage-at-the-gate.md), Bane Alias Chronicle XCVII, "
            "wave 33. First hostage-crisis entry for this alias: a Directorate officer holds three "
            "civilians at a garrison gate, demanding Bane present himself alone, unarmed, and "
            "ungeared before an execution deadline. Bane complies, going in with Onyx sheathed and no "
            "blade, and dramatizes VB-060's 'Already-Finished Negotiation' presence trait used with "
            "zero counter-threat, demand, or leverage offered at all -- the officer's own resolve "
            "erodes against a man who gives him nothing to react against, and releases all three "
            "hostages unharmed. No new named characters -- the officer, shopkeeper, old man, and child "
            "are unnamed; Corren Halst and Danne Sok reused. Opens wave 33."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1428",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Impersonator's Price\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-impersonators-price.md), Bane Alias Chronicle XCVIII, "
            "wave 33. First impersonation-for-profit entry: five criminal opportunists in crude "
            "replica Trinity-style gear extort a fifth of every wagon's goods from merchants on a "
            "trade road, invoking Bane's name for material gain -- distinct from the honest "
            "misattributed rumor of 'The Rumor He Never Corrected' (MCD-681), the Directorate's own "
            "fabricated propaganda in 'The Story They Wanted to Be True' (MCD-1098), and the "
            "consensual name-borrowing request of 'The Name They Wanted to Borrow' (MCD-934). Bane "
            "and crew expose the fraud publicly in the same market square, forcing restitution and a "
            "public confession rather than executing them. No new named characters -- the "
            "impersonators, caravan master, and merchants are unnamed; Efa Gol reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1429",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Wedding at the Waystation\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-wedding-at-the-waystation.md), Bane Alias Chronicle "
            "XCIX, wave 33, closing wave 33. Bane's first purely celebratory, entirely "
            "conflict-free entry: Toran (already locked, MCD-1099) marries a woman from a settlement "
            "freed three months earlier, and the column halts a full evening for the ceremony, with "
            "Bane standing as witness at Toran's request. No tactical, combat, or gear dimension of "
            "any kind -- distinct from every prior warm/personal register in the run, all of which "
            "still carried the war's weight directly in the scene. No new named characters -- the "
            "bride is deliberately left unnamed; Toran, Efa Gol, Danne Sok, and Corren Halst reused. "
            "Closes wave 33."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1430",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The One Who Walked the Other Way\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-one-who-walked-the-other-way.md), Bane Alias Chronicle "
            "C, wave 34. First desertion-in-reverse entry: a fighter recruited under Bane's own "
            "command deserts after a brutal engagement, coerced by a Directorate threat against his "
            "family, and is later found serving the garrison Bane's column is besieging. Recognized "
            "mid-engagement, Bane pulls him from the fight rather than killing or condemning him and "
            "arranges safe passage for him and his family out of the region, extending the amnesty "
            "logic of 'The Garrison He Let Walk' (MCD-1102) to a coerced deserter from his own ranks "
            "for the first time -- deliberately leaves some fighters' discomfort at his return "
            "unresolved. No new named characters -- the deserter and his family are unnamed; Corren "
            "Halst and Danne Sok reused. Opens wave 34."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1431",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Trade Neither Side Trusted\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-trade-neither-side-trusted.md), Bane Alias Chronicle "
            "CI, wave 34. First formal, proactive prisoner-exchange negotiation for this alias: three "
            "captured Directorate officers traded for eleven held rebels through a neutral "
            "trade-broker intermediary at a designated crossing, distinct from the reactive tribunal "
            "defense of 'The Council That Asked Him to Speak Plainly' (MCD-939) or any unilateral "
            "mercy-driven release. Deliberately staged as slow and procedural (individual verification, "
            "double counting, four hours to move fourteen people) rather than tense or "
            "combat-adjacent, testing patience and process over force or presence. No new named "
            "characters -- the broker and the Directorate escort commander are unnamed and one-scene."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1432",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Story That Outran Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-story-that-outran-him.md), Bane Alias Chronicle CII, "
            "wave 34, closing wave 34 and the thirty-second through thirty-fourth wave run. A trader "
            "mentions, in passing, an unverified small uprising three provinces away invoking Bane's "
            "name, in a region he has never visited and has no way to reach, confirm, or correct -- "
            "extends the legend-drift theme of 'The Song They Sang Without Knowing Whose It Was' "
            "(MCD-1108) and 'The Impersonator's Price' (MCD-1428) into its furthest, least "
            "controllable form, deliberately left permanently unresolved. No new named characters -- "
            "the trader is unnamed and one-scene; Efa Gol and Corren Halst reused. Closes wave 34."
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
            "batch": 276,
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
