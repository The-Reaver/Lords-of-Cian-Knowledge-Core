#!/usr/bin/env python3
"""Batch 249: Lord of Embers Alias Chronicle wave 21 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Lord of Embers Alias Chronicle wave 21 (LXI-LXIII), three entries continuing the highest "
    "prior numeral (LX, wave 20, MCD-1052). \"The Collapse They Meant to Cause\" (MCD-1083) is the "
    "wave's detailed, battle-intense Trinity combat showcase per standing craft instruction: the "
    "alias's first underground setting, a sabotaged ore-drift collapse timed to a coordinated "
    "surface ambush, resolved with Mafesto's grounding/conductance function applied to structural "
    "load-bearing, Obsidian Malice used for controlled precision demolition, and Onyx of Oblivion's "
    "Cadence Ruin used for the first time to locate trapped people by rhythm through stone, "
    "followed by Whisper of Shadows and Veil Piercer on the surface -- distinct from the Trench "
    "Monarch's own established mine-rescue precedent (MCD-636) by its deliberate sabotage and "
    "split-front shape. \"The Standard They Learned to Fake\" (MCD-1084) shows a genuinely new "
    "register of limit for 'metabolizes punishment' distinct from wave 20's collateral-harm shape "
    "(MCD-1050): counterfeiters exploiting the Open-Forge Standard's own legitimacy (MCD-1052) with "
    "faked tools already scattered and unrecallable across settlements, a diffuse reputational harm "
    "no rebuild speed can retrace, left honestly unresolved as a harder counter-mark is itself shown "
    "starting to be faked in turn. \"What Left the Forge and Kept Going\" (MCD-1085) closes the wave "
    "on a legacy beat directly extending \"The Boy Who Refused the Forge\" (MCD-884, wave 13), "
    "returning to that unnamed apprentice decades later as an established healer training his own "
    "apprentices under the same open-teaching method, proving the doctrine transferable beyond "
    "blacksmithing entirely. Collision-checked before drafting: no new named characters introduced "
    "in any of the three entries (all antagonists/officials/returning figures are unnamed and "
    "one- or two-scene, matching established convention); all reused already-locked elements "
    "(Mafesto, Obsidian Malice, Onyx of Oblivion and its five named powers, the Rolling Foundry "
    "Campaign's core facts per MCD-241, the recurring senior smith's successor per MCD-923/MCD-1052, "
    "and the unnamed healer-apprentice per MCD-884) confirmed against the live ledger with zero "
    "collisions. Abad's approval: \"another alias wave of all aliases\"."
)

NEW_RULES = [
    {
        "id": "MCD-1083",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Collapse They Meant to Cause\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-collapse-they-meant-to-cause.md), the Lord of Embers "
            "Alias Chronicle LXI, first entry in the twenty-first wave. Rebellion era, age 27, the "
            "Rolling Foundry Campaign (MCD-241), one of the marginal reopened ore drifts from the "
            "embargo (MCD-456). A detailed, battle-intense Trinity combat showcase: a Directorate "
            "demolitions specialist sabotages a support beam to seal eleven apprentices into a dead-end "
            "gallery, timed forty minutes ahead of a coordinated surface ambush on the ore-weighing "
            "terrace, expecting the floor's attention to be fully consumed underground. Kanja resolves "
            "both fronts inside fifteen minutes -- Mafesto's Kinetic Transfer System grounding the "
            "straining prop timber's shifting load rather than absorbing a blow, Obsidian Malice "
            "shearing the rubble choke point apart in controlled resonant pulses rather than a blunt "
            "discharge, and Onyx of Oblivion's Cadence Ruin locating the trapped apprentices by rhythm "
            "through stone for the first time, before Whisper of Shadows and Veil Piercer close the "
            "surface ambush. The demolitions specialist, taken alive, had correctly predicted Kanja "
            "would have to choose between the two fronts and simply misjudged how fast the first half "
            "could be resolved. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1084",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Standard They Learned to Fake\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-standard-they-learned-to-fake.md), the Lord of Embers "
            "Alias Chronicle LXII, wave 21. Rebellion era, age 27, the Rolling Foundry Campaign "
            "(MCD-241), some months after the Open-Forge Standard's institutionalization (MCD-1052). "
            "A genuinely new register of limit for 'metabolizes punishment': counterfeiters stamp a "
            "near-match of the Open-Forge Standard's guild seal onto substandard tools and sell them "
            "as genuine across several settlements, causing real injuries; unlike every prior "
            "punishment the floor has answered, the harm has no single location, cart, or forge left "
            "to march toward -- the counterfeit tools are already scattered and in daily use beyond "
            "the campaign's reach, unrecallable. Kanja issues a harder counter-mark through the guild "
            "council and covers proven-genuine-belief losses from campaign stores, but neither reaches "
            "backward to the harm already done, and within a season a second forger has already begun "
            "faking the harder mark too -- left honestly unresolved rather than cleanly fixed. The "
            "senior smith's successor (MCD-923, MCD-1052) appears consistently with her established "
            "role. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1085",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Left the Forge and Kept Going\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-left-the-forge-and-kept-going.md), the Lord of Embers "
            "Alias Chronicle LXIII, wave 21, closing the wave. Set decades after the Rolling Foundry "
            "Campaign (MCD-241), during the Long Mask era. A legacy beat directly extending 'The Boy "
            "Who Refused the Forge' (MCD-884, wave 13): Kanja visits the same unnamed apprentice, now "
            "an established healer with his own two apprentices, who reveals he carried forward not "
            "the smithing craft but the open-teaching principle itself -- asking a student what they "
            "actually want to build and teaching toward that answer rather than pressing skill into a "
            "prescribed shape -- applying it successfully to training healers rather than smiths, "
            "proving the Lord of Embers' method was always transferable beyond blacksmithing. No new "
            "named characters; the healer and his two apprentices are unnamed, matching MCD-884's own "
            "convention. Closes the Lord of Embers' twenty-first three-Chronicle wave (with 'The "
            "Collapse They Meant to Cause,' MCD-1083, and 'The Standard They Learned to Fake,' "
            "MCD-1084)."
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
            "batch": 249,
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
