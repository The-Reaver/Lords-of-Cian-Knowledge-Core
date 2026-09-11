#!/usr/bin/env python3
"""Batch 286: Captain Alias Chronicle waves 32, 33, and 34 (9 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "Continues the Alias Chronicle sub-series' thirty-second, thirty-third, and thirty-fourth waves "
    "for Captain, under Abad's direct authorization: \"do 3 more alias wave for all eleven.\" Wave 32 "
    "gives the rotating council-chair structure (MCD-1380) its first genuine transition -- Corren "
    "Halst's three-year term ends on schedule and Callum Breck is chosen as the second chair-holder -- "
    "then tests his command style in a detailed full-Trinity combat showcase defending a resettlement "
    "convoy, before closing on Mira (MCD-1370/1371/1372) being offered a formal council seat and the "
    "council inventing a new one-year non-voting observer term to let her accept it honestly. Wave 33 "
    "gives Danne Sok's daughter (MCD-1002) her own first fully independent command, mirroring Corren "
    "Halst's growth a generation later; stages the sub-series' first entry pitting the crew against its "
    "own protected people rather than an external enemy (a panicked grain-shortage crowd, resolved "
    "through restraint and a deliberate choice not to draw Obsidian Malice at all); and closes with "
    "Kanja beginning a concrete, ongoing practice of personally recording the founding generation's "
    "memories, the first real step on the promise made at MCD-920 and renewed at Garren Hask's memorial "
    "(MCD-1423). Wave 34 -- the alias's hundredth Chronicle overall -- gives the sub-series its first "
    "purely voluntary, uncoerced betrayal for personal gain, forcing the dispute council to write the "
    "charter's first involuntary-removal clause; stages a detailed full-Trinity combat showcase "
    "defending the Pier Nine memorial wall itself from a legacy-erasure attack by unreconciled Trust "
    "holdouts; and closes on a former enemy's descendant asking whether the wall's memory can hold a "
    "name from the other side, resolved with a distinct adjacent marker rather than integration. No new "
    "named characters across any of the nine entries -- every returning figure (Corren Halst, Callum "
    "Breck, Efa Gol, Maret Vos he/him, Pell Ostra, Mira, Danne Sok and his daughter, Garren Hask's "
    "already-established unnamed ledger successor) is reused from already-locked crew, and all one-scene "
    "antagonists, clerks, and the descendant are deliberately left unnamed, matching this alias's strong "
    "established convention. Collision-checked: MCD-1514 through MCD-1522 confirmed unused before "
    "drafting."
)

NEW_RULES = [
    {
        "id": "MCD-1514",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Three Years That Ran Out\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-three-years-that-ran-out.md), Captain Alias Chronicle "
            "XCIV, wave 32. The sub-series' first real test of the rotating council-chair structure "
            "(MCD-1380): Corren Halst's three-year term reaches its actual end and she declines a "
            "second term on principle, and the council chooses Callum Breck as the second chair-holder, "
            "tying his acceptance to his own already-locked 'Captain' origin (MCD-397) and Trench "
            "Monarch naming (CC-118). No new named characters. First entry, wave 32."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1515",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Watch Callum Breck Called\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-watch-callum-breck-called.md), Captain Alias Chronicle "
            "XCV, wave 32. A detailed full-Trinity combat showcase (Mafesto's Kinetic Transfer System, "
            "Obsidian Malice, Onyx of Oblivion's Cadence Ruin) defending a resettlement convoy, built "
            "around a genuine first for the sub-series -- Kanja fighting under another crew member's "
            "tactical command as the newly-seated chair. Extends Callum Breck's silent-signal "
            "shore-watch craft (MCD-1099) from a naval into a land-defense application, directly "
            "testing the private fear his own silence arc (CC-119) still carries. All eleven raiders "
            "taken alive. No new named characters. Second entry, wave 32."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1516",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Seat They Offered Her\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-seat-they-offered-her.md), Captain Alias Chronicle XCVI, "
            "wave 32, closing the wave. Mira (MCD-1370/1371/1372) is offered a formal dispute-council "
            "seat, extending her arc from operational courage (MCD-1421) and memorial-wall labor "
            "(MCD-1372/1423) into institutional life for the first time. Introduces a genuine addition "
            "to council practice -- a one-year non-voting observer term preceding full voting "
            "membership, proposed by newly-seated chair Callum Breck (MCD-1514) -- extending rather "
            "than contradicting the charter's (MCD-1056) existing free-membership and slow-trust "
            "principles. No new named characters. Closes wave 32."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1517",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The First Order She Gave Alone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-first-order-she-gave-alone.md), Captain Alias Chronicle "
            "XCVII, wave 33. Danne Sok's daughter (established MCD-1002, deliberately kept unnamed per "
            "that entry's own convention), now grown, leads her first fully independent operation "
            "(intercepting smugglers working a delta's back channels) with neither Kanja nor Corren "
            "Halst present, mirroring Halst's own growth a generation earlier ('The Officers Who "
            "Didn't Need Him There,' MCD-608) and extending the self-sufficiency thread built through "
            "MCD-1364/1385. Kanja's absence is deliberate, consistent with those entries. No new named "
            "characters. First entry, wave 33."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1518",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Crowd That Turned on Itself\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-crowd-that-turned-on-itself.md), Captain Alias Chronicle "
            "XCVIII, wave 33. The sub-series' first entry pitting the crew's protective role against "
            "its own protected people rather than an external enemy -- a panicked grain-shortage crowd "
            "at a distribution yard, with a small unnamed opportunist element exploiting the chaos "
            "rather than causing it. Onyx of Oblivion's Veil Piercer is used for crowd-intent "
            "discrimination rather than combat targeting, and Mafesto's Kinetic Transfer System "
            "redirects a friendly-side crush rather than an attack; Kanja deliberately never draws "
            "Obsidian Malice at all, extending the restraint-as-skill ethos into a register with no "
            "enemy to defeat. Efa Gol and Pell Ostra reused. No new named characters. Second entry, "
            "wave 33."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1519",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Names He Started Writing Down\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-names-he-started-writing-down.md), Captain Alias "
            "Chronicle XCIX, wave 33, closing the wave. Kanja takes his first concrete step toward the "
            "promise made at 'The Promise for After He's Gone' (MCD-920) and renewed at Garren Hask's "
            "memorial (MCD-1423): he begins a personal, narrative-memory practice distinct from Hask's "
            "operational ledger, starting with Efa Gol (extending her Tam Sullen backstory, CC-131) and "
            "Maret Vos (extending MCD-593/MCD-1369). Framed as an ongoing practice rather than a "
            "completed project. No new named characters. Closes wave 33."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1520",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Clerk Who Sold What Wasn't His\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-clerk-who-sold-what-wasnt-his.md), Captain Alias "
            "Chronicle C, wave 34 -- the hundredth Captain Alias Chronicle. The sub-series' first "
            "betrayal driven by pure voluntary self-interest rather than coercion, distinct from "
            "MCD-507/MCD-604's hostage-leverage entries. A relief clerk skims grain shipments for "
            "personal profit, caught through Danne Sok's daughter's audit competence (MCD-1002/1517); "
            "the dispute council, finding the charter (MCD-1056) silent on involuntary removal, amends "
            "it with its first for-cause expulsion clause -- full restitution, immediate removal, and "
            "an explicit but unearned door left open to future trust. The clerk is deliberately unnamed "
            "and non-recurring. No new named characters. First entry, wave 34."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1521",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What They Tried to Erase From the Wall\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-they-tried-to-erase-from-the-wall.md), Captain Alias "
            "Chronicle CI, wave 34. A detailed full-Trinity combat showcase (Onyx of Oblivion's Whisper "
            "of Shadows and Cadence Ruin, Mafesto's Kinetic Transfer System, Obsidian Malice) defending "
            "the Pier Nine memorial wall (MCD-1372) itself from an attack by unreconciled Trust "
            "holdouts aimed at erasing the crew's history rather than harming its people -- a genuinely "
            "new stake for this alias's combat register. All six attackers taken alive. Mira and "
            "Callum Breck (as chair) reused. No new named characters. Second entry, wave 34."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1522",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Name That Wasn't on the Wall\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-name-that-wasnt-on-the-wall.md), Captain Alias Chronicle "
            "CII, wave 34, closing the wave. Weeks after the attack on the memorial wall (MCD-1521), a "
            "former enemy soldier's descendant asks whether the wall's memory can hold a name from the "
            "other side; the council resolves it not by integrating the name into the crew's own wall "
            "but by creating a distinct, adjacent marker for those who never chose the side they died "
            "for, preserving rather than flattening the moral distinction Efa Gol raises. Mira's "
            "contribution reflects her still-new observer-seat standing (MCD-1516). The woman and her "
            "grandfather are deliberately unnamed and non-recurring. No new named characters. Closes "
            "wave 34 and this three-wave run (waves 32-34) at one hundred and two total Captain Alias "
            "Chronicles across thirty-four complete waves."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)
    assert len(NEW_RULES) == 9, f"expected 9 new rules, got {len(NEW_RULES)}"
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"
    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"
    ledger["rules"].extend(NEW_RULES)
    ledger["batches_completed"].append(
        {
            "batch": 286,
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
