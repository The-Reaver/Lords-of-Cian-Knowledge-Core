#!/usr/bin/env python3
"""Batch 321: reconciliation corrections surfaced by a read-only review of the Scourge Alias
Chronicle track (102 entries, the 284-year Long Mask disguise identity, ages 22-314). Mechanical
fixes applied directly to the Chronicle .md files (prose + header/continuity notes) and mirrored
here for the matching ledger rule statements: post-surrender Trinity (Mafesto/Obsidian Malice)
anachronisms across 17 entries swapped for the Long Mask's own built gear system (`ARS-344`
through `356`); a gear-version mislabeling (V3 relabeled V4 across a dozen entries, since `ARS-348`
locks V4 starting at age 180, not age 241 as several earlier drafts assumed); the Salt Keep's own
date reconciled (locked at age 140, matching `MCD-446`/`545`/`1476`'s own rule text) against four
entries that referenced it before it happened; "The First Night in the New Coat" (`MCD-811`)
reframed from a new Forge-Coat version to the Sovereign Eyes V4 refit, which `ARS-350` actually
locks at age 240+; a false MCD-1018 cross-reference removed from `MCD-1229` (that Chronicle is set
fifty years later); "Efa Gol's successor" corrected to Efa Gol herself in two entries predating her
age-150 handoff (`MCD-807`); two backward references to not-yet-happened entries reworded; a
self-contradicting Ironfall Boots deployment count fixed (`MCD-1235`); Kanja's locked late-Long-Mask
physical decline (`MCD-271`, "good days vs. bad days") applied by softening two entries' physical
beats without changing their outcomes; a span-arithmetic fix anchoring "years under this name" to
the persona's own age-30 start rather than Ash-Wharf (age 22); an impossible timeline claim removed
(`MCD-1244`); assorted mechanical fixes (a leaked rule-ID citation, an alias misattribution, two
wrong cross-references, a self-contradicting number, several elapsed-time slips including Garren
Hask's own ledger-keeping span -- quoted five different ways across the final-year entries and
reconciled to one consistent figure -- and two near-collision place names renamed). No new creative
facts anywhere in this pass -- pure reconciliation against already-locked canon, matching the Batch
226/68/320 precedent. NOT RUN as part of this pass -- prepared for separate execution."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Read-only review of the Scourge Alias Chronicle track, reconciliation pass, 2026-10-02"

with open(LEDGER_PATH) as f:
    ledger = json.load(f)

rules_by_id = {r["id"]: r for r in ledger["rules"]}

# --- Amend rule statements to match the corrected Chronicle prose ---
AMENDMENTS = {
    # C1: Mafesto/Obsidian Malice anachronisms (statements that explicitly asserted them)
    "MCD-446": (
        '"The Siege of the Salt Keep" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-siege-of-the-salt-keep.md), the Scourge Alias Chronicle "
        "VII, first entry in the third wave. Set roughly age 140, mid-Golden-Terror period: a "
        "detailed combat showcase breaching a three-generation fortified slaving depot using the "
        "Forge-Coat V3/Sovereign Eyes, the Ironhand Gauntlets' leverage to breach the gate, and the "
        "Ironfall Boots, freeing 180 captives -- Onyx of Oblivion, Mafesto, and Obsidian Malice "
        "correctly absent per the Trinity's age-30 surrender (`MCD-246`). No new named characters."
    ),
    "MCD-492": (
        '"The Crew That Challenged the Crescent" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-crew-that-challenged-the-crescent.md), the Scourge Alias "
        "Chronicle XI. Set roughly age 130: a detailed combat showcase against a rival pirate "
        "captain's three-ship squadron assembled specifically to test the Scourge's dominance over "
        "the Gale Straits, sequencing the full gear system (Forge-Coat, Sovereign Eyes, Ironhand "
        "Gauntlets, Ironfall Boots, Smoke System) -- Onyx of Oblivion, Mafesto, and Obsidian Malice "
        "correctly absent per the Trinity's age-30 surrender (`MCD-246`). The rival captain is "
        "disarmed and released rather than killed. No new named characters."
    ),
    "MCD-1041": (
        '"The Three-Cornered Fight" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-three-cornered-fight.md), The Scourge Alias Chronicle "
        "LVIII, wave 20. Age 58, V2 gear. A detailed combat showcase against two hostile parties who "
        "never coordinate with each other -- slavers trying to run captives out to a waiting "
        "Sovereign Trust salvage cutter, and the cutter's own crew trying to seize the ship's cargo "
        "as confiscated property under Trust salvage law. The Scourge frees the hold, denies both "
        "parties their claim, and disables the cutter's rigging with a single, non-lethal use of the "
        "Ironhand Gauntlets' leverage rather than letting either side identify him -- extending 'The "
        "Contract He Wouldn't Sign' (MCD-1017) into an operational priority: staying unclaimed by "
        "Trust jurisdiction even mid-rescue. Onyx of Oblivion, Mafesto, and Obsidian Malice correctly "
        "absent per the Trinity's age-30 surrender (`MCD-246`). No new named characters."
    ),
    "MCD-1074": (
        '"The Strait That Froze Early" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-strait-that-froze-early.md), the Scourge Alias Chronicle "
        "LXI, wave 21, first entry. Age 268, V4 gear (Forge-Coat/Smoke System/Sovereign Eyes/Ironhand "
        "Gauntlets all V4, ARS-347/350/352/354), Mend-Line still V3 (ARS-355, V4 doesn't begin until "
        "age 270). The sub-series' first cold/ice-environment combat showcase: a northern slaving "
        "route freezes eleven days early, trapping a convoy ship in pack ice. Crossing the floes "
        "alone, the Ironhand Gauntlets' V4 blood-heating keeps his grip functional where cold would "
        "otherwise cost it; the Ironfall Boots' impact-sole tremor, built to destabilize standing "
        "opponents, incidentally cracks the ice under a watch post, and he deliberately doesn't risk "
        "a second use near the hull itself, since a tremor strong enough against ice stressed by "
        "freezing water risks opening the ship to the sea before the forty-one captives below can be "
        "freed; the Forge-Coat's grounding weave redirects a boarding axe's own swing at close range. "
        "A hypothermic child is warmed via an off-label field use of the Mend-Line's sealed "
        "reservoirs (ARS-355) against her core rather than a wound. Efa Gol's own successor and "
        "Garren Hask (CC-130, CC-115/116) referenced in established roles, not staged in new action "
        "-- Efa Gol herself has already stepped back by this age (268), well past her age-150 "
        "handoff (`MCD-807`). Onyx of Oblivion, Mafesto, and Obsidian Malice correctly absent per the "
        "Trinity's age-30 surrender (`MCD-246`). No new named characters."
    ),
    "MCD-1469": (
        '"The Ones Who Sold Him Out" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-ones-who-sold-him-out.md), the Scourge Alias Chronicle "
        "XCIV, wave 32, first entry. Age 205, V4 gear. The sub-series' first genuine "
        "betrayal-from-within-a-freed-community failure state -- distinct from every prior tactical "
        "failure (the drowned captives of `MCD-544`, the compromised route of `MCD-1238`, the "
        "tactical retreat of `MCD-1075`) in that the threat originates from someone the crew's own "
        "reputation had earned trust from, not an external enemy's skill or luck. A rendezvous cove "
        "sold to slavers for payment is defeated because the schedule had already quietly changed "
        "two nights before, a detailed Long Mask gear ambush response following. Resolved without "
        "punishment of the informant, deliberately left open, extending the sub-series' established "
        "preference for honest, unresolved ledger entries. Reuses Efa Gol's established unnamed "
        "successor (`MCD-904`/`1240`/`1254`) and Garren Hask (`CC-115`/`116`). Onyx of Oblivion, "
        "Mafesto, and Obsidian Malice correctly absent per the Trinity's age-30 surrender "
        "(`MCD-246`). No new named characters. First entry in wave 32."
    ),
    "MCD-1471": (
        '"The Fleet That Wasn\'t His to Command" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-fleet-that-wasnt-his-to-command.md), the Scourge Alias "
        "Chronicle XCVI, wave 32, closing the wave. Age 195, V4 gear. The sub-series' first formal "
        "multi-party tactical alliance, distinct from the informal one-sided protection of 'The "
        "Signal Honest Ships Learned' (`MCD-382`) and the flat institutional refusals of 'The "
        "Contract He Wouldn't Sign' (`MCD-1017`) and 'The Insurance They Tried to Buy' (`MCD-1019`): "
        "a foreign anti-slaving squadron proposes a single time-limited joint operation against a "
        "fortified trafficking hub neither fleet can take alone, accepted on the same "
        "freely-chosen, freely-ended terms he'd offer any trusted ally, and a standing arrangement "
        "afterward is declined. A detailed full-gear combat showcase (Sovereign Eyes, Ironhand "
        "Gauntlets, the Rexmar Machete `ARS-260`) freeing ninety-six captives. No new named "
        "characters (the foreign commodore is unnamed and one-scene). Onyx of Oblivion, Mafesto, and "
        "Obsidian Malice correctly absent per the Trinity's age-30 surrender (`MCD-246`). Closes "
        "wave 32 (`MCD-1469` through `MCD-1471`)."
    ),
    # Soft "Trinity capability" statements
    "MCD-1232": (
        '"The Glass Reef" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-glass-reef.md), The Scourge Alias Chronicle LXVII, wave "
        "23, first entry. Age 250, V4 gear. The sub-series' first volcanic-obsidian-reef "
        "environment: the Sovereign Eyes' V4 Blueprint Eye structural overlay (ARS-350) reads the "
        "reef's true geometry to thread a channel no chart had mapped correctly, freeing ninety-one "
        "captives with the navigational help of an unnamed local diver whose lived knowledge "
        "complements the Long Mask's own gear rather than being superseded by it. No new named "
        "characters."
    ),
    "MCD-1242": (
        '"What Was Left to Give" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-was-left-to-give.md), The Scourge Alias Chronicle "
        "LXXVII, wave 26. Age 130, V3 gear. The sub-series' first post-liberation famine-relief "
        "entry: fifty-two captives are freed from a drought-exploiting grain-hoarding operation "
        "into an inland settlement with almost nothing left to receive them; the crew spends three "
        "days redirecting the operation's own hoarded grain stores rather than fighting, a "
        "deliberate contrast to MCD-814's already-achieved self-sufficiency by showing the "
        "unglamorous groundwork it depends on. No gear, and no Trinity -- long since surrendered -- "
        "solves the actual problem. No new named characters."
    ),
    "MCD-1476": (
        '"The Reef That Grew Back Wrong" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-reef-that-grew-back-wrong.md), the Scourge Alias "
        "Chronicle CI, wave 34. Age 175, V3 gear. The sub-series' first entry to address the "
        "long-term ecological cost of the crew's own operational history rather than any enemy "
        "action -- distinct from 'The Isle That Stopped Needing Him' (`MCD-814`), which showed "
        "achieved self-sufficiency, by showing instead an unglamorous cost that self-sufficiency "
        "didn't prevent and that no gear, and no Trinity -- long since surrendered -- can solve. Set "
        "at the already-locked Salt Keep site (`MCD-446`, age ~140) and its settlement (`MCD-545`, "
        "age ~200): decades of raid traffic and wreck debris have degraded the settlement's reef, "
        "and Kanja spends eleven days doing unglamorous manual restoration labor alongside its "
        "fishing families, unrecognized. No combat. No new named characters (the fisherman and a "
        "visiting reef-restoration elder are both deliberately unnamed). Onyx of Oblivion correctly "
        "absent per its L9 seal. Second entry in wave 34."
    ),
    # C5: drop the false MCD-1018 cross-reference
    "MCD-1229": (
        '"The Tribunal That Tried to Name Him" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-tribunal-that-tried-to-name-him.md), The Scourge Alias "
        "Chronicle LXIV, wave 22, first entry. Age 98, V3 gear. A Sovereign Trust admiralty tribunal "
        "convenes to formally classify the Scourge's legal status -- stateless pirate versus "
        "unrecognized belligerent -- and deadlocks across three irreconcilable written opinions, "
        "agreeing only that no ruling can be enforced against a party the court cannot locate or "
        "compel. Garren Hask's own sealed testimony, already entered once before in a different "
        "court over the Scrip-Forge evidence, is re-entered here. Institutional/legal-friction "
        "register extending MCD-1017/1041's jurisdictional theme. No new named characters."
    ),
    # C3: V3 -> V4 relabeling (ARS-348 locks V4 starting at age 180, not age 241)
    "MCD-830": (
        '"The Question Efa Gol Finally Asked" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-question-efa-gol-finally-asked.md), The Scourge Alias "
        "Chronicle XLV, wave 15 of ten (waves 6-15). Age 180, V4 gear. Efa Gol directly asks if he "
        "regrets the persona; left deliberately unresolved, closing the ten-wave run."
    ),
    "MCD-1043": (
        '"The Blade She Almost Didn\'t Sheathe" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-blade-she-almost-didnt-sheathe.md), The Scourge Alias "
        "Chronicle LX, wave 20, closing the wave. Age 190, V4 gear. Sena, a new minor one-scene "
        "named crew member and former captive herself, nearly kills an already-surrendered slaving "
        "captain out of her own remembered trauma; Kanja talks her down without force, explaining "
        "the doctrine's real mechanism -- every honored surrender is future people who never have to "
        "be rescued because the fight never happens -- and she sheathes the blade herself, anger "
        "intact. The sub-series' first entry where the non-lethal-surrender doctrine is enforced "
        "from inside the crew rather than tested from outside or by Kanja's own temper (distinct "
        "from MCD-829, MCD-447, MCD-492). Onyx of Oblivion correctly absent per its L9 seal. Closes "
        "the Scourge's twentieth wave (with 'The Three-Cornered Fight,' MCD-1041, and 'The Ones Too "
        "Young to Say Where From,' MCD-1042)."
    ),
    "MCD-1233": (
        '"The Rival Who Called Him a Setback" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-rival-who-called-him-a-setback.md), The Scourge Alias "
        "Chronicle LXVIII, wave 23. Age 190, V4 gear. Three unnamed legal-reform advocates confront "
        "him, arguing his raids undermine years of slow legislative progress against debt-bondage "
        "transfer by handing opponents propaganda; he voluntarily narrows his own operational "
        "targets to flatly illegal operations rather than the legally ambiguous ones the bill "
        "targets, leaving both sides' fundamental disagreement over method honestly unresolved. The "
        "sub-series' first friction with a legitimate, non-hostile reform movement. No new named "
        "characters."
    ),
    "MCD-1248": (
        '"The Fever That Outran the Rescue" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-fever-that-outran-the-rescue.md), The Scourge Alias "
        "Chronicle LXXXIII, wave 28. Age 205, V4 gear. A genuine, unprevented-loss failure state: "
        "the fastest clean liberation the crew has run in years still arrives four days too late for "
        "six of seventy-four captives already fatally weakened by a shipboard fever with a two-week "
        "head start no reconnaissance could have closed; the Mend-Line (ARS-355) is explicitly and "
        "correctly unable to help, extending its established scope to exclude illness alongside "
        "pain, organ repair, and concussive injury. No new named characters."
    ),
    "MCD-1250": (
        '"The Ruling That Changed Nothing" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-ruling-that-changed-nothing.md), The Scourge Alias "
        "Chronicle LXXXV, wave 29, first entry. Age 200, V4 gear. Direct, deliberately anticlimactic "
        'payoff to "The Tribunal That Tried to Name Him" (MCD-1229, age 98): over a century later, a '
        "new set of justices finally issues a ruling classifying the Scourge as an 'unaffiliated "
        "maritime irregular of indeterminate jurisdiction, subject to regional discretion' -- a "
        "sentence with no enforcement mechanism that changes nothing operationally, proving the "
        "earlier tribunal's deadlock right rather than resolving it. No new named characters."
    ),
    "MCD-1244": (
        '"The Duel He Didn\'t Need Onyx For" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-duel-he-didnt-need-onyx-for.md), The Scourge Alias "
        "Chronicle LXXIX, wave 27, first entry. Age 215, V4 gear. A near-miss discipline entry "
        "distinct from MCD-810's gear failure: a bodyguard trained specifically to counter Onyx of "
        "Oblivion's known techniques nearly wins an extended forty-minute duel, and the temptation "
        "to unseal Onyx arises purely internally under pressure; the seal holds by choice, and plain "
        "Rexmar Machete swordsmanship and endurance -- the same craft underlying the whole legend, "
        "already present (if less refined) when it freed two hundred and eleven captives off a "
        "slaver galleon decades earlier (`MCD-381`) -- wins instead. No new named characters."
    ),
    "MCD-1237": (
        '"The Smoke That Spoke First" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-smoke-that-spoke-first.md), The Scourge Alias Chronicle "
        "LXXII, wave 24, closing the wave. Age 225, V4 gear. The first detailed dramatization of the "
        "Smoke System's Signal mode (ARS-354) used by a non-crew party: an unnamed coastal "
        "watch-captain fires a Signal-mode canister salvaged from a raid eleven years earlier, and "
        "the crew's signal code -- spread organically into allied folklore -- summons help against a "
        "raiding party testing the town's protected reputation. No new named characters. Closes the "
        "Scourge's twenty-fourth wave."
    ),
    "MCD-1474": (
        '"The Grandson Who Came to Warn Him" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-grandson-who-came-to-warn-him.md), the Scourge Alias "
        "Chronicle XCIX, wave 33, closing the wave. Age 230, V4 gear (Ironhand Gauntlets still V3, "
        "`ARS-352`'s own separate V3/V4 boundary sitting at age 260). Direct sixty-year generational "
        "payoff to 'The Merchant Who Changed His Trade' (`MCD-824`, age 170), extending a reformed "
        "slaver's changed legacy into the next generation choosing loyalty to the crew unprompted -- "
        "distinct from every prior redemption entry (`MCD-824`, `MCD-1247`), which showed conversion "
        "in the moment rather than its inheritance decades later. A reformed slaver's grandson "
        "travels three days to warn the crew, unprompted, of a rival-slaver ambush borrowed from an "
        "outdated decoy code; the ambush is quietly avoided rather than fought. Reuses Efa Gol's "
        "(`CC-130`/`131`) contact network and Garren Hask (`CC-115`/`116`). No new named characters "
        "(the grandson is deliberately unnamed). Onyx of Oblivion correctly absent per its L9 seal. "
        "Closes wave 33 (`MCD-1472` through `MCD-1474`)."
    ),
    "MCD-1076": (
        '"The Charge She Measured Twice" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-charge-she-measured-twice.md), the Scourge Alias "
        "Chronicle LXIII, wave 21, closing the wave. Age 235, gear generation V4 (`ARS-348` locks V4 "
        "at ages 180-284, which age 235 falls within). The sub-series' first entry to center Pell "
        "Ostra (CC-132/133, the crew's demolitions and chemistry specialist) the way earlier waves "
        "centered Efa Gol (MCD-807) and Garren Hask (MCD-414): a warehouse slated for a breach raid "
        "shares its landward wall with an uninvolved nursery, and Ostra spends four hours mapping "
        "the wall's uneven mortar by ear before splitting her charge into a smaller lead crack and a "
        "larger follow-through timed a half-second behind it, breaching the warehouse cleanly while "
        "leaving the nursery wall's plaster uncracked. Dramatizes her established signature trait "
        "(CC-132) of addressing materials as requests rather than commands directly on the page for "
        "the first time in this sub-series. A moral-complexity/craft entry with no combat at all, "
        "resolved entirely through precision. Closes with a brief exchange comparing her "
        "measured-force philosophy to Kanja's own, noting it's the fruit of twenty-one decades "
        "working beside her (since the Black Trench, age 19), and a light generational-transmission "
        "beat with a deliberately unnamed apprentice. Onyx of Oblivion correctly absent per its L9 "
        "seal. No new named characters. Closes the Scourge's twenty-first wave (with 'The Strait "
        "That Froze Early,' MCD-1074, and 'The Wall He Chose Not to Bleed For,' MCD-1075)."
    ),
    "MCD-1235": (
        '"The Half-Second the Blade Bought" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-half-second-the-blade-bought.md), The Scourge Alias "
        "Chronicle LXX, wave 24, first entry. Age 238, V4 gear. The first detailed, in-action "
        "dramatization of the Ironfall Boots' retractable heel blade (ARS-353, established deployed "
        "eleven times across 284 years, saving his life or freedom in nine): falling through a "
        "hidden pit trap mid-rescue, the blade's trigger catches into the pit wall and arrests the "
        "fall, established here as the eleventh and final deployment and one of the nine "
        "life/freedom-saving uses, consistent with the existing count. No new named characters."
    ),
    "MCD-1475": (
        '"The One Who Chose to Leave" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-one-who-chose-to-leave.md), the Scourge Alias Chronicle "
        "C, wave 34, first entry. Age 198, V4 gear (Ironhand Gauntlets still V3, `ARS-352`'s own "
        "separate V3/V4 boundary sitting at age 260; the Mend-Line still V2, `ARS-355`'s own V3 "
        "threshold sitting at age 200). The sub-series' first voluntary, principled departure from "
        "the Scourge's operational core -- distinct from Efa Gol's aging-out retirement (`MCD-807`) "
        "and Pell Ostra's failing-hands retirement (`MCD-1472`) in that the departing crew member "
        "leaves neither worn out nor replaced by failure, but on a genuine ethical disagreement with "
        "the fear-based method itself, a real institutional-health test the doctrine has not "
        "previously faced from inside its own ranks. New minor named character: Rowan Vail (a "
        "thirty-one-year decoy-line veteran under Efa Gol, collision-checked clean against the full "
        "ledger before drafting), reassigned to settlement/placement work rather than removed from "
        "continuity. Reuses Efa Gol (`CC-130`/`131`) and Garren Hask (`CC-115`/`116`). No combat. "
        "Onyx of Oblivion correctly absent per its L9 seal. First entry in wave 34."
    ),
}

for rid, new_statement in AMENDMENTS.items():
    assert rid in rules_by_id, f"Unknown rule id in AMENDMENTS: {rid}"
    rules_by_id[rid]["statement"] = new_statement

ledger["batches_completed"].append({
    "batch": 329,
    "date": str(date.today()),
    "source": SOURCE,
    "rule_count": 0,
    "note": (
        "Reconciliation pass applying fixes surfaced by a read-only review of the Scourge Alias "
        "Chronicle track (102 entries, the 284-year Long Mask disguise identity, ages 22-314). "
        "Fixed in both the Chronicle .md files and these 21 matching ledger rule statements: "
        "post-surrender Trinity (Mafesto/Obsidian Malice) anachronisms across 17 entries swapped "
        "for the Long Mask's own built gear system (`ARS-344` through `356`) -- Mafesto's Kinetic "
        "Transfer System reframed as the Forge-Coat/Ironfall Boots grounding weave, Obsidian "
        "Malice's 'discharge' reframed as the Ironhand Gauntlets' leverage, every duplicated "
        "'two-year dormant charge' claim removed (MCD-446, 492, 543, 802, 805, 808, 812, 817, 823, "
        "829, 1041, 1074, 1075, 1469, 1470, 1471, 1476; MCD-1014/1015 left untouched as legitimate "
        "pre-seal Trinity use); a gear-version mislabeling corrected (V3 relabeled V4 across twelve "
        "entries -- MCD-830, 1043, 1233, 1248, 1250, 1469, 1244, 1237, 1474, 1076, 1235, 1475 -- "
        "since `ARS-348` locks V4 starting at age 180, not age 241 as several earlier drafts "
        "assumed); the Salt Keep's own date reconciled at age 140 (matching `MCD-446`/`545`/`1476`'s "
        "own rule text) against four entries (MCD-801, 807, 809, 819) that referenced it before it "
        "happened or mischaracterized it; 'The First Night in the New Coat' (`MCD-811`) reframed "
        "from a new Forge-Coat version to the Sovereign Eyes V4 refit, which `ARS-350` actually "
        "locks at age 240+; a false `MCD-1018` cross-reference removed from `MCD-1229` (that "
        "Chronicle is set fifty years later); 'Efa Gol's successor' corrected to Efa Gol herself in "
        "two entries (MCD-820, 822) predating her age-150 handoff (`MCD-807`); two backward "
        "references to not-yet-happened entries reworded (MCD-823 -> MCD-812; MCD-1239 -> "
        "MCD-1074); a self-contradicting Ironfall Boots deployment count fixed from 'eleven times "
        "... the tenth' to a consistent 'eleventh and final' (`MCD-1235`); Kanja's locked "
        "late-Long-Mask physical decline (`MCD-271`, 'good days vs. bad days') applied per Abad's "
        "ruling by softening two entries' physical beats (MCD-1406's beach liberation, MCD-1022's "
        "final boarding action) without changing either outcome; a span-arithmetic fix anchoring "
        "'years under this name' to the persona's own age-30 start rather than Ash-Wharf (age 22) "
        "in MCD-1022 and MCD-1255 (MCD-813 and MCD-1477 left unchanged, since they already counted "
        "correctly from age 22); an impossible timeline claim removed from `MCD-1244` (the galleon "
        "fight at `MCD-381` already used this gear, just an earlier version, corrected from "
        "'decades before any of this gear existed'/'twenty years' to the real ~163-year gap). "
        "Mechanical fixes: a leaked rule-ID citation stripped (`MCD-382`); an alias misattribution "
        "corrected (`MCD-1015`'s 'Furnace District' callback, which belongs to the Industrial Myth "
        "alias, corrected to 'the dredge-lines,' the Trench Monarch's own domain, matching the "
        "rule's own statement); a setting mismatch and a number mismatch reconciled between two "
        "linked entries (`MCD-1407`/`1408`); four wrong rule citations fixed (`MCD-413`: "
        "'MCD-267-area' -> `MCD-246`; `MCD-446`: 'MCD-413' -> `MCD-246` directly; `MCD-1016`: "
        "'MCD-291' -> `ARS-344`; `MCD-1014`: 'MCD-291/ARS-344' -> `ARS-347` alone); a false claimed "
        "killing corrected to a disarming to match the alias's established doctrine (`MCD-415`); a "
        "wrong attribution fixed ('Efa Gol's decoy line' -> her successor's, `MCD-1074`, age 268); "
        "a stale tracker figure corrected (`chronicle-tracks-status.md`'s Scourge row, 93 -> 102); "
        "two near-collision place names renamed (a slaving hub 'Kessara' -> 'Varrow', avoiding the "
        "locked SBD capital Kesmara; 'Ferrenline docks' -> 'Orencliff docks', avoiding the locked "
        "Ferrenhall patron dynasty); and a batch of elapsed-time slips corrected, including Garren "
        "Hask's own ledger-keeping span, which had been quoted five inconsistent ways across the "
        "final-year entries (ages 308-313) and is now reconciled to one consistent figure anchored "
        "to the persona's own age-30 start (MCD-1253: 277 -> 280 years; MCD-1255: 278 -> 283 years "
        "running; MCD-1406: 279 -> 283 years; MCD-1407: 270 -> 283 years; MCD-1252 already correct "
        "at 278, left unchanged), plus MCD-1471 ('fourteen years before' -> 'forty', matching "
        "`MCD-1017`'s actual age), MCD-1254 ('seven years earlier' -> 'forty-two', matching "
        "`MCD-1240`'s actual age), MCD-1246 ('forty years earlier' -> 'a hundred and forty', "
        "matching Efa Gol's own age-150 step-back), MCD-1243 ('two hundred and sixty-seven years' "
        "-> 'a hundred and twenty', since the forty-two-compartment Pocket Architecture is a V4 "
        "feature that didn't exist before age 180), MCD-1230 ('six years of documented reputation' "
        "-> 'a hundred and forty-six years'), and MCD-826 ('three centuries' of Garren Hask's "
        "ledgers -> 'seven decades', matching this entry's age 90 against Hask's own crew-founding "
        "age). No new creative facts anywhere in this pass -- pure reconciliation against "
        "already-locked canon, matching the Batch 226/68/320 precedent. NOT RUN as part of this "
        "pass -- prepared for separate execution."
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
      f"{len(AMENDMENTS)} rule statements amended.")
