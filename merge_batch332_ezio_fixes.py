#!/usr/bin/env python3
"""Batch 332: Phase 2 fable-review fixes, Ezio Valcari Character Chronicle material.

Mechanical/reconciliation fixes only. Amends ARS-404's rule statement to
remove a real-world-term leak ("the way a doctor reads an X-ray"). All
other findings from the review were either applied as prose-only
corrections to the one locked Chronicle file (MCD-1876, no ledger
statement change needed) and to the three still-UNLOCKED/PENDING-APPROVAL
draft Chronicles II-IV (corrected for internal consistency but NOT
locked -- they remain pending Abad's own approval), or are flagged in
CLAUDE.md as needing Abad's direct creative ruling (Ezio's true age
against CC-028; whether Fermand is a sixth knower of Ezio's classified
capability).
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Phase 2 fable-review of Ezio Valcari's Character Chronicle material "
    "(his profile doc, CC-073, MCD-1875, MCD-1876, CC-156, and the three "
    "pending-approval Chronicles II-IV) against the full ledger. "
    "Mechanical/reconciliation subset only."
)

AMENDMENTS = {
    "ARS-404": (
        "Extends ARS-210 (that entry's Attia's Rite/cane-sword listing for Ezio "
        "remains superseded in favor of Lauris per ARS-359 and is not restated "
        "here): the Archive-Key is a set of twelve hair-thin Living Drakma "
        "filaments, bio-tuned to Ezio's own resonance, housed in the hollow shaft "
        "of the Cipher Cane -- a plain, unremarkable cane that reads publicly as a "
        "theorist's affectation, privately as his only concealed-carry prop, "
        "distinct from and never confused with Attia's Rite. The filaments defeat "
        "locks and mechanisms by touch-reading their internal structure through "
        "micro-vibration feedback -- he identifies the correct configuration by "
        "feel, the way a trained hand reads structure through touch alone, then "
        "shapes a filament to match it. A secondary function lets the filaments "
        "interface directly with Directorate Drakma data-plates, reading sealed "
        "classified SBD records back to him as touch-interpreted micro-vibration. "
        "Structural Interrogation -- mapping a room's density and structure in two "
        "taps -- is performed with the same Cipher Cane."
    ),
}


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}

    amended = []
    for rid, new_statement in AMENDMENTS.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        rules_by_id[rid]["statement"] = new_statement
        amended.append(rid)

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule IDs found"

    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({
        "batch": next_batch,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": 0,
        "note": (
            "Phase 2 fable-review of Ezio Valcari's Character Chronicle material. "
            "Amends ARS-404 to remove a real-world-term leak ('the way a doctor "
            "reads an X-ray') from its rule statement. Also fixed, prose-only (no "
            "ledger-statement change needed): MCD-1876's own locked Chronicle I "
            "file (a settlement-count contradiction reconciled to three "
            "throughout; a dangling numeric age claim reworded pending Abad's "
            "ruling on Ezio's true age; two cosmetic fixes); and internal-"
            "consistency fixes to the three still-unlocked/pending-approval draft "
            "Chronicles II-IV (dangling numeric spans reworded, an incorrect "
            "header claim about Lauris Chronicle I corrected, a CC-108 overstatement "
            "softened) -- these three drafts remain UNLOCKED/PENDING APPROVAL, not "
            "locked by this batch. The profile doc's three different Industrial "
            "Myth appearance counts (84/31/35) were clarified in place with one "
            "defining sentence rather than changed, since all three measure "
            "genuinely different things. Two findings require Abad's own direct "
            "creative ruling and are deliberately left unresolved: Ezio's true age "
            "(CC-028's '75 years old' is contradicted by MCD-373's placement of "
            "him at roughly age 16 at the Furnace District Strike, which implies "
            "roughly 309 at Book 1, and by MCD-194/MCD-1661's two-centuries-old "
            "Lauris-recruitment arrangement); and whether Fermand Aurelias is a "
            "sixth knower of Ezio's classified combat capability (pending "
            "Chronicle IV's dialogue reads as telling him, in tension with its "
            "own header and Chronicle III's header, both of which assert he stays "
            "outside the closed five-person list -- WC-016/CC-027/CC-111)."
        ),
    })

    old_version = float(ledger["ledger_version"])
    ledger["ledger_version"] = str(round(old_version + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(
        f"OK: {len(ledger['rules'])} total rules, {len(ledger['batches_completed'])} "
        f"batches, ledger_version {ledger['ledger_version']}, zero duplicate IDs. "
        f"{len(amended)} rule statements amended: {', '.join(amended)}."
    )


if __name__ == "__main__":
    main()
