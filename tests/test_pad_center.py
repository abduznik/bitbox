import unittest
from tools.pad_center import run


class ToolTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual('--hi--', run(*('hi', '6', '-')))

    def test_case_2(self):
        self.assertEqual('long', run(*('long', '2', '.')))

    def test_case_3(self):
        self.assertEqual('____', run(*('', '4', '_')))

    def test_case_4(self):
        self.assertEqual('hi', run(*('hi', '0', ' ')))

    def test_case_5(self):
        self.assertEqual('🌍a🌍', run(*('a', '3', '🌍')))

    def test_invalid_arguments(self):
        for args in [(), ('a', '2'), ('a', '-1', '-'), ('a', 'x', '-'), ('a', '4', ''), ('a', '4', 'ab')]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                run(*args)
