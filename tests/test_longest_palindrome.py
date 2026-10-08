import pytest
from tools.longest_palindrome import run


def test_longest_palindrome_basic():
    assert run("forgeeksskeegfor") == "geeksskeeg"
    assert run("babad") == "bab"  # or "aba"
    assert run("cbbd") == "bb"
    assert run("a") == "a"
    assert run("ac") == "a"


def test_longest_palindrome_errors():
    assert run() == "Error: Please provide exactly one text argument."
    assert run("a", "b") == "Error: Please provide exactly one text argument."
    assert run("") == ""
