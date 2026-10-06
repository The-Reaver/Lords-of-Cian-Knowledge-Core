"""Batch 379: the Trinity on-page bar and the Book 1 unlock tier (Abad's rulings, 2026-10-06; follows
Batch 378). Locks VB-069 (the bar, what an open entry may say, Onyx-as-narrator gating, the manuscript
set, the Book 1 unlock tier, new entries, the Karkosa Heist as first use on the page, canon status, era
errors); appends pointer notes to VB-062, VB-026, MCD-1881, MCD-1902 and MCD-1907; corrects two era errors
(the Trinity shown in use during the sealed Long Mask) in the-recapture-at-dusk (MCD-1238) and
the-order-he-didnt-question (MCD-589); fixes kanja-haku-rexmar.md ("from age 18 through age 314 is Trinity
gear"); makes one mechanical wording fix (one sentence of MCD-1182
realigned with MCD-442); activates the gate manifest at
docs/lords-of-cian/archive/book1-unlock-trinity-manifest.md (+ .json; 188 entries); carries the change to every doc that states it; appends the Batch 379 paragraph to CLAUDE.md.
Usage: python3 merge_batch379_trinity_on_page.py <draft.md> "<approval quote>"
"""
import json
import os
import re
import sys
import textwrap
from collections import Counter

LEDGER = "canon-ledger.json"
SOURCE = ("Abad's rulings in conversation, 2026-10-06; drafted from the Trinity on-page census "
          "(research/trinity-on-page-census-2026-10-06.md)")
NEW_IDS = ["VB-069"]
CH = "docs/lords-of-cian/chronicles/"
PR = "docs/lords-of-cian/character-profiles/"
DOCS = "docs/lords-of-cian/"
MANI = DOCS + "archive/book1-unlock-trinity-manifest"
CENSUS = "research/trinity-on-page-census-2026-10-06.md"

# ---------------------------------------------------------------------------------------------
# (b) Ledger rule changes. No statement is rewritten. Each rule below takes an appended note; the
# note must not already be present. (rule id, appended clause)
# ---------------------------------------------------------------------------------------------
AMEND = []
APPEND = {
    "VB-062": " Batch 379 note: the Kanja-version track, the home of the Onyx accounts, sits in the Book 1 unlock "
              "tier, and so do the Alias entries that show the Trinity in use or cannot be decided either way "
              "(VB-069); open entries tell the Trinity's deeds as legend, rumor, aftermath, survivors' accounts and "
              "SBD Dossiers under that rule.",
    "VB-026": " Batch 379 note: the Kanja-version track and the eight manuscript Chronicles, which carry this "
              "handoff, sit in the Book 1 unlock tier (VB-069); the handoff itself is unchanged.",
    "MCD-1881": " Batch 379 note: a marquee kill dramatized in an entry in the Book 1 unlock tier (VB-069) stays "
                "referenceable as legend in open entries; the tiering is unchanged.",
    "MCD-1902": " Batch 379 note: in Book 1's present-day narrative the Karkosa Heist is the Trinity's first use, "
                "where it is reclaimed; where Book 1's own Rebellion chapters fall is left to Book 1; entries that "
                "show the Trinity in use sit in the Book 1 unlock tier until Book 1 is published (VB-069).",
    "MCD-1907": " Batch 379 note: the second attempt is the first full showing of the Trinity in combat in Book 1's "
                "present-day narrative (VB-069).",
    "MCD-589": " Corrected Batch 379, 2026-10-06: two lines that still had the Trinity committed to the forecast "
               "now name Kanja and his Long-Mask-era kit; the Trinity stays sealed at L9 through the Long Mask "
               "(MCD-246, VB-069).",
    "MCD-1238": " Corrected Batch 379, 2026-10-06: the guards' collapse is credited to the loadout alone; an "
                "earlier line credited 'the Trinity and the loadout together', which a Trinity sealed at L9 for "
                "the Long Mask cannot produce (MCD-246, VB-069).",
}

