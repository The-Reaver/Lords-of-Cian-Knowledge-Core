#!/usr/bin/env python3
"""Batch 321: reconciliation corrections surfaced by a read-only fable-review pass on the Crow King
Alias Chronicle corpus (102 entries). Mechanical fixes (a generation-count contradiction, a
Trinity-era anachronism, a contradictory "neutral Sovereign Trust magistrate" polity, the Rebellion
treated as a still-live war decades into the Long Mask, garbled dialogue misattributing who taught/
tested whom, a misattributed written-page authorship, a misattributed rasp-voice origin, wrong
rule-ID citations, loose "age 23" headers on entries that read as spanning years, a stale tracker
row, and an overclaimed cross-reference) -- no new creative facts, no new named characters, pure
reconciliation against already-locked canon, matching the Batch 226/68/320 precedent. The great
majority of the fixes (prose rewrites, continuity-note corrections, file-header clarifications) were
applied directly to the Chronicle markdown files; this script carries only the handful of changes
that also touch the canonical rule statement text in canon-ledger.json."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Read-only fable-review pass (Crow King Alias Chronicle corpus), reconciliation pass, 2026-10-02"

with open(LEDGER_PATH) as f:
    ledger = json.load(f)

rules_by_id = {r["id"]: r for r in ledger["rules"]}

# --- Amend rule statements to match the corrected Chronicle prose ---
AMENDMENTS = {
    # C1: MCD-854 wrongly framed the apprentice deepening her teaching of her own already-established
    # student (the third generation, MCD-548) as introducing a new, fourth person ("a third generation
    # of the craft"). No new generation is introduced in this entry.
    "MCD-854": (
        '"The Third Voice She Never Expected" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-third-voice-she-never-expected.md), The Crow King Alias "
        "Chronicle XXXIX, wave 13 of ten (waves 6-15). Corrected Batch 321, 2026-10-02: the apprentice "
        "deepens her own teaching of her already-established student (the third generation, MCD-548) "
        "after the student asks to be taught properly rather than simply deployed -- not the "
        "introduction of any new, fourth generation, as an earlier draft of this statement wrongly "
        "implied."
    ),
    # C2: explicitly anchored to "the fourth generation," whose own teaching lineage sits decades into
    # the 284-year Long Mask, well after the Trinity's age-30 vault surrender (MCD-246) -- the Trinity
    # cannot appear here. Swapped to the Long-Mask-era gear system per ARS-344 through ARS-356.
    "MCD-1484": (
        '"What Burned Loud Enough to Hear" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-burned-loud-enough-to-hear.md), Crow King Alias Chronicle "
        "C, wave 34, opening it. Corrected Batch 321, 2026-10-02: this entry is explicitly anchored to "
        '"the fourth generation," whose own teaching lineage sits decades into the 284-year Long Mask, '
        "well after the Trinity's already-locked age-30 vault surrender (MCD-246) -- the original "
        'statement wrongly described a "full-Trinity combat showcase." A detailed Long-Mask-era gear '
        "showcase rescuing twelve hostages from a deliberately-set burning granary, deliberately "
        'inverting "The Vault That Held No Light" (MCD-1045, wave 20, a legitimately pre-30 Trinity '
        "entry): where that entry used total silence as the tactical hinge, this one uses total, "
        "overwhelming noise -- cracking timber, exploding grain sacks, a failing roof beam -- with "
        "Kanja's own Rexmar-Mar instinct, the Forge-Coat, Ironfall Boots, the Ironhand Gauntlets, and "
        "the Rexmar Machete all reading the room by pressure and rhythm rather than sight or clean "
        "sound. Establishes structural fire/collapse conditions as a new environmental register. No "
        "new named characters."
    ),
    # C3/C4: "a neutral Sovereign Trust magistrate" is a contradiction (the Sovereign Trust is Kanja's
    # enemy polity, not a neutral one); reassigned to a magistrate from Aethel-Gard, already-locked as
    # neutral with potential to ally (POL-108). The cross-border-conflict framing is dropped with it.
    "MCD-1261": (
        '"The Foreign Magistrate\'s Report" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-foreign-magistrates-report.md), Crow King Alias Chronicle "
        "LXIX, wave 23, closing it. Corrected Batch 321, 2026-10-02: the original statement named her "
        '"a neutral Sovereign Trust magistrate" -- a contradiction, since the Sovereign Trust is '
        "Kanja's enemy polity, not a neutral one. A magistrate from Aethel-Gard (`POL-101`), a "
        "genuinely neutral polity (`POL-108`), formally documents the Hymn-Engine's true, unembellished "
        "history -- including its failures -- for an official archival record, the first institutional "
        "(rather than folk) documentation of the phenomenon. No new named characters. Closes wave 23 "
        "(with MCD-1259 and MCD-1260)."
    ),
    # C9: the apprentice's permanent rasp is the cost of the Braid's six-week rehearsal (MCD-384/418),
    # not the on-the-spot original marsh trick, which had no rehearsal at all.
    "MCD-418": (
        '"The Voice That Carried Three Hundred" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-voice-that-carried-three-hundred.md), Crow King Alias "
        "Chronicle VI, closing the second wave. Years later, one of the crew's original Hymn-Engine "
        "singers -- permanently rasp-voiced from the technique's six-week rehearsal -- teaches a new "
        "recruit the real cost behind the Braid's mechanics (corrected Batch 321, 2026-10-02 from "
        '"the marsh trick\'s mechanics," since the marsh trick itself had no rehearsal): sustained, '
        "relaxed consistency rather than forced power, and a toll to her voice she has never regretted "
        "paying. No new named characters. Closes the Crow King's second three-Chronicle wave (with "
        "'The Trap That Almost Closed,' MCD-416, and 'When the Crow Could Not Fly,' MCD-417)."
    ),
    # E5: MCD-1479's own teaching did not begin "immediately" -- it followed three separately deferred
    # visits, with no formal probation period at all, distinct from MCD-1482's imposed year's probation.
    "MCD-1482": (
        '"The Hunter Who Chose to Learn" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-hunter-who-chose-to-learn.md), Crow King Alias Chronicle "
        "XCVIII, wave 33. Corrected Batch 321, 2026-10-02 (a garbled timing phrase in the narrative "
        "reworded, and this statement's mischaracterization of MCD-1479 fixed). The Directorate "
        'officer who once tried to deceive Kanja himself ("The Hunter Who Studied the Hunter," '
        "Chronicle LXXIII, MCD-1265, wave 25) returns years later, having left Directorate service, "
        "asking to be taught rather than to counter the craft -- the first entry to bring a former "
        "adversary toward the lineage rather than resolve him as a defeated opponent. Kanja imposes a "
        "full year's probation working alongside the lineage before any teaching is considered, "
        "deliberately distinguished from the fifth generation's own admission (MCD-1479), reached only "
        "after three separately deferred visits and with no formal probation period imposed at all. No "
        "new named characters; the officer remains unnamed, per his original introduction."
    ),
    # E7: "Does not contradict" undersells the relationship -- this entry is consistent with, and
    # extends, Voris's established retirement rather than merely avoiding a conflict with it.
    "MCD-1262": (
        '"The Second Who Became the First" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-second-who-became-the-first.md), Crow King Alias Chronicle "
        "LXX, wave 24, opening it. Commandant Voris's former second, now promoted in his place after "
        "Voris's voluntary step-back from active pursuit, faces the craft for the first time without "
        "Voris's own field re-engagement, consulting the retired Voris directly for guidance rather "
        "than a solution. Consistent with, and extended by, Voris's established retirement (MCD-860) "
        "(corrected Batch 321, 2026-10-02 from the weaker 'does not contradict'). No new named "
        "characters."
    ),
}

for rid, new_statement in AMENDMENTS.items():
    assert rid in rules_by_id, f"Unknown rule id: {rid}"
    rules_by_id[rid]["statement"] = new_statement

ledger["batches_completed"].append({
    "batch": 324,
    "date": str(date.today()),
    "source": SOURCE,
    "rule_count": 0,
    "note": (
        "Reconciliation pass following a read-only fable-review of the Crow King Alias Chronicle "
        "corpus (102 entries), applied directly to the Chronicle files plus this handful of matching "
        "rule-statement amendments. No new rules, no new named characters -- pure reconciliation "
        "against already-locked canon, matching the Batch 226/68/320 precedent. Fixed: a "
        "generation-count contradiction where the apprentice deepening her own teaching of her "
        "already-established student (the third generation) was mistakenly framed as introducing a "
        "new, fourth person (MCD-854, plus a narrative-prose fix at MCD-916 restoring 'the apprentice' "
        "as the one who built and handed down a plan, not 'the apprentice's student'); a Trinity-era "
        "anachronism (MCD-1484, explicitly anchored to 'the fourth generation' decades into the Long "
        "Mask, swapped to the Long-Mask-era gear system per ARS-344 through ARS-356, matching the "
        "already-established fix pattern from Batch 314's Captain Trinity-fix; one-line pre-age-30 "
        "clarifications added to the two legitimate Trinity entries, MCD-1078 and MCD-1045, so this "
        "ambiguity doesn't recur); a contradictory 'neutral Sovereign Trust magistrate' (the Sovereign "
        "Trust is Kanja's enemy polity, not a neutral one) reassigned to a magistrate from Aethel-Gard, "
        "already-locked as neutral with potential to ally (MCD-1261, POL-108); the Rebellion treated "
        "as a still-live, two-sided war well into the Long Mask (MCD-1261's border framing, MCD-1275's "
        "'along the front,' and MCD-1262/1281's framing of ongoing active pursuit of 'the Crow King' "
        "by name reworked to pursuit of the craft/legend, since Kanja operates under the Scourge "
        "identity by this point, ARS-310); garbled dialogue misattributing who taught and tested whom "
        "across the generational lineage (MCD-1258's 'When I taught you'/'he asked me first' corrected "
        "to the apprentice/'she asked me first' per MCD-1046; MCD-1280's reversed who-brought-whom "
        "line and its claim that Kanja tested the third generation directly, corrected to the fourth "
        "generation per MCD-1046; MCD-1479's parallel claim that the third generation 'answered' "
        "Kanja's founding question, corrected to the apprentice, consistent with MCD-548); a "
        "misattributed written-page authorship (MCD-1409, the fourth generation claiming to have "
        "written the doctrine page himself rather than having heard the third generation read it "
        "aloud, per MCD-1256/1257); a misattributed rasp-voice origin (MCD-1264's 'original marsh "
        "trick' corrected to 'the Braid's six-week rehearsal,' and MCD-418's statement softened from "
        "'the marsh trick's mechanics' to 'the Braid's mechanics'); a reconciling line added to MCD-848 "
        "acknowledging the campfire idea sat shelved for roughly a year before the Wetlands "
        "encirclement forced it back out under pressure, reconciling MCD-236's 'invented ... on the "
        "spot' with the earlier months of development; wrong rule-ID citations (MCD-1267's CC-118/"
        "MCD-238 corrected to CC-117/CC-119; MCD-1410's MCD-1286 corrected to MCD-1266; MCD-915/"
        "MCD-987's wrongly-cited Chronicle XXVI tap-signal origin corrected to this entry itself/"
        "MCD-915, since Chronicle XXVI has no tap signals); loose 'age 23' headers on nine entries "
        "(MCD-449-451, 494-496, 546-548) whose own internal text implies years of elapsed time, "
        "loosened to 'ages 23-28'; a stale tracker row (the Crow King's count corrected from 93 to "
        "102 Chronicles, status corrected from 'not started (backfill)' to 'walkthrough drafted,' "
        "matching the alias's own profile-doc status); an inquiry-timing disambiguation (MCD-385's "
        "'the Coalfell inquiry, years after' reworded to 'a follow-up inquiry into Coalfell, years "
        "after,' distinguishing it from MCD-384's own inquiry-board testimony 'weeks later'); and an "
        "overclaimed cross-reference softened from 'already establishes' to 'consistent with, and "
        "extended by' (MCD-1262's statement and continuity note, MCD-1281's continuity note, and the "
        "alias's own profile doc). Two garbled prose lines reworded for clarity (MCD-1486's 'the day "
        "the trap door had shown him' and its 'a handful of seasons' vs. MCD-1278's three-week siege "
        "mismatch; MCD-1482's 'one season before it would have worked'). Two world-consistency slips "
        "fixed (MCD-1077's 'false radio chatter' -> 'false signal chatter,' no radios in this world; "
        "MCD-1484's 'popped like far-off gunfire' -> 'popped like far-off siege-shot'). Two "
        "writers'-room leaks removed from narrative prose (MCD-1282's 'Thirty waves and ninety "
        "Chronicles' -> 'Decades and four generations'; MCD-494's 'Chronicle-worthy successes' -> "
        "'the successes people retell')."
    ),
})

ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
ledger["last_updated"] = str(date.today())

ids = [r["id"] for r in ledger["rules"]]
assert len(ids) == len(set(ids)), "Duplicate rule IDs detected!"

with open(LEDGER_PATH, "w") as f:
    json.dump(ledger, f, indent=2)
    f.write("\n")

print(f"OK: {len(ledger['rules'])} total rules, {len(ledger['batches_completed'])} batches, "
      f"ledger_version {ledger['ledger_version']}, zero duplicate IDs.")
