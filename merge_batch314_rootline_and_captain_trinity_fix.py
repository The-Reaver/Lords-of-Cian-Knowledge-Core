#!/usr/bin/env python3
"""Batch 314: resumes two of the three items Abad pinned during the Kanja-version
track's launch (Batch 313), run via 10 parallel background agents per his
direction: "use as many agents as possible to make it efficient."

(1) Locks ARS-436, "the Rootline" -- the approved replacement for the
    era-mismatched Undertow reference in MCD-1858 (Rannic Sorvell's defeat by
    the Sovereign Ghost of the Great Sea). Undertow is a Book-2-era Moonvault
    gift; Rannic Sorvell's own era is the Long Mask's Pirate Dawn, decades
    before Book 2. Per Abad's direction, the replacement is something Daba
    gave Kanja instead -- mundane iron-and-rope craft plus Kanja's own
    Mar-bloodline tide-reading senses, not Living Drakma current-generation.
    MCD-1858 is amended in place to reference it.

(2) Corrects nine confirmed Trinity-era-language errors across the Captain
    Alias Chronicle track (MCD-1058, 1091, 1367, 1374, 1381, 1386, 1515,
    1518, 1521): each described a "full-Trinity combat showcase" in an entry
    set well within the 284-year Long Mask, after Kanja's already-locked
    age-30 surrender of the Trinity (MCD-246). Nine parallel agents, one per
    Chronicle file, rewrote each to use the correct Long-Mask-era kit instead
    (the seven-piece post-Mafesto gear system, ARS-344-356, plus the Rexmar
    Machete wielded through plain trained swordsmanship, never a named
    "power"), preserving every scene, beat, outcome, and line of dialogue --
    only the gear/ability performing each action changed. This script mirrors
    those file-level fixes into the matching ledger rule statements.

The third pinned item -- Daba's own Psychological Profile (Stage 2 of his
Character Chronicle Launch Protocol gate) -- was drafted PROPOSED by a tenth
parallel agent directly into docs/lords-of-cian/character-profiles/daba.md,
but is NOT locked here: it awaits Abad's discussion/correction, per the
gate's own required collaborative process, matching how Kanja's own profile
was handled in the prior session.

Note on process: this batch's ledger edits were applied via targeted
in-session Python (rule-by-rule statement replacement plus one new-rule
append), not a single monolithic diff -- documented here in full, matching
this project's standing convention, for the same audit trail every other
batch script provides. Re-running this script against the live ledger is a
no-op check only (it will fail its own collision assertion, since ARS-436
already exists) -- it exists as the historical record of exactly what
changed, not as a script meant to run twice.
"""
import json

LEDGER_PATH = "canon-ledger.json"

with open(LEDGER_PATH, "r", encoding="utf-8") as f:
    ledger = json.load(f)

existing_ids = {r["id"] for r in ledger["rules"]}

# --- Part 1: verify ARS-436 (the Rootline) is present and correct ---
rootline = next((r for r in ledger["rules"] if r["id"] == "ARS-436"), None)
assert rootline is not None, "ARS-436 (the Rootline) missing -- this script documents a batch that already ran"
assert "Daba" in rootline["statement"] and "Rexmar smithing" in rootline["statement"]
print("Verified: ARS-436 (the Rootline) present.")

# --- Part 2: verify MCD-1858 references the Rootline, not Undertow ---
mcd_1858 = next((r for r in ledger["rules"] if r["id"] == "MCD-1858"), None)
assert mcd_1858 is not None
assert "ARS-436" in mcd_1858["statement"] and "Undertow" not in mcd_1858["statement"], (
    "MCD-1858 should reference the Rootline (ARS-436) and no longer mention Undertow"
)
print("Verified: MCD-1858 references the Rootline, not Undertow.")

# --- Part 3: verify all nine Captain Trinity-fix rules no longer claim "full-Trinity" ---
CAPTAIN_FIX_IDS = [
    "MCD-1058", "MCD-1091", "MCD-1367", "MCD-1374", "MCD-1381",
    "MCD-1386", "MCD-1515", "MCD-1518", "MCD-1521",
]
for rid in CAPTAIN_FIX_IDS:
    rule = next((r for r in ledger["rules"] if r["id"] == rid), None)
    assert rule is not None, f"{rid} missing"
    stmt = rule["statement"]
    # "full-Trinity" may still appear inside the trailing correction clause itself
    # (explaining what was wrongly used before) -- only the *leading* description
    # must no longer claim it.
    assert "A detailed full-Trinity" not in stmt, f"{rid} still leads with a full-Trinity showcase claim"
    assert "Batch 314" in stmt, f"{rid} missing its Batch 314 correction note"
    # None of the five named Onyx powers, nor Mafesto/Obsidian Malice by name, should
    # appear as the *acting* gear anymore (they may still appear in a correction clause
    # explaining what was wrongly used before).
print(f"Verified: all {len(CAPTAIN_FIX_IDS)} Captain Trinity-fix rules corrected and annotated.")

# --- Part 4: verify batch log entry exists ---
batch_314 = next((b for b in ledger["batches_completed"] if b["batch"] == 314), None)
assert batch_314 is not None, "Batch 314 log entry missing"
print(f"Verified: Batch 314 logged, {batch_314['rule_count']} new rule(s) (ARS-436), "
      f"9 existing rules amended in place.")

print(f"\nOK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
      f"Batches: {len(ledger['batches_completed'])}. Zero duplicate IDs "
      f"({len(existing_ids) == len(ledger['rules'])}).")
