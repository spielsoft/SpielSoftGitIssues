---
name: spiel-issues-run
description: Process or resume an approved SpielSoft GitHub issue batch serially through build, independent review, authorized merge, and cleanup.
---

# Run a maintenance batch

Adapted from Matt Pocock's implement-spec coordinator. Read the shared
[workflow](../../references/workflow.md), [records](../../references/records.md),
and [merge procedure](../../references/merge.md).

Issues form a task graph with blocking relationships. Only the first eligible
unit in the owner-approved order runs. Use fresh contexts and sparse context
pointers to GitHub issues, project rules, code revisions, and bundled skills.

1. Load the approved batch, all its issue/PR records, and current Git/GitHub state.
   If no approved batch exists, use [triage](../spiel-issues-triage/SKILL.md).
   If approval is missing, present the proposal and wait. Discover existing open,
   closed, and merged PRs for each issue before creating work. If more than one
   plausible PR or branch exists, reconcile with Ian rather than guessing.
2. Resume merged work at verification and cleanup. Resume an open PR at the
   latest incomplete phase. A closed unmerged PR needs owner direction. Re-read
   comments after an ambiguous API error before retrying creation or mutation.
3. For the next unit, check dependencies' actual dispositions. If blocked, record
   why and return the choice of waiting or changing order to Ian. Create or
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
   repairs. Count rounds from GitHub on resume. At exhaustion, record unresolved
   findings, mark needs-human, and return to Ian.
6. Present the reviewed PR and validation evidence for Ian's explicit merge
   authorization at its current head. Await his decision. Approval of the batch
   does not grant merge permission. Follow the merge procedure, verify closure,
   and remove task-owned local state even if a failed merge must resume remotely.
7. Record completion and move to the next approved unit. On interruption, GitHub
   records and branches must suffice to reconstruct progress. Do not retain local
   progress files. Do not start the next unit while unresolved ownership, cleanup,
   or owner decisions remain.
