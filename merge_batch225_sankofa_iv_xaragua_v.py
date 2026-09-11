#!/usr/bin/env python3
"""Batch 225: Lock Sankofa Chronicle IV and Xaragua Chronicle V (MCD-1023, MCD-1024),
advancing the two deliberately reserved threads (PH2-021 conspiracy, PH2-061/062 long-arc)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = 'Abad: "lock it up." Advances the two deliberately reserved threads flagged across many prior batches: Sankofa\'s forged-letter conspiracy (PH2-021), deepened without resolving it, and the Kanja/Arturo Salvatierra Duho long-arc (PH2-061/062), advanced a meaningful step short of full payoff, per Abad\'s explicit choices on scope for each thread this round.'

NEW_RULES = [
    {
        "id": "MCD-1023",
        "category": "territory-chronicle",
        "statement": (
            "Sankofa Chronicle IV, \"What the Clinic Wasn't Told\" (full narrative text at "
            f"{CHRON_DIR}sankofa-chronicle-iv-what-the-clinic-wasnt-told.md), the fourth "
            "Sankofa territory Chronicle and the second to touch the forged-letter "
            "conspiracy from Chronicle II (MCD-360). Escalates the conspiracy from a single "
            "private letter aimed at one man's trust to a public pamphlet campaign aimed at "
            "an entire city's trust in the community health clinic Baale opened in Chronicle "
            "III (MCD-518), turning the institution he built to sit outside his own "
            "reputation into a new attack surface. Baale responds with transparency (opening "
            "the clinic's books publicly for three days) rather than violence or denial. A "
            "courier caught delivering a further wave of pamphlets is paid through a "
            "three-layer cutout chain and knows nothing of who is behind it, deepening "
            "PH2-021's 'conspiracy that never shows its face' framing without resolving it. "
            "Kra and Kojo (both already locked) reused; no new named characters. Kanja "
            "present throughout as the unnamed guest, without command, credit, or "
            "resolution authorship. The threat's author and motive remain deliberately "
            "unidentified at the close."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1024",
        "category": "territory-chronicle",
        "statement": (
            "Xaragua Chronicle V, \"The Night He Was Let Into the Room\" (full narrative "
            f"text at {CHRON_DIR}xaragua-chronicle-v-the-night-he-was-let-into-the-room.md), "
            "the fifth Xaragua Chronicle, set after Xaragua Chronicle IV (MCD-362) in the "
            "'modern' Arturo era. Advances the flagged Kanja/Arturo Salvatierra Duho "
            "(PH2-061) long-arc a meaningful step, deliberately short of its full payoff. "
            "Introduces a previously-undramatized standing private annual remembrance Arturo "
            "and Yaisa (PH2-062) hold for his lost dock-boy cohort -- Nzila, Tunde, and Bendu "
            "(named in MCD-361) -- with Kanja invited into it for the first time. Arturo "
            "states directly that this does not grant unguarded-banter parity with Yaisa, "
            "whose unique standing depends on remembering who he was before the reputation, "
            "not on earned trust; Kanja reciprocates with an unnamed personal disclosure of "
            "a past loss of his own, without naming himself or anyone else, maintaining the "
            "established unnamed-guest convention. Closes on a warmer, almost-banter note "
            "that deliberately stops short of the long-arc's flagged full payoff, leaving it "
            "open for a future entry. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collisions with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 225,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks Sankofa Chronicle IV (MCD-1023) and Xaragua Chronicle V (MCD-1024), "
                "advancing the two deliberately reserved threads (Sankofa's forged-letter "
                "conspiracy, PH2-021; the Kanja/Arturo long-arc, PH2-061/062). " + BATCH_NOTE
            ),
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate IDs after merge"
    print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
          f"Batches: {len(ledger['batches_completed'])}.")


if __name__ == "__main__":
    main()
