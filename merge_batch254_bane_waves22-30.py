#!/usr/bin/env python3
"""Batch 254: Bane Alias Chronicle waves 22-30 (27 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Bane's twenty-second through thirtieth Alias Chronicle waves (9 waves, 27 entries), drafted "
    "under Abad's blanket authorization to continue Bane's waves 22-30 uninterrupted. Pushes into "
    "genuinely new registers not yet used across Bane's prior 63 entries: a dedicated Whisper of "
    "Shadows showcase and its own established limit (fails against animal senses); a principled "
    "ideological rival whose disagreement with Bane's methods is never resolved; a civilian death "
    "from Bane's own crossfire, held without absolution; a first Obsidian Malice equipment failure "
    "(storm interference); proactive information-warfare countermeasure work; a new second-tier "
    "field commander trained by Corren Halst; a full-Trinity river-crossing combat showcase with "
    "Obsidian Malice deliberately withheld from the water; a pure epidemic/quarantine humanitarian "
    "entry; a genuine strategic cost of Bane's own amnesty doctrine; a desert/heat survival "
    "showcase; a new recurring antagonist (Colonel Serrin Draeth) introduced, advanced, and closed "
    "across three entries via his own direct recognition of VB-060 rather than combat; generational "
    "transmission through Efa Gol; a punitive Directorate reprisal Bane cannot prevent or answer; a "
    "children's folk-song legend-drift closer; a direct companion piece completing the caution/delay "
    "trade-off left one-sided by an earlier wave; a genuinely unresolvable dual-column dilemma with "
    "real loss on the unchosen side; a second, humanitarian Whisper of Shadows showcase; Bane "
    "deliberately absenting himself from an institutional tribunal he could dominate; a dense urban "
    "civilian-embedded full-Trinity showcase withholding Obsidian Malice entirely; a genuine failure "
    "of Danne Sok's own judgment; a volunteer rear-guard sacrifice Bane is talked out of joining; "
    "Garren Hask's own first refusal to record a cost in the crew ledger; a multi-week, whole-district "
    "restorative-labor register; and a closing pair of reflective entries (Corren Halst on why the "
    "aliases matter, Efa Gol closing the run) explicitly framing the alias as continuing rather than "
    "retiring. Two new minor named characters: Toran (a new second-tier field commander trained by "
    "Corren Halst) and Colonel Serrin Draeth (Bane's first recurring antagonist) -- both "
    "collision-checked clean against the full ledger before drafting. Every other entry reused "
    "already-locked crew (Corren Halst, Danne Sok, Efa Gol, Callum Breck, Maret Vos, Garren Hask). "
    "Abad's approval: \"lets do this 22nd Alias Chronicle wave for any/all of the eleven aliases to "
    "the 30th wave and you are to continue uninterrupted until completion this includes rigorous "
    "testing, commit, push to main origin.\""
)

NEW_RULES = [
    {
        "id": "MCD-1094",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Shadows Wouldn't Hide\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-shadows-wouldnt-hide.md), Bane Alias Chronicle "
            "LXIV, wave 22. First dedicated showcase of Onyx of Oblivion's Whisper of Shadows power "
            "for this alias: Bane and Danne Sok infiltrate a Directorate records depot to extract "
            "captured couriers, the power redirecting trained human attention away from Bane's "
            "movement through three patrol lines. Establishes a genuine, reusable limit -- the power "
            "has no effect on animal senses, nearly exposing them to a guard dog before Danne Sok's "
            "own improvisation solves it. No new named characters -- Danne Sok reused. Opens wave 22."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1095",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The General Who Wouldn't Sit With Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-general-who-wouldnt-sit-with-him.md), Bane Alias "
            "Chronicle LXV, wave 22. A principled rival partisan commander refuses to coordinate with "
            "Bane's methods on ideological grounds (force normalizes what they're fighting); the two "
            "run parallel, uncoordinated operations in the same district in the same week -- Bane "
            "takes a garrison by force, she starves it by boycott -- both succeed, and the "
            "disagreement is never resolved into alliance or agreement. No new named characters -- "
            "the rival commander is unnamed and one-scene; Corren Halst reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1096",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Crossfire Left Behind\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-crossfire-left-behind.md), Bane Alias Chronicle "
            "LXVI, wave 22, closing wave 22. A liberation raid succeeds by every operational metric "
            "except one -- a stray discharge kills a child hidden in an unlisted supply shed. Bane "
            "refuses to let Corren Halst frame it as an acceptable cost of war on his behalf, states "
            "the death is his to carry, and stays for the burial rather than moving the column on "
            "schedule. Deliberately unresolved civilian-cost grief register. No new named characters "
            "-- the mother and child are unnamed; Corren Halst reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1097",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Charge That Fired Too Soon\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-charge-that-fired-too-soon.md), Bane Alias Chronicle "
            "LXVII, wave 23. First genuine Obsidian Malice equipment failure for this alias: an "
            "electrical storm's ambient charge triggers a partial premature discharge mid-approach to "
            "a garrison, costing surprise; Bane adapts and wins anyway through improvisation, and "
            "openly acknowledges the failure to the crew afterward. Extends the weapon's established "
            "two-timescale charge mechanism with a new environmental-interference case, completing a "
            "documented failure case for all three Trinity pieces. No new named characters -- Corren "
            "Halst and Danne Sok reused. Opens wave 23."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1098",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Story They Wanted to Be True\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-story-they-wanted-to-be-true.md), Bane Alias Chronicle "
            "LXVIII, wave 23. Directorate propaganda fabricates a massacre and blames it on Bane to "
            "justify a crackdown on a border district; Bane counters proactively, before any formal "
            "proceeding, by escorting three independent, uninvolved merchants to the actual site to "
            "read the physical evidence themselves rather than narrating it to them -- deliberately "
            "contrasted against 'The Rumor He Never Corrected' (MCD-681) to establish the actual "
            "principle: he corrects a false story only when it costs real people something, not to "
            "protect his own reputation. No new named characters -- the merchants are unnamed; Danne "
            "Sok reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1099",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Lieutenant Corren Halst Chose\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-lieutenant-corren-halst-chose.md), Bane Alias "
            "Chronicle LXIX, wave 23, closing wave 23. Corren Halst personally trains a new "
            "second-tier field commander, Toran (new named minor character, collision-checked clean), "
            "extending the crew's operational discipline beyond the founding circle for the first "
            "time -- tests whether the standing order from 'The Night His Judgment Slipped' (MCD-1059, "
            "no operational plan runs past the fourth sleepless night without a second set of eyes) "
            "survives being taught secondhand. Corren Halst and Bane reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1100",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the River Carried Between Them\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-river-carried-between-them.md), Bane Alias "
            "Chronicle LXX, wave 24. A detailed full-Trinity combat showcase fought waist-deep during "
            "a night river crossing under attack: Mafesto redirects the current itself against "
            "wading attackers, Onyx's Cadence Ruin reads coordinated footsteps through the riverbed "
            "in place of sight, and Obsidian Malice's discharge is deliberately released clear of the "
            "water rather than through it to avoid endangering the forty people still crossing -- a "
            "new explicit safety constraint on the weapon. No new named characters -- Danne Sok "
            "reused. Opens wave 24."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1101",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fever That Moved Faster Than the Column\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fever-that-moved-faster-than-the-column.md), Bane "
            "Alias Chronicle LXXI, wave 24. Pure humanitarian entry, no combat: a fever outbreak "
            "spreads through a refugee camp faster than the column can move; Bane defers medical "
            "authority entirely to the camp's own healer and carries out her orders rather than "
            "directing treatment himself, including the harder call to leave the most contagious "
            "cases under guarded isolation rather than move the whole group. No new named characters "
            "-- the healer is unnamed; Efa Gol reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1102",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Garrison He Let Walk\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-garrison-he-let-walk.md), Bane Alias Chronicle LXXII, "
            "wave 24, closing wave 24. A garrison released under Bane's own amnesty terms re-arms and "
            "ambushes an unrelated Rebellion supply column weeks later, killing six -- the first "
            "entry to show a direct, specific cost of the mercy doctrine at strategic scale. Bane "
            "does not reverse the doctrine, states plainly to Corren Halst that the math was always "
            "going to cost something real eventually. No new named characters -- the former garrison "
            "captain is unnamed and does not appear on-page; Corren Halst reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1103",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Dry Crossing\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-dry-crossing.md), Bane Alias Chronicle LXXIII, wave "
            "25. New desert/heat survival-environment register: the column crosses a waterless "
            "thirty-one-mile salt basin under a hard deadline, with heat and thirst doing what no "
            "enemy in the run has managed. Extends the established selfless-ration-sharing habit "
            "(MCD-686) into a wordless exchange with Callum Breck, who quietly adjusts the ration "
            "count after noticing Bane giving up his own share. No new named characters -- Callum "
            "Breck and Efa Gol reused. Opens wave 25."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1104",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Colonel Who Came Back\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-colonel-who-came-back.md), Bane Alias Chronicle "
            "LXXIV, wave 25. Introduces Colonel Serrin Draeth (new named minor character, "
            "collision-checked clean), a Directorate officer defeated months earlier who returns for "
            "a personal rematch rather than under orders -- Bane's first recurring, rather than "
            "one-scene, antagonist. Bane declines to give him the personal fight he wants, completes "
            "the actual operation instead, and leaves the thread deliberately open. No other new "
            "named characters -- Corren Halst reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1105",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Efa Gol Taught the New Ones\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-efa-gol-taught-the-new-ones.md), Bane Alias Chronicle "
            "LXXV, wave 25, closing wave 25. Efa Gol personally trains six new recruits in decoy and "
            "diversion tactics -- generational transmission through her rather than Bane, paralleling "
            "wave 23's Corren Halst/Toran entry through a different crew member and skillset. Ties "
            "to her already-locked loss of pair-partner Tam Sullen at the Black Trench without "
            "restaging it. No new named characters -- the recruits are unnamed as a group."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1106",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Second Time the Colonel Came\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-second-time-the-colonel-came.md), Bane Alias Chronicle "
            "LXXVI, wave 26. Colonel Serrin Draeth returns, having drilled himself to resist VB-060's "
            "'Already-Finished Negotiation' presence trait by refusing to enter Bane's presence at "
            "all, communicating only through a subordinate -- the countermeasure's own existence "
            "becomes the tell, extending the trait's established limits (previously simple failure "
            "against unshaken discipline in 'The Man Who Didn't Flinch,' MCD-688) into deliberate "
            "avoidance. Thread advances, not resolved. No new named characters -- the lieutenant is "
            "unnamed and one-scene; Corren Halst reused. Opens wave 26."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1107",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Granary They Burned to Prove a Point\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-granary-they-burned-to-prove-a-point.md), Bane Alias "
            "Chronicle LXXVII, wave 26. A purely punitive Directorate reprisal -- a losing garrison "
            "commander burns a settlement's entire grain store for no military reason, then withdraws "
            "beyond reach before Bane hears of it -- the first entry where Bane's own presence and "
            "timing have zero effect on the triggering harm itself; he organizes emergency rationing "
            "and a relief convoy afterward rather than any form of retribution. No new named "
            "characters -- the garrison commander is unnamed and never appears on-page; Efa Gol "
            "reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1108",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Song They Sang Without Knowing Whose It Was\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-song-they-sang-without-knowing-whose-it-was.md), Bane "
            "Alias Chronicle LXXVIII, wave 26, closing wave 26. Refugee children turn garbled "
            "accounts of Bane into a marching song, unaware the man walking near the column's rear is "
            "its subject; Bane deliberately doesn't correct it, telling Danne Sok the song isn't "
            "about him anymore, it's about what the column needed to believe on a long walk. New "
            "folk-culture/legend-drift texture -- uncommercial, uninstitutional, specifically "
            "generational -- distinct from prior legend-drift entries. No new named characters -- "
            "Danne Sok reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1109",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Verification That Took Too Long the Right Way\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-verification-that-took-too-long-the-right-way.md), "
            "Bane Alias Chronicle LXXIX, wave 27. Direct companion piece to 'What the Delay Cost' "
            "(MCD-477): the same standing extra-day verification catches a fabricated Directorate "
            "counterintelligence lure meant to draw the column into an ambush, at zero cost this "
            "time -- deliberately not framed as vindication that caution is always right, only as "
            "the other half of a real, double-edged trade-off. No new named characters -- Corren "
            "Halst reused. Opens wave 27."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1110",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Two Columns That Never Met\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-two-columns-that-never-met.md), Bane Alias Chronicle "
            "LXXX, wave 27. A storm-washed road and a miscarried messenger (no one's fault) leave two "
            "allied columns unable to reach a rendezvous in time, forcing Bane to choose between two "
            "now-uncoordinated obligations; unlike 'What He Couldn't Be in Two Places For' (MCD-938), "
            "which found a clean solution, there is no way to save both here, and the allied column "
            "takes real losses waiting for relief that structurally could not have arrived in time. "
            "No new named characters -- Corren Halst and Garren Hask reused; Maret Vos referenced "
            "consistently with his he/him status (Batch 226) though not appearing on-page."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1111",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Silence After Meant\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-silence-after-meant.md), Bane Alias Chronicle "
            "LXXXI, wave 27, closing wave 27. A second, wholly humanitarian use of Whisper of Shadows "
            "(after MCD-1094): Bane escorts a dying, decade-long informant safely across contested "
            "ground so he can deliver one final piece of testimony before he dies, engaging no one "
            "the entire way -- protective rather than infiltration/extraction use of the power. No "
            "new named characters -- the informant and two safehouse listeners are unnamed; Danne "
            "Sok reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1112",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Trial They Held Without Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-trial-they-held-without-him.md), Bane Alias Chronicle "
            "LXXXII, wave 28. Direct extension of the arbiter-council thread (MCD-939, MCD-1028): for "
            "the first time Bane deliberately absents himself from an institutional proceeding he "
            "could dominate by presence alone, sending Corren Halst to observe only -- the council "
            "reaches a genuinely mixed verdict on its own, confirming to Bane the process is real "
            "rather than borrowed through his own presence in the room. No new named characters -- "
            "the collaborator is unnamed; Corren Halst reused. Opens wave 28."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1113",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Weight of the Ones Who Didn't Run\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-weight-of-the-ones-who-didnt-run.md), Bane Alias "
            "Chronicle LXXXIII, wave 28. A detailed full-Trinity combat showcase defending a dense "
            "urban tenement district whose residents refused evacuation, civilians embedded "
            "throughout the fighting rather than cleared ahead of it -- Mafesto's redirections are "
            "aimed along streets rather than into structures, Onyx's Cadence Ruin and reading of "
            "occupied doorways make the precision possible, and Obsidian Malice is withheld entirely "
            "as unsuitable for the terrain, decided before the engagement rather than constrained "
            "mid-use. No new named characters -- Efa Gol reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1114",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ones Danne Sok Couldn't Save\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ones-danne-sok-couldnt-save.md), Bane Alias Chronicle "
            "LXXXIV, wave 28, closing wave 28. A genuine failure entry for Danne Sok: his own "
            "split-second choice of which of two doors to breach first costs a captive's life -- the "
            "first real operational failure attributed directly to a founding crew member rather than "
            "to Bane, bad intelligence, or exhaustion. Bane makes him state plainly what he'd do "
            "differently with the same information (nothing) and frames that honest answer as the "
            "only apology available. No new named characters -- the captive and the guard are "
            "unnamed."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1115",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Colonel Understood Too Late\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-colonel-understood-too-late.md), Bane Alias "
            "Chronicle LXXXV, wave 29. Closes the three-entry Colonel Serrin Draeth thread (MCD-1104, "
            "MCD-1106): Draeth finally confronts Bane in person and, mid-confrontation, directly "
            "recognizes VB-060's 'Already-Finished Negotiation' framing for himself -- that there was "
            "never a personal fight to win -- and walks away unharmed, later requesting reassignment "
            "to a rear post rather than being killed or court-martialed, matching the sub-series' "
            "preference for nuanced closures over clean villain defeats. No new named characters -- "
            "Corren Halst reused. Opens wave 29."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1116",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ones Who Stayed Behind to Lie\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ones-who-stayed-behind-to-lie.md), Bane Alias "
            "Chronicle LXXXVI, wave 29. During a forced retreat, five recently freed captives "
            "volunteer to stay behind and fake continued resistance to buy the column time; Bane "
            "wants to stay with them and is talked out of it by the volunteers themselves, who argue "
            "his presence at the column's head matters more than one more sword in the rear guard -- "
            "first entry centering others' deliberate sacrifice rather than Bane's own. Two of the "
            "five survive. No new named characters -- the five volunteers are unnamed and "
            "deliberately distinct from founding-crew losses already established (Tam Sullen, Nev "
            "Torr); Corren Halst reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1117",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Garren Hask Refused to Write Down\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-garren-hask-refused-to-write-down.md), Bane Alias "
            "Chronicle LXXXVII, wave 29, closing wave 29. Direct payoff to MCD-1116 and companion "
            "piece to 'The Numbers Bane Left Behind' (MCD-695): Garren Hask deliberately leaves the "
            "rear guard's cost out of the crew's own running ledger, telling Bane some costs are owed "
            "to the people who paid them rather than to a book, and writing it down like every other "
            "number would make it smaller than it was -- extends his ledger-keeper role with its own "
            "stated limit for the first time. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1118",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Season Bane Didn't Fight\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-season-bane-didnt-fight.md), Bane Alias Chronicle "
            "LXXXVIII, wave 30. The largest-scale non-combat restorative-labor register in the run: "
            "the column spends six weeks rebuilding a liberated district's roofs and granaries ahead "
            "of winter, no gear drawn and no engagement across the entire entry, extending 'The "
            "Village He Didn't Burn' (MCD-691, a five-day rebuild) to a multi-week, whole-district "
            "scale. No new named characters -- Efa Gol, Callum Breck, and Danne Sok reused; the "
            "district elder is unnamed. Opens wave 30."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1119",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Names on One Man's List\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-names-on-one-mans-list.md), Bane Alias Chronicle "
            "LXXXIX, wave 30. A reflective entry through Corren Halst on the functional, in-world "
            "purpose of Kanja's multiple aliases -- not truth split into pieces but the same truth "
            "offered through enough different doors that it can reach whoever needs a specific one at "
            "the right moment. Deliberately framed as an in-fiction observation, not a structural or "
            "meta reference to the Alias Chronicle sub-series itself. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1120",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Name Still Meant\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-name-still-meant.md), Bane Alias Chronicle XC, "
            "wave 30, closing wave 30. Closing entry for waves 22-30: Efa Gol asks whether the name "
            "still fits after ninety operations, and Bane's answer directly counterpoints wave 15's "
            "'What the Name Cost Him to Set Down' (MCD-710) -- the alias isn't his to set down, it's "
            "the door that still reaches people who need it, and the run continues rather than ends. "
            "Reunites with Efa Gol (already locked, CC-130, established in MCD-433 as the crew member "
            "who checks on the man rather than the alias). No new named characters. Closes wave 30 "
            "and this nine-wave run."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 27, f"expected 27 new rules, got {len(NEW_RULES)}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    for r in NEW_RULES:
        assert r["category"] == "kanja-alias-chronicle", f"bad category on {r['id']}: {r['category']}"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 254,
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
