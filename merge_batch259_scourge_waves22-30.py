#!/usr/bin/env python3
"""Batch 259: The Scourge Alias Chronicle waves 22-30 (27 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Scourge's twenty-second through thirtieth Alias Chronicle waves (9 waves, 27 entries), "
    "drafted under Abad's blanket authorization to continue all eleven aliases' waves 22-30 "
    "uninterrupted. Pushed into genuinely new registers across this alias's deepest timeline: a "
    "Trust admiralty tribunal's century-spanning attempt (and eventual toothless ruling) to legally "
    "classify the Scourge; a legitimate reform movement's friction with the alias's vigilante "
    "methods; a public-health quarantine and a Blight-contaminated cave dramatizing the Breath "
    "Collar's filtration function; deep-gear showcases for the Ironfall Boots' retractable heel "
    "blade, the Smoke System's Signal mode, and the Sovereign Eyes' V4 fully-dark stealth mode; new "
    "environments (a volcanic glass reef, a high mountain pass, a monsoon river delta); genuine "
    "failure states (a compromised rendezvous route, a fever outrunning rescue, a near-temptation to "
    "break the Onyx seal); humanitarian/logistics entries with no combat at all; and direct payoffs "
    "to prior open hooks -- the boy once cut free, the traced sibling, the cabin boy grown old, Efa "
    "Gol's late-life 'does he regret it' question, and Efa Gol's successor maturing into her own "
    "independent doctrine -- closing on the year before the already-locked end of the 284-year Long "
    "Mask (MCD-1022, age 314). Zero new named characters were introduced across all 27 entries; "
    "every entry reused already-locked crew (Efa Gol, Garren Hask, Pell Ostra, Sena, and Efa Gol's "
    "established unnamed successor). Abad's approval: \"lets do this 22nd Alias Chronicle wave for "
    "any/all of the eleven aliases to the 30th wave and you are to continue uninterrupted until "
    "completion this includes rigorous testing, commit, push to main origin.\""
)

NEW_RULES = [
    {
        "id": "MCD-1229",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Tribunal That Tried to Name Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-tribunal-that-tried-to-name-him.md), The Scourge "
            "Alias Chronicle LXIV, wave 22, first entry. Age 98, V3 gear. A Sovereign Trust "
            "admiralty tribunal convenes to formally classify the Scourge's legal status -- "
            "stateless pirate versus unrecognized belligerent -- and deadlocks across three "
            "irreconcilable written opinions, agreeing only that no ruling can be enforced against a "
            "party the court cannot locate or compel. Garren Hask's already-locked sealed testimony "
            "(MCD-1018) is re-entered as the only documentary record both sides accept as genuine. "
            "Institutional/legal-friction register extending MCD-1017/1018/1041's jurisdictional "
            "theme. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1230",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Camp Fed by No One's Orders\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-camp-fed-by-no-ones-orders.md), The Scourge Alias "
            "Chronicle LXV, wave 22. Age 176, V3 gear. A port refuses entry to sixty-three freed "
            "captives over a genuine, non-malicious fever fear; the crew builds an improvised "
            "quarantine camp outside the harbor's jurisdiction rather than fight the refusal, using "
            "the Breath Collar's filtration function (ARS-351) in sustained field use for six days "
            "until the fever passes with no further deaths. The sub-series' first genuine public-"
            "health/quarantine crisis, resolved through logistics and patience rather than combat or "
            "leverage. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1231",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Ledger Said About the Boy He Cut Free\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-ledger-said-about-the-boy-he-cut-free.md), The "
            "Scourge Alias Chronicle LXVI, wave 22, closing the wave. Age 160, V3 gear. Direct "
            "payoff to \"The Boy He Once Cut Free\" (MCD-905, age 122), thirty-eight years later: "
            "Garren Hask's ledger entry for the freed-captive-turned-trafficker remains unresolved -- "
            "'held for account,' neither reform nor relapse ever reported -- and stays honestly open "
            "rather than fabricated closed, extending Hask's established honesty-over-tidiness "
            "principle. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1232",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Glass Reef\" (full narrative text at docs/lords-of-cian/chronicles/the-glass-reef.md), "
            "The Scourge Alias Chronicle LXVII, wave 23, first entry. Age 250, V4 gear. The "
            "sub-series' first volcanic-obsidian-reef environment: the Sovereign Eyes' V4 Blueprint "
            "Eye structural overlay (ARS-350) reads the reef's true geometry to thread a channel no "
            "chart had mapped correctly, freeing ninety-one captives with the navigational help of an "
            "unnamed local diver whose lived knowledge complements the gear rather than being "
            "superseded by it. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1233",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Rival Who Called Him a Setback\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-rival-who-called-him-a-setback.md), The Scourge Alias "
            "Chronicle LXVIII, wave 23. Age 190, V3 gear. Three unnamed legal-reform advocates "
            "confront him, arguing his raids undermine years of slow legislative progress against "
            "debt-bondage transfer by handing opponents propaganda; he voluntarily narrows his own "
            "operational targets to flatly illegal operations rather than the legally ambiguous ones "
            "the bill targets, leaving both sides' fundamental disagreement over method honestly "
            "unresolved. The sub-series' first friction with a legitimate, non-hostile reform "
            "movement. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1234",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Sibling She Waited Thirty Years For\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-sibling-she-waited-thirty-years-for.md), The Scourge "
            "Alias Chronicle LXIX, wave 23, closing the wave. Age 150, V3 gear. Direct payoff to "
            "\"The Family He Helped Her Find\" (MCD-1020, age 115), thirty-five years later: Garren "
            "Hask's ledger network finally locates the traced sibling, and the reunion happens on the "
            "page but arrives complicated and imperfect rather than clean -- recognition slowed by "
            "decades, real effort on both sides with no guarantee it holds. Hask logs it as 'found, "
            "and known, imperfectly.' No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1235",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Half-Second the Blade Bought\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-half-second-the-blade-bought.md), The Scourge Alias "
            "Chronicle LXX, wave 24, first entry. Age 238, V3 gear. The first detailed, in-action "
            "dramatization of the Ironfall Boots' retractable heel blade (ARS-353, established "
            "deployed eleven times across 284 years, saving his life or freedom in nine): falling "
            "through a hidden pit trap mid-rescue, the blade's trigger catches into the pit wall and "
            "arrests the fall, established here as the tenth deployment and one of the nine "
            "life/freedom-saving uses, consistent with the existing count. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1236",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Collar Filtered Out\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-collar-filtered-out.md), The Scourge Alias "
            "Chronicle LXXI, wave 24. Age 145, V3 gear. The sub-series' first cave/underground-tunnel "
            "environment: a slaving depot's expanded cave system has an unintended Blight-seam leak "
            "thickening the air; the Breath Collar's filtration membrane (ARS-351) keeps every breath "
            "clean across a three-hour rescue of sixty-eight captives while affected, unfiltered "
            "guards prove too sick to properly resist. Paired within the same wave as MCD-1230's "
            "quarantine use of the same component to show its range. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1237",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Smoke That Spoke First\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-smoke-that-spoke-first.md), The Scourge Alias "
            "Chronicle LXXII, wave 24, closing the wave. Age 225, V3 gear. The first detailed "
            "dramatization of the Smoke System's Signal mode (ARS-354) used by a non-crew party: an "
            "unnamed coastal watch-captain fires a Signal-mode canister salvaged from a raid eleven "
            "years earlier, and the crew's signal code -- spread organically into allied folklore -- "
            "summons help against a raiding party testing the town's protected reputation. No new "
            "named characters. Closes the Scourge's twenty-fourth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1238",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Recapture at Dusk\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-recapture-at-dusk.md), The Scourge Alias Chronicle "
            "LXXIII, wave 25, first entry. Age 172, V3 gear. A genuine tactical failure distinct from "
            "every prior one: a previously reliable overland rendezvous route, used successfully "
            "eleven times, proves compromised not by treachery but by an entirely unrelated second "
            "slaving operation independently watching the same ground, recapturing forty-three freed "
            "captives hours after their first rescue; a second, harder rescue is required, and the "
            "route is permanently retired. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1239",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Pass Where the Air Ran Thin\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-pass-where-the-air-ran-thin.md), The Scourge Alias "
            "Chronicle LXXIV, wave 25. Age 262, V4 gear. The sub-series' first high-altitude mountain "
            "environment, a genuinely land-locked smuggling route two days above the nearest "
            "navigable river that the sea-legend reputation had never reached; extends the Ironhand "
            "Gauntlets' V4 blood-heated grip (ARS-352, age 260+) to cold-stone/altitude climbing "
            "beyond its established cold-water use, and dramatizes deliberate restraint in the "
            "Ironfall Boots' impact-sole tremor near a lethal drop. Thirty-one freed. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1240",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Successor's First Command Alone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-successors-first-command-alone.md), The Scourge Alias "
            "Chronicle LXXV, wave 25, closing the wave. Age 270, V4 gear. Direct escalation from "
            "\"The Raid He Watched From the Rigging\" (MCD-904, age 265): five years later, Efa "
            "Gol's established unnamed successor runs an entire fifty-two-captive liberation a "
            "hundred miles from Kanja, who is physically absent and unreachable during the operation "
            "rather than staying aboard as an unused failsafe -- the fullest institutional-trust "
            "payoff of the successor thread to date. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1241",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"Sena's Own Student\" (full narrative text at docs/lords-of-cian/chronicles/senas-own-student.md), "
            "The Scourge Alias Chronicle LXXVI, wave 26, first entry. Age 235, V3 gear. Direct "
            "generational-transmission payoff to \"The Blade She Almost Didn't Sheathe\" (MCD-1043, "
            "age 190): forty-five years later, Sena (established minor crew member) talks down a "
            "newer, younger crew member's near-lethal impulse against an already-surrendered guard "
            "using the same words and doctrine Kanja once used on her, with Kanja present but not "
            "needing to intervene. No new named characters beyond the already-established Sena."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1242",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Was Left to Give\" (full narrative text at docs/lords-of-cian/chronicles/what-was-left-to-give.md), "
            "The Scourge Alias Chronicle LXXVII, wave 26. Age 130, V3 gear. The sub-series' first "
            "post-liberation famine-relief entry: fifty-two captives are freed from a drought-"
            "exploiting grain-hoarding operation into an inland settlement with almost nothing left "
            "to receive them; the crew spends three days redirecting the operation's own hoarded "
            "grain stores rather than fighting, a deliberate contrast to MCD-814's already-achieved "
            "self-sufficiency by showing the unglamorous groundwork it depends on. No gear or Trinity "
            "capability solves the actual problem. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1243",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Pocket He Almost Opened\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-pocket-he-almost-opened.md), The Scourge Alias "
            "Chronicle LXXVIII, wave 26, closing the wave. Age 300, V4 gear. The sub-series' first "
            "entry to directly engage the Forge-Coat's mysterious forty-second 'Captain's pocket' "
            "compartment (ARS-349) without resolving or revealing its contents: after a raid costs "
            "three crew lives and nearly a fourth (an elderly but still-present Garren Hask), Kanja's "
            "hand rests on the pocket's seam without opening it; Hask asks only whether he needs it "
            "tonight, not what it holds, and the mystery stays deliberately intact. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1244",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Duel He Didn't Need Onyx For\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-duel-he-didnt-need-onyx-for.md), The Scourge Alias "
            "Chronicle LXXIX, wave 27, first entry. Age 215, V3 gear. A near-miss discipline entry "
            "distinct from MCD-810's gear failure: a bodyguard trained specifically to counter Onyx "
            "of Oblivion's known techniques nearly wins an extended forty-minute duel, and the "
            "temptation to unseal Onyx arises purely internally under pressure; the seal holds by "
            "choice, and plain Rexmar Machete swordsmanship and endurance -- the same craft "
            "underlying the whole legend -- wins instead. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1245",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The River That Remembered the Rain\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-river-that-remembered-the-rain.md), The Scourge Alias "
            "Chronicle LXXX, wave 27. Age 95, V3 gear. The sub-series' first river-delta/monsoon-"
            "flood environment: a low-ground holding compound floods rapidly during a rare monsoon "
            "season after its guards flee, and the rescue becomes a race against rising water rather "
            "than a fight, freeing nineteen captives before the flood erases the site entirely by "
            "morning. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1246",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Efa Gol Never Asked Twice\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-efa-gol-never-asked-twice.md), The Scourge Alias "
            "Chronicle LXXXI, wave 27, closing the wave. Age 290, V4 gear. Direct continuation, not "
            "resolution, of the deliberately unresolved 'does he regret it' question first raised in "
            "\"The Question Efa Gol Finally Asked\" (MCD-830, age 180): over a hundred years later, "
            "Kanja gives a fuller but still genuinely ambiguous answer -- he cannot weigh what the "
            "persona has cost against what it has bought, and has stopped trying to. Extends Efa "
            "Gol's established post-retirement continuity (MCD-807, stepped back age 150). No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1247",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Forge That Bought Its Own Freedom\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-forge-that-bought-its-own-freedom.md), The Scourge "
            "Alias Chronicle LXXXII, wave 28, first entry. Age 180, V3 gear. Extends \"The Merchant "
            "Who Changed His Trade\" (MCD-824) into a new proactive register: an unnamed forge-town "
            "owner, acting on secondhand, unconfirmed reputation alone rather than any direct visit "
            "or pressure, spends two years voluntarily converting his slave-trade-linked ore "
            "operation before the crew ever arrives, discovered only by coincidence on an unrelated "
            "supply run. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1248",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fever That Outran the Rescue\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fever-that-outran-the-rescue.md), The Scourge Alias "
            "Chronicle LXXXIII, wave 28. Age 205, V3 gear. A genuine, unprevented-loss failure state: "
            "the fastest clean liberation the crew has run in years still arrives four days too late "
            "for six of seventy-four captives already fatally weakened by a shipboard fever with a "
            "two-week head start no reconnaissance could have closed; the Mend-Line (ARS-355) is "
            "explicitly and correctly unable to help, extending its established scope to exclude "
            "illness alongside pain, organ repair, and concussive injury. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1249",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Watch That Never Saw Him Coming\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-watch-that-never-saw-him-coming.md), The Scourge "
            "Alias Chronicle LXXXIV, wave 28, closing the wave. Age 260, V4 gear. The sub-series' "
            "first pure-stealth entry with zero combat and zero reputation invoked, dramatizing the "
            "Sovereign Eyes' V4 'fully dark stealth' mode (ARS-350) directly for the first time: a "
            "competent six-guard watch rotation never registers a three-hour infiltration that frees "
            "forty-one captives one at a time, leaving the garrison unaware any breach occurred. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1250",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ruling That Changed Nothing\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ruling-that-changed-nothing.md), The Scourge Alias "
            "Chronicle LXXXV, wave 29, first entry. Age 200, V3 gear. Direct, deliberately "
            "anticlimactic payoff to \"The Tribunal That Tried to Name Him\" (MCD-1229, age 98): over "
            "a century later, a new set of justices finally issues a ruling classifying the Scourge "
            "as an 'unaffiliated maritime irregular of indeterminate jurisdiction, subject to "
            "regional discretion' -- a sentence with no enforcement mechanism that changes nothing "
            "operationally, proving the earlier tribunal's deadlock right rather than resolving it. "
            "No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1251",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Boy Who Grew Old Waiting\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-boy-who-grew-old-waiting.md), The Scourge Alias "
            "Chronicle LXXXVI, wave 29. Age 292, V4 gear. Direct generational-loop payoff to \"The "
            "Boy Who Didn't Know His Name\" (MCD-448, age 210): eighty-two years later, the cabin boy "
            "is now an old man telling his own further-drifted version of the legend to his "
            "grandchildren; Kanja listens unremarked and again deliberately withholds his identity, "
            "and the old man dies years later still never knowing he told the story twice to the man "
            "who lived it. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1252",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Last Names Before the Silence\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-last-names-before-the-silence.md), The Scourge Alias "
            "Chronicle LXXXVII, wave 29, closing the wave. Age 308, V4 gear. An elegiac, deliberately "
            "quiet entry building toward the Long Mask's established close (MCD-1022, age 314) "
            "without depicting it: an elderly, no-longer-field-active Garren Hask and Kanja review "
            "the ledger's most recent decades together; Hask declines Kanja's suggestion to let "
            "someone else carry it, not yet finished with it. Pell Ostra (CC-132/133) reused in a "
            "small continuity beat (a ground reading lens). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1253",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Last Depot on the Old Charts\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-last-depot-on-the-old-charts.md), The Scourge Alias "
            "Chronicle LXXXVIII, wave 30, first entry. Age 310, V4 gear. Closes a decades-long "
            "background thread implicit in Garren Hask's ledger-keeper role: his original set of "
            "charted slaving routes from the alias's earliest years has its final uncrossed mark "
            "struck through as the last depot on those charts falls, eighty-nine freed; Hask retires "
            "the charts as history rather than working documents. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1254",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Successor Chose to Keep\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-successor-chose-to-keep.md), The Scourge Alias "
            "Chronicle LXXXIX, wave 30. Age 312, V4 gear. A direct maturation of the successor thread "
            "(MCD-904, MCD-1240): over forty years into her own independent command tenure, Efa "
            "Gol's established unnamed successor deliberately departs from both Kanja's and Efa "
            "Gol's own established decoy methods, building a three-diversion approach neither "
            "predecessor would have used and succeeding because it doesn't match what the reputation "
            "trained enemies to expect -- the institution evolving past its founders before the "
            "persona's own end. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1255",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Coat He Almost Didn't Put Back On\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-coat-he-almost-didnt-put-back-on.md), The Scourge "
            "Alias Chronicle XC, wave 30, closing the wave. Age 313, V4 gear, one year before the "
            "Long Mask's already-locked close (MCD-1022, age 314). After a costly mission, Kanja "
            "seriously considers ending the persona a year early; Efa Gol, Garren Hask, and Efa Gol's "
            "established unnamed successor each arrive in turn, and a scouted, time-limited rescue "
            "window persuades him to put the coat back on for one more year rather than end it that "
            "night -- setting up rather than restaging or contradicting MCD-1022's own final mission. "
            "No new named characters. Closes the Scourge's thirtieth wave and, for this run, the "
            "alias's Chronicle output at ninety total entries across thirty complete waves."
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
            "batch": 259,
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
