#!/usr/bin/env python3
"""Batch 301: Severin Ebonrath, First Patriarch of the Obsidian Prefecture's Senate of Twelve (POL-100)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-18, no source document. Drafted in response to a "
    "triage pass over Shelton Dexton's SBD-informant source material (THIS_IS_SUPERIOR_MANDATED_BY_"
    "IMPERATOR_SHELTON_DEXTON_1.docx and related uploads), which raised named-ruler coverage for the "
    "four Shattered Kingdoms nations as an open item. Cross-check against the live ledger found "
    "Aethel-Gard (CC-127, Thane-Gorm), the Hollow Shogunate (POL-070, Vile-Sire and Hollow-Dam), and "
    "the Astral Archipelago (POL-095/096, the three Council of Crossroads seats) already had named "
    "leadership; only the Obsidian Prefecture, already locked as ruled by a Senate of twelve "
    "Patriarchs (POL-040), lacked a named figure. The source material itself supplied no ruler name "
    "for the Prefecture, only unresolved tone/flavor questions -- this rule is invented fresh, not "
    "extracted. Collision-checked before drafting: 'Severin' and 'Ebonrath' both return zero hits "
    "against the full live ledger; the already-used antagonist-register surnames Cassius, Draconis, "
    "Blackthorne, and Aurelius were deliberately avoided."
)

NEW_RULES = [
    {
        "id": "POL-100",
        "category": "political-figure",
        "statement": (
            "Severin Ebonrath is First Patriarch of the Obsidian Prefecture's Senate of Twelve "
            "(extends POL-040's already-locked oligarchic structure -- he is first among equals by "
            "seniority and political skill, not a monarch). He is the public face and private "
            "architect of the already-locked Patient Caucus position (CULT-067): publicly he argues "
            "standard moderate restraint toward the Sovereign Trust; privately, his real position is "
            "about timing -- that the conflict which actually matters is the one at the Resumption, "
            "and resources spent on a premature war now are resources unavailable when it counts. "
            "This patience, sustained across decades, is what has made him effectively unremovable "
            "from the Senate's center of gravity, not weakness or indecision. Extends the already-"
            "locked MCD-328 (the Prefecture eventually commits 200,000 legionaries to the alliance's "
            "western front, per 'the already-locked Prefecture/Vestige manipulation material') and "
            "MCD-282 (Lady Vestige's power is institutional perception-warfare -- engineered optics, "
            "forged documents, manipulated communications, never mysticism): Severin's own carefully-"
            "reasoned patience becomes the exact lever Vestige uses against him -- at the relevant "
            "moment his Senate commits those legions believing it is their own patient calculus "
            "playing out, when it is actually her manipulation steering the timing. His defeat, when "
            "it comes, is entirely political and epistemic rather than a direct confrontation, "
            "consistent with the Prefecture's established decaying-marble/iron-fisted-bureaucracy "
            "register rather than a combat-antagonist one."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "lock it."'


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
            "batch": 301,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-18, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "Severin Ebonrath (POL-100) locked as First Patriarch of the Obsidian Prefecture's "
                "Senate of Twelve, the last of the four Shattered Kingdoms nations lacking a named "
                "ruler -- Aethel-Gard, the Hollow Shogunate, and the Astral Archipelago already had "
                "one each. Ties into the already-locked Patient Caucus position (CULT-067) and the "
                "Prefecture/Vestige legionary-commitment thread (MCD-328/MCD-282), giving him a "
                "coherent political throughline and a tragic hook rather than inventing him in "
                "isolation. " + BATCH_NOTE
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
