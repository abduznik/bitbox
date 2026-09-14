"""Behaviour and input validation for is_sorted."""

import pytest

from tools.is_sorted import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("1,2,3,4",), "True"),
        (("1,1,2",), "True"),
        (("1,3,2",), "False"),
        (("9",), "True"),
        (("-3,-2,0",), "True"),
        (("0.11,0.2",), "True"),
        (("9007199254740993,9007199254740992",), "False"),
    ],
)
def test_is_sorted(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize(
    "args", [(), ("1", "2"), ("",), ("1,,2",), ("x,2",), ("nan,1",), ("inf,2",)]
)
def test_is_sorted_rejects_invalid_input(args):
    with pytest.raises(ValueError):
        run(*args)
