#!/usr/bin/env python3
"""Batch 244: Blue-Collar Titan Alias Chronicle wave 21 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Blue-Collar Titan Alias Chronicle wave 21 (MCD-1068 through MCD-1070, LXI-LXIII): three "
    "genuinely new registers not covered in the alias's prior twenty waves. \"No Smell, No Smoke, "
    "No Sound\" is the alias's first asphyxiant/toxic-vapor hazard entry, a detailed full-Trinity "
    "rescue showcase deliberately contrasted against wave 20's fire/arson opener (MCD-1035) -- a "
    "heavier-than-air gas must be displaced downward rather than vented upward, and Obsidian "
    "Malice is deliberately withheld due to spark risk, forcing a new application of Onyx of "
    "Oblivion's Soulbound Edge and a new density/weight-reading register for Mafesto. \"What Her "
    "Hands Already Knew\" is the alias's first advocacy/sponsorship mentorship entry -- Kanja uses "
    "his own earned guild standing to get an unlicensed stonemason a fair competence test rather "
    "than vouching for her directly, deliberately set with a separate stonemasons' guild charter "
    "from the already-locked smiths' guild (MCD-409/MCD-539) to avoid any contradiction. \"The Day "
    "the Diggers Set Down Their Tools\" places Kanja on the authority side of a wage dispute with "
    "his own hired crew for the first time in the alias's run, resolved by his explicit rejection "
    "of that structural position, reusing Garren Hask's established ledger-keeper role (CC-115). "
    "No new named characters were introduced -- all newly-appearing figures (the mucker, the "
    "stonemason, the stonemasons' elder) are deliberately unnamed one-scene characters, "
    "collision-checked clean against the full ledger, consistent with this alias's established "
    "precedent for minor one-scene figures. Abad's approval: \"another alias wave of all aliases\"."
)

NEW_RULES = [
    {
        "id": "MCD-1068",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"No Smell, No Smoke, No Sound\" (full narrative text at "
            "docs/lords-of-cian/chronicles/no-smell-no-smoke-no-sound.md), the Blue-Collar Titan "
            "Alias Chronicle LXI, wave 21, first entry. The alias's first asphyxiant-vapor hazard "
            "entry: Directorate agents reopen an old sealed gallery to release a colorless, "
            "odorless, heavier-than-air vapor into a working gallery of twenty-one laborers, a "
            "hazard that kills silently by displacement rather than by fire, water, or collapse. A "
            "detailed full-Trinity rescue showcase deliberately distinct from every prior crisis "
            "register for this alias, most directly wave 20's fire/arson opener (MCD-1035, 'What "
            "the Smoke Was Hiding') -- venting a heavier-than-air gas requires displacing it "
            "downward and out through a low drain rather than venting it upward the way smoke is "
            "vented, and Obsidian Malice's usual discharge is deliberately withheld throughout "
            "given spark risk against trapped mineral vapor. Introduces a new density/weight-based "
            "sensing register for Mafesto's Kinetic Transfer System (ARS-010) and a new precision-"
            "cutting application of Onyx of Oblivion's Soulbound Edge in place of a forceful "
            "strike, opening the low ventilation path without spark or percussion, while Cadence "
            "Ruin and Veil Piercer clear the posted guards. All twenty-one laborers survive. "
            "Reuses already-locked crew members Corren Halst and Danne Sok. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1069",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Her Hands Already Knew\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-her-hands-already-knew.md), the Blue-Collar Titan "
            "Alias Chronicle LXII, wave 21, second entry. A cross-barrier mentorship entry distinct "
            "from every prior teaching/guild register for this alias -- 'The Guild Master's Test' "
            "(MCD-409) and 'The Guild That Made Him One of Their Own' (MCD-539), both about "
            "Kanja's own admission and testing, and the direct-instruction entries (MCD-657, "
            "MCD-653, MCD-1036). An unlicensed stonemason has diagnosed load-bearing structural "
            "work under her late father's license for six years, barred from principal licensure "
            "of her own by the stonemasons' guild charter -- a separate guild from the already-"
            "locked smiths' guild of MCD-409/MCD-539, deliberately kept distinct to avoid "
            "contradicting that guild's established unnamed woman guild master. Rather than vouch "
            "for her personally, Kanja insists the stonemasons' guild test her by its own genuine "
            "competence standard, exactly as he himself was tested; she diagnoses a structural "
            "fault three of the guild's own certified journeymen had missed and is licensed on the "
            "strength of that diagnosis alone. Extends the alias's core 'competence, not "
            "reputation' ethos from a new angle -- using earned standing to open a barrier for "
            "someone else rather than crossing one himself. The stonemason and the stonemasons' "
            "elder are new, deliberately unnamed one-scene characters (collision-checked: no named "
            "stonemason or second guild of this kind exists elsewhere in the ledger). No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1070",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Day the Diggers Set Down Their Tools\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-day-the-diggers-set-down-their-tools.md), the "
            "Blue-Collar Titan Alias Chronicle LXIII, wave 21, closing entry. A wage-justice entry "
            "distinct from every prior economic register for this alias -- 'The Bid He Refused to "
            "Win Cheaply' (MCD-672, an external contract bid) and 'The Quartermaster's Price' "
            "(MCD-1007, a materials trade). Forty-one hired laborers, sworn to no cause and paid "
            "under a wage schedule that never moved as hazard conditions worsened over seven weeks "
            "of siege, stop work rather than continue absorbing risk the original rate never "
            "priced for. For the first time in the alias's run, Kanja is placed structurally on "
            "the authority side of a labor dispute -- the wage schedule carries his own "
            "authorization -- rather than defaulting to solidarity by role. He resolves it by "
            "explicitly rejecting that structural position: an open, unrounded accounting of every "
            "hour worked under worsened conditions, full back pay authorized from the resistance's "
            "own operational funds, and the schedule rewritten to track hazard week over week "
            "rather than remaining fixed. Reuses already-locked crew member Garren Hask, drawing "
            "directly on his established role as the crew's counter and ledger-keeper (CC-115). "
            "The mucker who presses the entry's closing question is a new, deliberately unnamed "
            "one-scene character (collision-checked clean). No new named characters. Closes wave "
            "21 (with MCD-1068 and MCD-1069) and the twenty-first overall Blue-Collar Titan wave."
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
            "batch": 244,
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
