#!/usr/bin/env python3
"""Batch 311: the SBD Director's true name (Ilona Corrance), the Scrip-Ledger
disciplinary tier system, the Hollowing extension of WC-007's 'the Hollowed,'
the Prince Taboo/Turncoat Assets doctrine specific to Ozmund, and the Resonance
Singularity theory behind the SBD's whole Clinical Tone doctrine -- mined from
the 'SEALBOUND Directorate Dossier Analysis' find surfaced during the SBD deep
dive and Drive search. Extends already-locked material throughout; zero new
proper nouns beyond the Director's own name.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = (
    "SEALBOUND Directorate Dossier Analysis (Google Drive) reimagined/refined "
    "against the live ledger; Director name original invention, chat-drafted "
    "2026-09-27."
)

with open(LEDGER_PATH, "r", encoding="utf-8") as f:
    ledger = json.load(f)

existing_ids = {r["id"] for r in ledger["rules"]}

NEW_RULES = [
    {
        "id": "SBD-046",
        "category": "sbd-institutional-structure",
        "statement": (
            "Executive Director 'A.M.' -- the initials by which nearly every SBD "
            "record refers to the office, including its own internal case files "
            "-- is Ilona Corrance, the SBD's apex authority. The initialism is "
            "institutional habit rather than concealment: SEALBLACK-tier "
            "correspondence has used it for generations, long before Corrance's "
            "own tenure, and lower-clearance personnel genuinely do not know the "
            "name behind it. Corrance holds A.M.'s already-locked standing "
            "doctrine on Conflict Flags (MCD-1727) and full-transparency-"
            "received-in-good-faith relationship with Shelton Dexton "
            "(SBD-041/CC-140) as personal positions, not office tradition -- the "
            "next Director inherits the initials, not necessarily the "
            "philosophy."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "SBD-047",
        "category": "sbd-administrative-doctrine",
        "statement": (
            "Extends SBD-040/WC-007/ARS-399: the SBD enforces internal "
            "compliance through a tiered Scrip-Ledger disciplinary system "
            "layered onto ordinary personnel debt (extends WC-007's Metabolic "
            "Tether mechanics from subjects to staff). Level 1, Clinical Tone "
            "Failure -- using mythic/heroic language about a subject in "
            "official contexts -- draws a Metabolic Scrip-Fine, a 15% debt "
            "increase enforced biologically rather than merely on paper. Level "
            "2, Repeated Subject Agency -- treating a subject's will or "
            "personhood as real in a way that could compromise operational "
            "distance -- draws a Cognitive Reset: administered amnestics "
            "erasing the preceding 24 hours, removing the 'Emotional Variance' "
            "leadership considers the actual risk. Level 3, Mythic "
            "Contamination -- sustained, willful departure from clinical "
            "doctrine -- draws reassignment to Expendable Asset status, pulling "
            "the offending agent out of personnel entirely and into the same "
            "experimental population used for Resonance Sequestration testing "
            "(extends MCD-1727's Conflict Map program with its actual human "
            "cost). The system is self-policing by design: agents fear their "
            "own Scrip-Ledger more reliably than they fear the subjects."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "SBD-048",
        "category": "sbd-administrative-doctrine",
        "statement": (
            "Extends WC-007/CC-088/MCD-258: reaching 'the Hollowed' (100% "
            "Scrip-debt ratio) is not merely an economic dead end. Once a "
            "person's debt ratio is confirmed at 100%, the SBD classifies them "
            "as Fully Hollowed and eligible for Biological Repurposing -- "
            "consciousness suppressed via sustained amnestic dosing, the body "
            "retained as passive processing infrastructure (containment-field "
            "maintenance, archive indexing, the kind of continuous "
            "low-cognition labor the Directorate doesn't want a will attached "
            "to). This is the fate CC-088's Cooper fears specifically from Onyx "
            "of Oblivion, and the reason Level 3 Mythic Contamination (SBD-047) "
            "is designed to walk an offending agent to 100% debt on an "
            "accelerated timeline rather than punish them any other way -- "
            "reassignment to Expendable Asset status is the waiting room, "
            "Hollowing is the actual sentence."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "SBD-049",
        "category": "sbd-administrative-doctrine",
        "statement": (
            "Extends CC-090/MCD-100: SBD doctrine forbids referring to Ozmund "
            "by any sovereignty-implying term -- 'Prince' chief among them -- "
            "on the theory that the term itself constitutes a legitimacy claim "
            "the Directorate has administratively redacted; violation is "
            "punishable by summary reassignment directly to Hollowing "
            "(SBD-048), skipping the ordinary tiers, since the Directorate "
            "treats this specific term as an active threat rather than a tone "
            "lapse. Separately, and consistent with his already-locked Code of "
            "Honor (CC-090), containment planning for Ozmund leans on Turncoat "
            "Assets -- compromised or bribed personnel used to manufacture the "
            "one kind of failure (systemic betrayal) his own doctrine leaves "
            "him structurally unable to anticipate -- rather than on direct "
            "force, which his density and restraint both defeat."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1854",
        "category": "World Mechanics",
        "statement": (
            "The SBD's entire Clinical Tone doctrine (SBD-047, and the "
            "Approved-Terminology/Mythic-Term translation habit visible across "
            "its casework) rests on a real, tested theory internally called the "
            "Resonance Singularity: sustained mythic or heroic framing of a "
            "subject measurably strengthens that subject's resonance "
            "signature, the same physical channel the Talisman of Mao responds "
            "to (MCD-142) and Blight Frequency technology is built to suppress "
            "(ARS-398). Clinical language isn't PR -- it's the SBD's attempt "
            "at a passive counter-resonance field, applied through its own "
            "personnel as unwitting instruments, run on the same inherited "
            "Legacy Lattice architecture (ARS-393) as everything else it "
            "doesn't know it's using. The theory is also, per MCD-1727's own "
            "standing admission, unconfirmed and possibly one more false "
            "assumption the Oracle Conflict Map hasn't yet flagged."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

new_ids = [r["id"] for r in NEW_RULES]
assert len(new_ids) == 5
assert len(set(new_ids)) == len(new_ids)
collisions = existing_ids & set(new_ids)
assert not collisions, f"ID collision: {collisions}"

ledger["rules"].extend(NEW_RULES)

batch_note = (
    "Closes out the 'SEALBOUND Directorate Dossier Analysis' find surfaced "
    "during the SBD Drive search: reimagined its Scrip-Ledger disciplinary "
    "apparatus, its 'the Hollowed' fate, its Prince Taboo/Turncoat Assets "
    "doctrine against Ozmund, and its Resonance Singularity theory into the "
    "live ledger's own register and continuity, rather than adopting its "
    "deity-homage/fantasy-flavored framing wholesale. Named the SBD's "
    "Executive Director for the first time -- 'A.M.' stands for Ilona "
    "Corrance, with the initialism itself locked as standing institutional "
    "habit rather than concealment, so every existing A.M. cross-reference in "
    "the ledger stays valid without needing a rewrite. Reconciled 'the "
    "Hollowed' against its own already-locked WC-007 definition (100% "
    "Scrip-debt ratio) rather than let the source document's competing "
    "definition collide with it -- Hollowing is now locked as what "
    "the SBD actually does to a person once they reach that already-locked "
    "state, not a separate mechanic. Abad's approval: 'Ilona Corrance ... "
    "approving all recommendations.'"
)
ledger["batches_completed"].append(
    {
        "batch": 311,
        "date": str(date.today()),
        "source": "SEALBOUND Directorate Dossier Analysis (Google Drive)",
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
