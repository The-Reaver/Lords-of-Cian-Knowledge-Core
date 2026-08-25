#!/usr/bin/env python3
"""Batch 27: lock the 79 draft CC- rules from Batch 10 (Character Codex).

Not a new extraction -- Batch 10 already drafted these from
LORDS_OF_CIAN_Character_Codex_definitive.docx. They sat in status "draft"
because the two hard conflicts Batch 10 flagged (Pyro's mother, Lilith
Cyzak's dual identity) hadn't been ruled on yet. Both are now resolved:
Lilith via MCD-134 (CC-025 already marked superseded, no action needed here).
Pyro's mother via MCD-131/MCD-132/MCD-133 (deliberate in-universe
misdirection, not a continuity error) -- CC-045 and CC-046 are the two draft
rules that still carry the old "ended/killed" framing, so they get an
annotation pointing to the true account before locking, matching how
SBD-010 was handled for the same underlying conflict. The other 77 draft
CC- rules lock as-is, no textual changes.
"""
import json

LEDGER_PATH = "canon-ledger.json"

CC_045_REVISED = (
    "Stormbreaker (Kaelen) is the one who fought and defeated the Demaron "
    "entity possessing Pyro's mother during the Living Gate event, with "
    "Kanja's consent, and also serves as Pyro's guardian without Pyro "
    "knowing this history. The Codex's own framing that this 'ended her "
    "body's vessel' is deliberate in-universe misdirection (per MCD-133); "
    "MCD-131/MCD-132 are the sole authorial truth -- she survived, inverting "
    "the Gate into a forge and fusing into its architecture rather than "
    "being ended."
)

CC_046_REVISED = (
    "The Living Gate event: T.D.K. (Anu Un Ra) installed a voice-keyed "
    "'Living Gate' curse into Kanja's first and only wife (a veil-reader) as "
    "a containment response to her discovering his hidden architecture; her "
    "pregnancy amplified the Gate, a Demaron entity inhabited her, and Pyro "
    "and the three Dhar-Kael guardians (Varkul, Varruk, Sorya) were produced "
    "as her final act. The Codex's own framing that her 'body's vessel was "
    "ultimately ended' is deliberate in-universe misdirection (per MCD-133); "
    "MCD-131/MCD-132 are the sole authorial truth -- she survived, inverting "
    "the Gate into a forge and fusing into its architecture rather than "
    "being ended."
)

BATCH_NOTE = (
    'Abad approved locking all 79 draft CC- rules from Batch 10 in one pass: '
    '"Yes, lock all 79 now". CC-045 and CC-046 revised with an in-universe-'
    'misdirection annotation (matching SBD-010\'s precedent) before locking, '
    'since both still carried the pre-MCD-131/132/133 "killed/ended" framing. '
    'The other 77 draft rules lock unchanged. CC-025 stays "superseded" '
    '(already correct, Lilith Cyzak resolved via MCD-134). This closes the '
    'Character Codex extraction (Batch 10) fully.'
)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}
    draft_cc = [r for r in ledger["rules"] if r["id"].startswith("CC-") and r["status"] == "draft"]
    assert len(draft_cc) == 79, f"expected 79 draft CC- rules, found {len(draft_cc)}"

    assert rules_by_id["CC-045"]["status"] == "draft"
    assert rules_by_id["CC-046"]["status"] == "draft"
    rules_by_id["CC-045"]["statement"] = CC_045_REVISED
    rules_by_id["CC-046"]["statement"] = CC_046_REVISED

    locked_count = 0
    for r in draft_cc:
        r["status"] = "locked"
        locked_count += 1

    ledger["batches_completed"].append(
        {
            "batch": 27,
            "source_doc": "LORDS_OF_CIAN_Character_Codex_definitive.docx (Batch 10 drafts, approval pass only)",
            "source_id": "1gpcyrEhLybY9uZluuXB-A1g4t5e7zygn",
            "rule_count": locked_count,
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "3.0"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    cc_status = {}
    for r in ledger["rules"]:
        if r["id"].startswith("CC-"):
            cc_status[r["status"]] = cc_status.get(r["status"], 0) + 1
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")
    print(f"CC- status breakdown: {cc_status}")


if __name__ == "__main__":
    main()
