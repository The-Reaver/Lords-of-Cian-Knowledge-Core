"""Batch 379: the Trinity on-page bar and the Book 1 unlock tier (Abad's rulings, 2026-10-06; follows
Batch 378). Locks VB-069 (the bar, what an open entry may say, Onyx-as-narrator gating, the manuscript
set, the Book 1 unlock tier, new entries, the Karkosa Heist as first use on the page, canon status, era
errors); appends pointer notes to VB-062, VB-026, MCD-1881, MCD-1902 and MCD-1907; corrects two era errors
(the Trinity shown in use during the sealed Long Mask) in the-recapture-at-dusk (MCD-1238) and
the-order-he-didnt-question (MCD-589); fixes kanja-haku-rexmar.md ("from age 18 through age 314 is Trinity
gear"); activates the gate manifest at docs/lords-of-cian/archive/book1-unlock-trinity-manifest.md (+ .json);
carries the change to every doc that states it; appends the Batch 379 paragraph to CLAUDE.md.
Usage: python3 merge_batch379_trinity_on_page.py <draft.md> "<approval quote>"
"""
import json
import os
import re
import sys
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
              "tier, and so do the Alias entries that show the Trinity in use (VB-069); open entries tell the "
              "Trinity's deeds as legend, rumor, aftermath, survivors' accounts and SBD Dossiers under that rule.",
    "VB-026": " Batch 379 note: the Kanja-version track and the eight manuscript Chronicles, which carry this "
              "handoff, sit in the Book 1 unlock tier (VB-069); the handoff itself is unchanged.",
    "MCD-1881": " Batch 379 note: a marquee kill dramatized in an entry in the Book 1 unlock tier (VB-069) stays "
                "referenceable as legend in open entries; the tiering is unchanged.",
    "MCD-1902": " Batch 379 note: the Karkosa Heist is the Trinity's first use on the page for a reader, and "
                "entries that show the Trinity in use sit in the Book 1 unlock tier until Book 1 is published "
                "(VB-069).",
    "MCD-1907": " Batch 379 note: the second attempt is the first full showing of the Trinity in combat (VB-069).",
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
MS = ["chronicle-i-the-scrip-forge-raid.md", "chronicle-ii-the-dredge-line-ambush.md",
      "chronicle-iv-iron-shallows.md", "chronicle-v-the-siege-of-maw-9.md",
      "chronicle-vii-the-siege-of-the-ghost-harbor.md"]

