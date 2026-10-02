#!/usr/bin/env python3
"""Batch 334: Phase 3 fable-review fixes, Lauris Letitia Character Chronicle track.

Applies the rule-statement amendments from a Fable-model read-only review of all 109
Lauris Letitia Chronicles (MCD-1561-1565/1623-1626/1627-1726). The overwhelming majority of
the review's findings were pure prose-level corrections to the already-locked Chronicle .md
files (age-arithmetic fixes to match her true ~6,000-year age per MCD-1533, Fermand's
~200-year tenure per MCD-194/271, pronoun corrections, writers'-room/rule-ID leaks reworded,
narrator-boundary fixes, and a handful of real contradiction fixes) and needed no ledger-
statement change at all. This script amends only the subset of rule statements that
themselves needed correcting: citation fixes (MCD-1639, MCD-1692), a training-location fix
(MCD-1662), a wording overstatement fix (MCD-1667), two ARS-citation range fixes (MCD-1561,
MCD-1671), and the removal of duplicate/incorrect Strand K ordinal-position clauses
(MCD-1633 through MCD-1638, MCD-1677, MCD-1683) that double-counted or miscounted her own
entry position in the strand.

Five items from the review are new creative/worldbuilding decisions or require resolving a
larger cross-track contradiction and were deliberately left untouched pending Abad's own
ruling (dockside-crew mortality across several Strand W entries; whether Vask Ilvane should
be treated as a 13th Vask; Vael Korr-Drennen's gender/pronouns; the Ozmund/Book-1-era
placement question in two Strand W entries; and a pre-existing set of ledger contradictions
in MCD-156/160/171/217/267 predating this review, which need their own dedicated
reconciliation batch rather than being folded into this one).
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Phase 3 fable-review of the Lauris Letitia Character Chronicle track (109 Chronicles, "
    "docs/lords-of-cian/chronicles/lauris-chronicle-*.md, rules MCD-1561-1565/1623-1626/"
    "1627-1726) against the full ledger and corpus. Rule-statement amendment subset only -- "
    "see the Chronicle files' own in-place correction notes for the much larger set of "
    "prose-only fixes applied alongside this batch."
)

AMENDMENTS = {
    'MCD-1639': (
        "Lauris Chronicle XXII, 'The Wall That Came Apart in Silence' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxii-the-wall-that-came-apart-in-silence.md), a Strand D (Sealbound Directorate years) entry in her Character Chronicle series. Full-scene treatment of Operation 2, the Sister-of-Voren Abduction (previously only summarized at MCD-1543): her fourteen-kilometer night swim, the stacked-stone perimeter wall of a fortified former Directorate watch-station island disassembled by reading its load-bearing logic rather than forced (avoiding a percussive signature), and the roughly seven-minute extraction of Directorate archivist Sister Vaneth of Voren, closing the full engagement in forty-seven minutes with zero paramilitary deaths -- in place of a projected two-hundred-enforcer Directorate assault. Set within her ten Apprentice Contracts, with her assigned mentor Vael Korr-Drennen (MCD-177) present at the briefing; his reaction seeds, without yet stating, his own later retrospective assessment that she required no guidance from her second contract onward. No new named characters; Sister Vaneth of Voren and Vael Korr-Drennen already locked. No contradictions with any already-locked rule."
    ),
    'MCD-1662': (
        "Lauris Chronicle XLV, 'Testimony for No One Left to Hear It,' advances the standing testimony debt to the Iron-Speakers of Kares Prime (MCD-174, 'asking only that she preserve a record of what she found'; named among her active operational debts at MCD-211 as a debt whose discharge is 'already in progress'). After recording new archive material about Cian she considers genuinely worth preserving, Lauris confronts directly, for the first time, the fact that her own cohort at Vask Threnarr -- including her closest friend Velith, already locked, one of the 47 parthenogenically-conceived children raised alongside her (MCD-1553) -- will produce no descendants (MCD-1559), meaning the testimony's intended civilization is not merely dwindling but will end within an already largely determined span. She resolves to continue the archive exactly as before, reasoning it should exist for whoever on Cian eventually wants to know what Kares Prime was, even with no one left on Kares Prime to have commissioned the knowing -- but records plainly, for the first time, that she no longer knows with certainty who the testimony is for. Deepens rather than resolves the debt."
    ),
    'MCD-1692': (
        "Lauris Chronicle LXXV, 'The Container She Did Not Open' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxv-the-container-she-did-not-open.md), a Strand D entry giving full-scene treatment to Operation 8, the sealed Velkar riverbed container (previously only summarized at MCD-178: of unknown contents, delivered unopened to the Directorate's senior archive, where it remains sealed in the present day). Set within the Apprentice Contracts, reusing the already-locked Velkar riverbed location (MCD-178, Operation 8). Dramatizes her recovery of the anomalously dense, faintly humming container and her deliberate choice not to open it despite genuine temptation, trusting the Directorate's own caution -- deliberately preserves the contents as unknown, matching MCD-178's present-day framing exactly; no reveal. No new named characters. No contradictions with any already-locked rule."
    ),
    'MCD-1667': (
        "Lauris Chronicle L, 'Two Kinds of Patience' (full text at docs/lords-of-cian/chronicles/lauris-chronicle-l-two-kinds-of-patience.md): a stakes-free evening with Orlok on a rare visit to the crew, a third register of MCD-215's 'adequate-but-undemonstrative' clause -- a philosophical exchange between two of the crew's oldest present-day figures on witness and time, deliberately not detailing Orlok's Pavilion/Frequency Vigil secrets. No new named characters."
    ),
    'MCD-1561': (
        'Lauris Chronicle I, "The Shape Taught Twice" (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-i-the-shape-taught-twice.md), the first entry in Lauris Letitia\'s own Chronicle series under the Character Chronicle Gameplan, narrated by Fermand Aurelias per CC-034. A frontier holding near the Korren Highlands is found with an unfinished chalk perimeter matching the resonance-keying geometry from Operation 12\'s Settlement K-447 (MCD-1536); Lauris arrives before the pattern completes and stops it. A crude density-ward built by the circle fails against her mid-engagement, demonstrating the Density Saturation Inversion (ARS-357 through 366) directly for the first time: her signature grows harder rather than easier to detect as her density rises past a threshold, the inverse of every other density combatant on Cian. The engagement also puts her defining combat-joy (CC-134) on the page as an unqualified, competent pleasure in her own capability rather than grim duty. The circle\'s leader reveals he was taught the technique decades ago by an unnamed itinerant instructor calling it \'insurance\' -- confirming Settlement K-447\'s original actor is still alive and still teaching the method to unrelated circles, without identifying who they are. Lauris spares all six, extracting only the requirement that the settlement disclose the technique\'s real cost rather than keep it as a secret. Closes on her own admission that this operational debt -- unlike her others -- may never close on a schedule she controls. No new named characters.'
    ),
    'MCD-1671': (
        "'The Weight He Asked Her to Carry Gently' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-liv-the-weight-he-asked-her-to-carry-gently.md), Lauris Chronicle LIV, Strand W. Kanja asks Lauris to hold an antique clock's fine brass housing perfectly steady through an hour of delicate repair, seeking her exquisite control rather than raw capacity -- an inversion of expectation extending the Density Saturation Inversion mechanics (ARS-357 through 366). No new named characters."
    ),
    'MCD-1633': (
        "Lauris Chronicle XVI, 'The Weight They Meant to Take' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xvi-the-weight-they-meant-to-take.md), a Strand K (Kares Prime / deep past) entry in Lauris Letitia's own Chronicle series. Dramatizes one of the six defensive operations against non-Karesian incursions at orbital trade-points from the Long Operational Period (MCD-1555, age 1,841-~3,400), set at an unnamed outer trade-point distinct from the Olmedrin point she later departs through (MCD-175). A non-Karesian smuggling crew attempts to seize crated Living Drakma and hold an unarmed archivist hostage; Lauris disarms the crew with calibrated minimal force, extending her established precision-over-force reputation (MCD-1542/1543) to the Kares Prime era, and closes on her own private recognition that the trade-points' defensive numbers have thinned past ceremony into genuine vulnerability. No new named characters -- the smuggling crew stays deliberately unnamed, matching Chronicle II's (MCD-1562) convention for secondary figures. No contradictions with any already-locked rule."
    ),
    'MCD-1634': (
        "Lauris Chronicle XVII, 'The Second Shaft' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xvii-the-second-shaft.md), a Strand K entry. Dramatizes one of the eight geological emergency responses from the Long Operational Period (MCD-1555) in the pattern of the Vask Threnarr mining rescue (MCD-171), set at Vask Karth-Ven itself (already-locked location, MCD-1554) -- a gallery collapse in a deeper training-stock chamber traps eleven residents and kills two in the initial fall. Deliberately contrasted with MCD-171's earlier event: rather than simply outlasting the collapse through sustained Triad-Lock endurance, Lauris reads the collapse's structural load in real time and clears a precise channel while bearing only the mass the channel's own removal releases, extracting nine survivors within forty minutes -- showing her technique maturing past raw endurance over the intervening centuries. No new named characters. No contradictions."
    ),
    'MCD-1635': (
        "Lauris Chronicle XVIII, 'What Ilvane Left Behind' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xviii-what-ilvane-left-behind.md), a Strand K entry. Dramatizes the second of the three inter-Vask security operations from the Long Operational Period (MCD-1555; the first is Chronicle II, MCD-1562) -- a resource-scarcity dispute resolved without lethal force. A small, terminally failing Vask, Ilvane (new named location, collision-checked clean, zero prior hits), cannot survive the coming winter; Threnarr and Aldreth (both already-locked neighboring Vasks, established in Chronicle II) each press a claim to absorb its remaining ~40 residents and archive. Lauris arrives at the failing Iron-Speaker's own request, functions as custodian rather than combatant for eleven days, and ensures the population chooses its own absorption (Aldreth) collectively rather than being divided or relocated by force, with Threnarr negotiating a compromise (an archive loan) afterward. No new named characters beyond the location itself -- the Threnarr and Aldreth representatives stay unnamed, matching Chronicle II's convention. No contradictions."
    ),
    'MCD-1636': (
        "Lauris Chronicle XIX, 'The One She Asked For' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xix-the-one-she-asked-for.md), a Strand K entry. Dramatizes the first of the four training engagements Lauris requested herself during the Long Operational Period (MCD-1555), serving as primary opponent for a promising combatant from another Vask as she began to feel responsibility for developing the next generation's capability. Introduces Serath (new minor named character, a young combatant from Vask Olmedrin, already-locked location MCD-173 -- collision-checked clean, zero prior hits), whom Lauris trains for roughly six years at Vask Karth-Ven, adapting Tiramen's Karth-Sera principles (Continuous Engagement, Density-Progressive Combat; already locked MCD-169) to a student for the first time. Reuses Veska Karth-Ven, the already-locked instructor quoted at MCD-1558, as the one who prompts the mentorship. No contradictions."
    ),
    'MCD-1637': (
        "Lauris Chronicle XX, 'What the Floor Could No Longer Measure' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xx-what-the-floor-could-no-longer-measure.md), a Strand K entry, set roughly 250 years after Chronicle XIX (MCD-1636) and reusing Serath (now Olmedrin's own senior training authority) and Veska Karth-Ven. Dramatizes a routine reassessment on Vask Karth-Ven's central training floor (continuously calibrated for 28,000 years before Lauris's arrival, MCD-1554) during which the floor's instrumentation, for the first time in its recorded history, fails to produce a coherent reading of her combat-progression ceiling past the fourth hour of a sustained engagement. Functions as a deliberate hinge toward MCD-174: Lauris privately begins to wonder, for the first time, whether Kares Prime's surviving infrastructure has anything further to give her in return for her service -- foreshadowing without asserting MCD-174's later 'exhausted what the civilization's surviving infrastructure could still offer her' framing of her eventual decision to depart. No new named characters. No contradictions."
    ),
    'MCD-1638': (
        "Lauris Chronicle XXI, 'The Last Entry of the Long Operational Period' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxi-the-last-entry-of-the-long-operational-period.md), the closing entry of this wave's Strand K run, set at age ~3,400, the exact close of the Long Operational Period (MCD-1555). Dramatizes the fourth and final self-requested training engagement, introducing Doreth (new minor named character, collision-checked clean, zero prior hits) -- born at Vask Aldreth to one of the forty Ilvane residents relocated there in Chronicle XVIII (MCD-1635), a deliberate closing callback -- then closes with Lauris's own archive summary cataloguing all 23 Long Operational Period deployments (matching MCD-1555's own breakdown exactly: six trade-point defenses, eight geological emergencies, three inter-Vask disputes, four self-requested student trainings, and the Vask Olmedrin defense) and her first private articulation of the question that will become her eventual departure decision. Deliberately positioned at the exact threshold of MCD-174's decision window (age 3,400-3,580) without depicting the departure, Selene's death, or the Iron-Speaker deliberation, all reserved for future entries or already covered directly by MCD-174. No contradictions."
    ),
    'MCD-1677': (
        "Lauris Chronicle LX, 'The Century That Learned to Sit Still' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lx-the-century-that-learned-to-sit-still.md), the sixtieth entry in Lauris Letitia's own Chronicle series, opening the previously-undramatized ~1,100-year span between the close of the no-ceiling calibration period (age 114, Chronicle XIII, MCD-1630) and Velith's death (age ~1,200, Chronicle XIV, MCD-1631). Dramatizes the Sister-Hold's formal transition from crisis-rotation training to a standing, permanent instructor roster, and Tiramen's earliest private observations that would, decades later, begin the work already locked at MCD-169. No new named characters; reuses Veska Karth-Ven, Tiramen Karth-Ven, and Voreth Karth-Ven, all already locked. No contradictions with existing canon."
    ),
    'MCD-1683': (
        "Lauris Chronicle LXVI, 'What the Three Reasons Cost Her' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxvi-what-the-three-reasons-cost-her.md), the sixty-sixth entry in Lauris Letitia's own Chronicle series and the opening entry of this wave's departure sequence -- the direct payoff to the hook Chronicle XXI (MCD-1638) deliberately left open. Set roughly 180 years after Chronicle XXI, at age ~3,580, the far edge of MCD-174's decision window. Dramatizes the private articulation maturing into an actual decision: the ~180-year research period MCD-174 already locks, conducted at Vask-of-Vasks (the civilization's cultural/archival center, MCD-160), closing on the specific reasoning behind choosing Cian (the Kareth War-Order, the Sealbound Directorate's inherited Ionic-Rite methodology, and Living Drakma deposits approaching Kares Prime's own). No new named characters. No contradictions."
    ),
}


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}

    amended = []
    for rid, new_statement in AMENDMENTS.items():
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
            "Phase 3 fable-review of the Lauris Letitia Character Chronicle track. Amends 14 rule "
            "statements: MCD-1639 and MCD-1692 (citation fixes, MCD-176->MCD-177 and "
            "MCD-1534/Op4->MCD-178/Op8); MCD-1662 (her early cohort corrected from Vask Karth-Ven "
            "to Vask Threnarr); MCD-1667 (softened an overstated age-ranking claim); MCD-1561 and "
            "MCD-1671 (ARS-357-374 corrected to ARS-357 through 366); and MCD-1633 through "
            "MCD-1638, MCD-1677, and MCD-1683 (removed duplicate/incorrect Strand K ordinal-position "
            "clauses that double-counted or miscounted entries against MCD-1627-1632's own use of "
            "the same ordinals). The much larger set of prose-level fixes this same fable-review "
            "produced (age-arithmetic corrections to match her true ~6,000-year age per MCD-1533, "
            "Fermand's ~200-year tenure per MCD-194/271, pronoun corrections, a Density-Inversion/"
            "Spine-of-Dagon anachronism fix, a Brokenwall/Velaris method reconciliation, a "
            "Karth-Sera curriculum-origin fix, narrator-boundary fixes, and writers'-room/rule-ID "
            "leaks reworded to plain in-world phrasing) were applied directly to the already-locked "
            "Chronicle .md files themselves, each with its own correction note, and needed no "
            "ledger-statement change. Five items (dockside-crew mortality across several Strand W "
            "entries; Vask Ilvane as a possible 13th Vask; Vael Korr-Drennen's gender; the Ozmund/"
            "Book-1-era placement question; and a pre-existing MCD-156/160/171/217/267 "
            "contradiction set) are new creative decisions or a larger pre-existing reconciliation "
            "and are deliberately left untouched, flagged for Abad's own ruling."
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
        f"{len(amended)} rule statements amended: {', '.join(amended)}."
    )


if __name__ == "__main__":
    main()
