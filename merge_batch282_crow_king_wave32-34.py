#!/usr/bin/env python3
"""Batch 282: Crow King Alias Chronicle waves 32, 33, and 34 (9 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "Continues the Alias Chronicle sub-series' thirty-second, thirty-third, and thirty-fourth waves "
    "for the Crow King, under Abad's direct authorization: \"do 3 more alias wave for all eleven.\" "
    "Wave 32 lands a third distinct physical/environmental limit on the Hymn-Engine's core channels "
    "-- extreme cold numbing the tap-signal channel's tactile precision, after the throat wound "
    "(MCD-915) and temporary deafness (MCD-1266) already landed on voice and hearing -- then finally "
    "answers the fifth-generation question left open since wave 22 (MCD-1258) and advanced but "
    "unresolved in wave 30 (MCD-1280): teaching formally begins with the runner's son, and the wave "
    "closes on the lineage's first coordination failure caused purely by its own growth in scale, a "
    "message garbled across too many relay hands. Wave 33 carries the Hymn-Engine across open water "
    "for the first time (a strait crossing using cliff-reflected percussion rather than direct "
    "projection), brings back the Directorate officer who once tried to deceive Kanja himself "
    "(MCD-1265) now asking to be taught and set on a year's probation rather than admitted outright, "
    "and closes on the fifth generation's first independent field test revealing a third distinct "
    "lineage specialty -- reading unconscious physical tells rather than sound or numbers. Wave 34 "
    "opens with a detailed full-Trinity combat showcase inside a burning, collapsing granary, "
    "deliberately inverting the total-silence vault of wave 20 (MCD-1045) with total, overwhelming "
    "noise as the obstacle instead; continues with the lineage running two full operations "
    "simultaneously with zero Kanja foreknowledge or oversight, a genuine test of complete "
    "institutional autonomy; and closes the full three-wave run on the fourth generation quietly "
    "grieving Garren Hask's already-locked death (MCD-1422) -- an honest, uncorrectable loss his own "
    "gift has no tool for. No new named characters were introduced anywhere across all nine entries; "
    "every returning figure (the fourth generation, the apprentice, the third generation, the fifth "
    "generation/runner's son, Commandant Voris's former hunter-officer, Garren Hask) is already "
    "locked."
)

NEW_RULES = [
    {
        "id": "MCD-1478",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Frost That Dulled the Beat\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-frost-that-dulled-the-beat.md), Crow King Alias "
            "Chronicle XCIV, wave 32, opening it. A blizzard highland-camp extraction lands a third "
            "distinct physical limit on the Hymn-Engine's core channels -- after the throat wound "
            "(MCD-915) and temporary deafness (MCD-1266) -- when extreme cold numbs the fourth "
            "generation's hands mid-operation, degrading the tap-signal channel's precision for the "
            "first time. Resolved by simplifying to a crude, redundant two-signal layer built to "
            "survive numbed hands, added as a standing capability rather than a one-off fix. "
            "Establishes winter/blizzard conditions as a new environmental register. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1479",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fifth Voice\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fifth-voice.md), Crow King Alias Chronicle XCV, wave "
            "32. The fifth-generation question, raised in Chronicle LXVI (MCD-1258, wave 22) and "
            "advanced but left unresolved in Chronicle LXXXVIII (MCD-1280, wave 30), is finally "
            "answered: teaching formally begins with the runner's son as the fifth generation, "
            "decided collectively by Kanja, the apprentice, the third generation, and the fourth "
            "generation together rather than by any one of them alone, extending the consent-process "
            "theme established at the fourth generation's own beginning (MCD-1046). No new named "
            "characters; the runner's son remains unnamed."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1480",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Signal Passed Too Many Hands\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-signal-passed-too-many-hands.md), Crow King Alias "
            "Chronicle XCVI, wave 32, closing it. With five active generations now carrying the "
            "craft (Kanja, the apprentice, the third generation, the fourth generation, and the newly "
            "taught fifth, MCD-1479), a message relayed through too many hands garbles mid-chain, "
            "nearly causing a real failure at a bridge crossing -- the first coordination failure "
            "caused purely by the lineage's own growth in scale rather than an opponent, environment, "
            "or individual mistake. Resolved with a new standing practice: mandatory repeat-back "
            "confirmation past two relay hops. No new named characters. Closes wave 32 (with "
            "MCD-1478 and MCD-1479)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1481",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Signal That Crossed the Strait\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-signal-that-crossed-the-strait.md), Crow King Alias "
            "Chronicle XCVII, wave 33, opening it. The Hymn-Engine is carried across open water for "
            "the first time -- a labor-island extraction using a hollow pipe struck against a cliff "
            "face, reflected across a strait to mimic a patrol boat's own return signal three minutes "
            "early -- establishing open-water acoustic relay as a new terrain type built around "
            "water's distinct flat-carrying, then-abrupt-cutoff acoustic behavior, distinct from every "
            "prior environment (marsh, highland, urban, river, desert, mountain, total darkness, "
            "winter cold). Combined with the fourth generation's already-established falsified-"
            "paperwork method (MCD-1077) as a second independent layer, extending the two-technique "
            "combination precedent of \"The Braid and the Blade\" (MCD-495). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1482",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Hunter Who Chose to Learn\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-hunter-who-chose-to-learn.md), Crow King Alias "
            "Chronicle XCVIII, wave 33. The Directorate officer who once tried to deceive Kanja "
            "himself (\"The Hunter Who Studied the Hunter,\" Chronicle LXXIII, MCD-1265, wave 25) "
            "returns years later, having left Directorate service, asking to be taught rather than "
            "to counter the craft -- the first entry to bring a former adversary toward the lineage "
            "rather than resolve him as a defeated opponent. Kanja imposes a full year's probation "
            "working alongside the lineage before any teaching is considered, deliberately "
            "distinguished from the fifth generation's immediate admission (MCD-1479). No new named "
            "characters; the officer remains unnamed, per his original introduction."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1483",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Fifth Generation Chose to Notice\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-fifth-generation-chose-to-notice.md), Crow King "
            "Alias Chronicle XCIX, wave 33, closing it. The fifth generation's first independent "
            "field test -- confirming a quartermaster's grain-skimming through two days of watching "
            "unconscious physical tells rather than any voice or ledger -- reveals a third distinct "
            "specialty within the direct teaching lineage (behavioral/visual observation, alongside "
            "the apprentice's vocal/rhythmic register and the fourth generation's numeric/documentary "
            "one), paralleling the fourth generation's own solo debut (MCD-1077) as a structural "
            "counterpart and extending \"the craft was never really vocal at its core\" (MCD-845) "
            "into a genuinely different sensory channel. No new named characters; the quartermaster "
            "is unnamed and one-scene. Closes wave 33 (with MCD-1481 and MCD-1482)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1484",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Burned Loud Enough to Hear\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-burned-loud-enough-to-hear.md), Crow King Alias "
            "Chronicle C, wave 34, opening it. A detailed full-Trinity combat showcase rescuing "
            "twelve hostages from a deliberately-set burning granary, deliberately inverting "
            "\"The Vault That Held No Light\" (MCD-1045, wave 20): where that entry used total "
            "silence as the tactical hinge, this one uses total, overwhelming noise -- cracking "
            "timber, exploding grain sacks, a failing roof beam -- with Mafesto's Kinetic Transfer "
            "System, Obsidian Malice, and Onyx of Oblivion's Cadence Ruin, Veil Piercer, and "
            "Soulbound Edge all reading the room by pressure and rhythm rather than sight or clean "
            "sound. Establishes structural fire/collapse conditions as a new environmental register. "
            "No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1485",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Day Kanja Wasn't Anywhere Near Either One\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-day-kanja-wasnt-anywhere-near-either-one.md), Crow "
            "King Alias Chronicle CI, wave 34. The apprentice and the third generation run a Braid "
            "extraction at one end of a province while the fourth and fifth generations run a "
            "verified-truth tribunal action at the other, the same night, with Kanja aware of neither "
            "operation until told over dinner three days later -- a deliberate structural inversion "
            "of \"All Four Voices at Once\" (MCD-1264, wave 24), testing full institutional autonomy "
            "for the first time: the lineage no longer requires Kanja's presence, foreknowledge, or "
            "approval to function. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1486",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Numbers Couldn't Hold\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-numbers-couldnt-hold.md), Crow King Alias "
            "Chronicle CII, wave 34, closing it. Word reaches the fourth generation of Garren Hask's "
            "already-locked death (\"The Morning the Ledger Went Quiet,\" Captain Alias Chronicle "
            "XCII, MCD-1422, wave 31), extending the fourth generation's own established prior "
            "connection to Hask's supply accounting (\"The Siege That Needed No Braid,\" MCD-1278, "
            "wave 29); he finds his numeric gift has no tool for an honest, uncorrectable loss with "
            "no error to find in it, and the apprentice sits with him rather than offering any fix. "
            "A deliberately new emotional register closing this alias's growth-and-maturity run on a "
            "loss the craft cannot solve. No new named characters. Closes wave 34 (with MCD-1484 and "
            "MCD-1485) and this three-wave run (waves 32-34)."
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
            "batch": 282,
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
