#!/usr/bin/env python3
"""Batch 342: Fable-review fixes, Detroit homage-era Territory Chronicles
(Kazi, Taifa, Hekalu, Nyansa, Kiti).

Applies the mechanical/reconciliation subset of a Fable-model read-only
review of the Detroit Territory Chronicle corpus: a world-bleed error (the
Sealbound Directorate named inside the Phase 2 homage World, MCD-313, which
it does not belong to), a floor-size/readership-count conflation across
several Kazi Chronicles (200 men on "The Line Stops" halt itself vs. 4,000
readers of Kalamu's separate pamphlet), a timeline-placement header error
(Kazi IX wrongly claimed to precede Kazi I), an intra-arc contradiction over
whether Femi's trustee seat is paid, a stale institutional-tenure figure in
Kiti Chronicle II, a five-entry ordinal-numbering error across Kazi
Chronicles IX-XIII (each one off by five, since Chronicles IV-VIII already
correctly claim fourth-eighth), a misattributed/mistimed incident in Kazi
Chronicle VIII, an ability cross-bleed in Kiti Chronicle III (Ofin's "The
Override" language wrongly describing Owusu's own "The Long Tenure"), and a
stale PH2-051 clause superseded by Tunji/Femi's own Batch 287 addition.

Items left deliberately untouched per the review's own NEEDS-ABAD and
skip list (the "Torvald" naming-convention question, whether to fold
Hekalu III/Taifa II-III/Kiti III's extensions back into their base PH2-
rules, tech-register idiom polish, category-tag normalization, a cosmetic
Kazi X prose nit, and all enrichment items) are not applied here.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Fable-model read-only review of the Detroit homage-era Territory "
    "Chronicles (Kazi, Taifa, Hekalu, Nyansa, Kiti) against the full ledger "
    "and corpus."
)

AMENDMENTS = {
    "MCD-472": (
        "\"The Oath He Didn't Mean\" (full narrative text at docs/lords-of-cian/chronicles/the-oath-he-didnt-mean.md), Taifa Chronicle II. A new recruit swears the oath insincerely and is tempted into betrayal by a hostile outside patrol; Osei's inability to feel him through 'Kin at a Distance' (PH2-053) -- unlike every genuine sworn hand -- is itself the warning that gets Osei to the outer post in time, dramatizing the ability's sincerity requirement as a literal functioning mechanic. An unnamed Kanja is present, uninvolved. No new named characters. Second Taifa territory Chronicle. Corrected Batch 342, 2026-10-02: the threatening patrol was originally misdescribed as a Sealbound Directorate patrol, a world-bleed error -- the Directorate belongs to mainline Cian, not this homage World (MCD-313); corrected to an outside patrol sent by the claimed land's hostile neighbors."
    ),
    "MCD-1528": (
        "Kazi Chronicle IX, \"The Seat They Didn't Expect Him to Win\" (full narrative text at docs/lords-of-cian/chronicles/kazi-chronicle-ix-the-seat-they-didnt-expect-him-to-win.md), the ninth entry in Kazi's own Chronicles and the first with Femi (PH2-066) as protagonist, not a Kanja Chronicle -- Kanja appears only as an unnamed guest, present distributing ballots at the vote count, granted no command, intervention, or resolution credit. Set after the events of Kazi Chronicle I (MCD-351), dramatizing the campaign and election PH2-066 already states as accomplished fact: skeptical rank-and-file dismiss Femi as 'the movement's man' unsuited to a trustee's seat, and he wins them over not by trading on Irin's (PH2-051) reputation but through unglamorous, case-by-case grievance-hearing work unconnected to any larger cause. He wins by eleven votes out of just under nine hundred cast, a foothold and nothing grander. Tunji (PH2-065) reused for continuity depth. The incumbent is deliberately left unnamed, matching established precedent for undetailed antagonists. No new named characters introduced. Ninth Kazi territory Chronicle. Corrected Batch 342, 2026-10-02: this Chronicle originally misdescribed its own timeline placement (claiming to precede Irin's first halt, Kazi Chronicle I, MCD-351, rather than following it) and its own ordinal position (claiming to be the fourth entry rather than the ninth, since Chronicles IV-VIII already correctly claim fourth-eighth); both corrected."
    ),
    "MCD-1529": (
        "Kazi Chronicle X, \"What the Books Showed\" (full narrative text at docs/lords-of-cian/chronicles/kazi-chronicle-x-what-the-books-showed.md), the tenth entry in Kazi's own Chronicles, protagonist Femi (PH2-066), not a Kanja Chronicle -- Kanja appears only as an unnamed guest, present moving fund archive at Femi's own request, granted no command, intervention, or resolution credit. Set after Kazi Chronicle IX (MCD-1528): Femi exercises his trustee seat's plain, unenforced right to inspect the union benefit fund's own books, finds three years of disability claims denied at nearly double the normal rate under a signature belonging to a man who had left the fund's employ before half the stamps were dated, and forces the fund's other four trustees into the first audit vote in living memory, passing three to two. Irin (PH2-051) explicitly reflects on the institutional route as a genuinely different, slower-moving tool alongside 'The Line Stops' rather than a lesser one, extending PH2-066's own framing that Irin treats Femi's seat as one more front rather than a settled victory. Kunle (PH2-063) reused as the messenger between Femi and Irin. The fund's chairman, administrator, and departed signatory are deliberately left unnamed. No new named characters introduced. Tenth Kazi territory Chronicle. Corrected Batch 342, 2026-10-02: Irin's dialogue originally reused the pamphlet's four-thousand-reader circulation figure for the much smaller halt itself ('The Line Stops' binds roughly two hundred men on the plant floor, not four thousand); corrected. Also corrects this Chronicle's own ordinal self-description (fifth -> tenth), since Chronicles IV-VIII already correctly claim fourth-eighth."
    ),
    "MCD-1530": (
        "Kazi Chronicle XI, \"The Offer With the Teeth Filed Off\" (full narrative text at docs/lords-of-cian/chronicles/kazi-chronicle-xi-the-offer-with-the-teeth-filed-off.md), the eleventh entry in Kazi's own Chronicles, protagonist Femi (PH2-066), not a Kanja Chronicle -- Kanja appears only as an unnamed guest, present delivering returned committee files, granted no command, intervention, or resolution credit. Set some months after the fund audit (Kazi Chronicle X, MCD-1529): the union's own regional office, having watched Femi's audit cost the plant nothing directly, tries to neutralize him from inside the labor institution itself rather than oppose him from outside -- first with a co-optive full-time regional promotion that would remove him from the floor and from direct accountability to the men who elected him, then, when he refuses it, with quiet reassignment of his minor committee duties. Both attempts fail: he declines the promotion on the grounds that the seat's only real power is that the men who put him there can vote him back out, and he outlasts the retaliation by continuing the remaining work thoroughly enough that the reassigned duties are requested back by name within a season. Tunji (PH2-065) reused for continuity depth. The regional officer is deliberately left unnamed. A genuinely new register for the sub-series: the seat tested as a liability from inside the movement's own institution rather than from plant management. No new named characters introduced. Eleventh Kazi territory Chronicle. Corrected Batch 342, 2026-10-02: corrects this Chronicle's own ordinal self-description (sixth -> eleventh), since Chronicles IV-VIII already correctly claim fourth-eighth."
    ),
    "MCD-1531": (
        "Kazi Chronicle XII, \"Two Fronts, One War\" (full narrative text at docs/lords-of-cian/chronicles/kazi-chronicle-xii-two-fronts-one-war.md), the twelfth entry in Kazi's own Chronicles, co-protagonists Femi (PH2-066) and Irin (PH2-051) -- the first Kazi Chronicle to give both leaders direct dialogue and shared page time rather than one referencing the other secondhand. Not a Kanja Chronicle; Kanja appears only as an unnamed guest, present throughout, granted no command, intervention, or resolution credit. A finishing-section reclassification stripping six workers' pay grade puts Irin's instinct to call an immediate halt ('The Line Stops,' PH2-051) in direct tactical tension with Femi's already-filed formal reclassification grievance; the six affected workers, consulted by both men together, choose to pursue both at once rather than either alone. The halt wins the six men's pay back within nine days; the grievance, unhurried by the halt's quick win, closes four months later with the reclassification rule struck from the contract's language entirely, foreclosing it for any future workers rather than only reversing it for these six. Irin explicitly concludes the two approaches are complementary rather than competing, directly dramatizing PH2-066's own framing that Irin treats Femi's seat as one more front. The six workers are deliberately left unnamed. No new named characters introduced. Twelfth Kazi territory Chronicle. Corrected Batch 342, 2026-10-02: corrects this Chronicle's own ordinal self-description (seventh -> twelfth), since Chronicles IV-VIII already correctly claim fourth-eighth."
    ),
    "MCD-1532": (
        "Kazi Chronicle XIII, \"The Weight of Being Inside\" (full narrative text at docs/lords-of-cian/chronicles/kazi-chronicle-xiii-the-weight-of-being-inside.md), the thirteenth entry in Kazi's own Chronicles, protagonist Femi (PH2-066), not a Kanja Chronicle -- Kanja appears only as an unnamed guest, present in a small, recurring, unglamorous way (restacking returned case files late in the evening), granted no command, intervention, or resolution credit. A quiet, personal-register closer to Femi's first five-Chronicle arc (Kazi Chronicles IX-XIII): dramatizes the isolation of holding an institutional seat trusted fully by neither the other trustees above him nor some of the rank-and-file who elected him, one of whom tells him to his face that he no longer 'feels the line' the way the rest of them do. Kalamu (PH2-064) offers and is declined the press-based remedy that resolved a comparable friction in Kazi Chronicle II (MCD-363), a deliberate contrast establishing that Femi's problem is trust, not information, and is not the kind Kalamu's own gift can fix -- resolved instead by Femi's own resolve to hold the seat regardless of being called both 'the movement's man' and 'the union's man' by different sides of the same divide. The younger hand who confronts him is deliberately left unnamed. No new named characters introduced. Thirteenth Kazi territory Chronicle, closing Femi's first wave of five. Corrected Batch 342, 2026-10-02: corrects this Chronicle's own ordinal self-description (eighth -> thirteenth), since Chronicles IV-VIII already correctly claim fourth-eighth; also fixes an intra-arc contradiction where the younger hand's dialogue described Femi's unpaid trustee seat as a paid 'salary line.'"
    ),
    "PH2-051": (
        "Irin leads Kazi, homage to General Baker, the League of Revolutionary Black Workers' central founding organizer. 'Irin' is Yoruba for 'iron.' An assembly-line worker who turns the plant floor itself into the site of struggle, refusing to let the line's own leverage go to waste. Two lieutenants drawn from the real DRUM/League leadership circle stand as his founding co-organizers -- Kunle (PH2-063, homage to Ken Cockrel Sr.) and Kalamu (PH2-064, a composite homage to John Watson and Mike Hamlin); his in-plant organizing partner Tunji (PH2-065) and trustee-seat holder Femi (PH2-066) were added in Batch 287. Signature ability, 'The Line Stops': when Irin calls a halt, everyone bound into the same production chain feels it and understands why, instantly, without a word passed hand to hand. Cost: only works on people already structurally bound into the same chain of labor -- useless as leverage on anyone standing outside that relationship."
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
            "Fable-review fixes, Detroit homage-era Territory Chronicles "
            "(Kazi, Taifa, Hekalu, Nyansa, Kiti). Mechanical/reconciliation "
            "subset only, applied exactly as instructed. Amends MCD-472 "
            "(a Sealbound Directorate world-bleed error in Taifa Chronicle "
            "II -- the Directorate belongs to mainline Cian, not the Phase "
            "2 homage World, MCD-313); MCD-1528 through MCD-1532 (Kazi "
            "Chronicles IX-XIII: a five-entry ordinal-numbering error, "
            "each off by five since Chronicles IV-VIII already correctly "
            "claim fourth-eighth; MCD-1528 also corrects a timeline-"
            "placement error that had Chronicle IX precede Kazi Chronicle "
            "I rather than follow it; MCD-1529 also corrects a floor-size/"
            "readership-count conflation, 200 men on 'The Line Stops' "
            "halt itself vs. 4,000 readers of Kalamu's separate pamphlet; "
            "MCD-1532 also corrects an intra-arc contradiction over "
            "whether Femi's trustee seat is paid); and PH2-051 (a stale "
            "clause describing Kunle and Kalamu as Irin's only, "
            "not-yet-individually-named co-organizers, superseded by "
            "Tunji's and Femi's own addition in Batch 287). Also fixed, "
            "prose-only (no further ledger-statement change needed beyond "
            "the above): the same floor-size/readership conflation in "
            "Kazi Chronicle II (MCD-363, prose only -- its own statement "
            "did not carry the error); a misattributed and mistimed "
            "incident in Kazi Chronicle VIII (the withheld name was "
            "'the plant manager... the same manager from the gantry "
            "season,' corrected to a line supervisor predating the "
            "gantry walkout); and an ability cross-bleed in Kiti "
            "Chronicle III (prose wrongly described Owusu's 'The Long "
            "Tenure,' PH2-059, using Ofin's 'The Override' language -- "
            "corrected to an attrition-outlasting description matching "
            "Owusu's own ability) and a stale 'six years' institutional-"
            "tenure figure in Kiti Chronicle II (the-weeks-the-chair-sat-"
            "empty.md, corrected to two decades). Deliberately left "
            "untouched per the review's own NEEDS-ABAD and skip list: "
            "the 'Torvald' naming-convention question (Kazi Chronicles V "
            "and VIII); whether to fold Hekalu III/Taifa II-III/Kiti "
            "III's extensions back into PH2-055/053/059's own base rule "
            "text; tech-register idiom polish; category-tag "
            "normalization (handled corpus-wide separately); a cosmetic "
            "Kazi X prose nit ('eleven days' worth of pages'); and all "
            "enrichment items."
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
