"""Behaviour and input validation for count_negative."""

import pytest

from tools.count_negative import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("-1,2,-3",), "2"),
        (("1,2,3",), "0"),
        (("-5,-2,-9",), "3"),
        (("0,-1,0,-2",), "2"),
        (("10,-4,7,-1,0",), "2"),
        (("  -1, 2, -3  ",), "2"),
        (("1.5,-2.5,0",), "1"),
    ],
)
def test_count_negative(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("1,2", "3,4")])
def test_count_negative_rejects_wrong_argument_count(args):
    assert run(*args) == "Error: Please provide exactly one comma-separated list."


@pytest.mark.parametrize("args", [("",), ("1,x,-2",)])
def test_count_negative_rejects_bad_input(args):
    result = run(*args)
    assert result.startswith("Error:")
