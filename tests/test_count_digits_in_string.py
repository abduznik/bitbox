import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
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
