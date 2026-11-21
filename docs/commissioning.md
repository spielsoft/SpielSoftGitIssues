# Commissioning scenarios

Run these against controlled fixtures first, then the approved SpielOrders pilot.
Use fictional data. Static package validation establishes file integrity only.
Record actual observed outcomes; do not mark a scenario passed from reading it.

| Scenario | Required observed behavior |
| --- | --- |
| Real reproducible bug | Evidence-backed brief, owner-approved order, failing/passing regression evidence, linked PR, fresh independent review, explicit authorized squash merge |
| Request conflicts with product intent | Triage cites product rules and observed behavior; respectful explanation and owner-approved closure; commissioning label does not decide outcome |
| Interrupted PR creation | A PR already accepted by GitHub is discovered and reused after the client reports failure |
| Changed head after review | Old review/authorization remain historical; changed head gets renewed appropriate checks, independent review, and owner authorization |
| Main moves after validation | Integration impact assessed and checks repeated as needed; changed head gets renewed authorization |
| Merge succeeds, cleanup interrupted | Resume sees MERGED, avoids another merge, verifies closure and completes only task-owned cleanup |
| Approval followed by merge failure | Remote branch and PR retain work/recovery evidence; task-owned local state removed safely; resume reconstructs remotely |
| Unexpected local file | Preserve the file and report a cleanup blocker; no force removal |
| Review repeatedly fails | Initial review plus two repair/review cycles maximum across restarts, then owner escalation |
| Closed dependency was rejected | Do not treat it as delivered; return for disposition |
| Repeat completed invocation | No duplicate PR/comment/merge; completed units stay complete |
| Fresh context lacks owner authorization | GitHub history informs the handoff; renewed explicit merge authorization is requested |

## Live pilot prerequisites

Reinspect SpielOrders identity, instructions, clean state, open issues/PRs,
contribution restrictions, validation scripts, and GitHub settings. Amend its
checkout policy coherently before creating maintenance worktrees. Protect real
archive data, production app identity, signing rules, and foreground UI tests.
Ian approves the ordered batch and each merge. A distinct testing chat can help
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
