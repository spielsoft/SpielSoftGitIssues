# Workflow decisions

## Scope and ownership

Build one self-contained SpielSoftGitIssues plugin from a fixed revision of
Matt Pocock's plugin, with required dependencies and attribution retained.
Prefer copies and light adaptations after auditing upstream dependencies.
Shared workflow instructions belong in this plugin. Each application's custom
skills stay separately in that application's repository and remain authoritative
for its product, architecture, and validation requirements. Use unambiguous
plugin entry-point names and explicit references to applicable project guidance.

Run locally using Git and authenticated GitHub CLI. GitHub holds durable
operational records: issues, ordered batches, decisions, dependencies, PRs,
validation and review evidence, authorization, commits, and completion links.
Project configuration and plugin source are version-controlled tooling.

## Serial processing and approval

The triager proposes an ordered batch and dispositions for Ian's approval.
Process one coherent issue/fix through implementation, independent review,
Ian's merge decision, and cleanup before proceeding to the next.
Builders and fresh independent reviewers take turns. The review budget is one
initial review followed by at most two repair-and-review cycles; unresolved
findings then return to Ian.

Review, test evidence, and merge authorization identify the exact PR head commit.
Validation also records the base revision. Assess integration checks when main
changes. Changed code requires appropriate renewed validation and review;
changed PR head requires renewed merge authorization.

Squash merge to one main-branch commit per PR. Verify merged state, linked issue
closure, and branch cleanup. Reviews posted through Ian's GitHub identity are
agent review evidence; human authorization is a procedural gate.

## Recovery and local cleanup

After approval, all information needed to finish or resume the work must be on
GitHub. Push the complete implementation and record relevant evidence before
discarding working material. Approval alone is not evidence of a successful merge.
If merging fails, GitHub must retain the branch, PR, and recovery information.

At completion, remove task-owned local branches, disposable maintenance
worktrees, temporary logs, build outputs, and run locks. Do not retain a local
backlog, progress database, or task file. Use a disposable worktree per unit of
work so cleanup has a clear ownership boundary. Preserve the user's ordinary
checkout, unrelated files, and installed tooling. Never force-delete unexpected
changes; preserve the work and report the cleanup blocker.

Restart by inspecting GitHub and actual Git state. Use stable record markers and
explicit links to avoid duplicate PRs, comments, and actions. A merge completed
before interruption must resume at verification and cleanup.

## Project adoption and commissioning

Use a small version-controlled project tracker configuration pointing to product
rules and validation commands. Align applicable AGENTS.md policy before adopting
worktrees in a project. Repository settings changes must be concrete and visible.

Commission first against this plugin repository using an issue supplied by Ian’s
independent testing agent. Follow with the SpielOrders pilot: a genuine reproducible
bug and a report requesting behavior contrary to product intent. Use fictional data and product
evidence for triage. Also test interrupted PR creation, a changed head after
review, and reinvocation after merge before cleanup. Verify repeated invocation
does not duplicate completed work.

Keep local test evidence distinct from GitHub-enforced checks. Adopt
SpielPasswords and consider scheduling after successful manual commissioning.
