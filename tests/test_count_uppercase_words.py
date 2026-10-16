import unittest
from tools.count_uppercase_words import run


class ToolTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual('1', run(*('Hello world',)))

    def test_case_2(self):
        self.assertEqual('0', run(*('',)))

    def test_case_3(self):
        self.assertEqual('3', run(*('One TWO three Élan',)))

    def test_case_4(self):
        self.assertEqual('0', run(*('1hello lower',)))

    def test_case_5(self):
        self.assertEqual('3', run(*('A\tB\nC',)))

    def test_invalid_arguments(self):
        for args in [(), ('a', 'b')]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                run(*args)
