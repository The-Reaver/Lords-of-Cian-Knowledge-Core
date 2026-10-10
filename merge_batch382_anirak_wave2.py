"""Batch 382: Anirak Collections IV and V (MCD-1911, MCD-1912), her second wave.
Usage: python3 merge_batch382_anirak_wave2.py "<approval quote>"
"""
import json
import sys
from collections import Counter

LEDGER = "canon-ledger.json"
CH = "docs/lords-of-cian/chronicles/"
DOCS = "docs/lords-of-cian/"
TODAY = "2026-10-10"
DIRECTION = "go ahead with Anirak's two Collections"
SOURCE = "Original invention, chat-drafted 2026-10-10, no source document"
C4 = CH + "anirak-collection-iv-a-place-to-stand.md"
C5 = CH + "anirak-collection-v-what-he-did-in-the-dark.md"

NEW = [
    ("MCD-1911", "Anirak Collection IV, 'A Place to Stand' (full text at "
     "docs/lords-of-cian/chronicles/anirak-collection-iv-a-place-to-stand.md). Fourth entry of Anirak's Collections, "
     "opening her second wave, close-third per VB-065. Roughly Kanja 303, about three years after Ren comes aboard "
     "(MCD-1900): a Trust landing party comes for the harbor of Windbreak, a Southern Sweep settlement (MCD-255), "
     "with a ram-cart on the mole. The Captain's word reaches her by the bosun and he stays off the page. She commands "
     "her three (Edda, Hamund, Odile, MCD-1890) and Ren, and it is Ren's first use of his active field against people "
     "(CC-101, ARS-446). Her three hold back of his ring, so the reserved payoff of her three inside Ren's field is "
     "untouched. Her combinations are staged at Warm only (ARS-438 to ARS-447). Terms are given once; six run and are "
     "not struck, four sit, the landing captain is disarmed and sits, and two on the harbor wall are taken alive (CC-164). "
     "No kill, no marquee kill spent (MCD-1881). The mole's pad is cracked; the harbor-master's 'Cutters. Masons. By "
     "autumn.' and her 'By autumn.' commit the fleet's labor to its mending. New minor local geography: the mole, its "
     "elbow pad, the harbor gate. No new named characters. Clean on independent review."),
    ("MCD-1912", "Anirak Collection V, 'What He Did in the Dark' (full text at "
     "docs/lords-of-cian/chronicles/anirak-collection-v-what-he-did-in-the-dark.md). Fifth entry of Anirak's "
     "Collections, closing her second wave, close-third per VB-065. Roughly Kanja 304, some months after Windbreak "
     "(MCD-1911): Wystan of Windbreak, a new named character, adult (twenty-six), a harbor-watch hand who hauled stone "
     "on the mole under the fleet's masons and then signed aboard, serves her unasked. She sets him the night's work "
     "on the rudder tackle; a squall comes in the last watch and his pintle strap holds. She still cannot read why he "
     "serves her, since the Siren tells her nothing about motive (CC-112), and she tells him to keep her lamp. Her doubt "
     "stays open (anirak.md Section 2). No fight, no kill. Edda and Hamund appear; Odile and Ren do not; the Captain is "
     "off the page, and the ship and helmsman stay unnamed. Clean on independent review."),
]


