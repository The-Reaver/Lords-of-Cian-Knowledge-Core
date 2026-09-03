# A Claude Code Remote (cloud) session structurally has no device-bridge tools -- confirmed, not assumed

- id: 2026-09-03-cloud-sessions-lack-device-bridge
- type: finding
- status: candidate
- class: confirmed
- source: Lords-of-Cian-Knowledge-Core session, 2026-09-03, "Batch 49 and the Brain Trust gap"
- confidence: high -- verified directly via ToolSearch in the session itself, not inferred
- verified: 2026-09-03
- tags: fleet, infrastructure, device-bridge, brain-trust

## Body
A Claude Code Remote (cloud/scheduled) session has no `mcp__remote-devices__*` tools at all. This
was first found by the 2026-08-03 Anansi close-out session (`docs/lords-of-cian/anansi-closeout-2026-08-03.md`
in the Lords-of-Cian-Knowledge-Core repo) and was independently reconfirmed on 2026-09-03 by a
different cloud session via `ToolSearch` (query "remote-devices device bridge" returned nothing
relevant). It is a structural property of the session type, not a config gap, a permissions
issue, or something that can be fixed by asking the tool to appear. Any workflow step that
requires reading from or writing to the operator's device (`C:\Users\abadm\stag`) -- including
real Brain Trust ratification via `structure-notes/brain-trust-on-demand-protocol.md`, and an
ADR-0005-compliant raw archive write via `scripts/knowledge_home/archive_writer.py` -- cannot run
in a cloud session, full stop. It requires an interactive session with the device bridge live:
the Cowork desktop app open, or a local Claude Code session on the same machine, with
`desktop-4uc2ltp` connected. A cloud session should confirm this via ToolSearch before assuming
either way, per the 2026-08-03 doc's own instruction, rather than guessing.

## Links
- extends, (none in this repo's `notes/` yet -- `notes/` was empty at time of writing, could not
  dedup against the real device Core from this session), first documented in
  docs/lords-of-cian/anansi-closeout-2026-08-03.md
