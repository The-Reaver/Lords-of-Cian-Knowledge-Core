#!/usr/bin/env python3
"""Batch 321: corrections surfaced by a read-only review pass on the Trench Monarch Alias Chronicle
track (102 entries). Fixes the three earliest crew members' (Corren Halst, Danne Sok, Maret Vos)
origin story to match the already-locked manuscript account (Chronicle III, Batch 70) -- Maw
survivors who found each other on the docks before finding Kanja, not freed by his own hand -- plus
a Garren Hask recruitment misattribution, a kill-count contradiction with the "no killing" doctrine,
a Tavin Greer allegiance slip, a Dol Maren plank-bridge timeline error, and a set of mechanical
errors (a proper-noun collision, wrong citations, garbled sentences, an impossible timespan, an
anachronistic ability attribution, writers'-room leaks, a stale geography claim, and a stale
tracker count). No new creative facts beyond the new CC-160 dossier and the CC-158/159 origin-clause
amendments -- pure reconciliation against already-locked canon, matching the Batch 226/68/320
precedent. The affected Chronicle `.md` files were corrected directly as prose edits in a companion
pass; this script only amends the matching ledger rule statements and locks the new/amended CC-
rules."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Read-only review pass (Trench Monarch Alias Chronicle corpus), reconciliation pass, 2026-10-02"

with open(LEDGER_PATH) as f:
    ledger = json.load(f)

rules_by_id = {r["id"]: r for r in ledger["rules"]}

# --- Amend rule statements to match the corrected Chronicle prose ---
AMENDMENTS = {
    # --- C2: Halst/Sok/Vos origin story -- Maw survivors who found each other on the docks, not
    # freed by Kanja's own hand, matching the manuscript's own locked account (Chronicle III,
    # Batch 70: "three fighters who had found each other on the docks before they found Kanja").
    "MCD-533": (
        '"What Maret Vos Carried From Before" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-maret-vos-carried-from-before.md), Trench Monarch Alias "
        "Chronicle XV, closing the fifth wave. Maret Vos (already locked, one of the three earliest "
        "crew members, all Maw survivors who found each other on the docks before finding Kanja, "
        "`MCD-234`) finally shares his own account of those days -- quieter and less dramatized than "
        "Corren Halst's (`MCD-436`) or Danne Sok's (`MCD-530`), completing a trilogy of early-crew "
        "perspectives on the man before any alias existed. No new named characters beyond the "
        "already-locked Maret Vos. Closes the Trench Monarch's fifth three-Chronicle wave (with 'The "
        "Table Across from the Owners,' `MCD-531`, and 'The Hunt for One Man,' `MCD-532`). Corrected "
        "Batch 321, 2026-10-02: the original draft wrongly had Vos 'freed by Kanja's own hand' -- "
        "reworded to match the manuscript's own locked account (Chronicle III, Batch 70) and "
        "`MCD-234`: a Maw survivor who found Halst and Sok on the docks, then found Kanja."
    ),
    "MCD-641": (
        '"The Blow Danne Sok Took Without a Word" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-blow-danne-sok-took-without-a-word.md), The Trench "
        "Monarch Alias Chronicle XXXVI, wave 12 of the ten-wave sixth-through-fifteenth run. Danne "
        "Sok silently takes a chain-strike meant for Kanja, a wordless-loyalty register complementing "
        "his separately-closed spoken account (`MCD-530`). Corrected Batch 321, 2026-10-02: the "
        "original draft wrongly had Sok 'freed by Kanja' -- reworded to 'before he found Kanja,' "
        "matching the manuscript's own locked account (Chronicle III, Batch 70) and `MCD-234`: Sok is "
        "a Maw survivor who found Halst and Vos on the docks, then found Kanja, not freed by his hand."
    ),
    "MCD-1137": (
        '"What Corren Halst Never Told the Others" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-corren-halst-never-told-the-others.md), Trench Monarch "
        "Alias Chronicle LXXX, wave 27. Rebellion era, pre-Black-Trench. Corren Halst's own dedicated "
        "origin entry -- the last of the founding four without one. Reveals he was freed once before, "
        "from one of the Maws, by a rebellion cell that collapsed to internal betrayal; made his way "
        "to the docks afterward, found Danne Sok and Maret Vos there (two other Maw survivors with "
        "the same hard-earned caution), and the three of them together observed Kanja's crew for "
        "three weeks before approaching, ultimately trusting Garren Hask's meticulous, cross-witnessed "
        "ledger before trusting Kanja himself. No new named characters beyond the already-locked "
        "Corren Halst. Second entry in the Trench Monarch's twenty-seventh wave. Corrected Batch 321, "
        "2026-10-02: the original draft said he was freed from a 'work-camp' and placed his three-"
        "weeks observation of the crew before he'd found Halst and Sok on the docks -- reworded so "
        "the prior rescue is from one of the Maws (matching `MCD-234`'s Maw-survivor framing) and the "
        "observation period happens after the three of them had already found each other there, "
        "matching the manuscript's own locked account (Chronicle III, Batch 70)."
    ),
    # --- C3: Garren Hask's recruitment misattributed to a post-Dredge-Line Silt Row tally ---
    "MCD-623": (
        '"What Garren Hask Wrote Down First" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-garren-hask-wrote-down-first.md), The Trench Monarch "
        "Alias Chronicle XVIII, wave 6 of the ten-wave sixth-through-fifteenth run. Rebellion era, "
        "before the Dredge-Line Ambush. Not Hask's recruitment -- that happened earlier, at the "
        "Scrip-Forge Raid's Forge-7 evidence (`CC-115`) -- but the moment he formally takes over the "
        "crew's ledger-keeping role: his own pre-crew habit of independently cross-checking the "
        "Trench Monarch's figures is what earns him the job, grounding the later trust in his books "
        "in a concrete founding moment. No new named characters beyond the already-locked Garren "
        "Hask. Closes the Trench Monarch's sixth three-Chronicle wave. Corrected Batch 321, "
        "2026-10-02: the original draft wrongly staged this as Hask's first meeting with Kanja and a "
        "recruitment scene, contradicting `CC-115`'s already-locked Forge-7 recruitment; reframed as "
        "a promotion/responsibility moment set before the Dredge-Line Ambush, and the erroneous "
        "'thirty-one-year-old' age reference (31 is his tenure, not his age) corrected to 53, "
        "matching `CC-115`/Batch 48."
    ),
    # --- C4: Dredge-Line kill count contradicting the "no killing" doctrine ---
    "MCD-1129": (
        '"The Summer the Canal Went Dry" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-summer-the-canal-went-dry.md), Trench Monarch Alias "
        "Chronicle LXXII, wave 24, closing the wave. Rebellion era, pre-Black-Trench. A drought "
        "empties the founding canal to a cracked silt bed, the first entry deliberately inverting the "
        "water-and-flood motif that dominates the alias's prior Chronicles -- Dol Maren's plank-"
        "bridges stand over nothing, and an owner exploits the resulting wagon-traffic bottleneck to "
        "divert goods out of sight. Garren Hask adapts the tally method to wagon manifests and "
        "wheel-rut counts, catching the diversion through documentation alone, no combat or Onyx use. "
        "No new named characters -- the diverting owner is unnamed. Closes the Trench Monarch's "
        "twenty-fourth wave (with 'What the Blade Remembered Before Him,' `MCD-1127`, and 'The Man "
        "They Punished for Standing Near Him,' `MCD-1128`). Corrected Batch 321, 2026-10-02: the "
        "original draft's opening line claimed the canal 'had drowned two hundred soldiers the year "
        "before,' contradicting `MCD-231`'s own locked framing (the flood drowned the punitive "
        "column's density advantage in industrial sludge, not a literal 200-person death toll) and "
        "Kanja's established no-killing doctrine -- reworded to 'had broken the column's advantage.' "
        "A second line quoting a later Chronicle's own title in-world ('the \"Line That Wouldn't "
        "Break\" kind of defense') was also reworded to plain in-world phrasing."
    ),
    # --- C5: Tavin Greer's allegiance -- fixed to stay consistently Directorate-side ---
    "MCD-644": (
        '"What Tavin Greer Taught the Next Clerk" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-tavin-greer-taught-the-next-clerk.md), The Trench Monarch "
        "Alias Chronicle XXXIX, wave 13 of the ten-wave sixth-through-fifteenth run. Greer -- an "
        "active Directorate officer who never claims credit (`MCD-1131`, `MCD-403`) -- passes the "
        "founding instinct behind trust-verification to a newly posted Trust records clerk, the "
        "method institutionalizing on the Directorate's own side of the line rather than inside the "
        "crew's structure. Corrected Batch 321, 2026-10-02: the original draft had the new clerk "
        "'assigned to the five-district cross-checking work' as if embedded in the rebellion's own "
        "apparatus, contradicting Greer's consistently Directorate-side allegiance; reworded to a "
        "Trust records clerk."
    ),
    # --- C6: Dol Maren's plank-bridges built at the ambush itself, not afterward ---
    "MCD-1123": (
        '"What Dol Maren Built to Fail Safely" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-dol-maren-built-to-fail-safely.md), Trench Monarch Alias "
        "Chronicle LXVI, wave 22, closing the wave. Rebellion era, pre-Black-Trench. Dol Maren's "
        "first dedicated Trench-Monarch-era solo entry: one of his seventeen plank-bridges (`CC-121`) "
        "fails under an unexpectedly heavy Compliance requisition wagon, but fails exactly as "
        "designed -- sacrificial support beams letting go first, tipping the wagon safely into the "
        "canal rather than collapsing the span under the workers crossing it. Establishes his "
        "engineering philosophy of designing structures to fail predictably and safely, the direct "
        "origin of the load-assessment competence he later carries into shipwright work. No new "
        "named characters -- the wagon's two drivers are unnamed. Closes the Trench Monarch's "
        "twenty-second wave (with 'What the Charter Actually Said,' `MCD-1121`, and 'What Whisper of "
        "Shadows Was For,' `MCD-1122`). Corrected Batch 321, 2026-10-02: the original draft said the "
        "seventeen bridges were built 'in the weeks after the flood' -- reworded to match `CC-121`'s "
        "own lock that Maren built and load-tested them at the Dredge-Line Ambush itself."
    ),
    # --- E1: proper-noun collision -- "Vask" renamed to avoid Lauris's Karesian institutional term ---
    "MCD-627": (
        '"The Old Hand Who Wouldn\'t Kneel to a Boy" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-old-hand-who-wouldnt-kneel-to-a-boy.md), The Trench "
        "Monarch Alias Chronicle XXII, wave 8 of the ten-wave sixth-through-fifteenth run. A "
        "veteran's doubt about following 'a boy' is won over through humility and public "
        "self-correction, not authority. No new named characters. Corrected Batch 321, 2026-10-02: "
        "the veteran was originally named 'Ondrej Vask,' colliding with Lauris Letitia's own locked "
        "Karesian institutional term (Vask Karth-Ven and related usages); renamed to Ondrej Kessler, "
        "collision-checked clean."
    ),
    "MCD-637": (
        '"The Challenge He Wouldn\'t Answer With Steel" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-challenge-he-wouldnt-answer-with-steel.md), The Trench "
        "Monarch Alias Chronicle XXXII, wave 11 of the ten-wave sixth-through-fifteenth run. An "
        "honest rival's dominance-duel challenge, from a named loading-trade rival, Ruven Calx, is "
        "declined in favor of a public transparency contest, subverting genre expectation. One new "
        "named character -- Ruven Calx, collision-checked clean. Corrected Batch 321, 2026-10-02: "
        "the rule statement previously omitted Ruven Calx, who the Chronicle's own prose already "
        "names; statement updated to note him."
    ),
    # --- E2: wrong citations ---
    "MCD-1029": (
        '"The Lie Told in His Name" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-lie-told-in-his-name.md), The Trench Monarch Alias "
        "Chronicle LVIII, wave 20. A seventeen-year-old clerk at a rival tally operation falsely "
        "confesses to skimming wages, invoking the Trench Monarch's name and claiming the crew's "
        "protection, to shield his mother -- the actual, desperate skimmer -- from an owner's "
        "retaliation. Garren Hask's tally records disprove the confession's shift pattern and trace "
        "the true source; Kanja resolves it through the established method, negotiating restitution "
        "through labor rather than punishment once the shortfall is shown to match exactly the cost "
        "of medicine. Tells the boy the impulse to protect his mother needs no apology, but that the "
        "name isn't a coat to be borrowed without asking. First genuinely sympathetic (rather than "
        "malicious or profit-driven) misuse of the reputation shown in the sub-series -- prior 'lies "
        "told under his name' were malicious (the impersonator's extortion, `MCD-401`) or "
        "profit-motivated (the bribery slander campaign, `MCD-624`). No new named characters -- the "
        "clerk, his mother, and the owner are unnamed. First entry in the Trench Monarch's twentieth "
        "wave. Corrected Batch 321, 2026-10-02: the prior-entries citation wrongly pointed to "
        "`MCD-449` (an unrelated Crow King entry); corrected to `MCD-624`, the actual bribery slander "
        "campaign Chronicle."
    ),
    "MCD-1127": (
        '"What the Blade Remembered Before Him" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-blade-remembered-before-him.md), Trench Monarch Alias "
        "Chronicle LXX, wave 24. Rebellion era, pre-Black-Trench. A rare private, wordless exchange "
        "between Kanja and Onyx of Oblivion clarifies Soulbound Edge (`ARS-020`) as a renewable, "
        "revocable bond rather than possession -- distinct from Mafesto's forged-and-bonded "
        "relationship (`ARS-010`/`MCD-232`) -- the blade carries an unspecified centuries-deep "
        "history of prior wielders, including one whose bond it ended on its own terms for asking it "
        "to be a weapon it would not agree to be. No combat, no new named characters. First entry in "
        "the Trench Monarch's twenty-fourth wave. Corrected Batch 321, 2026-10-02: the original draft "
        "cited `MCD-291` (an unrelated Bio-Drakma mechanic) for Mafesto's forged-and-bonded "
        "relationship; corrected to `ARS-010`/`MCD-232`. Also removed an ungrounded in-scene "
        "comparison to Varruk's 'Angle-Whisper' ability (`CC-051`/`098`), which age-18 Kanja has no "
        "basis to reference; reworded to plain description."
    ),
    "MCD-1436": (
        '"What Callum Breck Carried Home at Night" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-callum-breck-carried-home-at-night.md), Trench Monarch "
        "Alias Chronicle XCVII, wave 33, first entry. Rebellion era, pre-Black-Trench, before Breck's "
        "silence arc (`CC-119`). A dedicated Callum Breck personal-life register, distinct from his "
        "already-locked coining-the-name origin (`MCD-368`) and his later reflection entry "
        "(`MCD-632`): Kanja walks Breck's nightly route home and witnesses the plain, unremarkable "
        "domestic life -- his established wife (unnamed, `CC-117`) and infant daughter Sera "
        "(`CC-117`) -- that the war and the name he coined have nothing to do with. No new named "
        "characters -- Breck's wife is deliberately kept unnamed, matching `CC-117`. First entry in "
        "the Trench Monarch's thirty-third wave. Corrected Batch 321, 2026-10-02: the header wrongly "
        "listed a second, bogus cross-reference ('MCD-403-adjacent') -- `MCD-403` is a Tavin Greer "
        "entry, not a Breck one; removed, leaving the one correct citation, `MCD-632`."
    ),
    # --- E3: Pell Ostra third-person self-reference + Coldrace accelerant claim ---
    "MCD-650": (
        '"The Name They Carried Into the Water" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-name-they-carried-into-the-water.md), The Trench Monarch "
        "Alias Chronicle XLV, wave 15 of the ten-wave sixth-through-fifteenth run. Efa Gol and Pell "
        "Ostra's joint reflection on the eve of the Black Trench closes the full fifteen-wave, "
        "forty-five-Chronicle run. Corrected Batch 321, 2026-10-02: Pell Ostra's own line wrongly "
        "referred to herself in the third person ('Ostra's already spent...') and cited 'accelerant "
        "work at Coldrace,' contradicting `MCD-648`'s own lock that the Coldrace site was a "
        "straightforward wage correction settled without incident; reworded to a first-person line "
        "about charge-prep for the coming battle, with the Coldrace reference removed."
    ),
    # --- E4: "two weeks"/"fortnight" vs. "three weeks" ---
    "MCD-944": (
        '"The Three Weeks He Wasn\'t There" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-two-weeks-he-wasnt-there.md), The Trench Monarch Alias "
        "Chronicle LI, wave 17. Reframes the two prior entries as one three-week stretch in which "
        "Halst, Sok, and Vos ran three sites entirely independently while Kanja was incapacitated -- "
        "the first dramatization of the method surviving its own originator's total absence. Closes "
        "wave 17. Corrected Batch 321, 2026-10-02: the title and several body references said "
        "'two weeks'/'fortnight' while other body text already said 'three weeks' -- made consistent "
        "throughout at three weeks, matching the majority usage (the file's path is unchanged)."
    ),
    # --- E5: Callum Breck age reference ---
    "MCD-1147": (
        '"What the Districts Kept After Him" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-districts-kept-after-him.md), Trench Monarch Alias "
        "Chronicle XC, wave 30, closing the wave. Rebellion era, pre-Black-Trench. An ensemble "
        "closer, explicitly not a restaging of `MCD-650`'s already-locked 'eve of the Black Trench' "
        "closing beat (Efa Gol and Pell Ostra's joint reflection, which formally closed the "
        "fifteen-wave run at the time) -- this entry is set at an unspecified, ordinary point in the "
        "era rather than the battle's immediate eve, and centers the method's accumulated "
        "self-sufficiency (every site running without Kanja's direct involvement) rather than any "
        "foreboding of the coming battle specifically. Reuses the full established roster of "
        "pre-Black-Trench crew (Corren Halst, Danne Sok, Maret Vos, Garren Hask, Callum Breck, Efa "
        "Gol, Pell Ostra) in brief, unremarkable moments of their own. No new named characters. "
        "Closes the Trench Monarch's thirtieth wave (with 'What the Auditors Never Found,' "
        "`MCD-1145`, and 'What Garren Hask Packed That Week,' `MCD-1146`) and the full run of nine "
        "waves, 22 through 30. Corrected Batch 321, 2026-10-02: a garbled sentence described Callum "
        "Breck as 'four years older than the boy who had chalked three words on a captured officer's "
        "forehead' -- corrected to read 'four years older than Kanja,' per `CC-117`."
    ),
    # --- E6: impossible "three years of Onyx-work" pre-Black-Trench ---
    "MCD-900": (
        '"The Wall That Wouldn\'t Hold Itself" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-wall-that-wouldnt-hold-itself.md), The Trench Monarch "
        "Alias Chronicle XLVI, wave 16. A storm collapses a canal retaining wall above forty "
        "families' homes at Warrow Bend. Pure disaster relief with no adversary and no Onyx use at "
        "all -- Kanja and the earliest crew spend two days doing raw physical labor to shore the "
        "wall by hand, extending the 'digging his own crown' ethos to nature and exhaustion, not "
        "just human opposition. Corrected Batch 321, 2026-10-02: the closing line claimed his hands "
        "were raw in a way 'three years of Onyx-work' had never left them -- impossible this early "
        "in the pre-Black-Trench era, since Onyx bonds at seventeen (`ARS-020`) and at most roughly "
        "two years have passed by this point; corrected to 'a year or more.'"
    ),
    # --- E7: "years before"/"would open"/Scrip-Forge wording ---
    "MCD-629": (
        '"What Pell Ostra Kept Safe" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-pell-ostra-kept-safe.md), The Trench Monarch Alias "
        "Chronicle XXIV, wave 8 of the ten-wave sixth-through-fifteenth run. Origin vignette: Pell "
        "Ostra's first self-directed use of fire/materials instinct to save records from a raid. "
        "Corrected Batch 321, 2026-10-02: the opening line said 'years before' the Black Trench "
        "(actually months away) and that her future charges 'would open' the ravine (`MCD-232` locks "
        "it as sealed, not opened); also garbled her Ash-Wharf role as 'scaling the Scrip-Forge "
        "stockpile' rather than `CC-133`'s own account (scaling the Scrip-Forge Raid's accelerant to "
        "detonate the Dead Drakma stockpile). All three corrected to match."
    ),
    # --- E8: "fourteen names" vs. MCD-1031's sixteen students ---
    "MCD-1435": (
        '"The Ledger He Taught Somewhere Else" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-ledger-he-taught-somewhere-else.md), Trench Monarch Alias "
        "Chronicle XCVI, wave 32, closing the wave. Rebellion era, pre-Black-Trench. The tally "
        "method's first successful independent replication: a trained graduate of Warehouse Twelve's "
        "classes (first named in `MCD-1031`) carries the verification discipline, deliberately "
        "stripped of the Trench Monarch name and reputation, to a distant granary town on her own "
        "initiative and with Kanja's blessing, succeeding where `MCD-947`'s earlier distant imitation "
        "(which copied the method's form without its rigor) failed and ruined an innocent owner. No "
        "new named characters -- the graduate, her cousin's husband, and the granary owner are all "
        "unnamed. Closes the Trench Monarch's thirty-second wave. Corrected Batch 321, 2026-10-02: "
        "the original draft said she was 'one of the first fourteen names' on Hask's attendance "
        "sheet, implying only fourteen students total; `MCD-1031` locks fourteen as the number of "
        "original requests and sixteen as the number who actually trained -- reworded to clarify she "
        "was one of the fourteen original requesters, one of sixteen who sat for the course."
    ),
    # --- E9: writers'-room/meta leaks ---
    "MCD-480": (
        '"The Line That Wouldn\'t Break" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-line-that-wouldnt-break.md), Trench Monarch Alias "
        "Chronicle XI. Rebellion era, age 18, before the Black Trench. New standalone material -- a "
        "detailed solo-blade combat showcase per Abad's craft instruction, distinct from 'What the "
        "Sword Remembers' (`MCD-369`) in focusing on defending others under fire rather than a "
        "powers demonstration. No new named characters. Corrected Batch 321, 2026-10-02: a line "
        "described the fight as not matching 'the clean, decisive powers showcase the line had heard "
        "about from the Warehouse Twelve stories' -- a writers'-room-flavored meta reference (and a "
        "mild anachronism, since Warehouse Twelve's own training-hub role is established much later, "
        "wave 20); reworded to plain in-world phrasing with no specific-source attribution."
    ),
    # --- E10: "Kessic flats" false new-geography claim ---
    "MCD-1062": (
        '"What He Owed Outside the Ledger" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-he-owed-outside-the-ledger.md), The Trench Monarch Alias "
        "Chronicle LXI, wave 21, first entry. Rebellion era, pre-Black-Trench. A cost of the alias's "
        "own founding battle that no tally can repay. Months after the Dredge-Line Ambush "
        "(`MCD-231`), a woman whose family's sixty-year grafted orchard on the Kessic flats was "
        "salt-killed by the same flood comes to Warehouse Twelve, not disputing that the flood was "
        "necessary, but pointing out that unlike every wage theft the tally method has ever "
        "corrected, her loss was never entered on any ledger at all. The established restitution "
        "method finds no purchase; Kanja offers his crew's labor toward reclamation across seasons "
        "while explicitly naming it insufficient, and writes the loss down himself on a page with no "
        "owner's name and no repayment schedule, signed with his own name rather than the alias. "
        "First entry in the sub-series to hold the founding battle itself accountable for collateral "
        "cost, and the first to close without the tally-verification method (`MCD-231`) providing a "
        "clean resolution. No new named characters -- the woman is unnamed, and Garren Hask (already "
        "locked) appears in his established ledger-keeper role. First entry in the Trench Monarch's "
        "twenty-first wave. Corrected Batch 321, 2026-10-02: the continuity note wrongly claimed "
        "'Kessic flats' was new, unclaimed geography with no existing ledger hit; 'Kessic' is already "
        "an established region name elsewhere in the Chronicle corpus (the Kessic Overwatch/Wardline "
        "installations) -- corrected to note the flats sit within that same broader region, still not "
        "claimed as a settlement, Hold, or Atlas-tracked location in its own right."
    ),
    # --- E11: Whisper of Shadows misattributed a structural/door-opening effect ---
    "MCD-1439": (
        '"The Night They Took Him Instead" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-night-they-took-him-instead.md), Trench Monarch Alias "
        "Chronicle C, wave 34, first entry. Rebellion era, pre-Black-Trench -- Onyx of Oblivion solo, "
        "Mafesto dormant and Obsidian Malice undeployed (`MCD-232`). The alias's first genuine "
        "capture-and-escape register: a thrown sack of quicklime dust defeats Onyx's own combat-read "
        "and Kanja is knocked out, bound, and blindfolded in a shuttered tannery by two captors "
        "debating ransom versus killing him outright; he escapes using Veil Piercer on the door hinge "
        "itself since his hands are bound, then defeats both captors before they realize the door "
        "failed from the inside. Establishes quicklime dust as a genuine, narrow sensory blind spot. "
        "No new named characters -- the captors are unnamed. First entry in the Trench Monarch's "
        "thirty-fourth wave. Corrected Batch 321, 2026-10-02: the door-hinge escape was originally "
        "attributed to Whisper of Shadows; that structural/door-opening function belongs to Veil "
        "Piercer (`MCD-636`/`1433`) -- corrected to match."
    ),
    # --- E13: Nev Torr misdescribed as "a frightened conscript's boy" ---
    "MCD-1441": (
        '"The First Time He Taught Them to Fight" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-first-time-he-taught-them-to-fight.md), Trench Monarch "
        "Alias Chronicle CII, wave 34, closing the wave. Rebellion era, pre-Black-Trench. Kanja "
        "directly and deliberately teaches ordinary bladework (no Onyx of Oblivion powers invoked) "
        "to his three earliest crew members -- Corren Halst, Danne Sok, and Maret Vos (he/him "
        "throughout, per the Batch 226 reconciliation) -- for the first time, prompted narratively by "
        "the capture in `MCD-1439` though not framed as a direct response to it. Distinct from his "
        "training of the already-locked Nev Torr (`MCD-1063`) and of an unrelated bullied bystander "
        "(`MCD-948`), both strangers to the crew at the time. No new named characters. Closes the "
        "Trench Monarch's thirty-fourth wave. Corrected Batch 321, 2026-10-02: the opening line "
        "misdescribed Nev Torr as 'a frightened conscript's boy'; `MCD-1063`/`CC-119` establish him "
        "as a riveter's apprentice/dockhand Callum Breck personally brought in, not a conscript -- "
        "reworded to match."
    ),
}

for rid, new_statement in AMENDMENTS.items():
    assert rid in rules_by_id, f"Unknown rule id: {rid}"
    rules_by_id[rid]["statement"] = new_statement

# --- C2: new CC-160 dossier for Maret Vos, plus CC-158/159 origin-clause amendments ---
rules_by_id["CC-158"]["statement"] = (
    "Corren Halst: he/him (reconciled Batch 320, 2026-10-01, resolving a real pronoun split -- "
    "he/him throughout the Bane Alias Chronicle corpus, but she/her in a number of Captain and "
    "Blue-Collar Titan entries -- in favor of the clear majority usage, the same resolution pattern "
    "as Maret Vos/Dol Maren, Batch 226). One of the three earliest crew members -- alongside Danne "
    "Sok and Maret Vos, all three Maw survivors who found each other on the docks before finding "
    "Kanja (Batch 321, 2026-10-02) -- fighting alongside him by the Black Trench (age 19, `MCD-234`), "
    "forming the nucleus of Kanja's earliest crew before the mass liberation. Serves as Bane's second "
    "and most heavily recurring confidant across the Bane Alias Chronicle corpus (34+ waves), later "
    "taking a rotating dispute-council chair term under the Captain-era charter (`MCD-1056`/`1380`) "
    "and, decades on, a dock-era leg injury forces a graceful transition from front-line rotation to "
    "training the crew's recruits (`MCD-1459`)."
)
rules_by_id["CC-159"]["statement"] = (
    "Danne Sok: he/him (reconciled Batch 320, 2026-10-01, same resolution as `CC-158`). One of the "
    "three earliest crew members -- alongside Corren Halst and Maret Vos, all three Maw survivors who "
    "found each other on the docks before finding Kanja (Batch 321, 2026-10-02) -- fighting alongside "
    "him by the Black Trench (age 19, `MCD-234`). Runs an intelligence/verification network "
    "referenced extensively across the Bane Alias Chronicle corpus (e.g. independently confirming a "
    "Directorate defector's account over six weeks, `MCD-1027`). Privately kept, for the whole of the "
    "war, a memory of the young Kanja's hands shaking for an hour after freeing him, before any alias "
    "existed (`MCD-530`). Has a daughter (deliberately kept unnamed) who grows up visiting the crew's "
    "ships and eventually enlists, leading her own first independent operation a generation after "
    "Corren Halst's own comparable growth (`MCD-1002`/`1517`)."
)

NEW_RULES = [
    {
        "id": "CC-160",
        "category": "character-crew",
        "statement": (
            "Maret Vos: he/him (consistent with his usage throughout the Trench Monarch Alias "
            "Chronicle corpus, e.g. `MCD-1441`). One of the three earliest crew members -- alongside "
            "Corren Halst (`CC-158`) and Danne Sok (`CC-159`) -- all three Maw survivors who found "
            "each other on the docks before finding Kanja (Batch 321, 2026-10-02), fighting alongside "
            "him by the Black Trench (age 19, `MCD-234`), forming the nucleus of Kanja's earliest "
            "crew before the mass liberation at Maw-9. The quietest and least dramatized of the "
            "three in his own telling of those days (`MCD-533`) -- where Halst and Sok each closed "
            "their accounts with a story, Vos closes his with silence, recalling three people who'd "
            "already freed themselves looking for somewhere the freedom would actually hold, rather "
            "than any single dramatic rescue. Personally trained by Kanja in ordinary bladework "
            "alongside Halst and Sok once Kanja notices none of the three had ever been formally "
            "taught (`MCD-1441`), where his already-present instincts turn out to need less "
            "correction than either of the other two's."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

existing_ids = set(rules_by_id.keys())
for r in NEW_RULES:
    assert r["id"] not in existing_ids, f"ID collision: {r['id']}"
    ledger["rules"].append(r)

ledger["batches_completed"].append({
    "batch": 323,
    "date": str(date.today()),
    "source": SOURCE,
    "rule_count": len(NEW_RULES),
    "note": (
        "Reconciliation pass following a read-only review of the Trench Monarch Alias Chronicle "
        "corpus (102 entries). Fixed: the three earliest crew members' (Corren Halst, Danne Sok, "
        "Maret Vos) origin story, reconciled against the manuscript's own locked account (Chronicle "
        "III, Batch 70) and MCD-234 -- Maw survivors who found each other on the docks before "
        "finding Kanja, not freed by his own hand (MCD-533, MCD-641, MCD-1137; new dossier locked "
        "at CC-160 for Maret Vos, matching CC-158/159's own format; CC-158/159 amended in place with "
        "the same origin clause); Garren Hask's recruitment misattributed to a post-Dredge-Line Silt "
        "Row tally, contradicting his already-locked Forge-7 recruitment (CC-115) -- reframed as the "
        "moment he formally took over the crew's ledger-keeping role, set before the Dredge-Line "
        "Ambush, with a stray '31-year-old' age reference (31 is tenure, not age) corrected to 53 "
        "(MCD-623); a kill-count line ('drowned two hundred soldiers') contradicting the Dredge-Line "
        "Ambush's own locked framing and the no-killing doctrine (MCD-1129); Tavin Greer's "
        "allegiance drifting crew-internal in one entry, contradicting his consistently Directorate-"
        "side role elsewhere (MCD-644); Dol Maren's seventeen plank-bridges wrongly built after the "
        "founding flood rather than during the ambush itself, per CC-121 (MCD-1123). Mechanical "
        "fixes: a proper-noun collision ('Vask' vs. Lauris's Karesian institutional term, MCD-627, "
        "renamed to Kessler) and an under-credited new name noted in its rule statement (Ruven Calx, "
        "MCD-637); three wrong citations (MCD-1029's MCD-449 -> MCD-624, MCD-1127's MCD-291 -> "
        "ARS-010/MCD-232, MCD-1436's bogus 'MCD-403-adjacent' removed); a third-person self-"
        "reference plus a contradicted Coldrace accelerant claim (MCD-650); an inconsistent "
        "two-weeks/fortnight-vs-three-weeks timespan, made consistent at three weeks (MCD-944); a "
        "garbled Callum Breck age sentence, corrected to 'four years older than Kanja' per CC-117 "
        "(MCD-1147); an impossible pre-Black-Trench 'three years of Onyx-work' timespan, corrected "
        "to 'a year or more' given Onyx bonds at seventeen per ARS-020 (MCD-900); a 'years before'/"
        "'would open' timeline and wording error plus a garbled CC-133 cross-reference, corrected to "
        "'months before'/'would seal' and the Scrip-Forge-accelerant/Dead-Drakma-stockpile wording "
        "(MCD-629); a 'fourteen names' claim contradicting MCD-1031's sixteen-student figure, "
        "clarified as fourteen original requesters out of sixteen trained (MCD-1435); two writers'-"
        "room/meta leaks reworded to plain in-world phrasing, one also an anachronistic Warehouse-"
        "Twelve reference (MCD-480) and one quoting a Chronicle's own title in-world (folded into "
        "the MCD-1129 fix above); a false 'new geography' collision-check claim for 'Kessic flats,' "
        "corrected to note it sits within the already-locked broader Kessic region (MCD-1062); "
        "Whisper of Shadows misattributed a structural door-opening effect that belongs to Veil "
        "Piercer per MCD-636/1433 (MCD-1439); and Nev Torr misdescribed as 'a frightened conscript's "
        "boy' rather than the riveter's apprentice/dockhand Callum Breck brought in, per MCD-1063/"
        "CC-119 (MCD-1441). The Chronicle tracker (chronicle-tracks-status.md) was also corrected "
        "from 93 to 102 Chronicles for the Trench Monarch row. Two items flagged by the review were "
        "deliberately left untouched as softer stylistic observations rather than clear errors "
        "(Danne Sok's taciturnity drift, and two further minor craft notes), per the review's own "
        "scoping. Pure reconciliation throughout -- no new creative facts beyond the one new dossier "
        "(CC-160) and the two origin-clause amendments, matching the Batch 226/68/320 precedent."
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
