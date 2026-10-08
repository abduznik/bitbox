import pytest
from tools.run_length_encode import run

def test_run_length_encode_example():
    assert run("aaaabbc", "") == "4a2b1c"

def test_run_length_encode_shortened():
    assert run("aaaabbc", "-s") == "4a2bc"