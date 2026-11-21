# SpielSoftGitIssues

A self-contained plugin for serial GitHub issue triage, local implementation,
independent review, and owner-authorized squash merging across SpielSoft projects.

Version 0.1.2 adds concise GitHub records. Adoption requires fresh review and
installation verification. Preserve the approved installed source throughout an
active maintenance run. Earlier verification remains in the commissioning history.

The plugin prepares and independently reviews PRs serially, then requests one
final approval of the ordered group of PR numbers and exact head commits.
Triage approval is a separate decision.

It contains prompt-driven skills;
the agent runs local Git, GitHub CLI, and project checks. It is not a background
service or a GitHub-enforced approval system.

## Skills

| Skill | Purpose |
| --- | --- |
| spiel-issues-setup | Configure a project while preserving its custom skills |
| spiel-issues-triage | Propose an evidence-backed ordered batch |
| spiel-issues-run | Process/resume the approved batch serially |
| spiel-issues-build | Implement one coherent unit and publish evidence |
| spiel-issues-review | Fresh independent Standards/Spec review |
| spiel-issues-split | Propose dependent slices for larger issues |
| spiel-issues-tdd | Behavioral regression testing guidance |
| spiel-issues-pr | PR summary, evidence, and merge risk |

## Local Codex installation

Use a Codex version with `codex plugin marketplace add` and `codex plugin add`.
From this repository:

```sh
codex plugin marketplace add .
codex plugin add spielsoft-git-issues@spielsoft
```

The marketplace contains this one self-contained plugin. Source lives here;
Codex manages its installed copy. Reopen or refresh the client as required to
make newly installed skills visible. Use setup in a target project, then triage
and run. The installed host needs local shell access, Git, authenticated gh, and
fresh independent agent execution for review. If review execution is unavailable,
the workflow reports a pending handoff instead of claiming independent review.

ChatGPT-host and Claude Code runtime verification remain pending. The shared
procedures are separated from host packaging for subsequent adaptation.

## Development and commissioning

```sh
python3 scripts/validate.py
```

This checks manifests, skill names/frontmatter, runtime links, labels, inventory,
and license presence. It does not prove agent behavior or live GitHub effects.
See [commissioning scenarios](docs/commissioning.md),
[workflow decisions](docs/workflow-decisions.md), and
[upstream inventory](docs/upstream-inventory.md).

This repository is the first commissioning target; SpielOrders and SpielPasswords
follow. Its setup is recorded in [the tracker configuration](docs/agents/issue-tracker.md). Application setup and
live commissioning require the target project's current rules and owner gates.

## License

MIT for SpielSoft original contributions. Adapted from Matt Pocock's MIT-licensed
skills, with retained Dex Horthy/HumanLayer credits. See
[third-party notices](THIRD_PARTY_NOTICES.md) and [LICENSE](LICENSE).
