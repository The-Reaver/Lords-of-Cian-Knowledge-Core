#!/usr/bin/env python3
"""Batch 256: Industrial Myth Alias Chronicle waves 22-30 (27 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Industrial Myth's twenty-second through thirtieth Alias Chronicle waves (9 waves, 27 "
    "entries), drafted under Abad's blanket authorization to continue all eleven aliases' waves "
    "22-30 uninterrupted. Pushed into registers never shown across the alias's prior twenty-one "
    "waves: honest conflicting testimony, apprenticeship-contract and housing/tenant-rights and "
    "workplace-injury domains, a hidden ledger kept to protect workers rather than steal from "
    "them, a direct personal bribe offered to Kanja, a non-monetary public-apology remedy, a "
    "disabled worker's own expertise as the decisive investigative method, Kanja running the "
    "arithmetic alone (and erring) when Ezio is incapacitated, a coerced fraud collaborator, a "
    "district sealed by quarantine worked entirely through a courier, the crew deferring to a "
    "district's own vote not to pursue a winnable claim, a young bystander-witness's careful "
    "testimony, the reputation itself outrunning the method and causing real harm, a voluntary "
    "deathbed confession, a genuine failure where the method's own pace costs a life (prompting a "
    "new standing emergency-relief practice), an administrator relieved to be caught, a language "
    "barrier worked through verified phonetic transcription, a full company-town truck-system "
    "case, a withdrawn complaint preserved unresolved for future context, a strategic partial "
    "confession masking a larger fraud, institutional triage under genuine case-volume scarcity, "
    "Pell Ostra's private shadow-notes paying off years later, and a closing pair leaving one case "
    "honestly unresolved when the war calls the crew elsewhere before a legacy reflection on the "
    "now-multi-volume archive. No new named characters were introduced across any of the 27 "
    "entries; every entry reused already-locked crew (Ezio Valcari, Pell Ostra) or unnamed "
    "one-scene figures. Strictly unarmed and non-combat throughout, per the alias's own ethos. "
    "Abad's approval: \"lets do this 22nd Alias Chronicle wave for any/all of the eleven aliases "
    "to the 30th wave and you are to continue uninterrupted until completion this includes "
    "rigorous testing, commit, push to main origin.\""
)

NEW_RULES = [
    {
        "id": "MCD-1148",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Testimony That Contradicted Itself\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-testimony-that-contradicted-itself.md), Industrial "
            "Myth Alias Chronicle LXIV, wave 22. A husband and wife give sincerely conflicting "
            "testimony about the mill's weekly schedule; Ezio's cross-referencing finds neither is "
            "lying, reconciling both accounts as true of two different, unannounced seasons rather "
            "than picking a winner -- the method's first honest-conflicting-testimony register."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1149",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Apprenticeship That Never Ended\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-apprenticeship-that-never-ended.md), Industrial Myth "
            "Alias Chronicle LXV, wave 22. The method's first apprenticeship-contract case: a bonded "
            "craft apprentice kept four years past any craft still being taught, proven through peer "
            "wheelwrights' competency comparison rather than wage arithmetic, resolved with a "
            "contract release and subsidy-fraud exposure rather than a coin settlement."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1150",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Second Set of Books\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-second-set-of-books.md), Industrial Myth Alias "
            "Chronicle LXVI, wave 22, closing the wave. The method's first case where a hidden "
            "second ledger protects workers rather than defrauds them -- an administrator "
            "understating official costs to shield his workers' true wages from a regional Trust "
            "comptroller's institutionalized skim above district level."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1151",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"Three Generations Under the Same Debt\" (full narrative text at "
            "docs/lords-of-cian/chronicles/three-generations-under-the-same-debt.md), Industrial "
            "Myth Alias Chronicle LXVII, wave 23. The method's first inherited multi-generational "
            "debt-bondage case: a fraudulent loan renewed against successive family members for "
            "fifty years is traced to its original terms and voided entirely as illegitimate past "
            "its fourth year, freeing grandfather, son, and grandson in one finding."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1152",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Coin Meant for Him Alone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-coin-meant-for-him-alone.md), Industrial Myth Alias "
            "Chronicle LXVIII, wave 23. The method's first direct personal bribe offered to Kanja "
            "himself to abandon a case unopened; he refuses and discloses the unwitnessed offer to "
            "Ezio anyway, extending the crew's internal transparency discipline."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1153",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Apology He Made Them Write Twice\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-apology-he-made-them-write-twice.md), Industrial "
            "Myth Alias Chronicle LXIX, wave 23, closing the wave. The method's first purely "
            "non-monetary remedy: workers demand a public apology over wages; a vague first draft "
            "is rejected as evasive and a specific, honest second draft is required and delivered."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1154",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What His Hands Never Saw\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-his-hands-never-saw.md), Industrial Myth Alias "
            "Chronicle LXX, wave 24. A blind quarry scale-tender's testimony, dismissed by his "
            "overseer as unreliable, is vindicated in full when his touch-and-sound tracking method "
            "proves more precise than the yard's own written weigh-book, exposing years of thumb-"
            "pressure scale fraud."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1155",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"Two Administrators, One Shortfall\" (full narrative text at "
            "docs/lords-of-cian/chronicles/two-administrators-one-shortfall.md), Industrial Myth "
            "Alias Chronicle LXXI, wave 24. The method's first triangulated-fraud case: two rival "
            "mill owners, each blaming the other, share a single shortfall that exists only in the "
            "uncoordinated gap between their two individually clean-looking books; both are held "
            "jointly liable and a standing cross-reconciliation practice is instituted."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1156",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Four Days Ezio Couldn't Stand\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-four-days-ezio-couldnt-stand.md), Industrial Myth "
            "Alias Chronicle LXXII, wave 24, closing the wave. Ezio is injured and Kanja runs the "
            "cross-referencing arithmetic alone for the first time, slower and less precise, making "
            "and publicly correcting his own errors rather than concealing them -- the first entry "
            "to show Kanja's real fluency limits against Ezio's trained skill."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1157",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Man Who Signed the False Entry\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-man-who-signed-the-false-entry.md), Industrial Myth "
            "Alias Chronicle LXXIII, wave 25. The method's first coerced-fraud-collaborator case: a "
            "clerk falsified coworkers' wages under threat to his bonded sister's conditions; the "
            "finding restores the workers' wages from the true wrongdoer, an unnamed mill owner, "
            "while separately documenting the owner's coercion, holding both facts at once."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1158",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The District Behind the Quarantine Line\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-district-behind-the-quarantine-line.md), Industrial "
            "Myth Alias Chronicle LXXIV, wave 25. A fever quarantine seals an entire district; the "
            "method is worked for six weeks entirely from outside the line through a single "
            "trusted courier, the finding explicitly marked provisional where it cannot verify, and "
            "confirmed in full once the quarantine lifts."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1159",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Vote Not to Ask\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-vote-not-to-ask.md), Industrial Myth Alias Chronicle "
            "LXXV, wave 25, closing the wave. A district votes, by clear majority, not to pursue a "
            "claim the ledger's own numbers plainly favor, judging the risk too great; Kanja defers "
            "entirely to the vote over Ezio's objection, establishing the numbers inform but never "
            "override the workers' own choice."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1160",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Youngest Ever Saw\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-youngest-ever-saw.md), Industrial Myth Alias "
            "Chronicle LXXVI, wave 26. The method's first case built on a young child bystander's "
            "testimony to an administrator's wrongdoing; taken with careful, age-appropriate "
            "handling and independently corroborated rather than relied on alone before any finding "
            "is built."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1161",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Boycott That Backfired\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-boycott-that-backfired.md), Industrial Myth Alias "
            "Chronicle LXXVII, wave 26. Workers inspired by the reputation organize their own walk-"
            "out without the method, and the owner uses it as pretext to dismiss and evict them "
            "before the crew arrives; the crew documents the damage and wins partial reinstatement "
            "after the fact -- the first entry where the reputation itself, outrunning the method, "
            "causes real and only partly reversible harm."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1162",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What He Confessed Before the End\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-he-confessed-before-the-end.md), Industrial Myth "
            "Alias Chronicle LXXVIII, wave 26, closing the wave. A dying administrator voluntarily "
            "confesses forty years of skimmed wages and pays restitution from his estate before "
            "death, over his heirs' objection; the crew's role is verifying and protecting the "
            "confession's validity rather than investigating resistance."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1163",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Roof Over the Ledger\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-roof-over-the-ledger.md), Industrial Myth Alias "
            "Chronicle LXXIX, wave 27. The method's first tenant/housing-rights case: an ironworks' "
            "mandatory company housing rent is engineered to rise in step with every wage increase, "
            "consuming it before workers can keep it; the finding fixes rent to honest comparable "
            "pricing and returns the engineered overcharges as back-owed wages."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1164",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"Too Slow By One Day\" (full narrative text at "
            "docs/lords-of-cian/chronicles/too-slow-by-one-day.md), Industrial Myth Alias Chronicle "
            "LXXX, wave 27. A genuine failure of the method's own careful pace: an ill dockyard "
            "laborer dies of exposure the night before his properly diligent, five-day case closes; "
            "the crew institutes a new standing practice of immediate provisional relief for any "
            "testifier with documented medical urgency."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1165",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Overseer Who Thanked Him for the Finding\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-overseer-who-thanked-him-for-the-finding.md), "
            "Industrial Myth Alias Chronicle LXXXI, wave 27, closing the wave. A rare register: an "
            "administrator who has wanted to fix a known wage problem for years but lacked the "
            "institutional standing to do so welcomes the crew's outside audit, which his own board "
            "finally believes; Kanja verifies the cooperative testimony as rigorously as any hostile "
            "case regardless."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1166",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ledger in a Tongue He Didn't Read\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ledger-in-a-tongue-he-didnt-read.md), Industrial "
            "Myth Alias Chronicle LXXXII, wave 28. The method's first language-barrier case: "
            "testimony taken through a bilingual interpreter, transcribed phonetically first and "
            "verified by a second independent bilingual worker, catching two small discrepancies "
            "before the finding is built; delivered afterward in both languages."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1167",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Company Town Owned\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-company-town-owned.md), Industrial Myth Alias "
            "Chronicle LXXXIII, wave 28. The method's largest single-employer case yet: a full "
            "company-town truck system where one owner controls wages, housing, and the only store, "
            "each individually legal; a combined cost-of-living audit prices the closed loop "
            "honestly and forces wages, rent, and store markups into alignment with the free market."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1168",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Record That Outlived the Complaint\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-record-that-outlived-the-complaint.md), Industrial "
            "Myth Alias Chronicle LXXXIV, wave 28, closing the wave. A woman withdraws her wage "
            "complaint under domestic pressure but asks her testimony be preserved unresolved "
            "rather than struck; eight months later it supplies decisive context for an unrelated "
            "worker's similar claim at the same mill -- the method's first witness-without-a-"
            "verdict record category."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1169",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Confession That Hid a Larger One\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-confession-that-hid-a-larger-one.md), Industrial "
            "Myth Alias Chronicle LXXXV, wave 29. An administrator's immediate, genuine confession "
            "of a minor overtime shortfall is a deliberate lid over a much larger two-year base-"
            "wage fraud his quick cooperation nearly kept hidden; Ezio's habit of auditing beyond "
            "any volunteered confession's stated boundary catches it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1170",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Season He Couldn't Slow Down\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-season-he-couldnt-slow-down.md), Industrial Myth "
            "Alias Chronicle LXXXVI, wave 29. Six districts request the crew in a single week, more "
            "than the method's own careful pace can answer; a written triage criteria -- medical "
            "urgency, active retaliation, workforce scale, then order of arrival -- is built and "
            "explained honestly to every delayed district, the crew's first institutional-scarcity "
            "problem."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1171",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Pell Ostra Wrote in the Margins\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-pell-ostra-wrote-in-the-margins.md), Industrial "
            "Myth Alias Chronicle LXXXVII, wave 29, closing the wave. Pell Ostra's private, "
            "deliberately inadmissible shadow-notes -- kept alongside the official ledger but never "
            "shown to Ezio -- prove decisive two years later, identifying an unnamed recurring "
            "observer connecting two otherwise unrelated frauds; the observer's identity is left "
            "deliberately open."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1172",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Wage That Wasn't the Whole Debt\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-wage-that-wasnt-the-whole-debt.md), Industrial Myth "
            "Alias Chronicle LXXXVIII, wave 30. The method's first workplace-injury liability case: "
            "a forge worker loses two fingers to a hazard his owner ignored despite two written "
            "warnings; Ezio, working with a district physician, builds the field's first lost-"
            "earning-capacity settlement rather than a wage-hour figure."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1173",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Last Holdout of This Front\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-last-holdout-of-this-front.md), Industrial Myth "
            "Alias Chronicle LXXXIX, wave 30. An administrator's lawful, total non-cooperation "
            "resists every method the crew has ever used; called to a new front of the war before "
            "the case can close, Kanja and Ezio leave it honestly recorded as unresolved rather "
            "than force a weaker finding or default it against the administrator -- the method's "
            "first case closed by the wider war's own demands rather than any finding."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1174",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Ledger Became\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-ledger-became.md), Industrial Myth Alias "
            "Chronicle XC, wave 30, closing the wave. A legacy closer bookending MCD-932's single-"
            "volume reflection at a larger scale: Kanja and Ezio look over eleven volumes of the "
            "now multi-generational archive and reckon honestly with its future beyond their own "
            "direct hands, closing this nine-wave run."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 27, f"expected 27 new rules, got {len(NEW_RULES)}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    for r in NEW_RULES:
        assert r["category"] == "kanja-alias-chronicle", f"bad category on {r['id']}"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 256,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-11, no source document",
            "rule_count": len(NEW_RULES),
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs found post-write!"

    print(
        f"OK. Total rules: {len(ledger['rules'])}. "
        f"Ledger version: {ledger['ledger_version']}. "
        f"Batches: {len(ledger['batches_completed'])}."
    )


if __name__ == "__main__":
    main()
