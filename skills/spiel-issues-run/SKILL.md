---
name: spiel-issues-run
description: Process or resume an approved SpielSoft GitHub issue batch serially through build, independent review, authorized merge, and cleanup.
---

# Run a maintenance batch

Adapted from Matt Pocock's implement-spec coordinator. Read the shared
[workflow](../../references/workflow.md), [records](../../references/records.md),
and [merge procedure](../../references/merge.md).

Issues form a task graph with blocking relationships. Prepare the first eligible
unit in the owner-approved order, then review it before preparing the next.
Reviewed unmerged PRs may wait for the final group decision. Use fresh contexts and sparse context
pointers to GitHub issues, project rules, code revisions, and bundled skills.

1. Load the approved batch, all its issue/PR records, and current Git/GitHub state.
   If no approved batch exists, use [triage](../spiel-issues-triage/SKILL.md).
   If approval is missing, present the proposal and wait. Discover existing open,
   closed, and merged PRs for each issue before creating work. If more than one
   plausible PR or branch exists, reconcile with Ian rather than guessing.
2. Resume merged work at verification and cleanup. Resume an open PR at the
   latest incomplete phase. A closed unmerged PR needs owner direction. Re-read
   bodies, comments and reviews after an ambiguous API error before retrying.
3. For the next unit, check dependencies' actual dispositions. If blocked, record
   why and return the choice of waiting or changing order to Ian. Distinguish
   preparation dependencies from delivery prerequisites using the shared workflow. Create or
   reconstruct its disposable worktree from the remote branch or current default
   branch, respecting project policy. Never reset unexpected existing changes.
4. Start one fresh builder using [build](../spiel-issues-build/SKILL.md). Pass the
   issue, approved brief/batch, project configuration, worktree, base SHA, and
   existing PR if any. Wait for the builder before review. Persist work/evidence
   on GitHub. No integration branch or parallel issue implementation is needed.
5. Start a fresh independent reviewer using
   [review](../spiel-issues-review/SKILL.md), with exact head/base and issue/rules.
   Record round 0. For blocking findings, hand them to the builder, then review
   the resulting revision in a fresh context; rounds 1 and 2 are the maximum
   repairs. Count rounds from canonical records and legacy reviews on resume. At exhaustion, record unresolved
   findings, mark needs-human, and return to Ian.
6. After a unit passes review, persist its exact head/base and evidence and mark
   it ready for the group. Clean disposable local state under the remote-preservation
   checks when safe. Prepare/review the next unit serially; waiting reviewed PRs
   do not require a merge decision before that work. Resolve ownership, unexpected
   files, and blocking review findings before proceeding.
7. Once the run's PRs are ready, check final heads, scopes, dependencies, and
   combined integration in the intended merge order. Present one ordered group
   of PR numbers, full head SHAs, reviews, validation, and limitations for Ian's
   explicit final approval. Triage approval grants no merge permission. Persist
   the group record and links; changed heads/membership/order require a revision.
8. Follow the merge procedure serially for approved members without individual
   reapproval prompts. Verify closure and cleanup after each and record partial
   group progress. A moved base triggers integration assessment and checks.
   On interruption, reconstruct completed and remaining members from GitHub and
   actual Git state; resume merged work at verification/cleanup. Preserve remote
   recovery evidence and retain no local progress files.
