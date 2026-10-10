"""Behaviour and input validation for is_harshad."""

import pytest

from tools.is_harshad import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("18",), "True"),
        (("1",), "True"),
        (("10",), "True"),
        (("12",), "True"),
        (("11",), "False"),
        (("13",), "False"),
        ((" 18 ",), "True"),
    ],
)
def test_is_harshad(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("1", "2")])
def test_is_harshad_rejects_wrong_argument_count(args):
    assert run(*args) == "Error: Please provide exactly one argument."


@pytest.mark.parametrize("args", [("",), ("x",), ("1.5",), ("0",), ("-4",)])
def test_is_harshad_rejects_bad_input(args):
    result = run(*args)
    assert result.startswith("Error:")
