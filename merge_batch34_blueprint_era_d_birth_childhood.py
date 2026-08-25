#!/usr/bin/env python3
"""Batch 34: World Adaptation Blueprint, Section VI Era D (birth and the Threnarr childhood)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'World_Adaptation_Blueprint' (Google Drive fileId "
    "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA, Lore Vault), Section VI "
    "('The Lauris Letitia Chronicle'), Era D ('Birth and the Threnarr "
    "Childhood')."
)

NEW_RULES = [
    {
        "id": "MCD-162",
        "category": "World Mechanics",
        "statement": (
            "Lauris was born at Vask Threnarr, concluding the 1,200-year, "
            "47-donor selection process (MCD-157). Her maternal candidate, "
            "Selene Aldreth-Vorr, was 38,200 years old at conception "
            "(mature second adulthood, MCD-149) and relocated from her "
            "home Vask Aldreth to Threnarr roughly three years before "
            "conception to begin the maternal-candidate protocols; the "
            "fertilization succeeded on the first attempt, and Lauris "
            "presented at birth as the highest-integrity Karesian genome "
            "documented in the previous 7,200 years. The senior archivist "
            "present, Drenneth Threnarr-Vask, recorded the birth in two "
            "sentences: 'The conception held. The civilization continues "
            "for one more lifespan.' Lauris read the entry herself at age "
            "230 and has never discussed the experience."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-163",
        "category": "World Mechanics",
        "statement": (
            "The Iron-Speakers knew at Lauris's birth that she was the "
            "civilization's last possible preservation -- their attempts "
            "to identify second and third candidate profiles had already "
            "failed by the time she was conceived. They did not yet know "
            "what the 47-donor recombination had actually produced "
            "(MCD-157); they expected a cooperative-era baseline and "
            "treated her accordingly. The gap between what they expected "
            "and what she actually was didn't become visible until her "
            "first anomalous density reading roughly 1,400 years later."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-164",
        "category": "World Mechanics",
        "statement": (
            "Selene raised Lauris within a five-member Threnarr "
            "Sister-Hold assembled specifically for the purpose, all "
            "sharing full daily authority over her under Karesian "
            "collective-childcare tradition: Selene herself (first among "
            "equals, biological lineage carrier); Drenneth Threnarr-Vask "
            "(the senior archivist, eldest of the Hold at 71,400 years); "
            "Mira Threnarr-Olmedrin (a combat instructor relocated from "
            "Vask Karth-Ven for Lauris's early physical training); Veth "
            "Threnarr-Karth (a pediatric-development medical archivist); "
            "and Olda Threnarr-Iralek (a historical archivist who ran "
            "Lauris's lineage and archival education). This arrangement "
            "held for the first 1,400 years of Lauris's life."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-165",
        "category": "World Mechanics",
        "statement": (
            "The Sister-Hold deliberately withheld from Lauris that she "
            "was the civilization's final preservation -- not to shield "
            "her, but to preserve the integrity of her childhood as data: "
            "the Iron-Speakers wanted to know what the unmodified genome "
            "produced when raised without that knowledge. To support "
            "this, the entire civilization's remaining parthenogenic-"
            "conception schedule was adjusted to produce a cohort of 47 "
            "other children at Vask Threnarr around her birth, none of "
            "them told either. Her closest cohort friend, Velith, was "
            "killed in a Vask Threnarr defensive operation when Lauris "
            "was ~1,200 years old; Lauris's archive entry recording "
            "Velith's death remains the longest single entry she has "
            "ever written."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-166",
        "category": "World Mechanics",
        "statement": (
            "Lauris's early childhood curriculum ran three tracks: "
            "physical conditioning from age 3 (stationary-density holds, "
            "controlled-fall training -- she tracked within cohort norms, "
            "static density 800-1,400x like her peers), archival training "
            "from age 5 under Olda (daily observation logs -- by age 8 "
            "her structural awareness already exceeded cohort average, "
            "noted privately but not flagged), and lineage education from "
            "age 7-12, taught only through Selene's maternal line, with "
            "her K-strand donor lineage deliberately withheld. At age 14, "
            "a routine cohort density assessment registered her at "
            "2,800x -- double the cohort ceiling, confirmed after "
            "recalibration and repeat testing ruled out instrument error. "
            "After a three-day deliberation, the Sister-Hold relocated "
            "her training to Vask Karth-Ven; Lauris took the news calmly, "
            "asked only whether she'd still see her cohort, and left "
            "Threnarr two months later with Selene accompanying her."
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
            "batch": 34,
            "source_doc": "World_Adaptation_Blueprint (Section VI, Era D: birth and the Threnarr childhood)",
            "source_id": "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "3.7"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
