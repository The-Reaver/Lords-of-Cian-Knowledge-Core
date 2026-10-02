#!/usr/bin/env python3
"""Batch 321: reconciliation corrections surfaced by a read-only fable-review pass on the Iron
Bastard Alias Chronicle corpus (102 entries). Mechanical fixes (Trinity-era gear anachronisms in
waves 16-34, which fall years past the Trinity's age-30 surrender, `MCD-246`; an era-framing
contradiction treating "the Rebellion" as a still-live war in that same window; a garbled
mis-gendered line; a conflated recurring-general identity; a citation error; leaked rule-IDs and
writers'-room language in narrative prose; several false/misattributed in-world claims) plus two
pragmatic judgment calls matching the Batch 320 precedent: the second student's pronoun resolved
she/her (the majority usage across the corpus), and "the second student" of `MCD-719` rewritten as
a genuinely new, distinct trainee rather than a wrongly re-identified first student. No new
creative facts -- pure reconciliation against already-locked canon, matching the Batch 226/320
precedent. This script only amends existing rule statements; it adds no new rules.

NOTE: this script was prepared by a read-only review/fix-application pass and has NOT been run.
Run it from the repo root once reviewed: `python3 merge_batch321_iron_bastard_fixes.py`
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Fable-review pass (Iron Bastard Alias Chronicle corpus), reconciliation pass, 2026-10-02"

with open(LEDGER_PATH) as f:
    ledger = json.load(f)

rules_by_id = {r["id"]: r for r in ledger["rules"]}

# --- Amend rule statements to match the corrected Chronicle prose ---
AMENDMENTS = {
    # C1 -- Trinity-era gear anachronism, waves 16-34 (years past MCD-246's age-30 surrender).
    # The 9 statements that explicitly billed a "full-Trinity combat showcase."
    "MCD-1047": (
        '"The Pass Strung on Cable and Air" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-pass-strung-on-cable-and-air.md), The Iron Bastard "
        "Alias Chronicle LVIII, wave 20, first entry. A detailed combat showcase against a "
        "mountain-pass suspension crossing built on three cable-anchor towers, two of them "
        "deliberately slackened decoys; thin high-altitude air attenuates the resonance doctrine's "
        "reach for the first time, solved by closing to direct cable contact rather than reading "
        "from range. Doubled verification (established MCD-497) identifies the true load-bearing "
        "tower before the Ironhand Gauntlets collapse only that one, while the Forge-Coat and "
        "Ironfall Boots ground answering fire and the Rexmar Machete clears the near tower's melee "
        "crew. The second student (established MCD-719, she/her) appears in a supporting capacity. "
        "No new named characters. Corrected Batch 321, 2026-10-02: the original statement billed a "
        "'full-Trinity' showcase and named Obsidian Malice/Mafesto/Onyx directly, anachronistic for "
        "wave 20, which falls years past the Trinity's age-30 surrender (`MCD-246`); reworded to "
        "the Long-Mask-era kit."
    ),
    "MCD-1080": (
        '"The Fire That Changed What the Iron Said" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-fire-that-changed-what-the-iron-said.md), the Iron "
        "Bastard Alias Chronicle LXI, wave 21, first entry. A detailed combat showcase freeing "
        "caged prisoners from a deliberately fired granary at Vell's Landing: heat-driven thermal "
        "expansion changes the iron cages' resonance signature continuously as the fire burns, "
        "forcing Kanja to extend the standing doubled-verification protocol (MCD-497) from "
        "confirming a static tension into tracking its rate of change and projecting forward to "
        "the moment the locks fail on their own. The Ironhand Gauntlets strike in three short "
        "pulses walked down the cage row rather than one sustained broadcast, the Forge-Coat and "
        "Ironfall Boots redirect a roof collapse as leverage rather than absorbing it passively, "
        "and the Rexmar Machete clears a falling beam from the escape path. Nineteen of twenty "
        "prisoners escape; Kanja carries the twentieth out himself. Efa Gol (CC-130) runs a "
        "diversion; the second student (MCD-719) observes. No new named characters. Corrected "
        "Batch 321, 2026-10-02: the original statement billed a 'full-Trinity' showcase and named "
        "Obsidian Malice/Mafesto/Onyx directly, anachronistic for wave 21, years past the Trinity's "
        "age-30 surrender (`MCD-246`); reworded to the Long-Mask-era kit."
    ),
    "MCD-1284": (
        '"The Shell That Grew Around the Iron" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-shell-that-grew-around-the-iron.md), Iron Bastard Alias "
        "Chronicle LXV, wave 22. A detailed, battle-intense combat showcase against a bio-armored "
        "Crawler variant grown with cultivated estuary coral specifically to exploit the new "
        "living/dead diagnostic distinction (`MCD-1283`); Kanja resolves the ambiguity by "
        "recognizing the coral's uniform, seeded growth pattern lacks a genuinely living "
        "structure's self-directed branching, then drives the Ironhand Gauntlets into the resin "
        "bonding layer to crack the shells free before the Forge-Coat and Ironfall Boots and the "
        "Rexmar Machete and Smoke System clear five of six Crawlers. The second student (`MCD-719`) "
        "appears in supporting capacity. No new named characters. Corrected Batch 321, 2026-10-02: "
        "the original statement billed a 'full-Trinity' showcase and named Obsidian "
        "Malice/Mafesto/Onyx directly, anachronistic for wave 22, years past the Trinity's age-30 "
        "surrender (`MCD-246`); reworded to the Long-Mask-era kit."
    ),
    "MCD-1287": (
        '"Two Ears on the Same Bridge" (full narrative text at '
        "docs/lords-of-cian/chronicles/two-ears-on-the-same-bridge.md), Iron Bastard Alias "
        "Chronicle LXVIII, wave 23. A detailed, deliberately restrained diagnostic duel between "
        "Kanja and the Trust diagnostician (`MCD-1286`) -- Kanja wins not by out-hearing him but by "
        "refusing to trust his own verification pass and instead reading the deceiver's own "
        "stance, applying the ethical-restraint lesson of `MCD-499`. Zero structural damage and "
        "zero use of the Ironhand Gauntlets; the engagement resolves through the Smoke System and "
        "a grounded defensive block alone. No new named characters. Corrected Batch 321, "
        "2026-10-02: the original statement named Obsidian Malice directly, anachronistic for wave "
        "23, years past the Trinity's age-30 surrender (`MCD-246`); reworded to the Long-Mask-era "
        "kit."
    ),
    "MCD-1290": (
        '"Four Ears, One Night" (full narrative text at '
        "docs/lords-of-cian/chronicles/four-ears-one-night.md), Iron Bastard Alias Chronicle LXXI, "
        "wave 24. A detailed, battle-intense showcase scaling the doctrine's full teaching lineage "
        "-- Kanja, the first student (`MCD-499`), the second student (`MCD-719`, she/her), and the "
        "third-generation apprentice (`MCD-967`/`1289`) -- into independent parallel operation, "
        "each reading a separate structure across a contested river valley in one night ahead of a "
        "Directorate enforcement sweep. Kanja's own thread catches a falsified-signature deception "
        "(`MCD-550`) at a munitions depot via doubled verification and resolves it with the full "
        "Long-Mask-era kit; all four sites succeed without misdiagnosis. No new named characters. "
        "Corrected Batch 321, 2026-10-02: the original statement billed a 'full-Trinity' showcase "
        "and described 'a Directorate advance,' both anachronistic/era-inconsistent for wave 24, "
        "years past the Trinity's age-30 surrender and the Rebellion's own end (`MCD-245`/`246`); "
        "reworded accordingly."
    ),
    "MCD-1293": (
        '"The Method Turned Against Its Own Lesson" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-method-turned-against-its-own-lesson.md), Iron Bastard "
        "Alias Chronicle LXXIV, wave 25. The doctrine's darkest confrontation entry: Kanja "
        "confronts the rogue former cohort graduate (`MCD-1292`), who admits he understood the "
        "ethical teaching completely and deliberately rejected it for profit; resolved through "
        "restraint and a final honest warning rather than combat -- the Ironhand Gauntlets never "
        "strike -- distinct from the fatal-misdiagnosis arc (`MCD-497`/`727`/`728`) since this was "
        "a deliberate choice, not a diagnostic error. No new named characters. Corrected Batch 321, "
        "2026-10-02: the original statement named Obsidian Malice directly, anachronistic for wave "
        "25, years past the Trinity's age-30 surrender (`MCD-246`); reworded to the Long-Mask-era "
        "kit."
    ),
    "MCD-1296": (
        '"Six Buildings, One Set of Hands" (full narrative text at '
        "docs/lords-of-cian/chronicles/six-buildings-one-set-of-hands.md), Iron Bastard Alias "
        "Chronicle LXXVII, wave 26. A detailed, battle-intense rescue showcase: an unpredictable "
        "aftershock endangers six structures at once during the earthquake triage (`MCD-1295`), "
        "three with trapped occupants. The Ironhand Gauntlets clear targeted debris rather than "
        "structural tension directly, the Forge-Coat and Ironfall Boots continuously ground "
        "ongoing tremor through Kanja's own frame, and a compressed full sequence of the Rexmar "
        "Machete and the Smoke System saves all six buildings' occupants, though two of the six "
        "structures themselves are condemned. The second student (`MCD-719`) appears in supporting "
        "capacity. No new named characters. Corrected Batch 321, 2026-10-02: the original statement "
        "billed a 'full-Trinity' showcase and named Obsidian Malice/Mafesto/Onyx directly, "
        "anachronistic for wave 26, years past the Trinity's age-30 surrender (`MCD-246`); reworded "
        "to the Long-Mask-era kit."
    ),
    "MCD-1413": (
        '"The Mill That Turned Against Itself" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-mill-that-turned-against-itself.md), Iron Bastard Alias "
        "Chronicle XCII, wave 31. A detailed, battle-intense combat showcase: a war-engine is "
        "rigged into a running tide-mill's own drivetrain, camouflaged by the mill's legitimate "
        "rotational vibration rather than hidden or falsified; the Forge-Coat and Ironfall Boots, "
        "the Ironhand Gauntlets, and the Rexmar Machete are used together as a real-time "
        "baseline-and-isolation network to find the one beat that doesn't belong, extending the "
        "three-voice diagnostic method (`MCD-721`) to a continuously operating civilian structure "
        "for the first time. Doubled verification (`MCD-497`) and the standing-alone check "
        "(`MCD-1081`) both confirm before the strike; the device is severed without stopping the "
        "mill or damaging its gearwork. No new named characters. Corrected Batch 321, 2026-10-02: "
        "the original statement billed a 'full-Trinity' showcase and named Obsidian "
        "Malice/Mafesto/Onyx directly, anachronistic for wave 31, years past the Trinity's age-30 "
        "surrender (`MCD-246`); reworded to the Long-Mask-era kit."
    ),
    "MCD-1488": (
        '"What the Mountain Threw Down With Them" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-mountain-threw-down-with-them.md), Iron Bastard "
        "Alias Chronicle XCV, wave 32. A detailed, battle-intense combat showcase: raiders "
        "deliberately weaponize the exact geological fracture identified in `MCD-1487`, forcing "
        "Kanja to redirect an unstoppable rockfall's outcome away from the settlement rather than "
        "prevent or stop it, distinct from the no-enemy earthquake-triage entries "
        "(`MCD-1295`/`1296`) and every prior enemy-Crawler/structure engagement against a designed "
        "object rather than a natural formation. The Forge-Coat and Ironfall Boots absorb incoming "
        "fire, the Rexmar Machete and Kanja's own instinctive Rexmar-Mar sense clear the vanguard, "
        "and the Ironhand Gauntlets, confirmed by doubled verification (`MCD-497`) under extreme "
        "time pressure, redirect the rockfall's true weak point into an empty ravine. No new named "
        "characters. Corrected Batch 321, 2026-10-02: the original statement billed a "
        "'full-Trinity' showcase and named Obsidian Malice/Mafesto/Onyx directly, anachronistic "
        "for wave 32, years past the Trinity's age-30 surrender (`MCD-246`); reworded to the "
        "Long-Mask-era kit."
    ),
    "MCD-1491": (
        '"The Shaft That Was Built to Bury Them" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-shaft-that-was-built-to-bury-them.md), Iron Bastard "
        "Alias Chronicle XCVIII, wave 33. A detailed, battle-intense combat showcase: the "
        "doctrine's first application inside a fully confined underground mine shaft, combining "
        "close-quarters combat against an ambush left behind to prevent rescue with a high-stakes, "
        "echo-distorted structural read on multiple already-destabilized support timbers, distinct "
        "from the acoustically-deadened vault (`MCD-712`, doctrine defeated outright, no combat) "
        "since confinement here distorts rather than blocks the read, requiring direct "
        "hand-to-timber contact and doubled verification (`MCD-497`) on every beam. The Smoke "
        "System and the Rexmar Machete clear the ambush in confined quarters, and the Forge-Coat "
        "and Ironfall Boots redirect a melee strike into the tunnel wall. No new named characters. "
        "Corrected Batch 321, 2026-10-02: the original statement billed a 'full-Trinity' showcase "
        "and named Obsidian Malice/Mafesto/Onyx directly, anachronistic for wave 33, years past the "
        "Trinity's age-30 surrender (`MCD-246`); reworded to the Long-Mask-era kit."
    ),
    "MCD-1494": (
        '"The Bridge That Answered to the Current" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-bridge-that-answered-to-the-current.md), Iron Bastard "
        "Alias Chronicle CI, wave 34. A detailed, battle-intense combat showcase: the doctrine's "
        "first application to a structure whose tension baseline never holds still, a lashed "
        "pontoon river crossing that shifts continuously with current, distinct from fixed naval "
        "rigging (`MCD-498`) and a storm-strained but structurally static keel (`MCD-1305`), and "
        "from the living fig-root bridge's own slow biological cycle (`MCD-1283`). Extends the "
        "continuous-monitoring technique first developed for the keel read (`MCD-1305`) into "
        "real-time combat conditions for the first time. The Forge-Coat and Ironfall Boots absorb "
        "incoming fire, the Rexmar Machete steadies the crossing column, and the Ironhand "
        "Gauntlets are used constructively to reinforce a failing mooring lashing rather than "
        "destructively against a target. The second student (`MCD-719`, she/her) appears in "
        "supporting capacity. No new named characters. Corrected Batch 321, 2026-10-02: the "
        "original statement billed a 'full-Trinity' showcase and named Obsidian Malice/Mafesto/"
        "Onyx directly, anachronistic for wave 34, years past the Trinity's age-30 surrender "
        "(`MCD-246`); reworded to the Long-Mask-era kit."
    ),

    # C1 -- two further statements naming Obsidian Malice directly without the "full-Trinity"
    # phrase, fixed for the same reason and consistency with the corrected prose files.
    "MCD-1302": (
        '"One Read, Two Flags" (full narrative text at '
        "docs/lords-of-cian/chronicles/one-read-two-flags.md), Iron Bastard Alias Chronicle "
        "LXXXIII, wave 28. A detailed technical-and-political showcase: the aqueduct (`MCD-1301`) "
        "is found failing not from sabotage but from two independent, uncoordinated repair "
        "efforts by each faction working against each other's tension across years of contested "
        "control; both sides' engineers complete an eleven-day joint repair under Kanja's live "
        "diagnostic coordination, with the Ironhand Gauntlets used once, restrained, to clear a "
        "failed section. No new named characters. Corrected Batch 321, 2026-10-02: the original "
        "statement named an Obsidian Malice discharge directly, anachronistic for wave 28, years "
        "past the Trinity's age-30 surrender (`MCD-246`); reworded to the Long-Mask-era kit."
    ),

    # C2 -- era-framing contradiction ("the Rebellion" treated as a still-live war in wave 28).
    "MCD-1301": (
        '"The Bridge Neither Side Trusted Alone" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-bridge-neither-side-trusted-alone.md), Iron Bastard "
        "Alias Chronicle LXXXII, wave 28, first entry. The Directorate successor (`MCD-734`) "
        "requests the doctrine's first formal cross-faction joint engineering operation: a "
        "neutral structural assessment of a failing aqueduct spanning contested border territory, "
        "which neither the Trust nor the resistance network trusts the other's engineers to read "
        "honestly. Kanja agrees on condition both sides receive the identical account "
        "simultaneously, extending the general/successor thread from adversary through respect "
        "into active cooperation. No new named characters; the successor remains unnamed per "
        "`MCD-734`. Corrected Batch 321, 2026-10-02: 'the rebels' reworded to 'the resistance "
        "network,' since the Rebellion itself formally ends at `MCD-245`/`246`, years before wave "
        "28; and 'the shelved report' clarified elsewhere in the entry to mean the Directorate "
        "general's own career-ending report (`MCD-734`), not the Trust scholar's report "
        "(`MCD-421`)."
    ),

    # C5 -- Trust scholar's pronoun, majority is he/him (MCD-551/740/1307/1309/1412/1414).
    "MCD-421": (
        '"The Scholar Who Measured the Impossible" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-scholar-who-measured-the-impossible.md), Iron Bastard "
        "Alias Chronicle VI, closing the second wave. A Trust materials scholar's eleven-month "
        "honest study concludes the resonance phenomenon is applied physics, not a supernatural "
        "weapon, and that the only real defense (extreme structural redundancy) is prohibitively "
        "expensive; his accurate report is quietly shelved in favor of a politically comfortable "
        "explanation. No new named characters. Closes the Iron Bastard's second three-Chronicle "
        "wave (with 'The Column He Could Not Leave Alone,' MCD-419, and 'The Column Built Without "
        "Metal,' MCD-420). Corrected Batch 321, 2026-10-02: the scholar's pronoun corrected to "
        "he/him throughout, matching the majority usage across `MCD-551`, `MCD-740`, `MCD-1307`, "
        "`MCD-1309`, `MCD-1412`, and `MCD-1414`."
    ),

    # C3/C4 -- MCD-719 rewritten as a genuinely new second trainee, not a re-identified first
    # student; her gender set explicitly to she/her, the majority usage for "the second student."
    "MCD-719": (
        '"The Second Student" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-second-student.md), The Iron Bastard Alias Chronicle "
        "XXIV, wave 8 of ten (waves 6-15). Generational transmission: a new trainee, recommended "
        "by the already-locked first student (`MCD-499`) after two years of observation, works "
        "solo successfully for the first time, confirming the doctrine's lasting growth beyond "
        "Kanja himself -- distinct from, not a re-test of, the first student. She/her, the "
        "majority usage established across the Iron Bastard corpus (10+ entries). Corrected Batch "
        "321, 2026-10-02: the original statement and prose wrongly re-identified the first student "
        "as this entry's subject; rewritten to introduce a genuinely distinct second trainee, and "
        "the backstory reference corrected from an unarmed overseer to the actual granary incident "
        "(`MCD-499`)."
    ),

    # E3 -- citation error: the off-hand-shield/frequency-inversion-lens detail belongs to
    # ARS-050, not MCD-238.
    "MCD-387": (
        '"What Held Together Stopped Holding" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-held-together-stopped-holding.md), Iron Bastard Alias "
        "Chronicle II. Rebellion era, a new engagement against a Trust Crawler variant engineered "
        "with four independent fitting alloys specifically to defeat the single-frequency "
        "resonance that exposed the original vulnerability. Kanja uses the Aegis-Talisman's "
        "frequency-inversion lens (`ARS-050`'s 'off-hand shield/talisman... forged separately') "
        "diagnostically first, cataloguing all four alloy signatures before cycling a sequential "
        "harmonic through each; Mafesto's Kinetic Transfer System absorbs answering fire, "
        "Obsidian Malice discharges into the already-loosened lead Crawler's plating, and Onyx's "
        "Cadence Ruin clears the boarding crew. Eleven of twelve Crawlers are disabled -- the "
        "four-alloy countermeasure produces four points of entry instead of one. No new named "
        "characters. Second entry in the Iron Bastard's three-Chronicle wave. Corrected Batch 321, "
        "2026-10-02: the off-hand-shield/frequency-inversion-lens citation corrected from "
        "`MCD-238` to `ARS-050`, the rule that actually locks that detail."
    ),

    # C9 -- MCD-452 clarified as a second, deliberately diagnostic application of the
    # bridge-collapse-against-cavalry tactic, not a competing "first" against MCD-243.
    "MCD-452": (
        '"The Bridge That Chose Its Moment" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-bridge-that-chose-its-moment.md), the Iron Bastard "
        "Alias Chronicle VII, first entry in the third wave. Holding a bridge alone as rear guard "
        "for a retreating column, Kanja lets a pursuing cavalry force fully commit onto the span "
        "before diagnostically listening to its structural tension and collapsing it from the "
        "pursued end with a single precisely timed Obsidian Malice discharge -- a timing-precision "
        "rescue/combat hybrid distinct from prior Iron Bastard entries. No new named characters. "
        "Clarified Batch 321, 2026-10-02: explicitly placed after the Battle of the Falling "
        "Bridge (`MCD-243`, 'the first recorded use of Mafesto's Kinetic Transfer System as a "
        "structural weapon') as a second, deliberately diagnostic application of the same "
        "bridge-collapse-against-cavalry tactic, not a competing claim to be the first such use."
    ),

    # C6 -- MCD-386's general clarified as a separate, one-scene figure distinct from the
    # recurring general of MCD-454 and its own legacy arc.
    "MCD-386": (
        '"No Ground Worth Taking" (full narrative text at '
        "docs/lords-of-cian/chronicles/no-ground-worth-taking.md), Iron Bastard Alias Chronicle I. "
        "Rebellion era, a new solo stand distinct from the original Iron Bastard's Stand "
        "(MCD-238, age 25). A general who studied only Kanja's terrain-dependent victories chooses "
        "open salt-pan specifically to strip away what he believes is a terrain advantage, not "
        "realizing the original Iron Bastard's Stand was already fought on open ground with no "
        "exploitable terrain -- the engagement proves the alias's advantage was never geography, "
        "ending the general's career when his own accurate report reads to his superiors as an "
        "admission of failure. No new named characters. First entry in the Iron Bastard's "
        "three-Chronicle wave. Clarified Batch 321, 2026-10-02: this general is a separate, "
        "one-scene figure, distinct from the recurring Directorate general of "
        "`MCD-454`/`723`/`730`/`734`/`1082`/`1301`/`1303`, who loses four different engagements "
        "(the original Stand, the four-alloy Crawler variant, a bridge, and a berm) and "
        "voluntarily resigns rather than being disgraced by a single report as this one is."
    ),

    # Consistency fix: the years-later callback to MCD-1283's decision used the same anachronistic
    # "discharge" framing in its own ledger statement; reworded to match the corrected prose.
    "MCD-1495": (
        '"What the Roots Grew Into" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-roots-grew-into.md), Iron Bastard Alias Chronicle "
        "CII, wave 34, closing the wave. A legacy-callback register, the first entry in this "
        "alias's run to return to a specific prior location years later purely to confirm a "
        "long-term outcome rather than advance a new mechanic, threat, or relationship: the living "
        "fig-root bridge (`MCD-1283`) has grown thicker and stronger exactly as its "
        "self-protecting nature predicted, now bearing a market and significantly increased foot "
        "traffic, vindicating the original decision not to strike it down. The second student "
        "(`MCD-719`, she/her) appears in a substantial reflective role. No new named characters. "
        "Closes the Iron Bastard's thirty-fourth wave (with `MCD-1493` and `MCD-1494`) and this "
        "run's three-wave arc (32-34). Corrected Batch 321, 2026-10-02: 'discharge' reworded to "
        "match the corrected prose; second student's gender noted as she/her, the majority usage."
    ),
}

for rid, new_statement in AMENDMENTS.items():
    assert rid in rules_by_id, f"Unknown rule ID: {rid}"
    rules_by_id[rid]["statement"] = new_statement

ledger["batches_completed"].append({
    "batch": 326,
    "date": str(date.today()),
    "source": SOURCE,
    "rule_count": 0,
    "note": (
        "Reconciliation pass following a read-only fable-review of the Iron Bastard Alias "
        "Chronicle corpus (102 entries), one of several parallel per-track reviews run under this "
        "same batch number (see also Batch 320's Bane pilot). Fixed at the prose level across 32 "
        "Chronicle files and amended 17 rule statements to match, with no new creative facts -- "
        "pure reconciliation against already-locked canon, matching the Batch 226/320 precedent. "
        "Fixed: Trinity-era gear anachronisms across waves 16-34 (years past the Trinity's age-30 "
        "surrender, MCD-246) -- Mafesto's Kinetic Transfer System, Obsidian Malice's discharge, "
        "and Onyx's named powers reworded to the Long-Mask-era kit (the Forge-Coat, Ironfall "
        "Boots, Ironhand Gauntlets, Smoke System, Rexmar Machete) across MCD-897, 898, 962, 963, "
        "1047, 1080, 1283, 1284, 1287, 1290, 1293, 1296, 1302, 1413, 1488, 1491, 1494; MCD-963's "
        "framing of the Aegis-Talisman as 'a piece of the Trinity's gear' corrected, since it is "
        "retained post-surrender and distinct from the Trinity per MCD-246; an era-framing "
        "contradiction treating 'the Rebellion' as a still-live war in that same window, reworded "
        "across MCD-898, 1082, 1290, 1301, and (as a consistency extension within the same wave "
        "28 scene) MCD-1302; MCD-719 rewritten to introduce a genuinely new, distinct second "
        "trainee rather than wrongly re-identifying the first student (MCD-499) as the subject of "
        "this test, with the granary backstory reference corrected to match MCD-499's own framing; "
        "five male-gendered instances of the second student (established she/her majority) "
        "corrected across MCD-1047, 1082, 1492, 1494, 1495; the Trust scholar's pronoun (MCD-421) "
        "corrected to he/him, matching the majority usage; the two distinct recurring Directorate "
        "generals (MCD-386's one-scene general vs. MCD-454's four-engagement, voluntarily-"
        "resigning general) disentangled, with MCD-723's opening reference corrected to follow "
        "MCD-454's own legacy arc consistently through MCD-730/734/1082/1301/1303, and a "
        "clarifying note added to MCD-386; MCD-731 corrected to allow that the discharge mechanics "
        "are achievable by ordinary mechanical means once the diagnostic read is correct, "
        "resolving an apparent conflict with several non-Trinity-discharge entries without "
        "touching them individually; Danne Sok's pronoun in MCD-963 corrected to he/him per "
        "CC-159; MCD-452 clarified as a second, deliberately diagnostic bridge-collapse-against-"
        "cavalry application following MCD-243, not a competing 'first'; and a dozen mechanical "
        "errors -- writers'-room 'wave'/'Chronicle'-count language leaking into in-world dialogue "
        "(MCD-1309, 1414, 1495), leaked inline rule-ID citations (MCD-1080, 1286, 1295, 1492), a "
        "citation error (MCD-387: MCD-238 -> ARS-050), MCD-719's misattributed 'unarmed overseer,' "
        "MCD-551's internally-inconsistent 'age 25' header, MCD-964's 'banned by council vote' "
        "(MCD-730 has the proposal fail to advance), MCD-1412's false 'taken off a dead man' claim "
        "(MCD-387 establishes the four-alloy variant as the corps' own engineering response), "
        "MCD-1301's conflated 'shelved report' citation, MCD-1082's garbled gendered line, a stale "
        "Chronicle-count figure in the tracker (93 -> 102), MCD-1048's first student referred to "
        "with 'her'/'his' pronouns reversed, MCD-1489's reserved 'Titan-class fighter' term, "
        "MCD-711's 'cut' corrected to 'broke' (Obsidian Malice is a war club per ARS-030, not a "
        "cutting weapon), MCD-899's garbled continuity-note citation, and MCD-965's false claim "
        "that Kanja personally defended the doctrine to councils before (MCD-730 has the general "
        "doing so, secondhand). E15 (tech-level flags: 'rail bridge,' 'black-powder charge') left "
        "untouched per the review's own direction, pending Abad's call on tech-level consistency. "
        "Pure reconciliation throughout -- no new creative facts, matching the Batch 226/320 "
        "precedent."
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
      f"ledger_version {ledger['ledger_version']}, zero duplicate IDs. "
      f"{len(AMENDMENTS)} rule statements amended, 0 new rules.")
