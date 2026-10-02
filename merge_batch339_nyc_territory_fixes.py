#!/usr/bin/env python3
"""Batch 339: Fable-review fixes, the NYC homage-era Territory Chronicles.

A Fable-model agent did a read-only review of the NYC Territory Chronicles
(Xaragua, Areito, Yara, Guanin, Boriken, plus Arturo Salvatierra Duho's Five
Families thread) and produced exact contradiction/error fixes. Most were
prose-only corrections applied directly to the Chronicle .md files (no
ledger-statement change needed). This script applies only the handful of
fixes that require amending rule statements: PH2-061 and PH2-062 (updating
Arturo's and Yaisa's statements to record that Kanja paid off the long-arc
banter thread in Xaragua Chronicle VI, MCD-1093, without granting him parity
with Yaisa's own standing), and MCD-464 (updating its file-path reference
after the Chronicle file it describes was renamed to match the project's
established territory-Chronicle naming convention).

One finding (C-3, Xaragua Chronicle III's cohort death count) needs Abad's
own creative ruling and is deliberately left untouched, as are the two
no-fix-needed findings (N-2, N-3) and all enrichment items.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Fable-model read-only review of the NYC homage-era Territory Chronicles "
    "(Xaragua, Areito, Yara, Guanin, Borikén, plus Arturo Salvatierra Duho's "
    "Five Families thread) against the full ledger and corpus."
)

AMENDMENTS = {
    "PH2-061": (
        "Arturo 'de la Muerte' Salvatierra Duho leads the Five Families (PH2-060), a Xaragua "
        "native and the fourth homage-era comrade to guest-relate to Kanja, but in a "
        "structurally distinct role: not a one-off guest in a Kanja battle, but Kanja's standing "
        "point of contact across all five Batey territories. Two surnames per Abad's direction, "
        "and neither is incidental. Arturo Salvatierra -- both the given name and the surname -- "
        "is not his family's name; it is the name Spanish colonization imposed on his lineage "
        "generations back, when his ancestors were stripped of who they were and folded into the "
        "colonizer's own naming system. He kept it deliberately, not from resignation but as a "
        "standing reminder of exactly what is owed and to whom. Later in life he traced what "
        "colonization tried to erase -- falsified records, destroyed archives, generations who "
        "could not say their own clan's name aloud without danger -- and recovered Duho, his "
        "actual clan name, the one erasure was built to make sure no one would ever find again. "
        "He added it rather than replacing anything, so both truths sit in his name at once: what "
        "was done to his family, and what survived it anyway. His nickname is a reputation, not a "
        "description -- earned by what happens to people who threaten what's his, not by how he "
        "treats his own. Physics: a biochemical branch (per VB-005's mass/sound/pressure/chemistry "
        "backbone), not density-scaling -- his signature ability, 'Blood Debt,' has three faces: "
        "protective (wounds seal, toxins break down, bleeding stops near him or on anyone he's "
        "personally claimed), its dark reverse (catastrophic hemorrhage or organ failure on "
        "someone he's decided is finished, almost never used), and turned inward (his own aging "
        "arrested at a chosen point, explaining why a much older man still looks mid-40s). Cost: "
        "only works at close range -- a hand on a shoulder, a shared table -- not a "
        "battlefield-wide aura, meaning grievances get settled at his table because that's the "
        "only place his protection holds; and every true use of the reverse face visibly ages him, "
        "since his youth is a resource he spends, not a fact about him. Personality: a force of "
        "nature, very rarely outwitted, unflappable and commanding without ever being boastful; "
        "the one exception is playful banter with those who've earned it, which as of Xaragua "
        "Chronicle II is only Yaisa (PH2-062); Kanja later earns the same standing on his own "
        "terms in Xaragua Chronicle VI (MCD-1093). Toward anyone descended from the specific "
        "colonial lineage responsible for what was done to his own -- regardless of that "
        "individual's rank, danger, or personal innocence -- he is deliberately, purposefully "
        "adversarial, and enjoys being so; this is a chosen and ongoing position, not a loss of "
        "control, and his S-tier standing means consequence was never what held him back from it. "
        "He is fully aware that race as a category did not exist before the colonial system that "
        "invented it to organize who could take from whom -- he is not confused about the science "
        "of it, and he directs his war at the lineage that built and benefited from that invented "
        "structure anyway, because the categories may be constructed but the harm done using them "
        "was not. He carries none of this as complaint or unresolved rage; he made his peace with "
        "the choice long ago and has never once second-guessed it. Backstory: a tormented past "
        "that is the actual source of his authority -- as a young man in Xaragua he was one of a "
        "tight cohort of dock boys who were each other's real family; war took several overseas, "
        "and Xaragua's own street war took most of the rest while he was gone, until only he and "
        "Yaisa remained from that generation. He did not study the criminal world from above; he "
        "survived every rung of it in sequence on the way up, which is why he understands it "
        "better than anyone. The Five Families, and 'No Blood at My Table' specifically, are his "
        "direct answer to that decade -- a debt he is still paying, not resolved grief. First "
        "appears in Xaragua Chronicle II ('The Man at the Head of the Table'), granting the "
        "still-unnamed Kanja passage through all five Batey territories on tested behavior alone "
        "-- Kanja declines to give his name even here, and Arturo does not press, consistent with "
        "the unnamed-guest pattern across Ogoun Xarey's and Yalokona's own Chronicles. Paid off in "
        "Xaragua Chronicle VI (MCD-1093): Kanja earns a place among Arturo's small circle capable "
        "of unguarded banter, under the private nickname 'Guaikán,' without Arturo ever learning "
        "his name."
    ),
    "PH2-062": (
        "Yaisa is the sole other survivor of Arturo Salvatierra Duho's (PH2-061) original "
        "dock-boy cohort, the generation lost to war and Xaragua's own street war. Now his "
        "second-in-command, running the Five Families' day-to-day business while he handles what "
        "only he can. The only person alive who remembers him before he became 'de la Muerte,' and "
        "the one person whose opinion of him predates the reputation -- which is why she was, "
        "until Xaragua Chronicle VI (MCD-1093), the only one who could banter with him unguarded; "
        "Kanja's later standing is explicitly a different category (fondness with no history), not "
        "parity with hers. Appears silently in Xaragua Chronicle II, present at the room's edge, "
        "unnamed to the stranger and given no dialogue in that scene -- her role is established "
        "for the reader, not yet for the story's other occupant."
    ),
    "MCD-464": (
        "\"The Price She Wouldn't Let Them Pay\" (full narrative text at "
        "docs/lords-of-cian/chronicles/yara-chronicle-ii-the-price-she-wouldnt-let-them-pay.md), "
        "Yara Chronicle II. A developer offers full clinic funding in exchange for Yalokona's "
        "public silence on a displacing zoning variance; she refuses, the variance passes anyway "
        "and the clinic's funding is delayed eighteen months, dramatizing the real cost of "
        "'Unbought and Unbossed' (PH2-006) as a genuine defeat rather than a clean win. An unnamed "
        "Kanja is present in the gallery, uninvolved. No new named characters. Second Yara "
        "territory Chronicle."
    ),
}


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}

    amended = []
    for rid, new_statement in AMENDMENTS.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        rules_by_id[rid]["statement"] = new_statement
        amended.append(rid)

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule IDs found"

    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({
        "batch": next_batch,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": 0,
        "note": (
            "Fable-review fixes to the NYC homage-era Territory Chronicles. Amends PH2-061 and "
            "PH2-062 to record that Kanja paid off the long-arc unguarded-banter thread in "
            "Xaragua Chronicle VI (MCD-1093), explicitly as a distinct category from Yaisa's own "
            "standing, not parity with it; and MCD-464's file-path reference after its Chronicle "
            "file was renamed from the-price-she-wouldnt-let-them-pay.md to "
            "yara-chronicle-ii-the-price-she-wouldnt-let-them-pay.md to match the project's "
            "established territory-Chronicle naming convention. All other findings from the "
            "review were applied as prose-only corrections directly to the Chronicle .md files "
            "(no ledger-statement change needed): a testing-period length mismatch (a week vs. "
            "the locked three days) and an unnamed-guest-convention leak in Xaragua Chronicle VI; "
            "a quoted-ability-name leak reframing 'Caucus' in Yara Chronicle III; an attrition-math "
            "error and a 'two who'd died' overstatement in Borikén Chronicle II; a stray 'seven "
            "years' duplication in Areíto Chronicle II; two real-world-term leaks ('Modern "
            "Laconic,' 'Rorschach-cut') in Xaragua Chronicle II; quoted-ability-name leaks in "
            "Guanín Chronicle III and Borikén Chronicle III; a stale 'not yet locked'/'pending "
            "Abad's approval' pair of header/footer claims in Xaragua Chronicle II now corrected "
            "to reflect that PH2-060 through PH2-062 locked in the same batch; a mis-sourced "
            "header claim in Xaragua Chronicle IV corrected to credit Xaragua Chronicle II's own "
            "header note as Naya's actual first mention; stale present-tense 'is to be "
            "superseded... when this locks' footer language corrected to past tense in Xaragua "
            "Chronicle I and Yara Chronicle I; and a singular/plural mismatch against PH2-008's "
            "single-patron framing in Guanín Chronicle I. docs/lords-of-cian/"
            "chronicle-tracks-status.md updated to reflect Areíto, Guanín, and Borikén each now "
            "having 3 Chronicles rather than 2. One finding (Xaragua Chronicle III's cohort death "
            "count vs. Chronicle V's three named chairs) needs Abad's own creative ruling and is "
            "deliberately left untouched; two findings (Eri Kotoko's ambiguous Guanín Chronicle I "
            "outcome; Chronicle VI's deliberate Kanja-POV exception) were confirmed as intentional, "
            "not errors, and needed no fix."
        ),
    })

    old_version = float(ledger["ledger_version"])
    ledger["ledger_version"] = str(round(old_version + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(
        f"OK: {len(ledger['rules'])} total rules, {len(ledger['batches_completed'])} "
        f"batches, ledger_version {ledger['ledger_version']}, zero duplicate IDs. "
        f"{len(amended)} rule statements amended: {', '.join(amended)}."
    )


if __name__ == "__main__":
    main()
