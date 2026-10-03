import json, re
P = "canon-ledger.json"
CH = "docs/lords-of-cian/chronicles/"
APPROVAL = "go"
SOURCE = "Voice correction of locked material per VB-063 and the Voice Progression Sheet (docs/lords-of-cian/voice/), 2026-10-03; no facts changed"
d = json.load(open(P, encoding="utf-8"))
R = {r["id"]: r for r in d["rules"]}

def ws_rep(path, a, b):
    t = open(path, encoding="utf-8").read()
    pat = r"\s+".join(re.escape(w) for w in a.split())
    assert len(re.findall(pat, t)) == 1, (path, a[:60])
    open(path, "w", encoding="utf-8").write(re.sub(pat, lambda m: b, t))

# Chronicle III header: superseded growth convention.
ws_rep(CH + "kanja-chronicle-iii-what-the-dark-could-not-keep.md",
  "Onyx's presence has grown from Chronicle I's near-silence to its second real appearance in this track, matching roughly the manuscript's own Chronicle II/III-level growth — still unlabeled, longer and more assertive than before.",
  "Onyx's closing coda is its second appearance in this track, longer and more interpretive than\nChronicle I's, with the body narration compressing toward the blade's register.")

# Storm That Walks MCD-571 / MCD-586 headers: Rebellion-era pin.
for rid, fn in (("MCD-571", "the-boats-that-didnt-come-in.md"), ("MCD-586", "what-the-chart-didnt-show.md")):
    ws_rep(CH + fn, "Narrated in neutral third-person prose.*",
      "Narrated in neutral third-person prose. Age pinned Batch 359, 2026-10-03: Rebellion era (age\n29-30), pre-sealing (`MCD-246`), so the Trinity gear stands. Abad's approval: \"go.\"*")

AMEND = [
 ("MCD-1866", "Onyx of Oblivion appears only in a near-silent, unlabeled closing coda -- its first appearance in this track, deliberately the shortest and least articulate of the whole wave, establishing the true zero point the later entries grow from.",
  "Onyx of Oblivion appears only in a short, unlabeled closing coda -- its first appearance in this track -- already in its full Codex voice per the Voice Progression Sheet's Phase 1 and VB-063 (present tense, compressed, verdicts delivered, 'the blade' and 'the boy'), sharper than the literary body around it."),
 ("MCD-1868", "Onyx's coda has grown to its second real appearance in this track -- longer and more assertive than Chronicle I's, still unlabeled, matching the Game Plan's specified growth curve.",
  "Onyx's coda is its second appearance in this track -- longer and more interpretive than Chronicle I's, still unlabeled -- with the body narration at the Voice Progression Sheet's late Phase 2 (combat compressed into fragments and present tense, Iron/Rust verdicts in the intense moments), per VB-063."),
 ("MCD-1880", "Narrated by Onyx throughout, completing VB-026's handoff: its self-reference shifts from 'the blade' to 'I' at the moment the case closes, beginning the seconds-count MCD-246 locks.",
  "Narrated by Onyx throughout, completing VB-026's handoff at the Voice Progression Sheet's close of Phase 3: 'the blade' holds from first line to last, the Captain is 'the Captain,' and its single sanctioned first-person line ('So I began it.') falls at the moment the case closes, beginning the seconds-count MCD-246 locks (VB-063)."),
]
PINS = [("MCD-562", 29), ("MCD-565", 29), ("MCD-568", 30), ("MCD-574", 30), ("MCD-577", 30), ("MCD-583", 30), ("MCD-571", None), ("MCD-586", None)]
for rid, old, new in AMEND:
    s = R[rid]["statement"]; assert s.count(old) == 1, rid
    R[rid]["statement"] = s.replace(old, new) + " Voice wording corrected Batch 359, 2026-10-03. Abad's approval: '" + APPROVAL + "'"
for rid, age in PINS:
    pin = f"age {age}, Rebellion era, pre-sealing" if age else "age 29-30, Rebellion era, pre-sealing"
    R[rid]["statement"] += f" Age pinned Batch 359, 2026-10-03: {pin} (MCD-246), so the Trinity gear stands."
nb = max(b["batch"] for b in d["batches_completed"]) + 1
d["batches_completed"].append({"batch": nb, "source": SOURCE, "rules_affected": len(AMEND) + len(PINS),
  "note": "Onyx voice corrections across locked material: Kanja Chronicles I (Phase 1 coda in full Codex voice, dialogue trimmed), II (dialogue only, pre-bonding), III (late Phase 2), IV (close of Phase 3, 'the Captain', 'the blade' throughout bar the sealing line); MCD-1866/1868/1880 voice wording; Onyx's conversational lines in Alias Chronicles MCD-715/720/721/1127 rewritten as utilitarian grip-fragments (prose only); eight Storm That Walks entries (MCD-562/565/568/571/574/577/583/586) pinned Rebellion-era, pre-sealing. Abad's approval: \"" + APPROVAL + "\""})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]
print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
