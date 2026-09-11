#!/usr/bin/env python3
"""Batch 261: Iron Bastard Alias Chronicle waves 22-30 (27 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Iron Bastard's twenty-second through thirtieth Alias Chronicle waves (9 waves, 27 "
    "entries), drafted under Abad's blanket authorization to continue all eleven aliases' waves "
    "22-30 uninterrupted. Nine genuinely new registers: the doctrine's first living/growing "
    "structure and a bio-armored Crawler countermeasure built to exploit it (wave 22); its first "
    "true peer opponent, a Trust-trained diagnostician using the authentic method against Kanja, "
    "left as an open ongoing rivalry rather than resolved (wave 23); a third-generation apprentice's "
    "unsupervised solo debut, a four-listener multi-site campaign, and the first student's dignified "
    "retirement from active field discharge into full-time teaching (wave 24); the doctrine's "
    "darkest entry yet, a cohort graduate who understood the ethical teaching completely and turned "
    "it to extortion anyway, and a settlement's near-ban of the doctrine after the betrayal (wave "
    "25); its first no-enemy citywide earthquake triage and multi-structure rescue, with a fast-read "
    "mode deliberately departing from standard doubled verification under time pressure (wave 26); "
    "its first application to a sacred structure, resolving a temple's fear that an honest read "
    "would cost its congregation's faith (wave 27); the Directorate successor's first formal "
    "cross-faction joint engineering collaboration, resolving a failure caused by uncoordinated dual "
    "repair rather than sabotage (wave 28); Dol Maren's calculation-over-faith request for a hull "
    "verification and the doctrine's first sustained continuous-monitoring application through a "
    "storm (wave 29); and the doctrine's formal academic naming as 'Tension Reading' alongside a "
    "genuinely unresolved new countermeasure that passes every existing safeguard, closing on a "
    "capstone reunion of the full teaching lineage (wave 30). No new named characters were "
    "introduced anywhere in this run, consistent with this alias's long-established convention of "
    "unnamed recurring roles (the Trust scholar, the Directorate general/successor, the first and "
    "second students, the third-generation apprentice, the Trust diagnostician) -- every entry "
    "reused already-locked crew (Garren Hask, Dol Maren) or these established unnamed roles for "
    "continuity depth instead. Abad's approval: \"lets do this 22nd Alias Chronicle wave for any/all "
    "of the eleven aliases to the 30th wave and you are to continue uninterrupted until completion "
    "this includes rigorous testing, commit, push to main origin.\""
)

NEW_RULES = [
    {
        "id": "MCD-1283",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Bridge That Was Still Growing\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-bridge-that-was-still-growing.md), Iron Bastard Alias "
            "Chronicle LXIV, wave 22, first entry. The doctrine's first application to a living, "
            "growing tension-bearing structure -- a settlement's fig-root river crossing, whose "
            "tension signature fluctuates on its own slow cycle rather than holding static. Kanja "
            "learns to distinguish 'living and self-protecting' from 'failing' and defeats a sapper "
            "crew's attempt to sever the bridge's anchor roots by hand without discharging against "
            "the bridge itself, deliberately choosing not to bring down a structure three "
            "generations of the settlement had spent that long growing. The second student (`MCD-719`) "
            "appears in supporting capacity. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1284",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Shell That Grew Around the Iron\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-shell-that-grew-around-the-iron.md), Iron Bastard "
            "Alias Chronicle LXV, wave 22. A detailed, battle-intense full-Trinity combat showcase "
            "against a bio-armored Crawler variant grown with cultivated estuary coral specifically "
            "to exploit the new living/dead diagnostic distinction (`MCD-1283`); Kanja resolves the "
            "ambiguity by recognizing the coral's uniform, seeded growth pattern lacks a genuinely "
            "living structure's self-directed branching, then discharges Obsidian Malice into the "
            "resin bonding layer to crack the shells free before Mafesto's Kinetic Transfer System "
            "and all five of Onyx of Oblivion's named powers (`ARS-020`) clear five of six Crawlers. "
            "The second student (`MCD-719`) appears in supporting capacity. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1285",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Old Tree He Left Standing\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-old-tree-he-left-standing.md), Iron Bastard Alias "
            "Chronicle LXVI, wave 22, closing the wave. A quiet, non-technical closer applying the "
            "living-structure distinction (`MCD-1283`) to an ordinary civilian tree threatening a "
            "granary foundation; Kanja identifies the tree as alive and recommends a shim and root "
            "redirection rather than felling, the deliberate opposite outcome of the condemned "
            "foundry elegy (`MCD-968`) -- correctly read as alive, it is left standing rather than "
            "brought down. No discharge occurs. The second student (`MCD-719`) appears in supporting "
            "capacity. No new named characters. Closes the Iron Bastard's twenty-second wave (with "
            "`MCD-1283` and `MCD-1284`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1286",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Listener on the Other Side\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-listener-on-the-other-side.md), Iron Bastard Alias "
            "Chronicle LXVII, wave 23, first entry. Introduces the doctrine's first genuine peer "
            "opponent: a Trust engineer who has independently mastered the authentic diagnostic-"
            "listening technique (distinct from the crude freelance-mercenary mimicry of `MCD-899` "
            "and the defected engineer's schematics-only contribution at `MCD-716`) over four years "
            "of study, and uses it to feed Kanja a false tension reading on a garrison bridge, "
            "exploiting the doubled-verification protocol's own timing window (`MCD-497`). Kept "
            "unnamed per the alias's established convention of unnamed recurring roles. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1287",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"Two Ears on the Same Bridge\" (full narrative text at "
            "docs/lords-of-cian/chronicles/two-ears-on-the-same-bridge.md), Iron Bastard Alias "
            "Chronicle LXVIII, wave 23. A detailed, deliberately restrained diagnostic duel between "
            "Kanja and the Trust diagnostician (`MCD-1286`) -- Kanja wins not by out-hearing him but "
            "by refusing to trust his own verification pass and instead reading the deceiver's own "
            "stance, applying the ethical-restraint lesson of `MCD-499`. Zero structural damage and "
            "zero discharge of Obsidian Malice; the engagement resolves through Whisper of Shadows "
            "and a grounded defensive block alone. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1288",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Rival Who Wouldn't Defect\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-rival-who-wouldnt-defect.md), Iron Bastard Alias "
            "Chronicle LXIX, wave 23, closing the wave. The Trust diagnostician (`MCD-1286`/`1287`) "
            "declines Kanja's defection offer, explaining his disagreement with the doctrine is "
            "ideological rather than institutional disillusionment (distinct from the engineer's "
            "resolved crossing at `MCD-716`), and is released unescorted -- establishing a genuine "
            "open, ongoing peer rivalry rather than a resolved arc. No new named characters. Closes "
            "the Iron Bastard's twenty-third wave (with `MCD-1286` and `MCD-1287`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1289",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Mission He Watched From Too Far to Help\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-mission-he-watched-from-too-far-to-help.md), Iron "
            "Bastard Alias Chronicle LXX, wave 24, first entry. The third-generation apprentice "
            "(`MCD-967`) undertakes her first fully independent solo commission -- a granary roof, "
            "correctly and cleanly read and discharged -- without Kanja's or the second student's "
            "(`MCD-719`) direct proximity, extending generational transmission to three degrees of "
            "separation from Kanja himself. The second student appears in a substantial reflective "
            "role. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1290",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"Four Ears, One Night\" (full narrative text at "
            "docs/lords-of-cian/chronicles/four-ears-one-night.md), Iron Bastard Alias Chronicle "
            "LXXI, wave 24. A detailed, battle-intense full-Trinity showcase scaling the doctrine's "
            "full teaching lineage -- Kanja, the first student (`MCD-499`), the second student "
            "(`MCD-719`), and the third-generation apprentice (`MCD-967`/`1289`) -- into independent "
            "parallel operation, each reading a separate structure across a contested river valley in "
            "one night ahead of a Directorate advance. Kanja's own thread catches a falsified-"
            "signature deception (`MCD-550`) at a munitions depot via doubled verification and "
            "resolves it with the full Trinity; all four sites succeed without misdiagnosis. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1291",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The First Student's Last Field Read\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-first-students-last-field-read.md), Iron Bastard "
            "Alias Chronicle LXXII, wave 24, closing the wave. The first student (`MCD-499`), whose "
            "hands have begun shaking on cold mornings, deliberately chooses to retire from active "
            "field discharge into a full-time teaching role after one final, cleanly executed "
            "footbridge read -- a dignified, chosen aging/mortality register distinct from the "
            "Directorate general's death (`MCD-734`), extending the doctrine's honesty-over-pride "
            "theme into its own originator's late-career choice. No new named characters; the first "
            "student remains unnamed and male per `MCD-499`. Closes the Iron Bastard's twenty-fourth "
            "wave (with `MCD-1289` and `MCD-1290`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1292",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ninth Who Passed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ninth-who-passed.md), Iron Bastard Alias Chronicle "
            "LXXIII, wave 25, first entry. Kanja learns that one of the nine graduates of the "
            "twelve-volunteer cohort (`MCD-1048`) -- trained personally in his own group of four -- "
            "has been using the authentic technique for extortion in a distant settlement, the "
            "doctrine's first genuine 'student turned rogue' register, distinct from resisted "
            "temptation (`MCD-499`), sensory/cognitive toll (`MCD-731`), and fake mercenary "
            "mimicry (`MCD-899`). Kept unnamed, identified only by his place in the cohort. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1293",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Method Turned Against Its Own Lesson\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-method-turned-against-its-own-lesson.md), Iron "
            "Bastard Alias Chronicle LXXIV, wave 25. The doctrine's darkest confrontation entry: "
            "Kanja confronts the rogue former cohort graduate (`MCD-1292`), who admits he understood "
            "the ethical teaching completely and deliberately rejected it for profit; resolved "
            "through restraint and a final honest warning rather than combat -- no discharge of "
            "Obsidian Malice occurs -- distinct from the fatal-misdiagnosis arc (`MCD-497`/`727`/"
            "`728`) since this was a deliberate choice, not a diagnostic error. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1294",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Settlement That Almost Said No\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-settlement-that-almost-said-no.md), Iron Bastard "
            "Alias Chronicle LXXV, wave 25, closing the wave. The settlement that sent the original "
            "cohort of twelve (`MCD-1048`) narrowly votes down a motion to ban the doctrine after "
            "learning of the rogue graduate's extortion (`MCD-1292`/`1293`); a fifth institutional-"
            "pressure vector distinct from political suppression (`MCD-730`), a shelved report "
            "(`MCD-421`), a licensing offer (`MCD-1082`), and curriculum adoption (`MCD-723`), this "
            "one driven by an internal betrayal, left deliberately unresolved rather than cleanly "
            "won. No new named characters. Closes the Iron Bastard's twenty-fifth wave (with "
            "`MCD-1292` and `MCD-1293`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1295",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Morning the Ground Lied to Everyone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-morning-the-ground-lied-to-everyone.md), Iron "
            "Bastard Alias Chronicle LXXVI, wave 26, first entry. The doctrine's first citywide, "
            "no-enemy earthquake-triage application: forty-one compromised structures across a port "
            "district, too many for the standard doubled-verification protocol (`MCD-497`) to assess "
            "individually in time. Kanja deliberately develops a new fast-triage mode -- a single "
            "confident pass sorting structures into stable/failing/uncertain piles, with full doubled "
            "verification reserved only for the uncertain third -- a reasoned departure from standard "
            "pacing driven by time-cost rather than deception or limitation. The second student "
            "(`MCD-719`) appears in supporting capacity. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1296",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"Six Buildings, One Set of Hands\" (full narrative text at "
            "docs/lords-of-cian/chronicles/six-buildings-one-set-of-hands.md), Iron Bastard Alias "
            "Chronicle LXXVII, wave 26. A detailed, battle-intense full-Trinity rescue showcase: an "
            "unpredictable aftershock endangers six structures at once during the earthquake triage "
            "(`MCD-1295`), three with trapped occupants. Obsidian Malice clears targeted debris "
            "rather than structural tension directly, Mafesto's Kinetic Transfer System continuously "
            "grounds ongoing tremor through Kanja's own frame, and a compressed full sequence of "
            "Onyx of Oblivion's named powers (`ARS-020`) saves all six buildings' occupants, though "
            "two of the six structures themselves are condemned. The second student (`MCD-719`) "
            "appears in supporting capacity. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1297",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What They Carved Into the New Threshold\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-they-carved-into-the-new-threshold.md), Iron "
            "Bastard Alias Chronicle LXXVIII, wave 26, closing the wave. Years after the earthquake "
            "rescue (`MCD-1295`/`1296`), the rebuilt rooming house's threshold is deliberately "
            "carved without Kanja's name, commemorating the event with an anonymous line instead -- "
            "a new civic-memorial register extending the doctrine's honesty-over-personal-credit "
            "theme (the free teaching lineage; the declined licensing offer, `MCD-1082`) into the "
            "community's own act of remembrance. No new named characters. Closes the Iron Bastard's "
            "twenty-sixth wave (with `MCD-1295` and `MCD-1296`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1298",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Priest Who Didn't Want to Know\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-priest-who-didnt-want-to-know.md), Iron Bastard "
            "Alias Chronicle LXXIX, wave 27, first entry. The doctrine's first application to a "
            "sacred structure: a temple priest resists Kanja's involvement with a foundation crack "
            "beneath a pillar their congregation's founding account credits to divine attention, "
            "fearing an honest structural answer will cost four hundred people's faith. Kanja argues "
            "the crack will tell its own truth eventually regardless; the priest grants permission "
            "overnight. A genuine new ethical register distinct from every prior institutional-"
            "pressure entry, since the resistance here is doctrinal in the religious sense. Kept "
            "unnamed. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1299",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Held the Pillar Up Was Never a Miracle\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-held-the-pillar-up-was-never-a-miracle.md), Iron "
            "Bastard Alias Chronicle LXXX, wave 27. The diagnostic read reveals the temple pillar "
            "(`MCD-1298`) is sound through extraordinary ancient joinery rather than divine "
            "intervention, and that the actual crack runs through a later, lesser, unrelated repair "
            "now finally failing on its own schedule; Kanja delivers the finding with deliberate care "
            "and explicitly declines to assert or deny the miraculous, keeping the doctrine's stated "
            "epistemic limit (tension only, never meaning -- `MCD-967`) intact. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1300",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Faith That Didn't Need the Lie\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-faith-that-didnt-need-the-lie.md), Iron Bastard "
            "Alias Chronicle LXXXI, wave 27, closing the wave. Days after Kanja's departure, the "
            "priest (`MCD-1298`/`1299`) sends a letter reporting the congregation's faith was "
            "strengthened rather than damaged by the honest finding, and that the repair is being "
            "redone to match the original joinery -- a deliberate constructive counterpoint to the "
            "doctrine's darker honesty-costs-something entries (`MCD-727`/`728`/`1081`), delivered "
            "in a new correspondence format. The second student (`MCD-719`) appears in supporting "
            "capacity. No new named characters. Closes the Iron Bastard's twenty-seventh wave (with "
            "`MCD-1298` and `MCD-1299`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1301",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Bridge Neither Side Trusted Alone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-bridge-neither-side-trusted-alone.md), Iron Bastard "
            "Alias Chronicle LXXXII, wave 28, first entry. The Directorate successor (`MCD-734`) "
            "requests the doctrine's first formal cross-faction joint engineering operation: a "
            "neutral structural assessment of a failing aqueduct spanning contested border "
            "territory, which neither the Trust nor the rebels trust the other's engineers to read "
            "honestly. Kanja agrees on condition both sides receive the identical account "
            "simultaneously, extending the general/successor thread from adversary through respect "
            "into active cooperation. No new named characters; the successor remains unnamed per "
            "`MCD-734`."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1302",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"One Read, Two Flags\" (full narrative text at "
            "docs/lords-of-cian/chronicles/one-read-two-flags.md), Iron Bastard Alias Chronicle "
            "LXXXIII, wave 28. A detailed technical-and-political showcase: the aqueduct (`MCD-1301`) "
            "is found failing not from sabotage but from two independent, uncoordinated repair "
            "efforts by each faction working against each other's tension across years of contested "
            "control; both sides' engineers complete an eleven-day joint repair under Kanja's live "
            "diagnostic coordination, with a single restrained Obsidian Malice discharge clearing a "
            "failed section. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1303",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Successor Called Progress\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-successor-called-progress.md), Iron Bastard "
            "Alias Chronicle LXXXIV, wave 28, closing the wave. Weeks after the aqueduct repair "
            "(`MCD-1301`/`1302`), the Directorate successor reflects with Kanja on the completed "
            "project as a deliberately modest 'proof of concept' rather than a resolved peace, "
            "extending the general/successor institutional arc (`MCD-454`/`734`) to its furthest "
            "point yet -- active, ongoing collaboration. No new named characters. Closes the Iron "
            "Bastard's twenty-eighth wave (with `MCD-1301` and `MCD-1302`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1304",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Dol Maren Wouldn't Sail Without\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-dol-maren-wouldnt-sail-without.md), Iron Bastard "
            "Alias Chronicle LXXXV, wave 29, first entry. Already-locked crew member Dol Maren "
            "(`CC-120`) personally asks Kanja to verify a four-week keel repair before a dangerous "
            "voyage despite trusting his own joinery, extending his established calculation-over-"
            "faith characterization into a personal, non-operational doctrine application paralleling "
            "Efa Gol's keepsake reading (`MCD-1049`) with a distinct register -- verification sought "
            "as a standard, not out of grief. No new named characters; no vessel is newly named."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1305",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Read That Never Stopped\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-read-that-never-stopped.md), Iron Bastard Alias "
            "Chronicle LXXXVI, wave 29. The doctrine's first sustained, continuous live-monitoring "
            "application: a storm strains the repaired keel (`MCD-1304`) past a single static "
            "reading's usefulness, forcing Kanja to hold an unbroken read open for hours, reporting "
            "a continuously shifting tension figure that lets Dol Maren order a bow-on course "
            "correction in time -- a new mechanic distinct from the rate-of-change projection used "
            "against the granary fire (`MCD-1080`), since no discharge ever occurs here. Dol Maren "
            "(`CC-120`) appears in a substantial role, he/him throughout. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1306",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Hull Held For Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-hull-held-for-him.md), Iron Bastard Alias "
            "Chronicle LXXXVII, wave 29, closing the wave. Safe landfall after the storm (`MCD-1305`); "
            "Dol Maren (`CC-120`) confirms the calculation and the doctrine agreed throughout, "
            "calling the continuous-monitoring read a verified instrument rather than an act of "
            "faith, and Garren Hask (`CC-115`) logs the voyage with a rare uncharacteristic personal "
            "note on Dol Maren having asked at all. No new named characters. Closes the Iron "
            "Bastard's twenty-ninth wave (with `MCD-1304` and `MCD-1305`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1307",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Name They Gave What He Never Named\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-name-they-gave-what-he-never-named.md), Iron Bastard "
            "Alias Chronicle LXXXVIII, wave 30, first entry. The independent academy that published "
            "the Trust scholar's once-shelved research (`MCD-421`/`551`) formally charters the "
            "doctrine as an academic discipline under the collision-checked new field name 'Tension "
            "Reading,' with the scholar as founding chair; Kanja accepts the name but declines an "
            "offered honorary council seat, extending the free-teaching principle (`MCD-499`/`719`/"
            "`967`/`1048`) and the declined licensing offer (`MCD-1082`) into refusing symbolic "
            "honor as well as money. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1308",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The First Design Neither Verification Caught\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-first-design-neither-verification-caught.md), Iron "
            "Bastard Alias Chronicle LXXXIX, wave 30. A genuine, deliberately unresolved new limit: "
            "a Crawler design passes doubled verification (`MCD-497`), the standing-alone check "
            "(`MCD-1081`), and falsified-signature detection (`MCD-550`) -- the tension is true, the "
            "target is alone, the signature is unfalsified -- yet the discharge still fails to "
            "transfer its disabling effect. Kanja deliberately declines to force an explanation and "
            "withdraws, leaving the mechanism unexplained as an open hook for a future wave. The "
            "second student (`MCD-719`) appears in supporting capacity. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1309",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"Everyone Who Ever Learned to Listen\" (full narrative text at "
            "docs/lords-of-cian/chronicles/everyone-who-ever-learned-to-listen.md), Iron Bastard "
            "Alias Chronicle XC, wave 30, closing the wave. A capstone reunion assembled by Garren "
            "Hask (`CC-115`) gathering the doctrine's full teaching lineage and recurring figures in "
            "one scene for the first time -- the first student (`MCD-499`), second student "
            "(`MCD-719`), third-generation apprentice (`MCD-967`/`1289`), Trust scholar (`MCD-421`/"
            "`551`/`1307`), Dol Maren (`CC-120`), and the Trust diagnostician (`MCD-1286`-`1288`) -- "
            "mirroring the earlier capstone at `MCD-740` at a larger scale. The unresolved "
            "countermeasure from `MCD-1308` is explicitly named and left open as a forward hook "
            "rather than resolved. No new named characters. Closes the Iron Bastard's thirtieth wave "
            "(with `MCD-1307` and `MCD-1308`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 27, f"expected 27 new rules, got {len(NEW_RULES)}"

    for r in NEW_RULES:
        assert r["category"] == "kanja-alias-chronicle", f"bad category on {r['id']}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 261,
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
