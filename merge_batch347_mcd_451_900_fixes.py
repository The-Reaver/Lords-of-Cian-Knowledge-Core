#!/usr/bin/env python3
"""Batch 347: Fable-review fixes, MCD rules 451-900.

Applies the mechanical subset of a Fable-model read-only review of MCD rules
451-900: the Captain-track "fourth vessel" ambiguity (C2, MCD-607, plus a
matching Chronicle-prose fix); a Garren Hask ship-naming count gap (C3,
CC-115); a Danne Sok "freed by Kanja" phrasing contradicting the already-
locked CC-158/159/160 self-freed ruling (C4, MCD-530, plus a Chronicle-prose
fix to what-danne-sok-never-told-anyone.md); a Sovereign Eyes V4 refit
clarified from generic "new gear" (E1, MCD-811); a successor citation
corrected to name Efa Gol's own decoy-command successor rather than implying
Kanja has one (E2, MCD-829, combined with its own wave-count fix); an
anachronistic "Trench Monarch" alias reference in a pre-alias-era scene (E3,
MCD-623, plus a matching Chronicle-prose fix); an inverted
earlier/later-written-vs-set description (E4, MCD-680, combined with its own
wave-count fix); a run-on sentence in Jibaro Chronicle III restating the
same PH2-042 condition twice (E6, MCD-516); five Sovereign Ghost of the
Great Sea Alias Chronicle self-naming omissions missing "of the Great Sea"
(E7, MCD-378/379/410/411/412); and a corpus-wide "wave N of ten (waves
6-15)" wording fix for N=11..15, which should read "wave N of the ten-wave
run (waves 6-15)" to match the already-corrected wave-11-15 phrasing used
elsewhere (E5, ~146 rules across MCD-561 through MCD-890, excluding
MCD-606-620 which a prior batch already fixed, and excluding MCD-680/829
whose wave-count wording is folded directly into their own E4/E2 fixes
above rather than double-processed).

Deliberately NOT touched, per the review's own NEEDS ABAD flag: C1 (the
Garren Hask lifespan contradiction between the Captain and Scourge tracks),
C5 (the Storm That Walks Trinity-era timeline-density concern), the
enrichment items (a possible Aegis-Talisman artificer, a lifespan-
clarification rule, extending CC-115 further), and E8 (collision
spot-checks, which came back clean).
"""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Fable-model read-only review of MCD rules 451-900 against the full "
    "ledger and Chronicle corpus. Mechanical/reconciliation subset only; "
    "one cross-track creative contradiction (Garren Hask's lifespan) and "
    "one timeline-density concern (the Storm That Walks) are deliberately "
    "left for Abad's own ruling."
)

# --- Hand-written full-statement amendments (C2-C4, E1-E4, E6-E7) ---------
# MCD-829 and MCD-680 fold in their own "wave N of ten (waves 6-15)" ->
# "wave N of the ten-wave run (waves 6-15)" fix directly, so they are
# excluded from the E5 loop below rather than double-processed.

