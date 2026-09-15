# tool: is_perfect_number
# description: Checks if a number is a perfect number (sum of proper divisors equals n).
# author: @1998LJ
# example: is_perfect_number("6") returns "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    if not val:
        return "Error: Argument cannot be empty."

    try:
        n = int(val)
    except ValueError:
        return "Error: Argument must be an integer."

    if n <= 1:
        return "False"

    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i*i != n:
                divisors_sum += n // i

    return str(divisors_sum == n)
