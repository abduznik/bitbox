"""Behaviour and input validation for aliquot_sum."""

import pytest

from tools.aliquot_sum import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("12",), "16"),
        (("1",), "0"),
        (("6",), "6"),
        (("28",), "28"),
        ((" 15 ",), "9"),
        (("100",), "117"),
    ],
)
def test_aliquot_sum(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("1", "2")])
def test_aliquot_sum_rejects_wrong_argument_count(args):
    assert run(*args) == "Error: Please provide exactly one argument."


@pytest.mark.parametrize("args", [("",), ("x",), ("1.5",), ("0",), ("-4",)])
def test_aliquot_sum_rejects_bad_input(args):
    result = run(*args)
    assert result.startswith("Error:")