AMENDMENTS = {
    "MCD-607": (
        "\"The Vote That Named the Third Ship\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-vote-that-named-the-third-ship.md), "
        "Captain Alias Chronicle XXXII, wave 11 of the ten-wave run (waves 6-15). "
        "Garren Hask, having already named the fleet's first three flagships "
        "himself (The Audit, The Receipt, The Ledger), deliberately hands the "
        "naming of the fourth vessel to be formally named -- a non-flagship "
        "transport -- to a crew vote instead of keeping it as his own honor; "
        "the crew names her The Second Chance. Corrected Batch 321, 2026-10-02: "
        "originally framed as the fleet's third ship, colliding with the "
        "Sovereign Ghost of the Great Sea alias's own, separately locked "
        "third-flagship naming scene (MCD-788, The Ledger); reframed as the "
        "fourth vessel, resolving the cross-track collision. Hask's own line "
        "changed from \"I've had my say twice\" to \"I've had my say three "
        "times.\" Corrected again Batch 347, 2026-10-02: \"the fleet's fourth "
        "vessel\" reworded to \"the fourth vessel to be formally named,\" "
        "clarifying this counts formally-named ships rather than the fleet's "
        "literal fourth vessel overall (the fleet holds many more than four "
        "ships by this point)."
    ),
    "CC-115": (
        "Garren Hask: a dock-smith on Dock-Row Six/Lower Portside with 31 "
        "years' tenure, recruited into the rebellion at its founding when his "
        "wife's years of suspecting Scrip fraud are confirmed by the Forge-7 "
        "evidence. Becomes the crew's 'counter' -- tallying casualties (Black "
        "Trench: 93 of 120 survive) and later the 12,006 Cestari freed at "
        "Maw-9 -- and its ledger-keeper, a role the text frames as the form "
        "his loyalty takes. Personally named the fleet's first three "
        "flagship-class vessels, The Audit, The Receipt, and The Ledger "
        "(MCD-788)."
    ),
    "MCD-530": (
        "\"What Danne Sok Never Told Anyone\" (full narrative text at "
        "docs/lords-of-cian/chronicles/what-danne-sok-never-told-anyone.md), "
        "Bane Alias Chronicle XV, closing the fifth wave. Danne Sok (already "
        "locked, one of the three earliest crew members, who had freed "
        "himself before the Black Trench (MCD-234)) finally shares a memory "
        "kept private the whole war: the young Kanja's hands shaking for an "
        "hour after the first fight the three of them stood beside him, "
        "before any alias existed -- a private counterweight to the legend, "
        "extending the 'tired, not scary' theme (MCD-478) back to its "
        "literal origin. No new named characters beyond the already-locked "
        "Danne Sok. Closes Bane's fifth three-Chronicle wave (with 'The Boy "
        "Who Wanted to Be Him,' MCD-528, and 'The Siege That Took Nine "
        "Days,' MCD-529)."
    ),
    "MCD-811": (
        "\"The First Night in the New Coat\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-first-night-in-the-new-coat.md), "
        "The Scourge Alias Chronicle XXVI, wave 9 of ten (waves 6-15). Age "
        "241, the Sovereign Eyes V4 refit's debut (ARS-350); the new lenses' "
        "rough, unglamorous first deployment, teething failures included."
    ),
    "MCD-829": (
        "\"The Fight He Fought Angry\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-fight-he-fought-angry.md), The "
        "Scourge Alias Chronicle XLIV, wave 15 of the ten-wave run (waves "
        "6-15). Age 168, V3 gear. A rare loss of composure and fury after "
        "captives are murdered to destroy evidence; a near-overreach checked "
        "by Efa Gol's successor in decoy command (MCD-807)."
    ),
    "MCD-623": (
        "\"What Garren Hask Wrote Down First\" (full narrative text at "
        "docs/lords-of-cian/chronicles/what-garren-hask-wrote-down-first.md), "
        "The Trench Monarch Alias Chronicle XVIII, wave 6 of the ten-wave "
        "sixth-through-fifteenth run. Rebellion era, before the Dredge-Line "
        "Ambush. Not Hask's recruitment -- that happened earlier, at the "
        "Scrip-Forge Raid's Forge-7 evidence (`CC-115`) -- but the moment he "
        "formally takes over the crew's ledger-keeping role: his own "
        "pre-crew habit of independently cross-checking Kanja's figures is "
        "what earns him the job, grounding the later trust in his books in "
        "a concrete founding moment. No new named characters beyond the "
        "already-locked Garren Hask. Closes the Trench Monarch's sixth "
        "three-Chronicle wave. Corrected Batch 321, 2026-10-02: the "
        "original draft wrongly staged this as Hask's first meeting with "
        "Kanja and a recruitment scene, contradicting `CC-115`'s "
        "already-locked Forge-7 recruitment; reframed as a "
        "promotion/responsibility moment set before the Dredge-Line Ambush, "
        "and the erroneous 'thirty-one-year-old' age reference (31 is his "
        "tenure, not his age) corrected to 53, matching `CC-115`/Batch 48. "
        "Corrected again Batch 347, 2026-10-02: \"the Trench Monarch's "
        "figures\" was anachronistic (this scene is set before that alias "
        "name is coined); corrected to \"Kanja's figures.\""
    ),
    "MCD-680": (
        "\"What Garren Hask Wrote in the Margins\" (full narrative text at "
        "docs/lords-of-cian/chronicles/what-garren-hask-wrote-in-the-margins.md), "
        "The Blue-Collar Titan Alias Chronicle XLV, wave 15 of the ten-wave "
        "run (waves 6-15). Garren Hask's closing cost-accounting ledger "
        "tallies the alias's true toll, failures included, as a grounding "
        "counterweight to the legend, closing the ten-wave run. Corrected "
        "Batch 321, 2026-10-02: \"the one death\" corrected to \"the "
        "deaths\" -- earlier-set-but-later-written entries (MCD-893, "
        "MCD-1070, MCD-1192) establish further deaths across the Killane "
        "campaign beyond the loss recorded at MCD-656."
    ),
    "MCD-516": (
        "Jibaro Chronicle III, \"The Week Five Doors Refused\" (full "
        "narrative text at "
        "docs/lords-of-cian/chronicles/jibaro-chronicle-iii-the-week-five-doors-refused.md). "
        "Five genuinely abandoned buildings across Jibaro are simultaneously "
        "occupied past the one-day threshold, all becoming permanently "
        "unreclaimable under 'The Occupation' (PH2-042), proving the "
        "ability scales to multiple sites at once as long as each site "
        "belongs to an institution he can shame into complicity (PH2-042) "
        "-- the unambiguous-public-shame condition Chronicle II (MCD-468) "
        "established -- and no purely private property is among the five. "
        "An unnamed Kanja helps carry belongings during the transition, "
        "uninvolved otherwise. No new named characters. Third Jibaro "
        "territory Chronicle. Corrected Batch 340, 2026-10-02: reconciled "
        "the ability's stated condition with PH2-042's own already-locked "
        "wording, and removed a tech-level anachronism (a 'rail depot') "
        "from the Chronicle prose. Corrected again Batch 347, 2026-10-02: "
        "tightened a run-on sentence that restated the PH2-042 condition "
        "twice."
    ),
    "MCD-378": (
        "\"The Chains That Remembered the Anchor\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-chains-that-remembered-the-anchor.md), "
        "Sovereign Ghost of the Great Sea Alias Chronicle II. Rebellion era, "
        "a new naval engagement distinct from the Siege of the Ghost Harbor "
        "(MCD-235). A convoy escort gunship is disabled at range by the "
        "anchor-chain magnetic-interference weapon (MCD-235, captured Iron "
        "Shallows chain reforged into the housing), seizing every iron "
        "fitting aboard; Kanja boards personally during the paralysis, "
        "demonstrating Mafesto's Kinetic Transfer System absorbing the "
        "drop's impact, Onyx's Whisper of Shadows in close multi-attacker "
        "quarters, and Obsidian Malice's stored-charge discharge clearing "
        "the deck in one motion. The gunship surrenders without a hull "
        "breach. No new named characters; the surrendering captain is "
        "unnamed and one-scene. Second entry in the Sovereign Ghost's "
        "three-Chronicle wave."
    ),
    "MCD-379": (
        "\"What the Lantern Watch Prayed For\" (full narrative text at "
        "docs/lords-of-cian/chronicles/what-the-lantern-watch-prayed-for.md), "
        "Sovereign Ghost of the Great Sea Alias Chronicle III, closing the "
        "wave. A young Trust supply-vessel lantern watchman, who never once "
        "sights The Audit across an entire season of night watches, learns "
        "from an older hand that the legend now does the ghost's work "
        "without her needing to appear again -- the Ghost Harbor casualty "
        "list is real, but every quiet watch since has been the fear doing "
        "the rest on its own. Extends VB-060's presence doctrine to "
        "reputation alone, absent any actual appearance. No new named "
        "characters. Closes the Sovereign Ghost of the Great Sea's "
        "three-Chronicle wave (with 'A Ship That Was Already Gone,' "
        "MCD-377, and 'The Chains That Remembered the Anchor,' MCD-378)."
    ),
    "MCD-410": (
        "\"The Wreck They Named for Him\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-wreck-they-named-for-him.md), "
        "Sovereign Ghost of the Great Sea Alias Chronicle IV, first entry "
        "in the second wave. An ordinary storm sinks a merchant convoy, but "
        "rumor falsely attaches the fleet to it, triggering a formal Trust "
        "diplomatic complaint and denied insurance claims; Kanja surrenders "
        "the fleet's own navigation logs to a neutral Astral Archipelago "
        "tribunal, an unprecedented sacrifice of operational secrecy, and "
        "is cleared, forcing the insurers to honor the original claims. No "
        "new named characters beyond the already-locked Dol Maren."
    ),
    "MCD-411": (
        "\"What the Hull Told Dol Maren\" (full narrative text at "
        "docs/lords-of-cian/chronicles/what-the-hull-told-dol-maren.md), "
        "Sovereign Ghost of the Great Sea Alias Chronicle V. A detailed "
        "naval technical showcase from Dol Maren's perspective (already "
        "locked, CC-120/CC-121): during a genuine hurricane, The Audit's "
        "deliberately flexible hull construction outlasts a rigid-hulled "
        "Trust blockade squadron's pursuit, disabling two pursuing ships "
        "through ordinary stress fractures Maren had already predicted. The "
        "squadron's after-action report misattributes the outcome to "
        "'rebel naval technology' rather than patient shipwright "
        "engineering. No new named characters beyond the already-locked Dol "
        "Maren."
    ),
    "MCD-412": (
        "\"The Girl Who Waited for Black Sails\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-girl-who-waited-for-black-sails.md), "
        "Sovereign Ghost of the Great Sea Alias Chronicle VI, closing the "
        "second wave. A seven-year-old's family fishing boat, stranded and "
        "facing seizure by a Trust requisition vessel, is saved when the "
        "fleet simply positions itself between the two boats and holds "
        "position until the requisition captain withdraws -- no shots "
        "fired, no boarding. Decades later she tells her grandchildren the "
        "story, extending VB-060's presence doctrine into protection rather "
        "than only terror, mirroring 'What the Lantern Watch Prayed For' "
        "(MCD-379) from the rescued side. No new named characters. Closes "
        "the Sovereign Ghost of the Great Sea's second three-Chronicle wave "
        "(with 'The Wreck They Named for Him,' MCD-410, and 'What the Hull "
        "Told Dol Maren,' MCD-411)."
    ),
}

