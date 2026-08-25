#!/usr/bin/env python3
"""Batch 33: World Adaptation Blueprint, Section VI Era C (the Women's Rule)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'World_Adaptation_Blueprint' (Google Drive fileId "
    "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA, Lore Vault), Section VI "
    "('The Lauris Letitia Chronicle'), Era C ('The Women's Rule')."
)

NEW_RULES = [
    {
        "id": "MCD-158",
        "category": "World Mechanics",
        "statement": (
            "The Sister-Hold structure (MCD-154) fully replaced the "
            "Pair-Hold tradition over ~1,200 years and had already been "
            "running for ~1,140 years by Lauris's birth -- she was born "
            "into its most mature, stabilized form. Three measurable "
            "cultural shifts distinguished it from the cooperative era: "
            "governance shifted from procedural duel to extended "
            "deliberation (all-female duels resolved less cleanly than "
            "mixed-sex ones, so the Iron-Speakers dropped the practice); "
            "the civilization turned past-oriented, with the Iron-Halls "
            "of Vask and archival preservation becoming the central "
            "institution of a society that had accepted its own ending; "
            "and it grew deliberately outward-facing in its later "
            "centuries, building the orbital-travel infrastructure that "
            "produced a second Karesian diaspora (small numbers of women "
            "leaving and rarely returning) -- the same infrastructure "
            "that later makes Lauris's own journey to Cian possible."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-159",
        "category": "World Mechanics",
        "statement": (
            "At Lauris's birth, Kares Prime held ~14,000 women across "
            "twelve surviving Vasks, down from a cooperative-era peak of "
            "~4 million across forty -- under half a percent of peak "
            "population, on a terminal demographic curve projected to "
            "reach zero in ~90,000 years without intervention. Lauris was "
            "the first of three planned final preservations the "
            "Iron-Speakers had prepared for; the second and third were "
            "never executed; her existence absorbed the entirety of the "
            "civilization's remaining preservation capacity. She was, "
            "functionally, the last child Kares Prime would ever produce."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-160",
        "category": "World Mechanics",
        "statement": (
            "The twelve surviving Vasks operated as specialized nodes at "
            "the bare minimum configuration the Iron-Speakers calculated "
            "could sustain the civilization's full function, no margin "
            "for loss: Vask Threnarr (the largest, ~3,200 people, the "
            "medical-archival repository and genetic preservation site -- "
            "where Lauris was born and raised through early childhood); "
            "Vask Aldreth (agriculture and Ironstorm Blood-derived "
            "exports, Selene Aldreth-Vorr's home Vask before she "
            "relocated to Threnarr); Vask Karth-Ven (smallest but "
            "operationally critical, the combat-development repository "
            "and site of the Karth-Sera curriculum, where Lauris "
            "relocates at age 14 for specialized training); Vask Olmedrin "
            "(the smallest by population, orbital-trade specialists "
            "managing contact with departing travelers); and eight "
            "further Vasks (Sethrenn, Vor-Meth, Iralek, Ostrenn, Drenmar, "
            "Vask-of-Vasks -- the original founding site, kept as a "
            "cultural rather than operational center -- Aerth, and "
            "Karen-Drael) covering deep-mountain Living Drakma mining, "
            "atmospheric research, historical archives, Iron-Speaker "
            "coordination, training-floor maintenance, civic "
            "infrastructure, and preservation of the depopulated Vasks' "
            "transferred archives."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-161",
        "category": "World Mechanics",
        "statement": (
            "The Sister-Hold civilization Lauris was raised in was calm "
            "rather than despairing -- its grief was thousands of years "
            "in the past -- and had instead developed a deep culture of "
            "memory: every adult woman knew her direct lineage back at "
            "least twelve generations (~180,000 years), and every "
            "Sister-Hold kept its own internal archive nested inside its "
            "Vask's larger one. Lauris's first inheritance from this "
            "culture wasn't her density or biology but the practice of "
            "careful witness: watching, recording, and withholding "
            "judgment until the data is complete. This is specifically "
            "what Ezio recognized and hired her for on first meeting -- "
            "her combat capability mattered less to him than her capacity "
            "to witness without rushing to a verdict."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full draft as pasted in-conversation: "lock it"'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 33,
            "source_doc": "World_Adaptation_Blueprint (Section VI, Era C: the Women's Rule)",
            "source_id": "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "3.6"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
