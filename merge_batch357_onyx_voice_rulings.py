import json
P = "canon-ledger.json"
APPROVAL = ("Self-reference: \"The blade\" (Recommended). Articles: Follow the manuscript (Recommended). "
            "\"Spike\": Ban it everywhere (Recommended). Count: Exact (Recommended).")
SOURCE = "Original invention, chat-drafted 2026-10-03, no source document; rulings on the Voice Bible and Voice Progression Sheet (docs/lords-of-cian/voice/)"
d = json.load(open(P, encoding="utf-8"))
R = {r["id"]: r for r in d["rules"]}
NEW = {"id": "VB-063", "category": "voice-bible-narrator-onyx", "status": "locked", "source": SOURCE,
  "statement": ("The Onyx voice standard and its gated check. Every Onyx-narrated or Onyx-voiced passage, in any "
   "track, is governed by the Voice Bible's Narrator 1 sheet and the Voice Progression Sheet (mirrored at "
   "docs/lords-of-cian/voice/), with the phase fixed by in-world age: Phase 1 ages 18-20, Phase 2 21-27, "
   "Phase 3 27-30, Phase 4 the Long Mask. Standing rulings where the documents and the manuscript differ: "
   "(1) Onyx refers to itself as 'the blade' ('us' permitted), never 'I'; the single exception is Kanja "
   "Chronicle IV's closing line at the sealing. (2) Articles follow the manuscript codas: kept, with the "
   "telegraphic effect carried by very short sentences, fragments, and refrains rather than article-dropping. "
   "(3) The word 'spike' is banned from all prose, the Density Spike and the Heartline's signals alike. "
   "(4) The seconds-count is exact, never hedged, reckoned on a 365-day year from the Sovereign Pier treaty. "
   "Carried from the documents: the Phase 1 closing coda is already in full Codex voice (present tense, "
   "compressed, verdicts delivered) -- the body narration compresses over the phases, the coda never grows "
   "from inarticulate to articulate; from Phase 3 Onyx calls Kanja 'the Captain', in Phase 4 only 'the "
   "Captain'; present tense is the Phase 4 default, including the scenes inside a retrospective Long Mask "
   "account, with past tense kept for the Dark Ledger frame and deep history; no equivocation, no balanced "
   "antithesis, no textbook explanation of powers or gear, no narrator emotional display -- loyalty shows as "
   "precision. Onyx speaks in any scene only through the grip and only in utilitarian fragments. Before any "
   "such draft is presented to Abad it passes the gated voice check in the character-profile template; a "
   "failing draft is redrafted, not presented. Supersedes the 'least articulate' Chronicle I coda convention "
   "(MCD-1866) and the first-person clause of VB-062. Abad's approval: '" + APPROVAL + "'")}
assert NEW["id"] not in R
d["rules"].append(NEW)
R["VB-062"]["statement"] += (" Amended Batch 357, 2026-10-03: Onyx narrates as 'the blade', never 'I' (VB-063); "
   "the first-person clause above is superseded, except Kanja Chronicle IV's closing line at the sealing. "
   "Abad's approval: '" + APPROVAL + "'")
s = R["ARS-437"]["statement"]
assert s.count("the specific spike of a kill") == 1
R["ARS-437"]["statement"] = s.replace("the specific spike of a kill", "the specific jolt of a kill") + (
   " Amended Batch 357, 2026-10-03: 'spike' replaced by 'jolt' per VB-063's ban on the word in prose. "
   "Abad's approval: '" + APPROVAL + "'")
nb = max(b["batch"] for b in d["batches_completed"]) + 1
d["batches_completed"].append({"batch": nb, "source": SOURCE, "rules_affected": 3,
  "note": "VB-063 locks the Onyx voice standard and its gated check (the blade not I; manuscript articles; 'spike' banned; exact seconds-count; Phase 1 coda in full voice; 'the Captain'; Phase 4 present tense); VB-062 first-person clause superseded; ARS-437 'spike' -> 'jolt'. Abad's approval: \"" + APPROVAL + "\""})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]
print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
