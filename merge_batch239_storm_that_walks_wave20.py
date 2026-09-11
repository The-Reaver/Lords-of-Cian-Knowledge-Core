#!/usr/bin/env python3
"""Batch 239: Storm That Walks Alias Chronicle wave 20 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Storm That Walks' twentieth Alias Chronicle wave (LVIII-LX): a full-Trinity combat "
    "showcase defending the storm-reading school's coastal compound from a smuggler raid timed to "
    "exploit storm cover (MCD-1053, the first entry to place the school itself under direct attack); "
    "the third-generation student's (MCD-983) first fully independent, unconfirmed storm call, made "
    "while the successor is legitimately absent rather than testing her (MCD-1054); and the "
    "successor's own formal, undramatic retirement and full institutional handoff to that student, "
    "confirming the doctrine now runs three generations deep and outlives any single person's "
    "presence (MCD-1055, closing the wave). No new named characters were introduced -- the school's "
    "raiders, the harbor-master, the third-generation student, and the successor all remain unnamed, "
    "consistent with the sub-series' established pattern. All three entries are placed after "
    "Sephtis's death (MCD-982) and do not contradict it or re-open his fate; the successor's "
    "retirement is a chosen stepping-back, not decline or death. Zero new proper-noun collisions "
    "(grep-checked against the full live ledger before drafting). Abad's approval: \"doorway for all "
    "the aliases that remain\" (approval of Bane's individually-presented wave 20 plus blanket "
    "authorization to continue the same wave for the remaining ten aliases)."
)

NEW_RULES = [
    {
        "id": "MCD-1053",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Night They Came for the School\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-night-they-came-for-the-school.md), Storm That Walks "
            "Alias Chronicle LVIII, wave 20, first entry in the wave. A smuggling faction whose trade "
            "has been broken by the storm-timing doctrine's growing reach (extending the "
            "institutional-reach thread of MCD-570-575) raids the storm-reading school's (MCD-978) "
            "coastal compound under cover of a storm, the same tactic the doctrine itself has always "
            "denied them. A detailed full-Trinity combat showcase -- Mafesto's Kinetic Transfer "
            "System redirecting a ramming charge's kinetic load back through the attacking hull's own "
            "timbers, Onyx's Whisper of Shadows closing distance inside the storm's own dark and "
            "Cadence Ruin timing strikes to gust gaps as a deliberate message, Obsidian Malice "
            "collapsing a dune face to strand the third landing party in the open, Veil Piercer "
            "confirming no further landing follows -- defends the school and its sleeping students "
            "with zero casualties on either side beyond the raiders taken. The first Storm That Walks "
            "entry where the Trinity defends an institution rather than a fleet, vessel, or rescue. "
            "Set after Sephtis's death (MCD-982), with his successor (MCD-505) acting as the school's "
            "sole senior authority. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1054",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Reading the Third Student Made Alone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-reading-the-third-student-made-alone.md), Storm That "
            "Walks Alias Chronicle LIX, wave 20. With Sephtis's successor (MCD-505) three days away "
            "on legitimate institutional business, the third-generation student (first introduced "
            "MCD-983) makes her first fully independent, unconfirmed storm call under real stakes -- "
            "correctly overriding forty years of seasonal almanac pattern to move a harbor fleet "
            "early, with the storm arriving two hours ahead of even her own revised number and the "
            "early-moved fleet losing nothing. Kanja, present by coincidence rather than as her "
            "teacher or tester, tells her afterward that she inherited not Sephtis's gift but three "
            "generations' accumulated courage in being visibly wrong. The first entry to individually "
            "center the third-generation student's own independent judgment, distinct from MCD-557's "
            "second-generation first-solo-call entry by testing institutional depth one generation "
            "further, with the successor's absence circumstantial rather than a designed test. Set "
            "after Sephtis's death (MCD-982) and the school's founding (MCD-978); the successor "
            "remains alive and active elsewhere. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1055",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Outlived the Woman Who Carried It\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-outlived-the-woman-who-carried-it.md), Storm That "
            "Walks Alias Chronicle LX, wave 20, closing the wave. Now elderly, Sephtis's successor "
            "(MCD-505) formally and undramatically retires from making storm calls herself, telling "
            "the third-generation student (MCD-983) that the real risk was no longer her hands but "
            "being trusted past the point of being checked, and hands over her full running ledger of "
            "calls -- successes and honest misses alike -- as the doctrine's actual inheritance rather "
            "than the gift itself. Confirms the storm-timing doctrine's institutional continuity now "
            "runs three generations deep and does not depend on any single living person, echoing and "
            "extending MCD-986's closing reflection from an institutional rather than personal angle. "
            "Distinct from Sephtis's own death-and-succession arc (MCD-981-983): a chosen "
            "stepping-back, not decline or death; does not assert or imply the successor's death. "
            "Kanja present throughout as a quiet witness, no command or resolution authorship. Closes "
            "the Storm That Walks' twentieth three-Chronicle wave (with 'The Night They Came for the "
            "School,' MCD-1053, and 'The Reading the Third Student Made Alone,' MCD-1054). No new "
            "named characters."
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
            "batch": 239,
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
