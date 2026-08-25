# My Rival's Distance: The Lords of Cian — Canon Work

By Abad Morel. This file tells a Claude Code session how to continue the canon-locking work exactly the way it has run so far in Cowork, without re-explaining the process each time.

## What this is

`canon-ledger.json` in this folder is the authoritative canon-rules ledger for the Lords of Cian world. It is a flat list of atomic, source-cited rules (`rules`), a log of every extraction/invention pass (`batches_completed`), and a small set of still-open questions (`open_decisions`). As of 2026-08-25 it sits at `ledger_version` 2.7, 537 rules, 24 batches, zero duplicate rule IDs.

The ledger is also mirrored as a doc in the "My Rival's Distance: The Lords Of Cian" Claude Project (`claude/canon-ledger.json`), so it stays visible across claude.ai, Cowork, and Claude Code. Whichever session edits the local file should sync the change back to that project doc when possible; if a session has no way to reach the Project, edit the local file and note in the handoff that a sync is still owed.

## The non-negotiable rule: draft, then explicit approval, then lock

Nothing gets merged into `canon-ledger.json` as `"status": "locked"` until Abad approves it in his own words, in that conversation. The workflow, every batch, without exception:

1. Before drafting anything, grep the live ledger for every proper noun the new material would introduce (character names, house names, place names, factions, currencies) to catch collisions with something already locked. This has caught real collisions more than once (a name that already belonged to a different character, a location name that collided with the protagonist crew's own name).
2. Draft the full rule text and paste it into the conversation, not a summary of it. Cross-check it against everything already locked and call out what it's consistent with or extends.
3. Wait for Abad's explicit approval in his own words. Quote that approval verbatim into the batch's `note` field when it locks; do not paraphrase it.
4. Only then write a merge script, run it, and lock the rules.

## Rule-ID prefixes in use

`MCD`, `VB`, `ARS`, `SBD`, `HLD`, `MAW`, `GEO`, `WC`, `CC`, `POL`, `COS`, `CHAR`, `CULT`, `WGD`, `ASH`. A new institution or system gets its own new prefix rather than overloading an existing one (`ASH-` was claimed this way for the Ashkeel institution). Check the ledger for the next unused ID in a prefix before drafting; never guess.

## Merge script pattern

Every batch gets its own script (`merge_batchN_description.py`, N is the next sequential batch number, currently 25): load the ledger, define a `SOURCE` string describing where the material came from (a real source document, or `"Original invention, chat-drafted <date>, no source document"` for from-scratch material), append each new rule as `{"id":, "category":, "statement":, "status": "locked", "source":}`, assert no ID collisions, append a `batches_completed` entry with the batch number, source doc, rule count, and a `note` quoting Abad's approval verbatim, bump `ledger_version` and `last_updated`, write the file back. Then verify with a one-liner that there are zero duplicate IDs and print the new total.

## Standing conventions

- **No AI attribution.** Every document and every field in the ledger reads as authored by Abad. No "Claude" mentions, no framing that implies an assistant wrote something. This was corrected retroactively across 12 fields on 2026-08-23 and applies to everything written since.
- **Child-safety hard stop.** If a source document combines underage characters with sexualized content, stop, quote the exact problem text to Abad, and do not process, catalog, or integrate it as written, regardless of fictional framing, until he corrects it.
- **This world's baseline lifespans are long** (hundreds to tens of thousands of years), which is why age floors in this world read very differently than they would in a realistic-length-lifespan setting; don't default to real-world age assumptions when a rule involves recruitment ages, apprenticeships, or generational spans.
- **"Cian" reuse outside Kanja's crew gets renamed, full stop.** Superseded 2026-08-25 from an earlier "decide per-instance" policy. Several source documents (e.g. "Guild of the Extraordinary") reuse "Cian," the world's own name, as an in-world proper-noun component (a scent name, a jurisdiction, a guild, a barracks tier). Abad's standing rule now: rename any such instance unless it's actually part of Kanja's crew/story material. Don't ask per-instance anymore; just apply it and note what you renamed.

## Currently queued, not yet started

- The standalone Domus Inviolate Dossier deep-read.
- The remaining Ashkeel batches: ~~the Seven High Arts as a formal system~~ **done, Batch 22, 2026-08-25 (`ASH-023` through `ASH-030`)**; ~~the collar/legal hierarchy and the Basalt Codex~~ **done, Batch 23, 2026-08-25 (`ASH-031` through `ASH-042`)**; ~~internal geography and the merchant guilds~~ **done, Batch 24, 2026-08-25 (`ASH-043` through `ASH-049`)**; still queued: named characters.
  - Comes from the same source document as Batches 19, 22, 23, and 24: "Guild of the Extraordinary" (Google Drive fileId `1cGEqnWXfUZOGSVksys32TSQninqSI_fWZ0LC7fSUGXM`). Quirks confirmed there that will resurface in this last batch:
    - **House-name translation is required, not optional.** The raw document still uses the pre-rename house names (Solaas, Kaelen, Nyxos, Thorne, Val-Cian). `ASH-014`/`ASH-015`/`ASH-016` already locked these as Corvessa, Kragmoor, Vhaerlow, Kestrion, and Aurelock respectively (Vane and Moros unchanged) under Abad's full-renaming-autonomy grant. Translate every occurrence before drafting; do not reintroduce the document's literal names.
    - **Enforcer/Iron-Collar recruitment age is 30, per the already-locked `ASH-016` — settled, not still open.** The document's own stated "16 and 22" combined an underage floor with mandatory sexualized content in the Phase I admission trial ("The Labyrinth of Desire") and tripped the child-safety hard stop when re-encountered fresh in Batch 22's research pass (`ASH-016` had already corrected this back in Batch 19, but that context wasn't in front of the session doing the Batch 22/23 read). Abad confirmed 2026-08-25: "30 stands." Batch 23 (`ASH-036`) drafted the Three Weeding Trials against this age, resolving the flag. A future session should not need to re-litigate this, but if the raw document is ever re-read cold, the same passage will look alarming again until cross-checked against `ASH-016`.
    - The document also reuses "Cian" (the world's own name) as an in-world proper-noun component in several places (Redoubts of Cian -> now the Iron Redoubts, Apothecaries of Cian -> now the Apothecaries of the Deep, the Vapor of Cian -> now the Obsidian Vapor, the Sanctuary of Cian -> now the Sanctuary of Ashkeel). See the standing convention above: rename any further instance without asking, unless it's genuinely part of Kanja's crew material.
- The 173-file Character Codex zip (curatorial extraction, Talisman of Mao lore flagged as priority).
- The World Adaptation Blueprint.
- C-001 through C-023 Codex-text corrections.
- Tier 4 Preparation Checklist cross-check.
- Three long-open items: `OPEN-005` (locating "Session Lock 2," probably never existed as a standalone document, see the ledger's own note), `OPEN-007` (interstitial world-phenomena chapters), `OPEN-008` (House Marlunar/Marvault/Marossen heads).

None of this is urgent or sequenced; work whichever thread Abad points to next.

## Separate, unrelated thread: the interactive archive app

The Lords of Cian interactive archive (a Lovable-built app, repo `The-Reaver/My-Rivals-Distance-Archive`) is a different project with its own reconciled game plan (`lords-of-cian-archive-game-plan.md`, also mirrored in the Claude Project). It is not blocked on canon work and canon work is not blocked on it. Two flags carried over from that plan, unresolved as of 2026-08-23: the connected GitHub repo has zero commits, and Row Level Security / email confirmation status on the deployed app may be leaving reader data exposed on a live public URL right now.