EDITS = [
    # --- era fixes: narrative prose ---
    (RECAP, "P", "the Trinity and the loadout together produced", "the loadout produced", 1),
    (ORDER, "P", "before committing the Trinity to a timing window", "before committing his kit to a timing window", 1),
    (ORDER, "P", "had verified before the Trinity moved.", "had verified before Kanja moved.", 1),
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
     "  density-scaled physical power. The gear is the Trinity until the surrender at the Sovereign Pier (age 30,\n"
     "  `MCD-246`) and the post-Mafesto kit with the Rexmar Machete from then on (`ARS-344` through `ARS-356`);\n"
     "  the Trinity returns only at the Karkosa Heist in Book 1 (`MCD-1902`).", 1),
    (KJ, "D",
     "**Gate cleared:** YES, 2026-09-28 — Chronicle prose may now be drafted for this track.\n",
     "**Gate cleared:** YES, 2026-09-28 — Chronicle prose may now be drafted for this track.\n"
     "**Book 1 unlock tier (`VB-069`, Batch 379):** every entry of this track, and the eight manuscript\n"
     "Chronicles, is filed in the Book 1 unlock tier (Onyx narrates them). Each keeps its standing and none is\n"
     "rewritten; the archive holds them until Book 1 is published. New entries of this track are written for the\n"
     "tier and added to `docs/lords-of-cian/archive/book1-unlock-trinity-manifest.md` in the batch that locks them.\n", 1),
    # --- the series template: the gate step carries the bar ---
    (TPL, "D",
     "  draft is presented with a connective-tissue note. The Section 1 findings above must be resolved\n"
     "  or queued before this gate clears.\n",
     "  draft is presented with a connective-tissue note. The Section 1 findings above must be resolved\n"
     "  or queued before this gate clears.\n"
     "- **Trinity on-page bar (`VB-069`, Batch 379):** before Book 1 is published, no entry for release shows\n"
     "  the Trinity (Mafesto, Onyx of Oblivion, Obsidian Malice) in use on the page. The draft's\n"
     "  connective-tissue note says whether it does. An entry that does, or that Onyx narrates, is written\n"
     "  for the Book 1 unlock tier and added to `docs/lords-of-cian/archive/book1-unlock-trinity-manifest.md`\n"
     "  in the batch that locks it. The Trinity may be named, and told through legend, rumor, aftermath,\n"
     "  survivors' accounts and SBD Dossiers, in any entry.\n", 1),
    # --- the tracker ---
    (TRK, "D",
     "\n## Alias Chronicle track (Kanja's 11 aliases)\n",
     "\n**Book 1 unlock tier (`VB-069`, Batch 379).** The seven entries above and the eight manuscript Chronicles are\n"
     "filed in the Book 1 unlock tier (Onyx narrates them), and so are 175 Alias entries that show the Trinity in use\n"
     "or could not be read either way (Bane 23, Blue-Collar Titan 30, Captain 5, Crow King 5, Iron Bastard 17,\n"
     "Lord of Embers 37, Scourge 1, Sovereign Ghost 23, Storm That Walks 13, Trench Monarch 21, Industrial Myth 0).\n"
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
     "Abad accepted the gate recommendations; they are locked as `VB-069`, and the gated entries are listed in\n"
     "`docs/lords-of-cian/archive/book1-unlock-trinity-manifest.md` (190 entries: 172 IN-USE, 15 TRACK, 3\n"
     "AMBIGUOUS-GATED; the three withdrawn Chronicles IX to XI are not listed). The three ERA-ERROR candidates of\n"
     "section 3 resolved as follows. `the-recapture-at-dusk` (`MCD-1238`) and `the-order-he-didnt-question`\n"
     "(`MCD-589`) were era errors and are corrected to the Long-Mask-era kit; neither shows the Trinity now.\n"
     "`the-call-he-got-wrong` (`MCD-594`) is read as Rebellion era from its place in the Captain track's early\n"
     "waves (wave 19 of that track is the Rebellion's close, `MCD-1004`; its header states no era), so it is not\n"
     "treated as an error and stays in the manifest as IN-USE; Abad is asked to confirm the era. A second\n"
     "scan of all 172 IN-USE files for post-Mafesto kit, ages above 30 and Long Mask mentions found no further\n"
     "era error. The one hit with \"age 33\", `the-white-that-took-the-map-away` (`MCD-1391`), carries it in a\n"
     "header correction note about when Sovereign Eyes is built; the entry itself is a Bane entry inside the\n"
     "Rebellion window.", 1),
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
     "  use, and every entry Onyx narrates, sit in the Book 1 unlock tier, listed in\n"
     "  `docs/lords-of-cian/archive/book1-unlock-trinity-manifest.md`; a new such entry joins the list in the batch\n"
     "  that locks it. Gated entries keep their standing and are not rewritten.\n", 1),
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
    ORDER: " Corrected Batch 379, 2026-10-06: two lines that still had the Trinity committed to the forecast "
           "('committing the Trinity to a timing window', 'before the Trinity moved') now name Kanja and his kit, "
           "matching the Batch 321 swap to the Long-Mask-era kit; the Trinity stays sealed at L9 through the "
           "Long Mask (`MCD-246`, `VB-069`).",
}


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
    assert len(ents) == m["counts"]["total"] == 190, len(ents)
    cls = Counter(e["reason"] for e in ents)
    assert cls == {"IN-USE": 172, "TRACK": 15, "AMBIGUOUS-GATED": 3}, cls
    files = [e["file"] for e in ents]
    assert len(set(files)) == len(files), "duplicate manifest file"
    for e in ents:
        assert os.path.exists(CH + e["file"]), e["file"]
        if e["rule"]:
            assert byid[e["rule"]]["status"] == "locked", e["rule"]
        else:
            assert e["file"].startswith("chronicle-"), e["file"]
    for gone in ("the-recapture-at-dusk.md", "the-order-he-didnt-question.md"):
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
                 "is your feedback'; then 'all recommendations, run the census' (answering a list whose item 7 was "
                 "'What pre-Book-1 entries may say. Should they be able to describe what the weapons do as legend? I "
                 "recommend yes. The alternative is that they only mention the weapons exist.' and whose item 8 was "
                 "'The census.'); then 'all yes on yiu 6 questions' ('yiu' reads 'you'; question 6 was 'Batch 379. "
                 "Should I draft the Trinity rule, the lock list and the two era fixes once 378 is locked?'). "
                 "VB-069 locks the bar (no entry open to readers shows the Trinity in use before Book 1 is "
                 "published), what an open entry may do (name the Trinity; legend, rumor, aftermath, survivors' "
                 "accounts and SBD Dossiers, which may be wrong; legend may describe what the weapons do), Onyx "
                 "narrating as the Trinity appearing (the Kanja-version track gates, and the eight manuscript "
                 "Chronicles gate as a set), the Book 1 unlock tier and its manifest, the Karkosa Heist as the "
                 "first use on the page for a reader (MCD-1902, MCD-070) with MCD-1907 as the first full showing, "
                 "that gated entries are not rewritten, and that the gate binds archive publication and new "
                 f"entries, not the canon status of gated entries. The manifest lists {n_manifest} entries (172 "
                 "IN-USE, 15 TRACK, 3 AMBIGUOUS-GATED). Era errors corrected: the-recapture-at-dusk (MCD-1238) and "
                 "the-order-he-didnt-question (MCD-589); the-call-he-got-wrong (MCD-594) is Rebellion era and "
                 "stays. kanja-haku-rexmar.md corrected (the Trinity is the gear to age 30 only). Pointer notes "
                 "appended to: " + ", ".join(sorted(amended)) + ". Files carried: " + ", ".join(files)
                 + f". Abad's approval, verbatim: \"{approval}\"."),
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
    c = c.replace(anchor, anchor + f"""
**Batch 379: the Trinity on-page bar and the Book 1 unlock tier (`VB-069`).** Abad: "{approval}"
- **The ruling.** Abad, 2026-10-06: "after the Karkosa Heist, with the Trinity. which is important we build up
  the fact that the trinity doesn't get used until after book one is published which means we may have to keep
  some of the Chronicles locked in the archive. cuz the way I'm thinking, wouldn't it be clever or better for the
  Trinity not to make an appearance at all pre-book one but be spoken about in all and not giving away the stories
  where he's actually using it like the 90 seconds his father Witnesses or the battles in which he uses the
  trinity? what is your feedback". He then accepted the recommendations put to him: "all recommendations, run the
  census" (his list included "**What pre-Book-1 entries may say.** Should they be able to describe what the
  weapons do as legend? I recommend yes. The alternative is that they only mention the weapons exist." and "**The
  census.**") and "all yes on yiu 6 questions" ("yiu" reads "you"; question 6: "**Batch 379.** Should I draft the
  Trinity rule, the lock list and the two era fixes once 378 is locked?").
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
  none is rewritten. New entries for release before Book 1 follow the bar. The first use on the page is the
  Karkosa Heist (`MCD-1902`, `MCD-070`) and the first full showing in combat is the second attempt (`MCD-1907`).
  An entry set between the Pier and the Heist that shows the Trinity in use is an era error, corrected and not
  gated (`MCD-246`). The prefix is `VB-` because the rule governs how entries are written and filed, as
  `VB-062`, `VB-063`, `VB-067` and `VB-068` do; the world facts it leans on stay in `MCD-`.
- **The manifest.** `docs/lords-of-cian/archive/book1-unlock-trinity-manifest.md`, with a `.json` copy, lists
  {n_manifest} entries: 172 IN-USE, 15 TRACK (7 Kanja-version, 8 manuscript), 3 AMBIGUOUS-GATED (the duel
  `MCD-1425`, the twelve locks `MCD-729`, the well `MCD-1144`). The three withdrawn Chronicles IX to XI are not
  listed, since a withdrawn entry never publishes. The 76 OPEN-MENTION entries stay open, the eight borderline
  ones among them (Abad: "all recommendations"). The census is `research/trinity-on-page-census-2026-10-06.md`.
- **Era errors.** `the-recapture-at-dusk` (`MCD-1238`, Scourge, age 172) credited the guards' collapse to "the
  Trinity and the loadout together"; `the-order-he-didnt-question` (`MCD-589`, Storm That Walks, Long Mask) still
  had the Trinity committed to the forecast in two lines. Both are corrected to the Long-Mask-era kit as
  Batches 314 and 321 did, with a correction clause in each entry and each rule. `the-call-he-got-wrong`
  (`MCD-594`, Captain) is read as Rebellion era from its place in the early waves of that track, its header
  stating no era, so it is not treated as an error and stays in the manifest. `kanja-haku-rexmar.md` no longer
  says the gear from 18 to 314 is the Trinity.
- **Covered only by Abad's final approval, which presented each item explicitly.** (a) New entries of the
  Kanja-version track are written for the tier, and the unlock is eligibility when Book 1 is published, subject
  to the archive's review, matching Phase 5 of the archive game plan (`VB-069`, items 4 and 5). (b) The first
  full showing in combat is `MCD-1907`, with the Heist's own fighting left open. (c) "The 3 AMBIGUOUS entries"
  are the duel, the twelve locks and the well; the other two of the census's five are the era errors.
  (d) `the-call-he-got-wrong` read as Rebellion era from its place in the Captain waves, its header stating no
  era. (e) Kanja Chronicle II gates with its track although it holds no Trinity and no Onyx. (f) The three
  withdrawn Chronicles IX to XI are not listed. (g) Legend describes what the weapons do at the level of effect
  and in the teller's own terms. (h) A told or recorded account may not stage the use as a scene, whatever the
  frame. (i) The name "Book 1 unlock tier" is kept although the archive already carries clearance levels and a
  T0 to T4 classification; the tier is a book placement.
- **Propagation.** {len(amended)} rule statements carry pointer or correction notes; {n_entries} entries and
  {n_docs} docs carried (the five manuscript headers' gate pointer, the Kanja profile, the series template, the
  tracker, the census, this file's standing sections, the manifest's status lines). The mirrored Voice Bible and Voice Progression Sheet stay
  unedited; the archive repo's Phase 5 plan is owed an update to name the manifest.
Ledger at `ledger_version` 38.1, {len(d['rules']):,} rules, 379 batches.
""")
    open("CLAUDE.md", "w", encoding="utf-8").write(c)

    d = json.load(open(LEDGER, encoding="utf-8"))
    dup = [k for k, v in Counter(r["id"] for r in d["rules"]).items() if v > 1]
    print("duplicates:", dup, "| total rules:", len(d["rules"]), "| version:", d["ledger_version"],
          "| rules amended:", len(amended), "| files edited:", len(files))


if __name__ == "__main__":
    main()
