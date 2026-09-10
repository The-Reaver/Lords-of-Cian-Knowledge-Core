#!/usr/bin/env python3
"""Batch 113: Lock the Iron Bastard's three-entry Alias Chronicle wave (MCD-386 through
MCD-388), continuing uninterrupted through the remaining alias waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-10, no source document."

BATCH_NOTE = (
    'Abad: "continue uninterrupted until completion this includes test, commit, push to main '
    'origin" (covering all ten remaining alias waves).'
)

NEW_RULES = [
    {
        "id": "MCD-386",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"No Ground Worth Taking\" (full narrative text at "
            "docs/lords-of-cian/chronicles/no-ground-worth-taking.md), Iron Bastard Alias "
            "Chronicle I. Rebellion era, a new solo stand distinct from the original Iron "
            "Bastard's Stand (MCD-238, age 25). A general who studied only Kanja's terrain-"
            "dependent victories chooses open salt-pan specifically to strip away what he "
            "believes is a terrain advantage, not realizing the original Iron Bastard's Stand "
            "was already fought on open ground with no exploitable terrain -- the engagement "
            "proves the alias's advantage was never geography, ending the general's career when "
            "his own accurate report reads to his superiors as an admission of failure. No new "
            "named characters. First entry in the Iron Bastard's three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-387",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Held Together Stopped Holding\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-held-together-stopped-holding.md), Iron Bastard "
            "Alias Chronicle II. Rebellion era, a new engagement against a Trust Crawler variant "
            "engineered with four independent fitting alloys specifically to defeat the single-"
            "frequency resonance that exposed the original vulnerability. Kanja uses the "
            "Aegis-Talisman's frequency-inversion lens (MCD-238's 'off-hand shield/talisman... "
            "forged separately') diagnostically first, cataloguing all four alloy signatures "
            "before cycling a sequential harmonic through each; Mafesto's Kinetic Transfer System "
            "absorbs answering fire, Obsidian Malice discharges into the already-loosened lead "
            "Crawler's plating, and Onyx's Cadence Ruin clears the boarding crew. Eleven of "
            "twelve Crawlers are disabled -- the four-alloy countermeasure produces four points of "
            "entry instead of one. No new named characters. Second entry in the Iron Bastard's "
            "three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-388",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"Ninety Minutes Inside a Crawler\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ninety-minutes-inside-a-crawler.md), Iron Bastard "
            "Alias Chronicle III, closing the wave. Set during the original Iron Bastard's Stand "
            "(MCD-238) itself, from inside one of the twelve targeted Crawlers -- a driver and "
            "gunner experience the ninety-minute resonance effect as their own vehicle "
            "progressively shaking itself apart from the inside with no visible cause, refusing "
            "to return to the field afterward. First human/crew-scale account of that engagement. "
            "No new named characters. Closes the Iron Bastard's three-Chronicle wave (with 'No "
            "Ground Worth Taking,' MCD-386, and 'What Held Together Stopped Holding,' MCD-387)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collisions with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 113,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Iron Bastard's three-entry Alias Chronicle wave (MCD-386 through "
                "MCD-388), the seventh of ten remaining alias waves. " + BATCH_NOTE
            ),
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate IDs after merge"
    print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
          f"Batches: {len(ledger['batches_completed'])}.")


if __name__ == "__main__":
    main()