# ---------------------------------------------------------------------------------------------
# (c) File edits: (path, region, exact old, new, expected count). Region: P narrative prose,
# H header note, N continuity note, D doc.
# ---------------------------------------------------------------------------------------------
RECAP = CH + "the-recapture-at-dusk.md"
ORDER = CH + "the-order-he-didnt-question.md"
KJ = PR + "kanja-haku-rexmar.md"
TPL = PR + "_TEMPLATE.md"
TRK = DOCS + "chronicle-tracks-status.md"
EYES = CH + "what-he-read-with-his-eyes-shut.md"
MS = ["chronicle-i-the-scrip-forge-raid.md", "chronicle-ii-the-dredge-line-ambush.md",
      "chronicle-iv-iron-shallows.md", "chronicle-v-the-siege-of-maw-9.md",
      "chronicle-vii-the-siege-of-the-ghost-harbor.md"]

EDITS = [
    # --- era fixes: narrative prose ---
    (RECAP, "P", "the Trinity and the loadout together produced", "the loadout produced", 1),
    (ORDER, "P", "before committing the Trinity to a timing window", "before committing his kit to a timing window", 1),
    (ORDER, "P", "had verified before the Trinity moved.", "had verified before Kanja moved.", 1),
    # --- a mechanical clarification: the decades of tactile reading are the old digger's (MCD-442) ---
    (EYES, "P", "decades of tactile reading he'd learned as a supplement",
     "decades of the old man's tactile reading, which Kanja had learned as a supplement", 1),
]
# --- manuscript Chronicles I, II, IV, V, VII: the header's gate pointer now cites the rule and the manifest ---
for _f in MS:
    EDITS.append((CH + _f, "H",
                  "Gated to Book 1 as a manuscript Chronicle together with III, VI and VIII (Trinity census, "
                  "`research/trinity-on-page-census-2026-10-06.md`).",
                  "Gated to Book 1 with the whole manuscript set (Book 1 unlock tier, `VB-069`; manifest "
                  "`docs/lords-of-cian/archive/book1-unlock-trinity-manifest.md`; census "
                  "`research/trinity-on-page-census-2026-10-06.md`).", 1))
