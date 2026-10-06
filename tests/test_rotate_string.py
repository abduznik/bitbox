import os
import subprocess
import sys
from pathlib import Path

import pytest

from tools.rotate_string import run


@pytest.mark.parametrize(
    "text,n,expected",
    [
        ("abc", "1", "bca"),
        ("abc", "0", "abc"),
        ("abc", "3", "abc"),
        ("abc", "7", "bca"),
        ("abc", "-1", "cab"),
        ("abc", "-7", "cab"),
        ("", "1", ""),
        ("x", "99", "x"),
        (" a b ", "2", " b  a"),
        ("ç🙂ğ", "1", "🙂ğç"),
    ],
)
def test_rotation(text, n, expected):
    assert run(text, n) == expected


@pytest.mark.parametrize("args", [(), ("abc",), ("abc", "1", "extra")])
def test_wrong_argument_count(args):
    assert run(*args) == "Error: expected text and rotation count"


@pytest.mark.parametrize("count", ["", "one", "1.5"])
def test_invalid_rotation_count(count):
    assert run("abc", count) == "Error: rotation count must be an integer"


def test_cli_discovers_rotation_tool():
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "bitbox.py", "rotate_string", "abc", "1"],
        cwd=root,
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "bca"
