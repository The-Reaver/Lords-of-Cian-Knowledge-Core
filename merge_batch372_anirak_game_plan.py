"""Batch 372: Anirak's Game Plan locked -- VB-065 new; VB-020, MCD-1881, CC-163, CC-101 amended."""
import json, re
from collections import Counter

LEDGER = "canon-ledger.json"
DRAFT = "docs/lords-of-cian/drafts/2026-10-04-anirak-game-plan-rules.md"
SOURCE = ("Anirak Game Plan (docs/lords-of-cian/character-profiles/anirak.md, Section 3), approved "
          "2026-10-04; rule text at " + DRAFT)
APPROVAL = "Abad's approval: 'let's go with your recommendations.'"

d = json.load(open(LEDGER, encoding="utf-8"))
ids = {r["id"] for r in d["rules"]}
t = open(DRAFT, encoding="utf-8").read()

def para(rid, cat):
    m = re.search(r"\*\*" + rid + r" \(new, " + cat + r"\)\.\*\* (.*?)\n\n", t, re.S)
    return " ".join(m.group(1).split()).replace("`", "")

def amend_text(rid):
    m = re.search(r"- \*\*`" + rid + r"`\.\*\* (.*?)(?=\n- \*\*|\n\n)", t, re.S)
    return " ".join(m.group(1).split()).replace("`", "")

assert "VB-065" not in ids
d["rules"].append({"id": "VB-065", "category": "voice-bible",
                   "statement": para("VB-065", "voice-bible") + " " + APPROVAL,
                   "status": "locked", "source": SOURCE})

R = {r["id"]: r for r in d["rules"]}
for rid in ("VB-020", "CC-101"):
    a = amend_text(rid)
    m = re.match(r'"(.*)" becomes "(.*)"$', a)
    old, new = m.group(1), m.group(2)
    assert R[rid]["statement"].count(old) == 1, rid
    R[rid]["statement"] = R[rid]["statement"].replace(old, new)
for rid in ("MCD-1881", "CC-163"):
    a = amend_text(rid)
    m = re.match(r'Append: "(.*)"$', a)
    R[rid]["statement"] = R[rid]["statement"].rstrip() + " Amended Batch 372, 2026-10-04: " + m.group(1) + " " + APPROVAL

nb = max(b["batch"] for b in d["batches_completed"]) + 1
d["batches_completed"].append({
    "batch": nb, "source": SOURCE, "rules_affected": 5,
    "note": ("Anirak's Game Plan approved and locked; her Character Chronicle gate is cleared. VB-065 "
             "sets her track's voice (close-third, articles kept, binary verdicts without Iron and Rust, "
             "no 'spike'). VB-020 adds her track to the close-third assignment. MCD-1881 sets her "
             "marquee constraints (at most three before Book 1, CC-164 necessity kills at Warm, run "
             "under the epithet Blades Fury). CC-163 dates the epithet's public use by Kanja 140 and "
             "lists who holds her name. CC-101: Sephtis recruited Ren under the disguise he kept after "
             "his staged withdrawal (MCD-982). Wave picked: Maw-11, the second harness, then Ren, in "
             "chronological order. Abad's approval, verbatim: 'let's go with your recommendations.'")})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-04"
json.dump(d, open(LEDGER, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(LEDGER, "a", encoding="utf-8").write("\n")
c = Counter(r["id"] for r in d["rules"])
print("batch", nb, "version", d["ledger_version"], "rules", len(d["rules"]),
      "duplicates", [k for k, v in c.items() if v > 1])
