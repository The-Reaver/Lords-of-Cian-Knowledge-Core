#!/usr/bin/env python3
"""Batch 293: Lauris Chronicles II-V -- the first four-strand wave, establishing
the pacing convention for her Character Chronicle series."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-17, no source document. First wave "
    "of Lauris Letitia's four-strand Character Chronicle series "
    "(docs/lords-of-cian/character-chronicle-gameplan.md)."
)

BATCH_NOTE = (
    "Establishes the pacing convention for Lauris's Character Chronicle series, agreed "
    "in conversation before drafting: four parallel strands rather than one flat "
    "numbered sequence -- Strand K (Kares Prime / deep past), Strand D (Sealbound "
    "Directorate years), Strand L (the Ledger / present-day operational debts), Strand "
    "W (Witness / present-day, quiet register) -- braided together in waves of one "
    "entry per strand, all still numbered in one continuous sequence. Every entry opens "
    "with a short archive fragment in Lauris's own spare voice before Fermand Aurelias's "
    "narration proper, a two-voice structure unique to this series since she is the only "
    "Tier 1 character who keeps a literal written archive Fermand is established as "
    "transcribing from (MCD-211). First wave: MCD-1562 (Strand K, 'The Vein Between Two "
    "Vasks,' one of the three inter-Vask security operations from the Long Operational "
    "Period, MCD-1555); MCD-1563 (Strand D, 'The Eighty Interviews,' full-scene treatment "
    "of Operation 19/the Long Pursuit, previously only summarized at MCD-1540); MCD-1564 "
    "(Strand L, 'The Last of the Seven,' advancing the Operation 38 third-facility debt, "
    "MCD-191, without resolving it or touching the K-Theta cave-system reveal MCD-193 "
    "reserves for a future book); MCD-1565 (Strand W, 'Two Archives, One Question,' a "
    "stakes-free evening with Sephtis extending their joint-archive-holder relationship, "
    "MCD-212, and putting CC-134's combat-joy trait on the page in a non-combat register "
    "for the first time). No new named characters across all four entries. Abad's "
    "approval: \"lock.\""
)

NEW_RULES = [
    {
        "id": "MCD-1562",
        "category": "lauris-character-chronicle",
        "statement": (
            "Lauris Chronicle II, \"The Vein Between Two Vasks\" (full narrative text at "
            "docs/lords-of-cian/chronicles/lauris-chronicle-ii-the-vein-between-two-vasks.md), "
            "the first entry of Strand K (Kares Prime / deep past) in her Character "
            "Chronicle series. Roughly six hundred years after achieving karth-ven, within "
            "the Long Operational Period (MCD-1555), Lauris resolves a resource-scarcity "
            "dispute between Vask Threnarr and Vask Aldreth over a shared forgeable ore-vein "
            "without drawing a weapon -- walking into the exact center of where the first "
            "blow between two armed delegations would have to pass through her, then asking "
            "each side to state its cost of losing the argument aloud to the other. The two "
            "sides reach their own arrangement without her proposing one; her own archive "
            "entry leaves open whether her presence changed the outcome or merely gave both "
            "sides time to reach the arithmetic they already knew -- the only uncertainty she "
            "records about any of her own actions across forty read archive entries. No new "
            "named characters; the opposing delegation stays deliberately unnamed."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1563",
        "category": "lauris-character-chronicle",
        "statement": (
            "Lauris Chronicle III, \"The Eighty Interviews\" (full narrative text at "
            "docs/lords-of-cian/chronicles/lauris-chronicle-iii-the-eighty-interviews.md), "
            "the first entry of Strand D (Sealbound Directorate years) in her Character "
            "Chronicle series. Full-scene treatment of Operation 19, the Long Pursuit "
            "(previously only summarized at MCD-1540): Lauris's 23-month, 80-interview "
            "investigative method for locating defected contractor Kaerith Vossen, building "
            "a predictive model of his decision-making rather than physically tracking him. "
            "Dramatizes the specific moment her institutional-blindness realization "
            "crystallizes -- a retired archivist's admission that he never questioned why the "
            "Directorate's oldest vaults use keying architecture no living engineer can "
            "explain -- as the first point in her archive where she uses the word 'inherited' "
            "about the Directorate's own methods rather than the engineering tradition's. "
            "Vossen's acquisition itself is procedurally clean and occupies little of the "
            "account; the eighty conversations that preceded it are the operation's true "
            "content. No new named characters -- Kaerith Vossen already locked (MCD-1540)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1564",
        "category": "lauris-character-chronicle",
        "statement": (
            "Lauris Chronicle IV, \"The Last of the Seven\" (full narrative text at "
            "docs/lords-of-cian/chronicles/lauris-chronicle-iv-the-last-of-the-seven.md), "
            "the first entry of Strand L (the Ledger / present-day operational debts) in her "
            "Character Chronicle series. Advances the third of Operation 38's withheld "
            "facilities (MCD-191, 'an open Lords of Cian objective') without resolving it: "
            "an Aerelin-network courier surfaces a manifest fragment narrowing the facility's "
            "location to a coastal ridge; Lauris locates and confirms it, but declines to "
            "attempt entry alone after reading its defensive architecture as considerably "
            "more sophisticated than the two already-cleared facilities from the same "
            "original seven, judging solo entry a wager rather than an operation. She marks "
            "the location and its defensive signature for a properly resourced future "
            "clearance rather than risk closing the debt by dying and leaving its subjects "
            "worse off. Reports to Ezio that the debt is precisely located for the first "
            "time in years, though still not discharged. No new named characters; the "
            "facility itself stays deliberately uncoded, matching MCD-191's own phrasing."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1565",
        "category": "lauris-character-chronicle",
        "statement": (
            "Lauris Chronicle V, \"Two Archives, One Question\" (full narrative text at "
            "docs/lords-of-cian/chronicles/lauris-chronicle-v-two-archives-one-question.md), "
            "the first entry of Strand W (Witness / present-day, quiet register) in her "
            "Character Chronicle series. A stakes-free evening: Lauris and Sephtis, the Lords "
            "of Cian's two joint-archive holders on Anu Un Ra's engineering tradition "
            "(MCD-212), cross-reference her Operation 3 Iron-Spire notes against his own "
            "partial Verith-era fragment for the first time, disagreeing amicably for roughly "
            "forty minutes without resolving whether the two resonance signatures share a "
            "common origin. Puts CC-134's combat-joy trait on the page in a non-combat "
            "register for the first time -- the same unqualified, competent pleasure she "
            "carries into a boarding action, here spent entirely on an unresolved research "
            "question neither party rushes to close. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 4, f"expected 4 new rules, got {len(NEW_RULES)}"
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 293,
            "date": str(date.today()),
            "source": SOURCE,
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
