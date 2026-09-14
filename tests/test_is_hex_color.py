"""Behaviour and input validation for is_hex_color."""

import pytest

from tools.is_hex_color import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("#FF5733",), "True"),
        (("#abc",), "True"),
        (("#abcd",), "True"),
        (("#12345678",), "True"),
        (("#abCD09",), "True"),
        (("",), "False"),
        (("FF5733",), "False"),
        (("#12",), "False"),
        (("#12345",), "False"),
        (("#1234567",), "False"),
        (("#123456789",), "False"),
        (("#ggg",), "False"),
        (("#abc\n",), "False"),
        ((" #abc",), "False"),
    ],
)
def test_is_hex_color(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("#fff", "#000")])
def test_is_hex_color_rejects_invalid_input(args):
    with pytest.raises(ValueError):
        run(*args)
