# Upstream inventory and adaptation map

Pinned source: https://github.com/mattpocock/skills/tree/abeeaf95660ba9e8b7c753eb38f441ca707a8823

Downloaded the archive for that exact revision. The machine-readable
[inventory](upstream-inventory.json) records original paths, destination paths,
and SHA-256 hashes of original bytes before adaptation. No runtime fetch of
upstream material is required.

| Upstream skill | Bundled skill | Adaptation |
| --- | --- | --- |
| setup-matt-pocock-skills | spiel-issues-setup | GitHub only; existing project rules; one tracker document; shared labels |
| triage | spiel-issues-triage | Role-based evidence and briefs; ordered approved batch; GitHub rejection history |
| implement-spec | spiel-issues-run | Serial coordinator; per-unit PR; restart from GitHub; bounded review and merge gate |
| implement | spiel-issues-build | One approved branch; local validation; coordinator owns independent review |
| code-review | spiel-issues-review | Retained Standards/Spec axes and smell guidance; fresh sequential reviewer |
| pr | spiel-issues-pr | Retained body/evidence/risk guidance and HumanLayer credits; exact head/base and closing links |
| to-tickets | spiel-issues-split | Coherent slices and blockers; approved GitHub children; serial order |
| tdd | spiel-issues-tdd | Retained behavior tests and loop; project testing conventions; no external design-skill dependency |

## Dependency dispositions

- Triage's AGENT-BRIEF.md: retained with shorter examples and approved-scope rules.
- Triage's OUT-OF-SCOPE.md: inspected; local rejection database replaced by GitHub
  disposition comments and links to existing product decisions.
- Triage's grilling/domain-modeling calls: replaced with focused clarification and
  references to existing project skills, when present. No mandatory external skills.
- Setup's GitHub template: adapted to project identity, product/validation links,
  explicit approval policy, and worktree policy. GitLab/local tracker templates,
  separate per-project label mapping, and domain-scaffolding templates are omitted.
- implement-spec's TDD/review dependencies: bundled named skills; concurrent
  integration-branch/merger-agent flow replaced by serial per-unit PR coordination.
- implement's TDD/review dependencies: bundled TDD, review delegated by coordinator.
- TDD's tests.md and mocking.md: retained verbatim. codebase-design dependency
  replaced by the short public-interface definition and project testing conventions.
- PR's CREDITS.md and metadata: retained verbatim, attributing Dex Horthy/HumanLayer.
  The PR skill embeds the credited visual guidance; it has no runtime dependency
  on HumanLayer's show-me skill. HumanLayer MIT notice is also bundled.
- Upstream marketplace structure: retained and renamed to SpielSoft. Codex plugin
  manifest follows the locally installed Codex format. Claude Code packaging and
  runtime commissioning remain future work.
- Upstream agent UI metadata, release tooling, npm dependencies, unrelated skills,
  documentation, and artwork are omitted. No upstream execution hooks are retained.

## Shared additions

The workflow, GitHub record markers, labels, and merge/cleanup procedure are
SpielSoft-specific additions under `references/`. These are operational policy;
project-specific product decisions and customized skills remain in the app repo.

Validate packaging and source hashes with
`python3 scripts/validate.py /path/to/downloaded/upstream`.
