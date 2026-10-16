import unittest
from tools.is_valid_parentheses import run


class ToolTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual('True', run(*('([])',)))

    def test_case_2(self):
        self.assertEqual('True', run(*('',)))

    def test_case_3(self):
        self.assertEqual('True', run(*('a{b[c](d)}',)))

    def test_case_4(self):
        self.assertEqual('False', run(*('([)]',)))

    def test_case_5(self):
        self.assertEqual('False', run(*(')',)))

    def test_case_6(self):
        self.assertEqual('False', run(*('(',)))

    def test_invalid_arguments(self):
        for args in [(), ('a', 'b')]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                run(*args)
