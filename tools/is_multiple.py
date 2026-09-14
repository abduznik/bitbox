# tool: is_multiple
# description: Check whether the first integer is a multiple of the second
# author: @00200200
# example: is_multiple "10" "5" -> "True"


def run(*args) -> str:
    if len(args) != 2:
        raise ValueError("Requires exactly two integers")
    number, divisor = (int(value) for value in args)
    if divisor == 0:
        raise ValueError("Divisor must not be zero")
    return str(number % divisor == 0)
