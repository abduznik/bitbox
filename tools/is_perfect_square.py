# tool: is_perfect_square
# description: Checks if a given number is a perfect square
# author: @navaneethsankar07
# example:  is_perfect_square "16" -> "True"


import math


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    try:
        n = int(args[0])
    except ValueError:
        return "Error: Argument must be an integer."

    if n < 0:
        return "False"

    root = math.isqrt(n)
    return str(root * root == n)
