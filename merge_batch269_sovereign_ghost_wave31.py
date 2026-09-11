#!/usr/bin/env python3
"""Batch 269: Sovereign Ghost of the Great Sea Alias Chronicle wave 31 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "The Sovereign Ghost of the Great Sea's thirty-first Alias Chronicle wave, drafted under Abad's "
    "blanket authorization to continue a 31st wave for all eleven aliases. Three genuinely new "
    "registers for this alias: a detailed full-Trinity combat showcase fought on foot across "
    "refrozen pack ice rather than ship-to-ship, when raiders exploit an early freeze to trap The "
    "Receipt and a supply tender ('The Channel the Ice Sealed Shut'); Callum Breck personally ending "
    "a standoff alone and unarmed through his own rebuilt voice rather than through Kanja or the "
    "Trinity, extending his already-locked voice-recovery arc into direct field leadership for the "
    "first time ('The Voice That Ended It Without a Blow'); and the fleet's reputation weaponized as "
    "unauthorized political propaganda by both sides of a distant conflict it has no actual part in, "
    "resolved by Kanja publicly refusing both endorsements ('The War That Wore Their Name'). No new "
    "named characters -- all three entries reuse already-locked crew (Garren Hask, Danne Sok, Callum "
    "Breck, Efa Gol). Zero proper-noun collisions found on pre-draft checks. Abad's approval: "
    "\"let's do a 31st alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1403",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Channel the Ice Sealed Shut\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-channel-the-ice-sealed-shut.md), Sovereign Ghost of "
            "the Great Sea Alias Chronicle XCI, wave 31, first entry in the wave. A new environmental "
            "register: a detailed full-Trinity combat showcase fought entirely on foot across "
            "refrozen pack ice rather than ship-to-ship, when raiders exploit an early freeze "
            "trapping The Receipt and a supply tender in a sealed channel -- Mafesto's Kinetic "
            "Transfer System reading hull vibration through ice, the Sovereign Eyes' Blueprint Eye "
            "overlay mapping ice thickness, the Ironfall Boots' grip-plating, a precision Obsidian "
            "Malice application fracturing ice underfoot, and Onyx of Oblivion's Whisper of Shadows "
            "and Soulbound Edge. Zero deaths on either side. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1404",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Voice That Ended It Without a Blow\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-voice-that-ended-it-without-a-blow.md), Sovereign "
            "Ghost of the Great Sea Alias Chronicle XCII, wave 31. A new register: Callum Breck "
            "boards a cornered slaver captain's ship alone and unarmed, ending a standoff over sixty "
            "chained captives through his own rebuilt voice rather than through Kanja or the Trinity "
            "-- the first entry in the fleet's recorded history resolved entirely by someone other "
            "than Kanja, extending Breck's already-locked voice-recovery arc (CC-116, MCD-397, "
            "MCD-542) into direct field leadership. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1405",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The War That Wore Their Name\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-war-that-wore-their-name.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle XCIII, wave 31, closing the wave. A genuinely new register: "
            "the fleet's reputation is invoked as unauthorized political propaganda by both sides of "
            "a distant civil conflict it has no actual part in; Kanja travels alone to publicly "
            "refuse both endorsements, distinct from the wave-28 political-neutrality mediation "
            "(MCD-1221), which the fleet was invited into rather than falsely claimed for. No new "
            "named characters. Closes wave 31 (MCD-1403 through MCD-1405)."
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
            "batch": 269,
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
