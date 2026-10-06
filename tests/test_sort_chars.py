from tools.sort_chars import run


def test_sort_chars_example():
    assert run("cba") == "abc"


def test_sort_chars_already_sorted():
    assert run("abc") == "abc"


def test_sort_chars_repeated_chars():
    assert run("banana") == "aaabnn"


def test_sort_chars_with_spaces():
    assert run("c b a") == "  abc"


def test_sort_chars_single_char():
    assert run("a") == "a"


def test_sort_chars_empty():
    assert run("") == ""