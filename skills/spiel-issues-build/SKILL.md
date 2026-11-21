---
name: spiel-issues-build
description: Implement one approved SpielSoft GitHub issue in its assigned maintenance worktree and prepare local evidence and a PR.
---

# Build one unit

Adapted from Matt Pocock's implement skill. Read the shared
[workflow](../../references/workflow.md) and [records](../../references/records.md).

Fetch the issue and approved brief, state its title, and read project rules.
Confirm the assigned branch, worktree ownership, base SHA, and scope before edits.
If the request or acceptance criteria conflict with product rules, return the
conflict for triage. Keep the application's customized skills separate and follow
its relevant implementation and validation guidance.

Use [TDD](../spiel-issues-tdd/SKILL.md) where appropriate: reproduce the bug with a
behavioral regression check, then make the smallest coherent fix. Run focused
checks during development and applicable full validation at completion. Record
unrun checks and permission-dependent UI tests honestly. Refactoring must serve
the issue and obey project review practice.

Commit on the assigned issue branch, inspect the committed diff, and validate
that final head as required. Push to the verified target repository. Discover
existing PRs by repository, head branch, and issue links before creating one.
Use [PR guidance](../spiel-issues-pr/SKILL.md) to create/update the PR and evidence;
link only issues actually resolved. Update the canonical PR record with validation
and recovery facts; do not post separate work or validation comments.

Return the PR, full head/base SHAs, evidence, and unresolved concerns to the
coordinator. The coordinator performs independent review in a fresh context and
queues the reviewed PR for the run's single final group approval. The coordinator
may prepare the next unit after this review while this PR waits unmerged. Do not
merge, self-approve, or independently start another issue.
