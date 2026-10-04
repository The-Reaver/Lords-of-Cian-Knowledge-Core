"""Batch 374: VB-066 (series names) and VB-067 (account types and reliability) locked; VB-062 amended."""
import json
import re
import sys
from collections import Counter

LEDGER = "canon-ledger.json"
DRAFT = sys.argv[1]
APPROVAL = "Abad's approval: 'lock it. once you're done we will move on to pyro and the Triad'."
SOURCE = "Original invention, chat-drafted 2026-10-04, no source document"

text = open(DRAFT, encoding="utf-8").read()
vb066 = re.search(r"\*\*VB-066\*\*\. (.+?)\n\n", text, re.S).group(1).strip()
vb067 = re.search(r"\*\*VB-067\*\*\. (.+?)\n\n", text, re.S).group(1).strip()
amend = re.search(r'VB-062 amendment \(same batch\): append "(.+?)"\n', text, re.S).group(1).strip()

d = json.load(open(LEDGER, encoding="utf-8"))
rules = {r["id"]: r for r in d["rules"]}
for rid, stmt in (("VB-066", vb066), ("VB-067", vb067)):
    assert rid not in rules, rid
    d["rules"].append({"id": rid, "category": "voice-bible", "statement": stmt + " " + APPROVAL,
                       "status": "locked", "source": SOURCE})
assert "Qualified by VB-067" not in rules["VB-062"]["statement"]
rules["VB-062"]["statement"] += " Amended Batch 374, 2026-10-04: " + amend + " " + APPROVAL

nb = max(b["batch"] for b in d["batches_completed"]) + 1
assert nb == 374, nb
d["batches_completed"].append({
    "batch": nb,
    "source": SOURCE,
    "rules_affected": 3,
    "note": "VB-066 locks the series names ('Chronicle' reserved for Kanja; Lauris the Records, Daba the "
            "Rolls, Ozmund the Testaments, Ezio the Exhibits, Anirak the Collections, the territories the "
            "Annals) and renames the launch gate the Series Launch Protocol. VB-067 locks the account types "
            "(the Series, Comrade Account, Adversary Account, Dossier, Hearsay) and the reliability rule. "
            "VB-062 amended to match. Anirak's series name changed from the presented 'Tallies' to "
            "'Collections' after independent review found it collided with Kanja's tally method and Daba's "
            "own 'Tally' list (MCD-1610). Clean on the seventh independent review. " + APPROVAL,
})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-04"
json.dump(d, open(LEDGER, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(LEDGER, "a", encoding="utf-8").write("\n")

d = json.load(open(LEDGER, encoding="utf-8"))
dups = [k for k, v in Counter(r["id"] for r in d["rules"]).items() if v > 1]
print("duplicates:", dups, "| rules:", len(d["rules"]), "| version:", d["ledger_version"],
      "| batch:", max(b["batch"] for b in d["batches_completed"]))
