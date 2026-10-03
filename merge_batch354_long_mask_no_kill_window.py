import json, datetime
P = "canon-ledger.json"
d = json.load(open(P, encoding="utf-8"))
APPROVAL = "lock in the age 30 and 48 no killing."
SOURCE = "Original invention, chat-drafted 2026-10-03, no source document"
NEW_RULES = [
    {"id": "MCD-1882", "category": "World Mechanics", "status": "locked", "source": SOURCE,
     "statement": ("The Long Mask's no-kill window. From the Sovereign Pier (age 30, MCD-1880 -- the nine "
        "killed there are the last) until the opening of the Pirate Dawn (age ~48, MCD-250), Kanja kills no "
        "one by his own hand. Onyx's Dark Ledger (ARS-437) records no kill spike across the whole span. The "
        "era's operations (MCD-247 through MCD-249: the Unarmed Siege of Maw-3, the Crucible Market raid, the "
        "False Dragon's Wake, and the rest) stay bloodless by his hand, carried by forged pressure, Standing "
        "Order 44-B, and the 'legend is the weapon' doctrine. The window governs Kanja's own hand only; crew "
        "and Avatars sit outside it. It binds every track: no Alias, Character, Territory, or Kanja-version "
        "Chronicle may show him killing anyone between those ages, and any existing entry that does is "
        "reconciled to non-lethal, crew-performed, or re-dated action. Extends CC-161 and MCD-1881. "
        "Abad's approval: 'lock in the age 30 and 48 no killing.'")},
]
ids = {r["id"] for r in d["rules"]}
for r in NEW_RULES:
    assert r["id"] not in ids, r["id"]
    d["rules"].append(r)
nb = max(b["batch"] for b in d["batches_completed"]) + 1
d["batches_completed"].append({"batch": nb,
    "source": SOURCE,
    "rules_affected": len(NEW_RULES),
    "note": "MCD-1882: Kanja kills no one by his own hand between the Sovereign Pier (age 30) and the opening of the Pirate Dawn (age ~48). Abad's approval: \"" + APPROVAL + "\""})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]
print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
