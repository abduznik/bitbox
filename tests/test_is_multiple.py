"""Behaviour and input validation for is_multiple."""

import pytest

from tools.is_multiple import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("10", "5"), "True"),
        (("11", "5"), "False"),
        (("0", "5"), "True"),
        (("-10", "5"), "True"),
        (("10", "-5"), "True"),
        (("9007199254740993", "3"), "True"),
    ],
)
def test_is_multiple(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize(
    "args", [(), ("1",), ("1", "2", "3"), ("1", "0"), ("x", "2"), ("1.5", "2")]
)
def test_is_multiple_rejects_invalid_input(args):
    with pytest.raises(ValueError):
        run(*args)
