# Machine state

Shared handoff record for the owner's machines. The rules are in
[multi-machine-context.md](multi-machine-context.md).

This file records what was done, on which machine, and up to which commit. It
does not claim a running service, a deployed environment or an accepted feature.

## Machines

Add a row when a machine first takes a role. Keep platform entries coarse: no
absolute paths, account names or host addresses.

| Machine | Role | Platform | Last recorded sync | What runs there |
| --- | --- | --- | --- | --- |
| `dev-1` | `dev` | Windows 10 | 2026-11-02 · `5364089` | documentation validators; Lokvetia Core not installed |
| `world-1` | `world` | not recorded | not recorded | nothing recorded |

`world-1` is a reserved label. No open-world server exists in this repository, so
nothing has been built or run under that role.

## Handoff log

Newest first. One entry per handoff: what changed, the commit the next machine
should start from, what was checked, and what is still open.

### 2026-11-02 · `dev-1`

- Added [multi-machine-context.md](multi-machine-context.md) and this state file;
  added the multi-machine bullet to [AGENTS.md](../AGENTS.md).
- Documentation only. No code, contract, manifest or backlog change.
- Written on `facd5e6` and re-applied on upstream `5364089`. `main` is protected
  and rejects merge commits and direct pushes, so this arrives on branch
  `claude/multi-machine-context`; start from that branch until it merges.
- Checks on the merged tree: `validate_translations.py` PASS (30 translations),
  `validate_backlog.py` PASS (74 items, 15 evidence entries). The test suite is
  not usable on this machine: `python -m unittest discover -s tests` reports 22
  errors from a missing `agent_factory` module and one `test_branding` failure,
  none of them reachable from a documentation change.
- Open: `world-1` has no checkout, role or platform recorded, and the open-world
  server architecture is undecided. Top-level documentation now pairs `*.uk.md`
  with `*.en.md` and registers the pair in
  [evolution/translations.json](evolution/translations.json); these two files are
  English-only and unregistered.
