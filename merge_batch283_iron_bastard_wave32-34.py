#!/usr/bin/env python3
"""Batch 283: Iron Bastard Alias Chronicle waves 32-34 (9 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Continues the Alias Chronicle sub-series' thirty-second, thirty-third, and thirty-fourth "
    "waves for the Iron Bastard, under Abad's direct authorization: \"do 3 more alias wave for all "
    "eleven.\" Wave 32 opens the doctrine's first application to a natural geological formation with "
    "no builder, forger, or living growth cycle behind it -- a sea-cliff overhang above a fishing "
    "settlement, read to a genuinely mixed, non-resolving finding rather than a clean verdict -- then "
    "a detailed full-Trinity combat showcase where raiders weaponize that exact fracture, forcing "
    "Kanja to redirect an unstoppable rockfall's outcome rather than prevent it, and closes on an "
    "entirely informal, non-Talisman lay hazard-watch tradition, the doctrine's simplest possible "
    "transmission. Wave 33 opens a new financial-crime register (a merchant's own deliberate "
    "insurance-fraud sabotage of his own warehouse, resolved diagnostically with no discharge), then "
    "a detailed full-Trinity combat showcase in a fully confined underground mine shaft -- the "
    "doctrine's first application in that environment, combining close-quarters combat with an "
    "echo-distorted structural read on destabilized support timbers -- and closes on the miners' "
    "guild formally requesting a standing doctrine-trained inspectorate, filled by the already-locked "
    "second student in the doctrine's first sector-specific institutional post. Wave 34 opens the "
    "doctrine's first fully tactile curriculum, built for a stonemason deaf since birth, establishing "
    "the core insight was never dependent on hearing; then a detailed full-Trinity combat showcase on "
    "a floating pontoon river crossing whose tension baseline never holds still, extending the "
    "continuous-monitoring technique from `MCD-1305` into real-time combat for the first time; and "
    "closes with a years-later return to the living fig-root bridge of `MCD-1283`, confirming its "
    "long-term growth vindicated the original choice not to discharge against it. No new named "
    "characters across all nine entries, consistent with this alias's long-established convention of "
    "unnamed recurring roles -- every entry reused already-locked crew (the second student, `MCD-719`) "
    "or newly introduced unnamed one-scene figures for continuity depth instead. Abad's approval: "
    "\"do 3 more alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1487",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Cliff That Had Never Been Taught to Lie\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-cliff-that-had-never-been-taught-to-lie.md), Iron "
            "Bastard Alias Chronicle XCIV, wave 32, first entry. The doctrine's first application "
            "to a natural rock formation with no design intent, forger, or living growth cycle "
            "behind it -- a sea-cliff overhang above a fishing settlement, distinct from every "
            "prior tension-bearing category (forged metal, `MCD-238`; wood/rope/lashing, "
            "`MCD-420`; living/growing tissue, `MCD-1283`). Kanja constructs an ad hoc baseline "
            "from the formation's own accumulated geological history and delivers a genuinely "
            "mixed, non-resolving finding -- partial, long-horizon risk rather than a clean "
            "safe/unsafe verdict -- extending the doctrine's stated epistemic limit (tension only, "
            "never meaning or prescription, `MCD-967`/`1299`) into open-ended timeframes. No "
            "discharge occurs; purely diagnostic. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1488",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Mountain Threw Down With Them\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-mountain-threw-down-with-them.md), Iron "
            "Bastard Alias Chronicle XCV, wave 32. A detailed, battle-intense full-Trinity combat "
            "showcase: raiders deliberately weaponize the exact geological fracture identified in "
            "`MCD-1487`, forcing Kanja to redirect an unstoppable rockfall's outcome away from the "
            "settlement rather than prevent or stop it, distinct from the no-enemy earthquake-"
            "triage entries (`MCD-1295`/`1296`) and every prior enemy-Crawler/structure engagement "
            "against a designed object rather than a natural formation. Mafesto's Kinetic Transfer "
            "System absorbs incoming fire, Onyx of Oblivion's Cadence Ruin, Veil Piercer, and "
            "Whisper of Shadows clear the vanguard (`ARS-020`), and Obsidian Malice's discharge, "
            "confirmed by doubled verification (`MCD-497`) under extreme time pressure, redirects "
            "the rockfall's true weak point into an empty ravine. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1489",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Watch They Kept After He Left\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-watch-they-kept-after-he-left.md), Iron Bastard "
            "Alias Chronicle XCVI, wave 32, closing the wave. An entirely informal, non-Talisman, "
            "single-gesture lay hazard-watch tradition begins at the settlement from `MCD-1487`/"
            "`1488`, distinct from every formal teaching lineage in the ledger (the first through "
            "third-generation students, `MCD-499`/`719`/`967`; the twelve-volunteer cohort, "
            "`MCD-1048`; the chartered academic discipline, `MCD-1307`) -- no mechanics or "
            "discharge is transmitted, only a memorized sensory baseline, extending the free-"
            "teaching principle to its simplest possible form. No new named characters. Closes "
            "the Iron Bastard's thirty-second wave (with `MCD-1487` and `MCD-1488`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1490",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Collapse That Was Never an Accident\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-collapse-that-was-never-an-accident.md), Iron "
            "Bastard Alias Chronicle XCVII, wave 33, first entry. A new financial-crime register: "
            "the doctrine detects a guild merchant's own deliberate sabotage of his own warehouse "
            "for indemnity-fund insurance fraud, distinct from the freelance-mercenary corruption "
            "of the doctrine's name (`MCD-899`), the false accusation leveled against Kanja "
            "personally (`MCD-965`), and every falsified-signature deception aimed at defeating a "
            "live discharge (`MCD-550`). Purely diagnostic and civil; no discharge occurs; "
            "resolution is guild restitution and suspension, not violence. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1491",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Shaft That Was Built to Bury Them\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-shaft-that-was-built-to-bury-them.md), Iron "
            "Bastard Alias Chronicle XCVIII, wave 33. A detailed, battle-intense full-Trinity "
            "combat showcase: the doctrine's first application inside a fully confined "
            "underground mine shaft, combining close-quarters combat against an ambush left "
            "behind to prevent rescue with a high-stakes, echo-distorted structural read on "
            "multiple already-destabilized support timbers, distinct from the acoustically-"
            "deadened vault (`MCD-712`, doctrine defeated outright, no combat) since confinement "
            "here distorts rather than blocks the read, requiring direct hand-to-timber contact "
            "and doubled verification (`MCD-497`) on every beam. Onyx of Oblivion's Whisper of "
            "Shadows, Cadence Ruin, and Soulbound Edge (`ARS-020`) clear the ambush in confined "
            "quarters, and Mafesto's Kinetic Transfer System redirects a melee strike into the "
            "tunnel wall. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1492",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Guild That Asked for Ears of Their Own\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-guild-that-asked-for-ears-of-their-own.md), Iron "
            "Bastard Alias Chronicle XCIX, wave 33, closing the wave. The miners' guild from "
            "`MCD-1491` formally requests a standing doctrine-trained inspectorate rather than "
            "ownership of the method, a new sector-specific institutional-adoption register "
            "distinct from Trust academy curriculum taught without Kanja present (`MCD-723`), the "
            "declined exclusive licensing offer (`MCD-1082`), and the chartered academic "
            "discipline (`MCD-1307`); the already-locked second student (`MCD-719`) fills the "
            "doctrine's first standing professional inspectorate post. No new named characters. "
            "Closes the Iron Bastard's thirty-third wave (with `MCD-1490` and `MCD-1491`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1493",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What His Hands Heard Instead\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-his-hands-heard-instead.md), Iron Bastard Alias "
            "Chronicle C, wave 34, first entry. A new inclusion/adaptation register: the "
            "doctrine's first fully tactile curriculum, built from the ground up for a stonemason "
            "deaf since birth, distinct from the Aegis-Talisman's own one-time device-independence "
            "entry (`MCD-963`, a temporary fallback for an already-trained master) since this is a "
            "permanent primary teaching mode for a new student, establishing the doctrine's core "
            "insight was never dependent on hearing and that a student never distracted by "
            "extraneous sound can read some signatures more cleanly. Self-contained single-entry "
            "arc, consistent with the alias's practice of one-off teaching vignettes (`MCD-737`, "
            "`MCD-965`) alongside its ongoing formal lineage. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1494",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Bridge That Answered to the Current\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-bridge-that-answered-to-the-current.md), Iron "
            "Bastard Alias Chronicle CI, wave 34. A detailed, battle-intense full-Trinity combat "
            "showcase: the doctrine's first application to a structure whose tension baseline "
            "never holds still, a lashed pontoon river crossing that shifts continuously with "
            "current, distinct from fixed naval rigging (`MCD-498`) and a storm-strained but "
            "structurally static keel (`MCD-1305`), and from the living fig-root bridge's own "
            "slow biological cycle (`MCD-1283`). Extends the continuous-monitoring technique "
            "first developed for the keel read (`MCD-1305`) into real-time combat conditions for "
            "the first time. Mafesto's Kinetic Transfer System absorbs incoming fire, Onyx of "
            "Oblivion's Cadence Ruin steadies the crossing column, and Obsidian Malice's discharge "
            "is used constructively to reinforce a failing mooring lashing rather than "
            "destructively against a target. The second student (`MCD-719`) appears in "
            "supporting capacity. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1495",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Roots Grew Into\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-roots-grew-into.md), Iron Bastard Alias "
            "Chronicle CII, wave 34, closing the wave. A legacy-callback register, the first "
            "entry in this alias's run to return to a specific prior location years later purely "
            "to confirm a long-term outcome rather than advance a new mechanic, threat, or "
            "relationship: the living fig-root bridge (`MCD-1283`) has grown thicker and "
            "stronger exactly as its self-protecting nature predicted, now bearing a market and "
            "significantly increased foot traffic, vindicating the original decision not to "
            "discharge against it. The second student (`MCD-719`) appears in a substantial "
            "reflective role. No new named characters. Closes the Iron Bastard's thirty-fourth "
            "wave (with `MCD-1493` and `MCD-1494`) and this run's three-wave arc (32-34)."
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
            "batch": 283,
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
