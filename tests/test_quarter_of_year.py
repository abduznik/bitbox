"""Behaviour and input validation for quarter_of_year."""

import pytest

from tools.quarter_of_year import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("2026-08-15",), "Q3"),
        (("2026-01-01",), "Q1"),
        (("2026-03-31",), "Q1"),
        (("2026-04-01",), "Q2"),
        (("2026-06-30",), "Q2"),
        (("2026-07-01",), "Q3"),
        (("2026-10-01",), "Q4"),
        (("2026-12-31",), "Q4"),
        ((" 2026-08-15 ",), "Q3"),
    ],
)
def test_quarter_of_year(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("2026-08-15", "extra")])
def test_quarter_of_year_rejects_wrong_argument_count(args):
    assert run(*args) == "Error: Please provide exactly one argument."


@pytest.mark.parametrize("args", [("",), ("not-a-date",), ("2026-13-01",), ("2026/08/15",)])
def test_quarter_of_year_rejects_bad_input(args):
    result = run(*args)
    assert result.startswith("Error:")
