# tool: goldbach_check
# description: Check if an even number is the sum of two primes
# author: @abduznik
# example: goldbach_check "10" -> "True"


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."
    try:
        n = int(str(args[0]).strip())
    except ValueError:
        return "Error: Argument must be an integer."
    if n < 4 or n % 2:
        return "False"
    for p in range(2, n // 2 + 1):
        if _is_prime(p) and _is_prime(n - p):
            return "True"
    return "False"
