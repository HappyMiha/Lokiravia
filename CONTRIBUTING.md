# Contributing to Lokiravia

Lokiravia is the game creation product by Lokvetia. Shared orchestration belongs
in [Lokvetia Core](https://github.com/HappyMiha/Lokvetia-Core); product integration
and the creator experience belong here. See the [compatibility guide](README.md#compatibility)
before changing package names, data paths or stable task IDs.

Read [AGENTS.md](AGENTS.md). Start from the current repository state, keep changes
focused, and preserve unrelated work. Describe the intended outcome, relevant
backlog IDs, upstream dependencies, and evidence in the change or pull request.
Contribution does not require a machine identity, central task reservation, or
machine-specific branch name.

Review the diff and run the checks relevant to the final version. Planning changes
should run `python scripts/validate_backlog.py`. A task marked `status:accepted`
must record at least one `evidence` entry; the validator refuses a manifest that
claims acceptance with nothing recorded. Changes to the corresponding
contracts or capability map should also run:

```sh
python scripts/validate_domain_contracts.py
python scripts/validate_engine_target_pack.py
python scripts/validate_evidence_gates.py
python scripts/validate_upstream_map.py
```

For product changes, use a qualified environment with the pinned Core dependency
and run the relevant tests, or `python -m unittest discover -s tests -v` for the
full suite. Record executed, failed, and skipped checks honestly. Do not treat
static validation or synthetic fixtures as real engine, game, or deployment proof.

Use a focused pull request when review is needed. Review dependency changes and
compatibility before integration; do not overwrite unrelated history or force-push
without explicit authorization. Merged implementation and owner acceptance remain
separate: product acceptance follows the source backlog and exact-version evidence.

Lokiravia is in early development, with a working local idea editor and planning
components. Development checks do not implement planned game generation, hosting,
or payments. Public repository visibility does not choose a Lokiravia software
license; those terms remain an owner decision. Keep supplied books, private source
files, extraction caches, credentials, and personal data out of Git.
