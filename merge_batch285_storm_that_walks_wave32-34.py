#!/usr/bin/env python3
"""Batch 285: Storm That Walks Alias Chronicle waves 32, 33, and 34 (9 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "Continues the Alias Chronicle sub-series' thirty-second, thirty-third, and thirty-fourth "
    "waves for the Storm That Walks, under Abad's direct authorization: \"do 3 more alias wave for "
    "all eleven.\" Wave 32 tests the weight of authority itself: the fourth-generation apprentice "
    "(ceded full forecasting authority at MCD-1419) makes her first honest independent miscalculation "
    "while holding it alone, a small-stakes ordinary miss rather than sabotage; a coastal volcanic "
    "ash-fall gives this alias its first genuine equipment failure, Obsidian Malice's discharge "
    "housing fouling mid-engagement and forcing Mafesto and Onyx of Oblivion to carry the fight "
    "without it; and Trust maritime underwriters begin pricing insurance premiums against certified "
    "school readings, the doctrine's first purely actuarial integration, tested by a contested claim "
    "resolved through the transparent-misses tradition. Wave 33 tests the craft against technology and "
    "bloodline: a Trust engineer's mechanical pressure-gauge relay network is tested head-to-head "
    "against the same already-flagged cold-current model gap and found to measure everything except "
    "the felt judgment that matters, resolving into a supplementary instrument layer rather than a "
    "replacement; the third-generation student's own son chooses shipwrighting over the family craft, "
    "the sub-series' first explicit dramatization of its non-hereditary continuity; and the long-"
    "dangling smuggling faction (MCD-1053/MCD-1338) is finally cornered and closed out in a detailed "
    "full-Trinity combat showcase using the overlap-window method, with half its crews offered "
    "legitimate trade routes. Wave 34 closes on new registers and legacy: the doctrine is used "
    "forensically for the first time, reconstructing a storm that already happened to locate "
    "survivors of an uninvolved wreck, marking the alias's hundredth Chronicle; the school holds its "
    "first purely joyful, zero-peril entry, guaranteeing clear skies for the apprentice's own coming-"
    "of-age festival; and the written creed (MCD-1345) fills its first volume, opening a second with "
    "the still-unresolved Titan-class weather gap (MCD-1420) deliberately carried forward rather than "
    "resolved. No new named characters across all nine entries; every entry reuses already-locked "
    "recurring figures (the student, the apprentice, the rival fleet's dual-tradition sailor, the "
    "northern pilot, Efa Gol, Kanja), collision-checked against the full live ledger before drafting. "
    "Abad's approval: \"do 3 more alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1505",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Miss That Was Only Hers\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-miss-that-was-only-hers.md), Storm That Walks Alias "
            "Chronicle XCIV, wave 32, first entry in the wave. Months after the fourth-generation "
            "apprentice was ceded full forecasting authority (MCD-1419), she makes her first genuine "
            "independent miscalculation while holding it alone -- an honest, small-stakes miss with no "
            "external cause -- and logs it transparently in the ledger herself, testing what the "
            "authority actually costs now that no one checks it behind her. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1506",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Ash Choked Off\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-ash-choked-off.md), Storm That Walks Alias "
            "Chronicle XCV, wave 32. A coastal volcanic ash-fall -- a new hazard for this alias -- fouls "
            "Obsidian Malice's discharge housing mid-engagement against an opportunistic Directorate "
            "strike, the sub-series' first genuine equipment failure for this alias, forcing Mafesto's "
            "Kinetic Transfer System and Onyx of Oblivion's Whisper of Shadows to carry the fight "
            "without their third piece. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1507",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Premium Paid on a Miss\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-premium-paid-on-a-miss.md), Storm That Walks Alias "
            "Chronicle XCVI, wave 32, closing the wave. Trust maritime underwriters begin pricing "
            "insurance premiums against the school's certified readings, the doctrine's first purely "
            "actuarial/economic integration; a contested claim over a wrecked hull that sailed on an "
            "honestly-worded moderate-risk reading is resolved when the third-generation student's "
            "ledger forces the underwriter to honor its own adopted risk-language. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1508",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Glass That Couldn't Feel the Cold Current\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-glass-that-couldnt-feel-the-cold-current.md), Storm "
            "That Walks Alias Chronicle XCVII, wave 33, first entry in the wave. A Trust engineer's "
            "relay network of mechanical pressure gauges, built to replace the school's trained "
            "readers outright, is tested against the same cold-current interaction already flagged as "
            "a doctrine gap at MCD-1346; the instruments read pressure accurately but miss the felt "
            "judgment that catches the danger, resolving into a supplementary early-warning layer "
            "feeding the school's readers rather than a replacement for them. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1509",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Trade He Chose Instead\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-trade-he-chose-instead.md), Storm That Walks Alias "
            "Chronicle XCVIII, wave 33. The third-generation student's own grown son tells her he will "
            "not carry the craft forward, having apprenticed instead to a hull-wright -- the "
            "sub-series' first explicit dramatization on the page that the doctrine's continuity was "
            "never a matter of bloodline, only of choosing it, retroactively affirming the "
            "already-unrelated apprentice's own selection (MCD-1343). Purely domestic register, no "
            "combat. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1510",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Window That Ended the Smuggling\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-window-that-ended-the-smuggling.md), Storm That Walks "
            "Alias Chronicle XCIX, wave 33, closing the wave. The smuggling faction that raided the "
            "school (MCD-1053) and exploited total windless fog (MCD-1338) is finally cornered in a "
            "detailed full-Trinity combat showcase -- Onyx of Oblivion's Veil Piercer exposing decoy "
            "hulls, Mafesto's Kinetic Transfer System, Obsidian Malice's discharge -- using the "
            "overlap-window method from MCD-1418/1419 to close the last blind spot on the coast; half "
            "the faction's crews are offered legitimate trade routes given the school's growing reach, "
            "the rest handed to the magistrate. Closes a long-dangling recurring antagonist thread. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1511",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Storm They Read Backward\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-storm-they-read-backward.md), Storm That Walks Alias "
            "Chronicle C, wave 34, first entry in the wave -- the alias's hundredth Chronicle. The "
            "doctrine is used forensically for the first time: the student and the fourth-generation "
            "apprentice reconstruct a storm that already happened, using drift patterns and the "
            "northern pilot's ice-reading method, to locate survivors of an uninvolved vessel that "
            "never consulted the school before it sailed; Kanja conducts the physical rescue using "
            "Mafesto's strength and Onyx of Oblivion's Whisper of Shadows, with no adversary and no "
            "combat. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1512",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Sky They Ordered Clear\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-sky-they-ordered-clear.md), Storm That Walks Alias "
            "Chronicle CI, wave 34. The doctrine's first purely joyful, zero-peril use: the school "
            "guarantees clear skies for the fourth-generation apprentice's own coming-of-age festival, "
            "with no threat, hostile party, or stake of any kind; Kanja appears without Onyx of "
            "Oblivion at his hip for the first time in this alias's run. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1513",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Second Volume\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-second-volume.md), Storm That Walks Alias Chronicle "
            "CII, wave 34, closing the wave. The written creed begun at MCD-1345 fills its last page "
            "after nine years and a second volume opens; the fourth-generation apprentice's first "
            "entry in it deliberately carries the still-unresolved Titan-class weather gap (MCD-1420) "
            "forward rather than resolving it, closing wave 34 on continuity rather than resolution, "
            "consistent with MCD-1363's established practice of leaving this alias's frontier open. "
            "Confirms the current generational state: Sephtis and his direct successor are both "
            "deceased, the third-generation student remains senior credentialed authority, and the "
            "fourth-generation apprentice holds full independent forecasting authority as acting field "
            "forecaster. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)
    assert len(NEW_RULES) == 9, f"expected 9 new rules, got {len(NEW_RULES)}"
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"
    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"
    ledger["rules"].extend(NEW_RULES)
    ledger["batches_completed"].append(
        {
            "batch": 285,
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
