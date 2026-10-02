#!/usr/bin/env python3
"""Batch 353: lock the Heartline and the Dark Ledger (ARS-437)."""
import json

LEDGER_PATH = "canon-ledger.json"
APPROVAL = "Both Heartline / Dark Ledger. keep all three, lock it"
SOURCE = ("Original invention, chat-drafted 2026-10-02, no source document. Formalizes Abad's "
          "statement that Onyx is biologically tethered to Kanja, extending ARS-020, MCD-201, "
          "CC-012, CC-013, MCD-246, and VB-062.")

RULE = {
    "id": "ARS-437",
    "category": "trinity-relic",
    "statement": (
        "The Heartline. Onyx of Oblivion's bond to Kanja (ARS-020, bonded at seventeen) is "
        "biological, not mere attunement: at bonding, the blade's Living Drakma lattice keyed itself "
        "to his blood, pulse, and nervous system. The Heartline is why Onyx feels Kanja at any "
        "distance, though it speaks only through whoever holds its grip (MCD-201). Across distance it "
        "runs one way -- Onyx receives, Kanja does not -- and carries the body only: heartbeat, "
        "strain and exhaustion, wounds and illness, sleep, the specific spike of a kill, and density "
        "surges, which Onyx records but never names (VB-021). It never carries words, sights, places, "
        "or thoughts; full exchange happens only through the grip. The Heartline does not break when "
        "Onyx is sealed at L9, the Silent Infinite (CC-012); it holds for the entire 284-year Long "
        "Mask. In the dark, Onyx keeps the Dark Ledger, a section of the Black Ledger (CC-013) unlike "
        "the rest of it: the Black Ledger records what the blade witnesses, the Dark Ledger only what "
        "it felt -- signals logged against its running seconds-count (MCD-246), with no causes "
        "attached. When the Karkosa Heist returns Onyx to Kanja's hand in Book 1 (MCD-070, ARS-010), "
        "grip contact restores the full channel: Onyx reads 284 years out of his body (scars, changed "
        "muscle memory, accumulated strain) and reconciles every Dark Ledger entry against what "
        "actually happened -- the mechanism behind VB-062's retrospective Long Mask accounts, each of "
        "which can open on a Dark Ledger entry before revealing its cause. Limits: through the "
        "Heartline, Onyx cannot locate Kanja, warn him, or act; it can only feel and record. Kanja "
        "does not know the bond survived the sealing until the reunion. Reserved: Maro Rexmar's death "
        "at the Fulfillment Ceremony happens while Onyx is still sealed and reaches the blade through "
        "the Heartline as a signal with no cause; this beat belongs to Book 1 and must not be drafted, "
        "foreshadowed, or referenced in any pre-Book-1 material. Abad's approval: '" + APPROVAL + "'"
    ),
    "status": "locked",
    "source": SOURCE,
}


def main():
    with open(LEDGER_PATH, encoding="utf-8") as f:
        ledger = json.load(f)
    assert RULE["id"] not in {r["id"] for r in ledger["rules"]}
    ledger["rules"].append(RULE)
    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({
        "batch": next_batch, "source": SOURCE, "rules_affected": 1,
        "note": ("Locks the Heartline (Onyx's biological bond to Kanja) and the Dark Ledger (its "
                 "record of felt-but-unwitnessed signals during the sealed Long Mask), as the source "
                 "mechanism for VB-062's retrospective Long Mask accounts. All three flagged choices "
                 "kept: the names, Kanja not knowing until the reunion, and the reserved Book-1 beat "
                 "of Maro's death arriving through the Heartline. Abad's approval, quoted verbatim: '"
                 + APPROVAL + "'"),
    })
    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = "2026-10-02"
    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")
    ids = [r["id"] for r in ledger["rules"]]
    print(f"OK: {len(ids)} rules, batch {next_batch}, ledger_version {ledger['ledger_version']}, "
          f"zero duplicate IDs: {len(ids) == len(set(ids))}")


if __name__ == "__main__":
    main()
