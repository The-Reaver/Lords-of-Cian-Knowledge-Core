#!/usr/bin/env python3
"""Batch 321: corrections surfaced by a read-only review pass on the Lord of Embers Alias
Chronicle track (102 entries). Fixes a Trinity-era gear anachronism (the Forge-Coat/Dark-Drakma
leather appearing at age 27, decades before it exists), a Mafesto mischaracterization (described
twice as forearm-scale/concealable gear rather than a full bio-bonded exoskeleton), chronology
compression throughout an 18-month tour (settlements/events described in "years"/"decades" when
only months have passed, and a 120-settlement figure against the locked 31, MCD-241), a Chronicle
numbering error (two trios of entries sharing roman numerals with two other, correctly-numbered
entries), a training-span mismatch between two entries, a header era contradiction, and a set of
mechanical errors (leaked rule-ID citations and writers'-room phrasing in narrative prose, stale
citations, a proper-noun collision with the already-locked Tomas Grieve, typos, and a stale
tracker count). No new creative facts -- pure reconciliation against already-locked canon, matching
the Batch 226/68/320 precedent. The affected Chronicle `.md` files were corrected directly as
prose/header edits in a companion pass; this script only amends the matching ledger rule
statements."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Read-only review pass (Lord of Embers Alias Chronicle corpus), reconciliation pass, 2026-10-02"

with open(LEDGER_PATH) as f:
    ledger = json.load(f)

rules_by_id = {r["id"]: r for r in ledger["rules"]}

# --- Amend rule statements to match the corrected Chronicle prose ---
AMENDMENTS = {
    # --- C1: MCD-1322 -- Forge-Coat/Dark-Drakma leather anachronism at age 27 ---
    "MCD-1322": (
        '"What Mafesto Couldn\'t Shed" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-coat-couldnt-shed.md), Lord of Embers Alias "
        "Chronicle LXXVI, first entry in the twenty-sixth wave. The alias's first real Mafesto "
        "damage/vulnerability entry: an accidental crack disables the Void-Lattice's "
        "light-absorptive quality across a whole shoulder panel, exposing Kanja to near-detection "
        "until the senior smith's successor improvises a rough field-repair compound, restoring "
        "roughly two-thirds function for six weeks pending proper repair. No new named characters. "
        "Corrected Batch 321, 2026-10-02: the damaged item was originally written as the "
        "Forge-Coat's Dark-Drakma leather, gear that doesn't exist until the Long Mask (ages "
        "33-284); retitled and rewritten around Mafesto's own Void-Lattice plating, which is live "
        "and wearable at age 27."
    ),
    # --- C2: chronology compression across an 18-month tour ---
    "MCD-1052": (
        '"The Standard They Wrote Into the Books" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-standard-they-wrote-into-the-books.md), the Lord of "
        "Embers Alias Chronicle LX, wave 20, closing the wave. Rebellion era, age 27, the Rolling "
        "Foundry Campaign. A regional smiths' guild council formally institutionalizes the "
        "campaign's open-method rebuild-and-teach doctrine as the 'Open-Forge Standard,' an "
        "examinable journeyman certification entered into guild law under no alias's name and "
        "requiring no candidate ever meet Kanja -- economic/institutional legitimization distinct "
        "from prior guild entries (personal exclusion overturned, a formal judged craft contest at "
        "MCD-921, a suppressed rebuild-speed report). The recurring senior smith's already-"
        "established successor (MCD-923), whose own testimony to the council prompted the "
        "delegation, is honored with authorship of the standard and declines to name it after "
        "herself, insisting it be named for what it does. Closes the Lord of Embers' twentieth "
        "three-Chronicle wave (with 'What the Slag Left Behind,' MCD-1050, and 'What the Trinity "
        "Couldn't Absorb,' MCD-1051). No new named characters. Corrected Batch 321, 2026-10-02: "
        "softened chronology compression (the delegation now arrives roughly a year into the "
        "18-month tour rather than at its end) and fixed the eldest's 'we already did that, years "
        "back' line to correctly reference the itinerant master smith's judged contest (MCD-921) "
        "rather than an impossible prior council test."
    ),
    "MCD-423": (
        '"The Night They Came for the Anvil" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-night-they-came-for-the-anvil.md), Lord of Embers Alias "
        "Chronicle V. A raid targets The Anvil (MCD-241) itself for its accumulated Dead Drakma "
        "stock; Kanja meets the boarders on deck rather than let the fight reach sleeping "
        "apprentices belowdecks, demonstrating Mafesto's grounding function, Obsidian Malice "
        "collapsing the boarding ramp structurally to strand the second wave, and Onyx's Whisper "
        "of Shadows/Veil Piercer clearing the deck. The raid breaks in six minutes. No new named "
        "characters; the salvage master is unnamed and one-scene. Corrected Batch 321, 2026-10-02: "
        "softened chronology compression ('full eighteen-month accumulation' and 'thirty-one "
        "settlements,' impossible this early in the tour at Chronicle V/wave 2, to 'months' and "
        "'two dozen settlements')."
    ),
    "MCD-1050": (
        '"What the Slag Left Behind" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-slag-left-behind.md), the Lord of Embers Alias "
        "Chronicle LVIII, first entry in the twentieth wave. Rebellion era, age 27, the Rolling "
        "Foundry Campaign (MCD-241). Six weeks of heavy salvage-smelting sends slag runoff into an "
        "unrelated downstream farm's irrigation channel, souring a season's crop with no enemy and "
        "no rebuild target involved -- a genuinely new register of limit for 'metabolizes "
        "punishment': harm the campaign's own industrial scale caused rather than absorbed, which "
        "no rebuild speed can reach backward to undo. Kanja voluntarily halts the site's smelting "
        "for four days, has apprentices cut a diversion trench and lime-treatment basin, and pays "
        "the ruined harvest's cost from campaign stores rather than pretend it was rebuilt. No new "
        "named characters. Corrected Batch 321, 2026-10-02: softened chronology compression "
        "('eighteen months and thirty-one settlements deep' to 'months and two dozen settlements "
        "deep')."
    ),
    "MCD-1333": (
        '"What They Agreed to Owe Each Other" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-they-agreed-to-owe-each-other.md), Lord of Embers "
        "Alias Chronicle LXXXVII, wave 29, closing the wave. The alias's first formal "
        "labor/economic-governance entry: an apprentice's blunt question exposes that the campaign "
        "had never built a compensation structure alongside its teaching structure; a graduated "
        "stipend and apprentice dispute council are co-designed with apprentices themselves, "
        "extending the open method's participatory ethos into labor governance. No new named "
        "characters. Corrected Batch 321, 2026-10-02: softened chronology compression ('Thirty-one "
        "settlements... later' to 'Two dozen settlements... later')."
    ),
    "MCD-1084": (
        '"The Standard They Learned to Fake" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-standard-they-learned-to-fake.md), the Lord of Embers "
        "Alias Chronicle LXII, wave 21. Rebellion era, age 27, the Rolling Foundry Campaign "
        "(MCD-241), some months after the Open-Forge Standard's institutionalization (MCD-1052). "
        "A genuinely new register of limit for 'metabolizes punishment': counterfeiters stamp a "
        "near-match of the Open-Forge Standard's guild seal onto substandard tools and sell them as "
        "genuine across several settlements, causing real injuries; unlike every prior punishment "
        "the floor has answered, the harm has no single location, cart, or forge left to march "
        "toward -- the counterfeit tools are already scattered and in daily use beyond the "
        "campaign's reach, unrecallable. Kanja issues a harder counter-mark through the guild "
        "council and covers proven-genuine-belief losses from campaign stores, but neither reaches "
        "backward to the harm already done, and within a season a second forger has already begun "
        "faking the harder mark too -- left honestly unresolved rather than cleanly fixed. The "
        "senior smith's successor (MCD-923, MCD-1052) appears consistently with her established "
        "role. No new named characters. Corrected Batch 321, 2026-10-02: softened chronology "
        "compression ('spent eighteen months learning to read the true one' to 'spent months "
        "learning to read the true one')."
    ),
    # --- C3: 120 settlements vs. the locked 31 (MCD-241) ---
    "MCD-890": (
        '"The Anvil\'s Last Anchorage" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-anvils-last-anchorage.md), The Lord of Embers Alias "
        "Chronicle XLV, wave 15 of ten (waves 6-15). A closing legacy entry at the tour's final, "
        "ordinary stop, reflecting on the full eighteen-month campaign's cumulative impact, "
        "closing the ten-wave run. Corrected Batch 321, 2026-10-02: fixed a settlement-count error "
        "('a hundred and twenty' settlements repeated throughout, when the campaign's own locked "
        "total is 31, MCD-241) to 'thirty-one'/'thirty'; Efa Gol's 'a hundred and twenty thousand "
        "people' line is unchanged, since that reached-population figure is correct per MCD-241."
    ),
    # --- C4: MCD-1330 -- thirty-year gap inside an 18-month tour ---
    "MCD-1330": (
        '"The Hands That Taught the Hands" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-hands-that-taught-the-hands.md), Lord of Embers Alias "
        "Chronicle LXXXIV, wave 28, closing the wave. A generational-transmission entry distinct "
        "from MCD-1085: one of the campaign's very first apprentices, roughly sixteen months later "
        "in the same tour, is shown teaching his own apprentice -- who never met Kanja directly -- "
        "the open method intact and unweakened by second-hand transmission, confirming the "
        "doctrine's fidelity survives second-hand transmission intact within smithing itself. No "
        "new named characters. Corrected Batch 321, 2026-10-02: 'decades later' and 'a full "
        "generation deep,' impossible inside an 18-month tour, corrected to keep the old man's "
        "return visit in-tour, roughly sixteen months after the campaign's opening."
    ),
    # --- C7: Mafesto mischaracterized as forearm-scale/concealable ---
    "MCD-1499": (
        '"The Cell They Thought Would Hold Him" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-cell-they-thought-would-hold-him.md), Lord of Embers "
        "Alias Chronicle XCVII, first entry in the thirty-third wave. Rebellion era, age 27, the "
        "Rolling Foundry Campaign (MCD-241). The alias's first deliberate-capture/infiltration "
        "register: Kanja allows himself to be taken prisoner by a garrison patrol to surface the "
        "location of an illicit requisitioned-iron storehouse and its supply-officer operator, "
        "keeping Mafesto dormant through a patience-driven interrogation before a detailed, "
        "battle-intense Trinity combat showcase (Obsidian Malice's precision non-lethal discharge, "
        "Onyx of Oblivion's Whisper of Shadows and Veil Piercer, Mafesto grounded and current "
        "again) carries the corridor-breach escape. The storehouse's iron is recovered and its "
        "falsified ledger convicts the supply officer. Garren Hask (CC-115) appears in his "
        "established ledger-cross-checking role. No new named characters. Corrected Batch 321, "
        "2026-10-02: Mafesto is a full bio-bonded exoskeleton, not forearm-scale gear; reworded so "
        "it's worn inert across Kanja's frame and read by the guards as ordinary plate armor, "
        "rather than held 'against his forearm.'"
    ),
    "MCD-1501": (
        '"What They Built From What They Saw" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-they-built-from-what-they-saw.md), Lord of Embers "
        "Alias Chronicle XCIX, wave 33, closing the wave. Rebellion era, age 27, the Rolling "
        "Foundry Campaign (MCD-241). A detailed, battle-intense Trinity combat showcase and a new "
        "villain-side-research register for the alias: a Directorate engineer builds a crude "
        "reverse-engineered imitation of Mafesto's Kinetic Transfer System from external "
        "observation alone, which catastrophically shatters its own wearer's ribs on first use by "
        "feeding a blow's full charge directly into him rather than grounding it through a "
        "calibrated frame. Obsidian Malice's discharge and Onyx of Oblivion's Whisper of Shadows "
        "deny the observing engineer his notes before he can destroy or transmit them; Garren Hask "
        "(CC-115) catalogues the confiscated notebook's contents before it is burned. Distinct from "
        "the counterfeit-guild-mark arms race (MCD-1084/MCD-1316) and the doctrine-theft entry "
        "(MCD-922). No new named characters. Closes the Lord of Embers' thirty-third "
        'three-Chronicle wave (with "The Cell They Thought Would Hold Him," MCD-1499, and "What '
        'the Smoke Said," MCD-1500). Corrected Batch 321, 2026-10-02: Mafesto is a full bio-bonded '
        "exoskeleton, not forearm-scale; the Directorate's crude copy reworded from a forearm "
        "harness to a partial chest-and-shoulder harness, and its failure reworded from shattering "
        "an arm to shattering ribs, consistent with where the harness now sits."
    ),
    # --- E1: Chronicle numbering -- MCD-500/501/502 (XIII/XIV/XV -> X/XI/XII) ---
    "MCD-500": (
        '"What Didn\'t Come Back This Time" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-didnt-come-back-this-time.md), the Lord of Embers "
        "Alias Chronicle X, first entry in the fourth wave. A third punitive burning finally "
        "outpaces the campaign's stretched salvage and marginal-ore resources; the settlement "
        "forge is not rebuilt and the settlement relocates instead, the first genuine, honestly "
        "acknowledged limit of 'metabolizes punishment' across every prior register. No new named "
        "characters. Renumbered Batch 321, 2026-10-02: was mislabeled Chronicle XIII, leaving a "
        "gap at X-XII while duplicating no other entry; corrected to X."
    ),
    "MCD-501": (
        '"The Saboteur Among the Apprentices" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-saboteur-among-the-apprentices.md), the Lord of Embers "
        "Alias Chronicle XI. A detailed detection-and-combat showcase: a Directorate infiltrator "
        "embedded among The Anvil's apprentices plants a slow structural sabotage; Kanja catches "
        "the wrongness in the beam's resonance and patiently traces it to its source over a full "
        "day before confronting and restraining the infiltrator, the threat coming from within the "
        "cohort rather than an external raid. No new named characters. Renumbered Batch 321, "
        "2026-10-02: was mislabeled Chronicle XIV; corrected to XI."
    ),
    "MCD-502": (
        '"The Smith They Said Couldn\'t Be One" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-smith-they-said-couldnt-be-one.md), the Lord of Embers "
        "Alias Chronicle XII, closing the fourth wave. A woman rejected by every conventional "
        "smithing guild purely on grounds of sex finds work judged on merit alone at The Anvil, "
        "extending the forge's meritocratic ethos into active confrontation with exclusionary "
        "guild practice. No new named characters. Closes the Lord of Embers' fourth three-Chronicle "
        "wave (with 'What Didn't Come Back This Time,' MCD-500, and 'The Saboteur Among the "
        "Apprentices,' MCD-501). Renumbered Batch 321, 2026-10-02: was mislabeled Chronicle XV; "
        "corrected to XII."
    ),
    # --- E1: Chronicle numbering -- MCD-552/553/554 (XVI/XVII/XVIII -> XIII/XIV/XV) ---
    "MCD-552": (
        '"The Night All Five Forges Burned at Once" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-night-all-five-forges-burned-at-once.md), the Lord of "
        "Embers Alias Chronicle XIII, first entry in the fifth wave. A detailed, large-scale combat "
        "showcase: a coordinated Directorate assault hits five linked forge sites simultaneously, "
        "and Kanja moves between all five within a single hour using Mafesto's converted charge, "
        "Obsidian Malice, and Onyx of Oblivion, none of the sites falling. No new named characters. "
        "Renumbered Batch 321, 2026-10-02: was mislabeled Chronicle XVI, duplicating 'The Crew That "
        "Rebuilt Without Him'; corrected to XIII, the numeral freed by MCD-500's own correction."
    ),
    "MCD-553": (
        '"The Smith Who Built Their Weapons" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-smith-who-built-their-weapons.md), the Lord of Embers "
        "Alias Chronicle XIV. A captured Directorate smith who forged the siege engines that killed "
        "rebel fighters is offered work rather than punishment, testing 'metabolizes punishment' "
        "against a skilled enemy craftsman rather than only civilians or economic pressure, over "
        "the crew's own genuine anger. No new named characters. Renumbered Batch 321, 2026-10-02: "
        "was mislabeled Chronicle XVII, duplicating 'What the Floodwater Couldn't Take'; corrected "
        "to XIV."
    ),
    "MCD-554": (
        '"What the Old Smith Saw in the Ashes" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-old-smith-saw-in-the-ashes.md), the Lord of Embers "
        "Alias Chronicle XV, closing the fifth wave. The campaign's recurring senior smith (first "
        "referenced in MCD-456) finds Kanja alone at the forge the night after the five-site "
        "attack, witnessing the private toll behind the reputation for the first time. No new "
        "named characters. Closes the Lord of Embers' fifth three-Chronicle wave (with 'The Night "
        "All Five Forges Burned at Once,' MCD-552, and 'The Smith Who Built Their Weapons,' "
        "MCD-553). Renumbered Batch 321, 2026-10-02: was mislabeled Chronicle XVIII, duplicating "
        "'The Engineer Who Came to Disprove Him'; corrected to XV. Also corrected: the senior "
        "smith's citation (MCD-456, her actual first appearance at wave 3, not MCD-502's later wave "
        "4) and 'decades of quiet trust' (impossible at age 27 inside an 18-month tour) to 'months "
        "of quiet trust.'"
    ),
    # --- E9: MCD-1328's successor-establishment citation ---
    "MCD-1328": (
        '"The Weeks the Method Stood Alone" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-weeks-the-method-stood-alone.md), Lord of Embers Alias "
        "Chronicle LXXXII, first entry in the twenty-eighth wave. Kanja is incapacitated by a real, "
        "non-fatal structural-collapse injury for three weeks; the campaign does not stop, the "
        "senior smith's successor (established across MCD-887/MCD-923, running the floor "
        "independently since MCD-1312) and a nearby rebuild completing on schedule without him, "
        "the clearest proof yet that the method outlasts its own founder's physical presence. No "
        "new named characters. Corrected Batch 321, 2026-10-02: fixed the successor's "
        "establishment citation to MCD-887/MCD-923 (not MCD-1312, a later, unrelated entry); "
        "stripped a leaked inline rule-ID citation and writers'-room phrasing from the narrative "
        "prose; and fixed a stale 'planned as the same wave's second entry' note to cite MCD-1329 "
        "directly, now that it's written."
    ),
    # --- E7: MCD-1334's "sustained years of service" ---
    "MCD-1334": (
        '"What the Anvil Needed From Itself" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-anvil-needed-from-itself.md), Lord of Embers Alias "
        "Chronicle LXXXVIII, first entry in the thirtieth wave. The alias's first base-maintenance "
        "entry: a hull survey after a year and more of converted service -- atop whatever wear the "
        "hull already carried from its years as an ore-hauler before the campaign ever claimed it "
        "-- and a sea storm prompts a deliberate three-week proactive refit of The Anvil itself, "
        'extending "metabolizes punishment"\'s rebuild ethos into ordinary preventive upkeep '
        "rather than crisis response. No new named characters. Corrected Batch 321, 2026-10-02: "
        "'sustained years of service,' impossible for an 18-month tour, now attributes older wear "
        "to the barge's pre-conversion years as an ore-hauler; and stripped a leaked inline "
        "rule-ID citation from the narrative prose."
    ),
    # --- E4: MCD-1500's mistaken Forge-Coat/Smoke System framing ---
    "MCD-1500": (
        '"What the Smoke Said" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-smoke-said.md), Lord of Embers Alias Chronicle "
        "XCVIII, wave 33. Rebellion era, age 27, the Rolling Foundry Campaign (MCD-241). A "
        "genuinely new logistics/communication register: Callum Breck proposes a standardized "
        "smoke-signal relay code across the campaign's linked forge sites for early warning, built "
        "from the campaign's own forge chimneys rather than any gear system. The code is tested "
        "within a week when a site's hourly all-clear pulse goes silent with no raid signal ahead "
        "of it -- the deliberately built silent-pulse protocol, not an active signal, is what "
        "actually saves three apprentices buried by a support collapse, reaching them in two hours "
        "rather than the half-day a rider would need. No new named characters. Corrected Batch "
        "321, 2026-10-02: removed a mistaken claim that the chimney code repurposes the "
        "Forge-Coat's Smoke System (MCD-291-293) -- that gear doesn't exist until the Long Mask, "
        "ages 33-284 -- recast as a plain, un-gear-cited chimney-signal code, matching the "
        "narrative, which never claimed otherwise."
    ),
    # --- E8: MCD-969's "Toma" collision with the already-locked Tomas Grieve ---
    "MCD-969": (
        '"What the Forge Carved in Memory" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-forge-carved-in-memory.md), The Lord of Embers "
        "Alias Chronicle XLIX, wave 17. An apprentice dies of illness, no enemy, no raid, nothing "
        "to rebuild. The floor's method has no answer for a cough; Kanja forges a plain, unmarked "
        "hinge in the boy's memory instead. First entry to confront loss with no adversary at all. "
        "Corrected Batch 321, 2026-10-02: the deceased apprentice's name, originally 'Toma,' "
        "collided with the already-locked Tomas Grieve (MCD-093/CC-124); renamed to Ilo "
        "(collision-checked clean against the live ledger) -- a minor new named character who does "
        "not appear on-page alive."
    ),
}

for rid, new_statement in AMENDMENTS.items():
    assert rid in rules_by_id, f"Unknown rule ID: {rid}"
    rules_by_id[rid]["statement"] = new_statement

ledger["batches_completed"].append({
    "batch": 330,
    "date": str(date.today()),
    "source": SOURCE,
    "rule_count": 0,
    "note": (
        "Reconciliation pass following a read-only review of the Lord of Embers Alias Chronicle "
        "corpus (102 entries). Fixed: a Trinity-era anachronism (MCD-1322's damaged item rewritten "
        "from the Forge-Coat's Dark-Drakma leather, gear that doesn't exist until age 33, to "
        "Mafesto's own Void-Lattice plating, live at age 27, with the file retitled 'What Mafesto "
        "Couldn't Shed'); chronology compression across an 18-month tour softened throughout "
        "(MCD-1052, MCD-423, MCD-1050, MCD-1333, MCD-1084 -- 'eighteen months'/'years'/'decades' "
        "reduced to 'months'/'a year'/'sixteen months' where entries sit mid-tour, and MCD-1052's "
        "misattributed 'we already did that, years back' line corrected to reference the itinerant "
        "master smith's judged contest, MCD-921); a settlement-count error (MCD-890's '120 "
        "settlements' corrected to the locked 31, MCD-241, with Efa Gol's correct '120,000 people' "
        "line left untouched); a 30-year gap inside the same tour (MCD-1330's old man rewritten as "
        "a first-stop apprentice revisited roughly sixteen months later, in-tour); a header era "
        "contradiction (MCD-457 re-eraed from an impossible 'age 27, several years after' an "
        "age-27 event to the Long Mask); a training-span mismatch (MCD-1312's 'six years' matched "
        "to MCD-887's 'the last several months'); Mafesto mischaracterized twice as forearm-scale/"
        "concealable gear rather than a full bio-bonded exoskeleton (MCD-1499, MCD-1501); a "
        "Chronicle-numbering collision (MCD-500/501/502 renumbered XIII/XIV/XV -> X/XI/XII, "
        "freeing those numerals for MCD-552/553/554, themselves renumbered XVI/XVII/XVIII -> "
        "XIII/XIV/XV, resolving duplicate numerals against 'The Crew That Rebuilt Without Him,' "
        "'What the Floodwater Couldn't Take,' and 'The Engineer Who Came to Disprove Him'); five "
        "leaked inline rule-ID citations and writers'-room phrasing stripped from narrative prose "
        "(MCD-1313, MCD-1314, MCD-1328, MCD-1334, MCD-1335) in favor of the in-world references "
        "already present in the same sentences; four 'than any prior showcase'/'across prior "
        "entries' writers'-room phrasings reworded to plain prose (MCD-1326, MCD-1329, MCD-1332, "
        "MCD-1497); two stale continuity-note references to planned-but-now-written entries "
        "corrected to cite the finished Chronicles directly (MCD-1310 -> MCD-1327, MCD-1328 -> "
        "MCD-1329); a mistaken Forge-Coat/Smoke System framing removed from a chimney-signal-code "
        "entry that never needed it (MCD-1500); a Mafesto gear citation corrected from 'the coat's "
        "whole vocabulary' to 'Mafesto's whole vocabulary' (MCD-1083); a proper-noun collision "
        "(MCD-969's deceased apprentice renamed from 'Toma' to 'Ilo,' clear of the already-locked "
        "Tomas Grieve, MCD-093/CC-124); three stale wave-establishment citations for the recurring "
        "senior smith corrected from 'wave 14' to waves 3-5/MCD-456/MCD-502/MCD-554 (MCD-969, "
        "MCD-974, MCD-977, the last of which also picks up its own citation fix to MCD-456 above); "
        "two typos (MCD-873 'a exhausted body' -> 'an exhausted body'; MCD-1324's dropped-word "
        "sentence reworded); one clarity fix (MCD-922's ambiguous opening line reworded to make "
        "clear the garrison is a Directorate installation Kanja's own scouts burned); and a stale "
        "tracker count (chronicle-tracks-status.md's Lord of Embers row, 93 -> 102). All fixes are "
        "prose-level reconciliation against already-locked canon or internal corpus consistency -- "
        "no new creative facts beyond MCD-969's renamed minor character, matching the Batch "
        "226/68/320 precedent. The affected Chronicle `.md` files were corrected directly as prose/"
        "header edits in a companion pass; this script only amends the matching ledger rule "
        "statements."
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
