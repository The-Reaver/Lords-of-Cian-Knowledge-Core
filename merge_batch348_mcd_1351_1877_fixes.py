#!/usr/bin/env python3
"""Batch 348: Fable-review mechanical fixes, MCD-1351 through MCD-1877 range.

Applies the mechanical subset of a read-only Fable-model review of MCD rules
1351-1877: two gear/era-anachronism corrections (C2, C6 -- the Sovereign
Ghost's Lodestone Lens entry and the Blue-Collar Titan's Killane-campaign
phase terminology), four citation/cross-reference corrections (E1), and a
category-field normalization pass (E2) plus one optional clarifying note
(E3, Mira/Mira Threnarr-Olmedrin coincidental homonym).

Deliberately NOT applied -- left completely untouched, pending Abad's own
creative/worldbuilding ruling: C1 (the Captain's-Five Moonvault gifts used
anachronistically pre-Book-1 -- MCD-1462's Lodestone Lens/Whalebone Tether
claims themselves, MCD-1465, MCD-951), C3 (the Sovereign Ghost era lock vs.
Rannic Sorvell's Long-Mask-era defeat -- MCD-250, CC-150, MCD-1858), C4
(Garren Hask's cross-track lifespan contradiction -- MCD-1407, MCD-1408,
MCD-1422, MCD-1423, MCD-1486), C5 (Vael Korr-Drennen's gender split --
MCD-1639, MCD-1689, MCD-1659, MCD-1705), the Torvald rename question
(MCD-1524, MCD-1527), MCD-1425's low-confidence era mismatch, and all
enrichment items.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Fable-model read-only review of MCD-1351 through MCD-1877 against the "
    "full ledger and corpus, mechanical-fix subset implemented by this "
    "session."
)

AMENDMENTS = {
    # C2: Sovereign Ghost's Lodestone Lens entry -- the Sovereign Eyes don't
    # exist yet at this Rebellion-era alias's placement; Mafesto's own
    # close-range helm overlay is period-correct. Only this one substring is
    # touched -- the Lodestone Lens/Whalebone Tether claims (C1, needs Abad)
    # are left completely untouched.
    "MCD-1462": (
        "\"What the Seafloor Told the Lens\" (full narrative text at "
        "docs/lords-of-cian/chronicles/what-the-seafloor-told-the-lens.md), "
        "Sovereign Ghost of the Great Sea Alias Chronicle XCVI, wave 32, "
        "closing the wave. A new-gear register: the first dramatized use of "
        "the Lodestone Lens (`ARS-382`) for this alias, reading a shifting "
        "seafloor hazard at extreme range from the deck to redirect a convoy "
        "no lookout could have seen coming in time -- distinct from "
        "Mafesto's own close-range helm overlay used throughout prior "
        "entries, and from the deliberate false channel-marker reef ambush "
        "(`MCD-772`) since this hazard is natural and undetected by anyone "
        "rather than a trap. Reuses Garren Hask and Danne Sok. No new named "
        "characters. Closes wave 32 (`MCD-1460` through `MCD-1462`). "
        "Corrected Batch 348, 2026-10-02: reworded a stale reference to the "
        "Sovereign Eyes' close-range Blueprint Eye HUD (not yet built at "
        "this alias's Rebellion-era placement) to Mafesto's own period-"
        "correct close-range helm overlay."
    ),
    # C6: the Blue-Collar Titan's Killane-campaign phase terminology, now
    # reconciled to the two-phase COVERT/OPEN structure locked at MCD-1877.
    "MCD-1402": (
        "\"The Man He Let Walk Away\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-man-he-let-walk-away.md), "
        "Blue-Collar Titan Alias Chronicle XCIII, wave 31, closing the wave. "
        "A reconciliation payoff to \"The Engineer Who Fought Like One\" "
        "(MCD-670), the alias's first genuine skill-versus-skill duel: the "
        "same unnamed Trust combat engineer, spared then on the strength of "
        "mutual professional recognition, returns later in the campaign's "
        "open phase, months on, as a civilian collaborator rather than an "
        "adversary, asking for the crew's actual rebuilding expertise rather "
        "than the alias's reputation, and receives it on the same standards "
        "as any other request, no favor granted for old respect. Reuses "
        "already-locked crew member Danne Sok and the unnamed engineer from "
        "MCD-670. No new named characters. Closes wave 31 (with MCD-1400 and "
        "MCD-1401). Corrected Batch 348, 2026-10-02: \"returns years later\" "
        "corrected to \"returns later in the campaign's open phase, months "
        "on\" to match the Killane campaign's now-locked ages-20-21 "
        "two-phase timeline (MCD-1877)."
    ),
    "MCD-1401": (
        "\"The Collective That Borrowed His Name\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-collective-that-borrowed-his-"
        "name.md), Blue-Collar Titan Alias Chronicle XCII, wave 31. The "
        "alias's first institutional-legitimacy-poaching entry: a rival "
        "post-ceasefire trade collective, the Founders' Guild, falsely "
        "implies Kanja's personal endorsement to draw membership away from "
        "the tradesmen's association he deliberately founded without his "
        "own name attached (MCD-662, reaffirmed MCD-1200). Rather than "
        "exposing or shutting the collective down, Kanja refuses in front "
        "of its own recruits to confirm or deny the implied endorsement, "
        "reaffirming that neither is his to give; the false claim is "
        "dropped within a season and the collective's membership holds "
        "steady on honestly earned reputation alone. Reuses already-locked "
        "crew member Garren Hask (CC-115). The Founders' Guild and its "
        "unnamed founder are collision-checked clean. No new named "
        "characters. Corrected Batch 348, 2026-10-02: \"post-war\" "
        "corrected to \"post-ceasefire\" to match MCD-1877's "
        "\"negotiated local ceasefire\" phase-boundary terminology for the "
        "Killane theater, not a full war's end."
    ),
    # E1: citation/cross-reference corrections.
    "MCD-1374": (
        "\"The Boarding in the Blind Dark\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-boarding-in-the-blind-dark.md), "
        "Captain Alias Chronicle LXXIV, wave 25. A detailed Long Mask-era "
        "gear boarding-action combat showcase (the Sovereign Eyes' overlay, "
        "the Forge-Coat and Ironfall Boots, the Ironhand Gauntlets, the "
        "Rexmar Machete, and Kanja's own instinctive Rexmar-Mar tactical "
        "sense) fought in total darkness during a moonless storm, the "
        "sub-series' first blind-dark engagement for this alias, with Efa "
        "Gol coordinating the operation by sound-count alone. Frees "
        "forty-one captives from a slaver vessel. No new named characters. "
        "Corrected, Batch 314, 2026-09-28: an earlier draft mistakenly "
        "staged this as a full-Trinity showcase, despite this Chronicle's "
        "placement well within the 284-year Long Mask era, after Kanja's "
        "already-locked age-30 surrender of the Trinity to its sealed vault "
        "(`MCD-246`); replaced with his correct Long-Mask-era kit (the "
        "seven-piece post-Mafesto gear system, `ARS-344` through `ARS-356`, "
        "plus the Rexmar Machete and his own instinctive Rexmar-Mar "
        "tactical sense). Corrected Batch 321, 2026-10-02: fixed a "
        "misattributed cross-reference (this is the Storm That Walks "
        "alias's own total-darkness precedent, `MCD-426`, \"The Dark Water "
        "Ambush\" -- not to be confused with the Crow King's unrelated "
        "\"The Vault That Held No Light,\" `MCD-1045`) and reworded the "
        "Sovereign Eyes' perception function from its amber \"glow\" to its "
        "overlay (`ARS-350`). Corrected Batch 348, 2026-10-02: that same "
        "cross-reference's citation itself was still wrong (MCD-416 is a "
        "different Chronicle, \"The Trap That Almost Closed\"; \"The Vault "
        "That Held No Light\" is correctly MCD-1045, now fixed above)."
    ),
    "MCD-1500": (
        "\"What the Smoke Said\" (full narrative text at "
        "docs/lords-of-cian/chronicles/what-the-smoke-said.md), Lord of "
        "Embers Alias Chronicle XCVIII, wave 33. Rebellion era, age 27, the "
        "Rolling Foundry Campaign (MCD-241). A genuinely new logistics/"
        "communication register: Callum Breck proposes a standardized "
        "smoke-signal relay code across the campaign's linked forge sites "
        "for early warning, built from the campaign's own forge chimneys "
        "rather than any gear system. The code is tested within a week when "
        "a site's hourly all-clear pulse goes silent with no raid signal "
        "ahead of it -- the deliberately built silent-pulse protocol, not "
        "an active signal, is what actually saves three apprentices buried "
        "by a support collapse, reaching them in two hours rather than the "
        "half-day a rider would need. No new named characters. Corrected "
        "Batch 321, 2026-10-02: removed a mistaken claim that the chimney "
        "code repurposes the Forge-Coat's Smoke System (ARS-354, within the "
        "ARS-344 through ARS-356 gear system) -- that gear doesn't exist "
        "until the Long Mask, ages 33-314 -- recast as a plain, "
        "un-gear-cited chimney-signal code, matching the narrative, which "
        "never claimed otherwise. Corrected Batch 348, 2026-10-02: the "
        "prior correction's own citation was wrong (MCD-291-293 are "
        "unrelated rules -- Bone-Tempering conductance, a Foundry-Anvil "
        "relabel, a Book-5 resting figure -- the Smoke System is correctly "
        "ARS-354, now fixed above) and its age range was wrong (\"ages "
        "33-284\" misstated the Long Mask's length in years as an age; the "
        "Long Mask's actual age range is 30 to 314, now fixed above)."
    ),
    "MCD-1720": (
        "Lauris Chronicle CIII, 'The Patience He Doesn't Save for Her' "
        "(full narrative text at docs/lords-of-cian/chronicles/lauris-"
        "chronicle-ciii-the-patience-he-doesnt-save-for-her.md), the eighth "
        "Strand W entry of this wave. A third, deliberately non-training-"
        "deck entry with Valen: he spends an hour correcting an unnamed "
        "sentry's basic stance with the same unhurried patience he gives "
        "Lauris herself, and Lauris watches from the sidelines rather than "
        "participates, putting his Master-at-Arms discipline (ARS-344) on "
        "the page from an observer's vantage for the first time. No new "
        "named characters. Corrected Batch 348, 2026-10-02: the "
        "Master-at-Arms citation was wrong (MCD-291 is an unrelated rule; "
        "Valen's Master-at-Arms role is correctly locked at ARS-344, now "
        "fixed above)."
    ),
    "MCD-1750": (
        "Ozmund Chronicle XXI, \"The Recruit He Almost Turned Away\" (full "
        "narrative text at docs/lords-of-cian/chronicles/ozmund-chronicle-"
        "xxi-the-recruit-he-almost-turned-away.md), opening a second "
        "Draconis-strand wave (Chronicles XXI-XXV, following the first "
        "wave's Chronicles I-VI), set later in the same pre-ceremony span, "
        "still strictly before the Fulfillment Ceremony (MCD-025), "
        "Aethelgard Verehimu alive. Dramatizes Draconis's (CC-085) standard "
        "for judging a House Guard recruit -- character surviving a bad "
        "first impression over polish -- through a rough-edged candidate, "
        "Brenner, who breaks formation to save a groundskeeper's child "
        "rather than hold the line as drilled; Draconis keeps him over his "
        "own second's objection. Ozmund privately absorbs a deliberately "
        "general lesson about judging instinct over performance, kept "
        "unspecific per the standing non-foreshadowing constraint. New "
        "minor named figure: Brenner (one-scene). Corrected Batch 348, "
        "2026-10-02: the wave's own chapter numbering was wrong/ambiguous "
        "(\"Chronicles II-VI\" collided with the first wave's own "
        "numbering); corrected to the actual Chronicles XXI-XXV."
    ),
    # E3 (optional): clarifying coincidental-homonym note.
    "MCD-1370": (
        "\"The Night the River Won\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-night-the-river-won.md), "
        "Captain Alias Chronicle LXX, wave 24. The sub-series' first "
        "genuine, unresolved rescue failure: a levee breaks in the dark and "
        "the crew saves thirty-one people but not a civilian father, "
        "Joran, who drowns going back for his wife, leaving his "
        "eight-year-old daughter Mira orphaned. Introduces two new minor "
        "named characters, Joran (non-recurring) and Mira (recurring "
        "through the rest of this run), both collision-checked clean "
        "against the full live ledger. First entry, wave 24. (Note: a "
        "coincidental homonym with the already-locked Mira "
        "Threnarr-Olmedrin, Lauris's Kares Prime combat instructor, "
        "MCD-164 -- different world, different era, matching the project's "
        "established coincidental-homonym precedent for names like "
        "Commodore Veska/Veska Karth-Ven.)"
    ),
}

# MCD-1877's category normalized to match comparable reconciliation rules
# (MCD-1533, MCD-1850-1865).
EXTRA_CATEGORY_AMENDMENTS = {
    "MCD-1877": "World Mechanics",
}

# E2: category normalization for the ten Kazi-era Phase 2 territory-Chronicle
# rules currently tagged with the corpus's two minority variants.
CATEGORY_NORMALIZE_IDS = [f"MCD-{i}" for i in range(1523, 1533)]
CATEGORY_NORMALIZE_FROM = {"territory-chronicle", "phase2-homage-chronicle"}
CATEGORY_NORMALIZE_TO = "phase2-territory-chronicle"


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}

    amended = []
    for rid, new_statement in AMENDMENTS.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        rules_by_id[rid]["statement"] = new_statement
        amended.append(rid)

    category_fixed = []
    for rid in CATEGORY_NORMALIZE_IDS:
        assert rid in rules_by_id, f"missing rule {rid}"
        cur = rules_by_id[rid].get("category")
        if cur in CATEGORY_NORMALIZE_FROM:
            rules_by_id[rid]["category"] = CATEGORY_NORMALIZE_TO
            category_fixed.append(rid)

    for rid, new_category in EXTRA_CATEGORY_AMENDMENTS.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        cur = rules_by_id[rid].get("category")
        if cur == "world-timeline":
            rules_by_id[rid]["category"] = new_category
            category_fixed.append(rid)

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule IDs found"

    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({
        "batch": next_batch,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": 0,
        "note": (
            "Mechanical-fix subset of a Fable-model read-only review of "
            "MCD-1351 through MCD-1877. Amends MCD-1462 (a Sovereign Eyes/"
            "Mafesto gear-anachronism substitution, C2), MCD-1402 and "
            "MCD-1401 (phase-boundary terminology reconciled to MCD-1877's "
            "locked two-phase Killane-campaign timeline, C6 -- MCD-1453's "
            "parallel sub-item skipped, no literal 'post-war' string "
            "present in its own statement), MCD-1374 (a cross-reference "
            "citation fix, MCD-416 -> MCD-1045), MCD-1500 (two citation/"
            "age-figure fixes: the Smoke System's real rule ID ARS-354, "
            "and the Long Mask's real age range 30-314 rather than its "
            "284-year length misstated as an age), MCD-1720 (a "
            "Master-at-Arms citation fix, MCD-291 -> ARS-344), and "
            "MCD-1750 (a chapter-numbering fix for its second Draconis-"
            "strand wave, Chronicles XXI-XXV rather than II-VI). Also "
            "appends an optional clarifying coincidental-homonym note to "
            "MCD-1370 (Mira / Mira Threnarr-Olmedrin, MCD-164). Normalizes "
            "the category field on 10 rules (MCD-1523 through MCD-1532, "
            "'territory-chronicle'/'phase2-homage-chronicle' -> "
            "'phase2-territory-chronicle', the corpus-wide plurality value) "
            "and on MCD-1877 ('world-timeline' -> 'World Mechanics', "
            "matching comparable reconciliation rules MCD-1533, "
            "MCD-1850-1865). One MCD-1402 sub-fix skipped: the reviewed "
            "fragment 'the visible evidence of years of work' does not "
            "appear anywhere in the live ledger text, so no change was "
            "made there beyond the 'returns years later' fix. All items "
            "marked NEEDS ABAD (C1, C3, C4, C5, the Torvald rename, E4, "
            "and all enrichment items) left completely untouched, pending "
            "Abad's own creative/worldbuilding ruling."
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
        f"{len(amended)} rule statements amended: {', '.join(amended)}. "
        f"{len(category_fixed)} category fields normalized: {', '.join(category_fixed)}."
    )


if __name__ == "__main__":
    main()
