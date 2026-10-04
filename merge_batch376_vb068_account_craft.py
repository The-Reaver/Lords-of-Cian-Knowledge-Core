"""Batch 376: VB-068 (the account craft standard) locked.

Abad's rulings at lock: greetings carried by action (R0.2) confirmed; spoken Spanish as phrase only,
never as an invented name (M1) confirmed; the standard's comic registers may run broader than VB-004
in told accounts, set out by a VB-004 amendment drafted separately (written deadpan until it locks).
The standard itself lives at docs/lords-of-cian/voice/account-craft-standard.md.
Usage: python3 merge_batch376_vb068_account_craft.py <draft.md>
"""
import json
import re
import sys
from collections import Counter

LEDGER = "canon-ledger.json"
DRAFT = sys.argv[1]
APPROVAL = "lock it, approve the picks, confirm all three"
SOURCE = "Original invention, chat-drafted 2026-10-04; research base research/accounts-psychology/00-09"

text = open(DRAFT, encoding="utf-8").read()
st = re.search(r"\*\*VB-068\*\*\. (.+?)\n\nApproval quote", text, re.S).group(1)
st = re.sub(r"\s+", " ", st.replace("`", "")).strip()

d = json.load(open(LEDGER, encoding="utf-8"))
ids = {r["id"] for r in d["rules"]}
assert "VB-068" not in ids
d["rules"].append({"id": "VB-068", "category": "voice-bible", "statement": st,
                   "status": "locked", "source": SOURCE})
d["batches_completed"].append({
    "batch": 376, "source": SOURCE, "rules_affected": 1,
    "note": ("VB-068 locks the account craft standard (docs/lords-of-cian/voice/account-craft-standard.md): "
             "teller state, identified listener and setting module fixed before drafting; the institution bar; "
             "the section 7 checklist made part of the Connective-Tissue Gate's independent review. Abad confirmed "
             "greetings carried by action (R0.2) and spoken Spanish as phrase only (M1), and ruled the comic "
             "registers may run broader than VB-004 in told accounts, by a VB-004 amendment drafted separately. "
             "The approved vocabulary picks lock as their own rules. Clean on the tenth independent review. "
             f"Abad's approval, verbatim: \"{APPROVAL}\"."),
})
d["ledger_version"] = "37.8"
d["last_updated"] = "2026-10-04"
json.dump(d, open(LEDGER, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(LEDGER, "a", encoding="utf-8").write("\n")

d = json.load(open(LEDGER, encoding="utf-8"))
dup = [k for k, v in Counter(r["id"] for r in d["rules"]).items() if v > 1]
print("duplicates:", dup, "| total rules:", len(d["rules"]), "| version:", d["ledger_version"])
