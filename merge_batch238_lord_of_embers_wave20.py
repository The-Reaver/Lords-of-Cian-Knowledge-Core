#!/usr/bin/env python3
"""Batch 238: Lord of Embers Alias Chronicle wave 20 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Lord of Embers Alias Chronicle wave 20 (LVIII-LX), three entries continuing the highest prior "
    "numeral (LVII, wave 19, MCD-977). \"What the Slag Left Behind\" (MCD-1050) shows a genuinely new "
    "register of limit for 'metabolizes punishment': collateral harm the campaign's own industrial "
    "scale caused (slag runoff poisoning a downstream farm's irrigation, unrelated to any enemy "
    "action), with a real, permanently unrecovered cost (a ruined season's crop) the floor's rebuild "
    "ethos cannot reach backward to undo. \"What the Trinity Couldn't Absorb\" (MCD-1051) is the "
    "wave's detailed, battle-intense Trinity combat showcase per standing craft instruction: a "
    "Directorate engineer engineers a non-kinetic caustic-vapor weapon specifically to defeat "
    "Mafesto's Kinetic Transfer System, the first genuine mechanical gap shown in that system, "
    "resolved through blacksmith's terrain knowledge and Onyx of Oblivion's blade work (Whisper of "
    "Shadows, Veil Piercer) rather than gear supremacy, with Obsidian Malice deliberately withheld "
    "because using it would worsen the threat. \"The Standard They Wrote Into the Books\" (MCD-1052) "
    "closes the wave on a fresh guild/economic-recognition register distinct from prior guild "
    "entries: a regional smiths' guild formally institutionalizes the campaign's open-method "
    "rebuild-and-teach doctrine into an examinable journeyman certification standard entered under no "
    "alias's name, paying forward the already-established recurring senior smith's successor "
    "(MCD-923) into a formal institutional role for the first time. Collision-checked before "
    "drafting: no new named characters introduced in any of the three entries (all antagonists/"
    "officials are unnamed and one-scene, matching established convention); all reused already-"
    "locked elements (Mafesto, Obsidian Malice, Onyx of Oblivion and its five named powers, The "
    "Anvil, the recurring senior smith and her successor, the Rolling Foundry Campaign's core facts "
    "per MCD-241) confirmed against the live ledger before use. Abad's approval: \"doorway for all "
    "the aliases that remain\" (approval of Bane's individually-presented wave 20 plus blanket "
    "authorization to continue the same wave for the remaining ten aliases)."
)

NEW_RULES = [
    {
        "id": "MCD-1050",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Slag Left Behind\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-slag-left-behind.md), the Lord of Embers Alias "
            "Chronicle LVIII, first entry in the twentieth wave. Rebellion era, age 27, the Rolling "
            "Foundry Campaign (MCD-241). Six weeks of heavy salvage-smelting sends slag runoff into "
            "an unrelated downstream farm's irrigation channel, souring a season's crop with no enemy "
            "and no rebuild target involved -- a genuinely new register of limit for 'metabolizes "
            "punishment': harm the campaign's own industrial scale caused rather than absorbed, which "
            "no rebuild speed can reach backward to undo. Kanja voluntarily halts the site's smelting "
            "for four days, has apprentices cut a diversion trench and lime-treatment basin, and pays "
            "the ruined harvest's cost from campaign stores rather than pretend it was rebuilt. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1051",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Trinity Couldn't Absorb\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-trinity-couldnt-absorb.md), the Lord of Embers "
            "Alias Chronicle LIX, wave 20. Rebellion era, age 27, the Rolling Foundry Campaign. A "
            "detailed, battle-intense Trinity combat showcase: a Directorate engineer engineers a "
            "caustic-vapor weapon specifically because it carries no kinetic force, defeating "
            "Mafesto's Kinetic Transfer System outright -- the first genuine mechanical gap shown in "
            "that system across the alias's full run. Kanja deliberately withholds Obsidian Malice "
            "(a discharge would ignite the vapor cloud rather than disperse it) and instead breaks a "
            "diversion-channel berm with Onyx of Oblivion to flood the terrace and drown the cloud in "
            "river water, then closes on the exposed delivery team with Onyx's Whisper of Shadows and "
            "Veil Piercer. The captured engineer's own report concludes the gap was real but "
            "irrelevant, since the floor's protection was never the gear alone. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1052",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Standard They Wrote Into the Books\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-standard-they-wrote-into-the-books.md), the Lord of "
            "Embers Alias Chronicle LX, wave 20, closing the wave. Rebellion era, age 27, the Rolling "
            "Foundry Campaign. A regional smiths' guild council formally institutionalizes the "
            "campaign's open-method rebuild-and-teach doctrine as the 'Open-Forge Standard,' an "
            "examinable journeyman certification entered into guild law under no alias's name and "
            "requiring no candidate ever meet Kanja -- economic/institutional legitimization distinct "
            "from prior guild entries (personal exclusion overturned, a formal judged craft contest, "
            "a suppressed rebuild-speed report). The recurring senior smith's already-established "
            "successor (MCD-923), whose own testimony to the council prompted the delegation, is "
            "honored with authorship of the standard and declines to name it after herself, insisting "
            "it be named for what it does. Closes the Lord of Embers' twentieth three-Chronicle wave "
            "(with 'What the Slag Left Behind,' MCD-1050, and 'What the Trinity Couldn't Absorb,' "
            "MCD-1051). No new named characters."
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
            "batch": 238,
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
