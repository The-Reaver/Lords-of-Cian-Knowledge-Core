#!/usr/bin/env python3
"""Batch 32: World Adaptation Blueprint, Section VI Era B (the death of the Karesian men)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'World_Adaptation_Blueprint' (Google Drive fileId "
    "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA, Lore Vault), Section VI "
    "('The Lauris Letitia Chronicle'), Era B ('The Death of the Men')."
)

NEW_RULES = [
    {
        "id": "MCD-153",
        "category": "World Mechanics",
        "statement": (
            "The K-strand (Karesian sex determination runs on a "
            "male-lineage chromosome analog) suffered a catastrophic "
            "replication failure beginning ~7,200 years before the "
            "series' present day, collapsing the male birth ratio from a "
            "stable 0.99 baseline to 0.71 in one generation and to "
            "near-zero within five. The Threnarr archivists' investigation "
            "(commissioned by the Iron-Speakers' Great Conclave, ~1,400 "
            "years to complete) concluded the failure was too abrupt and "
            "too narrowly targeted to be natural, and proposed an "
            "introduced-agent hypothesis they couldn't confirm: something "
            "had entered the Karesian gene pool through orbital trade "
            "contacts 80,000-100,000 years before detection and taken "
            "that long to manifest. The hypothesis is correct -- the "
            "agent was T.D.K.'s, calibrated during his original "
            "reconnaissance of Kares Prime (MCD-152) as a deferred-yield "
            "operation he'd largely forgotten about by the time it "
            "activated. The Karesian civilization never learned who "
            "killed it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-154",
        "category": "World Mechanics",
        "statement": (
            "The male population collapsed across five generations "
            "(First Affected Cohort at a 0.71 birth ratio, down to 0.01 "
            "by the Last Affected Cohort, ~12,000 surviving males against "
            "~280,000 women). The Last Conclave made three irreversible "
            "decisions: restructure the Pair-Hold system into all-female "
            "Sister-Holds preserving the same cooperative architecture "
            "(~1,200 years to complete); cryogenically preserve K-strand "
            "and female genetic samples against a repair that might never "
            "come; and, at the latest viable moment, attempt one final "
            "deliberately-selected pure-blood conception as the "
            "civilization's last preservation effort."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-155",
        "category": "World Mechanics",
        "statement": (
            "The last male Karesian, Vael Threnarr-Karth, died in combat "
            "roughly 60 years before Lauris's birth at 47,800 years old, "
            "defending an orbital trade-point he had no obligation to "
            "defend; his archived note ('The ledger is open. The pages "
            "are ready. Someone will write what I could not.') is "
            "preserved and Lauris read it at age eleven. After his death "
            "the civilization was single-sex for the first time in "
            "31,000 years. At Lauris's birth, Kares Prime held roughly "
            "14,000 Karesian women across the twelve surviving Vasks of "
            "the original forty -- the other twenty-eight had been "
            "depopulated and their archives folded into the survivors'."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-156",
        "category": "World Mechanics",
        "statement": (
            "The Last Conclave's final-conception decision wasn't "
            "executed immediately -- the Threnarr archivists spent "
            "roughly 1,200 years continually refining the donor and "
            "maternal-candidate selection for marginally higher genetic "
            "integrity, until sample degradation began outpacing the "
            "gains, forcing the conception at the latest viable point: "
            "Lauris was born ~4,000 years before the series' present. "
            "Selene (her mother) raised her for the first 1,400 years of "
            "her life before Selene was killed defending Vask Threnarr "
            "against a raiding incursion, at 67,400 years old; Selene's "
            "archive of raising Lauris is among what Lauris still carries "
            "aboard the Karkosa."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-157",
        "category": "World Mechanics",
        "statement": (
            "The final conception, drawing on 47 distinct high-integrity "
            "K-strand donor samples selected across 1,200 years, produced "
            "something the Threnarr archivists hadn't targeted: not a "
            "recreation of cooperative-era baseline Karesian biology, but "
            "a synthesis integrating structural variations no single "
            "Karesian had ever carried at once -- functionally the "
            "direction the species' biology was evolving toward before "
            "the K-strand decline cut it off. Concretely: Lauris's static "
            "density rose faster through childhood than any documented "
            "Karesian and exceeded the cooperative-era ceiling by "
            "adulthood; her Ironstorm Blood recovery runs continuously "
            "rather than in discrete phases, so she doesn't require "
            "standard post-engagement recovery; her density climbs across "
            "a sustained engagement rather than peaking early, reaching "
            "roughly 80% above her starting density at ~90 minutes of "
            "continuous combat; and her Hexa-Lamellar Lattice integrates "
            "donor-pool variations the archivists could only describe as "
            "an architecture 'the species was evolving toward.'"
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
            "batch": 32,
            "source_doc": "World_Adaptation_Blueprint (Section VI, Era B: the death of the men)",
            "source_id": "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "3.5"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
