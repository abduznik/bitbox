"""Tests for set_difference."""

import pytest

from tools.set_difference import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("1,2,3", "2,4"), "1,3"),
        (("apple,banana,mango", "banana"), "apple,mango"),
        (("a,b,a,c", "b"), "a,c"),
        (("1,2", "1,2"), ""),
        ((" apple, banana ", " banana "), "apple"),
        (("a,b,c", "x,y"), "a,b,c"),
        (("", "1,2"), ""),
    ],
)
def test_set_difference(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize(
    "args",
    [
        (),
        ("1,2",),
        ("1,2", "2,3", "4,5"),
    ],
)
def test_set_difference_rejects_wrong_argument_count(args):
    assert run(*args) == "Error: Please provide exactly two comma-separated lists."