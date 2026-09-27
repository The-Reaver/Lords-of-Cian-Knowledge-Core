#!/usr/bin/env python3
"""Batch 312: consolidates three parallel background-agent drafts, per Abad's
direction to work all four items from his 2026-09-27 sync-check list
continuously and uninterrupted:

1. The SEALBLACK Detachment Protocol + SBD institutional archive expansion
   (SBD-050 through SBD-065): the detachment classification/authorization/
   records system, five new anomaly-class entities, four new named
   detachments, four new named facilities.
2. Eleven new pre-Book-1 defeatable villains, spread across five registers
   (CC-147 through CC-157), plus their companion defeat rules
   (MCD-1855 through MCD-1865).
3. Nine new gifts/weapons/economic tools for the Unchained Legion's Book 2-5
   era (ARS-427 through ARS-435), extending the Ten Gifts/Arsenal of Cian.

Item 4 from Abad's list (checking how Book 1+ is actually written, to keep
this material compatible) was research done directly in-conversation, not a
drafting task -- confirmed the investigative-noir murder-mystery structure
is already locked at MCD-070 and the Voice Bible's Zafonian Gothic Noir
pillar (VB-001/003), and used that as the design constraint for item 2's
villain registers (institutional/mid-tier, not mastermind-tier).

One real contradiction was caught and fixed before this merge: the gear
agent's original ARS-429 claimed to be Valeria Korth's "first personal
weapon ever," which directly contradicts CC-104's already-locked Weaver's
Kit and Compass Needle. Corrected to a ranged-offensive extension of her
existing kit rather than a false "first weapon" claim.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = (
    "Three parallel background-agent drafts, consolidated 2026-09-27: "
    "original invention grounded throughout in already-locked mechanics "
    "(SBD-/CULT-/WC-007/ARS- SBD material; MAW-/CULT-/WGD- for the villain "
    "roster; ARS-/WC-007/MCD-1567-1570 for the gear/economic-weapons wave)."
)

with open(LEDGER_PATH, "r", encoding="utf-8") as f:
    ledger = json.load(f)

existing_ids = {r["id"] for r in ledger["rules"]}

DRAFT_FILES = [
    "/tmp/claude-0/-home-user-Lords-of-Cian-Knowledge-Core/195feb94-2811-5ec6-b57d-6031cdaf1569/scratchpad/sealblack_protocol_draft.json",
    "/tmp/claude-0/-home-user-Lords-of-Cian-Knowledge-Core/195feb94-2811-5ec6-b57d-6031cdaf1569/scratchpad/new_villains_draft.json",
    "/tmp/claude-0/-home-user-Lords-of-Cian-Knowledge-Core/195feb94-2811-5ec6-b57d-6031cdaf1569/scratchpad/new_gear_draft.json",
]

NEW_RULES = []
for path in DRAFT_FILES:
    with open(path, "r", encoding="utf-8") as f:
        NEW_RULES.extend(json.load(f))

for r in NEW_RULES:
    r["status"] = "locked"
    r["source"] = SOURCE

new_ids = [r["id"] for r in NEW_RULES]
assert len(new_ids) == 47, f"expected 47 new rules, got {len(new_ids)}"
assert len(set(new_ids)) == len(new_ids), "duplicate IDs within the new-rules batch"
collisions = existing_ids & set(new_ids)
assert not collisions, f"ID collision with live ledger: {collisions}"

ledger["rules"].extend(NEW_RULES)

batch_note = (
    "Executes all three drafting-heavy items from Abad's 2026-09-27 four-item "
    "sync-check list (item 3, checking Book 1's noir structure, was research "
    "done directly rather than a draft), per his direction: \"you got it "
    "perfect I need you to work on all four items use as many agents as "
    "necessary so it comes out clean and efficient. work continuously, "
    "uninterrupted, until completion. this includes rigorous testing, "
    "committing, pushing.\" Three parallel background agents drafted: (1) the "
    "SEALBLACK Detachment Protocol -- four standing detachment classes tied "
    "to SBD-040's clearance tiers and SBD-047's disciplinary system "
    "(SBD-050/051), a records/redaction pipeline extending the Continuity "
    "Lock (SBD-052) -- plus five new anomaly-class entities (SBD-053-057: "
    "the Encore, the Verdigris, the Sinkmark, the Open File, the Arrears), "
    "four new named detachments (SBD-058-061: the Coldline, the Quiet Hand, "
    "the Lockstitch Detachment, the Foundling Detachment), and four new "
    "named facilities (SBD-062-065: the Reliquary at Khorvane, the Kesmara "
    "Continuity Vault, the Compliance Exchange, the Sealed Annex); (2) eleven "
    "new pre-Book-1 villains tiered below the Five Champions/Avatars/Triad "
    "Guardians, spread across five registers (Directorate/Trust command, Maw "
    "circuit, Weregildd/slaver economics, institutional corruption, an "
    "independent Ever-Haunt trafficker) with companion defeat rules "
    "attributing each to an already-established protagonist (Daba/1804 x2, "
    "Bane, the Crow King, the Sovereign Ghost of the Great Sea, the "
    "Blue-Collar Titan, Red Beard x2, Lauris, Ezio Valcari, and a Kanja-crew "
    "team-up fielding CULT-197's three-source Anti-Resonance countermeasure "
    "for the first time) -- Chronicle prose dramatizing these defeats is a "
    "distinct future wave, matching the established Kazi Tunji/Femi "
    "precedent of locking characters before writing their Chronicles; and "
    "(3) nine new gifts/weapons/economic tools for the Unchained Legion's "
    "Book 2-5 era, including four genuinely new 'economic weapon' concepts "
    "against the Scrip/Metabolic-Tether system (the Actuarial Key, the "
    "Verity Vein, Oracle-Salting, the Bartered Chain) alongside three new "
    "physical gifts and two new institutional tools. One real contradiction "
    "was caught before locking: the gear draft's original ARS-429 claimed "
    "to be Valeria Korth's 'first personal weapon ever,' directly "
    "contradicting CC-104's already-locked Weaver's Kit and Compass Needle "
    "-- corrected to a ranged-offensive extension of her existing kit. All "
    "47 new rules collision-checked clean, both by each drafting agent "
    "against the live ledger independently and by a final consolidated "
    "cross-agent check confirming zero overlap between the three drafts' "
    "own new proper nouns. Deliberately left untouched per each agent's own "
    "restraint: the PH2- homage-era track (no named villain added there, "
    "flagged as its own future call given how carefully that track's "
    "antagonists have stayed unnamed), Archon Meridian (left ungeared "
    "pending his political alignment), and every previously-reserved thread "
    "(Haku's fate, the Drowning Vault's 120, PH2-021's closed conspiracy). "
    "No real-world proper nouns, no child-safety issues, anywhere across "
    "the 47 rules."
)
ledger["batches_completed"].append(
    {
        "batch": 312,
        "date": str(date.today()),
        "source": "Three parallel background-agent drafts (original invention)",
        "rule_count": len(NEW_RULES),
        "note": batch_note,
    }
)

ledger["ledger_version"] = f"{round(float(ledger['ledger_version']) + 0.1, 1):.1f}"
ledger["last_updated"] = str(date.today())

with open(LEDGER_PATH, "w", encoding="utf-8") as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
      f"Batches: {len(ledger['batches_completed'])}.")
