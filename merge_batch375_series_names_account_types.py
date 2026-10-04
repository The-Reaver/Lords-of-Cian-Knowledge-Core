"""Batch 375: VB-066 (series names) and VB-067 (account types and reliability) locked; VB-062 amended;
the series rename carried in the same batch (Connective-Tissue Gate step 3).

Order: (1) scripts/rename_series.py --apply renames files, rule statements, category tags, entry
titles/headers/notes, profiles and living docs; (2) hand fixes for residues the tool cannot judge;
(3) the new rules are added. Living-doc hand edits are committed alongside this script.
Usage: python3 merge_batch375_series_names_account_types.py <draft.md>
"""
import json
import re
import sys
from collections import Counter

LEDGER = "canon-ledger.json"
DRAFT = sys.argv[1]
APPROVAL = "Abad's approval: 'lock it. once you're done we will move on to pyro and the Triad'."
SOURCE = "Original invention, chat-drafted 2026-10-04, no source document"

import subprocess
subprocess.run([sys.executable, "scripts/rename_series.py", "--apply"], check=True)

HAND = {
    "VB-020": [("Lauris and Ezio Exhibits = Fermand (CC-034); Alias, Territory, Daba, and Anirak Collections = neutral close-third",
                "Lauris's Records and Ezio's Exhibits = Fermand (CC-034); the Alias Chronicles, the territory Annals, Daba's Rolls, and Anirak's Collections = neutral close-third")],
    "PH2-048": [("Chronicles are written as each homage-era territory's own numbered series", "Annals are written as each homage-era territory's own numbered series")],
    "PH2-061": [("Ogoun Xarey's and Yalokona's own Chronicles.", "Ogoun Xarey's and Yalokona's own Annals.")],
    "MCD-1859": [("No Chronicle prose has been drafted;", "No narrative prose has been drafted;")],
    "MCD-1860": [("No Chronicle prose has been drafted;", "No narrative prose has been drafted;")],
    "MCD-1862": [("No Chronicle prose has been drafted;", "No narrative prose has been drafted;")],
    "MCD-1864": [("No Chronicle prose has been drafted; this is a queued future beat for whenever Ezio's own Exhibits launches under the Tier 1 gameplan, pending Abad's review.",
                  "Narrative prose drafted Batch 318 as Ezio Exhibit I, 'The Frequency That Never Failed' (MCD-1876).")],
    "MCD-1867": [("Daba's own 50-Chronicle launch wave", "Daba's own 50-entry launch wave")],
    "MCD-1881": [("once her Character Chronicle gate clears", "once her Series Launch Protocol gate clears")],
}
d0 = json.load(open(LEDGER, encoding="utf-8"))
r0 = {r["id"]: r for r in d0["rules"]}
for rid, pairs in HAND.items():
    st = r0[rid]["statement"]
    for old, new in pairs:
        assert st.count(old) == 1, (rid, old)
        st = st.replace(old, new)
    r0[rid]["statement"] = st
json.dump(d0, open(LEDGER, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(LEDGER, "a", encoding="utf-8").write("\n")

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
assert nb == 375, nb
d["batches_completed"].append({
    "batch": nb,
    "source": SOURCE,
    "rules_affected": 3 + len(HAND),
    "note": "VB-066 locks the series names ('Chronicle' reserved for Kanja; Lauris the Records, Daba the "
            "Rolls, Ozmund the Testaments, Ezio the Exhibits, Anirak the Collections, the territories the "
            "Annals) and renames the launch gate the Series Launch Protocol. VB-067 locks the account types "
            "(the Series, Comrade Account, Adversary Account, Dossier, Hearsay) and the reliability rule. "
            "VB-062 amended to match. The rename was carried in the same batch by scripts/rename_series.py "
            "(362 entry files, ~390 rule statements, category tags, profiles, living docs, CLAUDE.md's standing "
            "rules) plus hand fixes to VB-020, PH2-048, PH2-061, MCD-1859, MCD-1860, MCD-1862, MCD-1864 (stale: "
            "Ezio Exhibit I already dramatizes it), MCD-1867, MCD-1881. Anirak's series name changed from the presented 'Tallies' to "
            "'Collections' after independent review found it collided with Kanja's tally method and Daba's "
            "own 'Tally' list (MCD-1610). Clean on the ninth independent review. " + APPROVAL,
})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-04"
json.dump(d, open(LEDGER, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(LEDGER, "a", encoding="utf-8").write("\n")

d = json.load(open(LEDGER, encoding="utf-8"))
dups = [k for k, v in Counter(r["id"] for r in d["rules"]).items() if v > 1]
print("duplicates:", dups, "| rules:", len(d["rules"]), "| version:", d["ledger_version"],
      "| batch:", max(b["batch"] for b in d["batches_completed"]))
