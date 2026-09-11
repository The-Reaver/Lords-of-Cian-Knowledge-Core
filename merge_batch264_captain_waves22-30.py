#!/usr/bin/env python3
"""Batch 264: Captain Alias Chronicle waves 22-30 (27 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Captain's twenty-second through thirtieth Alias Chronicle waves (9 waves, 27 entries), "
    "drafted under Abad's blanket authorization to draft waves 22-30 for the Captain alias "
    "specifically. Pushes into genuinely new registers not yet used for this alias: an "
    "informal succession test during an extended absence, post-war bureaucratic friction, an "
    "impostor exploiting the name, a mountain-pass combat showcase, pure humanitarian-logistics "
    "work, Maret Vos recommitting to the crew a second time, the sub-series' first outright "
    "rescue failure (introducing two new minor named characters, Joran -- who dies -- and his "
    "orphaned daughter Mira, both collision-checked clean, with Mira recurring warmly through "
    "the rest of the run), a new standing memorial-wall institution, Efa Gol's own aging, a "
    "blind-dark boarding showcase, external-governance jurisdiction friction, Trinity gear used "
    "for pure structural rescue engineering, generational transmission of Callum Breck's "
    "shore-watch craft, the direct five-year succession-promise payoff resolving into a rotating "
    "council-chair structure rather than a named heir, a years-later integration check-in on the "
    "Directorate officer from MCD-559, large-scale peacetime disaster relief directly answering "
    "the 'what is Captain for now' question, the ledger's generational handoff to the deckhand "
    "Kanja once taught to read, the deepest crew self-sufficiency test yet (a six-week absence), "
    "a charter-defending combat showcase, a direct unforced mortality-gap conversation between "
    "Kanja and Efa Gol, the charter's long-blank fourth clause finally being written, a full "
    "founding-crew reunion, and a reflective, deliberately open-ended closer. Abad's approval: "
    "\"lets do this 22nd Alias Chronicle wave for any/all of the eleven aliases to the 30th wave "
    "and you are to continue uninterrupted until completion this includes rigorous testing, "
    "commit, push to main origin.\""
)

NEW_RULES = [
    {
        "id": "MCD-1364",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Command He Left Behind\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-command-he-left-behind.md), Captain Alias "
            "Chronicle LXIV, wave 22. Kanja is away eleven days on unrelated business when a "
            "storm wrecks a merchant convoy off Pier Nine; Corren Halst leads the full crew "
            "response start to finish without him, an informal, undiscussed test of the "
            "succession question. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1365",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Permit They Wouldn't Stamp\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-permit-they-wouldnt-stamp.md), Captain Alias "
            "Chronicle LXV, wave 22. Post-war reconstruction bureaucracy denies the crew a "
            "docking permit for lack of a property deed; resolved through patient honest "
            "process rather than bribery or defiance, ending in a new registry category built "
            "specifically for the crew. No new named characters, no combat."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1366",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Man Who Sold the Name\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-man-who-sold-the-name.md), Captain Alias "
            "Chronicle LXVI, wave 22, closing the wave. A con man collects protection fees by "
            "letting people assume he speaks for the crew; Kanja resolves it by having him "
            "repay every coin personally and offering him a real job rather than punishment. No "
            "new named characters. Closes wave 22."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1367",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Pass Above the Orphan Road\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-pass-above-the-orphan-road.md), Captain Alias "
            "Chronicle LXVII, wave 23. A detailed full-Trinity combat showcase on a high "
            "mountain pass -- a new environmental register for Captain -- defending a "
            "forty-one-child war-orphan resettlement caravan from a raiding party; first "
            "on-page use of Onyx of Oblivion's Whisper of Shadows inside the Captain "
            "sub-series. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1368",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ledger of the Unclaimed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ledger-of-the-unclaimed.md), Captain Alias "
            "Chronicle LXVIII, wave 23. A pure humanitarian-logistics entry with zero combat: "
            "Efa Gol spends five months at a borrowed table cross-referencing three overlapping "
            "relief-office registries to reunite war orphans with surviving family, reuniting "
            "seventeen children the original paperwork had missed. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1369",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Maret Vos Chose Again\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-maret-vos-chose-again.md), Captain Alias "
            "Chronicle LXIX, wave 23, closing the wave. Years after nearly walking (MCD-593), "
            "Maret Vos is offered an honorable, no-questions-asked exit and, after three days' "
            "genuine consideration, chooses to stay a second time for a more self-aware reason "
            "than the first. Maret Vos remains he/him throughout. No new named characters. "
            "Closes wave 23."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1370",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Night the River Won\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-night-the-river-won.md), Captain Alias "
            "Chronicle LXX, wave 24. The sub-series' first genuine, unresolved rescue failure: "
            "a levee breaks in the dark and the crew saves thirty-one people but not a civilian "
            "father, Joran, who drowns going back for his wife, leaving his eight-year-old "
            "daughter Mira orphaned. Introduces two new minor named characters, Joran "
            "(non-recurring) and Mira (recurring through the rest of this run), both "
            "collision-checked clean against the full live ledger. First entry, wave 24."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1371",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Council That Argued Over Grief\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-council-that-argued-over-grief.md), Captain "
            "Alias Chronicle LXXI, wave 24. The dispute council genuinely deadlocks 3-3, "
            "Kanja deliberately abstaining, over how the crew should formally carry a civilian "
            "loss it didn't cause but couldn't prevent -- the charter's written clauses proving "
            "insufficient for a question they never anticipated. Mira and the late Joran "
            "reused from MCD-1370. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1372",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Wall at Pier Nine\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-wall-at-pier-nine.md), Captain Alias Chronicle "
            "LXXII, wave 24, closing the wave. Mira's own answer breaks the council's deadlock: "
            "a new standing memorial wall is built at Pier Nine's seawall, open to civilian and "
            "crew names alike, Joran's name carved first by Mira's own hand, with Tam Sullen's "
            "name (Efa Gol's Black Trench-era pair-partner, CC-130) added retroactively as its "
            "founding-era link, kept distinct from the separately-established unnamed rigger of "
            "MCD-998. No new proper nouns. Closes wave 24."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1373",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Numbers Efa Gol Wouldn't Give Up\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-numbers-efa-gol-wouldnt-give-up.md), Captain "
            "Alias Chronicle LXXIII, wave 25. Efa Gol's own aging becomes concretely real for "
            "the first time, mirroring but not repeating Garren Hask's own mortality entry "
            "(MCD-1089); she refuses retirement but accepts a second set of checking hands -- "
            "the now-grown deckhand from MCD-1001 -- extending her established grief-through-"
            "numbers coping mechanism (MCD-609) into explicit backstory. No new named "
            "characters. First entry, wave 25."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1374",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Boarding in the Blind Dark\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-boarding-in-the-blind-dark.md), Captain Alias "
            "Chronicle LXXIV, wave 25. A detailed full-Trinity boarding-action combat showcase "
            "fought in total darkness during a moonless storm, the sub-series' first blind-dark "
            "engagement for this alias, with Efa Gol coordinating the operation by sound-count "
            "alone. Frees forty-one captives from a slaver vessel. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1375",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Girl Pier Nine Took In\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-girl-pier-nine-took-in.md), Captain Alias "
            "Chronicle LXXV, wave 25, closing the wave. Mira is given the same unforced choice "
            "of belonging already established for Sera (MCD-1057) rather than a path decided "
            "for her, gradually becoming 'the girl Pier Nine took in' at her own pace. Mira "
            "reused from MCD-1370-1372. No new named characters. Closes wave 25."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1376",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Magistrate Who Wanted Jurisdiction\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-magistrate-who-wanted-jurisdiction.md), Captain "
            "Alias Chronicle LXXVI, wave 26. A reconstruction-era magistrate claims formal "
            "court authority over the crew's informal protection and dispute-council role; "
            "resolved over six meetings into a liaison arrangement that recognizes the "
            "council's own rulings rather than subordinating them -- the charter's first real "
            "test against external governance. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1377",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Kinetic Transfer System Held Up\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-kinetic-transfer-system-held-up.md), "
            "Captain Alias Chronicle LXXVII, wave 26. A detailed rescue-engineering showcase "
            "with no enemy present: Mafesto's Kinetic Transfer System is used to redirect a "
            "collapsing tenement's structural force sideways rather than deflect an attack, "
            "buying roughly ninety seconds to complete an evacuation, a genuinely new "
            "application of the gear's established redirect mechanic (MCD-291). No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1378",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Watch Callum Breck Taught\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-watch-callum-breck-taught.md), Captain Alias "
            "Chronicle LXXVIII, wave 26, closing the wave. Callum Breck formally teaches the "
            "silent-signal shore-watch system he built out of his own post-Black-Trench silence "
            "to a new trainee over the better part of a year, the sub-series' first entry to "
            "dramatize the origin and generational transmission of his craft. No new proper "
            "nouns. Closes wave 26."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1379",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"Five Years, As Promised\" (full narrative text at "
            "docs/lords-of-cian/chronicles/five-years-as-promised.md), Captain Alias Chronicle "
            "LXXIX, wave 27. The direct, on-schedule payoff to Corren Halst's five-year promise "
            "(MCD-1090): Kanja asks her the succession question again, and she argues the "
            "question itself was wrong -- pointing to the self-sufficiency this run's own prior "
            "waves demonstrated as evidence the crew has been training itself not to need any "
            "single successor. No new named characters. First entry, wave 27."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1380",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Answer That Wasn't Yes or No\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-answer-that-wasnt-yes-or-no.md), Captain Alias "
            "Chronicle LXXX, wave 27. Corren Halst proposes a rotating, three-year term-limited "
            "council-chair seat rather than a fixed successor, with Kanja explicitly barred "
            "from ever holding it; the dispute council debates and adopts it, resolving the "
            "charter's blank fourth clause's underlying question without naming an heir. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1381",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The First Watch Under the New Chair\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-first-watch-under-the-new-chair.md), Captain "
            "Alias Chronicle LXXXI, wave 27, closing the wave. A detailed full-Trinity combat "
            "showcase, called and led by Corren Halst as the new rotating chair rather than by "
            "default deference to Kanja, defends the resettlement house from MCD-1367's raider "
            "network under real stress, proving the new structure works. No new named "
            "characters. Closes wave 27."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1382",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Officer Ten Years In\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-officer-ten-years-in.md), Captain Alias "
            "Chronicle LXXXII, wave 28. A years-later check-in on the unnamed Directorate "
            "officer from MCD-559, now fully, quietly integrated into the crew; he reveals he "
            "turned down an offered clean return to his old rank years earlier without telling "
            "anyone. No new named characters. First entry, wave 28."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1383",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Flood That Wasn't War\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-flood-that-wasnt-war.md), Captain Alias "
            "Chronicle LXXXIII, wave 28. A large-scale, enemy-free disaster-relief response to "
            "three levee failures on the same river system that took Joran, directly answering "
            "the open question left at 'The War the Name Outlived' (MCD-1004) of what the "
            "'Captain' institution is for now that the war is over. Mira, now seventeen, works "
            "the intake line using Efa Gol's registry method. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1384",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ledger Hask Handed Over\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ledger-hask-handed-over.md), Captain Alias "
            "Chronicle LXXXIV, wave 28, closing the wave. Garren Hask formally hands the "
            "crew's original ledger to the now-grown deckhand Kanja once taught to read "
            "(MCD-1001), the direct generational payoff to that entry and to MCD-1373. No new "
            "named characters. Closes wave 28."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1385",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Weeks He Wasn't There\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-weeks-he-wasnt-there.md), Captain Alias "
            "Chronicle LXXXV, wave 29. Kanja deliberately absents himself from Pier Nine for "
            "six weeks, the sub-series' deepest self-sufficiency test, extending 'The Command "
            "He Left Behind' (MCD-1364) from days to weeks; the crew runs an entirely ordinary "
            "season without him. No new named characters. First entry, wave 29."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1386",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What They Wouldn't Let Him Take\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-they-wouldnt-let-him-take.md), Captain Alias "
            "Chronicle LXXXVI, wave 29. A detailed full-Trinity combat showcase defends the "
            "charter's own free-membership clause (MCD-1056, extending the Maret Vos precedent, "
            "MCD-593) when a predatory labor guild coerces junior crew members into hidden-"
            "penalty contracts; resolved primarily through Garren Hask exposing the fine print "
            "rather than force. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1387",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Years He'd Have to Watch Them Lose\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-years-hed-have-to-watch-them-lose.md), Captain "
            "Alias Chronicle LXXXVII, wave 29, closing the wave. Efa Gol initiates an unprompted, "
            "crisis-free conversation with Kanja about the mortality gap between his lifespan "
            "and the crew's own; the sub-series' most direct confrontation of the theme "
            "established at MCD-920, left unresolved rather than comforted away. No new named "
            "characters. Closes wave 29."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1388",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fourth Line, Finally Written\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fourth-line-finally-written.md), Captain Alias "
            "Chronicle LXXXVIII, wave 30. The charter's long-blank fourth clause (MCD-1056) is "
            "finally written: not a named heir but the rotating chair, the taught ledger "
            "lineage, and the memorial wall as standing structure, plus an explicit clause "
            "treating Kanja's own eventual absence like any other protected departure. No new "
            "named characters. First entry, wave 30."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1389",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Day the Whole Founding Crew Sat Down Together\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-day-the-whole-founding-crew-sat-down-together.md), "
            "Captain Alias Chronicle LXXXIX, wave 30. An impromptu founding-anniversary "
            "gathering, the sub-series' fullest reunion entry, bringing together Corren Halst, "
            "Callum Breck, Garren Hask, Efa Gol, Mira, Danne Sok's daughter, Maret Vos, Pell "
            "Ostra, and Sera in one conflict-free celebratory scene. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1390",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Name Would Carry Without Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-name-would-carry-without-him.md), Captain "
            "Alias Chronicle XC, wave 30, closing the wave and this nine-wave run. A "
            "reflective, deliberately open-ended closer: Kanja walks Pier Nine alone after the "
            "reunion, looking toward a distant future he cannot and does not try to resolve on "
            "the page. No new named characters. Closes wave 30."
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
            "batch": 264,
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
