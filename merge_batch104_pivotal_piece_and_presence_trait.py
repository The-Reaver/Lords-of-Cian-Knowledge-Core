#!/usr/bin/env python3
"""Batch 104: Lock "The Pivotal Piece" (MCD-365) and the new standing Voice Bible trait it
puts on the page for the first time -- the "Already-Finished Negotiation" presence effect
(VB-060), which Abad wants to recur across the whole series whenever a POV character shares a
scene with Kanja, under any alias, at a moment of consequence."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-10, no source document. Full narrative text at "
    "docs/lords-of-cian/chronicles/the-pivotal-piece.md."
)

BATCH_NOTE = (
    'Abad: "lock it. I love the description of someone describing how they felt and his '
    'presence I\'m referring to Bane. it is something that should live out through the series '
    'everyone feels that when in this presence. it was a great description of someone '
    'negotiating in a room they weren\'t in and just informing them now of what the results '
    'was brilliant writing"'
)

NEW_RULES = [
    {
        "id": "MCD-365",
        "category": "kanja-chronicle",
        "statement": (
            "\"The Pivotal Piece\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-pivotal-piece.md), a standalone Kanja-era scene, "
            "not a territory Chronicle. Rebellion era, age 19, the night after the Battle of the "
            "Black Trench (MCD-232), under the \"Bane\" alias -- the Directorate's own "
            "classification for a threat that destroys the force built to destroy it (MCD-232). "
            "An unnamed senior Sovereign Trust Undersecretary comes to the sealed ravine under "
            "parley, offering Bane a House seat, a new name, and protection in exchange for "
            "standing down, on behalf of \"the people who actually hold the ledgers this world "
            "runs on.\" Bane, without standing or raising his voice, delivers the line \"I am the "
            "pivotal piece to the scheme of all things. Not the Trust's scheme. Not yours... You "
            "can't buy a piece that was never on your board\" -- a declaration that he answers to "
            "something outside the Trust's frame entirely, not a boast or a threat the "
            "Undersecretary can report as one. The scene is the first on-page dramatization of "
            "the \"Already-Finished Negotiation\" standing presence trait (VB-060). The closing "
            "paragraph plants a deliberate, unscripted forward link to the line's later fame under "
            "the Scourge/pirate-era persona (ages 48-52) -- legend's own drift across aliases, not "
            "a scripted callback. No new named characters; the Undersecretary is unnamed and "
            "one-scene."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "VB-060",
        "category": "voice-bible-presence",
        "statement": (
            "Kanja's presence, under any alias and in any era, carries a standing characterization "
            "signature: people who share a scene with him at a moment of real consequence do not "
            "experience him as someone deciding, weighing, or negotiating in real time. They "
            "experience the specific, unsettling sense that he already reached his conclusion "
            "somewhere they were not invited to, and is only now, in this room, informing them of "
            "the result. This is a character trait, not a supernatural power -- a quality of "
            "already-settled certainty, delivered without volume, threat, or performance, that "
            "reads to anyone still operating in negotiation mode as something closer to terror "
            "than confrontation. First put on the page in \"The Pivotal Piece\" (MCD-365), via the "
            "unnamed Undersecretary's reaction to Bane: he came prepared with three rehearsed "
            "responses to theatrical refusal and none of them applied, because nothing he heard "
            "was a refusal being negotiated in front of him -- it was a result being reported. This "
            "trait is intended to recur across the series whenever a POV character meets Kanja, "
            "under whichever alias fits the era (Bane, the Scourge, and others still undramatized), "
            "at a scene of genuine stakes -- an early, personal-scale precursor to the "
            "already-locked \"legend is the weapon\" doctrine (established in-story at the False "
            "Dragon's Wake, age 35), which operates at institutional/reputational scale where this "
            "trait operates at the scale of a single room."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collisions with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 104,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-10, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks \"The Pivotal Piece\" (MCD-365), the standalone Kanja-era Chronicle "
                "embedding the corrected Bane quote, and a new standing Voice Bible rule "
                "(VB-060) capturing the presence trait Abad specifically flagged: Kanja, under "
                "any alias, reads to those around him at moments of consequence not as someone "
                "negotiating but as someone reporting a result already decided elsewhere -- "
                "intended to recur across the whole series, not a one-scene device. " + BATCH_NOTE
            ),
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate IDs after merge"
    print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
          f"Batches: {len(ledger['batches_completed'])}.")


if __name__ == "__main__":
    main()
