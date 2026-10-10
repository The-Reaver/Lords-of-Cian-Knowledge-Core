"""Batch 381: Mirza, the state and its army, the Axiom (MRZ-001 to MRZ-007), and the writing rule VB-070.
New prefix MRZ-. Draft: docs/lords-of-cian/drafts/2026-10-11-mirza-rules.md (revision 2, clean on review).
Usage: python3 merge_batch381_mirza.py "<approval quote>"
"""
import json
import re
import sys
from collections import Counter

LEDGER = "canon-ledger.json"
DOCS = "docs/lords-of-cian/"
DRAFT = DOCS + "drafts/2026-10-11-mirza-rules.md"
PLAN = DOCS + "drafts/2026-10-10-mirza.md"
TODAY = "2026-10-10"
PLACEMENT = ("Mirza's crown signs the pact while its science army tries to buy the doctrine. This is the richest "
             "option, and it gives Mirza an inner conflict from the start.")
DRAFT_APPROVAL = "Approved"
SOURCE = "Original invention, chat-drafted 2026-10-10, no source document"
IDS = ["MRZ-001", "MRZ-002", "MRZ-003", "MRZ-004", "MRZ-005", "MRZ-006", "MRZ-007", "VB-070"]


def parse_draft():
    text = open(DRAFT, encoding="utf-8").read()
    out = []
    for rid in IDS:
        m = re.search(r"### " + rid + r"\n\n- \*\*category:\*\* `([^`]+)`\n- \*\*statement:\*\* (.*?)\n\n", text, re.S)
        assert m, rid
        st = " ".join(m.group(2).split())
        st = st.replace("`", "").replace("*The Ledger*", "The Ledger")
        assert "*" not in st and "`" not in st, rid
        out.append((rid, m.group(1), st))
    return out


APPEND = {
    "MCD-490": " Batch 381 note: the foreign sea nation of this entry is Mirza (MRZ-001); the entry stands as written.",
    "MCD-1040": (" Batch 381 note: the foreign sea nation of this entry is Mirza, and the pact is its crown's own "
                 "course (MRZ-001); the entry stands as written."),
    "MCD-1414": (" Batch 381 note: the foreign crown and sovereign of this entry are Mirza's, and the royal corps is a "
                 "corps of the Axiom (MRZ-004); the entry stands as written, and the depot mystery's culprit stays "
                 "unassigned."),
    "MCD-1893": " Batch 381 note: the Foreign Sea nation is named Mirza (MRZ-001, MRZ-002).",
    "VB-004": (" Batch 381 note: the comic registers this rule allows do not extend to the name or the title of "
               "Mirza (VB-070)."),
    "VB-068": (" Batch 381 note: the registers this rule names do not extend to the name or the title of Mirza "
               "(VB-070)."),
}


def file_edits(approval):
    return [
        (DRAFT,
         "*Draft for Abad's approval, revision 2, dated 2026-10-10. Nothing here is locked.",
         f"*Locked, Batch 381, {TODAY}. Abad's approval of the draft: \"{DRAFT_APPROVAL}\"; lock: \"{approval}\". "
         "The reading of question 1 in section 6 is the text of `MRZ-004` as approved; questions 2 to 10 stay open. "
         "Revision 2, dated 2026-10-10.", 1),
        (DRAFT,
         "The Connective-Tissue Gate still owes its independent review of this\nrevision before it is presented as final.*",
         "Clean on independent review of this revision.*", 1),
        (PLAN,
         "*Abad's direction, 2026-10-07 to 2026-10-10. Nothing here is locked. Rule text gets drafted once the open\n"
         "choices below are made, then goes through the Connective-Tissue Gate.*",
         "*Superseded by the locked rules `MRZ-001` to `MRZ-007` and `VB-070` (Batch 381; draft at\n"
         "`docs/lords-of-cian/drafts/2026-10-11-mirza-rules.md`). Where these notes differ, the locked rules control:\n"
         "no institution takes \"of Mirza\", and no Archive or Tribunal exists. Abad's direction, 2026-10-07 to "
         "2026-10-10.*", 1),
        (DOCS + "character-profiles/alias-sovereign-ghost.md",
         "formal, then sustained bilateral acknowledgment (`MCD-490`, `MCD-1040`);",
         "formal, then sustained bilateral acknowledgment (`MCD-490`, `MCD-1040`; the nation is Mirza,\n"
         "  `MRZ-001`, Batch 381);", 1),
        ("CLAUDE.md", "`PH2`, `LEX`. A new", "`PH2`, `LEX`, `MRZ`. A new", 1),
        ("CLAUDE.md",
         "each locked as its own rule per `VB-068`)",
         "each locked as its own rule per `VB-068`; `MRZ-` was claimed 2026-10-10, Batch 381, for the state of "
         "Mirza and its army, the Axiom, a new institution kept apart from mainline Cian material)", 1),
    ]


