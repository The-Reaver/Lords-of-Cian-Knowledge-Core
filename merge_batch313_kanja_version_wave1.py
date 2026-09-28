#!/usr/bin/env python3
"""Batch 313: launches the new "Kanja version" Chronicle track's first wave
(Chronicles I-III), per Abad's explicit gate clearance (2026-09-28) on
docs/lords-of-cian/character-profiles/kanja-haku-rexmar.md -- Rules
Walkthrough, Psychological Profile, and Game Plan all approved before any
prose was drafted, per the Character Chronicle Launch Protocol.

Distinct from the existing 11-alias Alias Chronicle track: this track uses
Onyx of Oblivion's progressive narrator-handoff mechanic (VB-020/021/026),
scoped to the Rebellion only (ages 18-30). Chronicle I (age 18) opens with
Onyx's presence at near-zero; Chronicle II (pre-18, written second but set
chronologically first) has zero Onyx presence, being set before his age-17
bonding; Chronicle III (age 27) shows Onyx's second real appearance,
dramatizing Renfel Auberon's defeat (MCD-1865) -- the one Batch-312 villain
explicitly assigned to this track rather than any Alias Chronicle wave, per
the Game Plan's own villain-defeat arbitration.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = (
    "Original invention, chat-drafted 2026-09-28, extending already-locked "
    "material throughout (MCD-231/1568/1570 for Chronicles I-II; MCD-1865/"
    "CULT-197/198/WC-019 for Chronicle III)."
)

with open(LEDGER_PATH, "r", encoding="utf-8") as f:
    ledger = json.load(f)

existing_ids = {r["id"] for r in ledger["rules"]}

NEW_RULES = [
    {
        "id": "MCD-1866",
        "category": "kanja-character-chronicle",
        "statement": (
            "Kanja Chronicle I, 'The Fourteen Percent That Was Hers' (full text at "
            "docs/lords-of-cian/chronicles/kanja-chronicle-i-the-fourteen-percent-that-was-hers.md). "
            "The opening entry of the new Kanja-version Chronicle track -- Kanja himself as "
            "protagonist, narrated per VB-020/021/026's progressive narrator-handoff mechanic, "
            "distinct from the existing Alias Chronicle track. Age 18, four days after the "
            "Scrip-Forge Raid (MCD-231), three weeks before the Dredge-Line Ambush -- a "
            "deliberately small, non-combat vignette: a widow, Pava Rill, and her son Emrik "
            "bring a cracked kettle to Kanja's forge; he refuses to simply give her the money "
            "her debased wages cost her, instead trading two saved notes for the kettle's copper "
            "scrap at its real value, extending his already-locked evidence-over-charity, "
            "dignity-through-earned-trade ethos from politics into an ordinary household "
            "transaction. Onyx of Oblivion appears only in a near-silent, unlabeled closing "
            "coda -- its first appearance in this track, deliberately the shortest and least "
            "articulate of the whole wave, establishing the true zero point the later entries "
            "grow from."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1867",
        "category": "kanja-character-chronicle",
        "statement": (
            "Kanja Chronicle II, 'The Lesson He Carried Alone' (full text at "
            "docs/lords-of-cian/chronicles/kanja-chronicle-ii-the-lesson-he-carried-alone.md). "
            "The second entry of the Kanja-version track, written second but set "
            "chronologically first -- before Chronicle I, before the Rebellion, before Kanja's "
            "bonding with Onyx of Oblivion at seventeen (ARS-020), matching the project's "
            "established write-order-vs-in-universe-order precedent. Dramatizes the mutual "
            "mentorship between Kanja and Daba (MCD-1568/1570) from Kanja's own side for the "
            "first time: a failed night-training exercise on a drainage cut, where Kanja "
            "fortifies every mapped approach but is beaten through a disused footbridge nobody "
            "watches, teaching him to distrust settled ground -- the direct, undramatized root "
            "of the terrain-as-weapon logic he later applies at the Dredge-Line Ambush "
            "(MCD-231). Deliberately avoids restaging any specific dated scene from Daba's own "
            "50-Chronicle launch wave (Batch 296). Zero Onyx narrator presence -- no blade "
            "exists yet in Kanja's life at this point -- a clean structural contrast against "
            "Chronicle I's minimal-but-present coda."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1868",
        "category": "kanja-character-chronicle",
        "statement": (
            "Kanja Chronicle III, 'What the Dark Could Not Keep' (full text at "
            "docs/lords-of-cian/chronicles/kanja-chronicle-iii-what-the-dark-could-not-keep.md). "
            "The third entry of the Kanja-version track, age 27 (within this track's "
            "Rebellion-only window, before the Trinity's age-30 surrender, MCD-246). Dramatizes "
            "Renfel Auberon's defeat (CC-157/MCD-1865) -- the one Batch-312 villain explicitly "
            "assigned to this track rather than any Alias Chronicle wave, per the Game Plan's "
            "villain-defeat arbitration, since it requires Onyx as an active pre-age-30 combat "
            "participant. Kanja, Sephtis, and Ironbane corner Auberon in an unregistered "
            "warehouse holding six illegally captured Ever-Haunt entities and field CULT-197's "
            "three-source Anti-Resonance countermeasure (Onyx's Cadence Ruin, Sephtis's "
            "Chrono-Anchor bells, Ironbane's King's Roar) together on the page for the first "
            "time, forcing every entity to collapse to its lowest tier or disperse rather than "
            "be harmed outright. Auberon is captured alive, already partially Green-Mark-"
            "contaminated (CULT-198) from years of unsafe proximity to his own stock, and handed "
            "to the older custodial apparatus that tracks anomalies of this kind rather than to "
            "ordinary Trust law enforcement. Onyx's coda has grown to its second real "
            "appearance in this track -- longer and more assertive than Chronicle I's, still "
            "unlabeled, matching the Game Plan's specified growth curve."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

new_ids = [r["id"] for r in NEW_RULES]
assert len(new_ids) == 3
assert len(set(new_ids)) == len(new_ids), "duplicate IDs within the new-rules batch"
collisions = existing_ids & set(new_ids)
assert not collisions, f"ID collision with live ledger: {collisions}"

ledger["rules"].extend(NEW_RULES)

batch_note = (
    "Launches the new 'Kanja version' Chronicle track's first wave (Chronicles I-III), "
    "the gate having cleared on docs/lords-of-cian/character-profiles/kanja-haku-rexmar.md "
    "across three separate sessions of discussion: the Rules Walkthrough (background agent, "
    "matching the Ozmund-profile depth standard), the Psychological Profile (Abad confirmed "
    "the Scrip-Note core wound for this track's Rebellion-only window, then added the larger, "
    "reserved, post-window wound -- his father's murder at the Fulfillment Ceremony as 'the "
    "most devastating blow, but it awakens the urge to destroy his enemies,' explicitly walled "
    "off from this track and recorded for a future Book-1-era profile -- then approved the "
    "rest of the proposed profile with 'the rest lands, keep going'), and the Game Plan (Onyx "
    "as progressive narrator per VB-026, single sequence, Rebellion-only ages 18-30, and the "
    "villain-defeat track arbitration assigning Renfel Auberon's defeat to this track since it "
    "requires Onyx as an active pre-age-30 participant). Abad then picked all three offered "
    "Chronicle I candidates as the opening run, in order, under: 'continuously, uninterrupted, "
    "until completion. this includes rigorous testing, committing, pushing to main origin.' "
    "This track is deliberately distinct from the existing 11-alias Alias Chronicle track (990+ "
    "entries), which stays untouched as 'the regular accounting' -- flat neutral third-person "
    "throughout, no Onyx narrator presence at any era. The Kanja-version track is where Onyx's "
    "proper progressive-handoff voice, already demonstrated in the 8 manuscript Chronicles, "
    "gets built going forward. Zero new proper-noun collisions checked before drafting (Pava "
    "Rill, Emrik Rill); Chronicle III's Ever-Haunt sourcing was explicitly checked against "
    "WC-019/MCD-1621's Great-Breach timing to avoid a real chronology contradiction before "
    "committing to the scene."
)
ledger["batches_completed"].append(
    {
        "batch": 313,
        "date": str(date.today()),
        "source": "Original invention (new Chronicle track launch)",
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
