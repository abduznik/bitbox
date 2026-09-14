# tool: variance_of_list
# description: Population variance of comma-separated numbers (two decimals)
# author: @00200200
# example: variance_of_list "1,2,3" -> "0.67"

import math
import statistics


def run(*args) -> str:
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")
    numbers = [float(value.strip()) for value in args[0].split(",")]
    if not all(math.isfinite(value) for value in numbers):
        raise ValueError("Numbers must be finite")
    return f"{statistics.pvariance(numbers):.2f}"
