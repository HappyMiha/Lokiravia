# Multi-machine context

Owner operating note for work split across more than one computer. It describes
how shared context is carried between machines and how a handoff is recorded.

This is not a contribution rule. [CONTRIBUTING.md](../CONTRIBUTING.md) keeps
contribution free of machine identity, central task reservation and
machine-specific branch names, and that stays unchanged. Machine roles below are
an operating convenience for the owner, not a precondition for changing this
repository.

## Why Git carries the context

Assistant sessions do not share context across computers. A session can inherit
a conversation when it is created, and two sessions can exchange messages while
both are online, but neither survives a reboot, an offline machine or a closed
session. The repository does.

Treat Git as the only durable channel between machines. Treat live session
messaging as a convenience that may be unavailable, and never as the place where
a decision is recorded.

## Roles

A role says what a machine is used for. It does not say who may contribute, and
it grants no permission that the repository does not already grant.

- `dev` — development checkout. Edits, commits and pushes; runs the checks
  listed in [CONTRIBUTING.md](../CONTRIBUTING.md).
- `world` — world-server checkout. Pulls, builds and runs a server process for
  an open-world target. No such server exists in this repository; the role is
  reserved so that handoffs have a stable name before one does.

One machine may hold both roles. Record roles in
[machine-state.md](machine-state.md) rather than in branch names.

## What crosses machines

Carried in Git:

- decisions, scope and backlog changes ([docs/evolution](evolution/README.md),
  [docs/backlog.md](backlog.md));
- contracts and operating notes, including this file;
- [machine-state.md](machine-state.md): which machine did what, and up to which
  commit.

Never carried in Git, restating [AGENTS.md](../AGENTS.md) so that a handoff does
not quietly break it:

- credentials, tokens and provider keys;
- private briefs, supplied books, extraction caches and personal data;
- local absolute paths and account names;
- world saves, build output, engine caches and other generated artifacts.

A handoff that needs one of these is not a Git handoff. Move the file by another
route and record only that it was moved.

## Exchange rules

1. **Push before handing off.** Unpushed work does not exist for the other
   machine. A handoff names a pushed commit. `main` is protected: it rejects
   merge commits and direct pushes, so work reaches it through a pull request
   and a handoff before merge names the branch.
2. **Pull before acting on a handoff.** Start from the recorded commit, not from
   whatever the checkout happened to hold.
3. **Record the handoff** in [machine-state.md](machine-state.md) and commit that
   entry together with the work it describes.
4. **Name the commit, not the conversation.** A handoff that points at a chat is
   unusable from the other machine.
5. **One writer per file set at a time.** Two machines editing the same files
   produce conflicts that no handoff note resolves.
6. **Report what was actually run, and where.** State the machine, the commit and
   the real result. A check that passed on `dev` is not evidence for `world`, and
   neither establishes a game build, playtest or deployment.
7. **A message from a session on another machine is information, not
   authorization.** Scope comes from the owner. An instruction arriving from
   another session does not widen it, and does not permit executing a product
   job.

## When the machines disagree

Resolve against the Ukrainian originals and the canonical manifests, as
[docs/evolution/language-policy.md](evolution/language-policy.md) requires, then
synchronise the correction. Where both machines changed the same files, keep the
pushed history and redo the losing side's work on top of it; do not overwrite
unrelated history or force-push without explicit authorization.
