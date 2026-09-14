# tool: gcd_of_list
# description: Greatest common divisor of comma-separated integers
# author: @00200200
# example: gcd_of_list "12,18,24" -> "6"

import math


def run(*args) -> str:
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")
    numbers = [int(value.strip()) for value in args[0].split(",")]
    result = 0
    for number in numbers:
        result = math.gcd(result, number)
    return str(result)