# --- E5: corpus-wide "wave N of ten (waves 6-15)" wording fix, N=11..15 ---
# MCD-680 and MCD-829 already fold this fix into their own hand-written
# AMENDMENTS entries above, so they are skipped here to avoid
# double-processing / overwriting the fuller hand fix with a stale one.

WAVE_PATTERN = re.compile(r"wave (1[1-5]) of ten \(waves 6-15\)")


def compute_e5_amendments(ledger):
    e5 = {}
    for rule in ledger["rules"]:
        rid = rule["id"]
        if not rid.startswith("MCD-"):
            continue
        try:
            num = int(rid.split("-")[1])
        except ValueError:
            continue
        if not (561 <= num <= 890):
            continue
        if 606 <= num <= 620:
            continue  # already fixed in a prior batch
        if rid in AMENDMENTS:
            continue  # already hand-fixed above, wave wording folded in
        statement = rule["statement"]
        if WAVE_PATTERN.search(statement):
            new_statement = WAVE_PATTERN.sub(
                lambda m: f"wave {m.group(1)} of the ten-wave run (waves 6-15)",
                statement,
            )
            e5[rid] = new_statement
    return e5


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}

    e5_amendments = compute_e5_amendments(ledger)
    full_amendments = dict(AMENDMENTS)
    full_amendments.update(e5_amendments)

    amended = []
    for rid, new_statement in full_amendments.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        rules_by_id[rid]["statement"] = new_statement
        amended.append(rid)

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule IDs found"

    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({
        "batch": next_batch,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": 0,
        "note": (
            "Fable-review fixes, MCD rules 451-900 (mechanical subset). "
            "Amends MCD-607 (the 'fleet's fourth vessel' phrase clarified "
            "to 'the fourth vessel to be formally named,' plus a matching "
            "fix to the-vote-that-named-the-third-ship.md); CC-115 (Garren "
            "Hask's ship-naming credit extended from two to all three "
            "flagships, The Audit/The Receipt/The Ledger); MCD-530 (Danne "
            "Sok's 'freed before the Black Trench' phrasing corrected to "
            "'freed himself,' matching the already-locked CC-158/159/160 "
            "self-freed ruling, plus a matching prose fix to "
            "what-danne-sok-never-told-anyone.md); MCD-811 (the generic "
            "'new gear' V4 debut clarified as the Sovereign Eyes V4 "
            "refit's lenses, ARS-350); MCD-829 (the vague 'his successor' "
            "corrected to name Efa Gol's own decoy-command successor, "
            "MCD-807, since Kanja himself has no successor -- combined "
            "with its own wave-count wording fix); MCD-623 (an "
            "anachronistic 'Trench Monarch's figures' reference, set "
            "before that alias name is coined, corrected to 'Kanja's "
            f"figures,' plus a matching fix to "
            "what-garren-hask-wrote-down-first.md's continuity note); "
            "MCD-680 (an inverted 'later-set-but-earlier-written' "
            "description corrected to 'earlier-set-but-later-written' -- "
            "combined with its own wave-count wording fix); MCD-516 (a "
            "run-on sentence restating the PH2-042 shame condition twice, "
            "tightened); MCD-378/379/410/411/412 (five Sovereign Ghost "
            "Alias Chronicle self-naming references missing 'of the Great "
            f"Sea,' added); and {len(e5_amendments)} further MCD rules "
            "between MCD-561 and MCD-890 (excluding MCD-606-620, already "
            "fixed in a prior batch, and MCD-680/829, folded into their "
            "own fixes above) whose statements read 'wave N of ten (waves "
            "6-15)' for N in 11-15, corrected to 'wave N of the ten-wave "
            "run (waves 6-15)' to match the phrasing already used "
            "elsewhere for waves 11-15 of this run; waves 6-10 read "
            "correctly as-is and were left untouched. Deliberately NOT "
            "applied, per the review's own flag: C1 (the Garren Hask "
            "lifespan contradiction between the Captain and Scourge "
            "tracks -- needs Abad's ruling on which account controls), C5 "
            "(the Storm That Walks Trinity-era timeline-density concern), "
            "the enrichment items (a possible Aegis-Talisman artificer, a "
            "lifespan-clarification rule, extending CC-115 further -- all "
            "new content), and E8 (collision spot-checks, which came back "
            "clean, nothing to fix)."
        ),
    })

    old_version = float(ledger["ledger_version"])
    ledger["ledger_version"] = str(round(old_version + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(
        f"OK: {len(ledger['rules'])} total rules, {len(ledger['batches_completed'])} "
        f"batches, ledger_version {ledger['ledger_version']}, zero duplicate IDs. "
        f"{len(amended)} rule statements amended ({len(AMENDMENTS)} hand-fixed, "
        f"{len(e5_amendments)} via the E5 wave-wording loop)."
    )


if __name__ == "__main__":
    main()
