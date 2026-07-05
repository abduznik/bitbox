# tool: is_prime
# description: Checks if a number is prime
# author: @its-Sohan
# example: is_prime "7" -> "true"


def run(*args) -> str:
    n = int(args[0])
    if n < 2:
        return "false"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "false"
    return "true"
