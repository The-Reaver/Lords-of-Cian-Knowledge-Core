#!/usr/bin/env python3
"""Batch 99: Xaragua Chronicle IV, "The One He Chose to Teach" (MCD-362)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-10, no source document. Fourth Xaragua Chronicle, "
    "dramatizing Naya, Arturo's protegee, directly for the first time -- PH2-061 names her only in "
    "passing as flagged-for-future-payoff material. Full narrative text at "
    "docs/lords-of-cian/chronicles/xaragua-chronicle-iv-the-one-he-chose-to-teach.md."
)

NEW_RULES = [
    {
        "id": "MCD-362",
        "category": "phase2-homage-chronicle",
        "statement": (
            "Xaragua Chronicle IV, \"The One He Chose to Teach\" (full narrative text at "
            "docs/lords-of-cian/chronicles/xaragua-chronicle-iv-the-one-he-chose-to-teach.md), the "
            "fourth Xaragua Chronicle, set after Xaragua Chronicle II (MCD-337) in the 'modern' "
            "Arturo era -- chronologically the most recent of the four Xaragua Chronicles. "
            "Protagonist Arturo Salvatierra Duho (PH2-061). Introduces and dramatizes Naya, his "
            "protegee, directly for the first time (a new named character, collision-checked "
            "against the full live ledger, zero prior hits) -- found by Arturo as a six-year-old "
            "sole survivor of a tenement fire, her grief-held stillness deliberately mirroring and "
            "not restaging Arturo's own dock-boy-cohort loss (MCD-361). Sixteen years later, Arturo "
            "hands her, for the first time, sole authority to hear and resolve a dispute between "
            "two of the Five Families' captains over disputed dock territory; she resolves it "
            "through patience and listening rather than force, matching the ethos of 'No Blood at "
            "My Table.' Arturo confirms afterward that the test was never of her judgment (already "
            "proven over years) but of his own willingness to let someone else's judgment carry "
            "equal weight to his own. Explicitly reaffirms Yaisa's (PH2-062) unique standing as the "
            "only person who can banter with Arturo unguarded, declining to extend it to Naya; the "
            "separate flagged long-arc promise that Kanja himself eventually earns that same "
            "standing remains untouched, left for a future entry. Kanja appears only briefly and at "
            "the margins, granted no command, intervention, or resolution credit; his passage "
            "through NYC was already granted in Xaragua Chronicle II, so no re-introduction or "
            "re-testing occurs here. No proper-noun collisions beyond Naya, checked before drafting."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "lock it."'


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
            "batch": 99,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-10, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "Xaragua Chronicle IV (MCD-362), 'The One He Chose to Teach' -- dramatizes Naya, "
                "Arturo's protegee, directly for the first time, fulfilling PH2-061's "
                "flagged-for-future-payoff reference. " + BATCH_NOTE
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
