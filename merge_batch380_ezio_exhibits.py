"""Batch 380: Ezio Exhibits II-IV (MCD-1908 to MCD-1910) and approval-list items 4, 6 and 7
(MCD-268, CC-028, CC-027 amended). Draft: docs/lords-of-cian/drafts/2026-10-10-ezio-exhibits-ii-iv.md.
Usage: python3 merge_batch380_ezio_exhibits.py "<approval quote>"
"""
import json
import sys
from collections import Counter
from datetime import date

LEDGER = "canon-ledger.json"
CH = "docs/lords-of-cian/chronicles/"
DOCS = "docs/lords-of-cian/"
TODAY = "2026-10-10"
RULINGS = 'items 4, 6 and 7 "Yes" to all three'
SOURCE = ("Original invention, chat-drafted 2026-09-30, refreshed 2026-10-09, no source document; "
          "approval-list rulings in conversation, 2026-10-10")

E2 = CH + "ezio-exhibit-ii-the-question-he-waited-twenty-years-to-ask.md"
E3 = CH + "ezio-exhibit-iii-what-the-patron-never-says.md"
E4 = CH + "ezio-exhibit-iv-what-valen-never-let-slip.md"

NEW = [
    ("MCD-1908", "Ezio Exhibit II, 'The Question He Waited Twenty Years to Ask' (full narrative text at "
     "docs/lords-of-cian/chronicles/ezio-exhibit-ii-the-question-he-waited-twenty-years-to-ask.md). The Series: "
     "Ezio's Exhibits; teller Fermand Aurelias (CC-034, VB-024). Dramatizes Lauris Letitia's recruitment from "
     "Ezio's side (MCD-194): roughly two decades of reading her reports, three moments he judged acting would "
     "cost her more than waiting, and a single after-action phrase that decided him. She leaves the Directorate "
     "on her own; some two months later, while she moves between Aerelin's safe-houses (MCD-193, MCD-267), he "
     "arranges the meeting at a private coastal residence through Aerelin's mediation. Fermand withdraws to a "
     "side room. Ezio reports afterward the Sephtis-archive briefing, the Attia role, her three conditions "
     "accepted without amendment, and one subject the two agreed to say nothing further on, which he does not "
     "name. Fermand learns of the file only when asked to accompany him (CC-027 and MCD-268 as amended Batch "
     "380). No new named characters. Strictly pre-Book-1."),
    ("MCD-1909", "Ezio Exhibit III, 'What the Patron Never Says' (full narrative text at "
     "docs/lords-of-cian/chronicles/ezio-exhibit-iii-what-the-patron-never-says.md). The Series: Ezio's "
     "Exhibits; teller Fermand Aurelias. An ordinary handoff from Lady Nadea Thren (MCD-021, CC-029, CC-073): a "
     "Trust auditor in the Lawless Reaches, a three-month window, a briefing of a few words. As they leave she "
     "tells Ezio he looks tired; he does not answer. Fermand records a stillness between them whose content he "
     "does not know and asks for no account of it. States nothing of what either knows or feels, and neither "
     "touches nor foreshadows MCD-1875. No new named characters. Strictly pre-Book-1."),
    ("MCD-1910", "Ezio Exhibit IV, 'What Valen Never Let Slip' (full narrative text at "
     "docs/lords-of-cian/chronicles/ezio-exhibit-iv-what-valen-never-let-slip.md). The Series: Ezio's Exhibits; "
     "teller Fermand Aurelias. At a dockside house Valen keeps, a drunk merchant's factor speaks of combatants "
     "the Directorate cannot rate and turns to Ezio; Valen's laugh, placed at the exact moment, pulls the room's "
     "attention away, three times that evening. Ezio tells Fermand that Valen has done it since Ezio first put "
     "the face on, and that Valen chose the guarding himself. Fermand learns that Valen guards Ezio's cover and "
     "does not learn what it hides (WC-016, CC-026, CC-108, CC-027 as amended Batch 380). No new named "
     "characters. Strictly pre-Book-1."),
]

REPLACE_STATEMENT = {
    "CC-028": ("Ezio Valcari is roughly 308 years old at the Fulfillment Ceremony, five years younger than Kanja, "
               "who is 313 there (MCD-1901); he was about sixteen at the Furnace District Strike (MCD-373). He has "
               "750 years of wisdom-equivalence gained through training under Sephtis. Amended Batch 380 from an "
               "earlier '75', per approval-list item 6."),
}
APPEND = {
    "CC-027": (" Batch 380 note: Fermand Aurelias knows that Ezio keeps a cover and that Valen guards it, and does "
               "not know what it hides; he is not a sixth knower (approval-list item 7)."),
    "MCD-268": " Amended Batch 380, per approval-list item 4.",
}
SUBS = {
    "MCD-268": [
        ("Fermand Aurelias's escape (age 270)",
         "Fermand Aurelias's escape (Kanja age about 112, about two years before Lauris's recruitment, MCD-194)"),
        ("extraction coordinates delivered by Ghostwind",
         "extraction coordinates delivered by a Ghost-Lattice courier (Ghostwind is not recruited until Kanja "
         "age 130, MCD-258)"),
    ],
}


