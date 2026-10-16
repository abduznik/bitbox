import pytest
from tools.fibonacci_sequence import run


def test_fibonacci_sequence_basic():
    assert run("6") == "0,1,1,2,3,5"
    assert run("1") == "0"
    assert run("2") == "0,1"
    assert run("3") == "0,1,1"
    assert run("4") == "0,1,1,2"
    assert run("5") == "0,1,1,2,3"
    assert run("0") == ""
    assert run(" 6 ") == "0,1,1,2,3,5"


def test_fibonacci_sequence_errors():
    assert run() == "Error: expected an integer"
    assert run("") == "Error: expected an integer"
    assert run("   ") == "Error: expected an integer"
    assert run("abc") == "Error: argument must be an integer"
    assert run("2.5") == "Error: argument must be an integer"
    assert run("-3") == "Error: argument must be a non-negative integer"
