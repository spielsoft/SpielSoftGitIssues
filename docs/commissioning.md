# Commissioning scenarios

Run these against controlled fixtures and this plugin repository first, then the
approved SpielOrders pilot. Ian’s independent testing agent supplies the first issue.
Use fictional data. Static package validation establishes file integrity only.
Record actual observed outcomes; do not mark a scenario passed from reading it.

| Scenario | Required observed behavior |
| --- | --- |
| Real reproducible bug | Evidence-backed brief, owner-approved order, failing/passing regression evidence, linked PR, fresh independent review, explicit authorized squash merge |
| Request conflicts with product intent | Triage cites product rules and observed behavior; respectful explanation and owner-approved closure; commissioning label does not decide outcome |
| Interrupted PR creation | A PR already accepted by GitHub is discovered and reused after the client reports failure |
| Changed head after review | Old review/authorization remain historical; changed head gets renewed appropriate checks, independent review, and owner authorization |
| Main moves after validation | Integration impact assessed and checks repeated as needed; unchanged heads need no repeated approval; incompatible external changes stop merging |
| Two reviewed PRs await one decision | Build/review first, then build/review second; present both numbers/full heads in order, obtain one group approval, merge and verify each serially |
| Group head, membership, or order changes | Stop further merges; refresh applicable evidence and request a revised group decision; preserve the original authorization |
| Partial group completion/resume | Discover actual merged members, finish their verification/cleanup, reconstruct remaining approved heads; trusted existing authorization avoids individual prompts |
| Dependent PR preparation | Record prerequisite heads, distinguish preparation from delivery, validate combined order; planned later head changes require revised group approval |
| Merge succeeds, cleanup interrupted | Resume sees MERGED, avoids another merge, verifies closure and completes only task-owned cleanup |
| Approval followed by merge failure | Remote branch and PR retain work/recovery evidence; task-owned local state removed safely; resume reconstructs remotely |
| Unexpected local file | Preserve the file and report a cleanup blocker; no force removal |
| Review repeatedly fails | Initial review plus two repair/review cycles maximum across restarts, then owner escalation |
| Closed dependency was rejected | Do not treat it as delivered; return for disposition |
| Repeat completed invocation | No duplicate PR/comment/merge; completed units stay complete |
| Fresh context lacks owner authorization | GitHub history informs the handoff; explicit authorization for the remaining group is requested |

## Concise-record scenarios

Exercise these as instruction walkthroughs or controlled live trials; identify
which kind was performed and retain the resulting output for review.

- Supply a clean PR with complete tests and a fresh review at fixed head/base.
  Inspect rendered review text (`Approved`) and recover both axis outcomes,
  reviewer context, exact revisions and round from its metadata.
- Supply a reproducible defect and a request conflicting with product intent.
  Inspect actionable PR findings for the defect and a sourced issue disposition
  for the request; neither may be hidden in metadata.
- Simulate PR creation accepted before timeout, then retry with an automatically
  linked issue. Confirm reuse of the PR and no new issue/status comments.
- Resume a partial group with a legacy round-1 review, one merged member and an
  unexpected cleanup file. Recover authorization/history, preserve the file,
  update existing records, and leave the next member unmerged until resolved.
- Repeat with no changed facts. Confirm no writes; then change a head and confirm
  stale evidence cannot approve it or grant revised authorization.

## Live pilot prerequisites

Reinspect SpielOrders identity, instructions, clean state, open issues/PRs,
contribution restrictions, validation scripts, and GitHub settings. Amend its
checkout policy coherently before creating maintenance worktrees. Protect real
archive data, production app identity, signing rules, and foreground UI tests.
Ian approves the ordered triage batch, then one final ordered PR/head group. A distinct testing chat can help
file the commissioned reports when Ian coordinates it.

## Candidate 0.1.0 verification — 2026-11-21

- Downloaded and inventoried the exact upstream revision; source-file hashes verified.
- Package validator passed for eight skills, runtime references, manifests, labels,
  inventory, and complete MIT notices.
- Skill-creator's frontmatter validator passed for all eight skills.
- Installed successfully through the local Codex CLI marketplace and plugin APIs;
  Codex reports the plugin enabled. Compared all 18 runtime files against the
  installed cache after review fixes; contents match.
- A fresh independent reviewer walked the timeout, stale-head, unexpected-file,
  and repeated-review-failure scenarios. Fixed the reported failed-merge cleanup
  conflict, head/base evidence-key collision, and overly broad skill descriptions.
  The reviewer confirmed those findings resolved.
- This was an instruction-level scenario review, not live GitHub execution.
  SpielOrders commissioning, real merge/closure/cleanup execution, and ChatGPT
  and Claude Code host commissioning remain unverified.
