#!/usr/bin/env python3
"""Batch 75: formally declares Pre-Book-1 Foundation Complete
(roadmap Step 5). A milestone marker, not an in-fiction fact -- logged
as a batches_completed entry only, no new rules."""
import json

LEDGER_PATH = "canon-ledger.json"

BATCH_NOTE = 'Abad: "lock it"'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    ledger["batches_completed"].append(
        {
            "batch": 75,
            "source_doc": (
                "Pre-Book-1 Foundation Complete declaration (roadmap "
                "Step 5). The 'Pre-Book-1 Foundation Complete' "
                "checklist (docs/lords-of-cian/"
                "project-roadmap-and-status.md) is fully closed: (1) "
                "the 3 genuinely-open decisions (OPEN-005/007/008) "
                "resolved, Batch 69; (2) World Atlas scoping and "
                "correction, Batch 68; (3) Chronicles I-VIII rewrite "
                "against the corrected Atlas, Batches 70-71; (4) small "
                "backlog triage (Efa Gol/Pell Ostra, Undertow, two "
                "unopened docs), Batches 72-74; (5) this declaration. "
                "This closes the bounded, achievable 'foundation' "
                "milestone that lets canon work hand off cleanly "
                "toward the archive app. It does not mean canon work "
                "stops: the genuinely open-ended Phase 2 homage-era "
                "expansion (more cities, more territory Chronicles, "
                "Arturo's prequels, more Kanja Chronicles, general "
                "world-building) was never gated by this milestone and "
                "continues indefinitely in parallel, exactly as it has "
                "throughout. Separately and still unresolved: the "
                "archive-app device-bridge session (real Brain Trust "
                "review) remains blocked pending a Cowork/local "
                "session with the device bridge live -- unrelated to "
                "and not gated by this milestone."
            ),
            "source_id": None,
            "rule_count": 0,
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "7.8"
    ledger["last_updated"] = "2026-09-06"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")
    print("Pre-Book-1 Foundation Complete declared.")


if __name__ == "__main__":
    main()
