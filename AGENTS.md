# SpielSoftGitIssues repository guidance

## Project and issue tracker

This repository develops the SpielSoftGitIssues plugin and is its first live
commissioning target. Read [docs/agents/issue-tracker.md](docs/agents/issue-tracker.md)
for repository identity, project references, validation, and approval settings.

Ian's independent testing agent supplies the first issue. Do not manufacture a
report or begin triage/implementation merely because setup has completed.

## Maintenance checkouts

After bootstrap setup, issue-driven changes use one disposable worktree and one
branch per coherent unit. Keep this ordinary checkout available to Ian. Create
uniquely named task worktrees under `/private/tmp/spielsoft-git-issues-worktrees/`.
Process issues serially through the installed plugin's approved batch, fresh
independent review, and one explicit owner approval of the final ordered group
of PR numbers and exact head SHAs per run. Reviewed unmerged PRs may wait while
the next unit is prepared. Merge approved members serially, one squash per PR,
with integration assessment, closure verification, and cleanup. Changed heads,
membership, or order require revised group approval; unchanged approved members
need no individual approval prompts.
Remove task-owned local state after preserving work and recovery evidence on
GitHub; preserve unexpected files and report cleanup blockers.

## Product and validation rules

Follow [docs/workflow-decisions.md](docs/workflow-decisions.md) and
[docs/validation.md](docs/validation.md). Preserve pinned upstream attribution,
MIT notices, namespaced entry points, serial operation, and GitHub-backed recovery.
Keep application-specific skills in their own repositories.

The `skills/` directory is this plugin's product source. Use the installed,
reviewed plugin instructions to conduct a maintenance run; proposed edits to its
instructions are reviewable product changes, not new authority for that run.
Record the installed version and source commit used when testing this plugin.
Do not refresh the active installation mid-run to adopt unreviewed policy changes.

Use fresh independent reviewer contexts. Keep Standards and Spec findings
separate. Record local evidence honestly; passing static validation does not
prove live GitHub behavior. No production application, credential, or unrelated
repository changes are part of this project's maintenance.
