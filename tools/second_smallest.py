# tool: second_smallest
# description: Second-smallest value in comma-separated numbers
# author: @abduznik
# example: second_smallest "3,1,4,1,5" -> "1"


from decimal import Decimal, InvalidOperation


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."
    try:
        numbers = [Decimal(value.strip()) for value in args[0].split(",")]
    except InvalidOperation:
        return "Error: Expected comma-separated numbers"
    if not all(value.is_finite() for value in numbers):
        return "Error: Numbers must be finite"
    if len(numbers) < 2:
        return "Error: Requires at least two numbers"
    result = sorted(numbers)[1]
    if result == result.to_integral_value():
        return str(int(result))
    return format(result, "f").rstrip("0").rstrip(".")
