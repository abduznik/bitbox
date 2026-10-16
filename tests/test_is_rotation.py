import unittest
from tools.is_rotation import run


class ToolTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual('True', run(*('abc', 'bca')))

    def test_case_2(self):
        self.assertEqual('True', run(*('abc', 'abc')))

    def test_case_3(self):
        self.assertEqual('True', run(*('', '')))

    def test_case_4(self):
        self.assertEqual('False', run(*('abc', 'bc')))

    def test_case_5(self):
        self.assertEqual('False', run(*('abc', 'acb')))

    def test_case_6(self):
        self.assertEqual('True', run(*('é🌍', '🌍é')))

    def test_case_7(self):
        self.assertEqual('False', run(*('Ab', 'ab')))

    def test_invalid_arguments(self):
        for args in [(), ('a',), ('a', 'b', 'c')]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                run(*args)