CLAUDE_ANCHOR = "Ledger at `ledger_version` 38.2, 2,732 rules, 380 batches.\n"


def claude_para(approval):
    return (
        "\n**Batch 381: Mirza, the Axiom and the writing rule (`MRZ-001`-`MRZ-007`, `VB-070`).** Abad's placement: "
        f"\"{PLACEMENT}\"; approval of the draft: \"{DRAFT_APPROVAL}\"; lock: \"{approval}\". New prefix `MRZ-`. "
        "Drafted, then clean on independent review at revision 2.\n"
        "- **The state.** Mirza is the unnamed foreign sea nation of `MCD-490` and `MCD-1040`, under a crown "
        "that is an office. It lies within ordinary sailing reach of Cian, off the Atlas grid, and is not the "
        "fourth continent; its geography stays open (`MRZ-001`, `MRZ-002`).\n"
        "- **The army.** The Axiom: Postulants, Theorem as a rank only, a campaign \"a proof\", a won war "
        "\"proven\" (unrelated to the Proven density tier). Two schools, the Fulcrum and the Prism. Its science "
        "stays inside this world's physics and tech level (`MRZ-003`, `MRZ-006`).\n"
        "- **The conflict.** The royal corps of `MCD-1414` is the Axiom's. That sovereign sent the envoy, and "
        "the offer runs against the crown's own course of `MCD-1040`. The depot mystery keeps its culprit "
        "unassigned (`MRZ-004`). Other foreign contacts stay unidentified (`MRZ-007`).\n"
        "- **The title.** \"Of Mirza\" is only an earned title for proven scholar-soldiers, and \"Axiom of "
        "Mirza\" appears only in formal documents. \"Mirza is marching\" is outsiders' dialogue only (`MRZ-005`). "
        "`VB-070`: the name and the title are never comic in prose; enemies may mock them in dialogue.\n"
        "- **Owed.** `research/atlas-rebuild/mainline-gazetteer.json` (its \"Foreign Sea\" entry) awaits the "
        "same regeneration from the ledger recorded at Batch 378. Still open for Abad: what counts as proven for "
        "the title, whether the crown knows the Iron Bastard and the Ghost are one man, and the Kairo name.\n"
        "Ledger at `ledger_version` 38.3, 2,740 rules, 381 batches.\n"
    )


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    approval = sys.argv[1]
    new = parse_draft()
    d = json.load(open(LEDGER, encoding="utf-8"))
    rules = {r["id"]: r for r in d["rules"]}
    for rid, _, _ in new:
        assert rid not in rules, rid
    for rid, add in APPEND.items():
        assert add not in rules[rid]["statement"], rid
        rules[rid]["statement"] += add
    for rid, cat, st in new:
        d["rules"].append({"id": rid, "category": cat, "statement": st, "status": "locked", "source": SOURCE})
    d["batches_completed"].append({
        "batch": 381,
        "source": SOURCE + "; draft " + DRAFT,
        "rules_affected": IDS + list(APPEND),
        "note": ("Mirza locked under the new MRZ- prefix: the state, its army the Axiom and its two schools, the "
                 "earned title 'of Mirza', and the writing rule VB-070. Clean on independent review at revision 2. "
                 f"Abad's placement ruling, verbatim: '{PLACEMENT}'. Approval of the draft, verbatim: "
                 f"'{DRAFT_APPROVAL}'. Lock, verbatim: '{approval}'."),
    })
    d["ledger_version"] = "38.3"
    d["last_updated"] = TODAY
    json.dump(d, open(LEDGER, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    open(LEDGER, "a").write("\n")

    files = set()
    for path, old, new_s, n in file_edits(approval):
        s = open(path, encoding="utf-8").read()
        assert s.count(old) == n, (path, old, s.count(old))
        open(path, "w", encoding="utf-8").write(s.replace(old, new_s))
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
