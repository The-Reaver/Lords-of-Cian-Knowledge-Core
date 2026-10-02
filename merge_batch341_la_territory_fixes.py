#!/usr/bin/env python3
"""Batch 341: Fable-review fixes for the Los Angeles homage-era Territory Chronicles
(Sankofa, Aztlan, Atunbi, Ijoko, Orin).

Applies the subset of a Fable-model read-only review's findings that are pure
mechanical reconciliation/renaming -- prose-level Chronicle-file corrections
(timeline fixes, tech-level anachronisms, writers'-room leaks, a real-world
proper-noun leak, a grammar fix, a dropped-word fix) plus two statement
amendments (MCD-1025, MCD-1092) whose prose quoted the renamed characters, plus
a category-field normalization pass on 10 rules still carrying stale category
values from before the "phase2-territory-chronicle" convention was adopted.

One item (C3, Orin Chronicle I's phonograph-recording scene mechanism) and all
ENRICHMENT-cluster findings are deliberately NOT applied here -- they change a
locked scene's actual mechanism or add new creative material, not just reconcile
existing text, and remain queued for Abad's own review.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Fable-model read-only review of the Los Angeles homage-era Territory "
    "Chronicles (Sankofa, Aztlan, Atunbi, Ijoko, Orin) against the full ledger "
    "and corpus, implemented by this session."
)

# Rule-statement amendments: prose fixes whose narrative-file renames (Yao ->
# Mensah, Babatunde -> Adebayo) are quoted directly in the rule's own statement
# text.
AMENDMENTS = {
    "MCD-1025": (
        "Sankofa Chronicle V, \"What Tradecraft Gave Away\" (full narrative text at "
        "docs/lords-of-cian/chronicles/sankofa-chronicle-v-what-tradecraft-gave-away.md), "
        "the fifth Sankofa territory Chronicle and the third to touch the forged-letter/"
        "pamphlet conspiracy from Chronicles II and IV (MCD-360, MCD-1023). Protagonist "
        "Baale (PH2-021), not a Kanja Chronicle. Per the pacing agreed in Batch 225: the "
        "deliberate 'crack' entry, escalating the conspiracy from information warfare to "
        "a direct assassination attempt -- its first real risk of exposure -- without "
        "resolving the mystery. A hired direct attacker, Mensah (a new named character, "
        "Akan Thursday-born day-name per the standing PH2 naming convention, zero prior "
        "collisions), attacks Baale face to face at dusk; he survives the exchange and is "
        "bound to serve Baale per 'The Turn,' exactly matching the ability's mechanic. A "
        "second operative, positioned on a rooftop specifically to kill Baale by means "
        "that don't require him to survive a direct exchange (defeating the ability's own "
        "condition), has cold feet at the last second and flees without firing, left "
        "deliberately unidentified. Mensah's unprompted account of his own dead-drop "
        "recruitment -- instructions folded in a distinctive three-corner tucked fold -- "
        "matches exactly the never-publicized fold used in the COINTELPRO-era forged "
        "letters from PH2-021's own backstory near-death event, proving the current "
        "conspiracy is run by, or was taught directly by, someone from the original "
        "campaign who was never caught the first time. Deliberately does not reveal an "
        "author or name; the reveal is reserved for a future entry, per Abad's explicit "
        "pacing instruction. Kra and Kojo (both already locked) reused; no other named "
        "characters. Kanja does not appear in this entry at all -- a deliberate departure "
        "from every prior Sankofa Chronicle, judged too private and personal a moment even "
        "for an unnamed witness."
    ),
    "MCD-1092": (
        "Sankofa Chronicle VI, \"The Hand That Wrote the First Letter\" (full narrative "
        "text at docs/lords-of-cian/chronicles/sankofa-chronicle-vi-the-hand-that-wrote-"
        "the-first-letter.md), the sixth Sankofa territory Chronicle and the reveal to the "
        "forged-letter/pamphlet conspiracy from Chronicles II, IV, and V "
        "(MCD-360/MCD-1023/MCD-1025). Protagonist Baale (PH2-021), not a Kanja Chronicle. "
        "Over roughly a year, Mensah (bound via \"The Turn\" in Chronicle V) traces the "
        "dead-drop payment chain backward through its cutouts to a lease record naming the "
        "conspiracy's author: Adebayo (a new named character, Yoruba, zero prior "
        "collisions), a founding-era errand-runner/courier from Sankofa's earliest days -- "
        "recognized by Baale personally. Adebayo confesses to personally forging the "
        "original COINTELPRO-era letters that nearly killed Baale and Kra (PH2-021's "
        "backstory event) after being coerced by an unnamed counterintelligence operation; "
        "his decades of continued escalation (the private letter, the public pamphlets, "
        "the hired assassination attempt) are explained as a self-perpetuated, "
        "never-formally-closed assignment rather than an ongoing institutional program -- "
        "the apparatus itself is deliberately left unnamed even in resolution. Adebayo "
        "does not attack Baale at the confrontation, so \"The Turn\" is never triggered, "
        "honoring PH2-021's own stated mechanic precisely to the end: the ability has "
        "nothing to offer against a threat that simply stops rather than strikes. Baale "
        "resolves it through public exposure and naming rather than violence or captivity, "
        "consistent with his established restraint (Chronicle III's clinic, Chronicle IV's "
        "transparency). Kra, Kojo, and Mensah (all already locked) reused; no other named "
        "characters. Kanja does not appear in this entry, matching Chronicle V's "
        "precedent. Closes the six-entry forged-letter/pamphlet conspiracy arc."
    ),
}

# Category-field normalization: these 10 rules predate the
# "phase2-territory-chronicle" category convention (some still carry "World
# Mechanics" from their original batch, others "territory-chronicle" or
# "phase2-homage-chronicle") -- matching the MCD-365/MCD-1730 precedent for
# fixing category drift.
CATEGORY_FIXES = [
    "MCD-346", "MCD-347", "MCD-348", "MCD-349", "MCD-350",
    "MCD-359", "MCD-360", "MCD-1023", "MCD-1025", "MCD-1092",
]
TARGET_CATEGORY = "phase2-territory-chronicle"


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}

    amended = []
    for rid, new_statement in AMENDMENTS.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        rules_by_id[rid]["statement"] = new_statement
        amended.append(rid)

    recategorized = []
    for rid in CATEGORY_FIXES:
        assert rid in rules_by_id, f"missing rule {rid}"
        old_category = rules_by_id[rid].get("category")
        if old_category != TARGET_CATEGORY:
            rules_by_id[rid]["category"] = TARGET_CATEGORY
            recategorized.append((rid, old_category))

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule IDs found"

    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({
        "batch": next_batch,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": 0,
        "note": (
            "Fable-review fixes for the Los Angeles homage-era Territory Chronicles "
            "(Sankofa, Aztlan, Atunbi, Ijoko, Orin) -- mechanical/reconciliation subset "
            "only, applied directly. Amends MCD-1025 and MCD-1092's own statement text to "
            "match two renames made across their Chronicle files: Yao -> Mensah (resolves "
            "a near-collision with the already-locked 'Yaw,' Osei's brother/co-founder, "
            "PH2-053) and, in MCD-1092/Sankofa Chronicle VI only, Babatunde -> Adebayo "
            "(resolves a near-collision with the already-locked 'Tunde,' one of Arturo's "
            "dead dock-boy cohort members, MCD-361/MCD-1024). Also fixed, prose-only (no "
            "further ledger-statement change needed): Sankofa Chronicle V's internal "
            "timeline ('a decade of silence' -> 'three decades of silence,' matching "
            "Chronicle VI's own four separate 'thirty years' references), a Chronicle-"
            "numbering writers'-room leak ('three Chronicles before' -> 'a year before'), "
            "and a weapon clarified as a crossbow rather than an implied firearm (this "
            "world has none); Sankofa Chronicle IV's stale 'three months before' timeline "
            "figure brought into line with its own later, already-correct 'months before'; "
            "Sankofa Chronicle II's grammar error addressing Kojo alone as if two people; "
            "Aztlan Chronicle I's internal arithmetic error ('forty months of drilling' -> "
            "'six months,' matching the six-month figure stated twice elsewhere in the "
            "same Chronicle) and a writers'-room leak ('on a night this Chronicle does not "
            "cover' -> 'on a night still years away'); Aztlan Chronicle II's tech-level "
            "anachronism ('the cameras' -> 'the crowd and the broadsheet sketchers'); "
            "Atunbi Chronicle I's tech-level anachronism (a motor-vehicle 'truck' replaced "
            "throughout with a period-appropriate dray-team/sledges-and-drag-chain and the "
            "demolition crew itself) and a dropped-word prose glitch ('a fourth of new "
            "seedlings' -> 'a fresh row of new seedlings'); Ijoko Chronicle I's two "
            "tech-level anachronisms ('a spreadsheet' -> 'a ledger column'; 'the exit "
            "lights' -> 'the lamp left burning by the door'); and Orin Chronicle I's "
            "real-world proper-noun leak (a real jazz musician's name in dialogue, reworded "
            "to plain descriptive prose). Also normalizes category-field drift on 10 rules "
            "(MCD-346/347/348/349/350/359/360/1023/1025/1092) to the now-standard "
            "'phase2-territory-chronicle' value, matching the already-fixed MCD-365/"
            "MCD-1730 precedent. Deliberately NOT applied: C3 (Orin Chronicle I's "
            "phonograph-recording-mechanism anachronism), since it would change a locked "
            "scene's actual mechanism rather than reconcile existing text, and remains "
            "queued for Abad's own ruling; all ENRICHMENT-cluster findings; and EN5/EN6 "
            "(low-priority cosmetic items)."
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
        f"{len(recategorized)} rules recategorized to '{TARGET_CATEGORY}': "
        f"{recategorized}."
    )


if __name__ == "__main__":
    main()
