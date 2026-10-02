#!/usr/bin/env python3
"""Batch 340: Chicago homage-era Territory Chronicle fable-review fixes
(Ide, Kwan, Umoja, Jibaro, Uhuru).

Applies the rule-statement amendments that accompany the prose-level
corrections already made to the Chronicle .md files under
docs/lords-of-cian/chronicles/: a pronoun fix (Kasa is he/him), removal of
a withdrawn-Chronicle-event reference (Kofi was never at the Furnace
District Strike), a terminology-inversion fix ("The Override" is personal
to Ofin, not institutional to the seat -- the deliberate inverse of Kiti's
seat-bound "The Long Tenure"), a timeline softening ("overnight" ->
"within a week" / "decades" -> "years"), and a mechanical reconciliation
of "The Occupation" (PH2-042)'s stated condition against its own already-
locked wording (an institution's own public shame, not a freestanding
"nothing to be ashamed of" moral-clarity test).

No new creative/worldbuilding facts -- every amendment here reconciles an
already-locked rule statement against other already-locked canon (PH2-042,
MCD-355/475) or against the Chronicle prose it describes, matching the
reconciliation-not-invention discipline of prior fable-review batches
(331, 338).
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Phase-review fable pass on the Chicago homage-era Territory Chronicles "
    "(Ide, Kwan, Umoja, Jibaro, Uhuru -- MCD-343, MCD-358/465/466/467/468/514/"
    "515/516/517 and their Chronicle files) against the full ledger and corpus."
)

AMENDMENTS = {
    "MCD-468": (
        "\"The Building That Wouldn't Choose a Side\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-building-that-wouldnt-choose-a-side.md), "
        "Jibaro Chronicle II. Omoba occupies a neighborhood schoolhouse with a "
        "genuinely mixed history of real community benefit and real neglect; 'The "
        "Occupation' (PH2-042) fails to activate, establishing that its protection "
        "requires an unambiguous public shame on the owning institution's side "
        "(PH2-042's 'an institution he can shame into complicity') and withholds "
        "itself where the institution's genuinely mixed record lets it claim it is "
        "reclaiming the space to remedy its own failures, forcing a slower "
        "conventional negotiation instead. An unnamed Kanja is present throughout, "
        "uninvolved. No new named characters. Second Jibaro territory Chronicle. "
        "Corrected Batch 340, 2026-10-02: reconciled the ability's stated condition "
        "with PH2-042's own already-locked wording."
    ),
    "MCD-516": (
        "Jibaro Chronicle III, \"The Week Five Doors Refused\" (full narrative text "
        "at docs/lords-of-cian/chronicles/jibaro-chronicle-iii-the-week-five-doors-"
        "refused.md). Five genuinely abandoned buildings across Jibaro are "
        "simultaneously occupied past the one-day threshold, all becoming "
        "permanently unreclaimable under 'The Occupation' (PH2-042), proving the "
        "ability scales to multiple sites at once as long as each site belongs to "
        "an institution he can shame into complicity (PH2-042) with the "
        "unambiguous public shame Chronicle II (MCD-468) established as the "
        "ability's real condition -- no purely private property is among the "
        "five. An unnamed Kanja helps carry belongings during the transition, "
        "uninvolved otherwise. No new named characters. Third Jibaro territory "
        "Chronicle. Corrected Batch 340, 2026-10-02: reconciled the ability's "
        "stated condition with PH2-042's own already-locked wording, and removed "
        "a tech-level anachronism (a 'rail depot') from the Chronicle prose."
    ),
    "MCD-343": (
        "Kwan Chronicle I ('The Weight of Being Asked') is the first entry in "
        "Kwan's own Chronicle series, per the established structure "
        "(MCD-334/335/336/339/340/341/342): each Phase 2 homage-era territory has "
        "its own Chronicles, with its own leader as protagonist and Kanja "
        "appearing only as an unnamed guest. After eleven weeks of stalled "
        "open-housing organizing, Kasa (PH2-038) personally asks an unnamed, "
        "long-entrenched ward broker not to march but to speak one public "
        "sentence endorsing the cause in his own voice. Kasa's signature ability "
        "('The Invitation,' PH2-038) is shown directly in operation for the first "
        "time via this fresh recipient, deliberately distinct from the ability's "
        "own already-locked backstory event (the coalition's invitation of a "
        "real-world- shaped outside leader, who per PH2-038 stays backstory-only "
        "and is never separately named or dramatized on-page, matching the "
        "Toussaint-Louverture/Ogoun-Xarey precedent): the broker's single "
        "sentence converts eleven previously unreachable homeowners into "
        "marchers within the week. The ability's stated cost is honored "
        "explicitly and not softened -- the broker's words do not stop a single "
        "rock when the resulting march is attacked three blocks in, and the "
        "eventual agreement is left as a victory of uncertain real weight, "
        "consistent with PH2-038's own framing. An unnamed Kanja is present at "
        "the march and shields a struck marcher without taking command, credit, "
        "or narrative authorship. No new named characters introduced. Slots "
        "into no existing mainline battle -- original homage-era material set "
        "in Kwan itself, continuing Muungano's own run of territory Chronicles "
        "(Umoja and Ide already have one; Jibaro and Uhuru still do not). "
        "Corrected Batch 340, 2026-10-02: 'overnight' corrected to 'within the "
        "week' to match the Kwan Chronicle II prose fix."
    ),
    "MCD-517": (
        "Uhuru Chronicle III, \"What the Seat Couldn't Give the Next Man\" (full "
        "narrative text at docs/lords-of-cian/chronicles/uhuru-chronicle-iii-"
        "what-the-seat-couldnt-give-the-next-man.md). Set after Ofin's "
        "already-locked capstone death (MCD-358): his successor, elected on the "
        "same coalition, discovers 'The Override' (PH2-044) did not pass to him "
        "-- confirming directly on the page that the ability was personal to "
        "Ofin's own endurance and never attached to the seat (the inverse of "
        "Kiti's seat-bound 'The Long Tenure', MCD-355/MCD-475), and the "
        "successor must build ordinary political endurance from nothing. An "
        "unnamed Kanja observes from the gallery, uninvolved. No new named "
        "characters. Third Uhuru territory Chronicle. Corrected Batch 340, "
        "2026-10-02: fixed a terminology inversion -- the ability is personal "
        "to Ofin, not institutional to the seat, the deliberate inverse of "
        "Kiti's own seat-bound ability."
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
            "Chicago homage-era Territory Chronicle fable-review fixes (Ide, "
            "Kwan, Umoja, Jibaro, Uhuru). Prose-level corrections applied "
            "directly to the Chronicle .md files: a pronoun fix (Kasa is "
            "he/him throughout, matching the rest of the Chicago corpus -- "
            "the-man-who-had-nothing-left-to-give.md and "
            "kwan-chronicle-iii-the-landlord-who-changed-his-own-mind.md); "
            "removal of a reference to Kofi having welded tenders and haulers "
            "at the Furnace District Strike, an event he was never present at "
            "per locked canon, reworded to his own earlier Umoja organizing "
            "(the-fire-that-spread-too-thin.md, "
            "umoja-chronicle-iii-the-fire-that-crossed-the-city.md); an "
            "explicit unnamed-Kanja narrative line added to Umoja Chronicle "
            "III, matching the rest of the corpus's convention; a real-world "
            "proper-noun leak ('Council Wars') removed from Uhuru Chronicle "
            "II; a tech-level anachronism ('rail depot') removed from Jibaro "
            "Chronicle III; a Kanja-placement inconsistency with Ide Chronicle "
            "I fixed in Ide Chronicle II (he reached the square ahead of her, "
            "not beside her); and, in Uhuru Chronicle III, a terminology "
            "inversion fixed ('institutional' corrected to 'personal' for an "
            "ability that belongs to the man, not the office -- the deliberate "
            "inverse of Kiti's own seat-bound 'The Long Tenure'), a "
            "non-office-specific term substituted for 'alderman', and a "
            "timeline overstatement softened ('decades' -> 'years'). Also "
            "applied the mechanical reconciliation of 'The Occupation' "
            "(PH2-042)'s stated condition against its own already-locked "
            "wording across both Jibaro entries that describe it (Chronicle "
            "II, the-building-that-wouldnt-choose-a-side.md, and Chronicle "
            "III, jibaro-chronicle-iii-the-week-five-doors-refused.md): the "
            "ability's real condition is an institution's own public shame "
            "('an institution he can shame into complicity', PH2-042's own "
            "wording), not a freestanding 'nothing to be ashamed of' "
            "moral-clarity test -- ownership-detail wording changes only, no "
            "new named characters or new plot beats. Rule statements amended "
            "to match: MCD-468, MCD-516 (the Occupation reconciliation), "
            "MCD-343 ('overnight' -> 'within the week', matching the Kwan "
            "Chronicle II prose fix), and MCD-517 (the institutional/personal "
            "terminology inversion). Deliberately left untouched, per "
            "instruction: E-6 (whether PH2- ability names should be quoted as "
            "in-world dialogue), E-9 (the project-wide un-prefixed-filename "
            "rename), all ENRICHMENT items, E-7/E-8 (low-priority register "
            "notes), and kwan-chronicle-i-the-weight-of-being-asked.md's own "
            "'overnight' wording (superseded by the MCD-343 statement "
            "amendment rather than a prose edit, per instruction)."
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
