---
name: spiel-issues-triage
description: Evaluate GitHub reports against SpielSoft project behavior and propose an ordered batch for owner approval.
---

# Triage

Adapted from Matt Pocock's role-based triage. Read the shared
[workflow](../../references/workflow.md) and [records](../../references/records.md).
Use the [agent brief](AGENT-BRIEF.md) for actionable work.

## Roles and discovery

Categories: `bug`, `enhancement`. States: `spiel:needs-triage`, `spiel:needs-info`,
`spiel:ready`, `spiel:needs-human`, `spiel:wontfix`. Keep exactly one category and
one workflow state per triaged issue; preserve unrelated labels. Resolve
conflicting plugin states from the evidence or ask Ian when intent is ambiguous.

Discover unlabeled issues, needs-triage issues, and needs-info issues with new
reporter activity, oldest first. Also read relevant closed reports and existing
PRs. Resolve issue/PR number ambiguity before acting. External contributed code
is out of scope unless the project's contribution policy explicitly allows it.
An explicitly named external PR still must respect that policy.

## Evaluate each report

1. Gather the body, comments, labels, dates, linked PRs, applicable product rules,
   glossary/ADRs, and relevant code. Search by domain concept for existing behavior
   and similar prior rejections. Cite where you looked. Prior decisions are
   evidence to consider; changed product intent can warrant reconsideration.
2. Verify the claim. Reproduce bugs safely with fictional data and applicable
   checks. Record confirmed, not reproduced, or insufficient detail, with code
   and execution evidence. Distinguish an actual failure from a request contrary
   to intended behavior. A commissioning label never determines the verdict.
3. Identify duplicates and dependencies. Propose category, severity supported by
   impact, state, disposition, and order. A duplicate points to its canonical
   issue; an already-implemented request points to the implementation.
4. Ask specific questions only where missing information changes the decision.
   Reuse prior answers. Use existing project domain skills when needed and
   available; this plugin does not require external grilling/domain skills.

## Approve the ordered batch

Present all proposed comments, labels, closures, evidence, and work order in one
reviewable batch. Include complete acceptance criteria for actionable units.
For complex work use [split](../spiel-issues-split/SKILL.md) to propose coherent
slices. Wait for Ian's batch/disposition approval before applying mutations.

Record the approved batch and per-issue links using the records contract. Post
briefs for ready work; explain manual work for needs-human. For needs-info, record
what is established and the specific outstanding questions. For approved
rejections, post a respectful explanation citing product evidence, then close
with the appropriate reason. Rejected requests use `not planned`; already fixed
work uses `completed` only with implementation evidence. For duplicates, link the
canonical report and use an appropriate supported resolution.

Store rejection memory in GitHub; no `.out-of-scope` backlog is created. Post
comments before closure, then read back the outcome. Resume from prior records
and reporter answers without duplicating comments or re-asking resolved questions.
