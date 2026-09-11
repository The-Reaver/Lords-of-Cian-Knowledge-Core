#!/usr/bin/env python3
"""Batch 245: Sovereign Ghost of the Great Sea Alias Chronicle wave 21 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Sovereign Ghost of the Great Sea Alias Chronicle wave 21 (Chronicles LXI-LXIII), three "
    "genuinely new registers for this alias: a fireship-ambush Trinity/gear combat showcase "
    "highlighting the Sovereign Eyes, Breath Collar, and Ironfall Boots alongside Mafesto/Obsidian "
    "Malice/Onyx of Oblivion; the restraint-over-fear doctrine turned inward on the fleet's own crew "
    "for the first time (a theft investigated and resolved through accountability and reintegration "
    "rather than banishment or the lash); and a burial rite performed for enemy Trust dead recovered "
    "from a storm wreck, extending Garren Hask's true-record ledger principle to enemy dead. No new "
    "named characters were introduced; all three entries reuse already-locked crew (Dol Maren, "
    "he/him; Pell Ostra; Efa Gol; Garren Hask). Zero proper-noun collisions found on pre-draft "
    "checks. Abad's approval: \"another alias wave of all aliases\"."
)

NEW_RULES = [
    {
        "id": "MCD-1071",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Night the Water Burned\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-night-the-water-burned.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXI, wave 21, first entry in the wave. A detailed naval "
            "Trinity combat showcase against a fireship ambush -- six burning, pitch-packed hulks "
            "released on a timed tide into a narrow strait to trap the convoy The Ledger is "
            "escorting -- combining Mafesto's Kinetic Transfer System (redirecting a collapsing "
            "burning spar off a convoy deck), Obsidian Malice (severing two staged tow-cables to "
            "break one converging trap into six separate, survivable problems), the Sovereign Eyes' "
            "Blueprint Eye overlay (MCD-289/ARS-350, rendering six drift vectors clean through smoke "
            "and glare faster than unaided sight could track them), the Breath Collar's filtration "
            "function (ARS-351, holding smoke out of Kanja's own lungs through the boarding), the "
            "Ironfall Boots' stomp-tremor (ARS-353, downing two boarders exploiting the chaos), and "
            "Onyx of Oblivion's Whisper of Shadows and Soulbound Edge (boarding the nearest hulk "
            "through smoke to cut its lashed tiller and haul it off heading by hand). The convoy "
            "survives scorched but whole, no lives lost either side; the fireships' attackers are "
            "deliberately left unidentified, a loose thread rather than resolved here. Not a "
            "territory Chronicle."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1072",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Debt Kept Inside the Crew\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-debt-kept-inside-the-crew.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LXII, wave 21. A genuinely new register for this alias: the "
            "restraint-over-fear doctrine tested against the fleet's own crew rather than an enemy, "
            "when a young rigger (unnamed) is traced by Garren Hask -- extending his established "
            "true-record ledger role (MCD-445) into internal investigation for the first time -- to "
            "the theft of a silver ring and a sum of coin from a rescued family's recovered effects. "
            "Rather than the lash or banishment the crew's older hands expect, Kanja orders "
            "restitution and repayment through logged labor, resolving it through accountability and "
            "reintegration rather than mercy toward an opponent -- distinct from every prior external "
            "application of the doctrine (paroling clerks, releasing conscripts, sparing "
            "impersonators) and distinct from \"The Hand That Chose to Leave\" (MCD-955, wave 18), "
            "which resolved a doctrinal disagreement through a respectful parting rather than an "
            "internal wrongdoing. The rigger remains aboard, trusted again, six months on. Not a "
            "territory Chronicle."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1073",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Rites They Gave the Drowned\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-rites-they-gave-the-drowned.md), Sovereign Ghost of "
            "the Great Sea Alias Chronicle LXIII, wave 21, closing the wave. A quiet mourning "
            "register never used in this alias's prior 62 entries: after a Trust patrol pursuing the "
            "fleet is sunk by a squall rather than by combat, Kanja orders all eleven men recovered "
            "from the wreck -- seven dead, four living -- and personally performs a full burial rite "
            "over the dead, extending the restraint-over-fear doctrine to enemies who are already "
            "dead, where no strategic or reputational benefit is possible, over Efa Gol's initial "
            "objection that the fleet owes them nothing. Garren Hask logs all eleven names, recovered "
            "from a single surviving log-book, in the same ledger that already holds disabled hulls, "
            "freed captives, and (per MCD-1072, this same wave) a crewman's own repaid debt, "
            "extending the established true-record principle (MCD-445) to enemy dead for the first "
            "time. The four survivors are returned to the nearest Trust garrison under escort. Not a "
            "territory Chronicle."
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
            "batch": 245,
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
