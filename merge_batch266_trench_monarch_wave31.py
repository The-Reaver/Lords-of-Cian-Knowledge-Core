#!/usr/bin/env python3
"""Batch 266: Trench Monarch Alias Chronicle wave 31 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "The Trench Monarch's thirty-first Alias Chronicle wave, drafted under Abad's blanket "
    "authorization to continue a 31st wave for all eleven aliases. Three fresh registers, none "
    "repeating a prior wave's story shape: Danne Sok's first dedicated in-era entry within this "
    "alias's own run (a silent counter-intelligence catch, distinct from his already-locked Bane-"
    "alias origin memory, MCD-530); a new predatory-lending institutional thread answered with "
    "honest financial infrastructure (an interest-free emergency bridge fund) rather than "
    "confrontation, including a real operational cost; and the wave's first entirely "
    "celebratory, conflict-free entry, a dockworker wedding closing the wave on a warm note. No "
    "new named characters across all three entries -- the informant/courier, the lender and "
    "borrowers, and the bride and groom are all unnamed, consistent with this sub-series' strong "
    "preference for continuity depth over new names. Abad's approval: \"let's do a 31st alias "
    "wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1394",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Danne Sok Heard Before Anyone Else\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-danne-sok-heard-before-anyone-else.md), Trench "
            "Monarch Alias Chronicle XCI, wave 31. Rebellion era, pre-Black-Trench. Danne Sok's "
            "first dedicated in-era entry within the Trench Monarch's own run, distinct from his "
            "already-locked Bane-alias origin memory (MCD-530): his established silent-vigilance "
            "characterization is grounded in a concrete act, quietly identifying and removing a "
            "Trust-planted informant among new recruits through pattern-reading alone, no dialogue "
            "exchanged with the informant or his courier at any point. No new named characters -- "
            "the informant and courier are unnamed. First entry in the Trench Monarch's "
            "thirty-first wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1395",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Lender Who Named His Own Price\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-lender-who-named-his-own-price.md), Trench Monarch "
            "Alias Chronicle XCII, wave 31. Rebellion era, pre-Black-Trench. A new institutional "
            "register distinct from the already-locked licensing/charter/court threads: a "
            "predatory moneylender preys on workers waiting on slow but honest tally verification; "
            "rather than confronting him, Kanja and Garren Hask build a parallel interest-free "
            "emergency bridge fund from the crew's own resources, undercutting his usury through "
            "competition, not force. The fund runs dry twice, forcing Hask to triage the most "
            "urgent claims first -- a real operational cost, not a frictionless win. No new named "
            "characters -- the lender and the four borrowers are unnamed. Second entry in the "
            "Trench Monarch's thirty-first wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1396",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Wedding at the Third Canal Bend\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-wedding-at-the-third-canal-bend.md), Trench Monarch "
            "Alias Chronicle XCIII, wave 31, closing the wave. Rebellion era, pre-Black-Trench. "
            "The wave's first entirely conflict-free, celebratory entry -- a dockworker wedding at "
            "the third canal bend (first named in MCD-1147), where Kanja attends as an ordinary, "
            "unremarkable guest with no ceremonial role. Reuses the full established crew roster "
            "(Corren Halst, Danne Sok, Maret Vos, Garren Hask, Callum Breck, Efa Gol, Pell Ostra) "
            "in warm, unremarkable moments. No new named characters -- the bride and groom are "
            "unnamed. Closes the Trench Monarch's thirty-first wave (with \"What Danne Sok Heard "
            "Before Anyone Else,\" MCD-1394, and \"The Lender Who Named His Own Price,\" "
            "MCD-1395)."
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
            "batch": 266,
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
