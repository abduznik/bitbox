# tool: is_deficient
# description: Check if a number is deficient (sum of proper divisors < n)
# author: @abduznik
# example: is_deficient "10" -> "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."
    try:
        n = int(str(args[0]).strip())
    except ValueError:
        return "Error: Argument must be an integer."
    if n <= 0:
        return "False"
    total = 0 if n == 1 else 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return str(total < n)
