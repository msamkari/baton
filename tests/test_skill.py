import json
import pathlib
import re
import unittest
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent


def lf(b):
    return b.replace(b"\r\n", b"\n")


def skill_text():
    return lf((ROOT / "SKILL.md").read_bytes()).decode("utf-8")


class SkillTests(unittest.TestCase):
    def test_both_copies_and_bundle_are_identical(self):
        root = lf((ROOT / "SKILL.md").read_bytes())
        self.assertEqual(root, lf((ROOT / "skills" / "structured-handover-doc" / "SKILL.md").read_bytes()))
        with zipfile.ZipFile(ROOT / "releases" / "v1" / "structured-handover-doc.skill") as z:
            self.assertEqual(z.namelist(), ["structured-handover-doc/SKILL.md"])
            self.assertIsNone(z.testzip())
            self.assertEqual(lf(z.read(z.namelist()[0])), root)

    def test_frontmatter_and_version(self):
        t = skill_text()
        m = re.match(r"---\nname: structured-handover-doc\ndescription: (.+)\n---\n", t)
        self.assertTrue(m)
        j = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(j["name"], "structured-handover")
        self.assertEqual(j["license"], "MIT")
        self.assertRegex(j["version"], r"^\d+\.\d+\.\d+$")
        self.assertIn("## " + j["version"], (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))

    def test_question_rule_has_no_contradiction(self):
        t = skill_text()
        self.assertIn("ask exactly one direct clarifying question in the chat, and only before the document is created", t)
        self.assertIn("Only when it cannot be inferred", t)
        self.assertIn("After the document exists, no question goes in the chat", t)
        self.assertIn("the single comment described in the final step is the only question", t)
        self.assertNotIn("Don't put any question in the chat. After", t)  # the old unconditional wording
        self.assertNotIn("ask one direct question before starting", t)
        self.assertIn("add exactly one comment", t)

    def test_fallback_when_no_document_tool(self):
        t = skill_text()
        self.assertIn("If no document-creation tool or connector is available", t)
        self.assertIn("say so in one line", t)
        self.assertIn("offer to write the handover as a Markdown file in the project", t)
        self.assertIn("Write the file only after the user says yes", t)
        self.assertIn("never write a file without asking", t)

    def test_data_minimisation_rule(self):
        t = skill_text()
        for needle in ("Data minimisation", "health details", "financial account numbers", "passwords and keys",
                       "government ID numbers", "contact details", "unless the user explicitly asks for them to be included and they are needed for the handover"):
            self.assertIn(needle, t)
        self.assertNotIn("and contact details if available", t)

    def test_still_skill_only_and_no_personal_data(self):
        for p in ROOT.rglob("*"):
            if p.is_file() and ".git" not in p.parts and p.suffix in (".md", ".json") and p.name != "test_skill.py":
                self.assertIsNone(re.search(r"C:[\\/]Users|@gmail|sk-[A-Za-z0-9]{16}", p.read_text(encoding="utf-8")), str(p))
        stray = [p for p in ROOT.rglob("*.py") if p.parent.name != "tests" and ".git" not in p.parts]
        self.assertEqual(stray, [])  # skill only: no scripts
        self.assertNotIn("allowed-tools", skill_text())


if __name__ == "__main__":
    unittest.main()
