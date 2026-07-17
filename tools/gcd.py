# tool: gcd
# description: Calculates the greatest common divisor (GCD) of two integers.
# author: @navaneethsankar07
# example: gcd "12" "8" -> "4"


import math


def run(*args) -> str:
    if len(args) != 2:
        return "Error: Please provide exactly two arguments."

    try:
        a = int(args[0])
        b = int(args[1])
    except ValueError:
        return "Error: Arguments must be integers."

    return str(math.gcd(a, b))