def file_edits(approval):
    hdr = ('*Locked canon, Batch 380, {d} (`{rid}`). Clean on independent review. Abad\'s approval: "{a}". '
           'Teller and rulings: approval-list items 4, 6 and 7, "{r}".')
    old = "*UNLOCKED / PENDING APPROVAL. Draft, 2026-10-09."
    return [
        (E2, old, hdr.format(d=TODAY, rid="MCD-1908", a=approval, r=RULINGS), 1),
        (E3, old, hdr.format(d=TODAY, rid="MCD-1909", a=approval, r=RULINGS), 1),
        (E4, old, hdr.format(d=TODAY, rid="MCD-1910", a=approval, r=RULINGS), 1),
        (E2, "approval-list item 7, pending; `VB-067`", "`CC-027` as amended Batch 380; `VB-067`", 2),
        (DOCS + "character-profiles/ezio-valcari.md",
         "- `CC-028` — 75 years old (present-day/Book 1 timeline), with 750 years of wisdom-equivalence",
         "- `CC-028` — roughly 308 at the Fulfillment Ceremony, five years younger than Kanja (amended "
         "Batch 380 from 75), with 750 years of wisdom-equivalence", 1),
        (DOCS + "chronicle-tracks-status.md",
         "| wave 1 locked | 1 (own series, `MCD-1876`)",
         "| wave 2 locked | 4 (own series, `MCD-1876`, `MCD-1908`-`MCD-1910`)", 1),
        (DOCS + "approval-list-2026-10-03.md", "**4. When Fermand joined.**",
         "**4. When Fermand joined. RESOLVED, Batch 380 (`MCD-268`): about Kanja 112.**", 1),
        (DOCS + "approval-list-2026-10-03.md", "**6. Ezio's true age.**",
         "**6. Ezio's true age. RESOLVED, Batch 380 (`CC-028`): about 308.**", 1),
        (DOCS + "approval-list-2026-10-03.md",
         "**7. Is Fermand a sixth person who knows Ezio's classified capability?**",
         "**7. Is Fermand a sixth person who knows Ezio's classified capability? RESOLVED, Batch 380 "
         "(`CC-027`): no.**", 1),
    ]


CLAUDE_ANCHOR = "Ledger at `ledger_version` 38.1, 2,729 rules, 379 batches.\n"


def claude_para(approval):
    return (
        "\n**Batch 380: Ezio Exhibits II-IV (`MCD-1908`-`MCD-1910`) and approval-list items 4, 6 and 7.** "
        f"Abad: \"{RULINGS}\"; approval of the Exhibits: \"{approval}\". Drafted on Sonnet, reviewed on Opus "
        "(NOT CLEAN on all three, fixed, clean on re-check).\n"
        "- **Exhibit II** tells Lauris's recruitment from Ezio's side, after her own defection (`MCD-194`). "
        "**III** is a Nadea Thren handoff and stops short of `MCD-1875`. **IV** shows Valen guarding Ezio's cover.\n"
        "- **Rulings.** `CC-028`: Ezio is about 308 at the Ceremony, five years younger than Kanja. `CC-027`: "
        "Fermand knows a cover exists and that Valen guards it, not what it hides. `MCD-268`: Fermand escapes "
        "the Citadel at about Kanja 112, by a Ghost-Lattice courier, not Ghostwind.\n"
        "- Rests on approval-list item 2 (human lifespan), still open.\n"
        "Ledger at `ledger_version` 38.2, 2,732 rules, 380 batches.\n"
    )


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    approval = sys.argv[1]
    d = json.load(open(LEDGER, encoding="utf-8"))
    rules = {r["id"]: r for r in d["rules"]}
    for rid, _ in NEW:
        assert rid not in rules, rid
    for rid, st in REPLACE_STATEMENT.items():
        rules[rid]["statement"] = st
    for rid, pairs in SUBS.items():
        for a, b in pairs:
            assert rules[rid]["statement"].count(a) == 1, (rid, a)
            rules[rid]["statement"] = rules[rid]["statement"].replace(a, b)
    for rid, add in APPEND.items():
        assert add not in rules[rid]["statement"], rid
        rules[rid]["statement"] += add
    for rid, st in NEW:
        d["rules"].append({"id": rid, "category": "ezio-exhibits", "statement": st, "status": "locked",
                           "source": SOURCE})
    d["batches_completed"].append({
        "batch": 380,
        "source": SOURCE + "; draft docs/lords-of-cian/drafts/2026-10-10-ezio-exhibits-ii-iv.md",
        "rules_affected": [r for r, _ in NEW] + ["CC-028", "CC-027", "MCD-268"],
        "note": ("Ezio Exhibits II-IV locked; approval-list items 4, 6 and 7 ruled. Drafted on Sonnet, reviewed on "
                 "Opus: NOT CLEAN on all three at first review, fixed, clean on re-check. Abad's rulings, verbatim: "
                 f"'{RULINGS}'. Abad's approval of the Exhibits, verbatim: '{approval}'."),
    })
    d["ledger_version"] = "38.2"
    d["last_updated"] = TODAY
    json.dump(d, open(LEDGER, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    open(LEDGER, "a").write("\n")

    files = set()
    for path, old, new, n in file_edits(approval):
        s = open(path, encoding="utf-8").read()
        assert s.count(old) == n, (path, old, s.count(old))
        open(path, "w", encoding="utf-8").write(s.replace(old, new))
        files.add(path)
    c = open("CLAUDE.md", encoding="utf-8").read()
    assert c.count(CLAUDE_ANCHOR) == 1
    c = c.replace(CLAUDE_ANCHOR, CLAUDE_ANCHOR + claude_para(approval))
    open("CLAUDE.md", "w", encoding="utf-8").write(c)

    d = json.load(open(LEDGER, encoding="utf-8"))
    dup = [k for k, v in Counter(r["id"] for r in d["rules"]).items() if v > 1]
    print("duplicates:", dup, "| total rules:", len(d["rules"]), "| version:", d["ledger_version"],
          "| files edited:", len(files))


if __name__ == "__main__":
    main()
