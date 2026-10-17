"""Behaviour and input validation for mime_from_ext."""

import pytest

from tools.mime_from_ext import run


@pytest.mark.parametrize(
    "extension, expected",
    [
        (".png", "image/png"),
        ("jpg", "image/jpeg"),
        (".HTML", "text/html"),
        (".json", "application/json"),
        (".tar.gz", "application/x-tar"),
        ("  .svg  ", "image/svg+xml"),
        (".unknown-extension", "application/octet-stream"),
        ("", "application/octet-stream"),
    ],
)
def test_mime_from_ext(extension, expected):
    assert run(extension) == expected


@pytest.mark.parametrize("args", [(), (".png", ".jpg")])
def test_mime_from_ext_rejects_invalid_input(args):
    assert run(*args) == "Error: Requires exactly one argument"