EDITS += [
    # --- the Kanja profile: the line-71 error and the archive placement ---
    (KJ, "D",
     "  through age 314 is Trinity gear, inherited tactical instinct, and craft/reputation, not raw\n"
     "  density-scaled physical power.",
     "  through age 314 is gear, inherited tactical instinct, and craft/reputation, not raw\n"
     "  density-scaled physical power. The gear is the Trinity to the Pier at age 30; the Talisman, the\n"
     "  Aegis-Talisman and the Rexmar Machete from then on (`MCD-246`), with the post-Mafesto kit from age 33\n"
     "  (`ARS-344` through `ARS-356`); the Trinity again from the Karkosa Heist (`MCD-1902`).", 1),
    (KJ, "D",
     "**Gate cleared:** YES, 2026-09-28 — Chronicle prose may now be drafted for this track.\n",
     "**Gate cleared:** YES, 2026-09-28 — Chronicle prose may now be drafted for this track.\n"
     "**Book 1 unlock tier (`VB-069`, Batch 379):** every entry of this track, and the eight manuscript\n"
     "Chronicles, is filed in the Book 1 unlock tier (the Kanja-version track and the manuscript set). Each\n"
     "keeps its standing and none is rewritten; the archive holds them until Book 1 is published. New entries\n"
     "of this track are written for the tier and added to\n"
     "`docs/lords-of-cian/archive/book1-unlock-trinity-manifest.md` in the batch that locks them.\n", 1),
    # --- the series template: the gate step carries the bar ---
    (TPL, "D",
     "  draft is presented with a connective-tissue note. The Section 1 findings above must be resolved\n"
     "  or queued before this gate clears.\n",
     "  draft is presented with a connective-tissue note. The Section 1 findings above must be resolved\n"
     "  or queued before this gate clears.\n"
     "- **Trinity on-page bar (`VB-069`, Batch 379):** before Book 1 is published, no entry for release shows\n"
     "  the Trinity (Mafesto, Onyx of Oblivion, Obsidian Malice) in use on the page. The draft's\n"
     "  connective-tissue note says whether it does. An entry that does, that Onyx narrates, or that belongs\n"
     "  to the Kanja-version track is written for the Book 1 unlock tier and added to\n"
     "  `docs/lords-of-cian/archive/book1-unlock-trinity-manifest.md`\n"
     "  in the batch that locks it. The Trinity may be named, and told through legend, rumor, aftermath,\n"
     "  survivors' accounts and SBD Dossiers, in any entry.\n", 1),
    # --- the tracker ---
    (TRK, "D",
     "\n## Alias Chronicle track (Kanja's 11 aliases)\n",
     "\n**Book 1 unlock tier (`VB-069`, Batch 379).** The seven entries above and the eight manuscript Chronicles are\n"
     "filed in the Book 1 unlock tier (the Kanja-version track and the manuscript set), and so are 173 Alias entries\n"
     "that show the Trinity in use or could not be read either way (Bane 22, Blue-Collar Titan 30, Captain 5, Crow\n"
     "King 5, Iron Bastard 17, Lord of Embers 37, Scourge 1, Sovereign Ghost 23, Storm That Walks 13, Trench Monarch\n"
     "20, Industrial Myth 0).\n"
     "The archive holds them until Book 1 is published; each keeps its standing. The full list is\n"
     "`docs/lords-of-cian/archive/book1-unlock-trinity-manifest.md`.\n"
     "\n## Alias Chronicle track (Kanja's 11 aliases)\n", 1),
    # --- the census, which the manifest draws on ---
    (CENSUS, "D",
     "The only Trinity-in-use evidence of any strength is IV L75, and that line states the Trinity was not used.",
     "The only Trinity-in-use evidence of any strength is IV L75, and that line states the Trinity was not used.\n"
     "\n"
     "## 7. Resolution, Batch 379, 2026-10-06\n"
     "\n"
     "Abad's recommendation was accepted before the census ran; its gating is locked as `VB-069`, and the gated\n"
     "entries are listed in `docs/lords-of-cian/archive/book1-unlock-trinity-manifest.md` (188 entries: 172\n"
     "IN-USE, 15 TRACK, 1 AMBIGUOUS-GATED; the three withdrawn Chronicles IX to XI are not listed). The five\n"
     "AMBIGUOUS entries of section 4 and the three ERA-ERROR candidates of section 3 resolved as follows.\n"
     "`the-recapture-at-dusk` (`MCD-1238`) and `the-order-he-didnt-question` (`MCD-589`) were era errors and are\n"
     "corrected to the gear Kanja held at that age; neither shows the Trinity now. The twelve locks (`MCD-729`)\n"
     "could not be read either way and gates. The duel (`MCD-1425`) and the well (`MCD-1144`) state the Trinity\n"
     "unused and stay open. `the-call-he-got-wrong` (`MCD-594`) is read as Rebellion era: the Captain entries\n"
     "beside it (`MCD-591`, `MCD-596`) show Mafesto live, Corren Halst has read the waters longer than Kanja's\n"
     "body has lived, the scene is a wartime raid, and the file shows no post-Mafesto kit. Its header states no\n"
     "era, so it is not treated as an error and stays in the manifest as IN-USE; Abad is asked to confirm the era.\n"
     "`the-well-that-went-dry` (`MCD-1454`) was checked for the same risk and is read as Rebellion era. A second\n"
     "scan of all 172 IN-USE files for post-Mafesto kit, ages above 30 and Long Mask mentions found no further era\n"
     "error. The one hit with \"age 33\", `the-white-that-took-the-map-away` (`MCD-1391`), carries it in a header\n"
     "correction note about when Sovereign Eyes is built; the entry itself is a Bane entry inside the Rebellion\n"
     "window.", 1),
    # --- CLAUDE.md: the gate's independent review and the standing conventions ---
    ("CLAUDE.md", "D",
     "post-Mafesto kit after, Book-2 Moonvault gifts never before Book 2).",
     "post-Mafesto kit after, Book-2 Moonvault gifts never before Book 2), and that no entry for release before\n"
     "   Book 1 shows the Trinity in use (`VB-069`).", 1),
    ("CLAUDE.md", "D",
     "never by repeating the stopped request.\n",
     "never by repeating the stopped request.\n"
     "- **The Trinity on-page bar (Abad, 2026-10-06, `VB-069`).** Before Book 1 is published, no entry open to\n"
     "  readers shows the Trinity (Mafesto, Onyx of Oblivion, Obsidian Malice) in use on the page. It may be named\n"
     "  and told through legend, rumor, aftermath, survivors' accounts and SBD Dossiers. Entries that show it in\n"
     "  use, every entry Onyx narrates, every entry of the Kanja-version track and the eight manuscript Chronicles\n"
     "  sit in the Book 1 unlock tier, listed in `docs/lords-of-cian/archive/book1-unlock-trinity-manifest.md`; a new\n"
     "  such entry joins the list in the batch that locks it. Gated entries keep their standing and are not rewritten.\n", 1),
    # --- the manifest goes live ---
    (MANI + ".md", "D",
     "*Status: draft for Batch 379, 2026-10-06. It takes effect when `VB-069` locks; the merge script then changes this line. Source:",
     "*Status: locked, Batch 379, 2026-10-06 (`VB-069`). Source:", 1),
    (MANI + ".json", "D",
     "\"status\": \"draft for Batch 379; takes effect when VB-069 locks\"",
     "\"status\": \"locked, Batch 379, 2026-10-06 (VB-069)\"", 1),
]
NOTE_APPEND = {
    RECAP: " Corrected Batch 379, 2026-10-06: the guards' collapse is credited to the loadout alone. An earlier "
           "line credited it to 'the Trinity and the loadout together', which cannot stand in the Long Mask, "
           "when the Trinity is sealed at L9 (`MCD-246`, `VB-069`).",
    EYES: " Corrected Batch 379, 2026-10-06 (mechanical): 'decades of tactile reading he'd learned' now reads as "
          "decades of the old man's tactile reading, which Kanja had learned, realigning the sentence with `MCD-442`, "
          "where the old digger holds the decades of knowledge and Kanja learns it.",
    ORDER: " Corrected Batch 379, 2026-10-06: two lines that still had the Trinity committed to the forecast "
           "('committing the Trinity to a timing window', 'before the Trinity moved') now name Kanja and his kit, "
           "matching the Batch 325 swap (321 in this file's header) to the Long-Mask-era kit; the Trinity stays "
           "sealed at L9 through the Long Mask (`MCD-246`, `VB-069`).",
}


