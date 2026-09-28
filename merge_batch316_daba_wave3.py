#!/usr/bin/env python3
"""Batch 316: Daba's third Character Chronicle wave (Chronicles LIV-LVI),
per Abad's direction: "do the third Daba wave," then "lock it" on the
presented full text.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = (
    "Original invention, chat-drafted 2026-09-28, extending Daba's own "
    "50+3-Chronicle corpus (Batches 296, 315) and his gate profile "
    "(docs/lords-of-cian/character-profiles/daba.md)."
)

with open(LEDGER_PATH, "r", encoding="utf-8") as f:
    ledger = json.load(f)

existing_ids = {r["id"] for r in ledger["rules"]}

NEW_RULES = [
    {
        "id": "MCD-1872",
        "category": "daba-character-chronicle",
        "statement": (
            "Daba Chronicle LIV, 'The Window That Faced the Water' (full text at "
            "docs/lords-of-cian/chronicles/daba-chronicle-liv-the-window-that-faced-the-water.md). "
            "First entry of Daba's third Character Chronicle wave, paying off Chronicle LIII's "
            "closing line without fully resolving the larger open question of what he wants for "
            "himself. On a day the ledger holds no new name, Daba travels to Mika's coastal "
            "house and stays a full day -- his first real, concrete acknowledgment that "
            "something in his life can exist without a function or a debt attached to it. He "
            "leaves without promising a schedule for returning, but for the first time does not "
            "need the door held open for him -- he understands he can walk through it again. "
            "Whether this becomes a habit, or ever competes seriously with the network's claims "
            "on him, stays open. No new named characters; reuses Mika."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1873",
        "category": "daba-character-chronicle",
        "statement": (
            "Daba Chronicle LV, 'The Name Daba Never Spoke' (full text at "
            "docs/lords-of-cian/chronicles/daba-chronicle-lv-the-name-daba-never-spoke.md). "
            "Second entry of the wave. Prompted directly by his own near-death at Threnfall "
            "(MCD-1870), Daba confronts a structural gap he had never applied to himself: "
            "1804's blind-succession doctrine (locked at MCD-1597, Yeva Tolan/Marn) protects "
            "every cell's leadership against capture or loss except his own. Over three weeks he "
            "extends the same structure to the network's own top for the first time, choosing "
            "Kether as his unwitting successor through the identical method used elsewhere -- "
            "small, unexplained authority handed over on ordinary days, culminating in giving "
            "her unsupervised access to the annual list's back room. Kether does not learn she "
            "has been chosen, and does not learn the true margin of Threnfall's danger either, "
            "matching the doctrine's own stated logic (a second who watches her leader for signs "
            "of the next near-miss is already half doing the job before she's needed). Reuses "
            "Kether, Bren, and Wrenna. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1874",
        "category": "daba-character-chronicle",
        "statement": (
            "Daba Chronicle LVI, 'What Vetting Cannot See' (full text at "
            "docs/lords-of-cian/chronicles/daba-chronicle-lvi-what-vetting-cannot-see.md). "
            "Third entry of the wave, closing it -- the corpus's first genuine doctrine-limit "
            "entry for the vetting mechanism itself. Sarel Doune, a courier who passed 1804's "
            "full year-long vetting faithfully and shows no malice or carelessness, mentions a "
            "safehouse's approximate location to her own sister in an ordinary, loving family "
            "conversation; the fragment travels through two further unrelated conversations "
            "before landing, by pure administrative bad luck, unread in the wrong Trust district "
            "and causing no actual harm. Tracing the chain, Daba concludes the vetting doctrine "
            "(MCD-1567) has a real, permanent hole it cannot close -- it tests for resistance "
            "under deliberate pressure but has no method for a person's ordinary, ungovernable "
            "love for someone never vetted at all, and closing that hole would mean punishing "
            "the exact quality that makes a person trustworthy in the first place. He does not "
            "tell Sarel, judging that the fear it would create would cost more than the risk "
            "itself, and files the fact as a permanently unresolved, unaudited cost of the "
            "network's own safety rather than a problem to be solved. New named character Sarel "
            "Doune, collision-checked clean. Reuses Kether. No new other named characters; no "
            "child-safety issues."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

new_ids = [r["id"] for r in NEW_RULES]
assert len(new_ids) == 3
assert len(set(new_ids)) == len(new_ids), "duplicate IDs within the new-rules batch"
collisions = existing_ids & set(new_ids)
assert not collisions, f"ID collision with live ledger: {collisions}"

ledger["rules"].extend(NEW_RULES)

batch_note = (
    "Daba's third Character Chronicle wave, per Abad's direction: 'do the third Daba wave,' then "
    "'lock it' on the full presented text. No fresh candidate-pick cycle was run for this wave -- "
    "matching established project precedent for continuing an already-approved series (e.g. the "
    "Ozmund and Alias Chronicle multi-wave runs) -- new registers were chosen directly: paying off "
    "Chronicle LIII's house/Mika thread with real forward motion (LIV); extending the blind-"
    "succession doctrine to Daba's own position for the first time, prompted by his own near-death "
    "at Threnfall (LV, naming Kether as his unwitting successor); and the corpus's first honest, "
    "non-malicious vetting failure, exposing a genuine, permanent limit of the doctrine itself "
    "rather than a fixable gap (LVI). One new named character (Sarel Doune, collision-checked "
    "clean against the full live ledger before drafting). Daba's Character Chronicle series now "
    "stands at 56 total entries across three waves plus the original 50-entry launch."
)
ledger["batches_completed"].append(
    {
        "batch": 316,
        "date": str(date.today()),
        "source": "Original invention (Daba Character Chronicle third wave)",
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
