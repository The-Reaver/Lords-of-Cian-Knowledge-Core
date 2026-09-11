#!/usr/bin/env python3
"""Batch 263: Storm That Walks Alias Chronicle waves 22-30 (27 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Storm That Walks' twenty-second through thirtieth Alias Chronicle waves (9 waves, 27 "
    "entries), drafted under Abad's blanket authorization to continue all eleven aliases' waves "
    "22-30 uninterrupted. These nine waves push into genuinely new registers for this alias: the "
    "storm-interval verification regulation's own equity gap and its small-craft amendment "
    "(waves 22), the doctrine's first cold/ice-environment application and a wholly separate "
    "ice-reading tradition credited to an unnamed northern pilot (wave 23), the opening of a "
    "fourth generation of Sephtis's craft with its sensory technique detailed on the page for "
    "the first time (wave 24), the sub-series' largest false positive and a purely institutional "
    "hearing-room confrontation with no combat (wave 25), the rival fleet's own succession "
    "crisis resolved through the first deliberate cross-tradition apprenticeship (wave 26), the "
    "doctrine's first full-city evacuation at Ghost Harbor (wave 27), the retired successor's "
    "decline and death mirroring Sephtis's own arc (wave 28), a deeper-mechanics entry "
    "establishing the clean limits of Kanja's own Rex/Mar senses against the human doctrine and "
    "a three-tradition collaborative reading (wave 29), and a closing wave showing the school's "
    "fully self-organizing institution running an entire storm season with Kanja absent "
    "entirely for the first time in the sub-series' history (wave 30). No new named characters "
    "were introduced across any of the 27 entries -- every entry reused already-locked figures "
    "(Sephtis's lineage: the retired successor, the third-generation senior student, the new "
    "fourth-generation apprentice; the rival fleet's forecaster and its cross-trained dual-"
    "tradition sailor; Kanja; Efa Gol) or left one-off officials and civilians deliberately "
    "unnamed, matching this alias's own established convention. Abad's approval: \"lets do this "
    "22nd Alias Chronicle wave for any/all of the eleven aliases to the 30th wave and you are to "
    "continue uninterrupted until completion this includes rigorous testing, commit, push to "
    "main origin.\""
)

NEW_RULES = [
    {
        "id": "MCD-1337",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Law Didn't Reach\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-law-didnt-reach.md), Storm That Walks Alias "
            "Chronicle LXIV, wave 22, first entry in the wave. The third-generation student "
            "discovers the storm-interval verification regulation (MCD-1088) quietly excludes "
            "small independent fishers outside the fifty-league certified-station radius, and "
            "closes the gap by hand, reading weather in person for uncovered harbors before any "
            "formal fix exists. The first genuine equity-of-access test of the doctrine's written "
            "law. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1338",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Silence With No Wind In It\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-silence-with-no-wind-in-it.md), Storm That Walks "
            "Alias Chronicle LXV, wave 22. A detailed full-Trinity combat showcase in total "
            "windless fog, the one condition the storm-timing doctrine has no signal to read; the "
            "smuggling faction from MCD-1053 exploits the doctrine's silence, and Kanja's own "
            "non-doctrine senses (hearing, close-range awareness) carry the fight instead, "
            "keeping the doctrine's real limit honest rather than quietly covered. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1339",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Version of the Law They Wrote for Small Boats\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-version-of-the-law-they-wrote-for-small-boats.md), "
            "Storm That Walks Alias Chronicle LXVI, wave 22, closing the wave. The storm-interval "
            "verification regulation (MCD-1088) is formally amended with a four-paragraph small-"
            "craft addendum allowing standing seasonal readings for vessels outside the certified "
            "radius, resolving MCD-1337's equity gap. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1340",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ice That Doesn't Warn Like Water\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ice-that-doesnt-warn-like-water.md), Storm That "
            "Walks Alias Chronicle LXVII, wave 23, first entry in the wave. The third-generation "
            "student's storm-timing method fails to map onto northern pack-ice formation, a "
            "genuinely different phenomenon; an unnamed northern harbor pilot's own separate "
            "ice-reading tradition (water color, settling sound, gull behavior) is introduced as "
            "the operative doctrine for cold water. The sub-series' first entry where the "
            "student's trained method genuinely doesn't apply. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1341",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Break in the Floe\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-break-in-the-floe.md), Storm That Walks Alias "
            "Chronicle LXVIII, wave 23. A detailed full-Trinity rescue-and-combat showcase freeing "
            "three ships trapped by closing pack ice, using the northern pilot's ice-reading "
            "method (MCD-1340) rather than storm-timing doctrine to time the intervention; the "
            "student credits the rescue in the ledger under the pilot's own name rather than the "
            "school's tradition. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1342",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Cold Taught the Ledger\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-cold-taught-the-ledger.md), Storm That Walks "
            "Alias Chronicle LXIX, wave 23, closing the wave. The northern pilot's ice-reading "
            "method is formally added to the school's training as its own credited chapter, "
            "distinct from Sephtis's storm-timing tradition rather than absorbed into it -- the "
            "first addition to the curriculum credited to someone outside Sephtis's direct "
            "lineage. Plants a light hook: two unnamed students showing aptitude for the pilot's "
            "craft. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1343",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The One the Third Student Chose to Teach\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-one-the-third-student-chose-to-teach.md), Storm "
            "That Walks Alias Chronicle LXX, wave 24, first entry in the wave. The senior third-"
            "generation student (MCD-983/1054/1055/1086) selects and begins training her own "
            "apprentice, opening the fourth generation of Sephtis's craft; she deliberately "
            "front-loads the craft's emotional cost by making Sephtis's own oldest logged miss "
            "the apprentice's first lesson, rather than technical instruction. No new named "
            "characters -- the apprentice is left unnamed, matching this alias's established "
            "convention."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1344",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fourth Reading, Unwitnessed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fourth-reading-unwitnessed.md), Storm That Walks "
            "Alias Chronicle LXXI, wave 24. The fourth-generation apprentice's first supervised, "
            "low-stakes reading, detailing the doctrine's actual sensory technique on the page in "
            "full for the first time: barometric feel cross-checked against bodily memory, "
            "horizon water-color shift, gull-circling tightness (borrowed from the northern "
            "pilot's tradition), and the non-sensory skill of naming uncertainty aloud. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1345",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Four Generations Now Agree On\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-four-generations-now-agree-on.md), Storm That "
            "Walks Alias Chronicle LXXII, wave 24, closing the wave. The retired successor, the "
            "senior third-generation student, and the new fourth-generation apprentice formally "
            "write the doctrine's five core principles as an explicit written creed for the first "
            "time, the fifth line directly quoting Kanja's own reflection from MCD-1088. Brings "
            "all three living generations into direct collaborative dialogue for the first time. "
            "No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1346",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Storm That Never Came\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-storm-that-never-came.md), Storm That Walks Alias "
            "Chronicle LXXIII, wave 25, first entry in the wave. The senior third-generation "
            "student calls a major storm on full, independently cross-checked signal, moving "
            "three fleets at real cost; the storm dissipates against an unmodeled cold-current "
            "interaction, the sub-series' largest and most expensive false positive. Logged "
            "honestly in the ledger, identifying the cold-current gap as a real, now-flagged "
            "model limitation. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1347",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Reckoning at the Dock\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-reckoning-at-the-dock.md), Storm That Walks Alias "
            "Chronicle LXXIV, wave 25. A purely institutional hearing-room confrontation with no "
            "combat: a hostile Trust administrator uses MCD-1346's costly false positive to move "
            "against the school's regulatory standing; the retired successor's defense hinges on "
            "the ledger's transparent-misses tradition, which no rival record on the coast "
            "matches, and the hall requires the same standard from any challenger rather than "
            "stripping the school's authority. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1348",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Miss Bought Back\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-miss-bought-back.md), Storm That Walks Alias "
            "Chronicle LXXV, wave 25, closing the wave. Months after the costly false positive, "
            "the transparent handling of the miss draws new harbors to request standing readings "
            "specifically because of it, and the affected merchant returns having decided the "
            "school's honestly-logged failures make its record more trustworthy, not less. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1349",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Peer Who Had No One Left to Teach\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-peer-who-had-no-one-left-to-teach.md), Storm That "
            "Walks Alias Chronicle LXXVI, wave 26, first entry in the wave. The rival fleet's own "
            "generations-old weather tradition (MCD-985) faces its own succession crisis -- its "
            "aging forecaster has trained no successor in fifteen years; the third-generation "
            "student, drawing on the school's own succession history, suggests looking outside "
            "the rival fleet's own command for a candidate. No new named characters -- the rival "
            "forecaster remains unnamed, consistent with MCD-985."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1350",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fleet That Went Blind Together\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fleet-that-went-blind-together.md), Storm That "
            "Walks Alias Chronicle LXXVII, wave 26. A detailed full-Trinity combat showcase: with "
            "the rival forecaster incapacitated by illness during a genuine weather emergency, "
            "raiders exploit both fleets' shared vulnerability; the student reads weather for "
            "both fleets under one shared call, and the Trinity defends both together for the "
            "first time in active joint combat rather than one fleet protecting the other's "
            "agreement from outside (MCD-1087). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1351",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Student Who Crossed the Line Between Traditions\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-student-who-crossed-the-line-between-traditions."
            "md), Storm That Walks Alias Chronicle LXXVIII, wave 26, closing the wave. The rival "
            "forecaster, having seen her tradition's vulnerability exposed, asks the school to "
            "cross-train a promising sailor from her own fleet alongside her own instruction -- "
            "the first deliberate blending of the two weather traditions into a single dual-"
            "tradition apprenticeship. No new named characters requiring collision-check -- the "
            "rival sailor is described by role, not personally named, matching this lineage's "
            "established convention."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1352",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The City That Had Three Days\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-city-that-had-three-days.md), Storm That Walks "
            "Alias Chronicle LXXIX, wave 27, first entry in the wave. A supermassive storm "
            "threatens Ghost Harbor (formerly Ash Harbor, MCD-241, placed on the Atlas at "
            "GEO-006); the student brings the full transparent ledger to the harbor's magistrate, "
            "who orders a full evacuation on a three-day window -- the doctrine's first "
            "application at whole-city civilian-evacuation scale. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1353",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Held the Causeway\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-held-the-causeway.md), Storm That Walks Alias "
            "Chronicle LXXX, wave 27. A detailed full-Trinity showcase defending Ghost Harbor's "
            "main evacuation causeway from storm-surge collapse while it is still crowded with "
            "fleeing civilians, timed against the student's own surge reading; the causeway is "
            "held exactly long enough to clear every crossing before it collapses, with zero "
            "casualties. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1354",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Ghost Harbor Remembered This Time\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-ghost-harbor-remembered-this-time.md), Storm That "
            "Walks Alias Chronicle LXXXI, wave 27, closing the wave. Ghost Harbor's full "
            "evacuation succeeds with zero casualties; the fourth-generation apprentice (MCD-"
            "1343) takes a real field role for the first time, running confirmed-clear reports "
            "during the crisis, paying off his low-stakes debut at MCD-1344. The city formally "
            "and anonymously thanks 'the reading and the readers,' extending the doctrine's "
            "institutional-anonymity theme to civic scale. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1355",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Last Reading She Insisted On\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-last-reading-she-insisted-on.md), Storm That Walks "
            "Alias Chronicle LXXXII, wave 28, first entry in the wave. The retired successor, now "
            "elderly with the cold permanently settled in her hands, insists on making one final "
            "call herself, start to finish, refusing dictation -- a deliberate structural parallel "
            "to Sephtis's own late-life entry (MCD-981), distinct in cause (age, not fever) and "
            "in her refusal of the generosity he received. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1356",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Sky the Day They Buried Her\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-sky-the-day-they-buried-her.md), Storm That Walks "
            "Alias Chronicle LXXXIII, wave 28. The retired successor dies peacefully of natural "
            "causes; the senior third-generation student makes the sea-burial-rite reading "
            "herself, this time without the uncertainty of her first time doing so for Sephtis "
            "(MCD-982), understanding the weight as familiar rather than easier. Deliberately "
            "echoes MCD-982's title format. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1357",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Name They Gave the Second Method\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-name-they-gave-the-second-method.md), Storm That "
            "Walks Alias Chronicle LXXXIV, wave 28, closing the wave. Sailors informally name a "
            "reading-verification practice 'the second reader's watch,' tracing to the "
            "disagreement-resolution protocol the successor helped establish at MCD-979 -- a "
            "legacy entry deliberately distinct from MCD-983's strait named for Sephtis, since "
            "the successor, never given a proper name across her entire arc, receives a named "
            "practice rather than a place. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1358",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What His Own Senses Couldn't Tell Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-his-own-senses-couldnt-tell-him.md), Storm That "
            "Walks Alias Chronicle LXXXV, wave 29, first entry in the wave. Kanja's own Rex/Mar "
            "density-tuned senses register a distant Titan-class vessel's mass as an approaching "
            "storm, a false read caused by his senses reading mass generally rather than weather "
            "specifically; the fourth-generation apprentice identifies the cause. The sub-series' "
            "first entry establishing the clean limits of Kanja's own gift against the human "
            "doctrine. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1359",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Reading That Took Four Hands\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-reading-that-took-four-hands.md), Storm That Walks "
            "Alias Chronicle LXXXVI, wave 29. Two intersecting storm systems, including a "
            "recurrence of MCD-1346's unmodeled cold-current interaction, require the senior "
            "student, the fourth-generation apprentice, and the rival fleet's dual-tradition "
            "sailor to collaborate across three separate traditions on a single reading for the "
            "first time, converging on a safe window none of the three traditions could have "
            "found alone. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1360",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Method With No Name Left to Give It\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-method-with-no-name-left-to-give-it.md), Storm "
            "That Walks Alias Chronicle LXXXVII, wave 29, closing the wave. With Sephtis's storm-"
            "timing tradition, the rival fleet's independent method, and the northern pilot's ice-"
            "reading now blended into MCD-1359's successful convergence, the school formally "
            "acknowledges the doctrine can no longer be credited to any single tradition -- the "
            "sub-series' most explicit institutional-anonymity synthesis to date. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1361",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Council That Meets Without Being Summoned\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-council-that-meets-without-being-summoned.md), "
            "Storm That Walks Alias Chronicle LXXXVIII, wave 30, first entry in the wave. Kanja "
            "finds the school's senior student, the fourth-generation apprentice, the rival "
            "fleet's dual-tradition sailor, and newer students meeting entirely on their own "
            "initiative, an equinox tradition none of them formally decided to start -- the "
            "doctrine's first fully self-organizing institutional body. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1362",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Season They Ran It Without Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-season-they-ran-it-without-him.md), Storm That "
            "Walks Alias Chronicle LXXXIX, wave 30. Kanja is away on other business for a full "
            "storm season; the school's self-organizing institution handles every call, rescue, "
            "and evacuation correctly without him present at all -- the first entry in the entire "
            "sub-series, across all aliases, where Kanja is absent from the events themselves "
            "rather than an unnamed guest. The fourth-generation apprentice runs his first solo "
            "evacuation command. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1363",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What He Came Back To Find\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-he-came-back-to-find.md), Storm That Walks Alias "
            "Chronicle XC, wave 30, closing the wave. Kanja reflects with Efa Gol, bookending "
            "MCD-986, on thirty waves of this alias culminating in an institution that finally "
            "didn't need him present at all -- distinguishing this alias from every other he "
            "wears, each of which required his specific presence at least once. Deliberately "
            "leaves the alias open for future waves rather than declaring it finished. No new "
            "named characters."
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
        assert r["category"] == "kanja-alias-chronicle", f"bad category on {r['id']}"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 263,
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
