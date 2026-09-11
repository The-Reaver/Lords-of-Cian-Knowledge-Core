#!/usr/bin/env python3
"""Batch 241: Bane Alias Chronicle wave 21 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Locks Bane Alias Chronicles LXI-LXIII, wave 21: \"The Night His Judgment Slipped\" (MCD-1059), "
    "the first entry to locate a genuine failure inside Bane's own sustained exhaustion rather than "
    "bad intelligence, external caution, a broken promise, or a Trinity/gear limitation -- his own "
    "judgment degrades over eleven sleepless days, caught by Corren Halst and Danne Sok before it "
    "costs a harvest crew their lives, resulting in a standing rule that no operational plan, "
    "including his own, runs past the fourth sleepless night without a second set of eyes; \"The "
    "Twelve Miles That Never Stopped Moving\" (MCD-1060), a detailed full-Trinity combat showcase "
    "built around continuous motion rather than a held position -- a six-hundred-refugee convoy "
    "defended across twelve miles and three changing terrains without the column ever slowing below "
    "a walk, distinct from every prior fortified/siege/vertical/precision/ravine showcase; and \"The "
    "Weight Maret Vos Chose to Carry\" (MCD-1061), closing the wave, a payoff to wave 18's \"What He "
    "Couldn't Be in Two Places For\" (MCD-938) giving Maret Vos his own dedicated reflective "
    "perspective within Bane's own run for the first time, distinct from his earlier-crew trilogy "
    "entries already locked under the Trench Monarch and Captain aliases. New location: the Amitane "
    "flats (collision-checked, zero prior hits), thinly described and non-recurring. No new named "
    "characters anywhere in the wave -- Corren Halst, Danne Sok, Maret Vos (he/him, per the Batch 226 "
    "reconciliation), and Efa Gol all reused. Abad's approval: \"another alias wave of all aliases\"."
)

NEW_RULES = [
    {
        "id": "MCD-1059",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Night His Judgment Slipped\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-night-his-judgment-slipped.md), Bane Alias Chronicle "
            "LXI, wave 21. Rebellion era, within the \"Bane\" window -- not a territory Chronicle. "
            "Eleven days into holding three simultaneous operations open without a full night's "
            "sleep, Bane lays out a night-crossing route through a grain village's fields that he "
            "would, on any other night, have reflexively checked for late harvest crews still working "
            "after dark -- and doesn't, without noticing he hasn't. Danne Sok catches the omission by "
            "habit rather than suspicion (\"You always check the fields\"); a runner sent ahead in "
            "place of the column confirms thirty harvesters would have been directly in the route's "
            "path. The first entry to locate a genuine failure inside Bane's own sustained exhaustion "
            "rather than bad intelligence (MCD-682), external caution (\"What the Delay Cost\"), a "
            "broken promise (MCD-706), or any Trinity/gear limitation -- Onyx of Oblivion's own "
            "senses tell him nothing about a blind spot inside his own judgment. Corren Halst orders "
            "him to sleep nine hours on flat authority rather than Bane's own say-so; the column runs "
            "competently without him. Results in a new standing order, applied to himself for the "
            "first time by his own admission: no one, including Bane, runs an operational plan past "
            "the fourth consecutive sleepless night without a second set of eyes reviewing it who "
            "isn't as tired as he is. No new named characters -- Corren Halst, Danne Sok, and Maret "
            "Vos reused. New location: the Amitane flats, collision-checked clean, thinly described "
            "and non-recurring. Opens wave 21."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1060",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Twelve Miles That Never Stopped Moving\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-twelve-miles-that-never-stopped-moving.md), Bane "
            "Alias Chronicle LXII, wave 21. Rebellion era, within the \"Bane\" window -- not a "
            "territory Chronicle. A detailed full-Trinity combat showcase built around continuous "
            "motion rather than a held position: a six-hundred-refugee convoy, a wounded rearguard, "
            "and a pursuing Directorate cavalry screen force a twelve-mile defense across three "
            "changing terrains without the column's pace ever dropping below a walk, since stopping "
            "to fight properly would win the battle but cost the two remaining daylight hours needed "
            "to reach the border crossing. Across open grassland, Mafesto's Kinetic Transfer System "
            "redirects charging cavalry's own momentum sideways through Bane's footing mid-stride, "
            "dropping horse and rider without a halt in the column's march. Through a close pine "
            "stand, Onyx of Oblivion's Cadence Ruin folds an infantry bottleneck attempt apart before "
            "it reaches striking range while Veil Piercer picks two disguised scouts out of a "
            "civilian-looking knot mid-stride. Along a final exposed causeway, Obsidian Malice's "
            "two-year dormant charge is released in one arcing discharge timed to the pursuing "
            "commander's committed final push, delivered without Bane breaking stride to aim it. The "
            "column crosses the border zone an hour before dusk having never once formed up to fight "
            "from fixed ground. Distinguished from every prior full-Trinity showcase (the fortified-"
            "garrison assault, MCD-373; the multi-day siege, MCD-379; the vertical battlement fight, "
            "MCD-935; the precision-constrained bridge defense, MCD-1026; and the most-intense ravine "
            "battle, MCD-1013) by its continuous-motion constraint, requiring all three Trinity "
            "pieces to operate at pace across shifting terrain in one unbroken line of march rather "
            "than from a held position. No new named characters -- Efa Gol reused; the pursuing "
            "Directorate commander is unnamed and one-scene. Second entry in wave 21."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1061",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Weight Maret Vos Chose to Carry\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-weight-maret-vos-chose-to-carry.md), Bane Alias "
            "Chronicle LXIII, closing wave 21. Rebellion era, within the \"Bane\" window -- not a "
            "territory Chronicle. Direct payoff to wave 18's \"What He Couldn't Be in Two Places For\" "
            "(MCD-938), which established Bane splitting the column and trusting Maret Vos (already "
            "locked, he/him per the Batch 226 pronoun reconciliation) to run an interception alone. "
            "Three weeks later, Maret Vos privately admits he spent the operation's first hour waiting "
            "for Bane to arrive and take the plan back, and had deliberately set the ambush closer to "
            "the road than necessary to leave room for that. Bane confirms he saw the same tell in the "
            "plan's own positioning and chose not to say anything beforehand, stating the distinction "
            "plainly: Maret Vos didn't need his plan fixed, he needed to find out for himself that he "
            "didn't need Bane to fix it, and only the second was Bane's to give. Gives Maret Vos his "
            "own dedicated reflective perspective within Bane's own run for the first time, distinct "
            "from his already-locked earlier-crew trilogy entries under the Trench Monarch (\"What "
            "Maret Vos Carried From Before\") and Captain (\"The Night Maret Vos Almost Walked\") "
            "aliases, neither of which this entry repeats or restages. No new named characters -- "
            "Maret Vos, Bane, Corren Halst, and Danne Sok reused. Closes wave 21."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 3, f"expected 3 new rules, got {len(NEW_RULES)}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 241,
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
