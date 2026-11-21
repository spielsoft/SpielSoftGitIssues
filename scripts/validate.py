#!/usr/bin/env python3
"""Validate the distributable plugin without network or third-party packages."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('upstream', nargs='?', type=Path, metavar='UPSTREAM_DIRECTORY',
                    help='also verify source hashes against this upstream snapshot')
args = parser.parse_args()
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

manifest = json.loads((ROOT / '.codex-plugin/plugin.json').read_text())
market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
require(market['plugins'][0]['name'] == manifest['name'], 'Marketplace name mismatch')
source = (ROOT / market['plugins'][0]['source']).resolve()
require(source.is_dir(), 'Marketplace source directory is missing')
require(source == ROOT, 'Marketplace source must identify the validated package root')
skills = (source / manifest['skills']).resolve()
require(skills.is_relative_to(ROOT), 'Skills directory is outside package')
require(skills.is_dir(), 'Missing skills directory')
for entry_point in ('run', 'setup', 'triage', 'split', 'build', 'tdd', 'review', 'pr'):
    path = skills / f'spiel-issues-{entry_point}' / 'SKILL.md'
    require(path.is_file(), f'Missing required skill entry point: {path}')
require(manifest['license'] == 'MIT', 'Unexpected project license')
names = set()
for skill in sorted(skills.glob('*/SKILL.md')):
    text = skill.read_text()
    front = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    require(front is not None, f'{skill}: missing frontmatter')
    if not front:
        continue
    name = re.search(r'^name: ([a-z0-9-]+)$', front[1], re.M)
    desc = re.search(r'^description: .+', front[1], re.M)
    require(name is not None and name[1] == skill.parent.name, f'{skill}: invalid name')
    require(desc is not None, f'{skill}: missing description')
    if name:
        require(name[1] not in names, f'{skill}: duplicate name')
        names.add(name[1])
    require('../../references/workflow.md' in text, f'{skill}: missing shared contract')

# Check linked runtime dependencies, excluding fenced code and external links.
for folder in (skills, ROOT / 'references'):
    for path in folder.rglob('*.md'):
        text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for link in re.findall(r'\]\(([^)]+)\)', text):
            if '://' in link or link.startswith('#'):
                continue
            target = (path.parent / link.split('#')[0]).resolve()
            require(target.is_relative_to(ROOT), f'{path}: dependency outside package: {link}')
            require(target.is_file(), f'{path}: missing dependency: {link}')
        for forbidden in ('/setup-matt-pocock-skills', 'Call the Skill tool', 'call the Skill tool'):
            require(forbidden not in text, f'{path}: unresolved upstream invocation: {forbidden}')

inventory = json.loads((ROOT / 'docs/upstream-inventory.json').read_text())
require(len(inventory['revision']) == 40, 'Missing full upstream pin')
for entry in inventory['files']:
    require((ROOT / entry['destination']).is_file(), f'Missing imported file: {entry}')
    require(re.fullmatch('[0-9a-f]{64}', entry['upstream_sha256']) is not None, 'Invalid source digest')
# Optionally verify against a downloaded snapshot, without modifying it.
if args.upstream is not None:
    upstream = args.upstream
    for entry in inventory['files']:
        path = upstream / entry['source']
        require(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == entry['upstream_sha256'],
                f'Upstream source mismatch: {path}')
for path, holder in [('LICENSE', 'SpielSoft'), ('licenses/matt-pocock-MIT.txt', 'Matt Pocock'), ('licenses/humanlayer-MIT.txt', 'HumanLayer')]:
    text = (ROOT / path).read_text()
    require(holder in text and 'Permission is hereby granted' in text and 'THE SOFTWARE IS PROVIDED' in text,
            f'Incomplete license: {path}')
labels = json.loads((ROOT / 'references/labels.json').read_text())
required_labels = {
    'bug', 'enhancement', 'spiel:needs-triage', 'spiel:needs-info',
    'spiel:ready', 'spiel:needs-human', 'spiel:wontfix', 'spiel:batch',
}
label_names = set()
require(isinstance(labels, list), 'Labels must be a list')
if isinstance(labels, list):
    for index, label in enumerate(labels):
        require(isinstance(label, dict), f'Label {index}: expected an object')
        if not isinstance(label, dict):
            continue
        for field in ('name', 'description', 'color'):
            value = label.get(field)
            require(isinstance(value, str) and bool(value.strip()),
                    f'Label {index}: {field} must be a nonempty string')
        color = label.get('color')
        require(isinstance(color, str) and re.fullmatch(r'[0-9a-fA-F]{6}', color) is not None,
                f'Label {index}: color must contain six hexadecimal digits')
        name = label.get('name')
        if isinstance(name, str):
            require(name not in label_names, f'Duplicate label: {name}')
            label_names.add(name)
require(required_labels <= label_names,
        f'Missing required labels: {sorted(required_labels - label_names)}')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'Validated {len(names)} skills, runtime links, manifests, labels, licenses, and source inventory.')
if args.upstream is None:
    print('Upstream source hashes were not checked (package-only validation).')
else:
    print(f'Verified {len(inventory["files"])} upstream source hashes against {args.upstream}.')
