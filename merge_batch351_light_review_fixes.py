#!/usr/bin/env python3
"""Batch 351: light Fable-review reconciliation fixes for Batch 350 (Daba LVII-LVIII) and the
stale 'no prose drafted' clauses on the two villain rules they dramatize. No new facts."""
import json

LEDGER_PATH = "canon-ledger.json"
SOURCE = ("Light Fable-model consistency review, 2026-10-02, of all work since the Phase 5 MCD-core "
          "pass (Batch 349 fixes, Daba Chronicles LVII-LVIII, the archive roadmap, the Kanja "
          "Chronicle IV draft). Mechanical reconciliation only.")

AMENDMENTS = {
    "MCD-1878": [
        ("the same narrowing-into-a-bottleneck logic a much younger Kanja learned on a disused footbridge during his mentorship with Daba (MCD-1568, Daba Chronicle XVIII)",
         "the same narrowing-into-a-bottleneck logic 1804 itself established at the ford crossing recounted in Daba Chronicle XVIII (MCD-1588), the conceptual ancestor of Kanja's own Dredge-Line Ambush (MCD-231)"),
        ("consistent with his profile's standing note that no Chronicle in the corpus shows him personally endangered or tested in combat (Chronicle LII remains his only physical-threat entry)",
         "consistent with his profile's note that Chronicle LII (MCD-1870) remains the only entry putting him personally in physical danger"),
    ],
    "MCD-1879": [
        ("consistent with his established record-keeping habit (MCD-1610) of logging only deaths",
         "consistent with his established record-keeping habit (MCD-1610) of logging only 1804's own dead, never operations or enemy losses"),
    ],
    "MCD-1855": [
        ("No Chronicle prose has been drafted for this defeat; it is queued exactly as Batch 287 queued Tunji and Femi before their own Chronicles were written, pending Abad's review and explicit approval before any scene is drafted.",
         "Dramatized in Daba Chronicle LVII (MCD-1878, Batch 350)."),
    ],
    "MCD-1861": [
        ("No Chronicle prose has been drafted; this is a queued future Daba-wave beat, pending Abad's review.",
         "Dramatized in Daba Chronicle LVIII (MCD-1879, Batch 350)."),
    ],
}

BATCH_NOTE = (
    "Light Fable review of everything since the last review pass, per Abad's direction: "
    "'everything we've worked on so far since the last Fable review should be given a light "
    "Fable review unless it's too costly.' Batch 349's amendments came back clean. Fixed here: "
    "MCD-1878's footbridge/ford conflation (Daba Chronicle XVIII is a ford, not a footbridge; "
    "the footbridge lesson is Kanja Chronicle II's unrelated unwatched-approach lesson) and its "
    "stale 'never endangered' clause (Chronicle LII); MCD-1879's misdescription of Daba's tally "
    "(MCD-1610 logs 1804's own dead only); the stale 'no Chronicle prose drafted' clauses on "
    "MCD-1855/MCD-1861. Matching prose fixes applied to Daba Chronicles LVII/LVIII (including "
    "LVIII giving 1804 the Slab Compact's bloodline motive, corrected per MCD-1861/CULT-148/149) "
    "and daba.md. Reconciliation only, no new facts."
)


def main():
    with open(LEDGER_PATH, encoding="utf-8") as f:
        ledger = json.load(f)
    rules = {r["id"]: r for r in ledger["rules"]}
    for rid, pairs in AMENDMENTS.items():
        s = rules[rid]["statement"]
        for old, new in pairs:
            assert s.count(old) == 1, (rid, old[:60], s.count(old))
            s = s.replace(old, new)
        rules[rid]["statement"] = s
    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({"batch": next_batch, "source": SOURCE,
                                        "rules_affected": len(AMENDMENTS), "note": BATCH_NOTE})
    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = "2026-10-02"
    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")
    ids = [r["id"] for r in ledger["rules"]]
    print(f"OK: {len(ids)} rules, batch {next_batch}, ledger_version {ledger['ledger_version']}, "
          f"zero duplicate IDs: {len(ids) == len(set(ids))}")


if __name__ == "__main__":
    main()
