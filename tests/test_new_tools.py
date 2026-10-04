import pytest

from tools import (
    collapse_whitespace,
    goldbach_check,
    is_deficient,
    is_kaprekar,
    is_pronic,
    is_sociable,
    nth_prime,
    pairwise_sum,
    second_smallest,
    sum_of_primes,
    word_frequency_top,
)

CASES = [
    (collapse_whitespace, ("  hello   world  ",), "hello world"),
    (collapse_whitespace, ("hello",), "hello"),
    (word_frequency_top, ("the cat the dog the",), "the:3"),
    (word_frequency_top, ("",), ""),
    (is_deficient, ("10",), "True"),
    (is_deficient, ("12",), "False"),
    (is_sociable, ("1264460",), "True"),
    (is_sociable, ("6",), "False"),  # perfect number: period-1 chain
    (sum_of_primes, ("10",), "17"),
    (sum_of_primes, ("1",), "0"),
    (nth_prime, ("5",), "11"),
    (nth_prime, ("1",), "2"),
    (goldbach_check, ("10",), "True"),
    (goldbach_check, ("7",), "False"),
    (is_pronic, ("6",), "True"),
    (is_pronic, ("7",), "False"),
    (second_smallest, ("3,1,4,1,5",), "1"),
    (pairwise_sum, ("1,2,3", "4,5,6"), "5,7,9"),
    (is_kaprekar, ("9",), "True"),
    (is_kaprekar, ("10",), "False"),
]


@pytest.mark.parametrize("tool,args,expected", CASES, ids=[c[0].__name__ for c in CASES])
def test_issue_examples(tool, args, expected):
    assert tool.run(*args) == expected


def test_bad_input_returns_error_string():
    for tool in (is_deficient, is_sociable, sum_of_primes, nth_prime,
                 goldbach_check, is_pronic, second_smallest, is_kaprekar):
        assert tool.run().startswith("Error:")
        assert tool.run("abc").startswith("Error:")


def test_pairwise_sum_length_mismatch():
    assert pairwise_sum.run("1,2", "4,5,6").startswith("Error:")
