---
name: spiel-issues-setup
description: Configure a SpielSoft project for GitHub issue maintenance, preserving its custom skills and product rules.
---

# Setup SpielSoftGitIssues

Adapted from Matt Pocock's setup-matt-pocock-skills. Read the shared
[workflow](../../references/workflow.md). This is a prompt-driven setup skill.

## Explore

Inspect remotes, repository identity/default branch, GitHub CLI authentication,
AGENTS.md, CLAUDE.md when applicable, CONTRIBUTING.md, existing custom skills,
validation scripts, product decisions, and any existing tracker configuration.
Identify restrictions on worktrees, app data, signing, foreground UI testing,
and external contributions. Resolve conflicting checkout policies through a
concrete proposed edit before maintenance begins.

## Present and apply

Use [issue-tracker-github.md](issue-tracker-github.md) as the small in-repository
configuration template. Fill it with verified facts and links to existing docs.
Keep domain documents and project skills where they already live. Link the
configuration from applicable agent instructions without overwriting surrounding
policy. Shared labels come from [labels.json](../../references/labels.json).

Show the actual configuration/policy diff and missing labels. Existing setup
approval covers the shown changes; ask only for missing material choices or
unapproved mutations. Create missing labels after approval; preserve existing
labels' names, colors, and meanings. Do not overwrite unrelated labels or create
a separate per-project shared-policy copy.

Ensure squash merging is allowed. If disabled, propose enabling it. Keep other
merge methods as configured unless Ian requests a change. Branch deletion may
be done explicitly by the workflow; enabling repository-wide automatic deletion
requires approval of that setting change. Do not configure required approving
reviews under a nonexistent second identity. Local validation comments are not
required status checks.

## Verify

Read back identity, written configuration, instructions, and labels. Report exact
changes and remaining prerequisites. Re-running setup must inspect and update
existing content, never append duplicate sections. Optional issue/PR templates
are separate project changes when requested. Setup does not file commissioning
reports, change app behavior, or schedule runs.
