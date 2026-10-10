# tool: aliquot_sum
# description: Sum of the proper divisors of a number.
# author: @CRYPTONIKAV
# example: aliquot_sum "12" -> "16"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    try:
        n = int(val)
    except ValueError:
        return f"Error: Invalid integer '{val}'."
    if n < 1:
        return "Error: Expected a positive integer."

    total = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i != n:
                total += i
            other = n // i
            if other != i and other != n:
                total += other
        i += 1
    return str(total)
