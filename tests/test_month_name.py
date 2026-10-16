"""Behaviour and input validation for month_name."""

import pytest

from tools.month_name import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("2026-08-15",), "August"),
        (("2026-01-01",), "January"),
        (("2026-12-31",), "December"),
        (("2024-02-29",), "February"),
        ((" 2026-08-15 ",), "August"),
    ],
)
def test_month_name(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("2026-08-15", "extra")])
def test_month_name_rejects_wrong_argument_count(args):
    assert run(*args) == "Error: Please provide exactly one argument."


@pytest.mark.parametrize(
    "args", [("",), ("not-a-date",), ("2026-13-01",), ("2026/08/15",), ("15-08-2026",)]
)
def test_month_name_rejects_bad_input(args):
    result = run(*args)
    assert result.startswith("Error:")
