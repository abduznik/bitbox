# tool: lcm_of_list
# description: Least common multiple of comma-separated integers
# author: @00200200
# example: lcm_of_list "4,6" -> "12"

import math


def run(*args) -> str:
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")
    numbers = [int(value.strip()) for value in args[0].split(",")]
    result = 1
    for number in numbers:
        if result == 0 or number == 0:
            result = 0
        else:
            result = abs(result // math.gcd(result, number) * number)
    return str(result)
