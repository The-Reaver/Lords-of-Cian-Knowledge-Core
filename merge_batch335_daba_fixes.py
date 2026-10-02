#!/usr/bin/env python3
"""Batch 335: Phase 2 fable-review fixes, Daba Character Chronicle track.

Amends 6 rule statements to match prose corrections already applied to
the Chronicle files: a stray "Wrenna" collision with Chronicle XXIX's
Isolde Wrenna (the Batch-296 cross-block rename to "Tessin" was never
applied to this rule's own statement); a Corrow/Elowen Marn/Sarel Doune
proper-noun collision sweep; a pronoun fix for Deryn Kettel.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Phase 2 fable-review of Daba's Character Chronicle track (56 Chronicles, "
    "MCD-1566-1620 plus MCD-1869-1874) against the full ledger and corpus."
)

AMENDMENTS = {
    "MCD-1581": (
        "Daba Chronicle XI, \"The Boy Who Broke the Scaffold\" (full narrative text at "
        "docs/lords-of-cian/chronicles/daba-chronicle-xi-the-boy-who-broke-the-scaffold.md), "
        "the eleventh entry in Daba's own Chronicle series and the launch wave's "
        "first-contact entry. During Kanja's otherwise-unrecorded formative years "
        "(MCD-1568), a 1804 scout, Riasa Vorn (a new named character, "
        "collision-checked clean), reports a young Kanja dismantling three Trust "
        "enforcers at the Sarrow ore-cut using nothing but a structural read of a "
        "collapsing ore-basket scaffold -- pure uninstructed Rexmar instinct per "
        "MCD-311, causing no deaths. Daba investigates personally and confronts the "
        "boy at the ruined scaffold; both recognize the other as dangerous and "
        "unknown, and the entry closes on deliberate mutual wariness rather than any "
        "trust, establishing the state the mentorship must still be built from. New "
        "named character: Riasa Vorn. Corrected Batch 335, 2026-10-02: \"Corrow\" "
        "renamed \"Sarrow\" to resolve a collision with the already-locked Bane-track "
        "\"Corrow ravine network.\""
    ),
    "MCD-1613": (
        "Daba Chronicle XLIII, \"What the Smoke Never Touched\" (full narrative text "
        "at docs/lords-of-cian/chronicles/daba-chronicle-xliii-what-the-smoke-never-"
        "touched.md), the forty-third entry in Daba's own Chronicle series. Pursuing "
        "an unrelated forgery case, Daba and lieutenant Elowen Sarn (new named "
        "character) pass within sight of the already-locked Furnace District Strike "
        "(MCD-244, age 21) from a ridge overlooking the smelting district; Daba "
        "recognizes the unnamed unarmed figure below without naming him aloud, "
        "judges correctly that the standoff will not turn violent, and deliberately "
        "withdraws south with his own escort rather than approach, letting the "
        "strike resolve entirely on its own -- the strike itself runs the already-"
        "locked eleven days (MCD-244), not the two this entry's prose originally "
        "misstated. Dramatizes 1804 operating near but never within one of Kanja's "
        "own campaigns, honoring MCD-1569's \"never folded into\" constraint without "
        "altering that battle's own locked participant account. New minor named "
        "character Elowen Sarn, collision-checked clean. Corrected Batch 335, "
        "2026-10-02: \"Elowen Marn\" renamed \"Elowen Sarn\" to resolve an intra-track "
        "surname collision with the separately-locked Marn family (MCD-1597); strike "
        "duration reconciled to MCD-244's locked eleven days."
    ),
    "MCD-1870": (
        "Daba Chronicle LII, 'The Ground That Almost Wasn't Enough' (full text at "
        "docs/lords-of-cian/chronicles/daba-chronicle-lii-the-ground-that-almost-"
        "wasnt-enough.md). Second entry of the wave -- the first Chronicle in the "
        "entire 53-entry corpus to put Daba's S-tier rating (CC-135) under genuine "
        "physical threat, since he holds no variant biology or density scaling and "
        "his rating comes entirely from guerrilla mastery and tactical discipline. "
        "Closing a safehouse at Threnfall personally after it is traced by a "
        "patient, unnamed Trust Compliance captain and eleven enforcers, Daba "
        "survives only by applying his own core doctrine (density is not power if "
        "the terrain neutralizes it, MCD-1567/1568) to save his own life for the "
        "first time, escaping through a disused well and drainage culvert rather "
        "than confronting the perimeter directly. He is genuinely wounded -- an "
        "injury decided by luck, not skill, the first time in his own life that "
        "distinction has applied -- and is saved on arrival at a second safehouse "
        "by Tessin's counting-as-containment response, a discipline he built into "
        "her without ever fully explaining why. Reuses Bren and Tessin. No new "
        "named characters; the antagonist captain and his enforcers are "
        "deliberately unnamed. Does not touch or dramatize the separate, still-"
        "undramatized Harek Vondel defeat reserved at MCD-1855. Corrected Batch "
        "335, 2026-10-02: \"Wrenna\" renamed \"Tessin\" throughout -- the Batch-296 "
        "cross-block rename (to avoid a collision with Chronicle XXIX's Isolde "
        "Wrenna) reached MCD-1620's own statement but was never applied here."
    ),
    "MCD-1871": (
        "Daba Chronicle LIII, 'What a Quiet Year Looks Like' (full text at "
        "docs/lords-of-cian/chronicles/daba-chronicle-liii-what-a-quiet-year-looks-"
        "like.md). Third entry of the wave, closing it -- a deliberate pure-texture "
        "entry with no threat and no plot advance, showing 1804's mature, "
        "semi-dormant present day to day: Kether's refined seven-day recruit "
        "vetting, Tessin running two cells and keeping an unprompted personal "
        "margin-note habit in her reports, Deryn Kettel's ordinary stable work, and "
        "Perrin teaching a new intake the same terrain-as-weapon lesson Daba once "
        "taught Kanja. Daba reads his annual list of names aloud and finds nothing "
        "new to add to it for the first time in years, a rare quiet accounting. "
        "Closes on a soft, deliberately unresolved callback to Chronicle LI's "
        "still-open house/Mika thread -- he does not go that night either, but for "
        "the first time thinks he might. Reuses Kether, Tessin, Deryn Kettel, and "
        "Perrin. No new named characters. Does not name or imply MCD-1569's "
        "unspecified Book 1 trigger for 1804. Corrected Batch 335, 2026-10-02: "
        "\"Wrenna\" renamed \"Tessin\" throughout; a separate male \"Tessin\" character "
        "(an invented backstory cross-contaminated from a different track's plot, "
        "with no basis anywhere else in Daba's corpus) corrected to Perrin, the "
        "already-established senior coordinator; Deryn Kettel's pronouns corrected "
        "to she/her, matching Chronicle XLI."
    ),
    "MCD-1873": (
        "Daba Chronicle LV, 'The Name Daba Never Spoke' (full text at "
        "docs/lords-of-cian/chronicles/daba-chronicle-lv-the-name-daba-never-"
        "spoke.md). Second entry of the wave. Prompted directly by his own "
        "near-death at Threnfall (MCD-1870), Daba confronts a structural gap he "
        "had never applied to himself: 1804's blind-succession doctrine (locked at "
        "MCD-1597, Yeva Tolan/Marn) protects every cell's leadership against "
        "capture or loss except his own. Over three weeks he extends the same "
        "structure to the network's own top for the first time, choosing Kether "
        "as his unwitting successor through the identical method used elsewhere -- "
        "small, unexplained authority handed over on ordinary days, culminating in "
        "giving her unsupervised access to the annual list's back room. Kether "
        "does not learn she has been chosen, and does not learn the true margin of "
        "Threnfall's danger either, matching the doctrine's own stated logic (a "
        "second who watches her leader for signs of the next near-miss is already "
        "half doing the job before she's needed). Reuses Kether, Bren, and Tessin. "
        "No new named characters. Corrected Batch 335, 2026-10-02: \"Wrenna\" "
        "renamed \"Tessin\" throughout, matching the sibling fixes to MCD-1870/1871."
    ),
    "MCD-1874": (
        "Daba Chronicle LVI, 'What Vetting Cannot See' (full text at "
        "docs/lords-of-cian/chronicles/daba-chronicle-lvi-what-vetting-cannot-"
        "see.md). Third entry of the wave, closing it -- the corpus's first "
        "genuine doctrine-limit entry for the vetting mechanism itself. Lisbet "
        "Doune, a courier who passed 1804's full year-long vetting faithfully and "
        "shows no malice or carelessness, mentions a safehouse's approximate "
        "location to her own sister in an ordinary, loving family conversation; "
        "the fragment travels through two further unrelated conversations before "
        "landing, by pure administrative bad luck, unread in the wrong Trust "
        "district and causing no actual harm. Tracing the chain, Daba concludes "
        "the vetting doctrine (MCD-1567) has a real, permanent hole it cannot "
        "close -- it tests for resistance under deliberate pressure but has no "
        "method for a person's ordinary, ungovernable love for someone never "
        "vetted at all, and closing that hole would mean punishing the exact "
        "quality that makes a person trustworthy in the first place. He does not "
        "tell Lisbet, judging that the fear it would create would cost more than "
        "the risk itself, and files the fact as a permanently unresolved, "
        "unaudited cost of the network's own safety rather than a problem to be "
        "solved. New named character Lisbet Doune, collision-checked clean. "
        "Reuses Kether. No new other named characters; no child-safety issues. "
        "Corrected Batch 335, 2026-10-02: \"Sarel Doune\" renamed \"Lisbet Doune\" to "
        "resolve a one-letter collision with the already-locked \"Serel\" (MCD-1608)."
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
            "Phase 2 fable-review of Daba's Character Chronicle track. Amends 6 "
            "rule statements (MCD-1581, 1613, 1870, 1871, 1873, 1874) to match "
            "prose corrections: a stray 'Wrenna' never swept by the Batch-296 "
            "cross-block Tessin rename (MCD-1870/1871/1873); 'Corrow' renamed "
            "'Sarrow' to resolve a collision with the already-locked Bane-track "
            "Corrow ravine network (MCD-1581, plus Chronicles XI/XV); a male "
            "'Tessin' paragraph cross-contaminated from a different character's "
            "plot, corrected to Perrin (MCD-1871); 'Elowen Marn' renamed 'Elowen "
            "Sarn' to resolve a collision with the Marn family (MCD-1613); 'Sarel "
            "Doune' renamed 'Lisbet Doune' to resolve a collision with 'Serel' "
            "(MCD-1874); Deryn Kettel's pronouns corrected to she/her (MCD-1871). "
            "Also fixed, prose-only (no further ledger-statement change needed): "
            "MCD-1619's own 'the name, not the number' origin misassigned to "
            "Kanja in Chronicle XLIX's prose, corrected back to Daba; a dozen "
            "stale/impossible timeline figures across Chronicles IV/VI/X/XI/XIV/"
            "XV/XVI/XVIII/XX/XXIII/XXXV/XXXVI/XXXIX/XL/XLI softened or corrected "
            "to match 1804's actual young age during the mentorship era and the "
            "locked casualty/duration figures at MCD-232/244; a runner 'Ossa' "
            "renamed 'Tova' in Chronicle XVI to resolve a collision with the "
            "already-locked villain Ossa Drem (CC-154); two writers'-room leaks "
            "reworded; one firearms anachronism and one terrain-word slip fixed."
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
