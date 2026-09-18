#!/usr/bin/env python3
"""
Batch 299: Lauris Letitia's 50-Chronicle wave (Chronicles X through LIX).

Eight parallel background agents drafted a 50-entry wave across Lauris's established
four-strand Character Chronicle convention (Strand K: Kares Prime/deep past, Strand D:
Sealbound Directorate operations, Strand L: the Ledger/present-day operational debts,
Strand W: Witness/present-day quiet register), matching the block-structure precedent
set by Daba's own 50-Chronicle launch wave (Batch 296).

Abad's approval, quoted verbatim: "lock it, continue uninterrupted, test and push to main"
-- given directly in response to the proposed 8-agent strand/block structure.
"""
import json
from datetime import datetime, timezone

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-18, Lauris Character Chronicle wave (Chronicles X-LIX)."

BATCH_NOTE = (
    'Lauris Letitia\'s 50-Chronicle wave (Chronicles X-LIX, MCD-1627 through MCD-1676), drafted by 8 '
    'parallel background agents across her established four-strand convention (Strand K: Kares Prime/deep '
    'past, 12 entries, Chronicles X-XXI; Strand D: Sealbound Directorate operations, 13 entries, Chronicles '
    'XXII-XXXIV, giving full-scene treatment to Operations 2, 4, 5, 13, 14, 16, 17, 22, 26, 28, 29, 31, and '
    '37 of her 40-operation career; Strand L: the Ledger/present-day debts, deepen-don\'t-resolve, 12 '
    'entries, Chronicles XXXV-XLVI; Strand W: Witness/present-day quiet register, 13 entries, Chronicles '
    'XLVII-LIX, featuring Ozmund, Valen, Anansi, Orlok, Fermand himself as a participant for the first time, '
    'and five dockside crew members). Matches the block-structure precedent of Daba\'s own 50-Chronicle '
    'launch wave (Batch 296): each agent read the existing 9 Lauris Chronicles for voice/continuity, '
    'collision-checked its own new proper nouns against the live ledger, and was barred from touching '
    'canon-ledger.json or git. A final cross-agent sweep by the orchestrating session confirmed zero '
    'proper-noun collisions across all 8 agents\' output and against the full live ledger (new names: '
    'Iron-Speaker Vann, Vask Ilvane, Serath, Doreth, Corin Halvet, Tevan Kesk, CP-609). One in-flight naming '
    'slip was self-corrected by the Strand K wave-2 agent before finalizing (an anachronistic Cian-era '
    'epithet used in a Kares-Prime-era context). One typo ("enforaid\'s" -> "enforcer\'s") in MCD-1646\'s '
    'statement was corrected during consolidation. No new named characters beyond the small set above, all '
    'minor and collision-checked; every other returning figure reused already-locked canon. Abad\'s approval, '
    'quoted verbatim, given directly in response to the proposed 8-agent strand structure: "lock it, '
    'continue uninterrupted, test and push to main."'
)

