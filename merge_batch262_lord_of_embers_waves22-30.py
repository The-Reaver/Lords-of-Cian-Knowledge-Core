#!/usr/bin/env python3
"""Batch 262: Lord of Embers Alias Chronicle waves 22-30 (27 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Lord of Embers' twenty-second through thirtieth Alias Chronicle waves (9 waves, 27 "
    "entries), drafted under Abad's blanket authorization to continue all eleven aliases' waves "
    "22-30 uninterrupted. Genuinely new registers across this run: payoffs to two long-open hooks "
    "(the ballad-pilgrim myth, MCD-881, and the counterfeit-mark arms race, MCD-1084); an unplanned "
    "health-forced succession for the senior smith; the alias's first deep-cold, open-sea-storm, "
    "arid-canyon, and predator-wildlife environmental registers; institutional-decay, legal-hearing, "
    "bonded-labor-liberation, academy-founding, gear-vulnerability, hostage-coercion, crowd-safety, "
    "labor-governance, base-maintenance, and a multi-tactic adaptive-enemy capstone; a real injury "
    "that incapacitates Kanja for three weeks and tests the method's institutional resilience "
    "without him; and a closing distant-future entry showing the Open-Forge Standard fully "
    "disconnected from its own origin. No new named characters were introduced anywhere in this "
    "run; every entry reused already-locked crew (the senior smith and her successor, Garren Hask) "
    "or kept new secondary figures unnamed by role, matching this alias's own overwhelming "
    "established convention. Abad's approval: \"lets do this 22nd Alias Chronicle wave for any/all "
    "of the eleven aliases to the 30th wave and you are to continue uninterrupted until completion "
    "this includes rigorous testing, commit, push to main origin.\""
)

NEW_RULES = [
    {
        "id": "MCD-1310",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Ballad Brought to His Door\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-ballad-brought-to-his-door.md), Lord of Embers "
            "Alias Chronicle LXIV, first entry in the twenty-second wave. A direct payoff to \"The "
            "Ballad That Outgrew the Truth\" (MCD-881): a boy who walked eleven days on the strength "
            "of the exaggerated ballad arrives expecting a legend and finds an ordinary working man; "
            "the myth is left uncorrected, but he chooses to stay anyway, absorbed into the ordinary "
            "work rather than disillusioned by it. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1311",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Frost That Didn't Wait for Spring\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-frost-that-didnt-wait-for-spring.md), Lord of Embers "
            "Alias Chronicle LXV, wave 22. A detailed, battle-intense Trinity combat showcase in the "
            "alias's first deep-cold/frost environmental register: a Directorate patrol exploits an "
            "unseasonable freeze at a highland terrace, and Kanja discovers Mafesto's grounding "
            "mechanism (MCD-291) requires actively retaining heat before it can be redirected, a "
            "genuine cold-weather limit not previously shown. Obsidian Malice used for steam-based "
            "blinding rather than direct damage. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1312",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Senior Smith Set Down\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-senior-smith-set-down.md), Lord of Embers Alias "
            "Chronicle LXVI, wave 22, closing the wave. An unplanned, health-forced institutional-"
            "discontinuity entry, distinct from the deliberate training bookend at MCD-887: a wasting "
            "joint condition forces the senior smith into early, unceremonious retirement, and her "
            "already-established successor (MCD-923, MCD-1052) steps into full authority overnight, "
            "confirming the succession holds under an unplanned handoff. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1313",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Apprentice No One Vouched For\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-apprentice-no-one-vouched-for.md), Lord of Embers "
            "Alias Chronicle LXVII, first entry in the twenty-third wave. A genuinely new suspicion/"
            "trust register distinct from the real sabotage of MCD-501: an unvouched-for new arrival "
            "is wrongly suspected of espionage; resolved through patient, honest verification and "
            "direct conversation rather than confrontation, and the boy stays on, later guiding other "
            "frightened new arrivals himself. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1314",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Storm That Nearly Took the Anvil\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-storm-that-nearly-took-the-anvil.md), Lord of Embers "
            "Alias Chronicle LXVIII, wave 23. A detailed, battle-intense Trinity combat showcase: a "
            "genuine open-sea storm nearly capsizes The Anvil itself while a Directorate cutter uses "
            "the weather as cover for a boarding strike; Mafesto's grounding function is used to brace "
            "the ship's own straining structure and Obsidian Malice's discharge performs emergency "
            "mid-battle structural repair, both new applications of established gear mechanics. Kanja "
            "pulls enemy sailors from the water after the fight, extending established restraint. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1315",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Hands That Couldn't Lift a Hammer Still Built\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-hands-that-couldnt-lift-a-hammer-still-built.md), "
            "Lord of Embers Alias Chronicle LXIX, wave 23, closing the wave. A meritocracy entry "
            "extending the open method to a settlement's disabled and elderly population for the "
            "first time, finding non-physical roles (ledgering, weather-reading, precision inventory) "
            "matched to genuine aptitude rather than offering diminished or token work. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1316",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Mark No One Could Steal\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-mark-no-one-could-steal.md), Lord of Embers Alias "
            "Chronicle LXX, first entry in the twenty-fourth wave. A direct payoff to \"The Standard "
            "They Learned to Fake\" (MCD-1084): the senior smith's successor resolves the counterfeit-"
            "mark arms race not by escalating the physical die further but by moving proof of "
            "authenticity into a taught, hand-to-hand demonstrable skill no counterfeiter can copy "
            "from the finished tool alone -- a partial, not absolute, resolution. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1317",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Old Dam Remembered\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-old-dam-remembered.md), Lord of Embers Alias "
            "Chronicle LXXI, wave 24. A detailed, battle-intense Trinity combat showcase against a "
            "long-tail structural failure with no enemy involved: a rushed diversion dam built months "
            "earlier during the embargo (MCD-456) begins failing from internal stress, and the Trinity "
            "races to reinforce it in time to warn a downstream settlement, establishing that "
            "emergency-built fixes carry a genuine deferred cost. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1318",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Guild That Forgot Why It Opened\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-guild-that-forgot-why-it-opened.md), Lord of Embers "
            "Alias Chronicle LXXII, wave 24, closing the wave. The alias's first institutional-decay "
            "entry: a settlement's open-forge ethic has quietly curdled into a gatekeeping toll "
            "charged by self-appointed senior journeymen, resolved through accountability and memory "
            "-- confronting the journeymen in front of those the fee priced out -- rather than "
            "authority or force. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1319",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Hearing They Couldn't Hold Without Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-hearing-they-couldnt-hold-without-him.md), Lord of "
            "Embers Alias Chronicle LXXIII, first entry in the twenty-fifth wave. The alias's first "
            "legal/courtroom entry: a Sovereign Trust magistrate summons the Lord of Embers to answer "
            "for property damages misattributed to him, and Garren Hask (CC-115) testifies with "
            "documented arithmetic that unravels the Trust's own chronology, resulting in an "
            "indefinite adjournment rather than a clean acquittal. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1320",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Bonded Forge Gave Up\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-bonded-forge-gave-up.md), Lord of Embers Alias "
            "Chronicle LXXIV, wave 25. A detailed, battle-intense Trinity combat showcase liberating "
            "two hundred bonded adult workers from a Directorate-aligned foundry running on a "
            "compounding Scrip-Tether debt structure (extending MCD-422's mechanism); resolved with "
            "deliberate, precision non-lethal restraint given the density of uninvolved workers in "
            "the fight's space. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1321",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The School That Outgrew the Anvil\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-school-that-outgrew-the-anvil.md), Lord of Embers "
            "Alias Chronicle LXXV, wave 25, closing the wave. The alias's first institutional-legacy "
            "entry at genuine scale: the senior smith's successor founds a permanent, fixed smithing "
            "academy explicitly designed to outlast the mobile eighteen-month tour, deliberately "
            "carrying no alias's name on its founding charter; the ballad-pilgrim from MCD-1310 "
            "reappears among its founding cohort. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1322",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Coat Couldn't Shed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-coat-couldnt-shed.md), Lord of Embers Alias "
            "Chronicle LXXVI, first entry in the twenty-sixth wave. The alias's first real Forge-Coat "
            "damage/vulnerability entry: an accidental tear disables the coat's liquid-shedding, "
            "light-absorptive treatment (MCD-292) across a whole panel, exposing Kanja to near-"
            "detection until the senior smith's successor improvises a rough field-repair compound, "
            "restoring roughly two-thirds function for six weeks pending proper repair. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1323",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Came Down From the Ridge\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-came-down-from-the-ridge.md), Lord of Embers Alias "
            "Chronicle LXXVII, wave 26. A detailed, battle-intense Trinity combat showcase against a "
            "natural predator threat with no Directorate or human antagonist involved -- a highland "
            "pack driven down by a poor hunting season -- resolved by driving the pack off at Obsidian "
            "Malice's lowest intensity rather than killing them, extending the alias's established "
            "restraint into an ecological register. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1324",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Price They Asked for the Boy\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-price-they-asked-for-the-boy.md), Lord of Embers Alias "
            "Chronicle LXXVIII, wave 26, closing the wave. The alias's first hostage/coercion-pressure "
            "entry: kidnappers hold an apprentice's younger brother against a demand for the "
            "campaign's full Dead Drakma reserves; resolved through patient tracing via the Ghost-"
            "Lattice relay and a decisive extraction that never touches the named exchange point, "
            "rather than negotiation or an open trade. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1325",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Garrison Commander's Second Lesson\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-garrison-commanders-second-lesson.md), Lord of Embers "
            "Alias Chronicle LXXIX, first entry in the twenty-seventh wave. A direct rematch with the "
            "recurring Directorate garrison commander from \"What the Enemy Learned to Rebuild\" "
            "(MCD-922): a faster second rebuild (fourteen days, down from nineteen) demonstrates "
            "genuine method-mastery, and the commander admits an unresolved loyalty tension left "
            "deliberately open rather than resolved into defection or renewed hostility. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1326",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Canyon Carried Sound Of\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-canyon-carried-sound-of.md), Lord of Embers Alias "
            "Chronicle LXXX, wave 27. A detailed, battle-intense Trinity combat showcase in the "
            "alias's first arid/desert canyon environmental register: an ore convoy ambush is broken "
            "by turning the canyon's own dry-air acoustics against dug-in Directorate positions, with "
            "Cadence Ruin detecting repositioning through bare rock and Mafesto's grounding function "
            "shown working differently against parched, heat-radiating stone than wet or frozen "
            "ground. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1327",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Record They Got Right\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-record-they-got-right.md), Lord of Embers Alias "
            "Chronicle LXXXI, wave 27, closing the wave. A direct counterpart to \"The Ballad That "
            "Outgrew the Truth\" (MCD-881): an unnamed keeper of accounts has been compiling a plain, "
            "precise, corrected record of the campaign alongside the exaggerated ballad for six "
            "settlements, existing in coexistence with the myth rather than displacing it. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1328",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Weeks the Method Stood Alone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-weeks-the-method-stood-alone.md), Lord of Embers Alias "
            "Chronicle LXXXII, first entry in the twenty-eighth wave. Kanja is incapacitated by a real, "
            "non-fatal structural-collapse injury for three weeks; the campaign does not stop, the "
            "senior smith's successor (established at MCD-1312) running the floor independently and a "
            "nearby rebuild completing on schedule without him, the clearest proof yet that the method "
            "outlasts its own founder's physical presence. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1329",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What He Came Back to Finish\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-he-came-back-to-finish.md), Lord of Embers Alias "
            "Chronicle LXXXIII, wave 28, direct sequel to MCD-1328. A detailed, battle-intense Trinity "
            "combat showcase fought under genuine, still-healing physical limitation: Kanja fights the "
            "most tactically careful, restraint-driven engagement of the tour, leaning on Onyx of "
            "Oblivion to carry a larger share of the active fighting while Mafesto's grounding function "
            "does more defensive work than usual, successfully defending three settlements targeted "
            "specifically because word of his injury reached the Directorate. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1330",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Hands That Taught the Hands\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-hands-that-taught-the-hands.md), Lord of Embers Alias "
            "Chronicle LXXXIV, wave 28, closing the wave. A generational-transmission entry distinct "
            "from MCD-1085: one of the campaign's very first apprentices, decades later, is shown "
            "teaching his own apprentice -- who never met Kanja directly -- the open method intact and "
            "unweakened by second-hand transmission, confirming the doctrine's fidelity survives a "
            "full generation deep within smithing itself. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1331",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Priest Who Wouldn't Bless the Forge\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-priest-who-wouldnt-bless-the-forge.md), Lord of Embers "
            "Alias Chronicle LXXXV, first entry in the twenty-ninth wave. The alias's first spiritual/"
            "religious-friction entry: a local shrine-keeper objects to the open method's speed as a "
            "threat to older tempering rites; resolved through deliberate restraint -- teaching "
            "alongside rather than displacing the tradition, letting individual smiths choose for "
            "themselves -- rather than persuasion or demonstrated superiority. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1332",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Pilgrims Never Saw Coming\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-pilgrims-never-saw-coming.md), Lord of Embers "
            "Alias Chronicle LXXXVI, wave 29. A detailed, battle-intense Trinity combat showcase "
            "protecting a four-thousand-person pilgrimage crowd from a Directorate strike using the "
            "procession as cover; Mafesto's grounding function is repurposed for physically "
            "shepherding bystanders and Obsidian Malice's discharge is shaped into narrow containment "
            "lanes, prioritizing crowd safety and minimal disruption over speed for the first time. "
            "No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1333",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What They Agreed to Owe Each Other\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-they-agreed-to-owe-each-other.md), Lord of Embers "
            "Alias Chronicle LXXXVII, wave 29, closing the wave. The alias's first formal labor/"
            "economic-governance entry: an apprentice's blunt question exposes that the campaign had "
            "never built a compensation structure alongside its teaching structure; a graduated "
            "stipend and apprentice dispute council are co-designed with apprentices themselves, "
            "extending the open method's participatory ethos into labor governance. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1334",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Anvil Needed From Itself\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-anvil-needed-from-itself.md), Lord of Embers "
            "Alias Chronicle LXXXVIII, first entry in the thirtieth wave. The alias's first base-"
            "maintenance entry: a hull survey after years of service and a sea storm (MCD-1314) "
            "prompts a deliberate three-week proactive refit of The Anvil itself, extending "
            "\"metabolizes punishment\"'s rebuild ethos into ordinary preventive upkeep rather than "
            "crisis response. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1335",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"Everything They'd Learned at Once\" (full narrative text at "
            "docs/lords-of-cian/chronicles/everything-theyd-learned-at-once.md), Lord of Embers Alias "
            "Chronicle LXXXIX, wave 30. A mini-capstone Trinity combat showcase: a coordinated "
            "Directorate assault deliberately stacks four previously-countered tactics at once (a "
            "sabotaged-collapse diversion per MCD-1083, a split-attention ambush, a fabricated-report "
            "misdirection per MCD-970, and civilian-crowd cover per MCD-1332), and the Trinity, with "
            "Garren Hask (CC-115) catching the counterfeit supply signal, answers all four "
            "simultaneously using its full accumulated repertoire. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1336",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Standard That Forgot His Name\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-standard-that-forgot-his-name.md), Lord of Embers "
            "Alias Chronicle XC, wave 30, closing the wave. The alias's furthest-future institutional-"
            "legacy entry, set generations later during the Long Mask era: the Open-Forge Standard "
            "(MCD-1052) and its hand-taught verification method (MCD-1316) are shown fully "
            "disconnected from any memory of their origin, the deliberate outcome the successor's own "
            "refusal to name it after herself was always aiming toward; an unnamed, disguised elder "
            "Kanja observes without intervening. No new named characters. Closes the Lord of Embers' "
            "thirtieth three-Chronicle wave and this batch's nine-wave run."
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
        assert r["category"] == "kanja-alias-chronicle", f"bad category on {r['id']}: {r['category']}"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 262,
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
