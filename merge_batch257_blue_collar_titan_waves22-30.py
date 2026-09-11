#!/usr/bin/env python3
"""Batch 257: Blue-Collar Titan Alias Chronicle waves 22-30 (27 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Blue-Collar Titan's twenty-second through thirtieth Alias Chronicle waves (9 waves, 27 "
    "entries), drafted under Abad's blanket authorization to continue all eleven aliases' waves "
    "22-30 uninterrupted. Pushes into registers never used across the alias's prior 21 waves: a "
    "genuine natural disaster (seismic tremor), two new hazard types (corrosive acid vapor, "
    "geothermal heat), false-blame/reputation-defense turned inward, a land-boundary civil dispute, "
    "a child-labor discovery and institutional enforcement, Kanja's own temporary blindness forcing "
    "reliance on the tactile method he was taught, a self-governing workers' council founded and "
    "later formally reprimanding him, a civilian-occupied strategic self-flooding evacuation, a "
    "generational-reunion payoff (the widow's son), a propaganda/authenticity refusal, a deferred-"
    "consequence entry about a reasoned-not-rushed design choice, proactive peacetime housing "
    "construction, a fatigue/complacency safety-culture entry, a long-term defector-integration "
    "payoff, a new non-combat application of Mafesto's density-sensing register, a second-voice "
    "legacy ledger from Efa Gol, a weather-driven (not enemy-driven) surface flood, a despair/will-"
    "to-live rescue register, the taught apprentice correcting his own teacher, a multi-party "
    "criminal standoff, and a full run-closing trilogy: the siege's final certification, the first "
    "purely peacetime project, and a Killane-specific oral-history capstone. No new named "
    "characters were introduced across any of the 27 entries -- every new figure (the stonemason, "
    "the widow's son, the defected engineer, the journeyman, council representatives, and others) "
    "is deliberately kept unnamed and one-scene, matching this alias's strong established "
    "precedent, and every returning figure (Corren Halst, Danne Sok, Garren Hask, Efa Gol, Dol "
    "Maren) is reused from already-locked crew, collision-checked clean against the full ledger "
    "before drafting. Abad's approval: \"lets do this 22nd Alias Chronicle wave for any/all of the "
    "eleven aliases to the 30th wave and you are to continue uninterrupted until completion this "
    "includes rigorous testing, commit, push to main origin.\""
)

NEW_RULES = [
    {
        "id": "MCD-1175",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ground That Moved on Its Own\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ground-that-moved-on-its-own.md), Blue-Collar Titan "
            "Alias Chronicle LXIV, wave 22, opening the wave. The alias's first genuine natural-"
            "disaster entry with zero enemy involvement -- a seismic tremor sequence Kanja predicts "
            "and evacuates ahead of using a new predictive application of Mafesto's Kinetic Transfer "
            "System, with Obsidian Malice used as emergency shoring rather than a weapon. Reuses "
            "already-locked crew member Danne Sok. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1176",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Blame That Wasn't His to Clear\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-blame-that-wasnt-his-to-clear.md), Blue-Collar Titan "
            "Alias Chronicle LXV, wave 22. A reputation-defense entry -- Directorate propaganda "
            "falsely blames the Blue-Collar Titan for a collapse he didn't cause; rather than deny "
            "it in his own voice and let his name do the work, Kanja funds an independent forensic "
            "account that outcompetes the lie with better-sourced truth, extending the alias's "
            "structural-honesty ethos into self-defense. Reuses already-locked crew member Garren "
            "Hask. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1177",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What She Built Without Him Watching\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-she-built-without-him-watching.md), Blue-Collar "
            "Titan Alias Chronicle LXVI, wave 22, closing the wave. A letting-go mentorship entry: "
            "Kanja deliberately withholds his own inspection from the previously-sponsored "
            "stonemason's (MCD-1069) first fully solo repair project, resisting the urge to quietly "
            "check her work, and is rewarded when she later treats him as a peer rather than a "
            "sponsor for the first time. Reuses the unnamed stonemason from MCD-1069 and already-"
            "locked crew member Garren Hask. No new named characters. Closes wave 22."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1178",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fumes That Ate the Iron\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fumes-that-ate-the-iron.md), Blue-Collar Titan Alias "
            "Chronicle LXVII, wave 23, opening the wave. The alias's first corrosive/acid-vapor "
            "hazard: a breached mineral-runoff cistern eats iron and stone alike, forcing both "
            "Obsidian Malice and Onyx of Oblivion's Soulbound Edge to be deliberately withheld due "
            "to alloy-corrosion risk, resolved through Mafesto's terrain-reading and Onyx's Cadence "
            "Ruin alone. Reuses already-locked crew member Corren Halst. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1179",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Line No Deed Could Settle\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-line-no-deed-could-settle.md), Blue-Collar Titan "
            "Alias Chronicle LXVIII, wave 23. A civil property-boundary dispute between two "
            "civilian families, resolved through an honest physical survey of old foundation lines "
            "rather than a ruling for either side, extending the alias's structural-honesty method "
            "into land law for the first time. Reuses already-locked crew member Garren Hask. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1180",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ones Too Small to Dig\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ones-too-small-to-dig.md), Blue-Collar Titan Alias "
            "Chronicle LXIX, wave 23, closing the wave. Kanja discovers and rescues six illegally "
            "employed children being used by a subcontractor to work a narrow gallery evading the "
            "safety-training institution (MCD-657); the tradesmen's association (MCD-662) enforces "
            "a hard minimum age into its charter as a result, its first real enforcement test "
            "independent of Kanja's approval. Handled entirely as rescue and labor-rights reform "
            "with zero sexualized content. No new named characters. Closes wave 23."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1181",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Heat That Came Up From Below\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-heat-that-came-up-from-below.md), Blue-Collar Titan "
            "Alias Chronicle LXX, wave 24, opening the wave. The alias's first geothermal/extreme-"
            "heat hazard -- an unexpected earth-heat vent with no fire to extinguish, resolved by "
            "rerouting the excavation using a new thermal-gradient application of Mafesto's Kinetic "
            "Transfer System and efficient quarrying with Obsidian Malice. Reuses already-locked "
            "crew member Danne Sok. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1182",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What He Read With His Eyes Shut\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-he-read-with-his-eyes-shut.md), Blue-Collar Titan "
            "Alias Chronicle LXXI, wave 24. The alias's first entry centered on Kanja's own "
            "temporary incapacitation: blinded by dust mid-rescue, he completes a four-person "
            "extraction entirely through the tactile method taught by the old Killane digger "
            "(MCD-442), a direct payoff showing that lesson save him rather than others. Reuses "
            "already-locked crew member Corren Halst. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1183",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Council That Built Itself\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-council-that-built-itself.md), Blue-Collar Titan "
            "Alias Chronicle LXXII, wave 24, closing the wave. Workers formally establish a self-"
            "governing council with real voting authority, synthesizing the safety-training "
            "institution (MCD-657), the tradesmen's association (MCD-662), and the wage-dispute "
            "resolution (MCD-1070) into one lasting body; Kanja declines a unanimous offer of a "
            "permanent seat, accepting only a non-voting advisory role. Reuses already-locked crew "
            "member Garren Hask and the unnamed mucker from MCD-1070. No new named characters. "
            "Closes wave 24."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1184",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Signal That Meant Run\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-signal-that-meant-run.md), Blue-Collar Titan Alias "
            "Chronicle LXXIII, wave 25, opening the wave. A mass strategic-evacuation entry: "
            "resistance command orders Kanja to flood a civilian-occupied gallery he himself built "
            "to deny a Trust breakthrough, requiring the evacuation of 311 sheltering civilians and "
            "the flood's engineering to run as two interdependent clocks, raising the stakes of "
            "self-inflicted demolition beyond the empty-causeway precedent (MCD-891). Reuses "
            "already-locked crew members Efa Gol and Corren Halst. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1185",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Widow's Son Returned\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-widows-son-returned.md), Blue-Collar Titan Alias "
            "Chronicle LXXIV, wave 25. A generational payoff to \"The Widow Who Wouldn't Thank Him\" "
            "(MCD-677): her grown son returns years later asking to be trained in the trade that "
            "killed his father, choosing his own path separately from his mother's still-unresolved "
            "refusal of reconciliation. The son remains unnamed. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1186",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Exhibition They Wanted Him to Perform\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-exhibition-they-wanted-him-to-perform.md), Blue-"
            "Collar Titan Alias Chronicle LXXV, wave 25, closing the wave. Kanja refuses the "
            "resistance's own information office's request for a staged Trinity demonstration for "
            "morale, and substitutes a genuine, unscripted public repair of a broken aqueduct "
            "instead, extending the alias's refusal-to-fabricate principle into self-directed "
            "propaganda. No new named characters. Closes wave 25."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1187",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Reckoning of a Design Choice\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-reckoning-of-a-design-choice.md), Blue-Collar Titan "
            "Alias Chronicle LXXVI, wave 26, opening the wave. A deferred-consequence entry: a "
            "reasoned, defensible support-spacing compromise Kanja made under real time pressure "
            "years earlier surfaces a hidden structural cost only now, distinct from the in-the-"
            "moment rushed error of MCD-665 -- he reinforces the section at real cost and writes "
            "the decision and its consequence into training material rather than quietly "
            "correcting it. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1188",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Roof Before the Ledger\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-roof-before-the-ledger.md), Blue-Collar Titan Alias "
            "Chronicle LXXVII, wave 26. A proactive civilian-housing entry with zero crisis, "
            "combat, or rescue framing: Kanja spends nine unglamorous days building resettlement "
            "housing for 400 displaced families alongside civilian carpenters. Reuses already-"
            "locked crew member Garren Hask. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1189",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Watch That Forgot to Rest\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-watch-that-forgot-to-rest.md), Blue-Collar Titan "
            "Alias Chronicle LXXVIII, wave 26, closing the wave. A fatigue/complacency safety-"
            "culture entry: a near-miss caused by a night crew's gradually normalized overwork "
            "prompts Kanja to impose hard rotation caps and model the discipline himself, the "
            "threat here being internal exhaustion rather than any external enemy. Reuses already-"
            "locked crew member Garren Hask. No new named characters. Closes wave 26."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1190",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Engineer Who Stayed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-engineer-who-stayed.md), Blue-Collar Titan Alias "
            "Chronicle LXXIX, wave 27, opening the wave. A long-term-integration payoff to \"The "
            "Engineer Who Built Against Him\" (MCD-668): the defected Trust engineer's standing "
            "with the crew is tested eight months later when his former command sends a delegation "
            "to reclaim him, and Kanja backs him without speaking for him, letting the engineer "
            "argue his own choice. The engineer remains unnamed. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1191",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Weight Method Found\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-weight-method-found.md), Blue-Collar Titan "
            "Alias Chronicle LXXX, wave 27. A non-combat forensic entry extending Mafesto's density/"
            "weight-sensing register introduced in MCD-1068 into a new application: detecting a "
            "hidden counterfeit-currency cache by mass discrepancy alone, distinct from the manual "
            "weighing method of MCD-654. Reuses already-locked crew member Garren Hask and "
            "references the workers' council (MCD-1183). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1192",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ledger Efa Gol Kept Herself\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ledger-efa-gol-kept-herself.md), Blue-Collar Titan "
            "Alias Chronicle LXXXI, wave 27, closing the wave. A second-voice legacy-accounting "
            "entry distinct from Garren Hask's cost ledger (MCD-680): Efa Gol reveals her own "
            "independent record of every worker saved and every near-miss carried across her time "
            "with this alias since MCD-1012, and asks that it join the formal record. Reuses "
            "already-locked crew members Efa Gol and Garren Hask. No new named characters. Closes "
            "wave 27."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1193",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Storm That Found the Seams\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-storm-that-found-the-seams.md), Blue-Collar Titan "
            "Alias Chronicle LXXXII, wave 28, opening the wave. A weather-driven, not enemy-driven, "
            "surface-to-underground flooding crisis with no single breach point, requiring live "
            "coordination between Kanja underground and Dol Maren on the surface, resolved by "
            "mapping pressure differentials and cutting new emergency drainage. Reuses already-"
            "locked crew member Dol Maren. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1194",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Man Who Wouldn't Be Rescued\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-man-who-wouldnt-be-rescued.md), Blue-Collar Titan "
            "Alias Chronicle LXXXIII, wave 28. The alias's first despair/will-to-live rescue "
            "register: a trapped worker in shock has resigned himself to being unrecoverable, and "
            "Kanja must sustain verbal engagement alongside physical extraction to win back his "
            "will to be saved. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1195",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Apprentice Who Said No\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-apprentice-who-said-no.md), Blue-Collar Titan Alias "
            "Chronicle LXXXIV, wave 28, closing the wave. The taught lineage comes full circle: the "
            "orphaned boy from MCD-653, now a master via MCD-1036, corrects Kanja's own proposed "
            "shoring method with superior field evidence, and Kanja accepts the correction without "
            "hesitation. The journeyman remains unnamed. No new named characters. Closes wave 28."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1196",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Two Tunnels That Never Should Have Met\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-two-tunnels-that-never-should-have-met.md), Blue-"
            "Collar Titan Alias Chronicle LXXXV, wave 29, opening the wave. A multi-party criminal "
            "standoff entry: two unrelated illicit operations digging toward the same unclaimed "
            "passage from opposite ends confront each other, and Kanja defuses the standoff from a "
            "neutral position without enforcing for or against either. Reuses already-locked crew "
            "member Danne Sok. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1197",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Complaint Filed Against Himself\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-complaint-filed-against-himself.md), Blue-Collar "
            "Titan Alias Chronicle LXXXVI, wave 29. The workers' council (MCD-1183) files a formal "
            "grievance against Kanja over a unilateral evacuation decision from MCD-1068; he "
            "submits fully to the hearing process rather than defending himself outside it, and the "
            "council's ruling adds a faster emergency-authorization clause rather than overturning "
            "the underlying decision -- the council's first real test of authority over its own "
            "founder. Reuses already-locked crew member Garren Hask. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1198",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Last Reading Before the Peace\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-last-reading-before-the-peace.md), Blue-Collar Titan "
            "Alias Chronicle LXXXVII, wave 29, closing the wave. Set at the literal moment the "
            "Sewer War of Killane's ceasefire (MCD-234) takes effect: Kanja performs one final full "
            "structural certification of the entire tunnel network, confirming the eastern gallery "
            "from MCD-485 has settled stable, closing the alias's central historical anchor. Reuses "
            "already-locked crew member Corren Halst. No new named characters. Closes wave 29."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1199",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The First Thing He Built After the War\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-first-thing-he-built-after-the-war.md), Blue-Collar "
            "Titan Alias Chronicle LXXXVIII, wave 30, opening the wave. A peacetime coda set just "
            "after MCD-1198: Kanja builds an ordinary working well at a plaza with no crisis "
            "attached to it at all, the alias's first entirely unforced project, contrasting thirty "
            "waves of crisis-driven urgency with unhurried, quiet labor. Reuses already-locked crew "
            "member Garren Hask. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1200",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Outlived the Alias\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-outlived-the-alias.md), Blue-Collar Titan Alias "
            "Chronicle LXXXIX, wave 30. A synthesis entry set years after the war: the smiths' "
            "guild (MCD-409/MCD-539), the tradesmen's association (MCD-662), and the workers' "
            "council (MCD-1183/MCD-1197) are all shown functioning fully independently of Kanja's "
            "presence, the fullest payoff of the alias's institution-building arc. Reuses the "
            "unnamed journeyman from MCD-653/MCD-1036. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1201",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Last Name Anyone Used for Him There\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-last-name-anyone-used-for-him-there.md), Blue-Collar "
            "Titan Alias Chronicle XC, wave 30, closing the wave. A final Killane-specific oral-"
            "history capstone: Danne Sok, decades later, tells a young apprentice what the Blue-"
            "Collar Titan actually meant to the people who lived through the siege -- that he never "
            "let them believe the tunnels held together only because of his strength, distinct from "
            "both prior closer registers (MCD-680's ledger, MCD-671's cross-alias comparison). "
            "Reuses already-locked crew member Danne Sok. No new named characters. Closes wave 30 "
            "and this run's full nine-wave arc (waves 22-30)."
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
            "batch": 257,
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
