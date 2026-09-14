# tool: is_sorted
# description: Check whether comma-separated numbers are in nondecreasing order
# author: @00200200
# example: is_sorted "1,2,3,4" -> "True"

from decimal import Decimal, InvalidOperation


def run(*args) -> str:
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")
    try:
        numbers = [Decimal(value.strip()) for value in args[0].split(",")]
    except InvalidOperation as exc:
        raise ValueError("Expected comma-separated numbers") from exc
    if not all(value.is_finite() for value in numbers):
        raise ValueError("Numbers must be finite")
    return str(all(left <= right for left, right in zip(numbers, numbers[1:])))
