#!/usr/bin/env python3
"""Batch (computed dynamically): Phase 2 fable-review fixes, Ozmund Verehimu Character
Chronicle track (120 Chronicles, MCD-1730 through MCD-1849).

Applies the subset of the fable-review findings (C1-C10, E1-E4; C9/E5/E6 excluded as
needing Abad's own direct creative ruling) that are pure reconciliation against
already-locked canon or mechanical rule-ID corrections -- no new creative/world-
building facts. The corresponding prose-level fixes were already applied directly to
the 17 affected Chronicle .md files under docs/lords-of-cian/chronicles/, each with
its own "Corrected Batch 333, 2026-10-02" note in its header.

Rule statements amended here:
  - MCD-1741/1742/1743/1744/1745 (C1): "Set roughly N years before the Fulfillment
    Ceremony (MCD-025)" reworded to "Set strictly pre-Fulfillment-Ceremony (MCD-025),
    Ozmund age N" -- removes an implied fixed age-gap framing the larger open question
    (the ~190-year gap vs. this strand's own internal ages) doesn't actually need
    resolved to fix. The larger gap-framing question itself is NOT resolved here and
    remains open for Abad.
  - MCD-1806 (C10): "Ozmund, roughly twenty-six" -> "Ozmund, roughly twenty-five" to
    match the corrected Chronicle LXXVII file (timing moved from two years after
    Chronicle LXXVI to roughly a year after it, consistent with Chronicle XVI's age
    twenty-five and the year-long absence of Chronicle XXXIV).
  - MCD-1819 (C3): removes a reserved-thread leak -- "exercised through his Crown-Scar"
    reworded to "exercised through raw power," and the Crown-Scar's true siphon nature
    (MCD-290) is no longer referenced at all; replaced with a reference to his
    inherited physical power (the Density Spike, MCD-024) as the form of authority he
    declines to lean on.
  - MCD-1843 (C5 + E1): "Young Ozmund extends" -> "Ozmund, in his mid-twenties or
    later, extends" (this entry is part B of the coming-of-age strand's second wave,
    not his boyhood); Osric's citation corrected from Chronicle I (MCD-1730, which has
    no Osric) to his actual introduction at Chronicle XLVI (MCD-1775).
  - MCD-1844 (E1): Cobb's citation corrected from Chronicle XLIII (MCD-1772, which is
    tutor Alric Fenmoor, not Cobb) to his actual introduction at Chronicle XLIV
    (MCD-1773).
  - MCD-1778 (E1): the Aldenmoor citation corrected from MCD-1747 (Bevin's own
    introduction at Chronicle XVIII) to MCD-1746 (the actual introduction of the
    Aldenmoor settlement at Chronicle XVII).

C2, C4, C6, C7, C8, and the remaining E1 sub-items (the MCD-016 non-existent citation,
further Osric/Cobb/Aldenmoor mis-citations in other files) required only prose-level
fixes to the Chronicle .md files themselves, with no corresponding rule-statement text
to amend (verified against the live ledger before drafting this script).

Deliberately NOT applied, left for Abad's own ruling: C1's larger ~190-year gap-framing
question (only the "roughly N years before the Ceremony" phrasing itself was
mechanically reworded); C4's pre-existing MCD-138/MCD-1850 five-thousand-year tension
(flagged in the Chronicle XX header note, not resolved); C9 (an age-related creative
call); E5 (the Karkosa Atlas-queue item); E6 (whether to lock a specific Book-2
duration number).
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Phase 2 fable-review of the Ozmund Verehimu Character Chronicle track (120 "
    "Chronicles, MCD-1730 through MCD-1849) against the full ledger. "
    "Mechanical/reconciliation subset only (findings C1-C10, E1-E4; C9/E5/E6 excluded "
    "as needing Abad's own direct creative ruling)."
)

AMENDMENTS = {
    "MCD-1741": (
        "Ozmund Chronicle XII, \"Her Son, Not Her Line\" (full narrative text at "
        "docs/lords-of-cian/chronicles/ozmund-chronicle-xii-her-son-not-her-line.md), "
        "opens the Val Mirel strand of Ozmund's Character Chronicle series. Set "
        "strictly pre-Fulfillment-Ceremony (MCD-025), Ozmund age nine, Aethelgard "
        "alive and present but deliberately non-intervening: Val Mirel Kareth "
        "(MCD-101/CC-004/CC-016) teaches a nine-year-old Ozmund an original Kareth "
        "War-Order discipline, the Stone Count -- stillness that outlasts urgency "
        "rather than performs it -- directly against House Verehimu's court instinct "
        "to always be seen doing something, giving Ozmund his first on-page moment of "
        "holding both inheritances at once. Plants formative groundwork for his "
        "already-locked Solid-Dense Terra 'immovable foundation' physics (WC-006) and "
        "his Book 2 command-discipline at the repulsion of General Baryon "
        "(MCD-279/280). Narrated by Red Beard (Tarn Cestari) per VB-020/022/CC-020, "
        "reconstructed from a story Ozmund told him years later. No new named "
        "characters."
    ),
    "MCD-1742": (
        "Ozmund Chronicle XIII, \"The Reckoning of a Seventh Wing Tactician\" (full "
        "narrative text at docs/lords-of-cian/chronicles/"
        "ozmund-chronicle-xiii-the-reckoning-of-a-seventh-wing-tactician.md), second "
        "entry in the Val Mirel strand. Set strictly pre-Fulfillment-Ceremony "
        "(MCD-025), Ozmund age fifteen, Aethelgard alive but absent (referenced "
        "only): facing a patient raiding band on the grain road, Val Mirel Kareth's "
        "Seventh Wing tactical discipline (MCD-101/CC-004) -- watching a threat long "
        "enough to learn what it hides rather than acting on what it shows -- is set "
        "directly against a House Verehimu seneschal's political toll-negotiation "
        "method for the identical problem, with fifteen-year-old Ozmund taken along "
        "only to observe. Resolves with Ozmund understanding both approaches as the "
        "same discipline paid in different currencies, coin against patience, rather "
        "than opposed philosophies. Narrated by Red Beard (Tarn Cestari) per "
        "VB-020/022/CC-020, reconstructed from a story Ozmund told him twice, years "
        "apart, with no factual variance between tellings. No new named characters."
    ),
    "MCD-1743": (
        "Ozmund Chronicle XIV, \"What She Chose Not to Fight\" (full narrative text "
        "at docs/lords-of-cian/chronicles/"
        "ozmund-chronicle-xiv-what-she-chose-not-to-fight.md), third entry in the Val "
        "Mirel strand. Set strictly pre-Fulfillment-Ceremony (MCD-025), Ozmund age "
        "nineteen, Aethelgard alive but present only in reference: after a court "
        "reception where Val Mirel Kareth is treated with hollow, distant deference "
        "rather than genuine belonging, nineteen-year-old Ozmund confronts her "
        "directly about her chosen absence from his upbringing. She explains it as a "
        "deliberate protection of his own earned identity -- refusing to let him grow "
        "up inside a shadow he'd never get to prove he didn't need -- extending the "
        "profile's 'consent and earned loyalty' values layer and 'author of your own "
        "will' throughline, while making clear the choice costs her as much as it "
        "costs him. Deliberately left unresolved rather than healed. Narrated by Red "
        "Beard (Tarn Cestari) per VB-020/022/CC-020, reconstructed from a story "
        "Ozmund told him only once, very late. No new named characters."
    ),
    "MCD-1744": (
        "Ozmund Chronicle XV, \"The War-Sister's Warning\" (full narrative text at "
        "docs/lords-of-cian/chronicles/ozmund-chronicle-xv-the-war-sisters-warning.md"
        "), fourth entry in the Val Mirel strand. Set strictly pre-Fulfillment-"
        "Ceremony (MCD-025), Ozmund age twenty-two: on the last night of her longest "
        "visit, Val Mirel Kareth tells twenty-two-year-old Ozmund of an old, unnamed "
        "debt carried from the war to a woman she never names, torn apart from her by "
        "the war itself -- an oblique, deliberately unconfirmed forward reference "
        "toward MCD-101/MCD-137 (Val Saeryn and Val Mirel Kareth as war-sisters, both "
        "alive, Val Saeryn in deep cover) that neither names Val Saeryn nor Kanja nor "
        "explains the cousin relationship, fully consistent with MCD-318's locked "
        "fact that the cousins were essentially strangers until adulthood. She "
        "instructs him to recognize and honor the debt without demanding explanation "
        "if it is ever called through a line he cannot predict. Narrated by Red Beard "
        "(Tarn Cestari) per VB-020/022/CC-020, reconstructed from a story Ozmund only "
        "fully understood the possible weight of much later. No new named characters."
    ),
    "MCD-1745": (
        "Ozmund Chronicle XVI, \"A Different Kind of Armor\" (full narrative text at "
        "docs/lords-of-cian/chronicles/"
        "ozmund-chronicle-xvi-a-different-kind-of-armor.md), closing entry in the Val "
        "Mirel strand. Set strictly pre-Fulfillment-Ceremony (MCD-025), Ozmund age "
        "twenty-five, Aethelgard alive but present only in reference: after the death "
        "of an unnamed old House Guard soldier who helped raise him, twenty-five-"
        "year-old Ozmund's Verehimu-taught public composure leaves him with nowhere "
        "to put his grief; Val Mirel Kareth teaches him a second original Kareth "
        "War-Order discipline, the Hollow Stand -- built from the same root as the "
        "Stone Count (MCD-1741) but aimed at holding grief fully through rather than "
        "folding it away -- and stays with him through it, giving the strand its "
        "emotional high point and the project's first sustained, three-dimensional "
        "scene of warmth between mother and son. Plants the emotional root of the "
        "profile's 'grief converted directly into infrastructure' defense-mechanism "
        "layer, later expressed at Legion scale. Narrated by Red Beard (Tarn Cestari) "
        "per VB-020/022/CC-020, reconstructed from a story Ozmund told him only once, "
        "near the end. No new named characters; closes the five-entry Val Mirel "
        "strand."
    ),
    "MCD-1806": (
        "Ozmund Chronicle LXXVII, \"The Years She Would Not Have\" -- Val Mirel "
        "strand wave 3, Aethelgard alive. Ozmund, roughly twenty-five, finds Val "
        "Mirel in a private, unguarded moment of existential reckoning with the "
        "disparity between her ~89,003-year Kareth lifespan (MCD-101) and his own "
        "much shorter one. She names it not as fear but as a debt entered knowingly, "
        "and states she would rather love him briefly than never at all -- deepening, "
        "without contradicting, Chronicle XIV's (MCD-1743) rationale for her chosen "
        "distance. States nothing about her own eventual fate."
    ),
    "MCD-1819": (
        "Ozmund Chronicle XC, \"What the Room Had Learned to Expect of Him,\" "
        "closing wave 3 of the House politics strand. The wave's closing, "
        "retrospective entry: Red Beard and Ozmund reflect together on how, across "
        "ages 23-27, the region came to expect honest hearing and fair dealing from "
        "Ozmund in these small rooms, and how that earned, dispute-by-dispute "
        "political authority became the one form of power he fully trusts, since it "
        "was built rather than inherited or exercised through raw power. Synthesizes "
        "Chronicles LXXX-LXXXIX by name without advancing any reserved thread -- his "
        "inherited physical power (the Density Spike, MCD-024) is referenced only as "
        "a form of authority he chooses not to lean on; the Crown-Scar's true nature "
        "(MCD-290) is not referenced. No new named characters. Closes the House "
        "politics strand at 20 entries total (Chronicles XVII-XX, XXXVI-XL, LXXX-XC)."
    ),
    "MCD-1843": (
        "Ozmund Chronicle CXIV, \"What He Helped Another Carry\" -- coming-of-age "
        "strand wave 2. Ozmund, in his mid-twenties or later, extends Val Mirel "
        "Kareth's Hollow Stand discipline (MCD-1745) outward for the first time, "
        "finding Osric alone with a private, previously unstated thirty-year-old "
        "grief (his wife's death) and sitting with him in silence rather than trying "
        "to fix it. He learns that the discipline his mother gave him for holding his "
        "own unanswerable weight was \"built to be lent,\" not only for his own use. "
        "Deliberately echoes without restaging the earlier Joren entry (MCD-1776). No "
        "new named characters (Osric reused from MCD-1775)."
    ),
    "MCD-1844": (
        "Ozmund Chronicle CXV, \"The Race He Let Himself Lose\" -- coming-of-age "
        "strand wave 2. A rare, unguarded entry of pure joy -- Ozmund and stable boy "
        "Cobb (MCD-1773) race repeatedly in the lower paddock, and Ozmund realizes he "
        "has been unconsciously holding back even in a harmless footrace out of "
        "long-ingrained habit. One afternoon he runs freely for once, wins "
        "decisively, and Cobb's cheerful, uncomplicated reaction to losing teaches "
        "him that the careful version of himself is a chosen door, not the only one "
        "available, even though he goes back to holding back the very next day. No "
        "new named characters."
    ),
    "MCD-1778": (
        "Ozmund Chronicle XLIX, \"What He Practiced in the Dark\" (full narrative "
        "text at docs/lords-of-cian/chronicles/"
        "ozmund-chronicle-xlix-what-he-practiced-in-the-dark.md), fourth entry of "
        "the closing coming-of-age strand, strictly pre-ceremony. The series' most "
        "interior, least-witnessed entry to date: alone at night at the "
        "already-locked flooded quarry near Aldenmoor (MCD-1746), young Ozmund "
        "deliberately tests the floor rather than the ceiling of his Density Spike "
        "-- the one part of his inheritance genuinely his to define rather than "
        "born into -- extending CC-015/017/MCD-024's 'no threshold to cross' "
        "psychology into its most self-authored register. Narrator Red Beard "
        "explicitly flags this as reconstructed from a single sparse mention, the "
        "thinnest evidentiary base in the series. No new named characters."
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
            "Phase 2 fable-review of the Ozmund Verehimu Character Chronicle track "
            "(120 Chronicles). Amends MCD-1741/1742/1743/1744/1745 (reworded 'Set "
            "roughly N years before the Fulfillment Ceremony' to 'Set strictly "
            "pre-Fulfillment-Ceremony, Ozmund age N'), MCD-1806 (age corrected from "
            "twenty-six to twenty-five to match the corrected Chronicle LXXVII "
            "file), MCD-1819 (removes a Crown-Scar reserved-thread leak, reworded to "
            "reference only his inherited physical power/Density Spike as a form of "
            "authority declined), MCD-1843 (corrected 'Young Ozmund' to an explicit "
            "mid-twenties-or-later framing, and Osric's citation from Chronicle I/"
            "MCD-1730 -- which has no Osric -- to his real introduction at Chronicle "
            "XLVI/MCD-1775), MCD-1844 (Cobb's citation corrected from Chronicle "
            "XLIII/MCD-1772 -- which is tutor Alric Fenmoor, not Cobb -- to his real "
            "introduction at Chronicle XLIV/MCD-1773), and MCD-1778 (the Aldenmoor "
            "citation corrected from MCD-1747, Bevin's own introduction, to "
            "MCD-1746, the actual introduction of the Aldenmoor settlement). Also "
            "fixed, prose-only (no further ledger-statement change needed): 12 "
            "additional Chronicle .md files under docs/lords-of-cian/chronicles/ "
            "ozmund-chronicle-*.md, each carrying its own 'Corrected Batch 333, "
            "2026-10-02' header note -- a mistaken 'ordinary lifespan' phrasing for "
            "Val Mirel (XCII/LXXVII's own text); a dangling five-thousand-year age "
            "claim softened to vaguer phrasing in Chronicle XX (flagging the "
            "pre-existing MCD-138/MCD-1850 tension as still open, not resolved "
            "here); a Commander 'Rell' renamed 'Welk' in Chronicle XLV to resolve a "
            "collision with the established Rell/Tamsy fen-household family "
            "(Chronicle LXIV, MCD-1793); a continuity-notes phrasing fix in "
            "Chronicle LXIX acknowledging Red Beard's own retrospective reference to "
            "Aethelgard's death at the Ceremony; an understated 'centuries before he "
            "existed' reworded to 'long ages before he existed' in Chronicle LXXIV; "
            "a non-existent MCD-016 citation removed from Chronicle CXIX; further "
            "Osric/Cobb mis-citations corrected across Chronicles CVI, CXII, CXVI, "
            "and CXIX (to MCD-1775/MCD-1773); a writers'-room 'first account in this "
            "strand' leak and a stray in-line '(Chronicle XLV)' citation fixed in "
            "Chronicle XCVI; a real-world-religious-term leak ('family Bible') fixed "
            "in Chronicle LXXXV; and a second real-world-religious-term leak "
            "('God') fixed in Chronicle LVIII. Deliberately NOT applied, left for "
            "Abad's own direct creative ruling: C1's larger ~190-year gap-framing "
            "question (only the per-entry age phrasing was mechanically reworded); "
            "C4's pre-existing MCD-138/MCD-1850 five-thousand-year tension (flagged, "
            "not resolved); C9 (an age-related creative call); E5 (the Karkosa "
            "Atlas-queue item); and E6 (whether to lock a specific Book-2 duration "
            "number)."
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
