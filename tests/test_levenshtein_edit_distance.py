"""Behaviour and input validation for levenshtein_edit_distance."""

import pytest

from tools.levenshtein_edit_distance import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("kitten,sitting",), "3"),
        (("same,same",), "0"),
        ((",",), "0"),
        ((",abc",), "3"),
        (("abc,",), "3"),
        (("a,b",), "1"),
        (("ab,ba",), "2"),
        (("café,cafe",), "1"),
        (("a,a,b",), "2"),
    ],
)
def test_levenshtein_edit_distance(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("a", "b"), ("abc",)])
def test_levenshtein_edit_distance_rejects_invalid_input(args):
    with pytest.raises(ValueError):
        run(*args)
