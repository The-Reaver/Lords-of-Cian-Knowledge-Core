#!/usr/bin/env python3
"""Batch 116: Lock the Captain's three-entry Alias Chronicle wave (MCD-395 through MCD-397),
completing all ten remaining Alias Chronicle waves under Abad's continuous authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-10, no source document."

BATCH_NOTE = (
    'Abad: "continue uninterrupted until completion this includes test, commit, push to main '
    'origin" -- completes all ten remaining alias waves (Trench Monarch, Industrial Myth, '
    'Blue-Collar Titan, Sovereign Ghost of the Great Sea, the Scourge, the Crow King, the Iron '
    'Bastard, the Lord of Embers, the Storm That Walks, and Captain).'
)

NEW_RULES = [
    {
        "id": "MCD-395",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Word Before the Alias\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-word-before-the-alias.md), Captain Alias "
            "Chronicle I. Rebellion era, the naval campaigns (MCD-242, ages 21-22), from Garren "
            "Hask's perspective (already locked, CC-115/CC-116). The morning after Iron Shallows, "
            "Hask -- already established as the first person to address Kanja by his bare name -- "
            "explains that he privately thinks of him as 'Captain' rather than any Directorate-"
            "classified alias, a title of responsibility and trust rather than fear, tied to "
            "Kanja's personal habit of checking every casualty-list name himself. The name spreads "
            "through the crew quietly afterward. No new named characters beyond the already-"
            "locked Garren Hask. First entry in the Captain's three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-396",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Thirty Feet He Refused to Lose\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-thirty-feet-he-refused-to-lose.md), Captain Alias "
            "Chronicle II. Rebellion era, a new ambush on eleven unarmored new recruits crossing "
            "an exposed causeway. Kanja closes the exposed ground in seconds and holds it "
            "personally, demonstrating Mafesto's Kinetic Transfer System absorbing volley fire "
            "meant for the recruits, Obsidian Malice collapsing a rooftop ledge to break "
            "shooters' footing rather than kill them, and Onyx's Veil Piercer exploiting a gap in "
            "overlapping fire -- purely defensive, crew-protective use of the Trinity, distinct "
            "in register from the confrontational showcases in other alias waves. All eleven "
            "recruits reach cover uninjured. No new named characters. Second entry in the "
            "Captain's three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-397",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Word Callum Breck Chose\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-word-callum-breck-chose.md), Captain Alias "
            "Chronicle III, closing the wave and the full run of ten alias waves. Set six weeks "
            "after Callum Breck's already-locked first confirmed post-silence utterance ('Two "
            "hundred,' CC-119), without restaging it. Breck deliberately adopts 'Captain' over "
            "the 'Trench Monarch' alias he himself originally coined, explaining the shift as "
            "tied to Kanja's refusal to let Nev Torr's death at the Black Trench be assigned as "
            "Breck's fault -- a monarch rules over what happens to his people, a captain answers "
            "for it. The word spreads through the crew independently of, but arriving at the same "
            "conclusion as, Garren Hask's own adoption of it (MCD-395). No new named characters "
            "beyond the already-locked Callum Breck. Closes the Captain's three-Chronicle wave "
            "(with 'The Word Before the Alias,' MCD-395, and 'The Thirty Feet He Refused to "
            "Lose,' MCD-396) and completes all ten remaining Alias Chronicle waves."
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
            "batch": 116,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Captain's three-entry Alias Chronicle wave (MCD-395 through MCD-397), "
                "the tenth and final of ten remaining alias waves. Every named alias (Trench "
                "Monarch, Bane, Industrial Myth, Blue-Collar Titan, Sovereign Ghost of the Great "
                "Sea, the Scourge, the Crow King, the Iron Bastard, the Lord of Embers, the Storm "
                "That Walks, and Captain) now has a completed first three-Chronicle wave. "
                + BATCH_NOTE
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
