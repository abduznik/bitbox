import pytest
from tools.count_occurrences import run


def test_count_occurrences_basic():
    assert run("banana", "a") == "3"
    assert run("mississippi", "ss") == "2"
    assert run("hello world", "o") == "2"


def test_count_occurrences_no_match():
    assert run("banana", "z") == "0"


def test_count_occurrences_empty_substring():
    assert run("abc", "") == "4"


def test_count_occurrences_missing_arguments():
    assert run() == "Error: expected text and substring arguments"
    assert run("banana") == "Error: expected text and substring arguments"


def test_count_occurrences_invalid_types():
    assert run(123, "a") == "Error: expected string arguments"
    assert run("banana", 123) == "Error: expected string arguments"
    assert run(None, "a") == "Error: expected string arguments"
