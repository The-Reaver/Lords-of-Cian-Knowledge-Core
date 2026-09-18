#!/usr/bin/env python3
"""Batch 297: OPEN-007's two standalone world-phenomena interstitial chapters
(the Ever-Haunt, the Painter) -- content that MCD-338 left undrafted."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-18, no source document. Fulfills "
    "the 'full chapter content remains undrafted' gap MCD-338 left open when it "
    "resolved OPEN-007's structural question."
)

BATCH_NOTE = (
    "The two standalone world-phenomena interstitial chapters structurally confirmed at "
    "MCD-338 (Batch 69) -- content itself drafted for the first time, closing OPEN-007 in "
    "full. Proposed placement and register presented and agreed before drafting: the "
    "Ever-Haunt interstitial sits between Book 1 and Book 2, but deliberately does not "
    "retell any beat already covered by Book 2's own locked Act I-III structure "
    "(MCD-279-284) -- instead it follows an unconnected settlement (Ostrey Hollow) "
    "discovering a newly-loosed low-tier Ever-Haunt entity in the same general window as "
    "the Great Breach, dramatizing WC-019's five-tier classification at its lowest rung and "
    "CULT-198's 'inherited without understanding by the SBD' kennel detail at ground level; "
    "no named POV cast member appears anywhere in it. The Painter interstitial sits between "
    "Book 2 and Book 3, in a region the main cast never visits, elaborating CHAR-001's "
    "one-line dossier directly for the first time (a curious waystation worker, Coll, taken "
    "after asking to see inside the Painter's case; the recursive-canvas mechanic dramatized "
    "on the page) and giving the Painter an unconfirmed legend-name, 'Vantine,' without "
    "resolving his true origin -- matching the project's established precedent for leaving "
    "certain ancient/ambiguous figures deliberately open (Haku's fate, the Drowning Vault's "
    "120). Both chapters are true standalone atmospheric interludes: no named POV cast "
    "member appears in either, and neither resolves. New minor characters Senna, Doran, and "
    "Coll, all collision-checked clean against the full live ledger before drafting. Abad's "
    "approval: \"lock them up.\""
)

NEW_RULES = [
    {
        "id": "MCD-1621",
        "category": "World Mechanics",
        "statement": (
            "Interstitial chapter \"What the Kennels Forgot to Mean\" (full text at "
            "docs/lords-of-cian/interstitials/the-ever-haunt-what-the-kennels-forgot-to-mean.md), "
            "the first of two standalone world-phenomena interstitials confirmed at MCD-338, "
            "slotted between Book 1 and Book 2. An unconnected settlement (Ostrey Hollow) "
            "discovers a newly-loosed low-tier Ever-Haunt entity in the same general window as "
            "the Great Breach, dramatizing WC-019's classification and CULT-198's 'inherited "
            "without understanding by the SBD' kennel detail at ground level, deliberately not "
            "retelling any beat from Book 2's own locked Act I-III structure (MCD-279-284) and "
            "never naming any POV cast member. New minor characters Senna and Doran, "
            "collision-checked clean."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1622",
        "category": "World Mechanics",
        "statement": (
            "Interstitial chapter \"What the Canvas Kept\" (full text at "
            "docs/lords-of-cian/interstitials/the-painter-what-the-canvas-kept.md), the second "
            "of two standalone world-phenomena interstitials confirmed at MCD-338, elaborating "
            "the Painter (CHAR-001) between Book 2 and Book 3. A curious waystation worker, "
            "Coll, is taken by the Painter after asking to see inside his case; the "
            "recursive-canvas mechanic is dramatized directly for the first time, and the "
            "Painter is given an unconfirmed legend-name, 'Vantine,' with his true origin "
            "deliberately left open. No named cast member appears. New minor character Coll, "
            "collision-checked clean."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 2, f"expected 2 new rules, got {len(NEW_RULES)}"
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    open_decisions = ledger.get("open_decisions", [])
    for o in open_decisions:
        if o.get("id") == "OPEN-007":
            o["note"] = (
                o.get("note", "")
                + " Batch 297, 2026-09-18: full chapter content drafted and locked "
                "(MCD-1621, MCD-1622). OPEN-007 fully closed."
            )

    ledger["batches_completed"].append(
        {
            "batch": 297,
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