COVERED = [
    "(a) New entries of the Kanja-version track, and any new entry that needs the Trinity in use, are written for "
    "the tier, and the unlock is eligibility when Book 1 is published, subject to the archive's review, matching "
    "Phase 5 of the archive game plan (`VB-069`, items 4 and 5).",
    "(b) The first full showing of the Trinity in combat, in Book 1's present-day narrative, is `MCD-1907`, with the "
    "Heist's own fighting left open.",
    "(c) The gating itself: an entry that, read in full, cannot be decided either way (`MCD-729`) gates.",
    "(d) The 85 IN-USE entries whose header and rule state no era are carried at their track's default era.",
    "(e) Kanja Chronicle II gates with its track although it holds no Trinity and no Onyx.",
    "(f) The three withdrawn Chronicles IX to XI are not listed.",
    "(g) Legend describes what the weapons do at the level of effect and in the teller's own terms.",
    "(h) A told or recorded account may not stage the use as a scene, whatever the frame.",
    "(i) The definition that sets the tier apart from the archive's clearance levels and from its T0 to T4 "
    "classification, since the archive already carries both and a third \"tier\" could drift. The term \"Book 1 "
    "unlock tier\" was in the recommendation he accepted.",
    "(j) All eight manuscript Chronicles gate as a set.",
    "(k) `MCD-729` gates as an entry that, read in full, cannot be decided either way, while `MCD-1425` and "
    "`MCD-1144` stay open because they state the Trinity unused.",
    "(l) The eight borderline OPEN-MENTION entries stay open, with `the-siege-that-never-came` (`MCD-1011`) the "
    "closest call: Obsidian Malice is \"ready to discharge by midafternoon, its reserve built from the morning's "
    "work\", and no discharge is shown. Under item (1)'s one-clause test, the reserve implies Mafesto was engaged, "
    "which argues for gating.",
    "(m) Item (8) of the rule: an era error is corrected to the gear Kanja held at that age and is not filed in the "
    "tier, as a standing rule.",
    "(n) Item (6) of the rule: the Karkosa Heist is the Trinity's first use in Book 1's present-day narrative.",
    "(o) Item (1) of the rule: the in-use definition, under which a one-clause use, a failure and speech through the "
    "grip all count as use.",
    "(p) `the-call-he-got-wrong` (`MCD-594`) is read as Rebellion era. Its header states no era; the reading rests on "
    "`MCD-591` and `MCD-596`, the Captain entries beside it, which show Mafesto live, on Corren Halst's being older "
    "than Kanja's body (\"read these waters longer than I've been alive in this body\"), on the wartime raid itself, "
    "and on the absence of any post-Mafesto kit.",
]


