"""Exercise installation-path validation through the distributable CLI."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class InstallationPathTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.package = Path(self.temporary.name) / 'package'
        shutil.copytree(ROOT, self.package, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def update_json(self, relative, change):
        path = self.package / relative
        data = json.loads(path.read_text())
        change(data)
        path.write_text(json.dumps(data))

    def validate(self):
        return subprocess.run(
            [sys.executable, str(self.package / 'scripts/validate.py')],
            cwd=self.temporary.name, capture_output=True, text=True,
        )

    def test_unchanged_package_passes(self):
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Validated 8 skills', result.stdout)

    def test_missing_marketplace_source_fails(self):
        self.update_json('.claude-plugin/marketplace.json',
                         lambda data: data['plugins'][0].update(source='./does-not-exist'))
        result = self.validate()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('Marketplace source', result.stderr)

    def test_skills_directory_without_entry_points_fails(self):
        self.update_json('.codex-plugin/plugin.json',
                         lambda data: data.update(skills='./licenses/'))
        result = self.validate()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('Missing required skill entry point', result.stderr)

    def test_existing_unrelated_marketplace_source_fails(self):
        self.update_json('.claude-plugin/marketplace.json',
                         lambda data: data['plugins'][0].update(source='./licenses/'))
        result = self.validate()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('Marketplace source', result.stderr)

    def test_missing_required_entry_point_fails(self):
        (self.package / 'skills/spiel-issues-run/SKILL.md').unlink()
        result = self.validate()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('Missing required skill entry point', result.stderr)

    def test_configured_skills_are_validated(self):
        configured = self.package / 'configured-skills'
        shutil.copytree(self.package / 'skills', configured)
        self.update_json('.codex-plugin/plugin.json',
                         lambda data: data.update(skills='./configured-skills/'))
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)

        skill = configured / 'spiel-issues-run/SKILL.md'
        original = skill.read_text()
        skill.write_text(original.replace('description:', 'omitted-description:', 1))
        result = self.validate()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('missing description', result.stderr)

        skill.write_text(original + '\n[Missing dependency](missing.md)\n')
        result = self.validate()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('missing dependency', result.stderr)


if __name__ == '__main__':
    unittest.main()
