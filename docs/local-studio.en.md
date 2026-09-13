# Local AI studio

<!-- translation-metadata:start -->
<details>
<summary>Translation source and currency</summary>

Translation source: [local-studio.uk.md](local-studio.uk.md). Source SHA-256 (UTF-8/LF): `b3bd8aca7cf756feab9c7db5eaf2cd3bc6b33d9dbfd3712776efca0a824b38a7`.

</details>
<!-- translation-metadata:end -->

[Українська](local-studio.uk.md).

Lokiravia can hand a saved idea to local Core for planning without a second manual
mandate. This does not yet create a playable game automatically.

Install both projects with a compatible Core version on the same PC. Run
`python -m agent_factory.studio_local_worker --workspace WORKSPACE --actor operator --run-live`
on the PC with Ollama and a supported installed model. Then configure the Lokiravia process:

```powershell
$env:LOKIRAVIA_CORE_WORKSPACE = 'C:\Work\local-studio'
$env:LOKIRAVIA_CORE_URL = 'http://127.0.0.1:8765'
```

The server operator supplies this path; the browser cannot select it. Core's
database is `WORKSPACE/.agent-factory/state.db`. The URL must be a loopback origin
without credentials. Provider keys are never carried by the bridge or URL.

Saved ideas show **Start local studio planning**. The button uses the authenticated
owner and the current saved revision. Save outstanding edits first. Repeated
requests use the same revision key and mission. **Open studio progress** opens
the corresponding Core mission.

The bridge is disabled without configuration. An unqualified model cannot create
a mission. Other owners, stale revisions and posted actor overrides are refused.
This is a local integration, not a cloud-to-PC job dispatcher. Core's detailed
gap audit is at `docs/ai-studio-audit.en.md`.
