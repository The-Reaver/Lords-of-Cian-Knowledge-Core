#!/usr/bin/env python3
"""Batch 271: Crow King Alias Chronicle wave 31 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "The Crow King's thirty-first Alias Chronicle wave, drafted under Abad's blanket authorization "
    "to continue a 31st wave for all eleven aliases. Resolves where the doctrine page lost during a "
    "raid in wave 22 (\"The Page That Went Missing,\" MCD-1257) actually ended up: surfacing years "
    "later in a distant river town, where it seeded a wholly independent, unsanctioned practice built "
    "on its philosophy alone -- no knowledge of the Hymn-Engine, the Crow King name, or Kanja's "
    "identity. The wave opens with the discovery, turns on the fourth generation quietly correcting a "
    "dangerous near-lie without ever revealing himself, and closes on Kanja, the apprentice, the third "
    "generation, and the fourth generation choosing to leave the practice exactly as it is -- a literal "
    "payoff of wave 30's closing line that the craft's philosophy could survive without anyone "
    "remembering to call it by this name. No new named characters were introduced anywhere in this "
    "wave. Abad's approval: \"let's do a 31st alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1409",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Grew From the Page\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-grew-from-the-page.md), Crow King Alias Chronicle "
            "XCI, wave 31, opening it. A trader's secondhand story reveals that the doctrine page "
            "physically lost during a raid (MCD-1257) survived and, passed hand to hand into a "
            "distant river town over six years, seeded a loose, self-taught group who settle local "
            "disputes by a practice built entirely on the page's philosophy -- with no knowledge of "
            "the Hymn-Engine, the Crow King name, or Kanja's identity, confirming MCD-1257's own "
            "conclusion that the page held no exploitable technique. The fourth generation, "
            "apprentice, and third generation reused for continuity. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1410",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ones Who Never Learned His Name\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ones-who-never-learned-his-name.md), Crow King Alias "
            "Chronicle XCII, wave 31. The apprentice and the fourth generation travel to the river "
            "town and watch the self-taught group resolve a real water-rights dispute through the "
            "same listen-before-you-act discipline, unnamed and untrained by the lineage; the fourth "
            "generation quietly asks one corrective question that stops a younger member from winning "
            "the dispute with a confident falsehood, protecting the practice's core no-lying rule "
            "without ever revealing his identity or origin, consistent with the alias's established "
            "convention of staying unnamed to outsiders. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1411",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Name They Never Needed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-name-they-never-needed.md), Crow King Alias Chronicle "
            "XCIII, wave 31, closing it. Kanja, the apprentice, the third generation, and the fourth "
            "generation weigh what they found at the river town and deliberately decide to leave the "
            "independent practice exactly as it is -- unaffiliated, uncorrected, unformalized -- "
            "framing it as literal proof of MCD-1282's closing hope that the craft's underlying "
            "discipline could survive without anyone remembering to call it by this name. "
            "Deliberately distinguished from, and left separate from, the still-unresolved "
            "fifth-generation question (MCD-1258, MCD-1280), which stays open. No new named "
            "characters. Closes wave 31 (with MCD-1409 and MCD-1410)."
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
            "batch": 271,
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
