#!/usr/bin/env python3
"""
Batch 300: Lauris Letitia's second 50-Chronicle wave (Chronicles LX through CIX).

Eight parallel background agents drafted a second 50-entry wave across Lauris's established
four-strand Character Chronicle convention (Strand K: Kares Prime/deep past, Strand D: Sealbound
Directorate operations, Strand L: the Ledger/present-day operational debts, Strand W: Witness/
present-day quiet register), matching the block-structure precedent set by her own first 50-Chronicle
wave (Batch 299) and Daba's 50-Chronicle launch wave (Batch 296).

Abad's approval, quoted verbatim: "go" -- given directly in response to the proposed 8-agent
strand/block structure for this second wave.
"""
import json
from datetime import datetime, timezone

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-18, Lauris Character Chronicle wave (Chronicles LX-CIX)."

BATCH_NOTE = (
    'Lauris Letitia\'s second 50-Chronicle wave (Chronicles LX-CIX, MCD-1677 through MCD-1726), drafted '
    'by 8 parallel background agents continuing her established four-strand convention. Strand K (Kares '
    'Prime/deep past, 12 entries, Chronicles LX-LXXI): wave 3a (LX-LXV) fills the previously-undramatized '
    '~1,100-year gap between age 114 (Chronicle XIII) and Velith\'s death (age ~1,200, Chronicle XIV); '
    'wave 3b (LXVI-LXXI) pays off Chronicle XXI\'s reserved hook, dramatizing the full departure sequence '
    '(age ~3,580-4,000) MCD-174 covers in summary -- the Iron-Speaker deliberation, Selene\'s death, '
    'farewells, and the journey to the Olmedrin departure point. Strand D (Sealbound Directorate '
    'operations, 13 entries, Chronicles LXXII-LXXXIV): full-scene treatment for Operations 1, 3, 7, 8, 9, '
    '10, 11 (wave 3a, closing the Apprentice Contracts and opening the Established Hunter period) and '
    'Operations 18, 23, 24, 27, 32 (half of the MCD-190 pair, Operation 34 left untouched), and 36 (wave '
    '3b), all while continuing to avoid Operations 25, 30, 34, 38, and 40 (all reserved). Strand L (the '
    'Ledger, present-day debts, deepen-don\'t-resolve, 12 entries, Chronicles LXXXV-XCVI): wave 3a and 3b '
    'both continue existing threads (Corin Halvet, Tevan Kesk, CP-609, Aerelin\'s favor) and originate new '
    'ones (Operation 28\'s curriculum-leak question, Captain Drenneth\'s twelve crew, the Brokenwall/'
    'Velaris node-builder, a second concealed-population generation, an unidentified K-Theta visitor, her '
    'own early biological sampling) -- every entry ends without resolution. Strand W (Witness, '
    'present-day quiet register, 13 entries, Chronicles XCVII-CIX): wave 3a features previously-thin crew '
    '(Damu, Abyss, Matar, Cooper, Valeria Korth, Danne Sok); wave 3b gives second entries to Valen, '
    'Ozmund, Anansi, Orlok, Kanja, and Efa Gol in genuinely distinct registers, closing on a dockside-crew '
    'group scene (Garren Hask, Callum Breck, Efa Gol, Dol Maren, Pell Ostra) that closes the entire wave. '
    'New named characters, all minor and collision-checked clean against the full ledger and each other: '
    'Rassa (Strand K, a surviving cohort member), Merel Vantree (Strand D, self-corrected from an initial '
    '"Sela Vantree" after the agent caught a collision with the already-locked Arbitrator Sela of House '
    'Kestrion, ASH-057), Ossen Fael (Strand D, a minor depot clerk), and the Halfmoon Tide (Strand D, a '
    'Directorate vessel name). One in-flight typo was self-corrected by the Strand K wave-3a agent before '
    'finalizing (a rule-ID reference). Lauris now has 109 Chronicles total (I-CIX). Same process as her '
    'first wave and Daba\'s launch wave: files committed progressively with "Locked canon" headers already '
    'in place under the blanket authorization, the ledger merge itself running only after all 8 agents\' '
    'output and the cross-agent collision sweep were complete. Abad\'s approval, quoted verbatim, given '
    'directly in response to the proposed 8-agent strand structure: "go."'
)

