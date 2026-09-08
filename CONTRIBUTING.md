# Contributing to Lokiravia

Lokiravia is the game creation product by Lokvetia. Shared orchestration belongs
in [Lokvetia Core](https://github.com/HappyMiha/Lokvetia-Core); product integration
and the creator experience belong here. See the [compatibility guide](README.md#compatibility)
before changing package names, data paths or stable task IDs.

Read [AGENTS.md](AGENTS.md) and the [three-computer workflow](docs/team-workflow.md).

The worker names are HappyDucky02, HappySnowman, and HappyHahahaker. Configure each clone with the correct worker, inspect the shared register, and claim a ready task before starting. Use the branch created for your claim (`agent/<worker>/<TASK-ID>-<8hex>` with registry v2; existing `team/<worker>/...` branches remain valid) and declare the files you plan to change.

Commit a focused change, fetch and incorporate current `main`, and run `python scripts/team_checks.py`. The pre-push hook checks the current claim, dependencies, scope, branch history, and exact-commit evidence. Do not force-push or bypass hooks.

Use one PR per task. Include actual tests and known failures. HappyDucky02 coordinates merges initially; another worker reviews the result. A dependency is ready only after its work is merged and recorded, not merely pushed. Product acceptance still follows the source backlog.

Lokiravia is in early development, with a working local idea editor and planning components. Coordination scripts and checks are development tools; they do not implement the planned game generation, hosting or payments. Public repository visibility does not choose a Lokiravia software license; those terms remain an owner decision.
