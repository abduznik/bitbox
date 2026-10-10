"""Behaviour and input validation for is_pandigital."""

import pytest

from tools.is_pandigital import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("52134",), "True"),
        (("1",), "True"),
        (("123456789",), "True"),
        (("112",), "False"),
        (("124",), "False"),
        (("1235",), "False"),
        (("0",), "False"),
        (("abc",), "False"),
        (("",), "False"),
        ((" 52134 ",), "True"),
    ],
)
def test_is_pandigital(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("1", "2")])
def test_is_pandigital_rejects_wrong_argument_count(args):
    assert run(*args) == "Error: Please provide exactly one argument."
