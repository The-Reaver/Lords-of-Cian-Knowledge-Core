import json
P = "canon-ledger.json"
APPROVAL = "anything that needs correction is mandated to be corrected everything has to make sense"
SOURCE = "Crew/track reconciliation of locked rules against each other (MCD-155/160/1555, MCD-294/295, MCD-951, ARS-382/383, MCD-1635, MCD-1462, MCD-1465); chat-drafted 2026-10-03, no new source document"
d = json.load(open(P, encoding="utf-8"))
R = {r["id"]: r for r in d["rules"]}
nb = max(b["batch"] for b in d["batches_completed"]) + 1
touched = set()

def amend(rid, old, new):
    s = R[rid]["statement"]
    assert s.count(old) == 1, (rid, old, s.count(old))
    R[rid]["statement"] = s.replace(old, new)
    touched.add(rid)

# Item 3: Ilvane is a Threnarr daughter-hold, not a 13th Vask
amend("MCD-1635", "A small, terminally failing Vask, Ilvane (new named location,",
      "A small, terminally failing daughter-hold, Ilvane -- a sister-settlement founded from Threnarr some nine thousand years earlier, never one of the forty Vasks or the twelve survivors (MCD-155/160) (new named location,")

# Item 5: Book-2 Moonvault gifts not used pre-Book-1 in the Sovereign Ghost track
amend("MCD-1462", "A new-gear register: the first dramatized use of the Lodestone Lens (`ARS-382`) for this alias, reading a shifting seafloor hazard",
      "A senses register: Kanja's own unaided Rex/Mar senses (MCD-294/295) reading a shifting seafloor hazard")
amend("MCD-1462", "Corrected Batch 348, 2026-10-02:",
      "Corrected (prose, Batch 327): the Lodestone Lens (ARS-382) is a Book-2-onward Moonvault gift and does not appear. Corrected Batch 348, 2026-10-02:")
amend("MCD-1465", "The first dramatized use of the Whalebone Tether (`ARS-383`) for this alias, redirecting",
      "Ordinary hawser-and-boat work, redirecting")
amend("MCD-1465", "-- deliberately distinct from Undertow's own first dramatized use (`MCD-951`), which drags a hostile Titan-scale creature under,",
      "-- deliberately distinct from MCD-951, where a hostile Titan-scale creature is driven off with Kanja's Mar tide-sense and anchor-chain work,")
amend("MCD-1465", "Closes wave 33 (`MCD-1463` through `MCD-1465`).",
      "Closes wave 33 (`MCD-1463` through `MCD-1465`). Corrected (prose, Batch 327): the Whalebone Tether (ARS-383) and Undertow are Book-2-onward Moonvault gifts and do not appear.")

d["batches_completed"].append({"batch": nb, "source": SOURCE, "rules_affected": len(touched),
  "note": "Mechanical crew/track reconciliations under Abad's connective-tissue mandate (\"" + APPROVAL + "\"), no new facts: MCD-1635 reframes Ilvane as a Threnarr daughter-hold rather than a 13th Vask (matching MCD-155/160's twelve survivors and the Chronicle's own sister-settlement prose); MCD-1462 and MCD-1465 no longer claim first dramatized uses of the Lodestone Lens and Whalebone Tether, which Batch 321 already removed from the prose as Book-2-onward Moonvault gifts; companion file fixes: Ilvane wording (Lauris XVIII, XXI, profile), Xaragua Chronicle III's dock-boy cohort set to five with three dead, Ozmund Chronicle XII's unsourced 'three days' removed, the Storm That Walks MCD-1358 notes citation corrected, and alias-captain.md no longer counts MCD-1486's Crow King fourth generation as Hask's descendants. Items needing new rulings (Hask mortality, Lauris dockside/Ozmund placement, Vael gender, Ironbane, Auberon custodian, Orin phonograph, Torvald, near-collision renames) deliberately left for Abad."})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]
print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
