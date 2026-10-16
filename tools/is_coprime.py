# tool: is_coprime
# description: Checks if two integers are coprime
# author: @farukttbasar
# example: run("14", "15") -> "True"
import math

def run(*args, **kwargs) -> str:
    if kwargs or len(args) != 2:
        return "Error: Exactly two arguments are required"

    try:
        num_a = int(args[0])
        num_b = int(args[1])
    except (ValueError, TypeError):
        return "Error: Both arguments must be integers"

    return str(math.gcd(num_a, num_b) == 1)
