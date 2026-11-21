# Local validation

Run `python3 scripts/validate.py` from the repository root. It checks manifests,
skill names/frontmatter, runtime links, labels, source-inventory structure, and
license presence, with no network or third-party dependencies. Python 3.9+ is
required by the validator. Run `git diff --check` for whitespace defects.

When changing upstream imports, obtain the pinned archive in a disposable
location and run `python3 scripts/validate.py /path/to/upstream` to verify source
hashes. Preserve the upstream revision, notices, and file-level adaptation map.

For changed skills, also use the installed skill-creator's `quick_validate.py`
when available, with PyYAML in a disposable environment. Record a missing tool
as a limitation rather than claiming it ran. This external development check
is not a runtime dependency of the distributed plugin.

For workflow changes, have a fresh independent reviewer exercise applicable
scenarios in [commissioning.md](commissioning.md), recording inputs, prescribed
or executed actions, and outcomes. Distinguish an instruction walkthrough from
executed behavior. Reproduce a real bug through an appropriate observable boundary
before fixing it when feasible; avoid tests that only assert instruction wording.

For packaging changes, verify installation with the local Codex CLI and compare
installed runtime files to the reviewed source. Refresh the active installation
only after review/owner approval when a maintenance run depends on that plugin.
Never silently replace its governing policy during the run.

Before merging, record exact head/base SHAs, commands, results, reviewer findings,
and unrun checks in the PR. GitHub mutations in live tests follow the approved
batch and merge gates. Do not use another application's real data for tests.
