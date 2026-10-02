#!/usr/bin/env python3
"""Batch 338: Phase 3 fable-review fixes, the Kanja-version Chronicle track.

Amends MCD-1865 (an anachronistic post-Breach custodial-authority
reference, decades before the Great Breach that actually occurs at the
age this defeat is locked) and MCD-1588 (a stale "nine years prior"
figure the Batch 335 Daba prose fix corrected to "three years ago" but
never propagated to this rule's own statement).
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Phase 3 fable-review of the Kanja-version Chronicle track (Chronicles "
    "I-III, MCD-1866-1868) against the full ledger and corpus."
)

AMENDMENTS = {
    "MCD-1865": (
        "Renfel Auberon (CC-157) is eventually cornered and his contained "
        "Ever-Haunt stock safely neutralized by a coordinated application of "
        "CULT-197's own named three-source Anti-Resonance countermeasure -- "
        "Onyx's Cadence Ruin, Sephtis's Chrono-Anchor bells, and Ironbane's King's "
        "Roar -- fielded together for the first time on the page against a real "
        "threat rather than described only as a standing procedure, forcing every "
        "entity in Auberon's custody to flee or collapse to its lowest tier rather "
        "than be harmed outright. Auberon himself is captured alive rather than "
        "killed: years of unsafe proximity to his own 'merchandise' have already "
        "left him partially Green-Mark-contaminated (CULT-198), making him more a "
        "cautionary case than a mastermind, and he is handed to the older "
        "custodial apparatus that already tracks anomalies of this kind (the "
        "defeat sits at age 27, MCD-1868, well before the Great Breach) rather "
        "than to ordinary Trust law enforcement. Chronicle prose drafted Batch "
        "313 (MCD-1868)."
    ),
    "MCD-1588": (
        "Daba Chronicle XVIII, \"The Weight a Crossing Cannot Carry\" (full narrative "
        "text at docs/lords-of-cian/chronicles/daba-chronicle-xviii-the-weight-a-"
        "crossing-cannot-carry.md), the eighteenth entry in Daba's own Chronicle "
        "series. Dramatizes the discipline of making concentrated force irrelevant "
        "via a recounted (not restaged) 1804 operation three years prior: eight of "
        "Daba's fighters narrowed a forty-one-strong Trust ford crossing with "
        "submerged stake lines to three men abreast, ensuring only six soldiers "
        "could ever be engaged at once regardless of the column's total size, "
        "taking twelve losses before the rest of the column understood the water "
        "itself was refusing them reinforcement. Explicitly the most direct "
        "conceptual ancestor of Kanja's own later Dredge-Line Ambush (MCD-231). No "
        "new named characters."
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
            "Phase 3 fable-review of the Kanja-version Chronicle track (3 "
            "entries, Chronicles I-III). Amends MCD-1865 (its 'post-Breach "
            "anomalies' custodial-authority phrasing was anachronistic -- the "
            "Great Breach doesn't occur until Book 1's epilogue, decades after "
            "this defeat's own locked age-27 placement at MCD-1868; also records "
            "that Chronicle prose now exists) and MCD-1588 (a stale 'nine years "
            "prior' figure the Batch 335 Daba prose fix corrected to 'three years "
            "ago' in the Chronicle file itself but never propagated to this "
            "rule's own statement). Also fixed, prose-only: Chronicle III's "
            "header mis-dated the Gale Straits by two years and gave Sephtis an "
            "age roughly 200 years too old (stale age-arithmetic, same error "
            "class as the Lauris sweep); an entity-count arithmetic error (2+3+2 "
            "summed to seven, not six); Chronicle I's Scrip-Forge wage-shortfall "
            "dialogue conflated a 14%-content note with a 14% shortfall against "
            "its 38% stamp, corrected to state both figures; Chronicle II's "
            "header age specificity loosened from 'fifteenth year' to "
            "'seventeenth year' to match the only locked constraint (before "
            "Onyx's age-17 bonding) rather than an unforced tighter pin; a "
            "garbled line of dialogue punctuation fixed. The profile doc "
            "(kanja-haku-rexmar.md) had six stale/garbled lines corrected: the "
            "founding crew's CC- dossier gap (now filled, CC-158/159/160); the "
            "Industrial Myth's age (19 -> 21, matching Batch 321); a garbled "
            "sentence conflating Fermand and Onyx as the same narrator; a "
            "misattributed Ghost-Lattice/storm-doctrine citation; the track's own "
            "stale 'zero entries' status; a dangling empty bullet. Four findings "
            "need Abad's own creative/worldbuilding ruling and are deliberately "
            "left unresolved: a standing track convention mapping Rebellion-era "
            "age bands to Onyx's VB-026 presence-growth level, since write order "
            "and in-universe age currently disagree about how much Onyx should "
            "show at a given age; whether the track's narrator codas should be "
            "first-person or 'the blade' third-person by age band; locking "
            "Ironbane's (and possibly Soulreaver Zora's) Rebellion-era joining "
            "date, since Chronicle III is currently the only place in the entire "
            "corpus that puts Ironbane in Kanja's company before the Long Mask; "
            "and naming (or explicitly ruling out the SBD as) the 'older, quieter "
            "apparatus' Auberon is handed to."
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
