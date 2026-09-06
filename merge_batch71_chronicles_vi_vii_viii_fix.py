#!/usr/bin/env python3
"""Batch 71: completes the Chronicles I-VIII rewrite (roadmap Step 3).

No new canon facts -- this batch corrects manuscript prose to match
facts already locked in prior batches. Chronicle VI and Chronicle VIII
each get two fixes; Chronicle VII needed none once GEO-006 (Batch 70)
placed Ash Harbor on the Atlas, since the manuscript's own claim
("Jicome's southern coast") was already correct.

Chronicle VI ("The Sewer War of Killane"):
- The closing summary's "Blue-Collar Titan"/4,000-worker misattribution
  (which forward-referenced the Furnace District Strike, MCD-244, age
  21 -- a battle that hadn't happened yet at this chapter's age-20
  setting) replaced with a correct callback to the Scrip-Forge Raid,
  age 18, already discussed earlier in the same chapter.
- "liberated twelve thousand human beings from a quarry" corrected to
  "from Maw-9," matching arena/Maw terminology (distinct from Chronicle
  V's fine historical "quarry" usages, describing the site's origin).

Chronicle VIII ("The Ash-Wharf Massacre"):
- The Receipt's capture corrected from "a patrol intercept south of
  the Jicome Strait" to the eleven-week Reef-Chain Blockade / Kothrane
  Narrows, matching MCD-242.
- The 1.2-million-worker/40%/twelve-year charcoal-rubbing evidence
  corrected from "Killane" to "the Scrip-Forge Raid," matching
  MCD-286 (Killane's real evidence method, MCD-234, is unrelated).

Corrected texts saved to docs/lords-of-cian/chronicles/
chronicle-vi-the-sewer-war-of-killane.md and
chronicle-viii-the-ash-wharf-massacre.md. This closes roadmap Step 3:
all 8 manuscript Chronicles are now confirmed clean or corrected."""
import json

LEDGER_PATH = "canon-ledger.json"

BATCH_NOTE = 'Abad: "lock it"'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    ledger["batches_completed"].append(
        {
            "batch": 71,
            "source_doc": (
                "Chronicles I-VIII rewrite (roadmap Step 3), final pass: "
                "corrects Chronicle VI's Blue-Collar Titan misattribution "
                "and 'quarry'-as-Maw-9 terminology, and Chronicle VIII's "
                "Receipt-capture account and Killane evidence "
                "mislabeling, against locked canon (MCD-234, MCD-242, "
                "MCD-244, MCD-286). Chronicle VII needed no prose "
                "changes once GEO-006 (Batch 70) placed Ash Harbor on "
                "the Atlas. No new canon facts; corrected texts saved "
                "to docs/lords-of-cian/chronicles/. Closes roadmap "
                "Step 3 -- all 8 manuscript Chronicles now clean or "
                "corrected."
            ),
            "source_id": None,
            "rule_count": 0,
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "7.4"
    ledger["last_updated"] = "2026-09-06"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
