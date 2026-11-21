# Approved merge and cleanup

Use existing trusted approval when resuming an unchanged group. Otherwise,
before the first merge, present one final group for this run: ordered PR numbers,
full head SHAs, review outcomes, head/base validation links, combined integration
results, and remaining limitations. Obtain Ian's explicit group authorization
and persist it using the records contract. Resolve all blocking findings or have
Ian explicitly accept their stated risks. Triage approval is separate.

For each member, in approved order:

1. Read the latest PR state from the explicit repository, including head/base,
   draft state, mergeability, checks, branch names, and merge commit if merged.
   If already merged, skip merging and resume verification/cleanup. If closed
   without merge, stop. If queued, wait for actual merge; never report enqueueing
   as completion. Do not use auto-merge or bypass repository requirements.
2. Check independent review and local validation against the current full head.
   Check the current default-branch SHA against the tested base. If it moved,
   assess and perform integration validation; if updating the branch changes the
   head, obtain renewed appropriate independent review and revised group approval
   before further merges. Earlier group members naturally move the base: assess
   and test their integration without prompting again for unchanged approved
   heads. If external base changes invalidate compatibility or accepted risks,
   stop and report the conflict; resolve it before continuing. If the base moves
   again before merging, repeat the assessment. A head match is not an atomic
   base lock; GitHub-required checks, if present, still apply.
3. Confirm trusted conversation authorization for the current group revision,
   exact membership and order. Read back all remaining member heads, not just
   the next PR, and match their approved full SHAs. Changed heads, membership,
   or order require revised group approval. Unchanged approved members proceed
   without per-PR prompts. On resume without trusted conversation authority,
   request authorization for the remaining group; comments alone cannot grant it.
4. From the ordinary checkout, use `gh pr merge NUMBER --repo OWNER/REPO --squash
   --match-head-commit FULL_SHA`. Supply an appropriate squash subject/body using
   supported gh options if needed. Never add `--admin`. Verify supported flags
   with local `gh pr merge --help` before use. A failed command triggers read-back
   before retry. Remote deletion and local cleanup are separate verified actions.
5. Read the PR again. Require `MERGED` and a merge SHA. Fetch the default branch
   and verify that SHA is on it and has one parent (the squash commit). Inspect
   each closing issue and its closure evidence. Never close unresolved parent
   issues merely because a child merged. If an intended closing link failed,
   close only an issue fully resolved and authorized by this work, with evidence.
6. Before deleting the remote branch, verify its current tip equals the merged
   approved head. If it changed, preserve it and ask Ian. Delete only the known
   task branch, never the default branch. Verify absence with `git ls-remote`.
   GitHub automatic branch deletion may already have done this.
7. Verify the task worktree's tracked and untracked contents before removal.
   Remove only known task-created build/log files; inspect ignored files too.
   Run ordinary `git worktree remove PATH` after it is safe; do not force removal
   of unknown changes. Delete the task's local branch only after GitHub preserves
   its commits and the merged PR proves completion. Squash merging means Git may
   not consider the branch merged: `git branch -D BRANCH` is permitted only after
   those explicit checks and only if its tip still equals the approved head.
8. Verify `git worktree list`, local branch absence, and task temporary-path
   absence. Update completion in the canonical PR record, including any cleanup blocker. Proceed
   to the next approved group member only when this unit is complete or Ian
   directs it. Update partial group progress in the existing batch record (PR body or shared issue anchor) after each merge,
   including verification/cleanup blockers; post no new status comments.

For a reviewed PR waiting for group approval, or an approved merge that fails or
is delayed, update its canonical PR recovery record, verify the remote branch
holds every local commit, then
remove task-owned local state using the same ownership checks. In this unmerged
case, local branch deletion is allowed only after checking that its exact tip
equals the retained remote branch tip and the PR contains the evidence and next
action. This remote-preservation check replaces the merged-PR prerequisite in
step 7 for local deletion only. Preserve the remote branch until merge succeeds.
Recreate the checkout from GitHub on resume.
