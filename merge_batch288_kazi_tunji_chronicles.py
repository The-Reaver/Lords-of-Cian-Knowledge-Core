#!/usr/bin/env python3
"""Batch 288: Kazi Chronicles IV-VIII, Tunji's five-entry run (MCD-1523 through MCD-1527)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-12, no source document."

BATCH_NOTE = (
    "Five new Kazi (Detroit) territory Chronicles spotlighting Tunji (PH2-065) as protagonist, per "
    'Abad\'s direct authorization: "give them five Chronicles each" (referring to Tunji and Femi, '
    "the two new supporting-cast characters locked at PH2-065/PH2-066 in Batch 287). Drafted in "
    "parallel with a sibling agent's five Femi Chronicles under the same authorization -- disjoint "
    "MCD-ID range and file set, no shared files touched. Each entry explores a genuinely distinct "
    "register rather than repeating a prior beat: Kazi Chronicle IV, \"The List He Kept Before "
    "Anyone Asked\" (MCD-1523), dramatizes Tunji's patient recruitment/vetting method directly for "
    "the first time, months before any crisis, introducing Zola as a new recruit tested specifically "
    "under cost rather than ease. Kazi Chronicle V, \"What He Read Wrong\" (MCD-1524), is a genuine "
    "failure entry: Tunji misjudges a grievance as premature, workers walk out ahead of his "
    "groundwork, and a fast read made under pressure nearly costs the effort a wavering recruit, "
    "Torvald, before Zola's earlier vetting saves it. Kazi Chronicle VI, \"The Names He Was Teaching "
    "to Read the Floor\" (MCD-1525), is a mentorship entry: Tunji trains Bakari (already locked, "
    "MCD-363) and Zola in his own method, honestly recounting Chronicle V's failure as part of the "
    "teaching. Kazi Chronicle VII, \"What the Floor Never Let Him Set Down\" (MCD-1526), is a "
    "quiet, crisis-free personal/domestic entry with his aunt Adaeze, establishing Tunji's origin "
    "(raised from age nine after his mother's death) and the personal cost of a method built on "
    "always reading a room first -- Kanja's presence is reduced to a single peripheral, wordless "
    "appearance, matching the precedent set by Sankofa Chronicle V (MCD-1025), which omitted him "
    "entirely for a comparably private scene. Kazi Chronicle VIII, \"The Man Who Wouldn't Say Why\" "
    "(MCD-1527), dramatizes internal factional distrust (Torvald's lingering suspicion that Tunji's "
    "ease with Kunle and Kalamu means divided loyalty) and the first direct on-page contrast between "
    "Tunji's shop-floor register and Kunle's/Kalamu's legal-and-press registers, extending Kazi "
    "Chronicle II's (MCD-363) 'different kind of power' theme into an internal-trust register. Every "
    "new proper noun (Zola, Juma, Torvald, Adaeze) was collision-checked against the full live "
    "ledger before drafting -- zero prior hits for any. Irin, Kunle, Kalamu, and Bakari are reused "
    "throughout rather than newly introduced, per established preference for continuity depth. An "
    "unnamed Kanja appears in every entry except Kazi Chronicle VII, where his presence is reduced "
    "to a single peripheral, wordless appearance rather than omitted outright, and never takes "
    "command, credit, or resolution authorship in any of the five. No child-safety concerns in any "
    "entry."
)

NEW_RULES = [
    {
        "id": "MCD-1523",
        "category": "territory-chronicle",
        "statement": (
            "Kazi Chronicle IV, \"The List He Kept Before Anyone Asked\" (full narrative text at "
            "docs/lords-of-cian/chronicles/kazi-chronicle-iv-the-list-he-kept-before-anyone-asked.md), "
            "the fourth Kazi territory Chronicle and the first with Tunji (PH2-065) as protagonist "
            "rather than Irin. Understood to predate Kazi Chronicle I (MCD-351). Dramatizes Tunji's "
            "signature role directly for the first time: months of patient, unannounced observation "
            "of a new hire, Zola, testing specifically for a repeatable pattern of unprompted "
            "solidarity under real cost (a docked hour reversed on behalf of strangers) rather than "
            "under easy conditions, before any approach is made or any organizing purpose is named. "
            "Zola is a new named character (Nguni/Swahili-adjacent, 'calm/quiet'), collision-checked "
            "against the full live ledger before drafting (zero prior hits), introduced for likely "
            "reuse in future Tunji entries. An unnamed Kanja is present, hired onto the same floor, "
            "covering Zola's station without credit or acknowledgment -- no command, no intervention, "
            "no resolution authorship. No contradiction with Kazi Chronicle I: Irin's own halt in "
            "that Chronicle presupposes exactly this kind of pre-existing readiness already being in "
            "place on the floor."
        ),
        "status": "locked",
        "source": (
            SOURCE
            + " Full narrative text at "
            "docs/lords-of-cian/chronicles/kazi-chronicle-iv-the-list-he-kept-before-anyone-asked.md."
        ),
    },
    {
        "id": "MCD-1524",
        "category": "territory-chronicle",
        "statement": (
            "Kazi Chronicle V, \"What He Read Wrong\" (full narrative text at "
            "docs/lords-of-cian/chronicles/kazi-chronicle-v-what-he-read-wrong.md), the fifth Kazi "
            "territory Chronicle, second with Tunji (PH2-065) as protagonist. A genuine failure/"
            "limits entry: Tunji misjudges a gantry-crew scaffolding grievance as premature for three "
            "weeks running, and a rigger, Juma, is injured before Tunji's usual groundwork is in "
            "place, forcing the crew to walk out with no vetted readiness under them. Tunji improvises "
            "a fast read under pressure at the gate -- explicitly shown to be a guess rather than a "
            "reliable substitute for his slow method -- and one of the two riggers he picks on the "
            "spot, Torvald, nearly folds and walks two others out with him before Zola (introduced "
            "Kazi Chronicle IV, MCD-1523), vetted properly months earlier, talks them back into the "
            "line. Establishes a real limit of Tunji's method: patient ripeness-reading can misjudge "
            "timing, and speed does not preserve its reliability. Torvald and Juma are new one-scene "
            "minor named characters, collision-checked against the full live ledger before drafting "
            "(zero prior hits for either). An unnamed Kanja is present, helping carry the injured "
            "rigger to a cart without taking credit, command, or resolution authorship."
        ),
        "status": "locked",
        "source": (
            SOURCE
            + " Full narrative text at "
            "docs/lords-of-cian/chronicles/kazi-chronicle-v-what-he-read-wrong.md."
        ),
    },
    {
        "id": "MCD-1525",
        "category": "territory-chronicle",
        "statement": (
            "Kazi Chronicle VI, \"The Names He Was Teaching to Read the Floor\" (full narrative text "
            "at docs/lords-of-cian/chronicles/"
            "kazi-chronicle-vi-the-names-he-was-teaching-to-read-the-floor.md), the sixth Kazi "
            "territory Chronicle, third with Tunji (PH2-065) as protagonist. A mentorship entry set "
            "after Bakari's already-locked trial (Kazi Chronicle II, MCD-363): Tunji trains Bakari and "
            "Zola (MCD-1523) in his own ripeness-reading method, walking the floor with them and "
            "honestly recounting his own Chronicle V (MCD-1524) failure as part of the teaching, "
            "without softening his role in it. Establishes the method's two-part diagnostic in "
            "explicit terms (what a person is capable of under strain, paired with what it visibly "
            "costs them to keep being that way) and its irreducible slowness. Closes on an unnamed "
            "Kanja, observed carrying trays unasked for three weeks running, deliberately left as an "
            "open thread Tunji has not yet approached -- present without command, credit, or "
            "resolution authorship. No new named characters."
        ),
        "status": "locked",
        "source": (
            SOURCE
            + " Full narrative text at docs/lords-of-cian/chronicles/"
            "kazi-chronicle-vi-the-names-he-was-teaching-to-read-the-floor.md."
        ),
    },
    {
        "id": "MCD-1526",
        "category": "territory-chronicle",
        "statement": (
            "Kazi Chronicle VII, \"What the Floor Never Let Him Set Down\" (full narrative text at "
            "docs/lords-of-cian/chronicles/"
            "kazi-chronicle-vii-what-the-floor-never-let-him-set-down.md), the seventh Kazi territory "
            "Chronicle, fourth with Tunji (PH2-065) as protagonist. A quiet, crisis-free personal/"
            "domestic entry establishing Tunji's origin -- raised by his aunt Adaeze from age nine "
            "after his mother's death, in a crowded household that shaped his reading-people instinct "
            "before the plant ever did -- and dramatizing the personal toll of a method built on "
            "always reading a room first, extending PH2-065 beyond the workplace for the first time. "
            "Adaeze is a new named character (Igbo, 'princess/first daughter'), collision-checked "
            "against the full live ledger before drafting (zero prior hits), minor and non-recurring "
            "unless a future Chronicle wants her. Kanja's presence is reduced to a single peripheral, "
            "wordless appearance (a neighbor's boy fixing a porch step nearby) rather than omitted "
            "outright, matching the minimal-presence register the sub-series has already established "
            "as acceptable for a comparably private scene (Sankofa Chronicle V, MCD-1025, omitted him "
            "entirely). No plot event requiring resolution; deliberately a character-depth breather."
        ),
        "status": "locked",
        "source": (
            SOURCE
            + " Full narrative text at docs/lords-of-cian/chronicles/"
            "kazi-chronicle-vii-what-the-floor-never-let-him-set-down.md."
        ),
    },
    {
        "id": "MCD-1527",
        "category": "territory-chronicle",
        "statement": (
            "Kazi Chronicle VIII, \"The Man Who Wouldn't Say Why\" (full narrative text at "
            "docs/lords-of-cian/chronicles/kazi-chronicle-viii-the-man-who-wouldnt-say-why.md), the "
            "eighth Kazi territory Chronicle, fifth with Tunji (PH2-065) as protagonist, closing this "
            "five-Chronicle run. An internal-factional-distrust entry: Torvald (introduced Kazi "
            "Chronicle V, MCD-1524) suspects Tunji's ease with Kunle (PH2-063) and Kalamu (PH2-064) "
            "means divided loyalty away from the shop floor. Tunji resolves it not through argument "
            "but by letting Torvald watch him decline a press request from Kalamu (delaying a true "
            "story two weeks so it lands as proof rather than pressure), the first direct on-page "
            "contrast between Tunji's shop-floor register and Kunle's/Kalamu's legal-and-press "
            "registers, extending Kazi Chronicle II's (MCD-363) 'different kind of power' theme into "
            "an internal-trust register. Trust is deliberately left only partially repaired, not fully "
            "resolved, consistent with Tunji's own stated view that real trust takes months on both "
            "sides. Zola (MCD-1523), Kunle, and Kalamu are reused; no new named characters. An unnamed "
            "Kanja is present, filling water jugs at the station without dialogue, command, credit, or "
            "resolution authorship."
        ),
        "status": "locked",
        "source": (
            SOURCE
            + " Full narrative text at docs/lords-of-cian/chronicles/"
            "kazi-chronicle-viii-the-man-who-wouldnt-say-why.md."
        ),
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
            "batch": 288,
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
