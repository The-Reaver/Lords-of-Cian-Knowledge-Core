#!/usr/bin/env python3
"""Batch 236: Crow King Alias Chronicle wave 20 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Crow King's twentieth Alias Chronicle wave (three entries), continuing the same wave-20 pass "
    "run across all eleven aliases this session. \"What the Burned Ground Taught\" (MCD-1044) is the "
    "first entry across all twenty waves to dramatize the crew's own doctrinal response, in the field, "
    "to wave 19's genuine unrecovered regional breach (\"What They Couldn't Take Back,\" MCD-995) -- "
    "the third generation authors a deliberately irregular, partly manufactured operational rhythm to "
    "deny any future observer the consistent pattern that beat them once already, and explicitly claims "
    "only more time, not a fix. \"The Vault That Held No Light\" (MCD-1045) is a detailed full-Trinity "
    "combat showcase in total darkness -- a new location, Hollowmere Keep, collision-checked clean -- "
    "where a garrison commander strips all light from an underground vault on the mistaken premise that "
    "the Hymn-Engine and the Trinity are sight-dependent, handing Kanja the one environment where their "
    "acoustic and pressure-based design costs nothing at all. \"The Fourth Voice\" (MCD-1046) introduces "
    "the craft's fourth generation of transmission for the first time, with the third generation "
    "deliberately asking Kanja's judgment before teaching begins -- a self-imposed check distinct from "
    "the unasked starts of the two generations before her -- and closes the wave. No new named "
    "characters across any of the three entries; the new fourth-generation student is deliberately left "
    "unnamed, matching this alias's established convention of identifying lineage members by "
    "generational position rather than proper name. Abad's approval: \"doorway for all the aliases that "
    "remain\" (approval of Bane's individually-presented wave 20 plus blanket authorization to continue "
    "the same wave for the remaining ten aliases)."
)

NEW_RULES = [
    {
        "id": "MCD-1044",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Burned Ground Taught\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-burned-ground-taught.md), Crow King Alias Chronicle "
            "LVIII, wave 20, opening it. Direct follow-through on wave 19's unrecovered regional breach "
            "(\"What They Couldn't Take Back,\" MCD-995): months later, the crew returns not to the "
            "burned ground itself but to an uncompromised stretch of the same grain-road country to "
            "field-test a structural revision the third generation designed from Kanja's own diagnosis "
            "of the breach ('Not skill. Time.') -- a deliberately irregular, partly manufactured "
            "operational rhythm (real extractions, staged near-failures, unexplained stretches of "
            "inactivity, indistinguishable from outside the craft) built specifically to deny any single "
            "watching outpost a consistent enough pattern to study across a full season, as happened "
            "before. Against a garrison primed by secondhand knowledge of the earlier breach, it holds "
            "for six weeks, the garrison's own logs collapsing into unresolved contradictions. The third "
            "generation is explicit that this proves nothing solved, only bought time, honoring wave "
            "19's refusal to resolve the method's real limits into false confidence. No new named "
            "characters; the region and garrison stay unnamed, consistent with Chronicle LVII's own "
            "treatment."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1045",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Vault That Held No Light\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-vault-that-held-no-light.md), Crow King Alias Chronicle "
            "LIX, wave 20. A detailed full-Trinity combat showcase set in total darkness for the first "
            "time across all twenty waves: the garrison commander at Hollowmere Keep (new location, "
            "collision-checked clean), acting on captured fragments of doctrine, strips every light "
            "source from the Keep's underground prisoner vault on the premise that the Crow King's "
            "advantage is fundamentally visual, sealing the shaft to deny even ambient daylight. The "
            "premise is wrong on both counts he built it from: the Hymn-Engine was never sight-based, "
            "and neither is Onyx of Oblivion's own sensing. Cadence Ruin maps the vault's full layout "
            "and six-man guard rotation through acoustic reflection alone within four seconds; Veil "
            "Piercer confirms it through pressure and motion in the same absolute black, catching the "
            "one guard holding still enough to nearly go unheard; Mafesto's Kinetic Transfer System "
            "redirects a clustered rush into the wall the guards had been calling their own position "
            "from by voice; Obsidian Malice discharges twice, aimed by the same pressure-reading rather "
            "than sight. The vault clears in under two minutes; the commander's blindness advantage "
            "becomes Kanja's home-ground advantage instead. No new named characters; the garrison "
            "commander is unnamed and one-scene."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1046",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fourth Voice\" (full narrative text at docs/lords-of-cian/chronicles/the-fourth-"
            "voice.md), Crow King Alias Chronicle LX, wave 20, closing it. The craft's fourth generation "
            "of transmission begins for the first time: the third generation (already locked, MCD-548, "
            "MCD-994, MCD-995) asks Kanja's judgment before teaching a new student at all -- a "
            "two-year crew messenger-runner known for exact, unembellished recall -- deliberately "
            "distinct from how the craft passed to her, when the apprentice began teaching her without "
            "asking anyone first (Chronicle XV, MCD-548). Kanja meets the prospective student directly "
            "before endorsing the choice, and the teaching begins with the same foundational discipline "
            "passed down unchanged since Kanja's own original teaching: listening before cleverness. "
            "Framed explicitly as the craft maturing into something old enough to build its own consent "
            "process, not as a correction of the two generations that began without one. No new named "
            "characters; the fourth-generation student is deliberately left unnamed, consistent with "
            "this alias's established convention. Closes wave 20 (with \"What the Burned Ground Taught,\" "
            "MCD-1044, and \"The Vault That Held No Light,\" MCD-1045)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 3, f"expected 3 new rules, got {len(NEW_RULES)}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 236,
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
