from tools.index_of import run


def test_index_of_basic():
    assert run("hello", "ll") == "2"


def test_index_of_start():
    assert run("hello", "he") == "0"


def test_index_of_not_found():
    assert run("hello", "xyz") == "-1"


def test_index_of_empty_substring():
    assert run("hello", "") == "0"


def test_index_of_full_match():
    assert run("hello", "hello") == "0"


def test_index_of_missing_argument():
    assert run("hello") == "Error: index_of requires text and substring"
