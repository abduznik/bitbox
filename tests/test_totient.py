import unittest
from tools.totient import run


class ToolTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual('6', run(*('9',)))

    def test_case_2(self):
        self.assertEqual('1', run(*('1',)))

    def test_case_3(self):
        self.assertEqual('12', run(*('13',)))

    def test_case_4(self):
        self.assertEqual('12', run(*('36',)))

    def test_case_5(self):
        self.assertEqual('512', run(*('1024',)))

    def test_invalid_arguments(self):
        for args in [(), ('0',), ('-1',), ('3.5',), ('x',), ('9', 'extra')]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                run(*args)

    def test_matches_coprime_count(self):
        import math
        for n in range(1, 150):
            expected = sum(math.gcd(n, k) == 1 for k in range(1, n + 1))
            self.assertEqual(str(expected), run(str(n)))
