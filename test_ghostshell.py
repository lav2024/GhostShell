import unittest
from ghostshell import check_risks


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


if __name__ == "__main__":
    unittest.main()
