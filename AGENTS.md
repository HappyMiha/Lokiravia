# Repository guidance

Lokiravia is the creator product. Keep reusable orchestration, agent execution,
and engine capabilities in Lokvetia Core; keep the creator experience and product
integration here. Read [CONTRIBUTING.md](CONTRIBUTING.md) before making changes.

- Follow the user's authorized scope. Preserve unrelated work and inspect the
  current diff before editing or committing.
- Use focused changes with stable backlog IDs and explicit integration evidence.
  Backlog labels, merged code, and product acceptance are separate facts.
- Preserve the existing package names, data paths, migrations, and supported Core
  compatibility contracts unless the task explicitly changes them.
- Keep product execution permissions, worker admission, budgets, cancellation,
  recovery, and acceptance gates intact. Repository contribution rules do not
  grant an agent permission to execute a product job.
- Run checks relevant to the change and report their actual scope and failures.
  Synthetic tests do not establish a real game build, playtest, or deployment.
- Keep credentials, private briefs, supplied books, extraction caches, and other
  private source material out of Git. Preserve the Ukrainian documentation and
  follow the documented bilingual publication policy.
- When work is split across machines, treat Git as the only durable shared
  context: follow [docs/multi-machine-context.uk.md](docs/multi-machine-context.uk.md)
  ([English](docs/multi-machine-context.en.md)) and record each handoff in
  [docs/machine-state.uk.md](docs/machine-state.uk.md)
  ([English](docs/machine-state.en.md)). Machine roles are an operating
  convention and change no contribution rule.
- Review the final diff before publishing. Do not overwrite unrelated history or
  force-push without explicit authorization.
