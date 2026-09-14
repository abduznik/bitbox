"""Behaviour and input validation for fibonacci_nth."""

import pytest

from tools.fibonacci_nth import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("0",), "0"),
        (("1",), "1"),
        (("2",), "1"),
        (("6",), "8"),
        (("10",), "55"),
        (("100",), "354224848179261915075"),
    ],
)
def test_fibonacci_nth(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("1", "2"), ("-1",), ("1.5",), ("x",)])
def test_fibonacci_nth_rejects_invalid_input(args):
    with pytest.raises(ValueError):
        run(*args)
