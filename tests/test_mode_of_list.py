import pytest
from tools.mode_of_list import run


def test_mode_of_list_basic():
    assert run("1,2,2,3") == "2"
    assert run("5") == "5"
    assert run("1, 1, 2, 2") == "1,2"
    assert run("-3, -3, 0, 1") == "-3"
    assert run("1.5, 2.5, 2.5, 3.5") == "2.5"


def test_mode_of_list_errors_and_boundaries():
    assert run() == "Error: expected a comma-separated list of numbers"
    assert run("") == "Error: expected a comma-separated list of numbers"
    assert run("   ") == "Error: expected a comma-separated list of numbers"
    assert run("1,2,abc") == "Error: all elements must be numbers"
    # Strict boundary check: reject empty elements without silent tolerance
    assert run("1,,2") == "Error: all elements must be numbers"
    assert run(",1,2") == "Error: all elements must be numbers"
    assert run("1,2,") == "Error: all elements must be numbers"
    assert run("1, ,2") == "Error: all elements must be numbers"
