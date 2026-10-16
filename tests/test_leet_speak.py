import unittest
from tools.leet_speak import run


class ToolTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual('h3110', run(*('hello',)))

    def test_case_2(self):
        self.assertEqual('H3110', run(*('HELLO',)))

    def test_case_3(self):
        self.assertEqual('44331111005577', run(*('aAeEiIlLoOsStT',)))

    def test_case_4(self):
        self.assertEqual('xyz 123!', run(*('xyz 123!',)))

    def test_case_5(self):
        self.assertEqual('', run(*('',)))

    def test_invalid_arguments(self):
        for args in [(), ('a', 'b')]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                run(*args)
