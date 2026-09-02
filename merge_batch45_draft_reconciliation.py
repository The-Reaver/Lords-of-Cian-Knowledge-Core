#!/usr/bin/env python3
"""Batch 45: reconcile the 27 rules still sitting in "status": "draft" --
mostly early World Codex v3.4 (WC-) extractions and the remainder of the
Anu Un Ra Dossier (CULT-001/002/006/007/008/009) -- drafted from source
long ago but never taken through the explicit-approval lock step.

Cross-checked every one against the full live ledger (719 rules / 44
batches of accumulated corrections) for staleness and contradiction before
disposing of it:

- 25 rules are internally consistent with everything now locked (several
  independently corroborate later-locked material, e.g. WC-018/WC-020
  vs. the now-locked CULT-family Anu Un Ra rules) and are promoted to
  locked unmodified.
- WC-008 (regional split: Old Dominion 40% / Jicome 20% / Shattered
  Kingdoms 40%) directly contradicts the already-locked, later-dated
  MCD-094 (Shattered Kingdoms 75% / Sovereign Trust 15% / Jicome 10%,
  locked 2026-03-25). WC-008 is marked superseded rather than locked.
- WC-022 (five-book series structure) is promoted to locked but amended
  in place: its Book 4 and Book 5 titles were still placeholder "(TBD)"
  from before the series structure was finalized. The already-locked
  MCD-097 gives the real titles (Book 4, The Broken Meridian; Book 5,
  The Miner's Son) -- WC-022's Book 1 ("The Deposed King") and Book 2
  ("The Ever-Haunt") titles are the only source for those two titles
  anywhere in the ledger and are kept as-is.
"""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE_NOTE = (
    "Originally drafted from 'World Codex v3.4' (WC- rules) or the "
    "Lore Vault's 'DOSSIER: ANU UN RA' (CULT- rules) early in the "
    "project, before the explicit draft-then-approval workflow was "
    "formalized. Cross-checked against the full live ledger (719 rules, "
    "44 batches) in Batch 45 and found consistent with everything since "
    "locked; several independently corroborate later-locked material "
    "(e.g. WC-018's Five Champions roster and WC-020's Deposition "
    "account both match the now-locked CULT-family Anu Un Ra rules "
    "exactly). Promoted to locked per Abad's blanket authorization: "
    "\"you have my authorization to reconcile\"."
)

# Rules promoted to locked unmodified.
PLAIN_PROMOTIONS = [
    "WC-001", "WC-002", "WC-003", "WC-004", "WC-005", "WC-006", "WC-007",
    "WC-009", "WC-010", "WC-011", "WC-012", "WC-013", "WC-015", "WC-017",
    "WC-018", "WC-019", "WC-020", "WC-021", "WC-024",
    "CULT-001", "CULT-002", "CULT-006", "CULT-007", "CULT-008", "CULT-009",
]

BATCH_NOTE = (
    'Abad gave blanket authorization to review and resolve every '
    'remaining draft-status rule rather than approving each individually: '
    '"you have my authorization to reconcile"'
)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    by_id = {r["id"]: r for r in ledger["rules"]}

    for rid in PLAIN_PROMOTIONS:
        assert rid in by_id, f"{rid} not found"
        assert by_id[rid]["status"] == "draft", f"{rid} was not draft"
        by_id[rid]["status"] = "locked"
        by_id[rid]["note"] = SOURCE_NOTE

    # WC-008: contradicts the later, already-locked MCD-094 regional split.
    wc008 = by_id["WC-008"]
    assert wc008["status"] == "draft"
    wc008["status"] = "superseded"
    wc008["note"] = (
        "Superseded by the already-locked MCD-094 (Shattered Kingdoms "
        "75% / Sovereign Trust 15% / Jicome 10%, locked 2026-03-25), "
        "which directly contradicts this rule's regional percentages "
        "(Old Dominion 40% / Jicome 20% / Shattered Kingdoms 40%). "
        "Identified and resolved during the Batch 45 draft-reconciliation "
        "pass, per Abad's authorization: \"you have my authorization to "
        "reconcile\"."
    )

    # WC-022: promote, but fix the stale Book 4/5 "(TBD)" placeholders.
    wc022 = by_id["WC-022"]
    assert wc022["status"] == "draft"
    wc022["statement"] = (
        "Five-book series structure: Book 1 The Deposed King (murder "
        "investigation -> 10-Day Interregnum -> Pi-Awakening -> Great "
        "Breach epilogue), Book 2 The Ever-Haunt, Book 3 The Dark "
        "Monarch (Ozmund vs T.D.K., Crown-Scar revelation escalates), "
        "Book 4 The Broken Meridian (alliance converges, Orlok vs Vakas "
        "the draw), Book 5 The Miner's Son (three fronts, T.D.K. "
        "contained, Pyro peaks, Orlok transcends)."
    )
    wc022["status"] = "locked"
    wc022["note"] = (
        "Promoted to locked with Book 4/5 titles corrected in place: "
        "this rule's original text still carried '(TBD)' placeholders "
        "for Book 4 and Book 5, superseded by the already-locked "
        "MCD-097's real titles. Book 1 ('The Deposed King') and Book 2 "
        "('The Ever-Haunt') titles are this rule's own contribution -- "
        "no other locked rule states them. Resolved during the Batch 45 "
        "draft-reconciliation pass, per Abad's authorization: \"you have "
        "my authorization to reconcile\"."
    )

    ledger["batches_completed"].append(
        {
            "batch": 45,
            "source_doc": "Draft-status backlog reconciliation (25 World Codex v3.4 / Anu Un Ra Dossier rules promoted to locked, 1 corrected and promoted, 1 superseded by contradiction with already-locked MCD-094)",
            "source_id": None,
            "rule_count": 0,
            "status": "complete",
            "conflicts_found": 1,
            "conflicts_resolved": 1,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "4.8"
    ledger["last_updated"] = "2026-09-02"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    remaining_drafts = [r["id"] for r in ledger["rules"] if r["status"] == "draft"]
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")
    print(f"Remaining draft-status rules: {remaining_drafts}")


if __name__ == "__main__":
    main()
