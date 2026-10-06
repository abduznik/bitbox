import pytest
from tools.run_length_encode import run_length_encode

def test_run_length_encode_example():
    assert run_length_encode("aaaabbc", "") == "4a2b1c"

def test_run_length_encode_shortened():
    assert run_length_encode("aaaabbc", "-s") == "4a2bc"