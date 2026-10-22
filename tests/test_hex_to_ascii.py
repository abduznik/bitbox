
import unittest
from tools.hex_to_ascii import run


class ToolTests(unittest.TestCase):
    def test_valid_hex(self):
        self.assertEqual("Hi", run("4869"))

    def test_single_character(self):
        self.assertEqual("A", run("41"))

    def test_empty_string(self):
        self.assertEqual("", run(""))

    def test_invalid_hex(self):
        self.assertTrue(run("4G").startswith("Error:"))

    def test_odd_length_hex(self):
        self.assertTrue(run("486").startswith("Error:"))

    def test_non_ascii_byte(self):
        self.assertTrue(run("FF").startswith("Error:"))

    def test_missing_argument(self):
        self.assertTrue(run().startswith("Error:"))


if __name__ == "__main__":
    unittest.main()
