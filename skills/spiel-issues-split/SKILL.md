---
name: spiel-issues-split
description: Break a large GitHub issue into owner-approved coherent slices with explicit dependencies for serial maintenance.
---

# Split into coherent issues

Adapted from Matt Pocock's to-tickets. Read the shared
[workflow](../../references/workflow.md) and [records](../../references/records.md).

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a reference (a spec path, an issue number or URL) as an argument, fetch it and read its full body and comments.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Ticket titles and descriptions should use the project's domain glossary vocabulary, and respect ADRs in the area you're touching.

Look for opportunities to prefactor the code to make the implementation easier. "Make the change easy, then make the easy change."

### 3. Draft vertical slices

Break the work into **tracer bullet** tickets.

<vertical-slice-rules>

- Each slice cuts a narrow but COMPLETE path through every layer (schema, API, UI, tests): vertical, NOT a horizontal slice of one layer
- A completed slice is demoable or verifiable on its own
- Each slice is sized to fit in a single fresh context window
- Any prefactoring should be done first

</vertical-slice-rules>

Give each ticket its **blocking edges** and state whether each prerequisite is
needed for preparation or must be merged before delivery. Apply the shared
workflow dependency rules when preparing reviewed PRs for one group approval.

For wide refactors, sequence expand, migrate, and contract steps only when each
can land safely. If slices cannot pass validation independently, propose one
coherent PR or return the decomposition decision to Ian.

### Approve and publish

Present a numbered breakdown with title, blockers, acceptance criteria, and the
end-to-end behavior delivered by each issue. Include the proposed order in the
triage batch. Wait for approval before creating child issues. Reuse any existing
children rather than duplicating them after interruption.

Publish each approved slice as a GitHub issue, in dependency order. Link it to the
parent using native sub-issues where supported and record blockers through native
dependencies where available. Check local gh help before using version-dependent
flags; use explicit issue links as a fallback. Apply `spiel:ready` only after
approval. Leave the parent open until all of its acceptance criteria are met.

Each issue needs: parent link, current/desired behavior, acceptance criteria,
explicit scope boundaries, blocking issue URLs, and approved batch URL. Prefer
behavioral contracts to procedural file-edit instructions. Keep all operational
records on GitHub. Work serially through the approved order.
