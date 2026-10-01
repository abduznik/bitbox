import pytest
from tools.count_digits_in_string import run


def test_basic():
    assert run("abc123") == "3"


def test_no_digits():
    assert run("hello world") == "0"


def test_only_digits():
    assert run("1234567890") == "10"


def test_empty():
    assert run("") == "0"


def test_mixed_symbols():
    assert run("phone: +1 (555) 019-2834") == "11"


def test_missing_argument():
    assert run() == "Error: expected string argument"


def test_invalid_types():
    assert run(12345) == "Error: expected string argument"
    assert run(None) == "Error: expected string argument"
    assert run(["123"]) == "Error: expected string argument"
    assert run(True) == "Error: expected string argument"
