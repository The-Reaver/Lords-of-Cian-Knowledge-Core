#!/usr/bin/env python3
"""Batch 317: Ezio Valcari / Lady Nadea Thren Book 1 reconciliation beat.

Resolved during Ezio Valcari's Character Chronicle gate (Step 2,
Psychological Profile), where CC-073's ambiguity about whether Ezio knows
of Nadea's feelings was flagged as a live discussion point. Abad's
direction: "lets go with what makes the story more rich and stays true
to Ezio's character" -- delegating the creative call. Drafted and
presented in full; Abad's approval: "lock it."
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = (
    "Original invention, chat-drafted 2026-09-30, resolving a flagged "
    "ambiguity in CC-073 surfaced during Ezio Valcari's Character "
    "Chronicle gate (Step 2, Psychological Profile)."
)

with open(LEDGER_PATH, "r", encoding="utf-8") as f:
    ledger = json.load(f)

existing_ids = {r["id"] for r in ledger["rules"]}

# --- Amend CC-073 in place ---
CC073_NEW_STATEMENT = (
    "Lady Nadea Thren is Ezio Valcari's patron and is genuinely, secretly "
    "in love with him; Ezio figured out years ago both that she is 'the "
    "Viper' and that she loves him, and has chosen, deliberately and "
    "repeatedly, to say nothing and stay anyway -- restraint, not "
    "obliviousness."
)
amended = False
for r in ledger["rules"]:
    if r["id"] == "CC-073":
        r["statement"] = CC073_NEW_STATEMENT
        amended = True
        break
assert amended, "CC-073 not found -- aborting"

# --- New rule ---
NEW_RULES = [
    {
        "id": "MCD-1875",
        "category": "book1-structure",
        "statement": (
            "Extends MCD-070/CC-073 (amended same batch): during Book 1's "
            "climax (the Karkosa Heist act), Lady Nadea Thren steps out of "
            "patron-at-a-distance into direct field collaboration with "
            "Ezio at genuine personal risk -- a real cost for a defector "
            "whose own departure already dissolved the Mirrored Chorus "
            "(MCD-021). In the midst of it, Ezio breaks his own lifelong "
            "pattern of managed information for the first and only time "
            "on the page: he tells her plainly that he has always known "
            "she loves him. Not a declaration or a resolution -- a single "
            "act of chosen, deliberate vulnerability from a man whose "
            "defining burden is deception (CC-134), offered to the one "
            "person he's spent years protecting by saying nothing. What "
            "becomes of it afterward is deliberately left open, matching "
            "the project's own precedent for flexible book-level framing "
            "(MCD-216) -- this locks the character beat and its "
            "structural placement, not a specified romantic outcome."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

new_ids = [r["id"] for r in NEW_RULES]
assert len(new_ids) == len(set(new_ids)), "duplicate IDs within the new-rules batch"
collisions = existing_ids & set(new_ids)
assert not collisions, f"ID collision with live ledger: {collisions}"

ledger["rules"].extend(NEW_RULES)

batch_note = (
    "Resolved a flagged ambiguity in CC-073 (whether Ezio already knows of "
    "Nadea Thren's feelings) surfaced during Ezio's Character Chronicle "
    "gate, Step 2 (Psychological Profile). Presented as a genuine open "
    "question with two readings -- a long-held mutual tension finally "
    "acted on, versus a first-time revelation -- plus a shape question "
    "(operational/trust reconciliation vs. a tidy romantic resolution). "
    "Abad delegated the creative call: \"lets go with what makes the "
    "story more rich and stays true to Ezio's character.\" Ruled in favor "
    "of the richer, more character-consistent reading: Ezio already "
    "knows (a man this perceptive, this good at reading what people "
    "don't say, missing something this basic for years would undercut "
    "him), and the Book 1 climax reconciliation is a single act of "
    "chosen vulnerability rather than a grand declaration -- operational "
    "collaboration carrying the emotional weight, understated rather "
    "than resolved, matching Ezio's own noir narration register (VB-023) "
    "and his defining 'carries deception' throughline (CC-134). CC-073 "
    "amended in place to close the ambiguity; MCD-1875 locks the Book 1 "
    "climax beat itself, deliberately leaving the romantic outcome "
    "unspecified per the project's own MCD-216 precedent for flexible "
    "book-level framing. Presented in full; Abad's approval, quoted "
    "verbatim: \"lock it.\""
)
ledger["batches_completed"].append(
    {
        "batch": 317,
        "date": str(date.today()),
        "source": "Original invention (Ezio/Nadea Book 1 reconciliation beat)",
        "rule_count": len(NEW_RULES),
        "note": batch_note,
    }
)

ledger["ledger_version"] = f"{round(float(ledger['ledger_version']) + 0.1, 1):.1f}"
ledger["last_updated"] = str(date.today())

with open(LEDGER_PATH, "w", encoding="utf-8") as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
      f"Batches: {len(ledger['batches_completed'])}.")
