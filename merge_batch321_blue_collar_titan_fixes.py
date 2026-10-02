#!/usr/bin/env python3
"""Batch 321: reconciliation corrections surfaced by the fable-review pass on the Blue-Collar Titan
Alias Chronicle corpus. Locks one new reconciliation rule (the Killane campaign timeline, matching
the project's own MAW-066 precedent) and amends five already-locked rule statements to match the
corrected Chronicle prose: MCD-1459's statement (a lingering she/her reference missed by the Batch
320 sweep, now reconciled to he/him matching CC-158), MCD-680's "the one death" -> "the deaths"
phrasing, and MCD-1198's ceasefire attribution reworded to describe the Killane campaign's own
open-phase ceasefire rather than attributing a formal "ceasefire" directly to MCD-234. No new
creative facts beyond the single reconciliation rule -- pure reconciliation against already-locked
canon, matching the Batch 226/68/320 precedent."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Fable-review pass (Blue-Collar Titan Alias Chronicle corpus), reconciliation pass, 2026-10-02"

with open(LEDGER_PATH) as f:
    ledger = json.load(f)

rules_by_id = {r["id"]: r for r in ledger["rules"]}

# --- New reconciliation rule: the Killane campaign timeline (next unused MCD- ID) ---
NEW_RULES = [
    {
        "id": "MCD-1877",
        "category": "world-timeline",
        "statement": (
            "The Sewer War of Killane campaign timeline, reconciled (matching the project's own "
            "MAW-066 precedent): MCD-234's \"80-fighter, six-week infiltration\" is the opening "
            "COVERT phase of a longer Killane underground campaign -- the phase during which the "
            "Southern District's Scrip-Registry ledger is copied undetected and the garrison is "
            "diverted chasing sabotaged infrastructure. It is followed by a longer OPEN phase, in "
            "which the Blue-Collar Titan alias operates visibly across the district (institution-"
            "building, guild relations, hazard response, and the wage-justice and other labor "
            "disputes documented across the alias's own Chronicle run), ending in a negotiated "
            "local ceasefire specific to the Killane theater -- distinct from the Rebellion's own "
            "eventual age-30 Trinity surrender (MCD-246). Both phases fall within ages 20-21, since "
            "the Siege of the Ghost Harbor (age 21) is already locked as following the Killane "
            "theater. This resolves an apparent drift across the Blue-Collar Titan Alias Chronicle "
            "corpus, in which later-written entries variously describe the campaign in week-scale, "
            "month-scale, and (erroneously) year-or-decade-scale terms, as a two-phase campaign "
            "rather than a contradiction. Any reference across this alias's Chronicle corpus to a "
            "\"resistance command\" or \"command relay\" standing above Kanja refers to the "
            "Rebellion's own senior-crew/allied-cells council -- Kanja's own crew plus independent "
            "allied cells coordinating as peers -- never a superior hierarchy he formally answers "
            "to, consistent with his established command-autonomy throughout the Rebellion era."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

existing_ids = set(rules_by_id.keys())
for r in NEW_RULES:
    assert r["id"] not in existing_ids, f"ID collision: {r['id']}"
    ledger["rules"].append(r)

# --- Amend existing rule statements to match the corrected Chronicle prose ---

# E1: MCD-1459's statement still used she/her for Corren Halst even though the file itself was
# already fixed in Batch 320.
rules_by_id["MCD-1459"]["statement"] = (
    "\"The Rotation Corren Halst Finally Took\" (full narrative text at "
    "docs/lords-of-cian/chronicles/the-rotation-corren-halst-finally-took.md), Blue-Collar Titan "
    "Alias Chronicle CII, wave 34, closing the wave. The alias's first graceful institutional "
    "handoff extended to a founding crew member rather than to Kanja himself -- mirroring his own "
    "declined permanent workers'-council seat (MCD-1183) -- as Corren Halst's long-standing "
    "dock-era leg injury forces him off front-line ladder rotation and into leading the crew's "
    "training hall instead, his expertise redirected rather than retired. Distinct from the "
    "aging/mortality registers applied to secondary figures (MCD-1185). Reuses already-locked crew "
    "members Corren Halst and Danne Sok (both he/him per the Batch 320 reconciliation, CC-158/159). "
    "No new named characters. Closes wave 34 (with MCD-1457 and MCD-1458) and this run's "
    "three-wave arc (waves 32-34). Corrected Batch 321, 2026-10-02: statement's remaining she/her "
    "references fixed to he/him (missed by the Batch 320 sweep); \"eight decades\" corrected to "
    "\"a decade\" in the file's own dialogue, since this alias has no Long Mask counterpart."
)

# C4: MCD-680's statement -- "the one death" implies a single death, but later-set-but-earlier-
# written entries (MCD-893, MCD-1070, MCD-1192) establish further deaths across the campaign.
rules_by_id["MCD-680"]["statement"] = (
    "\"What Garren Hask Wrote in the Margins\" (full narrative text at "
    "docs/lords-of-cian/chronicles/what-garren-hask-wrote-in-the-margins.md), The Blue-Collar "
    "Titan Alias Chronicle XLV, wave 15 of ten (waves 6-15). Garren Hask's closing cost-accounting "
    "ledger tallies the alias's true toll, failures included, as a grounding counterweight to the "
    "legend, closing the ten-wave run. Corrected Batch 321, 2026-10-02: \"the one death\" corrected "
    "to \"the deaths\" -- later-set-but-earlier-written entries (MCD-893, MCD-1070, MCD-1192) "
    "establish further deaths across the Killane campaign beyond the loss recorded at MCD-656."
)

# C1: MCD-1198's statement -- stop attributing a formal "ceasefire" directly to MCD-234; describe
# it as the Killane campaign's own open-phase ceasefire, per the new reconciliation rule (MCD-1877).
rules_by_id["MCD-1198"]["statement"] = (
    "\"The Last Reading Before the Peace\" (full narrative text at "
    "docs/lords-of-cian/chronicles/the-last-reading-before-the-peace.md), Blue-Collar Titan Alias "
    "Chronicle LXXXVII, wave 29, closing the wave. Set at the literal moment the Killane campaign's "
    "own open-phase ceasefire (MCD-1877) takes effect: Kanja performs one final full structural "
    "certification of the entire tunnel network, confirming the eastern gallery from MCD-485 has "
    "settled stable, closing the alias's central historical anchor, first opened at MCD-234. Reuses "
    "already-locked crew member Corren Halst. No new named characters. Closes wave 29. Corrected "
    "Batch 321, 2026-10-02: no longer attributes a formal \"ceasefire\" directly to MCD-234 (which "
    "locks only the six-week covert phase); reframed as the longer campaign's own open-phase "
    "ceasefire per the new reconciliation rule, MCD-1877. Numeric prose in the file itself also "
    "fixed for internal timeline consistency (\"years back\" x2, \"two decades of later stress\" -> "
    "\"months\"); a writers'-room \"since its first Chronicle\" phrase and an in-world use of "
    "another entry's own title reworded to plain prose."
)

ledger["batches_completed"].append({
    "batch": 321,
    "date": str(date.today()),
    "source": SOURCE,
    "rule_count": len(NEW_RULES),
    "note": (
        "Reconciliation pass following a fable-review of the Blue-Collar Titan Alias Chronicle "
        "corpus (102 entries), matching the pilot-review precedent established on the Bane corpus "
        "(Batch 320). Locked one new reconciliation rule (MCD-1877), matching the project's own "
        "MAW-066 precedent: the Sewer War of Killane campaign (MCD-234's six-week covert phase, "
        "within ages 20-21) is reconciled as the opening phase of a longer Killane underground "
        "campaign, followed by an open phase ending in a negotiated local ceasefire specific to "
        "that theater, and any 'resistance command'/'command relay' reference above Kanja across "
        "this alias's corpus is clarified as the Rebellion's own senior-crew/allied-cells council, "
        "never a superior hierarchy he answers to. Corrected across the Chronicle files themselves "
        "(prose and header notes, not run through this script): numeric drift fixed in MCD-1035, "
        "MCD-1070 (left as-is, already consistent), MCD-1192, and MCD-1198; a Rolling Foundry "
        "Campaign era-mismatch removed from MCD-408/409 (a different alias's later age-27 era "
        "leaking into this alias's age-20/21 window); Kanja's stated tenure corrected to fit the "
        "Rebellion-era window (full-Trinity entries can't exceed age 30) in MCD-1400 and MCD-1459; "
        "a death-toll inconsistency fixed in MCD-680 (\"the one death\" -> \"the deaths\"); two "
        "mis-aged headers corrected to \"post-Killane\" in MCD-487 and MCD-539; a misused Onyx "
        "power (Cadence Ruin reattributed to Mafesto's kinetic transfer) and an Obsidian Malice "
        "materials/shape error (\"point-first\" -> \"head-first\") fixed in MCD-1175; an impossible "
        "onlooker detail fixed in MCD-653 (MCD-374 establishes Kanja surfaced alone); five she/her "
        "references for Danne Sok corrected to he/him in MCD-1201 (missed by the Batch 320 sweep, "
        "matching CC-159); eight writers'-room leaks (Chronicle-count/wave/Chronicle-title "
        "references) reworded to in-world phrasing across MCD-1068, MCD-1177, MCD-1198, MCD-1187, "
        "MCD-1199, MCD-1200, MCD-1201, and MCD-1402; Obsidian Malice mischaracterized as bladed or "
        "sheathed fixed in MCD-1068, MCD-1178 (also a materials slip -- it is Mao-forged Drakma, "
        "not an iron-alloy blade), and MCD-666 (\"cutting tool\" -> \"breaking bar\"); the stale "
        "Chronicle-count tracker figure corrected from 93 to 102 in chronicle-tracks-status.md; a "
        "wrong citation fixed in MCD-656 (MCD-538 -> the actual structural-failure entry, MCD-485); "
        "MCD-1192's origin reference corrected to MCD-1012 (the cellar breach, Efa Gol's actual "
        "first appearance); an unnamed recurring crew chief's gender flip resolved he/him "
        "(matching MCD-652) in MCD-1005; citations fixed in MCD-440 and MCD-442 (both now correctly "
        "cite MCD-440 as the non-visual-sensory-principle origin rather than MCD-374) and MCD-539 "
        "(MCD-665 added to its existing citation list); a numeric conflict resolved in MCD-662 "
        "('joined six weeks earlier' vs. the entry's own 'fifth week of the siege' framing); and "
        "inverted Obsidian Malice charge phrasing fixed in MCD-486 ('not yet fully spent' -> 'not "
        "yet fully recharged') and MCD-1011 ('charged and ready' reworded to reflect that the "
        "relic draws its reserve from Mafesto's gathered kinetic energy rather than functioning as "
        "a standalone pre-chargeable battery). This script applies only the rule-statement-level "
        "amendments (MCD-1459, MCD-680, MCD-1198) and the new reconciliation rule (MCD-1877); every "
        "other fix above was applied directly to the Chronicle files' prose and header notes, "
        "outside this script's scope. Pure reconciliation throughout -- no new creative facts "
        "beyond the single reconciliation rule, matching the Batch 226/68/320 precedent."
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
