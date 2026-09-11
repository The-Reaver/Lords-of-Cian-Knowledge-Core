#!/usr/bin/env python3
"""Batch 226: Maret Vos / Dol Maren pronoun and identity reconciliation.

Fixes in place (not new content):
  - MCD-593: pronoun "her" -> "him" (Maret Vos standardized to he/him, Abad's ruling).
  - MCD-751: statement corrected to name Dol Maren instead of Maret Vos, fixing a
    name mix-up (Maret Vos was erroneously given Dol Maren's already-locked
    crane-operator/shipwright role, CC-120/CC-121).
  - MCD-778: statement title and file path updated to match the renamed Chronicle
    file (the-wind-she-read-better.md -> the-wind-he-read-better.md), correcting
    Dol Maren's own mis-gendered pronoun in that entry.

No new rules. This is a reconciliation pass over existing locked rules, per Abad's
direct instruction to run it and his rulings on the two questions it raised.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

BATCH_NOTE = (
    'Abad: "do the Maret Vos pronoun reconciliation pass." Investigation found the '
    "inconsistency was wider than the two rules originally flagged (Batch 224's note) "
    "-- a real 3-3 split across nine Chronicle entries, plus a separate name mix-up "
    "where Maret Vos was erroneously given Dol Maren's already-locked crane-operator/"
    "shipwright role (CC-120/CC-121) in MCD-751, plus Dol Maren's own established male "
    "gender (CC-120) mis-rendered as she/her across seven further Chronicle files in "
    "the Sovereign Ghost of the Great Sea run. Presented both findings to Abad "
    'separately: "he/him" for Maret Vos\'s tiebreak, and "rename to Dol Maren" for the '
    "MCD-751 mix-up. All narrative files corrected directly (pronoun fixes do not "
    "change plot content or require a fresh draft/approval cycle); MCD-751's character "
    "identity change and the wider Dol Maren fix follow directly from already-locked "
    "canon (CC-120/CC-121's established male gender), not a new creative decision, so "
    "no separate approval cycle was needed for those beyond Abad's ruling on the mix-up "
    "itself."
)

STATEMENT_FIXES = {
    "MCD-593": (
        "\"The Night Maret Vos Almost Walked\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-night-maret-vos-almost-walked.md), Captain "
        "Alias Chronicle XVIII, wave 6 of ten (waves 6-15). Maret Vos tries to leave "
        "for good out of guilt/debt; Kanja lets him go freely, refusing to convert "
        "loyalty into obligation."
    ),
    "MCD-751": (
        "\"The Crane Operator's Other Ledger\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-crane-operators-other-ledger.md), The "
        "Industrial Myth Alias Chronicle XXVI, wave 9 of ten (waves 6-15). Dol Maren "
        "runs a parallel hazard ledger revealing unsafe conditions and wage theft are "
        "causally linked, forcing a combined settlement. Corrected, Batch 226: "
        "originally misattributed to Maret Vos, a different already-locked crew "
        "member with no established engineering competency -- the scene's content "
        "(hoist inspection, structural-load competence) matches Dol Maren's own "
        "already-locked shipwright/engineering role (CC-120/CC-121) exactly."
    ),
    "MCD-778": (
        "\"The Wind He Read Better\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-wind-he-read-better.md), Sovereign Ghost "
        "of the Great Sea Alias Chronicle XXIII, wave 8 of ten (waves 6-15). A pure "
        "sailing duel with zero Trinity powers: Dol Maren out-navigates a faster "
        "Trust courier ship. Corrected, Batch 226: title and file renamed from \"The "
        "Wind She Read Better\" / the-wind-she-read-better.md, fixing a mis-gendered "
        "pronoun for the already-locked, established-male (CC-120) Dol Maren."
    ),
}


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}
    for rule_id, new_statement in STATEMENT_FIXES.items():
        assert rule_id in rules_by_id, f"missing rule {rule_id}"
        rules_by_id[rule_id]["statement"] = new_statement

    ledger["batches_completed"].append(
        {
            "batch": 226,
            "date": str(date.today()),
            "source": "Reconciliation pass, no source document.",
            "rule_count": 0,
            "note": (
                "Corrects MCD-593, MCD-751, and MCD-778 statements in place (pronoun "
                "and character-identity fixes; no new rules, no plot changes). Nine "
                "additional Chronicle files corrected at the prose level only (not "
                "reflected in ledger statement text, which carried no pronoun in "
                "those cases): the-night-maret-vos-almost-walked.md, "
                "what-he-couldnt-be-in-two-places-for.md, "
                "what-maret-vos-carried-from-before.md, "
                "the-council-that-told-him-no.md, the-fire-he-chose-over-the-ambush.md "
                "(Maret Vos standardized to he/him); air-enough-for-six.md, "
                "the-gathering-at-the-ghost-fleets-anchorage.md, "
                "the-hull-dol-maren-wasnt-finished-with.md, "
                "the-storm-they-didnt-make.md, what-they-did-before-every-sailing.md, "
                "what-the-reef-wanted-to-take.md, the-wind-he-read-better.md "
                "(renamed from the-wind-she-read-better.md) (Dol Maren corrected to "
                "match his already-locked male gender, CC-120). " + BATCH_NOTE
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
