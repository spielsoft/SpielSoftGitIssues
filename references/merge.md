# Approved merge and cleanup

1. Read the latest PR state from the explicit repository, including head/base,
   draft state, mergeability, checks, branch names, and merge commit if merged.
   If already merged, skip merging and resume verification/cleanup. If closed
   without merge, stop. If queued, wait for actual merge; never report enqueueing
   as completion. Do not use auto-merge or bypass repository requirements.
2. Check independent review and local validation against the current full head.
   Check the current default-branch SHA against the tested base. If it moved,
   assess and perform integration validation; if updating the branch changes the
   head, obtain renewed independent review and Ian's approval. If the base moves
   again before merging, repeat the assessment. A head match is not an atomic
   base lock; GitHub-required checks, if present, still apply.
3. Present Ian the final PR, head, review findings/outcome, local evidence, and
   remaining limitations. Use his explicit merge authorization for that head.
   Record it using the shared records contract. All blocking findings must be
   resolved or explicitly accepted by Ian with the stated risk.
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
   absence. Record completion on the PR, including any cleanup blocker. Proceed
   to the next approved issue only when this unit is complete or Ian directs it.

If approval is given but merge fails or is delayed, publish the failure and all
recovery information, verify the remote branch holds every local commit, then
remove task-owned local state using the same ownership checks. In this unmerged
case, local branch deletion is allowed only after checking that its exact tip
equals the retained remote branch tip and the PR contains the evidence and next
action. This remote-preservation check replaces the merged-PR prerequisite in
step 7 for local deletion only. Preserve the remote branch until merge succeeds.
Recreate the checkout from GitHub on resume.
