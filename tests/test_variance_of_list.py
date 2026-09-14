"""Behaviour and input validation for variance_of_list."""

import pytest

from tools.variance_of_list import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("1,2,3",), "0.67"),
        (("2",), "0.00"),
        (("2,2,2",), "0.00"),
        ((" -1, 0, 1 ",), "0.67"),
        (("0.5,1.5",), "0.25"),
    ],
)
def test_variance_of_list(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize(
    "args", [(), ("1", "2"), ("",), ("1,,2",), ("x,2",), ("nan,1",), ("inf,2",)]
)
def test_variance_of_list_rejects_invalid_input(args):
    with pytest.raises(ValueError):
        run(*args)
