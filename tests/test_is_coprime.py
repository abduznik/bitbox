import pytest
from tools.is_coprime import run

@pytest.mark.parametrize(
  "a, b, expected",
  [
    ("14", "15", "True"),
    ("8", "9", "True"),
    ("12", "18", "False"),
    ("6", "9", "False"),
  ],
)

def test_is_coprime(a, b, expected):
  assert run(a, b) == expected

@pytest.mark.parametrize(
  "a, b",
  [
    ("x", "2"),
    ("5", "y"),
    ("abc", "xyz"),
    ("", "7"),
  ],
)

def test_invalid_input_returns_error(a, b):
  result = run(a, b)
  assert result.startswith("Error:")
