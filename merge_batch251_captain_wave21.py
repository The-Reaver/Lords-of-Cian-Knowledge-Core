#!/usr/bin/env python3
"""Batch 251: Captain Alias Chronicle wave 21 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Captain's twenty-first Alias Chronicle wave. \"What Only the Hall Could Save\" (MCD-1089) makes "
    "Garren Hask's own aging and mortality concretely real for the first time -- a heart failure "
    "combat medicine can't answer sends him to Sera's healers' hall, a direct, load-bearing payoff of "
    "\"What Sera Chose Instead\" (MCD-1057) and \"The Charter They Finally Wrote\" (MCD-1056), staying "
    "entirely off any ship under sail per MCD-1057's own closing line. \"The Notebook Garren Hask "
    "Finally Opened\" (MCD-1090) advances the mortality-succession thread from \"The Promise for After "
    "He's Gone\" (MCD-920) a genuine step -- Hask's private notebook reaches the council for the first "
    "time and Corren Halst is proposed, not confirmed, as a future council-chair successor -- "
    "deliberately left open rather than resolved, matching the sub-series' established advance-not-"
    "close precedent (the Sankofa territory Chronicle's \"crack\" entry, MCD-1025). \"The First Coin "
    "They Took From the Trust\" (MCD-1091) closes the wave with a detailed full-Trinity combat "
    "showcase in a new setting (a crowded civic grain-distribution plaza) and the sub-series' first "
    "paid commission, specifically from the Sovereign Trust the crew fought for twelve years, "
    "resolved through Kanja's own distinction between serving an institution and feeding the people "
    "under it; first on-page use of Onyx of Oblivion's Veil Piercer power inside the Captain "
    "sub-series. No new named characters introduced across all three entries -- Garren Hask, Sera, "
    "Corren Halst, Efa Gol, and Callum Breck all reused. Abad's approval: \"another alias wave of all "
    "aliases\"."
)

NEW_RULES = [
    {
        "id": "MCD-1089",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Only the Hall Could Save\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-only-the-hall-could-save.md), Captain Alias Chronicle "
            "LXI, wave 21. Years into the peace, Garren Hask collapses at his own ledger table -- a "
            "heart failing from decades of unrelenting work, a wound the crew's own combat medicine "
            "has no answer for -- and is taken to Sera's healers' hall (already locked, CC-117/"
            "MCD-1057) rather than treated aboard ship. Sera stabilizes him and teaches him to live "
            "around the condition rather than through it, and Kanja, standing in her hall as a man "
            "handing over someone he cannot save himself, understands for the first time exactly how "
            "much the crew now depends on the choice she made not to join it, a direct, concrete "
            "payoff of the charter's (MCD-1056) mutual free-membership principle. The entire scene "
            "stays off any ship under sail, consistent with MCD-1057's closing line. No new named "
            "characters -- Garren Hask, Efa Gol, Callum Breck, and Sera all reused. First entry, "
            "wave 21."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1090",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Notebook Garren Hask Finally Opened\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-notebook-garren-hask-finally-opened.md), Captain Alias "
            "Chronicle LXII, wave 21. Six weeks after his heart scare (MCD-1089), Garren Hask brings "
            "the private notebook already established at \"The Promise for After He's Gone\" "
            "(MCD-920) to the dispute council for the first time, moving it from a personal practice "
            "into the institutional record and taking a genuine step on the charter's deliberately "
            "blank fourth clause (MCD-1056) without resolving it. Corren Halst (already established "
            "as an independent commander, MCD-608) is proposed, not confirmed, as a future "
            "council-chair successor, and asks to be asked again in five years rather than decide "
            "under the shadow of Hask's scare; Kanja's own eventual role stays deliberately "
            "unaddressed. No new named characters -- Garren Hask, Corren Halst, Efa Gol, and Callum "
            "Breck all reused. Second entry, wave 21."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1091",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The First Coin They Took From the Trust\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-first-coin-they-took-from-the-trust.md), Captain Alias "
            "Chronicle LXIII, wave 21, closing the wave. A detailed full-Trinity combat showcase in a "
            "crowded civic plaza during a Sovereign Trust grain distribution -- the sub-series' first "
            "paid commission, and the first time the crew is formally hired by the Trust it fought for "
            "twelve years, producing genuine internal friction (Corren Halst) resolved through "
            "Kanja's own distinction between serving an institution and feeding the people under it. "
            "Onyx of Oblivion's Veil Piercer power reads eight raiders hidden inside the food line "
            "before the first sack is touched (its first on-page use inside the Captain sub-series, "
            "previously showcased for the Trench Monarch at MCD-369); Mafesto's Kinetic Transfer "
            "System redirects a committed blade strike away from a bystander, and Obsidian Malice "
            "discharges in three precisely angled bursts rather than one wide blast to avoid panicking "
            "the crowd. No new named characters -- Corren Halst, Efa Gol, Callum Breck, and Kanja all "
            "reused; the administrator and all eight raiders are deliberately unnamed. Closes "
            "Captain's twenty-first wave."
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
            "batch": 251,
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
