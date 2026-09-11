#!/usr/bin/env python3
"""Batch 237: Iron Bastard Alias Chronicle wave 20 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Iron Bastard Alias Chronicle wave 20 (LVIII-LX), following Bane's individually-presented "
    "wave 20. \"The Pass Strung on Cable and Air\" (MCD-1047) is a detailed high-altitude "
    "full-Trinity combat showcase against a mountain-pass suspension crossing rigged with decoy "
    "load-bearing towers, introducing thin air as a new environmental attenuator on the "
    "resonance doctrine's reach (distinct from ice, desert wind, underwater, and storm "
    "interference, each already used and each solved differently). \"The Cohort He Couldn't "
    "Teach Alone\" (MCD-1048) is the doctrine's first formal multi-student cohort, a genuine "
    "limit of solo teaching resolved by assembling the doctrine's first three-person teaching "
    "lineage (Kanja plus the already-locked first and second students). \"What Efa Gol Asked Him "
    "to Listen To\" (MCD-1049) closes the wave on the doctrine's first wholly personal, "
    "non-operational application -- reading a dead pair-partner's keepsake rigger's pulley for "
    "already-locked crew member Efa Gol (CC-130), no enemy or structure with any military or "
    "civic stake involved. No new named characters were introduced in any of the three entries; "
    "all reused already-locked crew (Danne Sok, the first and second students, Efa Gol) and "
    "figures. Abad's approval: \"doorway for all the aliases that remain\" (approval of Bane's "
    "individually-presented wave 20 plus blanket authorization to continue the same wave for the "
    "remaining ten aliases)."
)

NEW_RULES = [
    {
        "id": "MCD-1047",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Pass Strung on Cable and Air\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-pass-strung-on-cable-and-air.md), The Iron Bastard "
            "Alias Chronicle LVIII, wave 20, first entry. A detailed full-Trinity combat showcase "
            "against a mountain-pass suspension crossing built on three cable-anchor towers, two "
            "of them deliberately slackened decoys; thin high-altitude air attenuates the "
            "resonance doctrine's reach for the first time, solved by closing to direct cable "
            "contact rather than reading from range. Doubled verification (established MCD-497) "
            "identifies the true load-bearing tower before Obsidian Malice's discharge collapses "
            "only that one, while Mafesto's Kinetic Transfer System absorbs answering fire and "
            "Onyx's Cadence Ruin clears the near tower's melee crew. The second student "
            "(established MCD-719) appears in a supporting capacity. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1048",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Cohort He Couldn't Teach Alone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-cohort-he-couldnt-teach-alone.md), The Iron "
            "Bastard Alias Chronicle LIX, wave 20. A settlement council sends twelve volunteers "
            "to be trained in diagnostic listening at once, rather than the single-student model "
            "used every prior time (MCD-499, MCD-719, MCD-967); Kanja concludes he cannot safely "
            "supervise twelve simultaneous live readings alone, and resolves it by assembling the "
            "doctrine's first three-person teaching lineage -- himself, the already-locked first "
            "student, and the already-locked second student -- each taking a group of four. Nine "
            "of twelve pass the cohort's final trial; the three who don't are sent home with an "
            "honest accounting rather than a lesser certificate, per the doctrine's standing "
            "honesty-over-polish principle. Distinct from the Trust-side institutional legacy at "
            "MCD-723, where the general's report became curriculum taught by others without Kanja "
            "present at all. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1049",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Efa Gol Asked Him to Listen To\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-efa-gol-asked-him-to-listen-to.md), The Iron "
            "Bastard Alias Chronicle LX, wave 20, closing the wave. The doctrine's first wholly "
            "personal, non-operational application: already-locked crew member Efa Gol (CC-130) "
            "asks Kanja to read a small rigger's pulley that belonged to her dead pair-partner, "
            "dock rigger Tam Sullen (CC-131, killed at the Black Trench), off duty and with no "
            "enemy, structure, or military/civic stake involved at all. The reading confirms the "
            "pulley carries no hidden failure, only the honest wear of years of real use, and Gol "
            "keeps it without further explanation of why she needed to know. Distinct from the "
            "anonymous civilian smith's parallel intuition (MCD-722) and the dam's public "
            "civil-aid register (MCD-898). No new named characters; Tam Sullen's pulley is a new, "
            "minor keepsake object with no standing mechanical significance and no collision "
            "against any named item in the ledger. Closes the Iron Bastard's twentieth "
            "three-Chronicle wave (with 'The Pass Strung on Cable and Air,' MCD-1047, and 'The "
            "Cohort He Couldn't Teach Alone,' MCD-1048)."
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
            "batch": 237,
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
