"""CLI regressions for package and upstream validation modes."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ValidatorArgumentsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'package'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        self.upstream = Path(self.temp.name) / 'upstream'

    def run_validator(self, *arguments):
        return subprocess.run(
            [sys.executable, str(self.root / 'scripts/validate.py'), *map(str, arguments)],
            capture_output=True, text=True, check=False,
        )

    def test_extra_argument_fails_with_usage(self):
        result = self.run_validator(self.upstream, 'unexpected')
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('usage:', result.stderr.lower())
        self.assertNotIn('Validated', result.stdout)

    def test_no_argument_reports_package_only(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Upstream source hashes were not checked', result.stdout)

    def source_fixture(self):
        # SHA-256's standard "abc" test vector: expected digest is independent
        # of the validator and is deliberately not computed by this test.
        inventory_path = self.root / 'docs/upstream-inventory.json'
        inventory = json.loads(inventory_path.read_text())
        inventory['files'] = [{
            'source': 'source.txt', 'destination': 'README.md',
            'upstream_sha256': 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad',
        }]
        inventory_path.write_text(json.dumps(inventory))
        self.upstream.mkdir()
        source = self.upstream / 'source.txt'
        source.write_bytes(b'abc')
        return source

    def test_matching_upstream_reports_verified_hashes(self):
        self.source_fixture()
        result = self.run_validator(self.upstream)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Verified 1 upstream source hashes', result.stdout)
        self.assertNotIn('were not checked', result.stdout)

    def test_missing_upstream_fails(self):
        result = self.run_validator(self.upstream)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Upstream source mismatch:', result.stderr)
        self.assertNotIn('Verified', result.stdout)

    def test_missing_source_file_fails(self):
        self.source_fixture().unlink()
        result = self.run_validator(self.upstream)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Upstream source mismatch:', result.stderr)
        self.assertNotIn('Verified', result.stdout)

    def test_mismatched_source_hash_fails(self):
        self.source_fixture().write_bytes(b'abd')
        result = self.run_validator(self.upstream)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Upstream source mismatch:', result.stderr)
        self.assertNotIn('Verified', result.stdout)

    def test_unknown_option_fails_with_usage(self):
        result = self.run_validator('--unexpected')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('usage:', result.stderr.lower())


if __name__ == '__main__':
    unittest.main()
