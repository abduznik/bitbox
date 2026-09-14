"""Behaviour and input validation for is_twin_prime."""

import pytest

from tools.is_twin_prime import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("3",), "True"),
        (("5",), "True"),
        (("17",), "True"),
        (("2",), "False"),
        (("7",), "False"),
        (("9",), "False"),
        (("0",), "False"),
        (("-3",), "False"),
        (("49",), "False"),
    ],
)
def test_is_twin_prime(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("3", "5"), ("abc",), ("3.5",)])
def test_is_twin_prime_rejects_invalid_input(args):
    with pytest.raises(ValueError):
        run(*args)
