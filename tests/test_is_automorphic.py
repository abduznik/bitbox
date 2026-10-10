"""Behaviour and input validation for is_automorphic."""

import pytest

from tools.is_automorphic import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("25",), "True"),
        (("5",), "True"),
        (("6",), "True"),
        (("76",), "True"),
        (("1",), "True"),
        (("0",), "True"),
        (("7",), "False"),
        (("12",), "False"),
        ((" 25 ",), "True"),
    ],
)
def test_is_automorphic(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("1", "2")])
def test_is_automorphic_rejects_wrong_argument_count(args):
    assert run(*args) == "Error: Please provide exactly one argument."


@pytest.mark.parametrize("args", [("",), ("x",), ("1.5",), ("-4",)])
def test_is_automorphic_rejects_bad_input(args):
    result = run(*args)
    assert result.startswith("Error:")
