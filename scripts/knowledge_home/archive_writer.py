"""archive_writer.py: the append-only write path for research/knowledge-home/raw/.

Per ADR-0005 (docs/adr/0005-two-store-memory-archive-and-core.md): the archive is one
JSONL file per session, one JSON object per turn, written by append only. Nothing in
this module ever opens an archive file in "w" (truncate) mode, and no function here
deletes or rewrites an existing line. That is the whole safety property this file
exists to hold.

Turn numbers referenced by a note's `provenance.turns` are 1-indexed line numbers in
the JSONL file (line 1 is the first turn appended), matching how a human or a diff
tool would describe "line 188 of this file."
"""
import json
import os


def append_turn(archive_path, ts, role, text, tool_calls=None):
    """Append one turn to archive_path. Creates the file and parent dirs if missing.

    Returns the 1-indexed line number the turn was written to, so callers can build
    a note's provenance.turns range from the return values of consecutive calls.

    Never opens archive_path in "w" mode. Always "a" (append), which POSIX and
    Windows both guarantee only ever grows a file, never truncates or rewrites
    existing bytes.
    """
    if not archive_path:
        raise ValueError("archive_path is required")
    parent = os.path.dirname(archive_path)
    if parent and not os.path.isdir(parent):
        os.makedirs(parent, exist_ok=True)

    record = {"ts": ts, "role": role, "text": text, "tool_calls": tool_calls or []}
    line = json.dumps(record, ensure_ascii=False)

    # Line count BEFORE this write, to compute the 1-indexed line number of this turn.
    prior_lines = 0
    if os.path.exists(archive_path):
        with open(archive_path, "r", encoding="utf-8") as f:
            for _ in f:
                prior_lines += 1

    with open(archive_path, "a", encoding="utf-8") as f:
        f.write(line + "\n")

    return prior_lines + 1


def read_turns(archive_path):
    """Return the archive's turns as a list of dicts, in file (1-indexed) order."""
    if not os.path.exists(archive_path):
        return []
    turns = []
    with open(archive_path, "r", encoding="utf-8") as f:
        for raw_line in f:
            raw_line = raw_line.rstrip("\n")
            if not raw_line:
                continue
            turns.append(json.loads(raw_line))
    return turns


def read_raw_lines(archive_path):
    """Return the archive's raw text lines (no JSON parsing), 1-indexed by position."""
    if not os.path.exists(archive_path):
        return []
    with open(archive_path, "r", encoding="utf-8") as f:
        return [ln.rstrip("\n") for ln in f if ln.strip()]


def verify_prefix_unchanged(old_lines, new_lines):
    """Pure function proving the append-only invariant.

    old_lines: the archive's raw lines as they existed at some earlier point
    (e.g. the last committed version, from `git show HEAD:path`).
    new_lines: the archive's raw lines now.

    Returns (ok: bool, first_diff_index: int or None). ok is True only if every
    line in old_lines is present, unchanged, at the same position, at the start
    of new_lines (new_lines may have additional lines appended after that prefix).
    A shorter new_lines than old_lines is always a violation (that means deletion).
    """
    if len(new_lines) < len(old_lines):
        return False, len(new_lines)
    for i, old_line in enumerate(old_lines):
        if new_lines[i] != old_line:
            return False, i
    return True, None
