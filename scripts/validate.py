#!/usr/bin/env python3
"""Validate the distributable plugin without network or third-party packages."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

manifest = json.loads((ROOT / '.codex-plugin/plugin.json').read_text())
market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
require(market['plugins'][0]['name'] == manifest['name'], 'Marketplace name mismatch')
require((ROOT / manifest['skills']).is_dir(), 'Missing skills directory')
require(manifest['license'] == 'MIT', 'Unexpected project license')
names = set()
for skill in sorted((ROOT / 'skills').glob('*/SKILL.md')):
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
for folder in ('skills', 'references'):
    for path in (ROOT / folder).rglob('*.md'):
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
if len(sys.argv) == 2:
    upstream = Path(sys.argv[1])
    for entry in inventory['files']:
        path = upstream / entry['source']
        require(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == entry['upstream_sha256'],
                f'Upstream source mismatch: {path}')
for path, holder in [('LICENSE', 'SpielSoft'), ('licenses/matt-pocock-MIT.txt', 'Matt Pocock'), ('licenses/humanlayer-MIT.txt', 'HumanLayer')]:
    text = (ROOT / path).read_text()
    require(holder in text and 'Permission is hereby granted' in text and 'THE SOFTWARE IS PROVIDED' in text,
            f'Incomplete license: {path}')
labels = json.loads((ROOT / 'references/labels.json').read_text())
require(len({x['name'] for x in labels}) == len(labels), 'Duplicate labels')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'Validated {len(names)} skills, runtime links, manifests, labels, licenses, and source inventory.')
