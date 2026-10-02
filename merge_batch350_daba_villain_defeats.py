#!/usr/bin/env python3
"""Batch 350: lock Daba Chronicles LVII-LVIII (Harek Vondel's killing, Vex Thurlow's capture)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-10-02, no source document. Dramatizes the two "
    "Batch-312 villain defeats already queued to Daba's own Character Chronicle series in his "
    "profile doc (docs/lords-of-cian/character-profiles/daba.md): Harek Vondel's killing by 1804 "
    "(CC-147/MCD-1855) and Vex Thurlow's capture/handover (CC-153/MCD-1861)."
)

NEW_RULES = [
    {
        "id": "MCD-1878",
        "category": "daba-character-chronicle",
        "statement": (
            "Daba Chronicle LVII, \"The Correction That Announced Itself\" (full narrative text at "
            "docs/lords-of-cian/chronicles/daba-chronicle-lvii-the-correction-that-announced-itself.md), "
            "the fifty-seventh entry of Daba's own Character Chronicle series. Dramatizes Harek "
            "Vondel's killing by 1804 (CC-147/MCD-1855) for the first time: Vondel's own "
            "reputation-first 'advertise the correction before it arrives' tactic hands Kether's "
            "cell the advance notice and predictable approach route 1804's dispersed, "
            "doctrine-over-mass cells need to exploit him -- Rhyne Cadec collapses both ends of a "
            "defile along his detachment's own announced route, the same narrowing-into-a-bottleneck "
            "logic a much younger Kanja learned on a disused footbridge during his mentorship with "
            "Daba (MCD-1568, Daba Chronicle XVIII). Daba stays in his established post-mentorship "
            "role as architect, not operator -- present only at the planning stage, never at the "
            "ambush itself, consistent with his profile's standing note that no Chronicle in the "
            "corpus shows him personally endangered or tested in combat (Chronicle LII remains his "
            "only physical-threat entry). The kill stays deliberately unattributed to Kanja, any "
            "Alias, or 1804 by name, matching MCD-1569's 'never folded into... never publicly "
            "credited alongside' framing; the Directorate's own internal accounting lists it as an "
            "unsolved field loss. No new named characters; Kether and Rhyne Cadec both reused from "
            "the existing corpus. Abad's approval: 'lock it.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1879",
        "category": "daba-character-chronicle",
        "statement": (
            "Daba Chronicle LVIII, \"What the Debt Paper Led To\" (full narrative text at "
            "docs/lords-of-cian/chronicles/daba-chronicle-lviii-what-the-debt-paper-led-to.md), the "
            "fifty-eighth entry of Daba's own Character Chronicle series. Dramatizes Vex Thurlow's "
            "capture and handover by 1804 (CC-153/MCD-1861) for the first time: Orsk Dresk's cell, "
            "investigating an unrelated Weregildd recruiter working too close to 1804's own "
            "territory, traces the Writedown Compact's debt-paper trail back to Thurlow personally. "
            "Daba rules out both killing him (the Compact replaces an Assessor inside a season) and "
            "delivering him to the Trust (no institutional interest in prosecuting a man who ruins "
            "people too quietly to be their problem), and instead has Orsk's cell hand Thurlow -- "
            "alive, unharmed, stripped of every document his operation depended on -- to a rival "
            "criminal power already hostile to the Writedown Compact, exactly matching the source "
            "rule's own deliberately unglamorous, ambiguous resolution (1804's doctrine treats "
            "visible retribution as a liability, MCD-1567). No casualty, so no name is added to "
            "Daba's own tally, consistent with his established record-keeping habit (MCD-1610) of "
            "logging only deaths; the operation is instead filed under the corpus's own running "
            "category of things the doctrine answers only partway. No new named characters; Orsk "
            "Dresk and Kether both reused from the existing corpus. Abad's approval: 'lock it.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = (
    "Daba Chronicles LVII-LVIII locked, dramatizing the two Batch-312 pre-Book-1 villain defeats "
    "already queued to his series (Harek Vondel's killing, CC-147/MCD-1855; Vex Thurlow's "
    "capture, CC-153/MCD-1861). Both drafted and presented in full per the gate's own "
    "already-cleared status for Daba's series (wave 3 locked); no fresh Psychological "
    "Profile/Game Plan cycle was needed since both beats were already explicitly queued in his "
    "profile doc. The remaining seven Batch-312 villain defeats stay blocked: five need their "
    "track's own Character Chronicle Launch Protocol backfill (Bane, Crow King, Sovereign Ghost "
    "of the Great Sea, Blue-Collar Titan, Lauris), and two (Brakon Skevik, Ossa Drem, both "
    "reckoned by Red Beard) need a brand-new protagonist track launched from scratch -- Red Beard "
    "currently has no profile or gate at all. None of that work was attempted here. Abad's "
    "approval, quoted verbatim: 'lock it.'"
)


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    for rule in NEW_RULES:
        assert rule["id"] not in existing_ids, f"ID collision: {rule['id']}"
        ledger["rules"].append(rule)

    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append(
        {
            "batch": next_batch,
            "source": SOURCE,
            "rules_affected": len(NEW_RULES),
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = "2026-10-02"

    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    ids = [r["id"] for r in ledger["rules"]]
    dupes = len(ids) - len(set(ids))
    print(
        f"OK: {len(ledger['rules'])} total rules, {len(ledger['batches_completed'])} batches, "
        f"ledger_version {ledger['ledger_version']}, batch {next_batch}, "
        f"zero duplicate IDs: {dupes == 0}. New rules: {', '.join(r['id'] for r in NEW_RULES)}."
    )


if __name__ == "__main__":
    main()
