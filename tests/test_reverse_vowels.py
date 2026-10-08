from tools.reverse_vowels import run


def test_reverse_vowels_example():
    assert run("hello") == "holle"


def test_reverse_vowels_reverses_only_vowels():
    assert run(" information ") == " onfirmatoin "
    assert run("Python") == "Python"
    assert run("aeiouAEIOU") == "UOIEAuoiea"


def test_reverse_vowels_empty_and_single_vowel():
    assert run("") == ""
    assert run("u") == "u"


def test_reverse_vowels_invalid_argument():
    assert run() == "Error: expected string argument"
    assert run(123) == "Error: expected string argument"
    assert run(None) == "Error: expected string argument"
    assert run("hello", "world") == "Error: expected string argument"