def clean(t):
    t = re.sub(r"-\n\s*", "-", t)
    return re.sub(r"\s+", " ", t.replace("`", "").replace("**", "")).strip()


def parse_new(text):
    out = {}
    for m in re.finditer(r"\*\*(VB-069)\*\*\s*\(category: ([^)]+)\)\.\s*(.+?)(?=\n\n)", text, re.S):
        out[m.group(1)] = (m.group(2).strip(), clean(m.group(3)))
    assert sorted(out) == NEW_IDS, sorted(out)
    return out


def wrap_onto(body, clause, width=100):
    col = len(body) - body.rfind("\n") - 1
    out, line = "", ""
    for w in clause.split():
        if col + len(line) + 1 + len(w) > width and (line or col):
            out += line + "\n"
            col, line = 0, w
        else:
            line = (line + " " + w) if line else (" " + w if col else w)
    return out + line


def apply_file_edits():
    texts = {}
    for path, _region, old, new, n in EDITS:
        if path not in texts:
            texts[path] = open(path, encoding="utf-8").read()
        c = texts[path].count(old)
        assert c == n, (path, old[:80], c)
        texts[path] = texts[path].replace(old, new)
    for path, clause in NOTE_APPEND.items():
        t = texts.get(path) or open(path, encoding="utf-8").read()
        body = t.rstrip("\n")
        assert body.endswith("*") and "Batch 379" not in body[-len(clause) - 50:], path
        texts[path] = body[:-1] + wrap_onto(body[:-1], clause) + "*\n"
    for path, t in texts.items():
        open(path, "w", encoding="utf-8").write(t)
    return sorted(texts)


