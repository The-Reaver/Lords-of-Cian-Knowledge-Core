#!/usr/bin/env python3
"""Batch 56: Phase 1b, sixth document. Complete Structural Outline --
a near-duplicate planning draft of "MRD Five Book Arcs" (Batch 55), so
nearly all load-bearing material is already locked. Drafts only the
genuinely new secondary numbers, two new minor characters, one new
named ability, and resolves two real conflicts (one numeric, one
naming collision) found during triage."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "My_Rivals_Distance_Complete_Structural_Outline_Definitive (Google "
    "Drive fileId 1T-q9EfqxHVIyN9p8CZg8nqdA7FrTqx63d_9JcCC1gzg, the "
    "Lore Vault copy). Sixth document drafted under Phase 1b of the "
    "pre-Book-1-era roadmap. A background triage pass found this "
    "document to be a near-duplicate planning draft of MRD Five Book "
    "Arcs (Batch 55) -- nearly every load-bearing plot beat, named "
    "villain, and major mechanic is already locked, largely from the "
    "same underlying source material. Two real conflicts were found "
    "and resolved before drafting: the document's claim that the "
    "Sovereign Pier Accords were negotiated ~284 years before the "
    "Fulfillment Ceremony contradicts the already-locked MCD-091 "
    "(~296 years), likely a conflation with Kanja's unrelated 284-year "
    "Long Mask duration -- MCD-091 controls per Abad's ruling, and "
    "this document's figure is not drafted. The document names Red "
    "Beard's reckoning technique against the Silence 'the Manumission,' "
    "which collides with the already-locked ARS-140 (Azar Dreadlord's "
    "kit) -- renamed 'the Unchaining' per Abad's ruling, tying it to "
    "the already-established Unchained Legion/Unchained Kingdom "
    "terminology."
)

NEW_RULES = [
    {
        "id": "MCD-320",
        "category": "World Mechanics",
        "statement": (
            "T.D.K. detects the Pi-Awakening signal specifically from "
            "the Spire of Obolus, activating legacy dependencies with "
            "the line 'The Anomaly has awakened. Deploy the Coursers.' "
            "(extends the already-locked Great Breach epilogue "
            "material)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-127",
        "category": "character-crew",
        "statement": (
            "Two new Aethel-Gard figures: Elora-Grace runs the "
            "diplomatic mission that secures Aethel-Gard's commitment "
            "to the alliance; Thane-Gorm, 'the Root-Born Thane,' is the "
            "leader who recognizes the Verehimu bloodline and formally "
            "commits Aethel-Gard's forces (Book 3)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-384",
        "category": "avatar-arsenal",
        "statement": (
            "Extends CC-059 (the Zenith-Rod's ceiling bump from Kanja's "
            "reforge): the reforge itself takes 14 hours, and the rod "
            "is dual-configuration -- an 8cm carry form worn behind the "
            "ear, extending to 6 meters for engagement -- with a "
            "density feedback loop adding roughly 20-25% under active "
            "use."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-321",
        "category": "World Mechanics",
        "statement": (
            "Extends MCD-218 (Kanja's Book 3 push to ~32,000x): his "
            "Book 3 baseline figures underneath that overshoot are "
            "9,000x resting with a controlled spike ceiling of "
            "approximately 27,000x."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-322",
        "category": "World Mechanics",
        "statement": (
            "Extends MCD-218: the Shogunate's elite guard, 'the Seven "
            "Sin-Eaters,' number seven total; six engage the allied "
            "defenses directly, while Orlok's demonstrative set-piece "
            "engagement is specifically against a squad of three."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-323",
        "category": "World Mechanics",
        "statement": (
            "Extends MCD-219/MCD-290: Damu's Crown-Scar "
            "activation-detection catches the root-access signature "
            "roughly 1.7 seconds before it fires, triggering a "
            "two-part counter-response -- a neural-pathway-disrupting "
            "compound Damu injects, paired with a Living-Drakma-gorget "
            "frequency pulse Kanja applies via the Forgewright, tuned "
            "to the Rexmar bio-signature."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-324",
        "category": "World Mechanics",
        "statement": (
            "Extends the already-locked Val Mirel/Val Saeryn "
            "Kareth-sister material: the artifacts' delivery to Lauris "
            "ran through a 210-year, 14-intermediary operation across "
            "three nations. Fermand identifies the pattern via "
            "Predictive Oracle node-failure analysis (43 nodes over "
            "210 years matching the delivery architecture exactly), "
            "remarking to Ezio that 'the only person who runs an "
            "operation for two centuries without leaving a signature "
            "is someone who has been running operations longer than "
            "the institution being dismantled has existed.' Val "
            "Saeryn's involvement is suspected, not confirmed, at this "
            "point in the story."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-325",
        "category": "World Mechanics",
        "statement": (
            "During the Broken Meridian expedition's deepest descent, "
            "the Talisman of Mao registers an uncatalogued density "
            "signature matching Kinetic Concentration; separately, "
            "Damu finds and logs (without yet understanding it) a "
            "'familial' secondary resonance in Kanja's blood in the "
            "Red Index -- new foreshadowing detail, not previously "
            "locked."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-326",
        "category": "World Mechanics",
        "statement": (
            "Extends MCD-306 (the Exchange Protocol's inability to "
            "adapt to the Pi-Awakening frequency): Soledad Keme's "
            "account specifies T.D.K. outwaited rather than outfought "
            "the Merak rulers, and that the adaptation-loop failure "
            "was observed fourteen times across a 200-year period, "
            "roughly 50,000 years before Book 1, with no accumulation "
            "across attempts."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-327",
        "category": "World Mechanics",
        "statement": (
            "The Broken Meridian severance quest's concrete mechanic: "
            "severing the Crown-Scar siphon at scale requires a "
            "specific resonance frequency applied through a physical "
            "Meridian Engine fragment -- which T.D.K. possesses, "
            "making its recovery the explicit Book 5 objective."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-328",
        "category": "World Mechanics",
        "statement": (
            "The Obsidian Prefecture commits 200,000 legionaries to "
            "the alliance's western front (extends the already-locked "
            "Prefecture/Vestige manipulation material)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-128",
        "category": "character-crew",
        "statement": (
            "Extends MCD-095/098/220: Toussaint Louverture is 3,181 "
            "years old with a resting density of 14,000x."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-385",
        "category": "avatar-arsenal",
        "statement": (
            "Valen's 'White World': a time-dilation perceptual "
            "technique letting him operate inside the Blade's own "
            "0.8-second kill window during their Book 5 reckoning -- "
            "not previously named in the ledger."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-329",
        "category": "World Mechanics",
        "statement": (
            "The Warbody's five documented exploitable gaps, as a "
            "named framework (extends the general gap-finding concept "
            "at CC-036): mobility, seams, accumulation, overcommitment, "
            "and reset windows."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-330",
        "category": "World Mechanics",
        "statement": (
            "Extends MCD-227 (Ozmund's Book 5 combat ceiling, "
            "26,000x-28,000x, already locked): his calibrated "
            "Crown-Scar integration produces a 0.3-second recognition "
            "reflex against the Warbody's own Crown-Scar architecture."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-386",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-358 (Lauris's Density Saturation): in the "
            "Book 5 Engine front, she specifically targets the "
            "Warbody's reset windows (MCD-329), denying it clean "
            "stability-debt clearance so each successive reset runs "
            "progressively longer and less complete."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-387",
        "category": "avatar-arsenal",
        "statement": (
            "Renamed per a naming collision with the already-locked "
            "ARS-140 (Azar Dreadlord's 'the Manumission'): Red Beard's "
            "reckoning technique against the Silence (extends "
            "MCD-093/the Ronin reckonings) is 'the Unchaining,' tying "
            "into the already-established Unchained Legion/Unchained "
            "Kingdom terminology -- it 'makes the sound of a lock "
            "breaking... the sound of a ledger closing.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = (
    'Abad ruled on both flagged items directly: "default to keeping '
    'MCD-091\'s 296 as controlling and treating this document\'s 284 '
    'as the error" and, for the naming collision, \'"the Unchaining"\'.'
)


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
            "batch": 56,
            "source_doc": "My_Rivals_Distance_Complete_Structural_Outline_Definitive -- Phase 1b, sixth document: confirmed near-total redundancy with MRD Five Book Arcs (Batch 55); drafted only genuinely new secondary numbers, two new minor characters, one new named ability, and resolved two real conflicts (a numeric contradiction and a naming collision)",
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 2,
            "conflicts_resolved": 2,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "5.9"
    ledger["last_updated"] = "2026-09-04"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
