#!/usr/bin/env python3
"""Batch 310: The Three Ronin hook mined from Beloved_and_Blade_Ronin_Victims.docx.

Nelle Adessi and Tomas Grieve (Part I of the source document) turned out already
well-covered at CC-123/CC-124 (Batch 55). Part II (the Three Ronin) and the SBD
Wet-Work Team section held real, unmined mechanism material behind reckonings
MCD-092 currently only names in one line each. Pure extension of already-locked
figures -- zero new proper nouns.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Beloved_and_Blade_Ronin_Victims.docx (Google Drive, Lore Vault)."

with open(LEDGER_PATH, "r", encoding="utf-8") as f:
    ledger = json.load(f)

existing_ids = {r["id"] for r in ledger["rules"]}

NEW_RULES = [
    {
        "id": "CC-144",
        "category": "Character",
        "statement": (
            "Extends CULT-070/POL-102: the Silence was a Praetorian in the Obsidian "
            "Prefecture (~640 years old, 2,800x) expelled from service for 'excessive "
            "brutality' during a civilian suppression operation -- the Prefecture "
            "punishes failure, not cruelty, so the act was severe enough that Dhampir "
            "Black (POL-102, Fourth Patriarch, the Prefecture's own most dangerous "
            "combatant) personally authorized the expulsion. His demonstrative-kill "
            "methodology doesn't humiliate a body, it stages it into a position of "
            "failure -- a guard's weapon drawn but unfired, a sentry facing the wrong "
            "direction -- so the arrangement itself communicates that the victim's "
            "training was never designed for what walked through the door. His trophy "
            "cord (extends CC-125) exists because everything he takes is proof, "
            "without distinguishing warriors from civilians -- the same logic that let "
            "a builder's carpenter's square hang beside 47 dead guards' insignia."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-145",
        "category": "Character",
        "statement": (
            "Extends MCD-092: the Ghost has never had, or no longer remembers, a true "
            "name -- roughly 200 documented identities across a 400-500-year career, "
            "born into a Lawless Reaches nomadic population that dissolved in "
            "childhood, with no cultural affiliation or institutional training to "
            "trace. Deliberately maintains the lowest viable density (~180x) since "
            "high density is what Density Sight users and atmospheric distortion "
            "actually detect -- the Ghost's entire tradecraft is 'already inside' "
            "rather than breaching anything, occupying an identity the way other "
            "people occupy a room. His Book 4 reckoning: Anansi's Ghost-Lattice web "
            "and Valeria Korth's Thread-Perception (CC-104) don't find the Ghost "
            "directly -- they detect the absence of causal and relational threads "
            "where a person should be, a void in the web. He is captured, not killed, "
            "and held permanently as a documented, nameless prisoner -- the one "
            "outcome an identity built entirely on formlessness cannot survive."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-146",
        "category": "Character",
        "statement": (
            "Extends CC-109: the Blade trained as a cultivated warrior in the "
            "Celestial Zenith -- the same tradition that produced Orlok (POL-105) -- "
            "before her expulsion for premeditated murder: she killed a fellow "
            "cultivator in a training exercise using a density-shift technique timed "
            "to the exact 0.04-second window where the opponent's guard transitioned "
            "between positions, a kill-capability the Pavilion's own masters couldn't "
            "defend against. Her motive was never established; she offered no "
            "explanation and took the technique into the assassination market "
            "instead. Her Book 5 reckoning by Valen (extends CC-109) resolves "
            "mechanically, not just symbolically: her 520-year-refined 0.8-second "
            "window is a cultivated ceiling, while Valen's Precision Variant biology "
            "(CC-035) processes combat geometry fast enough that he is already inside "
            "the window the instant she initiates it -- the tradition she corrupted "
            "is the one that stops her."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1853",
        "category": "World Mechanics",
        "statement": (
            "Extends MCD-091/092/CULT-044/070/075/080: the wet-work team's actual "
            "Fulfillment Ceremony tradecraft -- arriving roughly four minutes after "
            "the Ronin's extraction, they secure the scene, remove the Ronin's entry "
            "traces, plant physical evidence suggesting an internal conspiracy -- the "
            "false narrative that misdirects Ezio's investigation for the first third "
            "of Book 1 -- and administer a short-term-recall-suppressing chemical "
            "compound through the venue's ventilation system to blunt witness memory "
            "of the engagement window. At the Unchained Kingdom during the Ghost's "
            "Book 3 infiltration, the team never enters the Kingdom itself; instead "
            "they sanitize the Ghost's communication trail by dismantling the "
            "Lawless Reaches relay points the transmissions routed through -- which "
            "is why Ezio later traces the relay points and finds them clean."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

new_ids = [r["id"] for r in NEW_RULES]
assert len(new_ids) == 4
assert len(set(new_ids)) == len(new_ids)
collisions = existing_ids & set(new_ids)
assert not collisions, f"ID collision: {collisions}"

ledger["rules"].extend(NEW_RULES)

batch_note = (
    "Abad picked 'the Three Ronin hook' from the still-open items flagged after Batch "
    "307/308. Read the full source document (Beloved_and_Blade_Ronin_Victims.docx) in "
    "full for the first time. Part I (Nelle Adessi, Tomas Grieve) turned out already "
    "well-covered at CC-123/CC-124 (Batch 55). Part II (the Three Ronin) and the SBD "
    "Wet-Work Team section held real, unmined mechanism material behind the reckonings "
    "MCD-092 only ever named in one line each: the Silence's Praetorian expulsion "
    "tying to the already-locked Dhampir Black (POL-102); the Ghost's true reckoning "
    "mechanism (Anansi/Valeria Korth's Thread-Perception detecting an absence of "
    "threads rather than the Ghost directly, captured not killed); the Blade's "
    "Celestial Zenith origin (the same tradition as Orlok) and the exact mechanical "
    "reason Valen's reckoning defeats her 0.8-second window; and the wet-work team's "
    "actual Summit tradecraft (the false-narrative misdirection of Ezio's Book 1 "
    "investigation, the memory-suppressing ventilation compound). Zero new proper "
    "nouns -- pure extension of already-locked figures. Abad's approval: \"lock it.\""
)
ledger["batches_completed"].append(
    {
        "batch": 310,
        "date": str(date.today()),
        "source": "Beloved_and_Blade_Ronin_Victims.docx (Google Drive)",
        "rule_count": len(NEW_RULES),
        "note": batch_note,
    }
)

ledger["ledger_version"] = f"{round(float(ledger['ledger_version']) + 0.1, 1):.1f}"
ledger["last_updated"] = str(date.today())

with open(LEDGER_PATH, "w", encoding="utf-8") as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
      f"Batches: {len(ledger['batches_completed'])}.")
