#!/usr/bin/env python3
"""Batch 289: Kazi Chronicles IX-XIII, Femi's (PH2-066) first five-Chronicle arc."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-12, no source document."

BATCH_NOTE = (
    "Five new Kazi Chronicles spotlighting Femi (PH2-066, homage to Ron March), matching Abad's "
    "direct authorization to \"give them five Chronicles each\" for Tunji and Femi, the two "
    "supporting-cast characters locked at PH2-065/PH2-066 in Batch 287. Femi himself is the true "
    "protagonist and viewpoint character throughout all five entries; Kanja appears only as an "
    "unnamed background guest with no command, credit, or resolution authorship, matching the "
    "established territory-Chronicle convention. Each entry explores a genuinely different facet of "
    "Femi's signature role (winning and holding an elected union seat as a foothold inside the "
    "institution the movement was built to pressure, per PH2-066): Kazi Chronicle IX, \"The Seat "
    "They Didn't Expect Him to Win\" (MCD-1528), dramatizes his actual campaign and election, won "
    "over skeptical rank-and-file who distrust him as 'the movement's man' through unglamorous, "
    "case-by-case grievance work rather than by trading on Irin's own reputation. Kazi Chronicle X, "
    "\"What the Books Showed\" (MCD-1529), shows him using his trustee seat's plain right of access "
    "to force an unexpected fund-audit vote no one on the fund's own board wanted, with Irin "
    "explicitly reflecting on it as a genuinely different, slower-moving tool alongside 'The Line "
    "Stops' rather than a lesser one. Kazi Chronicle XI, \"The Offer With the Teeth Filed Off\" "
    "(MCD-1530), dramatizes the seat becoming a real liability when the union's own regional office "
    "tries to neutralize him from inside with a co-optive promotion, then quiet retaliation, both "
    "refused or outlasted. Kazi Chronicle XII, \"Two Fronts, One War\" (MCD-1531), stages direct "
    "tactical friction between Femi's institutional-grievance route and Irin's confrontational "
    "floor-based halt over the same dispute, resolved not by either prevailing but by the affected "
    "workers choosing both at once, with Irin explicitly concluding the two approaches are "
    "complementary rather than competing. Kazi Chronicle XIII, \"The Weight of Being Inside\" "
    "(MCD-1532), closes the arc on a quiet personal register: the isolation of holding a seat "
    "trusted fully by neither the union leadership above him nor some of the rank-and-file who "
    "elected him. Every new proper noun was collision-checked against the full live ledger before "
    "drafting (zero prior hits); no new named characters were introduced in any of the five entries "
    "-- all reused already-locked figures (Irin, Tunji, Kunle, Kalamu) or left antagonists/minor "
    "figures deliberately unnamed, matching established precedent. Drafted in parallel with a "
    "sibling batch covering Tunji's own five Chronicles (numbered IV-VIII); no file or MCD-ID overlap "
    "between the two."
)

NEW_RULES = [
    {
        "id": "MCD-1528",
        "category": "phase2-homage-chronicle",
        "statement": (
            "Kazi Chronicle IX, \"The Seat They Didn't Expect Him to Win\" (full narrative text at "
            "docs/lords-of-cian/chronicles/kazi-chronicle-ix-the-seat-they-didnt-expect-him-to-win.md), "
            "the fourth entry in Kazi's own Chronicles and the first with Femi (PH2-066) as "
            "protagonist, not a Kanja Chronicle -- Kanja appears only as an unnamed guest, present "
            "distributing ballots at the vote count, granted no command, intervention, or resolution "
            "credit. Dramatizes the campaign and election PH2-066 already states as accomplished "
            "fact: skeptical rank-and-file dismiss Femi as 'the movement's man' unsuited to a "
            "trustee's seat, and he wins them over not by trading on Irin's (PH2-051) reputation but "
            "through unglamorous, case-by-case grievance-hearing work unconnected to any larger "
            "cause. He wins by eleven votes out of just under nine hundred cast, a foothold and "
            "nothing grander. Tunji (PH2-065) reused for continuity depth. The incumbent is "
            "deliberately left unnamed, matching established precedent for undetailed antagonists. "
            "No new named characters introduced. Fourth Kazi territory Chronicle."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1529",
        "category": "phase2-homage-chronicle",
        "statement": (
            "Kazi Chronicle X, \"What the Books Showed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/kazi-chronicle-x-what-the-books-showed.md), the fifth "
            "entry in Kazi's own Chronicles, protagonist Femi (PH2-066), not a Kanja Chronicle -- "
            "Kanja appears only as an unnamed guest, present moving fund archive at Femi's own "
            "request, granted no command, intervention, or resolution credit. Set after Kazi "
            "Chronicle IX (MCD-1528): Femi exercises his trustee seat's plain, unenforced right to "
            "inspect the union benefit fund's own books, finds three years of disability claims "
            "denied at nearly double the normal rate under a signature belonging to a man who had "
            "left the fund's employ before half the stamps were dated, and forces the fund's other "
            "four trustees into the first audit vote in living memory, passing three to two. Irin "
            "(PH2-051) explicitly reflects on the institutional route as a genuinely different, "
            "slower-moving tool alongside 'The Line Stops' rather than a lesser one, extending "
            "PH2-066's own framing that Irin treats Femi's seat as one more front rather than a "
            "settled victory. Kunle (PH2-063) reused as the messenger between Femi and Irin. The "
            "fund's chairman, administrator, and departed signatory are deliberately left unnamed. "
            "No new named characters introduced. Fifth Kazi territory Chronicle."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1530",
        "category": "phase2-homage-chronicle",
        "statement": (
            "Kazi Chronicle XI, \"The Offer With the Teeth Filed Off\" (full narrative text at "
            "docs/lords-of-cian/chronicles/kazi-chronicle-xi-the-offer-with-the-teeth-filed-off.md), "
            "the sixth entry in Kazi's own Chronicles, protagonist Femi (PH2-066), not a Kanja "
            "Chronicle -- Kanja appears only as an unnamed guest, present delivering returned "
            "committee files, granted no command, intervention, or resolution credit. Set some "
            "months after the fund audit (Kazi Chronicle X, MCD-1529): the union's own regional "
            "office, having watched Femi's audit cost the plant nothing directly, tries to "
            "neutralize him from inside the labor institution itself rather than oppose him from "
            "outside -- first with a co-optive full-time regional promotion that would remove him "
            "from the floor and from direct accountability to the men who elected him, then, when he "
            "refuses it, with quiet reassignment of his minor committee duties. Both attempts fail: "
            "he declines the promotion on the grounds that the seat's only real power is that the men "
            "who put him there can vote him back out, and he outlasts the retaliation by continuing "
            "the remaining work thoroughly enough that the reassigned duties are requested back by "
            "name within a season. Tunji (PH2-065) reused for continuity depth. The regional officer "
            "is deliberately left unnamed. A genuinely new register for the sub-series: the seat "
            "tested as a liability from inside the movement's own institution rather than from plant "
            "management. No new named characters introduced. Sixth Kazi territory Chronicle."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1531",
        "category": "phase2-homage-chronicle",
        "statement": (
            "Kazi Chronicle XII, \"Two Fronts, One War\" (full narrative text at "
            "docs/lords-of-cian/chronicles/kazi-chronicle-xii-two-fronts-one-war.md), the seventh "
            "entry in Kazi's own Chronicles, co-protagonists Femi (PH2-066) and Irin (PH2-051) -- "
            "the first Kazi Chronicle to give both leaders direct dialogue and shared page time "
            "rather than one referencing the other secondhand. Not a Kanja Chronicle; Kanja appears "
            "only as an unnamed guest, present throughout, granted no command, intervention, or "
            "resolution credit. A finishing-section reclassification stripping six workers' pay "
            "grade puts Irin's instinct to call an immediate halt ('The Line Stops,' PH2-051) in "
            "direct tactical tension with Femi's already-filed formal reclassification grievance; "
            "the six affected workers, consulted by both men together, choose to pursue both at "
            "once rather than either alone. The halt wins the six men's pay back within nine days; "
            "the grievance, unhurried by the halt's quick win, closes four months later with the "
            "reclassification rule struck from the contract's language entirely, foreclosing it for "
            "any future workers rather than only reversing it for these six. Irin explicitly "
            "concludes the two approaches are complementary rather than competing, directly "
            "dramatizing PH2-066's own framing that Irin treats Femi's seat as one more front. The "
            "six workers are deliberately left unnamed. No new named characters introduced. Seventh "
            "Kazi territory Chronicle."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1532",
        "category": "phase2-homage-chronicle",
        "statement": (
            "Kazi Chronicle XIII, \"The Weight of Being Inside\" (full narrative text at "
            "docs/lords-of-cian/chronicles/kazi-chronicle-xiii-the-weight-of-being-inside.md), the "
            "eighth entry in Kazi's own Chronicles, protagonist Femi (PH2-066), not a Kanja "
            "Chronicle -- Kanja appears only as an unnamed guest, present in a small, recurring, "
            "unglamorous way (restacking returned case files late in the evening), granted no "
            "command, intervention, or resolution credit. A quiet, personal-register closer to "
            "Femi's first five-Chronicle arc (Kazi Chronicles IX-XIII): dramatizes the isolation of "
            "holding an institutional seat trusted fully by neither the other trustees above him "
            "nor some of the rank-and-file who elected him, one of whom tells him to his face that "
            "he no longer 'feels the line' the way the rest of them do. Kalamu (PH2-064) offers and "
            "is declined the press-based remedy that resolved a comparable friction in Kazi "
            "Chronicle II (MCD-363), a deliberate contrast establishing that Femi's problem is trust, "
            "not information, and is not the kind Kalamu's own gift can fix -- resolved instead by "
            "Femi's own resolve to hold the seat regardless of being called both 'the movement's man' "
            "and 'the union's man' by different sides of the same divide. The younger hand who "
            "confronts him is deliberately left unnamed. No new named characters introduced. Eighth "
            "Kazi territory Chronicle, closing Femi's first wave of five."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 5, f"expected 5 new rules, got {len(NEW_RULES)}"
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 289,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-12, no source document",
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
