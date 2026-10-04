# tool: nth_prime
# description: Find the nth prime number (1-indexed)
# author: @abduznik
# example: nth_prime "5" -> "11"


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
    if n < 1:
        return "Error: argument must be a positive integer."
    found, candidate = 0, 1
    while found < n:
        candidate += 1
        if _is_prime(candidate):
            found += 1
    return str(candidate)
