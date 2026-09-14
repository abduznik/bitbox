"""Behaviour and input validation for word_frequency_top."""

import pytest

from tools.word_frequency_top import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("the cat the dog the",), "the:3"),
        (("cat dog cat dog",), "cat:2"),
        (("Cat cat",), "Cat:1"),
        (("  a\ta\nb ",), "a:2"),
        (("",), ""),
        (("  \t",), ""),
        (("kot kot pies",), "kot:2"),
    ],
)
def test_word_frequency_top(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("a", "b")])
def test_word_frequency_top_rejects_invalid_input(args):
    with pytest.raises(ValueError):
        run(*args)
