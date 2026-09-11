#!/usr/bin/env python3
"""Batch 233: Blue-Collar Titan Alias Chronicle wave 20 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Blue-Collar Titan's twentieth Alias Chronicle wave (three entries), continuing the "
    "established discipline of never repeating a prior wave's story shape. \"What the Smoke Was "
    "Hiding\" (MCD-1035) is the alias's first fire/arson hazard entry (distinct from every prior "
    "water- and collapse-based crisis) and a detailed full-Trinity combat/rescue showcase per the "
    "standing craft note -- Mafesto redirecting displaced air rather than force, Obsidian Malice used "
    "for precision venting rather than as a weapon or quarrying tool, Onyx of Oblivion clearing the "
    "posted guards. \"The Fitting He Carried Forward\" (MCD-1036) is a generational-legacy payoff "
    "directly continuing \"The Boy Who Wanted the Blade Instead\" (MCD-653, wave 6): the now-grown, "
    "still-unnamed orphan returns as a journeyman independently teaching the same lesson to a new "
    "orphan, with Kanja witnessing rather than delivering the lesson this time. \"What the Years "
    "Hadn't Moved\" (MCD-1037) is a retrospective legacy-check bookending the alias's first wave, "
    "with Kanja unprompted and alone revisiting the original Sewer War of Killane tunnels roughly two "
    "decades later to find his original work still holding. No new named characters were introduced "
    "across any of the three entries; a one-scene dredge-crew foreman in the third entry was "
    "collision-checked against the full ledger and left deliberately unnamed. Abad's approval: "
    "\"doorway for all the aliases that remain\" (approval of Bane's individually-presented wave 20 "
    "plus blanket authorization to continue the same wave for the remaining ten aliases)."
)

NEW_RULES = [
    {
        "id": "MCD-1035",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Smoke Was Hiding\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-smoke-was-hiding.md), the Blue-Collar Titan Alias "
            "Chronicle LVIII, wave 20. The alias's first fire/arson hazard entry: Directorate agents "
            "deliberately set a pitch-oil fire timed to shift change to cut off retreat for "
            "twenty-six workers deeper into the tunnel network, rather than collapsing it outright. A "
            "detailed full-Trinity combat/rescue showcase distinct from every prior water-based "
            "(MCD-440, MCD-486) and collapse-based (MCD-485, MCD-537, MCD-656) crisis: Mafesto's "
            "kinetic transfer redirecting displaced air backward along an old shored shaft rather than "
            "generating force, Obsidian Malice discharged as a single precision vent-strike to draw "
            "the fire toward the surface instead of the workers, and Onyx of Oblivion's Cadence Ruin "
            "and Veil Piercer clearing two guards posted to ensure no one survived the smoke. All "
            "twenty-six workers survive. No new named characters -- Danne Sok reused. Opens wave 20."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1036",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fitting He Carried Forward\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fitting-he-carried-forward.md), the Blue-Collar Titan "
            "Alias Chronicle LIX, wave 20. A generational-legacy payoff directly continuing \"The Boy "
            "Who Wanted the Blade Instead\" (MCD-653, wave 6): eleven years later, the same orphaned "
            "boy -- now a journeyman -- arrives with a supply caravan, having independently begun "
            "teaching Kanja's own redirect-to-trade lesson (the same pipe fitting, the same 'boring "
            "work that matters' phrase) to a newly orphaned boy of his own, without prompting or "
            "instruction from Kanja. Distinct from every prior mentorship register for this alias in "
            "that Kanja here witnesses a lesson's third-hand propagation rather than teaching or being "
            "taught directly. No new named characters -- both the original boy (now a journeyman) and "
            "the new orphan remain deliberately unnamed, consistent with MCD-653's own precedent. "
            "Second entry in wave 20."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1037",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Years Hadn't Moved\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-years-hadnt-moved.md), the Blue-Collar Titan "
            "Alias Chronicle LX, wave 20, closing the wave. A retrospective legacy-check entry: "
            "roughly two decades after the Sewer War of Killane (MCD-234), Kanja makes an unprompted, "
            "solitary return to the original western gallery he shored during the siege and finds it "
            "still holding, untouched by the structural failures that have required later crews to "
            "repair the surrounding network twice over. An unnamed one-scene dredge-crew foreman, "
            "collision-checked clean against the full ledger, confirms the gallery's reputation among "
            "the current generation of diggers without knowing who built it. Deliberately bookends "
            "\"The Titan's Own Hands\" (MCD-376, wave 1) and \"What Broke and What He Fixed\" "
            "(MCD-408, wave 2), both set during the original siege. No new named characters. Closes "
            "wave 20 (with MCD-1035 and MCD-1036) and the twentieth overall Blue-Collar Titan wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 3, f"expected 3 new rules, got {len(NEW_RULES)}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 233,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-11, no source document",
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
