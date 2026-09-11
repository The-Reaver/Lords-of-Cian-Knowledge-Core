#!/usr/bin/env python3
"""Batch 224: Lock the Scourge's seventeenth through nineteenth Alias Chronicle waves
(MCD-1014 through MCD-1022, 9 rules). Completes waves 17-19 across all eleven aliases."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "three more waves and then we\'ll move on to something else this includes '
    'testing committing and pushing to origin Main." Waves 17-19 (three-per-alias pacing) '
    "for the Scourge, completing waves 17-19 across all eleven aliases (Batches 214-224, "
    "99 new Chronicles, MCD-924 through MCD-1022)."
)

ENTRIES = [
    (17, "the-last-fight-before-the-silence", "The Last Fight Before the Silence", "XLIX",
     "Age 24. A Trust-linked slaving convoy funding a general's anti-Rebellion campaign is "
     "raided with full unsealed Trinity, including Onyx of Oblivion fighting freely for "
     "the first time under this alias -- predates the Long Mask and the V1 armor's debut."),
    (17, "the-prisoner-who-knew-three-names", "The Prisoner Who Knew Three Names", "L",
     "Age 27. A captured Trust officer recognizes the same man behind Bane, the Trench "
     "Monarch, and the Scourge by fighting rhythm alone. Resolved through pragmatic "
     "self-interest rather than threat or loyalty -- the closest any Chronicle has come to "
     "explicit cross-alias identity recognition."),
    (17, "the-name-chosen-to-outlast-the-others", "The Name Chosen to Outlast the Others",
     "LI",
     "Age 29. Valen Sinisterblade, Efa Gol, and a not-yet-elderly Garren Hask deliberately "
     "choose the Scourge as the persona built to carry the coming Long Mask, since Bane and "
     "the Trench Monarch are both too tied to the Rebellion's own datable history. Closes "
     "wave 17."),
    (18, "the-contract-he-wouldnt-sign", "The Contract He Wouldn't Sign", "LII",
     "Age 155, V3 gear. A Trust envoy offers a formal letter of marque in exchange for "
     "operating as a sanctioned agent. Refused: institutional ownership would destroy the "
     "trust the reputation depends on."),
    (18, "the-testimony-he-never-gave-in-person", "The Testimony He Never Gave in Person",
     "LIII",
     "Age 148, V3 gear. A prize-court conviction hinges on sworn testimony the Scourge "
     "can't give in person; Garren Hask delivers a sealed, corroborated account instead, "
     "and the court admits it. New civic/legal register."),
    (18, "the-insurance-they-tried-to-buy", "The Insurance They Tried to Buy", "LIV",
     "Age 135, V3 gear. A six-house trading consortium offers to pay for protection rather "
     "than be left alone by force. Refused, with a six-month grace period offered instead "
     "of retaliation. Closes wave 18."),
    (19, "the-family-he-helped-her-find", "The Family He Helped Her Find", "LV",
     "Age 115. A freed captive asks the crew's ledger network to help trace a sibling sold "
     "on a different route decades earlier; Garren Hask finds a lead, and the reunion's "
     "outcome is deliberately left off the page."),
    (19, "the-night-the-crew-took-someone-in", "The Night the Crew Took Someone In", "LVI",
     "Age 85. A freed captive formally requests and wins full crew membership, celebrated "
     "communally -- the sub-series' first entirely warm, conflict-free entry for this "
     "alias."),
    (19, "the-last-coat-he-ever-wore", "The Last Coat He Ever Wore", "LVII",
     "Age 314, V4 gear, the final year of the 284-year Long Mask. The literal last mission "
     "under the Scourge identity; the coat comes off for good that night, ending the span "
     "by conscious choice, deliberately left open for future material. Closes wave 19."),
]

assert len(ENTRIES) == 9


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 224, 2026-09-11 (`MCD-{mcd_id}`). The Scourge Alias "
        f"Chronicle {roman}, wave {wave}. Not a territory Chronicle. Narrated in neutral "
        f"third-person prose.*"
    )
    new_text, n = pattern.subn(replacement, text, count=1)
    assert n == 1, f"header pattern not found/replaced in {filename}"
    with open(path, "w") as f:
        f.write(new_text)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    start = 1014
    new_rules = []
    for i, (wave, filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The "
                f"Scourge Alias Chronicle {roman}, wave {wave}. {summary}"
            ),
            "status": "locked",
            "source": SOURCE,
        })

    new_ids = [r["id"] for r in new_rules]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collisions with existing ledger: {collisions}"

    ledger["rules"].extend(new_rules)

    ledger["batches_completed"].append({
        "batch": 224,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Scourge's seventeenth through nineteenth Alias Chronicle waves "
            "(MCD-1014 through MCD-1022, 9 rules). " + BATCH_NOTE
        ),
    })

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate IDs after merge"
    print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
          f"Batches: {len(ledger['batches_completed'])}.")


if __name__ == "__main__":
    main()
