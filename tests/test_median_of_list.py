"""Behaviour and input validation for median_of_list."""

import pytest

from tools.median_of_list import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("3,1,2",), "2"),
        (("4,1,3,2",), "2.5"),
        (("1.2,1.4",), "1.3"),
        (("9",), "9"),
        (("-5,-1,-3",), "-3"),
        (("9007199254740993,9007199254740995",), "9007199254740994"),
        ((" 3, 3, 1 ",), "3"),
    ],
)
def test_median_of_list(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize(
    "args", [(), ("1", "2"), ("",), ("1,,2",), ("x,2",), ("nan,1",), ("inf,2",)]
)
def test_median_of_list_rejects_invalid_input(args):
    with pytest.raises(ValueError):
        run(*args)
