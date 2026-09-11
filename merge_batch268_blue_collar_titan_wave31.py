#!/usr/bin/env python3
"""Batch 268: Blue-Collar Titan Alias Chronicle wave 31 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "The Blue-Collar Titan's thirty-first Alias Chronicle wave, drafted under Abad's blanket "
    "authorization to continue a 31st wave for all eleven aliases. Opens with the alias's first "
    "combat showcase against a mechanized Directorate siege engine rather than soldiers, a trap, "
    "or an environmental hazard, extending Mafesto's Kinetic Transfer System into moving-target "
    "vibration tracking and Obsidian Malice into precision-disabling a drive mechanism. The second "
    "entry introduces the alias's first institutional-legitimacy-poaching register, a rival "
    "post-war collective borrowing the reputation the tradesmen's association's own charter "
    "deliberately refuses to name, resolved through refusal rather than force. The wave closes with "
    "a reconciliation payoff to the already-locked duel in \"The Engineer Who Fought Like One\" "
    "(MCD-670), bringing that same unnamed Trust combat engineer back years later as a collaborator. "
    "No new named characters across any of the three entries; the Founders' Guild and its unnamed "
    "founder collision-checked clean. Abad's approval: \"let's do a 31st alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1400",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Machine That Dug Toward Them\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-machine-that-dug-toward-them.md), Blue-Collar Titan "
            "Alias Chronicle XCI, wave 31, opening the wave. The alias's first combat showcase "
            "against a mechanized Directorate boring engine driven as a weapon in its own right "
            "rather than a static trap or a triggered hazard -- Mafesto's Kinetic Transfer System "
            "tracks the machine's vibration signature to intercept it before it reaches a civilian "
            "shelter gallery, and Obsidian Malice is discharged as a precision strike on the drive "
            "shaft rather than a shield-breaking blow, disabling the engine intact instead of "
            "shattering its housing into shrapnel; Onyx of Oblivion's Cadence Ruin and Veil Piercer "
            "handle its four-man operating crew. Reuses already-locked crew member Danne Sok. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1401",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Collective That Borrowed His Name\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-collective-that-borrowed-his-name.md), Blue-Collar "
            "Titan Alias Chronicle XCII, wave 31. The alias's first institutional-legitimacy-"
            "poaching entry: a rival post-war trade collective, the Founders' Guild, falsely implies "
            "Kanja's personal endorsement to draw membership away from the tradesmen's association "
            "he deliberately founded without his own name attached (MCD-662, reaffirmed MCD-1200). "
            "Rather than exposing or shutting the collective down, Kanja refuses in front of its own "
            "recruits to confirm or deny the implied endorsement, reaffirming that neither is his to "
            "give; the false claim is dropped within a season and the collective's membership holds "
            "steady on honestly earned reputation alone. Reuses already-locked crew member Garren "
            "Hask (CC-115). The Founders' Guild and its unnamed founder are collision-checked clean. "
            "No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1402",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Man He Let Walk Away\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-man-he-let-walk-away.md), Blue-Collar Titan Alias "
            "Chronicle XCIII, wave 31, closing the wave. A reconciliation payoff to \"The Engineer "
            "Who Fought Like One\" (MCD-670), the alias's first genuine skill-versus-skill duel: the "
            "same unnamed Trust combat engineer, spared then on the strength of mutual professional "
            "recognition, returns years later as a civilian collaborator rather than an adversary, "
            "asking for the crew's actual rebuilding expertise rather than the alias's reputation, "
            "and receives it on the same standards as any other request, no favor granted for old "
            "respect. Reuses already-locked crew member Danne Sok and the unnamed engineer from "
            "MCD-670. No new named characters. Closes wave 31 (with MCD-1400 and MCD-1401)."
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
            "batch": 268,
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
