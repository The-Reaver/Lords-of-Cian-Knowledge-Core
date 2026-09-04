#!/usr/bin/env python3
"""Batch 55: Phase 1b, fifth document. MRD Five Book Arcs -- the full
five-book structural outline. Nearly all of it is already-locked
corroboration (Book titles, the Crown-Scar siphon mechanism, the Book 5
three fronts, Cassius Verehimu, Lucius Blackthorne, Nadea Thren, the
Gate Battle crossroads, the Twenty-Two Victories); this is the source
of a genuinely thin, high-value new slice: Nelle Adessi and Tomas
Grieve's full dossier and death scene (already locked only as a
one-liner, MCD-093), and Ozmund's permanent Crown-Scar shattering."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "MRD Five Book Arcs (Google Drive fileId "
    "1wnhx2dhZeVfgcjozXsunR1AFjjX-29YTBParNGe9Z-s, the Lore Vault "
    "copy). Fifth document drafted under Phase 1b of the "
    "pre-Book-1-era roadmap. Cross-checked against the full live "
    "ledger before drafting: the overwhelming majority of this "
    "document's five-book plot outline is already extensively locked "
    "from earlier batches (the Book titles at MCD-097/MCD-841-family, "
    "the Crown-Scar siphon mechanism at MCD-290 down to matching "
    "'thousands of taps' phrasing, the Book 5 three-front roster at "
    "MCD-221, Cassius Verehimu and Lucius Blackthorne in full, Nadea "
    "Thren's defection and Ezio patronage, the Book 5 Gate Battle "
    "crossroads moment, and the Twenty-Two Victories) -- treated as "
    "confirmed-redundant corroboration and not re-drafted. The "
    "genuinely new material is narrow: Nelle Adessi and Tomas Grieve's "
    "full biographical dossier and death-scene mechanics (previously "
    "locked only as a one-line summary, MCD-093), and Ozmund's "
    "permanent Crown-Scar command-resonance shattering, which nothing "
    "else in the ledger states."
)

NEW_RULES = [
    {
        "id": "CC-123",
        "category": "character-crew",
        "statement": (
            "Nelle Adessi: 34 years old, a former Cestari freed through "
            "Cooper and Lilith's bureaucratic intervention, density 38x "
            "(the lowest of any named character in the series). "
            "Becomes the Unchained Kingdom's first civilian physician, "
            "keeping a medical ledger with a 'What They Carried' "
            "section documenting the untreated damage the Maw and the "
            "Scrip economy left on freed bodies. Widens her clinic's "
            "doorway for Varkul without being asked, giving Pyro a "
            "room where people are healed rather than broken; Damu "
            "mentors her, recognizing a non-Variant medical instinct "
            "that reads people the way he reads blood."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-124",
        "category": "character-crew",
        "statement": (
            "Tomas Grieve: roughly 190 years old, a Shattered Kingdoms "
            "tradesman, density 220x, with 150 years' prior experience "
            "building deliberately temporary structures for nomadic "
            "and pirate populations. Arrives at the Unchained Kingdom "
            "as its first client asking for something permanent, and "
            "calls Ozmund by his first name from their earliest meeting "
            "(hauling foundation stones together) rather than by "
            "title. His housing work includes doors with interior "
            "locks specifically for privacy, not security -- freed "
            "Cestari's first doors they control themselves. His "
            "friendship with Nelle Adessi (shared wall between clinic "
            "and workshop) is deliberately unremarkable: professional "
            "neighbors, daily lunches, mutual small favors."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-125",
        "category": "character-crew",
        "statement": (
            "Extends MCD-093 (The Beloved): the 94-second Ronin "
            "operation's actual mechanics. The Ghost infiltrated the "
            "Unchained Kingdom six weeks prior as a freed Cestari with "
            "forged processing numbers, mapping the civilian hub's "
            "schedule by attending Nelle's clinic for a fabricated "
            "injury -- she treated the Ghost with genuine care, "
            "unknowingly recording their visit in her ledger. The "
            "Silence neutralizes two checkpoint guards as a "
            "demonstrative opening. The Blade kills Nelle mid-sentence "
            "at her ledger (her 0.8-second signature kill window); "
            "Tomas, hearing the disturbance through the shared wall he "
            "built, dies reaching toward it rather than reaching the "
            "door. The Silence braids Tomas's carpenter's square into "
            "an existing trophy cord of 47 military insignia -- a "
            "builder's tool alongside soldiers' medals."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-126",
        "category": "character-crew",
        "statement": (
            "The aftermath of CC-125: Damu reads Nelle's residual "
            "biological data (cardiac arrest was instantaneous, "
            "cortisol normal -- she never knew) and sits beside her "
            "body for forty minutes. Cooper's response on arrival: "
            "'The numbers don't work.' Ozmund closes Nelle's ledger, "
            "its final entry an unfinished name. Pyro loses the one "
            "space in his life that wasn't about war. The deaths "
            "harden the already-locked Dark Monarch escalation "
            "(MCD-093/related): confirmation, in Ozmund's own "
            "reasoning, that restraint and mercy get people killed, "
            "accelerating his righteous-excess prosecution of the "
            "Shogunate war rather than causing it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-319",
        "category": "World Mechanics",
        "statement": (
            "Ozmund permanently shatters the Crown-Scar's command "
            "resonance during a T.D.K.-fired siphon test (Book 3), "
            "extending MCD-290's siphon architecture: his Karesian "
            "maternal bloodline (Val Mirel Kareth) resists and breaks "
            "the connection through biological resistance and force of "
            "will. The cost is permanent -- the command-frequency "
            "compulsion that held the Unchained Legion's formation in "
            "Book 2 is gone for good, and from this point Ozmund leads "
            "only through earned loyalty. This is the mechanical setup "
            "for Book 5's Line front holding 'without compulsion' "
            "(payoff for the already-locked MCD-221 roster): 150,000 "
            "freed Cestari choosing to stand, not being compelled to."
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
            "batch": 55,
            "source_doc": "MRD Five Book Arcs -- Phase 1b, fifth document: confirmed nearly-total redundancy with already-locked material; drafted only Nelle Adessi/Tomas Grieve's full dossier and death-scene mechanics, and Ozmund's permanent Crown-Scar shattering",
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "5.8"
    ledger["last_updated"] = "2026-09-04"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
