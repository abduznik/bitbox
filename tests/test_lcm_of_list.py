"""Behaviour and input validation for lcm_of_list."""

import pytest

from tools.lcm_of_list import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("4,6",), "12"),
        (("4,6,10",), "60"),
        (("-4,6",), "12"),
        (("0,0",), "0"),
        (("0,5",), "0"),
        (("5,0",), "0"),
        (("-7",), "7"),
        (("100000000000000000000,3",), "300000000000000000000"),
    ],
)
def test_lcm_of_list(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize(
    "args", [(), ("1", "2"), ("",), ("1,,2",), ("x,2",), ("1.5,2",)]
)
def test_lcm_of_list_rejects_invalid_input(args):
    with pytest.raises(ValueError):
        run(*args)
