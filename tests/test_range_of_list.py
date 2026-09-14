import pytest
from tools.range_of_list import run


def test_range_of_list_basic():
    assert run("3,1,4,1,5") == "4"
    assert run("10, 20, 30") == "20"
    assert run("5") == "0"
    assert run("-5, 5") == "10"
    assert run("1.5, 4.5") == "3"


def test_range_of_list_errors():
    assert run() == "Error: expected a comma-separated list of numbers"
    assert run("") == "Error: expected a comma-separated list of numbers"
    assert run("1, 2, abc") == "Error: all elements must be numbers"
    assert run("   ") == "Error: expected a comma-separated list of numbers"


def test_range_of_list_empty_elements_boundary():
    assert run("1,,5") == "Error: all elements must be numbers"
    assert run(",1,5") == "Error: all elements must be numbers"
    assert run("1,5,") == "Error: all elements must be numbers"
    assert run("1, ,5") == "Error: all elements must be numbers"
