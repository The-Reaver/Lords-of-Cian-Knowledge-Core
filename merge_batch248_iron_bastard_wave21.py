#!/usr/bin/env python3
"""Batch 248: Iron Bastard Alias Chronicle wave 21 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Iron Bastard Alias Chronicle wave 21 (LXI-LXIII): a thermal/fire-expansion resonance combat "
    "showcase (the doctrine's first read against a continuously changing signature, extending doubled "
    "verification, MCD-497, into rate-of-change tracking), a genuine new limit where a fully correct, "
    "doubled-verified read still causes unintended harm via an unrecognized shared footing (a second "
    "awareness check added to the protocol), and an institutional/economic entry where the Ferrowright "
    "Consortium's exclusive-licensing offer is refused in favor of the doctrine's established free-"
    "teaching principle, with crew ledger-keeper Garren Hask (CC-115) in a supporting role. Zero new "
    "named characters; the Ferrowright Consortium collision-checked clean. Abad's approval: \"another "
    "alias wave of all aliases\"."
)

NEW_RULES = [
    {
        "id": "MCD-1080",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fire That Changed What the Iron Said\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fire-that-changed-what-the-iron-said.md), the Iron Bastard "
            "Alias Chronicle LXI, wave 21, first entry. A detailed full-Trinity combat showcase freeing "
            "caged prisoners from a deliberately fired granary at Vell's Landing: heat-driven thermal "
            "expansion changes the iron cages' resonance signature continuously as the fire burns, "
            "forcing Kanja to extend the standing doubled-verification protocol (MCD-497) from confirming "
            "a static tension into tracking its rate of change and projecting forward to the moment the "
            "locks fail on their own. Obsidian Malice discharges in three short pulses walked down the "
            "cage row rather than one sustained broadcast, Mafesto's Kinetic Transfer System redirects a "
            "roof collapse as leverage rather than absorbing it passively, and Onyx's Cadence Ruin clears "
            "a falling beam from the escape path. Nineteen of twenty prisoners escape; Kanja carries the "
            "twentieth out himself. Efa Gol (CC-130) runs a diversion; the second student (MCD-719) "
            "observes. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1081",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Wall He Saved That Broke Another\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-wall-he-saved-that-broke-another.md), the Iron Bastard "
            "Alias Chronicle LXII, wave 21. A genuine new limit of the doctrine: at Sennow Crossing, a "
            "retaining wall Kanja reads and collapses correctly, confirmed by doubled verification (MCD-"
            "497) both times, shares a century-old buried footing with a footbridge forty yards downslope "
            "that neither the wall's target readout nor any prior protocol flagged; removing the wall's "
            "load shifts the footing and the bridge collapses eleven seconds later, killing one of three "
            "washerwomen crossing it. The second student (MCD-719) traces the shared footing over two "
            "days of survey work. Kanja adds a second question to the doctrine's standing practice before "
            "any future discharge -- not whether the read is true, but whether the target structure is "
            "genuinely alone -- a doctrinal refinement distinct from wave 21's other refinement (MCD-1080) "
            "and distinct from the earlier fatal-misdiagnosis arc (MCD-497/727/728), since this read was "
            "correct throughout. Tam Sullen (CC-131) is referenced, not restaged. No new named characters; "
            "the washerwoman is deliberately left unnamed."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1082",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Guild That Wanted to Own the Sound\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-guild-that-wanted-to-own-the-sound.md), the Iron Bastard "
            "Alias Chronicle LXIII, wave 21, closing the wave. An institutional/economic entry: the "
            "Ferrowright Consortium, controlling inspection contracts across half the Sovereign Trust's "
            "shipping lanes, offers Kanja exclusive licensing, certification, and fee-sharing rights to "
            "the resonance doctrine, framed as safety-driven protection against careless use. Crew "
            "ledger-keeper Garren Hask (CC-115) reviews the contract and calls it fair money for something "
            "that isn't Kanja's to sell. Kanja hears out the safety argument in full before declining, "
            "refusing exclusivity in favor of the doctrine's already-established free teaching lineage "
            "(MCD-499, MCD-719, MCD-967, MCD-1048) as its own accountability structure, distinct from a "
            "licensing board answerable to shareholders. The Consortium withdraws the offer and later "
            "hires doctrine-trained engineers at ordinary market wages instead. A new institutional-"
            "pressure register for the doctrine, distinct from political suppression (MCD-730), a "
            "shelved report (MCD-421), and curriculum adoption without Kanja present (MCD-723). No new "
            "named characters; the Ferrowright Consortium collision-checked clean. Closes the Iron "
            "Bastard's twenty-first three-Chronicle wave (with MCD-1080 and MCD-1081)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 3, f"expected 3 new rules, got {len(NEW_RULES)}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 248,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-11, no source document",
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
