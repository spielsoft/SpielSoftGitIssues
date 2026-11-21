# Issue tracker: GitHub

<!-- Template: replace all angle-bracket fields with verified project facts. -->

Issues and PRs live in `<owner/repository>` on `<github-host>`.
Use authenticated local `gh`; explicitly specify this repository on operations.
Default branch: `<branch>`.

## Project rules

- Governing agent instructions: `<relative path>`
- Product intent and architecture: `<relative paths>`
- Validation commands and acceptance procedure: `<relative paths and commands>`
- Protected app/data/identity boundaries: `<relative paths and concise rules>`
- Foreground/UI-test permission: `<explicit policy>`
- Custom project skills: `<paths and routing guidance>`

## Maintenance approval and execution

- Ian approves the ordered triage batch and its listed dispositions.
- Ian approves one final ordered group of PR numbers and full head SHAs per run.
  Triage approval is distinct. Build/review proceed serially; reviewed PRs may wait
  unmerged. Changed heads, membership, or order require revised group approval;
  unchanged members proceed without individual prompts. Assess/test moved bases.
- Review: fresh independent context, initial review plus at most two repair/review cycles.
- Run locally and serially; temporary maintenance worktrees are allowed under
  `<agreed parent path>` by `<applicable policy section>`.
- GitHub retains operational records. Remove task-owned local state after
  approved work has been safely persisted; verify merge and cleanup separately.
- Shared workflow, records, and labels come from the installed SpielSoftGitIssues
  plugin. Project product/validation rules remain in this repository.
- External PRs as a request surface: no. Follow CONTRIBUTING.md for external code.

Read full issue bodies/comments and linked PRs. Use native GitHub dependencies
when available; otherwise record explicit blocking issue links. Inspect resolution
before treating a closed dependency as satisfied. Keep rejection reasons in GitHub
comments with product-rule links. Check existing closed reports before new work.
