# The Kanja-version track had drifted into a reflective first-person literary voice, so the Onyx voice check became a gate step with a script

- id: 2026-10-05-b-onyx-voice-drift-audit-and-gated-check
- type: finding
- status: ratified
- ratification: 2026-10-05, same-session independent review, ratified
- class: confirmed
- source: Canon session 2026-09-20 to 2026-10-05 (raw archive research/knowledge-home/raw/2026-10-05-canon-session-batches-303-377.jsonl), Batches 354-357
- confidence: high -- audit results and the author's correction are recorded in CLAUDE.md
- verified: 2026-10-05
- tags: lords-of-cian, voice-bible, onyx, audit, gate
REVIEW: high-impact

## Body
When the author read the first three Long Mask Onyx drafts (Kanja Chronicles V-VII, then unlocked) he asked whether they matched the Voice Bible's Onyx cadence. They did not, and neither did locked Kanja I, III, and IV: the track had been written as a reflective first-person literary voice instead of the telegraphic, morally absolute blade the Voice Bible and Voice Progression Sheet require. Both governing documents were then mirrored in the repo at docs/lords-of-cian/voice/. The author's ruling on process: "this should have been part of the rules that's gated." The voice check is now a gate step in docs/lords-of-cian/character-profiles/_TEMPLATE.md, with scripts/onyx_voice_check.py as the Phase 4 tool.

A full read-only voice audit found the drift confined to the Kanja-version track plus four Alias Chronicle entries giving Onyx conversational lines (Iron Bastard MCD-715, MCD-720, MCD-721; borderline Trench Monarch MCD-1127), and flagged several Storm That Walks entries (MCD-562, 565, 568, 574, 577, 583) putting Onyx in combat with no stated age. Lesson: a voice standard that lives only in reference documents was not being applied; it had to become a gated checklist item.

## Links
- depends_on, 2026-10-05-b-onyx-voice-standard-vb-063.md, the standard the check enforces
- related, 2026-10-05-b-kanja-v-vii-locked-and-locked-material-corrected.md, the corrections the audit drove