def check_manifest(byid):
    """The manifest must agree with the ledger and the files before it goes live."""
    m = json.load(open(MANI + ".json", encoding="utf-8"))
    ents = m["entries"]
    assert len(ents) == m["counts"]["total"] == 188, len(ents)
    cls = Counter(e["reason"] for e in ents)
    assert cls == {"IN-USE": 172, "TRACK": 15, "AMBIGUOUS-GATED": 1}, cls
    assert [e["rule"] for e in ents if e["reason"] == "AMBIGUOUS-GATED"] == ["MCD-729"]
    assert sum(1 for e in ents if e["track"].startswith("Alias:")) == 173
    files = [e["file"] for e in ents]
    assert len(set(files)) == len(files), "duplicate manifest file"
    for e in ents:
        assert os.path.exists(CH + e["file"]), e["file"]
        if e["rule"]:
            assert byid[e["rule"]]["status"] == "locked", e["rule"]
        else:
            assert e["file"].startswith("chronicle-"), e["file"]
    for gone in ("the-recapture-at-dusk.md", "the-order-he-didnt-question.md",
                 "the-duel-that-would-cost-nothing-but-him.md", "the-well-that-closed-over-the-boy.md"):
        assert gone not in files, gone
    md = open(MANI + ".md", encoding="utf-8").read()
    rows = re.findall(r"^\| \d+ \| `([^`]+)` \|", md, re.M)
    assert rows == files, "md and json lists differ"
    return len(ents)


