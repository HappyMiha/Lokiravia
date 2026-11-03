# Machine state

<!-- translation-metadata:start -->
<details>
<summary>Translation source and currency</summary>

Translation source: [machine-state.uk.md](machine-state.uk.md). Source SHA-256 (UTF-8/LF): `5c77677db00418f1187de42c1c6361531be5ad4e23e9df0adafd9737a3e63e4e`.

</details>
<!-- translation-metadata:end -->

[Українська](machine-state.uk.md).

Shared handoff record for the owner's machines. The rules are in
[multi-machine-context.en.md](multi-machine-context.en.md).

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

### 2026-11-03 · `dev-1`

- Both documents were split into a `*.uk.md` / `*.en.md` pair and registered in
  [evolution/translations.json](evolution/translations.json). Ukrainian is the
  original; the English page carries the source hash.
- Same scope, same branch `claude/multi-machine-context`.
- Checked: `validate_translations.py`.
- Open: this handoff log is now bilingual, so every future entry needs both
  versions and a fresh hash, or the validator marks the translation stale.

### 2026-11-02 · `dev-1`

- Added [multi-machine-context.en.md](multi-machine-context.en.md) and this state
  file; added the multi-machine bullet to [AGENTS.md](../AGENTS.md).
- Documentation only. No code, contract, manifest or backlog change.
- Written on `facd5e6` and re-applied on upstream `5364089`. `main` is protected
  and rejects merge commits and direct pushes, so this arrives on branch
  `claude/multi-machine-context`; start from that branch until it merges.
- Checks: `validate_translations.py` PASS (30 translations),
  `validate_backlog.py` PASS (74 items, 15 evidence entries). The test suite is
  not usable on this machine: `python -m unittest discover -s tests` reports 22
  errors from a missing `agent_factory` module and one `test_branding` failure,
  none of them reachable from a documentation change.
- Open: `world-1` has no checkout, role or platform recorded, and the open-world
  server architecture is undecided.
