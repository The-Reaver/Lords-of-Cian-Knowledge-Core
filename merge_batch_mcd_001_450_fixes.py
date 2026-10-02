#!/usr/bin/env python3
"""Fable-review mechanical fixes, MCD-001 through MCD-450 range.

Applies the mechanical/reconciliation subset of a read-only Fable-model review
of MCD-001 through MCD-450 against the full ledger: 24 statement-level fixes
(B1-B24, citation corrections, stale-figure reconciliations, a parent/child
disambiguation, a swapped list order, and a tech-level/real-world-object-leak
fix), plus metadata normalization (C1: uppercase LOCKED -> locked across 52
rules, with three composite statuses normalized separately; C2: null category
-> character-pyro on MCD-131/132/133; C3: territory-Chronicle category drift
normalized to phase2-territory-chronicle on 23 rules).

Deliberately NOT touched -- Section A of the review (genuine creative
contradictions requiring Abad's own ruling): the 296-vs-284-year Fulfillment
Ceremony timing question, the Kares Prime timeline arithmetic, Lauris/
Fermand's joining dates, Haryn Dael's age vs the Moonvault's age, Nadea
Thren's champion-seat history, Valen's join-date/surname, the first-Verehimu
contradiction, "Yuto Haku" naming, the adulthood-phase arithmetic for the
Kareth sisters, and the lower-priority A12 tensions. Also not touched: "B25"
from the original review (already fixed in an earlier batch -- MCD-1720
already correctly cites ARS-344, not MCD-291).

Every fix below was re-verified against the live ledger text immediately
before this script was written (exact-substring-count checks), since this
project runs many parallel fix-agents and some items may already have been
partially corrected by earlier batches. None of the 24 statement fixes or 3
status/category normalizations below were found already applied.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Fable-model read-only review of MCD-001 through MCD-450 against the "
    "full ledger, mechanical/reconciliation subset implemented by this "
    "session. Section A (genuine creative contradictions requiring Abad's "
    "own ruling) deliberately left untouched."
)

# ---------------------------------------------------------------------------
# Statement fragment replacements: (rule_id, old_fragment, new_fragment).
# Each old_fragment is asserted to appear exactly once in that rule's current
# live statement before being replaced; the resulting full statement is what
# gets written back.
# ---------------------------------------------------------------------------
FRAGMENT_FIXES = [
    # B2
    (
        "MCD-050",
        "Division 5, post-Thren replacement Champion Bolo Troth, function TBD.",
        "Division 5, post-Thren replacement Champion Bolo Troth, "
        "institutional-subversion and cult-coordination command (function "
        "resolved at MCD-135).",
    ),
    # B3
    (
        "MCD-034",
        'She will inherit two battle artifacts from the Kareth sisters '
        '(details deferred to "Session Lock 2, April 11 2026" -- not yet '
        'located in this corpus).',
        "She will inherit three battle artifacts from the Kareth sisters -- "
        "the Convergence, the Gradient, and the Patient Stone (ARS-361; "
        "received no earlier than Book 3).",
    ),
    # B6
    (
        "MCD-110",
        "(capital Karkosa, including Stormshelter Cove and Maw-7 Slab)",
        "(capital Karkosa, including Stormshelter Cove and the Throat -- "
        "the unnumbered Grand Maw of Karkosa, MAW-060; Maw-7 is the "
        "separate Keldane venue, MAW-061, per the Batch 103 GEO-003 "
        "correction)",
    ),
    # B7
    (
        "MCD-084",
        "Executed on the Slab of Maw-7.",
        "His parents were executed on the Slab of Judgment (Maw-7, "
        "Keldane; MAW-065/MAW-121).",
    ),
    # B8(a)
    (
        "MCD-209",
        "Across roughly 4,000 years of combat",
        "Across roughly 6,000 years of combat (MCD-1533)",
    ),
    # B8(b)
    (
        "MCD-209",
        "Orlok at post-enlightenment ~30,000x",
        "Orlok at post-enlightenment ~20,000x (MCD-096/CC-058)",
    ),
    # B9(a)
    (
        "MCD-214",
        "she is roughly twelve times Kanja's age in calendar years",
        "she is roughly nineteen times Kanja's age in calendar years",
    ),
    # B9(b)
    (
        "MCD-214",
        "(including Val Saeryn at 93,179, MCD-155)",
        "(including Val Saeryn at 93,179, MCD-101/MCD-149)",
    ),
    # B10
    (
        "MCD-217",
        "she is roughly 4,000 years old with roughly 96,000 years of "
        "expected lifespan remaining, consistent with the already-locked "
        "~100,000-year Karesian lifespan (MCD-148)",
        "she is roughly 6,000 years old (MCD-1533) with roughly 94,000 "
        "years of expected lifespan remaining, consistent with the "
        "already-locked ~100,000-year Karesian lifespan (MCD-149)",
    ),
    # B11(a)
    (
        "MCD-156",
        "Lauris was born ~4,000 years before the series' present.",
        "Lauris was born ~6,000 years before the series' present "
        "(MCD-1533).",
    ),
    # B11(b)
    (
        "MCD-156",
        "Selene (her mother) raised her for the first 1,400 years of her "
        "life before Selene was killed defending Vask Threnarr against a "
        "raiding incursion, at 67,400 years old;",
        "Selene (her mother) raised her and remained at her side until "
        "Selene was killed defending Vask Threnarr against a raiding "
        "incursion roughly 28 years before Lauris's departure (Lauris age "
        "~3,972, MCD-174/MCD-1686), at roughly 42,200 years old (38,200 "
        "at conception, MCD-162);",
    ),
    # B12
    (
        "MCD-163",
        "didn't become visible until her first anomalous density reading "
        "roughly 1,400 years later.",
        "didn't become visible until her first anomalous density reading "
        "at age 14 (2,800x, double the cohort ceiling, MCD-166).",
    ),
    # B13
    (
        "MCD-171",
        "Lauris's first lethal combat came at age 1,247:",
        "Lauris's first life-threatening deployment came at age 1,247:",
    ),
    # B14
    (
        "MCD-208",
        "confirmed the Talisman had been autonomously running Stage 2 for "
        "roughly three centuries,",
        "confirmed the Talisman had been autonomously running Stage 2 for "
        "roughly two centuries at that point (three by Book 1's present, "
        "MCD-142),",
    ),
    # B15
    (
        "MCD-201",
        "the reservation survived his death and every wielder transition "
        "since, until Lauris claimed it.",
        "the reservation survived every wielder transition since, until "
        "Lauris claimed it.",
    ),
    # B16
    (
        "MCD-309",
        "it is deliberately NOT extended to assert anything about Haku the "
        "Unifier's own fate, which stays unaddressed and open.",
        "it is deliberately NOT extended to assert anything about Haku the "
        "Unifier's own fate, which was subsequently resolved separately at "
        "MCD-314 (alive; narrative reveal reserved).",
    ),
    # B17
    (
        "MCD-338",
        "Exact book placement and full chapter content remain undrafted, "
        "reserved for a future dedicated pass.",
        "Both chapters have since been drafted and locked (Batch 297): the "
        "Ever-Haunt interstitial sits between Book 1 and Book 2 "
        "(MCD-1621), the Painter interstitial between Book 2 and Book 3 "
        "(MCD-1622).",
    ),
    # B18
    (
        "MCD-256",
        "the Century Mark marks the Talisman of Mao's first explicit "
        "transition from Stage 1 toward Stage 2.",
        "the Century Mark marks the first transition from Stage 1 toward "
        "Stage 2 that Kanja himself perceives (Grounded Bastion had "
        "already been running autonomously without his knowledge, "
        "MCD-142/MCD-208/MCD-252).",
    ),
    # B19
    (
        "MCD-312",
        "twelve raiders driven through forty warships in arrowhead "
        "formation, twice",
        "twenty-two raiders driven through forty warships in arrowhead "
        "formation, twice (the 22-ship arrowhead of MCD-242)",
    ),
    # B20
    (
        "MCD-230",
        "the Industrial Myth (21, first iteration, Furnace District "
        "Strike), the Blue-Collar Titan (20, Sewer War of Killane)",
        "the Blue-Collar Titan (20, Sewer War of Killane), the Industrial "
        "Myth (21, first iteration, Furnace District Strike)",
    ),
    # B21
    (
        "MCD-235",
        "The Audit (the Trust capital ship captured at Iron Shallows)",
        "The Audit (the Trust escort warship captured at Iron Shallows, "
        "MCD-285)",
    ),
    # B22
    (
        "MCD-257",
        "into a pocket the size of a tennis ball",
        "into a pocket the size of a man's fist",
    ),
    # B23
    (
        "MCD-258",
        "unintentionally filmed by the Trust's own propaganda crew and "
        "later leaked as Scourge recruitment material",
        "unintentionally recorded in full by the Trust's own propaganda "
        "chroniclers (sketch-artists and scribes) and later leaked as "
        "Scourge recruitment material",
    ),
    # B24 (MCD-275 half)
    (
        "MCD-275",
        "(Krael III, per MCD-277)",
        "(Krael III, per MCD-254)",
    ),
    # B24 (MCD-277 half)
    (
        "MCD-277",
        "per the genealogy resolved at MCD-254/MCD-275",
        "per the genealogy locked at MCD-254",
    ),
]

# B24 (MCD-254 half): an appended sentence rather than a fragment swap.
MCD_254_APPEND = (
    " The Krael name across the Long Mask is a three-generation Sovereign "
    "Trust naval dynasty descending from Admiral Dessius Krael of the Gale "
    "Straits (MCD-242): Dessius Krael II (active around Kanja's age 100) "
    "and Krael III (ages 222 and 298, MCD-275/MCD-277), a deliberate "
    "dynasty rather than a coincidental homonym."
)

# B1: MCD-139 status + append.
MCD_139_APPEND = (
    " Superseded by MCD-140 (Batch 28): the Avatar count is 19, not 16; "
    "WC-014 corrected to match."
)

# B4: MCD-103 status + append.
MCD_103_APPEND = (
    " Resolved Batch 69 (OPEN-005): 'Session Lock 2' never existed as a "
    "standalone document; the operative combat-tier ranking is the "
    "density-tier table locked at WC-024/WC-003."
)

# C1: uppercase LOCKED -> locked (plain cases).
C1_PLAIN_IDS = [
    "MCD-001", "MCD-002", "MCD-003", "MCD-004", "MCD-005", "MCD-010",
    "MCD-011", "MCD-012", "MCD-013", "MCD-020", "MCD-021", "MCD-022",
    "MCD-023", "MCD-024", "MCD-025", "MCD-026", "MCD-030", "MCD-031",
    "MCD-032", "MCD-033", "MCD-034", "MCD-040", "MCD-041", "MCD-050",
    "MCD-052", "MCD-060", "MCD-061", "MCD-070", "MCD-080", "MCD-081",
    "MCD-082", "MCD-083", "MCD-084", "MCD-085", "MCD-090", "MCD-091",
    "MCD-092", "MCD-093", "MCD-094", "MCD-095", "MCD-096", "MCD-097",
    "MCD-098", "MCD-099", "MCD-100", "MCD-102", "MCD-110", "MCD-111",
    "MCD-120", "MCD-121", "MCD-130",
]

# C1: composite statuses, normalized to "locked" with info preserved.
# MCD-051 and MCD-122's qualifier text is already fully reflected in their
# own statement prose (verified against live text), so no statement append
# is needed for either -- status field change only.
C1_COMPOSITE_TO_LOCKED = ["MCD-051", "MCD-122"]

# C1: MCD-112 composite status -> lowercase "flagged" (stays genuinely open;
# casing normalization only).
MCD_112_NEW_STATUS = "flagged"

# C2: null category -> character-pyro.
C2_IDS = ["MCD-131", "MCD-132", "MCD-133"]
C2_NEW_CATEGORY = "character-pyro"

# C3: territory-Chronicle category drift -> phase2-territory-chronicle.
C3_FROM_WORLD_MECHANICS = [
    "MCD-334", "MCD-335", "MCD-336", "MCD-337", "MCD-339", "MCD-340",
    "MCD-341", "MCD-342", "MCD-343", "MCD-344", "MCD-345", "MCD-351",
    "MCD-352", "MCD-353", "MCD-354", "MCD-355",
]
C3_FROM_HOMAGE_CHRONICLE = [
    "MCD-356", "MCD-357", "MCD-358", "MCD-361", "MCD-362", "MCD-363",
    "MCD-364",
]
C3_TARGET_CATEGORY = "phase2-territory-chronicle"
C3_EXTRA_CHECK_IDS = ["MCD-1024", "MCD-1093"]  # should already be correct


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}

    # --- Statement fragment fixes (B2, B3, B6, B7-B24 minus B1/B4/B5) ----
    statement_fixed = []
    skipped_already_fixed = []
    for rid, old_frag, new_frag in FRAGMENT_FIXES:
        assert rid in rules_by_id, f"missing rule {rid}"
        stmt = rules_by_id[rid]["statement"]
        if new_frag in stmt and old_frag not in stmt:
            skipped_already_fixed.append(f"{rid} (fragment)")
            continue
        count = stmt.count(old_frag)
        assert count == 1, (
            f"{rid}: expected exactly 1 occurrence of fragment, found "
            f"{count}: {old_frag!r}"
        )
        rules_by_id[rid]["statement"] = stmt.replace(old_frag, new_frag, 1)
        statement_fixed.append(rid)

    # --- B1: MCD-139 ------------------------------------------------------
    r = rules_by_id["MCD-139"]
    if "Superseded by MCD-140" not in r["statement"]:
        assert r["status"] == "locked", f"MCD-139 unexpected status {r['status']!r}"
        r["statement"] = r["statement"] + MCD_139_APPEND
        r["status"] = "superseded"
        statement_fixed.append("MCD-139")
    else:
        skipped_already_fixed.append("MCD-139 (B1)")

    # --- B4: MCD-103 -------------------------------------------------------
    r = rules_by_id["MCD-103"]
    if "Resolved Batch 69 (OPEN-005)" not in r["statement"]:
        r["statement"] = r["statement"] + MCD_103_APPEND
        r["status"] = "superseded"
        statement_fixed.append("MCD-103")
    else:
        skipped_already_fixed.append("MCD-103 (B4)")

    # --- B5: MCD-101 (status only) -----------------------------------------
    r = rules_by_id["MCD-101"]
    status_fixed = []
    if r["status"] != "locked":
        r["status"] = "locked"
        status_fixed.append("MCD-101")
    else:
        skipped_already_fixed.append("MCD-101 (B5, status already locked)")

    # --- B3: MCD-034 note field removal -------------------------------------
    r = rules_by_id["MCD-034"]
    note_removed = False
    if "note" in r:
        del r["note"]
        note_removed = True

    # --- B24: MCD-254 append -------------------------------------------------
    r = rules_by_id["MCD-254"]
    if "three-generation Sovereign Trust naval dynasty" not in r["statement"]:
        r["statement"] = r["statement"] + MCD_254_APPEND
        statement_fixed.append("MCD-254")
    else:
        skipped_already_fixed.append("MCD-254 (B24 append)")

    # --- C1: plain uppercase LOCKED -> locked -------------------------------
    for rid in C1_PLAIN_IDS:
        assert rid in rules_by_id, f"missing rule {rid}"
        if rules_by_id[rid]["status"] == "LOCKED":
            rules_by_id[rid]["status"] = "locked"
            status_fixed.append(rid)
        else:
            skipped_already_fixed.append(f"{rid} (C1, status={rules_by_id[rid]['status']!r})")

    # --- C1: composite statuses -> locked -----------------------------------
    for rid in C1_COMPOSITE_TO_LOCKED:
        assert rid in rules_by_id, f"missing rule {rid}"
        cur = rules_by_id[rid]["status"]
        if cur != "locked":
            rules_by_id[rid]["status"] = "locked"
            status_fixed.append(rid)
        else:
            skipped_already_fixed.append(f"{rid} (C1 composite, already locked)")

    # --- C1: MCD-112 FLAGGED -> flagged -------------------------------------
    r = rules_by_id["MCD-112"]
    if r["status"] != MCD_112_NEW_STATUS:
        r["status"] = MCD_112_NEW_STATUS
        status_fixed.append("MCD-112")
    else:
        skipped_already_fixed.append("MCD-112 (C1, already flagged)")

    # --- C2: null category -> character-pyro --------------------------------
    category_fixed = []
    for rid in C2_IDS:
        assert rid in rules_by_id, f"missing rule {rid}"
        if rules_by_id[rid].get("category") is None:
            rules_by_id[rid]["category"] = C2_NEW_CATEGORY
            category_fixed.append(rid)
        else:
            skipped_already_fixed.append(f"{rid} (C2, category={rules_by_id[rid].get('category')!r})")

    # --- C3: territory-Chronicle category drift -----------------------------
    for rid in C3_FROM_WORLD_MECHANICS:
        assert rid in rules_by_id, f"missing rule {rid}"
        cur = rules_by_id[rid].get("category")
        if cur == "World Mechanics":
            rules_by_id[rid]["category"] = C3_TARGET_CATEGORY
            category_fixed.append(rid)
        else:
            skipped_already_fixed.append(f"{rid} (C3, category={cur!r})")

    for rid in C3_FROM_HOMAGE_CHRONICLE:
        assert rid in rules_by_id, f"missing rule {rid}"
        cur = rules_by_id[rid].get("category")
        if cur == "phase2-homage-chronicle":
            rules_by_id[rid]["category"] = C3_TARGET_CATEGORY
            category_fixed.append(rid)
        else:
            skipped_already_fixed.append(f"{rid} (C3, category={cur!r})")

    # Sanity check: MCD-1024 / MCD-1093 should already be correct; confirm
    # and skip rather than touch (not in scope, verified not needing a fix).
    for rid in C3_EXTRA_CHECK_IDS:
        assert rid in rules_by_id, f"missing rule {rid}"
        cur = rules_by_id[rid].get("category")
        if cur == C3_TARGET_CATEGORY:
            skipped_already_fixed.append(f"{rid} (C3 extra-check, already correct)")
        else:
            # Would need attention but is explicitly out of this batch's
            # described scope beyond confirmation; leave untouched and flag.
            skipped_already_fixed.append(
                f"{rid} (C3 extra-check, UNEXPECTED category {cur!r}, left untouched)"
            )

    # Do NOT touch MCD-338's category (confirmed "World Mechanics" is
    # correct there -- an interstitial-chapter structural decision, not a
    # territory Chronicle).
    assert rules_by_id["MCD-338"]["category"] == "World Mechanics"

    # --- Collision / integrity checks ---------------------------------------
    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule IDs found"

    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({
        "batch": next_batch,
        "date": str(date.today()),
        "source": SOURCE,
        "rules_affected": len(set(statement_fixed)) + len(set(status_fixed)) + len(set(category_fixed)),
        "note": (
            "Mechanical-fix subset of a Fable-model read-only review of "
            "MCD-001 through MCD-450. Statement fixes: MCD-139 (superseded "
            "by MCD-140's Avatar-count correction), MCD-050 (Division 5's "
            "function resolved per MCD-135), MCD-034 (two artifacts -> "
            "three named per ARS-361, stale 'Session Lock 2' note "
            "removed), MCD-103 (superseded -- Session Lock 2 never "
            "existed, OPEN-005), MCD-110 (Maw-7 Slab corrected to the "
            "Throat per the Batch 103 GEO-003 correction), MCD-084 "
            "(clarified his parents, not Red Beard, were executed at the "
            "Slab of Judgment/Maw-7), MCD-209 (Lauris's age 4,000->6,000 "
            "per MCD-1533; Orlok's post-enlightenment figure 30,000x-"
            ">20,000x per MCD-096/CC-058), MCD-214 (age-ratio twelve-"
            ">nineteen times recomputed off her corrected age; Val "
            "Saeryn's citation MCD-155->MCD-101/MCD-149, MCD-155 being "
            "about an unrelated character), MCD-217 (age/lifespan-"
            "remaining recomputed off her corrected 6,000-year age, "
            "citation MCD-148->MCD-149), MCD-156 (birth-date recomputed; "
            "Selene's death re-dated to ~28 years before Lauris's "
            "departure per MCD-174/MCD-1686, replacing a stale '1,400 "
            "years into her life' figure MCD-172 already contradicts, "
            "and her age at death recomputed from her age at conception, "
            "MCD-162), MCD-163 (the density-reading-gap figure corrected "
            "to age 14/2,800x per MCD-166), MCD-171 ('first lethal "
            "combat' reworded to 'first life-threatening deployment,' "
            "no opponent in that scene), MCD-208 (the Stage-2 autonomous-"
            "running duration clarified as two centuries at that point in "
            "the narrative, three by Book 1's present per MCD-142), "
            "MCD-201 (dropped an assertion of Yuto Haku's death, which "
            "MCD-314 already locks as false -- he's alive), MCD-309 "
            "(updated its own forward reference now that MCD-314 has "
            "resolved Haku's fate as alive), MCD-338 (recorded that both "
            "interstitial chapters have since been drafted and locked at "
            "MCD-1621/MCD-1622, Batch 297), MCD-256 (clarified the "
            "Century Mark as the first Stage-1-to-2 transition Kanja "
            "himself perceives, not the Talisman's actual first "
            "transition, which MCD-142/208/252 already show ran "
            "autonomously earlier), MCD-312 (ship count twelve->twenty-"
            "two to match the already-locked 22-ship arrowhead at "
            "MCD-242/MCD-392), MCD-230 (swapped the Blue-Collar Titan/"
            "Industrial Myth list order to match their own stated ages, "
            "20 before 21), MCD-235 (The Audit reframed from 'capital "
            "ship' to 'escort warship' per MCD-285), MCD-257 (a real-"
            "world-object leak, 'tennis ball' -> 'a man's fist'), "
            "MCD-258 (a tech-level anachronism -- this world has no "
            "cameras/film -- 'filmed' -> 'recorded in full by... sketch-"
            "artists and scribes'), and MCD-275/MCD-277/MCD-254 (a "
            "circular-citation chain fixed: MCD-254 now carries the "
            "actual Krael three-generation-dynasty genealogy text that "
            "both MCD-275 and MCD-277 point to, and both of their own "
            "citations corrected to point at MCD-254 directly rather "
            "than at each other). 'B25' from the original review was "
            "confirmed already fixed in an earlier batch (MCD-1720 "
            "already cites ARS-344) and not reapplied. Metadata: 52 "
            "rules' uppercase 'LOCKED' status normalized to lowercase "
            "'locked' (C1), MCD-051/MCD-122's composite statuses "
            "normalized to 'locked' with their qualifier information "
            "already present in their own statement prose, MCD-112's "
            "'FLAGGED' normalized to lowercase 'flagged' (a genuinely "
            "open item, left open), MCD-131/132/133's null category set "
            "to 'character-pyro' matching MCD-022 (C2), and 23 rules' "
            "stale 'World Mechanics'/'phase2-homage-chronicle' category "
            "tags normalized to the corpus-wide convention "
            "'phase2-territory-chronicle' (C3; MCD-338 deliberately left "
            "at 'World Mechanics', a structural rule rather than a "
            "territory Chronicle; MCD-1024/MCD-1093 confirmed already "
            "correct and left untouched). Deliberately NOT touched: "
            "Section A of the review (the 296-vs-284-year Fulfillment "
            "Ceremony timing question, the Kares Prime timeline "
            "arithmetic, Lauris/Fermand's joining dates, Haryn Dael's "
            "age vs the Moonvault's age, Nadea Thren's champion-seat "
            "history, Valen's join-date/surname, the first-Verehimu "
            "contradiction, 'Yuto Haku' naming, the adulthood-phase "
            "arithmetic for the Kareth sisters, and the lower-priority "
            "A12 tensions) -- all left exactly as-is, reserved for "
            "Abad's own direct ruling."
        ),
    })

    old_version = float(ledger["ledger_version"])
    ledger["ledger_version"] = str(round(old_version + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    ids_final = [r["id"] for r in ledger["rules"]]
    dup_ok = len(ids_final) == len(set(ids_final))

    print(
        f"OK: {len(ledger['rules'])} total rules, "
        f"{len(ledger['batches_completed'])} batches, "
        f"ledger_version {ledger['ledger_version']}, "
        f"zero duplicate IDs: {dup_ok}.\n"
        f"Statements amended ({len(set(statement_fixed))}): "
        f"{sorted(set(statement_fixed))}\n"
        f"Status fields normalized ({len(set(status_fixed))}): "
        f"{sorted(set(status_fixed))}\n"
        f"Category fields normalized ({len(set(category_fixed))}): "
        f"{sorted(set(category_fixed))}\n"
        f"Note field removed from MCD-034: {note_removed}\n"
        f"Skipped (already fixed / confirmed correct) "
        f"({len(skipped_already_fixed)}): {skipped_already_fixed}"
    )


if __name__ == "__main__":
    main()
