"""Behaviour and input validation for second_largest."""

import pytest

from tools.second_largest import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("3,1,4,1,5",), "4"),
        (("5,5,4",), "4"),
        (("-1,-5,-3",), "-3"),
        (("1.2,1.4,1.3",), "1.3"),
        (("9007199254740993,9007199254740995",), "9007199254740993"),
    ],
)
def test_second_largest(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize(
    "args",
    [
        (),
        ("1", "2"),
        ("",),
        ("1,,2",),
        ("x,2",),
        ("nan,1",),
        ("inf,2",),
        ("1",),
        ("2,2",),
    ],
)
def test_second_largest_rejects_invalid_input(args):
    with pytest.raises(ValueError):
        run(*args)
