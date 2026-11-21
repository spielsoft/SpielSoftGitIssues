"""Exercise label validation through the validator CLI in disposable packages."""
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class LabelValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.package = Path(self.temporary.name) / 'plugin'
        shutil.copytree(ROOT, self.package,
                        ignore=shutil.ignore_patterns('.git', '__pycache__', 'tests'))
        self.label_path = self.package / 'references/labels.json'
        self.labels = json.loads(self.label_path.read_text())

    def validate(self, labels):
        self.label_path.write_text(json.dumps(labels))
        return subprocess.run([sys.executable, str(self.package / 'scripts/validate.py')],
                              cwd=self.package, capture_output=True, text=True)

    def assert_invalid(self, labels):
        result = self.validate(labels)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertNotIn('Traceback', result.stderr)
        self.assertIn('label', result.stderr.lower())

    def test_shipped_labels_pass(self):
        result = self.validate(self.labels)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_empty_or_missing_required_labels_fail(self):
        self.assert_invalid([])
        for name in ('bug', 'enhancement', 'spiel:needs-triage', 'spiel:needs-info',
                     'spiel:ready', 'spiel:needs-human', 'spiel:wontfix', 'spiel:batch'):
            with self.subTest(missing=name):
                self.assert_invalid([label for label in self.labels if label['name'] != name])

    def test_missing_empty_or_wrong_type_fields_fail(self):
        for field in ('name', 'description', 'color'):
            for value in (None, '', '   ', 123, True, [], {}):
                with self.subTest(field=field, value=value):
                    labels = copy.deepcopy(self.labels)
                    labels[0][field] = value
                    self.assert_invalid(labels)
            with self.subTest(missing=field):
                labels = copy.deepcopy(self.labels)
                del labels[0][field]
                self.assert_invalid(labels)

    def test_colors_require_exactly_six_hex_digits(self):
        for color in ('not-a-color', 'abc', '1234567', '#123456', '12345g',
                      '123456\n', ' 123456', '１２３４５６'):
            with self.subTest(color=color):
                labels = copy.deepcopy(self.labels)
                labels[0]['color'] = color
                self.assert_invalid(labels)
        labels = copy.deepcopy(self.labels)
        labels[0]['color'] = 'Ab09EF'
        result = self.validate(labels)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_duplicate_names_fail(self):
        self.assert_invalid(self.labels + [copy.deepcopy(self.labels[0])])

    def test_non_list_and_non_object_definitions_fail(self):
        for labels in (None, {}, 'bug', 1, [None], ['bug'], [123], [[]]):
            with self.subTest(labels=labels):
                self.assert_invalid(labels)


if __name__ == '__main__':
    unittest.main()
