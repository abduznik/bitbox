"""Behaviour and input validation for gcd_of_list."""

import pytest

from tools.gcd_of_list import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("12,18,24",), "6"),
        (("-12,18",), "6"),
        (("0,0",), "0"),
        (("0,9",), "9"),
        (("-7",), "7"),
        (("17,19",), "1"),
    ],
)
def test_gcd_of_list(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize(
    "args", [(), ("1", "2"), ("",), ("1,,2",), ("x,2",), ("1.5,2",)]
)
def test_gcd_of_list_rejects_invalid_input(args):
    with pytest.raises(ValueError):
        run(*args)
