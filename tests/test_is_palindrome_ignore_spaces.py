import pytest
from tools.is_palindrome_ignore_spaces import run


def test_is_palindrome_ignore_spaces_true():
    assert run("nurses run") == "True"
    assert run("racecar") == "True"
    assert run("was it a car or a cat i saw") == "True"


def test_is_palindrome_ignore_spaces_case_insensitive():
    assert run("Nurses Run") == "True"


def test_is_palindrome_ignore_spaces_false():
    assert run("hello world") == "False"
    assert run("nurses run!") == "False"


def test_is_palindrome_ignore_spaces_single_char_and_empty():
    assert run("a") == "True"
    assert run("") == "True"
    assert run("   ") == "True"


def test_is_palindrome_ignore_spaces_no_args():
    assert run() == "Error: expected a string argument"
