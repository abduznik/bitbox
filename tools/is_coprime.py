# tool: is_coprime
# description: Checks if two integers are coprime
# author: @farukttbasar
# example: run("14", "15") -> "True"
import math

def run(a: str, b: str) -> str:
    try:
        num_a = int(a)
        num_b = int(b)
    except (ValueError, TypeError):
        return "Both arguments must be integers"

    return str(math.gcd(num_a, num_b) == 1)
