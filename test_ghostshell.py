import unittest
from ghostshell import check_risks
from ghostshell import check_risks, explain_known_command

class TestGhostShell(unittest.TestCase):

    def test_normal_command_has_no_warning(self):
        self.assertEqual(check_risks("mkdir demo"), [])

    def test_recursive_delete_is_flagged(self):
        warnings = check_risks("rm -rf ./temp")
        self.assertTrue(any("Recursive deletion" in w for w in warnings))

    def test_shutdown_is_flagged(self):
        warnings = check_risks("shutdown")
        self.assertTrue(any("shut down" in w for w in warnings))

    def test_command_separator_is_flagged(self):
        warnings = check_risks("mkdir demo && shutdown")
        self.assertTrue(any("separators" in w for w in warnings))

    def test_matching_is_case_insensitive(self):
        warnings = check_risks("RM -RF ./temp")
        self.assertTrue(any("Recursive deletion" in w for w in warnings))
    
    def test_mkdir_explanation(self):
        result = explain_known_command("mkdir demo")
        self.assertIn("directory named demo", result)

    def test_mkdir_parent_option(self):
        result = explain_known_command("mkdir -p demo/subfolder")
        self.assertIn("parent directories", result)

    def test_unknown_command_returns_none(self):
        result = explain_known_command("unknowncommand")
        self.assertIsNone(result)
    def test_cd_with_path(self):
        result = explain_known_command("cd projects")
        self.assertIn("current directory to projects", result)

    def test_cd_parent_directory(self):
        result = explain_known_command("cd ..")
        self.assertIn("parent directory", result)

    def test_cd_without_path(self):
        result = explain_known_command("cd")
        self.assertIn("behavior depends on the shell", result)

if __name__ == "__main__":
    unittest.main()
