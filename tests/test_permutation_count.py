import pytest
from tools.permutation_count import run

@pytest.mark.parametrize(
    "n, r, expected",
    [
        ("5", "3", "60"),
        ("5", "0", "1"),
        ("4", "4", "24"),
        ("6", "2", "30"),
    ],
)

def test_permutation_count_valid(n, r, expected):
    assert run(n, r) == expected

@pytest.mark.parametrize(
    "n, r",
    [
        ("5", "-1"),
        ("-5", "2"),
        ("3", "5"),
        ("x", "2"),
        ("abc", "def"),
    ],
)

def test_permutation_count_invalid(n, r):
    assert run(n, r).startswith("Error:")
