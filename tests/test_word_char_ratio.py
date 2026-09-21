from tools.word_char_ratio import run


def test_word_char_ratio_with_punctuation():
    assert run("hello!") == "0.83"


def test_word_char_ratio_with_letters_only():
    assert run("hello") == "1.00"


def test_word_char_ratio_with_spaces():
    assert run("hello world") == "0.91"


def test_word_char_ratio_with_digits_only():
    assert run("12345") == "0.00"


def test_word_char_ratio_with_empty_string():
    assert run("") == "0.00"
