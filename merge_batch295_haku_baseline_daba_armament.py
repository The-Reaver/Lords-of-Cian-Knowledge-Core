#!/usr/bin/env python3
"""Batch 295: Kanja's inherited Haku-lineage tactical mastery as the baseline
Daba's guerrilla teaching enhances (amends MCD-1568 in place), plus the
armament payoff explaining 1804's disproportionate lethality (new MCD-1570)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-17, no source document. Extends the "
    "1804/Daba foundation locked in Batch 294, per Abad's follow-up direction."
)

BATCH_NOTE = (
    "Abad's follow-up (dictated, lightly garbled): Kanja already had 'free training' "
    "because Haku battled 'The Deposed King' Anu Un Ra and 'implemented Mastery of "
    "tactical Warfare,' which Daba's teaching 'enhances,' in exchange for 'the "
    "knowledge of Fortune greater armor and weaponry' that makes 1804 lethal and "
    "formidable. Resolved without a clarifying round: 'free training' maps directly "
    "to the already-locked MCD-311 (Rexmar tradition is biological/instinctive, not "
    "taught -- 'an eighteen-year-old Kanja with no formal military training'); Haku "
    "deposing Anu Un Ra ~5,000 years ago is already locked at WC-005/WC-020/CC-056/"
    "MCD-305, and 'The Deposed King' is already Anu Un Ra's own locked historical "
    "title, so no collision. 'Knowledge of Fortune' read as a dictation slip for "
    "'forging,' which MCD-1568 already has Kanja teaching Daba -- this closes the "
    "loop by giving that exchange its stated payoff. MCD-1568 amended in place to add "
    "the Haku-baseline clause (Daba enhances rather than originates Kanja's tactical "
    "sense). MCD-1570 locks the armament payoff: Daba's forging knowledge from Kanja "
    "is the concrete mechanical source of 1804's disproportionate lethality already "
    "asserted at MCD-1567, closing a gap that rule left unexplained. Zero new proper "
    "nouns, zero collisions. Abad's approval: \"lock it.\""
)

MCD_1568_AMENDED_STATEMENT = (
    "Kanja does not arrive to this mentorship a blank slate in tactical warfare: the "
    "same Rexmar-Haku convergence that makes him a Rexmar-tradition fighter (MCD-311) "
    "already carries an inherited, instinctive mastery of tactical warfare -- 'free' "
    "in the sense that it was never personally taught, only expressed, the biological "
    "legacy of Haku's own campaigns against Anu Un Ra roughly 5,000 years ago (WC-005, "
    "WC-020, CC-056, MCD-305). Some years before Kanja's Rebellion formally begins, "
    "Kanja and Daba enter a deliberate, mutual mentorship during Kanja's otherwise-"
    "unrecorded formative years: Daba does not originate Kanja's tactical thinking but "
    "enhances and refines it -- sharpening inherited instinct into deliberate "
    "small-unit doctrine, terrain-as-weapon thinking, and the discipline of making "
    "concentrated force irrelevant -- while Kanja teaches Daba forging, drawing on his "
    "own Rexmar tradition (MCD-294 through MCD-312). Daba becomes Kanja's conscious "
    "apprentice in forging: aware of exactly what he is learning and why, not a naive "
    "student absorbing technique without context. The exchange is the shared root of "
    "two doctrines that later look identical in practice: Daba's own guerrilla tactics "
    "and Kanja's already-locked terrain-physics doctrine at the Dredge-Line Ambush and "
    "Iron Shallows (MCD-231/233) -- density is not power if the terrain neutralizes "
    "it, a lesson 1804 taught Daba first and Daba taught Kanja second."
)

NEW_RULES = [
    {
        "id": "MCD-1570",
        "category": "World Mechanics",
        "statement": (
            "The forging knowledge Daba receives from Kanja (MCD-1568) is the "
            "concrete source of 1804's disproportionate lethality already locked at "
            "MCD-1567: applying Rexmar forging principles at guerrilla-network scale, "
            "Daba re-equips 1804's dispersed cells with armor and weaponry "
            "considerably beyond what a network of its size would otherwise field -- "
            "not mass-produced from a central armory, which would itself become the "
            "single point of failure MCD-1567 already rules out, but distributed, "
            "cell-by-cell craftsmanship Daba personally teaches onward through the "
            "network. This is the specific mechanical answer to how a force built "
            "deliberately small stays formidable rather than merely elusive."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    amended = False
    for r in ledger["rules"]:
        if r["id"] == "MCD-1568":
            assert not amended, "MCD-1568 found twice"
            r["statement"] = MCD_1568_AMENDED_STATEMENT
            amended = True
    assert amended, "MCD-1568 not found to amend"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 295,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs found post-write!"

    print(
        f"OK. Total rules: {len(ledger['rules'])}. "
        f"Ledger version: {ledger['ledger_version']}. "
        f"Batches: {len(ledger['batches_completed'])}."
    )


if __name__ == "__main__":
    main()
