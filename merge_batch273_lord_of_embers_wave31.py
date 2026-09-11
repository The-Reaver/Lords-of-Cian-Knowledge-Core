#!/usr/bin/env python3
"""Batch 273: Lord of Embers Alias Chronicle wave 31 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "The Lord of Embers' thirty-first Alias Chronicle wave, drafted under Abad's blanket "
    "authorization to continue a 31st wave for all eleven aliases. Two new registers for this "
    "alias: a natural-deprivation entry testing \"metabolizes punishment\" against an early hard "
    "freeze with no enemy involved (MCD-1415), and a flowing-water infrastructure combat showcase "
    "where a Directorate team sabotages a millrace powering trip-hammer forges (MCD-1416). Closes "
    "on the alias's first entry featuring a visiting fleet crew member from outside the campaign, "
    "Efa Gol (CC-130), reused rather than inventing a new character (MCD-1417). No new named "
    "characters introduced; Garren Hask (CC-115), Callum Breck, and Efa Gol (CC-130) all reused. "
    "Abad's approval: \"let's do a 31st alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1415",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Winter the Coal Sheds Went Empty\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-winter-the-coal-sheds-went-empty.md), Lord of Embers "
            "Alias Chronicle XCI, first entry in the thirty-first wave. Rebellion era, age 27, the "
            "Rolling Foundry Campaign (MCD-241). The alias's first entry with no enemy or sabotage "
            "involved at all -- an early, prolonged hard freeze cuts coastal coal delivery to three "
            "settlements, testing \"metabolizes punishment\" against natural deprivation rather than "
            "an act of destruction. Garren Hask tallies each settlement's exact fuel carry-forward "
            "and organizes an uneven rationing pool prioritizing the site closest to going cold; a "
            "settlement smith hoarding a private reserve releases it after his own apprentice "
            "confronts him; Kanja teaches a waste-heat-recovery technique cutting required fuel "
            "nearly a third. Extends the participatory rationing-council ethos of \"What They Agreed "
            "to Owe Each Other\" (MCD-1333) into a resource-scarcity context. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1416",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Millrace They Tried to Choke\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-millrace-they-tried-to-choke.md), Lord of Embers "
            "Alias Chronicle XCII, wave 31. A detailed, battle-intense Trinity combat showcase in "
            "the alias's first flowing-water infrastructure register: a Directorate sabotage team, "
            "spotted in advance by Callum Breck's established pattern-recognition, wedges a deliberate "
            "log-jam across the millrace powering a valley's trip-hammer forges, aiming to halt "
            "production without a direct attack. Mafesto's Kinetic Transfer System braces the "
            "wheel-house foundation against a released current surge rather than absorbing a blow; "
            "Obsidian Malice's discharge cuts the log-jam apart in controlled resonant slices rather "
            "than a blunt pulse; Onyx of Oblivion's Cadence Ruin locates the fleeing saboteurs by the "
            "wrongness of their movement against the channel's own learned rhythm, before Whisper of "
            "Shadows and Veil Piercer close the engagement. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1417",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Efa Gol Came to See\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-efa-gol-came-to-see.md), Lord of Embers Alias "
            "Chronicle XCIII, wave 31, closing the wave. Rebellion era, age 27, the Rolling Foundry "
            "Campaign (MCD-241). The alias's first entry featuring a visiting fleet crew member from "
            "outside the campaign: Efa Gol (CC-130), between decoy/diversion operations, spends three "
            "quiet, non-combat days aboard The Anvil and tells Kanja she came to see whether a thing "
            "built to outlast destruction looks different from the inside than from the decoy line "
            "that has guarded it from a distance -- explicitly tying her visit to her own Black Trench "
            "loss of pair-partner Tam Sullen and the established framing that the crew's pair-system "
            "design held, not her own individual toughness. Garren Hask appears in his established "
            "ledger role. Closes the Lord of Embers' thirty-first three-Chronicle wave (with \"The "
            "Winter the Coal Sheds Went Empty,\" MCD-1415, and \"The Millrace They Tried to Choke,\" "
            "MCD-1416). No new named characters."
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
            "batch": 273,
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
