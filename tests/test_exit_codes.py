import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_cli(*args):
    return subprocess.run(
        [sys.executable, os.path.join(ROOT, "bitbox.py"), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def test_success_exits_zero_with_output_on_stdout():
    r = run_cli("is_prime", "7")
    assert r.returncode == 0
    assert r.stdout.strip().lower() == "true"
    assert r.stderr == ""


def test_tool_error_string_goes_to_stderr_with_exit_one():
    r = run_cli("is_prime", "abc")
    assert r.returncode == 1
    assert r.stdout == ""
    assert r.stderr.startswith("Error:")


def test_unknown_tool_reports_on_stderr():
    r = run_cli("no_such_tool")
    assert r.returncode == 1
    assert r.stdout == ""
    assert r.stderr.startswith("Error:")


def test_wrong_argument_count_reports_on_stderr():
    r = run_cli("is_prime")
    assert r.returncode == 1
    assert r.stdout == ""
    assert r.stderr.startswith("Error:")
