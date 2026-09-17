#!/usr/bin/env python3
"""Batch 294: The 1804 tragedy, the 1804 faction, Daba, and his mutual
mentorship with Kanja -- new mainline pre-Rebellion foundation."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-17, no source document. New mainline "
    "pre-Rebellion material establishing the 1804 tragedy, the 1804 faction, Daba, "
    "and his mutual mentorship with Kanja, per Abad's direction."
)

BATCH_NOTE = (
    "New faction and S-tier character laying pre-Rebellion foundation for a future "
    "Book 1 payoff. Abad's original framing (lightly garbled by dictation) resolved "
    "via three clarifying questions before drafting: 'conjure' and 'Contra' both "
    "confirmed to mean Kanja; placement confirmed as new mainline pre-Rebellion/"
    "Rebellion-era material, not a separate homage World. Two further judgment calls "
    "(the perpetrator as Sovereign Trust suppression forces, and Daba as a survivor "
    "of 1804 himself) were proposed and confirmed before the full rule text was "
    "drafted and presented. MCD-1566 locks the tragedy itself: a Sovereign Trust "
    "punitive 'correction' against a settlement called the Rookery, 1,804 dead, "
    "overwhelmingly children plus the young caregivers who died trying to save them, "
    "roughly eight years before Kanja's Rebellion formally begins at MCD-231. "
    "MCD-1567 locks the 1804 faction Daba builds afterward -- the smallest standing "
    "force of any resistance faction in the ledger, deliberately so, doctrine over "
    "mass, disproportionately lethal and versatile for its size. CC-135 locks Daba "
    "himself, S-tier through guerrilla mastery and tactical discipline rather than "
    "density, following the same non-variant-biology precedent as Matar (CC-067). "
    "MCD-1568 locks the mutual mentorship with Kanja during his otherwise-unrecorded "
    "formative years -- Daba teaches guerrilla warfare, Kanja teaches forging (his "
    "own Rexmar tradition, MCD-294-312), and Daba becomes Kanja's conscious "
    "apprentice -- establishing the shared root of Daba's guerrilla doctrine and "
    "Kanja's own already-locked terrain-physics tactics at the Dredge-Line Ambush "
    "and Iron Shallows (MCD-231/233). MCD-1569 locks the dormant-infrastructure hook: "
    "1804 grows into a genuinely dispersed network with no single point of failure, "
    "built before Daba can see what it will need to answer, running semi-dormant "
    "through Kanja's Rebellion and Long Mask era and activating in earnest in Book 1 "
    "-- the specific trigger deliberately left unspecified, matching the project's "
    "established practice for future-book payoffs (Haku's fate, the Drowning Vault's "
    "120, MCD-314/183). Zero new proper-noun collisions (Daba, 1804, the Rookery all "
    "checked clean against the full live ledger before drafting). Abad's approval: "
    "\"lock it.\""
)

NEW_RULES = [
    {
        "id": "MCD-1566",
        "category": "World Mechanics",
        "statement": (
            "Roughly eight years before Kanja's Rebellion formally begins (age 18, "
            "MCD-231), Sovereign Trust suppression forces carried out a punitive "
            "'correction' against the Rookery, a dense tenement settlement on the "
            "Trust Domain's own periphery suspected of sheltering resistance activity "
            "-- setting the housing block ablaze and collapsing its stairwells to cut "
            "off escape. 1,804 died: the overwhelming majority children, plus the "
            "young men and women who served as the settlement's caregivers and died "
            "trying to get them out or fight back against the column. The Trust's "
            "official record lists it as a fire of undetermined origin; survivors and "
            "the wider region refuse that framing, known only by its death toll "
            "rather than a date or place-name that could be softened. The event "
            "predates and directly feeds into what becomes Kanja's Rebellion, though "
            "it is not asserted as its sole cause."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1567",
        "category": "World Mechanics",
        "statement": (
            "The survivors' network Daba built in the tragedy's aftermath took the "
            "number itself as its name, refusing to let the dead be reduced to a "
            "statistic others could stop counting. It fields the smallest standing "
            "force of any resistance faction referenced in the ledger, deliberately "
            "so -- doctrine over mass, dispersed cells cross-trained across "
            "reconnaissance, demolitions, medical support, and combat rather than a "
            "visible concentration of force, built on the lesson 1804 itself taught: "
            "anything large enough to be seen is large enough to be burned. No single "
            "loss collapses a function the group depends on. Disproportionately "
            "lethal and versatile relative to its size -- among the most effective "
            "non-Trinity forces in the ledger despite fielding a fraction of the "
            "personnel of comparable factions."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1568",
        "category": "World Mechanics",
        "statement": (
            "Some years before Kanja's Rebellion formally begins, Kanja and Daba "
            "enter a deliberate, mutual mentorship during Kanja's otherwise-"
            "unrecorded formative years: Daba teaches Kanja guerrilla warfare -- "
            "small-unit doctrine, terrain-as-weapon thinking, the discipline of "
            "making concentrated force irrelevant -- while Kanja teaches Daba "
            "forging, drawing on his own Rexmar tradition (MCD-294 through MCD-312). "
            "Daba becomes Kanja's conscious apprentice in forging: aware of exactly "
            "what he is learning and why, not a naive student absorbing technique "
            "without context. The exchange is the shared root of two doctrines that "
            "later look identical in practice: Daba's own guerrilla tactics and "
            "Kanja's already-locked terrain-physics doctrine at the Dredge-Line "
            "Ambush and Iron Shallows (MCD-231/233) -- density is not power if the "
            "terrain neutralizes it, a lesson 1804 taught Daba first and Daba taught "
            "Kanja second."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1569",
        "category": "World Mechanics",
        "statement": (
            "In the years following his mentorship of Kanja, Daba spends his own "
            "unrecorded years building 1804 into something considerably more durable "
            "than a single guerrilla cell -- a genuinely dispersed, versatile network "
            "with no single point of failure, deliberately built before he can see "
            "the full shape of what it will eventually need to answer. He does not "
            "know, building it, which enemies will surface; he understands only that "
            "keeping something resilient alive is worth the cost of maintaining it "
            "against a threat he cannot yet name. The network runs semi-dormant "
            "through the whole of Kanja's own Rebellion and Long Mask era, never "
            "folded into the Lords of Cian's own crew structure or publicly credited "
            "alongside it. It activates in earnest in Book 1, when an as-yet-"
            "undrafted triggering event forces the issue -- the specific trigger "
            "deliberately left unspecified, matching the project's established "
            "practice of leaving future-book payoffs open (Haku's fate, the Drowning "
            "Vault's 120, MCD-314/183) until that book is actually being drafted."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-135",
        "category": "Character",
        "statement": (
            "Daba, S-tier -- his rating earned through guerrilla mastery and "
            "tactical discipline rather than density, following the same non-"
            "variant-biology precedent already established for Matar (CC-067). A "
            "survivor of the tragedy that would come to be called 1804 (MCD-1566) -- "
            "one of the young caregivers present that day who lived -- he founded "
            "the guerrilla network that took the same number as its name (MCD-1567) "
            "in its aftermath and leads it as its smallest, most versatile, and "
            "among its most lethal force. His own guerrilla doctrine and Kanja's "
            "later Rebellion-era terrain-physics tactics share a common root, per "
            "the mutual mentorship locked at MCD-1568."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 5, f"expected 5 new rules, got {len(NEW_RULES)}"
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 294,
            "date": str(date.today()),
            "source": SOURCE,
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
