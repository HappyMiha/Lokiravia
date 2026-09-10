# Lokiravia: brand and compatibility

Effective 8 September 2026. **Lokiravia**, formerly AgentFactory Cloud, is the game creation product at [lokiravia.com](https://lokiravia.com). Use **Lokiravia — by Lokvetia** when introducing its relationship to the family brand. **Lokvetia Core** is the independent Apache-2.0 orchestration foundation at [lokvetia.com](https://lokvetia.com).

## Public identity

Use Lokiravia in the app, documentation, API identity and product descriptions. The preferred installed command is `lokiravia`; `agentfactory-brief` continues to run the same application. The repository's canonical name is `HappyMiha/Lokiravia`, with `HappyMiha/Lokvetia-Core` upstream. Both names are activated after compatible tooling has merged in both repositories.

## Existing installations keep their data

| Surface | Compatibility contract |
| --- | --- |
| CLI | `lokiravia` and `agentfactory-brief` share an entry point |
| Distribution/import | `agentfactory-cloud` and `agentfactory_cloud` remain stable |
| Core dependency | Existing `agent-factory-orchestrator` distribution and pinned commit remain stable |
| State/configuration | Existing database paths, environment variables, authentication, browser storage and credential identifiers remain unchanged |
| Planning/evidence | `cloud`, AF-CLD/AF-GC IDs, backlog filenames, contract schemas and historical source evidence remain unchanged |
| Old repository URLs | GitHub redirects preserve existing repository links after the rename |

These technical names preserve compatibility; they are not additional public products. Do not bulk-replace them in configuration, databases or provider settings. No content migration is required.

After the repository renames, review and incorporate current `main` while preserving local work before optionally changing the remote:

```sh
git remote set-url origin https://github.com/HappyMiha/Lokiravia.git
python -m pip install -e .
lokiravia --help
```

Keep the old repository names unused so GitHub redirects continue working. Preserve existing branch and pull request history when updating repository links. The Core dependency remains an installable, pinned compatibility reference.

## Product truth

Lokiravia remains in early development. The local idea editor and planning flows do not prove hosted game generation, engine execution, public publishing or commerce. The new domain and identity are not a production-launch claim. Public repository visibility does not select new license terms. DNS, website hosting and mail configuration remain separate operational work.

See the [visual identity](visual-identity.md) for artwork and usage.