def file_edits(approval):
    old = ('*UNLOCKED / PENDING APPROVAL. Draft, 2026-10-10. Wave 2, drafted on Abad\'s direction "go ahead with '
           'Anirak\'s two Collections" (2026-10-10).')
    hdr = ('*Locked canon, Batch 382, {d} (`{rid}`). Clean on independent review. Abad\'s approval: "{a}". Wave 2, '
           'drafted on Abad\'s direction "go ahead with Anirak\'s two Collections" (2026-10-10).')
    prof = DOCS + "character-profiles/anirak.md"
    road = DOCS + "archive-roadmap-2026-10-02.md"
    return [
        (C4, old, hdr.format(d=TODAY, rid="MCD-1911", a=approval), 1),
        (C5, old, hdr.format(d=TODAY, rid="MCD-1912", a=approval), 1),
        (prof, "**Status:** wave 1 locked (Batch 373, `MCD-1898`-`MCD-1900`, 2026-10-04)",
         "**Status:** wave 2 locked (Batch 382, `MCD-1911`-`MCD-1912`, 2026-10-10); wave 1 locked (Batch 373, "
         "`MCD-1898`-`MCD-1900`, 2026-10-04)", 1),
        (prof, "Kanja 304, a new hand tested on a night watch, no fight). Pending Abad's approval.",
         f"Kanja 304, a new hand tested on a night watch, no fight). Approved and locked, Batch 382: \"{approval}\".", 1),
        (prof, "  aboard, the one face that leaves her and comes back loose; she walks into his ring and takes him as\n"
         "  her charge. No fight.\n",
         "  aboard, the one face that leaves her and comes back loose; she walks into his ring and takes him as\n"
         "  her charge. No fight.\n"
         "- **IV, \"A Place to Stand\"** (`MCD-1911`, Batch 382). ~Kanja 303, Windbreak: a Trust landing party with a\n"
         "  ram-cart on the mole; Ren's first use of his field against people while her three hold back of his\n"
         "  ring. Terms once, six run, the captain sits. No kill.\n"
         "- **V, \"What He Did in the Dark\"** (`MCD-1912`, Batch 382). ~Kanja 304, at sea: Wystan of Windbreak\n"
         "  serves her unasked; his strap holds through a squall and she still cannot read why. No fight.\n", 1),
        (DOCS + "chronicle-tracks-status.md",
         "wave 1 locked (Batch 373, `MCD-1898`-`MCD-1900`, 2026-10-04) | 3 Collections (I-III);",
         "wave 1 locked (Batch 373, `MCD-1898`-`MCD-1900`, 2026-10-04); wave 2 locked (Batch 382, `MCD-1911`-"
         "`MCD-1912`, 2026-10-10) | 5 Collections (I-V);", 1),
        (road, "| Anirak: the Collections | 3 | 0 |", "| Anirak: the Collections | 5 | 0 |", 1),
        (road, "| Ezio: the Exhibits | 1 (3 more drafted, not locked) | 0 |", "| Ezio: the Exhibits | 4 | 0 |", 1),
        (road, "Anirak holds three\n  Collections (+2). Ezio holds one locked Exhibit with three drafted (+1 if the "
         "drafts are approved).",
         "Anirak holds five\n  Collections (done, Batch 382). Ezio holds four locked Exhibits (+1).", 1),
    ]


CLAUDE_ANCHOR = "Ledger at `ledger_version` 38.3, 2,740 rules, 381 batches.\n"


def claude_para(approval):
    return (
        "\n**Batch 382: Anirak's second wave (`MCD-1911`, `MCD-1912`).** Abad's direction: "
        f"\"{DIRECTION}\"; approval: \"{approval}\". Drafted on Sonnet, reviewed on Opus, fixed, clean on re-check.\n"
        "- **IV, \"A Place to Stand\"** (~Kanja 303). A Trust landing party at Windbreak's mole; Ren's first use of "
        "his field against people. Her three hold back of his ring. No kill.\n"
        "- **V, \"What He Did in the Dark\"** (~Kanja 304). Wystan of Windbreak (new, adult) serves her unasked; his "
        "strap holds in a squall, and she still cannot read his motive. No fight.\n"
        "- Anirak now holds five Collections, her launch count under the archive upload plan.\n"
        "Ledger at `ledger_version` 38.4, 2,742 rules, 382 batches.\n"
    )


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    approval = sys.argv[1]
    d = json.load(open(LEDGER, encoding="utf-8"))
    rules = {r["id"]: r for r in d["rules"]}
    for rid, _ in NEW:
        assert rid not in rules, rid
    for rid, st in NEW:
        d["rules"].append({"id": rid, "category": "anirak-collections", "statement": st, "status": "locked",
                           "source": SOURCE})
    d["batches_completed"].append({
        "batch": 382,
        "source": SOURCE + "; full texts at " + C4 + " and " + C5,
        "rules_affected": [r for r, _ in NEW],
        "note": ("Anirak's second wave locked: Collection IV 'A Place to Stand' (MCD-1911, ~Kanja 303, Windbreak, Ren's "
                 "first use of his field against people, no kill) and Collection V 'What He Did in the Dark' (MCD-1912, "
                 "~Kanja 304, Wystan of Windbreak, no fight). Drafted on Sonnet, reviewed on Opus, fixed, clean on "
                 f"re-check. Abad's direction, verbatim: '{DIRECTION}'. Approval, verbatim: '{approval}'."),
    })
    d["ledger_version"] = "38.4"
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
