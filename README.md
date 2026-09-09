# Lokiravia

![Lokiravia by Lokvetia](src/agentfactory_cloud/static/brand-wordmark.svg)

**Your idea. Your game world.**

**Концепція й архітектура:** [Живий світ, самовдосконалення Core, спільний портфель із 65 задач і план доказів](docs/evolution/README.md) — проєктна документація, не заява про готову реалізацію.

A game creation platform by [Lokvetia](https://lokvetia.com), powered by
[Lokvetia Core](https://github.com/HappyMiha/Lokvetia-Core).

[Product domain](https://lokiravia.com) · [Start locally](docs/game-brief-intake.md) ·
[Product plan](docs/product-description.md) · [Roadmap](docs/roadmap.md)

**Деплой і релізи:** [Deployment dashboard (в Lokvetia Core)](https://github.com/HappyMiha/Lokvetia-Core/blob/main/docs/deploy-dashboard.html) · [Автодеплой і rollback для Lokiravia](docs/autodeploy.md)

Formerly **AgentFactory Cloud**. Lokiravia is the creator product; Lokvetia is
the family brand, and Lokvetia Core is the independent orchestration engine.

**Early development.** A local game-idea editor is available. Hosted game creation,
engine execution and publishing are still planned; there is no verified deployed
Lokiravia game pipeline. The product domain is owned; this repository does not
establish that a hosted service is live there.

**Try the local editor:** [setup, features and evaluation](docs/game-brief-intake.md).
Save your original idea, edit a short game brief and revisit earlier versions.
Optional local AI helps organize your original sentences; review its choices.
Then choose **Plan the first playable version** to review a small scope, its
future roadmap, concrete tasks and a clearly labelled local AI estimate.
See [first-playable planning](docs/first-playable-planning.md) for its limits.

**Three-computer development:** [team workflow](docs/team-workflow.md) · [live shared task register](https://github.com/HappyMiha/Lokvetia-Core/blob/team-state/team-state.json). Each worker claims a task and uses an owned branch with checks before push and a pull request into `main`.

## The product direction

A creator will describe a game, agree on a small first version, let an AI team build and test it, play the result and ask for changes. The creator should receive the source project and supported builds to use outside Lokiravia.

**The first proof:** Godot 2D + GDScript → browser Play → Windows/source download → feedback → verified v2 → rollback.

**The Unreal and Gameplay AI direction:** an AI team opens Unreal, writes code, builds levels, tests and packages a game whose NPCs can act and remember during play.

- **Core:** the AI team, tasks, models, budget and recovery.
- **Unreal adapter:** editor and build operations through a qualified existing MCP backend.
- **Gameplay AI:** NPC memory, allowed actions and world behavior inside the game.

The first Unreal proof is **one level, three NPCs, one objective → Windows package → play without Unreal Editor → save/load → AI outage → a revised package after creator feedback**. Read the [architecture, delivery sequence and acceptance plan](docs/unreal-gameplay-plan.md). This expansion has its own qualification and keeps the first Godot milestone intact.

**The wider product loop:** Play → Remix → Create → Publish → Play.

## Two projects

- **[Lokvetia Core](https://github.com/HappyMiha/Lokvetia-Core):** the existing Apache-2.0, provider-neutral orchestration engine. It remains usable without Lokiravia.
- **[Lokiravia](https://github.com/HappyMiha/Lokiravia):** the commercial creator experience, hosted execution, game delivery, publishing and later commerce.

In architecture and coordination documents, **Core** and **Cloud** remain short
names for these responsibilities. They are not additional product brands.

Games, Community and Marketplace are modules within Cloud. They are not additional repositories. Core owns shared engine-neutral contracts and optional open-source game, engine and target packs outside its neutral runtime. Cloud's Games module uses those packs for the creator experience, project settings, play feedback and release policies; it does not build a second set of adapters.

The intended audience includes creators aged 12+ and adults. Actual access, public sharing and commerce depend on a qualified age/guardian, privacy and provider-permission model. The first internal pilot can use adults until those requirements are met.

## Read the plan

1. [Product description](docs/product-description.md) — users, journeys, MVP, architecture, Remix, safety and economics.
2. [Roadmap](docs/roadmap.md) — M0–M6 with evidence-based release gates.
3. [Backlog](docs/backlog.md) — readable tasks and acceptance criteria.
4. [Machine-readable backlog](examples/agentfactory-cloud-backlog.json) — seven epics and 67 stable AF-CLD tasks, schema v2.

The plan is based on the owner's supplied Cloud planning package. It extends the 42 AF-GC tasks in Core and preserves their upstream role. The live shared task register records current engineering progress; backlog descriptions preserve the original acceptance requirements. A task entry, valid JSON file or merged component is not evidence of a playable game.

The [Core/Cloud responsibility contract](docs/core-cloud-boundary.md) adds the AF-CLD-001 ownership map, rights records and design walkthroughs. It remains subject to integration and owner review.

## Scope and evidence

Start with a small reliable Godot game. Add hosted multi-tenancy next, then public publishing and Remix, then qualified commerce. Other engines, stores, factory templates and hybrid profiles require separate evidence before they are called supported.

Lokiravia is a separate public repository for a planned commercial product, made public at the owner's request. Public visibility does not select a software license. Lokiravia license terms remain an owner decision; Lokvetia Core keeps Apache-2.0.

## Compatibility

The public brand changes without relocating existing workspaces or changing
the execution contract:

| Surface | Preferred name | Compatibility retained |
| --- | --- | --- |
| Product | Lokiravia, by Lokvetia | Formerly AgentFactory Cloud |
| Repository | `HappyMiha/Lokiravia` | Existing history, issues and pull requests |
| Local command | `lokiravia --data <private-directory>` | `agentfactory-brief` accepts the same options |
| Python distribution / imports | `agentfactory-cloud` / `agentfactory_cloud` | Existing installations and integrations continue to resolve |
| Saved briefs and configuration | Existing `--data` directory and `AGENT_FACTORY_*` variables | No automatic path or database migration |
| Coordination and backlog | Existing `core:` / `cloud:` and `AF-*` task IDs | Registry ownership, dependencies and historical evidence remain intact |

The Core dependency remains pinned to the accepted commit through its existing
Git URL in `pyproject.toml`. A visual rebrand does not upgrade the engine.
Canonical repository links use the new names; the repository rename must be
completed when this change is released. Source archive names and historical
evidence links retain their original spelling.

See the [brand migration guide](docs/brand/migration.md) for existing checkouts
and the [visual identity](docs/brand/visual-identity.md) for artwork and usage.