def main():
    draft, approval = sys.argv[1], sys.argv[2]
    new = parse_new(open(draft, encoding="utf-8").read())
    d = json.load(open(LEDGER, encoding="utf-8"))
    byid = {r["id"]: r for r in d["rules"]}
    assert not set(NEW_IDS) & set(byid), "ID collision"
    n_manifest = check_manifest(byid)
    amended = set()
    for rid, clause in APPEND.items():
        assert "Batch 379" not in byid[rid]["statement"], rid
        byid[rid]["statement"] += clause
        amended.add(rid)
    for rid in NEW_IDS:
        cat, st = new[rid]
        d["rules"].append({"id": rid, "category": cat, "statement": st, "status": "locked", "source": SOURCE})
    files = apply_file_edits()
    d["batches_completed"].append({
        "batch": 379, "source": SOURCE, "rules_affected": len(NEW_IDS) + len(amended),
        "note": ("The Trinity on-page bar and the Book 1 unlock tier. Abad, 2026-10-06: 'after the Karkosa Heist, with "
                 "the Trinity. which is important we build up the fact that the trinity doesn't get used until after "
                 "book one is published which means we may have to keep some of the Chronicles locked in the archive. "
                 "cuz the way I'm thinking, wouldn't it be clever or better for the Trinity not to make an appearance "
                 "at all pre-book one but be spoken about in all and not giving away the stories where he's actually "
                 "using it like the 90 seconds his father Witnesses or the battles in which he uses the trinity? what "
                 "is your feedback'; then 'all recommendations, run the census' (answering a list whose item 7 "
                 "recommended that pre-Book-1 entries may describe what the weapons do as legend, and whose item 8 was "
                 "the census), an answer given before the census ran, accepting the recommendation that preceded the "
                 "census (gate and leave the entries as written; the bar; naming the Trinity and telling it through legend, "
                 "rumor, aftermath, survivors' accounts and SBD files; legend may describe what the weapons do; the "
                 "Book 1 unlock tier; the Kanja-version track gates because Onyx narrates it; new writing follows the "
                 "rule); then 'all yes on yiu 6 questions' ('yiu' reads 'you'; answering six questions whose sixth "
                 "asked whether to draft Batch 379), which confirmed only that Batch 379 be drafted. "
                 "VB-069 locks the bar (no entry open to readers shows the Trinity in use before Book 1 is "
                 "published), what an open entry may do (name the Trinity; legend, rumor, aftermath, survivors' "
                 "accounts and SBD Dossiers, which may be wrong; legend may describe what the weapons do), Onyx "
                 "narrating as the Trinity appearing (the Kanja-version track gates, and the eight manuscript "
                 "Chronicles gate as a set), the Book 1 unlock tier and its manifest, the Karkosa Heist as the "
                 "Trinity's first use in Book 1's present-day narrative (MCD-1902, MCD-070) with MCD-1907 as the first "
                 "full showing in combat there, that gated entries are not rewritten, and that the rule binds "
                 "archive publication and new entries while entries in the tier keep their canon standing. "
                 f"The manifest lists {n_manifest} entries (172 IN-USE, 15 TRACK, 1 AMBIGUOUS-GATED). Era errors "
                 "corrected: the-recapture-at-dusk (MCD-1238) and the-order-he-didnt-question (MCD-589); "
                 "the-call-he-got-wrong (MCD-594) is read as Rebellion era (covered only by the final approval) and "
                 "stays; the-well-that-went-dry (MCD-1454) was checked for the same risk and stays. "
                 "kanja-haku-rexmar.md corrected (the Trinity is the gear to age 30 only). Pointer notes "
                 "appended to: " + ", ".join(sorted(amended)) + ". Files carried: " + ", ".join(files)
                 + ". Covered only by Abad's final approval: " + " ".join(COVERED).replace("`", "")
                 + f" Abad's approval, verbatim: \"{approval}\"."),
    })
    d["ledger_version"] = "38.1"
    d["last_updated"] = "2026-10-06"
    json.dump(d, open(LEDGER, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    open(LEDGER, "a", encoding="utf-8").write("\n")

    n_entries = sum(1 for f in files if f.startswith(CH))
    n_docs = len(files) - n_entries
    c = open("CLAUDE.md", encoding="utf-8").read()
    anchor = "Ledger at `ledger_version` 38.0, 2,728 rules, 378 batches.\n"
    assert c.count(anchor) == 1
    covered_md = "\n".join(textwrap.fill(t, width=112, initial_indent="  - ", subsequent_indent="    ") for t in COVERED)
    c = c.replace(anchor, anchor + f"""
**Batch 379: the Trinity on-page bar and the Book 1 unlock tier (`VB-069`).** Abad: "{approval}"
- **The ruling.** Abad, 2026-10-06: "after the Karkosa Heist, with the Trinity. which is important we build up
  the fact that the trinity doesn't get used until after book one is published which means we may have to keep
  some of the Chronicles locked in the archive. cuz the way I'm thinking, wouldn't it be clever or better for the
  Trinity not to make an appearance at all pre-book one but be spoken about in all and not giving away the stories
  where he's actually using it like the 90 seconds his father Witnesses or the battles in which he uses the
  trinity? what is your feedback". He then said "all recommendations, run the census" (answering a list that
  included a recommendation that pre-Book-1 entries may describe what the weapons do as legend, and the census),
  before the census ran. It accepted the recommendation that preceded the census: gate the entries and leave them as written; the bar;
  naming the Trinity and telling it through legend, rumor, aftermath, survivors' accounts and SBD files; legend
  may describe what the weapons do; the Book 1 unlock tier; the Kanja-version track gates because Onyx narrates it;
  new writing follows the rule. His "all yes on yiu 6 questions" ("yiu" reads "you"; answering six questions whose
  sixth asked whether to draft Batch 379) confirmed only that Batch 379 is drafted.
- **The rule (`VB-069`).** Before Book 1 is published, no entry open to readers shows the Trinity (Mafesto, Onyx
  of Oblivion, Obsidian Malice) in use on the page. A piece is in use when a scene shows it worn and engaged,
  wielded, discharged or exercising a named power, including when it fails or acts in part; carried, racked,
  worn dormant or stated-unused is outside the bar, and so are the Talisman, the Aegis-Talisman, the Rexmar
  Machete and the post-Mafesto kit. An open entry may name the Trinity and tell it through legend, rumor,
  aftermath, survivors' accounts and SBD Dossiers (which may be wrong, `VB-067`); legend may describe what the
  weapons do, at the level of effect, within the teller's knowledge. A told account gives results and does not
  stage the use. An entry Onyx narrates counts as the Trinity appearing: the whole Kanja-version track gates, and
  so do the eight manuscript Chronicles. Entries that gate sit in the Book 1 unlock tier: they keep their standing,
  stay in the archive's vault and become eligible when Book 1 is published, subject to the archive's own review;
  none is rewritten. New entries for release before Book 1 follow the bar. In Book 1's present-day narrative the
  Trinity's first use is the Karkosa Heist (`MCD-1902`, `MCD-070`) and the first full showing in combat is the
  second attempt (`MCD-1907`). An entry set between the Pier and the Heist that shows the Trinity in use is an era
  error, corrected to the gear Kanja held at that age and not gated (`MCD-246`); the Heartline, the Dark Ledger
  and Onyx's retrospective narration are not use. The prefix is `VB-` because the rule governs how entries are
  written and filed, as `VB-062`, `VB-063`, `VB-067` and `VB-068` do; the world facts it leans on stay in `MCD-`.
- **The manifest.** `docs/lords-of-cian/archive/book1-unlock-trinity-manifest.md`, with a `.json` copy, lists
  {n_manifest} entries: 172 IN-USE, 15 TRACK (7 Kanja-version, 8 manuscript), 1 AMBIGUOUS-GATED (the twelve locks
  `MCD-729`). The three withdrawn Chronicles IX to XI are not listed, since a withdrawn entry never publishes. The
  76 OPEN-MENTION entries stay open, the eight borderline ones among them (covered only by the final approval),
  and so do the duel (`MCD-1425`) and the well (`MCD-1144`), which state the Trinity unused. The census is
  `research/trinity-on-page-census-2026-10-06.md`.
- **Era errors.** `the-recapture-at-dusk` (`MCD-1238`, Scourge, age 172) credited the guards' collapse to "the
  Trinity and the loadout together"; `the-order-he-didnt-question` (`MCD-589`, Storm That Walks, Long Mask) still
  had the Trinity committed to the forecast in two lines. Both are corrected to the Long-Mask-era kit as Batch 314
  and Batches 324 to 330 did, with a correction clause in each entry and each rule. `the-call-he-got-wrong`
  (`MCD-594`, Captain) is read as Rebellion era (covered only by the final approval), from the Captain entries
  beside it (`MCD-591`, `MCD-596`, which show Mafesto live), Corren Halst's being older than Kanja's body, the
  wartime raid and the absence of any post-Mafesto kit; its header states no era, so it is not treated as an
  error and stays in the manifest. `the-well-that-went-dry` (`MCD-1454`, Blue-Collar Titan) was checked for the
  same risk: it is set after the siege while the siege's shoring is still unfinished, and it stays.
  `kanja-haku-rexmar.md` no longer says the gear from 18 to 314 is the Trinity.
- **Covered only by Abad's final approval, which presented each item explicitly.**
{covered_md}
- **Propagation.** {len(amended)} rule statements carry pointer or correction notes; {n_entries} entries and
  {n_docs} docs carried. The {n_entries} entries are the five manuscript headers' gate pointer, the two era
  corrections and the `MCD-1182` wording. The {n_docs} docs are the Kanja profile, the series template, the tracker,
  the census, this file's standing sections and the manifest's two status lines. One
  mechanical wording fix rides along, which adds no fact: one sentence of `MCD-1182` gave the old digger's decades of
  tactile reading to Kanja and now realigns with `MCD-442`. The mirrored Voice Bible and Voice Progression Sheet
  stay unedited; the archive repo's Phase 5 plan is owed an update to name the manifest.
Ledger at `ledger_version` 38.1, {len(d['rules']):,} rules, 379 batches.
""")
    open("CLAUDE.md", "w", encoding="utf-8").write(c)

    d = json.load(open(LEDGER, encoding="utf-8"))
    dup = [k for k, v in Counter(r["id"] for r in d["rules"]).items() if v > 1]
    print("duplicates:", dup, "| total rules:", len(d["rules"]), "| version:", d["ledger_version"],
          "| rules amended:", len(amended), "| files edited:", len(files))


if __name__ == "__main__":
    main()
