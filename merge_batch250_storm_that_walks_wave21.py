#!/usr/bin/env python3
"""Batch 250: Storm That Walks Alias Chronicle wave 21 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Storm That Walks Alias Chronicle wave 21 (LXI-LXIII), three new entries continuing directly from "
    "wave 20's close (MCD-1053-1055): the successor's formal retirement and full handoff to the "
    "third-generation student. 'The Name She Had to Earn Twice' (MCD-1086) tests the student's own "
    "institutional legitimacy for the first time via a skeptical Trust liaison, with the retired "
    "successor deliberately declining to vouch for her, extending MCD-1055's closing lesson directly. "
    "'The Truce They Wouldn't Honor' (MCD-1087) is a detailed full-Trinity combat showcase defending the "
    "rival-tradition truce (MCD-985) from a holdout faction -- the first Storm That Walks entry protecting "
    "an agreement between two fleets rather than one fleet, vessel, rescue, or institution. 'What the Trust "
    "Wrote Into the Manual' (MCD-1088) closes the wave with the doctrine's first formal codification into "
    "written Sovereign Trust naval regulation, crediting the school rather than any one name. No new named "
    "characters introduced across any of the three entries; all reuse already-locked figures (the retired "
    "successor, the third-generation student, the rival squadron's commander) left unnamed per the "
    "sub-series' established pattern. Collision-checked against the full live ledger before drafting -- "
    "zero new proper nouns. Placed correctly relative to Sephtis's established death (MCD-982) and the "
    "successor's established retirement (MCD-1055): Sephtis is not re-referenced as living, and the "
    "successor's retirement is treated as permanent and unreversed throughout. Abad's approval: \"another "
    "alias wave of all aliases\"."
)

NEW_RULES = [
    {
        "id": "MCD-1086",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Name She Had to Earn Twice\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-name-she-had-to-earn-twice.md), Storm That Walks Alias "
            "Chronicle LXI, wave 21, first entry in the wave. A newly posted Sovereign Trust naval liaison "
            "unfamiliar with the school's succession refuses to act on the third-generation student's storm "
            "call over her lack of personal standing; the retired successor (MCD-1055), present throughout, "
            "deliberately declines to vouch for her, and the student instead proves her authority by handing "
            "over her own three-year forecasting ledger -- successes and honest misses alike -- rather than "
            "inheriting the successor's reputation. The liaison moves his fleet on her call alone; the storm "
            "arrives exactly as predicted. The first Storm That Walks entry to test the third-generation "
            "student's institutional legitimacy specifically, distinct from the doctrine's general "
            "credibility (already tested at MCD-564) or her own forecasting skill (already proven at "
            "MCD-1054), and a direct dramatization of MCD-1055's closing lesson about the successor "
            "'teaching herself when to stop being the reason people believe it.' Kanja present throughout, "
            "granted no vouching or resolution authorship. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1087",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Truce They Wouldn't Honor\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-truce-they-wouldnt-honor.md), Storm That Walks Alias "
            "Chronicle LXII, wave 21. A detailed full-Trinity combat showcase: during a joint weather-"
            "calibration drill between Kanja's fleet and the rival squadron under the mutual-berth truce "
            "established at MCD-985, four holdout ships that never accepted the truce break formation and "
            "attack in the dark, meaning to frame it as proof the truce was a trap. Mafesto's Kinetic "
            "Transfer System redirects the first ramming run into open water rather than toward the rival "
            "flagship it targeted, deliberately avoiding any appearance of Kanja's fleet retaliating against "
            "the rival squadron; Onyx's Cadence Ruin disables the second holdout's rigging in the storm's own "
            "gust-lulls with zero crew casualties; Whisper of Shadows and Soulbound Edge board and disable "
            "the third with three precise, bloodless line cuts; Obsidian Malice throws a wall of displaced "
            "water ahead of the fourth rather than striking its hull. All four holdouts disabled, no deaths "
            "on either side; the rival squadron's own commander takes the holdouts into her own custody in "
            "full view of both fleets. The first Storm That Walks entry where the Trinity defends an "
            "agreement between two fleets rather than a single fleet, vessel, rescue, or institution, with "
            "every strike deliberately calibrated to protect the attacking holdouts' own crews as carefully "
            "as the rival squadron's ships. No new named characters -- the four holdout captains and the "
            "rival commander (already established unnamed at MCD-985) remain unnamed."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1088",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Trust Wrote Into the Manual\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-trust-wrote-into-the-manual.md), Storm That Walks Alias "
            "Chronicle LXIII, wave 21, closing the wave. The Sovereign Trust formally codifies the storm-"
            "timing doctrine into written naval regulation -- a mandatory 'storm-interval verification' "
            "protocol requiring any officer disputing a certified reading to request the reader's full "
            "record before overriding it -- crediting the school as an institution rather than Sephtis, the "
            "successor, the third-generation student, or Kanja by any name. The retired successor frames it "
            "to the student as the doctrine outliving personal reputation entirely: 'we were only ever the "
            "part that had to be believed until the part that didn't need believing caught up.' Kanja "
            "privately reflects that the doctrine's growing anonymity mirrors his own aliases' names "
            "outlasting or displacing his own (Bane unclaimed, the Trench Monarch worn by a man who never "
            "sanctioned it). The sub-series' first entry to show the doctrine reach formal, written "
            "institutional permanence rather than only informal reach (MCD-570/572/573/587) or living "
            "memory (MCD-978/1053), directly extending MCD-1086's legitimacy-test outcome into its lasting "
            "procedural consequence. Closes the twenty-first wave (with MCD-1086 and MCD-1087) on a quiet, "
            "reflective register distinct from both prior wave-closing reflections (MCD-986, MCD-1055). No "
            "new named characters."
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
            "batch": 250,
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
