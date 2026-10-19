from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from install import install


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / "source"
        for name in ("ba-one", "ba-two"):
            skill = self.source / name
            (skill / "templates").mkdir(parents=True)
            (skill / "SKILL.md").write_text("example", encoding="utf-8")
            (skill / "templates/test.md").write_text("template", encoding="utf-8")

    def test_dry_run_has_no_writes(self):
        dest = self.base / "new-root"
        self.assertEqual(install(dest, source=self.source, dry_run=True), ["ba-one", "ba-two"])
        self.assertFalse(dest.exists())

    def test_conflict_preserves_existing_and_copies_nothing(self):
        dest = self.base / "installed"
        existing = dest / "ba-two"
        existing.mkdir(parents=True)
        sentinel = existing / "keep.txt"
        sentinel.write_text("unchanged", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            install(dest, source=self.source)
        self.assertFalse((dest / "ba-one").exists())
        self.assertEqual(sentinel.read_text(), "unchanged")

    def test_nested_resources_survive(self):
        dest = self.base / "installed"
        install(dest, source=self.source)
        for source_file in self.source.rglob("*"):
            if source_file.is_file():
                self.assertEqual(source_file.read_bytes(), (dest / source_file.relative_to(self.source)).read_bytes())

    def test_source_tree_cannot_be_destination(self):
        with self.assertRaises(ValueError):
            install(self.source / "ba-one" / "nested", source=self.source)


if __name__ == "__main__":
    unittest.main()
