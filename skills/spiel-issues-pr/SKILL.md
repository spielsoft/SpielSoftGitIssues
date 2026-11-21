---
name: spiel-issues-pr
description: Write or update a SpielSoftGitIssues maintenance PR with issue links, local evidence, exact revisions, and merge risk.
metadata:
  credits:
    skill: show-me
    author: Dex Horthy
    organisation: Humanlayer
    url: "https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md"
---

Adapted from Matt Pocock, including the retained [HumanLayer credit](CREDITS.md).
Read the shared [workflow](../../references/workflow.md) and
[records](../../references/records.md).

Lead with the concrete problem and resulting behavior. Usually one or two
sentences plus validation suffice. Use `Closes #N` for fully resolved issues.
Give commands/results and material limitations; use before/after evidence or a
visual only when it helps assess the change. Omit empty sections, generic risk
labels, checklists, and process narration. Follow required project template fields
without filling optional sections merely because they exist.

Discover an existing PR by repository, branch and issue before creation, including
closed and merged PRs. After an ambiguous response, read back before retrying.
Update the existing body and its canonical maintenance record in place, preserving
owner-authored content and historical evidence. Store full head/base and recovery
fields according to the records contract. Keep validation in the PR and independent
review on the PR; use automatic issue links or one brief pointer if needed.

A draft may open after a meaningful commit is pushed. Mark ready after validation
and independent review. Return the PR URL and unresolved concerns to the coordinator.
