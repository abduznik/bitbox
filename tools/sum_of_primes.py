# tool: sum_of_primes
# description: Sum all primes up to n
# author: @abduznik
# example: sum_of_primes "10" -> "17"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."
    try:
        n = int(str(args[0]).strip())
    except ValueError:
        return "Error: Argument must be an integer."
    if n < 2:
        return "0"
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return str(sum(i for i, prime in enumerate(is_prime) if prime))