NEW_RULES = [
    # Strand K, wave 1 (early Kares Prime) -- Chronicles X-XV, MCD-1627-1632
    {
        "id": "MCD-1627",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle X, 'What the Log Was Not Meant to Show' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-x-what-the-log-was-not-meant-to-show.md), the tenth entry in Lauris Letitia's own Chronicle series and the third entry of Strand K (Kares Prime / deep past), the first to dramatize her earliest childhood years at Vask Threnarr under archivist Olda Threnarr-Iralek (MCD-164/166). Set at age eight, it dramatizes for the first time the origin of her lifelong 'careful witness' discipline (MCD-161) through an observation-log exercise in which young Lauris records the structural mechanics of a training bout rather than its outcome, and dramatizes her earliest recorded exchange with cohort friend Velith (MCD-165/1553), whose death is not depicted here. No new named characters beyond a minor, collision-checked training-bout figure ('Iron-Speaker Vann'); reuses Olda Threnarr-Iralek, Velith, and the Vask Threnarr setting, all already locked. No contradictions with existing canon.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1628",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XI, 'The Number Recalibration Could Not Undo' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xi-the-number-recalibration-could-not-undo.md), the eleventh entry in Lauris Letitia's own Chronicle series and the fourth entry of Strand K. Dramatizes directly, for the first time, the age-fourteen cohort density assessment already locked at MCD-166 -- Mira Threnarr-Olmedrin's fourfold recalibration confirming Lauris's 2,800x reading, the Sister-Hold's three-day deliberation, and Lauris's own recorded priority on learning she would relocate to Vask Karth-Ven (whether she would still see her cohort) -- closing on Velith's own log entry for the departure. No new named characters; reuses Mira Threnarr-Olmedrin, Selene, Velith, and the Threnarr Sister-Hold, all already locked. No contradictions with existing canon.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1629",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XII, 'Eight Where Five Had Been' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xii-eight-where-five-had-been.md), the twelfth entry in Lauris Letitia's own Chronicle series and the fifth entry of Strand K. Dramatizes her arrival at Vask Karth-Ven at age fourteen, her expanded eight-member Sister-Hold (MCD-167), the Vask's mountain-built infrastructure and sixty-meter Drakma training floor (MCD-1554), and her first meetings with instructors Veska Karth-Ven, Tiramen Karth-Ven, and Voreth Karth-Ven -- including Mira Threnarr-Olmedrin's role making the introductions, extending her established prior residency at Karth-Ven before her relocation to Threnarr (MCD-164). No new named characters. No contradictions with existing canon.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1630",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XIII, 'The Session She Did Not End' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xiii-the-session-she-did-not-end.md), the thirteenth entry in Lauris Letitia's own Chronicle series and the sixth entry of Strand K. Dramatizes the no-ceiling calibration period of her first century at Vask Karth-Ven (age 14-114, MCD-168) directly for the first time -- the Sister-Hold's abandonment of projected density ceilings, the multi-instructor rotation her sustained non-fatigue forced on her training, and the already-locked quotes from Veska Karth-Ven and Voreth Karth-Ven (MCD-1558) placed in their full original context for the first time. No new named characters. No contradictions with existing canon.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1631",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XIV, 'What Velith Left in the Log' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xiv-what-velith-left-in-the-log.md), the fourteenth entry in Lauris Letitia's own Chronicle series and the seventh entry of Strand K. Dramatizes directly, for the first time, Velith's death in a Vask Threnarr defensive operation at approximately age 1,200 (MCD-165) and the writing of the longest single archive entry Lauris has ever produced -- Lauris arriving three days after the engagement, absent by training-calendar distance rather than choice, and choosing solitary, accuracy-focused private record over the Sister-Hold's communal remembrance custom. No new named characters; reuses Velith, already locked. No contradictions with existing canon.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1632",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XV, 'Three Hours in the Dark' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xv-three-hours-in-the-dark.md), the fifteenth entry in Lauris Letitia's own Chronicle series and the eighth entry of Strand K, closing this wave. Dramatizes directly, for the first time, the Vask Threnarr mining collapse already locked at MCD-171 -- her sustained three-hour Triad-Lock holding an unstable shaft's 2.4-million-metric-ton cumulative pressure-equivalent while three trapped stonework-guild women free themselves, framed as the civilization's own 'first lethal combat' classification despite the absence of any opponent, and closing on her already-locked archive line ('The shaft is sealed. The Hold continues.,' MCD-1558) restored to its full original context. No new named characters. No contradictions with existing canon.",
        "status": "locked",
        "source": SOURCE,
    },
    # Strand K, wave 2 (later Kares Prime) -- Chronicles XVI-XXI, MCD-1633-1638
    {
        "id": "MCD-1633",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XVI, 'The Weight They Meant to Take' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xvi-the-weight-they-meant-to-take.md), the third entry of Strand K (Kares Prime / deep past) in Lauris Letitia's own Chronicle series. Dramatizes one of the six defensive operations against non-Karesian incursions at orbital trade-points from the Long Operational Period (MCD-1555, age 1,841-~3,400), set at an unnamed outer trade-point distinct from the Olmedrin point she later departs through (MCD-175). A non-Karesian smuggling crew attempts to seize crated Living Drakma and hold an unarmed archivist hostage; Lauris disarms the crew with calibrated minimal force, extending her established precision-over-force reputation (MCD-1542/1543) to the Kares Prime era, and closes on her own private recognition that the trade-points' defensive numbers have thinned past ceremony into genuine vulnerability. No new named characters -- the smuggling crew stays deliberately unnamed, matching Chronicle II's (MCD-1562) convention for secondary figures. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1634",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XVII, 'The Second Shaft' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xvii-the-second-shaft.md), the fourth entry of Strand K. Dramatizes one of the eight geological emergency responses from the Long Operational Period (MCD-1555) in the pattern of the Vask Threnarr mining rescue (MCD-171), set at Vask Karth-Ven itself (already-locked location, MCD-1554) -- a gallery collapse in a deeper training-stock chamber traps eleven residents and kills two in the initial fall. Deliberately contrasted with MCD-171's earlier event: rather than simply outlasting the collapse through sustained Triad-Lock endurance, Lauris reads the collapse's structural load in real time and clears a precise channel while bearing only the mass the channel's own removal releases, extracting nine survivors within forty minutes -- showing her technique maturing past raw endurance over the intervening centuries. No new named characters. No contradictions.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1635",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XVIII, 'What Ilvane Left Behind' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xviii-what-ilvane-left-behind.md), the fifth entry of Strand K. Dramatizes the second of the three inter-Vask security operations from the Long Operational Period (MCD-1555; the first is Chronicle II, MCD-1562) -- a resource-scarcity dispute resolved without lethal force. A small, terminally failing Vask, Ilvane (new named location, collision-checked clean, zero prior hits), cannot survive the coming winter; Threnarr and Aldreth (both already-locked neighboring Vasks, established in Chronicle II) each press a claim to absorb its remaining ~40 residents and archive. Lauris arrives at the failing Iron-Speaker's own request, functions as custodian rather than combatant for eleven days, and ensures the population chooses its own absorption (Aldreth) collectively rather than being divided or relocated by force, with Threnarr negotiating a compromise (an archive loan) afterward. No new named characters beyond the location itself -- the Threnarr and Aldreth representatives stay unnamed, matching Chronicle II's convention. No contradictions.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1636",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XIX, 'The One She Asked For' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xix-the-one-she-asked-for.md), the sixth entry of Strand K. Dramatizes the first of the four training engagements Lauris requested herself during the Long Operational Period (MCD-1555), serving as primary opponent for a promising combatant from another Vask as she began to feel responsibility for developing the next generation's capability. Introduces Serath (new minor named character, a young combatant from Vask Olmedrin, already-locked location MCD-173 -- collision-checked clean, zero prior hits), whom Lauris trains for roughly six years at Vask Karth-Ven, adapting Tiramen's Karth-Sera principles (Continuous Engagement, Density-Progressive Combat; already locked MCD-169) to a student for the first time. Reuses Veska Karth-Ven, the already-locked instructor quoted at MCD-1558, as the one who prompts the mentorship. No contradictions.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1637",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XX, 'What the Floor Could No Longer Measure' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xx-what-the-floor-could-no-longer-measure.md), the seventh entry of Strand K, set roughly 250 years after Chronicle XIX (MCD-1636) and reusing Serath (now Olmedrin's own senior training authority) and Veska Karth-Ven. Dramatizes a routine reassessment on Vask Karth-Ven's central training floor (continuously calibrated for 28,000 years before Lauris's arrival, MCD-1554) during which the floor's instrumentation, for the first time in its recorded history, fails to produce a coherent reading of her combat-progression ceiling past the fourth hour of a sustained engagement. Functions as a deliberate hinge toward MCD-174: Lauris privately begins to wonder, for the first time, whether Kares Prime's surviving infrastructure has anything further to give her in return for her service -- foreshadowing without asserting MCD-174's later 'exhausted what the civilization's surviving infrastructure could still offer her' framing of her eventual decision to depart. No new named characters. No contradictions.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1638",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXI, 'The Last Entry of the Long Operational Period' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxi-the-last-entry-of-the-long-operational-period.md), the eighth entry of Strand K and closing entry of this wave, set at age ~3,400, the exact close of the Long Operational Period (MCD-1555). Dramatizes the fourth and final self-requested training engagement, introducing Doreth (new minor named character, collision-checked clean, zero prior hits) -- born at Vask Aldreth to one of the forty Ilvane residents relocated there in Chronicle XVIII (MCD-1635), a deliberate closing callback -- then closes with Lauris's own archive summary cataloguing all 23 Long Operational Period deployments (matching MCD-1555's own breakdown exactly: six trade-point defenses, eight geological emergencies, three inter-Vask disputes, four self-requested student trainings, and the Vask Olmedrin defense) and her first private articulation of the question that will become her eventual departure decision. Deliberately positioned at the exact threshold of MCD-174's decision window (age 3,400-3,580) without depicting the departure, Selene's death, or the Iron-Speaker deliberation, all reserved for future entries or already covered directly by MCD-174. No contradictions.",
        "status": "locked",
        "source": SOURCE,
    },
    # Strand D, part 1 (early SBD operations) -- Chronicles XXII-XXVIII, MCD-1639-1645
    {
        "id": "MCD-1639",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXII, 'The Wall That Came Apart in Silence' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxii-the-wall-that-came-apart-in-silence.md), a Strand D (Sealbound Directorate years) entry in her Character Chronicle series. Full-scene treatment of Operation 2, the Sister-of-Voren Abduction (previously only summarized at MCD-1543): her fourteen-kilometer night swim, the stacked-stone perimeter wall of a fortified former Directorate watch-station island disassembled by reading its load-bearing logic rather than forced (avoiding a percussive signature), and the roughly seven-minute extraction of Directorate archivist Sister Vaneth of Voren, closing the full engagement in forty-seven minutes with zero paramilitary deaths -- in place of a projected two-hundred-enforcer Directorate assault. Set within her ten Apprentice Contracts, with her assigned mentor Vael Korr-Drennen (MCD-176) present at the briefing; his reaction seeds, without yet stating, his own later retrospective assessment that she required no guidance from her second contract onward. No new named characters; Sister Vaneth of Voren and Vael Korr-Drennen already locked. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1640",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXIII, 'What She Chose Not to Say' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxiii-what-she-chose-not-to-say.md), a Strand D entry in her Character Chronicle series. Full-scene treatment of Operation 4, the Korren Smuggling Ring (previously only summarized at MCD-1534/MCD-1542): the calibrated collarbone-fracturing acquisition of smuggler Therik Voll at a restaurant table rather than an assault on his fortified warehouse, and the recovery of 'Sample K-403' -- a sealed fragment of Karesian biological material Lauris recognized on sight and delivered to the Directorate's Coastal Containment Office without disclosing her recognition. Deliberately frames this as a quieter, unwritten precursor to the private-notation habit Chronicle VII (MCD-1624) establishes as formally beginning at Operation 6, rather than contradicting it -- Operation 4's omission is an unnamed instinct, not yet the deliberate private ledger Operation 6 gives a name to. No new named characters; Therik Voll already locked. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1641",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXIV, 'The Floor of the Maelstrom' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxiv-the-floor-of-the-maelstrom.md), a Strand D entry in her Character Chronicle series. Full-scene treatment of Operation 5, the Maelstrom Beast (previously only summarized at MCD-1544): her three-hour walk along the channel floor of the deep tidal Voskharen Wetlands to the fourteen-meter apex predator's twenty-two-meter-deep primary chamber, surviving its bite (fracturing its own teeth against her sternum) and an approximately eighty-thousand-kilogram full-body compression coil distributed laterally by her Hexa-Lamellar Lattice, then terminating it with the Spine of Dagon drawn and swung underwater across a roughly seven-hour total engagement. Puts CC-134's defining combat-joy trait on the page in a pure-physicality register distinct from Chronicle I's crowd-control showcase. No new named characters. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1642",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXV, 'Delivered Alive' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxv-delivered-alive.md), a Strand D entry in her Character Chronicle series. Full-scene treatment of Operation 13, the Captain Drenneth Acquisition (previously only summarized at MCD-1546): the underwater hull-climb boarding of the Iron Veth, adapting her Karth-Ven cliff-face lattice-grip technique to a wooden hull, and the acquisition itself via the same calibrated collarbone-fracturing strike used at Operation 4. Dramatizes the operation's true weight -- Lauris's later, out-of-contract discovery that Drenneth died during Directorate processing despite her delivering him alive -- as an early, concrete data point in the institutional-doubt trajectory that Chronicle III's Operation 19 later completes, six operations before Operation 19 gives the pattern its name. Includes the already-locked coincidental-homonym note distinguishing Captain Drenneth from Drenneth Threnarr-Vask, her Sister-Hold archivist mentor. No new named characters; Captain Drenneth already locked. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1643",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXVI, 'No Longer Subtle' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxvi-no-longer-subtle.md), a Strand D entry in her Character Chronicle series. Full-scene treatment of Operation 14, the Vask of the Hollow (previously only summarized at MCD-1537): her solo, eighteen-day clearance of a fourteen-kilometer subterranean gallery system that had defeated six prior Directorate exploration teams, terminating roughly 720 engineered hostile entities and reaching the private conclusion that the pattern she had been noticing since Operation 3 was 'no longer subtle' -- also the operation after which the Directorate stopped assigning her a supervising mentor. Closes with a shorter epilogue on Operation 20's return roughly two years later: the new ~320-subject population generated by the same central node, and her decision to destroy the node itself rather than merely reseal the site a second time, the only revision to Directorate containment doctrine her career produced (the fourteen smaller redundancy nodes missed by this clearance and later found at Operation 36 per MCD-191 are referenced but not dramatized). No new named characters. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1644",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXVII, 'What Brokenwall Was Never Told' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxvii-what-brokenwall-was-never-told.md), a Strand D entry in her Character Chronicle series. Full-scene treatment of Operation 16, the Brokenwall mass civilian density-anomaly outbreak (previously only summarized at MCD-1538): her twenty-two-hour sustained precision-strike clearance of roughly two hundred simultaneously afflicted civilians (a discrete, granular register distinct from her usual single-opponent combat-progression climb), her private discovery of the planted Ionic Rite-derived resonance node responsible, and her decision to conceal it from the Directorate and rebury rather than destroy it, consistent with MCD-1538's statement that she reburied at Brokenwall and only destroyed the equivalent node outright at the later Velaris outbreak. The parallel Velaris outbreak (Operation 22) is deliberately left unnamed and undramatized here, since Operation 22 is separately given full-scene treatment at Chronicle XXIX (MCD-1646). No new named characters. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1645",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXVIII, 'Four Hours to Spare' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxviii-four-hours-to-spare.md), a Strand D entry in her Character Chronicle series. Full-scene treatment of Operation 17, the Drowning Vault breach clearance already referenced at MCD-179 and MCD-1547, and by name in Chronicle IV (MCD-1564, 'alone against twenty-three engineered subjects in a facility a mile beneath the sea'): her thirty-hour-window race against secondary-containment failure roughly 1,200 meters deep in the Voskharen Trench, viable without pressurized equipment via her Ironstorm Blood's oxygen-binding capacity. Dramatizes the four-hour controlled Phalanx-arrested descent, the fourteen-hour engagement against the twenty-three released Karesian-derived constructs (consistent in training with the Salt-Locked Archive's Operation 15 guardian construct per MCD-1547), and the eight-hour manual reconstruction of the breached primary containment barrier, resealed with four hours to spare. Closes on deliberate dramatic irony, consistent with MCD-183's reserved Operation 25 reveal: she believes she has simply closed a contract well, not knowing the true scale of what her reseal preserved behind it -- that reveal is explicitly not disclosed in this entry. No new named characters. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    # Strand D, part 2 (later SBD operations) -- Chronicles XXIX-XXXIV, MCD-1646-1651
    {
        "id": "MCD-1646",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXIX, 'The City Was Big. She Was Small.' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxix-the-city-was-big-she-was-small.md), the twenty-ninth entry in Lauris Letitia's own Chronicle series and a Strand D (Sealbound Directorate years) entry, gives full-scene treatment to Operation 22 (the Velaris outbreak, previously only summarized at MCD-1538): the 47-hour discrete-strike clearance of roughly 600 afflicted subjects across a city of forty thousand, and the origin of the 'Petite Catastrophe' alias, dramatizing the already-locked perimeter-watch enforcer's after-action line (MCD-1539) verbatim. Also dramatizes MCD-1541's escalating institutional trust and shows Lauris destroying rather than reburying the outbreak's source resonance node, a departure from her Settlement K-447 practice, and quietly declining to report the node's existence -- an early instance of the selective-disclosure pattern that grows across her Specialist period. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1647",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXX, 'The Movement Built to Watch Her' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxx-the-movement-built-to-watch-her.md), the thirtieth entry in Lauris Letitia's own Chronicle series, gives full-scene treatment to Operation 26 (previously only summarized at MCD-184): the insurgent leader Veth Korr, engaged and terminated in a brief tactical exchange, then revealed on Lauris's own extended exit reconnaissance to have been founded and resourced by the same engineering-tradition apparatus operating beneath the Directorate, engineered specifically to require her personal deployment. Dramatizes the operation as the point at which Lauris understood the apparatus was studying her combat methodology specifically, not merely operating independently of her. No new named characters; Veth Korr already locked.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1648",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXXI, 'What Her Own Hands Had Taught' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxxi-what-her-own-hands-had-taught.md), the thirty-first entry in Lauris Letitia's own Chronicle series, gives full-scene treatment to Operation 28 (previously only summarized at MCD-186): the cluster of seven engineered Karesian subjects, the last of whom fought using Lauris's own Karth-Sera curriculum and closely mirrored her own combat development around age 2,400. Dramatizes the extended engagement required to unlearn her own instinctive Karth-Sera counters against a mirrored opponent, and her unresolved private reaction to the working conclusion that the apparatus reverse-engineered the curriculum from observing her own operations rather than possessing an independent copy from Kares Prime. No new named characters; the subject stays unnamed, matching MCD-186's own phrasing.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1649",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXXII, 'We Are the Same. Run.' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxxii-we-are-the-same-run.md), the thirty-second entry in Lauris Letitia's own Chronicle series, gives full-scene treatment to Operation 29 (previously only summarized at MCD-187): the fleeing engineered Karesian subject CP-414's final minutes before termination, dramatizing her disclosure of additional Korren Highlands facilities, the mispronounced hint of Anu Un Ra's name (not resolved until Operation 34, referenced only as a forward pointer here, not dramatized), and her closing line, already locked verbatim: 'You were not the first. You will not be the last. We are the same. Run.' Dramatizes the rule's own claim that the message shaped every subsequent operation, marking the beginning of Lauris deliberately steering her own contract acceptances toward the Korren Highlands. No new named characters; CP-414 already locked.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1650",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXXIII, 'Aligned, Not Opposed' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxxiii-aligned-not-opposed.md), the thirty-third entry in Lauris Letitia's own Chronicle series, gives full-scene treatment to Operation 31 (previously only summarized at MCD-189): the acquisition-or-termination contract against Subject IM-099, revealed mid-engagement to be Kareth-Vassen Aerelin, a Cian-diaspora Kareth War-Order operative running an autonomous 60-year campaign against the engineering tradition's trafficking fronts. Dramatizes the mutual recognition, the staged termination that closed the Directorate's contract while leaving Aerelin free to continue operating, and the formation of their ongoing informal intelligence alliance -- Lauris's first deliberate act of working against, rather than merely withholding information from, the institution she served. No new named characters; Aerelin already locked.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1651",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXXIV, 'Three Facilities, Openly' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xxxiv-three-facilities-openly.md), the thirty-fourth entry in Lauris Letitia's own Chronicle series, gives full-scene treatment to Operation 37 (previously only summarized within MCD-191): Lauris's first openly joint operation with Aerelin's Kareth War-Order network, by then expanded to roughly 18 autonomous operatives -- three coordinated facility clearances conducted together over nine days, resulting in roughly 280 engineered Karesian subjects rescued to concealment rather than left to Directorate processing. Closes this wave deep in the Disillusionment sub-period, deliberately stopping at the edge of Operation 38 and not touching Operation 40 (the Defection), both reserved. No new named characters; Aerelin already locked.",
        "status": "locked",
        "source": SOURCE,
    },
    # Strand L, part 1 -- Chronicles XXXV-XL, MCD-1652-1657
    {
        "id": "MCD-1652",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXXV, 'What the Other Four Became' (docs/lords-of-cian/chronicles/lauris-chronicle-xxxv-what-the-other-four-became.md): extends the Operation 38 facility family (MCD-191) beyond the third withheld facility already covered at Chronicle IV (MCD-1564). A stale Directorate transfer manifest, surfaced through Aerelin's network, shows that one of the four Operation 38 facilities Lauris reported through ordinary channels (rather than withheld) had its subjects moved onward to an unnamed second designation roughly eleven years after her report, with three further unconnected transfer fragments bearing the same administrative signature suggesting the practice was standard Directorate procedure she never had visibility into. The trail goes cold before naming a destination. Deepens rather than resolves: 'reported' is established as never having meant 'released' or 'closed,' widening rather than narrowing the Operation 38 debt. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1653",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXXVI, 'The Two She Already Moved' (docs/lords-of-cian/chronicles/lauris-chronicle-xxxvi-the-two-she-already-moved.md): continues the Operation 38 facility family (MCD-191) from the other side of Chronicle XXXV (MCD-1652) -- the two of the three withheld facilities Lauris has already cleared and relocated to concealment. A maintenance visit to the nearer of the two reveals the relocated population has fallen from 41 to 38 across eleven years, three natural (non-violent, non-discovery-related) deaths attributable to age and, in one case, a likely degenerative condition present before the original clearance. Deepens rather than resolves: establishes that 'cleared' subjects remain in indefinite, unresolved concealment subject to ordinary mortality, distinct from but structurally parallel to the K-Theta cave-system maintenance thread (MCD-190/193, Chronicle VIII/MCD-1625). The second of the two facilities is not visited this entry; her rotation places it months out. No new named characters; the facility stays uncoded per MCD-191's and Chronicle IV's own practice.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1654",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXXVII, 'What a Revival Would Require' (docs/lords-of-cian/chronicles/lauris-chronicle-xxxvii-what-a-revival-would-require.md): advances the Drowning Vault's 120 (MCD-183), previously undramatized in any Lauris Chronicle, without touching the discharge Book 5 reserves for it (MCD-216). A joint planning session with Sephtis in the Karkosa's archive room establishes that the secured population's 20-to-8,000-year generation-age spread makes a single unified revival protocol impossible; staged, individualized revival would likely be required, with substantial medical/psychological support neither of them has assembled, and some fraction of the oldest-generation subjects may not have recoverable minds at all, a possibility left open rather than resolved. Sephtis agrees to begin cataloguing relevant archival fragments; no revival attempt is made. Deepens rather than resolves: reframes the debt's true complexity without advancing toward discharge. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1655",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXXVIII, 'A Dozen Doors, One Key Missing' (docs/lords-of-cian/chronicles/lauris-chronicle-xxxviii-a-dozen-doors-one-key-missing.md): advances the Sample K-403 thread (MCD-1534). Investigating via Aerelin's network, Lauris confirms the Directorate's Coastal Containment Office underwent at least two administrative reorganizations since she delivered the sample at Operation 4, and that K-403's file was reclassified into an unnamed, unlocated secondary long-term archive during the second reorganization -- harder to find than before rather than easier. The search surfaces partial administrative references to two further fragments among the roughly dozen scattered Karesian biological fragments MCD-1534 describes, also apparently relocated, neither currently actionable. Deepens rather than resolves: no fragment is recovered; she adds a standing archive-review line to check for further movement. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1656",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XXXIX, 'The Photographs She Has Not Shown Him' (docs/lords-of-cian/chronicles/lauris-chronicle-xxxix-the-photographs-she-has-not-shown-him.md): advances the Twin Anomaly photographs thread (MCD-1535). Prompted by the accumulated weight of the Operation 38 and Sample K-403 inquiries elsewhere in this wave, Lauris takes out the still-unanalyzed development-record photographs from Operation 6 for the longest sustained look she has given them in years, explicitly drawing the parallel to how letting 'not yet' become indefinite cost her with Sample K-403. She still declines to show them to Sephtis, reasoning that confirmation would obligate a response she is not yet positioned to give across her other open debts, but for the first time commits plainly to showing him eventually rather than leaving the question open indefinitely. Deepens rather than resolves: the photographs remain unshown. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1657",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XL, 'The Question She Still Owes' (docs/lords-of-cian/chronicles/lauris-chronicle-xl-the-question-she-still-owes.md): advances the Verith deferral (MCD-180) and the parallel Val Mirel Kareth non-contact arrangement (MCD-198), closing the wave-one Strand L push. The accumulated weight of the five debts advanced earlier in this wave (MCD-1652 through MCD-1656) brings Lauris to explicitly weigh invoking Sephtis's standing broker-contact protocol for the first time in the chronicle's run. She declines again, but names for the first time that the true obstacle was never 'the operational reason has not arisen' (MCD-198's own framing) but her own unreadiness for certainty over the Verith decision. Deepens rather than resolves: no contact is made; the deferral to a future conversation with Val Mirel (MCD-180) remains open. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    # Strand L, part 2 -- Chronicles XLI-XLVI, MCD-1658-1663
    {
        "id": "MCD-1658",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XLI, 'What Corin Halvet Asked For,' advances the standing debt behind Operation 37's roughly 280 engineered-Karesian subjects rescued to concealment (MCD-191, folded into MCD-212's 'further accumulated rescues') without resolving it. Corin Halvet, one of that population, was already an adult at his rescue and has spent two centuries under the concealment network's protection; he requests, for the first time from anyone in that population, to leave concealment and live openly at real personal risk rather than remain protected. Lauris meets him in person, confirms through direct questioning that his understanding of the risk and his motivation are genuinely his own, and defers the decision -- neither granting nor refusing it -- judging a request of this weight too large to settle as a single case rather than a precedent for the whole protected population. Deepens rather than resolves the debt; Corin Halvet's answer, and the wider policy question his request raises, remain open. New named character Corin Halvet, collision-checked clean.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1659",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XLII, 'The Dozen Unaccounted,' advances the Sample K-403 thread (MCD-1534) -- one of roughly a dozen scattered Karesian biological fragments recovered from Korren Highlands archaeological sites, of which Lauris delivered one to Directorate processing during Operation 4 without disclosing her own recognition of it. Working with retired Directorate historian Vael Korr-Drennen (already locked, MCD-1541), whom Sephtis had independently identified through her published retrospective on Lauris's own Directorate career, Lauris traces a second fragment's chain of custody through three documented transfers before the trail ends at a register entry marked 'disposed of per standing protocol' with its supporting attachment lost to an earlier records purge. This confirms institutional loss (or its appearance) for one additional fragment without locating it or the other roughly ten still unaccounted for, and without establishing whether the Directorate's own account of its losses can be trusted. Vael Korr-Drennen offers to continue the search independently; Lauris accepts. Deepens rather than resolves the debt.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1660",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XLIII, 'What Was Owed to a Name,' advances a reputational debt distinct from any of her operational or population debts: her Established Hunter-period Directorate nickname 'the Petite Catastrophe' (already locked, MCD-1539) is being invoked without her knowledge or consent by an unrelated debt-collector, Tevan Kesk, to intimidate defaulters along the Kesmara Eastern Hills trade roads into believing she personally backs his collections. Lauris confronts Kesk directly without violence, forbids further use of the name, and personally visits every debtor known to have paid under its implied threat to correct the record and recover what she can. She deliberately declines to press Kesk past his first, uncertain answer about where he learned the name, judging pursuit past that point would produce a confident lie rather than a true one -- leaving both the name's original source and the full extent of its unauthorized use open. New named character Tevan Kesk, collision-checked clean.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1661",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XLIV, 'The Terms She Still Controls,' advances a relational/trust debt with Kareth-Vassen Aerelin (already locked, MCD-191/194/197) distinct from any facility or population debt: through Sephtis's standing personal broker channel, Aerelin asks Lauris for help -- personal rather than institutional, per the condition Lauris negotiated without modification at her recruitment that her relationship with Aerelin's network stays on terms she controls rather than the movement's central command (MCD-194) -- assessing whether one of the roughly eighteen autonomous Kareth War-Order operatives from Operation 35's network, showing signs consistent with either fatigue or an early-stage cover compromise, needs extraction. Lauris agrees to assess in person, alone, without briefing Ezio or the wider Lords of Cian crew, honoring Aerelin's terms, but has not decided whether the situation, once assessed, will force her to break those terms for the first time in two centuries of the arrangement holding. Deepens rather than resolves the debt; the operative's status and whether extraction occurs remain open.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1662",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XLV, 'Testimony for No One Left to Hear It,' advances the standing testimony debt to the Iron-Speakers of Kares Prime (MCD-174, 'asking only that she preserve a record of what she found'; named among her active operational debts at MCD-211 as a debt whose discharge is 'already in progress'). After recording new archive material about Cian she considers genuinely worth preserving, Lauris confronts directly, for the first time, the fact that her own cohort at Vask Karth-Ven -- including her closest friend Velith, already locked, one of the 47 parthenogenically-conceived children raised alongside her (MCD-1553) -- will produce no descendants (MCD-1559), meaning the testimony's intended civilization is not merely dwindling but will end within an already largely determined span. She resolves to continue the archive exactly as before, reasoning it should exist for whoever on Cian eventually wants to know what Kares Prime was, even with no one left on Kares Prime to have commissioned the knowing -- but records plainly, for the first time, that she no longer knows with certainty who the testimony is for. Deepens rather than resolves the debt.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1663",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XLVI, 'What Run Was Supposed to Mean,' advances a promise debt tied to Operation 29's dying subject, Designation CP-414 (already locked, MCD-187: 'You were not the first. You will not be the last. We are the same. Run'), distinct from any facility, population, or reputational debt. Vael Korr-Drennen's continued registry search (this same wave, MCD-1659) surfaces a declassified transfer record naming a still-active containment designation, CP-609, held by one of the smaller semi-independent operations that inherited fragments of the Directorate's methodology, whose incomplete intake profile closely resembles CP-414's own final months. Lauris treats CP-414's dying words as an unfulfilled instruction rather than a closed memory, and -- departing from her usual reflex to act the moment she has enough information -- deliberately slows to confirm the record's currency and assess whether an approach would endanger the subject faster than patience would, rather than repeat the clean termination she gave CP-414 herself. Deepens rather than resolves the debt; whether CP-609 is genuinely still living, can be reached, or can be helped to 'run' in any real sense all remain open at the entry's close. New designation CP-609 (Directorate-style designation, not a proper name), collision-checked clean.",
        "status": "locked",
        "source": SOURCE,
    },
    # Strand W, part 1 -- Chronicles XLVII-LII, MCD-1664-1669
    {
        "id": "MCD-1664",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XLVII, 'The Thirty-First Point' (full text at docs/lords-of-cian/chronicles/lauris-chronicle-xlvii-the-thirty-first-point.md): a stakes-free training-deck sparring session between Lauris and Valen (Sinisterblade), extending MCD-215's 'sparring companionship' clause into its own dedicated scene for the first time -- her combat-joy (CC-134) shown against his already-locked 99.97%-efficiency perfectionism (CC-035 extension). No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1665",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XLVIII, 'The Watch He Didn't Ask Her to Keep' (full text at docs/lords-of-cian/chronicles/lauris-chronicle-xlviii-the-watch-he-didnt-ask-her-to-keep.md): a stakes-free night scene on a rampart with Ozmund Verehimu and Lilith Cyzak, extending MCD-215's 'adequate-but-undemonstrative ties to the rest of the crew' clause into its own dedicated entry for the first time -- Lauris's joy (CC-134) shown as counterweight to Ozmund's carried doubt, without touching his Crown-Scar, command, or succession material. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1666",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XLIX, 'What the Spark Sets Down' (full text at docs/lords-of-cian/chronicles/lauris-chronicle-xlix-what-the-spark-sets-down.md): a stakes-free evening with Anansi, a second register of MCD-215's 'adequate-but-undemonstrative' clause -- Lauris's joy (CC-134) shown as counterweight to Anansi's carried rage, consistent with his role as 'the Spark' of the revolutionary trio, without touching his classified sibling bond to Valeria Korth or any operational material. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1667",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle L, 'Two Kinds of Patience' (full text at docs/lords-of-cian/chronicles/lauris-chronicle-l-two-kinds-of-patience.md): a stakes-free evening with Orlok on a rare visit to the crew, a third register of MCD-215's 'adequate-but-undemonstrative' clause -- a philosophical exchange between the setting's two oldest present-day figures on witness and time, deliberately not detailing Orlok's Pavilion/Frequency Vigil secrets. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1668",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LI, 'The Bout With No Score Kept' (full text at docs/lords-of-cian/chronicles/lauris-chronicle-li-the-bout-with-no-score-kept.md): a second, deliberately distinct entry with Valen, dramatizing MCD-215's 'low conversational volume across long durations' clause almost literally across a near-wordless three-hour sparring session, distinct register from MCD-1664. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1669",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LII, 'The Four Who Rarely Share a Room' (full text at docs/lords-of-cian/chronicles/lauris-chronicle-lii-the-four-who-rarely-share-a-room.md): closing entry of this Strand W wave-part -- a single stakes-free evening where Ozmund Verehimu, Valen, Anansi, and Orlok are all incidentally present together with Lauris for the first time in the series, putting CC-134's full 'counterweight' framing (Kanja/grief, Ozmund/doubt, Ezio/deception, Anansi/rage, Valeria/perception, Sephtis/time, Lauris/joy) directly on the page as a synthesizing reflection. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    # Strand W, part 2 -- Chronicles LIII-LIX, MCD-1670-1676
    {
        "id": "MCD-1670",
        "category": "lauris-character-chronicle",
        "statement": "'The Archive He Never Let Anyone Touch' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-liii-the-archive-he-never-let-anyone-touch.md), Lauris Chronicle LIII, Strand W (Witness / present-day, quiet register), second Strand W wave. Fermand Aurelias appears as a participant for the first time in the series rather than only as narrator -- he continues narrating himself in the established third-person Baroque/Zafón-Noir register per CC-034/VB-024, explicitly naming and holding to that discipline. Lauris single-handedly reorganizes 30-plus years of his neglected personal archive (41 crates) in one afternoon, putting CC-134's combat-joy trait on the page in its most domestic register yet. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1671",
        "category": "lauris-character-chronicle",
        "statement": "'The Weight He Asked Her to Carry Gently' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-liv-the-weight-he-asked-her-to-carry-gently.md), Lauris Chronicle LIV, Strand W. Kanja asks Lauris to hold an antique clock's fine brass housing perfectly steady through an hour of delicate repair, seeking her exquisite control rather than raw capacity -- an inversion of expectation extending the Density Saturation Inversion mechanics (ARS-357 through 374). No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1672",
        "category": "lauris-character-chronicle",
        "statement": "'What Two Ledgers Agreed On' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lv-what-two-ledgers-agreed-on.md), Lauris Chronicle LV, Strand W. Garren Hask (CC-115, the crew's ledger-keeper) and Lauris spend an evening jointly reconciling a mis-tallied cargo manifest -- a deliberate thematic echo, not a repeat, of Chronicle V's 'two archives' evening with Sephtis: practical bookkeeping rather than ancient architecture. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1673",
        "category": "lauris-character-chronicle",
        "statement": "'Two Words Were Enough' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lvi-two-words-were-enough.md), Lauris Chronicle LVI, Strand W. Callum Breck (CC-117/118/119) and Lauris mend a fishing net together in near-total, comfortable silence, consistent with his established post-silence economy of functional speech rather than restaging his silence arc itself. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1674",
        "category": "lauris-character-chronicle",
        "statement": "'Read It Right the First Time' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lvii-read-it-right-the-first-time.md), Lauris Chronicle LVII, Strand W. Efa Gol (CC-130) teaches Lauris to read cargo-stack load-failure tells by pattern recognition -- a rare entry showing Lauris genuinely still learning a skill, met with unguarded enjoyment rather than impatience. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1675",
        "category": "lauris-character-chronicle",
        "statement": "'A Number, A Material, A Conclusion' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lviii-a-number-a-material-a-conclusion.md), Lauris Chronicle LVIII, Strand W. Dol Maren (CC-120, he/him per the Batch 226 pronoun reconciliation) assesses and repairs a personal keepsake of Lauris's own -- the series' first non-military request to him -- in his established terse number/material/conclusion reporting format. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1676",
        "category": "lauris-character-chronicle",
        "statement": "'What She Says to Things That Can't Answer' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lix-what-she-says-to-things-that-cant-answer.md), Lauris Chronicle LIX, Strand W, closing this second Strand W wave. Pell Ostra (CC-132/133, who addresses her materials as collaborators rather than commanding them) and Lauris discover a genuine kinship: both 'ask' rather than command what they work with, Ostra her compounds and Lauris her own density. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]

    assert len(new_ids) == 50, f"expected 50 new rules, got {len(new_ids)}"
    assert len(set(new_ids)) == 50, "duplicate IDs within NEW_RULES"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    expected_range = {f"MCD-{n}" for n in range(1627, 1677)}
    assert set(new_ids) == expected_range, f"ID range mismatch: {set(new_ids) ^ expected_range}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 299,
            "source": "Original invention, chat-drafted 2026-09-18, Lauris Character Chronicle wave (Chronicles X-LIX)",
            "rule_count": 50,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = f"{round(float(ledger['ledger_version']) + 0.1, 1)}"
    ledger["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate IDs found after merge!"

    print(f"Batch 299 merged. Ledger now at version {ledger['ledger_version']}, "
          f"{len(ledger['rules'])} rules, {len(ledger['batches_completed'])} batches.")
    print(f"Zero duplicate IDs confirmed across {len(ids)} rules.")


if __name__ == "__main__":
    main()
