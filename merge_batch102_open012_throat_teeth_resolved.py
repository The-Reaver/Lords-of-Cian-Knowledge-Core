#!/usr/bin/env python3
"""Batch 102: Amend OPEN-012 -- the Throat/Teeth half is resolved (stale cross-reference,
not a real gap), leaving only the RA/UK map codes genuinely open."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

BATCH_NOTE = 'Abad: "lock it."'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    found = False
    for o in ledger["open_decisions"]:
        if o.get("id") == "OPEN-012":
            found = True
            o["statement"] = (
                "What do the undefined map codes RA (10 cells, clustered in Lawless Reaches) "
                "and UK (5 cells, tied to a road named 'UK Spur') represent?"
            )
            o["note"] = (
                "The live Regional Atlas sheet contains these unresolved artifacts (see "
                "research/atlas-live-sheet-audit.md) with no defining legend entry anywhere. "
                "Abad does not currently recall their intended meaning, per his answer "
                "2026-09-06 ('I have forgotten'). Deferred -- possibly resolvable by reviewing "
                "the live Sheet's native UI (cell coloring/shapes the text export can't "
                "capture) or by fresh invention later. The Throat/Teeth half of this question, "
                "originally bundled in here, is resolved as of 2026-09-10 -- not a genuine gap, "
                "a stale cross-reference: MAW-060 and MAW-061 (sourced from "
                "Maw_Codex_Definitive_Edition.docx, extracted in a session predating this "
                "session's tracked batch log) already place them. The Throat is the Grand Maw "
                "of Karkosa, in Central Karkosa, the Sovereign Trust Domain's capital already "
                "locked on the Atlas at GEO-003. The Teeth is the Frontier Maw (Maw-12, "
                "'the Edge'), on the border between the Sovereign Trust's territory and the "
                "Shattered Kingdoms. Reconfirmed against a newer edition of the same source "
                "document (Maw_Codex_Definitive_Edition_3.docx, Abad-uploaded 2026-09-10), which "
                "contains no new facts on this point. " + BATCH_NOTE
            )
            break
    assert found, "OPEN-012 not found in open_decisions"

    ledger["batches_completed"].append(
        {
            "batch": 102,
            "date": str(date.today()),
            "source": (
                "Maw_Codex_Definitive_Edition_3.docx (Abad-uploaded 2026-09-10), reconciled "
                "against already-locked MAW-060/MAW-061/GEO-001/GEO-003"
            ),
            "rule_count": 0,
            "note": (
                "OPEN-012 amended: the Throat/Teeth half of the question is resolved as a "
                "stale cross-reference (MAW-060/061 already locate them), not a genuine gap; "
                "only the RA/UK map codes remain open. No new rules -- an open_decisions "
                "correction only. " + BATCH_NOTE
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
