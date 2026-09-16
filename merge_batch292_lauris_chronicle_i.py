#!/usr/bin/env python3
"""Batch 292: Lauris Chronicle I, "The Shape Taught Twice" -- her first entry
under the Character Chronicle Gameplan."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-16, no source document. First entry in "
    "Lauris Letitia's own Chronicle series under the Character Chronicle Gameplan "
    "(docs/lords-of-cian/character-chronicle-gameplan.md)."
)

BATCH_NOTE = (
    "First Chronicle in Lauris Letitia's own series, the Character Chronicle Gameplan's "
    "Tier 1 track. Resolves the gameplan's open narrator sub-question: narrated by Fermand "
    "Aurelias, per the already-locked CC-034 (\"Fermand narrates all Ezio and Lauris POV "
    "chapters in a Baroque/Zafón-Noir voice\") and VB-024's voice spec, distinct from both "
    "Onyx's Kanja narration and the close-third register used for the homage-era territory "
    "Chronicles -- Lauris is core Lords of Cian crew, not a stranger Kanja meets. Dramatizes "
    "two of her least-shown traits for the first time: the Density Saturation Inversion "
    "(ARS-357-374, fuller saturation makes her progressively less detectable) and her "
    "defining combat-joy (CC-134). Picks up the freshest live hook in her canon: Operation "
    "12's Settlement K-447 (MCD-1536, Batch 291) left unresolved who arranged the bodies or "
    "taught the resonance-keying technique. This entry deliberately deepens rather than "
    "resolves that mystery -- a second, unrelated circle was taught a degraded fragment of "
    "the same method by an unnamed itinerant instructor decades ago, confirming the original "
    "actor is still active and still teaching, without identifying them. No new named "
    "characters. Full text at "
    "docs/lords-of-cian/chronicles/lauris-chronicle-i-the-shape-taught-twice.md. Abad's "
    "approval: \"lock it.\""
)

NEW_RULES = [
    {
        "id": "MCD-1561",
        "category": "lauris-character-chronicle",
        "statement": (
            "Lauris Chronicle I, \"The Shape Taught Twice\" (full narrative text at "
            "docs/lords-of-cian/chronicles/lauris-chronicle-i-the-shape-taught-twice.md), "
            "the first entry in Lauris Letitia's own Chronicle series under the Character "
            "Chronicle Gameplan, narrated by Fermand Aurelias per CC-034. A frontier holding "
            "near the Korren Highlands is found with an unfinished chalk perimeter matching "
            "the resonance-keying geometry from Operation 12's Settlement K-447 (MCD-1536); "
            "Lauris arrives before the pattern completes and stops it. A crude density-ward "
            "built by the circle fails against her mid-engagement, demonstrating the Density "
            "Saturation Inversion (ARS-357-374) directly for the first time: her signature "
            "grows harder rather than easier to detect as her density rises past a threshold, "
            "the inverse of every other density combatant on Cian. The engagement also puts "
            "her defining combat-joy (CC-134) on the page as an unqualified, competent "
            "pleasure in her own capability rather than grim duty. The circle's leader "
            "reveals he was taught the technique decades ago by an unnamed itinerant "
            "instructor calling it 'insurance' -- confirming Settlement K-447's original "
            "actor is still alive and still teaching the method to unrelated circles, without "
            "identifying who they are. Lauris spares all six, extracting only the requirement "
            "that the settlement disclose the technique's real cost rather than keep it as a "
            "secret. Closes on her own admission that this operational debt -- unlike her "
            "others -- may never close on a schedule she controls. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 1, f"expected 1 new rule, got {len(NEW_RULES)}"
    new_ids = [r["id"] for r in NEW_RULES]
    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 292,
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