NEW_RULES = [
    # Strand K, wave 3a (age 114-1200 gap) -- Chronicles LX-LXV, MCD-1677-1682
    {
        "id": "MCD-1677",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LX, 'The Century That Learned to Sit Still' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lx-the-century-that-learned-to-sit-still.md), the sixtieth entry in Lauris Letitia's own Chronicle series and the thirteenth entry of Strand K (Kares Prime / deep past), opening the previously-undramatized ~1,100-year span between the close of the no-ceiling calibration period (age 114, Chronicle XIII, MCD-1630) and Velith's death (age ~1,200, Chronicle XIV, MCD-1631). Dramatizes the Sister-Hold's formal transition from crisis-rotation training to a standing, permanent instructor roster, and Tiramen's earliest private observations that would, decades later, begin the work already locked at MCD-169. No new named characters; reuses Veska Karth-Ven, Tiramen Karth-Ven, and Voreth Karth-Ven, all already locked. No contradictions with existing canon.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1678",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXI, 'What Velith Carried Between Visits' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxi-what-velith-carried-between-visits.md), the sixty-first entry in Lauris Letitia's own Chronicle series and the fourteenth entry of Strand K. Set at age ~280, dramatizes a scheduled Threnarr visit deepening the friendship with Velith already locked at MCD-165/1553 and the correspondence pattern established at Chronicle XI (MCD-1628). Shows Velith entering Threnarr's defensive complement, the same body Chronicle XIV (MCD-1631) already establishes was drawn in part from the cohort of forty-seven children and in which Velith is later killed, extending rather than contradicting that entry. Reuses Iron-Speaker Vann (MCD-1627). No new named characters. No contradictions with existing canon.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1679",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXII, 'The Stance Veska Kept Rebuilding' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxii-the-stance-veska-kept-rebuilding.md), the sixty-second entry in Lauris Letitia's own Chronicle series and the fifteenth entry of Strand K. Dramatizes a training session at age ~400, within the age-200-600 window already locked at MCD-170 for the kinetic-anchor stance behind the Phalanx's Triad-Lock configuration, trained under Veska. Uses 'Triad-Lock' as a period-native Karth-Ven stance name, matching the precedent already established by Chronicle XV (MCD-1632). Deliberately does not use the name 'Karth-Sera,' does not depict the curriculum as a named, unified system, and does not depict Spine of Dagon, the Aristocrat, or Attia's Rite, consistent with MCD-176's locked fact that those weapon-names bind to their disciplines only later, on Cian. No new named characters. No contradictions with existing canon.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1680",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXIII, 'What the Upper Archive Asked to Borrow' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxiii-what-the-upper-archive-asked-to-borrow.md), the sixty-third entry in Lauris Letitia's own Chronicle series and the sixteenth entry of Strand K. Dramatizes an informal, pre-Directorate instance of Lauris's 'careful witness' discipline (MCD-161) being called on in a civic, non-combat capacity at age ~750 to resolve an inter-Vask boundary-record dispute -- an unofficial precursor to, and deliberately distinct from, the three inter-Vask disputes formally counted among her twenty-three Long Operational Period deployments (MCD-1555, age 1,841-3,400). Extends Veska's established role as keeper of the cooperative-era upper-tier archives (MCD-167). No new named characters. No contradictions with existing canon.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1681",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXIV, 'The Point Where a Body Would Fail First' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxiv-the-point-where-a-body-would-fail-first.md), the sixty-fourth entry in Lauris Letitia's own Chronicle series and the seventeenth entry of Strand K. Dramatizes a training session at age ~950, within the age-600-1,100 window already locked at MCD-170 for the structural-breach strike trained under Tiramen -- shown as a still-unnamed precision technique rather than as 'Spine of Dagon,' consistent with MCD-176's locked fact that her four disciplines take on their weapon-names only later, on Cian. Extends her Hexa-Lamellar Lattice physiology (MCD-157/159) and Tiramen's established role as adaptive-methodology specialist (MCD-167). No new named characters. No contradictions with existing canon.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1682",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXV, 'The Last Ordinary Afternoon' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxv-the-last-ordinary-afternoon.md), the sixty-fifth entry in Lauris Letitia's own Chronicle series, the eighteenth and closing entry of Strand K for wave 3a. Set at age ~1,180, roughly twenty years before Velith's death in a Vask Threnarr defensive operation (age ~1,200, already locked at MCD-165/1631), this entry deliberately closes the ~1,100-year gap opened at Chronicle LX by ending at the exact threshold of Chronicle XIV without depicting the engagement itself, matching the wave-one precedent of Chronicle XXI closing at a threshold rather than a resolution. No new named characters. No contradictions with existing canon.",
        "status": "locked",
        "source": SOURCE,
    },
    # Strand K, wave 3b (departure sequence) -- Chronicles LXVI-LXXI, MCD-1683-1688
    {
        "id": "MCD-1683",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXVI, 'What the Three Reasons Cost Her' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxvi-what-the-three-reasons-cost-her.md), the sixty-sixth entry in Lauris Letitia's own Chronicle series, the ninth entry of Strand K and the opening entry of this wave's departure sequence -- the direct payoff to the hook Chronicle XXI (MCD-1638) deliberately left open. Set roughly 180 years after Chronicle XXI, at age ~3,580, the far edge of MCD-174's decision window. Dramatizes the private articulation maturing into an actual decision: the ~180-year research period MCD-174 already locks, conducted at Vask-of-Vasks (the civilization's cultural/archival center, MCD-160), closing on the specific reasoning behind choosing Cian (the Kareth War-Order, the Sealbound Directorate's inherited Ionic-Rite methodology, and Living Drakma deposits approaching Kares Prime's own). No new named characters. No contradictions.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1684",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXVII, 'What a Civilization Takes Its Time Deciding' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxvii-what-a-civilization-takes-its-time-deciding.md), the sixty-seventh entry in Lauris Letitia's own Chronicle series, the tenth entry of Strand K. Set at age ~3,580-3,600, immediately following Chronicle LXVI (MCD-1683). Dramatizes the opening of the Iron-Speaker deliberation already locked at MCD-174 (380 years, before agreeing to support her departure) -- the formal presentation of her decision to the assembled Iron-Speakers via Veska Karth-Ven's sponsorship, and the earliest, most contested years of a genuinely divided Council. Reuses Veska Karth-Ven. One unnamed senior Iron-Speaker voice, matching the established convention for secondary figures in this strand (Chronicles II, XVI, XVIII). No new named characters. No contradictions.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1685",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXVIII, 'The One Thing They Asked in Return' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxviii-the-one-thing-they-asked-in-return.md), the sixty-eighth entry in Lauris Letitia's own Chronicle series, the eleventh entry of Strand K. Set at age ~3,960, roughly 380 years after Chronicle LXVII (MCD-1684) opened the Iron-Speaker deliberation, closing it exactly as MCD-174 already locks: the Council agreeing to support her departure and asking only that she preserve a record of what she found -- the origin scene for the standing archive debt already locked at MCD-211. Reuses Veska Karth-Ven and the unnamed dissenting Iron-Speaker from Chronicle LXVII. No new named characters. No contradictions.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1686",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXIX, 'Thirty Seconds' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxix-thirty-seconds.md), the sixty-ninth entry in Lauris Letitia's own Chronicle series, the twelfth entry of Strand K. Set at age ~3,972, roughly 28 years before her scheduled departure and following the Iron-Speaker agreement in Chronicle LXVIII (MCD-1685). Dramatizes directly, for the first time, Selene's death in a Vask Threnarr defensive action already locked at MCD-174 -- Lauris fighting at her side, killing the attacker within thirty seconds of Selene's death, too late -- and the writing of the archive line already locked at MCD-1558 in its full original context for the first time. No new named characters; reuses Selene, already locked. No contradictions.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1687",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXX, 'Everyone She Had Time Left to See' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxx-everyone-she-had-time-left-to-see.md), the seventieth entry in Lauris Letitia's own Chronicle series, the thirteenth entry of Strand K. Set across the final months before departure, age ~3,999, in the interval MCD-174 establishes between Selene's death (Chronicle LXIX, MCD-1686) and the departure itself. Dramatizes her farewell circuit of her cohort at Vask Threnarr (the original 47-child cohort, MCD-165) and her instructors at Vask Karth-Ven, closing on a final private visit to Karth-Ven's central training floor -- the same floor Chronicle XX (MCD-1637) showed failing to measure her -- before she leaves the Vask for the last time. Reuses Veska Karth-Ven, Tiramen Karth-Ven, and Voreth Karth-Ven, all already locked. Introduces one new minor named character, Rassa (collision-checked clean, zero prior hits), a surviving member of Lauris's original cohort, for a single farewell scene. No contradictions.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1688",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXI, 'The World Is Below Me' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxi-the-world-is-below-me.md), the seventy-first entry in Lauris Letitia's own Chronicle series, the fourteenth entry of Strand K and the closing entry of this wave's departure sequence. Set at age ~4,000, in the final weeks and hours before the departure already locked at MCD-174 -- the journey to and arrival at the Vask Olmedrin orbital trade-point, the gathering of roughly 1,200 Karesian women to see her off, and her own final recorded line on departing Kares Prime, already locked at MCD-1558, placed in its full original context for the first time. Ends at the literal threshold of departure without depicting the journey to Cian itself, which MCD-175 already covers directly. Reuses Serath, already locked (MCD-1636), now Olmedrin's senior training authority. No new named characters. No contradictions.",
        "status": "locked",
        "source": SOURCE,
    },
    # Strand D, wave 3a (Operations 1-11) -- Chronicles LXXII-LXXVIII, MCD-1689-1695
    {
        "id": "MCD-1689",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXII, 'The Line That Let Her Through' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxii-the-line-that-let-her-through.md), a Strand D (Sealbound Directorate years) entry in her Character Chronicle series. Full-scene treatment of Operation 1, her very first Directorate contract (previously only summarized in passing at MCD-1542): alone and unescorted, she walks the length of a 58-person hostile debtors' picket line at the Tallow Road tithe post near Kesmara's Eastern District, unrecognized as a threat until she has already freed the two held Directorate clerks, well ahead of the requested four-hour-out enforcement column. Set within her ten Apprentice Contracts, with mentor Vael Korr-Drennen (MCD-177) present; dramatizes directly, for the first time, the exact moment behind his later mentorship-report line, placing it explicitly on this contract's second day. No new named characters. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1690",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXIII, 'What the Iron-Spire Would Not Strike' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxiii-what-the-iron-spire-would-not-strike.md), a Strand D entry giving full-scene treatment to Operation 3, the Iron-Spire (previously only summarized at MCD-178 as a malfunctioning resonance node whose defensive subroutines could not harm Karesian biology). Set within the Apprentice Contracts, in the high country above the Korren Highlands. Dramatizes her methodical three-pass testing of the tower's blade-constructs, which open for every intruder except her, and her cross-referencing of the site's four-century death record, finding every confirmed death caused by panic or fall rather than direct contact -- the first documented seed of the pattern-noticing later Chronicles (MCD-1537/Chronicle III) describe her tracking since Operation 3, deliberately left unresolved here. No new named characters. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1691",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXIV, 'Fourteen Voices, One Field' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxiv-fourteen-voices-one-field.md), a Strand D entry giving full-scene treatment to Operation 7, the Black Choir's substation (previously only summarized at MCD-178: a resonance field that had induced collective vocal-amplification capability in fourteen ungifted women). Set within the Apprentice Contracts at the Velkar mill-works. Dramatizes her four-day consensual testing of the fourteen affected laundry-workers' stable, non-hazardous capability, and her decision to file a report stating the field had fully dispersed rather than disclose the surviving capability -- the earliest instance of the selective-disclosure pattern MCD-1646/Chronicle XXIX later confirms recurring at Operation 22, occurring years earlier and for the first time. One new minor named character, Merel Vantree (the fourteen women's informal spokeswoman), collision-checked clean against the full ledger. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1692",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXV, 'The Container She Did Not Open' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxv-the-container-she-did-not-open.md), a Strand D entry giving full-scene treatment to Operation 8, the sealed Velkar riverbed container (previously only summarized at MCD-178: of unknown contents, delivered unopened to the Directorate's senior archive, where it remains sealed in the present day). Set within the Apprentice Contracts, reusing the already-locked Velkar riverbed location (MCD-1534, Operation 4). Dramatizes her recovery of the anomalously dense, faintly humming container and her deliberate choice not to open it despite genuine temptation, trusting the Directorate's own caution -- deliberately preserves the contents as unknown, matching MCD-178's present-day framing exactly; no reveal. No new named characters. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1693",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXVI, 'The Column That Did Not Balance' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxvi-the-column-that-did-not-balance.md), a Strand D entry giving full-scene treatment to Operation 9, previously entirely undrafted and unmentioned by number anywhere in the ledger. Original invention consistent with MCD-178's framing of the Apprentice Contracts' final two operations: a routine grain-tithe reconciliation contract during which Lauris independently and privately notices a small, consistent manifest discrepancy tracing to Operations Director Iyellen Macresh's own countersignature -- deliberately established as unreported and unconnected to the separate Internal Affairs investigation MCD-178 already confirms failed three times before Operation 10 was assigned to her; her own observation here plays no causal role in that process. One new minor named character, depot clerk Ossen Fael, collision-checked clean. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1694",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXVII, 'The Contract With Her Own Name On It' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxvii-the-contract-with-her-own-name-on-it.md), a Strand D entry giving full-scene treatment to Operation 10, previously only summarized at MCD-178: Operations Director Iyellen Macresh, exposed for embezzlement after three failed Internal Affairs attempts, terminated by Lauris herself at Iyellen's own private estate in the Kesmara Eastern Hills, closing the Apprentice Contracts. Dramatizes directly, for the first time, the mentorship-report line already locked at MCD-177, showing Vael Korr-Drennen filing it the same week this contract closes. References Chronicle LXXVI's Operation 9 discrepancy as a private, unconnected echo rather than its cause, per that entry's own stated sequence. No new named characters. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1695",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXVIII, 'Ninety Seconds Under the Bow' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxviii-ninety-seconds-under-the-bow.md), a Strand D entry giving full-scene treatment to Operation 11, the juvenile Tide-Wraith engagement (previously only summarized in a paired rule with Operation 21 at MCD-1545). Operation 11 opens the Established Hunter period (MCD-179: Operations 11 through 22); this entry is written as her first contract of that period, immediately following Chronicle LXXVII's Operation 10. Dramatizes in full combat detail the already-locked jaw-severing and spine-pursuit termination technique aboard the bait vessel the Halfmoon Tide, ending the engagement in the already-locked roughly ninety seconds with zero crew casualties, and shows the earliest informal crew reach for language about her, seeding the Established Hunter-era nicknaming pattern (MCD-1539). One new minor named element, the Directorate vessel the Halfmoon Tide, collision-checked clean. No contradictions with any already-locked rule.",
        "status": "locked",
        "source": SOURCE,
    },
    # Strand D, wave 3b (Operations 18-36) -- Chronicles LXXIX-LXXXIV, MCD-1696-1701
    {
        "id": "MCD-1696",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXIX, 'The Woman Who Spoke Like Home' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxix-the-woman-who-spoke-like-home.md), a Strand D entry in her Character Chronicle series, gives full-scene treatment to Operation 18, the Verith engagement (previously only summarized at MCD-180), in the closing stretch of the Established Hunter period. Dramatizes the contract as a direct consequence of what Operation 13 had already taught her about what 'delivered alive' can quietly become once a subject leaves her hands (MCD-1642, Chronicle XXV), and dramatizes the moment MCD-180 already locks as the first engineered Karesian she encountered alive and the moment she stopped considering herself the last of her kind on Cian. The deferred conversation with Val Mirel Kareth that MCD-180 reserves is referenced only as an unresolved debt, never dramatized. No new named characters; Verith already locked.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1697",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXX, 'What the Polarity Apparatus Remembered' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxx-what-the-polarity-apparatus-remembered.md), a Strand D entry in her Character Chronicle series, gives full-scene treatment to Operation 23, the Iron-Halls of Velkar (previously only summarized at MCD-181), opening this wave's run through the Specialist sub-period. Dramatizes the malfunctioning polarity-control apparatus and the cooperative-era Karesian technical instrumentation Lauris found written into it, letting her independently form, as a private working theory well ahead of her later Directorate-sourced confirmation, that the K-strand decline (MCD-153 through MCD-157) had been deliberate engineering rather than natural catastrophe, and that whoever was responsible had obtained material directly from Kares Prime during the deep cooperative era. Notes the already-locked naming coincidence distinguishing this site from Kares Prime's own Iron-Halls of Vask. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1698",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXXI, 'A Third Kind of Body' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxxi-a-third-kind-of-body.md), a Strand D entry in her Character Chronicle series, gives full-scene treatment to Operation 24, the fluctuating-density entity designated Subject AE-001 (previously only summarized at MCD-182), continuing the Specialist sub-period. Dramatizes the encounter MCD-182 already locks as Lauris's first direct evidence that the engineering tradition's source materials were not limited to Karesian biology, and that other, unidentified species were being processed by the same apparatus at facilities she had not yet located. No new named characters; Subject AE-001 stays a bare designation, matching MCD-182's own phrasing.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1699",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXXII, 'What Was Still Growing Beneath the Trench' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxxii-what-was-still-growing-beneath-the-trench.md), a Strand D entry in her Character Chronicle series, gives full-scene treatment to Operation 27 (previously only summarized at MCD-185, with tactical precedent already dramatized at MCD-1545 for Operations 11 and 21), continuing the Specialist sub-period. Dramatizes the location and destruction of a Tide-Wraith breeding substrate in the Voskharen Trench -- roughly 14 adults, ~400 juveniles, and the generative substrate itself -- and the revelation that the species was engineered rather than naturally evolved, an Ionic-Rite-derived production line believed, at the time, biologically extinguished on Cian. Deliberately leaves that belief exactly as uncertain as MCD-185 itself leaves it, without asserting or foreshadowing Operation 39's later disproof. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1700",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXXIII, 'The Costliest Thing She Ever Broke' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxxiii-the-costliest-thing-she-ever-broke.md), a Strand D entry in her Character Chronicle series, gives full-scene treatment to the Operation 32 half of MCD-190 (previously only summarized there alongside the separate, later Operation 34, which this entry deliberately does not touch and which remains reserved), deep in the Disillusionment sub-period. Dramatizes the destruction of a Living-Drakma-adjacent biological raw-material production substrate off the Voskharen coast -- MCD-190's own framing as the single most damaging act of sabotage against the engineering tradition in Lauris's contractor career -- as her first unilateral strike against the supply chain itself, extending the trajectory from Chronicle XXXIII's (MCD-1650) Operation 31 alliance with Aerelin. Does not reference Site K-Theta, the Anu Un Ra name reveal, or any Operation 34 content. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1701",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXXIV, 'What the Central Node Left Behind' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxxiv-what-the-central-node-left-behind.md), a Strand D entry in her Character Chronicle series and this wave's closing Strand D entry, deep in the Disillusionment sub-period. Gives full-scene treatment to Operation 36 (previously only summarized within MCD-191): the discovery and destruction of fourteen smaller redundancy nodes at the Vask of the Hollow, missed by her Operation 20 central-node destruction (already dramatized at Chronicle XXVI, MCD-1643), confirming the engineering tradition built distributed redundancy into its facilities generally. Closes the Vask of the Hollow arc Chronicle XXVI left open, and extends its 'no longer subtle' throughline into a new, deliberately unresolved dread: whether other sites she once considered closed conceal the same kind of redundancy. No new named characters; Aerelin's network (MCD-189/191) referenced consistently with its already-locked role.",
        "status": "locked",
        "source": SOURCE,
    },
    # Strand L, wave 3a -- Chronicles LXXXV-XC, MCD-1702-1707
    {
        "id": "MCD-1702",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXXV, 'The Trial She Would Not Call a Precedent' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxxv-the-trial-she-would-not-call-a-precedent.md), continues the Corin Halvet thread (MCD-1658) without resolving it: Lauris returns months later with a limited, supervised trial rather than a final ruling -- Halvet takes up an ordinary trade under a chosen name in a border settlement, watched at a discreet distance by one of Aerelin's operatives -- and is explicit that this is a single case study, not a policy. The debt widens rather than closes when two further Operation 37 survivors, hearing of Halvet's trial, independently ask for the same consideration; Lauris has not answered either request. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1703",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXXVI, 'A Story Sold More Than Once' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxxvi-a-story-sold-more-than-once.md), continues the Tevan Kesk reputational-debt thread (MCD-1660) without resolving it: a search surfaces two further debt-collectors on trade roads well beyond Kesk's own territory invoking a description closely matching 'the Petite Catastrophe' in nearly identical language, suggesting one common story circulating rather than three men separately inventing the same threat. Whether the spread is accidental drift or a deliberately seeded story, and who the 'itinerant trader' Kesk named actually was, remain unresolved; Vael Korr-Drennen has agreed to search further. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1704",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXXVII, 'The Road to Where She Is Recognizable' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxxvii-the-road-to-where-she-is-recognizable.md), continues the CP-609 thread (MCD-1663) without resolving it: a second transfer record confirms CP-609's designation was still active within an active intake as recently as eleven months prior, and a separate inquiry indicates the holding operation may be managing a population transfer within the current season, destination and timeline uncertain. Lauris departs to reach the site before any transfer completes; the entry ends with her en route, not arrived. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1705",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXXVIII, 'A Curriculum That Was Never Only Hers' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxxviii-a-curriculum-that-was-never-only-hers.md), originates a new standing debt extending Operation 28's unresolved discomfort (MCD-186): Lauris asks for the first time whether the reverse-engineered Karth-Sera fragment the engineering tradition built from observing her own operational behavior died with the Operation 28 subject or continued to be used afterward. A joint search with Vael Korr-Drennen finds no confirmed further subject, but surfaces scattered combat-assessment notes describing an unusually 'economical' fighting style neither woman can confirm or rule out as Karth-Sera-derived. Deliberately inconclusive; the search continues. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1706",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle LXXXIX, 'Twelve Names She Never Asked For' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-lxxxix-twelve-names-she-never-asked-for.md), originates a new standing debt extending Operation 13's already-locked aftermath (MCD-1546): Lauris realizes she has never investigated the fate of the twelve Iron Veth crew she disabled rather than killed during the same boarding that delivered Captain Drenneth alive, who died in processing regardless. A joint search finds four confirmed released, three transferred to a processing annex matching the same 'charter quietly dissolved' pattern already traced once in the Sample K-403 search, and five records that simply stop with no notation. The search continues. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1707",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XC, 'A Second Hand, Found Again' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xc-a-second-hand-found-again.md), originates a new standing debt extending the unresolved Brokenwall/Velaris planted-node question (MCD-1538, deliberately left unresolved whether the activations were Anu Un Ra's apparatus or a separate actor): a report reaches Lauris of a similarly constructed resonance-keyed device, discovered and disabled before triggering, in an unrelated border settlement. Whether the device is old and only now discovered, or newly planted -- implying the original actor remains active decades later -- cannot yet be determined; Lauris has requested it be secured intact for her own examination, not yet performed. Closes wave 3a's Strand L run. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    # Strand L, wave 3b -- Chronicles XCI-XCVI, MCD-1708-1713
    {
        "id": "MCD-1708",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XCI, 'The Question He Was Not Alone In Asking' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xci-the-question-he-was-not-alone-in-asking.md), continues Corin Halvet's still-undecided request to leave concealment (MCD-1658) without resolving it. Returning to Operation 37's roughly 280-strong concealed population (MCD-191) some months later, Lauris listens rather than polls, and confirms at least two further members have quietly wondered the same thing and never asked. The precedent she is weighing is no longer Corin Halvet's alone. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1709",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XCII, 'Those Who Never Knew Outside' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xcii-those-who-never-knew-outside.md), opens a distinct debt within Operation 37's population (MCD-191): a first native-born second generation has reached adulthood having known nothing but concealment. Their eldest asks Lauris not to leave, but raises a harder question she has no framework for: whether protection extended to a parent can still be called consent once it becomes the only world a child has ever known. Deliberately left open. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1710",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XCIII, 'What Fatigue Could Not Explain' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xciii-what-fatigue-could-not-explain.md), advances the Aerelin favor thread (MCD-1661): Lauris travels alone to observe covertly rather than approach the straining operative, confirming the fatigue Aerelin's distant analysis flagged is real, and noticing one procedural irregularity that is ambiguous between early surveillance and unrelated office politics. She reports an ambiguous read rather than a verdict, honoring the personal-terms condition (MCD-194) without resolving whether extraction is necessary. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1711",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XCIV, 'The Fragment She Called Inert' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xciv-the-fragment-she-called-inert.md), opens a new archival debt among the roughly fourteen sealed artifacts recovered across her Directorate career (MCD-1560): a control fragment salvaged from the Vask of the Hollow's central node during Operation 20 (MCD-1537), delivered under a generic inert-wreckage classification. Cross-referencing the resonance-keying mechanics traced at Settlement K-447, Brokenwall, and Velaris, she now suspects the fragment may retain independent keying capability, and finds -- consistent with Sample K-403's own reclassification (MCD-1655) -- that Directorate reorganizations have scattered the record of where it went. Deliberately left unlocated. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1712",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XCV, 'The Hand That Wasn't Hers' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xcv-the-hand-that-wasnt-hers.md), opens a new debt at Site K-Theta's relocated concealment site (MCD-190/193): a routine rotation visit finds small, competent signs that someone other than Lauris has recently been there -- a resupply and a structural repair she did not make. She cannot confirm or rule out a connection to Val Mirel Kareth's own parallel-aligned War-Order operatives (MCD-198/212) and does not attempt to find out, consistent with the standing non-contact arrangement. Deliberately does not advance or touch the K-Theta reveal-to-Kanja detail reserved at MCD-193. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1713",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XCVI, 'What She Let Them Take' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xcvi-what-she-let-them-take.md), opens a new debt concerning Lauris's own body: reviewing old intake records for an unrelated purpose, she confirms in writing for the first time that her own original Directorate intake included routine biological sampling she never questioned at the time. The timing predates Operation 28's engineered subject (MCD-186, 'the Copy'), whose mirrored combat capability she has always attributed to behavioral reverse-engineering alone; she now cannot rule out that a literal sample of her own biology was available considerably earlier. Deliberately left unconfirmed either way, closing wave 3b's Strand L run. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    # Strand W, wave 3a -- Chronicles XCVII-CII, MCD-1714-1719
    {
        "id": "MCD-1714",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XCVII, 'The Condition His Index Had No Page For' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xcvii-the-condition-his-index-had-no-page-for.md), ninety-seventh entry in her own Chronicle series, Strand W (Witness / present-day, quiet register), third Strand W wave. A stakes-free entry pairing Lauris with Damu (Julian Dael-Koss, CC-100), the crew's blood-sense medic -- he asks to take a purely curiosity-driven reading of her biology for his Red Index, which has never catalogued a synthesis-evolution Karesian, and finds no category that fits her. Puts CC-134's combat-joy trait on the page as the pleasure of being read accurately, by choice, for the first time. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1715",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XCVIII, 'The Weight Nobody Else Would Stand Under' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xcviii-the-weight-nobody-else-would-stand-under.md), ninety-eighth entry in her own Chronicle series, Strand W. A stakes-free entry pairing Lauris with Abyss (Ren Oshaal, CC-101), the crew's youngest member -- she becomes his preferred practice partner for controlling his Negative-Density Variant field's active-range output, since her own biology tolerates standing inside it without discomfort. Puts CC-134's combat-joy trait on the page as pleasure taken in a genuine physical limit tested safely. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1716",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle XCIX, 'What the Apothecary Could Not Name' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-xcix-what-the-apothecary-could-not-name.md), ninety-ninth entry in her own Chronicle series, Strand W. A stakes-free entry pairing Lauris with Matar (CC-102), the crew's most reserved member -- an evening spent helping him identify an unlabeled compound in the Apothecary, conducted almost entirely in comfortable silence. Puts CC-134's combat-joy trait on the page in its quietest register yet: satisfaction taken in patient, unhurried, largely wordless work. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1717",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle C, 'What the Manifest Could Not Route' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-c-what-the-manifest-could-not-route.md), one-hundredth entry in her own Chronicle series, Strand W. A stakes-free entry pairing Lauris with Cooper (Ronan Kellsward, CC-103), the crew's logistics specialist -- she helps him solve a supply-cache routing problem by personally testing the terrain's load-bearing capacity, a deliberate variation on Chronicle LV's ledger-reconciliation evening with Garren Hask: a physical problem rather than a bookkeeping one. Puts CC-134's combat-joy trait on the page as satisfaction in a hard, practical puzzle solved by testing rather than counting. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1718",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle CI, 'The Thread She Didn't Need to Cut' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-ci-the-thread-she-didnt-need-to-cut.md), one-hundred-first entry in her own Chronicle series, Strand W. A stakes-free entry pairing Lauris with Valeria Korth (CC-104), whose Thread-Perception biology perceives structural and causal connections as visible threads -- a demonstration undertaken purely for its own sake, on an old disused training vault. Puts CC-134's combat-joy trait on the page as pleasure taken in someone else's mastery, without any need to match or best it. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1719",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle CII, 'The Silence They Shared' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-cii-the-silence-they-shared.md), one-hundred-second entry in her own Chronicle series, closing wave 3a of Strand W. A stakes-free entry pairing Lauris with Danne Sok, one of the three earliest crew members freed before the Black Trench (MCD-234) -- a night watch shared in near-total silence, extending MCD-215's 'adequate-but-undemonstrative ties to the rest of the crew' clause into its own scene. Puts CC-134's combat-joy trait on the page as ease taken in shared, wordless company. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    # Strand W, wave 3b -- Chronicles CIII-CIX, MCD-1720-1726
    {
        "id": "MCD-1720",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle CIII, 'The Patience He Doesn't Save for Her' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-ciii-the-patience-he-doesnt-save-for-her.md), the eighth Strand W entry of this wave. A third, deliberately non-training-deck entry with Valen: he spends an hour correcting an unnamed sentry's basic stance with the same unhurried patience he gives Lauris herself, and Lauris watches from the sidelines rather than participates, putting his Master-at-Arms discipline (MCD-291) on the page from an observer's vantage for the first time. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1721",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle CIV, 'The Loaf That Would Not Rise' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-civ-the-loaf-that-would-not-rise.md), the ninth Strand W entry of this wave. A second Ozmund Verehimu entry, deliberately without Lilith Cyzak and in a lighter register than MCD-1665's rampart scene: Ozmund fails comically at baking bread for a self-hosted gathering, and Lauris's plain delight at his ordinary, consequence-free frustration puts CC-134's counterweight framing on the page through humor rather than grave affirmation. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1722",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle CV, 'The Quiet Work of the Web' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-cv-the-quiet-work-of-the-web.md), the tenth Strand W entry of this wave. A second Anansi entry, distinct from MCD-1666's game of stones: Lauris sits beside him through three hours of unglamorous Ghost-Lattice report-sorting, a register of shared patient labor extending CC-134's counterweight framing to his carried rage. No operational intelligence content or sibling-bond material touched. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1723",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle CVI, 'The First Stone He Ever Struck' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-cvi-the-first-stone-he-ever-struck.md), the eleventh Strand W entry of this wave. A second Orlok entry, distinct from MCD-1667's philosophical dialogue: a physical pilgrimage to the volcanic-ridge stone he first struck as a miner's son roughly 76,000 years ago, the literal origin of his self-taught density manipulation (CC-091), with Lauris the first person he has ever shown it to. Does not touch his Pavilion/Frequency Vigil secrets. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1724",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle CVII, 'The Weight They Moved for No Reason at All' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-cvii-the-weight-they-moved-for-no-reason-at-all.md), the twelfth Strand W entry of this wave. A second Kanja entry, deliberately inverting MCD-1671's exquisite-control register: Kanja and Lauris spend four unhurried minutes moving a meaningless boulder together purely for the pleasure of shared raw capacity, extending MCD-215's operational-deference tie into a purely playful register. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1725",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle CVIII, 'The Second Lesson She Was Promised' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-cviii-the-second-lesson-she-was-promised.md), the thirteenth Strand W entry of this wave. A direct sequel to MCD-1674, paying off Efa Gol's own closing line there: she extends her blunt, precise assessment style (CC-130) from reading cargo stacks to reading people and formations, drawing on her Rebellion command of decoy and diversion forces, and Lauris successfully applies the method unprompted by the entry's close. No new named characters.",
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1726",
        "category": "lauris-character-chronicle",
        "statement": "Lauris Chronicle CIX, 'What the Dock Keeps' (full narrative text at docs/lords-of-cian/chronicles/lauris-chronicle-cix-what-the-dock-keeps.md), the fourteenth and closing Strand W entry of this wave, and the closing entry of the entire second 50-Chronicle wave (Chronicles LX-CIX) across all four strands. A single stakes-free evening gathers Garren Hask, Callum Breck, Efa Gol, Dol Maren, and Pell Ostra together with Lauris for the first time -- a dockside/support-crew configuration distinct from MCD-1669's command-tier gathering -- closing by putting CC-134's full counterweight framing on the page a second time, from the vantage of the crew's ordinary working members. No new named characters.",
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

    expected_range = {f"MCD-{n}" for n in range(1677, 1727)}
    assert set(new_ids) == expected_range, f"ID range mismatch: {set(new_ids) ^ expected_range}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 300,
            "source": "Original invention, chat-drafted 2026-09-18, Lauris Character Chronicle wave (Chronicles LX-CIX)",
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

    print(f"Batch 300 merged. Ledger now at version {ledger['ledger_version']}, "
          f"{len(ledger['rules'])} rules, {len(ledger['batches_completed'])} batches.")
    print(f"Zero duplicate IDs confirmed across {len(ids)} rules.")


if __name__ == "__main__":
    main()
