"""Behaviour and input validation for is_base64."""

import pytest

from tools.is_base64 import run


@pytest.mark.parametrize(
    "text, expected",
    [
        ("aGVsbG8=", "True"),
        ("YWJjZA==", "True"),
        ("YWJj", "True"),
        ("", "False"),
        ("hello", "False"),
        ("aGVsbG8", "False"),
        ("aGVsbG8===", "False"),
        ("aGVs bG8=", "False"),
        ("aGVsbG8_", "False"),
        ("ZE==", "False"),
        ("مرحبا", "False"),
    ],
)
def test_is_base64(text, expected):
    assert run(text) == expected


@pytest.mark.parametrize("args", [(), ("YQ==", "Yg==")])
def test_is_base64_rejects_invalid_input(args):
    assert run(*args) == "Error: Requires exactly one argument"
