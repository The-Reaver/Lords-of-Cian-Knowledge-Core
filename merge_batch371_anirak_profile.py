"""Batch 371: Anirak's Psychological Profile recommendations locked (CC-163, CC-164),
plus amendments to MCD-251, ARS-440 and ARS-441 (Foreclosure)."""
import json, re
from collections import Counter

LEDGER = "canon-ledger.json"
DRAFT = "docs/lords-of-cian/drafts/2026-10-03-anirak-profile-rules.md"
SOURCE = ("Anirak Psychological Profile (docs/lords-of-cian/character-profiles/anirak.md, Section 2), "
          "recommendations approved 2026-10-03; rule text at " + DRAFT)
APPROVAL = "Abad's approval: 'approved' / 'lock it.'"

d = json.load(open(LEDGER, encoding="utf-8"))
ids = {r["id"] for r in d["rules"]}
t = open(DRAFT, encoding="utf-8").read()

def para(rid):
    m = re.search(r"\*\*" + rid + r" \(new, character-crew\)\.\*\* (.*?)\n\n", t, re.S)
    s = " ".join(m.group(1).split()).replace("`", "")
    return s

for rid in ("CC-163", "CC-164"):
    assert rid not in ids, rid
    d["rules"].append({"id": rid, "category": "character-crew",
                       "statement": para(rid) + " " + APPROVAL,
                       "status": "locked", "source": SOURCE})

amend = {
    "MCD-251": ("Establishes her four-person unit as the first sub-crew loyal to a lieutenant rather than to Kanja directly",
                "Establishes her four-person unit (Anirak leading Edda, Hamund, and Odile, MCD-1890), whose three are the first sub-crew loyal to a lieutenant rather than to Kanja directly"),
    "ARS-440": ("She was Maw-raised (MCD-251) and sold out of the circuit (MCD-1883) by a circuit that priced its fighters' freedom at a ratio set above any ordinary career's return (MAW-079), and she turned its vocabulary into a fighting style. Every combination below that pulls is a form of Debt Collection.",
                "She was sold into the Maw circuit at twelve against a debt (CC-163), Maw-raised (MCD-251), and sold out of the circuit (MCD-1883). That circuit priced her freedom against the debt, the same system that sets the Cestari manumission ratio above any ordinary career's return (MAW-079), and she turned its vocabulary into a fighting style. Every pulling combination in the Codex (ARS-441 through ARS-447) is a form of Debt Collection."),
    "ARS-441": ("clears everyone the Voice has dropped within her reach",
                "strips the weapons from everyone the Voice has dropped within her reach and is lethal only to those who keep coming (CC-164)"),
}
R = {r["id"]: r for r in d["rules"]}
old2, new2 = ("with the undersea and partner combinations below", "with the undersea and partner combinations (ARS-445, ARS-446)")
assert R["ARS-441"]["statement"].count(old2) == 1
R["ARS-441"]["statement"] = R["ARS-441"]["statement"].replace(old2, new2)
for rid, (old, new) in amend.items():
    assert R[rid]["statement"].count(old) == 1, rid
    R[rid]["statement"] = R[rid]["statement"].replace(old, new)

nb = max(b["batch"] for b in d["batches_completed"]) + 1
d["batches_completed"].append({
    "batch": nb, "source": SOURCE, "rules_affected": 5,
    "note": ("Anirak's Psychological Profile closed: CC-163 (origin -- pressure-born, sold into the Maw "
             "circuit at twelve against a debt, never Cestari; her Chain Harbor unit is Anirak leading "
             "Edda, Hamund, and Odile) and CC-164 (her necessity-kill register from the fleet's "
             "arrival at Chain Harbor onward, with the Flood State clause carried by Ren). MCD-251, ARS-440 and ARS-441 "
             "amended to match. The Batch 365 log's pending 'CC-163' is the Nadea Thren proposal, "
             "renumbered CC-165. Passed the Connective-Tissue Gate after five independent reviews. "
             "Abad's approval, verbatim: 'approved' / 'lock it.'")})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-03"
json.dump(d, open(LEDGER, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(LEDGER, "a", encoding="utf-8").write("\n")
c = Counter(r["id"] for r in d["rules"])
print("batch", nb, "version", d["ledger_version"], "rules", len(d["rules"]),
      "duplicates", [k for k, v in c.items() if v > 1])
