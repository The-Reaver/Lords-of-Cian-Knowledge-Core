#!/usr/bin/env python3
"""Batch 260: Crow King Alias Chronicle waves 22-30 (27 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Crow King's twenty-second through thirtieth Alias Chronicle waves (9 waves, 27 entries), "
    "drafted under Abad's blanket authorization to continue all eleven aliases' waves 22-30 "
    "uninterrupted. Pushes into genuinely new registers across the run: doctrine committed to "
    "writing for the first time (a single page of principle, its loss and independent "
    "corroboration, and a liberated town adopting its own version); new terrain (high-altitude thin "
    "air, a landslide rescue, a wide-open salt flat); a Voris successor inheriting institutional "
    "legacy without contradicting Voris's own established retirement; a lineage member's own "
    "temptation toward personal vengeance, resisted; the first operation run by Kanja and all three "
    "generations of the direct teaching lineage together; the first genuine near-deception of Kanja "
    "himself and his first physical vulnerability from the receiving end (temporary deafness); a "
    "judicial testimony-extraction register and a self-imposed limit against using the craft on "
    "neutral sacred ground; a humanitarian grain-redistribution entry inverting the fourth "
    "generation's own falsified-ledger method; a scout's resisted bribery offer; a historian's and "
    "Voris's own independently-corroborating institutional records of the craft's true history; an "
    "extended operational lull explored as the craft's purest form; the third generation's own "
    "Voris-mirroring step toward judgment over frontline mastery; a full-circle return to the "
    "reclaimed Voskharen Wetlands origin site; a siege where the craft plays a purely background "
    "logistics role; and a valedictory closer that deliberately leaves the fifth-generation question "
    "open rather than resolving it. No new named characters were introduced across any of the 27 "
    "entries; every entry reused already-locked crew (Commandant Voris, the apprentice, the third and "
    "fourth generations, Corren Halst, Garren Hask, Callum Breck) or left figures unnamed per this "
    "alias's established convention. Abad's approval: \"lets do this 22nd Alias Chronicle wave for "
    "any/all of the eleven aliases to the 30th wave and you are to continue uninterrupted until "
    "completion this includes rigorous testing, commit, push to main origin.\""
)

NEW_RULES = [
    {
        "id": "MCD-1256",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The First Page\" (full narrative text at docs/lords-of-cian/chronicles/the-first-page.md), "
            "Crow King Alias Chronicle LXIV, wave 22, opening it. The third generation writes the "
            "lineage's underlying discipline -- not tactics, but principle: listen before you act, "
            "restraint over cleverness -- down as a single page of text for the first time, showing it "
            "to Kanja before anyone else. Extends the generational-transmission theme into a "
            "doctrine-as-text register. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1257",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Page That Went Missing\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-page-that-went-missing.md), Crow King Alias Chronicle "
            "LXV, wave 22. The single written page of doctrine (MCD-1256) is lost during a raid; the "
            "third generation and Kanja conclude the philosophy was never an exploitable secret, "
            "confirmed when a defecting Directorate clerk is found already circulating and living by "
            "the same values after reading it. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1258",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Fifth Generation Might Ask\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-fifth-generation-might-ask.md), Crow King Alias "
            "Chronicle LXVI, wave 22, closing it. The fourth generation is approached by an outsider "
            "wanting to learn the craft and brings the unresolved question of a fifth generation "
            "upward rather than deciding alone; Kanja explicitly declines to dictate an answer, "
            "framing it as a question the craft hasn't yet built a process for. Deliberately left "
            "open. No new named characters. Closes wave 22 (with MCD-1256 and MCD-1257)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1259",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Mountain That Ate His Voice\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-mountain-that-ate-his-voice.md), Crow King Alias "
            "Chronicle LXVII, wave 23, opening it. High-altitude thin air degrades sustained vocal "
            "projection during a mountain-pass crossing, the first purely environmental (not "
            "injury-based) limit on the Hymn-Engine's spoken half; the crew adapts with a new "
            "visual signal-flag pattern. Establishes mountain/high-altitude as a new terrain type for "
            "this alias. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1260",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Rescue With No One Chasing Them\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-rescue-with-no-one-chasing-them.md), Crow King Alias "
            "Chronicle LXVIII, wave 23. A mountain landslide traps villagers with zero adversary "
            "anywhere in the story; the craft's coordination discipline (not its deception) is used "
            "purely for search-and-rescue, with a real, unsoftened partial loss (one of four victims "
            "not recovered in time). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1261",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Foreign Magistrate's Report\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-foreign-magistrates-report.md), Crow King Alias "
            "Chronicle LXIX, wave 23, closing it. A neutral Sovereign Trust magistrate formally "
            "documents the Hymn-Engine's true, unembellished history -- including its failures -- for "
            "an official cross-border archival record, the first institutional (rather than folk) "
            "documentation of the phenomenon. No new named characters. Closes wave 23 (with MCD-1259 "
            "and MCD-1260)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1262",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Second Who Became the First\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-second-who-became-the-first.md), Crow King Alias "
            "Chronicle LXX, wave 24, opening it. Commandant Voris's former second, now promoted in "
            "his place after Voris's voluntary step-back from active pursuit, faces the craft for the "
            "first time without Voris's own field re-engagement, consulting the retired Voris directly "
            "for guidance rather than a solution. Does not contradict Voris's established retirement "
            "(MCD-860). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1263",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Officer Kanja Chose Not to Ruin\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-officer-kanja-chose-not-to-ruin.md), Crow King Alias "
            "Chronicle LXXI, wave 24. The third generation is tempted toward using gathered "
            "intelligence for personal vengeance-by-information against a Directorate officer "
            "responsible for real harm; Kanja persuades her to use it only for its tactical value, "
            "the first entry where this temptation is felt by a lineage member rather than by Kanja "
            "himself. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1264",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"All Four Voices at Once\" (full narrative text at "
            "docs/lords-of-cian/chronicles/all-four-voices-at-once.md), Crow King Alias Chronicle "
            "LXXII, wave 24, closing it. The first operation run by Kanja and all three generations "
            "of the direct teaching lineage (the apprentice, the third generation, the fourth "
            "generation) together in one coordinated action, each contributing a distinct method, "
            "distinct from the multi-practitioner five-province operation (MCD-858). No new named "
            "characters. Closes wave 24 (with MCD-1262 and MCD-1263)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1265",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Hunter Who Studied the Hunter\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-hunter-who-studied-the-hunter.md), Crow King Alias "
            "Chronicle LXXIII, wave 25, opening it. A Directorate officer builds a false signal "
            "specifically to deceive Kanja himself by exploiting the Hymn-Engine's own logic; Kanja "
            "nearly takes it, caught only when the fourth generation cross-checks the sources' "
            "suspicious over-consistency. The first entry where Kanja is nearly fooled by his own "
            "method, resolved through the lineage's collective check rather than personal "
            "infallibility. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1266",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Silence After the Blast\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-silence-after-the-blast.md), Crow King Alias Chronicle "
            "LXXIV, wave 25. An explosion temporarily deafens Kanja mid-operation; the lineage carries "
            "the deception via the tap-signal relay and the apprentice's own unaided Braid for the "
            "first time without his participation or verification, the second physical limit landed "
            "on Kanja personally (after his throat wound, MCD-915), this time from the receiving end. "
            "No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1267",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Crew Never Said Out Loud\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-crew-never-said-out-loud.md), Crow King Alias "
            "Chronicle LXXV, wave 25, closing it. Callum Breck reflects on Kanja's near-deception and "
            "temporary deafness (MCD-1265, MCD-1266), drawing a direct parallel to his own already-"
            "locked four-month post-Black-Trench silence, and concludes the crew trusts Kanja more, "
            "not less, for needing them. Garren Hask reused for continuity. No new named characters. "
            "Closes wave 25 (with MCD-1265 and MCD-1266)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1268",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Testimony That Wasn't a Lie\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-testimony-that-wasnt-a-lie.md), Crow King Alias "
            "Chronicle LXXVI, wave 26, opening it. A captured Directorate soldier is brought before a "
            "newly-liberated town's improvised council; the fourth generation extracts truthful "
            "testimony not through deception but by laying out verified truth until lying against it "
            "stops being worth the effort -- a judicial/tribunal register extending 'verified truth as "
            "leverage.' No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1269",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Temple Would Not Allow\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-temple-would-not-allow.md), Crow King Alias "
            "Chronicle LXXVII, wave 26. The lineage self-imposes a limit against using the craft on a "
            "neutral shrine both warring sides have left unspoken-for by mutual agreement, taking a "
            "slower, costlier route instead -- the first entry establishing a location-based (rather "
            "than person-based) ethical constraint on the craft. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1270",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Council That Wrote It Into Practice\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-council-that-wrote-it-into-practice.md), Crow King "
            "Alias Chronicle LXXVIII, wave 26, closing it. A liberated town's council, having "
            "benefited from the craft's restraint-based testimony method (MCD-1268), formally adapts "
            "its own version of the underlying principles into local governing custom, building it in "
            "their own words rather than copying the crew's. No new named characters. Closes wave 26 "
            "(with MCD-1268 and MCD-1269)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1271",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Salt Flat Sang Wrong\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-salt-flat-sang-wrong.md), Crow King Alias Chronicle "
            "LXXIX, wave 27, opening it. A wide-open desert salt flat's long acoustic carry and "
            "heat-shimmer visual distortion are exploited together to throw a false troop count across "
            "the horizon, establishing salt-flat/desert as a new zero-cover terrain type distinct from "
            "every prior concealment-dependent environment. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1272",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Grain Convoy Never Reported\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-grain-convoy-never-reported.md), Crow King Alias "
            "Chronicle LXXX, wave 27. The fourth generation inverts his own falsified-ledger method "
            "(MCD-1077) to quietly redirect a Directorate-requisitioned grain reserve to starving "
            "settlements during a drought unrelated to the war, a purely humanitarian/economic-justice "
            "register with zero combat. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1273",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The One Who Almost Sold It\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-one-who-almost-sold-it.md), Crow King Alias Chronicle "
            "LXXXI, wave 27, closing it. One of the twenty trained scouts (MCD-917/MCD-990) is offered "
            "a large sum to sell the craft's real methods to a rival power; she refuses after genuine "
            "hesitation and self-reports it unprompted, testing the established authentication "
            "safeguards against internal temptation rather than external coercion for the first time. "
            "No new named characters. Closes wave 27 (with MCD-1271 and MCD-1272)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1274",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Scholar Who Wanted the Whole Truth\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-scholar-who-wanted-the-whole-truth.md), Crow King Alias "
            "Chronicle LXXXII, wave 28, opening it. A historian seeks out Corren Halst and others to "
            "document the Hymn-Engine's true, unembellished history against the exaggerated folk "
            "legend (MCD-833), producing the first crew-side institutional historical record. Corren "
            "Halst reused for continuity. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1275",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Days Nobody Sang\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-days-nobody-sang.md), Crow King Alias Chronicle "
            "LXXXIII, wave 28. A four-month operational lull during relative peace prompts the fourth "
            "generation and the apprentice to consider whether the craft's readiness atrophies without "
            "use, concluding that staying ready without anything to be ready for is itself the "
            "discipline's hardest and purest practice. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1276",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Third Generation Chose to Keep\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-third-generation-chose-to-keep.md), Crow King "
            "Alias Chronicle LXXXIV, wave 28, closing it. The third generation, experienced enough now "
            "to mirror Commandant Voris's own arc, decides to shift her primary role from frontline "
            "operations toward judgment -- deciding who learns next and what the craft becomes -- "
            "without stepping away from the craft entirely. No new named characters. Closes wave 28 "
            "(with MCD-1274 and MCD-1275)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1277",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Return to the Wetlands\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-return-to-the-wetlands.md), Crow King Alias Chronicle "
            "LXXXV, wave 29, opening it. Decades later, the lineage detours to the original Voskharen "
            "Wetlands compound (MCD-236), now fully reclaimed by the marsh with no trace of the "
            "original command platform or scarecrow left, a low-conflict full-circle callback to the "
            "Hymn-Engine's origin. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1278",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Siege That Needed No Braid\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-siege-that-needed-no-braid.md), Crow King Alias "
            "Chronicle LXXXVI, wave 29. During a three-week siege, the fourth generation applies his "
            "exacting numeric discipline to keeping Garren Hask's genuine, true supply accounting "
            "honest across a dozen supply lines rather than fabricating anything, showing the craft in "
            "a purely background logistics role for the first time. Garren Hask reused for continuity. "
            "No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1279",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Held When Nothing Else Did\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-held-when-nothing-else-did.md), Crow King Alias "
            "Chronicle LXXXVII, wave 29, closing it. Kanja and the apprentice reflect across the full "
            "span of the alias's run since the Night of the Crow King, concluding the discipline of "
            "listening and restraint, not any single trick, is what has let the craft outlast every "
            "countermeasure built against it. No new named characters. Closes wave 29 (with MCD-1277 "
            "and MCD-1278)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1280",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Question the Fourth Generation Finally Asked\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-question-the-fourth-generation-finally-asked.md), Crow "
            "King Alias Chronicle LXXXVIII, wave 30, opening it. The same runner's son from MCD-1258 "
            "returns; the fourth generation brings him publicly to Kanja and the third generation "
            "together rather than deciding alone, advancing the unresolved fifth-generation question "
            "without fully closing it. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1281",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Commandant's Last Report\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-commandants-last-report.md), Crow King Alias Chronicle "
            "LXXXIX, wave 30. A fully-retired Voris writes a final, honest retrospective report for "
            "the Directorate's own historical archive, concluding the method could never be studied to "
            "exhaustion because it stopped being one man's method before he finished studying it -- a "
            "Directorate-side institutional record paralleling MCD-1274, consistent with his "
            "established retirement (MCD-860). No new named characters beyond the already-locked "
            "Commandant Voris."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1282",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Legend That Finally Told the Truth\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-legend-that-finally-told-the-truth.md), Crow King Alias "
            "Chronicle XC, wave 30, closing it. The scholar's record (MCD-1274) and Voris's report "
            "(MCD-1281) reach the fourth generation independently and match almost everywhere it "
            "matters; the valedictory closer for the thirtieth wave deliberately leaves the "
            "fifth-generation question (MCD-1258, MCD-1280) open rather than resolving it. No new "
            "named characters. Closes wave 30 (with MCD-1280 and MCD-1281) and this run."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 27, f"expected 27 new rules, got {len(NEW_RULES)}"

    for r in NEW_RULES:
        assert r["category"] == "kanja-alias-chronicle", f"bad category on {r['id']}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 260,
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
