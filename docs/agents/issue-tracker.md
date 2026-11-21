# Issue tracker: GitHub

Issues and PRs live in `spielsoft/SpielSoftGitIssues` on `github.com`:
https://github.com/spielsoft/SpielSoftGitIssues

Use authenticated local `gh`, explicitly targeting this repository. The default
branch is `main`. The operational GitHub identity is `spielsoft`.

## Project rules

- Governing instructions: [AGENTS.md](../../AGENTS.md).
- Product intent: [README.md](../../README.md) and
  [workflow decisions](../workflow-decisions.md).
- Validation commands and evidence requirements: [validation](../validation.md).
- Commissioning scenarios: [commissioning](../commissioning.md).
- Attribution boundaries: [third-party notices](../../THIRD_PARTY_NOTICES.md) and
  [upstream inventory](../upstream-inventory.md).
- This repository has no application data, signing identities, or native UI tests.
  Tests must use fictional fixtures and disposable paths. Protect credentials,
  the ordinary checkout, installed plugin configuration, and unrelated repositories.
- Foreground/UI interaction is not required for routine validation. A new test
  needing such interaction should describe it and obtain Ian's agreement.
- There are no separate customized project skills at setup time. `skills/` is the
  distributable plugin source; follow AGENTS.md for self-referential testing.

## Maintenance approval and execution

Ian approves the ordered batch and its dispositions, then separately authorizes
one final ordered group of PR numbers and full head SHAs for squash merging.
Prepare and review units serially; reviewed PRs may wait unmerged. Changed heads,
membership, or order require revised group approval. Unchanged approved members
need no individual prompts; base movement triggers integration assessment/checks. Use a fresh independent reviewer, with one
initial review and at most two repair/review cycles. Run locally and serially.

Disposable maintenance worktrees under
`/private/tmp/spielsoft-git-issues-worktrees/` are allowed by AGENTS.md's
Maintenance checkouts section. Keep durable operational records on GitHub and
remove task-owned local state when safely persisted, verifying merge and cleanup
separately. Shared procedures and labels come from the installed SpielSoftGitIssues
plugin. Repository-wide automatic branch deletion is off; the workflow verifies
and deletes its own task branches explicitly.

External PRs as a request surface: no. A proposal to accept external code or change
that scope requires Ian's direction; this setup establishes no new contribution
policy. Issues are the initial commissioning surface.

Read full issue bodies/comments and linked PRs. Use native dependencies where
available, otherwise explicit issue links. Check resolutions before treating
closed blockers as delivered. Record product-based rejection explanations in
GitHub. Search existing open and closed records before creating new work.
