import pytest
from tools.collatz_length import run


def test_collatz_length_basic():
    # 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (8 steps)
    assert run("6") == "8"
    assert run("1") == "0"
    assert run("2") == "1"
    assert run("3") == "7"
    assert run("12") == "9"


def test_collatz_length_errors():
    assert run() == "Error: expected an integer"
    assert run("") == "Error: expected an integer"
    assert run("abc") == "Error: argument must be an integer"
    assert run("0") == "Error: argument must be a positive integer"
    assert run("-5") == "Error: argument must be a positive integer"
