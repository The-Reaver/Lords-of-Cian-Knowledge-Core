#!/usr/bin/env python3
"""Batch 39: Tier 4 Audit Preparation Checklist cross-check."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'Tier_4_Preparation_Checklist.docx' (Google Drive fileId "
    "1M9AgpCP8Q_E7a2y6-N3kbQRYlP5abxaS, two byte-identical copies also "
    "exist: 1xHYC2Q4YEm8CFSCHK5GCZKpnCn73OAJL). A QA checklist for "
    "auditing three structural-outline documents (Book1/Book2/Books 3-5) "
    "against a 'Session Lock April 11, 2026' authority document, itself "
    "not found in Drive (like the earlier OPEN-005 'Session Lock 2', it "
    "likely never existed as a standalone file distinct from the "
    "session-lock-2026-03-25 material already in this ledger). Most of "
    "the checklist's content -- the Ronin reckonings, the Beloved, "
    "Shattered Kingdoms geography, the Archipelago names, Orlok's stats, "
    "the Gate Battle roster, 'T.D.K. contained not killed,' and the hard "
    "style constraints (no antithesis, Mythic Realism, no borrowed "
    "terminology) -- is already locked under MCD-090 through MCD-100 and "
    "the Voice Bible rules. This batch locks only the checklist's "
    "genuinely new numeric/narrative specifics not previously in the "
    "ledger. The 'verify the structural outlines comply' instruction "
    "itself is a book-editing task outside the ledger's scope and is not "
    "acted on here."
)

NEW_RULES = [
    {
        "id": "MCD-218",
        "category": "World Mechanics",
        "statement": (
            "During the Ozmund fight in Book 3, Kanja pushes past his "
            "Book 3 density ceiling to approximately 32,000x, producing "
            "catastrophic structural debt in his Bio-Drakma skeleton. "
            "The Sin-Eaters interrupt before either man finishes the "
            "engagement. Kanja ends Book 3 alive but broken. Damu's "
            "assessment: 'The metal remembers the break. Whether it "
            "forgets is not my decision.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-219",
        "category": "World Mechanics",
        "statement": (
            "In Book 3, Ozmund's Crown-Scar (already locked as a choice "
            "he makes, MCD-100) is fully embraced but uncalibrated, "
            "producing an effective ceiling of 22,000x-24,000x. Red "
            "Beard's awakening line (MCD-100) uses the word 'General.' "
            "Ozmund's resting density is fixed at 15,000x across all "
            "five books; his growth across the series is architectural "
            "refinement of how that density is used, not an escalation "
            "of the baseline number."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-220",
        "category": "World Mechanics",
        "statement": (
            "The Anansi/Valeria sibling-bond reveal occurs on-page "
            "during the Book 5 Gate Battle (already locked at MCD-098). "
            "Toussaint Louverture arrives at the battle's crossroads "
            "moment and delivers the line 'The weight is equal'; Soledad "
            "Keme moves immediately in response, and the Archipelago "
            "nation answers -- committing its support at that moment."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-221",
        "category": "World Mechanics",
        "statement": (
            "Book 5's three fronts (already locked in general at "
            "MCD-097) break down as: Engine front -- Kanja, Ozmund, "
            "Pyro. Gate front -- Orlok, Anansi, Ezio, Fermand, Toussaint "
            "(matching the already-locked Gate team of MCD-098). Line "
            "front -- Red Beard, operating alone."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-222",
        "category": "World Mechanics",
        "statement": (
            "T.D.K.'s Warbody operates in three distinct states: "
            "Standard (28,000x-35,000x), Peak (40,000x-42,000x), and "
            "Reset (18,000x-22,000x). Kanja's Book 5 ceiling (42,000x+, "
            "already locked at MCD-144) exceeds the Warbody's Peak state "
            "for the first time in the series; the window in which this "
            "holds true is only seconds wide."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-223",
        "category": "World Mechanics",
        "statement": (
            "Pyro's Book 5 peak capability is deliberately left "
            "unlocked: no specific density numbers exist for it as of "
            "the present drafting, and his full potential remains sealed "
            "behind a reality-scar. His currently locked ability "
            "baseline is his Thermal Variant baseline, Metabolic "
            "Overdrive, and Causal Convergence; future material should "
            "present his Book 5 peak as significant without committing "
            "to density figures or additional abilities beyond this "
            "baseline."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-224",
        "category": "World Mechanics",
        "statement": (
            "The Anansi/Valeria sibling bond (already locked) becomes "
            "operationally relevant at the Ghost reckoning in Book 4 "
            "(their joint kill of the Ghost, already locked at MCD-092) "
            "and is dramatically revealed on-page during the Book 5 Gate "
            "Battle (MCD-220)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-225",
        "category": "World Mechanics",
        "statement": (
            "General Baryon (T.D.K.'s Weights/Conquest champion) "
            "operates at 22,000x sustained density. He is debt-bound to "
            "T.D.K. rather than loyal to him, and is vulnerable during "
            "Pi-Awakening events. Red Beard's line to him, delivered "
            "after a 40-minute engagement: 'You held the line.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-226",
        "category": "World Mechanics",
        "statement": (
            "Sereth Vaul ('the Silencer,' T.D.K.'s Echoes/Nameless "
            "Pursuit champion and commander of the Ever-Haunt) operates "
            "at 9,500x density, with Resonance Erasure as his signature "
            "ability. Pi-Awakening only reduces his capability by 30% -- "
            "a notably strong resistance compared to other T.D.K. "
            "champions. He spent 314 years preparing an operation "
            "against the Karkosa."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-227",
        "category": "World Mechanics",
        "statement": (
            "Kanja's Book 1 baseline density is 6,000x resting with a "
            "combat ceiling of approximately 18,000x. Ozmund's Book 5 "
            "combat ceiling reaches 26,000x-28,000x through calibrated "
            "Crown-Scar integration -- distinct from, and well above, "
            "his fixed 15,000x resting baseline (MCD-219)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full draft as pasted in-conversation: "proceed"'


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
            "batch": 39,
            "source_doc": "Tier_4_Preparation_Checklist.docx (cross-checked against the live ledger; most content already locked under MCD-090-100)",
            "source_id": "1M9AgpCP8Q_E7a2y6-N3kbQRYlP5abxaS",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "4.2"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
